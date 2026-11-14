import sqlite3
import httpx
import json
import re
import time
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "langeek.db")

def harvest_stories():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    stories = cur.execute("SELECT id, collection_id, title, url_id FROM reading_stories").fetchall()
    conn.close()

    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0"}, timeout=20.0, follow_redirects=True)
    print(f"Ingesting content for {len(stories)} reading stories...")

    for idx, s in enumerate(stories, 1):
        s_id = s['id']
        url_id = s['url_id']
        target_url = f"https://langeek.co/fr-EN/reading/course/{s_id}/{url_id}/0"
        print(f"[{idx}/{len(stories)}] Fetching story {s_id}: {s['title']}...")
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
            r_blocks = props.get('readingBlocks', [])
            q_blocks = props.get('quizBlocks', [])
            
            # Format paragraphs
            paragraphs = []
            for b in r_blocks:
                sentences = b.get('sentences', [])
                fr_text = ""
                en_text = ""
                for sent in sentences:
                    fr_text += (sent.get('sentence') or "") + " "
                    loc = sent.get('localizedProperties') or {}
                    en_text += (loc.get('sentence') or "") + " "
                paragraphs.append({
                    'fr': fr_text.strip(),
                    'en': en_text.strip(),
                    'audio': b.get('readableTextVoice')
                })
            
            c_conn = sqlite3.connect(DB_PATH)
            c_cur = c_conn.cursor()
            c_cur.execute("""
                UPDATE reading_stories 
                SET content_json = ?, quiz_json = ? 
                WHERE id = ?
            """, (json.dumps(paragraphs, ensure_ascii=False), json.dumps(q_blocks, ensure_ascii=False), s_id))
            c_conn.commit()
            c_conn.close()
            time.sleep(0.15)
        except Exception as e:
            print(f"  Error on {s_id}: {e}")

    print("All 30 reading stories ingested!")

if __name__ == "__main__":
    harvest_stories()
