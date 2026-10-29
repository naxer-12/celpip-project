# css_styles.py
# Modern French Editorial Design System for French Noun Gender Publications

MODERN_EDITORIAL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap');

@page {
  size: letter;
  margin: 14mm 14mm 16mm 14mm;
  @top-right {
    content: "FLE • SYSTÈME DE MAÎTRISE DU GENRE";
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    font-size: 7pt;
    font-weight: 600;
    color: #94a3b8;
    letter-spacing: 0.08em;
  }
  @bottom-center {
    content: "Page " counter(page);
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    font-size: 7.5pt;
    font-weight: 500;
    color: #64748b;
  }
}

@page :first {
  margin: 0;
  @top-right { content: normal; }
  @bottom-center { content: normal; }
}

* {
  box-sizing: border-box;
  -webkit-print-color-adjust: exact !important;
  print-color-adjust: exact !important;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  font-size: 9pt;
  line-height: 1.48;
  color: #1e293b;
  background-color: #faf9f6;
  margin: 0;
  padding: 0;
}

/* ==========================================
   STORYTELLING & ESSAY STYLING
   ========================================== */
.story-lead {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 10.5pt;
  line-height: 1.55;
  color: #1e293b;
  font-style: italic;
  background: #ffffff;
  border-left: 3.5px solid #4f46e5;
  padding: 10px 14px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 14px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
}

.history-box {
  background: #fffdfa;
  border: 1px solid #fed7aa;
  border-radius: 8px;
  padding: 10px 14px;
  margin: 12px 0;
  font-size: 8pt;
  line-height: 1.45;
  break-inside: avoid;
}

.history-box-title {
  font-weight: 700;
  color: #9a3412;
  font-size: 8.5pt;
  margin-bottom: 4px;
  display: flex;
  align-items: center;
  gap: 6px;
}

/* ==========================================
   PRONUNCIATION KEY & SOUND GUIDE
   ========================================== */
.pronunciation-master-box {
  background: #ffffff;
  border: 1px solid #cbd5e1;
  border-radius: 8px;
  padding: 12px 16px;
  margin: 16px 0;
  box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  break-inside: avoid;
}

.pron-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px 16px;
  margin-top: 8px;
}

.pron-row {
  font-size: 7.5pt;
  line-height: 1.35;
  border-bottom: 1px dotted #e2e8f0;
  padding-bottom: 4px;
}

.pron-symbol {
  font-family: 'JetBrains Mono', monospace;
  font-weight: 700;
  color: #4338ca;
  background: #e0e7ff;
  padding: 1px 5px;
  border-radius: 3px;
  margin-right: 6px;
}

/* ==========================================
   COVER PAGE HERO
   ========================================== */
.cover-page {
  page-break-after: always;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 24mm 20mm;
  background: linear-gradient(145deg, #faf9f6 0%, #f1f5f9 60%, #e2e8f0 100%);
  position: relative;
  overflow: hidden;
}

.cover-page::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 6px;
  background: linear-gradient(90deg, #4f46e5 0%, #e11d48 50%, #059669 100%);
}

.cover-pill-box {
  display: flex;
  gap: 8px;
  align-items: center;
}

.cover-pill {
  display: inline-block;
  padding: 4px 10px;
  font-size: 7.5pt;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: 9999px;
  background: #e0e7ff;
  color: #3730a3;
  border: 1px solid #c7d2fe;
}

.cover-pill-accent {
  background: #ffe4e6;
  color: #9f1239;
  border: 1px solid #fecdd3;
}

.cover-main {
  margin-top: 30px;
  margin-bottom: auto;
}

.cover-kicker {
  font-size: 10pt;
  font-weight: 700;
  color: #4f46e5;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-bottom: 12px;
}

.cover-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 32pt;
  font-weight: 700;
  line-height: 1.15;
  color: #0f172a;
  margin: 0 0 14px 0;
}

.cover-subtitle {
  font-size: 11pt;
  line-height: 1.5;
  color: #475569;
  max-width: 600px;
  margin: 0 0 24px 0;
}

.cover-features-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin-top: 24px;
  max-width: 620px;
}

.feature-box {
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px 14px;
}

