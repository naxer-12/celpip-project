// celtestpip/static/js/app.js
document.addEventListener("DOMContentLoaded", async () => {
  const container = document.getElementById("examsContainer");
  if (!container) return;

  try {
    const res = await fetch("/api/exams");
    let exams = await res.json();
    if (!exams || exams.length === 0) {
      // Fallback generator for 60 exams
      exams = Array.from({ length: 60 }, (_, i) => ({
        id: `exam${i + 1}`,
        name: `Exam ${i + 1}`
      }));
    }
    
    container.innerHTML = exams.map(e => `
      <a href="/exams/${e.id}/part/1" class="exam-badge">
        <div style="font-size:1.1rem; margin-bottom:0.25rem;">📝 ${e.name}</div>
        <span style="font-size:0.75rem; color:#64748b;">20 Parts Available</span>
      </a>
    `).join("");
  } catch (err) {
    console.error("Failed to load exams:", err);
  }
});
