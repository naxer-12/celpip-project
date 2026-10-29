#!/usr/bin/env python3
"""
Unit test for validating companion_data.json schema and pedagogical content.
Tests that all 33 chapters are present, complete, and structurally sound.
"""

import json
import os
import unittest

COMPANION_DATA_PATH = os.path.join(os.path.dirname(__file__), "companion_data.json")


class TestCompanionData(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_path = COMPANION_DATA_PATH
        if os.path.exists(cls.file_path):
            with open(cls.file_path, "r", encoding="utf-8") as f:
                cls.data = json.load(f)
        else:
            cls.data = None

    def test_file_exists(self):
        self.assertTrue(
            os.path.exists(self.file_path),
            f"Expected {self.file_path} to exist."
        )

    def test_json_valid_and_complete(self):
        self.assertIsNotNone(self.data, f"Cannot test contents because {self.file_path} is missing.")
        self.assertIsInstance(self.data, dict, "companion_data.json root must be a dictionary.")
        self.assertEqual(len(self.data), 33, f"Expected exactly 33 chapters, got {len(self.data)}.")

        expected_keys = {str(i) for i in range(1, 34)}
        self.assertEqual(set(self.data.keys()), expected_keys, "Keys must be strings '1' through '33'.")

    def test_all_33_chapters_detail(self):
        self.assertIsNotNone(self.data)
        for k in range(1, 34):
            key = str(k)
            with self.subTest(chapter=key):
                self.assertIn(key, self.data, f"Chapter {key} missing from companion_data.json")
                ch = self.data[key]

                # 1. ch_num
                self.assertEqual(ch.get("ch_num"), k, f"Chapter {key}: ch_num must equal {k}")

                # 2. Titles & Badges
                self.assertIsInstance(ch.get("title_fr"), str, f"Chapter {key}: title_fr must be string")
                self.assertTrue(len(ch.get("title_fr", "").strip()) > 0, f"Chapter {key}: title_fr is empty")

                self.assertIsInstance(ch.get("title_en"), str, f"Chapter {key}: title_en must be string")
                self.assertTrue(len(ch.get("title_en", "").strip()) > 0, f"Chapter {key}: title_en is empty")

                self.assertIsInstance(ch.get("theme_badge"), str, f"Chapter {key}: theme_badge must be string")
                self.assertTrue(len(ch.get("theme_badge", "").strip()) > 0, f"Chapter {key}: theme_badge is empty")

                # 3. Scenario & Context
                self.assertIsInstance(ch.get("scenario_title"), str, f"Chapter {key}: scenario_title must be string")
                self.assertTrue(len(ch.get("scenario_title", "").strip()) > 0, f"Chapter {key}: scenario_title empty")

                self.assertIsInstance(ch.get("scenario_context"), str, f"Chapter {key}: scenario_context must be string")
                self.assertTrue(len(ch.get("scenario_context", "").strip()) > 0, f"Chapter {key}: scenario_context empty")

                # 4. Dialogue / Story
                story = ch.get("dialogue_or_story")
                self.assertIsInstance(story, list, f"Chapter {key}: dialogue_or_story must be list")
                self.assertGreaterEqual(len(story), 4, f"Chapter {key}: dialogue_or_story should have >= 4 turns")

                for idx, turn in enumerate(story):
                    self.assertIsInstance(turn, dict, f"Chapter {key} line {idx}: turn must be a dict")
                    self.assertIn("speaker", turn, f"Chapter {key} line {idx}: missing speaker")
                    self.assertIn("fr", turn, f"Chapter {key} line {idx}: missing fr")
                    self.assertIn("en", turn, f"Chapter {key} line {idx}: missing en")
                    fr_text = turn["fr"]
                    self.assertTrue(len(fr_text.strip()) > 0, f"Chapter {key} line {idx}: fr text is empty")
                    self.assertTrue(len(turn["en"].strip()) > 0, f"Chapter {key} line {idx}: en text is empty")
                    # Tag balancing
                    self.assertEqual(fr_text.count("<b>"), fr_text.count("</b>"), f"Chapter {key} line {idx}: mismatched <b> tags")

                # 5. Cultural Tip
                tip = ch.get("cultural_tip")
                self.assertIsInstance(tip, str, f"Chapter {key}: cultural_tip must be string")
                self.assertTrue(len(tip.strip()) > 20, f"Chapter {key}: cultural_tip too short or empty")

                # 6. Exercise 1
                ex1 = ch.get("exercise_1")
                self.assertIsInstance(ex1, dict, f"Chapter {key}: exercise_1 must be dict")
                self.assertTrue(len(ex1.get("title", "").strip()) > 0, f"Chapter {key}: ex1 missing title")
                self.assertTrue(len(ex1.get("instruction", "").strip()) > 0, f"Chapter {key}: ex1 missing instruction")
                items1 = ex1.get("items")
                self.assertIsInstance(items1, list, f"Chapter {key}: ex1 items must be list")
                self.assertEqual(len(items1), 3, f"Chapter {key}: ex1 items count must be 3, got {len(items1)}")
                for item in items1:
                    self.assertTrue(len(item.strip()) > 0, f"Chapter {key}: ex1 item empty")
                    self.assertTrue("___" in item, f"Chapter {key}: ex1 item missing fill-in blank '___'")

                # 7. Exercise 2
                ex2 = ch.get("exercise_2")
                self.assertIsInstance(ex2, dict, f"Chapter {key}: exercise_2 must be dict")
                self.assertTrue(len(ex2.get("title", "").strip()) > 0, f"Chapter {key}: ex2 missing title")
                self.assertTrue(len(ex2.get("instruction", "").strip()) > 0, f"Chapter {key}: ex2 missing instruction")
                prompts2 = ex2.get("prompts")
                self.assertIsInstance(prompts2, list, f"Chapter {key}: ex2 prompts must be list")
                self.assertEqual(len(prompts2), 2, f"Chapter {key}: ex2 prompts count must be 2, got {len(prompts2)}")
                for p in prompts2:
                    self.assertTrue(len(p.strip()) > 0, f"Chapter {key}: ex2 prompt empty")

                # 8. Exercise 3
                ex3 = ch.get("exercise_3")
                self.assertIsInstance(ex3, dict, f"Chapter {key}: exercise_3 must be dict")
                self.assertTrue(len(ex3.get("title", "").strip()) > 0, f"Chapter {key}: ex3 missing title")
                self.assertTrue(len(ex3.get("instruction", "").strip()) > 0, f"Chapter {key}: ex3 missing instruction")
                items3 = ex3.get("items")
                self.assertIsInstance(items3, list, f"Chapter {key}: ex3 items must be list")
                self.assertEqual(len(items3), 3, f"Chapter {key}: ex3 items count must be 3, got {len(items3)}")
                for item in items3:
                    self.assertTrue(len(item.strip()) > 0, f"Chapter {key}: ex3 item empty")

                # 9. Answers
                answers = ch.get("answers")
                self.assertIsInstance(answers, str, f"Chapter {key}: answers must be string")
                self.assertTrue(len(answers.strip()) > 20, f"Chapter {key}: answers empty or too short")
                self.assertIn("Ex 1", answers, f"Chapter {key}: answers missing Ex 1 key")
                self.assertIn("Ex 2", answers, f"Chapter {key}: answers missing Ex 2 key")
                self.assertIn("Ex 3", answers, f"Chapter {key}: answers missing Ex 3 key")


if __name__ == "__main__":
    unittest.main()
