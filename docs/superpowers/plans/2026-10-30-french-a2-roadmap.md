# French A2 Learning Roadmap & Checklist Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Synthesize and generate the complete 71-page French A2 Learning Roadmap & Checklist as an exact visual replica of the A1 companion, delivering `French_Learning_Roadmap_Checklist_French_A2.pdf`, `French_Learning_Roadmap_Checklist_French_A2.html`, and `French_A2_Learning_Roadmap_Checklist.md`.

**Architecture:** A Python-based curriculum engine defines all 71 pages of structured CEFR A2 curriculum content, an HTML compiler injects this into 1:1 scaled templates with base64 embedded WOFF2 fonts and background templates, and headless Chromium prints the PDF via CDP `Page.printToPDF` with `preferCSSPageSize: true`. A Markdown generator produces the comprehensive text companion.

**Tech Stack:** Python 3, BeautifulSoup4, PIL (Pillow), Ego-Browser Node.js (CDP `Page.printToPDF`), Poppler (`pdfinfo`, `pdftoppm`).

**Spec:** `/Users/jainamshah/Downloads/Learning French/docs/superpowers/specs/2026-10-30-french-a2-roadmap-design.md`

## Global Constraints
- Page dimensions: strictly 902px width by 1166px height (677.04pt x 875.04pt) with 0 margin.
- Total page count: exactly 71 pages (no blank pages, no overflow).
- Visual branding: "THE LANGUAGE NETWORK" emblem, rounded aqua checkboxes (`#48b3b6`), seafoam table headers (`#d1ecee`), solid dark borders (1.5px `#1a1a1a`), teal page badges.
- Coordinates: 1:1 unscaled CSS coordinates (`transform: none` on text layer, pre-scaled fonts, widths, and negative letter margins).
- Curriculum level: CEFR A2 (Waystage / Elementary) covering 1,500–2,000 words, dual-past narration, future projection, polite conditional, relative and object pronouns, 4-skills checklists, and B1 readiness audit.

---

### Task 1: Complete A2 Curriculum Data Architecture (`a2_curriculum_data.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/a2_curriculum_data.py`
- Test: `/Users/jainamshah/Downloads/Learning French/test_a2_curriculum_data.py`

**Interfaces:**
- Produces: `A2_PAGES_DATA: dict[int, dict]` mapping page numbers `1` through `71` to their pedagogical content:
  - `page`: integer (1 to 71)
  - `badge_num`: integer or string (e.g. "1" to "70" for display in footer badge)
  - `title`: primary page title string
  - `subtitle`: optional section subtitle
  - `intro`: optional narrative / introductory paragraph
  - `type`: page type (`"cover"`, `"objectives"`, `"themes_table"`, `"functions_table"`, `"checklist"`, `"vocab_table"`, `"skills"`, `"audit"`)
  - `items`: list of checklist bullet strings (for checklist/skills/audit pages)
  - `sections`: list of sub-sections with title and items
  - `table`: optional dict with `headers: list[str]` and `rows: list[list[str]]` (for table pages)

- [ ] **Step 1: Write the failing test**

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_a2_curriculum_data.py`
Expected: FAIL with `ModuleNotFoundError: No module named 'a2_curriculum_data'`

- [ ] **Step 3: Implement `a2_curriculum_data.py`**

Create `a2_curriculum_data.py` containing complete, rigorous CEFR A2 curriculum content for all 71 pages:
- Page 1: Cover ("French Learning Roadmap & Checklist", "French A2")
- Pages 2–3: Overall Objectives of A2 Level (Elementary / Waystage) — Speaking, Writing, Listening, Reading
- Pages 4–6: Core Themes & Real-Life Outcomes Tables 1, 2, and 3 (Themes 1–14)
- Page 7: Core Communicative Functions & Authentic Sentences
- Pages 8–19: Grammar Foundation Master Checklist (Nouns/Plurals, Articles/Quantifiers, COD/COI, Y & En / Relative Pronouns, BANGS & Comparisons, Complex Negation, Question Forms, Prepositions of Time/Space, Passé Composé Deep Dive, Imparfait & Interrupted Past, Futur Simple vs Proche, Conditionnel de Politesse & Modals)
- Pages 20–29: 10 Thematic Vocabulary Modules (Biography/Milestones, Housing/Rentals, Household Routine, Gastronomy/Bistro, Shopping/Transactions, Urban Transit, Travel/Bookings, Health/Pharmacy, Professional World/Work, Media/Ecology)
- Pages 30–67: 4-Skills Mastery Checklists (Spoken Monologues, Simulated Dialogues, Debating/Opinions, Phone Skills, Public Announcements, Counter Exchanges, Voicemails, Realia Reading, Menus, Letters/Postcards, Formal Emails, Phonetics/Liaisons, Sociocultural Etiquette)
- Pages 68–71: Diagnostic Assessment & "Ready for B1" Final Audit.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 test_a2_curriculum_data.py`
Expected: PASS (all 71 pages validated, all assertions succeed)

