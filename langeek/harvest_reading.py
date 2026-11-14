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

def setup_reading_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reading_collections (
            id INTEGER PRIMARY KEY,
            title TEXT,
            url_id TEXT,
            photo TEXT,
            photo_thumbnail TEXT,
            description TEXT,
            courses_count INTEGER DEFAULT 0,
            position INTEGER DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS reading_stories (
            id INTEGER PRIMARY KEY,
            collection_id INTEGER,
            title TEXT,
            url_id TEXT,
            level TEXT,
            description TEXT,
            photo TEXT,
            photo_thumbnail TEXT,
            content_json TEXT,
            quiz_json TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (collection_id) REFERENCES reading_collections(id)
        )
    """)
    conn.commit()
    conn.close()

def harvest_reading():
    setup_reading_tables()
    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}, timeout=25.0)

    print("Fetching Reading Overview (/fr-EN/reading)...")
    resp = client.get("https://langeek.co/fr-EN/reading")
    if resp.status_code != 200:
        print(f"Failed to fetch reading overview: HTTP {resp.status_code}")
        return

    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
    if not m:
        print("No __NEXT_DATA__ in reading overview")
        return

    data = json.loads(m.group(1))
    props = data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
    levels = props.get('levels', [])

    conn = get_db()
    cur = conn.cursor()

    total_stories = 0
    for idx, lvl in enumerate(levels):
        col_id = lvl.get('id')
        title = lvl.get('title', '')
        url_id = lvl.get('urlId', '')
        photo = lvl.get('photo', '')
        thumb = lvl.get('photoThumbnail', '')
        desc = lvl.get('description', '')
        courses = lvl.get('courses', [])

        cur.execute("""
            INSERT OR REPLACE INTO reading_collections (id, title, url_id, photo, photo_thumbnail, description, courses_count, position)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (col_id, title, url_id, photo, thumb, desc, len(courses), idx))

        print(f"Collection {col_id}: {title} ({len(courses)} stories)")
        for c in courses:
            story_id = c.get('id')
            c_title = c.get('title', '')
            c_url_id = c.get('urlId', '')
            c_lvl = c.get('level', '')
            c_desc = c.get('description', '')
            c_photo = c.get('photo', '')
            c_thumb = c.get('photoThumbnail', '')

            cur.execute("""
                INSERT OR REPLACE INTO reading_stories (id, collection_id, title, url_id, level, description, photo, photo_thumbnail)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (story_id, col_id, c_title, c_url_id, c_lvl, c_desc, c_photo, c_thumb))
            total_stories += 1

    conn.commit()
    conn.close()
    print(f"Reading collections and {total_stories} stories indexed successfully!")

if __name__ == "__main__":
    harvest_reading()
