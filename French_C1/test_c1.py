import unittest
import os
import subprocess
from bs4 import BeautifulSoup
from c1_curriculum_data import C1_PAGES_DATA

class TestC1Roadmap(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_C1.html")
        self.pdf_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_C1.pdf")
        self.md_path = os.path.join(self.base_dir, "French_C1_Learning_Roadmap_Checklist.md")

    def test_curriculum_data_integrity(self):
        self.assertEqual(len(C1_PAGES_DATA), 71)
        for i in range(1, 72):
            self.assertIn(i, C1_PAGES_DATA, f"Missing page {i}")
            p = C1_PAGES_DATA[i]
            self.assertEqual(p["page"], i)
            self.assertTrue(len(p["title"]) > 0)
        
        all_text = " ".join(str(v) for v in C1_PAGES_DATA.values()).lower()
        self.assertIn("subjonctif imparfait", all_text)
        self.assertIn("conditionnel passé", all_text)
        self.assertIn("synthèse de documents", all_text)
        self.assertIn("nominalisation", all_text)
        self.assertIn("ready to move to c2", all_text)

    def test_c1_html_structure(self):
        self.assertTrue(os.path.exists(self.html_path), "C1 HTML missing")
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

    def test_c1_pdf_dimensions_and_page_count(self):
        self.assertTrue(os.path.exists(self.pdf_path), "C1 PDF missing")
        self.assertGreater(os.path.getsize(self.pdf_path), 2 * 1024 * 1024)
        res = subprocess.run(["pdfinfo", self.pdf_path], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("677.04 x 875.04 pts", res.stdout)
        pages_line = [l for l in res.stdout.splitlines() if l.startswith("Pages:")]
        self.assertEqual(int(pages_line[0].split(":")[1].strip()), 71)

    def test_c1_markdown(self):
        self.assertTrue(os.path.exists(self.md_path), "C1 MD missing")
        with open(self.md_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("# French Learning Roadmap & Checklist (French C1)", c)
        for i in range(1, 72):
            self.assertIn(f"## Page {i}", c)
        self.assertIn("- [ ]", c)
        self.assertIn("|", c)

if __name__ == "__main__":
    unittest.main()
