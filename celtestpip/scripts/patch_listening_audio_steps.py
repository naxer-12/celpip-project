"""Patch all CELPIP listening practice pages with initial audio step.

Inserts the passage audio (section1.mp3 / conversation 1) immediately following
the task instructions screen so the listening audio plays before the questions.
"""

import os
import json
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")


def patch_listening_practice_html(content: str) -> str:
    """Insert initial passage audio step after task instructions if missing."""
    prefix = "steps\\\":["
    idx = content.find(prefix)
    if idx == -1:
        return content
    start_arr = idx + len(prefix)

    first_sep = content.find("},{\\\"type\\\":\\\"", start_arr)
    if first_sep == -1:
        return content

    step1_type = content[
        first_sep + len("},{\\\"type\\\":\\\"") : first_sep + len("},{\\\"type\\\":\\\"") + 20
    ].split("\\\"")[0]
    if step1_type == "audio":
        return content

    # Extract practice object by balanced braces
    p_prefix = "practice\\\":{"
    p_idx = content.find(p_prefix)
    if p_idx == -1:
        return content
    start_obj = p_idx + len(p_prefix) - 1
    depth = 0
    found = False
    for i in range(start_obj, len(content)):
        c = content[i]
        if c == "{":
            depth += 1
            found = True
        elif c == "}":
            depth -= 1
            if found and depth == 0:
                end_obj = i + 1
                break
    if not found:
        return content

    try:
        raw_p_str = content[start_obj:end_obj]
        decoded_p = raw_p_str.encode("utf-8").decode("unicode_escape")
        practice = json.loads(decoded_p)
    except Exception:
        return content

    if not practice.get("audio"):
        return content

    new_audio_step = {
        "type": "audio",
        "title": "Audio",
        "audio": practice["audio"],
        "transcript": practice.get("transcript", ""),
        "timings": practice.get("audioTimings"),
    }

    raw_step0_end = first_sep + 1

    dumped = json.dumps(new_audio_step, separators=(",", ":"))
    escaped = dumped.replace("\\", "\\\\").replace('"', r'\"')

    patched = content[:raw_step0_end] + "," + escaped + content[raw_step0_end:]

    # Shift any Flight path references into subsequent audio steps (e.g. Part 1 sections 2 & 3)
    if "steps:7:timings" in patched:
        patched = patched.replace("steps:7:timings", "steps:8:timings")
    if "steps:3:timings" in patched:
        patched = patched.replace("steps:3:timings", "steps:4:timings")

    return patched


def patch_all_practices() -> int:
    """Patch all listening practice files on disk."""
    files = glob.glob(os.path.join(PAGES_DIR, "practices_listening_*.html"))
    count = 0
    for fpath in files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        patched = patch_listening_practice_html(content)
        if patched != content:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(patched)
            count += 1

    print(f"Patched {count} listening practice files with initial audio step.")
    return count


if __name__ == "__main__":
    patch_all_practices()
