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

def harvest_categories():
    conn = get_db()
    cur = conn.cursor()
    categories = cur.execute("SELECT id, title, slug, collection_id FROM categories WHERE collection_id IN ('topic-related', 'most-common', 'categorized-words')").fetchall()
    conn.close()

    client = httpx.Client(verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}, timeout=20.0)
    
    print(f"Harvesting subcategories for {len(categories)} categories...")
    
    for idx, cat in enumerate(categories, 1):
        cat_id = cat['id']
        slug = cat['slug'] or 'category'
        url = f"https://langeek.co/fr-EN/vocab/category/{cat_id}/{slug}"
        print(f"[{idx}/{len(categories)}] Fetching Cat {cat_id}: {cat['title']}...")
        
        try:
            resp = client.get(url)
            if resp.status_code != 200:
                print(f"  Warning: HTTP {resp.status_code} for {url}")
                continue
                
            m = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', resp.text)
            if not m:
                print("  Warning: No __NEXT_DATA__ found")
                continue
                
            data = json.loads(m.group(1))
            props = data.get('props', {}).get('pageProps', {}).get('initialState', {}).get('static', {})
            cat_obj = props.get('category', {})
            subcategories = cat_obj.get('subCategories', [])
            
            print(f"  Found {len(subcategories)} subcategories for {cat['title']}")
            
            db_conn = get_db()
            db_cur = db_conn.cursor()
            
            # Update category meta if available
            db_cur.execute("""
                UPDATE categories 
                SET title = ?, description = ?, photo = ?, words_count = ?, subcategories_count = ?
                WHERE id = ?
            """, (
                cat_obj.get('title') or cat['title'],
                cat_obj.get('description') or '',
                cat_obj.get('photo') or '',
                cat_obj.get('wordsCount', 0),
                len(subcategories),
                cat_id
            ))
            
            for s in subcategories:
                sub_id = s.get('id')
                db_cur.execute("""
                    INSERT OR REPLACE INTO subcategories (id, category_id, title, original_title, slug, words_count, position, photo, description)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    sub_id,
                    cat_id,
                    s.get('title', ''),
                    s.get('originalTitle', ''),
                    s.get('urlId', ''),
                    s.get('wordsCount', 0),
                    s.get('position', 0),
                    s.get('photo', ''),
                    s.get('description', '')
                ))
            
            db_conn.commit()
            db_conn.close()
            time.sleep(0.15)
            
        except Exception as e:
            print(f"  Error on category {cat_id}: {e}")

if __name__ == "__main__":
    harvest_categories()
