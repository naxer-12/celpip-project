"""Tests for Course Section Completion Progress and Link Internalization."""

import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app
from celtestpip.server.database import save_course_progress, get_completed_course_sections


@pytest.fixture
def client():
    return TestClient(app)


def test_course_section_progress_api(client):
    section_id = "cmfppsiro007xx3bn283u8rx6"

    # 1. Mark as complete
    resp = client.post(
        f"/api/courses/sections/{section_id}/progress",
        json={"sectionId": section_id, "completed": True},
    )
    assert resp.status_code == 200
    assert resp.json() == {"success": True, "sectionId": section_id, "completed": True}

    # 2. Query section progress
    resp_get = client.get(f"/api/courses/sections/{section_id}/progress")
    assert resp_get.status_code == 200
    assert resp_get.json() == {"sectionId": section_id, "completed": True}

    # 3. Query all progress
    resp_all = client.get("/api/courses/progress")
    assert resp_all.status_code == 200
    assert section_id in resp_all.json()["completedSections"]

    # 4. Toggle back to incomplete
    resp_undo = client.post(
        f"/api/courses/sections/{section_id}/progress",
        json={"sectionId": section_id, "completed": False},
    )
    assert resp_undo.status_code == 200
    assert resp_undo.json() == {"success": True, "sectionId": section_id, "completed": False}

    resp_get2 = client.get(f"/api/courses/sections/{section_id}/progress")
    assert resp_get2.status_code == 200
    assert resp_get2.json() == {"sectionId": section_id, "completed": False}


def test_course_page_dynamically_reflects_completion(client):
    section_id = "cmfppsiro007xx3bn283u8rx6"

    # Mark as completed
    client.post(
        f"/api/courses/sections/{section_id}/progress",
        json={"sectionId": section_id, "completed": True},
    )

    # Fetch lesson page
    resp = client.get("/courses/celpip-listening/test-mechanics-interface-confidence")
    assert resp.status_code == 200
    assert '\"isCompleted\":true' in resp.text or '\\\"isCompleted\\\":true' in resp.text

    # Revert to incomplete
    client.post(
        f"/api/courses/sections/{section_id}/progress",
        json={"sectionId": section_id, "completed": False},
    )


def test_all_course_links_are_internalized(client):
    resp = client.get("/courses/celpip-listening/orientation-success-targets")
    assert resp.status_code == 200

    html = resp.text
    # No external celtestpip.com navigation links
    assert 'href="https://www.celtestpip.com/listening"' not in html
    assert 'href="https://www.celtestpip.com/exams"' not in html
    assert 'href="https://www.celtestpip.com/courses/' not in html

    # Clean internal relative links
    assert 'href="/listening"' in html
    assert 'href="/exams"' in html
    assert 'href="/courses/celpip-listening/test-mechanics-interface-confidence"' in html
    assert 'href="/courses/celpip-listening/test-day-playbook-listening-exam-success"' in html


def test_test_mechanics_page_links_are_internalized(client):
    resp = client.get("/courses/celpip-listening/test-mechanics-interface-confidence")
    assert resp.status_code == 200

    html = resp.text
    assert 'href="https://www.celtestpip.com/' not in html
    assert 'href="/courses"' in html
    assert 'href="/courses/celpip-listening"' in html
