import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app

client = TestClient(app)

def test_numeric_and_slug_exam_api():
    """Verify numeric ID /api/exams/1/part/1 resolves identically to /api/exams/exam1/part/1."""
    res_num = client.get("/api/exams/1/part/1")
    assert res_num.status_code == 200
    data_num = res_num.json()

    res_slug = client.get("/api/exams/exam1/part/1")
    assert res_slug.status_code == 200
    data_slug = res_slug.json()

    assert data_num["id"] == data_slug["id"]
    assert data_num["part_name"] == data_slug["part_name"]
    assert len(data_num["questions"]) == len(data_slug["questions"])

def test_exam_parts_list_api():
    """Verify /api/exams/{id}/parts returns all parts for an exam."""
    res = client.get("/api/exams/1/parts")
    assert res.status_code == 200
    parts = res.json()
    assert len(parts) >= 20
    assert parts[0]["part_number"] == 1
    assert parts[-1]["part_number"] == 20

def test_exam_routes_support_numeric_and_slug():
    """Verify HTML routes support numeric and slug format without 404."""
    for path in ["/exams/1", "/exams/exam1", "/exams/1/part/1", "/exams/exam1/part/7", "/exams/1/results"]:
        res = client.get(path)
        assert res.status_code == 200
        assert "text/html" in res.headers["content-type"]
        assert "<title>CELPIP Exam Simulator</title>" in res.text

def test_exams_catalog_has_catalog_script():
    """Verify /exams catalog page includes exams_catalog.js script."""
    res = client.get("/exams")
    assert res.status_code == 200
    assert "exams_catalog.js" in res.text

def test_exams_catalog_js_is_served():
    """Verify exams_catalog.js is properly served as javascript."""
    res = client.get("/static/js/exams_catalog.js")
    assert res.status_code == 200
    assert "exam-dropdown-menu" in res.text
    assert "Complete Test" in res.text

def test_platform_content_pages_replicated():
    """Verify platform pages are served without 404 Not Found."""
    pages = [
        "/listening",
        "/reading",
        "/writing",
        "/speaking",
        "/questions",
        "/courses",
        "/reviews",
        "/words",
        "/tools/crs-calculator"
    ]
    for p in pages:
        res = client.get(p)
        assert res.status_code == 200
        assert "text/html" in res.headers.get("content-type", "")
        assert len(res.text) > 1000
        assert "Not Found" not in res.text[:200]
