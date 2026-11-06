# Remove Brand Logo & Structure Resources for A2–C2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove "The Language Network" brand logo completely from all 6 CEFR roadmaps (A1–C2), eliminate any visual overlapping of words/images, and integrate a comprehensive structured learning resources section (Module 7: Pages 53–67) for levels A2 through C2 modeled after A1's reference architecture.

**Architecture:** 
1. Clean the master raw background images `1.jpg`–`71.jpg` in `scribd_raw/images/` and level cover images by seamlessly removing "The Language Network" logo (filling the cover top tab with matching background color and pages 2–71 top coordinates `(360, 40, 545, 135)` with pure white `#FFFFFF`).
2. Synthesize curated, CEFR-aligned structured resource datasets (books, audio series, podcasts, YouTube channels, apps, official DELF/DALF exam practice) for French A2, B1, B2, C1, and C2 across pages 53–67.
3. Update HTML generators with a card-based CSS structure (`background: #ffffff; border-radius: 8px;`) ensuring zero text-image collision or layout overlap.
4. Recompile all 6 master PDFs (71 pages each, `677.04 x 875.04 pts`), run visual and unit test verifications, re-split into modular units and single worksheets, and deliver to `output/` and Desktop.

**Tech Stack:** Python 3 (Pillow, pypdf), Chrome Headless (`--print-to-pdf`), pdftoppm, HTML5/CSS3.

## Global Constraints
- Strictly 71 pages per roadmap (426 pages total across all 6 levels).
- Standard page dimensions `677.04 x 875.04 pts` (`902px x 1166px`).
- Zero brand logo of "The Language Network" anywhere in any PDF.
- Zero overlapping between text, background graphics, or letters.
- Preserve all existing high-quality curriculum content for Modules 1–6 (pages 1–52) and Module 8 (pages 68–71).

---

### Task 1: Remove "The Language Network" Logo from Master Background Images & Covers

**Files:**
- Modify: `scribd_raw/images/1.jpg` through `71.jpg`
- Modify: `French_A1/French_Learning_Roadmap_Checklist_French_A1.html`
- Modify: `French_A2/build_a2_cover.py`, `French_B1/build_b1_cover.py`, `French_B2/build_b2_cover.py`, `French_C1/build_c1_cover.py`, `French_C2/build_c2_cover.py`

- [ ] **Step 1: Clean raw images 1.jpg to 71.jpg**
  Write and run a Python script to:
  - Fill rectangle `(350, 0, 555, 95)` on `1.jpg` with sky blue `(117, 203, 230)` removing the top tab logo.
  - Fill rectangle `(360, 40, 545, 135)` on `2.jpg` to `71.jpg` with pure white `#FFFFFF`.
  - For pages 53 to 67 in `scribd_raw/images/`, create clean white canvases so no old A1 screenshots bleed into A2–C2.

- [ ] **Step 2: Regenerate level covers without logo**
  Run cover generators (`build_a2_cover.py`, `build_b1_cover.py`, `build_b2_cover.py`, `build_c1_cover.py`, `build_c2_cover.py`) to produce updated `1_a2.jpg`, `1_b1.jpg`, `1_b2.jpg`, `1_c1.jpg`, `1_c2.jpg`. Copy to each level's `scribd_raw/images/`.

- [ ] **Step 3: Update French A1 HTML and recompile A1 PDF**
  Replace base64 image data URIs in `French_A1/French_Learning_Roadmap_Checklist_French_A1.html` with cleaned images. Compile `French_A1.pdf` via Chrome headless.

- [ ] **Step 4: Verify logo removal**
  Render pages 1 and 2 of A1 and A2 with `pdftoppm` and inspect to verify zero logo remnants.

---

### Task 2: Synthesize Structured Resource Datasets for A2, B1, B2, C1, and C2

**Files:**
- Modify: `French_A2/a2_curriculum_data.py` (pages 53–67)
- Modify: `French_B1/b1_curriculum_data.py` (pages 53–67)
- Modify: `French_B2/b2_curriculum_data.py` (pages 53–67)
- Modify: `French_C1/c1_curriculum_data.py` (pages 53–67)
- Modify: `French_C2/c2_curriculum_data.py` (pages 53–67)

