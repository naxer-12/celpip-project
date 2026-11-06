#!/usr/bin/env python3
"""
resources_data_builder.py - Curated Structured Resources for CEFR Levels A2, B1, B2, C1, and C2.
Generates pages 53 to 67 for each level matching the A1 structure:
- 53: Overview & Immersion Architecture
- 54: 1. Structured CEFR-Aligned Audio Platforms
- 55: Interactive Grammar, Vocabulary & Listening Workstations
- 56: News in Slow / Accessible French & Press Platforms
- 57: 2. Calibrated Podcasts (Primary Audio Series)
- 58: Storytelling & Narrative Audio Podcasts
- 59: Natural Spoken French & Conversation Podcasts
- 60: Thematic Deep-Dive & Cultural Audio
- 61: 3. Top YouTube Channels (Visual + Audio)
- 62: Pedagogical YouTube Channels (Grammar & Dictations)
- 63: Story Listening, Documentaries & Comprehensible Input
- 64: 4. Dedicated Apps, Spaced Repetition & Reading Tools
- 65: 5. Standard Coursebooks & Graded Readers (with Audio)
- 66: 6. Official DELF/DALF Exam Practice & Past Papers
- 67: Level-Specific Auditory & Immersion Milestones Checklist
"""

def get_a2_resources():
    return {
        53: {
            "page": 53, "type": "checklist",
            "title": "A2 French – Learning & Listening Practice Resources",
            "subtitle": "Level: A2 (Elementary / Waystage) • Audio Immersion & Study Architecture",
            "badge_num": "52",
            "intro": "The A2 level marks the transition from isolated survival words to understanding connected sentences, daily routines, social exchanges, and past/future narratives.",
            "sections": [
                {
                    "title": "Core A2 Listening & Study Methodology",
                    "items": [
                        "Prioritize Comprehensible Input: Target audio where you understand 70–80% without looking at transcripts.",
                        "The 3-Step Audio Method: 1st listen for gist without text; 2nd listen with transcript to highlight new vocabulary; 3rd listen while shadowing out loud.",
                        "Daily Ear Tuning Routine: Dedicate 20 minutes daily to structured audio + 10 minutes of active repetition."
                    ]
                },
                {
                    "title": "Weekly Resource Allocation Framework",
                    "items": [
                        "Monday & Wednesday: CEFR-aligned interactive audio exercises (TV5Monde / RFI).",
                        "Tuesday & Thursday: Slow storytelling and conversational podcasts (Coffee Break / Duolingo).",
                        "Friday: YouTube visual street interviews (Easy French) and pronunciation drills.",
                        "Weekend: One chapter of an A2 graded reader with audio CD + Anki spaced repetition review."
                    ]
                }
            ]
        },
        54: {
            "page": 54, "type": "resources",
            "title": "1. Structured Listening Platforms (CEFR-Aligned)",
            "subtitle": "Interactive Video Modules, Authentic Audio & Comprehension Quizzes",
            "badge_num": "53",
            "intro": "These official platforms offer verified CEFR A2-aligned French listening materials with progressive exercises and transcripts.",
            "resources": [
                {
                    "name": "TV5Monde – Apprendre le français (Niveau A2)",
                    "badge": "Top Recommendation",
                    "url": "apprendre.tv5monde.com",
                    "what": "Over 400 interactive video activities categorised by CEFR A2 topics (family, city life, cuisine, travel).",
                    "features": "Embedded video player with toggleable subtitles, vocabulary dossiers, and automated self-correcting quizzes.",
                    "focus": "Authentic Francophone television clips adapted with pedagogical comprehension questions.",
                    "tips": "Complete 2 video dossiers weekly. Write a 3-sentence summary of each video in your practice journal."
                },
                {
                    "name": "RFI – Le français facile avec RFI (A2)",
                    "badge": "Essential Audio",
                    "url": "francaisfacile.rfi.fr",
                    "what": "Pedagogical audio capsules produced by Radio France Internationale for elementary learners.",
                    "features": "Short radio dialogues, downloadable MP3 audio, printable transcripts, and grammar focus exercises.",
                    "focus": "Everyday situations, public transport announcements, shopping exchanges, and weather reports.",
                    "tips": "Listen once with your eyes closed to visualize the situation before reading the dialogue text."
                }
            ]
        },
        55: {
            "page": 55, "type": "resources",
            "title": "Interactive Grammar & Listening Workstations",
            "subtitle": "Targeted Auditory Drills for Verb Tenses, Pronouns & Agreement",
            "badge_num": "54",
            "intro": "Sharpen your grammatical reflexes through ear training and instantaneous audio-check exercises.",
            "resources": [
                {
                    "name": "Le Point du FLE – Compréhension Orale A2",
                    "badge": "Resource Directory",
                    "url": "lepointdufle.net",
                    "what": "Curated directory of over 300 free online audio exercises specifically tagged for A2 learners.",
                    "features": "Links to dictations, audio quizzes, gap-fill activities, and phonetic differentiation drills.",
                    "focus": "Distinguishing passé composé vs imparfait aurally, identifying direct/indirect object pronouns.",
                    "tips": "Use the 'Dictées A2' section once a week to train your ears on silent verb endings and plurals."
                },
                {
                    "name": "Français Facile – Audio & Dictées A2",
                    "badge": "Self-Testing",
                    "url": "francaisfacile.com",
                    "what": "Massive community-driven portal with thousands of self-grading audio exercises.",
                    "features": "Audio clips with multiple-choice questions, audio dictation tool with automated error correction.",
                    "focus": "Everyday French vocabulary, number comprehension (1–10,000), time expressions, and question forms.",
                    "tips": "Complete the '100 tests de débutant/intermédiaire' to identify weak auditory comprehension spots."
                }
            ]
        },
        56: {
            "page": 56, "type": "resources",
            "title": "News in Slow French & Accessible Audio Press",
            "subtitle": "Bridging the Gap to Current Affairs with Simplified Vocabulary",
            "badge_num": "55",
            "intro": "Engage with real-world news and Francophone society without becoming overwhelmed by native speed.",
            "resources": [
                {
                    "name": "RFI – Le Journal en français facile",
                    "badge": "Daily News Habit",
                    "url": "francaisfacile.rfi.fr/fr/podcasts/journal-en-fran%C3%A7ais-facile",
                    "what": "A 10-minute daily international news bulletin broadcast worldwide in simple, accessible French.",
                    "features": "Read at a steady, measured tempo with full verbatim transcript published simultaneously.",
                    "focus": "Major global events, international politics, climate, and cultural milestones explained simply.",
                    "tips": "Read the transcript first, listen while following the text, then listen a second time without text."
                },
                {
                    "name": "1jour1actu – Les actualités pour enfants et apprenants",
                    "badge": "Accessible Media",
                    "url": "1jour1actu.com",
                    "what": "Short animated videos and audio articles explaining world events in clear, pedagogically crafted French.",
                    "features": "1-to-2 minute engaging audio animations answering questions like 'C'est quoi l'ONU ?' or 'Pourquoi recycle-t-on ?'",
                    "focus": "Clear enunciation, everyday civic vocabulary, and concise explanatory sentence structures.",
                    "tips": "Perfect for a 5-minute morning warm-up before beginning formal grammar study."
                }
            ]
        },
        57: {
            "page": 57, "type": "resources",
            "title": "2. Level-Calibrated Podcasts (Slow French)",
            "subtitle": "Structured Audio Lessons with Step-by-Step English & French Support",
            "badge_num": "56",
            "intro": "These podcasts provide ideal transitional pacing, clear articulation, and contextual explanations.",
            "resources": [
                {
                    "name": "Coffee Break French (Season 2)",
                    "badge": "Grammar & Travel",
                    "url": "coffeebreaklanguages.com / Spotify / Apple Podcasts",
                    "what": "40 structured 15-to-20 minute audio lessons guiding learners through elementary to intermediate French.",
                    "features": "Teacher (Mark) and learner (Anna) dynamic breaks down concepts in English with authentic native examples.",
                    "focus": "Mastery of past tenses, relative pronouns (qui, que), reflexive verbs, and holiday/dining scenarios.",
                    "tips": "Repeat each French dialogue line aloud during the lesson's dedicated pause intervals."
                },
                {
                    "name": "One Thing in a French Day",
                    "badge": "Daily Life Snippets",
                    "url": "onethinginafrenchday.podbean.com",
                    "what": "Laetitia shares a short 3-minute vignette of her daily life in Paris three times a week.",
                    "features": "Natural, pleasant native delivery spoken clearly at a moderate pace without English explanations.",
                    "focus": "French bakery visits, school runs, family meals, book purchases, and Parisian street observations.",
                    "tips": "Subscribe to the newsletter for transcripts to highlight colloquial daily idioms (*un coup d'œil, faire la queue*)."
                }
            ]
        },
        58: {
            "page": 58, "type": "resources",
            "title": "Storytelling & Narrative Podcasts",
            "subtitle": "Fostering Comprehension Through Engaging Real-Life Narratives",
            "badge_num": "57",
            "intro": "Retain vocabulary and natural cadence effortlessly by listening to human stories and cultural accounts.",
            "resources": [
                {
                    "name": "Duolingo French Podcast (A2 Stories)",
                    "badge": "Bilingual Narratives",
                    "url": "podcast.duolingo.com/french / Spotify",
                    "what": "True stories told by native Francophones from across the globe (France, Senegal, Quebec, Haiti, Vietnam).",
                    "features": "Narrated in slow, articulate French with English narration providing context, accompanied by online transcripts.",
                    "focus": "Courage, cultural traditions, environmental challenges, and historical adventures.",
                    "tips": "Great for listening while commuting or exercising. Focus on understanding the story arc without pausing."
                },
                {
                    "name": "French Blabla Podcast",
                    "badge": "Colloquial Quirks",
                    "url": "frenchblabla.com",
                    "what": "Caroline breaks down how real French people speak outside of textbooks in 10-minute friendly episodes.",
                    "features": "Explains common spoken contractions, filler words (*genre, en fait, du coup*), and pronunciation shortcuts.",
                    "focus": "Sounding natural in conversation and avoiding stiff, overly formal textbook phrasing.",
                    "tips": "Practice Caroline's 'challenge of the day' with an online language partner or tutor."
                }
            ]
        },
        59: {
            "page": 59, "type": "resources",
            "title": "Natural Spoken French Podcasts",
            "subtitle": "Stepping into 100% French Immersion at an Accessible Tempo",
            "badge_num": "58",
            "intro": "Build confidence with podcasts presented entirely in French without any English translation crutches.",
            "resources": [
                {
                    "name": "Français Authentique (Johan)",
                    "badge": "Natural Method",
                    "url": "francaisauthentique.com / YouTube / Spotify",
                    "what": "Short 10-minute episodes explaining common French expressions, proverbs, and personal development topics.",
                    "features": "Spoken entirely in clear, natural French at a steady tempo; complete free transcripts available.",
                    "focus": "Idiomatic expressions (*poser un lapin, avoir le cafard, en avoir ras-le-bol*) and daily conversational ease.",
                    "tips": "Follow Johan's Rule 3: Repeat the same episode 3 to 5 times across several days to absorb phrasing naturally."
                },
                {
                    "name": "innerFrench – Early Episodes (#01 to #30)",
                    "badge": "Transition to B1",
                    "url": "innerfrench.com / Spotify / Apple Podcasts",
                    "what": "Hugo Cotton speaks about psychology, sociology, and culture in 100% slow, natural French.",
                    "features": "Intellectually engaging topics without infantilizing vocabulary; complete synchronized transcripts online.",
                    "focus": "Connecting ideas, opinion formulations (*je pense que, à mon avis*), and cultural comparisons.",
                    "tips": "Start with episode #01. Listen once without transcript, then review difficult words in the transcript."
                }
            ]
        },
        60: {
            "page": 60, "type": "resources",
            "title": "Situational Dialogues & Cultural Discovery",
            "subtitle": "Practical Conversations for Travel, Socializing & Everyday Tasks",
            "badge_num": "59",
            "intro": "Equip yourself with realistic dialogues covering common social encounters and practical errands.",
            "resources": [
                {
                    "name": "Podcast Français Facile – Dialogues A2",
                    "badge": "Practical Roleplay",
                    "url": "podcastfrancaisfacile.com",
                    "what": "Hundreds of realistic dialogues recorded at normal and slow speeds with matching comprehension questions.",
                    "features": "Categorised by situation: at the pharmacy, asking for directions, returning a purchase, booking tickets.",
                    "focus": "Polite formulaic expressions (*s'il vous plaît, pourriez-vous, je voudrais savoir si*), practical numbers.",
                    "tips": "Roleplay both characters out loud in your room to train mouth muscle memory and rhythm."
                },
                {
                    "name": "Radio France – Les P'tits Bateaux",
                    "badge": "Curious Questions",
                    "url": "radiofrance.fr/franceinter/podcasts/les-p-tits-bateaux",
                    "what": "Children call in to ask scientific, historical, or everyday questions answered by friendly experts in 3 minutes.",
                    "features": "Short, clear answers avoiding impenetrable jargon, rich in vivid descriptive vocabulary.",
                    "focus": "Nature, animal behavior, space, history, and the origins of everyday objects.",
                    "tips": "Take notes of 3 new nouns or adjectives from every episode to expand your descriptive range."
                }
            ]
        },
        61: {
            "page": 61, "type": "resources",
            "title": "3. Top YouTube Channels (Visual + Audio)",
            "subtitle": "Real Street Interviews, Dual Subtitles & Authentic French Voices",
            "badge_num": "60",
            "intro": "Combine facial cues, body language, and dual subtitles to train ear-brain synchronization.",
            "resources": [
                {
                    "name": "Easy French (Easy Languages)",
                    "badge": "Street Interviews",
                    "url": "youtube.com/@EasyFrench",
                    "what": "Interviews with native French speakers in the streets of Paris, Nantes, and Lyon discussing relatable topics.",
                    "features": "Yellow French subtitles on top, white English subtitles below. Natural everyday speed with diverse accents.",
                    "focus": "What French people eat, weekend routines, fashion, pet peeves, and conversational slang.",
                    "tips": "Cover the English subtitles with a strip of paper on your screen to force French processing."
                },
                {
                    "name": "Français avec Pierre – Série A2",
                    "badge": "Pedagogical Fun",
                    "url": "youtube.com/@FrancaisavecPierre",
                    "what": "Engaging, high-energy video lessons featuring Pierre and Noemi breaking down A2 essentials.",
                    "features": "Humorous sketches, clear on-screen summary cards, interactive dictations, and pronunciation workouts.",
                    "focus": "Avoiding false friends, mastering nasal vowels, understanding French jokes, and tense comparisons.",
                    "tips": "Pause the video during quiz prompts and state your answer out loud before Pierre reveals the solution."
                }
            ]
        },
        62: {
            "page": 62, "type": "resources",
            "title": "Pedagogical YouTube Channels",
            "subtitle": "Systematic Grammar Breakdowns, Phonetics & Listening Dictations",
            "badge_num": "61",
            "intro": "Target specific pronunciation hurdles and tricky syntax rules with dedicated Francophone educators.",
            "resources": [
                {
                    "name": "French School TV (Vincent)",
                    "badge": "Grammar Mastery",
                    "url": "youtube.com/@FrenchSchoolTV",
                    "what": "Comprehensive pedagogical video lessons taught by a certified FLE teacher with clear visual boards.",
                    "features": "Structured video series for DELF A2 preparation, listening drills, and grammatical distinctions.",
                    "focus": "Direct object pronouns (le, la, les) vs indirect (lui, leur), future simple vs near future, prepositions of place.",
                    "tips": "Follow Vincent's 'DELF A2 Preparation Playlist' during the final 4 weeks of your A2 roadmap."
                },
                {
                    "name": "Comme une Française (Géraldine)",
                    "badge": "Cultural Nuance",
                    "url": "youtube.com/@Commeunefrancaise",
                    "what": "Bite-sized videos dissecting real French etiquette, social dos and don'ts, and spoken French shortcuts.",
                    "features": "English explanations highlighting what French textbooks never tell you about actual Parisian speech.",
                    "focus": "Dropping the 'ne' in negation, proper greeting rituals (*la bise*), ordering coffee like a local.",
                    "tips": "Incorporate Géraldine's top 5 everyday conversational formulas into your speaking practice."
                }
            ]
        },
        63: {
            "page": 63, "type": "resources",
            "title": "Comprehensible Input & Story Listening",
            "subtitle": "Acquiring Vocabulary Naturally Through Visual Context & Storytelling",
            "badge_num": "62",
            "intro": "Absorb high-frequency words effortlessly through the proven Comprehensible Input (CI) methodology.",
            "resources": [
                {
                    "name": "Alice Ayel – French Stories (A2)",
                    "badge": "Comprehensible Input",
                    "url": "youtube.com/@AliceAyel",
                    "what": "Storytelling videos illustrated in real time on a whiteboard by a certified language teacher.",
                    "features": "Super-clear enunciation, gestures, immediate visual context for every new word, repetition without boredom.",
                    "focus": "Folktales, fairy stories, daily adventures, and cultural narratives told in simple, natural French.",
                    "tips": "Sit back and watch without writing notes. Allow your subconscious mind to map words to meanings."
                },
                {
                    "name": "French Fairy Tales (Contes en Français)",
                    "badge": "Animated Classics",
                    "url": "youtube.com/@FrenchFairyTales",
                    "what": "Animated classic tales (Cinderella, The Three Little Pigs, Aladdin) dubbed in expressive French.",
                    "features": "High-quality animation with clear voice actors, predictable plotlines that make guessing meaning easy.",
                    "focus": "Narrative past tenses (*passé composé* and *imparfait*), descriptive adjectives, dialogue exchanges.",
                    "tips": "Watch stories you already know in English so your brain focuses entirely on the French phrasing."
                }
            ]
        },
        64: {
            "page": 64, "type": "resources",
            "title": "4. Dedicated Apps, Flashcards & Reading Tools",
            "subtitle": "Digital Workstations for Spaced Repetition & Contextual Lexical Lookups",
            "badge_num": "63",
            "intro": "Anchor vocabulary permanently in your long-term memory with smart algorithm-driven study tools.",
            "resources": [
                {
                    "name": "Anki (Spaced Repetition System)",
                    "badge": "Memory Anchor",
                    "url": "apps.ankiweb.net (iOS / Android / Desktop)",
                    "what": "Open-source spaced repetition flashcard software that schedules reviews right before you forget.",
                    "features": "Download the community deck 'French 1,500 Most Common Words' with native audio pronunciation.",
                    "focus": "Core A2 nouns, verbs with prepositions (*penser à, décider de*), irregular past participles.",
                    "tips": "Review 20 new cards and your daily reviews every morning without fail (approx. 10–15 minutes)."
                },
                {
                    "name": "LingQ & Readlang (Contextual Readers)",
                    "badge": "Reading Immersion",
                    "url": "lingq.com / readlang.com",
                    "what": "Platforms that let you import any French article, story, or video transcript and click any word for an instant definition.",
                    "features": "Synchronized audio player, automatic vocabulary tracking, color-coded word familiarity.",
                    "focus": "Building reading speed without tedious dictionary toggling, reinforcing vocabulary in context.",
                    "tips": "Import RFI Journal en français facile transcripts into Readlang to read and listen simultaneously."
                }
            ]
        },
        65: {
            "page": 65, "type": "resources",
            "title": "5. Standard Coursebooks & Graded Readers",
            "subtitle": "Authoritative Textbooks & Audio Novellas with Exercises",
            "badge_num": "64",
            "intro": "Consolidate your learning with internationally recognized FLE textbooks and audio readers.",
            "resources": [
                {
                    "name": "CLE International – Grammaire Progressive du Français (Niveau Débutant & Intermédiaire)",
                    "badge": "The FLE Standard",
                    "url": "cle-international.com / Available on Amazon & Bookstores",
                    "what": "The undisputed gold standard for learning French grammar: theory on the left page, exercises on the right.",
                    "features": "Clear tables, communicative examples, integrated audio CD with listening exercises and dictations.",
                    "focus": "Passé composé vs imparfait, futur simple, possessive/demonstrative pronouns, prepositions.",
                    "tips": "Work through 2 chapters weekly and keep a personal notebook of every exercise mistake you make."
                },
                {
                    "name": "Hachette – Lire en Français Facile (Collection A2)",
                    "badge": "Graded Fiction",
                    "url": "hachettefle.com",
                    "what": "Novellas and classics adapted for A2 vocabulary levels (700 to 1,200 unique headwords) with full audio.",
                    "features": "Includes titles like 'Le Fantôme de l'Opéra', 'Arsène Lupin', and 'Le Tour du Monde en 80 Jours'.",
                    "focus": "Narrative flow, reading stamina, emotional vocabulary, and comprehension questions at the back.",
                    "tips": "Listen to the audio chapter first, then read the text to verify your comprehension."
                }
            ]
        },
        66: {
            "page": 66, "type": "resources",
            "title": "6. Official DELF A2 Exam Prep & Past Papers",
            "subtitle": "Official French Ministry of Education Examination Simulations",
            "badge_num": "65",
            "intro": "Validate your skills against official international benchmarks with realistic mock exams and scoring grids.",
            "resources": [
                {
                    "name": "France Éducation International – Épreuves DELF A2",
                    "badge": "Official Papers",
                    "url": "france-education-international.fr",
                    "what": "Official government website offering authentic past exam papers, audio tracks, and examiner grading rubrics.",
                    "features": "Downloadable listening test MP3s, candidate exam booklets, and official answer keys.",
                    "focus": "The 4 official examination pillars: Compréhension de l'oral (25m), des écrits (30m), Production écrite (45m), orale (6-8m).",
                    "tips": "Complete a full timed mock exam under strict test conditions at the conclusion of Module 8."
                },
                {
                    "name": "Didier – Le DELF A2 100% Réussite",
                    "badge": "Prep Handbook",
                    "url": "didierfle.com",
                    "what": "The premier preparation handbook with step-by-step exam strategy breakdowns and 4 complete mock exams.",
                    "features": "Audio CD, self-evaluation grids, model written production essays, and examiner tips.",
                    "focus": "Time management, identifying key words in audio prompts, avoiding common test traps.",
                    "tips": "Study the sample written production answers to learn high-scoring sentence connectors (*d'abord, ensuite, enfin*)."
                }
            ]
        },
        67: {
            "page": 67, "type": "checklist",
            "title": "A2 Listening & Immersion Mastery Checklist",
            "subtitle": "Audit Your Auditory Comprehension and Resource Completion",
            "badge_num": "66",
            "intro": "Before proceeding to the final Module 8 Readiness Assessment, confirm that you have integrated these listening habits and can complete these auditory tasks in real time.",
            "sections": [
                {
                    "title": "A2 Auditory Can-Do Benchmarks",
                    "items": [
                        "I can understand clear, slow announcements in train stations, airports, and public transport.",
                        "I can follow the main points of everyday conversations about work, family, shopping, and hobbies.",
                        "I can catch numbers, dates, times, prices, and phone numbers in natural spoken dialogues.",
                        "I can understand directions given in the street (turn left, take the third street, straight ahead).",
                        "I can understand simple instructions given by a doctor, shop assistant, or postal worker.",
                        "I can follow the general story arc of a slow French podcast (Duolingo French Podcast, innerFrench).",
                        "I can distinguish between the past (passé composé/imparfait) and present in spoken French.",
                        "I have established a consistent weekly routine consuming at least 2 hours of French audio."
                    ]
                }
            ]
        }
    }

