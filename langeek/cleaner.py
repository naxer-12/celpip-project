"""HTML, DOM & State Cleaner for LanGeek Offline Test Replica.

Strips client-side paywalls, enables mock Pro/Premium status in Next.js __NEXT_DATA__,
rewrites external media through local media proxy to fix CDN MIME type bugs,
decouples third-party auth dependencies, and injects non-destructive unblocking CSS.
"""

import re
import json
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger("langeek_cleaner")

MOCK_PRO_USER = {
    "id": 999999,
    "email": "learner@local.dev",
    "name": "French Explorer (Pro)",
    "isPremium": True,
    "isEmailVerified": True,
    "tier": "premium",
    "plan": "unlimited",
    "credits": 99999,
    "roles": ["user", "premium"],
    "avatar": None,
    "createdAt": "2026-01-01T00:00:00+00:00"
}

def rewrite_media_urls_in_str(text: str) -> str:
    """Rewrite third-party CDN and API media URLs to route through the local /media-proxy."""
    # cdn.langeek.co/photo/...
    text = re.sub(
        r'https://cdn\.langeek\.co/photo/([^"\'`\s]+)',
        r'/media-proxy?url=https://cdn.langeek.co/photo/\1',
        text
    )
    # api.langeek.co/v1/assets/...
    text = re.sub(
        r'https://api\.langeek\.co/v1/assets/([^"\'`\s]+)',
        r'/media-proxy?url=https://api.langeek.co/v1/assets/\1',
        text
    )
    # tts.langeek.co/read?...
    text = re.sub(
        r'https://tts\.langeek\.co/read\?([^"\'`\s]+)',
        r'/media-proxy?url=https://tts.langeek.co/read?\1',
        text
    )
    return text


def patch_next_data_json(next_data_json: str) -> str:
    """Parse and patch __NEXT_DATA__ JSON string with active Pro status and unblocked states."""
    try:
        data = json.loads(next_data_json)
    except Exception as e:
        logger.warning(f"Failed to parse __NEXT_DATA__ JSON: {e}")
        return rewrite_media_urls_in_str(next_data_json)

    props = data.get("props", {})
    page_props = props.get("pageProps", {})
    init_state = page_props.get("initialState", {})

    client_state = init_state.get("client", {})
    if isinstance(client_state, dict):
        # 1. Inject Authenticated Pro User
        client_state["auth"] = {"user": MOCK_PRO_USER}

        # 2. Inject Active Plan Data
        client_state["plan"] = {
            "data": {
                "id": "unlimited_pro",
                "title": "LanGeek Premium (Unlocked Replica)",
                "isPremium": True,
                "hasAccess": True,
                "daysRemaining": 3650
            },
            "status": "succeeded",
            "hasError": False,
            "plans": {
                "data": [
                    {
                        "id": "lifetime_plan",
                        "title": "Unlimited Access",
                        "isCurrent": True
                    }
                ],
                "status": "succeeded",
                "hasError": False
            }
        }

        # 3. Ensure learnPage features are fully active
        if "learnPage" in client_state and isinstance(client_state["learnPage"], dict):
            client_state["learnPage"]["isSpellingAvailable"] = True
            client_state["learnPage"]["grammarPractiveAvailable"] = True

    # Serialize back and route media through proxy
    serialized = json.dumps(data, ensure_ascii=False)
    return rewrite_media_urls_in_str(serialized)


