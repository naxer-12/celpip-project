# build_publications.py
# Master HTML assembler and PDF renderer for French Noun Gender Publications

import subprocess
import os
import json
from rules_data import RULES_CHAPTERS
from vocab_data import ALL_VOCABULARY
from worksheet_data import ALL_WORKSHEET_SECTIONS
from exceptions_chart_data import EXCEPTIONS_DATABASE
from render_exceptions_chart import render_exception_card_html, build_standalone_exceptions_pdf
from css_styles import MODERN_EDITORIAL_CSS

CHROME_PATH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUTPUT_DIR = "/Users/jainamshah/Downloads/Learning French"

def get_badge_class(gender):
    if gender == "masculine":
        return "badge-masc"
    elif gender == "feminine":
        return "badge-fem"
    elif gender == "dual":
        return "badge-dual"
    return "badge-amber"

def render_cover_html(title, subtitle, kicker, badge1="FLE PÉDAGOGIE", badge2="A1 → C2 COMPLET"):
    return f"""
    <div class="cover-page">
      <div class="cover-pill-box">
        <span class="cover-pill">{badge1}</span>
        <span class="cover-pill cover-pill-accent">{badge2}</span>
      </div>
      <div class="cover-main">
        <div class="cover-kicker">{kicker}</div>
        <h1 class="cover-title">{title}</h1>
        <p class="cover-subtitle">{subtitle}</p>
        <div class="cover-features-grid">
          <div class="feature-box">
            <div class="feature-box-title"><span>✦</span> NARRATION HISTORIQUE & GUEULOIR</div>
            <div class="feature-box-desc">Le test acoustique de Flaubert, la conquête normande de 1066, la création d'« ordinateur » et la bataille politique de la féminisation.</div>
          </div>
          <div class="feature-box">
            <div class="feature-box-title"><span>🔊</span> GUIDE PHONÉTIQUE INTUITIF</div>
            <div class="feature-box-desc">Découpage syllabique, astuces acoustiques et règles des consonnes muettes pour une prononciation naturelle sans accent plat.</div>
          </div>
          <div class="feature-box">
            <div class="feature-box-title"><span>◈</span> ATLAS VISUEL DES EXCEPTIONS</div>
            <div class="feature-box-desc">36 fiches illustrées avec icônes vectorielles dédiées pour fixer visuellement chaque piège trompeur (plage, eau, silence, squelette...).</div>
          </div>
          <div class="feature-box">
            <div class="feature-box-title"><span>⚡</span> CAHIER D'ACTIVITÉS EN 6 NIVEAUX</div>
            <div class="feature-box-desc">140 exercices intensifs (drills de rapidité, chasse aux pièges, double genre, accords) avec corrigé intégral expliqué pas à pas.</div>
          </div>
        </div>
      </div>
      <div class="cover-footer">
        <div>
          <div class="cover-author">Édition Pédagogique de Référence • FLE All-in-One</div>
          <div>Conforme aux normes du CECRL (Cadre Européen Commun de Référence pour les Langues)</div>
        </div>
        <div style="text-align: right;">
          <div>Format Grand Format A4 / Letter</div>
          <div>Système Minimaliste Éditorial Français</div>
        </div>
      </div>
    </div>
    """

