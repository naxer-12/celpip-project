import os
import json
import pytest
import httpx
from celtestpip.crawler.download_media import (
    get_safe_filename,
    scan_media_urls,
    download_file,
    download_all_media,
    load_all_exam_parts,
)


def test_safe_filename():
    url = "https://blob.vercel.com/practices/cm3/section1-SIGXC.mp3"
    filename = get_safe_filename(url)
    assert filename.endswith(".mp3")
    assert "section1" in filename or len(filename) > 8


def test_safe_filename_query_and_fallback():
    url_with_query = "https://blob.vercel.com/path/test-audio.mp3?token=12345"
    fn1 = get_safe_filename(url_with_query)
    assert fn1.endswith(".mp3")
    assert "test-audio" in fn1

    url_no_ext_audio = "https://blob.vercel.com/audio/sample_stream"
    fn2 = get_safe_filename(url_no_ext_audio)
    assert fn2.endswith(".mp3")

    url_no_ext_image = "https://blob.vercel.com/photo/graphic"
    fn3 = get_safe_filename(url_no_ext_image)
    assert fn3.endswith(".jpg")


def test_scan_media_urls():
    sample_part = {
        "audio_urls": ["https://blob.vercel.com/audio.mp3"],
        "image_url": "https://blob.vercel.com/image.jpg",
        "questions": [{"audio_url": "https://blob.vercel.com/q1.mp3"}],
    }
    audio_urls, image_urls = scan_media_urls([sample_part])
    assert len(audio_urls) == 2
    assert len(image_urls) == 1
    assert "https://blob.vercel.com/audio.mp3" in audio_urls
    assert "https://blob.vercel.com/q1.mp3" in audio_urls
    assert "https://blob.vercel.com/image.jpg" in image_urls


def test_scan_media_urls_empty_and_invalid():
    sample_parts = [
        {},
        {"audio_urls": [None, "", "not-a-url"]},
        {"image_url": None},
        {"questions": [{"audio_url": ""}, {"audio_url": None}]},
    ]
    audio_urls, image_urls = scan_media_urls(sample_parts)
    assert len(audio_urls) == 0
    assert len(image_urls) == 0


@pytest.mark.asyncio
async def test_download_file(tmp_path):
    dest_path = str(tmp_path / "test.mp3")

    def mock_handler(request: httpx.Request) -> httpx.Response:
        if request.url == "https://blob.vercel.com/test.mp3":
            return httpx.Response(200, content=b"fake-mp3-bytes")
        return httpx.Response(404)

    transport = httpx.MockTransport(mock_handler)
    async with httpx.AsyncClient(transport=transport) as client:
        # 1. Download success
        res = await download_file(client, "https://blob.vercel.com/test.mp3", dest_path)
        assert res is True
        assert os.path.exists(dest_path)
        with open(dest_path, "rb") as f:
            assert f.read() == b"fake-mp3-bytes"

        # 2. Checkpoint check: if file already exists with size > 0, returns True without re-fetching
        res_cached = await download_file(client, "https://blob.vercel.com/test.mp3", dest_path)
        assert res_cached is True

        # 3. 404 failure
        bad_dest = str(tmp_path / "notfound.mp3")
        res_fail = await download_file(client, "https://blob.vercel.com/missing.mp3", bad_dest)
        assert res_fail is False
        assert not os.path.exists(bad_dest)


@pytest.mark.asyncio
async def test_download_all_media(tmp_path, monkeypatch):
    base_dir = str(tmp_path / "media")
    audio_urls = {"https://blob.vercel.com/section1.mp3"}
    image_urls = {"https://blob.vercel.com/diagram.png"}

    def mock_handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=b"media_content")

    transport = httpx.MockTransport(mock_handler)
    orig_client_init = httpx.AsyncClient.__init__

    def patched_init(self, *args, **kwargs):
        kwargs["transport"] = transport
        orig_client_init(self, *args, **kwargs)

    monkeypatch.setattr(httpx.AsyncClient, "__init__", patched_init)

    media_map = await download_all_media(audio_urls, image_urls, base_dir=base_dir, concurrency=2)

    assert "https://blob.vercel.com/section1.mp3" in media_map
    assert media_map["https://blob.vercel.com/section1.mp3"].startswith("/media/audio/")
    assert "https://blob.vercel.com/diagram.png" in media_map
    assert media_map["https://blob.vercel.com/diagram.png"].startswith("/media/images/")

    map_path = os.path.join(base_dir, "media_map.json")
    assert os.path.exists(map_path)
    with open(map_path, "r", encoding="utf-8") as f:
        loaded_map = json.load(f)
    assert loaded_map == media_map


def test_load_all_exam_parts(tmp_path):
    raw_dir = tmp_path / "raw_exams"
    raw_dir.mkdir()
    f1 = raw_dir / "exam1_part1.json"
    f1.write_text(json.dumps({"exam_id": "exam1", "part_number": 1}), encoding="utf-8")
    f2 = raw_dir / "exam1_part2.json"
    f2.write_text(json.dumps({"exam_id": "exam1", "part_number": 2}), encoding="utf-8")
    f3 = raw_dir / "ignore.txt"
    f3.write_text("random", encoding="utf-8")

    parts = load_all_exam_parts(str(raw_dir))
    assert len(parts) == 2
    assert {p["part_number"] for p in parts} == {1, 2}
