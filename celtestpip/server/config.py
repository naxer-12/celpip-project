"""Configuration, constants, paths, and caching policies for CELTESTPIP."""

import os
from typing import Dict
from celtestpip.scripts.unlock_all_pro_content import clean_html

# Directory paths
SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SERVER_DIR)
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "data", "media")
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
NEXT_STATIC_DIR = os.path.join(STATIC_DIR, "_next", "static")
ANIMATION_DIR = os.path.join(STATIC_DIR, "animation")
DB_PATH = os.environ.get("CELTESTPIP_DB_PATH", os.path.join(BASE_DIR, "data", "celtestpip.db"))

# HTTP Cache-Control headers
IMMUTABLE_HEADERS = {"Cache-Control": "public, max-age=31536000, immutable"}
STATIC_HEADERS = {"Cache-Control": "public, max-age=86400"}
PAGE_HEADERS = {"Cache-Control": "no-cache, must-revalidate"}

# In-memory page cache for sub-millisecond response times
PAGE_CACHE: Dict[str, str] = {}


def normalize_exam_id(exam_id: str) -> str:
    """Normalize exam identifiers, ensuring numeric IDs like '1' map to 'exam1'."""
    if not exam_id.startswith("exam") and exam_id.isdigit():
        return f"exam{exam_id}"
    return exam_id


def get_cached_template(filename: str) -> str:
    """Retrieve and clean a static HTML template with in-memory caching."""
    if filename in PAGE_CACHE:
        return PAGE_CACHE[filename]
    path = os.path.join(STATIC_DIR, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = clean_html(f.read())
        PAGE_CACHE[filename] = content
        return content
    return ""


def prewarm_page_cache() -> None:
    """Pre-warm frequently accessed static pages into in-memory cache on startup."""
    for fn in ["index.html", "exams.html", "exam.html", "calculator.html"]:
        p = os.path.join(STATIC_DIR, fn)
        if os.path.exists(p):
            try:
                with open(p, "r", encoding="utf-8") as f:
                    PAGE_CACHE[fn] = clean_html(f.read())
            except Exception:
                pass

    if os.path.exists(PAGES_DIR):
        for pf in ["home.html", "listening.html", "reading.html", "writing.html", "speaking.html", "words.html"]:
            p = os.path.join(PAGES_DIR, pf)
            if os.path.exists(p):
                slug = pf.replace(".html", "")
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        PAGE_CACHE[slug] = clean_html(f.read())
                except Exception:
                    pass
