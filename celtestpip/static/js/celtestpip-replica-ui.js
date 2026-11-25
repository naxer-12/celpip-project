/**
 * CELTESTPIP 1:1 Replica UI Hydration
 * Restores native header mega-dropdowns (Practice & Free Guides), populates
 * empty Lottie/icon containers with crisp Lucide SVGs, and powers homepage demo tabs.
 */
(function () {
  'use strict';

  const SVGS = {
    headphones: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/></svg>',
    book: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    pen: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>',
    mic: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-full h-full"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>',
    trophy: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#d97706" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5 m-auto"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/></svg>',
    star: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#f59e0b" stroke="#f59e0b" stroke-width="1.5" class="w-5 h-5 m-auto"><path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/></svg>',
    crown: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#15803d" stroke="#15803d" stroke-width="1.5" class="w-5 h-5 m-auto"><path d="m2 4 3 12h14l3-12-6 7-4-7-4 7-6-7zm3 16h14"/></svg>',
    clock: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-6 h-6 text-zinc-500"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
  };

  function bindNavDropdowns() {
    const nav = document.querySelector('nav');
    if (!nav || nav.dataset.dropdownsBound === '1') return;
    nav.dataset.dropdownsBound = '1';

    // Remove any injected extra nav links (Score Calculator / Pricing) that bleed into mega-menu
    const centerNav = nav.querySelector('div.lg\\:flex.hidden');
    if (centerNav) {
      Array.from(centerNav.children).forEach((child) => {
        if (child.tagName === 'A' && (child.getAttribute('href') === '/calculator' || (child.textContent || '').trim() === 'Pricing')) {
          child.remove();
        }
      });
    }

    const containers = Array.from(nav.querySelectorAll('div.relative'));
    const closeAll = (except) => {
      containers.forEach((wrap) => {
        if (wrap === except) return;
        const btn = wrap.querySelector('button[aria-expanded]');
        const panel = wrap.querySelector('div.absolute');
        if (btn) btn.setAttribute('aria-expanded', 'false');
        if (panel) {
          panel.classList.add('opacity-0', 'invisible', 'scale-[0.97]');
          panel.classList.remove('opacity-100', 'visible', 'scale-100');
        }
      });
    };

    containers.forEach((wrap) => {
      const btn = wrap.querySelector('button[aria-expanded]');
      const panel = wrap.querySelector('div.absolute');
      if (!btn || !panel) return;

      let hideTimer = null;
      const openPanel = () => {
        if (hideTimer) clearTimeout(hideTimer);
        closeAll(wrap);
        btn.setAttribute('aria-expanded', 'true');
        panel.classList.remove('opacity-0', 'invisible', 'scale-[0.97]');
        panel.classList.add('opacity-100', 'visible', 'scale-100');
        // Clamp wide mega-dropdown inside viewport so it never clips left/right
        const wrapRect = wrap.getBoundingClientRect();
        const panelWidth = panel.offsetWidth || 820;
        const idealLeft = (wrapRect.width - panelWidth) / 2;
        const minLeft = 16 - wrapRect.left;
        const maxLeft = window.innerWidth - 16 - panelWidth - wrapRect.left;
        const clamped = Math.max(minLeft, Math.min(maxLeft, idealLeft));
        panel.style.left = `${clamped}px`;
        panel.style.transform = 'none';
      };
      const scheduleClose = () => {
        hideTimer = setTimeout(() => closeAll(null), 160);
      };

      wrap.addEventListener('mouseenter', openPanel);
      wrap.addEventListener('mouseleave', scheduleClose);
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = btn.getAttribute('aria-expanded') === 'true';
        if (isOpen) closeAll(null);
        else openPanel();
      });
    });

    document.addEventListener('click', (e) => {
      if (!nav.contains(e.target)) closeAll(null);
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeAll(null);
    });
  }

  function hydrateIcons() {
    // Remove any injected extra nav links (Score Calculator / Pricing) on inner pages so they don't bleed into mega-menu
    if (window.location.pathname !== '/') {
      document.querySelectorAll('nav a').forEach((a) => {
        const txt = (a.textContent || '').trim();
        if (txt === 'Score Calculator' || (txt === 'Pricing' && !a.querySelector('button'))) {
          a.remove();
        }
      });
    }

    // 1. Hide empty src="" images so no broken image icon appears
    document.querySelectorAll('img[src=""]').forEach((img) => {
      img.style.display = 'none';
    });

    // 2. Header button icons (Rankings, Reviews, Upgrade/Pricing)
    document.querySelectorAll('a[href="/rankings"] div.w-6.h-6').forEach((el) => {
      if (!el.querySelector('svg')) el.innerHTML = SVGS.trophy;
    });
    document.querySelectorAll('a[href="/reviews"] div.w-6.h-6').forEach((el) => {
      if (!el.querySelector('svg')) el.innerHTML = SVGS.star;
    });
    document.querySelectorAll('button.main2-btn div.w-6.h-6').forEach((el) => {
      if (!el.querySelector('svg')) el.innerHTML = SVGS.crown;
    });

    // 3. Practice Mega-Menu 4-column icons
    const megaMap = [
      { sel: 'a[href="/listening"] div.w-5.h-5', svg: SVGS.headphones, color: 'text-emerald-700' },
      { sel: 'a[href="/reading"] div.w-5.h-5', svg: SVGS.book, color: 'text-blue-700' },
      { sel: 'a[href="/writing"] div.w-5.h-5', svg: SVGS.pen, color: 'text-amber-700' },
      { sel: 'a[href="/speaking"] div.w-5.h-5', svg: SVGS.mic, color: 'text-purple-700' },
    ];
    megaMap.forEach(({ sel, svg, color }) => {
      document.querySelectorAll(sel).forEach((el) => {
        if (!el.querySelector('svg')) {
          el.classList.add(color);
          el.innerHTML = svg;
        }
      });
    });

    // 4. Skill & Part Hero H1 Icon Boxes
    const path = window.location.pathname || '/';
    let heroSvg = null;
    let heroColor = 'text-emerald-700';
    if (path.includes('listening')) { heroSvg = SVGS.headphones; heroColor = 'text-emerald-700'; }
    else if (path.includes('reading')) { heroSvg = SVGS.book; heroColor = 'text-sky-700'; }
    else if (path.includes('writing')) { heroSvg = SVGS.pen; heroColor = 'text-amber-700'; }
    else if (path.includes('speaking')) { heroSvg = SVGS.mic; heroColor = 'text-purple-700'; }

    if (heroSvg) {
      document.querySelectorAll('div.size-7, div.size-9').forEach((el) => {
        if (!el.querySelector('svg')) {
          el.classList.add(heroColor);
          el.innerHTML = heroSvg;
        }
      });
    }

    // 5. Make sure Upgrade button links cleanly to /exams instead of dead click
    document.querySelectorAll('button.main2-btn').forEach((btn) => {
      if (!btn.closest('a') && btn.dataset.bound !== '1') {
        btn.dataset.bound = '1';
        btn.addEventListener('click', () => { window.location.href = '/exams'; });
      }
    });
  }

  function hydrateHomepageInteractive() {
    if (window.location.pathname !== '/') return;

    // Ensure hero target band shows 10+ cleanly
    const heroNum = document.querySelector('h1 span.tabular-nums');
    if (heroNum && heroNum.textContent.trim() === '7') {
      heroNum.textContent = '10+';
    }

    // Populate 4x2 Quick-Nav Grid (-mt-[92px]) if Next.js Suspense left its cards empty
    const quickNavHost = Array.from(document.querySelectorAll('div')).find((d) =>
      d.className && typeof d.className === 'string' && d.className.includes('-mt-[92px]')
    );
    if (quickNavHost && !quickNavHost.textContent.trim()) {
      const cards = [
        { href: '/listening', title: 'Listening', sub: '6 parts', bg: 'bg-emerald-100 text-emerald-700', icon: SVGS.headphones },
        { href: '/reading', title: 'Reading', sub: '4 parts', bg: 'bg-sky-100 text-sky-700', icon: SVGS.book },
        { href: '/writing', title: 'Writing', sub: '2 tasks', bg: 'bg-amber-100 text-amber-700', icon: SVGS.pen },
        { href: '/speaking', title: 'Speaking', sub: '8 tasks', bg: 'bg-purple-100 text-purple-700', icon: SVGS.mic },
        { href: '/exams', title: 'Mock Tests', sub: '75 tests', bg: 'bg-blue-100 text-blue-700', icon: SVGS.trophy },
        { href: '/courses', title: 'Courses', sub: 'Lessons', bg: 'bg-indigo-100 text-indigo-700', icon: SVGS.book },
        { href: '/learn/templates', title: 'Templates', sub: '10 tasks', bg: 'bg-rose-100 text-rose-700', icon: SVGS.pen },
        { href: '/words', title: 'Vocabulary', sub: 'By task', bg: 'bg-teal-100 text-teal-700', icon: SVGS.star },
      ];
      quickNavHost.innerHTML = `
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-4xl mx-auto px-4">
          ${cards.map((c) => `
            <a href="${c.href}" class="group flex items-center gap-3 p-3.5 rounded-2xl bg-white border border-zinc-200 shadow-sm hover:shadow-md hover:border-blue-300 transition-all">
              <div class="w-10 h-10 rounded-xl ${c.bg} p-2 shrink-0 flex items-center justify-center">${c.icon}</div>
              <div class="min-w-0">
                <div class="text-sm font-bold text-zinc-900 truncate">${c.title}</div>
                <div class="text-xs font-medium text-zinc-500">${c.sub}</div>
              </div>
            </a>
          `).join('')}
        </div>
      `;
    }

    // Wire homepage AI Scoring demo pill buttons if rendered empty
    const demoPills = Array.from(document.querySelectorAll('button')).filter((b) =>
      /^(Score|01 Coverage|02 How it sounded|03 What to fix|04 Score higher|05 Next steps)$/.test((b.textContent || '').trim())
    );
    if (demoPills.length > 0) {
      const demoCardHost = demoPills[0].closest('section') || demoPills[0].parentElement.parentElement;
      let preview = document.getElementById('homeDemoPreviewBox');
      if (!preview && demoCardHost) {
        const emptyCols = Array.from(demoCardHost.querySelectorAll('div')).find((d) =>
          d.className && d.className.includes('columns-2') && d.children.length === 0
        );
        if (emptyCols) {
          emptyCols.style.display = 'block';
          emptyCols.innerHTML = `
            <div id="homeDemoPreviewBox" class="p-6 rounded-2xl bg-white border border-zinc-200 shadow-sm text-left">
              <div class="flex items-center justify-between mb-3">
                <span class="text-xs font-bold uppercase tracking-wider text-blue-600">AI CELPIP Coach Preview</span>
                <span class="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-100 text-emerald-800">CLB 9 Ready</span>
              </div>
              <h4 id="homeDemoTitle" class="text-lg font-bold text-zinc-900 mb-2">Estimated Level: 9 / 12</h4>
              <p id="homeDemoBody" class="text-sm text-zinc-600 leading-relaxed">Full rubric scoring across Content &amp; Coherence, Vocabulary, Readability/Listenability, and Task Fulfillment on every Writing and Speaking submission.</p>
            </div>
          `;
        }
      }

      const contentMap = {
        'Score': ['Estimated Level: 9 / 12', 'Instant CLB level estimation with a 4-pillar rubric breakdown (Coherence, Vocabulary, Grammar/Listenability, Task Fulfillment).'],
        '01 Coverage': ['Prompt Bullet Coverage: 3 / 3', 'Checks every required bullet point in your email, survey response, or speaking prompt so you never lose marks for missing details.'],
        '02 How it sounded': ['Speaking Pace: 128 wpm · Natural Pauses', 'Measures speech rate, hesitation pauses, intonation variety, and clarity across all 8 CELPIP Speaking tasks.'],
        '03 What to fix': ['45 Targeted Sentence Upgrades', 'Side-by-side inline diff highlighting grammar slips, word-choice improvements, and smoother Canadian English transitions.'],
        '04 Score higher': ['CLB 10+ Model Rewrite', 'See and listen to your exact idea rewritten at a CLB 10–12 level so you learn how to upgrade your own phrasing.'],
        '05 Next steps': ['Personalized Study Plan', 'Direct links to the exact Part Practice sets, Collocations lessons, and Templates that target your weakest rubric pillar.'],
      };

      demoPills.forEach((pill) => {
        pill.addEventListener('click', () => {
          const key = (pill.textContent || '').trim();
          const data = contentMap[key];
          const tEl = document.getElementById('homeDemoTitle');
          const bEl = document.getElementById('homeDemoBody');
          if (data && tEl && bEl) {
            tEl.textContent = data[0];
            bEl.textContent = data[1];
          }
        });
      });
    }
  }

  function initAll() {
    // Restore legitimate glassmorphic containers (Quick-Nav Grid, backdrop-blur-xl) hidden by legacy unlock CSS
    ['celtestpip-unlock-style', 'replica-unlock-style'].forEach((id) => {
      const st = document.getElementById(id);
      if (st && st.textContent && (st.textContent.includes('backdrop-blur') || st.textContent.includes('blur-'))) {
        st.textContent = 'svg[class*="lock"], [aria-label*="Membership"] { display: none !important; }\n@media (min-width: 1024px) { #headerStartBtn { display: none !important; } }';
      }
    });
    bindNavDropdowns();
    hydrateIcons();
    hydrateHomepageInteractive();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
  setTimeout(initAll, 250);
  setTimeout(initAll, 900);
})();
