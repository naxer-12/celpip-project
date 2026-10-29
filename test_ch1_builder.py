import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

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
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Running header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 11 * 72 - 28, "FLE A1 • Vocabulaire Essentiel • Système de Rétention Cognitive")
            self.drawRightString(8.5 * 72 - 36, 11 * 72 - 28, "Fiche d'Évaluation & Corrigé")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(36, 11 * 72 - 32, 8.5 * 72 - 36, 11 * 72 - 32)
            
        # Running footer
        footer_text = f"Page {self._pageNumber} sur {page_count}"
        self.drawRightString(8.5 * 72 - 36, 22, footer_text)
        self.drawString(36, 22, "RÉPUBLIQUE FRANÇAISE • FLE A1 CURRICULUM — REPRODUCTION PÉDAGOGIQUE AUTORISÉE")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(36, 32, 8.5 * 72 - 36, 32)
        self.restoreState()

print("Canvas class ready.")
