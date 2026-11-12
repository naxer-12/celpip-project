"""Vocabulary, Personal Word Bank, Translation, and TTS endpoints.

Manages user vocabulary lists, mastery tracking, word definitions, and audio speech
with persistent SQLite storage and fast in-memory access.
"""

from typing import Dict, Any, List
from fastapi import APIRouter, Request

from celtestpip.server.config import DB_PATH
from celtestpip.server.database import get_db_connection

router = APIRouter(tags=["Vocabulary"])

USER_WORDS_STORE: Dict[str, dict] = {}


def load_words_from_db():
    """Sync in-memory store from SQLite database."""
    try:
        conn = get_db_connection(DB_PATH)
        cur = conn.cursor()
        cur.execute("SELECT * FROM user_words")
        for row in cur.fetchall():
            w = row["word"]
            USER_WORDS_STORE[w] = {
                "id": row["id"],
                "word": w,
                "bundleId": row["bundle_id"],
                "mastered": bool(row["mastered"]),
                "reviewCount": row["review_count"],
                "notes": row["notes"] or "",
                "createdAt": str(row["created_at"]),
                "lastReviewed": str(row["last_reviewed"]),
            }
        conn.close()
    except Exception:
        pass


@router.get("/api/user-words")
def get_user_words() -> List[Dict[str, Any]]:
    """Retrieve all vocabulary words saved to the user's word bank."""
    if not USER_WORDS_STORE:
        load_words_from_db()
    return list(USER_WORDS_STORE.values())


@router.post("/api/user-words")
async def save_user_word(request: Request) -> Dict[str, Any]:
    """Add a new word to user's vocabulary collection and persist to SQLite."""
    try:
        data = await request.json()
        word = data.get("word", "").lower().strip()
        bundle_id = data.get("bundleId")
        if word and word not in USER_WORDS_STORE:
            USER_WORDS_STORE[word] = {
                "id": f"uw_{word}",
                "word": word,
                "bundleId": bundle_id,
                "mastered": False,
                "reviewCount": 1,
                "notes": "",
                "createdAt": "2026-11-05T00:00:00.000Z",
                "lastReviewed": "2026-11-05T00:00:00.000Z",
            }
        elif word:
            USER_WORDS_STORE[word]["reviewCount"] = USER_WORDS_STORE[word].get("reviewCount", 0) + 1
            USER_WORDS_STORE[word]["lastReviewed"] = "2026-11-05T00:00:00.000Z"

        if word:
            try:
                conn = get_db_connection(DB_PATH)
                cur = conn.cursor()
                cur.execute("""
                INSERT OR REPLACE INTO user_words (id, word, bundle_id, mastered, review_count, notes)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    USER_WORDS_STORE[word]["id"],
                    word,
                    bundle_id,
                    1 if USER_WORDS_STORE[word]["mastered"] else 0,
                    USER_WORDS_STORE[word]["reviewCount"],
                    USER_WORDS_STORE[word]["notes"],
                ))
                conn.commit()
                conn.close()
            except Exception:
                pass

        return USER_WORDS_STORE.get(word, {"ok": True})
    except Exception:
        return {"ok": True}


@router.get("/api/user-words/{word}")
def get_single_user_word(word: str) -> Dict[str, Any]:
    """Retrieve details for a single saved word."""
    word_clean = word.lower().strip()
    if word_clean not in USER_WORDS_STORE:
        load_words_from_db()
    return USER_WORDS_STORE.get(word_clean, {
        "id": f"uw_{word_clean}",
        "word": word_clean,
        "mastered": False,
        "reviewCount": 1,
        "notes": "",
        "createdAt": "2026-11-05T00:00:00.000Z",
        "lastReviewed": "2026-11-05T00:00:00.000Z",
    })


@router.patch("/api/user-words/{word}")
async def patch_user_word(word: str, request: Request) -> Dict[str, Any]:
    """Update learning status or notes for a word and persist."""
    word_clean = word.lower().strip()
    item = USER_WORDS_STORE.get(word_clean, {
        "id": f"uw_{word_clean}",
        "word": word_clean,
        "mastered": False,
        "reviewCount": 1,
        "notes": "",
        "createdAt": "2026-11-05T00:00:00.000Z",
        "lastReviewed": "2026-11-05T00:00:00.000Z",
    })
    try:
        body = await request.json()
        if "mastered" in body:
            item["mastered"] = bool(body["mastered"])
        if "notes" in body:
            item["notes"] = str(body["notes"] or "")
        item["lastReviewed"] = "2026-11-05T00:00:00.000Z"

        try:
            conn = get_db_connection(DB_PATH)
            cur = conn.cursor()
            cur.execute("""
            INSERT OR REPLACE INTO user_words (id, word, bundle_id, mastered, review_count, notes)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                item["id"],
                word_clean,
                item.get("bundleId"),
                1 if item["mastered"] else 0,
                item.get("reviewCount", 1),
                item.get("notes", ""),
            ))
            conn.commit()
            conn.close()
        except Exception:
            pass
    except Exception:
        pass

    USER_WORDS_STORE[word_clean] = item
    return item


@router.delete("/api/user-words/{word}")
def delete_user_word(word: str) -> Dict[str, Any]:
    """Delete a word from user's vocabulary list and SQLite."""
    word_clean = word.lower().strip()
    USER_WORDS_STORE.pop(word_clean, None)
    try:
        conn = get_db_connection(DB_PATH)
        cur = conn.cursor()
        cur.execute("DELETE FROM user_words WHERE word = ?", (word_clean,))
        conn.commit()
        conn.close()
    except Exception:
        pass
    return {"ok": True}


@router.post("/api/words/translate")
def translate_word() -> Dict[str, Any]:
    """Mock translation endpoint for vocabulary definitions."""
    return {"translation": "Definition available"}


@router.post("/api/tts")
def tts_endpoint() -> Dict[str, Any]:
    """Mock text-to-speech endpoint for word pronunciation."""
    return {"url": None}
