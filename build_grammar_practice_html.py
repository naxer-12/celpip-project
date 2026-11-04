"""Generator for French Grammar Practice Workbook HTML (A1–A2).

Transforms structured French grammar curriculum data into a minimalist,
typography-focused, print-ready HTML workbook with A4 paged media styles.
"""

import html
import os
import sys
import french_grammar_data as data

OUTPUT_FILE = "French_Grammar_Practice_A1_A2.html"


def generate_css() -> str:
    """Return embedded CSS stylesheet with print media rules and typography."""
    return """
    @page {
      size: A4 portrait;
      margin: 18mm 18mm 20mm 18mm;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1f2937;
      background-color: #ffffff;
      line-height: 1.5;
      font-size: 10pt;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    .container {
      max-width: 800px;
      margin: 0 auto;
      padding: 32px 24px;
    }

    /* Document Header */
    .doc-header {
      border-bottom: 2px solid #111827;
      padding-bottom: 18px;
      margin-bottom: 32px;
    }

    .header-tagline {
      font-size: 8.5pt;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #4b5563;
      margin-bottom: 4px;
    }

    .doc-title {
      font-size: 24pt;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: #111827;
      line-height: 1.2;
    }

    .doc-subtitle {
      font-size: 11pt;
      color: #4b5563;
      margin-top: 8px;
      line-height: 1.45;
    }

    .doc-meta-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin-top: 14px;
      font-size: 8.5pt;
      font-weight: 500;
      color: #4b5563;
    }

    .meta-separator {
      color: #9ca3af;
    }

    /* Topic Sections */
    .topic-section {
      margin-bottom: 36px;
    }

    .topic-header {
      margin-top: 28px;
      margin-bottom: 16px;
      padding-bottom: 8px;
      border-bottom: 1.5px solid #1f2937;
      break-after: avoid;
      page-break-after: avoid;
    }

    .topic-num {
      font-size: 8.5pt;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #6b7280;
    }

    .topic-title {
      font-size: 16pt;
      font-weight: 600;
      letter-spacing: -0.015em;
      color: #111827;
      margin-top: 2px;
    }

    .topic-desc {
      font-size: 8.5pt;
      color: #6b7280;
      margin-top: 2px;
    }

    /* Questions */
    .questions-list {
      display: flex;
      flex-direction: column;
    }

    .question-item {
      padding: 12px 0;
      border-bottom: 1px solid #f0f1f3;
      break-inside: avoid;
      page-break-inside: avoid;
    }

    .question-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 4px;
    }

    .question-id-scenario {
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .question-num {
      font-size: 9.5pt;
      font-weight: 700;
      color: #4b5563;
      font-variant-numeric: tabular-nums;
    }

    .question-scenario {
      font-size: 8.5pt;
      font-style: italic;
      color: #6b7280;
    }

    .badge {
      font-size: 8pt;
      font-weight: 600;
      border-radius: 9999px;
      padding: 2px 8px;
      letter-spacing: 0.04em;
      display: inline-block;
      line-height: 1.2;
    }

    .badge-a1 {
      background-color: #e6f4ea;
      color: #137333;
    }

    .badge-a2 {
      background-color: #e8f0fe;
      color: #1a73e8;
    }

    .question-prompt {
      font-size: 10pt;
      color: #1f2937;
      line-height: 1.5;
      margin-top: 2px;
    }

    .options-list {
      display: flex;
      flex-wrap: wrap;
      gap: 8px 18px;
      margin-top: 8px;
      padding-left: 2px;
    }

    .option-item {
      font-size: 9.5pt;
      color: #374151;
      line-height: 1.4;
    }

    .response-line {
      border-bottom: 1px dashed #e5e7eb;
      margin-top: 10px;
      height: 16px;
      width: 100%;
    }

    /* Answer Key Section */
    .answer-key-section {
      page-break-before: always;
      break-before: page;
      margin-top: 36px;
      padding-top: 24px;
    }

    .answer-key-header {
      border-bottom: 2px solid #111827;
      padding-bottom: 10px;
      margin-bottom: 18px;
      break-after: avoid;
      page-break-after: avoid;
    }

    .answer-key-title {
      font-size: 18pt;
      font-weight: 700;
      color: #111827;
      letter-spacing: -0.02em;
    }

    .answer-key-subtitle {
      font-size: 8.5pt;
      color: #4b5563;
      margin-top: 4px;
      line-height: 1.4;
    }

    .answer-key-grid {
      column-count: 4;
      column-gap: 16px;
      font-size: 8pt;
      line-height: 1.35;
    }

    .answer-item {
      break-inside: avoid;
      page-break-inside: avoid;
      margin-bottom: 8px;
      padding-bottom: 6px;
      border-bottom: 1px dotted #e5e7eb;
    }

    .ans-header {
      display: flex;
      align-items: baseline;
      gap: 4px;
      flex-wrap: wrap;
    }

    .ans-num {
      font-weight: 700;
      color: #111827;
      font-variant-numeric: tabular-nums;
    }

    .ans-badge {
      font-size: 6.5pt;
      padding: 1px 4px;
      border-radius: 3px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    .ans-badge-a1 {
      background-color: #e6f4ea;
      color: #137333;
    }

    .ans-badge-a2 {
      background-color: #e8f0fe;
      color: #1a73e8;
    }

    .ans-val {
      font-weight: 600;
      color: #111827;
    }

    .ans-exp {
      font-size: 7.5pt;
      color: #4b5563;
      margin-top: 2px;
      line-height: 1.35;
    }

    /* Screen Responsiveness */
    @media screen and (max-width: 820px) {
      .answer-key-grid {
        column-count: 2;
      }
    }

    @media screen and (max-width: 500px) {
      .answer-key-grid {
        column-count: 1;
      }
    }

    /* Paged Print Rules */
    @media print {
      body {
        background-color: #ffffff;
        font-size: 9.5pt;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }
      .container {
        max-width: 100%;
        margin: 0;
        padding: 0;
      }
      .question-item {
        break-inside: avoid;
        page-break-inside: avoid;
      }
      .topic-header {
        break-after: avoid;
        page-break-after: avoid;
      }
      .answer-key-section {
        page-break-before: always;
        break-before: page;
      }
      .answer-key-grid {
        column-count: 4;
      }
    }
    """


