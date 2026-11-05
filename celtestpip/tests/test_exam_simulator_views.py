import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app

client = TestClient(app)

def test_exam_part_page_serves_exam_html():
    response = client.get("/exams/exam1/part/1")
    assert response.status_code == 200
    assert "text/html" in response.headers.get("content-type", "")
    content = response.text
    assert "<title>CELPIP Exam Simulator</title>" in content
    assert 'id="examTitle"' in content
    assert 'id="partsList"' in content
    assert 'id="partHeading"' in content
    assert 'id="timer"' in content
    assert 'id="audioSection"' in content
    assert 'id="imageSection"' in content
    assert 'id="questionsContainer"' in content
    assert 'id="submitBtn"' in content
    assert 'id="toggleTranscriptBtn"' in content
    assert 'id="transcriptBox"' in content
    assert '<script src="/static/js/exam_runner.js"></script>' in content

def test_exam_runner_js_accessible():
    response = client.get("/static/js/exam_runner.js")
    assert response.status_code == 200
    content = response.text
    assert "/api/exams/" in content
    assert "questionsContainer" in content
    assert "submitBtn" in content
    assert "toggleTranscriptBtn" in content
    assert "/api/attempts" in content
