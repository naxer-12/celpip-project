#!/usr/bin/env python3
"""
split_roadmaps.py - Split all 6 French Learning Roadmap PDFs (A1, A2, B1, B2, C1, C2) into:
1. Modular Unit PDFs (8 unified curriculum modules per level)
2. Individual Page PDFs (71 single-page worksheets per level)
And deposit into /Users/jainamshah/Desktop/French Material/French_Roadmaps_A1_A2_B1_B2_Split/
with convenience symlinks on Desktop.
"""

import os
import sys
import shutil
import re
import pypdf
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DESKTOP_DIR = Path("/Users/jainamshah/Desktop/French Material")
TARGET_SPLIT_ROOT = DESKTOP_DIR / "French_Roadmaps_A1_A2_B1_B2_Split"

# Import curriculum data
sys.path.append(str(BASE_DIR / "French_A2"))
sys.path.append(str(BASE_DIR / "French_B1"))
sys.path.append(str(BASE_DIR / "French_B2"))
sys.path.append(str(BASE_DIR / "French_C1"))
sys.path.append(str(BASE_DIR / "French_C2"))

from a2_curriculum_data import A2_PAGES_DATA
from b1_curriculum_data import B1_PAGES_DATA
from b2_curriculum_data import B2_PAGES_DATA
from c1_curriculum_data import C1_PAGES_DATA
from c2_curriculum_data import C2_PAGES_DATA

def get_page_title(level_code: str, page_num: int) -> str:
    data_map = {
        "A2": A2_PAGES_DATA,
        "B1": B1_PAGES_DATA,
        "B2": B2_PAGES_DATA,
        "C1": C1_PAGES_DATA,
        "C2": C2_PAGES_DATA,
    }
    if level_code in data_map:
        return data_map[level_code][page_num]["title"]
    return f"A1 Page {page_num}"

# Standard 8 Units for All Levels
def get_level_units(level_code: str, next_level: str):
    return [
        {"index": 1, "title": "Unit 1: Overview, Objectives & Core Themes", "start": 1, "end": 7, "slug": "01_Unit_1_Overview_Objectives_and_Themes"},
        {"index": 2, "title": "Unit 2: Grammar Mastery & Verb Tenses", "start": 8, "end": 19, "slug": "02_Unit_2_Grammar_and_Verb_Tenses"},
        {"index": 3, "title": "Unit 3: Thematic Vocabulary Modules", "start": 20, "end": 29, "slug": "03_Unit_3_Thematic_Vocabulary_Modules"},
        {"index": 4, "title": "Unit 4: Speaking Goals & Checklists", "start": 30, "end": 42, "slug": "04_Unit_4_Speaking_Goals_and_Checklists"},
        {"index": 5, "title": "Unit 5: Writing Goals & Checklists", "start": 43, "end": 52, "slug": "05_Unit_5_Writing_Goals_and_Checklists"},
        {"index": 6, "title": "Unit 6: Structured Learning Resources (Books, Podcasts, Channels & Apps)", "start": 53, "end": 66, "slug": "06_Unit_6_Structured_Learning_Resources"},
        {"index": 7, "title": "Unit 7: Listening & Immersion Mastery Checklist", "start": 67, "end": 67, "slug": "07_Unit_7_Listening_and_Immersion_Milestones"},
        {"index": 8, "title": f"Unit 8: Final Self-Evaluation & {next_level} Readiness", "start": 68, "end": 71, "slug": "08_Unit_8_Final_Self_Evaluation_and_Readiness"},
    ]

LEVELS = [
    ("A1", "French_A1", "A2"),
    ("A2", "French_A2", "B1"),
    ("B1", "French_B1", "B2"),
    ("B2", "French_B2", "C1"),
    ("C1", "French_C1", "C2"),
    ("C2", "French_C2", "Mastery"),
]

def sanitize_filename(name: str) -> str:
    cleaned = re.sub(r'[\/:*?"<>|«»]', '', name)
    cleaned = cleaned.replace(" ", "_").replace("–", "-").replace("—", "-")
    return re.sub(r'_+', '_', cleaned).strip("_")

def process_level(level_code: str, folder_name: str, next_level: str):
    print(f"\n{'='*50}\nProcessing Level French {level_code}...\n{'='*50}")
    src_pdf = BASE_DIR / folder_name / f"French_Learning_Roadmap_Checklist_{folder_name}.pdf"
    output_master_pdf = OUTPUT_DIR / f"French_Learning_Roadmap_Checklist_{folder_name}.pdf"
    
    # Copy to master output dir
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src_pdf, output_master_pdf)
    
    # Destinations in Desktop
    level_split_dir = TARGET_SPLIT_ROOT / f"French_{level_code}_Roadmap_Split"
    modules_dir = level_split_dir / "01_By_Curriculum_Modules"
    pages_dir = level_split_dir / "02_By_Individual_Pages"
    modules_dir.mkdir(parents=True, exist_ok=True)
    pages_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy master PDF into level split dir
    shutil.copy2(src_pdf, level_split_dir / f"Master_French_{level_code}_Roadmap_71_Pages.pdf")
    
    reader = pypdf.PdfReader(str(src_pdf))
    assert len(reader.pages) == 71, f"Expected 71 pages, got {len(reader.pages)}"
    
    # 1. Split by 8 units
    units = get_level_units(level_code, next_level)
    print(f"Extracting 8 modular unit slices to 01_By_Curriculum_Modules...")
    for u in units:
        start_idx = u["start"] - 1
        end_idx = u["end"]
        writer = pypdf.PdfWriter()
        writer.append(reader, pages=(start_idx, end_idx))
        out_unit_path = modules_dir / f"{u['slug']}.pdf"
        with open(out_unit_path, "wb") as f_out:
            writer.write(f_out)
            
    # 2. Split by 71 individual pages
    print(f"Extracting 71 single-page worksheets to 02_By_Individual_Pages...")
    for p_num in range(1, 72):
        writer = pypdf.PdfWriter()
        writer.append(reader, pages=(p_num - 1, p_num))
        title = get_page_title(level_code, p_num)
        clean_title = sanitize_filename(title)[:45]
        page_pdf_name = f"Page_{p_num:02d}_{clean_title}.pdf"
        out_page_path = pages_dir / page_pdf_name
        with open(out_page_path, "wb") as f_out:
            writer.write(f_out)
            
    # Top-level symlink
    symlink_path = DESKTOP_DIR / f"French_{level_code}_Roadmap_Split"
    if symlink_path.is_symlink() or symlink_path.exists():
        symlink_path.unlink()
    symlink_path.symlink_to(level_split_dir)
    print(f"Created convenience symlink: {symlink_path} -> {level_split_dir}")

def main():
    TARGET_SPLIT_ROOT.mkdir(parents=True, exist_ok=True)
    for code, folder, nxt in LEVELS:
        process_level(code, folder, nxt)
        
    complete_dir = TARGET_SPLIT_ROOT / "Complete_Roadmaps_A1_to_C2"
    complete_dir.mkdir(parents=True, exist_ok=True)
    for code, folder, _ in LEVELS:
        src = OUTPUT_DIR / f"French_Learning_Roadmap_Checklist_{folder}.pdf"
        shutil.copy2(src, complete_dir / f"French_{code}_Complete_Roadmap_71_Pages.pdf")
        
    print(f"\n{'='*50}\nAll 6 Roadmaps (A1–C2) successfully split and delivered!\n{'='*50}")

if __name__ == "__main__":
    main()
