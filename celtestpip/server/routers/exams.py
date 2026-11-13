"""Exams API and Simulator endpoints.

Provides listing of exams (exam1-exam60), exam part details (audio, images,
instructions, transcripts, questions), full-text question search, and scoring attempts.
"""

import json
import sqlite3
from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException

from celtestpip.server.config import DB_PATH, normalize_exam_id
from celtestpip.server.database import get_db_connection
from celtestpip.server.models import AttemptSubmission
from celtestpip.server.scoring import raw_score_to_clb
from celtestpip.server.turso import is_turso_enabled, execute_turso

router = APIRouter(tags=["Exams"])


@router.get("/api/exams")
def get_all_exams() -> List[Dict[str, Any]]:
    """Return all available exams with total parts count."""
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT id, name, total_parts FROM exams ORDER BY id ASC")
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


@router.get("/api/exams/{exam_id}/part/{part_number}")
def get_exam_part_data(exam_id: str, part_number: int) -> Dict[str, Any]:
    """Retrieve full test data for a single exam part, including questions and audio."""
    exam_id = normalize_exam_id(exam_id)
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    part_id = f"{exam_id}_part{part_number}"
    cur.execute("SELECT * FROM exam_parts WHERE id = ?", (part_id,))
    part_row = cur.fetchone()
    if not part_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Exam part not found")

    cur.execute("SELECT * FROM questions WHERE part_id = ? ORDER BY question_number ASC", (part_id,))
    q_rows = cur.fetchall()
    conn.close()

    questions = []
    for q in q_rows:
        qd = dict(q)
        qd["options"] = json.loads(qd.get("options_json") or "[]")
        qd.pop("options_json", None)
        questions.append(qd)

    res = dict(part_row)
    res["audio_urls"] = json.loads(res.get("audio_urls_json") or "[]")
    res["transcripts"] = json.loads(res.get("transcripts_json") or "[]")
    res.pop("audio_urls_json", None)
    res.pop("transcripts_json", None)
    res["questions"] = questions
    return res


@router.get("/api/exams/{exam_id}")
@router.get("/api/exams/{exam_id}/parts")
def get_exam_parts_list(exam_id: str) -> List[Dict[str, Any]]:
    """Return summary list of all parts belonging to an exam."""
    exam_id = normalize_exam_id(exam_id)
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exam_parts WHERE exam_id = ? ORDER BY part_number ASC", (exam_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]


@router.post("/api/attempts")
def save_attempt(attempt: AttemptSubmission) -> Dict[str, Any]:
    """Save user exam attempt and compute Canadian Language Benchmark (CLB) estimate."""
    exam_id = normalize_exam_id(attempt.exam_id)
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    part_id = f"{exam_id}_part{attempt.part_number}"
    cur.execute("SELECT skill FROM exam_parts WHERE id = ?", (part_id,))
    row = cur.fetchone()
    skill = row["skill"] if row else "LISTENING"

    clb = attempt.clb_estimate if attempt.clb_estimate is not None else raw_score_to_clb(skill, attempt.score)
    cur.execute("""
    INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (exam_id, attempt.part_number, attempt.score, attempt.total_questions, clb, json.dumps(attempt.answers)))
    conn.commit()
    conn.close()

    # If Turso cloud database is enabled, persist attempt to cloud
    if is_turso_enabled():
        try:
            execute_turso("""
            INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json)
            VALUES (?, ?, ?, ?, ?, ?)
            """, [exam_id, attempt.part_number, attempt.score, attempt.total_questions, clb, json.dumps(attempt.answers)])
        except Exception:
            pass

    return {"status": "saved", "clb": clb}


@router.get("/api/search")
def search_questions(q: str) -> List[Dict[str, Any]]:
    """Full-text search (FTS5) across all questions, options, and explanations."""
    if not q or not q.strip():
        return []
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    clean_q = "".join(c for c in q if c.isalnum() or c.isspace()).strip()
    if not clean_q:
        conn.close()
        return []
    match_query = f"{clean_q}*"
    try:
        cur.execute("""
        SELECT part_id, question_text, explanation FROM fts_questions 
        WHERE fts_questions MATCH ? LIMIT 50
        """, (match_query,))
        rows = cur.fetchall()
    except (sqlite3.OperationalError, Exception):
        rows = []
    finally:
        conn.close()
    return [dict(r) for r in rows]
