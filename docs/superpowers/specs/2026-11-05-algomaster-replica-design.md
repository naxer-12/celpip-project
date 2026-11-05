# Algomaster Full-Stack Crawler & Self-Hosted Replica Specification

**Date:** 2026-11-05  
**Target Path:** `/Users/jainamshah/Downloads/algomaster`  
**Status:** Approved Design Specification  

---

## 1. Executive Summary & Goals

The objective of this project is to crawl, extract, and replicate all public content from `https://algomaster.io/` into a fully functional, self-hosted, offline-capable platform.

### Target Content Inventory (from sitemap):
- **Practice Problems (~849 items):** Curated coding problems across DSA patterns, System Design, Low Level Design (LLD), and Concurrency. Each problem includes complete descriptions, examples, constraints, multiple solution approaches (e.g. Brute Force vs Optimal), multi-language code snippets (Python, Java, C++, JavaScript, Go), and algorithmic complexity analysis (time & space).
- **Animations (~1,291 items):** Interactive step-by-step visualizations of algorithm execution with playback controls and pointer/array state changes.
- **Roadmaps (29 items):** Structured learning roadmaps (DSA, Java, Python, C++, Go, SQL, Git, OS, Computer Networks, System Design, etc.).
- **Learn Articles (~3,878 items):** In-depth guides on System Design, LLD architectures, Engineering blogs, and AI engineering.

### Key Goals:
1. **Resumable, Polite Crawler:** Asynchronous Python crawler that tracks URL states in a persistent SQLite queue with polite delays and automatic retry on rate limits.
2. **Offline Decoupled Data Archive:** Raw HTML and RSC payloads cached locally to enable offline re-parsing without repeated network requests.
3. **Structured Relational Storage:** Clean SQLite database (`algomaster.db`) storing normalized problems, solutions, code tabs, roadmaps, and animations.
4. **Instant Sub-Millisecond Search:** SQLite FTS5 full-text search index across problem statements, patterns, code snippets, and explanations with BM25 ranking and snippet highlighting.
5. **Faithful UI Replica:** A responsive, lightweight single-page application replicating Algomaster's sleek aesthetic (dark/light theme, category sidebar, tabbed solution approaches, syntax-highlighted code tabs, complexity cards, interactive animation player, and `⌘K` command palette).
6. **Zero External Runtime Dependencies:** Runs self-contained via Python FastAPI with no Node.js or webpack build step required.

### Non-Goals:
- Account authentication or paywall bypass (only public sitemap resources are crawled).
- Online code execution sandbox (code tabs provide syntax-highlighted reference solutions with one-click copy).

---

## 2. System Architecture & Directory Structure

```text
/Users/jainamshah/Downloads/algomaster/
├── crawler/
│   ├── __init__.py
│   ├── queue_manager.py     # SQLite queue state machine (pending, fetching, cached, parsed, failed)
│   ├── crawler.py           # Async HTTP crawler (httpx, worker pool, polite rate-limiting, retries)
│   ├── parser.py            # Next.js RSC and Lexical AST extractor for problems, code, and roadmaps
│   └── asset_downloader.py  # Mirrors static assets (CSS, fonts, interactive animation JS bundles)
├── data/
│   ├── queue.db             # Crawl progress & retry tracker
│   ├── algomaster.db        # Core SQLite database with FTS5 virtual tables
│   ├── raw/                 # Cached raw HTML/RSC files for offline re-parsing
│   └── assets/              # Mirrored styles, fonts, and animation JS chunks
├── server/
│   ├── __init__.py
│   ├── app.py               # FastAPI application entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── problems.py      # Problem list, filters, and detail API
│   │   ├── animations.py    # Animation list and offline player embedding
│   │   ├── roadmaps.py      # Roadmap trees and milestone endpoints
│   │   ├── learn.py         # Module and guide endpoints
│   │   └── search.py        # FTS5 search query handler
│   └── db.py                # Database connection helpers & row mappers
├── static/
│   ├── index.html           # SPA entry point matching Algomaster's layout
│   ├── app.js               # Reactive SPA controller (routing, filters, code tabs, search modal)
│   └── style.css            # Dark/light theme styles, typography, and badges
├── tests/
│   ├── test_queue.py        # Queue state machine tests
│   ├── test_parser.py       # HTML & RSC parsing accuracy tests
│   └── test_api.py          # FastAPI endpoint and search tests
├── requirements.txt         # fastapi, uvicorn, httpx, beautifulsoup4, pytest
├── run_crawler.py           # CLI runner for staged pilot or full crawl
├── run_server.py            # One-command server startup
└── README.md                # Usage, setup, and documentation
```

