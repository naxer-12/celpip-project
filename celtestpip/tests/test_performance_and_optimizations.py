import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_gzip_compression_enabled(client):
    headers = {"Accept-Encoding": "gzip"}
    resp = client.get("/exams", headers=headers)
    assert resp.status_code == 200
    assert resp.headers.get("Content-Encoding") == "gzip"

def test_static_immutable_cache_headers(client):
    resp = client.get("/_next/static/immutable/chunks/1hqel2llswsmf.js")
    assert resp.status_code == 200
    assert "public" in resp.headers.get("Cache-Control", "")
    assert "immutable" in resp.headers.get("Cache-Control", "")

def test_page_cache_headers(client):
    resp = client.get("/exams")
    assert resp.status_code == 200
    assert "no-cache" in resp.headers.get("Cache-Control", "")

def test_clerk_local_mock_endpoints(client):
    resp = client.get("/v1/client")
    assert resp.status_code == 200
    data = resp.json()
    assert data["response"]["status"] == "ok"

    resp_env = client.get("/v1/environment")
    assert resp_env.status_code == 200
    assert resp_env.json()["authConfig"]["singleSessionMode"] is True

def test_manifest_and_animation_endpoints(client):
    resp_mf = client.get("/manifest.webmanifest")
    assert resp_mf.status_code == 200
    assert "application/manifest+json" in resp_mf.headers.get("Content-Type", "")

    resp_anim = client.get("/animation/book_ai.json")
    assert resp_anim.status_code == 200
    assert "application/json" in resp_anim.headers.get("Content-Type", "")

def test_in_memory_page_cache_speed(client):
    # First fetch warms cache
    resp1 = client.get("/practices/listening_cmn2ldtkn008b80un8zyrvxr9")
    assert resp1.status_code == 200
    # Second fetch comes directly from RAM
    resp2 = client.get("/practices/listening_cmn2ldtkn008b80un8zyrvxr9")
    assert resp2.status_code == 200
    assert resp2.text == resp1.text
