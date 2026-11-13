# LanGeek French (`fr-EN`) Offline Staging & Testing Sandbox

A high-performance, offline-first staging replica and structured database of **LanGeek French** ([`https://langeek.co/fr-EN`](https://langeek.co/fr-EN)), built following the 5-phase web application replication methodology.

Features full paywall stripping, Next.js `__NEXT_DATA__` state unlocking, auth decoupling (eliminating infinite spinner loops), SQLite relational storage with FTS5 full-text search, and a FastAPI proxy server with dynamic upstream fallback.

---

## Key Features

- **949 Mapped Learning Routes:** Covers all canonical French learning paths from `sitemap-0.xml`, `sitemap-1.xml`, and `sitemap-3.xml`:
  - **82 Core Indexes & Categories:** CEFR Levels (A1, A2, B1, B2, C1), TCF exam preparation (A1–C2), 3,000 most common French words, reading modules, and pronunciation guides.
  - **105 In-Depth Grammar Courses:** Full syntactic and grammatical breakdowns (Subject pronouns, determiners, verb moods, punctuation, sentence structures).
  - **762 Topic & Level Vocabulary Decks:** Structured word lists with phonetic definitions, part of speech, English translations, and bilingual example pairs.
- **Client-Side Pro / Premium Unlocked:**
  - Patches serialized Next.js `__NEXT_DATA__` state to grant perpetual `isPremium: true`, `hasAccess: true`, and unlimited credits.
  - Injects non-destructive unblocking CSS (`#replica-unlock-style`) to eliminate blur utility classes (`blur-sm`, `filter blur-sm`, `backdrop-blur-*`) and lock banners.
- **Decoupled Auth Dependencies:**
  - Mock endpoints for `/v1/a`, `/v1/geoip`, and `/v1/plan` provide valid session states, preventing infinite client loading spinners.
- **Dual-Stream Extraction & SQLite Database:**
  - Extracts raw word entries, IPA phonetics, French definitions, English translations, and contextual sentence pairs into `data/langeek.db`.
  - Built-in **FTS5 full-text search engine** for sub-millisecond lexical queries.
- **Dual-Dialect Audio & Media Checkpointing:**
  - Tracks standard French (France) and Canadian French (`accent=CA`) text-to-speech audio URLs alongside illustration cards.
- **Dynamic Upstream Fallback:**
  - Missing or uncrawled routes are automatically fetched on demand from `langeek.co`, piped through the cleaner, cached to disk, and indexed in the background.

---

## Directory Structure

```text
langeek/
├── crawler.py          # Asynchronous sitemap & page crawler with checkpointing
├── cleaner.py          # Next.js state patcher, paywall stripper & unblocking styles
├── build_db.py         # SQLite schema, page indexer & FTS5 full-text search builder
├── server.py           # FastAPI server with in-memory cache & dynamic fallback proxy
├── media_fetcher.py    # Media and dual-dialect audio harvester
├── Dockerfile          # Container build definition
├── docker-compose.yml  # Docker Compose staging configuration
├── requirements.txt    # Python dependencies (fastapi, uvicorn, httpx, jinja2, pytest)
├── README.md           # Documentation & operational guide
├── data/
│   ├── pages/          # Cleaned, offline-ready HTML pages
│   ├── langeek.db      # SQLite relational database & FTS5 index
│   └── media/          # Downloaded audio pronunciations & illustrations
├── static/
│   └── next/static/    # Cached JavaScript bundles, CSS stylesheets, and fonts
└── tests/
    └── test_replica.py # Comprehensive unit and integration test suite
```

---

## Quickstart

### 1. Requirements

- Python 3.10+
- Install dependencies:
  ```bash
  pip install -r langeek/requirements.txt
  ```

### 2. Crawl Content

To crawl a curated seed batch (home, grammar index, vocab index, sample courses, and flashcard modules):
```bash
python -m langeek.crawler --limit 20
```

To execute a full crawl across all 949 canonical `/fr-EN` pages:
```bash
python -m langeek.crawler
```

### 3. Build or Re-index the SQLite Database

Parse all downloaded HTML pages in `data/pages/` into structured relational tables and rebuild the FTS5 search index:
```bash
python -m langeek.build_db
```

### 4. Run the Staging Server

Start the FastAPI replica server:
```bash
python -m langeek.server
```
Or via Uvicorn:
```bash
uvicorn langeek.server:app --host 0.0.0.0 --port 8080
```

Open your browser to:
- **Replica Home:** [http://localhost:8080/fr-EN](http://localhost:8080/fr-EN)
- **Vocabulary Index:** [http://localhost:8080/fr-EN/vocab](http://localhost:8080/fr-EN/vocab)
- **Grammar Index:** [http://localhost:8080/fr-EN/grammar](http://localhost:8080/fr-EN/grammar)
- **Interactive Flashcards:** [http://localhost:8080/fr-EN/vocab/subcategory/10476/learn/flashcard](http://localhost:8080/fr-EN/vocab/subcategory/10476/learn/flashcard)
- **Interactive Quiz:** [http://localhost:8080/fr-EN/vocab/subcategory/10476/learn/quiz](http://localhost:8080/fr-EN/vocab/subcategory/10476/learn/quiz)
- **API Documentation:** [http://localhost:8080/docs](http://localhost:8080/docs)

---

## Offline API Endpoints

The replica includes built-in REST endpoints for offline querying and application integrations:

| Method | Endpoint | Description |
|:---|:---|:---|
| `GET` | `/api/stats` | Returns database statistics (words, categories, courses, cached pages). |
| `GET` | `/api/search?q={term}` | Lightning-fast FTS5 full-text search across all French words, definitions, and examples. |
| `GET` | `/api/grammar?level={level}` | Lists indexed French grammar lessons and structural blocks. |
| `GET` | `/v1/a` | Decoupled mock user profile with unlocked Pro tier. |
| `GET` | `/v1/plan` | Decoupled mock subscription plan (`unlimited_pro`). |
| `GET` | `/v1/geoip` | Local mock IP geolocation (`Paris, France`). |

---

## Docker Deployment

To build and run the replica inside a containerized sandbox:

```bash
docker compose -f langeek/docker-compose.yml up --build
```

The container mounts `./data` and `./static` volumes so crawled pages, database indices, and media assets persist across container restarts.

---

## Running the Test Suite

Run the automated test suite to verify HTML state patching, SQLite indexing, FTS5 search queries, decoupled auth endpoints, and page serving:

```bash
pytest langeek/tests/test_replica.py -v
```
