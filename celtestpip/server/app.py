"""CELTESTPIP Local Application Server.

A modular, production-grade FastAPI application powering the offline CELPIP
exam simulation, practice questions engine, Canadian Language Benchmark (CLB)
scoring system, and vocabulary word bank.
"""

import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response

from celtestpip.server.config import (
    BASE_DIR,
    STATIC_DIR,
    MEDIA_DIR,
    PAGES_DIR,
    NEXT_STATIC_DIR,
    ANIMATION_DIR,
    DB_PATH,
    PAGE_CACHE,
    PAGE_HEADERS,
    STATIC_HEADERS,
    normalize_exam_id,
    get_cached_template,
    prewarm_page_cache,
)
from celtestpip.server.database import init_db
from celtestpip.scripts.unlock_all_pro_content import clean_html
from celtestpip.server.routers import (
    exams_router,
    practices_router,
    vocabulary_router,
    user_router,
    clerk_router,
    assets_router,
    pages_router,
)

CURSORS_DIR = os.path.join(STATIC_DIR, "cursors")
AVATAR_DIR = os.path.join(STATIC_DIR, "img", "avatar")


def ensure_db() -> None:
    """Ensure database exists and tables are initialized."""
    if not os.path.exists(DB_PATH):
        init_db(DB_PATH)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager for startup and shutdown hooks."""
    ensure_db()
    prewarm_page_cache()
    yield


app = FastAPI(
    title="CELTESTPIP Local Replica Server",
    description="Offline-first CELPIP Exam Preparation Platform & Simulator",
    version="2.0.0",
    lifespan=lifespan,
)


class HeadMiddleware(BaseHTTPMiddleware):
    """Intercept HTTP HEAD requests and return matching headers without body."""
    async def dispatch(self, request: Request, call_next):
        if request.method == "HEAD":
            request.scope["method"] = "GET"
            response = await call_next(request)
            return Response(
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type,
            )
        return await call_next(request)


# 1. Register Middlewares
app.add_middleware(HeadMiddleware)
app.add_middleware(GZipMiddleware, minimum_size=1000)

# 2. Mount Static Assets Directories
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
if os.path.exists(CURSORS_DIR):
    app.mount("/cursors", StaticFiles(directory=CURSORS_DIR), name="cursors")
if os.path.exists(AVATAR_DIR):
    app.mount("/avatar", StaticFiles(directory=AVATAR_DIR), name="avatar")
if os.path.exists(ANIMATION_DIR):
    app.mount("/animation", StaticFiles(directory=ANIMATION_DIR), name="animation")

# 3. Include Routers
app.include_router(assets_router)
app.include_router(exams_router)
app.include_router(practices_router)
app.include_router(vocabulary_router)
app.include_router(user_router)
app.include_router(clerk_router)
# Pages router MUST be included last because of the catch-all dynamic /{full_path:path} route
app.include_router(pages_router)

__all__ = [
    "app",
    "DB_PATH",
    "BASE_DIR",
    "STATIC_DIR",
    "MEDIA_DIR",
    "PAGES_DIR",
    "NEXT_STATIC_DIR",
    "ANIMATION_DIR",
    "PAGE_CACHE",
    "PAGE_HEADERS",
    "STATIC_HEADERS",
    "normalize_exam_id",
    "get_cached_template",
    "prewarm_page_cache",
    "ensure_db",
    "clean_html",
]
