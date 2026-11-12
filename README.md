# CELPIP Project (CELTESTPIP Replica & Simulation Engine)

An offline-first, full-fidelity replica and interactive simulation platform for the **CELPIP** (Canadian English Language Proficiency Index Program) General Exam.

---

## 📖 Table of Contents
1. [Overview](#-overview)
2. [CELPIP Core Concepts & Test Structure](#-celpip-core-concepts--test-structure)
3. [Canadian Language Benchmark (CLB) Scoring](#-canadian-language-benchmark-clb-scoring)
4. [Software Architecture & Design](#-software-architecture--design)
5. [Interactive Features](#-interactive-features)
6. [Project Structure](#-project-structure)
7. [Getting Started](#-getting-started)
8. [Testing & Verification](#-testing--verification)

---

## 🎯 Overview

The **CELPIP Project** is engineered as a high-performance, developer-friendly, and student-focused preparation environment. It mirrors the exact UI/UX, timing, media formats, audio players, and scoring mechanics of official CELPIP practice platforms, completely unlocked for free tester access without paywalls, subscriptions, or login blockers.

### Key Highlights
- **60 Full CELPIP Mock Exams**: Complete coverage with all 20 parts per exam.
- **Real-Time Interactive Question Runner**: Instant state reflection (green checks, red crosses, amber missed badges) with zero perpetual loading spinners.
- **Offline-First Media Engine**: Streaming support for all listening passages, question audio clips, and diagram visuals.
- **Comprehensive Vocabulary Builder**: Dedicated word bank with task categorization, definitions, and mastery progress.
- **Official CLB Calculator**: Automatic conversion of raw test scores (0–38) to Canadian Language Benchmark (CLB) bands.

---

## 🧠 CELPIP Core Concepts & Test Structure

The CELPIP General Test evaluates four foundational language competencies required for Canadian permanent residency (Express Entry) and Canadian citizenship.

```
+-----------------------------------------------------------------------+
|                       CELPIP General Test Structure                   |
+-------------------+-------------------+-------------------+-----------+
|    Listening      |      Reading      |      Writing      | Speaking  |
|   47-55 mins      |    55-60 mins     |    53-60 mins     |15-20 mins |
|     6 Parts       |      4 Parts      |      2 Tasks      |  8 Tasks  |
+-------------------+-------------------+-------------------+-----------+
```

### 1. Listening (47–55 minutes, 6 Parts, ~38 Questions)
- **Part 1: Listening to Problem Solving** — A conversation where two people identify and resolve a logistical or daily problem.
- **Part 2: Listening to a Daily Life Conversation** — Natural dialogue between friends, colleagues, or service providers.
- **Part 3: Listening for Information** — Detailed factual discussion or interview.
- **Part 4: Listening to a News Item** — Broadcast-style report covering an incident, civic event, or innovation.
- **Part 5: Listening to a Discussion** — Multi-speaker video/audio dialogue analyzing options or perspectives.
- **Part 6: Listening to Viewpoints** — Complex debate discussing contrasting opinions on a community issue.

### 2. Reading (55–60 minutes, 4 Parts, 38 Questions)
- **Part 1: Reading Correspondence** — Personal or business email followed by comprehension questions and a response letter.
- **Part 2: Reading to Apply a Diagram** — Visual schedule, brochure, or infographic linked to email correspondence.
- **Part 3: Reading for Information** — Informational article with 4 paragraph-matching questions and detail inquiries.
- **Part 4: Reading for Viewpoints** — Academic or editorial article analyzing social attitudes and policy arguments.

### 3. Writing (53–60 minutes, 2 Tasks)
- **Task 1: Writing an Email** — 150–200 words addressing a formal or semi-formal situation with 3 bulleted instructions.
- **Task 2: Responding to Survey Questions** — 150–200 words choosing between two community/workplace proposals and justifying the choice.

### 4. Speaking (15–20 minutes, 8 Tasks)
- **Task 1: Giving Advice** — Guiding a friend or family member making a decision.
- **Task 2: Talking about a Personal Experience** — Past-tense narrative on a memorable personal event.
- **Task 3: Describing a Scene** — Detailed description of an action-packed illustration.
- **Task 4: Making Predictions** — Forecasting what will happen next in the scene.
- **Task 5: Comparing and Persuading** — Selecting an item from two choices and persuading someone to agree.
- **Task 6: Dealing with a Difficult Situation** — Negotiating a compromise or breaking difficult news.
- **Task 7: Expressing Opinions** — Persuasive speech on a controversial social or civic issue.
- **Task 8: Describing an Unusual Situation** — Explaining a bizarre object or scene to someone who cannot see it.

---

## 📊 Canadian Language Benchmark (CLB) Scoring

Immigration, Refugees and Citizenship Canada (IRCC) evaluates language proficiency using the Canadian Language Benchmark (CLB) scale from 1 to 12.

| Raw Score (Listening /38) | Raw Score (Reading /38) | Official CLB Level | IRCC Express Entry Significance |
|:---:|:---:|:---:|:---|
| **37 – 38** | **38** | **CLB 12** | Flawless fluent proficiency |
| **35 – 36** | **36 – 37** | **CLB 11** | Advanced precision and nuance |
| **33 – 34** | **33 – 35** | **CLB 10** | Highly effective operational command |
| **30 – 32** | **31 – 32** | **CLB 9** | **Express Entry Sweet Spot** (Max CRS bonus points) |
| **27 – 29** | **28 – 30** | **CLB 8** | Fluent everyday command |
| **23 – 26** | **24 – 27** | **CLB 7** | Minimum threshold for Federal Skilled Worker (FSW) |
| **17 – 22** | **19 – 23** | **CLB 6** | Developing intermediate |
| **11 – 16** | **15 – 18** | **CLB 5** | Minimum threshold for Federal Skilled Trades (FST) |
| **7 – 10** | **10 – 14** | **CLB 4** | Minimum Canadian Citizenship requirement |
| **0 – 6** | **0 – 9** | **CLB 3** | Beginning English |

---

## 🏛 Software Architecture & Design

The backend is built with Python 3 and FastAPI, designed with strict separation of concerns, high-speed in-memory caching, and full testability.

```
                           +------------------------+
                           |  Browser / Client UI   |
                           +-----------+------------+
                                       |
                     HTTP / REST / Static Asset Requests
                                       |
                                       v
                     +----------------------------------+
                     |        FastAPI Server            |
                     |  (Lifespan, HeadMiddleware, Gzip)|
                     +-----------------+----------------+
                                       |
         +-----------------------------+-----------------------------+
         |              |              |              |              |
         v              v              v              v              v
    [pages.py]     [exams.py]    [practices.py] [vocabulary.py]   [assets.py]
         |              |              |              |              |
         |              +--------------+--------------+              |
         |                             |                             |
         v                             v                             v
  +--------------+            +------------------+           +---------------+
  | PAGE_CACHE   |            | SQLite Database  |           | Local Media / |
  | (Clean HTML) |            | (FTS5 Questions) |           | Next.js Chunks|
  +--------------+            +------------------+           +---------------+
```

### Architecture Components
- **`celtestpip/server/config.py`**: Centralized path resolution, Cache-Control policies, and template caches.
- **`celtestpip/server/models.py`**: Pydantic data schemas enforcing strict request validation and documentation.
- **`celtestpip/server/scoring.py`**: Domain module for CLB conversion logic, score tables, and level descriptions.
- **`celtestpip/server/database.py`**: SQLite database helpers, FTS5 virtual tables, schema creation, and transaction management.
- **`celtestpip/server/routers/`**:
  - `exams.py`: REST APIs for exams, exam parts, submissions, and full-text search.
  - `practices.py`: Fast question answering endpoints, answer recording, writing and speaking feedback.
  - `vocabulary.py`: Word bank CRUD, word status tracking, translation, and TTS endpoints.
  - `user.py`: Mock Pro membership and unlimited practice credits.
  - `clerk.py`: Offline Clerk auth provider allowing instant single-session tester access.
  - `assets.py`: Media streaming (.mp3, .wav, images) and immutable Next.js static asset delivery.
  - `pages.py`: HTML views (Home, Exams Catalog, Exam Runner, CLB Calculator, dynamic pages).
- **`celtestpip/server/app.py`**: Clean application assembler, middleware registration, and router inclusion.

---

## ⚡ Interactive Features

### 1. Zero-Jank Question Answering
When clicking options during a test:
- Local state updates immediately (`OptionMark` highlights blue with `aria-checked="true"`).
- `POST /api/question` acknowledges instantly (200 OK) without blocking UI threads.
- Upon revealing answers:
  - **Correct Answer**: Highlighted in soft green (`bg-emerald-100`) with green checkmark (`✓`).
  - **User's Wrong Choice**: Highlighted in soft red (`bg-rose-100`) with red cross (`✕`).
  - **Missed Option**: Tagged in soft amber (`bg-amber-100`) with dash (`-`).

### 2. Full Content Unlocking
- Pro locks, blur filters (`backdrop-blur-sm`, `filter blur-sm`), and subscription paywalls are stripped using non-destructive AST and regex transforms.
- Next.js RSC Flight JSON hydration variables (`isProUser: true`, `isPremium: true`, `hasAccess: true`, `userCredits: 9999`) ensure client components render in full unlocked mode.

---

## 📁 Project Structure

```
celpip-project/
├── celtestpip/
│   ├── crawler/              # Automated ingestion pipeline for exams & media
│   │   ├── crawl_content.py  # Page content & sitemap crawler
│   │   ├── crawl_exams.py    # RSC flight payload crawler
│   │   ├── download_media.py # Audio and image asset downloader
│   │   └── rsc_parser.py     # Parser extracting exam questions & transcripts
│   ├── data/                 # Local data storage
│   │   ├── celtestpip.db     # SQLite database with FTS5 search
│   │   ├── media/            # Audio files (.mp3) and image assets
│   │   └── pages/            # Replicated and unlocked HTML content pages
│   ├── scripts/
│   │   └── unlock_all_pro_content.py # Content unlocking and paywall removal
│   ├── server/               # Modular FastAPI application
│   │   ├── app.py            # Main application assembly & lifespan
│   │   ├── config.py         # Paths, headers, and in-memory caches
│   │   ├── database.py       # SQLite connection and migrations
│   │   ├── models.py         # Pydantic schemas
│   │   ├── scoring.py        # Official CLB scoring engine
│   │   └── routers/          # Modular route handlers
│   │       ├── assets.py     # Static & media streaming
│   │       ├── clerk.py      # Mock Clerk authentication
│   │       ├── exams.py      # Exam catalog & simulator APIs
│   │       ├── pages.py      # HTML routes & page caching
│   │       ├── practices.py  # Interactive question answering
│   │       ├── user.py       # Pro status & credits
│   │       └── vocabulary.py # Word bank & vocabulary APIs
│   ├── static/               # Frontend bundles, Next.js chunks, fonts, styles
│   ├── tests/                # Automated pytest suite (77 tests)
│   ├── build_db.py           # Database build pipeline
│   ├── server.py             # Dual-port server launcher (ports 8001 & 3000)
│   └── requirements.txt      # Python dependencies
├── README.md                 # Complete system documentation
└── .gitignore                # Git ignore configuration
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- `pip` package manager

### 1. Install Dependencies
```bash
pip install -r celtestpip/requirements.txt
```

### 2. Start the Server
Launch the local replica server:
```bash
python3 celtestpip/server.py --port 8001
```
The server binds across all interfaces and dual-stack IPv4/IPv6 sockets:
- **Primary Server:** [http://localhost:8001](http://localhost:8001)
- **Companion Server:** [http://localhost:3000](http://localhost:3000)

### 3. Open in Browser
- **Home Landing Page:** `http://localhost:8001/` or `http://localhost:3000/home`
- **Exams Catalog:** `http://localhost:8001/exams`
- **CLB Calculator:** `http://localhost:8001/tools/clb-calculator`
- **Exam Simulator (e.g. Exam 1):** `http://localhost:8001/exams/exam1/part1`

---

## 🧪 Testing & Verification

The project includes an end-to-end automated test suite covering all APIs, routers, HTML pages, cache headers, scoring logic, and unlocked content:

```bash
pytest celtestpip/tests -v
```

**Results:**
```
======================== 77 passed in 2.35s =========================
```
