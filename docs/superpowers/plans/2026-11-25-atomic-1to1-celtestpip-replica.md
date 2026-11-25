# Atomic 1:1 CELTESTPIP Replication Plan

**Goal:** Restore and perfect the 1:1 visual, layout, and interactive parity of `https://www.celtestpip.com/` across the Homepage (`/`), Navigation Header & Dropdowns, Part Pages (`/parts/*`), and all 4 Skill Simulators (Listening, Reading, Writing, Speaking) — completely unlocked with zero login walls so a user cannot tell the replica apart from the original site.

## Architecture & Tasks

### Task 1: Restore Original Homepage & Native Header Navigation (`169e981:celtestpip/static/index.html` + `pages.py`)
- Restore `celtestpip/static/index.html` from `169e981` (the exact crawled `celtestpip.com` homepage with sky clouds, student avatars, `10+` hand-drawn green circle, 4x2 Quick-Nav Grid, AI Scoring, 3-Step Process, VS comparison, and global footer).
- Keep `<link rel="stylesheet" href="/static/css/style.css">`, `<div id="examsContainer" class="hidden"></div>`, and `<script src="/static/js/app.js"></script>` for backward compatibility with existing tests.
- Remove the `#celtestpip-single-nav` override from `pages.py` so the authentic `celtestpip.com` `<nav>` renders on every page!

### Task 2: Native Header Mega-Dropdowns, Lottie/Icon Hydration & Footer Polish (`celtestpip-replica-ui.js`)
- Create `celtestpip/static/js/celtestpip-replica-ui.js` (loaded via `pages.py` on `/` and all replicated pages):
  - **Header Dropdowns:** Wire the `Practice` mega-dropdown (4-column Listening/Reading/Writing/Speaking menu + `All practice questions ->`) and `Free Guides` dropdown (`All free guides`, `Writing & Speaking Templates`, `Video Lessons`, 9 topic links) on hover + click!
  - **Icon & Lottie Hydration:** Populate every empty `<div class="w-6 h-6 ...">`, `<div class="size-7 lg:size-9">`, and `span.h-14.w-14` icon container with crisp Lucide SVG icons matching the original site (Rankings podium, Reviews stars, Upgrade crown, Headphones, BookOpen, PenLine, Mic, Clock) — re-running after React hydration settles.
  - **Clean Header Auth Buttons:** Replace any residual `Login / Sign up` / `Upgrade` blockers with unlocked navigation (`Practice Free` / `Full Mock Tests` -> `/exams`, or clean single-user unlocked badge) while preserving exact button geometry and colors.
  - **Homepage Demo & Counter Polish:** Animate the hero `10+` counter and wire the homepage interactive demo section pills (`Score`, `01 Coverage`, `02 How it sounded`, `03 What to fix`, `04 Score higher`, `05 Next steps`) so there are zero dead controls on `/`.

### Task 3: Exact Listening & Reading Simulator Parity (`celtestpip-runner.js`)
- **Shared Workspace Left Rail & Sidebar:** Wire the collapsed left rail `>` (`Show sidebar`) button and `Prev`/`Next` chevrons across all 4 skills so clicking `>` opens/closes the full question list sidebar!
- **Listening (`/practices/listening_*`):**
  - Match the original `celtestpip.com` Audio Player (`Play/Pause` large blue circle, blue seek bar, `0:00 / 1:05`, `-10s`, `+10s`, `1x` speed pill, `"Transcript"` accordion, `"Next ->"` header button + header progress bar).
  - Match the original 50/50 Question Screen (`"Time remaining: 30 seconds"` badge in header, left compact audio player + `"Question transcript"` accordion, right `#F0F7FF` card with 4 radio choices and `"Show Answer"` revealing warm amber highlight + per-option ✅/❌ explanations).
  - Wire header `"Answers key"` button to open a clean Answer Key modal (unlocked, zero login prompt!).
- **Reading (`/practices/reading_*`):**
  - Keep the original inline `[1 v]`..`[11 v]` button aesthetic! Clicking any `[N v]` button opens a **floating white popover** anchored directly below the button (matching `celtestpip.com` `step_57.png`) with 4 radio options. Selecting an option updates the button label cleanly (`[7 detailed v]`).
  - Wire `"Show Answers"` to highlight and fill all 11 blanks inline in warm amber/yellow + explanations; wire header `"Answers Key"` to open the unlocked Answer Key modal!

### Task 4: Exact Writing & Speaking Interactive Parity + Example Report Modals (`celtestpip-runner.js`)
- **Writing (`/practices/writing_*`):**
  - Wire the native `<textarea>` with live `N / 150–200 words` counter & segmented progress bar (zero `"Login to Write"` modal!).
  - Wire `Weak` / `Normal` / `Top` Sample Answer tabs (with mint-green active `Top` pill & bolded blue target vocabulary phrases) and clickable `Words` pills.
  - Wire `Score my answer` and `See an example report` to open the **7-section Example/Score Report modal** (`01 Score`, `02 Coverage`, `03 Repaired`, `04 Score higher`, `05 Next time`, `06 Study next`, `07 The answer`) matching `celtestpip.com`!
- **Speaking (`/practices/speaking_*`):**
  - Populate the **Clock icon** inside the `Preparation Time 30` gray rounded box and run the live `30` -> `0` countdown!
  - Wire `Skip` to transition cleanly to the **"Record to get your score"** state with the bright red **`Record | 90s`** button and **`Prep again`** button!
  - Wire `Record | 90s` to record via browser `MediaRecorder` (with 90s countdown fallback if mic unavailable, zero `"Login to Record"` modal!) and evaluate/play back the response.
  - Wire `Weak` / `Normal` / `Top` tabs and `See an example report` to open the 7-section Speaking Example Report modal!

### Task 5: Part-Page Topic Filter Popovers, Impeccable Audit, & Side-by-Side Verification
- On `/parts/*`: wire `Practice` | `Part Details` | `FAQ` tabs, `Topic [All topics v]` floating pill popover (filtering the practice grid live!), and `Free only` toggle.
- Run `/Users/jainamshah/.gemini/config/skills/impeccable/scripts/impeccable detect --json` on modified UI files and fix any findings.
- Run `pytest celtestpip/tests/ -q` (updating `test_frontend_shell.py` to match the restored authentic homepage).
- Verify side-by-side in Chrome via browser subagent across `/`, `/listening`, `/parts/listening_clziyrj8900021stdrf3o49w5`, `/practices/listening_cmcwhh3ft008jtgu9sjrb1lvy`, `/practices/reading_cmmll1ds0001520uni1chgpm1`, `/practices/writing_cmn4fn42w00iayqunknpiu9b0`, and `/practices/speaking_cmn4ctr9u0083yqunezy28o5s`, then push to `origin/main`!
