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


async def ensure_subcategory_words(sub_id: int, locale: str = "fr-EN") -> List[Dict[str, Any]]:
    """Ensure vocabulary words for a subcategory exist in SQLite, fetching upstream if missing."""
    conn = get_db()
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT id, entry, part_of_speech, french_def, english_trans, other_trans, photo_url, thumb_url, audio_url, audio_ca_url, ipa, ipa_loc, grammar_info, card_json
        FROM words
        WHERE subcategory_id = ?
        ORDER BY position ASC, id ASC
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
    loc_prefix = "en" if locale == "en" else "fr-EN"
    logger.info(f"Subcategory {sub_id} words not yet in DB; fetching on-demand from upstream ({loc_prefix})...")
    url = f"{UPSTREAM_BASE}/{loc_prefix}/vocab/subcategory/{sub_id}/learn"
    try:
        if http_client is not None:
            resp = await http_client.get(url)
        else:
            async with httpx.AsyncClient(verify=False, timeout=15.0) as temp_client:
                resp = await temp_client.get(url)

        if resp.status_code == 200:
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
            if m:
                d = json.loads(m.group(1))
                sub_data = d.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {}).get('subcategory', {})
                cards = sub_data.get('cards', [])
                for idx, card in enumerate(cards):
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
                        INSERT OR REPLACE INTO words (id, subcategory_id, entry, part_of_speech, french_def, english_trans, other_trans, photo_url, thumb_url, audio_url, audio_ca_url, ipa, ipa_loc, grammar_info, card_json, position)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (w_id, sub_id, entry, pos, french_def, eng, other, photo, thumb, audio, audio_ca, ipa, ipa_loc, grammar, card_str, idx))

                    for ex in mt.get('examples', []):
                        ex_id = ex.get('id')
                        fr_s = ex.get('example')
                        loc_ex = ex.get('localizedProperties') or {}
                        en_s = loc_ex.get('example')
                        if fr_s:
                            cur.execute("INSERT OR REPLACE INTO examples (id, word_id, french_sentence, english_sentence) VALUES (?, ?, ?, ?)", (ex_id, w_id, fr_s, en_s))
                conn.commit()

        # Re-query
        return await ensure_subcategory_words(sub_id, locale=locale)
    except Exception as e:
        logger.error(f"Error fetching subcategory {sub_id} words: {e}")
        conn.close()
        return []


