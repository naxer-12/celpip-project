# CELTESTPIP Handover & Project Status

> **Target Audience:** Any incoming AI agent, engineer, or collaborator taking over this repository.  
> **Status as of November 2026:** Fully functional, 100% offline-capable, 84/84 pytest tests passing, deployed via Render connected to `origin/main`.

---

## 1. Executive Summary & Architecture

`celtestpip` is a pixel-perfect, 1:1 atomic replica of the CELPIP preparation platform ([celtestpip.com](https://www.celtestpip.com)), re-engineered to run fully offline and self-contained with **zero paywalls**, **zero mandatory external network requests**, and **zero dependency on an active Node.js server**.

### Tech Stack
- **Backend:** Python 3.14+ FastAPI (`celtestpip.server.app:app`), Uvicorn, SQLite3 / Turso DB (`libsql://celpip-db-naxer-12.aws-ap-south-1.turso.io` with fallback to `celtestpip/data/celtestpip.db`).
- **Frontend:** Pre-rendered Next.js App Router SSG (Server-Side Generated) HTML + Next.js client-side React Flight/RSC chunk bundles.
- **Hosting / Deployment:** Render Web Service deploying automatically on pushes to `origin/main`.
- **Media & Assets:** Local storage under `celtestpip/data/media/` and `celtestpip/static/` with an on-demand proxy-cache fallback for missing assets.

---

## 2. Key Directories & File Inventory

```
celtestpip/
├── server/
│   ├── app.py                     # Main FastAPI application entrypoint with CORS & GZip
│   ├── config.py                  # Global directory constants, headers, and in-memory caches
│   └── routers/
│       ├── pages.py               # Serves HTML pages (exams, practices, learn, words, etc.)
│       ├── practices.py           # Practice session endpoints (/api/practices/{id}/result, /done, /question)
│       ├── assets.py              # Next.js static bundles, images, and audio streaming with Range headers
│       ├── exams.py               # Full mock exam endpoints and scoring calculators
│       └── auth.py                # Local Clerk auth mock endpoints (/v1/client, /v1/environment)
├── scripts/
│   ├── patch_listening_audio_steps.py  # Injects passage audio (Step 1) & updates Flight reference pointers
│   └── unlock_all_pro_content.py       # Master paywall cleaner, spinner stripper, and HTML patcher
├── static/
│   └── _next/static/immutable/chunks/  # Next.js React client bundles
│       ├── 2fvw__nnw3kbd_v2.js         # Decoupled useAuthedFetch (offline Clerk unblocked)
│       ├── 24w9ng0sqrv9g_v2.js         # Answer Key component with defensive options fallback
│       └── ...
├── data/
│   ├── celtestpip.db             # Local SQLite database (questions, practices, exams, vocab)
│   ├── pages/                    # 592 pre-rendered listening practice HTML pages + reading/exam pages
│   └── media/                    # Audio MP3s and exam images
└── tests/                        # 84 automated pytest tests (100% passing)
```

---

## 3. Critical Technical Lessons & Gotchas (MUST READ)

### Gotcha A: React Server Component (Flight / RSC) Payload Shifting
- **Problem:** When modifying pre-rendered Next.js pages (such as adding the conversation audio player before Question 1), inserting a step into `practice.steps` shifts all subsequent step indices.
- **Why it breaks:** React's client-side deserializer relies on internal Flight references (e.g. `steps:3:timings`, `steps:7:timings`). If the indices in `steps` shift but references aren't updated, React throws:
  ```
  React Error #570: Invalid reference.
  ```
- **The Fix:** In `celtestpip/scripts/patch_listening_audio_steps.py`, any reference like `steps:3:timings` must be shifted to `steps:4:timings`, and `steps:7:timings` to `steps:8:timings`. Always use `patch_listening_audio_steps.py` when reprocessing practice templates.

### Gotcha B: Next.js Answer Key Component Schema Requirement
- **Problem:** When a user clicks **"Answers key"**, the Next.js component `g` in `chunks/24w9ng0sqrv9g.js` loops over:
  ```javascript
  x.filter(t => e.options[t]) // where x = ["option1", "option2", "option3", "option4"]
  ```
- **Why it breaks:** If `/api/practices/{practice_id}/result` returns questions without a nested `options` dictionary (`e.options` is `undefined`), JavaScript throws:
  ```
  TypeError: Cannot read properties of undefined (reading 'option1')
  ```
  This immediately triggers Next.js's top-level Error Boundary: *"Oops! Something went wrong"*.
- **The Fix:**
  1. Backend (`celtestpip/server/routers/practices.py`): Ensure `get_practice_questions()` returns:
     ```json
     {
       "id": "...",
       "question": "...",
       "options": {
         "option1": "First choice",
         "option2": "Second choice",
         "option3": "Third choice",
         "option4": "Fourth choice"
       },
       "userAnswer": "option1",
       "isCorrect": true,
       "explanation": "..."
     }
     ```
  2. Frontend defensive guard (`24w9ng0sqrv9g_v2.js`): `e.options = e.options || e`.

### Gotcha C: Clerk `useAuthedFetch` Offline Hang
- **Problem:** Clicking "Answers key" hangs indefinitely on *"Checking your answers..."* with an animated spinner.
- **Why it breaks:** In `chunks/2fvw__nnw3kbd.js`, the `useAuthedFetch` hook attempts to fetch a session token via `await getToken()`. Because Clerk is not connected online, the returned Promise never settles.
- **The Fix:** In `chunks/2fvw__nnw3kbd_v2.js`, set `let i = null` directly instead of awaiting `getToken()`. This allows all local fetch calls to fire immediately.

### Gotcha D: Chromium `Cache-Control: immutable` Chunk Caching
- **Problem:** Editing files inside `_next/static/immutable/chunks/` has NO effect in the browser because Chromium caches them permanently under RFC 8246.
- **The Fix:** Always version modified bundles (e.g., `2fvw__nnw3kbd_v2.js` and `24w9ng0sqrv9g_v2.js`) and update the script references in the HTML files and FastAPI routers.

---

## 4. How to Run, Test, and Verify

### Running the Local Development Server
```bash
python3 -m uvicorn celtestpip.server.app:app --host 127.0.0.1 --port 8000
```
Visit:
- Home: `http://localhost:8000/`
- Listening Hub: `http://localhost:8000/listening`
- Listening Practice: `http://localhost:8000/practices/listening_cmn4hda7y00pyyqundlh38n09`
- Reading Hub: `http://localhost:8000/reading`
- Exam Simulator: `http://localhost:8000/exams`

### Running the Test Suite
```bash
pytest celtestpip/tests/ -v
```
All **84 tests** must pass before committing or pushing.

### Deploying to Render
Render is configured with continuous deployment from GitHub:
- **Repository:** `https://github.com/naxer-12/celpip-project.git`
- **Branch:** `main`
- **Deploy Trigger:** Simply `git push origin main`.
- **Render Build Command:** Defined in Render dashboard (installs dependencies via `pip install -r requirements.txt`).
- **Render Start Command:** `uvicorn celtestpip.server.app:app --host 0.0.0.0 --port $PORT`

---

## 5. Useful Scripts

1. **`celtestpip/scripts/patch_listening_audio_steps.py`**:
   Scans and patches listening practice HTML files to insert Step 1 conversation passage audio and adjust Flight references.
   ```bash
   python3 -m celtestpip.scripts.patch_listening_audio_steps
   ```

2. **`celtestpip/scripts/unlock_all_pro_content.py`**:
   Master content unlocker. Removes Pro badge overlays, replaces auth spinners, and patches Flight payloads.
   ```bash
   python3 -m celtestpip.scripts.unlock_all_pro_content
   ```

---

## 6. Current Roadmap / Future Opportunities
- **Speaking & Writing Submissions:** Currently, questions and prompts are 100% unlocked; AI score evaluation mock engines can be further expanded to provide simulated automated CLB scoring offline.
- **Turso Sync:** If updating the database schema, migrate changes to both local `celtestpip/data/celtestpip.db` and the Turso cloud database using the provided Turso credentials.
