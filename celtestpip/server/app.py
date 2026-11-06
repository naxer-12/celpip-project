import os
import json
import sqlite3
import mimetypes
from contextlib import asynccontextmanager
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel

from celtestpip.server.database import get_db_connection, init_db
from celtestpip.server.scoring import raw_score_to_clb
from celtestpip.scripts.unlock_all_pro_content import clean_html

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "data", "media")
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
NEXT_STATIC_DIR = os.path.join(STATIC_DIR, "_next", "static")
ANIMATION_DIR = os.path.join(STATIC_DIR, "animation")
DB_PATH = os.environ.get("CELTESTPIP_DB_PATH", os.path.join(BASE_DIR, "data", "celtestpip.db"))

PAGE_CACHE: Dict[str, str] = {}

def normalize_exam_id(exam_id: str) -> str:
    if not exam_id.startswith("exam") and exam_id.isdigit():
        return f"exam{exam_id}"
    return exam_id

def ensure_db():
    if not os.path.exists(DB_PATH):
        init_db(DB_PATH)

def prewarm_page_cache():
    for fn in ["index.html", "exams.html", "exam.html", "calculator.html"]:
        p = os.path.join(STATIC_DIR, fn)
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    PAGE_CACHE[fn] = clean_html(f.read())
            except Exception:
                pass

ensure_db()

@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_db()
    prewarm_page_cache()
    yield

app = FastAPI(
    title="CELTESTPIP Local Replica",
    description="Offline CELPIP Practice & Mock Exam Simulator",
    lifespan=lifespan,
)

# GZip compression (reduces payload sizes by 85-93%)
app.add_middleware(GZipMiddleware, minimum_size=1000)

class HeadMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "HEAD":
            request.scope["method"] = "GET"
            response = await call_next(request)
            return Response(status_code=response.status_code, headers=dict(response.headers))
        return await call_next(request)

app.add_middleware(HeadMiddleware)

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
os.makedirs(PAGES_DIR, exist_ok=True)
os.makedirs(NEXT_STATIC_DIR, exist_ok=True)
os.makedirs(ANIMATION_DIR, exist_ok=True)
CURSORS_DIR = os.path.join(STATIC_DIR, "cursors")
AVATAR_DIR = os.path.join(STATIC_DIR, "img", "avatar")
os.makedirs(CURSORS_DIR, exist_ok=True)
os.makedirs(AVATAR_DIR, exist_ok=True)

MEDIA_CACHE_DIR = os.path.join(MEDIA_DIR, "cache")
os.makedirs(MEDIA_CACHE_DIR, exist_ok=True)

IMMUTABLE_HEADERS = {"Cache-Control": "public, max-age=31536000, immutable"}
STATIC_HEADERS = {"Cache-Control": "public, max-age=86400"}
PAGE_HEADERS = {"Cache-Control": "no-cache, must-revalidate"}

@app.get("/media/{file_path:path}")
def serve_media(file_path: str):
    import re, ssl, urllib.request
    # 1. Check local media dir directly
    local_path = os.path.join(MEDIA_DIR, file_path)
    if os.path.exists(local_path) and os.path.isfile(local_path):
        return FileResponse(local_path, headers=STATIC_HEADERS)
    
    # 2. Check cache
    safe_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', file_path)
    cache_path = os.path.join(MEDIA_CACHE_DIR, safe_name)
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
        return FileResponse(cache_path, headers=STATIC_HEADERS)
    
    # 3. Fetch from remote blob storage
    remote_url = f"https://u108saydmkdhqew3.public.blob.vercel-storage.com/{file_path}"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(remote_url, headers={"User-Agent": "Mozilla/5.0 (CELTESTPIP Replica)"})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            content = resp.read()
            with open(cache_path, "wb") as f:
                f.write(content)
            content_type = resp.headers.get("Content-Type", "audio/mpeg" if file_path.endswith(".mp3") else "image/jpeg")
            return Response(content=content, media_type=content_type, headers=STATIC_HEADERS)
    except Exception:
        raise HTTPException(status_code=404, detail="Media asset not found")

