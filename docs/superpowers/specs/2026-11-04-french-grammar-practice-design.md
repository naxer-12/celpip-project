# French Grammar Practice Workbook (A1–A2) Design Spec

## 1. Overview & Objective
This specification defines a minimalist, visually clean, typography-focused French grammar practice workbook.
The output format will be a self-contained, responsive, print-ready HTML document (`French_Grammar_Practice_A1_A2.html`) that can also be printed or converted directly to A4 PDF with exact millimeter page formatting.

---

## 2. Structural Requirements & Content Scope

### 2.1 Grammar Topics (4 Core Modules)
1. **Module 1: Les Articles & Les Déterminants**
   - Definite, indefinite, and partitive articles
   - Possessive and demonstrative adjectives
   - Negation transformations (*pas de*)
   - Prepositional contractions (*au, du*)
   - Geographic articles and omissions with professions

2. **Module 2: Les Temps Verbaux & Conjugaisons**
   - Present indicative (*-er*, regular *-ir*, and essential irregulars: *être, avoir, aller, faire, prendre, venir, pouvoir, vouloir*)
   - *Futur proche* (*aller* + infinitif)
   - Imperative mood for basic commands/directions
   - *Passé composé* with *avoir* and *être* (including past participle agreement)
   - *Imparfait* for descriptions, habitual actions, and contrast with *passé composé*

3. **Module 3: Les Prépositions**
   - Spatial prepositions (*sur, sous, devant, derrière, dans, entre, à côté de*)
   - Prepositions of destination and origin (*à, de* and contractions)
   - Geographic prepositions with countries and cities (*en, au, aux, à*)
   - Temporal and durational markers (*à, en, pendant, depuis, dans*)
   - Transportation prepositions (*en train* vs *à vélo*)
   - Common verb + preposition dependencies (*commencer à, décider de, s'intéresser à*)

4. **Module 4: Les Pronoms**
   - Subject pronouns (*je, tu, il, elle, on, nous, vous, ils, elles*)
   - Tonic / disjunctive pronouns (*moi, toi, lui, elle, nous, vous, eux, elles*)
   - Direct object pronouns (COD: *le, la, l', les*)
   - Indirect object pronouns (COI: *lui, leur*)
   - Relative pronouns (*qui* vs *que/qu'*)
   - Introduction to adverbial pronouns *en* (quantity) and *y* (locations)

### 2.2 Question Counts & CEFR Level Progression
- **Total Questions**: 80 questions across the entire document.
- **Per Topic Distribution**: Exactly 20 questions per topic.
  - **A1**: Exactly 10 questions per topic (Questions 1–10, 21–30, 41–50, 61–70)
  - **A2**: Exactly 10 questions per topic (Questions 11–20, 31–40, 51–60, 71–80)

### 2.3 Question Varieties & Formats
Every section contains an evenly rotated blend of 4 pedagogical formats:
1. **Fill-in-the-blank (`______`)**: A natural sentence with a blank requiring the appropriate grammatical element.
2. **Multiple choice**: Contextual sentence followed by 4 mutually distinct options (a, b, c, d).
3. **Error correction**: A natural communicative utterance containing a subtle, common learner error to identify and rewrite correctly.
4. **Short translation**: A contextual English communicative sentence to render into idiomatic French.

### 2.4 Tone & Realistic Scenarios
Every question is contextualized in real-life settings:
- Ordering in cafés, boulangeries, and bistros
- Sending emails to colleagues, teachers, or landlords
- Asking for directions, train schedules, and airport travel
- Describing vacation memories, weekend routines, and photos

---

## 3. Design & Typography Rules

### 3.1 Layout & Grid
- **Page Size**: A4 portrait standard (`210mm × 297mm`).
- **Margins**: Generous whitespace (`18mm` top/bottom, `18mm` left/right).
- **Single Column**: Uncluttered single-column reading flow with clean vertical rhythm.
- **Question Separators**: Subtle hairline rule (`border-bottom: 1px solid #f0f1f3;`) between questions with `12px` top/bottom padding.
- **Decorations**: Zero illustrations, zero heavy borders, zero shadows, zero colored card boxes. Visual hierarchy achieved strictly through typography, padding, and subtle badge accents.

### 3.2 Typography Hierarchy
- **Font Stack**: Clean modern sans-serif: `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.
- **Document Header**:
  - Title: 24pt, bold (`font-weight: 700`), letter-spacing `-0.025em`, dark slate (`#111827`).
  - Subtitle: 11pt, regular (`#6b7280`), brief pedagogical overview.
- **Section Headers**:
  - 16pt, semibold (`font-weight: 600`), letter-spacing `-0.015em`, color `#1f2937`, with a subtle category descriptor.
- **Question Body**:
  - Item number: 9.5pt, bold monospace/sans (`#6b7280`).
  - Question text: 10pt, regular, line-height `1.5`, color `#1f2937`.
  - Context / scenario tag: 8.5pt italic (`#9ca3af`) indicating setting (*Au marché*, *Au bureau*).
  - Multiple choice options: 9.5pt, clean horizontal or vertical list with subtle letter indicators (`a)`, `b)`, `c)`, `d)`).

### 3.3 CEFR Badge Design
- Compact pill badges (`border-radius: 9999px; font-size: 8pt; font-weight: 600; padding: 2px 7px; display: inline-block; letter-spacing: 0.04em;`):
  - **A1**: Background `#e6f4ea` (light mint green), Text `#137333` (deep forest green).
  - **A2**: Background `#e8f0fe` (light soft blue), Text `#1a73e8` (deep cobalt blue).

---

## 4. Answer Key Specification
- Located on the final page with a forced print page break (`page-break-before: always;`).
- Compact multi-column layout (4 columns on desktop/print for maximum space efficiency).
- Font size: 8.5pt, compact line-height.
- Entry structure:
  - `[Question #] [Correct Answer] — [Concise grammatical explanation]`
  - Example: `1. du — partitive masculine singular (beurre)`
  - Example: `32. sommes arrivés — passé composé with être (movement verb), masculine plural agreement`

---

## 5. File Deliverables & Verification
1. `French_Grammar_Practice_A1_A2.html`: Standalone, zero-dependency HTML file with embedded CSS, fully self-contained.
2. Verified print styles (`@media print`) ensuring crisp A4 page rendering without awkward orphans or widows (`break-inside: avoid;`).
3. Verification script to confirm exactly 80 questions (4 topics × 20 questions; 10 A1 + 10 A2 per topic) and 80 corresponding answer keys.
