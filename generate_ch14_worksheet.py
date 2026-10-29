#!/usr/bin/env python3
"""
French A1 Cognitive Retention Worksheet Generator
Topic: Chapitre 14 - Le travail et les professions
Curriculum: FLE A1 (100 FLE Didier & French_A1_Vocab.pdf Section 5)
Outputs: Chapitre_14_Le_travail_et_les_professions_Worksheet.docx
"""

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = "/Users/jainamshah/Desktop/French Material/Worksheets"
DOCX_NAME = "Chapitre_14_Le_travail_et_les_professions_Worksheet.docx"
DOCX_PATH = os.path.join(OUTPUT_DIR, DOCX_NAME)

# ----------------------------------------------------------------------
# COLOR PALETTE & STYLING CONSTANTS
# ----------------------------------------------------------------------
HEX_NAVY = "1E3A8A"        # Deep Navy / Primary Heading
HEX_BLUE = "2563EB"        # Royal Blue / Secondary Accent
HEX_LIGHT_BLUE = "EFF6FF"  # Soft Ice Blue / Box Fill
HEX_SLATE_DARK = "1E293B"  # Charcoal / Body Text
HEX_SLATE_LIGHT = "F8FAFC" # Off-white / Table Alternate Row
HEX_BORDER = "CBD5E1"     # Slate Border
HEX_CRIMSON = "991B1B"    # Trap / Alert
HEX_LIGHT_CRIMSON = "FEF2F2" # Alert Fill
HEX_EMERALD = "065F46"    # Success / Anchor
HEX_LIGHT_EMERALD = "ECFDF5" # Success Fill
HEX_HEADER_GRAY = "E2E8F0" # Header Background

COLOR_NAVY = RGBColor(30, 58, 138)
COLOR_BLUE = RGBColor(37, 99, 235)
COLOR_SLATE_DARK = RGBColor(30, 41, 59)
COLOR_CRIMSON = RGBColor(153, 27, 27)
COLOR_EMERALD = RGBColor(6, 95, 70)
COLOR_MUTED = RGBColor(100, 116, 139)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=120, bottom=120, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_cell_box_border(cell, color_hex="CBD5E1", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def set_cell_left_border(cell, color_hex="1E3A8A", sz="24"):
    # sz 24 = 3pt thick accent bar on left
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def set_cell_bottom_border(cell, color_hex="CBD5E1", sz="6"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)

def make_row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def add_callout_box(doc, title, text, box_type="info"):
    # box_type: "info" (navy/blue), "trap" (crimson), "tip" (emerald)
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    
    cell = table.cell(0, 0)
    cell.width = Inches(7.0)
    
    if box_type == "trap":
        fill_hex = HEX_LIGHT_CRIMSON
        border_hex = HEX_CRIMSON
        title_color = COLOR_CRIMSON
        icon = "⚠️ PIÈGE CLASSIQUE (PHONÉTIQUE & GRAMMAIRE) : "
    elif box_type == "tip":
        fill_hex = HEX_LIGHT_EMERALD
        border_hex = HEX_EMERALD
        title_color = COLOR_EMERALD
        icon = "💡 ANCRE DE RETENTION (ASTUCE MÉMORISATION) : "
    else:
        fill_hex = HEX_LIGHT_BLUE
        border_hex = HEX_NAVY
        title_color = COLOR_NAVY
        icon = "📌 RÈGLE PÉDAGOGIQUE CLÉ : "
        
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=140, bottom=140, left=180, right=180)
    set_cell_left_border(cell, color_hex=border_hex, sz="24")
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    
    r_title = p.add_run(icon + title + "\n")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(10)
    r_title.font.color.rgb = title_color
    
    r_text = p.add_run(text)
    r_text.font.name = "Arial"
    r_text.font.size = Pt(9.5)
    r_text.font.color.rgb = COLOR_SLATE_DARK
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def add_tier_header(doc, tier_title, subtitle, points):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    
    # Tier Tag + Title
    r_title = p.add_run(tier_title.upper())
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(12)
    r_title.font.color.rgb = COLOR_NAVY
    
    r_pts = p.add_run(f"  [{points}]")
    r_pts.bold = True
    r_pts.font.name = "Arial"
    r_pts.font.size = Pt(11)
    r_pts.font.color.rgb = COLOR_CRIMSON
    
    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(6)
    p_sub.paragraph_format.keep_with_next = True
    
    r_sub = p_sub.add_run(subtitle)
    r_sub.italic = True
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9.5)
    r_sub.font.color.rgb = COLOR_MUTED