@app.get("/_next/static/{file_path:path}")
def serve_next_static(file_path: str):
    import re, ssl, urllib.request
    is_immutable = "immutable" in file_path
    headers = IMMUTABLE_HEADERS if is_immutable else STATIC_HEADERS

    local_file = os.path.join(NEXT_STATIC_DIR, file_path)
    if os.path.exists(local_file) and os.path.isfile(local_file):
        return FileResponse(local_file, headers=headers)
    
    # Check in static/css or static/js or static/fonts or static/img
    base_name = os.path.basename(file_path)
    for sub in ["css", "js", "fonts", "img"]:
        cand = os.path.join(STATIC_DIR, sub, base_name)
        if os.path.exists(cand) and os.path.isfile(cand):
            return FileResponse(cand, headers=headers)
    
    # Fetch from celtestpip.com
    remote_url = f"https://www.celtestpip.com/_next/static/{file_path}"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(remote_url, headers={"User-Agent": "Mozilla/5.0 (CELTESTPIP Replica)"})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            content = resp.read()
            os.makedirs(os.path.dirname(local_file), exist_ok=True)
            with open(local_file, "wb") as f:
                f.write(content)
            content_type, _ = mimetypes.guess_type(local_file)
            if not content_type:
                if file_path.endswith(".css"):
                    content_type = "text/css"
                elif file_path.endswith(".js"):
                    content_type = "application/javascript"
                elif file_path.endswith(".woff2"):
                    content_type = "font/woff2"
                else:
                    content_type = "application/octet-stream"
            return Response(content=content, media_type=content_type, headers=headers)
    except Exception:
        raise HTTPException(status_code=404, detail="Next static asset not found")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/cursors", StaticFiles(directory=CURSORS_DIR), name="cursors")
app.mount("/avatar", StaticFiles(directory=AVATAR_DIR), name="avatar")
app.mount("/animation", StaticFiles(directory=ANIMATION_DIR), name="animation")

@app.get("/manifest.webmanifest")
def get_manifest():
    mf = os.path.join(STATIC_DIR, "manifest.webmanifest")
    if os.path.exists(mf):
        return FileResponse(mf, media_type="application/manifest+json", headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)

@app.get("/icon.png")
@app.get("/apple-icon.png")
def get_icon():
    p = os.path.join(STATIC_DIR, "img", "icon.png")
    if os.path.exists(p):
        return FileResponse(p, media_type="image/png", headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)

@app.get("/favicon.ico")
def get_favicon():
    fav = os.path.join(STATIC_DIR, "img", "favicon.ico")
    if os.path.exists(fav):
        return FileResponse(fav, headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)

@app.get("/logo.png")
def get_logo():
    logo = os.path.join(STATIC_DIR, "img", "logo.png")
    if os.path.exists(logo):
        return FileResponse(logo, headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)

@app.get("/_next/image")
def get_next_image(url: str = "/logo.png", w: Optional[int] = None, q: Optional[int] = None):
    import re, urllib.request
    if "avatar" in url:
        m = re.search(r'(\d+)\.jpg', url)
        if m:
            av_path = os.path.join(AVATAR_DIR, f"{m.group(1)}.jpg")
            if os.path.exists(av_path):
                return FileResponse(av_path)
    if "logo" in url:
        return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"))
    if "icon" in url:
        return FileResponse(os.path.join(STATIC_DIR, "img", "icon.png"))

    if url.startswith("http://") or url.startswith("https://"):
        safe_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', url)
        cache_path = os.path.join(MEDIA_CACHE_DIR, safe_name)
        if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
            return FileResponse(cache_path)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (CELTESTPIP Replica)"})
            with urllib.request.urlopen(req, timeout=12) as resp:
                content = resp.read()
                with open(cache_path, "wb") as f:
                    f.write(content)
                content_type = resp.headers.get("Content-Type", "image/jpeg")
                return Response(content=content, media_type=content_type)
        except Exception:
            return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"))

    if url.startswith("/media/"):
        return serve_media(url.replace("/media/", ""))

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
    exam_id = normalize_exam_id(exam_id)
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

@app.get("/api/exams/{exam_id}")
@app.get("/api/exams/{exam_id}/parts")
def get_exam_parts_list(exam_id: str):
    exam_id = normalize_exam_id(exam_id)
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exam_parts WHERE exam_id = ? ORDER BY part_number ASC", (exam_id,))
    parts = [dict(r) for r in cur.fetchall()]
    conn.close()
    if not parts:
        raise HTTPException(status_code=404, detail="Exam not found")
    return parts

@app.post("/api/attempts")
def save_attempt(attempt: AttemptSubmission):
    exam_id = normalize_exam_id(attempt.exam_id)
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        exam_id,
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

