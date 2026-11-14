"""Ditto Architecture: LanGeek French Autonomous Replica Server.

Renders pixel-perfect, zero-dependency templates matching LanGeek's design
(Home, Vocabulary Dashboard, Level Categories, and Interactive Flashcards/Quiz/Spelling),
backed by SQLite relational database, FTS5 full-text search, and media proxy.
"""

import os
import re
import json
import sqlite3
import hashlib
import logging
import mimetypes
from urllib.parse import urlparse
from typing import Optional, List, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, Response, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("langeek_server")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")
STATIC_ASSETS_DIR = os.path.join(STATIC_DIR, "assets")
MEDIA_PROXY_DIR = os.path.join(BASE_DIR, "data", "media", "proxy_cache")
DB_PATH = os.path.join(BASE_DIR, "data", "langeek.db")
UPSTREAM_BASE = "https://langeek.co"

templates = Jinja2Templates(directory=TEMPLATES_DIR)
http_client: Optional[httpx.AsyncClient] = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global http_client
    http_client = httpx.AsyncClient(
        verify=False,
        timeout=20.0,
        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
    )
    os.makedirs(STATIC_ASSETS_DIR, exist_ok=True)
    os.makedirs(MEDIA_PROXY_DIR, exist_ok=True)
    yield
    if http_client:
        await http_client.aclose()


