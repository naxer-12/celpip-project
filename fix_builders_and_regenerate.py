#!/usr/bin/env python3
"""
fix_builders_and_regenerate.py - Fix CSS escaping and fonts path in all builders, then build HTML.
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

BUILDERS = [
    ("French_A2", "build_a2_html.py", "#2572be"),
    ("French_B1", "build_b1_html.py", "#6b46c1"),
    ("French_B2", "build_b2_html.py", "#9f1239"),
    ("French_C1", "build_c1_html.py", "#047857"),
    ("French_C2", "build_c2_html.py", "#1e1b4b"),
]

def fix_builder(level_dir, script_name, accent):
    filepath = os.path.join(ROOT_DIR, level_dir, script_name)
    print(f"Fixing {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix FONTS_METADATA_PATH
    content = re.sub(
        r'FONTS_METADATA_PATH\s*=\s*os\.path\.join\(BASE_DIR,\s*"scribd_fonts\.json"\)',
        'FONTS_METADATA_PATH = os.path.join(BASE_DIR, "scribd_fonts.json")\n'
        'if not os.path.exists(FONTS_METADATA_PATH):\n'
        '    FONTS_METADATA_PATH = os.path.join(os.path.dirname(BASE_DIR), "scribd_fonts.json")',
        content
    )

    # 2. Fix IMAGES_DIR and FONTS_DIR fallback
    content = re.sub(
        r'IMAGES_DIR\s*=\s*os\.path\.join\(BASE_DIR,\s*"scribd_raw",\s*"images"\)',
        'IMAGES_DIR = os.path.join(BASE_DIR, "scribd_raw", "images")\n'
        'if not os.path.exists(IMAGES_DIR):\n'
        '    IMAGES_DIR = os.path.join(os.path.dirname(BASE_DIR), "scribd_raw", "images")',
        content
    )
    content = re.sub(
        r'FONTS_DIR\s*=\s*os\.path\.join\(BASE_DIR,\s*"scribd_raw",\s*"fonts"\)',
        'FONTS_DIR = os.path.join(BASE_DIR, "scribd_raw", "fonts")\n'
        'if not os.path.exists(FONTS_DIR):\n'
        '    FONTS_DIR = os.path.join(os.path.dirname(BASE_DIR), "scribd_raw", "fonts")',
        content
    )

    # 3. Clean any unescaped Resource Card Styles block
    content = re.sub(r'/\* Resource Card Styles \*/.*?\.resource-url \{.*?\}\n', '', content, flags=re.DOTALL)

    # 4. Insert properly escaped Resource Card Styles into the CSS block
    escaped_css = f"""
/* Resource Card Styles */
.resource-card {{{{
  background: #ffffff !important;
  border: 1px solid #cbd5e1 !important;
  border-left: 5px solid {accent} !important;
  border-radius: 8px !important;
  padding: 8px 12px !important;
  margin-bottom: 10px !important;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06) !important;
}}}}
.resource-card-header {{{{
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  margin-bottom: 4px !important;
  padding-bottom: 3px !important;
  border-bottom: 1px solid #f1f5f9 !important;
}}}}
.resource-name {{{{
  font-size: 15px !important;
  font-weight: bold !important;
  color: #1e293b !important;
}}}}
.resource-badge {{{{
  background: #f1f5f9 !important;
  color: {accent} !important;
  border: 1px solid {accent} !important;
  padding: 2px 7px !important;
  border-radius: 12px !important;
  font-size: 10px !important;
  font-weight: bold !important;
}}}}
.resource-row {{{{
  font-size: 11.5px !important;
  line-height: 1.4 !important;
  color: #334155 !important;
  margin-bottom: 3px !important;
}}}}
.resource-label {{{{
  font-weight: bold !important;
  color: #0f172a !important;
}}}}
.resource-url {{{{
  color: {accent} !important;
  font-family: monospace !important;
  font-size: 11px !important;
}}}}
"""
    content = content.replace("</style>", escaped_css + "\n</style>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {filepath} successfully.")

def main():
    for level_dir, script_name, accent in BUILDERS:
        fix_builder(level_dir, script_name, accent)

if __name__ == "__main__":
    main()
