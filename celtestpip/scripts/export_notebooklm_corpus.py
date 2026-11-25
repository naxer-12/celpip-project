"""Export and curate all CELPIP practice content into clean Markdown files
organized into 4 category folders for Google NotebookLM ingestion.
"""

import glob
import json
import os
import re
import sqlite3
from typing import Any, Dict, List, Optional
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(BASE_DIR, "data", "celtestpip.db")
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
EXPORT_DIR = os.path.join(ROOT_DIR, "notebooklm_celpip_export")

SKILL_FOLDERS = {
    "listening": "01_Listening",
    "reading": "02_Reading",
    "writing": "03_Writing",
    "speaking": "04_Speaking",
}


def html_article_to_markdown(html_path: str) -> Optional[str]:
    """Extract main title and article/prose content from a pre-rendered HTML page."""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception:
        return None

    soup = BeautifulSoup(raw, "html.parser")
    for tag in soup(["script", "style", "nav", "footer", "noscript", "svg"]):
        tag.decompose()

    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(" ", strip=True) if title_el else os.path.basename(html_path)
    title = title.replace(" | CELTESTPIP", "").strip()

    article = soup.find("article") or soup.find("main")
    if not article:
        return None

    lines: List[str] = [f"## {title}", ""]
    seen_text = set()

    for el in article.find_all(["h2", "h3", "h4", "p", "li", "blockquote", "table"]):
        # Skip nested elements already captured by parent li/blockquote/table
        if el.name == "p" and el.find_parent(["li", "blockquote", "table"]):
            continue
        if el.name in ("h2", "h3", "h4"):
            txt = el.get_text(" ", strip=True)
            if txt and txt not in seen_text:
                seen_text.add(txt)
                level = "#" * (int(el.name[1]) + 1)
                lines.append(f"{level} {txt}\n")
        elif el.name == "blockquote":
            txt = el.get_text(" ", strip=True)
            if txt and txt not in seen_text:
                seen_text.add(txt)
                lines.append(f"> {txt}\n")
        elif el.name == "li":
            txt = el.get_text(" ", strip=True)
            if txt and txt not in seen_text:
                seen_text.add(txt)
                lines.append(f"- {txt}")
        elif el.name == "table":
            rows = []
            for tr in el.find_all("tr"):
                cells = [c.get_text(" ", strip=True).replace("|", "\\|") for c in tr.find_all(["th", "td"])]
                if cells:
                    rows.append("| " + " | ".join(cells) + " |")
            if rows:
                lines.append("")
                lines.append(rows[0])
                col_count = rows[0].count("|") - 1
                if col_count > 0:
                    lines.append("| " + " | ".join(["---"] * col_count) + " |")
                lines.extend(rows[1:])
                lines.append("")
        elif el.name == "p":
            txt = el.get_text(" ", strip=True)
            if txt and len(txt) > 2 and txt not in seen_text:
                seen_text.add(txt)
                lines.append(f"{txt}\n")

    body = "\n".join(lines).strip()
    if len(body) < 80:
        return None
    return body


def extract_words_markdown(html_path: str) -> Optional[str]:
    """Extract vocabulary words/definitions from a words_*.html page."""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception:
        return None

    # Try Flight JSON word objects first
    words_found = []
    for m in re.finditer(r'\\"word\\":\\"([^\\"]+)\\",\\"meaning\\":\\"([^\\"]*)\\"', raw):
        w = m.group(1)
        meaning = m.group(2).replace("\\n", " ")
        words_found.append((w, meaning))

    soup = BeautifulSoup(raw, "html.parser")
    title_el = soup.find("h1") or soup.find("title")
    title = title_el.get_text(" ", strip=True) if title_el else os.path.basename(html_path)
    title = title.replace(" | CELTESTPIP", "").strip()

    lines = [f"## {title}", ""]
    if words_found:
        seen = set()
        for w, meaning in words_found:
            if w not in seen:
                seen.add(w)
                lines.append(f"- **{w}**: {meaning}")
    else:
        art = html_article_to_markdown(html_path)
        if art:
            return art
        return None

    return "\n".join(lines)


