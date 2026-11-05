import re
import json
from typing import Dict, Any, List, Optional


def extract_json_blobs(text: str) -> List[Any]:
    blobs = []
    decoder = json.JSONDecoder()
    pos = 0
    length = len(text)
    
    while pos < length:
        idx1 = text.find('[', pos)
        idx2 = text.find('{', pos)
        if idx1 == -1 and idx2 == -1:
            break
        start = idx1 if idx2 == -1 else (idx2 if idx1 == -1 else min(idx1, idx2))
        try:
            obj, end = decoder.raw_decode(text, start)
            blobs.append(obj)
            pos = max(end, start + 1)
        except Exception:
            pos = start + 1
            
    return blobs


def _walk_for_key(obj: Any, key: str) -> List[Any]:
    results = []
    if isinstance(obj, dict):
        if key in obj:
            results.append(obj[key])
        for v in obj.values():
            results.extend(_walk_for_key(v, key))
    elif isinstance(obj, list):
        for item in obj:
            results.extend(_walk_for_key(item, key))
    return results


def parse_exam_rsc(rsc_text: str) -> Optional[Dict[str, Any]]:
    blobs = extract_json_blobs(rsc_text)
    
    # Locate practice object
    practice_objs = []
    for b in blobs:
        practice_objs.extend(_walk_for_key(b, "practice"))
    practice_objs = [p for p in practice_objs if isinstance(p, dict)]
    
    # Locate questions
    question_candidates = []
    def _find_q(obj):
        res = []
        if isinstance(obj, dict):
            if "option1" in obj or ("type" in obj and obj.get("type") == "question"):
                res.append(obj)
            for v in obj.values():
                res.extend(_find_q(v))
        elif isinstance(obj, list):
            for item in obj:
                res.extend(_find_q(item))
        return res

    for b in blobs:
        # Check direct questions list or walk
        qs = _walk_for_key(b, "questions")
        if qs and isinstance(qs[0], list):
            question_candidates.extend(qs[0])
        question_candidates.extend(_find_q(b))
    
    # Deduplicate questions by ID or text/options
    questions = []
    seen_q_ids = set()
    for qc in question_candidates:
        if not isinstance(qc, dict):
            continue
        content = qc.get("content", qc)
        if not isinstance(content, dict):
            continue
        
        # Build options list
        options = []
        for i in range(1, 9):
            opt = content.get(f"option{i}")
            if opt:
                options.append(str(opt).strip())
                
        q_text = content.get("question", "")
        if not q_text and not options:
            continue

        qid = content.get("id") or str(qc.get("questionNumber")) or f"q_{len(questions)+1}"
        dedup_key = qid if content.get("id") else f"{q_text}_{options[:1]}"
        if dedup_key in seen_q_ids:
            continue
        seen_q_ids.add(dedup_key)
        
        questions.append({
            "id": qid,
            "question_number": qc.get("questionNumber", len(questions) + 1),
            "priority": content.get("priority", 0),
            "question_text": q_text,
            "audio_url": content.get("audio"),
            "options": options,
            "correct_answer": str(content.get("answer", "")),
            "explanation": content.get("explanation", ""),
            "section": content.get("section", 1)
        })
    
    # Extract metadata
    exam_id = "exam1"
    part_number = 1
    skill = "LISTENING"
    part_name = "Practice Part"
    practice_id = ""
    transcripts = []
    audio_urls = []
    image_url = None
    instructions = ""
    
    for b in blobs:
        eids = _walk_for_key(b, "examId")
        if eids:
            exam_id = eids[0]
        pnums = _walk_for_key(b, "partNumber")
        if pnums:
            digits = re.search(r'\d+', str(pnums[0]))
            if digits:
                part_number = int(digits.group())
            
    if practice_objs:
        p = practice_objs[0]
        practice_id = str(p.get("id", ""))
        part_info = p.get("part", {})
        skill = part_info.get("type", "LISTENING")
        part_name = p.get("name", part_info.get("name", "Practice Part"))
        instructions = p.get("text", "")
        
        for a_key in ["audio", "audio2", "audio3"]:
            a = p.get(a_key)
            if a and a.startswith("http"):
                audio_urls.append(a)
                
        for t_key in ["transcript", "transcript2", "transcript3"]:
            t = p.get(t_key)
            if t and isinstance(t, str) and not t.startswith("$"):
                transcripts.append(t)
                
        image_url = p.get("image")
        
    # Check if transcripts were stored as string tokens elsewhere in RSC
    for line in rsc_text.split("\n"):
        if re.search(r'^[0-9a-f]+:T[0-9a-f]+,', line):
            text_val = re.sub(r'^[0-9a-f]+:T[0-9a-f]+,', '', line).strip()
            if any(marker in text_val for marker in ["WOMAN:", "MAN:", "Speaker:"]) and text_val not in transcripts:
                transcripts.append(text_val)
                
    return {
        "exam_id": exam_id,
        "part_number": part_number,
        "skill": skill,
        "part_name": part_name,
        "part_title": part_name,
        "practice_id": practice_id,
        "instructions": instructions,
        "audio_urls": audio_urls,
        "image_url": image_url,
        "image_urls": [image_url] if image_url else [],
        "transcripts": transcripts,
        "questions": questions
    }
