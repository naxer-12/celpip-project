import os
import pytest
from fastapi.testclient import TestClient
from celtestpip.server.app import app

@pytest.fixture
def client():
    return TestClient(app)

def test_practice_runner_js_exists_and_serves(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    assert "javascript" in resp.headers["content-type"]
    content = resp.text
    # Verify core audio player functions exist in bundle
    assert "mountAudioPlayer" in content
    assert "mountQuestionStep" in content
    assert "formatTime" in content

def test_question_step_features_in_runner(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    content = resp.text
    assert "startCountdown" in content
    assert "renderOptions" in content
    assert "Show Answer" in content

