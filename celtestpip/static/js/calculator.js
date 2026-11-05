function calculateCLB(skill, score) {
  score = Math.max(0, Math.min(38, parseInt(score, 10) || 0));
  if (skill === "LISTENING") {
    if (score >= 37) return 12;
    if (score >= 35) return 11;
    if (score >= 33) return 10;
    if (score >= 30) return 9;
    if (score >= 27) return 8;
    if (score >= 23) return 7;
    if (score >= 17) return 6;
    if (score >= 11) return 5;
    if (score >= 7) return 4;
    return 3;
  } else {
    if (score >= 38) return 12;
    if (score >= 36) return 11;
    if (score >= 33) return 10;
    if (score >= 31) return 9;
    if (score >= 28) return 8;
    if (score >= 24) return 7;
    if (score >= 19) return 6;
    if (score >= 15) return 5;
    if (score >= 10) return 4;
    return 3;
  }
}

document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("calcBtn");
  if (!btn) return;
  btn.addEventListener("click", () => {
    const skill = document.getElementById("skillSelect").value;
    const score = document.getElementById("rawScore").value;
    const clb = calculateCLB(skill, score);
    document.getElementById("clbResult").innerText = `CLB ${clb}`;
  });
});

if (typeof module !== "undefined" && module.exports) {
  module.exports = { calculateCLB };
}