.feature-box-title {
  font-weight: 700;
  font-size: 8.5pt;
  color: #1e293b;
  margin-bottom: 2px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.feature-box-desc {
  font-size: 7.5pt;
  color: #64748b;
  line-height: 1.35;
}

.cover-footer {
  border-top: 1px solid #cbd5e1;
  padding-top: 14px;
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  font-size: 7.5pt;
  color: #64748b;
}

.cover-author {
  font-weight: 700;
  color: #1e293b;
  font-size: 8.5pt;
}

/* ==========================================
   HEADINGS & TYPOGRAPHY
   ========================================== */
.chapter-hero {
  page-break-before: always;
  margin-bottom: 18px;
  padding-bottom: 12px;
  border-bottom: 2px solid #e2e8f0;
  position: relative;
}

.chapter-badge {
  display: inline-block;
  font-size: 7pt;
  font-weight: 800;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4f46e5;
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  padding: 3px 8px;
  border-radius: 4px;
  margin-bottom: 6px;
}

.chapter-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 20pt;
  font-weight: 700;
  color: #0f172a;
  margin: 0 0 4px 0;
  line-height: 1.2;
}

.chapter-subtitle {
  font-size: 9.5pt;
  color: #64748b;
  margin: 0 0 10px 0;
  font-weight: 500;
}

.section-hero {
  margin-top: 18px;
  margin-bottom: 10px;
  padding-bottom: 6px;
  border-bottom: 1px solid #e2e8f0;
  break-after: avoid;
}

.section-title {
  font-size: 12.5pt;
  font-weight: 700;
  color: #1e293b;
  margin: 0;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* ==========================================
   CALLOUTS & ALERT BOXES
   ========================================== */
.callout {
  border-radius: 8px;
  padding: 10px 14px;
  margin: 12px 0;
  font-size: 8.5pt;
  line-height: 1.45;
  break-inside: avoid;
}

.callout-tip {
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  color: #166534;
}

.callout-trap {
  background: #fffbeb;
  border: 1px solid #fde68a;
  color: #92400e;
}

.callout-fem {
  background: #fff1f2;
  border: 1px solid #fecdd3;
  color: #9f1239;
}

.callout-masc {
  background: #eef2ff;
  border: 1px solid #c7d2fe;
  color: #3730a3;
}

/* ==========================================
   RULE CARDS & TABLES
   ========================================== */
.ending-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 12px 14px;
  margin-bottom: 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
  break-inside: avoid;
}

.ending-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #f1f5f9;
  padding-bottom: 6px;
  margin-bottom: 8px;
}

.ending-name {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11pt;
  font-weight: 700;
  color: #0f172a;
}

.badge {
  display: inline-block;
  padding: 2px 7px;
  font-size: 6.5pt;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  border-radius: 9999px;
}

.badge-masc {
  background: #e0e7ff;
  color: #3730a3;
  border: 1px solid #c7d2fe;
}

.badge-fem {
  background: #ffe4e6;
  color: #9f1239;
  border: 1px solid #fecdd3;
}

.badge-dual {
  background: #f3e8ff;
  color: #6b21a8;
  border: 1px solid #e9d5ff;
}

.badge-amber {
  background: #fef3c7;
  color: #92400e;
  border: 1px solid #fde68a;
}

.words-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 6px 14px;
  margin: 6px 0;
}

.word-item {
  font-size: 8pt;
  display: flex;
  justify-content: space-between;
  border-bottom: 1px dotted #e2e8f0;
  padding-bottom: 2px;
}

.word-fr {
  font-weight: 600;
  color: #1e293b;
}

.word-en {
  color: #64748b;
  font-style: italic;
}

.mnemonic-box {
  background: #f8fafc;
  border-left: 3px solid #6366f1;
  padding: 6px 10px;
  font-size: 7.5pt;
  color: #334155;
  margin-top: 8px;
  border-radius: 0 4px 4px 0;
}

/* ==========================================
   MASTER VOCABULARY VAULT CARDS (WITH ENRICHED PHONETICS)
   ========================================== */
.vocab-vault-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin: 10px 0;
}

.vocab-card {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 9px 12px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.02);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  break-inside: avoid;
}

.vocab-card.is-trap {
  border-left: 3.5px solid #d97706;
  background: #fffdfa;
}

.vocab-card.is-masc {
  border-left: 3.5px solid #4f46e5;
}

