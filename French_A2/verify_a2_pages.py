import os
import subprocess

SAMPLE_PAGES = [1, 4, 16, 25, 30, 50, 71]
pdf_path = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_A2.pdf"
out_dir = "/tmp/a2_verify"
os.makedirs(out_dir, exist_ok=True)

for p in SAMPLE_PAGES:
    prefix = f"{out_dir}/page_{p}"
    cmd = ["pdftoppm", "-png", "-r", "150", "-f", str(p), "-l", str(p), pdf_path, prefix]
    subprocess.run(cmd, check=True)
    print(f"Rendered sample page {p}")
