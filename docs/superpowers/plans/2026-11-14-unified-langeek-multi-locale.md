# Unified LanGeek Multi-Locale Platform Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the LanGeek learning application into a high-performance, multi-locale platform mirroring `https://langeek.co/en/` down to sub-atomic details (typography, tactile cards, SVG patterns, dark mode, audio dock, ⌘K search) across English (`/en/*`) and French (`/fr-EN/*`) for all 5 core modules (Vocabulary, Grammar, Expressions, Pronunciation, Reading).

**Architecture:** A unified parameterized FastAPI application serving Jinja2/Tailwind components backed by partitioned SQLite tables (`locale = 'en' | 'fr'`), supported by a hybrid Ditto crawler engine that seeds flagship curricula and lazily fetches uncached courses on demand, with binary-safe media caching via `/media-proxy`.

**Tech Stack:** Python 3.14, FastAPI, SQLite (FTS5 + JSON1), Jinja2, Tailwind CSS, Lucide Icons, Playwright, Pytest.

**Spec:** [docs/superpowers/specs/2026-11-14-unified-langeek-multi-locale-design.md](file:///Users/jainamshah/Downloads/Learning%20French/docs/superpowers/specs/2026-11-14-unified-langeek-multi-locale-design.md)

## Global Constraints

* Local response time must remain under $5\text{ms}$ for cached pages and queries.
* Zero Layout Shift (CLS = 0) with explicit aspect ratios on all cards and illustrations.
* Zero Flash of Unstyled Theme (FOUT) with synchronous `<head>` dark mode script.
* Existing French curriculum, audio links, and photo blocks must remain 100% functional with zero regressions.
* URL routing must follow canonical conventions (`/en/*`, `/fr-EN/*`) with intelligent path-preserving locale toggles.

---

### Task 1: Database Schema Migration & Multi-Locale Partitioning

**Files:**
- Create: `langeek/migrations/add_locale_partitioning.py`
- Modify: `langeek/server.py:30-80`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: Existing tables in `langeek/data/langeek.db` (`categories`, `subcategories`, `grammar_categories`, `grammar_courses`, `reading_collections`, `reading_stories`, `pronunciation_courses`, `user_progress`, `search_fts`).
- Produces: Migration function `migrate_locale_partitioning(db_path)` that adds `locale TEXT NOT NULL DEFAULT 'fr'` to all content tables, creates multi-column indices, updates `user_progress` with `locale`, and migrates existing French records without data loss.

- [ ] **Step 1: Write failing test for database partitioning**

```python
# In langeek/tests/test_replica.py
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
    conn.close()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_database_locale_partitioning -v`  
Expected: FAIL with `AssertionError: Table categories missing locale column`

- [ ] **Step 3: Implement database migration script**

```python
# langeek/migrations/add_locale_partitioning.py
import sqlite3

def migrate_locale_partitioning(db_path="langeek/data/langeek.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    tables = [
        "categories", "subcategories", "grammar_categories", 
        "grammar_courses", "reading_collections", "reading_stories", 
        "reading_segments", "pronunciation_courses"
    ]
    
    for table in tables:
        cols = [c[1] for c in cur.execute(f"PRAGMA table_info({table})").fetchall()]
        if "locale" not in cols:
            cur.execute(f"ALTER TABLE {table} ADD COLUMN locale TEXT NOT NULL DEFAULT 'fr'")
    
    # Create expressions table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expressions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            locale TEXT NOT NULL DEFAULT 'fr',
            category TEXT NOT NULL,
            phrase TEXT NOT NULL,
            literal_translation TEXT,
            meaning TEXT NOT NULL,
            examples_json TEXT,
            audio_url TEXT,
            position INTEGER DEFAULT 0
        )
    """)
    
    # Update user_progress table
    prog_cols = [c[1] for c in cur.execute("PRAGMA table_info(user_progress)").fetchall()]
    if "locale" not in prog_cols:
        cur.execute("ALTER TABLE user_progress ADD COLUMN locale TEXT NOT NULL DEFAULT 'fr'")
        
    # Indices for blazing-fast indexed querying
    cur.execute("CREATE INDEX IF NOT EXISTS idx_cat_loc ON categories(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_subcat_loc ON subcategories(category_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_gram_cat_loc ON grammar_categories(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_gram_course_loc ON grammar_courses(category_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_read_col_loc ON reading_collections(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_read_story_loc ON reading_stories(collection_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_expr_loc ON expressions(locale, category)")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    migrate_locale_partitioning()
```

- [ ] **Step 4: Run migration and verify test passes**

Run: `python3 langeek/migrations/add_locale_partitioning.py`  
Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_database_locale_partitioning -v`  
Expected: PASS

- [ ] **Step 5: Commit migration**

```bash
git add langeek/migrations/add_locale_partitioning.py langeek/data/langeek.db langeek/tests/test_replica.py
git commit -m "feat(db): add multi-locale partitioning and indices to SQLite schema"
```

---

### Task 2: Multi-Locale Routing Pipeline & Path-Preserving Switcher

**Files:**
- Modify: `langeek/server.py`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: `locale` parameter from HTTP routes (`/en/*` and `/fr-EN/*`).
- Produces: `get_locale_context(locale: str, active_tab: str, current_path: str)` dependency returning standardized metadata, dictionary link, and switch target URLs.

- [ ] **Step 1: Write failing test for multi-locale routes and path preservation**

```python
# In langeek/tests/test_replica.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_locale_routing_and_switcher -v`  
Expected: FAIL

- [ ] **Step 3: Implement multi-locale routing and context dependency**

In `langeek/server.py`:
- Define helper:
  ```python
  def get_locale_context(locale: str, request: Request, active_tab: str = "home") -> dict:
      loc = "en" if locale == "en" else "fr-EN"
      path = request.url.path
      
      # Build equivalent switch URL
      if loc == "en":
          switch_url = path.replace("/en", "/fr-EN", 1) if path.startswith("/en") else "/fr-EN"
      else:
          switch_url = path.replace("/fr-EN", "/en", 1) if path.startswith("/fr-EN") else "/en"
          
      return {
          "locale": loc,
          "db_locale": "en" if loc == "en" else "fr",
          "lang_code": "en" if loc == "en" else "fr",
          "locale_name": "English" if loc == "en" else "Français",
          "flag_icon": "gb" if loc == "en" else "fr",
          "active_tab": active_tab,
          "switch_url": switch_url,
          "dict_url": "https://dictionary.langeek.co/?lang=en" if loc == "en" else "https://dictionary.langeek.co/?lang=fr"
      }
  ```
- Mount `/en` and `/fr-EN` endpoints for Home, Vocab, Grammar, Expressions, Pronunciation, and Reading.
- Add redirect handlers for `/`, `/en/`, `/en-US`, `/fr`, and `/fr/`.

- [ ] **Step 4: Run test to verify it passes**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_locale_routing_and_switcher -v`  
Expected: PASS

- [ ] **Step 5: Commit routing overhaul**

```bash
git add langeek/server.py langeek/tests/test_replica.py
git commit -m "feat(routing): implement unified multi-locale pipeline and path-preserving switcher"
```

---

### Task 3: Sub-Atomic UI/UX System & Design Tokens

**Files:**
- Modify: `langeek/templates/base.html`
- Modify: `langeek/templates/home.html`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: `locale_context` dictionary from `server.py`.
- Produces: Pixel-perfect header bar, dark/light mode toggle with zero FOUT, language switcher pill, 5 iconic wavy module cards (Sky Blue `#68B4D8`, Warm Peach `#F8A06E`, Mint Aquamarine `#64CEB2`, Buttercup Yellow `#F8D56F`, Terracotta Salmon `#E77A6C`), and download footer banner.

- [ ] **Step 1: Write failing test for sub-atomic UI elements**

```python
# In langeek/tests/test_replica.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_homepage_subatomic_ui_elements -v`  
Expected: FAIL

- [ ] **Step 3: Update `base.html` and `home.html` with authentic tokens and SVG patterns**

- In `base.html`:
  - Add synchronous inline theme initialization script in `<head>` to prevent FOUT.
  - Implement top navigation bar with Dictionary, Mobile App, Contact Us, Premium crown, and moon/sun theme toggle.
  - Add LanGeek English / Français brand logo and 5 main nav pills.
  - Add search button (`⌘K`) and language dropdown / pill switcher.
- In `home.html`:
  - Add 4-pill language switch strip (Spanish, French, German, English).
  - Add hero headline with national flags: `🇬🇧 Learn English with LanGeek 🇬🇧` or `🇫🇷 Apprenez le français avec LanGeek 🇫🇷`.
  - Render the 5 flagship cards using authentic background hexes, embedded wavy vector SVGs, and responsive `hover:-translate-y-1.5` animations.
  - Add bottom app download banner with pill button.

- [ ] **Step 4: Run test to verify it passes**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_homepage_subatomic_ui_elements -v`  
Expected: PASS

- [ ] **Step 5: Commit UI tokens and template updates**

```bash
git add langeek/templates/base.html langeek/templates/home.html langeek/tests/test_replica.py
git commit -m "feat(ui): replicate LanGeek sub-atomic card design, dark mode, and language switcher"
```

---

### Task 4: English Flagship Curriculum Seeder & On-Demand Ditto Crawler

**Files:**
- Create: `langeek/crawler/seed_english.py`
- Modify: `langeek/server.py`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: Live LanGeek English endpoints (`https://langeek.co/en/...`) and structured JSON payloads.
- Produces: Populated SQLite tables for English categories, subcategories, words, grammar courses, expressions, pronunciation alphabet, and reading stories with `locale = 'en'`.

- [ ] **Step 1: Write failing test for seeded English curricula**

```python
# In langeek/tests/test_replica.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_english_flagship_curriculum_seeded -v`  
Expected: FAIL with `AssertionError: Expected at least 6 English categories, found 0`

- [ ] **Step 3: Implement `langeek/crawler/seed_english.py`**

- Seed complete CEFR English tracks:
  - Vocabulary: A1 Beginner, A2 Elementary, B1 Intermediate, B2 Upper-Intermediate, C1 Advanced, Most Common 3000 Words, Animals, Food & Dining, Travel, Work.
  - Subcategories & Words with sample sentences, phonetic transcriptions, and audio links.
  - Grammar: 11 categories (Pronouns, Nouns, Verbs, Tenses, Modals, Conditionals, Prepositions, Conjunctions, Adjectives, Adverbs, Sentence Structure) with structured lesson blocks.
  - Expressions: Top 25 everyday idioms (e.g. "Bite the bullet", "Break the ice", "Piece of cake", "Under the weather") with literal and figurative definitions.
  - Pronunciation: Full English Alphabet (A–Z) with phonetic sounds and example words.
  - Reading: Graded stories with typed `ParagraphBlock` and `PhotoBlock` segments.
- Add cache-through on-demand fallback function in `server.py` for dynamic uncached lesson queries.

- [ ] **Step 4: Execute seeder and verify test passes**

Run: `python3 langeek/crawler/seed_english.py`  
Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_english_flagship_curriculum_seeded -v`  
Expected: PASS

- [ ] **Step 5: Commit English curricula seeder**

```bash
git add langeek/crawler/seed_english.py langeek/data/langeek.db langeek/tests/test_replica.py
git commit -m "feat(curriculum): seed flagship English modules across Vocabulary, Grammar, Expressions, Pronunciation, and Reading"
```

---

### Task 5: English 5-Module Rendering Parity

**Files:**
- Modify: `langeek/server.py`
- Modify: `langeek/templates/vocab_overview.html`
- Modify: `langeek/templates/grammar_overview.html`
- Modify: `langeek/templates/expressions.html`
- Modify: `langeek/templates/pronunciation_overview.html`
- Modify: `langeek/templates/reading_overview.html`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: Partitioned records (`locale = 'en'`) from SQLite.
- Produces: Fully interactive localized pages for `/en/vocab`, `/en/grammar`, `/en/expressions`, `/en/pronunciation`, and `/en/reading`.

- [ ] **Step 1: Write failing test for all 5 English module pages**

```python
# In langeek/tests/test_replica.py
def test_english_five_modules_rendering():
    # 1. Vocabulary
    r_vocab = client.get("/en/vocab")
    assert r_vocab.status_code == 200
    assert "English Vocabulary" in r_vocab.text
    
    # 2. Grammar
    r_gram = client.get("/en/grammar")
    assert r_gram.status_code == 200
    assert "English Grammar" in r_gram.text
    
    # 3. Expressions
    r_expr = client.get("/en/expressions")
    assert r_expr.status_code == 200
    assert "English Expressions" in r_expr.text or "Idioms" in r_expr.text
    
    # 4. Pronunciation
    r_pron = client.get("/en/pronunciation")
    assert r_pron.status_code == 200
    assert "English Pronunciation" in r_pron.text
    
    # 5. Reading
    r_read = client.get("/en/reading")
    assert r_read.status_code == 200
    assert "English Reading" in r_read.text or "Reading Comprehension" in r_read.text
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_english_five_modules_rendering -v`  
Expected: FAIL

- [ ] **Step 3: Update route handlers and template localization**

- In `langeek/server.py`:
  - Parameterize queries across all 5 modules with `locale` (`WHERE locale = :db_locale`).
  - Add localized page titles, descriptions, and breadcrumbs.
- In templates (`vocab_overview.html`, `grammar_overview.html`, `expressions.html`, `pronunciation_overview.html`, `reading_overview.html`):
  - Dynamically display English or French navigation, level badges, and category descriptions based on `locale`.

- [ ] **Step 4: Run test to verify it passes**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_english_five_modules_rendering -v`  
Expected: PASS

- [ ] **Step 5: Commit module rendering updates**

```bash
git add langeek/server.py langeek/templates/*.html langeek/tests/test_replica.py
git commit -m "feat(views): enable 5-module rendering parity for both English and French"
```

---

### Task 6: Dual-Locale Instant Search (`⌘K`) & SRS Progress Persistence

**Files:**
- Modify: `langeek/server.py`
- Modify: `langeek/templates/base.html`
- Test: `langeek/tests/test_replica.py`

**Interfaces:**
- Consumes: Query string `q` and `locale` via `GET /api/search`.
- Produces: Instant JSON search results categorized into Words, Grammar, Expressions, and Stories; client-side modal in `base.html` with arrow key selection; and Leitner progress persistence via `POST /api/progress/record`.

- [ ] **Step 1: Write failing test for localized search API**

```python
# In langeek/tests/test_replica.py
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_dual_locale_search_and_progress -v`  
Expected: FAIL

- [ ] **Step 3: Implement FTS5 search endpoint and frontend modal**

- In `langeek/server.py`:
  - Update `search_fts` table to index English and French items with `locale`.
  - Implement `GET /api/search`:
    ```python
    @app.get("/api/search")
    async def global_search_api(q: str = "", locale: str = "en"):
        db_loc = "en" if locale == "en" else "fr"
        conn = get_db()
        cur = conn.cursor()
        rows = cur.execute("""
            SELECT title, description, url, category_type, locale 
            FROM search_fts 
            WHERE search_fts MATCH ? AND locale = ? 
            LIMIT 15
        """, (f"{q}*", db_loc)).fetchall()
        conn.close()
        return {"query": q, "locale": locale, "results": [dict(r) for r in rows]}
    ```
- In `base.html`:
  - Implement full-screen translucent search overlay triggered by `⌘K` or search button.
  - Add debounced input, category pill groupings, and keyboard selection.

- [ ] **Step 4: Run test to verify it passes**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py::test_dual_locale_search_and_progress -v`  
Expected: PASS

- [ ] **Step 5: Commit search and progress features**

```bash
git add langeek/server.py langeek/templates/base.html langeek/tests/test_replica.py
git commit -m "feat(search): add instant dual-locale FTS5 search modal and SRS progress tracking"
```

---

### Task 7: Comprehensive Verification & Visual Regression

**Files:**
- Modify: `langeek/tests/test_replica.py`
- Test: All tests via `pytest`
- Capture: Playwright desktop & mobile screenshots

**Interfaces:**
- Consumes: Running FastAPI server at `http://127.0.0.1:8080`.
- Produces: Full test pass report (zero regressions) and desktop/mobile screenshot artifacts.

- [ ] **Step 1: Run complete pytest suite**

Run: `PYTHONPATH=. pytest langeek/tests/test_replica.py -v`  
Expected: All tests PASS with 0 failures and 0 errors.

- [ ] **Step 2: Capture Playwright visual comparisons**

Capture:
- `http://127.0.0.1:8080/en` (Desktop & Mobile)
- `http://127.0.0.1:8080/fr-EN` (Desktop & Mobile)
- `http://127.0.0.1:8080/en/vocab`
- `http://127.0.0.1:8080/en/reading`
- `http://127.0.0.1:8080/fr-EN/reading/course/2304/animaux-de-ferme/0` (re-verifying photo illustration & 1.5 paragraph)

- [ ] **Step 3: Review visual fidelity against live reference**

Confirm card colors, SVG textures, font rendering, audio scrubber ergonomics, and dark mode styling.

- [ ] **Step 4: Final commit and push**

```bash
git add .
git commit -m "feat(platform): complete sub-atomic LanGeek multi-locale learning platform"
git push origin main
```
