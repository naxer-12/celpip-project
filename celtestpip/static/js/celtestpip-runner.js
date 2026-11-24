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
