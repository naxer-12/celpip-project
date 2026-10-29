#!/usr/bin/env python3
"""
render_companion_pdf.py - HTML/CSS Single-Page Template & Headless Chrome Rendering

Generates 33 single-page French A1 vocabulary companion sheets from `companion_data.json`.
Compiles the complete document into `companion_pages.html` styled with modern CSS Paged Media,
and invokes macOS Headless Google Chrome to render `companion_pages.pdf` (33 pages, US Letter).
"""

import json
import logging
import os
import subprocess
import sys
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "companion_data.json"
HTML_OUTPUT_PATH = BASE_DIR / "companion_pages.html"
PDF_OUTPUT_PATH = BASE_DIR / "companion_pages.pdf"

CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")


def generate_html(data: dict) -> str:
    """Generate HTML5 document for all 33 companion pages using CSS Paged Media."""
    html_pages = []

    for ch_idx in range(1, 34):
        ch_key = str(ch_idx)
        if ch_key not in data:
            raise KeyError(f"Chapter {ch_key} not found in companion data")

        d = data[ch_key]
        ch_num = d["ch_num"]
        title_fr = d["title_fr"]
        title_en = d["title_en"]
        theme_badge = d["theme_badge"]
        scenario_title = d["scenario_title"]
        scenario_context = d["scenario_context"]
        dialogue = d["dialogue_or_story"]
        cultural_tip = d["cultural_tip"]
        ex1 = d["exercise_1"]
        ex2 = d["exercise_2"]
        ex3 = d["exercise_3"]
        answers = d["answers"]

        # Dialogue rows
        dialogue_html = []
        for line in dialogue:
            spk = line["speaker"]
            fr = line["fr"]
            en = line["en"]
            dialogue_html.append(f"""
            <div class="dialogue-item">
              <div class="dialogue-fr"><strong class="speaker">{spk} :</strong> {fr}</div>
              <div class="dialogue-en">{en}</div>
            </div>""")
        dialogue_block = "\n".join(dialogue_html)

        # Ex 1 items
        ex1_items_html = "\n".join(
            f'<div class="ex-item">{item}</div>' for item in ex1["items"]
        )

        # Ex 2 items
        ex2_items_html = "\n".join(
            f'<div class="ex-item">{p}</div>' for p in ex2["prompts"]
        )

        # Ex 3 items
        ex3_items_html = "\n".join(
            f'<div class="ex-item">{item}</div>' for item in ex3["items"]
        )

        page_html = f"""
    <!-- UNIT PAGE {ch_num:02d} -->
    <div class="unit-page" id="ch-{ch_num:02d}">
      <!-- HEADER BANNER -->
      <header class="header-banner">
        <div class="header-left">
          <div class="header-top-row">
            <span class="chapter-badge">CHAPITRE {ch_num:02d}</span>
            <span class="companion-subtitle-pill">FICHE D'IMMERSION &amp; CONSOLIDATION ACTIVE</span>
          </div>
          <h1 class="chapter-title-fr">{title_fr}</h1>
          <div class="chapter-title-en">{title_en}</div>
        </div>
        <div class="header-right">
          <span class="theme-badge">{theme_badge}</span>
          <span class="curriculum-level">NIVEAU DÉBUTANT A1 • VOCABULAIRE ESSENTIEL</span>
        </div>
      </header>

      <!-- PARTIE A: IMMERSION & RÉCIT VIVANT -->
      <section class="partie-a">
        <div class="section-header">
          <span class="section-tag">PARTIE A</span>
          <span class="section-title-text">Immersion Contextuelle &amp; Récit Vivant</span>
        </div>
        <div class="scenario-meta">
          <span class="scenario-title">Scénario : {scenario_title}</span>
          <span class="scenario-context">— {scenario_context}</span>
        </div>
        <div class="dialogue-list">
          {dialogue_block}
        </div>
        <div class="cultural-tip">
          <div class="tip-header">💡 REPÈRE CULTUREL &amp; USAGES</div>
          <div class="tip-body">{cultural_tip}</div>
        </div>
      </section>

      <!-- PARTIE B: EXERCICES D'ANCRAGE COGNITIF -->
      <section class="partie-b">
        <div class="section-header">
          <span class="section-tag">PARTIE B</span>
          <span class="section-title-text">Exercices d'Ancrage Cognitif &amp; Mémorisation</span>
        </div>
        
        <!-- EX 1: Complétion Contextuelle -->
        <div class="exercise-box ex1">
          <div class="ex-header">
            <span class="ex-badge">EXERCICE 1</span>
            <span class="ex-title">{ex1['title']}</span>
            <span class="ex-instruction">— {ex1['instruction']}</span>
          </div>
          <div class="ex-items">
            {ex1_items_html}
          </div>
        </div>

        <!-- EX 2 & 3: Défi Créatif & Chasse à l'Intrus -->
        <div class="exercise-row-2col">
          <div class="exercise-box ex2">
            <div class="ex-header">
              <span class="ex-badge">EXERCICE 2</span>
              <span class="ex-title">{ex2['title']}</span>
            </div>
            <div class="ex-instruction-sub">{ex2['instruction']}</div>
            <div class="ex-items">
              {ex2_items_html}
            </div>
          </div>

          <div class="exercise-box ex3">
            <div class="ex-header">
              <span class="ex-badge">EXERCICE 3</span>
              <span class="ex-title">{ex3['title']}</span>
            </div>
            <div class="ex-instruction-sub">{ex3['instruction']}</div>
            <div class="ex-items">
              {ex3_items_html}
            </div>
          </div>
        </div>
      </section>

      <!-- FOOTER & AUTO-CORRECTION -->
      <footer class="footer-container">
        <div class="answer-box">
          <div class="answer-title">🔑 SOLUTIONS &amp; AUTO-CORRECTION (Vérification autonome après réalisation) :</div>
          <div class="answer-text">{answers}</div>
        </div>
        <div class="bottom-nav">
          <span>VOCABULAIRE ESSENTIEL DU FRANÇAIS A1 • ÉDITION COMPAGNON IMMERSION</span>
          <span>CHAPITRE {ch_num:02d} • PAGE DE CONSOLIDATION (3/3)</span>
        </div>
      </footer>
    </div>"""
        html_pages.append(page_html)

    pages_content = "\n".join(html_pages)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vocabulaire Essentiel A1 — Fiches Compagnon d'Immersion</title>