def render_toc_html(include_rules=True, include_exceptions=True, include_vocab=True, include_worksheet=True, include_answers=True):
    items = []
    if include_rules:
        items.append(("01", "L'Architecture Musicale du Genre & Le Gueuloir de Flaubert", "L'intuition acoustique, l'héritage latin, la conquête de 1066 et la création d'« ordinateur »"))
        items.append(("02", "Les Suffixes de la Gamme Masculine & Leurs Pièges", "Les terminaisons régulières (-age, -eau, -ment, -al...), les neutres grecs en -ma et la formule Plage-Cage"))
        items.append(("03", "Les Suffixes de la Gamme Féminine & Leurs Exceptions", "Les terminaisons abstraites (-tion, -té, -ence, -ure...) et le squelette de l'exception"))
        items.append(("04", "Champs Sémantiques : Pouvoir, Géographie, Animaux & Marques", "Féminisation des métiers (Lionel Jospin, Roselyne Bachelot), départements de 1789 et Barbie"))
        items.append(("05", "Noms à Double Genre, Décalages Sémantiques & Homophones", "Livre, tour, poêle, voile, manche, et le mystère poétique de 'gens' et d'Amour, Délice, Orgue"))
    if include_exceptions:
        items.append(("06", "L'Atlas Visuel Illustré des 36 Exceptions Majeures", "Cartographie graphique des faux amis de genre avec illustrations vectorielles et phonétique"))
    if include_vocab:
        items.append(("07", "Le Grand Coffre Lexical Progressif : A1 → C2 (200 Noms)", "Inventaire complet ordonné par niveau avec prononciation intuitive, mnémotechnique et exemples"))
    if include_worksheet:
        items.append(("08", "Cahier d'Entraînement Intensif en 6 Niveaux (140 Items)", "Drills de rapidité, chasseurs de pièges, matrice de double genre et phrases à compléter"))
    if include_answers:
        items.append(("09", "Corrigé Détaillé & Justifications Pédagogiques", "Solutions pas à pas pour l'ensemble des 140 questions avec renvois explicites aux règles"))

    toc_rows = "".join([f"""
      <div style="display: flex; gap: 14px; margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px dotted #cbd5e1; break-inside: avoid;">
        <div style="font-family: 'Playfair Display', serif; font-size: 14pt; font-weight: 700; color: #4f46e5; width: 32px;">{num}</div>
        <div style="flex-grow: 1;">
          <div style="font-weight: 700; font-size: 9.5pt; color: #0f172a;">{title}</div>
          <div style="font-size: 8pt; color: #64748b; font-style: italic;">{desc}</div>
        </div>
      </div>
    """ for num, title, desc in items])

    return f"""
    <div style="page-break-before: always; margin-bottom: 24px;">
      <div class="chapter-hero">
        <span class="chapter-badge">SOMMAIRE GÉNÉRAL</span>
        <h2 class="chapter-title">Table des Matières & Architecture Pédagogique</h2>
        <p class="chapter-subtitle">Une progression rigoureuse alliant synthèse culturelle, intuition sonore, repères visuels et mise en pratique.</p>
      </div>
      <div style="max-width: 650px; margin-top: 18px;">
        {toc_rows}
      </div>
    </div>
    """

