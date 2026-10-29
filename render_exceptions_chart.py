# render_exceptions_chart.py
# Standalone renderer for the Visual Atlas & Master Chart of French Gender Traps

import os
import subprocess
from exceptions_chart_data import EXCEPTIONS_DATABASE
from css_styles import MODERN_EDITORIAL_CSS

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = "/Users/jainamshah/Downloads/Learning French"

def render_exception_card_html(item):
    badge_class = "badge-fem" if item["gender"] == "feminine" else "badge-masc"
    gender_label = "FÉMININ" if item["gender"] == "feminine" else "MASCULIN"
    border_color = "#e11d48" if item["gender"] == "feminine" else "#4f46e5"
    bg_tint = "#fff5f5" if item["gender"] == "feminine" else "#f0f4ff"

    return f"""
    <div class="exception-visual-card" style="border-left: 4px solid {border_color}; background: #ffffff;">
      <div style="display: flex; gap: 12px; align-items: center; border-bottom: 1px solid #f1f5f9; padding-bottom: 8px; margin-bottom: 8px;">
        <div class="exception-svg-wrap" style="background: {bg_tint}; padding: 6px; border-radius: 8px; flex-shrink: 0;">
          {item['svg']}
        </div>
        <div style="flex-grow: 1;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-family: 'Playfair Display', serif; font-size: 13pt; font-weight: 700; color: #0f172a;">{item['french']}</span>
            <span class="badge {badge_class}">{gender_label}</span>
          </div>
          <div style="font-size: 8.5pt; font-weight: 600; color: #334155;">{item['english']}</div>
        </div>
      </div>

      <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 5px; padding: 5px 8px; font-size: 7.5pt; color: #92400e; margin-bottom: 8px;">
        <strong>⚠️ Piège :</strong> {item['deceptive_rule']}
      </div>

      <div style="background: #f8fafc; border-radius: 5px; padding: 6px 8px; margin-bottom: 8px;">
        <div style="display: flex; align-items: baseline; gap: 6px;">
          <span style="font-size: 8pt; font-weight: 700; color: #4338ca;">🔊 Prononciation :</span>
          <span style="font-family: 'JetBrains Mono', monospace; font-size: 8.5pt; font-weight: 700; color: #0f172a;">[{item['phonetic']}]</span>
          <span style="font-size: 7.5pt; color: #64748b; font-style: italic;">({item['syllables']})</span>
        </div>
        <div style="font-size: 7pt; color: #475569; margin-top: 2px;">
          <strong>Guide phonétique :</strong> {item['sound_tip']}
        </div>
      </div>

      <div style="font-size: 7.5pt; color: #334155; margin-bottom: 6px;">
        <strong>Astuce Mémoire :</strong> {item['mnemonic']}
      </div>

      <div style="border-top: 1px dashed #e2e8f0; padding-top: 5px; font-size: 7.5pt;">
        <div style="font-style: italic; color: #1e293b;">« {item['example_fr']} »</div>
        <div style="color: #64748b; font-size: 7pt;">{item['example_en']}</div>
      </div>
    </div>
    """

