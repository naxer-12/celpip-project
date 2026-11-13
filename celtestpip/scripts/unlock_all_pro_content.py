import os
import re
import glob

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
PAGES_DIR = os.path.join(BASE_DIR, "data", "pages")

START_BTN_HDR = """<button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2" id="headerStartBtn">Start<svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></button>"""
START_BTN_BOX = """<div class="mt-6 flex flex-col w-full lg:w-fit"><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-12 px-7 shadow text-[15px] font-bold" id="startTaskBtn">Start <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg></button></div>"""

def clean_html(html: str) -> str:
    # 0. Point Clerk to local patched version to prevent origin domain crashes
    if 'https://clerk.celtestpip.com/npm/@clerk/clerk-js@6/dist/clerk.browser.js' in html:
        html = html.replace('https://clerk.celtestpip.com/npm/@clerk/clerk-js@6/dist/clerk.browser.js', '/static/js/clerk.browser.js')

    # 1. Update RSC JSON flags so React hydrates as Pro/authenticated
    if 'false' in html or 'undefined' in html:
        if 'hasAccess' in html:
            html = re.sub(r'hasAccess\\?"\s*:\s*false', r'hasAccess\":true', html)
        if 'isPremium' in html:
            html = re.sub(r'isPremium\\?"\s*:\s*false', r'isPremium\":true', html)
        if 'isProUser' in html:
            html = re.sub(r'isProUser\\?"\s*:\s*false', r'isProUser\":true', html)
        if 'isLoggedIn' in html:
            html = re.sub(r'isLoggedIn\\?"\s*:\s*false', r'isLoggedIn\":true', html)
        if 'userCredits' in html:
            html = re.sub(r'userCredits\\?"\s*:\s*0', r'userCredits\":9999', html)
        if 'userId' in html:
            html = re.sub(r'userId\\?"\s*:\s*\\?"\$undefined\\?"', r'userId\":\"tester\"', html)

    # 2. Replace static paywall box with start button
    if 'Upgrade to Pro' in html:
        paywall_regex = r'<div class="mt-6 flex flex-col w-full lg:w-fit">.*?Upgrade to Pro.*?</button>\s*</div>'
        html = re.sub(paywall_regex, START_BTN_BOX, html, flags=re.DOTALL)

        if 'This practice is for Pro Members Only' in html:
            generic_paywall_regex = r'<div[^>]*>.*?This practice is for Pro Members Only.*?Upgrade to Pro.*?</button>\s*</div>'
            html = re.sub(generic_paywall_regex, START_BTN_BOX, html, flags=re.DOTALL)

        if 'This speaking practice is for Pro' in html:
            speaking_paywall_regex = r'<div class="flex flex-col items-center text-center animate-in fade-in-0 duration-300">.*?This speaking practice is for Pro.*?Upgrade to Pro</button></div>'
            html = re.sub(speaking_paywall_regex, '', html, flags=re.DOTALL)

        blur_overlay_regex = r'<div class="absolute inset-0 top-20 items-center justify-center flex flex-col gap-2">.*?Upgrade to Pro</button></div>'
        html = re.sub(blur_overlay_regex, '', html, flags=re.DOTALL)

    # 3. Replace disabled "Pro only" button with "Start" button
    if 'Pro only' in html:
        header_pro_regex = r'<button class="[^"]*" disabled=""><svg[^>]*lucide-lock[^>]*>.*?</svg>Pro only</button>'
        html = re.sub(header_pro_regex, START_BTN_HDR, html, flags=re.DOTALL)

    if 'blur' in html:
        html = html.replace('blur-sm select-none', '')
        html = html.replace('blur-[2px]', '')
        html = html.replace('filter blur-sm', '')
        html = html.replace('blur-[5px] select-none', '')
        html = html.replace('blur-[4px] select-none', '')
        html = html.replace('blur-[5px]', '')
        html = html.replace('blur-[4px]', '')
        html = html.replace('backdrop-blur-sm', '')
        html = html.replace('backdrop-blur-lg', '')

    # 4. Vocabulary bundles cleanup
    if 'locked' in html:
        html = html.replace(r'\"locked\":true', r'\"locked\":false')
        html = html.replace('"locked":true', '"locked":false')
        html = html.replace(r'\"isPremium\":false', r'\"isPremium\":true')
        html = html.replace(r'\"isFree\":false', r'\"isFree\":true')
        html = html.replace(r'\"isLoggedIn\":false', r'\"isLoggedIn\":true')

    if 'This word unlocks' in html:
        html = html.replace("This word unlocks with CELTESTPIP Pro, with its meaning and example.", "Tap to view meaning and examples.")
        html = html.replace('<span class="sr-only">Locked</span>', '<span class="sr-only">Not mastered yet</span>')
        lock_span_pat = r'<span class="flex h-5 w-5 items-center justify-center rounded-full bg-zinc-100"><svg[^>]*lucide-lock[^>]*>.*?</svg></span>'
        html = re.sub(lock_span_pat, '<span class="flex h-5 w-5 items-center justify-center rounded-full border border-dashed border-zinc-200"></span>', html)
        banner_pat = r'<div class="mt-8 flex justify-center"><button [^>]*>.*?Unlock all.*?words with Pro</button></div>'
        html = re.sub(banner_pat, '', html, flags=re.DOTALL)

    # Safe class transformation for locks and pro badges across both HTML and RSC flight payloads
    if 'lucide-lock' in html:
        html = html.replace('lucide-lock', 'hidden')
    if 'inline-flex items-center gap-1 text-xs font-semibold text-zinc-500' in html:
        html = html.replace('inline-flex items-center gap-1 text-xs font-semibold text-zinc-500', 'hidden')

    # Replace or inject non-destructive unblocking CSS to hide residual locks, pro badges, or paywalls cleanly without React hydration mismatches
    if 'celtestpip-unlock-style' in html:
        html = re.sub(r'<style id="celtestpip-unlock-style">.*?</style>', '', html)
    if '</head>' in html:
        unlock_css = '<style id="celtestpip-unlock-style">svg[class*="lock"], [aria-label*="Membership"], div[class*="backdrop-blur"], div[class*="blur-"], .blur-sm, .filter.blur-sm { display: none !important; filter: none !important; }</style>'
        html = html.replace('</head>', f'{unlock_css}</head>', 1)

    # 5. Remove floating "Pro Membership / Upgrade Now / SALE" widget
    if 'Upgrade to Pro Membership' in html:
        floating_widget_regex = r'<div class="(?:hidden 2xl:flex fixed bottom-8 left-8 z-40|fixed bottom-4 left-4 z-50)[^"]*">.*?Upgrade to Pro Membership.*?SALE</div>\s*</div>\s*</div>'
        html = re.sub(floating_widget_regex, '', html, flags=re.DOTALL)
        floating_widget_simple = r'<div class="[^"]*fixed bottom-[48][^"]*">.*?Upgrade to Pro Membership.*?</div>\s*</div>\s*</div>'
        html = re.sub(floating_widget_simple, '', html, flags=re.DOTALL)

    # 5. Remove "Mock exams are for Pro Members. Upgrade" banner
    if 'Mock exams are for' in html:
        mock_banner_regex = r'<div class="[^"]*bg-blue-50[^"]*">\s*<p>Mock exams are for <b[^>]*>Pro Members</b>\.</p>.*?Upgrade\s*</button>\s*</div>'
        html = re.sub(mock_banner_regex, '', html, flags=re.DOTALL)

    # 6. Ensure "Start Free Practice" CTA buttons navigate directly to /exams
    if 'hero-cta-shine' in html and 'href="/home"' in html:
        html = re.sub(
            r'<a([^>]*?)href="/home"([^>]*?>\s*<button[^>]*?hero-cta-shine)',
            r'<a\1href="/exams"\2 onclick="window.location.href=\'/exams\'"',
            html
        )
    if 'Start practicing for free' in html and 'href="/home"' in html:
        html = re.sub(
            r'<a([^>]*?)href="/home"([^>]*?>\s*<button[^>]*?>\s*Start practicing for free)',
            r'<a\1href="/exams"\2 onclick="window.location.href=\'/exams\'"',
            html
        )

    # 7. Replace spinning auth placeholder button with clean static Sign in / Sign up button
    if 'lucide-loader-circle' in html:
        spinner_btn_regex = r'<button[^>]*>\s*<svg[^>]*lucide-loader-circle[^>]*animate-spin[^>]*>.*?</svg>\s*</button>'
        static_signin_btn = '<a href="/exams"><button class="items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 bg-white white-btn text-zinc-900 rounded-xl border border-zinc-300 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 flex lg:w-[128px] w-[80px]"><span class="lg:hidden">Sign in</span><span class="hidden lg:block">Login / Sign up</span></button></a>'
        html = re.sub(spinner_btn_regex, static_signin_btn, html, flags=re.DOTALL)

    return html

def process_file(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        cleaned = clean_html(content)
        if cleaned != content:
            with open(path, "w", encoding="utf-8") as f:
                f.write(cleaned)
            return True
    except Exception as e:
        print(f"Error processing {path}: {e}")
    return False

def main():
    modified = 0
    total = 0

    # Clean static pages
    for fn in ["exam.html", "exams.html", "index.html", "calculator.html"]:
        p = os.path.join(STATIC_DIR, fn)
        if os.path.exists(p):
            total += 1
            if process_file(p):
                modified += 1

    # Clean all cached pages
    pages = glob.glob(os.path.join(PAGES_DIR, "*.html"))
    for p in pages:
        total += 1
        if process_file(p):
            modified += 1

    print(f"Processed {total} files: modified {modified} files to remove Pro blockers.")

if __name__ == "__main__":
    main()
