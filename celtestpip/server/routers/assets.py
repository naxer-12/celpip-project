"""Static assets, media streaming, icons, and Next.js static bundles.

Serves local audio/images with fallback to cached blob storage, Next.js immutable
chunks with long-lived Cache-Control headers, and application manifest/icons.
"""

import os
import re
import ssl
import hashlib
import mimetypes
import urllib.request
from typing import Optional
from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import FileResponse

from celtestpip.server.config import (
    STATIC_DIR,
    MEDIA_DIR,
    NEXT_STATIC_DIR,
    STATIC_HEADERS,
)

router = APIRouter(tags=["Assets"])

MEDIA_CACHE_DIR = os.path.join(MEDIA_DIR, "cache")
os.makedirs(MEDIA_CACHE_DIR, exist_ok=True)
AVATAR_DIR = os.path.join(STATIC_DIR, "img", "avatar")

IMMUTABLE_HEADERS = {
    "Cache-Control": "public, max-age=31536000, immutable",
    "X-Content-Type-Options": "nosniff",
}


@router.get("/media/{file_path:path}")
def serve_media(file_path: str):
    """Serve media files (audio mp3/wav, test images) from local storage or cache."""
    # 1. Local media directory
    local_path = os.path.join(MEDIA_DIR, file_path)
    if os.path.exists(local_path) and os.path.isfile(local_path):
        return FileResponse(local_path, headers=STATIC_HEADERS)

    # 2. Local media cache
    safe_name = re.sub(r'[^a-zA-Z0-9_\-\.]', '_', file_path)
    cache_path = os.path.join(MEDIA_CACHE_DIR, safe_name)
    if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
        return FileResponse(cache_path, headers=STATIC_HEADERS)

    # 3. Remote Vercel Blob storage fallback
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
            return FileResponse(cache_path, media_type=content_type, headers=STATIC_HEADERS)
    except Exception:
        raise HTTPException(status_code=404, detail="Media asset not found")


@router.get("/_next/static/{file_path:path}")
def serve_next_static(file_path: str):
    """Serve Next.js immutable bundles, stylesheets, and fonts."""
    is_immutable = "immutable" in file_path
    headers = IMMUTABLE_HEADERS if is_immutable else STATIC_HEADERS

    local_file = os.path.join(NEXT_STATIC_DIR, file_path)
    if os.path.exists(local_file) and os.path.isfile(local_file):
        return FileResponse(local_file, headers=headers)

    base_name = os.path.basename(file_path)
    for sub in ["css", "js", "fonts", "img"]:
        cand = os.path.join(STATIC_DIR, sub, base_name)
        if os.path.exists(cand) and os.path.isfile(cand):
            return FileResponse(cand, headers=headers)

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


@router.get("/manifest.webmanifest")
def get_manifest():
    """Application web manifest."""
    mf = os.path.join(STATIC_DIR, "manifest.webmanifest")
    if os.path.exists(mf):
        return FileResponse(mf, media_type="application/manifest+json", headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)


@router.get("/icon.png")
@router.get("/apple-icon.png")
def get_icon():
    """Application icons."""
    p = os.path.join(STATIC_DIR, "img", "icon.png")
    if os.path.exists(p):
        return FileResponse(p, media_type="image/png", headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)


@router.get("/favicon.ico")
def get_favicon():
    """Application favicon."""
    fav = os.path.join(STATIC_DIR, "img", "favicon.ico")
    if os.path.exists(fav):
        return FileResponse(fav, headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)


@router.get("/logo.png")
def get_logo():
    """Brand logo image."""
    logo = os.path.join(STATIC_DIR, "img", "logo.png")
    if os.path.exists(logo):
        return FileResponse(logo, headers=STATIC_HEADERS)
    raise HTTPException(status_code=404)


IMG_CACHE_DIR = os.path.join(STATIC_DIR, "img", "cache")
os.makedirs(IMG_CACHE_DIR, exist_ok=True)


@router.get("/_next/image")
def get_next_image(url: str = "/logo.png", w: Optional[int] = None, q: Optional[int] = None):
    """Next.js Image Optimization proxy serving optimized images with disk caching."""
    # 1. Local avatar matching
    if "avatar" in url and not url.startswith("http"):
        m = re.search(r'(\d+)\.jpg', url)
        if m:
            av_path = os.path.join(AVATAR_DIR, f"{m.group(1)}.jpg")
            if os.path.exists(av_path):
                return FileResponse(av_path, headers=STATIC_HEADERS)

    # 2. Local static assets
    if url.startswith("/"):
        clean_path = url.lstrip("/")
        local_cand = os.path.join(STATIC_DIR, clean_path)
        if os.path.exists(local_cand) and os.path.isfile(local_cand):
            return FileResponse(local_cand, headers=STATIC_HEADERS)
        if "logo" in url:
            return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"), headers=STATIC_HEADERS)
        if "icon" in url:
            return FileResponse(os.path.join(STATIC_DIR, "img", "icon.png"), headers=STATIC_HEADERS)

    # 3. Remote URL caching (Vercel blob, Google user content, external illustrations)
    if url.startswith("http://") or url.startswith("https://"):
        ext = ".jpg"
        if ".png" in url:
            ext = ".png"
        elif ".webp" in url:
            ext = ".webp"
        elif ".jpeg" in url:
            ext = ".jpeg"
        elif ".svg" in url:
            ext = ".svg"

        url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
        cached_file = os.path.join(IMG_CACHE_DIR, f"{url_hash}{ext}")

        if os.path.exists(cached_file) and os.path.getsize(cached_file) > 0:
            content_type, _ = mimetypes.guess_type(cached_file)
            return FileResponse(cached_file, media_type=content_type or "image/jpeg", headers=STATIC_HEADERS)

        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (CELTESTPIP Replica)"})
            with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
                if resp.status == 200:
                    data = resp.read()
                    with open(cached_file, "wb") as f:
                        f.write(data)
                    content_type = resp.headers.get("Content-Type", "image/jpeg")
                    return Response(content=data, media_type=content_type, headers=STATIC_HEADERS)
        except Exception:
            pass

    return FileResponse(os.path.join(STATIC_DIR, "img", "logo.png"), headers=STATIC_HEADERS)
