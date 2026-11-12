"""CELPIP Canadian Language Benchmark (CLB) Scoring Engine.

This module converts raw scores (out of 38 questions for Listening and Reading)
into Canadian Language Benchmark (CLB) levels (CLB 3 to 12).

Official Canadian Immigration Context (IRCC):
- CLB 4-5: Initial Basic Proficiency (Federal Skilled Trades baseline, Citizenship).
- CLB 7: Adequate Intermediate Proficiency (Federal Skilled Worker minimum threshold).
- CLB 9+: Initial Advanced Proficiency (Unlocks maximum CRS points in Express Entry).
- CLB 10-12: Fluent / Advanced Native-equivalent Proficiency.
"""

from typing import Dict, Tuple

# Mapping of raw score ranges (min_score, max_score) to official CLB benchmark level
LISTENING_CLB_TABLE: Dict[int, Tuple[int, int]] = {
    12: (37, 38),
    11: (35, 36),
    10: (33, 34),
    9: (30, 32),
    8: (27, 29),
    7: (23, 26),
    6: (17, 22),
    5: (11, 16),
    4: (7, 10),
    3: (0, 6),
}

READING_CLB_TABLE: Dict[int, Tuple[int, int]] = {
    12: (38, 38),
    11: (36, 37),
    10: (33, 35),
    9: (31, 32),
    8: (28, 30),
    7: (24, 27),
    6: (19, 23),
    5: (15, 18),
    4: (10, 14),
    3: (0, 9),
}


def raw_score_to_clb(skill: str, score: int) -> int:
    """Convert raw score (0-38) to Canadian Language Benchmark (CLB) level 3-12.

    Args:
        skill: The skill evaluated ('LISTENING', 'READING', 'WRITING', 'SPEAKING').
        score: The raw score achieved (clamped between 0 and 38).

    Returns:
        Integer benchmark score between 3 and 12.
    """
    score = max(0, min(38, int(score)))
    skill_clean = (skill or "").strip().upper()

    if skill_clean == "LISTENING":
        for clb_level, (min_val, max_val) in LISTENING_CLB_TABLE.items():
            if min_val <= score <= max_val:
                return clb_level
        return 3

    if skill_clean == "READING":
        for clb_level, (min_val, max_val) in READING_CLB_TABLE.items():
            if min_val <= score <= max_val:
                return clb_level
        return 3

    # For qualitative skills (Writing / Speaking) or uncalibrated parts, default to CLB 7
    return 7


def get_clb_description(clb: int) -> str:
    """Return a descriptive human-readable summary of the CLB level."""
    descriptions = {
        12: "Flawless Proficiency: Fluent, nuanced English in all professional and social domains.",
        11: "Advanced Proficiency: Understands and produces complex language with high precision.",
        10: "Highly Effective: Communicates effectively with subtle understanding of tone and context.",
        9: "Express Entry Sweet Spot: Strong operational command with minor non-systemic inaccuracies.",
        8: "Fluent Everyday Command: Understands complex speech and texts with good vocabulary range.",
        7: "Adequate Intermediate: Minimum requirement for Express Entry Federal Skilled Worker stream.",
        6: "Developing Intermediate: Capable in familiar situations, some hesitation in complex tasks.",
        5: "Basic Work Proficiency: Meets basic communication needs for vocational tasks.",
        4: "Minimum Citizenship Threshold: Handles simple everyday interactions.",
        3: "Beginning English: Limited vocabulary and simple sentence structures.",
    }
    return descriptions.get(clb, "Standard benchmark proficiency")
