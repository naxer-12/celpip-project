"""Official CELPIP raw score (out of 38) to Canadian Language Benchmark (CLB) conversion."""


def raw_score_to_clb(skill: str, score: int) -> int:
    score = max(0, min(38, score))
    if skill.upper() == "LISTENING":
        if score >= 37:
            return 12
        if score >= 35:
            return 11
        if score >= 33:
            return 10
        if score >= 30:
            return 9
        if score >= 27:
            return 8
        if score >= 23:
            return 7
        if score >= 17:
            return 6
        if score >= 11:
            return 5
        if score >= 7:
            return 4
        return 3
    elif skill.upper() == "READING":
        if score >= 38:
            return 12
        if score >= 36:
            return 11
        if score >= 33:
            return 10
        if score >= 31:
            return 9
        if score >= 28:
            return 8
        if score >= 24:
            return 7
        if score >= 19:
            return 6
        if score >= 15:
            return 5
        if score >= 10:
            return 4
        return 3
    return 7
