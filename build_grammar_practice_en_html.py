#!/usr/bin/env python3
"""
build_grammar_practice_en_html.py - Generator for the English Edition of the French Grammar Practice Workbook.
Includes contextual sub-line English translations and English-speaker-focused grammar explanations.
"""

import os
import html
import french_grammar_en_data as data

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_HTML = os.path.join(ROOT_DIR, "French_Grammar_Practice_English_Edition.html")

CSS_STYLES = """
    :root {
      --font-stack: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      --text-main: #111827;
      --text-muted: #4b5563;
      --text-gloss: #6b7280;
      --border-hairline: #f0f1f3;
      --bg-a1: #e6f4ea;
      --text-a1: #137333;
      --bg-a2: #e8f0fe;
      --text-a2: #1a73e8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: var(--font-stack);
      color: var(--text-main);
      background-color: #ffffff;
      line-height: 1.5;
      font-size: 10pt;
      -webkit-font-smoothing: antialiased;
    }

    @page {
      size: A4 portrait;
      margin: 18mm 18mm 20mm 18mm;
    }

    .workbook-container {
      max-width: 820px;
      margin: 0 auto;
      padding: 36px 24px;
    }

    /* Header */
    .doc-header {
      margin-bottom: 32px;
      padding-bottom: 20px;
      border-bottom: 1.5px solid #e5e7eb;
    }

    .doc-title {
      font-size: 22pt;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: #111827;
      margin-bottom: 6px;
    }

    .doc-subtitle {
      font-size: 11pt;
      color: var(--text-muted);
      margin-bottom: 12px;
    }

    .edition-badge {
      display: inline-block;
      font-size: 8pt;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 10px;
      border-radius: 9999px;
      background-color: #f3f4f6;
      color: #374151;
      border: 1px solid #e5e7eb;
    }

    /* Modules */
    .topic-section {
      margin-bottom: 36px;
      break-inside: auto;
    }

    .topic-header {
      margin-top: 28px;
      margin-bottom: 18px;
      padding-bottom: 8px;
      border-bottom: 1.5px solid #e5e7eb;
      break-after: avoid;
      page-break-after: avoid;
    }

    .topic-title {
      font-size: 15pt;
      font-weight: 600;
      color: #1f2937;
      letter-spacing: -0.015em;
    }

    .topic-desc {
      font-size: 9pt;
      color: var(--text-muted);
      margin-top: 3px;
    }

    /* Questions */
    .question-item {
      padding: 13px 0 15px 0;
      border-bottom: 1px solid var(--border-hairline);
      break-inside: avoid;
      page-break-inside: avoid;
    }

    .question-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 6px;
    }

    .q-number {
      font-size: 9.5pt;
      font-weight: 700;
      color: #4b5563;
    }

    .badge {
      display: inline-block;
      font-size: 7.5pt;
      font-weight: 700;
      text-transform: uppercase;
      padding: 1px 7px;
      border-radius: 9999px;
      letter-spacing: 0.03em;
    }

    .badge-a1 {
      background-color: var(--bg-a1);
      color: var(--text-a1);
    }

    .badge-a2 {
      background-color: var(--bg-a2);
      color: var(--text-a2);
    }

    .scenario-tag {
      font-size: 8.5pt;
      color: #9ca3af;
      margin-left: auto;
      font-style: italic;
    }

    .prompt-fr {
      font-size: 10.5pt;
      font-weight: 500;
      color: #111827;
      line-height: 1.45;
      margin-bottom: 3px;
    }

    /* Underline / Sub-line English Translation */
    .prompt-en {
      font-size: 9pt;
      font-style: italic;
      color: var(--text-gloss);
      line-height: 1.4;
      margin-bottom: 8px;
      padding-left: 2px;
    }

    .options-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 6px 16px;
      margin-top: 6px;
      margin-bottom: 4px;
    }

    .option-pill {
      font-size: 9.5pt;
      color: #374151;
      padding: 3px 6px;
      background-color: #fafafa;
      border-radius: 4px;
    }

    .response-line {
      margin-top: 8px;
      border-bottom: 1px dashed #d1d5db;
      height: 18px;
      width: 100%;
    }

    /* Answer Key */
    .answer-key-section {
      page-break-before: always;
      break-before: page;
      margin-top: 40px;
      padding-top: 24px;
    }

    .ak-header {
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 1.5px solid #111827;
    }

    .ak-title {
      font-size: 16pt;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #111827;
    }

    .ak-subtitle {
      font-size: 9pt;
      color: var(--text-muted);
      margin-top: 3px;
    }

    .ak-grid {
      column-count: 4;
      column-gap: 16px;
      column-fill: balance;
    }

    .ak-entry {
      break-inside: avoid;
      page-break-inside: avoid;
      margin-bottom: 11px;
      font-size: 8pt;
      line-height: 1.35;
      padding-bottom: 7px;
      border-bottom: 1px dotted #e5e7eb;
    }

    .ak-qnum {
      font-weight: 700;
      color: #374151;
      margin-right: 4px;
    }

    .ak-ans {
      font-weight: 700;
      color: #111827;
    }

    .ak-badge {
      font-size: 6.5pt;
      padding: 1px 4px;
      margin-left: 3px;
      border-radius: 3px;
      font-weight: 600;
    }

    .ak-exp {
      display: block;
      color: #4b5563;
      font-size: 7.5pt;
      margin-top: 2px;
      line-height: 1.3;
    }

    @media print {
      body {
        font-size: 9.5pt;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
      .workbook-container {
        max-width: 100%;
        padding: 0;
      }
      .question-item {
        padding: 9px 0 11px 0;
      }
      .prompt-fr {
        font-size: 10pt;
      }
      .prompt-en {
        font-size: 8.5pt;
      }
      .ak-grid {
        column-count: 4;
        column-gap: 14px;
      }
      .ak-entry {
        font-size: 7.5pt;
        margin-bottom: 8px;
        padding-bottom: 5px;
      }
      .ak-exp {
        font-size: 7pt;
      }
    }

    @media screen and (max-width: 820px) {
      .ak-grid {
        column-count: 2;
      }
    }

    @media screen and (max-width: 520px) {
      .ak-grid {
        column-count: 1;
      }
      .options-grid {
        grid-template-columns: 1fr;
      }
    }
"""

