"""Practice questions, interactive answers, and task submissions.

Handles live question interaction without perpetual spinners, progress tracking,
answer explanations, and Writing/Speaking submission feedback.
"""

import os
import re
import json
import uuid
from typing import Dict, Any, List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from celtestpip.server.config import PAGES_DIR
from celtestpip.server.scoring import evaluate_writing_response, evaluate_speaking_response

router = APIRouter(tags=["Practices"])

USER_ANSWERS: Dict[str, str] = {}
WRITING_SUBMISSIONS: Dict[str, Dict[str, Any]] = {}
SPEAKING_SUBMISSIONS: Dict[str, Dict[str, Any]] = {}


def get_practice_questions(practice_id: str) -> List[Dict[str, Any]]:
    clean_id = (
        practice_id.replace("listening_", "")
        .replace("reading_", "")
        .replace("writing_", "")
        .replace("speaking_", "")
    )
    cand_files = [
        os.path.join(PAGES_DIR, f"practices_listening_{clean_id}.html"),
        os.path.join(PAGES_DIR, f"practices_{practice_id}.html"),
        os.path.join(PAGES_DIR, f"practices_{clean_id}.html"),
    ]
    target_file = None
    for cf in cand_files:
        if os.path.exists(cf) and os.path.getsize(cf) > 1000:
            target_file = cf
            break

    if not target_file:
        return []

    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return []

    # 1. First attempt: Extract full Question array directly from practice JSON object
    questions = []
    p_idx = content.find("practice\\\":{")
    if p_idx != -1:
        start = p_idx + len("practice\\\":{") - 1
        depth = 0
        found = False
        for i in range(start, len(content)):
            if content[i] == "{":
                depth += 1
                found = True
            elif content[i] == "}":
                depth -= 1
                if found and depth == 0:
                    end = i + 1
                    break
        if found:
            try:
                p_obj = json.loads(content[start:end].encode("utf-8").decode("unicode_escape"))
                raw_qs = p_obj.get("Question") or []
                for q in raw_qs:
                    qid = str(q.get("id"))
                    ans = str(q.get("answer", "1"))
                    user_val = USER_ANSWERS.get(qid)
                    if user_val:
                        if str(user_val).startswith("option"):
                            user_ans_str = str(user_val)
                            opt_num = user_ans_str.replace("option", "")
                        else:
                            opt_num = str(user_val)
                            user_ans_str = f"option{opt_num}"
                        is_correct = (str(opt_num) == str(ans))
                    else:
                        user_ans_str = None
                        is_correct = False

                    opts = {
                        "option1": q.get("option1"),
                        "option2": q.get("option2"),
                        "option3": q.get("option3"),
                        "option4": q.get("option4"),
                        "option5": q.get("option5"),
                        "option6": q.get("option6"),
                        "option7": q.get("option7"),
                        "option8": q.get("option8"),
                    }
                    correct_cnt = q.get("correctCount", 8000) or 8000
                    incorrect_cnt = q.get("incorrectCount", 1500) or 1500
                    questions.append({
                        "id": qid,
                        "priority": q.get("priority", 1),
                        "question": q.get("question", ""),
                        "audio": q.get("audio"),
                        "options": opts,
                        "option1": q.get("option1"),
                        "option2": q.get("option2"),
                        "option3": q.get("option3"),
                        "option4": q.get("option4"),
                        "option5": q.get("option5"),
                        "option6": q.get("option6"),
                        "option7": q.get("option7"),
                        "option8": q.get("option8"),
                        "explanation": q.get("explanation", ""),
                        "section": q.get("section", 1),
                        "answer": ans,
                        "practiceId": practice_id,
                        "correctCount": correct_cnt,
                        "incorrectCount": incorrect_cnt,
                        "correctPercentage": round(correct_cnt / max(1, (correct_cnt + incorrect_cnt)) * 100),
                        "userAnswer": user_ans_str,
                        "isCorrect": is_correct,
                    })
            except Exception:
                pass

    if questions:
        return questions

    # 2. Fallback: Regex matching from raw flight lines
    matches = re.findall(
        r"\{\\\"id\\\":\\\"([a-zA-Z0-9_-]+)\\\",\\\"priority\\\":\d+,\\\"question\\\":\\\"(.*?)\\\".*?\\\"option1\\\":\\\"(.*?)\\\",\\\"option2\\\":\\\"(.*?)\\\",\\\"option3\\\":\\\"(.*?)\\\",\\\"option4\\\":\\\"(.*?)\\\".*?\\\"explanation\\\":\\\"(.*?)\\\".*?\\\"answer\\\":\\\"(\d+)\\\"",
        content,
    )

    seen = set()
    for m in matches:
        qid = m[0]
        if qid in seen:
            continue
        seen.add(qid)
        ans = str(m[7])
        user_val = USER_ANSWERS.get(qid)
        if user_val:
            if str(user_val).startswith("option"):
                user_ans_str = str(user_val)
                opt_num = user_ans_str.replace("option", "")
            else:
                opt_num = str(user_val)
                user_ans_str = f"option{opt_num}"
            is_correct = (str(opt_num) == str(ans))
        else:
            user_ans_str = None
            is_correct = False

        opt1 = m[2].replace('\\"', '"')
        opt2 = m[3].replace('\\"', '"')
        opt3 = m[4].replace('\\"', '"')
        opt4 = m[5].replace('\\"', '"')
        opts = {
            "option1": opt1,
            "option2": opt2,
            "option3": opt3,
            "option4": opt4,
            "option5": None,
            "option6": None,
            "option7": None,
            "option8": None,
        }
        questions.append({
            "id": qid,
            "question": m[1].replace('\\"', '"').replace('\\\\n', '\n'),
            "options": opts,
            "option1": opt1,
            "option2": opt2,
            "option3": opt3,
            "option4": opt4,
            "explanation": m[6].replace('\\"', '"').replace('\\\\n', '\n'),
            "answer": ans,
            "userAnswer": user_ans_str,
            "isCorrect": is_correct,
            "correctPercentage": 82,
        })
    return questions