def extract_flight_practice(html_path: str) -> Optional[Dict[str, Any]]:
    """Extract practice title and steps array from Next.js Flight payload."""
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            raw = f.read()
    except Exception:
        return None

    m_title = re.search(r"<title>(.*?)</title>", raw)
    title = m_title.group(1).replace(" | CELTESTPIP", "").strip() if m_title else os.path.basename(html_path)

    # Locate steps array in Flight script
    m_steps = re.search(r'\\"steps\\":\s*(\[.*?\])(?:,|\\})', raw)
    if not m_steps:
        # Fallback: extract main text
        art = html_article_to_markdown(html_path)
        return {"title": title, "fallback_md": art} if art else None

    # Use bracket matching for full steps array
    idx = raw.find(r'\"steps\":[')
    if idx == -1:
        idx = raw.find('"steps":[')
    if idx == -1:
        art = html_article_to_markdown(html_path)
        return {"title": title, "fallback_md": art} if art else None

    start = raw.find("[", idx)
    depth = 0
    end = -1
    in_str = False
    esc = False
    for i in range(start, len(raw)):
        ch = raw[i]
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == '"':
            in_str = not in_str
        elif not in_str:
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break

    if end == -1:
        return None

    arr_str = raw[start:end]
    try:
        # Unescape Flight string encoding
        if r'\"' in arr_str:
            arr_str = json.loads('"' + arr_str.replace('"', '\\"').replace('\\\\"', '\\"') + '"')
    except Exception:
        pass

    try:
        steps = json.loads(arr_str)
        return {"title": title, "steps": steps}
    except Exception:
        # Try simpler unescape
        try:
            cleaned = arr_str.replace(r'\"', '"').replace(r'\\n', '\n').replace(r'\\"', '"')
            steps = json.loads(cleaned)
            return {"title": title, "steps": steps}
        except Exception:
            art = html_article_to_markdown(html_path)
            return {"title": title, "fallback_md": art} if art else None


def format_practice_to_md(pdata: Dict[str, Any], idx_num: int) -> str:
    """Format an extracted practice dict into clean Markdown."""
    lines = [f"## Practice {idx_num}: {pdata['title']}", ""]
    if pdata.get("fallback_md"):
        lines.append(pdata["fallback_md"])
        return "\n".join(lines)

    for step in pdata.get("steps", []):
        if not isinstance(step, dict):
            continue
        stype = step.get("type")
        content = step.get("content")
        if isinstance(content, str):
            if stype in ("task", "reading", "audio"):
                lines.append(f"### {stype.title()}\n{content}\n")
            continue
        if not isinstance(content, dict):
            content = {}
        if stype == "task":
            desc = content.get("description") or content.get("instructions") or content.get("prompt") or ""
            if desc:
                lines.append(f"**Instructions:** {desc}\n")
        elif stype == "audio":
            transcript = content.get("transcript") or step.get("transcript") or ""
            if transcript:
                lines.append("### Audio Transcript")
                lines.append(f"{transcript}\n")
        elif stype == "reading":
            passage = content.get("passage") or content.get("text") or ""
            if passage:
                lines.append("### Reading Passage")
                lines.append(f"{passage}\n")
        elif stype == "question":
            q_num = step.get("questionNumber") or ""
            q_text = content.get("question") or ""
            lines.append(f"**Q{q_num}:** {q_text}")
            for opt_i in range(1, 9):
                opt_val = content.get(f"option{opt_i}")
                if opt_val:
                    lines.append(f"- {opt_i}. {opt_val}")
            ans = content.get("answer")
            exp = content.get("explanation")
            if ans:
                lines.append(f"- **Correct Answer:** Option {ans}")
            if exp:
                lines.append(f"- **Explanation:** {exp}")
            lines.append("")

    return "\n".join(lines)


