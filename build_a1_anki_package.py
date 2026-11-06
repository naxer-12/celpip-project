#!/usr/bin/env python3
"""
build_a1_anki_package.py

Generates a standalone, production-ready Anki package (.apkg) for the 100 DELF A1
French flashcards covering Greetings, Personal Identity, Age, Jobs & Hobbies.

Model specifications:
- Fields: French, English, Pronunciation, Audio, Gender, Sentence, Conjugation, Liaison_Notes
- Card Front: French term with article prominently displayed, phonetic pronunciation pill,
              audio link button, and color-coded gender badge.
- Card Back: FrontSide, styled dashed divider, English meaning, example sentence with English
             translation, plural/conjugation drill, and liaison / teacher's notes.
- Complete responsive CSS supporting light mode and dark mode (.nightMode, .night_mode,
  and prefers-color-scheme).
"""

import os
import re
import sys
import json
import sqlite3
import zipfile
import tempfile
import urllib.parse
import genanki

# Import dataset from build_flashcards_dataset
from build_flashcards_dataset import cards

# Constants & IDs
MODEL_ID = 1607392319
DECK_ID = 1792834190
DECK_NAME = "DELF A1 French - Introductions, Identity, Age, Jobs & Hobbies (100 Cards)"
OUTPUT_PATH = "/Users/jainamshah/Downloads/Learning French/French_A1_100_Flashcards.apkg"