@router.put("/api/practices/{practice_id}/done")
@router.post("/api/practices/{practice_id}/done")
def mark_practice_done(practice_id: str) -> Dict[str, Any]:
    """Mark a practice session as completed."""
    return {"status": "ok", "practiceId": practice_id, "isCompleted": True}


@router.get("/api/practices/{practice_id}/result")
def get_practice_result(practice_id: str):
    """Retrieve score, accuracy, and detailed results for a practice test."""
    questions = get_practice_questions(practice_id)
    if questions:
        return JSONResponse(
            content={"result": questions, "betterThanPercentage": 85},
            headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
        )
    return JSONResponse(
        content={"result": [], "betterThanPercentage": 85},
        headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
    )


@router.put("/api/practices/{practice_id}/explanation")
@router.post("/api/practices/{practice_id}/explanation")
def unlock_practice_explanation(practice_id: str):
    """Unlock detailed question rationale and explanation."""
    questions = get_practice_questions(practice_id)
    if questions:
        return JSONResponse(
            content={"result": questions, "betterThanPercentage": 85},
            headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
        )
    return JSONResponse(
        content={"result": {"explanation": "Explanations unlocked for testing."}},
        headers={"Cache-Control": "no-store, no-cache, must-revalidate"},
    )


@router.post("/api/practices/{practice_id}/answer")
def record_practice_answer(practice_id: str) -> Dict[str, Any]:
    """Record an answer for a specific practice item."""
    return {"status": "ok"}


@router.post("/api/question")
async def record_question_answer(request: Request) -> Dict[str, Any]:
    """Handle instant question answer submission.
    
    Provides immediate 200 OK so client radio buttons reflect chosen state
    without hanging or showing perpetual spinning loading indicators.
    """
    try:
        data = await request.json()
    except Exception:
        data = {}
    if "questionId" in data and "answer" in data:
        qid = str(data["questionId"])
        USER_ANSWERS[qid] = str(data["answer"])
    return {
        "ok": True,
        "status": "ok",
        "questionId": data.get("questionId"),
        "answer": data.get("answer"),
    }


@router.post("/api/questions/report")
async def report_question(request: Request) -> Dict[str, Any]:
    """Acknowledge question bug reports and feedback."""
    return {"ok": True, "status": "ok"}


async def _extract_request_payload(request: Request) -> Dict[str, Any]:
    """Parse either multipart/form-data or JSON body safely without failing on empty requests."""
    content_type = (request.headers.get("content-type") or "").lower()
    payload: Dict[str, Any] = {}
    if "multipart/form-data" in content_type or "application/x-www-form-urlencoded" in content_type:
        try:
            form = await request.form()
            for key, val in form.multi_items():
                if hasattr(val, "read"):
                    raw_bytes = await val.read()
                    payload["_audio_size_bytes"] = len(raw_bytes)
                else:
                    payload[key] = val
        except Exception:
            pass
    elif "application/json" in content_type:
        try:
            data = await request.json()
            if isinstance(data, dict):
                payload.update(data)
        except Exception:
            pass
    else:
        try:
            raw_body = await request.body()
            if raw_body:
                data = json.loads(raw_body.decode("utf-8"))
                if isinstance(data, dict):
                    payload.update(data)
        except Exception:
            pass
    return payload


