import pytest
import sqlite3
import os
import json
from celtestpip.server.scoring import raw_score_to_clb
from celtestpip.server.database import init_db, insert_exam_part, get_exam_parts, get_db_connection

def test_clb_scoring():
    assert raw_score_to_clb("LISTENING", 38) == 12
    assert raw_score_to_clb("LISTENING", 36) >= 10
    assert raw_score_to_clb("READING", 38) == 12
    assert raw_score_to_clb("READING", 0) == 3

def test_database_insert_and_query(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)
    
    sample_part = {
        "exam_id": "exam1",
        "part_number": 1,
        "skill": "LISTENING",
        "part_name": "Problem Solving",
        "instructions": "Listen carefully",
        "audio_urls": ["/media/audio/sample.mp3"],
        "image_url": None,
        "transcripts": ["Hello world"],
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
    
    insert_exam_part(db_path, sample_part)
    parts = get_exam_parts(db_path, "exam1")
    assert len(parts) == 1
    assert parts[0]["part_name"] == "Problem Solving"

def test_database_with_media_map_and_fts(tmp_path):
    db_path = str(tmp_path / "test_fts.db")
    init_db(db_path)

    media_map = {
        "https://example.com/audio1.mp3": "/media/audio/audio1.mp3",
        "https://example.com/img1.png": "/media/images/img1.png",
        "https://example.com/q1.mp3": "/media/audio/q1.mp3"
    }

    sample_part = {
        "exam_id": "exam2",
        "part_number": 2,
        "skill": "READING",
        "part_name": "Reading to Apply a Diagram",
        "instructions": "Read the email and look at the diagram.",
        "audio_urls": ["https://example.com/audio1.mp3"],
        "image_url": "https://example.com/img1.png",
        "transcripts": [],
        "questions": [
            {
                "id": "q2",
                "question_number": 1,
                "priority": 1,
                "question_text": "Where should the package be delivered?",
                "audio_url": "https://example.com/q1.mp3",
                "options": ["Front door", "Back porch"],
                "correct_answer": "1",
                "explanation": "The note specifies the front door.",
                "section": 1
            }
        ]
    }

    insert_exam_part(db_path, sample_part, media_map=media_map)

    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT audio_urls_json, image_url FROM exam_parts WHERE id = 'exam2_part2'")
    row = cur.fetchone()
    audio_urls = json.loads(row["audio_urls_json"])
    assert audio_urls == ["/media/audio/audio1.mp3"]
    assert row["image_url"] == "/media/images/img1.png"

    cur.execute("SELECT audio_url FROM questions WHERE id = 'q2'")
    qrow = cur.fetchone()
    assert qrow["audio_url"] == "/media/audio/q1.mp3"

    # Test FTS5 search
    cur.execute("SELECT part_id, question_text FROM fts_questions WHERE fts_questions MATCH 'package'")
    fts_rows = cur.fetchall()
    assert len(fts_rows) == 1
    assert fts_rows[0]["part_id"] == "exam2_part2"

    # Test idempotency (re-insert should not duplicate FTS rows)
    insert_exam_part(db_path, sample_part, media_map=media_map)
    cur.execute("SELECT part_id, question_text FROM fts_questions WHERE fts_questions MATCH 'package'")
    fts_rows_after = cur.fetchall()
    assert len(fts_rows_after) == 1

    conn.close()

def test_build_db_pipeline(tmp_path):
    from celtestpip.build_db import build_database

    raw_dir = tmp_path / "raw"
    raw_dir.mkdir()
    media_dir = tmp_path / "media"
    media_dir.mkdir()

    sample_data = {
        "exam_id": "exam3",
        "part_number": 1,
        "skill": "LISTENING",
        "part_name": "Listening Test",
        "instructions": "Instructions here",
        "audio_urls": ["http://remote.url/audio.mp3"],
        "image_url": None,
        "transcripts": ["Transcript line"],
        "questions": [
            {
                "id": "q3",
                "question_number": 1,
                "priority": 1,
                "question_text": "Sample question?",
                "audio_url": None,
                "options": ["A", "B"],
                "correct_answer": "1",
                "explanation": "Because A",
                "section": 1
            }
        ]
    }
    with open(raw_dir / "exam3_part1.json", "w", encoding="utf-8") as f:
        json.dump(sample_data, f)

    media_map_path = str(media_dir / "media_map.json")
    with open(media_map_path, "w", encoding="utf-8") as f:
        json.dump({"http://remote.url/audio.mp3": "/media/audio/audio.mp3"}, f)

    db_path = str(tmp_path / "pipeline.db")
    build_database(raw_dir=str(raw_dir), db_path=db_path, media_map_path=media_map_path)

    parts = get_exam_parts(db_path, "exam3")
    assert len(parts) == 1
    assert parts[0]["part_name"] == "Listening Test"
    audio_urls = json.loads(parts[0]["audio_urls_json"])
    assert audio_urls == ["/media/audio/audio.mp3"]
