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

    # Test progress validation (word_id required)
    resp_no_id = client.post("/api/progress/mark", json={"score": 4})
    assert resp_no_id.status_code == 400
    assert resp_no_id.json()["message"] == "word_id is required"

    # Test FTS5 search with boolean keywords
    resp_bool = client.get("/api/search?q=cat+AND+dog")
    assert resp_bool.status_code == 200
    assert "results" in resp_bool.json()

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
    for lang in ["/es", "/de"]:
        r = client.get(lang, follow_redirects=False)
        assert r.status_code in (302, 307)


def test_locale_routing_and_switcher():
    # Test Root Redirection
    resp_root = client.get("/", follow_redirects=False)
    assert resp_root.status_code in (302, 307)
    assert resp_root.headers["location"] in ("/en", "/fr-EN")
    
    # Test English Home
    resp_en = client.get("/en")
    assert resp_en.status_code == 200
    assert "Learn English with LanGeek" in resp_en.text
    assert "href=\"/fr-EN\"" in resp_en.text
    
    # Test French Home
    resp_fr = client.get("/fr-EN")
    assert resp_fr.status_code == 200
    assert "Apprenez le français" in resp_fr.text
    assert "href=\"/en\"" in resp_fr.text
    
    # Test Aliases
    assert client.get("/en/", follow_redirects=False).headers["location"] == "/en"
    assert client.get("/en-US", follow_redirects=False).headers["location"] == "/en"
    assert client.get("/fr", follow_redirects=False).headers["location"] == "/fr-EN"
    assert client.get("/fr/", follow_redirects=False).headers["location"] == "/fr-EN"

    # Test Path-Preserving Helper
    from langeek.server import get_locale_context
    ctx_en = get_locale_context("en", current_path="/en/vocab")
    assert ctx_en["locale"] == "en"
    assert ctx_en["switch_url"] == "/fr-EN/vocab"
    assert ctx_en["db_locale"] == "en"
    assert ctx_en["lang_code"] == "en"
    assert "lang=en" in ctx_en["dict_url"]

    ctx_fr = get_locale_context("fr-EN", current_path="/fr-EN/reading/course/2304/animaux-de-ferme/0")
    assert ctx_fr["locale"] == "fr-EN"
    assert ctx_fr["switch_url"] == "/en/reading/course/2304/animaux-de-ferme/0"
    assert ctx_fr["db_locale"] == "fr"
    assert ctx_fr["lang_code"] == "fr"
    assert "lang=fr" in ctx_fr["dict_url"]


def test_database_locale_partitioning():
    import sqlite3
    conn = sqlite3.connect("langeek/data/langeek.db")
    cur = conn.cursor()
    tables = [
        "categories", "subcategories", "grammar_categories", 
        "grammar_courses", "reading_collections", "reading_stories", 
        "reading_segments", "pronunciation_courses"
    ]
    for table in tables:
        cols = [c[1] for c in cur.execute(f"PRAGMA table_info({table})").fetchall()]
        assert "locale" in cols, f"Table {table} missing locale column"
    # Verify existing rows default to 'fr'
    fr_count = cur.execute("SELECT count(*) FROM categories WHERE locale = 'fr'").fetchone()[0]
    assert fr_count > 0
    # Verify expressions table exists with locale column
    expr_cols = [c[1] for c in cur.execute("PRAGMA table_info(expressions)").fetchall()]
    assert "locale" in expr_cols, "Table expressions missing locale column"
    # Verify user_progress has locale column
    prog_cols = [c[1] for c in cur.execute("PRAGMA table_info(user_progress)").fetchall()]
    assert "locale" in prog_cols, "Table user_progress missing locale column"
    conn.close()


def test_homepage_subatomic_ui_elements():
    resp = client.get("/en")
    assert resp.status_code == 200
    # 5 module cards with authentic classes and icons
    assert "bg-[#68B4D8]" in resp.text or "sky" in resp.text.lower()
    assert "bg-[#F8A06E]" in resp.text or "peach" in resp.text.lower() or "orange" in resp.text.lower()
    assert "bg-[#64CEB2]" in resp.text or "mint" in resp.text.lower() or "teal" in resp.text.lower()
    assert "bg-[#F8D56F]" in resp.text or "yellow" in resp.text.lower()
    assert "bg-[#E77A6C]" in resp.text or "terracotta" in resp.text.lower() or "rose" in resp.text.lower()
    # Dark mode toggle script in head
    assert "localStorage.theme" in resp.text
    # 4 language pill selectors
    assert "español" in resp.text
    assert "Deutsch" in resp.text


