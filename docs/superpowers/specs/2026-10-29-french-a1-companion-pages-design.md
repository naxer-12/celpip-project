# Specification: French A1 Vocabulary Enriched Companion Edition

**Date:** 2026-10-29  
**Status:** Approved by User  
**Target Book:** `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf`  
**Output Book:** `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf`  

---

## 1. Executive Summary & Objective

The objective is to expand the existing 83-page curriculum book *Vocabulaire Essentiel du Français A1 (Édition Intégrale 33 Chapitres)* into an enriched, interactive 116-page master edition.

For every unit (Chapitres 01 to 33), a dedicated single-page **Immersion & Rétention Active** companion sheet is inserted directly underneath that unit (following page 2 of each chapter). Each companion sheet contextualizes the complete vocabulary of the unit inside a creative, realistic French story/dialogue and provides active recall exercises (contextual fill-ins, sentence builders, and discrimination tasks) to solidify retention.

---

## 2. Structural & Interleaving Architecture

### 2.1 Page Breakdown

* **Original Book (83 pages)**:
  * Pages 01–04: Front Matter (Cover, Welcome, Table of Contents, Pronunciation Super-Guide).
  * Pages 05–70: 33 Units $\times$ 2 pages per unit.
  * Pages 71–83: Back Matter (Grammar Engine, Master A1 French-English Glossary, Completion Certificate).
* **Enriched Edition (116 pages)**:
  * Pages 01–04: Front Matter preserved losslessly.
  * Pages 05–103: 33 Units $\times$ 3 pages per unit (Page 1: Content, Page 2: Original Self-Check Quiz, Page 3: **New Companion Page**).
  * Pages 104–116: Back Matter preserved losslessly.

### 2.2 Mathematical Mapping

For any Chapter $k \in [1, 33]$:
* Original Page 1: $P_{\text{orig}, 1}(k) = 2k + 3 \longrightarrow P_{\text{new}, 1}(k) = 3k + 2$
* Original Page 2: $P_{\text{orig}, 2}(k) = 2k + 4 \longrightarrow P_{\text{new}, 2}(k) = 3k + 3$
* **New Companion Page**: $P_{\text{new}, 3}(k) = 3k + 4$

---

## 3. Visual & Layout System (1-Page Guarantee)

Each companion sheet is built with semantic HTML5 and modern CSS Paged Media matching the aesthetic signature of the core book:

* **Page Dimensions:** US Letter (`8.5in` $\times$ `11.0in`), `@page { size: letter; margin: 0.40in; }`.
* **Typography:** Modern clean sans-serif stack (`system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`).
* **Color Palette:**
  * Primary Navy: `#1A365D` (hero header, table heads, section accents)
  * Gold / Accent: `#D97706` / `#B45309` (unit badges, key callouts)
  * Background Tint: `#F8FAFC` (card bodies)
  * Border Tone: `#E2E8F0` / `#CBD5E0`
  * Text Body: `#1E293B`
* **Layout Structure (Strict 1-Page Box Model):**
  1. **Unit Header Banner (Height ~48px):** Chapter number, French title, English subtitle, and *Fiche d'Immersion & Consolidation*.
  2. **Partie A — Immersion Contextuelle & Récit Vivant (~42% of page):**
     * Engaging real-world scenario (dialogue or narrative).
     * Every key vocabulary item and collocation is embedded naturally in bold navy font (`<b>...</b>`).
     * Mini bilingual annotations / marginal notes explaining cultural nuances or idioms.
  3. **Partie B — Exercices d'Ancrage Cognitif & Mémorisation (~44% of page):**
     * **Exercice 1 — Complétion Contextuelle (Gap-fill):** 3 situational prompts requiring active recall of chapter terms.
     * **Exercice 2 — Défi Créatif / Production Guidée (Sentence-Building):** Formulate authentic sentences connecting required vocabulary pairs.
     * **Exercice 3 — Chasse à l'Intrus ou Discrimination Grammaticale:** Critical thinking task identifying gender mismatches or thematic anomalies.
  4. **Auto-Correction & Barème (~10% of page):**
     * Compact, discreet answers at the bottom for autonomous checking.

---

## 4. Curricular Scope: 33 Units Breakdown

