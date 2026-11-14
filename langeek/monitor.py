"""
LanGeek Continuous Crawling & Change Monitoring Agent
Provides persistent URL inventory tracking, diff detection, and administrator reporting.
"""

import hashlib
import json
import logging
import re
import sqlite3
import time
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
import httpx

logger = logging.getLogger("langeek.monitor")
DB_PATH = "langeek/data/langeek.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_monitor_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS crawl_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            category TEXT,
            status_code INTEGER,
            title TEXT,
            content_hash TEXT,
            previous_hash TEXT,
            content_length INTEGER,
            change_detected INTEGER DEFAULT 0,
            diff_summary TEXT,
            last_crawled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS monitor_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            reference_url TEXT,
            change_category TEXT,
            suggested_action TEXT,
            priority TEXT DEFAULT 'normal',
            status TEXT DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS monitor_config (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    # Set default config
    cur.execute("INSERT OR IGNORE INTO monitor_config (key, value) VALUES ('interval_hours', '12')")
    cur.execute("INSERT OR IGNORE INTO monitor_config (key, value) VALUES ('status', 'active')")
    cur.execute("INSERT OR IGNORE INTO monitor_config (key, value) VALUES ('last_run', ?)", (datetime.now(timezone.utc).isoformat(),))
    conn.commit()
    conn.close()


async def run_crawl_cycle() -> Dict[str, Any]:
    """Execute a single crawl pass across all monitored URLs, detecting changes."""
    init_monitor_tables()
    conn = get_db()
    cur = conn.cursor()
    urls = cur.execute("SELECT id, url, category, content_hash FROM crawl_snapshots").fetchall()

    results = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_monitored": len(urls),
        "crawled": 0,
        "changed": 0,
        "failed": 0,
        "details": []
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9"
    }

    async with httpx.AsyncClient(verify=False, timeout=15.0) as client:
        for row in urls:
            row_id = row['id']
            url = row['url']
            old_hash = row['content_hash']
            try:
                resp = await client.get(url, headers=headers)
                results["crawled"] += 1

                # Extract title
                title_match = re.search(r'<title>(.*?)</title>', resp.text, re.IGNORECASE)
                title = title_match.group(1).strip() if title_match else url

                # Normalize content by removing dynamic timestamp/token attributes
                normalized = re.sub(r'data-syncdate="[^"]*"', '', resp.text)
                normalized = re.sub(r'<script[^>]*__NEXT_DATA__[^>]*>.*?</script>', '', normalized)
                new_hash = hashlib.sha256(normalized.encode('utf-8')).hexdigest()

                change_detected = 1 if (old_hash and old_hash != 'init_hash' and old_hash != new_hash) else 0
                diff_summary = ""

                if change_detected:
                    results["changed"] += 1
                    diff_summary = f"Content hash updated from {old_hash[:8]} to {new_hash[:8]} (Length: {len(resp.text)} bytes)"
                    # Create monitor task
                    cur.execute("""
                        INSERT INTO monitor_tasks (reference_url, change_category, suggested_action, priority, status)
                        VALUES (?, 'DOM Content Shift', ?, 'high', 'pending')
                    """, (url, diff_summary))

                cur.execute("""
                    UPDATE crawl_snapshots
                    SET status_code = ?, title = ?, content_hash = ?, previous_hash = ?,
                        content_length = ?, change_detected = ?, diff_summary = ?, last_crawled_at = CURRENT_TIMESTAMP
                    WHERE id = ?
                """, (resp.status_code, title, new_hash, old_hash, len(resp.text), change_detected, diff_summary, row_id))

                results["details"].append({
                    "url": url,
                    "status_code": resp.status_code,
                    "changed": bool(change_detected),
                    "title": title
                })

            except Exception as e:
                results["failed"] += 1
                logger.warning(f"Error crawling {url}: {e}")
                results["details"].append({"url": url, "error": str(e)})

    # Update last_run config
    cur.execute("UPDATE monitor_config SET value = ? WHERE key = 'last_run'", (datetime.now(timezone.utc).isoformat(),))
    conn.commit()
    conn.close()

    return results


def get_monitor_stats() -> Dict[str, Any]:
    """Return aggregated status for Administrator Dashboard."""
    init_monitor_tables()
    conn = get_db()
    cur = conn.cursor()

    total_monitored = cur.execute("SELECT count(*) FROM crawl_snapshots").fetchone()[0]
    total_changed = cur.execute("SELECT count(*) FROM crawl_snapshots WHERE change_detected = 1").fetchone()[0]
    pending_tasks = cur.execute("SELECT count(*) FROM monitor_tasks WHERE status = 'pending'").fetchone()[0]
    completed_tasks = cur.execute("SELECT count(*) FROM monitor_tasks WHERE status = 'completed'").fetchone()[0]

    last_run_row = cur.execute("SELECT value FROM monitor_config WHERE key = 'last_run'").fetchone()
    last_run = last_run_row[0] if last_run_row else "Never"

    interval_row = cur.execute("SELECT value FROM monitor_config WHERE key = 'interval_hours'").fetchone()
    interval_hours = int(interval_row[0]) if interval_row else 12

    snapshots = cur.execute("""
        SELECT id, url, category, status_code, title, content_length, change_detected, diff_summary, last_crawled_at
        FROM crawl_snapshots
        ORDER BY last_crawled_at DESC
        LIMIT 20
    """).fetchall()

    tasks = cur.execute("""
        SELECT id, reference_url, change_category, suggested_action, priority, status, created_at
        FROM monitor_tasks
        ORDER BY created_at DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    return {
        "total_monitored": total_monitored,
        "total_changed": total_changed,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "last_run": last_run,
        "interval_hours": interval_hours,
        "snapshots": [dict(s) for s in snapshots],
        "tasks": [dict(t) for t in tasks]
    }