def generate_exceptions_chart_html():
    cards = [render_exception_card_html(item) for item in EXCEPTIONS_DATABASE]

    return f"""
    <div class="cover-page" style="page-break-after: always; height: auto; min-height: 94vh;">
      <div class="cover-pill-box">
        <span class="cover-pill" style="background: #fef3c7; color: #92400e; border-color: #fde68a;">ATLAS VISUEL DES EXCEPTIONS</span>
        <span class="cover-pill cover-pill-accent">FLE MAÎTRISE</span>
      </div>
      <div class="cover-main" style="margin-top: 20px;">
        <div class="cover-kicker">RÉPERTOIRE ILLUSTRÉ DES FAUX AMIS & PIÈGES DE GENRE</div>
        <h1 class="cover-title" style="font-size: 26pt;">Le Grand Tableau Illustré des Exceptions</h1>
        <p class="cover-subtitle" style="font-size: 11pt;">
          Une cartographie visuelle complète des 36 mots trompeurs majeurs de la langue française. Chaque fiche associe une illustration vectorielle, la règle enfreinte, une prononciation intuitive et une ancre mnémotechnique indélébile.
        </p>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 18px;">
          <div class="feature-box">
            <div class="feature-box-title"><span>👁️</span> ANCRAGE VISUEL</div>
            <div class="feature-box-desc">Chaque exception possède son icône dédiée pour créer une empreinte visuelle immédiate dans la mémoire.</div>
          </div>
          <div class="feature-box">
            <div class="feature-box-title"><span>🔊</span> PHONÉTIQUE INTUITIVE</div>
            <div class="feature-box-desc">Découpage syllabique et astuces phonétiques pour anglophones (lettres muettes, voyelles nasales).</div>
          </div>
          <div class="feature-box">
            <div class="feature-box-title"><span>💡</span> HISTOIRE MNÉMOTECHNIQUE</div>
            <div class="feature-box-desc">Une phrase narrative frappante pour ne plus jamais hésiter entre 'le' et 'la'.</div>
          </div>
        </div>
      </div>
      <div class="cover-footer">
        <div><strong>Édition Illustrée Grand Format</strong> • Conforme aux Chapitres 2 & 3 du FLE All-in-One</div>
        <div>Système Editorial Minimaliste • Chroma Pastels</div>
      </div>
    </div>

    <div style="page-break-before: always; margin-top: 10px;">
      <div class="chapter-hero">
        <span class="chapter-badge">ATLAS VISUEL • PARTIE 1</span>
        <h2 class="chapter-title">Les Faux Noms Masculins (Mots en Suffixe Masculin qui sont FÉMININS)</h2>
        <p class="chapter-subtitle">Ces noms se terminent par -age, -eau, -ain, -ent, -is ou une consonne, mais sont rigoureusement féminins.</p>
      </div>
      <div class="exceptions-grid">
        {''.join(cards[:18])}
      </div>
    </div>

    <div style="page-break-before: always; margin-top: 10px;">
      <div class="chapter-hero">
        <span class="chapter-badge">ATLAS VISUEL • PARTIE 2</span>
        <h2 class="chapter-title">Les Faux Noms Féminins (Mots en Suffixe Féminin qui sont MASCULINS)</h2>
        <p class="chapter-subtitle">Ces noms se terminent par -ence, -ée, -ette, -eur, -ie, -té ou le 'e' muet, mais sont rigoureusement masculins.</p>
      </div>
      <div class="exceptions-grid">
        {''.join(cards[18:])}
      </div>
    </div>
    """

def build_standalone_exceptions_pdf():
    chart_content = generate_exceptions_chart_html()
    extra_css = """
    .exceptions-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin: 12px 0;
    }
    .exception-visual-card {
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 10px 12px;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
      break-inside: avoid;
    }
    """
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>French Noun Gender - Visual Exceptions Atlas</title>
<style>
{MODERN_EDITORIAL_CSS}
{extra_css}
</style>
</head>
<body>
{chart_content}
</body>
</html>"""

    html_path = os.path.join(OUTPUT_DIR, "French_Gender_Exceptions_Visual_Chart.html")
    pdf_path = os.path.join(OUTPUT_DIR, "French_Gender_Exceptions_Visual_Chart.pdf")

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Wrote HTML source to {html_path}")

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--enable-local-file-access",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        file_size = os.path.getsize(pdf_path)
        print(f"SUCCESS: Rendered Standalone Exceptions Visual Chart: {pdf_path} ({file_size} bytes)")
    else:
        print(f"ERROR: Chrome failed with code {res.returncode}")
        print(res.stderr)

if __name__ == "__main__":
    build_standalone_exceptions_pdf()
