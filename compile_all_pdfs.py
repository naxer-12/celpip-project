#!/usr/bin/env python3
"""
compile_all_pdfs.py - Compile all 5 level PDFs (A2, B1, B2, C1, C2) using Chrome Headless
"""

import os
import subprocess

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_JOBS = [
    ("French_A2", "French_Learning_Roadmap_Checklist_French_A2.html", "French_Learning_Roadmap_Checklist_French_A2.pdf"),
    ("French_B1", "French_Learning_Roadmap_Checklist_French_B1.html", "French_Learning_Roadmap_Checklist_French_B1.pdf"),
    ("French_B2", "French_Learning_Roadmap_Checklist_French_B2.html", "French_Learning_Roadmap_Checklist_French_B2.pdf"),
    ("French_C1", "French_Learning_Roadmap_Checklist_French_C1.html", "French_Learning_Roadmap_Checklist_French_C1.pdf"),
    ("French_C2", "French_Learning_Roadmap_Checklist_French_C2.html", "French_Learning_Roadmap_Checklist_French_C2.pdf"),
]

def compile_pdf(level_dir, html_name, pdf_name):
    html_path = os.path.join(ROOT_DIR, level_dir, html_name)
    pdf_path = os.path.join(ROOT_DIR, level_dir, pdf_name)
    
    cmd = [
        CHROME_BIN,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path}"
    ]
    print(f"Compiling {pdf_name}...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
        print(f"SUCCESS: {pdf_name} ({size_mb:.2f} MB)")
    else:
        print(f"FAILED: {pdf_name}")
        print("STDERR:", res.stderr[:300])

def main():
    for level_dir, html_name, pdf_name in PDF_JOBS:
        compile_pdf(level_dir, html_name, pdf_name)

if __name__ == "__main__":
    main()