def render_pronunciation_guide_html():
    return """
    <div style="page-break-before: always; margin-bottom: 24px;">
      <div class="chapter-hero">
        <span class="chapter-badge">MÉTHODE ACOUSTIQUE</span>
        <h2 class="chapter-title">Guide d'Intuition Phonétique pour Anglophones</h2>
        <p class="chapter-subtitle">Les 5 règles d'or pour déchiffrer la prononciation française sans hésitation ni accent plat.</p>
      </div>
      <div class="pronunciation-master-box">
        <div style="font-weight: 700; font-size: 9.5pt; color: #1e1b4b; margin-bottom: 8px;">
          ✦ Le Code Phonétique Utilisé dans cet Ouvrage
        </div>
        <p style="font-size: 8pt; color: #334155; line-height: 1.45; margin-bottom: 12px;">
          Le français ne se lit pas lettre par lettre. Pour chaque mot de notre lexique, nous fournissons une transcription phonétique intuitive avec les syllabes accentuées en <strong>MAJUSCULES</strong>, le découpage rythmique, et l'astuce acoustique.
        </p>
        <div class="pron-grid">
          <div class="pron-row">
            <span class="pron-symbol">[AHN]</span>
            <strong>Voyelle nasale ouverte (an, en, am, em) :</strong>
            <br>L'air passe par le nez, la bouche reste ouverte comme pour dire 'ah'. Ne prononcez <em>jamais</em> le 'n' !
            <br><em>Exemples :</em> <strong>le vent</strong> [luh VAHN], <strong>le silence</strong> [luh see-LAHNS].
          </div>
          <div class="pron-row">
            <span class="pron-symbol">[AN]</span>
            <strong>Voyelle nasale plate (in, ain, ein, un) :</strong>
            <br>Sourire large, son nasal rappelant le 'a' de <em>cat</em> projeté dans le nez. Le 'n' reste muet.
            <br><em>Exemples :</em> <strong>le pain</strong> [luh PAN], <strong>le vin</strong> [luh VAN], <strong>la main</strong> [lah MAN].
          </div>
          <div class="pron-row">
            <span class="pron-symbol">[OHN]</span>
            <strong>Voyelle nasale ronde (on, om) :</strong>
            <br>Lèvres très arrondies en 'o', son nasal profond. Pas de 'n' consonantique.
            <br><em>Exemples :</em> <strong>le pont</strong> [luh POHN], <strong>la maison</strong> [lah may-ZOHN].
          </div>
          <div class="pron-row">
            <span class="pron-symbol">[EW]</span>
            <strong>Le 'U' français pur (u, û, eu) :</strong>
            <br>Placez votre bouche pour siffler (lèvres très serrées en avant) et essayez de prononcer un 'ee' anglais.
            <br><em>Exemples :</em> <strong>le musée</strong> [luh mew-ZAY], <strong>la voiture</strong> [lah vwah-TYOOR].
          </div>
          <div class="pron-row">
            <span class="pron-symbol">[ZH]</span>
            <strong>Le 'J' et 'G' doux (j, ge, gi) :</strong>
            <br>Friction douce identique au 's' dans les mots anglais <em>measure, pleasure, vision</em>.
            <br><em>Exemples :</em> <strong>le fromage</strong> [luh froh-MAHZH], <strong>la plage</strong> [lah PLAHZH].
          </div>
          <div class="pron-row">
            <span class="pron-symbol">SILENT</span>
            <strong>La Règle CaReFuL des Consonnes Finales :</strong>
            <br>En règle générale, les consonnes finales <em>-d, -p, -s, -t, -x, -z</em> sont <strong>TOTALEMENT MUETTES</strong> !
            <br>Seules les consonnes du mot <strong>CaReFuL</strong> (C, R, F, L) se prononcent habituellement.
            <br><em>Exemples :</em> <strong>la nuit</strong> [lah NWEE] (t muet), <strong>le chat</strong> [luh SHAH] (t muet), <strong>la voix</strong> [lah VWAH] (x muet).
          </div>
        </div>
      </div>
    </div>
    """

