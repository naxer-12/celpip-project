import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

with open("/tmp/live_exam_navbar.html", "r", encoding="utf-8") as f:
    nav_html = f.read()

# Make sure logo inside navbar uses local logo
nav_html = re.sub(r'src="[^"]*logo[^"]*"', 'src="/static/img/logo.png"', nav_html)

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, interactive-widget=resizes-content" />
  <title>CELPIP Exam Simulator</title>
  <meta name="description" content="Prepare for CELPIP with 4,000+ practice questions, 60 full mock exams, sample answers for every CLB level, and instant AI scoring. Practice all 4 skills online." />
  <link rel="icon" href="/static/img/favicon.ico" sizes="48x48" type="image/x-icon" />
  <link rel="apple-touch-icon" href="/static/img/icon.png" sizes="512x512" type="image/png" />
  <link rel="stylesheet" href="/static/css/44vsw4r55n3z4.css" />
  <link rel="stylesheet" href="/static/css/3pdzgbtsttvpc.css" />
  <link rel="stylesheet" href="/static/css/3wd6q86c4y2h1.css" />
  <link rel="stylesheet" href="/static/css/style.css">
  <link rel="preload" href="/static/fonts/OpenRunde_Regular-s.p.1jlhbliok6_eb.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/static/fonts/OpenRunde_Medium-s.p.0tyjjf8cs-eei.woff2" as="font" type="font/woff2" crossorigin="" />
  <link rel="preload" href="/static/fonts/OpenRunde_Bold-s.p.2uyvtvsynw6zk.woff2" as="font" type="font/woff2" crossorigin="" />
</head>
<body class="w-full bg-[#f1f2ee] font_ec461ab0-module__C9YHLG__variable space_grotesk_b68b8d46-module__-Dn4UG__variable font_ec461ab0-module__C9YHLG__className" lang="en">

<!-- AUTHENTIC LIVE NAVBAR -->
__NAV_HTML__

<!-- Fixed pro membership pill bottom-left -->
<div class="hidden 2xl:flex fixed bottom-8 left-8 z-40">
  <div class="relative inline-block w-48 group">
    <div class="flex flex-col w-full bg-gradient-to-br from-blue-700 via-blue-800 to-indigo-900 rounded-2xl h-fit p-3 cursor-pointer shadow-lg shadow-blue-600/20 transition-all duration-300 hover:shadow-blue-600/30 overflow-hidden" role="button" tabindex="0">
      <div class="relative z-10">
        <div class="size-14 shadow-lg bg-white p-2 rounded-2xl mb-2 flex items-center justify-center">
          <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
        </div>
        <div class="flex flex-col justify-start gap-0.5 mt-1">
          <p class="text-lg font-bold text-white tracking-wide text-left">Pro Membership</p>
          <p class="text-[12px] text-white/70 text-left w-full leading-relaxed">Unlock all premium features</p>
        </div>
        <button class="inline-flex items-center justify-center whitespace-nowrap text-sm ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-secondary main2-btn text-zinc-900 rounded-xl border border-green-400 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 w-full mt-3.5 font-bold">Upgrade Now</button>
      </div>
    </div>
    <div class="absolute -top-2.5 -right-2.5 bg-gradient-to-r from-orange-500 to-red-500 text-white text-[13px] font-bold px-2.5 py-1 rounded-lg shadow-md transform rotate-6">SALE</div>
  </div>
</div>

