# Unified LanGeek Multi-Locale Platform: Architectural Design Specification

**Date:** 2026-11-14  
**Author:** Antigravity Engineering  
**Scope:** Unified Multi-Locale Platform (`/en` and `/fr-EN`), sub-atomic UI/UX mirroring of live `https://langeek.co/en/`, and elevation of the 5 core learning modules (Vocabulary, Grammar, Expressions, Pronunciation, Reading).

---

## 1. Executive Summary & Goals

This specification defines the complete architectural overhaul of the LanGeek replica into a production-grade, multi-locale learning platform. The system mirrors `https://langeek.co/en/` down to the sub-atomic details—tactile typography, wavy card textures, responsive micro-interactions, dark/light mode, synchronized audio dock, and Leitner spaced-repetition—while uniting English (`/en/*`) and French (`/fr-EN/*`) under a shared, high-performance Ditto architecture.

### Primary Goals:
1. **Multi-Locale Core:** Establish unified routing for English (`/en`) and French (`/fr-EN`) with path-preserving locale switching across all 5 modules.
2. **Sub-Atomic UI/UX:** Replicate LanGeek's 5 iconic card styles (sky blue, warm peach, mint aquamarine, buttercup yellow, terracotta salmon) with authentic SVG patterns, rounded-3xl radii, and hover physics.
3. **5-Module Parity:** Deliver full functional depth across Vocabulary, Grammar, Expressions, Pronunciation, and Reading for both languages.
4. **Hybrid Seeding & On-Demand Caching:** Pre-seed flagship curricula into local SQLite and seamlessly fetch uncached courses on demand with automatic persistence.
5. **Zero Layout Shift & High Performance:** Ensure sub-5ms local page delivery, zero layout shift (CLS = 0), zero flash of unstyled theme (FOUT), and low-latency audio streaming.

---

## 2. Multi-Locale Architecture & Routing Pipeline

### 2.1 Canonical Routes

```
/                                 --> Detects stored locale cookie or header, redirects to /en or /fr-EN
/en                               --> English Learning Home
/en/vocab                         --> English Vocabulary Overview (A1-C2, Topics, Frequency)
/en/vocab/category/{id}/{slug}    --> Category Lessons & Subcategories Grid
/en/vocab/subcategory/{id}/learn  --> Interactive Studio (Flashcards, Quiz, Dictation)
/en/vocab/subcategory/{id}/words  --> Full Wordlist & Audio Dictionary
/en/grammar                       --> English Grammar Hub (11 Core Modules)
/en/grammar/{id}/{slug}           --> Grammar Category Courses
/en/grammar/course/{id}/{slug}    --> Formatted Interactive Grammar Lesson
/en/expressions                   --> English Idioms, Sayings & Phrasal Verbs
/en/pronunciation                 --> English Pronunciation & Phonetics Hub
/en/pronunciation/101/alphabet    --> Interactive English Alphabet Hub (A-Z)
/en/reading                       --> Graded English Reading Stories Hub
/en/reading/course/{id}/{slug}/{segment} --> Multi-Segment Reader with Synced Audio Dock
/en/plans                         --> LanGeek Premium Showcase
/en/mobile-app                    --> iOS & Android Showcase
/en/contact-us                    --> Contact & Feedback
/en/sign-in                       --> Auth & User Profile Simulator

/fr-EN/*                          --> Identical parallel structure for French
```

### 2.2 Aliases & Redirects
* `/en/` and `/en-US` $\rightarrow$ `/en` (307 Redirect)
* `/fr` and `/fr/` $\rightarrow$ `/fr-EN` (307 Redirect)
* `/es` $\rightarrow$ `/es-EN` (Stub redirect to `/en` with badge)
* `/de` $\rightarrow$ `/de-EN` (Stub redirect to `/en` with badge)

### 2.3 Route Parameterization & Context Middleware
All localized route handlers utilize a shared dependency `get_locale_context`:
```python
def get_locale_context(locale: str = "en") -> dict:
    if locale not in ("en", "fr-EN"):
        locale = "en"
    return {
        "locale": locale,
        "lang_code": "en" if locale == "en" else "fr",
        "locale_name": "English" if locale == "en" else "Français",
        "flag": "gb" if locale == "en" else "fr",
        "switch_urls": {
            "en": "/en",
            "fr-EN": "/fr-EN"
        }
    }
```
When switching locales, the active subpath is retained (e.g., `/en/reading` $\leftrightarrow$ `/fr-EN/reading`).

---

## 3. Data Models & SQLite Schema Migration

### 3.1 Schema Partitioning
The database `langeek/data/langeek.db` is partitioned by a `locale` column (`TEXT NOT NULL DEFAULT 'fr'`) across all content tables:

1. **`categories` & `subcategories` (Vocabulary):**
   - Added column: `locale TEXT NOT NULL DEFAULT 'fr'`
   - Index: `idx_categories_locale ON categories(locale, position)`
   - Index: `idx_subcategories_cat_loc ON subcategories(category_id, locale)`

