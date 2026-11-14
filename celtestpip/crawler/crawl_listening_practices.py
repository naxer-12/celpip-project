"""Concurrent Crawler for all 590 CELPIP Listening Practices.

Harvests all 590 practice tests from celtestpip.com across all 6 listening parts,
unlocks Pro content and paywalls via clean_html(), and caches them locally
in celtestpip/data/pages/practices_listening_*.html for 100% offline parity.
"""

import os
import re
import ssl
import glob
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Set

from celtestpip.scripts.unlock_all_pro_content import clean_html

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")


def get_all_listening_practice_ids() -> List[str]:
    """Scan all 6 listening part pages and extract unique practice IDs."""
    practice_ids: Set[str] = set()
    part_files = glob.glob(os.path.join(PAGES_DIR, "parts_listening_*.html"))

    for pf in part_files:
        try:
            with open(pf, "r", encoding="utf-8") as f:
                content = f.read()
            matches = re.findall(r"/practices/(listening_[a-zA-Z0-9_-]+)", content)
            practice_ids.update(matches)
        except Exception as e:
            print(f"Error reading {pf}: {e}")

    return sorted(list(practice_ids))


def fetch_and_save_practice(practice_id: str, max_retries: int = 3) -> bool:
    """Fetch a single practice test, unlock it, and write to disk."""
    target_path = os.path.join(PAGES_DIR, f"practices_{practice_id}.html")
    if os.path.exists(target_path) and os.path.getsize(target_path) > 50000:
        return True

    url = f"https://www.celtestpip.com/practices/{practice_id}"
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=12) as resp:
                if resp.status == 200:
                    raw_html = resp.read().decode("utf-8", errors="replace")
                    cleaned = clean_html(raw_html)
                    with open(target_path, "w", encoding="utf-8") as f:
                        f.write(cleaned)
                    return True
        except Exception as e:
            if attempt == max_retries - 1:
                print(f"[FAIL] {practice_id}: {e}")
            time.sleep(0.5 * (attempt + 1))

    return False


def crawl_all(concurrency: int = 16) -> None:
    """Run concurrent crawling of all missing practice tests."""
    practice_ids = get_all_listening_practice_ids()
    print(f"Total listening practices found in part hubs: {len(practice_ids)}")

    missing = [
        pid for pid in practice_ids
        if not os.path.exists(os.path.join(PAGES_DIR, f"practices_{pid}.html"))
        or os.path.getsize(os.path.join(PAGES_DIR, f"practices_{pid}.html")) < 50000
    ]

    print(f"Already cached: {len(practice_ids) - len(missing)}, Missing to crawl: {len(missing)}")
    if not missing:
        print("All practices already harvested and unlocked!")
        return

    start_time = time.time()
    completed = 0
    failed = 0

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        future_map = {executor.submit(fetch_and_save_practice, pid): pid for pid in missing}

        for future in as_completed(future_map):
            pid = future_map[future]
            try:
                success = future.result()
                if success:
                    completed += 1
                else:
                    failed += 1
            except Exception as e:
                failed += 1
                print(f"Unhandled exception for {pid}: {e}")

            total_done = completed + failed
            if total_done % 25 == 0 or total_done == len(missing):
                elapsed = time.time() - start_time
                rate = total_done / elapsed if elapsed > 0 else 0
                remaining = (len(missing) - total_done) / rate if rate > 0 else 0
                print(
                    f"Progress: [{total_done}/{len(missing)}] "
                    f"Completed: {completed}, Failed: {failed} "
                    f"({rate:.1f} tests/sec, ~{remaining:.0f}s left)"
                )

    print(
        f"\nCrawl complete in {time.time() - start_time:.1f}s. "
        f"Total harvested: {completed}, Failed: {failed}."
    )


if __name__ == "__main__":
    crawl_all()
