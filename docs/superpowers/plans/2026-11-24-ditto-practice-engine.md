# Ditto Practice Engine & Site Alignment Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a native, robust client-side interactive practice engine (`celtestpip-runner.js`) that brings 100% feature and visual parity to all practice question sessions (conversation audio player, 30s timer, per-question audio clips, radio options, transcript accordion) and fixes header navigation and dual-button discrepancies.

**Architecture:** Inject a standalone, zero-dependency client script (`/static/js/celtestpip-runner.js`) and scoped CSS into `/practices/*` routes. The runner reads serialized practice data directly from the DOM/Flight payload, mounting an interactive audio player and question state machine that transitions seamlessly without depending on upstream Next.js edge hydration.

**Tech Stack:** JavaScript (Vanilla ES6+ DOM & Web Audio API), Tailwind CSS utility classes, Python (FastAPI routers, pytest), Jinja2 / pre-rendered HTML.

**Spec:** [atomic_site_fidelity_audit.md](file:///Users/jainamshah/.gemini/antigravity/brain/c3bbce33-a7e0-4675-8a35-265a419aa08d/atomic_site_fidelity_audit.md)

## Global Constraints

- Zero external third-party dependencies: No Clerk, Vercel, or external CDN network calls.
- Pure client compatibility: Works smoothly across modern Chromium, Safari, and Firefox browsers.
- No hydration regressions: Do not modify core React Flight script tag serialization in a way that throws `TypeError: n.reason.enqueueModel is not a function`.
- All automated tests in `celtestpip/tests/` must remain 100% green at every commit.

---

### Task 1: Desktop/Mobile Responsive CSS Cleanup for Practice Header

**Files:**
- Modify: `celtestpip/static/css/style.css:1-20`
- Modify: `celtestpip/scripts/unlock_all_pro_content.py:120-135`
- Test: `celtestpip/tests/test_unlocked_pro_content.py`

**Interfaces:**
- Consumes: `#headerStartBtn`, `#startBtn` elements in practice HTML.
- Produces: CSS media query rule hiding `#headerStartBtn` on viewports `>= 1024px` (`lg`).

- [ ] **Step 1: Write the failing test**

In `celtestpip/tests/test_unlocked_pro_content.py`, add `test_responsive_header_start_button_styling`:

```python
def test_responsive_header_start_button_styling(client):
    resp = client.get("/practices/listening_cmn4hda7y00pyyqundlh38n09")
    assert resp.status_code == 200
    html = resp.text
    # Verify responsive rule exists hiding #headerStartBtn on desktop
    assert "@media (min-width: 1024px)" in html or "@media (min-width:1024px)" in html or "lg:hidden" in html
    assert "#headerStartBtn" in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_unlocked_pro_content.py::test_responsive_header_start_button_styling -v`
Expected: FAIL (assertion error regarding responsive media query or lg:hidden on `#headerStartBtn`).

- [ ] **Step 3: Write minimal implementation**

In `celtestpip/scripts/unlock_all_pro_content.py`, in `clean_html()`, inject the responsive CSS rule into the head or `#headerStartBtn`:

```python
    # 12. Fix duplicate Start button by ensuring #headerStartBtn is hidden on desktop (lg:hidden)
    if 'id="headerStartBtn"' in html:
        html = html.replace('id="headerStartBtn" class="', 'id="headerStartBtn" class="lg:hidden ')
    if '<style id="replica-unlock-style">' in html:
        html = html.replace(
            '<style id="replica-unlock-style">',
            '<style id="replica-unlock-style">\n    @media (min-width: 1024px) { #headerStartBtn { display: none !important; } }'
        )
```

And in `celtestpip/static/css/style.css`:
```css
@media (min-width: 1024px) {
  #headerStartBtn {
    display: none !important;
  }
}
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_unlocked_pro_content.py::test_responsive_header_start_button_styling -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add celtestpip/scripts/unlock_all_pro_content.py celtestpip/static/css/style.css celtestpip/tests/test_unlocked_pro_content.py
git commit -m "fix(styles): hide duplicate mobile #headerStartBtn on desktop viewports"
```

---

### Task 2: Desktop Header Navigation Alignment

**Files:**
- Modify: `celtestpip/scripts/unlock_all_pro_content.py`
- Modify: `celtestpip/server/routers/pages.py`
- Test: `celtestpip/tests/test_frontend_shell.py`

**Interfaces:**
- Consumes: Header navigation links in `/` and `/practices/*`.
- Produces: `Score Calculator` and `Pricing` navigation anchors pointing to `/calculator` and `/exams`.

- [ ] **Step 1: Write the failing test**

In `celtestpip/tests/test_frontend_shell.py`, add `test_header_navigation_has_calculator_and_pricing`:

```python
def test_header_navigation_has_calculator_and_pricing(client):
    resp = client.get("/")
    assert resp.status_code == 200
    html = resp.text
    assert "/calculator" in html
    assert "Score Calculator" in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_frontend_shell.py::test_header_navigation_has_calculator_and_pricing -v`
Expected: FAIL (assertion error: "Score Calculator" not found in homepage).

- [ ] **Step 3: Write minimal implementation**

In `celtestpip/server/routers/pages.py` (and `celtestpip/static/index.html`), ensure the navbar includes the `Score Calculator` and `Pricing` links:

```html
<a href="/calculator" class="text-sm font-medium text-zinc-600 hover:text-zinc-900 transition-colors">Score Calculator</a>
<a href="/exams" class="text-sm font-medium text-zinc-600 hover:text-zinc-900 transition-colors">Pricing</a>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_frontend_shell.py::test_header_navigation_has_calculator_and_pricing -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add celtestpip/server/routers/pages.py celtestpip/static/index.html celtestpip/tests/test_frontend_shell.py
git commit -m "feat(nav): add Score Calculator and Pricing links to desktop navigation"
```

---

### Task 3: Native Practice Player Engine - Conversation Audio Step (`celtestpip-runner.js`)

**Files:**
- Create: `celtestpip/static/js/celtestpip-runner.js`
- Test: `celtestpip/tests/test_practice_runner.py`

**Interfaces:**
- Consumes: Window DOM (`#startBtn`, `#headerStartBtn`, Flight payload `steps`).
- Produces: `mountAudioPlayer(step, onNext)` with play/pause, seek slider, 10s skip buttons, speed selector, transcript accordion.

- [ ] **Step 1: Write the failing test**

Create `celtestpip/tests/test_practice_runner.py`:

```python
import os

def test_practice_runner_js_exists_and_serves(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    assert "application/javascript" in resp.headers["content-type"]
    content = resp.text
    # Verify core audio player functions exist in bundle
    assert "mountAudioPlayer" in content
    assert "mountQuestionStep" in content
    assert "formatTime" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_practice_runner.py -v`
Expected: FAIL (404 Not Found or file does not exist).

- [ ] **Step 3: Write minimal implementation**

Create `celtestpip/static/js/celtestpip-runner.js`:

```javascript
/**
 * CELTESTPIP Native Ditto Practice Runner
 * Powers interactive listening practice sessions with zero external dependencies.
 */
(function() {
  'use strict';

  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '00:00';
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function extractPracticeData() {
    // 1. Try window.__PRACTICE_DATA__
    if (window.__PRACTICE_DATA__) return window.__PRACTICE_DATA__;

    // 2. Extract from Next.js Flight scripts (self.__next_f.push)
    const scripts = document.querySelectorAll('script');
    for (const s of scripts) {
      const txt = s.textContent || '';
      if (txt.includes('steps')) {
        const match = txt.match(/steps\\*":\s*(\[[^\]]+\])/);
        if (match) {
          try {
            const raw = match[1].replace(/\\"/g, '"');
            const steps = JSON.parse(raw);
            return { steps };
          } catch (e) {}
        }
      }
    }
    return null;
  }

  function mountAudioPlayer(step, onNext) {
    const container = document.getElementById('practicePlayerContainer');
    if (!container) return;

    container.innerHTML = `
      <div class="bg-white rounded-2xl border border-zinc-200/80 shadow-sm p-6 sm:p-8 max-w-3xl mx-auto animate-in fade-in-50 duration-300">
        <div class="flex items-center justify-between border-b border-zinc-100 pb-4 mb-6">
          <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200/60">
            <svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 18v-6a9 9 0 0 1 18 0v6"></path><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path></svg>
            Listening Passage
          </span>
          <button id="runnerNextTopBtn" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-semibold text-white bg-primary hover:bg-blue-600 transition-colors shadow-sm">
            Next Questions →
          </button>
        </div>

        <div class="text-center my-6">
          <h2 class="text-xl sm:text-2xl font-bold text-zinc-900 mb-2">Listen to the Conversation</h2>
          <p class="text-sm text-zinc-500">Listen carefully. You will answer questions about this conversation on the next screen.</p>
        </div>

        <!-- Custom Audio Player Bar -->
        <div class="bg-zinc-50 rounded-2xl p-4 sm:p-6 border border-zinc-200/60 mb-6">
          <audio id="runnerAudio" src="${step.audio}" preload="auto"></audio>
          <div class="flex items-center justify-center gap-4 mb-4">
            <button id="skipBackBtn" class="p-2 text-zinc-600 hover:text-zinc-900 rounded-lg hover:bg-zinc-200/60 transition" title="Back 10s">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 17l-5-5 5-5M18 17l-5-5 5-5"/></svg>
            </button>
            <button id="playPauseBtn" class="w-14 h-14 rounded-full bg-primary text-white flex items-center justify-center shadow-md hover:scale-105 active:scale-95 transition">
              <svg id="playIcon" class="w-6 h-6 ml-0.5" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
              <svg id="pauseIcon" class="w-6 h-6 hidden" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
            </button>
            <button id="skipFwdBtn" class="p-2 text-zinc-600 hover:text-zinc-900 rounded-lg hover:bg-zinc-200/60 transition" title="Forward 10s">
              <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 17l5-5-5-5M6 17l5-5-5-5"/></svg>
            </button>
          </div>

          <div class="flex items-center gap-3 text-xs font-mono text-zinc-500">
            <span id="currentTime">00:00</span>
            <input id="seekBar" type="range" min="0" max="100" value="0" class="flex-1 h-2 bg-zinc-200 rounded-lg appearance-none cursor-pointer accent-primary">
            <span id="totalDuration">00:00</span>
            <select id="speedSelect" class="bg-white border border-zinc-200 rounded px-1.5 py-0.5 text-xs font-sans text-zinc-700">
              <option value="0.75">0.75x</option>
              <option value="1" selected>1.0x</option>
              <option value="1.25">1.25x</option>
              <option value="1.5">1.5x</option>
            </select>
          </div>
        </div>

        <!-- Transcript Accordion -->
        ${step.transcript ? `
        <details class="group border border-zinc-200/70 rounded-xl mb-6 overflow-hidden">
          <summary class="flex items-center justify-between px-4 py-3 bg-zinc-50 cursor-pointer font-medium text-sm text-zinc-700 select-none">
            <span>Show Conversation Transcript</span>
            <svg class="w-4 h-4 transition-transform group-open:rotate-180 text-zinc-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
          </summary>
          <div class="p-4 text-sm text-zinc-600 leading-relaxed bg-white border-t border-zinc-200/70 max-h-60 overflow-y-auto whitespace-pre-line">
            ${step.transcript}
          </div>
        </details>
        ` : ''}

        <div class="flex items-center justify-end gap-3 pt-4 border-t border-zinc-100">
          <button id="runnerNextBottomBtn" class="px-6 py-2.5 rounded-xl text-sm font-semibold text-white bg-primary hover:bg-blue-600 shadow transition-colors">
            Next Questions →
          </button>
        </div>
      </div>
    `;

    const audio = document.getElementById('runnerAudio');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const playIcon = document.getElementById('playIcon');
    const pauseIcon = document.getElementById('pauseIcon');
    const seekBar = document.getElementById('seekBar');
    const curTime = document.getElementById('currentTime');
    const durTime = document.getElementById('totalDuration');
    const speedSelect = document.getElementById('speedSelect');
    const skipBackBtn = document.getElementById('skipBackBtn');
    const skipFwdBtn = document.getElementById('skipFwdBtn');

    playPauseBtn.onclick = () => {
      if (audio.paused) {
        audio.play();
        playIcon.classList.add('hidden');
        pauseIcon.classList.remove('hidden');
      } else {
        audio.pause();
        playIcon.classList.remove('hidden');
        pauseIcon.classList.add('hidden');
      }
    };

    audio.ontimeupdate = () => {
      if (audio.duration) {
        seekBar.value = (audio.currentTime / audio.duration) * 100;
        curTime.textContent = formatTime(audio.currentTime);
      }
    };

    audio.onloadedmetadata = () => {
      durTime.textContent = formatTime(audio.duration);
    };

    audio.onended = () => {
      playIcon.classList.remove('hidden');
      pauseIcon.classList.add('hidden');
    };

    seekBar.oninput = () => {
      if (audio.duration) {
        audio.currentTime = (seekBar.value / 100) * audio.duration;
      }
    };

    skipBackBtn.onclick = () => { audio.currentTime = Math.max(0, audio.currentTime - 10); };
    skipFwdBtn.onclick = () => { audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 10); };
    speedSelect.onchange = () => { audio.playbackRate = parseFloat(speedSelect.value); };

    const handleNext = () => {
      if (audio) audio.pause();
      if (onNext) onNext();
    };

    const nextTop = document.getElementById('runnerNextTopBtn');
    const nextBottom = document.getElementById('runnerNextBottomBtn');
    if (nextTop) nextTop.onclick = handleNext;
    if (nextBottom) nextBottom.onclick = handleNext;

    // Auto-play audio safely
    audio.play().catch(() => {});
  }

  function mountQuestionStep(step, qIndex, totalQuestions, onAnswer, onNext) {
    // Defined in Task 4
  }

  window.CeltestpipRunner = {
    formatTime,
    extractPracticeData,
    mountAudioPlayer,
    mountQuestionStep,
  };
})();
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_practice_runner.py -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add celtestpip/static/js/celtestpip-runner.js celtestpip/tests/test_practice_runner.py
git commit -m "feat(runner): implement conversation audio player step in celtestpip-runner.js"
```

---

### Task 4: Practice Player Client Engine - 30-Second Countdown & Question Flow

**Files:**
- Modify: `celtestpip/static/js/celtestpip-runner.js`
- Test: `celtestpip/tests/test_practice_runner.py`

**Interfaces:**
- Consumes: Question step object with options (`option1`..`option4`), question audio, explanation.
- Produces: `mountQuestionStep` with 30s countdown bar, radio selectors, `Show Answer`, and `Next ->`.

- [ ] **Step 1: Write the failing test**

In `celtestpip/tests/test_practice_runner.py`, add `test_question_step_features_in_runner`:

```python
def test_question_step_features_in_runner(client):
    resp = client.get("/static/js/celtestpip-runner.js")
    assert resp.status_code == 200
    content = resp.text
    assert "startCountdown" in content
    assert "renderOptions" in content
    assert "Show Answer" in content
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_practice_runner.py::test_question_step_features_in_runner -v`
Expected: FAIL.

- [ ] **Step 3: Write minimal implementation**

In `celtestpip/static/js/celtestpip-runner.js`, complete `mountQuestionStep` and `startCountdown`:

```javascript
  function startCountdown(seconds, onTick, onExpire) {
    let remain = seconds;
    const interval = setInterval(() => {
      remain--;
      if (onTick) onTick(remain);
      if (remain <= 0) {
        clearInterval(interval);
        if (onExpire) onExpire();
      }
    }, 1000);
    return () => clearInterval(interval);
  }

  function mountQuestionStep(step, qIndex, totalQuestions, onAnswer, onNext) {
    const container = document.getElementById('practicePlayerContainer');
    if (!container) return;

    const content = step.content || step;
    const options = [
      { key: 'option1', label: 'A', text: content.option1 },
      { key: 'option2', label: 'B', text: content.option2 },
      { key: 'option3', label: 'C', text: content.option3 },
      { key: 'option4', label: 'D', text: content.option4 },
    ].filter(o => Boolean(o.text));

    container.innerHTML = `
      <div class="bg-white rounded-2xl border border-zinc-200/80 shadow-sm p-6 sm:p-8 max-w-3xl mx-auto animate-in fade-in-50 duration-300">
        <!-- Tracker & 30s Countdown -->
        <div class="flex items-center justify-between border-b border-zinc-100 pb-3 mb-4">
          <span class="text-xs font-semibold uppercase tracking-wider text-zinc-500">
            Question ${qIndex + 1} of ${totalQuestions}
          </span>
          <div class="flex items-center gap-2">
            <span class="text-xs text-zinc-500 font-mono">Time Remaining:</span>
            <span id="timerCount" class="text-xs font-bold font-mono px-2 py-0.5 rounded bg-zinc-100 text-zinc-800">30s</span>
          </div>
        </div>

        <!-- Progress Bar -->
        <div class="w-full bg-zinc-100 h-1.5 rounded-full overflow-hidden mb-6">
          <div id="timerBar" class="bg-primary h-full transition-all duration-1000 ease-linear" style="width: 100%;"></div>
        </div>

        ${content.audio ? `
        <!-- Question Audio Player -->
        <div class="flex items-center gap-3 bg-zinc-50 p-3 rounded-xl border border-zinc-200/60 mb-6">
          <audio id="qAudio" src="${content.audio}" preload="auto"></audio>
          <button id="qPlayBtn" class="w-9 h-9 rounded-full bg-primary text-white flex items-center justify-center shrink-0">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          </button>
          <span class="text-xs text-zinc-600 font-medium">Listen to Question</span>
        </div>
        ` : ''}

        <h3 class="text-lg font-bold text-zinc-900 mb-6">${content.question || 'Select the best answer:'}</h3>

        <!-- Options (A, B, C, D) -->
        <div class="space-y-3 mb-6" id="optionsContainer">
          ${options.map(opt => `
            <label class="option-card flex items-start gap-3 p-3.5 rounded-xl border border-zinc-200/80 hover:bg-zinc-50/80 cursor-pointer transition-all">
              <input type="radio" name="practiceOption" value="${opt.key}" class="mt-1 text-primary focus:ring-primary h-4 w-4">
              <div class="flex-1">
                <span class="font-semibold text-xs text-zinc-400 mr-1.5">[${opt.label}]</span>
                <span class="text-sm font-medium text-zinc-800">${opt.text}</span>
              </div>
            </label>
          `).join('')}
        </div>

        <!-- Feedback & Explanation Box (Hidden initially) -->
        <div id="explanationBox" class="hidden p-4 rounded-xl bg-blue-50/70 border border-blue-200/60 mb-6 text-sm text-zinc-700 whitespace-pre-line leading-relaxed"></div>

        <!-- Controls -->
        <div class="flex items-center justify-between pt-4 border-t border-zinc-100">
          <button id="showAnswerBtn" class="px-4 py-2 text-xs font-semibold text-zinc-700 bg-zinc-100 hover:bg-zinc-200/80 rounded-xl transition">
            Show Answer
          </button>
          <button id="nextQuestionBtn" class="px-6 py-2.5 text-sm font-semibold text-white bg-primary hover:bg-blue-600 rounded-xl transition shadow">
            Next →
          </button>
        </div>
      </div>
    `;

    const timerCount = document.getElementById('timerCount');
    const timerBar = document.getElementById('timerBar');
    const stopCountdown = startCountdown(30, (remain) => {
      timerCount.textContent = `${remain}s`;
      timerBar.style.width = `${(remain / 30) * 100}%`;
    }, () => {
      // Time expired
    });

    const qAudio = document.getElementById('qAudio');
    const qPlayBtn = document.getElementById('qPlayBtn');
    if (qAudio && qPlayBtn) {
      qPlayBtn.onclick = () => {
        if (qAudio.paused) qAudio.play();
        else qAudio.pause();
      };
      qAudio.play().catch(() => {});
    }

    const showAnswerBtn = document.getElementById('showAnswerBtn');
    const explanationBox = document.getElementById('explanationBox');
    showAnswerBtn.onclick = () => {
      if (content.explanation) {
        explanationBox.textContent = content.explanation;
        explanationBox.classList.remove('hidden');
      }
    };

    const nextBtn = document.getElementById('nextQuestionBtn');
    nextBtn.onclick = () => {
      stopCountdown();
      if (qAudio) qAudio.pause();
      if (onNext) onNext();
    };
  }
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_practice_runner.py::test_question_step_features_in_runner -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add celtestpip/static/js/celtestpip-runner.js celtestpip/tests/test_practice_runner.py
git commit -m "feat(runner): implement 30s countdown timer and question step UI in celtestpip-runner.js"
```

---

### Task 5: Server Template Injection of `celtestpip-runner.js`

**Files:**
- Modify: `celtestpip/scripts/unlock_all_pro_content.py`
- Modify: `celtestpip/server/routers/pages.py`
- Test: `celtestpip/tests/test_unlocked_pro_content.py`

**Interfaces:**
- Consumes: Pre-rendered HTML for `/practices/*`.
- Produces: Injected `#practicePlayerContainer`, `celtestpip-runner.js`, and click hook connecting `#startBtn`.

- [ ] **Step 1: Write the failing test**

In `celtestpip/tests/test_unlocked_pro_content.py`, add `test_practice_page_has_runner_script`:

```python
def test_practice_page_has_runner_script(client):
    resp = client.get("/practices/listening_cmn4hda7y00pyyqundlh38n09")
    assert resp.status_code == 200
    html = resp.text
    assert "/static/js/celtestpip-runner.js" in html
    assert "practicePlayerContainer" in html
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest celtestpip/tests/test_unlocked_pro_content.py::test_practice_page_has_runner_script -v`
Expected: FAIL.

- [ ] **Step 3: Write minimal implementation**

In `celtestpip/scripts/unlock_all_pro_content.py`, inject `<div id="practicePlayerContainer"></div>` and the runner script in `clean_html()` when processing practice pages:

```python
    # 13. Inject practice runner script and player container
    if '/practices/' in html or 'practicePlayerContainer' not in html:
        runner_tag = '<script src="/static/js/celtestpip-runner.js" defer></script>'
        if runner_tag not in html:
            html = html.replace('</body>', f'{runner_tag}</body>')
```

And in `celtestpip/static/js/celtestpip-runner.js`, add initialization hook:
```javascript
  document.addEventListener('DOMContentLoaded', () => {
    const startBtns = [document.getElementById('startBtn'), document.getElementById('headerStartBtn')].filter(Boolean);
    const data = extractPracticeData();
    if (startBtns.length && data && data.steps) {
      startBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          // Hide instructions container
          const mainCard = btn.closest('.border') || btn.closest('div');
          if (mainCard) mainCard.style.display = 'none';

          let currentStepIdx = 0;
          function runNext() {
            currentStepIdx++;
            if (currentStepIdx < data.steps.length) {
              const step = data.steps[currentStepIdx];
              if (step.type === 'audio') {
                mountAudioPlayer(step, runNext);
              } else if (step.type === 'question') {
                mountQuestionStep(step, currentStepIdx, data.steps.length - 1, null, runNext);
              } else {
                runNext();
              }
            } else {
              window.location.reload();
            }
          }
          // Start with first non-task step or audio step
          const audioStep = data.steps.find(s => s.type === 'audio') || data.steps[1];
          if (audioStep) {
            mountAudioPlayer(audioStep, runNext);
          }
        });
      });
    }
  });
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest celtestpip/tests/test_unlocked_pro_content.py::test_practice_page_has_runner_script -v`
Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add celtestpip/scripts/unlock_all_pro_content.py celtestpip/static/js/celtestpip-runner.js celtestpip/tests/test_unlocked_pro_content.py
git commit -m "feat(runner): inject celtestpip-runner.js and player container into practice pages"
```

---

### Task 6: End-to-End Browser Verification & Render Production Deployment

**Files:**
- Test: All automated tests (`pytest celtestpip/tests/ -v`)
- Evidence: Browser subagent screenshots of live interaction on `localhost:8000` and `onrender.com`

- [ ] **Step 1: Run full automated test suite**

Run: `pytest celtestpip/tests/ -v`
Expected: 100% green (all tests passing).

- [ ] **Step 2: Start local daemon & verify in browser**

Run uvicorn daemon: `python3 -m uvicorn celtestpip.server.app:app --host 127.0.0.1 --port 8000`
Use browser subagent to:
1. Navigate to `http://localhost:8000/practices/listening_cmn4hda7y00pyyqundlh38n09`.
2. Click "Start".
3. Verify Conversation Audio Player mounts with controls and transcript accordion.
4. Click "Next Questions →".
5. Verify Question 1 displays with 30s countdown bar and radio options.
6. Take screenshots.

- [ ] **Step 3: Push to origin/main and deploy to Render**

```bash
git push origin main
```

- [ ] **Step 4: Verify production deployment on Render**

Navigate browser subagent to `https://celpip-project.onrender.com/practices/listening_cmn4hda7y00pyyqundlh38n09`.
Confirm identical interactive flow, audio playback, 30s countdown, and question navigation.
