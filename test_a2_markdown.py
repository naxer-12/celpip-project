# test_a2_markdown.py
import unittest
import os

class TestA2Markdown(unittest.TestCase):
    def setUp(self):
        self.md_path = "/Users/jainamshah/Downloads/Learning French/French_A2_Learning_Roadmap_Checklist.md"

    def test_file_exists_and_content(self):
        self.assertTrue(os.path.exists(self.md_path), "A2 Markdown file missing")
        with open(self.md_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("# French Learning Roadmap & Checklist (French A2)", content)
        for i in range(1, 72):
            self.assertIn(f"## Page {i}", content, f"Page {i} missing from markdown")
        self.assertGreater(len(content.splitlines()), 1000, "Markdown file is shorter than expected")

    def test_markdown_features(self):
        self.assertTrue(os.path.exists(self.md_path), "A2 Markdown file missing")
        with open(self.md_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("- [ ]", content, "Markdown should contain interactive checkboxes")
        self.assertIn("|", content, "Markdown should contain tables")
        self.assertIn("passé composé", content.lower(), "Key A2 grammar topic missing")
        self.assertIn("imparfait", content.lower(), "Key A2 grammar topic missing")
        self.assertIn("futur simple", content.lower(), "Key A2 grammar topic missing")

if __name__ == "__main__":
    unittest.main()
