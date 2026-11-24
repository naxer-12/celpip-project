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
            try {
              let raw = txt.slice(startIdx, endIdx);
              raw = raw.replace(/\\"/g, '"');
              const steps = JSON.parse(raw);
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
  };

  function initRunner() {
    const startBtns = [
      document.getElementById('startBtn'),
      document.getElementById('startTaskBtn'),
      document.getElementById('headerStartBtn')
    ].filter(Boolean);
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
