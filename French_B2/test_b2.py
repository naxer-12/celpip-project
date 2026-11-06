import unittest
import os
import re
import subprocess
from bs4 import BeautifulSoup
from b2_curriculum_data import B2_PAGES_DATA

class TestB2Roadmap(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_B2.html")
        self.pdf_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_B2.pdf")
        self.md_path = os.path.join(self.base_dir, "French_B2_Learning_Roadmap_Checklist.md")

    def test_curriculum_data_integrity(self):
        self.assertEqual(len(B2_PAGES_DATA), 71)
        for i in range(1, 72):
            self.assertIn(i, B2_PAGES_DATA, f"Missing page {i}")
            p = B2_PAGES_DATA[i]
            self.assertEqual(p["page"], i)
            self.assertTrue(len(p["title"]) > 0)
        
        all_text = " ".join(str(v) for v in B2_PAGES_DATA.values()).lower()
        self.assertIn("subjonctif passé", all_text)
        self.assertIn("futur antérieur", all_text)
        self.assertIn("nominalisation", all_text)
        self.assertIn("conditionnel", all_text)
        self.assertIn("ready to move to c1", all_text)

    def test_b2_html_structure(self):
        self.assertTrue(os.path.exists(self.html_path), "B2 HTML missing")
        self.assertGreater(os.path.getsize(self.html_path), 2 * 1024 * 1024)
        with open(self.html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        pages = soup.find_all("div", class_="newpage")
        self.assertEqual(len(pages), 71)

        # Check badges on pages 2..71
        for i in range(2, 72):
            p = soup.find(id=f"page{i}")
            badge_div = p.find("div", class_="page-badge")
            self.assertIsNotNone(badge_div, f"Page {i} missing badge")
            self.assertEqual(badge_div.get_text().strip(), str(i - 1))

    def test_b2_pdf_dimensions_and_page_count(self):
        self.assertTrue(os.path.exists(self.pdf_path), "B2 PDF missing")
        self.assertGreater(os.path.getsize(self.pdf_path), 2 * 1024 * 1024)
        res = subprocess.run(["pdfinfo", self.pdf_path], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("677.04 x 875.04 pts", res.stdout)
        pages_line = [l for l in res.stdout.splitlines() if l.startswith("Pages:")]
        self.assertEqual(int(pages_line[0].split(":")[1].strip()), 71)

    def test_b2_markdown(self):
        self.assertTrue(os.path.exists(self.md_path), "B2 MD missing")
        with open(self.md_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("# French Learning Roadmap & Checklist (French B2)", c)
        for i in range(1, 72):
            self.assertIn(f"## Page {i}", c)
        self.assertIn("- [ ]", c)
        self.assertIn("|", c)

if __name__ == "__main__":
    unittest.main()