async def fetch_and_cache_upstream(upstream_path: str, db_locale: str = "en") -> bool:
    """Fetch uncached lesson/module page from upstream LanGeek, extract __NEXT_DATA__, and persist to SQLite."""
    global http_client
    path = upstream_path.lstrip("/")
    target_url = f"{UPSTREAM_BASE}/{path}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": f"{UPSTREAM_BASE}/"
    }
    logger.info(f"Cache-through fallback: attempting upstream fetch for {target_url} (locale={db_locale})")
    try:
        if http_client is not None:
            resp = await http_client.get(target_url, headers=headers, follow_redirects=True)
        else:
            async with httpx.AsyncClient(verify=False, timeout=15.0) as temp_client:
                resp = await temp_client.get(target_url, headers=headers, follow_redirects=True)

        if resp.status_code != 200:
            logger.warning(f"Upstream fetch failed: {target_url} returned HTTP {resp.status_code}")
            return False

        m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text, flags=re.DOTALL)
        if not m:
            logger.warning(f"No __NEXT_DATA__ found at {target_url}")
            return False

        data = json.loads(m.group(1))
        page_props = data.get("props", {}).get("pageProps", {})
        init_state = page_props.get("initialState", {})
        static_data = init_state.get("static", {})

        conn = get_db()
        cur = conn.cursor()
        cached_any = False

        # 1. Subcategory & Vocabulary Cards
        sub = static_data.get("subcategory")
        cat = static_data.get("category")
        if sub and isinstance(sub, dict):
            sub_id = sub.get("id")
            cat_id = (cat.get("id") if cat else None) or sub.get("categoryId")
            if cat and isinstance(cat, dict):
                cur.execute("""
                    INSERT INTO categories (id, slug, title, description, web_title, photo_thumbnail, locale)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        title=excluded.title,
                        description=excluded.description,
                        web_title=excluded.web_title
                """, (
                    cat_id,
                    cat.get("urlId") or cat.get("slug"),
                    cat.get("title") or cat.get("webTitle"),
                    cat.get("description"),
                    cat.get("webTitle"),
                    cat.get("photoThumbnail"),
                    db_locale
                ))
            cards = sub.get("cards", [])
            cur.execute("""
                INSERT INTO subcategories (id, category_id, slug, title, description, web_title, words_count, estimated_time, locale)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title=excluded.title,
                    description=excluded.description,
                    words_count=excluded.words_count
            """, (
                sub_id,
                cat_id,
                sub.get("urlId") or str(sub_id),
                sub.get("title") or sub.get("originalTitle"),
                sub.get("description"),
                sub.get("webTitle"),
                len(cards) if cards else sub.get("wordsCount", 0),
                sub.get("estimatedLearningTime", 0),
                db_locale
            ))
            for idx, card in enumerate(cards):
                mt = card.get("mainTranslation") or {}
                if not mt:
                    continue
                w_id = card.get("id") or mt.get("id")
                entry = mt.get("title") or ""
                pos = (mt.get("partOfSpeech") or {}).get("partOfSpeechType")
                french_def = mt.get("translation") or ""
                loc = mt.get("localizedProperties") or {}
                eng = loc.get("translation") or ""
                other = loc.get("otherTranslations") or ""
                wp = mt.get("wordPhoto") or {}
                photo = wp.get("photo")
                thumb = wp.get("photoThumbnail")
                audio = mt.get("titleVoice")
                audio_ca = mt.get("titleVoice2")
                ipa = mt.get("pronunciation") or ((mt.get("metadata") or {}).get("nlpAnalyzedData", {}).get("pronunciationIPA"))
                ipa_loc = (mt.get("metadata") or {}).get("nlpAnalyzedData", {}).get("pronunciationLocalization")
                grammar = json.dumps((mt.get("partOfSpeech") or {}).get("grammaticalInformation") or {}, ensure_ascii=False)
                card_str = json.dumps(card, ensure_ascii=False)

                cur.execute("""
                    INSERT INTO words (id, subcategory_id, entry, part_of_speech, french_def, english_trans, other_trans, photo_url, thumb_url, audio_url, audio_ca_url, ipa, ipa_loc, grammar_info, card_json, position)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        entry=excluded.entry,
                        english_trans=excluded.english_trans,
                        french_def=excluded.french_def,
                        audio_url=excluded.audio_url,
                        photo_url=excluded.photo_url
                """, (w_id, sub_id, entry, pos, french_def, eng, other, photo, thumb, audio, audio_ca, ipa, ipa_loc, grammar, card_str, idx))

                for ex in mt.get("examples", []):
                    ex_id = ex.get("id")
                    fr_s = ex.get("example")
                    loc_ex = ex.get("localizedProperties") or {}
                    en_s = loc_ex.get("example")
                    if fr_s:
                        cur.execute("INSERT OR REPLACE INTO examples (id, word_id, french_sentence, english_sentence) VALUES (?, ?, ?, ?)", (ex_id, w_id, fr_s, en_s))
            cached_any = True

        # 2. Category Overview
        elif cat and isinstance(cat, dict) and not sub:
            cat_id = cat.get("id")
            cur.execute("""
                INSERT INTO categories (id, slug, title, description, web_title, photo_thumbnail, photo, words_count, subcategories_count, locale)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title=excluded.title,
                    description=excluded.description,
                    words_count=excluded.words_count,
                    subcategories_count=excluded.subcategories_count
            """, (
                cat_id,
                cat.get("urlId") or cat.get("slug"),
                cat.get("title") or cat.get("webTitle"),
                cat.get("description"),
                cat.get("webTitle"),
                cat.get("photoThumbnail"),
                cat.get("photo"),
                cat.get("wordsCount", 0),
                len(cat.get("subCategories", [])),
                db_locale
            ))
            for s in cat.get("subCategories", []):
                cur.execute("""
                    INSERT INTO subcategories (id, category_id, slug, title, description, web_title, words_count, estimated_time, locale)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        title=excluded.title,
                        description=excluded.description
                """, (
                    s.get("id"),
                    cat_id,
                    s.get("urlId") or str(s.get("id")),
                    s.get("title") or s.get("originalTitle"),
                    s.get("description"),
                    s.get("webTitle"),
                    s.get("wordsCount", 0),
                    s.get("estimatedLearningTime", 0),
                    db_locale
                ))
            cached_any = True

        # 3. Grammar Course & Blocks
        course = static_data.get("course")
        seg = static_data.get("segment")
        if course and isinstance(course, dict):
            c_id = course.get("id")
            blocks = (seg.get("blocks", []) if seg else [])
            cur.execute("""
                INSERT INTO grammar_courses (id, url_id, title, level, web_title, description, blocks_count, blocks_json, category_id, photo, photo_thumbnail, original_title, locale)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title=excluded.title,
                    blocks_count=excluded.blocks_count,
                    blocks_json=excluded.blocks_json
            """, (
                c_id,
                course.get("urlId"),
                course.get("title") or (seg.get("title") if seg else ""),
                seg.get("level", "intermediate") if seg else "intermediate",
                course.get("webTitle") or (seg.get("webTitle") if seg else ""),
                course.get("description") or (seg.get("description") if seg else ""),
                len(blocks),
                json.dumps({"blocks": blocks}, ensure_ascii=False) if blocks else "[]",
                course.get("levelId") or course.get("categoryId"),
                course.get("photo"),
                course.get("photoThumbnail"),
                course.get("originalTitle"),
                db_locale
            ))
            cached_any = True

        # 4. Reading Story & Paragraph/Photo Blocks
        r_blocks = static_data.get("readingBlocks")
        story = static_data.get("course")
        if r_blocks and isinstance(r_blocks, list) and story and isinstance(story, dict):
            story_id = story.get("id")
            if story_id:
                paragraphs = []
                for b in r_blocks:
                    if b.get("blockType") == "PhotoBlock" or b.get("photo"):
                        paragraphs.append({
                            "type": "photo",
                            "blockType": "PhotoBlock",
                            "photo": b.get("photo"),
                            "photo_thumbnail": b.get("photoThumbnail")
                        })
                    else:
                        sentences = b.get("sentences", [])
                        text_main = " ".join((s.get("sentence") or "") for s in sentences).strip()
                        text_trans = " ".join(((s.get("localizedProperties") or {}).get("sentence") or "") for s in sentences).strip()
                        paragraphs.append({
                            "type": "paragraph",
                            "blockType": "ParagraphBlock",
                            "fr": text_main,
                            "en": text_trans or text_main,
                            "audio": b.get("readableTextVoice")
                        })
                cur.execute("""
                    INSERT INTO reading_stories (id, collection_id, title, url_id, level, description, photo, photo_thumbnail, content_json, quiz_json, locale)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(id) DO UPDATE SET
                        content_json=excluded.content_json,
                        title=excluded.title
                """, (
                    story_id,
                    story.get("levelId") or story.get("collectionId"),
                    story.get("title"),
                    story.get("urlId"),
                    story.get("level", "intermediate"),
                    story.get("description", ""),
                    story.get("photo"),
                    story.get("photoThumbnail"),
                    json.dumps(paragraphs, ensure_ascii=False),
                    "[]",
                    db_locale
                ))
                cur.execute("""
                    INSERT INTO reading_segments (story_id, segment_index, title, url_id, photo, content_json, locale)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(story_id, segment_index) DO UPDATE SET
                        content_json=excluded.content_json,
                        title=excluded.title
                """, (
                    story_id,
                    0,
                    story.get("title", "Chapter 1"),
                    story.get("urlId"),
                    story.get("photo"),
                    json.dumps(paragraphs, ensure_ascii=False),
                    db_locale
                ))
                cached_any = True

        conn.commit()
        conn.close()
        logger.info(f"Cache-through fallback result for {target_url}: cached_any={cached_any}")
        return cached_any
    except Exception as e:
        logger.error(f"Error in fetch_and_cache_upstream for {target_url}: {e}")
        return False



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


