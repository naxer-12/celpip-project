import unittest
import os
import re
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
            soup = BeautifulSoup(content, "html.parser")
            text = soup.get_text()

        # Verify distinctive keywords across modules
        self.assertIn("Overall Objectives of A2 Level", text)
        self.assertIn("Real-Life Outcomes at CEFR A2", text)
        self.assertIn("A2 French – Core Communicative Functions", text)
        self.assertIn("A2 Grammar: Nouns, Gender Rules & Plural Patterns", text)
        self.assertIn("A2 Thematic Vocabulary: Biography & Life Milestones", text)
        self.assertIn("A2 Speaking Mastery: Continuous Monologue", text)
        self.assertIn("B1 Transition Benchmark", text)
        self.assertIn("Félicitations pour votre parcours", text)

        # Verify proper HTML escaping of ampersands in markup
        self.assertIn("A2 Grammar: Nouns, Gender Rules &amp; Plural Patterns", content)
        self.assertIn("Roadmap &amp; Checklist", content)

    def test_badge_numbers(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")

        # Verify .page-badge CSS positioning within page bounds (902px x 1166px)
        badge_css_match = re.search(r'\.page-badge\s*\{([^}]+)\}', content)
        self.assertIsNotNone(badge_css_match, ".page-badge CSS rule missing")
        badge_css = badge_css_match.group(1)

        m_left = re.search(r'left:\s*([\d\.]+)px', badge_css)
        m_top = re.search(r'top:\s*([\d\.]+)px', badge_css)
        self.assertIsNotNone(m_left, ".page-badge missing left coordinate")
        self.assertIsNotNone(m_top, ".page-badge missing top coordinate")
        left_val = float(m_left.group(1))
        top_val = float(m_top.group(1))
        self.assertGreaterEqual(left_val, 0.0)
        self.assertLessEqual(left_val, 902.0)
        self.assertGreaterEqual(top_val, 0.0)
        self.assertLessEqual(top_val, 1166.0)

        # Verify all pages 2..71 badge DOM structure and values
        for i in range(2, 72):
            p = soup.find(id=f"page{i}")
            badge_div = p.find("div", class_="page-badge")
            self.assertIsNotNone(badge_div, f"Page {i} missing .page-badge element")
            expected_num = str(i - 1)
            self.assertEqual(badge_div.get_text().strip(), expected_num, f"Page {i} badge text mismatch")

            # Verify no nested child spans with absolute coordinates causing double offsets
            nested_abs = badge_div.find_all(lambda tag: tag.has_attr("style") and "left:" in tag["style"])
            self.assertEqual(len(nested_abs), 0, f"Page {i} badge has nested element with duplicate offset style")
            nested_spans_a = badge_div.find_all("span", class_="a")
            self.assertEqual(len(nested_spans_a), 0, f"Page {i} badge has child span.a causing double offset")

if __name__ == "__main__":
    unittest.main()