CARD_CSS = """
/* ====================================================
   DELF A1 FRENCH ANKI STYLESHEET (LIGHT & DARK MODE)
   ==================================================== */

.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  font-size: 15px;
  text-align: center;
  background-color: #f1f5f9;
  color: #0f172a;
  padding: 16px 10px;
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

.card * {
  box-sizing: border-box;
}

/* Card Shell */
.anki-card-wrapper {
  max-width: 520px;
  margin: 0 auto;
}

.card-box {
  background: #ffffff;
  border-radius: 16px;
  box-shadow: 0 4px 16px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(15, 23, 42, 0.05);
  border: 1px solid #e2e8f0;
  padding: 24px 20px;
  text-align: center;
}

.deck-meta {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #64748b;
  margin-bottom: 12px;
}

/* Top Meta & Gender Badges */
.top-meta-row {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 14px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.3px;
  text-transform: uppercase;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
}

.badge-m {
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
}

.badge-f {
  background: #fdf2f8;
  color: #be185d;
  border: 1px solid #fbcfe8;
}

.badge-v {
  background: #fffbeb;
  color: #b45309;
  border: 1px solid #fde68a;
}

.badge-mf {
  background: #faf5ff;
  color: #7e22ce;
  border: 1px solid #e9d5ff;
}

.badge-x {
  background: #f1f5f9;
  color: #475569;
  border: 1px solid #cbd5e1;
}

/* French Term (With Article) */
.french-container {
  margin: 12px 0 18px 0;
}

.french-term {
  font-size: 32px;
  font-weight: 800;
  color: #0f172a;
  letter-spacing: -0.6px;
  line-height: 1.25;
}

/* Pills Row (Pronunciation & Audio) */
.pills-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
}

.pronunciation-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #f8fafc;
  color: #334155;
  border: 1px solid #cbd5e1;
  padding: 5px 12px;
  border-radius: 9999px;
  font-size: 12.5px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-weight: 600;
}

.audio-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #2563eb;
  color: #ffffff !important;
  text-decoration: none;
  padding: 5px 14px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.15s ease;
  box-shadow: 0 1px 3px rgba(37, 99, 235, 0.3);
}

.audio-btn:hover {
  background: #1d4ed8;
  transform: translateY(-1px);
}

/* Card Divider */
#answer.card-divider, hr#answer {
  border: none;
  border-top: 2px dashed #cbd5e1;
  margin: 18px auto;
  max-width: 520px;
}

/* Back Side Content */
.card-back-container {
  text-align: left;
  margin-top: 14px;
}

.card-back {
  text-align: left;
}

.back-section {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 12px 14px;
  margin-bottom: 12px;
}

.back-section:last-child {
  margin-bottom: 0;
}

.section-label {
  font-size: 10px;
  font-weight: 800;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  color: #64748b;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 5px;
}

/* English Meaning */
.meaning-section {
  background: #eff6ff;
  border-color: #bfdbfe;
  text-align: center;
}

.meaning-section .section-label {
  color: #2563eb;
  justify-content: center;
}

.meaning-text {
  font-size: 21px;
  font-weight: 700;
  color: #1e3a8a;
  line-height: 1.35;
}

/* Example Sentence */
.sentence-section {
  border-left: 3.5px solid #10b981;
}

.sentence-fr {
  font-weight: 600;
  color: #0f172a;
  font-size: 14.5px;
  margin-bottom: 4px;
}

.sentence-en {
  font-style: italic;
  color: #475569;
  font-size: 13.5px;
  line-height: 1.4;
}

/* Plural / Conjugation Drill */
.drill-section {
  border-left: 3.5px solid #3b82f6;
}

.drill-content {
  font-size: 13.5px;
  color: #1e293b;
  line-height: 1.45;
}

.drill-content code {
  background: #e2e8f0;
  color: #0f172a;
  padding: 2px 5px;
  border-radius: 4px;
  font-family: ui-monospace, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
}

/* Liaison & Notes */
.notes-section {
  border-left: 3.5px solid #f59e0b;
}

.notes-content {
  font-size: 13px;
  color: #334155;
  line-height: 1.5;
}

.notes-content strong {
  color: #b91c1c;
  font-weight: 700;
}

.notes-content code {
  background: #f1f5f9;
  color: #0f172a;
  padding: 1px 5px;
  border-radius: 3px;
  font-family: ui-monospace, Menlo, Monaco, Consolas, monospace;
  font-size: 12px;
  border: 1px solid #e2e8f0;
}

/* ====================================================
   DARK MODE / NIGHT MODE (Anki Desktop & Mobile & Web)
   ==================================================== */
.nightMode.card, .night_mode.card, body.nightMode, body.night_mode {
  background-color: #0b0f19 !important;
  color: #f1f5f9 !important;
}

.nightMode .card-box, .night_mode .card-box {
  background: #1e293b;
  border-color: #334155;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
}

.nightMode .deck-meta, .night_mode .deck-meta {
  color: #94a3b8;
}

.nightMode .french-term, .night_mode .french-term {
  color: #f8fafc;
}

.nightMode .pronunciation-pill, .night_mode .pronunciation-pill {
  background: #0f172a;
  border-color: #334155;
  color: #cbd5e1;
}

.nightMode .audio-btn, .night_mode .audio-btn {
  background: #3b82f6;
  color: #ffffff !important;
  box-shadow: 0 1px 4px rgba(59, 130, 246, 0.4);
}

.nightMode .audio-btn:hover, .night_mode .audio-btn:hover {
  background: #60a5fa;
}

.nightMode #answer.card-divider, .night_mode #answer.card-divider,
.nightMode hr#answer, .night_mode hr#answer {
  border-top-color: #475569;
}

.nightMode .back-section, .night_mode .back-section {
  background: #0f172a;
  border-color: #334155;
}

.nightMode .meaning-section, .night_mode .meaning-section {
  background: #172554;
  border-color: #1e40af;
}

.nightMode .meaning-section .section-label, .night_mode .meaning-section .section-label {
  color: #93c5fd;
}

.nightMode .meaning-text, .night_mode .meaning-text {
  color: #bfdbfe;
}

.nightMode .section-label, .night_mode .section-label {
  color: #94a3b8;
}

.nightMode .sentence-fr, .night_mode .sentence-fr {
  color: #f1f5f9;
}

.nightMode .sentence-en, .night_mode .sentence-en {
  color: #94a3b8;
}

.nightMode .drill-content, .night_mode .drill-content {
  color: #e2e8f0;
}

.nightMode .drill-content code, .night_mode .drill-content code {
  background: #1e293b;
  color: #93c5fd;
}

.nightMode .notes-content, .night_mode .notes-content {
  color: #cbd5e1;
}

.nightMode .notes-content strong, .night_mode .notes-content strong {
  color: #f87171;
}

.nightMode .notes-content code, .night_mode .notes-content code {
  background: #1e293b;
  border-color: #334155;
  color: #fbcfe8;
}

.nightMode .badge-m, .night_mode .badge-m {
  background: #172554;
  color: #93c5fd;
  border-color: #1e40af;
}

.nightMode .badge-f, .night_mode .badge-f {
  background: #500724;
  color: #fbcfe8;
  border-color: #831843;
}

.nightMode .badge-v, .night_mode .badge-v {
  background: #451a03;
  color: #fde68a;
  border-color: #78350f;
}

.nightMode .badge-mf, .night_mode .badge-mf {
  background: #3b0764;
  color: #e9d5ff;
  border-color: #6b21a8;
}

.nightMode .badge-x, .night_mode .badge-x {
  background: #1e293b;
  color: #94a3b8;
  border-color: #334155;
}

/* System Dark Mode Fallback */
@media (prefers-color-scheme: dark) {
  .card:not(.lightMode) {
    background-color: #0b0f19;
    color: #f1f5f9;
  }
  .card:not(.lightMode) .card-box {
    background: #1e293b;
    border-color: #334155;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  }
  .card:not(.lightMode) .deck-meta { color: #94a3b8; }
  .card:not(.lightMode) .french-term { color: #f8fafc; }
  .card:not(.lightMode) .pronunciation-pill {
    background: #0f172a;
    border-color: #334155;
    color: #cbd5e1;
  }
  .card:not(.lightMode) .audio-btn {
    background: #3b82f6;
    color: #ffffff !important;
  }
  .card:not(.lightMode) #answer.card-divider,
  .card:not(.lightMode) hr#answer {
    border-top-color: #475569;
  }
  .card:not(.lightMode) .back-section {
    background: #0f172a;
    border-color: #334155;
  }
  .card:not(.lightMode) .meaning-section {
    background: #172554;
    border-color: #1e40af;
  }
  .card:not(.lightMode) .meaning-section .section-label { color: #93c5fd; }
  .card:not(.lightMode) .meaning-text { color: #bfdbfe; }
  .card:not(.lightMode) .section-label { color: #94a3b8; }
  .card:not(.lightMode) .sentence-fr { color: #f1f5f9; }
  .card:not(.lightMode) .sentence-en { color: #94a3b8; }
  .card:not(.lightMode) .drill-content { color: #e2e8f0; }
  .card:not(.lightMode) .drill-content code {
    background: #1e293b;
    color: #93c5fd;
  }
  .card:not(.lightMode) .notes-content { color: #cbd5e1; }
  .card:not(.lightMode) .notes-content strong { color: #f87171; }
  .card:not(.lightMode) .notes-content code {
    background: #1e293b;
    border-color: #334155;
    color: #fbcfe8;
  }
  .card:not(.lightMode) .badge-m {
    background: #172554;
    color: #93c5fd;
    border-color: #1e40af;
  }
  .card:not(.lightMode) .badge-f {
    background: #500724;
    color: #fbcfe8;
    border-color: #831843;
  }
  .card:not(.lightMode) .badge-v {
    background: #451a03;
    color: #fde68a;
    border-color: #78350f;
  }
  .card:not(.lightMode) .badge-mf {
    background: #3b0764;
    color: #e9d5ff;
    border-color: #6b21a8;
  }
  .card:not(.lightMode) .badge-x {
    background: #1e293b;
    color: #94a3b8;
    border-color: #334155;
  }
}
"""

