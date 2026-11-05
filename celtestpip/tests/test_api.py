import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app, DB_PATH
from celtestpip.server.database import init_db, insert_exam_part

client = TestClient(app)

def test_api_exams_endpoint():
    response = client.get("/api/exams")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_api_submit_attempt():
    payload = {
        "exam_id": "exam1",
        "part_number": 1,
        "answers": {"q1": "1"},
        "score": 1,
        "total_questions": 1,
        "clb_estimate": 10
    }
    response = client.post("/api/attempts", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "saved"
    assert response.json()["clb"] == 10

def test_api_exam_part_not_found():
    response = client.get("/api/exams/nonexistent/part/99")
    assert response.status_code == 404

def test_api_exam_part_found():
    sample_part = {
        "exam_id": "exam99",
        "part_number": 1,
        "skill": "LISTENING",
        "part_name": "Problem Solving",
        "instructions": "Listen carefully",
        "audio_urls": ["/media/audio/sample.mp3"],
        "image_url": None,
        "transcripts": ["Hello world transcript"],
        "questions": [
            {
                "id": "q1",
                "question_number": 1,
                "priority": 1,
                "question_text": "What is the greeting?",
                "audio_url": None,
                "options": ["Hello", "Goodbye"],
                "correct_answer": "1",
                "explanation": "Said hello",
                "section": 1
            }
        ]
    }
    insert_exam_part(DB_PATH, sample_part)
    
    response = client.get("/api/exams/exam99/part/1")
    assert response.status_code == 200
    data = response.json()
    assert data["exam_id"] == "exam99"
    assert data["part_number"] == 1
    assert data["part_name"] == "Problem Solving"
    assert isinstance(data["audio_urls"], list)
    assert isinstance(data["transcripts"], list)
    assert len(data["questions"]) == 1
    assert data["questions"][0]["options"] == ["Hello", "Goodbye"]

def test_api_search():
    response = client.get("/api/search?q=greeting")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_html_routes():
    res_index = client.get("/")
    assert res_index.status_code == 200
    assert "CELTESTPIP" in res_index.text

    res_exam = client.get("/exams/exam1/part/1")
    assert res_exam.status_code == 200

    res_calc = client.get("/tools/clb-calculator")
    assert res_calc.status_code == 200
    assert "CLB Calculator" in res_calc.text
