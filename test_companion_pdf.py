"""
test_companion_pdf.py - Validates that companion_pages.pdf meets all specifications:
- PDF file exists
- Exactly 33 pages (1 per chapter)
- Each page has US Letter dimensions (612 x 792 points)
- Each page contains the correct chapter number, titles, and key pedagogical sections
"""

import os
import unittest
from pathlib import Path
import pypdf

PDF_PATH = Path(__file__).parent / "companion_pages.pdf"
DATA_PATH = Path(__file__).parent / "companion_data.json"


class TestCompanionPDF(unittest.TestCase):
    def test_01_pdf_exists(self):
        """Verify companion_pages.pdf exists on disk."""
        self.assertTrue(PDF_PATH.exists(), f"File {PDF_PATH} does not exist")
        self.assertGreater(PDF_PATH.stat().st_size, 10000, "PDF file is suspiciously small")

    def test_02_page_count_and_dimensions(self):
        """Verify companion_pages.pdf has exactly 33 pages and US Letter dimensions."""
        if not PDF_PATH.exists():
            self.skipTest(f"{PDF_PATH} not found")

        reader = pypdf.PdfReader(str(PDF_PATH))
        self.assertEqual(len(reader.pages), 33, f"Expected 33 pages, found {len(reader.pages)}")

        for idx, page in enumerate(reader.pages, start=1):
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            self.assertAlmostEqual(
                width, 612.0, delta=2.0,
                msg=f"Page {idx} width {width} pt is not US Letter (612 pt)"
            )
            self.assertAlmostEqual(
                height, 792.0, delta=2.0,
                msg=f"Page {idx} height {height} pt is not US Letter (792 pt)"
            )

    def test_03_page_content_per_chapter(self):
        """Verify each page contains the corresponding chapter number and required content sections."""
        if not PDF_PATH.exists():
            self.skipTest(f"{PDF_PATH} not found")

        import json
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        reader = pypdf.PdfReader(str(PDF_PATH))
        for ch_num in range(1, 34):
            idx = ch_num - 1
            page = reader.pages[idx]
            text = page.extract_text() or ""
            
            # Verify chapter number is on the page
            ch_str_2d = f"{ch_num:02d}"
            ch_str_1d = str(ch_num)
            has_ch = (
                f"CHAPITRE {ch_str_2d}" in text.upper()
                or f"CHAPITRE {ch_str_1d}" in text.upper()
                or f"CH. {ch_str_2d}" in text.upper()
                or f"CH {ch_str_2d}" in text.upper()
            )
            self.assertTrue(
                has_ch,
                f"Page {idx+1} for Chapter {ch_num} is missing chapter number indicator in extracted text"
            )

            # Check that sections are present
            self.assertTrue(
                "Partie A" in text or "PARTIE A" in text or "Immersion" in text,
                f"Page {idx+1} (Ch {ch_num}) missing Partie A indicator"
            )
            self.assertTrue(
                "Partie B" in text or "PARTIE B" in text or "Exercice" in text,
                f"Page {idx+1} (Ch {ch_num}) missing Partie B indicator"
            )

            # Check French title snippet
            ch_data = data[str(ch_num)]
            title_fr = ch_data["title_fr"]
            # First word of title (or key token) should be present
            first_word = title_fr.split()[0]
            self.assertIn(
                first_word.lower(),
                text.lower(),
                f"Page {idx+1} (Ch {ch_num}) missing title word '{first_word}'"
            )


if __name__ == "__main__":
    unittest.main()
