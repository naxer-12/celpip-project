import json
import os
import pytest
from fastapi.testclient import TestClient

from celtestpip.build_db import build_database
from celtestpip.server.app import DB_PATH, app
from celtestpip.server.database import get_db_connection, init_db, insert_exam_part

client = TestClient(app)


def test_full_application_flow():
    """Validates the end-to-end user navigation flow:

    1. Access index page and static assets (CSS, JS).
    2. Access CLB calculator page.
    3. Access exam simulator page.
    4. Fetch list of exams via API.
    5. Fetch specific exam part with questions and transcripts.
    6. Submit an exam attempt and get CLB score estimate.
    7. Perform full-text search across the question bank.
    """
    # 1. Check index page
    res = client.get("/")
    assert res.status_code == 200
    assert "CELTESTPIP" in res.text

    # Verify static assets
    css_res = client.get("/static/css/style.css")
    assert css_res.status_code == 200
    assert "body" in css_res.text

    js_res = client.get("/static/js/app.js")
    assert js_res.status_code == 200

    runner_js = client.get("/static/js/exam_runner.js")
    assert runner_js.status_code == 200

    # 2. Check calculator
    res = client.get("/tools/clb-calculator")
    assert res.status_code == 200
    assert "CLB Calculator" in res.text

    calc_js = client.get("/static/js/calculator.js")
    assert calc_js.status_code == 200

    # 3. Check exams API
    res = client.get("/api/exams")
    assert res.status_code == 200
    exams = res.json()
    assert isinstance(exams, list)

    # 4. Insert an end-to-end exam part for verification
    e2e_part = {
        "exam_id": "exam_e2e",
        "part_number": 1,
        "skill": "LISTENING",
        "part_name": "Identifying Similarities and Differences",
        "instructions": "Listen to the conversation and answer questions.",
        "audio_urls": ["/media/audio/e2e_sample.mp3"],
        "image_url": None,
        "transcripts": ["Discussion regarding public transit schedules in Vancouver."],
        "questions": [
            {
                "id": "e2e_q1",
                "question_number": 1,
                "priority": 1,
                "question_text": "What transit option was selected for downtown commute?",
                "audio_url": None,
                "options": ["Skytrain", "Bicycle", "Express Bus", "Ferry"],
                "correct_answer": "1",
                "explanation": "Skytrain offers the most rapid downtown transit connection.",
                "section": 1,
            }
        ],
    }
    insert_exam_part(DB_PATH, e2e_part)

    # 5. Check exam simulator HTML view
    exam_view_res = client.get("/exams/exam_e2e/part/1")
    assert exam_view_res.status_code == 200

    # 6. Check exam part API
    part_res = client.get("/api/exams/exam_e2e/part/1")
    assert part_res.status_code == 200
    part_data = part_res.json()
    assert part_data["exam_id"] == "exam_e2e"
    assert part_data["part_number"] == 1
    assert part_data["skill"] == "LISTENING"
    assert len(part_data["questions"]) == 1
    assert part_data["questions"][0]["options"] == [
        "Skytrain",
        "Bicycle",
        "Express Bus",
        "Ferry",
    ]
    assert "Vancouver" in part_data["transcripts"][0]

    # 7. Check non-existent part returns 404
    missing_res = client.get("/api/exams/nonexistent/part/999")
    assert missing_res.status_code == 404

    # 8. Check attempt submission
    attempt_payload = {
        "exam_id": "exam_e2e",
        "part_number": 1,
        "answers": {"e2e_q1": "1"},
        "score": 1,
        "total_questions": 1,
        "clb_estimate": 10,
    }
    attempt_res = client.post("/api/attempts", json=attempt_payload)
    assert attempt_res.status_code == 200
    attempt_data = attempt_res.json()
    assert attempt_data["status"] == "saved"
    assert attempt_data["clb"] == 10

    # 9. Verify attempt saved in database
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM user_attempts WHERE exam_id = 'exam_e2e' ORDER BY id DESC LIMIT 1"
    )
    row = cur.fetchone()
    assert row is not None
    assert row["score"] == 1
    assert row["clb_estimate"] == 10
    conn.close()

    # 10. Check FTS search
    search_res = client.get("/api/search?q=Skytrain")
    assert search_res.status_code == 200
    search_data = search_res.json()
    assert isinstance(search_data, list)
    assert len(search_data) >= 1
    assert any("Skytrain" in r.get("explanation", "") or "Skytrain" in r.get("question_text", "") for r in search_data)


def test_e2e_offline_build_and_serve_pipeline(tmp_path):
    """End-to-end verification of raw data ingestion -> build_database -> query."""
    raw_dir = tmp_path / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    media_dir = tmp_path / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    part_json = {
        "exam_id": "exam50",
        "part_number": 2,
        "skill": "READING",
        "part_name": "Reading to Apply a Diagram",
        "instructions": "Read the informational email.",
        "audio_urls": [],
        "image_url": "https://celtestpip.com/images/schedule_chart.png",
        "transcripts": [],
        "questions": [
            {
                "id": "q50_2_1",
                "question_number": 1,
                "priority": 1,
                "question_text": "Which workshop commences at 10:00 AM?",
                "audio_url": None,
                "options": ["Resume Building", "Interview Prep", "Networking"],
                "correct_answer": "2",
                "explanation": "The schedule diagram indicates Interview Prep starts at 10:00 AM.",
                "section": 1,
            }
        ],
    }

    raw_file = raw_dir / "exam50_part2.json"
    with open(raw_file, "w", encoding="utf-8") as f:
        json.dump(part_json, f)

    media_map = {
        "https://celtestpip.com/images/schedule_chart.png": "/media/images/schedule_chart.png"
    }
    media_map_file = media_dir / "media_map.json"
    with open(media_map_file, "w", encoding="utf-8") as f:
        json.dump(media_map, f)

    test_db_path = str(tmp_path / "e2e_pipeline.db")
    build_database(
        raw_dir=str(raw_dir),
        db_path=test_db_path,
        media_map_path=str(media_map_file),
    )

    # Verify database contents
    conn = get_db_connection(test_db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exams WHERE id = 'exam50'")
    exam_row = cur.fetchone()
    assert exam_row is not None
    assert exam_row["name"] == "Exam 50"

    cur.execute("SELECT * FROM exam_parts WHERE id = 'exam50_part2'")
    part_row = cur.fetchone()
    assert part_row is not None
    assert part_row["image_url"] == "/media/images/schedule_chart.png"

    cur.execute("SELECT * FROM fts_questions WHERE fts_questions MATCH 'workshop'")
    fts_rows = cur.fetchall()
    assert len(fts_rows) == 1
    assert fts_rows[0]["part_id"] == "exam50_part2"

    conn.close()
