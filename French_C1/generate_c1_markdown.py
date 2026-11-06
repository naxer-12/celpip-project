#!/usr/bin/env python3
"""
generate_c1_markdown.py - Markdown Generator for French C1 Learning Roadmap & Checklist
"""

import os
from c1_curriculum_data import C1_PAGES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT_PATH = os.path.join(BASE_DIR, "French_C1_Learning_Roadmap_Checklist.md")


def format_cell(text: str) -> str:
    """Format table cell text for GFM table compliance."""
    return text.replace("|", r"\|").replace("\r\n", "<br>").replace("\n", "<br>").strip()


def generate_markdown(output_path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Generate French_C1_Learning_Roadmap_Checklist.md from C1_PAGES_DATA."""
    lines = [
        "# French Learning Roadmap & Checklist (French C1)",
        "",
        "> **CEFR Level**: C1 (Autonomous User / Effective Operational Proficiency)",
        "> **Source**: Synthesized Pedagogical Curriculum & CEFR C1 Competence Framework",
        "> **Total Pages**: 71",
        "> **Companion Document**: Interactive checklist and reference guide for complete French C1 mastery and DALF C1 preparation",
        "",
        "---",
        "",
    ]

    for p_num in range(1, 72):
        data = C1_PAGES_DATA[p_num]
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
            lines.append("- [ ] Full autonomous operational proficiency in academic, professional, and cultural contexts.")
            lines.append("- [ ] Mastery of DALF C1 document synthesis and 250+ word structured argumentation.")
            lines.append("- [ ] Command of 6,000–8,000 active French words spanning high-level intellectual domains.")
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
                lines.append("> ### 🎉 CEFR C2 Transition Benchmark")
                lines.append("> If you have mastered and checked off at least 85–90% of the criteria across this roadmap:")
                lines.append("> **You are fully prepared to advance to French C2 (Mastery / Maîtrise)! Félicitations pour votre parcours d'excellence !**")
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