1. **Ch 01:** Greetings, everyday politeness, alphabet, introductions (*bonjour, enchanté, s'appeler, prénom*).
2. **Ch 02:** Numbers 0–100, months, seasons, birthdays, telephone (*âge, avoir... ans, date de naissance*).
3. **Ch 03:** Nationalities, countries, prepositions (*en, au, aux*), street addresses.
4. **Ch 04:** Body parts, physical sensations, stages of life (*la tête, les bras, l'enfance, adulte*).
5. **Ch 05:** Physical & moral descriptions, hair, eyes, colors, personality adjectives.
6. **Ch 06:** Five senses, emotions, moods, psychological states (*la joie, la peur, sentir*).
7. **Ch 07:** Nuclear & extended family, couple life, marital status (*époux, conjoint, parents*).
8. **Ch 08:** Sports, facilities, verbs *faire du* vs. *jouer à* (*football, natation, terrain*).
9. **Ch 09:** Cultural activities, cinema, museum, instruments (*musée, exposition, spectacle*).
10. **Ch 10:** Days of the week, daily parts, telling time (*midi, minuit, quart, demi*).
11. **Ch 11:** Daily routine, chores, reflexive verbs (*se réveiller, faire le ménage*).
12. **Ch 12:** French schooling system, levels, diplomas (*collège, lycée, université, examen*).
13. **Ch 13:** School stationery, classroom materials, academic subjects (*stylo, cahier, trousse*).
14. **Ch 14:** Professions, corporate settings, work routines (*bureau, collègue, entreprise*).
15. **Ch 15:** House, apartment, rooms, leasing, architecture (*chambre, cuisine, salon, louer*).
16. **Ch 16:** Furniture, interior appliances, home equipment (*canapé, armoire, réfrigérateur*).
17. **Ch 17:** Public transit, bus, metro, ticketing, railway stations (*gare, quai, billet, correspondance*).
18. **Ch 18:** Private driving, vehicles, traffic rules (*voiture, permis, autoroute, rond-point*).
19. **Ch 19:** Tourism, vacation planning, weather, climates (*météo, valise, monuments, soleil*).
20. **Ch 20:** Hotels, camping, gîtes, amenities, reservations (*chambre double, tente, clé*).
21. **Ch 21:** Fruits, vegetables, open-air farmers markets (*pommes, carottes, maraîcher, kilo*).
22. **Ch 22:** Meats, poultry, seafood, eggs, grains, bakery (*boucherie, poissonnerie, pain, farine*).
23. **Ch 23:** Dairy products, cheeses, beverages, wines (*fromage, yaourt, lait, eau minérale*).
24. **Ch 24:** Meal times, culinary habits, setting the table (*assiette, fourchette, couteau, dîner*).
25. **Ch 25:** Bistro culture, restaurant menus, ordering meals (*serveur, carte, addition, plat*).
26. **Ch 26:** Errands, boutique shopping, supermarket aisles (*caddie, caisse, magasin, prix*).
27. **Ch 27:** Clothing, shoes, fabrics, fitting rooms, style (*pantalon, robe, taille, essayer*).
28. **Ch 28:** Illnesses, doctor visits, symptoms, aches (*avoir mal à..., fièvre, rhume, toux*).
29. **Ch 29:** Medical specialists, hospital, pharmacy (*ordonnance, médecin, infirmier, clinique*).
30. **Ch 30:** City landmarks, public services, navigation (*poste, mairie, carrefour, tout droit*).
31. **Ch 31:** Countryside, flora, domestic & wild animals (*forêt, rivière, vache, oiseau*).
32. **Ch 32:** Digital tools, smartphones, email, postal services (*ordinateur, mot de passe, colis, timbre*).
33. **Ch 33:** Administrative procedures, prefecture, residence permits (*titre de séjour, formulaire, CAF*).

---

## 5. Technical Pipeline & Implementation Architecture

1. **Extraction & Database Builder (`build_companion_data.py`):**
   * Reads `chapters_extracted.json` and `chapters_batch_1..3.json`.
   * Assembles a structured JSON database (`companion_chapters.json`) containing rich scenarios, vocabulary word banks, and targeted exercises for all 33 units.
2. **HTML Page Generator (`render_companion_pages.py`):**
   * Generates a single unified HTML document with CSS `@page { size: letter; margin: 0.40in; }` and `.page-break` between units.
   * Compiles the 33 pages into a temporary 33-page PDF via Headless Chrome:
     `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf=<temp_pdf> <html_file>`
3. **Interleaving & Lossless Assembly (`assemble_enriched_edition.py`):**
   * Reads original PDF (83 pages) and companion PDF (33 pages) via `pypdf.PdfReader`.
   * Assembles pages in sequence:
     * Pages 1–4 from Original
     * For each unit $k \in [1, 33]$:
       * Unit $k$ Original Page 1
       * Unit $k$ Original Page 2
       * Unit $k$ Companion Page (from companion PDF)
     * Pages 71–83 from Original
   * Writes to `/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf`.
4. **Verification Script (`verify_enriched_edition.py`):**
   * Validates total page count is exactly 116.
   * Validates every unit contains 3 pages (Page 1 = Intro, Page 2 = Quiz, Page 3 = Immersion Companion).
   * Validates no content cutoffs or visual overlaps.

---

## 6. Spec Self-Review Checklist

* [x] **Placeholder scan:** No TBD, TODO, or vague statements.
* [x] **Internal consistency:** Page count math ($4 + 33 \times 3 + 13 = 116$) is consistent across all sections.
* [x] **Scope check:** Strictly covers all 33 units of French A1 vocabulary companion pages and produces the new enriched PDF.
* [x] **Ambiguity check:** File paths, output names, and exact interleaving formulas are mathematically defined.
