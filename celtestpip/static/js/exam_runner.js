// celtestpip/static/js/exam_runner.js
// Authentic interactive exam runner for CELTESTPIP replica

const CELPIP_PARTS = [
  { num: 1, code: "L1", skill: "LISTENING", name: "Listening to Problem Solving", color: "emerald", time: 480 },
  { num: 2, code: "L2", skill: "LISTENING", name: "Listening to a Daily Life Conversation", color: "emerald", time: 480 },
  { num: 3, code: "L3", skill: "LISTENING", name: "Listening for Information", color: "emerald", time: 480 },
  { num: 4, code: "L4", skill: "LISTENING", name: "Listening to a News Item", color: "emerald", time: 480 },
  { num: 5, code: "L5", skill: "LISTENING", name: "Listening to a Discussion", color: "emerald", time: 480 },
  { num: 6, code: "L6", skill: "LISTENING", name: "Listening for Viewpoints", color: "emerald", time: 480 },
  { num: 7, code: "R1", skill: "READING", name: "Reading Correspondence", color: "sky", time: 660 },
  { num: 8, code: "R2", skill: "READING", name: "Reading to Apply a Diagram", color: "sky", time: 660 },
  { num: 9, code: "R3", skill: "READING", name: "Reading for Information", color: "sky", time: 660 },
  { num: 10, code: "R4", skill: "READING", name: "Reading for Viewpoints", color: "sky", time: 660 },
  { num: 11, code: "W1", skill: "WRITING", name: "Writing an Email", color: "amber", time: 1620 },
  { num: 12, code: "W2", skill: "WRITING", name: "Responding to Survey Questions", color: "amber", time: 1560 },
  { num: 13, code: "S1", skill: "SPEAKING", name: "Giving Advice", color: "purple", time: 120 },
  { num: 14, code: "S2", skill: "SPEAKING", name: "Talking about a Personal Experience", color: "purple", time: 120 },
  { num: 15, code: "S3", skill: "SPEAKING", name: "Describing a Scene", color: "purple", time: 120 },
  { num: 16, code: "S4", skill: "SPEAKING", name: "Making Predictions", color: "purple", time: 120 },
  { num: 17, code: "S5", skill: "SPEAKING", name: "Comparing and Persuading", color: "purple", time: 120 },
  { num: 18, code: "S6", skill: "SPEAKING", name: "Dealing with a Difficult Situation", color: "purple", time: 120 },
  { num: 19, code: "S7", skill: "SPEAKING", name: "Expressing Opinions", color: "purple", time: 120 },
  { num: 20, code: "S8", skill: "SPEAKING", name: "Describing an Unusual Situation", color: "purple", time: 120 },
];

