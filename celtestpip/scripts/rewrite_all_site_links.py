"""Internalize all external celtestpip.com links across all HTML templates.

Rewrites all absolute links pointing to https://www.celtestpip.com or https://celtestpip.com
to site-relative internal links (e.g. /listening, /exams, /courses/...) so all navigation
stays 100% within the site on Render and local environments.
"""

import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Regex to match celtestpip.com domains
DOMAIN_WITH_PATH_RE = re.compile(r"https?://(?:www\.)?celtestpip\.com/")
BARE_DOMAIN_RE = re.compile(r"https?://(?:www\.)?celtestpip\.com(?=[\"'()#>\s\\]|$)")


def rewrite_celtestpip_links(text: str) -> str:
    """Rewrite any celtestpip.com absolute URLs to relative internal paths."""
    # 1. Replace domain followed by slash: https://www.celtestpip.com/abc -> /abc
    text = DOMAIN_WITH_PATH_RE.sub("/", text)
    # 2. Replace bare domain at end of string or before delimiters: https://www.celtestpip.com -> /
    text = BARE_DOMAIN_RE.sub("/", text)
    return text


def process_all_html_files():
    """Batch-process all HTML files in data/pages and static."""
    files_to_check = glob.glob(os.path.join(PAGES_DIR, "*.html")) + glob.glob(os.path.join(STATIC_DIR, "*.html"))
    total_modified = 0
    total_links_rewritten = 0

    print(f"Scanning {len(files_to_check)} HTML files for external celtestpip.com links...")

    for file_path in files_to_check:
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as f:
                content = f.read()

            if "celtestpip.com" in content:
                # Count before
                matches_before = len(DOMAIN_WITH_PATH_RE.findall(content)) + len(BARE_DOMAIN_RE.findall(content))
                if matches_before > 0:
                    rewritten = rewrite_celtestpip_links(content)
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(rewritten)
                    total_modified += 1
                    total_links_rewritten += matches_before
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    print(f"Completed! Modified {total_modified} files, rewritten {total_links_rewritten} links to internal paths.")


if __name__ == "__main__":
    process_all_html_files()
