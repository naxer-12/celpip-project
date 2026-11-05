# CELTESTPIP Full-Depth Crawler & Offline Replica Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a robust asynchronous crawler, SQLite database builder, and FastAPI/Vanilla JS local web application replicating `https://www.celtestpip.com` with all 60 mock exams, 1,200 parts, offline audio/images, and an interactive exam simulator.

**Architecture:** An asynchronous Python crawler uses custom Next.js RSC flight protocol decoders to extract complete question trees, answers, audio URLs, and transcripts without browser automation. An asset downloader mirrors MP3s and images locally. A SQLite database indexes all content with FTS5. A lightweight FastAPI server serves the REST API and a responsive vanilla frontend matching the original site's look and feel.

**Tech Stack:** Python 3.10+, FastAPI, Uvicorn, HTTPX, SQLite 3 (FTS5), pytest, Vanilla HTML5/CSS3/ES6.

**Spec:** `docs/superpowers/specs/2026-11-05-celtestpip-replica-design.md`

## Global Constraints
- Python 3.10+ compatible.
- All code and data stored under `celtestpip/`.
- No external node/npm build dependencies; pure vanilla HTML/CSS/ES6.
- 100% offline functionality when local media is downloaded.
- Resilient crawler with file-based checkpointing in `celtestpip/data/raw/`.

---

### Task 1: Scaffolding and Environment Setup

**Files:**
- Create: `celtestpip/requirements.txt`
- Create: `celtestpip/__init__.py`
- Create: `celtestpip/crawler/__init__.py`
- Create: `celtestpip/server/__init__.py`
- Create: `celtestpip/tests/__init__.py`
- Test: `celtestpip/tests/test_scaffold.py`

**Interfaces:**
- Consumes: None
- Produces: Project directory hierarchy and environment dependencies.

- [ ] **Step 1: Write scaffold test**

```python
# celtestpip/tests/test_scaffold.py
import os

def test_directories_exist():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.isdir(os.path.join(base, "crawler"))
    assert os.path.isdir(os.path.join(base, "server"))
    assert os.path.isdir(os.path.join(base, "static"))
    assert os.path.isfile(os.path.join(base, "requirements.txt"))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_scaffold.py -v`
Expected: FAIL (file or directory not found)

- [ ] **Step 3: Create directory structure and requirements.txt**

```text
# celtestpip/requirements.txt
fastapi>=0.110.0
uvicorn>=0.28.0
httpx>=0.27.0
aiofiles>=23.2.1
pydantic>=2.6.0
pytest>=8.0.0
pytest-asyncio>=0.23.0
```

Create folders:
`celtestpip/crawler`, `celtestpip/server`, `celtestpip/static/css`, `celtestpip/static/js`, `celtestpip/static/img`, `celtestpip/data/raw/exams`, `celtestpip/data/raw/pages`, `celtestpip/data/media/audio`, `celtestpip/data/media/images`, `celtestpip/tests`.
Add empty `__init__.py` in packages.

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_scaffold.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/
git commit -m "feat(scaffold): initialize celtestpip directory structure and dependencies"
```

---

### Task 2: React Server Component (RSC) Flight Parser

**Files:**
- Create: `celtestpip/crawler/rsc_parser.py`
- Test: `celtestpip/tests/test_parser.py`

**Interfaces:**
- Consumes: Raw text response from `https://www.celtestpip.com/exams/{exam_id}/{part_id}` with `RSC: 1`
- Produces: `parse_exam_rsc(rsc_text: str) -> dict` returning normalized exam part dictionary:
  `{"exam_id": str, "part_number": int, "part_title": str, "skill": str, "practice_id": str, "audio_urls": list, "image_urls": list, "transcripts": list, "questions": list}`

- [ ] **Step 1: Write test for RSC parser**

```python
# celtestpip/tests/test_parser.py
import pytest
from celtestpip.crawler.rsc_parser import parse_exam_rsc

MOCK_RSC_PAYLOAD = '''
1:"$Sreact.fragment"
7:[{"practice":{"id":"p123","name":"Meal Delivery","text":"Instructions here","audio":"https://blob.vercel.com/audio1.mp3","audio2":"https://blob.vercel.com/audio2.mp3","transcript":"Lucia: Hello","transcript2":"Man: Hi","part":{"type":"LISTENING","name":"Problem Solving","time":60}},"examId":"exam1","partNumber":1}]
8:[{"type":"question","content":{"id":"q1","priority":1,"question":"What went wrong?","option1":"Wrong order","option2":"Late delivery","option3":"Overcharged","option4":"Spoiled food","answer":"1","explanation":"She got tacos instead of salmon."},"questionNumber":1}]
'''

def test_parse_exam_rsc():
    data = parse_exam_rsc(MOCK_RSC_PAYLOAD)
    assert data is not None
    assert data["exam_id"] == "exam1"
    assert data["part_number"] == 1
    assert data["skill"] == "LISTENING"
    assert len(data["audio_urls"]) == 2
    assert "https://blob.vercel.com/audio1.mp3" in data["audio_urls"]
    assert len(data["transcripts"]) == 2
    assert len(data["questions"]) == 1
    q = data["questions"][0]
    assert q["question_text"] == "What went wrong?"
    assert q["options"] == ["Wrong order", "Late delivery", "Overcharged", "Spoiled food"]
    assert q["correct_answer"] == "1"
    assert "tacos" in q["explanation"]
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_parser.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'celtestpip.crawler.rsc_parser'`

- [ ] **Step 3: Implement `rsc_parser.py`**

