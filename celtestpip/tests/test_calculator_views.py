import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app
from celtestpip.server.scoring import raw_score_to_clb

client = TestClient(app)

def test_calculator_page_serves_html():
    response = client.get("/tools/clb-calculator")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    content = response.text
    assert "<title>CELPIP to CLB Score Calculator</title>" in content
    assert "CELPIP Raw Score to CLB Converter" in content
    assert 'id="skillSelect"' in content
    assert 'id="rawScore"' in content
    assert 'id="calcBtn"' in content
    assert 'id="clbResult"' in content
    assert '<script src="/static/js/calculator.js"></script>' in content
    assert '<link rel="stylesheet" href="/static/css/style.css">' in content

def test_calculator_js_accessible():
    response = client.get("/static/js/calculator.js")
    assert response.status_code == 200
    content = response.text
    assert "function calculateCLB" in content
    assert "skillSelect" in content
    assert "rawScore" in content
    assert "calcBtn" in content
    assert "clbResult" in content
    assert "LISTENING" in content
