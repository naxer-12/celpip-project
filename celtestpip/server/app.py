import os
import json
import sqlite3
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from celtestpip.server.database import get_db_connection, init_db
from celtestpip.server.scoring import raw_score_to_clb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "data", "media")
DB_PATH = os.environ.get("CELTESTPIP_DB_PATH", os.path.join(BASE_DIR, "data", "celtestpip.db"))

def ensure_db():
    if not os.path.exists(DB_PATH):
        init_db(DB_PATH)

ensure_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_db()
    yield

app = FastAPI(
    title="CELTESTPIP Local Replica",
    description="Offline CELPIP Practice & Mock Exam Simulator",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static mounting
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
CURSORS_DIR = os.path.join(STATIC_DIR, "cursors")
os.makedirs(CURSORS_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")
app.mount("/cursors", StaticFiles(directory=CURSORS_DIR), name="cursors")

@app.get("/favicon.ico")
def get_favicon():
    fav = os.path.join(STATIC_DIR, "img", "favicon.ico")
    if os.path.exists(fav):
        return FileResponse(fav)
    raise HTTPException(status_code=404)

@app.get("/logo.png")
def get_logo():
    logo = os.path.join(STATIC_DIR, "img", "logo.png")
    if os.path.exists(logo):
        return FileResponse(logo)
    raise HTTPException(status_code=404)

@app.get("/_next/image")
def get_next_image(url: str = "/logo.png"):
    if "logo" in url:
        return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"))
    if "icon" in url:
        return FileResponse(os.path.join(STATIC_DIR, "img", "icon.png"))
    return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"))

class AttemptSubmission(BaseModel):
    exam_id: str
    part_number: int
    answers: Dict[str, str]
    score: int
    total_questions: int
    clb_estimate: Optional[int] = None

@app.get("/api/exams")
def get_all_exams():
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exams ORDER BY CAST(SUBSTR(id, 5) AS INTEGER) ASC")
    exams = [dict(r) for r in cur.fetchall()]
    conn.close()
    return exams

@app.get("/api/exams/{exam_id}/part/{part_number}")
def get_exam_part_data(exam_id: str, part_number: int):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    part_id = f"{exam_id}_part{part_number}"
    cur.execute("SELECT * FROM exam_parts WHERE id = ?", (part_id,))
    part = cur.fetchone()
    if not part:
        conn.close()
        raise HTTPException(status_code=404, detail="Exam part not found")
        
    part_dict = dict(part)
    part_dict["audio_urls"] = json.loads(part_dict.get("audio_urls_json") or "[]")
    part_dict["transcripts"] = json.loads(part_dict.get("transcripts_json") or "[]")
    
    cur.execute("SELECT * FROM questions WHERE part_id = ? ORDER BY question_number ASC", (part_id,))
    questions = []
    for q in cur.fetchall():
        qd = dict(q)
        qd["options"] = json.loads(qd["options_json"])
        questions.append(qd)
    part_dict["questions"] = questions
    conn.close()
    return part_dict

@app.post("/api/attempts")
def save_attempt(attempt: AttemptSubmission):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        attempt.exam_id,
        attempt.part_number,
        attempt.score,
        attempt.total_questions,
        attempt.clb_estimate,
        json.dumps(attempt.answers)
    ))
    conn.commit()
    conn.close()
    return {"status": "saved", "clb": attempt.clb_estimate}

@app.get("/api/search")
def search_questions(q: str):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    try:
        cur.execute("""
        SELECT part_id, question_text, explanation FROM fts_questions 
        WHERE fts_questions MATCH ? LIMIT 20
        """, (f"{q}*",))
        results = [dict(r) for r in cur.fetchall()]
    except sqlite3.OperationalError:
        results = []
    finally:
        conn.close()
    return results

@app.get("/", response_class=HTMLResponse)
def index_page():
    index_html = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_html):
        with open(index_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CELTESTPIP Local Server Running</h1><p>Frontend template ready at /static/index.html</p>"

@app.get("/exams", response_class=HTMLResponse)
def exams_catalog_page():
    exams_html = os.path.join(STATIC_DIR, "exams.html")
    if os.path.exists(exams_html):
        with open(exams_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CELTESTPIP Exams Catalog</h1>"

@app.get("/exams/{exam_id}", response_class=HTMLResponse)
def exam_landing_page(exam_id: str):
    return exam_page(exam_id, 1)

@app.get("/exams/{exam_id}/part{part_number}", response_class=HTMLResponse)
def exam_page_slug(exam_id: str, part_number: int):
    return exam_page(exam_id, part_number)

@app.get("/exams/{exam_id}/part/{part_number}", response_class=HTMLResponse)
def exam_page(exam_id: str, part_number: int):
    exam_html = os.path.join(STATIC_DIR, "exam.html")
    if os.path.exists(exam_html):
        with open(exam_html, "r", encoding="utf-8") as f:
            return f.read()
    index_html = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return "<h1>CELTESTPIP Exam Page</h1>"

@app.get("/tools/clb-calculator", response_class=HTMLResponse)
def calculator_page():
    calc_html = os.path.join(STATIC_DIR, "calculator.html")
    if os.path.exists(calc_html):
        with open(calc_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CLB Calculator</h1>"
