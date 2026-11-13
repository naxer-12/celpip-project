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


def is_turso_enabled() -> bool:
    """Return True if Turso cloud database credentials are configured."""
    return bool(TURSO_DATABASE_URL and TURSO_AUTH_TOKEN)


def _get_turso_pipeline_url() -> str:
    """Convert libsql:// or https:// URL to the /v2/pipeline endpoint."""
    url = TURSO_DATABASE_URL
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

    pipeline_url = _get_turso_pipeline_url()
    headers = {
        "Authorization": f"Bearer {TURSO_AUTH_TOKEN}",
        "Content-Type": "application/json",
    }

    args = []
    if params:
        for p in params:
            if p is None:
                args.append({"type": "null"})
            elif isinstance(p, int):
                args.append({"type": "integer", "value": str(p)})
            elif isinstance(p, float):
                args.append({"type": "float", "value": p})
            elif isinstance(p, bool):
                args.append({"type": "integer", "value": "1" if p else "0"})
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