- [ ] **Step 1: Define structured resource schema**
  Format each resource entry with `name`, `platform`, `url`, `focus`, `features`, `recommendation`, and `status`.

- [ ] **Step 2: Synthesize A2 Resources (Pages 53–67)**
  Add TV5Monde A2, RFI français facile, Coffee Break French Season 2, Duolingo French Stories, Easy French A2, Français avec Pierre A2, CLE Grammaire Progressive A2, Le DELF A2 100% Réussite, Anki A2 1500 words.

- [ ] **Step 3: Synthesize B1 Resources (Pages 53–67)**
  Add TV5Monde B1, innerFrench podcast, Journal en français facile, Transfert, French School TV, CLE Grammaire Progressive Intermédiaire, Édito B1, DELF B1 past papers.

- [ ] **Step 4: Synthesize B2 Resources (Pages 53–67)**
  Add TV5Monde B2, Géopolitique Le Monde, Affaires Sensibles, HugoDécrypte, Karambolage, CLE Grammaire Avancé, Édito B2, DELF B2 prep, Le Robert/Antidote.

- [ ] **Step 5: Synthesize C1 Resources (Pages 53–67)**
  Add France Culture, France Inter, Le Monde diplomatique, Thinkerview, Usul, Blast, CLE Perfectionnement, DALF C1 100% Réussite, CNRTL, synthèse de documents guides.

- [ ] **Step 6: Synthesize C2 Resources (Pages 53–67)**
  Add Collège de France lectures, Répliques (France Culture), NRF, Académie Française, Grevisse Le Bon Usage, DALF C2 100% Réussite, Pléiade editions, argumentation & stylistique mastery.

---

### Task 3: Implement Card-Based Zero-Overlap Layout in HTML Generators

**Files:**
- Modify: `French_A2/build_a2_html.py`
- Modify: `French_B1/build_b1_html.py`
- Modify: `French_B2/build_b2_html.py`
- Modify: `French_C1/build_c1_html.py`
- Modify: `French_C2/build_c2_html.py`

- [ ] **Step 1: Add `.resource-card` CSS styles**
  Define `.resource-card` with solid white background, neat border, accent header tag, structured key-value lines, and compact spacing.

- [ ] **Step 2: Add `render_resource_page` layout handler**
  Render pages 53–67 cleanly as structured resources, guaranteeing content fits perfectly in `1166px` height with zero overlapping.

- [ ] **Step 3: Generate HTML files for A2, B1, B2, C1, C2**
  Run builders to regenerate all HTML files.

---

### Task 4: Recompile All 6 PDFs & Visual Verification

**Files:**
- Recompile: `French_A1.pdf`, `French_A2.pdf`, `French_B1.pdf`, `French_B2.pdf`, `French_C1.pdf`, `French_C2.pdf`

- [ ] **Step 1: Compile all 6 PDFs via Chrome headless**
- [ ] **Step 2: Verify page count (71 pages) and geometry (677.04 x 875.04 pts)**
- [ ] **Step 3: Render and inspect visual snapshots (pages 1, 2, 54, 57, 65) across all 6 levels**

---

### Task 5: Update Markdown Checklists and Run Unit Test Suites

**Files:**
- Modify: `French_A2_...md`, `French_B1_...md`, `French_B2_...md`, `French_C1_...md`, `French_C2_...md`
- Run: `test_a1.py`, `test_a2_curriculum.py`, `test_b1.py`, `test_b2.py`, `test_c1.py`, `test_c2.py`

- [ ] **Step 1: Regenerate Markdown checklists**
- [ ] **Step 2: Update and run all unit test suites (assert 100% passing)**

---

### Task 6: Re-Split Master PDFs and Deliver to Desktop

**Files:**
- Modify/Run: `split_roadmaps.py`
- Deliver: `output/` and `/Users/jainamshah/Desktop/French Material/French_Roadmaps_Complete_A1_to_C2_Split/`

- [ ] **Step 1: Execute split_roadmaps.py across all 6 levels**
- [ ] **Step 2: Copy updated master PDFs to output/ and desktop**
- [ ] **Step 3: Verify all 48 modular units and 426 worksheets exist and match specifications**
