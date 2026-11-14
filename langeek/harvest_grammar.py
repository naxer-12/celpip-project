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

def setup_grammar_tables():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS grammar_categories (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            url_id TEXT,
            photo_thumbnail TEXT,
            course_length INTEGER DEFAULT 0,
            position INTEGER DEFAULT 0
        )
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS grammar_courses (
            id INTEGER PRIMARY KEY,
            category_id INTEGER,
            title TEXT,
            original_title TEXT,
            url_id TEXT,
            web_title TEXT,
            description TEXT,
            photo TEXT,
            photo_thumbnail TEXT,
            level TEXT,
            content_json TEXT,
            blocks_count INTEGER DEFAULT 0,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES grammar_categories(id)
        )
    """)
    conn.commit()
    conn.close()

def harvest_grammar():
    setup_grammar_tables()
    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}, timeout=25.0)

    print("Fetching Grammar Overview (/fr-EN/grammar)...")
    resp = client.get("https://langeek.co/fr-EN/grammar")
    if resp.status_code != 200:
        print(f"Failed to fetch grammar overview: HTTP {resp.status_code}")
        return

    m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
    if not m:
        print("No __NEXT_DATA__ in grammar overview")
        return

    data = json.loads(m.group(1))
    props = data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
    ref = props.get('levels', {}).get('reference', {})

    conn = get_db()
    cur = conn.cursor()

    total_courses_count = 0
    for cat_id_str, cat_info in ref.items():
        cat_id = int(cat_id_str)
        title = cat_info.get('title', '')
        desc = cat_info.get('description', '')
        url_id = cat_info.get('urlId', '')
        photo = cat_info.get('photoThumbnail', '')
        course_len = cat_info.get('courseLength', 0)
        pos = cat_info.get('position', 0)

        cur.execute("""
            INSERT OR REPLACE INTO grammar_categories (id, title, description, url_id, photo_thumbnail, course_length, position)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (cat_id, title, desc, url_id, photo, course_len, pos))

        cat_url = f"https://langeek.co/fr-EN/grammar/{cat_id}/{url_id}"
        print(f"Fetching grammar category {cat_id} ({title}) from {cat_url}...")
        try:
            cat_resp = client.get(cat_url)
            if cat_resp.status_code == 200:
                cm = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', cat_resp.text)
                if cm:
                    cdata = json.loads(cm.group(1))
                    cprops = cdata.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
                    lvl = cprops.get('level', {})
                    courses = lvl.get('courses', [])
                    print(f"  Found {len(courses)} courses in {title}")

                    for c in courses:
                        course_id = c.get('id')
                        c_title = c.get('title', '')
                        c_url_id = c.get('urlId', '')
                        c_web_title = c.get('webTitle', '')
                        c_desc = c.get('description', '')
                        c_photo = c.get('photo', '')
                        c_thumb = c.get('photoThumbnail', '')
                        c_lvl = c.get('level', '')

                        cur.execute("""
                            INSERT OR REPLACE INTO grammar_courses 
                            (id, category_id, title, original_title, url_id, web_title, description, photo, photo_thumbnail, level)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, (course_id, cat_id, c_title, c_title, c_url_id, c_web_title, c_desc, c_photo, c_thumb, c_lvl))
                        total_courses_count += 1

            conn.commit()
            time.sleep(0.2)
        except Exception as e:
            print(f"  Error fetching courses for {title}: {e}")

    conn.commit()
    conn.close()
    print(f"Grammar categories and {total_courses_count} courses indexed successfully!")

if __name__ == "__main__":
    harvest_grammar()