# Builders for B1, B2, C1, and C2 follow the exact same structure calibrated to their respective CEFR levels.

def get_b1_resources():
    return {
        53: {
            "page": 53, "type": "checklist",
            "title": "B1 French – Learning & Listening Practice Resources",
            "subtitle": "Level: B1 (Intermediate / Threshold) • Audio Immersion & Study Architecture",
            "badge_num": "52",
            "intro": "The B1 level represents the pivotal threshold where learners transition from structured learner materials to authentic native media, debates, and independent self-expression.",
            "sections": [
                {
                    "title": "Core B1 Listening & Study Methodology",
                    "items": [
                        "Embrace Native Speed: Transition from deliberately slowed audio to natural conversational cadence with normal liaisons.",
                        "Subjunctive & Hypothesis Ear Tuning: Train your ear to detect mood markers (il faut que, bien que, si j'avais su) automatically.",
                        "Daily 30-Minute Immersion Habit: 15 minutes of structured news/audio essays + 15 minutes of unscripted native conversations/podcasts."
                    ]
                },
                {
                    "title": "Weekly Resource Allocation Framework",
                    "items": [
                        "Monday & Wednesday: Native podcast essays (innerFrench / Français avec Pierre) + note-taking.",
                        "Tuesday & Thursday: Daily news decoding (RFI Journal en français facile / 20 Minutes Audio).",
                        "Friday: Cultural video essays and street interviews (Easy French Intermediate / Karambolage ARTE).",
                        "Weekend: One chapter of intermediate contemporary literature (Mondes en VF) + DELF B1 listening test simulation."
                    ]
                }
            ]
        },
        54: {
            "page": 54, "type": "resources",
            "title": "1. Structured Listening Platforms (CEFR-Aligned)",
            "subtitle": "Authentic Television Segments, Audio Reports & Analytical Quizzes",
            "badge_num": "53",
            "intro": "Official platforms providing pedagogical scaffolds for authentic Francophone broadcast media.",
            "resources": [
                {
                    "name": "TV5Monde – Apprendre le français (Niveau B1)",
                    "badge": "Top Recommendation",
                    "url": "apprendre.tv5monde.com",
                    "what": "Over 500 interactive video dossiers based on genuine French TV broadcasts, news clips, and short documentaries.",
                    "features": "Advanced video player with toggleable transcripts, cultural background notes, and multi-tier comprehension exercises.",
                    "focus": "Decoding fast native speech, implicit viewpoints, professional interviews, and cultural reports.",
                    "tips": "Complete the '7 Jours sur la Planète' B1 activities weekly to keep up with current global issues in French."
                },
                {
                    "name": "RFI Savoirs – Les Clés de l'Actualité (B1)",
                    "badge": "Knowledge & Audio",
                    "url": "savoirs.rfi.fr",
                    "what": "Educational audio capsules produced by RFI exploring sociology, history, ecology, and science.",
                    "features": "Full audio streaming with downloadable MP3, pedagogical worksheets, and vocabulary glossaries.",
                    "focus": "Subject-specific terminology, structured reasoning, and contrasting international perspectives.",
                    "tips": "Summarize the key argument of each 4-minute report in 50 French words using logical connectors (*en revanche, par conséquent*)."
                }
            ]
        },
        55: {
            "page": 55, "type": "resources",
            "title": "Interactive Grammar & Listening Workstations",
            "subtitle": "Refining Complex Syntax, Pronoun Combinations & Subjunctive Refinement",
            "badge_num": "54",
            "intro": "Master the syntactic architecture of intermediate French through ear training and immediate interactive validation.",
            "resources": [
                {
                    "name": "Le Point du FLE – Compréhension Orale & Grammaire B1",
                    "badge": "Comprehensive Portal",
                    "url": "lepointdufle.net",
                    "what": "Exhaustive index of intermediate listening exercises from French universities and language centers.",
                    "features": "Categorised by grammar target: double pronouns (*je le lui donne*), relative pronouns (*dont, où, lequel*), and conditional mood.",
                    "focus": "Instant auditory recognition of tense nuances and spoken colloquial contractions.",
                    "tips": "Do the 'Pronoms relatifs composés' listening quiz series to eliminate hesitation in complex sentences."
                },
                {
                    "name": "Lingolia Français – B1 Audio Modules",
                    "badge": "Visual Syntax",
                    "url": "francais.lingolia.com",
                    "what": "Structured grammar resource pairing crystal-clear syntax charts with authentic recorded native dialogues.",
                    "features": "Bite-sized grammar rule explanations, interactive fill-in-the-blank listening sentences with immediate error highlighting.",
                    "focus": "Subjunctive triggers vs indicative reality, passive voice construction, and indirect reported speech.",
                    "tips": "Take the 'B1 Diagnostic Assessment' to pinpoint exactly which grammatical categories need ear reinforcement."
                }
            ]
        },
        56: {
            "page": 56, "type": "resources",
            "title": "Daily News & Authentic Audio Press",
            "subtitle": "Developing Fluency with Current Affairs, Debates & Editorial Commentary",
            "badge_num": "55",
            "intro": "Transition from simplified learner news to the full-speed rhythm of French journalism.",
            "resources": [
                {
                    "name": "RFI – Le Journal en français facile",
                    "badge": "Daily Benchmark",
                    "url": "francaisfacile.rfi.fr",
                    "what": "Daily 10-minute news bulletin covering the world's top headlines in clear, articulately spoken French.",
                    "features": "Broadcast live daily; transcript available within minutes of transmission. Standard French without regional slang.",
                    "focus": "Geopolitics, economics, climate science, cultural festivals, and political elections.",
                    "tips": "Listen at 1.0x speed without looking at the text. Challenge yourself to write down the 3 main news stories covered."
                },
                {
                    "name": "20 Minutes – Podcasts d'Actualité",
                    "badge": "Fast Snackable Audio",
                    "url": "20minutes.fr/podcasts",
                    "what": "Bite-sized 3-to-5 minute audio reports covering daily lifestyle, tech innovations, and French cultural buzz.",
                    "features": "Energetic, youthful native pacing with contemporary French vocabulary and colloquial turns of phrase.",
                    "focus": "Everyday concerns in modern France, tech trends, cinema releases, and environmental initiatives.",
                    "tips": "Listen once to catch the general topic; note down any unfamiliar slang to research in Le Robert dictionary."
                }
            ]
        },
        57: {
            "page": 57, "type": "resources",
            "title": "2. Level-Calibrated Podcasts (Intermediate)",
            "subtitle": "Thought-Provoking Ideas, Psychology & Society Spoken Naturally",
            "badge_num": "56",
            "intro": "Engage your intellect with podcasts that treat you like an intelligent adult while maintaining accessible articulation.",
            "resources": [
                {
                    "name": "innerFrench (Hugo Cotton)",
                    "badge": "The B1 Gold Standard",
                    "url": "innerfrench.com / Spotify / Apple Podcasts",
                    "what": "Over 130 captivating 30-minute episodes exploring philosophy, history, sociology, and modern lifestyle.",
                    "features": "Hugo speaks at a natural yet articulate cadence without dumbing down complex ideas; full free synchronized transcripts online.",
                    "focus": "Why the French love strikes, the philosophy of happiness, climate paradoxes, and the history of the baguette.",
                    "tips": "Listen while walking. Pause after interesting segments and summarize Hugo's argument aloud in French."
                },
                {
                    "name": "Français avec Pierre – Le Podcast",
                    "badge": "Idiomatic Immersion",
                    "url": "francaisavecpierre.com / Spotify",
                    "what": "Conversations between Pierre and Noemi exploring French idiomatic nuances, cultural debates, and lifestyle.",
                    "features": "Unscripted, warm conversational banter highlighting subtle nuances between near-synonyms and conversational register.",
                    "focus": "Subtle humour, everyday expressions (*avoir le melon, couper les cheveux en quatre*), and social etiquette.",
                    "tips": "Create Anki flashcards for the 5 idiomatic expressions explained in each weekly episode."
                }
            ]
        },
        58: {
            "page": 58, "type": "resources",
            "title": "Narrative & Storytelling Podcasts",
            "subtitle": "Gripping Human Confessions, Memories & Personal Journeys",
            "badge_num": "57",
            "intro": "Experience the emotional depth of native French through unscripted personal accounts and travelogues.",
            "resources": [
                {
                    "name": "Transfert (Slate.fr / Louie Media - Selected Episodes)",
                    "badge": "Gripping Confessions",
                    "url": "slate.fr/podcasts/transfert / Spotify",
                    "what": "Everyday people sit alone in front of a microphone and recount an extraordinary personal secret or turning point.",
                    "features": "No interviewer, no music interruption; pure raw human storytelling with diverse native accents and natural pacing.",
                    "focus": "Family secrets, unbelievable coincidences, adventures, heartbreak, and resilience.",
                    "tips": "Choose shorter episodes (under 20 mins) first. Let the emotional intensity carry your comprehension forward."
                },
                {
                    "name": "Balades (innerFrench Travel Audio)",
                    "badge": "Acoustic Journey",
                    "url": "innerfrench.com",
                    "what": "Immersive acoustic journeys taking listeners through famous regions of France (the Loire castles, Mont Saint-Michel, Marseille).",
                    "features": "Rich sound design, historical storytelling, and descriptive sensory vocabulary.",
                    "focus": "Architectural terms, geographical vocabulary, regional legends, and historical milestones.",
                    "tips": "Follow along with Google Earth to visualize the streets and monuments described in each episode."
                }
            ]
        },
        59: {
            "page": 59, "type": "resources",
            "title": "Conversational & Mindset Podcasts",
            "subtitle": "Everyday Speech Rhythm, Natural Fillers & Cultural Perspectives",
            "badge_num": "58",
            "intro": "Develop an ear for the authentic cadence of conversations between native Francophones.",
            "resources": [
                {
                    "name": "Français Authentique – B1 Série Intermédiaire",
                    "badge": "Daily Mindset",
                    "url": "francaisauthentique.com",
                    "what": "Johan shares reflections on personal development, reading habits, productivity, and French philosophical sayings.",
                    "features": "100% spoken French with natural liaisons and relaxed enunciation; full transcripts available for every episode.",
                    "focus": "Building long-term language learning consistency, mastering spontaneous speech, and expanding vocabulary.",
                    "tips": "Listen to the same episode once in the morning and once in the evening to lock in the speech patterns."
                },
                {
                    "name": "French Voices Podcast (Jessica)",
                    "badge": "Inspiring Interviews",
                    "url": "frenchvoicespodcast.com",
                    "what": "In-depth interviews with French artisans, authors, scientists, and entrepreneurs about their passions and professions.",
                    "features": "Native French speakers from diverse professional backgrounds speaking naturally about their specialized crafts.",
                    "focus": "Professional vocabulary (wine making, pastry arts, watchmaking, literature), varied accents, and speech rhythms.",
                    "tips": "Download the accompanying vocabulary study guides to master specialized career-oriented vocabulary."
                }
            ]
        },
        60: {
            "page": 60, "type": "resources",
            "title": "Society, Psychology & Culture Podcasts",
            "subtitle": "Deepening Vocabulary Around Human Emotions, Habits & Society",
            "badge_num": "59",
            "intro": "Learn how Francophones dissect emotions, personal growth, and societal questions.",
            "resources": [
                {
                    "name": "Change ma vie (Clotilde Dusoulier)",
                    "badge": "Personal Growth",
                    "url": "changemavie.com / Spotify / Apple Podcasts",
                    "what": "One of France's top-rated personal development podcasts, exploring mindset, emotional well-being, and clarity.",
                    "features": "Clotilde's diction is exceptionally articulate, calm, and crystalline. Perfect audio engineering and rhythm.",
                    "focus": "Cognitive psychology, emotional nuance, managing stress, decision making, and interpersonal relationships.",
                    "tips": "Transcribe a 2-minute snippet from each episode to train your ear on precise subjunctive and conditional clauses."
                },
                {
                    "name": "Émotions (Louie Media)",
                    "badge": "Audio Documentary",
                    "url": "louiemedia.com/emotions",
                    "what": "An audio documentary series investigating why we feel what we feel: anger, nostalgia, impostor syndrome, empathy.",
                    "features": "Blends personal testimonies, expert neuroscientist commentary, and literary quotes with cinematic soundscapes.",
                    "focus": "Sophisticated descriptive adjectives, psychological vocabulary, and nuanced arguments.",
                    "tips": "Pay close attention to how speakers transition between personal anecdotes and generalized theoretical conclusions."
                }
            ]
        },
        61: {
            "page": 61, "type": "resources",
            "title": "3. Top YouTube Channels (Visual + Audio)",
            "subtitle": "Unscripted Street Interviews, Subcultural Slang & Native Cadence",
            "badge_num": "60",
            "intro": "Watch real French people express unscripted opinions with authentic colloquial speed.",
            "resources": [
                {
                    "name": "Easy French – Intermediate & Advanced Series",
                    "badge": "Unscripted Street Speech",
                    "url": "youtube.com/@EasyFrench",
                    "what": "Real Parisian and regional street interviews discussing hot topics: cost of living, vacation culture, dating, politics.",
                    "features": "Dual subtitles (French/English) with color coding. Captures genuine spoken contractions (*chuis, t'sais, j'crois pas*).",
                    "focus": "Spontaneous colloquial reactions, hesitation markers (*euh, bah, du coup*), and everyday body language.",
                    "tips": "Read only the French subtitles; challenge yourself to shadow the speakers at their exact cadence."
                },
                {
                    "name": "innerFrench YouTube Channel",
                    "badge": "Video Essays",
                    "url": "youtube.com/@innerFrench",
                    "what": "Engaging visual essays analyzing French society, cinema classics, historical controversies, and cultural clichés.",
                    "features": "High-production video editing, visual illustrations of key points, and clear French closed captions.",
                    "focus": "French history, why French people love arguing, the myth of Paris syndrome, and French cinema recommendations.",
                    "tips": "Leave a structured 3-paragraph comment in French summarizing your opinion on the video's core question."
                }
            ]
        },
        62: {
            "page": 62, "type": "resources",
            "title": "Pedagogical YouTube Channels",
            "subtitle": "Mastering Pronunciation Pitfalls, Register Shifts & Complex Grammar",
            "badge_num": "61",
            "intro": "Refine your linguistic accuracy with expert Francophone teachers specializing in intermediate plateaus.",
            "resources": [
                {
                    "name": "French School TV (Vincent)",
                    "badge": "Syntax & Exam Technique",
                    "url": "youtube.com/@FrenchSchoolTV",
                    "what": "Systematic, classroom-quality lessons covering B1 grammar hurdles: *subjonctif*, *pronom en & y*, and logical connectors.",
                    "features": "Interactive digital whiteboard, clear color-coded tables, and dedicated DELF B1 preparation series.",
                    "focus": "Mastering the tricky rules that separate high-scoring DELF B1 candidates from those who fail.",
                    "tips": "Complete Vincent's 'DELF B1 Production Écrite' series to learn the 5 golden essay structures."
                },
                {
                    "name": "Maprofdefrançais (Geneviève)",
                    "badge": "Pronunciation & Phonetics",
                    "url": "youtube.com/@maprofdefrancais",
                    "what": "Certified teacher exploring the subtle phonetic differences between French accents, spoken contractions, and liaisons.",
                    "features": "Clear mouth close-ups, phonetic charts, and comparisons between European French and Quebec French.",
                    "focus": "Forbidden vs mandatory liaisons, rhythmic accent groups, and sound-alikes (*c'est / s'est / sais*).",
                    "tips": "Record yourself repeating Geneviève's phonetic minimal pairs to eradicate persistent accent interference."
                }
            ]
        },
        63: {
            "page": 63, "type": "resources",
            "title": "Documentaries, Culture & Comedy",
            "subtitle": "Short-Form Cultural Insights, Humorous Contrasts & Satire",
            "badge_num": "62",
            "intro": "Explore Francophone humor and cultural quirks through top television and digital productions.",
            "resources": [
                {
                    "name": "ARTE Karambolage",
                    "badge": "Cultural Decoding",
                    "url": "youtube.com/@karambolage / arte.tv",
                    "what": "Witty 5-to-10 minute animated essays decoding the subtle cultural differences between France, Germany, and the world.",
                    "features": "Superb voiceover acting, clever animation, and crystal-clear articulation analyzing everyday objects and traditions.",
                    "focus": "Why the French use 'vous', the history of the Carte Vitale, May 1st lily-of-the-valley, French table manners.",
                    "tips": "Watch the 'L'objet' and 'La coutume' segments; write down the cultural lesson in your French study journal."
                },
                {
                    "name": "ARTE Regards & Reportages Courts",
                    "badge": "European Documentaries",
                    "url": "arte.tv/fr",
                    "what": "High-caliber 30-minute documentary reports exploring human stories, ecological challenges, and social realities.",
                    "features": "Professional documentary narration with real interviews from diverse regions and backgrounds.",
                    "focus": "Contemporary European issues, sustainable agriculture, artisan craftsmanship, and alpine preservation.",
                    "tips": "Use the ARTE website with French subtitles enabled to bridge gaps in regional interview dialogue."
                }
            ]
        },
        64: {
            "page": 64, "type": "resources",
            "title": "4. Dedicated Apps, Reference Tools & Lexicons",
            "subtitle": "Digital Workstations for Vocabulary Retention & Contextual Reading",
            "badge_num": "63",
            "intro": "Expand your vocabulary from 1,500 to over 3,500 active headwords with smart digital tools.",
            "resources": [
                {
                    "name": "LingQ & Beelinguapp (B1 Dual Readers)",
                    "badge": "Text & Audio Sync",
                    "url": "lingq.com / beelinguapp.com",
                    "what": "Interactive reading platforms featuring unabridged French short stories and news paired with synchronized native audio.",
                    "features": "Click any word for instantaneous definition; words are automatically added to your spaced repetition review queue.",
                    "focus": "Eliminating dictionary friction, building reading speed, and absorbing natural preposition collocations.",
                    "tips": "Read 2 intermediate articles daily on LingQ while listening to the native voiceover."
                },
                {
                    "name": "Antidote (Druide Informatique)",
                    "badge": "Writing Reference",
                    "url": "antidote.info (Desktop / Web)",
                    "what": "The undisputed gold standard reference tool and grammatical corrector used by French editors and universities.",
                    "features": "Deep synonym dictionary, semantic field maps, co-occurrences, complete conjugation tables, and style guides.",
                    "focus": "Identifying repetitive vocabulary, finding more precise verbs, and correcting agreement errors.",
                    "tips": "Paste your practice DELF essays into Antidote to analyze your lexical diversity score and sentence structure."
                }
            ]
        },
        65: {
            "page": 65, "type": "resources",
            "title": "5. Standard Coursebooks & Graded Fiction",
            "subtitle": "Authoritative Textbooks & Contemporary Novels with Audio",
            "badge_num": "64",
            "intro": "Anchor your grammar and reading stamina with globally acclaimed FLE coursebooks and original French fiction.",
            "resources": [
                {
                    "name": "CLE International – Grammaire Progressive du Français (Niveau Intermédiaire)",
                    "badge": "The FLE Holy Grail",
                    "url": "cle-international.com / Bookstores worldwide",
                    "what": "The essential grammar manual across language schools worldwide: 600 exercises, clear color charts, and audio CD.",
                    "features": "Systematic progression covering all B1 grammar: subjunctive, passive voice, conditionnel passé, indirect speech.",
                    "focus": "Grammatical precision, communicative contexts, and rigorous self-correction exercises with answer keys.",
                    "tips": "Complete 3 chapters weekly. Never skip the auditory comprehension exercises on the accompanying CD."
                },
                {
                    "name": "Collection Mondes en VF (Didier FLE)",
                    "badge": "Original Literature",
                    "url": "didierfle.com",
                    "what": "Original contemporary fiction written by celebrated Francophone authors specifically for B1 language learners.",
                    "features": "Complete unadapted stories written in accessible French; includes free downloadable MP3 audio recording of the entire book.",
                    "focus": "Literary flow, emotional resonance, authentic dialogues, and cultural immersion.",
                    "tips": "Read while listening to the audio to internalize the natural rhythm and intonation of French prose."
                }
            ]
        },
        66: {
            "page": 66, "type": "resources",
            "title": "6. Official DELF B1 Exam Prep & Past Papers",
            "subtitle": "Simulating the 4 Examination Pillars with Official Rubrics",
            "badge_num": "65",
            "intro": "Prepare methodically for the official French Ministry of Education B1 examination.",
            "resources": [
                {
                    "name": "France Éducation International – Épreuves DELF B1",
                    "badge": "Official Benchmark",
                    "url": "france-education-international.fr",
                    "what": "Official government website offering authentic past exam sessions, candidate booklets, and audio recordings.",
                    "features": "Downloadable MP3 audio files for the 25-minute listening exam, sample candidate essays with examiner scores.",
                    "focus": "The 4 exam components: Compréhension de l'oral (25m), des écrits (35m), Production écrite (45m), orale (15m).",
                    "tips": "Take a full timed mock exam under strict exam conditions 3 weeks before your official test date."
                },
                {
                    "name": "Didier – Le DELF B1 100% Réussite",
                    "badge": "Complete Prep Guide",
                    "url": "didierfle.com",
                    "what": "Comprehensive preparation guide with step-by-step strategy workshops and 4 complete practice exams.",
                    "features": "Audio CD with authentic radio clips, candidate evaluation grids, and model essays with examiner commentary.",
                    "focus": "Mastering the formal letter format, presenting an opinion debate, and extracting specific details from radio broadcasts.",
                    "tips": "Memorize the 10 transitional connectors (*néanmoins, toutefois, en effet, quant à*) to score high on written cohesion."
                }
            ]
        },
        67: {
            "page": 67, "type": "checklist",
            "title": "B1 Listening & Immersion Mastery Checklist",
            "subtitle": "Audit Your Auditory Comprehension and Resource Completion",
            "badge_num": "66",
            "intro": "Before advancing to the final Module 8 Readiness Assessment, verify that you can perform these intermediate listening tasks in real-world Francophone settings.",
            "sections": [
                {
                    "title": "B1 Auditory Can-Do Benchmarks",
                    "items": [
                        "I can understand the main points of clear standard speech on familiar matters regularly encountered at work, school, and leisure.",
                        "I can follow radio documentaries and podcasts (innerFrench, RFI) when spoken at a measured native tempo.",
                        "I can identify emotional nuances, disagreement, and hesitation in conversational French.",
                        "I can follow the plot of French films and TV series when supported by French closed captions.",
                        "I can extract specific technical details from announcements, instructions, and telephone messages.",
                        "I understand how opinions are introduced and supported in debates (*à mon sens, j'estime que, de mon côté*).",
                        "I can understand spoken explanations of travel issues, healthcare instructions, and administrative procedures.",
                        "I have established a daily 30-minute habit of listening to authentic French media."
                    ]
                }
            ]
        }
    }

