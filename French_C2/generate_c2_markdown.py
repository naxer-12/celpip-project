#!/usr/bin/env python3
"""
generate_c2_markdown.py - Markdown Generator for French C2 Learning Roadmap & Checklist
"""

import os
from c2_curriculum_data import C2_PAGES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT_PATH = os.path.join(BASE_DIR, "French_C2_Learning_Roadmap_Checklist.md")


def format_cell(text: str) -> str:
    """Format table cell text for GFM table compliance."""
    return text.replace("|", r"\|").replace("\r\n", "<br>").replace("\n", "<br>").strip()


def generate_markdown(output_path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Generate French_C2_Learning_Roadmap_Checklist.md from C2_PAGES_DATA."""
    lines = [
        "# French Learning Roadmap & Checklist (French C2)",
        "",
        "> **CEFR Level**: C2 (Mastery / Bilingual Virtuosity)",
        "> **Source**: Synthesized Pedagogical Curriculum & CEFR C2 Competence Framework",
        "> **Total Pages**: 71",
        "> **Companion Document**: Interactive checklist and reference guide for complete French C2 mastery and DALF C2 preparation",
        "",
        "---",
        "",
    ]

    for p_num in range(1, 72):
        data = C2_PAGES_DATA[p_num]
        lines.append(f"## Page {p_num}")
        lines.append("")
        lines.append(f"### {data['title']}")
        lines.append("")

        subtitle = data.get("subtitle")
        if subtitle:
            lines.append(f"*{subtitle}*")
            lines.append("")

        intro = data.get("intro")
        if intro:
            lines.append(intro)
            lines.append("")

        p_type = data.get("type", "checklist")

        if p_type == "cover":
            lines.append("#### Target Competencies & Milestones")
            lines.append("")
            lines.append("- [ ] Full bilingual mastery (Maîtrise) of the French language across all academic, literary, and cultural realms.")
            lines.append("- [ ] Mastery of DALF C2 integrated dossier synthesis (700+ words) and spontaneous 15-minute oratorical defense.")
            lines.append("- [ ] Command of 10,000+ active French words spanning high intellectual, classical, and idiomatic domains.")
            lines.append("")

        elif p_type in ("outcomes", "functions"):
            headers = data.get("table_headers", [])
            rows = data.get("table_rows", [])
            if headers and rows:
                lines.append("#### Reference Table")
                lines.append("")
                lines.append("| " + " | ".join(format_cell(h) for h in headers) + " |")
                lines.append("| " + " | ".join("---" for _ in headers) + " |")
                for r in rows:
                    lines.append("| " + " | ".join(format_cell(str(c)) for c in r) + " |")
                lines.append("")

            footer_title = data.get("footer_title")
            footer_items = data.get("footer_items", [])
            if footer_items:
                lines.append(f"#### {footer_title}")
                lines.append("")
                for item in footer_items:
                    lines.append(f"- [ ] {item}")
                lines.append("")

        elif p_type == "resources":
            resources = data.get("resources", [])
            for res in resources:
                name = res.get("name", "")
                badge = res.get("badge", "")
                url = res.get("url", "")
                what = res.get("what", "")
                features = res.get("features", "")
                focus = res.get("focus", "")
                tips = res.get("tips", "")
                lines.append(f"### {name} `[{badge}]`")
                lines.append(f"- **Platform / URL**: `{url}`")
                lines.append(f"- **Content**: {what}")
                lines.append(f"- **Key Features**: {features}")
                lines.append(f"- **Focus**: {focus}")
                lines.append(f"- **Study Routine**: {tips}")
                lines.append(f"- [ ] Active study resource verified\n")
        elif p_type == "audit":
            sections = data.get("sections", [])
            for sec in sections:
                lines.append(f"#### {sec['title']}")
                lines.append("")
                for item in sec.get("items", []):
                    lines.append(f"- [ ] {item}")
                lines.append("")
            if p_num == 71:
                lines.append("> ### 👑 CEFR C2 Bilingual Mastery & Lifelong Francophonie")
                lines.append("> Félicitations ! You have attained the highest recognized level of language proficiency: CEFR C2.")
                lines.append("> **You possess full bilingual virtuosity, intellectual autonomy, and cultural immersion in the Francophone world!**")
                lines.append("")

        else:  # checklist, grammar, thematic_vocab, speaking, listening, reading, writing
            sections = data.get("sections", [])
            for sec in sections:
                lines.append(f"#### {sec['title']}")
                lines.append("")
                for item in sec.get("items", []):
                    lines.append(f"- [ ] {item}")
                lines.append("")

        if p_num < 71:
            lines.append("---")
            lines.append("")

    content = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated {output_path} ({len(lines)} lines)")
    return content


if __name__ == "__main__":
    generate_markdown()
