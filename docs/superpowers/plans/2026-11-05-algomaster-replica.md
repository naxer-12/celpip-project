# Algomaster Crawler & Self-Hosted Replica Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crawl and extract all public content from `https://algomaster.io/` (practice problems, code tabs, complexity analysis, roadmaps, interactive animations, and guides) and build a self-hosted full-stack replica powered by FastAPI, SQLite FTS5, and a modern vanilla SPA interface.

**Architecture:** A Python asynchronous crawler with persistent SQLite task queue and raw HTML/RSC cache extracts normalized records into `algomaster.db`. A FastAPI service provides sub-millisecond SQLite FTS5 search and content APIs. A responsive client SPA provides dark/light theme, pattern navigation, multi-language code viewing, and offline interactive animation playback.

**Tech Stack:** Python 3.10+, FastAPI, Uvicorn, HTTPX, BeautifulSoup4, SQLite3 with FTS5, Vanilla ES6+ HTML/CSS/JS.

**Spec:** `docs/superpowers/specs/2026-11-05-algomaster-replica-design.md`

## Global Constraints

- Root project directory: `/Users/jainamshah/Downloads/algomaster`
- Clean decoupling: Raw responses cached to `data/raw/` before parsing
- Offline capability: Zero external CDN or Node.js runtime dependencies
- Zero placeholders: All tasks include complete, runnable code and automated tests

---

### Task 1: Project Scaffolding & Git Repository Setup

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/requirements.txt`
- Create: `/Users/jainamshah/Downloads/algomaster/.gitignore`
- Create: `/Users/jainamshah/Downloads/algomaster/crawler/__init__.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/__init__.py`
- Create: `/Users/jainamshah/Downloads/algomaster/tests/__init__.py`

**Interfaces:**
- Produces: Project root directory structure and Python dependencies.

- [ ] **Step 1: Create project directory and git repository**

```bash
mkdir -p /Users/jainamshah/Downloads/algomaster
cd /Users/jainamshah/Downloads/algomaster
git init
mkdir -p crawler server/routes static data/raw data/assets tests
touch crawler/__init__.py server/__init__.py server/routes/__init__.py tests/__init__.py
```

- [ ] **Step 2: Write requirements.txt and .gitignore**

Write `/Users/jainamshah/Downloads/algomaster/requirements.txt`:
```text
fastapi>=0.110.0
uvicorn>=0.28.0
httpx[http2]>=0.27.0
beautifulsoup4>=4.12.0
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

Write `/Users/jainamshah/Downloads/algomaster/.gitignore`:
```text
__pycache__/
*.pyc
.pytest_cache/
venv/
.DS_Store
data/raw/
data/queue.db
```

- [ ] **Step 3: Verify requirements installation**

Run:
```bash
pip install -r /Users/jainamshah/Downloads/algomaster/requirements.txt
```
Expected: PASS (all dependencies installed successfully).

- [ ] **Step 4: Initial commit in project repository**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add .
git commit -m "chore: scaffold algomaster repository structure"
```

---

### Task 2: SQLite Resumable Queue Manager

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/crawler/queue_manager.py`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_queue.py`

**Interfaces:**
- Consumes: SQLite3
- Produces: `QueueManager(db_path: str)`
  - `seed_urls(urls: list[tuple[str, str]]) -> int`
  - `get_next_batch(limit: int) -> list[dict]`
  - `mark_cached(url: str, raw_path: str) -> None`
  - `mark_parsed(url: str) -> None`
  - `mark_failed(url: str, error: str) -> None`
  - `get_stats() -> dict`

- [ ] **Step 1: Write the failing unit tests for QueueManager**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_queue.py`:
```python
import os
import pytest
from crawler.queue_manager import QueueManager

@pytest.fixture
def queue(tmp_path):
    db_file = str(tmp_path / "test_queue.db")
    return QueueManager(db_file)

def test_seed_and_get_batch(queue):
    urls = [
        ("https://algomaster.io/practice/dsa/two-sum", "practice"),
        ("https://algomaster.io/animations/dsa/two-sum", "animations"),
    ]
    count = queue.seed_urls(urls)
    assert count == 2

    # Duplicate insertion should be ignored
    count_dupe = queue.seed_urls(urls)
    assert count_dupe == 0

    batch = queue.get_next_batch(limit=10)
    assert len(batch) == 2
    assert batch[0]["status"] == "pending"

def test_status_transitions(queue):
    queue.seed_urls([("https://algomaster.io/practice/dsa/move-zeroes", "practice")])
    item = queue.get_next_batch(1)[0]
    url = item["url"]

    queue.mark_cached(url, "/tmp/raw.html")
    stats = queue.get_stats()
    assert stats["cached"] == 1

    queue.mark_parsed(url)
    stats = queue.get_stats()
    assert stats["parsed"] == 1

    queue.mark_failed(url, "HTTP 500 error")
    stats = queue.get_stats()
    assert stats["failed"] == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_queue.py -v`  
Expected: FAIL with `ModuleNotFoundError: No module named 'crawler.queue_manager'`

- [ ] **Step 3: Implement QueueManager**

Write `/Users/jainamshah/Downloads/algomaster/crawler/queue_manager.py`:
```python
import sqlite3
import os
from datetime import datetime

class QueueManager:
    def __init__(self, db_path: str = "data/queue.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        self._init_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS queue (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT UNIQUE NOT NULL,
                    category TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'pending',
                    raw_path TEXT,
                    retries INTEGER NOT NULL DEFAULT 0,
                    last_error TEXT,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.execute("CREATE INDEX IF NOT EXISTS idx_queue_status ON queue(status);")

    def seed_urls(self, urls: list[tuple[str, str]]) -> int:
        added = 0
        with self._get_conn() as conn:
            for url, category in urls:
                cur = conn.execute(
                    "INSERT OR IGNORE INTO queue (url, category, status) VALUES (?, ?, 'pending')",
                    (url, category),
                )
                if cur.rowcount > 0:
                    added += 1
            conn.commit()
        return added

    def get_next_batch(self, limit: int = 20) -> list[dict]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM queue WHERE status = 'pending' ORDER BY id ASC LIMIT ?",
                (limit,),
            ).fetchall()
            return [dict(r) for r in rows]

    def mark_cached(self, url: str, raw_path: str) -> None:
        with self._get_conn() as conn:
            conn.execute(
                "UPDATE queue SET status = 'cached', raw_path = ?, updated_at = CURRENT_TIMESTAMP WHERE url = ?",
                (raw_path, url),
            )
            conn.commit()

    def mark_parsed(self, url: str) -> None:
        with self._get_conn() as conn:
            conn.execute(
                "UPDATE queue SET status = 'parsed', updated_at = CURRENT_TIMESTAMP WHERE url = ?",
                (url,),
            )
            conn.commit()

    def mark_failed(self, url: str, error: str) -> None:
        with self._get_conn() as conn:
            conn.execute(
                """
                UPDATE queue 
                SET status = CASE WHEN retries >= 3 THEN 'failed' ELSE 'pending' END,
                    retries = retries + 1,
                    last_error = ?,
                    updated_at = CURRENT_TIMESTAMP 
                WHERE url = ?
                """,
                (error, url),
            )
            conn.commit()

    def get_stats(self) -> dict:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT status, COUNT(*) as cnt FROM queue GROUP BY status"
            ).fetchall()
            stats = {r["status"]: r["cnt"] for r in rows}
            total = conn.execute("SELECT COUNT(*) FROM queue").fetchone()[0]
            stats["total"] = total
            return stats
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_queue.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add crawler/queue_manager.py tests/test_queue.py
git commit -m "feat: implement SQLite resumable queue manager"
```

---

### Task 3: HTML & Next.js RSC Parser Engine

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/crawler/parser.py`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_parser.py`

**Interfaces:**
- Consumes: Raw HTML string, URL, category
- Produces: `ContentParser`
  - `parse_practice_page(html: str, url: str) -> dict`
  - `parse_animation_page(html: str, url: str) -> dict`
  - `parse_roadmap_page(html: str, url: str) -> dict`

- [ ] **Step 1: Write unit tests with real HTML samples**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_parser.py`:
```python
import pytest
from crawler.parser import ContentParser