def get_b2_resources():
    return {
        53: {
            "page": 53, "type": "checklist",
            "title": "B2 French – Advanced Immersion & Audio Guide",
            "subtitle": "Level: B2 (Upper-Intermediate / Vantage) • Full Independence Framework",
            "badge_num": "52",
            "intro": "The B2 level represents the stage of genuine communicative independence: understanding rapid, complex debate, implicit subtext, irony, and cultural nuance across all Francophone media.",
            "sections": [
                {
                    "title": "Core B2 Listening & Study Methodology",
                    "items": [
                        "Ditch Learner Content: Transition 100% to media made by native French speakers for native French speakers.",
                        "Speed & Argument Tracking: Train your ear on fast-paced radio debate shows where multiple speakers talk simultaneously.",
                        "The Argument Analysis Habit: Don't just follow the story; identify the thesis, concessions, counter-arguments, and rhetorical tone."
                    ]
                },
                {
                    "title": "Weekly Resource Allocation Framework",
                    "items": [
                        "Monday & Wednesday: Public radio podcasts (France Inter Affaires Sensibles / France Culture Les Pieds sur terre).",
                        "Tuesday & Thursday: Investigative video journalism and geopolitics (HugoDécrypte / ARTE Le Dessous des Cartes).",
                        "Friday: Unfiltered social debate and cultural podcasts (Binge Audio Kiffe ta race / Programme B).",
                        "Weekend: Read authentic French literary fiction (Folio) + complete one DELF B2 timed oral/written synthesis task."
                    ]
                }
            ]
        },
        54: {
            "page": 54, "type": "resources",
            "title": "1. Structured Listening Platforms (CEFR-Aligned)",
            "subtitle": "Specialized News Dossiers, International Geopolitics & Social Debates",
            "badge_num": "53",
            "intro": "Advanced platforms providing pedagogical structures around complex authentic French broadcasts.",
            "resources": [
                {
                    "name": "TV5Monde – 7 Jours sur la Planète (B2)",
                    "badge": "Top Broadcast Analysis",
                    "url": "apprendre.tv5monde.com",
                    "what": "Weekly world news analysis show featuring authentic reports from France 2, RTBF (Belgium), and Radio-Canada.",
                    "features": "Downloadable pedagogical dossiers, specialized terminology sheets, and advanced synthesis questions.",
                    "focus": "Complex sociological, environmental, and diplomatic issues analyzed with high-register vocabulary.",
                    "tips": "Practice writing a 150-word synthesis of the weekly lead story within a strict 20-minute window."
                },
                {
                    "name": "RFI Savoirs – Grands Dossiers & Débats",
                    "badge": "Advanced Audio",
                    "url": "savoirs.rfi.fr",
                    "what": "In-depth radio documentaries exploring world history, international trade, philosophy, and human rights.",
                    "features": "Full broadcast audio tracks, complete verbatim transcripts, and interactive comprehension quizzes.",
                    "focus": "Nuanced arguments, specialized economic and diplomatic terminology, and debate protocols.",
                    "tips": "Identify and catalog the rhetorical concession structures (*certes... mais, bien que... il n'en demeure pas moins*)."
                }
            ]
        },
        55: {
            "page": 55, "type": "resources",
            "title": "Interactive Public Radio & News Workstations",
            "subtitle": "Immersing in France's Elite Radio Networks & Unscripted Panels",
            "badge_num": "54",
            "intro": "Access thousands of hours of live and archived high-register native radio on demand.",
            "resources": [
                {
                    "name": "Radio France App (France Inter, France Culture, France Info)",
                    "badge": "The Immersion Hub",
                    "url": "radiofrance.fr / Mobile App",
                    "what": "The centralized portal for France's premier national public radio stations, covering news, culture, and science.",
                    "features": "High-quality audio streams, customizable playlist queues, offline downloading, and thematic categorization.",
                    "focus": "Rapid conversational pace, cultural references, sophisticated banter, and articulate debate.",
                    "tips": "Replace your morning commute music with France Inter's 'Le 7/9' morning news program."
                },
                {
                    "name": "TV5Monde – Émissions Complètes (Kiosque & Mag)",
                    "badge": "Press Debates",
                    "url": "tv5monde.com/emissions",
                    "what": "Weekly roundtables where international Francophone journalists debate controversial world affairs.",
                    "features": "Multiple native accents (French, Swiss, Belgian, Senegalese, Canadian) clashing over hot topics.",
                    "focus": "Interruptive speech, fast-paced rebuttal formulas, diplomatic expressions, and analytical rhetoric.",
                    "tips": "Take side notes on which arguments you agree with and prepare an oral 3-minute counter-argument."
                }
            ]
        },
        56: {
            "page": 56, "type": "resources",
            "title": "Authentic Press & Investigative Journalism",
            "subtitle": "Decoding Elite French Print Media & Narrative Journalism",
            "badge_num": "55",
            "intro": "Develop deep reading fluency across France's most respected newspapers and investigative outlets.",
            "resources": [
                {
                    "name": "Le Monde & Courrier International (Audio Articles)",
                    "badge": "Elite Journalism",
                    "url": "lemonde.fr / courrierinternational.com",
                    "what": "France's leading newspaper of record offering professional audio recordings of major investigative articles.",
                    "features": "Articles narrated by professional voice actors, rich literary register, and impeccable syntactic precision.",
                    "focus": "In-depth investigative reports, geopolitical analyses, cultural critiques, and economic forecasts.",
                    "tips": "Read along with the audio article to observe how complex periodic sentences are rhythmically grouped."
                },
                {
                    "name": "Mediapart – Les Grands Entretiens",
                    "badge": "Investigative Video",
                    "url": "mediapart.fr / YouTube",
                    "what": "Independent investigative journalism platform featuring longform 1-to-2 hour interviews with public figures.",
                    "features": "In-depth questioning by seasoned investigative journalists holding officials accountable without fluff.",
                    "focus": "Legal, political, and socio-economic terminology, rigorous fact-checking, and sharp cross-examination.",
                    "tips": "Focus on the journalist's interrogation techniques: note down polite yet firm probing questions."
                }
            ]
        },
        57: {
            "page": 57, "type": "resources",
            "title": "2. Top Native Podcasts: Current Affairs & Storytelling",
            "subtitle": "France's Most Acclaimed Audio Documentaries & Narrative Journalism",
            "badge_num": "56",
            "intro": "Engage with the top-ranked narrative podcasts listened to by millions of French citizens daily.",
            "resources": [
                {
                    "name": "Affaires Sensibles (Fabrice Drouelle - France Inter)",
                    "badge": "France's #1 Podcast",
                    "url": "radiofrance.fr/franceinter/podcasts/affaires-sensibles",
                    "what": "Gripping 50-minute narrative audio documentaries recounting major historical trials, scandals, and events of the past 50 years.",
                    "features": "Drouelle's dramatic, mesmerizing storytelling style accompanied by archival radio clips and actor recreations.",
                    "focus": "Rich descriptive adjectives, dramatic narrative tenses, legal terminology, and modern French history.",
                    "tips": "Listen in a quiet room with headphones. The sound design and tension will completely immerse you."
                },
                {
                    "name": "Géopolitique (Pierre Haski - France Inter)",
                    "badge": "Concise Diplomacy",
                    "url": "radiofrance.fr/franceinter/podcasts/geopolitique",
                    "what": "A sharp, incisive 4-minute daily analysis dissecting the most critical international conflict or diplomatic event.",
                    "features": "Pristine, eloquent syntax delivered by one of France's most experienced foreign correspondents.",
                    "focus": "International treaties, strategic alliances, balance of power, and global economic implications.",
                    "tips": "Write a 3-bullet-point summary of Haski's daily thesis every morning as a micro-routine."
                }
            ]
        },
        58: {
            "page": 58, "type": "resources",
            "title": "Top Native Podcasts: Society & Human Stories",
            "subtitle": "Unfiltered Voices, Intimate Realities & Sociological Insights",
            "badge_num": "57",
            "intro": "Listen to the raw, unscripted voices of contemporary Francophone society.",
            "resources": [
                {
                    "name": "Les Pieds sur terre (France Culture)",
                    "badge": "Unscripted Human Audio",
                    "url": "radiofrance.fr/franceculture/podcasts/les-pieds-sur-terre",
                    "what": "Half-hour documentary episodes composed entirely of authentic, unedited testimonies from ordinary citizens.",
                    "features": "No voiceover commentary, no didactic narration; just real French people sharing raw lived experiences.",
                    "focus": "Authentic regional accents, working-class idiom, emotional cadence, and sociological reality.",
                    "tips": "Excellent training for understanding spontaneous French without standard radio polish."
                },
                {
                    "name": "Transfert (Louie Media / Slate)",
                    "badge": "Psychological Journeys",
                    "url": "louiemedia.com/transfert",
                    "what": "Intimate confessions where individuals recount life-altering moral dilemmas, betrayals, and discoveries.",
                    "features": "Exquisite audio production, natural conversational pacing, complex emotional vocabulary.",
                    "focus": "Nuanced human psychology, moral introspection, storytelling techniques, and conversational flow.",
                    "tips": "Pay attention to how storytellers express doubt, regret (*j'aurais dû, si seulement*), and realization."
                }
            ]
        },
        59: {
            "page": 59, "type": "resources",
            "title": "Top Native Podcasts: Culture & Contemporary Debate",
            "subtitle": "Exploring Identity, Subcultures & Progressive Thought",
            "badge_num": "58",
            "intro": "Broaden your cultural lexicon with progressive audio discussions on modern French society.",
            "resources": [
                {
                    "name": "Kiffe ta race (Binge Audio - Rokhaya Diallo & Grace Ly)",
                    "badge": "Societal Questions",
                    "url": "binge.audio/podcast/kiffetarace",
                    "what": "A candid, lively bi-weekly discussion dissecting questions of race, identity, and representation in France.",
                    "features": "Dynamic dialogue with expert guests, authors, and sociologists, blending academic concepts with slang.",
                    "focus": "Sociological terms, contemporary debate terminology, conversational interruptions, and modern cultural references.",
                    "tips": "Take note of modern colloquial expressions and inclusive language formulations used in Parisian cultural circles."
                },
                {
                    "name": "Programme B (Binge Audio - Thomas Rozec)",
                    "badge": "Narrative Journalism",
                    "url": "binge.audio/podcast/programme-b",
                    "what": "Daily 20-minute investigative podcast exploring unexpected cultural phenomena, political controversies, and tech trends.",
                    "features": "Fast-paced documentary narrative combining on-the-ground reporting with cultural commentary.",
                    "focus": "Tech culture, media ecosystems, political satire, and contemporary subcultures.",
                    "tips": "Great for learning current media buzzwords and colloquial abbreviations (*la tech, les fake news, le buzz*)."
                }
            ]
        },
        60: {
            "page": 60, "type": "resources",
            "title": "Top Native Podcasts: Science, History & Philosophy",
            "subtitle": "Intellectual Stimulation with Engaging Storytelling Formats",
            "badge_num": "59",
            "intro": "Dive into fascinating historical and scientific deep-dives designed for curious French adults.",
            "resources": [
                {
                    "name": "Culture 2000 (Fréquence Moderne)",
                    "badge": "Fun History",
                    "url": "culture2000.lepodcast.fr / Spotify",
                    "what": "An energetic, humorous panel of history buffs and educators revisiting major world events and historical figures.",
                    "features": "1-hour episodes structured with chronological chapters, banter, musical breaks, and cultural context.",
                    "focus": "Historical vocabulary (revolutions, empires, treaties), lively group debate, and cultural jokes.",
                    "tips": "Listen to episodes covering French history (The French Revolution, May 68, Napoleon) for high cultural ROI."
                },
                {
                    "name": "La Terre au Carré (Mathieu Vidard - France Inter)",
                    "badge": "Science & Ecology",
                    "url": "radiofrance.fr/franceinter/podcasts/la-terre-au-carre",
                    "what": "Daily 1-hour program dedicated to the environment, planetary science, biodiversity, and scientific discoveries.",
                    "features": "Interviews with leading climatologists, biologists, and environmental advocates discussing solutions.",
                    "focus": "Scientific terminology, environmental policy, ecological vocabulary, and statistical analysis.",
                    "tips": "Essential vocabulary preparation for the DELF B2 written and oral production components."
                }
            ]
        },
        61: {
            "page": 61, "type": "resources",
            "title": "3. Top YouTube Channels for B2 Immersion",
            "subtitle": "Rapid-Fire News, Pop-Culture Decoding & Visual Analysis",
            "badge_num": "60",
            "intro": "Engage with France's leading digital creators who shape modern Francophone online discourse.",
            "resources": [
                {
                    "name": "HugoDécrypte – Les Actus du Jour",
                    "badge": "Daily News Must-Watch",
                    "url": "youtube.com/@HugoDecrypte",
                    "what": "Daily 10-minute news summary presented by Hugo Travers, the leading independent news channel for French youth.",
                    "features": "Clear, rapid-fire modern French enunciation, dynamic graphics, and objective synthesis of global events.",
                    "focus": "Politics, tech, global conflicts, and environmental laws explained with pristine lexical clarity.",
                    "tips": "Watch daily at 1.0x speed. Hugo's cadence is the perfect benchmark for B2 auditory processing speed."
                },
                {
                    "name": "Karambolage (ARTE)",
                    "badge": "Cultural Mastery",
                    "url": "youtube.com/@karambolage",
                    "what": "Witty, animated short films exploring the hidden linguistic origins and cultural rituals of France.",
                    "features": "Superb writing, linguistic etymology, humorous visual animations, and elegant voiceover delivery.",
                    "focus": "Idiomatic expressions, historical traditions (*la galette des rois*), and social etiquette.",
                    "tips": "The 'L'étymologie' segment is fantastic for understanding how French words evolved from Latin and Old French."
                }
            ]
        },
        62: {
            "page": 62, "type": "resources",
            "title": "Specialized YouTube: History, Science & Essays",
            "subtitle": "High-Production Video Documentaries & Intellectual Explorations",
            "badge_num": "61",
            "intro": "Explore specialized academic fields presented with passion, rigor, and cinematic visual editing.",
            "resources": [
                {
                    "name": "Nota Bene (Benjamin Brillaud)",
                    "badge": "Epic History",
                    "url": "youtube.com/@notabenem" ,
                    "what": "France's largest history channel; high-production documentaries examining historical myths, battles, and kings.",
                    "features": "Clear articulation, engaging narrative pacing, interviews with museum curators, and on-location filming.",
                    "focus": "Military history, medieval society, ancient civilizations, and archaeological breakthroughs.",
                    "tips": "Turn on French subtitles for specialized historical terminology (*les croisades, les armoiries, le clergé*)."
                },
                {
                    "name": "Scilabus (Viviane Lalande)",
                    "badge": "Curious Science",
                    "url": "youtube.com/@scilabus",
                    "what": "Physics and biology questions explored through scientific rigor, hands-on experiments, and curiosity.",
                    "features": "Articulate explanations by a PhD engineer, clear diagrams, and relatable everyday questions.",
                    "focus": "Hypothesis formulation, experimental reasoning (*or, ainsi, par conséquent*), and scientific nouns.",
                    "tips": "Pay close attention to how Viviane structures a scientific hypothesis and presents empirical proof."
                }
            ]
        },
        63: {
            "page": 63, "type": "resources",
            "title": "Geopolitics, Documentaries & ARTE Cinema",
            "subtitle": "World-Class Mapping Analysis & Feature-Length Investigative Films",
            "badge_num": "62",
            "intro": "Master geopolitical discourse and documentary storytelling through public television archives.",
            "resources": [
                {
                    "name": "Le Dessous des Cartes (ARTE)",
                    "badge": "Geopolitical Gold Standard",
                    "url": "youtube.com/@LeDessousdesCartesARTE / arte.tv",
                    "what": "Legendary weekly geopolitical show using dynamic maps to analyze global power shifts, borders, and resources.",
                    "features": "Hosted by Émilie Aubry; features impeccable, formal French prose with advanced diplomatic terminology.",
                    "focus": "Maritime trade routes, energy transitions, border disputes, demographic trends, and international law.",
                    "tips": "Essential viewing for mastering the vocabulary needed for the DELF B2 formal essay component."
                },
                {
                    "name": "ARTE Documentaires",
                    "badge": "Feature Documentaries",
                    "url": "arte.tv/fr / YouTube",
                    "what": "Full-length 52-to-90 minute investigative documentaries covering history, fine arts, society, and nature.",
                    "features": "Award-winning filmmaking, voiceovers by France's top documentary narrators, and global topics.",
                    "focus": "Literary narration, sophisticated transitions, multi-source interviews, and specialized terminology.",
                    "tips": "Watch one full-length documentary every weekend to build long-form auditory concentration stamina."
                }
            ]
        },
        64: {
            "page": 64, "type": "resources",
            "title": "4. Dedicated Dictionaries, Stylistic Tools & Anki",
            "subtitle": "Authoritative Reference Software for Sophisticated Written & Spoken Precision",
            "badge_num": "63",
            "intro": "Equip yourself with the professional digital tools used by Francophone journalists and academics.",
            "resources": [
                {
                    "name": "Dictionnaire Le Robert & Larousse en Ligne",
                    "badge": "Lexical Authority",
                    "url": "lerobert.com / larousse.fr",
                    "what": "The definitive contemporary dictionaries of the French language with comprehensive definitions and examples.",
                    "features": "Includes nuance distinctions between synonyms, register labels (*soutenu, familier*), and etymology notes.",
                    "focus": "Finding precise verbs to replace weak generic verbs (*faire, dire, mettre, avoir*), prepositional regimes.",
                    "tips": "Look up words in the Robert monolingual dictionary; read the French definition rather than translating."
                },
                {
                    "name": "Antidote 11 (Druide Informatique)",
                    "badge": "Grammar & Style Suite",
                    "url": "antidote.info",
                    "what": "The world's most advanced software suite for writing and mastering French, used across Francophone newsrooms.",
                    "features": "Deep semantic maps, synonym engine, syntax analyzer that flags weak phrasing, pleonasms, and passive verbs.",
                    "focus": "Elevating your writing style, eliminating repeated words, and mastering complex agreement nuances.",
                    "tips": "Run every DELF practice essay through Antidote's 'Style' filter to identify and eradicate stylistic clumsy phrasing."
                }
            ]
        },
        65: {
            "page": 65, "type": "resources",
            "title": "5. Standard Coursebooks & Contemporary Literature",
            "subtitle": "Advanced Pedagogical Grammars & Unabridged French Novels",
            "badge_num": "64",
            "intro": "Consolidate advanced syntax and begin reading original, unadapted Francophone literature.",
            "resources": [
                {
                    "name": "CLE International – Grammaire Progressive du Français (Niveau Avancé)",
                    "badge": "Advanced Syntax Bible",
                    "url": "cle-international.com / Major Bookstores",
                    "what": "400 comprehensive exercises tackling the subtle syntax points that challenge even advanced learners.",
                    "features": "Subjunctive imperfect, inversion of subject, complex relative pronouns, passive nuances, and discourse connectors.",
                    "focus": "Rigorous grammatical mastery, nuances of register (*langue soutenue*), and stylistic variation.",
                    "tips": "Focus heavily on the chapters on 'L'Expression de la Cause, de la Conséquence et de l'Opposition'."
                },
                {
                    "name": "Unabridged Contemporary Literature (Collection Folio / Livre de Poche)",
                    "badge": "Authentic Reading",
                    "url": "gallimard.fr/Catalogue/FOLIO",
                    "what": "Jump into real, unadapted French novels with accessible prose styles and gripping contemporary plots.",
                    "features": "Recommended authors: Annie Ernaux (*La Place*), Albert Camus (*L'Étranger*), Amélie Nothomb (*Stupeur et Tremblements*).",
                    "focus": "Past literary tenses (*passé simple* recognition), emotional introspection, dialogue formatting, and literary cadence.",
                    "tips": "Read 10 pages daily without pausing for every unknown word. Underline only words repeated multiple times."
                }
            ]
        },
        66: {
            "page": 66, "type": "resources",
            "title": "6. Official DELF B2 Exam Prep & Synthesis Tasks",
            "subtitle": "Mastering the 30-Minute Listening Exam & Oral Argumentation",
            "badge_num": "65",
            "intro": "Systematic preparation for the official French Ministry of Education B2 diploma.",
            "resources": [
                {
                    "name": "France Éducation International – Épreuves DELF B2",
                    "badge": "Official Benchmark",
                    "url": "france-education-international.fr",
                    "what": "Official past examination sessions featuring the 30-minute listening test and actual scoring rubrics.",
                    "features": "Long audio documents (radio broadcasts, conferences) with multiple-choice and open-ended synthesis questions.",
                    "focus": "The 4 examination pillars: Compréhension orale (30m), écrite (1h), Production écrite (1h), orale (20m + 30m prep).",
                    "tips": "Practice note-taking during the 2 listening passes using abbreviations and arrows to capture key figures."
                },
                {
                    "name": "Didier – Le DELF B2 100% Réussite",
                    "badge": "Top Prep Manual",
                    "url": "didierfle.com",
                    "what": "The definitive preparation manual containing strategy workshops, 4 full mock exams, and audio CD.",
                    "features": "Step-by-step guides on structuring a persuasive letter to an authority (*lettre formelle au maire ou directeur*).",
                    "focus": "Structuring the 20-minute oral defense: introduction, problem statement (*problématique*), 2-part development, conclusion.",
                    "tips": "Record yourself giving a 10-minute presentation on a controversial topic; review and critique your pacing."
                }
            ]
        },
        67: {
            "page": 67, "type": "checklist",
            "title": "B2 Listening & Immersion Mastery Checklist",
            "subtitle": "Audit Your Auditory Independence and Resource Completion",
            "badge_num": "66",
            "intro": "Before advancing to the final Module 8 Readiness Assessment, confirm that you have achieved complete auditory independence across Francophone media.",
            "sections": [
                {
                    "title": "B2 Auditory Can-Do Benchmarks",
                    "items": [
                        "I can understand extended speech and lectures and follow complex lines of argument provided the topic is reasonably familiar.",
                        "I can understand most TV news and current affairs programs (France Inter, HugoDécrypte) without subtitles.",
                        "I can understand the majority of French films in standard dialect and recognize colloquial idioms and slang.",
                        "I can identify irony, sarcasm, humor, and subtle speaker viewpoints in unscripted debates.",
                        "I can follow fast-paced discussions between native speakers who interrupt one another without losing the thread.",
                        "I can extract key statistical data, dates, and cause-and-effect relationships from specialized reports.",
                        "I can understand complex instructions regarding technical, administrative, or legal procedures.",
                        "I have eliminated all reliance on English translations and consume authentic French media daily as a natural habit."
                    ]
                }
            ]
        }
    }

