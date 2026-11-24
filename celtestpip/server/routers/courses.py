"""Course section progress and completion tracking router.

Enables marking course lessons as complete or incomplete, storing progress
in local SQLite and Turso cloud database for permanent persistence across restarts.
"""

from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel
from celtestpip.server.database import save_course_progress, get_completed_course_sections

router = APIRouter(prefix="/api/courses", tags=["Courses"])


class CourseProgressRequest(BaseModel):
    sectionId: str
    completed: bool


@router.post("/sections/{section_id}/progress")
def update_section_progress(section_id: str, payload: CourseProgressRequest):
    """Mark a course lesson / section as complete or incomplete."""
    save_course_progress(section_id, payload.completed)
    return {
        "success": True,
        "sectionId": section_id,
        "completed": payload.completed,
    }


@router.get("/sections/{section_id}/progress")
def get_section_progress(section_id: str):
    """Retrieve progress state for a specific course section."""
    completed_sections = get_completed_course_sections()
    is_completed = section_id in completed_sections
    return {
        "sectionId": section_id,
        "completed": is_completed,
    }


@router.get("/progress")
def get_all_course_progress():
    """Retrieve all completed course sections for the active user."""
    completed_sections = list(get_completed_course_sections())
    return {
        "completedSections": completed_sections,
    }
