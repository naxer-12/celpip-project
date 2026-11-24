import json
import os
import shutil
import subprocess
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

def test_extract_practice_data_handles_flight_string_unescaping(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    content = resp.text
    # 1. Verify two-stage JSON parse logic is present in the runner code
    assert "unescaped = JSON.parse" in content
    assert "totalQ = step.totalQuestions" in content

    # 2. Verify via node execution that extractPracticeData parses Flight strings with internal quotes
    node_path = shutil.which("node")
    if node_path:
        test_script = r"""
        const fs = require('fs');
        const code = fs.readFileSync('celtestpip/static/js/celtestpip-runner.js', 'utf8');
        const flightPayload = String.raw`self.__next_f.push([1, "12:{\"steps\":[{\"type\":\"question\",\"questionNumber\":1,\"totalQuestions\":8,\"content\":{\"question\":\"What does \\\"CELPIP\\\" stand for?\",\"explanation\":\"Explanation mentions \\\"score\\\".\"}}]}"])`;

        const dom = {
          window: {},
          document: {
            readyState: 'complete',
            querySelectorAll: (sel) => sel === 'script' ? [{ textContent: flightPayload }] : [],
            getElementById: () => null,
            addEventListener: () => {}
          }
        };

        const fn = new Function('window', 'document', code);
        fn(dom.window, dom.document);
        const res = dom.window.CeltestpipRunner.extractPracticeData();
        console.log(JSON.stringify(res));
        """
        proc = subprocess.run([node_path, "-e", test_script], capture_output=True, text=True, check=True)
        data = json.loads(proc.stdout)
        assert data is not None
        assert len(data["steps"]) == 1
        q = data["steps"][0]["content"]["question"]
        assert 'What does "CELPIP" stand for?' == q
        exp = data["steps"][0]["content"]["explanation"]
        assert 'Explanation mentions "score".' == exp

def test_universal_start_button_selector_logic(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    content = resp.text
    # Verify universal text matching selector exists
    assert "findStartButtons" in content
    assert "startsWith('Start')" in content or "textContent.trim()" in content


