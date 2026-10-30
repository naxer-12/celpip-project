# test_a2_curriculum_data.py
import unittest
from a2_curriculum_data import A2_PAGES_DATA

class TestA2CurriculumData(unittest.TestCase):
    def test_total_page_count(self):
        """Verify all 71 pages are defined."""
        self.assertEqual(len(A2_PAGES_DATA), 71)
        for pnum in range(1, 72):
            self.assertIn(pnum, A2_PAGES_DATA, f"Missing page {pnum}")

    def test_page_structures(self):
        """Verify that every page has valid title, badge_num, and content payload."""
        for pnum, data in A2_PAGES_DATA.items():
            self.assertEqual(data["page"], pnum)
            self.assertIn("type", data)
            self.assertIn("title", data)
            self.assertTrue(len(data["title"]) > 0, f"Page {pnum} title is empty")
            
            # Type specific checks
            if data["type"] == "checklist":
                self.assertTrue(len(data.get("items", [])) > 0 or len(data.get("sections", [])) > 0,
                                f"Checklist page {pnum} has no items")
            elif data["type"] in ("themes_table", "functions_table", "vocab_table"):
                self.assertIn("table", data)
                self.assertTrue(len(data["table"]["rows"]) > 0, f"Table page {pnum} has no rows")
            elif data["type"] == "audit":
                self.assertTrue(len(data.get("items", [])) > 0, f"Audit page {pnum} has no items")

    def test_key_a2_grammar_and_themes_present(self):
        """Verify core CEFR A2 topics exist in the dataset."""
        all_text = " ".join(str(v) for v in A2_PAGES_DATA.values())
        self.assertIn("passé composé", all_text.lower())
        self.assertIn("imparfait", all_text.lower())
        self.assertIn("futur simple", all_text.lower())
        self.assertIn("conditionnel", all_text.lower())
        self.assertIn("pronoms", all_text.lower())
        self.assertIn("ready to move to b1", all_text.lower())

if __name__ == "__main__":
    unittest.main()
