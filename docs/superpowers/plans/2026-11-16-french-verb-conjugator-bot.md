# French Verb Conjugator Telegram Bot Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a production-ready French Verb Conjugator Telegram Bot in Python from scratch that replicates Lingolia Français, provides live inline typing suggestions, interactive mood navigation with auto-chunking, and deploy it to a fresh GitHub repository.

**Architecture:** A pure standard-library scraper (`urllib.request`, `http.cookiejar`, `html.parser`) fetches and parses conjugations from Lingolia Français with in-memory caching. A modern async Telegram Bot (`python-telegram-bot>=21.0`) provides message handling, live autocomplete via Telegram Inline Mode, aligned monospaced French conjugation layouts, and interactive inline keyboards.

**Tech Stack:** Python 3.9+, `python-telegram-bot>=21.0`, `python-dotenv>=1.0.0`, standard libraries (`urllib.request`, `http.cookiejar`, `html.parser`, `json`, `re`, `functools`).

**Spec:** `docs/superpowers/specs/2026-11-16-french-verb-conjugator-bot-design.md`

## Global Constraints

- Never commit `TELEGRAM_BOT_TOKEN` or `.env` to Git.
- Scraper must use only Python standard library (`urllib.request`, `http.cookiejar`, `html.parser`).
- Bot must run on `python-telegram-bot>=21.0` using modern async patterns.
- Telegram message character limit ($\le 4096$) must be respected via automatic chunking.
- Input normalization must convert curly apostrophes (`’` $\to$ `'`), lowercase, trim, and handle reflexive verbs (`se lever`, `s'appeler`).
- Live suggestions must be supported via Telegram Inline Query mode (`@verb_conjugator_bot <query>`).

---

### Task 1: Project Scaffolding & Environment Setup

**Files:**
- Create: `french_verb_conjugator_bot/.gitignore`
- Create: `french_verb_conjugator_bot/.env.example`
- Create: `french_verb_conjugator_bot/.env`
- Create: `french_verb_conjugator_bot/requirements.txt`

**Interfaces:**
- Produces: Base project structure and dependency definitions.

- [ ] **Step 1: Create project directory and `.gitignore`**
Create `french_verb_conjugator_bot/.gitignore` ensuring `.env`, virtual environments, cache files, and OS files are completely ignored:
```gitignore
.env
.venv/
venv/
env/
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.DS_Store
```

- [ ] **Step 2: Create `.env.example` and local `.env`**
Create `french_verb_conjugator_bot/.env.example`:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
```
Create `french_verb_conjugator_bot/.env` containing the user's token:
```env
TELEGRAM_BOT_TOKEN=9025532963:AAHvRxYdgzAqnPj37iPKYnRgcXSG_kfBfwY
```

- [ ] **Step 3: Create `requirements.txt`**
```text
python-telegram-bot>=21.0
python-dotenv>=1.0.0
```

- [ ] **Step 4: Verify requirements installation**
Run: `pip install -r french_verb_conjugator_bot/requirements.txt`
Expected: Successfully installed `python-telegram-bot` and `python-dotenv`.

---

### Task 2: Pure Standard Library Lingolia Scraper Engine

**Files:**
- Create: `french_verb_conjugator_bot/lingolia.py`
- Create: `french_verb_conjugator_bot/test_scraper.py`

**Interfaces:**
- Produces:
  - `class LingoliaScraper`:
    - `get_conjugation(verb: str) -> Optional[Dict[str, Any]]`
    - `autocomplete(query: str) -> List[str]`
    - `normalize_verb(verb: str) -> str`

- [ ] **Step 1: Write test cases in `test_scraper.py`**
Write tests covering:
- Regular verb (`parler`)
- Auxiliary verb (`être`)
- Reflexive verb (`s’appeler` with curly apostrophe and `se lever`)
- Invalid verb (`azertyuiop`)
- Autocomplete prefix (`parl`)

- [ ] **Step 2: Implement `normalize_verb` in `lingolia.py`**
Normalize whitespace, convert curly quotes/apostrophes `’` and `‘` to `'`, convert to lowercase.

- [ ] **Step 3: Implement session token retrieval and form POST**
Implement `_get_session_and_token()` using `http.cookiejar.CookieJar` and `urllib.request.build_opener`. Extract `REQUEST_TOKEN` from Lingolia's initial GET HTML.
Implement `_fetch_verb_html(verb: str) -> str` sending form-encoded POST data.

- [ ] **Step 4: Implement HTML parser for conjugation tables**
Implement `_parse_conjugation_html(html_content: str, verb: str)` using `html.parser.HTMLParser`:
- Validate `var VerbData = {...};`
- Parse `<div class="container_tables active">`
- Extract non-conjugated forms: Infinitif, Participe présent, Participe passé, Auxiliaire.
- Extract moods: Indicatif, Conditionnel, Subjonctif, Impératif.
- Extract tenses and `(subject, verb_form)` pairs.