.vocab-card.is-fem {
  border-left: 3.5px solid #e11d48;
}

.vocab-card.is-dual {
  border-left: 3.5px solid #7c3aed;
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 4px;
}

.card-fr-title {
  font-size: 10.5pt;
  font-weight: 700;
  color: #0f172a;
}

.card-pron-box {
  background: #f1f5f9;
  border-radius: 4px;
  padding: 4px 6px;
  margin-bottom: 6px;
}

.card-phonetic {
  font-family: 'JetBrains Mono', monospace;
  font-size: 7.5pt;
  font-weight: 700;
  color: #3730a3;
}

.card-syllables {
  font-size: 7pt;
  color: #64748b;
  margin-left: 4px;
  font-style: italic;
}

.card-sound-tip {
  font-size: 6.5pt;
  color: #475569;
  margin-top: 1px;
}

.card-en {
  font-size: 8.5pt;
  font-weight: 600;
  color: #334155;
  margin-bottom: 6px;
}

.card-mnemonic {
  font-size: 7.5pt;
  color: #475569;
  background: #f8fafc;
  padding: 4px 8px;
  border-radius: 4px;
  margin-bottom: 6px;
  line-height: 1.35;
}

.card-example {
  border-top: 1px dashed #e2e8f0;
  padding-top: 5px;
  font-size: 7.5pt;
}

.card-ex-fr {
  font-style: italic;
  color: #1e293b;
  margin-bottom: 2px;
}

.card-ex-en {
  color: #64748b;
  font-size: 7pt;
}

/* ==========================================
   VISUAL EXCEPTION CARDS (SVG ATLAS)
   ========================================== */
.exceptions-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
  margin: 12px 0;
}

.exception-visual-card {
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 10px 12px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
  break-inside: avoid;
}

.exception-svg-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ==========================================
   WORKSHEETS & EXERCISES
   ========================================== */
.worksheet-section {
  page-break-before: always;
  margin-bottom: 20px;
}

.worksheet-hero {
  border-bottom: 2px solid #0f172a;
  padding-bottom: 8px;
  margin-bottom: 14px;
}

.exercise-group {
  margin-bottom: 16px;
  break-inside: avoid;
}

.exercise-inst {
  font-size: 8.5pt;
  font-weight: 600;
  color: #475569;
  margin-bottom: 10px;
  background: #f1f5f9;
  padding: 6px 10px;
  border-radius: 6px;
}

.quiz-grid-2col {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px 16px;
}

.quiz-grid-3col {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px 12px;
}

.quiz-item {
  font-size: 8pt;
  padding: 4px 0;
  border-bottom: 1px solid #f1f5f9;
  display: flex;
  align-items: baseline;
  break-inside: avoid;
}

.quiz-num {
  font-weight: 700;
  color: #64748b;
  width: 24px;
  flex-shrink: 0;
}

.quiz-prompt {
  flex-grow: 1;
  color: #1e293b;
}

.quiz-blank {
  display: inline-block;
  min-width: 45px;
  border-bottom: 1px solid #94a3b8;
  margin: 0 4px;
}

/* ==========================================
   ANSWER KEY STYLING
   ========================================== */
.ans-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px 14px;
  margin-top: 10px;
}

.ans-item {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: 6px;
  padding: 6px 10px;
  font-size: 7.5pt;
  break-inside: avoid;
}

.ans-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 2px;
}

.ans-num {
  font-weight: 700;
  color: #0f172a;
}

.ans-correct {
  font-weight: 800;
  color: #059669;
  background: #ecfdf5;
  padding: 1px 6px;
  border-radius: 4px;
}

.ans-rule {
  color: #64748b;
  line-height: 1.35;
}

/* ==========================================
   DATA TABLES
   ========================================== */
.data-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8pt;
  margin: 10px 0;
  break-inside: avoid;
}

.data-table th {
  background: #f8fafc;
  color: #1e293b;
  font-weight: 700;
  text-align: left;
  padding: 6px 10px;
  border-bottom: 2px solid #e2e8f0;
  font-size: 7.5pt;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.data-table td {
  padding: 5px 10px;
  border-bottom: 1px solid #f1f5f9;
  color: #334155;
}

.data-table tr:nth-child(even) {
  background-color: #fafbfc;
}
"""
