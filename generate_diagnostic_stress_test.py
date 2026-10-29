import os
import sys

# Generator for French Linguistic Diagnostic & Stress-Test Workbook
# Creates both DOCX and PDF formats

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/jainamshah/Downloads/Learning French"
DOCX_PATH = os.path.join(BASE_DIR, "French_Diagnostic_Stress_Test_Workbook.docx")
PDF_PATH = os.path.join(BASE_DIR, "French_Diagnostic_Stress_Test_Workbook.pdf")

# Palette
NAVY_HEX = "0F172A"      # Slate 900
INDIGO_HEX = "1E1B4B"    # Deep Indigo / Oxford
BURGUNDY_HEX = "881337"  # Deep Crimson / Burgundy
AMBER_HEX = "9A3412"     # Rust / Burnt Amber
LIGHT_BG = "F8FAFC"      # Slate 50
CALLOUT_BG = "F1F5F9"    # Slate 100
ALERT_BG = "FFFBEB"      # Amber 50
BORDER_HEX = "CBD5E1"    # Slate 300
DARK_TEXT_HEX = "0F172A"

NAVY_RGB = RGBColor(15, 23, 42)
INDIGO_RGB = RGBColor(30, 27, 75)
BURGUNDY_RGB = RGBColor(136, 19, 55)
AMBER_RGB = RGBColor(154, 52, 18)
DARK_RGB = RGBColor(15, 23, 42)
MUTED_RGB = RGBColor(71, 85, 105)

def style_cell(cell, fill_hex=None, borders=None, pad_tb=100, pad_lr=120):
    tcPr = cell._element.get_or_add_tcPr()
    if fill_hex:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)
    if pad_tb or pad_lr:
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{pad_tb}" w:type="dxa"/>'
            f'<w:bottom w:w="{pad_tb}" w:type="dxa"/>'
            f'<w:left w:w="{pad_lr}" w:type="dxa"/>'
            f'<w:right w:w="{pad_lr}" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)
    if borders is not None:
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
        for edge in ('top', 'left', 'bottom', 'right'):
            if edge in borders:
                b = borders[edge]
                tcBorders.append(parse_xml(
                    f'<w:{edge} {nsdecls("w")} w:val="{b.get("val", "single")}" '
                    f'w:sz="{b.get("sz", "4")}" w:space="0" w:color="{b.get("color", BORDER_HEX)}"/>'
                ))
            else:
                tcBorders.append(parse_xml(f'<w:{edge} {nsdecls("w")} w:val="none"/>'))
        tcPr.append(tcBorders)

