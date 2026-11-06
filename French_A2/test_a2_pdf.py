import unittest, os, subprocess

class TestA2PDF(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.pdf_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_A2.pdf")

    def test_pdf_exists_and_size(self):
        self.assertTrue(os.path.exists(self.pdf_path), "A2 PDF does not exist")
        self.assertGreater(os.path.getsize(self.pdf_path), 2 * 1024 * 1024, "PDF too small (<2MB)")

    def test_pdf_page_count_strictly_71(self):
        result = subprocess.run(["pdfinfo", self.pdf_path], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        
        pages_line = [l for l in result.stdout.splitlines() if l.startswith("Pages:")]
        self.assertTrue(len(pages_line) > 0, "No Pages line found in pdfinfo")
        page_count = int(pages_line[0].split(":")[1].strip())
        self.assertEqual(page_count, 71, f"Expected 71 pages, but got {page_count}")

    def test_pdf_page_dimensions(self):
        result = subprocess.run(["pdfinfo", self.pdf_path], capture_output=True, text=True)
        self.assertIn("677.04 x 875.04 pts", result.stdout)

if __name__ == "__main__":
    unittest.main()
