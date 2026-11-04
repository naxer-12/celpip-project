import os
import pytest

def test_english_edition_curriculum_data():
    import french_grammar_en_data as en_data

    assert len(en_data.TOPICS) == 4
    assert len(en_data.QUESTIONS) == 80

    for q in en_data.QUESTIONS:
        assert "prompt_fr" in q and len(q["prompt_fr"].strip()) > 0
        assert "prompt_en" in q and len(q["prompt_en"].strip()) > 0
        assert "explanation_en" in q and len(q["explanation_en"].strip()) > 0
        assert "scenario_bilingual" in q and len(q["scenario_bilingual"].strip()) > 0
        assert q["level"] in ("A1", "A2")

def test_english_edition_html_generation():
    html_path = "French_Grammar_Practice_English_Edition.html"
    assert os.path.exists(html_path), "HTML file must exist"
    
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify structural and CSS features
    assert "<!DOCTYPE html>" in content
    assert "prompt-en" in content or "sub-translation" in content
    assert "@page" in content
    assert "size: A4 portrait" in content
    assert "page-break-before: always" in content or "break-before: page" in content
    assert "Answer Key &amp; Grammar Notes" in content or "Answer Key & Grammar Notes" in content
    
    # Verify all 80 questions are present
    for i in range(1, 81):
        assert f'id="q{i}"' in content