- [ ] **Step 5: Commit**

```bash
git add a2_curriculum_data.py test_a2_curriculum_data.py
git commit -m "feat(curriculum): synthesize complete 71-page CEFR A2 curriculum dataset"
```

---

### Task 2: Cover Art & Template Preparation (`build_a2_cover.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/build_a2_cover.py`
- Test: `/Users/jainamshah/Downloads/Learning French/test_a2_cover.py`
- Produces: `/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1_a2.jpg`

**Interfaces:**
- Consumes: `/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1.jpg`
- Produces: `scribd_raw/images/1_a2.jpg` with the pill updated from "French A1" to "French A2" matching the original royal blue pill geometry (`(365, 324, 538, 376)`).

- [ ] **Step 1: Write the failing test**

```python
# test_a2_cover.py
import unittest, os
from PIL import Image

class TestA2Cover(unittest.TestCase):
    def test_cover_image_exists_and_dimensions(self):
        cover_path = "/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1_a2.jpg"
        self.assertTrue(os.path.exists(cover_path), "1_a2.jpg does not exist")
        im = Image.open(cover_path)
        self.assertEqual(im.size, (904, 1169))

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_a2_cover.py`
Expected: FAIL with `AssertionError: 1_a2.jpg does not exist`

- [ ] **Step 3: Implement `build_a2_cover.py`**

Write script that loads `scribd_raw/images/1.jpg`, renders the updated "French A2" badge matching the exact color palette, rounded rectangle corner radius, and crisp typography, and saves to `scribd_raw/images/1_a2.jpg`.

```python
# build_a2_cover.py
import os
from PIL import Image, ImageDraw, ImageFont

def generate_a2_cover():
    src_path = "/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1.jpg"
    dst_path = "/Users/jainamshah/Downloads/Learning French/scribd_raw/images/1_a2.jpg"
    im = Image.open(src_path).convert("RGB")
    draw = ImageDraw.Draw(im)
    
    # Coordinates of the pill badge: x1=365, y1=324, x2=538, y2=376
    # Royal blue background: #2f80ed or sampled from original #236db6
    pill_box = (365, 324, 538, 376)
    draw.rounded_rectangle(pill_box, radius=10, fill="#2572be")
    
    # Try finding standard bold font
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Trebuchet MS Bold.ttf", 34)
    except:
        font = ImageFont.load_default()
        
    text = "French A2"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    text_x = pill_box[0] + (pill_box[2] - pill_box[0] - text_w) / 2
    text_y = pill_box[1] + (pill_box[3] - pill_box[1] - text_h) / 2 - 2
    
    draw.text((text_x, text_y), text, fill="#ffffff", font=font)
    im.save(dst_path, quality=95)
    print("Generated:", dst_path)

if __name__ == "__main__":
    generate_a2_cover()
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 build_a2_cover.py && python3 test_a2_cover.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add build_a2_cover.py test_a2_cover.py scribd_raw/images/1_a2.jpg
git commit -m "feat(cover): create high-resolution French A2 cover artwork"
```

---

### Task 3: HTML Builder Engine (`build_a2_html.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/build_a2_html.py`
- Test: `/Users/jainamshah/Downloads/Learning French/test_a2_html.py`
- Produces: `/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.html`

