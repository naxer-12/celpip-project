import sqlite3
import json
import os
from typing import Dict, Any, List, Optional

def get_db_connection(db_path: str = "celtestpip/data/celtestpip.db") -> sqlite3.Connection:
    dirname = os.path.dirname(db_path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str = "celtestpip/data/celtestpip.db"):
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        total_parts INTEGER DEFAULT 20
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exam_parts (
        id TEXT PRIMARY KEY,
        exam_id TEXT NOT NULL REFERENCES exams(id),
        part_number INTEGER NOT NULL,
        skill TEXT NOT NULL,
        part_name TEXT NOT NULL,
        instructions TEXT,
        audio_urls_json TEXT,
        image_url TEXT,
        transcripts_json TEXT
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        part_id TEXT NOT NULL REFERENCES exam_parts(id),
        question_number INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        audio_url TEXT,
        options_json TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        section INTEGER DEFAULT 1
    );
    """)
    cur.execute("""
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
    # FTS5 index
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS fts_questions USING fts5(
        part_id UNINDEXED,
        question_text,
        options_json,
        explanation
    );
    """)
    conn.commit()
    conn.close()

def insert_exam_part(db_path: str, data: Dict[str, Any], media_map: Optional[Dict[str, str]] = None):
    media_map = media_map or {}
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    
    exam_id = data["exam_id"]
    part_num = data["part_number"]
    part_id = f"{exam_id}_part{part_num}"
    
    cur.execute("INSERT OR IGNORE INTO exams (id, name) VALUES (?, ?)", (exam_id, f"Exam {exam_id.replace('exam', '')}"))
    
    audio_urls = [media_map.get(a, a) for a in (data.get("audio_urls") or [])]
    raw_img = data.get("image_url")
    img = media_map.get(raw_img, raw_img) if raw_img else None
    
    cur.execute("""
    INSERT OR REPLACE INTO exam_parts 
    (id, exam_id, part_number, skill, part_name, instructions, audio_urls_json, image_url, transcripts_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        part_id,
        exam_id,
        part_num,
        data.get("skill", "LISTENING"),
        data.get("part_name", f"Part {part_num}"),
        data.get("instructions", ""),
        json.dumps(audio_urls),
        img,
        json.dumps(data.get("transcripts", []))
    ))
    
    cur.execute("DELETE FROM fts_questions WHERE part_id = ?", (part_id,))

    for q in data.get("questions", []):
        raw_qa = q.get("audio_url")
        qa = media_map.get(raw_qa, raw_qa) if raw_qa else None
        opts_json = json.dumps(q.get("options", []))
        q_text = str(q.get("question_text") or "").strip()
        q_ans = str(q.get("correct_answer") or "").strip()
        q_exp = str(q.get("explanation") or "").strip()
        cur.execute("""
        INSERT OR REPLACE INTO questions 
        (id, part_id, question_number, question_text, audio_url, options_json, correct_answer, explanation, section)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            str(q.get("id") or f"{part_id}_q{q.get('question_number', 1)}"),
            part_id,
            q.get("question_number", 1),
            q_text,
            qa,
            opts_json,
            q_ans,
            q_exp,
            q.get("section", 1)
        ))
        cur.execute("""
        INSERT INTO fts_questions (part_id, question_text, options_json, explanation)
        VALUES (?, ?, ?, ?)
        """, (part_id, q_text, opts_json, q_exp))
        
    conn.commit()
    conn.close()

def get_exam_parts(db_path: str, exam_id: str) -> List[Dict[str, Any]]:
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exam_parts WHERE exam_id = ? ORDER BY part_number ASC", (exam_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]
