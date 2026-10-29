#!/usr/bin/env python3
"""
French Numbers (0 to 10,000) Examination & Curriculum System
Generates:
1. French_Numbers_Exam_Student_Version.docx  -> Exam paper ready for students (editable type-in boxes, no answers)
2. French_Numbers_Exam_Student_Version.pdf   -> Print-ready student exam
3. French_Numbers_Exam_Teacher_Key.docx      -> Complete grading key with full solutions, points, and trap notes
4. French_Numbers_Exam_Teacher_Key.pdf       -> Print-ready teacher grading key
5. French_Numbers_0-10000_Workbook.docx      -> Master workbook with cheat sheet, practice sections, and answer key
6. French_Numbers_0-10000_Workbook.pdf       -> Master workbook PDF
"""

import os
import sys
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.pdfgen import canvas

BASE_DIR = "/Users/jainamshah/Downloads/Learning French"

# ----------------------------------------------------------------------
# DATA DEFINITION
# ----------------------------------------------------------------------

PHASES_DATA = [
    {
        "phase_id": "Phase 1A",
        "title": "Base Digits & Unique Teens (0–16)",
        "pts": "8 pts (1 pt each)",
        "desc": "Master atomic digits, acute accents (zéro), silent letters (sept, huit), and non-compound teens (11–16).",
        "questions": [
            {"num": "1.1", "prompt": "Write in French: 0", "type": "D2F", "pts": "1", "answer": "zéro", "trap": "Requires the acute accent (accent aigu) on the 'é'. Never spell as English 'zero'."},
            {"num": "1.2", "prompt": "Write in French: 7", "type": "D2F", "pts": "1", "answer": "sept", "trap": "Contains a silent 'p' from Latin 'septem'. Pronounced /sɛt/."},
            {"num": "1.3", "prompt": "Write in French: 8", "type": "D2F", "pts": "1", "answer": "huit", "trap": "Aspirated 'h' blocks elision ('le huit', not 'l'huit'). Final 't' pronounced /ɥit/."},
            {"num": "1.4", "prompt": "Write in French: 9", "type": "D2F", "pts": "1", "answer": "neuf", "trap": "Final 'f' /nœf/ changes to voiced /v/ in liaison before 'ans' or 'heures' (e.g., 'neuf ans' = /nœ-vɑ̃/)."},
            {"num": "1.5", "prompt": "Convert to digits: onze", "type": "F2D", "pts": "1", "answer": "11", "trap": "Vowel root that blocks elision ('le onze', never 'l'onze')."},
            {"num": "1.6", "prompt": "Write in French: 14", "type": "D2F", "pts": "1", "answer": "quatorze", "trap": "Spelled 'quatorze' (with 'o'), not 'quatri-'. Contrast with 'quatre' (4)."},
            {"num": "1.7", "prompt": "Write in French: 15", "type": "D2F", "pts": "1", "answer": "quinze", "trap": "Nasal vowel /kɛ̃z/. Contrast with 'cinq' (5) and 'cinquante' (50)."},
            {"num": "1.8", "prompt": "Convert to digits: seize", "type": "F2D", "pts": "1", "answer": "16", "trap": "The final unique Latin teen root before compound teens begin at 17 (dix-sept)."}
        ]
    },
    {
        "phase_id": "Phase 1B",
        "title": "Standard Decades & The 'Et-un' Rule (17–69)",
        "pts": "8 pts (1 pt each)",
        "desc": "Compound teens (17–19), regular decades (20–60), and conjunction 'et' for unit 1 under the 1990 reform.",
        "questions": [
            {"num": "2.1", "prompt": "Write in French: 17", "type": "D2F", "pts": "1", "answer": "dix-sept", "trap": "First additive compound teen (10 + 7). Hyphenated."},
            {"num": "2.2", "prompt": "Write in French: 19", "type": "D2F", "pts": "1", "answer": "dix-neuf", "trap": "Compound teen (10 + 9). Pronounced /diz-nœf/ with voiced /z/."},
            {"num": "2.3", "prompt": "Write in French: 21", "type": "D2F", "pts": "1", "answer": "vingt-et-un", "trap": "The 'et-un' rule: under the 1990 reform, hyphens link all components: 'vingt-et-un'."},
            {"num": "2.4", "prompt": "Convert to digits: vingt-quatre", "type": "F2D", "pts": "1", "answer": "24", "trap": "Standard decade compound (20 + 4). Direct hyphenation, no 'et'."},
            {"num": "2.5", "prompt": "Write in French: 31", "type": "D2F", "pts": "1", "answer": "trente-et-un", "trap": "Decade 30 (trente) + unit 1 takes 'et-un' with 1990 hyphens."},
            {"num": "2.6", "prompt": "Write in French: 48", "type": "D2F", "pts": "1", "answer": "quarante-huit", "trap": "Decade 40 (quarante) + 8. Directly hyphenated. No 'et'."},
            {"num": "2.7", "prompt": "Write in French: 51", "type": "D2F", "pts": "1", "answer": "cinquante-et-un", "trap": "Decade 50 (cinquante) + unit 1 takes 'et-un' with 1990 hyphens."},
            {"num": "2.8", "prompt": "Convert to digits: soixante-cinq", "type": "F2D", "pts": "1", "answer": "65", "trap": "Decade 60 (soixante, /swa.sɑ̃t/, 'x' pronounced /s/) + 5."}
        ]
    },
    {
        "phase_id": "Phase 2A",
        "title": "The 70s Trap (Base 60 + Teens)",
        "pts": "6 pts (1 pt each)",
        "desc": "Standard Metropolitan French continuation in base 60: 60 + 10 through 60 + 19, and the 71 exception.",
        "questions": [
            {"num": "3.1", "prompt": "Write in French: 70", "type": "D2F", "pts": "1", "answer": "soixante-dix", "trap": "Base 60: literally 60 + 10. Hyphenated."},
            {"num": "3.2", "prompt": "Write in French: 71", "type": "D2F", "pts": "1", "answer": "soixante-et-onze", "trap": "THE 71 TRAP: Unlike 81 and 91, 71 retains 'et' because it builds on 60 ('soixante-et-onze')."},
            {"num": "3.3", "prompt": "Convert to digits: soixante-douze", "type": "F2D", "pts": "1", "answer": "72", "trap": "60 + 12 = 72. 'et' is dropped for units 72–79."},
            {"num": "3.4", "prompt": "Write in French: 75", "type": "D2F", "pts": "1", "answer": "soixante-quinze", "trap": "60 + 15 = 75. Do not write *septante* in standard Metropolitan French."},
            {"num": "3.5", "prompt": "Write in French: 77", "type": "D2F", "pts": "1", "answer": "soixante-dix-sept", "trap": "Triple compound: 60 + 10 + 7. Hyphens connect each component."},
            {"num": "3.6", "prompt": "Write in French: 79", "type": "D2F", "pts": "1", "answer": "soixante-dix-neuf", "trap": "60 + 10 + 9 = 79. Final step before the vigesimal 80s."}
        ]
    },
    {
        "phase_id": "Phase 2B",
        "title": "The 80s (Vigesimal Base 4 × 20)",
        "pts": "6 pts (1 pt each)",
        "desc": "Vigesimal base (4 × 20). Master the plural '-s' on 'vingts', dropping '-s' when followed, and disappearance of 'et'.",
        "questions": [
            {"num": "4.1", "prompt": "Write in French: 80", "type": "D2F", "pts": "1", "answer": "quatre-vingts", "trap": "PLURAL -S TRAP: 'vingt' is multiplied (4 × 20) AND terminates the number, so it MUST take a plural '-s'."},
            {"num": "4.2", "prompt": "Write in French: 81", "type": "D2F", "pts": "1", "answer": "quatre-vingt-un", "trap": "DOUBLE TRAP: 1) NO 'et' (never *quatre-vingt-et-un*!). 2) '-s' on 'vingt' is DROPPED because it is followed by 'un'."},
            {"num": "4.3", "prompt": "Convert to digits: quatre-vingt-quatre", "type": "F2D", "pts": "1", "answer": "84", "trap": "4 × 20 + 4 = 84. 'vingt' has no '-s' because it is followed by 'quatre'."},
            {"num": "4.4", "prompt": "Write in French: 85", "type": "D2F", "pts": "1", "answer": "quatre-vingt-cinq", "trap": "4 × 20 + 5 = 85. 'vingt' remains singular."},
            {"num": "4.5", "prompt": "Write in French: 88", "type": "D2F", "pts": "1", "answer": "quatre-vingt-huit", "trap": "4 × 20 + 8 = 88. 'vingt' has no '-s'. In liaison, 't' links to 'huit' (/ka.trə.vɛ̃.tɥit/)."},
            {"num": "4.6", "prompt": "Convert to digits: quatre-vingts", "type": "F2D", "pts": "1", "answer": "80", "trap": "Terminal '-s' on 'vingts' confirms exactly 80."}
        ]
    },
    {
        "phase_id": "Phase 2C",
        "title": "The 90s (Vigesimal + Teens: 4 × 20 + Teens)",
        "pts": "6 pts (1 pt each)",
        "desc": "Combining 4 × 20 with teens 10–19. Note absence of 'et' in 91 and invariable 'vingt'.",
        "questions": [
            {"num": "5.1", "prompt": "Write in French: 90", "type": "D2F", "pts": "1", "answer": "quatre-vingt-dix", "trap": "4 × 20 + 10 = 90. 'vingt' has NO '-s' because it is followed by 'dix'."},
            {"num": "5.2", "prompt": "Write in French: 91", "type": "D2F", "pts": "1", "answer": "quatre-vingt-onze", "trap": "THE 91 TRAP: NO 'et' (unlike 71!). Do not write *quatre-vingt-et-onze*. No '-s' on 'vingt'."},
            {"num": "5.3", "prompt": "Convert to digits: quatre-vingt-quatorze", "type": "F2D", "pts": "1", "answer": "94", "trap": "4 × 20 + 14 = 94. Teen root 'quatorze'."},
            {"num": "5.4", "prompt": "Write in French: 95", "type": "D2F", "pts": "1", "answer": "quatre-vingt-quinze", "trap": "4 × 20 + 15 = 95."},
            {"num": "5.5", "prompt": "Write in French: 97", "type": "D2F", "pts": "1", "answer": "quatre-vingt-dix-sept", "trap": "Quadruple compound: 4 × 20 + 10 + 7. All hyphenated."},
            {"num": "5.6", "prompt": "Write in French: 99", "type": "D2F", "pts": "1", "answer": "quatre-vingt-dix-neuf", "trap": "4 × 20 + 10 + 9 = 99. The highest 2-digit numeral."}
        ]
    },
    {
        "phase_id": "Phase 3",
        "title": "The Hundreds (100–999)",
        "pts": "9 pts (1 pt each)",
        "desc": "Rules for 'cent': bare 'cent', plural '-s' on multiplied hundreds, dropping '-s' when followed, and no 'et' after hundreds.",
        "questions": [
            {"num": "6.1", "prompt": "Write in French: 100", "type": "D2F", "pts": "1", "answer": "cent", "trap": "BARE CENT: Never write *un cent*. 100 is simply 'cent'."},
            {"num": "6.2", "prompt": "Write in French: 101", "type": "D2F", "pts": "1", "answer": "cent-un", "trap": "NO 'ET' AFTER CENT: French never says *cent-et-un*. Hyphenated: 'cent-un'."},
            {"num": "6.3", "prompt": "Write in French: 200", "type": "D2F", "pts": "1", "answer": "deux-cents", "trap": "PLURAL -S ON CENT: Multiplied (2 × 100) and followed by nothing, so 'cent' TAKES an '-s'."},
            {"num": "6.4", "prompt": "Write in French: 205", "type": "D2F", "pts": "1", "answer": "deux-cent-cinq", "trap": "DROPPED -S: Because 'cent' is followed by 'cinq', it loses its plural '-s'."},
            {"num": "6.5", "prompt": "Convert to digits: trois-cents", "type": "F2D", "pts": "1", "answer": "300", "trap": "Multiplied bare hundred with plural '-s' = exact 300."},
            {"num": "6.6", "prompt": "Write in French: 380", "type": "D2F", "pts": "1", "answer": "trois-cent-quatre-vingts", "trap": "DUAL TRAP: 'cent' has NO '-s' (followed by 80); but 'vingt' HAS an '-s' (multiplied 4 × 20, terminates number)."},
            {"num": "6.7", "prompt": "Write in French: 382", "type": "D2F", "pts": "1", "answer": "trois-cent-quatre-vingt-deux", "trap": "TRIPLE CHECK: Neither 'cent' nor 'vingt' takes an '-s' because subsequent numerals follow."},
            {"num": "6.8", "prompt": "Write in French: 575", "type": "D2F", "pts": "1", "answer": "cinq-cent-soixante-quinze", "trap": "500 + 75: 'cent' has no '-s' (followed by 75); 75 is 'soixante-quinze'."},
            {"num": "6.9", "prompt": "Convert to digits: huit-cent-quatre-vingt-quatorze", "type": "F2D", "pts": "1", "answer": "894", "trap": "800 + (4 × 20 + 14) = 894."}
        ]
    },
    {
        "phase_id": "Phase 4",
        "title": "The Thousands (1,000–10,000)",
        "pts": "8 pts (1 pt each)",
        "desc": "'Mille' is strictly invariable (never takes an '-s'). Bare 1,000 is always 'mille' (never *un mille*).",
        "questions": [
            {"num": "7.1", "prompt": "Write in French: 1 000", "type": "D2F", "pts": "1", "answer": "mille", "trap": "BARE MILLE: Never say *un mille*. Always simply 'mille'."},
            {"num": "7.2", "prompt": "Write in French: 2 000", "type": "D2F", "pts": "1", "answer": "deux-mille", "trap": "INVARIABLE MILLE: Unlike 'cents', 'mille' NEVER takes an '-s'. Never write *deux-milles*!"},
            {"num": "7.3", "prompt": "Write in French: 4 008", "type": "D2F", "pts": "1", "answer": "quatre-mille-huit", "trap": "INTERIOR ZEROS: Zero hundreds and zero tens are omitted. Hyphenated: 'quatre-mille-huit'."},
            {"num": "7.4", "prompt": "Convert to digits: six-mille-deux-cents", "type": "F2D", "pts": "1", "answer": "6 200", "trap": "'mille' is invariable; 'cents' takes plural '-s' because it terminates the expression."},
            {"num": "7.5", "prompt": "Write in French: 7 080", "type": "D2F", "pts": "1", "answer": "sept-mille-quatre-vingts", "trap": "'mille' invariable; 'quatre-vingts' carries terminal '-s' because nothing follows 80."},
            {"num": "7.6", "prompt": "Write in French: 7 083", "type": "D2F", "pts": "1", "answer": "sept-mille-quatre-vingt-trois", "trap": "'quatre-vingt' loses its '-s' because 'trois' follows."},
            {"num": "7.7", "prompt": "Write in French: 9 999", "type": "D2F", "pts": "1", "answer": "neuf-mille-neuf-cent-quatre-vingt-dix-neuf", "trap": "'mille' invariable, 'cent' without '-s', 'vingt' without '-s'."},
            {"num": "7.8", "prompt": "Write in French: 10 000", "type": "D2F", "pts": "1", "answer": "dix-mille", "trap": "Upper boundary of workbook. 'dix-mille' — invariable 'mille'."}
        ]
    }
]