def render_rules_html():
    html = []
    for ch in RULES_CHAPTERS:
        html.append(f"""
        <div class="chapter-hero">
          <span class="chapter-badge">MODULE {ch['num']}</span>
          <h2 class="chapter-title">{ch['title']}</h2>
          <p class="chapter-subtitle">{ch['subtitle']}</p>
        </div>
        <div style="font-size: 8.5pt; color: #334155; margin-bottom: 14px; line-height: 1.48;">
          {ch['intro']}
        </div>
        """)

        # Check sections
        if "sections" in ch:
            for sec in ch["sections"]:
                html.append(f"""
                <div class="section-hero">
                  <h3 class="section-title"><span>✦</span> {sec['title']}</h3>
                </div>
                <div style="font-size: 8.5pt; color: #334155; line-height: 1.48;">
                  {sec['content']}
                </div>
                """)

        # Check endings
        if "endings" in ch:
            for end in ch["endings"]:
                badge_type = "badge-masc" if "Masculine" in end["nature"] else "badge-fem"
                ex_words = "".join([f"""
                  <div class="word-item">
                    <span class="word-fr">{w['fr']}</span>
                    <span class="word-en">{w['en']}</span>
                  </div>
                """ for w in end["examples"]])

                exc_block = ""
                if end["exceptions"]:
                    exc_items = "".join([f"""
                      <div class="word-item" style="border-bottom-color: #fecdd3;">
                        <span class="word-fr" style="color: #be123c;">{e['fr']}</span>
                        <span class="word-en">{e['en']}</span>
                      </div>
                    """ for e in end["exceptions"]])
                    exc_block = f"""
                    <div style="margin-top: 8px; padding-top: 6px; border-top: 1px dashed #fecdd3;">
                      <div style="font-size: 7.5pt; font-weight: 700; color: #9f1239; margin-bottom: 4px; text-transform: uppercase;">
                        ⚠️ Pièges & Exceptions Notables ({len(end['exceptions'])}) :
                      </div>
                      <div class="words-grid">
                        {exc_items}
                      </div>
                    </div>
                    """

                html.append(f"""
                <div class="ending-card">
                  <div class="ending-header">
                    <span class="ending-name">{end['suffix']}</span>
                    <span class="badge {badge_type}">{end['nature']}</span>
                  </div>
                  <div style="font-size: 8pt; color: #475569; margin-bottom: 6px;">
                    {end['rules']}
                  </div>
                  <div class="words-grid">
                    {ex_words}
                  </div>
                  {exc_block}
                  <div class="mnemonic-box">
                    <strong>Astuce Mémoire :</strong> {end['mnemonic']}
                  </div>
                </div>
                """)

        # Check categories (Chapter 4)
        if "categories" in ch:
            for cat in ch["categories"]:
                html.append(f"""
                <div class="ending-card" style="margin-bottom: 16px;">
                  <div class="ending-header">
                    <span style="font-size: 10.5pt; font-weight: 700; color: #0f172a;">{cat['name']}</span>
                    <span class="badge badge-amber">CHAMP SÉMANTIQUE</span>
                  </div>
                  <div style="font-size: 8.5pt; color: #334155; line-height: 1.48;">
                    {cat['rules']}
                  </div>
                </div>
                """)

        # Check pairs (Chapter 5)
        if "pairs" in ch:
            html.append("""
            <div class="section-hero">
              <h3 class="section-title"><span>✦</span> Noms Homographes à Double Genre</h3>
            </div>
            """)
            for p in ch["pairs"]:
                html.append(f"""
                <div class="ending-card" style="margin-bottom: 10px;">
                  <div class="ending-header">
                    <span style="font-family: 'JetBrains Mono', monospace; font-size: 11pt; font-weight: 700; color: #4338ca;">{p['word']}</span>
                    <span class="badge badge-dual">VARIATION SÉMANTIQUE</span>
                  </div>
                  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; margin: 4px 0; font-size: 8pt;">
                    <div style="background: #eef2ff; padding: 6px 8px; border-radius: 4px; border-left: 2px solid #4f46e5;">
                      <strong>Masculin :</strong> {p['masc']}
                    </div>
                    <div style="background: #fff1f2; padding: 6px 8px; border-radius: 4px; border-left: 2px solid #e11d48;">
                      <strong>Féminin :</strong> {p['fem']}
                    </div>
                  </div>
                  <div style="font-size: 7.5pt; font-style: italic; color: #475569; margin-top: 4px; background: #fafafa; padding: 4px 8px; border-radius: 4px;">
                    <strong>Exemple en contexte :</strong> {p['sentence']}
                  </div>
                </div>
                """)

        if "gender_shifters" in ch:
            html.append("""
            <div class="section-hero">
              <h3 class="section-title"><span>✦</span> Curiosités Linguistiques & Homophones Acoustiques</h3>
            </div>
            """)
            for gs in ch["gender_shifters"]:
                html.append(f"""
                <div class="callout callout-trap" style="margin-bottom: 12px;">
                  <div style="font-weight: 700; font-size: 9pt; margin-bottom: 4px; color: #92400e;">
                    ◈ {gs['name']}
                  </div>
                  <div style="font-size: 8pt; color: #78350f;">
                    {gs['rule']}
                  </div>
                </div>
                """)

    return "\n".join(html)

