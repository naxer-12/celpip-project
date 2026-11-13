"""Unit & Integration Test Suite for LanGeek Ditto Replica.

Verifies page rendering, CEFR category details, interactive Flashcard & Quiz suites,
SQLite indexing, FTS5 full-text search, media proxy, and progress tracking.
"""

import os
import json
import sqlite3
import pytest
from fastapi.testclient import TestClient

from langeek.server import app

client = TestClient(app)

def test_home_page_rendering():
    resp = client.get("/fr-EN")
    assert resp.status_code == 200
    assert "Learn French with" in resp.text
    assert "Vocabulary" in resp.text
    assert "Grammar" in resp.text
    assert "Reading" in resp.text
    assert "Pronunciation" in resp.text
    assert "logo-fr.svg" in resp.text


def test_vocab_overview_rendering():
    resp = client.get("/fr-EN/vocab")
    assert resp.status_code == 200
    assert "Level-Based French Vocabulary" in resp.text
    assert "A1" in resp.text
    assert "Beginner" in resp.text
    assert "C1" in resp.text
    assert "Advanced" in resp.text
    assert "Words learned" in resp.text
    assert "Daily Goal" in resp.text


def test_category_detail_rendering():
    # Test C1 Level Category (750 / niveau-c1)
    resp = client.get("/fr-EN/vocab/category/750/niveau-c1")
    assert resp.status_code == 200
    assert "French C1 Vocabulary" in resp.text
    assert "Appearance and Physical Characteristics" in resp.text
    assert "Flashcards" in resp.text
    assert "Quiz" in resp.text
    assert "Spelling" in resp.text
    assert "Wordlist" in resp.text


def test_interactive_learning_suites():
    # Test Flashcard learner for subcategory 12943
    resp_flash = client.get("/fr-EN/vocab/subcategory/12943/learn/flashcard")
    assert resp_flash.status_code == 200
    assert "Card 1" in resp_flash.text
    assert "handicap" in resp_flash.text.lower() or "wordsData" in resp_flash.text

    # Test Quiz mode
    resp_quiz = client.get("/fr-EN/vocab/subcategory/12943/learn/quiz")
    assert resp_quiz.status_code == 200
    assert "Score:" in resp_quiz.text

    # Test Spelling mode
    resp_spell = client.get("/fr-EN/vocab/subcategory/12943/learn/spelling")
    assert resp_spell.status_code == 200
    assert "Type the French word" in resp_spell.text


def test_static_assets_and_icons():
    # Test logo
    resp_logo = client.get("/assets/logo/logo-fr.svg")
    assert resp_logo.status_code == 200
    assert "image/svg+xml" in resp_logo.headers.get("content-type", "")

    # Test CEFR plant icons
    resp_icon = client.get("/assets/img/vocab/cefr-a1.svg")
    assert resp_icon.status_code == 200
    assert "image/svg+xml" in resp_icon.headers.get("content-type", "")


def test_search_and_progress_apis():
    # Test FTS5 search
    resp_search = client.get("/api/search?q=salut")
    assert resp_search.status_code == 200
    data = resp_search.json()
    assert "results" in data

    # Test progress recording
    resp_prog = client.post("/api/progress/mark", json={"word_id": 866216, "score": 4})
    assert resp_prog.status_code == 200
    assert resp_prog.json()["status"] == "recorded"
    assert resp_prog.json()["state"] == "mastered"

    # Test progress summary
    resp_sum = client.get("/api/progress/summary")
    assert resp_sum.status_code == 200
    assert resp_sum.json()["status"] == "success"
    assert resp_sum.json()["mastered"] >= 1