@app.get("/next/{next_path:path}")
async def serve_next_assets(next_path: str):
    """Serve Next.js CSS, JS, and font media assets with caching."""
    local_file = os.path.join(STATIC_DIR, "next", next_path)
    if os.path.exists(local_file) and os.path.getsize(local_file) > 0:
        mime = guess_content_type(local_file)
        return FileResponse(local_file, media_type=mime)

    upstream_url = f"{UPSTREAM_BASE}/next/{next_path}"
    try:
        resp = await http_client.get(upstream_url)
        if resp.status_code == 200:
            os.makedirs(os.path.dirname(local_file), exist_ok=True)
            with open(local_file, "wb") as f:
                f.write(resp.content)
            mime = guess_content_type(next_path, resp.content)
            return Response(content=resp.content, media_type=mime, headers={"Cache-Control": "public, max-age=31536000"})
    except Exception as e:
        logger.warning(f"Error fetching next asset {upstream_url}: {e}")

    raise HTTPException(status_code=404, detail="Next asset not found")


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
# Multi-Locale Context Helper & Core Application Views
# ---------------------------------------------------------
SUPPORTED_LOCALES = ("en", "fr-EN")


def get_locale_context(locale: Optional[str] = "en", request: Optional[Request] = None, active_tab: str = "home", current_path: Optional[str] = None) -> dict:
    """Provide standardized multi-locale metadata, dictionary link, and path-preserving switch URLs."""
    loc = "en" if locale == "en" else "fr-EN"
    if current_path is not None:
        path = current_path
    elif request is not None:
        path = request.url.path
    else:
        path = f"/{loc}"
        
    # Build equivalent switch URL preserving current subpath
    if loc == "en":
        switch_url = path.replace("/en", "/fr-EN", 1) if path.startswith("/en") else "/fr-EN"
    else:
        switch_url = path.replace("/fr-EN", "/en", 1) if path.startswith("/fr-EN") else "/en"
        
    return {
        "locale": loc,
        "db_locale": "en" if loc == "en" else "fr",
        "lang_code": "en" if loc == "en" else "fr",
        "locale_name": "English" if loc == "en" else "Français",
        "flag_icon": "gb" if loc == "en" else "fr",
        "active_tab": active_tab,
        "switch_url": switch_url,
        "dict_url": "https://dictionary.langeek.co/?lang=en" if loc == "en" else "https://dictionary.langeek.co/?lang=fr"
    }