# --- Pro & Assessment Mock APIs ---
@app.get("/api/user/membership")
def get_user_membership():
    return {
        "isPremium": True,
        "isPro": True,
        "credits": 9999,
        "user": {
            "id": "tester",
            "email": "tester@celtestpip.local",
            "firstName": "CELPIP",
            "lastName": "Tester"
        }
    }

@app.get("/api/user/credits")
def get_user_credits():
    return {"credits": 9999, "isPro": True, "isPremium": True}

@app.put("/api/practices/{practice_id}/done")
@app.post("/api/practices/{practice_id}/done")
def mark_practice_done(practice_id: str):
    return {"status": "ok", "practiceId": practice_id, "isCompleted": True}

@app.get("/api/practices/{practice_id}/result")
def get_practice_result(practice_id: str):
    return {"result": {"score": 8, "total": 8, "percentage": 100}}

@app.put("/api/practices/{practice_id}/explanation")
@app.post("/api/practices/{practice_id}/explanation")
def unlock_practice_explanation(practice_id: str):
    return {"result": {"explanation": "Explanations unlocked for testing."}}

@app.post("/api/practices/{practice_id}/answer")
def record_practice_answer(practice_id: str):
    return {"status": "ok"}

@app.post("/api/question")
async def record_question_answer(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}
    return {
        "ok": True,
        "status": "ok",
        "questionId": data.get("questionId"),
        "answer": data.get("answer")
    }

@app.post("/api/questions/report")
async def report_question(request: Request):
    return {"ok": True, "status": "ok"}

@app.post("/api/writing")
@app.post("/api/writing/update")
async def handle_writing_submit(request: Request):
    return {
        "id": "mock_writing_submit_1",
        "score": 10,
        "clb": 10,
        "wordCount": 185,
        "feedback": "Strong lexical variety, clear coherence, accurate paragraph transitions, and task fulfillment.",
        "corrected": "Excellent draft. Minor stylistic tweaks applied.",
        "createdAt": "2026-11-05T20:00:00Z"
    }

@app.post("/api/speaking")
@app.post("/api/speaking/update")
async def handle_speaking_submit(request: Request):
    return {
        "id": "mock_speaking_submit_1",
        "score": 10,
        "clb": 10,
        "fluency": "High",
        "pronunciation": "Clear",
        "vocabulary": "Advanced",
        "feedback": "Natural pace, coherent structure, varied vocabulary, and clear speech delivery.",
        "createdAt": "2026-11-05T20:00:00Z"
    }

USER_WORDS_STORE: Dict[str, dict] = {}

@app.get("/api/user-words")
def get_user_words():
    return list(USER_WORDS_STORE.values())

@app.post("/api/user-words")
async def save_user_word(request: Request):
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
                "lastReviewed": "2026-11-05T00:00:00.000Z"
            }
        elif word:
            USER_WORDS_STORE[word]["reviewCount"] = USER_WORDS_STORE[word].get("reviewCount", 0) + 1
            USER_WORDS_STORE[word]["lastReviewed"] = "2026-11-05T00:00:00.000Z"
        return USER_WORDS_STORE.get(word, {"ok": True})
    except Exception:
        return {"ok": True}

@app.get("/api/user-words/{word}")
def get_single_user_word(word: str):
    word_clean = word.lower().strip()
    return USER_WORDS_STORE.get(word_clean, {
        "id": f"uw_{word_clean}",
        "word": word_clean,
        "mastered": False,
        "reviewCount": 1,
        "notes": "",
        "createdAt": "2026-11-05T00:00:00.000Z",
        "lastReviewed": "2026-11-05T00:00:00.000Z"
    })

@app.patch("/api/user-words/{word}")
async def patch_user_word(word: str, request: Request):
    word_clean = word.lower().strip()
    item = USER_WORDS_STORE.get(word_clean, {
        "id": f"uw_{word_clean}",
        "word": word_clean,
        "mastered": False,
        "reviewCount": 1,
        "notes": "",
        "createdAt": "2026-11-05T00:00:00.000Z",
        "lastReviewed": "2026-11-05T00:00:00.000Z"
    })
    try:
        body = await request.json()
        if "mastered" in body:
            item["mastered"] = bool(body["mastered"])
        if "notes" in body:
            item["notes"] = str(body["notes"] or "")
        item["lastReviewed"] = "2026-11-05T00:00:00.000Z"
    except Exception:
        pass
    USER_WORDS_STORE[word_clean] = item
    return item

@app.delete("/api/user-words/{word}")
def delete_user_word(word: str):
    word_clean = word.lower().strip()
    USER_WORDS_STORE.pop(word_clean, None)
    return {"ok": True}

