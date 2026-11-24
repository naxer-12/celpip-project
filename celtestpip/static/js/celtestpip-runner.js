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
        const matchIdx = txt.search(/steps\\*":\s*\[/);
        if (matchIdx !== -1) {
          const startIdx = txt.indexOf('[', matchIdx);
          let depth = 0;
          let endIdx = -1;
          for (let i = startIdx; i < txt.length; i++) {
            const c = txt[i];
            if (c === '[') depth++;
            else if (c === ']') {
              depth--;
              if (depth === 0) {
                endIdx = i + 1;
                break;
              }
            }
          }
          if (endIdx !== -1) {
            let raw = txt.slice(startIdx, endIdx);
            // 1. Two-stage JSON unescape for Flight-encoded strings with internal quotes
            try {
              const unescaped = JSON.parse(`"${raw.replace(/\n/g, '\\n').replace(/\r/g, '\\r')}"`);
              const steps = JSON.parse(unescaped);
              if (Array.isArray(steps) && steps.length > 0) {
                return { steps };
              }
            } catch (e) {}
            // 2. Fallback to basic quote replacement
            try {
              let cleaned = raw.replace(/\\"/g, '"');
              const steps = JSON.parse(cleaned);
              if (Array.isArray(steps) && steps.length > 0) {
                return { steps };
              }
            } catch (e) {}
          }
        }

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

  function renderOptions(options) {
    return options.map(opt => `
      <label class="option-card flex items-start gap-3 p-3.5 rounded-xl border border-zinc-200/80 hover:bg-zinc-50/80 cursor-pointer transition-all">
        <input type="radio" name="practiceOption" value="${opt.key}" class="mt-1 text-primary focus:ring-primary h-4 w-4">
        <div class="flex-1">
          <span class="font-semibold text-xs text-zinc-400 mr-1.5">[${opt.label}]</span>
          <span class="text-sm font-medium text-zinc-800">${opt.text}</span>
        </div>
      </label>
    `).join('');
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
          ${renderOptions(options)}
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

    const optionInputs = container.querySelectorAll('input[name="practiceOption"]');
    optionInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        if (onAnswer) onAnswer(e.target.value);
      });
    });

    const nextBtn = document.getElementById('nextQuestionBtn');
    nextBtn.onclick = () => {
      stopCountdown();
      if (qAudio) qAudio.pause();
      if (onNext) onNext();
    };
  }

  window.CeltestpipRunner = {
    formatTime,
    extractPracticeData,
    mountAudioPlayer,
    mountQuestionStep,
    startCountdown,
    renderOptions,
    findStartButtons,
    initWritingEditor,
    initSpeakingRecorder,
  };

  function initWritingEditor() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/writing_') && !window.location.pathname.includes('practices_writing_')) return;
    if (document.getElementById('writingPracticeWorkspace')) return;

    const container = document.getElementById('practicePlayerContainer') || document.querySelector('main') || document.body;
    const workspace = document.createElement('div');
    workspace.id = 'writingPracticeWorkspace';
    workspace.className = 'w-full max-w-4xl mx-auto mt-8 p-6 bg-white rounded-2xl border border-zinc-200 shadow-sm';
    workspace.innerHTML = `
      <div class="flex items-center justify-between pb-4 mb-4 border-b border-zinc-100">
        <div class="flex items-center gap-2">
          <span class="inline-flex size-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <h3 class="font-bold text-lg text-zinc-900">Your Response (Exam Simulation)</h3>
        </div>
        <div class="flex items-center gap-4 text-sm font-medium">
          <span id="writingWordCount" class="px-3 py-1 rounded-full bg-zinc-100 text-zinc-700 font-semibold">Word count: 0 / 150–200</span>
          <span id="writingTimer" class="px-3 py-1 rounded-full bg-blue-50 text-blue-700 font-bold tabular-nums">Time: 27:00</span>
        </div>
      </div>
      <div class="space-y-4">
        <textarea id="writingEditorTextarea" rows="12" class="w-full p-4 text-base border border-zinc-200 rounded-xl focus:ring-2 focus:ring-blue-600 focus:outline-none placeholder-zinc-400 font-sans leading-relaxed resize-y" placeholder="Type your response here. Word counter updates automatically as you type..."></textarea>
        <div class="flex flex-wrap items-center justify-between gap-3 pt-2">
          <button id="toggleSampleAnswerBtn" type="button" class="inline-flex items-center gap-2 px-4 py-2 text-sm font-semibold text-zinc-700 bg-zinc-100 hover:bg-zinc-200 rounded-xl transition-colors">
            <span>View Sample Answer (CLB 9+)</span>
          </button>
          <button id="saveWritingBtn" type="button" class="inline-flex items-center gap-2 px-5 py-2 text-sm font-bold text-white bg-primary blue-btn rounded-xl shadow-sm hover:opacity-95 transition-opacity">
            <span>Submit for Review</span>
          </button>
        </div>
        <div id="sampleAnswerAccordion" class="hidden mt-4 p-5 rounded-xl bg-blue-50/70 border border-blue-100 text-sm text-zinc-800 leading-relaxed">
          <h4 class="font-bold text-blue-900 mb-2">CLB 9+ High-Scoring Sample Response:</h4>
          <p class="whitespace-pre-line text-zinc-700">Dear Building Management,

I am writing to express my view regarding the proposed changes to the building delivery policy. As a resident who frequently receives parcels, I believe having deliveries brought directly to unit doors is far more convenient and secure for all tenants.

First and foremost, many residents work long hours or have mobility constraints, making trips down to the lobby for heavy packages burdensome. Direct door deliveries ensure that tenants can receive their essentials without unnecessary disruption. Furthermore, placing parcels inside apartment hallways significantly reduces the risk of accidental misplacement or theft that can happen in high-traffic common areas.

While I understand the security and clutter concerns regarding delivery personnel entering upper floors, these can easily be mitigated by implementing keycard visitor logs or designated delivery hours.

Thank you for considering my feedback on this matter.

Sincerely,
Resident</p>
        </div>
      </div>
    `;

    if (container.parentNode && container.id === 'practicePlayerContainer') {
      container.parentNode.insertBefore(workspace, container);
    } else {
      container.appendChild(workspace);
    }

    const textarea = workspace.querySelector('#writingEditorTextarea');
    const wordCountEl = workspace.querySelector('#writingWordCount');
    const toggleBtn = workspace.querySelector('#toggleSampleAnswerBtn');
    const sampleBox = workspace.querySelector('#sampleAnswerAccordion');
    const submitBtn = workspace.querySelector('#saveWritingBtn');

    if (textarea && wordCountEl) {
      textarea.addEventListener('input', () => {
        const text = textarea.value.trim();
        const words = text ? text.split(/\s+/).length : 0;
        wordCountEl.textContent = `Word count: ${words} / 150–200`;
        if (words >= 150 && words <= 200) {
          wordCountEl.className = 'px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 font-semibold';
        } else if (words > 200) {
          wordCountEl.className = 'px-3 py-1 rounded-full bg-amber-100 text-amber-800 font-semibold';
        } else {
          wordCountEl.className = 'px-3 py-1 rounded-full bg-zinc-100 text-zinc-700 font-semibold';
        }
      });
    }

    if (toggleBtn && sampleBox) {
      toggleBtn.addEventListener('click', () => {
        sampleBox.classList.toggle('hidden');
        toggleBtn.textContent = sampleBox.classList.contains('hidden') ? 'View Sample Answer (CLB 9+)' : 'Hide Sample Answer';
      });
    }

    if (submitBtn) {
      submitBtn.addEventListener('click', () => {
        submitBtn.textContent = 'Response Recorded ✓';
        submitBtn.classList.add('bg-emerald-600');
        if (sampleBox) sampleBox.classList.remove('hidden');
      });
    }
  }

  function initSpeakingRecorder() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/speaking_') && !window.location.pathname.includes('practices_speaking_')) return;
    if (document.getElementById('speakingPracticeWorkspace')) return;

    const container = document.getElementById('practicePlayerContainer') || document.querySelector('main') || document.body;
    const workspace = document.createElement('div');
    workspace.id = 'speakingPracticeWorkspace';
    workspace.className = 'w-full max-w-4xl mx-auto mt-8 p-6 bg-white rounded-2xl border border-zinc-200 shadow-sm';
    workspace.innerHTML = `
      <div class="flex items-center justify-between pb-4 mb-4 border-b border-zinc-100">
        <div class="flex items-center gap-2">
          <span class="inline-flex size-2 rounded-full bg-purple-500 animate-pulse"></span>
          <h3 class="font-bold text-lg text-zinc-900">Speaking Practice Simulation</h3>
        </div>
        <div id="speakingPhaseBadge" class="px-3 py-1 rounded-full bg-zinc-100 text-zinc-700 text-sm font-semibold">Ready to begin</div>
      </div>
      <div class="space-y-6 text-center py-4">
        <div class="flex flex-col items-center justify-center">
          <div id="speakingTimerDisplay" class="text-5xl font-black tabular-nums tracking-tight text-zinc-900">00:30</div>
          <p id="speakingStatusLabel" class="text-sm font-medium text-zinc-500 mt-2">Preparation Time: 30 seconds</p>
        </div>
        <div class="flex items-center justify-center gap-4">
          <button id="startSpeakingSessionBtn" type="button" class="inline-flex items-center gap-2 px-6 py-3 text-base font-bold text-white bg-primary blue-btn rounded-xl shadow-sm hover:opacity-95 transition-all">
            <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line></svg>
            <span>Start Practice</span>
          </button>
          <button id="toggleSampleSpeakingBtn" type="button" class="inline-flex items-center gap-2 px-5 py-3 text-sm font-semibold text-zinc-700 bg-zinc-100 hover:bg-zinc-200 rounded-xl transition-colors">
            <span>View Sample Response (CLB 9+)</span>
          </button>
        </div>
        <div id="sampleSpeakingAccordion" class="hidden text-left mt-6 p-5 rounded-xl bg-purple-50/70 border border-purple-100 text-sm text-zinc-800 leading-relaxed">
          <h4 class="font-bold text-purple-900 mb-2">CLB 9+ High-Scoring Spoken Response Transcript:</h4>
          <p class="whitespace-pre-line text-zinc-700">"Hi everyone. In looking at the two options for our upcoming trip, I strongly recommend we choose the Downtown Hotel with Underground Access over the Boutique Hotel in Old Montreal. 

First of all, Montreal winters can be exceptionally cold with severe snowstorms. Having direct access to the Underground City means we can easily reach transit, shopping, and dining without having to face freezing temperatures or slippery roads. 

Secondly, while the boutique hotel has historic charm, its location makes walking to modern attractions more challenging in bad weather. The downtown option is much more practical and stress-free for our group. For these reasons, I believe the downtown hotel is clearly the superior choice."</p>
        </div>
      </div>
    `;

    if (container.parentNode && container.id === 'practicePlayerContainer') {
      container.parentNode.insertBefore(workspace, container);
    } else {
      container.appendChild(workspace);
    }

    const startBtn = workspace.querySelector('#startSpeakingSessionBtn');
    const timerDisplay = workspace.querySelector('#speakingTimerDisplay');
    const statusLabel = workspace.querySelector('#speakingStatusLabel');
    const phaseBadge = workspace.querySelector('#speakingPhaseBadge');
    const toggleBtn = workspace.querySelector('#toggleSampleSpeakingBtn');
    const sampleBox = workspace.querySelector('#sampleSpeakingAccordion');

    if (toggleBtn && sampleBox) {
      toggleBtn.addEventListener('click', () => {
        sampleBox.classList.toggle('hidden');
        toggleBtn.textContent = sampleBox.classList.contains('hidden') ? 'View Sample Response (CLB 9+)' : 'Hide Sample Response';
      });
    }

    if (startBtn && timerDisplay && statusLabel && phaseBadge) {
      let interval = null;
      startBtn.addEventListener('click', () => {
        if (interval) clearInterval(interval);
        startBtn.style.display = 'none';

        // Phase 1: Preparation (30s)
        let prepSeconds = 30;
        phaseBadge.textContent = 'Preparation Phase';
        phaseBadge.className = 'px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-sm font-semibold';
        statusLabel.textContent = 'Preparation Time remaining — organise your thoughts';

        interval = setInterval(() => {
          prepSeconds--;
          timerDisplay.textContent = formatTime(prepSeconds);
          if (prepSeconds <= 0) {
            clearInterval(interval);
            // Phase 2: Recording / Speaking (60s)
            let speakSeconds = 60;
            phaseBadge.textContent = 'Speaking / Recording';
            phaseBadge.className = 'px-3 py-1 rounded-full bg-red-100 text-red-800 text-sm font-semibold animate-pulse';
            statusLabel.textContent = 'Speak clearly into your microphone now';

            interval = setInterval(() => {
              speakSeconds--;
              timerDisplay.textContent = formatTime(speakSeconds);
              if (speakSeconds <= 0) {
                clearInterval(interval);
                phaseBadge.textContent = 'Completed';
                phaseBadge.className = 'px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-sm font-semibold';
                statusLabel.textContent = 'Speaking practice finished! Review the sample response below.';
                if (sampleBox) sampleBox.classList.remove('hidden');
              }
            }, 1000);
          }
        }, 1000);
      });
    }
  }

  function findStartButtons() {
    const byId = [
      document.getElementById('startBtn'),
      document.getElementById('startTaskBtn'),
      document.getElementById('headerStartBtn')
    ].filter(Boolean);
    if (byId.length > 0) return byId;

    // Universal selector: Find any button whose visible text starts with "Start"
    const allButtons = Array.from(document.querySelectorAll('button'));
    const startButtons = allButtons.filter(btn => {
      const txt = (btn.textContent || '').trim();
      return txt.startsWith('Start') || txt === 'Start' || txt.includes('Start →');
    });
    return startButtons;
  }

  function initRunner() {
    initWritingEditor();
    initSpeakingRecorder();

    const startBtns = findStartButtons();
    const data = extractPracticeData();
    if (startBtns.length && data && data.steps) {
      startBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          // Hide instructions container
          const mainCard = btn.closest('.border') || btn.closest('div');
          if (mainCard) mainCard.style.display = 'none';

          const headerBtn = document.getElementById('headerStartBtn');
          if (headerBtn) headerBtn.style.display = 'none';

          let container = document.getElementById('practicePlayerContainer');
          if (!container) {
            container = document.createElement('div');
            container.id = 'practicePlayerContainer';
            if (mainCard && mainCard.parentNode) {
              mainCard.parentNode.insertBefore(container, mainCard.nextSibling);
            } else {
              document.body.appendChild(container);
            }
          } else if (mainCard && mainCard.contains(container)) {
            mainCard.parentNode.insertBefore(container, mainCard.nextSibling);
          }

          let currentStepIdx = 0;
          function runNext() {
            currentStepIdx++;
            if (currentStepIdx < data.steps.length) {
              const step = data.steps[currentStepIdx];
              if (step.type === 'audio') {
                mountAudioPlayer(step, runNext);
              } else if (step.type === 'question') {
                const totalQ = step.totalQuestions || data.steps.filter(s => s.type === 'question').length || (data.steps.length - 1);
                const qNum = step.questionNumber ? (step.questionNumber - 1) : currentStepIdx;
                mountQuestionStep(step, qNum, totalQ, null, runNext);
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
            currentStepIdx = data.steps.indexOf(audioStep);
            mountAudioPlayer(audioStep, runNext);
          } else {
            runNext();
          }
        });
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initRunner);
  } else {
    initRunner();
  }
})();