SECTION_2_DRILLS = [
    {"num": "2.01", "prompt": "Write in French: 37", "type": "D2F", "pts": "1", "answer": "trente-sept", "trap": "Standard decade + unit."},
    {"num": "2.02", "prompt": "Convert to digits: quatre-vingt-trois", "type": "F2D", "pts": "1", "answer": "83", "trap": "4 × 20 + 3 = 83. No '-s' on vingt."},
    {"num": "2.03", "prompt": "Write in French: 116", "type": "D2F", "pts": "1", "answer": "cent-seize", "trap": "Bare cent + unique teen root 'seize'. No 'et'."},
    {"num": "2.04", "prompt": "Write in French: 250", "type": "D2F", "pts": "1", "answer": "deux-cent-cinquante", "trap": "'cent' has no '-s' because 50 follows."},
    {"num": "2.05", "prompt": "Convert to digits: quatre-cents", "type": "F2D", "pts": "1", "answer": "400", "trap": "'cents' has plural '-s' because it is multiplied and ends the number."},
    {"num": "2.06", "prompt": "Write in French: 471", "type": "D2F", "pts": "1", "answer": "quatre-cent-soixante-et-onze", "trap": "71 uses 'soixante-et-onze'. 'cent' has no '-s'."},
    {"num": "2.07", "prompt": "Write in French: 680", "type": "D2F", "pts": "1", "answer": "six-cent-quatre-vingts", "trap": "'cent' singular, 'vingts' plural with '-s'!"},
    {"num": "2.08", "prompt": "Convert to digits: sept-cent-quatre-vingt-un", "type": "F2D", "pts": "1", "answer": "781", "trap": "700 + 81. Notice 81 has no 'et' and vingt has no '-s'."},
    {"num": "2.09", "prompt": "Write in French: 892", "type": "D2F", "pts": "1", "answer": "huit-cent-quatre-vingt-douze", "trap": "800 + (4 × 20 + 12). 'cent' singular, 'vingt' singular."},
    {"num": "2.10", "prompt": "Write in French: 1 011", "type": "D2F", "pts": "1", "answer": "mille-onze", "trap": "Bare 'mille', interior zero hundred skipped, teen 'onze'."},
    {"num": "2.11", "prompt": "Convert to digits: mille-trois-cents", "type": "F2D", "pts": "1", "answer": "1 300", "trap": "1000 + 300. 'cents' takes plural '-s' at the end."},
    {"num": "2.12", "prompt": "Write in French: 1 795", "type": "D2F", "pts": "1", "answer": "mille-sept-cent-quatre-vingt-quinze", "trap": "1000 + 700 + 95 (4 × 20 + 15)."},
    {"num": "2.13", "prompt": "Write in French: 2 001", "type": "D2F", "pts": "1", "answer": "deux-mille-un", "trap": "Interior zeros skipped. No 'et' after mille!"},
    {"num": "2.14", "prompt": "Convert to digits: deux-mille-quatre-vingts", "type": "F2D", "pts": "1", "answer": "2 080", "trap": "2000 + 80. 'quatre-vingts' has terminal '-s'."},
    {"num": "2.15", "prompt": "Write in French: 2 086", "type": "D2F", "pts": "1", "answer": "deux-mille-quatre-vingt-six", "trap": "Terminal unit 'six' removes the '-s' from 'vingt'."},
    {"num": "2.16", "prompt": "Write in French: 3 400", "type": "D2F", "pts": "1", "answer": "trois-mille-quatre-cents", "trap": "'cents' has plural '-s' because it terminates the compound."},
    {"num": "2.17", "prompt": "Write in French: 3 407", "type": "D2F", "pts": "1", "answer": "trois-mille-quatre-cent-sept", "trap": "'sept' follows 'cent', so 'cent' drops the '-s'."},
    {"num": "2.18", "prompt": "Convert to digits: cinq-mille-cinq-cent-cinquante-cinq", "type": "F2D", "pts": "1", "answer": "5 555", "trap": "Mastery of repeated '5' roots: cinq, mille, cinq, cent, cinquante, cinq."},
    {"num": "2.19", "prompt": "Write in French: 6 071", "type": "D2F", "pts": "1", "answer": "six-mille-soixante-et-onze", "trap": "Contains 71 ('soixante-et-onze') within a 6,000s compound."},
    {"num": "2.20", "prompt": "Write in French: 6 780", "type": "D2F", "pts": "1", "answer": "six-mille-sept-cent-quatre-vingts", "trap": "'cent' singular, 'vingts' plural with '-s'."},
    {"num": "2.21", "prompt": "Convert to digits: sept-mille-cent-quatre-vingt-dix", "type": "F2D", "pts": "1", "answer": "7 190", "trap": "7000 + 100 + 90."},
    {"num": "2.22", "prompt": "Write in French: 7 896", "type": "D2F", "pts": "1", "answer": "sept-mille-huit-cent-quatre-vingt-seize", "trap": "7000 + 800 + 96 (4 × 20 + 16)."},
    {"num": "2.23", "prompt": "Write in French: 8 000", "type": "D2F", "pts": "1", "answer": "huit-mille", "trap": "Invariable 'mille' with no '-s'."},
    {"num": "2.24", "prompt": "Convert to digits: huit-mille-huit-cents", "type": "F2D", "pts": "1", "answer": "8 800", "trap": "'cents' has plural '-s' at the end of the expression."},
    {"num": "2.25", "prompt": "Write in French: 8 880", "type": "D2F", "pts": "1", "answer": "huit-mille-huit-cent-quatre-vingts", "trap": "'cent' has no '-s', but 'vingts' HAS an '-s'."},
    {"num": "2.26", "prompt": "Write in French: 8 888", "type": "D2F", "pts": "1", "answer": "huit-mille-huit-cent-quatre-vingt-huit", "trap": "Neither 'cent' nor 'vingt' has '-s' here."},
    {"num": "2.27", "prompt": "Write in French: 9 018", "type": "D2F", "pts": "1", "answer": "neuf-mille-dix-huit", "trap": "Interior zero hundred skipped; compound teen 18 ('dix-huit')."},
    {"num": "2.28", "prompt": "Convert to digits: neuf-mille-quatre-vingt-onze", "type": "F2D", "pts": "1", "answer": "9 091", "trap": "9000 + 91. 91 has no 'et' and vingt has no '-s'."},
    {"num": "2.29", "prompt": "Write in French: 9 777", "type": "D2F", "pts": "1", "answer": "neuf-mille-sept-cent-soixante-dix-sept", "trap": "9000 + 700 + 77 (60 + 17)."},
    {"num": "2.30", "prompt": "Write in French: 10 000", "type": "D2F", "pts": "1", "answer": "dix-mille", "trap": "Workbook ceiling. 'mille' is invariable."}
]