def render_visual_exceptions_section_html():
    cards = [render_exception_card_html(item) for item in EXCEPTIONS_DATABASE]
    return f"""
    <div style="page-break-before: always; margin-top: 14px;">
      <div class="chapter-hero">
        <span class="chapter-badge">ATLAS VISUEL DES EXCEPTIONS</span>
        <h2 class="chapter-title">Le Grand Tableau Illustré des Exceptions</h2>
        <p class="chapter-subtitle">Les 36 mots trompeurs essentiels des chapitres 2 et 3 dotés de leurs illustrations vectorielles, découpage phonétique et ancres mnémotechniques.</p>
      </div>
      <div class="exceptions-grid">
        {''.join(cards)}
      </div>
    </div>
    """

def render_vocab_vault_html():
    levels = ["A1", "A2", "B1", "B2", "C1", "C2"]
    level_titles = {
        "A1": "Niveau A1 • Les Fondations Quotidiens & Pièges Élémentaires",
        "A2": "Niveau A2 • Expansion Usuelle & Domaines Thématiques",
        "B1": "Niveau B1 • Autonomie Fonctionnelle & Racines Scientifiques",
        "B2": "Niveau B2 • Maîtrise Avancée & Décalages Sémantiques",
        "C1": "Niveau C1 • Registre Soutenu, Abstractions & Déclinaisons Historiques",
        "C2": "Niveau C2 • Précision Littéraire & Distinctions Acoustiques Rares"
    }

    html = ["""
    <div class="chapter-hero">
      <span class="chapter-badge">LE GRAND RÉPERTOIRE</span>
      <h2 class="chapter-title">Le Coffre Lexical Progressif : A1 → C2</h2>
      <p class="chapter-subtitle">200 noms français indispensables entièrement annotés : genre, prononciation intuitive pour anglophones (syllabes et astuce sonore), ancre mnémotechnique et phrase modèle.</p>
    </div>
    """]

    for lvl in levels:
        lvl_words = [w for w in ALL_VOCABULARY if w["cefr"] == lvl]
        if not lvl_words:
            continue

        cards_html = []
        for w in lvl_words:
            card_class = "is-trap" if w["is_exception"] else (f"is-{w['gender']}")
            badge_class = get_badge_class(w["gender"])

            exc_pill = ""
            if w["is_exception"]:
                exc_pill = '<span class="badge badge-amber" style="margin-left: 4px;">PIÈGE</span>'

            syllables_span = f"<span class='card-syllables'>({w.get('syllables', '')})</span>" if w.get('syllables') else ""
            sound_tip_div = f"<div class='card-sound-tip'><strong>Astuce :</strong> {w.get('sound_tip', '')}</div>" if w.get('sound_tip') else ""

            cards_html.append(f"""
            <div class="vocab-card {card_class}">
              <div>
                <div class="card-top">
                  <span class="card-fr-title">{w['french']}</span>
                  <div>
                    <span class="badge {badge_class}">{w['gender'][:4]}</span>
                    {exc_pill}
                  </div>
                </div>

                <div class="card-pron-box">
                  <span style="font-size: 7.5pt; font-weight: 700; color: #4f46e5;">🔊 </span>
                  <span class="card-phonetic">[{w['phonetic']}]</span>
                  {syllables_span}
                  {sound_tip_div}
                </div>

                <div class="card-en">{w['english']} • <span style="font-size: 7pt; color: #64748b; font-weight: normal;">{w['rule_category']}</span></div>
                <div class="card-mnemonic"><strong>Mémo :</strong> {w['mnemonic']}</div>
              </div>
              <div class="card-example">
                <div class="card-ex-fr">« {w['example_fr']} »</div>
                <div class="card-ex-en">{w['example_en']}</div>
              </div>
            </div>
            """)

        html.append(f"""
        <div style="page-break-before: always; margin-top: 14px;">
          <div class="section-hero">
            <h3 class="section-title"><span>◈</span> {level_titles[lvl]} ({len(lvl_words)} noms)</h3>
          </div>
          <div class="vocab-vault-grid">
            {''.join(cards_html)}
          </div>
        </div>
        """)

    return "\n".join(html)