**Interfaces:**
- Consumes: `a2_curriculum_data.py` (`A2_PAGES_DATA`), `scribd_raw/images/`, `scribd_raw/fonts/`, `scribd_fonts.json`
- Produces: `French_Learning_Roadmap_Checklist_French_A2.html` containing 71 fully styled, self-contained `.newpage` divs.

- [ ] **Step 1: Write the failing test**

```python
# test_a2_html.py
import unittest, os
from bs4 import BeautifulSoup

class TestA2HTML(unittest.TestCase):
    def setUp(self):
        self.html_path = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.html"

    def test_file_exists_and_size(self):
        self.assertTrue(os.path.exists(self.html_path), "A2 HTML file missing")
        self.assertGreater(os.path.getsize(self.html_path), 2 * 1024 * 1024, "HTML file too small (<2MB)")

    def test_all_71_pages_present(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        pages = soup.find_all("div", class_="newpage")
        self.assertEqual(len(pages), 71)
        for i in range(1, 72):
            p = soup.find(id=f"page{i}")
            self.assertIsNotNone(p, f"page{i} div missing")

    def test_print_css_present(self):
        with open(self.html_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("@page", content)
        self.assertIn("size: 902px 1166px", content)
        self.assertIn("French Learning Roadmap & Checklist", content)
        self.assertIn("French A2", content)

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_a2_html.py`
Expected: FAIL with `AssertionError: A2 HTML file missing`

- [ ] **Step 3: Implement `build_a2_html.py`**

Write `build_a2_html.py`:
1. Embeds all 193 WOFF2 fonts from `scribd_raw/fonts/` as base64 data URIs.
2. Injects the scaled kerning and spacing rules (`.w1` to `.w39` widths, `.l1` to `.l39` margins).
3. Embeds background images `1_a2.jpg` (page 1) and `2.jpg`–`71.jpg` (pages 2–71) as base64 data URIs.
4. Generates the 1:1 scaled text layers for all 71 pages using the curriculum data from `a2_curriculum_data.py`.
5. Formats headings, intro text, checklist bullets with exact typography and vertical alignments, table cells with seafoam headers and solid borders, and bottom-right page badge numbers.
6. Writes to `French_Learning_Roadmap_Checklist_French_A2.html`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 build_a2_html.py && python3 test_a2_html.py`
Expected: PASS (71 `.newpage` containers generated, correct CSS, file size > 3MB)

- [ ] **Step 5: Commit**

```bash
git add build_a2_html.py test_a2_html.py
git commit -m "feat(html): build complete 71-page French A2 standalone HTML generator"
```

---

### Task 4: Headless Chromium PDF Compilation (`compile_a2_pdf.js`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/compile_a2_pdf.js`
- Test: `/Users/jainamshah/Downloads/Learning French/test_a2_pdf.py`
- Produces: `/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf`

**Interfaces:**
- Consumes: `/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.html`
- Produces: `/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf` (exact 71 pages, 902x1166px / 677.04x875.04pt).

- [ ] **Step 1: Write the failing test**

```python
# test_a2_pdf.py
import unittest, os, subprocess

class TestA2PDF(unittest.TestCase):
    def setUp(self):
        self.pdf_path = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf"

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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_a2_pdf.py`
Expected: FAIL with `AssertionError: A2 PDF does not exist`

- [ ] **Step 3: Implement `compile_a2_pdf.js`**

Write node script to execute via ego-browser nodejs:
```javascript
// compile_a2_pdf.js
const task = await taskSpace("render A2 pdf");
const page = task.page("p1");
const htmlPath = "file:///Users/jainamshah/Downloads/Learning%20French/French_Learning_Roadmap_Checklist_French_A2.html";
console.log("Loading A2 HTML...");
await page.goto(htmlPath, { timeout: 30000 });
console.log("Waiting for fonts...");
await page.evaluate(() => document.fonts.ready);
console.log("Printing to PDF...");
const pdfData = await page.cdp("Page.printToPDF", {
  printBackground: true,
  preferCSSPageSize: true,
  marginTop: 0,
  marginBottom: 0,
  marginLeft: 0,
  marginRight: 0
});
const fs = await import("node:fs/promises");
const outPath = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf";
await fs.writeFile(outPath, Buffer.from(pdfData.data, "base64"));
console.log("PDF created successfully at:", outPath);
await task.finish({ keep: [] });
```