<div class="nav-clearance min-h-screen flex flex-col w-full overflow-x-clip lg:pt-[64px] pt-[64px] z-10">
  <div class="relative max-w-[996px] mx-auto w-full lg:p-2 p-4 pt-6 lg:min-h-[calc(100dvh-64px)] lg:flex lg:flex-col lg:justify-center max-lg:px-0 max-lg:pt-12 max-lg:pb-0 fira_sans_29488ef3-module__KB-tEG__variable">

    <!-- Mobile Part Selection Bar -->
    <div class="lg:hidden fixed top-16 left-0 right-0 z-30 h-12 flex items-center gap-2 px-3 bg-white border-b border-zinc-200">
      <div class="min-w-0 flex-1">
        <button type="button" id="mobilePartBtn" class="flex w-full min-w-0 items-center gap-2 h-10 -ml-1 pl-1 pr-1.5 rounded-xl active:bg-zinc-100 transition-colors">
          <span class="shrink-0 w-7 h-7 rounded-lg flex items-center justify-center border bg-emerald-50 border-emerald-200">
            <svg class="lucide lucide-ear w-4 h-4 text-emerald-700" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M6 8.5a6.5 6.5 0 1 1 13 0c0 6-6 6-6 10a3.5 3.5 0 1 1-7 0"></path><path d="M15 8.5a2.5 2.5 0 0 0-5 0v1a2 2 0 1 1 0 4"></path></svg>
          </span>
          <span class="min-w-0 flex flex-col text-left leading-tight">
            <span class="text-[10px] font-semibold text-zinc-500 truncate" id="mobilePartLabel">Listening Part 1</span>
            <span class="text-[13px] font-bold text-zinc-800 truncate" id="mobilePartName">Listening to Problem Solving</span>
          </span>
          <svg class="lucide lucide-chevron-down w-4 h-4 text-zinc-400 shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"></path></svg>
        </button>
      </div>
    </div>

    <!-- Side Vertical Parts Indicator (Desktop) -->
    <nav aria-label="Exam parts" class="absolute right-full top-1/2 z-30 mr-3 hidden -translate-y-1/2 flex-col gap-[7px] xl:flex" id="sidePartsNav">
      <!-- Injected by exam_runner.js -->
    </nav>

    <!-- Part Selector Popover (4 Columns) -->
    <div class="hidden absolute top-16 left-6 z-50 w-[820px] max-w-[calc(100vw-3rem)] max-h-[calc(100vh-120px)] overflow-y-auto overflow-x-hidden rounded-2xl border border-zinc-200 bg-white text-zinc-900 shadow-2xl transition-all" id="partMenuPopover">
      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-px bg-zinc-100 p-0" id="partsList">
        <!-- Injected by exam_runner.js -->
      </div>
    </div>

    <!-- MAIN SIMULATOR CARD -->
    <div class="bg-white rounded-2xl w-full h-full flex flex-col lg:overflow-hidden border border-zinc-300 shadow lg:shadow-sm lg:h-[min(880px,calc(100dvh-124px))] max-lg:h-[calc(100dvh-112px)] max-lg:overflow-hidden max-lg:rounded-none max-lg:border-0 max-lg:shadow-none max-lg:bg-zinc-100">
      
      <!-- Card Header -->
      <header class="hidden lg:flex flex-col shrink-0 border-b border-zinc-300 bg-gradient-to-b from-zinc-100 to-zinc-200">
        <div class="flex items-center gap-3.5 px-5 py-3.5">
          <div class="min-w-0 flex-1 flex">
            <div class="min-w-0 flex-1">
              <button type="button" aria-haspopup="dialog" id="partSelectorBtn" class="group flex min-w-0 max-w-full flex-col items-start rounded-lg text-left focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-900 focus-visible:ring-offset-2 cursor-pointer" aria-expanded="false">
                <span class="flex min-w-0 max-w-full items-center gap-2">
                  <span class="truncate text-[17px] font-bold leading-snug text-zinc-900" id="partHeading">Listening Part 1: Listening to Problem Solving</span>
                  <span aria-hidden="true" class="flex h-6 w-6 shrink-0 items-center justify-center rounded-md border border-zinc-300 bg-white text-zinc-700 shadow-sm transition-colors group-hover:border-zinc-400 group-hover:bg-zinc-50">
                    <svg class="lucide lucide-chevron-down h-4 w-4" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"></path></svg>
                  </span>
                </span>
                <span class="mt-0.5 truncate text-[13px] font-medium text-zinc-500" id="examTitle">Exam 1</span>
              </button>
            </div>
          </div>
          <div class="flex items-center gap-2.5 shrink-0" id="headerRightSlot">
            <p role="timer" aria-live="off" class="hidden items-center gap-1.5 shrink-0 whitespace-nowrap font-medium tabular-nums text-[13px] lg:text-[14px] text-zinc-500" id="timer">
              <svg class="lucide lucide-timer w-4 h-4 shrink-0 text-zinc-900" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="10" x2="14" y1="2" y2="2"></line><line x1="12" x2="15" y1="14" y2="11"></line><circle cx="12" cy="14" r="8"></circle></svg>
              <span class="hidden lg:inline">Time remaining:</span>
              <b class="font-bold text-zinc-900" id="timerDisplay">27 seconds</b>
            </p>
            <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 cursor-pointer" id="headerNextBtn" type="button">
              Next
              <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
            </button>
          </div>
        </div>
        <div class="h-[3px] w-full bg-zinc-300" role="presentation">
          <div class="h-full rounded-r-full bg-zinc-900 transition-[width] duration-300 ease-out motion-reduce:transition-none" id="progressBar" style="width: 0%;"></div>
        </div>
      </header>

      <!-- Pro Member Banner -->
      <div class="flex shrink-0 items-center justify-center gap-4 border-b border-zinc-200 bg-blue-50 px-4 py-2 text-[13px] font-medium text-blue-900 max-lg:mx-3 max-lg:mt-3 max-lg:rounded-2xl max-lg:border">
        <p>Mock exams are for <b class="font-bold">Pro Members</b>.</p>
        <button class="inline-flex items-center justify-center whitespace-nowrap text-sm ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-secondary main2-btn text-zinc-900 rounded-xl border border-green-400 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 font-bold cursor-pointer" type="button">
          <svg class="lucide lucide-gem w-5 h-5 text-green-700 fill-green-100 mr-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M10.5 3 8 9l4 13 4-13-2.5-6"></path><path d="M17 3a2 2 0 0 1 1.6.8l3 4a2 2 0 0 1 .013 2.382l-7.99 10.986a2 2 0 0 1-3.247 0l-7.99-10.986A2 2 0 0 1 2.4 7.8l2.998-3.997A2 2 0 0 1 7 3z"></path><path d="M2 9h20"></path></svg>
          Upgrade
        </button>
      </div>

      <!-- Main Stage Container -->
      <div class="relative flex flex-col w-full flex-1 min-h-0 lg:overflow-hidden lg:[&>*]:flex-1 lg:[&>*]:min-h-0 max-lg:overflow-y-auto max-lg:overscroll-contain max-lg:pb-[calc(6.5rem+env(safe-area-inset-bottom,0px))]">
        
        <!-- STAGE 0: Instructions Screen -->
        <div class="p-4 lg:p-6 h-full overflow-y-auto overscroll-contain max-lg:h-auto max-lg:overflow-visible max-lg:mx-3 max-lg:mt-3 max-lg:w-auto max-lg:rounded-2xl max-lg:border max-lg:border-zinc-200 max-lg:bg-white max-lg:shadow-sm" id="stageInstructions">
          <p class="font-practice flex items-start gap-2 text-base font-medium text-[#1a578a]">
            <svg class="lucide lucide-info mt-[3px] h-4 w-4 shrink-0 fill-[#1a578a] text-[#1a578a] [&>path]:stroke-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
            <span id="instructionHeader">Listening to Problem Solving</span>
          </p>
          <ul class="mt-2 max-w-2xl divide-y divide-zinc-200 lg:ml-6" id="instructionsList">
            <!-- Bullets inserted dynamically -->
          </ul>
          <button class="items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 mt-5 hidden lg:inline-flex cursor-pointer" id="startPracticeBtn" type="button">
            Start
            <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
          </button>
        </div>

        <!-- STAGE 1: Stimulus Presentation Screen -->
        <div class="hidden lg:p-6 p-4 w-full flex flex-col items-start overflow-y-auto overscroll-contain max-lg:overflow-visible max-lg:mx-3 max-lg:mt-3 max-lg:w-auto max-lg:rounded-2xl max-lg:border max-lg:border-zinc-200 max-lg:bg-white max-lg:shadow-sm" id="stageStimulus">
          <p class="font-practice flex items-start gap-2 text-base font-medium text-[#1a578a]">
            <svg class="lucide lucide-info mt-[3px] h-4 w-4 shrink-0 fill-[#1a578a] text-[#1a578a] [&>path]:stroke-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
            <span id="stimulusHeader">Instructions:</span>
          </p>
          <div class="mt-3 lg:pl-6 font-semibold font-practice text-[14px] leading-6 text-zinc-800" id="stimulusTextContainer">
            <p class="text-[14px] mb-2" id="stimulusPromptText"></p>
          </div>
          <!-- Stimulus Image -->
          <div class="hidden mt-3 lg:ml-6 w-full max-w-[660px]" id="imageSection">
            <img alt="Stimulus" id="partImage" class="w-full h-auto rounded-lg border border-zinc-200 object-contain max-h-[440px]" src="" />
          </div>
          <!-- Stimulus Audio -->
          <div class="hidden mt-4 lg:ml-6 w-full max-w-[660px]" id="stimulusAudioSection">
            <div class="w-full rounded-2xl border border-zinc-200 bg-white shadow-sm p-4" id="stimulusAudioPlayerContainer">
              <!-- Rendered by exam_runner.js -->
            </div>
          </div>
        </div>

        <!-- STAGE 2: Questions View (2-Column Grid) -->
        <div class="hidden grid lg:grid-cols-2 grid-cols-1 shrink-0 w-full h-full grow divide-y lg:divide-y-0 lg:divide-x divide-zinc-300 max-lg:block max-lg:h-auto max-lg:overflow-visible max-lg:divide-y-0" id="stageQuestions">
          <!-- Left Column: Audio / Passage / Transcript -->
          <div class="lg:p-6 p-4 lg:py-6 lg:bg-[#f5f5f5] overflow-y-auto max-lg:overflow-visible [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:bg-zinc-300 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-zinc-100 max-lg:mx-3 max-lg:mt-3 max-lg:w-auto max-lg:rounded-2xl max-lg:border max-lg:border-zinc-200 max-lg:bg-white max-lg:shadow-sm" id="questionLeftPane">
            <p class="font-practice flex items-start gap-2 text-base font-medium text-[#1a578a] mb-4">
              <svg class="lucide lucide-info mt-[3px] h-4 w-4 shrink-0 fill-[#1a578a] text-[#1a578a] [&>path]:stroke-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
              <span id="questionLeftHeader">Listen to the question.</span>
            </p>

            <!-- Custom Audio Player Widget -->
            <div id="audioSection" class="w-full mb-3">
              <div class="w-full relative overflow-hidden rounded-2xl border border-zinc-200 bg-white shadow-sm">
                <audio id="questionAudioElem" playsinline="" preload="metadata" class="sr-only"></audio>
                <div class="px-3 py-2.5">
                  <div class="flex items-center gap-3">
                    <button type="button" id="qAudioPlayBtn" aria-label="Play" class="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-blue-600 text-white shadow-sm transition-all hover:-translate-y-0.5 hover:bg-blue-700 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 cursor-pointer">
                      <svg id="qAudioPlayIcon" class="lucide lucide-play h-5 w-5 translate-x-px" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2"><path d="M5 5a2 2 0 0 1 3.008-1.728l11.997 6.998a2 2 0 0 1 .003 3.458l-12 7A2 2 0 0 1 5 19z"></path></svg>
                    </button>
                    <div class="min-w-0 flex-1">
                      <div role="slider" id="qAudioSeekBar" tabindex="0" aria-label="Seek" class="group relative -my-2 block touch-pan-y py-2 focus-visible:outline-none cursor-pointer">
                        <div class="relative h-1.5 w-full overflow-hidden rounded-full bg-zinc-200">
                          <div class="absolute inset-y-0 left-0 rounded-full bg-zinc-300" style="width: 100%;"></div>
                          <div id="qAudioProgressFill" class="absolute inset-y-0 left-0 rounded-full bg-blue-600" style="width: 0%;"></div>
                        </div>
                        <div id="qAudioSeekThumb" aria-hidden="true" class="pointer-events-none absolute top-1/2 h-3 w-3 -translate-x-1/2 -translate-y-1/2 rounded-full bg-blue-600 shadow ring-2 ring-white transition-opacity opacity-0 group-hover:opacity-100" style="left: 0%;"></div>
                      </div>
                      <div class="mt-2 grid grid-cols-[1fr_auto_1fr] items-center gap-2">
                        <span id="qAudioCurrentTime" class="text-[12px] font-medium tabular-nums text-zinc-500">0:00</span>
                        <div class="flex items-center gap-1 justify-self-center">
                          <button type="button" id="qAudioBack10Btn" aria-label="Back 10 seconds" class="inline-flex h-7 items-center gap-0.5 rounded-lg px-1.5 text-zinc-500 transition-colors hover:bg-zinc-100 hover:text-zinc-800 cursor-pointer">
                            <svg class="lucide lucide-rotate-ccw h-3.5 w-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"></path><path d="M3 3v5h5"></path></svg>
                            <span class="text-[10px] font-bold tabular-nums">10</span>
                          </button>
                          <button type="button" id="qAudioFwd10Btn" aria-label="Forward 10 seconds" class="inline-flex h-7 items-center gap-0.5 rounded-lg px-1.5 text-zinc-500 transition-colors hover:bg-zinc-100 hover:text-zinc-800 cursor-pointer">
                            <span class="text-[10px] font-bold tabular-nums">10</span>
                            <svg class="lucide lucide-rotate-cw h-3.5 w-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 1 1-9-9c2.52 0 4.93 1 6.74 2.74L21 8"></path><path d="M21 3v5h-5"></path></svg>
                          </button>
                          <button type="button" id="qAudioSpeedBtn" class="inline-flex h-6 min-w-11 items-center justify-center rounded-lg border border-zinc-200 px-2 text-[11px] font-bold tabular-nums text-zinc-600 transition-colors hover:border-zinc-300 hover:text-zinc-800 cursor-pointer">1x</button>
                        </div>
                        <span id="qAudioDuration" class="justify-self-end text-[12px] font-medium tabular-nums text-zinc-500">0:00</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Reading Passage Section -->
            <div id="readingPassageSection" class="hidden bg-white p-5 rounded-2xl border border-zinc-200 text-sm leading-relaxed text-zinc-800 mb-3 font-practice max-h-[480px] overflow-y-auto">
            </div>

            <!-- Collapsible Transcript Accordion -->
            <div class="border border-zinc-200 rounded-xl bg-white mb-3 overflow-hidden" id="transcriptContainer">
              <button type="button" id="toggleTranscriptBtn" class="flex flex-1 items-center justify-between h-11 gap-2 px-3 py-0 text-[13px] font-semibold text-zinc-700 hover:bg-zinc-50 w-full cursor-pointer">
                <span class="flex items-center gap-2">
                  <svg class="lucide lucide-scroll-text h-4 w-4 shrink-0 text-zinc-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 12h-5"></path><path d="M15 8h-5"></path><path d="M19 17V5a2 2 0 0 0-2-2H4"></path><path d="M8 21h12a2 2 0 0 0 2-2v-1a1 1 0 0 0-1-1H11a1 1 0 0 0-1 1v1a2 2 0 1 1-4 0V5a2 2 0 1 0-4 0v2a1 1 0 0 0 1 1h3"></path></svg>
                  Question transcript
                </span>
                <svg id="transcriptChevron" class="lucide lucide-chevron-down h-4 w-4 shrink-0 text-zinc-400 transition-transform duration-200" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"></path></svg>
              </button>
              <div id="transcriptBox" class="hidden p-3.5 border-t border-zinc-200 text-xs font-practice text-zinc-700 leading-relaxed bg-zinc-50/50">
                <div id="transcriptContent"></div>
              </div>
            </div>

            <!-- Official Test Warning Notice -->
            <p class="text-[13px] leading-6 font-medium text-amber-900/80 w-full bg-amber-50 p-3 rounded-xl border border-amber-100">
              In the official test, you can't rewind or replay the audio, and there's no transcript.
            </p>
          </div>

          <!-- Right Column: Question + Options container -->
          <div class="p-6 lg:bg-[#eef8f9] h-full shrink-0 overflow-y-auto max-lg:h-auto max-lg:p-4 max-lg:overflow-visible [&::-webkit-scrollbar]:w-2 [&::-webkit-scrollbar-thumb]:bg-zinc-300 [&::-webkit-scrollbar-thumb]:rounded-full [&::-webkit-scrollbar-track]:bg-zinc-100 max-lg:mx-3 max-lg:mt-3 max-lg:w-auto max-lg:rounded-2xl max-lg:border max-lg:border-zinc-200 max-lg:bg-white max-lg:shadow-sm" id="questionRightPane">
            <p class="font-practice text-[14px] leading-6 mb-3 font-medium text-zinc-700" id="questionNumberLabel">Question 1 of 8</p>
            <p class="font-practice flex items-start gap-2 text-base font-medium text-[#1a578a] mb-3">
              <svg class="lucide lucide-info mt-[3px] h-4 w-4 shrink-0 fill-[#1a578a] text-[#1a578a] [&>path]:stroke-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><path d="M12 16v-4"></path><path d="M12 8h.01"></path></svg>
              <span id="questionPromptHeading">Choose the best answer to each question.</span>
            </p>
            <div id="questionsContainer" class="flex flex-col">
              <!-- Radiogroup options injected by exam_runner.js -->
            </div>
          </div>
        </div>

        <!-- STAGE WRITING -->
        <div class="hidden grid lg:grid-cols-2 grid-cols-1 shrink-0 w-full h-full grow divide-y lg:divide-y-0 lg:divide-x divide-zinc-300" id="stageWriting">
          <div class="p-6 bg-zinc-50 overflow-y-auto">
            <h3 class="font-bold text-zinc-900 text-base mb-3" id="writingPromptTitle">Writing Task</h3>
            <div class="font-practice text-sm leading-relaxed text-zinc-800 whitespace-pre-line" id="writingPromptText"></div>
          </div>
          <div class="p-6 bg-white flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between mb-2">
                <span class="text-xs font-bold text-zinc-600">Response</span>
                <span class="text-xs font-semibold text-blue-700 bg-blue-50 px-2 py-0.5 rounded-full" id="writingWordCount">Words: 0 / 150-200</span>
              </div>
              <textarea id="writingTextarea" class="w-full h-80 p-4 border border-zinc-200 rounded-xl focus:border-blue-500 focus:ring-2 focus:ring-blue-100 font-practice text-sm leading-relaxed resize-none" placeholder="Type your response here..."></textarea>
            </div>
            <div class="mt-4 pt-3 border-t border-zinc-100 flex items-center justify-between">
              <button type="button" id="writingModelAnswerBtn" class="text-xs font-semibold text-blue-600 hover:text-blue-800 underline">View CLB 10-12 Model Answer</button>
            </div>
          </div>
        </div>

        <!-- STAGE SPEAKING -->
        <div class="hidden p-6 lg:p-8 h-full overflow-y-auto flex flex-col items-center justify-center text-center" id="stageSpeaking">
          <div class="max-w-xl mx-auto w-full bg-zinc-50 border border-zinc-200 rounded-2xl p-6 shadow-sm">
            <span class="text-xs font-bold uppercase tracking-wider text-purple-700 bg-purple-100 px-2.5 py-1 rounded-full inline-block mb-3" id="speakingBadge">Speaking Task</span>
            <h3 class="text-lg font-bold text-zinc-900 mb-2" id="speakingPromptTitle">Speaking Prompt</h3>
            <p class="font-practice text-sm text-zinc-700 leading-relaxed mb-6 whitespace-pre-line" id="speakingPromptText"></p>
            <div class="flex items-center justify-center gap-4 py-4">
              <div class="p-4 rounded-full bg-purple-100 text-purple-800">
                <svg class="w-10 h-10 animate-pulse" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line></svg>
              </div>
            </div>
            <p class="text-xs text-zinc-500 font-medium" id="speakingStatusText">Preparation Time: 30 seconds</p>
          </div>
        </div>

        <!-- STAGE 3: Results / Answer Key Screen -->
        <div class="hidden p-6 lg:p-8 h-full overflow-y-auto" id="stageResults">
          <div class="max-w-3xl mx-auto flex flex-col gap-6">
            <div class="flex items-center justify-between p-6 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-700 text-white shadow-md">
              <div>
                <span class="text-xs uppercase tracking-wider font-semibold text-blue-200">Practice Complete</span>
                <h2 class="text-2xl font-bold mt-1" id="resultsTitle">Listening Part 1 Results</h2>
                <p class="text-sm text-blue-100 mt-0.5" id="resultsSubtitle">Exam 1 • CELPIP Practice</p>
              </div>
              <div class="text-right">
                <div class="text-3xl font-extrabold" id="scoreDisplay">8 / 8</div>
                <div class="text-xs font-semibold uppercase tracking-wider bg-white/20 px-2.5 py-1 rounded-full mt-1 inline-block" id="clbDisplay">CLB Level 10+</div>
              </div>
            </div>

            <div class="flex items-center justify-between pb-2 border-b border-zinc-200">
              <h3 class="font-bold text-zinc-900 text-lg">Detailed Answer Key &amp; Explanations</h3>
              <button id="retakeBtn" type="button" class="text-xs font-semibold text-blue-600 hover:text-blue-800 border border-blue-200 bg-white px-3 py-1.5 rounded-lg shadow-sm cursor-pointer">Restart Part</button>
            </div>

            <div class="space-y-4" id="resultsBreakdown">
              <!-- Explanations populated by exam_runner.js -->
            </div>
          </div>
        </div>

      </div>

      <!-- Footer (Desktop) -->
      <footer class="hidden lg:flex shrink-0 items-center justify-between gap-3 border-t border-zinc-300 bg-gradient-to-t from-zinc-100 to-zinc-200 px-5 py-3" id="examFooter">
        <a href="#" id="showAnswersBtn">
          <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-white white-btn text-zinc-900 rounded-xl border border-zinc-300 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 cursor-pointer" type="button">
            Answer Key &amp; Score
            <svg class="lucide lucide-arrow-up-right w-4 h-4 ml-1 text-blue-600" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path d="M7 7h10v10"></path><path d="M7 17 17 7"></path></svg>
          </button>
        </a>
        <div class="flex items-center gap-2.5">
          <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-white white-btn text-zinc-900 rounded-xl border border-zinc-300 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-4 py-2 cursor-pointer" aria-label="Previous step" id="footerBackBtn" type="button">
            <svg class="lucide lucide-arrow-left w-4 h-4 mr-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path></svg>
            Back
          </button>
          <button class="hidden inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold ring-offset-background transition-[color,background-color,border-color,box-shadow,transform] ease-out-strong active:scale-[0.98] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 h-10 px-6 py-2 shadow-sm cursor-pointer" id="submitBtn" type="button">
            Submit Answers
          </button>
        </div>
      </footer>

      <!-- Mobile Footer Action Bar -->
      <div class="lg:hidden fixed bottom-0 left-0 right-0 z-50 p-2 pointer-events-none touch-action-manipulation">
        <div class="absolute left-0 right-0 bottom-0 top-0 bg-background/10 backdrop-blur-lg pointer-events-none" style="mask-image:linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 50%);-webkit-mask-image:linear-gradient(to bottom, rgba(0, 0, 0, 0) 0%, rgb(0, 0, 0) 50%)"></div>
        <div class="relative mb-4 mx-auto w-fit max-w-[calc(100vw-1.5rem)] pointer-events-auto flex items-center gap-2">
          <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold bg-white white-btn rounded-xl border border-zinc-300 hover:-translate-y-0.5 active:translate-y-0 duration-200 shrink-0 h-11 w-11 p-0 shadow text-zinc-600" aria-label="Previous step" id="mobileBackBtn">
            <svg class="lucide lucide-arrow-left w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path></svg>
          </button>
          <button class="inline-flex items-center justify-center whitespace-nowrap font-semibold bg-primary blue-btn text-white rounded-xl border border-blue-800 hover:-translate-y-0.5 active:translate-y-0 duration-200 py-2 h-12 px-7 text-[15px] shadow" id="mobileNextBtn">
            Next
            <svg class="lucide lucide-arrow-right w-4 h-4 ml-2" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg>
          </button>
          <button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-semibold bg-white white-btn rounded-xl border border-zinc-300 hover:-translate-y-0.5 active:translate-y-0 duration-200 shrink-0 h-11 w-11 p-0 shadow text-zinc-600" aria-label="Answer key and score" id="mobileAnswersBtn">
            <svg class="lucide lucide-list-checks w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 5h8"></path><path d="M13 12h8"></path><path d="M13 19h8"></path><path d="m3 17 2 2 4-4"></path><path d="m3 7 2 2 4-4"></path></svg>
          </button>
        </div>
      </div>

    </div>

  </div>
</div>

<script src="/static/js/exam_runner.js"></script>
</body>
</html>
"""

final_html = template.replace("__NAV_HTML__", nav_html)

out_path = os.path.join(STATIC_DIR, "exam.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Saved exam.html successfully, length:", len(final_html))