CARD_FRONT_TEMPLATE = """
<div class="anki-card-wrapper">
  <div class="deck-meta">DELF A1 FRENCH</div>

  <div class="card-box card-front">
    <div class="top-meta-row">
      {{#Gender}}
      <div class="gender-container">{{Gender}}</div>
      {{/Gender}}
    </div>

    <div class="french-container">
      <div class="french-term">{{French}}</div>
    </div>

    <div class="pills-row">
      {{#Pronunciation}}
      <div class="pronunciation-pill" title="Phonetic Guide">
        <span class="pill-icon">🗣️</span>
        <span class="pill-text">{{Pronunciation}}</span>
      </div>
      {{/Pronunciation}}

      {{#Audio}}
      <div class="audio-container">{{Audio}}</div>
      {{/Audio}}
    </div>
  </div>
</div>
"""

CARD_BACK_TEMPLATE = """
{{FrontSide}}

<hr id="answer" class="card-divider">

<div class="anki-card-wrapper card-back-container">
  <div class="card-box card-back">
    <div class="back-section meaning-section">
      <div class="section-label">ENGLISH MEANING</div>
      <div class="meaning-text">{{English}}</div>
    </div>

    {{#Sentence}}
    <div class="back-section sentence-section">
      <div class="section-label">EXAMPLE SENTENCE (A1)</div>
      <div class="sentence-content">{{Sentence}}</div>
    </div>
    {{/Sentence}}

    {{#Conjugation}}
    <div class="back-section drill-section">
      <div class="section-label">PLURAL / CONJUGATION DRILL</div>
      <div class="drill-content">{{Conjugation}}</div>
    </div>
    {{/Conjugation}}

    {{#Liaison_Notes}}
    <div class="back-section notes-section">
      <div class="section-label">LIAISON & TEACHER'S NOTES</div>
      <div class="notes-content">{{Liaison_Notes}}</div>
    </div>
    {{/Liaison_Notes}}
  </div>
</div>
"""


