import glob
import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from celtestpip.server.database import init_db, insert_exam_part


def build_database(
    raw_dir="celtestpip/data/raw/exams",
    db_path="celtestpip/data/celtestpip.db",
    media_map_path="celtestpip/data/media/media_map.json",
):
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