def get_c1_resources():
    return {
        53: {
            "page": 53, "type": "checklist",
            "title": "C1 French – Academic Research & Immersion Guide",
            "subtitle": "Level: C1 (Advanced / Effective Operational Proficiency) • Intellectual Autonomy",
            "badge_num": "52",
            "intro": "The C1 level represents full intellectual autonomy: effortlessly understanding complex academic lectures, literary essays, specialized radio debates, and abstract philosophical dialectics.",
            "sections": [
                {
                    "title": "Core C1 Listening & Study Methodology",
                    "items": [
                        "Master the French Academic Register: Internalize the rhythm, syntactic structures, and rhetorical markers of Francophone intellectuals.",
                        "Rapid-Fire Colloquial + High Literary Register: Move seamlessly between rapid Parisian street vernacular and formal 19th-century prose.",
                        "Synthesis & Critical Deconstruction: Train your mind to identify implicit assumptions, rhetorical fallacies, and underlying philosophical paradigms."
                    ]
                },
                {
                    "title": "Weekly Resource Allocation Framework",
                    "items": [
                        "Monday & Wednesday: Deep philosophical and historical lectures (France Culture Concordance des temps / Le Cours de l'histoire).",
                        "Tuesday & Thursday: Unfiltered investigative interviews and geopolitical analysis (Thinkerview / Le Monde diplomatique).",
                        "Friday: Literary criticism, performing arts, and cinema panels (Le Masque et la Plume / La Compagnie des auteurs).",
                        "Weekend: Work on a timed DALF C1 'Synthèse de documents' (220 words from 3 complex texts) + reading Pléiade literature."
                    ]
                }
            ]
        },
        54: {
            "page": 54, "type": "resources",
            "title": "1. Academic & Intellectual Audio Platforms",
            "subtitle": "Immersing in France's Elite Intellectual Broadcasts & Public Radio",
            "badge_num": "53",
            "intro": "Official institutions and public broadcasters providing peerless longform intellectual discourse.",
            "resources": [
                {
                    "name": "France Culture (Radio France)",
                    "badge": "Intellectual Powerhouse",
                    "url": "radiofrance.fr/franceculture",
                    "what": "France's national cultural public radio station, delivering 24/7 intellectual programming on philosophy, history, and science.",
                    "features": "Pristine acoustic production, roundtables with top university professors, authors, and philosophers.",
                    "focus": "Sophisticated vocabulary, abstract conceptual frameworks, complex periodic syntax, and rhetorical eloquence.",
                    "tips": "Make France Culture your default background audio while working or studying to absorb high-register cadence."
                },
                {
                    "name": "INA – Institut National de l'Audiovisuel",
                    "badge": "Historical Archives",
                    "url": "ina.fr / YouTube",
                    "what": "France's national audiovisual repository preserving over 80 years of television and radio debates and interviews.",
                    "features": "Historic broadcasts featuring iconic thinkers: Jean-Paul Sartre, Simone de Beauvoir, Michel Foucault, Roland Barthes.",
                    "focus": "Classical French rhetorical wit (*l'esprit français*), historical register shifts, and post-war intellectual debates.",
                    "tips": "Watch the 'Grands Entretiens' playlist to observe how 20th-century French masters structured spontaneous oral arguments."
                }
            ]
        },
        55: {
            "page": 55, "type": "resources",
            "title": "Investigative Journalism & Societal Analysis",
            "subtitle": "Uncompromising Public Debate, Media Critique & Analytical Panels",
            "badge_num": "54",
            "intro": "Engage with independent Francophone investigative platforms that challenge established dogmas.",
            "resources": [
                {
                    "name": "Mediapart – Émissions et Grands Débats",
                    "badge": "Independent Journalism",
                    "url": "mediapart.fr / YouTube",
                    "what": "Premier independent investigative newspaper featuring longform panel discussions and intellectual confrontations.",
                    "features": "Unedited 2-hour debates between sociologists, union leaders, politicians, and investigative reporters.",
                    "focus": "Legal jurisprudence, state institutions, political corruption, and constitutional philosophy.",
                    "tips": "Notice how guests deploy concessions before launching devastating counter-arguments (*je vous concède que... toutefois*)."
                },
                {
                    "name": "France Inter – Le Téléphone Sonne & Le Grand Face-à-Face",
                    "badge": "Public Debate",
                    "url": "radiofrance.fr/franceinter",
                    "what": "France's top morning and evening debate shows uniting columnists, politicians, and citizen call-ins.",
                    "features": "High-velocity debates with spontaneous interruptions, rhetorical traps, and sharp dialectical clashes.",
                    "focus": "Real-time polemics, conversational velocity, rhetorical wit, and public policy analysis.",
                    "tips": "Train yourself to follow the thread of argument even when three panelists speak simultaneously."
                }
            ]
        },
        56: {
            "page": 56, "type": "resources",
            "title": "Major Print Reviews & Critical Essay Publications",
            "subtitle": "Elite Francophone Periodicals Exploring Geopolitics, Ideas & Arts",
            "badge_num": "55",
            "intro": "Read the world's most rigorous Francophone monthly journals of international affairs and philosophy.",
            "resources": [
                {
                    "name": "Le Monde diplomatique (Audio Edition & Print)",
                    "badge": "The Premier Critical Journal",
                    "url": "monde-diplomatique.fr / Audio Edition",
                    "what": "Renowned monthly journal published in Paris analyzing international politics, economics, culture, and social theory.",
                    "features": "Exhaustive 5,000-word investigative essays, zero sensationalism, impeccable literary French syntax and rich lexicon.",
                    "focus": "Structural geopolitical shifts, post-colonial economics, critical sociology, and philosophical essays.",
                    "tips": "Subscribe to the audio edition to listen to professional voice actors narrating the longform articles."
                },
                {
                    "name": "Philosophie Magazine",
                    "badge": "Applied Philosophy",
                    "url": "philomag.com",
                    "what": "Contemporary monthly review examining breaking global controversies through the thought of classical philosophers.",
                    "features": "Accessible yet rigorous philosophical dialectics applying Kant, Spinoza, and Deleuze to AI, climate, and democracy.",
                    "focus": "Epistemology, moral philosophy, ethical dilemmas, and conceptual precision.",
                    "tips": "Great for acquiring the philosophical vocabulary essential for the DALF C1 and C2 production sections."
                }
            ]
        },
        57: {
            "page": 57, "type": "resources",
            "title": "2. Top C1 Podcasts: History & International Strategy",
            "subtitle": "Deep Historical Precedents, Diplomatic Dossiers & Strategic Analyses",
            "badge_num": "56",
            "intro": "Delve into history's turning points and global geopolitical strategy with top French researchers.",
            "resources": [
                {
                    "name": "Concordance des temps (Jean-Noël Jeanneney - France Culture)",
                    "badge": "Historical Dialectic",
                    "url": "radiofrance.fr/franceculture/podcasts/concordance-des-temps",
                    "what": "A renowned historian invites a fellow researcher each Saturday to illuminate a modern crisis using historical parallels.",
                    "features": "58 minutes of exquisite, scholarly French dialogue interspersed with archival recordings and literary excerpts.",
                    "focus": "Historical nuances, political philosophy, archival analysis, and sophisticated rhetorical sentence structures.",
                    "tips": "Listen with a notebook. The historical terminology and elegant syntax represent the peak of French radio."
                },
                {
                    "name": "Affaires étrangères (Christine Ockrent - France Culture)",
                    "badge": "Diplomatic Dossiers",
                    "url": "radiofrance.fr/franceculture/podcasts/affaires-etrangeres",
                    "what": "Weekly 1-hour strategic analysis of global power dynamics hosted by seasoned international journalist Christine Ockrent.",
                    "features": "Panels uniting foreign ambassadors, military strategists, intelligence specialists, and academic researchers.",
                    "focus": "International law, strategic alliances, energy sovereignty, and diplomatic negotiations.",
                    "tips": "Essential listening for preparing the DALF C1 oral synthesis on geopolitics or international relations."
                }
            ]
        },
        58: {
            "page": 58, "type": "resources",
            "title": "Top C1 Podcasts: Ideas, Philosophy & Society",
            "subtitle": "Exploring Human Nature, Intellectual Movements & Sociology",
            "badge_num": "57",
            "intro": "Expand your conceptual agility with podcasts dissecting the architecture of human thought.",
            "resources": [
                {
                    "name": "Le Cours de l'histoire (Xavier Mauduit - France Culture)",
                    "badge": "Daily History Immersion",
                    "url": "radiofrance.fr/franceculture/podcasts/le-cours-de-l-histoire",
                    "what": "Daily 1-hour documentary series exploring social, cultural, and political history through thematic week-long series.",
                    "features": "Interviews with leading university professors, archival sound design, and vivid narrative recreations.",
                    "focus": "Social history, history of ideas, daily life across centuries, and historiographical methodology.",
                    "tips": "Listen to 4-part series (e.g. 'Histoire du livre', 'Histoire de la diplomatie') to master specialized domain lexicons."
                },
                {
                    "name": "Grand Bien Vous Fasse (Ali Rebeihi - France Inter)",
                    "badge": "Psychology & Culture",
                    "url": "radiofrance.fr/franceinter/podcasts/grand-bien-vous-fasse",
                    "what": "Daily 1-hour exploration of human behavior, personal relationships, philosophy of everyday life, and society.",
                    "features": "Panels of psychiatrists, sociologists, philosophers, and writers answering profound human dilemmas.",
                    "focus": "Emotional nuance, human relationships, cognitive science, and practical ethics.",
                    "tips": "Notice how guests transition smoothly between empirical medical facts and abstract philosophical reflections."
                }
            ]
        },
        59: {
            "page": 59, "type": "resources",
            "title": "Top C1 Podcasts: Literature, Arts & Critique",
            "subtitle": "Uncompromising Literary Analysis, Theatre Debates & Cinema Reviews",
            "badge_num": "58",
            "intro": "Sharpen your aesthetic judgment and literary critique with France's sharpest cultural critics.",
            "resources": [
                {
                    "name": "La Compagnie des auteurs (France Culture)",
                    "badge": "Literary Retrospectives",
                    "url": "radiofrance.fr/franceculture/podcasts/la-compagnie-des-auteurs",
                    "what": "Monographic series dedicating 4 full hour-long episodes to dissecting the life, style, and philosophy of one major writer.",
                    "features": "Covers giants of literature: Proust, Baudelaire, Victor Hugo, Flaubert, Camus, Montaigne, and Duras.",
                    "focus": "Literary analysis, stylistic figures, textual deconstruction, and biographical context.",
                    "tips": "Listen to the series on an author right before reading one of their major novels."
                },
                {
                    "name": "Le Masque et la Plume (Jérôme Garcin - France Inter)",
                    "badge": "France's Oldest Radio Show",
                    "url": "radiofrance.fr/franceinter/podcasts/le-masque-et-la-plume",
                    "what": "Broadcast continuously since 1955: four prominent critics debate newly released films, books, and plays without filter.",
                    "features": "Witty, scathing, enthusiastic, and merciless intellectual debate filled with humor and literary erudition.",
                    "focus": "Aesthetic vocabulary, rhetorical argumentation, devastating punchlines, and passionate cultural defense.",
                    "tips": "A masterclass in how to praise or demolish a work of art with rhetorical elegance and flair."
                }
            ]
        },
        60: {
            "page": 60, "type": "resources",
            "title": "Top C1 Podcasts: Economics & Critical Thought",
            "subtitle": "Challenging Economic Models, Public Philosophy & Sociology",
            "badge_num": "59",
            "intro": "Engage with cutting-edge academic critique and longform intellectual interviews.",
            "resources": [
                {
                    "name": "Le Nouvel Esprit public (Philippe Meyer)",
                    "badge": "Independent Roundtable",
                    "url": "lenouvelespritpublic.fr / Spotify",
                    "what": "Independent weekly debate series continuing the legacy of France Culture's classic 'L'Esprit public'.",
                    "features": "Uniting top political scientists, historians, and economists (e.g. Jean-Louis Bourlanges, Nicole Gnesotto).",
                    "focus": "Deep constitutional analysis, European integration, democratic resilience, and fiscal policy.",
                    "tips": "Observe the exquisite courtesy with which veteran French intellectuals dissect each other's theses."
                },
                {
                    "name": "Hors-Série (hors-serie.net)",
                    "badge": "Longform Interviews",
                    "url": "hors-serie.net",
                    "what": "Subscriber-funded longform interview website featuring 2-hour uninterrupted dialogues with contemporary thinkers.",
                    "features": "Hosted by Judith Bernard and Laura Raim; deep dives into newly published sociological and philosophical books.",
                    "focus": "Sociological theory, radical philosophy, post-capitalism, and epistemological critique.",
                    "tips": "Take comprehensive notes during the interview to simulate academic lecture comprehension."
                }
            ]
        },
        61: {
            "page": 61, "type": "resources",
            "title": "3. Top YouTube Channels for Advanced Discourse",
            "subtitle": "Unedited Longform Interviews, Media Critique & Satirical Video Essays",
            "badge_num": "60",
            "intro": "Watch uninterrupted longform French debates and sharp socio-political video essays.",
            "resources": [
                {
                    "name": "Thinkerview",
                    "badge": "Uncensored Longform",
                    "url": "youtube.com/@Thinkerview",
                    "what": "Unedited, zero-cut 2-to-3 hour longform interviews with intelligence directors, economists, hackers, and philosophers.",
                    "features": "Dark studio aesthetic, aggressive interview style pushing guests beyond rehearsed talking points.",
                    "focus": "Cybersecurity, resource depletion, monetary policy, geopolitics, and civil liberties.",
                    "tips": "The ultimate test of auditory concentration: can you maintain complete comprehension over 2 hours without subtitles?"
                },
                {
                    "name": "Blast, Le Souffle de l'Info",
                    "badge": "Independent Video News",
                    "url": "youtube.com/@blast-info",
                    "what": "Independent citizen-backed media platform featuring investigative documentaries, sociopolitical essays, and debates.",
                    "features": "Hosted by veteran journalists (Denis Robert, Salomé Saqué); rigorous editorial line focusing on social justice.",
                    "focus": "Environmental transition, economic inequality, media monopolies, and political reform.",
                    "tips": "Analyze Salomé Saqué's fast-paced presentations for clear articulation of statistical and economic arguments."
                }
            ]
        },
        62: {
            "page": 62, "type": "resources",
            "title": "Specialized YouTube: Philosophy, Science & Ethics",
            "subtitle": "Intellectual Video Essays, Thought Experiments & Cognitive Science",
            "badge_num": "61",
            "intro": "Explore university-grade philosophy and scientific ethics presented with stunning visual storytelling.",
            "resources": [
                {
                    "name": "Monsieur Phi (Thibaut Giraud)",
                    "badge": "Analytical Philosophy",
                    "url": "youtube.com/@MonsieurPhi",
                    "what": "France's top academic philosophy channel, run by a doctor in philosophy exploring logic, ethics, and epistemology.",
                    "features": "Clear, precise dissection of philosophical paradoxes, trolley problems, AI ethics, and cognitive biases.",
                    "focus": "Logical deduction, formal rhetoric, precise argumentation terminology, and analytic philosophy.",
                    "tips": "His video series on 'Comment bien argumenter' is essential study material for DALF C1 argumentation."
                },
                {
                    "name": "Le Vortex (ARTE)",
                    "badge": "Science & Humanities",
                    "url": "youtube.com/@LeVortexARTE",
                    "what": "Collaborative project by ARTE bringing together leading French popularizers to discuss cross-disciplinary dilemmas.",
                    "features": "High-production sketches and dialogues blending linguistics, anthropology, neuroscience, and quantum physics.",
                    "focus": "Cross-disciplinary discourse, academic terminology, and ethical implications of technological innovation.",
                    "tips": "Take note of the linguistic transitions used to bridge hard scientific data with sociological theory."
                }
            ]
        },
        63: {
            "page": 63, "type": "resources",
            "title": "Documentaries, Classical Theatre & Masterclasses",
            "subtitle": "Accessing France's Highest Theatrical & Academic Traditions",
            "badge_num": "62",
            "intro": "Immerse yourself in classical French theatrical performance and public university chairs.",
            "resources": [
                {
                    "name": "Collège de France – Conférences en Ligne",
                    "badge": "The Pinnacle of Academia",
                    "url": "college-de-france.fr / YouTube",
                    "what": "Public university lectures given by France's most prestigious academic chairs since 1530: literature, physics, history.",
                    "features": "Free audio and video streams of full semester lecture courses by world-renowned French scholars.",
                    "focus": "Academic lectures (*cours magistraux*), dense periodic syntax, specialized research vocabulary, and rhetorical finesse.",
                    "tips": "Choose an inaugural lecture (*leçon inaugurale*) in a subject you love; listen to 20 minutes daily."
                },
                {
                    "name": "ARTE Concert & Théâtre Contemporain",
                    "badge": "Performing Arts",
                    "url": "arte.tv/fr/arte-concert",
                    "what": "Full live performances of French theatre, opera, and contemporary dance recorded at the Avignon Festival and Comédie-Française.",
                    "features": "Pristine acoustic capture, subtitles available in French, performances of classic and modern playwrights.",
                    "focus": "Theatrical projection, verse delivery (alexandrines in Racine/Molière), emotional cadence, and dramatic monologue.",
                    "tips": "Read the play's script alongside the theatrical performance to appreciate classical French prosody."
                }
            ]
        },
        64: {
            "page": 64, "type": "resources",
            "title": "4. Advanced Research Lexicons & Computational Tools",
            "subtitle": "Authoritative Academic Dictionaries & Stylistic Workstations",
            "badge_num": "63",
            "intro": "Harness the computational lexicographical databases used by French linguists and researchers.",
            "resources": [
                {
                    "name": "CNRTL – Trésor de la Langue Française informatisé (TLFi)",
                    "badge": "The Supreme Academic Lexicon",
                    "url": "cnrtl.fr/definition",
                    "what": "The most authoritative academic dictionary of the French language (19th and 20th centuries) created by the CNRS.",
                    "features": "100,000 words, 270,000 definitions, 430,000 literary examples from major authors, historical etymology, and syntactic regimes.",
                    "focus": "Tracking exact semantic nuances, literary usages, rare collocations, and historical register shifts.",
                    "tips": "Bookmark CNRTL as your primary dictionary. Read the literary quotes to see how masters used the word."
                },
                {
                    "name": "Dictionnaire des Synonymes et Nuances (CRISCO - Université de Caen)",
                    "badge": "Semantic Nuance Map",
                    "url": "crisco2.unicaen.fr/des",
                    "what": "Electronic dictionary of synonyms mapping lexical proximity and nuance gradients using mathematical clumping.",
                    "features": "Visual semantic distance maps showing which synonyms are formal, pejorative, literary, or archaic.",
                    "focus": "Finding the exact, irreplaceable word to express subtle shades of thought in essays.",
                    "tips": "Use CRISCO when writing your DALF C1 essays to eradicate generic verbs and repetitive adjectives."
                }
            ]
        },
        65: {
            "page": 65, "type": "resources",
            "title": "5. Standard Academic Coursebooks & Literature",
            "subtitle": "Grammar Perfectionnement & French Literary Classics",
            "badge_num": "64",
            "intro": "Complete your mastery of literary grammar and immerse yourself in France's greatest literary prose.",
            "resources": [
                {
                    "name": "CLE International – Grammaire Progressive du Français (Niveau Perfectionnement)",
                    "badge": "The Mastery Manual",
                    "url": "cle-international.com / Major Bookstores",
                    "what": "The pinnacle of pedagogical French grammars: covers the rarest syntax points, literary tenses, and stylistic elegance.",
                    "features": "Subjonctif imparfait, conditionnel passé 2e forme, inversion stylistique, concordance des temps complexe, figures de style.",
                    "focus": "Eliminating every remaining trace of non-native syntax and mastering formal written French prose.",
                    "tips": "Complete all exercises on 'La Nominalisation et les Procédés de Style' for direct application to DALF C1."
                },
                {
                    "name": "Éditions Gallimard – Collection Folio Classique & Pléiade",
                    "badge": "Literary Monuments",
                    "url": "gallimard.fr",
                    "what": "Immerse yourself in unabridged masterpieces of French thought and fiction with scholarly introductions and critical notes.",
                    "features": "Authors: Marcel Proust, Jean-Paul Sartre, Simone de Beauvoir, Albert Camus, Marguerite Duras, Michel Houellebecq.",
                    "focus": "Complex periodic sentence architecture, rich philosophical vocabulary, subtle irony, and psychological introspection.",
                    "tips": "Read 15 pages daily. Keep a dedicated notebook to record stunning sentences and rhetorical structures."
                }
            ]
        },
        66: {
            "page": 66, "type": "resources",
            "title": "6. Official DALF C1 Exam Prep & Synthèse de Documents",
            "subtitle": "Mastering the Rigorous 4-Hour Academic Examination",
            "badge_num": "65",
            "intro": "Structured training for the prestigious DALF C1 diploma granted by the French Ministry of Education.",
            "resources": [
                {
                    "name": "France Éducation International – Épreuves DALF C1",
                    "badge": "Official Benchmark",
                    "url": "france-education-international.fr",
                    "what": "Official examination archive offering past session papers, long audio recordings (interviews, lectures), and scoring rubrics.",
                    "features": "Choice between 2 domains: 'Lettres et Sciences Humaines' or 'Sciences'. Authentic candidate syntheses with examiner notes.",
                    "focus": "Compréhension orale (40m), écrite (50m), Production écrite : Synthèse + Essai (2h30), orale : Exposé + Débat (30m + 1h prep).",
                    "tips": "The 'Synthèse de documents' requires summarizing 2–3 disparate texts without adding any personal opinion."
                },
                {
                    "name": "Didier – Le DALF C1/C2 100% Réussite",
                    "badge": "The Essential Prep Guide",
                    "url": "didierfle.com",
                    "what": "Comprehensive methodology manual authored by official CIEP/FEI examiners with step-by-step synthesis templates.",
                    "features": "Audio tracks with academic lectures, analytical breakdowns of successful syntheses, and oral debate strategies.",
                    "focus": "Structuring the 15-minute oral monologue, anticipating jury objections, and defending a thesis under pressure.",
                    "tips": "Master the 3-part synthesis introduction: Accroche, Présentation des documents, Problématique & Plan."
                }
            ]
        },
        67: {
            "page": 67, "type": "checklist",
            "title": "C1 Intellectual Immersion & Fluency Checklist",
            "subtitle": "Audit Your Advanced Operational Proficiency and Research Habits",
            "badge_num": "66",
            "intro": "Before advancing to the final Module 8 Readiness Assessment, verify that you have achieved true intellectual and auditory autonomy.",
            "sections": [
                {
                    "title": "C1 Auditory & Intellectual Can-Do Benchmarks",
                    "items": [
                        "I can understand enough to follow extended speech on abstract and complex topics beyond my field, though I may confirm details occasionally.",
                        "I can follow complex academic lectures, panel discussions, and debates (France Culture, Collège de France) at full native speed.",
                        "I can recognize a wide range of idiomatic expressions, cultural allusions, and colloquial register shifts effortlessly.",
                        "I can synthesize information from multiple spoken and written sources into a coherent, objective oral or written presentation.",
                        "I can detect underlying attitudes, irony, and implicit sociopolitical stances in complex media reports.",
                        "I can formulate ideas and opinions with precision and relate my contribution skillfully to those of other speakers.",
                        "I can follow television plays, films, and classical theatre performances without relying on subtitles.",
                        "I have integrated authentic high-register French media into my professional and intellectual life on a permanent basis."
                    ]
                }
            ]
        }
    }

