#!/usr/bin/env python3
"""
update_and_run_markdown_generators.py - Add resources support to markdown generators and run them
"""

import os

MARKDOWN_GENERATORS = [
    ("French_A2", "generate_a2_markdown.py"),
    ("French_B1", "generate_b1_markdown.py"),
    ("French_B2", "generate_b2_markdown.py"),
    ("French_C1", "generate_c1_markdown.py"),
    ("French_C2", "generate_c2_markdown.py"),
]

RESOURCES_MD_SNIPPET = """
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
                lines.append(f"- [ ] Active study resource verified\\n")
"""

def update_md_script(level_dir, script_name):
    filepath = os.path.join(level_dir, script_name)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if 'elif p_type == "resources":' not in content:
        target = 'elif p_type == "audit":'
        if target in content:
            content = content.replace(target, RESOURCES_MD_SNIPPET.strip() + "\n        " + target)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filepath}")
        else:
            print(f"Could not find target in {filepath}")

    # Run the script
    cmd = f'cd "{level_dir}" && python3 {script_name}'
    print(f"Running {cmd}...")
    os.system(cmd)

def main():
    for level_dir, script_name in MARKDOWN_GENERATORS:
        update_md_script(level_dir, script_name)

if __name__ == "__main__":
    main()