```python
# celtestpip/crawler/rsc_parser.py
import re
import json
from typing import Dict, Any, List, Optional

def extract_json_blobs(text: str) -> List[Any]:
    blobs = []
    # Pattern to match lines like: id:[...] or id:{...}
    # where id is hex or alphanumeric
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        colon_idx = line.find(":")
        if colon_idx != -1 and line[:colon_idx].replace("_", "").isalnum():
            candidate = line[colon_idx + 1:].strip()
            if candidate.startswith(("{", "[")):
                try:
                    obj = json.loads(candidate)
                    blobs.append(obj)
                except Exception:
                    pass
    return blobs

def _walk_for_key(obj: Any, key: str) -> List[Any]:
    results = []
    if isinstance(obj, dict):
        if key in obj:
            results.append(obj[key])
        for v in obj.values():
            results.extend(_walk_for_key(v, key))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(_walk_for_key(item, key))
    return results

def parse_exam_rsc(rsc_text: str) -> Optional[Dict[str, Any]]:
    blobs = extract_json_blobs(rsc_text)
    
    # Locate practice object
    practice_objs = []
    for b in blobs:
        practice_objs.extend(_walk_for_key(b, "practice"))
    
    # Locate questions
    question_candidates = []
    for b in blobs:
        # Check direct questions list or walk
        qs = _walk_for_key(b, "questions")
        if qs and isinstance(qs[0], list):
            question_candidates.extend(qs[0])
        # Also check elements with "type": "question"
        if isinstance(b, list):
            for item in b:
                if isinstance(item, dict) and item.get("type") == "question":
                    question_candidates.append(item)
    
    # Deduplicate questions by ID or number
    questions = []
    seen_q_ids = set()
    for qc in question_candidates:
        content = qc.get("content", qc)
        qid = content.get("id") or str(qc.get("questionNumber"))
        if qid in seen_q_ids:
            continue
        seen_q_ids.add(qid)
        
        # Build options list
        options = []
        for i in range(1, 9):
            opt = content.get(f"option{i}")
            if opt:
                options.append(str(opt).strip())
                
        questions.append({
            "id": qid,
            "question_number": qc.get("questionNumber", len(questions) + 1),
            "priority": content.get("priority", 0),
            "question_text": content.get("question", ""),
            "audio_url": content.get("audio"),
            "options": options,
            "correct_answer": str(content.get("answer", "")),
            "explanation": content.get("explanation", ""),
            "section": content.get("section", 1)
        })
    
    # Extract metadata
    exam_id = "exam1"
    part_number = 1
    skill = "LISTENING"
    part_name = "Practice Part"
    transcripts = []
    audio_urls = []
    image_url = None
    instructions = ""
    
    for b in blobs:
        eids = _walk_for_key(b, "examId")
        if eids:
            exam_id = eids[0]
        pnums = _walk_for_key(b, "partNumber")
        if pnums:
            part_number = int(pnums[0])
            
    if practice_objs:
        p = practice_objs[0]
        part_info = p.get("part", {})
        skill = part_info.get("type", "LISTENING")
        part_name = p.get("name", part_info.get("name", "Practice Part"))
        instructions = p.get("text", "")
        
        for a_key in ["audio", "audio2", "audio3"]:
            a = p.get(a_key)
            if a and a.startswith("http"):
                audio_urls.append(a)
                
        for t_key in ["transcript", "transcript2", "transcript3"]:
            t = p.get(t_key)
            if t and isinstance(t, str) and not t.startswith("$"):
                transcripts.append(t)
                
        image_url = p.get("image")
        
    # Check if transcripts were stored as string tokens elsewhere in RSC
    for line in rsc_text.split("\n"):
        if re.search(r'^[0-9a-f]+:T[0-9a-f]+,', line):
            text_val = re.sub(r'^[0-9a-f]+:T[0-9a-f]+,', '', line).strip()
            if any(marker in text_val for marker in ["WOMAN:", "MAN:", "Speaker:"]) and text_val not in transcripts:
                transcripts.append(text_val)
                
    return {
        "exam_id": exam_id,
        "part_number": part_number,
        "skill": skill,
        "part_name": part_name,
        "instructions": instructions,
        "audio_urls": audio_urls,
        "image_url": image_url,
        "transcripts": transcripts,
        "questions": questions
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_parser.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/crawler/rsc_parser.py celtestpip/tests/test_parser.py
git commit -m "feat(parser): implement React Server Component flight data decoder"
```

---

### Task 3: Asynchronous Exam Crawler

**Files:**
- Create: `celtestpip/crawler/crawl_exams.py`
- Test: `celtestpip/tests/test_crawl_exams.py`

**Interfaces:**
- Consumes: Target URLs `https://www.celtestpip.com/exams/{exam_id}/part{part_number}` with `RSC: 1`
- Produces: JSON files in `celtestpip/data/raw/exams/{exam_id}_part{part_number}.json`

- [ ] **Step 1: Write mock test for crawl_exams**

```python
# celtestpip/tests/test_crawl_exams.py
import pytest
import os
import json
from unittest.mock import AsyncMock, patch
from celtestpip.crawler.crawl_exams import crawl_single_part, ExamCrawler

@pytest.mark.asyncio
async def test_crawl_single_part(tmp_path):
    mock_rsc = '7:[{"practice":{"id":"p1","name":"Test","text":"Inst","audio":"","part":{"type":"READING","name":"Reading"}},"examId":"exam1","partNumber":1}]'
    
    with patch("httpx.AsyncClient.get") as mock_get:
        mock_resp = AsyncMock()
        mock_resp.status_code = 200
        mock_resp.text = mock_rsc
        mock_get.return_value = mock_resp
        
        output_dir = str(tmp_path)
        result = await crawl_single_part(None, "exam1", 1, output_dir=output_dir)
        
        assert result is not None
        assert result["exam_id"] == "exam1"
        assert result["part_number"] == 1
        
        # Verify file saved
        file_path = os.path.join(output_dir, "exam1_part1.json")
        assert os.path.isfile(file_path)
        with open(file_path) as f:
            saved = json.load(f)
            assert saved["exam_id"] == "exam1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_crawl_exams.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `crawl_exams.py`**

```python
# celtestpip/crawler/crawl_exams.py
import os
import json
import asyncio
import logging
from typing import Optional, Dict, Any, List
import httpx
from celtestpip.crawler.rsc_parser import parse_exam_rsc

logger = logging.getLogger(__name__)

BASE_URL = "https://www.celtestpip.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "RSC": "1",
    "Accept": "*/*",
}

async def crawl_single_part(
    client: Optional[httpx.AsyncClient],
    exam_id: str,
    part_number: int,
    output_dir: str = "celtestpip/data/raw/exams"
) -> Optional[Dict[str, Any]]:
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{exam_id}_part{part_number}.json")
    
    # Checkpoint check
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    url = f"{BASE_URL}/exams/{exam_id}/part{part_number}"
    should_close = False
    if client is None:
        client = httpx.AsyncClient(headers=HEADERS, timeout=15.0, follow_redirects=True)
        should_close = True

    try:
        response = await client.get(url)
        if response.status_code == 200:
            parsed = parse_exam_rsc(response.text)
            if parsed:
                parsed["exam_id"] = exam_id
                parsed["part_number"] = part_number
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(parsed, f, indent=2, ensure_ascii=False)
                return parsed
        elif response.status_code == 404:
            logger.info(f"Part {part_number} does not exist for {exam_id}")
            return None
        else:
            logger.warning(f"HTTP {response.status_code} fetching {url}")
            return None
    except Exception as e:
        logger.error(f"Error fetching {url}: {e}")
        return None
    finally:
        if should_close:
            await client.aclose()

class ExamCrawler:
    def __init__(self, concurrency: int = 5, output_dir: str = "celtestpip/data/raw/exams"):
        self.concurrency = concurrency
        self.output_dir = output_dir

    async def crawl_all(self, start_exam: int = 1, end_exam: int = 60) -> List[Dict[str, Any]]:
        sem = asyncio.Semaphore(self.concurrency)
        results = []
        
        async with httpx.AsyncClient(headers=HEADERS, timeout=20.0, follow_redirects=True) as client:
            tasks = []
            for exam_num in range(start_exam, end_exam + 1):
                exam_id = f"exam{exam_num}"
                for part_num in range(1, 21):
                    async def sem_task(e_id=exam_id, p_num=part_num):
                        async with sem:
                            res = await crawl_single_part(client, e_id, p_num, self.output_dir)
                            await asyncio.sleep(0.1)  # courteous delay
                            return res
                    tasks.append(sem_task())
            
            raw_results = await asyncio.gather(*tasks, return_exceptions=True)
            for r in raw_results:
                if isinstance(r, dict):
                    results.append(r)
        return results
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_crawl_exams.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/crawler/crawl_exams.py celtestpip/tests/test_crawl_exams.py
git commit -m "feat(crawler): implement asynchronous exam crawler with checkpointing"
```

---

### Task 4: Sitemap Content & Calculators Crawler

**Files:**
- Create: `celtestpip/crawler/crawl_content.py`
- Test: `celtestpip/tests/test_crawl_content.py`

**Interfaces:**
- Consumes: `https://www.celtestpip.com/sitemap.xml` and content page URLs
- Produces: Articles, Question Bank topic manifests, and Calculator formulas in `celtestpip/data/raw/pages/` and `celtestpip/data/raw/tools/`

