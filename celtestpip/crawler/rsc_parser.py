import re
import json
from typing import Dict, Any, List, Optional


def extract_json_blobs(text: str) -> List[Any]:
    blobs = []
    # Pattern to match lines like: id:[...] or id:{...}
    # where id is hex or alphanumeric
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        colon_idx = line.find(":")
        if colon_idx != -1 and line[:colon_idx].replace("_", "").isalnum():
            candidate = line[colon_idx + 1:].strip()
            if candidate.startswith(("{", "[")):
                try:
                    obj = json.loads(candidate)
                    blobs.append(obj)
                except Exception:
                    pass
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
    
    # Locate questions
    question_candidates = []
    for b in blobs:
        # Check direct questions list or walk
        qs = _walk_for_key(b, "questions")
        if qs and isinstance(qs[0], list):
            question_candidates.extend(qs[0])
        # Also check elements with "type": "question"
        if isinstance(b, list):
            for item in b:
                if isinstance(item, dict) and item.get("type") == "question":
                    question_candidates.append(item)
    
    # Deduplicate questions by ID or number
    questions = []
    seen_q_ids = set()
    for qc in question_candidates:
        content = qc.get("content", qc)
        qid = content.get("id") or str(qc.get("questionNumber"))
        if qid in seen_q_ids:
            continue
        seen_q_ids.add(qid)
        
        # Build options list
        options = []
        for i in range(1, 9):
            opt = content.get(f"option{i}")
            if opt:
                options.append(str(opt).strip())
                
        questions.append({
            "id": qid,
            "question_number": qc.get("questionNumber", len(questions) + 1),
            "priority": content.get("priority", 0),
            "question_text": content.get("question", ""),
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
            part_number = int(pnums[0])
            
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