@app.get("/")
async def root_redirect(request: Request):
    loc = request.cookies.get("locale")
    if not loc:
        accept_lang = request.headers.get("accept-language", "").lower()
        if "fr" in accept_lang and "en" not in accept_lang:
            loc = "fr-EN"
        else:
            loc = "en"
    target = "/fr-EN" if loc == "fr-EN" else "/en"
    return RedirectResponse(url=target, status_code=307)


@app.get("/en/")
@app.get("/en-US")
@app.get("/en-US/")
async def en_alias_redirect():
    return RedirectResponse(url="/en", status_code=307)


@app.get("/fr")
@app.get("/fr/")
@app.get("/fr-EN/")
async def fr_alias_redirect():
    return RedirectResponse(url="/fr-EN", status_code=307)


@app.get("/es")
@app.get("/es/")
@app.get("/de")
@app.get("/de/")
async def stub_lang_redirect():
    return RedirectResponse(url="/en", status_code=307)


@app.get("/{locale}")
async def home_view(request: Request, locale: str = "fr-EN"):
    """Render pixel-perfect Home Page matching LanGeek."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="home")
    return templates.TemplateResponse(request, "home.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/plans")
async def plans_view(request: Request, locale: str = "fr-EN"):
    """Render LanGeek Pro / Unlimited Plans Showcase."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="plans")
    return templates.TemplateResponse(request, "plans.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/mobile-app")
async def mobile_app_view(request: Request, locale: str = "fr-EN"):
    """Render LanGeek Mobile App Showcase."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="mobile")
    return templates.TemplateResponse(request, "mobile_app.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/contact-us")
async def contact_us_view(request: Request, locale: str = "fr-EN"):
    """Render LanGeek Pedagogical Support & Contact."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="contact")
    return templates.TemplateResponse(request, "contact_us.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/expressions")