def render_question(q: dict) -> str:
    """Render a single practice question as HTML."""
    qid = q["id"]
    level = q["level"]
    badge_cls = f"badge-{level.lower()}"
    scenario = html.escape(q["scenario"])
    prompt = html.escape(q["prompt"])

    html_parts = [
        f'        <article class="question-item" id="q{qid}">',
        '          <div class="question-meta">',
        '            <div class="question-id-scenario">',
        f'              <span class="question-num">Q{qid}.</span>',
        f'              <span class="question-scenario">« {scenario} »</span>',
        '            </div>',
        f'            <span class="badge {badge_cls}">{level}</span>',
        '          </div>',
        f'          <p class="question-prompt">{prompt}</p>',
    ]

    if q.get("type") == "multiple_choice" and q.get("options"):
        html_parts.append('          <div class="options-list">')
        for opt in q["options"]:
            html_parts.append(f'            <span class="option-item">{html.escape(opt)}</span>')
        html_parts.append('          </div>')
    else:
        html_parts.append('          <div class="response-line"></div>')

    html_parts.append('        </article>')
    return "\n".join(html_parts)


def render_answer_item(q: dict) -> str:
    """Render a single answer key entry as HTML."""
    qid = q["id"]
    level = q["level"]
    badge_cls = f"ans-badge-{level.lower()}"
    ans = html.escape(q["answer"])
    exp = html.escape(q["explanation"])

    return f"""        <div class="answer-item">
          <div class="ans-header">
            <span class="ans-num">{qid}.</span>
            <span class="ans-badge {badge_cls}">{level}</span>
            <span class="ans-val">{ans}</span>
          </div>
          <div class="ans-exp">— {exp}</div>
        </div>"""


def generate_html() -> str:
    """Generate the complete self-contained HTML document."""
    css = generate_css()

    topic_sections_html = []
    for idx, topic in enumerate(data.TOPICS, start=1):
        topic_qs = [q for q in data.QUESTIONS if q["topic"] == topic]
        escaped_topic = html.escape(topic)

        questions_html = "\n".join(render_question(q) for q in topic_qs)

        section_html = f"""      <section class="topic-section">
        <header class="topic-header">
          <div class="topic-num">Module {idx:02d}</div>
          <h2 class="topic-title">{escaped_topic}</h2>
          <div class="topic-desc">20 questions communicatives • 10 questions A1 + 10 questions A2</div>
        </header>
        <div class="questions-list">
{questions_html}
        </div>
      </section>"""
        topic_sections_html.append(section_html)

    all_topics_html = "\n\n".join(topic_sections_html)

    answers_html = "\n".join(render_answer_item(q) for q in data.QUESTIONS)

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cahier d'Exercices de Grammaire Française (A1–A2)</title>
  <style>{css}
  </style>
</head>
<body>
  <div class="container">
    <header class="doc-header">
      <div class="header-tagline">Cahier d'Entraînement Pratique &bull; Cadre Européen (CECRL)</div>
      <h1 class="doc-title">Grammaire Française • Niveaux A1–A2</h1>
      <p class="doc-subtitle">
        80 exercices communicatifs contextualisés (Articles, Conjugaisons, Prépositions, Pronoms) avec corrigés complets et explications grammaticales.
      </p>
      <div class="doc-meta-bar">
        <span>Niveau : A1 &amp; A2</span>
        <span class="meta-separator">•</span>
        <span>4 Modules Thématiques</span>
        <span class="meta-separator">•</span>
        <span>80 Questions Pratiques</span>
        <span class="meta-separator">•</span>
        <span>Corrigés Détaillés</span>
      </div>
    </header>

    <main>
{all_topics_html}
    </main>

    <section class="answer-key-section" id="answer-key">
      <header class="answer-key-header">
        <div class="topic-num">Corrigés &amp; Solutions</div>
        <h2 class="answer-key-title">Corrigés &amp; Explications / Answer Key</h2>
        <p class="answer-key-subtitle">
          Solutions complètes et justifications grammaticales synthétiques pour les 80 exercices.
        </p>
      </header>
      <div class="answer-key-grid">
{answers_html}
      </div>
    </section>
  </div>
</body>
</html>
"""


def main():
    """Build and write the HTML practice workbook."""
    html_output = generate_html()
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), OUTPUT_FILE)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output):,} characters)")


if __name__ == "__main__":
    main()