app = FastAPI(
    title="LanGeek French Ditto Replica",
    description="Autonomous, Pixel-Perfect French Learning Sandbox for Students",
    version="2.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def guess_content_type(file_path: str, body: bytes = b"") -> str:
    lower = file_path.lower()
    if lower.endswith(".js"): return "application/javascript; charset=utf-8"
    if lower.endswith(".css"): return "text/css; charset=utf-8"
    if lower.endswith(".svg"): return "image/svg+xml"
    if lower.endswith(".png"): return "image/png"
    if lower.endswith((".jpg", ".jpeg")): return "image/jpeg"
    if lower.endswith(".webp"): return "image/webp"
    if lower.endswith(".woff2"): return "font/woff2"
    if lower.endswith(".woff"): return "font/woff"
    if lower.endswith(".ico"): return "image/x-icon"
    if lower.endswith(".json"): return "application/json; charset=utf-8"
    if lower.endswith(".mp3"): return "audio/mpeg"

    if body.startswith(b"\xff\xd8\xff"): return "image/jpeg"
    if body.startswith(b"\x89PNG"): return "image/png"
    if body.startswith(b"GIF8"): return "image/gif"
    if body.startswith(b"RIFF") and b"WEBP" in body[:12]: return "image/webp"
    if body.startswith(b"<svg") or b"<svg" in body[:100]: return "image/svg+xml"
    if body.startswith(b"ID3") or body.startswith(b"\xff\xfb") or body.startswith(b"\xff\xf3"): return "audio/mpeg"

    mime, _ = mimetypes.guess_type(file_path)
    return mime or "application/octet-stream"


async def ensure_subcategory_words(sub_id: int) -> List[Dict[str, Any]]:
    """Ensure vocabulary words for a subcategory exist in SQLite, fetching upstream if missing."""
    conn = get_db()
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT id, entry, part_of_speech, french_def, english_trans, other_trans, photo_url, thumb_url, audio_url, audio_ca_url, ipa, ipa_loc, grammar_info, card_json
        FROM words
        WHERE subcategory_id = ?
        ORDER BY id ASC
    """, (sub_id,)).fetchall()

    if rows:
        results = []
        for r in rows:
            w_dict = dict(r)
            if w_dict.get('card_json'):
                try:
                    cj = json.loads(w_dict['card_json']) if isinstance(w_dict['card_json'], str) else w_dict['card_json']
                    mt = cj.get('mainTranslation', {})
                    examples = []
                    for ex in mt.get('examples', []):
                        examples.append({
                            'fr': ex.get('example'),
                            'en': (ex.get('localizedProperties') or {}).get('example'),
                            'audio_fr': ex.get('exampleVoice'),
                            'audio_ca': ex.get('exampleVoice2')
                        })
                    w_dict['examples'] = examples
                    w_dict['grammar'] = mt.get('partOfSpeech', {}).get('grammaticalInformation') or {}
                    w_dict['metadata'] = mt.get('metadata') or {}
                except Exception:
                    pass
            if 'examples' not in w_dict or not w_dict['examples']:
                ex_rows = cur.execute("SELECT french_sentence as fr, english_sentence as en FROM examples WHERE word_id = ?", (r['id'],)).fetchall()
                w_dict['examples'] = [dict(ex) for ex in ex_rows]
            if 'grammar' not in w_dict and w_dict.get('grammar_info'):
                try:
                    w_dict['grammar'] = json.loads(w_dict['grammar_info'])
                except Exception:
                    w_dict['grammar'] = {}
            results.append(w_dict)
        conn.close()
        return results

    # Fetch on-demand from upstream
    logger.info(f"Subcategory {sub_id} words not yet in DB; fetching on-demand from upstream...")
    url = f"{UPSTREAM_BASE}/fr-EN/vocab/subcategory/{sub_id}/learn"
    try:
        resp = await http_client.get(url)
        if resp.status_code == 200:
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
            if m:
                d = json.loads(m.group(1))
                sub_data = d.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {}).get('subcategory', {})
                cards = sub_data.get('cards', [])
                for card in cards:
                    mt = card.get('mainTranslation', {})
                    if not mt: continue
                    w_id = card.get('id') or mt.get('id')
                    entry = mt.get('title')
                    pos = mt.get('partOfSpeech', {}).get('partOfSpeechType')
                    french_def = mt.get('translation')
                    loc = mt.get('localizedProperties') or {}
                    eng = loc.get('translation')
                    other = loc.get('otherTranslations')
                    wp = mt.get('wordPhoto') or {}
                    photo = wp.get('photo')
                    thumb = wp.get('photoThumbnail')
                    audio = mt.get('titleVoice')
                    audio_ca = mt.get('titleVoice2')

                    ipa = mt.get('pronunciation') or (mt.get('metadata', {}).get('nlpAnalyzedData', {}).get('pronunciationIPA'))
                    ipa_loc = mt.get('metadata', {}).get('nlpAnalyzedData', {}).get('pronunciationLocalization')
                    grammar = json.dumps(mt.get('partOfSpeech', {}).get('grammaticalInformation') or {}, ensure_ascii=False)
                    card_str = json.dumps(card, ensure_ascii=False)

                    cur.execute("""
                        INSERT OR REPLACE INTO words (id, subcategory_id, entry, part_of_speech, french_def, english_trans, other_trans, photo_url, thumb_url, audio_url, audio_ca_url, ipa, ipa_loc, grammar_info, card_json)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (w_id, sub_id, entry, pos, french_def, eng, other, photo, thumb, audio, audio_ca, ipa, ipa_loc, grammar, card_str))

                    for ex in mt.get('examples', []):
                        ex_id = ex.get('id')
                        fr_s = ex.get('example')
                        loc_ex = ex.get('localizedProperties') or {}
                        en_s = loc_ex.get('example')
                        if fr_s:
                            cur.execute("INSERT OR REPLACE INTO examples (id, word_id, french_sentence, english_sentence) VALUES (?, ?, ?, ?)", (ex_id, w_id, fr_s, en_s))
                conn.commit()

        # Re-query
        return await ensure_subcategory_words(sub_id)
    except Exception as e:
        logger.error(f"Error fetching subcategory {sub_id} words: {e}")
        conn.close()
        return []


