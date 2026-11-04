import pytest

def test_curriculum_structure():
    import french_grammar_data as data
    
    # 4 topics
    assert len(data.TOPICS) == 4
    expected_topics = [
        "Les Articles & Les Déterminants",
        "Les Temps Verbaux & Conjugaisons",
        "Les Prépositions",
        "Les Pronoms"
    ]
    for topic in expected_topics:
        assert topic in data.TOPICS

    # Exactly 80 questions
    assert len(data.QUESTIONS) == 80
    
    # Check IDs 1 to 80 sequentially
    ids = [q["id"] for q in data.QUESTIONS]
    assert ids == list(range(1, 81))

def test_topic_distribution_and_cefr_levels():
    import french_grammar_data as data
    
    for topic in data.TOPICS:
        topic_questions = [q for q in data.QUESTIONS if q["topic"] == topic]
        assert len(topic_questions) == 20
        
        a1_questions = [q for q in topic_questions if q["level"] == "A1"]
        a2_questions = [q for q in topic_questions if q["level"] == "A2"]
        assert len(a1_questions) == 10
        assert len(a2_questions) == 10

def test_question_types_and_fields():
    import french_grammar_data as data
    
    valid_types = {"fill_in_the_blank", "multiple_choice", "error_correction", "translation"}
    
    for q in data.QUESTIONS:
        assert q["type"] in valid_types
        assert len(q["prompt"].strip()) > 0
        assert len(q["scenario"].strip()) > 0
        assert len(q["answer"].strip()) > 0
        assert len(q["explanation"].strip()) > 0
        
        if q["type"] == "multiple_choice":
            assert "options" in q
            assert len(q["options"]) == 4
            assert any(q["answer"].startswith(opt[:2]) or q["answer"] == opt for opt in q["options"])