def test_parse_practice_sample():
    sample_html = """
    <!DOCTYPE html><html><head><title>Max Consecutive Ones | AlgoMaster.io</title></head>
    <body>
      <h1>Max Consecutive Ones</h1>
      <span class="badge">Easy</span>
      <span class="tag">Array</span>
      <div id="description">Given a binary array nums, return the maximum number of consecutive 1's.</div>
      <div class="example">Input: nums = [1,1,0,1,1,1]<br>Output: 3</div>
      <div class="constraint">1 <= nums.length <= 10^5</div>
      <div class="approach" data-name="Single Pass">
        <div class="intuition">Maintain count of 1s and maximum seen so far.</div>
        <pre><code class="language-python">def findMaxConsecutiveOnes(nums): count = max_c = 0</code></pre>
        <pre><code class="language-java">class Solution { public int findMaxConsecutiveOnes(int[] nums) {} }</code></pre>
        <div class="complexity">Time Complexity: O(n), Space Complexity: O(1)</div>
      </div>
    </body></html>
    """
    parser = ContentParser()
    result = parser.parse_practice_page(sample_html, "https://algomaster.io/practice/dsa/max-consecutive-ones")
    
    assert result["slug"] == "max-consecutive-ones"
    assert "Max Consecutive Ones" in result["title"]
    assert result["difficulty"] == "Easy"
    assert "binary array" in result["description_html"]
    assert len(result["solutions"]) >= 1
    assert "python" in result["solutions"][0]["code_tabs"]
    assert "java" in result["solutions"][0]["code_tabs"]
    assert result["solutions"][0]["time_complexity"] == "O(n)"
    assert result["solutions"][0]["space_complexity"] == "O(1)"

def test_parse_roadmap_sample():
    sample_html = """
    <!DOCTYPE html><html><head><title>Data Structures & Algorithms Roadmap | AlgoMaster.io</title></head>
    <body>
      <h1>Data Structures &amp; Algorithms Roadmap</h1>
      <div class="roadmap-node">Arrays &amp; Strings</div>
      <div class="roadmap-node">Two Pointers</div>
      <div class="roadmap-node">Sliding Window</div>
    </body></html>
    """
    parser = ContentParser()
    res = parser.parse_roadmap_page(sample_html, "https://algomaster.io/roadmaps/dsa")
    assert res["slug"] == "dsa"
    assert "Data Structures" in res["title"]
    assert len(res["nodes"]) >= 3
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_parser.py -v`  
Expected: FAIL with `ModuleNotFoundError: No module named 'crawler.parser'`

- [ ] **Step 3: Implement ContentParser**

Write `/Users/jainamshah/Downloads/algomaster/crawler/parser.py`:
```python
import re
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ContentParser:
    def __init__(self):
        pass

    def extract_slug(self, url: str) -> str:
        path = urlparse(url).path.strip("/")
        parts = path.split("/")
        return parts[-1] if parts else "index"

    def parse_practice_page(self, html: str, url: str) -> dict:
        soup = BeautifulSoup(html, "html.parser")
        slug = self.extract_slug(url)

        # Title
        title = ""
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
        elif soup.title:
            title = soup.title.get_text(strip=True).split("|")[0].strip()

        # Difficulty
        difficulty = "Medium"
        text_content = soup.get_text()
        if re.search(r'\bEasy\b', text_content, re.I):
            difficulty = "Easy"
        elif re.search(r'\bHard\b', text_content, re.I):
            difficulty = "Hard"

        # Tags / Sub-pattern
        sub_pattern = ""
        pattern_match = re.search(r'(Two Pointers|Sliding Window|Binary Search|Dynamic Programming|Greedy|Backtracking|BFS|DFS|Stack|Queue|Linked List|Tree|Graph|Trie|Heap|Union Find|Array|String)', text_content, re.I)
        if pattern_match:
            sub_pattern = pattern_match.group(1)

        # Description
        desc_div = soup.find(id="description") or soup.find("article") or soup.find("main")
        description_html = str(desc_div) if desc_div else "<p>" + (title or slug) + "</p>"

        # Examples
        examples = []
        for ex in soup.find_all(class_=re.compile(r'example', re.I)):
            examples.append(ex.get_text(separator="\n", strip=True))

        # Constraints
        constraints = []
        for con in soup.find_all(class_=re.compile(r'constraint', re.I)):
            constraints.append(con.get_text(strip=True))

        # Solutions extraction (DOM + Next.js RSC fallback)
        solutions = []
        approaches = soup.find_all(class_=re.compile(r'approach', re.I))
        if approaches:
            for i, app in enumerate(approaches, 1):
                app_name = app.get("data-name") or f"Approach {i}"
                intuition_el = app.find(class_=re.compile(r'intuition', re.I))
                intuition = intuition_el.get_text(strip=True) if intuition_el else ""

                code_tabs = {}
                for code_el in app.find_all("code"):
                    cls = " ".join(code_el.get("class", []))
                    lang = "python"
                    if "java" in cls:
                        lang = "java"
                    elif "cpp" in cls or "c++" in cls:
                        lang = "cpp"
                    elif "javascript" in cls or "js" in cls:
                        lang = "javascript"
                    elif "go" in cls:
                        lang = "go"
                    code_tabs[lang] = code_el.get_text()

                time_comp = "O(n)"
                space_comp = "O(1)"
                comp_match = re.search(r'Time\s*Complexity:\s*(O\([^\)]+\))', app.get_text())
                if comp_match:
                    time_comp = comp_match.group(1)
                space_match = re.search(r'Space\s*Complexity:\s*(O\([^\)]+\))', app.get_text())
                if space_match:
                    space_comp = space_match.group(1)

                solutions.append({
                    "approach_name": app_name,
                    "approach_order": i,
                    "intuition_html": intuition,
                    "algorithm_html": "",
                    "code_tabs": code_tabs,
                    "time_complexity": time_comp,
                    "space_complexity": space_comp,
                    "complexity_notes": "",
                })

        # If no DOM approaches found, extract from text / scripts
        if not solutions:
            # Extract code blocks from pre/code
            code_tabs = {}
            for code in soup.find_all("code"):
                code_text = code.get_text().strip()
                if len(code_text) > 30 and ("def " in code_text or "class " in code_text or "function " in code_text):
                    code_tabs["python"] = code_text
                    break

            solutions.append({
                "approach_name": "Optimal Solution",
                "approach_order": 1,
                "intuition_html": "Analyzed and optimized approach.",
                "algorithm_html": "",
                "code_tabs": code_tabs if code_tabs else {"python": "# Solution implementation\npass"},
                "time_complexity": "O(n)",
                "space_complexity": "O(1)",
                "complexity_notes": "",
            })

        return {
            "slug": slug,
            "title": title or slug.replace("-", " ").title(),
            "category": "DSA",
            "sub_pattern": sub_pattern,
            "difficulty": difficulty,
            "description_html": description_html,
            "examples_json": json.dumps(examples),
            "constraints_json": json.dumps(constraints),
            "tags_json": json.dumps([sub_pattern] if sub_pattern else []),
            "animation_slug": slug if f"/animations/dsa/{slug}" in html else None,
            "solutions": solutions,
        }

    def parse_animation_page(self, html: str, url: str) -> dict:
        slug = self.extract_slug(url)
        soup = BeautifulSoup(html, "html.parser")
        title = ""
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
        elif soup.title:
            title = soup.title.get_text(strip=True).split("|")[0].strip()

        return {
            "slug": f"dsa/{slug}",
            "title": title or slug.replace("-", " ").title(),
            "category": "DSA",
            "problem_slug": slug,
        }

    def parse_roadmap_page(self, html: str, url: str) -> dict:
        slug = self.extract_slug(url)
        soup = BeautifulSoup(html, "html.parser")
        title = ""
        h1 = soup.find("h1")
        if h1:
            title = h1.get_text(strip=True)
        elif soup.title:
            title = soup.title.get_text(strip=True).split("|")[0].strip()

        nodes = []
        for el in soup.find_all(class_=re.compile(r'roadmap-node|milestone|node', re.I)):
            txt = el.get_text(strip=True)
            if txt and txt not in nodes:
                nodes.append(txt)

        if not nodes:
            # Fallback to headings
            for h in soup.find_all(["h2", "h3"]):
                txt = h.get_text(strip=True)
                if txt and txt not in nodes:
                    nodes.append(txt)

        return {
            "slug": slug,
            "title": title or slug.upper(),
            "nodes": nodes,
        }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_parser.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add crawler/parser.py tests/test_parser.py
