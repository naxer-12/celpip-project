"""Tests for French Grammar Practice HTML generation and formatting."""

import html
import os
import re
import pytest
import french_grammar_data as data

HTML_FILE = "French_Grammar_Practice_A1_A2.html"


def get_html_content():
    assert os.path.exists(HTML_FILE), f"Expected {HTML_FILE} to exist."
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        return f.read()


def test_html_file_exists():
    assert os.path.exists(HTML_FILE), f"File {HTML_FILE} not found."


def test_doctype_and_typography():
    content = get_html_content()
    # Must have doctype
    assert "<!DOCTYPE html>" in content or "<!doctype html>" in content.lower()

    # Must specify Inter and system sans-serif font stack
    assert "Inter" in content
    assert "-apple-system" in content or "system-ui" in content or "BlinkMacSystemFont" in content
    assert "sans-serif" in content


def test_paged_media_and_print_styles():
    content = get_html_content()
    # Must contain @page declaration with A4 portrait and 18mm margin
    assert "@page" in content
    assert "size: A4 portrait" in content or "A4 portrait" in content
    assert "18mm" in content

    # Must have print media queries
    assert "@media print" in content

    # Question containers must avoid page break inside
    assert "break-inside: avoid" in content or "page-break-inside: avoid" in content


def test_topic_sections_present():
    content = get_html_content()
    for topic in data.TOPICS:
        escaped_topic = html.escape(topic)
        assert topic in content or escaped_topic in content, f"Topic '{topic}' not found in HTML"


def test_all_80_questions_present():
    content = get_html_content()
    # Verify count of question elements
    question_matches = re.findall(r'id="q\d+"', content)
    assert len(question_matches) == 80, f"Expected exactly 80 question IDs, found {len(question_matches)}"

    for q in data.QUESTIONS:
        qid = q["id"]
        # Question identifier must be present in DOM
        assert f'id="q{qid}"' in content, f"Question ID 'q{qid}' not found in HTML"

        # Context scenario should appear
        escaped_scenario = html.escape(q["scenario"])
        assert q["scenario"] in content or escaped_scenario in content, (
            f"Scenario '{q['scenario']}' for Q{qid} not found"
        )

        # Question prompt must appear
        escaped_prompt = html.escape(q["prompt"])
        assert q["prompt"] in content or escaped_prompt in content, (
            f"Prompt for Q{qid} not found"
        )


def test_cefr_badges():
    content = get_html_content()
    # Check badge classes
    assert "badge-a1" in content
    assert "badge-a2" in content

    # Exactly 40 A1 badges and 40 A2 badges in the question list
    a1_badges = len(re.findall(r'class="badge badge-a1"', content))
    a2_badges = len(re.findall(r'class="badge badge-a2"', content))
    assert a1_badges == 40, f"Expected 40 A1 badges, found {a1_badges}"
    assert a2_badges == 40, f"Expected 40 A2 badges, found {a2_badges}"

    # Check colors defined in spec
    assert "#e6f4ea" in content.lower()  # A1 mint green bg
    assert "#137333" in content.lower()  # A1 deep forest green text
    assert "#e8f0fe" in content.lower()  # A2 soft blue bg
    assert "#1a73e8" in content.lower()  # A2 deep cobalt blue text


def test_answer_key_and_page_break():
    content = get_html_content()
    # Must have an answer key section
    assert "Corrigés" in content or "Answer Key" in content or "Solutions" in content

    # Must force page break before answer key
    assert "page-break-before: always" in content or "break-before: page" in content

    # Multi-column layout for answer key
    assert "column-count: 4" in content or "columns: 4" in content

    # Check that all 80 answers and explanations are included
    for q in data.QUESTIONS:
        escaped_ans = html.escape(q["answer"])
        assert q["answer"] in content or escaped_ans in content, (
            f"Answer for Q{q['id']} not found in HTML"
        )

        escaped_exp = html.escape(q["explanation"])
        assert q["explanation"] in content or escaped_exp in content, (
            f"Explanation for Q{q['id']} not found in HTML"
        )
