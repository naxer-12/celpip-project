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

document.addEventListener("DOMContentLoaded", async () => {
  const pathParts = window.location.pathname.split("/").filter(Boolean);
  let examId = "exam1";
  let partNumber = 1;

  for (let i = 0; i < pathParts.length; i++) {
    const p = pathParts[i];
    if (p.startsWith("exam")) {
      examId = p;
    } else if (p.startsWith("part")) {
      const match = p.match(/\d+/);
      if (match) partNumber = parseInt(match[0], 10);
    } else if (p === "part" && pathParts[i + 1]) {
      partNumber = parseInt(pathParts[i + 1], 10) || 1;
    }
  }

  const currentMeta = CELPIP_PARTS.find(p => p.num === partNumber) || CELPIP_PARTS[0];

  // Set headings & metadata
  const examTitleElem = document.getElementById("examTitle");
  if (examTitleElem) examTitleElem.innerText = `${examId.toUpperCase()}`;

  const partHeadingElem = document.getElementById("partHeading");
  if (partHeadingElem) partHeadingElem.innerText = `${currentMeta.skill} Part ${currentMeta.num > 12 ? currentMeta.num - 12 : (currentMeta.num > 10 ? currentMeta.num - 10 : (currentMeta.num > 6 ? currentMeta.num - 6 : currentMeta.num))} : ${currentMeta.name}`;

  const instructionHeader = document.getElementById("instructionHeader");
  if (instructionHeader) instructionHeader.innerText = currentMeta.name;

  // Render 4-column dropdown menu
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

  // Toggle Dropdown Popover
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

  // Prev / Next Navigation buttons
  const prevBtn = document.getElementById("prevPartBtn");
  const nextBtn = document.getElementById("nextPartBtn");
  if (prevBtn) {
    if (partNumber > 1) {
      prevBtn.href = `/exams/${examId}/part/${partNumber - 1}`;
    } else {
      prevBtn.classList.add("opacity-50", "pointer-events-none");
    }
  }
  if (nextBtn) {
    if (partNumber < 20) {
      nextBtn.href = `/exams/${examId}/part/${partNumber + 1}`;
    } else {
      nextBtn.classList.add("opacity-50", "pointer-events-none");
    }
  }

  // Timer countdown
  let timeLeft = currentMeta.time || 600;
  let timerInterval = null;
  const timerElem = document.getElementById("timer");
  const timerDisplay = document.getElementById("timerDisplay") || timerElem;

  const updateTimer = () => {
    const mins = Math.floor(timeLeft / 60);
    const secs = timeLeft % 60;
    const formatted = `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
    if (timerDisplay) timerDisplay.innerText = formatted;
    if (timeLeft > 0) {
      timeLeft--;
    } else if (timerInterval) {
      clearInterval(timerInterval);
    }
  };
  updateTimer();

  // Start Practice action
  const startPracticeBtn = document.getElementById("startPracticeBtn");
  const instructionsScreen = document.getElementById("instructionsScreen");
  const activePracticeScreen = document.getElementById("activePracticeScreen");
  if (startPracticeBtn) {
    startPracticeBtn.addEventListener("click", () => {
      if (instructionsScreen) instructionsScreen.classList.add("hidden");
      if (activePracticeScreen) activePracticeScreen.classList.remove("hidden");
      if (!timerInterval) {
        timerInterval = setInterval(updateTimer, 1000);
      }
      // auto play audio if available
      const firstAudio = document.querySelector("#audioSection audio");
      if (firstAudio) {
        firstAudio.play().catch(() => {});
      }
    });
  }

  // Fetch Part Data from backend
  try {
    const res = await fetch(`/api/exams/${examId}/part/${partNumber}`);
    if (!res.ok) throw new Error("Part data not found");
    const data = await res.json();

    if (data.part_name && partHeadingElem) {
      partHeadingElem.innerText = `${data.skill} : ${data.part_name}`;
    }

    // Instructions
    const instructionsList = document.getElementById("instructionsList");
    if (instructionsList && data.instructions) {
      const lines = data.instructions.split("\n").filter(l => l.trim().length > 0);
      if (lines.length > 0) {
        instructionsList.innerHTML = lines.map(line => `
          <li class="flex items-start gap-3 py-3">
            <span class="mt-[9px] h-1.5 w-1.5 shrink-0 rounded-full bg-zinc-400"></span>
            <span>${escapeHtml(line.replace(/^[•\-\*]\s*/, ""))}</span>
          </li>
        `).join("");
      }
    }

    // Audio tracks
    const audioSec = document.getElementById("audioSection");
    const audioContainer = document.getElementById("audioPlayerContainer") || audioSec;
    if (data.audio_urls && data.audio_urls.length > 0) {
      audioSec.classList.remove("hidden");
      audioContainer.innerHTML = data.audio_urls.map((a, idx) => `
        <div class="rounded-xl border border-zinc-100 bg-zinc-50 p-3">
          <label class="text-xs font-semibold text-zinc-600 block mb-1.5">Track ${idx + 1}</label>
          <audio controls class="w-full h-10" src="${a}"></audio>
        </div>
      `).join("");
    }

    // Stimulus Image
    const imgSec = document.getElementById("imageSection");
    const partImage = document.getElementById("partImage");
    if (data.image_url) {
      imgSec.classList.remove("hidden");
      if (partImage) partImage.src = data.image_url;
    }

    // Transcripts
    const transcriptBox = document.getElementById("transcriptBox");
    const transcriptContent = document.getElementById("transcriptContent") || transcriptBox;
    if (data.transcripts && data.transcripts.length > 0) {
      transcriptContent.innerHTML = data.transcripts.map(t => `<p class="whitespace-pre-line text-xs text-amber-950">${escapeHtml(t)}</p>`).join("");
    }

    // Render Questions
    const qContainer = document.getElementById("questionsContainer");
    const questions = data.questions || [];
    if (questions.length === 0) {
      qContainer.innerHTML = `
        <div class="p-8 text-center text-zinc-500 font-practice">
          <p class="font-semibold text-base text-zinc-700">Practice questions loaded.</p>
          <p class="text-xs mt-1">Review the audio material or prompt on the left.</p>
        </div>
      `;
    } else {
      qContainer.innerHTML = questions.map((q, idx) => `
        <div class="question-block rounded-2xl border border-zinc-200 bg-white p-5 shadow-sm" data-qid="${q.id}" data-answer="${q.correct_answer}">
          <div class="flex items-center justify-between mb-3">
            <span class="text-xs font-bold uppercase tracking-wider text-blue-700 bg-blue-50 px-2 py-0.5 rounded-md">Question ${idx + 1} of ${questions.length}</span>
            <span class="text-xs text-zinc-400 font-medium">1 mark</span>
          </div>
          <p class="text-[15px] font-semibold text-zinc-900 leading-snug mb-4">${escapeHtml(q.question_text)}</p>
          
          ${q.audio_url ? `
            <div class="mb-4 p-2 bg-zinc-50 rounded-xl border border-zinc-200">
              <audio controls class="w-full h-8" src="${q.audio_url}"></audio>
            </div>
          ` : ""}

          <div class="options-list flex flex-col gap-2.5">
            ${q.options.map((opt, oIdx) => `
              <label class="opt-label relative flex items-center gap-3.5 p-3.5 rounded-xl border border-zinc-200 bg-white hover:border-zinc-300 hover:bg-zinc-50 cursor-pointer transition-all">
                <input type="radio" name="q_${q.id}" value="${oIdx + 1}" class="sr-only">
                <span class="radio-indicator flex h-5 w-5 shrink-0 items-center justify-center rounded-full border border-zinc-300 text-[11px] font-bold text-zinc-500 transition-colors">
                  ${String.fromCharCode(65 + oIdx)}
                </span>
                <span class="text-[14px] text-zinc-800 leading-snug select-none">${escapeHtml(opt)}</span>
              </label>
            `).join("")}
          </div>

          <div class="explanation-box hidden mt-4 p-4 rounded-xl bg-zinc-50 border border-zinc-200 text-xs font-practice text-zinc-800 leading-relaxed" id="exp_${q.id}">
            <p class="font-bold text-zinc-900 mb-1">Answer Analysis:</p>
            <p class="whitespace-pre-line">${escapeHtml(q.explanation || "Correct answer: " + q.correct_answer)}</p>
          </div>
        </div>
      `).join("");

      // Radio selection highlight styling
      document.querySelectorAll(".opt-label").forEach(label => {
        const radio = label.querySelector("input[type='radio']");
        radio.addEventListener("change", () => {
          const block = label.closest(".question-block");
          block.querySelectorAll(".opt-label").forEach(l => {
            l.classList.remove("border-blue-600", "bg-blue-50/50", "ring-2", "ring-blue-500/20");
            const indicator = l.querySelector(".radio-indicator");
            if (indicator) {
              indicator.classList.remove("border-blue-600", "bg-blue-600", "text-white");
              indicator.classList.add("border-zinc-300", "text-zinc-500");
            }
          });
          if (radio.checked) {
            label.classList.add("border-blue-600", "bg-blue-50/50", "ring-2", "ring-blue-500/20");
            const indicator = label.querySelector(".radio-indicator");
            if (indicator) {
              indicator.classList.add("border-blue-600", "bg-blue-600", "text-white");
              indicator.classList.remove("border-zinc-300", "text-zinc-500");
            }
          }
        });
      });
    }

    // Submission handler
    const submitBtn = document.getElementById("submitBtn");
    const showAnswersBtn = document.getElementById("showAnswersBtn");

    const revealAnswersAndScore = () => {
      let score = 0;
      const total = questions.length;
      const answers = {};

      document.querySelectorAll(".question-block").forEach(qb => {
        const qid = qb.dataset.qid;
        const correct = String(qb.dataset.answer).trim();
        const selected = qb.querySelector(`input[name="q_${qid}"]:checked`);
        const chosenVal = selected ? String(selected.value).trim() : "";
        answers[qid] = chosenVal;

        qb.querySelectorAll(".opt-label").forEach((label, lIdx) => {
          const val = String(lIdx + 1);
          label.classList.remove("border-blue-600", "bg-blue-50/50", "ring-2", "ring-blue-500/20");
          if (val === correct) {
            label.classList.add("correct", "border-emerald-500", "bg-emerald-50/70", "text-emerald-950", "font-medium", "ring-2", "ring-emerald-500/30");
          } else if (chosenVal && val === chosenVal) {
            label.classList.add("incorrect", "border-rose-400", "bg-rose-50/70", "text-rose-950", "line-through", "ring-2", "ring-rose-400/30");
          }
        });

        if (chosenVal === correct && correct !== "") score++;
        const exp = document.getElementById(`exp_${qid}`);
        if (exp) exp.classList.remove("hidden");
      });

      // Send attempt to server
      fetch("/api/attempts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ exam_id: examId, part_number: partNumber, answers, score, total_questions: total })
      }).catch(console.error);

      alert(`Part Complete! Your Score: ${score} / ${total}`);
    };

    if (submitBtn) submitBtn.addEventListener("click", revealAnswersAndScore);
    if (showAnswersBtn) showAnswersBtn.addEventListener("click", revealAnswersAndScore);

    // Transcript toggle
    const toggleTranscriptBtn = document.getElementById("toggleTranscriptBtn");
    if (toggleTranscriptBtn && transcriptBox) {
      toggleTranscriptBtn.addEventListener("click", () => {
        transcriptBox.classList.toggle("hidden");
      });
    }

  } catch (err) {
    console.error("Failed to load exam part:", err);
  }
});
