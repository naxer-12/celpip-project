import os
import re
import ssl
import asyncio
import logging
import urllib.request
import xml.etree.ElementTree as ET
from typing import List
import httpx

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
os.makedirs(PAGES_DIR, exist_ok=True)

SITEMAP_URL = "https://www.celtestpip.com/sitemap.xml"
NON_ENGLISH_PREFIXES = ("/zh", "/ko", "/ja", "/es", "/fr", "/pa", "/hi", "/fa")

def get_sitemap_urls() -> List[str]:
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(SITEMAP_URL, headers={"User-Agent": "Mozilla/5.0"})
    content = urllib.request.urlopen(req, context=ctx, timeout=15).read()
    root = ET.fromstring(content)
    
    urls = []
    for child in root:
        loc = child.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        if loc is not None and loc.text:
            u = loc.text.strip()
            path = u.replace("https://www.celtestpip.com", "")
            if not any(path.startswith(prefix) for prefix in NON_ENGLISH_PREFIXES):
                urls.append(u)
    return urls

async def download_page(client: httpx.AsyncClient, sem: asyncio.Semaphore, url: str) -> bool:
    slug = url.replace("https://www.celtestpip.com", "").strip("/")
    if not slug:
        slug = "home"
    if slug == "exams":
        return True
    
    safe_slug = slug.replace("/", "_") + ".html"
    dest_path = os.path.join(PAGES_DIR, safe_slug)
    
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return True
    
    async with sem:
        try:
            resp = await client.get(url)
            if resp.status_code == 200:
                with open(dest_path, "w", encoding="utf-8") as f:
                    f.write(resp.text)
                logger.info(f"Saved {safe_slug} ({len(resp.text)} bytes)")
                return True
            else:
                logger.warning(f"Failed {url}: HTTP {resp.status_code}")
                return False
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return False

async def main():
    urls = get_sitemap_urls()
    logger.info(f"Found {len(urls)} English URLs in sitemap")
    
    sem = asyncio.Semaphore(20)
    limits = httpx.Limits(max_keepalive_connections=20, max_connections=25)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
    }
    
    async with httpx.AsyncClient(verify=False, limits=limits, headers=headers, timeout=25.0) as client:
        tasks = [download_page(client, sem, u) for u in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
    
    successful = sum(1 for r in results if r is True)
    logger.info(f"Successfully downloaded and cached {successful}/{len(urls)} pages to {PAGES_DIR}")

if __name__ == "__main__":
    asyncio.run(main())