# ---------------------------------------------------------
# Static Assets & Media Proxy
# ---------------------------------------------------------
@app.get("/assets/{asset_path:path}")
async def serve_site_assets(asset_path: str):
    """Serve site SVGs, flags, logos, and UI textures."""
    local_file = os.path.join(STATIC_ASSETS_DIR, asset_path)
    if os.path.exists(local_file) and os.path.getsize(local_file) > 0:
        mime = guess_content_type(local_file)
        return FileResponse(local_file, media_type=mime)

    upstream_url = f"{UPSTREAM_BASE}/assets/{asset_path}"
    try:
        resp = await http_client.get(upstream_url)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(local_file), exist_ok=True)
            with open(local_file, "wb") as f:
                f.write(resp.content)
            mime = guess_content_type(asset_path, resp.content)
            return Response(content=resp.content, media_type=mime, headers={"Cache-Control": "public, max-age=31536000"})
    except Exception as e:
        logger.warning(f"Error fetching asset {upstream_url}: {e}")

    raise HTTPException(status_code=404, detail="Asset not found")


@app.get("/media-proxy")
async def media_proxy(request: Request, url: str = ""):
    """Proxy third-party CDN photos & TTS audio with corrected binary MIME headers."""
    raw_query = str(request.url.query)
    if "url=" in raw_query:
        target_url = raw_query.split("url=", 1)[1]
        from urllib.parse import unquote
        url = unquote(target_url) if "%" in target_url else target_url

    if not url or len(url) < 10:
        raise HTTPException(status_code=400, detail="Missing or invalid url parameter")

    parsed = urlparse(url)
    allowed_domains = ("langeek.co", "b-amooz.com", "bamooz.com", "googleapis.com", "gstatic.com")
    if not any(parsed.netloc.endswith(dom) or dom in parsed.netloc for dom in allowed_domains):
        raise HTTPException(status_code=400, detail="External domains forbidden")

    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()
    cache_file = os.path.join(MEDIA_PROXY_DIR, url_hash)

    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 0:
        with open(cache_file, "rb") as f:
            content = f.read()
        mime = guess_content_type(url, content)
        return Response(content=content, media_type=mime, headers={"Cache-Control": "public, max-age=31536000", "Access-Control-Allow-Origin": "*"})

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://langeek.co/"
    }
    try:
        resp = await http_client.get(url, headers=headers)
        if resp.status_code == 200:
            body = resp.content
            mime = guess_content_type(url, body)
            with open(cache_file, "wb") as f:
                f.write(body)
            return Response(
                content=body,
                media_type=mime,
                headers={"Cache-Control": "public, max-age=31536000", "Access-Control-Allow-Origin": "*"}
            )
        else:
            raise HTTPException(status_code=resp.status_code, detail="Media fetch failed")
    except Exception as e:
        logger.error(f"Error proxying media {url}: {e}")
        raise HTTPException(status_code=502, detail=str(e))


@app.get("/sw.js")
async def unregister_sw():
    content = """
    self.addEventListener('install', () => self.skipWaiting());
    self.addEventListener('activate', () => {
        self.registration.unregister();
        self.clients.claim();
    });
    """
    return Response(content=content, media_type="application/javascript")


# ---------------------------------------------------------
# Core Application Views
# ---------------------------------------------------------
@app.get("/")
@app.get("/es")
@app.get("/de")
@app.get("/en")
async def root_redirect():
    return RedirectResponse(url="/fr-EN")

@app.get("/fr-EN")
async def home_view(request: Request):
    """Render pixel-perfect Home Page matching Image 3."""
    return templates.TemplateResponse(request, "home.html", {"active_tab": "home"})

@app.get("/fr-EN/plans")
async def plans_view(request: Request):
    """Render LanGeek Pro / Unlimited Plans Showcase."""
    return templates.TemplateResponse(request, "plans.html", {"active_tab": "plans"})

@app.get("/fr-EN/mobile-app")
async def mobile_app_view(request: Request):
    """Render LanGeek Mobile App Showcase."""
    return templates.TemplateResponse(request, "mobile_app.html", {"active_tab": "mobile"})

@app.get("/fr-EN/contact-us")
async def contact_us_view(request: Request):
    """Render LanGeek Pedagogical Support & Contact."""
    return templates.TemplateResponse(request, "contact_us.html", {"active_tab": "contact"})

@app.get("/fr-EN/expressions")
async def expressions_view(request: Request):
    """Render French Expressions and Idioms Showcase."""
    return templates.TemplateResponse(request, "expressions.html", {"active_tab": "expressions"})