---

## 3. Data Model & SQLite Schema (`algomaster.db`)

### `problems`
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing identifier |
| `slug` | TEXT UNIQUE | URL slug (e.g. `max-consecutive-ones`) |
| `title` | TEXT | Problem title |
| `category` | TEXT | `DSA`, `System Design`, `Low Level Design`, `Concurrency` |
| `sub_pattern` | TEXT | Pattern tag (e.g. `Sliding Window`, `Two Pointers`, `Dynamic Programming`) |
| `difficulty` | TEXT | `Easy`, `Medium`, or `Hard` |
| `description_html` | TEXT | Clean problem description HTML |
| `examples_json` | TEXT | JSON array of examples with inputs, outputs, and explanations |
| `constraints_json` | TEXT | JSON array of constraints |
| `tags_json` | TEXT | JSON array of tags (e.g. `["Array", "Sliding Window"]`) |
| `animation_slug` | TEXT NULL | Slug of corresponding interactive animation if available |
| `created_at` | TIMESTAMP | Timestamp of record creation |

### `solutions`
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing identifier |
| `problem_slug` | TEXT | Foreign key to `problems(slug)` |
| `approach_name` | TEXT | Approach title (e.g. `Brute Force`, `Single Pass`) |
| `approach_order` | INTEGER | Order of presentation (1, 2, 3...) |
| `intuition_html` | TEXT | Explanation of intuition and approach logic |
| `algorithm_html` | TEXT | Step-by-step algorithm explanation |
| `code_tabs_json` | TEXT | JSON object: `{"python": "...", "java": "...", "cpp": "...", "javascript": "...", "go": "..."}` |
| `time_complexity` | TEXT | E.g. `O(n)` |
| `space_complexity` | TEXT | E.g. `O(1)` |
| `complexity_notes` | TEXT | Detailed breakdown of time & space factors |

### `animations`
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing identifier |
| `slug` | TEXT UNIQUE | Animation slug (e.g. `dsa/max-consecutive-ones`) |
| `title` | TEXT | Animation title |
| `category` | TEXT | Animation category (e.g. `DSA`) |
| `problem_slug` | TEXT NULL | Mapped problem slug |
| `raw_cached_path` | TEXT | Local path to cached offline player HTML |

### `roadmaps`
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing identifier |
| `slug` | TEXT UNIQUE | Roadmap slug (e.g. `dsa`, `python`, `system-design`) |
| `title` | TEXT | Roadmap display title |
| `nodes_json` | TEXT | Hierarchical topics, milestones, and sections |

### `learn_articles`
| Column | Type | Description |
|---|---|---|
| `id` | INTEGER PRIMARY KEY | Auto-incrementing identifier |
| `slug` | TEXT UNIQUE | Article slug |
| `module` | TEXT | Module name (`system-design`, `lld`, `ai-engineering`, `eng-blogs`) |
| `title` | TEXT | Article title |
| `content_html` | TEXT | Formatted article body HTML |
| `order_index` | INTEGER | Display ordering index |

### `fts_content` (FTS5 Virtual Table)
Indexed fields:
- `title`
- `category`
- `sub_pattern`
- `difficulty`
- `content` (description, intuition, code, and notes)
- `slug`

---

## 4. Crawler & Parser Pipeline

### 4.1 Queue Manager (`crawler/queue_manager.py`)
- SQLite database `data/queue.db` storing every URL from the sitemap.
- States:
  - `pending`: Ready to be downloaded.
  - `fetching`: Currently being processed by an async worker.
  - `cached`: Raw HTML written to disk.
  - `parsed`: Data extracted and indexed in `algomaster.db`.
  - `failed`: Retries exhausted (with error message logged).
- Method `seed_from_sitemap(sitemap_url)` automatically parses the sitemap and categorizes URLs into sections.

### 4.2 Async Crawler (`crawler/crawler.py`)
- Built using `httpx.AsyncClient` with HTTP/2 and connection pooling.
- Concurrency bounded via `asyncio.Semaphore(5)`.
- Polite delays (300ms–800ms jitter between requests per worker).
- Automatic backoff on HTTP 429 (`Too Many Requests`) or 503 errors.
- Every successful fetch writes directly to `data/raw/<section>/<slug>.html`.

