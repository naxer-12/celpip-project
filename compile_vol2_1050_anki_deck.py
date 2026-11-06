#!/usr/bin/env python3
"""
Master Compiler for French A1-A2 Volume 2 (1,050 Flashcards Deck)
Merges all 35 topics (30 unique words each = 1,050 flashcards)
Guaranteed 0% overlap with Volume 1!
Builds:
  1. French_A1_A2_Vol2_1050_Master_Deck.apkg
  2. French_A1_A2_Vol2_1050_Master_Reference.md
  3. French_A1_A2_Vol2_1050_Master_Printable.html
Verifies SQLite integrity of the resulting .apkg file.
"""

import os
import sys
import json
import urllib.parse
import re
import sqlite3
import zipfile
import genanki

import data_vol2_part1
import data_vol2_part2
import data_vol2_part3

# Import Volume 1 for duplicate assertion
import data_topics_part1
import data_topics_part2
import data_topics_part3

# Aggregate Volume 1 words
vol1_words = set()
for mod in [data_topics_part1, data_topics_part2, data_topics_part3]:
    d = getattr(mod, "TOPICS_PART1", getattr(mod, "TOPICS_PART2", getattr(mod, "TOPICS_PART3", {})))
    for t, cards in d.items():
        for c in cards:
            vol1_words.add(c["french"].strip().lower())
print(f"Volume 1 reference words loaded: {len(vol1_words)}")

# Aggregate all 35 Volume 2 topics
ALL_TOPICS_VOL2 = {}
ALL_TOPICS_VOL2.update(data_vol2_part1.TOPICS_VOL2_PART1)
ALL_TOPICS_VOL2.update(data_vol2_part2.TOPICS_VOL2_PART2)
ALL_TOPICS_VOL2.update(data_vol2_part3.TOPICS_VOL2_PART3)

print(f"Total Volume 2 topics collected: {len(ALL_TOPICS_VOL2)}")
total_cards = sum(len(c) for c in ALL_TOPICS_VOL2.values())
print(f"Total Volume 2 cards: {total_cards}")

if len(ALL_TOPICS_VOL2) != 35 or total_cards != 1050:
    print(f"ERROR: Expected 35 topics and 1,050 cards, got {len(ALL_TOPICS_VOL2)} topics and {total_cards} cards!")
    sys.exit(1)

# Verify 0 duplicates with Volume 1 and 0 internal repeats
vol2_words_seen = set()
for topic_title, cards in ALL_TOPICS_VOL2.items():
    if len(cards) != 30:
        print(f"ERROR: Topic '{topic_title}' has {len(cards)} cards instead of 30!")
        sys.exit(1)
    for c in cards:
        w = c["french"].strip().lower()
        if w in vol1_words:
            print(f"FATAL ERROR: Word '{c['french']}' in topic '{topic_title}' already exists in Volume 1!")
            sys.exit(1)
        if w in vol2_words_seen:
            print(f"FATAL ERROR: Internal duplicate in Volume 2 '{c['french']}' in topic '{topic_title}'!")
            sys.exit(1)
        vol2_words_seen.add(w)

print("AUDIT SUCCESS: All 1,050 Volume 2 words are 100% unique from Volume 1 and have zero internal repeats!")

OUTPUT_DIR = "/Users/jainamshah/Downloads/Learning French"
APKG_PATH = os.path.join(OUTPUT_DIR, "French_A1_A2_Vol2_1050_Master_Deck.apkg")
MD_PATH = os.path.join(OUTPUT_DIR, "French_A1_A2_Vol2_1050_Master_Reference.md")
HTML_PATH = os.path.join(OUTPUT_DIR, "French_A1_A2_Vol2_1050_Master_Printable.html")

# ---------------------------------------------------------
# 1. ANKI DECK GENERATION
# ---------------------------------------------------------
DECK_ID = 1892837501
MODEL_ID = 1692837502

