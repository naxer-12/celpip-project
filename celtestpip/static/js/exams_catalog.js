document.addEventListener("DOMContentLoaded", () => {
  let activeMenu = null;

  function closeMenu() {
    if (activeMenu) {
      activeMenu.remove();
      activeMenu = null;
    }
  }

  document.addEventListener("click", (e) => {
    if (activeMenu && !activeMenu.contains(e.target)) {
      closeMenu();
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
  });

  window.addEventListener("scroll", () => {
    if (activeMenu) closeMenu();
  }, { passive: true });

  // Find all cards
  const allParagraphs = document.querySelectorAll("p");
  allParagraphs.forEach((p) => {
    const text = (p.textContent || "").trim();
    const match = text.match(/^Exam\s+(\d+)$/i);
    if (!match) return;

    const examNum = match[1];
    const examSlug = `exam${examNum}`;

    // Find card container
    let card = p.parentElement;
    while (card && !card.classList.contains("border-zinc-200")) {
      card = card.parentElement;
    }
    if (!card) return;

    // Make title clickable
    p.style.cursor = "pointer";
    p.classList.add("hover:text-blue-600", "transition-colors");
    p.title = `Start Full Exam ${examNum}`;
    p.addEventListener("click", () => {
      window.location.href = `/exams/${examSlug}/part/1`;
    });

    const buttons = card.querySelectorAll("button");
    if (buttons.length >= 2) {
      const startBtn = buttons[0];
      const scoreBtn = buttons[1];

      // Score button direct navigation
      scoreBtn.style.cursor = "pointer";
      scoreBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        window.location.href = `/exams/${examSlug}/results`;
      });

      // Start button popover dropdown
      startBtn.style.cursor = "pointer";
      startBtn.addEventListener("click", (e) => {
        e.stopPropagation();
        if (activeMenu && activeMenu.dataset.examSlug === examSlug) {
          closeMenu();
          return;
        }
        closeMenu();

        // Create dropdown popover
        const menu = document.createElement("div");
        menu.id = "exam-dropdown-menu";
        menu.dataset.examSlug = examSlug;
        menu.className = "absolute z-50 w-56 rounded-2xl border border-zinc-200 bg-white p-2 shadow-2xl shadow-zinc-900/20 text-sm font-medium text-zinc-800";
        menu.style.position = "absolute";

        menu.innerHTML = `
          <div class="px-2.5 py-1.5 text-xs font-bold text-zinc-400 uppercase tracking-wider">Exam ${examNum} Practice</div>
          <a href="/exams/${examSlug}/part/1" class="flex items-center gap-2.5 px-3 py-2 rounded-xl hover:bg-zinc-100 font-semibold text-zinc-900 transition-colors">
            <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span>
            <span>Complete Test</span>
          </a>
          <div class="h-px bg-zinc-100 my-1.5"></div>
          <a href="/exams/${examSlug}/part/1" class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-emerald-50 text-emerald-800 transition-colors">
            <span class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-500"></span>Listening</span>
            <span class="text-xs text-emerald-700 bg-emerald-100/80 px-2 py-0.5 rounded-md font-mono font-bold">P 1-6</span>
          </a>
          <a href="/exams/${examSlug}/part/7" class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-blue-50 text-blue-800 transition-colors">
            <span class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500"></span>Reading</span>
            <span class="text-xs text-blue-700 bg-blue-100/80 px-2 py-0.5 rounded-md font-mono font-bold">P 7-10</span>
          </a>
          <a href="/exams/${examSlug}/part/11" class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-amber-50 text-amber-800 transition-colors">
            <span class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-amber-500"></span>Writing</span>
            <span class="text-xs text-amber-700 bg-amber-100/80 px-2 py-0.5 rounded-md font-mono font-bold">P 11-12</span>
          </a>
          <a href="/exams/${examSlug}/part/13" class="flex items-center justify-between px-3 py-2 rounded-xl hover:bg-purple-50 text-purple-800 transition-colors">
            <span class="flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-purple-500"></span>Speaking</span>
            <span class="text-xs text-purple-700 bg-purple-100/80 px-2 py-0.5 rounded-md font-mono font-bold">P 13-20</span>
          </a>
        `;

        document.body.appendChild(menu);

        // Position menu below button
        const rect = startBtn.getBoundingClientRect();
        const top = rect.bottom + window.scrollY + 6;
        const left = rect.left + window.scrollX;
        menu.style.top = `${top}px`;
        menu.style.left = `${left}px`;

        activeMenu = menu;
      });
    }
  });
});
