import pytest
import os
import json
from unittest.mock import AsyncMock, patch
from celtestpip.crawler.crawl_content import (
    parse_sitemap_urls,
    extract_page_content,
    crawl_page,
    ContentCrawler,
)

SAMPLE_SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://www.celtestpip.com</loc></url>
<url><loc>https://www.celtestpip.com/questions</loc></url>
<url><loc>https://www.celtestpip.com/tools/clb-calculator</loc></url>
</urlset>"""


def test_parse_sitemap():
    urls = parse_sitemap_urls(SAMPLE_SITEMAP)
    assert len(urls) == 3
    assert "https://www.celtestpip.com/questions" in urls
    assert "https://www.celtestpip.com/tools/clb-calculator" in urls


def test_extract_page_content():
    html = """<!DOCTYPE html>
<html>
<head>
    <title>CLB Score Calculator | Celtestpip</title>
    <meta name="description" content="Calculate your Canadian Language Benchmark score easily.">
</head>
<body>
    <header><nav>Nav links</nav></header>
    <main>
        <h1>CLB Calculator</h1>
        <p>Interactive tool to convert CELPIP scores to CLB levels.</p>
    </main>
    <footer>Footer notes</footer>
</body>
</html>"""
    url = "https://www.celtestpip.com/tools/clb-calculator"
    data = extract_page_content(html, url)

    assert data["slug"] == "tools/clb-calculator"
    assert data["url"] == url
    assert data["title"] == "CLB Score Calculator | Celtestpip"
    assert data["description"] == "Calculate your Canadian Language Benchmark score easily."
    assert "<h1>CLB Calculator</h1>" in data["content_html"]
    assert "<header>" not in data["content_html"]


def test_extract_page_content_fallbacks():
    html = "<html><body><p>Simple body with no tags</p></body></html>"
    url = "https://www.celtestpip.com"
    data = extract_page_content(html, url)

    assert data["slug"] == "home"
    assert data["url"] == url
    assert data["title"] == url
    assert data["description"] == ""
    assert data["content_html"] == html


@pytest.mark.asyncio
async def test_crawl_page(tmp_path):
    sample_html = """<html>
<head><title>Questions Bank</title><meta name="description" content="All questions"></head>
<main><p>Question list</p></main>
</html>"""
    url = "https://www.celtestpip.com/questions"
    output_dir = str(tmp_path / "pages")

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.text = sample_html
        mock_get.return_value = mock_resp

        result = await crawl_page(None, url, output_dir=output_dir)
        assert result is not None
        assert result["slug"] == "questions"
        assert result["title"] == "Questions Bank"
        assert result["description"] == "All questions"

        # Check saved checkpoint file
        saved_file = os.path.join(output_dir, "questions.json")
        assert os.path.exists(saved_file)
        with open(saved_file, "r", encoding="utf-8") as f:
            saved_data = json.load(f)
            assert saved_data["slug"] == "questions"


@pytest.mark.asyncio
async def test_crawl_page_checkpoint(tmp_path):
    output_dir = str(tmp_path / "pages")
    os.makedirs(output_dir, exist_ok=True)
    saved_file = os.path.join(output_dir, "questions.json")
    cached_data = {
        "slug": "questions",
        "url": "https://www.celtestpip.com/questions",
        "title": "Cached Title",
        "description": "Cached Desc",
        "content_html": "<main>cached</main>"
    }
    with open(saved_file, "w", encoding="utf-8") as f:
        json.dump(cached_data, f)

    with patch("httpx.AsyncClient.get") as mock_get:
        result = await crawl_page(None, "https://www.celtestpip.com/questions", output_dir=output_dir)
        assert result == cached_data
        mock_get.assert_not_called()


@pytest.mark.asyncio
async def test_crawl_page_http_error(tmp_path):
    output_dir = str(tmp_path / "pages")
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 404
        mock_get.return_value = mock_resp

        result = await crawl_page(None, "https://www.celtestpip.com/nonexistent", output_dir=output_dir)
        assert result is None


@pytest.mark.asyncio
async def test_content_crawler(tmp_path):
    pages_dir = str(tmp_path / "pages")
    tools_dir = str(tmp_path / "tools")

    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://www.celtestpip.com/about</loc></url>
<url><loc>https://www.celtestpip.com/tools/clb-calculator</loc></url>
</urlset>"""

    def mock_get_impl(url, *args, **kwargs):
        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        if "sitemap.xml" in url:
            mock_resp.text = sitemap_xml
        else:
            mock_resp.text = f"<html><head><title>{url}</title></head><main>Content for {url}</main></html>"
        return mock_resp

    with patch("httpx.AsyncClient.get", side_effect=mock_get_impl):
        crawler = ContentCrawler(concurrency=2, pages_dir=pages_dir, tools_dir=tools_dir)
        results = await crawler.crawl_sitemap("https://www.celtestpip.com/sitemap.xml")
        assert len(results) == 2
        slugs = [r["slug"] for r in results]
        assert "about" in slugs
        assert "tools/clb-calculator" in slugs

        # Verify tool saved in tools_dir and page saved in pages_dir
        assert os.path.exists(os.path.join(pages_dir, "about.json"))
        assert os.path.exists(os.path.join(tools_dir, "tools_clb-calculator.json"))
