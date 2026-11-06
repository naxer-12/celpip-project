import os
import urllib.parse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Import cards from dataset builder
from build_flashcards_dataset import cards

ARIAL_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL_ITALIC_PATH = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
ARIAL_UNICODE_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

if os.path.exists(ARIAL_UNICODE_PATH):
    pdfmetrics.registerFont(TTFont('Arial', ARIAL_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Bold', ARIAL_BOLD_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Italic', ARIAL_ITALIC_PATH))
    pdfmetrics.registerFont(TTFont('ArialUnicode', ARIAL_UNICODE_PATH))
    pdfmetrics.registerFontFamily(
        'ArialUnicode',
        normal='ArialUnicode',
        bold='Arial-Bold',
        italic='Arial-Italic',
        boldItalic='Arial-Bold'
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
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont(BASE_FONT, 8)
        self.setFillColor(colors.HexColor("#64748b"))
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(792 - 36, 20, page_text)
        self.drawString(36, 20, "DELF A1 French 100 Flashcards Master Deck — Introductions, Identity, Age, Jobs & Hobbies")
        self.restoreState()

def build_pdf():
    pdf_path = "/Users/jainamshah/Downloads/Learning French/French_A1_100_Flashcards.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(letter),
        leftMargin=28,
        rightMargin=28,
        topMargin=28,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontName=BOLD_FONT,
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#1e3a8a"),
        spaceAfter=4
    )
    sub_style = ParagraphStyle(
        'SubStyle',
        parent=styles['Normal'],
        fontName=BASE_FONT,
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#475569"),
        spaceAfter=8
    )

    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['Normal'],
        fontName=BASE_FONT,
        fontSize=7.2,
        leading=9.2,
        textColor=colors.HexColor("#0f172a")
    )
    cell_bold = ParagraphStyle(
        'CellBold',
        parent=styles['Normal'],
        fontName=BOLD_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor("#0f172a")
    )
    cell_phonetic = ParagraphStyle(
        'CellPhonetic',
        parent=styles['Normal'],
        fontName=ITALIC_FONT,
        fontSize=7.0,
        leading=9.0,
        textColor=colors.HexColor("#2563eb")
    )
    th_style = ParagraphStyle(
        'THStyle',
        parent=styles['Normal'],
        fontName=BOLD_FONT,
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white
    )

    elements = [
        Paragraph("DELF A1 French: 100 Essential Flashcards Master Deck", title_style),
        Paragraph("Topics: Greetings, Personal Identity, Age, Nationalities, Occupations & Hobbies | Pronunciation, Grammar, Plurals & Liaisons", sub_style),
    ]

    table_data = [[
        Paragraph("<b>#</b>", th_style),
        Paragraph("<b>French (with Article)</b>", th_style),
        Paragraph("<b>English Meaning</b>", th_style),
        Paragraph("<b>Pronunciation</b>", th_style),
        Paragraph("<b>Gender</b>", th_style),
        Paragraph("<b>Example Sentence (A1)</b>", th_style),
        Paragraph("<b>Plural / Conjugation</b>", th_style),
        Paragraph("<b>Liaison & Teacher's Notes</b>", th_style)
    ]]

    def clean_text(txt):
        if not txt:
            return ""
        # Convert markdown bold/italics and fix br tags for ReportLab
        txt = txt.replace('<br>', '<br/>')
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('&amp;amp;', '&amp;')
        txt = txt.replace('<br/>', 'TEMP_BR')
        txt = txt.replace('<', '&lt;').replace('>', '&gt;')
        txt = txt.replace('TEMP_BR', '<br/>')
        txt = txt.replace('**', '')
        txt = txt.replace('*', '')
        return txt

    for c in cards:
        table_data.append([
            Paragraph(f"<b>{c['num']}</b>", cell_style),
            Paragraph(f"<b>{clean_text(c['french'])}</b>", cell_bold),
            Paragraph(clean_text(c['english']), cell_style),
            Paragraph(clean_text(c['pronunciation']), cell_phonetic),
            Paragraph(clean_text(c['gender']), cell_style),
            Paragraph(clean_text(c['sentence']), cell_style),
            Paragraph(clean_text(c['plural_or_conj']), cell_style),
            Paragraph(clean_text(c['liaison_notes']), cell_style),
        ])

    # Printable landscape width = 792 - 56 = 736
    # 8 columns: 22, 100, 95, 95, 54, 150, 110, 110 = 736
    col_widths = [22, 95, 90, 95, 54, 150, 115, 115]

    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))

    elements.append(t)
    doc.build(elements, canvasmaker=NumberedCanvas)
    print("PDF generated successfully:", pdf_path)

if __name__ == '__main__':
    build_pdf()
