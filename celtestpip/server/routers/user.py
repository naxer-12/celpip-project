"""User Profile, Membership, and Practice Credits endpoints.

Provides unlocked mock status so all testers automatically have Pro access
and unlimited credits without requiring external billing or account setup.
"""

from typing import Dict, Any
from fastapi import APIRouter

from celtestpip.server.config import DB_PATH
from celtestpip.server.database import get_db_connection
from celtestpip.server.turso import is_turso_enabled

router = APIRouter(tags=["User"])


@router.get("/api/user/membership")
def get_user_membership() -> Dict[str, Any]:
    """Return active Pro membership details for testing."""
    return {
        "isPremium": True,
        "isPro": True,
        "credits": 9999,
        "user": {
            "id": "tester",
            "email": "tester@celtestpip.local",
            "firstName": "CELPIP",
            "lastName": "Tester",
        },
    }


@router.get("/api/user/credits")
def get_user_credits() -> Dict[str, Any]:
    """Return unlimited test-taker practice credits."""
    return {"credits": 9999, "isPro": True, "isPremium": True}


@router.get("/api/user/sync-status")
def get_sync_status() -> Dict[str, Any]:
    """Report active database mode (Turso Cloud vs local SQLite fallback) and record counts."""
    turso_active = is_turso_enabled()
    attempts_count = 0
    words_count = 0
    try:
        conn = get_db_connection(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM user_attempts")
        attempts_count = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM user_words")
        words_count = cur.fetchone()[0]
        conn.close()
    except Exception:
        pass

    return {
        "mode": "turso" if turso_active else "sqlite_fallback",
        "tursoEnabled": turso_active,
        "localDbPath": DB_PATH,
        "localCounts": {
            "user_attempts": attempts_count,
            "user_words": words_count,
        },
    }
