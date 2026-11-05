import pytest
import os
import json
from unittest.mock import AsyncMock, patch
from celtestpip.crawler.crawl_exams import crawl_single_part, ExamCrawler


@pytest.mark.asyncio
async def test_crawl_single_part(tmp_path):
    mock_rsc = '7:[{"practice":{"id":"p1","name":"Test","text":"Inst","audio":"","part":{"type":"READING","name":"Reading"}},"examId":"exam1","partNumber":1}]'

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.text = mock_rsc
        mock_get.return_value = mock_resp

        output_dir = str(tmp_path)
        result = await crawl_single_part(None, "exam1", 1, output_dir=output_dir)

        assert result is not None
        assert result["exam_id"] == "exam1"
        assert result["part_number"] == 1

        # Verify file saved
        file_path = os.path.join(output_dir, "exam1_part1.json")
        assert os.path.isfile(file_path)
        with open(file_path) as f:
            saved = json.load(f)
            assert saved["exam_id"] == "exam1"


@pytest.mark.asyncio
async def test_crawl_single_part_checkpoint(tmp_path):
    output_dir = str(tmp_path)
    file_path = os.path.join(output_dir, "exam2_part3.json")
    checkpoint_data = {
        "exam_id": "exam2",
        "part_number": 3,
        "skill": "LISTENING",
        "questions": []
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(checkpoint_data, f)

    # With checkpoint existing, httpx.AsyncClient.get should never be called
    with patch("httpx.AsyncClient.get") as mock_get:
        result = await crawl_single_part(None, "exam2", 3, output_dir=output_dir)
        assert result == checkpoint_data
        mock_get.assert_not_called()


@pytest.mark.asyncio
async def test_crawl_single_part_404(tmp_path):
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 404
        mock_get.return_value = mock_resp

        output_dir = str(tmp_path)
        result = await crawl_single_part(None, "exam1", 99, output_dir=output_dir)
        assert result is None
        assert not os.path.exists(os.path.join(output_dir, "exam1_99.json"))


@pytest.mark.asyncio
async def test_crawl_single_part_network_error(tmp_path):
    with patch("httpx.AsyncClient.get", side_effect=Exception("Connection reset")):
        output_dir = str(tmp_path)
        result = await crawl_single_part(None, "exam1", 1, output_dir=output_dir)
        assert result is None


@pytest.mark.asyncio
async def test_exam_crawler_crawl_all(tmp_path):
    output_dir = str(tmp_path)
    mock_rsc = '7:[{"practice":{"id":"p1","name":"Test","text":"Inst","audio":"","part":{"type":"READING","name":"Reading"}},"examId":"exam1","partNumber":1}]'

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.text = mock_rsc
        mock_get.return_value = mock_resp

        crawler = ExamCrawler(concurrency=2, output_dir=output_dir)
        # Test crawl_all over a small slice (1 exam, 2 parts for instance, but crawl_all iterates 1..20 parts per exam)
        # So for 1 exam it will make 20 requests
        results = await crawler.crawl_all(start_exam=1, end_exam=1)
        assert len(results) == 20
        assert mock_get.call_count == 20