SECTION_2_PHONE_NUMBERS = [
    {
        "num": "P.1",
        "raw": "06 14 78 92 80",
        "description": "French Mobile Number (Standard format: 5 pairs)",
        "pts": "3",
        "pairs": ["06", "14", "78", "92", "80"],
        "answer": "zéro-six, quatorze, soixante-dix-huit, quatre-vingt-douze, quatre-vingts",
        "trap": "Notice the pair 80 ('quatre-vingts') takes plural '-s' because it stands alone as a 2-digit block."
    },
    {
        "num": "P.2",
        "raw": "01 42 68 71 95",
        "description": "Île-de-France / Paris Landline Number",
        "pts": "3",
        "pairs": ["01", "42", "68", "71", "95"],
        "answer": "zéro-un, quarante-deux, soixante-huit, soixante-et-onze, quatre-vingt-quinze",
        "trap": "Contrasts 71 ('soixante-et-onze', keeps 'et') with 95 ('quatre-vingt-quinze', no 'et')."
    },
    {
        "num": "P.3",
        "raw": "07 81 20 89 00",
        "description": "French Mobile Number (Edge-case pairs)",
        "pts": "3",
        "pairs": ["07", "81", "20", "89", "00"],
        "answer": "zéro-sept, quatre-vingt-un, vingt, quatre-vingt-neuf, zéro-zéro (or double-zéro)",
        "trap": "Tests 81 ('quatre-vingt-un' with NO 'et' and NO '-s'), 20 ('vingt'), 89, and 00."
    }
]

SECTION_2_HISTORICAL_YEARS = [
    {
        "num": "H.1",
        "year": "1789",
        "event": "Prise de la Bastille & Révolution française",
        "pts": "2.5",
        "answer": "mille-sept-cent-quatre-vingt-neuf",
        "alt_answer": "dix-sept-cent-quatre-vingt-neuf",
        "trap": "Modern official: 'mille-sept-cent-quatre-vingt-neuf'. Traditional reading: 'dix-sept-cent...'. All components hyphenated."
    },
    {
        "num": "H.2",
        "year": "1998",
        "event": "Victoire de la France à la Coupe du Monde de Football",
        "pts": "2.5",
        "answer": "mille-neuf-cent-quatre-vingt-dix-huit",
        "alt_answer": "dix-neuf-cent-quatre-vingt-dix-huit",
        "trap": "1000 + 900 + 98 (4 × 20 + 18). Cent and vingt both drop '-s' because subsequent numerals follow."
    },
    {
        "num": "H.3",
        "year": "2024",
        "event": "Jeux Olympiques et Paralympiques de Paris",
        "pts": "2.5",
        "answer": "deux-mille-vingt-quatre",
        "alt_answer": None,
        "pts": "2.5",
        "trap": "2000s years always start with 'deux-mille' (never *vingt-cent*). 'mille' never takes an '-s'."
    },
    {
        "num": "H.4",
        "year": "1515",
        "event": "Bataille de Marignan (François Ier)",
        "pts": "2.5",
        "answer": "mille-cinq-cent-quinze",
        "alt_answer": "quinze-cent-quinze",
        "trap": "Standard cardinal: 'mille-cinq-cent-quinze'. Famous mnemonic: 'quinze-cent-quinze'."
    }
]

# ----------------------------------------------------------------------
# WORD DOCUMENT XML HELPERS
# ----------------------------------------------------------------------

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_cell_box_border(cell, color_hex="CBD5E1", sz="4"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def set_cell_bottom_border(cell, color_hex="CBD5E1", sz="6"):
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)

def make_row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

# ----------------------------------------------------------------------
# WORD DOCUMENT GENERATION (STUDENT EXAM / TEACHER KEY / WORKBOOK)
# ----------------------------------------------------------------------