<style>
@page {{
  size: letter;
  margin: 0;
}}
* {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}}
body {{
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  color: #1E293B;
  background-color: #FFFFFF;
  -webkit-font-smoothing: antialiased;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}}

/* STRICT 1-PAGE PER UNIT */
.unit-page {{
  width: 8.5in;
  height: 11in;
  box-sizing: border-box;
  padding: 0.35in 0.40in;
  page-break-after: always;
  break-after: page;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #FFFFFF;
}}
.unit-page:last-child {{
  page-break-after: avoid;
  break-after: avoid;
}}

/* HEADER BANNER */
.header-banner {{
  border-bottom: 2.5px solid #1A365D;
  padding-bottom: 5px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
}}
.header-left {{
  display: flex;
  flex-direction: column;
  gap: 2px;
}}
.header-top-row {{
  display: flex;
  align-items: center;
  gap: 8px;
}}
.chapter-badge {{
  background: #1A365D;
  color: #FFFFFF;
  font-size: 8.5pt;
  font-weight: 800;
  letter-spacing: 0.8px;
  padding: 2px 7px;
  border-radius: 3px;
  text-transform: uppercase;
}}
.companion-subtitle-pill {{
  color: #D97706;
  font-size: 8pt;
  font-weight: 800;
  letter-spacing: 0.5px;
  text-transform: uppercase;
}}
.chapter-title-fr {{
  font-size: 14pt;
  font-weight: 800;
  color: #1A365D;
  line-height: 1.15;
}}
.chapter-title-en {{
  font-size: 8.5pt;
  color: #64748B;
  font-style: italic;
}}
.header-right {{
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
}}
.theme-badge {{
  background: #FEF3C7;
  border: 1px solid #D97706;
  color: #92400E;
  font-size: 7.5pt;
  font-weight: 800;
  letter-spacing: 0.6px;
  padding: 2.5px 9px;
  border-radius: 12px;
  text-transform: uppercase;
  white-space: nowrap;
}}
.curriculum-level {{
  font-size: 7.5pt;
  font-weight: 600;
  color: #64748B;
  letter-spacing: 0.4px;
}}