def export_courses_and_guides(skill: str, out_dir: str) -> None:
    """Export all course lessons and learn guides for a given skill."""
    course_files = sorted(glob.glob(os.path.join(PAGES_DIR, f"courses_celpip-{skill}*.html")))
    learn_files = sorted(glob.glob(os.path.join(PAGES_DIR, f"learn_*{skill}*.html")))
    all_files = course_files + learn_files

    sections = [f"# CELPIP {skill.title()} — Strategy Courses & Study Guides\n"]
    for path in all_files:
        md = html_article_to_markdown(path)
        if md:
            sections.append(md)
            sections.append("\n---\n")

    out_path = os.path.join(out_dir, f"01_{skill.title()}_Courses_and_Guides.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sections))
    print(f"Wrote {out_path} ({len(all_files)} source files)")


def export_vocabulary(skill: str, out_dir: str) -> None:
    """Export vocabulary word lists for a skill."""
    word_files = sorted(glob.glob(os.path.join(PAGES_DIR, f"words_{skill}*.html")))
    sections = [f"# CELPIP {skill.title()} — High-Frequency Vocabulary\n"]
    for path in word_files:
        md = extract_words_markdown(path)
        if md:
            sections.append(md)
            sections.append("\n---\n")

    out_path = os.path.join(out_dir, f"02_{skill.title()}_Vocabulary.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sections))
    print(f"Wrote {out_path} ({len(word_files)} source files)")


def export_db_mock_exams(skill_upper: str, out_dir: str) -> None:
    """Export all mock exam parts and questions from SQLite for a given skill."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """
        SELECT ep.*, e.name as exam_title
        FROM exam_parts ep
        LEFT JOIN exams e ON ep.exam_id = e.id
        WHERE ep.skill = ?
        ORDER BY ep.exam_id, ep.part_number
        """,
        (skill_upper,),
    )
    parts = [dict(r) for r in cur.fetchall()]

    # Group into chunks of ~180 parts per file so each Markdown file stays well within NotebookLM limits
    chunk_size = 180
    for chunk_idx in range(0, max(1, len(parts)), chunk_size):
        chunk = parts[chunk_idx : chunk_idx + chunk_size]
        vol = (chunk_idx // chunk_size) + 1
        lines = [
            f"# CELPIP {skill_upper.title()} — Mock Exam Bank (Volume {vol})\n",
            f"Contains {len(chunk)} authentic exam parts with full passages/transcripts, questions, answer keys, and explanations.\n",
        ]
        for p in chunk:
            lines.append(f"## {p.get('exam_title') or p['exam_id']} — Part {p['part_number']}: {p.get('part_name') or ''}\n")
            if p.get("instructions"):
                lines.append(f"### Prompt / Passage / Instructions\n{p['instructions']}\n")
            if p.get("transcripts_json"):
                try:
                    transcripts = json.loads(p["transcripts_json"])
                    if transcripts:
                        lines.append("### Audio Transcript")
                        for t in transcripts:
                            if t:
                                lines.append(f"{t}\n")
                except Exception:
                    pass

            cur.execute(
                "SELECT * FROM questions WHERE part_id = ? ORDER BY question_number",
                (p["id"],),
            )
            qs = [dict(q) for q in cur.fetchall()]
            if qs:
                lines.append("### Questions & Answer Key")
                for q in qs:
                    q_txt = q.get("question_text") or "(Select the best option)"
                    lines.append(f"**Q{q['question_number']}:** {q_txt}")
                    try:
                        opts = json.loads(q.get("options_json") or "[]")
                        for oi, opt in enumerate(opts, start=1):
                            lines.append(f"- {oi}. {opt}")
                    except Exception:
                        pass
                    if q.get("correct_answer"):
                        lines.append(f"- **Correct Answer:** Option {q['correct_answer']}")
                    if q.get("explanation"):
                        lines.append(f"- **Explanation:** {q['explanation']}")
                    lines.append("")
            lines.append("---\n")

        out_path = os.path.join(out_dir, f"03_{skill_upper.title()}_Mock_Exams_Vol{vol}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Wrote {out_path} ({len(chunk)} parts)")

    conn.close()


def export_standalone_practices(skill: str, out_dir: str) -> None:
    """Export standalone practice_*.html files into balanced Markdown volumes."""
    files = sorted(glob.glob(os.path.join(PAGES_DIR, f"practices_{skill}_*.html")))
    if not files:
        return

    chunk_size = 150
    for chunk_idx in range(0, len(files), chunk_size):
        chunk = files[chunk_idx : chunk_idx + chunk_size]
        vol = (chunk_idx // chunk_size) + 1
        sections = [f"# CELPIP {skill.title()} — Standalone Practice Sets (Volume {vol})\n"]
        extracted = 0
        for i, path in enumerate(chunk, start=chunk_idx + 1):
            pdata = extract_flight_practice(path)
            if pdata:
                sections.append(format_practice_to_md(pdata, i))
                sections.append("\n---\n")
                extracted += 1

        if extracted > 0:
            out_path = os.path.join(out_dir, f"04_{skill.title()}_Practice_Sets_Vol{vol}.md")
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("\n".join(sections))
            print(f"Wrote {out_path} ({extracted} practices)")


def main() -> None:
    os.makedirs(EXPORT_DIR, exist_ok=True)
    for skill, folder_name in SKILL_FOLDERS.items():
        out_dir = os.path.join(EXPORT_DIR, folder_name)
        os.makedirs(out_dir, exist_ok=True)
        print(f"\n=== Curating {folder_name} ===")
        export_courses_and_guides(skill, out_dir)
        export_vocabulary(skill, out_dir)
        export_db_mock_exams(skill.upper(), out_dir)
        export_standalone_practices(skill, out_dir)


if __name__ == "__main__":
    main()