async def expressions_view(request: Request, locale: str = "fr-EN"):
    """Render Expressions and Idioms Showcase."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="expressions")
    return templates.TemplateResponse(request, "expressions.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/vocab")
async def vocab_overview_view(request: Request, locale: str = "fr-EN"):
    """Render pixel-perfect Vocabulary Overview matching LanGeek."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    
    # Live stats
    learned_words = cur.execute("SELECT count(*) FROM user_progress WHERE status IN ('learned', 'mastered') AND (locale = ? OR locale = ?)", (db_loc, loc_ctx["locale"])).fetchone()[0]
    total_words = cur.execute("SELECT count(*) FROM words").fetchone()[0]
    total_subcategories = cur.execute("SELECT count(*) FROM subcategories WHERE locale = ?", (db_loc,)).fetchone()[0]
    if total_subcategories == 0 and db_loc == "fr":
        total_subcategories = cur.execute("SELECT count(*) FROM subcategories").fetchone()[0]
    
    topics = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'topic-related' AND (locale = ? OR locale = ?) ORDER BY title", (db_loc, loc_ctx["locale"])).fetchall()
    if not topics and db_loc == "fr":
        topics = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'topic-related' ORDER BY title").fetchall()

    most_common = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'most-common' AND (locale = ? OR locale = ?) ORDER BY id", (db_loc, loc_ctx["locale"])).fetchall()
    if not most_common and db_loc == "fr":
        most_common = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'most-common' ORDER BY id").fetchall()

    categorized = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'categorized-words' AND (locale = ? OR locale = ?) ORDER BY id", (db_loc, loc_ctx["locale"])).fetchall()
    if not categorized and db_loc == "fr":
        categorized = cur.execute("SELECT id, slug, title, photo, words_count, subcategories_count FROM categories WHERE collection_id = 'categorized-words' ORDER BY id").fetchall()
    conn.close()

    stats = {
        "learned_words": learned_words,
        "total_words": total_words if total_words > 0 else 5884,
        "total_subcategories": total_subcategories if total_subcategories > 0 else 796,
        "learned_today": 0
    }
    return templates.TemplateResponse(request, "vocab_overview.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "stats": stats,
        "topics": [dict(t) for t in topics],
        "most_common": [dict(m) for m in most_common],
        "categorized": [dict(c) for c in categorized]
    })


@app.get("/{locale}/vocab/category/{cat_id}/{slug}")
@app.get("/{locale}/vocab/category/{cat_id}")
async def category_detail_view(cat_id: int, request: Request, locale: str = "fr-EN", slug: Optional[str] = None):
    """Render pixel-perfect Category & Lessons list."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (cat_id,)).fetchone()
    if not cat_row:
        conn.close()
        upstream_slug = slug or ""
        path = f"{loc_ctx['locale']}/vocab/category/{cat_id}/{upstream_slug}".rstrip("/")
        cached = await fetch_and_cache_upstream(path, db_locale=db_loc)
        if cached:
            conn = get_db()
            cur = conn.cursor()
            cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (cat_id,)).fetchone()
        if not cat_row:
            raise HTTPException(status_code=404, detail="Category not found")
    
    sub_rows = cur.execute("SELECT * FROM subcategories WHERE category_id = ? ORDER BY position ASC, id ASC", (cat_id,)).fetchall()
    conn.close()

    return templates.TemplateResponse(request, "category_detail.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "category": dict(cat_row),
        "subcategories": [dict(s) for s in sub_rows]
    })


@app.get("/{locale}/vocab/subcategory/{sub_id}/learn")
@app.get("/{locale}/vocab/subcategory/{sub_id}/learn/review")
async def learn_studio_view(sub_id: int, request: Request, locale: str = "fr-EN"):
    """Render Rich Vocabulary Detail Studio."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    if not sub_row:
        conn.close()
        path = f"{loc_ctx['locale']}/vocab/subcategory/{sub_id}/learn"
        await fetch_and_cache_upstream(path, db_locale=db_loc)
        conn = get_db()
        cur = conn.cursor()
        sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id, locale=locale)
    return templates.TemplateResponse(request, "learn_studio.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Words"},
        "category": dict(cat_row) if cat_row else {"slug": "c1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })


@app.get("/{locale}/vocab/subcategory/{sub_id}/learn/flashcard")
async def flashcards_learner_view(sub_id: int, request: Request, locale: str = "fr-EN"):
    """Render Interactive 3D Flashcards Student Learning Suite."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id, locale=locale)
    return templates.TemplateResponse(request, "learn_flashcard.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Words"},
        "category": dict(cat_row) if cat_row else {"slug": "c1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })


@app.get("/{locale}/vocab/subcategory/{sub_id}/learn/quiz")
async def quiz_learner_view(sub_id: int, request: Request, locale: str = "fr-EN"):
    """Render Interactive Multiple-Choice Vocabulary Quiz."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id, locale=locale)
    return templates.TemplateResponse(request, "learn_quiz.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Quiz"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })


