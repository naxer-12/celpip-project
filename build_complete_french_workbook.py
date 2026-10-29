import os
import sys

# Script to generate complete French Foundations Practice Workbook in DOCX and PDF

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/jainamshah/Downloads/Learning French"
DOCX_PATH = os.path.join(BASE_DIR, "French_Foundations_Workbook.docx")
PDF_PATH = os.path.join(BASE_DIR, "French_Foundations_Workbook.pdf")

# Palette
NAVY_HEX = "1B365D"
SLATE_HEX = "4A607A"
AMBER_HEX = "B45309"
RED_HEX = "B91C1C"
LIGHT_BG = "F8FAFC"
CALLOUT_BG = "F1F5F9"
ALERT_BG = "FFFBEB"
BORDER_HEX = "CBD5E1"
DARK_TEXT_HEX = "0F172A"

NAVY_RGB = RGBColor(27, 54, 93)
SLATE_RGB = RGBColor(74, 96, 122)
AMBER_RGB = RGBColor(180, 83, 9)
RED_RGB = RGBColor(185, 28, 28)
DARK_RGB = RGBColor(15, 23, 42)
MUTED_RGB = RGBColor(100, 116, 139)

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

def create_docx():
    doc = docx.Document()
    
    # Page setup - 0.75 in margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
        # Header / Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("French Foundations Practice Workbook  |  Zero-Revision System")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = MUTED_RGB
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("CEFR A1–A2 Active Mastery  •  Applied Linguistics & Instructional Design")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = MUTED_RGB

    def add_p(text="", style='Normal', space_before=0, space_after=4, bold=False, italic=False, color=DARK_RGB, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
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
        p.paragraph_format.space_after = Pt(6)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(16)
        r.font.bold = True
        r.font.color.rgb = NAVY_RGB
        
        # Bottom accent border line via table or thin rule
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.columns[0].width = Inches(7.0)
        c = t.cell(0, 0)
        style_cell(c, fill_hex=NAVY_HEX, borders={}, pad_tb=15, pad_lr=0)
        cp = c.paragraphs[0]
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        cpr = cp.add_run("")
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_h2(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(12.5)
        r.font.bold = True
        r.font.color.rgb = SLATE_RGB
        return p

    def add_callout_box(title, content, callout_type="info"):
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
            b_col = RED_HEX
            bg_col = "FEF2F2"
            t_col = RED_RGB
        else:
            b_col = NAVY_HEX
            bg_col = CALLOUT_BG
            t_col = NAVY_RGB

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
        rc = p2.add_run(content)
        rc.font.name = "Calibri"
        rc.font.size = Pt(9.5)
        rc.font.color.rgb = DARK_RGB
        
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ COVER / TITLE ------------------
    cover_tbl = doc.add_table(rows=1, cols=1)
    cover_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cover_tbl.autofit = False
    cover_tbl.columns[0].width = Inches(7.0)
    c_cell = cover_tbl.cell(0, 0)
    style_cell(c_cell, fill_hex=NAVY_HEX, borders={}, pad_tb=300, pad_lr=240)
    
    cp1 = c_cell.paragraphs[0]
    cp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp1.paragraph_format.space_before = Pt(0)
    cp1.paragraph_format.space_after = Pt(4)
    rt = cp1.add_run("FRENCH FOUNDATIONS PRACTICE WORKBOOK")
    rt.font.name = "Calibri"
    rt.font.size = Pt(22)
    rt.font.bold = True
    rt.font.color.rgb = RGBColor(255, 255, 255)
    
    cp2 = c_cell.add_paragraph()
    cp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp2.paragraph_format.space_before = Pt(2)
    cp2.paragraph_format.space_after = Pt(8)
    rs = cp2.add_run("The Zero-Revision Applied Linguistics System: Muscle Memory, Acoustic Calibration & Register Mastery")
    rs.font.name = "Calibri"
    rs.font.size = Pt(11)
    rs.font.italic = True
    rs.font.color.rgb = RGBColor(226, 232, 240)

    cp3 = c_cell.add_paragraph()
    cp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp3.paragraph_format.space_before = Pt(4)
    cp3.paragraph_format.space_after = Pt(0)
    rm = cp3.add_run("Comprehensive Active Practice  •  100% Non-Ambiguous Tasks  •  Annotated Analytical Answer Key")
    rm.font.name = "Calibri"
    rm.font.size = Pt(9)
    rm.font.color.rgb = RGBColor(148, 163, 184)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Pedagogical Architecture Callout
    add_callout_box(
        "METHODOLOGICAL DESIGN: ZERO-REVISION MASTERY ARCHITECTURE",
        "This workbook is engineered using cognitive elimination tasks, contrastive analysis, and acoustic transcription drills. "
        "Standard workbooks force students to constantly re-read grammar explanations because they test passive recognition. "
        "Here, every exercise forces high-stakes active retrieval: you must choose registers under realistic pragmatic constraints, "
        "physically strike silent letters, differentiate homophones through liaison phonetics, and collapse articles under negation. "
        "Once completed and checked against the 'Why You Tripped' analytical key, the target structures become intuitive reflexes.",
        "info"
    )

    # -------------------------------------------------------------
    # PART 1: TARGETED DIAGNOSTICS
    # -------------------------------------------------------------
    add_h1("PART 1: TARGETED DIAGNOSTICS (Isolating the Mechanics)")
    
    # MODULE 1A
    add_h2("Module 1A: Pronoun Nuance & Social Calibration (\"Tu\" vs. \"Vous\" & \"On\")")
    add_callout_box(
        "CORE MECHANIC: REGISTRATION & SEMANTIC POLARITY",
        "• TU: Solidarity, horizontal intimacy, children (<12), pets, fellow students.\n"
        "• VOUS (Singular): Deference, vertical hierarchy, strangers, professionals, commercial transactions.\n"
        "• VOUS (Plural): Any group of 2+ individuals, regardless of intimacy.\n"
        "• ON: Grammatically 3rd person singular (verb ends like il/elle). Semantically: (1) Informal spoken 'we' (nous) where adjectives agree with the real subjects; (2) Universal indefinite 'people in general / one' where adjectives remain masculine singular.",
        "info"
    )

    add_p("Drill 1.1: Pragmatic Register Classification (Scenarios 1–10)", bold=True, color=SLATE_RGB, size=11, space_before=6)
    add_p("For each scenario, mark the required address pronoun and state the sociolinguistic justification.")

    scenarios = [
        ("1. You walk into a Parisian boulangerie at 7:30 AM to buy a baguette from the baker.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("2. You meet a 20-year-old student sitting next to you on your first day at the Sorbonne.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("3. You are petting an energetic Golden Retriever puppy in the Jardin des Tuileries.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("4. You meet your 76-year-old neighbor, Madame Mercier, collecting mail in your building's lobby.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("5. You are in your annual performance evaluation with your corporate department director in La Défense.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("6. You ask an armed police officer (agent de police) near the Gare du Nord for walking directions.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("7. You arrive at a terrace table where your 4 closest childhood friends are waiting for drinks.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("8. You conduct an introductory discovery video call with a prospective corporate consulting client.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("9. You comfort an 8-year-old lost child crying in the Galeries Lafayette department store.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________"),
        ("10. Two elderly American tourists stop you on the Pont Neuf asking in French for the metro entrance.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Sociolinguistic Justification: ____________________________________________________________________")
    ]

    for title, opts, just in scenarios:
        add_p(title, bold=True, space_before=4, space_after=1)
        add_p(opts, space_before=0, space_after=1)
        add_p(just, color=MUTED_RGB, space_before=0, space_after=4)

    add_p("Drill 1.2: The Meaning-Shift & Agreement of \"On\" (Items 11–15)", bold=True, color=SLATE_RGB, size=11, space_before=8)
    add_p("Conjugate the verb, select the correct adjective agreement, and classify the semantic role of 'on'.")

    on_items = [
        ("11. En France, on (manger / mangent) ______________ souvent du fromage avant le dessert.\n"
         "Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'\n"
         "Agreement check: ___________________________________________________________________"),
        ("12. Marc et moi, ce soir on (être) ______________ très (fatigué / fatigués / fatiguée) ______________.\n"
         "Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'\n"
         "Agreement check: ___________________________________________________________________"),
        ("13. Quand on (avoir) ______________ peur dans le noir, le rythme cardiaque s'accélère.\n"
         "Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'\n"
         "Agreement check: ___________________________________________________________________"),
        ("14. Avec Camille et Élodie, demain on (aller) ______________ à la plage ; on est (ravi / ravis / ravies) ______________.\n"
         "Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'\n"
         "Agreement check: ___________________________________________________________________"),
        ("15. Dans cette bibliothèque nationale, on ne (devoir / doivent) ______________ pas parler à voix haute.\n"
         "Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'\n"
         "Agreement check: ___________________________________________________________________")
    ]
    for item in on_items:
        add_p(item, space_before=3, space_after=4)

    # MODULE 1B
    add_h2("Module 1B: Être vs. Avoir (Conjugation & Idiomatic Collisions)")
    add_callout_box(
        "CORE MECHANIC: ELISION & FALSE-FRIEND IDIOMS",
        "• Elision: 'Je' drops the -e before vowels/silent-h ONLY with avoir (J'ai, J'avais) and vowel verbs. NEVER with être: 'Je suis' (no elision possible).\n"
        "• The English False-Friend Trap: English uses 'to be' for physiological sensations, but French views them as temporary POSSESSIONS governed by AVOIR:\n"
        "  - avoir X ans (to be X years old)\n"
        "  - avoir faim / soif (to be hungry / thirsty)\n"
        "  - avoir chaud / froid (to be hot / cold)\n"
        "  - avoir peur / sommeil (to be afraid / sleepy)\n"
        "  - avoir raison / tort (to be right / wrong)\n"
        "  - avoir besoin de / envie de (to need / to feel like)",
        "info"
    )

    add_p("Drill 1.3: Speed Paradigm & Elision Precision (Items 1–7)", bold=True, color=SLATE_RGB, size=11, space_before=6)
    add_p("Fill in the exact conjugated form of ÊTRE or AVOIR with mandatory elision applied.")

    drill_1_3 = [
        "1. (Je + avoir) ______________ 28 ans et (je + être) ______________ ingénieur à Lyon.",
        "2. Nous (être) ______________ très occupés aujourd'hui, mais nous (avoir) ______________ le temps d'écouter.",
        "3. Tu (être) ______________ prêt pour la présentation, ou tu (avoir) ______________ encore des doutes ?",
        "4. Ils (avoir) ______________ un nouvel appartement au centre-ville et ils (être) ______________ ravis.",
        "5. Vous (être) ______________ en avance, mais vous (avoir) ______________ tout votre matériel avec vous.",
        "6. Elle (avoir) ______________ deux sœurs qui (être) ______________ chirurgiennes à l'hôpital Pasteur.",
        "7. On (être) ______________ lundi matin et on (avoir) ______________ déjà une réunion importante."
    ]
    for d in drill_1_3:
        add_p(d, space_before=2, space_after=3)

    add_p("Drill 1.4: False-Friend Idiomatic Collision Drills (Items 8–15)", bold=True, color=SLATE_RGB, size=11, space_before=8)
    add_p("Supply the conjugated form of ÊTRE or AVOIR. Identify the English false-friend trigger.")

    drill_1_4 = [
        "8. Pendant la tempête de neige, les randonneurs ______________ extrêmement froid aux mains.\n"
        "   Idiom check: ________________________________________________________________________",
        "9. Antoine a fêté son anniversaire hier : il ______________ maintenant 35 ans.\n"
        "   Idiom check: ________________________________________________________________________",
        "10. Après 25 kilomètres de marche sous le soleil de midi, nous ______________ une soif terrible.\n"
        "   Idiom check: ________________________________________________________________________",
        "11. Tu as recompté les totaux ? Je pense que tu ______________ tort et que le comptable ______________ raison.\n"
        "   Idiom check: ________________________________________________________________________",
        "12. Il est deux heures du matin ; les enfants ne tiennent plus debout, ils ______________ sommeil.\n"
        "   Idiom check: ________________________________________________________________________",
        "13. Pourquoi fermes-tu la porte à clé ? Est-ce que tu ______________ peur du noir ?\n"
        "   Idiom check: ________________________________________________________________________",
        "14. Ce matin, elle ______________ épuisée (state) parce qu'elle ______________ beaucoup de soucis (possession).\n"
        "   Contrast check: _____________________________________________________________________",
        "15. Est-ce que vous ______________ besoin d'une pause ou est-ce que vous ______________ prêts à continuer ?\n"
        "   Contrast check: _____________________________________________________________________"
    ]
    for d in drill_1_4:
        add_p(d, space_before=3, space_after=3)

    # MODULE 1C
    add_h2("Module 1C: The French Sound Engine & Phonetics")
    add_callout_box(
        "CORE PHONETIC MECHANICS: THE SPOKEN ENGINE",
        "• The CaReFuL Rule: Consonants C, R, F, L are generally PRONOUNCED at the end of words (sac, hiver, chef, ciel). Consonants D, S, T, X, P, G are SILENT (grand, chats, lit, deux, trop, sang).\n"
        "• Plural Verb Trap: The 3rd person plural verb ending '-ent' (ils parlent, ils vendent) is 100% SILENT ([parl], [vɑ̃d]). It is NEVER pronounced as a nasal vowel [-ɑ̃]!\n"
        "• Nasal Vowels: Vowel + single N/M followed by consonant or word boundary = Nasal (bon [bõ], fin [fɛ̃], un [œ̃]). Double N/M or following vowel destroys nasalization (bonne [bɔn], fine [fin], une [yn]).\n"
        "• Liaisons: Under-arc (‿) carries latent final consonant to the next vowel sound. 'Ils ont' = [il-z‿õ]. 'Ils sont' = [il-sõ]. Liaison after 'ET' is CATEGORICALLY FORBIDDEN (glottal boundary).",
        "info"
    )

    add_p("Drill 1.5: Silent Consonant Striking Radar (Sentences 1–5)", bold=True, color=SLATE_RGB, size=11, space_before=6)
    add_p("Physically strike out (or list) every silent final consonant letter and the silent verbal '-ent' endings.")

    drill_1_5 = [
        "1. « Ils parlent tout le temps avec leurs petits enfants. »\n"
        "   List silent letters / endings: ________________________________________________________\n"
        "   Phonetic transcription summary: ____________________________________________________",
        "2. « Le grand chat blanc dort sous le lit en bois. »\n"
        "   List silent letters / endings: ________________________________________________________\n"
        "   Phonetic transcription summary: ____________________________________________________",
        "3. « Nous attendons le train de nuit dans un grand froid. »\n"
        "   List silent letters / endings: ________________________________________________________\n"
        "   Phonetic transcription summary: ____________________________________________________",
        "4. « Les deux vieux loups gris courent vers le bois épais. »\n"
        "   List silent letters / endings: ________________________________________________________\n"
        "   Phonetic transcription summary: ____________________________________________________",
        "5. « Cet aspect du projet est trop suspect et très lourd. »\n"
        "   List silent letters / endings: ________________________________________________________\n"
        "   Phonetic transcription summary: ____________________________________________________"
    ]
    for d in drill_1_5:
        add_p(d, space_before=3, space_after=3)

    add_p("Drill 1.6: Nasal vs. Oral Minimal Pair Discrimination (Items 6–10)", bold=True, color=SLATE_RGB, size=11, space_before=8)
    add_p("Classify each word as having a [Nasal Vowel] or an [Oral Vowel + Pronounced Consonant].")

    drill_1_6 = [
        "6. bon  [  ] Nasal  [  ] Oral         vs.    bonne   [  ] Nasal  [  ] Oral",
        "7. fin  [  ] Nasal  [  ] Oral         vs.    fine    [  ] Nasal  [  ] Oral",
        "8. un   [  ] Nasal  [  ] Oral         vs.    une     [  ] Nasal  [  ] Oral",
        "9. plein [  ] Nasal  [  ] Oral        vs.    pleine  [  ] Nasal  [  ] Oral",
        "10. cousin [  ] Nasal  [  ] Oral      vs.    cousine [  ] Nasal  [  ] Oral"
    ]
    for d in drill_1_6:
        add_p(d, space_before=2, space_after=2)

    add_p("Drill 1.7: The Liaison Radar: Mandatory (‿) vs. Forbidden (✗) (Items 11–15)", bold=True, color=SLATE_RGB, size=11, space_before=8)
    add_p("Mark each underlined junction as Mandatory (‿) with its phonetic transition sound ([z], [t], [n]) or Forbidden (✗).")

    drill_1_7 = [
        "11. Junction comparison:\n"
        "    a) « Ils ___ ont vingt ans. »      Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]\n"
        "    b) « Ils ___ sont calmes. »       Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]",
        "12. Junction comparison:\n"
        "    a) « C'est un ___ ami fidèle. »   Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]\n"
        "    b) « Paul et ___ un ami. »        Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]",
        "13. Junction comparison:\n"
        "    a) « Il est très ___ élégant. »   Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]\n"
        "    b) « Un soldat ___ anglais. »     Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]",
        "14. Junction comparison:\n"
        "    a) « Elle reste chez ___ elle. »   Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]\n"
        "    b) « Vers ___ onze heures. »      Mark: [ ‿ / ✗ ]  Transition sound: [ ___ ]",
        "15. Acoustic Minimal Pair Transcription (Fast Speech Trap):\n"
        "    You hear: [il-z‿õ fɛ̃]   -> Transcribe in French: _________________________________________\n"
        "    You hear: [il-sõ fɛ̃]    -> Transcribe in French: _________________________________________"
    ]
    for d in drill_1_7:
        add_p(d, space_before=3, space_after=3)

    # MODULE 1D
    add_h2("Module 1D: \"Il y a\" & The Negation Trap")
    add_callout_box(
        "CORE SYNTACTIC MECHANIC: THE ARTICLE COLLAPSE",
        "• Affirmative: Il y a + [un / une / des / du / de la / de l'] + noun.\n"
        "• Interrogative: 'Est-ce qu'il y a... ?' or inverted 'Y a-t-il... ?'\n"
        "• THE FATAL NEGATION TRAP: Under negation (il n'y a pas...), indefinite articles (un, une, des) and partitive articles (du, de la, des) MANDATORILY COLLAPSE into 'DE' (or 'D\'' before vowels).\n"
        "  - Il y a un livre  ->  Il n'y a pas DE livre. (NEVER: *Il n'y a pas un livre)\n"
        "  - Il y a des erreurs  ->  Il n'y a pas D'erreur(s). (NEVER: *Il n'y a pas des erreurs)",
        "info"
    )

    add_p("Drill 1.8: 3-Way Structural Transformations (Items 1–6)", bold=True, color=SLATE_RGB, size=11, space_before=6)
    add_p("Given the affirmative base sentence, write both the complete Negative form and the Interrogative form.")

    drill_1_8 = [
        ("1. Affirmative: « Il y a un problème avec cette réservation. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________"),
        ("2. Affirmative: « Il y a une pharmacie de garde près de la gare. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________"),
        ("3. Affirmative: « Il y a des tables disponibles sur la terrasse. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________"),
        ("4. Affirmative: « Il y a un ascenseur en service dans cet hôtel. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________"),
        ("5. Affirmative: « Il y a des questions difficiles dans cet examen. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________"),
        ("6. Affirmative: « Il y a une place libre dans ce compartiment de train. »",
         "   Negative:      ____________________________________________________________________________",
         "   Interrogative: ____________________________________________________________________________")
    ]
    for aff, neg, inter in drill_1_8:
        add_p(aff, bold=True, space_before=3, space_after=1)
        add_p(neg, space_before=0, space_after=1)
        add_p(inter, space_before=0, space_after=3)

    add_p("Drill 1.9: The Article Collapse Elimination Drill (Items 7–12)", bold=True, color=SLATE_RGB, size=11, space_before=8)
    add_p("Fill in the blanks with the correct affirmative article ('un', 'une', 'des') or the negative particle ('de', 'd'').")

    drill_1_9 = [
        "7. Dans ce studio, il y a _________ balcon agréable, mais il n'y a pas _________ terrasse.",
        "8. Au marché ce matin, il y a _________ tomates fraîches, mais il n'y a pas _________ fraises.",
        "9. Est-ce qu'il y a _________ problème technique ? Non, soyez rassuré, il n'y a pas _________ problème.",
        "10. Sur cette page de code, il y a _________ erreurs de syntaxe, mais il n'y a pas _________ bogue critique.",
        "11. Dans ce village médiéval, il y a _________ boulangerie artisanale, mais il n'y a pas _________ supermarché.",
        "12. Sur son bureau d'architecte, il y a _________ ordinateurs récents, mais il n'y a pas _________ imprimante."
    ]
    for d in drill_1_9:
        add_p(d, space_before=2, space_after=3)

    # -------------------------------------------------------------
    # PART 2: INTEGRATED REAL-WORLD SCENARIOS
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("PART 2: INTEGRATED REAL-WORLD SCENARIOS (No English Crutches)")
    add_callout_box(
        "METHODOLOGICAL DESIGN: ZERO ENGLISH DRILLS",
        "These 20 scenarios simulate genuine communicative demands in Francophone environments. "
        "You must synthesize all 4 foundational pillars simultaneously: Register Calibration, Auxiliary Selection, "
        "The Sound Engine (liaisons & silent letters), and 'Il y a' Negation Collapses.",
        "info"
    )

    add_h2("Section 2A: Forensic Error-Correction Drills (Scenarios 1–10)")
    add_p("Each scenario below contains subtle, deliberate errors (register mismatch, auxiliary confusion, illegal liaisons, failure to collapse negation). "
          "Underline the errors, categorize the failure mode, and write the fully corrected French version.")

    err_scenarios = [
        ("Scenario 1: Addressing the counter staff at a Parisian boulangerie.",
         "Flawed text: « Bonjour monsieur ! Tu as des croissants chauds ? Non, désolé, il n'y a pas des croissants aujourd'hui. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Phonetics\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 2: Intake consultation at a medical clinic in Lyon.",
         "Flawed text: « Bonjour docteur. Je suis 32 ans et depuis ce matin, je suis très chaud et j'ai froid en même temps. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Phonetics\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 3: Two university students discussing weekend study plans.",
         "Flawed text: « Pierre et moi, demain on parlent du projet avec le professeur. On est très content de commencer. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Agreement/Ending   [  ] Phonetics\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 4: Inquiring about trains at Gare Saint-Lazare with an SNCF agent.",
         "Flawed text: « Pardon monsieur l'agent. Est-ce que il y a un train pour Rouen ? Non, il y a pas un train avant midi. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Elision\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 5: Restaurant host addressing a couple entering a dining room.",
         "Flawed text: « Bonsoir madame, bonsoir monsieur. Vous êtes faim ? Nous avons une belle table près de la fenêtre. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Phonetics\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 6: Discussing siblings during a casual conversation.",
         "Flawed text: « Mes deux frères sont 20 ans. En hiver, ils ont toujours très froid et ils parlent [pronounced -ɑ̃] vite. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Verbal Pronunciation\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 7: Starting an email to a senior partner at a law firm.",
         "Flawed text: « Salut Maître Renard ! Est-ce que tu as reçu les documents ? Il y a des questions urgentes. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Salutation\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 8: Tourist information desk inquiry on a Monday morning.",
         "Flawed text: « Est-ce qu'il y a des musées ouverts à Paris aujourd'hui ? Non, le lundi il n'y a pas des musées d'art. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Phonetics\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 9: Acoustic confusion in fast conversational speech.",
         "Flawed text: « Les enfants [il-sõ fɛ̃] (intended: they are hungry) et leurs parents [il-z‿õ fatige] (intended: they are tired). »",
         "Failure modes: [  ] Register   [  ] Auxiliary Collision   [  ] Acoustic / Liaison Inversion\n"
         "Corrected text: __________________________________________________________________________________"),
        ("Scenario 10: Hotel guest questioning a missing amenity at checkout.",
         "Flawed text: « Dans ma chambre, il n'y a pas un minibar, et mon collègue et [‿ liaison] un client attendent dehors. »",
         "Failure modes: [  ] Register   [  ] Auxiliary   [  ] Negation Article   [  ] Forbidden Liaison\n"
         "Corrected text: __________________________________________________________________________________")
    ]

    for title, flawed, resp in err_scenarios:
        add_p(title, bold=True, space_before=4, space_after=1)
        add_p(flawed, italic=True, space_before=0, space_after=1)
        add_p(resp, color=MUTED_RGB, space_before=0, space_after=4)

    add_h2("Section 2B: Contextual Micro-Dialogue Completions (Dialogues 11–20)")
    add_p("Complete the dialogue turns by conjugating the verbs, respecting social registers, collapsing articles, and maintaining phonetic precision.")

    dialogues = [
        ("Dialogue 11: Check-in at Hôtel de la Paix (Nice)\n"
         "Réceptionniste: « Bonjour madame. Vous (avoir) ______________ une réservation ? »\n"
         "Cliente: « Oui, au nom de Leclerc. Est-ce qu'il y a (un ascenseur) ______________ ? »\n"
         "Réceptionniste: « Oui, mais malheureusement aujourd'hui il n'y a pas (ascenseur) ______________ en service ; nous (être) ______________ en travaux. »"),
        
        ("Dialogue 12: Ordering at a Parisian Bistro\n"
         "Serveur: « Bonjour messieurs. Vous (être / avoir) ______________ faim ? Que désirez-vous ? »\n"
         "Client 1: « Nous (avoir) ______________ très soif pour commencer. Est-ce qu'il y a (de l'eau minérale) ______________ fraîche ? »\n"
         "Serveur: « Oui bien sûr. Et pour le plat du jour, il n'y a plus (poisson) ______________, mais il y a un excellent canard. »"),

        ("Dialogue 13: Lost in the Marais District (Paris)\n"
         "Touriste: « Pardon madame, excusez-moi de vous déranger. Est-ce que vous (avoir) ______________ l'heure ? »\n"
         "Parisienne âgée: « Oui, il (être) ______________ 16 heures 15. Vous (chercher) ______________ le métro ? »\n"
         "Touriste: « Oui, est-ce qu'il y a (une station) ______________ près d'ici ? »\n"
         "Parisienne: « Non, dans cette rue il n'y a pas (station) ______________, mais à 200 mètres il y a Saint-Paul. »"),

        ("Dialogue 14: Emergency Call to SOS Médecins\n"
         "Opérateur: « Bonjour monsieur. Quel (être) ______________ votre problème ? »\n"
         "Patient: « Mon fils de 5 ans (avoir) ______________ très chaud et il (avoir) ______________ 39 de fièvre. »\n"
         "Opérateur: « Est-ce qu'il y a (d'autres symptômes) ______________ comme des vomissements ? »\n"
         "Patient: « Non, il n'y a pas (autres symptômes) ______________, mais il (avoir) ______________ peur. »"),

        ("Dialogue 15: Friday Evening Planning Between Flatmates\n"
         "Lucas: « Antoine, ce soir on (aller) ______________ au cinéma ou on (rester) ______________ à l'appartement ? »\n"
         "Antoine: « Moi, je (avoir) ______________ sommeil et je (être) ______________ épuisé par ma semaine. »\n"
         "Lucas: « D'accord, alors on (commander) ______________ une pizza ? Est-ce qu'il y a (des boissons) ______________ au frigo ? »\n"
         "Antoine: « Non, il n'y a plus (boisson) ______________ fraîche, il faut descendre à l'épicerie. »"),

        ("Dialogue 16: Studio Apartment Inspection\n"
         "Propriétaire: « Entrez monsieur. Comme vous le voyez, il y a (une cuisine équipée) ______________. »\n"
         "Locataire: « C'est très lumineux. Est-ce qu'il y a (un lave-linge) ______________ ? »\n"
         "Propriétaire: « Non, dans ce studio il n'y a pas (lave-linge) ______________, mais il y a une laverie en face. »\n"
         "Locataire: « Très bien. Et pour le chauffage, vous (être) ______________ sûr qu'il n'y a pas (problème) ______________ en hiver ? »"),

        ("Dialogue 17: First Morning at a French Tech Company\n"
         "Manager: « Bienvenue Thomas ! Tu (être) ______________ prêt pour ton premier jour ? Ici, on (se tutoyer) ______________ tous. »\n"
         "Thomas: « Merci Marc ! Oui, je (avoir) ______________ hâte de commencer. Est-ce qu'il y a (des tâches) ______________ prioritaires ce matin ? »\n"
         "Manager: « Pour l'instant, il n'y a pas (tâche) ______________ urgente. On (aller) ______________ d'abord prendre un café. »"),

        ("Dialogue 18: At the Pharmacy Counter\n"
         "Pharmacienne: « Bonjour monsieur, vous (avoir) ______________ besoin d'un conseil ? »\n"
         "Client: « Oui, ma femme (avoir) ______________ un rhume carabiné et elle (avoir) ______________ très froid. »\n"
         "Pharmacienne: « Est-ce qu'elle (avoir) ______________ de la toux ? »\n"
         "Client: « Non, il n'y a pas (toux) ______________, juste des frissons et de la fatigue. »"),

        ("Dialogue 19: Sunday Lunch with Prospective French In-Laws\n"
         "Gendre potentiel: « Bonjour monsieur, bonjour madame. Vous (avoir) ______________ une maison magnifique. »\n"
         "Belle-mère: « Merci Julien ! Mets-toi à l'aise... enfin, mettez-vous à l'aise ! Vous (avoir) ______________ faim ? »\n"
         "Gendre potentiel: « Oui, nous (avoir) ______________ hâte de goûter votre cuisine. Est-ce qu'il y a (du vin rouge) ______________ pour accompagner ? »\n"
         "Beau-père: « Bien sûr ! Mais rassurez-vous, il n'y a pas (alcool fort) ______________ à table. »"),

        ("Dialogue 20: Lost Baggage Service at Charles de Gaulle Airport\n"
         "Passager: « Pardon madame, mon vol arrive de Montréal mais il n'y a pas (valise) ______________ sur le tapis. »\n"
         "Agente: « Vous (avoir) ______________ votre reçu d'enregistrement ? »\n"
         "Passager: « Oui, le voici. Est-ce qu'il y a (un vol suivant) ______________ aujourd'hui ? »\n"
         "Agente: « Malheureusement, non, il n'y a plus (autre vol) ______________ ce soir. Nous (être) ______________ désolés. »")
    ]

    for d_text in dialogues:
        lines = d_text.split("\n")
        add_p(lines[0], bold=True, space_before=4, space_after=1)
        for subline in lines[1:]:
            add_p(subline, space_before=0, space_after=1)
        add_p("", space_before=0, space_after=3)

    # -------------------------------------------------------------
    # PART 3: COMPREHENSIVE ANNOTATED ANSWER KEY
    # -------------------------------------------------------------
    doc.add_page_break()
    add_h1("PART 3: COMPREHENSIVE ANNOTATED ANSWER KEY")
    add_callout_box(
        "HOW TO USE THIS KEY: THE 'WHY YOU TRIPPED' (POURQUOI L'ERREUR ?) PROTOCOL",
        "Do not merely check if your answer is right or wrong. Every time your answer diverged from the key, "
        "read the accompanying 'Why You Tripped' analytical note. These notes diagnose the exact phonetic collision, "
        "syntactic rule, or sociopragmatic boundary that caused the error, locking in zero-revision intuition.",
        "alert"
    )

    # KEY: MODULE 1A
    add_h2("Answer Key — Module 1A: Pronoun Nuance & Social Calibration")
    add_p("1. VOUS (Singulier) — Commercial transaction in a shop with an adult stranger. French pragmatic norms strictly require 'vous' to establish professional distance and respect.\n"
          "2. TU — Solidarity register. University students in France horizontally address each other with 'tu' from day one.\n"
          "3. TU — Animals and pets are universally addressed with 'tu' (tutoyés).\n"
          "4. VOUS (Singulier) — Generational deference + neighborly polite distance. Default for elderly acquaintances.\n"
          "5. VOUS (Singulier) — Corporate hierarchy. In formal French corporate settings, junior employees address senior executives with 'vous' unless explicitly invited to tutoyer.\n"
          "6. VOUS (Singulier) — Representatives of state authority (police, gendarmes, judges) require mandatory 'vous'. Using 'tu' with police can be legally construed as 'outrage à agent'.\n"
          "7. VOUS (Pluriel) — Plural address. Even though all individuals are intimate friends, 2+ people ALWAYS require 'vous' (there is no plural 'tu' in modern French).\n"
          "8. VOUS (Singulier) — Professional business development. 'Vous' is mandatory to signal competence, boundaries, and formal reliability.\n"
          "9. TU — Children under adolescence (<12–14 years) are naturally addressed with 'tu' by all adults.\n"
          "10. VOUS (Pluriel) — Plural address + stranger deference. Group of 2 elderly visitors.")

    add_callout_box(
        "WHY YOU TRIPPED: THE 'PLURAL TU' ILLUSION",
        "Common learner error: Trying to find a plural form of 'tu' (like Spanish 'vosotros' or slang 'y'all'). In French, 'tu' only exists as a singular pronoun. The moment you speak to two or more individuals, you MUST use 'vous' regardless of how intimately you know them. Addressing a group of siblings or childhood friends requires 'vous' without creating any emotional coldness.",
        "alert"
    )

    add_p("11. mange | Meaning: Indefinite 'People / One in general' (Universal cultural practice). Agreement: N/A (General statement).\n"
          "12. est / fatigués | Meaning: Spoken 'Nous' (We). Verb is 3rd singular ('est'), but predicative adjective agrees with real plural subjects ('Marc et moi' = masculine plural -> 'fatigués').\n"
          "13. a | Meaning: Indefinite 'People / One in general' (Biological axiom). Verb agrees with singular 'on'.\n"
          "14. va / ravies | Meaning: Spoken 'Nous' (We). Verb agrees with singular 'on' ('va'), but predicative adjective agrees with the two female speakers ('Camille, Élodie et moi' = feminine plural -> 'ravies').\n"
          "15. doit | Meaning: Indefinite 'People / One in general' (Institutional regulation). Verb agrees with singular 'on'.")

    add_callout_box(
        "WHY YOU TRIPPED: THE HYBRID NATURE OF 'ON'",
        "Linguistic Trap: Learners often conjugate verbs in the plural after 'on' because they know it means 'we' (*on mangent). The rule is absolute: the verb following 'on' is ALWAYS 3rd person singular (identical to il/elle). However, in modern French, when 'on' clearly refers to specific individuals, predicative adjectives agree in gender and number with the real people: 'On est fatigués' (masc. pl.) or 'On est prêtes' (fem. pl.).",
        "alert"
    )

    # KEY: MODULE 1B
    add_h2("Answer Key — Module 1B: Être vs. Avoir (Conjugation & Idiomatic Collisions)")
    add_p("1. J'ai / je suis (Elision occurs with 'J'ai'; NEVER elide 'Je suis' -> *J'suis is non-standard slang).\n"
          "2. sommes / avons\n"
          "3. es / as\n"
          "4. ont / sont (Watch acoustic differentiation: [il-z‿õ] vs [il-sõ]).\n"
          "5. êtes / avez\n"
          "6. a / sont\n"
          "7. est / a\n"
          "8. ont (Idiom: avoir froid = to experience cold; English 'to be cold').\n"
          "9. a (Idiom: avoir X ans = to be X years old; English 'to be X years old').\n"
          "10. avons (Idiom: avoir soif = to be thirsty; English 'to be thirsty').\n"
          "11. as / a (Idiom: avoir tort / avoir raison = to be wrong / to be right).\n"
          "12. ont (Idiom: avoir sommeil = to be sleepy; English 'to be sleepy').\n"
          "13. as (Idiom: avoir peur = to be afraid; English 'to be afraid').\n"
          "14. est (state -> être) / a (cause/possession -> avoir).\n"
          "15. avez (avoir besoin de = to need) / êtes (être prêt = to be ready).")

    add_callout_box(
        "WHY YOU TRIPPED: THE ANGLOPHONE 'TO BE' TRAP (*JE SUIS 25 ANS)",
        "Why this happens: In English, age and internal temperature are treated as essential states of existence ('I am 25', 'I am cold'). In the Romance linguistic mindset, you do not embody coldness or numerical age as an ontological identity; you possess years of life that have accrued to you, and you experience cold as a temporary physical acquisition. Saying *« Je suis chaud » does not mean 'I am feeling warm'—it is idiomatic slang for being sexually aroused or enthusiastic. Always lock in: AVOIR chaud/froid/faim/soif/peur/sommeil.",
        "alert"
    )

    # KEY: MODULE 1C
    add_h2("Answer Key — Module 1C: Phonetics & The Spoken Engine")
    add_p("1. Silent letters: « Ils » (-s), « parlent » (-ent silent verbal marker), « tout » (-t), « le », « temps » (-p, -s), « avec » (c pronounced), « leurs » (-s), « petits » (-s), « enfants » (-s). Pronounced phonetically: [il parl tu lə tɑ̃ a-vɛk lœr pə-ti z‿ɑ̃-fɑ̃].\n"
          "2. Silent letters: « grand » (-d), « chat » (-t), « blanc » (-c), « dort » (-t), « sous » (-s), « lit » (-t), « bois » (-s). Note: 'lit' and 'bois' end in silent consonants.\n"
          "3. Silent letters: « attendons » (-s), « train » (-n is part of nasal vowel [ɛ̃]), « nuit » (-t), « grand » (-d), « froid » (-d).\n"
          "4. Silent letters: « Les » (-s), « deux » (-x), « vieux » (-x), « loups » (-p, -s), « gris » (-s), « courent » (-ent verbal marker), « vers » (-s), « bois » (-s), « épais » (-s).\n"
          "5. Silent letters: « aspect » (-c, -t), « projet » (-t), « est » (-s, -t), « trop » (-p), « suspect » (-c, -t pronounced in standard French as [sys-pɛkt] or [sys-pɛ]; strictly -ct is often retained in Latin roots except final -t), « et » (-t), « lourd » (-d).")

    add_callout_box(
        "WHY YOU TRIPPED: THE VERBAL '-ENT' DECEPTION",
        "Why learners make this mistake: In French nouns and adverbs like 'lent' (slow) or 'vraiment' (truly), the '-ent' ending forms the nasal vowel [ɑ̃]. Consequently, English speakers instinctively pronounce 'ils parlent' as *[il par-lɑ̃]. This is completely ungrammatical in French: the verbal 3rd person plural inflection '-ent' is an etymological fossil that is 100% SILENT. 'Ils parlent' sounds IDENTICAL to 'il parle' ([il parl]). The only way a French listener knows it is plural in speech is through context or a liaison with a following vowel.",
        "alert"
    )

    add_p("6. bon = [Nasal] ([bõ])  |  bonne = [Oral Vowel + Consonant] ([bɔn])\n"
          "7. fin = [Nasal] ([fɛ̃])  |  fine = [Oral Vowel + Consonant] ([fin])\n"
          "8. un = [Nasal] ([œ̃])  |  une = [Oral Vowel + Consonant] ([yn])\n"
          "9. plein = [Nasal] ([plɛ̃])  |  pleine = [Oral Vowel + Consonant] ([plɛn])\n"
          "10. cousin = [Nasal] ([ku-zɛ̃])  |  cousine = [Oral Vowel + Consonant] ([ku-zin])")

    add_p("11. a) Ils ‿ ont [z] (Mandatory liaison: subject pronoun + verb) | b) Ils sont ✗ [s] (No liaison; initial [s] of verb 'sont').\n"
          "12. a) un ‿ ami [n] (Mandatory liaison: determiner + noun) | b) Paul et ✗ un ami (FORBIDDEN LIAISON: liaison after 'et' is strictly forbidden).\n"
          "13. a) très ‿ élégant [z] (Mandatory liaison: monosyllabic adverb + adj) | b) soldat ✗ anglais (FORBIDDEN LIAISON: singular noun + adj).\n"
          "14. a) chez ‿ elle [z] (Mandatory liaison: preposition + pronoun) | b) vers ✗ onze heures (FORBIDDEN LIAISON: before 'onze' / 'onzième', treated as glottal boundary).\n"
          "15. [il-z‿õ fɛ̃] = « Ils ont faim » (They are hungry) | [il-sõ fɛ̃] = « Ils sont fins » (They are fine/delicate/clever). Notice the acoustic bridge: [z] belongs to AVOIR; [s] belongs to ÊTRE!")

    add_callout_box(
        "WHY YOU TRIPPED: THE FATAL 'ET' LIAISON BLUNDER",
        "Never make a liaison after 'ET'. In French phonology, 'et' (and) is a coordinating conjunction that marks a major structural boundary in speech. It is accompanied by a subtle glottal pause. Making a liaison with 'et' (*et-t-un ami) is considered an illiterate phonetic error in French. Always pronounce 'et' as an isolated oral vowel [e] followed by a clean break.",
        "alert"
    )

    # KEY: MODULE 1D
    add_h2("Answer Key — Module 1D: \"Il y a\" & The Negation Trap")
    add_p("1. Neg: « Il n'y a pas de problème avec cette réservation. » | Int: « Est-ce qu'il y a un problème avec cette réservation ? » (ou « Y a-t-il un problème... ? »)\n"
          "2. Neg: « Il n'y a pas de pharmacie de garde près de la gare. » | Int: « Est-ce qu'il y a une pharmacie de garde près de la gare ? »\n"
          "3. Neg: « Il n'y a pas de tables disponibles sur la terrasse. » | Int: « Est-ce qu'il y a des tables disponibles sur la terrasse ? »\n"
          "4. Neg: « Il n'y a pas d'ascenseur en service dans cet hôtel. » | Int: « Est-ce qu'il y a un ascenseur en service dans cet hôtel ? »\n"
          "5. Neg: « Il n'y a pas de questions difficiles dans cet examen. » | Int: « Est-ce qu'il y a des questions difficiles dans cet examen ? »\n"
          "6. Neg: « Il n'y a pas de place libre dans ce compartiment de train. » | Int: « Est-ce qu'il y a une place libre dans ce compartiment de train ? »")

    add_callout_box(
        "WHY YOU TRIPPED: THE INDEFINITE ARTICLE COLLAPSE",
        "In affirmative French, 'un', 'une', and 'des' indicate quantity (one, some). Under standard direct negation (ne... pas), quantity collapses to zero. In French syntax, zero quantity requires the partitive preposition 'DE' (or 'D\'' before a vowel). Saying *« Il n'y a pas des tables » sounds to a native speaker like 'There isn't a specific cluster of some tables.' The only grammatical structure is: « Il n'y a pas DE tables ».",
        "alert"
    )

    add_p("7. un / de\n"
          "8. des / de\n"
          "9. un / de\n"
          "10. des / de\n"
          "11. une / de\n"
          "12. des / d'")

    # KEY: PART 2
    add_h2("Answer Key — Part 2: Integrated Real-World Scenarios")
    add_p("Section 2A: Forensic Corrections (Scenarios 1–10)", bold=True, color=SLATE_RGB)
    
    p2_corrections = [
        ("Scenario 1", "Errors: Register ('Tu' -> 'Vous') and Negation article ('des' -> 'de').\n"
         "Correct version: « Bonjour monsieur ! Vous avez des croissants chauds ? Non, désolé, il n'y a pas de croissants aujourd'hui. »"),
        ("Scenario 2", "Errors: Auxiliary with age (*Je suis 32 ans -> J'ai 32 ans) and sensations (*je suis très chaud -> j'ai très chaud).\n"
         "Correct version: « Bonjour docteur. J'ai 32 ans et depuis ce matin, j'ai très chaud et j'ai froid en même temps. »"),
        ("Scenario 3", "Errors: Verbal agreement with 'on' (*on parlent -> on parle) and adjective agreement (*content -> contents).\n"
         "Correct version: « Pierre et moi, demain on parle du projet avec le professeur. On est très contents de commencer. »"),
        ("Scenario 4", "Errors: Elision before vowel (*est-ce que il y a -> est-ce qu'il y a), missing 'ne' in formal written standard, and negation article collapse (*pas un train -> pas de train).\n"
         "Correct version: « Pardon monsieur l'agent. Est-ce qu'il y a un train pour Rouen ? Non, il n'y a pas de train avant midi. »"),
        ("Scenario 5", "Errors: Auxiliary with hunger (*vous êtes faim -> vous avez faim).\n"
         "Correct version: « Bonsoir madame, bonsoir monsieur. Vous avez faim ? Nous avons une belle table près de la fenêtre. »"),
        ("Scenario 6", "Errors: Auxiliary with age (*sont 20 ans -> ont 20 ans) and verbal pronunciation (parlent must be pronounced [parl], never [par-lɑ̃]).\n"
         "Correct version: « Mes deux frères ont 20 ans. En hiver, ils ont toujours très froid et ils parlent lentement. »"),
        ("Scenario 7", "Errors: Inappropriate register with senior partner (*Salut / *tu -> Bonjour Maître / vous avez).\n"
         "Correct version: « Bonjour Maître Renard. Est-ce que vous avez reçu les documents ? Il y a des questions urgentes. »"),
        ("Scenario 8", "Errors: Negation article failure (*il n'y a pas des musées -> il n'y a pas de musées).\n"
         "Correct version: « Est-ce qu'il y a des musées ouverts à Paris aujourd'hui ? Non, le lundi il n'y a pas de musées d'art. »"),
        ("Scenario 9", "Errors: Liaison inversion. [il-sõ] is être ('they are'); [il-z‿õ] is avoir ('they have').\n"
         "Correct version: « Les enfants ont faim [il-z‿õ fɛ̃] et leurs parents sont très fatigués [il sõ trɛ fa-ti-ge]. »"),
        ("Scenario 10", "Errors: Negation collapse (*pas un minibar -> pas de minibar) and illegal liaison after 'et' (*et ‿ un client -> et ✗ un client).\n"
         "Correct version: « Dans ma chambre, il n'y a pas de minibar, et mon collègue et [pas de liaison] un client attendent dehors. »")
    ]
    for s_name, text in p2_corrections:
        add_p(f"{s_name}: {text}", space_before=3, space_after=3)

    add_p("Section 2B: Micro-Dialogue Solutions (Dialogues 11–20)", bold=True, color=SLATE_RGB, space_before=6)
    
    dialogue_answers = [
        "Dialogue 11: avez | un ascenseur | d'ascenseur | sommes",
        "Dialogue 12: avez (faim) | avons | de l'eau minérale | de poisson",
        "Dialogue 13: avez | est | cherchez | une station | de station",
        "Dialogue 14: est | a (très chaud) | a (39 de fièvre) | d'autres symptômes | d'autres symptômes | a (peur)",
        "Dialogue 15: va | reste | ai (sommeil) | suis (épuisé) | commande | des boissons | de boisson",
        "Dialogue 16: une cuisine équipée | un lave-linge | de lave-linge | êtes | de problème",
        "Dialogue 17: es (prêt) | se tutoie | ai (hâte) | des tâches | de tâche | va",
        "Dialogue 18: avez (besoin) | a (un rhume) | a (très froid) | a (de la toux) | de toux",
        "Dialogue 19: avez | avez (faim) | avons (hâte) | du vin rouge | d'alcool fort",
        "Dialogue 20: de valise | Avez | un vol suivant | d'autre vol | sommes (désolés)"
    ]
    for d_ans in dialogue_answers:
        add_p(d_ans, space_before=2, space_after=2)

    # Save DOCX
    doc.save(DOCX_PATH)
    print(f"Successfully generated DOCX at {DOCX_PATH}")

def create_pdf():
    # ReportLab document setup with custom NumberedCanvas
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
                self.setFillColor(colors.HexColor("#64748B"))
                # Running header
                self.drawString(54, letter[1] - 36, "French Foundations Practice Workbook  |  Zero-Revision System")
                self.setStrokeColor(colors.HexColor("#CBD5E1"))
                self.setLineWidth(0.5)
                self.line(54, letter[1] - 42, letter[0] - 54, letter[1] - 42)
                
                # Footer
                page_str = f"Page {self._pageNumber} of {page_count}"
                self.drawRightString(letter[0] - 54, 36, page_str)
                self.drawString(54, 36, "CEFR A1–A2 Active Mastery  •  Applied Linguistics & Instructional Design")
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
    
    # Custom styles
    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.white,
        alignment=1, # Center
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#E2E8F0'),
        alignment=1,
        spaceAfter=6
    )
    meta_style = ParagraphStyle(
        'CoverMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#94A3B8'),
        alignment=1
    )
    h1_style = ParagraphStyle(
        'DocH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=17,
        textColor=colors.HexColor('#1B365D'),
        spaceBefore=14,
        spaceAfter=4
    )
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11.5,
        leading=14,
        textColor=colors.HexColor('#4A607A'),
        spaceBefore=10,
        spaceAfter=4
    )
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0F172A'),
        spaceBefore=2,
        spaceAfter=3
    )
    body_bold = ParagraphStyle(
        'DocBodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    muted_style = ParagraphStyle(
        'DocMuted',
        parent=body_style,
        fontName='Helvetica',
        textColor=colors.HexColor('#475569')
    )
    callout_t_style = ParagraphStyle(
        'CalloutTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#1B365D'),
        spaceAfter=3
    )
    callout_b_style = ParagraphStyle(
        'CalloutBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1E293B')
    )
    alert_t_style = ParagraphStyle(
        'AlertTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor('#B45309'),
        spaceAfter=3
    )

    story = []

    def make_callout(title, body, is_alert=False):
        b_color = colors.HexColor('#B45309') if is_alert else colors.HexColor('#1B365D')
        bg_color = colors.HexColor('#FFFBEB') if is_alert else colors.HexColor('#F1F5F9')
        t_style = alert_t_style if is_alert else callout_t_style
        
        t_para = Paragraph(title, t_style)
        b_para = Paragraph(body.replace('\n', '<br/>'), callout_b_style)
        
        tbl = Table([[ [t_para, b_para] ]], colWidths=[letter[0] - 108])
        tbl.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_color),
            ('LINELEFT', (0,0), (0,0), 3.5, b_color),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 10),
            ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ]))
        return tbl

    # Cover Header
    cover_data = [[ [
        Paragraph("FRENCH FOUNDATIONS PRACTICE WORKBOOK", title_style),
        Paragraph("The Zero-Revision Applied Linguistics System: Muscle Memory, Acoustic Calibration & Register Mastery", subtitle_style),
        Paragraph("Comprehensive Active Practice  •  100% Non-Ambiguous Tasks  •  Annotated Analytical Answer Key", meta_style)
    ] ]]
    cover_table = Table(cover_data, colWidths=[letter[0] - 108])
    cover_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1B365D')),
        ('TOPPADDING', (0,0), (-1,-1), 16),
        ('BOTTOMPADDING', (0,0), (-1,-1), 16),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(cover_table)
    story.append(Spacer(1, 8))

    story.append(make_callout(
        "METHODOLOGICAL DESIGN: ZERO-REVISION MASTERY ARCHITECTURE",
        "This workbook is engineered using cognitive elimination tasks, contrastive analysis, and acoustic transcription drills. "
        "Standard workbooks test passive recognition, forcing learners to re-read grammar theory later. "
        "Here, every drill requires active production: calibrated register selections, physical silent letter recognition, "
        "liaison boundary marking, and negation article collapsing. Completing these drills embeds immediate linguistic intuition."
    ))
    story.append(Spacer(1, 10))

    # PART 1
    story.append(Paragraph("PART 1: TARGETED DIAGNOSTICS (Isolating the Mechanics)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1B365D'), spaceAfter=8))
    
    # Module 1A
    story.append(Paragraph("Module 1A: Pronoun Nuance & Social Calibration (\"Tu\" vs. \"Vous\" & \"On\")", h2_style))
    story.append(make_callout(
        "CORE MECHANIC: REGISTRATION & SEMANTIC POLARITY",
        "• TU: Solidarity, horizontal intimacy, children (<12), pets, fellow students.<br/>"
        "• VOUS (Singular): Deference, vertical hierarchy, strangers, professionals, commercial transactions.<br/>"
        "• VOUS (Plural): Any group of 2+ individuals, regardless of intimacy.<br/>"
        "• ON: Grammatically 3rd person singular (verb ends like il/elle). Semantically: (1) Informal spoken 'we' (nous) where adjectives agree with the real subjects; (2) Universal indefinite 'people in general / one' where adjectives remain masculine singular."
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Drill 1.1: Pragmatic Register Classification (Scenarios 1–10)</b>", body_bold))
    story.append(Paragraph("Mark the required address pronoun and state the sociolinguistic justification.", body_style))
    
    scenarios_data = [
        ("1. You walk into a Parisian boulangerie at 7:30 AM to buy a baguette from the baker.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("2. You meet a 20-year-old student sitting next to you on your first day at the Sorbonne.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("3. You are petting an energetic Golden Retriever puppy in the Jardin des Tuileries.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("4. You meet your 76-year-old neighbor, Madame Mercier, collecting mail in the lobby.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("5. You are in your annual performance evaluation with your corporate department director.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("6. You ask an armed police officer (agent de police) near the Gare du Nord for directions.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("7. You arrive at a terrace table where your 4 closest childhood friends are waiting.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("8. You conduct an introductory discovery video call with a prospective corporate client.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("9. You comfort an 8-year-old lost child crying in the Galeries Lafayette department store.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________"),
        ("10. Two elderly tourists stop you on the Pont Neuf asking in French for the metro entrance.",
         "[  ] Tu       [  ] Vous (Singulier)       [  ] Vous (Pluriel)",
         "Justification: ____________________________________________________________________")
    ]
    for s_title, opts, just in scenarios_data:
        story.append(Paragraph(f"<b>{s_title}</b>", body_style))
        story.append(Paragraph(opts, body_style))
        story.append(Paragraph(just, muted_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.2: The Meaning-Shift & Agreement of \"On\" (Items 11–15)</b>", body_bold))
    on_pdf_data = [
        "11. En France, on (manger / mangent) ______________ souvent du fromage avant le dessert.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Agreement check: ___________________________________________________________________",
        "12. Marc et moi, ce soir on (être) ______________ très (fatigué / fatigués / fatiguée) ______________.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Agreement check: ___________________________________________________________________",
        "13. Quand on (avoir) ______________ peur dans le noir, le rythme cardiaque s'accélère.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Agreement check: ___________________________________________________________________",
        "14. Avec Camille et Élodie, demain on (aller) ______________ à la plage ; on est (ravi / ravis / ravies) ______________.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Agreement check: ___________________________________________________________________",
        "15. Dans cette bibliothèque nationale, on ne (devoir / doivent) ______________ pas parler à voix haute.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Meaning: [  ] Spoken 'Nous' (We)   [  ] Indefinite 'People / One in general'<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Agreement check: ___________________________________________________________________"
    ]
    for item in on_pdf_data:
        story.append(Paragraph(item, body_style))
        story.append(Spacer(1, 2))

    # Module 1B
    story.append(Spacer(1, 6))
    story.append(Paragraph("Module 1B: Être vs. Avoir (Conjugation & Idiomatic Collisions)", h2_style))
    story.append(make_callout(
        "CORE MECHANIC: ELISION & FALSE-FRIEND IDIOMS",
        "• Elision: 'Je' elides to 'J\'' before vowels only with avoir (J'ai) and vowel verbs. NEVER with être: 'Je suis'.<br/>"
        "• The English False-Friend Trap: French expresses somatic sensations and age via AVOIR (possession), not ÊTRE (identity):<br/>"
        "  - avoir X ans (to be X years old)<br/>"
        "  - avoir faim / soif (to be hungry / thirsty)<br/>"
        "  - avoir chaud / froid (to be hot / cold)<br/>"
        "  - avoir peur / sommeil (to be afraid / sleepy)<br/>"
        "  - avoir raison / tort (to be right / wrong)<br/>"
        "  - avoir besoin de / envie de (to need / to feel like)"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.3: Speed Paradigm & Elision Precision (Items 1–7)</b>", body_bold))
    drill_1_3_pdf = [
        "1. (Je + avoir) ______________ 28 ans et (je + être) ______________ ingénieur à Lyon.",
        "2. Nous (être) ______________ très occupés aujourd'hui, mais nous (avoir) ______________ le temps d'écouter.",
        "3. Tu (être) ______________ prêt pour la présentation, ou tu (avoir) ______________ encore des doutes ?",
        "4. Ils (avoir) ______________ un nouvel appartement au centre-ville et ils (être) ______________ ravis.",
        "5. Vous (être) ______________ en avance, mais vous (avoir) ______________ tout votre matériel avec vous.",
        "6. Elle (avoir) ______________ deux sœurs qui (être) ______________ chirurgiennes à l'hôpital Pasteur.",
        "7. On (être) ______________ lundi matin et on (avoir) ______________ déjà une réunion importante."
    ]
    for d in drill_1_3_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.4: False-Friend Idiomatic Collision Drills (Items 8–15)</b>", body_bold))
    drill_1_4_pdf = [
        "8. Pendant la tempête de neige, les randonneurs ______________ extrêmement froid aux mains.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "9. Antoine a fêté son anniversaire hier : il ______________ maintenant 35 ans.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "10. Après 25 kilomètres de marche sous le soleil de midi, nous ______________ une soif terrible.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "11. Tu as recompté les totaux ? Je pense que tu ______________ tort et que le comptable ______________ raison.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "12. Il est deux heures du matin ; les enfants ne tiennent plus debout, ils ______________ sommeil.<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "13. Pourquoi fermes-tu la porte à clé ? Est-ce que tu ______________ peur du noir ?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Idiom check: ________________________________________________________________________",
        "14. Ce matin, elle ______________ épuisée (state) parce qu'elle ______________ beaucoup de soucis (possession).<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Contrast check: _____________________________________________________________________",
        "15. Est-ce que vous ______________ besoin d'une pause ou est-ce que vous ______________ prêts à continuer ?<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Contrast check: _____________________________________________________________________"
    ]
    for d in drill_1_4_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 2))

    # Module 1C
    story.append(Spacer(1, 6))
    story.append(Paragraph("Module 1C: The French Sound Engine & Phonetics", h2_style))
    story.append(make_callout(
        "CORE PHONETIC MECHANICS: THE SPOKEN ENGINE",
        "• CaReFuL Rule: C, R, F, L generally PRONOUNCED at word ends (sac, hiver, chef, ciel). D, S, T, X, P, G are SILENT (grand, chats, lit, deux, trop).<br/>"
        "• Plural Verb Trap: 3rd person plural verb ending '-ent' (ils parlent) is 100% SILENT ([parl]). It is NEVER a nasal vowel [-ɑ̃]!<br/>"
        "• Nasal Vowels: Vowel + single N/M at word end / before consonant = Nasal (bon, fin, un). Double N/M destroys nasalization (bonne, fine, une).<br/>"
        "• Liaisons: Mandatory ‿ with [z], [t], [n]. 'Ils ont' = [il-z‿õ]. 'Ils sont' = [il-sõ]. Liaison after 'ET' is CATEGORICALLY FORBIDDEN."
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.5: Silent Consonant Striking Radar (Sentences 1–5)</b>", body_bold))
    drill_1_5_pdf = [
        "1. « Ils parlent tout le temps avec leurs petits enfants. »<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Silent letters/endings: ________________________________________________________________",
        "2. « Le grand chat blanc dort sous le lit en bois. »<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Silent letters/endings: ________________________________________________________________",
        "3. « Nous attendons le train de nuit dans un grand froid. »<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Silent letters/endings: ________________________________________________________________",
        "4. « Les deux vieux loups gris courent vers le bois épais. »<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Silent letters/endings: ________________________________________________________________",
        "5. « Cet aspect du projet est trop suspect et très lourd. »<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Silent letters/endings: ________________________________________________________________"
    ]
    for d in drill_1_5_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.6: Nasal vs. Oral Minimal Pair Discrimination (Items 6–10)</b>", body_bold))
    drill_1_6_pdf = [
        "6. bon  [  ] Nasal  [  ] Oral         vs.    bonne   [  ] Nasal  [  ] Oral",
        "7. fin  [  ] Nasal  [  ] Oral         vs.    fine    [  ] Nasal  [  ] Oral",
        "8. un   [  ] Nasal  [  ] Oral         vs.    une     [  ] Nasal  [  ] Oral",
        "9. plein [  ] Nasal  [  ] Oral        vs.    pleine  [  ] Nasal  [  ] Oral",
        "10. cousin [  ] Nasal  [  ] Oral      vs.    cousine [  ] Nasal  [  ] Oral"
    ]
    for d in drill_1_6_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.7: The Liaison Radar: Mandatory (‿) vs. Forbidden (✗) (Items 11–15)</b>", body_bold))
    drill_1_7_pdf = [
        "11. a) « Ils ___ ont vingt ans. »  Mark: [ ‿ / ✗ ]  Sound: [ ___ ]  |  b) « Ils ___ sont calmes. »  Mark: [ ‿ / ✗ ]",
        "12. a) « C'est un ___ ami fidèle. » Mark: [ ‿ / ✗ ]  Sound: [ ___ ]  |  b) « Paul et ___ un ami. »  Mark: [ ‿ / ✗ ]",
        "13. a) « Il est très ___ élégant. »  Mark: [ ‿ / ✗ ]  Sound: [ ___ ]  |  b) « Un soldat ___ anglais. » Mark: [ ‿ / ✗ ]",
        "14. a) « Elle reste chez ___ elle. » Mark: [ ‿ / ✗ ]  Sound: [ ___ ]  |  b) « Vers ___ onze heures. » Mark: [ ‿ / ✗ ]",
        "15. Acoustic Transcription Trap:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Hear: [il-z‿õ fɛ̃]  -> French: ____________________________________________________<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Hear: [il-sõ fɛ̃]   -> French: ____________________________________________________"
    ]
    for d in drill_1_7_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 2))

    # Module 1D
    story.append(Spacer(1, 6))
    story.append(Paragraph("Module 1D: \"Il y a\" & The Negation Trap", h2_style))
    story.append(make_callout(
        "CORE SYNTACTIC MECHANIC: THE ARTICLE COLLAPSE",
        "• Affirmative: Il y a + [un / une / des / du / de la] + noun.<br/>"
        "• THE FATAL NEGATION TRAP: Under negation (il n'y a pas...), indefinite/partitive articles MANDATORILY COLLAPSE into 'DE' (or 'D\'' before vowels).<br/>"
        "  - Il y a un livre  ->  Il n'y a pas DE livre. (NEVER: *Il n'y a pas un livre)<br/>"
        "  - Il y a des erreurs  ->  Il n'y a pas D'erreur(s). (NEVER: *Il n'y a pas des erreurs)"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.8: 3-Way Structural Transformations (Items 1–6)</b>", body_bold))
    drill_1_8_pdf = [
        ("1. Affirmative: « Il y a un problème avec cette réservation. »",
         "Negative: __________________________________ | Interrogative: __________________________________"),
        ("2. Affirmative: « Il y a une pharmacie de garde près de la gare. »",
         "Negative: __________________________________ | Interrogative: __________________________________"),
        ("3. Affirmative: « Il y a des tables disponibles sur la terrasse. »",
         "Negative: __________________________________ | Interrogative: __________________________________"),
        ("4. Affirmative: « Il y a un ascenseur en service dans cet hôtel. »",
         "Negative: __________________________________ | Interrogative: __________________________________"),
        ("5. Affirmative: « Il y a des questions difficiles dans cet examen. »",
         "Negative: __________________________________ | Interrogative: __________________________________"),
        ("6. Affirmative: « Il y a une place libre dans ce compartiment de train. »",
         "Negative: __________________________________ | Interrogative: __________________________________")
    ]
    for aff, resp in drill_1_8_pdf:
        story.append(Paragraph(f"<b>{aff}</b>", body_style))
        story.append(Paragraph(resp, muted_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Drill 1.9: The Article Collapse Elimination Drill (Items 7–12)</b>", body_bold))
    drill_1_9_pdf = [
        "7. Dans ce studio, il y a _________ balcon agréable, mais il n'y a pas _________ terrasse.",
        "8. Au marché ce matin, il y a _________ tomates fraîches, mais il n'y a pas _________ fraises.",
        "9. Est-ce qu'il y a _________ problème technique ? Non, soyez rassuré, il n'y a pas _________ problème.",
        "10. Sur cette page de code, il y a _________ erreurs de syntaxe, mais il n'y a pas _________ bogue critique.",
        "11. Dans ce village médiéval, il y a _________ boulangerie artisanale, mais il n'y a pas _________ supermarché.",
        "12. Sur son bureau d'architecte, il y a _________ ordinateurs récents, mais il n'y a pas _________ imprimante."
    ]
    for d in drill_1_9_pdf:
        story.append(Paragraph(d, body_style))
        story.append(Spacer(1, 1.5))

    # PART 2
    story.append(PageBreak())
    story.append(Paragraph("PART 2: INTEGRATED REAL-WORLD SCENARIOS (No English Crutches)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1B365D'), spaceAfter=8))
    story.append(make_callout(
        "METHODOLOGICAL DESIGN: ZERO ENGLISH DRILLS",
        "These 20 communicative scenarios synthesize all 4 foundational pillars: Register Calibration, Auxiliary Selection, "
        "The Sound Engine (liaisons & silent letters), and 'Il y a' Negation Collapses."
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Section 2A: Forensic Error-Correction Drills (Scenarios 1–10)", h2_style))
    story.append(Paragraph("Underline the errors, categorize failure modes, and write the fully corrected French version.", body_style))
    
    err_pdf = [
        ("Scenario 1: Counter staff at a Parisian boulangerie.",
         "Flawed: « Bonjour monsieur ! Tu as des croissants chauds ? Non, désolé, il n'y a pas des croissants aujourd'hui. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 2: Intake consultation at a medical clinic in Lyon.",
         "Flawed: « Bonjour docteur. Je suis 32 ans et depuis ce matin, je suis très chaud et j'ai froid en même temps. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 3: Two university students discussing weekend study plans.",
         "Flawed: « Pierre et moi, demain on parlent du projet avec le professeur. On est très content de commencer. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 4: Inquiring about trains at Gare Saint-Lazare with an SNCF agent.",
         "Flawed: « Pardon monsieur l'agent. Est-ce que il y a un train pour Rouen ? Non, il y a pas un train avant midi. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 5: Restaurant host addressing a dining couple.",
         "Flawed: « Bonsoir madame, bonsoir monsieur. Vous êtes faim ? Nous avons une belle table près de la fenêtre. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 6: Discussing siblings during a casual conversation.",
         "Flawed: « Mes deux frères sont 20 ans. En hiver, ils ont toujours très froid et ils parlent [pronounced -ɑ̃] vite. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 7: Starting an email to a senior partner at a law firm.",
         "Flawed: « Salut Maître Renard ! Est-ce que tu as reçu les documents ? Il y a des questions urgentes. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 8: Tourist information desk inquiry on a Monday morning.",
         "Flawed: « Est-ce qu'il y a des musées ouverts à Paris aujourd'hui ? Non, le lundi il n'y a pas des musées d'art. »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 9: Acoustic confusion in fast conversational speech.",
         "Flawed: « Les enfants [il-sõ fɛ̃] (intended: hungry) et leurs parents [il-z‿õ fatige] (intended: tired). »",
         "Correct: __________________________________________________________________________________"),
        ("Scenario 10: Hotel guest questioning a missing amenity at checkout.",
         "Flawed: « Dans ma chambre, il n'y a pas un minibar, et mon collègue et [‿ liaison] un client attendent dehors. »",
         "Correct: __________________________________________________________________________________")
    ]
    for s_title, flawed, corr in err_pdf:
        story.append(Paragraph(f"<b>{s_title}</b>", body_style))
        story.append(Paragraph(f"<i>{flawed}</i>", muted_style))
        story.append(Paragraph(corr, muted_style))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Section 2B: Contextual Micro-Dialogue Completions (Dialogues 11–20)", h2_style))
    dialogues_pdf = [
        ("Dialogue 11: Check-in at Hôtel de la Paix (Nice)",
         "Réceptionniste: « Bonjour madame. Vous (avoir) ______________ une réservation ? »<br/>"
         "Cliente: « Oui, au nom de Leclerc. Est-ce qu'il y a (un ascenseur) ______________ ? »<br/>"
         "Réceptionniste: « Oui, mais malheureusement aujourd'hui il n'y a pas (ascenseur) ______________ en service ; nous (être) ______________ en travaux. »"),
        ("Dialogue 12: Ordering at a Parisian Bistro",
         "Serveur: « Bonjour messieurs. Vous (être / avoir) ______________ faim ? Que désirez-vous ? »<br/>"
         "Client 1: « Nous (avoir) ______________ très soif pour commencer. Est-ce qu'il y a (de l'eau minérale) ______________ fraîche ? »<br/>"
         "Serveur: « Oui bien sûr. Et pour le plat du jour, il n'y a plus (poisson) ______________, mais il y a un excellent canard. »"),
        ("Dialogue 13: Lost in the Marais District (Paris)",
         "Touriste: « Pardon madame, excusez-moi de vous déranger. Est-ce que vous (avoir) ______________ l'heure ? »<br/>"
         "Parisienne âgée: « Oui, il (être) ______________ 16 heures 15. Vous (chercher) ______________ le métro ? »<br/>"
         "Touriste: « Oui, est-ce qu'il y a (une station) ______________ près d'ici ? »<br/>"
         "Parisienne: « Non, dans cette rue il n'y a pas (station) ______________, mais à 200 mètres il y a Saint-Paul. »"),
        ("Dialogue 14: Emergency Call to SOS Médecins",
         "Opérateur: « Bonjour monsieur. Quel (être) ______________ votre problème ? »<br/>"
         "Patient: « Mon fils de 5 ans (avoir) ______________ très chaud et il (avoir) ______________ 39 de fièvre. »<br/>"
         "Opérateur: « Est-ce qu'il y a (d'autres symptômes) ______________ comme des vomissements ? »<br/>"
         "Patient: « Non, il n'y a pas (autres symptômes) ______________, mais il (avoir) ______________ peur. »"),
        ("Dialogue 15: Friday Evening Planning Between Flatmates",
         "Lucas: « Antoine, ce soir on (aller) ______________ au cinéma ou on (rester) ______________ à l'appartement ? »<br/>"
         "Antoine: « Moi, je (avoir) ______________ sommeil et je (être) ______________ épuisé par ma semaine. »<br/>"
         "Lucas: « D'accord, alors on (commander) ______________ une pizza ? Est-ce qu'il y a (des boissons) ______________ au frigo ? »<br/>"
         "Antoine: « Non, il n'y a plus (boisson) ______________ fraîche, il faut descendre à l'épicerie. »"),
        ("Dialogue 16: Studio Apartment Inspection",
         "Propriétaire: « Entrez monsieur. Comme vous le voyez, il y a (une cuisine équipée) ______________. »<br/>"
         "Locataire: « C'est très lumineux. Est-ce qu'il y a (un lave-linge) ______________ ? »<br/>"
         "Propriétaire: « Non, dans ce studio il n'y a pas (lave-linge) ______________, mais il y a une laverie en face. »<br/>"
         "Locataire: « Très bien. Et pour le chauffage, vous (être) ______________ sûr qu'il n'y a pas (problème) ______________ en hiver ? »"),
        ("Dialogue 17: First Morning at a French Tech Company",
         "Manager: « Bienvenue Thomas ! Tu (être) ______________ prêt pour ton premier jour ? Ici, on (se tutoyer) ______________ tous. »<br/>"
         "Thomas: « Merci Marc ! Oui, je (avoir) ______________ hâte de commencer. Est-ce qu'il y a (des tâches) ______________ prioritaires ce matin ? »<br/>"
         "Manager: « Pour l'instant, il n'y a pas (tâche) ______________ urgente. On (aller) ______________ d'abord prendre un café. »"),
        ("Dialogue 18: At the Pharmacy Counter",
         "Pharmacienne: « Bonjour monsieur, vous (avoir) ______________ besoin d'un conseil ? »<br/>"
         "Client: « Oui, ma femme (avoir) ______________ un rhume carabiné et elle (avoir) ______________ très froid. »<br/>"
         "Pharmacienne: « Est-ce qu'elle (avoir) ______________ de la toux ? »<br/>"
         "Client: « Non, il n'y a pas (toux) ______________, juste des frissons et de la fatigue. »"),
        ("Dialogue 19: Sunday Lunch with Prospective French In-Laws",
         "Gendre potentiel: « Bonjour monsieur, bonjour madame. Vous (avoir) ______________ une maison magnifique. »<br/>"
         "Belle-mère: « Merci Julien ! Mets-toi à l'aise... enfin, mettez-vous à l'aise ! Vous (avoir) ______________ faim ? »<br/>"
         "Gendre potentiel: « Oui, nous (avoir) ______________ hâte de goûter votre cuisine. Est-ce qu'il y a (du vin rouge) ______________ ? »<br/>"
         "Beau-père: « Bien sûr ! Mais rassurez-vous, il n'y a pas (alcool fort) ______________ à table. »"),
        ("Dialogue 20: Lost Baggage Service at Charles de Gaulle Airport",
         "Passager: « Pardon madame, mon vol arrive de Montréal mais il n'y a pas (valise) ______________ sur le tapis. »<br/>"
         "Agente: « Vous (avoir) ______________ votre reçu d'enregistrement ? »<br/>"
         "Passager: « Oui, le voici. Est-ce qu'il y a (un vol suivant) ______________ aujourd'hui ? »<br/>"
         "Agente: « Malheureusement, non, il n'y a plus (autre vol) ______________ ce soir. Nous (être) ______________ désolés. »")
    ]
    for d_title, d_turns in dialogues_pdf:
        story.append(Paragraph(f"<b>{d_title}</b>", body_style))
        story.append(Paragraph(d_turns, body_style))
        story.append(Spacer(1, 2))

    # PART 3: ANSWER KEY
    story.append(PageBreak())
    story.append(Paragraph("PART 3: COMPREHENSIVE ANNOTATED ANSWER KEY", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1B365D'), spaceAfter=8))
    story.append(make_callout(
        "HOW TO USE THIS KEY: THE 'WHY YOU TRIPPED' PROTOCOL",
        "Review every divergent answer against the analytical callouts below. "
        "These diagnose the exact phonetic collision, syntactic rule, or sociopragmatic boundary behind each pitfall.",
        is_alert=True
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Answer Key — Module 1A: Pronoun Nuance & Social Calibration", h2_style))
    story.append(Paragraph("1. VOUS (Singulier) — Commercial transaction in a shop with an adult stranger. French pragmatic norms strictly require 'vous' to establish professional distance and respect.<br/>"
                           "2. TU — Solidarity register. University students in France horizontally address each other with 'tu' from day one.<br/>"
                           "3. TU — Animals and pets are universally addressed with 'tu' (tutoyés).<br/>"
                           "4. VOUS (Singulier) — Generational deference + neighborly polite distance. Default for elderly acquaintances.<br/>"
                           "5. VOUS (Singulier) — Corporate hierarchy. In formal French corporate settings, junior employees address senior executives with 'vous' unless explicitly invited to tutoyer.<br/>"
                           "6. VOUS (Singulier) — Representatives of state authority (police, gendarmes, judges) require mandatory 'vous'. Using 'tu' with police can be legally construed as 'outrage à agent'.<br/>"
                           "7. VOUS (Pluriel) — Plural address. Even though all individuals are intimate friends, 2+ people ALWAYS require 'vous' (there is no plural 'tu' in modern French).<br/>"
                           "8. VOUS (Singulier) — Professional business development. 'Vous' is mandatory to signal competence, boundaries, and formal reliability.<br/>"
                           "9. TU — Children under adolescence (<12–14 years) are naturally addressed with 'tu' by all adults.<br/>"
                           "10. VOUS (Pluriel) — Plural address + stranger deference. Group of 2 elderly visitors.", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE 'PLURAL TU' ILLUSION",
        "Common learner error: Trying to find a plural form of 'tu' (like Spanish 'vosotros' or slang 'y'all'). In French, 'tu' only exists as a singular pronoun. The moment you speak to two or more individuals, you MUST use 'vous' regardless of how intimately you know them. Addressing a group of siblings or childhood friends requires 'vous' without creating any emotional coldness.",
        is_alert=True
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("11. mange | Meaning: Indefinite 'People / One in general' (Universal cultural practice). Agreement: N/A.<br/>"
                           "12. est / fatigués | Meaning: Spoken 'Nous' (We). Verb is 3rd singular ('est'), but predicative adjective agrees with real plural subjects ('Marc et moi' = masculine plural -> 'fatigués').<br/>"
                           "13. a | Meaning: Indefinite 'People / One in general' (Biological axiom). Verb agrees with singular 'on'.<br/>"
                           "14. va / ravies | Meaning: Spoken 'Nous' (We). Verb agrees with singular 'on' ('va'), but predicative adjective agrees with female speakers ('Camille, Élodie et moi' = feminine plural -> 'ravies').<br/>"
                           "15. doit | Meaning: Indefinite 'People / One in general' (Institutional regulation). Verb agrees with singular 'on'.", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE HYBRID NATURE OF 'ON'",
        "Linguistic Trap: Learners often conjugate verbs in the plural after 'on' because they know it means 'we' (*on mangent). The rule is absolute: the verb following 'on' is ALWAYS 3rd person singular (identical to il/elle). However, when 'on' refers to specific individuals, predicative adjectives agree in gender and number with the real subjects: 'On est fatigués' (masc. pl.) or 'On est prêtes' (fem. pl.).",
        is_alert=True
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Answer Key — Module 1B: Être vs. Avoir (Conjugation & Idiomatic Collisions)", h2_style))
    story.append(Paragraph("1. J'ai / je suis (Elision with J'ai; never elide 'Je suis' in standard French).<br/>"
                           "2. sommes / avons<br/>"
                           "3. es / as<br/>"
                           "4. ont / sont (Acoustic contrast: [il-z‿õ] vs [il-sõ]).<br/>"
                           "5. êtes / avez<br/>"
                           "6. a / sont<br/>"
                           "7. est / a<br/>"
                           "8. ont (Idiom: avoir froid = to experience cold; English 'to be cold').<br/>"
                           "9. a (Idiom: avoir X ans = to be X years old; English 'to be X years old').<br/>"
                           "10. avons (Idiom: avoir soif = to be thirsty; English 'to be thirsty').<br/>"
                           "11. as / a (Idiom: avoir tort / avoir raison = to be wrong / to be right).<br/>"
                           "12. ont (Idiom: avoir sommeil = to be sleepy; English 'to be sleepy').<br/>"
                           "13. as (Idiom: avoir peur = to be afraid; English 'to be afraid').<br/>"
                           "14. est (state -> être) / a (cause/possession -> avoir).<br/>"
                           "15. avez (avoir besoin de = to need) / êtes (être prêt = to be ready).", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE ANGLOPHONE 'TO BE' TRAP (*JE SUIS 25 ANS)",
        "Why this happens: In English, age and internal temperature are treated as essential states of existence ('I am 25', 'I am cold'). In French, you possess years of life accrued, and you experience temperature as an external physical acquisition. Saying *« Je suis chaud » is colloquial slang for sexual arousal or excitement. Always remember: AVOIR chaud/froid/faim/soif/peur/sommeil.",
        is_alert=True
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Answer Key — Module 1C: Phonetics & The Spoken Engine", h2_style))
    story.append(Paragraph("1. Silent letters: « Ils » (-s), « parlent » (-ent verbal marker), « tout » (-t), « temps » (-p, -s), « leurs » (-s), « petits » (-s), « enfants » (-s). Pronounced: [il parl tu lə tɑ̃ a-vɛk lœr pə-ti z‿ɑ̃-fɑ̃].<br/>"
                           "2. Silent letters: « grand » (-d), « chat » (-t), « blanc » (-c), « dort » (-t), « sous » (-s), « lit » (-t), « bois » (-s).<br/>"
                           "3. Silent letters: « attendons » (-s), « train » (-n in nasal [ɛ̃]), « nuit » (-t), « grand » (-d), « froid » (-d).<br/>"
                           "4. Silent letters: « Les » (-s), « deux » (-x), « vieux » (-x), « loups » (-p, -s), « gris » (-s), « courent » (-ent verbal marker), « vers » (-s), « bois » (-s), « épais » (-s).<br/>"
                           "5. Silent letters: « aspect » (-c, -t), « projet » (-t), « est » (-s, -t), « trop » (-p), « et » (-t), « lourd » (-d).", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE VERBAL '-ENT' DECEPTION",
        "Why learners make this mistake: In French nouns/adverbs like 'lent' (slow) or 'vraiment' (truly), '-ent' forms the nasal vowel [ɑ̃]. Consequently, English speakers instinctively pronounce 'ils parlent' as *[il par-lɑ̃]. This is ungrammatical: the verbal 3rd person plural inflection '-ent' is an etymological fossil that is 100% SILENT. 'Ils parlent' sounds IDENTICAL to 'il parle' ([il parl]).",
        is_alert=True
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("6. bon = [Nasal] ([bõ]) | bonne = [Oral] ([bɔn])<br/>"
                           "7. fin = [Nasal] ([fɛ̃]) | fine = [Oral] ([fin])<br/>"
                           "8. un = [Nasal] ([œ̃]) | une = [Oral] ([yn])<br/>"
                           "9. plein = [Nasal] ([plɛ̃]) | pleine = [Oral] ([plɛn])<br/>"
                           "10. cousin = [Nasal] ([ku-zɛ̃]) | cousine = [Oral] ([ku-zin])", body_style))
    story.append(Paragraph("11. a) Ils ‿ ont [z] (Mandatory: pronoun + verb) | b) Ils sont ✗ [s] (No liaison; initial [s] of 'sont').<br/>"
                           "12. a) un ‿ ami [n] (Mandatory: determiner + noun) | b) Paul et ✗ un ami (FORBIDDEN LIAISON: never make a liaison after 'et').<br/>"
                           "13. a) très ‿ élégant [z] (Mandatory: adverb + adj) | b) soldat ✗ anglais (FORBIDDEN LIAISON: singular noun + adj).<br/>"
                           "14. a) chez ‿ elle [z] (Mandatory: preposition + pronoun) | b) vers ✗ onze heures (FORBIDDEN LIAISON: before 'onze').<br/>"
                           "15. [il-z‿õ fɛ̃] = « Ils ont faim » (They are hungry) | [il-sõ fɛ̃] = « Ils sont fins » (They are fine/delicate).", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE FATAL 'ET' LIAISON BLUNDER",
        "Never make a liaison after 'ET'. In French phonology, 'et' (and) is a coordinating conjunction marking a structural boundary accompanied by a glottal pause. Making a liaison with 'et' (*et-t-un ami) is considered an illiterate phonetic error. Pronounce 'et' as an isolated oral vowel [e] followed by a clean break.",
        is_alert=True
    ))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Answer Key — Module 1D: \"Il y a\" & The Negation Trap", h2_style))
    story.append(Paragraph("1. Neg: « Il n'y a pas de problème avec cette réservation. » | Int: « Est-ce qu'il y a un problème avec cette réservation ? »<br/>"
                           "2. Neg: « Il n'y a pas de pharmacie de garde près de la gare. » | Int: « Est-ce qu'il y a une pharmacie de garde près de la gare ? »<br/>"
                           "3. Neg: « Il n'y a pas de tables disponibles sur la terrasse. » | Int: « Est-ce qu'il y a des tables disponibles sur la terrasse ? »<br/>"
                           "4. Neg: « Il n'y a pas d'ascenseur en service dans cet hôtel. » | Int: « Est-ce qu'il y a un ascenseur en service dans cet hôtel ? »<br/>"
                           "5. Neg: « Il n'y a pas de questions difficiles dans cet examen. » | Int: « Est-ce qu'il y a des questions difficiles dans cet examen ? »<br/>"
                           "6. Neg: « Il n'y a pas de place libre dans ce compartiment de train. » | Int: « Est-ce qu'il y a une place libre dans ce compartiment de train ? »", body_style))
    story.append(make_callout(
        "WHY YOU TRIPPED: THE INDEFINITE ARTICLE COLLAPSE",
        "Under standard direct negation (ne... pas), quantity collapses to zero. In French syntax, zero quantity requires the partitive preposition 'DE' (or 'D\'' before vowels). Saying *« Il n'y a pas des tables » is ungrammatical. The only correct syntax is: « Il n'y a pas DE tables ».",
        is_alert=True
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("7. un / de  |  8. des / de  |  9. un / de  |  10. des / de  |  11. une / de  |  12. des / d'", body_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("Answer Key — Part 2: Integrated Real-World Scenarios", h2_style))
    story.append(Paragraph("<b>Section 2A: Forensic Corrections (Scenarios 1–10)</b>", body_bold))
    p2_corr_pdf = [
        "1. « Bonjour monsieur ! Vous avez des croissants chauds ? Non, désolé, il n'y a pas de croissants aujourd'hui. »",
        "2. « Bonjour docteur. J'ai 32 ans et depuis ce matin, j'ai très chaud et j'ai froid en même temps. »",
        "3. « Pierre et moi, demain on parle du projet avec le professeur. On est très contents de commencer. »",
        "4. « Pardon monsieur l'agent. Est-ce qu'il y a un train pour Rouen ? Non, il n'y a pas de train avant midi. »",
        "5. « Bonsoir madame, bonsoir monsieur. Vous avez faim ? Nous avons une belle table près de la fenêtre. »",
        "6. « Mes deux frères ont 20 ans. En hiver, ils ont toujours très froid et ils parlent [parl] lentement. »",
        "7. « Bonjour Maître Renard. Est-ce que vous avez reçu les documents ? Il y a des questions urgentes. »",
        "8. « Est-ce qu'il y a des musées ouverts à Paris aujourd'hui ? Non, le lundi il n'y a pas de musées d'art. »",
        "9. « Les enfants ont faim [il-z‿õ fɛ̃] et leurs parents sont très fatigués [il-sõ trɛ fa-ti-ge]. »",
        "10. « Dans ma chambre, il n'y a pas de minibar, et mon collègue et [pas de liaison] un client attendent dehors. »"
    ]
    for c_item in p2_corr_pdf:
        story.append(Paragraph(c_item, body_style))
        story.append(Spacer(1, 1.5))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Section 2B: Micro-Dialogue Solutions (Dialogues 11–20)</b>", body_bold))
    d_ans_pdf = [
        "11: avez | un ascenseur | d'ascenseur | sommes",
        "12: avez (faim) | avons | de l'eau minérale | de poisson",
        "13: avez | est | cherchez | une station | de station",
        "14: est | a (très chaud) | a (39 de fièvre) | d'autres symptômes | d'autres symptômes | a (peur)",
        "15: va | reste | ai (sommeil) | suis (épuisé) | commande | des boissons | de boisson",
        "16: une cuisine équipée | un lave-linge | de lave-linge | êtes | de problème",
        "17: es (prêt) | se tutoie | ai (hâte) | des tâches | de tâche | va",
        "18: avez (besoin) | a (un rhume) | a (très froid) | a (de la toux) | de toux",
        "19: avez | avez (faim) | avons (hâte) | du vin rouge | d'alcool fort",
        "20: de valise | Avez | un vol suivant | d'autre vol | sommes (désolés)"
    ]
    for da in d_ans_pdf:
        story.append(Paragraph(da, body_style))
        story.append(Spacer(1, 1.5))

    # Build PDF
    pdf_doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at {PDF_PATH}")

if __name__ == "__main__":
    create_docx()
    create_pdf()
