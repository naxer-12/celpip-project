# French A1 Vocabulary Enriched Companion Edition Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate 33 dedicated single-page immersion and active recall companion pages for all 33 units of French A1 vocabulary, and interleave them directly after each unit into `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf`, producing a new 116-page master edition at `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf`.

**Architecture:** A Python-driven modular pipeline extracts vocabulary and pedagogical assets for all 33 chapters (`chapters_extracted.json` + `chapters_batch_1..3.json`), synthesizes high-engagement creative scenarios and active-recall exercises formatted into a modern CSS Paged Media template, renders the 33 pages to PDF via macOS Headless Chrome, and losslessly interleaves each page after page 2 of each unit via `pypdf`.

**Tech Stack:** Python 3, `pypdf`, Headless Google Chrome (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`), HTML5/CSS3 Paged Media.

**Spec:** `docs/superpowers/specs/2026-10-29-french-a1-companion-pages-design.md`

## Global Constraints

- **Source PDF Path:** `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf` (83 pages, untouched).
- **Target PDF Path:** `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf` (exact 116 pages).
- **Page Dimensions:** US Letter (`8.5in` $\times$ `11.0in`), margins `0.40in`.
- **Layout Guarantee:** Every companion unit MUST fit strictly on 1 single page without vertical overflow.
- **Vocabulary Coverage:** 100% of target vocabulary terms for all 33 units must be incorporated into the creative narrative or exercises.
- **Palette:** Navy `#1A365D`, Gold `#D97706`, Slate `#64748B`, Dark text `#1E293B`, Tint `#F8FAFC`.

---

### Task 1: Complete 33-Chapter Companion Content Generator (`generate_companion_content.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/generate_companion_content.py`
- Create: `/Users/jainamshah/Downloads/Learning French/companion_data.json`
- Test: `/Users/jainamshah/Downloads/Learning French/test_companion_data.py`

**Interfaces:**
- Consumes: `/Users/jainamshah/Downloads/Learning French/chapters_extracted.json`, `chapters_batch_1.json`, `chapters_batch_2.json`, `chapters_batch_3.json`
- Produces: `companion_data.json` containing a dictionary mapping `'1'` through `'33'` with fields:
  ```json
  {
    "ch_num": 1,
    "title_fr": "Les présentations et les salutations",
    "title_en": "Greetings, Politeness & Identity",
    "theme_badge": "L'IDENTITÉ & LES RENCONTRES",
    "scenario_title": "Première Rencontre au Café de Flore",
    "scenario_context": "Paul rencontre Sophie pour la première fois à Paris.",
    "dialogue_or_story": [
      {"speaker": "Paul", "fr": "<b>Bonjour Madame</b> ! Excusez-moi...", "en": "Good morning ma'am! Excuse me..."},
      ...
    ],
    "cultural_tip": "En France, on salue toujours le personnel en entrant...",
    "exercise_1": {
      "title": "Exercice 1 — Complétion Contextuelle",
      "instruction": "Complétez avec le terme exact du chapitre :",
      "items": ["Comment vous vous _______________ ?", ...]
    },
    "exercise_2": {
      "title": "Exercice 2 — Défi Créatif",
      "instruction": "Rédigez deux phrases en utilisant les mots imposés :",
      "prompts": ["Utilisez 'enchanté' et 'prénom'...", ...]
    },
    "exercise_3": {
      "title": "Exercice 3 — Chasse à l'Intrus",
      "instruction": "Identifiez l'intrus et justifiez brièvement :",
      "items": ["Bonjour / Salut / Bonsoir / Signature (Intrus : ...)", ...]
    },
    "answers": "1. appelez | 2. ... | 3. Signature (terme administratif, les autres sont des salutations)"
  }
  ```

- [ ] **Step 1: Write test for companion data validation**
- [ ] **Step 2: Run test to verify it fails initially**
- [ ] **Step 3: Implement `generate_companion_content.py` covering all 33 units with full pedagogical richness**
- [ ] **Step 4: Execute generator and verify all 33 units exist in `companion_data.json`**
- [ ] **Step 5: Run tests and ensure 100% pass**

---

### Task 2: HTML/CSS Single-Page Template & Headless Chrome Rendering (`render_companion_pdf.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/render_companion_pdf.py`
- Create: `/Users/jainamshah/Downloads/Learning French/companion_pages.html`
- Create: `/Users/jainamshah/Downloads/Learning French/companion_pages.pdf`
- Test: `/Users/jainamshah/Downloads/Learning French/test_companion_pdf.py`

**Interfaces:**
- Consumes: `companion_data.json`
- Produces: `companion_pages.pdf` (exactly 33 pages, 1 per chapter, US Letter size)

- [ ] **Step 1: Write test checking `companion_pages.pdf` has exactly 33 pages and proper dimensions**
- [ ] **Step 2: Run test to verify failure**
- [ ] **Step 3: Implement `render_companion_pdf.py` using CSS Paged Media and Headless Chrome CLI**
- [ ] **Step 4: Render HTML and invoke Headless Chrome to generate `companion_pages.pdf`**
- [ ] **Step 5: Verify each page matches exact US Letter dimensions and fits strictly on 1 page per unit**

---

### Task 3: Lossless Interleaving & Assembly of 116-Page Master Edition (`assemble_enriched_edition.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/assemble_enriched_edition.py`
- Produce: `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf`
- Test: `/Users/jainamshah/Downloads/Learning French/test_assembly.py`

**Interfaces:**
- Consumes:
  - Original PDF: `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf` (83 pages)
  - Companion PDF: `/Users/jainamshah/Downloads/Learning French/companion_pages.pdf` (33 pages)
- Produces:
  - Enriched PDF: `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf` (116 pages)

- [ ] **Step 1: Write test for page interleaving logic and metadata preservation**
- [ ] **Step 2: Run test to verify failure**
- [ ] **Step 3: Implement `assemble_enriched_edition.py` with `pypdf`**
- [ ] **Step 4: Run assembly script and generate 116-page enriched edition**
- [ ] **Step 5: Run tests to verify the interleaved structure (every chapter has Page 1, Page 2, Companion Page)**

---

### Task 4: Complete Pipeline Verification & Quality Audit (`verify_enriched_edition.py`)

**Files:**
- Create: `/Users/jainamshah/Downloads/Learning French/verify_enriched_edition.py`

**Interfaces:**
- Validates the resulting 116-page PDF for:
  - Total page count = 116.
  - Non-empty text on every companion page.
  - Proper sequence: Chapitre $k$ on pages $3k+2, 3k+3, 3k+4$.
  - Original pages 1–4 and 104–116 preserved identically.

- [ ] **Step 1: Implement `verify_enriched_edition.py`**
- [ ] **Step 2: Run verification script and inspect stdout logs**
- [ ] **Step 3: Output clickable links and confirmation summary to user**