def format_markdown(text: str) -> str:
    """Converts inline markdown formatting (**bold**, *(italics)*, *italics*, `code`) into HTML."""
    if not text:
        return ""
    # bold: **text**
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # parenthetical italics: *(text)*
    text = re.sub(r"\*\((.*?)\)\*", r"<em>(\1)</em>", text)
    # single asterisks: *text*
    text = re.sub(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    # code/backticks: `text`
    text = re.sub(r"`(.*?)`", r"<code>\1</code>", text)
    return text


def format_sentence_field(sentence: str) -> str:
    """
    Splits French sentence and parenthetical English translation,
    returning structured HTML.
    """
    m = re.match(r"^(.*?)\s*\*\((.*?)\)\*\s*$", sentence)
    if m:
        fr = format_markdown(m.group(1).strip())
        en = format_markdown(m.group(2).strip())
        return f'<div class="sentence-fr">{fr}</div><div class="sentence-en">&ldquo;{en}&rdquo;</div>'
    return format_markdown(sentence)


def format_gender_badge(gender: str) -> str:
    """Formats gender string into a modern, color-coded badge element."""
    if "Masculine" in gender and "Feminine" not in gender:
        b_class = "badge-m"
        icon = "🔵"
    elif "Feminine" in gender and "Masculine" not in gender and "Verb" not in gender:
        b_class = "badge-f"
        icon = "🟣"
    elif "Verb" in gender:
        b_class = "badge-v"
        icon = "🟡"
    elif "Epicene" in gender or ("Masculine" in gender and "Feminine" in gender) or "Adjective" in gender:
        b_class = "badge-mf"
        icon = "🟣/🔵"
    else:
        b_class = "badge-x"
        icon = "⚪"
    return f'<span class="badge {b_class}">{icon} {gender}</span>'


def format_audio_button(audio_query: str) -> str:
    """Formats an external Google Translate web audio button."""
    query_encoded = urllib.parse.quote(audio_query)
    url = f"https://translate.google.com/?sl=fr&tl=en&text={query_encoded}&op=translate"
    return f'<a class="audio-btn" href="{url}" target="_blank" rel="noopener" title="Listen to native pronunciation">🔊 Listen</a>'


def get_section_tag(card_num: int) -> str:
    """Returns canonical section tag based on card index."""
    if 1 <= card_num <= 15:
        return "1_Salutations"
    elif 16 <= card_num <= 28:
        return "2_Identite"
    elif 29 <= card_num <= 44:
        return "3_Age_Nombres"
    elif 45 <= card_num <= 60:
        return "4_Nationalites_Langues"
    elif 61 <= card_num <= 80:
        return "5_Professions_Metiers"
    elif 81 <= card_num <= 100:
        return "6_Loisirs_Passions"
    return "General"


def create_anki_model() -> genanki.Model:
    """Creates the custom DELF A1 French Anki Model."""
    fields = [
        {"name": "French"},
        {"name": "English"},
        {"name": "Pronunciation"},
        {"name": "Audio"},
        {"name": "Gender"},
        {"name": "Sentence"},
        {"name": "Conjugation"},
        {"name": "Liaison_Notes"},
    ]

    templates = [
        {
            "name": "DELF A1 French Recognition & Recall",
            "qfmt": CARD_FRONT_TEMPLATE,
            "afmt": CARD_BACK_TEMPLATE,
        }
    ]

    return genanki.Model(
        model_id=MODEL_ID,
        name="DELF A1 French Model",
        fields=fields,
        templates=templates,
        css=CARD_CSS,
        sort_field_index=0,
    )


def build_a1_package(output_path: str = OUTPUT_PATH) -> str:
    """Constructs deck, notes, and exports to the .apkg file."""
    model = create_anki_model()
    deck = genanki.Deck(deck_id=DECK_ID, name=DECK_NAME)

    print(f"Building Anki deck '{DECK_NAME}'...")
    print(f"Model ID: {MODEL_ID}, Deck ID: {DECK_ID}")
    print(f"Total cards to process: {len(cards)}")

    for c in cards:
        num = c["num"]
        french_raw = c["french"]
        english_raw = c["english"]
        pronunciation_raw = c["pronunciation"]
        audio_query = c["audio_query"]
        gender_raw = c["gender"]
        sentence_raw = c["sentence"]
        plural_raw = c["plural_or_conj"]
        liaison_raw = c["liaison_notes"]

        # Formatted fields
        french_field = french_raw
        english_field = english_raw
        pronunciation_field = pronunciation_raw
        audio_field = format_audio_button(audio_query)
        gender_field = format_gender_badge(gender_raw)
        sentence_field = format_sentence_field(sentence_raw)
        conjugation_field = format_markdown(plural_raw)
        liaison_notes_field = format_markdown(liaison_raw)

        field_values = [
            french_field,
            english_field,
            pronunciation_field,
            audio_field,
            gender_field,
            sentence_field,
            conjugation_field,
            liaison_notes_field,
        ]

        # Stable guid
        stable_guid = genanki.guid_for(str(num), french_raw)
        section_tag = get_section_tag(num)
        tags = ["DELF_A1", f"Section_{section_tag}", "A1_Vocabulary"]

        note = genanki.Note(
            model=model,
            fields=field_values,
            guid=stable_guid,
            tags=tags,
        )
        deck.add_note(note)

    # Package deck into .apkg file
    package = genanki.Package(deck)
    package.write_to_file(output_path)
    print(f"Successfully generated package at: {output_path}")

    return output_path


def verify_apkg(package_path: str) -> dict:
    """Verifies that the generated .apkg file is valid and contains all 100 notes."""
    print("\n--- Verifying Anki Package ---")
    if not os.path.exists(package_path):
        raise FileNotFoundError(f"Package file not found: {package_path}")

    file_size = os.path.getsize(package_path)
    print(f"File exists: {package_path}")
    print(f"File size: {file_size:,} bytes ({file_size / 1024:.2f} KB)")

    if file_size <= 20480:
        raise ValueError(f"File size {file_size} is under the 20KB threshold!")

    # Inspect zip contents
    with zipfile.ZipFile(package_path, "r") as zf:
        namelist = zf.namelist()
        print(f"Zip archive entries: {namelist}")
        if "collection.anki2" not in namelist:
            raise ValueError("Archive is missing collection.anki2 SQLite database!")

        with tempfile.TemporaryDirectory() as tmpdir:
            zf.extract("collection.anki2", tmpdir)
            db_path = os.path.join(tmpdir, "collection.anki2")

            conn = sqlite3.connect(db_path)
            cur = conn.cursor()

            # Verify deck & models
            cur.execute("SELECT decks, models FROM col")
            decks_json, models_json = cur.fetchone()
            decks_dict = json.loads(decks_json)
            models_dict = json.loads(models_json)

            # Check deck name
            deck_found = False
            for d in decks_dict.values():
                if d.get("name") == DECK_NAME:
                    deck_found = True
                    break

            # Check model name
            model_found = False
            for m in models_dict.values():
                if m.get("name") == "DELF A1 French Model":
                    model_found = True
                    break

            # Verify note count
            cur.execute("SELECT count(*) FROM notes")
            note_count = cur.fetchone()[0]

            # Verify cards generated
            cur.execute("SELECT count(*) FROM cards")
            card_count = cur.fetchone()[0]

            # Verify first 3 notes
            cur.execute("SELECT id, guid, flds FROM notes ORDER BY id ASC LIMIT 3")
            sample_notes = cur.fetchall()

            conn.close()

    print(f"Deck verification: {'FOUND' if deck_found else 'MISSING'}")
    print(f"Model verification: {'FOUND' if model_found else 'MISSING'}")
    print(f"Total notes in database: {note_count}")
    print(f"Total cards in database: {card_count}")

    if note_count != 100:
        raise ValueError(f"Expected 100 notes, but found {note_count}!")

    if card_count != 100:
        raise ValueError(f"Expected 100 cards, but found {card_count}!")

    return {
        "file_path": package_path,
        "file_size_bytes": file_size,
        "file_size_kb": round(file_size / 1024, 2),
        "deck_id": DECK_ID,
        "deck_name": DECK_NAME,
        "model_id": MODEL_ID,
        "model_name": "DELF A1 French Model",
        "note_count": note_count,
        "card_count": card_count,
        "status": "VERIFIED_SUCCESSFUL",
    }


if __name__ == "__main__":
    out = build_a1_package(OUTPUT_PATH)
    results = verify_apkg(out)
    print("\nSummary Results:")
    print(json.dumps(results, indent=2))
