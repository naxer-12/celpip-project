"""HTML Page Views, Practice Catalog, and Dynamic Content routing.

Serves pre-rendered Next.js pages, full test simulator interfaces, CLB calculator,
and dynamic learning materials with in-memory caching and paywall stripping.
"""

import os
import ssl
import urllib.request
from typing import Optional
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse

from celtestpip.server.config import (
    STATIC_DIR,
    PAGES_DIR,
    PAGE_CACHE,
    PAGE_HEADERS,
    get_cached_template,
    normalize_exam_id,
)
from celtestpip.scripts.unlock_all_pro_content import clean_html
from celtestpip.scripts.rewrite_all_site_links import rewrite_celtestpip_links

router = APIRouter(tags=["Pages"])


def _apply_course_progress(content: str, slug: str) -> str:
    """Inject completed course sections into pre-rendered course HTML and Flight state."""
    import re
    from celtestpip.server.database import get_completed_course_sections
    completed_sections = get_completed_course_sections()
    if not completed_sections:
        return content

    for sec_id in completed_sections:
        content = re.sub(
            r'(\\\"id\\\":\\\"' + re.escape(sec_id) + r'\\\"(?:(?!\\\"id\\\":).)*?\\\"isCompleted\\\":)false',
            r'\g<1>true',
            content
        )

    # Check if current lesson is completed
    section_slug = slug.split("/")[-1] if "/" in slug else slug
    m = re.search(r'\\\"id\\\":\\\"([a-z0-9]+)\\\"[^\}]*?\\\"slug\\\":\\\"' + re.escape(section_slug) + r'\\\"', content)
    current_id = m.group(1) if m else None
    if current_id and current_id in completed_sections:
        content = content.replace(r'\"isCompleted\":false,\"outline\":', r'\"isCompleted\":true,\"outline\":')
        content = content.replace("Finished this lesson?", "Lesson complete")
        content = content.replace("Mark as complete", "Mark as not done")
        content = content.replace("Mark it done so your course progress stays accurate.", "It counts towards your course progress. Carry on to the next lesson below.")
    return content


@router.post("/api/debug-log")
async def client_debug_logger(request: Request):
    """Log arbitrary client debugging data."""
    try:
        body = await request.body()
        print(">>> CLIENT DEBUG:", body.decode("utf-8", errors="replace"))
    except Exception as e:
        print(">>> CLIENT DEBUG ERROR:", e)
    return {"ok": True}


@router.post("/api/client-error")
async def client_error_logger(request: Request):
    """Log client error details."""
    try:
        body = await request.body()
        print(">>> CLIENT ERROR RECEIVED:", body.decode("utf-8", errors="replace"))
    except Exception as e:
        print(">>> CLIENT ERROR LOGGING FAILED:", e)
    return {"ok": True}


@router.post("/cdn-cgi/rum")
def client_telemetry_stub():
    """Absorb client logging and telemetry gracefully."""
    return {"ok": True}


@router.get("/", response_class=HTMLResponse)
def index_page() -> HTMLResponse:
    """Home landing page with interactive skill categories and practice tests."""
    if "_index_v2" in PAGE_CACHE:
        return HTMLResponse(PAGE_CACHE["_index_v2"], headers=PAGE_HEADERS)
    path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace("1191lj8_x8otc.js", "1191lj8_x8otc_v2.js")
        PAGE_CACHE["_index_v2"] = content
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Local Server Running</h1>", headers=PAGE_HEADERS)


@router.get("/exams", response_class=HTMLResponse)
def exams_catalog_page() -> HTMLResponse:
    """Exams catalog page listing all 60 full CELPIP practice tests."""
    content = get_cached_template("exams.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exams Catalog</h1>", headers=PAGE_HEADERS)


@router.get("/exams/{exam_id}", response_class=HTMLResponse)
def exam_landing_page(exam_id: str) -> HTMLResponse:
    """Exam landing page, automatically starting at Part 1."""
    exam_id = normalize_exam_id(exam_id)
    return exam_page(exam_id, 1)