@app.get("/{locale}/vocab/subcategory/{sub_id}/learn/spelling")
async def spelling_learner_view(sub_id: int, request: Request, locale: str = "fr-EN"):
    """Render Interactive Audio Dictation Spelling Practice."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id, locale=locale)
    return templates.TemplateResponse(request, "learn_spelling.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Spelling"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words,
        "words_json": json.dumps(words, ensure_ascii=False)
    })


@app.get("/{locale}/vocab/subcategory/{sub_id}/word-list")
@app.get("/{locale}/vocab/subcategory/{sub_id}/wordlist")
@app.get("/{locale}/vocab/subcategory/{sub_id}/words")
async def word_list_view(sub_id: int, request: Request, locale: str = "fr-EN"):
    """Render Complete Lesson Wordlist Dictionary Table."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="vocab")
    conn = get_db()
    cur = conn.cursor()
    sub_row = cur.execute("SELECT * FROM subcategories WHERE id = ?", (sub_id,)).fetchone()
    cat_row = cur.execute("SELECT * FROM categories WHERE id = ?", (sub_row['category_id'],)).fetchone() if sub_row else None
    conn.close()

    words = await ensure_subcategory_words(sub_id, locale=locale)
    return templates.TemplateResponse(request, "word_list.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "subcategory": dict(sub_row) if sub_row else {"id": sub_id, "title": "Lesson Wordlist"},
        "category": dict(cat_row) if cat_row else {"slug": "niveau-a1", "title": "Vocabulary"},
        "words": words
    })


@app.get("/{locale}/grammar")
async def grammar_overview_view(request: Request, locale: str = "fr-EN"):
    """Render Grammar Overview."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="grammar")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    categories = cur.execute("SELECT * FROM grammar_categories WHERE locale = ? ORDER BY position ASC", (db_loc,)).fetchall()
    if not categories and db_loc == "fr":
        categories = cur.execute("SELECT * FROM grammar_categories ORDER BY position ASC").fetchall()
    courses = cur.execute("SELECT id, url_id, title, level, web_title, description, blocks_count FROM grammar_courses WHERE locale = ? ORDER BY id ASC LIMIT 6", (db_loc,)).fetchall()
    if not courses and db_loc == "fr":
        courses = cur.execute("SELECT id, url_id, title, level, web_title, description, blocks_count FROM grammar_courses ORDER BY id ASC LIMIT 6").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "grammar_overview.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "categories": [dict(c) for c in categories],
        "courses": [dict(c) for c in courses]
    })


@app.get("/{locale}/grammar/{cat_id}/{slug}")
@app.get("/{locale}/grammar/{cat_id}")
async def grammar_category_view(cat_id: int, request: Request, locale: str = "fr-EN", slug: Optional[str] = None):
    """Render courses for a Grammar module."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="grammar")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    cat_row = cur.execute("SELECT * FROM grammar_categories WHERE id = ?", (cat_id,)).fetchone()
    if not cat_row:
        conn.close()
        upstream_slug = slug or ""
        path = f"{loc_ctx['locale']}/grammar/{cat_id}/{upstream_slug}".rstrip("/")
        cached = await fetch_and_cache_upstream(path, db_locale=db_loc)
        if cached:
            conn = get_db()
            cur = conn.cursor()
            cat_row = cur.execute("SELECT * FROM grammar_categories WHERE id = ?", (cat_id,)).fetchone()
        if not cat_row:
            raise HTTPException(status_code=404, detail="Grammar category not found")
    courses = cur.execute("SELECT * FROM grammar_courses WHERE category_id = ? ORDER BY id ASC", (cat_id,)).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "grammar_category.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "category": dict(cat_row),
        "courses": [dict(c) for c in courses]
    })