MODULE_SUBTITLES = {
    "Les Articles & Les Déterminants": "Definite, indefinite, partitive, possessive, and demonstrative determiners · Q1–Q20",
    "Les Temps Verbaux & Conjugaisons": "Present, near future, imperative, passé composé, and imperfect tenses · Q21–Q40",
    "Les Prépositions": "Spatial, temporal, geographic, and verb-dependent prepositions · Q41–Q60",
    "Les Pronoms": "Subject, tonic, direct (COD), indirect (COI), relative, and adverbial pronouns · Q61–Q80"
}


def render_html():
    sections_html = []

    for topic_idx, topic in enumerate(data.TOPICS, start=1):
        topic_questions = [q for q in data.QUESTIONS if q["topic"] == topic]
        topic_desc = MODULE_SUBTITLES.get(topic, "")

        items_html = []
        for q in topic_questions:
            badge_class = "badge-a1" if q["level"] == "A1" else "badge-a2"
            scenario_text = html.escape(q.get("scenario_bilingual", q.get("scenario", "")))
            prompt_fr_text = html.escape(q["prompt_fr"])
            prompt_en_text = html.escape(q["prompt_en"])

            options_markup = ""
            if q["type"] == "multiple_choice" and q.get("options"):
                opt_items = "".join(f'<div class="option-pill">{html.escape(opt)}</div>' for opt in q["options"])
                options_markup = f'<div class="options-grid">{opt_items}</div>'
            else:
                options_markup = '<div class="response-line"></div>'

            items_html.append(f"""
        <article class="question-item" id="q{q['id']}">
          <div class="question-meta">
            <span class="q-number">Q{q['id']}.</span>
            <span class="badge {badge_class}">{html.escape(q['level'])}</span>
            <span class="scenario-tag">{scenario_text}</span>
          </div>
          <div class="prompt-fr">{prompt_fr_text}</div>
          <div class="prompt-en">{prompt_en_text}</div>
          {options_markup}
        </article>""")

        questions_joined = "\n".join(items_html)
        sections_html.append(f"""
      <section class="topic-section">
        <header class="topic-header">
          <h2 class="topic-title">Module 0{topic_idx} : {html.escape(topic)}</h2>
          <div class="topic-desc">{html.escape(topic_desc)}</div>
        </header>
        <div class="questions-list">
          {questions_joined}
        </div>
      </section>""")

    # Answer Key Section (English explanations)
    ak_entries = []
    for q in data.QUESTIONS:
        badge_class = "badge-a1" if q["level"] == "A1" else "badge-a2"
        ak_entries.append(f"""
        <div class="ak-entry">
          <span class="ak-qnum">{q['id']}.</span>
          <span class="ak-ans">{html.escape(q['answer'])}</span>
          <span class="ak-badge {badge_class}">{html.escape(q['level'])}</span>
          <span class="ak-exp">{html.escape(q['explanation_en'])}</span>
        </div>""")

    ak_html_content = "\n".join(ak_entries)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>French Grammar Practice Workbook (A1–A2) — English Edition</title>
  <style>
{CSS_STYLES}
  </style>
</head>
<body>
  <div class="workbook-container">
    <header class="doc-header">
      <span class="edition-badge">English Edition · Bilingual Gloss &amp; Explanations</span>
      <h1 class="doc-title">French Grammar Practice Workbook (A1–A2)</h1>
      <p class="doc-subtitle">Minimalist contextual practice with sub-line English translations and complete grammar notes for English speakers.</p>
    </header>

    <main>
      {"".join(sections_html)}

      <section class="answer-key-section">
        <header class="ak-header">
          <h2 class="ak-title">Answer Key &amp; Grammar Notes (Corrigés &amp; Explications)</h2>
          <p class="ak-subtitle">Detailed grammatical justifications for English speakers, addressing language contrasts and typical stumbling blocks.</p>
        </header>
        <div class="ak-grid">
          {ak_html_content}
        </div>
      </section>
    </main>
  </div>
</body>
</html>
"""

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)

    print(f"Successfully generated {OUTPUT_HTML} ({len(full_html):,} characters)")


if __name__ == "__main__":
    render_html()
