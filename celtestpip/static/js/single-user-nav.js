/**
 * Unified Single-User Navigation Bar
 * Replaces bloated multi-user SaaS header & broken circular skeleton buttons
 * with a clean, instant practice-only navigation bar across all pages.
 */
(function () {
  'use strict';

  const NAV_ITEMS = [
    { label: 'Home', href: '/' },
    { label: 'Mock Exams', href: '/exams' },
    { label: 'Listening', href: '/listening' },
    { label: 'Reading', href: '/reading' },
    { label: 'Writing', href: '/writing' },
    { label: 'Speaking', href: '/speaking' },
    { label: 'Courses', href: '/courses' },
    { label: 'Vocabulary', href: '/words' },
    { label: 'Calculator', href: '/calculator' },
  ];

  function injectStyles() {
    if (document.getElementById('celtestpip-single-nav-css')) return;
    const style = document.createElement('style');
    style.id = 'celtestpip-single-nav-css';
    style.textContent = `
      /* Hide bloated legacy Next.js navs, nprogress loaders, and upgrade promos */
      nav:not(#celtestpip-single-nav) { display: none !important; }
      #nprogress { display: none !important; }
      img[src=""] { display: none !important; }
      body { padding-top: 68px !important; }
      #celtestpip-single-nav {
        position: fixed;
        top: 0; left: 0; right: 0;
        min-height: 60px;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #e4e4e7;
        display: flex;
        align-items: center;
        padding: 6px 16px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      }
      #celtestpip-single-nav .nav-inner {
        max-width: 1280px;
        width: 100%;
        margin: 0 auto;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        justify-content: space-between;
        gap: 8px 12px;
      }
      #celtestpip-single-nav .nav-brand {
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        flex-shrink: 0;
      }
      #celtestpip-single-nav .nav-brand img {
        height: 26px;
        width: auto;
      }
      #celtestpip-single-nav .nav-links {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 4px;
      }
      #celtestpip-single-nav .nav-link {
        padding: 5px 10px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: 600;
        color: #3f3f46;
        text-decoration: none;
        white-space: nowrap;
        transition: background-color 0.15s, color 0.15s;
      }
      #celtestpip-single-nav .nav-link:hover {
        background: #f4f4f5;
        color: #18181b;
      }
      #celtestpip-single-nav .nav-link.active {
        background: #eff6ff;
        color: #1d4ed8;
      }
      #celtestpip-single-nav .nav-badge {
        display: none;
        align-items: center;
        gap: 6px;
        padding: 5px 10px;
        border-radius: 9999px;
        background: #ecfdf5;
        border: 1px solid #a7f3d0;
        color: #065f46;
        font-size: 12px;
        font-weight: 600;
        white-space: nowrap;
        flex-shrink: 0;
      }
      @media (min-width: 1024px) {
        #celtestpip-single-nav .nav-badge { display: inline-flex; }
      }
    `;
    document.head.appendChild(style);
  }

  function mountNav() {
    injectStyles();
    if (document.getElementById('celtestpip-single-nav')) return;

    const path = window.location.pathname || '/';
    const nav = document.createElement('nav');
    nav.id = 'celtestpip-single-nav';
    nav.setAttribute('aria-label', 'Practice Navigation');

    const linksHtml = NAV_ITEMS.map(item => {
      const isActive = item.href === '/'
        ? path === '/'
        : path === item.href || path.startsWith(item.href + '/') || (item.href !== '/' && path.includes('/' + item.href.slice(1) + '_'));
      return `<a href="${item.href}" class="nav-link${isActive ? ' active' : ''}">${item.label}</a>`;
    }).join('');

    nav.innerHTML = `
      <div class="nav-inner">
        <a href="/" class="nav-brand">
          <img src="/static/img/logo.png" alt="CELTESTPIP" onerror="this.style.display='none'" />
        </a>
        <div class="nav-links">${linksHtml}</div>
        <div class="nav-badge" title="Single-user local practice mode">
          <span style="width:7px;height:7px;border-radius:50%;background:#10b981;display:inline-block;"></span>
          Personal Practice
        </div>
      </div>
    `;

    document.body.insertBefore(nav, document.body.firstChild);

    // Sync body top padding to nav height (handles mobile wrap cleanly)
    const syncPad = () => {
      document.body.style.setProperty('padding-top', `${nav.offsetHeight + 4}px`, 'important');
    };
    syncPad();
    window.addEventListener('resize', syncPad);

    populateSkillHeaderIcons(path);
  }

  function populateSkillHeaderIcons(path) {
    const icons = {
      listening: '<svg class="w-full h-full text-emerald-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 14h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-7a9 9 0 0 1 18 0v7a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3"/></svg>',
      reading: '<svg class="w-full h-full text-sky-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
      writing: '<svg class="w-full h-full text-amber-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/></svg>',
      speaking: '<svg class="w-full h-full text-purple-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" x2="12" y1="19" y2="22"/></svg>',
    };
    let svg = null;
    if (path.includes('listening')) svg = icons.listening;
    else if (path.includes('reading')) svg = icons.reading;
    else if (path.includes('writing')) svg = icons.writing;
    else if (path.includes('speaking')) svg = icons.speaking;
    if (!svg) return;

    document.querySelectorAll('div.size-7, div.size-9').forEach(el => {
      if (!el.innerHTML.trim()) el.innerHTML = svg;
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountNav);
  } else {
    mountNav();
  }
})();