@app.get("/{locale}/grammar/course/{course_id}/{slug}/{level}")
@app.get("/{locale}/grammar/course/{course_id}/{slug}")
async def grammar_lesson_view(course_id: int, request: Request, locale: str = "fr-EN", slug: Optional[str] = None, level: Optional[str] = None):
    """Render Grammar Lesson Course with syntax blocks & quiz."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="grammar")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    row = cur.execute("SELECT * FROM grammar_courses WHERE id = ?", (course_id,)).fetchone()
    if not row:
        conn.close()
        upstream_slug = slug or ""
        path = f"{loc_ctx['locale']}/grammar/course/{course_id}/{upstream_slug}".rstrip("/")
        cached = await fetch_and_cache_upstream(path, db_locale=db_loc)
        if cached:
            conn = get_db()
            cur = conn.cursor()
            row = cur.execute("SELECT * FROM grammar_courses WHERE id = ?", (course_id,)).fetchone()
        if not row:
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
        **loc_ctx,
        "locale_context": loc_ctx,
        "course": course_dict,
        "category": dict(cat_row) if cat_row else None,
        "blocks": blocks,
        "questions": questions
    })


@app.get("/{locale}/reading")
async def reading_overview_view(request: Request, locale: str = "fr-EN"):
    """Render Reading Comprehension Overview."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="reading")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    col_rows = cur.execute("SELECT * FROM reading_collections WHERE locale = ? ORDER BY position ASC", (db_loc,)).fetchall()
    if not col_rows and db_loc == "fr":
        col_rows = cur.execute("SELECT * FROM reading_collections ORDER BY position ASC").fetchall()
    collections = []
    for c in col_rows:
        c_dict = dict(c)
        story_rows = cur.execute("SELECT * FROM reading_stories WHERE collection_id = ? ORDER BY id ASC", (c_dict['id'],)).fetchall()
        c_dict['stories'] = [dict(s) for s in story_rows]
        collections.append(c_dict)
    conn.close()
    return templates.TemplateResponse(request, "reading_overview.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "collections": collections
    })


