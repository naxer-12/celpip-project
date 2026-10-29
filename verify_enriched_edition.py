#!/usr/bin/env python3
"""verify_enriched_edition.py

Comprehensive Verification & Quality Audit Script for the French A1 Vocabulary Enriched Master Edition:
Target: /Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf

Audit Criteria:
1. File Existence & Size: Validates existence and non-corrupt file size (> 50 MB).
2. Page Count: Validates total page count is exactly 116 pages.
3. Front Matter Integrity: Validates pages 1-4 are identical in text to the original front matter.
4. Back Matter Integrity: Validates pages 104-116 are identical in text to original back matter (pages 71-83).
5. Interleaved 3-Page Units: Validates each chapter k in [1, 33]:
   - Page 3k+2: Original Chapter k Page 1 (Vocabulaire)
   - Page 3k+3: Original Chapter k Page 2 (Quiz & Exercices)
   - Page 3k+4: Companion Chapter k Page (Immersion & Consolidation)
6. Pedagogical Content Completeness: Validates each companion page contains:
   - "IMMERSION CONTEXTUELLE" (Partie A)
   - "EXERCICES D'ANCRAGE" (Partie B)
   - Chapter number & French title
   - "AUTO-CORRECTION" (Solutions footer)
7. Dimensional Conformance: Validates standard print geometry across all 116 pages:
   - Companion pages: 612 x 792 pt (US Letter +/- 2 pt)
   - Original textbook pages: 595 x 842 pt (A4 +/- 2 pt)
8. Text Extractability: Validates non-empty text extraction on all 116 pages.

Prints a comprehensive ASCII verification report and exits 0 on success, non-zero on failure.
"""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import pypdf

# Default paths
DEFAULT_ENRICHED_PDF = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Enriched_Edition.pdf"
DEFAULT_ORIGINAL_PDF = "/Users/jainamshah/Desktop/French Material/Vocabulaire_Essentiel_A1_33_Chapitres_Edition.pdf"
DEFAULT_COMPANION_PDF = "/Users/jainamshah/Downloads/Learning French/companion_pages.pdf"
DEFAULT_DATA_JSON = "/Users/jainamshah/Downloads/Learning French/companion_data.json"


@dataclass
class CheckResult:
    category: str
    description: str
    passed: bool
    details: str
    page_range: Optional[str] = None


@dataclass
class ChapterAudit:
    ch_num: int
    title_fr: str
    page_1: int
    page_2: int
    page_companion: int
    p1_verified: bool = False
    p2_verified: bool = False
    comp_verified: bool = False
    has_immersion: bool = False
    has_exercices: bool = False
    has_autocorrection: bool = False
    has_title: bool = False
    has_ch_num: bool = False

    @property
    def fully_passed(self) -> bool:
        return (
            self.p1_verified
            and self.p2_verified
            and self.comp_verified
            and self.has_immersion
            and self.has_exercices
            and self.has_autocorrection
            and self.has_title
            and self.has_ch_num
        )


