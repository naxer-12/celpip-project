"""Turso Cloud SQLite Integration.

Enables cloud persistence for user exam attempts and vocabulary words using
Turso's HTTP Pipeline API (libSQL). Requires zero native C/Rust compilation.

When TURSO_DATABASE_URL and TURSO_AUTH_TOKEN are set (e.g., on Render),
user progress is written directly to Turso cloud so it survives container restarts.
When unset, the application falls back seamlessly to local SQLite.
"""

import os
import json
import logging
from typing import Dict, Any, List, Optional
import httpx

logger = logging.getLogger("celtestpip.turso")

TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL", "").strip()
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN", "").strip()


def _get_turso_credentials() -> tuple[str, str]:
    """Read Turso credentials dynamically from environment (supports runtime updates)."""
    url = os.environ.get("TURSO_DATABASE_URL", "").strip()
    token = os.environ.get("TURSO_AUTH_TOKEN", "").strip()
    return url, token


def is_turso_enabled() -> bool:
    """Return True if Turso cloud database credentials are configured."""
    url, token = _get_turso_credentials()
    return bool(url and token)


def _get_turso_pipeline_url() -> str:
    """Convert libsql:// or https:// URL to the /v2/pipeline endpoint."""
    url, _ = _get_turso_credentials()
    if url.startswith("libsql://"):
        url = "https://" + url[len("libsql://"):]
    url = url.rstrip("/")
    if not url.endswith("/v2/pipeline"):
        url = f"{url}/v2/pipeline"
    return url


def execute_turso(sql: str, params: Optional[List[Any]] = None) -> Dict[str, Any]:
    """Execute a single SQL statement against Turso via HTTP Pipeline API."""
    if not is_turso_enabled():
        return {"error": "Turso not enabled"}

    _, token = _get_turso_credentials()
    pipeline_url = _get_turso_pipeline_url()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    args = []
    if params:
        for p in params:
            if p is None:
                args.append({"type": "null"})
            elif isinstance(p, bool):
                args.append({"type": "integer", "value": "1" if p else "0"})
            elif isinstance(p, int):
                args.append({"type": "integer", "value": str(p)})
            elif isinstance(p, float):
                args.append({"type": "float", "value": p})
            else:
                args.append({"type": "text", "value": str(p)})

    payload = {
        "requests": [
            {
                "type": "execute",
                "stmt": {
                    "sql": sql,
                    "args": args,
                },
            },
            {"type": "close"},
        ]
    }

    try:
        with httpx.Client(timeout=8.0) as client:
            resp = client.post(pipeline_url, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                results = data.get("results", [])
                if results and results[0].get("type") == "ok":
                    return results[0].get("response", {}).get("result", {})
            return {"error": f"HTTP {resp.status_code}: {resp.text}"}
    except Exception as e:
        logger.error(f"Failed to execute Turso query: {e}")
        return {"error": str(e)}


def init_turso_tables() -> None:
    """Initialize user progress and vocabulary tables in Turso cloud."""
    if not is_turso_enabled():
        return

    execute_turso("""
    CREATE TABLE IF NOT EXISTS user_attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exam_id TEXT NOT NULL,
        part_number INTEGER NOT NULL,
        score INTEGER NOT NULL,
        total_questions INTEGER NOT NULL,
        clb_estimate INTEGER,
        answers_json TEXT NOT NULL,
        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    execute_turso("""
    CREATE TABLE IF NOT EXISTS user_words (
        id TEXT PRIMARY KEY,
        word TEXT UNIQUE NOT NULL,
        bundle_id TEXT,
        mastered BOOLEAN DEFAULT 0,
        review_count INTEGER DEFAULT 1,
        notes TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_reviewed TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)


def sync_local_to_turso(db_path: str) -> Dict[str, Any]:
    """Push local SQLite user_attempts and user_words rows to Turso cloud."""
    import sqlite3

    if not is_turso_enabled():
        return {"status": "skipped", "reason": "turso_not_configured", "synced_attempts": 0, "synced_words": 0}

    init_turso_tables()
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    synced_words = 0
    synced_attempts = 0
    try:
        cur.execute("SELECT id, word, bundle_id, mastered, review_count, notes, created_at, last_reviewed FROM user_words")
        for row in cur.fetchall():
            res = execute_turso(
                """
                INSERT INTO user_words (id, word, bundle_id, mastered, review_count, notes, created_at, last_reviewed)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(word) DO UPDATE SET
                    mastered = excluded.mastered,
                    review_count = excluded.review_count,
                    notes = excluded.notes,
                    last_reviewed = excluded.last_reviewed
                """,
                [
                    row["id"],
                    row["word"],
                    row["bundle_id"],
                    int(bool(row["mastered"])),
                    row["review_count"],
                    row["notes"],
                    row["created_at"],
                    row["last_reviewed"],
                ],
            )
            if "error" not in res:
                synced_words += 1

        cur.execute("SELECT exam_id, part_number, score, total_questions, clb_estimate, answers_json, completed_at FROM user_attempts")
        for row in cur.fetchall():
            res = execute_turso(
                """
                INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json, completed_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    row["exam_id"],
                    row["part_number"],
                    row["score"],
                    row["total_questions"],
                    row["clb_estimate"],
                    row["answers_json"],
                    row["completed_at"],
                ],
            )
            if "error" not in res:
                synced_attempts += 1
    finally:
        conn.close()

    return {
        "status": "synced",
        "synced_attempts": synced_attempts,
        "synced_words": synced_words,
    }
