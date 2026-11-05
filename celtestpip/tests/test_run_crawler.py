import json
import os
import pytest
from unittest.mock import patch, AsyncMock, MagicMock
from celtestpip.crawler.run_crawler import build_parser, main, run_pipeline


def test_build_parser_defaults():
    parser = build_parser()
    args = parser.parse_args([])
    assert args.exams is False
    assert args.content is False
    assert args.media is False
    assert args.all is False
    assert args.limit == 60


def test_build_parser_explicit_flags():
    parser = build_parser()
    args = parser.parse_args(["--exams", "--limit", "25"])
    assert args.exams is True
    assert args.content is False
    assert args.media is False
    assert args.all is False
    assert args.limit == 25


def test_main_defaults_to_all():
    with patch("celtestpip.crawler.run_crawler.run_pipeline", new_callable=AsyncMock) as mock_pipeline:
        main([])
        mock_pipeline.assert_called_once_with(
            crawl_exams_flag=True,
            crawl_content_flag=True,
            download_media_flag=True,
            limit_exams=60,
        )


def test_main_calls_run_pipeline_with_flags():
    with patch("celtestpip.crawler.run_crawler.run_pipeline", new_callable=AsyncMock) as mock_pipeline:
        main(["--exams", "--limit", "15"])
        mock_pipeline.assert_called_once_with(
            crawl_exams_flag=True,
            crawl_content_flag=False,
            download_media_flag=False,
            limit_exams=15,
        )


def test_main_all_flag():
    with patch("celtestpip.crawler.run_crawler.run_pipeline", new_callable=AsyncMock) as mock_pipeline:
        main(["--all", "--limit", "30"])
        mock_pipeline.assert_called_once_with(
            crawl_exams_flag=True,
            crawl_content_flag=True,
            download_media_flag=True,
            limit_exams=30,
        )


def test_main_partial_flags_combination():
    with patch("celtestpip.crawler.run_crawler.run_pipeline", new_callable=AsyncMock) as mock_pipeline:
        main(["--content", "--media"])
        mock_pipeline.assert_called_once_with(
            crawl_exams_flag=False,
            crawl_content_flag=True,
            download_media_flag=True,
            limit_exams=60,
        )


@pytest.mark.asyncio
async def test_run_pipeline_exams_only(tmp_path):
    mock_crawler = MagicMock()
    mock_crawler.crawl_all = AsyncMock(return_value=[{"id": "exam1_part1"}])

    with patch("celtestpip.crawler.run_crawler.ExamCrawler", return_value=mock_crawler) as mock_cls:
        await run_pipeline(
            crawl_exams_flag=True,
            crawl_content_flag=False,
            download_media_flag=False,
            limit_exams=10,
            pages_dir=str(tmp_path / "pages"),
            exams_dir=str(tmp_path / "exams"),
            media_dir=str(tmp_path / "media"),
        )
        mock_cls.assert_called_once_with(concurrency=6, output_dir=str(tmp_path / "exams"))
        mock_crawler.crawl_all.assert_called_once_with(start_exam=1, end_exam=10)


@pytest.mark.asyncio
async def test_run_pipeline_content_only(tmp_path):
    pages_dir = tmp_path / "pages"
    sample_sitemap = """<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
      <url><loc>https://www.celtestpip.com/test-page</loc></url>
    </urlset>"""

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = sample_sitemap

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resp)
    mock_client.__aenter__.return_value = mock_client
    mock_client.__aexit__.return_value = None

    with patch("celtestpip.crawler.run_crawler.httpx.AsyncClient", return_value=mock_client):
        await run_pipeline(
            crawl_exams_flag=False,
            crawl_content_flag=True,
            download_media_flag=False,
            pages_dir=str(pages_dir),
            exams_dir=str(tmp_path / "exams"),
            media_dir=str(tmp_path / "media"),
        )

    sitemap_file = pages_dir / "sitemap_urls.json"
    assert sitemap_file.exists()
    with open(sitemap_file, "r") as f:
        data = json.load(f)
    assert data == ["https://www.celtestpip.com/test-page"]


