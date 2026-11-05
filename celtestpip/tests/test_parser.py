import pytest
from celtestpip.crawler.rsc_parser import parse_exam_rsc, extract_json_blobs

MOCK_RSC_PAYLOAD = '''
1:"$Sreact.fragment"
7:[{"practice":{"id":"p123","name":"Meal Delivery","text":"Instructions here","audio":"https://blob.vercel.com/audio1.mp3","audio2":"https://blob.vercel.com/audio2.mp3","transcript":"Lucia: Hello","transcript2":"Man: Hi","part":{"type":"LISTENING","name":"Problem Solving","time":60}},"examId":"exam1","partNumber":1}]
8:[{"type":"question","content":{"id":"q1","priority":1,"question":"What went wrong?","option1":"Wrong order","option2":"Late delivery","option3":"Overcharged","option4":"Spoiled food","answer":"1","explanation":"She got tacos instead of salmon."},"questionNumber":1}]
'''

def test_parse_exam_rsc():
    data = parse_exam_rsc(MOCK_RSC_PAYLOAD)
    assert data is not None
    assert data["exam_id"] == "exam1"
    assert data["part_number"] == 1
    assert data["skill"] == "LISTENING"
    assert len(data["audio_urls"]) == 2
    assert "https://blob.vercel.com/audio1.mp3" in data["audio_urls"]
    assert len(data["transcripts"]) == 2
    assert len(data["questions"]) == 1
    q = data["questions"][0]
    assert q["question_text"] == "What went wrong?"
    assert q["options"] == ["Wrong order", "Late delivery", "Overcharged", "Spoiled food"]
    assert q["correct_answer"] == "1"
    assert "tacos" in q["explanation"]


def test_parse_exam_rsc_token_transcripts():
    payload = '''
7:[{"practice":{"id":"p456","name":"Conversation","text":"Listen","part":{"type":"LISTENING","name":"Conversation Part"}},"examId":"exam2","partNumber":2}]
9:T12,WOMAN: Good morning, how can I help you today?
a:T34,MAN: I would like to return this package.
'''
    data = parse_exam_rsc(payload)
    assert data["exam_id"] == "exam2"
    assert data["part_number"] == 2
    assert len(data["transcripts"]) == 2
    assert "WOMAN: Good morning, how can I help you today?" in data["transcripts"]
    assert "MAN: I would like to return this package." in data["transcripts"]


def test_parse_exam_rsc_empty():
    data = parse_exam_rsc("")
    assert data is not None
    assert isinstance(data["questions"], list)
    assert len(data["questions"]) == 0
