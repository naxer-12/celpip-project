import json

# Inspect ch 12-22 text in chapters_extracted.json
with open('chapters_extracted.json') as f:
    data = json.load(f)

for ch in range(12, 23):
    txt = data[str(ch)]['text']
    lines = [l.strip() for l in txt.split('\n') if l.strip()]
    print(f'Ch {ch:02d}: {lines[1] if len(lines)>1 else ""} | {len(lines)} lines')
