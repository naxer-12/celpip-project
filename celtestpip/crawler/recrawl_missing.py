import os
import json
import asyncio
import re
import glob
import logging
import httpx
from celtestpip.crawler.rsc_parser import parse_exam_rsc

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = "https://www.celtestpip.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "RSC": "1",
    "Accept": "*/*",
}

async def fetch_and_update(client: httpx.AsyncClient, sem: asyncio.Semaphore, exam_id: str, part_num: int, output_dir: str):
    filename = os.path.join(output_dir, f"{exam_id}_part{part_num}.json")
    url = f"{BASE_URL}/exams/{exam_id}/part{part_num}"
    async with sem:
        try:
            resp = await client.get(url, headers=HEADERS)
            if resp.status_code == 200:
                parsed = parse_exam_rsc(resp.text)
                if parsed:
                    parsed["exam_id"] = exam_id
                    parsed["part_number"] = part_num
                    with open(filename, "w", encoding="utf-8") as f:
                        json.dump(parsed, f, indent=2, ensure_ascii=False)
                    return True
        except Exception as e:
            logger.warning(f"Error fetching {url}: {e}")
    return False

async def main():
    output_dir = "celtestpip/data/raw/exams"
    parts_to_update = []
    for fn in glob.glob(f"{output_dir}/*.json"):
        with open(fn) as f:
            d = json.load(f)
        inst = str(d.get("instructions") or "").strip()
        is_dollar_inst = bool(re.match(r"^\$[0-9a-fA-F]+$", inst))
        is_missing_transcripts = (d.get("skill") == "LISTENING" and len(d.get("transcripts") or []) < 2 and d.get("part_number") in [1, 2, 3, 5])
        if is_dollar_inst or is_missing_transcripts:
            parts_to_update.append((d["exam_id"], d["part_number"]))

    logger.info(f"Starting recrawl of {len(parts_to_update)} parts with concurrency 20...")
    sem = asyncio.Semaphore(20)
    limits = httpx.Limits(max_connections=30, max_keepalive_connections=20)
    async with httpx.AsyncClient(timeout=15.0, limits=limits, verify=False) as client:
        tasks = [
            fetch_and_update(client, sem, eid, pnum, output_dir)
            for eid, pnum in parts_to_update
        ]
        results = await asyncio.gather(*tasks)
    success = sum(1 for r in results if r)
    logger.info(f"Finished recrawl: {success}/{len(parts_to_update)} succeeded.")

if __name__ == "__main__":
    asyncio.run(main())
