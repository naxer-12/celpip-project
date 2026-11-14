import sqlite3
import httpx
import json
import re
import time
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "langeek.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def setup_pronunciation_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pronunciation_courses (
            id INTEGER PRIMARY KEY,
            hub_id INTEGER DEFAULT 101,
            title TEXT,
            url_id TEXT,
            letter TEXT,
            description TEXT,
            photo TEXT,
            photo_thumbnail TEXT,
            content_json TEXT,
            position INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def harvest_pronunciation():
    setup_pronunciation_tables()
    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}, timeout=25.0)

    url = "https://langeek.co/fr-EN/pronunciation/101/alphabet-francais"
    print(f"Fetching Alphabet Hub from {url}...")
    resp = client.get(url)
    if resp.status_code != 200:
        print(f"Failed to fetch alphabet hub: HTTP {resp.status_code}")
        return

    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
    if not m:
        print("No __NEXT_DATA__ in alphabet hub")
        return

    data = json.loads(m.group(1))
    props = data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
    lvl = props.get('level', {})
    courses = lvl.get('courses', [])

    conn = get_db()
    cur = conn.cursor()

    print(f"Found {len(courses)} letter courses...")
    for idx, c in enumerate(courses):
        course_id = c.get('id')
        title = c.get('title', '')
        url_id = c.get('urlId', '')
        desc = c.get('description', '')
        photo = c.get('photo', '')
        thumb = c.get('photoThumbnail', '')
        
        # Extract letter character from title, e.g. "La lettre « A » en français" -> "A"
        letter_match = re.search(r'«\s*([A-Za-zÀ-ÿ])\s*»', title)
        letter = letter_match.group(1).upper() if letter_match else chr(65 + idx)

        cur.execute("""
            INSERT OR REPLACE INTO pronunciation_courses (id, hub_id, title, url_id, letter, description, photo, photo_thumbnail, position)
            VALUES (?, 101, ?, ?, ?, ?, ?, ?, ?)
        """, (course_id, title, url_id, letter, desc, photo, thumb, idx))

    conn.commit()
    conn.close()
    print("French Alphabet letter courses indexed successfully!")

if __name__ == "__main__":
    harvest_pronunciation()
