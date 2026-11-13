"""Asynchronous Sitemap & Route Crawler for LanGeek French (fr-EN).

Discovers, extracts, cleans, and checkpoints HTML and React data payloads,
automatically indexing vocabulary, flashcards, and grammar into SQLite.
"""

import os
import ssl
import sys
import argparse
import asyncio
import logging
import urllib.request
import xml.etree.ElementTree as ET
from typing import List, Set, Optional
import httpx

from langeek.cleaner import clean_replica_html
from langeek.build_db import (
    init_db, extract_next_data, index_subcategory_page,
    index_grammar_page, rebuild_fts_index
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("langeek_crawler")

BASE_URL = "https://langeek.co"
TARGET_LOCALE = "/fr-EN"

def get_fr_en_sitemap_urls(limit: Optional[int] = None) -> List[str]:
    """Parse LanGeek sitemaps (sitemap-0, 1, 3) and extract all canonical /fr-EN URLs."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

    # Sitemaps 0, 1, and 3 contain the fr-EN content
    target_sitemaps = [
        f"{BASE_URL}/sitemap-0.xml",
        f"{BASE_URL}/sitemap-1.xml",
        f"{BASE_URL}/sitemap-3.xml"
    ]

    discovered = []
    for sm in target_sitemaps:
        try:
            req = urllib.request.Request(sm, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
                root = ET.fromstring(resp.read())
                for child in root:
                    loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
                    if loc is not None and loc.text:
                        url = loc.text.strip()
                        if "/fr-EN" in url:
                            discovered.append(url)
                            if limit and len(discovered) >= limit:
                                return discovered
        except Exception as e:
            logger.error(f"Error reading sitemap {sm}: {e}")

    logger.info(f"Discovered {len(discovered)} total canonical fr-EN URLs across sitemaps.")
    return discovered


def url_to_safe_filename(url: str) -> str:
    """Convert URL path to canonical disk filename (ignoring query strings)."""
    path = url.replace(BASE_URL, "").split("?")[0].strip("/") or "home"
    safe = path.replace("/", "_")
    return safe + ".html"


async def crawl_and_process_url(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    url: str,
    output_dir: str,
    db_path: str,
    skip_existing: bool = True
) -> bool:
    """Fetch single page, clean paywalls/auth, save to disk, and index into SQLite."""
    safe_name = url_to_safe_filename(url)
    dest_path = os.path.join(output_dir, safe_name)

    if skip_existing and os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return True

    async with sem:
        try:
            resp = await client.get(url)
            if resp.status_code == 200:
                raw_html = resp.text
                cleaned_html = clean_replica_html(raw_html)

                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(cleaned_html)

                # Index structured data into SQLite
                next_data = extract_next_data(raw_html)
                if next_data:
                    conn = init_db(db_path)
                    try:
                        if "/vocab/subcategory/" in url:
                            index_subcategory_page(conn, next_data)
                        elif "/grammar/course/" in url:
                            index_grammar_page(conn, next_data)
                    finally:
                        conn.close()

                logger.info(f"Saved & Indexed: {safe_name} ({len(cleaned_html)} bytes)")
                return True
            else:
                logger.warning(f"Failed {url}: HTTP {resp.status_code}")
                return False
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return False


async def run_crawl_pipeline(
    output_dir: str = "langeek/data/pages",
    db_path: str = "langeek/data/langeek.db",
    concurrency: int = 10,
    limit: Optional[int] = None,
    specific_urls: Optional[List[str]] = None
):
    """Run full async crawler pipeline."""
    os.makedirs(output_dir, exist_ok=True)
    conn = init_db(db_path)
    conn.close()

    urls = specific_urls or get_fr_en_sitemap_urls(limit=limit)
    if limit and len(urls) > limit:
        urls = urls[:limit]

    logger.info(f"Beginning crawl for {len(urls)} pages with concurrency={concurrency}...")

    sem = asyncio.Semaphore(concurrency)
    limits = httpx.Limits(max_keepalive_connections=concurrency, max_connections=concurrency + 5)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    async with httpx.AsyncClient(verify=False, limits=limits, headers=headers, timeout=25.0) as client:
        tasks = [crawl_and_process_url(client, sem, u, output_dir, db_path) for u in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    success_count = sum(1 for r in results if r is True)
    logger.info(f"Crawl completed: {success_count}/{len(urls)} pages stored.")

    # Rebuild FTS5 search index
    conn = init_db(db_path)
    rebuild_fts_index(conn)
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LanGeek French Crawler")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of pages to crawl")
    parser.add_argument("--concurrency", type=int, default=10, help="Concurrent HTTP requests")
    parser.add_argument("--output", type=str, default="langeek/data/pages", help="Output directory")
    parser.add_argument("--db", type=str, default="langeek/data/langeek.db", help="SQLite database path")
    args = parser.parse_args()

    asyncio.run(run_crawl_pipeline(
        output_dir=args.output,
        db_path=args.db,
        concurrency=args.concurrency,
        limit=args.limit
    ))