function escapeHtml(str) {
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

function resolveMediaUrl(url) {
  if (!url) return "";
  if (url.startsWith("https://u108saydmkdhqew3.public.blob.vercel-storage.com/")) {
    const path = url.replace("https://u108saydmkdhqew3.public.blob.vercel-storage.com/", "");
    return `/media/${path}`;
  }
  return url;
}

function formatTime(seconds) {
  const mins = Math.floor(seconds / 60);
  const secs = Math.floor(seconds % 60);
  return `${mins}:${secs.toString().padStart(2, "0")}`;
}

document.addEventListener("DOMContentLoaded", async () => {
  const pathParts = window.location.pathname.split("/").filter(Boolean);
  let examId = "exam1";
  let partNumber = 1;
  const isResultsView = window.location.pathname.includes("/results") || window.location.search.includes("results");

  for (let i = 0; i < pathParts.length; i++) {
    const p = pathParts[i];
    if (p !== "exams" && p.startsWith("exam")) {
      examId = p;
    } else if (i > 0 && pathParts[i - 1] === "exams" && /^\d+$/.test(p)) {
      examId = "exam" + p;
    } else if (p === "part" && pathParts[i + 1]) {
      partNumber = parseInt(pathParts[i + 1], 10) || 1;
    } else if (p.startsWith("part")) {
      const match = p.match(/\d+/);
      if (match) partNumber = parseInt(match[0], 10);
    }
  }

  if (!examId.startsWith("exam") && /^\d+$/.test(examId)) {
    examId = "exam" + examId;
  }

  // Parse query params if partNumber in query
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("partNumber")) {
    const match = urlParams.get("partNumber").match(/\d+/);
    if (match) partNumber = parseInt(match[0], 10);
  }

  const currentMeta = CELPIP_PARTS.find(p => p.num === partNumber) || CELPIP_PARTS[0];

  // Headings & Header info
  const examTitleElem = document.getElementById("examTitle");
  if (examTitleElem) examTitleElem.innerText = examId.toUpperCase();

  const partHeadingElem = document.getElementById("partHeading");
  if (partHeadingElem) {
    const shortNum = currentMeta.num > 12 ? currentMeta.num - 12 : (currentMeta.num > 10 ? currentMeta.num - 10 : (currentMeta.num > 6 ? currentMeta.num - 6 : currentMeta.num));
    partHeadingElem.innerText = `${currentMeta.skill} Part ${shortNum}: ${currentMeta.name}`;
  }

  const instructionHeader = document.getElementById("instructionHeader");
  if (instructionHeader) instructionHeader.innerText = currentMeta.name;

  // 4-column Part Selector Popover
  const partsList = document.getElementById("partsList");
  if (partsList) {
    const sections = [
      { name: "Listening", color: "emerald", parts: CELPIP_PARTS.slice(0, 6) },
      { name: "Reading", color: "sky", parts: CELPIP_PARTS.slice(6, 10) },
      { name: "Writing", color: "amber", parts: CELPIP_PARTS.slice(10, 12) },
      { name: "Speaking", color: "purple", parts: CELPIP_PARTS.slice(12, 20) },
    ];

    partsList.innerHTML = sections.map(sec => `
      <div class="bg-white p-3 transition-colors">
        <div class="flex items-center gap-2.5 px-2 py-2 mb-1.5 rounded-xl bg-${sec.color}-50/50">
          <span class="text-[13px] font-bold text-${sec.color}-700">${sec.name}</span>
        </div>
        <div class="space-y-1">
          ${sec.parts.map(p => {
            const isActive = p.num === partNumber;
            const activeClass = isActive ? `bg-${sec.color}-100 font-bold text-${sec.color}-900` : `text-zinc-600 hover:text-zinc-900 hover:bg-zinc-50`;
            return `
              <a href="/exams/${examId}/part/${p.num}" class="part-btn flex items-center gap-2 px-2 py-1.5 rounded-lg text-xs transition-colors ${activeClass}">
                <span class="text-[10px] font-bold rounded px-1.5 py-0.5 border border-zinc-200 bg-white text-${sec.color}-700 shrink-0">${p.code}</span>
                <span class="truncate">${p.name}</span>
              </a>
            `;
          }).join("")}
        </div>
      </div>
    `).join("");
  }

  // Toggle Part Popover
  const partSelectorBtn = document.getElementById("partSelectorBtn");
  const partMenuPopover = document.getElementById("partMenuPopover");
  if (partSelectorBtn && partMenuPopover) {
    partSelectorBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      partMenuPopover.classList.toggle("hidden");
    });
    document.addEventListener("click", (e) => {
      if (!partMenuPopover.contains(e.target) && e.target !== partSelectorBtn) {
        partMenuPopover.classList.add("hidden");
      }
    });
  }

  // Timer Countdown state
  let timeLeft = currentMeta.time || 600;
  let timerInterval = null;
  const timerElem = document.getElementById("timer");
  const timerDisplay = document.getElementById("timerDisplay") || timerElem;

  const updateTimerDisplay = () => {
    const mins = Math.floor(timeLeft / 60);
    const secs = timeLeft % 60;
    if (timerDisplay) {
      timerDisplay.innerText = `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
    }
    if (timeLeft > 0) {
      timeLeft--;
    } else if (timerInterval) {
      clearInterval(timerInterval);
    }
  };

  const startTimer = () => {
    if (!timerInterval) {
      if (timerElem) timerElem.classList.remove("hidden");
      if (timerElem) timerElem.classList.add("flex");
      updateTimerDisplay();
      timerInterval = setInterval(updateTimerDisplay, 1000);
    }
  };

  // State Management for Interactive Engine
  let examData = null;
  let questions = [];
  let userAnswers = {};
  let currentStage = isResultsView ? "results" : "instructions"; // "instructions" | "stimulus" | "questions" | "writing" | "speaking" | "results"
  let currentQuestionIndex = 0;
  let totalSteps = 10;

  // Audio Elements & State
  const questionAudioElem = document.getElementById("questionAudioElem");
  const qAudioPlayBtn = document.getElementById("qAudioPlayBtn");
  const qAudioPlayIcon = document.getElementById("qAudioPlayIcon");
  const qAudioSeekBar = document.getElementById("qAudioSeekBar");
  const qAudioProgressFill = document.getElementById("qAudioProgressFill");
  const qAudioSeekThumb = document.getElementById("qAudioSeekThumb");
  const qAudioCurrentTime = document.getElementById("qAudioCurrentTime");
  const qAudioDuration = document.getElementById("qAudioDuration");
  const qAudioBack10Btn = document.getElementById("qAudioBack10Btn");
  const qAudioFwd10Btn = document.getElementById("qAudioFwd10Btn");
  const qAudioSpeedBtn = document.getElementById("qAudioSpeedBtn");

  const speeds = [1, 1.25, 1.5, 0.75];
  let currentSpeedIdx = 0;

  // Custom Audio Controls
  if (questionAudioElem) {
    const updatePlayState = (isPlaying) => {
      if (!qAudioPlayIcon) return;
      if (isPlaying) {
        qAudioPlayIcon.innerHTML = `<line x1="10" x2="10" y1="4" y2="20"></line><line x1="14" x2="14" y1="4" y2="20"></line>`;
        qAudioPlayIcon.setAttribute("class", "lucide lucide-pause h-5 w-5");
      } else {
        qAudioPlayIcon.innerHTML = `<path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"></path>`;
        qAudioPlayIcon.setAttribute("class", "lucide lucide-play h-5 w-5 translate-x-px");
      }
    };

    if (qAudioPlayBtn) {
      qAudioPlayBtn.addEventListener("click", () => {
        if (questionAudioElem.paused) {
          questionAudioElem.play().catch(console.error);
        } else {
          questionAudioElem.pause();
        }
      });
    }

    questionAudioElem.addEventListener("play", () => updatePlayState(true));
    questionAudioElem.addEventListener("pause", () => updatePlayState(false));

    questionAudioElem.addEventListener("timeupdate", () => {
      const cur = questionAudioElem.currentTime || 0;
      const dur = questionAudioElem.duration || 1;
      if (qAudioCurrentTime) qAudioCurrentTime.innerText = formatTime(cur);
      const pct = Math.min(100, Math.max(0, (cur / dur) * 100));
      if (qAudioProgressFill) qAudioProgressFill.style.width = `${pct}%`;
      if (qAudioSeekThumb) qAudioSeekThumb.style.left = `${pct}%`;
    });

    questionAudioElem.addEventListener("loadedmetadata", () => {
      const dur = questionAudioElem.duration || 0;
      if (qAudioDuration) qAudioDuration.innerText = formatTime(dur);
    });

    if (qAudioSeekBar) {
      const handleSeek = (e) => {
        const rect = qAudioSeekBar.getBoundingClientRect();
        const clientX = e.touches ? e.touches[0].clientX : e.clientX;
        const clickPos = Math.max(0, Math.min(rect.width, clientX - rect.left));
        const pct = clickPos / rect.width;
        if (questionAudioElem.duration) {
          questionAudioElem.currentTime = pct * questionAudioElem.duration;
        }
      };
      qAudioSeekBar.addEventListener("click", handleSeek);
    }

    if (qAudioBack10Btn) {
      qAudioBack10Btn.addEventListener("click", () => {
        questionAudioElem.currentTime = Math.max(0, questionAudioElem.currentTime - 10);
      });
    }

    if (qAudioFwd10Btn) {
      qAudioFwd10Btn.addEventListener("click", () => {
        questionAudioElem.currentTime = Math.min(questionAudioElem.duration || 0, questionAudioElem.currentTime + 10);
      });
    }

    if (qAudioSpeedBtn) {
      qAudioSpeedBtn.addEventListener("click", () => {
        currentSpeedIdx = (currentSpeedIdx + 1) % speeds.length;
        const spd = speeds[currentSpeedIdx];
        questionAudioElem.playbackRate = spd;
        qAudioSpeedBtn.innerText = `${spd}x`;
      });
    }
  }

  // Accordion Toggle for Transcripts
  const toggleTranscriptBtn = document.getElementById("toggleTranscriptBtn");
  const transcriptBox = document.getElementById("transcriptBox");
  const transcriptChevron = document.getElementById("transcriptChevron");
  if (toggleTranscriptBtn && transcriptBox) {
    toggleTranscriptBtn.addEventListener("click", () => {
      const isHidden = transcriptBox.classList.toggle("hidden");
      if (transcriptChevron) {
        if (!isHidden) {
          transcriptChevron.classList.add("rotate-180");
        } else {
          transcriptChevron.classList.remove("rotate-180");
        }
      }
    });
  }

  // Load Part Data from Backend
  try {
    const res = await fetch(`/api/exams/${examId}/part/${partNumber}`);
    if (!res.ok) throw new Error("Exam part not found");
    examData = await res.json();
    questions = examData.questions || [];
    totalSteps = Math.max(3, questions.length + 2);

    if (examData.part_name && partHeadingElem) {
      partHeadingElem.innerText = `${examData.skill} : ${examData.part_name}`;
    }

    // Set stageInstructions bullet points
    const instructionsList = document.getElementById("instructionsList");
    if (instructionsList) {
      let bullets = [
        "You will hear a conversation between two people. The conversation is about a problem that one of them has.",
        "After each section of the conversation, you will hear a question. You will hear the conversation and the questions only once.",
        "Choose the best answer to each question."
      ];
      if (examData.instructions && examData.skill === "LISTENING") {
        bullets = [
          examData.instructions,
          "After each section of the conversation, you will hear a question. You will hear the audio only once.",
          "Choose the best answer to each question."
        ];
      } else if (examData.skill === "READING") {
        bullets = [
          "Read the following message and answer the questions that follow.",
          "You can refer back to the text while answering.",
          "Choose the best option to complete each statement or answer each question."
        ];
      } else if (examData.skill === "WRITING") {
        bullets = [
          examData.instructions || "Read the scenario and write your response.",
          "Keep your response within the suggested word count (150-200 words).",
          "You will receive an instant AI assessment and CLB benchmark."
        ];
      } else if (examData.skill === "SPEAKING") {
        bullets = [
          examData.instructions || "Speak your answer clearly into the microphone.",
          "You will have 30 seconds to prepare and 60 seconds to speak.",
          "Review the sample high-scoring response upon completion."
        ];
      }
      instructionsList.innerHTML = bullets.map(b => `
        <li class="flex items-start gap-3 py-3">
          <span class="mt-[9px] h-1.5 w-1.5 shrink-0 rounded-full bg-zinc-400"></span>
          <span>${escapeHtml(b)}</span>
        </li>
      `).join("");
    }

    // Render Stage Function
    const renderStage = () => {
      const stageInstructions = document.getElementById("stageInstructions");
      const stageStimulus = document.getElementById("stageStimulus");
      const stageQuestions = document.getElementById("stageQuestions");
      const stageWriting = document.getElementById("stageWriting");
      const stageSpeaking = document.getElementById("stageSpeaking");
      const stageResults = document.getElementById("stageResults");
      const progressBar = document.getElementById("progressBar");
      const headerNextBtn = document.getElementById("headerNextBtn");
      const footerBackBtn = document.getElementById("footerBackBtn");
      const submitBtn = document.getElementById("submitBtn");

      // Hide all stages first
      if (stageInstructions) stageInstructions.classList.add("hidden");
      if (stageStimulus) stageStimulus.classList.add("hidden");
      if (stageQuestions) stageQuestions.classList.add("hidden");
      if (stageWriting) stageWriting.classList.add("hidden");
      if (stageSpeaking) stageSpeaking.classList.add("hidden");
      if (stageResults) stageResults.classList.add("hidden");

      if (currentStage === "instructions") {
        if (stageInstructions) stageInstructions.classList.remove("hidden");
        if (progressBar) progressBar.style.width = "0%";
        if (headerNextBtn) {
          headerNextBtn.classList.remove("hidden");
          headerNextBtn.innerHTML = `Start <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>`;
        }
        if (footerBackBtn) {
          footerBackBtn.onclick = () => { window.location.href = "/exams"; };
        }
        if (submitBtn) submitBtn.classList.add("hidden");
        return;
      }

      startTimer();

      if (currentStage === "stimulus") {
        if (stageStimulus) stageStimulus.classList.remove("hidden");
        if (progressBar) progressBar.style.width = `${(1 / totalSteps) * 100}%`;

        // Fill stimulus text
        const stimulusPromptText = document.getElementById("stimulusPromptText");
        if (stimulusPromptText) {
          stimulusPromptText.innerText = examData.instructions || "Listen to the following conversation and answer the questions.";
        }

        // Fill stimulus image
        const partImage = document.getElementById("partImage");
        if (examData.image_url && partImage) {
          partImage.classList.remove("hidden");
          partImage.src = `/_next/image?url=${encodeURIComponent(examData.image_url)}&w=3840&q=75`;
        }

        // Stimulus audio container (hidden to match live pixel-for-pixel)
        const stimulusAudioSec = document.getElementById("stimulusAudioSection");
        if (stimulusAudioSec) stimulusAudioSec.classList.add("hidden");

        if (headerNextBtn) {
          headerNextBtn.classList.remove("hidden");
          headerNextBtn.innerHTML = `Next <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>`;
        }
        if (footerBackBtn) {
          footerBackBtn.onclick = () => { currentStage = "instructions"; renderStage(); };
        }
        if (submitBtn) submitBtn.classList.add("hidden");
        return;
      }

      if (currentStage === "questions") {
        if (stageQuestions) stageQuestions.classList.remove("hidden");
        const stepNum = currentQuestionIndex + 2;
        if (progressBar) progressBar.style.width = `${(stepNum / totalSteps) * 100}%`;

        const q = questions[currentQuestionIndex];
        if (!q) return;

        // Left Pane setup
        const questionLeftHeader = document.getElementById("questionLeftHeader");
        const audioSection = document.getElementById("audioSection");
        const readingPassageSection = document.getElementById("readingPassageSection");

        if (examData.skill === "READING") {
          if (questionLeftHeader) questionLeftHeader.innerText = "Read the passage.";
          if (audioSection) audioSection.classList.add("hidden");
          if (readingPassageSection) {
            readingPassageSection.classList.remove("hidden");
            readingPassageSection.innerHTML = escapeHtml(examData.instructions || "").replace(/\n/g, "<br/>");
          }
        } else {
          if (questionLeftHeader) questionLeftHeader.innerText = "Listen to the question.";
          if (readingPassageSection) readingPassageSection.classList.add("hidden");
          if (audioSection) audioSection.classList.remove("hidden");

          // Load audio for question
          const audioSrc = resolveMediaUrl(q.audio_url || (examData.audio_urls && examData.audio_urls[0]));
          if (questionAudioElem && audioSrc && questionAudioElem.src !== audioSrc) {
            questionAudioElem.src = audioSrc;
            questionAudioElem.load();
          }
        }

        // Fill transcripts
        const transcriptContent = document.getElementById("transcriptContent");
        if (transcriptContent && examData.transcripts && examData.transcripts.length > 0) {
          transcriptContent.innerHTML = examData.transcripts.map(t => `<p class="whitespace-pre-line mb-3 text-zinc-800">${escapeHtml(t)}</p>`).join("");
        }

        // Right Pane setup
        const questionNumberLabel = document.getElementById("questionNumberLabel");
        if (questionNumberLabel) {
          questionNumberLabel.innerText = `Question ${currentQuestionIndex + 1} of ${questions.length}`;
        }

        const questionPromptHeading = document.getElementById("questionPromptHeading");
        if (questionPromptHeading) {
          questionPromptHeading.innerText = q.question_text || "Choose the best answer to each question.";
        }

        // Render radio options
        const questionsContainer = document.getElementById("questionsContainer");
        if (questionsContainer) {
          const selectedVal = userAnswers[q.id];
          questionsContainer.innerHTML = `
            <div aria-label="Options" class="flex flex-col divide-y divide-zinc-300/80" role="radiogroup">
              ${q.options.map((optText, oIdx) => {
                const optNum = String(oIdx + 1);
                const isChecked = selectedVal === optNum;
                return `
                  <div class="flex flex-col">
                    <button type="button" role="radio" aria-checked="${isChecked}" data-opt="${optNum}"
                      class="option-radio-btn flex w-full items-start gap-2.5 rounded-lg px-2.5 py-2.5 text-left transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-zinc-900 cursor-pointer ${isChecked ? 'bg-white shadow-sm ring-1 ring-zinc-300/80' : 'hover:bg-white/60'}">
                      ${isChecked ? `
                        <svg class="lucide lucide-circle-dot mt-0.5 h-4 w-4 shrink-0 text-blue-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"></circle>
                          <circle cx="12" cy="12" r="4" fill="currentColor"></circle>
                        </svg>
                      ` : `
                        <svg class="lucide lucide-circle mt-0.5 h-4 w-4 shrink-0 text-zinc-400" viewBox="0 0 24 24" fill="white" stroke="currentColor" stroke-width="2">
                          <circle cx="12" cy="12" r="10"></circle>
                        </svg>
                      `}
                      <span class="font-practice text-[14px] leading-6 text-zinc-800">${escapeHtml(optText)}</span>
                    </button>
                  </div>
                `;
              }).join("")}
            </div>
          `;

          // Bind option selection
          questionsContainer.querySelectorAll(".option-radio-btn").forEach(btn => {
            btn.addEventListener("click", () => {
              userAnswers[q.id] = btn.getAttribute("data-opt");
              renderStage();
            });
          });
        }

        // Footer & Header Next button
        const isLastQuestion = currentQuestionIndex === questions.length - 1;
        if (headerNextBtn) {
          headerNextBtn.classList.remove("hidden");
          if (isLastQuestion) {
            headerNextBtn.innerHTML = `Submit`;
          } else {
            headerNextBtn.innerHTML = `Next <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>`;
          }
        }

        if (footerBackBtn) {
          footerBackBtn.onclick = () => {
            if (currentQuestionIndex > 0) {
              currentQuestionIndex--;
              renderStage();
            } else {
              currentStage = examData.image_url || (examData.audio_urls && examData.audio_urls.length > 0) ? "stimulus" : "instructions";
              renderStage();
            }
          };
        }

        if (submitBtn) {
          if (isLastQuestion) {
            submitBtn.classList.remove("hidden");
          } else {
            submitBtn.classList.add("hidden");
          }
        }
        return;
      }

      if (currentStage === "writing") {
        if (stageWriting) stageWriting.classList.remove("hidden");
        const writingPromptTitle = document.getElementById("writingPromptTitle");
        const writingPromptText = document.getElementById("writingPromptText");
        const writingWordCount = document.getElementById("writingWordCount");
        const writingTextarea = document.getElementById("writingTextarea");
        const writingModelAnswerBtn = document.getElementById("writingModelAnswerBtn");

        if (writingPromptTitle) writingPromptTitle.innerText = examData.part_name || "Writing Task";
        if (writingPromptText) writingPromptText.innerText = examData.instructions || "Write your response according to the scenario.";

        if (writingTextarea && writingWordCount) {
          writingTextarea.addEventListener("input", () => {
            const words = writingTextarea.value.trim().split(/\s+/).filter(Boolean).length;
            writingWordCount.innerText = `Words: ${words} / 150-200`;
          });
        }

        if (headerNextBtn) {
          headerNextBtn.innerHTML = `Submit`;
        }
        return;
      }

      if (currentStage === "speaking") {
        if (stageSpeaking) stageSpeaking.classList.remove("hidden");
        const speakingPromptTitle = document.getElementById("speakingPromptTitle");
        const speakingPromptText = document.getElementById("speakingPromptText");
        const speakingStatusText = document.getElementById("speakingStatusText");

        if (speakingPromptTitle) speakingPromptTitle.innerText = examData.part_name || "Speaking Task";
        if (speakingPromptText) speakingPromptText.innerText = examData.instructions || "Speak your answer into the microphone.";

        if (headerNextBtn) {
          headerNextBtn.innerHTML = `Submit`;
        }
        return;
      }

      if (currentStage === "results") {
        if (stageResults) stageResults.classList.remove("hidden");
        if (progressBar) progressBar.style.width = "100%";
        if (headerNextBtn) headerNextBtn.classList.add("hidden");
        if (submitBtn) submitBtn.classList.add("hidden");
        if (timerElem) timerElem.classList.add("hidden");

        // Calculate score
        let score = 0;
        const total = questions.length;
        questions.forEach(q => {
          if (userAnswers[q.id] && String(userAnswers[q.id]).trim() === String(q.correct_answer).trim()) {
            score++;
          }
        });

        // Calculate CLB
        const pct = total > 0 ? (score / total) : 1;
        let clb = "CLB Level 10-12";
        if (pct < 0.5) clb = "CLB Level 4-5";
        else if (pct < 0.65) clb = "CLB Level 6-7";
        else if (pct < 0.8) clb = "CLB Level 8";
        else if (pct < 0.95) clb = "CLB Level 9";

        const scoreDisplay = document.getElementById("scoreDisplay");
        if (scoreDisplay) scoreDisplay.innerText = `${score} / ${total}`;

        const clbDisplay = document.getElementById("clbDisplay");
        if (clbDisplay) clbDisplay.innerText = clb;

        const resultsTitle = document.getElementById("resultsTitle");
        if (resultsTitle) resultsTitle.innerText = `${examData.skill} Part ${partNumber} Results`;

        const resultsSubtitle = document.getElementById("resultsSubtitle");
        if (resultsSubtitle) resultsSubtitle.innerText = `${examId.toUpperCase()} • CELPIP Practice`;

        // Render question review breakdown
        const resultsBreakdown = document.getElementById("resultsBreakdown");
        if (resultsBreakdown) {
          resultsBreakdown.innerHTML = questions.map((q, idx) => {
            const userChoice = userAnswers[q.id];
            const isCorrect = userChoice && String(userChoice).trim() === String(q.correct_answer).trim();
            const correctOptIdx = parseInt(q.correct_answer, 10) - 1;
            const correctText = q.options[correctOptIdx] || "";
            const userOptIdx = userChoice ? parseInt(userChoice, 10) - 1 : -1;
            const userText = userOptIdx >= 0 ? q.options[userOptIdx] : "No answer";

            return `
              <div class="rounded-2xl border ${isCorrect ? 'border-emerald-200 bg-emerald-50/20' : 'border-rose-200 bg-rose-50/20'} p-5">
                <div class="flex items-center justify-between mb-2">
                  <span class="text-xs font-bold uppercase tracking-wider ${isCorrect ? 'text-emerald-700 bg-emerald-100' : 'text-rose-700 bg-rose-100'} px-2.5 py-0.5 rounded-full">
                    ${isCorrect ? '✅ Question ' + (idx + 1) + ' • Correct' : '❌ Question ' + (idx + 1) + ' • Incorrect'}
                  </span>
                  <span class="text-xs font-medium text-zinc-500">1 mark</span>
                </div>
                <h4 class="font-bold text-zinc-900 text-sm mb-3">${escapeHtml(q.question_text)}</h4>
                
                <div class="space-y-2 mb-3 text-xs font-practice">
                  <div class="flex items-center gap-2 p-2.5 rounded-xl border ${isCorrect ? 'border-emerald-400 bg-emerald-50 text-emerald-950 font-semibold' : 'border-rose-300 bg-rose-50 text-rose-950'}">
                    <span class="font-bold">Your answer:</span>
                    <span>${escapeHtml(userText)}</span>
                  </div>
                  ${!isCorrect ? `
                    <div class="flex items-center gap-2 p-2.5 rounded-xl border border-emerald-400 bg-emerald-50 text-emerald-950 font-semibold">
                      <span class="font-bold">Correct answer:</span>
                      <span>${escapeHtml(correctText)}</span>
                    </div>
                  ` : ''}
                </div>

                ${q.explanation ? `
                  <div class="mt-3 p-3.5 rounded-xl bg-white border border-zinc-200 text-xs text-zinc-700 leading-relaxed font-practice whitespace-pre-line">
                    <b class="text-zinc-900 block mb-1">Official Explanation:</b>
                    ${escapeHtml(q.explanation)}
                  </div>
                ` : ''}
              </div>
            `;
          }).join("");
        }

        // Save attempt to server
        fetch("/api/attempts", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            exam_id: examId,
            part_number: partNumber,
            score,
            total_questions: total,
            clb_estimate: clb,
            answers: userAnswers
          })
        }).catch(console.error);

        const retakeBtn = document.getElementById("retakeBtn");
        if (retakeBtn) {
          retakeBtn.onclick = () => {
            userAnswers = {};
            currentQuestionIndex = 0;
            currentStage = "instructions";
            renderStage();
          };
        }
      }
    };

    // Forward Navigation Click Handler
    const advanceNext = () => {
      if (currentStage === "instructions") {
        if (examData.skill === "WRITING") {
          currentStage = "writing";
        } else if (examData.skill === "SPEAKING") {
          currentStage = "speaking";
        } else if (examData.image_url || (examData.audio_urls && examData.audio_urls.length > 0)) {
          currentStage = "stimulus";
        } else {
          currentStage = "questions";
        }
        renderStage();
      } else if (currentStage === "stimulus") {
        currentStage = "questions";
        currentQuestionIndex = 0;
        renderStage();
      } else if (currentStage === "questions") {
        if (currentQuestionIndex < questions.length - 1) {
          currentQuestionIndex++;
          renderStage();
        } else {
          currentStage = "results";
          renderStage();
        }
      } else if (currentStage === "writing" || currentStage === "speaking") {
        currentStage = "results";
        renderStage();
      }
    };

    // Wire Buttons
    const startPracticeBtn = document.getElementById("startPracticeBtn");
    if (startPracticeBtn) startPracticeBtn.addEventListener("click", advanceNext);

    const headerNextBtn = document.getElementById("headerNextBtn");
    if (headerNextBtn) headerNextBtn.addEventListener("click", advanceNext);

    const mobileNextBtn = document.getElementById("mobileNextBtn");
    if (mobileNextBtn) mobileNextBtn.addEventListener("click", advanceNext);

    const submitBtn = document.getElementById("submitBtn");
    if (submitBtn) {
      submitBtn.addEventListener("click", () => {
        currentStage = "results";
        renderStage();
      });
    }

    const showAnswersBtn = document.getElementById("showAnswersBtn");
    if (showAnswersBtn) {
      showAnswersBtn.addEventListener("click", (e) => {
        e.preventDefault();
        currentStage = "results";
        renderStage();
      });
    }

    const mobileAnswersBtn = document.getElementById("mobileAnswersBtn");
    if (mobileAnswersBtn) {
      mobileAnswersBtn.addEventListener("click", (e) => {
        e.preventDefault();
        currentStage = "results";
        renderStage();
      });
    }

    // Initial render
    renderStage();

  } catch (err) {
    console.error("Failed to load exam part data:", err);
  }
});