- [ ] **Step 5: Implement autocomplete endpoint**
Implement `autocomplete(query: str) -> List[str]` sending POST with `action=fmd&id=104&lang=francais` and `X-Requested-With: XMLHttpRequest`.

- [ ] **Step 6: Run `test_scraper.py`**
Run: `python3 -m unittest french_verb_conjugator_bot/test_scraper.py -v`
Expected: All tests pass.

---

### Task 3: Telegram Bot Engine & Interactive Visual Layout

**Files:**
- Create: `french_verb_conjugator_bot/bot.py`

**Interfaces:**
- Consumes: `LingoliaScraper` from `lingolia.py`.
- Produces: Running Telegram bot application with command and message handlers.

- [ ] **Step 1: Implement HTML message formatting & monospaced column alignment**
Format non-conjugated forms, moods, and tenses with clean monospaced alignments (`<code>je          parle</code>`), emoji headers, and dividers.

- [ ] **Step 2: Implement inline keyboard builder**
Build keyboards with active state badges:
- `[ ✅ Indicatif ]` `[ 🔸 Conditionnel ]`
- `[ 🔸 Subjonctif ]` `[ 🔸 Impératif ]`
- `[ 📚 Tout afficher ]` `[ 🌐 Lingolia ]`

- [ ] **Step 3: Implement safe chunking algorithm**
Ensure that when generating "Tout afficher", if the text exceeds 3,800 characters, it cleanly splits along mood boundaries into Part 1 and Part 2 without breaking HTML tags.

- [ ] **Step 4: Implement `/start`, `/help`, and `/conj` handlers**
Welcome user, explain inline mode, handle `/conj <verb>`, and handle plain text French verb inputs.

- [ ] **Step 5: Implement fallback suggestion buttons**
When `get_conjugation(verb)` returns `None`, query `autocomplete(verb)`.
If suggestions exist, return:
`⚠️ Verbe non trouvé. Vouliez-vous dire :` with inline buttons for each candidate (`[ parler ]`, `[ partir ]`, etc.).

---

### Task 4: Live Inline Mode & Callback Navigation

**Files:**
- Modify: `french_verb_conjugator_bot/bot.py`

**Interfaces:**
- Produces:
  - `callback_query_handler` for instant tab switching (`tab:<verb>:<mood>`).
  - `inline_query_handler` for live autocomplete typing suggestions (`@verb_conjugator_bot <query>`).

- [ ] **Step 1: Implement callback query handler**
When a user clicks a mood tab button:
1. Extract verb and target mood from callback data.
2. Retrieve verb data from scraper's in-memory LRU cache.
3. Edit message text and update keyboard with active tab indicator via `query.edit_message_text`.
4. Answer callback query with `await query.answer()`.

- [ ] **Step 2: Implement inline query handler**
When user types `@verb_conjugator_bot <query>`:
1. Query `scraper.autocomplete(query)`.
2. For top results, create `InlineQueryResultArticle` with:
   - Title: Infinitive verb.
   - Description: "Appuyez pour voir la conjugaison complète".
   - Input message content: Formatted Indicative view with full interactive inline keyboard.
3. Call `await update.inline_query.answer(results, cache_time=300)`.

---

### Task 5: Documentation & BotFather Configuration Guide

**Files:**
- Create: `french_verb_conjugator_bot/README.md`

- [ ] **Step 1: Write `README.md`**
Include:
- Features overview.
- Requirements and installation instructions.
- Environment variables setup (`TELEGRAM_BOT_TOKEN`).
- Local run instructions (`python3 bot.py`).
- Enabling Telegram Inline Mode via `@BotFather` (`/setinline` and `/setinlineplaceholder`).
- Deployment guides (Docker, Render, Railway).

---

### Task 6: Git Initialization & GitHub Deployment

**Files:**
- Repository: `french_verb_conjugator_bot`

- [ ] **Step 1: Initialize Git and verify `.gitignore`**
Run `git init` inside `french_verb_conjugator_bot`.
Verify `git status` does NOT show `.env`.

- [ ] **Step 2: Initial Commit**
Commit all project files (`.gitignore`, `.env.example`, `requirements.txt`, `lingolia.py`, `bot.py`, `test_scraper.py`, `README.md`).

- [ ] **Step 3: Create GitHub remote repository & push**
Run: `gh repo create naxer-12/french-verb-conjugator-bot --public --source=. --remote=origin --push`
Verify repo is online at `https://github.com/naxer-12/french-verb-conjugator-bot`.

- [ ] **Step 4: Final verification and live bot run check**
Test bot launch locally to confirm Telegram connection and polling readiness.
