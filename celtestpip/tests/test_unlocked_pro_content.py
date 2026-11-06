import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app
from celtestpip.scripts.unlock_all_pro_content import clean_html

@pytest.fixture
def client():
    return TestClient(app)

def test_mock_membership_api(client):
    resp = client.get("/api/user/membership")
    assert resp.status_code == 200
    data = resp.json()
    assert data["isPremium"] is True
    assert data["isPro"] is True
    assert data["credits"] == 9999
    assert data["user"]["id"] == "tester"

def test_mock_credits_api(client):
    resp = client.get("/api/user/credits")
    assert resp.status_code == 200
    data = resp.json()
    assert data["credits"] == 9999
    assert data["isPro"] is True
    assert data["isPremium"] is True

def test_mock_practices_api(client):
    # Done
    resp = client.put("/api/practices/listening_123/done")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

    # Result
    resp = client.get("/api/practices/listening_123/result")
    assert resp.status_code == 200
    assert "result" in resp.json()

    # Explanation
    resp = client.put("/api/practices/listening_123/explanation")
    assert resp.status_code == 200
    assert "explanation" in resp.json()["result"]

    # Answer
    resp = client.post("/api/practices/listening_123/answer")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"

def test_mock_writing_and_speaking_api(client):
    # Writing
    resp = client.post("/api/writing")
    assert resp.status_code == 200
    w_data = resp.json()
    assert "id" in w_data
    assert w_data["score"] == 10
    assert w_data["clb"] == 10

    # Speaking
    resp = client.post("/api/speaking")
    assert resp.status_code == 200
    s_data = resp.json()
    assert "id" in s_data
    assert s_data["score"] == 10
    assert s_data["clb"] == 10

def test_clean_html_removes_paywall_elements():
    sample_locked_html = """
    <div>
        <button class="btn" disabled=""><svg class="lucide-lock"></svg>Pro only</button>
        <div class="mt-6 flex flex-col w-full lg:w-fit">
            <p>This practice is for Pro Members Only</p>
            <button>Upgrade to Pro</button>
        </div>
        <div class="fixed bottom-4 left-4 z-50">Upgrade to Pro Membership SALE</div>
        </div></div>
        <script>self.__next_f.push([1, "{\\"hasAccess\\":false,\\"isPremium\\":false,\\"isProUser\\":false,\\"userCredits\\":0,\\"userId\\":\\"$undefined\\"}"])</script>
    </div>
    """
    cleaned = clean_html(sample_locked_html)
    assert "Pro only" not in cleaned
    assert "This practice is for Pro Members Only" not in cleaned
    assert "Upgrade to Pro" not in cleaned
    assert "Upgrade to Pro Membership" not in cleaned
    assert 'hasAccess\\":true' in cleaned
    assert 'isPremium\\":true' in cleaned
    assert 'isProUser\\":true' in cleaned
    assert 'userCredits\\":9999' in cleaned
    assert 'userId\\":\\"tester\\"' in cleaned

def test_practice_page_served_unlocked(client):
    resp = client.get("/practices/listening_cmn2ldtkn008b80un8zyrvxr9")
    if resp.status_code == 200:
        html = resp.text
        assert "This practice is for Pro Members Only" not in html
        assert "Upgrade to Pro" not in html
        assert 'hasAccess\\":true' in html

def test_user_words_crud_api(client):
    # 1. Post/save word
    resp = client.post("/api/user-words", json={"word": "correspondence", "bundleId": "bundle_1"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["word"] == "correspondence"

    # 2. Get single word
    resp_get = client.get("/api/user-words/correspondence")
    assert resp_get.status_code == 200
    assert resp_get.json()["word"] == "correspondence"

    # 3. Patch word mastery and notes
    resp_patch = client.patch("/api/user-words/correspondence", json={"mastered": True, "notes": "Important term"})
    assert resp_patch.status_code == 200
    assert resp_patch.json()["mastered"] is True
    assert resp_patch.json()["notes"] == "Important term"

    # 4. Get list of user words
    resp_list = client.get("/api/user-words")
    assert resp_list.status_code == 200
    assert any(w["word"] == "correspondence" for w in resp_list.json())

def test_words_catalog_served_unlocked(client):
    resp = client.get("/words")
    assert resp.status_code == 200
    html = resp.text
    # Zero lock icons on word bundle cards
    assert "lucide-lock" not in html

def test_words_bundle_page_served_unlocked(client):
    resp = client.get("/words/reading-part-1-reading-correspondence")
    assert resp.status_code == 200
    html = resp.text
    assert "lucide-lock" not in html
    assert "blur-[5px]" not in html
    assert "blur-[4px]" not in html
    assert "This word unlocks with CELTESTPIP Pro" not in html
    assert 'locked\\":true' not in html

def test_swimming_lesson_practice_served_unlocked(client):
    resp = client.get("/practices/listening/cmn2ldtkn008b80un8zyrvxr9")
    assert resp.status_code == 200
    html = resp.text
    assert "This practice is for Pro Members Only" not in html
    assert "Upgrade to Pro" not in html
    assert "Pro only" not in html
    assert "Start" in html

def test_question_answer_api(client):
    resp = client.post("/api/question", json={"questionId": "cm2v39qoc003h10y3u8q9r9z2", "answer": "option2"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["ok"] is True
    assert data["questionId"] == "cm2v39qoc003h10y3u8q9r9z2"
    assert data["answer"] == "option2"

def test_questions_report_api(client):
    resp = client.post("/api/questions/report", json={"questionId": "cm2v39qoc003h10y3u8q9r9z2", "reason": "other"})
    assert resp.status_code == 200
    assert resp.json()["ok"] is True