def test_english_flagship_curriculum_seeded():
    import sqlite3
    conn = sqlite3.connect("langeek/data/langeek.db")
    cur = conn.cursor()
    # Check English vocabulary categories
    en_cats = cur.execute("SELECT count(*) FROM categories WHERE locale = 'en'").fetchone()[0]
    assert en_cats >= 6, f"Expected at least 6 English categories, found {en_cats}"
    
    # Check English grammar courses
    en_gram = cur.execute("SELECT count(*) FROM grammar_courses WHERE locale = 'en'").fetchone()[0]
    assert en_gram >= 5, f"Expected at least 5 English grammar courses, found {en_gram}"
    
    # Check English expressions
    en_expr = cur.execute("SELECT count(*) FROM expressions WHERE locale = 'en'").fetchone()[0]
    assert en_expr >= 5, f"Expected at least 5 English expressions, found {en_expr}"
    
    # Check English pronunciation courses
    en_pron = cur.execute("SELECT count(*) FROM pronunciation_courses WHERE locale = 'en'").fetchone()[0]
    assert en_pron >= 26, f"Expected 26 English alphabet letters, found {en_pron}"
    
    # Check English reading stories
    en_read = cur.execute("SELECT count(*) FROM reading_stories WHERE locale = 'en'").fetchone()[0]
    assert en_read >= 3, f"Expected at least 3 English reading stories, found {en_read}"
    conn.close()


def test_french_curriculum_integrity_preserved():
    import sqlite3
    conn = sqlite3.connect("langeek/data/langeek.db")
    cur = conn.cursor()
    assert cur.execute("SELECT count(*) FROM categories WHERE locale = 'fr'").fetchone()[0] == 44
    assert cur.execute("SELECT count(*) FROM subcategories WHERE locale = 'fr'").fetchone()[0] == 796
    assert cur.execute("SELECT count(*) FROM grammar_categories WHERE locale = 'fr'").fetchone()[0] == 11
    assert cur.execute("SELECT count(*) FROM grammar_courses WHERE locale = 'fr'").fetchone()[0] == 74
    assert cur.execute("SELECT count(*) FROM reading_collections WHERE locale = 'fr'").fetchone()[0] == 5
    assert cur.execute("SELECT count(*) FROM reading_stories WHERE locale = 'fr'").fetchone()[0] == 30
    assert cur.execute("SELECT count(*) FROM reading_segments WHERE locale = 'fr'").fetchone()[0] == 179
    assert cur.execute("SELECT count(*) FROM pronunciation_courses WHERE locale = 'fr'").fetchone()[0] == 26
    conn.close()


@pytest.mark.asyncio
async def test_cache_through_fallback_interface():
    from unittest.mock import patch, AsyncMock
    import httpx
    from langeek.server import fetch_and_cache_upstream
    mock_resp = httpx.Response(404, request=httpx.Request("GET", "https://langeek.co/test"))
    with patch("httpx.AsyncClient.get", new_callable=AsyncMock, return_value=mock_resp):
        # Test handling of non-existent upstream path returns False gracefully without throwing
        res = await fetch_and_cache_upstream("en/non-existent-sample-route-999999", db_locale="en")
        assert res is False


def test_english_five_modules_rendering():
    # 1. Vocabulary
    r_vocab = client.get("/en/vocab")
    assert r_vocab.status_code == 200
    assert "English Vocabulary" in r_vocab.text
    assert "/en/vocab/category/2001/a1-level" in r_vocab.text
    assert "Level-Based English Vocabulary" in r_vocab.text
    
    # 2. Grammar
    r_gram = client.get("/en/grammar")
    assert r_gram.status_code == 200
    assert "English Grammar" in r_gram.text
    assert "/en/grammar/course/" in r_gram.text
    assert "Complete English Grammar Syllabus" in r_gram.text
    
    # 3. Expressions
    r_expr = client.get("/en/expressions")
    assert r_expr.status_code == 200
    assert "English Expressions" in r_expr.text or "Idioms" in r_expr.text
    assert "Bite the bullet" in r_expr.text or "Break the ice" in r_expr.text
    
    # 4. Pronunciation
    r_pron = client.get("/en/pronunciation")
    assert r_pron.status_code == 200
    assert "English Pronunciation" in r_pron.text
    assert "/en/pronunciation/101/alphabet" in r_pron.text
    
    # 5. Reading
    r_read = client.get("/en/reading")
    assert r_read.status_code == 200
    assert "English Reading" in r_read.text or "Reading Comprehension" in r_read.text
    assert "/en/reading/" in r_read.text
    assert "Famous Figures" in r_read.text or "Nature and Wildlife" in r_read.text


