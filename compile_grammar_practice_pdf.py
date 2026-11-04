#!/usr/bin/env python3
"""
compile_grammar_practice_pdf.py - Render French_Grammar_Practice_A1_A2.html to PDF via Playwright
"""

import os
from playwright.sync_api import sync_playwright

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(ROOT_DIR, "French_Grammar_Practice_A1_A2.html")
PDF_PATH = os.path.join(ROOT_DIR, "French_Grammar_Practice_A1_A2.pdf")


def compile_pdf():
    if not os.path.exists(HTML_PATH):
        raise FileNotFoundError(f"Source HTML file not found: {HTML_PATH}")

    print(f"Loading {HTML_PATH}...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file://{HTML_PATH}")
        page.wait_for_load_state("networkidle")

        print("Rendering print PDF...")
        page.emulate_media(media="print")
        page.pdf(
            path=PDF_PATH,
            format="A4",
            print_background=True,
            margin={"top": "18mm", "right": "18mm", "bottom": "20mm", "left": "18mm"},
        )
        browser.close()

    size_kb = os.path.getsize(PDF_PATH) / 1024
    print(f"SUCCESS: Generated {PDF_PATH} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    compile_pdf()
