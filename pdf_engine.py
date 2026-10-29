import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Register Unicode TrueType Fonts
ARIAL_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL_ITALIC_PATH = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
ARIAL_BOLD_ITALIC_PATH = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
ARIAL_UNICODE_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

if os.path.exists(ARIAL_UNICODE_PATH):
    pdfmetrics.registerFont(TTFont('Arial', ARIAL_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Bold', ARIAL_BOLD_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Italic', ARIAL_ITALIC_PATH))
    pdfmetrics.registerFont(TTFont('Arial-BoldItalic', ARIAL_BOLD_ITALIC_PATH))
    pdfmetrics.registerFont(TTFont('ArialUnicode', ARIAL_UNICODE_PATH))
    pdfmetrics.registerFontFamily(
        'ArialUnicode',
        normal='ArialUnicode',
        bold='Arial-Bold',
        italic='Arial-Italic',
        boldItalic='Arial-BoldItalic'
    )
    BASE_FONT = "ArialUnicode"
    BOLD_FONT = "Arial-Bold"
    ITALIC_FONT = "Arial-Italic"
else:
    BASE_FONT = "Helvetica"
    BOLD_FONT = "Helvetica-Bold"
    ITALIC_FONT = "Helvetica-Oblique"

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
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        self.setFont(BASE_FONT, 7.5)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Running header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 11 * 72 - 24, "FLE A1 • SYSTÈME DE RÉTENTION COGNITIVE — VOCABULAIRE ESSENTIEL")
            self.drawRightString(8.5 * 72 - 36, 11 * 72 - 24, "FICHE D'ACTIVITÉS & CORRIGÉ DÉTAILLÉ")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(36, 11 * 72 - 28, 8.5 * 72 - 36, 11 * 72 - 28)
            
        # Running footer
        footer_text = f"Page {self._pageNumber} sur {page_count}"
        self.drawRightString(8.5 * 72 - 36, 20, footer_text)
        self.drawString(36, 20, "RÉPUBLIQUE FRANÇAISE • FLE A1 CURRICULUM — REPRODUCTION PÉDAGOGIQUE AUTORISÉE")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(36, 28, 8.5 * 72 - 36, 28)
        self.restoreState()

def get_custom_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name="HeroTitle",
        fontName=BOLD_FONT,
        fontSize=12.5,
        leading=15.5,
        textColor=colors.white,
        alignment=1 # Center
    ))
    styles.add(ParagraphStyle(
        name="HeroSub",
        fontName=BASE_FONT,
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#E2E8F0"),
        alignment=1
    ))
    styles.add(ParagraphStyle(
        name="HeroGold",
        fontName=BOLD_FONT,
        fontSize=10,
        leading=12.5,
        textColor=colors.HexColor("#FEF08A"),
        alignment=1
    ))
    styles.add(ParagraphStyle(
        name="SectionHeading",
        fontName=BOLD_FONT,
        fontSize=9.5,
        leading=12.5,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=7,
        spaceAfter=2,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name="SectionSubtitle",
        fontName=ITALIC_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=3,
        keepWithNext=True
    ))
    styles.add(ParagraphStyle(
        name="BoxTitleInfo",
        fontName=BOLD_FONT,
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1A365D")
    ))
    styles.add(ParagraphStyle(
        name="BoxTitleTrap",
        fontName=BOLD_FONT,
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#9B2C2C")
    ))
    styles.add(ParagraphStyle(
        name="BoxTitleTip",
        fontName=BOLD_FONT,
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#065F46")
    ))
    styles.add(ParagraphStyle(
        name="BoxBody",
        fontName=BASE_FONT,
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#2D3748")
    ))
    styles.add(ParagraphStyle(
        name="TableCell",
        fontName=BASE_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#1A202C")
    ))
    styles.add(ParagraphStyle(
        name="TableCellBold",
        fontName=BOLD_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#1A365D")
    ))
    styles.add(ParagraphStyle(
        name="TableHead",
        fontName=BOLD_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    ))
    styles.add(ParagraphStyle(
        name="ExPrompt",
        fontName=BASE_FONT,
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=1.5,
        spaceAfter=1.5
    ))
    styles.add(ParagraphStyle(
        name="CorrigeTitle",
        fontName=BOLD_FONT,
        fontSize=11.5,
        leading=14.5,
        textColor=colors.white,
        alignment=1
    ))
    return styles

def build_callout(title, text, kind="info", width=540):
    styles = get_custom_styles()
    if kind == "trap":
        bg_color = colors.HexColor("#FFF5F5")
        border_color = colors.HexColor("#9B2C2C")
        t_style = styles["BoxTitleTrap"]
        icon = "⚠️ PIÈGE CLASSIQUE : "
    elif kind == "tip":
        bg_color = colors.HexColor("#ECFDF5")
        border_color = colors.HexColor("#065F46")
        t_style = styles["BoxTitleTip"]
        icon = "💡 ANCRE DE RÉTENTION : "
    else:
        bg_color = colors.HexColor("#EFF6FF")
        border_color = colors.HexColor("#1A365D")
        t_style = styles["BoxTitleInfo"]
        icon = "📌 RÈGLE PÉDAGOGIQUE CLÉ : "
        
    p_content = [
        Paragraph(f"{icon}{title}", t_style),
        Spacer(1, 2),
        Paragraph(text.replace("\n", "<br/>"), styles["BoxBody"])
    ]
    t = Table([[p_content]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg_color),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LINELEFT', (0,0), (-1,-1), 3.0, border_color),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    return t

print("pdf_engine module setup complete with ArialUnicode support.")
