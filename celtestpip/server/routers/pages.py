"""HTML Page Views, Practice Catalog, and Dynamic Content routing.

Serves pre-rendered Next.js pages, full test simulator interfaces, CLB calculator,
and dynamic learning materials with in-memory caching and paywall stripping.
"""

import os
import ssl
import urllib.request
from typing import Optional
from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from celtestpip.server.config import (
    PAGES_DIR,
    PAGE_CACHE,
    PAGE_HEADERS,
    get_cached_template,
    normalize_exam_id,
)
from celtestpip.scripts.unlock_all_pro_content import clean_html

router = APIRouter(tags=["Pages"])


@router.get("/", response_class=HTMLResponse)
def index_page() -> HTMLResponse:
    """Home landing page with interactive skill categories and practice tests."""
    content = get_cached_template("index.html")
    if content:
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
        return HTMLResponse(PAGE_CACHE[safe_slug], headers=PAGE_HEADERS)

    page_file = os.path.join(PAGES_DIR, f"{safe_slug}.html")
    if os.path.exists(page_file) and os.path.getsize(page_file) > 0:
        with open(page_file, "r", encoding="utf-8") as f:
            content = f.read()
        cleaned = clean_html(content)
        PAGE_CACHE[safe_slug] = cleaned
        return HTMLResponse(cleaned, headers=PAGE_HEADERS)

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
                with open(page_file, "w", encoding="utf-8") as f:
                    f.write(cleaned)
                PAGE_CACHE[safe_slug] = cleaned
                return HTMLResponse(cleaned, headers=PAGE_HEADERS)
    except Exception:
        pass

    raise HTTPException(status_code=404, detail="Page not found")