@pytest.mark.asyncio
async def test_run_pipeline_content_non_200(tmp_path):
    pages_dir = tmp_path / "pages"

    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_resp.text = "Not Found"

    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resp)
    mock_client.__aenter__.return_value = mock_client
    mock_client.__aexit__.return_value = None

    with patch("celtestpip.crawler.run_crawler.httpx.AsyncClient", return_value=mock_client):
        await run_pipeline(
            crawl_exams_flag=False,
            crawl_content_flag=True,
            download_media_flag=False,
            pages_dir=str(pages_dir),
            exams_dir=str(tmp_path / "exams"),
            media_dir=str(tmp_path / "media"),
        )

    sitemap_file = pages_dir / "sitemap_urls.json"
    assert not sitemap_file.exists()


@pytest.mark.asyncio
async def test_run_pipeline_media_only(tmp_path):
    exams_dir = tmp_path / "exams"
    media_dir = tmp_path / "media"
    exams_dir.mkdir(parents=True)

    exam_file = exams_dir / "exam1_part1.json"
    exam_data = {
        "audio_urls": ["https://www.celtestpip.com/audio/sample.mp3"],
        "image_url": "https://www.celtestpip.com/images/sample.jpg",
        "questions": [],
    }
    exam_file.write_text(json.dumps(exam_data), encoding="utf-8")

    # Also add an invalid/corrupt json file to test error tolerance
    corrupt_file = exams_dir / "exam1_corrupt.json"
    corrupt_file.write_text("invalid json {", encoding="utf-8")

    with patch("celtestpip.crawler.run_crawler.download_all_media", new_callable=AsyncMock) as mock_download:
        mock_download.return_value = {"https://www.celtestpip.com/audio/sample.mp3": "/media/audio/sample.mp3"}

        await run_pipeline(
            crawl_exams_flag=False,
            crawl_content_flag=False,
            download_media_flag=True,
            pages_dir=str(tmp_path / "pages"),
            exams_dir=str(exams_dir),
            media_dir=str(media_dir),
        )

        mock_download.assert_called_once()
        audio_urls, image_urls = mock_download.call_args[0]
        assert "https://www.celtestpip.com/audio/sample.mp3" in audio_urls
        assert "https://www.celtestpip.com/images/sample.jpg" in image_urls


@pytest.mark.asyncio
async def test_run_pipeline_all_stages(tmp_path):
    exams_dir = tmp_path / "exams"
    pages_dir = tmp_path / "pages"
    media_dir = tmp_path / "media"
    exams_dir.mkdir(parents=True)

    mock_crawler = MagicMock()
    mock_crawler.crawl_all = AsyncMock(return_value=[{"exam_id": "exam1", "part_number": 1}])

    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = "<urlset><url><loc>https://www.celtestpip.com/p1</loc></url></urlset>"
    mock_client = AsyncMock()
    mock_client.get = AsyncMock(return_value=mock_resp)
    mock_client.__aenter__.return_value = mock_client
    mock_client.__aexit__.return_value = None

    with patch("celtestpip.crawler.run_crawler.ExamCrawler", return_value=mock_crawler), \
         patch("celtestpip.crawler.run_crawler.httpx.AsyncClient", return_value=mock_client), \
         patch("celtestpip.crawler.run_crawler.download_all_media", new_callable=AsyncMock) as mock_download:

        mock_download.return_value = {}

        await run_pipeline(
            crawl_exams_flag=True,
            crawl_content_flag=True,
            download_media_flag=True,
            limit_exams=2,
            pages_dir=str(pages_dir),
            exams_dir=str(exams_dir),
            media_dir=str(media_dir),
        )

        mock_crawler.crawl_all.assert_called_once_with(start_exam=1, end_exam=2)
        assert (pages_dir / "sitemap_urls.json").exists()
        mock_download.assert_called_once()
