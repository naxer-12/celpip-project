# Design Specification: French Verb Conjugator Telegram Bot

**Date:** 2026-11-16  
**Author:** Antigravity / DeepMind Team  
**Status:** Approved  

---

## 1. Overview & Goals
Build a production-grade Telegram bot in Python from scratch that replicates the full conjugation feature set of [Lingolia Français Conjugator](https://francais.lingolia.com/en/grammar/conjugator).

The bot provides:
1. Instant French verb lookups directly from plain text chat messages and commands (`/start`, `/help`, `/conj <verb>`).
2. Live "as-you-type" infinitive autocomplete via Telegram **Inline Mode** (`@verb_conjugator_bot <query>`).
3. Comprehensive coverage:
   - **Formes non conjuguées**: Infinitif, Participe passé, Participe présent, Auxiliaire.
   - **All 4 Moods & Tenses**: Indicatif, Conditionnel, Subjonctif, Impératif.
4. Rich interactive layout using Telegram HTML formatting (aligned monospaced columns, emoji hierarchy) with inline keyboard tab switching.
5. Auto-chunking for the "View All Moods" option to stay strictly within Telegram's 4,096-character limit.
6. In-memory LRU caching for instant tab switching with $<1$ ms latency.
7. Robust input normalization (handling curly apostrophes, reflexive pronouns, trimming).
8. Fallback suggestions powered by Lingolia's autocomplete endpoint when invalid or inflected verbs are entered.
9. Git repository initialization, automated testing suite, and deployment to GitHub (`naxer-12/french-verb-conjugator-bot`) with strict security practices (`TELEGRAM_BOT_TOKEN` never committed).

---

## 2. System Architecture

```
User in Telegram Chat ───────────► bot.py (python-telegram-bot v21+)
 (Plain text, /conj, Inline)          │
                                      ▼
                             Input Normalizer
                                      │
                                      ▼
                             In-Memory LRU Cache
                                ├── (Cache Hit) ──► Instant Response
                                └── (Cache Miss) ─► lingolia.py (LingoliaScraper)
                                                         │
                                        ┌────────────────┴────────────────┐
                                        ▼                                 ▼
                                 Lingolia Form POST            Lingolia Autocomplete
                              (REQUEST_TOKEN + Cookie)         (fmd XHR endpoint)
                                        │                                 │
                                        ▼                                 ▼
                                HTMLParser Engine               Candidate List [JSON]
                                        │                                 │
                                        ▼                                 ▼
                             Conjugation Data Model              Suggestions Buttons
                                        │
                                        ▼
                             HTML & Keyboard Formatter
                                        │
                                        ▼
                             Chunker (Telegram ≤4096)
                                        │
                                        ▼
                               Telegram Message / Edit
```

---

## 3. Detailed Component Specifications

### 3.1 Scraping & Extraction Engine (`lingolia.py`)
* **Standard Library Dependencies**: `urllib.request`, `urllib.parse`, `http.cookiejar`, `html.parser`, `re`, `json`, `functools`. No external scraping libraries (pure stdlib).
* **Session Lifecycle**:
  * Persistent `CookieJar` attached to `urllib.request.build_opener`.
  * `_get_request_token()`: Fetches `GET https://francais.lingolia.com/en/grammar/conjugator` and extracts `<input type="hidden" name="REQUEST_TOKEN" value="([a-f0-9]+)">`.
* **Form Submission (`POST`)**:
  * URL: `https://francais.lingolia.com/en/grammar/conjugator`
  * Form parameters:
    * `FORM_SUBMIT=""`
    * `REQUEST_TOKEN=<token>`
    * `search_verb[input]=<verb>`
    * `search_verb[force]=""`
    * `verb=""`
    * `search_verb[language]="francais"`
  * User-Agent and standard browser headers included.
* **HTML Parsing & Extraction**:
  * Validation: Searches for `var VerbData = ({.*?});`. If `{}` or missing, triggers fallback.
  * Parser: `LingoliaHTMLParser(HTMLParser)`:
    * Locates `<div class="container_tables active">`.
    * Extracts non-conjugated forms:
      * Infinitif
      * Participe présent
      * Participe passé
      * Auxiliaire (avoir / être)
    * Scans `<table class="table_verbs">`:
      * `<h3>` $\to$ Mood (Indicatif, Conditionnel, Subjonctif, Impératif).
      * `<th colspan="2">` $\to$ Tense (Présent, Imparfait, Passé composé, etc.).
      * Rows: `td.lia_subject` (pronoun) and `td.lia_verb` (verb form).
* **Autocomplete API**:
  * `POST https://francais.lingolia.com/en/grammar/conjugator`
  * Headers: `X-Requested-With: XMLHttpRequest`, `Content-Type: application/x-www-form-urlencoded`.
  * Body: `verb=<query>&action=fmd&id=104&lang=francais&REQUEST_TOKEN=<token>`.
  * Response: JSON list of matching infinitives (e.g., `["parler", "partir", "parvenir"]`).
* **Caching**:
  * `@functools.lru_cache(maxsize=512)` on parsed verb records and autocomplete results.

### 3.2 Telegram Bot Engine (`bot.py`)
* **Dependencies**: `python-telegram-bot>=21.0`, `python-dotenv>=1.0.0`.
* **Normalizer**:
  * Strips leading/trailing punctuation and whitespace.
  * Replaces curly quotes `’`, `‘` with standard single quote `'`.
  * Normalizes reflexive prefixes: `se lever` $\to$ `se lever`, `s’appeler` $\to$ `s'appeler`.
  * Lowercases query.
* **Handlers**:
  1. `start_command` & `help_command`: Onboarding guide and examples.
  2. `conj_command`: `/conj <verb>` triggers search.
  3. `message_handler`: Intercepts plain text French verbs and replies with conjugation.
  4. `callback_query_handler`: Handles mood switching (`tab:verb:mood`), dynamically updating the message with `edit_message_text`.
  5. `inline_query_handler`: Implements live typing suggestions for `@verb_conjugator_bot <query>`, returning instant interactive previews.
* **Visual Presentation**:
  * Uses Telegram HTML formatting.
  * Monospaced code blocks (`<code>je          parle</code>`) ensure pronouns and verb stems align vertically.
  * Inline buttons with active mood markers:
    * `[ ✅ Indicatif ]` `[ 🔸 Conditionnel ]`
    * `[ 🔸 Subjonctif ]` `[ 🔸 Impératif ]`
    * `[ 📚 Tout afficher ]` `[ 🌐 Ouvrir sur Lingolia ]`
* **Safe Chunking**:
  * For "Tout afficher" (View All Moods), constructs sections sequentially.
  * If the assembled HTML exceeds 3,800 characters, automatically partitions across multiple sequential messages without breaking HTML tags.

---

## 4. Test Strategy (`test_scraper.py`)
Automated tests using `unittest`:
1. `test_regular_verb`: Queries `parler`, verifies non-conjugated forms and all 4 moods.
2. `test_auxiliary_and_irregular_verbs`: Tests `être`, `avoir`, `aller`, `faire`.
3. `test_reflexive_verbs`: Tests `se lever` and `s’appeler` (including curly apostrophe normalization).
4. `test_invalid_verb_detection`: Tests gibberish (`azertyuiop`) to ensure `None` is returned cleanly without exceptions.
5. `test_autocomplete`: Tests prefix queries like `parl` to verify candidates like `parler` are returned.

---

## 5. Security & Deployment

1. **Security**:
   - `.env` excluded in `.gitignore`.
   - `.env.example` committed with dummy placeholder `TELEGRAM_BOT_TOKEN=your_token_here`.
   - Token loaded securely via `python-dotenv` and `os.getenv("TELEGRAM_BOT_TOKEN")`.
2. **Repository Setup**:
   - Directory: `./french_verb_conjugator_bot/`
   - Git init, branch `main`.
   - GitHub repo: `naxer-12/french-verb-conjugator-bot` via `gh repo create`.
3. **Deployment Options Documented**:
   - Local execution via `python3 bot.py`.
   - 24/7 Cloud deployment options (Docker / Render / Railway / systemd).
   - BotFather setup guide for inline queries (`/setinline`).