# ----------------------------------------------------------------------
# DOCUMENT BUILDER
# ----------------------------------------------------------------------
def build_worksheet():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = Document()
    
    # Standard margins: 0.75 in
    for section in doc.sections:
        section.top_margin = Inches(0.7)
        section.bottom_margin = Inches(0.7)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        section.different_first_page_header_footer = False
        
        # Header / Footer
        header = section.header
        p_hdr = header.paragraphs[0]
        p_hdr.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r_hdr = p_hdr.add_run("FLE A1 • Vocabulaire Essentiel • Chapitre 14 : Le travail et les professions")
        r_hdr.font.name = "Arial"
        r_hdr.font.size = Pt(8)
        r_hdr.font.color.rgb = COLOR_MUTED
        
        footer = section.footer
        p_ftr = footer.paragraphs[0]
        p_ftr.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_ftr = p_ftr.add_run("Système de Rétention Cognitive FLE A1 • Page ")
        r_ftr.font.name = "Arial"
        r_ftr.font.size = Pt(8.5)
        r_ftr.font.color.rgb = COLOR_MUTED

    # ------------------------------------------------------------------
    # HERO HEADER / METADATA BOX
    # ------------------------------------------------------------------
    hero_table = doc.add_table(rows=1, cols=1)
    hero_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hero_table.autofit = False
    hero_cell = hero_table.cell(0, 0)
    hero_cell.width = Inches(7.0)
    
    set_cell_background(hero_cell, "1E3A8A")
    set_cell_margins(hero_cell, top=160, bottom=160, left=200, right=200)
    
    p_h = hero_cell.paragraphs[0]
    p_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_h.paragraph_format.space_before = Pt(0)
    p_h.paragraph_format.space_after = Pt(2)
    
    r_h1 = p_h.add_run("RÉPUBLIQUE FRANÇAISE • FLE CURRICULUM A1\n")
    r_h1.font.name = "Arial"
    r_h1.font.size = Pt(9)
    r_h1.bold = True
    r_h1.font.color.rgb = RGBColor(191, 219, 254) # Pale blue
    
    r_h2 = p_h.add_run("FICHE DE TRAVAIL & RÉTENTION COGNITIVE\n")
    r_h2.font.name = "Arial"
    r_h2.font.size = Pt(16)
    r_h2.bold = True
    r_h2.font.color.rgb = RGBColor(255, 255, 255)
    
    r_h3 = p_h.add_run("CHAPITRE 14 : LE TRAVAIL ET LES PROFESSIONS\n")
    r_h3.font.name = "Arial"
    r_h3.font.size = Pt(12)
    r_h3.bold = True
    r_h3.font.color.rgb = RGBColor(254, 240, 138) # Light gold accent
    
    r_h4 = p_h.add_run("Dual Coding · Morphologie du Genre · Collocations Épisodiques · Cloze Contextuel")
    r_h4.font.name = "Arial"
    r_h4.font.size = Pt(9)
    r_h4.italic = True
    r_h4.font.color.rgb = RGBColor(226, 232, 240)
    
    # Metadata Form Table
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    meta_table = doc.add_table(rows=2, cols=4)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False
    
    col_widths = [Inches(1.8), Inches(2.2), Inches(1.5), Inches(1.5)]
    meta_data = [
        [("Nom de l'apprenant :", True), ("___________________________", False), ("Niveau CECR :", True), ("A1 (Débutant)", False)],
        [("Date d'évaluation :", True), ("___________________________", False), ("Durée estimée :", True), ("25 – 30 min", False)]
    ]
    
    for row_idx, row in enumerate(meta_table.rows):
        make_row_cant_split(row)
        for col_idx, cell in enumerate(row.cells):
            cell.width = col_widths[col_idx]
            set_cell_background(cell, "F1F5F9" if row_idx % 2 == 0 else "FFFFFF")
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            text, is_bold = meta_data[row_idx][col_idx]
            r = p.add_run(text)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.bold = is_bold
            r.font.color.rgb = COLOR_NAVY if is_bold else COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Pedagogical Brief / Retention Guide Box
    add_callout_box(
        doc,
        "GUIDE DE TRAVAIL & ÉCHELLE DE RÉTENTION (5 TIERS)",
        "Cette fiche d'acquisition lexicale est structurée selon l'échelle cognitive de rétention FLE :\n"
        "• Tier 1 : Ancrage phonétique & orthographique (lettres muettes, règle C-R-F-L, liaisons)\n"
        "• Tier 2 : Encodage morphologique du genre (suffi xes -eur/-euse, -teur/-trice, -ien/-ienne, épicènes)\n"
        "• Tier 3 : Collocations & paires verbe-nom (travailler dans vs chez, pas d'article après être)\n"
        "• Tier 4 : Cloze contextuel & micro-situations communicatives (entretien, pause-café, networking)\n"
        "• Tier 5 : Restitution active & détection d'intrus (production immédiate et justification cognitive)",
        box_type="info"
    )

    # ------------------------------------------------------------------
    # TIER 1: ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE (Dual Coding) [10 pts]
    # ------------------------------------------------------------------
    add_tier_header(
        doc,
        "Tier 1 : Ancrage Phonétique & Orthographique",
        "Objectif : Identifier les lettres muettes, maîtriser la règle C-R-F-L et les déclencheurs de liaison.",
        "10 Points"
    )
    
    add_callout_box(
        doc,
        "RÈGLE C-R-F-L & EXCEPTION DES PROFESSIONS EN -ER",
        "En français, les consonnes finales sont généralement MUETTES sauf C, R, F, L (règle 'CaReFuL').\n"
        "ATTENTION : Les métiers masculins en -ER (boulanger, infirmier, boucher, cuisinier) sont une EXCEPTION MAJEURE ! Le 'r' final est silencieux et 'er' se prononce [e]. En revanche, au féminin (-ère), l'accent grave ouvre le son [ɛʁ] et le 'r' devient fortement prononcé !",
        box_type="trap"
    )

    # Exercise 1.1: Phonetic Audit Table
    p_ex1 = doc.add_paragraph()
    p_ex1.paragraph_format.space_before = Pt(4)
    p_ex1.paragraph_format.space_after = Pt(4)
    p_ex1.paragraph_format.keep_with_next = True
    r = p_ex1.add_run("Exercice 1.1 — Audit des Sons et des Lettres Muettes [4 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex1.add_run("Cochez la case appropriée pour indiquer si la consonne finale est prononcée ou muette, puis notez la transcription approchée.")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    t_ph = doc.add_table(rows=7, cols=5)
    t_ph.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_ph.autofit = False
    
    ph_widths = [Inches(1.8), Inches(1.3), Inches(1.3), Inches(1.3), Inches(1.3)]
    ph_headers = ["Mot / Profession", "Consonne finale", "Prononcée ?", "Muette ?", "Son final (A1 IPA)"]
    
    for i, h in enumerate(ph_headers):
        cell = t_ph.cell(0, i)
        cell.width = ph_widths[i]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    ph_rows_data = [
        ("1. un avocat (m.)", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ ah-voh-kah ]"),
        ("2. une avocate (f.)", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ ah-voh-kaht ]"),
        ("3. un infirmier (m.)", "Consonne 'r'", "[  ] Oui", "[  ] Oui", "[ anh-feer-myay ]"),
        ("4. une infirmière (f.)", "Consonne 'r'", "[  ] Oui", "[  ] Oui", "[ anh-feer-myair ]"),
        ("5. un pharmacien (m.)", "Voyelle nasale 'en'", "[  ] Nasale [ɛ̃]", "[  ] Orale [ɛn]", "[ -syanh ]"),
        ("6. une pharmacienne (f.)", "Voyelle 'enne'", "[  ] Nasale [ɛ̃]", "[  ] Orale [ɛn]", "[ -syen ]"),
    ]

    for r_idx, row_data in enumerate(ph_rows_data, start=1):
        row = t_ph.rows[r_idx]
        make_row_cant_split(row)
        for c_idx, val in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = ph_widths[c_idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 != 0 else "F8FAFC")
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx == 0 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_NAVY if c_idx == 0 else COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Exercise 1.2: Orthographic Repair Drill
    p_ex2 = doc.add_paragraph()
    p_ex2.paragraph_format.space_before = Pt(6)
    p_ex2.paragraph_format.space_after = Pt(2)
    p_ex2.paragraph_format.keep_with_next = True
    r = p_ex2.add_run("Exercice 1.2 — Chasse aux Fautes d'Orthographe & Accents [3 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex2.add_run("Corrigez l'orthographe des professions suivantes en ajoutant les accents manquants (é, è, ê) ou en rectifiant la graphie :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    t_ortho = doc.add_table(rows=4, cols=2)
    t_ortho.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_ortho.autofit = False
    ortho_widths = [Inches(3.5), Inches(3.5)]
    
    ortho_items = [
        ("a) un ingenieur  ->  ________________________", "b) un medecin  ->  ________________________"),
        ("c) une secretaire  ->  ________________________", "d) un chomeur  ->  ________________________"),
        ("e) une cuisiniere  ->  ________________________", "f) une boite  ->  ________________________")
    ]
    
    for r_idx, (c1, c2) in enumerate(ortho_items):
        row = t_ortho.rows[r_idx]
        make_row_cant_split(row)
        for c_idx, text in enumerate([c1, c2]):
            cell = row.cells[c_idx]
            cell.width = ortho_widths[c_idx]
            set_cell_background(cell, "FFFFFF")
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            set_cell_box_border(cell, color_hex="E2E8F0", sz="4")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Exercise 1.3: Liaison & Enchaînement Audit
    p_ex3 = doc.add_paragraph()
    p_ex3.paragraph_format.space_before = Pt(6)
    p_ex3.paragraph_format.space_after = Pt(2)
    p_ex3.paragraph_format.keep_with_next = True
    r = p_ex3.add_run("Exercice 1.3 — Déclenchement de la Liaison Obligatoire [3 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex3.add_run("Indiquez si l'article indéfini 'un' [œ̃] fait une liaison obligatoire [œ̃.n-] avec le mot suivant :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    liaison_items = [
        "1. un avocat      -> [  ] Liaison [œ̃.na.vɔ.ka]      [  ] Pas de liaison",
        "2. un dentiste    -> [  ] Liaison                   [  ] Pas de liaison [œ̃.dɑ̃.tist]",
        "3. un ingénieur   -> [  ] Liaison [œ̃.nɛ̃.ʒe.njœʁ]   [  ] Pas de liaison",
        "4. un employé     -> [  ] Liaison [œ̃.nɑ̃.plwa.je]    [  ] Pas de liaison",
        "5. un patron      -> [  ] Liaison                   [  ] Pas de liaison [œ̃.pa.tʁɔ̃]",
        "6. un architecte  -> [  ] Liaison [œ̃.naʁ.ʃi.tɛkt]   [  ] Pas de liaison"
    ]
    t_lia = doc.add_table(rows=3, cols=2)
    t_lia.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lia.autofit = False
    for r_idx in range(3):
        row = t_lia.rows[r_idx]
        make_row_cant_split(row)
        for c_idx in range(2):
            idx = r_idx * 2 + c_idx
            cell = row.cells[c_idx]
            cell.width = Inches(3.5)
            set_cell_background(cell, "F8FAFC")
            set_cell_margins(cell, top=60, bottom=60, left=90, right=90)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(liaison_items[idx])
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------------------
    # TIER 2: ENCODAGE MORPHOLOGIQUE DU GENRE (Chunked Encoding) [10 pts]
    # ------------------------------------------------------------------
    add_tier_header(
        doc,
        "Tier 2 : Encodage Morphologique du Genre",
        "Objectif : Automatiser les régularités flexionnelles (M -> F) sans jamais isoler un nom de son article.",
        "10 Points"
    )

    add_callout_box(
        doc,
        "RÈGLE D'OR DU GENRE EN FLE : TOUJOURS LIER L'ARTICLE AU NOM !",
        "Ne mémorisez JAMAIS un nom de profession seul. Apprenez TOUJOURS le binôme article + nom :\n"
        "• Modèle -er -> -ère : le boulanger / la boulangère | l'infirmier / l'infirmière\n"
        "• Modèle -ien -> -ienne : le pharmacien / la pharmacienne | le musicien / la musicienne\n"
        "• Modèle -eur -> -euse : le serveur / la serveuse | le coiffeur / la coiffeuse\n"
        "• Modèle -teur -> -trice : l'acteur / l'actrice | le réalisateur / la réalisatrice\n"
        "• Modèle invariable en -e : le/la comptable, le/la journaliste, le/la dentiste, le/la secrétaire\n"
        "• Cas traditionnels : un médecin -> une femme médecin (ou une médecin) | un professeur -> une professeure",
        box_type="tip"
    )

    # Exercise 2.1: Gender Transformation Matrix
    p_ex21 = doc.add_paragraph()
    p_ex21.paragraph_format.space_before = Pt(4)
    p_ex21.paragraph_format.space_after = Pt(4)
    p_ex21.paragraph_format.keep_with_next = True
    r = p_ex21.add_run("Exercice 2.1 — Matrice de Transformation Morphologique [6 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex21.add_run("Complétez la forme féminine correspondante SANS OUBLIER l'article défini (la / l') ou indéfini (une) :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    t_gen = doc.add_table(rows=7, cols=4)
    t_gen.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_gen.autofit = False
    gen_widths = [Inches(1.8), Inches(1.7), Inches(1.8), Inches(1.7)]
    
    headers_gen = ["Masculin (Donné)", "Féminin (À écrire)", "Masculin (Donné)", "Féminin (À écrire)"]
    for i, h in enumerate(headers_gen):
        cell = t_gen.cell(0, i)
        cell.width = gen_widths[i]
        set_cell_background(cell, "2563EB")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    matrix_pairs = [
        ("1. Le boulanger", "-> ___________________", "7. Le traducteur", "-> ___________________"),
        ("2. Un informaticien", "-> ___________________", "8. Un chirurgien", "-> ___________________"),
        ("3. Le serveur", "-> ___________________", "9. Le dentiste", "-> ___________________"),
        ("4. Un acteur", "-> ___________________", "10. Un patron", "-> ___________________"),
        ("5. Le coiffeur", "-> ___________________", "11. L'agent immobilier", "-> ___________________"),
        ("6. Le comptable", "-> ___________________", "12. Un employé", "-> ___________________"),
    ]

    for r_idx, (m1, f1, m2, f2) in enumerate(matrix_pairs, start=1):
        row = t_gen.rows[r_idx]
        make_row_cant_split(row)
        for c_idx, val in enumerate([m1, f1, m2, f2]):
            cell = row.cells[c_idx]
            cell.width = gen_widths[c_idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 != 0 else "F8FAFC")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.bold = (c_idx in [0, 2])
            r.font.color.rgb = COLOR_NAVY if (c_idx in [0, 2]) else COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Exercise 2.2: Gender Detective
    p_ex22 = doc.add_paragraph()
    p_ex22.paragraph_format.space_before = Pt(6)
    p_ex22.paragraph_format.space_after = Pt(2)
    p_ex22.paragraph_format.keep_with_next = True
    r = p_ex22.add_run("Exercice 2.2 — Détective de Genre : Repérez et Corrigez l'Erreur [4 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex22.add_run("Chaque phrase contient une erreur d'article ou de terminaison de genre. Soulignez l'erreur et réécrivez la phrase correctement.")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    error_sentences = [
        "1. Marie travaille comme un doctoresse dans un grande usine.\n   Correction : _____________________________________________________________________________",
        "2. Sarah est une acteuse très talentueuse au théâtre de Paris.\n   Correction : _____________________________________________________________________________",
        "3. Mon frère travaille avec un secrétaire très efficace (fém.).\n   Correction : _____________________________________________________________________________",
        "4. Thomas est une pharmacien réputé dans notre quartier.\n   Correction : _____________________________________________________________________________"
    ]
    for s in error_sentences:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(s)
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------------------
    # TIER 3: COLLOCATIONS & PAIRES VERBE-NOM (Episodic Memory) [10 pts]
    # ------------------------------------------------------------------
    add_tier_header(
        doc,
        "Tier 3 : Collocations & Paires Verbe-Nom",
        "Objectif : Ancrer les patrons communicatifs naturels (verbes + prépositions + substantifs).",
        "10 Points"
    )

    add_callout_box(
        doc,
        "LA RÈGLE CRUCIALE : PAS D'ARTICLE APRÈS LE VERBE ÊTRE !",
        "En anglais, on dit obligatoirement : 'I am A doctor' ou 'She is AN engineer'.\n"
        "En français A1, ON SUPPRIME L'ARTICLE : 'Je suis médecin.' | 'Elle est avocate.' | 'Il est professeur.'\n"
        "On ajoute l'article seulement si la profession est qualifiée par un adjectif : 'C'est UN excellent médecin.'\n"
        "Prépositions de lieu : On dit 'travailler DANS un bureau / une usine' (lieu physique), mais 'travailler CHEZ Renault / Google' (nom d'entreprise / personne).",
        box_type="trap"
    )

    # Exercise 3.1: Preposition Matrix
    p_ex31 = doc.add_paragraph()
    p_ex31.paragraph_format.space_before = Pt(4)
    p_ex31.paragraph_format.space_after = Pt(4)
    p_ex31.paragraph_format.keep_with_next = True
    r = p_ex31.add_run("Exercice 3.1 — Prépositions et Milieu Professionnel (DANS vs CHEZ vs AU) [5 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex31.add_run("Complétez chaque phrase avec la préposition exacte : 'dans un(e)', 'chez', ou 'au' :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    prep_items = [
        "1. Sophie est comptable ; elle travaille ________ (un bureau / une grande boîte internationale).",
        "2. Antoine est ingénieur ; il travaille ________ (Google / une entreprise tech américaine).",
        "3. Céline est chirurgienne ; elle opère les patients ________ (l'hôpital public).",
        "4. Depuis deux mois, Marc a perdu son emploi ; il est actuellement ________ chômage.",
        "5. Ma cousine est vendeuse ; elle travaille ________ (un magasin de vêtements)."
    ]
    for item in prep_items:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(item)
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.color.rgb = COLOR_SLATE_DARK

    # Exercise 3.2: High-Frequency Workplace Verb-Noun Collocations
    p_ex32 = doc.add_paragraph()
    p_ex32.paragraph_format.space_before = Pt(6)
    p_ex32.paragraph_format.space_after = Pt(4)
    p_ex32.paragraph_format.keep_with_next = True
    r = p_ex32.add_run("Exercice 3.2 — Paires Verbe-Nom Authentiques (Association) [5 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex32.add_run("Reliez chaque verbe professionnel à son complément naturel pour former une collocation authentique :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    t_colloc = doc.add_table(rows=6, cols=3)
    t_colloc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_colloc.autofit = False
    col_w = [Inches(2.5), Inches(3.5), Inches(1.0)]
    
    colloc_headers = ["Verbe d'action", "Complément d'objet / Notion", "Votre réponse"]
    for i, h in enumerate(colloc_headers):
        cell = t_colloc.cell(0, i)
        cell.width = col_w[i]
        set_cell_background(cell, "1E3A8A")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    colloc_data = [
        ("1. Chercher...", "A. des heures supplémentaires (pour terminer un projet)", "1 -> [    ]"),
        ("2. Faire...", "B. un bon salaire à la fin de chaque mois", "2 -> [    ]"),
        ("3. Toucher...", "C. sa retraite après quarante ans de carrière", "3 -> [    ]"),
        ("4. Prendre...", "D. un stage en entreprise (pour valider son diplôme)", "4 -> [    ]"),
        ("5. Poser...", "E. sa candidature / son CV (pour une offre d'emploi)", "5 -> [    ]"),
    ]
    for r_idx, (v, c, ans) in enumerate(colloc_data, start=1):
        row = t_colloc.rows[r_idx]
        make_row_cant_split(row)
        for c_idx, text in enumerate([v, c, ans]):
            cell = row.cells[c_idx]
            cell.width = col_w[c_idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 != 0 else "F8FAFC")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if c_idx < 2 else WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = "Arial"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_NAVY if c_idx == 0 else COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------------------
    # TIER 4: CLOZE CONTEXTUEL & MICRO-SITUATIONS (Retrieval Practice) [10 pts]
    # ------------------------------------------------------------------
    add_tier_header(
        doc,
        "Tier 4 : Cloze Contextuel & Micro-Situations Réelles",
        "Objectif : Récupération active du lexique dans des mini-dialogues de communication authentique.",
        "10 Points"
    )

    add_callout_box(
        doc,
        "MÉTHODE DE RÉCUPÉRATION ACTIVE",
        "Complétez les blancs en vous basant sur l'indice entre crochets [English Cue]. Ne cherchez pas une banque de mots : forcez votre mémoire à récupérer directement le terme français exact avec son orthographe et ses accords !",
        box_type="tip"
    )

    # Micro-Situation A
    p_ms_a = doc.add_paragraph()
    p_ms_a.paragraph_format.space_before = Pt(4)
    p_ms_a.paragraph_format.space_after = Pt(2)
    p_ms_a.paragraph_format.keep_with_next = True
    r = p_ms_a.add_run("Situation A — Rencontre lors d'une réception (Networking) [3 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_NAVY

    dialogue_a = (
        "• Thomas : Bonjour Madame. Qu'est-ce que vous ___________________________ [do for a living] ?\n"
        "• Élodie : Bonjour ! Je ___________________________ [am an architect (f.) — attention : pas d'article !] chez Vinci.\n"
        "• Thomas : C'est formidable ! Et vous travaillez ___________________________ [in an office] ou sur les chantiers ?"
    )
    p_dia = doc.add_paragraph()
    p_dia.paragraph_format.space_before = Pt(2)
    p_dia.paragraph_format.space_after = Pt(6)
    r = p_dia.add_run(dialogue_a)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.font.color.rgb = COLOR_SLATE_DARK

    # Micro-Situation B
    p_ms_b = doc.add_paragraph()
    p_ms_b.paragraph_format.space_before = Pt(4)
    p_ms_b.paragraph_format.space_after = Pt(2)
    p_ms_b.paragraph_format.keep_with_next = True
    r = p_ms_b.add_run("Situation B — L'entretien d'embauche (Job Interview) [4 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_NAVY

    dialogue_b = (
        "• Le recruteur : Bonjour Julien. Vous ___________________________ [are looking for a job] actuellement ?\n"
        "• Julien : Oui, tout à fait. J'ai terminé un ___________________________ [internship] de six mois le mois dernier.\n"
        "• Le recruteur : Parfait. Notre ___________________________ [company / firm] recherche un bon\n"
        "  ___________________________ [IT developer / specialist (m.)] pour un travail à temps plein."
    )
    p_dib = doc.add_paragraph()
    p_dib.paragraph_format.space_before = Pt(2)
    p_dib.paragraph_format.space_after = Pt(6)
    r = p_dib.add_run(dialogue_b)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.font.color.rgb = COLOR_SLATE_DARK

    # Micro-Situation C
    p_ms_c = doc.add_paragraph()
    p_ms_c.paragraph_format.space_before = Pt(4)
    p_ms_c.paragraph_format.space_after = Pt(2)
    p_ms_c.paragraph_format.keep_with_next = True
    r = p_ms_c.add_run("Situation C — La Pause-Café entre collègues (Colleagues Chat) [3 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_NAVY

    dialogue_c = (
        "• Julie : Tu as parlé avec ___________________________ [the boss (m.)] ce matin ?\n"
        "• Marc : Oui, il a dit que nous devons faire des ___________________________ [overtime hours] ce vendredi.\n"
        "• Julie : Encore ? Décidément, j'ai hâte de prendre ___________________________ [my retirement] !"
    )
    p_dic = doc.add_paragraph()
    p_dic.paragraph_format.space_before = Pt(2)
    p_dic.paragraph_format.space_after = Pt(6)
    r = p_dic.add_run(dialogue_c)
    r.font.name = "Arial"
    r.font.size = Pt(9)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # TIER 5: RESTITUTION ACTIVE & DÉTECTION D'INTRUS [10 pts]
    # ------------------------------------------------------------------
    add_tier_header(
        doc,
        "Tier 5 : Restitution Active & Production Personnelle",
        "Objectif : Traduction inverse ciblée et discrimination sémantique / morphologique avancée.",
        "10 Points"
    )

    # Exercise 5.1: Reverse Translation Prompts
    p_ex51 = doc.add_paragraph()
    p_ex51.paragraph_format.space_before = Pt(4)
    p_ex51.paragraph_format.space_after = Pt(2)
    p_ex51.paragraph_format.keep_with_next = True
    r = p_ex51.add_run("Exercice 5.1 — Défis de Traduction Inverse (Anglais -> Français) [6 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex51.add_run("Traduisez les phrases suivantes en français courant en appliquant strictement les règles de grammaire A1 :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    trans_prompts = [
        ("1. What do you do for a living? (polite / formal with 'vous')", "-> __________________________________________________________________________________"),
        ("2. I am a lawyer (feminine) and I work in a company in Lyon.", "-> __________________________________________________________________________________"),
        ("3. Nicolas is looking for a job in a bakery.", "-> __________________________________________________________________________________"),
        ("4. My colleague (feminine) works full-time; she is very competent.", "-> __________________________________________________________________________________"),
        ("5. Are you an engineer (masculine)? (informal with 'tu')", "-> __________________________________________________________________________________"),
        ("6. She does not work anymore; she is retired.", "-> __________________________________________________________________________________")
    ]
    for prompt, line in trans_prompts:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(prompt + "\n")
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run(line)
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_SLATE_DARK

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # Exercise 5.2: L'Intrus avec Justification
    p_ex52 = doc.add_paragraph()
    p_ex52.paragraph_format.space_before = Pt(6)
    p_ex52.paragraph_format.space_after = Pt(2)
    p_ex52.paragraph_format.keep_with_next = True
    r = p_ex52.add_run("Exercice 5.2 — L'Intrus avec Justification Cognitive [4 points]\n")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_NAVY
    r_sub = p_ex52.add_run("Trouvez l'intrus parmi les 4 termes et justifiez OBLIGATOIREMENT votre choix (critère grammatical, genre, ou sémantique) :")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(9)
    r_sub.font.color.rgb = COLOR_SLATE_DARK

    intrus_items = [
        ("1. Un médecin  •  Un avocat  •  Un bureau  •  Un professeur",
         "• Intrus : ________________________  |  Justification : ______________________________________________________"),
        ("2. Une actrice  •  Une boulangère  •  Une serveuse  •  Un cuisinier",
         "• Intrus : ________________________  |  Justification : ______________________________________________________"),
        ("3. Une usine  •  Une entreprise  •  Un salaire  •  Un hôpital",
         "• Intrus : ________________________  |  Justification : ______________________________________________________"),
        ("4. Travailler dans  •  Faire un stage  •  Prendre le bus  •  Chercher un emploi",
         "• Intrus : ________________________  |  Justification : ______________________________________________________")
    ]
    for prompt, line in intrus_items:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(prompt + "\n")
        r1.bold = True
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run(line)
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # PAGE BREAK -> CORRIGÉ DÉTAILLÉ & EXPLICATIONS
    # ------------------------------------------------------------------
    doc.add_page_break()

    # Answer Key Hero Banner
    ak_table = doc.add_table(rows=1, cols=1)
    ak_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    ak_table.autofit = False
    ak_cell = ak_table.cell(0, 0)
    ak_cell.width = Inches(7.0)
    
    set_cell_background(ak_cell, "065F46") # Emerald green for teacher / answer key
    set_cell_margins(ak_cell, top=140, bottom=140, left=200, right=200)
    
    p_ak = ak_cell.paragraphs[0]
    p_ak.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ak.paragraph_format.space_before = Pt(0)
    p_ak.paragraph_format.space_after = Pt(2)
    
    r1 = p_ak.add_run("SECTION PÉDAGOGIQUE & AUTO-CORRECTION\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(9)
    r1.bold = True
    r1.font.color.rgb = RGBColor(167, 243, 208)
    
    r2 = p_ak.add_run("CORRIGÉ DÉTAILLÉ & ANCRES DE MÉMORISATION\n")
    r2.font.name = "Arial"
    r2.font.size = Pt(15)
    r2.bold = True
    r2.font.color.rgb = RGBColor(255, 255, 255)
    
    r3 = p_ak.add_run("Chapitre 14 : Le travail et les professions • Barème total : /50 points")
    r3.font.name = "Arial"
    r3.font.size = Pt(10)
    r3.italic = True
    r3.font.color.rgb = RGBColor(209, 250, 229)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # ------------------------------------------------------------------
    # CORRIGÉ TIER 1
    # ------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("CORRIGÉ TIER 1 : ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE [/10 pts]")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    t_sol1 = doc.add_table(rows=7, cols=4)
    t_sol1.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sol1.autofit = False
    s1_w = [Inches(1.8), Inches(1.2), Inches(1.8), Inches(2.2)]
    s1_h = ["Item", "Statut sonore", "Prononciation A1", "Explication & Ancre cognitive"]
    
    for i, h in enumerate(s1_h):
        c = t_sol1.cell(0, i)
        c.width = s1_w[i]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, top=80, bottom=80, left=80, right=80)
        p_c = c.paragraphs[0]
        p_c.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_c.add_run(h)
        r_c.font.name = "Arial"
        r_c.font.size = Pt(8.5)
        r_c.bold = True
        r_c.font.color.rgb = RGBColor(255, 255, 255)

    sol1_data = [
        ("1. un avocat", "Muette", "[ah-voh-kah]", "Le 't' final est muet (règle standard des consonnes finales)."),
        ("2. une avocate", "Prononcée", "[ah-voh-kaht]", "Le '-e' féminin oblige la consonne 't' à être articulée."),
        ("3. un infirmier", "Muette", "[anh-feer-myay]", "Exception C-R-F-L : la terminaison '-er' sonne [e] sans 'r'."),
        ("4. une infirmière", "Prononcée", "[anh-feer-myair]", "L'accent grave '-ère' ouvre le son [ɛ] et vocalise le 'r' [ʁ]."),
        ("5. un pharmacien", "Nasale [ɛ̃]", "[fahr-mah-syanh]", "La finale '-ien' produit une voyelle nasale pure sans 'n' oral."),
        ("6. une pharmacienne", "Orale [ɛn]", "[fahr-mah-syen]", "Le dédoublement '-nne' dénasalise : voyelle claire + 'n' articulé.")
    ]
    for r_idx, (it, st, pr, ex) in enumerate(sol1_data, start=1):
        row = t_sol1.rows[r_idx]
        make_row_cant_split(row)
        for c_idx, val in enumerate([it, st, pr, ex]):
            cell = row.cells[c_idx]
            cell.width = s1_w[c_idx]
            set_cell_background(cell, "FFFFFF" if r_idx % 2 != 0 else "F8FAFC")
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            set_cell_box_border(cell, color_hex="CBD5E1", sz="4")
            p_c = cell.paragraphs[0]
            p_c.paragraph_format.space_before = Pt(0)
            p_c.paragraph_format.space_after = Pt(0)
            r_c = p_c.add_run(val)
            r_c.font.name = "Arial"
            r_c.font.size = Pt(8)
            r_c.bold = (c_idx < 2)
            r_c.font.color.rgb = COLOR_NAVY if c_idx == 0 else COLOR_SLATE_DARK

    p_sol12 = doc.add_paragraph()
    p_sol12.paragraph_format.space_before = Pt(4)
    p_sol12.paragraph_format.space_after = Pt(2)
    p_sol12.add_run("Exercice 1.2 — Solutions Orthographe [3 pts] :\n").bold = True
    sol_12_text = (
        "• a) un ingénieur (accent aigu sur le 2e 'e')\n"
        "• b) un médecin (accent aigu sur le 1er 'e')\n"
        "• c) une secrétaire (accent aigu sur le 1er 'e')\n"
        "• d) un chômeur (accent circonflexe sur 'ô')\n"
        "• e) une cuisinière (accent grave sur 'è')\n"
        "• f) une boîte (accent circonflexe sur le 'î' - toléré 'boite' rectif. 1990)"
    )
    r = p_sol12.add_run(sol_12_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    p_sol13 = doc.add_paragraph()
    p_sol13.paragraph_format.space_before = Pt(4)
    p_sol13.paragraph_format.space_after = Pt(4)
    p_sol13.add_run("Exercice 1.3 — Solutions Liaisons [3 pts] :\n").bold = True
    sol_13_text = (
        "• 1. un avocat -> LIAISON [œ̃.na.vɔ.ka] (voyelle initiale)\n"
        "• 2. un dentiste -> PAS de liaison [œ̃.dɑ̃.tist] (consonne initiale 'd')\n"
        "• 3. un ingénieur -> LIAISON [œ̃.nɛ̃.ʒe.njœʁ] (voyelle initiale 'i')\n"
        "• 4. un employé -> LIAISON [œ̃.nɑ̃.plwa.je] (voyelle initiale 'e')\n"
        "• 5. un patron -> PAS de liaison [œ̃.pa.tʁɔ̃] (consonne initiale 'p')\n"
        "• 6. un architecte -> LIAISON [œ̃.naʁ.ʃi.tɛkt] (voyelle initiale 'a')"
    )
    r = p_sol13.add_run(sol_13_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # CORRIGÉ TIER 2
    # ------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("CORRIGÉ TIER 2 : ENCODAGE MORPHOLOGIQUE DU GENRE [/10 pts]")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    p_sol21 = doc.add_paragraph()
    p_sol21.paragraph_format.space_before = Pt(2)
    p_sol21.paragraph_format.space_after = Pt(2)
    p_sol21.add_run("Exercice 2.1 — Matrice des Métiers [6 pts] :\n").bold = True
    sol_21_text = (
        "1. Le boulanger -> la boulangère (-er -> -ère)\n"
        "2. Un informaticien -> une informaticienne (-ien -> -ienne)\n"
        "3. Le serveur -> la serveuse (-eur -> -euse)\n"
        "4. Un acteur -> une actrice (-teur -> -trice)\n"
        "5. Le coiffeur -> la coiffeuse (-eur -> -euse)\n"
        "6. Le comptable -> la comptable (épicène invariable en -e)\n"
        "7. Le traducteur -> la traductrice (-teur -> -trice)\n"
        "8. Un chirurgien -> une chirurgienne (-ien -> -ienne)\n"
        "9. Le dentiste -> la dentiste (épicène invariable en -e)\n"
        "10. Un patron -> une patronne (-on -> -onne)\n"
        "11. L'agent immobilier -> l'agente immobilière (ou l'agent)\n"
        "12. Un employé -> une employée (-é -> -ée)"
    )
    r = p_sol21.add_run(sol_21_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    p_sol22 = doc.add_paragraph()
    p_sol22.paragraph_format.space_before = Pt(4)
    p_sol22.paragraph_format.space_after = Pt(4)
    p_sol22.add_run("Exercice 2.2 — Détective de Genre [4 pts] :\n").bold = True
    sol_22_text = (
        "1. 'Marie travaille comme une femme médecin (ou médecin) dans UNE grande usine.' (Usine est féminin : une usine).\n"
        "2. 'Sarah est UNE ACTRICE très talentueuse...' (Attention au piège : 'acteuse' n'existe pas en français standard ! Le suffixe de racine latine est -teur -> -trice).\n"
        "3. 'Mon frère travaille avec UNE secrétaire très efficace.' (L'article doit s'accorder avec le genre de la personne).\n"
        "4. 'Thomas est UN pharmacien réputé...' (Thomas est masculin, donc 'un pharmacien')."
    )
    r = p_sol22.add_run(sol_22_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # CORRIGÉ TIER 3
    # ------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("CORRIGÉ TIER 3 : COLLOCATIONS & PAIRES VERBE-NOM [/10 pts]")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    p_sol31 = doc.add_paragraph()
    p_sol31.paragraph_format.space_before = Pt(2)
    p_sol31.paragraph_format.space_after = Pt(2)
    p_sol31.add_run("Exercice 3.1 — Prépositions Professionnelles [5 pts] :\n").bold = True
    sol_31_text = (
        "1. dans un bureau / dans une grande boîte (bureau et boîte = contenants physiques/structures fermées).\n"
        "2. chez Google (chez s'utilise pour les entreprises désignées par leur nom propre commercial).\n"
        "3. à l'hôpital (contraction prépositionnelle standard de lieu institutionnel).\n"
        "4. au chômage (expression idiomatique figée : être au chômage).\n"
        "5. dans un magasin (lieu physique clos)."
    )
    r = p_sol31.add_run(sol_31_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    p_sol32 = doc.add_paragraph()
    p_sol32.paragraph_format.space_before = Pt(4)
    p_sol32.paragraph_format.space_after = Pt(4)
    p_sol32.add_run("Exercice 3.2 — Paires Verbe-Nom [5 pts] :\n").bold = True
    sol_32_text = (
        "• 1 -> D : Chercher un emploi / un travail (To look for a job)\n"
        "• 2 -> A ou D : Faire des heures supplémentaires / Faire un stage\n"
        "• 3 -> B : Toucher un bon salaire (To earn / collect a good salary)\n"
        "• 4 -> C : Prendre sa retraite (To retire)\n"
        "• 5 -> E : Poser sa candidature (To apply / submit an application)"
    )
    r = p_sol32.add_run(sol_32_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # CORRIGÉ TIER 4
    # ------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("CORRIGÉ TIER 4 : CLOZE CONTEXTUEL & MICRO-SITUATIONS [/10 pts]")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    sol_4_text = (
        "• Situation A (3 pts) :\n"
        "  - vous faites dans la vie (Formule communicative consacrée)\n"
        "  - suis architecte (Rappel : SANS article après être ! 'Je suis une architecte' est fautif)\n"
        "  - dans un bureau (Lieu de travail)\n\n"
        "• Situation B (4 pts) :\n"
        "  - cherchez un emploi / un travail\n"
        "  - stage (Stage en entreprise = internship, et non une scène de théâtre)\n"
        "  - entreprise / boîte (boîte en registre familier courant)\n"
        "  - informaticien / développeur\n\n"
        "• Situation C (3 pts) :\n"
        "  - le patron\n"
        "  - heures supplémentaires\n"
        "  - ma retraite"
    )
    p_sol4 = doc.add_paragraph()
    r = p_sol4.add_run(sol_4_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # CORRIGÉ TIER 5
    # ------------------------------------------------------------------
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run("CORRIGÉ TIER 5 : RESTITUTION ACTIVE & DÉTECTION D'INTRUS [/10 pts]")
    r.bold = True
    r.font.name = "Arial"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    sol_51_text = (
        "Exercice 5.1 — Traductions Inverses (6 pts) :\n"
        "1. 'Qu'est-ce que vous faites dans la vie ?' (ou : 'Quelle est votre profession ?')\n"
        "2. 'Je suis avocate et je travaille dans une entreprise à Lyon.' (Pas d'article devant avocate !)\n"
        "3. 'Nicolas cherche un travail (ou un emploi) dans une boulangerie.'\n"
        "4. 'Ma collègue travaille à temps plein ; elle est très compétente.'\n"
        "5. 'Tu es ingénieur ?' (ou : 'Est-ce que tu es ingénieur ?')\n"
        "6. 'Elle ne travaille plus ; elle est à la retraite (ou retraitée).'"
    )
    p_sol51 = doc.add_paragraph()
    r = p_sol51.add_run(sol_51_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    sol_52_text = (
        "Exercice 5.2 — L'Intrus avec Justification (4 pts) :\n"
        "1. Intrus : Un bureau | Justification : C'est un lieu de travail / meuble (inanimé), tandis que les trois autres sont des personnes / professions.\n"
        "2. Intrus : Un cuisinier | Justification : C'est une profession au masculin, alors que les trois autres sont au féminin (actrice, boulangère, serveuse).\n"
        "3. Intrus : Un salaire | Justification : C'est une rémunération financière abstraite, alors que les trois autres sont des bâtiments / lieux de travail physiques.\n"
        "4. Intrus : Prendre le bus | Justification : C'est une action de transport quotidien, alors que les trois autres sont des collocations spécifiques au marché de l'emploi."
    )
    p_sol52 = doc.add_paragraph()
    r = p_sol52.add_run(sol_52_text)
    r.font.name = "Arial"
    r.font.size = Pt(8.5)
    r.font.color.rgb = COLOR_SLATE_DARK

    # ------------------------------------------------------------------
    # ANCRES DE MÉMORISATION PROFONDE (PEDAGOGICAL ANCHORS)
    # ------------------------------------------------------------------
    add_callout_box(
        doc,
        "ANCRES DE MÉMORISATION & PIÈGES MAJEURS ENREGISTRÉS DANS CETTE FICHE",
        "1. La suppression de l'article avec ÊTRE : Contrairement à l'anglais ('I am a teacher'), le français considère la profession comme un attribut statutaire assimilé à un adjectif. On dit donc 'Je suis professeur', SANS article. L'article réapparaît uniquement si la profession est caractérisée ('C'est un professeur exceptionnel').\n\n"
        "2. La dualité 'DANS' vs 'CHEZ' : Utilisez 'chez' dès qu'il s'agit d'une marque, d'une enseigne commerciale ou du nom d'une personne ('Je travaille chez Renault', 'chez le dentiste'). Utilisez 'dans' pour désigner le cadre architectural physique ('dans un bureau', 'dans une usine', 'dans un atelier').\n\n"
        "3. Le mot polysémique 'BUREAU' : Retenez qu'en français, 'le bureau' désigne à la fois le meuble sur lequel on écrit (desk) ET la pièce ou le bâtiment de travail (office). Pour dire 'I work in an office', on dit 'Je travaille dans un bureau'.\n\n"
        "4. Les faux-amis du monde professionnel : Le terme 'stage' en français désigne un apprentissage pratique en entreprise (internship) et NON une scène de spectacle. Le mot 'boîte' est l'équivalent familier ultra-courant d'entreprise ('Je bosse dans une bonne boîte').",
        box_type="tip"
    )

    doc.save(DOCX_PATH)
    print(f"SUCCESS: Generated {DOCX_PATH}")

if __name__ == "__main__":
    build_worksheet()
