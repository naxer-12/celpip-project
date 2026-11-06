import re
import json
from typing import Dict, Any, List, Optional


def parse_all_rsc_chunks(stream: str) -> Dict[str, Any]:
    chunks = {}
    stream_bytes = stream.encode("utf-8") if isinstance(stream, str) else stream
    pos = 0
    length = len(stream_bytes)
    decoder = json.JSONDecoder()
    while pos < length:
        while pos < length and stream_bytes[pos:pos+1] in (b"\r", b"\n"):
            pos += 1
        if pos >= length:
            break
        colon_idx = stream_bytes.find(b":", pos)
        if colon_idx == -1:
            break
        chunk_id = stream_bytes[pos:colon_idx].decode("ascii", errors="ignore")
        if not re.match(r"^[0-9a-fA-F]+$", chunk_id):
            next_nl = stream_bytes.find(b"\n", pos)
            if next_nl == -1:
                break
            pos = next_nl + 1
            continue
        pos = colon_idx + 1
        if pos < length and stream_bytes[pos:pos+1] == b"T":
            comma_idx = stream_bytes.find(b",", pos)
            if comma_idx == -1:
                break
            hex_len = stream_bytes[pos+1:comma_idx].decode("ascii", errors="ignore")
            try:
                byte_len = int(hex_len, 16)
            except ValueError:
                next_nl = stream_bytes.find(b"\n", pos)
                if next_nl == -1:
                    break
                pos = next_nl + 1
                continue
            val_start = comma_idx + 1
            next_nl = stream_bytes.find(b"\n", val_start)
            if next_nl != -1 and byte_len < (next_nl - val_start):
                line_part = stream_bytes[val_start:next_nl]
                if any(m in line_part for m in [b"WOMAN:", b"MAN:", b"Speaker:"]):
                    byte_len = next_nl - val_start
            val_end = val_start + byte_len
            chunks[chunk_id] = stream_bytes[val_start:val_end].decode("utf-8", errors="replace").strip("\r\n")
            pos = val_end
        else:
            try:
                text_slice = stream_bytes[pos:].decode("utf-8")
                obj, end = decoder.raw_decode(text_slice)
                chunks[chunk_id] = obj
                pos += len(text_slice[:end].encode("utf-8"))
            except Exception:
                next_nl = stream_bytes.find(b"\n", pos)
                if next_nl == -1:
                    break
                pos = next_nl + 1
    return chunks


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
    chunks = parse_all_rsc_chunks(rsc_text)

    def resolve_val(val: Any) -> Any:
        if isinstance(val, str) and val.startswith("$"):
            k = val[1:]
            if k in chunks:
                return resolve_val(chunks[k])
        return val

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
                options.append(str(resolve_val(opt)).strip())
                
        q_text = str(resolve_val(content.get("question", "")))
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
            "explanation": str(resolve_val(content.get("explanation", ""))),
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
        instructions = str(resolve_val(p.get("text", "")))
        
        for a_key in ["audio", "audio2", "audio3"]:
            a = p.get(a_key)
            if a and a.startswith("http"):
                audio_urls.append(a)
                
        for t_key in ["transcript", "transcript2", "transcript3"]:
            t = resolve_val(p.get(t_key))
            if t and isinstance(t, str) and not t.startswith("$") and t not in transcripts:
                transcripts.append(t)
                
        image_url = p.get("image")
        
    # Check if transcripts were stored as string tokens or text chunks in RSC
    for chunk_val in chunks.values():
        if isinstance(chunk_val, str) and any(marker in chunk_val for marker in ["WOMAN:", "MAN:", "Speaker:"]):
            val_clean = chunk_val.strip()
            if val_clean not in transcripts:
                transcripts.append(val_clean)
                
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
