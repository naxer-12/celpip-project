import pprint
import os

def get_c1_data():
    pages = {}

    # Page 1: Cover
    pages[1] = {
        "page": 1,
        "type": "cover",
        "title": "French Learning Roadmap & Checklist",
        "subtitle": "French C1",
        "badge_num": "",
        "intro": ""
    }

    # Page 2: Overall Objectives of C1 Level (Autonomous / Effective Operational Proficiency)
    pages[2] = {
        "page": 2,
        "type": "objectives",
        "title": "Overall Objectives of C1 Level (Autonomous User / Effective Operational Proficiency)",
        "subtitle": "Speaking & Listening Rigor for Complex Academic & Professional Scenarios",
        "badge_num": "1",
        "intro": "Welcome to French C1! At this advanced stage, you become an autonomous speaker. You can express yourself fluently and spontaneously without searching for words, conduct structured oral presentations, engage in formal academic debate, and understand implicit cultural meanings.",
        "sections": [
            {
                "title": "Speak (Spoken Production & Spoken Interaction)",
                "items": [
                    "Deliver a clear, well-structured 10-to-15 minute oral presentation (exposé) defending an argumentative thesis on complex societal topics.",
                    "Engage in rigorous debate with a native-speaking panel, countering counterarguments with poise, precision, and logical rigor.",
                    "Vary your language dynamically across registers: from elevated academic discourse to idiomatic and colloquial exchanges.",
                    "Qualify your assertions with subtle epistemic modality: expressing concession, doubt, hypothetical nuance, and understated irony."
                ]
            },
            {
                "title": "Listen (Listening Comprehension)",
                "items": [
                    "Follow extended university lectures, specialized technical seminars, and complex panel discussions with ease.",
                    "Understand fast, natural spoken French across various regional and international Francophone accents (France, Canada, Belgium, Switzerland, West Africa).",
                    "Grasp implicit meanings, satirical undercurrents, subtle humor, and rhetorical strategies employed in native media (France Culture, RFI)."
                ]
            }
        ]
    }

    # Page 3: Overall Objectives of C1 Level (Continued)
    pages[3] = {
        "page": 3,
        "type": "objectives",
        "title": "Overall Objectives of C1 Level (Continued)",
        "subtitle": "Reading & Writing Skills for Document Synthesis & Critical Argumentation",
        "badge_num": "2",
        "intro": "At C1, your written production and reading comprehension reach full academic independence. You can master the strict methodology of the DALF C1 document synthesis (synthèse de documents) and write sophisticated 250+ word argumentative essays.",
        "sections": [
            {
                "title": "Write (Written Production & Academic Synthesis)",
                "items": [
                    "Write a flawless, objective document synthesis (synthèse de documents, ~220 words) combining multiple source texts without personal bias or external input.",
                    "Compose structured argumentative essays and opinion pieces (essai argumenté, ~250 words) with clear problem statements, dialectical plans, and persuasive rhetoric.",
                    "Demonstrate high stylistic mastery: varied sentence lengths, absolute subject inversions, nominalization, and formal rhetorical connectors.",
                    "Maintain zero tolerance for basic agreement or conjugation errors, using advanced past participles and subjunctive mood effortlessly."
                ]
            },
            {
                "title": "Read (Reading Comprehension & Critical Analysis)",
                "items": [
                    "Read and critically analyze complex non-fiction essays, intellectual press editorials (Le Monde, Courrier International), and literary texts.",
                    "Identify hidden intentions, ideological assumptions, metaphorical language, and satirical tones in multifaceted documents.",
                    "Synthesize contradictory viewpoints from multiple texts rapidly through targeted skimming and scanning."
                ]
            }
        ]
    }

    # Page 4: Real-Life Outcomes & Core Themes (Themes 1–3)
    pages[4] = {
        "page": 4,
        "type": "outcomes",
        "title": "C1 French – Real-Life Outcomes & Core Themes (Themes 1–3)",
        "subtitle": "Philosophy & Ethics, International Geopolitics, and Environmental Crisis",
        "badge_num": "3",
        "intro": "At CEFR C1, you tackle high-level intellectual domains. Here are the first three core thematic arenas and real-world milestones expected of an autonomous speaker.",
        "table_headers": ["Theme", "Core Knowledge & Lexical Scope", "Real-Life C1 Spoken & Written Outcomes"],
        "table_rows": [
            ["1. Philosophy & Ethics", "Epistemology, bioethics, moral dilemmas, existential philosophy, human rights", "➤ Defend an ethical stance on genetic editing in a public university debate\n➤ Formulate a rigorous problem statement on utilitarianism vs deontology"],
            ["2. Geopolitics & Diplomacy", "Multilateral institutions, sovereignty, international law, treaties, diplomacy", "➤ Analyze the consequences of economic sanctions on regional stability\n➤ Draft a diplomatic policy briefing synthesizing opposing sovereign interests"],
            ["3. Ecology & Climate Crisis", "Ecological transition, carbon neutrality, biodiversity loss, circular economy", "➤ Present a cost-benefit critique of geoengineering versus conservation\n➤ Evaluate environmental policy whitepapers and identify scientific discrepancies"]
        ],
        "footer_title": "Real-Life C1 Milestones (Themes 1–3)",
        "footer_items": [
            "Participate smoothly in round-table academic conferences without prior script preparation.",
            "Synthesize divergent geopolitical viewpoints into a neutral, cohesive executive summary.",
            "Command an active lexicon of over 6,000 words covering specialized academic terminology."
        ]
    }

    # Page 5: Core Themes & Topics (Themes 4–7)
    pages[5] = {
        "page": 5,
        "type": "outcomes",
        "title": "C1 French – Core Themes & Topics (Themes 4–7)",
        "subtitle": "Artificial Intelligence, Macroeconomics, Contemporary Arts & Justice",
        "badge_num": "4",
        "intro": "Themes 4 through 7 explore technical, economic, and institutional domains. You must handle both specialized vocabulary and nuanced dialectical debate.",
        "table_headers": ["Theme", "Core Knowledge & Lexical Scope", "Real-Life C1 Spoken & Written Outcomes"],
        "table_rows": [
            ["4. AI & Digital Technologies", "Algorithms, automation, transhumanism, data privacy, surveillance capitalism", "➤ Critique the ethical boundaries of generative artificial intelligence in education\n➤ Write a press opinion editorial on digital sovereignty and algorithm bias"],
            ["5. Macroeconomics & Labor", "Inflation, monetary policy, labor precarity, globalization, universal basic income", "➤ Debate the merits of degrowth economic models against green growth\n➤ Interpret corporate financial audits and macroeconomic trend reports in French"],
            ["6. Arts & Aesthetics", "Art history, literary theory, cinema critique, cultural heritage, architecture", "➤ Critique an exhibition or film using sophisticated aesthetic and cultural terminology\n➤ Defend the public funding of avant-garde arts against pragmatic budgetary cuts"],
            ["7. Justice & Society", "Constitutional rights, penal reform, systemic inequality, social mobility", "➤ Formulate an argument on restorative justice vs retributive punishment\n➤ Draft a legal commentary examining the scope of civil liberties in digital spaces"]
        ],
        "footer_title": "Real-Life C1 Milestones (Themes 4–7)",
        "footer_items": [
            "Switch seamlessly between technical economic jargon and general public-facing communication.",
            "Write persuasive articles suitable for publication in prominent French cultural periodicals.",
            "Formulate subtle rhetorical questions that stimulate deep audience reflection during debates."
        ]
    }

    # Page 6: Core Themes & Topics (Themes 8–10)
    pages[6] = {
        "page": 6,
        "type": "outcomes",
        "title": "C1 French – Core Themes & Topics (Themes 8–10)",
        "subtitle": "Media Ethics, Cognitive Sciences & Sustainable Urban Sociology",
        "badge_num": "5",
        "intro": "The final thematic modules examine modern information ecosystems, cognitive psychology, and the future of human urban habitats.",
        "table_headers": ["Theme", "Core Knowledge & Lexical Scope", "Real-Life C1 Spoken & Written Outcomes"],
        "table_rows": [
            ["8. Media & Post-Truth", "Disinformation, echo chambers, press freedom, investigative journalism, algorithmic curation", "➤ Deconstruct media propaganda strategies and identify fallacious reasoning\n➤ Produce a 3-minute oral critique of algorithmic echo chambers and public trust"],
            ["9. Cognitive Sciences & Education", "Neuroscience, neurodiversity, pedagogical methods, attention economy, mental health", "➤ Discuss the cognitive impact of smartphone overuse on child development\n➤ Synthesize research articles on alternative pedagogical models (Montessori, Freinet)"],
            ["10. Urbanism & Habitat", "Smart cities, gentrification, rural revitalization, public transit, social housing", "➤ Present an architectural proposal for sustainable, carbon-neutral social housing\n➤ Debate urban mobility policies: pedestrianization vs suburban vehicular access"]
        ],
        "footer_title": "Real-Life C1 Milestones (Themes 8–10)",
        "footer_items": [
            "Demonstrate total intellectual flexibility across cross-disciplinary subject matters.",
            "Express fine distinctions of degree, probability, and personal conviction without ambiguity.",
            "Build an active vocabulary approaching 7,500 words with idiomatic and stylistic panache."
        ]
    }

    # Page 7: Core Communicative Functions
    pages[7] = {
        "page": 7,
        "type": "functions",
        "title": "C1 French – Advanced Communicative Functions",
        "subtitle": "Dialectical Refutation, Concessive Nuance, Epistemic Modality & Irony",
        "badge_num": "6",
        "intro": "At C1, communication is defined by how subtly and convincingly you navigate disagreement, express nuance, and structure intellectual discourse.",
        "table_headers": ["Communicative Function", "Advanced Formulae & Idiomatic Structures", "Context & Rhetorical Intent"],
        "table_rows": [
            ["Conceding with Nuance", "Certes... il n'en demeure pas moins que / Tout en admettant que... je maintiens que", "Validate the opponent's observation while preserving your core counter-thesis."],
            ["Dialectical Pivot & Refutation", "Loin de corroborer cette thèse, force est de constater que / Cet argument pèche par...", "Dismantle fallacious reasoning and shift the argument toward a stronger foundation."],
            ["Epistemic Modality (Degrees of Certainty)", "Il est hautement plausible que / D'aucuns soutiendraient que / Il est à craindre que", "Express precise probability, speculative hypotheses, and intellectual humility."],
            ["Understated Irony & Litotes", "Ce n'est point un vain mot / Il est pour le moins paradoxal de prétendre que...", "Highlight contradictions subtly without resorting to aggressive or abrasive language."],
            ["Oratorical Structuring & Synthesis", "Au regard de ce qui précède / À l'aune de ces considérations / En définitive", "Conclude complex presentations with authority, summarizing disparate strands of thought."]
        ],
        "footer_title": "Spoken & Written Communicative Targets",
        "footer_items": [
            "Never sound blunt or dogmatic; frame assertions with academic poise and objective evidence.",
            "Maintain complete control over emotional temperature during heated intellectual disagreements.",
            "Use rhetorical figures such as litotes and rhetorical questions to engage the listener's intellect."
        ]
    }

    # Pages 8-19: Grammar Mastery (12 pages)
    grammar_topics = [
        (8, "C1 Grammar: Le Subjonctif Imparfait & Plus-que-Parfait",
         "Recognition, Stylistic Register, and Classical Literary Usage",
         "While rarely spoken in daily life, mastering the imperfect and pluperfect subjunctive is indispensable for understanding classical literature, legal texts, and elevated French journalism.",
         [
             ("Morphology of Subjonctif Imparfait", [
                 "Derived from the passé simple stem: que je parlasse, qu'il parlât, que nous parlassions.",
                 "Irregular stems: être (que je fusse), avoir (que j'eusse), faire (que je fisse), venir (que je vinsse).",
                 "Note the circumflex on the 3rd person singular: qu'il allât, qu'il sût, qu'il vînt, qu'il pût."
             ]),
             ("Concordance des Temps & Stylistic Effect", [
                 "Used when the main clause is in a past tense: 'Il fallait qu'il partît sur-le-champ.'",
                 "Subjonctif plus-que-parfait expresses unfulfilled past condition: 'Bien qu'il eût terminé...'",
                 "Imparts immense gravity, historical depth, and elegance to formal written prose."
             ]),
             ("Modern Equivalents & Passive Recognition", [
                 "In standard contemporary French, the present subjunctive usually replaces the imperfect subjunctive.",
                 "At C1, you must recognize these forms instantly when reading essays, decrees, and literature.",
                 "Active mastery of the 3rd person singular ('qu'il pût', 'qu'il voulût') is expected in elevated DALF C1 writing."
             ])
         ]),
        (9, "C1 Grammar: Le Conditionnel Passé (2ème Forme)",
         "Advanced Counterfactuals & Elevated Hypothetical Constructions",
         "The second form of the past conditional is identical in morphology to the pluperfect subjunctive, offering a prestigious literary register for hypothetical regrets and past impossibilities.",
         [
             ("Morphology & Identity", [
                 "Formed with the imperfect subjunctive of être/avoir + past participle: 'J'eusse aimé', 'Il fût parti'.",
                 "Identical to the subjonctif plus-que-parfait, functioning as a high-register counterfactual.",
                 "Example: 'Eût-il su la vérité, il eût agi différemment' (Had he known the truth, he would have acted differently)."
             ]),
             ("Inversion of Auxiliary Without 'Si'", [
                 "Allows replacing 'Si j'avais su' with the elegant inversion: 'Eussé-je connu vos intentions...'",
                 "Eliminates the repetitive use of 'si' in sophisticated argumentative writing.",
                 "Example: 'Fût-ce au péril de sa vie, il n'eût jamais trahi ses idéaux.'"
             ]),
             ("Practical Stylistic Application", [
                 "Used in critical editorials to express poignant historical counterfactuals ('Without this error, France would have...').",
                 "Enriches the candidate's stylistic score on the DALF C1 essay by demonstrating classical depth."
             ])
         ]),
        (10, "C1 Grammar: L'Inversion du Sujet Avancée",
         "Complex Inversion, Absolute Inversion & Inversion After Initial Adverbs",
         "Inversion is not merely a question marker in French; at C1, it is a primary device for modulating rhythm, emphasis, and oratorical weight.",
         [
             ("Inversion After Initial Limiting Adverbs", [
                 "Compulsory or highly expected after: À peine, Peut-être, Sans doute, Aussi, Encore, Vainement, Rarement.",
                 "À peine était-il entré que la sonnerie retentit (Hardly had he entered when...).",
                 "Peut-être conviendrait-il de reconsidérer ces postulats (Perhaps it would be fitting to reconsider...).",
                 "Aussi devons-nous tirer les enseignements de cette crise (Therefore we must draw lessons...)."
             ]),
             ("Inversion Complexe (Noun Subject + Resumptive Pronoun)", [
                 "Le gouvernement s'est-il montré à la hauteur des enjeux ? (Has the government risen to the stakes?)",
                 "Ces mesures sont-elles réellement applicables ? Used to establish rhetorical resonance.",
                 "Gives the sentence an elevated, balanced rhythm suited to formal speeches."
             ]),
             ("Absolute Inversion in Relative & Comparative Clauses", [
                 "...comme l'atteste le rapport publié hier (as the report published yesterday attests).",
                 "...ainsi que le prévoyait la directive européenne (as the European directive foresaw).",
                 "Places the longer, heavier subject at the end of the sentence (law of increasing constituents)."
             ])
         ]),
        (11, "C1 Grammar: La Nominalisation Complexe & Restructuration",
         "Condensing Complex Clauses into Elegant Syntactic Noun Phrases",
         "Academic and journalistic French heavily prefers noun-centric structures over strings of subordinate verb clauses. Nominalization enhances density, authority, and concision.",
         [
             ("Transforming Verbal Propositions into Noun Phrases", [
                 "Verb clause: 'Parce que le climat se dérègle rapidement, les gouvernements doivent agir.'",
                 "Nominalized: 'Le dérèglement accéléré du climat impose une action gouvernementale immédiate.'",
                 "Eliminates clumsy connectors like 'parce que' and elevates the register to executive prose."
             ]),
             ("Suffixation & Semantic Precision", [
                 "Master suffix patterns: -ment (effondrement), -tion/-ation (prolifération), -ence (émergence).",
                 "Distinguish subtle nuances: 'recouvrement' (recovery of taxes) vs 'recouvrance' (regaining health).",
                 "Use abstract nominalizations to conceptualize arguments: 'l'inadéquation', 'l'obsolescence'."
             ]),
             ("Syntactic Balance & Avoiding Nominal Heaviness", [
                 "Avoid stacking more than two prepositional phrases ('de... de... de...').",
                 "Pair nominal subjects with dynamic, precise verbs: 'entraîner', 'susciter', 'corroborer', 'endiguer'.",
                 "Crucial for the DALF C1 document synthesis where word economy is strictly enforced."
             ])
         ]),
        (12, "C1 Grammar: Participe Présent, Adjectif Verbal & Gérondif",
         "Advanced Participial Clauses and Syntactic Subordination",
         "Participial constructions replace relative clauses and causal conjunctions, creating smooth transitions and rhythm in written French.",
         [
             ("Participe Présent vs Adjectif Verbal (Orthographic Distinctions)", [
                 "Participe présent is invariable (ending in -ant) and expresses an action: 'négligeant les consignes'.",
                 "Adjectif verbal agrees in gender/number and denotes a state: 'une attitude négligente'.",
                 "Crucial spelling differences: différant (participle) vs différent (adj); convainquant vs convaincant."
             ]),
             ("Participial Clauses (Propositions Participiales)", [
                 "Replaces causal or temporal subordinates when subjects differ: 'La séance étant levée, les délégués partirent.'",
                 "Replaces relative clauses: 'Les candidats remplissant les critères...' (= qui remplissent).",
                 "Creates swift, economical sentence flow typical of institutional whitepapers."
             ]),
             ("Advanced Gérondif (En + Participe Présent)", [
                 "Expresses simultaneous cause, manner, or condition: 'En régulant ce marché, l'État préviendra les crises.'",
                 "With 'tout', expresses concessive opposition: 'Tout en reconnaissant les progrès, il déplore les retards.'"
             ])
         ]),
        (13, "C1 Grammar: Les Systèmes Concessifs Poussés",
         "Advanced Formulations of Concession, Opposition & Paradox",
         "Simple 'bien que' is basic. At C1, you master a comprehensive palette of nuanced concessive structures to construct intricate arguments.",
         [
             ("Concessive Subjunctive Structures", [
                 "Quoique + subjonctif: 'Quoiqu'il soit contesté, ce traité demeure valide.'",
                 "Quel que + subjonctif: 'Quels que soient les obstacles, nous persévérerons.'",
                 "Si + adj + que + subjonctif: 'Si brillante que soit cette théorie, elle manque de preuves.'",
                 "Tout + adj + que + indicatif/subjonctif: 'Tout érudit qu'il est, il commet des bévues.'"
             ]),
             ("Idiomatic Concessive Verbal Turns", [
                 "Avoir beau + infinitif: 'Il a beau multiplier les déclarations, l'opinion reste sceptique.'",
                 "Quand bien même + conditionnel: 'Quand bien même vous auriez raison, la loi l'interdit.'",
                 "Loin de + infinitif: 'Loin d'apaiser les tensions, cette décision a ravivé les conflits.'"
             ]),
             ("Adverbial & Prepositional Concessives", [
                 "En dépit de / Nonobstant (formal): 'Nonobstant les réserves formulées, le projet a été adopté.'",
                 "Il n'en reste pas moins que / Il n'empêche que: Used to pivot after conceding an adversary's point."
             ])
         ]),
        (14, "C1 Grammar: La Cause & la Conséquence Formelles",
         "Nuanced Causality, Negative Cause & Logical Consequence",
         "Moving beyond 'parce que' and 'donc'. At C1, you express subtle shades of causality: justification, fault, pretext, and disproportionate consequence.",
         [
             ("Formal & Specialized Causal Connectors", [
                 "D'autant plus que / D'autant moins que: 'Le projet est risqué, d'autant plus que les financements manquent.'",
                 "Faute de + nom/infinitif (Negative cause): 'Faute de concertation préalable, la grève a éclaté.'",
                 "À force de + nom/infinitif (Accumulated cause): 'À force de tergiverser, l'entreprise a manqué le virage.'",
                 "Sous prétexte que + indicatif (Dubious pretext): 'Sous prétexte qu'il pleuvait, il n'est pas venu.'"
             ]),
             ("Formal Consequence & Proportionality", [
                 "De telle sorte que / De façon que + indicatif (result) ou subjonctif (intent).",
                 "Au point de + infinitif / À tel point que: 'La situation s'est dégradée au point de paralyser la région.'",
                 "Si bien que / Par conséquent / Partant (archaic/legal consequence): 'Il est mineur, partant irresponsable.'"
             ]),
             ("Stylistic Placement & Avoidance of Monotony", [
                 "Place causal phrases at the head of sentences to establish context: 'Eu égard aux circonstances...'",
                 "Use participial causality: 'Craignant des représailles, ils gardèrent le silence.'"
             ])
         ]),
        (15, "C1 Grammar: Les Pronoms Relatifs Composés Complexes",
         "Precision in Spatial, Temporal, and Prepositional Subordination",
         "Compound relative pronouns ensure razor-sharp precision in legal, academic, and technical documents.",
         [
             ("Contracted Forms with Prepositions 'À' and 'De'", [
                 "Auquel, à laquelle, auxquels, auxquelles (with prepositions ending in 'à': grâce auquel, face auquel).",
                 "Duquel, de laquelle, desquels, desquelles (with compound prepositions: près duquel, au terme duquel).",
                 "Never confuse 'dont' (simple complement of 'de') with 'duquel' (governed by a compound preposition)."
             ]),
             ("Distinction: 'Dont' vs 'Duquel'", [
                 "Correct: 'Le problème dont je parle' (parler de -> simple preposition -> dont).",
                 "Correct: 'La crise au cœur de laquelle nous nous trouvons' (au cœur de -> compound preposition -> laquelle).",
                 "Incorrect: 'La table à côté de dont je suis assis' -> 'à côté de laquelle'."
             ]),
             ("Relative Pronouns for Human vs Inanimate Referents", [
                 "After prepositions: prefer 'qui' or 'lequel' for humans ('l'expert auprès de qui / duquel il s'est formé').",
                 "Compulsory 'lequel' for inanimates: 'le dossier sur lequel nous travaillons' (never 'sur qui').",
                 "Pronom relatif indéfini: 'ce à quoi', 'ce en quoi', 'ce dont' ('Voilà ce en quoi réside l'essentiel')."
             ])
         ]),
        (16, "C1 Grammar: Concordance des Temps dans le Discours Rapporté",
         "Complex Indirect Speech, Free Indirect Style & Temporal Backshifting",
         "Mastering temporal concordance when reporting statements, testimonies, and archival documents across multiple layers of past tenses.",
         [
             ("Systematic Backshift After Past Introductory Verbs", [
                 "Direct Présent -> Imparfait: 'Il a affirmé qu'il comprenait la situation.'",
                 "Direct Passé Composé -> Plus-que-Parfait: 'Elle a déclaré qu'elle avait déjà transmis le dossier.'",
                 "Direct Futur Simple -> Conditionnel Présent: 'Ils ont promis qu'ils réviseraient les tarifs.'",
                 "Direct Futur Antérieur -> Conditionnel Passé: 'Il assura qu'il aurait terminé avant midi.'"
             ]),
             ("Modifications of Temporal & Spatial Deictics", [
                 "Aujourd'hui -> Ce jour-là; Demain -> Le lendemain; Hier -> La veille.",
                 "La semaine prochaine -> La semaine suivante; Il y a deux jours -> Deux jours plus tôt / auparavant.",
                 "Essential for narrative coherence in historical essays and case study reporting."
             ]),
             ("Le Style Indirect Libre (Free Indirect Speech)", [
                 "Retains the character's internal voice and emotional coloring while using past tenses and 3rd person.",
                 "Example: 'Partirait-elle maintenant ? Non, elle devait attendre que l'orage passât.'",
                 "Elevates written expression in narrative analyses and literary commentary."
             ])
         ]),
        (17, "C1 Grammar: Tournures Passives Pronominales & Impersonnelles",
         "Depersonalizing Discourse to Enhance Academic Objectivity",
         "Objective academic writing avoids 'je' and overuse of 'on'. C1 writers use pronominal passives and elevated impersonal constructions.",
         [
             ("Pronominal Passive Construction (La Voix Passive Pronominale)", [
                 "Replaces standard passive when the agent is obvious or irrelevant.",
                 "Example: 'Ces dossiers se traitent en commission' (= sont traités).",
                 "Example: 'L'accord s'est conclu à l'unanimité' (= a été conclu).",
                 "More natural and dynamic in French than repetitive auxiliary passive ('est fait par...')."
             ]),
             ("Elevated Impersonal Structures", [
                 "Il convient de + infinitif: 'Il convient de rappeler les faits.' (It is fitting to recall...).",
                 "Il s'ensuit que + indicatif: 'Il s'ensuit que les prévisions étaient erronées.' (It follows that...).",
                 "Il importe que + subjonctif: 'Il importe que chacun assume ses responsabilités.'",
                 "Il appert que (legal/archaic): 'Il appert que les conditions sont réunies.'"
             ]),
             ("Neutralizing Personal Bias in Critical Synthesis", [
                 "Instead of 'Je pense que...', write: 'Il appert à l'évidence que...' or 'Force est de constater que...'",
                 "Gives statements universal institutional authority."
             ])
         ]),
        (18, "C1 Grammar: Connecteurs Rhétoriques & Articulation Logique",
         "Mastering the Architecture of Elevated Argumentative Thought",
         "Connectors are the skeletal framework of persuasive discourse. C1 speakers command rare, sophisticated connectors to build seamless intellectual transitions.",
         [
             ("Hierarchizing & Enumerating Complex Ideas", [
                 "En premier lieu, en second lieu, en dernier ressort (avoid overusing 'd'abord / ensuite').",
                 "Non seulement... mais encore / qui plus est / d'ailleurs / du reste.",
                 "À cela s'ajoute le fait que... / Sans omettre de mentionner que..."
             ]),
             ("Refining & Rectifying Thought (Reformulation)", [
                 "En d'autres termes / Pour le dire autrement / À proprement parler.",
                 "Ou plutôt / Mieux encore / Plus exactement: 'Un compromis, ou plutôt un faux-semblant.'",
                 "En l'occurrence / En l'espèce (specifically in this case)."
             ]),
             ("Concluding & Synthesizing", [
                 "En somme / Somme toute / En dernière analyse / Tout bien considéré.",
                 "En guise de conclusion / Il appert en définitive que...",
                 "Transforms a disjointed essay into a harmonious, compelling oratorical piece."
             ])
         ]),
        (19, "C1 Grammar: Les Registres de Langue & Stylistique",
         "Navigating Between Soutenu, Académique, Familier and Argot",
         "A true C1 user is not restricted to one tone. You can seamlessly decode street slang while writing impeccably formal academic prose.",
         [
             ("Le Registre Soutenu (Elevated / Literary)", [
                 "Vocabulary: 'subodorer' (pressentir), 'morose' (triste), 'péremptoire' (catégorique).",
                 "Syntax: inversion, subjunctive imperfect, avoidance of abbreviations.",
                 "Used in legal pleadings, academic journals, formal state diplomacy."
             ]),
             ("Le Registre Académique / Journalistique", [
                 "Clear, objective, nominalized, conceptually precise, neutral tone.",
                 "Used in Le Monde, Les Échos, university dissertations, DALF C1 examination."
             ]),
             ("Le Registre Familier & Argotique (Passive Decoding & Natural Slang)", [
                 "Verlan: 'zarbi' (bizarre), 'relou' (lourd), 'ouf' (fou), 'laisse béton' (laisse tomber).",
                 "Colloquial apocopes: 'le prof', 'la manif', 'la télé', 'la fac', 'un appart'.",
                 "You know when it is appropriate to use them and when they must be strictly avoided."
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
        (20, "C1 Thematic Vocabulary: Philosophie, Pensée Critique & Éthique",
         "Epistemological Concepts, Moral Philosophy & Dialectical Inquiry",
         "Master 12 essential high-level philosophical terms to debate ethics, human nature, and intellectual inquiry.",
         [
             ("L'Épistémologie", "f.", "Theory of knowledge and scientific validity", "L'épistémologie contemporaine questionne l'objectivité des algorithmes."),
             ("La Déontologie", "f.", "Ethical code governing professional duties", "Le respect de la déontologie médicale interdit tout conflit d'intérêts."),
             ("Le Manichéisme", "m.", "Binary, black-and-white worldview", "Il faut dépasser ce manichéisme réducteur pour saisir la complexité du problème."),
             ("La Contingence", "f.", "Quality of what might happen or not; uncertainty", "L'histoire humaine est marquée par la contingence des événements."),
             ("L'Aporie", "f.", "Logical impasse or unsolvable philosophical puzzle", "Cette contradiction philosophique conduit à une véritable aporie."),
             ("L'Herméneutique", "f.", "Art and theory of textual interpretation", "L'herméneutique des textes sacrés exige une rigueur philologique absolue."),
             ("Intrinsèque", "adj.", "Inherent, belonging naturally to something", "La liberté de penser possède une valeur éthique intrinsèque."),
             ("L'Altérité", "f.", "State of being other, recognition of difference", "La découverte de l'altérité est au cœur de l'expérience interculturelle."),
             ("Corroborer", "v.", "To confirm, substantiate with evidence", "Les nouvelles données archéologiques viennent corroborer cette hypothèse."),
             ("Infirmer", "v.", "To invalidate, disprove a theory", "Cette découverte inattendue vient infirmer les modèles théoriques antérieurs."),
             ("Le Postulat", "m.", "Foundational premise taken for granted", "Le postulat de départ repose sur l'égalité fondamentale des citoyens."),
             ("La Doxa", "f.", "Popular, unquestioned public opinion", "Le rôle de l'intellectuel est de bousculer la doxa établie.")
         ]),
        (21, "C1 Thematic Vocabulary: Géopolitique & Relations Internationales",
         "Sovereignty, Multilateralism, Diplomacy & Strategic Conflicts",
         "Analyze international power balances, trade treaties, and geopolitical stability with sovereign precision.",
         [
             ("La Souveraineté", "f.", "Supreme authority of a state over its territory", "Les négociations touchent au cœur de la souveraineté nationale."),
             ("L'Hégémonie", "f.", "Dominance of one state or group over others", "L'hégémonie économique américaine est désormais contestée par des puissances émergentes."),
             ("Le Multilatéralisme", "m.", "Cooperation among multiple nations toward shared goals", "Le multilatéralisme constitue le seul rempart contre l'unilatéralisme belliqueux."),
             ("L'Ingérence", "f.", "Unlawful interference in another nation's affairs", "L'ingérence humanitaire suscite d'intenses débats au Conseil de sécurité."),
             ("L'Autarcie", "f.", "Economic self-sufficiency without foreign trade", "Aucune nation moderne ne peut prospérer en vivant en autarcie complète."),
             ("Le Blocus", "m.", "Naval, economic or military blockade", "Le blocus maritime paralyse l'approvisionnement en denrées essentielles."),
             ("La Belligérance", "f.", "State of armed conflict or warfare", "Les deux États sont entrés dans une phase de belligérance ouverte."),
             ("L'Accréditation", "f.", "Official diplomatic recognition of an ambassador", "L'ambassadeur a présenté ses lettres d'accréditation au chef de l'État."),
             ("Le Contentieux", "m.", "Ongoing legal dispute or diplomatic grievance", "Ce contentieux frontalier empoisonne les relations bilatérales depuis des décennies."),
             ("Pérenne", "adj.", "Lasting, enduring across generations", "Les traités de paix doivent garantir une stabilité régionale pérenne."),
             ("Ratifier", "v.", "To officially approve and sign a treaty", "Le parlement a enfin ratifié l'accord de coopération environnementale."),
             ("L'Exaction", "f.", "Act of extortion, violence, or abuse of power", "Les observateurs de l'ONU ont dénoncé les exactions commises contre les civils.")
         ]),
        (22, "C1 Thematic Vocabulary: Transition Écologique & Climat",
         "Carbon Neutrality, Biodiversity, Planetary Boundaries & Eco-Transition",
         "Command the technical and political terminology governing the ecological revolution and planetary crises.",
         [
             ("L'Anthropocène", "m.", "Geological epoch dominated by human activity", "L'Anthropocène se caractérise par une modification irréversible de la biosphère."),
             ("La Résilience", "f.", "Capacity of ecosystems to absorb shocks and recover", "La résilience des forêts boréales face aux mégafeux est aujourd'hui compromise."),
             ("La Sobriété", "f.", "Voluntary moderation in energy and resource use", "La sobriété énergétique ne relève pas de la pénurie, mais d'un choix éthique."),
             ("L'Écocide", "m.", "Massive destruction of ecosystems by human action", "Plusieurs juristes militent pour faire reconnaître l'écocide par la Cour pénale."),
             ("Le Dérèglement", "m.", "Systemic disturbance or breakdown of climate norms", "Le dérèglement climatique amplifie la fréquence des sécheresses sévères."),
             ("L'Obsolescence", "f.", "Process of becoming outdated or unusable", "L'obsolescence programmée des appareils électroniques génère des tonnes de déchets."),
             ("La Biodiversité", "f.", "Variety of biological life on Earth", "L'érosion dramatique de la biodiversité menace les chaînes trophiques."),
             ("Péricliter", "v.", "To decline rapidly, deteriorate toward ruin", "Sans aides ciblées, les écosystèmes côtiers risquent de péricliter."),
             ("L'Agroécologie", "f.", "Farming practices based on ecological principles", "L'agroécologie permet de restaurer la fertilité des sols sans intrants chimiques."),
             ("La Finitude", "f.", "Finite, limited nature of resources or life", "La prise de conscience de la finitude de notre planète s'impose désormais à tous."),
             ("Endiguer", "v.", "To stem, contain, or halt a destructive trend", "Il devient impératif d'endiguer la prolifération des microplastiques marins."),
             ("L'Empreinte", "f.", "Footprint, ecological mark left by activity", "Réduire son empreinte carbone exige une transformation des modes de transport.")
         ]),
        (23, "C1 Thematic Vocabulary: Intelligence Artificielle & Sciences",
         "Algorithms, Bio-Technologies, Machine Learning & Transhumanism",
         "Analyze the societal disruption of machine learning, quantum computing, and bio-technological breakthroughs.",
         [
             ("L'Algorithme", "m.", "Step-by-step computational procedure", "Les algorithmes de recommandation enferment les usagers dans des bulles cognitives."),
             ("Le Transhumanisme", "m.", "Movement advocating technological enhancement of humans", "Le transhumanisme promet l'éradication de la sénescence grâce aux biotechnologies."),
             ("L'Intelligibilité", "f.", "Clarity, capability of being understood by reason", "L'intelligibilité des réseaux de neurones profonds reste un défi pour la recherche."),
             ("La Disruption", "f.", "Radical technological shakeup of an established market", "Cette innovation de rupture provoque une disruption majeure dans le secteur médical."),
             ("La Falsifiabilité", "f.", "Popperian criterion of scientific testability", "Une théorie scientifique doit obligatoirement répondre au critère de falsifiabilité."),
             ("Le Biais", "m.", "Systematic distortion, prejudice in data", "Les biais algorithmiques reproduisent et accentuent les discriminations existantes."),
             ("L'Apprentissage", "m.", "Machine learning (apprentissage automatique)", "L'apprentissage supervisé nécessite d'immenses bases de données annotées."),
             ("L'Automatisation", "f.", "Replacement of human labor by machinery", "L'automatisation robotique des entrepôts redéfinit les compétences logistiques."),
             ("Subvertir", "v.", "To undermine, overthrow established rules", "Les outils génératifs subvertissent les méthodes traditionnelles d'évaluation."),
             ("La Singularity", "f.", "Technological singularity; theoretical event", "Certains futurologues redoutent l'avènement d'une singularité technologique incontrôlable."),
             ("Empirique", "adj.", "Based on observation rather than pure theory", "Cette conclusion repose sur des observations empiriques rigoureusement documentées."),
             ("L'Éthique", "f.", "Moral philosophy governing research and tech", "L'éthique de la recherche biomédicale encadre strictement le clonage thérapeutique.")
         ]),
        (24, "C1 Thematic Vocabulary: Économie Mondiale & Marché du Travail",
         "Macroeconomics, Monetary Policy, Labor Precarity & Globalization",
         "Critique financial models, central bank decisions, and structural transformations in the labor force.",
         [
             ("La Stagflation", "f.", "Simultaneous inflation and stagnant economic output", "La banque centrale redoute un retour de la stagflation des années soixante-dix."),
             ("La Précarité", "f.", "Insecurity, vulnerability of job or living conditions", "La précarité des travailleurs indépendants soulève d'urgentes questions sociales."),
             ("L'Austérité", "f.", "Fiscal policy curbing public spending", "Les politiques d'austérité budgétaire ont affaibli les services hospitaliers."),
             ("L'Ubérisation", "f.", "Platform-based gig economy bypassing traditional contracts", "L'ubérisation du secteur des livraisons contourne le droit du travail classique."),
             ("L'Assouplissement", "m.", "Quantitative easing (assouplissement quantitatif)", "L'assouplissement monétaire a soutenu les marchés financiers durant la récession."),
             ("La Conjoncture", "f.", "Current economic situation or climate", "Une conjoncture défavorable incite les ménages à thésauriser leur épargne."),
             ("L'Inadéquation", "f.", "Mismatch between supply and demand", "L'inadéquation entre l'offre et la demande de main-d'œuvre freine l'embauche."),
             ("Juguler", "v.", "To curb, choke off, bring under control", "Les hausses de taux directeurs visent à juguler une inflation galopante."),
             ("Le Revenu", "m.", "Universal basic income (revenu universel)", "L'expérimentation d'un revenu universel d'existence suscite d'ardents débats."),
             ("La Solvabilité", "f.", "Financial solvency, ability to pay debts", "La solvabilité des banques régionales a été confirmée par les tests de résistance."),
             ("Endémique", "adj.", "Pervasive, chronically present in a system", "Le chômage des jeunes demeure un problème endémique dans cette région."),
             ("La Délocalisation", "f.", "Offshoring of manufacturing to lower-cost nations", "La délocalisation des usines a dévitalisé les anciens bassins industriels.")
         ]),
        (25, "C1 Thematic Vocabulary: Arts, Culture & Philosophie Esthétique",
         "Art Theory, Hermeneutics, Literary Tropes & Cultural Heritage",
         "Engage with high cultural criticism, museology, cinematic aesthetics, and intellectual heritage.",
         [
             ("L'Esthétique", "f.", "Philosophy of art, beauty, and taste", "L'esthétique minimaliste de cette mise en scène souligne l'angoisse des protagonistes."),
             ("Le Canon", "m.", "Authoritative, accepted standard or collection", "L'élargissement du canon littéraire permet de redécouvrir des voix féminines oubliées."),
             ("La Dépouillement", "m.", "Austere simplicity, artistic purity", "Le dépouillement de la scénographie renforce l'intensité dramatique du texte."),
             ("La Catharsis", "f.", "Emotional purification through theatrical art", "La tragédie classique grecque opère une catharsis libératrice chez le spectateur."),
             ("L'Éclectisme", "m.", "Deriving ideas or styles from broad sources", "L'éclectisme de sa production architecturale mêle éléments baroques et béton brut."),
             ("La Postérité", "f.", "Future generations, enduring cultural memory", "Ce chef-d'œuvre méconnu de son vivant n'a rencontré la gloire qu'à la postérité."),
             ("Iconoclaste", "adj./m.", "Challenging cherished beliefs and revered symbols", "Son interprétation iconoclaste de Molière a provoqué la polémique au festival."),
             ("L'Éphémère", "m./adj.", "Transitory, fleeting nature of contemporary art", "Le street art tire sa force subversive de son caractère foncièrement éphémère."),
             ("Exacerber", "v.", "To aggravate, heighten intensity of feelings", "L'éclairage en clair-obscur vient exacerber la tension dramatique du tableau."),
             ("Le Pastiche", "m.", "Artistic work imitating the style of another", "Ce roman n'est pas un plagiat, mais un pastiche virtuose de Proust."),
             ("La Filiation", "f.", "Lineage, conceptual heritage linking creators", "On reconnaît dans cette œuvre la filiation directe avec le surréalisme français."),
             ("Sublimer", "v.", "To elevate to a higher spiritual or aesthetic level", "L'artiste parvient à sublimer la douleur du deuil à travers la danse.")
         ]),
        (26, "C1 Thematic Vocabulary: Justice, Droits Humains & Société",
         "Constitutional Rights, Penal Reform, Jurisprudence & Equity",
         "Master the vocabulary of jurisprudence, civic liberties, systemic discrimination, and penal reform.",
         [
             ("La Jurisprudence", "f.", "Case law, legal principles established by court rulings", "Cet arrêt du Conseil d'État marque un revirement historique de la jurisprudence."),
             ("L'Inviolabilité", "f.", "Sacred, untouchable constitutional protection", "L'inviolabilité du domicile privé constitue une garantie constitutionnelle majeure."),
             ("La Récidive", "f.", "Repeat offending, relapse into criminal behavior", "Les magistrats privilégient un accompagnement socio-éducatif pour prévenir la récidive."),
             ("L'Équité", "f.", "Fairness and justice beyond rigid statutory law", "Le juge a tranché en équité pour protéger la partie la plus vulnérable."),
             ("La Prescription", "f.", "Statute of limitations extinguishing legal action", "Le délai de prescription pour les crimes contre l'humanité est juridiquement imprescriptible."),
             ("Le Réquisitoire", "m.", "Formal closing indictment by the prosecutor", "Le procureur a prononcé un réquisitoire implacable réclamant une peine exemplaire."),
             ("L'Acquittement", "m.", "Official verdict clearing an accused person", "L'insuffisance criante de preuves matérielles a conduit à un acquittement sans appel."),
             ("L'Impunité", "f.", "Exemption from punishment or loss", "Mettre fin à l'impunité des crimes de guerre est la mission première de la CPI."),
             ("Bafouer", "v.", "To flout, trample on laws, rights, or dignity", "Ce décret bafoue ouvertement les libertés fondamentales garanties par la Charte."),
             ("Disproportionné", "adj.", "Out of proportion, excessively severe", "L'usage de la force policière a été jugé disproportionné par le Défenseur des droits."),
             ("Le Recours", "m.", "Legal appeal, petition to a higher judicial body", "Les avocats ont déposé un recours suspensif devant la Cour européenne."),
             ("La Rétorsion", "f.", "Retaliation, countermeasures against a breach", "L'État a adopté des mesures de rétorsion douanière pour défendre ses entreprises.")
         ]),
        (27, "C1 Thematic Vocabulary: Médias, Post-Vérité & Information",
         "Journalistic Ethics, Misinformation, Propaganda & Digital Ecology",
         "Deconstruct the mechanisms of information warfare, digital virality, and independent press accountability.",
         [
             ("La Déontologie", "f.", "Journalistic ethics and professional code of conduct", "La charte de déontologie interdit la publication d'informations non recoupées."),
             ("L'Infobésité", "f.", "Information overload caused by digital media", "L'infobésité permanente altère notre capacité d'attention et de jugement critique."),
             ("La Désinformation", "f.", "Deliberate spreading of false information", "Cette campagne de désinformation orchestrée cherche à déstabiliser le processus électoral."),
             ("La Propagande", "f.", "Biased information used to promote an ideology", "Le régime use d'une propagande omniprésente pour museler toute opposition démocratique."),
             ("Le Recoupement", "m.", "Cross-checking facts across diverse independent sources", "Le recoupement rigoureux des témoignages a permis de révéler le scandale financier."),
             ("La Facture", "f.", "Style or build (journalistic construction)", "Cet article d'investigation est d'une facture remarquable par son équilibre."),
             ("L'Écueil", "m.", "Pitfall, hidden danger threatening a process", "L'écueil majeur du journalisme de flux réside dans la précipitation sensationnaliste."),
             ("Relayer", "v.", "To pass on, broadcast, amplify news", "Les réseaux sociaux relaient des rumeurs infondées à une vitesse fulgurante."),
             ("Tendancieux", "adj.", "Biased, slanted to serve a particular narrative", "Ce reportage télévisé a été critiqué pour son cadrage tendancieux et partial."),
             ("L'Omerta", "f.", "Code of silence, systemic conspiracy of secrecy", "Les lanceurs d'alerte ont bravé l'omerta qui régnait au sein de l'institution."),
             ("Démystifier", "v.", "To debunk, strip illusions from a false belief", "Le travail des fact-checkers vise à démystifier les théories conspirationnistes."),
             ("La Pluralité", "f.", "Diversity of independent viewpoints in press", "La pluralité de la presse est la condition sine qua non d'un débat démocratique sain.")
         ]),
        (28, "C1 Thematic Vocabulary: Sciences Cognitives & Éducation",
         "Neuroscience, Learning Theories, Attention Economy & Pedagogy",
         "Analyze the science of human cognition, memory consolidation, and radical pedagogical innovation.",
         [
             ("La Plasticité", "f.", "Neuroplasticity; brain's capacity to reorganize", "La plasticité cérébrale démontre que l'apprentissage reste possible à tout âge."),
             ("La Métacognition", "f.", "Awareness and understanding of one's own thought processes", "Développer la métacognition chez l'élève favorise une autonomie d'apprentissage durable."),
             ("L'Attrition", "f.", "Gradual loss, erosion of cognitive capacity", "L'attrition de la mémoire de travail résulte souvent d'une surcharge cognitive prolongée."),
             ("L'Attention", "f.", "Attention economy (l'économie de l'attention)", "L'économie de l'attention monétise le temps de cerveau disponible au détriment de l'étude."),
             ("L'Assimilation", "f.", "Cognitive integration of new concepts", "L'assimilation durable d'une langue étrangère exige des réactivations espacées."),
             ("Le Tuteur", "m.", "Scaffolding, mentoring framework in pedagogy", "L'enseignant agit comme un tuteur bienveillant guidant la réflexion de l'apprenant."),
             ("Empirique", "adj.", "Demonstrated by experimentation and observation", "Les bénéfices du sommeil sur la mémorisation sont prouvés par des données empiriques."),
             ("L'Empathie", "f.", "Ability to understand and share others' feelings", "L'empathie cognitive joue un rôle primordial dans la médiation pédagogique."),
             ("Stimuler", "v.", "To encourage, invigorate cognitive functions", "La lecture quotidienne de textes exigeants stimule l'imagination conceptuelle."),
             ("L'Inhibition", "f.", "Cognitive inhibition; filtering out distractors", "L'inhibition des automatismes permet de surmonter les erreurs de raisonnement intuitif."),
             ("Holistique", "adj.", "Holistic; considering the whole person/system", "Une approche holistique de l'éducation prend en compte le bien-être physique et émotionnel."),
             ("La Mnémotechnique", "f.", "Techniques aiding memory retention", "Les procédés mnémotechniques facilitent la mémorisation des déclinaisons complexes.")
         ]),
        (29, "C1 Thematic Vocabulary: Urbanisme & Sociologie Spatiale",
         "Smart Cities, Gentrification, Suburban Dynamics & Territorial Equity",
         "Discuss the design of metropolis habitats, transport networks, and urban spatial justice.",
         [
             ("La Gentrification", "f.", "Inflow of affluent residents transforming working-class areas", "La gentrification des faubourgs repousse les ménages modestes vers les périphéries lointaines."),
             ("La Mixité", "f.", "Social and demographic diversity in neighborhoods", "La loi impose un quota minimal de logements sociaux pour garantir la mixité urbaine."),
             ("L'Étalement", "m.", "Urban sprawl expanding into agricultural lands", "L'étalement urbain dévore des milliers d'hectares de terres arables chaque année."),
             ("La Mobilité", "f.", "Movement of people through public transit", "Le développement des mobilités douces réduit considérablement la pollution sonore."),
             ("L'Enclavement", "m.", "Isolation, lack of transport access of an area", "L'enclavement des cités périurbaines entrave l'accès aux bassins d'emplois."),
             ("La Dévitalisation", "f.", "Loss of economic and cultural vitality in town centers", "La dévitalisation des cœurs de villes moyennes s'accélère avec les centres commerciaux."),
             ("La Résilience", "f.", "Urban capacity to withstand heatwaves and floods", "La résilience urbaine exige de végétaliser massivement les toitures et cours d'écoles."),
             ("Réhabiliter", "v.", "To renovate, restore decaying housing stock", "La municipalité a choisi de réhabiliter les friches industrielles en tiers-lieux culturels."),
             ("Péricliter", "v.", "To wither away, decay through lack of upkeep", "Sans entretien public régulier, le patrimoine architectural finit par péricliter."),
             ("La Végétalisation", "f.", "Greening of urban concrete surfaces", "La végétalisation des façades atténue le phénomène d'îlot de chaleur urbain."),
             ("Ségrégatif", "adj.", "Producing or reinforcing spatial segregation", "Ce plan d'urbanisme a été dénoncé pour son caractère ségrégatif et exclusif."),
             ("Le Tiers-Lieu", "m.", "Community space distinct from home and workplace", "Les tiers-lieux favorisent la coopération locale, le télétravail et l'innovation citoyenne.")
         ])
    ]

    for page_num, title, subtitle, intro, terms in vocab_modules:
        sections = []
        # Group 12 terms into two sets of 6 for balanced page layout
        half = len(terms) // 2
        sections.append({
            "title": "Module Lexical: Concepts Fondamentaux (Partie 1)",
            "items": [
                f"{term} ({pos}): {defn} — Ex: « {ex} »"
                for term, pos, defn, ex in terms[:half]
            ]
        })
        sections.append({
            "title": "Module Lexical: Applications & Nuances (Partie 2)",
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
        (30, "C1 Speaking Mastery: L'Exposé Structuré (DALF C1 Format)",
         "Organizing a 10-to-15 Minute Monologue from Written Dossiers",
         "The DALF C1 oral presentation requires delivering a cohesive monologue based on several conflicting source documents, followed by an in-depth thesis defense.",
         [
             ("Phase 1: Synthesizing the Core Dossier (3-4 mins)", [
                 "Extract the central controversy without summarizing text-by-text.",
                 "Formulate a precise 'problématique' that interrogates the tension between the sources.",
                 "Announce a clear, two- or three-part plan: 'Dans un premier temps... puis... enfin...'"
             ]),
             ("Phase 2: Developing Your Argumentative Position (6-8 mins)", [
                 "Move beyond the dossier: provide fresh historical, cultural, and personal examples.",
                 "Use clear signposting: 'Abordons à présent le second versant de notre analyse...'",
                 "Balance abstract concepts with concrete societal case studies."
             ]),
             ("Phase 3: The Authoritative Conclusion (2 mins)", [
                 "Synthesize your findings without introducing totally new unexamined arguments.",
                 "Provide a thought-provoking opening ('élargissement') to stimulate jury debate."
             ])
         ]),
        (31, "C1 Speaking Mastery: La Problématisation & l'Annonce du Plan",
         "Transforming a General Theme into a Razor-Sharp Intellectual Question",
         "A great C1 presentation lives or dies by its problem statement. Avoid superficial questions like 'Is technology good or bad?' in favor of nuanced dialectical inquiries.",
         [
             ("Formulating a Dialectical Problem Statement", [
                 "Weak: 'Faut-il interdire l'intelligence artificielle dans les universités ?'",
                 "C1 Standard: 'Dans quelle mesure l'intégration des intelligences artificielles redéfinit-elle les frontières entre émancipation intellectuelle et assujettissement cognitif ?'",
                 "Use structures like: 'Dans quelle mesure...', 'En quoi... met-il en péril...', 'Comment concilier... et...'."
             ]),
             ("Elegantly Announcing Your Plan", [
                 "Avoid robotic phrasing like 'Ma première partie sera...'.",
                 "Elevated style: 'Afin d'éclairer cette question, nous examinerons d'abord les vertus démocratiques du dispositif, avant de mesurer les dérives qu'induit son instrumentalisation marchande.'",
                 "Check that the plan directly answers the announced problem statement."
             ]),
             ("Establishing Immediate Intellectual Credibility", [
                 "Open with a striking quotation, historical paradox, or compelling statistical reality.",
                 "Set a measured, confident vocal pace from the very first sentence."
             ])
         ]),
        (32, "C1 Speaking Mastery: La Soutenance Dialectique & Réfutation",
         "Defending Your Thesis with Logic, Evidence & Rhetorical Balance",
         "During the presentation, you must defend a firm viewpoint while recognizing legitimate counter-arguments.",
         [
             ("Structuring Each Sub-Argument (A-E-I Pattern)", [
                 "Assertion (Affirmation): State the core point clearly with conceptual precision.",
                 "Explication (Explanation): Unpack the sociological, economic, or ethical mechanism.",
                 "Illustration (Evidence): Provide a tangible cultural or real-world Francophone example."
             ]),
             ("Pre-empting Objections (Anticipation Rhétorique)", [
                 "Acknowledge the obvious counter-argument before the jury raises it.",
                 "Formula: 'On pourrait certes objecter que... Néanmoins, cet argument omet de considérer que...'",
                 "Demonstrates total mastery of the topic's complexities."
             ]),
             ("Managing Vocal Cadence and Pauses", [
                 "Silence is a powerful rhetorical tool; pause for two seconds after key assertions.",
                 "Vary pitch and stress to keep the examining committee intellectually engaged."
             ])
         ]),
        (33, "C1 Spoken Interaction: Le Débat Contradictoire avec le Jury",
         "Navigating High-Pressure Exchanges with Intellectual Composure",
         "Following your monologue, the examining panel will challenge your assertions for 15 to 20 minutes.",
         [
             ("Listening Actively to the Examiner's Challenge", [
                 "Never interrupt the examiner; take brief mental notes while they speak.",
                 "Reformulate the question to demonstrate comprehension: 'Si je saisis bien le sens de votre objection...'",
                 "Gains valuable thinking time while showing polite academic respect."
             ]),
             ("Conceding Graciously Without Retreating", [
                 "Acknowledge valid points: 'C'est un point tout à fait pertinent que vous soulevez là...'",
                 "Pivot smoothly back to your thesis: 'Toutefois, si l'on examine la dynamique sur le long terme...'",
                 "Avoid defensive or stubborn postures; embrace academic nuance."
             ]),
             ("Refuting Weak Evidence Firmly", [
                 "Target methodological flaws: 'Il me semble que cette corrélation ne vaut pas causalité.'",
                 "Provide a precise counter-example from Francophone current affairs."
             ])
         ]),
        (34, "C1 Spoken Interaction: Traiter les Questions-Pièges & Objections",
         "Rhetorical Strategies for Extreme, Unfair, or Ambiguous Questions",
         "DALF examiners deliberately test your composure with provocations, paradoxes, and radical hypotheticals.",
         [
             ("Handling the False Dilemma Trap", [
                 "Examiner trap: 'Donc selon vous, il faut soit tout interdire, soit tout autoriser ?'",
                 "C1 Refutation: 'Je ne poserais pas l'alternative en termes si binaires. Il s'agit plutôt de concevoir une régulation modulée qui...' ",
                 "Reject the false dichotomy and introduce a nuanced third path."
             ]),
             ("Handling the Hyperbolic Slippery Slope", [
                 "Examiner trap: 'Si l'on vous suit, demain plus personne ne travaillera !'",
                 "C1 Refutation: 'Ce serait pousser le raisonnement jusqu'à une extrémité que je ne cautionne pas. Mon propos vise uniquement à...'",
                 "Restore moderate boundaries without getting agitated."
             ]),
             ("Handling Questions Outside Your Knowledge Base", [
                 "Never invent false statistics; admit limitations elegantly: 'Bien que je ne dispose pas des chiffres précis sur ce volet, le principe général demeure...'",
                 "Re-anchor the answer to principles you command completely."
             ])
         ]),
        (35, "C1 Spoken Interaction: L'Atténuation, la Modération & le Doute",
         "The Art of Nuanced Hesitation and Intellectual Humility",
         "Dogmatism is a red flag at C1. Native academics use sophisticated modal attenuation to make arguments unassailable.",
         [
             ("Using the Conditional for Prudent Claims", [
                 "Instead of 'Cela prouve que...', use: 'Ces indices tendraient à suggérer que...'",
                 "Instead of 'C'est une catastrophe', use: 'On pourrait y déceler les prémices d'une dérive préoccupante.'",
                 "Softens assertive edges and invites constructive dialogue."
             ]),
             ("Expressions of Prudence and Hesitation", [
                 "'Il serait prématuré d'affirmer de manière catégorique que...'",
                 "'Sous réserve de confirmation empirique, il semble que...'",
                 "'Gardons-nous de tirer des conclusions hâtives de cette seule étude.'"
             ]),
             ("Balancing Prudence with Conviction", [
                 "Once the caveats are established, deliver your core stance with clarity.",
                 "'Tout en mesurant ces limites, ma conviction reste que cette réforme s'impose.'"
             ])
         ]),
        (36, "C1 Spoken Interaction: L'Ironie, le Second Degré & la Distance",
         "Employing Understatement and Wit to Defuse Tensions",
         "The French cultural tradition values wit (l'esprit) and polite understatement (la litote) in public debate.",
         [
             ("Using Litotes in Academic Exchanges", [
                 "Litote: expressing something by denying its contrary ('Ce n'est pas faux', 'Ce n'est point négligeable').",
                 "'Le bilan de ce ministre est pour le moins contrasté' (= disastrous).",
                 "'Votre proposition n'est pas exempte de paradoxes' (= full of glaring contradictions)."
             ]),
             ("Cultivating Distance and Socratic Irony", [
                 "Ask clarifying questions that expose absurdities: 'Faut-il en déduire que la liberté d'expression ne s'appliquerait qu'à ceux qui partagent notre avis ?'",
                 "Smile politely; let the logic do the dismantling rather than aggressive tone."
             ]),
             ("Cultural Boundaries: Irony vs Sarcasm", [
                 "Sarcasm is destructive; intellectual irony is playful and respectful.",
                 "Never mock an interlocutor; focus critique entirely on concepts and arguments."
             ])
         ]),
        (37, "C1 Spoken Interaction: La Rhétorique Persuasive & Formules d'Impact",
         "Oratorical Flourishes, Ternary Rhythm, and Memorable Climax",
         "Elevate your spoken French from merely accurate communication to genuine eloquence and oratorical power.",
         [
             ("The Power of the Ternary Rhythm (La Règle de Trois)", [
                 "Group points in threes for maximum acoustic impact and memorability.",
                 "Example: 'Ce projet manque de vision stratégique, d'ancrage territorial et de légitimité démocratique.'",
                 "Gives speech an intrinsic melodic authority recognized in French rhetoric."
             ]),
             ("Rhetorical Questions (Questions Oratoires)", [
                 "Engage the audience: 'Pouvons-nous décemment cautionner un tel recul au nom de la rentabilité ?'",
                 "Immediately answer your own question to maintain command of the debate."
             ]),
             ("Memorable Formulae for Openings and Closings", [
                 "'Le véritable enjeu ne réside pas dans... mais bien dans notre capacité à...'",
                 "'En dernière analyse, l'histoire ne nous jugera pas sur nos intentions, mais sur nos actes.'"
             ])
         ]),
        (38, "C1 Spoken Fluency: Fluidité Spontanée & Suppression des Tics",
         "Eliminating Verbal Hesitations and Cognitive Pauses",
         "Achieving true spontaneity without relying on 'euh', 'genre', 'du coup', or repetitive fillers.",
         [
             ("Eliminating Colloquial Tics", [
                 "Banish overused fillers: replace 'du coup' with 'par conséquent', 'ainsi', 'de ce fait'.",
                 "Replace 'en mode' or 'genre' with 'à la manière de', 'pour ainsi dire'.",
                 "Replace repetitive 'voilà' with a crisp, measured silence."
             ]),
             ("Techniques for Buying Thinking Time", [
                 "Rephrase the question: 'La question est d'une grande complexité et mérite d'être examinée sous plusieurs angles...'",
                 "Use bridging phrases: 'Avant de répondre sur le fond, permettez-moi de préciser un préalable...'",
                 "Inhale deeply through the nose; think before initiating the sentence."
             ]),
             ("Simulated Rapid Conversational Turns", [
                 "Practice 60-second spontaneous monologues on unexpected abstract prompts.",
                 "Focus on maintaining uninterrupted flow while preserving grammatical agreements."
             ])
         ]),
        (39, "C1 Spoken Idioms: Tournures & Expressions Idiomatiques Soutenues",
         "Prestigious Idiomatic Turns That Signal Deep Cultural Immersion",
         "Incorporate refined idiomatic turns naturally to sound like an educated Francophone intellectual.",
         [
             ("Formal Idioms of Agreement & Disagreement", [
                 "'Être en porte-à-faux avec' (To be awkwardly at odds with reality or principles).",
                 "'Apporter de l'eau au moulin de' (To provide grist to someone's mill / strengthen their case).",
                 "'Faire la part des choses' (To distinguish between different aspects / weigh objectively).",
                 "'Battre en brèche' (To fiercely challenge, tear down an argument or dogma)."
             ]),
             ("Idioms of Action & Caution", [
                 "'Prendre le taureau par les cornes' (To confront a problem boldly).",
                 "'Nager entre deux eaux' (To remain uncommitted / sit on the fence).",
                 "'Jeter le pavé dans la mare' (To cause a stir / drop a bombshell with an uncomfortable truth).",
                 "'Laisser la bride sur le cou' (To give free rein / allow unbridled autonomy)."
             ]),
             ("Using Idioms with Taste and Measure", [
                 "Never string multiple idioms together in one sentence; use them as pinpoint stylistic highlights.",
                 "Ensure the idiom matches the formal register: avoid low-register street slang in formal debate."
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
        (40, "C1 Listening Mastery: Conférences Universitaires & Débats",
         "Decoding Extended Intellectual Speech, Technical Seminars & Panels",
         "At C1, you must follow academic presentations and high-level round-table discussions lasting up to 10 minutes without fatigue.",
         [
             ("Identifying Abstract Conceptual Frameworks", [
                 "Track how professors introduce paradigms, cite theoretical lineages, and define parameters.",
                 "Distinguish the speaker's own original hypotheses from those they cite merely to refute.",
                 "Detect non-verbal emphasis, rhetorical slowdowns, and changes in vocal register."
             ]),
             ("Filtering Out Ambient Academic Jargon", [
                 "Separate essential core logic from ornamental terminology.",
                 "Synthesize long-winded academic explanations into single concise proposition statements."
             ]),
             ("Target Media & Podcasts", [
                 "Listen to 'Les Chemins de la philosophie' (France Culture) and 'Le Collège de France' lectures.",
                 "Practice summarizing 45-minute lectures in a single written paragraph."
             ])
         ]),
        (41, "C1 Listening Mastery: Émissions Radiophoniques Approfondies",
         "Mastering France Culture, RFI, France Inter & Investigative Radio",
         "Authentic radio shows feature overlapping dialogue, rapid interruptions, and references to current French political and literary lore.",
         [
             ("Decoding Overlapping and Fast Conversational Exchanges", [
                 "In lively French panel shows, guests interrupt and talk over each other regularly.",
                 "Train your ear to isolate the dominant speaker's thread while filtering out conversational cross-talk.",
                 "Identify conversational pivots: 'Mais permettez !', 'Si je puis me permettre...', 'Attendez !'"
             ]),
             ("Cultural and Historical Subtexts", [
                 "Recognize passing allusions to French political milestones (Mai 68, l'affaire Dreyfus, la Ve République).",
                 "Connect topical debates to enduring French ideological fault lines (laïcité, modèle républicain)."
             ]),
             ("Daily Practice Routine", [
                 "Listen to 'L'Esprit public' (France Culture) or 'Le Téléphone sonne' (France Inter) at 1.25x speed.",
                 "Write down the core dispute and the contrasting positions of each guest panelist."
             ])
         ]),
        (42, "C1 Listening Mastery: Détection des Sous-Entendus & Implicite",
         "Grasping What is Deliberately Left Unsaid or Couched in Irony",
         "Native speakers rarely say everything explicitly. C1 listeners read between the spoken lines with pinpoint psychological acumen.",
         [
             ("Recognizing Subtle Vocal Irony and Tonal Inflection", [
                 "Detect exaggerated intonation drops that indicate mock approval: 'Bien entendu, tout cela est parfait...'",
                 "Listen for pauses that signal disbelief or polite disdain.",
                 "Decode rhetorical understatement: 'Il n'est pas impossible que...' often means 'It is virtually certain that...'."
             ]),
             ("Deconstructing Political Euphemisms", [
                 "Translate diplomatic jargon: 'un plan de sauvegarde de l'emploi' = mass layoffs.",
                 "'Des divergences d'appréciation' = irreconcilable diplomatic feud.",
                 "'Une concertation constructive' = negotiations ended in complete deadlock."
             ]),
             ("Self-Audit Question", [
                 "After listening to an interview, ask: 'What did the speaker deliberately avoid answering?'"
             ])
         ]),
        (43, "C1 Listening Mastery: Variétés Régionales & Accents Francophones",
         "Comprehending French from Quebec, Belgium, Switzerland & West Africa",
         "The French language is global. A C1 certificate proves you understand authentic spoken French across all Francophone continents.",
         [
             ("Quebec French (Le Français Québécois)", [
                 "Vowel dipthongization, distinct cadence, and local idioms: 'char' (voiture), 'magasiner' (faire des courses).",
                 "Phonetic differences: pronunciation of 't' and 'd' before 'i' and 'u' as 'ts' and 'dz'.",
                 "Practice with Radio-Canada podcasts ('Midi info', 'Aujourd'hui l'histoire')."
             ]),
             ("African Francophonie (Dakar, Abidjan, Yaoundé)", [
                 "Clear articulation, melodic pitch, and unique localized expressions ('faire palabre', 'cadencer').",
                 "Practice with RFI Afrique ('Le Débat africain', 'Appels sur l'actualité')."
             ]),
             ("Belgian & Swiss French", [
                 "Numbers ('septante', 'nonante'), subtle cadence shifts, and local idiomatic connectors ('à tantôt', 'santé').",
                 "Listen to RTBF (Belgium) and RTS (Switzerland) news broadcasts."
             ])
         ]),
        (44, "C1 Listening Mastery: Discours Spontanés à Débit Très Rapide",
         "Processing High-Speed Native Speech with Complete Ease",
         "Native speakers routinely blend vowels, omit 'ne' in negation, and contract syllables at 250+ words per minute.",
         [
             ("Phonetic Reductions in Native Flow", [
                 "'Je ne sais pas' -> 'Chais pas' [ʃɛpa].",
                 "'Il y a' -> 'Y a' [ja]; 'Qu'est-ce que tu fais' -> 'Qu'est-ce tu fais' [kɛstyfɛ].",
                 "'Il faut qu'on y aille' -> 'Faut qu'on y aille' [fokɔ̃njaj]."
             ]),
             ("Anticipatory Listening (La Prédiction Sémantique)", [
                 "Use your knowledge of grammar and collocations to predict the end of the clause before it is spoken.",
                 "Freed-up cognitive bandwidth allows you to focus on macro-meaning rather than decoding individual syllables."
             ]),
             ("Shadowing Exercise", [
                 "Practice 'shadowing': repeat a fast France Culture audio track with a half-second delay.",
                 "Calibrates mouth, ear, and brain to real-time native speech tempo."
             ])
         ]),
        (45, "C1 Listening Mastery: Prise de Notes Synthétique Efficace",
         "Structuring Notes for Real-Time Oral Synthesis and DALF C1",
         "Taking effective notes during a 10-minute audio track without transcribing every word.",
         [
             ("The Two-Column Matrix Method", [
                 "Divide paper into two columns: Left = Thematic Axes & Claims; Right = Specific Data & Evidence.",
                 "Use spatial layout, arrows, and indentation rather than continuous full sentences."
             ]),
             ("Standard French Abbreviation System", [
                 "Use standard symbols: + (plus), - (moins), -> (entraîne, mène à), cf. (se référer à).",
                 "Abbreviations: tjrs (toujours), jms (jamais), devpt (développement), gouv (gouvernement), eco (économie)."
             ]),
             ("Capturing Key Conceptual Transitions", [
                 "Circle logical connectors in red (cependant, par conséquent, or, d'ailleurs).",
                 "These transitions provide the structural roadmap for your subsequent oral summary."
             ])
         ]),
        (46, "C1 Listening Mastery: Distinction des Nuances Émotionnelles",
         "Decoding Affect, Cynicism, Pathos, Indignation and Sarcasm",
         "Differentiating between genuine passion, feigned outrage, calculated cynicism, and earnest concern.",
         [
             ("Acoustic Markers of Indignation", [
                 "Rising pitch on non-final syllables, sharp glottal attacks, and clipped terminal consonants.",
                 "Example: 'C'est tout bonnement inadmissible !'",
                 "Recognize when a politician is performing indignation vs presenting factual rebuttals."
             ]),
             ("Acoustic Markers of Resignation and Fatalism", [
                 "Dropping pitch across the whole clause, accompanied by audible exhalations.",
                 "Example: 'Que voulez-vous qu'on y fasse... à ce stade, les dés sont jetés.'"
             ]),
             ("Analyzing the Speaker's Hidden Agenda", [
                 "Ask: 'Is the speaker attempting to persuade, intimidate, console, or divide the audience?'"
             ])
         ]),
        (47, "C1 Listening Mastery: Discours Spécialisés & Jargon",
         "Handling Medicine, Law, Finance, and Technology Lexicons",
         "A C1 speaker navigates professional seminars and court proceedings without being bewildered by specialized jargon.",
         [
             ("Decoding Greek and Latin Scientific Roots", [
                 "Recognize common roots: bio- (vie), chrono- (temps), démo- (peuple), télé- (loin), omni- (tout).",
                 "Deduce the meaning of unfamiliar terms (e.g., 'iatrogène', 'polysémique', 'incommensurable') in context."
             ]),
             ("Corporate and Administrative Jargon", [
                 "Understand terms like: 'le reporting', 'le benchmarking', 'les externalités négatives', 'les parties prenantes'.",
                 "Identify how institutional buzzwords are used to obscure unpleasant realities."
             ]),
             ("Listening to Judicial Pleadings", [
                 "Follow legal court audio (e.g., Cour de cassation hearings available on public archives).",
                 "Identify formal opening addresses and procedural arguments."
             ])
         ]),
        (48, "C1 Listening Strategies: Reconstitution Sémantique",
         "Overcoming Acoustic Noise, Poor Microphones, and Muffled Audio",
         "Real-world audio is rarely studio-clean. Learn to reconstruct missed words using contextual logic.",
         [
             ("Using Contextual Redundancy (La Redondance Sémantique)", [
                 "Human speech repeats core messages through synonymy, antonymy, and grammatical agreement.",
                 "If a verb is muffled, deduce it from its subject and object complements."
             ]),
             ("Grammatical Deduction of Inaudible Particles", [
                 "A feminine adjective ending indicates an inaudible feminine noun earlier in the sentence.",
                 "A subjunctive verb indicates an inaudible concessive or doubtful conjunction."
             ]),
             ("Training with Degraded Audio", [
                 "Practice listening to train station announcements, crowded street interviews, and archive recordings from 1950."
             ])
         ]),
        (49, "C1 Listening Checklist: Auto-Évaluation de la Compréhension",
         "Self-Audit Rubric for C1 Listening Proficiency and DALF Success",
         "Audit your auditory capabilities against official CEFR C1 performance indicators.",
         [
             ("Autonomous Comprehension Benchmarks", [
                 "[ ] I can follow a 30-minute academic conference with zero subtitles and take organized, useful notes.",
                 "[ ] I instantly understand radio debates featuring fast, overlapping speech (France Culture).",
                 "[ ] I catch subtle humor, irony, and sarcasm in political satire and comedic podcasts.",
                 "[ ] I understand major regional Francophone accents (Quebec, West Africa, Belgium, Switzerland) without difficulty."
             ]),
             ("Technical and Analytical Benchmarks", [
                 "[ ] I can distinguish between factual reporting and ideological spin through vocal cues.",
                 "[ ] I recognize classical and literary vocabulary used during formal ceremonies and lectures.",
                 "[ ] I can reconstruct the overall line of reasoning even when 10% of specific technical words are unknown."
             ]),
             ("DALF C1 Exam Preparedness", [
                 "[ ] I can answer detailed comprehension questions after only two hearings of a 6-minute complex audio track."
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
        (50, "C1 Reading Comprehension: Tribunes de Presse & Éditoriaux",
         "Deconstructing Opinion Pieces in Le Monde, Le Figaro & Courrier International",
         "Editorial journalism represents the gold standard of contemporary French intellectual argumentation.",
         [
             ("Analyzing the Author's Thesis and Ideological Stance", [
                 "Identify the thesis in the opening or concluding paragraphs ('l'attaque' and 'la chute').",
                 "Map the author's political and philosophical sympathies through lexical choices and connotations.",
                 "Notice the use of concessive pivots: how the author disarms opponents before striking with their core point."
             ]),
             ("Decoding Polemical and Satirical Tropes", [
                 "Look for loaded vocabulary: 'prétendu', 'soi-disant', 'une prétendue avancée', 'un simulacre'.",
                 "Spot rhetorical questions designed to mock an opposing policy."
             ]),
             ("Recommended Sources", [
                 "Daily reading: Le Monde (tribunes libres), Le Figaro (débats/opinions), Philosophie Magazine, Le 1."
             ])
         ]),
        (51, "C1 Reading Comprehension: Essais Littéraires & Philosophiques",
         "Navigating Complex Non-Fiction, Existential Prose & Cultural Essays",
         "Engage with major French intellectual essayists (Barthes, Foucault, Camus, Simone de Beauvoir, Edgar Morin).",
         [
             ("Tracking Extended Conceptual Architecture", [
                 "Follow an abstract argument sustained across 10 to 20 pages without losing the conceptual thread.",
                 "Annotate margin notes: summarize each paragraph in a three-word conceptual slug.",
                 "Notice how classical French writers define their terms strictly before deploying them."
             ]),
             ("Appreciating Stylistic Density", [
                 "Observe sentence periods: long, rhythmic clauses building toward an emphatic climax.",
                 "Identify literary metaphors used to illuminate abstract philosophical dilemmas."
             ]),
             ("Practical Reading Exercise", [
                 "Read an excerpt from Camus's 'Le Mythe de Sisyphe' or Lévi-Strauss's 'Tristes Tropiques'.",
                 "Analyze how stylistic elegance enhances the persuasive power of the philosophical argument."
             ])
         ]),
        (52, "C1 Reading Comprehension: Textes Juridiques, Chartes & Décrets",
         "Decoding Institutional Texts, Treaties, Legislation and Regulations",
         "Legal and administrative French is characterized by maximum precision, absolute lack of emotional adjectives, and unique syntactic formulas.",
         [
             ("Understanding the Structure of French Legal Texts", [
                 "The 'Visa' and 'Considérant': preambles outlining the legal grounds of a decree.",
                 "The 'Dispositif': numbered articles setting forth binding statutory rules ('Article premier...').",
                 "Use of the performative present tense: 'Le présent arrêté fixe...' (carries the force of law)."
             ]),
             ("Specific Legal Formulae and Archaic Precision", [
                 "'Sans préjudice de' (Without detriment to / notwithstanding).",
                 "'Est réputé' (Is deemed to be / is legally considered as).",
                 "'Nul ne peut se prévaloir de sa propre turpitude' (No one can benefit from their own wrongdoing)."
             ]),
             ("Application in Civil Society", [
                 "Crucial for understanding tenancy contracts, labor employment agreements, and civil rights declarations."
             ])
         ]),
        (53, "C1 Reading Comprehension: Rapports Institutionnels & Études",
         "Extracting Data and Methodology from Sociological Whitepapers",
         "Read reports from institutions such as l'INSEE, le Conseil économique, social et environnemental (CESE), and OECD.",
         [
             ("Interpreting Statistical Commentary in Prose", [
                 "Understand statistical terminology: 'médiane', 'décile', 'écart-type', 'corrélation vs causalité'.",
                 "Notice how sociologists qualify trends: 'une baisse tendancielle', 'un tassement', 'une embellie passagère'."
             ]),
             ("Critiquing Research Methodology", [
                 "Examine the sample size ('l'échantillon'), the time horizon, and potential selection biases.",
                 "Check whether policy recommendations are genuinely justified by the underlying empirical data."
             ]),
             ("Synthesizing for Oral Briefings", [
                 "Practice extracting three key findings and two policy dilemmas from a 40-page executive summary."
             ])
         ]),
        (54, "C1 Reading Strategies: Analyse de l'Implicite & Ironie",
         "Detecting Subtle Satire, Double Meanings, and Ideological Bias",
         "French writers excel at irony, understatement, and veiled criticism. Learn to read what is written between the lines.",
         [
             ("Spotting Sarcastic Inversion", [
                 "The literal meaning is the opposite of the author's real intent ('Nos brillants technocrates ont encore frappé').",
                 "Look for mismatched stylistic registers: using majestic classical vocabulary to describe mundane incompetence."
             ]),
             ("Analyzing Connotations and Register Clashes", [
                 "Notice when an author replaces a neutral term ('un projet') with a loaded term ('un mirage', 'un délire').",
                 "Look for quotation marks ('scare quotes') indicating ideological skepticism."
             ]),
             ("The Role of Cultural Allusions", [
                 "Recognize references to La Fontaine's fables, Voltaire's Candide, or historic French political speeches.",
                 "These allusions add layers of subtext accessible only to culturally literate readers."
             ])
         ]),
        (55, "C1 Reading Strategies: Progression Thématique & Ruptures",
         "Analyzing How Authors Thread Information from Clause to Clause",
         "Understand the three classical models of thematic progression in French expository writing.",
         [
             ("Progression à Thème Constant", [
                 "The same subject/theme is maintained across multiple sentences with new information (rheme) added each time.",
                 "Creates a focused, stable rhythm suitable for biographical and narrative passages."
             ]),
             ("Progression Linéaire", [
                 "The rheme (new information) of sentence 1 becomes the theme (subject) of sentence 2.",
                 "Creates a dynamic, cascading chain of logic: 'A engendre B, qui suscite C, d'où découle D.'",
                 "The hallmark of rigorous philosophical and scientific exposition."
             ]),
             ("Progression à Thème Dérivé", [
                 "An overarching hyper-theme is announced, followed by individual sentences exploring its sub-components.",
                 "Essential for structuring multipart academic essays and whitepaper sections."
             ])
         ]),
        (56, "C1 Reading Strategies: Lecture Rapide & Écrémage Critique",
         "Skimming and Scanning High-Density Academic Texts in Minutes",
         "The DALF C1 gives you limited time to digest 3 to 4 dense documents (1,500 to 2,000 words total).",
         [
             ("The 'Diagonale Critique' Method", [
                 "Read the title, subheadings, and first and last sentences of every paragraph.",
                 "Underline the core thesis in sentence 1; scan paragraph bodies only for evidence and statistics."
             ]),
             ("Mapping Textual Architecture Visually", [
                 "Circle logical connectors at paragraph breaks (Cependant, En revanche, Par conséquent).",
                 "Determine whether paragraph 3 supports or contradicts paragraph 2 without reading every line."
             ]),
             ("Target Speed Goal", [
                 "Reach a reading speed of 300 to 350 words per minute while maintaining 80%+ conceptual retention."
             ])
         ]),
        (57, "C1 Reading Analysis: Confrontation de Documents Contradictoires",
         "Comparing Divergent Source Texts on the Same Controversy",
         "The core preparatory skill for the DALF C1 document synthesis (synthèse de documents).",
         [
             ("Constructing a Comparative Synthesis Grid", [
                 "Draw a matrix: Columns = Document 1, Document 2, Document 3; Rows = Thematic Problem Axes.",
                 "Fill cells with concise keywords: What does Doc 1 say on Axis A? What does Doc 2 say?"
             ]),
             ("Identifying Concordances, Discordances, and Complementarities", [
                 "Concordance: Points where all authors agree (forms your baseline context).",
                 "Discordance: Direct ideological conflicts (forms your main dialectical opposition).",
                 "Complémentarité: Unique statistical or technical data introduced by one document only."
             ]),
             ("Eliminating Peripheral Trivia", [
                 "Discard illustrative anecdotes, author biographies, and emotional rhetoric; retain only conceptual substance."
             ])
         ]),
        (58, "C1 Reading Analysis: Terminologie & Déconstruction",
         "Dismantling Sophisms, False Equivalences & Ideological Jargon",
         "Sharpen your intellectual immunity against propaganda, fallacious rhetoric, and pseudo-scientific prose.",
         [
             ("Identifying Common Sophisms", [
                 "L'argument d'autorité (Appeal to authority without empirical proof).",
                 "Le faux dilemme (Forcing a binary choice when intermediate options exist).",
                 "L'homme de paille (Straw man: caricaturing an opponent's thesis to make it easy to refute).",
                 "La pente glissante (Slippery slope: claiming a moderate reform will lead directly to apocalypse)."
             ]),
             ("Deconstructing Semantic Shifts", [
                 "Notice when an author subtly changes the definition of a key word between the opening and the conclusion.",
                 "Examine terms with disputed meanings: 'laïcité', 'méritocratie', 'liberté'."
             ]),
             ("Academic Objectivity", [
                 "Evaluate arguments based strictly on their internal validity rather than personal political sympathy."
             ])
         ]),
        (59, "C1 Reading Checklist: Auto-Évaluation de la Compréhension",
         "CEFR C1 Benchmarks for Advanced Textual and Literary Analysis",
         "Assess your autonomous reading fluency against official international standards.",
         [
             ("Critical Reading Competencies", [
                 "[ ] I can read any editorial from Le Monde, Le Figaro, or Courrier International without a dictionary.",
                 "[ ] I understand implicit meanings, sarcasm, and subtle irony in intellectual and literary essays.",
                 "[ ] I can skim a 10-page institutional report in 5 minutes and accurately summarize its core controversy."
             ]),
             ("Comparative and Synthesis Competencies", [
                 "[ ] I can compare two contradictory opinion pieces and identify the exact points of philosophical discord.",
                 "[ ] I recognize classical figures of style, literary periods, and elevated connectors effortlessly.",
                 "[ ] I read at 300+ words per minute with over 80% conceptual retention."
             ]),
             ("DALF C1 Exam Preparedness", [
                 "[ ] I can complete the reading and analysis of a 3-document dossier within 45 minutes during mock exams."
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
        (60, "C1 Writing Mastery: La Synthèse de Documents (DALF C1)",
         "The Strict Methodology of the DALF C1 Document Synthesis",
         "The synthèse de documents is a uniquely French academic exercise: an objective, condensed combination of multiple source texts into a single coherent article (~220 words).",
         [
             ("The Golden Rules of the Synthèse", [
                 "Zero Personal Opinion: Never write 'je', 'à mon avis', or introduce external knowledge.",
                 "Zero Plagiarism: Direct quoting is heavily penalized; every idea must be reformulated in your own words.",
                 "Strict Word Count: Target 220 words (+/- 10%); exceeding limits incurs severe score deductions.",
                 "Neutral, Professional Tone: Act as an objective institutional rapporteur."
             ]),
             ("The 4-Step Production Sequence", [
                 "1. Read and annotate the dossier with a comparative matrix (30 mins).",
                 "2. Draft the problem statement and two-part thematic plan (15 mins).",
                 "3. Write the synthesis directly with fluid transitions (35 mins).",
                 "4. Count words and perform systematic grammar/orthography audit (10 mins)."
             ]),
             ("Handling Document Attributions", [
                 "Do not write 'Document 1 dit... puis Document 2 dit...'.",
                 "Synthesize by themes: 'Si certains observateurs soulignent... d'autres experts mettent en garde contre...'"
             ])
         ]),
        (61, "C1 Writing Mastery: La Synthèse (Structure & Reformulation)",
         "Crafting the Introduction, Thematic Balance, and Reformulation",
         "Examine the architectural anatomy of a high-scoring DALF C1 synthesis.",
         [
             ("The Three-Part Introduction (~30-40 words)", [
                 "L'accroche thématique: Present the shared topic without naming documents.",
                 "La problématique: The core underlying controversy uniting the dossier.",
                 "L'annonce du plan: A balanced two-part outline ('Dans un premier temps... puis...').",
                 "Note: A formal conclusion is NOT mandatory in the C1 synthesis; focus word count on the body."
             ]),
             ("Advanced Reformulation Techniques", [
                 "Nominalization: replace verb clauses with concise noun phrases.",
                 "Synonymy and Semantic Re-framing: convert informal phrasing into academic register.",
                 "Condensation: merge three illustrative examples into a single category label ('les énergies fossiles')."
             ]),
             ("Maintaining Perfect Thematic Balance", [
                 "Ensure Part 1 and Part 2 are roughly equal in length (~80-90 words each).",
                 "Integrate points from all dossier documents across both parts."
             ])
         ]),
        (62, "C1 Writing Mastery: L'Essai Argumenté (La Problématique)",
         "Formulating a Compelling Thesis for the 250-Word Argumentative Essay",
         "The second written task of the DALF C1 requires defending a personal position on a societal debate with academic rigor (~250 words).",
         [
             ("The Role of the Problématique in the Essai Argumenté", [
                 "The problem statement proves you have grasped the deeper implications of the prompt.",
                 "Transform a simplistic question into a multidimensional societal dilemma.",
                 "Example prompt: 'Faut-il restreindre le trafic automobile en ville ?'",
                 "C1 Problématique: 'En quoi la pacification de l'espace urbain par la restriction automobile oblige-t-elle à repenser l'équité territoriale et le droit fondamental à la mobilité ?'"
             ]),
             ("Crafting an Irresistible Opening (L'Accroche)", [
                 "Start with a striking philosophical observation, historical turning point, or compelling paradox.",
                 "Avoid childish clichés like 'Depuis la nuit des temps...' or 'De nos jours...'."
             ]),
             ("Stating Your Stance with Nuance", [
                 "Avoid crude declarations like 'Je suis 100% contre ce projet'.",
                 "Prefer nuanced positioning: 'S'il convient d'encourager la transition, nous soutiendrons qu'une telle mesure ne saurait être viable sans garanties sociales solides.'"
             ])
         ]),
        (63, "C1 Writing Mastery: L'Essai Argumenté (Plans & Rhétorique)",
         "Dialectical, Thematic, and Analytical Essay Architectures",
         "Select the essay plan that best fits your topic and allows for maximum rhetorical elegance.",
         [
             ("The Dialectical Plan (Thèse / Antithèse / Synthèse)", [
                 "Ideal for controversial topics with stark opposing camps.",
                 "Part 1 (Thèse): Present the strongest arguments in favor of the measure.",
                 "Part 2 (Antithèse): Present the fundamental flaws and objections.",
                 "Part 3 (Synthèse / Dépassement): Resolve the contradiction through a higher conceptual framework."
             ]),
             ("The Thematic Plan (Aspects Économiques, Éthiques, Sociétaux)", [
                 "Ideal for open-ended prompts asking you to explore the ramifications of a phenomenon.",
                 "Part 1: The economic and technological drivers.",
                 "Part 2: The ethical and human consequences."
             ]),
             ("The Analytical Plan (Problème / Causes / Solutions)", [
                 "Ideal for policy proposals and crisis management briefs."
             ])
         ]),
        (64, "C1 Writing Mastery: L'Article d'Opinion & la Tribune",
         "Publishing-Grade Persuasive Prose with Engaging Register",
         "Writing an impactful opinion piece (tribune libre) destined for a broad educated public.",
         [
             ("Choosing an Engaging Headline (Le Titre Accrocheur)", [
                 "A great C1 title is memorable and evocative: 'La démocratie à l'épreuve des algorithmes : le réveil nécessaire'.",
                 "Use chiasmus or contrast: 'Quand l'urgence écologique défie la lenteur démocratique'."
             ]),
             ("Writing with Force and Cadence (L'Attaque et la Chute)", [
                 "L'Attaque: The opening sentence must immediately seize the reader's intellect.",
                 "La Chute: The final sentence must resonate like an oratorical clarion call, leaving a lasting impression."
             ]),
             ("Modulating Register for Persuasion", [
                 "Combine elevated academic vocabulary with passionate rhetorical appeals.",
                 "Use rhetorical questions and direct civic appeals ('Nous ne saurions tolérer que...')."
             ])
         ]),
        (65, "C1 Writing Style: Richesse Lexicale & Variété Syntaxique",
         "Elevating Your Style: Word Choice, Sentence Lengths & Collocations",
         "At C1, examiners reward stylistic panache. Avoid repetitive syntax and bland verbs.",
         [
             ("Banishing Weak Verbs (Les Verbes Pauvres)", [
                 "Replace 'faire' with: 'commettre' (une erreur), 'perpétrer' (un acte), 'élaborer' (un plan), 'exercer' (une pression).",
                 "Replace 'avoir' with: 'bénéficier de' (avantages), 'éprouver' (des doutes), 'détenir' (un pouvoir).",
                 "Replace 'il y a' with: 'il subsiste', 'il s'ensuit', 'on observe', 'il règne'."
             ]),
             ("Alternating Sentence Lengths (Rhythm and Cadence)", [
                 "Follow an elaborate, 35-word periodic sentence with a sharp, 6-word punchy assertion.",
                 "Creates a captivating musicality that makes reading your essay an absolute pleasure."
             ]),
             ("Mastering High-Level Collocations", [
                 "'Une divergence criante', 'un espoir ténu', 'une volonté farouche', 'un paradoxe saisissant'."
             ])
         ]),
        (66, "C1 Writing Mechanics: Connecteurs Logiques Soutenus",
         "Architectural Connectors that Establish Smooth Transitions",
         "Move far beyond 'premièrement', 'de plus', and 'pour conclure'. Use the gold-standard repertoire of French academic transitions.",
         [
             ("Connectors for Nuanced Opposition & Concession", [
                 "'Il n'en demeure pas moins que...', 'Nonobstant le fait que...'",
                 "'En dépit de ces avancées, force est de constater que...'",
                 "'Quoi qu'il en soit, il paraît illusoire d'espérer...'"
             ]),
             ("Connectors for Logical Progression & Cause", [
                 "'D'autant que...', 'Partant de ce constat...', 'Eu égard à la gravité des faits...'",
                 "'Il s'ensuit naturellement que...'"
             ]),
             ("Connectors for Synthesis and Resolution", [
                 "'À l'aune de ces réflexions...', 'En dernière analyse...', 'Tout bien pesé...'"
             ])
         ]),
        (67, "C1 Writing Mechanics: Protocole d'Auto-Correction C1",
         "The Systematic 5-Minute Proofreading Routine (Zero Syntax Error)",
         "At C1, candidates lose precious marks not on complex grammar, but on careless agreement slips. Follow this strict checklist.",
         [
             ("Phase 1: Past Participle Agreement Scan", [
                 "Scan every single 'avoir' auxiliary: check for preceding direct objects (COD).",
                 "Example: 'Les mesures qu'il a prises' (prises agrees with 'les mesures').",
                 "Scan pronominal verbs: 'Elles se sont parlé' (no agreement, parler à), but 'Elles se sont vues' (agreement, voir qqn)."
             ]),
             ("Phase 2: Subjunctive Mood Verification", [
                 "Check every clause following 'bien que', 'quoique', 'afin que', 'pour que', 'avant que'.",
                 "Verify irregular subjunctive stems: 'qu'il sache', 'qu'il puisse', 'qu'ils veuillent'."
             ]),
             ("Phase 3: Word Count & Punctuation Audit", [
                 "Count words accurately (hyphenated words like 'c'est-à-dire' count as multiple words according to official rules).",
                 "Ensure proper French punctuation spacing: non-breaking space before colons, semicolons, and question marks."
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

    # Pages 68-71: Final Self-Evaluation & Milestone Readiness (4 pages)
    audit_pages = [
        (68, "Final Self-Evaluation: Speaking Readiness & Debate Mastery",
         "Audit of Spoken Monologue, Dialectical Defense, and Panel Exchanges",
         "Evaluate your oral performance against the rigorous official criteria of the DALF C1 jury.",
         [
             ("1. Monologue Structuré & Problématique (Exposé Oral)", [
                 "[ ] I can synthesize a complex 3-document dossier into a clear, focused problem statement within 1 hour of preparation.",
                 "[ ] I present an organized 10-to-15 minute oral presentation with clear plan signposting and diverse arguments.",
                 "[ ] I balance abstract theoretical concepts with concrete sociological and Francophone cultural examples.",
                 "[ ] I speak continuously without reading pre-written full sentences, maintaining steady eye contact with the jury."
             ]),
             ("2. Débat Contradictoire avec le Jury (Spoken Interaction)", [
                 "[ ] I defend my thesis calmly and convincingly when challenged by hostile examiner counterarguments.",
                 "[ ] I acknowledge valid opposing points with concessive nuance without abandoning my foundational thesis.",
                 "[ ] I detect and neutralize false dilemmas, hasty generalizations, and trap questions without agitation.",
                 "[ ] I modulate my tone between formal academic defense and polite, engaging conversational banter."
             ]),
             ("3. Fluency & Oratorical Panache", [
                 "[ ] I speak at natural native tempo (200+ words/min) with zero disruptive 'euh' or informal verbal tics.",
                 "[ ] I incorporate ternary rhythms, rhetorical questions, and elevated idiomatic expressions naturally."
             ])
         ]),
        (69, "Final Self-Evaluation: Auditory, Literary & Receptive Autonomy",
         "Audit of Fast Native Broadcasts, Regional Accents, and Difficult Texts",
         "Assess your ability to understand complex, unedited French across all media formats and regional accents.",
         [
             ("1. Compréhension Orale Approfondie (Listening)", [
                 "[ ] I understand university lectures and panel debates on France Culture without missing key arguments.",
                 "[ ] I follow fast native French with overlapping speech, colloquial contractions, and background ambient noise.",
                 "[ ] I readily understand major regional and international Francophone accents (Quebec, West Africa, Belgium, Switzerland).",
                 "[ ] I take clean, structured notes during a 10-minute speech using standard abbreviations and logical mapping."
             ]),
             ("2. Compréhension Écrite & Critique (Reading)", [
                 "[ ] I read leading articles and editorials in Le Monde, Le Figaro, and Courrier International at 300+ words/min.",
                 "[ ] I detect underlying ideological bias, irony, metaphorical subtext, and unstated assumptions in essays.",
                 "[ ] I can compare three conflicting texts on a controversial topic and map their agreements and discords within 30 minutes.",
                 "[ ] I understand complex legal declarations, decrees, and institutional whitepapers without specialized training."
             ])
         ]),
        (70, "Final Self-Evaluation: Written Synthesis & Stylistic Precision",
         "Audit of the DALF C1 Document Synthesis and 250-Word Argumentative Essay",
         "Verify your written production against official DALF C1 grading matrices (Synthèse + Essai argumenté).",
         [
             ("1. La Synthèse de Documents (Objective Synthesis)", [
                 "[ ] I can produce a strict 220-word synthesis (+/- 10%) combining multiple source documents without external bias.",
                 "[ ] I reformulate every concept in my own words, avoiding direct quotes and stylistic plagiarism entirely.",
                 "[ ] I maintain an objective, formal rapporteur tone without ever using 'je', 'mon opinion', or personal anecdotes.",
                 "[ ] My introduction contains an engaging hook, a razor-sharp problem statement, and an explicit two-part plan."
             ]),
             ("2. L'Essai Argumenté (Persuasive Essay)", [
                 "[ ] I compose a 250+ word argumentative essay structured around a solid dialectical or thematic plan.",
                 "[ ] I formulate an engaging hook and a thought-provoking conclusion ('élargissement') that opens future avenues.",
                 "[ ] I use a rich palette of advanced rhetorical connectors (il n'en demeure pas moins, partant, eu égard à).",
                 "[ ] I vary sentence lengths, employing absolute subject inversions and sophisticated nominalizations."
             ]),
             ("3. Grammatical & Orthographic Flawlessness", [
                 "[ ] My text contains zero basic errors in past participle agreement, subjunctive mood, or gender concordances."
             ])
         ]),
        (71, "Final Milestone: Ready to Move to C2 Mastery & DALF C1 Success",
         "Final Certification Readiness, Autonomous Fluency, and Path to C2",
         "Congratulations on completing the French C1 Curriculum Roadmap! Review your overall readiness for DALF C1 certification.",
         [
             ("The C1 Autonomous User Benchmark", [
                 "You are no longer an intermediate student translating from English. You think, conceptualize, debate, and write directly in French with academic poise, intellectual subtlety, and cultural authority.",
                 "You can participate in university seminars, lead executive business meetings in Paris, Montreal, or Geneva, and read the greatest works of French literature with profound appreciation."
             ]),
             ("DALF C1 Exam Success Checklist", [
                 "[ ] Compréhension de l'oral: Scored 15+/25 on official mock exams.",
                 "[ ] Compréhension des écrits: Scored 15+/25 on official mock exams.",
                 "[ ] Production écrite (Synthèse + Essai): Scored 15+/25 on official mock exams.",
                 "[ ] Production orale (Exposé + Débat): Scored 15+/25 on official mock exams.",
                 "[ ] Overall composite score exceeds 50/100 with no single component below 5/25."
             ]),
             ("Looking Forward to CEFR C2 (Mastery / Maîtrise)", [
                 "If you scored 85%+ across this checklist, you are officially ready to advance to French C2: the pinnacle of language mastery, featuring classical French literature, rhetorical virtuosity, and native-level bilingual fluency."
             ])
         ])
    ]

    for page_num, title, subtitle, intro, sections in audit_pages:
        # Also provide items flattened for backwards compatibility with tests
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
    c1_data = get_c1_data()
    print(f"Generated C1 data: {len(c1_data)} pages")
    with open("c1_curriculum_data.py", "w", encoding="utf-8") as f:
        f.write("# c1_curriculum_data.py\n")
        f.write("# Comprehensive 71-page CEFR C1 Curriculum Dataset\n\n")
        f.write("C1_PAGES_DATA = ")
        f.write(pprint.pformat(c1_data, indent=4, width=120))
        f.write("\n")
    print("Successfully wrote c1_curriculum_data.py")
