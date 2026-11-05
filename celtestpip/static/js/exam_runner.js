// celtestpip/static/js/exam_runner.js

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
  const parts = window.location.pathname.split("/").filter(Boolean);
  const examId = parts[1] || "exam1";
  const partNumber = parseInt(parts[3] || "1", 10);

  document.getElementById("examTitle").innerText = `${examId.toUpperCase()} • Part ${partNumber}`;
  
  // Render sidebar links (parts 1 to 20)
  const partsList = document.getElementById("partsList");
  partsList.innerHTML = Array.from({ length: 20 }, (_, i) => {
    const num = i + 1;
    const active = num === partNumber ? "active" : "";
    return `<a href="/exams/${examId}/part/${num}" class="part-btn ${active}">Part ${num}</a>`;
  }).join("");

  // Countdown timer
  let timeLeft = 600;
  const timerElem = document.getElementById("timer");
  if (timerElem) {
    const updateTimer = () => {
      const mins = Math.floor(timeLeft / 60);
      const secs = timeLeft % 60;
      timerElem.innerText = `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
      if (timeLeft > 0) {
        timeLeft--;
      }
    };
    updateTimer();
    setInterval(updateTimer, 1000);
  }

  // Fetch Part Data
  try {
    const res = await fetch(`/api/exams/${examId}/part/${partNumber}`);
    if (!res.ok) throw new Error("Part data not found");
    const data = await res.json();

    document.getElementById("partHeading").innerText = `${data.skill}: ${data.part_name}`;
    document.getElementById("partInstructions").innerText = data.instructions || "Answer the questions below.";

    // Audios
    const audioSec = document.getElementById("audioSection");
    if (data.audio_urls && data.audio_urls.length > 0) {
      audioSec.innerHTML = data.audio_urls.map((a, idx) => `
        <div style="margin-bottom:0.75rem;">
          <label style="font-size:0.85rem; font-weight:600;">Audio Track ${idx + 1}:</label>
          <audio controls class="audio-player" src="${a}"></audio>
        </div>
      `).join("");
    }

    // Image
    const imgSec = document.getElementById("imageSection");
    if (data.image_url) {
      imgSec.innerHTML = `<img src="${data.image_url}" style="max-width:100%; border-radius:8px; border:1px solid #e2e8f0;">`;
    }

    // Questions
    const qContainer = document.getElementById("questionsContainer");
    qContainer.innerHTML = (data.questions || []).map((q, idx) => `
      <div class="question-block" data-qid="${q.id}" data-answer="${q.correct_answer}">
        <p style="font-weight:600;">Question ${idx + 1}: ${escapeHtml(q.question_text)}</p>
        ${q.audio_url ? `<audio controls src="${q.audio_url}" style="margin:0.5rem 0; width:100%;"></audio>` : ""}
        <div class="options-list">
          ${q.options.map((opt, oIdx) => `
            <label class="opt-label">
              <input type="radio" name="q_${q.id}" value="${oIdx + 1}">
              <span>${escapeHtml(opt)}</span>
            </label>
          `).join("")}
        </div>
        <div class="explanation-box" id="exp_${q.id}">
          <strong>Explanation:</strong> ${escapeHtml(q.explanation || "No explanation provided.")}
        </div>
      </div>
    `).join("");

    // Transcripts
    const transcriptBox = document.getElementById("transcriptBox");
    if (data.transcripts && data.transcripts.length > 0) {
      transcriptBox.innerHTML = `<h4>Audio Transcript</h4>` + data.transcripts.map(t => `<p style="margin-top:0.5rem; white-space:pre-line;">${t}</p>`).join("");
    }

    // Submission logic
    document.getElementById("submitBtn").addEventListener("click", () => {
      let score = 0;
      const total = (data.questions || []).length;
      const answers = {};

      document.querySelectorAll(".question-block").forEach(qb => {
        const qid = qb.dataset.qid;
        const correct = qb.dataset.answer;
        const selected = qb.querySelector(`input[name="q_${qid}"]:checked`);
        const chosenVal = selected ? selected.value : "";
        answers[qid] = chosenVal;

        qb.querySelectorAll(".opt-label").forEach((label, lIdx) => {
          if (String(lIdx + 1) === correct) {
            label.classList.add("correct");
          } else if (chosenVal && String(lIdx + 1) === chosenVal) {
            label.classList.add("incorrect");
          }
        });

        if (chosenVal === correct) score++;
        const exp = document.getElementById(`exp_${qid}`);
        if (exp) exp.style.display = "block";
      });

      alert(`Part Complete! Your Score: ${score} / ${total}`);
      fetch("/api/attempts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ exam_id: examId, part_number: partNumber, answers, score, total_questions: total })
      }).catch(console.error);
    });

    // Transcript toggle
    document.getElementById("toggleTranscriptBtn").addEventListener("click", () => {
      transcriptBox.style.display = transcriptBox.style.display === "none" ? "block" : "none";
    });

  } catch (err) {
    console.error(err);
  }
});
