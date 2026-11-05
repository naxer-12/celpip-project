import os
import re
import json
import asyncio
import logging
import xml.etree.ElementTree as ET
from typing import List, Dict, Any, Optional
import httpx

logger = logging.getLogger(__name__)

BASE_URL = "https://www.celtestpip.com"
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def parse_sitemap_urls(xml_text: str) -> List[str]:
    """Extract all URLs from a sitemap XML document."""
    urls = []
    try:
        root = ET.fromstring(xml_text)
        for elem in root.iter():
            if elem.tag.endswith("loc") and elem.text:
                urls.append(elem.text.strip())
    except Exception as e:
        logger.error(f"Error parsing sitemap XML: {e}")
    return urls


def extract_page_content(html_text: str, url: str) -> Dict[str, Any]:
    """Extract metadata, title, and body content from an HTML document."""
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else url

    # Extract meta description (support both name before content and content before name)
    desc_match = re.search(r'<meta\s+[^>]*name=["\']description["\']\s+content=["\'](.*?)["\']', html_text, re.IGNORECASE)
    if not desc_match:
        desc_match = re.search(r'<meta\s+[^>]*content=["\'](.*?)["\']\s+name=["\']description["\']', html_text, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else ""

    # Extract article/main content
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_text, re.IGNORECASE | re.DOTALL)
    content_html = main_match.group(1).strip() if main_match else html_text

    slug = url.replace(BASE_URL, "").strip("/") or "home"
    return {
        "slug": slug,
        "url": url,
        "title": title,
        "description": description,
        "content_html": content_html,
    }


async def crawl_page(
    client: Optional[httpx.AsyncClient],
    url: str,
    output_dir: str = "celtestpip/data/raw/pages",
) -> Optional[Dict[str, Any]]:
    """Crawl a single content page with disk checkpointing."""
    os.makedirs(output_dir, exist_ok=True)
    slug = url.replace(BASE_URL, "").strip("/") or "home"
    safe_slug = slug.replace("/", "_")
    filename = os.path.join(output_dir, f"{safe_slug}.json")

    # Checkpoint check
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    should_close = False
    if client is None:
        client = httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=15.0, follow_redirects=True)
        should_close = True

    try:
        response = await client.get(url)
        if response.status_code == 200:
            extracted = extract_page_content(response.text, url)
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(extracted, f, indent=2, ensure_ascii=False)
            return extracted
        elif response.status_code == 404:
            logger.info(f"Page 404 not found: {url}")
            return None
        else:
            logger.warning(f"HTTP {response.status_code} fetching {url}")
            return None
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None
    finally:
        if should_close:
            await client.aclose()


class ContentCrawler:
    """Crawler for sitemap-discovered content pages and calculator tools."""

    def __init__(
        self,
        concurrency: int = 5,
        pages_dir: str = "celtestpip/data/raw/pages",
        tools_dir: str = "celtestpip/data/raw/tools",
    ):
        self.concurrency = concurrency
        self.pages_dir = pages_dir
        self.tools_dir = tools_dir

    async def crawl_sitemap(
        self, sitemap_url: str = f"{BASE_URL}/sitemap.xml"
    ) -> List[Dict[str, Any]]:
        sem = asyncio.Semaphore(self.concurrency)
        results: List[Dict[str, Any]] = []

        async with httpx.AsyncClient(headers=DEFAULT_HEADERS, timeout=20.0, follow_redirects=True) as client:
            resp = await client.get(sitemap_url)
            if resp.status_code != 200:
                logger.error(f"Failed to fetch sitemap: {resp.status_code}")
                return results

            urls = parse_sitemap_urls(resp.text)
            tasks = []

            for url in urls:
                target_dir = self.tools_dir if "/tools/" in url else self.pages_dir

                async def sem_task(target_url=url, out_dir=target_dir):
                    async with sem:
                        res = await crawl_page(client, target_url, output_dir=out_dir)
                        await asyncio.sleep(0.05)
                        return res

                tasks.append(sem_task())

            raw_results = await asyncio.gather(*tasks, return_exceptions=True)
            for r in raw_results:
                if isinstance(r, dict):
                    results.append(r)

        return results


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    crawler = ContentCrawler()
    asyncio.run(crawler.crawl_sitemap())