### 4.3 Parser Engine (`crawler/parser.py`)
- Parses Next.js RSC streams (`self.__next_f.push(...)`) and DOM elements.
- Extracts:
  - Problem statements, test cases, and constraints.
  - Solution approaches with multi-language code snippets.
  - Algorithmic complexities and explanatory text.
  - Roadmaps and guide structures.
- Writes extracted records directly into `algomaster.db` in atomic SQLite transactions.

### 4.4 Static Asset Downloader (`crawler/asset_downloader.py`)
- Identifies critical Next.js bundles, CSS stylesheets, fonts, and icons.
- Downloads and stores them in `data/assets/`.
- Rewrites internal CDN and origin references to local relative paths `/assets/...` to guarantee offline rendering of interactive animations and roadmaps.

---

## 5. Backend Server & Search Engine

### 5.1 FastAPI Endpoints (`server/app.py`)
- `GET /api/stats`: Returns count of crawled problems, animations, roadmaps, and crawl progress.
- `GET /api/problems`: List problems with query params:
  - `category`: Filter by category
  - `pattern`: Filter by pattern (e.g. `Two Pointers`)
  - `difficulty`: `Easy` | `Medium` | `Hard`
  - `search`: Keyword query
  - `page` & `limit`: Pagination support
- `GET /api/problems/{slug}`: Full problem payload with all solution approaches, code tabs, and complexity cards.
- `GET /api/animations`: List all interactive animations.
- `GET /api/animations/{slug}`: Animation details and offline player integration.
- `GET /api/roadmaps`: List all 29 developer roadmaps.
- `GET /api/roadmaps/{slug}`: Roadmap tree and milestone nodes.
- `GET /api/learn`: Chapter index for guides and blogs.
- `GET /api/learn/{slug}`: Guide article body and diagrams.
- `GET /api/search?q={query}`: FTS5 query returning matched items, BM25 scores, and highlighted snippets.

---

## 6. Frontend Replica UI (`static/`)

### 6.1 User Interface Layout
- **Header:** Brand emblem, section links (**Practice**, **Animations**, **Roadmaps**, **Learn**), global search trigger (`⌘K`), dark/light theme switch, and completed problem counter.
- **Practice View:**
  - Sidebar: Filter by DSA pattern, difficulty, and category.
  - Main Problem Area:
    - Problem title, difficulty badge, and pattern tag.
    - Description tab with formatted examples and constraints.
    - Approach tabs (e.g. *Brute Force*, *Single Pass*).
    - Multi-language code editor tabs (Python, Java, C++, JavaScript, Go) with copy button and syntax highlighting.
    - Complexity card callout box displaying Time and Space complexities.
    - Animation button to toggle the interactive visualization for this problem.
- **Animation View:**
  - Interactive playback frame rendering algorithm step progression with speed slider and navigation controls.
- **Roadmap View:**
  - Visual timeline/card hierarchy displaying progression topics and checklists.
- **Global Search (`⌘K` Modal):**
  - Instant keyboard-accessible modal with real-time FTS5 search results.

---

## 7. Staged Execution & Verification Plan

### Phase 1: Scaffolding & Core Implementation
- Create target folder `/Users/jainamshah/Downloads/algomaster`.
- Initialize Git repository, directory hierarchy, and `requirements.txt`.
- Implement `crawler/queue_manager.py`, `crawler/parser.py`, `crawler/crawler.py`, and `crawler/asset_downloader.py`.

### Phase 2: Pilot Batch Crawl & Test
- Seed queue with sitemap.
- Run a targeted pilot crawl of:
  - 25 representative DSA problems across patterns (Two Pointers, Sliding Window, Trees, Graphs, DP).
  - 5 interactive animation pages.
  - 3 developer roadmaps (DSA, Python, System Design).
- Run unit test suite (`pytest tests/`) verifying:
  - Problem title, difficulty, description extraction.
  - Solution approaches and multi-language code tabs.
  - Time and space complexity fields.
  - Static asset mirroring for animations.

### Phase 3: Backend & Frontend Replica Implementation
- Implement FastAPI server routes, database helpers, and FTS5 search engine.
- Build frontend SPA (`index.html`, `app.js`, `style.css`).
- Launch server on `http://localhost:8000` and verify:
  - Category and pattern filtering.
  - Solution tab switching and language code copying.
  - Interactive animation playback.
  - `⌘K` search latency (< 10ms) and snippet rendering.

### Phase 4: Full Dataset Crawling
- Provide command-line runner `python run_crawler.py --full` with live progress logging to crawl all 6,058 URLs.
- Verify checkpointing, resumption, and database integrity.