def render_worksheet_html():
    html = ["""
    <div class="chapter-hero">
      <span class="chapter-badge">CAHIER PRATIQUE</span>
      <h2 class="chapter-title">Cahier d'Exercices en 6 Niveaux de Rétention</h2>
      <p class="chapter-subtitle">140 exercices intensifs conçus pour automatiser la reconnaissance du genre en un seul passage.</p>
    </div>
    """]

    for sec in ALL_WORKSHEET_SECTIONS:
        items_html = []
        if sec["tier"] in ["Tier 1", "Tier 2"]:
            for it in sec["items"]:
                items_html.append(f"""
                <div class="quiz-item">
                  <span class="quiz-num">{it['id']}.</span>
                  <span class="quiz-prompt">{it['prompt']}</span>
                </div>
                """)
            grid_class = "quiz-grid-2col"
        else:
            for it in sec["items"]:
                items_html.append(f"""
                <div class="quiz-item" style="padding: 6px 0;">
                  <span class="quiz-num">{it['id']}.</span>
                  <span class="quiz-prompt">{it['prompt']}</span>
                </div>
                """)
            grid_class = "quiz-grid-2col" if len(sec["items"]) > 10 else ""

        html.append(f"""
        <div class="worksheet-section">
          <div class="worksheet-hero">
            <div style="font-size: 7.5pt; font-weight: 800; color: #4f46e5; letter-spacing: 0.1em; text-transform: uppercase;">{sec['tier']}</div>
            <h3 style="font-size: 13pt; font-weight: 700; color: #0f172a; margin: 2px 0 4px 0;">{sec['title']}</h3>
          </div>
          <div class="exercise-inst">Consigne : {sec['instruction']}</div>
          <div class="{grid_class}">
            {''.join(items_html)}
          </div>
        </div>
        """)

    return "\n".join(html)

def render_answer_key_html():
    html = ["""
    <div class="chapter-hero">
      <span class="chapter-badge">SOLUTIONS & ANALYSE</span>
      <h2 class="chapter-title">Corrigé Intégral & Justifications Pédagogiques</h2>
      <p class="chapter-subtitle">Retrouvez ci-dessous la solution précise de chacun des 140 items, accompagnée de la règle morphologique ou étymologique appliquée.</p>
    </div>
    """]

    for sec in ALL_WORKSHEET_SECTIONS:
        ans_items = []
        for it in sec["items"]:
            ans_items.append(f"""
            <div class="ans-item">
              <div class="ans-header">
                <span class="ans-num">#{it['id']}</span>
                <span class="ans-correct">{it['ans']}</span>
              </div>
              <div class="ans-rule"><strong>Justification :</strong> {it['rule']}</div>
            </div>
            """)

        html.append(f"""
        <div style="page-break-before: always; margin-top: 14px;">
          <div class="section-hero">
            <h3 class="section-title"><span>✓</span> Corrigé {sec['tier']} • {sec['title']}</h3>
          </div>
          <div class="ans-grid">
            {''.join(ans_items)}
          </div>
        </div>
        """)

    return "\n".join(html)

def compile_document(html_content, output_html_path, output_pdf_path):
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>French Noun Gender Mastery</title>
<style>
{MODERN_EDITORIAL_CSS}
</style>
</head>
<body>
{html_content}
</body>
</html>"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Wrote HTML source to {output_html_path}")

    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--enable-local-file-access",
        f"--print-to-pdf={output_pdf_path}",
        output_html_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        file_size = os.path.getsize(output_pdf_path)
        print(f"SUCCESS: Rendered {output_pdf_path} ({file_size} bytes)")
    else:
        print(f"ERROR: Chrome failed with code {res.returncode}")
        print(res.stderr)

