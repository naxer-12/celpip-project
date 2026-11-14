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
    # Test Rich Vocabulary Detail Studio (Matches LanGeek User Screenshot)
    resp_studio = client.get("/fr-EN/vocab/subcategory/12943/learn")
    assert resp_studio.status_code == 200
    assert "handicapé" in resp_studio.text
    assert "Composition" in resp_studio.text
    assert "Masculine Singular" in resp_studio.text
    assert "qui présente une déficience physique ou mentale" in resp_studio.text

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


def test_admin_monitor_and_crawling():
    # Test Admin Monitor Dashboard
    resp_mon = client.get("/admin/monitor")
    assert resp_mon.status_code == 200
    assert "LanGeek Continuous Monitor" in resp_mon.text
    assert "Monitored Reference Routes" in resp_mon.text

    # Test Admin Status API
    resp_stat = client.get("/api/admin/status")
    assert resp_stat.status_code == 200
    data = resp_stat.json()
    assert data["total_monitored"] >= 10
    assert "snapshots" in data
    assert len(data["snapshots"]) >= 10


def test_grammar_hub_and_lessons():
    # Test Grammar Hub with 11 Reference Modules
    resp_hub = client.get("/fr-EN/grammar")
    assert resp_hub.status_code == 200
    assert "French Grammar Guide" in resp_hub.text
    assert "Pronoms" in resp_hub.text
    assert "Déterminants" in resp_hub.text
    assert "Verbes" in resp_hub.text
    assert "Structure de la phrase" in resp_hub.text

    # Test Grammar Lesson Course 86
    resp_lesson = client.get("/fr-EN/grammar/course/86/pronoms-sujets/intermediate")
    assert resp_lesson.status_code == 200
    assert "Pronoms sujets" in resp_lesson.text
    assert "What Are Subject Pronouns" in resp_lesson.text


def test_topic_and_common_vocabulary():
    # Test Topic-Related category (637: Animaux)
    resp_topic = client.get("/fr-EN/vocab/category/637/Animaux")
    assert resp_topic.status_code == 200
    assert "Animaux" in resp_topic.text
    assert "Lessons (" in resp_topic.text

    # Test Most Common category (818: 3000 mots les plus courants)
    resp_common = client.get("/fr-EN/vocab/category/818/3000-mots-francais-les-plus-courants")
    assert resp_common.status_code == 200
    assert "3000" in resp_common.text
    assert "Start" in resp_common.text


def test_grammar_category_module():
    resp_cat = client.get("/fr-EN/grammar/13/pronoms")
    assert resp_cat.status_code == 200
    assert "Pronoms" in resp_cat.text
    assert "Pronoms sujets" in resp_cat.text
    assert "Courses in this Module" in resp_cat.text


def test_reading_comprehension_suite():
    # Test Reading Overview
    resp_read = client.get("/fr-EN/reading")
    assert resp_read.status_code == 200
    assert "Reading comprehension" in resp_read.text
    assert "Browse by Categories" in resp_read.text
    assert "header.png" in resp_read.text
    assert "Animaux" in resp_read.text
    assert "Nature" in resp_read.text
    assert "Maison et meubles" in resp_read.text
    assert "Vie quotidienne" in resp_read.text
    assert "Corps et santé" in resp_read.text

    # Test Reading Collection (87: Animaux)
    resp_col = client.get("/fr-EN/reading/87/animaux")
    assert resp_col.status_code == 200
    assert "Animaux de la ferme" in resp_col.text
    assert "Animaux sauvages" in resp_col.text
    assert "Beginner" in resp_col.text
    assert "6 Stories" in resp_col.text

    # Test Reading Story Redirection (redirects without segment to /0)
    resp_redir = client.get("/fr-EN/reading/course/2304/animaux-de-ferme", follow_redirects=False)
    assert resp_redir.status_code == 307
    assert resp_redir.headers["location"] == "/fr-EN/reading/course/2304/animaux-de-ferme/0"

    # Test Reading Story Segment 0 (Vache)
    resp_story0 = client.get("/fr-EN/reading/course/2304/animaux-de-ferme/0")
    assert resp_story0.status_code == 200
    assert "Animaux de la ferme" in resp_story0.text
    assert "Vache" in resp_story0.text
    assert "Mouton" in resp_story0.text
    assert "Cheval" in resp_story0.text
    assert "Une vache est un grand animal" in resp_story0.text
    assert "story-audio-player" in resp_story0.text
    assert "audio-scrubber" in resp_story0.text
    # Verify PhotoBlock inline illustration is rendered without empty badge
    assert "Story illustration" in resp_story0.text
    assert "Les vaches donnent du lait" in resp_story0.text
    assert "Cows give milk" in resp_story0.text
    assert "1.5" in resp_story0.text
    assert "1.8" in resp_story0.text

    # Test Reading Story Segment 1 (Mouton)
    resp_story1 = client.get("/fr-EN/reading/course/2304/animaux-de-ferme/1")
    assert resp_story1.status_code == 200
    assert "Mouton" in resp_story1.text
    assert "mouton" in resp_story1.text.lower()


def test_pronunciation_alphabet_suite():
    # Test Pronunciation Overview
    resp_pron = client.get("/fr-EN/pronunciation")
    assert resp_pron.status_code == 200
    assert "French Pronunciation" in resp_pron.text
    assert "French Alphabet" in resp_pron.text

    # Test Alphabet Hub (26 Letters)
    resp_alpha = client.get("/fr-EN/pronunciation/101/alphabet-francais")
    assert resp_alpha.status_code == 200
    assert "Alphabet français" in resp_alpha.text
    assert "The Letter \"A\" in French" in resp_alpha.text
    assert "The Letter \"Z\" in French" in resp_alpha.text


def test_auxiliary_pages_and_navigation():
    # Test Plans (Premium Showcase)
    resp_plans = client.get("/fr-EN/plans")
    assert resp_plans.status_code == 200
    assert "LanGeek Premium" in resp_plans.text

    # Test Mobile App Showcase
    resp_app = client.get("/fr-EN/mobile-app")
    assert resp_app.status_code == 200
    assert "iOS & Android" in resp_app.text

    # Test Contact Us
    resp_contact = client.get("/fr-EN/contact-us")
    assert resp_contact.status_code == 200
    assert "Contact LanGeek Support" in resp_contact.text

    # Test Expressions Showcase
    resp_expr = client.get("/fr-EN/expressions")
    assert resp_expr.status_code == 200
    assert "Poser un lapin" in resp_expr.text

    # Test Language Switcher Redirects
    for lang in ["/es", "/de", "/en"]:
        r = client.get(lang, follow_redirects=False)
        assert r.status_code in (302, 307)
        assert r.headers["location"] == "/fr-EN"
