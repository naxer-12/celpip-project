import pprint
import os

def get_c2_data():
    pages = {}

    # Page 1: Cover
    pages[1] = {
        "page": 1,
        "type": "cover",
        "title": "French Learning Roadmap & Checklist",
        "subtitle": "French C2",
        "badge_num": "",
        "intro": ""
    }

    # Page 2: Overall Objectives of C2 Level (Mastery / Bilingual Competence)
    pages[2] = {
        "page": 2,
        "type": "objectives",
        "title": "Overall Objectives of C2 Level (Mastery / Bilingual Virtuosity)",
        "subtitle": "Classical Eloquence, Spoken Virtuosity & Intuitive Native Fluency",
        "badge_num": "1",
        "intro": "Welcome to French C2! At this pinnacle of language acquisition, you achieve complete mastery (Maîtrise). You possess native-equivalent fluency, intuitive linguistic precision, classical oratorical power, and the ability to appreciate and deploy subtle literary nuance, irony, and cultural subtext effortlessly.",
        "sections": [
            {
                "title": "Speak (Spoken Production & Spoken Virtuosity)",
                "items": [
                    "Deliver an authoritative, unscripted oral critique and synthesis of a 15-minute recorded audio dossier on abstract cultural or scientific dilemmas.",
                    "Engage in rapid, high-level intellectual debate with an expert panel, handling hostile counter-arguments, logical fallacies, and rapid interruptions with supreme composure.",
                    "Modulate your register with masterly ease: effortlessly moving from contemporary Parisian street slang to classical 17th-century literary prose.",
                    "Command all nuances of French oratorical cadence: ternary rhythms, litotes, deliberate pauses, chiasmus, and witty irony."
                ]
            },
            {
                "title": "Listen (Intuitive Auditory Immersion)",
                "items": [
                    "Understand any spoken French without conscious cognitive effort, whether live native speech, muffled recordings, or fast overlapping dialogue.",
                    "Decode regional accents, contemporary verlan, archaic literary registers, and obscure cultural puns in real time.",
                    "Appreciate the emotional undercurrents, subtle psychological motives, and unspoken cynicism beneath public speeches and debates."
                ]
            }
        ]
    }

    # Page 3: Overall Objectives of C2 Level (Continued)
    pages[3] = {
        "page": 3,
        "type": "objectives",
        "title": "Overall Objectives of C2 Level (Continued)",
        "subtitle": "Academic Dissertation, Hermeneutic Acuity & Publication-Grade Prose",
        "badge_num": "2",
        "intro": "At C2, your reading and writing rival those of an educated native intellectual. You can produce publication-grade essays, navigate dense philosophical treatises, and write with flawless orthographic and syntactic elegance.",
        "sections": [
            {
                "title": "Write (Publication-Grade Production & Synthesis)",
                "items": [
                    "Compose comprehensive dossiers of synthesis and argumentative essays (700+ words in DALF C2, or condensed executive briefs) with impeccable rhetoric.",
                    "Craft analytical dissertations, cultural critiques, and persuasive political pamphlets worthy of prominent French periodicals.",
                    "Demonstrate total mastery of French stylistic conventions: incisive clauses, absolute inversions, rich metaphors, and expressive punctuation.",
                    "Exhibit zero syntactic, grammatical, or typographical errors; employ rare tenses (passé simple, subjonctif imparfait) with sovereign taste."
                ]
            },
            {
                "title": "Read (Hermeneutic Acuity & Literary Immersion)",
                "items": [
                    "Read classical literature (Rabelais, Proust, Baudelaire), contemporary avant-garde fiction, and dense metaphysical treaties with effortless comprehension.",
                    "Instantly recognize authorial styles, pastiches, ideological undertones, and historical intertextuality.",
                    "Synthesize highly complex, divergent treatises and deconstruct subtle sophisms and rhetorical sleights of hand."
                ]
            }
        ]
    }

    # Page 4: Real-Life Outcomes & Core Domains (Domains 1–3)
    pages[4] = {
        "page": 4,
        "type": "outcomes",
        "title": "C2 French – Real-Life Outcomes & Core Domains (Domains 1–3)",
        "subtitle": "Epistemology & Metaphysics, Constitutional Jurisprudence & Deep Ecology",
        "badge_num": "3",
        "intro": "At CEFR C2, your competence spans humanity's most demanding intellectual frontiers. Here are the first three macro-domains of mastery.",
        "table_headers": ["Macro-Domain", "Conceptual & Lexical Horizons", "Real-Life C2 Bilingual Milestones"],
        "table_rows": [
            ["1. Epistemology & Metaphysics", "Theory of consciousness, phenomenological reduction, ontology, logic, determinism", "➤ Deliver an impromptu keynote address analyzing the ontological limits of AI\n➤ Author a philosophical critique deconstructing deterministic reductionism"],
            ["2. Constitutional Jurisprudence", "Supranational sovereignty, human rights covenants, constitutional review, jurisprudence", "➤ Draft an amicus curiae legal brief for the European Court of Human Rights in French\n➤ Defend a constitutional petition before an appellate judicial committee with oratorical brilliance"],
            ["3. Deep Ecology & Anthropocene", "Systemic planetary boundaries, ecological breakdown, degrowth, biopolitics", "➤ Moderate a high-stakes multilateral climate convention with sovereign diplomatic poise\n➤ Formulate a comprehensive socioeconomic roadmap for post-carbon territorial resilience"]
        ],
        "footer_title": "Real-Life C2 Milestones (Domains 1–3)",
        "footer_items": [
            "Think, theorize, and publish original research directly in French with stylistic authority.",
            "Deconstruct and counter subtle intellectual sophisms in real-time academic symposiums.",
            "Command an active lexicon of over 10,000 words spanning all intellectual disciplines."
        ]
    }

    # Page 5: Core Domains & Topics (Domains 4–7)
    pages[5] = {
        "page": 5,
        "type": "outcomes",
        "title": "C2 French – Core Domains & Topics (Domains 4–7)",
        "subtitle": "Bioethics, Heterodox Economics, Literary Poetics & Anthropological Myths",
        "badge_num": "4",
        "intro": "Domains 4 through 7 address advanced scientific bioethics, global monetary systems, classical literary poetics, and foundational human mythologies.",
        "table_headers": ["Macro-Domain", "Conceptual & Lexical Horizons", "Real-Life C2 Bilingual Milestones"],
        "table_rows": [
            ["4. Advanced Bioethics & Genetics", "CRISPR gene editing, neural interfaces, transhumanist ethics, clinical trials", "➤ Preside over a national bioethics consultative committee on genome editing policies\n➤ Debate the moral implications of artificial wombs and cognitive neuro-enhancement"],
            ["5. Monetary Economics & Capitalism", "Modern monetary theory, sovereign debt crises, financialization, trade hegemony", "➤ Deliver an expert television commentary on central bank quantitative tightening\n➤ Critique the systemic risks of decentralized finance and shadow banking in a financial review"],
            ["6. Literary History & Poetics", "Classical French canon, prosody, stylistics, literary theory, hermeneutics", "➤ Write a published literary critique analyzing stylistic cadence in Marcel Proust\n➤ Recite and deconstruct classical French Alexandrine verse with flawless prosodic meter"],
            ["7. Structural Anthropology & Myth", "Foundational mythologies, kinship structures, rites of passage, collective memory", "➤ Analyze contemporary political rituals using structuralist anthropological methodology\n➤ Synthesize ethnological field reports on indigenous cosmologies and Francophone heritage"]
        ],
        "footer_title": "Real-Life C2 Milestones (Domains 4–7)",
        "footer_items": [
            "Participate as an equal peer alongside native French university professors and public intellectuals.",
            "Write essays characterized by impeccable rhythm, elegant metaphors, and razor-sharp argumentation.",
            "Appreciate the full emotional and historical resonance of every word in the French language."
        ]
    }

    # Page 6: Core Domains & Topics (Domains 8–10)
    pages[6] = {
        "page": 6,
        "type": "outcomes",
        "title": "C2 French – Core Domains & Topics (Domains 8–10)",
        "subtitle": "Information Warfare, French Linguistics & Utopian Urbanism",
        "badge_num": "5",
        "intro": "The final thematic domains examine cognitive warfare, the historical evolution of the French language, and the philosophical design of future human habitats.",
        "table_headers": ["Macro-Domain", "Conceptual & Lexical Horizons", "Real-Life C2 Bilingual Milestones"],
        "table_rows": [
            ["8. Cyberguerre & Opinion", "Cognitive warfare, algorithmic manipulation, deepfakes, state propaganda", "➤ Produce a comprehensive geopolitical intelligence report on election cyber-sabotage\n➤ Formulate defense doctrines safeguarding digital civil liberties against surveillance states"],
            ["9. Linguistics & Francophonie", "Diachronic linguistics, sociolinguistics, creole genesis, language politics", "➤ Analyze the evolution of the French language from Vulgar Latin to contemporary slang\n➤ Advocate for global multilingual policies and cultural diversity at international summits"],
            ["10. Utopian Architecture & Space", "Psychogeography, architectural phenomenology, mega-structures, territorial equity", "➤ Author an architectural manifesto on sustainable urban utopias and human scale\n➤ Defend the preservation of historical cultural landscapes against utilitarian urban sprawl"]
        ],
        "footer_title": "Real-Life C2 Milestones (Domains 8–10)",
        "footer_items": [
            "Exhibit total cultural and linguistic naturalization within the Francophone world.",
            "Navigate high-pressure media interviews and state debates with effortless linguistic virtuosity.",
            "Master the entire continuum of French literature from the Renaissance to the digital age."
        ]
    }

    # Page 7: Masterful Communicative Functions
    pages[7] = {
        "page": 7,
        "type": "functions",
        "title": "C2 French – Masterful Communicative Functions",
        "subtitle": "Socratic Irony, Oratorical Cadence, Subversive Wit & Sublime Concession",
        "badge_num": "6",
        "intro": "At C2, language is no longer an instrument of mere communication; it is an art of intellectual seduction, conceptual rigor, and sovereign persuasion.",
        "table_headers": ["Masterful Function", "Classical Formulae & Oratorical Turns", "Stylistic & Rhetorical Intent"],
        "table_rows": [
            ["Sublime Concession & Pivot", "Quand bien même l'on accorderait que... force est de reconnaître / Nonobstant ces louables intentions...", "Magnanimously concede maximum ground before executing an unanswerable philosophical checkmate."],
            ["Socratic Irony & Understatement", "Il est pour le moins singulier de constater que... / L'argument n'est point dénué d'une piquante ironie", "Expose intellectual contradictions with refined, razor-sharp French wit and polite detachment."],
            ["Chiasmus & Rhetorical Contrast", "Il faut manger pour vivre et non pas vivre pour manger / Quand la politique abdique, la barbarie triomphe", "Create symmetrical, memorable aphorisms that resonate in the listener's memory forever."],
            ["Ternary Oratorical Cadence", "Cette politique manque de souffle moral, de vision stratégique et de légitimité démocratique", "Deploy balanced three-part periods that endow the argument with acoustic authority and poetic weight."],
            ["Sovereign Conclusion", "Il n'est que de constater / Quoi qu'il en soit, l'histoire tranchera / En dernière instance...", "Close a masterclass debate with absolute conceptual clarity, elevating the debate above partisan squabbling."]
        ],
        "footer_title": "C2 Virtuosity Checklist",
        "footer_items": [
            "Never raise your voice; let the elegance and precision of your French disarm hostility.",
            "Command silence before speaking, and conclude with an unforgettable rhetorical resonance.",
            "Infuse your French with the spirit of Voltaire, the depth of Montaigne, and the clarity of Descartes."
        ]
    }

    # Pages 8-19: Classical & Literary Grammar, Stylistics & Rhetoric (12 pages)
    grammar_topics = [
        (8, "C2 Grammar: Le Passé Simple & le Passé Antérieur",
         "Active Production & Mastery in Classical Literary and Historical Prose",
         "While conversational French uses the passé composé, C2 mastery requires active, effortless production of the passé simple and anterior past in historical, narrative, and critical essays.",
         [
             ("All Verb Classes of the Passé Simple", [
                 "Class 1 in -a-: il parla, ils parlèrent; nous parlâmes, vous parlâtes (note circumflex).",
                 "Class 2 in -i-: il finit, ils finirent; il prit, ils prirent; il mit, ils mirent.",
                 "Class 3 in -u-: il courut, ils coururent; il connut, ils connurent; il mourut, ils moururent.",
                 "Class 4 in -in- (tenir, venir): il tint, ils tinrent; il vint, ils vinrent; nous tînmes, vous vîntes."
             ]),
             ("Le Passé Antérieur (Immediate Precedence in the Past)", [
                 "Formed with passé simple of auxiliary + past participle: 'Dès qu'il eut achevé son réquisitoire, il se rassit.'",
                 "Expresses an action completed immediately before another past action: 'À peine le décret fut-il promulgué que...'",
                 "Gives historical and biographical essays supreme narrative velocity and classical precision."
             ]),
             ("Stylistic Resonance in Modern Analytical Prose", [
                 "Used in leading historical reviews (L'Histoire) and high cultural essays.",
                 "Demonstrates total command of literary French heritage and narrative dignity."
             ])
         ]),
        (9, "C2 Grammar: Le Subjonctif dans ses Usages les Plus Rares",
         "Active Mastery of the Imperfect Subjunctive & Elliptical Clauses",
         "At C2, you actively employ the third-person imperfect subjunctive for elevated literary style and master rare subjunctive triggers.",
         [
             ("Active Deployment of 3rd Person Singular Subjonctif Imparfait", [
                 "Circumflex on vowel before -t: qu'il allât, qu'il sût, qu'il vînt, qu'il pût, qu'il mourût.",
                 "Example: 'Le roi exigea que chacun obéît sans murmurer.'",
                 "Example: 'Il fallait que la nation comprît l'urgence de la situation.'",
                 "Imparts unparalleled gravitas and stylistic distinction to formal written prose."
             ]),
             ("Subjonctif sans 'Que' (Optative & Concessive Inversions)", [
                 "Fût-ce : 'Fût-ce au prix de lourds sacrifices, nous devons agir.' (Even were it at the cost...).",
                 "Vienne / Viennent : 'Vienne l'orage, nous resterons debout.' (Come what storm may...).",
                 "Plaise à : 'Plaise au ciel que cette paix soit durable !'",
                 "Grand bien lui fasse ! / Coûte que coûte !"
             ]),
             ("Subjonctif dans les Propositions Relatives à Connotation Restrictive", [
                 "After superlatives: 'C'est le plus remarquable orateur que j'aie jamais entendu.'",
                 "After exclusive negatives: 'Il n'est personne qui ne sache la vérité.'",
                 "Expresses the conceptual limit of human experience."
             ])
         ]),
        (10, "C2 Stylistics: Figures de Style Majeures",
         "Chiasmus, Litotes, Oxymoron, Antiphrasis & Metonymy",
         "Figures of style are not mere ornaments; they are sophisticated instruments of cognitive persuasion and aesthetic delight.",
         [
             ("Le Chiasme (Crosswise Syntactic Symmetry: A-B-B-A)", [
                 "'La beauté de l'art console des laideurs de la vie, et dans les laideurs du monde l'art trouve sa beauté.'",
                 "'Il faut travailler pour vivre, et non consumer sa vie à travailler.'",
                 "Locks an intellectual truth into an unassailable geometric symmetry."
             ]),
             ("L'Oxymore & l'Antithèse (Harmonizing Apparent Contradictions)", [
                 "Oxymore: pairing contradictory words ('une obscure clarté', 'un silence assourdissant', 'une cruelle douceur').",
                 "Antithèse: opposing ideas across clauses ('Paris est un océan : jetez-y la sonde, vous n'en connaîtrez jamais la profondeur')."
             ]),
             ("La Litote, l'Euphémisme & la Prétérition", [
                 "Litote: say less to convey immense weight ('Va, je ne te hais point' = je t'aime éperdument).",
                 "Prétérition: announcing you will not speak of something while fully detailing it ('Je ne rappellerai point ici ses trahisons...')."
             ])
         ]),
        (11, "C2 Stylistics: L'Inversion Oratoire & la Période Rhétorique",
         "Mastering the Oratorical Period, Ternary Balance & Breath Control",
         "The classical French periodic sentence builds tension across multiple subordinate clauses before resolving triumphantly in the main clause.",
         [
             ("The Architecture of the French Period (La Période Oratoire)", [
                 "Protase (rising momentum): Accumulate subordinate hypotheses, participial clauses, and concessions.",
                 "Acmé (peak tension): The pivot point where the argument reaches maximum intensity.",
                 "Apodose (falling resolution): The main clause lands with crystal-clear philosophical decisiveness."
             ]),
             ("Example of a High-Classical Periodic Sentence", [
                 "'Quand bien même les temps seraient sombres, que les certitudes d'hier vacilleraient et que l'avenir semblerait barré d'orages, l'esprit humain ne saurait renoncer à sa quête de justice.'",
                 "Practice constructing and vocalizing 40-to-50 word periodic sentences with smooth breath control."
             ]),
             ("The Law of Increasing Constituents (La Loi des Constituants Croissants)", [
                 "In balanced prose, shorter sentence elements precede longer ones to maintain rhythmic acceleration."
             ])
         ]),
        (12, "C2 Syntax: Propositions Incises & Appositions Complexes",
         "Parenthetical Nuance, Detached Appositions & Punctuation Acuity",
         "Weave parenthetical insights and appositive adjectives into sentences without fracturing syntactic harmony.",
         [
             ("Mastering the Proposition Incise", [
                 "Insert reflections smoothly: 'Cette décision, me semble-t-il, pèche par excès d'optimisme.'",
                 "Subject inversion in incises: '..., affirment les observateurs, ...', '..., rétorqua-t-il d'une voix posée.'",
                 "Use em-dashes (tirets cadratins) for authoritative parenthetical commentary."
             ]),
             ("Detached Appositions at the Sentence Head", [
                 "'Inlassable voyageur, scrutateur lucide des âmes et styliste virtuose, l'écrivain nous livre ici son testament spirituel.'",
                 "Condenses extensive biographical or descriptive context into a luminous opening cascade."
             ]),
             ("Punctuation as a Musical Instrument", [
                 "The semicolon (point-virgule) balances independent clauses of equal intellectual weight.",
                 "The colon (deux-points) introduces an explanation, theatrical consequence, or dramatic revelation."
             ])
         ]),
        (13, "C2 Rhetoric: La Concession Ultime & le Dépassement",
         "Mastering Sovereign Concession: Quand bien même, Nonobstant, Ne fût-ce que",
         "Concession at C2 is not weakness; it is the ultimate display of intellectual magnanimity that precedes total philosophical victory.",
         [
             ("Quand bien même + Conditionnel", [
                 "'Quand bien même cette politique produirait des gains à court terme, elle hypothèque durablement l'avenir.'",
                 "Grants the adversary's best possible scenario, then proves it still fails fundamentally."
             ]),
             ("Nonobstant & En dépit de (Formal Register)", [
                 "'Nonobstant les protestations véhémentes de l'opposition, le décret a été promulgué.'",
                 "'Nonobstant le fait que...' (elevated variant of 'bien que')."
             ]),
             ("Ne fût-ce que (Restrictive Hypothesis)", [
                 "'Il faut tenter cette expérience, ne fût-ce que pour en démontrer l'infaisabilité.' (If only to...).",
                 "'Consacrez-y une heure par jour, ne fût-ce que pour maintenir vos acquis.'"
             ])
         ]),
        (14, "C2 Stylistics: L'Atténuation, l'Implicite & le Sous-Entendu",
         "The Art of Sovereign Understatement and Unspoken Allusion",
         "In French high society and intellectual debate, what is left unsaid carries ten times the weight of overt declaration.",
         [
             ("The Masterful Understatement (La Litote d'Usage)", [
                 "Instead of 'C'est absurde', say: 'La pertinence de cette conclusion m'apparaît pour le moins douteuse.'",
                 "Instead of 'Il ment', say: 'Il prend de singulières libertés avec l'exactitude historique.'",
                 "Renders your criticism lethal while preserving aristocratic politeness."
             ]),
             ("Decoding Sociocultural Subtexts", [
                 "Understand when praise is actually a veiled reprimand: 'Une proposition d'une remarquable audace...' (= totally unhinged).",
                 "'Un travailleur consciencieux' (= lacks imagination or brilliance)."
             ]),
             ("The Power of the Ellipsis", [
                 "Know when to stop speaking before the logical conclusion; let the listener's intellect complete the thought."
             ])
         ]),
        (15, "C2 Lexicology: Argot Contemporain, Verlan & Parler Jeune",
         "Decoding Street French, Slang, Verlan & Popular Expressions",
         "A true C2 bilingual commands the full spectrum of French, including modern street vernacular and youth slang.",
         [
             ("Contemporary Verlan & Street Lexicon", [
                 "'Le seum' (anger/frustration), 'le zbeul' (chaos), 'la hess' (misery/poverty).",
                 "'C'est chanmé' (méchant = wicked/amazing), 'c'est vénère' (énervé = furious), 'un reuch' (cher = expensive).",
                 "'Être en PLS' (Position Latérale de Sécurité = overwhelmed, in despair)."
             ]),
             ("Colloquial Idiomatic Expressions", [
                 "'Avoir le seum', 'faire crari' (pretend), 'se prendre un vent' (to get ignored/snubbed).",
                 "'C'est carré' (it's perfect/all good), 'casser la démarche' (strut with swagger)."
             ]),
             ("Sociolinguistic Codes and Registers", [
                 "Know when to appreciate street culture and cinema (La Haine, Les Misérables by Ladj Ly) without adopting inappropriate slang in formal settings."
             ])
         ]),
        (16, "C2 Lexicology: Français Classique & Archaïsmes Délibérés",
         "Deliberate Classical Flourishes, Archaic Precision & Legal Cadence",
         "Injecting deliberate classical flourishes into written prose to achieve historical depth and solemnity.",
         [
             ("Prestigious Archaic Adverbs and Particles", [
                 "'Naguère' (recently, in former times) vs 'Jadis' (in the ancient past).",
                 "'Prou' (much / enough, as in 'peu ou prou' = more or less).",
                 "'Ores' (now, as in 'd'ores et déjà' = already, from this moment on).",
                 "'Quérir' (to fetch, as in 'aller quérir des renforts')."
             ]),
             ("High-Register Classical Adjectives", [
                 "'Pellucide' (limpid, crystal clear), 'obsidional' (siege mentality, besieged).",
                 "'Pétulant' (vibrant, irrepressible), 'délétère' (harmful, toxic to mind or health).",
                 "'Faraud' (boastful, arrogant), 'pusillanime' (faint-hearted, timid)."
             ]),
             ("Legal and Diplomatic Solemnity", [
                 "Use these terms sparingly like rare spices; one well-placed classical word elevates an entire essay."
             ])
         ]),
        (17, "C2 Rhetoric: Connecteurs Logiques Rares & Rhétoriques",
         "Voire, Partant, Pour autant, Il n'en demeure pas moins, À rebours",
         "The rarest and most potent logical connectors in the French oratorical tradition.",
         [
             ("Voire (And even / Indeed)", [
                 "Used to escalate an assertion: 'Une maladresse, voire une provocation délibérée.'",
                 "Never say 'voire même' (a pleonasm condemned by the Académie française); write simply 'voire'."
             ]),
             ("Partant & Dès lors (Logical and Inevitable Consequence)", [
                 "'L'accusé était à l'étranger le soir du crime, partant incapable de l'avoir commis.'",
                 "Expresses deductive consequence with mathematical rigor."
             ]),
             ("Pour autant (Notwithstanding / Even so)", [
                 "Used in negative or interrogative contexts: 'Le projet a été validé ; est-il pour autant souhaitable ?'",
                 "'Il a commis des erreurs, il n'est pas pour autant disqualifié.'"
             ]),
             ("À rebours de / Au rebours de", [
                 "'Agir à rebours du bon sens' (contrary to common sense / against the grain)."
             ])
         ]),
        (18, "C2 Stylistics: L'Art de la Polémique & du Pamphlet",
         "The Great French Tradition of Polemical Literature and Satire",
         "From Voltaire and Émile Zola ('J'accuse...!') to modern public intellectuals, master the art of righteous polemic.",
         [
             ("Anaphora and Rhythmic Accumulation (L'Anaphore Oratoire)", [
                 "Repeat an opening phrase for overwhelming emotional and rhetorical power.",
                 "Example: 'Moi président de la République... Moi président de la République...'",
                 "Example: 'J'accuse le général... J'accuse le colonel... J'accuse les bureaux de la guerre...'"
             ]),
             ("The Deadly Sarcastic Compliment", [
                 "Praise the adversary's diligence only to reveal the monstrosity of their goals.",
                 "'On ne saurait refuser à nos adversaires un zèle admirable dans l'art de ruiner la nation.'"
             ]),
             ("The Dignified Moral Appeal", [
                 "Conclude polemics not with personal venom, but with a soaring appeal to universal human values."
             ])
         ]),
        (19, "C2 Linguistics: Subtilités Régionales & Francophonie Mondiale",
         "Socio-Historical Linguistics, Diachronic Evolution & French Norms",
         "Understanding how the French language lives, breathes, and evolves across 300 million speakers worldwide.",
         [
             ("The Concept of 'Le Bon Usage' vs Living Evolution", [
                 "The historical role of the Académie française and the Littré dictionary.",
                 "The inclusive evolution of vocabulary: feminization of titles, digital loanwords, and African Francophone innovations."
             ]),
             ("Francophone Linguistic Heritage", [
                 "Appreciate Caribbean creole literature (Aimé Césaire, Édouard Glissant, la créolité).",
                 "Understand Maghreb Francophone literature (Tahar Ben Jelloun, Assia Djebar).",
                 "The French language belongs to everyone who enriches it."
             ]),
             ("Linguistic Tolerance and Supreme Command", [
                 "The true C2 master knows the official standard rules better than anyone, allowing them to break them intentionally for artistic effect."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in grammar_topics:
        pages[page_num] = {
            "page": page_num,
            "type": "grammar",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ]
        }

    # Pages 20-29: Thematic Vocabulary Modules (10 pages)
    vocab_modules = [
        (20, "C2 Thematic Vocabulary: Épistémologie & Théorie de la Connaissance",
         "Ontology, Metaphysics, Phenomenological Inquiry & Mind-Body Dualism",
         "Master 12 profound philosophical terms to debate consciousness, reality, and scientific truth.",
         [
             ("L'Ontologie", "f.", "Philosophical study of the nature of being and existence", "L'ontologie heideggérienne explore la question du sens de l'Être."),
             ("La Phénoménologie", "f.", "Philosophical investigation of conscious experience", "La phénoménologie husserlienne propose un retour aux choses mêmes."),
             ("La Téléologie", "f.", "Explanation of phenomena by purpose or final design", "La biologie contemporaine rejette toute explication téléologique de l'évolution."),
             ("L'Incommensurabilité", "f.", "Lack of common measure between paradigms", "L'incommensurabilité des paradigmes scientifiques selon Thomas Kuhn prévient toute comparaison simpliste."),
             ("Le Solipsisme", "m.", "Philosophical idea that only one's own mind exists", "Ce doute méthodique poussé à l'extrême frôle le solipsisme absolu."),
             ("La Noosphère", "f.", "Sphere of human thought and spiritual consciousness", "Teilhard de Chardin conceptualise la noosphère comme étape ultime de l'évolution."),
             ("Immanent", "adj.", "Existing or operating within; inherent to the world", "Spinoza conçoit Dieu comme une puissance immanente à la nature."),
             ("Transcendant", "adj.", "Surpassing physical boundaries; otherworldly", "La morale kantienne repose sur un impératif catégorique transcendant."),
             ("L'Intellection", "f.", "Act of pure intellectual understanding", "L'intellection immédiate de ce théorème échappe à l'esprit non initié."),
             ("Le Déterminisme", "m.", "Doctrine that all events are causally determined", "La physique quantique a ébranlé le déterminisme mécaniste classique."),
             ("L'Axiome", "m.", "Self-evident proposition requiring no proof", "Toute géométrie formelle se déploie à partir d'un ensemble d'axiomes indémontrables."),
             ("Subsumer", "v.", "To classify, incorporate under a more general category", "Ce concept permet de subsumer une multitude de faits disparates sous une seule loi.")
         ]),
        (21, "C2 Thematic Vocabulary: Droit Supranational & Souveraineté",
         "Constitutionalism, International Treaties, Jus Cogens & Extradition",
         "Debate legal philosophy, international tribunals, and sovereign jurisdiction with judicial mastery.",
         [
             ("Le Jus Cogens", "m.", "Peremptory norms of international law from which no derogation is permitted", "L'interdiction de la torture relève du jus cogens universellement contraignant."),
             ("L'Extraterritorialité", "f.", "Jurisdiction of domestic law beyond national borders", "L'extraterritorialité des lois économiques américaines suscite de vives contestations diplomatiques."),
             ("La Supranationalité", "f.", "Authority transcending national state borders", "La Cour de justice de l'Union européenne incarne un modèle de supranationalité inédit."),
             ("L'Habeas Corpus", "m.", "Fundamental legal right protecting against arbitrary detention", "L'Habeas Corpus constitue la pierre angulaire de l'État de droit démocratique."),
             ("La Prérogative", "f.", "Exclusive right or privilege attached to an office", "La grâce présidentielle demeure une prérogative régalienne héritée de la monarchie."),
             ("L'Impugnation", "f.", "Challenging the validity of a legal act or treaty", "L'impugnation de cette clause contractuelle a été portée devant le tribunal arbitral."),
             ("Déroger", "v.", "To deviate from or circumvent a statutory rule", "Aucune disposition contractuelle ne saurait déroger à l'ordre public."),
             ("L'Erga Omnes", "loc.", "Rights or obligations enforceable against all states", "La protection de la haute mer engendre des obligations erga omnes pour toute la communauté internationale."),
             ("Le Contentieux", "m.", "Litigation, body of disputes before a court", "Le contentieux constitutionnel garantit la conformité des lois aux droits fondamentaux."),
             ("L'Inaliénabilité", "f.", "Quality of rights that cannot be surrendered or transferred", "L'inaliénabilité des droits de l'homme fonde la dignité humaine."),
             ("Abroger", "v.", "To formally repeal or abolish a law", "Le parlement a voté pour abroger définitivement ce décret désuet."),
             ("La Forclusion", "f.", "Loss of a legal right through failure to exercise it within time", "Le retard dans le dépôt du mémoire a entraîné la forclusion irrémédiable du recours.")
         ]),
        (22, "C2 Thematic Vocabulary: Écologie Profonde & Anthropocène",
         "Deep Ecology, Biocentrism, Planetary Boundaries & Systemic Collapse",
         "Analyze ecological collapse, thermodynamic limits, and post-humanist environmental philosophy.",
         [
             ("Le Biocentrisme", "m.", "Ethical view extending inherent value to all living beings", "Le biocentrisme rompt avec des siècles d'anthropocentrisme prédateur."),
             ("La Collapsologie", "f.", "Study of systemic civilizational collapse", "La collapsologie envisage l'effondrement thermo-industriel non comme une dystopie, mais comme une certitude."),
             ("L'Homéostasie", "f.", "Self-regulating equilibrium of an organism or planet", "L'hypothèse Gaïa décrit la Terre comme un système doué d'homéostasie climatique."),
             ("L'Entropie", "f.", "Measure of thermodynamic disorder and energy dissipation", "L'activité industrielle accélère l'entropie terrestre en dissipant des ressources non renouvelables."),
             ("L'Écocentrisme", "m.", "Holistic philosophy valuing whole ecosystems over individuals", "L'écocentrisme accorde des droits juridiques aux fleuves, forêts et montagnes."),
             ("La Biosphère", "f.", "Global ecological system integrating all living beings", "La préservation de la biosphère exige une réduction drastique de notre métabolisme économique."),
             ("L'Écocide", "m.", "Massive, deliberate annihilation of ecosystems", "L'introduction de l'écocide dans le droit pénal international redéfinit la responsabilité des multinationales."),
             ("Anthique", "adj.", "Relating to human nature (ou l'anthropisation)", "L'anthropisation quasi totale des paysages européens a détruit les espaces de naturalité primaire."),
             ("L'Eutrophisation", "f.", "Excessive nutrients causing aquatic dead zones", "L'eutrophisation des estuaires résulte du ruissellement massif d'engrais azotés."),
             ("Péricliter", "v.", "To decline toward extinction or complete collapse", "Les populations d'insectes pollinisateurs périclitent à un rythme alarmant."),
             ("La Biocapacité", "f.", "Earth's capacity to regenerate biological materials", "L'humanité consomme chaque année l'équivalent de 1,7 fois la biocapacité planétaire."),
             ("La Résilience", "f.", "Capacity of living systems to absorb catastrophic shocks", "La résilience des coraux tropicaux est mise à l'épreuve par le réchauffement des océans.")
         ]),
        (23, "C2 Thematic Vocabulary: Bioéthique Poussée & Génétique",
         "Genome Editing, Neuro-Enhancement, Chimeras & Transhumanist Ethics",
         "Navigate the ethical dilemmas of gene editing, artificial wombs, and post-biological evolution.",
         [
             ("L'Eugénisme", "m.", "Selection of desired genetic traits; ethical dilemma", "La tentation d'un eugénisme libéral ressurgit avec la démocratisation des tests génétiques embryonnaires."),
             ("L'Épigénétique", "f.", "Modifications of gene expression without altering DNA code", "L'épigénétique démontre que les traumatismes et l'environnement modèlent l'expression génomique."),
             ("La Chimère", "f.", "Organism containing cells from distinct species", "La création de chimères homme-animal en laboratoire soulève d'immenses vertiges éthiques."),
             ("L'Ectogenèse", "f.", "Gestation of a fetus in an artificial womb", "L'ectogenèse bouleverserait la maternité biologique et la symbolique de l'engendrement."),
             ("La Sénescence", "f.", "Biological aging process and cellular deterioration", "Les recherches sur la sénescence cellulaire visent à retarder indéfiniment la mort biologique."),
             ("La Neuroéthique", "f.", "Ethical study of brain interfaces and cognitive modulation", "La neuroéthique encadre les implants cérébraux pour préserver la liberté de conscience."),
             ("Le Clonage", "m.", "Asexual reproduction yielding genetically identical copies", "Le clonage reproductif humain fait l'objet d'une réprobation morale quasi universelle."),
             ("L'Iatrogénie", "f.", "Adverse condition induced by medical treatment or drugs", "Les effets iatrogènes de ce traitement expérimental ont contraint à l'arrêt prématuré des essais."),
             ("Thérapeutique", "adj.", "Relating to the healing of disease; medicinal", "La thérapie génique offre des perspectives thérapeutiques inespérées pour les maladies orphelines."),
             ("Dénaturer", "v.", "To alter natural qualities; pervert essence", "Les transhumanistes refusent l'idée qu'améliorer l'être humain reviendrait à le dénaturer."),
             ("La Somatisation", "f.", "Physical manifestation of psychological distress", "L'angoisse existentielle se traduit souvent par des somatisations chroniques complexes."),
             ("La Procréation", "f.", "Assisted reproduction (procréation médicalement assistée)", "La procréation médicalement assistée élargit les frontières traditionnelles de la filiation.")
         ]),
        (24, "C2 Thematic Vocabulary: Macroéconomie Hétérodoxe & Finance",
         "Central Banking, Shadow Banking, Fiat Currency & Post-Capitalism",
         "Deconstruct monetary policy, financialization, sovereign debt crises, and heterodox economic theories.",
         [
             ("L'Hétérodoxie", "f.", "Economic theories diverging from neoclassical orthodoxy", "L'hétérodoxie économique de Keynes et Schumpeter offre des clés pour penser les crises contemporaines."),
             ("La Financiarisation", "f.", "Dominance of financial markets over real economic output", "La financiarisation excessive de l'économie détourne le capital des investissements productifs."),
             ("La Liquidité", "f.", "Availability of cash or easily convertible assets", "La trappe à liquidité neutralise l'impact des baisses de taux directeurs décidées par la banque centrale."),
             ("La Déflation", "f.", "Persistent drop in overall price level causing recession", "La spirale déflationniste paralyse la consommation et alourdit le fardeau des dettes souveraines."),
             ("La Fongibilité", "f.", "Property of a good whose units are interchangeable", "L'or et les devises de réserve possèdent une fongibilité parfaite sur les marchés mondiaux."),
             ("L'Oligopole", "m.", "Market dominated by a small number of giant producers", "L'oligopole des géants du numérique étouffe la concurrence et dicte ses conditions aux régulateurs."),
             ("La Titrisation", "f.", "Packaging of debt obligations into tradeable securities", "La titrisation opaque des créances douteuses fut le détonateur de la crise des subprimes de 2008."),
             ("Spolier", "v.", "To dispossess, rob of property by fraud or force", "L'hyperinflation a pour effet de spolier les épargnants au profit des emprunteurs."),
             ("La Rente", "f.", "Economic income derived without productive contribution", "La rente pétrolière alimente des régimes autoritaires et freine la diversification économique."),
             ("L'Élasticité", "f.", "Measure of responsiveness of demand to price change", "L'élasticité-prix de l'énergie est particulièrement faible à court terme pour les ménages captifs."),
             ("La Chrématistique", "f.", "Aristotelian art of accumulating wealth for its own sake", "Aristote condamnait la chrématistique comme une perversion stérile de la véritable économie domestique."),
             ("Assainir", "v.", "To clean up, restore financial health to institutions", "Le gouvernement a dû injecter des capitaux publics pour assainir le bilan des banques en faillite.")
         ]),
        (25, "C2 Thematic Vocabulary: Histoire Littéraire & Poétique",
         "Prosody, Alexandrines, Semiotics, Intertextuality & Stylistics",
         "Analyze the architecture of French literary masterpieces from the Pléiade to the Nouveau Roman.",
         [
             ("La Prosodie", "f.", "Patterns of rhythm and sound in poetry and verse", "La prosodie racinienne allie la rigueur métrique de l'alexandrin à une musicalité tragique souveraine."),
             ("La Césure", "f.", "Rhythmic pause dividing a poetic line (césure à l'hémistiche)", "La césure à l'hémistiche coupe l'alexandrin classique en deux moitiés égales de six syllabes."),
             ("L'Enjambement", "m.", "Continuation of a sentence without pause beyond the end of a line", "L'enjambement baudelairien brise la monotonie du vers pour exprimer le déchirement du Spleen."),
             ("L'Intertextualité", "f.", "Complex relationship between texts referencing one another", "Ce roman contemporain déploie une intertextualité constante avec l'Odyssée d'Homère et l'Ulysse de Joyce."),
             ("La Polysémie", "f.", "Coexistence of multiple meanings in a word or text", "La polysémie du langage poétique mallarméen ouvre chaque strophe à d'infinies lectures symboliques."),
             ("L'Hypotypose", "f.", "Vivid, striking description that brings a scene to life", "L'hypotypose de la bataille de Waterloo chez Victor Hugo saisit le lecteur avec une force hallucinatoire."),
             ("L'Alchimie", "f.", "Mystical transformation of base materials into gold", "Baudelaire résume son ambition poétique : « Tu m'as donné ta boue et j'en ai fait de l'or »."),
             ("L'Aphorisme", "m.", "Pithy, concise observation containing a general truth", "Les maximes de La Rochefoucauld poussent l'aphorisme moraliste jusqu'à la perfection stylistique."),
             ("L'Exégèse", "f.", "Critical, scholarly explanation or interpretation of a text", "Une exégèse rigoureuse de la Recherche prouve la cohérence architecturale du projet proustien."),
             ("L'Incipit", "m.", "Opening words or sentence of a novel", "L'incipit de L'Étranger de Camus figure parmi les plus célèbres et déstabilisants de la littérature mondiale."),
             ("La Mise en abyme", "f.", "Story within a story, self-reflective artistic device", "Ce roman use de la mise en abyme en mettant en scène un écrivain rédigeant le livre que nous lisons."),
             ("La Solennité", "f.", "Stately solemnity, ceremonial gravity in language", "La solennité des oraisons funèbres de Bossuet captive par son souffle oratoire inégalé.")
         ]),
        (26, "C2 Thematic Vocabulary: Anthropologie Sociale & Mythes",
         "Structuralism, Kinship, Rites of Passage, Sacred & Profane",
         "Explore human societies, foundational cosmologies, and Lévi-Straussian structural anthropology.",
         [
             ("Le Structuralisme", "m.", "Method analyzing elements of human culture in relation to a broad system", "Le structuralisme de Claude Lévi-Strauss démontre l'universalité des structures logiques de l'esprit humain."),
             ("Le Totémisme", "m.", "Belief in a spiritual kinship with a totem animal or plant", "Le totémisme ne relève pas de la pensée magique enfantine, mais d'une classification symbolique sophistiquée."),
             ("L'Exogamie", "f.", "Custom of marrying outside a community or clan", "La prohibition universelle de l'inceste impose l'exogamie et fonde l'échange social entre les groupes."),
             ("Le Liminaire", "adj.", "Threshold state; transitional phase in a rite of passage", "La phase liminaire du rituel sépare l'initié du monde profane avant sa renaissance sociale."),
             ("Le Profane", "m./adj.", "Secular, non-sacred realm in social anthropology", "L'anthropologue Mircea Eliade oppose la transcendance du sacré à la quotidienneté du profane."),
             ("L'Animisme", "m.", "Belief that non-human entities possess a spiritual essence", "L'animisme amazonien conçoit les animaux et plantes comme des sujets dotés d'une intentionnalité propre."),
             ("L'Ethnocentrisme", "m.", "Judging other cultures by the standards of one's own", "L'ethnocentrisme colonial a longtemps aveuglé l'Occident sur la richesse des civilisations extra-européennes."),
             ("Transgresser", "v.", "To violate or breach a sacred social taboo", "Le mythe met souvent en scène un héros condamné pour avoir osé transgresser l'ordre divin."),
             ("Le Syncrétisme", "m.", "Merging of different religious cultures or schools of thought", "Le candomblé brésilien illustre un syncrétisme fascinant entre traditions yorubas et catholicisme."),
             ("L'Incommensurabilité", "f.", "Inability to compare disparate systems by common standards", "L'incommensurabilité apparente des cultures n'empêche pas l'existence d'invariants anthropologiques."),
             ("La Filiation", "f.", "Lineage, transmission of kinship and ancestral rights", "Les sociétés matrilinéaires organisent la filiation et la transmission des biens par la lignée maternelle."),
             ("Le Chamanisme", "m.", "Practice involving altered consciousness to interact with spirits", "Le chamanisme sibérien opère une médiation thérapeutique entre la communauté et les esprits tutélaires.")
         ]),
        (27, "C2 Thematic Vocabulary: Cyberguerre & Géopolitique des Données",
         "Cognitive Warfare, Deepfakes, Cyber-Espionage & Digital Sovereignty",
         "Master the technical and strategic lexicon of information conflict and sovereign cybersecurity.",
         [
             ("La Cyberguerre", "f.", "State-sponsored cyber-attacks targeting vital infrastructure", "La cyberguerre se déroule dans l'ombre sans déclaration officielle de belligérance."),
             ("L'Astroturfing", "m.", "Masking the sponsors of a message to make it appear grassroots", "Les fermes de trolls recourent à l'astroturfing pour simuler un mouvement citoyen spontané."),
             ("La Rétorsion", "f.", "Retaliatory countermeasures against cyber-sabotage", "L'Alliance atlantique a étendu l'article 5 aux cyberattaques justifiant des mesures de rétorsion."),
             ("L'Asymétrie", "f.", "Imbalance between conventional armies and stealthy cyber-hackers", "L'asymétrie du cyberespace permet à un petit commando de paralyser les réseaux électriques d'une superpuissance."),
             ("La Déniabilité", "f.", "Plausible deniability of state involvement in cyber-attacks", "La déniabilité plausible complique l'attribution juridique des cyberattaques sophistiquées."),
             ("L'Intégrité", "f.", "Soundness, uncorrupted state of data systems", "Garantir l'intégrité des registres électoraux numériques est une exigence démocratique absolue."),
             ("L'Exfiltration", "f.", "Covert unauthorized extraction of sensitive data", "L'exfiltration de documents confidentiels a mis en péril la sécurité des agents de renseignement."),
             ("Infiltrer", "v.", "To penetrate, gain unauthorized clandestine access", "Des rançongiciels ont réussi à infiltrer les serveurs hospitaliers, bloquant les blocs opératoires."),
             ("La Furtivité", "f.", "Stealth, capacity to operate undetected by security tools", "La furtivité de ce logiciel espion lui a permis de demeurer indétecté durant plusieurs années."),
             ("L'Hégémonie", "f.", "Dominance over cloud computing, microchips, and networks", "L'hégémonie technologique des fondeurs de semi-conducteurs concentre les tensions géopolitiques mondiales."),
             ("Le Rançongiciel", "m.", "Ransomware; malicious extortion software", "Les hôpitaux refusent de céder au chantage des cybercriminels réclamant une rançon en cryptomonnaies."),
             ("La Souveraineté", "f.", "Digital sovereignty over sovereign data and cables", "La souveraineté numérique européenne exige des infrastructures infonuagiques souveraines et indépendantes.")
         ]),
        (28, "C2 Thematic Vocabulary: Philosophie du Langage & Sémiotique",
         "Signifier, Signified, Speech Acts, Deconstruction & Hermeneutics",
         "Deconstruct the architecture of human language with Saussure, Austin, and Derrida.",
         [
             ("Le Signifiant", "m.", "Physical form of a linguistic sign (acoustic or written)", "Ferdinand de Saussure dissocie le signifiant phonétique du signifié conceptuel."),
             ("Le Signifié", "m.", "Mental concept or idea represented by a signifier", "Le lien unissant le signifiant au signifié est foncièrement arbitraire et conventionnel."),
             ("Le Performatif", "m./adj.", "Speech act where declaring something accomplishes the act", "Dans l'énoncé « Je vous déclare mari et femme », le verbe possède une valeur performative immédiate."),
             ("La Sémiotique", "f.", "Study of signs and symbols and their interpretation", "La sémiotique barthienne débusque les mythes bourgeois dissimulés dans les affiches publicitaires."),
             ("L'Aphasie", "f.", "Loss of ability to understand or express speech", "L'étude clinique des aphasies a permis de cartographier les aires cérébrales du langage."),
             ("La Déconstruction", "f.", "Derridean philosophical strategy challenging binary oppositions", "La déconstruction derridienne révèle les contradictions internes et les non-dits des textes philosophiques."),
             ("L'Arbitraire", "m.", "Lack of natural link between sign and referent", "L'arbitraire du signe linguistique est le postulat fondamental de la linguistique moderne."),
             ("Dénué", "adj.", "Devoid, stripped of meaning or substance", "Ce discours creux est entièrement dénué de portée conceptuelle réelle."),
             ("Le Référent", "m.", "The real-world object to which a linguistic sign points", "Il ne faut jamais confondre le référent empirique réel avec l'image mentale que nous en formons."),
             ("L'Interlocution", "f.", "Dialogue, reciprocal communication between subjects", "L'éthique de la discussion chez Habermas repose sur une interlocution symétrique et non coercitive."),
             ("La Métalangue", "f.", "Language used to describe or analyze language itself", "La grammaire et la linguistique constituent les métalangues indispensables à l'analyse textuelle."),
             ("La Pragmatique", "f.", "Study of language use in relation to practical context", "La pragmatique linguistique montre que le sens d'un énoncé dépend entièrement de la situation d'énonciation.")
         ]),
        (29, "C2 Thematic Vocabulary: Psychogéographie & Mutations Urbaines",
         "Urban Phenomenology, Situationist Drift, Megastructures & Spatial Justice",
         "Critique the emotional geometry of cities, architectural utopias, and contemporary territorial crises.",
         [
             ("La Psychogéographie", "f.", "Study of the precise effects of geographical environment on emotion", "La psychogéographie situationniste invite à une redécouverte sensible et subversive de la ville."),
             ("La Dérive", "f.", "Technique of rapid passage through varied ambiances without purpose", "La dérive théorisée par Guy Debord brise le conditionnement utilitaire du trajet domicile-travail."),
             ("L'Utopie", "f.", "Imagined ideal society or visionary architectural blueprint", "L'utopie moderniste de Le Corbusier rêvait d'une ville radieuse ordonnée autour de la ligne droite."),
             ("La Dystopie", "f.", "Oppressive, nightmare urban society", "Les mégapoles tentaculaires d'Asie du Sud-Est matérialisent les dystopies cyberpunk les plus sombres."),
             ("La Ségrégation", "f.", "Spatial separation of socioeconomic classes in cities", "La ségrégation spatiale renforce les inégalités scolaires et compromet la cohésion républicaine."),
             ("La Périurbanisation", "f.", "Expansion of residential zones on rural fringes", "La périurbanisation pavillonnaire engendre une dépendance absolue à l'automobile individuelle."),
             ("L'Anomie", "f.", "Breakdown of social norms and alienation in metropolis", "L'anomie urbaine guette les solitudes anonymes enfermées dans les grands ensembles dégradés."),
             ("Réhabiliter", "v.", "To restore, recondition historic buildings without gentrification", "Réhabiliter le centre ancien sans chasser les populations populaires relève du funambulisme politique."),
             ("La Bétonisation", "f.", "Paving over natural soil with concrete and tarmac", "La bétonisation outrancière des zones humides aggrave les inondations lors des épisodes méditerranéens."),
             ("L'Hyper-Lieu", "m.", "Globalized non-place characterized by intense connectivity", "Les aéroports internationaux constituent des hyper-lieux déconnectés de toute identité locale."),
             ("La Densification", "f.", "Increasing building density to curb urban sprawl", "La densification harmonieuse des cœurs de quartier évite l'artificialisation destructrice des terres arables."),
             ("L'Îlot", "m.", "Urban heat island (îlot de chaleur urbain)", "La création de coulées vertes permet de désamorcer les îlots de chaleur caniculaires en plein été.")
         ])
    ]

    for page_num, title, subtitle, intro, terms in vocab_modules:
        sections = []
        half = len(terms) // 2
        sections.append({
            "title": "Module Lexical: Haute Précision Conceptuelle (Partie 1)",
            "items": [
                f"{term} ({pos}): {defn} — Ex: « {ex} »"
                for term, pos, defn, ex in terms[:half]
            ]
        })
        sections.append({
            "title": "Module Lexical: Registres & Applications Littéraires (Partie 2)",
            "items": [
                f"{term} ({pos}): {defn} — Ex: « {ex} »"
                for term, pos, defn, ex in terms[half:]
            ]
        })
        pages[page_num] = {
            "page": page_num,
            "type": "thematic_vocab",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": sections
        }

    # Pages 30-39: Speaking Mastery (10 pages)
    speaking_pages = [
        (30, "C2 Speaking Mastery: La Restitution Critique (Format DALF C2)",
         "Oratorical Synthesis of a 15-Minute Audio Dossier Without Notes",
         "The DALF C2 oral examination is one of the most prestigious language tests in the world: you listen to a 15-minute authentic recording and deliver an unscripted, highly structured monologue followed by an in-depth debate.",
         [
             ("Phase 1: Deep Real-Time Synthesizing During Audio (15 mins)", [
                 "Listen to the 15-minute recording twice; take structured notes on the problem, conflicting voices, and ideological stakes.",
                 "Extract the central controversy without falling into chronological transcript summary.",
                 "Frame a philosophical problématique that connects the audio to broader civilizational questions."
             ]),
             ("Phase 2: The Masterful Monologue (10 to 15 mins)", [
                 "Introduction: Captivating hook, synthesis of audio sources, razor-sharp problem statement, clear plan.",
                 "Development: Present your personal analysis with balance, historical precedents, and cultural depth.",
                 "Conclusion: Powerful oratorical closure leaving an indelible impression on the jury."
             ]),
             ("Phase 3: The Intellectual Debate with the Jury (20 to 25 mins)", [
                 "Respond to probing questions from a panel of university examiners.",
                 "Demonstrate absolute poise, verbal agility, polite firmness, and intellectual subtlety."
             ])
         ]),
        (31, "C2 Speaking Mastery: Improvisation Oratoire Structurée",
         "The Art of Thinking on Your Feet with Architectural Precision",
         "True bilingual mastery means you never experience cognitive freezing. You can structure an eloquent argument in seconds.",
         [
             ("The Classical Tripartite Improv Structure", [
                 "Always anchor impromptu speech in a three-step movement: Constat (The Observation), Analyse (The Root Cause), Dépassement (The Philosophical Resolution).",
                 "Never wander aimlessly; every sentence must serve the overarching thesis."
             ]),
             ("The Technique of Conceptual Anchor Words (Les Mots-Piliers)", [
                 "Select three powerful abstract terms before speaking (e.g., légitimité, temporalité, responsabilité).",
                 "Weave these terms through your speech like musical motifs, creating thematic unity."
             ]),
             ("Controlling Physical Demeanor and Vocal Timbre", [
                 "Anchor feet firmly; maintain open, dignified posture and direct eye contact with every panel member.",
                 "Lower your vocal pitch slightly; a resonant, unhurried voice conveys authority and serenity."
             ])
         ]),
        (32, "C2 Speaking Mastery: Défense de Thèse sans Notes",
         "Delivering a Flawless 15-Minute Address with Maximum Eye Contact",
         "Reading from a script destroys oratorical charisma. At C2, you speak entirely from a one-page bullet-point outline.",
         [
             ("The One-Page Structural Memory Map", [
                 "Write only numbers, arrows, and conceptual keywords on your outline paper.",
                 "Never write complete sentences: reading pre-written sentences produces a flat, robotic intonation.",
                 "Glance down only during intentional pauses at transition moments."
             ]),
             ("Modulating Energy and Oratorical Crescendo", [
                 "Begin with quiet, measured solemnity; build intensity through concrete case studies.",
                 "Reach a persuasive rhetorical crescendo before delivering a poised, quiet conclusion."
             ]),
             ("Handling Memory Slips Gracefully", [
                 "If an exact statistic or author name escapes you, pivot without pausing: 'Comme le soulignait un éminent sociologue contemporain...'",
                 "Never apologize or say 'J'ai oublié'; maintain an unbroken illusion of effortless command."
             ])
         ]),
        (33, "C2 Spoken Interaction: Le Débat d'Experts avec le Jury",
         "Meeting University Professors as an Equal Intellectual Peer",
         "During the DALF C2 oral defense, examiners will challenge your core premise. Win the debate with elegance, not aggression.",
         [
             ("The Principle of Intellectual Magnanimity", [
                 "Compliment the examiner's objection before dismantling it: 'L'objection que vous soulevez est d'une redoutable pertinence, et elle touche au cœur de la contradiction...'",
                 "Shows total self-confidence and transforms a combat into a collaborative philosophical seminar."
             ]),
             ("Exposing Methodological Assumptions", [
                 "Politely unpack the premise of the question: 'Il me semble toutefois que votre question présuppose que le marché s'autorégule, ce qui est précisément le postulat contesté.'",
                 "Shift the debate from defending your conclusions to questioning the framework of the objection."
             ]),
             ("Varying Register Between Rigor and Warmth", [
                 "Use elevated academic discourse for theory, and warm conversational French for interactive banter."
             ])
         ]),
        (34, "C2 Spoken Interaction: Désamorçage d'Arguments Fallacieux",
         "Neutralizing Sophisms, Ad Hominem Attacks & False Equivalences",
         "Examiners deliberately use provocative or fallacious arguments to test your logical resilience.",
         [
             ("Neutralizing the Reductio Ad Absurdum", [
                 "Examiner: 'Alors pourquoi ne pas purement et simplement abolir toute loi ?'",
                 "C2 Response: 'Pousser l'argument jusqu'à cette absurdité permet de souligner les dangers d'un excès, mais mon propos ne saurait se confondre avec l'anarchisme. Il s'agit plutôt de...' ",
                 "Remain calm; dissect the rhetorical distortion with surgical detachment."
             ]),
             ("Neutralizing the False Analogy", [
                 "Examiner: 'Comparer cette réforme à Mai 68 est disproportionné !'",
                 "C2 Response: 'La comparaison n'est pas identité ; elle vaut sur le plan de la dynamique sociologique, non sur l'échelle des violences matérielles.'",
                 "Clarify the precise perimeter of your analogy."
             ]),
             ("The Art of the Decisive Counter-Question", [
                 "'Mais permettez-moi de vous retourner la question : comment garantiriez-vous l'équité sans ce mécanisme ?'"
             ])
         ]),
        (35, "C2 Spoken Interaction: L'Éloquence Spontanée & Maîtrise Vocale",
         "Breath Control, Intonation, Phonation and Acoustic Radiance",
         "Language at C2 is acoustic music. Master the physical mechanics of French pronunciation and oratorical resonance.",
         [
             ("Diaphragmatic Breathing and Vocal Placement", [
                 "Breathe from the lower abdomen; speak on sustained exhalations to ensure rich vocal resonance.",
                 "Avoid ending sentences with an upward question-like pitch inflection; land firmly on tonic accents."
             ]),
             ("The Melody of French Prosody", [
                 "Respect rhythmic group boundaries (groupes rythmiques); place tonic stress on the final syllable of the group.",
                 "Master compulsory liaisons ('les_enfants', 'un_homme') and optional elevated liaisons ('il est_arrivé', 'ils sont_allés').",
                 "Avoid forbidden liaisons that sound pedantic or uneducated ('un soldat // anglais', 'et // alors')."
             ]),
             ("Vocal Dynamics: Accelerando and Rallentando", [
                 "Accelerate slightly during narrative examples; slow down deliberately for philosophical maxims."
             ])
         ]),
        (36, "C2 Spoken Interaction: Nuances Culturelles & Esprit Français",
         "Mastering Wit, Subversive Irony, Sarcastic Banter & Understatement",
         "Understanding and wielding 'l'esprit français'—the intellectual tradition of witty paradox and playful irreverence.",
         [
             ("The Distinction Between 'L'Esprit' and 'L'Humour'", [
                 "English humour tends to be self-deprecating; French 'esprit' is rapid, satirical, philosophical, and conversational.",
                 "Use paradoxical turns of phrase that make the jury smile while acknowledging a serious truth."
             ]),
             ("Self-Possessed Detachment (La Désinvolture Maîtrisée)", [
                 "Never appear desperate to impress; speak with the easy, relaxed elegance of a salon conversationalist.",
                 "Smile gently at difficult questions: a relaxed posture signals complete intellectual dominance."
             ]),
             ("Navigating French Taboos and Shared Consensus", [
                 "Respect core republican values (laïcité, égalité républicaine, universalisme) while debating their contemporary tensions."
             ])
         ]),
        (37, "C2 Spoken Fluency: Aisance Native sans Hésitation Cognitive",
         "Zero Translation Delay, Total Spontaneous Conceptualization",
         "At C2, you no longer process thought in your native tongue. Your mind operates natively within the French conceptual apparatus.",
         [
             ("Achieving Direct Conceptualization", [
                 "Concepts like 'dépaysement', 'flânerie', 'laïcité', or 'esprit de l'escalier' exist as direct neural representations.",
                 "You formulate sentences directly around French syntactic idioms rather than translating word-by-word."
             ]),
             ("Rapid Topic Switching Drills", [
                 "Practice switching instantly between topics: from quantum computing to medieval stained glass windows in 30 seconds.",
                 "Maintain identical syntactic complexity and lexical precision across all subjects."
             ]),
             ("The Test of Spontaneous Humor", [
                 "When you can make native speakers laugh with an impromptu, culturally contextual pun, you have reached true C2."
             ])
         ]),
        (38, "C2 Spoken Mastery: Adaptation Immédiate à tout Contexte",
         "Chameleon-Like Register Shifts from Street Banter to Diplomatic Gala",
         "Adapt your vocabulary, body language, and syntax instantly to whoever you are speaking with.",
         [
             ("Speaking with Artisans, Workers & Youth (Populaire / Familier)", [
                 "Warm, direct, idiomatic, contractions without pretension: 'C'est pas évident', 'Ça roule', 'On fait aller'.",
                 "Never sound condescending or excessively bookish in informal settings."
             ]),
             ("Speaking in Corporate, Administrative & Media Contexts (Courant / Professionnel)", [
                 "Crisp, clear, efficient, nominalized, respectful of corporate hierarchy and institutional procedures."
             ]),
             ("Speaking in Academies, State Ceremonies & Legal Courts (Soutenu / Oratoire)", [
                 "Full grammatical concordances, subjunctive moods, subject inversions, zero contractions, aristocratic poise."
             ])
         ]),
        (39, "C2 Spoken Idioms: Proverbes Anciens, Aphorismes & Citations",
         "Weaving Classical Quotes, Maxims & Proverbs into Modern Discourse",
         "Deploy literary quotations and ancient proverbs with surgical relevance to settle philosophical debates.",
         [
             ("Classical Aphorisms for Rhetorical Climax", [
                 "'Le cœur a ses raisons que la raison ne connaît point' (Pascal) — For emotional vs rational policy debates.",
                 "'Science sans conscience n'est que ruine de l'âme' (Rabelais) — For bioethics and AI governance debates.",
                 "'Le mieux est l'ennemi du bien' (Voltaire) — For pragmatism vs ideological perfectionism.",
                 "'On ne naît pas femme, on le devient' (Simone de Beauvoir) — For gender, sociology, and existential freedom."
             ]),
             ("Timeless Proverbs Deployed with Irony", [
                 "'Tant va la cruche à l'eau qu'à la fin elle se casse' (Persistent recklessness brings disaster).",
                 "'Qui trop embrasse mal étreint' (Attempting too much accomplishes nothing).",
                 "'Il n'est de pire sourd que celui qui ne veut pas entendre' (Willful blindness to facts)."
             ]),
             ("Golden Rule of Citation", [
                 "Never quote to show off; quote only when the author's words crystallize your argument better than any paraphrase could."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in speaking_pages:
        pages[page_num] = {
            "page": page_num,
            "type": "speaking",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ]
        }

    # Pages 40-49: Listening Comprehension (10 pages)
    listening_pages = [
        (40, "C2 Listening Mastery: Dossiers Radiophoniques Complexes",
         "Decoding Dense 15-Minute Audio Tracks with Multiple Overlapping Voices",
         "The DALF C2 listening exam tests your ability to absorb a 15-minute uninterrupted recording of university debates or investigative radio reports.",
         [
             ("Mapping Complex Polyphonic Soundscapes", [
                 "Identify 3 to 5 distinct speakers: the presenter, the academic theorist, the pragmatic opponent, the field witness.",
                 "Distinguish each speaker's underlying thesis, personal biases, and rhetorical strategies.",
                 "Filter out rapid background ambient noises, applause, street sounds, and cross-talk."
             ]),
             ("Tracking Narrative Arcs Across 15 Minutes", [
                 "A 15-minute recording has its own dramatic rhythm: introduction, case studies, heated confrontation, philosophical resolution.",
                 "Map the turning points where speakers shift their stance or concede points."
             ]),
             ("Target Audio Sources", [
                 "Listen to 'Affaires étrangères' (France Culture), 'Le Grand Face-à-face' (France Inter), 'La Méthode scientifique'."
             ])
         ]),
        (41, "C2 Listening Mastery: Analyse Critique Immédiate d'Audio C2",
         "Extracting the Underlying Theoretical Stakes and Contradictions",
         "Moving beyond 'What did they say?' to 'Why did they say it, and what structural flaws exist in their logic?'",
         [
             ("Detecting Concealed Methodological Flaws", [
                 "Notice when an interviewee quotes selective data while omitting contradictory counter-evidence.",
                 "Identify when a politician evades a direct question by launching into an emotional personal anecdote."
             ]),
             ("Evaluating the Credibility of Experts", [
                 "Assess whether the speaker represents an independent research body, an ideological lobby, or a commercial enterprise.",
                 "Listen for telltale linguistic markers of corporate PR spin."
             ]),
             ("Preparing for the Oral Synthesis", [
                 "Formulate three critical questions you would pose to the speakers if they were in front of you."
             ])
         ]),
        (42, "C2 Listening Mastery: Compréhension Intuitive de l'Argot & Débit",
         "Decoding Fast Verlan, Colloquial Contractions & Native Speech at Max Speed",
         "Complete comfort with French spoken at 300+ words per minute in comedy shows, rap music, and crowded bistros.",
         [
             ("Decoding Rapid Verlan in Spontaneous Audio", [
                 "Understand verlan words in context without mental translation: 'zarbi', 'ouf', 'reum', 'meuf', 'keuf', 'ripou'.",
                 "Recognize double-verlan (verlan de verlan): 'rebeu' -> 'beur' -> 'arabe'."
             ]),
             ("Phonetic Reductions and Syllabic Elisions", [
                 "Listen to how native speakers collapse four words into one: 'Qu'est-ce qu'il y a ?' -> 'Kesskiya ?' [kɛskija].",
                 "'T'as qu'à le faire' -> [takalfɛʁ]. 'S'il te plaît' -> [stəplɛ].",
                 "Your ear processes these acoustic patterns directly as semantic wholes."
             ]),
             ("Immersion Material", [
                 "Listen to modern French stand-up comedy (Fary, Paul Mirabel) and French cinema without subtitles."
             ])
         ]),
        (43, "C2 Listening Mastery: Jeux de Mots, Calembours & Allusions",
         "Understanding Humor, Cultural Puns, Wordplay and Double Entendres",
         "The ultimate test of bilingual fluency: getting the joke in real time alongside native listeners.",
         [
             ("Decoding Homophonic Wordplay (Les Calembours)", [
                 "French literature and satirical media (Le Canard enchaîné) rely heavily on phonetic puns.",
                 "Example: Playing on 'sens' (direction, meaning, sensory perception) or 'vers' (toward, green, verse, worm).",
                 "Recognize the humorous friction created when two words sound identical but mean wildly different things."
             ]),
             ("Cultural and Literary Allusions in Radio Satire", [
                 "Listen to 'Les Grosses Têtes' or 'C'est encore nous' on France Inter.",
                 "Identify instant references to French political gaffes, historic scandals, and classical literary lines."
             ]),
             ("The Spontaneous Smile Test", [
                 "If you laugh at the exact moment the French audience laughs, your cognitive auditory lag is officially zero."
             ])
         ]),
        (44, "C2 Listening Mastery: Débats Télévisés Agités & Discours",
         "Navigating Heated Electoral Debates, Verbal Brawls and Interjections",
         "Presidential debates and prime-time political shows represent maximum acoustic chaos and rhetorical confrontation.",
         [
             ("Following Competing Threads During Shouting Matches", [
                 "Isolate the substantive policy debate from personal insults and posturing.",
                 "Notice who controls the temporal rhythm of the debate and who is pushed onto the defensive."
             ]),
             ("Decoding Interjections and Scornful Particles", [
                 "'Voyons !', 'Enfin !', 'Allons donc !', 'De grâce !', 'C'est un comble !'",
                 "These particles convey immense emotional and rhetorical voltage."
             ]),
             ("Analyzing Body Language in Video Debates", [
                 "Observe smirks, ironic head tilts, and dismissive hand gestures that accompany verbal exchanges."
             ])
         ]),
        (45, "C2 Listening Mastery: Prise de Notes Analytique Immédiate",
         "Mastering the Architecture of Fast Symbolic Notation for DALF C2",
         "Transforming a 15-minute auditory torrent into a structured two-page conceptual map.",
         [
             ("The Conceptual Hierarchy Mapping Method", [
                 "Never write full sentences. Use symbols, indented tiers, and geometric arrows.",
                 "Tier 1 (Left Margin): Core Paradigm Conflict (e.g., Liberté vs Sécurité).",
                 "Tier 2 (Indented): Divergent arguments deployed by speakers.",
                 "Tier 3 (Right Margin): Specific data points, author citations, and fallacies detected."
             ]),
             ("Developing Personalized Shorthand Symbols", [
                 "Psi = psychologique; Phi = philosophique; Delta = changement; Sigma = somme/société; Omega = fin/mort.",
                 "Circle points of severe disagreement in red pencil for instant retrieval during your oral presentation."
             ]),
             ("Five-Minute Post-Audio Review", [
                 "Immediately after the recording stops, spend 5 minutes drawing connective arrows between related arguments across the sheet."
             ])
         ]),
        (46, "C2 Listening Mastery: Décryptage des Non-Dits & Intentions",
         "Psychological Penetration of Hidden Agendas and Dissembled Motives",
         "At C2, you listen like an intelligence analyst, decoding the unspoken motivations of public speakers.",
         [
             ("Detecting the 'Langue de Bois' (Evasive Bureaucratic Discourse)", [
                 "Notice the proliferation of passive verbs, nominalizations, and vague abstractions designed to evade responsibility.",
                 "'Des mesures appropriées seront mises en œuvre le moment venu' = We have no plan and will do nothing."
             ]),
             ("Analyzing Strategic Pauses and Micro-Hesitations", [
                 "Notice when a speaker pauses uncharacteristically before answering: it signals cognitive discomfort or deception.",
                 "Identify sudden changes in vocal volume or register as defensive tells."
             ]),
             ("Evaluating Ethical Alignment", [
                 "Ask: 'Whose economic or political interests benefit if the audience accepts this speaker's premise?'"
             ])
         ]),
        (47, "C2 Listening Mastery: Conférences Philosophiques & Séminaires",
         "Following High-Level Epistemological Discourses (Collège de France)",
         "Engage with the world's most demanding academic lectures by French philosophers, mathematicians, and historians.",
         [
             ("Navigating Highly Abstract Conceptual Density", [
                 "Lecturers at the Collège de France (Foucault, Barthes, Bourdieu) construct intricate conceptual architectures.",
                 "Learn to hold abstract definitions in working memory while the speaker explores historical manifestations."
             ]),
             ("Recognizing Specialized Philosophical Vocabulary in Context", [
                 "Hear terms like 'aporétique', 'heuristique', 'paradigme', 'téléologique' and grasp their operational role immediately."
             ]),
             ("Listening as an Active Dialectical Dialogue", [
                 "Mentally interrogate the speaker's claims as they speak: anticipate objections and formulate counter-theses."
             ])
         ]),
        (48, "C2 Listening Strategies: Intuition Auditive Totale",
         "Zero Mental Translation, Total Immersion in the French Soundscape",
         "The final auditory milestone: French sounds as transparent and effortless as your mother tongue.",
         [
             ("The Total Immersion Environment", [
                 "Surround your daily life with authentic French: news, literature audiobooks, podcasts, telephone calls.",
                 "Your brain ceases to classify French as a 'foreign' tongue; it becomes a co-equal primary medium of cognition."
             ]),
             ("Instant Aesthetic Appreciation", [
                 "You appreciate not only the factual content of speech, but the musical beauty of a speaker's phrasing and timbre."
             ]),
             ("The Ultimate Auditory Proof", [
                 "You can fall asleep listening to a French philosophical podcast and wake up having understood the argument."
             ])
         ]),
        (49, "C2 Listening Checklist: Auto-Évaluation de la Maîtrise",
         "Official CEFR C2 Performance Indicators for Native-Level Auditory Mastery",
         "Confirm your complete auditory autonomy against international DALF C2 benchmarks.",
         [
             ("Complete Auditory Autonomy", [
                 "[ ] I understand any spoken French, including native speed, street slang, and academic jargon, without strain.",
                 "[ ] I can listen to a 15-minute recording from France Culture and deliver an immediate structured critique.",
                 "[ ] I instantly recognize subtle irony, sarcasm, cultural innuendos, and double meanings in humor.",
                 "[ ] I understand fast overlapping dialogue in heated televised political debates with zero cognitive lag."
             ]),
             ("Dialectical and Critical Acuity", [
                 "[ ] I can identify the underlying ideological assumptions and hidden sophisms in complex lectures.",
                 "[ ] I take structured, symbolic notes during a 15-minute audio track without transcribing full sentences.",
                 "[ ] I appreciate the poetic meter, rhythm, and classical oratorical cadence of French theatrical prose."
             ]),
             ("DALF C2 Exam Preparedness", [
                 "[ ] I am fully prepared to take the oral comprehension and production section of the DALF C2 examination."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in listening_pages:
        pages[page_num] = {
            "page": page_num,
            "type": "listening",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ]
        }

    # Pages 50-59: Reading Comprehension (10 pages)
    reading_pages = [
        (50, "C2 Reading Comprehension: Grands Textes Littéraires",
         "Navigating Marcel Proust, Louis-Ferdinand Céline, Albert Camus & Julien Gracq",
         "At C2, you read the towering monuments of French literature with total comprehension and profound aesthetic joy.",
         [
             ("Mastering the Proustian Periodic Sentence", [
                 "Navigate sentences spanning 20 lines with multiple relative subordinates, comparisons, and parenthetical insights.",
                 "Never lose the grammatical subject; follow the delicate psychological nuances as they unfold in slow motion.",
                 "Analyze how Proust's syntax mirrors the associative flow of involuntary memory."
             ]),
             ("Decoding Céline's Spoken-Language Stylistic Revolution", [
                 "Read 'Voyage au bout de la nuit': understand the three-dot cadence (les trois points), the fragmented syntax, and visceral street vocabulary.",
                 "Appreciate how Céline dismantled bourgeois academic prose to reinvent French literary rhythm."
             ]),
             ("Poetic Geographies of Julien Gracq", [
                 "Experience Gracq's majestic, slow-moving prose describing landscapes charged with military tension and mythical expectation."
             ])
         ]),
        (51, "C2 Reading Comprehension: Traités Philosophiques & Manifestes",
         "Engaging with Descartes, Rousseau, Sartre, Derrida, Deleuze & Foucault",
         "Read primary philosophical treatises in their original French text without dumbed-down translations.",
         [
             ("Deconstructing Classical Cartesian and Enlightenment Prose", [
                 "Read Descartes's 'Discours de la méthode' and Rousseau's 'Du contrat social'.",
                 "Notice the architectural clarity of classical 17th- and 18th-century French: 'Ce que l'on conçoit bien s'énonce clairement...'"
             ]),
             ("Navigating 20th-Century Post-Structuralist Philosophy", [
                 "Tackle Deleuze's 'Mille Plateaux', Derrida's 'De la grammatologie', and Foucault's 'Surveiller et punir'.",
                 "Understand how these thinkers intentionally subvert conventional grammar to interrogate power structures."
             ]),
             ("Synthesizing Complex Ideological Manifestos", [
                 "Extract the central radical thesis of an intellectual manifesto and evaluate its historical impact."
             ])
         ]),
        (52, "C2 Reading Comprehension: Revues Savantes & Études Critiques",
         "Reading Academic Journals: Revue Française de Science Politique, Les Temps Modernes",
         "Analyze specialized peer-reviewed papers published by leading French university presses (PUF, Seuil, Gallimard).",
         [
             ("Deconstructing the Academic Article Format", [
                 "Analyze the abstract, theoretical framing (revue de littérature), empirical methodology, and discussion.",
                 "Identify how authors position their work within or against existing schools of thought (Bourdieu vs Boudon)."
             ]),
             ("Extracting Theoretical Innovations", [
                 "Notice when an author introduces a new sociological or conceptual term (e.g., 'l'habitus', 'le capital symbolique').",
                 "Evaluate whether the empirical evidence genuinely justifies the author's theoretical conclusions."
             ]),
             ("Speed and Critical Acuity", [
                 "Read a 30-page academic article in 20 minutes and write an executive critique highlighting strengths and weaknesses."
             ])
         ]),
        (53, "C2 Reading Comprehension: Textes Polyphoniques & Ambivalence",
         "Deciphering Contradictory Narrators, Unreliable Voices & Double Meanings",
         "Advanced literature uses multiple narrators, unreliable testimony, and layered psychological ambiguity.",
         [
             ("Detecting the Unreliable Narrator (Le Narrateur Non Fiable)", [
                 "Identify when the narrator is self-deluded, hypocritical, or subtly insane (e.g., Camus's 'La Chute').",
                 "Spot contradictions between what the narrator claims to feel and how they actually behave."
             ]),
             ("Deciphering Polyphonic Novels", [
                 "Follow multiple narrative voices with distinct social registers, dialects, and ideological perspectives.",
                 "Understand that the author's true stance is not voiced by any single character, but emerges from their clash."
             ]),
             ("Embracing Ambiguity and Open Endings", [
                 "Great literature resists simplistic moralizing; learn to appreciate rich, unsolved philosophical ambiguities."
             ])
         ]),
        (54, "C2 Reading Strategies: Herméneutique & Déconstruction",
         "Reading as an Act of Deep Intellectual Deconstruction",
         "At C2, reading is an active interrogation of text, ideology, and linguistic power.",
         [
             ("The Hermeneutics of Suspicion (L'Herméneutique du Soupçon)", [
                 "Following Marx, Nietzsche, and Freud: look beneath surface declarations to uncover underlying power, economic, or psychological motives.",
                 "Ask: 'What ideological worldview does this text take for granted as \"natural\"?'"
             ]),
             ("Identifying Binary Oppositions and Deconstructing Them", [
                 "Find the foundational oppositions upon which the text rests: Nature vs Culture, Rational vs Emotional, Center vs Periphery.",
                 "Demonstrate how the text's own logic inadvertently undermines these rigid divisions."
             ]),
             ("Interrogating the Text's Absences and Silences", [
                 "Notice which social groups, perspectives, or historical facts are completely omitted from the narrative."
             ])
         ]),
        (55, "C2 Reading Strategies: Évaluation Idéologique & Stylistique",
         "Critiquing the Fusion of Form and Content in Masterpiece Prose",
         "Evaluate how an author's stylistic choices reinforce or contradict their stated ideological thesis.",
         [
             ("The Union of Form and Idea (Le Fond et la Forme)", [
                 "Notice how syntax embodies philosophical intent: a clipped, dry style mirrors cynical detachment.",
                 "Analyze how rhythm, alliteration, and sentence length evoke visceral emotional responses in the reader."
             ]),
             ("Spotting Stylistic Incongruities and Flaws", [
                 "Identify when an author slips into pretentiousness, mixed metaphors, or hollow rhetorical posturing.",
                 "Develop an incorruptible critical palate that distinguishes genuine literary genius from pretentious fashion."
             ]),
             ("Comparative Stylistic Audits", [
                 "Compare how three different authors describe the same historical event (e.g., the Paris Commune)."
             ])
         ]),
        (56, "C2 Reading Analysis: Synthèse de Textes Conceptuellement Divergents",
         "Synthesizing 4 Dense Texts into a Single Cohesive Philosophical Matrix",
         "The foundation of the DALF C2 written exam: digesting an extensive multi-document dossier and extracting a unified problematic.",
         [
             ("Building the Multi-Document Matrix (Le Tableau Synoptique C2)", [
                 "Dossier contains: 1 academic article, 1 historical text, 1 literary excerpt, 1 statistical survey (2,500 words total).",
                 "Map the texts across 3 philosophical tension axes: Ethical, Sociopolitical, and Ontological.",
                 "Identify hidden harmonies between seemingly unrelated disciplines (e.g., poetry and economics)."
             ]),
             ("Extracting the Core Dialectical Controversy", [
                 "Formulate an overarching question that encompasses all 4 texts without reducing them to simplistic summary."
             ]),
             ("Time Management Mastery", [
                 "Complete the exhaustive reading and matrix mapping of the 2,500-word dossier within 45 minutes."
             ])
         ]),
        (57, "C2 Reading Analysis: Reconnaissance Instantanée des Styles",
         "Recognizing Voltaire, Balzac, Flaubert, Hugo & Proust at a Glance",
         "A C2 Francophile can identify the author of an uncredited paragraph from syntactic and lexical fingerprints alone.",
         [
             ("Syntactic Fingerprints of Major Masters", [
                 "Voltaire: Swift, razor-sharp irony, light ternary rhythm, sparkling anticlerical wit.",
                 "Victor Hugo: Antithetical drama, grand cosmic metaphors, biblical solemnity, monumental lists.",
                 "Gustave Flaubert: Implacable objective detachment, sensory perfection, rhythmic cadence of the 'gueuloir'.",
                 "Émile Zola: Sweeping epic realism, biological determinism, colossal metabolic metaphors of society.",
                 "Marcel Proust: Immense periodic sentences, psychological dissection, sensory triggers, metaphors of art and time."
             ]),
             ("The Pastiche Recognition Test", [
                 "Differentiate between an original masterwork and a virtuoso stylistic imitation."
             ])
         ]),
        (58, "C2 Reading Analysis: Décryptage de l'Ironie Tragique & Satire",
         "The Fierce Satire of Swift, Voltaire, Montesquieu & Contemporary Pamphleteers",
         "Appreciating dark humor, bitter political pamphlets, and tragic irony in French letters.",
         [
             ("The Mechanics of Tragic Irony", [
                 "The audience or reader understands the horrific reality while the protagonist remains blind (e.g., Oedipe, Phèdre).",
                 "Analyze how French dramatists use double-edged dialogue to heighten tragic tension."
             ]),
             ("The Montesquieu Irony (De l'esclavage des nègres)", [
                 "Analyze Montesquieu's famous text: every argument in favor of slavery is deliberately monstrous and absurd.",
                 "Understand how absolute irony can be misinterpreted by naive readers as literal endorsement."
             ]),
             ("Contemporary Satirical Journalism", [
                 "Read Le Canard enchaîné and Charlie Hebdo with full cultural, political, and comedic comprehension."
             ])
         ]),
        (59, "C2 Reading Checklist: Auto-Évaluation de la Maîtrise Textuelle",
         "CEFR C2 Benchmarks for Literary Immersion, Hermeneutics & Hermetic Texts",
         "Confirm your complete reading autonomy across all centuries of the French literary and academic canon.",
         [
             ("Complete Textual Autonomy", [
                 "[ ] I read classical and contemporary French literature (Proust, Céline, Gracq, Camus) without a dictionary.",
                 "[ ] I understand dense philosophical treatises (Descartes, Rousseau, Sartre, Foucault) in the original French text.",
                 "[ ] I instantly detect irony, satire, unreliable narration, and double entendres in any written work.",
                 "[ ] I can identify the authorial style of major French literary masters from a single paragraph."
             ]),
             ("Synthesis & Analytical Acuity", [
                 "[ ] I can digest a 2,500-word multi-document dossier and extract a unified dialectical problematic in 45 minutes.",
                 "[ ] I read at 350+ words per minute with over 85% retention of complex conceptual arguments.",
                 "[ ] I appreciate the poetic meter, cadence, and stylistic architecture of French Alexandrine verse."
             ]),
             ("DALF C2 Exam Preparedness", [
                 "[ ] I am fully prepared to take the written comprehension and production section of the DALF C2 examination."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in reading_pages:
        pages[page_num] = {
            "page": page_num,
            "type": "reading",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ]
        }

    # Pages 60-67: Writing Mastery (8 pages)
    writing_pages = [
        (60, "C2 Writing Mastery: Le Dossier de Synthèse C2 (Méthode DALF)",
         "Writing an Authoritative, Integrated Synthesis and Argumentative Essay",
         "The DALF C2 written exam combines comprehension and production into a single monumental task: synthesizing a complex dossier and taking a defended stand (700+ words).",
         [
             ("The Integrated C2 Written Task Architecture", [
                 "Unlike C1 (which separates synthesis and essay), DALF C2 demands an integrated text.",
                 "You are commissioned as an expert rapporteur: you must synthesize the dossier's evidence while constructing an unassailable personal thesis.",
                 "Target length: minimum 700 words of dense, publication-grade academic French."
             ]),
             ("The 3.5-Hour Exam Time Budget", [
                 "Hour 1: Analytical reading of the dossier, comparative matrix, problematic formulation.",
                 "Hour 2: Detailed outline planning (dialectical structure, transitions, evidence pairing).",
                 "Hour 3: Writing with fluid stylistic rhythm, nominalization, and oratorical cadence.",
                 "Last 30 mins: Exhaustive proofreading for past participle agreements, subjunctive forms, and punctuation."
             ]),
             ("The Tone of Sovereign Authority", [
                 "Adopt the authoritative, objective voice of an academic director, senior diplomat, or chief editor."
             ])
         ]),
        (61, "C2 Writing Mastery: L'Essai Critique & la Dissertation",
         "The Sacred French Academic Discipline: Thèse, Antithèse, Synthèse",
         "The French dissertation is an intellectual ritual: a rigorous tripartite meditation that overcomes contradictions.",
         [
             ("The Anatomy of the Dialectical Movement", [
                 "Première Partie (Thèse): Validate the common assertion, explore its strongest justifications and evidence.",
                 "Deuxième Partie (Antithèse): Dismantle the thesis, reveal its hidden paradoxes, moral costs, and systemic failures.",
                 "Troisième Partie (Synthèse / Dépassement): Do NOT compromise ('a bit of both'). Reframe the question at a higher conceptual level."
             ]),
             ("The Sacred Art of Transitions (Le Bilan-Charnière)", [
                 "Every part must end with a transitional paragraph (le bilan-charnière).",
                 "Summarize the ground conquered in Part 1, identify its fundamental limitation, and pose the driving question of Part 2."
             ]),
             ("Proportion and Balance", [
                 "All three parts must be strictly balanced in word count and intellectual weight (~200 words each)."
             ])
         ]),
        (62, "C2 Writing Mastery: Le Plaidoyer Rhétorique & le Discours",
         "The Grand Tradition of French Legal and Political Eloquence",
         "Writing a persuasive speech (plaidoyer) destined to be delivered before a parliament, high court, or historical tribunal.",
         [
             ("The Classical Parts of an Oratorical Speech", [
                 "Exorde (Opening): Captivate the jury's benevolence and establish the moral stakes (captatio benevolentiae).",
                 "Narration (Narratio): State the uncontested facts with dramatic clarity and narrative tension.",
                 "Confirmation (Confirmatio): Present your legal, ethical, and philosophical proofs.",
                 "Réfutation (Refutatio): Anticipate and tear down the opposing counsel's arguments.",
                 "Péroraison (Peroratio): The emotional and moral climax; a soaring appeal to history and justice."
             ]),
             ("Deploying Rhetorical Devices for Maximum Impact", [
                 "Use anaphoras, rhetorical questions, and apostrophes ('Messieurs les jurés !', 'Citoyens !').",
                 "Vary sentence rhythm: build from short, urgent accusations to a majestic, rolling period."
             ])
         ]),
        (63, "C2 Writing Mastery: L'Article de Fond & la Revue Culturelle",
         "Publishing-Grade Cultural Criticism in Les Temps Modernes or Esprit",
         "Writing an authoritative long-form essay for intellectual periodicals, literary journals, or state cultural magazines.",
         [
             ("Crafting an Indelible Opening and Closing (Attaque et Chute)", [
                 "L'Attaque: Begin in media res with an astonishing cultural paradox or philosophical provocation.",
                 "La Chute: Close with an open-ended, haunting aphorism that resonates in the reader's intellect for days."
             ]),
             ("Balancing Intellect and Aesthetic Sensibility", [
                 "Combine rigorous conceptual analysis with vivid, sensual descriptions of artworks, films, or cities.",
                 "Avoid dry, pedantic academese; write with passionate, refined literary panache."
             ]),
             ("Targeting the Tone of High Francophone Periodicals", [
                 "Study the prose style of Le Débat, Esprit, Commentaire, and Revue des Deux Mondes."
             ])
         ]),
        (64, "C2 Writing Style: Élégance, Variété Lexicale & Panache",
         "The Signature of a Great Stylist: Eliminating Monotony and Clichés",
         "At C2, your prose must possess a distinct, memorable authorial voice and irreproachable stylistic elegance.",
         [
             ("Banishing Lexical Clichés and Dead Metaphors", [
                 "Purge tired clichés: replace 'la goutte d'eau qui fait déborder le vase' with 'le point de rupture', 'le détonateur'.",
                 "Replace 'au jour d'aujourd'hui' (an intolerable barbarism) with 'à ce jour', 'dans la conjoncture actuelle'.",
                 "Invent fresh, precise metaphors that illuminate abstract connections."
             ]),
             ("Syntactic Musicality and Cadence", [
                 "Read your draft aloud to test its acoustic musicality (l'épreuve du gueuloir).",
                 "Listen for awkward consonant collisions (cacophonies) or unintentional rhymes in prose.",
                 "Ensure clauses breathe naturally with human lung capacity."
             ]),
             ("Mastering the Rare Epithet", [
                 "Pair nouns with unexpected, deeply resonant adjectives: 'un silence de plomb', 'une lucidité féroce', 'une clarté lunaire'."
             ])
         ]),
        (65, "C2 Writing Style: Métaphores Originales & Rapprochements",
         "The Art of the Illuminating Metaphor and Conceptual Synthesis",
         "Metaphor at C2 is not decorative poetry; it is an engine of conceptual discovery that unites distant realities.",
         [
             ("The Aristotelian Theory of Metaphor", [
                 "Aristotle: 'To master metaphor is to perceive similarities between disparate domains.'",
                 "Illuminate an economic crisis using an ecological metaphor; illuminate an algorithm using a theological metaphor.",
                 "Example: 'L'oubli n'est pas la négation de la mémoire, mais son tamis nécessaire.'"
             ]),
             ("Avoiding Mixed Metaphors (Les Métaphores Filées et Incohérentes)", [
                 "Never mix incompatible imagery: 'Ce navire prend l'eau et prendra bientôt racine.'",
                 "Maintain metaphoric coherence throughout the paragraph (la métaphore filée)."
             ]),
             ("Subtle Symbolism", [
                 "Use recurring motifs (light, shadow, stone, water, mirrors) to create thematic cohesion across a long essay."
             ])
         ]),
        (66, "C2 Writing Mechanics: Ponctuation Expressive & Typographie",
         "The Musical and Logical Roles of Semicolons, Em-Dashes & Colons",
         "Punctuation in French is not merely grammatical; it is the rhythm and breath of thought itself.",
         [
             ("The Prestigious Semicolon (Le Point-Virgule)", [
                 "Separates two independent clauses whose logical link is so intimate that a period would sever the thought, while a comma would blur it.",
                 "Example: 'L'utopie est nécessaire ; elle dessine l'horizon vers lequel cheminent les peuples.'"
             ]),
             ("The Em-Dash for Incisive Asides (Le Tiret Cadratin — )", [
                 "Use em-dashes (with spaces) for authoritative parenthetical commentary.",
                 "Example: 'Cette politique — faut-il le rappeler ? — a conduit le pays au bord de l'abîme.'"
             ]),
             ("French Typographical Invariants", [
                 "Guillemets français (« ... ») with internal non-breaking spaces, never straight quotes (\").",
                 "Mandatory non-breaking space before : ; ! ? % €.",
                 "Capitalization of accented letters: É, À, Ç, È, Î, Ô."
             ])
         ]),
        (67, "C2 Writing Mechanics: Perfection Orthographique & Zéro Faute",
         "The Ruthless Final Proofreading Protocol of the C2 Master",
         "At C2, a single careless agreement error in a public dissertation damages intellectual credibility. Apply this ruthless protocol.",
         [
             ("The Reverse-Sentence Proofreading Scan", [
                 "Read your text backwards, sentence by sentence, from the conclusion to the introduction.",
                 "Decouples brain from narrative flow, forcing total visual focus on individual word agreements."
             ]),
             ("The Four Deadly Grammatical Traps", [
                 "1. Past participles of pronominal verbs (se succéder, se plaire -> invariables : elles se sont succédé).",
                 "2. Past participles followed by infinitives: 'Les chanteurs que j'ai entendus chanter' (heard them sing) vs 'La chanson que j'ai entendu chanter' (heard it sung).",
                 "3. Adjectives of color: compound colors are invariable ('des yeux bleu marine', 'des robes vert pomme').",
                 "4. Subjunctive irregularities: 'qu'il voie' (not qu'il voit), 'qu'il croie' (not qu'il croit)."
             ]),
             ("The Final Word Count Audit", [
                 "Verify that the text meets or exceeds 700 words (for DALF C2) with zero filler or redundant verbiage."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in writing_pages:
        pages[page_num] = {
            "page": page_num,
            "type": "writing",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ]
        }

    # Pages 68-71: Final Self-Evaluation & Lifelong Francophone Mastery (4 pages)
    audit_pages = [
        (68, "Final Self-Evaluation: Masterful Spoken Eloquence & Debate Acuity",
         "Audit of Spoken Virtuosity, Unscripted Monologues, and Expert Panels",
         "Evaluate your oral performance against the highest international criteria of the DALF C2 jury.",
         [
             ("1. Restitution Critique & Monologue sans Notes (DALF C2 Format)", [
                 "[ ] I can listen to a 15-minute uninterrupted academic recording and deliver an immediate structured critique.",
                 "[ ] I present a 15-minute unscripted monologue speaking only from a one-page bullet-point outline.",
                 "[ ] I formulate a profound, original philosophical problématique that connects the audio to civilizational issues.",
                 "[ ] I deploy ternary rhythms, oratorical periods, litotes, and classical metaphors with effortless grace."
             ]),
             ("2. Débat d'Experts avec le Jury (Spoken Interaction)", [
                 "[ ] I debate university professors as an equal intellectual peer, maintaining absolute poise and charm.",
                 "[ ] I neutralize false dilemmas, slippery slopes, and provocative sophisms with surgical logic.",
                 "[ ] I concede maximum ground magnanimously before pivoting to an unanswerable philosophical counter-stroke.",
                 "[ ] I modulate my tone effortlessly between formal academic defense and engaging, witty conversational banter."
             ]),
             ("3. Native Acoustic Fluency & Prosody", [
                 "[ ] I speak with diaphragmatic vocal resonance, perfect tonic accentuation, and zero cognitive pauses.",
                 "[ ] I command the full spectrum of French idioms, classical quotes, and contemporary street slang."
             ])
         ]),
        (69, "Final Self-Evaluation: Native-Equivalent Auditory & Literary Immersion",
         "Audit of High-Speed Audio, Cultural Wit, and Classical Textual Acuity",
         "Assess your ability to understand any spoken or written French across all historical eras, genres, and media formats.",
         [
             ("1. Compréhension Orale Native (Listening)", [
                 "[ ] I understand any spoken French without conscious cognitive effort, including street slang and dense academic lectures.",
                 "[ ] I immediately catch subtle irony, sarcasm, double entendres, and cultural allusions in radio satire.",
                 "[ ] I follow fast overlapping dialogue in televised electoral debates with zero comprehension fatigue.",
                 "[ ] I understand all regional and international Francophone varieties (Quebec, West Africa, Belgium, Switzerland)."
             ]),
             ("2. Compréhension Écrite & Herméneutique (Reading)", [
                 "[ ] I read classical literature (Proust, Céline, Gracq, Hugo, Montaigne) with profound aesthetic delight.",
                 "[ ] I read dense philosophical treatises (Descartes, Rousseau, Sartre, Foucault) in the original French text.",
                 "[ ] I can digest a 2,500-word multi-document dossier and build a complete comparative matrix in 45 minutes.",
                 "[ ] I instantly recognize authorial styles, pastiches, and the ideological subtexts of literary works."
             ])
         ]),
        (70, "Final Self-Evaluation: Flawless Written Production & Stylistic Panache",
         "Audit of the 700+ Word Integrated Synthesis and Academic Dissertation",
         "Verify your written production against official DALF C2 grading rubrics (Dossier de Synthèse & Essai critique).",
         [
             ("1. Le Dossier de Synthèse & l'Essai Critique (DALF C2)", [
                 "[ ] I can compose an integrated dossier synthesis and critical essay exceeding 700 words within 3.5 hours.",
                 "[ ] My introduction features an unforgettable hook, an incisive problem statement, and a balanced tripartite plan.",
                 "[ ] My dissertation follows a rigorous dialectical movement (Thèse / Antithèse / Dépassement) with transitional pivots.",
                 "[ ] My conclusion delivers an authoritative philosophical synthesis and an inspiring opening ('élargissement')."
             ]),
             ("2. Stylistic Brilliance & Authorial Voice", [
                 "[ ] I vary sentence lengths musically, deploying absolute inversions, appositions, and periodic sentences.",
                 "[ ] I command a rich palette of rare logical connectors (voire, partant, nonobstant, à rebours de).",
                 "[ ] I use expressive punctuation (semicolons, em-dashes, colons) and follow strict French typographical rules.",
                 "[ ] My writing is entirely free of clichés, weak verbs, and repetitive syntactic structures."
             ]),
             ("3. Zero-Defect Orthographic & Grammatical Accuracy", [
                 "[ ] My 700+ word draft contains zero errors in past participle agreement, subjunctive mood, or gender concordance."
             ])
         ]),
        (71, "Final Milestone: Full CEFR C2 Bilingual Mastery & Lifelong Fluency",
         "The Pinnacle of French Language Acquisition: Lifelong Bilingual Mastery",
         "Félicitations ! You have completed the entire 6-level CEFR French Learning Roadmap (A1, A2, B1, B2, C1, C2)!",
         [
             ("The CEFR C2 Master (Maîtrise)", [
                 "You are no longer a non-native speaker studying a second language. You possess full bilingual mastery of the French language.",
                 "You think, theorize, create, debate, love, and dream in French with the same effortless nuance as a native Francophone intellectual.",
                 "You hold the keys to one of the world's greatest cultural, philosophical, literary, and diplomatic traditions."
             ]),
             ("The DALF C2 Certification Success", [
                 "[ ] Compréhension et production orales: Scored 25+/50 on official DALF C2 mock trials.",
                 "[ ] Compréhension et production écrites: Scored 25+/50 on official DALF C2 mock trials.",
                 "[ ] Overall composite score exceeds 50/100, earning the permanent, lifetime DALF C2 Diploma from the French Ministry of Education."
             ]),
             ("The Lifelong Francophone Journey", [
                 "Language mastery is not an endpoint; it is an enduring way of life. Continue reading Le Monde, listening to France Culture, devouring French novels, attending the theater, and engaging with the global Francophone community for the rest of your life."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in audit_pages:
        flattened_items = []
        for s_title, s_items in sections:
            flattened_items.extend(s_items)
            
        pages[page_num] = {
            "page": page_num,
            "type": "audit",
            "title": title,
            "subtitle": subtitle,
            "badge_num": str(page_num - 1),
            "intro": intro,
            "sections": [
                {"title": s_title, "items": s_items} for s_title, s_items in sections
            ],
            "items": flattened_items
        }

    return pages

if __name__ == "__main__":
    c2_data = get_c2_data()
    print(f"Generated C2 data: {len(c2_data)} pages")
    with open("c2_curriculum_data.py", "w", encoding="utf-8") as f:
        f.write("# c2_curriculum_data.py\n")
        f.write("# Comprehensive 71-page CEFR C2 Curriculum Dataset\n\n")
        f.write("C2_PAGES_DATA = ")
        f.write(pprint.pformat(c2_data, indent=4, width=120))
        f.write("\n")
    print("Successfully wrote c2_curriculum_data.py")
