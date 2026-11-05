# CELTESTPIP Full-Depth Crawler & Offline Replica Specification

- **Date:** 2026-11-05
- **Status:** Approved
- **Target Site:** `https://www.celtestpip.com`
- **Output Directory:** `celtestpip/`

---

## 1. Overview & Objectives

The goal is to crawl, extract, and replicate `https://www.celtestpip.com` across all depths into a self-contained, 100% offline-capable local web application.

### Key Deliverables
1. **Asynchronous Crawler & RSC Parser**: Decodes Next.js App Router React Server Component (`RSC`) payloads to extract structured exam data, questions, answer keys, explanations, transcripts, and media links without relying on brittle browser automation.
2. **Offline Media Mirror**: Downloads all audio MP3s and scene images from Vercel blob storage into a structured local directory with checksum deduplication.
3. **Structured SQLite Database**: Stores all 60 mock exams, 1,200 exam parts, 4,000+ questions, question bank categories, CLB/CRS calculator formulas, and search indexes (FTS5).
4. **Standalone Web Application (FastAPI & Vanilla JS)**: A responsive, dependency-free local web application matching the authentic visual identity of `celtestpip.com`, featuring an interactive CELPIP exam simulator with audio player, countdown timers, instant answer checking, score analysis, and estimated CLB level calculation.

---

## 2. Target Site Architecture & Extraction Strategy

- **Platform**: Next.js App Router running on Vercel behind Cloudflare.
- **RSC Data Stream**: The target exposes full component flight data when sent the `RSC: 1` request header.
- **Data Completeness**: Even for unauthenticated visitors (`userId: null`, `isPremium: false`), the server component payload delivers:
  - All question titles, text, priority, and question IDs.
  - All option choices (`option1` through `option8`).
  - Correct answer keys and full explanations.
  - Multi-part listening audio URLs (`audio`, `audio2`, `audio3`) on Vercel blob storage.
  - Conversation and lecture transcripts (`transcript`, `transcript2`, `transcript3`).
  - Question-level audio URLs for spoken prompts.
  - Scene and question images (`image`).
  - Audio timestamp synchronization data (`audioTimings`).
- **Scope**:
  - 60 full mock exams (`exam1` through `exam60`).
  - 20 parts per exam:
    - Listening: Parts 1–6
    - Reading: Parts 1–4
    - Writing: Tasks 1–2
    - Speaking: Tasks 1–8
  - 373 public pages listed in `sitemap.xml` (Question bank, guides, CLB and CRS calculators).

---

## 3. Directory Layout

The application will be organized in a modular `celtestpip/` project folder:

```text
celtestpip/
├── crawler/
│   ├── __init__.py
│   ├── rsc_parser.py         # Extracts questions, transcripts, options, and media from RSC flight data
│   ├── crawl_exams.py        # Asynchronously iterates exam1..exam60 x part1..part20 with checkpointing
│   ├── crawl_content.py      # Sitemap scraper for question bank, guides, tools
│   ├── download_media.py     # Concurrent MP3 and image downloader with deduplication
│   └── run_crawler.py        # Master pipeline CLI
├── data/
│   ├── raw/
│   │   ├── exams/            # Individual exam part JSON files (checkpoint storage)
│   │   ├── pages/            # Scraped content pages and sitemap manifest
│   │   └── tools/            # Scraped CLB/CRS formulas and tables
│   ├── media/
│   │   ├── audio/            # Downloaded listening/speaking MP3 files
│   │   ├── images/           # Downloaded question/scene images
│   │   └── media_map.json    # Map from remote Vercel URLs to local filenames
│   └── celtestpip.db         # Indexed SQLite database
├── server/
│   ├── __init__.py
│   ├── app.py                # FastAPI routes (API and static routes)
│   ├── database.py           # SQLite query helpers and attempt recorder
│   └── scoring.py            # CELPIP raw-to-CLB score converter
├── static/
│   ├── css/
│   │   └── style.css         # Styling matching celtestpip (#f1f2ee palette, Space Grotesk)
│   ├── js/
│   │   ├── exam_runner.js    # Interactive exam simulator, audio sync, timer, scoring
│   │   ├── calculator.js     # Interactive CLB & CRS points calculators
│   │   └── app.js            # Dashboard, navigation, and study mode controls
│   └── img/
│       └── logo.png          # App branding & iconography
├── build_db.py               # Generates celtestpip.db from data/raw/
├── server.py                 # Main entrypoint: uvicorn server running on http://localhost:8000
├── requirements.txt          # Python requirements: fastapi, uvicorn, httpx, aiofiles
├── tests/
│   ├── test_parser.py        # Unit tests for RSC extraction
│   ├── test_db.py            # Unit tests for SQLite schema and queries
│   └── test_api.py           # End-to-end integration tests for FastAPI endpoints
└── README.md                 # Full documentation
```