def test_dual_locale_search_and_progress():
    # Test English Search
    r_search_en = client.get("/api/search?q=animal&locale=en")
    assert r_search_en.status_code == 200
    data_en = r_search_en.json()
    assert "results" in data_en
    assert len(data_en["results"]) > 0
    assert all(r.get("locale") == "en" for r in data_en["results"])

    # Test French Search
    r_search_fr = client.get("/api/search?q=animal&locale=fr-EN")
    assert r_search_fr.status_code == 200
    data_fr = r_search_fr.json()
    assert "results" in data_fr
    assert len(data_fr["results"]) > 0
    assert all(r.get("locale") in ("fr", "fr-EN") for r in data_fr["results"])

    # Test Leitner progress recording with locale
    r_prog_en = client.post("/api/progress/record", json={"word_id": 1000016, "score": 4, "locale": "en"})
    assert r_prog_en.status_code == 200
    assert r_prog_en.json()["status"] == "recorded"
    assert r_prog_en.json()["state"] == "mastered"

    r_prog_fr = client.post("/api/progress/record", json={"word_id": 866216, "score": 3, "locale": "fr-EN"})
    assert r_prog_fr.status_code == 200
    assert r_prog_fr.json()["status"] == "recorded"
    assert r_prog_fr.json()["state"] == "learned"

    # Test progress validation (word_id required)
    resp_no_id = client.post("/api/progress/mark", json={"score": 4})
    assert resp_no_id.status_code == 400
    assert resp_no_id.json()["message"] == "word_id is required"

    # Test FTS5 search with boolean keywords
    resp_bool = client.get("/api/search?q=cat+AND+dog")
    assert resp_bool.status_code == 200
    assert "results" in resp_bool.json()

    # Test progress summary per locale
    r_sum_en = client.get("/api/progress/summary?locale=en")
    assert r_sum_en.status_code == 200
    data_sum_en = r_sum_en.json()
    assert data_sum_en["mastered"] >= 1

    r_sum_fr = client.get("/api/progress/summary?locale=fr-EN")
    assert r_sum_fr.status_code == 200
    data_sum_fr = r_sum_fr.json()
    assert data_sum_fr["learned"] >= 1


def test_comprehensive_platform_verification():
    """Task 7: Comprehensive verification across both locales and sub-atomic platform components."""
    locales = ["en", "fr-EN"]
    sections = ["vocab", "grammar", "expressions", "pronunciation", "reading"]

    # Verify all 5 core modules render with HTTP 200 in both locales
    for loc in locales:
        home_res = client.get(f"/{loc}")
        assert home_res.status_code == 200
        assert "LanGeek" in home_res.text

        for sec in sections:
            sec_res = client.get(f"/{loc}/{sec}")
            assert sec_res.status_code == 200, f"Failed for {loc}/{sec}"

    # Verify Reading story with chapter stepper, photo, translation
    story_res = client.get("/fr-EN/reading/course/2304/animaux-de-ferme/0")
    assert story_res.status_code == 200
    assert "Animaux de la ferme" in story_res.text
    assert "Vache" in story_res.text
    assert "audio-scrubber" in story_res.text

    # Verify search escaping and boolean token safety
    search_res = client.get("/api/search?q=NOT+AND+OR+fruit*")
    assert search_res.status_code == 200
    assert "results" in search_res.json()

    # Verify progress recording validation
    bad_req1 = client.post("/api/progress/record", json={"score": 5})
    assert bad_req1.status_code == 400
    assert bad_req1.json()["message"] == "word_id is required"

    bad_req2 = client.post("/api/progress/mark", json={"word_id": None, "score": 2})
    assert bad_req2.status_code == 400
    assert bad_req2.json()["message"] == "word_id is required"