def clean_replica_html(
    html: str,
    target_locale: str = "fr-EN",
    mock_user_name: str = "Pro French Learner"
) -> str:
    """Transform crawled LanGeek HTML into an unlocked, offline-friendly replica."""

    # 1. Patch __NEXT_DATA__ payload
    next_data_match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', html, flags=re.DOTALL)
    if next_data_match:
        raw_json = next_data_match.group(1)
        patched_json = patch_next_data_json(raw_json)
        html = html[:next_data_match.start(1)] + patched_json + html[next_data_match.end(1):]

    # 2. Rewrite HTML image & media tags to route through /media-proxy
    html = re.sub(
        r'src=["\']https://cdn\.langeek\.co/photo/([^"\']+)["\']',
        r'src="/media-proxy?url=https://cdn.langeek.co/photo/\1"',
        html
    )
    html = re.sub(
        r'src=["\']https://api\.langeek\.co/v1/assets/([^"\']+)["\']',
        r'src="/media-proxy?url=https://api.langeek.co/v1/assets/\1"',
        html
    )

    # 3. General Regex flag patching across inline scripts
    for flag in ["isPremium", "hasAccess", "isProUser", "isSubscribed"]:
        html = re.sub(rf'"{flag}"\s*:\s*false', f'"{flag}":true', html)

    # 4. Strip Upgrade / Paywall Modals & Lock Banners
    upgrade_patterns = [
        r'<div[^>]*>.*?This (?:feature|lesson|content|course) is (?:for|available for) Premium Members Only.*?Upgrade.*?</button>\s*</div>',
        r'<div class="[^"]*fixed bottom-[48][^"]*">.*?Upgrade to (?:Premium|Pro) Membership.*?</div>\s*</div>\s*</div>',
        r'<div[^>]*aria-label="Membership"[^>]*>.*?</div>'
    ]
    for pat in upgrade_patterns:
        html = re.sub(pat, '', html, flags=re.DOTALL | re.IGNORECASE)

    # 5. Remove Tailwind Blur utility classes
    for blur_cls in [
        "blur-sm select-none", "blur-[2px]", "filter blur-sm",
        "blur-[5px] select-none", "blur-[4px] select-none",
        "blur-[5px]", "blur-[4px]", "backdrop-blur-sm", "backdrop-blur-lg"
    ]:
        if blur_cls in html:
            html = html.replace(blur_cls, "")

    # 6. Navbar Auth Decoupling: Replace Login link/spinner with Pro Profile badge
    login_btn_pattern = r'<a[^>]*href="[^"]*(?:/login|/user/profile)"[^>]*>\s*<button[^>]*>.*?Login.*?</button>\s*</a>'
    pro_badge = (
        f'<div class="flex items-center space-x-2 px-3 py-1.5 bg-amber-500/10 text-amber-600 rounded-xl border border-amber-500/20 text-xs font-semibold">'
        f'<span>👑</span><span>{mock_user_name}</span>'
        f'</div>'
    )
    html = re.sub(login_btn_pattern, pro_badge, html, count=1, flags=re.DOTALL | re.IGNORECASE)

    # Replace spinning SVG loaders if present in auth buttons
    spinner_regex = r'<button[^>]*>\s*<svg[^>]*animate-spin[^>]*>.*?</svg>\s*</button>'
    html = re.sub(spinner_regex, pro_badge, html, flags=re.DOTALL)

    # 7. Inject Unblocking & Polish Styles into <head>
    if "replica-unlock-style" in html:
        html = re.sub(r'<style id="replica-unlock-style">.*?</style>', '', html)

    unlock_css = (
        '<style id="replica-unlock-style">\n'
        '  /* LanGeek Offline Test Replica Styling */\n'
        '  svg[class*="lock"], [aria-label*="Membership"], div[class*="backdrop-blur"],\n'
        '  div[class*="blur-"], .blur-sm, .filter.blur-sm { display: none !important; filter: none !important; }\n'
        '  #replica-badge {\n'
        '    position: fixed; bottom: 12px; right: 12px; z-index: 9999;\n'
        '    background: #0f172a; color: #38bdf8; font-size: 11px; font-weight: 600;\n'
        '    padding: 6px 12px; border-radius: 9999px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);\n'
        '    border: 1px solid #1e293b; pointer-events: none; opacity: 0.85;\n'
        '  }\n'
        '</style>\n'
    )
    if "</head>" in html:
        html = html.replace("</head>", f"{unlock_css}</head>", 1)

    # 8. Add subtle offline replica pill before </body>
    if "</body>" in html and 'id="replica-badge"' not in html:
        pill = '<div id="replica-badge">⚡ LanGeek Offline Replica (fr-EN Unlocked)</div>\n'
        html = html.replace("</body>", f"{pill}</body>", 1)

    return html
