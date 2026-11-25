"""Async atomic crawler for all missing practice pages, tools, and guides
from celtestpip.com, piping every page through paywall-stripping clean_html().
"""

import asyncio
import glob
import os
import re
import ssl
import urllib.request
from typing import List, Set, Tuple

import httpx

from celtestpip.scripts.unlock_all_pro_content import clean_html
from celtestpip.scripts.rewrite_all_site_links import rewrite_celtestpip_links

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
ORIGIN = "https://www.celtestpip.com"


def discover_missing_routes() -> List[Tuple[str, str]]:
    """Collect all missing practice, tool, and learn routes."""
    local_pages: Set[str] = set(
        os.path.basename(p)[:-5] for p in glob.glob(os.path.join(PAGES_DIR, "*.html"))
    )
    targets: Set[str] = set()

    # 1. Discover all practice slugs from parts_*.html
    for pf in glob.glob(os.path.join(PAGES_DIR, "parts_*.html")):
        with open(pf, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()
        for m in re.findall(r'/practices/((?:listening|reading|writing|speaking)_[a-z0-9]+)', content):
            targets.add(f"practices/{m}")

    # 2. Discover missing English routes from sitemap.xml
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        req = urllib.request.Request(f"{ORIGIN}/sitemap.xml", headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            xml = r.read().decode("utf-8", errors="replace")
        for u in re.findall(r"<loc>(.*?)</loc>", xml):
            path = u.replace(ORIGIN, "").strip("/")
            if not path:
                continue
            if re.match(r"^(zh|fr|es|pt|ko|ja|vi|hi|ar|ru|fa)(/|$)", path):
                continue
            if path in ("exams", "home", "auth/sign-in", "auth/sign-up"):
                continue
            targets.add(path)
    except Exception as e:
        print(f"Sitemap fetch warning: {e}")

    missing: List[Tuple[str, str]] = []
    for path in sorted(targets):
        safe_slug = path.replace("/", "_")
        out_path = os.path.join(PAGES_DIR, f"{safe_slug}.html")
        if safe_slug not in local_pages or not os.path.exists(out_path) or os.path.getsize(out_path) == 0:
            missing.append((path, out_path))
    return missing


async def fetch_and_save(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    path: str,
    out_path: str,
    stats: dict,
) -> None:
    url = f"{ORIGIN}/{path}"
    async with sem:
        for attempt in range(2):
            try:
                resp = await client.get(url, timeout=20.0, follow_redirects=True)
                if resp.status_code == 200 and len(resp.text) > 1000:
                    cleaned = clean_html(resp.text)
                    cleaned = rewrite_celtestpip_links(cleaned)
                    with open(out_path, "w", encoding="utf-8") as f:
                        f.write(cleaned)
                    stats["ok"] += 1
                    if stats["ok"] % 100 == 0:
                        print(f"  Crawled & unlocked {stats['ok']}/{stats['total']} pages (failed={stats['fail']})")
                    return
            except Exception:
                await asyncio.sleep(0.4 * (attempt + 1))
        stats["fail"] += 1


async def crawl_all() -> None:
    missing = discover_missing_routes()
    print(f"Discovered {len(missing)} missing pages to crawl & unlock.")
    if not missing:
        return

    stats = {"ok": 0, "fail": 0, "total": len(missing)}
    sem = asyncio.Semaphore(24)
    limits = httpx.Limits(max_connections=30, max_keepalive_connections=20)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

    async with httpx.AsyncClient(limits=limits, headers=headers, verify=False) as client:
        tasks = [fetch_and_save(client, sem, path, out_path, stats) for path, out_path in missing]
        await asyncio.gather(*tasks)

    print(f"Crawl complete: ok={stats['ok']}, fail={stats['fail']}, total={stats['total']}")


def main() -> None:
    asyncio.run(crawl_all())


if __name__ == "__main__":
    main()
