"""Practice questions, interactive answers, and task submissions.

Handles live question interaction without perpetual spinners, progress tracking,
answer explanations, and Writing/Speaking submission feedback.
"""

import os
import re
import json
from typing import Dict, Any, List
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from celtestpip.server.config import PAGES_DIR

router = APIRouter(tags=["Practices"])

USER_ANSWERS: Dict[str, str] = {}


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


@router.post("/api/writing")
@router.post("/api/writing/update")
async def handle_writing_submit(request: Request) -> Dict[str, Any]:
    """Process CELPIP Writing Task responses (Email / Survey)."""
    return {
        "id": "mock_writing_submit_1",
        "score": 10,
        "clb": 10,
        "wordCount": 185,
        "feedback": "Strong lexical variety, clear coherence, accurate paragraph transitions, and task fulfillment.",
        "corrected": "Excellent draft. Minor stylistic tweaks applied.",
        "createdAt": "2026-11-05T20:00:00Z",
    }


@router.post("/api/speaking")
@router.post("/api/speaking/update")
async def handle_speaking_submit(request: Request) -> Dict[str, Any]:
    """Process CELPIP Speaking Task audio / responses."""
    return {
        "id": "mock_speaking_submit_1",
        "score": 10,
        "clb": 10,
        "fluency": "High",
        "pronunciation": "Clear",
        "vocabulary": "Advanced",
        "feedback": "Natural pace, coherent structure, varied vocabulary, and clear speech delivery.",
        "createdAt": "2026-11-05T20:00:00Z",
    }
