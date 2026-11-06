import os
import json
import asyncio
import logging
from typing import Optional, Dict, Any, List
import httpx
from celtestpip.crawler.rsc_parser import parse_exam_rsc

logger = logging.getLogger(__name__)

BASE_URL = "https://www.celtestpip.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "RSC": "1",
    "Accept": "*/*",
}


async def crawl_single_part(
    client: Optional[httpx.AsyncClient],
    exam_id: str,
    part_number: int,
    output_dir: str = "celtestpip/data/raw/exams"
) -> Optional[Dict[str, Any]]:
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{exam_id}_part{part_number}.json")

    # Checkpoint check
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    url = f"{BASE_URL}/exams/{exam_id}/part{part_number}"
    should_close = False
    if client is None:
        client = httpx.AsyncClient(headers=HEADERS, timeout=15.0, follow_redirects=True, verify=False)
        should_close = True

    try:
        response = await client.get(url)
        if response.status_code == 200:
            parsed = parse_exam_rsc(response.text)
            if parsed:
                parsed["exam_id"] = exam_id
                parsed["part_number"] = part_number
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(parsed, f, indent=2, ensure_ascii=False)
                return parsed
        elif response.status_code == 404:
            logger.info(f"Part {part_number} does not exist for {exam_id}")
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


class ExamCrawler:
    def __init__(self, concurrency: int = 5, output_dir: str = "celtestpip/data/raw/exams"):
        self.concurrency = concurrency
        self.output_dir = output_dir

    async def crawl_all(self, start_exam: int = 1, end_exam: int = 60) -> List[Dict[str, Any]]:
        sem = asyncio.Semaphore(self.concurrency)
        results = []

        async with httpx.AsyncClient(headers=HEADERS, timeout=20.0, follow_redirects=True, verify=False) as client:
            tasks = []
            for exam_num in range(start_exam, end_exam + 1):
                exam_id = f"exam{exam_num}"
                for part_num in range(1, 21):
                    async def sem_task(e_id=exam_id, p_num=part_num):
                        async with sem:
                            res = await crawl_single_part(client, e_id, p_num, self.output_dir)
                            await asyncio.sleep(0.1)  # courteous delay
                            return res
                    tasks.append(sem_task())

            raw_results = await asyncio.gather(*tasks, return_exceptions=True)
            for r in raw_results:
                if isinstance(r, dict):
                    results.append(r)
        return results


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    crawler = ExamCrawler()
    asyncio.run(crawler.crawl_all())
