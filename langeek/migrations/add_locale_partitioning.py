"""Database Schema Migration: Multi-Locale Partitioning.

Adds 'locale' column to content tables, creates expressions table,
and establishes high-performance compound indices for multi-locale querying.
"""

import os
import sqlite3
import logging

logger = logging.getLogger("langeek_migration")
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def migrate_locale_partitioning(db_path="langeek/data/langeek.db"):
    if not os.path.exists(db_path):
        alt_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "langeek.db")
        if os.path.exists(alt_path):
            db_path = alt_path

    logger.info("Starting multi-locale partitioning migration on %s", db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    tables = [
        "categories", "subcategories", "grammar_categories",
        "grammar_courses", "reading_collections", "reading_stories",
        "reading_segments", "pronunciation_courses"
    ]

    for table in tables:
        cols = [c[1] for c in cur.execute(f"PRAGMA table_info({table})").fetchall()]
        if "locale" not in cols:
            logger.info("Adding locale column to %s", table)
            cur.execute(f"ALTER TABLE {table} ADD COLUMN locale TEXT NOT NULL DEFAULT 'fr'")

    # Ensure categories has position column for idx_cat_loc index
    cat_cols = [c[1] for c in cur.execute("PRAGMA table_info(categories)").fetchall()]
    if "position" not in cat_cols:
        logger.info("Adding position column to categories")
        cur.execute("ALTER TABLE categories ADD COLUMN position INTEGER DEFAULT 0")

    # Create expressions table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expressions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            locale TEXT NOT NULL DEFAULT 'fr',
            category TEXT NOT NULL,
            phrase TEXT NOT NULL,
            literal_translation TEXT,
            meaning TEXT NOT NULL,
            examples_json TEXT,
            audio_url TEXT,
            position INTEGER DEFAULT 0
        )
    """)

    # Update user_progress table
    prog_cols = [c[1] for c in cur.execute("PRAGMA table_info(user_progress)").fetchall()]
    if "locale" not in prog_cols:
        logger.info("Adding locale column to user_progress")
        cur.execute("ALTER TABLE user_progress ADD COLUMN locale TEXT NOT NULL DEFAULT 'fr'")

    # Indices for blazing-fast indexed querying
    cur.execute("CREATE INDEX IF NOT EXISTS idx_cat_loc ON categories(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_subcat_loc ON subcategories(category_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_gram_cat_loc ON grammar_categories(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_gram_course_loc ON grammar_courses(category_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_read_col_loc ON reading_collections(locale, position)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_read_story_loc ON reading_stories(collection_id, locale)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_expr_loc ON expressions(locale, category)")

    conn.commit()
    conn.close()
    logger.info("Multi-locale partitioning migration completed successfully.")


if __name__ == "__main__":
    migrate_locale_partitioning()
