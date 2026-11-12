# CELTESTPIP Local Replica & Simulator

A fast, complete offline replica of `https://www.celtestpip.com` featuring all 60 mock exams, question banks, offline audio playback, an interactive exam simulator, and an official Canadian Language Benchmark (CLB) score calculator.

---

## Architecture Overview

The backend has been modularized with clean separation of concerns:

```
celtestpip/server/
├── app.py                # Application entrypoint, lifespan hooks, and middleware
├── config.py             # Paths, cache policies, and in-memory page cache
├── database.py           # SQLite connection, FTS5 table indexing, and query helpers
├── models.py             # Pydantic schemas for requests and responses
├── scoring.py            # Official CELPIP raw-score to CLB level conversion engine
└── routers/
    ├── assets.py         # Media streaming and immutable static assets
    ├── clerk.py          # Offline single-session Clerk authentication provider
    ├── exams.py          # REST APIs for exams, parts, search, and scoring attempts
    ├── pages.py          # HTML page views (Home, Exams, Results, Calculator, dynamic pages)
    ├── practices.py      # Interactive question runner and speaking/writing tasks
    ├── user.py           # User membership status and unlimited practice credits
    └── vocabulary.py     # Personal word bank, definitions, and audio pronunciation
```

---

## Key Features

- **All 60 CELPIP Mock Exams**: Complete coverage across all 20 listening, reading, writing, and speaking parts per exam.
- **100% Offline Capable**: All exam text, transcripts, explanations, audio recordings, and images are cached locally with zero external network dependencies.
- **Zero-Jank Question Answering**: Instant option selection, clean green checkmarks for correct choices, red crosses for wrong answers, and amber dashes for missed questions.
- **Official CLB Score Calculator**: Real-time Canadian Language Benchmark (CLB 3–12) calculator mapping raw test scores to official benchmarks.
- **SQLite + FTS5 Full-Text Search**: Instant search across all practice questions, passages, and detailed explanations.
- **Local Progress & Attempts Tracking**: Saves user test scores, submitted answers, and benchmark estimates locally in SQLite.

---

## Quickstart

### 1. Install Dependencies

```bash
pip install -r celtestpip/requirements.txt
```

### 2. Run the Server

```bash
python3 celtestpip/server.py --port 8001
```

- Primary Port: `http://localhost:8001`
- Companion Port: `http://localhost:3000`

### 3. Run Automated Tests

```bash
pytest celtestpip/tests -v
```
