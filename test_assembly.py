"""Unit and integration tests for assemble_enriched_edition.py.

Verifies the lossless interleaving and assembly of the 116-page master edition:
- Target PDF exists at /Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf
- Total page count is exactly 116
- Front matter (pages 1-4) preserved from original
- Back matter (pages 104-116) preserved from original (pages 71-83)
- Each unit k (1..33) forms a 3-page block:
  - Page 3k+2: Original unit Page 1
  - Page 3k+3: Original unit Page 2 (Quiz)
  - Page 3k+4: Companion unit page (Immersion & exercises)
"""

import os
import unittest
import pypdf

ORIGINAL_PDF_PATH = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf"
COMPANION_PDF_PATH = "/Users/jainamshah/Downloads/Learning French/companion_pages.pdf"
ENRICHED_PDF_PATH = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf"


class TestAssembly(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # The target file must exist to run these tests
        if not os.path.exists(ENRICHED_PDF_PATH):
            raise FileNotFoundError(
                f"Enriched PDF not found at {ENRICHED_PDF_PATH}. Run assemble_enriched_edition.py first."
            )
        cls.enriched_reader = pypdf.PdfReader(ENRICHED_PDF_PATH)
        cls.orig_reader = pypdf.PdfReader(ORIGINAL_PDF_PATH)
        cls.comp_reader = pypdf.PdfReader(COMPANION_PDF_PATH)

    def test_target_pdf_exists(self):
        """Verify target PDF exists and is non-empty."""
        self.assertTrue(os.path.exists(ENRICHED_PDF_PATH), "Target enriched PDF must exist")
        self.assertGreater(os.path.getsize(ENRICHED_PDF_PATH), 100_000, "Enriched PDF size must be > 100KB")

    def test_total_page_count(self):
        """Verify enriched PDF has exactly 116 pages (4 front + 33*3 units + 13 back)."""
        self.assertEqual(len(self.orig_reader.pages), 83, "Original PDF must have 83 pages")
        self.assertEqual(len(self.comp_reader.pages), 33, "Companion PDF must have 33 pages")
        self.assertEqual(len(self.enriched_reader.pages), 116, "Enriched PDF must have exactly 116 pages")

    def test_front_matter_preserved(self):
        """Verify front matter (pages 1-4, indices 0-3) is preserved from original."""
        for page_idx in range(4):
            orig_text = self.orig_reader.pages[page_idx].extract_text()
            enriched_text = self.enriched_reader.pages[page_idx].extract_text()
            self.assertEqual(
                enriched_text.strip(),
                orig_text.strip(),
                f"Front matter mismatch on page {page_idx + 1}"
            )

    def test_back_matter_preserved(self):
        """Verify back matter (pages 104-116, indices 103-115) preserved from original (pages 71-83, indices 70-82)."""
        # Original back matter: pages 71-83 (indices 70-82, total 13 pages)
        # Enriched back matter: pages 104-116 (indices 103-115, total 13 pages)
        for offset in range(13):
            orig_idx = 70 + offset
            enriched_idx = 103 + offset
            orig_text = self.orig_reader.pages[orig_idx].extract_text()
            enriched_text = self.enriched_reader.pages[enriched_idx].extract_text()
            self.assertEqual(
                enriched_text.strip(),
                orig_text.strip(),
                f"Back matter mismatch: original page {orig_idx + 1} vs enriched page {enriched_idx + 1}"
            )

    def test_interleaved_units_structure(self):
        """Verify all 33 units have exact 3-page structure:
        - Page 3k+2: Original Unit Page 1
        - Page 3k+3: Original Unit Page 2 (Quiz)
        - Page 3k+4: Companion Unit Page
        """
        for k in range(1, 34):
            # 1-based page numbers:
            p_new_1 = 3 * k + 2
            p_new_2 = 3 * k + 3
            p_new_comp = 3 * k + 4

            # 0-based indices:
            idx_new_1 = p_new_1 - 1
            idx_new_2 = p_new_2 - 1
            idx_new_comp = p_new_comp - 1

            orig_p1_idx = (2 * k + 3) - 1
            orig_p2_idx = (2 * k + 4) - 1
            comp_idx = k - 1

            # Check Page 1 of Unit k
            orig_p1_text = self.orig_reader.pages[orig_p1_idx].extract_text().strip()
            new_p1_text = self.enriched_reader.pages[idx_new_1].extract_text().strip()
            self.assertEqual(
                new_p1_text,
                orig_p1_text,
                f"Unit {k} Page 1 mismatch at enriched page {p_new_1}"
            )

            # Check Page 2 of Unit k (Quiz)
            orig_p2_text = self.orig_reader.pages[orig_p2_idx].extract_text().strip()
            new_p2_text = self.enriched_reader.pages[idx_new_2].extract_text().strip()
            self.assertEqual(
                new_p2_text,
                orig_p2_text,
                f"Unit {k} Page 2 mismatch at enriched page {p_new_2}"
            )

            # Check Companion Page of Unit k
            comp_text = self.comp_reader.pages[comp_idx].extract_text().strip()
            new_comp_text = self.enriched_reader.pages[idx_new_comp].extract_text().strip()
            self.assertEqual(
                new_comp_text,
                comp_text,
                f"Unit {k} Companion page mismatch at enriched page {p_new_comp}"
            )

            # Check companion page content indicators
            self.assertIn("FICHE D'IMMERSION", new_comp_text, f"Unit {k} companion header missing")

    def test_metadata_copied(self):
        """Verify original PDF metadata or title is preserved."""
        orig_meta = self.orig_reader.metadata or {}
        enriched_meta = self.enriched_reader.metadata or {}
        # If original had a title, enriched should have title
        if '/Title' in orig_meta:
            self.assertIn('/Title', enriched_meta)
            self.assertTrue(len(enriched_meta['/Title']) > 0)


if __name__ == '__main__':
    unittest.main()