@app.get("/{locale}/reading/{col_id}/{slug}")
@app.get("/{locale}/reading/{col_id}")
async def reading_collection_view(col_id: int, request: Request, locale: str = "fr-EN", slug: Optional[str] = None):
    """Render stories in a Reading Collection."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="reading")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    col_row = cur.execute("SELECT * FROM reading_collections WHERE id = ?", (col_id,)).fetchone()
    if not col_row:
        conn.close()
        upstream_slug = slug or ""
        path = f"{loc_ctx['locale']}/reading/{col_id}/{upstream_slug}".rstrip("/")
        cached = await fetch_and_cache_upstream(path, db_locale=db_loc)
        if cached:
            conn = get_db()
            cur = conn.cursor()
            col_row = cur.execute("SELECT * FROM reading_collections WHERE id = ?", (col_id,)).fetchone()
        if not col_row:
            raise HTTPException(status_code=404, detail="Reading collection not found")
    stories = cur.execute("SELECT * FROM reading_stories WHERE collection_id = ? ORDER BY id ASC", (col_id,)).fetchall()
    conn.close()
    return templates.TemplateResponse(request, "reading_collection.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "collection": dict(col_row),
        "stories": [dict(s) for s in stories]
    })


@app.get("/{locale}/reading/course/{story_id}/{slug}/{segment}")
@app.get("/{locale}/reading/course/{story_id}/{slug}")
async def reading_story_view(story_id: int, request: Request, locale: str = "fr-EN", slug: Optional[str] = None, segment: Optional[str] = None):
    """Render Reading Story with multi-segment chapter stepper, aligned translation & audio."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="reading")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    story_row = cur.execute("SELECT * FROM reading_stories WHERE id = ?", (story_id,)).fetchone()
    if not story_row:
        conn.close()
        upstream_slug = slug or ""
        path = f"{loc_ctx['locale']}/reading/course/{story_id}/{upstream_slug}/0".rstrip("/")
        cached = await fetch_and_cache_upstream(path, db_locale=db_loc)
        if cached:
            conn = get_db()
            cur = conn.cursor()
            story_row = cur.execute("SELECT * FROM reading_stories WHERE id = ?", (story_id,)).fetchone()
        if not story_row:
            raise HTTPException(status_code=404, detail="Reading story not found")

    
    story_dict = dict(story_row)
    actual_slug = slug or story_dict.get('url_id', 'story')

    # If segment is not specified, redirect to segment 0 to match live LanGeek routing
    if segment is None:
        conn.close()
        return RedirectResponse(url=f"/{loc_ctx['locale']}/reading/course/{story_id}/{actual_slug}/0", status_code=307)

    try:
        current_segment_idx = int(segment)
    except ValueError:
        current_segment_idx = 0

    col_row = cur.execute("SELECT * FROM reading_collections WHERE id = ?", (story_dict.get('collection_id'),)).fetchone()
    seg_rows = cur.execute("SELECT * FROM reading_segments WHERE story_id = ? ORDER BY segment_index ASC", (story_id,)).fetchall()
    conn.close()

    segments = [dict(s) for s in seg_rows]
    current_segment = None
    if segments:
        if 0 <= current_segment_idx < len(segments):
            current_segment = segments[current_segment_idx]
        else:
            current_segment = segments[0]
            current_segment_idx = 0

    paragraphs = []
    if current_segment and current_segment.get('content_json'):
        try:
            paragraphs = json.loads(current_segment['content_json'])
        except Exception:
            pass
    elif story_dict.get('content_json'):
        try:
            paragraphs = json.loads(story_dict['content_json'])
        except Exception:
            pass

    prev_segment_idx = current_segment_idx - 1 if current_segment_idx > 0 else None
    next_segment_idx = current_segment_idx + 1 if (segments and current_segment_idx < len(segments) - 1) else None

    return templates.TemplateResponse(request, "reading_story.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
        "hide_site_nav": True,
        "hide_site_footer": True,
        "story": story_dict,
        "collection": dict(col_row) if col_row else None,
        "segments": segments,
        "current_segment_index": current_segment_idx,
        "current_segment": current_segment,
        "paragraphs": paragraphs,
        "prev_segment_index": prev_segment_idx,
        "next_segment_index": next_segment_idx
    })


@app.get("/{locale}/pronunciation")
async def pronunciation_overview_view(request: Request, locale: str = "fr-EN"):
    """Render Pronunciation Guide."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="pronunciation")
    return templates.TemplateResponse(request, "pronunciation_overview.html", {
        **loc_ctx,
        "locale_context": loc_ctx
    })


@app.get("/{locale}/pronunciation/101/alphabet-francais")
@app.get("/{locale}/pronunciation/alphabet-francais")
@app.get("/{locale}/pronunciation/101/alphabet-anglais")
@app.get("/{locale}/pronunciation/101/alphabet")
@app.get("/{locale}/pronunciation/alphabet")
async def pronunciation_alphabet_view(request: Request, locale: str = "fr-EN"):
    """Render Alphabet Guide with pronunciation."""
    if locale not in SUPPORTED_LOCALES:
        raise HTTPException(status_code=404, detail="Locale not found")
    loc_ctx = get_locale_context(locale, request, active_tab="pronunciation")
    db_loc = loc_ctx["db_locale"]
    conn = get_db()
    cur = conn.cursor()
    courses = cur.execute("SELECT * FROM pronunciation_courses WHERE locale = ? ORDER BY position ASC", (db_loc,)).fetchall()
    if not courses and db_loc == "fr":
        courses = cur.execute("SELECT * FROM pronunciation_courses ORDER BY position ASC").fetchall()
    conn.close()
    return templates.TemplateResponse(request, "pronunciation_alphabet.html", {
        **loc_ctx,
        "locale_context": loc_ctx,
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