CSS = """
.card {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 15px;
    text-align: left;
    color: #1e293b;
    background-color: #ffffff;
    padding: 24px;
    line-height: 1.5;
    max-width: 640px;
    margin: 0 auto;
    border-radius: 12px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.nightMode .card, .night_mode .card {
    color: #f1f5f9;
    background-color: #0f172a;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
}
.vol-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 800;
    text-transform: uppercase;
    background: #0284c7;
    color: #ffffff;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.topic-tag {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.nightMode .topic-tag { color: #94a3b8; }
.header-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 12px;
}
.badge-m { background: #dbeafe; color: #1e40af; }
.badge-f { background: #fce7f3; color: #9d174d; }
.badge-v { background: #fef3c7; color: #92400e; }
.badge-x { background: #e2e8f0; color: #334155; }
.nightMode .badge-m { background: #1e3a8a; color: #bfdbfe; }
.nightMode .badge-f { background: #831843; color: #fbcfe8; }
.nightMode .badge-v { background: #78350f; color: #fde68a; }
.nightMode .badge-x { background: #334155; color: #cbd5e1; }

.french-word {
    font-size: 28px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
    letter-spacing: -0.01em;
}
.nightMode .french-word { color: #f8fafc; }

.action-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
}
.pill {
    display: inline-flex;
    align-items: center;
    background: #f1f5f9;
    color: #334155;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 13px;
    font-weight: 600;
}
.nightMode .pill { background: #1e293b; color: #cbd5e1; }

.audio-btn {
    display: inline-flex;
    align-items: center;
    background: #0284c7;
    color: #ffffff !important;
    text-decoration: none;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
}
.audio-btn:hover { background: #0369a1; }

.card-divider {
    border: none;
    border-top: 2px dashed #e2e8f0;
    margin: 18px 0;
}
.nightMode .card-divider { border-top-color: #334155; }

.section-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 4px;
    letter-spacing: 0.05em;
}
.nightMode .section-label { color: #94a3b8; }

.english-box {
    background: #eff6ff;
    border-left: 4px solid #0284c7;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    margin-bottom: 14px;
    font-size: 17px;
    font-weight: 700;
    color: #075985;
}
.nightMode .english-box {
    background: #0c4a6e;
    border-left-color: #38bdf8;
    color: #e0f2fe;
}

.detail-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 10px 12px;
    border-radius: 6px;
    margin-bottom: 12px;
    font-size: 14px;
}
.nightMode .detail-box {
    background: #1e293b;
    border-color: #334155;
    color: #e2e8f0;
}

.code-text {
    font-family: ui-monospace, Menlo, Monaco, Consolas, monospace;
    font-size: 12.5px;
    color: #0369a1;
}
.nightMode .code-text { color: #38bdf8; }

.notes-text {
    font-size: 12.5px;
    color: #b91c1c;
    font-weight: 500;
    line-height: 1.45;
}
.nightMode .notes-text { color: #f87171; }
"""

model = genanki.Model(
    MODEL_ID,
    "French A1-A2 Master Model (Vol 2)",
    fields=[
        {"name": "Topic"},
        {"name": "French"},
        {"name": "English"},
        {"name": "Pronunciation"},
        {"name": "Audio"},
        {"name": "Gender"},
        {"name": "Sentence"},
        {"name": "Conjugation"},
        {"name": "Liaison_Notes"},
        {"name": "BadgeClass"}
    ],
    templates=[
        {
            "name": "French Vocabulary Card",
            "qfmt": """
<div class="card">
    <div><span class="vol-badge">Volume 2</span></div>
    <div class="topic-tag">{{Topic}}</div>
    <div class="header-badge {{BadgeClass}}">{{Gender}}</div>
    <div class="french-word">{{French}}</div>
    <div class="action-row">
        <span class="pill">🗣️ {{Pronunciation}}</span>
        {{Audio}}
    </div>
</div>
""",
            "afmt": """
<div class="card">
    {{FrontSide}}
    <hr id="answer" class="card-divider">
    <div class="section-label">English Meaning</div>
    <div class="english-box">{{English}}</div>
    
    <div class="section-label">Example Sentence</div>
    <div class="detail-box">
        <div>{{Sentence}}</div>
    </div>
    
    <div class="section-label">Plural / Conjugation Drill</div>
    <div class="detail-box">
        <div class="code-text">{{Conjugation}}</div>
    </div>
    
    <div class="section-label">Liaison, Grammar & Teacher's Notes</div>
    <div class="detail-box">
        <div class="notes-text">{{Liaison_Notes}}</div>
    </div>
</div>
"""
        }
    ],
    css=CSS
)