@app.post("/api/words/translate")
def translate_word():
    return {"translation": "Definition available"}

@app.post("/api/tts")
def tts_endpoint():
    return {"url": None}

# --- Clerk Local Mock Endpoints to prevent external network latency and polling jank ---
@app.get("/v1/client")
@app.post("/v1/client")
@app.get("/v1/client/{subpath:path}")
@app.post("/v1/client/{subpath:path}")
def mock_clerk_client():
    return {
        "response": {
            "status": "ok",
            "client": {
                "id": "client_tester",
                "sessions": [
                    {
                        "id": "sess_tester",
                        "status": "active",
                        "user": {
                            "id": "tester",
                            "primaryEmailAddress": {"emailAddress": "tester@celtestpip.local"}
                        }
                    }
                ],
                "lastActiveSessionId": "sess_tester"
            }
        }
    }

@app.get("/v1/environment")
@app.get("/v1/environment/{subpath:path}")
def mock_clerk_environment():
    return {
        "authConfig": {"singleSessionMode": True},
        "userSettings": {},
        "displayConfig": {}
    }

def get_cached_template(filename: str) -> str:
    if filename in PAGE_CACHE:
        return PAGE_CACHE[filename]
    p = os.path.join(STATIC_DIR, filename)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f:
            content = clean_html(f.read())
        PAGE_CACHE[filename] = content
        return content
    return ""

@app.get("/", response_class=HTMLResponse)
def index_page():
    content = get_cached_template("index.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Local Server Running</h1><p>Frontend template ready at /static/index.html</p>", headers=PAGE_HEADERS)

@app.get("/exams", response_class=HTMLResponse)
def exams_catalog_page():
    content = get_cached_template("exams.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exams Catalog</h1>", headers=PAGE_HEADERS)

@app.get("/exams/{exam_id}", response_class=HTMLResponse)
def exam_landing_page(exam_id: str):
    exam_id = normalize_exam_id(exam_id)
    return exam_page(exam_id, 1)

@app.get("/exams/{exam_id}/results", response_class=HTMLResponse)
def exam_results_page(exam_id: str, partNumber: Optional[str] = None):
    exam_id = normalize_exam_id(exam_id)
    content = get_cached_template("exam.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exam Results</h1>", headers=PAGE_HEADERS)

@app.get("/exams/{exam_id}/part{part_number}", response_class=HTMLResponse)
def exam_page_slug(exam_id: str, part_number: int):
    exam_id = normalize_exam_id(exam_id)
    return exam_page(exam_id, part_number)

@app.get("/exams/{exam_id}/part/{part_number}", response_class=HTMLResponse)
def exam_page(exam_id: str, part_number: int):
    exam_id = normalize_exam_id(exam_id)
    content = get_cached_template("exam.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exam Page</h1>", headers=PAGE_HEADERS)

@app.get("/tools/clb-calculator", response_class=HTMLResponse)
def calculator_page():
    content = get_cached_template("calculator.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CLB Calculator</h1>", headers=PAGE_HEADERS)

@app.get("/{full_path:path}", response_class=HTMLResponse)
def dynamic_content_page(full_path: str):
    import ssl, urllib.request
    slug = full_path.strip("/")
    if not slug:
        return index_page()
    
    safe_slug = slug.replace("/", "_")
    if safe_slug in PAGE_CACHE:
        return HTMLResponse(PAGE_CACHE[safe_slug], headers=PAGE_HEADERS)

    page_file = os.path.join(PAGES_DIR, f"{safe_slug}.html")
    if os.path.exists(page_file) and os.path.getsize(page_file) > 0:
        with open(page_file, "r", encoding="utf-8") as f:
            content = f.read()
        cleaned = clean_html(content)
        PAGE_CACHE[safe_slug] = cleaned
        return HTMLResponse(cleaned, headers=PAGE_HEADERS)
    
    # Try fetching from celtestpip.com and caching locally
    remote_url = f"https://www.celtestpip.com/{slug}"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(remote_url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            if resp.status == 200:
                content = resp.read().decode("utf-8", errors="replace")
                cleaned = clean_html(content)
                with open(page_file, "w", encoding="utf-8") as f:
                    f.write(cleaned)
                PAGE_CACHE[safe_slug] = cleaned
                return HTMLResponse(cleaned, headers=PAGE_HEADERS)
    except Exception:
        pass
    
    raise HTTPException(status_code=404, detail="Page not found")