def generate_docx_document(file_path, mode="student"):
    """
    mode:
      - 'student': Clean exam paper with candidate info header, instructions, fillable answer boxes, point badges. NO answers.
      - 'teacher': Full exam paper with answers filled in bold navy, trap notes, scoring rubric.
      - 'workbook': Comprehensive workbook with cheat sheet, practice sections, and answer key at the back.
    """
    print(f"Generating DOCX ({mode}): {file_path} ...")
    doc = Document()

    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

    COLOR_NAVY = RGBColor(26, 54, 93)       # #1A365D
    COLOR_CRIMSON = RGBColor(155, 44, 44)   # #9B2C2C
    COLOR_SLATE = RGBColor(45, 55, 72)      # #2D3748
    COLOR_MUTED = RGBColor(113, 128, 150)   # #718096
    COLOR_PLACEHOLDER = RGBColor(148, 163, 184) # #94A3B8
    COLOR_STUDENT_ANS = RGBColor(15, 23, 42)

    # 1. HEADER HERO / CANDIDATE BLOCK
    if mode in ["student", "teacher"]:
        title_p = doc.add_paragraph()
        title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        tr = title_p.add_run("ÉPREUVE DE FRANÇAIS : MAÎTRISE DES NOMBRES (0 À 10 000)\n")
        tr.font.name = "Arial"
        tr.font.size = Pt(16)
        tr.font.bold = True
        tr.font.color.rgb = COLOR_NAVY

        sub_title = "OFFICIAL EXAMINATION PAPER — STUDENT COPY" if mode == "student" else "EXAMINATION GRADING KEY & TEACHER RUBRIC"
        tr2 = title_p.add_run(f"{sub_title}\n")
        tr2.font.name = "Arial"
        tr2.font.size = Pt(11)
        tr2.font.bold = True
        tr2.font.color.rgb = COLOR_CRIMSON if mode == "student" else COLOR_NAVY

        tr3 = title_p.add_run("French Language Assessment • Cardinal Numerals & Morphology • 1990 Spelling Reform")
        tr3.font.name = "Arial"
        tr3.font.size = Pt(9)
        tr3.font.italic = True
        tr3.font.color.rgb = COLOR_MUTED

        # Candidate Details Table
        cand_table = doc.add_table(rows=2, cols=2)
        cand_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cand_table.autofit = False
        cand_widths = [Inches(4.4), Inches(2.6)]

        for r_idx in range(2):
            for c_idx in range(2):
                cell = cand_table.cell(r_idx, c_idx)
                cell.width = cand_widths[c_idx]
                set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
                set_cell_box_border(cell, "CBD5E1", "4")
                set_cell_background(cell, "F8FAFC")

        # Cell (0,0): Student Name & Date
        c00 = cand_table.cell(0, 0).paragraphs[0]
        r = c00.add_run("Nom de l'étudiant(e) / Name: ")
        r.font.bold = True
        r.font.size = Pt(9.5)
        c00.add_run("____________________________________\n")
        r_d = c00.add_run("Date de l'examen / Date: ")
        r_d.font.bold = True
        r_d.font.size = Pt(9.5)
        c00.add_run("__________________")

        # Cell (0,1): Score Box
        c01 = cand_table.cell(0, 1).paragraphs[0]
        c01.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_s1 = c01.add_run("NOTE FINALE / SCORE\n")
        r_s1.font.bold = True
        r_s1.font.size = Pt(9)
        r_s1.font.color.rgb = COLOR_CRIMSON
        score_val = "          / 100 points" if mode == "student" else "  100 / 100 points (KEY)  "
        r_s2 = c01.add_run(score_val)
        r_s2.font.bold = True
        r_s2.font.size = Pt(13)
        r_s2.font.color.rgb = COLOR_NAVY

        # Cell (1,0): Class & Candidate ID
        c10 = cand_table.cell(1, 0).paragraphs[0]
        r_c = c10.add_run("Classe / Section: ")
        r_c.font.bold = True
        r_c.font.size = Pt(9.5)
        c10.add_run("_________________    ")
        r_id = c10.add_run("N° Étudiant: ")
        r_id.font.bold = True
        r_id.font.size = Pt(9.5)
        c10.add_run("___________")

        # Cell (1,1): Exam Conditions
        c11 = cand_table.cell(1, 1).paragraphs[0]
        c11.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_t = c11.add_run("Durée / Time: 60 minutes\nCalculatrice interdite (No aids)")
        r_t.font.size = Pt(8.5)
        r_t.font.italic = True
        r_t.font.color.rgb = COLOR_MUTED

        doc.add_paragraph()

        # Instructions Callout Box
        inst_table = doc.add_table(rows=1, cols=1)
        inst_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        inst_cell = inst_table.cell(0, 0)
        set_cell_background(inst_cell, "FEFCBF" if mode == "student" else "EDF2F7")
        set_cell_box_border(inst_cell, "D69E2E" if mode == "student" else "CBD5E1", "6")
        set_cell_margins(inst_cell, top=100, bottom=100, left=140, right=140)

        ip = inst_cell.paragraphs[0]
        ir_t = ip.add_run("CONSIGNES DE L'EXAMEN / CANDIDATE INSTRUCTIONS:\n")
        ir_t.font.bold = True
        ir_t.font.size = Pt(9.5)
        ir_t.font.color.rgb = COLOR_CRIMSON

        inst_text = (
            "1. Orthographe officielle de 1990: Conformément aux rectifications orthographiques officielles, liez TOUS les mots d'un nombre composé par des traits d'union sans exception (ex: vingt-et-un, soixante-et-onze, trois-mille-deux-cent-quatre-vingts).\n"
            "2. Accord de 'cent' et 'vingt': Accordez au pluriel (-s) uniquement s'ils sont multipliés ET qu'aucun chiffre ne suit (ex: deux-cents, quatre-vingts vs deux-cent-cinq, quatre-vingt-un).\n"
            "3. Règle de 'mille': Le mot 'mille' est strictement invariable (jamais de -s).\n"
            "4. Modalité de saisie: Tapez votre réponse directement dans les encadrés grisés ci-dessous, ou écrivez lisiblement à la main."
        )
        ir_b = ip.add_run(inst_text)
        ir_b.font.size = Pt(8.5)
        ir_b.font.color.rgb = COLOR_SLATE

        doc.add_paragraph()

    else:
        # Master Workbook Hero
        banner_table = doc.add_table(rows=1, cols=1)
        banner_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        banner_cell = banner_table.cell(0, 0)
        set_cell_background(banner_cell, "EDF2F7")
        set_cell_box_border(banner_cell, "1A365D", "8")
        set_cell_margins(banner_cell, top=180, bottom=180, left=200, right=200)

        p = banner_cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r1 = p.add_run("FRENCH NUMBERS PRACTICE WORKBOOK (0–10,000)\n")
        r1.font.bold = True
        r1.font.size = Pt(18)
        r1.font.color.rgb = COLOR_NAVY
        r2 = p.add_run("Comprehensive Curriculum, Diagnostic Phases & Fluency Drills\n")
        r2.font.bold = True
        r2.font.size = Pt(11)
        r2.font.color.rgb = COLOR_SLATE
        r3 = p.add_run("Official 1990 Spelling Reform Orthography • Complete Annotated Answer Key Included")
        r3.font.italic = True
        r3.font.size = Pt(9)
        r3.font.color.rgb = COLOR_MUTED

        doc.add_paragraph()

        # Cheat sheet
        rules_table = doc.add_table(rows=1, cols=1)
        rules_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        rcell = rules_table.cell(0, 0)
        set_cell_background(rcell, "FEFCBF")
        set_cell_box_border(rcell, "D69E2E", "6")
        set_cell_margins(rcell, top=120, bottom=120, left=160, right=160)
        rp = rcell.paragraphs[0]
        rt = rp.add_run("ESSENTIAL 1990 SPELLING REFORM RULES & TRAP PREVENTION\n")
        rt.font.bold = True
        rt.font.size = Pt(9.5)
        rt.font.color.rgb = COLOR_CRIMSON
        rb = rp.add_run(
            "• 1990 Systematic Hyphens: ALL words forming a compound number are hyphenated (vingt-et-un, cent-un, trois-mille-deux-cent-quatre-vingts).\n"
            "• Cent: Multiplied hundreds take '-s' ONLY when terminating the number (deux-cents vs deux-cent-cinq). Bare 100 is always 'cent' (never *un cent*). Zero 'et' after hundreds (cent-un).\n"
            "• Vingt (80 vs 81–99): 80 = quatre-vingts (takes -s). 81–99 drop the -s (81 = quatre-vingt-un). Notice: 81 and 91 NEVER take 'et'!\n"
            "• Mille: 1,000 is bare 'mille' (never *un mille*). 'Mille' is strictly invariable and NEVER takes an -s (deux-mille).\n"
            "• Conjunction 'et': Restricted to 21, 31, 41, 51, 61, and 71."
        )
        rb.font.size = Pt(8.5)
        rb.font.color.rgb = COLOR_SLATE
        doc.add_paragraph()

    # ==========================================
    # SECTION 1: PHASE-BY-PHASE DIAGNOSTICS
    # ==========================================
    s1_head = doc.add_paragraph()
    s1_run = s1_head.add_run("SECTION 1: Phase-by-Phase Diagnostic (51 Points Total)")
    s1_run.font.name = "Arial"
    s1_run.font.size = Pt(14)
    s1_run.font.bold = True
    s1_run.font.color.rgb = COLOR_NAVY

    s1_desc = doc.add_paragraph()
    s1_drun = s1_desc.add_run("Complete each diagnostic question below. Type your response in the shaded box or write clearly. (1 point per question)")
    s1_drun.font.size = Pt(9)
    s1_drun.font.italic = True
    s1_drun.font.color.rgb = COLOR_MUTED

    for phase in PHASES_DATA:
        p_head = doc.add_paragraph()
        p_run = p_head.add_run(f"{phase['phase_id']}: {phase['title']} — {phase['pts']}")
        p_run.font.name = "Arial"
        p_run.font.size = Pt(11)
        p_run.font.bold = True
        p_run.font.color.rgb = COLOR_CRIMSON

        p_sub = doc.add_paragraph()
        p_srun = p_sub.add_run(phase['desc'])
        p_srun.font.size = Pt(8.5)
        p_srun.font.italic = True
        p_srun.font.color.rgb = COLOR_MUTED

        # Build table for phase questions
        # Columns: [0.6 in (Num), 2.5 in (Prompt), 3.2 in (Answer Box), 0.7 in (Score)] = 7.0 in
        cols_w = [Inches(0.6), Inches(2.5), Inches(3.2), Inches(0.7)]
        q_table = doc.add_table(rows=len(phase["questions"]), cols=4)
        q_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        q_table.autofit = False

        for idx, q in enumerate(phase["questions"]):
            row = q_table.rows[idx]
            make_row_cant_split(row)

            c_num = row.cells[0]
            c_prompt = row.cells[1]
            c_ans = row.cells[2]
            c_pts = row.cells[3]

            for ci, w in enumerate(cols_w):
                row.cells[ci].width = w
                set_cell_margins(row.cells[ci], top=70, bottom=70, left=80, right=80)

            # Item Num
            p_n = c_num.paragraphs[0]
            rn = p_n.add_run(q["num"])
            rn.font.bold = True
            rn.font.size = Pt(9)
            rn.font.color.rgb = COLOR_SLATE

            # Prompt
            p_pr = c_prompt.paragraphs[0]
            rp = p_pr.add_run(q["prompt"])
            rp.font.bold = True
            rp.font.size = Pt(9)
            rp.font.color.rgb = COLOR_NAVY

            # Answer Box
            set_cell_background(c_ans, "F8FAFC")
            set_cell_box_border(c_ans, "CBD5E1", "4")
            p_ans = c_ans.paragraphs[0]

            if mode == "student":
                ra = p_ans.add_run("[ Type answer here / Tapez votre réponse ]")
                ra.font.italic = True
                ra.font.size = Pt(8.5)
                ra.font.color.rgb = COLOR_PLACEHOLDER
            else: # teacher or teacher key view
                ra = p_ans.add_run(q["answer"])
                ra.font.bold = True
                ra.font.size = Pt(9.5)
                ra.font.color.rgb = COLOR_NAVY
                if mode == "teacher":
                    ra_trap = p_ans.add_run(f"\n[Note: {q['trap']}]")
                    ra_trap.font.size = Pt(7.5)
                    ra_trap.font.color.rgb = COLOR_CRIMSON

            # Points / Score badge
            p_pt = c_pts.paragraphs[0]
            p_pt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            if mode == "student":
                rpt = p_pt.add_run("[   / 1 pt]")
            else:
                rpt = p_pt.add_run("[ 1 / 1 pt]")
            rpt.font.size = Pt(8)
            rpt.font.color.rgb = COLOR_MUTED

        doc.add_paragraph()

    # ==========================================
    # SECTION 2: COMPREHENSIVE DRILLS
    # ==========================================
    doc.add_page_break()
    s2_head = doc.add_paragraph()
    s2_run = s2_head.add_run("SECTION 2: Randomized Comprehensive Drills (49 Points Total)")
    s2_run.font.name = "Arial"
    s2_run.font.size = Pt(14)
    s2_run.font.bold = True
    s2_run.font.color.rgb = COLOR_NAVY

    # Part A: 30 Mixed Drills
    pa_head = doc.add_paragraph()
    pa_run = pa_head.add_run("Part A: 30 Mixed Cardinal Drills (0 to 10,000) — 30 pts (1 pt each)")
    pa_run.font.name = "Arial"
    pa_run.font.size = Pt(11)
    pa_run.font.bold = True
    pa_run.font.color.rgb = COLOR_CRIMSON

    d_table = doc.add_table(rows=len(SECTION_2_DRILLS), cols=4)
    d_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    d_table.autofit = False

    for idx, item in enumerate(SECTION_2_DRILLS):
        row = d_table.rows[idx]
        make_row_cant_split(row)

        c_num = row.cells[0]
        c_prompt = row.cells[1]
        c_ans = row.cells[2]
        c_pts = row.cells[3]

        for ci, w in enumerate(cols_w):
            row.cells[ci].width = w
            set_cell_margins(row.cells[ci], top=60, bottom=60, left=80, right=80)

        # Num
        p_n = c_num.paragraphs[0]
        rn = p_n.add_run(item["num"])
        rn.font.bold = True
        rn.font.size = Pt(8.5)
        rn.font.color.rgb = COLOR_SLATE

        # Prompt
        p_pr = c_prompt.paragraphs[0]
        rp = p_pr.add_run(item["prompt"])
        rp.font.bold = True
        rp.font.size = Pt(8.5)
        rp.font.color.rgb = COLOR_NAVY

        # Answer Box
        set_cell_background(c_ans, "F8FAFC")
        set_cell_box_border(c_ans, "CBD5E1", "4")
        p_ans = c_ans.paragraphs[0]

        if mode == "student":
            ra = p_ans.add_run("[ Type answer here ]")
            ra.font.italic = True
            ra.font.size = Pt(8)
            ra.font.color.rgb = COLOR_PLACEHOLDER
        else:
            ra = p_ans.add_run(item["answer"])
            ra.font.bold = True
            ra.font.size = Pt(9)
            ra.font.color.rgb = COLOR_NAVY
            if mode == "teacher":
                ra_trap = p_ans.add_run(f"\n[Note: {item['trap']}]")
                ra_trap.font.size = Pt(7.5)
                ra_trap.font.color.rgb = COLOR_CRIMSON

        # Pts
        p_pt = c_pts.paragraphs[0]
        p_pt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rpt = p_pt.add_run("[   / 1 pt]" if mode == "student" else "[ 1 / 1 pt]")
        rpt.font.size = Pt(8)
        rpt.font.color.rgb = COLOR_MUTED

    doc.add_paragraph()

    # Part B: Phone Numbers
    doc.add_page_break()
    pb_head = doc.add_paragraph()
    pb_run = pb_head.add_run("Part B: Real-World Fluency — French Phone Numbers — 9 pts (3 pts each)")
    pb_run.font.name = "Arial"
    pb_run.font.size = Pt(11)
    pb_run.font.bold = True
    pb_run.font.color.rgb = COLOR_CRIMSON

    pb_desc = doc.add_paragraph()
    pb_drun = pb_desc.add_run("In France, phone numbers are grouped and pronounced in 2-digit pairs. Write out each pair in words:")
    pb_drun.font.size = Pt(8.5)
    pb_drun.font.italic = True
    pb_drun.font.color.rgb = COLOR_MUTED

    phone_cols_w = [Inches(2.5), Inches(3.8), Inches(0.7)]
    p_table = doc.add_table(rows=len(SECTION_2_PHONE_NUMBERS), cols=3)
    p_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    p_table.autofit = False

    for idx, item in enumerate(SECTION_2_PHONE_NUMBERS):
        row = p_table.rows[idx]
        make_row_cant_split(row)

        c_prompt = row.cells[0]
        c_ans = row.cells[1]
        c_pts = row.cells[2]

        for ci, w in enumerate(phone_cols_w):
            row.cells[ci].width = w
            set_cell_margins(row.cells[ci], top=80, bottom=80, left=90, right=90)

        # Prompt
        p_pr = c_prompt.paragraphs[0]
        rp1 = p_pr.add_run(f"{item['num']}  {item['raw']}\n")
        rp1.font.bold = True
        rp1.font.size = Pt(9.5)
        rp1.font.color.rgb = COLOR_NAVY
        rp2 = p_pr.add_run(f"({item['description']})")
        rp2.font.size = Pt(8)
        rp2.font.italic = True
        rp2.font.color.rgb = COLOR_MUTED

        # Answer Box
        set_cell_background(c_ans, "F8FAFC")
        set_cell_box_border(c_ans, "CBD5E1", "4")
        p_ans = c_ans.paragraphs[0]

        if mode == "student":
            ra = p_ans.add_run("P1: [         ]  P2: [         ]  P3: [         ]\nP4: [         ]  P5: [         ]")
            ra.font.size = Pt(8.5)
            ra.font.color.rgb = COLOR_PLACEHOLDER
        else:
            ra = p_ans.add_run(item["answer"])
            ra.font.bold = True
            ra.font.size = Pt(9)
            ra.font.color.rgb = COLOR_NAVY
            if mode == "teacher":
                ra_trap = p_ans.add_run(f"\n[Note: {item['trap']}]")
                ra_trap.font.size = Pt(7.5)
                ra_trap.font.color.rgb = COLOR_CRIMSON

        # Pts
        p_pt = c_pts.paragraphs[0]
        p_pt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rpt = p_pt.add_run("[   / 3 pts]" if mode == "student" else "[ 3 / 3 pts]")
        rpt.font.size = Pt(8)
        rpt.font.color.rgb = COLOR_MUTED

    doc.add_paragraph()

    # Part C: Historical Years
    pc_head = doc.add_paragraph()
    pc_run = pc_head.add_run("Part C: Real-World Fluency — Historical Calendar Years — 10 pts (2.5 pts each)")
    pc_run.font.name = "Arial"
    pc_run.font.size = Pt(11)
    pc_run.font.bold = True
    pc_run.font.color.rgb = COLOR_CRIMSON

    y_table = doc.add_table(rows=len(SECTION_2_HISTORICAL_YEARS), cols=3)
    y_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    y_table.autofit = False

    for idx, item in enumerate(SECTION_2_HISTORICAL_YEARS):
        row = y_table.rows[idx]
        make_row_cant_split(row)

        c_prompt = row.cells[0]
        c_ans = row.cells[1]
        c_pts = row.cells[2]

        for ci, w in enumerate(phone_cols_w):
            row.cells[ci].width = w
            set_cell_margins(row.cells[ci], top=80, bottom=80, left=90, right=90)

        # Prompt
        p_pr = c_prompt.paragraphs[0]
        rp1 = p_pr.add_run(f"{item['num']}  Year {item['year']}\n")
        rp1.font.bold = True
        rp1.font.size = Pt(9.5)
        rp1.font.color.rgb = COLOR_NAVY
        rp2 = p_pr.add_run(f"({item['event']})")
        rp2.font.size = Pt(8)
        rp2.font.italic = True
        rp2.font.color.rgb = COLOR_MUTED

        # Answer Box
        set_cell_background(c_ans, "F8FAFC")
        set_cell_box_border(c_ans, "CBD5E1", "4")
        p_ans = c_ans.paragraphs[0]

        if mode == "student":
            ra = p_ans.add_run("[ Type full French year in words here ]")
            ra.font.size = Pt(8.5)
            ra.font.italic = True
            ra.font.color.rgb = COLOR_PLACEHOLDER
        else:
            ra = p_ans.add_run(item["answer"])
            ra.font.bold = True
            ra.font.size = Pt(9)
            ra.font.color.rgb = COLOR_NAVY
            if item["alt_answer"]:
                ra_alt = p_ans.add_run(f"\n(Accepted alternative: {item['alt_answer']})")
                ra_alt.font.size = Pt(8)
                ra_alt.font.italic = True
                ra_alt.font.color.rgb = COLOR_MUTED
            if mode == "teacher":
                ra_trap = p_ans.add_run(f"\n[Note: {item['trap']}]")
                ra_trap.font.size = Pt(7.5)
                ra_trap.font.color.rgb = COLOR_CRIMSON

        # Pts
        p_pt = c_pts.paragraphs[0]
        p_pt.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rpt = p_pt.add_run("[   / 2.5 pts]" if mode == "student" else "[ 2.5 / 2.5 pts]")
        rpt.font.size = Pt(8)
        rpt.font.color.rgb = COLOR_MUTED

    # ==========================================
    # SECTION 3: ANSWER KEY (IF WORKBOOK MODE)
    # ==========================================
    if mode == "workbook":
        doc.add_page_break()
        s3_head = doc.add_paragraph()
        s3_run = s3_head.add_run("SECTION 3: Complete Answer Key & Trap Annotations")
        s3_run.font.name = "Arial"
        s3_run.font.size = Pt(16)
        s3_run.font.bold = True
        s3_run.font.color.rgb = COLOR_NAVY

        s3_desc = doc.add_paragraph()
        s3_drun = s3_desc.add_run("Teacher & self-study reference: full solutions with explicit linguistic justifications and 1990 reform rule references.")
        s3_drun.font.size = Pt(9.5)
        s3_drun.font.italic = True
        s3_drun.font.color.rgb = COLOR_MUTED

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
                row = sol_table.rows[idx]
                make_row_cant_split(row)
                c_num = row.cells[0]
                c_ans = row.cells[1]
                c_trap = row.cells[2]
                c_num.width = Inches(0.6)
                c_ans.width = Inches(2.2)
                c_trap.width = Inches(4.2)
                for ci in range(3):
                    set_cell_margins(row.cells[ci], top=50, bottom=50, left=60, right=60)
                    set_cell_background(row.cells[ci], "F7FAFC")
                    set_cell_box_border(row.cells[ci], "CBD5E1", "2")

                p1 = c_num.paragraphs[0]
                r1 = p1.add_run(q["num"])
                r1.font.bold = True
                r1.font.size = Pt(8.5)
                r1.font.color.rgb = COLOR_SLATE

                p2 = c_ans.paragraphs[0]
                r2 = p2.add_run(q["answer"])
                r2.font.bold = True
                r2.font.size = Pt(9)
                r2.font.color.rgb = COLOR_NAVY

                p3 = c_trap.paragraphs[0]
                r3_lbl = p3.add_run("[Rule / Trap] ")
                r3_lbl.font.bold = True
                r3_lbl.font.size = Pt(8)
                r3_lbl.font.color.rgb = COLOR_CRIMSON
                r3 = p3.add_run(q["trap"])
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
            row = d_sol_table.rows[idx]
            make_row_cant_split(row)
            c_num = row.cells[0]
            c_ans = row.cells[1]
            c_trap = row.cells[2]
            c_num.width = Inches(0.6)
            c_ans.width = Inches(2.2)
            c_trap.width = Inches(4.2)
            for ci in range(3):
                set_cell_margins(row.cells[ci], top=45, bottom=45, left=60, right=60)
                set_cell_background(row.cells[ci], "F7FAFC")
                set_cell_box_border(row.cells[ci], "CBD5E1", "2")

            p1 = c_num.paragraphs[0]
            r1 = p1.add_run(item["num"])
            r1.font.bold = True
            r1.font.size = Pt(8.5)
            r1.font.color.rgb = COLOR_SLATE

            p2 = c_ans.paragraphs[0]
            r2 = p2.add_run(item["answer"])
            r2.font.bold = True
            r2.font.size = Pt(9)
            r2.font.color.rgb = COLOR_NAVY

            p3 = c_trap.paragraphs[0]
            r3_lbl = p3.add_run("[Note] ")
            r3_lbl.font.bold = True
            r3_lbl.font.size = Pt(8)
            r3_lbl.font.color.rgb = COLOR_CRIMSON
            r3 = p3.add_run(item["trap"])
            r3.font.size = Pt(8)
            r3.font.color.rgb = COLOR_SLATE

        doc.add_paragraph()

        # Phone Answers
        pb_ans_head = doc.add_paragraph()
        pb_ans_run = pb_ans_head.add_run("Solutions: Section 2 Phone Numbers (Part B)")
        pb_ans_run.font.name = "Arial"
        pb_ans_run.font.size = Pt(11)
        pb_ans_run.font.bold = True
        pb_ans_run.font.color.rgb = COLOR_CRIMSON

        p_sol_table = doc.add_table(rows=len(SECTION_2_PHONE_NUMBERS), cols=3)
        p_sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for idx, item in enumerate(SECTION_2_PHONE_NUMBERS):
            row = p_sol_table.rows[idx]
            make_row_cant_split(row)
            c1 = row.cells[0]
            c2 = row.cells[1]
            c3 = row.cells[2]
            c1.width = Inches(0.9)
            c2.width = Inches(2.7)
            c3.width = Inches(3.4)
            for ci in range(3):
                set_cell_margins(row.cells[ci], top=50, bottom=50, left=60, right=60)
                set_cell_background(row.cells[ci], "F7FAFC")
                set_cell_box_border(row.cells[ci], "CBD5E1", "2")

            p1 = c1.paragraphs[0]
            r1 = p1.add_run(f"{item['num']}\n{item['raw']}")
            r1.font.bold = True
            r1.font.size = Pt(8.5)
            r1.font.color.rgb = COLOR_SLATE

            p2 = c2.paragraphs[0]
            r2 = p2.add_run(item["answer"])
            r2.font.bold = True
            r2.font.size = Pt(8.5)
            r2.font.color.rgb = COLOR_NAVY

            p3 = c3.paragraphs[0]
            r3_lbl = p3.add_run("[Note] ")
            r3_lbl.font.bold = True
            r3_lbl.font.size = Pt(8)
            r3_lbl.font.color.rgb = COLOR_CRIMSON
            r3 = p3.add_run(item["trap"])
            r3.font.size = Pt(8)
            r3.font.color.rgb = COLOR_SLATE

        doc.add_paragraph()

        # Historical Year Answers
        pc_ans_head = doc.add_paragraph()
        pc_ans_run = pc_ans_head.add_run("Solutions: Section 2 Historical Years (Part C)")
        pc_ans_run.font.name = "Arial"
        pc_ans_run.font.size = Pt(11)
        pc_ans_run.font.bold = True
        pc_ans_run.font.color.rgb = COLOR_CRIMSON

        y_sol_table = doc.add_table(rows=len(SECTION_2_HISTORICAL_YEARS), cols=3)
        y_sol_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        for idx, item in enumerate(SECTION_2_HISTORICAL_YEARS):
            row = y_sol_table.rows[idx]
            make_row_cant_split(row)
            c1 = row.cells[0]
            c2 = row.cells[1]
            c3 = row.cells[2]
            c1.width = Inches(0.9)
            c2.width = Inches(2.7)
            c3.width = Inches(3.4)
            for ci in range(3):
                set_cell_margins(row.cells[ci], top=50, bottom=50, left=60, right=60)
                set_cell_background(row.cells[ci], "F7FAFC")
                set_cell_box_border(row.cells[ci], "CBD5E1", "2")

            p1 = c1.paragraphs[0]
            r1 = p1.add_run(f"{item['num']}\n{item['year']}")
            r1.font.bold = True
            r1.font.size = Pt(8.5)
            r1.font.color.rgb = COLOR_SLATE

            p2 = c2.paragraphs[0]
            r2 = p2.add_run(item["answer"])
            r2.font.bold = True
            r2.font.size = Pt(8.5)
            r2.font.color.rgb = COLOR_NAVY
            if item["alt_answer"]:
                r2_alt = p2.add_run(f"\nAlt: {item['alt_answer']}")
                r2_alt.font.size = Pt(7.5)
                r2_alt.font.italic = True
                r2_alt.font.color.rgb = COLOR_MUTED

            p3 = c3.paragraphs[0]
            r3_lbl = p3.add_run("[Note] ")
            r3_lbl.font.bold = True
            r3_lbl.font.size = Pt(8)
            r3_lbl.font.color.rgb = COLOR_CRIMSON
            r3 = p3.add_run(item["trap"])
            r3.font.size = Pt(8)
            r3.font.color.rgb = COLOR_SLATE

    doc.save(file_path)
    print(f"Saved: {file_path}")

