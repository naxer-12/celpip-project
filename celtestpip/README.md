# CELTESTPIP Local Replica

A fast, complete offline replica of `https://www.celtestpip.com` featuring all 60 mock exams, question banks, offline audio playback, and an interactive exam simulator.

## Features

- **All 60 CELPIP Mock Exams**: Complete coverage across all 8 listening and reading test parts per exam.
- **100% Offline Capable**: All exam text, transcripts, explanations, audio recordings, and images are cached locally with zero external network dependencies.
- **Interactive Exam Simulator**: Timed mock exam interface featuring audio player, passage views, multi-question radio selections, instant grading, and answer reviews.
- **Official CLB Score Calculator**: Real-time Canadian Language Benchmark (CLB 3–12) calculator mapping raw test scores to official benchmarks.
- **SQLite + FTS5 Full-Text Search**: Instant search across all practice questions, passages, and detailed explanations.
- **Local Progress & Attempts Tracking**: Saves user test scores, submitted answers, and benchmark estimates locally in SQLite.

---

## Project Structure

```
celtestpip/
├── crawler/                  # Async crawling & parsing pipeline
│   ├── crawl_content.py      # Informational pages & sitemap crawler
│   ├── crawl_exams.py        # Next.js RSC flight payload crawler
│   ├── download_media.py     # Concurrent audio and image asset downloader
│   ├── parser.py             # Next.js RSC parser extracting exam questions & transcripts
│   └── run_crawler.py        # Unified CLI entrypoint with concurrency controls
├── data/                     # Offline storage
│   ├── raw/                  # Downloaded raw JSON parts & page caches
│   ├── media/                # Local audio (.mp3) and image files
│   └── celtestpip.db         # Indexed SQLite database with FTS5 virtual table
├── server/                   # FastAPI backend
│   ├── app.py                # REST API, static asset mounting, and HTML routing
│   ├── database.py           # SQLite schema initialization and data queries
│   └── scoring.py            # CELPIP raw-score to CLB level conversion logic
├── static/                   # Pure HTML5 / CSS3 / Vanilla JS frontend
│   ├── index.html            # Main dashboard & mock exam directory
│   ├── exam.html             # Interactive exam simulator view
│   ├── calculator.html       # Standalone interactive CLB calculator
│   ├── css/style.css         # Modern, accessible styling
│   └── js/                   # Frontend controllers (app.js, exam_runner.js, calculator.js)
├── tests/                    # Comprehensive pytest test suite
├── build_db.py               # SQLite database build pipeline script
├── server.py                 # Development server launch script (Uvicorn)
└── requirements.txt          # Python dependencies
```

---

## Quickstart

### 1. Install Dependencies

```bash
pip install -r celtestpip/requirements.txt
```

### 2. Run Crawler to Download Exams and Media

Crawl exams and offline media assets using the crawler CLI:

```bash
# Crawl initial 5 exams + media assets
python -m celtestpip.crawler.run_crawler --limit 5

# Or crawl all 60 exams with all media
python -m celtestpip.crawler.run_crawler --all

# Optional: Crawl specific components independently
python -m celtestpip.crawler.run_crawler --exams-only --limit 10
python -m celtestpip.crawler.run_crawler --media-only
python -m celtestpip.crawler.run_crawler --pages-only
```

#### Crawler CLI Options

| Flag | Description | Default |
|---|---|---|
| `--all` | Execute all pipeline stages (exams, pages, media) | `False` |
| `--limit N` | Maximum number of exams to crawl | All (60) |
| `--exams-only` | Run only the Next.js RSC exam crawler | `False` |
| `--media-only` | Run only media asset downloading | `False` |
| `--pages-only` | Run only informational sitemap page crawler | `False` |
| `--workers N` | Number of concurrent download workers | `5` |
| `--rate-limit S`| Delay between requests in seconds | `0.2` |

### 3. Build SQLite Database

Ingests raw parsed JSON files and creates local relational and full-text search tables:

```bash
python celtestpip/build_db.py
```

### 4. Launch the Local Application

Start the FastAPI local server:

```bash
python celtestpip/server.py
```

Open your browser to:
**[http://localhost:8000](http://localhost:8000)**

---

## Web Routes & REST API

### Frontend Views

- `GET /` — Home dashboard displaying all 60 mock exams, question statistics, and quick navigation.
- `GET /tools/clb-calculator` — Interactive Canadian Language Benchmark (CLB) score calculator.
- `GET /exams/{exam_id}/part/{part_number}` — Interactive exam test simulator for a specific exam part.

### API Endpoints

- `GET /api/exams` — List all indexed exams and total available parts.
- `GET /api/exams/{exam_id}/part/{part_number}` — Retrieve full exam part data including instructions, questions, answer options, transcripts, and local media URLs.
- `POST /api/attempts` — Submit user exam answers to store raw score, total questions, and CLB estimate.
- `GET /api/search?q={query}` — Full-Text Search (FTS5) querying question text and answer explanations.

---

## Testing

Run the full automated test suite verifying scrapers, parsers, DB build, API endpoints, and end-to-end flows:

```bash
pytest celtestpip/tests -v
```