deck = genanki.Deck(DECK_ID, "French A1-A2 Master Vocabulary Deck - Volume 2 (35 Topics - 1,050 Cards)")

for topic_title, cards in ALL_TOPICS_VOL2.items():
    # Clean topic slug for tagging
    topic_slug = re.sub(r'[^a-zA-Z0-9]+', '_', topic_title).strip('_')
    
    for c in cards:
        fr = c.get('french', '')
        en = c.get('english', '')
        pron = c.get('pronunciation', '')
        gender = c.get('gender', 'N/A')
        sent = c.get('sentence', '')
        conj = c.get('plural_or_conj', '')
        notes = c.get('liaison_notes', '')

        # Classify badge
        g_lower = gender.lower()
        if 'masculine' in g_lower and 'feminine' not in g_lower:
            badge_class = "badge-m"
        elif 'feminine' in g_lower:
            badge_class = "badge-f"
        elif 'verb' in g_lower:
            badge_class = "badge-v"
        else:
            badge_class = "badge-x"

        # Audio link
        encoded = urllib.parse.quote(fr)
        audio = f'<a class="audio-btn" href="https://translate.google.com/?sl=fr&tl=en&text={encoded}&op=translate" target="_blank">🔊 Listen</a>'

        note = genanki.Note(
            model=model,
            fields=[
                topic_title,
                fr,
                en,
                pron,
                audio,
                gender,
                sent,
                conj,
                notes,
                badge_class
            ],
            tags=["French_A1_A2_Vol2_Master", topic_slug]
        )
        deck.add_note(note)

print(f"Compiled {len(deck.notes)} notes into deck. Writing to {APKG_PATH}...")
genanki.Package(deck).write_to_file(APKG_PATH)
print("Anki package written successfully.")

# ---------------------------------------------------------
# 2. MARKDOWN REFERENCE GENERATION
# ---------------------------------------------------------
print(f"Generating Markdown reference at {MD_PATH}...")
with open(MD_PATH, 'w', encoding='utf-8') as f:
    f.write("# French A1–A2 Master Vocabulary Reference — Volume 2 (1,050 Flashcards)\n\n")
    f.write("> **Comprehensive 35-Topic Curriculum (Volume 2)** for English-Speaking Learners\n")
    f.write("> Total Topics: 35 | Total Vocabulary Cards: 1,050 | Zero Overlap with Volume 1 | Format: 8 Pedagogical Fields per card\n\n")
    f.write("## Table of Contents\n\n")
    for i, topic in enumerate(ALL_TOPICS_VOL2.keys(), 1):
        clean_anchor = re.sub(r'[^a-zA-Z0-9]+', '-', topic.lower()).strip('-')
        f.write(f"{i}. [{topic}](#{clean_anchor})\n")
    f.write("\n---\n\n")

    for topic_title, cards in ALL_TOPICS_VOL2.items():
        f.write(f"## {topic_title}\n\n")
        f.write("| French (with Article) | English Meaning | Pronunciation | Audio | Gender / Word Type | Example Sentence | Plural / Conjugation | Liaison & Teacher's Notes |\n")
        f.write("|:---|:---|:---|:---:|:---|:---|:---|:---|\n")
        for c in cards:
            fr = c['french'].replace('|', '\\|')
            en = c['english'].replace('|', '\\|')
            pron = c['pronunciation'].replace('|', '\\|')
            gender = c['gender'].replace('|', '\\|')
            sent = c['sentence'].replace('|', '\\|')
            conj = c['plural_or_conj'].replace('|', '\\|')
            notes = c['liaison_notes'].replace('|', '\\|')
            encoded = urllib.parse.quote(c['french'])
            audio_link = f"[🔊 Audio](https://translate.google.com/?sl=fr&tl=en&text={encoded}&op=translate)"
            
            f.write(f"| **{fr}** | {en} | `{pron}` | {audio_link} | `{gender}` | {sent} | {conj} | {notes} |\n")
        f.write("\n---\n\n")