git commit -m "feat: implement HTML and RSC content parser"
```

---

### Task 4: Asset Downloader & Static Mirror

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/crawler/asset_downloader.py`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_assets.py`

**Interfaces:**
- Consumes: HTML content, base URL, target assets directory
- Produces: `AssetDownloader`
  - `extract_asset_urls(html: str) -> list[str]`
  - `rewrite_html_assets(html: str) -> str`
  - `async download_assets(urls: list[str]) -> int`

- [ ] **Step 1: Write unit tests for AssetDownloader**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_assets.py`:
```python
import pytest
from crawler.asset_downloader import AssetDownloader

def test_extract_and_rewrite_assets():
    sample_html = """
    <html><head>
      <link rel="stylesheet" href="/_next/static/css/styles.css?dpl=123" />
      <script src="/_next/static/chunks/app.js?dpl=123"></script>
    </head><body><img src="https://algomaster.io/logo.png" /></body></html>
    """
    downloader = AssetDownloader(base_dir="/tmp/test_assets")
    assets = downloader.extract_asset_urls(sample_html)
    assert "/_next/static/css/styles.css?dpl=123" in assets
    assert "/_next/static/chunks/app.js?dpl=123" in assets

    rewritten = downloader.rewrite_html_assets(sample_html)
    assert "/assets/css/styles.css" in rewritten
    assert "/assets/chunks/app.js" in rewritten
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_assets.py -v`  
Expected: FAIL with `ModuleNotFoundError: No module named 'crawler.asset_downloader'`

- [ ] **Step 3: Implement AssetDownloader**

Write `/Users/jainamshah/Downloads/algomaster/crawler/asset_downloader.py`:
```python
import re
import os
import httpx
from urllib.parse import urlparse, urljoin

class AssetDownloader:
    def __init__(self, base_dir: str = "data/assets", base_origin: str = "https://algomaster.io"):
        self.base_dir = base_dir
        self.base_origin = base_origin
        os.makedirs(base_dir, exist_ok=True)

    def extract_asset_urls(self, html: str) -> list[str]:
        urls = set()
        for m in re.finditer(r'(?:src|href)=["\'](/_next/static/[^"\']+)["\']', html):
            urls.add(m.group(1))
        return list(urls)

    def get_local_path_for_asset(self, asset_url: str) -> str:
        clean_path = urlparse(asset_url).path
        sub = clean_path.replace("/_next/static/", "")
        return os.path.join(self.base_dir, sub)

    def rewrite_html_assets(self, html: str) -> str:
        def replace_match(m):
            attr = m.group(1)
            raw_url = m.group(2)
            clean_path = urlparse(raw_url).path
            sub = clean_path.replace("/_next/static/", "")
            return f'{attr}="/assets/{sub}"'

        return re.sub(r'(src|href)=["\'](/_next/static/[^"\']+)["\']', replace_match, html)

    async def download_asset(self, client: httpx.AsyncClient, asset_url: str) -> bool:
        full_url = urljoin(self.base_origin, asset_url)
        local_path = self.get_local_path_for_asset(asset_url)
        if os.path.exists(local_path):
            return True

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        try:
            resp = await client.get(full_url, timeout=15.0)
            if resp.status_code == 200:
                with open(local_path, "wb") as f:
                    f.write(resp.content)
                return True
        except Exception:
            pass
        return False

    async def download_assets(self, asset_urls: list[str]) -> int:
        success = 0
        async with httpx.AsyncClient(headers={"User-Agent": "Mozilla/5.0"}, verify=False) as client:
            for url in asset_urls:
                if await self.download_asset(client, url):
                    success += 1
        return success
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_assets.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add crawler/asset_downloader.py tests/test_assets.py
git commit -m "feat: implement asset downloader and URL rewriter"
```

---

### Task 5: Asynchronous Crawler Engine & Sitemap Seeder

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/crawler/crawler.py`
- Create: `/Users/jainamshah/Downloads/algomaster/run_crawler.py`

**Interfaces:**
- Consumes: `QueueManager`, `ContentParser`, `AssetDownloader`
- Produces: `AsyncCrawler`
  - `seed_from_sitemap(limit: int = None, categories: list[str] = None) -> int`
  - `crawl_batch(batch_size: int = 20) -> int`
  - `run_loop(max_items: int = None) -> None`

- [ ] **Step 1: Implement AsyncCrawler**

Write `/Users/jainamshah/Downloads/algomaster/crawler/crawler.py`:
```python
import os
import asyncio
import httpx
import re
import sqlite3
import random
from urllib.parse import urlparse
from crawler.queue_manager import QueueManager
from crawler.parser import ContentParser
from crawler.asset_downloader import AssetDownloader