2. **`words` & `examples`:**
   - Word records store the lemma, translation, phonetic spelling, part of speech, and audio URL.
   - Example sentences store the localized sentence, translation, and audio URL.

3. **`grammar_categories` & `grammar_courses`:**
   - Added column: `locale TEXT NOT NULL DEFAULT 'fr'`
   - Index: `idx_grammar_courses_loc ON grammar_courses(category_id, locale)`

4. **`expressions`:**
   - Schema: `id, locale, category, phrase, literal_translation, meaning, examples_json, audio_url, position`

5. **`pronunciation_courses`:**
   - Added column: `locale TEXT NOT NULL DEFAULT 'fr'`
   - Contains letter guides, IPA sound representations, and sample word matrices.

6. **`reading_collections`, `reading_stories`, `reading_segments`:**
   - Added column: `locale TEXT NOT NULL DEFAULT 'fr'`
   - Segment `content_json` stores typed polymorphic blocks:
     - `{"type": "paragraph", "fr": "...", "en": "...", "audio": "...", "position": N}`
     - `{"type": "photo", "photo": "...", "photo_thumbnail": "...", "aspect_ratio": 1.25, "position": N}`

7. **`user_progress` (Unified Spaced Repetition):**
   - Schema: `id, user_id, locale, item_type, item_id, srs_box, state, last_reviewed, next_review, correct_count, incorrect_count`
   - Enables independent Leitner tracking for English and French study.

8. **`search_fts` (Full-Text Search):**
   - FTS5 virtual table indexing `title, description, content, url, locale`.

---

## 4. Hybrid Ditto Crawler & Caching Engine

Following the *Ditto Architecture* from `/replicating-web-apps`:

### 4.1 Upfront Flagship Seeding
A specialized seed script (`langeek/crawler/seed_english.py`) extracts flagship English modules from `https://langeek.co/en/`:
* **Vocabulary:**
  - CEFR A1 (Beginner Essentials), A2 (Elementary), B1 (Intermediate), B2 (Upper-Intermediate), C1/C2 (Advanced).
  - Top 1000/3000 high-frequency words.
  - Flagship topic packs: Animals, Daily Routine, Food & Dining, Travel, Work & Career.
* **Grammar:**
  - 11 core categories (Pronouns, Nouns, Verbs, Tenses, Modals, Conditionals, Prepositions).
* **Expressions:**
  - Flagship collections: Everyday Idioms, Business Expressions, Animal Metaphors, Food Expressions.
* **Pronunciation:**
  - Complete A–Z English Alphabet hub with phonetic sound clips and example words.
* **Reading:**
  - Flagship graded stories with verified `ParagraphBlock` and `PhotoBlock` segments.

### 4.2 On-Demand Cache-Through Fallback
When a visitor accesses an uncached English or French lesson:
1. Route handler queries SQLite.
2. If missing, it fetches the upstream URL from `https://langeek.co` with browser headers.
3. Extracts structured JSON payload from `__NEXT_DATA__`.
4. Writes records to SQLite.
5. Renders immediately using the native local template.

### 4.3 Binary Media Proxy (`/media-proxy`)
All audio streams, illustrations, and icons flow through `/media-proxy`:
* Verifies magic bytes (`\xff\xd8\xff` for JPEG, `\x89PNG` for PNG, `ID3` for MP3).
* Enforces correct MIME types (`audio/mpeg`, `image/png`, `image/jpeg`, `image/svg+xml`).
* Caches binary files locally to disk, ensuring 100% offline playback resilience.

---

## 5. Sub-Atomic UI/UX System & Design Tokens

### 5.1 The 5 Iconic Module Cards
Each module card on the homepage and hub pages replicates live LanGeek's distinct chromatic and tactile identity:

| Module | Background Color | Accent Hex | Vector Texture Pattern | Emblem Icon |
|:---|:---|:---|:---|:---|
| **Vocabulary** | Sky Blue | `#68B4D8` | Topological wave contour lines | Theater Masks (`🎭`) |
| **Expressions** | Warm Peach | `#F8A06E` | Dot-matrix rays & burst grid | Radiant Lightbulb (`💡`) |
| **Reading** | Mint Aquamarine | `#64CEB2` | Concentric circular arc ripples | Open Document (`📄`) |
| **Pronunciation** | Buttercup Yellow | `#F8D56F` | Horizontal chevron waves | Speaking Silhouette (`🗣️`) |
| **Grammar** | Terracotta Salmon | `#E77A6C` | Organic botanical leaf branches | Open Textbook (`📖`) |

* Geometry: `rounded-3xl` (24px corner radius), border-0, soft ambient shadow.
* Micro-interaction: Hover transforms `transform -translate-y-1.5 duration-300`, elevating cards smoothly.

### 5.2 Typography System
* **Primary Sans:** `Noto Sans`, system font stack for all UI labels, navigation links, and controls.
* **Editorial Reading Serif:** `Fraunces` / `Merriweather` / Georgia for reading story paragraphs (`font-reading-regular`, `font-reading-bold-italic`).
* **Technical Mono:** Monospace numerals for audio duration, speed indicators (`1.0x`), and phonetic notation (`/ˈæpl/`).

