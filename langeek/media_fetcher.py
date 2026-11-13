"""Asynchronous Media & Audio Cache Fetcher for LanGeek Replica.

Harvests dual-accent French audio pronunciations (France & Canada) and
illustration thumbnails from LanGeek CDN for 100% offline usage.
"""

import os
import sqlite3
import hashlib
import asyncio
import logging
import argparse
from typing import Optional
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("langeek_media")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MEDIA_DIR = os.path.join(BASE_DIR, "data", "media")
AUDIO_DIR = os.path.join(MEDIA_DIR, "audio")
IMAGES_DIR = os.path.join(MEDIA_DIR, "images")
DB_PATH = os.path.join(BASE_DIR, "data", "langeek.db")

async def download_asset(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    url: str,
    dest_dir: str,
    file_ext: str = ".mp3"
) -> Optional[str]:
    """Download single media file with hash-based filename checkpointing."""
    if not url:
        return None
    url_hash = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
    fname = f"{url_hash}{file_ext}"
    dest_path = os.path.join(dest_dir, fname)

    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 100:
        return dest_path

    async with sem:
        try:
            resp = await client.get(url)
            if resp.status_code == 200:
                os.makedirs(dest_dir, exist_ok=True)
                with open(dest_path, "wb") as f:
                    f.write(resp.content)
                logger.debug(f"Saved media: {fname} ({len(resp.content)} bytes)")
                return dest_path
            else:
                logger.warning(f"Failed media {url}: {resp.status_code}")
                return None
        except Exception as e:
            logger.warning(f"Error media {url}: {e}")
            return None


async def harvest_media(db_path: str = DB_PATH, concurrency: int = 10, limit: Optional[int] = None):
    """Scan words table in SQLite and download audio & image files."""
    if not os.path.exists(db_path):
        logger.error(f"Database {db_path} not found.")
        return

    os.makedirs(AUDIO_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    query = "SELECT id, entry, audio_url, audio_ca_url, thumb_url, photo_url FROM words"
    if limit:
        query += f" LIMIT {limit}"
    rows = cur.execute(query).fetchall()
    conn.close()

    logger.info(f"Harvesting media for {len(rows)} vocabulary entries...")

    sem = asyncio.Semaphore(concurrency)
    limits = httpx.Limits(max_keepalive_connections=concurrency, max_connections=concurrency + 5)
    headers = {"User-Agent": "Mozilla/5.0"}

    async with httpx.AsyncClient(verify=False, limits=limits, headers=headers, timeout=20.0) as client:
        tasks = []
        for r in rows:
            _, _, audio_fr, audio_ca, thumb, photo = r
            if audio_fr:
                tasks.append(download_asset(client, sem, audio_fr, AUDIO_DIR, ".mp3"))
            if audio_ca:
                tasks.append(download_asset(client, sem, audio_ca, AUDIO_DIR, "_ca.mp3"))
            if thumb:
                tasks.append(download_asset(client, sem, thumb, IMAGES_DIR, ".jpeg"))
            elif photo:
                tasks.append(download_asset(client, sem, photo, IMAGES_DIR, ".jpeg"))

        results = await asyncio.gather(*tasks, return_exceptions=True)

    success_cnt = sum(1 for res in results if res and isinstance(res, str))
    logger.info(f"Media harvesting finished: {success_cnt}/{len(tasks)} files cached.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LanGeek Media Harvester")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of entries")
    parser.add_argument("--concurrency", type=int, default=10, help="Concurrency level")
    parser.add_argument("--db", type=str, default=DB_PATH, help="SQLite DB path")
    args = parser.parse_args()

    asyncio.run(harvest_media(db_path=args.db, concurrency=args.concurrency, limit=args.limit))