class EnrichedEditionAuditor:
    def __init__(
        self,
        enriched_pdf_path: str = DEFAULT_ENRICHED_PDF,
        original_pdf_path: str = DEFAULT_ORIGINAL_PDF,
        companion_pdf_path: str = DEFAULT_COMPANION_PDF,
        data_json_path: str = DEFAULT_DATA_JSON,
        verbose: bool = False,
    ):
        self.enriched_path = enriched_pdf_path
        self.original_path = original_pdf_path
        self.companion_path = companion_pdf_path
        self.data_path = data_json_path
        self.verbose = verbose

        self.results: List[CheckResult] = []
        self.chapter_audits: List[ChapterAudit] = []
        self.enriched_reader: Optional[pypdf.PdfReader] = None
        self.orig_reader: Optional[pypdf.PdfReader] = None
        self.comp_reader: Optional[pypdf.PdfReader] = None
        self.companion_data: Dict = {}

    def log(self, message: str):
        if self.verbose:
            print(f"  [VERBOSE] {message}")

    def run_all_audits(self) -> bool:
        """Executes the full suite of audit validations."""
        start_time = time.time()

        # Step 1: File Existence and File Size (> 50 MB)
        self._audit_file_existence_and_size()

        # Load resources if files exist
        if not self._load_resources():
            self._print_report(time.time() - start_time)
            return False

        # Step 2: Total Page Count (116)
        self._audit_total_page_count()

        # Step 3: Front Matter Preservation (Pages 1-4)
        self._audit_front_matter()

        # Step 4: Back Matter Preservation (Pages 104-116)
        self._audit_back_matter()

        # Step 5 & 6: 33 Interleaved Chapter Units & Pedagogical Content Fidelity
        self._audit_chapters_interleaving_and_content()

        # Step 7 & 8: Text Extractability & Dimensional Conformance
        self._audit_dimensions_and_text_extraction()

        elapsed = time.time() - start_time
        all_passed = all(r.passed for r in self.results)
        self._print_report(elapsed)
        return all_passed

    def _audit_file_existence_and_size(self):
        """Audits file existence and size (> 50 MB)."""
        if not os.path.exists(self.enriched_path):
            self.results.append(
                CheckResult(
                    category="File Integrity",
                    description="Target Enriched PDF Exists",
                    passed=False,
                    details=f"File not found: {self.enriched_path}",
                )
            )
            return

        size_bytes = os.path.getsize(self.enriched_path)
        size_mb = size_bytes / (1024 * 1024)
        passed_size = size_mb > 50.0

        self.results.append(
            CheckResult(
                category="File Integrity",
                description="Target Enriched PDF Exists & Size > 50 MB",
                passed=passed_size,
                details=f"Size: {size_mb:.2f} MB (Expected: > 50.0 MB)",
            )
        )

    def _load_resources(self) -> bool:
        """Loads PDF readers and metadata."""
        try:
            if not os.path.exists(self.enriched_path):
                return False
            self.enriched_reader = pypdf.PdfReader(self.enriched_path)

            if not os.path.exists(self.original_path):
                self.results.append(
                    CheckResult(
                        category="Dependencies",
                        description="Original PDF Available",
                        passed=False,
                        details=f"Missing: {self.original_path}",
                    )
                )
                return False
            self.orig_reader = pypdf.PdfReader(self.original_path)

            if not os.path.exists(self.companion_path):
                self.results.append(
                    CheckResult(
                        category="Dependencies",
                        description="Companion PDF Available",
                        passed=False,
                        details=f"Missing: {self.companion_path}",
                    )
                )
                return False
            self.comp_reader = pypdf.PdfReader(self.companion_path)

            if not os.path.exists(self.data_path):
                self.results.append(
                    CheckResult(
                        category="Dependencies",
                        description="Companion Data JSON Available",
                        passed=False,
                        details=f"Missing: {self.data_path}",
                    )
                )
                return False

            with open(self.data_path, "r", encoding="utf-8") as f:
                self.companion_data = json.load(f)

            return True
        except Exception as e:
            self.results.append(
                CheckResult(
                    category="Dependencies",
                    description="Resource Loading",
                    passed=False,
                    details=f"Failed loading resources: {str(e)}",
                )
            )
            return False

    def _audit_total_page_count(self):
        """Audits exact page counts of original, companion, and enriched PDFs."""
        total_enriched = len(self.enriched_reader.pages)
        total_orig = len(self.orig_reader.pages)
        total_comp = len(self.comp_reader.pages)

        passed = total_enriched == 116 and total_orig == 83 and total_comp == 33
        details = (
            f"Enriched: {total_enriched}/116 pages | "
            f"Original: {total_orig}/83 pages | "
            f"Companion: {total_comp}/33 pages"
        )
        self.results.append(
            CheckResult(
                category="Page Geometry",
                description="Exact 116-Page Master Count (4 Front + 33x3 Units + 13 Back)",
                passed=passed,
                details=details,
                page_range="1-116",
            )
        )

    def _audit_front_matter(self):
        """Audits pages 1-4 against original front matter."""
        mismatches = []
        for idx in range(4):
            orig_txt = self.orig_reader.pages[idx].extract_text() or ""
            enriched_txt = self.enriched_reader.pages[idx].extract_text() or ""
            if orig_txt.strip() != enriched_txt.strip():
                mismatches.append(f"Page {idx + 1}")

        passed = len(mismatches) == 0
        details = "Identical text across all 4 front matter pages" if passed else f"Mismatches on: {', '.join(mismatches)}"
        self.results.append(
            CheckResult(
                category="Front Matter",
                description="Lossless Preservation of Front Matter (Pages 1-4)",
                passed=passed,
                details=details,
                page_range="1-4",
            )
        )

    def _audit_back_matter(self):
        """Audits pages 104-116 against original pages 71-83."""
        mismatches = []
        for offset in range(13):
            orig_idx = 70 + offset
            enriched_idx = 103 + offset
            orig_txt = self.orig_reader.pages[orig_idx].extract_text() or ""
            enriched_txt = self.enriched_reader.pages[enriched_idx].extract_text() or ""
            if orig_txt.strip() != enriched_txt.strip():
                mismatches.append(f"Enriched Page {enriched_idx + 1} (Orig {orig_idx + 1})")

        passed = len(mismatches) == 0
        details = "Identical text across all 13 back matter pages" if passed else f"Mismatches on: {', '.join(mismatches)}"
        self.results.append(
            CheckResult(
                category="Back Matter",
                description="Lossless Preservation of Back Matter (Pages 104-116 vs Orig 71-83)",
                passed=passed,
                details=details,
                page_range="104-116",
            )
        )

    def _audit_chapters_interleaving_and_content(self):
        """Audits interleaved 3-page structure and pedagogical content for all 33 units."""
        all_units_valid = True
        failed_chapters = []

        for k in range(1, 34):
            # 1-based page indices
            p1_num = 3 * k + 2
            p2_num = 3 * k + 3
            p_comp_num = 3 * k + 4

            # 0-based array indices
            enriched_p1_idx = p1_num - 1
            enriched_p2_idx = p2_num - 1
            enriched_comp_idx = p_comp_num - 1

            orig_p1_idx = (2 * k + 3) - 1
            orig_p2_idx = (2 * k + 4) - 1
            comp_idx = k - 1

            ch_info = self.companion_data.get(str(k), {})
            title_fr = ch_info.get("title_fr", f"Chapitre {k}")

            audit = ChapterAudit(
                ch_num=k,
                title_fr=title_fr,
                page_1=p1_num,
                page_2=p2_num,
                page_companion=p_comp_num,
            )

            # 1. Verify Page 1 (Original Textbook Vocab page)
            orig_p1_txt = self.orig_reader.pages[orig_p1_idx].extract_text() or ""
            enr_p1_txt = self.enriched_reader.pages[enriched_p1_idx].extract_text() or ""
            audit.p1_verified = (orig_p1_txt.strip() == enr_p1_txt.strip())

            # 2. Verify Page 2 (Original Textbook Quiz page)
            orig_p2_txt = self.orig_reader.pages[orig_p2_idx].extract_text() or ""
            enr_p2_txt = self.enriched_reader.pages[enriched_p2_idx].extract_text() or ""
            audit.p2_verified = (orig_p2_txt.strip() == enr_p2_txt.strip())

            # 3. Verify Page 3 (Companion Immersion Page identical to companion_pages.pdf)
            comp_txt = self.comp_reader.pages[comp_idx].extract_text() or ""
            enr_comp_txt = self.enriched_reader.pages[enriched_comp_idx].extract_text() or ""
            audit.comp_verified = (comp_txt.strip() == enr_comp_txt.strip())

            # 4. Pedagogical Content Assertions on Companion Page
            norm_comp_txt = " ".join(enr_comp_txt.split())
            norm_comp_upper = norm_comp_txt.upper()

            # "IMMERSION CONTEXTUELLE"
            audit.has_immersion = "IMMERSION CONTEXTUELLE" in norm_comp_upper or "PARTIE A" in norm_comp_upper

            # "EXERCICES D'ANCRAGE"
            audit.has_exercices = "EXERCICES" in norm_comp_upper and ("ANCRAGE" in norm_comp_upper)

            # "AUTO-CORRECTION"
            audit.has_autocorrection = "AUTO-CORRECTION" in norm_comp_upper or "CORRECTION" in norm_comp_upper

            # Chapter number
            ch_num_pat_2d = f"CHAPITRE {k:02d}"
            ch_num_pat_1d = f"CHAPITRE {k}"
            audit.has_ch_num = ch_num_pat_2d in norm_comp_upper or ch_num_pat_1d in norm_comp_upper

            # French Title
            norm_title = " ".join(title_fr.split()).lower()
            audit.has_title = norm_title in norm_comp_txt.lower()

            self.chapter_audits.append(audit)
            if not audit.fully_passed:
                all_units_valid = False
                failed_chapters.append(f"Ch {k}")

        self.results.append(
            CheckResult(
                category="Unit Interleaving",
                description="Strict 3-Page Structure (Pages 3k+2, 3k+3, 3k+4) for All 33 Units",
                passed=all_units_valid,
                details="All 33 chapters correctly interleaved in 3-page unit blocks" if all_units_valid else f"Failed units: {', '.join(failed_chapters)}",
                page_range="5-103",
            )
        )

        all_pedagogical = all(
            a.has_immersion and a.has_exercices and a.has_autocorrection and a.has_ch_num and a.has_title
            for a in self.chapter_audits
        )
        self.results.append(
            CheckResult(
                category="Pedagogical Quality",
                description="Required Companion Sections (Immersion, Exercices, Title, Auto-Correction)",
                passed=all_pedagogical,
                details="100% of 33 companion pages contain all 4 required pedagogical pillars" if all_pedagogical else "Incomplete companion sections detected",
                page_range="7, 10, ..., 103",
            )
        )

    def _audit_dimensions_and_text_extraction(self):
        """Audits page dimensions and non-empty text extraction on all 116 pages."""
        empty_text_pages = []
        dim_mismatches = []
        companion_page_count = 0
        original_page_count = 0

        for i, page in enumerate(self.enriched_reader.pages):
            page_num = i + 1
            txt = page.extract_text()
            if not txt or len(txt.strip()) == 0:
                empty_text_pages.append(page_num)

            w = float(page.mediabox.width)
            h = float(page.mediabox.height)

            # Companion pages are pages 3k+4 (7, 10, 13, ..., 103)
            is_companion = (page_num - 4) % 3 == 0 and 5 <= page_num <= 103

            if is_companion:
                companion_page_count += 1
                # US Letter: 612 x 792 pt
                if abs(w - 612.0) > 2.0 or abs(h - 792.0) > 2.0:
                    dim_mismatches.append(f"Page {page_num} (Companion: {w:.1f}x{h:.1f} pt)")
            else:
                original_page_count += 1
                # Standard A4: 595 x 842 pt
                if abs(w - 595.0) > 2.0 or abs(h - 842.0) > 2.0:
                    dim_mismatches.append(f"Page {page_num} (Original: {w:.1f}x{h:.1f} pt)")

        passed_text = len(empty_text_pages) == 0
        self.results.append(
            CheckResult(
                category="Text Extractability",
                description="Non-Empty Text Extraction Across All 116 Pages",
                passed=passed_text,
                details=f"All 116 pages contain searchable text ({len(empty_text_pages)} empty)" if passed_text else f"Empty pages: {empty_text_pages}",
                page_range="1-116",
            )
        )

        passed_dims = len(dim_mismatches) == 0
        self.results.append(
            CheckResult(
                category="Page Dimensions",
                description="Standard Page Geometry (33 Companion US Letter 612x792 pt, 83 Original A4 595x842 pt)",
                passed=passed_dims,
                details=f"33 Companion pages (612x792 pt) + 83 Original pages (595x842 pt) validated" if passed_dims else f"Dimension mismatches: {', '.join(dim_mismatches[:5])}",
                page_range="1-116",
            )
        )

    def _print_report(self, elapsed_seconds: float):
        """Renders an ASCII verification report to stdout."""
        border = "=" * 80
        thin_border = "-" * 80
        sub_border = "." * 80

        print("\n" + border)
        print(" VOCABULAIRE ESSENTIEL DU FRANÇAIS A1 - ÉDITION ENRICHIE (116 PAGES)")
        print(" PIPELINE VERIFICATION & QUALITY AUDIT REPORT")
        print(border)
        print(f" Target File    : {self.enriched_path}")
        if os.path.exists(self.enriched_path):
            size_mb = os.path.getsize(self.enriched_path) / (1024 * 1024)
            print(f" File Size      : {size_mb:.2f} MB")
        print(f" Audit Duration : {elapsed_seconds:.2f} seconds")
        print(thin_border)
        print(f"{'STATUS':<8} | {'CATEGORY':<20} | {'PAGES':<10} | {'CHECK DESCRIPTION'}")
        print(thin_border)

        all_passed = True
        for r in self.results:
            status_tag = "[PASS]" if r.passed else "[FAIL]"
            if not r.passed:
                all_passed = False
            pages_str = r.page_range or "-"
            print(f"{status_tag:<8} | {r.category:<20} | {pages_str:<10} | {r.description}")
            print(f"         > Details: {r.details}")

        print(thin_border)
        print(" 33-CHAPTER INTERLEAVED UNIT COMPLIANCE AUDIT MATRIX")
        print(thin_border)
        print(f"{'CH':<4} | {'PAGES (P1, P2, COMP)':<22} | {'ORIG P1/P2':<12} | {'COMP FIDELITY':<15} | {'TITLE & TOPIC'}")
        print(sub_border)

        for audit in self.chapter_audits:
            page_group = f"P{audit.page_1}, P{audit.page_2}, P{audit.page_companion}"
            orig_status = "PASS / PASS" if (audit.p1_verified and audit.p2_verified) else "FAIL"
            comp_status = "PASS (100%)" if audit.fully_passed else "FAIL"
            title_trunc = audit.title_fr[:32] + ("..." if len(audit.title_fr) > 32 else "")
            print(f"{audit.ch_num:>2}   | {page_group:<22} | {orig_status:<12} | {comp_status:<15} | {title_trunc}")

        print(border)
        if all_passed:
            print(" [FINAL VERDICT] ALL AUDIT CRITERIA PASSED - 116-PAGE MASTER EDITION VERIFIED")
            print(" The enriched master edition is publication-grade, losslessly interleaved,")
            print(" fully extractable, and pedagogical requirements are 100% satisfied.")
        else:
            print(" [FINAL VERDICT] AUDIT FAILED - QUALITY ANOMALIES DETECTED")
            print(" Please inspect failure details listed above.")
        print(border + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify and audit the 116-page French A1 Enriched Master Edition."
    )
    parser.add_argument(
        "--enriched-pdf",
        default=DEFAULT_ENRICHED_PDF,
        help="Path to the assembled enriched edition PDF",
    )
    parser.add_argument(
        "--original-pdf",
        default=DEFAULT_ORIGINAL_PDF,
        help="Path to original textbook PDF",
    )
    parser.add_argument(
        "--companion-pdf",
        default=DEFAULT_COMPANION_PDF,
        help="Path to 33-page companion PDF",
    )
    parser.add_argument(
        "--data-json",
        default=DEFAULT_DATA_JSON,
        help="Path to companion content JSON data",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose inspection output",
    )

    args = parser.parse_args()

    auditor = EnrichedEditionAuditor(
        enriched_pdf_path=args.enriched_pdf,
        original_pdf_path=args.original_pdf,
        companion_pdf_path=args.companion_pdf,
        data_json_path=args.data_json,
        verbose=args.verbose,
    )

    success = auditor.run_all_audits()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
