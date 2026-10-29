#!/usr/bin/env python3
"""
French Numbers (0 to 10,000) Practice Workbook & Comprehensive Answer Key Generator
Produces:
1. French_Numbers_0-10000_Workbook.pdf (Printable & Form-Ready PDF via ReportLab)
2. French_Numbers_0-10000_Workbook.docx (Fully Editable Word Document via python-docx)
Conforms strictly to the official 1990 French spelling reform (Rectifications orthographiques).
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = "/Users/jainamshah/Downloads/Learning French"
PDF_PATH = os.path.join(OUTPUT_DIR, "French_Numbers_0-10000_Workbook.pdf")
DOCX_PATH = os.path.join(OUTPUT_DIR, "French_Numbers_0-10000_Workbook.docx")

# ----------------------------------------------------------------------
# DATA DEFINITIONS
# ----------------------------------------------------------------------

PHASES_DATA = [
    {
        "phase_id": "Phase 1A",
        "title": "Base Digits & Unique Teens (0–16)",
        "subtitle": "Focus: Tricky spellings, accents, silent letters, and unique teen roots",
        "description": "Master the atomic building blocks of the French numbering system. Pay special attention to accents (zéro), silent consonants (sept, huit), and the non-compound teens (11–16).",
        "questions": [
            {"num": "1.1", "prompt": "Write in French: 0", "type": "D2F", "input": "0", "answer": "zéro", "trap": "Requires the acute accent (accent aigu) on the 'é'. Never spell as English 'zero'."},
            {"num": "1.2", "prompt": "Write in French: 7", "type": "D2F", "input": "7", "answer": "sept", "trap": "Contains a silent 'p' from Latin 'septem'. Pronounced /sɛt/."},
            {"num": "1.3", "prompt": "Write in French: 8", "type": "D2F", "input": "8", "answer": "huit", "trap": "Features an aspirated 'h' (h aspiré) — elision is blocked (e.g., 'le huit', never 'l'huit'). Final 't' is pronounced /ɥit/ except before a consonant in rapid speech."},
            {"num": "1.4", "prompt": "Write in French: 9", "type": "D2F", "input": "9", "answer": "neuf", "trap": "Final 'f' /nœf/ changes to /v/ in liaison before 'ans' or 'heures' (e.g., 'neuf ans' = /nœ-vɑ̃/)."},
            {"num": "1.5", "prompt": "Convert to digits: onze", "type": "F2D", "input": "onze", "answer": "11", "trap": "Treated as starting with a semi-consonant: blocks elision ('le onze', not 'l'onze')."},
            {"num": "1.6", "prompt": "Write in French: 14", "type": "D2F", "input": "14", "answer": "quatorze", "trap": "Spelled 'quatorze' (with 'o'), not 'quatri-'. Avoid confusing with 'quatre' (4) or 'quarante' (40)."},
            {"num": "1.7", "prompt": "Write in French: 15", "type": "D2F", "input": "15", "answer": "quinze", "trap": "Nasal vowel /kɛ̃z/. Do not confuse with 'cinq' (5) or 'cinquante' (50)."},
            {"num": "1.8", "prompt": "Convert to digits: seize", "type": "F2D", "input": "seize", "answer": "16", "trap": "The final unique Latin-derived root teen before compound teens begin at 17 (dix-sept)."}
        ]
    },
    {
        "phase_id": "Phase 1B",
        "title": "Standard Decades & The 'Et-un' Rule (17–69)",
        "subtitle": "Focus: Compound teens (17–19), regular decades (20–60), and the conjunction 'et' for unit 1",
        "description": "Notice how compound teens start at 17 (10 + unit). For decades 20 through 60, unit 1 uses 'et-un' with hyphens under the 1990 reform, while units 2–9 use direct hyphens.",
        "questions": [
            {"num": "2.1", "prompt": "Write in French: 17", "type": "D2F", "input": "17", "answer": "dix-sept", "trap": "First compound teen formed by addition (10 + 7). Joined by a hyphen."},
            {"num": "2.2", "prompt": "Write in French: 19", "type": "D2F", "input": "19", "answer": "dix-neuf", "trap": "Compound teen (10 + 9). Pronounced /diz-nœf/ with voiced /z/."},
            {"num": "2.3", "prompt": "Write in French: 21", "type": "D2F", "input": "21", "answer": "vingt-et-un", "trap": "The 'et-un' rule! Under the 1990 reform, consistent hyphens link all components: 'vingt-et-un' (traditional had no hyphens around 'et')."},
            {"num": "2.4", "prompt": "Convert to digits: vingt-quatre", "type": "F2D", "input": "vingt-quatre", "answer": "24", "trap": "Standard decade compound (20 + 4). Direct hyphenation, no 'et'."},
            {"num": "2.5", "prompt": "Write in French: 31", "type": "D2F", "input": "31", "answer": "trente-et-un", "trap": "Decade 30 (trente) + unit 1 takes 'et-un' (1990: 'trente-et-un')."},
            {"num": "2.6", "prompt": "Write in French: 48", "type": "D2F", "input": "48", "answer": "quarante-huit", "trap": "Decade 40 (quarante) + 8. Directly hyphenated. No 'et'."},
            {"num": "2.7", "prompt": "Write in French: 51", "type": "D2F", "input": "51", "answer": "cinquante-et-un", "trap": "Decade 50 (cinquante) + unit 1 takes 'et-un' with 1990 hyphens."},
            {"num": "2.8", "prompt": "Convert to digits: soixante-cinq", "type": "F2D", "input": "soixante-cinq", "answer": "65", "trap": "Decade 60 (soixante, pronounced /swa.sɑ̃t/ — the 'x' sounds like 's') + 5."}
        ]
    },
    {
        "phase_id": "Phase 2A",
        "title": "The 70s Trap (Base 60 + Teens)",
        "subtitle": "Focus: Base-60 continuation (60 + 10 through 60 + 19) and the 71 exception",
        "description": "Metropolitan French has no unique root for 'seventy'; it continues counting in base 60 by adding the teens (10 through 19) directly to 'soixante'.",
        "questions": [
            {"num": "3.1", "prompt": "Write in French: 70", "type": "D2F", "input": "70", "answer": "soixante-dix", "trap": "Literally '60 + 10'. Hyphenated compound."},
            {"num": "3.2", "prompt": "Write in French: 71", "type": "D2F", "input": "71", "answer": "soixante-et-onze", "trap": "THE 71 TRAP: Unlike 81 and 91, 71 retains the conjunction 'et' because it builds on 60 ('soixante-et-onze'). 1990 reform joins all with hyphens."},
            {"num": "3.3", "prompt": "Convert to digits: soixante-douze", "type": "F2D", "input": "soixante-douze", "answer": "72", "trap": "60 + 12 = 72. Notice 'et' is dropped; only 71 carries 'et'."},
            {"num": "3.4", "prompt": "Write in French: 75", "type": "D2F", "input": "75", "answer": "soixante-quinze", "trap": "60 + 15 = 75. Do not say *septante* in standard Metropolitan French."},
            {"num": "3.5", "prompt": "Write in French: 77", "type": "D2F", "input": "77", "answer": "soixante-dix-sept", "trap": "Triple compound: 60 + 10 + 7. Hyphens connect each component."},
            {"num": "3.6", "prompt": "Write in French: 79", "type": "D2F", "input": "79", "answer": "soixante-dix-neuf", "trap": "60 + 10 + 9 = 79. The final step before the vigesimal 80s."}
        ]
    },
    {
        "phase_id": "Phase 2B",
        "title": "The 80s (Vigesimal Base 4 × 20)",
        "subtitle": "Focus: The plural '-s' on 'vingts', omission of '-s' when followed, and disappearance of 'et'",
        "description": "The Celtic vigesimal (base-20) legacy survives in 80: 'quatre-vingts' (4 twenties). Here lies one of the most tested grammar traps in French orthography.",
        "questions": [
            {"num": "4.1", "prompt": "Write in French: 80", "type": "D2F", "input": "80", "answer": "quatre-vingts", "trap": "THE PLURAL -S TRAP: 'vingt' is multiplied (4 × 20) AND ends the number, so it MUST take a plural '-s'. Spelled 'quatre-vingts'."},
            {"num": "4.2", "prompt": "Write in French: 81", "type": "D2F", "input": "81", "answer": "quatre-vingt-un", "trap": "THE DOUBLE TRAP: 1) NO 'et' (never *quatre-vingt-et-un*!). 2) The '-s' on 'vingt' is DROPPED immediately because it is followed by another numeral ('un')."},
            {"num": "4.3", "prompt": "Convert to digits: quatre-vingt-quatre", "type": "F2D", "input": "quatre-vingt-quatre", "answer": "84", "trap": "4 × 20 + 4 = 84. 'vingt' has no '-s' because it is followed by 'quatre'."},
            {"num": "4.4", "prompt": "Write in French: 85", "type": "D2F", "input": "85", "answer": "quatre-vingt-cinq", "trap": "4 × 20 + 5 = 85. 'vingt' remains singular."},
            {"num": "4.5", "prompt": "Write in French: 88", "type": "D2F", "input": "88", "answer": "quatre-vingt-huit", "trap": "4 × 20 + 8 = 88. 'vingt' has no '-s'. In liaison, 't' in vingt can link to 'huit' (/ka.trə.vɛ̃.tɥit/)."},
            {"num": "4.6", "prompt": "Convert to digits: quatre-vingts", "type": "F2D", "input": "quatre-vingts", "answer": "80", "trap": "Presence of the terminating '-s' confirms exactly 80."}
        ]
    },
    {
        "phase_id": "Phase 2C",
        "title": "The 90s (Vigesimal + Teens: 4 × 20 + Teens)",
        "subtitle": "Focus: Combining 4 × 20 with 10–19, no 'et' in 91, and no '-s' on 'vingt'",
        "description": "The 90s combine the vigesimal structure (4 × 20) with the teens (10–19). 'Vingt' is never followed by an empty tail, so it never takes an '-s'.",
        "questions": [
            {"num": "5.1", "prompt": "Write in French: 90", "type": "D2F", "input": "90", "answer": "quatre-vingt-dix", "trap": "4 × 20 + 10 = 90. 'vingt' has NO '-s' because it is followed by 'dix'."},
            {"num": "5.2", "prompt": "Write in French: 91", "type": "D2F", "input": "91", "answer": "quatre-vingt-onze", "trap": "THE 91 TRAP: No 'et' (unlike 71!). Do not write *quatre-vingt-et-onze*. No '-s' on 'vingt'."},
            {"num": "5.3", "prompt": "Convert to digits: quatre-vingt-quatorze", "type": "F2D", "input": "quatre-vingt-quatorze", "answer": "94", "trap": "4 × 20 + 14 = 94. Teen root 'quatorze'."},
            {"num": "5.4", "prompt": "Write in French: 95", "type": "D2F", "input": "95", "answer": "quatre-vingt-quinze", "trap": "4 × 20 + 15 = 95."},
            {"num": "5.5", "prompt": "Write in French: 97", "type": "D2F", "input": "97", "answer": "quatre-vingt-dix-sept", "trap": "Quadruple compound: 4 × 20 + 10 + 7. All hyphenated."},
            {"num": "5.6", "prompt": "Write in French: 99", "type": "D2F", "input": "99", "answer": "quatre-vingt-dix-neuf", "trap": "4 × 20 + 10 + 9 = 99. The ultimate 2-digit number challenge."}
        ]
    },
    {
        "phase_id": "Phase 3",
        "title": "The Hundreds (100–999)",
        "subtitle": "Focus: Bare 'cent', plural '-s' rules on 'cents' vs compound drop, and zero 'et' after hundreds",
        "description": "Rules for 'cent': 1) Never say 'un cent'; 2) 'cent' takes an '-s' when multiplied AND terminating the number; 3) The '-s' drops immediately if followed by ANY number; 4) French NEVER says 'cent et un' (no 'et' after hundreds).",
        "questions": [
            {"num": "6.1", "prompt": "Write in French: 100", "type": "D2F", "input": "100", "answer": "cent", "trap": "BARE CENT: Never write *un cent*. In French, 100 is simply 'cent'."},
            {"num": "6.2", "prompt": "Write in French: 101", "type": "D2F", "input": "101", "answer": "cent-un", "trap": "NO 'ET' AFTER CENT: Unlike English ('one hundred and one'), French never uses 'et' after cent. Under 1990 reform: 'cent-un'."},
            {"num": "6.3", "prompt": "Write in French: 200", "type": "D2F", "input": "200", "answer": "deux-cents", "trap": "PLURAL -S ON CENT: Multiplied (2 × 100) and followed by nothing, so 'cent' TAKES an '-s': 'deux-cents'."},
            {"num": "6.4", "prompt": "Write in French: 205", "type": "D2F", "input": "205", "answer": "deux-cent-cinq", "trap": "DROPPED -S: Because 'cent' is followed by 'cinq', it loses its plural '-s' and becomes singular: 'deux-cent-cinq'."},
            {"num": "6.5", "prompt": "Convert to digits: trois-cents", "type": "F2D", "input": "trois-cents", "answer": "300", "trap": "Multiplied bare hundred with plural '-s' = exact 300."},
            {"num": "6.6", "prompt": "Write in French: 380", "type": "D2F", "input": "380", "answer": "trois-cent-quatre-vingts", "trap": "THE CLASSIC DUAL TEST: 'cent' has NO '-s' (followed by quatre-vingts); BUT 'vingt' HAS an '-s' (multiplied 4 × 20, nothing follows)!"},
            {"num": "6.7", "prompt": "Write in French: 382", "type": "D2F", "input": "382", "answer": "trois-cent-quatre-vingt-deux", "trap": "TRIPLE CHECK: Neither 'cent' nor 'vingt' takes an '-s' because both are followed by downstream numerals ('deux')."},
            {"num": "6.8", "prompt": "Write in French: 575", "type": "D2F", "input": "575", "answer": "cinq-cent-soixante-quinze", "trap": "500 + 75: 'cent' has no '-s' (followed by 75); 75 is 'soixante-quinze'."},
            {"num": "6.9", "prompt": "Convert to digits: huit-cent-quatre-vingt-quatorze", "type": "F2D", "input": "huit-cent-quatre-vingt-quatorze", "answer": "894", "trap": "800 + (4 × 20 + 14) = 894."}
        ]
    },
    {
        "phase_id": "Phase 4",
        "title": "The Thousands (1,000–10,000)",
        "subtitle": "Focus: Bare 'mille', strictly invariable 'mille' (never '-s'), interior zeros, and compounding",
        "description": "'Mille' is strictly an invariable adjective in French: it NEVER takes an '-s' under any circumstance (unlike 'million' or 'milliard' which are nouns). 1,000 is always bare 'mille' (never 'un mille').",
        "questions": [
            {"num": "7.1", "prompt": "Write in French: 1 000", "type": "D2F", "input": "1 000", "answer": "mille", "trap": "BARE MILLE: Never say *un mille*. Always simply 'mille'."},
            {"num": "7.2", "prompt": "Write in French: 2 000", "type": "D2F", "input": "2 000", "answer": "deux-mille", "trap": "INVARIABLE MILLE: Unlike 'cents', 'mille' NEVER takes an '-s'. Never write *deux-milles*!"},
            {"num": "7.3", "prompt": "Write in French: 4 008", "type": "D2F", "input": "4 008", "answer": "quatre-mille-huit", "trap": "INTERIOR ZEROS: The zero hundreds and zero tens are skipped completely. Hyphenated: 'quatre-mille-huit'."},
            {"num": "7.4", "prompt": "Convert to digits: six-mille-deux-cents", "type": "F2D", "input": "six-mille-deux-cents", "answer": "6 200", "trap": "'mille' is singular/invariable, while 'cents' correctly carries an '-s' because it terminates the number (200)."},
            {"num": "7.5", "prompt": "Write in French: 7 080", "type": "D2F", "input": "7 080", "answer": "sept-mille-quatre-vingts", "trap": "'mille' is invariable; 'quatre-vingts' carries the terminal '-s' because nothing follows 80."},
            {"num": "7.6", "prompt": "Write in French: 7 083", "type": "D2F", "input": "7 083", "answer": "sept-mille-quatre-vingt-trois", "trap": "'quatre-vingt' loses its '-s' because 'trois' follows."},
            {"num": "7.7", "prompt": "Write in French: 9 999", "type": "D2F", "input": "9 999", "answer": "neuf-mille-neuf-cent-quatre-vingt-dix-neuf", "trap": "All components chained: 'mille' invariable, 'cent' without '-s', 'vingt' without '-s'."},
            {"num": "7.8", "prompt": "Write in French: 10 000", "type": "D2F", "input": "10 000", "answer": "dix-mille", "trap": "Upper boundary of workbook. 'dix-mille' — invariable 'mille'."}
        ]
    }
]

SECTION_2_DRILLS = [
    {"num": "2.01", "prompt": "Write in French: 37", "type": "D2F", "input": "37", "answer": "trente-sept", "trap": "Standard decade + unit."},
    {"num": "2.02", "prompt": "Convert to digits: quatre-vingt-trois", "type": "F2D", "input": "quatre-vingt-trois", "answer": "83", "trap": "4 × 20 + 3 = 83. No '-s' on vingt."},
    {"num": "2.03", "prompt": "Write in French: 116", "type": "D2F", "input": "116", "answer": "cent-seize", "trap": "Bare cent + unique teen root 'seize'. No 'et'."},
    {"num": "2.04", "prompt": "Write in French: 250", "type": "D2F", "input": "250", "answer": "deux-cent-cinquante", "trap": "'cent' has no '-s' because 50 follows."},
    {"num": "2.05", "prompt": "Convert to digits: quatre-cents", "type": "F2D", "input": "quatre-cents", "answer": "400", "trap": "'cents' has plural '-s' because it is multiplied and ends the number."},
    {"num": "2.06", "prompt": "Write in French: 471", "type": "D2F", "input": "471", "answer": "quatre-cent-soixante-et-onze", "trap": "71 uses 'soixante-et-onze'. 'cent' has no '-s'."},
    {"num": "2.07", "prompt": "Write in French: 680", "type": "D2F", "input": "680", "answer": "six-cent-quatre-vingts", "trap": "'cent' singular, 'vingts' plural with '-s'!"},
    {"num": "2.08", "prompt": "Convert to digits: sept-cent-quatre-vingt-un", "type": "F2D", "input": "sept-cent-quatre-vingt-un", "answer": "781", "trap": "700 + 81. Notice 81 has no 'et' and vingt has no '-s'."},
    {"num": "2.09", "prompt": "Write in French: 892", "type": "D2F", "input": "892", "answer": "huit-cent-quatre-vingt-douze", "trap": "800 + (4 × 20 + 12). 'cent' singular, 'vingt' singular."},
    {"num": "2.10", "prompt": "Write in French: 1 011", "type": "D2F", "input": "1 011", "answer": "mille-onze", "trap": "Bare 'mille', interior zero hundred skipped, teen 'onze'."},
    {"num": "2.11", "prompt": "Convert to digits: mille-trois-cents", "type": "F2D", "input": "mille-trois-cents", "answer": "1 300", "trap": "1000 + 300. 'cents' takes plural '-s' at the end."},
    {"num": "2.12", "prompt": "Write in French: 1 795", "type": "D2F", "input": "1 795", "answer": "mille-sept-cent-quatre-vingt-quinze", "trap": "1000 + 700 + 95 (4 × 20 + 15)."},
    {"num": "2.13", "prompt": "Write in French: 2 001", "type": "D2F", "input": "2 001", "answer": "deux-mille-un", "trap": "Interior zeros skipped. No 'et' after mille!"},
    {"num": "2.14", "prompt": "Convert to digits: deux-mille-quatre-vingts", "type": "F2D", "input": "deux-mille-quatre-vingts", "answer": "2 080", "trap": "2000 + 80. 'quatre-vingts' has terminal '-s'."},
    {"num": "2.15", "prompt": "Write in French: 2 086", "type": "D2F", "input": "2 086", "answer": "deux-mille-quatre-vingt-six", "trap": "Terminal unit 'six' removes the '-s' from 'vingt'."},
    {"num": "2.16", "prompt": "Write in French: 3 400", "type": "D2F", "input": "3 400", "answer": "trois-mille-quatre-cents", "trap": "'cents' has plural '-s' because it terminates the compound."},
    {"num": "2.17", "prompt": "Write in French: 3 407", "type": "D2F", "input": "3 407", "answer": "trois-mille-quatre-cent-sept", "trap": "'sept' follows 'cent', so 'cent' drops the '-s'."},
    {"num": "2.18", "prompt": "Convert to digits: cinq-mille-cinq-cent-cinquante-cinq", "type": "F2D", "input": "cinq-mille-cinq-cent-cinquante-cinq", "answer": "5 555", "trap": "Mastery of repeated '5' roots: cinq, mille, cinq, cent, cinquante, cinq."},
    {"num": "2.19", "prompt": "Write in French: 6 071", "type": "D2F", "input": "6 071", "answer": "six-mille-soixante-et-onze", "trap": "Contains 71 ('soixante-et-onze') within a 6,000s compound."},
    {"num": "2.20", "prompt": "Write in French: 6 780", "type": "D2F", "input": "6 780", "answer": "six-mille-sept-cent-quatre-vingts", "trap": "'cent' singular, 'vingts' plural with '-s'."},
    {"num": "2.21", "prompt": "Convert to digits: sept-mille-cent-quatre-vingt-dix", "type": "F2D", "input": "sept-mille-cent-quatre-vingt-dix", "answer": "7 190", "trap": "7000 + 100 + 90."},
    {"num": "2.22", "prompt": "Write in French: 7 896", "type": "D2F", "input": "7 896", "answer": "sept-mille-huit-cent-quatre-vingt-seize", "trap": "7000 + 800 + 96 (4 × 20 + 16)."},
    {"num": "2.23", "prompt": "Write in French: 8 000", "type": "D2F", "input": "8 000", "answer": "huit-mille", "trap": "Invariable 'mille' with no '-s'."},
    {"num": "2.24", "prompt": "Convert to digits: huit-mille-huit-cents", "type": "F2D", "input": "huit-mille-huit-cents", "answer": "8 800", "trap": "'cents' has plural '-s' at the end of the expression."},
    {"num": "2.25", "prompt": "Write in French: 8 880", "type": "D2F", "input": "8 880", "answer": "huit-mille-huit-cent-quatre-vingts", "trap": "'cent' has no '-s', but 'vingts' HAS an '-s'."},
    {"num": "2.26", "prompt": "Write in French: 8 888", "type": "D2F", "input": "8 888", "answer": "huit-mille-huit-cent-quatre-vingt-huit", "trap": "Neither 'cent' nor 'vingt' has '-s' here."},
    {"num": "2.27", "prompt": "Write in French: 9 018", "type": "D2F", "input": "9 018", "answer": "neuf-mille-dix-huit", "trap": "Interior zero hundred skipped; compound teen 18 ('dix-huit')."},
    {"num": "2.28", "prompt": "Convert to digits: neuf-mille-quatre-vingt-onze", "type": "F2D", "input": "neuf-mille-quatre-vingt-onze", "answer": "9 091", "trap": "9000 + 91. 91 has no 'et' and vingt has no '-s'."},
    {"num": "2.29", "prompt": "Write in French: 9 777", "type": "D2F", "input": "9 777", "answer": "neuf-mille-sept-cent-soixante-dix-sept", "trap": "9000 + 700 + 77 (60 + 17)."},
    {"num": "2.30", "prompt": "Write in French: 10 000", "type": "D2F", "input": "10 000", "answer": "dix-mille", "trap": "Workbook ceiling. 'mille' is invariable."}
]

SECTION_2_PHONE_NUMBERS = [
    {
        "num": "P.1",
        "raw": "06 14 78 92 80",
        "description": "French Mobile Number",
        "pairs": ["06", "14", "78", "92", "80"],
        "answer": "zéro-six, quatorze, soixante-dix-huit, quatre-vingt-douze, quatre-vingts",
        "trap": "Notice the pair 80 ('quatre-vingts') takes the plural '-s' because it is spoken/written as a standalone two-digit block with nothing following."
    },
    {
        "num": "P.2",
        "raw": "01 42 68 71 95",
        "description": "Île-de-France (Paris) Landline Number",
        "pairs": ["01", "42", "68", "71", "95"],
        "answer": "zéro-un, quarante-deux, soixante-huit, soixante-et-onze, quatre-vingt-quinze",
        "trap": "Contrasts 71 ('soixante-et-onze', which keeps 'et') with 95 ('quatre-vingt-quinze', base 80+15 with no 'et')."
    },
    {
        "num": "P.3",
        "raw": "07 81 20 89 00",
        "description": "French Mobile Number with Edge Pairs",
        "pairs": ["07", "81", "20", "89", "00"],
        "answer": "zéro-sept, quatre-vingt-un, vingt, quatre-vingt-neuf, zéro-zéro (or double-zéro)",
        "trap": "Tests 81 ('quatre-vingt-un' with NO 'et' and NO '-s'), followed by 20 ('vingt'), 89 ('quatre-vingt-neuf'), and double zero."
    }
]

SECTION_2_HISTORICAL_YEARS = [
    {
        "num": "H.1",
        "year": "1789",
        "event": "Prise de la Bastille & Révolution française",
        "answer": "mille-sept-cent-quatre-vingt-neuf",
        "alt_answer": "dix-sept-cent-quatre-vingt-neuf",
        "trap": "In modern official French, 'mille-sept-cent-quatre-vingt-neuf'. In traditional historical reading, counting by hundreds is accepted ('dix-sept cent...'). Under 1990 rules, all components are hyphenated."
    },
    {
        "num": "H.2",
        "year": "1998",
        "event": "Victoire de la France à la Coupe du Monde de Football",
        "answer": "mille-neuf-cent-quatre-vingt-dix-huit",
        "alt_answer": "dix-neuf-cent-quatre-vingt-dix-huit",
        "trap": "1000 + 900 + 98 (4 × 20 + 18). Cent and vingt both drop '-s' because numerals follow."
    },
    {
        "num": "H.3",
        "year": "2024",
        "event": "Jeux Olympiques et Paralympiques de Paris",
        "answer": "deux-mille-vingt-quatre",
        "alt_answer": None,
        "trap": "Year in the 2000s: always starts with 'deux-mille' (never *vingt-cent*). Note: 'mille' never takes an '-s'."
    },
    {
        "num": "H.4",
        "year": "1515",
        "event": "Bataille de Marignan (Francis I)",
        "answer": "mille-cinq-cent-quinze",
        "alt_answer": "quinze-cent-quinze",
        "trap": "Famous school mnemonic in France ('quinze-cent-quinze'). Standard cardinal form is 'mille-cinq-cent-quinze'."
    }
]

# ----------------------------------------------------------------------
# NUMBERED CANVAS FOR REPORTLAB (PAGE X OF Y)
# ----------------------------------------------------------------------

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Don't draw running header on cover/first page
        if self._pageNumber > 1:
            # Header
            self.drawString(54, 11 * inch - 36, "FRENCH NUMBERS (0–10,000) PRACTICE WORKBOOK")
            self.drawRightString(8.5 * inch - 54, 11 * inch - 36, "1990 REFORM COMPLIANT")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)
        
        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 46, 8.5 * inch - 54, 46)
        self.drawString(54, 32, "Curriculum Design & Linguistic Reference • Antigravity French Series")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 32, page_str)
        self.restoreState()


# ----------------------------------------------------------------------
# REPORTLAB PDF GENERATOR
# ----------------------------------------------------------------------

def build_pdf():
    print(f"Generating PDF: {PDF_PATH} ...")
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    
    # Custom palette
    NAVY = colors.HexColor("#1A365D")
    CRIMSON = colors.HexColor("#9B2C2C")
    SLATE = colors.HexColor("#2D3748")
    MUTED = colors.HexColor("#718096")
    BG_LIGHT = colors.HexColor("#F7FAFC")
    BORDER_LIGHT = colors.HexColor("#E2E8F0")
    AMBER_BG = colors.HexColor("#FEFCBF")
    AMBER_BORDER = colors.HexColor("#D69E2E")
    
    # Text styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=NAVY,
        alignment=1, # Center
        spaceAfter=6
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=MUTED,
        alignment=1,
        spaceAfter=15
    )
    h1_style = ParagraphStyle(
        'SecHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=NAVY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'SubSecHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=CRIMSON,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=SLATE
    )
    body_bold = ParagraphStyle(
        'BodyDarkBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=13,
        textColor=SLATE
    )
    q_prompt_style = ParagraphStyle(
        'QPrompt',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=NAVY
    )
    hint_style = ParagraphStyle(
        'QHint',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=MUTED
    )
    ans_style = ParagraphStyle(
        'AnswerText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=NAVY
    )
    trap_note_style = ParagraphStyle(
        'TrapNote',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=CRIMSON
    )

    story = []

    # ==========================
    # COVER / HEADER HERO BOX
    # ==========================
    hero_text = """
    <b>FRENCH NUMBERS PRACTICE WORKBOOK</b><br/>
    <font size="11" color="#4A5568"><b>Comprehensive Mastery from 0 to 10,000 • Official 1990 Reform Orthography</b></font><br/>
    <font size="8.5" color="#718096">Designed for Intensive Handwritten & Typed Practice with Complete Annotated Answer Key</font>
    """
    hero_p = Paragraph(hero_text, ParagraphStyle('Hero', fontName='Helvetica', fontSize=18, leading=22, textColor=NAVY, alignment=1))
    hero_table = Table([[hero_p]], colWidths=[7.0 * inch])
    hero_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EDF2F7")),
        ('BOX', (0, 0), (-1, -1), 1.5, NAVY),
        ('TOPPADDING', (0, 0), (-1, -1), 14),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 14),
        ('LEFTPADDING', (0, 0), (-1, -1), 16),
        ('RIGHTPADDING', (0, 0), (-1, -1), 16),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(hero_table)
    story.append(Spacer(1, 10))

    # ==========================
    # CHEAT SHEET / GRAMMAR RULES BOX
    # ==========================
    rules_html = """
    <b>ESSENTIAL 1990 SPELLING RULES & TRAP PREVENTION CHEAT SHEET:</b><br/>
    • <b>1990 Systematic Hyphens:</b> ALL words within a compound number are linked by hyphens without exception (e.g., <i>vingt-et-un</i>, <i>soixante-et-onze</i>, <i>trois-mille-deux-cent-quatre-vingts</i>).<br/>
    • <b>The Rule of 'Cent':</b> Multiplied hundreds take a plural <b>-s</b> ONLY when followed by nothing (e.g., 200 = <i>deux-cents</i>). If ANY number follows, the -s is dropped (e.g., 205 = <i>deux-cent-cinq</i>). Bare 100 is always just <i>cent</i> (never *un cent*). Zero 'et' after hundreds (101 = <i>cent-un</i>).<br/>
    • <b>The Rule of 'Vingt' (80 vs 81–99):</b> 80 = <i>quatre-vingts</i> (takes <b>-s</b> because multiplied and followed by nothing). For 81–99, the -s drops immediately (81 = <i>quatre-vingt-un</i>, 90 = <i>quatre-vingt-dix</i>). Notice: 81 and 91 NEVER use 'et'!<br/>
    • <b>The Invariable 'Mille':</b> 1,000 is bare <i>mille</i> (never *un mille*). 'Mille' is strictly invariable and NEVER takes an -s (e.g., 2,000 = <i>deux-mille</i>).<br/>
    • <b>The 'Et-un' Exception:</b> Conjunction 'et' is used ONLY for 21, 31, 41, 51, 61, and 71. Omitted in 81 and 91.
    """
    rules_p = Paragraph(rules_html, ParagraphStyle('Rules', fontName='Helvetica', fontSize=8, leading=11.5, textColor=SLATE))
    rules_table = Table([[rules_p]], colWidths=[7.0 * inch])
    rules_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), AMBER_BG),
        ('BOX', (0, 0), (-1, -1), 1, AMBER_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))
    story.append(rules_table)
    story.append(Spacer(1, 14))

    # ==========================
    # SECTION 1: PHASE DIAGNOSTICS
    # ==========================
    sec1_title = Paragraph("SECTION 1: Phase-by-Phase Diagnostic (Concept Mastery)", h1_style)
    sec1_desc = Paragraph(
        "Complete the targeted diagnostics below. Write your responses clearly in the blank spaces provided. Pay strict attention to the 1990 spelling reform conventions.",
        body_style
    )
    story.append(sec1_title)
    story.append(sec1_desc)
    story.append(Spacer(1, 8))

    for phase in PHASES_DATA:
        # Phase header
        p_header = Paragraph(f"<b>{phase['phase_id']}: {phase['title']}</b>", h2_style)
        p_sub = Paragraph(f"<i>{phase['subtitle']}</i>", hint_style)
        
        # Build question rows
        table_data = []
        for q in phase["questions"]:
            q_text = Paragraph(f"<b>{q['num']}</b> &nbsp; {q['prompt']}", q_prompt_style)
            # Blank line representation for practice
            blank_p = Paragraph("<font color='#CBD5E0'>_________________________________________________________________</font>", body_style)
            table_data.append([q_text, blank_p])
        
        q_table = Table(table_data, colWidths=[2.7 * inch, 4.3 * inch])
        q_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.white),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 2.8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2.8),
            ('LEFTPADDING', (0, 0), (0, -1), 4),
            ('RIGHTPADDING', (-1, 0), (-1, -1), 4),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#EDF2F7")),
        ]))

        phase_block = [p_header, p_sub, Spacer(1, 4), q_table, Spacer(1, 10)]
        story.append(KeepTogether(phase_block))

    # ==========================
    # SECTION 2: COMPREHENSIVE DRILLS
    # ==========================
    story.append(PageBreak())
    sec2_title = Paragraph("SECTION 2: Randomized Comprehensive Drills (Fluency & Retention)", h1_style)
    sec2_desc = Paragraph(
        "Synthesize all concepts across the full 0–10,000 range. Work through the 30 randomized mixed numbers, followed by real-world applications in French phone numbers and calendar years.",
        body_style
    )
    story.append(sec2_title)
    story.append(sec2_desc)
    story.append(Spacer(1, 8))

    # 30 Drills in a clean two-column or organized table
    part_a_head = Paragraph("<b>Part A: 30 Mixed Cardinal Drills (0 to 10,000)</b>", h2_style)
    story.append(part_a_head)
    story.append(Spacer(1, 4))

    drill_table_data = []
    for item in SECTION_2_DRILLS:
        prompt_p = Paragraph(f"<b>{item['num']}</b> &nbsp; {item['prompt']}", q_prompt_style)
        blank_p = Paragraph("<font color='#CBD5E0'>___________________________________________________________</font>", body_style)
        drill_table_data.append([prompt_p, blank_p])

    drill_table = Table(drill_table_data, colWidths=[2.8 * inch, 4.2 * inch])
    drill_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (0, -1), 4),
        ('RIGHTPADDING', (-1, 0), (-1, -1), 4),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#EDF2F7")),
    ]))
    story.append(drill_table)
    story.append(Spacer(1, 14))

    # Real-World: Phone Numbers
    part_b_head = Paragraph("<b>Part B: Real-World Fluency — French Phone Numbers (Spoken in 2-Digit Pairs)</b>", h2_style)
    part_b_desc = Paragraph(
        "In France, 10-digit phone numbers are always pronounced and written in pairs of two digits (e.g., 06 14 78 92 80). Write out each pair in full French words.",
        hint_style
    )
    story.append(KeepTogether([part_b_head, part_b_desc]))
    story.append(Spacer(1, 6))

    phone_table_data = []
    for p_item in SECTION_2_PHONE_NUMBERS:
        p_label = Paragraph(f"<b>{p_item['num']} &nbsp; {p_item['raw']}</b><br/><font color='#718096' size='7.5'>{p_item['description']}</font>", q_prompt_style)
        p_blank = Paragraph("<font color='#CBD5E0'>Pairs: ________________ , ________________ , ________________ , ________________ , ________________</font>", body_style)
        phone_table_data.append([p_label, p_blank])

    phone_table = Table(phone_table_data, colWidths=[2.6 * inch, 4.4 * inch])
    phone_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
    ]))
    story.append(KeepTogether([phone_table]))
    story.append(Spacer(1, 14))

    # Real-World: Historical Years
    part_c_head = Paragraph("<b>Part C: Real-World Fluency — Landmark Historical Calendar Years</b>", h2_style)
    part_c_desc = Paragraph("Write out the full French words for these landmark historical years.", hint_style)
    story.append(KeepTogether([part_c_head, part_c_desc]))
    story.append(Spacer(1, 6))

    year_table_data = []
    for y_item in SECTION_2_HISTORICAL_YEARS:
        y_label = Paragraph(f"<b>{y_item['num']} &nbsp; Year {y_item['year']}</b><br/><font color='#718096' size='7.5'>{y_item['event']}</font>", q_prompt_style)
        y_blank = Paragraph("<font color='#CBD5E0'>___________________________________________________________</font>", body_style)
        year_table_data.append([y_label, y_blank])

    year_table = Table(year_table_data, colWidths=[2.6 * inch, 4.4 * inch])
    year_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
    ]))
    story.append(KeepTogether([year_table]))

    # ==========================
    # SECTION 3: ANSWER KEY & TRAP ANNOTATIONS
    # ==========================
    story.append(PageBreak())
    sec3_title = Paragraph("SECTION 3: Complete Answer Key & Trap Annotations", h1_style)
    sec3_sub = Paragraph(
        "<b>Teacher's & Self-Study Reference:</b> Full written solutions for every single problem with explicit linguistic justifications, grammar trap explanations, and pronunciation notes.",
        body_style
    )
    story.append(sec3_title)
    story.append(sec3_sub)
    story.append(Spacer(1, 10))

    # Section 1 Solutions by Phase
    for phase in PHASES_DATA:
        p_ans_head = Paragraph(f"<b>Solutions for {phase['phase_id']}: {phase['title']}</b>", h2_style)
        
        sol_data = []
        for q in phase["questions"]:
            num_p = Paragraph(f"<b>{q['num']}</b>", body_bold)
            ans_p = Paragraph(f"<b>{q['answer']}</b>", ans_style)
            trap_p = Paragraph(f"<font color='#9B2C2C'><b>[Rule / Trap Note]</b></font> {q['trap']}", trap_note_style)
            sol_data.append([num_p, ans_p, trap_p])
        
        sol_table = Table(sol_data, colWidths=[0.5 * inch, 2.2 * inch, 4.3 * inch])
        sol_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 4.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#E2E8F0")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ]))
        
        story.append(KeepTogether([p_ans_head, Spacer(1, 3), sol_table, Spacer(1, 8)]))

    # Section 2 Solutions
    sec2_ans_head = Paragraph("<b>Solutions for Section 2: Comprehensive Mixed Drills (Part A)</b>", h2_style)
    story.append(PageBreak())
    story.append(sec2_ans_head)
    story.append(Spacer(1, 6))

    drill_sol_data = []
    for item in SECTION_2_DRILLS:
        num_p = Paragraph(f"<b>{item['num']}</b>", body_bold)
        ans_p = Paragraph(f"<b>{item['answer']}</b>", ans_style)
        trap_p = Paragraph(f"<font color='#9B2C2C'><b>[Note]</b></font> {item['trap']}", trap_note_style)
        drill_sol_data.append([num_p, ans_p, trap_p])

    drill_sol_table = Table(drill_sol_data, colWidths=[0.55 * inch, 2.45 * inch, 4.0 * inch])
    drill_sol_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 2.8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.8),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#E2E8F0")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    story.append(drill_sol_table)
    story.append(Spacer(1, 12))

    # Phone Number Solutions
    phone_ans_head = Paragraph("<b>Solutions for Section 2: Real-World Phone Numbers (Part B)</b>", h2_style)
    phone_sol_data = []
    for p_item in SECTION_2_PHONE_NUMBERS:
        num_p = Paragraph(f"<b>{p_item['num']}</b><br/><font size='7' color='#718096'>{p_item['raw']}</font>", body_bold)
        ans_p = Paragraph(f"<b>{p_item['answer']}</b>", ans_style)
        trap_p = Paragraph(f"<font color='#9B2C2C'><b>[Note]</b></font> {p_item['trap']}", trap_note_style)
        phone_sol_data.append([num_p, ans_p, trap_p])

    phone_sol_table = Table(phone_sol_data, colWidths=[0.8 * inch, 2.7 * inch, 3.5 * inch])
    phone_sol_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#E2E8F0")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    story.append(KeepTogether([phone_ans_head, Spacer(1, 3), phone_sol_table, Spacer(1, 10)]))

    # Historical Year Solutions
    year_ans_head = Paragraph("<b>Solutions for Section 2: Historical Calendar Years (Part C)</b>", h2_style)
    year_sol_data = []
    for y_item in SECTION_2_HISTORICAL_YEARS:
        num_p = Paragraph(f"<b>{y_item['num']}</b><br/><font size='7' color='#718096'>{y_item['year']}</font>", body_bold)
        alt_str = f"<br/><font size='7.5' color='#4A5568'><i>Alt: {y_item['alt_answer']}</i></font>" if y_item['alt_answer'] else ""
        ans_p = Paragraph(f"<b>{y_item['answer']}</b>{alt_str}", ans_style)
        trap_p = Paragraph(f"<font color='#9B2C2C'><b>[Note]</b></font> {y_item['trap']}", trap_note_style)
        year_sol_data.append([num_p, ans_p, trap_p])

    year_sol_table = Table(year_sol_data, colWidths=[0.8 * inch, 2.7 * inch, 3.5 * inch])
    year_sol_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#E2E8F0")),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
    ]))
    story.append(KeepTogether([year_ans_head, Spacer(1, 3), year_sol_table]))

    doc.build(story, canvasmaker=NumberedCanvas)
    print("PDF build successful.")


# ----------------------------------------------------------------------
# PYTHON-DOCX GENERATOR
# ----------------------------------------------------------------------

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def build_docx():
    print(f"Generating DOCX: {DOCX_PATH} ...")
    doc = Document()
    
    # Page setup: Letter, 0.75 in margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Styles
    COLOR_NAVY = RGBColor(26, 54, 93)      # #1A365D
    COLOR_CRIMSON = RGBColor(155, 44, 44)  # #9B2C2C
    COLOR_SLATE = RGBColor(45, 55, 72)     # #2D3748
    COLOR_MUTED = RGBColor(113, 128, 150)  # #718096

    # Hero Banner
    banner_table = doc.add_table(rows=1, cols=1)
    banner_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    banner_cell = banner_table.cell(0, 0)
    set_cell_background(banner_cell, "EDF2F7")
    set_cell_margins(banner_cell, top=200, bottom=200, left=250, right=250)
    
    p = banner_cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p.add_run("FRENCH NUMBERS PRACTICE WORKBOOK\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(20)
    r1.font.bold = True
    r1.font.color.rgb = COLOR_NAVY
    
    r2 = p.add_run("Comprehensive Concept Mastery & Fluency Drills (0 to 10,000)\n")
    r2.font.name = "Arial"
    r2.font.size = Pt(11)
    r2.font.bold = True
    r2.font.color.rgb = COLOR_SLATE

    r3 = p.add_run("Strictly Compliant with the 1990 Official Spelling Reform • Includes Full Annotated Answer Key")
    r3.font.name = "Arial"
    r3.font.size = Pt(9.5)
    r3.font.italic = True
    r3.font.color.rgb = COLOR_MUTED

    doc.add_paragraph()

    # Cheat Sheet Table
    rules_table = doc.add_table(rows=1, cols=1)
    rules_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_cell = rules_table.cell(0, 0)
    set_cell_background(r_cell, "FEFCBF")
    set_cell_margins(r_cell, top=140, bottom=140, left=200, right=200)
    
    rp = r_cell.paragraphs[0]
    r_title = rp.add_run("ESSENTIAL 1990 SPELLING REFORM RULES & TRAP PREVENTION\n")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(10)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_CRIMSON

    rules_text = (
        "• 1990 Reform Hyphens: ALL words forming a compound numeral are systematically joined by hyphens without exception (e.g., vingt-et-un, soixante-et-onze, trois-mille-deux-cent-quatre-vingts).\n"
        "• The Rule of 'Cent': Multiplied hundreds take a plural -s ONLY when not followed by another numeral (e.g., 200 = deux-cents; 205 = deux-cent-cinq). Bare 100 is always 'cent' (never *un cent*). Never use 'et' after hundreds (101 = cent-un).\n"
        "• The Rule of 'Vingt' (80 vs 81–99): 80 = quatre-vingts (multiplied 4 × 20, takes -s). 81–99 drop the -s immediately (81 = quatre-vingt-un; 90 = quatre-vingt-dix). Notice: 81 and 91 NEVER take 'et'!\n"
        "• The Invariable 'Mille': 1,000 is bare 'mille' (never *un mille*). 'Mille' is strictly invariable and NEVER takes an -s (e.g., 2,000 = deux-mille).\n"
        "• The 'Et-un' Rule: Conjunction 'et' is strictly limited to 21, 31, 41, 51, 61, and 71."
    )
    r_body = rp.add_run(rules_text)
    r_body.font.name = "Arial"
    r_body.font.size = Pt(8.5)
    r_body.font.color.rgb = COLOR_SLATE

    doc.add_paragraph()

    # SECTION 1
    s1_p = doc.add_paragraph()
    s1_run = s1_p.add_run("SECTION 1: Phase-by-Phase Diagnostic (Concept Mastery)")
    s1_run.font.name = "Arial"
    s1_run.font.size = Pt(15)
    s1_run.font.bold = True
    s1_run.font.color.rgb = COLOR_NAVY

    s1_desc = doc.add_paragraph()
    s1_desc_run = s1_desc.add_run("Write your answers directly on the line or type in the designated field. Follow 1990 hyphenation rules.")
    s1_desc_run.font.name = "Arial"
    s1_desc_run.font.size = Pt(9.5)
    s1_desc_run.font.italic = True
    s1_desc_run.font.color.rgb = COLOR_MUTED

    for phase in PHASES_DATA:
        ph_head = doc.add_paragraph()
        ph_run = ph_head.add_run(f"{phase['phase_id']}: {phase['title']}")
        ph_run.font.name = "Arial"
        ph_run.font.size = Pt(12)
        ph_run.font.bold = True
        ph_run.font.color.rgb = COLOR_CRIMSON

        sub_p = doc.add_paragraph()
        sub_r = sub_p.add_run(f"{phase['subtitle']} — {phase['description']}")
        sub_r.font.name = "Arial"
        sub_r.font.size = Pt(8.5)
        sub_r.font.italic = True
        sub_r.font.color.rgb = COLOR_MUTED

        q_table = doc.add_table(rows=len(phase["questions"]), cols=2)
        q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        q_table.autofit = False

        for idx, q in enumerate(phase["questions"]):
            cell_q = q_table.cell(idx, 0)
            cell_a = q_table.cell(idx, 1)
            cell_q.width = Inches(2.8)
            cell_a.width = Inches(4.2)
            set_cell_margins(cell_q, top=60, bottom=60, left=100, right=100)
            set_cell_margins(cell_a, top=60, bottom=60, left=100, right=100)

            qp = cell_q.paragraphs[0]
            qr = qp.add_run(f"{q['num']}  {q['prompt']}")
            qr.font.name = "Arial"
            qr.font.size = Pt(9.5)
            qr.font.bold = True
            qr.font.color.rgb = COLOR_NAVY

            ap = cell_a.paragraphs[0]
            ar = ap.add_run("____________________________________________________")
            ar.font.name = "Arial"
            ar.font.size = Pt(9)
            ar.font.color.rgb = RGBColor(203, 213, 224)

        doc.add_paragraph()

    # SECTION 2
    doc.add_page_break()
    s2_p = doc.add_paragraph()
    s2_run = s2_p.add_run("SECTION 2: Randomized Comprehensive Drills (Fluency & Retention)")
    s2_run.font.name = "Arial"
    s2_run.font.size = Pt(15)
    s2_run.font.bold = True
    s2_run.font.color.rgb = COLOR_NAVY

    # Part A
    pa_head = doc.add_paragraph()
    pa_run = pa_head.add_run("Part A: 30 Mixed Cardinal Drills (0 to 10,000 Range)")
    pa_run.font.name = "Arial"
    pa_run.font.size = Pt(12)
    pa_run.font.bold = True
    pa_run.font.color.rgb = COLOR_CRIMSON

    drill_table = doc.add_table(rows=len(SECTION_2_DRILLS), cols=2)
    drill_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    drill_table.autofit = False

    for idx, item in enumerate(SECTION_2_DRILLS):
        cq = drill_table.cell(idx, 0)
        ca = drill_table.cell(idx, 1)
        cq.width = Inches(2.8)
        ca.width = Inches(4.2)
        set_cell_margins(cq, top=50, bottom=50, left=80, right=80)
        set_cell_margins(ca, top=50, bottom=50, left=80, right=80)

        p = cq.paragraphs[0]
        r = p.add_run(f"{item['num']}  {item['prompt']}")
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY

        ap = ca.paragraphs[0]
        ar = ap.add_run("_________________________________________________")
        ar.font.name = "Arial"
        ar.font.size = Pt(8.5)
        ar.font.color.rgb = RGBColor(203, 213, 224)

    doc.add_paragraph()

    # Part B: Phone Numbers
    pb_head = doc.add_paragraph()
    pb_run = pb_head.add_run("Part B: Real-World Fluency — French Phone Numbers (Spoken in Pairs)")
    pb_run.font.name = "Arial"
    pb_run.font.size = Pt(12)
    pb_run.font.bold = True
    pb_run.font.color.rgb = COLOR_CRIMSON

    pb_desc = doc.add_paragraph()
    pb_drun = pb_desc.add_run("French numbers are pronounced in 2-digit pairs. Write out each pair in words:")
    pb_drun.font.name = "Arial"
    pb_drun.font.size = Pt(8.5)
    pb_drun.font.italic = True
    pb_drun.font.color.rgb = COLOR_MUTED

    p_table = doc.add_table(rows=len(SECTION_2_PHONE_NUMBERS), cols=2)
    p_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, item in enumerate(SECTION_2_PHONE_NUMBERS):
        c1 = p_table.cell(idx, 0)
        c2 = p_table.cell(idx, 1)
        c1.width = Inches(2.6)
        c2.width = Inches(4.4)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c2, top=70, bottom=70, left=100, right=100)

        p = c1.paragraphs[0]
        r = p.add_run(f"{item['num']}  {item['raw']}\n({item['description']})")
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY

        p2 = c2.paragraphs[0]
        r2 = p2.add_run("Pairs: ____________ , ____________ , ____________ , ____________ , ____________")
        r2.font.name = "Arial"
        r2.font.size = Pt(8)
        r2.font.color.rgb = RGBColor(203, 213, 224)

    doc.add_paragraph()

    # Part C: Historical Years
    pc_head = doc.add_paragraph()
    pc_run = pc_head.add_run("Part C: Real-World Fluency — Historical Calendar Years")
    pc_run.font.name = "Arial"
    pc_run.font.size = Pt(12)
    pc_run.font.bold = True
    pc_run.font.color.rgb = COLOR_CRIMSON

    y_table = doc.add_table(rows=len(SECTION_2_HISTORICAL_YEARS), cols=2)
    y_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, item in enumerate(SECTION_2_HISTORICAL_YEARS):
        c1 = y_table.cell(idx, 0)
        c2 = y_table.cell(idx, 1)
        c1.width = Inches(2.6)
        c2.width = Inches(4.4)
        set_cell_margins(c1, top=70, bottom=70, left=100, right=100)
        set_cell_margins(c2, top=70, bottom=70, left=100, right=100)

        p = c1.paragraphs[0]
        r = p.add_run(f"{item['num']}  Year {item['year']}\n({item['event']})")
        r.font.name = "Arial"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = COLOR_NAVY

        p2 = c2.paragraphs[0]
        r2 = p2.add_run("____________________________________________________")
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.color.rgb = RGBColor(203, 213, 224)

    # SECTION 3: ANSWER KEY
    doc.add_page_break()
    s3_p = doc.add_paragraph()
    s3_run = s3_p.add_run("SECTION 3: Dedicated Answer Key & Trap Annotations")
    s3_run.font.name = "Arial"
    s3_run.font.size = Pt(16)
    s3_run.font.bold = True
    s3_run.font.color.rgb = COLOR_NAVY

    s3_desc = doc.add_paragraph()
    s3_drun = s3_desc.add_run("Full solutions for every question with explicit linguistic justifications, 1990 reform rule references, and trap warnings.")
    s3_drun.font.name = "Arial"
    s3_drun.font.size = Pt(9.5)
    s3_drun.font.italic = True
    s3_drun.font.color.rgb = COLOR_MUTED

    # Section 1 Answers
    for phase in PHASES_DATA:
        p_ans_head = doc.add_paragraph()
        p_ans_run = p_ans_head.add_run(f"Solutions: {phase['phase_id']} ({phase['title']})")
        p_ans_run.font.name = "Arial"
        p_ans_run.font.size = Pt(11)
        p_ans_run.font.bold = True
        p_ans_run.font.color.rgb = COLOR_CRIMSON

        sol_table = doc.add_table(rows=len(phase["questions"]), cols=3)
        sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        sol_table.autofit = False

        for idx, q in enumerate(phase["questions"]):
            c_num = sol_table.cell(idx, 0)
            c_ans = sol_table.cell(idx, 1)
            c_trap = sol_table.cell(idx, 2)
            c_num.width = Inches(0.6)
            c_ans.width = Inches(2.2)
            c_trap.width = Inches(4.2)
            set_cell_margins(c_num, top=50, bottom=50, left=60, right=60)
            set_cell_margins(c_ans, top=50, bottom=50, left=60, right=60)
            set_cell_margins(c_trap, top=50, bottom=50, left=60, right=60)
            set_cell_background(c_num, "F7FAFC")
            set_cell_background(c_ans, "F7FAFC")
            set_cell_background(c_trap, "F7FAFC")

            p1 = c_num.paragraphs[0]
            r1 = p1.add_run(q["num"])
            r1.font.name = "Arial"
            r1.font.size = Pt(8.5)
            r1.font.bold = True
            r1.font.color.rgb = COLOR_SLATE

            p2 = c_ans.paragraphs[0]
            r2 = p2.add_run(q["answer"])
            r2.font.name = "Arial"
            r2.font.size = Pt(9)
            r2.font.bold = True
            r2.font.color.rgb = COLOR_NAVY

            p3 = c_trap.paragraphs[0]
            r3_lbl = p3.add_run("[Rule / Trap] ")
            r3_lbl.font.name = "Arial"
            r3_lbl.font.size = Pt(8)
            r3_lbl.font.bold = True
            r3_lbl.font.color.rgb = COLOR_CRIMSON
            r3 = p3.add_run(q["trap"])
            r3.font.name = "Arial"
            r3.font.size = Pt(8)
            r3.font.color.rgb = COLOR_SLATE

        doc.add_paragraph()

    # Section 2 Answers
    doc.add_page_break()
    s2_ans_head = doc.add_paragraph()
    s2_ans_run = s2_ans_head.add_run("Solutions: Section 2 Mixed Drills (Part A)")
    s2_ans_run.font.name = "Arial"
    s2_ans_run.font.size = Pt(12)
    s2_ans_run.font.bold = True
    s2_ans_run.font.color.rgb = COLOR_CRIMSON

    d_sol_table = doc.add_table(rows=len(SECTION_2_DRILLS), cols=3)
    d_sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    d_sol_table.autofit = False

    for idx, item in enumerate(SECTION_2_DRILLS):
        c_num = d_sol_table.cell(idx, 0)
        c_ans = d_sol_table.cell(idx, 1)
        c_trap = d_sol_table.cell(idx, 2)
        c_num.width = Inches(0.6)
        c_ans.width = Inches(2.4)
        c_trap.width = Inches(4.0)
        set_cell_margins(c_num, top=45, bottom=45, left=60, right=60)
        set_cell_margins(c_ans, top=45, bottom=45, left=60, right=60)
        set_cell_margins(c_trap, top=45, bottom=45, left=60, right=60)
        set_cell_background(c_num, "F7FAFC")
        set_cell_background(c_ans, "F7FAFC")
        set_cell_background(c_trap, "F7FAFC")

        p1 = c_num.paragraphs[0]
        r1 = p1.add_run(item["num"])
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_SLATE

        p2 = c_ans.paragraphs[0]
        r2 = p2.add_run(item["answer"])
        r2.font.name = "Arial"
        r2.font.size = Pt(9)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_NAVY

        p3 = c_trap.paragraphs[0]
        r3_lbl = p3.add_run("[Note] ")
        r3_lbl.font.name = "Arial"
        r3_lbl.font.size = Pt(8)
        r3_lbl.font.bold = True
        r3_lbl.font.color.rgb = COLOR_CRIMSON
        r3 = p3.add_run(item["trap"])
        r3.font.name = "Arial"
        r3.font.size = Pt(8)
        r3.font.color.rgb = COLOR_SLATE

    doc.add_paragraph()

    # Section 2 Part B Phone Answers
    pb_ans_head = doc.add_paragraph()
    pb_ans_run = pb_ans_head.add_run("Solutions: Section 2 Phone Numbers (Part B)")
    pb_ans_run.font.name = "Arial"
    pb_ans_run.font.size = Pt(11)
    pb_ans_run.font.bold = True
    pb_ans_run.font.color.rgb = COLOR_CRIMSON

    p_sol_table = doc.add_table(rows=len(SECTION_2_PHONE_NUMBERS), cols=3)
    p_sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, item in enumerate(SECTION_2_PHONE_NUMBERS):
        c1 = p_sol_table.cell(idx, 0)
        c2 = p_sol_table.cell(idx, 1)
        c3 = p_sol_table.cell(idx, 2)
        c1.width = Inches(0.9)
        c2.width = Inches(2.7)
        c3.width = Inches(3.4)
        set_cell_margins(c1, top=50, bottom=50, left=60, right=60)
        set_cell_margins(c2, top=50, bottom=50, left=60, right=60)
        set_cell_margins(c3, top=50, bottom=50, left=60, right=60)
        set_cell_background(c1, "F7FAFC")
        set_cell_background(c2, "F7FAFC")
        set_cell_background(c3, "F7FAFC")

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(f"{item['num']}\n{item['raw']}")
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_SLATE

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(item["answer"])
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_NAVY

        p3 = c3.paragraphs[0]
        r3_lbl = p3.add_run("[Note] ")
        r3_lbl.font.name = "Arial"
        r3_lbl.font.size = Pt(8)
        r3_lbl.font.bold = True
        r3_lbl.font.color.rgb = COLOR_CRIMSON
        r3 = p3.add_run(item["trap"])
        r3.font.name = "Arial"
        r3.font.size = Pt(8)
        r3.font.color.rgb = COLOR_SLATE

    doc.add_paragraph()

    # Section 2 Part C Historical Year Answers
    pc_ans_head = doc.add_paragraph()
    pc_ans_run = pc_ans_head.add_run("Solutions: Section 2 Historical Years (Part C)")
    pc_ans_run.font.name = "Arial"
    pc_ans_run.font.size = Pt(11)
    pc_ans_run.font.bold = True
    pc_ans_run.font.color.rgb = COLOR_CRIMSON

    y_sol_table = doc.add_table(rows=len(SECTION_2_HISTORICAL_YEARS), cols=3)
    y_sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, item in enumerate(SECTION_2_HISTORICAL_YEARS):
        c1 = y_sol_table.cell(idx, 0)
        c2 = y_sol_table.cell(idx, 1)
        c3 = y_sol_table.cell(idx, 2)
        c1.width = Inches(0.9)
        c2.width = Inches(2.7)
        c3.width = Inches(3.4)
        set_cell_margins(c1, top=50, bottom=50, left=60, right=60)
        set_cell_margins(c2, top=50, bottom=50, left=60, right=60)
        set_cell_margins(c3, top=50, bottom=50, left=60, right=60)
        set_cell_background(c1, "F7FAFC")
        set_cell_background(c2, "F7FAFC")
        set_cell_background(c3, "F7FAFC")

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(f"{item['num']}\n{item['year']}")
        r1.font.name = "Arial"
        r1.font.size = Pt(8.5)
        r1.font.bold = True
        r1.font.color.rgb = COLOR_SLATE

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(item["answer"])
        r2.font.name = "Arial"
        r2.font.size = Pt(8.5)
        r2.font.bold = True
        r2.font.color.rgb = COLOR_NAVY
        if item["alt_answer"]:
            r2_alt = p2.add_run(f"\nAlt: {item['alt_answer']}")
            r2_alt.font.name = "Arial"
            r2_alt.font.size = Pt(7.5)
            r2_alt.font.italic = True
            r2_alt.font.color.rgb = COLOR_MUTED

        p3 = c3.paragraphs[0]
        r3_lbl = p3.add_run("[Note] ")
        r3_lbl.font.name = "Arial"
        r3_lbl.font.size = Pt(8)
        r3_lbl.font.bold = True
        r3_lbl.font.color.rgb = COLOR_CRIMSON
        r3 = p3.add_run(item["trap"])
        r3.font.name = "Arial"
        r3.font.size = Pt(8)
        r3.font.color.rgb = COLOR_SLATE

    doc.save(DOCX_PATH)
    print("DOCX build successful.")

if __name__ == "__main__":
    build_pdf()
    build_docx()
    print("All builds finished successfully!")