---

## 4. Subsystems Specification

### 4.1. Crawler & Extractor Subsystem

#### `rsc_parser.py`
- Parses Next.js RSC flight protocol.
- Identifies JSON dictionary payloads containing:
  - `practice`: Practice ID, name, section texts, transcripts, audio URLs, scene images.
  - `part`: Skill type, part name, slug, time limits.
  - `questions`: List of question objects with `question`, `option1`..`option8`, `answer`, `explanation`, `audio`, `image`.
- Normalizes disparate skill types into unified schema.

#### `crawl_exams.py`
- Target URL pattern: `https://www.celtestpip.com/exams/{exam_id}/{part_id}`.
- Exhaustive loop: `exam_id` in `exam1`..`exam60`, `part_id` in `part1`..`part20`.
- Rate limiting: Semaphore-controlled concurrency (5 workers) with exponential backoff on HTTP 429/503.
- Checkpointing: Before querying, checks if `data/raw/exams/{exam_id}_{part_id}.json` exists. If present, skips network call.

#### `download_media.py`
- Collects all unique URLs ending in `.mp3`, `.wav`, `.jpg`, `.jpeg`, `.png`, `.webp` from `data/raw/`.
- Computes SHA256 or safe filename from URL slug.
- Saves audio to `data/media/audio/{filename}` and images to `data/media/images/{filename}`.
- Outputs `data/media/media_map.json` mapping `remote_url -> local_relative_path`.

---

### 4.2. Database Schema (`data/celtestpip.db`)

Built via `build_db.py`:

```sql
CREATE TABLE IF NOT EXISTS exams (
    id TEXT PRIMARY KEY,               -- e.g. 'exam1'
    name TEXT NOT NULL,                -- e.g. 'Exam 1'
    total_parts INTEGER DEFAULT 20,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS exam_parts (
    id TEXT PRIMARY KEY,               -- e.g. 'exam1_part1'
    exam_id TEXT NOT NULL REFERENCES exams(id),
    part_number INTEGER NOT NULL,      -- 1 to 20
    skill TEXT NOT NULL,               -- 'LISTENING', 'READING', 'WRITING', 'SPEAKING'
    part_name TEXT NOT NULL,           -- e.g. 'Listening to Problem Solving'
    part_slug TEXT,                    -- e.g. 'L1'
    time_limit INTEGER DEFAULT 60,     -- duration in seconds
    instructions TEXT,
    text_content TEXT,
    audio_url TEXT,                    -- local path: /media/audio/...
    audio2_url TEXT,
    audio3_url TEXT,
    image_url TEXT,                    -- local path: /media/images/...
    transcript TEXT,
    transcript2 TEXT,
    transcript3 TEXT,
    audio_timings TEXT                 -- JSON string
);

CREATE TABLE IF NOT EXISTS questions (
    id TEXT PRIMARY KEY,
    part_id TEXT NOT NULL REFERENCES exam_parts(id),
    question_number INTEGER NOT NULL,
    priority INTEGER,
    question_text TEXT NOT NULL,
    audio_url TEXT,                    -- prompt audio
    options_json TEXT NOT NULL,        -- JSON array of choices
    correct_answer TEXT NOT NULL,      -- e.g. '1', '2', '3', '4'
    explanation TEXT,
    section INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS articles (
    slug TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    content_html TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS user_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_id TEXT NOT NULL,
    part_number INTEGER NOT NULL,
    score INTEGER NOT NULL,
    total_questions INTEGER NOT NULL,
    clb_estimate INTEGER,
    answers_json TEXT NOT NULL,
    completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Full text search index
CREATE VIRTUAL TABLE IF NOT EXISTS fts_questions USING fts5(
    part_id UNINDEXED,
    question_text,
    options_json,
    explanation
);
```