def get_c2_resources():
    return {
        53: {
            "page": 53, "type": "checklist",
            "title": "C2 French – Native Mastery & Lifetime Immersion Guide",
            "subtitle": "Level: C2 (Mastery / Polymathic Fluency) • Lifelong Cultural Integration",
            "badge_num": "52",
            "intro": "The C2 level represents the absolute peak of language acquisition: effortless, native-level mastery characterized by stylistic precision, rhetorical finesse, spontaneous wit, and cultural erudition.",
            "sections": [
                {
                    "title": "Core C2 Mastery & Aesthetic Methodology",
                    "items": [
                        "Beyond Functional Fluency: Shift your focus entirely from 'being understood' to stylistic elegance, rhythm, and rhetorical panache.",
                        "The Art of Nuance: Master the exact semantic shade of words, historical connotations, stylistic figures, and register subversion.",
                        "Spontaneous Dialectical Defense: Defend complex theses orally against adversarial intellectual cross-examination with poise."
                    ]
                },
                {
                    "title": "Weekly Polymathic Immersion Framework",
                    "items": [
                        "Monday & Wednesday: High-register intellectual clashes (France Culture Répliques / Alain Finkielkraut).",
                        "Tuesday & Thursday: Classical literature deconstruction and academic seminars (Collège de France / Académie Française).",
                        "Friday: Historic cultural archives and literary reviews (Apostrophes INA / La Nouvelle Revue Française).",
                        "Weekend: Literary prose composition (Plaidoyer / Dissertation tripartite) + reading Pléiade critical editions."
                    ]
                }
            ]
        },
        54: {
            "page": 54, "type": "resources",
            "title": "1. Prestigious Academic & Scholarly Institutions",
            "subtitle": "The Highest Sanctuaries of Francophone Intellectual & Literary Heritage",
            "badge_num": "53",
            "intro": "Connect directly with France's supreme academic bodies shaping literature, sciences, and the arts.",
            "resources": [
                {
                    "name": "Le Collège de France (Fondé en 1530)",
                    "badge": "The Pinnacle of Knowledge",
                    "url": "college-de-france.fr / YouTube",
                    "what": "France's most prestigious research and higher education institution: professors teach their research in public lectures.",
                    "features": "Over 10,000 hours of free video and audio lectures covering pure mathematics, literary theory, anthropology, and history.",
                    "focus": "Pristine academic French prose, groundbreaking intellectual paradigms, and philosophical rigor.",
                    "tips": "Follow a full lecture series by chairs in French literature (e.g. Antoine Compagnon, William Marx)."
                },
                {
                    "name": "L'Académie Française (Fondée en 1635)",
                    "badge": "The Guardians of the Language",
                    "url": "academie-francaise.fr",
                    "what": "The official council of the 'Immortels' tasked with defining the French language and producing the official Dictionnaire.",
                    "features": "Published reception speeches (*discours de réception*), literary prize citations, and columns on language disputes (*Dire, ne pas dire*).",
                    "focus": "Classical syntactic purity, rhetorical figures, eulogies, and normative linguistic jurisprudence.",
                    "tips": "Study the reception speeches of recent Immortels to observe the highest register of formal French rhetoric."
                }
            ]
        },
        55: {
            "page": 55, "type": "resources",
            "title": "National Archives & Historic Literary Media",
            "subtitle": "Exploring Centuries of Manuscript Treasures, Conferences & Philosophy",
            "badge_num": "54",
            "intro": "Access the digitized cultural memory of the Francophone world.",
            "resources": [
                {
                    "name": "BnF – Bibliothèque Nationale de France & Gallica",
                    "badge": "National Library Portal",
                    "url": "bnf.fr / gallica.bnf.fr",
                    "what": "France's national library providing millions of digitized books, manuscripts, rare recordings, and curator podcasts.",
                    "features": "Podcasts, virtual exhibitions, conferences by leading historians, and digitized original editions of classic masterpieces.",
                    "focus": "Paleography, book history, literary evolution from the Middle Ages to the Enlightenment, and intellectual history.",
                    "tips": "Explore Gallica's curated audio archives to hear French speech recordings from the early 20th century."
                },
                {
                    "name": "L'Institut de France",
                    "badge": "The Five Academies",
                    "url": "institutdefrance.fr",
                    "what": "The historic institution uniting France's five academies (Française, Inscriptions et Belles-Lettres, Sciences, Beaux-Arts, Sciences Morales).",
                    "features": "Public academic sessions, interdisciplinary debates, and ceremonial addresses by France's leading thinkers.",
                    "focus": "Formal eulogies, scientific philosophy, jurisprudence, aesthetic critiques, and classical humanitarian ethics.",
                    "tips": "Read the annual 'Séance Solennelle' proceedings to master solemn ceremonial French prose."
                }
            ]
        },
        56: {
            "page": 56, "type": "resources",
            "title": "Elite Literary Reviews & Critical Journals",
            "subtitle": "The Historic Periodicals Defining Modern French Letters & Philosophy",
            "badge_num": "55",
            "intro": "Read the most rigorous, historic literary reviews published continuously for over a century.",
            "resources": [
                {
                    "name": "La Nouvelle Revue Française (NRF - Gallimard)",
                    "badge": "The Literary Legend",
                    "url": "la-nrf.net / Éditions Gallimard",
                    "what": "Founded in 1908 by André Gide; the most influential literary review in modern French history.",
                    "features": "Original short fiction, critical essays, philosophical reflections, and poems by the greatest living Francophone authors.",
                    "focus": "Literary stylistics, avant-garde prose, critical textual commentary, and philosophical aesthetics.",
                    "tips": "Read one issue per quarter to keep your finger on the pulse of contemporary French high literature."
                },
                {
                    "name": "Revue des Deux Mondes",
                    "badge": "Historic Bimonthly Review",
                    "url": "revuedesdeuxmondes.fr",
                    "what": "One of the oldest continuously published reviews in Europe (founded 1829); published Balzac, Hugo, and Baudelaire.",
                    "features": "Rigorous essays exploring history, literature, philosophy, and foreign policy written by prominent academics.",
                    "focus": "Deep historical memory, classical essay architecture, sophisticated literary critique, and geopolitical reflection.",
                    "tips": "Notice how authors structure longform critical arguments with historical precedents and rhetorical elegance."
                }
            ]
        },
        57: {
            "page": 57, "type": "resources",
            "title": "2. Top C2 Podcasts: High-Register Debate & Thought",
            "subtitle": "The Most Intellectually Demanding Dialectics on French Radio",
            "badge_num": "56",
            "intro": "Listen to the sharpest intellectual minds clashing over philosophy, literature, and politics.",
            "resources": [
                {
                    "name": "Répliques (Alain Finkielkraut - France Culture)",
                    "badge": "The Ultimate Audio Benchmark",
                    "url": "radiofrance.fr/franceculture/podcasts/repliques",
                    "what": "Broadcast for over 35 years: philosopher Alain Finkielkraut invites two leading intellectuals to debate a profound question.",
                    "features": "Uncompromising high register, classical quotes cited from memory, complex periodic sentences, and intense dialectic.",
                    "focus": "Literary interpretation, political philosophy, cultural heritage, and existential questions.",
                    "tips": "If you can follow Répliques without fatigue, your auditory French comprehension is at true native mastery level."
                },
                {
                    "name": "Les Idées Larges (Laura Raim - ARTE / France Culture)",
                    "badge": "Contemporary Thought",
                    "url": "arte.tv/fr/videos/RC-021427/les-idees-larges / Spotify",
                    "what": "Sharp 25-minute intellectual confrontations exploring provocative sociological, economic, and philosophical theses.",
                    "features": "Laura Raim interrogates top researchers on groundbreaking academic essays and paradigm shifts.",
                    "focus": "Epistemology, critical theory, technological ethics, and structural sociology.",
                    "tips": "Summarize the two opposing philosophical schools presented in each episode in a 1-page synthetic essay."
                }
            ]
        },
        58: {
            "page": 58, "type": "resources",
            "title": "Top C2 Podcasts: History, Memory & Epistemology",
            "subtitle": "Scholarly Research Monograph Interviews & Deep Memory",
            "badge_num": "57",
            "intro": "Engage with academic historians and philosophers at the bleeding edge of historical epistemology.",
            "resources": [
                {
                    "name": "Matières à penser (France Culture)",
                    "badge": "Polymathic Dialogue",
                    "url": "radiofrance.fr/franceculture/podcasts/matieres-a-penser",
                    "what": "45-minute daily dialogues hosted by eminent intellectuals (Dominique Méda, René Frydman, Frédéric Worms).",
                    "features": "Explores ethical dilemmas, the future of work, democratic institutions, and medical humanities.",
                    "focus": "Philosophical ethics, social contracts, epistemological inquiry, and humanistic values.",
                    "tips": "Pay close attention to how guests construct rigorous dialectical syntheses (*thèse, antithèse, synthèse*)."
                },
                {
                    "name": "Paroles d'histoire (André Loez)",
                    "badge": "Scholarly History",
                    "url": "parolesdhistoire.fr / Spotify",
                    "what": "In-depth podcast interviewing academic historians on newly published research books, archival discoveries, and historiography.",
                    "features": "Scholarly discussions avoiding popular history simplifications; rigorous methodological inquiry.",
                    "focus": "Historiographical debates, source criticism, archival methodology, and international comparative history.",
                    "tips": "Great for acquiring the specialized scholarly French used in university dissertations and doctoral theses."
                }
            ]
        },
        59: {
            "page": 59, "type": "resources",
            "title": "Top C2 Podcasts: Linguistics, Rhetoric & Style",
            "subtitle": "Dissecting the Evolution, Quirks & Rhetorical Tropes of the Language",
            "badge_num": "58",
            "intro": "Deepen your meta-linguistic understanding of French syntax, etymology, and political rhetoric.",
            "resources": [
                {
                    "name": "Le Vif du sujet & Les Mots de l'actualité",
                    "badge": "Rhetorical Deconstruction",
                    "url": "francaisfacile.rfi.fr / radiofrance.fr",
                    "what": "Short linguistic chronicles dissecting how politicians, media, and corporations manipulate language.",
                    "features": "Euphemisms, semantic drift, buzzwords, and rhetorical fallacies analyzed through linguistics and etymology.",
                    "focus": "Political rhetoric, doublespeak (*la langue de bois*), semantic shifts, and neologisms.",
                    "tips": "Incorporate these analytical insights when preparing the DALF C2 critical analysis of press documents."
                },
                {
                    "name": "Tire ta langue (France Culture Archives)",
                    "badge": "Language History",
                    "url": "radiofrance.fr/franceculture/podcasts/tire-ta-langue",
                    "what": "Classic radio series celebrating the oddities, slang, regional idioms, and historical evolution of French.",
                    "features": "Linguists, lexicographers, and poets exploring why certain words disappear, spelling reforms, and French accents.",
                    "focus": "Old French roots, argot, phonetic shifts, and the poetic possibilities of French vocabulary.",
                    "tips": "Learn 1 archaic French turn of phrase per week to add literary charm to your written production."
                }
            ]
        },
        60: {
            "page": 60, "type": "resources",
            "title": "Top C2 Podcasts: High Culture & Theatrical Arts",
            "subtitle": "Blind Classical Music Critiques, Radio Theatre & Opera Analysis",
            "badge_num": "59",
            "intro": "Indulge in France's peerless high-culture radio programming and audio drama.",
            "resources": [
                {
                    "name": "La Tribune des critiques de disques (France Musique)",
                    "badge": "Aesthetic Discernment",
                    "url": "radiofrance.fr/francemusique/podcasts/la-tribune-des-critiques-de-disques",
                    "what": "Since 1946: three expert music critics listen blind to several recordings of a classical masterpiece and debate the finest.",
                    "features": "Exquisite aesthetic vocabulary, passionate defense of interpretations, subtle comparisons of timbre and tempo.",
                    "focus": "Sensory adjectives, aesthetic vocabulary, nuanced comparisons, and passionate rhetorical persuasion.",
                    "tips": "A fantastic lesson in how to articulate extremely subjective, subtle impressions with objective lexical precision."
                },
                {
                    "name": "Fictions de France Culture (Théâtre & Créations)",
                    "badge": "Full-Cast Audio Drama",
                    "url": "radiofrance.fr/franceculture/podcasts/fictions-theatre-et-cie",
                    "what": "Full-cast radio plays adapting classical tragedies, modern existential drama, and contemporary sci-fi.",
                    "features": "World-class voice actors from the Comédie-Française, cinematic sound design, and emotional intensity.",
                    "focus": "Rapid-fire dialogue, emotional inflection, dialect diversity, and poetic verse delivery.",
                    "tips": "Listen in complete darkness to fully engage your auditory imagination and emotional processing."
                }
            ]
        },
        61: {
            "page": 61, "type": "resources",
            "title": "3. Historic Cultural Television & Literary Panels",
            "subtitle": "Iconic Televised Debates with the Greatest Thinkers of the 20th Century",
            "badge_num": "60",
            "intro": "Witness the golden age of French cultural television where novelists and philosophers engaged in legendary verbal duels.",
            "resources": [
                {
                    "name": "Apostrophes (Bernard Pivot - INA)",
                    "badge": "The Greatest Literary TV Show",
                    "url": "ina.fr / YouTube",
                    "what": "Broadcast live on Friday nights (1975–1990): 90 minutes of unscripted debate between 4-5 authors hosted by Bernard Pivot.",
                    "features": "Iconic moments with Marguerite Duras, Vladimir Nabokov, Charles Bukowski, Claude Lévi-Strauss, and Françoise Sagan.",
                    "focus": "Spontaneous intellectual sparring, wit (*l'art de la repartie*), literary register, and intellectual passion.",
                    "tips": "Watch Pivot's interview with Marguerite Duras to observe how pause, silence, and cadence shape French rhetoric."
                },
                {
                    "name": "Bouillon de Culture (Bernard Pivot)",
                    "badge": "Cultural Roundtable",
                    "url": "ina.fr / YouTube",
                    "what": "The successor to Apostrophes (1991–2001), broadening the debate to cinema, theater, philosophy, and history.",
                    "features": "Includes the famous 'Questionnaire de Bernard Pivot' answered by global icons (Umberto Eco, Woody Allen).",
                    "focus": "Cultural references, poetic improvisation, literary storytelling, and witty repartee.",
                    "tips": "Answer the 10 questions of Bernard Pivot yourself in French to practice spontaneous literary self-expression."
                }
            ]
        },
        62: {
            "page": 62, "type": "resources",
            "title": "Master Rhetoric, Oratory & Eloquence",
            "subtitle": "The Art of Persuasion, Public Speaking Competitions & Classical Tropes",
            "badge_num": "61",
            "intro": "Master the classical rhetorical techniques that govern French legal defense and political oratory.",
            "resources": [
                {
                    "name": "Concours d'Éloquence & Concours Lysias",
                    "badge": "University Oratory",
                    "url": "youtube.com (Search: Concours Lysias / Conférence Berryer)",
                    "what": "Prestigious university law debate tournaments where students plead absurd or philosophical questions with wit and rigor.",
                    "features": "Praising the unpraisable, mock courtroom defenses, devastating rhetorical rebuttals, and standing ovations.",
                    "focus": "Rhetorical figures (chiasmus, antanaclasis, hyperbaton), comic timing, dramatic pauses, and persuasive ethos/pathos/logos.",
                    "tips": "Watch winning speeches to learn how to open an argument with an unforgettable literary hook (*l'accroche*)."
                },
                {
                    "name": "Études Rhétoriques & Stylistique (Chaines FLE / Lettres Modernes)",
                    "badge": "Stylistic Analysis",
                    "url": "youtube.com",
                    "what": "Academic video analyses examining the stylistic devices used in classical French texts from Bossuet to Proust.",
                    "features": "Deep dissections of sentence rhythm (cadence majeure/mineure), vowel harmony, and syntactical inversions.",
                    "focus": "Stylistic terminology, literary prosody, periodic sentence architecture, and euphonic rhythm.",
                    "tips": "Integrate 2 classical rhetorical figures (e.g. litotes, zeugma) into your practice DALF C2 plaidoyer."
                }
            ]
        },
        63: {
            "page": 63, "type": "resources",
            "title": "Classical Theatre & Auteur Cinema",
            "subtitle": "Molière's Wit, Racine's Alexandrines & French New Wave Immersion",
            "badge_num": "62",
            "intro": "Master the pinnacle of French dramatic language through live theatrical recordings and classic cinema.",
            "resources": [
                {
                    "name": "Comédie-Française en Ligne",
                    "badge": "The House of Molière",
                    "url": "comedie-francaise.fr / YouTube",
                    "what": "Full stage productions from France's oldest active national theatre (founded in 1680 by Louis XIV).",
                    "features": "Productions of Molière (*Le Misanthrope*), Racine (*Phèdre*), Corneille (*Le Cid*), Marivaux, and Edmond Rostand (*Cyrano*).",
                    "focus": "Alexandrine 12-syllable poetic meter, hemistich breaks, theatrical diction, and tragic/comic register.",
                    "tips": "Memorize Cyrano de Bergerac's 'Tirade du nez' to master rapid-fire rhythmic French elocution."
                },
                {
                    "name": "Cinéma d'Auteur Français (La Nouvelle Vague & Modern Auteurs)",
                    "badge": "Cinematic Mastery",
                    "url": "Criterion Channel / LaCinetek.com",
                    "what": "Uncompromising French cinema from Truffaut, Godard, Rohmer, Agnès Varda, Alain Resnais, and Olivier Assayas.",
                    "features": "Literary screenplays, philosophical dialogues, moral ambiguities, and naturalistic French speech rhythms.",
                    "focus": "Éric Rohmer's films (*Six Moral Tales*) are legendary for their articulate, novelistic dialogue exchanges.",
                    "tips": "Watch Rohmer's *Ma nuit chez Maud* with a pen in hand: it is a 110-minute masterclass in Pascalian philosophy."
                }
            ]
        },
        64: {
            "page": 64, "type": "resources",
            "title": "4. Master Reference Works & Lexicographical Authorities",
            "subtitle": "The Definitive Grammars & Historical Dictionaries of the French Language",
            "badge_num": "63",
            "intro": "Consult the ultimate authorities when settling fine points of grammar, usage, and etymology.",
            "resources": [
                {
                    "name": "Maurice Grevisse & André Goosse – Le Bon Usage",
                    "badge": "The Supreme Bible of French Grammar",
                    "url": "lebonusage.com / De Boeck Supérieur",
                    "what": "1,700-page monumental reference work consulted by the Académie Française, editors, and the Conseil d'État.",
                    "features": "Exhaustive coverage of every grammatical rule, historical exception, and literary variation backed by 40,000 author citations.",
                    "focus": "Settling any possible dispute regarding agreement, subjunctive use, prepositions, and literary punctuation.",
                    "tips": "Look up contested syntax rules in 'Le Grevisse' to discover how Racine, Hugo, or Proust resolved them."
                },
                {
                    "name": "Dictionnaire de l'Académie Française (9e Édition)",
                    "badge": "Official State Lexicon",
                    "url": "dictionnaire-academie.fr",
                    "what": "The official institutional dictionary of the French state, recently completed in its landmark 9th edition.",
                    "features": "Authoritative definitions, etymologies, register designations, and normative warnings against barbaric neologisms.",
                    "focus": "Pure French terminology, official legal/administrative vocabulary, and classical philosophical definitions.",
                    "tips": "Use the comparative search to see how the definition and spelling of words evolved between the 1st (1694) and 9th edition."
                }
            ]
        },
        65: {
            "page": 65, "type": "resources",
            "title": "5. Monumental Literature & Stylistic Compendia",
            "subtitle": "Masterpieces of French Thought in Definitive Pléiade Editions",
            "badge_num": "64",
            "intro": "Read the summit of French prose style in definitive scholarly critical editions.",
            "resources": [
                {
                    "name": "Bibliothèque de la Pléiade (Éditions Gallimard)",
                    "badge": "The Gold Standard of World Literature",
                    "url": "la-pleiade.fr",
                    "what": "The world's most prestigious literary collection: printed on fine bible paper, bound in leather with critical scholarly apparatus.",
                    "features": "Complete works of Montaigne (*Les Essais*), Pascal (*Les Pensées*), Proust, Chateaubriand, and Baudelaire.",
                    "focus": "Periodic syntax, psychological introspection, classical rhetorical balance, and timeless aesthetic beauty.",
                    "tips": "Reading one volume of Montaigne or Proust will elevate your active French vocabulary by thousands of words."
                },
                {
                    "name": "Marcel Proust – À la recherche du temps perdu",
                    "badge": "The Ultimate Syntactic Gauntlet",
                    "url": "gallimard.fr",
                    "what": "The greatest novel of the 20th century: 3,000 pages exploring memory, time, social snobbery, art, and love.",
                    "features": "Famous for its expansive, serpentine periodic sentences spanning up to 30 lines with multiple nested clauses.",
                    "focus": "Periodic sentence mastery, exquisite adjective placement, subtle irony, and sensory nuance.",
                    "tips": "Read the opening chapter of *Du côté de chez Swann* aloud to experience the musical breathing rhythm of Proustian prose."
                }
            ]
        },
        66: {
            "page": 66, "type": "resources",
            "title": "6. Official DALF C2 Examination & Thesis Defense",
            "subtitle": "Mastering the 30-Minute Oral Plaidoyer & 3-Part Dissertation",
            "badge_num": "65",
            "intro": "The highest qualification in French as a Foreign Language, certifying native bilingual equivalence.",
            "resources": [
                {
                    "name": "France Éducation International – Épreuves DALF C2",
                    "badge": "The Crown Credential",
                    "url": "france-education-international.fr",
                    "what": "Official C2 examination session archives featuring complex dossier materials (texts, statistical charts, and audio).",
                    "features": "2 separate examination sections: 1. Compréhension et production écrites (3h30), 2. Compréhension et production orales (30m + 1h prep).",
                    "focus": "Synthesizing a 2,000-word dossier into a structured academic essay (*dissertation*) and delivering a 15-minute defense monologue.",
                    "tips": "The oral defense requires a 15-minute uninterrupted presentation followed by a 15-minute adversarial debate with the jury."
                },
                {
                    "name": "Didier – Le DALF C2 100% Réussite",
                    "badge": "C2 Exam Master Guide",
                    "url": "didierfle.com",
                    "what": "The definitive preparation manual for C2 candidates with complete mock exams, audio files, and model dissertations.",
                    "features": "In-depth methodology for the 3-part dissertation (*thèse, antithèse, synthèse/dépassement*) and rhetorical persuasion.",
                    "focus": "Anticipating counter-arguments, managing the 1-hour oral preparation time, and maintaining stylistic poise.",
                    "tips": "Never take a dogmatic one-sided stance. A high-scoring C2 response demonstrates intellectual nuance and synthesis."
                }
            ]
        },
        67: {
            "page": 67, "type": "checklist",
            "title": "C2 Polymathic Fluency & Mastery Checklist",
            "subtitle": "Audit Your Effortless Native Equivalence and Stylistic Panache",
            "badge_num": "66",
            "intro": "Confirm that you have achieved effortless, spontaneous native bilingual equivalence across all domains of the French language.",
            "sections": [
                {
                    "title": "C2 Mastery Can-Do Benchmarks",
                    "items": [
                        "I have no difficulty understanding any kind of spoken language, whether live or broadcast, even when delivered at fast native speed.",
                        "I can appreciate and interpret subtle stylistic figures, irony, cultural puns, and colloquial double entendres effortlessly.",
                        "I can participate effortlessly in any debate or conversation with a good familiarity of idiomatic expressions and colloquialisms.",
                        "I can formulate thoughts smoothly and precisely, qualifying my statements and differentiating finer shades of meaning.",
                        "I can present a complex argument or literary critique with an effective logical structure that helps the listener notice significant points.",
                        "I can read with ease virtually all forms of the written language, including abstract, structurally complex, or highly colloquial literary texts.",
                        "I can write clear, smoothly-flowing complex texts in an appropriate style, using periodic sentence structures and advanced rhetorical devices.",
                        "French has become an organic, permanent dimension of my intellectual identity and daily life."
                    ]
                }
            ]
        }
    }
