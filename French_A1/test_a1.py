import unittest
import os
import subprocess
from bs4 import BeautifulSoup

class TestA1Roadmap(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_A1.html")
        self.pdf_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_A1.pdf")
        self.md_path = os.path.join(self.base_dir, "French_A1_Learning_Roadmap_Checklist.md")

    def test_a1_html_structure(self):
        self.assertTrue(os.path.exists(self.html_path), "A1 HTML missing")
        self.assertGreater(os.path.getsize(self.html_path), 2 * 1024 * 1024)
        with open(self.html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        pages = soup.find_all("div", class_="newpage")
        self.assertEqual(len(pages), 71)

    def test_a1_pdf_dimensions_and_page_count(self):
        self.assertTrue(os.path.exists(self.pdf_path), "A1 PDF missing")
        self.assertGreater(os.path.getsize(self.pdf_path), 2 * 1024 * 1024)
        res = subprocess.run(["pdfinfo", self.pdf_path], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("677.04 x 875.04 pts", res.stdout)
        pages_line = [l for l in res.stdout.splitlines() if l.startswith("Pages:")]
        self.assertEqual(int(pages_line[0].split(":")[1].strip()), 71)

    def test_a1_markdown(self):
        self.assertTrue(os.path.exists(self.md_path), "A1 MD missing")
        with open(self.md_path, "r", encoding="utf-8") as f:
            c = f.read()
        self.assertIn("# French Learning Roadmap & Checklist (French A1)", c)
        for i in range(1, 72):
            self.assertIn(f"## Page {i}", c)

if __name__ == "__main__":
    unittest.main()