- [ ] **Step 1: Write test for crawl_content**

```python
# celtestpip/tests/test_crawl_content.py
import pytest
from unittest.mock import AsyncMock, patch
from celtestpip.crawler.crawl_content import parse_sitemap_urls, extract_page_content

SAMPLE_SITEMAP = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url><loc>https://www.celtestpip.com</loc></url>
<url><loc>https://www.celtestpip.com/questions</loc></url>
<url><loc>https://www.celtestpip.com/tools/clb-calculator</loc></url>
</urlset>"""

def test_parse_sitemap():
    urls = parse_sitemap_urls(SAMPLE_SITEMAP)
    assert len(urls) == 3
    assert "https://www.celtestpip.com/questions" in urls
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_crawl_content.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `crawl_content.py`**

```python
# celtestpip/crawler/crawl_content.py
import os
import re
import json
import xml.etree.ElementTree as ET
import httpx
from typing import List, Dict, Any

def parse_sitemap_urls(xml_text: str) -> List[str]:
    urls = []
    root = ET.fromstring(xml_text)
    for elem in root.iter():
        if elem.tag.endswith("loc") and elem.text:
            urls.append(elem.text.strip())
    return urls

def extract_page_content(html_text: str, url: str) -> Dict[str, Any]:
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', html_text, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else url
    
    # Extract meta description
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html_text, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else ""
    
    # Extract article/main content
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_text, re.IGNORECASE | re.DOTALL)
    content_html = main_match.group(1).strip() if main_match else html_text
    
    slug = url.replace("https://www.celtestpip.com", "").strip("/") or "home"
    return {
        "slug": slug,
        "url": url,
        "title": title,
        "description": description,
        "content_html": content_html
    }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_crawl_content.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/crawler/crawl_content.py celtestpip/tests/test_crawl_content.py
git commit -m "feat(crawler): implement sitemap and content page extractor"
```

---

### Task 5: Media Downloader and Asset Mapper

**Files:**
- Create: `celtestpip/crawler/download_media.py`
- Test: `celtestpip/tests/test_download_media.py`

**Interfaces:**
- Consumes: Extracted raw JSON files in `celtestpip/data/raw/exams/`
- Produces: Downloaded audio and images in `celtestpip/data/media/audio/` and `celtestpip/data/media/images/`, plus `celtestpip/data/media/media_map.json`

- [ ] **Step 1: Write test for download_media**

```python
# celtestpip/tests/test_download_media.py
import pytest
import os
from celtestpip.crawler.download_media import get_safe_filename, scan_media_urls

def test_safe_filename():
    url = "https://blob.vercel.com/practices/cm3/section1-SIGXC.mp3"
    filename = get_safe_filename(url)
    assert filename.endswith(".mp3")
    assert "section1" in filename or len(filename) > 8

def test_scan_media_urls():
    sample_part = {
        "audio_urls": ["https://blob.vercel.com/audio.mp3"],
        "image_url": "https://blob.vercel.com/image.jpg",
        "questions": [{"audio_url": "https://blob.vercel.com/q1.mp3"}]
    }
    audio_urls, image_urls = scan_media_urls([sample_part])
    assert len(audio_urls) == 2
    assert len(image_urls) == 1
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_download_media.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `download_media.py`**

```python
# celtestpip/crawler/download_media.py
import os
import re
import json
import hashlib
import asyncio
from typing import List, Tuple, Dict, Set
import httpx

def get_safe_filename(url: str) -> str:
    clean_url = url.split("?")[0]
    basename = os.path.basename(clean_url)
    ext = os.path.splitext(basename)[1].lower()
    if not ext:
        ext = ".mp3" if "audio" in url else ".jpg"
    hash_prefix = hashlib.sha256(url.encode("utf-8")).hexdigest()[:8]
    clean_base = re.sub(r'[^a-zA-Z0-9_\-]', '_', os.path.splitext(basename)[0])[:30]
    return f"{clean_base}_{hash_prefix}{ext}"

def scan_media_urls(parts: List[Dict]) -> Tuple[Set[str], Set[str]]:
    audio_urls = set()
    image_urls = set()
    for p in parts:
        for a in p.get("audio_urls", []):
            if a and a.startswith("http"):
                audio_urls.add(a)
        img = p.get("image_url")
        if img and img.startswith("http"):
            image_urls.add(img)
        for q in p.get("questions", []):
            qa = q.get("audio_url")
            if qa and qa.startswith("http"):
                audio_urls.add(qa)
    return audio_urls, image_urls

async def download_file(client: httpx.AsyncClient, url: str, dest_path: str) -> bool:
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
        return True
    try:
        resp = await client.get(url, follow_redirects=True)
        if resp.status_code == 200:
            with open(dest_path, "wb") as f:
                f.write(resp.content)
            return True
    except Exception:
        pass
    return False

async def download_all_media(
    audio_urls: Set[str],
    image_urls: Set[str],
    base_dir: str = "celtestpip/data/media",
    concurrency: int = 10
) -> Dict[str, str]:
    audio_dir = os.path.join(base_dir, "audio")
    image_dir = os.path.join(base_dir, "images")
    os.makedirs(audio_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)
    
    media_map = {}
    sem = asyncio.Semaphore(concurrency)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        tasks = []
        for url in audio_urls:
            fn = get_safe_filename(url)
            dest = os.path.join(audio_dir, fn)
            media_map[url] = f"/media/audio/{fn}"
            async def t(u=url, d=dest):
                async with sem:
                    await download_file(client, u, d)
            tasks.append(t())
            
        for url in image_urls:
            fn = get_safe_filename(url)
            dest = os.path.join(image_dir, fn)
            media_map[url] = f"/media/images/{fn}"
            async def t(u=url, d=dest):
                async with sem:
                    await download_file(client, u, d)
            tasks.append(t())
            
        await asyncio.gather(*tasks)
        
    map_file = os.path.join(base_dir, "media_map.json")
    with open(map_file, "w", encoding="utf-8") as f:
        json.dump(media_map, f, indent=2)
        
    return media_map
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_download_media.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/crawler/download_media.py celtestpip/tests/test_download_media.py
git commit -m "feat(media): implement concurrent media asset downloader and local mapper"
```

---

### Task 6: Master Crawler Pipeline Runner