# ----------------------------------------------------------------------
# REPORTLAB STUDENT EXAM PDF GENERATOR
# ----------------------------------------------------------------------

class ExamNumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(ExamNumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(ExamNumberedCanvas, self).showPage()
        super(ExamNumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "ÉPREUVE DE FRANÇAIS — NOMBRES DE 0 À 10 000")
            self.drawRightString(8.5 * inch - 54, 11 * inch - 36, "EXAMEN OFFICIEL • 100 POINTS")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)
        
        # Footer
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 46, 8.5 * inch - 54, 46)
        self.drawString(54, 32, "Curriculum de Français • Orthographe 1990 • Ne rien inscrire en dessous de cette ligne")
        page_str = f"Page {self._pageNumber} / {page_count}"
        self.drawRightString(8.5 * inch - 54, 32, page_str)
        self.restoreState()

def generate_pdf_exam(file_path, mode="student"):
    print(f"Generating PDF ({mode}): {file_path} ...")
    doc = SimpleDocTemplate(
        file_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()
    NAVY = colors.HexColor("#1A365D")
    CRIMSON = colors.HexColor("#9B2C2C")
    SLATE = colors.HexColor("#2D3748")
    MUTED = colors.HexColor("#718096")
    BOX_BG = colors.HexColor("#F8FAFC")
    BOX_BORDER = colors.HexColor("#CBD5E1")
    AMBER_BG = colors.HexColor("#FEFCBF")
    AMBER_BORDER = colors.HexColor("#D69E2E")

    h1_style = ParagraphStyle('SecH1', fontName='Helvetica-Bold', fontSize=14, leading=18, textColor=NAVY, spaceBefore=10, spaceAfter=6, keepWithNext=True)
    h2_style = ParagraphStyle('SecH2', fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=CRIMSON, spaceBefore=8, spaceAfter=4, keepWithNext=True)
    hint_style = ParagraphStyle('HintStyle', fontName='Helvetica-Oblique', fontSize=8, leading=11, textColor=MUTED)
    q_style = ParagraphStyle('QStyle', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=NAVY)
    q_num_style = ParagraphStyle('QNumStyle', fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=SLATE)
    pts_style = ParagraphStyle('PtsStyle', fontName='Helvetica', fontSize=7.5, leading=10, textColor=MUTED, alignment=2)
    ans_style = ParagraphStyle('AnsStyle', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=NAVY)
    trap_style = ParagraphStyle('TrapStyle', fontName='Helvetica', fontSize=7.5, leading=10, textColor=CRIMSON)

    story = []

    # 1. Candidate Header Block
    sub_title = "CAHIER D'EXAMEN OFFICIEL — COPIE DE L'ÉTUDIANT(E)" if mode == "student" else "CORRIGÉ OFFICIEL & GRILLE DE NOTATION"
    header_html = f"""
    <para align="center">
    <b><font size="15" color="#1A365D">ÉPREUVE DE FRANÇAIS : MAÎTRISE DES NOMBRES (0 À 10 000)</font></b><br/>
    <b><font size="10.5" color="#9B2C2C">{sub_title}</font></b><br/>
    <font size="8" color="#718096">Évaluation sommative de morphologie numérique • Rectifications orthographiques de 1990</font>
    </para>
    """
    story.append(Paragraph(header_html, styles['Normal']))
    story.append(Spacer(1, 8))

    # Details table
    score_display = "<b>NOTE:</b> &nbsp; _______ / 100" if mode == "student" else "<b>NOTE:</b> &nbsp; <b>100 / 100 (CORRIGÉ)</b>"
    cand_data = [
        [
            Paragraph("<b>Nom de l'élève:</b> ___________________________<br/><b>Date:</b> ___________________", styles['Normal']),
            Paragraph(f"<para align='center'><font size='11' color='#9B2C2C'>{score_display}</font><br/><font size='7.5' color='#718096'>Barème: 100 points au total</font></para>", styles['Normal'])
        ],
        [
            Paragraph("<b>Classe / Groupe:</b> _________________________<br/><b>N° Candidat:</b> ________________", styles['Normal']),
            Paragraph("<para align='center'><b>Durée:</b> 60 minutes<br/><font size='7.5' color='#718096'>Calculatrice et documents interdits</font></para>", styles['Normal'])
        ]
    ]
    cand_table = Table(cand_data, colWidths=[4.4 * inch, 2.6 * inch])
    cand_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BOX_BG),
        ('BOX', (0, 0), (-1, -1), 1, BOX_BORDER),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BOX_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    story.append(cand_table)
    story.append(Spacer(1, 8))

    # Instructions box
    inst_html = """
    <b>CONSIGNES D'ÉVALUATION:</b><br/>
    1. Liez <b>tous les composants</b> des nombres composés par un trait d'union (réforme 1990 : <i>vingt-et-un</i>, <i>trois-mille-deux-cents</i>).<br/>
    2. <i>Cent</i> et <i>vingt</i> prennent un <b>-s</b> uniquement s'ils sont multipliés et qu'aucun nombre ne suit.<br/>
    3. <i>Mille</i> est strictement <b>invariable</b>. Inscrivez vos réponses dans les encadrés réservés.
    """
    inst_table = Table([[Paragraph(inst_html, ParagraphStyle('Inst', fontName='Helvetica', fontSize=8, leading=11, textColor=SLATE))]], colWidths=[7.0 * inch])
    inst_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), AMBER_BG),
        ('BOX', (0, 0), (-1, -1), 0.8, AMBER_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(inst_table)
    story.append(Spacer(1, 10))

    # SECTION 1
    story.append(Paragraph("SECTION 1: Phase-by-Phase Diagnostic (51 Points Total)", h1_style))
    story.append(Paragraph("<i>Répondez à chaque question dans la zone réservée. (1 point par question)</i>", hint_style))
    story.append(Spacer(1, 6))

    for phase in PHASES_DATA:
        p_head = Paragraph(f"<b>{phase['phase_id']}: {phase['title']}</b> &nbsp;—&nbsp; <font color='#718096' size='8'>{phase['pts']}</font>", h2_style)
        
        q_rows = []
        for q in phase["questions"]:
            c_num = Paragraph(f"<b>{q['num']}</b>", q_num_style)
            c_pr = Paragraph(q["prompt"], q_style)
            if mode == "student":
                c_ans = Paragraph("<font color='#CBD5E1'><i>Zone de réponse / Réponse écrite ici</i></font>", ParagraphStyle('Blank', fontName='Helvetica-Oblique', fontSize=8, leading=10, textColor=MUTED))
                c_pts = Paragraph("[ &nbsp; / 1 pt]", pts_style)
            else:
                c_ans = Paragraph(f"<b>{q['answer']}</b><br/><font color='#9B2C2C' size='7'><i>[Note: {q['trap']}]</i></font>", ans_style)
                c_pts = Paragraph("[ 1 / 1 pt]", pts_style)
            q_rows.append([c_num, c_pr, c_ans, c_pts])

        t = Table(q_rows, colWidths=[0.55 * inch, 2.35 * inch, 3.4 * inch, 0.7 * inch])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('BACKGROUND', (2, 0), (2, -1), BOX_BG),
            ('BOX', (2, 0), (2, -1), 0.5, BOX_BORDER),
            ('INNERGRID', (2, 0), (2, -1), 0.5, colors.HexColor("#E2E8F0")),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#EDF2F7")),
        ]))
        story.append(KeepTogether([p_head, Spacer(1, 2), t, Spacer(1, 6)]))

    # SECTION 2
    story.append(PageBreak())
    story.append(Paragraph("SECTION 2: Randomized Comprehensive Drills (49 Points Total)", h1_style))
    story.append(Paragraph("<b>Part A: 30 Mixed Cardinal Drills (0 to 10,000) — 30 Points (1 pt each)</b>", h2_style))
    story.append(Spacer(1, 4))

    d_rows = []
    for item in SECTION_2_DRILLS:
        c_num = Paragraph(f"<b>{item['num']}</b>", q_num_style)
        c_pr = Paragraph(item["prompt"], q_style)
        if mode == "student":
            c_ans = Paragraph("<font color='#CBD5E1'><i>Zone de réponse</i></font>", hint_style)
            c_pts = Paragraph("[ &nbsp; / 1 pt]", pts_style)
        else:
            c_ans = Paragraph(f"<b>{item['answer']}</b><br/><font color='#9B2C2C' size='7'><i>[Note: {item['trap']}]</i></font>", ans_style)
            c_pts = Paragraph("[ 1 / 1 pt]", pts_style)
        d_rows.append([c_num, c_pr, c_ans, c_pts])

    t_drill = Table(d_rows, colWidths=[0.55 * inch, 2.35 * inch, 3.4 * inch, 0.7 * inch])
    t_drill.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3.5),
        ('BACKGROUND', (2, 0), (2, -1), BOX_BG),
        ('BOX', (2, 0), (2, -1), 0.5, BOX_BORDER),
        ('INNERGRID', (2, 0), (2, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#EDF2F7")),
    ]))
    story.append(t_drill)
    story.append(Spacer(1, 10))

    # Part B: Phone Numbers
    story.append(PageBreak())
    story.append(Paragraph("<b>Part B: Real-World Fluency — French Phone Numbers — 9 Points (3 pts each)</b>", h2_style))
    story.append(Paragraph("<i>French phone numbers are pronounced in 2-digit pairs. Write out each pair in words:</i>", hint_style))
    story.append(Spacer(1, 6))

    p_rows = []
    for item in SECTION_2_PHONE_NUMBERS:
        c_pr = Paragraph(f"<b>{item['num']} &nbsp; {item['raw']}</b><br/><font color='#718096' size='7.5'><i>{item['description']}</i></font>", q_style)
        if mode == "student":
            c_ans = Paragraph("<font color='#CBD5E1'>P1: [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ] &nbsp; P2: [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ] &nbsp; P3: [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ]<br/>P4: [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ] &nbsp; P5: [ &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ]</font>", hint_style)
            c_pts = Paragraph("[ &nbsp; / 3 pts]", pts_style)
        else:
            c_ans = Paragraph(f"<b>{item['answer']}</b><br/><font color='#9B2C2C' size='7'><i>[Note: {item['trap']}]</i></font>", ans_style)
            c_pts = Paragraph("[ 3 / 3 pts]", pts_style)
        p_rows.append([c_pr, c_ans, c_pts])

    t_phone = Table(p_rows, colWidths=[2.6 * inch, 3.7 * inch, 0.7 * inch])
    t_phone.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (1, 0), (1, -1), BOX_BG),
        ('BOX', (1, 0), (1, -1), 0.5, BOX_BORDER),
        ('INNERGRID', (1, 0), (1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
    ]))
    story.append(t_phone)
    story.append(Spacer(1, 10))

    # Part C: Historical Years
    story.append(Paragraph("<b>Part C: Real-World Fluency — Historical Calendar Years — 10 Points (2.5 pts each)</b>", h2_style))
    story.append(Spacer(1, 4))

    y_rows = []
    for item in SECTION_2_HISTORICAL_YEARS:
        c_pr = Paragraph(f"<b>{item['num']} &nbsp; Year {item['year']}</b><br/><font color='#718096' size='7.5'><i>{item['event']}</i></font>", q_style)
        if mode == "student":
            c_ans = Paragraph("<font color='#CBD5E1'><i>Zone de réponse (Écrire en lettres)</i></font>", hint_style)
            c_pts = Paragraph("[ &nbsp; / 2.5 pts]", pts_style)
        else:
            alt_txt = f"<br/><font color='#4A5568' size='7'><i>(Alt: {item['alt_answer']})</i></font>" if item.get('alt_answer') else ""
            c_ans = Paragraph(f"<b>{item['answer']}</b>{alt_txt}<br/><font color='#9B2C2C' size='7'><i>[Note: {item['trap']}]</i></font>", ans_style)
            c_pts = Paragraph("[ 2.5 / 2.5 pts]", pts_style)
        y_rows.append([c_pr, c_ans, c_pts])

    t_year = Table(y_rows, colWidths=[2.6 * inch, 3.7 * inch, 0.7 * inch])
    t_year.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('BACKGROUND', (1, 0), (1, -1), BOX_BG),
        ('BOX', (1, 0), (1, -1), 0.5, BOX_BORDER),
        ('INNERGRID', (1, 0), (1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E1")),
    ]))
    story.append(t_year)

    doc.build(story, canvasmaker=ExamNumberedCanvas)
    print(f"Saved: {file_path}")

