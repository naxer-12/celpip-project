import unittest
import os
from bs4 import BeautifulSoup

class TestA2HTML(unittest.TestCase):
    def setUp(self):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.html_path = os.path.join(self.base_dir, "French_Learning_Roadmap_Checklist_French_A2.html")

    def test_file_exists_and_size(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        self.assertGreater(os.path.getsize(self.html_path), 2 * 1024 * 1024, "HTML file too small (<2MB)")

    def test_all_71_pages_present(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        with open(self.html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        pages = soup.find_all("div", class_="newpage")
        self.assertEqual(len(pages), 71)
        for i in range(1, 72):
            p = soup.find(id=f"page{i}")
            self.assertIsNotNone(p, f"page{i} div missing")
            
            # Check image layer
            img_layer = p.find("div", class_="image_layer")
            self.assertIsNotNone(img_layer, f"page{i} image_layer missing")
            img = img_layer.find("img")
            self.assertIsNotNone(img, f"page{i} img missing")
            self.assertTrue(img.get("src", "").startswith("data:image/jpeg;base64,"), f"page{i} img not base64 embedded")
            
            # Check text layer
            text_layer = p.find("div", class_="text_layer")
            self.assertIsNotNone(text_layer, f"page{i} text_layer missing")

    def test_print_css_present(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("@page", content)
        self.assertIn("size: 902px 1166px", content)
        self.assertIn("French Learning Roadmap & Checklist", content)
        self.assertIn("French A2", content)
        self.assertIn(".text_layer span.w1", content)
        self.assertIn(".text_layer span.w39", content)
        self.assertIn(".text_layer span.l1", content)
        self.assertIn(".text_layer span.l39", content)
        self.assertIn("data:font/woff2;base64,", content)

    def test_curriculum_content_coverage(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Verify distinctive keywords across modules
        self.assertIn("Overall Objectives of A2 Level", content)
        self.assertIn("Real-Life Outcomes at CEFR A2", content)
        self.assertIn("A2 French – Core Communicative Functions", content)
        self.assertIn("A2 Grammar: Nouns, Gender Rules & Plural Patterns", content)
        self.assertIn("A2 Thematic Vocabulary: Biography & Life Milestones", content)
        self.assertIn("A2 Speaking Mastery: Continuous Monologue", content)
        self.assertIn("Ready to Move to B1", content)

    def test_badge_numbers(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        with open(self.html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        for i in range(2, 72):
            p = soup.find(id=f"page{i}")
            badge_text = str(i - 1)
            self.assertIn(badge_text, p.get_text(), f"Page {i} missing badge number {badge_text}")

if __name__ == "__main__":
    unittest.main()
