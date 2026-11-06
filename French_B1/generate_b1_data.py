import pprint

def get_b1_data():
    pages = {}

    # Page 1: Cover
    pages[1] = {
        "page": 1,
        "type": "cover",
        "title": "French Learning Roadmap & Checklist",
        "subtitle": "French B1",
        "badge_num": "",
        "intro": ""
    }

    # Page 2: Overall Objectives (Threshold / Intermediate)
    pages[2] = {
        "page": 2,
        "type": "objectives",
        "title": "Overall Objectives of B1 Level (Threshold / Intermediate)",
        "subtitle": "Speaking & Listening Skills for Independent Expression",
        "badge_num": "1",
        "intro": "Welcome to French B1! At this intermediate level, you become an independent user of French. You can navigate social, academic, and professional situations, share your opinions on society issues, and tell stories in rich detail.",
        "sections": [
            {
                "title": "Speak (Spoken Production & Spoken Interaction)",
                "items": [
                    "Express and defend your opinions on cultural and social topics using clear arguments and examples.",
                    "Give a structured 3-minute talk on a familiar subject without reading from notes.",
                    "Handle unexpected situations when traveling, dealing with authorities, or resolving customer disputes.",
                    "Engage in discussions with French speakers, reacting to their arguments and adding your own perspective."
                ]
            },
            {
                "title": "Listen (Listening Comprehension)",
                "items": [
                    "Follow the main points of radio news broadcasts, podcasts, and documentaries on familiar topics.",
                    "Understand everyday conversations between native speakers when spoken clearly at natural speed.",
                    "Catch the speaker's viewpoint, attitude, and tone in debates, interviews, and public presentations."
                ]
            }
        ]
    }

    # Page 3: Overall Objectives (Continued)
    pages[3] = {
        "page": 3,
        "type": "objectives",
        "title": "Overall Objectives of B1 Level (Continued)",
        "subtitle": "Reading & Writing Skills for Personal and Professional Independence",
        "badge_num": "2",
        "intro": "At B1, your reading and writing allow you to express nuanced thoughts, compose well-organized essays, and read newspapers, literary excerpts, and formal correspondence with ease.",
        "sections": [
            {
                "title": "Write (Written Production & Interaction)",
                "items": [
                    "Write clear, connected texts (160–180 words) describing experiences, feelings, and personal reactions.",
                    "Draft well-structured opinion essays arguing for or against a controversial topic with logical connectors.",
                    "Write formal letters to administration, employers, or customer service (lettre de réclamation, lettre de motivation).",
                    "Summarize short articles and contribute thoughtfully to online forums and collaborative debates."
                ]
            },
            {
                "title": "Read (Reading Comprehension)",
                "items": [
                    "Read opinion columns, press articles, and interviews in newspapers like Le Monde and Le Figaro.",
                    "Understand standard formal letters, administrative forms, employment contracts, and workplace memos.",
                    "Read modern French short stories, novels, and cultural reviews, following the plot and character emotions."
                ]
            }
        ]
    }

    # Page 4: Real-Life Outcomes & Themes 1-4
    pages[4] = {
        "page": 4,
        "type": "themes_table",
        "title": "B1 French – Real-Life Outcomes & Core Themes & Topics",
        "subtitle": "Real-Life Outcomes at CEFR B1 (Themes 1–4)",
        "badge_num": "3",
        "intro": "These real-life outcomes and thematic areas represent the intermediate threshold of independent communication in French.",
        "items": [
            "Participate actively in discussions about modern society, climate, work, and digital media.",
            "Write structured formal letters and argumentative essays expressing your personal viewpoints.",
            "Understand radio podcasts and news stories covering current affairs and cultural debates."
        ],
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 1: Society, Migration & Diversity", "Integration, multicultural communities, generations, and volunteering.", "« L'engagement associatif permet de renforcer la solidarité entre générations. »"],
                ["Theme 2: Ecology & Climate Action", "Renewable energy, biodiversity, waste reduction, and sustainable living.", "« Il est indispensable que chacun réduise sa consommation de plastique au quotidien. »"],
                ["Theme 3: Modern Workplace & Labor Rights", "Teleworking, work-life balance, employment conditions, and career transitions.", "« Bien que le télétravail offre de la flexibilité, il peut parfois isoler les salariés. »"],
                ["Theme 4: Digital Era & Social Networks", "Information overload, data privacy, social media influence, and digital safety.", "« Les réseaux sociaux facilitent la communication, mais ils peuvent propager de fausses nouvelles. »"]
            ]
        }
    }

    # Page 5: Themes 5-7
    pages[5] = {
        "page": 5,
        "type": "themes_table",
        "title": "B1 French – Core Themes & Topics (Part 2)",
        "subtitle": "Themes 5–7: Culture, Science & Consumer Rights",
        "badge_num": "4",
        "intro": "Expand your vocabulary to explore cultural heritage, science, and conscious consumer habits in the Francophone world.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 5: Culture, Arts & Heritage", "Cinema, theater, festivals, literature, and preserving historical monuments.", "« Ce festival met en valeur la richesse des cultures francophones à travers le monde. »"],
                ["Theme 6: Science, Health & Well-being", "Medical progress, healthy lifestyles, mental health, and bioethics.", "« Les experts recommandent d'adopter une alimentation variée pour préserver sa santé. »"],
                ["Theme 7: Responsible Consumption & Ethics", "Fair trade, local markets, circular economy, and fighting food waste.", "« Privilégier les circuits courts permet de soutenir les producteurs locaux. »"]
            ]
        }
    }

    # Page 6: Themes 8-10
    pages[6] = {
        "page": 6,
        "type": "themes_table",
        "title": "B1 French – Core Themes & Topics (Part 3)",
        "subtitle": "Themes 8–10: Education, Urban Life & Civic Rights",
        "badge_num": "5",
        "intro": "Discuss education systems, life in eco-cities, and active citizenship with intermediate vocabulary.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 8: Education & Lifelong Learning", "University studies, apprenticeships, student mobility, and studying abroad.", "« Participer à un échange universitaire offre une ouverture culturelle exceptionnelle. »"],
                ["Theme 9: Urban Life & Future Cities", "Public transport, urban green spaces, bike sharing, and smart cities.", "« Les villes modernes doivent développer des pistes cyclables sécurisées. »"],
                ["Theme 10: Justice, Law & Citizenship", "Voting, equality, civic duties, human rights, and community activism.", "« Le droit de vote constitue l'un des piliers fondamentaux de la démocratie. »"]
            ]
        }
    }

    # Page 7: Communicative Functions
    pages[7] = {
        "page": 7,
        "type": "functions_table",
        "title": "B1 French – Core Communicative Functions",
        "subtitle": "Themes 11–14 & Intermediate Speaking Functions",
        "badge_num": "6",
        "intro": "These core speaking and writing patterns help you express opinions, defend ideas, and handle debates in French.",
        "table": {
            "headers": ["Communicative Function", "Grammar & Key Patterns", "Practical Real-Life Example"],
            "rows": [
                ["Expressing Necessity & Desire", "Subjonctif présent", "« Il faut que nous trouvions une solution écologique durable. »"],
                ["Hypothetical Situations", "Si + imparfait + conditionnel", "« Si j'avais plus de temps libre, je ferais du bénévolat dans une association. »"],
                ["Expressing Regrets & Wishes", "Conditionnel passé", "« J'aurais aimé participer à cette conférence passionnante hier soir. »"],
                ["Reporting Past Speech", "Discours indirect au passé", "« Le directeur a affirmé qu'il prendrait des mesures dès le mois prochain. »"],
                ["Highlighting Information", "Mise en relief (C'est... qui/que)", "« C'est cette initiative citoyenne qui a permis de transformer le quartier. »"],
                ["Expressing Cause & Concession", "Bien que + subj. / En raison de", "« Bien qu'il fasse froid, nous avons maintenu notre manifestation sportive. »"]
            ]
        }
    }

    # Pages 8-19: Grammar Foundation
    # Page 8: Le Subjonctif Présent
    pages[8] = {
        "page": 8,
        "type": "checklist",
        "title": "B1 Grammar: Le Subjonctif Présent",
        "subtitle": "Formation & Core Triggers: Necessity, Wishes & Feelings",
        "badge_num": "7",
        "intro": "The subjonctif expresses subjectivity, emotions, doubts, and necessity. Learn how to form it and when to use it.",
        "sections": [
            {
                "title": "1. Forming the Subjonctif Présent",
                "items": [
                    "Take the ils/elles form of the present tense, drop -ent, and add endings: -e, -es, -e, -ions, -iez, -ent.",
                    "Example with parler (ils parlent): que je parle, que tu parles, qu'il parle, que nous parlions, que vous parliez, qu'ils parlent.",
                    "Key irregular stems: être (sois, soit, soyons, soyez, soient), avoir (aie, ait, ayons, ayez, aient).",
                    "Other essential irregular stems: faire (fass-), aller (aill- / all-), pouvoir (puiss-), savoir (sach-), vouloir (veuill- / voul-)."
                ]
            },
            {
                "title": "2. Core Subjunctive Triggers",
                "items": [
                    "Necessity & obligation: « Il faut que... », « Il est nécessaire que... », « Il est indispensable que... »",
                    "Wishes & desire: « Je veux que... », « Je souhaite que... », « J'aimerais que... »",
                    "Emotions & feelings: « Je suis content que... », « J'ai peur que... », « C'est dommage que... »",
                    "Remember: two different subjects are required (je veux que TU viennes; but je veux venir with one subject)."
                ]
            }
        ]
    }

    # Page 9: Subjonctif vs Indicatif
    pages[9] = {
        "page": 9,
        "type": "checklist",
        "title": "B1 Grammar: Subjonctif vs Indicatif",
        "subtitle": "Certainty vs Uncertainty, Belief & Doubt",
        "badge_num": "8",
        "intro": "Understand when to use the indicatif (for facts and certainty) versus the subjonctif (for doubts and possibilities).",
        "sections": [
            {
                "title": "1. Verbs of Opinion: Affirmative vs Negative",
                "items": [
                    "Affirmative opinion uses the indicatif: « Je pense qu'il a raison », « Je crois que c'est vrai. »",
                    "Negative opinion triggers the subjonctif: « Je ne pense pas qu'il ait raison », « Je ne crois pas que ce soit facile. »",
                    "Questions with inversion trigger the subjonctif: « Pensez-vous qu'elle puisse venir demain ? »",
                    "Verbs of certainty always take indicatif: « Il est certain que... », « Il est évident que... », « Je suis sûr que... »"
                ]
            },
            {
                "title": "2. Doubt, Possibility & Conjunctions",
                "items": [
                    "Doubt triggers subjunctive: « Il est douteux que... », « Je doute que nous arrivions à l'heure. »",
                    "Probability (indicatif) vs Possibility (subjonctif): « Il est probable qu'il viendra » vs « Il est possible qu'il vienne ».",
                    "Subjunctive conjunctions: pour que (so that), bien que (although), avant que (before), à condition que (provided that).",
                    "Indicative conjunctions: parce que (because), pendant que (while), depuis que (since), après que (after)."
                ]
            }
        ]
    }

    # Page 10: Le Conditionnel Présent & Passé
    pages[10] = {
        "page": 10,
        "type": "checklist",
        "title": "B1 Grammar: Le Conditionnel Présent & Passé",
        "subtitle": "Politeness, Wishes, Regrets & Unconfirmed Information",
        "badge_num": "9",
        "intro": "Use the conditionnel to soften requests, give diplomatic advice, express regrets about the past, and report unverified news.",
        "sections": [
            {
                "title": "1. Le Conditionnel Présent",
                "items": [
                    "Formation: future stem + imparfait endings (-ais, -ais, -ait, -ions, -iez, -aient): je voyagerais, nous aimerions.",
                    "Giving friendly advice: « Tu devrais en parler à ton responsable », « Vous feriez mieux de réserver à l'avance. »",
                    "Polite requests: « Pourriez-vous me transmettre ce document ? », « J'aimerais obtenir un renseignement. »",
                    "Journalistic unconfirmed news: « Le ministre démissionnerait selon des sources proches. »"
                ]
            },
            {
                "title": "2. Le Conditionnel Passé (Regrets & Past Hypotheses)",
                "items": [
                    "Formation: avoir or être in conditionnel présent + past participle: « J'aurais aimé », « Elle serait partie. »",
                    "Expressing past regrets: « J'aurais dû travailler davantage pour cet examen difficile. »",
                    "Expressing reproaches: « Tu aurais pu me prévenir plus tôt de ton absence ! »",
                    "Past hypotheses with Si: « Si j'avais su, je serais venu avec toi hier. »"
                ]
            }
        ]
    }

    # Page 11: Hypothèses avec 'Si'
    pages[11] = {
        "page": 11,
        "type": "checklist",
        "title": "B1 Grammar: Hypothèses avec 'Si'",
        "subtitle": "Three Levels of Hypotheses: Real, Potential & Imaginary",
        "badge_num": "10",
        "intro": "Learn how to express possibilities, future conditions, and imaginary scenarios using the 3 classic 'Si' structures.",
        "sections": [
            {
                "title": "1. Real & Potential Hypotheses",
                "items": [
                    "Type 1: Real / Likely condition (Si + Présent → Futur Simple / Impératif): « Si tu viens ce soir, nous dînerons ensemble. »",
                    "Type 1 with Imperative: « Si vous avez des questions, n'hésitez pas à me contacter. »",
                    "Type 2: Imaginary / Potential condition (Si + Imparfait → Conditionnel Présent): « Si j'avais un million d'euros, je voyagerais autour du monde. »",
                    "Giving advice with Type 2: « Si j'étais à ta place, je postulerais à cette offre d'emploi. »"
                ]
            },
            {
                "title": "2. Past Unfulfilled Hypotheses & Rule of 'Si'",
                "items": [
                    "Type 3: Impossible past condition (Si + Plus-que-parfait → Conditionnel Passé): « Si nous étions partis plus tôt, nous n'aurions pas raté l'avion. »",
                    "Mixed condition (past cause, present result): « Si j'avais appris le français plus jeune, je le parlerais couramment aujourd'hui. »",
                    "The golden rule: NEVER put future or conditionnel right after 'si' (« Les 'si' n'aiment pas les 'rais' »).",
                    "Expressing conditions without 'si': en cas de + nom, à condition de + infinitif, avec ou sans."
                ]
            }
        ]
    }

    # Page 12: Pronoms Relatifs Composés & 'Dont'
    pages[12] = {
        "page": 12,
        "type": "checklist",
        "title": "B1 Grammar: Pronoms Relatifs Composés & 'Dont'",
        "subtitle": "Connecting Ideas with Dont, Lequel, Auquel, and Duquel",
        "badge_num": "11",
        "intro": "Level up your sentences by mastering 'dont' (replaces de) and compound relative pronouns like 'lequel' and 'auquel'.",
        "sections": [
            {
                "title": "1. The Relative Pronoun 'Dont'",
                "items": [
                    "Dont replaces a noun introduced by 'de': « C'est le livre dont je t'ai parlé hier » (parler de quelque chose).",
                    "Dont with verbs: avoir besoin de, avoir envie de, se souvenir de: « L'outil dont j'ai besoin est sur la table. »",
                    "Dont expresses possession: « J'ai rencontré une collègue dont le travail est passionnant. »",
                    "Dont with quantities: « Il y avait dix candidats, dont trois étudiants étrangers. »"
                ]
            },
            {
                "title": "2. Compound Relative Pronouns (Lequel, Auquel, Duquel)",
                "items": [
                    "Lequel, laquelle, lesquels, lesquelles (with prepositions like avec, sans, pour, sur): « La table sur laquelle j'écris. »",
                    "Auquel, à laquelle, auxquels, auxquelles (with à): « Le projet auquel je participe activement. »",
                    "Duquel, de laquelle, desquels, desquelles (with compound prepositions: près de, à côté de): « L'arbre à côté duquel je me suis assis. »",
                    "Note: use qui (not lequel) when referring to people after prepositions: « L'ami avec qui je voyage. »"
                ]
            }
        ]
    }

    # Page 13: Pronoms Relatifs Indéfinis (Ce qui, Ce que, Ce dont)
    pages[13] = {
        "page": 13,
        "type": "checklist",
        "title": "B1 Grammar: Pronoms Relatifs Indéfinis",
        "subtitle": "Using Ce qui, Ce que, Ce dont, and Ce à quoi for Emphasis",
        "badge_num": "12",
        "intro": "Use indefinite relative pronouns to refer to abstract ideas, whole sentences, or to emphasize what you mean.",
        "sections": [
            {
                "title": "1. Ce qui, Ce que, and Ce dont",
                "items": [
                    "Ce qui is the subject (followed by a verb): « Dis-moi ce qui s'est passé ce matin. »",
                    "Ce que is the direct object (followed by subject + verb): « Je ne comprends pas ce que tu dis. »",
                    "Ce dont replaces de + noun/idea: « Ce dont j'ai le plus besoin en ce moment, c'est de repos. »",
                    "Ce à quoi replaces à + idea: « Ce à quoi je pense est un projet innovant pour l'entreprise. »"
                ]
            },
            {
                "title": "2. Emphasizing Ideas (La Mise en Relief)",
                "items": [
                    "Emphasize the subject: « C'est Paul qui a rédigé le rapport », « Ce sont mes collègues qui m'ont soutenu. »",
                    "Emphasize the object: « C'est ce livre que je préfère entre tous. »",
                    "Structure with Ce qui / Ce que... c'est: « Ce qui me passionne, c'est l'histoire de France. »",
                    "Structure with Ce dont... c'est: « Ce dont je suis fier, c'est d'avoir réussi cet examen par moi-même. »"
                ]
            }
        ]
    }

    # Page 14: Le Discours Indirect au Passé
    pages[14] = {
        "page": 14,
        "type": "checklist",
        "title": "B1 Grammar: Le Discours Indirect au Passé",
        "subtitle": "Reporting Past Speech and Tense Agreement",
        "badge_num": "13",
        "intro": "Learn how to report what someone said in the past without repeating their exact words, adjusting tenses accurately.",
        "sections": [
            {
                "title": "1. Tense Shifts in Past Reported Speech",
                "items": [
                    "Present shifts to Imparfait: Il a dit : « Je suis fatigué » → Il a dit qu'il ÉTAIT fatigué.",
                    "Passé composé shifts to Plus-que-parfait: Il a dit : « J'ai fini » → Il a dit qu'il AVAIT FINI.",
                    "Futur simple shifts to Conditionnel présent: Il a dit : « Je viendrai » → Il a dit qu'il VIENDRAIT.",
                    "Futur proche shifts to Imparfait of aller + inf: Il a dit : « Je vais partir » → Il a dit qu'il ALLAIT PARTIR."
                ]
            },
            {
                "title": "2. Time Word Adjustments & Reporting Verbs",
                "items": [
                    "Aujourd'hui becomes ce jour-là; demain becomes le lendemain; hier becomes la veille.",
                    "Ici becomes là-bas; cette semaine becomes cette semaine-là.",
                    "Reporting questions with si (yes/no): « Est-ce que tu viens ? » → Il m'a demandé SI je venais.",
                    "Use varied reporting verbs: affirmer, expliquer, prétendre, annoncer, promettre, souligner."
                ]
            }
        ]
    }

    # Page 15: La Voix Passive & Formes Passives
    pages[15] = {
        "page": 15,
        "type": "checklist",
        "title": "B1 Grammar: La Voix Passive & Formes Passives",
        "subtitle": "Forming the Passive Voice and Using Natural Alternatives",
        "badge_num": "14",
        "intro": "The passive voice is common in French journalism, administrative reports, and historical writing.",
        "sections": [
            {
                "title": "1. Forming the Passive Voice",
                "items": [
                    "Formation: Être (in the required tense) + past participle + par + agent: « Le pont a été construit en 1900 par Eiffel. »",
                    "Past participle agreement: always agrees in gender and number with the subject: « La décision sera annoncée demain. »",
                    "Use 'de' instead of 'par' with verbs of feeling and state: aimé de, respecté de, entouré de, suivi de.",
                    "Passive in different tenses: le texte est écrit (present), a été écrit (past), sera écrit (future)."
                ]
            },
            {
                "title": "2. Natural Active Alternatives to the Passive",
                "items": [
                    "Use 'on' for general actions (preferred in spoken French): « On a trouvé une solution » instead of « Une solution a été trouvée. »",
                    "Use pronominal passive verbs: « Ce produit se vend très bien », « Cette langue s'apprend facilement. »",
                    "Use faire + infinitive for actions done by someone else: « Je fais réparer ma voiture au garage. »",
                    "Use laisser + infinitive: « Elle s'est laissé convaincre par ses amis. »"
                ]
            }
        ]
    }

    # Page 16: Le Gérondif & Participe Présent
    pages[16] = {
        "page": 16,
        "type": "checklist",
        "title": "B1 Grammar: Le Gérondif & Participe Présent",
        "subtitle": "Expressing Simultaneity, Means, and Cause with En + -ant",
        "badge_num": "15",
        "intro": "The gérondif links two actions happening at the same time and explains how or why an action happened.",
        "sections": [
            {
                "title": "1. Forming the Gérondif (En + Stem + -ant)",
                "items": [
                    "Take the nous form of the present tense, drop -ons, and add -ant: nous parlons → en parlant, nous finissons → en finissant.",
                    "Irregular gérondifs: être (en étant), avoir (en ayant), savoir (en sachant).",
                    "Rule: both actions must have the exact same subject: « En marchant, Paul écoute de la musique. »",
                    "Expressing simultaneity (while doing): « J'ai rencontré un vieil ami en faisant mes courses au marché. »"
                ]
            },
            {
                "title": "2. Expressing Means, Cause & Condition",
                "items": [
                    "Expressing means (by doing): « C'est en pratiquant tous les jours qu'on apprend une langue. »",
                    "Expressing cause (because of doing): « En arrivant en retard, il a manqué le début de la réunion. »",
                    "Expressing condition (if you do): « En travaillant avec rigueur, tu réussiras ton examen. »",
                    "Add 'tout' for contrast or emphasis: « Tout en étant d'accord, il a émis quelques réserves. »"
                ]
            }
        ]
    }

    # Page 17: Le Plus-que-parfait
    pages[17] = {
        "page": 17,
        "type": "checklist",
        "title": "B1 Grammar: Le Plus-que-parfait",
        "subtitle": "The 'Past of the Past' and Temporal Anteriority",
        "badge_num": "16",
        "intro": "When telling a story in the past, use the plus-que-parfait to describe actions that had already happened earlier.",
        "sections": [
            {
                "title": "1. Forming the Plus-que-parfait",
                "items": [
                    "Auxiliary avoir or être in the imparfait + past participle: j'avais parlé, j'étais venu(e).",
                    "With avoir: j'avais fini, tu avais compris, nous avions mangé, ils avaient vu.",
                    "With être (movement & reflexive verbs): j'étais parti(e), elle s'était levée, nous étions rentrés.",
                    "Participle agreement rules are identical to the passé composé."
                ]
            },
            {
                "title": "2. Usage in Past Narration & 'Si' Clauses",
                "items": [
                    "Describing anteriority in stories: « Quand la police est arrivée, les cambrioleurs s'étaient déjà enfuis. »",
                    "Explaining past causes: « Il n'avait pas faim parce qu'il avait déjà déjeuné avec ses collègues. »",
                    "Hypotheses with Si: « Si tu m'avais prévenu, j'aurais préparé une chambre d'amis. »",
                    "Expressing solitary regrets with Si seulement: « Si seulement j'avais su la vérité plus tôt ! »"
                ]
            }
        ]
    }

    # Page 18: Connecteurs Logiques (Cause, Conséquence & But)
    pages[18] = {
        "page": 18,
        "type": "checklist",
        "title": "B1 Grammar: Connecteurs Logiques (Part 1)",
        "subtitle": "Expressing Cause, Consequence & Purpose in Complex Sentences",
        "badge_num": "17",
        "intro": "Move beyond basic connectors. Use precise B1 transition words to structure sophisticated paragraphs.",
        "sections": [
            {
                "title": "1. Expressing Cause (Why Something Happens)",
                "items": [
                    "Puisque (since / as everyone knows): « Puisque tu es libre demain, viens nous rejoindre à la fête. »",
                    "Comme (as - placed at start of sentence): « Comme il pleuvait des cordes, nous sommes restés à la maison. »",
                    "En raison de / À cause de (negative/neutral cause + noun): « Le vol a été annulé en raison du brouillard. »",
                    "Grâce à (positive cause + noun): « J'ai réussi cet examen grâce à votre aide précieuse. »"
                ]
            },
            {
                "title": "2. Expressing Consequence & Purpose",
                "items": [
                    "Par conséquent / En conséquence (therefore): « La demande a augmenté, par conséquent nous embauchons. »",
                    "C'est pourquoi / Ainsi (that is why / thus): « Le train est en grève, c'est pourquoi je télétravaille. »",
                    "Pour que / Afin que (+ Subjonctif): « Je vous explique les consignes pour que vous compreniez bien. »",
                    "Pour / Afin de (+ Infinitif when subjects are the same): « Je prends des cours afin d'améliorer mon français. »"
                ]
            }
        ]
    }

    # Page 19: Connecteurs Logiques (Opposition & Concession)
    pages[19] = {
        "page": 19,
        "type": "checklist",
        "title": "B1 Grammar: Connecteurs Logiques (Part 2)",
        "subtitle": "Expressing Contrast, Concession & Restriction",
        "badge_num": "18",
        "intro": "Master the art of nuance by learning how to contrast two facts and express concessions in debates.",
        "sections": [
            {
                "title": "1. Expressing Opposition (Contrasting Two Facts)",
                "items": [
                    "Alors que / Tandis que (while / whereas): « Paul préfère la ville tandis que Marie adore la campagne. »",
                    "Au lieu de (+ Infinitif / Nom): « Au lieu de te plaindre, propose des solutions constructives. »",
                    "Par contre / En revanche (on the other hand): « Ce logement est petit ; en revanche, il est très lumineux. »",
                    "Contrairement à (+ Nom): « Contrairement à nos prévisions, l'événement a attiré beaucoup de monde. »"
                ]
            },
            {
                "title": "2. Expressing Concession (Unexpected Outcomes)",
                "items": [
                    "Bien que / Quoique (+ Subjonctif): « Bien qu'il soit jeune, il gère une équipe de dix personnes avec succès. »",
                    "Malgré (+ Nom): « Malgré la pluie battante, nous avons poursuivi notre randonnée en montagne. »",
                    "Cependant / Pourtant / Néanmoins (however / yet): « Il a beaucoup révisé ; pourtant, il a trouvé l'épreuve difficile. »",
                    "Quand même / Tout de même (still / all the same): « C'est un peu risqué, mais je vais essayer quand même ! »"
                ]
            }
        ]
    }

    # Pages 20-29: Thematic Vocabulary Modules (Tables with 10 rows)
    # Page 20: Society, Migration & Diversity
    pages[20] = {
        "page": 20,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Society, Migration & Diversity",
        "subtitle": "Multicultural Communities, Integration & Solidarity",
        "badge_num": "19",
        "intro": "Essential terms to discuss immigration, community solidarity, and social diversity in the Francophone world.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'intégration", "n.f.", "integration / inclusion", "« L'apprentissage de la langue favorise une bonne intégration sociale. »"],
                ["la diversité", "n.f.", "diversity", "« La diversité culturelle constitue une véritable richesse pour le pays. »"],
                ["le bénévole", "n.m.", "volunteer", "« De nombreux bénévoles s'investissent auprès des personnes isolées. »"],
                ["la citoyenneté", "n.f.", "citizenship", "« L'obtention de la citoyenneté s'accompagne de droits et de devoirs. »"],
                ["la solidarité", "n.f.", "solidarity / mutual help", "« Un bel élan de solidarité s'est manifesté après les inondations. »"],
                ["s'adapter", "v. pron.", "to adapt oneself", "« Les nouveaux arrivants apprennent à s'adapter aux coutumes locales. »"],
                ["l'association", "n.f.", "non-profit organization", "« Cette association lutte contre la précarité et l'exclusion sociale. »"],
                ["le réfugié", "n.m.", "refugee", "« Les réfugiés bénéficient du droit d'asile selon les traités internationaux. »"],
                ["la discrimination", "n.f.", "discrimination", "« La loi punit sévèrement toute forme de discrimination à l'embauche. »"],
                ["le vivre-ensemble", "n.m.", "social harmony / coexistence", "« Le respect des différences est indispensable au vivre-ensemble républicain. »"]
            ]
        }
    }

    # Page 21: Ecology, Sustainable Development & Climate Action
    pages[21] = {
        "page": 21,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Ecology & Climate Action",
        "subtitle": "Renewable Energy, Recycling & Protecting Nature",
        "badge_num": "20",
        "intro": "Vocabulary to discuss global warming, environmental initiatives, and sustainable habits for the future.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le réchauffement climatique", "n.m.", "global warming", "« Le réchauffement climatique entraîne la fonte accélérée des glaciers. »"],
                ["l'énergie renouvelable", "n.f.", "renewable energy", "« Il faut investir davantage dans les énergies renouvelables comme l'éolien. »"],
                ["la biodiversité", "n.f.", "biodiversity", "« La préservation des forêts est vitale pour maintenir la biodiversité. »"],
                ["le tri sélectif", "n.m.", "waste sorting / recycling", "« Tous les habitants participent activement au tri sélectif des déchets. »"],
                ["l'empreinte carbone", "n.f.", "carbon footprint", "« Prendre le train au lieu de l'avion réduit fortement l'empreinte carbone. »"],
                ["la pollution", "n.f.", "pollution", "« Les grandes villes prennent des mesures pour limiter la pollution de l'air. »"],
                ["durable", "adj.", "sustainable", "« L'agriculture durable protège à la fois la santé et les sols nourriciers. »"],
                ["les déchets", "n.m.pl.", "waste / trash", "« De nombreuses initiatives visent à réduire les emballages et les déchets. »"],
                ["menacer", "v.", "to threaten / endanger", "« L'urbanisation rapide menace les habitats naturels de nombreuses espèces. »"],
                ["la transition écologique", "n.f.", "ecological transition", "« La transition écologique nécessite l'engagement des citoyens et des gouvernements. »"]
            ]
        }
    }

    # Page 22: Employment, Workplace Rights & Labor Relations
    pages[22] = {
        "page": 22,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Employment & Labor Rights",
        "subtitle": "Working Conditions, Trade Unions & Career Evolution",
        "badge_num": "21",
        "intro": "Professional vocabulary to discuss working conditions, employment contracts, and labor negotiations.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le contrat de travail", "n.m.", "employment contract", "« Avant de commencer votre poste, lisez attentivement votre contrat de travail. »"],
                ["le licenciement", "n.m.", "layoff / dismissal", "« La fermeture de l'usine a provoqué le licenciement de cinquante salariés. »"],
                ["la grève", "n.f.", "strike / walkout", "« Les cheminots sont en grève pour réclamer une hausse des salaires. »"],
                ["le syndicat", "n.m.", "trade union", "« Le syndicat négocie les conditions de travail avec la direction générale. »"],
                ["l'augmentation", "n.f.", "pay rise / increase", "« Les employés demandent une augmentation salariale liée à l'inflation. »"],
                ["le congé payé", "n.m.", "paid holiday / leave", "« En France, les salariés bénéficient de cinq semaines de congés payés par an. »"],
                ["la reconversion professionnelle", "n.f.", "career change / retraining", "« Après dix ans dans la finance, elle a entamé une reconversion dans l'artisanat. »"],
                ["les heures supplémentaires", "n.f.pl.", "overtime hours", "« Les heures supplémentaires sont rémunérées à un taux majoré selon la loi. »"],
                ["postuler", "v.", "to apply for a job", "« J'ai postulé à cette offre en envoyant mon CV et une lettre de motivation. »"],
                ["l'équilibre vie pro-vie perso", "n.m.", "work-life balance", "« Le télétravail contribue souvent à un meilleur équilibre vie pro-vie perso. »"]
            ]
        }
    }

    # Page 23: Digital Revolution, Social Networks & AI
    pages[23] = {
        "page": 23,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Digital Revolution & AI",
        "subtitle": "Internet Ethics, Social Media & Emerging Technologies",
        "badge_num": "22",
        "intro": "Key terminology to talk about artificial intelligence, social media influence, data privacy, and digital habits.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'intelligence artificielle", "n.f.", "artificial intelligence (AI)", "« L'intelligence artificielle transforme en profondeur le monde médical et éducatif. »"],
                ["les données personnelles", "n.f.pl.", "personal data", "« Les lois européennes protègent strictement la confidentialité des données personnelles. »"],
                ["l'infox / fausse nouvelle", "n.f.", "fake news / misinformation", "« Il est indispensable de vérifier ses sources pour ne pas relayer d'infox. »"],
                ["le réseau social", "n.m.", "social network", "« Les influenceurs utilisent les réseaux sociaux pour promouvoir des produits. »"],
                ["la cybersécurité", "n.f.", "cybersecurity", "« Les entreprises investissent massivement pour renforcer leur cybersécurité. »"],
                ["l'écran", "n.m.", "screen", "« Passer trop de temps devant les écrans perturbe le sommeil des enfants. »"],
                ["le piratage informatique", "n.m.", "computer hacking", "« Le piratage des comptes bancaires en ligne représente un défi croissant. »"],
                ["l'algorithme", "n.m.", "algorithm", "« Les algorithmes personnalisent le contenu affiché selon vos centres d'intérêt. »"],
                ["se déconnecter", "v. pron.", "to disconnect / go offline", "« Il est conseillé de se déconnecter complètement pendant les week-ends. »"],
                ["numérique", "adj.", "digital", "« La transformation numérique facilite l'accès aux démarches administratives. »"]
            ]
        }
    }

    # Page 24: Media, Press Freedom & Information Ethics
    pages[24] = {
        "page": 24,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Media & Press Freedom",
        "subtitle": "Journalism, Censorship, Opinion Columns & News Channels",
        "badge_num": "23",
        "intro": "Vocabulary to discuss press independence, news media channels, investigative reporting, and freedom of speech.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la liberté de la presse", "n.f.", "freedom of the press", "« La liberté de la presse est garantie par la déclaration des droits de l'homme. »"],
                ["le journaliste d'investigation", "n.m.", "investigative journalist", "« Ce journaliste d'investigation a révélé une affaire de corruption majeure. »"],
                ["la une", "n.f.", "front page (newspaper)", "« Cette victoire historique des athlètes français fait la une de tous les journaux. »"],
                ["l'éditorial", "n.m.", "editorial / opinion column", "« L'éditorial du rédacteur en chef analyse la crise économique actuelle. »"],
                ["la censure", "n.f.", "censorship", "« Les régimes autoritaires imposent souvent une stricte censure des médias. »"],
                ["la source fiable", "n.f.", "reliable source", "« Un bon reporter doit toujours croiser plusieurs sources fiables d'information. »"],
                ["le sondage d'opinion", "n.m.", "opinion poll / survey", "« Selon le dernier sondage d'opinion, une majorité de citoyens soutient cette réforme. »"],
                ["le reportage", "n.m.", "news report / documentary", "« La chaîne publique a diffusé un reportage saisissant sur l'Arctique. »"],
                ["diffuser", "v.", "to broadcast / air", "« Cette station de radio diffuse des informations en continu vingt-quatre heures sur vingt-quatre. »"],
                ["le droit d'auteur", "n.m.", "copyright / author rights", "« La loi protège les créateurs de contenu grâce au respect du droit d'auteur. »"]
            ]
        }
    }

    # Page 25: Culture, Heritage & Francophone Diversity
    pages[25] = {
        "page": 25,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Culture & Francophonie",
        "subtitle": "Artistic Heritage, Traditions & The Francophone World",
        "badge_num": "24",
        "intro": "Terms to discuss French literature, heritage sites, and the rich linguistic diversity of the Francophone world.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le patrimoine culturel", "n.m.", "cultural heritage", "« La gastronomie française est inscrite au patrimoine culturel de l'UNESCO. »"],
                ["la Francophonie", "n.f.", "the Francophone community", "« La Francophonie réunit plus de 300 millions de locuteurs sur cinq continents. »"],
                ["le chef-d'œuvre", "n.m.", "masterpiece", "« Le tableau de la Joconde au musée du Louvre est un chef-d'œuvre universel. »"],
                ["le monument historique", "n.m.", "historic monument", "« La cathédrale Notre-Dame de Paris est un monument historique emblématique. »"],
                ["la tradition séculaire", "n.f.", "centuries-old tradition", "« Ce village de Provence perpétue une tradition séculaire de fabrication du savon. »"],
                ["le vernissage", "n.m.", "gallery opening / preview", "« Nous sommes invités au vernissage de la nouvelle exposition de peinture ce soir. »"],
                ["un extrait littéraire", "n.m.", "literary excerpt", "« En classe, nous avons étudié un extrait littéraire de Victor Hugo. »"],
                ["le metteur en scène", "n.m.", "theater / movie director", "« Le metteur en scène a proposé une interprétation moderne de cette pièce classique. »"],
                ["transmettre", "v.", "to pass down / transmit", "« Les aînés ont à cœur de transmettre leur savoir et leurs coutumes aux jeunes. »"],
                ["le rayonnement culturel", "n.m.", "cultural influence / reach", "« Le cinéma et la mode contribuent au rayonnement culturel de la France. »"]
            ]
        }
    }

    # Page 26: Higher Education, Academic Mobility & Research
    pages[26] = {
        "page": 26,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Higher Education & Research",
        "subtitle": "University Life, Erasmus Mobility & Degrees",
        "badge_num": "25",
        "intro": "Vocabulary for navigating university studies, study-abroad programs, academic research, and exams.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'enseignement supérieur", "n.m.", "higher education", "« Les universités et les grandes écoles composent l'enseignement supérieur français. »"],
                ["la bourse d'études", "n.f.", "scholarship / study grant", "« Il a obtenu une bourse d'études au mérite pour financer son master à l'étranger. »"],
                ["le programme Erasmus", "n.m.", "Erasmus mobility exchange", "« De nombreux étudiants européens partent un an en France grâce au programme Erasmus. »"],
                ["la licence / le master", "n.", "Bachelor's / Master's degree", "« Après sa licence de lettres modernes, elle prépare un master en communication. »"],
                ["le mémoire de recherche", "n.m.", "dissertation / research thesis", "« Il doit soutenir son mémoire de recherche devant un jury à la fin du semestre. »"],
                ["l'amphithéâtre", "n.m.", "lecture hall", "« Le cours magistral d'histoire réunit deux cents étudiants dans l'amphithéâtre. »"],
                ["le stage obligatoire", "n.m.", "mandatory internship", "« Les étudiants doivent valider un stage obligatoire de trois mois en entreprise. »"],
                ["s'inscrire à l'université", "expr.", "to enroll at university", "« Les inscriptions universitaires ouvrent au mois de juillet sur la plateforme nationale. »"],
                ["échouer / réussir un examen", "expr.", "to fail / pass an exam", "« Elle a révisé avec persévérance et a réussi tous ses examens du premier coup. »"],
                ["la passerelle", "n.f.", "academic pathway / bridge", "« Ce diplôme offre des passerelles vers les métiers du journalisme et de l'édition. »"]
            ]
        }
    }

    # Page 27: Health, Bioethics & Medical Advances
    pages[27] = {
        "page": 27,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Health, Bioethics & Medicine",
        "subtitle": "Public Health, Prevention, Mental Well-Being & Ethics",
        "badge_num": "26",
        "intro": "Discuss medical care, health insurance systems, mental wellness, and modern bioethical questions.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la Sécurité sociale", "n.f.", "national health insurance", "« La Sécurité sociale rembourse une grande partie des consultations médicales. »"],
                ["la mutuelle de santé", "n.f.", "complementary health insurance", "« Il est conseillé de souscrire une bonne mutuelle pour couvrir les soins dentaires. »"],
                ["la prévention", "n.f.", "disease prevention", "« Les campagnes de prévention rappellent l'importance du dépistage régulier. »"],
                ["la santé mentale", "n.f.", "mental health", "« Prendre soin de sa santé mentale est tout aussi important que la santé physique. »"],
                ["l'effet secondaire", "n.m.", "side effect", "« Lisez attentivement la notice pour connaître les effets secondaires possibles. »"],
                ["le vaccin", "n.m.", "vaccine", "« La vaccination protège la population contre les maladies infectieuses graves. »"],
                ["le traitement médical", "n.m.", "medical treatment / therapy", "« Le médecin a prescrit un traitement médical adapté pour soulager ses douleurs. »"],
                ["la thérapie", "n.f.", "therapy / counseling", "« Elle consulte un psychologue pour suivre une thérapie après son burn-out. »"],
                ["l'espérance de vie", "n.f.", "life expectancy", "« Les progrès de la médecine ont permis d'augmenter nettement l'espérance de vie. »"],
                ["la bioéthique", "n.f.", "bioethics", "« Les lois de bioéthique encadrent la recherche génétique et les dons d'organes. »"]
            ]
        }
    }

    # Page 28: Responsible Consumption, Fair Trade & Circular Economy
    pages[28] = {
        "page": 28,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Consumption & Circular Economy",
        "subtitle": "Ethical Shopping, Fair Trade, Repairability & Zero-Waste",
        "badge_num": "27",
        "intro": "Vocabulary for discussing conscious consumer choices, fair trade products, circular economy, and zero waste.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le commerce équitable", "n.m.", "fair trade", "« Acheter du café issu du commerce équitable garantit un revenu juste aux producteurs. »"],
                ["l'économie circulaire", "n.f.", "circular economy", "« L'économie circulaire vise à recycler et réutiliser les matériaux au lieu de les jeter. »"],
                ["le gaspillage alimentaire", "n.f.", "food waste", "« De nombreuses applications permettent aux commerçants de lutter contre le gaspillage. »"],
                ["les produits de saison", "n.m.pl.", "seasonal produce", "« Consommer des fruits et légumes de saison est meilleur pour le goût et la planète. »"],
                ["le circuit court", "n.m.", "direct-from-producer sales", "« Acheter directement à la ferme en circuit court supprime les intermédiaires. »"],
                ["l'obsolescence programmée", "n.f.", "planned obsolescence", "« La loi française interdit l'obsolescence programmée des appareils électroniques. »"],
                ["l'indice de réparabilité", "n.m.", "repairability score / index", "« Vérifiez l'indice de réparabilité avant d'acheter un ordinateur ou un smartphone. »"],
                ["d'occasion / de seconde main", "expr.", "second-hand / pre-owned", "« J'ai acheté ce meuble en bois d'occasion dans une brocante du quartier. »"],
                ["le mode de vie zéro déchet", "n.m.", "zero-waste lifestyle", "« Adopter un mode de vie zéro déchet commence par l'achat d'aliments en vrac. »"],
                ["boycotter", "v.", "to boycott", "« Les consommateurs ont décidé de boycotter cette marque pour protester contre ses pratiques. »"]
            ]
        }
    }

    # Page 29: Justice, Law, Human Rights & Citizenship
    pages[29] = {
        "page": 29,
        "type": "vocab_table",
        "title": "B1 Thematic Vocabulary: Justice, Law & Citizenship",
        "subtitle": "Legal Rights, Court Procedures & Human Rights",
        "badge_num": "28",
        "intro": "Essential terms to understand legal debates, court procedures, human rights, and democratic processes in France.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'état de droit", "n.m.", "the rule of law", "« Le respect de l'état de droit garantit les libertés fondamentales de chaque citoyen. »"],
                ["les droits fondamentaux", "n.m.pl.", "fundamental human rights", "« La constitution protège les droits fondamentaux de tous les individus sans distinction. »"],
                ["l'avocat de la défense", "n.m.", "defense lawyer / attorney", "« L'avocat de la défense a plaidé l'acquittement de son client devant la cour. »"],
                ["le tribunal / le juge", "n.", "court / judge", "« L'affaire a été examinée par le tribunal judiciaire de grande instance. »"],
                ["le témoin", "n.m.", "witness", "« Plusieurs témoins oculaires ont été entendus par les enquêteurs de police. »"],
                ["la loi / voter une loi", "expr.", "law / to pass a law", "« L'Assemblée nationale a voté une nouvelle loi pour protéger l'environnement. »"],
                ["porter plainte", "expr.", "to file a formal complaint", "« La victime s'est rendue au commissariat pour porter plainte après le vol de son sac. »"],
                ["la présomption d'innocence", "n.f.", "presumption of innocence", "« Tout accusé bénéficie de la présomption d'innocence jusqu'au verdict final. »"],
                ["l'amende", "n.f.", "fine / penalty", "« Stationner sur une place handicapée est passible d'une amende de 135 euros. »"],
                ["le devoir civique", "n.m.", "civic duty", "« Participer aux scrutins électoraux est un devoir civique pour chaque citoyen. »"]
            ]
        }
    }

    # Pages 30-39: Spoken Production & Interaction
    # Page 30: Monologue Suivi: Expressing an Opinion on Society [Respect illustration!]
    pages[30] = {
        "page": 30,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Expressing an Opinion",
        "subtitle": "Structuring a 3-Minute Monologue on a Society Topic",
        "badge_num": "29",
        "intro": "At CEFR B1, you can speak continuously for 2.5 to 3 minutes, presenting your viewpoint on a controversial issue clearly.",
        "sections": [
            {
                "title": "1. Introducing Your Topic & Thematic Hook",
                "items": [
                    "Introduce the document or topic: « Ce document aborde la question cruciale du télétravail dans notre société. »",
                    "Pose the central debate question: « On peut donc se demander si cette pratique est bénéfique pour tous. »",
                    "Announce your presentation plan: « Dans un premier temps, j'évoquerai les avantages, puis j'aborderai les limites. »"
                ]
            },
            {
                "title": "2. Developing Your Argument",
                "items": [
                    "Present arguments in favor: « D'un côté, cela permet de réduire le stress lié aux transports quotidiens. »",
                    "Provide concrete examples: « Par exemple, de nombreux salariés gagnent deux heures par jour. »",
                    "Conclude with your personal stance: « En conclusion, je suis convaincu que le modèle hybride est le plus équilibré. »"
                ]
            }
        ]
    }

    # Page 31: Monologue Suivi: Structuring an Argument with Examples
    pages[31] = {
        "page": 31,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Developing Arguments with Examples",
        "subtitle": "Connecting Points Logically and Providing Supporting Evidence",
        "badge_num": "30",
        "intro": "Back up your claims with convincing illustrations, personal experiences, and logical transitions.",
        "sections": [
            {
                "title": "1. Introducing Compelling Evidence",
                "items": [
                    "Illustrate a point: « Prenons l'exemple de la gratuité des transports publics dans plusieurs villes. »",
                    "Share personal observations: « D'après ma propre expérience, l'apprentissage d'une langue ouvre l'esprit. »",
                    "Cite general trends: « Les études montrent qu'une majorité de jeunes privilégient les mobilités douces. »",
                    "Use contrast effectively: « Certes, cette mesure a un coût élevé, mais ses bénéfices écologiques sont indéniables. »"
                ]
            },
            {
                "title": "2. Smooth Transitions Between Points",
                "items": [
                    "Moving to a second argument: « En outre, il convient d'ajouter que cette réforme favorise l'égalité des chances. »",
                    "Addressing counterarguments: « Certains affirment que c'est impossible ; pourtant, les faits prouvent le contraire. »",
                    "Reinforcing an idea: « Non seulement cela stimule l'économie, mais cela renforce également le lien social. »",
                    "Ending with an open question: « Cela ne devrait-il pas nous inciter à repenser complètement nos modes de vie ? »"
                ]
            }
        ]
    }

    # Page 32: Debating: Presenting Counterarguments & Defending
    pages[32] = {
        "page": 32,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Debating & Defending Opinions",
        "subtitle": "Answering Examiner Questions and Defending Your Point of View",
        "badge_num": "31",
        "intro": "In the DELF B1 debate, the examiner will challenge your arguments. Learn how to respond diplomatically and firmly.",
        "sections": [
            {
                "title": "1. Conceding Points Politely (La Concession)",
                "items": [
                    "Acknowledge the examiner's point: « Vous avez tout à fait raison de souligner cet aspect du problème. »",
                    "Introduce your counter-perspective: « Néanmoins, on ne peut pas ignorer les retombées positives à long terme. »",
                    "Clarify misunderstandings: « Ce n'est pas exactement ce que je voulais dire ; permettez-moi de préciser ma pensée. »",
                    "Balance the debate: « Il est vrai que cela demande des efforts financiers, mais l'enjeu climatique est primordial. »"
                ]
            },
            {
                "title": "2. Holding Your Ground and Concluding",
                "items": [
                    "Reiterate your main point: « Je maintiens donc que cette mesure est non seulement utile mais urgente. »",
                    "Express nuanced certainty: « Je reste persuadé que les citoyens sont prêts pour un tel changement. »",
                    "Defend personal choices: « Pour ma part, j'ai déjà adopté cette démarche et j'en constate les bienfaits. »",
                    "Close the debate with courtesy: « C'est pourquoi je pense qu'un dialogue constructif reste la meilleure voie à suivre. »"
                ]
            }
        ]
    }

    # Page 33: Problem-Solving in Unfamiliar Situations
    pages[33] = {
        "page": 33,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Problem-Solving & Role-Plays",
        "subtitle": "Handling Disputes, Bureaucracy & Unexpected Glitches",
        "badge_num": "32",
        "intro": "In DELF B1 part 2, you must resolve an everyday dispute with a clerk, landlord, or agency representative.",
        "sections": [
            {
                "title": "1. Explaining the Problem Firmly and Politely",
                "items": [
                    "Describe the error clearly: « Bonjour, je viens vers vous car j'ai constaté une erreur sur ma facture de téléphone. »",
                    "State the facts and timeline: « J'ai souscrit ce forfait le mois dernier et on m'a facturé des frais non prévus. »",
                    "Show relevant evidence: « Voici le contrat original ainsi que la preuve de paiement effectuée le 5 du mois. »",
                    "Remain calm and constructive: « Je comprends votre position, mais vous conviendrez que cette situation est anormale. »"
                ]
            },
            {
                "title": "2. Negotiating a Fair Resolution",
                "items": [
                    "Ask for an immediate remedy: « Je souhaiterais obtenir un remboursement ou un avoir sur ma prochaine facture. »",
                    "Propose a compromise: « Si vous ne pouvez pas me rembourser aujourd'hui, pourriez-vous prolonger mon abonnement ? »",
                    "Ask to speak to a manager if needed: « Dans ce cas, puis-je m'entretenir avec votre responsable hiérarchique ? »",
                    "Confirm the agreed outcome: « Nous sommes donc bien d'accord : vous créditez mon compte de cinquante euros d'ici vendredi ? »"
                ]
            }
        ]
    }

    # Page 34: Nuanced Agreement & Constructive Disagreement
    pages[34] = {
        "page": 34,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Nuanced Agreement & Disagreement",
        "subtitle": "Moving Beyond 'Oui' and 'Non' in Everyday Discussions",
        "badge_num": "33",
        "intro": "French conversational culture values nuanced reasoning. Learn how to agree partly, disagree with tact, and qualify statements.",
        "sections": [
            {
                "title": "1. Expressing Partial Agreement",
                "items": [
                    "« Je partage votre avis sur ce point, mais il faut regarder la situation dans son ensemble. »",
                    "« C'est en partie vrai, même si d'autres facteurs entrent également en jeu. »",
                    "« Jusqu'à un certain point, oui, mais cela ne règle pas le problème de fond. »",
                    "« On ne peut qu'être d'accord avec ce principe général, bien que son application soit complexe. »"
                ]
            },
            {
                "title": "2. Polite and Constructive Disagreement",
                "items": [
                    "« Je ne vois pas les choses sous cet angle ; permettez-moi de vous exposer mon point de vue. »",
                    "« Permettez-moi d'exprimer un doute quant à l'efficacité réelle de cette solution. »",
                    "« Ce n'est pas tout à fait exact ; les statistiques montrent une tendance bien différente. »",
                    "« Je crains de ne pas pouvoir vous suivre sur ce terrain-là car les risques sont trop grands. »"
                ]
            }
        ]
    }

    # Page 35: Expressing Doubts, Hopes & Feelings
    pages[35] = {
        "page": 35,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Expressing Doubts, Hopes & Feelings",
        "subtitle": "Sharing Complex Emotions and Subjective Reactions",
        "badge_num": "34",
        "intro": "Express hope, relief, disappointment, skepticism, and enthusiastic approval using intermediate grammar patterns.",
        "sections": [
            {
                "title": "1. Expressing Doubts and Skepticism",
                "items": [
                    "« Je suis plutôt sceptique quant aux résultats annoncés pour cette nouvelle politique. »",
                    "« Cela me paraît un peu trop beau pour être vrai, nous devrions rester prudents. »",
                    "« J'ai de sérieux doutes sur la faisabilité technique de ce projet dans les délais prévus. »",
                    "« Rien ne garantit que les consommateurs adhéreront spontanément à cette initiative. »"
                ]
            },
            {
                "title": "2. Expressing Hope, Relief and Disappointment",
                "items": [
                    "« J'ai bon espoir que les négociations aboutissent rapidement à un accord équitable. »",
                    "« Quel soulagement d'apprendre que le projet a été validé à l'unanimité ! »",
                    "« C'est une grande déception pour toute l'équipe qui s'était investie corps et âme. »",
                    "« Je trouve regrettable qu'aucune concertation n'ait eu lieu avec les principaux intéressés. »"
                ]
            }
        ]
    }

    # Page 36: Workplace Meetings & Short Presentations
    pages[36] = {
        "page": 36,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Workplace Meetings & Talks",
        "subtitle": "Presenting Project Updates and Collaborating with Coworkers",
        "badge_num": "35",
        "intro": "Deliver short professional presentations, participate in team meetings, and ask questions effectively.",
        "sections": [
            {
                "title": "1. Presenting a Project Update",
                "items": [
                    "Welcome attendees and state the objective: « Bonjour à tous, aujourd'hui je vais vous faire un point d'étape sur le projet X. »",
                    "Review completed milestones: « Ces dernières semaines, nous avons franchi plusieurs étapes clés avec succès. »",
                    "Highlight current challenges: « La principale difficulté réside actuellement dans le respect des délais de livraison. »",
                    "Propose actionable next steps: « Pour remédier à cela, je vous propose de réorganiser les priorités de l'équipe. »"
                ]
            },
            {
                "title": "2. Intervening in Professional Discussions",
                "items": [
                    "Ask for the floor politely: « Est-ce que je peux me permettre d'intervenir un instant sur ce point ? »",
                    "Support a colleague's proposal: « Je soutiens pleinement l'idée avancée par Sophie, qui me paraît très pragmatique. »",
                    "Ask for clarification on data: « Pourriez-vous nous préciser sur quelles données chiffrées repose cette estimation ? »",
                    "Summarize action items: « Si nous résumons nos décisions : Thomas s'occupe du budget et Sarah finalise la présentation. »"
                ]
            }
        ]
    }

    # Page 37: Speech Rhythm, Intonation & Sentence Stress
    pages[37] = {
        "page": 37,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Speech Rhythm & Intonation",
        "subtitle": "Mastering Rhythmic Groups, Melody, and Tonic Accents",
        "badge_num": "36",
        "intro": "Improve your accent and fluency by mastering the melodic rhythm and tonic stress of natural French speech.",
        "sections": [
            {
                "title": "1. The French Rhythmic Group (Groupe Souffle)",
                "items": [
                    "French places stress on the final syllable of the sense group, not on individual words.",
                    "Practice smooth phrasing: « Un petit garçon / est entré dans la boulangerie / pour acheter du pain. »",
                    "Avoid stressing English-style prefixes (say dé-ve-lop-PE-ment, not DE-velopment).",
                    "Elongate the final vowel of each thought group slightly to sound effortlessly natural."
                ]
            },
            {
                "title": "2. Expressive Intonation in Argumentation",
                "items": [
                    "Rising intonation marks continuation: voice goes up at commas and lists.",
                    "Falling intonation marks finality and conviction at the end of a conclusive statement.",
                    "Intonation for rhetorical questions: voice drops smoothly at the end of « N'est-ce pas évident ? »",
                    "Emphatic stress (accent d'insistance) placed on the first consonant to highlight strong emotion: « C'est FORM-idable ! »"
                ]
            }
        ]
    }

    # Page 38: Casual vs Formal Spoken French Registers
    pages[38] = {
        "page": 38,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Casual vs Formal Registers",
        "subtitle": "Navigating Between Colloquial (Familier) and Standard French",
        "badge_num": "37",
        "intro": "At B1, you know when to use standard French and when to recognize colloquial slang used by French friends.",
        "sections": [
            {
                "title": "1. Common Colloquial French Equivalents (Argot & Familier)",
                "items": [
                    "le travail → le boulot, le taf (« J'ai beaucoup de boulot cette semaine »).",
                    "l'argent → le fric, les sous (« Ça coûte un max de fric »).",
                    "la voiture → la bagnole (« J'ai garé ma bagnole dans la rue voisine »).",
                    "le livre → le bouquin (« C'est un super bouquin que je te conseille vivement »).",
                    "manger → bouffer (« On va bouffer un morceau ensemble ? »).",
                    "avoir peur → avoir la trouille (« J'ai eu la trouille de ma vie dans cet ascenseur »)."
                ]
            },
            {
                "title": "2. Register Awareness for Tests & Exams",
                "items": [
                    "In DELF B1 oral exams, strictly maintain the Standard register (registre courant).",
                    "Do NOT drop the negative 'ne' in formal exams (always say « Je ne pense pas », never « J'pense pas »).",
                    "Address the examiner exclusively as « vous » throughout the conversation.",
                    "Use appropriate polite closings: « Je vous remercie pour cet échange constructif. »"
                ]
            }
        ]
    }

    # Page 39: Transition Phrases & Conversational Connectors
    pages[39] = {
        "page": 39,
        "type": "checklist",
        "title": "B1 Speaking Mastery: Transition Phrases for Debates",
        "subtitle": "Essential Spoken Bridges to Guide Your Listeners",
        "badge_num": "38",
        "intro": "Keep your listeners engaged and guide them smoothly through your train of thought using these spoken bridges.",
        "sections": [
            {
                "title": "1. Introducing New Perspectives",
                "items": [
                    "« D'ailleurs, il ne faut pas oublier un élément déterminant dans cette affaire... »",
                    "« À cet égard, il est intéressant d'examiner ce qui se passe chez nos voisins européens. »",
                    "« Cela m'amène directement à évoquer mon second argument, à savoir... »",
                    "« Pour illustrer mon propos de manière très concrète, laissez-moi vous citer un fait récent. »"
                ]
            },
            {
                "title": "2. Refocusing and Wrapping Up",
                "items": [
                    "Refocusing after a tangent: « Mais revenons-en à l'essentiel de notre sujet... »",
                    "Summarizing prior points: « En somme, comme nous venons de le constater ensemble... »",
                    "Concluding clearly: « Pour conclure sur cette question, je dirais que la modération reste la clé. »",
                    "Inviting questions: « Je vous remercie pour votre attention et je suis prêt à répondre à vos questions. »"
                ]
            }
        ]
    }

    # Pages 40-49: Listening Comprehension
    # Page 40: Radio News & Press Reviews (RFI, France Info)
    pages[40] = {
        "page": 40,
        "type": "checklist",
        "title": "B1 Listening Mastery: Radio News & Press Reviews",
        "subtitle": "Understanding Authentic Broadcasts (RFI, France Info)",
        "badge_num": "39",
        "intro": "Listen to authentic French radio bulletins, understanding the main storylines, quotes, and background analyses.",
        "sections": [
            {
                "title": "1. Structure of a French Radio News Bulletin",
                "items": [
                    "Catch the opening headlines (les titres): three or four major breaking stories summarized in 30 seconds.",
                    "Identify the transition jingles and correspondent reports from cities worldwide.",
                    "Catch the numbers and statistics: millions of euros, percentages, and survey findings.",
                    "Differentiate between the journalist's summary and quotes from official speakers."
                ]
            },
            {
                "title": "2. Press Reviews (La Revue de Presse)",
                "items": [
                    "Understand how commentators compare front-page headlines from different daily papers.",
                    "Catch contrasting political stances between progressive and conservative editorials.",
                    "Identify journalistic wordplay, satirical headlines, and cultural references.",
                    "Filter through rapid speech to capture the core thesis of each commentator."
                ]
            }
        ]
    }

    # Page 41: Panel Discussions & Debates on Social Topics
    pages[41] = {
        "page": 41,
        "type": "checklist",
        "title": "B1 Listening Mastery: Panel Discussions & Debates",
        "subtitle": "Following Multi-Speaker Discussions with Diverse Viewpoints",
        "badge_num": "40",
        "intro": "Follow live roundtables where multiple guests talk over each other, express passionate views, and defend policies.",
        "sections": [
            {
                "title": "1. Tracking Multiple Interlocutors",
                "items": [
                    "Identify each guest's profession and role: sociologist, government minister, activist, or business leader.",
                    "Notice who is interrupting whom and how the moderator regains control of the debate.",
                    "Catch transition cues: « Si je peux me permettre d'ajouter un mot... », « Laissez-moi terminer ! »",
                    "Recognize when a guest changes their tone from diplomatic to heated or indignant."
                ]
            },
            {
                "title": "2. Identifying Points of Convergence and Disagreement",
                "items": [
                    "Detect common ground agreed upon by all parties before they debate the controversial specifics.",
                    "Identify the exact bone of contention: budget costs, timeline, ethics, or personal freedom.",
                    "Catch nuances of irony or skepticism in a speaker's laughter or rhetorical questions.",
                    "Summarize mentally what each speaker ultimately advocated for at the end of the exchange."
                ]
            }
        ]
    }

    # Page 42: Cultural Podcasts & Documentary Audio
    pages[42] = {
        "page": 42,
        "type": "checklist",
        "title": "B1 Listening Mastery: Cultural Podcasts & Documentaries",
        "subtitle": "Understanding Storytelling, Art, History & Science Audio",
        "badge_num": "41",
        "intro": "Listen to popular French cultural podcasts (France Culture, Arte Radio) with comfort and high comprehension.",
        "sections": [
            {
                "title": "1. Following Narrative Arc in Documentaries",
                "items": [
                    "Identify the historical or cultural mystery being investigated by the narrator.",
                    "Follow chronological flashbacks using plus-que-parfait and historical present tenses.",
                    "Understand ambient recordings, background music cues, and archival voice clips.",
                    "Extract the central message regarding human nature, societal evolution, or scientific breakthroughs."
                ]
            },
            {
                "title": "2. In-Depth Cultural Interviews",
                "items": [
                    "Follow conversations with novelists, film directors, and philosophers discussing their creative process.",
                    "Understand abstract questions about artistic motivation, inspiration, and society critique.",
                    "Catch figurative language, book excerpts read aloud, and personal reflections on career milestones.",
                    "Note down recommended titles, historical dates, and key philosophical ideas for further study."
                ]
            }
        ]
    }

    # Page 43: Public Speeches, Conferences & Presentations
    pages[43] = {
        "page": 43,
        "type": "checklist",
        "title": "B1 Listening Mastery: Public Speeches & Talks",
        "subtitle": "Understanding Formal Presentations, Keynotes & TED-Style Talks",
        "badge_num": "42",
        "intro": "Understand formal keynote addresses, conference presentations, and academic lectures delivered in French.",
        "sections": [
            {
                "title": "1. Decoding Formal Rhetorical Structures",
                "items": [
                    "Recognize formal introductory courtesies: « C'est un honneur tout particulier d'être parmi vous aujourd'hui... »",
                    "Follow structural milestones: « Mon intervention s'articulera autour de trois axes principaux. »",
                    "Spot rhetorical repetitions used to emphasize key points: « Nous devons agir, nous devons innover... »",
                    "Identify the speaker's overarching thesis and call to collective action in the final peroration."
                ]
            },
            {
                "title": "2. Handling Dense Technical Information",
                "items": [
                    "Filter out specialized jargon to focus on the logical cause-and-effect conclusions.",
                    "Understand verbal explanations of charts and graphs: « Comme vous pouvez le constater sur ce graphique... »",
                    "Catch qualifying remarks: « Notons cependant que ces résultats doivent être interprétés avec précaution. »",
                    "Formulate relevant follow-up questions based on the presenter's conclusions."
                ]
            }
        ]
    }

    # Page 44: Professional Meetings & Collaborative Discussions
    pages[44] = {
        "page": 44,
        "type": "checklist",
        "title": "B1 Listening Mastery: Workplace Meetings & Briefings",
        "subtitle": "Following Agendas, Budget Reviews & Project Deadlines",
        "badge_num": "43",
        "intro": "Feel comfortable in professional meeting rooms: follow team briefings, understand budget decisions, and take notes.",
        "sections": [
            {
                "title": "1. Meeting Agendas and Management Briefs",
                "items": [
                    "Understand the meeting agenda: « À l'ordre du jour ce matin : la validation du budget annuel et le planning. »",
                    "Catch specific deadline updates: « Le livrable final doit être impérativement transmis avant le 15 décembre. »",
                    "Identify task assignments: « Qui souhaite se charger de coordonner les relations avec les fournisseurs ? »",
                    "Understand performance reviews and KPIs presented by department heads."
                ]
            },
            {
                "title": "2. Subtle Workplace Dynamics & Negotiations",
                "items": [
                    "Recognize when a colleague is expressing polite pushback against an unreasonable request.",
                    "Identify underlying compromises reached between marketing, finance, and technical teams.",
                    "Detect workplace humor and informal camaraderie used to ease meeting tensions.",
                    "Confirm action items before leaving: « Nous validons donc cette proposition à condition que le budget reste identique. »"
                ]
            }
        ]
    }

    # Page 45: Varied Francophone Accents (Quebec, Switzerland, Africa)
    pages[45] = {
        "page": 45,
        "type": "checklist",
        "title": "B1 Listening Mastery: Varied Francophone Accents",
        "subtitle": "Understanding French from Quebec, Switzerland, Belgium & West Africa",
        "badge_num": "44",
        "intro": "French is a global language. Train your ear to understand regional accents and vocabulary variations across the world.",
        "sections": [
            {
                "title": "1. European Variations (Belgium & Switzerland)",
                "items": [
                    "Numbers in Switzerland and Belgium: septante (70), octante / huitante (80), nonante (90).",
                    "Meal names: le déjeuner (breakfast), le dîner (lunch), le souper (dinner).",
                    "Belgian expressions: « savoir » used for « pouvoir » (« Tu sais me passer le sel ? »), « une fois ».",
                    "Vowel openness differences: recognizing distinct regional intonation and vowel length."
                ]
            },
            {
                "title": "2. North American & African Francophonie",
                "items": [
                    "Quebec French (Québécois): characteristic dipthongs, vocabulary like « le char » (car), « le chum » (boyfriend).",
                    "Quebec question particle '-tu': « Tu viens-tu ce soir ? » instead of « Est-ce que tu viens ? »",
                    "African French (Senegal, Ivory Coast, Cameroon): rolled 'r', rhythmic syllable timing, formal polite greetings.",
                    "African French idioms: expressions of respect, community solidarity, and proverbs woven into conversation."
                ]
            }
        ]
    }

    # Page 46: Catching Nuances, Irony & Implied Attitudes
    pages[46] = {
        "page": 46,
        "type": "checklist",
        "title": "B1 Listening Mastery: Tone, Irony & Implied Meaning",
        "subtitle": "Hearing Between the Lines: Sarcasm, Understatement & Humor",
        "badge_num": "45",
        "intro": "French speakers frequently use understatement (litote) and gentle irony. Learn to detect when 'c'est pas mal' means 'it's amazing'.",
        "sections": [
            {
                "title": "1. French Understatement (La Litote)",
                "items": [
                    "« C'est pas mal » usually means it is actually very good or impressive.",
                    "« C'est pas terrible » means it is quite bad or disappointing.",
                    "« Il n'est pas idiot » means he is exceptionally clever.",
                    "« Ce n'est pas donné » means it is quite expensive."
                ]
            },
            {
                "title": "2. Detecting Sarcasm and Irony",
                "items": [
                    "Recognize ironic praise: « Bravo, c'est du beau travail ! » said in a deadpan tone when someone drops a plate.",
                    "Catch sarcastic rhetorical questions: « Et la marmotte, elle met le chocolat dans le papier d'alu ? » (You really expect me to believe that?)",
                    "Identify self-deprecating humor used to downplay achievements in professional settings.",
                    "Differentiate between serious criticism and teasing among friends."
                ]
            }
        ]
    }

    # Page 47: Distinguishing Facts from Personal Opinions
    pages[47] = {
        "page": 47,
        "type": "checklist",
        "title": "B1 Listening Mastery: Facts vs Opinions",
        "subtitle": "Critical Listening: Objective Statements vs Subjective Claims",
        "badge_num": "46",
        "intro": "DELF B1 listening tasks require you to distinguish verified facts from the personal beliefs of interviewed speakers.",
        "sections": [
            {
                "title": "1. Clues that Signal Objective Facts",
                "items": [
                    "Use of passive voice or impersonal structures: « Il a été démontré que... », « Les statistiques indiquent... »",
                    "Specific data: official dates, legal articles, verified test results, and census figures.",
                    "Attributive citations: « Selon le rapport officiel publié hier par le ministère... »",
                    "Neutral journalistic tone without emotional adjectives or voice modulation."
                ]
            },
            {
                "title": "2. Clues that Signal Subjective Opinions",
                "items": [
                    "Verbs of feeling and belief: « J'ai le sentiment que... », « Il me semble que... », « À mes yeux... »",
                    "Evaluative adjectives: inadmissible, remarquable, choquant, scandaleux, merveilleux.",
                    "Use of the conditionnel to express possibilities rather than confirmed certainties.",
                    "Emotional markers and rhetorical exclamations: « C'est tout de même incroyable que personne n'ait réagi ! »"
                ]
            }
        ]
    }

    # Page 48: Following Fast Discussions with Interruptions
    pages[48] = {
        "page": 48,
        "type": "checklist",
        "title": "B1 Listening Mastery: Following Fast Discussions",
        "subtitle": "Handling Overlapping Speech, Fillers & Sudden Topic Shifts",
        "badge_num": "47",
        "intro": "Native French speakers converse rapidly and interrupt with passion. Learn how to stay anchored during lively discussions.",
        "sections": [
            {
                "title": "1. Recognizing Conversational Interruption Tactics",
                "items": [
                    "Polite interruptions: « Si vous me permettez de rebondir sur vos propos... »",
                    "Firm interjections: « Attendez, attendez ! Vous ne pouvez pas laisser dire cela ! »",
                    "Yielding the floor: « Allez-y, je vous en prie, terminez votre démonstration. »",
                    "Reclaiming the floor: « Laissez-moi au moins aller jusqu'au bout de ma phrase ! »"
                ]
            },
            {
                "title": "2. Filtering Fillers and Mental Anchoring",
                "items": [
                    "Filter out rapid conversational fillers: « genre », « enfin bref », « du coup », « en quelque sorte ».",
                    "Anchor on the main verb when two people speak simultaneously: identify the grammatical agreement.",
                    "Follow body language and eye contact cues when watching televised debates or videos.",
                    "Synthesize the conclusion of the dispute: did the speakers agree to disagree or find common ground?"
                ]
            }
        ]
    }

    # Page 49: Note-Taking from Spoken Audio
    pages[49] = {
        "page": 49,
        "type": "checklist",
        "title": "B1 Listening Mastery: Note-Taking Strategies",
        "subtitle": "Capturing Key Facts, Names & Dates While Listening",
        "badge_num": "48",
        "intro": "In DELF B1, you hear each recording twice. Master note-taking techniques to record essential answers on the first listen.",
        "sections": [
            {
                "title": "1. First Listen: The Big Picture (Le Premier Écoute)",
                "items": [
                    "Read the questionnaire carefully before the audio begins to anticipate vocabulary and questions.",
                    "During the first listen, write down only key nouns, numbers, and main verbs.",
                    "Identify the global topic: Who is talking? What is the main issue? What is the overall conclusion?",
                    "Use abbreviations and symbols: + (plus), - (moins), → (entraîne/provoque), tx (taux), bcp (beaucoup)."
                ]
            },
            {
                "title": "2. Second Listen: Targeted Details (La Seconde Écoute)",
                "items": [
                    "Focus specifically on unanswered questions from the test sheet.",
                    "Double-check numbers, prices, percentages, dates, and proper names of places.",
                    "Verify the speaker's nuance: did they say 'never', 'rarely', 'sometimes', or 'always'?",
                    "Complete full sentence answers in clear, legible French during the final 3-minute review pause."
                ]
            }
        ]
    }

    # Pages 50-59: Reading Comprehension
    # Page 50: Press Editorials & Opinion Columns
    pages[50] = {
        "page": 50,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Press Editorials",
        "subtitle": "Analyzing Opinion Columns in Le Monde, Courrier International & Libération",
        "badge_num": "49",
        "intro": "Read editorial articles from leading French publications, identifying the author's stance and arguments.",
        "sections": [
            {
                "title": "1. Anatomy of a French Newspaper Editorial",
                "items": [
                    "The Lede (Le Chapeau): a bold 2-3 sentence teaser summarizing the main controversy.",
                    "The hook: referencing a recent legislative vote, global summit, or social trend.",
                    "The author's thesis: identifying where the editorialist takes a clear stand on the issue.",
                    "Logical transitions: tracing paragraphs connected by « En revanche », « Certes », « Par conséquent »."
                ]
            },
            {
                "title": "2. Analyzing Tone and Rhetorical Devices",
                "items": [
                    "Recognizing polemical tone: words designed to provoke debate and civic reaction.",
                    "Spotting rhetorical questions used to guide the reader toward the author's preferred conclusion.",
                    "Differentiating reported quotes from the editorialist's own interpretations.",
                    "Summarizing the final call to action or warning presented in the closing paragraph."
                ]
            }
        ]
    }

    # Page 51: Cultural Reviews of Books & Films
    pages[51] = {
        "page": 51,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Cultural Reviews",
        "subtitle": "Critiques of Novels, Cinema Releases & Art Exhibitions",
        "badge_num": "50",
        "intro": "Read cultural critiques in magazines like Télérama and Les Inrockuptibles, understanding aesthetic judgments.",
        "sections": [
            {
                "title": "1. Film & Theater Reviews",
                "items": [
                    "The synopsis (Le pitch): brief summary of plot, setting, and main character conflicts.",
                    "Critique of acting and directing: « Une interprétation magistrale portée par un casting d'exception. »",
                    "Critique of pacing: « Malgré quelques longueurs dans la seconde partie, le dénouement reste bouleversant. »",
                    "Star ratings and final recommendations: knowing whether the critic advises viewers to go or skip."
                ]
            },
            {
                "title": "2. Literary Reviews & Book Award Coverage",
                "items": [
                    "Coverage of prestigious French literary prizes: Prix Goncourt, Prix Renaudot, Prix Fémina.",
                    "Appraisal of writing style: « Une écriture incisive, poétique et empreinte d'une grande sensibilité. »",
                    "Analysis of social themes explored in contemporary fiction: identity, family, exile, modern alienation.",
                    "Extracting favorite quotes selected by the critic to showcase the author's voice."
                ]
            }
        ]
    }

    # Page 52: Charters, Regulations & Workplace Policies
    pages[52] = {
        "page": 52,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Charters & Policies",
        "subtitle": "Decoding Internal Rules, Safety Regulations & Co-Ownership Charters",
        "badge_num": "51",
        "intro": "Understand legalistic and administrative texts: building co-ownership rules, company charters, and safety policies.",
        "sections": [
            {
                "title": "1. Deciphering Regulatory Language",
                "items": [
                    "Mandatory obligations: « Tout occupant est tenu de veiller à la tranquillité de l'immeuble. »",
                    "Prohibitions and fines: « Il est strictement interdit d'encombrer les parties communes sous peine d'amende. »",
                    "Permitted actions with prior notice: « Les travaux bruyants ne sont autorisés qu'entre 9h et 18h en semaine. »",
                    "Safety and emergency evacuation protocols: identifying assembly points and fire extinguisher instructions."
                ]
            },
            {
                "title": "2. Company Charters & IT Guidelines",
                "items": [
                    "Charter of professional ethics: rules regarding conflicts of interest, equality, and anti-harassment.",
                    "IT acceptable use policy: guidelines for company laptops, remote work access, and data security.",
                    "Procedure for reporting grievances: understanding who to contact (délégués du personnel, direction RH).",
                    "Understanding legal clauses regarding intellectual property created during employment."
                ]
            }
        ]
    }

    # Page 53: Sociological Surveys & Infographics
    pages[53] = {
        "page": 53,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Surveys & Infographics",
        "subtitle": "Interpreting Statistical Charts, Demographics & Public Polls",
        "badge_num": "52",
        "intro": "Read sociological reports, INSEE demographic charts, and opinion survey infographics with accurate comprehension.",
        "sections": [
            {
                "title": "1. Reading Statistical Figures and Percentages",
                "items": [
                    "Proportions: « Plus d'un tiers des sondés (36 %) estiment que le pouvoir d'achat a diminué. »",
                    "Majorities: « Une écrasante majorité (78 %) se déclare favorable au renforcement des pistes cyclables. »",
                    "Trends and evolutions: « Ce chiffre est en constante progression depuis le début de la décennie. »",
                    "Stagnation and declines: « Le taux de chômage a enregistré une baisse sensible de deux points cette année. »"
                ]
            },
            {
                "title": "2. Analyzing Infographics & Survey Methodology",
                "items": [
                    "Methodology box: understanding sample size (« Échantillon représentatif de 1 005 personnes âgées de 18 ans et plus »).",
                    "Margin of error and survey dates: identifying when the poll was taken to evaluate relevance.",
                    "Comparing demographic breakdowns: contrasting responses by age group, profession, and region.",
                    "Synthesizing the overarching sociological conclusion of the graphic."
                ]
            }
        ]
    }

    # Page 54: Contemporary Literature & Short Stories
    pages[54] = {
        "page": 54,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Contemporary Literature",
        "subtitle": "Appreciating Modern Francophone Novels, Dialogue & Narrative Tension",
        "badge_num": "53",
        "intro": "Read excerpts from modern French authors (Annie Ernaux, Amélie Nothomb, Tahar Ben Jelloun) with enjoyment.",
        "sections": [
            {
                "title": "1. Following Literary Descriptions & Atmosphere",
                "items": [
                    "Atmospheric scene-setting combining rich sensory adjectives and figurative comparisons.",
                    "Internal monologues: following a character's unspoken fears, jealousies, and ambitions.",
                    "Understanding character relationships through subtext in authentic dialogue exchanges.",
                    "Recognizing past tenses in narrative literature (passé simple recognition, imparfait, plus-que-parfait)."
                ]
            },
            {
                "title": "2. Literary Devices & Stylistic Choices",
                "items": [
                    "Metaphors and similes: understanding figurative expressions used to portray emotion.",
                    "Foreshadowing: picking up subtle textual clues that hint at an impending plot twist.",
                    "Social commentary embedded in fictional storytelling: reflecting on real-world inequality or historical trauma.",
                    "Formulating personal interpretations of open or ambiguous endings."
                ]
            }
        ]
    }

    # Page 55: Formal Correspondence: Inquiries & Complaints
    pages[55] = {
        "page": 55,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Formal Correspondence",
        "subtitle": "Analyzing Administrative Letters, Claim Notices & Legal Demands",
        "badge_num": "54",
        "intro": "Read formal letters from government ministries, legal attorneys, insurance adjusters, and service providers.",
        "sections": [
            {
                "title": "1. Standard Administrative Letter Architecture",
                "items": [
                    "Sender and recipient block: identifying official registration numbers, dates, and postal codes.",
                    "The subject line (Objet): immediate clarification of the letter's legal purpose (« Objet : Mise en demeure »).",
                    "Reference numbers: Vos références / Nos références for tracking case files.",
                    "The formal opening and closing salutations: « Madame la Directrice, », « Veuillez agréer mes salutations distinguées. »"
                ]
            },
            {
                "title": "2. Identifying Legal Deadlines & Required Actions",
                "items": [
                    "Explicit deadlines for reply: « À défaut de réponse sous quinzaine, nous transmettrons le dossier au contentieux. »",
                    "Required supporting documents: identifying which certificates, IDs, or receipts must be enclosed.",
                    "Financial demands and penalty fees: understanding exact sums owed and breakdown of late interest charges.",
                    "Appeal procedures: understanding where and how to file a formal appeal or counter-claim."
                ]
            }
        ]
    }

    # Page 56: Science & Environmental Articles
    pages[56] = {
        "page": 56,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Science & Environment",
        "subtitle": "Understanding Popular Science, Eco-Innovations & Health Studies",
        "badge_num": "55",
        "intro": "Read accessible science journalism (Science & Vie, Geo, National Geographic France) on nature and technology.",
        "sections": [
            {
                "title": "1. Scientific Discoveries and Innovations",
                "items": [
                    "The research objective: identifying the hypothesis formulated by international researchers.",
                    "Methodology: laboratory experiments, clinical trials, satellite observation, or archaeological digs.",
                    "Major findings: understanding breakthroughs in clean energy, marine biology, or medicine.",
                    "Practical applications: how this scientific breakthrough could change daily life in the next decade."
                ]
            },
            {
                "title": "2. Environmental Warnings and Solutions",
                "items": [
                    "Impact of human activity on ecosystems: deforestation, ocean acidification, plastic pollution.",
                    "Proposed eco-solutions: rewilding projects, carbon capture, circular packaging, and agroecology.",
                    "Quotes from climatologists and field biologists calling for legislative action.",
                    "Balancing economic growth against environmental preservation in editorial debates."
                ]
            }
        ]
    }

    # Page 57: Biographies of Cultural & Historical Figures
    pages[57] = {
        "page": 57,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Historical Biographies",
        "subtitle": "Tracing the Lives of Influential Francophone Figures",
        "badge_num": "56",
        "intro": "Read biographical profiles of major historical and cultural figures (Marie Curie, Jean Moulin, Simone Veil, Aimé Césaire).",
        "sections": [
            {
                "title": "1. Tracing Milestones and Turning Points",
                "items": [
                    "Origins and early education: identifying early obstacles overcome by the figure.",
                    "Decisive turning point: the historical crisis or discovery that launched their fame.",
                    "Major achievements: laws passed, scientific patents filed, literary masterpieces published.",
                    "Enduring legacy: how their actions continue to shape contemporary France and the world."
                ]
            },
            {
                "title": "2. Chronological Linking Words in Biographies",
                "items": [
                    "Chronological anchoring: « Dès son plus jeune âge », « C'est en 1944 que... », « Quelques années plus tard... »",
                    "Adversity markers: « Malgré l'hostilité de ses pairs », « En dépit de nombreuses arrestations... »",
                    "Consequence markers: « Cet engagement sans faille lui valut l'admiration de la nation tout entière. »",
                    "Posthumous honors: entry into the Panthéon, naming of avenues, universities, and commemorative coins."
                ]
            }
        ]
    }

    # Page 58: Decoding Metaphors & Idioms in Press
    pages[58] = {
        "page": 58,
        "type": "checklist",
        "title": "B1 Reading Comprehension: Idioms & Metaphors in Press",
        "subtitle": "Understanding Journalistic Idioms, Figures of Speech & Catchy Titles",
        "badge_num": "57",
        "intro": "French journalists love figurative expressions. Learn to decode common press idioms and catchy headlines.",
        "sections": [
            {
                "title": "1. Common Journalistic Idioms",
                "items": [
                    "« Jeter de l'huile sur le feu » (to add fuel to the fire / inflame tensions).",
                    "« Tirer la sonnette d'alarme » (to sound the alarm / warn of imminent danger).",
                    "« Jeter l'éponge » (to throw in the towel / give up a contest or election).",
                    "« Mettre les pieds dans le plat » (to bluntly bring up an awkward truth).",
                    "« Tourner la page » (to turn over a new leaf / move on from a scandal or crisis).",
                    "« Trouver un terrain d'entente » (to find common ground / reach a compromise)."
                ]
            },
            {
                "title": "2. Wordplay and Double Meanings in Headlines",
                "items": [
                    "Recognize puns on famous proverbs: modifying a proverb to comment on current politics.",
                    "Alliteration and rhyming in newspaper headlines: designed to catch the reader's eye at newsstands.",
                    "Using meteorological metaphors for economic crises: « avis de tempête sur les marchés financiers ».",
                    "Understanding military metaphors used in sports reporting: « une victoire éclatante sur le terrain »."
                ]
            }
        ]
    }

    # Page 59: Reading Strategies: Reading for Gist & Detail
    pages[59] = {
        "page": 59,
        "type": "checklist",
        "title": "B1 Reading Strategies: Gist, Detail & Inference",
        "subtitle": "Effective Reading Techniques for DELF B1 and Long Articles",
        "badge_num": "58",
        "intro": "Master intermediate reading techniques to answer exam questions accurately within the 35-minute time limit.",
        "sections": [
            {
                "title": "1. Two-Pass Reading Technique for Exams",
                "items": [
                    "Pass 1 (Global Gist): skim title, subheadings, and first/last sentences of each paragraph in 2 minutes.",
                    "Analyze exam questions: underline keywords in the questions before beginning the deep read.",
                    "Pass 2 (Detailed Search): locate the specific paragraph where each answer is anchored.",
                    "Verify exact quote vs personal rephrasing: ensure your written justification matches the text."
                ]
            },
            {
                "title": "2. Inferring Implicit Meaning (Lire Entre les Lignes)",
                "items": [
                    "Distinguish between what is explicitly stated versus what the author clearly implies.",
                    "Notice the author's choice of adjectives: are they enthusiastic, neutral, or quietly skeptical?",
                    "Identify punctuation cues: quotation marks (guillemets) indicating irony or distancing (« une prétendue solution »).",
                    "Eliminate distractor options: watch out for choices that contain words from the text but state the opposite."
                ]
            }
        ]
    }

    # Pages 60-67: Written Production & Interaction
    # Page 60: Structuring an Opinion Essay (Essai Argumentatif)
    pages[60] = {
        "page": 60,
        "type": "checklist",
        "title": "B1 Writing Mastery: The Argumentative Essay",
        "subtitle": "Writing a Cohesive 160–180 Word Essay (Essai Argumentatif)",
        "badge_num": "59",
        "intro": "In DELF B1, you must write a structured 160 to 180-word essay expressing your opinion on a societal issue.",
        "sections": [
            {
                "title": "1. The 3-Part Essay Structure",
                "items": [
                    "Introduction (30–40 words): introduce the topic with a hook, define the debate, and state your thesis clearly.",
                    "Body Paragraph 1 (50–60 words): first major argument supported by a real-world example and connectors.",
                    "Body Paragraph 2 (50–60 words): second major argument addressing counterarguments or offering solutions.",
                    "Conclusion (30–40 words): summarize your stance and end with a thought-provoking final outlook."
                ]
            },
            {
                "title": "2. Word Count & Polish Checklist",
                "items": [
                    "Target word count: strictly between 160 and 180 words (a 10% margin is permitted: 144 to 198 words).",
                    "Paragraph formatting: leave a blank line between introduction, body paragraphs, and conclusion.",
                    "Use at least 4 varied logical connectors: d'une part, d'autre part, en revanche, par conséquent.",
                    "Include at least one complex grammar structure: subjonctif, conditionnel, or mise en relief."
                ]
            }
        ]
    }

    # Page 61: Formal Complaint Letters (Lettre de Réclamation)
    pages[61] = {
        "page": 61,
        "type": "checklist",
        "title": "B1 Writing Mastery: Formal Complaint Letters",
        "subtitle": "Writing Effective Claims to Landlords, Airlines & Merchants",
        "badge_num": "60",
        "intro": "Draft assertive, polite formal complaint letters demanding refunds, repairs, or compensations.",
        "sections": [
            {
                "title": "1. Opening & Stating the Facts",
                "items": [
                    "Formal header: your name and address (top left), recipient details (top right), date and city.",
                    "Clear subject line: « Objet : Réclamation – Annulation du vol AF456 du 12 juillet et demande d'indemnisation. »",
                    "State the facts objectively: dates, booking numbers, invoice numbers, and contractual commitments.",
                    "Describe the prejudice suffered: « Cet incident m'a contraint à réserver une chambre d'hôtel à mes frais. »"
                ]
            },
            {
                "title": "2. Formulating Demand & Polite Legal Closing",
                "items": [
                    "State your explicit expectation: « Par conséquent, je vous saurais gré de bien vouloir procéder au remboursement. »",
                    "Attach copies of supporting documents: « Vous trouverez ci-joint la copie de mes billets et des factures acquittées. »",
                    "Set a reasonable timeframe: « J'espère obtenir un retour favorable de votre part sous un délai de quinze jours. »",
                    "Formal closing formula: « Dans cette attente, je vous prie d'agréer, Madame, Monsieur, l'expression de mes salutations distinguées. »"
                ]
            }
        ]
    }

    # Page 62: Cover Letters & Applications (Lettre de Motivation)
    pages[62] = {
        "page": 62,
        "type": "checklist",
        "title": "B1 Writing Mastery: Cover Letters & Applications",
        "subtitle": "Writing a Persuasive Lettre de Motivation for Jobs & Internships",
        "badge_num": "61",
        "intro": "Learn the traditional French 3-part cover letter structure (Vous / Moi / Nous) to apply for jobs and internships.",
        "sections": [
            {
                "title": "1. The Vous / Moi / Nous Methodology",
                "items": [
                    "Part 1 (Vous): show knowledge of the company and praise their mission or reputation in the sector.",
                    "Part 2 (Moi): present your studies, language skills, and relevant past experiences that fit the job profile.",
                    "Part 3 (Nous): explain what you and the company can achieve together through collaboration.",
                    "Use active, dynamic verbs: coordonner, développer, concevoir, optimiser, animer, analyser."
                ]
            },
            {
                "title": "2. Requesting an Interview & Formal Sign-Off",
                "items": [
                    "Express eagerness for an interview: « Je reste à votre entière disposition pour convenir d'un entretien. »",
                    "Mention attached CV: « Je me permets de joindre à ce courrier mon curriculum vitæ détaillé. »",
                    "Polite formal closing: « Je vous prie d'agréer, Madame, Monsieur, l'assurance de ma parfaite considération. »",
                    "Check handwriting or clean digital layout with standard French margins and line spacing."
                ]
            }
        ]
    }

    # Page 63: Writing an Opinion Article or Forum Post
    pages[63] = {
        "page": 63,
        "type": "checklist",
        "title": "B1 Writing Mastery: Online Articles & Forum Posts",
        "subtitle": "Writing Engaging Blog Posts, Reader Contributions & Social Commentary",
        "badge_num": "62",
        "intro": "Write engaging contributions for online citizen forums, lifestyle blogs, and reader response pages.",
        "sections": [
            {
                "title": "1. Catchy Titles and Engaging Hooks",
                "items": [
                    "Craft an intriguing headline: « Vivre sans smartphone : utopie ou nécessité pour notre bien-être ? »",
                    "Engage the online community: « Chers internautes, qui parmi vous n'a jamais ressenti le besoin de déconnecter ? »",
                    "Share personal anecdotes to ground your opinion in real-life authenticity.",
                    "Keep sentences punchy and dynamic, using rhetorical questions and exclamations."
                ]
            },
            {
                "title": "2. Moderating and Inviting Comments",
                "items": [
                    "Address different perspectives fairly: « Je conçois tout à fait que certains trouvent cela impossible au travail. »",
                    "Offer practical tips: « Pour ma part, voici trois astuces simples qui ont transformé mon quotidien. »",
                    "Invite community debate: « Et vous, quelle est votre expérience sur ce sujet ? Laissez vos réflexions en commentaire ! »",
                    "Sign off with an engaging pseudonym or warm sign-off: « Au plaisir d'échanger avec vous tous ! »"
                ]
            }
        ]
    }

    # Page 64: Writing Concise Text Summaries (Le Compte Rendu)
    pages[64] = {
        "page": 64,
        "type": "checklist",
        "title": "B1 Writing Mastery: Text Summaries & Briefings",
        "subtitle": "Synthesizing Key Information from Long Articles without Plagiarism",
        "badge_num": "63",
        "intro": "Summarize 500-word articles into a 100-word executive briefing, rephrasing ideas in your own words.",
        "sections": [
            {
                "title": "1. Extracting Core Information",
                "items": [
                    "Identify the central thesis and strip away secondary details, illustrative examples, and repetition.",
                    "Highlight the author's primary arguments and their corresponding conclusions.",
                    "Rephrase concepts using synonyms: never copy contiguous sentences verbatim from the original text.",
                    "Maintain strict objectivity: do NOT introduce your personal opinion into a summary briefing."
                ]
            },
            {
                "title": "2. Cohesive Synthesis Architecture",
                "items": [
                    "Introduce the source: « Dans cet article paru dans Le Figaro, l'auteur s'interroge sur l'impact de... »",
                    "Synthesize main points using attributive verbs: « L'auteur souligne que... », « Il démontre ensuite que... »",
                    "Use neutral logical transitions: « De surcroît », « Enfin », « Parallèlement ».",
                    "Verify that the summary represents exactly 20–25% of the original text length."
                ]
            }
        ]
    }

    # Page 65: Complex Connectors & Paragraph Flow
    pages[65] = {
        "page": 65,
        "type": "checklist",
        "title": "B1 Writing Mechanics: Complex Logical Connectors",
        "subtitle": "Structuring Advanced Paragraphs (En effet, Par conséquent, Bien que)",
        "badge_num": "64",
        "intro": "Elevate your writing style from basic French to intermediate elegance with logical connectors.",
        "sections": [
            {
                "title": "1. Explanation, Addition & Contrast Connectors",
                "items": [
                    "En effet (indeed / in fact - explains why): « Le projet a pris du retard. En effet, plusieurs pièces manquaient. »",
                    "De plus / Par ailleurs (furthermore / in addition): « Par ailleurs, les coûts de transport ont augmenté. »",
                    "Néanmoins / En revanche (nevertheless / on the other hand): « L'offre est séduisante ; néanmoins, elle comporte des risques. »",
                    "D'autant plus que (all the more so since): « C'est une opportunité rare, d'autant plus que le poste est en télétravail. »"
                ]
            },
            {
                "title": "2. Consequence, Purpose & Conclusion Connectors",
                "items": [
                    "Par conséquent / C'est ainsi que (consequently / this is how): « Par conséquent, nous devons revoir notre stratégie. »",
                    "Afin de / De façon à (+ Infinitif): « Il convient d'agir vite de façon à éviter tout malentendu. »",
                    "En définitive / Somme toute (all in all / ultimately): « En définitive, cette réforme s'avère bénéfique. »",
                    "Punctuation rule: always place a comma after sentence-initial connectors (En effet, / Par ailleurs, / Cependant,)."
                ]
            }
        ]
    }

    # Page 66: Register Mastery: Informal vs Standard vs Formal
    pages[66] = {
        "page": 66,
        "type": "checklist",
        "title": "B1 Writing Mechanics: Register Mastery",
        "subtitle": "Adapting Vocabulary, Syntax & Salutations to Your Audience",
        "badge_num": "65",
        "intro": "Master the three French language registers: familiar with friends, standard for articles, and formal for administration.",
        "sections": [
            {
                "title": "1. Comparing the Three Registers",
                "items": [
                    "Informal (Familier): « Salut ! T'as vu le truc hier ? C'était trop cool ! » (friends and close family).",
                    "Standard (Courant): « Bonjour, as-tu regardé l'émission hier ? Elle était très intéressante. » (work, school, media).",
                    "Formal (Soutenu): « Madame, auriez-vous l'amabilité de me transmettre le document mentionné hier ? » (administration).",
                    "Avoid mixing registers within the same letter or essay."
                ]
            },
            {
                "title": "2. Salutation & Closing Formulas Across Registers",
                "items": [
                    "Informal: « Salut Marc », « Bises », « Grosses bises », « À la prochaine ! »",
                    "Standard / Professional: « Bonjour Monsieur Martin », « Bien cordialement », « Cordialement », « Meilleures salutations ».",
                    "Formal / Administrative: « Veuillez agréer, Monsieur le Juge, l'expression de mes salutations très respectueuses. »",
                    "Never use « Chère Madame » in formal administrative letters unless you know the recipient personally."
                ]
            }
        ]
    }

    # Page 67: Writing Mechanics: Advanced Self-Editing
    pages[67] = {
        "page": 67,
        "type": "checklist",
        "title": "B1 Writing Mechanics: Advanced Self-Editing",
        "subtitle": "Catching Subjunctive Errors, Participle Agreements & False Friends",
        "badge_num": "66",
        "intro": "Develop an expert self-editing checklist to eliminate grammatical slips before turning in written work.",
        "sections": [
            {
                "title": "1. Advanced Grammar Self-Audit Checklist",
                "items": [
                    "Subjunctive verification: Did you use the subjunctive after 'il faut que', 'bien que', 'pour que', and negative opinion verbs?",
                    "Past participle agreement with avoir: Did you agree the participle when a direct object precedes the verb? (« La lettre que j'ai écrite »).",
                    "Reflexive verb agreements: Does the participle agree with the reflexive pronoun? (« Elle s'est lavée » vs « Elle s'est lavé les mains »).",
                    "Tense harmony in narration: Are you consistent between passé composé, imparfait, and plus-que-parfait?"
                ]
            },
            {
                "title": "2. Spelling, Accents & False Friends",
                "items": [
                    "Homophones: check c'est / s'est / ses / ces / sais / sait carefully in context.",
                    "Accents: ensure difference between tâche (task) and tache (stain), sûr (sure) and sur (on).",
                    "Watch out for false friends: opportunité (favorable timing, not simple chance), assister à (to attend, not to assist).",
                    "Capitalization: months, days, and language names do NOT take capital letters in French (français, lundi, mai)."
                ]
            }
        ]
    }

    # Pages 68-71: Assessment & B2 Readiness
    # Page 68: Final Self-Evaluation: Speaking Readiness & Debating Skills
    pages[68] = {
        "page": 68,
        "type": "audit",
        "title": "Final Self-Evaluation: Speaking Readiness & Debating Skills",
        "subtitle": "Spoken Production & Interactive Argumentation Audit",
        "badge_num": "67",
        "intro": "Comprehensive diagnostic checklist to evaluate whether your spoken French meets the CEFR B1 threshold.",
        "items": [
            "I can deliver an uninterrupted 3-minute presentation expressing my viewpoint on a societal issue.",
            "I can defend my arguments in a debate, responding to objections and conceding points diplomatically.",
            "I can handle unexpected transactional disputes with landlords, airlines, and service providers in French.",
            "I can participate actively in workplace team meetings, suggesting ideas and summarizing action items.",
            "I can express complex feelings, skepticism, hope, and relief with nuanced vocabulary.",
            "I naturally adjust my intonation and speech rhythm to sound convincing and fluent.",
            "I distinguish between colloquial slang with friends and standard formal register in professional settings.",
            "I use transitional debate bridges smoothly to connect ideas and guide my listeners."
        ],
        "sections": [
            {
                "title": "1. Spoken Production Audit (Monologue Suivi)",
                "items": [
                    "Continuous argument flow: Can you present a structured monologue with an introduction, two arguments, and a conclusion?",
                    "Supporting evidence: Can you illustrate every main point with a concrete real-life example or personal anecdote?",
                    "Grammar versatility: Do you comfortably integrate subjonctif, conditionnel, and 'si' hypotheses into your speech?",
                    "Self-correction agility: When you make a minor grammatical slip, can you correct yourself and keep the conversational flow going?"
                ]
            },
            {
                "title": "2. Spoken Interaction Audit (Débat & Échange)",
                "items": [
                    "Debating stamina: Can you maintain a lively 5-minute back-and-forth discussion with an educated native speaker?",
                    "Concession techniques: Can you acknowledge a counterargument using « Certes... mais » before defending your thesis?",
                    "Negotiation autonomy: Can you propose practical compromises and reach agreements in role-play disputes?",
                    "Clarification skills: Can you rephrase your argument when your conversation partner asks for clarification?"
                ]
            }
        ]
    }

    # Page 69: Final Self-Evaluation: Receptive & Written Mastery
    pages[69] = {
        "page": 69,
        "type": "audit",
        "title": "Final Self-Evaluation: Receptive & Written Mastery",
        "subtitle": "Checking Your Listening, Reading & Argumentative Writing Skills",
        "badge_num": "68",
        "intro": "Evaluate your listening comprehension of radio broadcasts, reading of newspaper editorials, and essay writing.",
        "items": [
            "I can understand main news stories and cultural reports on French radio broadcasts (RFI, France Info).",
            "I can follow debates and roundtables between multiple native speakers discussing current events.",
            "I can read opinion columns, cultural reviews, and sociological reports in major French publications.",
            "I can decode administrative charters, co-ownership regulations, and formal dispute letters.",
            "I can write a well-structured 160 to 180-word argumentative essay with clear paragraphs and transitions.",
            "I can write formal complaint letters and persuasive cover letters following French conventions.",
            "I can summarize a 500-word article into a concise 100-word executive briefing in my own words.",
            "I can adapt my writing tone across familiar, standard, and formal registers with confidence."
        ],
        "sections": [
            {
                "title": "1. Listening & Reading Audit",
                "items": [
                    "Authentic radio audio: Can you identify the main topic, participant viewpoints, and key statistics on two listens?",
                    "Implied tone & irony: Can you detect when a speaker or journalist is using understatement, sarcasm, or humor?",
                    "Editorial analysis: Can you extract the core thesis of a newspaper article and distinguish facts from opinions?",
                    "Reading efficiency: Can you read a 600-word text and answer comprehension questions within 20 minutes?"
                ]
            },
            {
                "title": "2. Written Production Audit",
                "items": [
                    "Essay architecture: Can you write an argumentative essay with introduction, two body paragraphs, and conclusion?",
                    "Logical transitions: Do you use connectors like 'en effet', 'par conséquent', 'bien que', and 'en revanche' correctly?",
                    "Formal salutations: Do you know the exact opening and closing formulas for administrative and business letters?",
                    "Word count discipline: Can you meet the 160–180 word requirement without falling short or padding?"
                ]
            }
        ]
    }

    # Page 70: Final Self-Evaluation: Grammar, Syntax & Vocabulary Depth
    pages[70] = {
        "page": 70,
        "type": "audit",
        "title": "Final Self-Evaluation: Grammar, Syntax & Vocabulary Depth",
        "subtitle": "Checking Your Core B1 Grammar Rules and 3,000+ Words",
        "badge_num": "69",
        "intro": "Verify that you have mastered the core grammar rules and essential vocabulary of the CEFR B1 level.",
        "items": [
            "I can form and use the subjonctif présent after verbs of necessity, emotion, doubt, and conjunctions.",
            "I know when to use the subjonctif versus the indicatif based on certainty and subjectivity.",
            "I can formulate all three types of hypotheses with 'si' using present, imparfait, and plus-que-parfait.",
            "I can express regrets and unconfirmed news using the conditionnel présent and passé.",
            "I can use complex relative pronouns (dont, lequel, auquel, duquel, ce qui, ce que, ce dont) accurately.",
            "I can report speech in the past, applying proper tense shifts and time word changes.",
            "I have an active vocabulary of over 2,500 to 3,000 words across all intermediate societal themes.",
            "I consistently self-edit past participle agreements, subjunctive triggers, and accents in my writing."
        ],
        "sections": [
            {
                "title": "1. Core Grammar & Syntax Audit",
                "items": [
                    "Subjunctive mastery: Can you identify irregular subjunctive stems (fass-, puiss-, veuill-, aill-) instantly?",
                    "Past tense anteriority: Do you distinguish between passé composé, imparfait, and plus-que-parfait in storytelling?",
                    "Passive and impersonal voice: Can you rephrase passive sentences using 'on' or pronominal passive verbs?",
                    "Gérondif usage: Can you explain simultaneity, means, and cause using 'en + participe présent'?"
                ]
            },
            {
                "title": "2. Thematic Vocabulary Depth (3,000+ Words)",
                "items": [
                    "Society & environment: Integration, diversity, global warming, renewable energy, circular economy, fair trade.",
                    "Work & digital media: Telework, employment contracts, trade unions, cybersecurity, AI, press freedom.",
                    "Culture & citizenship: Cultural heritage, higher education, healthcare system, human rights, civic duties.",
                    "Debate idioms: Jeter de l'huile sur le feu, tirer la sonnette d'alarme, trouver un terrain d'entente."
                ]
            }
        ]
    }

    # Page 71: Final Milestone: Ready to Move to B2 Certification [Respect illustration!]
    pages[71] = {
        "page": 71,
        "type": "audit",
        "title": "Final Milestone: Ready to Move to B2 Certification",
        "subtitle": "Congratulations! You Have Reached CEFR B1 Independence",
        "badge_num": "70",
        "intro": "Review your final checklist items to confirm you are completely ready to step into Advanced Intermediate French (B2).",
        "items": [
            "Spoken autonomy: You can express and defend your opinions on cultural and social topics with ease.",
            "Receptive fluency: You can understand authentic French radio news, documentaries, and press editorials.",
            "Written precision: You can write structured argumentative essays and formal administrative letters.",
            "Grammar maturity: You comfortably command the subjunctive, conditional, passive, and relative pronouns.",
            "Ready to move to B2: You are fully prepared to begin your CEFR B2 advanced intermediate journey!"
        ],
        "sections": [
            {
                "title": "1. Final B1 Certification Audit",
                "items": [
                    "Debate confidence: You can defend a point of view during an unexpected oral discussion with a native speaker.",
                    "Nuanced expression: You can explain doubts, hypotheses, feelings, and constructive disagreements.",
                    "Reading depth: You can follow contemporary literature and analyze journalistic rhetoric.",
                    "Broad vocabulary: You possess over 2,500–3,000 active words across all modern society themes."
                ]
            }
        ]
    }

    return pages

if __name__ == "__main__":
    pages = get_b1_data()
    print(f"Generated {len(pages)} pages.")
    with open("b1_curriculum_data.py", "w", encoding="utf-8") as f:
        f.write("# b1_curriculum_data.py - CEFR B1 Curriculum Dataset\n")
        f.write("# Rich, authentic French with clear, learner-friendly English\n\n")
        f.write("B1_PAGES_DATA = ")
        f.write(pprint.pformat(pages, width=120, sort_dicts=False))
        f.write("\n")
    print("Successfully wrote b1_curriculum_data.py")