---

### 4.3. FastAPI Server & API Specification

Root runner: `server.py` launching `server.app:app` via Uvicorn on port 8000.

#### Endpoints
- `GET /` — Home dashboard displaying all 60 mock exams, skills overview, and user progress.
- `GET /exams` — Exam directory with filtering and status.
- `GET /exams/{exam_id}` — Exam overview page listing parts 1–20.
- `GET /exams/{exam_id}/part/{part_number}` — Full interactive exam interface for that part.
- `GET /questions` — Categorized question bank for focused practice.
- `GET /tools/clb-calculator` — Interactive Canadian Language Benchmark score calculator.
- `GET /tools/crs-calculator` — Interactive Express Entry CRS point simulator.
- `GET /learn` — Study guides and strategy articles.
- `GET /api/exams` — JSON list of all exams and completion statistics.
- `GET /api/exams/{exam_id}/part/{part_number}` — JSON payload for test runner (questions, options, media, transcript).
- `POST /api/attempts` — Saves user test submission, returns score, accuracy, and estimated CLB band.
- `GET /api/search?q={query}` — Full-text search across all questions and explanations.
- `GET /media/{type}/{filename}` — Serves offline audio and image files.

---

### 4.4. Frontend & Interactive Exam Simulator

#### Design System
- Neutral warm background: `#f1f2ee`
- Card background: `#ffffff` with subtle border `#e2e3de`
- Primary brand accent: Deep navy `#101828` and active teal/blue `#0284c7`
- Typography: Clean sans-serif and Space Grotesk
- Fully responsive across desktop, laptop, and tablet viewports.

#### Simulator Logic (`exam_runner.js`)
- **Timer Engine**: Accurate countdown timer per part, matching official CELPIP time allowances.
- **Audio Synchronization**: Automatically plays listening section audios, supports replay in practice mode, and tracks completion.
- **Answer Selection**: Radio-button selection with visual selection feedback.
- **Dual Mode**:
  - **Timed Exam Mode**: No feedback until "Submit Part", mimicking the authentic test room experience.
  - **Study Practice Mode**: Toggle "Show Answer" to instantly reveal the correct option, detailed official explanation, and full transcript.
- **Score Calculation & CLB Mapping**:
  - Automatically scores multiple-choice sections.
  - Maps Listening (raw 0–38) and Reading (raw 0–38) scores directly to CLB 4 through CLB 12 using official IRCC conversion tables.
  - Saves completed attempts to local SQLite database via `/api/attempts`.

---

## 5. Verification & Testing Plan

1. **Parser Tests (`test_parser.py`)**:
   - Verify sample RSC payloads from Listening, Reading, Writing, and Speaking parts parse without errors.
   - Assert all fields (`question`, `options`, `answer`, `explanation`, `audio`, `transcript`) are accurately populated.
2. **Database Integrity Tests (`test_db.py`)**:
   - Verify SQLite schema initialization, foreign key constraints, and indexing.
   - Test FTS5 full-text search queries.
3. **API & Server Integration Tests (`test_api.py`)**:
   - Verify FastAPI endpoints return status 200, proper JSON schemas, and valid HTML views.
   - Verify static asset routes serve offline MP3s and images correctly.
4. **End-to-End Test Run**:
   - Run crawler on initial batch (`exam1` through `exam5`), download media, build DB, start server, and simulate test submission with scoring verification.