/* SECTION HEADERS */
.section-header {{
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 4px;
}}
.section-tag {{
  background: #1A365D;
  color: #FFFFFF;
  font-size: 7.5pt;
  font-weight: 800;
  letter-spacing: 0.5px;
  padding: 1.5px 6px;
  border-radius: 3px;
}}
.section-title-text {{
  font-size: 9pt;
  font-weight: 800;
  color: #1A365D;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}}

/* PARTIE A: IMMERSION & DIALOGUE */
.partie-a {{
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-left: 3.5px solid #1A365D;
  border-radius: 4px;
  padding: 7px 10px;
}}
.scenario-meta {{
  display: flex;
  align-items: baseline;
  gap: 6px;
  margin-bottom: 5px;
  padding-bottom: 4px;
  border-bottom: 1px dashed #E2E8F0;
}}
.scenario-title {{
  font-size: 8.5pt;
  font-weight: 700;
  color: #0F172A;
}}
.scenario-context {{
  font-size: 8pt;
  color: #64748B;
  font-style: italic;
}}
.dialogue-list {{
  display: flex;
  flex-direction: column;
  gap: 3.5px;
}}
.dialogue-item {{
  display: flex;
  flex-direction: column;
  line-height: 1.25;
}}
.dialogue-fr {{
  font-size: 8.5pt;
  color: #0F172A;
}}
.dialogue-fr strong.speaker {{
  color: #1A365D;
  font-weight: 700;
}}
.dialogue-fr b {{
  color: #1A365D;
  background: #EFF6FF;
  padding: 0 2px;
  border-radius: 2px;
  font-weight: 700;
}}
.dialogue-en {{
  font-size: 7.5pt;
  color: #64748B;
  font-style: italic;
  padding-left: 10px;
}}
.cultural-tip {{
  margin-top: 6px;
  background: #FFFBEB;
  border: 1px solid #FDE68A;
  border-left: 3px solid #D97706;
  border-radius: 3px;
  padding: 4px 8px;
}}
.tip-header {{
  font-size: 7pt;
  font-weight: 800;
  color: #92400E;
  letter-spacing: 0.5px;
  margin-bottom: 1px;
}}
.tip-body {{
  font-size: 7.5pt;
  color: #78350F;
  line-height: 1.25;
}}

/* PARTIE B: EXERCICES */
.partie-b {{
  margin-top: 2px;
}}
.exercise-box {{
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 4px;
  padding: 6px 9px;
}}
.ex-header {{
  display: flex;
  align-items: center;
  gap: 6px;
  margin-bottom: 3px;
}}
.ex-badge {{
  background: #D97706;
  color: #FFFFFF;
  font-size: 7pt;
  font-weight: 800;
  padding: 1.5px 5px;
  border-radius: 2px;
  letter-spacing: 0.4px;
}}
.ex-title {{
  font-size: 8pt;
  font-weight: 700;
  color: #1A365D;
}}
.ex-instruction {{
  font-size: 7.5pt;
  color: #64748B;
  font-style: italic;
}}
.ex-instruction-sub {{
  font-size: 7pt;
  color: #64748B;
  font-style: italic;
  margin-bottom: 3px;
}}
.ex-items {{
  display: flex;
  flex-direction: column;
  gap: 3px;
}}
.ex-item {{
  font-size: 8pt;
  color: #1E293B;
  line-height: 1.25;
}}
.exercise-row-2col {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-top: 5px;
}}

/* FOOTER & AUTO-CORRECTION */
.footer-container {{
  margin-top: 3px;
}}
.answer-box {{
  background: #F8FAFC;
  border: 1px dashed #CBD5E1;
  border-radius: 3px;
  padding: 4px 8px;
}}
.answer-title {{
  font-size: 7pt;
  font-weight: 800;
  color: #475569;
  letter-spacing: 0.4px;
  margin-bottom: 1px;
}}
.answer-text {{
  font-size: 7pt;
  color: #64748B;
  line-height: 1.25;
}}
.bottom-nav {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 3px;
  margin-top: 3px;
  border-top: 1px solid #E2E8F0;
  font-size: 7pt;
  color: #94A3B8;
  font-weight: 500;
}}
</style>
</head>
<body>
{pages_content}
</body>
</html>
"""


def render_pdf_with_chrome(html_path: Path, pdf_path: Path) -> None:
    """Invoke headless Google Chrome to compile HTML into PDF."""
    if not os.path.exists(CHROME_BIN):
        raise FileNotFoundError(f"Headless Chrome binary not found at: {CHROME_BIN}")

    file_url = f"file://{html_path.resolve()}"
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        "--no-pdf-header-footer",
        file_url,
    ]
    logging.info(f"Executing Chrome headless render: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        logging.error(f"Chrome rendering failed: {result.stderr}")
        raise RuntimeError(f"Chrome exit code {result.returncode}: {result.stderr}")

    logging.info(f"Successfully generated PDF at: {pdf_path}")


def main():
    """Main execution pipeline for rendering companion pages."""
    logging.info(f"Reading companion data from: {DATA_PATH}")
    if not DATA_PATH.exists():
        logging.error(f"Data file does not exist: {DATA_PATH}")
        sys.exit(1)

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    logging.info(f"Loaded {len(data)} chapters from companion_data.json")

    logging.info(f"Writing HTML to: {HTML_OUTPUT_PATH}")
    html_content = generate_html(data)
    with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(html_content)

    logging.info(f"Rendering PDF to: {PDF_OUTPUT_PATH}")
    render_pdf_with_chrome(HTML_OUTPUT_PATH, PDF_OUTPUT_PATH)

    # Sanity check
    import pypdf
    reader = pypdf.PdfReader(str(PDF_OUTPUT_PATH))
    page_count = len(reader.pages)
    logging.info(f"Rendered PDF page count: {page_count}")
    if page_count != 33:
        logging.error(f"Expected 33 pages, but got {page_count}")
        sys.exit(1)

    logging.info("All 33 companion pages rendered cleanly and verified!")


if __name__ == "__main__":
    main()
