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
      body { padding-top: 64px !important; }
      #celtestpip-single-nav {
        position: fixed;
        top: 0; left: 0; right: 0;
        height: 64px;
        z-index: 9999;
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(8px);
        border-bottom: 1px solid #e4e4e7;
        display: flex;
        align-items: center;
        padding: 0 20px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
      }
      #celtestpip-single-nav .nav-inner {
        max-width: 1280px;
        width: 100%;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
      }
      #celtestpip-single-nav .nav-brand {
        display: flex;
        align-items: center;
        gap: 8px;
        text-decoration: none;
        flex-shrink: 0;
      }
      #celtestpip-single-nav .nav-brand img {
        height: 28px;
        width: auto;
      }
      #celtestpip-single-nav .nav-links {
        display: flex;
        align-items: center;
        gap: 4px;
        overflow-x: auto;
        scrollbar-width: none;
      }
      #celtestpip-single-nav .nav-links::-webkit-scrollbar { display: none; }
      #celtestpip-single-nav .nav-link {
        padding: 6px 11px;
        border-radius: 8px;
        font-size: 13.5px;
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
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountNav);
  } else {
    mountNav();
  }
})();
