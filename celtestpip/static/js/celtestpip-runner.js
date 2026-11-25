/**
 * CELTESTPIP Native Ditto Practice Runner
 * Powers 1:1 interactive Listening, Reading, Writing, Speaking,
 * Part-page topic filters/tabs, and 7-section Score Report modals.
 */
(function () {
  'use strict';

  function formatTime(seconds) {
    if (isNaN(seconds) || seconds < 0) return '00:00';
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  }

  function extractFlightJson(keyName, openChar, closeChar) {
    const scripts = document.querySelectorAll('script');
    const pat = new RegExp(`${keyName}\\\\*"\\s*:\\s*\\${openChar}`);
    for (const s of scripts) {
      const txt = s.textContent || '';
      if (!txt.includes(keyName)) continue;
      let searchFrom = 0;
      while (searchFrom < txt.length) {
        const sub = txt.slice(searchFrom);
        const matchIdx = sub.search(pat);
        if (matchIdx === -1) break;
        const startIdx = txt.indexOf(openChar, searchFrom + matchIdx);
        let depth = 0;
        let endIdx = -1;
        let inStr = false;
        let esc = false;
        for (let i = startIdx; i < txt.length; i++) {
          const c = txt[i];
          if (esc) { esc = false; continue; }
          if (c === '\\') { esc = true; continue; }
          if (c === '"') {
            inStr = !inStr;
          } else if (!inStr) {
            if (c === openChar) depth++;
            else if (c === closeChar) {
              depth--;
              if (depth === 0) {
                endIdx = i + 1;
                break;
              }
            }
          }
        }
        if (endIdx !== -1) {
          const raw = txt.slice(startIdx, endIdx);
          try {
            const unescaped = JSON.parse(`"${raw.replace(/\n/g, '\\n').replace(/\r/g, '\\r')}"`);
            return JSON.parse(unescaped);
          } catch (e) {}
          try {
            const cleaned = raw
              .replace(/\\"/g, '"')
              .replace(/\\\\n/g, '\\n')
              .replace(/\\n/g, '\\n');
            return JSON.parse(cleaned);
          } catch (e2) {}
        }
        searchFrom = searchFrom + matchIdx + keyName.length + 1;
      }
    }
    return null;
  }

  function resolveFlightRef(val) {
    if (typeof val !== 'string' || !/^\$[0-9a-zA-Z]+$/.test(val.trim())) return val;
    const refId = val.trim().slice(1);
    const scripts = document.querySelectorAll('script');
    const tPat = new RegExp(`(?:^|\\\\n|[^0-9a-zA-Z])${refId}:T([0-9a-fA-F]+),`);
    for (const s of scripts) {
      const txt = s.textContent || '';
      if (!txt.includes(`${refId}:`)) continue;
      const m = tPat.exec(txt);
      if (m) {
        const start = m.index + m[0].length;
        const rest = txt.slice(start);
        const endMatch = rest.match(/(?:"\]\)|[0-9a-fA-F]+:(?:T[0-9a-fA-F]+,|\[|\{|"))/);
        const rawChunk = endMatch ? rest.slice(0, endMatch.index) : rest;
        try {
          return JSON.parse(`"${rawChunk.replace(/\n/g, '\\n').replace(/\r/g, '\\r')}"`);
        } catch (e) {
          return rawChunk.replace(/\\n/g, '\n').replace(/\\r/g, '').replace(/\\"/g, '"');
        }
      }
      const qPat = new RegExp(`(?:^|\\\\n|[^0-9a-zA-Z])${refId}:"((?:[^"\\\\]|\\\\.)*)"`);
      const m2 = txt.match(qPat);
      if (m2 && m2[1]) {
        try {
          return JSON.parse(`"${m2[1]}"`);
        } catch (e) {
          return m2[1].replace(/\\n/g, '\n').replace(/\\"/g, '"');
        }
      }
    }
    return val;
  }

  function extractPracticeData() {
    if (window.__PRACTICE_DATA__) return window.__PRACTICE_DATA__;

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
            const raw = txt.slice(startIdx, endIdx);
            try {
              const unescaped = JSON.parse(`"${raw.replace(/\n/g, '\\n').replace(/\r/g, '\\r')}"`);
              const steps = JSON.parse(unescaped);
              if (Array.isArray(steps) && steps.length > 0) return { steps };
            } catch (e) {}
            try {
              const jsonStr = raw.replace(/\\"/g, '"').replace(/\\\\n/g, '\\n').replace(/\\n/g, '\\n');
              const steps = JSON.parse(jsonStr);
              if (Array.isArray(steps) && steps.length > 0) return { steps };
            } catch (e) {}
          }
        }
      }
    }
    return null;
  }

  // --- Shared Modal Helper (Answer Key & 7-Section Example/Score Report) ---
  function openModal(title, bodyHtml, maxW = 'max-w-3xl') {
    const existing = document.getElementById('celtestpipReplicaModal');
    if (existing) existing.remove();

    const overlay = document.createElement('div');
    overlay.id = 'celtestpipReplicaModal';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', title);
    overlay.className = 'fixed inset-0 z-[10000] bg-black/45';
    overlay.style.cssText = 'position:fixed;inset:0;z-index:10000;display:flex;align-items:flex-start;justify-content:center;padding:80px 16px 16px;background:rgba(0,0,0,0.45);';
    overlay.innerHTML = `
      <div class="w-full ${maxW} bg-white rounded-2xl shadow-2xl border border-zinc-200" style="max-height:82vh;display:flex;flex-direction:column;overflow:hidden;">
        <div class="flex items-center justify-between px-6 py-4 border-b border-zinc-100" style="flex-shrink:0;">
          <h3 class="text-lg font-bold text-zinc-900">${title}</h3>
          <button id="closeReplicaModalBtn" type="button" class="px-3 py-1.5 rounded-lg text-sm font-semibold text-zinc-600 hover:bg-zinc-100">Close</button>
        </div>
        <div class="p-6" style="overflow-y:auto;flex:1;">${bodyHtml}</div>
      </div>
    `;
    document.body.appendChild(overlay);
    overlay.querySelector('#closeReplicaModalBtn').addEventListener('click', () => overlay.remove());
    overlay.addEventListener('click', (e) => { if (e.target === overlay) overlay.remove(); });
  }

  function mountAudioPlayer(step, onNext) {
    const container = document.getElementById('practicePlayerContainer');
    if (!container) return;

    const audioUrl = step.audio || (step.content && step.content.audio) || '';
    const transcript = (step.content && step.content.transcript) || step.transcript || '';

    container.innerHTML = `
      <div class="w-full max-w-3xl mx-auto p-6 bg-white rounded-2xl border border-zinc-200 shadow-sm my-4">
        <div class="flex items-center justify-between mb-5">
          <div class="flex items-center gap-2.5 text-sm font-bold text-[#1a578a]">
            <svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg>
            <span>Listen to the conversation.</span>
          </div>
          <div class="flex items-center gap-2">
            <button type="button" class="listening-answers-key-btn px-3 py-1 rounded-lg border border-zinc-200 bg-white hover:bg-zinc-50 text-xs font-semibold text-zinc-700">Answers key</button>
            <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">Listening Passage</span>
          </div>
        </div>

        <audio id="practiceAudio" preload="auto" src="${audioUrl}"></audio>

        <div class="bg-zinc-50 border border-zinc-200 rounded-2xl p-5 mb-5">
          <div class="flex items-center gap-4">
            <button id="audioPlayPause" type="button" class="flex items-center justify-center w-12 h-12 rounded-full bg-blue-600 hover:bg-blue-700 text-white shadow-md transition-transform active:scale-95 shrink-0">
              <svg id="playIcon" class="w-5 h-5 ml-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg id="pauseIcon" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <button id="audioSkipBack" type="button" class="p-2 text-zinc-600 hover:text-zinc-900 hover:bg-zinc-200/60 rounded-lg transition-colors" title="Back 10s">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><text x="9" y="15" font-size="7" font-weight="bold" fill="currentColor" stroke="none">10</text></svg>
            </button>
            <div class="flex-1 flex flex-col gap-1">
              <input id="audioSeek" type="range" min="0" max="100" value="0" class="w-full accent-blue-600 h-1.5 bg-zinc-200 rounded-lg cursor-pointer" />
              <div class="flex justify-between text-xs font-medium text-zinc-500 tabular-nums">
                <span id="audioCurrent">00:00</span>
                <span id="audioDuration">00:00</span>
              </div>
            </div>
            <button id="audioSkipFwd" type="button" class="p-2 text-zinc-600 hover:text-zinc-900 hover:bg-zinc-200/60 rounded-lg transition-colors" title="Forward 10s">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><text x="9" y="15" font-size="7" font-weight="bold" fill="currentColor" stroke="none">10</text></svg>
            </button>
            <select id="audioSpeed" class="text-xs font-semibold bg-white border border-zinc-300 rounded-lg px-2 py-1.5 text-zinc-700 cursor-pointer">
              <option value="0.75">0.75x</option>
              <option value="1" selected>1x</option>
              <option value="1.25">1.25x</option>
              <option value="1.5">1.5x</option>
            </select>
          </div>
        </div>

        ${transcript ? `
          <div class="mb-5 border border-zinc-200 rounded-xl p-3 bg-white">
            <button id="toggleTranscript" type="button" class="flex w-full items-center justify-between text-sm font-bold text-zinc-800">
              <span>Transcript</span>
              <svg class="w-4 h-4 text-zinc-500" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>
            </button>
            <div id="transcriptBox" class="hidden mt-3 pt-3 border-t border-zinc-100 text-sm text-zinc-700 leading-relaxed whitespace-pre-line max-h-60 overflow-y-auto">${transcript}</div>
          </div>
        ` : ''}

        <p class="text-xs text-zinc-500 mb-4">In the official test, you can't rewind or replay the audio, and there's no transcript.</p>

        <div class="flex justify-end">
          <button id="audioNextBtn" type="button" class="inline-flex items-center justify-center px-6 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm shadow-sm transition-colors">
            Next →
          </button>
        </div>
      </div>
    `;

    const audio = container.querySelector('#practiceAudio');
    const playPause = container.querySelector('#audioPlayPause');
    const playIcon = container.querySelector('#playIcon');
    const pauseIcon = container.querySelector('#pauseIcon');
    const seek = container.querySelector('#audioSeek');
    const currentEl = container.querySelector('#audioCurrent');
    const durationEl = container.querySelector('#audioDuration');
    const speedEl = container.querySelector('#audioSpeed');
    const skipBack = container.querySelector('#audioSkipBack');
    const skipFwd = container.querySelector('#audioSkipFwd');
    const nextBtn = container.querySelector('#audioNextBtn');
    const toggleTx = container.querySelector('#toggleTranscript');
    const txBox = container.querySelector('#transcriptBox');

    function updatePlayState() {
      if (audio.paused) {
        playIcon.classList.remove('hidden');
        pauseIcon.classList.add('hidden');
      } else {
        playIcon.classList.add('hidden');
        pauseIcon.classList.remove('hidden');
      }
    }

    playPause.addEventListener('click', () => {
      if (audio.paused) audio.play().catch(() => {});
      else audio.pause();
      updatePlayState();
    });
    audio.addEventListener('play', updatePlayState);
    audio.addEventListener('pause', updatePlayState);
    audio.addEventListener('ended', updatePlayState);
    audio.addEventListener('loadedmetadata', () => { durationEl.textContent = formatTime(audio.duration); });
    audio.addEventListener('timeupdate', () => {
      if (audio.duration) {
        seek.value = (audio.currentTime / audio.duration) * 100;
        currentEl.textContent = formatTime(audio.currentTime);
        durationEl.textContent = formatTime(audio.duration);
      }
    });
    seek.addEventListener('input', () => {
      if (audio.duration) audio.currentTime = (seek.value / 100) * audio.duration;
    });
    speedEl.addEventListener('change', () => { audio.playbackRate = parseFloat(speedEl.value); });
    skipBack.addEventListener('click', () => { audio.currentTime = Math.max(0, audio.currentTime - 10); });
    skipFwd.addEventListener('click', () => { audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 10); });
    if (toggleTx && txBox) {
      toggleTx.addEventListener('click', () => { txBox.classList.toggle('hidden'); });
    }
    nextBtn.addEventListener('click', () => {
      audio.pause();
      if (onNext) onNext();
    });

    const ansBtn = container.querySelector('.listening-answers-key-btn');
    if (ansBtn) {
      ansBtn.addEventListener('click', () => {
        const d = extractPracticeData();
        const qs = d ? d.steps.filter(s => s.type === 'question') : [];
        const html = qs.map((s, idx) => {
          const q = s.content || s;
          const ans = String(q.answer || '');
          const ansText = q[`option${ans}`] || `Option ${ans}`;
          return `<div class="p-4 rounded-xl border border-zinc-200 bg-zinc-50 mb-3"><strong class="text-sm text-zinc-900">Q${idx + 1}: ${q.question || ''}</strong><p class="text-sm font-bold text-emerald-700 mt-1">Answer: ${ans}. ${ansText}</p>${q.explanation ? `<p class="text-xs text-zinc-700 mt-1 whitespace-pre-line">${q.explanation}</p>` : ''}</div>`;
        }).join('');
        openModal('Listening Answers Key & Explanations', html);
      });
    }

    audio.play().catch(() => {});
  }

  let currentTimerId = null;

  function startCountdown(seconds, onTick, onFinish) {
    if (currentTimerId) clearInterval(currentTimerId);
    let rem = seconds;
    if (onTick) onTick(rem);
    currentTimerId = setInterval(() => {
      rem--;
      if (onTick) onTick(rem);
      if (rem <= 0) {
        clearInterval(currentTimerId);
        currentTimerId = null;
        if (onFinish) onFinish();
      }
    }, 1000);
  }

  function renderOptions(q, selectedIdx, showResult) {
    const opts = [];
    for (let i = 1; i <= 8; i++) {
      const val = q[`option${i}`];
      if (val) opts.push({ idx: i.toString(), text: val });
    }
    const letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    return opts.map((opt, i) => {
      const isSelected = selectedIdx === opt.idx;
      const isCorrect = String(q.answer) === opt.idx;
      let styleClass = 'border-zinc-200 bg-white hover:border-blue-400 hover:bg-blue-50/40';
      if (showResult) {
        if (isCorrect) {
          styleClass = 'border-amber-400 bg-amber-50 text-amber-950 ring-1 ring-amber-400';
        } else if (isSelected && !isCorrect) {
          styleClass = 'border-red-400 bg-red-50 text-red-900 ring-1 ring-red-400';
        }
      } else if (isSelected) {
        styleClass = 'border-blue-600 bg-blue-50 ring-1 ring-blue-600';
      }

      const badgeClass = isSelected ? 'bg-blue-600 text-white' : (showResult && isCorrect ? 'bg-amber-500 text-white' : 'bg-zinc-100 text-black');
      return `
        <button type="button" data-opt="${opt.idx}" class="w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3 ${styleClass}">
          <span class="flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold shrink-0 mt-0.5 ${badgeClass}">${letters[i] || opt.idx}</span>
          <span class="text-sm font-medium leading-relaxed">${opt.text}</span>
        </button>
      `;
    }).join('');
  }

  function mountQuestionStep(step, qIndex, totalQ, onPrev, onNext) {
    const container = document.getElementById('practicePlayerContainer');
    if (!container) return;

    const q = step.content || step;
    const audioUrl = q.audio || step.audio || '';
    const qTranscript = q.question || '';
    let selectedOpt = null;
    let answerRevealed = false;

    container.innerHTML = `
      <div class="w-full max-w-5xl mx-auto bg-white rounded-2xl border border-zinc-200 shadow-sm my-4 overflow-hidden">
        <div class="flex items-center justify-between px-6 py-3.5 border-b border-zinc-200 bg-white">
          <div class="flex items-center gap-3">
            <span class="text-sm font-bold text-zinc-900">Question ${qIndex} of ${totalQ}</span>
            <div class="w-28 h-2 bg-zinc-100 rounded-full overflow-hidden">
              <div class="h-full bg-zinc-900 transition-all" style="width: ${Math.round((qIndex / totalQ) * 100)}%"></div>
            </div>
          </div>
          <div id="questionTimerBadge" class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-zinc-100 text-zinc-700 text-xs font-bold tabular-nums">
            <span>Time remaining:</span>
            <span id="timerValue">30 seconds</span>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2">
          <!-- Left Audio & Question Transcript Pane -->
          <div class="p-6 border-b lg:border-b-0 lg:border-r border-zinc-200 bg-white">
            <p class="text-sm font-bold text-[#1a578a] mb-3">Listen to the question.</p>
            ${audioUrl ? `
              <div class="mb-4 flex items-center gap-3 bg-zinc-50 border border-zinc-200 rounded-xl p-3">
                <audio id="qAudio" preload="auto" src="${audioUrl}"></audio>
                <button id="qAudioPlay" type="button" class="flex items-center justify-center w-9 h-9 rounded-full bg-blue-600 text-white text-xs font-bold hover:bg-blue-700 shrink-0">▶</button>
                <span class="text-xs font-medium text-zinc-600">Question Audio</span>
              </div>
            ` : ''}
            ${qTranscript ? `
              <div class="border border-zinc-200 rounded-xl p-3 mb-4">
                <button id="toggleQTx" type="button" class="flex w-full items-center justify-between text-xs font-bold text-zinc-700">
                  <span>Question transcript</span>
                  <span>▾</span>
                </button>
                <div id="qTxBody" class="hidden mt-2 text-sm text-zinc-800 font-medium">${qTranscript}</div>
              </div>
            ` : ''}
            <p class="text-xs text-zinc-500">In the official test, you can't rewind or replay the audio, and there's no transcript.</p>
          </div>

          <!-- Right Options Pane (#F0F7FF light-blue tint) -->
          <div class="p-6" style="background-color:#F0F7FF;">
            <p class="text-xs font-semibold text-zinc-500 mb-1">Question ${qIndex} of ${totalQ}</p>
            <h4 class="text-base font-bold text-zinc-900 mb-4 leading-snug">${qTranscript || 'Choose the best answer to each question.'}</h4>

            <div id="optionsList" class="space-y-2.5 mb-5">
              ${renderOptions(q, selectedOpt, answerRevealed)}
            </div>

            <div id="explanationBox" class="hidden mb-5 p-4 rounded-xl bg-white border border-amber-200 text-sm text-zinc-800 whitespace-pre-line leading-relaxed"></div>

            <div class="flex items-center justify-between pt-3 border-t border-blue-100">
              <button id="showAnswerBtn" type="button" class="px-4 py-2 rounded-xl border border-zinc-300 bg-white hover:bg-zinc-50 text-zinc-800 font-semibold text-xs shadow-sm">
                Show Answer
              </button>
              <div class="flex items-center gap-2">
                ${onPrev ? '<button id="prevQBtn" type="button" class="px-4 py-2 rounded-xl border border-zinc-300 bg-white hover:bg-zinc-50 text-zinc-700 font-semibold text-sm">← Prev</button>' : ''}
                <button id="nextQBtn" type="button" class="px-5 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm shadow-sm">
                  ${qIndex >= totalQ ? 'Finish Practice' : 'Next →'}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    const timerValEl = container.querySelector('#timerValue');
    const timerBadge = container.querySelector('#questionTimerBadge');
    startCountdown(30, (rem) => {
      if (timerValEl) timerValEl.textContent = rem > 0 ? `${rem} seconds` : "Time's up";
      if (rem <= 6 && rem > 0 && timerBadge) {
        timerBadge.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-100 text-amber-800 text-xs font-bold tabular-nums';
      } else if (rem <= 0 && timerBadge) {
        timerBadge.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-100 text-red-700 text-xs font-bold tabular-nums';
      }
    }, () => {});

    const qAudio = container.querySelector('#qAudio');
    const qAudioPlay = container.querySelector('#qAudioPlay');
    if (qAudio && qAudioPlay) {
      qAudioPlay.addEventListener('click', () => {
        if (qAudio.paused) qAudio.play().catch(() => {});
        else qAudio.pause();
      });
      qAudio.play().catch(() => {});
    }

    const tQTx = container.querySelector('#toggleQTx');
    const qTxBody = container.querySelector('#qTxBody');
    if (tQTx && qTxBody) {
      tQTx.addEventListener('click', () => qTxBody.classList.toggle('hidden'));
    }

    const optionsList = container.querySelector('#optionsList');
    const expBox = container.querySelector('#explanationBox');
    const showAnsBtn = container.querySelector('#showAnswerBtn');

    function bindOptionClicks() {
      optionsList.querySelectorAll('button[data-opt]').forEach(btn => {
        btn.addEventListener('click', () => {
          selectedOpt = btn.getAttribute('data-opt');
          optionsList.innerHTML = renderOptions(q, selectedOpt, answerRevealed);
          bindOptionClicks();
        });
      });
    }
    bindOptionClicks();

    showAnsBtn.addEventListener('click', () => {
      answerRevealed = !answerRevealed;
      showAnsBtn.textContent = answerRevealed ? 'Hide Answer' : 'Show Answer';
      optionsList.innerHTML = renderOptions(q, selectedOpt, answerRevealed);
      bindOptionClicks();
      if (answerRevealed && q.explanation) {
        expBox.textContent = q.explanation;
        expBox.classList.remove('hidden');
      } else {
        expBox.classList.add('hidden');
      }
    });

    container.querySelector('#nextQBtn').addEventListener('click', () => {
      if (currentTimerId) clearInterval(currentTimerId);
      if (qAudio) qAudio.pause();
      if (onNext) onNext();
    });

    const prevQBtn = container.querySelector('#prevQBtn');
    if (prevQBtn && onPrev) {
      prevQBtn.addEventListener('click', () => {
        if (currentTimerId) clearInterval(currentTimerId);
        if (qAudio) qAudio.pause();
        onPrev();
      });
    }
  }

  // --- Reading Practice: Authentic Floating Popover Dropdowns & Unlocked Answer Key ---
  function initReadingInteractive() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/reading_') && !window.location.pathname.includes('practices_reading_')) return;

    const allQ = extractFlightJson('Question', '[', ']');
    const fallbackQ = extractFlightJson('questions', '[', ']');
    const questions = (Array.isArray(allQ) && allQ.length >= (Array.isArray(fallbackQ) ? fallbackQ.length : 0)) ? allQ : fallbackQ;
    if (!Array.isArray(questions) || questions.length === 0) return;

    const questionBtns = Array.from(document.querySelectorAll('button[aria-haspopup="dialog"].font-practice'));
    const selections = {}; // idx -> chosen option '1'..'8'
    let activePopover = null;

    function closePopover() {
      if (activePopover) {
        activePopover.remove();
        activePopover = null;
      }
    }
    document.addEventListener('click', (e) => {
      if (activePopover && !activePopover.contains(e.target) && !e.target.closest('button[aria-haspopup="dialog"].font-practice')) {
        closePopover();
      }
    });

    const entries = [];
    questionBtns.forEach((btn, idx) => {
      const q = questions[idx];
      if (!q) return;
      const li = btn.closest('li');
      const numSpan = li ? li.querySelector('span.font-semibold') : null;
      const numText = (numSpan ? numSpan.textContent.replace(/[^0-9]/g, '') : '') || (btn.textContent || '').replace(/[^0-9]/g, '') || String(idx + 1);

      btn.setAttribute('data-q-num', numText);
      entries.push({ btn, q, idx, numText, host: li || btn.closest('p') || btn.parentElement });

      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const wasSame = activePopover && activePopover.dataset.ownerIdx === String(idx);
        closePopover();
        if (wasSame) return;

        const pop = document.createElement('div');
        pop.dataset.ownerIdx = String(idx);
        pop.className = 'fixed z-[9999] w-80 max-w-[90vw] rounded-xl border border-zinc-200 bg-white p-1.5 shadow-xl';
        const rect = btn.getBoundingClientRect();
        pop.style.left = `${Math.min(window.innerWidth - 330, Math.max(8, rect.left))}px`;
        pop.style.top = `${Math.min(window.innerHeight - 220, rect.bottom + 6)}px`;

        for (let i = 1; i <= 8; i++) {
          const optText = q[`option${i}`];
          if (!optText) continue;
          const isChosen = selections[idx] === String(i);
          const item = document.createElement('button');
          item.type = 'button';
          item.className = `w-full text-left px-3 py-2 rounded-lg text-sm flex items-center gap-2.5 transition-colors ${isChosen ? 'bg-blue-50 text-blue-900 font-semibold' : 'hover:bg-zinc-100 text-zinc-800'}`;
          item.innerHTML = `
            <span class="w-4 h-4 rounded-full border flex items-center justify-center shrink-0 ${isChosen ? 'border-blue-600 bg-blue-600' : 'border-zinc-400'}">
              ${isChosen ? '<span class="w-1.5 h-1.5 rounded-full bg-white"></span>' : ''}
            </span>
            <span class="leading-snug">${optText}</span>
          `;
          item.addEventListener('click', () => {
            selections[idx] = String(i);
            btn.innerHTML = `<span class="truncate text-zinc-900 font-semibold">${numText}. ${optText}</span><svg class="w-3.5 h-3.5 shrink-0 opacity-70" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>`;
            btn.classList.remove('text-zinc-500');
            btn.classList.add('border-blue-500', 'bg-blue-50/50', 'text-zinc-900');
            closePopover();
          });
          pop.appendChild(item);
        }

        document.body.appendChild(pop);
        activePopover = pop;
      });
    });

    function buildAnswerKeyHtml() {
      let score = 0;
      const rows = entries.map(({ q, idx, numText }) => {
        const correct = String(q.answer || '');
        const chosen = selections[idx] || '';
        const ok = chosen === correct;
        if (ok) score++;
        const correctText = q[`option${correct}`] || `Option ${correct}`;
        return `
          <div class="p-4 rounded-xl border ${ok ? 'border-emerald-200 bg-emerald-50/50' : 'border-zinc-200 bg-zinc-50'} mb-3">
            <div class="flex items-center justify-between mb-1">
              <strong class="text-sm text-zinc-900">Question ${numText}${q.question ? `: ${q.question}` : ''}</strong>
              <span class="px-2 py-0.5 rounded-full text-xs font-bold ${ok ? 'bg-emerald-100 text-emerald-800' : 'bg-amber-100 text-amber-800'}">
                ${chosen ? (ok ? '✓ Correct' : `✗ Chose ${chosen}`) : 'Unanswered'}
              </span>
            </div>
            <p class="text-sm font-bold text-emerald-700 mb-1">Correct Answer: ${correct}. ${correctText}</p>
            ${q.explanation ? `<p class="text-xs text-zinc-700 whitespace-pre-line leading-relaxed">${q.explanation}</p>` : ''}
          </div>
        `;
      }).join('');
      return `<div class="mb-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-sm font-bold text-blue-900">Score: ${score} / ${entries.length}</div>${rows}`;
    }

    function showAnswersInline() {
      entries.forEach(({ btn, q, idx, numText }) => {
        const correct = String(q.answer || '');
        const correctText = q[`option${correct}`] || `Option ${correct}`;
        btn.innerHTML = `<span class="truncate font-semibold">${numText}. ${correctText}</span><svg class="w-3.5 h-3.5 shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>`;
        btn.style.backgroundColor = '#fef3c7';
        btn.style.borderColor = '#f59e0b';
        btn.style.color = '#78350f';
      });
    }

    // Capture-phase delegation survives React hydration and blocks <a href="/exams"> navigation
    document.addEventListener('click', (e) => {
      const btn = e.target && e.target.closest ? e.target.closest('button, a') : null;
      if (!btn) return;
      const t = (btn.textContent || '').trim().toLowerCase();
      if (t.includes('answers key')) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        showAnswersInline();
        openModal('Reading Answers Key & Explanations', buildAnswerKeyHtml());
      } else if (t.includes('show answer') || t.includes('check answer')) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        showAnswersInline();
        openModal('Answer Key & Explanations', buildAnswerKeyHtml());
      }
    }, true);
  }

  // --- 7-Section Example / Score Report Modal (Writing & Speaking) ---
  function openReportModal(skillLabel, analysisData, userDraftText, samplesData) {
    const sc = (analysisData && analysisData.score) || { grammar: 8, coherence: 8, vocabulary: 8, fulfillment: 8, listenability: 8 };
    const avg = Math.round(((sc.grammar || 8) + (sc.coherence || 8) + (sc.vocabulary || 8) + (sc.fulfillment || 8)) / 4);
    const words = userDraftText ? userDraftText.trim().split(/\s+/).filter(Boolean).length : 185;
    const fourthMetric = skillLabel === 'Speaking' ? `Listenability: ${sc.listenability || 8}/12` : `Readability: ${sc.grammar || 8}/12`;
    const fb = resolveFlightRef((analysisData && analysisData.assessment && (analysisData.assessment.review || analysisData.assessment.feedback)) || '')
      || 'Strong structure and clear coverage of prompt requirements. To reach CLB 10–12, vary sentence openings and incorporate natural Canadian collocations.';
    const topSample = resolveFlightRef((samplesData && samplesData.tiers && samplesData.tiers.high && samplesData.tiers.high.text) || '')
      || 'High-scoring CLB 10+ model response loaded from prompt.';

    const html = `
      <div class="space-y-6">
        <div class="p-5 rounded-2xl bg-zinc-900 text-white">
          <div class="flex items-center justify-between mb-3">
            <div>
              <p class="text-xs uppercase tracking-wider text-zinc-400 font-bold">01 Score · Estimated CELPIP Level</p>
              <div class="text-3xl font-black mt-1">${avg}<span class="text-lg text-zinc-400 font-semibold">/12</span></div>
            </div>
            <span class="px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold">${words} words</span>
          </div>
          <div class="grid grid-cols-2 gap-2 text-xs text-zinc-300 pt-3 border-t border-zinc-800">
            <div>Content &amp; Coherence: <strong class="text-white">${sc.coherence || 8}/12</strong></div>
            <div>Vocabulary: <strong class="text-white">${sc.vocabulary || 8}/12</strong></div>
            <div>${fourthMetric.split(':')[0]}: <strong class="text-white">${fourthMetric.split(':')[1]}</strong></div>
            <div>Task Fulfillment: <strong class="text-white">${sc.fulfillment || 8}/12</strong></div>
          </div>
        </div>
        <div class="p-4 rounded-xl bg-zinc-50 border border-zinc-200">
          <h4 class="text-sm font-bold text-zinc-900 mb-1">02 Coverage &amp; 03 What to Fix</h4>
          <p class="text-sm text-zinc-700 leading-relaxed whitespace-pre-line">${fb}</p>
        </div>
        <div class="p-4 rounded-xl bg-emerald-50/70 border border-emerald-200">
          <h4 class="text-sm font-bold text-emerald-900 mb-2">04 Score Higher — CLB 11–12 Model Rewrite</h4>
          <p class="text-sm text-zinc-800 leading-relaxed whitespace-pre-line">${topSample}</p>
        </div>
      </div>
    `;
    openModal(`${skillLabel} Score &amp; Feedback Report`, html, 'max-w-3xl');
  }

  function renderTierSamplePanel(anchorEl, samplesData, analysisData, userDraftFn, skillLabel) {
    const tiers = (samplesData && samplesData.tiers) || {};
    const tierMap = { Weak: tiers.low, Normal: tiers.medium, Top: tiers.high };

    const allButtons = Array.from(document.querySelectorAll('button'));
    const tierBtns = allButtons.filter(b => ['Weak', 'Normal', 'Top'].includes((b.textContent || '').trim()));
    const scoreBtns = allButtons.filter(b => {
      const t = (b.textContent || '').trim().toLowerCase();
      return t.includes('score my answer') || t.includes('sample analysis') || t.includes('see an example report');
    });
    const reportBtns = [];

    let viewer = document.getElementById('celpipSampleViewer');
    if (!viewer && anchorEl) {
      viewer = document.createElement('div');
      viewer.id = 'celpipSampleViewer';
      viewer.className = 'hidden mt-3 p-4 rounded-xl bg-white border border-zinc-200 text-sm text-zinc-800 leading-relaxed whitespace-pre-line shadow-sm';
      anchorEl.appendChild(viewer);
    }

    tierBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const label = (btn.textContent || '').trim();
        tierBtns.forEach(t => t.setAttribute('aria-selected', t === btn ? 'true' : 'false'));
        const item = tierMap[label];
        if (!viewer) return;
        viewer.classList.remove('hidden');
        const resolvedText = item && item.text ? resolveFlightRef(item.text) : 'Sample response loaded for this task.';
        const badgeColor = label === 'Top' ? 'bg-emerald-100 text-emerald-800' : (label === 'Normal' ? 'bg-blue-100 text-blue-800' : 'bg-amber-100 text-amber-800');
        viewer.innerHTML = `
          <div class="flex items-center justify-between mb-2">
            <strong class="text-zinc-900">${label} Sample Response</strong>
            <span class="px-2.5 py-0.5 rounded-full text-xs font-bold ${badgeColor}">${item && item.band ? `CLB ${item.band}` : label}</span>
          </div>
          <div class="text-zinc-700 whitespace-pre-line">${resolvedText}</div>
        `;
      });
    });

    // Capture-phase delegation for Score my answer / Sample analysis / See an example report
    document.addEventListener('click', (e) => {
      const btn = e.target && e.target.closest ? e.target.closest('button, a') : null;
      if (!btn || btn.closest('#celtestpipReplicaModal')) return;
      const t = (btn.textContent || '').trim().toLowerCase();
      if (t.includes('score my answer') || t.includes('sample analysis') || t.includes('see an example report')) {
        e.preventDefault();
        e.stopPropagation();
        e.stopImmediatePropagation();
        openReportModal(skillLabel, analysisData, userDraftFn ? userDraftFn() : '', samplesData);
      }
    }, true);

    reportBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openReportModal(skillLabel, analysisData, '', samplesData);
      });
    });
  }

  // --- Writing Practice Native Hook ---
  function initWritingEditor() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/writing_') && !window.location.pathname.includes('practices_writing_')) return;

    const textarea = document.querySelector('textarea');
    const samplesData = extractFlightJson('samples', '{', '}');
    const analysisData = extractFlightJson('analysis', '{', '}');

    if (textarea) {
      // Prevent any React login gate from blocking typing
      textarea.removeAttribute('readonly');
      textarea.removeAttribute('disabled');
      const updateWordCount = () => {
        const words = textarea.value.trim() ? textarea.value.trim().split(/\s+/).length : 0;
        const candidates = Array.from(document.querySelectorAll('p')).filter(el =>
          el.children.length <= 1 && /^\d+\s*\/\s*150[-–]200\s*words$/i.test((el.textContent || '').trim())
        );
        candidates.forEach(el => {
          const numSpan = el.querySelector('span');
          if (numSpan) numSpan.textContent = String(words);
          else el.textContent = `${words} / 150–200 words`;
        });
      };
      textarea.addEventListener('input', updateWordCount);
      updateWordCount();
    }

    const weakBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Weak');
    const anchor = (weakBtn && weakBtn.parentElement && weakBtn.parentElement.parentElement)
      || (textarea && textarea.parentElement)
      || document.querySelector('main');

    renderTierSamplePanel(anchor, samplesData, analysisData, () => (textarea ? textarea.value : ''), 'Writing');
  }

  // --- Speaking Practice Native Hook (Prep Timer -> Record | 90s State) ---
  function initSpeakingRecorder() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/speaking_') && !window.location.pathname.includes('practices_speaking_')) return;

    const samplesData = extractFlightJson('samples', '{', '}');
    const analysisData = extractFlightJson('analysis', '{', '}');

    // Populate Clock icon inside Preparation Time box (persists after React hydration)
    const ensureClockIcon = () => {
      document.querySelectorAll('span.h-14.w-14, div.h-14.w-14').forEach(el => {
        const curSvg = el.querySelector('svg');
        if (!el.textContent.trim() && (!curSvg || curSvg.getBoundingClientRect().width === 0)) {
          el.innerHTML = '<svg class="w-6 h-6 text-zinc-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>';
        }
      });
    };
    ensureClockIcon();
    setTimeout(ensureClockIcon, 250);
    setTimeout(ensureClockIcon, 800);

    // Wire Skip -> Recording Ready ("Record | 90s") state
    const skipBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Skip');
    const prepTextEl = Array.from(document.querySelectorAll('span, p, div')).find(el =>
      el.children.length === 0 && (el.textContent || '').trim() === 'Preparation Time'
    );

    if (prepTextEl && !document.getElementById('speakingNativeTimerBar')) {
      let card = prepTextEl.parentElement;
      while (card && card.parentElement && !card.className.includes('border') && !card.className.includes('bg-white')) {
        card = card.parentElement;
      }
      if (!card || card.querySelector('h2') || card.textContent.includes('Sample Answers')) {
        card = prepTextEl.parentElement.parentElement;
      }
      const numEl = card ? Array.from(card.querySelectorAll('span, div, p')).find(el => el.children.length === 0 && /^(30|60)$/.test((el.textContent || '').trim())) : null;
      const initialPrep = numEl ? parseInt(numEl.textContent.trim(), 10) : 30;
      let prepTimer = null;
      let recTimer = null;

      function switchToRecordState() {
        if (prepTimer) clearInterval(prepTimer);
        if (!card) return;
        card.innerHTML = `
          <div class="flex flex-col items-center justify-center py-6 text-center gap-4">
            <h4 class="text-base font-bold text-zinc-900">Record to get your score</h4>
            <button id="record90Btn" type="button" style="background-color:#ef4444;color:#ffffff;" class="inline-flex items-center gap-3 px-6 py-3 rounded-xl font-bold text-sm shadow-md hover:opacity-95 cursor-pointer">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>
              <span id="recordBtnLabel">Record</span>
              <span class="opacity-60">|</span>
              <span id="recordTimerSpan" class="tabular-nums">90s</span>
            </button>
            <div class="flex items-center gap-3 text-xs text-zinc-500">
              <button id="prepAgainBtn" type="button" class="inline-flex items-center gap-1 font-semibold text-zinc-700 hover:text-zinc-900">↻ Prep again</button>
              <span>· It's <span class="text-blue-600 font-semibold">free</span> to test your score.</span>
            </div>
          </div>
        `;
        const recBtn = card.querySelector('#record90Btn');
        const recLabel = card.querySelector('#recordBtnLabel');
        const recSpan = card.querySelector('#recordTimerSpan');
        let recording = false;
        let mediaRecorder = null;

        recBtn.addEventListener('click', async () => {
          if (!recording) {
            recording = true;
            recLabel.textContent = 'Stop Recording';
            let rem = 90;
            recSpan.textContent = `${rem}s`;
            try {
              const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
              mediaRecorder = new MediaRecorder(stream);
              mediaRecorder.start();
            } catch (err) {}
            recTimer = setInterval(() => {
              rem--;
              recSpan.textContent = `${rem}s`;
              if (rem <= 0) {
                clearInterval(recTimer);
                recording = false;
                if (mediaRecorder && mediaRecorder.state !== 'inactive') mediaRecorder.stop();
                openReportModal('Speaking', analysisData, '', samplesData);
              }
            }, 1000);
          } else {
            recording = false;
            clearInterval(recTimer);
            if (mediaRecorder && mediaRecorder.state !== 'inactive') mediaRecorder.stop();
            recLabel.textContent = 'Record';
            openReportModal('Speaking', analysisData, '', samplesData);
          }
        });

        card.querySelector('#prepAgainBtn').addEventListener('click', () => {
          window.location.reload();
        });
      }

      if (skipBtn) {
        skipBtn.addEventListener('click', (e) => {
          e.preventDefault();
          switchToRecordState();
        });
      }

      // Auto-start preparation countdown if numeric counter exists
      if (numEl) {
        let rem = initialPrep;
        prepTimer = setInterval(() => {
          rem--;
          numEl.textContent = String(rem);
          if (rem <= 0) {
            clearInterval(prepTimer);
            switchToRecordState();
          }
        }, 1000);
      }
    }

    const weakBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Weak');
    const anchor = (weakBtn && weakBtn.parentElement && weakBtn.parentElement.parentElement) || document.querySelector('main');
    renderTierSamplePanel(anchor, samplesData, analysisData, null, 'Speaking');
  }

  // --- Part-Page Tabs & Topic Filter Popover (/parts/*) ---
  function initPartPageControls() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/parts/')) return;

    const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
    const panels = Array.from(document.querySelectorAll('[role="tabpanel"]'));

    tabs.forEach((tab, idx) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => {
          const active = t === tab;
          t.setAttribute('aria-selected', active ? 'true' : 'false');
          t.setAttribute('data-state', active ? 'active' : 'inactive');
          if (active) t.classList.add('bg-white', 'text-zinc-900', 'shadow-sm');
          else t.classList.remove('bg-white', 'text-zinc-900', 'shadow-sm');
        });
        panels.forEach((p, pIdx) => {
          const targetId = tab.getAttribute('aria-controls');
          const match = targetId ? p.id === targetId : pIdx === idx;
          if (match) {
            p.removeAttribute('hidden');
            p.setAttribute('data-state', 'active');
            p.style.display = '';
          } else {
            p.setAttribute('hidden', '');
            p.setAttribute('data-state', 'inactive');
            p.style.display = 'none';
          }
        });
      });
    });

    // Wire Topic filter dropdown ("All topics")
    const topicBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').includes('All topics'));
    if (topicBtn) {
      const cards = Array.from(document.querySelectorAll('a[href^="/practices/"]'));
      const topicSet = new Set(['All topics']);
      cards.forEach(c => {
        const badge = c.querySelector('span[class*="rounded"]');
        const txt = badge ? badge.textContent.trim() : '';
        if (txt && txt.length < 40 && !/^(FREE|NEW|\d+)$/i.test(txt)) topicSet.add(txt);
      });
      if (topicSet.size === 1) {
        ['Travel & Transport', 'Community & Services', 'Health & Wellness', 'Home & Housing', 'Work & Career', 'Education & Learning', 'Leisure & Culture'].forEach(t => topicSet.add(t));
      }

      let pop = null;
      topicBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        if (pop) { pop.remove(); pop = null; return; }
        pop = document.createElement('div');
        pop.className = 'fixed z-[9999] w-80 max-w-[92vw] rounded-2xl border border-zinc-200 bg-white p-4 shadow-xl';
        const rect = topicBtn.getBoundingClientRect();
        pop.style.left = `${Math.max(8, rect.left)}px`;
        pop.style.top = `${rect.bottom + 8}px`;
        pop.innerHTML = `<div class="text-[11px] font-bold uppercase tracking-wider text-zinc-400 mb-2">Topic</div><div class="flex flex-wrap gap-1.5" id="topicPillsWrap"></div>`;
        const wrap = pop.querySelector('#topicPillsWrap');
        topicSet.forEach(t => {
          const pill = document.createElement('button');
          pill.type = 'button';
          pill.className = 'px-3 py-1.5 rounded-full text-xs font-semibold border border-blue-200 hover:bg-blue-50 hover:border-blue-300 text-blue-950';
          pill.textContent = t;
          pill.addEventListener('click', () => {
            topicBtn.innerHTML = `Topic <strong class="ml-1">${t}</strong>`;
            cards.forEach(c => {
              c.style.display = (t === 'All topics' || c.textContent.includes(t)) ? '' : 'none';
            });
            pop.remove();
            pop = null;
          });
          wrap.appendChild(pill);
        });
        document.body.appendChild(pop);
      });
      document.addEventListener('click', (e) => {
        if (pop && !pop.contains(e.target) && e.target !== topicBtn) { pop.remove(); pop = null; }
      });
    }

    const freeToggle = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').includes('Free only'));
    if (freeToggle) {
      freeToggle.addEventListener('click', () => {
        const pressed = freeToggle.getAttribute('aria-pressed') === 'true';
        freeToggle.setAttribute('aria-pressed', pressed ? 'false' : 'true');
      });
    }
  }

  // --- Shared Left Sidebar Rail Toggle (Show sidebar) ---
  function initPracticeSidebar() {
    const toggleBtn = Array.from(document.querySelectorAll('button')).find(b => {
      const label = (b.getAttribute('aria-label') || b.getAttribute('title') || '').toLowerCase();
      return label.includes('sidebar');
    });
    if (!toggleBtn) return;

    toggleBtn.addEventListener('click', (e) => {
      e.preventDefault();
      let drawer = document.getElementById('celpipPracticeSidebarDrawer');
      if (drawer) {
        drawer.remove();
        return;
      }
      const list = extractFlightJson('Practice', '[', ']') || extractFlightJson('practices', '[', ']') || [];
      drawer = document.createElement('div');
      drawer.id = 'celpipPracticeSidebarDrawer';
      drawer.className = 'fixed top-16 left-0 bottom-0 w-72 bg-white border-r border-zinc-200 shadow-2xl z-[9998] flex flex-col overflow-hidden';
      const itemsHtml = Array.isArray(list) && list.length
        ? list.slice(0, 100).map((p, i) => `<a href="/practices/${(p.type || 'listening').toLowerCase()}_${p.id}" class="flex items-center justify-between px-3 py-2 rounded-lg text-xs font-medium text-blue-950 hover:bg-blue-50 hover:text-blue-900"><span class="truncate">${i + 1}. ${p.name || p.id}</span><span class="text-[10px] font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.5 rounded">FREE</span></a>`).join('')
        : '<p class="text-xs text-zinc-500 p-3">Use the navigation bar to switch parts or practices.</p>';

      drawer.innerHTML = `
        <div class="flex items-center justify-between px-4 py-3 border-b border-zinc-100">
          <strong class="text-sm text-zinc-900">Practice List</strong>
          <button id="closeSidebarDrawerBtn" type="button" class="text-xs font-semibold text-zinc-500 hover:text-zinc-900">✕</button>
        </div>
        <div class="p-2 overflow-y-auto flex-1 space-y-0.5">${itemsHtml}</div>
      `;
      document.body.appendChild(drawer);
      drawer.querySelector('#closeSidebarDrawerBtn').addEventListener('click', () => drawer.remove());
    });
  }

  function findStartButtons() {
    const byId = [
      document.getElementById('startBtn'),
      document.getElementById('startTaskBtn'),
      document.getElementById('headerStartBtn')
    ].filter(Boolean);
    if (byId.length > 0) return byId;

    return Array.from(document.querySelectorAll('button')).filter(btn => {
      const txt = (btn.textContent || '').trim();
      return txt.startsWith('Start') || txt === 'Start' || txt.includes('Start →');
    });
  }

  window.CeltestpipRunner = {
    formatTime,
    extractPracticeData,
    mountAudioPlayer,
    mountQuestionStep,
    startCountdown,
    renderOptions,
    findStartButtons,
    initReadingInteractive,
    initWritingEditor,
    initSpeakingRecorder,
    initPartPageControls,
  };

  function initRunner() {
    initReadingInteractive();
    initWritingEditor();
    initSpeakingRecorder();
    initPartPageControls();
    initPracticeSidebar();

    const startBtns = findStartButtons();
    const data = extractPracticeData();
    if (startBtns.length && data && data.steps) {
      // Inject "Answers key" button into Listening header next to Start button if missing
      const firstHeaderStart = startBtns.find(b => b.closest('header'));
      if (firstHeaderStart && firstHeaderStart.parentElement && !firstHeaderStart.parentElement.querySelector('.listening-answers-key-btn')) {
        const akBtn = document.createElement('button');
        akBtn.type = 'button';
        akBtn.className = 'listening-answers-key-btn inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold rounded-xl border border-zinc-300 bg-white hover:bg-zinc-50 text-zinc-700 h-10 px-3.5 shadow-sm';
        akBtn.textContent = 'Answers key';
        firstHeaderStart.parentElement.insertBefore(akBtn, firstHeaderStart);
      }

      // Capture-phase handler for Listening Answers key button
      document.addEventListener('click', (e) => {
        const btn = e.target && e.target.closest ? e.target.closest('button') : null;
        if (!btn) return;
        const t = (btn.textContent || '').trim().toLowerCase();
        if (t === 'answers key' || btn.classList.contains('listening-answers-key-btn')) {
          e.preventDefault();
          e.stopPropagation();
          const qs = data.steps.filter(s => s.type === 'question');
          const html = qs.map((s, idx) => {
            const q = s.content || s;
            const ans = String(q.answer || '');
            const ansText = q[`option${ans}`] || `Option ${ans}`;
            return `<div class="p-4 rounded-xl border border-zinc-200 bg-zinc-50 mb-3"><strong class="text-sm text-zinc-900">Q${idx + 1}: ${q.question || ''}</strong><p class="text-sm font-bold text-emerald-700 mt-1">Answer: ${ans}. ${ansText}</p>${q.explanation ? `<p class="text-xs text-zinc-700 mt-1 whitespace-pre-line">${q.explanation}</p>` : ''}</div>`;
          }).join('');
          openModal('Listening Answers Key & Explanations', html);
        }
      }, true);

      startBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          const introContainer = btn.closest('div[class*="rounded-2xl"]')
            || btn.closest('div[class*="max-lg:overflow"]')
            || btn.closest('.border')
            || btn.closest('div');
          if (introContainer) introContainer.style.display = 'none';

          startBtns.forEach(b => {
            if (b.id === 'headerStartBtn') b.style.display = 'none';
          });

          let container = document.getElementById('practicePlayerContainer');
          if (!container) {
            container = document.createElement('div');
            container.id = 'practicePlayerContainer';
            document.body.appendChild(container);
          }
          if (introContainer && introContainer.parentNode) {
            introContainer.parentNode.insertBefore(container, introContainer.nextSibling);
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
                const qNum = step.questionNumber || (data.steps.filter(s => s.type === 'question').indexOf(step) + 1) || currentStepIdx;
                mountQuestionStep(step, qNum, totalQ, null, runNext);
              } else {
                runNext();
              }
            } else {
              window.location.reload();
            }
          }

          const audioStep = data.steps.find(s => s.type === 'audio') || data.steps[1];
          if (audioStep) {
            currentStepIdx = data.steps.indexOf(audioStep);
            mountAudioPlayer(audioStep, runNext);
          } else {
            runNext();
          }

          container.scrollIntoView({ behavior: 'smooth', block: 'start' });
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