@app.get("/fr-EN/vocab")
async def vocab_overview_view(request: Request):
    """Render pixel-perfect Vocabulary Overview matching Image 4."""
    conn = get_db()
    cur = conn.cursor()
    
    # Live stats
    learned_words = cur.execute("SELECT count(*) FROM user_progress WHERE status IN ('learned', 'mastered')").fetchone()[0]
    total_words = cur.execute("SELECT count(*) FROM words").fetchone()[0]
    total_subcategories = cur.execute("SELECT count(*) FROM subcategories").fetchone()[0]
    
    topics = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'topic-related' ORDER BY title").fetchall()
    most_common = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'most-common' ORDER BY id").fetchall()
    categorized = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'categorized-words' ORDER BY id").fetchall()
    conn.close()

    stats = {
        "learned_words": learned_words,
        "total_words": total_words if total_words > 0 else 5884,
        "total_subcategories": total_subcategories if total_subcategories > 0 else 796,
        "learned_today": 0
    }
    return templates.TemplateResponse(request, "vocab_overview.html", {
        "active_tab": "vocab",
        "stats": stats,
        "topics": [dict(t) for t in topics],
        "most_common": [dict(m) for m in most_common],
        "categorized": [dict(c) for c in categorized]
    })

@app.get("/fr-EN/vocab/category/{cat_id}/{slug}")
@app.get("/fr-EN/vocab/category/{cat_id}")
async def category_detail_view(cat_id: int, request: Request, slug: Optional[str] = None):
    """Render pixel-perfect Category & Lessons list matching Image 5."""
    conn = get_db()
    cur = conn.cursor()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (cat_id,)).fetchone()
    if not cat_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Category not found")
    
    sub_rows = cur.execute("SELECT * FROM subcategories WHERE category_id = ? ORDER BY id ASC", (cat_id,)).fetchall()
    conn.close()

    return templates.TemplateResponse(request, "category_detail.html", {
        "active_tab": "vocab",
        "category": dict(cat_row),
        "subcategories": [dict(s) for s in sub_rows]
    })

