import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_index_page_returns_html_and_branding(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    content = response.text
    assert "CELTESTPIP" in content
    assert '<link rel="stylesheet" href="/static/css/style.css">' in content
    assert '<script src="/static/js/app.js"></script>' in content
    assert 'id="examsContainer"' in content
    assert "Listening" in content
    assert "Reading" in content
    assert "Writing" in content
    assert "Speaking" in content

def test_static_css_served(client):
    response = client.get("/static/css/style.css")
    assert response.status_code == 200
    assert "--bg-main: #f1f2ee" in response.text
    assert ".exams-grid" in response.text
    assert ".exam-badge" in response.text

def test_static_js_served(client):
    response = client.get("/static/js/app.js")
    assert response.status_code == 200
    assert "examsContainer" in response.text
    assert "/api/exams" in response.text
    assert "DOMContentLoaded" in response.text

def test_header_navigation_has_single_user_practice_links(client):
    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.text
    assert "/calculator" in html
    assert "Score Calculator" in html
    assert "/exams" in html
    assert "/listening" in html
    assert "/reading" in html
    assert "/writing" in html
    assert "/speaking" in html
    assert "/words" in html
    assert "Single-User Practice Mode" in html
    assert "single-user-nav.js" in html
    assert "Login / Sign up" not in html

    calc_resp = client.get("/calculator")
    assert calc_resp.status_code == 200
    assert "single-user-nav.js" in calc_resp.text

def test_all_core_pages_have_unified_single_user_nav(client):
    for path in ["/listening", "/reading", "/writing", "/speaking", "/courses", "/words", "/exams", "/calculator"]:
        resp = client.get(path)
        assert resp.status_code == 200, f"{path} failed"
        assert "single-user-nav.js" in resp.text, f"{path} missing single-user-nav.js"
        assert "single-user-nav-prehide" in resp.text, f"{path} missing prehide style"