@router.get("/exams/{exam_id}/results", response_class=HTMLResponse)
def exam_results_page(exam_id: str, partNumber: Optional[str] = None) -> HTMLResponse:
    """Exam scoring and results review page."""
    exam_id = normalize_exam_id(exam_id)
    content = get_cached_template("exam.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exam Results</h1>", headers=PAGE_HEADERS)


@router.get("/exams/{exam_id}/part{part_number}", response_class=HTMLResponse)
def exam_page_slug(exam_id: str, part_number: int) -> HTMLResponse:
    """Exam simulation runner with slug route (e.g. /exams/exam1/part1)."""
    exam_id = normalize_exam_id(exam_id)
    return exam_page(exam_id, part_number)


@router.get("/exams/{exam_id}/part/{part_number}", response_class=HTMLResponse)
def exam_page(exam_id: str, part_number: int) -> HTMLResponse:
    """Full-screen CELPIP exam simulation interface."""
    exam_id = normalize_exam_id(exam_id)
    content = get_cached_template("exam.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CELTESTPIP Exam Page</h1>", headers=PAGE_HEADERS)


@router.get("/tools/clb-calculator", response_class=HTMLResponse)
def calculator_page() -> HTMLResponse:
    """Interactive Canadian Language Benchmark (CLB) score calculator tool."""
    content = get_cached_template("calculator.html")
    if content:
        return HTMLResponse(content, headers=PAGE_HEADERS)
    return HTMLResponse("<h1>CLB Calculator</h1>", headers=PAGE_HEADERS)


@router.get("/{full_path:path}", response_class=HTMLResponse)
def dynamic_content_page(full_path: str) -> HTMLResponse:
    """Serve any replicated content page (practice sets, study guides, vocabulary)."""
    slug = full_path.strip("/")
    if not slug:
        return index_page()

    safe_slug = slug.replace("/", "_")
    if safe_slug in PAGE_CACHE:
        content = PAGE_CACHE[safe_slug]
        if safe_slug.startswith("courses_"):
            content = _apply_course_progress(content, slug)
        return HTMLResponse(content, headers=PAGE_HEADERS)

    page_file = os.path.join(PAGES_DIR, f"{safe_slug}.html")
    if os.path.exists(page_file) and os.path.getsize(page_file) > 0:
        with open(page_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = (
            content.replace("2fvw__nnw3kbd.js", "2fvw__nnw3kbd_v2.js")
            .replace("24w9ng0sqrv9g.js", "24w9ng0sqrv9g_v2.js")
            .replace("00m674sfix9n3.js", "00m674sfix9n3_v2.js")
            .replace("1191lj8_x8otc.js", "1191lj8_x8otc_v2.js")
        )
        content = rewrite_celtestpip_links(content)
        PAGE_CACHE[safe_slug] = content
        if safe_slug.startswith("courses_"):
            content = _apply_course_progress(content, slug)
        return HTMLResponse(content, headers=PAGE_HEADERS)

    # Remote fallback to crawl missing content pages on demand
    remote_url = f"https://www.celtestpip.com/{slug}"
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(remote_url, headers={"User-Agent": "Mozilla/5.0 (CELTESTPIP Replica)"})
        with urllib.request.urlopen(req, context=ctx, timeout=8) as resp:
            if resp.status == 200:
                content = resp.read().decode("utf-8", errors="replace")
                cleaned = clean_html(content)
                cleaned = rewrite_celtestpip_links(cleaned)
                with open(page_file, "w", encoding="utf-8") as f:
                    f.write(cleaned)
                PAGE_CACHE[safe_slug] = cleaned
                if safe_slug.startswith("courses_"):
                    cleaned = _apply_course_progress(cleaned, slug)
                return HTMLResponse(cleaned, headers=PAGE_HEADERS)
    except Exception:
        pass

    raise HTTPException(status_code=404, detail="Page not found")