def build_docx():
    doc = docx.Document()
    
    # 0.75-inch margins
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
        # Header / Footer
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("French Linguistic Diagnostic & Stress-Test Workbook  |  University Division")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = MUTED_RGB
        
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("Zero-Tolerance Precision Assessment  •  Department of Applied Linguistics")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = MUTED_RGB

    def add_p(text="", style='Normal', space_before=0, space_after=3, bold=False, italic=False, color=DARK_RGB, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        if text:
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.italic = italic
            r.font.color.rgb = color
        return p

    def add_h1(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(15)
        r.font.bold = True
        r.font.color.rgb = INDIGO_RGB
        
        # Divider line
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.columns[0].width = Inches(7.0)
        c = t.cell(0, 0)
        style_cell(c, fill_hex=INDIGO_HEX, borders={}, pad_tb=15, pad_lr=0)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_h2(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = BURGUNDY_RGB
        return p

    def add_callout(title, text, callout_type="info"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(7.0)
        cell = tbl.cell(0, 0)
        
        if callout_type == "alert":
            b_col = AMBER_HEX
            bg_col = ALERT_BG
            t_col = AMBER_RGB
        elif callout_type == "danger":
            b_col = BURGUNDY_HEX
            bg_col = "FFF1F2"
            t_col = BURGUNDY_RGB
        else:
            b_col = INDIGO_HEX
            bg_col = CALLOUT_BG
            t_col = INDIGO_RGB

        borders = {'left': {'val': 'single', 'sz': 24, 'color': b_col}}
        style_cell(cell, fill_hex=bg_col, borders=borders, pad_tb=120, pad_lr=160)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        rt = p.add_run(title)
        rt.font.name = "Calibri"
        rt.font.size = Pt(10)
        rt.font.bold = True
        rt.font.color.rgb = t_col
        
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(0)
        rc = p2.add_run(text)
        rc.font.name = "Calibri"
        rc.font.size = Pt(9.5)
        rc.font.color.rgb = DARK_RGB
        
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ COVER HEADER ------------------
    cover_tbl = doc.add_table(rows=1, cols=1)
    cover_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cover_tbl.autofit = False
    cover_tbl.columns[0].width = Inches(7.0)
    c_cell = cover_tbl.cell(0, 0)
    style_cell(c_cell, fill_hex=INDIGO_HEX, borders={}, pad_tb=300, pad_lr=240)
    
    cp1 = c_cell.paragraphs[0]
    cp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp1.paragraph_format.space_before = Pt(0)
    cp1.paragraph_format.space_after = Pt(4)
    rt = cp1.add_run("FRENCH LINGUISTIC DIAGNOSTIC & STRESS-TEST WORKBOOK")
    rt.font.name = "Calibri"
    rt.font.size = Pt(20)
    rt.font.bold = True
    rt.font.color.rgb = RGBColor(255, 255, 255)
    
    cp2 = c_cell.add_paragraph()
    cp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp2.paragraph_format.space_before = Pt(2)
    cp2.paragraph_format.space_after = Pt(6)
    rs = cp2.add_run("A Brutally Thorough Examination of French Foundations, Phonetics, Pragmatics & Fossilized Errors")
    rs.font.name = "Calibri"
    rs.font.size = Pt(11)
    rs.font.italic = True
    rs.font.color.rgb = RGBColor(226, 232, 240)

    cp3 = c_cell.add_paragraph()
    cp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp3.paragraph_format.space_before = Pt(4)
    cp3.paragraph_format.space_after = Pt(0)
    rm = cp3.add_run("Undergraduate French Linguistics & Advanced Foundations Division  •  Zero Tolerance for False Friends")
    rm.font.name = "Calibri"
    rm.font.size = Pt(9)
    rm.font.color.rgb = RGBColor(148, 163, 184)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_callout(
        "INSTRUCTIONAL PREAMBLE: THE STRESS-TEST PROTOCOL",
        "This workbook is intentionally unaccommodating. It is engineered to aggressively stress-test beginner-to-intermediate "
        "learners to expose fossilized misconceptions, acoustic blind spots, false friends, and register violations. "
        "Every section requires active cognitive production: classifying sociopragmatic registers, reducing compound subjects, "
        "distinguishing subtle homophones, classifying 30 final consonants under phonetic rules, and correcting deceptive prose. "
        "Do not consult reference grammars while completing this diagnostic. Check your work against Section 5 only upon completion.",
        "danger"
    )

    # -------------------------------------------------------------
    # SECTION 1: FOUNDATIONAL MECHANICS
    # -------------------------------------------------------------
    add_h1("SECTION 1: FOUNDATIONAL MECHANICS (Rapid Identification & Conjugation Drills)")
    
    add_h2("1.1 Complete Rapid-Fire Paradigm Grid: Isolation & Mixed Contexts")
    add_p("Supply the exact present-indicative form of ÊTRE or AVOIR, strictly applying mandatory elision where appropriate.")

    table_1_1 = [
        ("1. (Je + avoir)", "____________________", "7. (Je + être)", "____________________"),
        ("2. (Tu + être)", "____________________", "8. (Tu + avoir)", "____________________"),
        ("3. (Il/Elle/On + avoir)", "____________________", "9. (Il/Elle/On + être)", "____________________"),
        ("4. (Nous + être)", "____________________", "10. (Nous + avoir)", "____________________"),
        ("5. (Vous + avoir)", "____________________", "11. (Vous + être)", "____________________"),
        ("6. (Ils/Elles + être)", "____________________", "12. (Ils/Elles + avoir)", "____________________")
    ]
    t1 = doc.add_table(rows=1, cols=4)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t1.columns[0].width = Inches(2.0)
    t1.columns[1].width = Inches(1.5)
    t1.columns[2].width = Inches(2.0)
    t1.columns[3].width = Inches(1.5)
    
    # Header
    hdr = t1.rows[0].cells
    hdr[0].paragraphs[0].add_run("Prompt A").bold = True
    hdr[1].paragraphs[0].add_run("Answer A").bold = True
    hdr[2].paragraphs[0].add_run("Prompt B").bold = True
    hdr[3].paragraphs[0].add_run("Answer B").bold = True
    for c in hdr:
        style_cell(c, fill_hex=INDIGO_HEX, borders={}, pad_tb=80, pad_lr=100)
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        c.paragraphs[0].runs[0].font.name = "Calibri"
        c.paragraphs[0].runs[0].font.size = Pt(9.5)

    for row_data in table_1_1:
        row = t1.add_row().cells
        for idx, val in enumerate(row_data):
            row[idx].paragraphs[0].add_run(val)
            row[idx].paragraphs[0].runs[0].font.name = "Calibri"
            row[idx].paragraphs[0].runs[0].font.size = Pt(9)
            style_cell(row[idx], fill_hex=LIGHT_BG if idx%2==1 else None, pad_tb=60, pad_lr=80)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_h2("1.2 Subject Pronoun Reduction & Compound Subjects (15 Drill Items)")
    add_p("Reduce the following complex, compound, or collective noun phrases into their exact grammatical subject pronoun (je, tu, il, elle, on, nous, vous, ils, elles).")

    pronoun_reductions = [
        ("1. « Marie et toi »", "-> Grammatical Subject Pronoun: ____________________"),
        ("2. « L'équipe et moi »", "-> Grammatical Subject Pronoun: ____________________"),
        ("3. « Le chien et la chatte »", "-> Grammatical Subject Pronoun: ____________________"),
        ("4. « Mes deux sœurs et leur amie »", "-> Grammatical Subject Pronoun: ____________________"),
        ("5. « Toi et lui »", "-> Grammatical Subject Pronoun: ____________________"),
        ("6. « Ni Paul ni moi »", "-> Grammatical Subject Pronoun: ____________________"),
        ("7. « Tout le monde »", "-> Grammatical Subject Pronoun: ____________________"),
        ("8. « La majorité des étudiants » (formal verb agreement)", "-> Grammatical Subject Pronoun: ____________________"),
        ("9. « Cet homme et ses enfants »", "-> Grammatical Subject Pronoun: ____________________"),
        ("10. « Le professeur et vous »", "-> Grammatical Subject Pronoun: ____________________"),
        ("11. « Toi et tes collègues »", "-> Grammatical Subject Pronoun: ____________________"),
        ("12. « Ma mère et mon père »", "-> Grammatical Subject Pronoun: ____________________"),
        ("13. « Les directrices et leurs associés masculins »", "-> Grammatical Subject Pronoun: ____________________"),
        ("14. « L'ensemble de la classe »", "-> Grammatical Subject Pronoun: ____________________"),
        ("15. « Ni toi ni elle »", "-> Grammatical Subject Pronoun: ____________________")
    ]
    for prompt, blank in pronoun_reductions:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{prompt}  ")
        r1.bold = True
        r1.font.size = Pt(9.5)
        r2 = p.add_run(blank)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = MUTED_RGB

    add_h2("1.3 Elision Triggers & Structural Constraints (8 Precision Items)")
    add_p("Determine whether mandatory elision occurs. Write the contracted or full form and specify the exact rule constraint.")

    elision_drills = [
        ("1. (je + espérer)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("2. (je + être)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("3. (tu + aimer) [spoken vs written standard]", "Result: ____________________  | Constraint: _____________________________________________"),
        ("4. (que + il)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("5. (qui + il)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("6. (si + il)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("7. (si + elle)", "Result: ____________________  | Constraint: _____________________________________________"),
        ("8. (ce + être)", "Result: ____________________  | Constraint: _____________________________________________")
    ]
    for item, bl in elision_drills:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{item}  ")
        r1.bold = True
        r1.font.size = Pt(9.5)
        r2 = p.add_run(bl)
        r2.font.size = Pt(9.5)
        r2.font.color.rgb = MUTED_RGB

    # -------------------------------------------------------------
    # SECTION 2: PRAGMATIC & SEMANTIC STRESS-TESTS
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("SECTION 2: PRAGMATIC & SEMANTIC STRESS-TESTS (Zero Tolerance for False Friends)")

    add_h2("2.1 The Tu vs. Vous Pragmatic Decision Matrix (10 Real-World Scenarios)")
    add_p("For each scenario, select the sociolinguistically required address pronoun and state the precise pragmatic rationale.")

    tu_vous_matrix = [
        ("1. You are meeting your prospective French mother-in-law (belle-mère) for Sunday lunch at her home.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("2. A gendarme flags your car down on a rural road for a routine driver's license inspection.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("3. An adult stranger in the Châtelet metro station stops you to ask what time it is.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("4. You are addressing two siblings (ages 6 and 9) playing on the sidewalk outside your building.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("5. You are speaking to a fellow 20-year-old student sitting beside you on your first day of class at Paris-Sorbonne.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("6. You are meeting your corporate division director (Directeur Général) during your quarterly review.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("7. An independent artisan plumber arrives at your apartment to repair a leaking radiator.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("8. You are speaking to an unknown dog sitting quietly on a café terrace.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("9. You join a table of four close childhood friends who have known each other since primary school.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________"),
        ("10. You are conducting an exploratory discovery Zoom call with a high-value prospective business client.",
         "[  ] Tu       [  ] Vous (Singulier formel)       [  ] Vous (Pluriel collectif)",
         "Pragmatic Rationale: __________________________________________________________________________________")
    ]
    for s_title, opts, rat in tu_vous_matrix:
        add_p(s_title, bold=True, space_before=3, space_after=1)
        add_p(opts, space_before=0, space_after=1)
        add_p(rat, color=MUTED_RGB, space_before=0, space_after=3)

    add_h2("2.2 The Être vs. Avoir Semantic Gauntlet (25 High-Stakes Sentences)")
    add_p("Supply the conjugated present-indicative form of ÊTRE or AVOIR. Identify the exact semantic trigger or false-friend collision.")

    gauntlet_25 = [
        "1. Malgré le chauffage éteint, les enfants n'______________ pas froid dans leur chambre.",
        "2. Mon grand-père fêtera bientôt son centenaire : il ______________ 99 ans aujourd'hui.",
        "3. Après une journée de jeûne médical, nous ______________ une faim insoutenable.",
        "4. Tu as vérifié les données du tableur ? Je crains que tu ______________ tort sur ce point.",
        "5. Il est trois heures du matin ; mes paupières sont lourdes, j'______________ sommeil.",
        "6. Pourquoi fermes-tu les volets ? Est-ce que tu ______________ peur des éclairs ?",
        "7. Les passagers bloqués sur le quai ______________ très en colère contre la SNCF.",
        "8. Ne touchez pas cette plaque de cuisson ! Elle ______________ brûlante (state).",
        "9. Attention au piège : « Elle ______________ chaude » vs « Elle ______________ chaud » (expliquez le sens).",
        "10. Est-ce que vous ______________ d'accord avec les termes de ce contrat bilatéral ?",
        "11. Les étudiants ______________ besoin de consulter les archives avant de rédiger leur thèse.",
        "12. Le patient tremble sous sa couverture : il ______________ 40 de fièvre.",
        "13. Vous ______________ en retard de quinze minutes pour l'entretien d'embauche.",
        "14. Elle n'ose pas prendre la parole en public car elle ______________ honte de son accent.",
        "15. Nous ______________ très fiers des résultats académiques de nos élèves.",
        "16. Ce matin, je me sens faible : je pense que je ______________ malade (condition).",
        "17. Après avoir couru un marathon sous la canicule, vous ______________ une soif dévorante.",
        "18. Le témoin affirme que le suspect ______________ l'air suspect et agité.",
        "19. Nous n'______________ pas l'habitude de dîner avant vingt et une heures en Espagne.",
        "20. Malgré leurs excuses répétées, ils ______________ entièrement responsables de l'accident.",
        "21. Pourquoi cries-tu ? Est-ce que tu ______________ mal à la tête ou à la gorge ?",
        "22. Qui ______________ raison dans ce débat juridique, le procureur ou la défense ?",
        "23. Ce soir, on ______________ envie de déguster des fruits de mer sur le port.",
        "24. Les touristes ______________ perdus dans les ruelles médiévales de la vieille ville.",
        "25. Je ne peux pas travailler ce soir : je ______________ épuisé par ma garde à l'hôpital."
    ]
    for sent in gauntlet_25:
        add_p(sent, space_before=2, space_after=2)

    add_h2("2.3 \"Il y a\" Multi-Step Syntactic Transformations (8 Drills)")
    add_p("Transform each affirmative statement into: (a) Interrogative with formal inversion (Y a-t-il...), and (b) Strict negative with mandatory indefinite/partitive article reduction into DE/D'.")

    transformations_8 = [
        ("1. Affirmative: « Il y a un problème technique avec le serveur central. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("2. Affirmative: « Il y a une pharmacie ouverte le dimanche dans ce quartier. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("3. Affirmative: « Il y a des erreurs de calcul dans le rapport financier. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("4. Affirmative: « Il y a un ascenseur fonctionnel dans cet immeuble haussmannien. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("5. Affirmative: « Il y a de l'eau potable disponible dans le refuge de montagne. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("6. Affirmative: « Il y a des places assises réservées pour les personnes âgées. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("7. Affirmative: « Il y a une issue de secours à l'arrière de la salle de conférence. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________"),
        ("8. Affirmative: « Il y a des documents confidentiels sur le bureau du directeur. »",
         "a) Interrogative (Inversion): _____________________________________________________________________\n"
         "b) Strict Negative:           _____________________________________________________________________")
    ]
    for aff, resp in transformations_8:
        add_p(aff, bold=True, space_before=3, space_after=1)
        add_p(resp, color=MUTED_RGB, space_before=0, space_after=3)

    # -------------------------------------------------------------
    # SECTION 3: THE PHONETIC GAUNTLET
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("SECTION 3: THE PHONETIC GAUNTLET (Pronunciation & Decoding)")

    add_h2("3.1 Silent vs. Sounded Final Consonants: 30-Word Forensic Classification")
    add_p("Examine the final letter(s) of each word in isolation. Classify as [SILENT] or [PRONOUNCED] and supply the exact IPA transcription.")

    words_30 = [
        ("1. blanc (c)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("2. est (st)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("3. lit (t)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("4. lits (ts)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("5. clef (f)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("6. hiver (r)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("7. tabac (c)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("8. nid (d)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("9. fils [son] (ls)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("10. fils [threads] (s)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("11. six [alone] (x)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("12. sept (pt)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("13. huit [alone] (t)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("14. porc (rc)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("15. mer (r)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("16. net (t)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("17. chef (f)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("18. pied (d)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("19. fusil (l)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("20. corps (rps)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("21. sirop (p)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("22. coup (p)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("23. plat (t)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("24. nez (z)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("25. dix [alone] (x)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("26. gaz (z)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("27. sac (c)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("28. drap (p)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("29. sang (g)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/"),
        ("30. respect (ct)", "[ ] SILENT  [ ] PRONOUNCED", "IPA: /_________/")
    ]

    t30 = doc.add_table(rows=1, cols=3)
    t30.alignment = WD_TABLE_ALIGNMENT.CENTER
    t30.columns[0].width = Inches(2.2)
    t30.columns[1].width = Inches(2.6)
    t30.columns[2].width = Inches(2.2)
    
    h30 = t30.rows[0].cells
    h30[0].paragraphs[0].add_run("Target Word (Final Letter)").bold = True
    h30[1].paragraphs[0].add_run("Classification").bold = True
    h30[2].paragraphs[0].add_run("Phonetic Transcription").bold = True
    for c in h30:
        style_cell(c, fill_hex=INDIGO_HEX, borders={}, pad_tb=70, pad_lr=90)
        c.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)
        c.paragraphs[0].runs[0].font.name = "Calibri"
        c.paragraphs[0].runs[0].font.size = Pt(9)

    for w, cl, ipa in words_30:
        row = t30.add_row().cells
        row[0].paragraphs[0].add_run(w).font.name = "Calibri"
        row[1].paragraphs[0].add_run(cl).font.name = "Calibri"
        row[2].paragraphs[0].add_run(ipa).font.name = "Calibri"
        row[0].paragraphs[0].runs[0].font.size = Pt(8.5)
        row[1].paragraphs[0].runs[0].font.size = Pt(8.5)
        row[2].paragraphs[0].runs[0].font.size = Pt(8.5)
        for c in row:
            style_cell(c, pad_tb=40, pad_lr=70)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_h2("3.2 Acoustic Discrimination & Minimal Pairs (8 Precision Pairs)")
    add_p("Analyze each minimal pair. Provide the distinct IPA phonetic transcription and identify the acoustic features that prevent native misunderstanding.")

    minimal_pairs = [
        ("1. « ils ont » vs. « ils sont »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("2. « dessus » vs. « dessous »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("3. « vin » vs. « vent »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("4. « un » vs. « une »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("5. « bon » vs. « bonne »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("6. « plein » vs. « pleine »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("7. « beau » vs. « bon »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________"),
        ("8. « poisson » vs. « poison »",
         "IPA 1: /____________________/  | IPA 2: /____________________/\n"
         "Acoustic distinction: __________________________________________________________________________")
    ]
    for mp, detail in minimal_pairs:
        add_p(mp, bold=True, space_before=2, space_after=1)
        add_p(detail, color=MUTED_RGB, space_before=0, space_after=3)

    add_h2("3.3 The Liaison Traffic Light: Mandatory, Optional, or Forbidden (10 Sentences)")
    add_p("Examine the marked junction [ _|_ ]. Classify the liaison as [MANDATORY], [OPTIONAL], or [FORBIDDEN]. State the linking phoneme if pronounced, or the phonetic boundary blocking liaison.")

    liaison_10 = [
        ("1. « Les [ _|_ ] amis de ma sœur arrivent ce soir. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("2. « Paul et [ _|_ ] un collègue préparent le dossier. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("3. « Cet étudiant [ _|_ ] intelligent a réussi le concours. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("4. « Nous admirons les [ _|_ ] héros de la Résistance. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("5. « Elles sont [ _|_ ] arrivées vers [ _|_ ] onze heures. » (Junction 2: vers/onze)",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("6. « C'est un homme très [ _|_ ] aimable et courtois. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("7. « Ils ont acheté des livres [ _|_ ] intéressants. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("8. « Ils sont [ _|_ ] amis depuis l'enfance. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("9. « Ont [ _|_ ] ils terminé leurs devoirs ? »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________"),
        ("10. « Un soldat [ _|_ ] anglais monte la garde. »",
         "Classification: [  ] MANDATORY   [  ] OPTIONAL   [  ] FORBIDDEN  | Phoneme/Boundary: __________________")
    ]
    for s_sent, bl in liaison_10:
        add_p(s_sent, bold=True, space_before=2, space_after=1)
        add_p(bl, color=MUTED_RGB, space_before=0, space_after=3)

    add_h2("3.4 Accent Shift Mechanics: 8 Contrastive Minimal Pairs")
    add_p("Explain the precise grammatical or phonetic difference produced by adding, altering, or omitting the diacritic.")

    accent_shifts = [
        ("1. « a » vs. « à »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("2. « ou » vs. « où »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("3. « sur » vs. « sûr »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("4. « manger » vs. « mangé »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("5. « du » vs. « dû »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("6. « des » vs. « dès »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("7. « la » vs. « là »", "Linguistic / Grammatical shift: _________________________________________________________"),
        ("8. « peche » vs. « pêche »", "Linguistic / Grammatical shift: _________________________________________________________")
    ]
    for p_pair, bl in accent_shifts:
        add_p(p_pair, bold=True, space_before=2, space_after=1)
        add_p(bl, color=MUTED_RGB, space_before=0, space_after=3)

    # -------------------------------------------------------------
    # SECTION 4: BRUTAL ERROR-HUNTING
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("SECTION 4: BRUTAL ERROR-HUNTING & PARAGRAPH CORRECTION")
    add_p("The following 3 paragraphs contain deceptive, insidious errors: false auxiliary verbs, unreduced negative articles, illegal liaisons, incorrect pronoun reductions, agreement errors, and missed elisions. "
          "Locate each error, categorize its linguistic failure mode, and write the complete, immaculate French correction.")

    paragraphs_3 = [
        ("Paragraph 1: Une journée ordinaire au bureau",
         "« Bonjour monsieur le Directeur. Est-ce que tu as cinq minutes ? Marie et moi, on parlent du budget annuel. "
         "Dans notre service, il n'y a pas des ordinateurs portables disponibles et les stagiaires sont 21 ans. "
         "Ils sont très faim à midi parce que il n'y a pas un restaurant d'entreprise dans l'immeuble. "
         "Mon collègue et [liaison prononcée] un client attendent votre réponse depuis ce matin. »",
         "Target Errors to Locate: 7 distinct violations (Register, Agreement with 'on', Negative article collapse, Age auxiliary, Sensation auxiliary, Missed elision, Forbidden liaison after 'et').\n\n"
         "Your Corrected Text:\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________"),

        ("Paragraph 2: Une visite médicale compliquée",
         "« Bonjour docteur. Je suis 35 ans et depuis hier soir, je suis très chaud et j'ai froid en même temps. "
         "Mes deux enfants ont aussi malade ; ils sont peur du thermomètre et ils parlent [prononcé avec son nasal -ɑ̃] sans cesse. "
         "Est-ce que il y a des médicaments sans ordonnance ? Non, dans cette pharmacie il n'y a pas des antibiotiques libres. "
         "Paul et toi, vous avez très fatigués par cette épidémie saisonnière. »",
         "Target Errors to Locate: 7 distinct violations (Age auxiliary, Somatic sensation false friend, State auxiliary with 'malade', Sensation auxiliary with 'peur', Verbal plural '-ent' phonetics, Elision before vowel, Negative article collapse, Auxiliary with 'fatigués').\n\n"
         "Your Corrected Text:\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________"),

        ("Paragraph 3: Le départ mouvementé en vacances",
         "« Toi et moi, nous partent en vacances demain à l'aube. Dans notre valise, il n'y a pas des maillots de bain. "
         "Nous admirons les [liaison en [z]] héros du roman que nous lisons. Sur la table, il y a du vin rouge mais il n'y a pas du pain. "
         "Pierre et lui sont faim mais ils ont [prononcé avec [s]] très calmes. Est-ce que sur la plage il y a des transats libres ? "
         "Non, à cette saison, il n'y a pas des transats disponibles nulle part. »",
         "Target Errors to Locate: 7 distinct violations (Verb agreement with compound 'nous', Negative article reduction, Forbidden liaison before 'héros' [h aspiré], Negative partitive reduction, Auxiliary with 'faim', Acoustic inversion of ont/sont, Negative article reduction).\n\n"
         "Your Corrected Text:\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________\n"
         "____________________________________________________________________________________________________")
    ]

    for p_title, p_flawed, p_work in paragraphs_3:
        add_p(p_title, bold=True, color=BURGUNDY_RGB, size=11, space_before=4, space_after=2)
        add_p(p_flawed, italic=True, space_before=0, space_after=3)
        add_p(p_work, color=MUTED_RGB, space_before=0, space_after=6)

    # -------------------------------------------------------------
    # SECTION 5: UNCOMPROMISING ANSWER KEY
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("SECTION 5: UNCOMPROMISING ANSWER KEY & TECHNICAL EXPLANATIONS")
    add_callout(
        "DIAGNOSTIC PROTOCOL: ZERO PERFORMANCE AGREEMENT",
        "This answer key contains unabbreviated solutions, exact IPA phonetic representations, and technical explanations. "
        "Review every single mistake through the linguistic notes to dismantle fossilized habits.",
        "alert"
    )

    add_h2("Section 1 Solutions: Foundational Mechanics")
    add_p("1.1 Conjugation Grid:\n"
          "1. J'ai (mandatory elision)  |  7. Je suis (no elision)\n"
          "2. Tu es  |  8. Tu as\n"
          "3. Il/Elle/On a  |  9. Il/Elle/On est\n"
          "4. Nous sommes  |  10. Nous avons\n"
          "5. Vous avez  |  11. Vous êtes\n"
          "6. Ils/Elles sont  |  12. Ils/Elles ont (Note phonetics: [il-sõ] vs. [il-z‿õ])")

    add_p("1.2 Subject Pronoun Reduction:\n"
          "1. « Marie et toi » -> VOUS (2nd person plural: any group including 'toi' without 'moi').\n"
          "2. « L'équipe et moi » -> NOUS (1st person plural: 1st person takes priority over 3rd person).\n"
          "3. « Le chien et la chatte » -> ILS (Grammatical rule of masculine gender priority in mixed groups).\n"
          "4. « Mes deux sœurs et leur amie » -> ELLES (All subjects are feminine animate nouns).\n"
          "5. « Toi et lui » -> VOUS (2nd person takes precedence over 3rd person).\n"
          "6. « Ni Paul ni moi » -> NOUS (Compound negative including speaker).\n"
          "7. « Tout le monde » -> IL (Syntactically grammatically 3rd person singular, despite plural semantic meaning).\n"
          "8. « La majorité des étudiants » -> ELLE (Formal syntactic agreement with singular head noun 'la majorité').\n"
          "9. « Cet homme et ses enfants » -> ILS (Masculine plural).\n"
          "10. « Le professeur et vous » -> VOUS (2nd person plural).\n"
          "11. « Toi et tes collègues » -> VOUS.\n"
          "12. « Ma mère et mon père » -> ILS (Mixed gender plural defaults to grammatical masculine).\n"
          "13. « Les directrices et leurs associés masculins » -> ILS (Presence of even one masculine entity forces masculine plural).\n"
          "14. « L'ensemble de la classe » -> IL (Head noun 'ensemble' is masculine singular).\n"
          "15. « Ni toi ni elle » -> VOUS (2nd person takes precedence).")

    add_p("1.3 Elision Triggers:\n"
          "1. J'espère — Mandatory elision of 'je' before vowel.\n"
          "2. Je suis — Elision FORBIDDEN (verb begins with consonant /s/; *j'suis is non-standard vernacular).\n"
          "3. Tu aimes — Elision FORBIDDEN in standard written French (*t'aimes is informal oral elision only).\n"
          "4. Qu'il — Mandatory elision of conjunction/relative 'que' before vowel.\n"
          "5. Qui il (qui est-ce...) — Elision FORBIDDEN. The relative pronoun 'qui' NEVER elides (*qu'il arrive = que + il, never qui + il).\n"
          "6. S'il — Mandatory elision of 'si' before masculine pronouns 'il' and 'ils'.\n"
          "7. Si elle — Elision FORBIDDEN. 'Si' NEVER elides before 'elle', 'elles', or other words (*s'elle is ungrammatical).\n"
          "8. C'est — Mandatory elision of demonstrative 'ce' before vowel form of être.")

    add_h2("Section 2 Solutions: Pragmatic & Semantic Stress-Tests")
    add_p("2.1 Pragmatic Decision Matrix:\n"
          "1. VOUS (Singulier formel) — In-law introductions require formal deference until explicit permission to tutoyer is granted.\n"
          "2. VOUS (Singulier formel) — Law enforcement agents require mandatory 'vous'. Using 'tu' is legally punishable as 'outrage à agent'.\n"
          "3. VOUS (Singulier formel) — Adult strangers in public spaces strictly require 'vous' to establish baseline civil respect.\n"
          "4. VOUS (Pluriel collectif) — Plural address. Even though individual children are tutoyés, a group of 2+ individuals ALWAYS takes 'vous'.\n"
          "5. TU — Horizontal peer solidarity among university students in modern France.\n"
          "6. VOUS (Singulier formel) — Vertical hierarchy in corporate environments.\n"
          "7. VOUS (Singulier formel) — Professional commercial interaction with an independent contractor.\n"
          "8. TU — Animals and pets are universally tutoyés.\n"
          "9. VOUS (Pluriel collectif) — Plural collective. French has no plural 'tu'. Any group is addressed with 'vous'.\n"
          "10. VOUS (Singulier formel) — Professional business development call.")

    add_p("2.2 The Être vs. Avoir Semantic Gauntlet (1–25):\n"
          "1. n'ont pas (avoir froid) | 2. a (avoir X ans) | 3. avons (avoir faim) | 4. as (avoir tort)\n"
          "5. ai (avoir sommeil) | 6. as (avoir peur) | 7. sont (être en colère) | 8. est (être brûlante)\n"
          "9. Explication : « Elle a chaud » = elle ressent de la chaleur physique. « Elle est chaude » = expression familière signifiant qu'elle est sexuellement excitée ou prête à faire la fête (piège de registre grossier).\n"
          "10. êtes (être d'accord) | 11. ont (avoir besoin de) | 12. a (avoir de la fièvre) | 13. êtes (être en retard)\n"
          "14. a (avoir honte) | 15. sommes (être fier) | 16. suis (être malade) | 17. avez (avoir soif)\n"
          "18. a (avoir l'air) | 19. avons (avoir l'habitude de) | 20. sont (être responsable) | 21. as (avoir mal à)\n"
          "22. a (avoir raison) | 23. a (avoir envie de) | 24. sont (être perdu) | 25. suis (être épuisé).")

    add_p("2.3 \"Il y a\" Syntactic Transformations:\n"
          "1. a) Y a-t-il un problème technique avec le serveur central ?  |  b) Il n'y a pas de problème technique avec le serveur central.\n"
          "2. a) Y a-t-il une pharmacie ouverte le dimanche dans ce quartier ?  |  b) Il n'y a pas de pharmacie ouverte le dimanche dans ce quartier.\n"
          "3. a) Y a-t-il des erreurs de calcul dans le rapport financier ?  |  b) Il n'y a pas d'erreur(s) de calcul dans le rapport financier.\n"
          "4. a) Y a-t-il un ascenseur fonctionnel dans cet immeuble haussmannien ?  |  b) Il n'y a pas d'ascenseur fonctionnel dans cet immeuble haussmannien.\n"
          "5. a) Y a-t-il de l'eau potable disponible dans le refuge de montagne ?  |  b) Il n'y a pas d'eau potable disponible dans le refuge de montagne.\n"
          "6. a) Y a-t-il des places assises réservées pour les personnes âgées ?  |  b) Il n'y a pas de places assises réservées pour les personnes âgées.\n"
          "7. a) Y a-t-il une issue de secours à l'arrière de la salle ?  |  b) Il n'y a pas d'issue de secours à l'arrière de la salle.\n"
          "8. a) Y a-t-il des documents confidentiels sur le bureau du directeur ?  |  b) Il n'y a pas de documents confidentiels sur le bureau du directeur.")

    add_callout(
        "TECHNICAL LINGUISTIC NOTE: THE ARTICLE COLLAPSE RULE",
        "Why *« Il n'y a pas des problèmes »* is strictly ungrammatical: The indefinite determiners ('un', 'une', 'des') and partitives ('du', 'de la') quantify non-zero entities. Under the direct scope of sentential negation ('ne... pas'), the quantity collapses to absolute zero. In standard French syntax, absolute zero quantification takes the bare prepositional marker 'de' (or 'd\'' before a vowel). Retaining 'des' under negation is only permitted when 'pas' negates a specific noun in opposition: « Je ne veux pas des pommes, je veux des poires ».",
        "alert"
    )

    add_h2("Section 3 Solutions: The Phonetic Gauntlet")
    add_p("3.1 30-Word Forensic Classification:\n"
          "1. blanc : SILENT (c) -> /blɑ̃/\n"
          "2. est : SILENT (st) -> /ɛ/\n"
          "3. lit : SILENT (t) -> /li/\n"
          "4. lits : SILENT (ts) -> /li/\n"
          "5. clef : SILENT (f) in traditional spelling -> /kle/ (sometimes pronounced in modern 'clé')\n"
          "6. hiver : PRONOUNCED (r) -> /i.vɛʁ/ (CaReFuL rule: final r pronounced after e in polysyllabic words, unlike -er verbs)\n"
          "7. tabac : SILENT (c) -> /ta.ba/ (Exception to CaReFuL)\n"
          "8. nid : SILENT (d) -> /ni/\n"
          "9. fils [son] : PRONOUNCED (s), SILENT (l) -> /fis/\n"
          "10. fils [threads] : SILENT (s), PRONOUNCED (l) -> /fil/\n"
          "11. six [alone] : PRONOUNCED (x as [s]) -> /sis/ (Becomes silent before consonant: 'six chats' [si ʃa]; liaison [z] before vowel: 'six ans' [si.z‿ɑ̃])\n"
          "12. sept : PRONOUNCED (t), SILENT (p) -> /sɛt/\n"
          "13. huit [alone] : PRONOUNCED (t) -> /ɥit/\n"
          "14. porc : SILENT (rc) -> /pɔʁ/\n"
          "15. mer : PRONOUNCED (r) -> /mɛʁ/ (CaReFuL)\n"
          "16. net : PRONOUNCED (t) -> /nɛt/ (Exception: final t sounded)\n"
          "17. chef : PRONOUNCED (f) -> /ʃɛf/ (CaReFuL)\n"
          "18. pied : SILENT (d) -> /pje/\n"
          "19. fusil : SILENT (l) -> /fy.zi/ (Exception to CaReFuL)\n"
          "20. corps : SILENT (rps) -> /kɔʁ/\n"
          "21. sirop : SILENT (p) -> /si.ʁo/\n"
          "22. coup : SILENT (p) -> /ku/\n"
          "23. plat : SILENT (t) -> /pla/\n"
          "24. nez : SILENT (z) -> /ne/\n"
          "25. dix [alone] : PRONOUNCED (x as [s]) -> /dis/\n"
          "26. gaz : PRONOUNCED (z) -> /ɡaz/\n"
          "27. sac : PRONOUNCED (c) -> /sak/ (CaReFuL)\n"
          "28. drap : SILENT (p) -> /dʁa/\n"
          "29. sang : SILENT (g) -> /sɑ̃/\n"
          "30. respect : SILENT (ct) -> /ʁɛs.pɛ/")

    add_p("3.2 Minimal Pairs IPA & Acoustic Distinctions:\n"
          "1. ils ont /il.z‿õ/ vs. ils sont /il.sõ/ — Acoustic feature: Voiced alveolar fricative [z] from liaison indicates AVOIR; voiceless alveolar fricative [s] indicates ÊTRE.\n"
          "2. dessus /də.sy/ vs. dessous /də.su/ — Acoustic feature: High front rounded vowel [y] vs. high back rounded vowel [u]. Minimal lip and tongue position shift.\n"
          "3. vin /vɛ̃/ vs. vent /vɑ̃/ — Acoustic feature: Open-mid front unrounded nasal vowel [ɛ̃] vs. open back rounded nasal vowel [ɑ̃].\n"
          "4. un /œ̃/ vs. une /yn/ — Acoustic feature: Open-mid front rounded nasal vowel [œ̃] vs. oral front rounded vowel + alveolar nasal consonant [yn].\n"
          "5. bon /bɔ̃/ vs. bonne /bɔn/ — Acoustic feature: Pure nasal vowel [bɔ̃] vs. denasalized open-mid back oral vowel followed by sounded nasal consonant [bɔn].\n"
          "6. plein /plɛ̃/ vs. pleine /plɛn/ — Acoustic feature: Nasal [ɛ̃] vs. oral [ɛ] + sounded [n].\n"
          "7. beau /bo/ vs. bon /bɔ̃/ — Acoustic feature: Oral back close-mid vowel [o] vs. open-mid back nasal vowel [ɔ̃].\n"
          "8. poisson /pwa.sõ/ vs. poison /pwa.zõ/ — Acoustic feature: Voiceless [s] (spelled ss) vs. voiced [z] (intervocalic single s).")

    add_p("3.3 Liaison Traffic Light:\n"
          "1. MANDATORY — Determiner + Noun (« les_amis ») -> Phoneme [z].\n"
          "2. FORBIDDEN — Conjunction 'et' (« et // un »). Strictly forbidden glottal pause.\n"
          "3. FORBIDDEN — Singular noun + Adjective (« étudiant // intelligent »). In standard modern French, liaison is forbidden after a singular noun subject/head.\n"
          "4. FORBIDDEN — 'H aspiré' (« les // héros »). Germanic etymology prevents both elision and liaison.\n"
          "5. FORBIDDEN — Before numeral 'onze' (« vers // onze heures »). Treated as consonant boundary.\n"
          "6. MANDATORY — Monosyllabic adverb + Adjective (« très_aimable ») -> Phoneme [z].\n"
          "7. OPTIONAL — Plural noun + Adjective (« livres_intéressants »). Pronounced [z] in elevated speech; omitted in everyday speech.\n"
          "8. OPTIONAL — Verb être 3rd plural + Predicate (« sont_amis »). Pronounced [t] in careful speech; frequently dropped in informal register.\n"
          "9. MANDATORY — Inverted subject pronoun (« ont-ils ») -> Phoneme [t].\n"
          "10. FORBIDDEN — Singular noun + Adjective (« soldat // anglais »).")

    add_callout(
        "TECHNICAL LINGUISTIC NOTE: 'H ASPIRÉ' VS. 'H MUET'",
        "Why *« les‿héros »* is a fatal error: French has two distinct categories of word-initial 'h'. (1) 'H muet' (Latin origin: l'homme, les‿hommes) triggers mandatory elision and liaison. (2) 'H aspiré' (Frankish / Germanic origin: le héros, les // héros, la haine) historical phonology retained a Germanic glottal fricative [h]. Although the sound itself has vanished from modern pronunciation, it continues to function as an invisible consonant boundary, strictly prohibiting both elision (*l'héros is impossible) and liaison (*les-z-héros is ungrammatical; note that 'les héroïnes' uses 'h muet'!).",
        "alert"
    )

    add_p("3.4 Accent Shifts:\n"
          "1. « a » (verb avoir, 3rd sing) vs. « à » (preposition of location/direction).\n"
          "2. « ou » (coordinating conjunction 'or') vs. « où » (locative/temporal relative adverb 'where/when').\n"
          "3. « sur » (preposition 'on/upon') vs. « sûr » (adjective 'certain/safe').\n"
          "4. « manger » (infinitive verb [mɑ̃.ʒe]) vs. « mangé » (past participle [mɑ̃.ʒe]; identical in sound but distinct syntax).\n"
          "5. « du » (contracted article de+le or partitive) vs. « dû » (past participle of irregular verb devoir).\n"
          "6. « des » (indefinite plural article) vs. « dès » (temporal preposition 'as soon as / starting from').\n"
          "7. « la » (definite feminine article/pronoun) vs. « là » (locative adverb 'there').\n"
          "8. « peche » (orthographically invalid in modern French) vs. « pêche » (noun 'peach' or 'fishing', or 1st/3rd sing verb pêcher).")

    add_h2("Section 4 Solutions: Brutal Error-Hunting & Paragraph Correction")
    add_p("Paragraph 1 Correction (7 Errors Resolved):\n"
          "« Bonjour Monsieur le Directeur. Est-ce que VOUS AVEZ cinq minutes ? Marie et moi, ON PARLE du budget annuel. "
          "Dans notre service, il n'y a pas D'ordinateurs portables disponibles et les stagiaires ONT 21 ans. "
          "Ils ONT très faim à midi parce QU'IL n'y a pas DE restaurant d'entreprise dans l'immeuble. "
          "Mon collègue et [pas de liaison] un client attendent votre réponse depuis ce matin. »\n"
          "Linguistic Notes: (1) Tu -> Vous (professional hierarchy). (2) on parlent -> on parle (on takes 3rd sing). (3) pas des ordinateurs -> pas d'ordinateurs (negation collapse). (4) sont 21 ans -> ont 21 ans (age requires avoir). (5) sont très faim -> ont très faim (somatic state requires avoir). (6) parce que il -> parce qu'il (mandatory elision). (7) pas un restaurant -> pas de restaurant (negation collapse). (8) liaison after 'et' removed.")

    add_p("Paragraph 2 Correction (7 Errors Resolved):\n"
          "« Bonjour docteur. J'AI 35 ans et depuis hier soir, J'AI très chaud et j'ai froid en même temps. "
          "Mes deux enfants SONT aussi MALADES ; ils ONT peur du thermomètre et ils parlent [prononcé [parl]] sans cesse. "
          "Est-ce QU'IL y a des médicaments sans ordonnance ? Non, dans cette pharmacie il n'y a pas D'antibiotiques libres. "
          "Paul et toi, vous ÊTES très fatigués par cette épidémie saisonnière. »\n"
          "Linguistic Notes: (1) Je suis 35 ans -> J'ai 35 ans. (2) je suis chaud -> j'ai chaud (somatic sensation). (3) ont malade -> sont malades (malade is adjective describing state of health, takes être). (4) sont peur -> ont peur (fear requires avoir). (5) parlent pronounced [parl] (verbal -ent is silent, never [ɑ̃]). (6) est-ce que il -> est-ce qu'il (elision). (7) pas des antibiotiques -> pas d'antibiotiques (negation collapse). (8) vous avez fatigués -> vous êtes fatigués (fatigué is predicate adjective taking être).")

    add_p("Paragraph 3 Correction (7 Errors Resolved):\n"
          "« Toi et moi, nous PARTONS en vacances demain à l'aube. Dans notre valise, il n'y a pas DE maillots de bain. "
          "Nous admirons les [pas de liaison] héros du roman que nous lisons. Sur la table, il y a du vin rouge mais il n'y a pas DE pain. "
          "Pierre et lui ONT faim mais ils SONT très calmes. Est-ce que sur la plage il y a des transats libres ? "
          "Non, à cette saison, il n'y a pas DE transats disponibles nulle part. »\n"
          "Linguistic Notes: (1) nous partent -> nous partons (1st pers plural verb agreement). (2) pas des maillots -> pas de maillots (negation collapse). (3) liaison blocked before 'héros' (h aspiré). (4) pas du pain -> pas de pain (partitive collapses to de under negation). (5) sont faim -> ont faim (hunger requires avoir). (6) acoustic trap: ils ont [il-z‿õ] faim / ils sont [il-sõ] calmes. (7) pas des transats -> pas de transats (negation collapse).")

    # Save DOCX
    doc.save(DOCX_PATH)
    print(f"Successfully generated DOCX at: {DOCX_PATH}")

def build_pdf():
    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            num_pages = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                self.draw_page_decorations(num_pages)
                super().showPage()
            super().save()

        def draw_page_decorations(self, page_count):
            if self._pageNumber > 1:
                self.saveState()
                self.setFont("Helvetica", 8)
                self.setFillColor(colors.HexColor("#475569"))
                # Running header
                self.drawString(54, letter[1] - 36, "French Linguistic Diagnostic & Stress-Test Workbook  |  University Division")
                self.setStrokeColor(colors.HexColor("#CBD5E1"))
                self.setLineWidth(0.5)
                self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
                
                # Footer
                page_str = f"Page {self._pageNumber} of {page_count}"
                self.drawRightString(letter[0] - 54, 36, page_str)
                self.drawString(54, 36, "Zero-Tolerance Precision Assessment  •  Department of Applied Linguistics")
                self.line(54, 46, letter[0] - 54, 46)
                self.restoreState()

    pdf_doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=colors.white, alignment=1, spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName='Helvetica-Oblique', fontSize=10, leading=13,
        textColor=colors.HexColor('#E2E8F0'), alignment=1, spaceAfter=4
    )
    meta_style = ParagraphStyle(
        'CoverMeta', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=10,
        textColor=colors.HexColor('#94A3B8'), alignment=1
    )
    h1_style = ParagraphStyle(
        'DocH1', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=13, leading=16,
        textColor=colors.HexColor('#1E1B4B'), spaceBefore=12, spaceAfter=3
    )
    h2_style = ParagraphStyle(
        'DocH2', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=10.5, leading=13,
        textColor=colors.HexColor('#881337'), spaceBefore=8, spaceAfter=3
    )
    body_style = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11,
        textColor=colors.HexColor('#0F172A'), spaceBefore=1.5, spaceAfter=2
    )
    body_bold = ParagraphStyle(
        'DocBodyBold', parent=body_style,
        fontName='Helvetica-Bold'
    )
    muted_style = ParagraphStyle(
        'DocMuted', parent=body_style,
        fontName='Helvetica', textColor=colors.HexColor('#475569')
    )
    callout_t_style = ParagraphStyle(
        'CalloutTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=11,
        textColor=colors.HexColor('#1E1B4B'), spaceAfter=2
    )
    callout_b_style = ParagraphStyle(
        'CalloutBody', parent=styles['Normal'],
        fontName='Helvetica', fontSize=8, leading=10.5,
        textColor=colors.HexColor('#1E293B')
    )
    alert_t_style = ParagraphStyle(
        'AlertTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=11,
        textColor=colors.HexColor('#9A3412'), spaceAfter=2
    )
    danger_t_style = ParagraphStyle(
        'DangerTitle', parent=styles['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=11,
        textColor=colors.HexColor('#881337'), spaceAfter=2
    )

    story = []

    def make_callout(title, body, c_type="info"):
        if c_type == "danger":
            b_color = colors.HexColor('#881337')
            bg_color = colors.HexColor('#FFF1F2')
            t_style = danger_t_style
        elif c_type == "alert":
            b_color = colors.HexColor('#9A3412')
            bg_color = colors.HexColor('#FFFBEB')
            t_style = alert_t_style
        else:
            b_color = colors.HexColor('#1E1B4B')
            bg_color = colors.HexColor('#F1F5F9')
            t_style = callout_t_style
        
        t_para = Paragraph(title, t_style)
        b_para = Paragraph(body.replace('\n', '<br/>'), callout_b_style)
        
        tbl = Table([[ [t_para, b_para] ]], colWidths=[letter[0] - 108])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('LINELEFT', (0,0), (0,0), 3.5, b_color),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return tbl

    # Cover
    cover_data = [[ [
        Paragraph("FRENCH LINGUISTIC DIAGNOSTIC & STRESS-TEST WORKBOOK", title_style),
        Paragraph("A Brutally Thorough Examination of French Foundations, Phonetics, Pragmatics & Fossilized Errors", subtitle_style),
        Paragraph("Undergraduate French Linguistics & Advanced Foundations Division  •  Zero Tolerance for False Friends", meta_style)
    ] ]]
    cover_table = Table(cover_data, colWidths=[letter[0] - 108])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E1B4B')),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(cover_table)
    story.append(Spacer(1, 6))

    story.append(make_callout(
        "INSTRUCTIONAL PREAMBLE: THE STRESS-TEST PROTOCOL",
        "This diagnostic workbook is designed to aggressively challenge intermediate assumptions. "
        "Every section requires active cognitive production: classifying sociopragmatic registers, reducing compound subjects, "
        "differentiating minimal pairs, classifying 30 final consonants under phonetic rules, and correcting deceptive prose. "
        "Complete all tasks without reference materials; review Section 5 upon completion.",
        "danger"
    ))
    story.append(Spacer(1, 8))

    # SECTION 1
    story.append(Paragraph("SECTION 1: FOUNDATIONAL MECHANICS (Rapid Identification & Conjugation Drills)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=6))
    
    story.append(Paragraph("1.1 Complete Rapid-Fire Paradigm Grid: Isolation & Mixed Contexts", h2_style))
    story.append(Paragraph("Supply the exact present-indicative form of ÊTRE or AVOIR with mandatory elision.", body_style))
    
    grid_rows = [
        ["Prompt A", "Answer A", "Prompt B", "Answer B"],
        ["1. (Je + avoir)", "____________________", "7. (Je + être)", "____________________"],
        ["2. (Tu + être)", "____________________", "8. (Tu + avoir)", "____________________"],
        ["3. (Il/Elle/On + avoir)", "____________________", "9. (Il/Elle/On + être)", "____________________"],
        ["4. (Nous + être)", "____________________", "10. (Nous + avoir)", "____________________"],
        ["5. (Vous + avoir)", "____________________", "11. (Vous + être)", "____________________"],
        ["6. (Ils/Elles + être)", "____________________", "12. (Ils/Elles + avoir)", "____________________"]
    ]
    g_tbl = Table(grid_rows, colWidths=[130, 120, 130, 120])
    g_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E1B4B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(g_tbl)
    story.append(Spacer(1, 6))

    story.append(Paragraph("1.2 Subject Pronoun Reduction & Compound Subjects (15 Drill Items)", h2_style))
    pronoun_pdf = [
        "1. « Marie et toi » -> ____________________  |  2. « L'équipe et moi » -> ____________________",
        "3. « Le chien et la chatte » -> ____________________  |  4. « Mes deux sœurs et leur amie » -> ____________________",
        "5. « Toi et lui » -> ____________________  |  6. « Ni Paul ni moi » -> ____________________",
        "7. « Tout le monde » -> ____________________  |  8. « La majorité des étudiants » -> ____________________",
        "9. « Cet homme et ses enfants » -> ____________________  |  10. « Le professeur et vous » -> ____________________",
        "11. « Toi et tes collègues » -> ____________________  |  12. « Ma mère et mon père » -> ____________________",
        "13. « Les directrices et leurs associés » -> ____________________  |  14. « L'ensemble de la classe » -> ____________________",
        "15. « Ni toi ni elle » -> ____________________"
    ]
    for p_line in pronoun_pdf:
        story.append(Paragraph(p_line, body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("1.3 Elision Triggers & Structural Constraints (8 Precision Items)", h2_style))
    elision_pdf = [
        "1. (je + espérer) -> Result: ____________________ | Constraint: _____________________________________________",
        "2. (je + être) -> Result: ____________________ | Constraint: _____________________________________________",
        "3. (tu + aimer) [standard écrit] -> Result: ____________________ | Constraint: _____________________________________________",
        "4. (que + il) -> Result: ____________________ | Constraint: _____________________________________________",
        "5. (qui + il) -> Result: ____________________ | Constraint: _____________________________________________",
        "6. (si + il) -> Result: ____________________ | Constraint: _____________________________________________",
        "7. (si + elle) -> Result: ____________________ | Constraint: _____________________________________________",
        "8. (ce + être) -> Result: ____________________ | Constraint: _____________________________________________"
    ]
    for e_line in elision_pdf:
        story.append(Paragraph(e_line, body_style))

    # SECTION 2
    story.append(PageBreak())
    story.append(Paragraph("SECTION 2: PRAGMATIC & SEMANTIC STRESS-TESTS (Zero Tolerance for False Friends)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=6))
    
    story.append(Paragraph("2.1 The Tu vs. Vous Pragmatic Decision Matrix (10 Scenarios)", h2_style))
    tu_vous_pdf = [
        ("1. Prospective French mother-in-law (belle-mère) met at Sunday family lunch.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("2. Gendarme flagging car down on rural road for routine license check.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("3. Adult stranger in Châtelet metro station asking for the time.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("4. Two children (ages 6 and 9) playing on the sidewalk outside your building.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("5. Fellow 20-year-old student sitting next to you on first day at Sorbonne.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("6. Corporate division director during quarterly review.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("7. Independent artisan plumber arriving at apartment for repairs.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("8. Unknown dog sitting quietly on a café terrace.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("9. Table of four close childhood friends known since primary school.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________"),
        ("10. Exploratory Zoom call with high-value prospective client.",
         "[  ] Tu    [  ] Vous (Singulier formel)    [  ] Vous (Pluriel collectif) | Rationale: __________________________")
    ]
    for s_t, opt in tu_vous_pdf:
        story.append(Paragraph(f"<b>{s_t}</b>", body_style))
        story.append(Paragraph(opt, muted_style))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 6))
    story.append(Paragraph("2.2 The Être vs. Avoir Semantic Gauntlet (25 High-Stakes Sentences)", h2_style))
    g25_pdf = [
        "1. Malgré le chauffage éteint, les enfants n'______________ pas froid dans leur chambre.",
        "2. Mon grand-père fêtera bientôt son centenaire : il ______________ 99 ans aujourd'hui.",
        "3. Après une journée de jeûne médical, nous ______________ une faim insoutenable.",
        "4. Tu as vérifié les données du tableur ? Je crains que tu ______________ tort sur ce point.",
        "5. Il est trois heures du matin ; mes paupières sont lourdes, j'______________ sommeil.",
        "6. Pourquoi fermes-tu les volets ? Est-ce que tu ______________ peur des éclairs ?",
        "7. Les passagers bloqués sur le quai ______________ très en colère contre la SNCF.",
        "8. Ne touchez pas cette plaque de cuisson ! Elle ______________ brûlante (state).",
        "9. Piège critique : « Elle ______________ chaude » vs « Elle ______________ chaud » (distinguez le sens).",
        "10. Est-ce que vous ______________ d'accord avec les termes de ce contrat bilatéral ?",
        "11. Les étudiants ______________ besoin de consulter les archives avant leur thèse.",
        "12. Le patient tremble sous sa couverture : il ______________ 40 de fièvre.",
        "13. Vous ______________ en retard de quinze minutes pour l'entretien d'embauche.",
        "14. Elle n'ose pas parler en public car elle ______________ honte de son accent.",
        "15. Nous ______________ très fiers des résultats académiques de nos élèves.",
        "16. Ce matin, je me sens faible : je pense que je ______________ malade (condition).",
        "17. Après 42 km sous la canicule, vous ______________ une soif dévorante.",
        "18. Le témoin affirme que le suspect ______________ l'air suspect et agité.",
        "19. Nous n'______________ pas l'habitude de dîner avant 21 heures en Espagne.",
        "20. Malgré leurs excuses, ils ______________ entièrement responsables de l'accident.",
        "21. Pourquoi cries-tu ? Est-ce que tu ______________ mal à la tête ou à la gorge ?",
        "22. Qui ______________ raison dans ce débat juridique, le procureur ou la défense ?",
        "23. Ce soir, on ______________ envie de déguster des fruits de mer sur le port.",
        "24. Les touristes ______________ perdus dans les ruelles médiévales de la vieille ville.",
        "25. Je ne peux pas sortir ce soir : je ______________ épuisé par ma garde à l'hôpital."
    ]
    for sent in g25_pdf:
        story.append(Paragraph(sent, body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("2.3 \"Il y a\" Multi-Step Syntactic Transformations (8 Drills)", h2_style))
    t8_pdf = [
        ("1. « Il y a un problème technique avec le serveur central. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("2. « Il y a une pharmacie ouverte le dimanche dans ce quartier. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("3. « Il y a des erreurs de calcul dans le rapport financier. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("4. « Il y a un ascenseur fonctionnel dans cet immeuble. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("5. « Il y a de l'eau potable disponible dans le refuge. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("6. « Il y a des places assises réservées pour les aînés. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("7. « Il y a une issue de secours à l'arrière de la salle. »",
         "Inversion: ________________________________________ | Neg: ________________________________________"),
        ("8. « Il y a des documents confidentiels sur le bureau. »",
         "Inversion: ________________________________________ | Neg: ________________________________________")
    ]
    for aff, resp in t8_pdf:
        story.append(Paragraph(f"<b>{aff}</b>", body_style))
        story.append(Paragraph(resp, muted_style))
        story.append(Spacer(1, 1))

    # SECTION 3
    story.append(PageBreak())
    story.append(Paragraph("SECTION 3: THE PHONETIC GAUNTLET (Pronunciation & Decoding)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=6))
    
    story.append(Paragraph("3.1 Silent vs. Sounded Final Consonants: 30-Word Forensic Classification", h2_style))
    story.append(Paragraph("Classify each final consonant in isolation as [SILENT] or [PRONOUNCED] and provide IPA.", body_style))
    
    t30_pdf_data = [
        ["Word (Target)", "Class", "IPA", "Word (Target)", "Class", "IPA"],
        ["1. blanc (c)", "[ ] Sil [ ] Pro", "/______/", "16. net (t)", "[ ] Sil [ ] Pro", "/______/"],
        ["2. est (st)", "[ ] Sil [ ] Pro", "/______/", "17. chef (f)", "[ ] Sil [ ] Pro", "/______/"],
        ["3. lit (t)", "[ ] Sil [ ] Pro", "/______/", "18. pied (d)", "[ ] Sil [ ] Pro", "/______/"],
        ["4. lits (ts)", "[ ] Sil [ ] Pro", "/______/", "19. fusil (l)", "[ ] Sil [ ] Pro", "/______/"],
        ["5. clef (f)", "[ ] Sil [ ] Pro", "/______/", "20. corps (rps)", "[ ] Sil [ ] Pro", "/______/"],
        ["6. hiver (r)", "[ ] Sil [ ] Pro", "/______/", "21. sirop (p)", "[ ] Sil [ ] Pro", "/______/"],
        ["7. tabac (c)", "[ ] Sil [ ] Pro", "/______/", "22. coup (p)", "[ ] Sil [ ] Pro", "/______/"],
        ["8. nid (d)", "[ ] Sil [ ] Pro", "/______/", "23. plat (t)", "[ ] Sil [ ] Pro", "/______/"],
        ["9. fils [son] (ls)", "[ ] Sil [ ] Pro", "/______/", "24. nez (z)", "[ ] Sil [ ] Pro", "/______/"],
        ["10. fils [threads] (s)", "[ ] Sil [ ] Pro", "/______/", "25. dix [alone] (x)", "[ ] Sil [ ] Pro", "/______/"],
        ["11. six [alone] (x)", "[ ] Sil [ ] Pro", "/______/", "26. gaz (z)", "[ ] Sil [ ] Pro", "/______/"],
        ["12. sept (pt)", "[ ] Sil [ ] Pro", "/______/", "27. sac (c)", "[ ] Sil [ ] Pro", "/______/"],
        ["13. huit [alone] (t)", "[ ] Sil [ ] Pro", "/______/", "28. drap (p)", "[ ] Sil [ ] Pro", "/______/"],
        ["14. porc (rc)", "[ ] Sil [ ] Pro", "/______/", "29. sang (g)", "[ ] Sil [ ] Pro", "/______/"],
        ["15. mer (r)", "[ ] Sil [ ] Pro", "/______/", "30. respect (ct)", "[ ] Sil [ ] Pro", "/______/"]
    ]
    t30_tbl = Table(t30_pdf_data, colWidths=[90, 80, 75, 95, 80, 80])
    t30_tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E1B4B')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t30_tbl)
    story.append(Spacer(1, 6))

    story.append(Paragraph("3.2 Acoustic Discrimination & Minimal Pairs (8 Precision Pairs)", h2_style))
    mp_pdf = [
        "1. « ils ont » vs « ils sont » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "2. « dessus » vs « dessous » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "3. « vin » vs « vent » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "4. « un » vs « une » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "5. « bon » vs « bonne » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "6. « plein » vs « pleine » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "7. « beau » vs « bon » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________",
        "8. « poisson » vs « poison » -> IPA 1: /_________/ | IPA 2: /_________/ | Feature: ____________________"
    ]
    for mp_l in mp_pdf:
        story.append(Paragraph(mp_l, body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("3.3 The Liaison Traffic Light: Mandatory, Optional, or Forbidden (10 Sentences)", h2_style))
    l_pdf = [
        "1. « Les [ _|_ ] amis de ma sœur arrivent. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "2. « Paul et [ _|_ ] un collègue préparent. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "3. « Cet étudiant [ _|_ ] intelligent a réussi. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "4. « Nous admirons les [ _|_ ] héros. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "5. « Arrivées vers [ _|_ ] onze heures. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "6. « Un homme très [ _|_ ] aimable. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "7. « Des livres [ _|_ ] intéressants. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "8. « Ils sont [ _|_ ] amis depuis l'enfance. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "9. « Ont [ _|_ ] ils terminé leurs devoirs ? » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________",
        "10. « Un soldat [ _|_ ] anglais monte la garde. » -> [ ] MAND [ ] OPT [ ] FORBID | Sound/Barrier: _____________"
    ]
    for l_line in l_pdf:
        story.append(Paragraph(l_line, body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("3.4 Accent Shift Mechanics: 8 Contrastive Minimal Pairs", h2_style))
    acc_pdf = [
        "1. « a » vs « à » -> Shift: __________________________________________________________________________",
        "2. « ou » vs « où » -> Shift: __________________________________________________________________________",
        "3. « sur » vs « sûr » -> Shift: __________________________________________________________________________",
        "4. « manger » vs « mangé » -> Shift: __________________________________________________________________________",
        "5. « du » vs « dû » -> Shift: __________________________________________________________________________",
        "6. « des » vs « dès » -> Shift: __________________________________________________________________________",
        "7. « la » vs « là » -> Shift: __________________________________________________________________________",
        "8. « peche » vs « pêche » -> Shift: __________________________________________________________________________"
    ]
    for a_line in acc_pdf:
        story.append(Paragraph(a_line, body_style))

    # SECTION 4
    story.append(PageBreak())
    story.append(Paragraph("SECTION 4: BRUTAL ERROR-HUNTING & PARAGRAPH CORRECTION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=6))
    story.append(Paragraph("Locate each deceptive error in the paragraphs below, categorize the violation, and rewrite cleanly.", body_style))
    
    p3_pdf = [
        ("Paragraph 1: Une journée ordinaire au bureau",
         "« Bonjour monsieur le Directeur. Est-ce que tu as cinq minutes ? Marie et moi, on parlent du budget annuel. "
         "Dans notre service, il n'y a pas des ordinateurs portables disponibles et les stagiaires sont 21 ans. "
         "Ils sont très faim à midi parce que il n'y a pas un restaurant d'entreprise dans l'immeuble. "
         "Mon collègue et [liaison prononcée] un client attendent votre réponse depuis ce matin. »",
         "Correction: ____________________________________________________________________________________________________<br/>"
         "____________________________________________________________________________________________________"),
        ("Paragraph 2: Une visite médicale compliquée",
         "« Bonjour docteur. Je suis 35 ans et depuis hier soir, je suis très chaud et j'ai froid en même temps. "
         "Mes deux enfants ont aussi malade ; ils sont peur du thermomètre et ils parlent [prononcé [par-lɑ̃]] sans cesse. "
         "Est-ce que il y a des médicaments sans ordonnance ? Non, dans cette pharmacie il n'y a pas des antibiotiques libres. "
         "Paul et toi, vous avez très fatigués par cette épidémie saisonnière. »",
         "Correction: ____________________________________________________________________________________________________<br/>"
         "____________________________________________________________________________________________________"),
        ("Paragraph 3: Le départ mouvementé en vacances",
         "« Toi et moi, nous partent en vacances demain à l'aube. Dans notre valise, il n'y a pas des maillots de bain. "
         "Nous admirons les [liaison [z]] héros du roman que nous lisons. Sur la table, il y a du vin rouge mais il n'y a pas du pain. "
         "Pierre et lui sont faim mais ils ont [prononcé avec [s]] très calmes. Est-ce que sur la plage il y a des transats libres ? "
         "Non, à cette saison, il n'y a pas des transats disponibles nulle part. »",
         "Correction: ____________________________________________________________________________________________________<br/>"
         "____________________________________________________________________________________________________")
    ]
    for p_t, p_fl, p_cr in p3_pdf:
        story.append(Paragraph(f"<b>{p_t}</b>", body_style))
        story.append(Paragraph(f"<i>{p_fl}</i>", muted_style))
        story.append(Paragraph(p_cr, muted_style))
        story.append(Spacer(1, 4))

    # SECTION 5: ANSWER KEY
    story.append(PageBreak())
    story.append(Paragraph("SECTION 5: UNCOMPROMISING ANSWER KEY & TECHNICAL EXPLANATIONS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=6))
    story.append(make_callout(
        "DIAGNOSTIC PROTOCOL: ZERO PERFORMANCE AGREEMENT",
        "Review every mistake through the analytical linguistic explanations below to eliminate fossilized errors.",
        "alert"
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Section 1 Solutions: Foundational Mechanics", h2_style))
    story.append(Paragraph("<b>1.1 Conjugation Grid:</b> 1. J'ai (elision mandatory) | 2. Tu es | 3. Il/Elle/On a | 4. Nous sommes | 5. Vous avez | 6. Ils/Elles sont || 7. Je suis (no elision) | 8. Tu as | 9. Il/Elle/On est | 10. Nous avons | 11. Vous êtes | 12. Ils/Elles ont.", body_style))
    story.append(Paragraph("<b>1.2 Subject Pronouns:</b> 1. VOUS | 2. NOUS | 3. ILS | 4. ELLES | 5. VOUS | 6. NOUS | 7. IL | 8. ELLE | 9. ILS | 10. VOUS | 11. VOUS | 12. ILS | 13. ILS | 14. IL | 15. VOUS.", body_style))
    story.append(Paragraph("<b>1.3 Elision Triggers:</b> 1. J'espère (mandatory) | 2. Je suis (forbidden before consonant) | 3. Tu aimes (forbidden in standard written French) | 4. Qu'il (mandatory) | 5. Qui il (forbidden; 'qui' never elides) | 6. S'il (mandatory before il/ils) | 7. Si elle (forbidden; 'si' never elides before elle/elles) | 8. C'est (mandatory before vowel).", body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Section 2 Solutions: Pragmatic & Semantic Stress-Tests", h2_style))
    story.append(Paragraph("<b>2.1 Pragmatic Matrix:</b> 1. Vous (sing. formel) | 2. Vous (sing. formel) | 3. Vous (sing. formel) | 4. Vous (pluriel collectif) | 5. Tu | 6. Vous (sing. formel) | 7. Vous (sing. formel) | 8. Tu | 9. Vous (pluriel collectif) | 10. Vous (sing. formel).", body_style))
    story.append(Paragraph("<b>2.2 Être vs Avoir Gauntlet:</b> 1. ont (avoir froid) | 2. a (avoir X ans) | 3. avons (avoir faim) | 4. as (avoir tort) | 5. ai (avoir sommeil) | 6. as (avoir peur) | 7. sont (être en colère) | 8. est (brûlante) | 9. Avoir chaud = température corporelle; Être chaude = argot à connotation sexuelle | 10. êtes | 11. ont (avoir besoin) | 12. a (de la fièvre) | 13. êtes (en retard) | 14. a (avoir honte) | 15. sommes (fiers) | 16. suis (malade) | 17. avez (soif) | 18. a (avoir l'air) | 19. avons (l'habitude) | 20. sont (responsables) | 21. as (mal à) | 22. a (raison) | 23. a (envie) | 24. sont (perdus) | 25. suis (épuisé).", body_style))
    story.append(Paragraph("<b>2.3 \"Il y a\" Transformations:</b> 1. Y a-t-il un... ? / Il n'y a pas de... | 2. Y a-t-il une... ? / Il n'y a pas de... | 3. Y a-t-il des... ? / Il n'y a pas d'... | 4. Y a-t-il un... ? / Il n'y a pas d'... | 5. Y a-t-il de l'... ? / Il n'y a pas d'... | 6. Y a-t-il des... ? / Il n'y a pas de... | 7. Y a-t-il une... ? / Il n'y a pas d'... | 8. Y a-t-il des... ? / Il n'y a pas de...", body_style))

    story.append(make_callout(
        "TECHNICAL LINGUISTIC NOTE: THE ARTICLE COLLAPSE",
        "Direct negation collapses indefinite ('un/une/des') and partitive ('du/de la') articles into 'de/d''. "
        "Saying *« Il n'y a pas des livres » is ungrammatical; zero quantity requires the prepositional particle 'de'.",
        "alert"
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Section 3 Solutions: The Phonetic Gauntlet", h2_style))
    story.append(Paragraph("<b>3.1 30-Word Finals:</b> 1. blanc (sil /blɑ̃/) | 2. est (sil /ɛ/) | 3. lit (sil /li/) | 4. lits (sil /li/) | 5. clef (sil /kle/) | 6. hiver (pro /i.vɛʁ/) | 7. tabac (sil /ta.ba/) | 8. nid (sil /ni/) | 9. fils [son] (pro s /fis/) | 10. fils [threads] (sil s /fil/) | 11. six (pro /sis/) | 12. sept (pro t /sɛt/) | 13. huit (pro /ɥit/) | 14. porc (sil /pɔʁ/) | 15. mer (pro /mɛʁ/) | 16. net (pro /nɛt/) | 17. chef (pro /ʃɛf/) | 18. pied (sil /pje/) | 19. fusil (sil /fy.zi/) | 20. corps (sil /kɔʁ/) | 21. sirop (sil /si.ʁo/) | 22. coup (sil /ku/) | 23. plat (sil /pla/) | 24. nez (sil /ne/) | 25. dix (pro /dis/) | 26. gaz (pro /ɡaz/) | 27. sac (pro /sak/) | 28. drap (sil /dʁa/) | 29. sang (sil /sɑ̃/) | 30. respect (sil /ʁɛs.pɛ/).", body_style))
    story.append(Paragraph("<b>3.2 Minimal Pairs:</b> 1. /il.z‿õ/ (avoir [z]) vs /il.sõ/ (être [s]) | 2. /də.sy/ [y] vs /də.su/ [u] | 3. /vɛ̃/ [ɛ̃] vs /vɑ̃/ [ɑ̃] | 4. /œ̃/ [œ̃] vs /yn/ [yn] | 5. /bɔ̃/ vs /bɔn/ | 6. /plɛ̃/ vs /plɛn/ | 7. /bo/ [o] vs /bɔ̃/ [ɔ̃] | 8. /pwa.sõ/ [s] vs /pwa.zõ/ [z].", body_style))
    story.append(Paragraph("<b>3.3 Liaisons:</b> 1. MANDATORY [z] | 2. FORBIDDEN (after 'et') | 3. FORBIDDEN (singular noun + adj) | 4. FORBIDDEN ('h aspiré') | 5. FORBIDDEN (before 'onze') | 6. MANDATORY [z] | 7. OPTIONAL [z] | 8. OPTIONAL [t] | 9. MANDATORY [t] | 10. FORBIDDEN (singular noun).", body_style))
    story.append(Paragraph("<b>3.4 Accent Shifts:</b> 1. a (verb) vs à (prep) | 2. ou (or) vs où (where) | 3. sur (on) vs sûr (sure) | 4. manger (inf) vs mangé (participle) | 5. du (art) vs dû (devoir) | 6. des (art) vs dès (as soon as) | 7. la (art/pro) vs là (there) | 8. peche (invalid) vs pêche (peach/fishing).", body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Section 4 Solutions: Brutal Error-Hunting", h2_style))
    story.append(Paragraph("<b>Paragraph 1:</b> « Bonjour Monsieur le Directeur. Est-ce que <u>vous avez</u> cinq minutes ? Marie et moi, on <u>parle</u> du budget annuel. Dans notre service, il n'y a pas <u>d'ordinateurs</u> portables disponibles et les stagiaires <u>ont</u> 21 ans. Ils <u>ont</u> très faim à midi parce <u>qu'il</u> n'y a pas <u>de</u> restaurant d'entreprise dans l'immeuble. Mon collègue et [pas de liaison] un client attendent votre réponse depuis ce matin. »", body_style))
    story.append(Paragraph("<b>Paragraph 2:</b> « Bonjour docteur. <u>J'ai</u> 35 ans et depuis hier soir, <u>j'ai</u> très chaud et j'ai froid en même temps. Mes deux enfants <u>sont</u> aussi <u>malades</u> ; ils <u>ont</u> peur du thermomètre et ils parlent [prononcé [parl]] sans cesse. Est-ce <u>qu'il</u> y a des médicaments sans ordonnance ? Non, dans cette pharmacie il n'y a pas <u>d'antibiotiques</u> libres. Paul et toi, vous <u>êtes</u> très fatigués par cette épidémie saisonnière. »", body_style))
    story.append(Paragraph("<b>Paragraph 3:</b> « Toi et moi, nous <u>partons</u> en vacances demain à l'aube. Dans notre valise, il n'y a pas <u>de</u> maillots de bain. Nous admirons les [pas de liaison] héros du roman que nous lisons. Sur la table, il y a du vin rouge mais il n'y a pas <u>de</u> pain. Pierre et lui <u>ont</u> faim mais ils <u>sont</u> très calmes. Est-ce que sur la plage il y a des transats libres ? Non, à cette saison, il n'y a pas <u>de</u> transats disponibles nulle part. »", body_style))

    # Build PDF
    pdf_doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at: {PDF_PATH}")

if __name__ == "__main__":
    build_docx()
    build_pdf()
