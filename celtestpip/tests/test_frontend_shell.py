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

def test_header_navigation_has_calculator_and_pricing(client):
    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.text
    assert "/calculator" in html
    assert "Score Calculator" in html
    assert "/exams" in html
    assert "Pricing" in html

    calc_resp = client.get("/calculator")
    assert calc_resp.status_code == 200
