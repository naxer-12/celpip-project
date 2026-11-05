import argparse
import asyncio
import glob
import json
import os
import sys

from celtestpip.crawler.crawl_exams import ExamCrawler
from celtestpip.crawler.crawl_content import parse_sitemap_urls
from celtestpip.crawler.download_media import scan_media_urls, download_all_media
import httpx


async def run_pipeline(
    crawl_exams_flag: bool,
    crawl_content_flag: bool,
    download_media_flag: bool,
    limit_exams: int = 60,
    pages_dir: str = "celtestpip/data/raw/pages",
    exams_dir: str = "celtestpip/data/raw/exams",
    media_dir: str = "celtestpip/data/media",
):
    print("=" * 60)
    print("CELTESTPIP CRAWLER PIPELINE")
    print("=" * 60)

    # 1. Crawl Exams
    if crawl_exams_flag:
        print(f"\n[1/3] Crawling exams (exam1 to exam{limit_exams})...")
        crawler = ExamCrawler(concurrency=6, output_dir=exams_dir)
        results = await crawler.crawl_all(start_exam=1, end_exam=limit_exams)
        print(f"-> Successfully extracted {len(results)} exam parts.")

    # 2. Crawl Content
    if crawl_content_flag:
        print("\n[2/3] Fetching sitemap and content pages...")
        os.makedirs(pages_dir, exist_ok=True)
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get("https://www.celtestpip.com/sitemap.xml")
            if resp.status_code == 200:
                urls = parse_sitemap_urls(resp.text)
                print(f"-> Discovered {len(urls)} URLs from sitemap.")
                with open(os.path.join(pages_dir, "sitemap_urls.json"), "w") as f:
                    json.dump(urls, f, indent=2)

    # 3. Download Media
    if download_media_flag:
        print("\n[3/3] Scanning and downloading media assets...")
        exam_files = glob.glob(os.path.join(exams_dir, "*.json"))
        parts = []
        for ef in exam_files:
            try:
                with open(ef, "r", encoding="utf-8") as f:
                    parts.append(json.load(f))
            except Exception:
                pass
        audio_urls, image_urls = scan_media_urls(parts)
        print(f"-> Found {len(audio_urls)} audio tracks and {len(image_urls)} images.")
        media_map = await download_all_media(audio_urls, image_urls, base_dir=media_dir)
        print(f"-> Media mapping saved with {len(media_map)} assets.")

    print("\nPipeline execution completed successfully.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CELTESTPIP Master Crawler")
    parser.add_argument("--exams", action="store_true", help="Crawl exams")
    parser.add_argument("--content", action="store_true", help="Crawl sitemap pages")
    parser.add_argument("--media", action="store_true", help="Download media assets")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    parser.add_argument("--limit", type=int, default=60, help="Limit number of exams (default: 60)")
    return parser


def main(args=None):
    parser = build_parser()
    parsed_args = parser.parse_args(args)

    if not any([parsed_args.exams, parsed_args.content, parsed_args.media, parsed_args.all]):
        parsed_args.all = True

    asyncio.run(
        run_pipeline(
            crawl_exams_flag=parsed_args.all or parsed_args.exams,
            crawl_content_flag=parsed_args.all or parsed_args.content,
            download_media_flag=parsed_args.all or parsed_args.media,
            limit_exams=parsed_args.limit,
        )
    )


if __name__ == "__main__":
    main()
