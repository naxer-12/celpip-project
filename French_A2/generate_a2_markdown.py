#!/usr/bin/env python3
"""
generate_a2_markdown.py - Markdown Generator for French A2 Learning Roadmap & Checklist

Serializes CEFR A2 curriculum data from a2_curriculum_data.py into a complete,
fully-structured reference document and interactive checklist companion
(French_A2_Learning_Roadmap_Checklist.md) featuring all 71 pages, checkable lists,
thematic & vocabulary markdown tables, and CEFR audit benchmarks.
"""

import os
from a2_curriculum_data import A2_PAGES_DATA

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT_PATH = os.path.join(BASE_DIR, "French_A2_Learning_Roadmap_Checklist.md")


def format_cell(text: str) -> str:
    """Format table cell text for GFM table compliance."""
    return text.replace("|", r"\|").replace("\r\n", "<br>").replace("\n", "<br>").strip()


def format_table(table_data: dict) -> str:
    """Format dictionary with 'headers' and 'rows' into a standard Markdown table."""
    headers = table_data.get("headers", [])
    rows = table_data.get("rows", [])
    if not headers or not rows:
        return ""

    table_lines = [
        "| " + " | ".join(format_cell(h) for h in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        table_lines.append("| " + " | ".join(format_cell(str(c)) for c in row) + " |")
    return "\n".join(table_lines)


def generate_markdown(output_path: str = DEFAULT_OUTPUT_PATH) -> str:
    """Generate French_A2_Learning_Roadmap_Checklist.md from A2_PAGES_DATA."""
    lines = [
        "# French Learning Roadmap & Checklist (French A2)",
        "",
        "> **CEFR Level**: A2 (Waystage / Elementary)",
        "> **Source**: Synthesized Pedagogical Curriculum & CEFR A2 Competence Framework",
        "> **Total Pages**: 71",
        "> **Companion Document**: Interactive checklist and reference guide for complete French A2 mastery",
        "",
        "---",
        "",
    ]

    for p_num in range(1, 72):
        data = A2_PAGES_DATA[p_num]
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
            items = data.get("items", [])
            if items:
                lines.append("#### Target Competencies & Milestones")
                lines.append("")
                for item in items:
                    lines.append(f"- [ ] {item}")
                lines.append("")
            sections = data.get("sections", [])
            for sec in sections:
                lines.append(f"#### {sec['title']}")
                lines.append("")
                for item in sec.get("items", []):
                    lines.append(f"- [ ] {item}")
                lines.append("")

        elif p_type in ("themes_table", "functions_table", "vocab_table"):
            items = data.get("items", [])
            if items:
                if p_num == 4:
                    header_name = "Real-Life Communicative Outcomes"
                elif p_type == "functions_table":
                    header_name = "Core Communicative Functions Summary"
                elif p_type == "vocab_table":
                    header_name = "High-Frequency Vocabulary Checklist"
                else:
                    header_name = "Key Outcomes & Competencies"
                lines.append(f"#### {header_name}")
                lines.append("")
                for item in items:
                    lines.append(f"- [ ] {item}")
                lines.append("")

            table = data.get("table")
            if table:
                lines.append("#### Thematic Reference Table")
                lines.append("")
                lines.append(format_table(table))
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
                lines.append("> ### 🎉 CEFR B1 Transition Benchmark")
                lines.append("> If you have mastered and checked off at least 85–90% of the criteria across this roadmap:")
                lines.append("> **You are fully prepared to advance to French B1 (Intermediate)! Félicitations pour votre parcours !**")
                lines.append("")

        else:  # checklist & objectives
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