def main():
    print("Building French Noun Gender Master Publications with Full Narratives & Visual Exceptions...")

    pronunciation_guide_html = render_pronunciation_guide_html()
    rules_html = render_rules_html()
    visual_exceptions_html = render_visual_exceptions_section_html()
    vocab_html = render_vocab_vault_html()
    worksheet_html = render_worksheet_html()
    answers_html = render_answer_key_html()

    # 1. DELIVERABLE A: MASTER ALL-IN-ONE PUBLICATION
    print("\n--- 1. Compiling Master Edition (All-In-One) ---")
    master_cover = render_cover_html(
        "Le Genre des Noms Français : Guide Ultime & Cahier d'Assimilation",
        "Système exhaustif d'identification des genres du français basé sur l'intuition acoustique, les récits historiques, les suffixes réguliers, un atlas visuel illustré des exceptions, un coffre lexical A1 → C2 et un cahier de rétention en un seul coup.",
        "MANUEL DE RÉFÉRENCE, ATLAS VISUEL & WORKBOOK COMPLET",
        "ÉDITION INTÉGRALE MASTER",
        "A1 → C2 • 140 EXERCICES • ATLAS VISUEL"
    )
    master_toc = render_toc_html(True, True, True, True, True)
    master_content = (master_cover + master_toc + pronunciation_guide_html + rules_html +
                      visual_exceptions_html + vocab_html + worksheet_html + answers_html)
    compile_document(
        master_content,
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Master_Guide.html"),
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Master_Guide.pdf")
    )

    # 2. DELIVERABLE B: STUDY & REFERENCE COMPANION
    print("\n--- 2. Compiling Study Guide Companion ---")
    study_cover = render_cover_html(
        "Grammaire, Histoires & Lexique du Genre des Noms Français",
        "Guide théorique complet couvrant l'ensemble des règles de terminaisons, les récits linguistiques (Flaubert, Jospin, départements de 1789), l'atlas visuel des exceptions et le coffre lexical progressif A1 → C2 annoté.",
        "GUIDE D'ÉTUDE, RÉCITS HISTORIQUES & LEXIQUE COMPLET",
        "LIVRE DE COURS & ATLAS",
        "A1 → C2 VOCABULAIRE & PIÈGES"
    )
    study_toc = render_toc_html(True, True, True, False, False)
    study_content = study_cover + study_toc + pronunciation_guide_html + rules_html + visual_exceptions_html + vocab_html
    compile_document(
        study_content,
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Study_Guide.html"),
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Study_Guide.pdf")
    )

    # 3. DELIVERABLE C: STUDENT WORKBOOK & SOLUTIONS
    print("\n--- 3. Compiling Student Practice Workbook ---")
    workbook_cover = render_cover_html(
        "Cahier d'Exercices du Genre des Noms Français",
        "140 exercices pratiques en 6 niveaux intensifs (réflexes, pièges trompeurs, double genre, accords et progression CECRL) suivis du corrigé intégral expliqué pas à pas.",
        "WORKBOOK D'ENTRAÎNEMENT INTENSIF",
        "CAHIER D'ACTIVITÉS",
        "140 EXERCICES & SOLUTIONS"
    )
    workbook_toc = render_toc_html(False, False, False, True, True)
    workbook_content = workbook_cover + workbook_toc + worksheet_html + answers_html
    compile_document(
        workbook_content,
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Student_Workbook.html"),
        os.path.join(OUTPUT_DIR, "French_Noun_Gender_Student_Workbook.pdf")
    )

    # 4. DELIVERABLE D: STANDALONE VISUAL EXCEPTIONS ATLAS
    print("\n--- 4. Compiling Standalone Exceptions Visual Atlas ---")
    build_standalone_exceptions_pdf()

    print("\nAll 4 French Gender Publications successfully compiled and rendered!")

if __name__ == "__main__":
    main()