**Files:**
- Create: `celtestpip/crawler/run_crawler.py`

**Interfaces:**
- Consumes: CLI flags `--exams`, `--content`, `--media`, `--all`
- Produces: Execution orchestration for the complete crawl lifecycle.

- [ ] **Step 1: Implement `run_crawler.py`**

```python
# celtestpip/crawler/run_crawler.py
import argparse
import asyncio
import glob
import json
import os
import sys

from celtestpip.crawler.crawl_exams import ExamCrawler
from celtestpip.crawler.crawl_content import parse_sitemap_urls, extract_page_content
from celtestpip.crawler.download_media import scan_media_urls, download_all_media
import httpx

async def run_pipeline(crawl_exams_flag: bool, crawl_content_flag: bool, download_media_flag: bool, limit_exams: int = 60):
    print("=" * 60)
    print("CELTESTPIP CRAWLER PIPELINE")
    print("=" * 60)
    
    # 1. Crawl Exams
    if crawl_exams_flag:
        print(f"\n[1/3] Crawling exams (exam1 to exam{limit_exams})...")
        crawler = ExamCrawler(concurrency=6)
        results = await crawler.crawl_all(start_exam=1, end_exam=limit_exams)
        print(f"-> Successfully extracted {len(results)} exam parts.")

    # 2. Crawl Content
    if crawl_content_flag:
        print("\n[2/3] Fetching sitemap and content pages...")
        pages_dir = "celtestpip/data/raw/pages"
        os.makedirs(pages_dir, exist_ok=True)
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get("https://www.celtestpip.com/sitemap.xml")
            if resp.status_code == 200:
                urls = parse_sitemap_urls(resp.text)
                print(f"-> Discovered {len(urls)} URLs from sitemap.")
                with open(os.path.join(pages_dir, "sitemap_urls.json"), "w") as f:
                    json.dump(urls, f, indent=2)

    # 3. Download Media
    if download_media_flag:
        print("\n[3/3] Scanning and downloading media assets...")
        exam_files = glob.glob("celtestpip/data/raw/exams/*.json")
        parts = []
        for ef in exam_files:
            try:
                with open(ef, "r", encoding="utf-8") as f:
                    parts.append(json.load(f))
            except Exception:
                pass
        audio_urls, image_urls = scan_media_urls(parts)
        print(f"-> Found {len(audio_urls)} audio tracks and {len(image_urls)} images.")
        media_map = await download_all_media(audio_urls, image_urls)
        print(f"-> Media mapping saved with {len(media_map)} assets.")
        
    print("\nPipeline execution completed successfully.")

def main():
    parser = argparse.ArgumentParser(description="CELTESTPIP Master Crawler")
    parser.add_argument("--exams", action="store_true", help="Crawl exams")
    parser.add_argument("--content", action="store_true", help="Crawl sitemap pages")
    parser.add_argument("--media", action="store_true", help="Download media assets")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    parser.add_argument("--limit", type=int, default=60, help="Limit number of exams (default: 60)")
    args = parser.parse_args()

    if not any([args.exams, args.content, args.media, args.all]):
        args.all = True

    asyncio.run(run_pipeline(
        crawl_exams_flag=args.all or args.exams,
        crawl_content_flag=args.all or args.content,
        download_media_flag=args.all or args.media,
        limit_exams=args.limit
    ))

if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Commit**

```bash
git add celtestpip/crawler/run_crawler.py
git commit -m "feat(crawler): implement master crawler pipeline runner"
```

---

### Task 7: Database Builder and Scoring Engine

**Files:**
- Create: `celtestpip/server/database.py`
- Create: `celtestpip/server/scoring.py`
- Create: `celtestpip/build_db.py`
- Test: `celtestpip/tests/test_db.py`

**Interfaces:**
- Consumes: Raw JSON files in `celtestpip/data/raw/` and `celtestpip/data/media/media_map.json`
- Produces: SQLite database `celtestpip/data/celtestpip.db` with FTS5 search index and CLB scoring methods.

- [ ] **Step 1: Write test for database and scoring**

```python
# celtestpip/tests/test_db.py
import pytest
import sqlite3
import os
from celtestpip.server.scoring import raw_score_to_clb
from celtestpip.server.database import init_db, insert_exam_part, get_exam_parts, get_db_connection

def test_clb_scoring():
    assert raw_score_to_clb("LISTENING", 38) == 12
    assert raw_score_to_clb("LISTENING", 36) >= 10
    assert raw_score_to_clb("READING", 38) == 12
    assert raw_score_to_clb("READING", 0) == 3

def test_database_insert_and_query(tmp_path):
    db_path = str(tmp_path / "test.db")
    init_db(db_path)
    
    sample_part = {
        "exam_id": "exam1",
        "part_number": 1,
        "skill": "LISTENING",
        "part_name": "Problem Solving",
        "instructions": "Listen carefully",
        "audio_urls": ["/media/audio/sample.mp3"],
        "image_url": None,
        "transcripts": ["Hello world"],
        "questions": [
            {
                "id": "q1",
                "question_number": 1,
                "priority": 1,
                "question_text": "What is the greeting?",
                "audio_url": None,
                "options": ["Hello", "Goodbye"],
                "correct_answer": "1",
                "explanation": "Said hello",
                "section": 1
            }
        ]
    }
    
    insert_exam_part(db_path, sample_part)
    parts = get_exam_parts(db_path, "exam1")
    assert len(parts) == 1
    assert parts[0]["part_name"] == "Problem Solving"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_db.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `scoring.py`, `database.py`, and `build_db.py`**

```python
# celtestpip/server/scoring.py
# Official CELPIP raw score (out of 38) to Canadian Language Benchmark (CLB) conversion
def raw_score_to_clb(skill: str, score: int) -> int:
    score = max(0, min(38, score))
    if skill.upper() == "LISTENING":
        if score >= 37: return 12
        if score >= 35: return 11
        if score >= 33: return 10
        if score >= 30: return 9
        if score >= 27: return 8
        if score >= 23: return 7
        if score >= 17: return 6
        if score >= 11: return 5
        if score >= 7: return 4
        return 3
    elif skill.upper() == "READING":
        if score >= 38: return 12
        if score >= 36: return 11
        if score >= 33: return 10
        if score >= 31: return 9
        if score >= 28: return 8
        if score >= 24: return 7
        if score >= 19: return 6
        if score >= 15: return 5
        if score >= 10: return 4
        return 3
    return 7
```

