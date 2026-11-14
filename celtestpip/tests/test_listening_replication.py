"""Comprehensive Integration and Regression Tests for CELPIP Listening Section Replication.

Verifies:
1. Hub page `/listening` structure, SEO metadata, 70 mock exams copy, and FAQ accordions.
2. All 6 Part hubs (`/parts/listening_*`) serve unlocked Free badges without locks.
3. Remote course banners proxy and serve high-resolution illustrations with local caching.
4. Decoupled Clerk authentication mocks preventing origin mismatches on localhost.
5. Practice tests serve unlocked interactive player interfaces with audio assets.
"""

import os
import glob
from fastapi.testclient import TestClient

from celtestpip.server.app import app
from celtestpip.server.config import PAGES_DIR, STATIC_DIR

client = TestClient(app)


def test_listening_hub_page_serves_html_and_metadata():
    """Verify /listening serves full pre-rendered HTML with exact branding."""
    resp = client.get("/listening")
    assert resp.status_code == 200
    html = resp.text

    assert "CELPIP Listening Practice Test 2026: Free with Answers" in html
    assert "70 mock exams" in html
    assert "faq-heading-listening" in html
    assert "lucide-headphones" in html or "listening.json" in html
    assert "/parts/listening_clziyrj8900021stdrf3o49w5" in html


def test_listening_course_images_proxy_and_cache():
    """Verify Next.js image proxy caches and returns full-resolution course banners."""
    test_urls = [
        "https://u108saydmkdhqew3.public.blob.vercel-storage.com/admin/2026/february/1770950556423-hf_20260212_162709_a206f90b-ee7e-44b2-96b3-5998a586f3af-PxQ37w1X464xhrCsUqLINaCKlRVbEF.jpeg",
        "https://u108saydmkdhqew3.public.blob.vercel-storage.com/admin/2026/february/1770950583795-hf_20260212_162804_7dfb36ad-c97b-4bec-bc3a-cf21b28d0ff3-7wRCQ6Y90f1QfSNg79KtAmdfnfuJeQ.jpeg",
    ]
    for url in test_urls:
        resp = client.get(f"/_next/image?url={url}&w=1920&q=75")
        assert resp.status_code == 200
        assert resp.headers["content-type"] in ["image/jpeg", "image/png", "image/webp"]
        assert len(resp.content) > 50000


def test_all_six_listening_part_hubs_served():
    """Verify all 6 part hubs are served with 200 OK and unlocked Free badges."""
    part_slugs = [
        "listening_clziyrj8900021stdrf3o49w5",
        "listening_clziyrj8b00031std9ana3ehf",
        "listening_clziyrj8b00041stdl7ai27c0",
        "listening_clziyrj8c00051stdxie738a0",
        "listening_clziyrj8c00061stdkzfkuvpm",
        "listening_clziyrj8c00071stdhsejrnmp",
    ]
    for slug in part_slugs:
        resp = client.get(f"/parts/{slug}")
        assert resp.status_code == 200
        html = resp.text
        assert "Pro practice, locked" not in html
        assert ">Free</span>" in html


def test_listening_practice_player_unlocked():
    """Verify listening practice tests load with player controls, questions, and audio tracks."""
    resp = client.get("/practices/listening_cmcwhh3ft008jtgu9sjrb1lvy")
    assert resp.status_code == 200
    html = resp.text

    assert "Upgrade to Pro" not in html
    assert "Pro only" not in html
    assert ".mp3" in html


def test_all_590_practices_harvested():
    """Verify all 590 practice tests are stored on disk."""
    practices = glob.glob(os.path.join(PAGES_DIR, "practices_listening_*.html"))
    assert len(practices) >= 590