@app.get("/fr-EN/vocab/subcategory/{sub_id}/learn")
@app.get("/fr-EN/vocab/subcategory/{sub_id}/learn/review")
async def learn_studio_view(sub_id: int, request: Request):
    """Render Rich Vocabulary Detail Studio (Matches LanGeek User Screenshot)."""
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id)
    return templates.TemplateResponse(request, "learn_studio.html", {
        "active_tab": "vocab",
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Words"},
        "category": dict(cat_row) if cat_row else {"slug": "c1", "title": "Level-Based French Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })

@app.get("/fr-EN/vocab/subcategory/{sub_id}/learn/flashcard")
async def flashcards_learner_view(sub_id: int, request: Request):
    """Render Interactive 3D Flashcards Student Learning Suite."""
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id)
    return templates.TemplateResponse(request, "learn_flashcard.html", {
        "active_tab": "vocab",
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Words"},
        "category": dict(cat_row) if cat_row else {"slug": "c1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })

@app.get("/fr-EN/vocab/subcategory/{sub_id}/learn/quiz")
async def quiz_learner_view(sub_id: int, request: Request):
    """Render Interactive Multiple-Choice Vocabulary Quiz."""
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id)
    return templates.TemplateResponse(request, "learn_quiz.html", {
        "active_tab": "vocab",
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Quiz"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })

@app.get("/fr-EN/vocab/subcategory/{sub_id}/learn/spelling")
async def spelling_learner_view(sub_id: int, request: Request):
    """Render Interactive Audio Dictation Spelling Practice."""
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id)
    return templates.TemplateResponse(request, "learn_spelling.html", {
        "active_tab": "vocab",
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Spelling"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })

@app.get("/fr-EN/vocab/subcategory/{sub_id}/word-list")
@app.get("/fr-EN/vocab/subcategory/{sub_id}/wordlist")
@app.get("/fr-EN/vocab/subcategory/{sub_id}/words")
async def word_list_view(sub_id: int, request: Request):
    """Render Complete Lesson Wordlist Dictionary Table."""
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id)
    return templates.TemplateResponse(request, "word_list.html", {
        "active_tab": "vocab",
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Wordlist"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words
    })

@app.get("/fr-EN/grammar")
async def grammar_overview_view(request: Request):
    """Render French Grammar Overview."""
    conn = get_db()
    cur = conn.cursor()
    categories = cur.execute("SELECT * FROM grammar_categories ORDER BY position ASC").fetchall()
    courses = cur.execute("SELECT id, url_id, title, level, web_title, description, blocks_count FROM grammar_courses ORDER BY id ASC LIMIT 6").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "grammar_overview.html", {
        "active_tab": "grammar",
        "categories": [dict(c) for c in categories],
        "courses": [dict(c) for c in courses]
    })

@app.get("/fr-EN/grammar/{cat_id}/{slug}")
@app.get("/fr-EN/grammar/{cat_id}")
async def grammar_category_view(cat_id: int, request: Request, slug: Optional[str] = None):
    """Render courses for a French Grammar module."""
    conn = get_db()
    cur = conn.cursor()
    cat_row = cur.execute("SELECT * FROM grammar_categories WHERE id = ?", (cat_id,)).fetchone()
    if not cat_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Grammar category not found")
    courses = cur.execute("SELECT * FROM grammar_courses WHERE category_id = ? ORDER BY id ASC", (cat_id,)).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "grammar_category.html", {
        "active_tab": "grammar",
        "category": dict(cat_row),
        "courses": [dict(c) for c in courses]
    })

@app.get("/fr-EN/grammar/course/{course_id}/{slug}/{level}")
@app.get("/fr-EN/grammar/course/{course_id}/{slug}")
async def grammar_lesson_view(course_id: int, request: Request, slug: Optional[str] = None, level: Optional[str] = None):
    """Render French Grammar Lesson Course with syntax blocks & quiz."""
    conn = get_db()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM grammar_courses WHERE id = ?", (course_id,)).fetchone()
    if not row:
        conn.close()
        raise HTTPException(status_code=404, detail="Grammar course not found")
    
    course_dict = dict(row)
    cat_row = cur.execute("SELECT * FROM grammar_categories WHERE id = ?", (course_dict.get('category_id'),)).fetchone()
    conn.close()

    blocks = []
    questions = []
    if course_dict.get('blocks_json'):
        try:
            bj = json.loads(course_dict['blocks_json'])
            if isinstance(bj, dict):
                blocks = bj.get('blocks', [])
                questions = bj.get('questions', [])
            elif isinstance(bj, list):
                blocks = bj
        except Exception:
            pass

    return templates.TemplateResponse(request, "grammar_lesson.html", {
        "active_tab": "grammar",
        "course": course_dict,
        "category": dict(cat_row) if cat_row else None,
        "blocks": blocks,
        "questions": questions
    })

@app.get("/fr-EN/reading")
async def reading_overview_view(request: Request):
    """Render French Reading Comprehension Overview."""
    conn = get_db()
    cur = conn.cursor()
    collections = cur.execute("SELECT * FROM reading_collections ORDER BY position ASC").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "reading_overview.html", {
        "active_tab": "reading",
        "collections": [dict(c) for c in collections]
    })

@app.get("/fr-EN/reading/{col_id}/{slug}")
@app.get("/fr-EN/reading/{col_id}")
async def reading_collection_view(col_id: int, request: Request, slug: Optional[str] = None):
    """Render stories in a French Reading Collection."""
    conn = get_db()
    cur = conn.cursor()
    col_row = cur.execute("SELECT * FROM reading_collections WHERE id = ?", (col_id,)).fetchone()
    if not col_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Reading collection not found")
    stories = cur.execute("SELECT * FROM reading_stories WHERE collection_id = ? ORDER BY id ASC", (col_id,)).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "reading_collection.html", {
        "active_tab": "reading",
        "collection": dict(col_row),
        "stories": [dict(s) for s in stories]
    })

@app.get("/fr-EN/reading/course/{story_id}/{slug}/{segment}")
@app.get("/fr-EN/reading/course/{story_id}/{slug}")
async def reading_story_view(story_id: int, request: Request, slug: Optional[str] = None, segment: Optional[str] = None):
    """Render French Reading Story with aligned translation & audio."""
    conn = get_db()
    cur = conn.cursor()
    story_row = cur.execute("SELECT * FROM reading_stories WHERE id = ?", (story_id,)).fetchone()
    if not story_row:
        conn.close()
        raise HTTPException(status_code=404, detail="Reading story not found")
    
    story_dict = dict(story_row)
    col_row = cur.execute("SELECT * FROM reading_collections WHERE id = ?", (story_dict.get('collection_id'),)).fetchone()
    conn.close()

    paragraphs = []
    if story_dict.get('content_json'):
        try:
            paragraphs = json.loads(story_dict['content_json'])
        except Exception:
            pass

    return templates.TemplateResponse(request, "reading_story.html", {
        "active_tab": "reading",
        "story": story_dict,
        "collection": dict(col_row) if col_row else None,
        "paragraphs": paragraphs
    })

@app.get("/fr-EN/pronunciation")
async def pronunciation_overview_view(request: Request):
    """Render French Pronunciation Guide."""
    return templates.TemplateResponse(request, "pronunciation_overview.html", {
        "active_tab": "pronunciation"
    })

@app.get("/fr-EN/pronunciation/101/alphabet-francais")
@app.get("/fr-EN/pronunciation/alphabet-francais")
async def pronunciation_alphabet_view(request: Request):
    """Render French Alphabet Guide (26 letters with pronunciation)."""
    conn = get_db()
    cur = conn.cursor()
    courses = cur.execute("SELECT * FROM pronunciation_courses ORDER BY position ASC").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "pronunciation_alphabet.html", {
        "active_tab": "pronunciation",
        "courses": [dict(c) for c in courses]
    })


# ---------------------------------------------------------
# Local APIs & Offline Search Engine
# ---------------------------------------------------------
@app.get("/api/search")
async def search_french_words(q: str = Query(..., min_length=1), limit: int = 25):
    """Lightning-fast FTS5 search across French words, phonetics, definitions, and examples."""
    conn = get_db()
    cur = conn.cursor()
    clean_q = re.sub(r'[^a-zA-Z0-9\u00C0-\u017F]', ' ', q).strip()
    match_query = f"{clean_q}*"
    try:
        rows = cur.execute("""
            SELECT w.id, w.entry, w.part_of_speech, w.french_def, w.english_trans,
                   w.photo_url, w.thumb_url, w.audio_url, w.audio_ca_url,
                   (SELECT french_sentence FROM examples WHERE word_id = w.id LIMIT 1) as sample_french,
                   (SELECT english_sentence FROM examples WHERE word_id = w.id LIMIT 1) as sample_english
            FROM search_fts f
            JOIN words w ON w.id = f.word_id
            WHERE search_fts MATCH ?
            LIMIT ?
        """, (match_query, limit)).fetchall()
        results = [dict(r) for r in rows]
    except Exception as e:
        logger.warning(f"FTS search error: {e}")
        rows = cur.execute("""
            SELECT w.id, w.entry, w.part_of_speech, w.french_def, w.english_trans,
                   w.photo_url, w.thumb_url, w.audio_url, w.audio_ca_url
            FROM words w
            WHERE w.entry LIKE ? OR w.english_trans LIKE ?
            LIMIT ?
        """, (f"%{clean_q}%", f"%{clean_q}%", limit)).fetchall()
        results = [dict(r) for r in rows]
    finally:
        conn.close()

    return {"query": q, "count": len(results), "results": results}

@app.get("/api/stats")
async def get_stats():
    conn = get_db()
    cur = conn.cursor()
    words_cnt = cur.execute("SELECT count(*) FROM words").fetchone()[0]
    examples_cnt = cur.execute("SELECT count(*) FROM examples").fetchone()[0]
    cats_cnt = cur.execute("SELECT count(*) FROM categories").fetchone()[0]
    subcats_cnt = cur.execute("SELECT count(*) FROM subcategories").fetchone()[0]
    courses_cnt = cur.execute("SELECT count(*) FROM grammar_courses").fetchone()[0]
    conn.close()
    return {
        "words": words_cnt,
        "examples": examples_cnt,
        "categories": cats_cnt,
        "subcategories": subcats_cnt,
        "grammar_courses": courses_cnt
    }

@app.post("/api/progress/mark")
async def mark_progress(request: Request):
    """Save flashcard recall grading into SQLite."""
    try:
        data = await request.json()
        word_id = data.get("word_id")
        score = data.get("score", 3)
        status = "mastered" if score >= 4 else "learned" if score >= 3 else "learning"

        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO user_progress (word_id, status, review_count, last_reviewed_at)
            VALUES (?, ?, 1, CURRENT_TIMESTAMP)
            ON CONFLICT(word_id) DO UPDATE SET
                status=excluded.status,
                review_count=review_count + 1,
                last_reviewed_at=CURRENT_TIMESTAMP
        """, (word_id, status))
        conn.commit()
        conn.close()
        return JSONResponse({"status": "recorded", "word_id": word_id, "state": status})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)}, status_code=400)


@app.get("/api/progress/summary")
async def progress_summary():
    """Return summary statistics of words learned, mastered, and reviewing."""
    conn = get_db()
    cur = conn.cursor()
    total_words = cur.execute("SELECT count(*) FROM words").fetchone()[0]
    mastered = cur.execute("SELECT count(*) FROM user_progress WHERE status = 'mastered'").fetchone()[0]
    learned = cur.execute("SELECT count(*) FROM user_progress WHERE status = 'learned'").fetchone()[0]
    learning = cur.execute("SELECT count(*) FROM user_progress WHERE status = 'learning'").fetchone()[0]
    conn.close()
    return JSONResponse({
        "status": "success",
        "total_catalog_words": total_words,
        "mastered": mastered,
        "learned": learned,
        "learning": learning,
        "total_active": mastered + learned + learning
    })


# Mock APIs
@app.get("/v1/a")
@app.get("/api/v1/a")
async def mock_auth_user():
    return JSONResponse({
        "status": "success",
        "user": {
            "id": 999999,
            "email": "learner@local.dev",
            "name": "French Explorer (Pro)",
            "tier": "premium",
            "isPremium": True,
            "credits": 99999
        }
    })

@app.get("/v1/plan")
@app.get("/api/v1/plan")
async def mock_plan():
    return JSONResponse({
        "data": {
            "id": "unlimited_pro",
            "title": "LanGeek Unlimited Lifetime (Replica)",
            "isPremium": True,
            "hasAccess": True
        },
        "status": "succeeded"
    })

@app.get("/v1/geoip")
@app.get("/api/v1/geoip")
async def mock_geoip():
    return JSONResponse({"country": "FR", "city": "Paris", "continent": "EU"})


# ---------------------------------------------------------
# Administrator Crawler & Change Monitor Dashboard
# ---------------------------------------------------------
from langeek.monitor import get_monitor_stats, run_crawl_cycle

@app.get("/admin/monitor")
async def admin_dashboard_view(request: Request):
    """Render Administrator Dashboard for Crawler & Change Monitor."""
    stats = get_monitor_stats()
    return templates.TemplateResponse(request, "admin_dashboard.html", {
        "active_tab": "admin",
        "stats": stats
    })

@app.get("/api/admin/status")
async def admin_status_api():
    """Return aggregated stats for monitor."""
    return JSONResponse(get_monitor_stats())

@app.post("/api/admin/crawl/run")
async def admin_trigger_crawl():
    """Execute manual crawl pass across all monitored URLs."""
    res = await run_crawl_cycle()
    return JSONResponse(res)


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("langeek.server:app", host="0.0.0.0", port=port, reload=False)
