import sqlite3
import httpx
import json
import re
import time
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "langeek.db")

def harvest_grammar_courses():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    courses = cur.execute("SELECT id, url_id, level, title FROM grammar_courses").fetchall()
    conn.close()

    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0"}, timeout=20.0, follow_redirects=True)
    print(f"Ingesting content for {len(courses)} grammar courses...")

    for idx, c in enumerate(courses, 1):
        c_id = c['id']
        url_id = c['url_id']
        lvl = c['level'] or 'intermediate'
        target_url = f"https://langeek.co/fr-EN/grammar/course/{c_id}/{url_id}/{lvl}"
        print(f"[{idx}/{len(courses)}] Course {c_id}: {c['title']}...")
        try:
            resp = client.get(target_url)
            if resp.status_code != 200:
                print(f"  Warning: HTTP {resp.status_code}")
                continue
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
            if not m:
                print("  Warning: No __NEXT_DATA__")
                continue
            d = json.loads(m.group(1))
            props = d.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
            seg = props.get('segment', {})
            blocks = seg.get('blocks', [])
            q_blocks = seg.get('questionBlocks', [])
            toc = seg.get('tableOfContent', [])

            c_conn = sqlite3.connect(DB_PATH)
            c_cur = c_conn.cursor()
            c_cur.execute("""
                UPDATE grammar_courses 
                SET blocks_count = ?, blocks_json = ?
                WHERE id = ?
            """, (
                len(blocks),
                json.dumps({
                    'blocks': blocks,
                    'questions': q_blocks,
                    'toc': toc,
                    'description': seg.get('description', '')
                }, ensure_ascii=False),
                c_id
            ))
            c_conn.commit()
            c_conn.close()
            time.sleep(0.12)
        except Exception as e:
            print(f"  Error on course {c_id}: {e}")

    print("All grammar courses ingested!")

if __name__ == "__main__":
    harvest_grammar_courses()