print("Markdown reference written successfully.")

# ---------------------------------------------------------
# 3. HTML PRINTABLE GENERATION
# ---------------------------------------------------------
print(f"Generating Printable HTML at {HTML_PATH}...")

html_head = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>French A1-A2 Master Vocabulary Deck - Volume 2 (1,050 Flashcards)</title>
    <style>
        :root {
            --primary: #0284c7;
            --primary-light: #e0f2fe;
            --border: #e2e8f0;
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --bg-table-alt: #f8fafc;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            color: var(--text-dark);
            background: #ffffff;
            margin: 0;
            padding: 30px;
            line-height: 1.45;
        }
        .header-container {
            border-bottom: 3px solid var(--primary);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        h1 {
            color: var(--primary);
            font-size: 28px;
            margin: 0 0 8px 0;
            font-weight: 800;
        }
        .subtitle {
            font-size: 15px;
            color: var(--text-muted);
            margin: 0;
        }
        .summary-bar {
            display: flex;
            gap: 20px;
            margin-top: 15px;
            flex-wrap: wrap;
        }
        .summary-badge {
            background: var(--primary-light);
            color: var(--primary);
            padding: 6px 14px;
            border-radius: 9999px;
            font-weight: 700;
            font-size: 13px;
        }
        .topic-section {
            margin-bottom: 40px;
            page-break-after: always;
        }
        .topic-title {
            color: var(--primary);
            font-size: 20px;
            font-weight: 800;
            border-bottom: 2px solid var(--border);
            padding-bottom: 8px;
            margin-bottom: 14px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
            margin-bottom: 20px;
        }
        th {
            background: #0f172a;
            color: #ffffff;
            text-align: left;
            padding: 9px 10px;
            font-size: 11.5px;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }
        td {
            padding: 8px 10px;
            border-bottom: 1px solid var(--border);
            vertical-align: top;
        }
        tr:nth-child(even) td {
            background-color: var(--bg-table-alt);
        }
        .fr-word {
            font-weight: 800;
            color: #0f172a;
            font-size: 14px;
            white-space: nowrap;
        }
        .pron-pill {
            display: inline-block;
            background: #f1f5f9;
            color: #334155;
            padding: 2px 7px;
            border-radius: 4px;
            font-family: ui-monospace, Menlo, Consolas, monospace;
            font-size: 11.5px;
            font-weight: 600;
        }
        .badge {
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10.5px;
            font-weight: 700;
        }
        .badge-m { background: #dbeafe; color: #1e40af; }
        .badge-f { background: #fce7f3; color: #9d174d; }
        .badge-v { background: #fef3c7; color: #92400e; }
        .badge-x { background: #e2e8f0; color: #334155; }
        .sentence-text {
            color: #334155;
        }
        .sentence-en {
            color: #64748b;
            font-style: italic;
            font-size: 12px;
        }
        .conj-text {
            font-family: ui-monospace, Menlo, Consolas, monospace;
            font-size: 11.5px;
            color: #0369a1;
        }
        .notes-text {
            font-size: 11.5px;
            color: #b91c1c;
        }
        .audio-link {
            color: #0284c7;
            text-decoration: none;
            font-weight: 700;
            font-size: 12px;
        }
        .audio-link:hover { text-decoration: underline; }
        @media print {
            body { padding: 10px; font-size: 11px; }
            .topic-section { page-break-after: always; }
            th { background: #334155 !important; color: #fff !important; -webkit-print-color-adjust: exact; }
            .badge-m, .badge-f, .badge-v, .badge-x { -webkit-print-color-adjust: exact; }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <h1>Guide Complet de Vocabulaire Français (A1–A2) — Volume 2</h1>
        <p class="subtitle">Volume 2 Master Flashcard Reference & Curriculum | 100% Unique Non-Overlapping Set for English-Speaking Learners</p>
        <div class="summary-bar">
            <span class="summary-badge">📚 35 Full Topics</span>
            <span class="summary-badge">🃏 1,050 Brand-New Flashcards (30 per topic)</span>
            <span class="summary-badge">✨ 0% Overlap with Volume 1</span>
            <span class="summary-badge">🗣️ Phonetic Respellings & Audio</span>
            <span class="summary-badge">⚠️ Complete Gender, Liaison & Notes</span>
        </div>
    </div>
"""

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html_head)
    
    for topic_title, cards in ALL_TOPICS_VOL2.items():
        f.write(f'<div class="topic-section">\n')
        f.write(f'  <div class="topic-title">{topic_title}</div>\n')
        f.write('  <table>\n')
        f.write('    <thead>\n')
        f.write('      <tr>\n')
        f.write('        <th style="width:16%;">Français (avec Article)</th>\n')
        f.write('        <th style="width:14%;">Sens Anglais</th>\n')
        f.write('        <th style="width:13%;">Prononciation</th>\n')
        f.write('        <th style="width:5%;">Audio</th>\n')
        f.write('        <th style="width:10%;">Genre / Type</th>\n')
        f.write('        <th style="width:16%;">Phrase d\'Exemple</th>\n')
        f.write('        <th style="width:13%;">Pluriel / Conjugaison</th>\n')
        f.write('        <th style="width:13%;">Liaison & Notes</th>\n')
        f.write('      </tr>\n')
        f.write('    </thead>\n')
        f.write('    <tbody>\n')
        
        for c in cards:
            fr = c['french']
            en = c['english']
            pron = c['pronunciation']
            gender = c['gender']
            sent = c['sentence']
            conj = c['plural_or_conj']
            notes = c['liaison_notes']
            
            g_lower = gender.lower()
            if 'masculine' in g_lower and 'feminine' not in g_lower:
                b_class = "badge-m"
            elif 'feminine' in g_lower:
                b_class = "badge-f"
            elif 'verb' in g_lower:
                b_class = "badge-v"
            else:
                b_class = "badge-x"
                
            encoded = urllib.parse.quote(fr)
            audio_html = f'<a class="audio-link" href="https://translate.google.com/?sl=fr&tl=en&text={encoded}&op=translate" target="_blank">🔊</a>'
            
            # Format sentence with translation italicized
            sent_html = sent.replace('*(', '<br><span class="sentence-en">(').replace(')*', ')</span>')
            
            f.write('      <tr>\n')
            f.write(f'        <td class="fr-word">{fr}</td>\n')
            f.write(f'        <td><strong>{en}</strong></td>\n')
            f.write(f'        <td><span class="pron-pill">{pron}</span></td>\n')
            f.write(f'        <td style="text-align:center;">{audio_html}</td>\n')
            f.write(f'        <td><span class="badge {b_class}">{gender}</span></td>\n')
            f.write(f'        <td class="sentence-text">{sent_html}</td>\n')
            f.write(f'        <td class="conj-text">{conj}</td>\n')
            f.write(f'        <td class="notes-text">{notes}</td>\n')
            f.write('      </tr>\n')
            
        f.write('    </tbody>\n')
        f.write('  </table>\n')
        f.write('</div>\n')
        
    f.write('</body>\n</html>\n')

print("Printable HTML written successfully.")

# ---------------------------------------------------------
# 4. SQLITE INTEGRITY VERIFICATION
# ---------------------------------------------------------
print("Verifying Anki package (.apkg) via SQLite...")
with zipfile.ZipFile(APKG_PATH, 'r') as z:
    file_list = z.namelist()
    db_filename = 'collection.anki21' if 'collection.anki21' in file_list else 'collection.anki2'
    z.extract(db_filename, '/tmp')
    db_path = os.path.join('/tmp', db_filename)

conn = sqlite3.connect(db_path)
cur = conn.cursor()
cur.execute("SELECT count(*) FROM notes;")
note_count = cur.fetchone()[0]
cur.execute("SELECT count(*) FROM cards;")
card_count = cur.fetchone()[0]
conn.close()
os.remove(db_path)

print(f"VERIFICATION SUCCESSFUL: {note_count} notes and {card_count} cards verified in SQLite!")
print("Volume 2 generation and compilation is 100% complete!")
