"""Practice questions, interactive answers, and task submissions.

Handles live question interaction without perpetual spinners, progress tracking,
answer explanations, and Writing/Speaking submission feedback.
"""

from typing import Dict, Any
from fastapi import APIRouter, Request

router = APIRouter(tags=["Practices"])


@router.put("/api/practices/{practice_id}/done")
@router.post("/api/practices/{practice_id}/done")
def mark_practice_done(practice_id: str) -> Dict[str, Any]:
    """Mark a practice session as completed."""
    return {"status": "ok", "practiceId": practice_id, "isCompleted": True}


@router.get("/api/practices/{practice_id}/result")
def get_practice_result(practice_id: str) -> Dict[str, Any]:
    """Retrieve score, accuracy, and detailed results for a practice test."""
    return {"result": {"score": 8, "total": 8, "percentage": 100}}


@router.put("/api/practices/{practice_id}/explanation")
@router.post("/api/practices/{practice_id}/explanation")
def unlock_practice_explanation(practice_id: str) -> Dict[str, Any]:
    """Unlock detailed question rationale and explanation."""
    return {"result": {"explanation": "Explanations unlocked for testing."}}


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
