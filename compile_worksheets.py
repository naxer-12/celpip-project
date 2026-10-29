import os
import re
import json
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from pdf_engine import NumberedCanvas, get_custom_styles, build_callout

OUTPUT_DIR = "/Users/jainamshah/Desktop/French Material/Worksheets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name):
    # Remove accents and special chars for clean filenames
    import unicodedata
    n = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode('utf-8')
    n = re.sub(r'[^a-zA-Z0-9]+', '_', n).strip('_')
    return n

def build_worksheet_pdf(ch_data, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = get_custom_styles()
    story = []
    
    ch_num = ch_data["ch_num"]
    title_fr = ch_data["title_fr"]
    title_en = ch_data["title_en"]
    word_count = ch_data["word_count"]
    target_time = ch_data.get("target_time", "30–35 min")
    total_marks = ch_data.get("total_marks", 50)
    passing_mark = ch_data.get("passing_mark", "80% (40/50)")
    traps = ch_data.get("traps", [])
    
    # ------------------------------------------------------------------
    # 1. HERO BANNER
    # ------------------------------------------------------------------
    hero_data = [
        [Paragraph("RÉPUBLIQUE FRANÇAISE • FLE CURRICULUM A1", styles["HeroSub"])],
        [Paragraph("FICHE D'ACTIVITÉS & RÉTENTION COGNITIVE", styles["HeroTitle"])],
        [Paragraph(f"CHAPITRE {ch_num:02d} : {title_fr.upper()}", styles["HeroGold"])],
        [Paragraph(f"{title_en} · Architecture Cognitive à 5 Niveaux", styles["HeroSub"])]
    ]
    hero_t = Table(hero_data, colWidths=[540])
    hero_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1A365D")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(hero_t)
    story.append(Spacer(1, 4))
    
    # ------------------------------------------------------------------
    # 2. METADATA FORM BOX
    # ------------------------------------------------------------------
    meta_data = [
        [Paragraph("<b>Nom de l'apprenant :</b> ___________________________", styles["TableCell"]),
         Paragraph("<b>Niveau CECR :</b> A1 (Débutant)", styles["TableCell"])],
        [Paragraph("<b>Date d'évaluation :</b> ___________________________", styles["TableCell"]),
         Paragraph(f"<b>Durée :</b> {target_time}  |  <b>Total :</b> /{total_marks} pts  |  <b>Seuil :</b> {passing_mark}", styles["TableCell"])]
    ]
    meta_t = Table(meta_data, colWidths=[300, 240])
    meta_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_t)
    story.append(Spacer(1, 5))
    
    # ------------------------------------------------------------------
    # 3. MISSION BRIEFING & TRAPS CALLOUT
    # ------------------------------------------------------------------
    traps_html = "".join([f"&nbsp;&nbsp;• {t}<br/>" for t in traps])
    orient_text = (
        f"<b>• Périmètre lexical testé :</b> Ce document teste de manière exhaustive les <b>{word_count} items lexicaux</b> essentiels de ce chapitre.<br/>"
        f"<b>• Pièges phonétiques, orthographiques et grammaticaux majeurs :</b><br/>"
        f"{traps_html}"
        f"<b>• Objectif pédagogique :</b> Fixation à long terme via double codage, encodage morphologique et rappel actif."
    )
    story.append(build_callout("MISSION BRIEFING & ORIENTATION BILINGUE", orient_text, kind="info", width=540))
    story.append(Spacer(1, 6))
    
    # ------------------------------------------------------------------
    # 4. TIER 1: ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE [10 PTS]
    # ------------------------------------------------------------------
    t1 = ch_data["tier1"]
    story.append(Paragraph("TIER 1 : ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Objectif : Identifier les lettres muettes, maîtriser la règle C-R-F-L et décoder les sons IPA.", styles["SectionSubtitle"]))
    
    # Tip callout
    story.append(build_callout(t1["phonetic_tip_title"], t1["phonetic_tip_text"], kind="tip", width=540))
    story.append(Spacer(1, 4))
    
    # Ex 1.1: Table
    story.append(Paragraph(f"<b>{t1['ex1_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    
    # Calculate colWidths for 5 cols summing to 540
    col_w_t1 = [135, 95, 115, 95, 100]
    headers_t1 = [Paragraph(f"<b>{h}</b>", styles["TableHead"]) for h in t1["ex1_headers"]]
    table_rows_t1 = [headers_t1]
    for row in t1["ex1_rows"]:
        formatted_row = [Paragraph(str(cell), styles["TableCell"]) for cell in row]
        table_rows_t1.append(formatted_row)
        
    t1_table = Table(table_rows_t1, colWidths=col_w_t1)
    t1_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A365D")),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t1_table)
    story.append(Spacer(1, 4))
    
    # Ex 1.2: Orthography items in 2 columns
    story.append(Paragraph(f"<b>{t1['ex2_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    items_12 = t1["ex2_items"]
    half = (len(items_12) + 1) // 2
    col1 = [Paragraph(it, styles["TableCell"]) for it in items_12[:half]]
    col2 = [Paragraph(it, styles["TableCell"]) for it in items_12[half:]]
    # Pad col2 if odd
    while len(col2) < len(col1):
        col2.append(Paragraph("", styles["TableCell"]))
    ex12_matrix = []
    for i in range(len(col1)):
        ex12_matrix.append([col1[i], col2[i]])
    ex12_table = Table(ex12_matrix, colWidths=[270, 270])
    ex12_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#EDF2F7")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(ex12_table)
    story.append(Spacer(1, 4))
    
    # Ex 1.3: Liaisons items
    story.append(Paragraph(f"<b>{t1['ex3_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    items_13 = t1["ex3_items"]
    half13 = (len(items_13) + 1) // 2
    col1_13 = [Paragraph(it, styles["TableCell"]) for it in items_13[:half13]]
    col2_13 = [Paragraph(it, styles["TableCell"]) for it in items_13[half13:]]
    while len(col2_13) < len(col1_13):
        col2_13.append(Paragraph("", styles["TableCell"]))
    ex13_matrix = []
    for i in range(len(col1_13)):
        ex13_matrix.append([col1_13[i], col2_13[i]])
    ex13_table = Table(ex13_matrix, colWidths=[270, 270])
    ex13_table.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#EDF2F7")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(ex13_table)
    story.append(Spacer(1, 6))
    
    # ------------------------------------------------------------------
    # 5. TIER 2: COMPULSORY GENDER & ARTICLE BINDING [10 PTS]
    # ------------------------------------------------------------------
    t2 = ch_data["tier2"]
    story.append(Paragraph("TIER 2 : ENCODAGE MORPHOLOGIQUE & GENRE GRAMMATICAL [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Règle d'or : Zéro substantif isolé. Tout nom s'apprend lié à son article défini ou indéfini.", styles["SectionSubtitle"]))
    
    story.append(build_callout(t2["gender_rule_title"], t2["gender_rule_text"], kind="info", width=540))
    story.append(Spacer(1, 4))
    
    # Ex 2.1: Matrix Table
    story.append(Paragraph(f"<b>{t2['ex1_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    col_w_t2 = [160, 110, 160, 110]
    headers_t2 = [Paragraph(f"<b>{h}</b>", styles["TableHead"]) for h in t2["ex1_headers"]]
    table_rows_t2 = [headers_t2]
    for row in t2["ex1_rows"]:
        formatted_row = [Paragraph(str(cell), styles["TableCell"]) for cell in row]
        table_rows_t2.append(formatted_row)
        
    t2_table = Table(table_rows_t2, colWidths=col_w_t2)
    t2_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2B6CB0")),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t2_table)
    story.append(Spacer(1, 4))
    
    # Ex 2.2: Detective sentences
    story.append(Paragraph(f"<b>{t2['ex2_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    for s in t2["ex2_sentences"]:
        story.append(Paragraph(s.replace("\n", "<br/>"), styles["TableCell"]))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 4))
    
    # ------------------------------------------------------------------
    # 6. TIER 3: COLLOCATION & NATURAL VERB-NOUN CHUNKS [10 PTS]
    # ------------------------------------------------------------------
    t3 = ch_data["tier3"]
    story.append(Paragraph("TIER 3 : COLLOCATIONS & CHUNKS COMMUNICATIFS [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Objectif : Fixer les syntagmes naturels et automatismes verbaux en contexte d'action.", styles["SectionSubtitle"]))
    
    story.append(build_callout(t3["colloc_tip_title"], t3["colloc_tip_text"], kind="tip", width=540))
    story.append(Spacer(1, 4))
    
    # Ex 3.1: Communicative chunks sentences
    story.append(Paragraph(f"<b>{t3['ex1_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    for s in t3["ex1_sentences"]:
        story.append(Paragraph(s, styles["TableCell"]))
        story.append(Spacer(1, 1.5))
    story.append(Spacer(1, 3))
    
    # Ex 3.2: Collocation matching table
    story.append(Paragraph(f"<b>{t3['ex2_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    col_w_t3 = [230, 230, 80]
    headers_t3 = [Paragraph(f"<b>{h}</b>", styles["TableHead"]) for h in t3["ex2_headers"]]
    table_rows_t3 = [headers_t3]
    for row in t3["ex2_rows"]:
        formatted_row = [Paragraph(str(cell), styles["TableCell"]) for cell in row]
        table_rows_t3.append(formatted_row)
        
    t3_table = Table(table_rows_t3, colWidths=col_w_t3)
    t3_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2C7A7B")),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t3_table)
    story.append(Spacer(1, 6))
    
    # ------------------------------------------------------------------
    # 7. TIER 4: CONTEXTUAL CLOZE & PRAGMATIC MICRO-DIALOGUES [10 PTS]
    # ------------------------------------------------------------------
    t4 = ch_data["tier4"]
    story.append(Paragraph("TIER 4 : MICRO-DIALOGUES SITUATIONNELS [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Objectif : Récupération active sans banque de mots dans des scénarios FLE réels.", styles["SectionSubtitle"]))
    
    story.append(build_callout(t4["cloze_tip_title"], t4["cloze_tip_text"], kind="info", width=540))
    story.append(Spacer(1, 4))
    
    for diag in t4["dialogues"]:
        d_title = diag["title"]
        d_lines = "<br/>".join(diag["lines"])
        p_diag = [
            Paragraph(f"<b>{d_title}</b>", styles["TableCellBold"]),
            Spacer(1, 2),
            Paragraph(d_lines, styles["TableCell"])
        ]
        t_diag = Table([[p_diag]], colWidths=[540])
        t_diag.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#3182CE")),
        ]))
        story.append(t_diag)
        story.append(Spacer(1, 4))
        
    story.append(Spacer(1, 4))
    
    # ------------------------------------------------------------------
    # 8. TIER 5: EXHAUSTIVE ACTIVE RECALL & REVERSE PRODUCTION [10 PTS]
    # ------------------------------------------------------------------
    t5 = ch_data["tier5"]
    story.append(Paragraph("TIER 5 : RESTITUTION ACTIVE & PENSÉE CRITIQUE [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Objectif : Traduction ciblée anglais-français et justification sémantique de l'intrus.", styles["SectionSubtitle"]))
    
    # Ex 5.1: Reverse translations
    story.append(Paragraph(f"<b>{t5['ex1_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    for prompt_pair in t5["ex1_prompts"]:
        story.append(Paragraph(f"<b>{prompt_pair[0]}</b>", styles["TableCell"]))
        story.append(Paragraph(f"{prompt_pair[1]}", styles["TableCell"]))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 4))
    
    # Ex 5.2: L'intrus with justification
    story.append(Paragraph(f"<b>{t5['ex2_title']}</b>", styles["TableCellBold"]))
    story.append(Spacer(1, 2))
    for item in t5["ex2_intrus"]:
        story.append(Paragraph(f"<b>{item[0]}</b>", styles["TableCellBold"]))
        story.append(Paragraph(f"{item[1]}", styles["TableCell"]))
        story.append(Spacer(1, 2))
    story.append(Spacer(1, 8))
    
    # ------------------------------------------------------------------
    # 9. CORRIGÉ DÉTAILLÉ (FRESH PAGE)
    # ------------------------------------------------------------------
    story.append(PageBreak())
    
    # Corrigé Header Banner
    corr_hero_data = [
        [Paragraph("RÉPUBLIQUE FRANÇAISE • FLE CURRICULUM A1", styles["HeroSub"])],
        [Paragraph(f"CORRIGÉ DÉTAILLÉ & CLÉS DE MÉMORISATION", styles["CorrigeTitle"])],
        [Paragraph(f"CHAPITRE {ch_num:02d} : {title_fr.upper()}", styles["HeroGold"])],
        [Paragraph("Solutions complètes · Barème de notation /50 · Explications cognitives", styles["HeroSub"])]
    ]
    corr_hero_t = Table(corr_hero_data, colWidths=[540])
    corr_hero_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#742A2A")), # Deep Burgundy/Crimson
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(corr_hero_t)
    story.append(Spacer(1, 6))
    
    c = ch_data["corrige"]
    
    # Tier 1 Corrige
    p_t1 = [
        Paragraph("<b>SOLUTIONS TIER 1 : ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE [10 PTS]</b>", styles["TableCellBold"]),
        Spacer(1, 2),
        Paragraph(c["tier1_text"].replace("\n", "<br/>"), styles["TableCell"])
    ]
    t_box_1 = Table([[p_t1]], colWidths=[540])
    t_box_1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFF5F5")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#C53030")),
    ]))
    story.append(t_box_1)
    story.append(Spacer(1, 4))
    
    # Tier 2 Corrige
    p_t2 = [
        Paragraph("<b>SOLUTIONS TIER 2 : ENCODAGE MORPHOLOGIQUE & GENRE [10 PTS]</b>", styles["TableCellBold"]),
        Spacer(1, 2),
        Paragraph(c["tier2_text"].replace("\n", "<br/>"), styles["TableCell"])
    ]
    t_box_2 = Table([[p_t2]], colWidths=[540])
    t_box_2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#2B6CB0")),
    ]))
    story.append(t_box_2)
    story.append(Spacer(1, 4))
    
    # Tier 3 Corrige
    p_t3 = [
        Paragraph("<b>SOLUTIONS TIER 3 : COLLOCATIONS & CHUNKS [10 PTS]</b>", styles["TableCellBold"]),
        Spacer(1, 2),
        Paragraph(c["tier3_text"].replace("\n", "<br/>"), styles["TableCell"])
    ]
    t_box_3 = Table([[p_t3]], colWidths=[540])
    t_box_3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#2C7A7B")),
    ]))
    story.append(t_box_3)
    story.append(Spacer(1, 4))
    
    # Tier 4 Corrige
    p_t4 = [
        Paragraph("<b>SOLUTIONS TIER 4 : MICRO-DIALOGUES SITUATIONNELS [10 PTS]</b>", styles["TableCellBold"]),
        Spacer(1, 2),
        Paragraph(c["tier4_text"].replace("\n", "<br/>"), styles["TableCell"])
    ]
    t_box_4 = Table([[p_t4]], colWidths=[540])
    t_box_4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F7FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#3182CE")),
    ]))
    story.append(t_box_4)
    story.append(Spacer(1, 4))
    
    # Tier 5 Corrige
    p_t5 = [
        Paragraph("<b>SOLUTIONS TIER 5 : RESTITUTION ACTIVE & L'INTRUS [10 PTS]</b>", styles["TableCellBold"]),
        Spacer(1, 2),
        Paragraph(c["tier5_text"].replace("\n", "<br/>"), styles["TableCell"])
    ]
    t_box_5 = Table([[p_t5]], colWidths=[540])
    t_box_5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFBEB")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 2.5, colors.HexColor("#D97706")),
    ]))
    story.append(t_box_5)
    story.append(Spacer(1, 6))
    
    # Pedagogical Memory Anchors
    story.append(build_callout(c["anchors_title"], c["anchors_text"], kind="tip", width=540))
    story.append(Spacer(1, 6))
    
    # BUILD PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    return output_path

if __name__ == "__main__":
    with open("chapters_batch_1.json", "r", encoding="utf-8") as f:
        b1 = json.load(f)
    test_ch1 = b1["1"]
    out_file = os.path.join(OUTPUT_DIR, "Chapitre_01_Les_presentations_et_les_salutations_Worksheet.pdf")
    build_worksheet_pdf(test_ch1, out_file)
    print("Test build of Chapter 1 complete! File:", out_file)