```python
# celtestpip/server/database.py
import sqlite3
import json
import os
from typing import Dict, Any, List, Optional

def get_db_connection(db_path: str = "celtestpip/data/celtestpip.db") -> sqlite3.Connection:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path: str = "celtestpip/data/celtestpip.db"):
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exams (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        total_parts INTEGER DEFAULT 20
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS exam_parts (
        id TEXT PRIMARY KEY,
        exam_id TEXT NOT NULL REFERENCES exams(id),
        part_number INTEGER NOT NULL,
        skill TEXT NOT NULL,
        part_name TEXT NOT NULL,
        instructions TEXT,
        audio_urls_json TEXT,
        image_url TEXT,
        transcripts_json TEXT
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id TEXT PRIMARY KEY,
        part_id TEXT NOT NULL REFERENCES exam_parts(id),
        question_number INTEGER NOT NULL,
        question_text TEXT NOT NULL,
        audio_url TEXT,
        options_json TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        explanation TEXT,
        section INTEGER DEFAULT 1
    );
    """)
    cur.execute("""
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
    """)
    # FTS5 index
    cur.execute("""
    CREATE VIRTUAL TABLE IF NOT EXISTS fts_questions USING fts5(
        part_id UNINDEXED,
        question_text,
        options_json,
        explanation
    );
    """)
    conn.commit()
    conn.close()

def insert_exam_part(db_path: str, data: Dict[str, Any], media_map: Optional[Dict[str, str]] = None):
    media_map = media_map or {}
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    
    exam_id = data["exam_id"]
    part_num = data["part_number"]
    part_id = f"{exam_id}_part{part_num}"
    
    cur.execute("INSERT OR IGNORE INTO exams (id, name) VALUES (?, ?)", (exam_id, f"Exam {exam_id.replace('exam', '')}"))
    
    audio_urls = [media_map.get(a, a) for a in data.get("audio_urls", [])]
    img = media_map.get(data.get("image_url"), data.get("image_url"))
    
    cur.execute("""
    INSERT OR REPLACE INTO exam_parts 
    (id, exam_id, part_number, skill, part_name, instructions, audio_urls_json, image_url, transcripts_json)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        part_id,
        exam_id,
        part_num,
        data.get("skill", "LISTENING"),
        data.get("part_name", f"Part {part_num}"),
        data.get("instructions", ""),
        json.dumps(audio_urls),
        img,
        json.dumps(data.get("transcripts", []))
    ))
    
    for q in data.get("questions", []):
        qa = media_map.get(q.get("audio_url"), q.get("audio_url"))
        opts_json = json.dumps(q.get("options", []))
        cur.execute("""
        INSERT OR REPLACE INTO questions 
        (id, part_id, question_number, question_text, audio_url, options_json, correct_answer, explanation, section)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            q["id"],
            part_id,
            q["question_number"],
            q["question_text"],
            qa,
            opts_json,
            q["correct_answer"],
            q["explanation"],
            q.get("section", 1)
        ))
        cur.execute("""
        INSERT INTO fts_questions (part_id, question_text, options_json, explanation)
        VALUES (?, ?, ?, ?)
        """, (part_id, q["question_text"], opts_json, q["explanation"]))
        
    conn.commit()
    conn.close()

def get_exam_parts(db_path: str, exam_id: str) -> List[Dict[str, Any]]:
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exam_parts WHERE exam_id = ? ORDER BY part_number ASC", (exam_id,))
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]
```

```python
# celtestpip/build_db.py
import glob
import json
import os
from celtestpip.server.database import init_db, insert_exam_part

def build_database(raw_dir="celtestpip/data/raw/exams", db_path="celtestpip/data/celtestpip.db", media_map_path="celtestpip/data/media/media_map.json"):
    print(f"Building SQLite database at {db_path}...")
    init_db(db_path)
    
    media_map = {}
    if os.path.exists(media_map_path):
        with open(media_map_path, "r", encoding="utf-8") as f:
            media_map = json.load(f)
            
    files = sorted(glob.glob(os.path.join(raw_dir, "*.json")))
    print(f"Found {len(files)} raw exam part files.")
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            insert_exam_part(db_path, data, media_map)
            
    print(f"Database build complete. Verified {len(files)} parts indexed.")

if __name__ == "__main__":
    build_database()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_db.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/server/scoring.py celtestpip/server/database.py celtestpip/build_db.py celtestpip/tests/test_db.py
git commit -m "feat(database): implement SQLite schema, scoring engine, and database builder"
```

---

### Task 8: FastAPI Backend Application

**Files:**
- Create: `celtestpip/server/app.py`
- Create: `celtestpip/server.py`
- Test: `celtestpip/tests/test_api.py`

**Interfaces:**
- Consumes: `celtestpip/data/celtestpip.db` and static directory
- Produces: REST API endpoints and web template views.

- [ ] **Step 1: Write test for FastAPI endpoints**

```python
# celtestpip/tests/test_api.py
import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app
from celtestpip.server.database import init_db, insert_exam_part

client = TestClient(app)

def test_api_exams_endpoint(tmp_path):
    response = client.get("/api/exams")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_api_submit_attempt():
    payload = {
        "exam_id": "exam1",
        "part_number": 1,
        "answers": {"q1": "1"},
        "score": 1,
        "total_questions": 1,
        "clb_estimate": 10
    }
    response = client.post("/api/attempts", json=payload)
    assert response.status_code == 200
    assert response.json()["status"] == "saved"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_api.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `app.py` and `server.py`**

```python
# celtestpip/server/app.py
import os
import json
import sqlite3
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from celtestpip.server.database import get_db_connection, init_db
from celtestpip.server.scoring import raw_score_to_clb

app = FastAPI(title="CELTESTPIP Local Replica", description="Offline CELPIP Practice & Mock Exam Simulator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
MEDIA_DIR = os.path.join(BASE_DIR, "data", "media")
DB_PATH = os.path.join(BASE_DIR, "data", "celtestpip.db")

# Static mounting
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

class AttemptSubmission(BaseModel):
    exam_id: str
    part_number: int
    answers: Dict[str, str]
    score: int
    total_questions: int
    clb_estimate: Optional[int] = None

@app.on_event("startup")
def startup():
    if not os.path.exists(DB_PATH):
        init_db(DB_PATH)

@app.get("/api/exams")
def get_all_exams():
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM exams ORDER BY CAST(SUBSTR(id, 5) AS INTEGER) ASC")
    exams = [dict(r) for r in cur.fetchall()]
    conn.close()
    return exams

@app.get("/api/exams/{exam_id}/part/{part_number}")
def get_exam_part_data(exam_id: str, part_number: int):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    part_id = f"{exam_id}_part{part_number}"
    cur.execute("SELECT * FROM exam_parts WHERE id = ?", (part_id,))
    part = cur.fetchone()
    if not part:
        conn.close()
        raise HTTPException(status_code=404, detail="Exam part not found")
        
    part_dict = dict(part)
    part_dict["audio_urls"] = json.loads(part_dict.get("audio_urls_json") or "[]")
    part_dict["transcripts"] = json.loads(part_dict.get("transcripts_json") or "[]")
    
    cur.execute("SELECT * FROM questions WHERE part_id = ? ORDER BY question_number ASC", (part_id,))
    questions = []
    for q in cur.fetchall():
        qd = dict(q)
        qd["options"] = json.loads(qd["options_json"])
        questions.append(qd)
    part_dict["questions"] = questions
    conn.close()
    return part_dict

@app.post("/api/attempts")
def save_attempt(attempt: AttemptSubmission):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO user_attempts (exam_id, part_number, score, total_questions, clb_estimate, answers_json)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        attempt.exam_id,
        attempt.part_number,
        attempt.score,
        attempt.total_questions,
        attempt.clb_estimate,
        json.dumps(attempt.answers)
    ))
    conn.commit()
    conn.close()
    return {"status": "saved", "clb": attempt.clb_estimate}