### 5.3 Theme System (Dark / Light)
* **Light Mode:** Canvas `#FFFFFF`, slate backgrounds `#F8FAFC` and `#F1F5F9`, high-contrast text `#0F172A`.
* **Dark Mode:** Canvas `#0B1120`, card backgrounds `#1E293B`, subtle borders `#334155`, text `#F8FAFC`.
* **Zero FOUT:** Inline script in `<head>` applies `.dark` before first paint from `localStorage.getItem('theme')`.

### 5.4 Persistent Audio Dock
Docked fixed at the viewport bottom in Reading and Pronunciation modules:
* Left: Thumbnail avatar, chapter number, segment title, and collection link.
* Center: Playback speed pill (`0.75x`, `1.0x`, `1.25x`, `1.5x`), skip $-10\text{s}$, central Royal Blue circular play/pause disc (`#1554AD`), skip $+10\text{s}$, smooth dragging scrubber bar with elapsed/total timestamps.
* Right: Volume slider, Safe Eyes sepia toggle, `文A` translation toggle, and fullscreen trigger.

### 5.5 Global Search Modal (`⌘K`)
* Instant floating overlay triggered by search icon or `⌘K` / `Ctrl+K`.
* Real-time autocomplete backed by SQLite FTS5.
* Categorized results (Vocabulary, Grammar, Expressions, Reading).
* Arrow key navigation with instant enter-to-navigate.

---

## 6. Detailed Module Specifications

### 6.1 Vocabulary (`/{locale}/vocab`)
* **Hub:** Level filters (A1 to C2), Topic packs, Frequency lists.
* **Interactive Studio (`/learn`):**
  - **Flashcards:** 3D flip card, audio trigger, phonetic guide, and 4-grade Leitner buttons (Again, Hard, Good, Easy).
  - **Quiz:** 4-choice interactive question with instant sound/color feedback.
  - **Spelling Dictation:** Audio playback with on-screen accent toolbar and live validation.
  - **Wordlist Dictionary:** Sortable table of all words, definitions, and audio.

### 6.2 Grammar (`/{locale}/grammar`)
* **Hub:** 11 core categories.
* **Course Lesson:**
  - Highlighting syntax formulas (`Subject + Auxiliary + Verb`).
  - Example tables with audio triggers.
  - Interactive "Test Your Knowledge" comprehension cards with instant answers.

### 6.3 Expressions (`/{locale}/expressions`)
* **Hub:** Thematic idiom categories.
* **Idiom Cards:**
  - Target phrase in bold.
  - Literal translation box (cultural meaning).
  - Figurative explanation box.
  - Conversational example dialogue with native audio.

### 6.4 Pronunciation (`/{locale}/pronunciation`)
* **Hub:** The Alphabet, Vowels, Consonants, Liaisons/Connected Speech.
* **Alphabet Hub (`/101/alphabet`):**
  - 26 interactive letter cards (A–Z).
  - Audio playback for isolated letter and letter in sample words.
  - IPA phonetic transcription.

### 6.5 Reading (`/{locale}/reading`)
* **Hub:** Graded story collections.
* **Story Reader (`/course/{id}/{slug}/{segment}`):**
  - Segment stepper with round avatar thumbnails.
  - Polymorphic blocks:
    - `ParagraphBlock`: Sequential black square badges (`1.1`, `1.2`...), serif text, collapsible translation box, and paragraph audio button.
    - `PhotoBlock`: Centered illustration cards without paragraph badges.
  - Bottom audio dock synchronized with reading paragraphs, auto-highlighting the active card as audio plays.

---

## 7. Verification & Testing Strategy

### 7.1 Automated Pytest Suite (`langeek/tests/test_replica.py`)
1. **Locale & Routing Tests:** Verifies `/en`, `/fr-EN`, redirects, and path-preserving switching.
2. **5-Module English Tests:** Verifies status 200, template rendering, and core data for Vocabulary, Grammar, Expressions, Pronunciation, and Reading.
3. **French Zero-Regression Tests:** Confirms 100% of existing French routes, audio, and photo blocks remain intact.
4. **Search API Tests:** Validates `/api/search` with FTS5 queries in $<5\text{ms}$.
5. **SRS Progress Tests:** Validates Leitner box updates in `user_progress`.

### 7.2 Visual Regression (Playwright)
* Desktop ($1280\times 800$) and mobile ($375\times 667$) captures compared against reference screenshots from `https://langeek.co/`.
* Confirms card colors, SVG textures, font rendering, audio scrubber ergonomics, and dark mode styling.

---

## 8. Success Criteria & Quality Gates

* [x] Both English (`/en/*`) and French (`/fr-EN/*`) accessible with seamless locale switching.
* [x] All 5 modules operational with authentic UI/UX and audio playback.
* [x] Polymorphic `PhotoBlock` and sequential `ParagraphBlock` rendering active across all reading stories.
* [x] Dark/Light theme switch with persistent `localStorage` and zero FOUT.
* [x] Instant `⌘K` global search across both languages.
* [x] 100% passing automated test suite (`pytest`).
