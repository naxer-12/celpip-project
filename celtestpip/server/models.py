"""Pydantic schemas and data contracts for CELTESTPIP API requests and responses."""

from typing import Dict, Any, Optional
from pydantic import BaseModel, Field


class AttemptSubmission(BaseModel):
    """Schema for recording a user's completed exam part attempt."""
    exam_id: str = Field(..., description="The exam identifier, e.g. 'exam1'")
    part_number: int = Field(..., description="The part number within the exam (1-20)")
    score: int = Field(..., ge=0, description="Raw score achieved")
    total_questions: int = Field(..., ge=1, description="Total questions in this part")
    clb_estimate: Optional[int] = Field(None, description="Optional pre-computed CLB score")
    answers: Dict[str, Any] = Field(default_factory=dict, description="Dictionary of user selected answers keyed by question ID")


class QuestionAnswerSubmission(BaseModel):
    """Schema for individual question interaction."""
    questionId: Optional[str] = None
    answer: Optional[str] = None
    userAnswer: Optional[str] = None
    is_correct: Optional[bool] = None


class UserWordCreate(BaseModel):
    """Schema for saving a new vocabulary word to user's word bank."""
    word: str
    bundleId: Optional[str] = None
    translation: Optional[str] = ""
    definition: Optional[str] = ""
    example: Optional[str] = ""
    learned: Optional[bool] = False
