/**
 * CELTESTPIP Native Ditto Practice Runner
 * Powers interactive Listening, Reading, Writing, Speaking, and Part-page controls
 * with zero external dependencies.
 */
(function() {
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
    // Match Next.js Flight text chunk: `4c:T<hexlen>,<body...>` (preceded by start, non-alnum, or escaped \n)
    const tPat = new RegExp(`(?:^|\\\\n|[^0-9a-zA-Z])${refId}:T([0-9a-fA-F]+),`);
    for (const s of scripts) {
      const txt = s.textContent || '';
      if (!txt.includes(`${refId}:`)) continue;
      const m = tPat.exec(txt);
      if (m) {
        const start = m.index + m[0].length;
        const rest = txt.slice(start);
        // Stop at end of push string `"])` or next chunk `<hex>:T<hex>,` or `<hex>:[`
        const endMatch = rest.match(/(?:"\]\)|[0-9a-fA-F]+:(?:T[0-9a-fA-F]+,|\[|\{|"))/);
        const rawChunk = endMatch ? rest.slice(0, endMatch.index) : rest;
        try {
          return JSON.parse(`"${rawChunk.replace(/\n/g, '\\n').replace(/\r/g, '\\r')}"`);
        } catch (e) {
          return rawChunk.replace(/\\n/g, '\n').replace(/\\r/g, '').replace(/\\"/g, '"');
        }
      }
      // Fallback: `4c:"..."`
      const qPat = new RegExp(`(?:^|[^0-9a-zA-Z])${refId}:"((?:[^"\\\\]|\\\\.)*)"`);
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
              let jsonStr = raw.replace(/\\"/g, '"').replace(/\\\\n/g, '\\n').replace(/\\n/g, '\\n');
              const steps = JSON.parse(jsonStr);
              if (Array.isArray(steps) && steps.length > 0) {
                return { steps };
              }
            } catch (e) {}
          }
        }
      }
    }
    return null;
  }

  function mountAudioPlayer(step, onNext) {
    const container = document.getElementById('practicePlayerContainer');
    if (!container) return;

    const audioUrl = step.audio || (step.content && step.content.audio) || '';
    const transcript = (step.content && step.content.transcript) || step.transcript || '';

    container.innerHTML = `
      <div class="w-full max-w-3xl mx-auto p-6 bg-white rounded-2xl border border-zinc-200 shadow-sm my-4">
        <div class="flex items-center justify-between mb-6">
          <div class="flex items-center gap-3">
            <span class="flex h-3 w-3 rounded-full bg-emerald-500 animate-pulse"></span>
            <h3 class="text-lg font-bold text-zinc-900">Listen to the Conversation</h3>
          </div>
          <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200">Listening Passage</span>
        </div>

        <audio id="practiceAudio" preload="auto" src="${audioUrl}"></audio>

        <!-- Custom Audio Bar -->
        <div class="bg-zinc-50 border border-zinc-200 rounded-xl p-4 mb-6">
          <div class="flex items-center gap-4 mb-3">
            <button id="audioSkipBack" type="button" class="p-2 text-zinc-600 hover:text-zinc-900 hover:bg-zinc-200/60 rounded-lg transition-colors" title="Back 10s">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><text x="9" y="15" font-size="7" font-weight="bold" fill="currentColor" stroke="none">10</text></svg>
            </button>
            <button id="audioPlayPause" type="button" class="flex items-center justify-center w-12 h-12 rounded-full bg-blue-600 hover:bg-blue-700 text-white shadow-md transition-transform active:scale-95">
              <svg id="playIcon" class="w-5 h-5 ml-0.5" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
              <svg id="pauseIcon" class="w-5 h-5 hidden" fill="currentColor" viewBox="0 0 24 24"><path d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
            </button>
            <button id="audioSkipFwd" type="button" class="p-2 text-zinc-600 hover:text-zinc-900 hover:bg-zinc-200/60 rounded-lg transition-colors" title="Forward 10s">
              <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><text x="9" y="15" font-size="7" font-weight="bold" fill="currentColor" stroke="none">10</text></svg>
            </button>

            <div class="flex-1 flex flex-col gap-1">
              <input id="audioSeek" type="range" min="0" max="100" value="0" class="w-full accent-blue-600 h-1.5 bg-zinc-200 rounded-lg cursor-pointer" />
              <div class="flex justify-between text-xs font-medium text-zinc-500 tabular-nums">
                <span id="audioCurrent">00:00</span>
                <span id="audioDuration">00:00</span>
              </div>
            </div>

            <select id="audioSpeed" class="text-xs font-semibold bg-white border border-zinc-300 rounded-lg px-2 py-1.5 text-zinc-700 cursor-pointer">
              <option value="0.75">0.75x</option>
              <option value="1" selected>1x</option>
              <option value="1.25">1.25x</option>
              <option value="1.5">1.5x</option>
            </select>
          </div>
        </div>

        ${transcript ? `
          <div class="mb-6">
            <button id="toggleTranscript" type="button" class="flex items-center gap-2 text-sm font-semibold text-blue-600 hover:text-blue-700">
              <span>Show Conversation Transcript</span>
              <svg class="w-4 h-4 transition-transform" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>
            </button>
            <div id="transcriptBox" class="hidden mt-3 p-4 rounded-xl bg-zinc-50 border border-zinc-200 text-sm text-zinc-700 leading-relaxed whitespace-pre-line max-h-60 overflow-y-auto">${transcript}</div>
          </div>
        ` : ''}

        <div class="flex justify-end">
          <button id="audioNextBtn" type="button" class="inline-flex items-center justify-center px-6 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm shadow-sm transition-colors">
            Next Questions →
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
      if (audio.paused) {
        audio.play().catch(() => {});
      } else {
        audio.pause();
      }
      updatePlayState();
    });

    audio.addEventListener('play', updatePlayState);
    audio.addEventListener('pause', updatePlayState);
    audio.addEventListener('ended', updatePlayState);

    audio.addEventListener('loadedmetadata', () => {
      durationEl.textContent = formatTime(audio.duration);
    });

    audio.addEventListener('timeupdate', () => {
      if (audio.duration) {
        seek.value = (audio.currentTime / audio.duration) * 100;
        currentEl.textContent = formatTime(audio.currentTime);
        durationEl.textContent = formatTime(audio.duration);
      }
    });

    seek.addEventListener('input', () => {
      if (audio.duration) {
        audio.currentTime = (seek.value / 100) * audio.duration;
      }
    });

    speedEl.addEventListener('change', () => {
      audio.playbackRate = parseFloat(speedEl.value);
    });

    skipBack.addEventListener('click', () => {
      audio.currentTime = Math.max(0, audio.currentTime - 10);
    });

    skipFwd.addEventListener('click', () => {
      audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 10);
    });

    if (toggleTx && txBox) {
      toggleTx.addEventListener('click', () => {
        txBox.classList.toggle('hidden');
      });
    }

    nextBtn.addEventListener('click', () => {
      audio.pause();
      if (onNext) onNext();
    });

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
      const isCorrect = q.answer === opt.idx;
      let styleClass = 'border-zinc-200 bg-white hover:border-blue-400 hover:bg-blue-50/30';
      if (showResult) {
        if (isCorrect) {
          styleClass = 'border-emerald-500 bg-emerald-50 text-emerald-900 ring-1 ring-emerald-500';
        } else if (isSelected && !isCorrect) {
          styleClass = 'border-red-500 bg-red-50 text-red-900 ring-1 ring-red-500';
        }
      } else if (isSelected) {
        styleClass = 'border-blue-600 bg-blue-50 ring-1 ring-blue-600';
      }

      return `
        <button type="button" data-opt="${opt.idx}" class="w-full text-left p-4 rounded-xl border transition-all flex items-start gap-3 ${styleClass}">
          <span class="flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold shrink-0 mt-0.5 ${isSelected ? 'bg-blue-600 text-white' : 'bg-zinc-100 text-zinc-700'}">${letters[i] || opt.idx}</span>
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
    let selectedOpt = null;
    let answerRevealed = false;

    container.innerHTML = `
      <div class="w-full max-w-3xl mx-auto p-6 bg-white rounded-2xl border border-zinc-200 shadow-sm my-4">
        <div class="flex items-center justify-between mb-4 pb-3 border-b border-zinc-100">
          <div class="flex items-center gap-3">
            <span class="text-sm font-bold text-zinc-900">Question ${qIndex} of ${totalQ}</span>
            <div class="w-32 h-2 bg-zinc-100 rounded-full overflow-hidden">
              <div class="h-full bg-blue-600 transition-all" style="width: ${Math.round((qIndex / totalQ) * 100)}%"></div>
            </div>
          </div>
          <div id="questionTimerBadge" class="flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 border border-amber-200 text-amber-800 text-xs font-bold tabular-nums">
            <span>⏱</span>
            <span id="timerValue">30s</span>
          </div>
        </div>

        ${audioUrl ? `
          <div class="mb-5 flex items-center gap-3 bg-zinc-50 border border-zinc-200 rounded-xl p-3">
            <audio id="qAudio" preload="auto" src="${audioUrl}"></audio>
            <button id="qAudioPlay" type="button" class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-blue-600 text-white text-xs font-semibold hover:bg-blue-700">
              <span>▶ Listen to Question</span>
            </button>
            <span class="text-xs text-zinc-500">Audio plays automatically</span>
          </div>
        ` : ''}

        <h4 class="text-base font-bold text-zinc-900 mb-4 leading-snug">${q.question || 'Listen to the question and choose the best answer.'}</h4>

        <div id="optionsList" class="space-y-2.5 mb-6">
          ${renderOptions(q, selectedOpt, answerRevealed)}
        </div>

        <div id="explanationBox" class="hidden mb-6 p-4 rounded-xl bg-zinc-50 border border-zinc-200 text-sm text-zinc-800 whitespace-pre-line leading-relaxed"></div>

        <div class="flex items-center justify-between pt-2 border-t border-zinc-100">
          <button id="showAnswerBtn" type="button" class="px-4 py-2 rounded-xl border border-zinc-300 bg-white hover:bg-zinc-50 text-zinc-700 font-semibold text-xs">
            Show Answer
          </button>
          <div class="flex items-center gap-2">
            ${onPrev ? '<button id="prevQBtn" type="button" class="px-4 py-2 rounded-xl border border-zinc-300 bg-white hover:bg-zinc-50 text-zinc-700 font-semibold text-sm">← Prev</button>' : ''}
            <button id="nextQBtn" type="button" class="px-6 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-semibold text-sm shadow-sm">
              ${qIndex >= totalQ ? 'Finish Practice' : 'Next →'}
            </button>
          </div>
        </div>
      </div>
    `;

    const timerValEl = container.querySelector('#timerValue');
    const timerBadge = container.querySelector('#questionTimerBadge');
    startCountdown(30, (rem) => {
      if (timerValEl) timerValEl.textContent = `${rem}s`;
      if (rem <= 5 && timerBadge) {
        timerBadge.className = 'flex items-center gap-1.5 px-3 py-1 rounded-full bg-red-50 border border-red-200 text-red-700 text-xs font-bold tabular-nums animate-pulse';
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
      optionsList.innerHTML = renderOptions(q, selectedOpt, answerRevealed);
      bindOptionClicks();
      if (answerRevealed && q.explanation) {
        expBox.textContent = q.explanation;
        expBox.classList.remove('hidden');
      } else {
        expBox.classList.add('hidden');
      }
    });

    const nextQBtn = container.querySelector('#nextQBtn');
    nextQBtn.addEventListener('click', () => {
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

  // --- Reading Practice Interactive Hook ---
  function initReadingInteractive() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/reading_') && !window.location.pathname.includes('practices_reading_')) return;

    const allQ = extractFlightJson('Question', '[', ']');
    const fallbackQ = extractFlightJson('questions', '[', ']');
    const questions = (Array.isArray(allQ) && allQ.length >= (Array.isArray(fallbackQ) ? fallbackQ.length : 0)) ? allQ : fallbackQ;
    if (!Array.isArray(questions) || questions.length === 0) return;

    const selects = [];
    // Replace all unhydrated Radix question dropdown buttons (Q1-Q6 and inline letter blanks Q7-Q11)
    const questionBtns = Array.from(document.querySelectorAll('button[aria-haspopup="dialog"].font-practice'));
    questionBtns.forEach((btn, idx) => {
      const li = btn.closest('li');
      const numSpan = li ? li.querySelector('span.font-semibold') : null;
      const rawBtnNum = (btn.textContent || '').replace(/[^0-9]/g, '');
      const numText = (numSpan ? numSpan.textContent.replace(/[^0-9]/g, '') : '') || rawBtnNum || String(idx + 1);
      const q = questions[idx];
      if (!q) return;

      const sel = document.createElement('select');
      sel.setAttribute('data-q-num', numText);
      sel.className = 'inline-flex h-7 max-w-full rounded-md border border-zinc-400 bg-white px-2 text-[14px] font-medium text-zinc-800 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-600 cursor-pointer align-middle mx-0.5';
      const defaultOpt = document.createElement('option');
      defaultOpt.value = '';
      defaultOpt.textContent = `${numText}. Select...`;
      sel.appendChild(defaultOpt);

      for (let i = 1; i <= 8; i++) {
        const txt = q[`option${i}`];
        if (!txt) continue;
        const opt = document.createElement('option');
        opt.value = String(i);
        opt.textContent = `${i}. ${txt}`;
        sel.appendChild(opt);
      }

      const host = li || btn.closest('p') || btn.parentElement;
      btn.parentNode.replaceChild(sel, btn);
      selects.push({ sel, q, num: numText, li: host });
    });

    // Wire "Answers Key" and "Show Answers" buttons
    const answerButtons = Array.from(document.querySelectorAll('button')).filter(b => {
      const t = (b.textContent || '').trim();
      return t.includes('Answers Key') || t.includes('Show Answers') || t.includes('Check Answers');
    });

    function revealReadingAnswers() {
      let score = 0;
      selects.forEach(({ sel, q, li }) => {
        const chosen = sel.value;
        const correct = String(q.answer || '');
        if (chosen && chosen === correct) {
          score++;
          sel.style.borderColor = '#10b981';
          sel.style.backgroundColor = '#ecfdf5';
        } else {
          sel.style.borderColor = '#ef4444';
          sel.style.backgroundColor = '#fef2f2';
        }
        let hint = li.querySelector('.celpip-reading-hint');
        if (!hint) {
          hint = document.createElement('div');
          hint.className = 'celpip-reading-hint mt-1.5 mb-2 p-2.5 rounded-lg bg-zinc-50 border border-zinc-200 text-xs text-zinc-700 leading-relaxed whitespace-pre-line';
          li.appendChild(hint);
        }
        const correctText = q[`option${correct}`] || `Option ${correct}`;
        hint.innerHTML = `<strong class="text-emerald-700">Answer: ${correct}. ${correctText}</strong>${q.explanation ? `\n${q.explanation}` : ''}`;
      });

      // Summary banner at top of question list
      const firstLi = selects[0] && selects[0].li;
      if (firstLi && firstLi.parentNode) {
        let banner = document.getElementById('readingScoreBanner');
        if (!banner) {
          banner = document.createElement('div');
          banner.id = 'readingScoreBanner';
          banner.className = 'mb-4 p-3 rounded-xl bg-blue-50 border border-blue-200 text-sm font-bold text-blue-900';
          firstLi.parentNode.insertBefore(banner, firstLi);
        }
        banner.textContent = `Answer Key Revealed — Score: ${score} / ${selects.length}`;
      }
    }

    answerButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        revealReadingAnswers();
      });
    });
  }

  // --- Shared Sample / Analysis Extractor for Writing & Speaking ---
  function renderTierSamplePanel(anchorEl, samplesData, analysisData, userDraftFn) {
    const tiers = (samplesData && samplesData.tiers) || {};
    const tierMap = {
      Weak: tiers.low,
      Normal: tiers.medium,
      Top: tiers.high,
    };

    const allButtons = Array.from(document.querySelectorAll('button'));
    const tierBtns = allButtons.filter(b => ['Weak', 'Normal', 'Top'].includes((b.textContent || '').trim()));
    const analysisBtns = allButtons.filter(b => (b.textContent || '').trim().includes('Sample analysis'));
    const scoreBtns = allButtons.filter(b => (b.textContent || '').trim().includes('Score my answer'));

    let viewer = document.getElementById('celpipSampleViewer');
    if (!viewer && anchorEl) {
      viewer = document.createElement('div');
      viewer.id = 'celpipSampleViewer';
      viewer.className = 'hidden mt-3 p-4 rounded-xl bg-zinc-50 border border-zinc-200 text-sm text-zinc-800 leading-relaxed whitespace-pre-line';
      anchorEl.appendChild(viewer);
    }

    function showContent(title, badge, bodyText, tone = 'blue') {
      if (!viewer) return;
      viewer.classList.remove('hidden');
      const colors = tone === 'emerald' ? 'bg-emerald-100 text-emerald-800' : 'bg-blue-100 text-blue-800';
      viewer.innerHTML = `
        <div class="flex items-center justify-between mb-2">
          <strong class="text-zinc-900">${title}</strong>
          ${badge ? `<span class="px-2.5 py-0.5 rounded-full text-xs font-bold ${colors}">${badge}</span>` : ''}
        </div>
        <div class="text-zinc-700 whitespace-pre-line">${bodyText}</div>
      `;
    }

    tierBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const label = (btn.textContent || '').trim();
        tierBtns.forEach(t => t.setAttribute('aria-selected', t === btn ? 'true' : 'false'));
        const item = tierMap[label];
        if (item && item.text) {
          const resolvedText = resolveFlightRef(item.text);
          showContent(`${label} Sample Response`, item.band ? `CLB ${item.band}` : label, resolvedText);
        } else {
          showContent(`${label} Sample Response`, label, 'Sample response loaded for this task.');
        }
      });
    });

    analysisBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const rawFb = (analysisData && analysisData.assessment && (analysisData.assessment.review || analysisData.assessment.feedback));
        const fb = (rawFb ? resolveFlightRef(rawFb) : null)
          || 'Focus on covering all prompt bullets clearly, maintaining consistent tone/register, using varied complex sentences, and staying close to the target word/time limit.';
        const sc = (analysisData && analysisData.score)
          ? `Grammar: ${analysisData.score.grammar}/12 · Coherence: ${analysisData.score.coherence}/12 · Vocabulary: ${analysisData.score.vocabulary}/12 · Fulfillment: ${analysisData.score.fulfillment}/12`
          : 'CLB 9+ Criteria Check';
        showContent('Sample Analysis & Rubric', sc, fb, 'emerald');
      });
    });

    scoreBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const text = userDraftFn ? userDraftFn() : '';
        const words = text.trim() ? text.trim().split(/\s+/).length : 0;
        const paras = text.trim() ? text.trim().split(/\n+/).filter(Boolean).length : 0;
        let est = 'CLB 5–6 (Keep expanding)';
        if (words >= 145 && words <= 215 && paras >= 3) est = 'CLB 9–10+ (Strong structure & length)';
        else if (words >= 110) est = 'CLB 7–8 (Good length — verify all prompt points)';
        showContent(
          'Instant Draft Evaluation',
          `${words} words · ${paras} paragraphs`,
          `Estimated Band: ${est}\n\nTarget Range: 150–200 words organized into clear opening, body paragraphs covering every bullet point, and polite sign-off.`,
          'emerald'
        );
      });
    });
  }

  // --- Writing Practice Native Hook (No Duplicate Lower Box) ---
  function initWritingEditor() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/writing_') && !window.location.pathname.includes('practices_writing_')) return;

    const textarea = document.querySelector('textarea');
    const samplesData = extractFlightJson('samples', '{', '}');
    const analysisData = extractFlightJson('analysis', '{', '}');

    // Hook built-in word counter (<p><span>0</span> / 150–200 words</p>)
    if (textarea) {
      const updateWordCount = () => {
        const words = textarea.value.trim() ? textarea.value.trim().split(/\s+/).length : 0;
        const candidates = Array.from(document.querySelectorAll('p, div')).filter(el =>
          /\d+\s*\/\s*150[-–]200\s*words/i.test((el.textContent || '').trim())
        );
        candidates.forEach(el => {
          const numSpan = el.querySelector('span');
          if (numSpan) {
            numSpan.textContent = String(words);
          } else {
            el.textContent = `${words} / 150–200 words`;
          }
        });
      };
      textarea.addEventListener('input', updateWordCount);
      updateWordCount();
    }

    // Find anchor for sample viewer near the Weak/Normal/Top bar or below textarea
    const weakBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Weak');
    const anchor = (weakBtn && weakBtn.parentElement && weakBtn.parentElement.parentElement)
      || (textarea && textarea.parentElement)
      || document.querySelector('main');

    renderTierSamplePanel(anchor, samplesData, analysisData, () => (textarea ? textarea.value : ''));
  }

  // --- Speaking Practice Native Hook (No Duplicate Lower Box) ---
  function initSpeakingRecorder() {
    if (typeof window === 'undefined' || !window.location || !window.location.pathname) return;
    if (!window.location.pathname.includes('/practices/speaking_') && !window.location.pathname.includes('practices_speaking_')) return;

    const samplesData = extractFlightJson('samples', '{', '}');
    const analysisData = extractFlightJson('analysis', '{', '}');

    // Populate empty mic icon box next to Preparation Time (<span class="flex h-14 w-14 ...">)
    // Re-run after React hydration settles so it isn't cleared
    const ensureMicIcon = () => {
      document.querySelectorAll('span.h-14.w-14, div.h-14.w-14').forEach(el => {
        const curSvg = el.querySelector('svg');
        if (!el.textContent.trim() && (!curSvg || curSvg.getBoundingClientRect().width === 0)) {
          el.innerHTML = '<svg class="w-6 h-6 text-purple-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>';
        }
      });
    };
    ensureMicIcon();
    setTimeout(ensureMicIcon, 250);
    setTimeout(ensureMicIcon, 800);

    // Inject interactive Prep -> Speaking countdown control into the upper practice card
    const prepLabel = Array.from(document.querySelectorAll('span, p, div')).find(el =>
      el.children.length === 0 && (el.textContent || '').includes('Preparation Time')
    );
    if (prepLabel && !document.getElementById('speakingNativeTimerBar')) {
      const bar = document.createElement('div');
      bar.id = 'speakingNativeTimerBar';
      bar.className = 'mt-3 flex flex-wrap items-center gap-3 p-3 rounded-xl bg-purple-50 border border-purple-200';
      bar.innerHTML = `
        <button id="speakingStartTimerBtn" type="button" style="background-color:#7e22ce;color:#ffffff;" class="px-4 py-1.5 rounded-lg text-xs font-bold shadow-sm hover:opacity-95 cursor-pointer">
          ▶ Start Prep &amp; Speak Timer
        </button>
        <span id="speakingTimerStatus" class="text-xs font-bold text-purple-900 tabular-nums">Ready: 30s Prep → 60s Speaking</span>
      `;
      const hostCard = prepLabel.closest('.border') || prepLabel.parentElement;
      if (hostCard) hostCard.appendChild(bar);

      const startTimerBtn = bar.querySelector('#speakingStartTimerBtn');
      const statusEl = bar.querySelector('#speakingTimerStatus');
      let timerRef = null;
      startTimerBtn.addEventListener('click', () => {
        if (timerRef) clearInterval(timerRef);
        let prep = 30;
        statusEl.textContent = `Prep Time: ${formatTime(prep)}`;
        timerRef = setInterval(() => {
          prep--;
          if (prep > 0) {
            statusEl.textContent = `Prep Time: ${formatTime(prep)}`;
          } else {
            clearInterval(timerRef);
            let speak = 60;
            statusEl.textContent = `🎤 Speaking Now: ${formatTime(speak)}`;
            timerRef = setInterval(() => {
              speak--;
              if (speak > 0) {
                statusEl.textContent = `🎤 Speaking Now: ${formatTime(speak)}`;
              } else {
                clearInterval(timerRef);
                statusEl.textContent = '✓ Time Complete! Review Top Sample or Analysis.';
              }
            }, 1000);
          }
        }, 1000);
      });
    }

    // Wire Skip button
    const skipBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Skip');
    if (skipBtn) {
      skipBtn.addEventListener('click', () => {
        const statusEl = document.getElementById('speakingTimerStatus');
        if (statusEl) statusEl.textContent = '🎤 Prep skipped — Speaking Phase (60s)';
      });
    }

    const weakBtn = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').trim() === 'Weak');
    const anchor = (weakBtn && weakBtn.parentElement && weakBtn.parentElement.parentElement) || document.querySelector('main');
    renderTierSamplePanel(anchor, samplesData, analysisData, null);
  }

  // --- Part-Page Tabs & Filters (/parts/*) ---
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
          if (active) {
            t.classList.add('bg-white', 'text-zinc-900', 'shadow-sm');
          } else {
            t.classList.remove('bg-white', 'text-zinc-900', 'shadow-sm');
          }
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

    // Wire Free only toggle button
    const freeToggle = Array.from(document.querySelectorAll('button')).find(b => (b.textContent || '').includes('Free only'));
    if (freeToggle) {
      freeToggle.addEventListener('click', () => {
        const pressed = freeToggle.getAttribute('aria-pressed') === 'true';
        freeToggle.setAttribute('aria-pressed', pressed ? 'false' : 'true');
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

    const allButtons = Array.from(document.querySelectorAll('button'));
    return allButtons.filter(btn => {
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

    const startBtns = findStartButtons();
    const data = extractPracticeData();
    if (startBtns.length && data && data.steps) {
      startBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
          e.preventDefault();
          // Hide the entire outer instructions/intro card cleanly
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
