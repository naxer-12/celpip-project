import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from pdf_engine import NumberedCanvas, get_custom_styles, build_callout

def test_render():
    pdf_path = "test_worksheet.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )
    styles = get_custom_styles()
    story = []
    
    # Hero Banner
    hero_data = [
        [Paragraph("RÉPUBLIQUE FRANÇAISE • FLE CURRICULUM A1", styles["HeroSub"])],
        [Paragraph("FICHE DE TRAVAIL & RÉTENTION COGNITIVE", styles["HeroTitle"])],
        [Paragraph("CHAPITRE 1 : LES PRÉSENTATIONS ET LES SALUTATIONS", styles["HeroGold"])],
        [Paragraph("Greetings, Politeness & Identity · Dual Coding · 5-Tier Architecture", styles["HeroSub"])]
    ]
    hero_t = Table(hero_data, colWidths=[540])
    hero_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#1A365D")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(hero_t)
    story.append(Spacer(1, 4))
    
    # Metadata Form Table
    meta_data = [
        [Paragraph("<b>Nom de l'apprenant :</b> ___________________________", styles["TableCell"]),
         Paragraph("<b>Niveau CECR :</b> A1 (Débutant)", styles["TableCell"])],
        [Paragraph("<b>Date d'évaluation :</b> ___________________________", styles["TableCell"]),
         Paragraph("<b>Durée :</b> 30–35 min  |  <b>Total :</b> /50 pts  |  <b>Seuil :</b> 80%", styles["TableCell"])]
    ]
    meta_t = Table(meta_data, colWidths=[300, 240])
    meta_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(meta_t)
    story.append(Spacer(1, 6))
    
    # Orientation Callout Box
    orient_text = (
        "<b>• Périmètre lexical testé :</b> 42 items lexicaux authentiques de ce chapitre.<br/>"
        "<b>• Pièges phonétiques & grammaticaux :</b><br/>"
        "  - Le 't' final muet dans 'salut' [sah-lyoo] vs 't' prononcé en anglais.<br/>"
        "  - Les voyelles nasales dans 'bonjour' [ohn], 'rien' [yanh], 'enchanté' [ahn].<br/>"
        "  - Distinction Tu vs Vous : 'S'il te plaît' (familier) vs 'S'il vous plaît' (formel)."
    )
    story.append(build_callout("MISSION BRIEFING & ORIENTATION BILINGUE", orient_text, kind="info", width=540))
    story.append(Spacer(1, 6))
    
    # Tier 1
    story.append(Paragraph("TIER 1 : ANCRAGE PHONÉTIQUE & ORTHOGRAPHIQUE [10 PTS]", styles["SectionHeading"]))
    story.append(Paragraph("Objectif : Identifier les lettres muettes, maîtriser la règle C-R-F-L et décoder les sons IPA.", styles["SectionSubtitle"]))
    
    # Build
    doc.build(story, canvasmaker=NumberedCanvas)
    print("Test render successful! File created:", pdf_path)

test_render()