def main():
    print("=== BUILDING COMPREHENSIVE FRENCH NUMBERS SYSTEM ===")
    
    # 1. Student Exam Paper (DOCX & PDF)
    student_docx = os.path.join(BASE_DIR, "French_Numbers_Exam_Student_Version.docx")
    generate_docx_document(student_docx, mode="student")
    
    student_pdf = os.path.join(BASE_DIR, "French_Numbers_Exam_Student_Version.pdf")
    generate_pdf_exam(student_pdf, mode="student")

    # 2. Teacher Grading Key & Annotated Rubric (DOCX & PDF)
    teacher_docx = os.path.join(BASE_DIR, "French_Numbers_Exam_Teacher_Key.docx")
    generate_docx_document(teacher_docx, mode="teacher")
    
    teacher_pdf = os.path.join(BASE_DIR, "French_Numbers_Exam_Teacher_Key.pdf")
    generate_pdf_exam(teacher_pdf, mode="teacher")

    # 3. Master Practice Workbook (DOCX & PDF)
    workbook_docx = os.path.join(BASE_DIR, "French_Numbers_0-10000_Workbook.docx")
    generate_docx_document(workbook_docx, mode="workbook")

    print("\nALL ARTIFACTS GENERATED SUCCESSFULLY!")

if __name__ == "__main__":
    main()
