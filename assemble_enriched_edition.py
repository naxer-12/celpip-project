#!/usr/bin/env python3
"""assemble_enriched_edition.py

Losslessly interleaves the original 83-page A1 French textbook with the 33 newly generated
companion pages to produce the complete 116-page master edition:
- Pages 001-004: Front matter (Cover, Welcome, TOC, Pronunciation Super-Guide)
- Pages 005-103: 33 Units x 3 pages (Page 1: Vocab, Page 2: Quiz, Page 3: Immersion Companion)
- Pages 104-116: Back matter (Grammar Engine, Master Glossary, Certificate)

Output target:
/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf
"""

import os
import sys
import pypdf

DEFAULT_ORIGINAL_PDF = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf"
DEFAULT_COMPANION_PDF = "/Users/jainamshah/Downloads/Learning French/companion_pages.pdf"
DEFAULT_OUTPUT_PDF = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf"


def assemble_enriched_edition(
    original_pdf_path: str = DEFAULT_ORIGINAL_PDF,
    companion_pdf_path: str = DEFAULT_COMPANION_PDF,
    output_pdf_path: str = DEFAULT_OUTPUT_PDF,
) -> str:
    """Interleaves original textbook pages with companion pages to produce the enriched edition."""
    if not os.path.exists(original_pdf_path):
        raise FileNotFoundError(f"Original PDF not found: {original_pdf_path}")
    if not os.path.exists(companion_pdf_path):
        raise FileNotFoundError(f"Companion PDF not found: {companion_pdf_path}")

    print(f"Reading original PDF: {original_pdf_path}")
    orig_reader = pypdf.PdfReader(original_pdf_path)
    total_orig = len(orig_reader.pages)
    if total_orig != 83:
        raise ValueError(f"Expected 83 pages in original PDF, found {total_orig}")

    print(f"Reading companion PDF: {companion_pdf_path}")
    comp_reader = pypdf.PdfReader(companion_pdf_path)
    total_comp = len(comp_reader.pages)
    if total_comp != 33:
        raise ValueError(f"Expected 33 pages in companion PDF, found {total_comp}")

    writer = pypdf.PdfWriter()

    # Step 1: Front Matter (Pages 1-4, indices 0-3)
    print("Appending Front Matter (pages 1-4)...")
    for idx in range(4):
        writer.add_page(orig_reader.pages[idx])

    # Step 2: Interleaved Units 1 to 33 (3 pages per unit)
    # Unit k:
    #   Original Page 1 -> orig index: (2*k + 3) - 1 = 2*k + 2
    #   Original Page 2 -> orig index: (2*k + 4) - 1 = 2*k + 3
    #   Companion Page  -> comp index: k - 1
    # Resulting in Enriched Pages:
    #   3*k + 2 (Unit Page 1)
    #   3*k + 3 (Unit Page 2 / Quiz)
    #   3*k + 4 (Unit Page 3 / Companion Immersion)
    print("Interleaving 33 units (pages 5-103)...")
    for k in range(1, 34):
        orig_p1_idx = 2 * k + 2
        orig_p2_idx = 2 * k + 3
        comp_idx = k - 1

        writer.add_page(orig_reader.pages[orig_p1_idx])
        writer.add_page(orig_reader.pages[orig_p2_idx])
        writer.add_page(comp_reader.pages[comp_idx])

    # Step 3: Back Matter (Pages 71-83 from original, indices 70-82)
    # Appended to Enriched Pages 104-116
    print("Appending Back Matter (pages 104-116)...")
    for idx in range(70, 83):
        writer.add_page(orig_reader.pages[idx])

    total_pages = len(writer.pages)
    if total_pages != 116:
        raise ValueError(f"Expected 116 total pages, assembled {total_pages}")

    # Step 4: Metadata
    if orig_reader.metadata:
        metadata = dict(orig_reader.metadata)
        metadata["/Title"] = "Vocabulaire Essentiel du Français A1 - Édition Enrichie (33 Chapitres)"
        metadata["/Subject"] = "Vocabulaire A1 avec Fiches d'Immersion et Consolidation Active"
        writer.add_metadata(metadata)

    # Step 5: Write out
    out_dir = os.path.dirname(output_pdf_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    print(f"Writing 116-page enriched edition to: {output_pdf_path}")
    with open(output_pdf_path, "wb") as f_out:
        writer.write(f_out)

    out_size_mb = os.path.getsize(output_pdf_path) / (1024 * 1024)
    print(f"Successfully assembled {total_pages} pages ({out_size_mb:.2f} MB)")
    return output_pdf_path


if __name__ == "__main__":
    orig_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ORIGINAL_PDF
    comp_path = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_COMPANION_PDF
    out_path = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_OUTPUT_PDF

    assemble_enriched_edition(orig_path, comp_path, out_path)