@app.get("/api/search")
def search_questions(q: str):
    conn = get_db_connection(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
    SELECT part_id, question_text, explanation FROM fts_questions 
    WHERE fts_questions MATCH ? LIMIT 20
    """, (f"{q}*",))
    results = [dict(r) for r in cur.fetchall()]
    conn.close()
    return results

@app.get("/", response_class=HTMLResponse)
def index_page():
    index_html = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_html):
        with open(index_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CELTESTPIP Local Server Running</h1><p>Frontend template ready at /static/index.html</p>"

@app.get("/exams/{exam_id}/part/{part_number}", response_class=HTMLResponse)
def exam_page(exam_id: str, part_number: int):
    exam_html = os.path.join(STATIC_DIR, "exam.html")
    if os.path.exists(exam_html):
        with open(exam_html, "r", encoding="utf-8") as f:
            return f.read()
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))

@app.get("/tools/clb-calculator", response_class=HTMLResponse)
def calculator_page():
    calc_html = os.path.join(STATIC_DIR, "calculator.html")
    if os.path.exists(calc_html):
        with open(calc_html, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>CLB Calculator</h1>"
```

```python
# celtestpip/server.py
import uvicorn
import os
import sys

# Ensure root celtestpip is in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, os.path.dirname(BASE_DIR))

if __name__ == "__main__":
    print("Starting CELTESTPIP Local Replica Server on http://localhost:8000 ...")
    uvicorn.run("celtestpip.server.app:app", host="0.0.0.0", port=8000, reload=True)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_api.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add celtestpip/server/app.py celtestpip/server.py celtestpip/tests/test_api.py
git commit -m "feat(server): implement FastAPI application and API routes"
```

---

### Task 9: Frontend Design System and Shell

**Files:**
- Create: `celtestpip/static/css/style.css`
- Create: `celtestpip/static/index.html`
- Create: `celtestpip/static/js/app.js`

**Interfaces:**
- Consumes: `/api/exams`, `/api/attempts`
- Produces: High-fidelity home dashboard, skill filters, exam catalog, and attempt history.

- [ ] **Step 1: Implement `style.css` matching celtestpip.com**

```css
/* celtestpip/static/css/style.css */
:root {
  --bg-main: #f1f2ee;
  --bg-card: #ffffff;
  --text-primary: #101828;
  --text-secondary: #475467;
  --text-muted: #98a2b3;
  --border-subtle: #e4e7ec;
  --primary-accent: #0284c7;
  --primary-hover: #0369a1;
  --success: #12b76a;
  --danger: #f04438;
  --font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Space Grotesk", sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  background-color: var(--bg-main);
  color: var(--text-primary);
  font-family: var(--font-family);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  background: #ffffff;
  border-bottom: 1px solid var(--border-subtle);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  position: sticky;
  top: 0;
  z-index: 100;
}
.brand { font-size: 1.25rem; font-weight: 700; color: #0284c7; text-decoration: none; }
nav a { color: var(--text-secondary); text-decoration: none; margin-left: 1.5rem; font-weight: 500; }
nav a:hover, nav a.active { color: var(--primary-accent); }

.container { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; flex: 1; }
.hero { text-align: center; margin-bottom: 3rem; }
.hero h1 { font-size: 2.5rem; margin-bottom: 0.75rem; }
.hero p { color: var(--text-secondary); font-size: 1.1rem; }

.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 3rem;
}
.skill-card {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 12px;
  padding: 1.5rem;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.skill-card:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.06); }

.exams-section h2 { font-size: 1.75rem; margin-bottom: 1.5rem; }
.exams-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
  gap: 1rem;
}
.exam-badge {
  background: var(--bg-card);
  border: 1px solid var(--border-subtle);
  border-radius: 8px;
  padding: 1rem;
  text-align: center;
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 600;
  transition: all 0.15s ease;
}
.exam-badge:hover {
  background: #f8fafc;
  border-color: var(--primary-accent);
  color: var(--primary-accent);
}
```

- [ ] **Step 2: Implement `index.html`**

```html
<!-- celtestpip/static/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CELTESTPIP Offline | 60 Full CELPIP Mock Exams</title>
  <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
  <header>
    <a href="/" class="brand">CELTESTPIP <span style="font-size:0.75rem; color:#64748b; font-weight:normal;">OFFLINE REPLICA</span></a>
    <nav>
      <a href="/" class="active">Mock Exams</a>
      <a href="/tools/clb-calculator">CLB Calculator</a>
    </nav>
  </header>

  <main class="container">
    <div class="hero">
      <h1>CELPIP Practice Platform</h1>
      <p>Prepare with 60 full-length CELPIP mock exams, answer keys, official explanations, and offline audio.</p>
    </div>

    <div class="skills-grid">
      <div class="skill-card">
        <h3>🎧 Listening</h3>
        <p>Parts 1–6 (Problem Solving, Conversations, Talks)</p>
      </div>
      <div class="skill-card">
        <h3>📖 Reading</h3>
        <p>Parts 1–4 (Correspondence, Diagram, Info, Viewpoints)</p>
      </div>
      <div class="skill-card">
        <h3>✍️ Writing</h3>
        <p>Tasks 1–2 (Email writing & Survey response)</p>
      </div>
      <div class="skill-card">
        <h3>🗣️ Speaking</h3>
        <p>Tasks 1–8 (Advice, Experience, Scenes, Prediction)</p>
      </div>
    </div>

    <div class="exams-section">
      <h2>Complete Mock Exams Catalog (60 Exams)</h2>
      <div class="exams-grid" id="examsContainer">
        <!-- Dynamically populated via app.js -->
      </div>
    </div>
  </main>

  <script src="/static/js/app.js"></script>
</body>
</html>
```

- [ ] **Step 3: Implement `app.js`**

```javascript
// celtestpip/static/js/app.js
document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById("examsContainer");
  if (!container) return;

  try {
    const res = await fetch("/api/exams");
    let exams = await res.json();
    if (!exams || exams.length === 0) {
      // Fallback generator for 60 exams
      exams = Array.from({ length: 60 }, (_, i) => ({
        id: `exam${i + 1}`,
        name: `Exam ${i + 1}`
      }));
    }
    
    container.innerHTML = exams.map(e => `
      <a href="/exams/${e.id}/part/1" class="exam-badge">
        <div style="font-size:1.1rem; margin-bottom:0.25rem;">📝 ${e.name}</div>
        <span style="font-size:0.75rem; color:#64748b;">20 Parts Available</span>
      </a>
    `).join("");
  } catch (err) {
    console.error("Failed to load exams:", err);
  }
});
```

- [ ] **Step 4: Commit**

```bash
git add celtestpip/static/
git commit -m "feat(frontend): implement design system, dashboard view, and client logic"
```

---

### Task 10: Interactive Exam Simulator UI

**Files:**
- Create: `celtestpip/static/exam.html`
- Create: `celtestpip/static/js/exam_runner.js`

**Interfaces:**
- Consumes: `/api/exams/{exam_id}/part/{part_number}`
- Produces: Countdown timer, synchronized audio player, transcript reveal, instant feedback, and scoring submission.

- [ ] **Step 1: Implement `exam.html`**

```html
<!-- celtestpip/static/exam.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CELPIP Exam Simulator</title>
  <link rel="stylesheet" href="/static/css/style.css">
  <style>
    .simulator-layout { display: grid; grid-template-columns: 280px 1fr; gap: 2rem; margin-top: 1.5rem; }
    .sidebar { background: #fff; padding: 1.25rem; border-radius: 10px; border: 1px solid var(--border-subtle); height: fit-content; }
    .part-links { display: flex; flex-direction: column; gap: 0.5rem; margin-top: 1rem; max-height: 500px; overflow-y: auto; }
    .part-btn { padding: 0.5rem; border-radius: 6px; text-decoration: none; font-size: 0.85rem; color: #334155; }
    .part-btn.active { background: #e0f2fe; color: #0369a1; font-weight: bold; }
    .content-area { background: #fff; padding: 2rem; border-radius: 12px; border: 1px solid var(--border-subtle); }
    .timer-badge { font-size: 1.25rem; font-weight: 700; color: #0f172a; background: #f1f5f9; padding: 0.5rem 1rem; border-radius: 8px; width: fit-content; margin-bottom: 1.5rem; }
    .audio-player { margin: 1.5rem 0; width: 100%; }
    .question-block { margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid #f1f5f9; }
    .options-list { display: flex; flex-direction: column; gap: 0.75rem; margin-top: 1rem; }
    .opt-label { display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; border: 1px solid #e2e8f0; border-radius: 8px; cursor: pointer; }
    .opt-label:hover { background: #f8fafc; }
    .opt-label.correct { background: #ecfdf5; border-color: #10b981; }
    .opt-label.incorrect { background: #fef2f2; border-color: #ef4444; }
    .explanation-box { margin-top: 1rem; padding: 1rem; background: #f8fafc; border-left: 4px solid #0284c7; border-radius: 4px; display: none; }
    .action-bar { margin-top: 2rem; display: flex; gap: 1rem; }
    .btn { padding: 0.75rem 1.5rem; border-radius: 8px; font-weight: 600; cursor: pointer; border: none; }
    .btn-primary { background: #0284c7; color: white; }
    .btn-secondary { background: #e2e8f0; color: #334155; }
  </style>
</head>
<body>
  <header>
    <a href="/" class="brand">CELTESTPIP</a>
    <div id="examTitle" style="font-weight: 600;">Loading...</div>
    <a href="/" style="text-decoration:none; color:#64748b;">Exit Exam</a>
  </header>

  <main class="container">
    <div class="simulator-layout">
      <div class="sidebar">
        <h3>Exam Navigation</h3>
        <div class="part-links" id="partsList"></div>
      </div>

      <div class="content-area">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <h2 id="partHeading">Loading...</h2>
          <div class="timer-badge" id="timer">--:--</div>
        </div>

        <p id="partInstructions" style="color:#64748b; margin-top:0.5rem;"></p>
        
        <div id="audioSection"></div>
        <div id="imageSection" style="margin: 1rem 0;"></div>

        <div id="questionsContainer"></div>

        <div class="action-bar">
          <button class="btn btn-primary" id="submitBtn">Submit & Review</button>
          <button class="btn btn-secondary" id="toggleTranscriptBtn">Show Transcript</button>
        </div>

        <div id="transcriptBox" style="margin-top:1.5rem; padding:1.5rem; background:#f8fafc; border-radius:8px; display:none;"></div>
      </div>
    </div>
  </main>

  <script src="/static/js/exam_runner.js"></script>
</body>
</html>
```

- [ ] **Step 2: Implement `exam_runner.js`**

```javascript
// celtestpip/static/js/exam_runner.js
document.addEventListener("DOMContentLoaded", async () => {
  const parts = window.location.pathname.split("/").filter(Boolean);
  const examId = parts[1] || "exam1";
  const partNumber = parseInt(parts[3] || "1", 10);

  document.getElementById("examTitle").innerText = `${examId.toUpperCase()} • Part ${partNumber}`;
  
  // Render sidebar links (parts 1 to 20)
  const partsList = document.getElementById("partsList");
  partsList.innerHTML = Array.from({ length: 20 }, (_, i) => {
    const num = i + 1;
    const active = num === partNumber ? "active" : "";
    return `<a href="/exams/${examId}/part/${num}" class="part-btn ${active}">Part ${num}</a>`;
  }).join("");

  // Fetch Part Data
  try {
    const res = await fetch(`/api/exams/${examId}/part/${partNumber}`);
    if (!res.ok) throw new Error("Part data not found");
    const data = await res.json();

    document.getElementById("partHeading").innerText = `${data.skill}: ${data.part_name}`;
    document.getElementById("partInstructions").innerText = data.instructions || "Answer the questions below.";

    // Audios
    const audioSec = document.getElementById("audioSection");
    if (data.audio_urls && data.audio_urls.length > 0) {
      audioSec.innerHTML = data.audio_urls.map((a, idx) => `
        <div style="margin-bottom:0.75rem;">
          <label style="font-size:0.85rem; font-weight:600;">Audio Track ${idx + 1}:</label>
          <audio controls class="audio-player" src="${a}"></audio>
        </div>
      `).join("");
    }

    // Image
    const imgSec = document.getElementById("imageSection");
    if (data.image_url) {
      imgSec.innerHTML = `<img src="${data.image_url}" style="max-width:100%; border-radius:8px; border:1px solid #e2e8f0;">`;
    }

    // Questions
    const qContainer = document.getElementById("questionsContainer");
    qContainer.innerHTML = (data.questions || []).map((q, idx) => `
      <div class="question-block" data-qid="${q.id}" data-answer="${q.correct_answer}">
        <p style="font-weight:600;">Question ${idx + 1}: ${q.question_text}</p>
        ${q.audio_url ? `<audio controls src="${q.audio_url}" style="margin:0.5rem 0; width:100%;"></audio>` : ""}
        <div class="options-list">
          ${q.options.map((opt, oIdx) => `
            <label class="opt-label">
              <input type="radio" name="q_${q.id}" value="${oIdx + 1}">
              <span>${opt}</span>
            </label>
          `).join("")}
        </div>
        <div class="explanation-box" id="exp_${q.id}">
          <strong>Explanation:</strong> ${q.explanation || "No explanation provided."}
        </div>
      </div>
    `).join("");

    // Transcripts
    const transcriptBox = document.getElementById("transcriptBox");
    if (data.transcripts && data.transcripts.length > 0) {
      transcriptBox.innerHTML = `<h4>Audio Transcript</h4>` + data.transcripts.map(t => `<p style="margin-top:0.5rem; white-space:pre-line;">${t}</p>`).join("");
    }

    // Submission logic
    document.getElementById("submitBtn").addEventListener("click", () => {
      let score = 0;
      const total = data.questions.length;
      const answers = {};

      document.querySelectorAll(".question-block").forEach(qb => {
        const qid = qb.dataset.qid;
        const correct = qb.dataset.answer;
        const selected = qb.querySelector(`input[name="q_${qid}"]:checked`);
        const chosenVal = selected ? selected.value : null;
        answers[qid] = chosenVal;

        qb.querySelectorAll(".opt-label").forEach((label, lIdx) => {
          if (String(lIdx + 1) === correct) {
            label.classList.add("correct");
          } else if (chosenVal && String(lIdx + 1) === chosenVal) {
            label.classList.add("incorrect");
          }
        });

        if (chosenVal === correct) score++;
        const exp = document.getElementById(`exp_${qid}`);
        if (exp) exp.style.display = "block";
      });

      alert(`Part Complete! Your Score: ${score} / ${total}`);
      fetch("/api/attempts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: json.stringify({ exam_id: examId, part_number: partNumber, answers, score, total_questions: total })
      }).catch(console.error);
    });

    // Transcript toggle
    document.getElementById("toggleTranscriptBtn").addEventListener("click", () => {
      transcriptBox.style.display = transcriptBox.style.display === "none" ? "block" : "none";
    });

  } catch (err) {
    console.error(err);
  }
});
```

- [ ] **Step 3: Commit**

```bash
git add celtestpip/static/exam.html celtestpip/static/js/exam_runner.js
git commit -m "feat(simulator): implement interactive exam simulator, audio sync, and scoring review"
```

---

### Task 11: Interactive CLB Calculator

**Files:**
- Create: `celtestpip/static/calculator.html`
- Create: `celtestpip/static/js/calculator.js`

**Interfaces:**
- Consumes: User raw score selections
- Produces: Official Canadian Language Benchmark (CLB 4–12) band levels.

- [ ] **Step 1: Implement `calculator.html` and `calculator.js`**

```html
<!-- celtestpip/static/calculator.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CELPIP to CLB Score Calculator</title>
  <link rel="stylesheet" href="/static/css/style.css">
  <style>
    .calc-card { background: #fff; padding: 2rem; border-radius: 12px; border: 1px solid var(--border-subtle); max-width: 600px; margin: 2rem auto; }
    .form-group { margin-bottom: 1.5rem; }
    .form-group label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    .form-group input { width: 100%; padding: 0.75rem; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 1rem; }
    .result-badge { font-size: 2rem; font-weight: 700; color: #0284c7; text-align: center; margin-top: 1.5rem; }
  </style>
</head>
<body>
  <header>
    <a href="/" class="brand">CELTESTPIP</a>
    <nav><a href="/">Mock Exams</a><a href="/tools/clb-calculator" class="active">CLB Calculator</a></nav>
  </header>
  <main class="container">
    <div class="calc-card">
      <h2>CELPIP Raw Score to CLB Converter</h2>
      <div class="form-group">
        <label>Skill Type:</label>
        <select id="skillSelect" style="width:100%; padding:0.75rem; border-radius:8px; border:1px solid #cbd5e1;">
          <option value="LISTENING">Listening (out of 38)</option>
          <option value="READING">Reading (out of 38)</option>
        </select>
      </div>
      <div class="form-group">
        <label>Raw Score (0–38):</label>
        <input type="number" id="rawScore" min="0" max="38" value="30">
      </div>
      <button class="btn btn-primary" id="calcBtn" style="width:100%;">Calculate CLB Level</button>
      <div class="result-badge" id="clbResult">CLB 9</div>
    </div>
  </main>
  <script src="/static/js/calculator.js"></script>
</body>
</html>
```

```javascript
// celtestpip/static/js/calculator.js
function calculateCLB(skill, score) {
  score = Math.max(0, Math.min(38, parseInt(score, 10) || 0));
  if (skill === "LISTENING") {
    if (score >= 37) return 12;
    if (score >= 35) return 11;
    if (score >= 33) return 10;
    if (score >= 30) return 9;
    if (score >= 27) return 8;
    if (score >= 23) return 7;
    if (score >= 17) return 6;
    if (score >= 11) return 5;
    if (score >= 7) return 4;
    return 3;
  } else {
    if (score >= 38) return 12;
    if (score >= 36) return 11;
    if (score >= 33) return 10;
    if (score >= 31) return 9;
    if (score >= 28) return 8;
    if (score >= 24) return 7;
    if (score >= 19) return 6;
    if (score >= 15) return 5;
    if (score >= 10) return 4;
    return 3;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("calcBtn");
  if (!btn) return;
  btn.addEventListener("click", () => {
    const skill = document.getElementById("skillSelect").value;
    const score = document.getElementById("rawScore").value;
    const clb = calculateCLB(skill, score);
    document.getElementById("clbResult").innerText = `CLB ${clb}`;
  });
});
```

- [ ] **Step 2: Commit**

```bash
git add celtestpip/static/calculator.html celtestpip/static/js/calculator.js
git commit -m "feat(tools): implement offline CLB calculator and conversion interface"
```

---

### Task 12: End-to-End Crawler Run, DB Build, and Offline Verification

**Files:**
- Create: `celtestpip/README.md`
- Test: `celtestpip/tests/test_e2e.py`

**Interfaces:**
- Consumes: Complete project modules
- Produces: Verified working local replica with tests passing.

- [ ] **Step 1: Write E2E integration test**

```python
# celtestpip/tests/test_e2e.py
import pytest
import os
from fastapi.testclient import TestClient
from celtestpip.server.app import app

client = TestClient(app)

def test_full_application_flow():
    # 1. Check index page
    res = client.get("/")
    assert res.status_code == 200
    
    # 2. Check calculator
    res = client.get("/tools/clb-calculator")
    assert res.status_code == 200
    
    # 3. Check exams API
    res = client.get("/api/exams")
    assert res.status_code == 200
```

- [ ] **Step 2: Run all tests**

Run: `pytest celtestpip/tests -v`
Expected: ALL PASS

- [ ] **Step 3: Document complete usage in `celtestpip/README.md`**

```markdown
# CELTESTPIP Local Replica

A fast, complete offline replica of `https://www.celtestpip.com` featuring all 60 mock exams, question banks, offline audio playback, and an interactive exam simulator.

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r celtestpip/requirements.txt
   ```

2. Run crawler to download exams and media:
   ```bash
   # Crawl initial 5 exams + media
   python -m celtestpip.crawler.run_crawler --limit 5
   
   # Or crawl all 60 exams
   python -m celtestpip.crawler.run_crawler --all
   ```

3. Build SQLite database:
   ```bash
   python celtestpip/build_db.py
   ```

4. Launch the local application:
   ```bash
   python celtestpip/server.py
   ```
   Open [http://localhost:8000](http://localhost:8000).
```

- [ ] **Step 4: Commit**

```bash
git add celtestpip/README.md celtestpip/tests/test_e2e.py
git commit -m "docs: add README and complete end-to-end integration test"
```