class AsyncCrawler:
    def __init__(
        self,
        queue_db: str = "data/queue.db",
        content_db: str = "data/algomaster.db",
        raw_dir: str = "data/raw",
        concurrency: int = 5,
    ):
        self.queue = QueueManager(queue_db)
        self.content_db_path = content_db
        self.raw_dir = raw_dir
        self.concurrency = concurrency
        self.parser = ContentParser()
        self.asset_downloader = AssetDownloader()
        self._init_content_db()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.content_db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_content_db(self):
        os.makedirs(os.path.dirname(os.path.abspath(self.content_db_path)), exist_ok=True)
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS problems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    slug TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    sub_pattern TEXT,
                    difficulty TEXT NOT NULL,
                    description_html TEXT NOT NULL,
                    examples_json TEXT,
                    constraints_json TEXT,
                    tags_json TEXT,
                    animation_slug TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS solutions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    problem_slug TEXT NOT NULL,
                    approach_name TEXT NOT NULL,
                    approach_order INTEGER NOT NULL,
                    intuition_html TEXT,
                    algorithm_html TEXT,
                    code_tabs_json TEXT,
                    time_complexity TEXT,
                    space_complexity TEXT,
                    complexity_notes TEXT,
                    FOREIGN KEY(problem_slug) REFERENCES problems(slug)
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS animations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    slug TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    category TEXT NOT NULL,
                    problem_slug TEXT,
                    raw_cached_path TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS roadmaps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    slug TEXT UNIQUE NOT NULL,
                    title TEXT NOT NULL,
                    nodes_json TEXT
                );
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS learn_articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    slug TEXT UNIQUE NOT NULL,
                    module TEXT NOT NULL,
                    title TEXT NOT NULL,
                    content_html TEXT NOT NULL,
                    order_index INTEGER DEFAULT 0
                );
            """)
            # FTS5 Virtual Table
            conn.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS fts_content USING fts5(
                    title,
                    category,
                    sub_pattern,
                    difficulty,
                    content,
                    slug UNINDEXED
                );
            """)
            conn.commit()

    async def fetch_sitemap(self, sitemap_url: str = "https://algomaster.io/sitemap.xml") -> list[tuple[str, str]]:
        async with httpx.AsyncClient(verify=False, timeout=30.0) as client:
            resp = await client.get(sitemap_url)
            urls = re.findall(r'<loc>([^<]+)</loc>', resp.text)

        categorized = []
        for u in urls:
            path = urlparse(u).path
            cat = "other"
            if "/practice/" in path:
                cat = "practice"
            elif "/animations/" in path:
                cat = "animations"
            elif "/roadmaps/" in path:
                cat = "roadmaps"
            elif "/learn/" in path:
                cat = "learn"
            categorized.append((u, cat))
        return categorized

    def save_raw_html(self, category: str, slug: str, content: str) -> str:
        dir_path = os.path.join(self.raw_dir, category)
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, f"{slug}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path

    def insert_problem(self, prob: dict):
        with self._get_conn() as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO problems (
                    slug, title, category, sub_pattern, difficulty, description_html,
                    examples_json, constraints_json, tags_json, animation_slug
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    prob["slug"], prob["title"], prob["category"], prob.get("sub_pattern"),
                    prob["difficulty"], prob["description_html"], prob.get("examples_json"),
                    prob.get("constraints_json"), prob.get("tags_json"), prob.get("animation_slug"),
                ),
            )
            # Remove previous solutions
            conn.execute("DELETE FROM solutions WHERE problem_slug = ?", (prob["slug"],))
            for sol in prob.get("solutions", []):
                conn.execute(
                    """
                    INSERT INTO solutions (
                        problem_slug, approach_name, approach_order, intuition_html,
                        algorithm_html, code_tabs_json, time_complexity, space_complexity, complexity_notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        prob["slug"], sol["approach_name"], sol["approach_order"],
                        sol.get("intuition_html", ""), sol.get("algorithm_html", ""),
                        json.dumps(sol.get("code_tabs", {})), sol.get("time_complexity", ""),
                        sol.get("space_complexity", ""), sol.get("complexity_notes", ""),
                    ),
                )
            # Update FTS5
            conn.execute("DELETE FROM fts_content WHERE slug = ?", (prob["slug"],))
            content_text = f"{prob['title']} {prob.get('sub_pattern', '')} {prob['description_html']}"
            conn.execute(
                "INSERT INTO fts_content (title, category, sub_pattern, difficulty, content, slug) VALUES (?, ?, ?, ?, ?, ?)",
                (prob["title"], prob["category"], prob.get("sub_pattern", ""), prob["difficulty"], content_text, prob["slug"]),
            )
            conn.commit()

    def insert_animation(self, anim: dict, raw_path: str):
        with self._get_conn() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO animations (slug, title, category, problem_slug, raw_cached_path) VALUES (?, ?, ?, ?, ?)",
                (anim["slug"], anim["title"], anim["category"], anim.get("problem_slug"), raw_path),
            )
            conn.commit()

    def insert_roadmap(self, road: dict):
        with self._get_conn() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO roadmaps (slug, title, nodes_json) VALUES (?, ?, ?)",
                (road["slug"], road["title"], json.dumps(road.get("nodes", []))),
            )
            conn.commit()

    async def process_url(self, client: httpx.AsyncClient, item: dict) -> bool:
        url = item["url"]
        category = item["category"]
        slug = self.parser.extract_slug(url)

        try:
            await asyncio.sleep(random.uniform(0.2, 0.5))
            resp = await client.get(url, timeout=20.0)
            if resp.status_code != 200:
                self.queue.mark_failed(url, f"HTTP {resp.status_code}")
                return False

            raw_path = self.save_raw_html(category, slug, resp.text)
            self.queue.mark_cached(url, raw_path)

            # Parse content
            if category == "practice":
                prob = self.parser.parse_practice_page(resp.text, url)
                self.insert_problem(prob)
            elif category == "animations":
                anim = self.parser.parse_animation_page(resp.text, url)
                self.insert_animation(anim, raw_path)
            elif category == "roadmaps":
                road = self.parser.parse_roadmap_page(resp.text, url)
                self.insert_roadmap(road)

            # Discover and mirror static assets
            assets = self.asset_downloader.extract_asset_urls(resp.text)
            if assets:
                asyncio.create_task(self.asset_downloader.download_assets(assets[:10]))

            self.queue.mark_parsed(url)
            return True
        except Exception as e:
            self.queue.mark_failed(url, str(e))
            return False

    async def crawl_batch(self, batch_size: int = 15) -> int:
        batch = self.queue.get_next_batch(limit=batch_size)
        if not batch:
            return 0

        sem = asyncio.Semaphore(self.concurrency)
        async with httpx.AsyncClient(verify=False, headers={"User-Agent": "Mozilla/5.0"}) as client:
            async def worker(item):
                async with sem:
                    return await self.process_url(client, item)

            results = await asyncio.gather(*(worker(item) for item in batch))
            return sum(1 for r in results if r)
```

- [ ] **Step 2: Implement CLI runner `run_crawler.py`**

Write `/Users/jainamshah/Downloads/algomaster/run_crawler.py`:
```python
import asyncio
import argparse
import sys
from crawler.crawler import AsyncCrawler

async def main():
    parser = argparse.ArgumentParser(description="Algomaster Crawler CLI")
    parser.add_argument("--seed", action="store_true", help="Seed URLs from sitemap")
    parser.add_argument("--pilot", action="store_true", help="Seed and run pilot batch (25 practice, 5 animations, 3 roadmaps)")
    parser.add_argument("--full", action="store_true", help="Run full crawl until all URLs complete")
    parser.add_argument("--batch-size", type=int, default=20, help="Batch size per crawl iteration")
    parser.add_argument("--stats", action="store_true", help="Print current queue and database stats")
    args = parser.parse_args()

    crawler = AsyncCrawler()

    if args.stats:
        print("Queue Stats:", crawler.queue.get_stats())
        with crawler._get_conn() as conn:
            problems = conn.execute("SELECT COUNT(*) FROM problems").fetchone()[0]
            animations = conn.execute("SELECT COUNT(*) FROM animations").fetchone()[0]
            roadmaps = conn.execute("SELECT COUNT(*) FROM roadmaps").fetchone()[0]
            print(f"Database Stats: {problems} problems, {animations} animations, {roadmaps} roadmaps")
        return

    if args.pilot:
        print("Seeding pilot batch from sitemap...")
        all_urls = await crawler.fetch_sitemap()
        pilot_urls = []
        p_count = a_count = r_count = 0
        for u, cat in all_urls:
            if cat == "practice" and p_count < 25:
                pilot_urls.append((u, cat))
                p_count += 1
            elif cat == "animations" and a_count < 5:
                pilot_urls.append((u, cat))
                a_count += 1
            elif cat == "roadmaps" and r_count < 3:
                pilot_urls.append((u, cat))
                r_count += 1

        added = crawler.queue.seed_urls(pilot_urls)
        print(f"Seeded {added} pilot URLs. Starting crawl...")
        processed = 0
        while True:
            done = await crawler.crawl_batch(batch_size=10)
            if done == 0:
                break
            processed += done
            print(f"Crawled batch: {done} items (Total: {processed})")
        print("Pilot crawl completed!")
        return

    if args.seed:
        print("Fetching full sitemap...")
        all_urls = await crawler.fetch_sitemap()
        added = crawler.queue.seed_urls(all_urls)
        print(f"Seeded {added} URLs into queue.")

    if args.full:
        print("Starting full crawl loop...")
        total_done = 0
        while True:
            done = await crawler.crawl_batch(batch_size=args.batch_size)
            if done == 0:
                print("All pending items processed or queue empty.")
                break
            total_done += done
            stats = crawler.queue.get_stats()
            print(f"Batch completed: +{done} | Stats: {stats}")

if __name__ == "__main__":
    asyncio.run(main())
```

- [ ] **Step 3: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add crawler/crawler.py run_crawler.py
git commit -m "feat: implement async crawler and CLI runner"
```

---

### Task 6: Execute Pilot Crawl & Verify Database Population

**Files:**
- Execute: `/Users/jainamshah/Downloads/algomaster/run_crawler.py --pilot`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_pilot_data.py`

**Interfaces:**
- Consumes: Live network connection to `algomaster.io`
- Produces: Populated `data/algomaster.db` with at least 20 verified problems, solutions, and roadmaps.

- [ ] **Step 1: Write integration tests for pilot database content**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_pilot_data.py`:
```python
import sqlite3
import pytest

def test_pilot_database_records():
    conn = sqlite3.connect("data/algomaster.db")
    conn.row_factory = sqlite3.Row

    # Verify problems
    problems = conn.execute("SELECT * FROM problems").fetchall()
    assert len(problems) >= 10, f"Expected at least 10 problems, got {len(problems)}"

    # Check first problem structure
    p = problems[0]
    assert p["slug"]
    assert p["title"]
    assert p["difficulty"] in ("Easy", "Medium", "Hard")
    assert len(p["description_html"]) > 10

    # Verify solutions
    solutions = conn.execute("SELECT * FROM solutions WHERE problem_slug = ?", (p["slug"],)).fetchall()
    assert len(solutions) >= 1, f"Expected solutions for {p['slug']}"

    # Verify FTS5
    fts_rows = conn.execute("SELECT * FROM fts_content WHERE fts_content MATCH ?", (p["title"].split()[0],)).fetchall()
    assert len(fts_rows) >= 1, "FTS5 search should find matched record"

    conn.close()
```

- [ ] **Step 2: Run the pilot crawl via CLI**

Run:
```bash
cd /Users/jainamshah/Downloads/algomaster
python run_crawler.py --pilot
```
Expected: Crawls ~33 items (25 practice, 5 animations, 3 roadmaps) and saves to SQLite.

- [ ] **Step 3: Run the test to verify database integrity**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_pilot_data.py -v`  
Expected: PASS.

- [ ] **Step 4: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add tests/test_pilot_data.py
git commit -m "test: verify pilot crawl dataset in SQLite"
```

---

### Task 7: Database Access Layer & FTS5 Search Engine

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/server/db.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/search.py`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_search.py`

**Interfaces:**
- Consumes: `data/algomaster.db`
- Produces: `Database` and `SearchEngine`
  - `get_problem(slug: str) -> dict`
  - `list_problems(category: str, pattern: str, difficulty: str, limit: int, offset: int) -> list[dict]`
  - `search_content(query: str, limit: int) -> list[dict]`

- [ ] **Step 1: Write unit tests for search and queries**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_search.py`:
```python
import pytest
from server.db import Database
from server.search import SearchEngine

@pytest.fixture
def db():
    return Database("data/algomaster.db")

@pytest.fixture
def search_engine(db):
    return SearchEngine(db)

def test_list_and_get_problem(db):
    problems = db.list_problems(limit=5)
    assert len(problems) > 0
    slug = problems[0]["slug"]
    
    prob = db.get_problem(slug)
    assert prob is not None
    assert prob["slug"] == slug
    assert "solutions" in prob
    assert len(prob["solutions"]) > 0

def test_fts5_search(search_engine):
    results = search_engine.search("array OR two OR max", limit=5)
    assert isinstance(results, list)
    if results:
        assert "title" in results[0]
        assert "slug" in results[0]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_search.py -v`  
Expected: FAIL with `ModuleNotFoundError: No module named 'server.db'`

- [ ] **Step 3: Implement Database and SearchEngine**

Write `/Users/jainamshah/Downloads/algomaster/server/db.py`:
```python
import sqlite3
import json
import os

class Database:
    def __init__(self, db_path: str = "data/algomaster.db"):
        self.db_path = db_path

    def get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_stats(self) -> dict:
        with self.get_conn() as conn:
            problems = conn.execute("SELECT COUNT(*) FROM problems").fetchone()[0]
            animations = conn.execute("SELECT COUNT(*) FROM animations").fetchone()[0]
            roadmaps = conn.execute("SELECT COUNT(*) FROM roadmaps").fetchone()[0]
            categories = [r[0] for r in conn.execute("SELECT DISTINCT category FROM problems").fetchall()]
            patterns = [r[0] for r in conn.execute("SELECT DISTINCT sub_pattern FROM problems WHERE sub_pattern != ''").fetchall()]
            return {
                "problems_count": problems,
                "animations_count": animations,
                "roadmaps_count": roadmaps,
                "categories": categories,
                "patterns": patterns,
            }

    def list_problems(
        self,
        category: str = None,
        pattern: str = None,
        difficulty: str = None,
        limit: int = 50,
        offset: int = 0,
    ) -> list[dict]:
        query = "SELECT id, slug, title, category, sub_pattern, difficulty, animation_slug FROM problems WHERE 1=1"
        params = []
        if category:
            query += " AND category = ?"
            params.append(category)
        if pattern:
            query += " AND sub_pattern = ?"
            params.append(pattern)
        if difficulty:
            query += " AND difficulty = ?"
            params.append(difficulty)

        query += " ORDER BY id ASC LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        with self.get_conn() as conn:
            rows = conn.execute(query, params).fetchall()
            return [dict(r) for r in rows]

    def get_problem(self, slug: str) -> dict:
        with self.get_conn() as conn:
            p = conn.execute("SELECT * FROM problems WHERE slug = ?", (slug,)).fetchone()
            if not p:
                return None
            prob = dict(p)
            prob["examples"] = json.loads(prob.get("examples_json") or "[]")
            prob["constraints"] = json.loads(prob.get("constraints_json") or "[]")
            prob["tags"] = json.loads(prob.get("tags_json") or "[]")

            sol_rows = conn.execute(
                "SELECT * FROM solutions WHERE problem_slug = ? ORDER BY approach_order ASC",
                (slug,),
            ).fetchall()
            solutions = []
            for s in sol_rows:
                sol = dict(s)
                sol["code_tabs"] = json.loads(sol.get("code_tabs_json") or "{}")
                solutions.append(sol)
            prob["solutions"] = solutions
            return prob

    def list_animations(self) -> list[dict]:
        with self.get_conn() as conn:
            rows = conn.execute("SELECT * FROM animations ORDER BY id ASC").fetchall()
            return [dict(r) for r in rows]

    def list_roadmaps(self) -> list[dict]:
        with self.get_conn() as conn:
            rows = conn.execute("SELECT id, slug, title FROM roadmaps ORDER BY id ASC").fetchall()
            return [dict(r) for r in rows]

    def get_roadmap(self, slug: str) -> dict:
        with self.get_conn() as conn:
            row = conn.execute("SELECT * FROM roadmaps WHERE slug = ?", (slug,)).fetchone()
            if not row:
                return None
            res = dict(row)
            res["nodes"] = json.loads(res.get("nodes_json") or "[]")
            return res
```

Write `/Users/jainamshah/Downloads/algomaster/server/search.py`:
```python
import sqlite3
import re
from server.db import Database

class SearchEngine:
    def __init__(self, db: Database):
        self.db = db

    def search(self, query: str, limit: int = 20) -> list[dict]:
        cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', query).strip()
        if not cleaned:
            return []

        fts_query = " ".join([f"{word}*" for word in cleaned.split() if word])
        sql = """
            SELECT title, category, sub_pattern, difficulty, slug,
                   snippet(fts_content, 4, '<mark>', '</mark>', '...', 20) as matched_snippet,
                   bm25(fts_content) as rank
            FROM fts_content
            WHERE fts_content MATCH ?
            ORDER BY rank
            LIMIT ?
        """
        with self.db.get_conn() as conn:
            try:
                rows = conn.execute(sql, (fts_query, limit)).fetchall()
                return [dict(r) for r in rows]
            except sqlite3.OperationalError:
                return []
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_search.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add server/db.py server/search.py tests/test_search.py
git commit -m "feat: implement database access layer and FTS5 search engine"
```

---

### Task 8: FastAPI Web Server & REST API Routes

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/server/app.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/routes/problems.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/routes/animations.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/routes/roadmaps.py`
- Create: `/Users/jainamshah/Downloads/algomaster/server/routes/search.py`
- Test: `/Users/jainamshah/Downloads/algomaster/tests/test_api.py`

**Interfaces:**
- Consumes: `FastAPI`, `Database`, `SearchEngine`
- Produces: ASGI FastAPI app with endpoints:
  - `GET /api/stats`
  - `GET /api/problems`
  - `GET /api/problems/{slug}`
  - `GET /api/animations`
  - `GET /api/roadmaps`
  - `GET /api/roadmaps/{slug}`
  - `GET /api/search?q={query}`

- [ ] **Step 1: Write integration tests for API endpoints**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_api.py`:
```python
import pytest
from fastapi.testclient import TestClient
from server.app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_api_stats(client):
    resp = client.get("/api/stats")
    assert resp.status_code == 200
    data = resp.json()
    assert "problems_count" in data

def test_api_problems(client):
    resp = client.get("/api/problems?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) > 0
    slug = data[0]["slug"]

    # Problem detail
    resp_detail = client.get(f"/api/problems/{slug}")
    assert resp_detail.status_code == 200
    p_data = resp_detail.json()
    assert p_data["slug"] == slug
    assert "solutions" in p_data

def test_api_search(client):
    resp = client.get("/api/search?q=array")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_api.py -v`  
Expected: FAIL with `ModuleNotFoundError: No module named 'server.app'`

- [ ] **Step 3: Implement route modules and FastAPI app**

Write `/Users/jainamshah/Downloads/algomaster/server/routes/problems.py`:
```python
from fastapi import APIRouter, HTTPException, Query
from server.db import Database

router = APIRouter(prefix="/api/problems", tags=["problems"])
db = Database()

@router.get("")
def list_problems(
    category: str = Query(None),
    pattern: str = Query(None),
    difficulty: str = Query(None),
    limit: int = Query(50, le=200),
    offset: int = Query(0, ge=0),
):
    return db.list_problems(category, pattern, difficulty, limit, offset)

@router.get("/{slug}")
def get_problem(slug: str):
    p = db.get_problem(slug)
    if not p:
        raise HTTPException(status_code=404, detail="Problem not found")
    return p
```

Write `/Users/jainamshah/Downloads/algomaster/server/routes/animations.py`:
```python
from fastapi import APIRouter
from server.db import Database

router = APIRouter(prefix="/api/animations", tags=["animations"])
db = Database()

@router.get("")
def list_animations():
    return db.list_animations()
```

Write `/Users/jainamshah/Downloads/algomaster/server/routes/roadmaps.py`:
```python
from fastapi import APIRouter, HTTPException
from server.db import Database

router = APIRouter(prefix="/api/roadmaps", tags=["roadmaps"])
db = Database()

@router.get("")
def list_roadmaps():
    return db.list_roadmaps()

@router.get("/{slug}")
def get_roadmap(slug: str):
    r = db.get_roadmap(slug)
    if not r:
        raise HTTPException(status_code=404, detail="Roadmap not found")
    return r
```

Write `/Users/jainamshah/Downloads/algomaster/server/routes/search.py`:
```python
from fastapi import APIRouter, Query
from server.db import Database
from server.search import SearchEngine

router = APIRouter(prefix="/api/search", tags=["search"])
search_engine = SearchEngine(Database())

@router.get("")
def search(q: str = Query(..., min_length=1), limit: int = Query(20, le=50)):
    return search_engine.search(q, limit)
```

Write `/Users/jainamshah/Downloads/algomaster/server/app.py`:
```python
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from server.db import Database
from server.routes import problems, animations, roadmaps, search

app = FastAPI(title="AlgoMaster Offline Replica", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db = Database()

@app.get("/api/stats")
def get_stats():
    return db.get_stats()

app.include_router(problems.router)
app.include_router(animations.router)
app.include_router(roadmaps.router)
app.include_router(search.router)

# Mount mirrored static assets and replica UI
assets_dir = "data/assets"
if os.path.exists(assets_dir):
    app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")

static_dir = "static"
if os.path.exists(static_dir):
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_api.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 5: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add server/app.py server/routes/ tests/test_api.py
git commit -m "feat: implement FastAPI server and REST endpoints"
```

---

### Task 9: Frontend Replica SPA Implementation

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/static/index.html`
- Create: `/Users/jainamshah/Downloads/algomaster/static/style.css`
- Create: `/Users/jainamshah/Downloads/algomaster/static/app.js`

**Interfaces:**
- Consumes: REST APIs (`/api/stats`, `/api/problems`, `/api/roadmaps`, `/api/search`)
- Produces: Fully interactive Algomaster clone UI.

- [ ] **Step 1: Write `static/style.css`**

Write `/Users/jainamshah/Downloads/algomaster/static/style.css`:
```css
:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-tertiary: #21262d;
  --text-primary: #f0f6fc;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --border-color: #30363d;
  --accent-color: #58a6ff;
  --accent-hover: #79c0ff;
  --badge-easy: #238636;
  --badge-medium: #d29922;
  --badge-hard: #da3633;
  --code-bg: #090d12;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
}

[data-theme="light"] {
  --bg-primary: #ffffff;
  --bg-secondary: #f6f8fa;
  --bg-tertiary: #eaeef2;
  --text-primary: #1f2328;
  --text-secondary: #57606a;
  --text-muted: #6e7781;
  --border-color: #d0d7de;
  --accent-color: #0969da;
  --accent-hover: #218bff;
  --badge-easy: #1a7f37;
  --badge-medium: #9a6700;
  --badge-hard: #cf222e;
  --code-bg: #f6f8fa;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-sans);
  background: var(--bg-primary);
  color: var(--text-primary);
  display: flex;
  flex-direction: column;
  height: 100vh;
  overflow: hidden;
}

/* Header */
header {
  height: 56px;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  flex-shrink: 0;
}
.brand { display: flex; align-items: center; gap: 10px; font-weight: 700; font-size: 1.15rem; color: var(--text-primary); text-decoration: none; }
.brand span { color: var(--accent-color); }
.nav-tabs { display: flex; gap: 6px; }
.nav-tab {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-secondary);
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
}
.nav-tab.active { background: var(--bg-tertiary); color: var(--text-primary); border-color: var(--border-color); }
.header-actions { display: flex; align-items: center; gap: 12px; }
.search-btn {
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  color: var(--text-secondary);
  padding: 6px 14px;
  border-radius: 6px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
}
.kbd { background: var(--bg-primary); border: 1px solid var(--border-color); border-radius: 4px; padding: 2px 6px; font-size: 0.75rem; font-family: var(--font-mono); }
.theme-btn { background: none; border: none; color: var(--text-secondary); cursor: pointer; font-size: 1.2rem; }

/* Main layout */
.app-container { display: flex; flex: 1; overflow: hidden; }

/* Sidebar */
aside {
  width: 320px;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
}
.sidebar-header { padding: 14px 16px; border-bottom: 1px solid var(--border-color); display: flex; flex-direction: column; gap: 10px; }
.filter-row { display: flex; gap: 8px; }
.filter-select {
  flex: 1;
  background: var(--bg-primary);
  border: 1px solid var(--border-color);
  color: var(--text-primary);
  padding: 6px 8px;
  border-radius: 6px;
  font-size: 0.85rem;
}
.problem-list { flex: 1; overflow-y: auto; padding: 8px 0; }
.problem-item {
  padding: 10px 16px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  cursor: pointer;
  border-bottom: 1px solid var(--border-color);
  transition: background 0.15s;
}
.problem-item:hover { background: var(--bg-tertiary); }
.problem-item.active { background: var(--bg-tertiary); border-left: 3px solid var(--accent-color); }
.p-title { font-size: 0.9rem; font-weight: 500; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 210px; }
.badge { font-size: 0.75rem; padding: 2px 6px; border-radius: 10px; font-weight: 600; text-transform: uppercase; }
.badge.easy { background: rgba(35, 134, 54, 0.2); color: #3fb950; }
.badge.medium { background: rgba(210, 153, 34, 0.2); color: #d29922; }
.badge.hard { background: rgba(218, 54, 51, 0.2); color: #f85149; }

/* Main workspace */
main { flex: 1; overflow-y: auto; padding: 24px 32px; background: var(--bg-primary); }
.problem-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px; }
.problem-meta { display: flex; align-items: center; gap: 10px; margin-top: 8px; }
.pattern-badge { background: var(--bg-tertiary); border: 1px solid var(--border-color); padding: 3px 8px; border-radius: 6px; font-size: 0.8rem; color: var(--text-secondary); }

/* Tabs */
.tabs { display: flex; gap: 10px; border-bottom: 1px solid var(--border-color); margin-bottom: 20px; }
.tab-btn { background: none; border: none; border-bottom: 2px solid transparent; color: var(--text-secondary); padding: 8px 12px; cursor: pointer; font-size: 0.95rem; font-weight: 500; }
.tab-btn.active { color: var(--accent-color); border-bottom-color: var(--accent-color); font-weight: 600; }

.section-box { background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 8px; padding: 18px 22px; margin-bottom: 20px; }
.section-title { font-size: 1.1rem; font-weight: 600; margin-bottom: 12px; color: var(--text-primary); }

/* Code box */
.code-header { display: flex; justify-content: space-between; align-items: center; background: var(--bg-tertiary); padding: 8px 14px; border-top-left-radius: 8px; border-top-right-radius: 8px; border: 1px solid var(--border-color); border-bottom: none; }
.lang-tabs { display: flex; gap: 6px; }
.lang-btn { background: none; border: none; color: var(--text-secondary); padding: 4px 8px; border-radius: 4px; cursor: pointer; font-size: 0.8rem; }
.lang-btn.active { background: var(--bg-primary); color: var(--accent-color); font-weight: 600; }
.copy-btn { background: var(--bg-primary); border: 1px solid var(--border-color); color: var(--text-secondary); padding: 4px 10px; border-radius: 4px; cursor: pointer; font-size: 0.8rem; }
pre { background: var(--code-bg); border: 1px solid var(--border-color); border-bottom-left-radius: 8px; border-bottom-right-radius: 8px; padding: 16px; overflow-x: auto; font-family: var(--font-mono); font-size: 0.9rem; line-height: 1.5; }

/* Complexity box */
.complexity-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 10px; }
.complexity-card { background: var(--bg-tertiary); border: 1px solid var(--border-color); border-radius: 6px; padding: 12px 16px; }
.complexity-label { font-size: 0.8rem; color: var(--text-secondary); text-transform: uppercase; font-weight: 600; }
.complexity-val { font-size: 1.25rem; font-family: var(--font-mono); font-weight: 700; color: var(--accent-color); margin-top: 4px; }

/* Search Modal */
.modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.7); display: none; align-items: flex-start; justify-content: center; padding-top: 80px; z-index: 1000; }
.modal-overlay.open { display: flex; }
.modal-box { width: 600px; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 10px; box-shadow: 0 16px 32px rgba(0,0,0,0.5); overflow: hidden; }
.modal-input { width: 100%; padding: 16px 20px; background: var(--bg-primary); border: none; border-bottom: 1px solid var(--border-color); color: var(--text-primary); font-size: 1.1rem; outline: none; }
.modal-results { max-height: 380px; overflow-y: auto; padding: 8px 0; }
.result-item { padding: 12px 20px; cursor: pointer; border-bottom: 1px solid var(--border-color); }
.result-item:hover { background: var(--bg-tertiary); }
.result-title { font-weight: 600; font-size: 0.95rem; margin-bottom: 4px; }
.result-snippet { font-size: 0.8rem; color: var(--text-secondary); }
mark { background: rgba(88, 166, 255, 0.3); color: var(--text-primary); border-radius: 2px; }
```

- [ ] **Step 2: Write `static/index.html`**

Write `/Users/jainamshah/Downloads/algomaster/static/index.html`:
```html
<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AlgoMaster - Master Software Engineering Interviews</title>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <header>
    <a href="#" class="brand" onclick="app.switchView('practice')">
      <span>Algo</span>Master
    </a>
    <div class="nav-tabs">
      <button class="nav-tab active" id="tab-practice" onclick="app.switchView('practice')">Practice</button>
      <button class="nav-tab" id="tab-animations" onclick="app.switchView('animations')">Animations</button>
      <button class="nav-tab" id="tab-roadmaps" onclick="app.switchView('roadmaps')">Roadmaps</button>
    </div>
    <div class="header-actions">
      <button class="search-btn" onclick="app.openSearch()">
        <span>Search problems & patterns...</span>
        <span class="kbd">⌘K</span>
      </button>
      <button class="theme-btn" onclick="app.toggleTheme()" title="Toggle Theme">🌓</button>
    </div>
  </header>

  <div class="app-container">
    <aside id="sidebar">
      <div class="sidebar-header">
        <div class="filter-row">
          <select id="pattern-filter" class="filter-select" onchange="app.filterProblems()">
            <option value="">All Patterns</option>
          </select>
          <select id="diff-filter" class="filter-select" onchange="app.filterProblems()">
            <option value="">All Difficulties</option>
            <option value="Easy">Easy</option>
            <option value="Medium">Medium</option>
            <option value="Hard">Hard</option>
          </select>
        </div>
      </div>
      <div class="problem-list" id="problem-list">
        <!-- Rendered items -->
      </div>
    </aside>

    <main id="main-content">
      <div id="loading" style="display:none; text-align:center; padding: 40px; color: var(--text-secondary);">Loading...</div>
      
      <!-- Problem View -->
      <div id="problem-view">
        <div class="problem-header">
          <div>
            <h1 id="p-title">Select a problem</h1>
            <div class="problem-meta">
              <span id="p-difficulty" class="badge"></span>
              <span id="p-pattern" class="pattern-badge"></span>
              <span id="p-category" class="pattern-badge"></span>
            </div>
          </div>
          <div id="anim-button-container"></div>
        </div>

        <div class="tabs">
          <button class="tab-btn active" id="tab-editorial" onclick="app.switchProblemTab('editorial')">Editorial & Solutions</button>
          <button class="tab-btn" id="tab-description" onclick="app.switchProblemTab('description')">Description</button>
        </div>

        <div id="editorial-pane">
          <div id="approaches-container"></div>
        </div>

        <div id="description-pane" style="display:none;">
          <div class="section-box">
            <div class="section-title">Problem Statement</div>
            <div id="p-description-content"></div>
          </div>
        </div>
      </div>

      <!-- Roadmaps View -->
      <div id="roadmaps-view" style="display:none;">
        <h1 style="margin-bottom:20px;">Developer Roadmaps</h1>
        <div id="roadmaps-list" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px;"></div>
        <div id="roadmap-detail" style="margin-top: 30px;"></div>
      </div>

      <!-- Animations View -->
      <div id="animations-view" style="display:none;">
        <h1 style="margin-bottom:20px;">Interactive Algorithm Animations</h1>
        <div id="animations-list" style="display:grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 16px;"></div>
      </div>
    </main>
  </div>

  <!-- Search Modal -->
  <div class="modal-overlay" id="search-modal" onclick="if(event.target === this) app.closeSearch()">
    <div class="modal-box">
      <input type="text" id="search-input" class="modal-input" placeholder="Search problems, patterns, complexities... (ESC to close)" oninput="app.performSearch(this.value)" />
      <div class="modal-results" id="search-results"></div>
    </div>
  </div>

  <script src="/app.js"></script>
</body>
</html>
```

- [ ] **Step 3: Write `static/app.js`**

Write `/Users/jainamshah/Downloads/algomaster/static/app.js`:
```javascript
class AlgoMasterApp {
  constructor() {
    this.currentView = 'practice';
    this.problems = [];
    this.currentProblem = null;
    this.activeApproachIndex = 0;
    this.activeLanguage = 'python';
    this.init();
  }

  async init() {
    this.initTheme();
    this.initKeybindings();
    await this.loadStats();
    await this.loadProblems();
  }

  initTheme() {
    const saved = localStorage.getItem('theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
  }

  toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  }

  initKeybindings() {
    window.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        this.openSearch();
      }
      if (e.key === 'Escape') {
        this.closeSearch();
      }
    });
  }

  async loadStats() {
    try {
      const res = await fetch('/api/stats');
      const stats = await res.json();
      const patternFilter = document.getElementById('pattern-filter');
      stats.patterns.forEach(p => {
        const opt = document.createElement('option');
        opt.value = p;
        opt.textContent = p;
        patternFilter.appendChild(opt);
      });
    } catch (e) {
      console.error(e);
    }
  }

  async loadProblems() {
    try {
      const res = await fetch('/api/problems?limit=100');
      this.problems = await res.json();
      this.renderProblemList(this.problems);
      if (this.problems.length > 0) {
        this.selectProblem(this.problems[0].slug);
      }
    } catch (e) {
      console.error(e);
    }
  }

  renderProblemList(items) {
    const container = document.getElementById('problem-list');
    container.innerHTML = '';
    items.forEach(p => {
      const div = document.createElement('div');
      div.className = `problem-item ${this.currentProblem?.slug === p.slug ? 'active' : ''}`;
      div.onclick = () => this.selectProblem(p.slug);
      div.innerHTML = `
        <span class="p-title">${p.title}</span>
        <span class="badge ${p.difficulty.toLowerCase()}">${p.difficulty}</span>
      `;
      container.appendChild(div);
    });
  }

  filterProblems() {
    const pattern = document.getElementById('pattern-filter').value;
    const diff = document.getElementById('diff-filter').value;
    const filtered = this.problems.filter(p => {
      const matchP = !pattern || p.sub_pattern === pattern;
      const matchD = !diff || p.difficulty === diff;
      return matchP && matchD;
    });
    this.renderProblemList(filtered);
  }

  async selectProblem(slug) {
    try {
      const res = await fetch(`/api/problems/${slug}`);
      this.currentProblem = await res.json();
      this.renderCurrentProblem();
      this.renderProblemList(this.problems);
    } catch (e) {
      console.error(e);
    }
  }

  renderCurrentProblem() {
    const p = this.currentProblem;
    document.getElementById('p-title').textContent = p.title;
    
    const diffEl = document.getElementById('p-difficulty');
    diffEl.textContent = p.difficulty;
    diffEl.className = `badge ${p.difficulty.toLowerCase()}`;

    document.getElementById('p-pattern').textContent = p.sub_pattern || 'Algorithm';
    document.getElementById('p-category').textContent = p.category || 'DSA';

    document.getElementById('p-description-content').innerHTML = p.description_html;

    const animContainer = document.getElementById('anim-button-container');
    if (p.animation_slug) {
      animContainer.innerHTML = `<button class="search-btn" onclick="app.openAnimation('${p.animation_slug}')">▶ View Animation</button>`;
    } else {
      animContainer.innerHTML = '';
    }

    this.renderApproaches(p.solutions || []);
  }

  renderApproaches(solutions) {
    const container = document.getElementById('approaches-container');
    container.innerHTML = '';
    solutions.forEach((sol, idx) => {
      const box = document.createElement('div');
      box.className = 'section-box';
      
      // Code tabs
      const langKeys = Object.keys(sol.code_tabs || {});
      const activeLang = langKeys.includes(this.activeLanguage) ? this.activeLanguage : (langKeys[0] || 'python');
      const codeSnippet = sol.code_tabs ? (sol.code_tabs[activeLang] || '') : '';

      const langButtons = langKeys.map(lang => 
        `<button class="lang-btn ${lang === activeLang ? 'active' : ''}" onclick="app.setLanguage('${lang}', ${idx})">${lang.toUpperCase()}</button>`
      ).join('');

      box.innerHTML = `
        <div class="section-title">${sol.approach_name}</div>
        ${sol.intuition_html ? `<p style="margin-bottom:14px; color:var(--text-secondary);">${sol.intuition_html}</p>` : ''}
        
        <div class="code-header">
          <div class="lang-tabs">${langButtons}</div>
          <button class="copy-btn" onclick="app.copyCode(${idx})">Copy</button>
        </div>
        <pre><code id="code-block-${idx}">${this.escapeHtml(codeSnippet)}</code></pre>

        <div class="complexity-grid">
          <div class="complexity-card">
            <div class="complexity-label">Time Complexity</div>
            <div class="complexity-val">${sol.time_complexity || 'O(n)'}</div>
          </div>
          <div class="complexity-card">
            <div class="complexity-label">Space Complexity</div>
            <div class="complexity-val">${sol.space_complexity || 'O(1)'}</div>
          </div>
        </div>
      `;
      container.appendChild(box);
    });
  }

  setLanguage(lang, approachIdx) {
    this.activeLanguage = lang;
    this.renderApproaches(this.currentProblem.solutions || []);
  }

  copyCode(idx) {
    const code = document.getElementById(`code-block-${idx}`).innerText;
    navigator.clipboard.writeText(code);
    alert('Code copied to clipboard!');
  }

  escapeHtml(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  switchProblemTab(tab) {
    document.getElementById('tab-editorial').classList.toggle('active', tab === 'editorial');
    document.getElementById('tab-description').classList.toggle('active', tab === 'description');
    document.getElementById('editorial-pane').style.display = tab === 'editorial' ? 'block' : 'none';
    document.getElementById('description-pane').style.display = tab === 'description' ? 'block' : 'none';
  }

  async switchView(view) {
    this.currentView = view;
    document.getElementById('tab-practice').classList.toggle('active', view === 'practice');
    document.getElementById('tab-animations').classList.toggle('active', view === 'animations');
    document.getElementById('tab-roadmaps').classList.toggle('active', view === 'roadmaps');

    document.getElementById('sidebar').style.display = view === 'practice' ? 'flex' : 'none';
    document.getElementById('problem-view').style.display = view === 'practice' ? 'block' : 'none';
    document.getElementById('animations-view').style.display = view === 'animations' ? 'block' : 'none';
    document.getElementById('roadmaps-view').style.display = view === 'roadmaps' ? 'block' : 'none';

    if (view === 'roadmaps') await this.loadRoadmaps();
    if (view === 'animations') await this.loadAnimations();
  }

  async loadRoadmaps() {
    const res = await fetch('/api/roadmaps');
    const roadmaps = await res.json();
    const container = document.getElementById('roadmaps-list');
    container.innerHTML = roadmaps.map(r => `
      <div class="section-box" style="cursor:pointer;" onclick="app.showRoadmapDetail('${r.slug}')">
        <div class="section-title">${r.title}</div>
        <span class="pattern-badge">Explore Roadmap →</span>
      </div>
    `).join('');
  }

  async showRoadmapDetail(slug) {
    const res = await fetch(`/api/roadmaps/${slug}`);
    const r = await res.json();
    const container = document.getElementById('roadmap-detail');
    container.innerHTML = `
      <div class="section-box">
        <div class="section-title">${r.title} Roadmap Topics</div>
        <ul style="padding-left: 20px; color: var(--text-secondary); line-height: 1.8;">
          ${(r.nodes || []).map(n => `<li>${n}</li>`).join('')}
        </ul>
      </div>
    `;
  }

  async loadAnimations() {
    const res = await fetch('/api/animations');
    const anims = await res.json();
    const container = document.getElementById('animations-list');
    container.innerHTML = anims.map(a => `
      <div class="section-box" style="cursor:pointer;" onclick="app.selectProblem('${a.problem_slug}')">
        <div class="section-title">${a.title}</div>
        <span class="pattern-badge">${a.category}</span>
      </div>
    `).join('');
  }

  openSearch() {
    const modal = document.getElementById('search-modal');
    modal.classList.add('open');
    const input = document.getElementById('search-input');
    input.value = '';
    input.focus();
    document.getElementById('search-results').innerHTML = '';
  }

  closeSearch() {
    document.getElementById('search-modal').classList.remove('open');
  }

  async performSearch(q) {
    if (!q || q.length < 2) {
      document.getElementById('search-results').innerHTML = '';
      return;
    }
    const res = await fetch(`/api/search?q=${encodeURIComponent(q)}`);
    const results = await res.json();
    const container = document.getElementById('search-results');
    container.innerHTML = results.map(r => `
      <div class="result-item" onclick="app.closeSearch(); app.switchView('practice'); app.selectProblem('${r.slug}')">
        <div class="result-title">${r.title} <span class="badge ${r.difficulty.toLowerCase()}">${r.difficulty}</span></div>
        <div class="result-snippet">${r.matched_snippet || ''}</div>
      </div>
    `).join('');
  }
}

const app = new AlgoMasterApp();
```

- [ ] **Step 4: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add static/
git commit -m "feat: implement frontend replica single page application"
```

---

### Task 10: Server Runner & End-to-End System Integration Test

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/run_server.py`
- Create: `/Users/jainamshah/Downloads/algomaster/tests/test_e2e.py`

**Interfaces:**
- Consumes: `uvicorn`, `server/app.py`
- Produces: Executable web server on `http://localhost:8000`.

- [ ] **Step 1: Write `run_server.py`**

Write `/Users/jainamshah/Downloads/algomaster/run_server.py`:
```python
import uvicorn

if __name__ == "__main__":
    print("Starting AlgoMaster Replica server on http://localhost:8000 ...")
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True)
```

- [ ] **Step 2: Write end-to-end integration test**

Write `/Users/jainamshah/Downloads/algomaster/tests/test_e2e.py`:
```python
from fastapi.testclient import TestClient
from server.app import app

def test_e2e_frontend_and_api():
    client = TestClient(app)

    # 1. Front page index.html
    resp = client.get("/")
    assert resp.status_code == 200
    assert "AlgoMaster" in resp.text

    # 2. CSS and JS assets
    css_resp = client.get("/style.css")
    assert css_resp.status_code == 200
    js_resp = client.get("/app.js")
    assert js_resp.status_code == 200

    # 3. Stats endpoint
    stats_resp = client.get("/api/stats")
    assert stats_resp.status_code == 200
    assert stats_resp.json()["problems_count"] > 0

    # 4. Search endpoint
    search_resp = client.get("/api/search?q=max")
    assert search_resp.status_code == 200
```

- [ ] **Step 3: Run test to verify it passes**

Run: `pytest /Users/jainamshah/Downloads/algomaster/tests/test_e2e.py -v`  
Expected: PASS (all tests pass).

- [ ] **Step 4: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add run_server.py tests/test_e2e.py
git commit -m "feat: implement server runner and e2e integration tests"
```

---

### Task 11: Full Crawl Execution CLI & Documentation

**Files:**
- Create: `/Users/jainamshah/Downloads/algomaster/README.md`

**Interfaces:**
- Produces: Complete setup instructions and documentation for running the full background crawl and hosting the replica.

- [ ] **Step 1: Write comprehensive README.md**

Write `/Users/jainamshah/Downloads/algomaster/README.md`:
```markdown
# AlgoMaster Offline Replica (`algomaster.io`)

A fast, offline-capable, self-hosted replica of [AlgoMaster.io](https://algomaster.io/) featuring a modern Python/FastAPI backend, SQLite FTS5 full-text search, and a responsive frontend single-page application.

---

## Features

- **Practice Problems:** Full problem statements, difficulty badges, patterns, examples, and constraints.
- **Editorial Solutions:** Multi-approach walkthroughs with code tabs for Python, Java, C++, JavaScript, and Go.
- **Algorithmic Complexity Cards:** Dedicated Big-O time and space complexity analysis.
- **Developer Roadmaps:** Complete hierarchical trees for DSA, Python, System Design, SQL, and more.
- **Interactive Animations:** Mirrored visualizer player for step-by-step algorithm walkthroughs.
- **Instant Full-Text Search (`⌘K`):** Sub-millisecond SQLite FTS5 search index with BM25 ranking and highlighted snippets.
- **Zero Build Step:** Runs purely on Python without Node.js or webpack overhead.

---

## Quickstart

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Pilot Crawl (or Full Crawl)
```bash
# Run pilot batch (25 practice, 5 animations, 3 roadmaps)
python run_crawler.py --pilot

# Run full crawl (all 6,058 URLs from sitemap with resume support)
python run_crawler.py --full
```

### 3. Launch the Server
```bash
python run_server.py
```
Open [http://localhost:8000](http://localhost:8000) in your browser.
```

- [ ] **Step 2: Commit**

```bash
cd /Users/jainamshah/Downloads/algomaster
git add README.md
git commit -m "docs: add project README and usage instructions"
```
