import os
import re
import json
import hashlib
import asyncio
import logging
from typing import List, Tuple, Dict, Set, Optional
import httpx

logger = logging.getLogger(__name__)


def get_safe_filename(url: str) -> str:
    """Generate a safe, unique filename for a media asset URL."""
    clean_url = url.split("?")[0]
    basename = os.path.basename(clean_url)
    ext = os.path.splitext(basename)[1].lower()
    if not ext:
        ext = ".mp3" if "audio" in url.lower() else ".jpg"
    hash_prefix = hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]
    clean_base = re.sub(r'[^a-zA-Z0-9_\-]', '_', os.path.splitext(basename)[0])[:30]
    return f"{clean_base}_{hash_prefix}{ext}"


def scan_media_urls(parts: List[Dict]) -> Tuple[Set[str], Set[str]]:
    """Scan raw exam parts and collect unique audio and image URLs."""
    audio_urls: Set[str] = set()
    image_urls: Set[str] = set()

    for p in parts:
        if not isinstance(p, dict):
            continue
        for a in p.get("audio_urls", []) or []:
            if isinstance(a, str) and a.startswith("http"):
                audio_urls.add(a)
        img = p.get("image_url")
        if isinstance(img, str) and img.startswith("http"):
            image_urls.add(img)
        for q in p.get("questions", []) or []:
            if isinstance(q, dict):
                qa = q.get("audio_url")
                if isinstance(qa, str) and qa.startswith("http"):
                    audio_urls.add(qa)

    return audio_urls, image_urls


async def download_file(client: httpx.AsyncClient, url: str, dest_path: str) -> bool:
    """Download a single media asset with checkpointing."""
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return True
    try:
        resp = await client.get(url, follow_redirects=True)
        if resp.status_code == 200:
            with open(dest_path, "wb") as f:
                f.write(resp.content)
            return True
        logger.warning(f"HTTP {resp.status_code} downloading {url}")
    except Exception as e:
        logger.error(f"Error downloading {url}: {e}")
    return False


async def download_all_media(
    audio_urls: Set[str],
    image_urls: Set[str],
    base_dir: str = "celtestpip/data/media",
    concurrency: int = 10
) -> Dict[str, str]:
    """Download all collected audio and image assets and create media_map.json."""
    audio_dir = os.path.join(base_dir, "audio")
    image_dir = os.path.join(base_dir, "images")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    media_map: Dict[str, str] = {}
    sem = asyncio.Semaphore(concurrency)

    async with httpx.AsyncClient(timeout=30.0) as client:
        tasks = []

        for url in audio_urls:
            fn = get_safe_filename(url)
            dest = os.path.join(audio_dir, fn)
            media_map[url] = f"/media/audio/{fn}"

            async def t_audio(u: str = url, d: str = dest):
                async with sem:
                    await download_file(client, u, d)

            tasks.append(t_audio())

        for url in image_urls:
            fn = get_safe_filename(url)
            dest = os.path.join(image_dir, fn)
            media_map[url] = f"/media/images/{fn}"

            async def t_image(u: str = url, d: str = dest):
                async with sem:
                    await download_file(client, u, d)

            tasks.append(t_image())

        await asyncio.gather(*tasks)

    map_file = os.path.join(base_dir, "media_map.json")
    with open(map_file, "w", encoding="utf-8") as f:
        json.dump(media_map, f, indent=2, ensure_ascii=False)

    return media_map


def load_all_exam_parts(raw_exams_dir: str = "celtestpip/data/raw/exams") -> List[Dict]:
    """Load all exam parts from disk."""
    parts = []
    if not os.path.exists(raw_exams_dir):
        return parts

    for fname in sorted(os.listdir(raw_exams_dir)):
        if fname.endswith(".json"):
            path = os.path.join(raw_exams_dir, fname)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        parts.append(data)
            except Exception as e:
                logger.warning(f"Failed to read exam part {path}: {e}")

    return parts


async def main():
    logging.basicConfig(level=logging.INFO)
    parts = load_all_exam_parts()
    logger.info(f"Loaded {len(parts)} exam parts.")
    audio_urls, image_urls = scan_media_urls(parts)
    logger.info(f"Found {len(audio_urls)} audio assets and {len(image_urls)} image assets.")
    media_map = await download_all_media(audio_urls, image_urls)
    logger.info(f"Media mapping complete with {len(media_map)} assets mapped.")


if __name__ == "__main__":
    asyncio.run(main())