@router.post("/api/writing")
@router.post("/api/writing/update")
async def handle_writing_submit(request: Request) -> Dict[str, Any]:
    """Process CELPIP Writing Task responses (Email / Survey) with offline CLB scoring."""
    payload = await _extract_request_payload(request)
    is_update = request.url.path.endswith("/update")
    existing_id = str(payload.get("userPracticeSubmitId") or "").strip()

    if is_update and existing_id and existing_id in WRITING_SUBMISSIONS:
        prev = WRITING_SUBMISSIONS[existing_id]
        result = evaluate_writing_response(
            response_text=prev.get("_raw_text", ""),
            practice_id=prev.get("practiceId") or "",
            time_spent=prev.get("timeSpent"),
            submission_id=existing_id,
        )
        WRITING_SUBMISSIONS[existing_id] = {**result, "_raw_text": prev.get("_raw_text", "")}
        return result

    response_text = str(
        payload.get("response")
        or payload.get("text")
        or payload.get("content")
        or payload.get("answer")
        or ""
    )
    practice_id = str(payload.get("practiceId") or "")
    time_spent_raw = payload.get("timeSpent")
    try:
        time_spent = int(time_spent_raw) if time_spent_raw is not None and str(time_spent_raw).strip() != "" else None
    except (ValueError, TypeError):
        time_spent = None

    sub_id = existing_id or (f"writing_{uuid.uuid4().hex[:12]}" if response_text.strip() else "mock_writing_submit_1")
    result = evaluate_writing_response(
        response_text=response_text,
        practice_id=practice_id,
        time_spent=time_spent,
        submission_id=sub_id,
    )
    WRITING_SUBMISSIONS[sub_id] = {**result, "_raw_text": response_text}
    return result


@router.post("/api/speaking")
@router.post("/api/speaking/update")
async def handle_speaking_submit(request: Request) -> Dict[str, Any]:
    """Process CELPIP Speaking Task audio / responses with offline CLB scoring."""
    payload = await _extract_request_payload(request)
    is_update = request.url.path.endswith("/update")
    existing_id = str(payload.get("userPracticeSubmitId") or "").strip()

    if is_update and existing_id and existing_id in SPEAKING_SUBMISSIONS:
        prev = SPEAKING_SUBMISSIONS[existing_id]
        result = evaluate_speaking_response(
            audio_size_bytes=prev.get("_audio_size_bytes", 0),
            transcript=prev.get("_transcript", ""),
            practice_text=prev.get("_practice_text", ""),
            practice_id=prev.get("practiceId") or "",
            duration_seconds=prev.get("estimatedDurationSec"),
            submission_id=existing_id,
        )
        SPEAKING_SUBMISSIONS[existing_id] = {
            **result,
            "_audio_size_bytes": prev.get("_audio_size_bytes", 0),
            "_transcript": prev.get("_transcript", ""),
            "_practice_text": prev.get("_practice_text", ""),
        }
        return result

    audio_size_bytes = int(payload.get("_audio_size_bytes", 0) or 0)
    transcript = str(
        payload.get("transcript")
        or payload.get("response")
        or payload.get("text")
        or ""
    )
    practice_text = str(payload.get("practiceText") or "")
    practice_id = str(payload.get("practiceId") or "")
    duration_raw = payload.get("duration") or payload.get("audioDuration")
    try:
        duration_seconds = float(duration_raw) if duration_raw is not None and str(duration_raw).strip() != "" else None
    except (ValueError, TypeError):
        duration_seconds = None

    has_input = audio_size_bytes > 0 or bool(transcript.strip()) or duration_seconds is not None
    sub_id = existing_id or (f"speaking_{uuid.uuid4().hex[:12]}" if has_input else "mock_speaking_submit_1")

    result = evaluate_speaking_response(
        audio_size_bytes=audio_size_bytes,
        transcript=transcript,
        practice_text=practice_text,
        practice_id=practice_id,
        duration_seconds=duration_seconds,
        submission_id=sub_id,
    )
    SPEAKING_SUBMISSIONS[sub_id] = {
        **result,
        "_audio_size_bytes": audio_size_bytes,
        "_transcript": transcript,
        "_practice_text": practice_text,
    }
    return result