- [ ] **Step 4: Run compilation and test to verify it passes**

Run:
```bash
ego-browser nodejs < compile_a2_pdf.js
python3 test_a2_pdf.py
```
Expected: PASS (PDF exists, exactly 71 pages, 677.04 x 875.04 pts, size > 2MB)

- [ ] **Step 5: Commit**

```bash
git add compile_a2_pdf.js test_a2_pdf.py
git commit -m "feat(pdf): compile 71-page French A2 PDF via CDP Page.printToPDF"
```

---

### Task 5: Markdown Reference Document (`generate_a2_markdown.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/generate_a2_markdown.py`
- Test: `/Users/jainamshah/Downloads/Learning French/test_a2_markdown.py`
- Produces: `/Users/jainamshah/Downloads/Learning French/French_A2_Learning_Roadmap_Checklist.md`

**Interfaces:**
- Consumes: `a2_curriculum_data.py` (`A2_PAGES_DATA`)
- Produces: `French_A2_Learning_Roadmap_Checklist.md`

- [ ] **Step 1: Write the failing test**

```python
# test_a2_markdown.py
import unittest, os

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

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 test_a2_markdown.py`
Expected: FAIL with `AssertionError: A2 Markdown file missing`

- [ ] **Step 3: Implement `generate_a2_markdown.py`**

Write script to format `A2_PAGES_DATA` into standard markdown with checkboxes (`- [ ]`), tables, headers, and descriptions, and write to `French_A2_Learning_Roadmap_Checklist.md`.

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 generate_a2_markdown.py && python3 test_a2_markdown.py`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add generate_a2_markdown.py test_a2_markdown.py French_A2_Learning_Roadmap_Checklist.md
git commit -m "docs(curriculum): generate French A2 markdown reference and checklist companion"
```

---

### Task 6: Visual Quality Audit & Multi-Page Verification

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/verify_a2_pages.py`
- Produces: Temporary PNG renders of Pages 1, 4, 16, 25, 30, 50, 71 for visual inspection.

**Interfaces:**
- Consumes: `/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf`
- Validates: Typography legibility, checkbox alignment, table cell wrapping, absence of character collision.

- [ ] **Step 1: Write `verify_a2_pages.py` to extract PNGs**

```python
# verify_a2_pages.py
import subprocess, os

SAMPLE_PAGES = [1, 4, 16, 25, 30, 50, 71]
pdf_path = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf"
out_dir = "/tmp/a2_verify"
os.makedirs(out_dir, exist_ok=True)

for p in SAMPLE_PAGES:
    prefix = f"{out_dir}/page_{p}"
    cmd = ["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p), pdf_path, prefix]
    subprocess.run(cmd, check=True)
    print(f"Rendered sample page {p}")
```

- [ ] **Step 2: Run `verify_a2_pages.py`**

Run: `python3 verify_a2_pages.py`
Expected: Generates `/tmp/a2_verify/page_1-01.png`, `page_4-04.png`, `page_16-16.png`, etc.

- [ ] **Step 3: Visual audit with `read_file`**

Inspect each extracted PNG:
- Page 1: Verify title "French Learning Roadmap & Checklist" and "French A2" pill badge.
- Page 4: Verify Core Themes table formatting and Real-Life Outcomes checkmarks.
- Page 16: Verify Passé Composé grammar rules, DR & MRS VANDERTRAMP, and agreement checklists.
- Page 25: Verify Urban Transit vocabulary table alignment.
- Page 30: Verify Speaking Production checklist and classroom background artwork.
- Page 50: Verify Reading Comprehension culture schedule and typography.
- Page 71: Verify "Ready to move to B1" audit criteria and bottom page badge `70`.

- [ ] **Step 4: Commit**

```bash
git add verify_a2_pages.py
git commit -m "test(visual): add sample page extraction and visual verification script"
```
