# French Grammar Practice Workbook (A1–A2) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a minimalist, visually clean, typography-focused French grammar practice workbook HTML with 80 contextual questions (4 topics × 20 questions; 10 A1 + 10 A2 per topic) and complete answer key, print-ready for A4 PDF.

**Architecture:** A decoupled architecture with a structured curriculum data module (`french_grammar_data.py`), a suite of automated validation tests (`test_french_grammar_data.py` and `test_grammar_practice_html.py`), and a standalone HTML generator (`build_grammar_practice_html.py`) that outputs `French_Grammar_Practice_A1_A2.html` with pure CSS paged media formatting.

**Tech Stack:** Python 3, Pytest, HTML5, CSS3 (Paged Media `@page`, Flexbox, Grid).

**Spec:** `docs/superpowers/specs/2026-11-04-french-grammar-practice-design.md`

## Global Constraints
- Target 4 topics: Articles & Determiners, Verb Tenses & Conjugations, Prepositions, Pronouns.
- Exactly 20 questions per topic: 10 A1 questions and 10 A2 questions (80 questions total).
- 4 rotating question formats: fill-in-the-blank, multiple choice, error correction, short translation.
- Natural, real-life communicative contexts for every question (café, email, directions, travel, daily life).
- Minimalist design: clean single sans-serif typography, generous whitespace, soft pill tags (`A1` mint green, `A2` soft sky blue), hairline dividers, zero shadows/borders/illustrations.
- Answer key on final page (`page-break-before: always;`) in compact multi-column format with brief grammatical explanations.
- Output file: `French_Grammar_Practice_A1_A2.html` in workspace root.

---

### Task 1: Create the Test Suite for Curriculum Data

**Files:**
- Create: `test_french_grammar_data.py`

**Interfaces:**
- Consumes: `TOPICS`, `QUESTIONS` from `french_grammar_data.py`
- Produces: Test runner verification for question counts, CEFR distribution, formatting, and answer keys.

- [ ] **Step 1: Write the failing test**

```python
import pytest

def test_curriculum_structure():
    import french_grammar_data as data
    
    # 4 topics
    assert len(data.TOPICS) == 4
    expected_topics = [
        "Les Articles & Les Déterminants",
        "Les Temps Verbaux & Conjugaisons",
        "Les Prépositions",
        "Les Pronoms"
    ]
    for topic in expected_topics:
        assert topic in data.TOPICS

    # Exactly 80 questions
    assert len(data.QUESTIONS) == 80
    
    # Check IDs 1 to 80 sequentially
    ids = [q["id"] for q in data.QUESTIONS]
    assert ids == list(range(1, 81))

def test_topic_distribution_and_cefr_levels():
    import french_grammar_data as data
    
    for topic in data.TOPICS:
        topic_questions = [q for q in data.QUESTIONS if q["topic"] == topic]
        assert len(topic_questions) == 20
        
        a1_questions = [q for q in topic_questions if q["level"] == "A1"]
        a2_questions = [q for q in topic_questions if q["level"] == "A2"]
        assert len(a1_questions) == 10
        assert len(a2_questions) == 10

def test_question_types_and_fields():
    import french_grammar_data as data
    
    valid_types = {"fill_in_the_blank", "multiple_choice", "error_correction", "translation"}
    
    for q in data.QUESTIONS:
        assert q["type"] in valid_types
        assert len(q["prompt"].strip()) > 0
        assert len(q["scenario"].strip()) > 0
        assert len(q["answer"].strip()) > 0
        assert len(q["explanation"].strip()) > 0
        
        if q["type"] == "multiple_choice":
            assert "options" in q
            assert len(q["options"]) == 4
            assert any(q["answer"].startswith(opt[:2]) or q["answer"] == opt for opt in q["options"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest test_french_grammar_data.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'french_grammar_data'"

- [ ] **Step 3: Commit test file**

```bash
git add test_french_grammar_data.py
git commit -m "test: add test suite for French grammar curriculum data"
```

---

### Task 2: Implement Complete French Grammar Curriculum Data (80 Questions)

**Files:**
- Create: `french_grammar_data.py`

**Interfaces:**
- Consumes: None
- Produces: `TOPICS: list[str]`, `QUESTIONS: list[dict]`

- [ ] **Step 1: Write complete curriculum data with all 80 questions and explanations**

Implement `french_grammar_data.py` covering:
- **Topic 1: Les Articles & Les Déterminants** (Q1–Q10 A1, Q11–Q20 A2)
- **Topic 2: Les Temps Verbaux & Conjugaisons** (Q21–Q30 A1, Q31–Q40 A2)
- **Topic 3: Les Prépositions** (Q41–Q50 A1, Q51–Q60 A2)
- **Topic 4: Les Pronoms** (Q61–Q70 A1, Q71–Q80 A2)
All items with realistic scenarios, varied question types, exact answers, and concise grammatical justifications.

- [ ] **Step 2: Run tests to verify curriculum data passes**

Run: `pytest test_french_grammar_data.py -v`
Expected: PASS (all 3 tests passing)

- [ ] **Step 3: Commit curriculum data**

```bash
git add french_grammar_data.py
git commit -m "feat: implement complete 80-question French grammar curriculum data"
```

---

### Task 3: Create HTML Generator Test and Implementation

**Files:**
- Create: `test_grammar_practice_html.py`
- Create: `build_grammar_practice_html.py`
- Output: `French_Grammar_Practice_A1_A2.html`

**Interfaces:**
- Consumes: `french_grammar_data.py`
- Produces: `French_Grammar_Practice_A1_A2.html`

- [ ] **Step 1: Write failing HTML test**

Write `test_grammar_practice_html.py` checking:
- HTML file exists
- Contains doctype, Inter / system sans-serif typography rules
- Contains print media styles (`@media print`, `@page { size: A4 portrait; margin: 18mm; }`)
- Contains all 4 section titles
- Contains all 80 question IDs
- Contains CEFR badges with correct CSS classes
- Contains Answer Key section with forced page break (`page-break-before: always;`)

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest test_grammar_practice_html.py -v`
Expected: FAIL (file does not exist yet)

- [ ] **Step 3: Implement `build_grammar_practice_html.py`**

Write clean generator script using semantic HTML, pure CSS layout, hairline borders, soft colored tags, single-column vertical flow, and 4-column compact answer key on final page.
Execute `python3 build_grammar_practice_html.py` to generate `French_Grammar_Practice_A1_A2.html`.

- [ ] **Step 4: Run HTML test to verify it passes**

Run: `pytest test_grammar_practice_html.py -v`
Expected: PASS

- [ ] **Step 5: Commit generator and tests**

```bash
git add test_grammar_practice_html.py build_grammar_practice_html.py French_Grammar_Practice_A1_A2.html
git commit -m "feat: implement HTML generator for French grammar practice workbook"
```

---

### Task 4: Visual & Content Verification

**Files:**
- Read/Inspect: `French_Grammar_Practice_A1_A2.html`

**Interfaces:**
- Consumes: `French_Grammar_Practice_A1_A2.html`
- Produces: Visual verification confirmation, print layout check, and final summary.

- [ ] **Step 1: Run comprehensive pytest suite across both test files**

Run: `pytest test_french_grammar_data.py test_grammar_practice_html.py -v`
Expected: All tests pass.

- [ ] **Step 2: Verify HTML in browser / headless engine for print formatting and visual elegance**

Test rendering and inspect DOM elements to ensure no overlapping elements, clean margins, and proper page breaks.

- [ ] **Step 3: Final git commit & report to user**

Provide clear instructions for viewing and printing to PDF.
