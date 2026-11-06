import pprint

def get_b2_data():
    pages = {}

    # Page 1: Cover
    pages[1] = {
        "page": 1,
        "type": "cover",
        "title": "French Learning Roadmap & Checklist",
        "subtitle": "French B2",
        "badge_num": "",
        "intro": ""
    }

    # Page 2: Overall Objectives of B2 Level (Independent User / Vantage)
    pages[2] = {
        "page": 2,
        "type": "objectives",
        "title": "Overall Objectives of B2 Level (Independent User / Vantage)",
        "subtitle": "Speaking & Listening Skills for Advanced Argumentation",
        "badge_num": "1",
        "intro": "Welcome to French B2! At this advanced intermediate stage, you become a fully independent speaker. You can debate complex societal questions, defend your ideas spontaneously, follow fast conversations, and understand complex cultural nuances.",
        "sections": [
            {
                "title": "Speak (Spoken Production & Spoken Interaction)",
                "items": [
                    "Present and defend an argumentative thesis for 4 to 5 minutes on controversial social, political, or ethical issues.",
                    "Engage in lively debates with native speakers, refuting opposing arguments and offering convincing counter-examples.",
                    "Adapt your tone and vocabulary smoothly between informal banter, standard professional French, and formal academic discussion.",
                    "Qualify your opinions with subtlety, expressing doubt, probability, concession, and irony without hesitation."
                ]
            },
            {
                "title": "Listen (Listening Comprehension)",
                "items": [
                    "Follow extended speeches, conferences, and technical presentations even when the topic is abstract or specialized.",
                    "Understand authentic radio debates, panel discussions, and podcasts spoken at fast native speed with overlapping dialogue.",
                    "Identify underlying attitudes, implicit criticism, irony, and rhetorical strategies used by public speakers and journalists."
                ]
            }
        ]
    }

    # Page 3: Overall Objectives of B2 Level (Continued)
    pages[3] = {
        "page": 3,
        "type": "objectives",
        "title": "Overall Objectives of B2 Level (Continued)",
        "subtitle": "Reading & Writing Skills for Academic & Professional Mastery",
        "badge_num": "2",
        "intro": "At B2, your reading and writing reach full professional and academic fluency. You can analyze long-form journalism, synthesize opposing arguments, and compose sophisticated 250-word argumentative essays.",
        "sections": [
            {
                "title": "Write (Written Production & Interaction)",
                "items": [
                    "Write well-structured argumentative essays and articles (250 words) synthesizing multiple viewpoints with clarity.",
                    "Draft formal administrative petitions, open letters (tribunes libres), and executive project proposals.",
                    "Vary your sentence structure using nominalization, relative pronouns, and diverse rhetorical connectors.",
                    "Proofread and self-correct with precision, maintaining flawless agreement of past participles and subjunctive mood."
                ]
            },
            {
                "title": "Read (Reading Comprehension)",
                "items": [
                    "Read long-form investigative articles, editorials, and commentary in Le Monde, Libération, and Courrier International.",
                    "Analyze contemporary French literature, essays, and short stories, understanding character subtext and narrative irony.",
                    "Quickly skim and synthesize dense administrative decrees, legal white papers, and economic reports for key facts."
                ]
            }
        ]
    }

    # Page 4: Real-Life Outcomes & Themes 1-4
    pages[4] = {
        "page": 4,
        "type": "themes_table",
        "title": "B2 French – Real-Life Outcomes & Core Themes & Topics",
        "subtitle": "Real-Life Outcomes at CEFR B2 (Themes 1–4)",
        "badge_num": "3",
        "intro": "These real-life competencies and societal themes represent full independent mastery of French for academic, professional, and civic life.",
        "items": [
            "Defend an argumentative thesis convincingly in live debate with educated native speakers.",
            "Write sophisticated formal synthesis essays (250 words) balancing opposing viewpoints.",
            "Follow complex radio debates and long-form intellectual commentary with ease."
        ],
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 1: Bioethics & Medical Advances", "Genetic editing, reproductive rights, organ donation, and medical ethics.", "« Les avancées du génie génétique soulèvent des questions éthiques fondamentales. »"],
                ["Theme 2: Artificial Intelligence & Surveillance", "Algorithm bias, digital sovereignty, data privacy, and facial recognition.", "« Le déploiement massif de l'IA exige une régulation juridique rigoureuse. »"],
                ["Theme 3: Globalization & Economic Models", "Fair trade, degrowth, neoliberalism, circular economy, and supply chains.", "« Il convient de repenser notre modèle de croissance face aux limites planétaires. »"],
                ["Theme 4: Democracy & Civic Institutions", "Direct democracy, citizen assemblies, freedom of protest, and constitutional reform.", "« Les conventions citoyennes permettent de revitaliser le dialogue démocratique. »"]
            ]
        }
    }

    # Page 5: Themes 5-7
    pages[5] = {
        "page": 5,
        "type": "themes_table",
        "title": "B2 French – Core Themes & Topics (Part 2)",
        "subtitle": "Themes 5–7: Environmental Justice, Arts & Changing Work",
        "badge_num": "4",
        "intro": "Explore complex debates around environmental justice, modern culture, and the changing landscape of labor.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 5: Environmental Justice & Energy", "Nuclear vs renewable power, climate migration, climate litigation, and eco-anxiety.", "« Les contentieux climatiques incitent les États à respecter leurs engagements écologiques. »"],
                ["Theme 6: Modern Literature, Arts & Society", "Cultural appropriation, artistic censorship, museum repatriation, and street art.", "« La restitution des œuvres d'art ouvre une nouvelle ère de coopération mémorielle. »"],
                ["Theme 7: The Changing World of Work", "Automation, platform workers, quiet quitting, universal basic income, and burn-out.", "« L'ubérisation de l'économie remet en cause les protections sociales traditionnelles. »"]
            ]
        }
    }

    # Page 6: Themes 8-10
    pages[6] = {
        "page": 6,
        "type": "themes_table",
        "title": "B2 French – Core Themes & Topics (Part 3)",
        "subtitle": "Themes 8–10: Media, Education & Future Cities",
        "badge_num": "5",
        "intro": "Debate media polarization, education reforms, and urban design challenges with advanced vocabulary.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 8: Media Polarization & Truth", "Information echo chambers, deepfakes, whistleblowers, and press ownership.", "« La concentration des médias entre les mains de quelques industriels inquiète les observateurs. »"],
                ["Theme 9: Education Reforms & Mobility", "Standardized testing, elite schools (grandes écoles), affirmative action, and social ladders.", "« La démocratisation de l'enseignement supérieur doit s'accompagner d'un véritable tutorat. »"],
                ["Theme 10: Future Cities & Architecture", "Gentrification, urban sprawl, pedestrianization, passive houses, and urban farming.", "« La piétonnisation des centres historiques favorise à la fois le commerce et la santé publique. »"]
            ]
        }
    }

    # Page 7: Communicative Functions
    pages[7] = {
        "page": 7,
        "type": "functions_table",
        "title": "B2 French – Core Communicative Functions",
        "subtitle": "Themes 11–14 & Advanced Communicative Functions",
        "badge_num": "6",
        "intro": "Master these advanced linguistic devices to construct persuasive arguments, handle objections, and summarize complex ideas.",
        "table": {
            "headers": ["Communicative Function", "Grammar & Key Patterns", "Practical Real-Life Example"],
            "rows": [
                ["Nuanced Concession", "Bien que / Quoique + subj. / Avoir beau", "« J'ai beau examiner vos arguments, je n'y trouve aucune justification économique viable. »"],
                ["Formal Subject Inversion", "Inversion après adverbs (Peut-être, À peine)", "« À peine la loi avait-elle été votée que les premières contestations ont surgi. »"],
                ["Expressing Future Completion", "Futur antérieur", "« D'ici la fin du siècle, la communauté internationale aura dû réinventer sa production d'énergie. »"],
                ["Refuting Counterarguments", "Loin de là / Il ne s'agit nullement de", "« Loin de vouloir freiner l'innovation, il s'agit plutôt d'encadrer ses dérives potentielles. »"],
                ["Rhetorical Nominalization", "Transformation en tournure nominale", "« L'adoption rapide de ce protocole permettra la stabilisation des cours boursiers. »"],
                ["Advanced Past Hypotheses", "Au cas où + cond. / En admettant que + subj.", "« En admettant que cette thèse soit validée, quelles en seraient les répercussions pratiques ? »"]
            ]
        }
    }

    # Pages 8-19: Grammar Foundation
    # Page 8: Le Subjonctif Passé
    pages[8] = {
        "page": 8,
        "type": "checklist",
        "title": "B2 Grammar: Le Subjonctif Passé",
        "subtitle": "Formation, Tense Harmony & Nuances of Completed Action",
        "badge_num": "7",
        "intro": "The subjonctif passé is used when the subjunctive action is finished prior to the main clause verb.",
        "sections": [
            {
                "title": "1. Forming the Subjonctif Passé",
                "items": [
                    "Auxiliary Avoir or Être in the subjonctif présent + past participle: que j'aie parlé, que tu sois parti(e).",
                    "With Avoir: que j'aie fini, que tu aies compris, qu'il ait fait, que nous ayons vu, qu'ils aient pu.",
                    "With Être (movement & reflexive verbs): que je sois arrivé(e), qu'elle se soit plainte, que nous soyons intervenus.",
                    "Past participle agreement rules apply fully: gender and number agree with the subject when using être."
                ]
            },
            {
                "title": "2. When to Use Subjonctif Passé",
                "items": [
                    "Completed action before a present emotion: « Je suis ravi que vous ayez obtenu ce poste prestigieux. »",
                    "Expressing relief or regret about a past outcome: « C'est dommage qu'ils n'aient pas assisté à la conférence. »",
                    "After temporal conjunctions (avant que + ne explétif): « Avant qu'il n'ait pu réagir, l'accord était déjà signé. »",
                    "Doubts regarding past events: « Je doute qu'elle ait commis cette faute délibérément. »"
                ]
            }
        ]
    }

    # Page 9: Subjonctif vs Indicatif: Subtle Nuances
    pages[9] = {
        "page": 9,
        "type": "checklist",
        "title": "B2 Grammar: Subjonctif vs Indicatif (Subtle Nuances)",
        "subtitle": "Verbs with Dual Meaning, Concessions & Relative Clauses",
        "badge_num": "8",
        "intro": "At B2, the choice between subjunctive and indicative depends on fine nuances of certainty, intention, and subjectivity.",
        "sections": [
            {
                "title": "1. Verbs with Dual Meaning (Indicatif vs Subjonctif)",
                "items": [
                    "Comprendre: + Indicatif (understand a fact: « Je comprends qu'il est fatigué ») vs + Subjonctif (sympathize/accept: « Je comprends qu'il veuille partir »).",
                    "Admettre: + Indicatif (acknowledge reality: « J'admets que c'est vrai ») vs + Subjonctif (tolerate: « J'admets qu'il fasse des erreurs »).",
                    "Dire / Prétendre: + Indicatif (statement: « Il dit qu'il vient ») vs + Subjonctif (order: « Dis-lui qu'il vienne »).",
                    "Espérer: always takes the indicatif in affirmative statements (« J'espère qu'il viendra »), unlike souhaiter (+ subj.)."
                ]
            },
            {
                "title": "2. Subjunctive in Relative Clauses",
                "items": [
                    "Looking for something that might not exist: « Je cherche quelqu'un qui sache parler japonais » (uncertainty).",
                    "Looking for a specific known person: « Je connais quelqu'un qui sait parler japonais » (certainty / indicatif).",
                    "After superlatives (le seul, l'unique, le premier qui): « C'est le plus beau film que j'aie jamais vu » (subjonctif passé).",
                    "After negative antecedents: « Il n'y a personne qui puisse résoudre cette énigme. »"
                ]
            }
        ]
    }

    # Page 10: Le Futur Antérieur
    pages[10] = {
        "page": 10,
        "type": "checklist",
        "title": "B2 Grammar: Le Futur Antérieur",
        "subtitle": "Anteriority in the Future, Probabilities & Suppositions",
        "badge_num": "9",
        "intro": "The futur antérieur expresses an action that will be completed before another future action, or an educated guess about the past.",
        "sections": [
            {
                "title": "1. Forming the Futur Antérieur",
                "items": [
                    "Auxiliary Avoir or Être in the futur simple + past participle: j'aurai parlé, je serai arrivé(e).",
                    "Regular conjugation: j'aurai terminé, tu auras compris, nous aurons agi, ils auront découvert.",
                    "Verbs with être: elle sera partie, nous nous serons concertés, ils seront rentrés.",
                    "Past participle agreement follows standard rules for compound tenses."
                ]
            },
            {
                "title": "2. Advanced Usage: Anteriority & Probability",
                "items": [
                    "Action completed before a future deadline: « Dès que nous aurons signé le contrat, nous commencerons les travaux. »",
                    "Temporal conjunctions triggering futur antérieur: dès que, aussitôt que, quand, lorsque, une fois que.",
                    "Expressing probability about a past action: « Paul n'est pas venu ; il aura sans doute raté sa correspondance. »",
                    "Historical / chronological projection: « Dans dix ans, nos modes de transport auront profondément changé. »"
                ]
            }
        ]
    }

    # Page 11: L'Inversion Complexe du Sujet
    pages[11] = {
        "page": 11,
        "type": "checklist",
        "title": "B2 Grammar: L'Inversion Complexe du Sujet",
        "subtitle": "Elevating Written Syntax and Formal Argumentative Style",
        "badge_num": "10",
        "intro": "Master formal subject inversion to add elegance and persuasive power to your written essays and formal speeches.",
        "sections": [
            {
                "title": "1. Inversion after Adverbs (Peut-être, À peine, Aussi)",
                "items": [
                    "Peut-être at the start of a clause: « Peut-être aurions-nous dû solliciter un deuxième avis juridique. »",
                    "À peine (scarcely / barely): « À peine le ministre avait-il pris la parole que des manifestants ont protesté. »",
                    "Aussi (therefore / so at start of clause): « Les délais étaient serrés ; aussi avons-nous mobilisé toute l'équipe. »",
                    "Sans doute: « Sans doute les réformes porteront-elles leurs fruits d'ici l'année prochaine. »"
                ]
            },
            {
                "title": "2. Complex Inversion with Noun Subjects",
                "items": [
                    "Keep the noun subject, add hyphenated pronoun after the verb: « Le président a-t-il validé ce décret ? »",
                    "Inversion in incise clauses (in reported speech): « 'La situation est maîtrisée', a affirmé le préfet. »",
                    "Inversion in relative clauses: « C'est le résultat qu'ont obtenu les chercheurs du laboratoire. »",
                    "Euphonic 't' inserted between vowels: « Où va-t-on ? », « Quand arrivera-t-elle ? »"
                ]
            }
        ]
    }

    # Page 12: La Nominalisation
    pages[12] = {
        "page": 12,
        "type": "checklist",
        "title": "B2 Grammar: La Nominalisation",
        "subtitle": "Transforming Verbal Phrases into Concise Formal Noun Phrases",
        "badge_num": "11",
        "intro": "Nominalization is the trademark of French academic, journalistic, and administrative style. It condenses ideas and increases impact.",
        "sections": [
            {
                "title": "1. Common Suffixes for Verbal Nominalization",
                "items": [
                    "Suffix -tion/-ation: augmenter → l'augmentation, publier → la publication, réformer → la réforme / la réformation.",
                    "Suffix -ment: développer → le développement, licencier → le licenciement, ralentir → le ralentissement.",
                    "Suffix -age: recycler → le recyclage, bloquer → le blocage, nettoyer → le nettoyage.",
                    "Suffix -ure: fermer → la fermeture, rompre → la rupture, signer → la signature."
                ]
            },
            {
                "title": "2. Nominalization in Press Headlines & Essays",
                "items": [
                    "Transforming clauses: « Parce que le chômage a baissé » → « Grâce à la baisse du chômage... »",
                    "Transforming passive verbs: « Les prix ont été gelés » → « Le gel des prix par les autorités compétentes. »",
                    "Headline compression: « Deux ministres ont démissionné » → « Démission surprise de deux ministres. »",
                    "Using nominal structures to open paragraphs in formal argumentative essays."
                ]
            }
        ]
    }

    # Page 13: Les Pronoms Relatifs Complexes & Littéraires
    pages[13] = {
        "page": 13,
        "type": "checklist",
        "title": "B2 Grammar: Pronoms Relatifs Complexes",
        "subtitle": "Dont vs Duquel, Quoi, Où Temporal, and Elevated Pronouns",
        "badge_num": "12",
        "intro": "Navigate the subtle boundaries between relative pronouns in formal written French and high-level debate.",
        "sections": [
            {
                "title": "1. Dont vs Duquel / De laquelle",
                "items": [
                    "Use dont for simple verbs followed by 'de': « La loi dont nous parlons » (parler de).",
                    "Use duquel/de laquelle after compound prepositions: « La table au milieu de laquelle se trouve le dossier. »",
                    "Avoid double prepositions with dont (never write 'près de dont' ; write 'près duquel').",
                    "Dont with possession: noun keeps its definite article: « Un écrivain dont le livre est célèbre » (never 'dont son livre')."
                ]
            },
            {
                "title": "2. Indefinite 'Quoi' and Temporal 'Où'",
                "items": [
                    "Quoi after prepositions with indefinite antecedents (rien, quelque chose, ce): « Il n'y a rien à quoi je tienne davantage. »",
                    "« C'est ce à quoi je pensais » / « C'est ce de quoi nous débattions ce matin. »",
                    "Où referring to time periods: « Le jour où nous nous sommes rencontrés », « L'époque où le télétravail n'existait pas. »",
                    "D'où expressing origin or logical consequence: « D'où l'importance de vérifier ses sources avec méthode. »"
                ]
            }
        ]
    }

    # Page 14: Les Nuances des Verbes Modaux
    pages[14] = {
        "page": 14,
        "type": "checklist",
        "title": "B2 Grammar: Nuances des Verbes Modaux",
        "subtitle": "Devoir, Pouvoir, Savoir, and Falloir across Tenses and Moods",
        "badge_num": "13",
        "intro": "French modal verbs convey subtle shades of probability, moral duty, physical ability, and speculation depending on tense.",
        "sections": [
            {
                "title": "1. Nuances of 'Devoir'",
                "items": [
                    "Present indicative: moral obligation or scheduled plan (« Il doit arriver à 14h »).",
                    "Imparfait: past probability or unfulfilled intention (« Il devait nous rejoindre, mais son train a eu du retard »).",
                    "Conditionnel présent: polite advice or moral expectation (« Vous devriez consulter un spécialiste »).",
                    "Conditionnel passé: unfulfilled past obligation or strong reproach (« Tu aurais dû me prévenir plus tôt ! »)."
                ]
            },
            {
                "title": "2. Nuances of 'Pouvoir' and 'Savoir'",
                "items": [
                    "Pouvoir in conditionnel: diplomatic possibility (« Pourrions-nous envisager une autre option ? »).",
                    "Pouvoir in conditionnel passé: lost opportunity or past reproach (« Elle aurait pu nous avertir du danger »).",
                    "Savoir in conditional: polite capability (« Je ne saurais vous dire avec certitude »).",
                    "Subjunctive forms: « Bien qu'il puisse réussir », « Pour autant que je sache »."
                ]
            }
        ]
    }

    # Page 15: L'Expression de l'Hypothèse Avancée
    pages[15] = {
        "page": 15,
        "type": "checklist",
        "title": "B2 Grammar: L'Hypothèse Avancée",
        "subtitle": "Conjunctions with Subjunctive, Conditional, and Noun Phrases",
        "badge_num": "14",
        "intro": "Go beyond basic 'Si' clauses by mastering advanced hypothetical conjunctions required for DELF B2 argumentation.",
        "sections": [
            {
                "title": "1. Conjunctions Requiring the Subjunctive",
                "items": [
                    "À condition que (provided that): « Nous signerons à condition que toutes les garanties soient réunies. »",
                    "Pourvu que (as long as / let's hope that): « Pourvu que les négociations aboutissent d'ici vendredi. »",
                    "À moins que (+ ne explétif: unless): « Nous partirons demain à moins qu'il ne pleuve trop fort. »",
                    "En admettant que / En supposant que: « En admettant qu'il accepte, quelles seront vos exigences ? »"
                ]
            },
            {
                "title": "2. Conjunctions with Conditional and Prepositions",
                "items": [
                    "Au cas où (+ Conditionnel: in case): « Emportez un parapluie au cas où il pleuvrait ce soir. »",
                    "Quand bien même (+ Conditionnel: even if): « Quand bien même il présenterait ses excuses, le préjudice est fait. »",
                    "En cas de (+ Nom): « En cas d'urgence médicale, composez immédiatement le 15. »",
                    "À défaut de (+ Nom / Infinitif): « À défaut de solution parfaite, choisissons le moindre mal. »"
                ]
            }
        ]
    }

    # Page 16: Concession & Opposition Nuancée
    pages[16] = {
        "page": 16,
        "type": "checklist",
        "title": "B2 Grammar: Concession & Opposition Nuancée",
        "subtitle": "Mastering Quoique, Bien que, Avoir beau, and Tout... que",
        "badge_num": "15",
        "intro": "Concession is the cornerstone of advanced dialectical thought. Contrast facts and acknowledge limitations with elegance.",
        "sections": [
            {
                "title": "1. Concession with Subjunctive & Avoir Beau",
                "items": [
                    "Bien que / Quoique (+ Subjonctif): « Bien que ce projet soit ambitieux, il présente des faiblesses évidentes. »",
                    "Avoir beau (+ Infinitif: no matter how much / in vain): « J'ai beau chercher, je ne trouve aucune erreur dans ce bilan. »",
                    "En dépit de / Malgré (+ Nom): « En dépit des protestations syndicales, le conseil d'administration a voté le texte. »",
                    "Tout... que / Quelque... que (+ Subjonctif): « Tout compétent qu'il soit, il a commis une faute de jugement majeure. »"
                ]
            },
            {
                "title": "2. Nuanced Opposition Connectors",
                "items": [
                    "Loin de (+ Infinitif): « Loin de résoudre la crise, cette décision n'a fait qu'accentuer la discorde. »",
                    "Non pas que (+ Subjonctif): « Non pas que je sois opposé au changement, mais la méthode me semble inadéquate. »",
                    "Tandis que / Alors que (contrasting two realities): « Les profits ont augmenté alors que les salaires ont stagné. »",
                    "Par contre vs En revanche: prefer en revanche in formal written essays (par contre is colloquial)."
                ]
            }
        ]
    }

    # Page 17: Concordance des Temps Complexe & Discours Rapporté
    pages[17] = {
        "page": 17,
        "type": "checklist",
        "title": "B2 Grammar: Concordance des Temps Complexe",
        "subtitle": "Advanced Reported Speech and Polyphonic Narrative Discourse",
        "badge_num": "16",
        "intro": "Manage complex polyphonic narratives and reported speech across multi-layered past timeframes.",
        "sections": [
            {
                "title": "1. Complex Indirect Speech Transitions",
                "items": [
                    "Preserve conditional forms without modification: Il disait : « Je viendrais si je pouvais » → Il disait qu'il viendrait s'il pouvait.",
                    "Preserve past subjunctive: Il déplorait : « Je regrette qu'il soit parti » → Il déplorait qu'il fût parti / soit parti.",
                    "Free indirect discourse (Discours indirect libre): blending character's thoughts directly into third-person narration.",
                    "Varied reporting verbs: contester, insinuer, concéder, déplorer, objecter, rétorquer, préconiser."
                ]
            },
            {
                "title": "2. Temporal Perspective and Modal Attributions",
                "items": [
                    "Expressing future from a past perspective: conditionnel présent acts as 'future in the past'.",
                    "Expressing completed future from a past perspective: conditionnel passé acts as 'futur antérieur in the past'.",
                    "Reported questions with indirect interrogatives: « Je me demande ce qu'il adviendra de cette initiative. »",
                    "Attributing quotes ethically in synthesis: using neutral attributive formulas like « selon l'auteur », « d'après les analystes »."
                ]
            }
        ]
    }

    # Page 18: L'Argumentation & Les Connecteurs Rhétoriques
    pages[18] = {
        "page": 18,
        "type": "checklist",
        "title": "B2 Grammar: Connecteurs Rhétoriques d'Argumentation",
        "subtitle": "Structuring a Complex Dialectical Argument (Thèse, Antithèse, Synthèse)",
        "badge_num": "17",
        "intro": "Deploy high-level rhetorical signposts to build bulletproof arguments and guide your readers through complex essays.",
        "sections": [
            {
                "title": "1. Introducing and Classifying Arguments",
                "items": [
                    "D'une part... d'autre part... (on one hand... on the other hand...): balancing dual considerations.",
                    "Non seulement... mais encore / mais aussi: « Non seulement cela stimule l'économie, mais cela protège l'environnement. »",
                    "En premier lieu... ensuite... enfin... (hierarchical logical ordering).",
                    "Quant à / Pour ce qui est de (as for): directing the reader's focus toward a specific dimension."
                ]
            },
            {
                "title": "2. Refutation, Concession and Synthesis Markers",
                "items": [
                    "Certes... néanmoins... (conceding a point before refuting it with stronger evidence).",
                    "Force est de constater que... (one is forced to acknowledge that...): stating an undeniable reality.",
                    "Il n'en demeure pas moins que... (the fact remains that...): anchoring the core truth after a concession.",
                    "Au terme de cette analyse / En dernière analyse: introducing the final synthesis and balanced verdict."
                ]
            }
        ]
    }

    # Page 19: Registres de Langue & Stylistique Française
    pages[19] = {
        "page": 19,
        "type": "checklist",
        "title": "B2 Grammar: Registres de Langue & Stylistique",
        "subtitle": "Mastering Elevated Style (Soutenu) and Avoiding Register Clashes",
        "badge_num": "18",
        "intro": "At B2, you master the elevated register (registre soutenu) and avoid mixing colloquial words into formal academic writing.",
        "sections": [
            {
                "title": "1. Lexical Elevation (Courant to Soutenu)",
                "items": [
                    "le problème → la problématique, l'écueil, l'impasse, le dilemme.",
                    "important → primordial, capital, déterminant, incontournable.",
                    "montrer → mettre en exergue, illustrer, mettre en lumière, attester.",
                    "causer / provoquer → engendrer, susciter, induire, occasionner.",
                    "changer → modifier, bouleverser, infléchir, métamorphoser."
                ]
            },
            {
                "title": "2. Stylistic Devices & Concordance Discipline",
                "items": [
                    "Avoid vague fillers: eliminate « il y a », « c'est bien », « c'est mauvais » from argumentative essays.",
                    "Use active, transitive verbs instead of nominal crutches: prefer « cette mesure stimulera l'emploi » over « cela aura un impact sur ».",
                    "Maintain register consistency throughout a single text (never place familiar slang inside a formal petition).",
                    "Punctuation discipline: semicolons to separate balanced antitheses; em-dashes for parenthetical commentary."
                ]
            }
        ]
    }

    # Pages 20-29: Thematic Vocabulary Modules (Tables with 10 rows)
    # Page 20: Bioethics, Genetics & Medical Technology
    pages[20] = {
        "page": 20,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Bioethics & Medical Technology",
        "subtitle": "Genetics, Assisted Reproduction, Euthanasia & Ethical Boards",
        "badge_num": "19",
        "intro": "Specialized vocabulary to debate complex bioethical dilemmas, genetic engineering, and palliative care policies.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le génie génétique", "n.m.", "genetic engineering", "« Le génie génétique offre des perspectives thérapeutiques révolutionnaires mais controversées. »"],
                ["la procréation médicalement assistée (PMA)", "n.f.", "assisted reproduction", "« La législation sur la PMA pour toutes a suscité de vifs débats parlementaires. »"],
                ["l'euthanasie / la fin de vie", "n.f.", "euthanasia / end of life", "« Les conventions citoyennes se sont penchées sur l'encadrement légal de la fin de vie. »"],
                ["le principe de précaution", "n.m.", "precautionary principle", "« Les scientifiques invoquent le principe de précaution avant d'autoriser ce traitement. »"],
                ["les soins palliatifs", "n.m.pl.", "palliative care", "« Le développement des soins palliatifs est indispensable pour soulager la souffrance. »"],
                ["le don d'organes", "n.m.", "organ donation", "« La loi française repose sur le consentement présumé en matière de don d'organes. »"],
                ["le séquençage génomique", "n.m.", "genome sequencing", "« Le séquençage génomique permet de personnaliser les thérapies anticancéreuses. »"],
                ["l'acharnement thérapeutique", "n.m.", "futile medical obstinacy", "« Le corps médical doit éviter tout acharnement thérapeutique déraisonnable. »"],
                ["l'expérimentation animale", "n.f.", "animal testing", "« Les laboratoires cherchent des alternatives éthiques à l'expérimentation animale. »"],
                ["le comité d'éthique", "n.m.", "ethics committee / board", "« Le comité consultatif d'éthique a rendu un avis très nuancé sur cette innovation. »"]
            ]
        }
    }

    # Page 21: Artificial Intelligence, Algorithms & Digital Surveillance
    pages[21] = {
        "page": 21,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: AI & Digital Surveillance",
        "subtitle": "Machine Learning, Facial Recognition, Biases & Data Sovereignty",
        "badge_num": "20",
        "intro": "Debate the societal impact of artificial intelligence, algorithm accountability, and digital surveillance.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'apprentissage automatique", "n.m.", "machine learning", "« L'apprentissage automatique permet aux modèles de s'améliorer sans programmation explicite. »"],
                ["la reconnaissance faciale", "n.f.", "facial recognition", "« L'usage de la reconnaissance faciale dans l'espace public menace les libertés civiles. »"],
                ["le biais algorithmique", "n.m.", "algorithmic bias", "« Les concepteurs doivent veiller à éliminer tout biais algorithmique discriminatoire. »"],
                ["la souveraineté numérique", "n.f.", "digital sovereignty", "« L'Union européenne cherche à bâtir une véritable souveraineté numérique face aux GAFAM. »"],
                ["la surveillance de masse", "n.f.", "mass surveillance", "« Les révélations des lanceurs d'alerte ont mis au jour un système de surveillance de masse. »"],
                ["l'automatisation", "n.f.", "automation", "« L'automatisation accrue de l'industrie transforme la nature même des qualifications requises. »"],
                ["la désinformation", "n.f.", "disinformation / info warfare", "« Les usines à clics diffusent de la désinformation pour déstabiliser les scrutins électoraux. »"],
                ["le chiffrement des données", "n.m.", "data encryption", "« Le chiffrement de bout en bout garantit l'inviolabilité des communications privées. »"],
                ["le droit à l'oubli", "n.m.", "right to be forgotten", "« Le droit à l'oubli numérique permet d'exiger l'effacement de données obsolètes. »"],
                ["l'éthique de l'IA", "n.f.", "AI ethics / governance", "« Les experts internationaux réclament une charte contraignante sur l'éthique de l'IA. »"]
            ]
        }
    }

    # Page 22: Geopolitics, Globalization & International Relations
    pages[22] = {
        "page": 22,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Geopolitics & Globalization",
        "subtitle": "Multilateral Treaties, Diplomacy, Sanctions & Sovereignty",
        "badge_num": "21",
        "intro": "Analyze world affairs, international diplomacy, multilateral alliances, and economic globalization.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le multilatéralisme", "n.m.", "multilateralism", "« Le multilatéralisme demeure indispensable pour relever les défis planétaires comme le climat. »"],
                ["le traité international", "n.m.", "international treaty", "« Les pays signataires ont ratifié le traité international sur la non-prolifération nucléaire. »"],
                ["les sanctions économiques", "n.f.pl.", "economic sanctions", "« Les sanctions économiques ciblées visent à asphyxier le financement des conflits armés. »"],
                ["la délocalisation", "n.f.", "offshoring / outsourcing", "« La délocalisation des usines vers des pays à bas coûts a fragilisé le tissu industriel local. »"],
                ["le protectionnisme", "n.m.", "protectionism", "« Certaines puissances adoptent des mesures protectionnistes pour protéger leur marché intérieur. »"],
                ["l'hégémonie culturelle", "n.f.", "cultural hegemony", "« La défense de l'exception culturelle française vise à contrecarrer l'hégémonie américaine. »"],
                ["le cessez-le-feu", "n.m.", "ceasefire / truce", "« Les diplomates de l'ONU négocient ardemment un cessez-le-feu immédiat et pérenne. »"],
                ["la diplomatie d'influence", "n.f.", "soft power / diplomacy", "« La gastronomie et la Francophonie sont les fers de lance de la diplomatie d'influence. »"],
                ["le droit d'ingérence", "n.m.", "right of humanitarian intervention", "« La notion de droit d'ingérence humanitaire fait l'objet de vives controverses juridiques. »"],
                ["l'interdépendance", "n.f.", "interdependence", "« La crise sanitaire mondiale a mis en lumière l'extrême interdépendance des économies. »"]
            ]
        }
    }

    # Page 23: Economics, Finance & Sustainable Business Models
    pages[23] = {
        "page": 23,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Economics & Sustainable Models",
        "subtitle": "Inflation, Fiscal Policies, Degrowth & Corporate Responsibility",
        "badge_num": "22",
        "intro": "Debate macroeconomic trends, corporate social responsibility (RSE), and alternative economic indicators.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le produit intérieur brut (PIB)", "n.m.", "gross domestic product (GDP)", "« Les économistes s'accordent à dire que le PIB ne mesure pas le bien-être réel des populations. »"],
                ["la responsabilité sociétale (RSE)", "n.f.", "corporate social responsibility", "« Les grandes entreprises doivent publier un bilan annuel de leur politique RSE. »"],
                ["la décroissance", "n.f.", "degrowth", "« Les partisans de la décroissance préconisent une réduction volontaire de la consommation globale. »"],
                ["l'évasion fiscale", "n.f.", "tax evasion / dodging", "« La lutte contre l'évasion fiscale internationale permettrait de renflouer les finances publiques. »"],
                ["le pouvoir d'achat", "n.m.", "purchasing power", "« La hausse généralisée de l'inflation pèse lourdement sur le pouvoir d'achat des ménages. »"],
                ["la bulle spéculative", "n.f.", "speculative bubble", "« L'éclatement de la bulle spéculative immobilière a provoqué une récession majeure. »"],
                ["l'investissement socialement responsable", "n.m.", "socially responsible investing", "« Les épargnants se tournent de plus en plus vers des fonds d'investissement éthiques. »"],
                ["la dette souveraine", "n.f.", "sovereign debt", "« Le remboursement de la dette souveraine constitue un défi budgétaire pour de nombreux États. »"],
                ["la précarité énergétique", "n.f.", "energy poverty", "« L'isolation thermique des bâtiments est une priorité pour lutter contre la précarité énergétique. »"],
                ["l'économie sociale et solidaire", "n.f.", "social and solidarity economy", "« L'économie sociale et solidaire réinvestit ses excédents au service du projet collectif. »"]
            ]
        }
    }

    # Page 24: Political Systems, Democratic Institutions & Protests
    pages[24] = {
        "page": 24,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Politics, Democracy & Protests",
        "subtitle": "Parliamentary Debates, Civil Disobedience & Civic Rights",
        "badge_num": "23",
        "intro": "Vocabulary to discuss political reforms, constitutional law, social protests, and citizen referendums.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la séparation des pouvoirs", "n.f.", "separation of powers", "« La séparation des pouvoirs entre exécutif, législatif et judiciaire prévient tout abus autoritaire. »"],
                ["la désobéissance civile", "n.f.", "civil disobedience", "« Les militants écologistes assument des actes de désobéissance civile non violente. »"],
                ["le référendum d'initiative citoyenne", "n.m.", "citizen-initiated referendum", "« L'introduction du référendum d'initiative citoyenne permettrait d'accroître la participation. »"],
                ["la motion de censure", "n.f.", "motion of no confidence", "« L'opposition a déposé une motion de censure pour tenter de renverser le gouvernement. »"],
                ["la représentativité", "n.f.", "representativeness", "« Le mode de scrutin proportionnel vise à améliorer la représentativité des minorités politiques. »"],
                ["la laïcité", "n.f.", "secularism / neutrality", "« La laïcité garantit la liberté de conscience et la neutralité de l'État envers toutes les religions. »"],
                ["l'abstentionnisme", "n.m.", "voter abstention", "« La hausse préoccupante de l'abstentionnisme électoral fragilise la légitimité des élus. »"],
                ["la décentralisation", "n.f.", "decentralization", "« La décentralisation transfère des compétences décisionnelles de l'État central vers les régions. »"],
                ["le contre-pouvoir", "n.m.", "counter-power / check", "« La presse indépendante et la justice constituent des contre-pouvoirs indispensables. »"],
                ["l'engagement militant", "n.m.", "activist engagement", "« L'engagement militant des jeunes prend aujourd'hui la forme de mobilisations numériques et de marches. »"]
            ]
        }
    }

    # Page 25: Ecology, Biodiversity Crisis & Energy Transition
    pages[25] = {
        "page": 25,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Ecology & Energy Transition",
        "subtitle": "Climate Crises, Agroecology, Carbon Neutrality & Ecosystems",
        "badge_num": "24",
        "intro": "Debate ecological crises, nuclear vs renewable energy, carbon taxation, and biodiversity preservation.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la neutralité carbone", "n.f.", "carbon neutrality", "« Atteindre la neutralité carbone d'ici 2050 implique de décarboner totalement l'industrie. »"],
                ["l'effondrement de la biodiversité", "n.m.", "biodiversity collapse", "« L'effondrement de la biodiversité végétale et animale met en péril l'équilibre des écosystèmes. »"],
                ["la taxe carbone", "n.f.", "carbon tax", "« Une taxe carbone équitable doit s'accompagner d'aides ciblées pour les ménages les plus modestes. »"],
                ["l'agroécologie", "n.f.", "agroecology / organic farming", "« L'agroécologie favorise les régulations naturelles pour produire sans intrants chimiques toxiques. »"],
                ["le mix énergétique", "n.m.", "energy mix", "« Le débat national porte sur la part du nucléaire et des énergies renouvelables dans le mix énergétique. »"],
                ["la déforestation massive", "n.f.", "mass deforestation", "« La déforestation massive en Amazonie détruit l'un des principaux puits de carbone planétaires. »"],
                ["l'éco-anxiété", "n.f.", "eco-anxiety", "« L'éco-anxiété touche de nombreux adolescents face aux prévisions alarmantes des climatologues. »"],
                ["le verdissement d'image (greenwashing)", "n.m.", "greenwashing", "« Les associations écologistes dénoncent le greenwashing des multinationales polluantes. »"],
                ["la résilience climatique", "n.f.", "climate resilience", "« Les villes côtières doivent renforcer leur résilience climatique face à la montée des océans. »"],
                ["la sobriété énergétique", "n.f.", "energy sobriety / conservation", "« La sobriété énergétique consiste à réduire notre consommation superflue au lieu de produire plus. »"]
            ]
        }
    }

    # Page 26: Philosophy, Human Rights & Social Justice
    pages[26] = {
        "page": 26,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Philosophy & Social Justice",
        "subtitle": "Ethics, Enlightenment Thought, Equality & Human Dignity",
        "badge_num": "25",
        "intro": "Engage with French philosophical traditions, human rights debates, and questions of universalism versus particularism.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'universalisme républicain", "n.m.", "republican universalism", "« L'universalisme républicain postule que tous les citoyens sont égaux sans distinction d'origine. »"],
                ["l'égalité des chances", "n.f.", "equality of opportunity", "« L'école républicaine a pour mission historique d'assurer une véritable égalité des chances. »"],
                ["le déterminisme social", "n.m.", "social determinism", "« Les sociologues analysent comment le déterminisme social influence les choix d'orientation scolaire. »"],
                ["l'aliénation", "n.f.", "alienation", "« Le philosophe décrit l'aliénation de l'individu moderne face à la société de consommation. »"],
                ["la dignité humaine", "n.f.", "human dignity", "« La dignité humaine constitue le principe suprême et inaliénable du droit constitutionnel. »"],
                ["la liberté de conscience", "n.f.", "freedom of conscience", "« La liberté de conscience autorise chacun à croire, à douter ou à ne pas avoir de religion. »"],
                ["l'éthique déontologique", "n.f.", "deontological ethics", "« L'éthique déontologique impose de respecter des devoirs moraux absolus en toutes circonstances. »"],
                ["le contrat social", "n.m.", "social contract", "« Selon Rousseau, le contrat social fonde la souveraineté populaire et la volonté générale. »"],
                ["la solidarité intergénérationnelle", "n.f.", "intergenerational solidarity", "« Le système de retraite par répartition incarne la solidarité intergénérationnelle nationale. »"],
                ["l'émancipation", "n.f.", "emancipation / liberation", "« L'accès universel au savoir demeure le plus formidable vecteur d'émancipation humaine. »"]
            ]
        }
    }

    # Page 27: Contemporary Arts, Literary Critique & Cinema
    pages[27] = {
        "page": 27,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Arts & Literary Critique",
        "subtitle": "Cinematography, Aesthetic Movements, Irony & Artistic Freedom",
        "badge_num": "26",
        "intro": "Analyze contemporary French cinema, literary styles, visual arts, and aesthetic critiques with nuance.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la mise en abyme", "n.f.", "mise en abyme (story within a story)", "« Le réalisateur utilise une mise en abyme virtuose pour interroger le pouvoir de l'illusion. »"],
                ["le courant esthétique", "n.m.", "aesthetic movement", "« Ce roman s'inscrit dans le courant esthétique du nouveau roman expérimental des années 60. »"],
                ["le cinéma d'auteur", "n.m.", "auteur cinema / art house", "« Le cinéma d'auteur français privilégie la vision personnelle et singulière du réalisateur. »"],
                ["la portée allégorique", "n.f.", "allegorical significance", "« La portée allégorique de cette pièce de théâtre fait écho aux tragédies politiques actuelles. »"],
                ["l'art subversif", "n.m.", "subversive art", "« Les artistes de rue créent des œuvres subversives pour contester l'ordre économique établi. »"],
                ["l'audace stylistique", "n.f.", "stylistic boldness", "« Les critiques littéraires ont unanimement salué l'audace stylistique de cette jeune autrice. »"],
                ["la polysémie", "n.f.", "polysemy (multiple meanings)", "« La polysémie de ce poème autorise de multiples lectures et interprétations philosophiques. »"],
                ["l'engagement de l'artiste", "n.m.", "artist's social commitment", "« Sartre soutenait que l'engagement de l'artiste était indispensable face aux dérives du pouvoir. »"],
                ["le clair-obscur", "n.m.", "chiaroscuro (light and shadow)", "« Le directeur de la photographie maîtrise à la perfection l'usage du clair-obscur dramatique. »"],
                ["la catharsis", "n.f.", "catharsis", "« La tragédie grecque visait la catharsis des passions spectaculaires à travers la terreur et la pitié. »"]
            ]
        }
    }

    # Page 28: Sociology, Urban Dynamics & Demographic Shifts
    pages[28] = {
        "page": 28,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Sociology & Urban Dynamics",
        "subtitle": "Gentrification, Social Cohesion, Demography & Suburbs",
        "badge_num": "27",
        "intro": "Vocabulary to discuss urban segregation, gentrification, social mobility, and demographic aging in France.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'embourgeoisement (gentrification)", "n.m.", "gentrification", "« L'embourgeoisement des quartiers populaires repousse les populations modestes en banlieue. »"],
                ["la fracture sociale", "n.f.", "social divide / fracture", "« Les politiques publiques de la ville peinent à résorber la fracture sociale entre métropoles et zones rurales. »"],
                ["l'ascenseur social", "n.m.", "social elevator / mobility", "« Le blocage de l'ascenseur social alimente un sentiment profond de désillusion chez les jeunes diplômés. »"],
                ["le vieillissement démographique", "n.m.", "population aging", "« Le vieillissement démographique pose le défi du financement de la dépendance et des retraites. »"],
                ["la mixité sociale", "n.f.", "social diversity / mixing", "« L'obligation de construire des logements sociaux vise à encourager la mixité sociale urbaine. »"],
                ["l'exode urbain", "n.m.", "urban exodus", "« L'essor du télétravail a stimulé un exode urbain partiel vers les villes moyennes de province. »"],
                ["la précarisation", "n.f.", "casualization / precarity", "« La précarisation de l'emploi touche en premier lieu les jeunes et les travailleurs non qualifiés. »"],
                ["le tissu associatif", "n.m.", "community / NGO fabric", "« Le riche tissu associatif local joue un rôle fondamental de médiation et de soutien scolaire. »"],
                ["le repli identitaire", "n.m.", "communitarian retreat / isolation", "« Les sociologues mettent en garde contre le repli identitaire provoqué par le sentiment d'abandon. »"],
                ["la politique de la ville", "n.f.", "urban revitalization policy", "« La politique de la ville subventionne des projets de réhabilitation urbaine et culturelle. »"]
            ]
        }
    }

    # Page 29: Labor Evolution, Gig Economy & Workplace Psychology
    pages[29] = {
        "page": 29,
        "type": "vocab_table",
        "title": "B2 Thematic Vocabulary: Labor & Workplace Psychology",
        "subtitle": "Gig Economy, Burnout, Meaning at Work & Remote Management",
        "badge_num": "28",
        "intro": "Debate the future of employment, workplace mental health, platform economics, and corporate governance.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'ubérisation de l'économie", "n.f.", "uberization / gig economy", "« L'ubérisation contourne les protections traditionnelles du droit du travail et des conventions collectives. »"],
                ["le travailleur indépendant", "n.m.", "freelancer / contractor", "« De nombreux jeunes professionnels préfèrent le statut de travailleur indépendant pour son autonomie. »"],
                ["l'épuisement professionnel (burn-out)", "n.m.", "workplace burnout", "« Le surmenage et la pression des objectifs numériques conduisent fréquemment à l'épuisement professionnel. »"],
                ["la quête de sens au travail", "n.f.", "search for meaning at work", "« La quête de sens incite certains cadres à quitter les multinationales pour des métiers artisanaux. »"],
                ["le droit à la déconnexion", "n.m.", "right to disconnect", "« Le droit à la déconnexion interdit aux employeurs de solliciter leurs salariés en dehors des heures ouvrées. »"],
                ["le management bienveillant", "n.m.", "supportive management", "« Le management bienveillant améliore à la fois le bien-être au travail et l'efficacité opérationnelle. »"],
                ["le dialogue social", "n.m.", "social dialogue / labor talks", "« La reprise d'un dialogue social loyal est indispensable pour désamorcer le conflit syndical en cours. »"],
                ["la charge mentale", "n.f.", "mental load", "« L'articulation entre vie professionnelle et responsabilités familiales accroît la charge mentale des mères. »"],
                ["le salaire universel", "n.m.", "universal basic income", "« Les partisans du salaire universel affirment qu'il éradiquerait la grande pauvreté économique. »"],
                ["la démission silencieuse (quiet quitting)", "n.f.", "quiet quitting", "« La démission silencieuse traduit le refus des salariés de s'investir au-delà de leurs obligations strictes. »"]
            ]
        }
    }

    # Pages 30-39: Spoken Production & Interaction
    # Page 30: DELF B2 Oral Monologue: Defending an Impromptu Thesis [Respect illustration!]
    pages[30] = {
        "page": 30,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Defending an Impromptu Thesis",
        "subtitle": "Structuring a 4 to 5-Minute DELF B2 Oral Argumentation",
        "badge_num": "29",
        "intro": "Deliver a compelling, structured 5-minute defense of an argumentative thesis based on a short society trigger document.",
        "sections": [
            {
                "title": "1. Introduction Architecture (1 minute)",
                "items": [
                    "Formulate a captivating hook (accroche): reference a recent social event, statistic, or philosophical paradox.",
                    "Present the stimulus document: introduce the source, author, and main controversy without reading long quotes.",
                    "Formulate the central problem statement (problématique): pose an insightful question opening two perspectives.",
                    "Announce your dialectical plan: « Dans un premier temps, j'analyserai... puis j'examinerai... enfin, je proposerai... »"
                ]
            },
            {
                "title": "2. Developing Two Opposing Pillars with Synthesis",
                "items": [
                    "Pillar 1 (Thèse): defend the primary viewpoint with two substantiated arguments and concrete examples.",
                    "Pillar 2 (Antithèse): expose the limitations, hidden risks, or opposing perspective with equal rigor.",
                    "Pillar 3 (Synthèse / Dépassement): reconcile both positions into a balanced, mature policy recommendation.",
                    "Deliver an impactful conclusion: summarize your thesis and open an ethical question for the examiner."
                ]
            }
        ]
    }

    # Page 31: Advanced Argumentation: The Classical Dialectical Plan
    pages[31] = {
        "page": 31,
        "type": "checklist",
        "title": "B2 Speaking Mastery: The Dialectical Plan",
        "subtitle": "Mastering Thèse, Antithèse, and Synthèse in Oral Exams",
        "badge_num": "30",
        "intro": "The dialectical plan (Thèse / Antithèse / Synthèse) is the benchmark of French intellectual argumentation. Master its structure.",
        "sections": [
            {
                "title": "1. Building the Thesis and Antithesis",
                "items": [
                    "Thèse: validate the mainstream benefits: « Il est indéniable que le numérique facilite l'accès au savoir. »",
                    "Introduce compelling data or cultural evidence: cite historical milestones, sociological studies, or legal precedents.",
                    "Antithèse: introduce rigorous objections: « Toutefois, force est de constater que la fracture numérique s'aggrave. »",
                    "Avoid absolute claims: use modal adverbs (vraisemblablement, manifestement, potentiellement) to maintain nuance."
                ]
            },
            {
                "title": "2. The Synthesis (Le Dépassement)",
                "items": [
                    "The synthesis is NOT a lukewarm middle ground; it is a higher-level solution transcending the contradiction.",
                    "Propose systemic criteria: « Dès lors, la question n'est pas de bannir l'outil, mais d'éduquer les citoyens à son usage critique. »",
                    "Balance rights and responsibilities: reconcile individual liberty with collective public welfare.",
                    "Close your oral demonstration with authoritative rhetorical conviction and calm self-assurance."
                ]
            }
        ]
    }

    # Page 32: Impromptu Debate: Rebuttals & Tactful Refutation
    pages[32] = {
        "page": 32,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Impromptu Debate & Rebuttals",
        "subtitle": "Handling Cross-Examination with French Examiners and Peers",
        "badge_num": "31",
        "intro": "In part 2 of DELF B2, the examiner will challenge your arguments. Defend your point of view with poise, tact, and precision.",
        "sections": [
            {
                "title": "1. Countering Fallacies and Hostile Questions",
                "items": [
                    "Reframe leading questions: « Votre remarque est pertinente, mais elle déplace quelque peu le cœur du débat... »",
                    "Highlight logical fallacies: « Ne confondons pas corrélation et causalité dans cette analyse statistique. »",
                    "Concede points gracefully (concession dialectique): « Je vous concède volontiers que cette mesure est coûteuse... »",
                    "Rebound with a stronger imperative: « ...néanmoins, l'inaction écologique coûtera infiniment plus cher à notre société. »"
                ]
            },
            {
                "title": "2. Conversational Assertiveness and Diplomatic Poise",
                "items": [
                    "Maintain eye contact with the examiner and avoid defensive body language during sharp questioning.",
                    "Ask counter-questions to test examiner assumptions: « Comment concilieriez-vous alors cette position avec l'impératif éthique ? »",
                    "Use precise transitions: « Permettez-moi de nuancer votre propos », « C'est précisément pour cette raison que... »",
                    "Show flexibility: acknowledge valid compromises without abandoning your overarching thesis."
                ]
            }
        ]
    }

    # Page 33: Spoken Interaction: Academic & Professional Negotiations
    pages[33] = {
        "page": 33,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Professional Negotiations",
        "subtitle": "Conducting Complex Workplace Negotiations and Academic Defenses",
        "badge_num": "32",
        "intro": "Negotiate contracts, project scopes, budget allocations, and collective agreements in fluent professional French.",
        "sections": [
            {
                "title": "1. Opening Offers and Strategic Framing",
                "items": [
                    "Frame shared objectives: « Notre intérêt commun réside dans la réussite pérenne de ce partenariat stratégique. »",
                    "Establish clear baseline conditions: « Nous sommes disposés à faire des concessions, à condition que le calendrier soit garanti. »",
                    "Reject unacceptable clauses diplomatically: « En l'état actuel des choses, cette clause d'exclusivité est difficilement recevable. »",
                    "Propose phased compromises: « Ne pourrions-nous pas envisager un déploiement échelonné sur deux semestres ? »"
                ]
            },
            {
                "title": "2. Closing the Deal and Solidifying Consensuses",
                "items": [
                    "Summarize points of agreement: « Si je résume notre consensus : vous réduisez les coûts et nous augmentons le volume. »",
                    "Handle remaining sticking points: « Réservons ce dernier point pour une relecture juridique conjointe demain. »",
                    "Maintain a constructive and respectful tone throughout tense financial bargaining.",
                    "Formal handshake and written confirmation: « Je vous ferai parvenir le protocole d'accord récapitulatif d'ici ce soir. »"
                ]
            }
        ]
    }

    # Page 34: Expressing Nuanced Conviction, Irony & Rhetorical Distance
    pages[34] = {
        "page": 34,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Nuanced Conviction & Irony",
        "subtitle": "Deploying Intellectual Wit, Sarcasm, and Critical Distance",
        "badge_num": "33",
        "intro": "Master the art of the French intellectual debate: express sharp opinions with subtle wit, irony, and rhetorical elegance.",
        "sections": [
            {
                "title": "1. Expressing Rhetorical Distance",
                "items": [
                    "Distancing from extreme stances: « Je me garderai bien de verser dans un optimisme béat ou un catastrophisme excessif. »",
                    "Qualifying general statements: « Il serait hâtif d'en déduire que l'ensemble de la profession partage cette analyse. »",
                    "Using modal adverbs for nuanced precision: ostensiblement, paradoxalement, indubitablement, théoriquement.",
                    "Expressing polite reservation: « Permettez-moi de manifester un certain scepticisme quant à la portée réelle de ce décret. »"
                ]
            },
            {
                "title": "2. Sophisticated Irony and Understatement in Debate",
                "items": [
                    "Using dry irony to disarm weak arguments: « Quelle surprise de constater que cette étude a été financée par l'industrie pétrolière ! »",
                    "Litote as intellectual elegance: « Ce n'est pas le moindre des paradoxes de notre politique énergétique. »",
                    "Exposing double standards: « On s'inquiète de la dette publique tout en exonérant d'impôts les plus grandes fortunes. »",
                    "Concluding with a punchy aphorism that leaves a memorable impression on your listeners."
                ]
            }
        ]
    }

    # Page 35: Public Speaking: Modulating Delivery & Cadence
    pages[35] = {
        "page": 35,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Public Speaking & Rhetorical Cadence",
        "subtitle": "Pacing, Pauses, Eye Contact & Voice Inflexions for Maximum Impact",
        "badge_num": "34",
        "intro": "Transform your speech from grammatically correct French into a persuasive, charismatic public delivery.",
        "sections": [
            {
                "title": "1. Mastering Rhetorical Pauses (Le Silence Rhétorique)",
                "items": [
                    "Pause for 2 seconds after asking a rhetorical question to allow the audience to anticipate your answer.",
                    "Lower your volume slightly when delivering a profound insight to command complete room attention.",
                    "Vary tempo: accelerate during compelling narrative sequences; slow down during key statistical definitions.",
                    "Avoid vocal filler crutches (« euh », « genre », « voilà ») by replacing hesitation with clean silence."
                ]
            },
            {
                "title": "2. Body Language & Eye Contact in French Debates",
                "items": [
                    "Maintain steady, assertive eye contact with both examiners; do not stare down at your notes.",
                    "Use open hand gestures to emphasize balanced comparisons (left hand for thèse, right hand for antithèse).",
                    "Keep your posture tall and relaxed, projecting your voice from the diaphragm with clear resonance.",
                    "Smile authentically when greeting the examination jury and concluding your presentation."
                ]
            }
        ]
    }

    # Page 36: French Advanced Phonetics: Liaison Interdite vs Facultative
    pages[36] = {
        "page": 36,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Advanced French Phonetics",
        "subtitle": "Mandatory, Forbidden & Optional Liaisons in Elevated French",
        "badge_num": "35",
        "intro": "Master the strict rules of French liaison to sound educated and natural in both formal speeches and everyday discussions.",
        "sections": [
            {
                "title": "1. Forbidden Liaisons (Liaisons Interdites - NEVER Make These)",
                "items": [
                    "After the conjunction 'et' (and): NEVER pronounce liaison between 'et' and the next vowel (« et / alors »).",
                    "After a singular noun ending in consonant: « un chat / intelligent » (never pronounce the 't').",
                    "Before an aspirated 'h' (h aspiré): « les / héros », « en / haut » (making liaison here is a glaring error).",
                    "Between inverted verb-subject and complement: « Sont-ils / allés ? », « Ont-ils / accepté ? »"
                ]
            },
            {
                "title": "2. Optional Liaisons in Elevated Style (Liaisons Facultatives)",
                "items": [
                    "After plural nouns in formal speech: « des débats_intéressants », « des lois_injustes » (pronounce 'z').",
                    "After auxiliary verbs: « ils sont_arrivés », « nous avons_obtenu » (adds formal polish).",
                    "After monosyllabic adverbs: « trop_aimable », « bien_entendu », « plus_amplement ».",
                    "In casual speech, optional liaisons are dropped; in DELF B2 formal monologues, adopting some adds elegance."
                ]
            }
        ]
    }

    # Page 37: Colloquial vs Standard vs Elevated Registers in Debate
    pages[37] = {
        "page": 37,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Navigating Three Registers",
        "subtitle": "Knowing When to Shift from Familier to Courant and Soutenu",
        "badge_num": "36",
        "intro": "At B2, you effortlessly switch between registers according to the social setting, without mixing incompatible levels.",
        "sections": [
            {
                "title": "1. Recognizing and Avoiding Inappropriate Slang",
                "items": [
                    "Familiar terms to strictly avoid in formal exams: un flic (un policier), du pognon (de l'argent), un mec (un homme).",
                    "Avoid truncated words in academic essays: la télé (la télévision), la pub (la publicité), la fac (l'université).",
                    "Watch out for colloquial syntax: never omit 'ne' in negation during formal DELF presentations.",
                    "Avoid overly casual conversation openers: use « Bonjour Madame, Monsieur » instead of « Salut ! »"
                ]
            },
            {
                "title": "2. Adopting Elevated Vocabulary and Phrasing (Soutenu)",
                "items": [
                    "Use precise modal formulas: « Auriez-vous l'obligeance de... », « Il appert que cette décision... »",
                    "Use inverted subjunctive for concessions: « Fût-ce au détriment de nos intérêts immédiats... »",
                    "Deploy refined verbs: obvier, pallier (without 'à'), pérenniser, endiguer, exacerber, susciter.",
                    "Match your register to the examiner: standard fluent conversational tone for dialogue; polished elevated style for synthesis."
                ]
            }
        ]
    }

    # Page 38: Rhetorical Idioms, Proverbs & Cultural Allusions in Debate
    pages[38] = {
        "page": 38,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Rhetorical Idioms & Allusions",
        "subtitle": "Weaving Cultural Proverbs and Historical Allusions into Debate",
        "badge_num": "37",
        "intro": "French intellectual discourse is steeped in historical, literary, and philosophical proverbs. Deploy them strategically.",
        "sections": [
            {
                "title": "1. Classical Rhetorical Idioms",
                "items": [
                    "« L'arbre qui cache la forêt »: focusing on a minor controversy while ignoring the systemic crisis.",
                    "« Le jeu n'en vaut pas la chandelle »: the prospective benefits do not justify the risks or financial costs.",
                    "« Remettre les pendules à l'heure »: setting the record straight and dispelling misconceptions.",
                    "« Faire la part des choses »: distinguishing between valid complaints and exaggerated emotional claims.",
                    "« Mettre la charrue avant les bœufs »: rushing to implement solutions before diagnosing the root cause."
                ]
            },
            {
                "title": "2. Cultural & Literary Allusions",
                "items": [
                    "« Un combat de David contre Goliath »: referring to small citizen associations taking on corporate giants.",
                    "« Le tonneau des Danaïdes »: describing endless public spending without measurable results.",
                    "« Ouvrir la boîte de Pandore »: warning that passing an ambiguous law will unleash unforeseen crises.",
                    "« Le mythe de Sisyphe »: referencing Camus to discuss repetitive, absurd bureaucratic tasks."
                ]
            }
        ]
    }

    # Page 39: Fast Conversational Turns & Active Interventions
    pages[39] = {
        "page": 39,
        "type": "checklist",
        "title": "B2 Speaking Mastery: Fast Conversational Turns",
        "subtitle": "Claiming the Floor, Managing Interruptions & Active Listening",
        "badge_num": "38",
        "intro": "Take an active role in fast group conversations: claim the floor confidently, redirect debates, and summarize consensus.",
        "sections": [
            {
                "title": "1. Intervening with Authority and Politeness",
                "items": [
                    "Claim the floor smoothly: « Si je puis me permettre d'intervenir à ce stade de la discussion... »",
                    "Refocus after an interruption: « Pour en revenir au cœur de notre échange, laissez-moi souligner que... »",
                    "Handle aggressive interruptions: « Je vous ai écouté sans vous couper la parole, accordez-moi la même courtoisie. »",
                    "Bridge contrasting opinions: « Nous avons deux visions divergentes sur la table : comment pouvons-nous les concilier ? »"
                ]
            },
            {
                "title": "2. Driving Group Consensus",
                "items": [
                    "Synthesize scattered ideas: « Ce qui ressort de nos débats, c'est une volonté unanime d'agir sur le long terme. »",
                    "Propose a vote or resolution: « Je suggère que nous arrêtions notre choix sur la proposition de compromis. »",
                    "Express institutional appreciation: « Je tiens à saluer la franchise et la haute tenue de nos débats d'aujourd'hui. »",
                    "Leave no unaddressed objections: verify that every participant feels heard before concluding."
                ]
            }
        ]
    }

    # Pages 40-49: Listening Comprehension
    # Page 40: Broadcast Radio Debates & Investigative Reports (France Culture)
    pages[40] = {
        "page": 40,
        "type": "checklist",
        "title": "B2 Listening Mastery: Broadcast Radio & Investigations",
        "subtitle": "Understanding France Culture, France Inter, and Investigative Podcasts",
        "badge_num": "39",
        "intro": "Follow fast, intellectually demanding audio documentaries, investigative radio, and cultural broadcasts.",
        "sections": [
            {
                "title": "1. Anatomy of In-Depth Radio Investigations",
                "items": [
                    "Follow investigative storytelling blending field recordings, phone taps, archive audio, and commentary.",
                    "Identify subtle editorial stances woven into narrator voiceover and ironic musical cues.",
                    "Extract precise numbers, dates, and names of shell corporations or legal entities under scrutiny.",
                    "Synthesize the overarching geopolitical or corporate malfeasance exposed by the investigation."
                ]
            },
            {
                "title": "2. Academic Panels on France Culture",
                "items": [
                    "Follow roundtables where historians, sociologists, and economists debate abstract concepts at rapid speed.",
                    "Understand complex theoretical frameworks (structuralism, neoliberalism, post-colonialism) explained orally.",
                    "Track philosophical disagreements where participants challenge each other's foundational premises.",
                    "Take organized, structured notes capturing the core dialectical progression of the academic exchange."
                ]
            }
        ]
    }

    # Page 41: Academic Conferences & Keynote Lectures
    pages[41] = {
        "page": 41,
        "type": "checklist",
        "title": "B2 Listening Mastery: Academic Conferences & Lectures",
        "subtitle": "Following University Keynotes, Colloquiums & Scientific Symposia",
        "badge_num": "40",
        "intro": "Listen to formal university lectures and research symposiums, following complex academic argumentation with ease.",
        "sections": [
            {
                "title": "1. Tracking Formal Lecture Architecture",
                "items": [
                    "Identify the lecturer's research hypothesis presented in the introductory preamble.",
                    "Follow empirical demonstrations: laboratory data, comparative field studies, and methodology explanations.",
                    "Recognize theoretical objections anticipated and answered preemptively by the speaker.",
                    "Capture the concluding synthesis outlining future avenues for scientific or historical inquiry."
                ]
            },
            {
                "title": "2. Q&A Sessions and Academic Critiques",
                "items": [
                    "Understand technical questions posed by peer researchers in the audience during post-lecture Q&A.",
                    "Follow delicate rhetorical sparring between competing academic schools of thought.",
                    "Identify when a researcher concedes limitations in their data or calls for further empirical validation.",
                    "Synthesize the broader societal implications of the academic discovery announced."
                ]
            }
        ]
    }

    # Page 42: Political Interviews: Detecting Spin & Rhetorical Posturing
    pages[42] = {
        "page": 42,
        "type": "checklist",
        "title": "B2 Listening Mastery: Political Interviews & Media Spin",
        "subtitle": "Detecting Evasions, Media Training, and Rhetorical Deflection",
        "badge_num": "41",
        "intro": "Deconstruct political interviews: spot when an interviewee sidesteps questions, changes the topic, or uses pre-packaged talking points.",
        "sections": [
            {
                "title": "1. Identifying Evasion Techniques (Langue de Bois)",
                "items": [
                    "Answering a different question: pivoting from budget deficits to patriotic achievements.",
                    "Using passive nominalizations to avoid assigning blame: « Des erreurs ont été commises » instead of « J'ai commis une erreur ».",
                    "Counter-attacking the interviewer's motives: « Votre question est biaisée et ne reflète pas les attentes des Français. »",
                    "Spotting empty platitudes (truismes): stating obvious generalities to avoid committing to policy specifics."
                ]
            },
            {
                "title": "2. Analyzing Hardball Journalistic Techniques",
                "items": [
                    "Repeated questioning: journalist asking the exact same question three times until a concrete answer is given.",
                    "Quoting past contradictory statements: confronting the politician with their own recorded words from two years ago.",
                    "Using verified third-party statistics to dismantle political claims live on air.",
                    "Evaluating the politician's emotional composure: detecting defensiveness, irritation, or performative warmth."
                ]
            }
        ]
    }

    # Page 43: Complex Cultural Documentaries & Philosophical Debates
    pages[43] = {
        "page": 43,
        "type": "checklist",
        "title": "B2 Listening Mastery: Documentaries & Philosophy",
        "subtitle": "Understanding Historical Archives, Art Analysis & Philosophical Talks",
        "badge_num": "42",
        "intro": "Understand rich cultural documentaries broadcast on Arte and France Télévisions with full aesthetic appreciation.",
        "sections": [
            {
                "title": "1. Historical and Archival Audio",
                "items": [
                    "Follow historical audio recordings from the 1940s to 1980s with older microphone technology and accents.",
                    "Understand wartime speeches (De Gaulle, Churchill in French) and resistance radio messages.",
                    "Follow voiceover narration describing complex geopolitical treaties, military campaigns, and diplomatic crises.",
                    "Contrast primary source witness testimonies with modern retrospective historical analysis."
                ]
            },
            {
                "title": "2. Philosophical and Aesthetic Reflections",
                "items": [
                    "Understand philosophical monologues on the nature of memory, identity, time, and artistic beauty.",
                    "Follow curators explaining the artistic choices, lighting, and composition of modern art installations.",
                    "Detect subtle allegorical interpretations connecting classical literature with modern societal angst.",
                    "Extract inspiring quotes and philosophical axioms for your own argumentative essays."
                ]
            }
        ]
    }

    # Page 44: Fast Multi-Speaker Panel Discussions
    pages[44] = {
        "page": 44,
        "type": "checklist",
        "title": "B2 Listening Mastery: Multi-Speaker Panel Discussions",
        "subtitle": "Tracking Overlapping Speech, Cacophony & Sudden Debates",
        "badge_num": "43",
        "intro": "Maintain comprehension during fiery French television talk shows where guests interrupt and talk over each other.",
        "sections": [
            {
                "title": "1. Anchoring During Cacophonous Exchanges",
                "items": [
                    "Focus on the dominant voice carrying the argumentative burden when two participants shout simultaneously.",
                    "Track the moderator's bell or verbal intervention: « S'il vous plaît, un à la fois, le public ne comprend rien ! »",
                    "Identify non-verbal cues: sarcastic laughter, sighs, desk tapping, and facial exasperation.",
                    "Synthesize the competing positions once the commotion settles and each speaker restates their thesis."
                ]
            },
            {
                "title": "2. Analyzing Emotional Escalation and Conflict Resolution",
                "items": [
                    "Notice when an ideological disagreement turns into a personal ad hominem attack.",
                    "Track how seasoned debaters defuse tension using humor, self-deprecation, or a sudden change of register.",
                    "Identify points where polarized debaters unexpectedly discover shared values or mutual concerns.",
                    "Evaluate which debater scored the decisive rhetorical victory based on composure and factual grounding."
                ]
            }
        ]
    }

    # Page 45: Global Francophone Varieties & Literary Accents
    pages[45] = {
        "page": 45,
        "type": "checklist",
        "title": "B2 Listening Mastery: Global Francophone Accents",
        "subtitle": "Audio Comprehension across Quebec, North Africa, and West Africa",
        "badge_num": "44",
        "intro": "Appreciate the rich acoustic diversity of French spoken in Montreal, Dakar, Geneva, Brussels, and Algiers.",
        "sections": [
            {
                "title": "1. North American & Caribbean Francophonie",
                "items": [
                    "Quebec French in media: following Radio-Canada news broadcasts, political debates, and cultural documentaries.",
                    "Understanding Quebec colloquial register (joual) versus standard Radio-Canada international pronunciation.",
                    "Haitian and Antillean French: distinct melodic cadence, vowel nasalization, and rich creole loanwords.",
                    "Recognizing regional North American idiomatic expressions in cinema dialogue and interviews."
                ]
            },
            {
                "title": "2. African & Maghrebian Francophonie",
                "items": [
                    "North African French (Maghreb): clear dental consonants, rapid cadence, and Arabic-influenced idioms.",
                    "Sub-Saharan African French (Senegal, Ivory Coast, Congo): vibrant oratorical style, formal respect, and proverbs.",
                    "Understanding literary interviews with major African writers (Alain Mabanckou, Fatou Diome).",
                    "Embracing global Francophone expressions that enrich the French language worldwide."
                ]
            }
        ]
    }

    # Page 46: Catching Subtext, Implicit Critique & Satire
    pages[46] = {
        "page": 46,
        "type": "checklist",
        "title": "B2 Listening Mastery: Subtext, Irony & Satire",
        "subtitle": "Decoding Le Canard Enchaîné Style Humor, Sarcasm & Understatement",
        "badge_num": "45",
        "intro": "French humor relies heavily on double entendres, satire, and deadpan irony. Master the ability to catch what is left unsaid.",
        "sections": [
            {
                "title": "1. Deciphering Satirical Comedy & Radio Chronicles",
                "items": [
                    "Follow morning humorists on France Inter (humorous chronicles dissecting political follies).",
                    "Understand parodies where the satirist adopts the voice and flaws of a public figure in character.",
                    "Spot hyperbolic exaggeration used to expose the absurdity of a newly proposed law.",
                    "Detect the critical boundary between gentle humor, biting satire, and serious journalistic condemnation."
                ]
            },
            {
                "title": "2. Identifying Implicit Criticism in Polite Speech",
                "items": [
                    "Understand diplomatic critiques disguised as faint praise: « C'est une démarche pour le moins courageuse... » (it's suicidal).",
                    "Spot veiled skepticism in tone of voice: a slight pause before an adjective signaling profound doubt.",
                    "Understand passive-aggressive workplace compliments: « Félicitations pour ce travail, qui a au moins le mérite d'exister. »",
                    "React appropriately to subtle humor in social and professional gatherings with French peers."
                ]
            }
        ]
    }

    # Page 47: Analyzing Argumentative Fallacies in Spoken French
    pages[47] = {
        "page": 47,
        "type": "checklist",
        "title": "B2 Listening Mastery: Spotting Argumentative Fallacies",
        "subtitle": "Detecting False Dilemmas, Ad Hominem Attacks & Slippery Slopes",
        "badge_num": "46",
        "intro": "Sharpen your critical listening skills by identifying dishonest rhetorical tricks and logical fallacies in live debates.",
        "sections": [
            {
                "title": "1. Classic Fallacies in French Political Discourse",
                "items": [
                    "L'attaque ad hominem: attacking the opponent's character or wealth instead of addressing their argument.",
                    "Le faux dilemme: presenting only two extreme options (« C'est la réforme ou le chaos économique »).",
                    "La pente savonneuse (slippery slope): claiming that one modest change will inevitably lead to total catastrophe.",
                    "L'épouvantail (straw man): caricaturing the opponent's position to make it easy to knock down."
                ]
            },
            {
                "title": "2. Emotional and Statistical Manipulation",
                "items": [
                    "L'appel à l'émotion: using tragic individual anecdotes to distract from broader statistical realities.",
                    "L'argument d'autorité: claiming something must be true simply because an unnamed expert allegedly said so.",
                    "Generalizations from unrepresentative samples: « Tout le monde sait bien que... », « Les Français en ont assez de... »",
                    "Mentally categorizing these fallacies during DELF B2 listening tasks to answer critical analysis questions."
                ]
            }
        ]
    }

    # Page 48: High-Speed Spoken French: Reduced Pronunciations
    pages[48] = {
        "page": 48,
        "type": "checklist",
        "title": "B2 Listening Mastery: High-Speed Spoken French",
        "subtitle": "Deciphering Reduced Syllables, Word Mergers & Rapid Colloquialisms",
        "badge_num": "47",
        "intro": "When native French speakers talk casually at full speed, whole syllables disappear. Train your ear to decode reduced speech.",
        "sections": [
            {
                "title": "1. Systematic Reductions in Casual Speech",
                "items": [
                    "« Je suis » sounds like « Chui » (« Chui fatigué », « Chui d'accord »).",
                    "« Je ne sais pas » reduces to « Chais pas » or simply « Chépa ».",
                    "« Qu'est-ce que » reduces to « Kesk » (« Kesk tu fais ? », « Kesk y a ? »).",
                    "Dropping intermediate 'l' sounds: « Il y a » → « Y a » ; « Il faut » → « Faut » ; « Il n'y en a pas » → « Y en a pas »."
                ]
            },
            {
                "title": "2. Merged Words and Fast Conversational Clues",
                "items": [
                    "« C'est-à-dire » spoken as a single fluid burst: « sta-dire ».",
                    "« De toute façon » condensed into « tte façon ».",
                    "« S'il te plaît » pronounced as « steuplé ».",
                    "Developing automatic neural recognition so these casual contractions never derail your global comprehension."
                ]
            }
        ]
    }

    # Page 49: Strategic Note-Taking for Audio Synthesis
    pages[49] = {
        "page": 49,
        "type": "checklist",
        "title": "B2 Listening Mastery: Note-Taking for Synthesis",
        "subtitle": "Capturing Dense 5-Minute Audio Documents for Restitution",
        "badge_num": "48",
        "intro": "In DELF B2, you listen to long authentic documents. Master two-column thematic note-taking to capture key arguments.",
        "sections": [
            {
                "title": "1. The Two-Column Thematic Grid Method",
                "items": [
                    "Divide your blank sheet into two columns: Column 1 for Thèse (arguments for); Column 2 for Antithèse (arguments against).",
                    "Use a dedicated margin for numbers, percentages, dates, and proper names of experts or organizations.",
                    "Use standardized shorthand symbols: ↑ (augmentation/progrès), ↓ (baisse/déclin), ≠ (différent/opposé), pb (problème).",
                    "Never write full sentences: capture telegraphic keywords that trigger immediate conceptual recall."
                ]
            },
            {
                "title": "2. Synthesis and Cross-Checking",
                "items": [
                    "During the pause between listens, connect related ideas with numbered arrows across your notes.",
                    "Identify the speaker's overarching thesis and moral conclusion during the second listen.",
                    "Verify exact spelling of proper nouns and technical terms needed for written answer sheets.",
                    "Formulate a 30-second mental executive summary of the entire audio document before answering questions."
                ]
            }
        ]
    }

    # Pages 50-59: Reading Comprehension
    # Page 50: Long-Form Press Investigations & Editorial Essays
    pages[50] = {
        "page": 50,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Press Investigations & Essays",
        "subtitle": "Deconstructing Long-Form Articles in Le Monde Diplomatique & Libération",
        "badge_num": "49",
        "intro": "Read 1,500-word investigative features and editorial essays with complete critical analysis and deep vocabulary comprehension.",
        "sections": [
            {
                "title": "1. Dissecting Long-Form Journalistic Structure",
                "items": [
                    "The Chapeau (teaser lede) and subheadings (intertitres): understanding how journalists segment long essays.",
                    "Identifying the author's theoretical framework: Marxist, liberal, ecological, or sovereignist perspectives.",
                    "Tracing data corroboration: examining how investigative journalists support claims with leaked documents.",
                    "Recognizing the pivot point where an objective factual report shifts into an ideological critique."
                ]
            },
            {
                "title": "2. Critical Deconstruction of Rhetoric",
                "items": [
                    "Analyze loaded adjectives and evaluative adverbs chosen to steer the reader's judgment.",
                    "Identify rhetorical counterweights: how the author introduces token arguments before systematically demolishing them.",
                    "Extract primary thesis statements from the concluding paragraph of each investigative section.",
                    "Summarize the essay's overarching thesis in two elegant sentences of your own French phrasing."
                ]
            }
        ]
    }

    # Page 51: Philosophical Treatises & Intellectual Essays
    pages[51] = {
        "page": 51,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Philosophical Treatises",
        "subtitle": "Reading Excerpts from Rousseau, Voltaire, Sartre, and Modern Thinkers",
        "badge_num": "50",
        "intro": "Engage with French philosophical texts, understanding abstract reasoning, dialectical propositions, and ethical questions.",
        "sections": [
            {
                "title": "1. Following Abstract Conceptual Arguments",
                "items": [
                    "Identify foundational definitions: how the philosopher defines freedom, justice, alienated labor, or consciousness.",
                    "Follow syllogistic deductions: premise major, premise minor, and inevitable logical conclusion.",
                    "Understand hypothetical thought experiments used to test the universality of an ethical principle.",
                    "Recognize classical 18th-century syntactic inversions and literary sentence structures in Enlightenment texts."
                ]
            },
            {
                "title": "2. Modern Sociological and Philosophical Essays",
                "items": [
                    "Read contemporary intellectuals (Michel Foucault, Pierre Bourdieu, Edgar Morin, Mona Chollet).",
                    "Understand sociological concepts: habitus, cultural capital, biopolitics, systemic intersectionality.",
                    "Analyze how modern essayists critique hyper-consumerism, surveillance capitalism, and loneliness.",
                    "Formulate your personal critical evaluation of the philosopher's core thesis."
                ]
            }
        ]
    }

    # Page 52: Legal Decrees, Directives & White Papers
    pages[52] = {
        "page": 52,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Decrees & White Papers",
        "subtitle": "Decoding Institutional Directives, Legal Frameworks & Policy Papers",
        "badge_num": "51",
        "intro": "Understand administrative decrees, European directives, and ministerial white papers with professional precision.",
        "sections": [
            {
                "title": "1. Deciphering Legislative and Regulatory Syntax",
                "items": [
                    "Structure of French decrees: « Vu la Constitution... Vu le Code du travail... Décrète ce qui suit... »",
                    "Articles and paragraphs (alinéas): navigating numbered legal clauses and exceptions.",
                    "Obligation formulas: « est passible de », « sont tenus de », « sous peine de nullité de plein droit ».",
                    "Effective dates and transitional provisions: identifying when a reform legally enters into force."
                ]
            },
            {
                "title": "2. Government White Papers & Impact Assessments",
                "items": [
                    "Executive summaries of public policy reforms: understanding stated policy objectives versus budget realities.",
                    "Evaluating stakeholder impact assessments: how a law will affect small businesses, employees, and municipalities.",
                    "Deciphering bureaucratic acronyms: PLFSS, CESE, ARS, RGPD, CSE, prud'hommes.",
                    "Extracting actionable legal rights and compliance obligations for organizations."
                ]
            }
        ]
    }

    # Page 53: Sociological Studies & Macroeconomic Reports
    pages[53] = {
        "page": 53,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Sociological Studies",
        "subtitle": "Analyzing INSEE Data, Demographic Reports & Economic Research",
        "badge_num": "52",
        "intro": "Read dense socioeconomic research papers, deciphering statistical data, longitudinal trends, and demographic shifts.",
        "sections": [
            {
                "title": "1. Reading Sociological Methodology & Samples",
                "items": [
                    "Evaluate sample composition: quotas by age, socioeconomic category (CSP), gender, and regional distribution.",
                    "Understand longitudinal studies tracking population cohorts over decades.",
                    "Analyze correlation vs causality in sociological findings regarding educational achievement and wealth.",
                    "Differentiate between raw data findings and the sociologist's qualitative interpretations."
                ]
            },
            {
                "title": "2. Macroeconomic Analysis and Forecasts",
                "items": [
                    "Understand economic indicators: trade balance deficit, sovereign debt ratios, inflation baskets, bond yields.",
                    "Analyze reports on labor market flexibilization, pension system solvency, and tax redistributive effects.",
                    "Compare divergent economic forecasts published by the Banque de France, OECD, and independent think tanks.",
                    "Synthesize macroeconomic findings to support arguments in DELF B2 written essays."
                ]
            }
        ]
    }

    # Page 54: Contemporary & Classical French Literature
    pages[54] = {
        "page": 54,
        "type": "checklist",
        "title": "B2 Reading Comprehension: French Literature",
        "subtitle": "Literary Masterpieces from Camus and Flaubert to Modern Authors",
        "badge_num": "53",
        "intro": "Read classical and modern French novels with fluency, appreciating stylistic nuance, voice, and narrative depth.",
        "sections": [
            {
                "title": "1. Narrative Voice and Literary Tenses",
                "items": [
                    "Recognize the passé simple in literary narrative: il parla, il prit, ils voulurent, il fut, il eut.",
                    "Understand the imperfect subjunctive in elevated literature: « encore eût-il fallu qu'il le sût ».",
                    "Analyze polyphonic narrative points of view: alternating between omniscient narrator and interior monologues.",
                    "Follow shifts in literary register: aristocratic elegance contrasted with visceral street dialogue."
                ]
            },
            {
                "title": "2. Thematic Depth and Symbolic Interpretation",
                "items": [
                    "Explore existential themes: absurdity, rebellion, personal authenticity in Camus (L'Étranger, La Peste).",
                    "Explore social realist critique: class struggle, provincial boredom, societal hypocrisy in Balzac and Flaubert.",
                    "Read modern Francophone voices exploring post-colonial identity, migration, and female autonomy.",
                    "Formulate deep personal aesthetic critiques on the emotional power and lasting relevance of the text."
                ]
            }
        ]
    }

    # Page 55: Formal Administrative Appeals & Legal Petitions
    pages[55] = {
        "page": 55,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Appeals & Petitions",
        "subtitle": "Deciphering Administrative Appeals, Formal Injunctions & Legal Demands",
        "badge_num": "54",
        "intro": "Understand formal legal correspondence, administrative appeals (recours gracieux), and citizen petitions.",
        "sections": [
            {
                "title": "1. Structure of an Administrative Appeal (Recours)",
                "items": [
                    "Recours gracieux (appeal to the deciding official) vs Recours hiérarchique (appeal to superior ministry).",
                    "Legal basis (moyens de droit): establishing which laws, decrees, or European conventions were violated.",
                    "Factual basis (moyens de fait): establishing the verifiable events demonstrating administrative error.",
                    "The specific claim (conclusions): explicitly demanding the annulment or modification of the contested decision."
                ]
            },
            {
                "title": "2. Citizen Petitions and Collective Manifestos",
                "items": [
                    "The call to mobilization: analyzing persuasive rhetoric designed to gather citizen signatures.",
                    "Denunciation of injustice: framing government or corporate decisions as violations of the public good.",
                    "Demands for policy reform: concrete legislative changes demanded from parliament or municipal mayors.",
                    "Assessing legal feasibility: distinguishing realistic legal demands from purely symbolic protests."
                ]
            }
        ]
    }

    # Page 56: Scientific Papers & Ecological Impact Assessments
    pages[56] = {
        "page": 56,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Scientific Papers",
        "subtitle": "Understanding Peer-Reviewed Studies, Climate Reports & Impact Assessments",
        "badge_num": "55",
        "intro": "Read peer-reviewed scientific summaries (IPCC / GIEC reports, environmental impact assessments) with technical fluency.",
        "sections": [
            {
                "title": "1. Navigating Scientific Summaries (Rapports du GIEC)",
                "items": [
                    "The Summary for Policymakers (Résumé à l'intention des décideurs): synthesizing key climate trajectories.",
                    "Confidence levels: understanding IPCC formulations: « très probable » (90%), « pratiquement certain » (99%).",
                    "Climate tipping points (points de bascule): permafrost thaw, ocean current disruption, Amazon dieback.",
                    "Mitigation and adaptation strategies: carbon pricing, rewilding, energy conservation, coastal defenses."
                ]
            },
            {
                "title": "2. Environmental Impact Assessments (Études d'Impact)",
                "items": [
                    "Baseline ecosystem audit: flora, fauna, water tables, and soil composition before project kickoff.",
                    "Direct and indirect impacts: acoustic pollution, habitat fragmentation, and greenhouse emissions.",
                    "The Mitigation Hierarchy (Éviter / Réduire / Compenser): evaluating the developer's compensation measures.",
                    "Citizen inquiry findings (Enquête publique): reading public observations and the inquiry commissioner's report."
                ]
            }
        ]
    }

    # Page 57: Cultural & Historical Essays on French Identity
    pages[57] = {
        "page": 57,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Historical & Cultural Essays",
        "subtitle": "Exploring Republican Ideals, Memory & Francophone Identity",
        "badge_num": "56",
        "intro": "Read profound cultural essays examining the historical roots of French secularism (laïcité), memory, and national identity.",
        "sections": [
            {
                "title": "1. The Foundations of French Republican Thought",
                "items": [
                    "The 1789 legacy: Declaration of the Rights of Man, abolition of privilege, universal equality before the law.",
                    "The 1905 Law on Secularism: neutrality of the State, freedom of religious belief and freedom from religion.",
                    "The French social model: state welfare, public healthcare, redistributive taxation, and public services.",
                    "Memory debates (Guerre des mémoires): examining historical commemorations, colonial history, and reconciliation."
                ]
            },
            {
                "title": "2. The Evolution of Contemporary Francophone Identity",
                "items": [
                    "Debating the boundaries between multiculturalism and republican assimilation in modern France.",
                    "The defense of the French language: Académie française debates, Toubon Law, language purity vs evolution.",
                    "The Francophone worldview: promoting linguistic diversity as an alternative to Anglo-American monolingualism.",
                    "Synthesizing complex cultural essays to formulate nuanced arguments in your own writing."
                ]
            }
        ]
    }

    # Page 58: Decoding Irony, Stylistic Polyphony & Double Meanings
    pages[58] = {
        "page": 58,
        "type": "checklist",
        "title": "B2 Reading Comprehension: Irony & Polyphony",
        "subtitle": "Mastering Double Entendres, Textual Irony & Multivocal Discourse",
        "badge_num": "57",
        "intro": "Advanced French prose often contains polyphonic layers where the author's real meaning is the exact opposite of the literal text.",
        "sections": [
            {
                "title": "1. Identifying Written Irony (L'Ironie Textuelle)",
                "items": [
                    "Antiphrasis (L'Antiphrase): praising an absurd policy enthusiastically to highlight its catastrophic foolishness.",
                    "Ironic quotation marks: « Ces 'brillants' gestionnaires ont ruiné l'entreprise en six mois. »",
                    "Mock-heroic tone: describing petty administrative bickering using grandiose military vocabulary.",
                    "Socratic faux-naivety: pretending not to understand an obvious injustice to force the reader to confront it."
                ]
            },
            {
                "title": "2. Polyphonic Discourse (Les Voix Multiples)",
                "items": [
                    "Distinguishing when the author is quoting an opponent's thesis versus advancing their own core belief.",
                    "Identifying free indirect discourse where character thoughts blend into third-person narration without quotes.",
                    "Tracing shifts in register that signal a change of speaker or perspective in contemporary novels.",
                    "Answering subtle DELF B2 reading questions that test whether you grasped the author's true implied judgment."
                ]
            }
        ]
    }

    # Page 59: Strategic Reading: Fast Synthesis & Critical Evaluation
    pages[59] = {
        "page": 59,
        "type": "checklist",
        "title": "B2 Reading Strategies: Fast Synthesis & Evaluation",
        "subtitle": "Reading 800 Words and Answering Critical Questions in 25 Minutes",
        "badge_num": "58",
        "intro": "Master the exam reading techniques required for DELF B2: fast skimming, thesis detection, and synthesis under strict time limits.",
        "sections": [
            {
                "title": "1. The 3-Step B2 Exam Reading Method",
                "items": [
                    "Step 1 (3 minutes): Skim title, lede, author, publication date, and subheadings to establish thematic context.",
                    "Step 2 (2 minutes): Read all exam questions carefully; identify question types (factual recall, author attitude, synthesis).",
                    "Step 3 (15 minutes): Deep read with a highlighter, marking text passages that directly answer specific question prompts.",
                    "Step 4 (5 minutes): Write concise, grammatically flawless answers in French, rephrasing ideas rather than copying."
                ]
            },
            {
                "title": "2. Avoiding Traps in Multiple-Choice Questions",
                "items": [
                    "Beware of literal word matches: distractor choices often repeat exact words from the text but reverse the meaning.",
                    "Watch out for extreme absolute adverbs in answer choices (toujours, jamais, exclusivement, tous les citoyens).",
                    "Verify the author's nuanced position: choose answers that capture balanced conditionality rather than simplistic dogma.",
                    "Check that your written answers directly address the question without wandering into irrelevant commentary."
                ]
            }
        ]
    }

    # Pages 60-67: Written Production & Interaction
    # Page 60: DELF B2 Argumentative Essay: Structuring a 250-Word Synthesis
    pages[60] = {
        "page": 60,
        "type": "checklist",
        "title": "B2 Writing Mastery: The 250-Word Argumentative Essay",
        "subtitle": "Mastering the DELF B2 Written Production (Essai Argumentatif)",
        "badge_num": "59",
        "intro": "In DELF B2, you must write a 250-word formal argumentative text (essay, letter, or article) defending a thesis with structured paragraphs.",
        "sections": [
            {
                "title": "1. The Formal Architecture of the B2 Essay",
                "items": [
                    "Introduction (40–50 words): Hook (accroche) + Thematic Context + Problem Statement (problématique) + Outline.",
                    "Body Paragraph 1 (70–80 words): First major argument + concrete illustration + logical connectors.",
                    "Body Paragraph 2 (70–80 words): Second major argument addressing counterarguments + nuanced concession.",
                    "Conclusion (40–50 words): Concise summary of the demonstration + open forward-looking question (ouverture)."
                ]
            },
            {
                "title": "2. Word Count Management & Precision Scoring",
                "items": [
                    "Target word count: strictly around 250 words (acceptable range: 225 to 275 words; going under 225 loses points).",
                    "How French words are counted: « l'environnement » = 2 words ; « c'est-à-dire » = 1 word ; « un chef-d'œuvre » = 2 words.",
                    "Clear paragraph separation: leave a blank line between introduction, body paragraphs, and conclusion.",
                    "Ensure a balanced demonstration: never write a one-sided polemic; show intellectual maturity through concession."
                ]
            }
        ]
    }

    # Page 61: Formal Letter to Authorities (Lettre de Réclamation Formelle / Au Maire)
    pages[61] = {
        "page": 61,
        "type": "checklist",
        "title": "B2 Writing Mastery: Formal Letter to Authorities",
        "subtitle": "Writing Petitions, Civic Grievances & Official Appeals to Mayors and Directors",
        "badge_num": "60",
        "intro": "Write assertive, highly polite formal letters to municipal mayors, corporate CEOs, and government officials.",
        "sections": [
            {
                "title": "1. Official Letterhead and Opening Formulas",
                "items": [
                    "Official header block: your contact details (top left), recipient's full title and address (top right), date and city.",
                    "Precise subject line: « Objet : Recours gracieux – Contestation de la décision d'urbanisme du 14 mars 2026. »",
                    "Formal opening salutation: « Monsieur le Maire, », « Madame la Directrice générale, » (never write 'Cher Monsieur').",
                    "Stating the civic purpose: « En tant que représentant du collectif des résidents du quartier, je me permets de vous interpeller... »"
                ]
            },
            {
                "title": "2. Argumentative Demonstration & Closing Formulations",
                "items": [
                    "Expose the prejudice to the community using objective evidence, safety risks, and quality-of-life impacts.",
                    "Propose viable policy alternatives: « Plutôt que de détruire ce parc, nous suggérons son aménagement en jardin partagé. »",
                    "Urge personal intervention: « Nous sollicitons une réunion de concertation avant le démarrage des travaux. »",
                    "Elevated closing formula: « Dans l'attente de votre réponse, je vous prie d'agréer, Monsieur le Maire, l'expression de ma haute considération. »"
                ]
            }
        ]
    }

    # Page 62: Professional Proposal & Business Case (Proposition de Projet)
    pages[62] = {
        "page": 62,
        "type": "checklist",
        "title": "B2 Writing Mastery: Professional Business Proposals",
        "subtitle": "Writing Project Pitches, Executive Summaries & Change Management Cases",
        "badge_num": "61",
        "intro": "Draft compelling professional proposals, business cases, and innovation pitches for corporate leadership.",
        "sections": [
            {
                "title": "1. Structuring the Executive Business Case",
                "items": [
                    "Executive Summary (Le Résumé Opérationnel): stating the business opportunity, budget, and projected ROI.",
                    "Diagnosing the problem (L'État des lieux): analyzing current inefficiencies, customer churn, or competitive lag.",
                    "The proposed strategic solution: detailing methodology, technological tools, team allocations, and milestone timeline.",
                    "Risk mitigation matrix: anticipating potential roadblocks (regulatory, technical, financial) and remedies."
                ]
            },
            {
                "title": "2. Financials and Call to Action",
                "items": [
                    "Budget breakdown and resource allocation: presenting costs clearly with transparent return on investment models.",
                    "Change management plan: detailing how employees will be trained and guided through the operational transition.",
                    "Closing call to action: requesting formal project authorization and budget sign-off from the board.",
                    "Polite professional closing: « Je reste à votre entière disposition pour vous présenter cette initiative lors du prochain comité de direction. »"
                ]
            }
        ]
    }

    # Page 63: Editorial & Opinion Article for Press (Tribune Libre)
    pages[63] = {
        "page": 63,
        "type": "checklist",
        "title": "B2 Writing Mastery: The Press Editorial (Tribune Libre)",
        "subtitle": "Writing Engaging Opinion Columns for Le Monde or Intellectual Blogs",
        "badge_num": "62",
        "intro": "Write a thought-provoking opinion column (tribune libre) intended for publication in the national press or a prominent blog.",
        "sections": [
            {
                "title": "1. Catchy Headlines and Persuasive Opening",
                "items": [
                    "Craft a provocative title: « Transition écologique : cessons de culpabiliser les citoyens ordinaires ! »",
                    "The bold lede (Le chapeau): summarize the urgency of the societal issue in two punchy sentences.",
                    "The civic alarm: highlight why current government or corporate policies are dangerously misguided.",
                    "Adopt an authoritative collective voice: using « nous » to build solidarity with the reading public."
                ]
            },
            {
                "title": "2. Persuasive Rhetoric and Manifesto Climax",
                "items": [
                    "Deploy striking metaphors and historical parallels to make abstract economic or ethical concepts tangible.",
                    "Rebut common objections with sharp intellectual wit: « L'argument du coût économique ne tient pas face à l'urgence vitale. »",
                    "Formulate a clear manifesto demand: calling on citizens, courts, and lawmakers to implement immediate reform.",
                    "End with a memorable philosophical aphorism that resonates in public debate."
                ]
            }
        ]
    }

    # Page 64: Critical Review & Synthesis of Opposing Views (Note de Synthèse)
    pages[64] = {
        "page": 64,
        "type": "checklist",
        "title": "B2 Writing Mastery: Synthesis of Opposing Views",
        "subtitle": "Writing Objective Summaries of Competing Documents (Note de Synthèse)",
        "badge_num": "63",
        "intro": "Synthesize two contradictory documents into an objective 200-word briefing note balancing both perspectives fairly.",
        "sections": [
            {
                "title": "1. Identifying Points of Convergence and Disagreement",
                "items": [
                    "Analyze both source texts side by side: what foundational problem do both authors agree exists?",
                    "Identify where the authors diverge sharply: methodology, ideological priorities, ethical boundaries, or timeline.",
                    "Group arguments thematically rather than text by text (never do Part 1 = Text A, Part 2 = Text B).",
                    "Maintain strict editorial neutrality: use attributive formulas (« Pour le premier auteur... En revanche, le second démontre... »)."
                ]
            },
            {
                "title": "2. Writing the Cohesive Synthesis",
                "items": [
                    "Brief introduction stating the common societal issue without naming documents awkwardly.",
                    "Thematic body paragraphs contrasting the proposed solutions with sophisticated logical transitions.",
                    "Rephrase all ideas completely in your own words (zero copy-pasting of sentences from either source).",
                    "Objective concluding summary stating the core dilemma facing modern decision-makers."
                ]
            }
        ]
    }

    # Page 65: Advanced Rhetorical Connectors & Transitional Flow
    pages[65] = {
        "page": 65,
        "type": "checklist",
        "title": "B2 Writing Mechanics: Advanced Rhetorical Connectors",
        "subtitle": "Polishing Syntax with High-Level Signposts and Logical Transitions",
        "badge_num": "64",
        "intro": "Deploy advanced rhetorical connectors to create smooth, natural transitions between paragraphs and complex sentences.",
        "sections": [
            {
                "title": "1. Concession and Rebuttal Signposts",
                "items": [
                    "Certes... néanmoins... : « Certes, cette réforme implique des sacrifices ; néanmoins, elle est indispensable. »",
                    "Il n'en reste pas moins que : « Même si les critiques sont nombreuses, il n'en reste pas moins que les résultats sont positifs. »",
                    "Loin de... : « Loin de résoudre la crise, cette mesure a attisé les rancœurs. »",
                    "Encore faut-il que (+ Subjonctif): « L'innovation est une bonne chose, encore faut-il qu'elle soit accessible à tous. »"
                ]
            },
            {
                "title": "2. Logical Deduction and Synthesis Signposts",
                "items": [
                    "Dès lors / Partant de là : « Dès lors, il apparaît évident que nous devons revoir notre cadre réglementaire. »",
                    "Force est d'admettre que : « Force est d'admettre que les prévisions initiales étaient trop optimistes. »",
                    "En tout état de cause / Quoi qu'il en soit : « Quoi qu'il en soit, le calendrier des élections sera maintenu. »",
                    "Punctuation mastery: using em-dashes (—) and semicolons (;) to structure multi-clause periods elegantly."
                ]
            }
        ]
    }

    # Page 66: Stylistic Precision: Nominalization & Syntactic Variety
    pages[66] = {
        "page": 66,
        "type": "checklist",
        "title": "B2 Writing Mechanics: Stylistic Precision & Variety",
        "subtitle": "Varying Sentence Structures, Passive Transforms & Rhythm",
        "badge_num": "65",
        "intro": "Elevate your writing style from good to extraordinary by eliminating repetitive phrasing and varying sentence lengths.",
        "sections": [
            {
                "title": "1. Eliminating Clunky Verbal Crutches",
                "items": [
                    "Eliminate weak 'Il y a' structures: replace « Il y a beaucoup de problèmes » with « De multiples écueils subsistent. »",
                    "Eliminate vague 'choses': replace « Il a dit des choses importantes » with « Il a formulé des propositions capitales. »",
                    "Transform verbal clauses into powerful nominal openers: « L'avènement des énergies renouvelables modifiera la donne. »",
                    "Use active, dynamic verbs: stimuler, infléchir, pérenniser, endiguer, fragiliser, orchestrer."
                ]
            },
            {
                "title": "2. Sentence Rhythm and Structural Variety",
                "items": [
                    "Alternate between long, periodic sentences (complex syntax) and short, punchy declarative statements.",
                    "Use appositive adjectives at the start of clauses: « Conscient des enjeux climatiques, le gouvernement a réagi promptement. »",
                    "Use chiasmus and parallel structures to make arguments memorable: « Travailler pour vivre, et non vivre pour travailler. »",
                    "Avoid accidental repetitions of the same word within a 3-sentence span by deploying precise synonyms."
                ]
            }
        ]
    }

    # Page 67: Writing Mechanics: Flawless Grammar & Concordance
    pages[67] = {
        "page": 67,
        "type": "checklist",
        "title": "B2 Writing Mechanics: Flawless Grammar Self-Audit",
        "subtitle": "The Ultimate 5-Step Proofreading Routine for DELF B2 Exam Perfection",
        "badge_num": "66",
        "intro": "Dedicate the final 10 minutes of your exam writing time to a systematic, high-yield proofreading routine.",
        "sections": [
            {
                "title": "1. The 5-Step Grammatical Self-Audit Routine",
                "items": [
                    "Pass 1: Past participle agreement with Avoir when COD precedes: « Les mesures que nous avons adoptées ».",
                    "Pass 2: Subjunctive mood triggers: verify verbs following il faut que, bien que, pour que, and negative opinion verbs.",
                    "Pass 3: Subject-verb agreement with collective and inverted subjects: « La plupart des citoyens soutiennent ce projet ».",
                    "Pass 4: Prepositional accuracy: pallier le manque (never 'pallier à') ; se rappeler quelque chose (never 'se rappeler de').",
                    "Pass 5: Accents and spelling homophones: tâche (task) vs tache (stain) ; notre (possessive) vs le nôtre (pronoun)."
                ]
            },
            {
                "title": "2. Formatting and Visual Presentation Checks",
                "items": [
                    "Verify word count is strictly between 225 and 275 words, writing the total count at the bottom of the page.",
                    "Ensure clean indentations (alinéas) at the start of each new paragraph.",
                    "Confirm that the tone remains consistently formal (no colloquial slips, no missing 'ne' in negations).",
                    "Verify that both address blocks, date, and formal sign-offs are aligned according to French postal etiquette."
                ]
            }
        ]
    }

    # Pages 68-71: Assessment & C1 Readiness
    # Page 68: Final Self-Evaluation: Spoken Argumentation & Debate Autonomy
    pages[68] = {
        "page": 68,
        "type": "audit",
        "title": "Final Self-Evaluation: Spoken Argumentation & Debate",
        "subtitle": "Comprehensive Oral Production & Interaction Audit for B2 Threshold",
        "badge_num": "67",
        "intro": "Comprehensive diagnostic checklist to evaluate whether your spoken French meets the CEFR B2 independent threshold.",
        "items": [
            "I can deliver an uninterrupted 5-minute presentation defending an argumentative thesis on a controversial issue.",
            "I can engage in lively cross-examination with an educated native speaker, defending my ideas and refuting objections.",
            "I can structure my speech dialectically using Thèse, Antithèse, and Synthèse without notes.",
            "I naturally adjust my delivery cadence, voice modulation, and pauses to hold audience attention.",
            "I express nuanced certainty, doubt, probability, and constructive concessions without stumbling.",
            "I smoothly navigate between informal French with peers, standard workplace French, and formal academic debate.",
            "I can identify and dismantle common logical fallacies in opposing arguments during discussions.",
            "I weave cultural idioms, proverbs, and historical allusions naturally into my spoken debate."
        ],
        "sections": [
            {
                "title": "1. Spoken Production Audit (Monologue Argumenté)",
                "items": [
                    "Thematic hook and problem statement: Can you formulate an engaging intro, define the controversy, and announce a plan in 60 seconds?",
                    "Dual-pillar demonstration: Can you defend two opposing sides of a complex debate with equal rigor and supporting evidence?",
                    "Dialectical synthesis: Can you transcend simplistic contradictions and propose a mature systemic policy resolution?",
                    "Fluency and composure: Can you speak at normal native speed for 5 minutes without long unnatural hesitations?"
                ]
            },
            {
                "title": "2. Spoken Interaction Audit (Débat & Échange)",
                "items": [
                    "Rebuttal agility: Can you counter an unexpected objection from the examiner on the spot with a convincing example?",
                    "Concession techniques: Can you acknowledge an opponent's valid point (« Certes... mais ») before reasserting your thesis?",
                    "Reframing skills: Can you rephrase a biased or aggressive question diplomatically before answering?",
                    "Negotiation stamina: Can you conduct an 8-minute professional or civic negotiation to a satisfactory consensus?"
                ]
            }
        ]
    }

    # Page 69: Final Self-Evaluation: Receptive Comprehension & Critical Analysis
    pages[69] = {
        "page": 69,
        "type": "audit",
        "title": "Final Self-Evaluation: Receptive Comprehension",
        "subtitle": "Checking Your Listening, Reading & Critical Analysis Mastery",
        "badge_num": "68",
        "intro": "Evaluate your listening comprehension of fast authentic radio broadcasts and your reading of long-form intellectual articles.",
        "items": [
            "I can follow fast radio news bulletins, cultural documentaries, and investigative reports (France Culture, Arte).",
            "I can understand panel discussions with multiple speakers talking simultaneously and interrupting each other.",
            "I can identify speaker attitudes, implicit critique, irony, and political spin in live interviews.",
            "I can read long-form investigative journalism and editorial essays in Le Monde and Courrier International.",
            "I can follow contemporary French literature, short stories, and philosophical treatises with enjoyment.",
            "I can decipher administrative decrees, institutional white papers, and co-ownership regulations with accuracy.",
            "I can write a 250-word argumentative essay or formal petition respecting French conventions.",
            "I can synthesize opposing documents into an objective briefing note without copying source sentences."
        ],
        "sections": [
            {
                "title": "1. Listening Comprehension Audit",
                "items": [
                    "Authentic broadcast audio: Can you understand the core thesis and secondary arguments of a 5-minute radio report on two listens?",
                    "Subtext and irony detection: Can you identify when a journalist or commentator is using deadpan humor or sarcasm?",
                    "Accent versatility: Can you follow native speakers from Quebec, Belgium, Switzerland, Senegal, and the Maghreb?",
                    "Strategic note-taking: Can you capture dates, numbers, and opposing arguments simultaneously using a two-column grid?"
                ]
            },
            {
                "title": "2. Reading Comprehension Audit",
                "items": [
                    "Speed reading and skimming: Can you read an 800-word editorial and answer detailed comprehension questions in 20 minutes?",
                    "Literary and stylistic analysis: Can you identify polyphony, metaphors, and free indirect discourse in contemporary novels?",
                    "Implicit inference: Can you deduce the author's unspoken attitude when they use understatement and litotes?",
                    "Distractor elimination: Can you identify and eliminate tricky multiple-choice options with precision?"
                ]
            }
        ]
    }

    # Page 70: Final Self-Evaluation: Advanced Grammar, Syntax & Vocabulary
    pages[70] = {
        "page": 70,
        "type": "audit",
        "title": "Final Self-Evaluation: Advanced Grammar & Vocabulary",
        "subtitle": "Checking Your Command of Complex Syntax and 4,000+ Active Words",
        "badge_num": "69",
        "intro": "Verify that you have mastered the advanced grammar structures and rich vocabulary required for CEFR B2 certification.",
        "items": [
            "I can conjugate and use the subjonctif passé accurately to express completed actions.",
            "I master subtle subjonctif vs indicatif distinctions after dual-meaning verbs and relative clauses.",
            "I use the futur antérieur for completed future actions and past suppositions with confidence.",
            "I deploy formal subject inversion after adverbs like peut-être, à peine, and aussi with elegance.",
            "I use nominalization to transform verbal sentences into dense, formal journalistic prose.",
            "I command complex relative pronouns (dont, auquel, duquel, ce à quoi) without grammatical errors.",
            "I have an active working vocabulary of over 4,000 to 5,000 words across all core societal themes.",
            "I routinely proofread my written work, eliminating agreement, subjunctive, and syntax errors."
        ],
        "sections": [
            {
                "title": "1. Advanced Grammar & Syntax Audit",
                "items": [
                    "Concession mastery: Do you comfortably use bien que, quoique, avoir beau, and en dépit de in essays?",
                    "Hypothetical sophistication: Can you formulate conditions using à moins que (+ ne explétif), à condition que, and au cas où?",
                    "Reported speech concordance: Can you shift speech into the past, adjusting tenses and temporal adverbs accurately?",
                    "Rhetorical connectors: Do you naturally deploy certes, néanmoins, force est de constater, and dès lors?"
                ]
            },
            {
                "title": "2. Thematic Vocabulary Precision (4,000–5,000 Words)",
                "items": [
                    "Ethics & AI: Génie génétique, algorithmes, biais, reconnaissance faciale, souveraineté numérique.",
                    "Ecology & economics: Neutralité carbone, décroissance, agroécologie, RSE, circuits courts, résilience.",
                    "Politics & society: Laïcité, séparation des pouvoirs, désobéissance civile, gentrification, mixité sociale.",
                    "Professional workplace: Ubérisation, charge mentale, burn-out, droit à la déconnexion, dialogue social."
                ]
            }
        ]
    }

    # Page 71: Final Milestone: Ready to Move to C1 Certification [Respect illustration!]
    pages[71] = {
        "page": 71,
        "type": "audit",
        "title": "Final Milestone: Ready to Move to C1 Certification",
        "subtitle": "Congratulations! You Have Mastered CEFR B2 Independent Fluency",
        "badge_num": "70",
        "intro": "Review your final milestone criteria to confirm you are completely prepared to step into C1 (Autonomous User / Effective Operational Proficiency).",
        "items": [
            "Independent debate mastery: You can defend a complex thesis spontaneously in front of a jury of native speakers.",
            "Intellectual listening fluency: You can understand fast, overlapping broadcast debates, podcasts, and university lectures.",
            "Academic writing precision: You can compose a 250-word synthesis essay or formal petition with flawless rhetorical structure.",
            "Deep linguistic culture: You possess an active vocabulary of over 4,000 words and appreciate French literary and civic culture.",
            "Ready to move to C1: You are fully prepared to begin your CEFR C1 journey toward near-native autonomous mastery!"
        ],
        "sections": [
            {
                "title": "1. Final B2 Certification Benchmark",
                "items": [
                    "Autonomous fluency: You can communicate naturally in French in academic, professional, and personal environments without fatigue.",
                    "Nuanced argumentation: You can present balanced perspectives, conceding points and using subtle rhetorical irony.",
                    "Stylistic versatility: You effortlessly shift between informal banter, standard professional French, and elevated formal prose.",
                    "Solid C1 foundation: You possess the grammatical precision and vocabulary depth needed for advanced C1 and DALF certification."
                ]
            }
        ]
    }

    return pages

if __name__ == "__main__":
    pages = get_b2_data()
    print(f"Generated {len(pages)} pages.")
    with open("b2_curriculum_data.py", "w", encoding="utf-8") as f:
        f.write("# b2_curriculum_data.py - CEFR B2 Curriculum Dataset\n")
        f.write("# Rich, authentic French with clear, learner-friendly English\n\n")
        f.write("B2_PAGES_DATA = ")
        f.write(pprint.pformat(pages, width=120, sort_dicts=False))
        f.write("\n")
    print("Successfully wrote b2_curriculum_data.py")
