import json

def get_a2_data():
    pages = {}
    
    # Page 1: Cover
    pages[1] = {
        "page": 1,
        "type": "cover",
        "title": "French Learning Roadmap & Checklist",
        "subtitle": "French A2",
        "badge_num": "",
        "intro": ""
    }

    # Page 2: Overall Objectives
    pages[2] = {
        "page": 2,
        "type": "objectives",
        "title": "Overall Objectives of A2 Level (Elementary / Waystage)",
        "subtitle": "Speaking & Listening Skills for Daily Life",
        "badge_num": "1",
        "intro": "Welcome to French A2! At this level, you build on what you learned in A1 and start communicating more independently. You will learn to talk about your daily life, your past, your future plans, and handle real conversations with French speakers.",
        "sections": [
            {
                "title": "Speak (Spoken Production & Spoken Interaction)",
                "items": [
                    "Tell stories about your past, trips, and weekend activities using the passé composé and imparfait.",
                    "Ask for help, shop, and order food in everyday places like shops, train stations, and restaurants.",
                    "Share your opinions, agree or disagree politely, and say what you like or dislike.",
                    "Ask simple questions to keep conversations going with friends, coworkers, and locals."
                ]
            },
            {
                "title": "Listen (Listening Comprehension)",
                "items": [
                    "Catch the main points in clear announcements at train stations, airports, and stores.",
                    "Follow friendly everyday conversations when people speak clearly at normal speed.",
                    "Understand short radio or podcast reports about daily news, weather, and culture."
                ]
            }
        ]
    }

    # Page 3: Overall Objectives (Continued)
    pages[3] = {
        "page": 3,
        "type": "objectives",
        "title": "Overall Objectives of A2 Level (Continued)",
        "subtitle": "Reading & Writing Skills for Practical Independence",
        "badge_num": "2",
        "intro": "At A2, your reading and writing become much more natural and practical. You can read everyday signs, messages, and short articles, and write clear notes, messages, and personal stories.",
        "sections": [
            {
                "title": "Write (Written Production & Interaction)",
                "items": [
                    "Write friendly emails, postcards, and messages (60–80 words) about your holidays, daily life, or recent events.",
                    "Write simple formal notes, like asking a landlord a question or requesting info from a hotel or school.",
                    "Connect your sentences smoothly using words like et, mais, parce que, donc, and alors.",
                    "Fill out standard forms and write brief online reviews about restaurants, hotels, or products."
                ]
            },
            {
                "title": "Read (Reading Comprehension)",
                "items": [
                    "Understand everyday documents like train timetables, restaurant menus, recipes, and store flyers.",
                    "Read personal emails, letters, and invitations from friends and colleagues.",
                    "Read short newspaper news items, event descriptions, and simple online articles."
                ]
            }
        ]
    }

    # Page 4: Real-Life Outcomes & Core Themes 1-4
    pages[4] = {
        "page": 4,
        "type": "themes_table",
        "title": "A2 French – Real-Life Outcomes & Core Themes & Topics",
        "subtitle": "Real-Life Outcomes at CEFR A2 (Themes 1–4)",
        "badge_num": "3",
        "intro": "Here is what you will be able to do in real life by mastering the A2 level, along with the first four core conversational themes.",
        "items": [
            "Talk about what you did yesterday and what you plan to do tomorrow.",
            "Manage everyday shopping, dining out, and travel bookings in French.",
            "Describe people, places, memories, and personal experiences with confidence."
        ],
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 1: Personal Life & Identity", "Studies, daily routines, habits, personality traits, and hobbies.", "« Je fais du sport trois fois par semaine et j'adore la lecture. »"],
                ["Theme 2: Family & Social Circles", "Extended family, childhood memories, friendships, and celebrations.", "« Quand j'étais petit, nous passions nos vacances chez mes grands-parents. »"],
                ["Theme 3: Housing & Home Life", "Finding an apartment, rooms, furniture, household chores, and neighborhood.", "« Je cherche un appartement de deux pièces près du métro. »"],
                ["Theme 4: Work & Professional Life", "Jobs, office routines, daily tasks, meetings, and workplace communications.", "« Je travaille comme graphiste et je participe à des réunions chaque matin. »"]
            ]
        }
    }

    # Page 5: Themes 5-7
    pages[5] = {
        "page": 5,
        "type": "themes_table",
        "title": "A2 French – Core Themes & Topics (Part 2)",
        "subtitle": "Themes 5–7: Travel, Shopping & French Dining",
        "badge_num": "4",
        "intro": "These themes cover travel, shopping, and everyday dining. They give you the practical vocabulary you need for real-world independence.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 5: Travel, Transport & Holidays", "Booking train tickets, hotels, asking for directions, and describing trips.", "« J'ai réservé un billet de train pour Lyon et un hôtel au centre-ville. »"],
                ["Theme 6: Shopping, Fashion & Services", "Buying clothes, sizes, colors, prices, returning items, and post office.", "« Je voudrais essayer cette veste en taille M, s'il vous plaît. »"],
                ["Theme 7: Food, Cooking & Dining Out", "Grocery shopping, following recipes, ordering meals in restaurants, and French food culture.", "« Comme plat principal, je prends le poulet rôti avec des légumes de saison. »"]
            ]
        }
    }

    # Page 6: Themes 8-10
    pages[6] = {
        "page": 6,
        "type": "themes_table",
        "title": "A2 French – Core Themes & Topics (Part 3)",
        "subtitle": "Themes 8–10: Health, Free Time & The Natural World",
        "badge_num": "5",
        "intro": "Learn to talk about your health, free time, culture, and nature using practical A2 French vocabulary.",
        "table": {
            "headers": ["Theme & Context", "Key Topics & Vocabulary", "Example Sentence"],
            "rows": [
                ["Theme 8: Health, Body & Wellbeing", "Visiting the doctor, describing symptoms, illnesses, parts of the body, and pharmacy needs.", "« J'ai mal à la gorge et j'ai de la fièvre depuis deux jours. »"],
                ["Theme 9: Free Time, Sports & Arts", "Outdoor activities, sports, going to the cinema, concerts, and museum visits.", "« Nous sommes allés voir une belle exposition de peinture le week-end dernier. »"],
                ["Theme 10: Nature, Weather & Climate", "Weather forecasts, seasons, climate, animals, and simple eco-habits.", "« Il fait beau aujourd'hui, mais la météo annonce de la pluie pour demain. »"]
            ]
        }
    }

    # Page 7: Communicative Functions
    pages[7] = {
        "page": 7,
        "type": "functions_table",
        "title": "A2 French – Core Communicative Functions",
        "subtitle": "Themes 11–14 & Essential Speaking Functions",
        "badge_num": "6",
        "intro": "Use these core speaking patterns to express your thoughts clearly, ask questions, and interact smoothly with French speakers.",
        "table": {
            "headers": ["Communicative Function", "Grammar & Key Patterns", "Practical Real-Life Example"],
            "rows": [
                ["Narrating Past Events", "Passé composé + Imparfait", "« Samedi matin, je suis sorti et il faisait un soleil magnifique. »"],
                ["Expressing Future Plans", "Futur proche & Futur simple", "« L'année prochaine, nous voyagerons en France pendant trois semaines. »"],
                ["Comparing Things & Places", "Plus... que / Moins... que", "« Ce train est plus rapide que le bus, mais il est un peu plus cher. »"],
                ["Making Polite Requests", "Conditionnel de politesse", "« Pourriez-vous m'indiquer le chemin de la gare, s'il vous plaît ? »"],
                ["Giving Advice & Instructions", "Il faut + infinitif / Impératif", "« Tu devrais te reposer et il faut boire beaucoup d'eau. »"],
                ["Explaining Causes & Goals", "Parce que / Pour + infinitif", "« J'apprends le français pour trouver un travail à Montréal. »"]
            ]
        }
    }

    # Grammar Pages (8-19)
    # Page 8: Nouns, Gender Rules & Plural Patterns
    pages[8] = {
        "page": 8,
        "type": "checklist",
        "title": "A2 Grammar: Nouns, Gender Rules & Plural Patterns",
        "subtitle": "How to Spot Word Genders and Form Plurals",
        "badge_num": "7",
        "intro": "At A2, you can guess if a noun is masculine or feminine by looking at its ending, and learn the most common irregular plural forms.",
        "sections": [
            {
                "title": "1. Word Endings That Show Gender",
                "items": [
                    "Feminine endings: words ending in -tion/-sion (la situation), -té (la liberté), -ette (la bicyclette), -ance/-ence (la présence), and -ure (la culture).",
                    "Masculine endings: words ending in -ment (le développement), -isme (le réalisme), -age (le voyage, le garage), -eau (le bateau), and -oir (le miroir).",
                    "Greek words ending in -e that are masculine: un problème, un système, un programme, un groupe.",
                    "Words that use the same form for both genders: un/une collègue, un/une touriste, un/une artiste."
                ]
            },
            {
                "title": "2. Regular and Irregular Plurals",
                "items": [
                    "Words ending in -al change to -aux: un journal → des journaux, un animal → des animaux, un travail → des travaux.",
                    "Words ending in -s, -x, or -z do not change in the plural: un prix → des prix, un nez → des nez, un pays → des pays.",
                    "Special plurals to memorize: Monsieur → Messieurs, Madame → Mesdames, un grand-père → des grands-pères.",
                    "Remember that plural endings like -s and -x are silent when you speak."
                ]
            }
        ]
    }

    # Page 9: Articles, Partitives & Quantifiers
    pages[9] = {
        "page": 9,
        "type": "checklist",
        "title": "A2 Grammar: Articles, Partitives & Quantifiers",
        "subtitle": "Talking About Quantities and Using the Right Article",
        "badge_num": "8",
        "intro": "Learn how to talk about whole items, parts of things, and exact quantities when shopping, cooking, and talking about habits.",
        "sections": [
            {
                "title": "1. Partitive Articles (Some / Any)",
                "items": [
                    "Use du for masculine things you can't count: « Je bois du café le matin. »",
                    "Use de la for feminine things: « Je voudrais de la salade et de la confiture. »",
                    "Use de l' before a vowel or silent h: « Il faut boire de l'eau tous les jours. »",
                    "Use des for plural items: « J'achète des fruits et des légumes au marché. »"
                ]
            },
            {
                "title": "2. Quantities and Negation with 'De'",
                "items": [
                    "After quantity words, use just de or d': beaucoup de, un peu de, trop de, assez de, un kilo de.",
                    "In negative sentences, du, de la, des turn into de or d': « Je n'ai pas de voiture », « Il n'y a plus d'œufs. »",
                    "Exception: with the verb être, the article stays the same in negative: « Ce ne sont pas des problèmes. »",
                    "Use specific containers: une bouteille d'eau, un paquet de gâteaux, une boîte de chocolat."
                ]
            }
        ]
    }

    # Page 10: Object Pronouns (COD & COI)
    pages[10] = {
        "page": 10,
        "type": "checklist",
        "title": "A2 Grammar: Object Pronouns (Les Pronoms COD & COI)",
        "subtitle": "Replacing Nouns with Me, Te, Le, La, Lui, Leur",
        "badge_num": "9",
        "intro": "Object pronouns help you avoid repeating words and make your French sound much more natural and fluent.",
        "sections": [
            {
                "title": "1. Direct Object Pronouns (COD: me, te, le, la, nous, vous, les)",
                "items": [
                    "Direct objects answer 'Who?' or 'What?' directly: « Tu regardes ce film ? Oui, je le regarde. »",
                    "Replace feminine nouns with la (or l'): « Tu connais cette ville ? Oui, je la connais bien. »",
                    "Replace plural nouns with les: « J'aime ces photos, je les garde toutes. »",
                    "Pronouns go directly before the conjugated verb: « Je ne les vois pas souvent. »"
                ]
            },
            {
                "title": "2. Indirect Object Pronouns (COI: me, te, lui, nous, vous, leur)",
                "items": [
                    "Indirect objects replace people introduced by à: « Je parle à mon ami » → « Je lui parle. »",
                    "Lui is used for both 'to him' and 'to her': « Je lui téléphone ce soir. »",
                    "Leur replaces plural people: « J'écris à mes parents » → « Je leur écris. »",
                    "Placement with two verbs: pronoun goes in front of the infinitive: « Je vais lui parler demain. »"
                ]
            }
        ]
    }

    # Page 11: Pronouns 'Y', 'En' & Relative Pronouns
    pages[11] = {
        "page": 11,
        "type": "checklist",
        "title": "A2 Grammar: Les Pronoms 'Y', 'En' & Relative Pronouns",
        "subtitle": "Using Y, En, Qui, and Que to Connect Sentences",
        "badge_num": "10",
        "intro": "Master two tiny French pronouns (y and en) and learn how to link two sentences together using qui and que.",
        "sections": [
            {
                "title": "1. The Pronouns 'Y' and 'En'",
                "items": [
                    "Y replaces places introduced by à, en, chez, dans: « Tu vas à Paris ? Oui, j'y vais en train. »",
                    "Y replaces things introduced by à: « Tu penses à tes vacances ? Oui, j'y pense souvent. »",
                    "En replaces nouns introduced by de or quantities: « Tu veux du pain ? Oui, j'en veux un peu. »",
                    "En with numbers: keep the number at the end: « Tu as des frères ? Oui, j'en ai deux. »"
                ]
            },
            {
                "title": "2. Relative Pronouns: Qui vs Que",
                "items": [
                    "Qui is the subject of the next verb (followed by a verb): « C'est un ami qui habite à Nice. »",
                    "Que is the object of the next verb (followed by a subject + verb): « C'est le livre que je lis. »",
                    "Que becomes qu' before a vowel sound: « Le cadeau qu'il m'a offert est magnifique. »",
                    "Notice that qui never becomes qu' before a vowel: « La personne qui arrive est en retard. »"
                ]
            }
        ]
    }

    # Page 12: BANGS Adjectives & Comparative Structures
    pages[12] = {
        "page": 12,
        "type": "checklist",
        "title": "A2 Grammar: BANGS Adjectives & Comparative Structures",
        "subtitle": "Where to Put Adjectives and How to Compare Things",
        "badge_num": "11",
        "intro": "Most French adjectives go after the noun, but a small group goes before. Learn the BANGS rule and how to compare items.",
        "sections": [
            {
                "title": "1. The BANGS Rule for Adjective Position",
                "items": [
                    "Beauty: beau, joli go before the noun: « C'est une belle maison et un joli jardin. »",
                    "Age: jeune, vieux, nouveau go before the noun: « Un vieux quartier, une nouvelle voiture. »",
                    "Number: premier, deuxième, dernier go before the noun: « Le premier train du matin. »",
                    "Goodness: bon, mauvais go before the noun: « C'est une bonne idée et un bon repas. »",
                    "Size: grand, petit, gros go before the noun: « Une grande table et un petit café. »",
                    "Colors, shapes, and nationalities always go AFTER the noun: « Une table ronde, du vin français. »"
                ]
            },
            {
                "title": "2. Comparing Things (Comparatives & Superlatives)",
                "items": [
                    "More than: plus + adjective + que (« Le train est plus rapide que la voiture. »).",
                    "Less than: moins + adjective + que (« Ce manteau est moins cher que l'autre. »).",
                    "As... as: aussi + adjective + que (« Cet appartement est aussi grand que le tien. »).",
                    "Superlative: le plus / la plus / les plus (« C'est la plus belle ville de la région. »)."
                ]
            }
        ]
    }

    # Page 13: Complex Negation & Adverbs
    pages[13] = {
        "page": 13,
        "type": "checklist",
        "title": "A2 Grammar: Complex Negation & Adverbs in -ment",
        "subtitle": "Saying 'Never', 'Nothing', 'No longer' and Making Adverbs",
        "badge_num": "12",
        "intro": "Expand your French beyond 'ne... pas'. Learn how to say 'never', 'no one', 'nothing', and build adverbs ending in -ment.",
        "sections": [
            {
                "title": "1. Advanced Negation Patterns",
                "items": [
                    "Ne... plus (no longer / not anymore): « Je n'habite plus à Lyon, j'ai déménagé à Paris. »",
                    "Ne... jamais (never): « Il ne prend jamais le métro aux heures de pointe. »",
                    "Ne... rien (nothing): « Je ne comprends rien à ce problème difficile. »",
                    "Ne... personne (nobody / no one): « Il n'y a personne dans la salle d'attente. »",
                    "Word order in passé composé: rien and jamais go between avoir and participle: « Je n'ai rien vu. »"
                ]
            },
            {
                "title": "2. Forming Adverbs with -ment",
                "items": [
                    "Take the feminine adjective and add -ment: lente → lentement, douce → doucement.",
                    "If masculine adjective ends in a vowel, add -ment directly: poli → poliment, vrai → vraiment.",
                    "Adjectives ending in -ent/-ant become -emment/-amment: récent → récemment, courant → couramment.",
                    "Key irregular adverbs: bon → bien, mauvais → mal, rapide → vite."
                ]
            }
        ]
    }

    # Page 14: Question Formation & Interrogatives
    pages[14] = {
        "page": 14,
        "type": "checklist",
        "title": "A2 Grammar: Question Formation & Interrogatives",
        "subtitle": "Asking Questions in Daily Life with Ease",
        "badge_num": "13",
        "intro": "Learn the three ways to ask questions in French and master question words like où, quand, comment, and pourquoi.",
        "sections": [
            {
                "title": "1. Three Ways to Ask a Question",
                "items": [
                    "Casual style (voice goes up): « Tu viens avec nous ce soir ? »",
                    "Standard style (with est-ce que): « Est-ce que vous avez une chambre libre ? »",
                    "Formal style (inversion): « Parlez-vous anglais ? Avez-vous l'heure ? »",
                    "Negative questions with 'si': answer with si to say yes to a negative question: « Tu ne viens pas ? Si, je viens ! »"
                ]
            },
            {
                "title": "2. Question Words (Où, Quand, Comment, etc.)",
                "items": [
                    "Où (Where): « Où est la pharmacie la plus proche ? »",
                    "Quand (When): « Quand part le prochain train pour Marseille ? »",
                    "Comment (How): « Comment vous appelez-vous ? Comment ça fonctionne ? »",
                    "Pourquoi (Why) and Parce que (Because): « Pourquoi tu pars ? Parce que je suis fatigué. »",
                    "Combien (How much / many): « Combien coûte ce billet aller-retour ? »",
                    "Quel, quelle, quels, quelles (Which / What): « Quelle est votre adresse email ? »"
                ]
            }
        ]
    }

    # Page 15: Prepositions of Time & Connectors
    pages[15] = {
        "page": 15,
        "type": "checklist",
        "title": "A2 Grammar: Prepositions of Time & Connectors",
        "subtitle": "Time Expressions and Words That Link Your Ideas",
        "badge_num": "14",
        "intro": "Use time words to anchor your stories in the past, present, or future, and use connectors to build smooth paragraphs.",
        "sections": [
            {
                "title": "1. Prepositions of Time (Depuis, Pendant, Il y a, Dans)",
                "items": [
                    "Depuis (since / for - still happening): present tense + depuis: « J'habite ici depuis trois ans. »",
                    "Pendant (during / for a finished time): « J'ai vécu en Espagne pendant six mois. »",
                    "Il y a (ago): passé composé + il y a: « Je suis arrivé en France il y a deux semaines. »",
                    "Dans (in - future time): futur + dans: « Le train partira dans dix minutes. »",
                    "En (time taken to do something): « Il a fini ses devoirs en une demi-heure. »"
                ]
            },
            {
                "title": "2. Linking Words (Connectors)",
                "items": [
                    "Telling stories in order: d'abord (first), ensuite (then), puis (after that), enfin (finally).",
                    "Cause and result: parce que (because), comme (as/since), donc (so/therefore), alors (so).",
                    "Contrast and opposition: mais (but), cependant (however), quand même (anyway).",
                    "Giving examples: par exemple, comme, c'est-à-dire (that is to say)."
                ]
            }
        ]
    }

    # Page 16: The Dual-Past System – Passé Composé
    pages[16] = {
        "page": 16,
        "type": "checklist",
        "title": "A2 Grammar: The Dual-Past System – Passé Composé",
        "subtitle": "Talking About Completed Past Events and Actions",
        "badge_num": "15",
        "intro": "The passé composé is used to talk about actions that happened and finished in the past. Learn how to choose between avoir and être.",
        "sections": [
            {
                "title": "1. Passé Composé with Avoir",
                "items": [
                    "Most verbs use avoir: j'ai mangé, tu as fini, il a attendu, nous avons voyagé.",
                    "Regular participle endings: -er verbs end in -é (parlé), -ir verbs end in -i (choisi), -re verbs end in -u (vendu).",
                    "Common irregular participles: fait (faire), pris (prendre), vu (voir), bu (boire), eu (avoir), été (être), mis (mettre).",
                    "Negation goes around the helping verb: « Je n'ai pas compris la question. »"
                ]
            },
            {
                "title": "2. Passé Composé with Être (Movement & Reflexive Verbs)",
                "items": [
                    "Verbs of movement/state use être: aller, venir, arriver, partir, monter, descendre, naître, mourir.",
                    "Reflexive verbs always use être: « Je me suis réveillé à sept heures ce matin. »",
                    "Agreement rule with être: add -e for feminine and -s for plural: « Elle est allée à Paris », « Ils sont partis hier. »",
                    "Watch out for passer, monter, descendre: they use avoir if they have a direct object: « J'ai passé un bel examen. »"
                ]
            }
        ]
    }

    # Page 17: The Dual-Past System – L'Imparfait
    pages[17] = {
        "page": 17,
        "type": "checklist",
        "title": "A2 Grammar: The Dual-Past System – L'Imparfait",
        "subtitle": "Descriptions, Habits, and Background in the Past",
        "badge_num": "16",
        "intro": "The imparfait sets the scene in the past. Use it to describe weather, feelings, physical appearances, and past habits.",
        "sections": [
            {
                "title": "1. How to Form the Imparfait",
                "items": [
                    "Take the nous form of the present tense, drop -ons, and add: -ais, -ais, -ait, -ions, -iez, -aient.",
                    "Example with parler (nous parlons): je parlais, tu parlais, il parlait, nous parlions, vous parliez, ils parlaient.",
                    "The only irregular stem is être: j'étais, tu étais, il était, nous étions, vous étiez, ils étaient.",
                    "Notice that -ais, -ait, and -aient all sound exactly the same when spoken aloud."
                ]
            },
            {
                "title": "2. When to Use Passé Composé vs Imparfait",
                "items": [
                    "Use imparfait for ongoing descriptions: « Il faisait beau et les oiseaux chantaient. »",
                    "Use imparfait for past habits: « Quand j'étais jeune, je faisais du vélo tous les jours. »",
                    "Use passé composé for sudden actions that interrupt: « Je dormais (imparfait) quand le téléphone a sonné (passé composé). »",
                    "Use passé composé for a series of completed steps: « Je me suis levé, j'ai bu un café et je suis parti. »"
                ]
            }
        ]
    }

    # Page 18: Futur Simple & Future Intentions
    pages[18] = {
        "page": 18,
        "type": "checklist",
        "title": "A2 Grammar: Futur Simple & Future Intentions",
        "subtitle": "Talking About Tomorrow, Next Year, and Your Dreams",
        "badge_num": "17",
        "intro": "Learn how to talk about the future using both the futur simple (for scheduled plans and predictions) and the futur proche.",
        "sections": [
            {
                "title": "1. Forming the Futur Simple",
                "items": [
                    "For regular -er and -ir verbs, add endings to the full infinitive: -ai, -as, -a, -ons, -ez, -ont.",
                    "Example with voyager: je voyagerai, tu voyageras, il voyagera, nous voyagerons, vous voyagerez, ils voyageront.",
                    "For -re verbs, drop the final -e before adding endings: attendre → j'attendrai, vendre → je vendrai.",
                    "Key irregular future stems: avoir (aur-), être (ser-), faire (fer-), aller (ir-), venir (viendr-), pouvoir (pourr-)."
                ]
            },
            {
                "title": "2. Futur Proche vs Futur Simple",
                "items": [
                    "Futur proche (aller + infinitive) is used for immediate plans: « Je vais préparer le dîner dans un instant. »",
                    "Futur simple is used for longer-term projects: « Dans cinq ans, j'achèterai une maison à la campagne. »",
                    "Futur simple is common in written French, news forecasts, and formal promises: « La météo sera ensoleillée demain. »",
                    "Si clauses with present + future: « Si j'ai le temps ce week-end, je viendrai te voir. »"
                ]
            }
        ]
    }

    # Page 19: Polite Conditional, Imperative & Modals
    pages[19] = {
        "page": 19,
        "type": "checklist",
        "title": "A2 Grammar: Polite Conditional, Imperative & Modals",
        "subtitle": "Polite Requests, Commands, and Helpful Helping Verbs",
        "badge_num": "18",
        "intro": "Sound polite and natural when ordering food or asking for help, and give friendly directions and instructions.",
        "sections": [
            {
                "title": "1. Polite Requests with the Conditionnel",
                "items": [
                    "Use « Je voudrais... » instead of « Je veux... »: « Je voudrais un café et un croissant, s'il vous plaît. »",
                    "Use « J'aimerais... » to express wishes: « J'aimerais visiter le musée du Louvre ce samedi. »",
                    "Use « Pourriez-vous... ? » to ask someone for help: « Pourriez-vous répéter plus lentement, s'il vous plaît ? »",
                    "Use « Tu devrais... » to give friendly advice: « Tu devrais te reposer si tu es fatigué. »"
                ]
            },
            {
                "title": "2. Imperative & Key Modal Verbs",
                "items": [
                    "Form the imperative with tu, nous, vous without subject pronouns: « Regarde ! », « Allons-y ! », « Prenez votre temps ! »",
                    "Remember to drop the final -s in tu form for -er verbs: « Parle plus fort ! » (not parles).",
                    "Modal verb Pouvoir (can/may): « Est-ce que je peux vous aider ? », « Tu peux venir demain ? »",
                    "Modal verb Devoir (must/have to): « Je dois partir maintenant pour ne pas rater mon train. »",
                    "Modal verb Vouloir (to want): « Nous voulons réserver une table pour ce soir. »"
                ]
            }
        ]
    }

    # Vocab Tables (Pages 20-29)
    # Page 20: Biography & Life Milestones
    pages[20] = {
        "page": 20,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Biography & Life Milestones",
        "subtitle": "Words for Life Events, Childhood & Achievements",
        "badge_num": "19",
        "intro": "These words help you share your personal story, talk about your family history, and describe major events in your life.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la naissance", "n.f.", "birth", "« J'ai fêté la naissance de ma petite nièce. »"],
                ["l'enfance", "n.f.", "childhood", "« J'ai passé une enfance très heureuse à la campagne. »"],
                ["la jeunesse", "n.f.", "youth", "« Pendant ma jeunesse, je jouais souvent au basket. »"],
                ["déménager", "v.", "to move house", "« Nous allons déménager dans une nouvelle maison le mois prochain. »"],
                ["grandir", "v.", "to grow up", "« Elle a grandi dans le sud de la France près de la mer. »"],
                ["le diplôme", "n.m.", "diploma / degree", "« Il a obtenu son diplôme universitaire l'été dernier. »"],
                ["se marier", "v.", "to get married", "« Mes deux meilleurs amis vont se marier en juin. »"],
                ["prendre sa retraite", "expr.", "to retire", "« Mon père va prendre sa retraite à la fin de l'année. »"],
                ["un souvenir", "n.m.", "memory", "« J'ai gardé de magnifiques souvenirs de notre voyage. »"],
                ["le parcours", "n.m.", "life path / journey", "« Son parcours professionnel est vraiment très inspirant. »"]
            ]
        }
    }

    # Page 21: Housing & Rental
    pages[21] = {
        "page": 21,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Housing & Rental",
        "subtitle": "Finding an Apartment, Rooms & Leases",
        "badge_num": "20",
        "intro": "Use these words when looking for an apartment, talking to a landlord, or describing your living space.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["le loyer", "n.m.", "rent", "« Le loyer mensuel est de 750 euros, charges comprises. »"],
                ["le propriétaire", "n.m.", "landlord / owner", "« Le propriétaire a accepté de repeindre le salon. »"],
                ["le locataire", "n.m.", "tenant", "« L'ancien locataire a quitté l'appartement hier. »"],
                ["le rez-de-chaussée", "n.m.", "ground floor", "« L'appartement se trouve au rez-de-chaussée avec terrasse. »"],
                ["l'ascenseur", "n.m.", "elevator", "« Cet immeuble moderne dispose d'un grand ascenseur. »"],
                ["meublé(e)", "adj.", "furnished", "« Je cherche un petit studio meublé près de l'université. »"],
                ["les charges", "n.f.pl.", "utility charges", "« L'eau et le chauffage sont inclus dans les charges. »"],
                ["la colocation", "n.f.", "flatshare", "« Je vis en colocation avec deux étudiants sympathiques. »"],
                ["le quartier", "n.m.", "neighborhood", "« C'est un quartier calme avec de nombreux commerces. »"],
                ["visiter", "v.", "to view / visit", "« Nous allons visiter un appartement demain matin. »"]
            ]
        }
    }

    # Page 22: Household & Maintenance
    pages[22] = {
        "page": 22,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Household & Maintenance",
        "subtitle": "Daily Chores, Appliances & Home Repairs",
        "badge_num": "21",
        "intro": "Talk about household chores, home appliances, and everyday repairs around the house.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["faire le ménage", "expr.", "to do housework", "« Je fais le ménage tous les samedis matin. »"],
                ["l'aspirateur", "n.m.", "vacuum cleaner", "« Je passe l'aspirateur dans toutes les chambres. »"],
                ["le lave-linge", "n.m.", "washing machine", "« Le lave-linge est en panne depuis hier soir. »"],
                ["le lave-vaisselle", "n.m.", "dishwasher", "« Il faut vider le lave-vaisselle après le repas. »"],
                ["la poubelle", "n.f.", "trash can / bin", "« N'oublie pas de sortir la poubelle ce soir. »"],
                ["le fer à repasser", "n.m.", "clothing iron", "« Je repasse mes chemises avec un fer à repasser. »"],
                ["en panne", "expr.", "broken / out of order", "« Le chauffage est en panne, il fait très froid. »"],
                ["réparer", "v.", "to fix / repair", "« Le technicien viendra réparer le chauffe-eau mardi. »"],
                ["la clé", "n.f.", "key", "« J'ai oublié mes clés à l'intérieur de l'appartement. »"],
                ["l'ampoule", "n.f.", "light bulb", "« Il faut changer l'ampoule de la lampe du bureau. »"]
            ]
        }
    }

    # Page 23: Gastronomy & Dining Out
    pages[23] = {
        "page": 23,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Gastronomy & Dining Out",
        "subtitle": "Menus, French Dishes & Ordering Food",
        "badge_num": "22",
        "intro": "Order with confidence at French cafés and restaurants, and understand what is written on food menus.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'entrée", "n.f.", "starter / appetizer", "« En entrée, je choisis une soupe à l'oignon maison. »"],
                ["le plat principal", "n.m.", "main course", "« Comme plat principal, je prends le saumon grillé. »"],
                ["la cuisson", "n.f.", "meat cooking level", "« Pour la cuisson du steak : saignant, à point ou bien cuit ? »"],
                ["la garniture", "n.f.", "side dish", "« Le plat est servi avec des frites comme garniture. »"],
                ["l'addition", "n.f.", "the bill / check", "« L'addition, s'il vous plaît ! On peut payer par carte ? »"],
                ["le pourboire", "n.m.", "tip", "« Le service est compris, mais nous laissons un pourboire. »"],
                ["une carafe d'eau", "expr.", "tap water pitcher", "« Pourriez-vous nous apporter une carafe d'eau fraîche ? »"],
                ["le serveur / la serveuse", "n.", "waiter / waitress", "« Le serveur est très attentionné et souriant. »"],
                ["épicé(e)", "adj.", "spicy", "« Ce plat traditionnel est délicieux mais très épicé. »"],
                ["fait maison", "expr.", "homemade", "« Tous nos desserts sont préparés maison chaque matin. »"]
            ]
        }
    }

    # Page 24: Retail & Shopping
    pages[24] = {
        "page": 24,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Retail & Shopping",
        "subtitle": "Clothing, Sizes, Prices & Returns",
        "badge_num": "23",
        "intro": "Shop smoothly in clothing stores, supermarkets, and boutiques, and handle exchanges or refunds.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la taille", "n.f.", "size (clothing)", "« Vous faites quelle taille ? Je fais du 38 ou du 40. »"],
                ["la pointure", "n.f.", "shoe size", "« Ma pointure de chaussures est du 42. »"],
                ["la cabine d'essayage", "n.f.", "fitting room", "« Où se trouvent les cabines d'essayage, s'il vous plaît ? »"],
                ["essayer", "v.", "to try on", "« Est-ce que je peux essayer ce pull en laine bleue ? »"],
                ["les soldes", "n.m.pl.", "seasonal sales", "« Il y a des réductions fantastiques pendant les soldes. »"],
                ["en promotion", "expr.", "on special offer", "« Ces baskets confortables sont actuellement en promotion. »"],
                ["le ticket de caisse", "n.m.", "receipt", "« Gardez votre ticket de caisse pour tout échange. »"],
                ["rembourser", "v.", "to refund", "« Pouvez-vous me rembourser cet article défectueux ? »"],
                ["le moyen de paiement", "n.m.", "payment method", "« Quels sont vos moyens de paiement acceptés ? »"],
                ["payer en espèces", "expr.", "to pay in cash", "« Vous préférez payer par carte ou payer en espèces ? »"]
            ]
        }
    }

    # Page 25: Urban Mobility & Transport
    pages[25] = {
        "page": 25,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Urban Mobility & Transport",
        "subtitle": "Subway, Buses, Trains & City Transit",
        "badge_num": "24",
        "intro": "Navigate French cities easily using the metro, buses, trains, bicycles, and ride shares.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["la station de métro", "n.f.", "metro station", "« Descendez à la prochaine station de métro. »"],
                ["la correspondance", "n.f.", "connection / transfer", "« Il faut changer de ligne à la correspondance de Châtelet. »"],
                ["le quai", "n.m.", "train platform", "« Le train pour Bordeaux partira du quai numéro 3. »"],
                ["le contrôleur", "n.m.", "ticket inspector", "« Le contrôleur a vérifié tous les billets dans la voiture. »"],
                ["valider son titre", "expr.", "to validate ticket", "« N'oubliez pas de valider votre ticket avant de monter. »"],
                ["la voie", "n.f.", "track / platform lane", "« Attention, le train arrive sur la voie B. »"],
                ["le retard", "n.m.", "delay", "« Le train a dix minutes de retard en raison de travaux. »"],
                ["la piste cyclable", "n.f.", "bike path", "« C'est plus agréable et rapide de rouler sur la piste cyclable. »"],
                ["le carrefour", "n.m.", "intersection", "« Tournez à droite au carrefour avec les feux tricolores. »"],
                ["les heures de pointe", "n.f.pl.", "rush hour", "« Le métro est très bondé pendant les heures de pointe. »"]
            ]
        }
    }

    # Page 26: Travel & Tourism
    pages[26] = {
        "page": 26,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Travel & Tourism",
        "subtitle": "Hotels, Luggage, Sightseeing & Bookings",
        "badge_num": "25",
        "intro": "Book accommodations, ask questions at tourist offices, and describe your holiday experiences.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["une chambre double", "n.f.", "double room", "« J'ai réservé une chambre double avec vue sur la mer. »"],
                ["la réservation", "n.f.", "booking / reservation", "« J'ai une réservation au nom de Martin pour deux nuits. »"],
                ["la valise", "n.f.", "suitcase", "« N'oubliez pas d'étiqueter votre valise avec vos coordonnées. »"],
                ["le passeport", "n.m.", "passport", "« Veuillez présenter votre passeport au contrôle de sécurité. »"],
                ["la visite guidée", "n.f.", "guided tour", "« Nous avons suivi une passionnante visite guidée du château. »"],
                ["le dépliant", "n.m.", "brochure / flyer", "« Prenez un dépliant à l'office de tourisme du village. »"],
                ["le séjour", "n.m.", "stay / trip duration", "« Nous avons passé un séjour inoubliable en Provence. »"],
                ["compris / inclus", "adj.", "included", "« Le petit-déjeuner buffet est compris dans le tarif. »"],
                ["la carte postale", "n.f.", "postcard", "« J'ai envoyé une jolie carte postale à mes grands-parents. »"],
                ["louer un véhicule", "expr.", "to rent a vehicle", "« Nous allons louer une petite voiture pour visiter la région. »"]
            ]
        }
    }

    # Page 27: Health & Medicine
    pages[27] = {
        "page": 27,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Health & Medicine",
        "subtitle": "Symptoms, Doctor Visits & Pharmacy Needs",
        "badge_num": "26",
        "intro": "Explain how you feel when you are sick, talk to a pharmacist, and schedule a doctor appointment.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["avoir mal à", "expr.", "to have pain in", "« J'ai très mal à la tête et mal au dos depuis ce matin. »"],
                ["la fièvre", "n.f.", "fever", "« L'enfant a 38,5 degrés de fièvre, il doit se reposer. »"],
                ["le rhume", "n.m.", "a cold", "« J'ai attrapé un gros rhume avec le changement de saison. »"],
                ["l'ordonnance", "n.f.", "prescription", "« Le médecin m'a rédigé une ordonnance pour des comprimés. »"],
                ["la pharmacie", "n.f.", "pharmacy", "« Où est la pharmacie de garde la plus proche, s'il vous plaît ? »"],
                ["le médicament", "n.m.", "medicine / pill", "« Il faut prendre ce médicament deux fois par jour pendant les repas. »"],
                ["tousser", "v.", "to cough", "« Il tousse beaucoup et a du mal à respirer la nuit. »"],
                ["se blesser", "v.", "to injure oneself", "« Elle s'est blessée à la cheville en jouant au tennis. »"],
                ["le pansement", "n.m.", "bandage / plaster", "« Mettez un petit pansement propre sur votre coupure. »"],
                ["prendre rendez-vous", "expr.", "to book an appointment", "« Je voudrais prendre rendez-vous chez le dentiste ce jeudi. »"]
            ]
        }
    }

    # Page 28: The Professional Workplace
    pages[28] = {
        "page": 28,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: The Professional Workplace",
        "subtitle": "Jobs, Colleagues, Meetings & Daily Tasks",
        "badge_num": "27",
        "intro": "Talk about what you do for a living, your work schedule, and everyday office communications.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["l'entreprise", "n.f.", "company / business", "« Je travaille dans une entreprise internationale de logiciels. »"],
                ["le collègue", "n.m.", "colleague / coworker", "« Mes collègues de travail sont très accueillants et polis. »"],
                ["la réunion", "n.f.", "meeting", "« Nous avons une réunion d'équipe tous les lundis à dix heures. »"],
                ["le bureau", "n.m.", "office / desk", "« Mon bureau se trouve au troisième étage près de la fenêtre. »"],
                ["le courriel", "n.m.", "email", "« Je vous envoie un courriel avec les pièces jointes importantes. »"],
                ["le salaire", "n.m.", "salary / pay", "« Le salaire est versé au début de chaque mois. »"],
                ["le stage", "n.m.", "internship", "« Elle effectue un stage de six mois en marketing digital. »"],
                ["télétravailler", "v.", "to work from home", "« Je télétravaille deux jours par semaine depuis chez moi. »"],
                ["le congé", "n.m.", "leave / holiday time", "« Je prends une semaine de congés payés au mois d'août. »"],
                ["signer un contrat", "expr.", "to sign a contract", "« Il est très heureux de signer un contrat à durée indéterminée. »"]
            ]
        }
    }

    # Page 29: Media, Culture & Hobbies
    pages[29] = {
        "page": 29,
        "type": "vocab_table",
        "title": "A2 Thematic Vocabulary: Media, Culture & Hobbies",
        "subtitle": "News, Cinema, Books, Music & Internet",
        "badge_num": "28",
        "intro": "Discuss what you like watching, listening to, and reading, and talk about your favorite digital media.",
        "table": {
            "headers": ["French Term", "Type", "English Meaning", "Example Sentence"],
            "rows": [
                ["les actualités", "n.f.pl.", "the news", "« J'écoute les actualités à la radio tous les matins au réveil. »"],
                ["le spectacle", "n.m.", "show / performance", "« Nous avons réservé des places pour un spectacle d'humour. »"],
                ["le réseau social", "n.m.", "social network", "« Les jeunes passent beaucoup de temps sur les réseaux sociaux. »"],
                ["le roman", "n.m.", "novel", "« Je lis un roman policier captivant pendant mes trajets. »"],
                ["la séance", "n.f.", "movie screening", "« La prochaine séance de cinéma commence à vingt heures pile. »"],
                ["l'exposition", "n.f.", "art exhibition", "« Il y a une superbe exposition de photographies au musée. »"],
                ["le loisir", "n.m.", "hobby / pastime", "« La peinture et la randonnée sont mes loisirs préférés. »"],
                ["télécharger", "v.", "to download", "« Tu peux télécharger cette application gratuite sur ton téléphone. »"],
                ["l'abonnement", "n.m.", "subscription", "« J'ai un abonnement mensuel pour écouter de la musique. »"],
                ["le documentaire", "n.m.", "documentary", "« Hier soir, nous avons regardé un documentaire sur la nature. »"]
            ]
        }
    }

    # Pages 30-39: Speaking Mastery
    # Page 30: Continuous Monologue (Part 1) [Respect illustration: bottom right has image]
    pages[30] = {
        "page": 30,
        "type": "checklist",
        "title": "A2 Speaking Mastery: Continuous Monologue",
        "subtitle": "Talking About Your Identity, Studies & Work",
        "badge_num": "29",
        "intro": "At A2, you can deliver a simple 1.5 to 2-minute speech about yourself without freezing. Practice these points.",
        "sections": [
            {
                "title": "1. Introducing Yourself Clearly",
                "items": [
                    "Say your name, age, nationality, and where you live: « Je m'appelle..., j'ai... ans et j'habite à... »",
                    "Describe your studies and what you do for work every day: « Je travaille comme... et mes tâches sont... »",
                    "Talk about who you live with: « J'habite seul / avec ma famille / en colocation dans un appartement. »"
                ]
            },
            {
                "title": "2. Talking About Your Daily Routine",
                "items": [
                    "Describe a typical weekday morning and evening: « En semaine, je me lève à sept heures et je prépare mon café. »",
                    "Mention your favorite hobbies and sports: « Pendant mon temps libre, j'aime faire du sport et cuisiner. »",
                    "Explain why you are learning French: « J'apprends le français parce que je voudrais voyager et travailler en France. »"
                ]
            }
        ]
    }

    # Page 31: Continuous Monologue (Part 2)
    pages[31] = {
        "page": 31,
        "type": "checklist",
        "title": "A2 Speaking Mastery: Continuous Monologue (Part 2)",
        "subtitle": "Sharing Past Memories and Holiday Stories",
        "badge_num": "30",
        "intro": "Tell a past story by blending the passé composé for events and the imparfait for background descriptions.",
        "sections": [
            {
                "title": "1. Setting the Scene in the Past",
                "items": [
                    "Describe when and where it took place: « L'été dernier, je suis parti en vacances en Italie avec des amis. »",
                    "Describe the weather and the mood: « Il faisait très chaud et nous étions tous ravis d'être ensemble. »",
                    "Describe what the place was like: « L'hôtel était charmant et la vue sur les montagnes était splendide. »"
                ]
            },
            {
                "title": "2. Recounting the Main Events",
                "items": [
                    "Tell what you did each day: « Nous avons visité des musées, nous avons nagé et goûté des plats locaux. »",
                    "Talk about an unexpected event or surprise: « Un jour, nous avons manqué le train et nous avons dû attendre deux heures ! »",
                    "Conclude with your feelings: « C'était une expérience formidable et j'aimerais beaucoup y retourner un jour. »"
                ]
            }
        ]
    }

    # Page 32: Continuous Monologue (Part 3)
    pages[32] = {
        "page": 32,
        "type": "checklist",
        "title": "A2 Speaking Mastery: Continuous Monologue (Part 3)",
        "subtitle": "Talking About Future Plans and Ambitions",
        "badge_num": "31",
        "intro": "Share your plans for next weekend, your next holiday, and your long-term dreams with confidence.",
        "sections": [
            {
                "title": "1. Near-Future Plans (Futur Proche)",
                "items": [
                    "Describe what you plan to do this coming weekend: « Ce week-end, je vais aller au cinéma et voir des amis. »",
                    "Talk about short-term projects: « La semaine prochaine, je vais commencer un nouveau projet au travail. »",
                    "Mention errands you will run: « Samedi après-midi, je vais faire des courses au supermarché. »"
                ]
            },
            {
                "title": "2. Long-Term Ambitions (Futur Simple)",
                "items": [
                    "Talk about your career dreams: « Dans quelques années, j'aimerais diriger ma propre entreprise. »",
                    "Describe trips you plan to take: « L'année prochaine, nous voyagerons au Canada pendant un mois. »",
                    "Use if clauses to discuss possibilities: « Si je réussis mon examen de français, je chercherai un travail à Paris. »"
                ]
            }
        ]
    }

    # Page 33: Spoken Interaction: Service Counters
    pages[33] = {
        "page": 33,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Service Counters",
        "subtitle": "Getting Help at the Post Office, Station & Bank",
        "badge_num": "32",
        "intro": "Handle practical errands at public service counters politely and without stress.",
        "sections": [
            {
                "title": "1. At the Post Office & Bank",
                "items": [
                    "Ask to send a letter or parcel: « Je voudrais envoyer ce colis en recommandé pour l'Espagne, s'il vous plaît. »",
                    "Buy stamps: « Bonjour, je voudrais trois timbres pour l'étranger. »",
                    "Inquire about payment and currency: « Est-ce que je peux retirer de l'argent avec cette carte bancaire ? »",
                    "Handle missing mail: « Je viens chercher un recommandé avec mon avis de passage et ma pièce d'identité. »"
                ]
            },
            {
                "title": "2. At the Train Station & Travel Desk",
                "items": [
                    "Ask for ticket options: « Je voudrais un aller-retour pour Lyon en seconde classe, s'il vous plaît. »",
                    "Inquire about discounts: « Est-ce qu'il y a un tarif étudiant ou une réduction jeune disponible ? »",
                    "Check departure details: « De quel quai part le train de dix heures quinze pour Marseille ? »",
                    "Confirm train connections: « Est-ce que ce train est direct ou est-ce qu'il faut changer de train ? »"
                ]
            }
        ]
    }

    # Page 34: Spoken Interaction: Retail Exchanges
    pages[34] = {
        "page": 34,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Retail Exchanges",
        "subtitle": "Shopping for Clothes, Sizes, Prices & Returns",
        "badge_num": "33",
        "intro": "Shop in clothing stores and markets, ask clerks for assistance, and handle returns or exchanges with ease.",
        "sections": [
            {
                "title": "1. In Clothing & Shoe Stores",
                "items": [
                    "Greet and explain what you are looking for: « Bonjour, je cherche une veste légère pour le printemps. »",
                    "Ask for sizes: « Avez-vous ce modèle en taille 38 ou en taille supérieure ? »",
                    "Ask to try clothes on: « Où se trouvent les cabines d'essayage, s'il vous plaît ? »",
                    "Give feedback on how it fits: « C'est un peu trop grand / trop serré. Avez-vous la taille en dessous ? »"
                ]
            },
            {
                "title": "2. Inquiries, Payment & Exchanges",
                "items": [
                    "Ask about colors: « Est-ce que vous avez cette chemise en bleu marine ou en blanc ? »",
                    "Ask the price: « Combien coûte cet article ? Est-il en promotion pendant les soldes ? »",
                    "Ask about payment: « Puis-je régler par carte bancaire sans contact ou uniquement en liquide ? »",
                    "Request an exchange or refund: « Cet article a un petit défaut, est-ce possible de l'échanger ? »"
                ]
            }
        ]
    }

    # Page 35: Spoken Interaction: Invitations & Social Life
    pages[35] = {
        "page": 35,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Invitations & Social Life",
        "subtitle": "Inviting Friends, Accepting & Declining Politely",
        "badge_num": "34",
        "intro": "Connect with friends, suggest fun activities, accept invitations gladly, or decline politely with an excuse.",
        "sections": [
            {
                "title": "1. Making Suggestions & Inviting People",
                "items": [
                    "Propose an outing: « Ça te dirait d'aller boire un verre ce soir après le travail ? »",
                    "Suggest a time and place: « On pourrait se retrouver samedi à quatorze heures devant le cinéma. »",
                    "Ask about availability: « Tu es libre ce week-end ? J'organise une petite fête chez moi. »",
                    "Plan activities together: « Qu'est-ce que tu aimerais faire cet après-midi ? »"
                ]
            },
            {
                "title": "2. Accepting, Declining & Proposing Alternatives",
                "items": [
                    "Accept with enthusiasm: « Avec grand plaisir ! C'est une excellente idée ! »",
                    "Confirm details: « Parfait, je note le rendez-vous. Qu'est-ce que je peux apporter ? »",
                    "Decline politely: « Je suis vraiment désolé, mais je ne suis pas disponible ce soir-là. »",
                    "Give a polite reason: « J'ai déjà un engagement de famille prévu depuis longtemps. »",
                    "Offer an alternative date: « Est-ce qu'on peut remettre ça à dimanche ou à la semaine prochaine ? »"
                ]
            }
        ]
    }

    # Page 36: Spoken Interaction: Expressing & Defending Opinions
    pages[36] = {
        "page": 36,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Expressing & Defending Opinions",
        "subtitle": "Sharing Your Thoughts, Agreeing & Disagreeing",
        "badge_num": "35",
        "intro": "Participate in informal discussions with friends and coworkers, share what you think, and explain why.",
        "sections": [
            {
                "title": "1. Stating Your Opinion Clearly",
                "items": [
                    "Use opinion starters: « À mon avis... », « Selon moi... », « Je pense que... », « Je crois que... »",
                    "State your preferences: « Je préfère habiter en ville parce qu'il y a plus d'activités culturelles. »",
                    "Explain your reasons with connectors: « C'est important parce que ça permet de gagner du temps. »",
                    "Say what you like or dislike: « Ce qui me plaît le plus dans cette ville, c'est l'ambiance chaleureuse. »"
                ]
            },
            {
                "title": "2. Agreeing and Disagreeing Politely",
                "items": [
                    "Express agreement: « Oui, tout à fait ! », « Je suis entièrement d'accord avec toi. », « C'est vrai. »",
                    "Express polite disagreement: « Je ne suis pas d'accord », « Ce n'est pas tout à fait mon avis. »",
                    "Add nuance: « Oui, c'est vrai, mais d'un autre côté, c'est un peu trop cher. »",
                    "Ask for their opinion: « Et toi, qu'en penses-tu ? Tu es d'accord avec cette proposition ? »"
                ]
            }
        ]
    }

    # Page 37: Spoken Mastery: Expressing Sensations & Feelings
    pages[37] = {
        "page": 37,
        "type": "checklist",
        "title": "A2 Spoken Mastery: Expressing Sensations & Feelings",
        "subtitle": "Talking About Physical Needs, Moods & Emotions",
        "badge_num": "36",
        "intro": "Express your physical sensations, current mood, and emotional reactions in natural French.",
        "sections": [
            {
                "title": "1. Physical Sensations (Avoir + Noun)",
                "items": [
                    "Express hunger and thirst: « J'ai une faim de loup ! », « J'ai très soif, je vais boire un verre d'eau. »",
                    "Express temperature sensations: « J'ai chaud avec ce pull », « J'ai froid, peux-tu fermer la fenêtre ? »",
                    "Express tiredness and sleepiness: « J'ai sommeil, je me suis couché très tard hier soir. »",
                    "Express fear and haste: « J'ai peur des chiens », « J'ai hâte de partir en vacances d'été ! »"
                ]
            },
            {
                "title": "2. Moods & Emotional States (Être + Adjective)",
                "items": [
                    "Express happiness and excitement: « Je suis très heureux et soulagé d'avoir réussi mon examen. »",
                    "Express worry or disappointment: « Je suis inquiet pour mon ami », « C'est vraiment dommage ! »",
                    "Express surprise: « Quelle surprise ! Je ne m'attendais pas du tout à te voir ici ! »",
                    "Ask about someone's wellbeing: « Ça va ? Qu'est-ce qui ne va pas ? Tu as l'air fatigué aujourd'hui. »"
                ]
            }
        ]
    }

    # Page 38: Spoken Interaction: Telephone Communication
    pages[38] = {
        "page": 38,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Telephone Communication",
        "subtitle": "Making and Answering Phone Calls in French",
        "badge_num": "37",
        "intro": "Feel confident on the phone: introduce yourself, ask to speak to someone, take notes, and end calls politely.",
        "sections": [
            {
                "title": "1. Starting the Call & Introducing Yourself",
                "items": [
                    "Standard phone greeting: « Allô, bonjour, ici Thomas Martin à l'appareil. »",
                    "Ask to speak to someone: « Bonjour, est-ce que je pourrais parler à Madame Dubois, s'il vous plaît ? »",
                    "State the reason for your call: « Je vous appelle au sujet de l'annonce pour l'appartement à louer. »",
                    "Verify you have the right number: « Bonjour, suis-je bien au cabinet médical du docteur Laurent ? »"
                ]
            },
            {
                "title": "2. Taking Messages & Ending the Call",
                "items": [
                    "Handle an unavailable person: « Il est en réunion actuellement. Souhaitez-vous lui laisser un message ? »",
                    "Leave a callback request: « Pourriez-vous lui demander de me rappeler sur mon portable ? »",
                    "Ask to repeat if connection is bad: « La ligne est mauvaise, pourriez-vous répéter plus fort ? »",
                    "End the call politely: « Merci beaucoup pour votre aide. Je vous souhaite une excellente journée. »"
                ]
            }
        ]
    }

    # Page 39: Spoken Interaction: Everyday Idioms & Fillers
    pages[39] = {
        "page": 39,
        "type": "checklist",
        "title": "A2 Spoken Interaction: Everyday Idioms & Fillers",
        "subtitle": "Natural French Fillers and Daily Expressions",
        "badge_num": "38",
        "intro": "Use authentic French conversation fillers and popular expressions to sound like a native speaker.",
        "sections": [
            {
                "title": "1. Conversational Fillers (Thinking Out Loud)",
                "items": [
                    "Use « alors » and « donc » to lead into your thought: « Alors, ce que je voulais dire, c'est que... »",
                    "Use « bon » and « ben » for informal pauses: « Bon, d'accord, on fait comme ça alors ! »",
                    "Use « en fait » (actually): « En fait, je ne suis pas disponible vendredi, mais samedi oui. »",
                    "Use « voyons » or « attends » when hesitating: « Attends, laisse-moi vérifier dans mon agenda. »"
                ]
            },
            {
                "title": "2. Common Daily Idioms",
                "items": [
                    "« Ça roule ! » or « Ça marche ! » (That works / sounds good!): « Rendez-vous à midi ? Ça marche ! »",
                    "« Pas de souci ! » (No problem / no worries): « Merci pour ton aide ! Pas de souci, avec plaisir ! »",
                    "« C'est pas grave » (It doesn't matter / no big deal): « Pardon pour le retard ! C'est pas grave du tout. »",
                    "« Tu m'étonnes ! » (Tell me about it! / No kidding!): « Il fait un froid de canard dehors ! Tu m'étonnes ! »"
                ]
            }
        ]
    }

    # Pages 40-49: Listening Comprehension
    # Page 40: Public Transit Announcements
    pages[40] = {
        "page": 40,
        "type": "checklist",
        "title": "A2 Listening Mastery: Public Transit Announcements",
        "subtitle": "Catching Key Info at Train Stations and Airports",
        "badge_num": "39",
        "intro": "Learn to catch the most important words in French loudspeaker announcements without getting overwhelmed.",
        "sections": [
            {
                "title": "1. Train Station Announcements (SNCF)",
                "items": [
                    "Identify train numbers and destinations: « Le TGV numéro 6614 à destination de Lyon Part-Dieu... »",
                    "Catch platform changes: « ...partira voie D au lieu de la voie F. Eloignez-vous de la bordure du quai. »",
                    "Understand delay announcements: « Ce train accuse un retard estimé à environ quinze minutes. »",
                    "Identify safety instructions: « Prenez garde à la fermeture automatique des portes, attention au départ ! »"
                ]
            },
            {
                "title": "2. Airport & Metro Announcements",
                "items": [
                    "Catch boarding calls: « Dernier appel pour les passagers du vol Air France 1234 porte B12. »",
                    "Understand baggage reminders: « Ne laissez aucun bagage sans surveillance sous peine de destruction. »",
                    "Catch metro line service interruptions: « En raison d'un incident technique, le trafic est interrompu. »",
                    "Recognize stop names and transfers: « Prochain arrêt : Gare du Nord. Correspondance avec les lignes 4 et 5. »"
                ]
            }
        ]
    }

    # Page 41: Counter & Service Transactions
    pages[41] = {
        "page": 41,
        "type": "checklist",
        "title": "A2 Listening Mastery: Counter & Service Transactions",
        "subtitle": "Understanding Cashiers, Waiters & Clerks",
        "badge_num": "40",
        "intro": "Understand fast questions from supermarket cashiers, restaurant servers, and service clerks.",
        "sections": [
            {
                "title": "1. Supermarket & Store Cashiers",
                "items": [
                    "Recognize customer loyalty questions: « Avez-vous la carte de fidélité du magasin ? »",
                    "Recognize bag questions: « Vous désirez un sac pour vos courses ? »",
                    "Understand payment prompts: « Vous réglez comment ? Vous pouvez poser votre carte sur le terminal. »",
                    "Understand receipts offers: « Voulez-vous votre ticket de caisse ou votre reçu bancaire ? »"
                ]
            },
            {
                "title": "2. Restaurant Servers & Hotel Desks",
                "items": [
                    "Understand table greetings: « Bonjour, vous avez réservé une table ? Pour combien de personnes ? »",
                    "Understand ordering prompts: « Vous avez choisi ou vous désirez encore quelques minutes ? »",
                    "Catch water and bread questions: « De l'eau gazeuse ou une carafe d'eau plate pour accompagner ? »",
                    "Understand dessert choices: « Un dessert ou un café pour terminer votre repas ? »"
                ]
            }
        ]
    }

    # Page 42: Voicemails & Phone Messages
    pages[42] = {
        "page": 42,
        "type": "checklist",
        "title": "A2 Listening Mastery: Voicemails & Phone Messages",
        "subtitle": "Understanding Recorded Messages and Callback Requests",
        "badge_num": "41",
        "intro": "Listen to French voicemails, note down numbers and times, and understand why the person called.",
        "sections": [
            {
                "title": "1. Friendly Voicemails from Friends",
                "items": [
                    "Identify who is calling: « Salut, c'est Sarah ! Je t'appelle parce que... »",
                    "Catch proposed meeting times: « On se voit ce soir vers vingt heures au bistrot habituel ? »",
                    "Understand messages about delays: « Je suis coincé dans les bouchons, je serai là avec dix minutes de retard. »",
                    "Catch the call to action: « Rappelle-moi dès que tu as deux minutes, à tout à l'heure ! »"
                ]
            },
            {
                "title": "2. Professional & Medical Messages",
                "items": [
                    "Catch doctor office reminders: « Bonjour, le secrétariat du docteur Martin vous rappelle votre rendez-vous. »",
                    "Write down dates and times: catch numbers like « mardi 14 à 16h45 » on the first listen.",
                    "Understand business hours on automated messages: « Nos bureaux sont ouverts du lundi au vendredi. »",
                    "Note down callback phone numbers spoken in pairs: « au 06 12 34 56 78 »."
                ]
            }
        ]
    }

    # Page 43: Radio Weather & Daily News Bulletins
    pages[43] = {
        "page": 43,
        "type": "checklist",
        "title": "A2 Listening Mastery: Radio Weather & Daily News",
        "subtitle": "Catching Forecasts and Daily News Headlines",
        "badge_num": "42",
        "intro": "Understand simple weather reports and the main points of short news stories on French radio.",
        "sections": [
            {
                "title": "1. Weather Reports (La Météo)",
                "items": [
                    "Identify general weather conditions: « De belles éclaircies sur le nord, mais des averses sur les côtes. »",
                    "Catch temperatures across regions: « Les maximales atteindront 22 degrés à Lille et 28 à Marseille. »",
                    "Understand seasonal alerts: « Attention aux rafales de vent et aux risques d'orages en fin de journée. »",
                    "Catch tomorrow's outlook: « Demain, le ciel sera globalement dégagé avec un temps doux et agréable. »"
                ]
            },
            {
                "title": "2. Short News Headlines (Le Flash Info)",
                "items": [
                    "Catch the main topic: politics, sports, environment, culture, or daily life.",
                    "Identify who did what: « Le président a annoncé une nouvelle loi sur le travail ce matin. »",
                    "Catch sports results: « L'équipe de France de rugby a remporté son match hier soir avec brio. »",
                    "Filter out unfamiliar words to focus on key facts: who, what, when, and where."
                ]
            }
        ]
    }

    # Page 44: Short Radio Stories & Cultural Features
    pages[44] = {
        "page": 44,
        "type": "checklist",
        "title": "A2 Listening Mastery: Short Radio Stories",
        "subtitle": "Following Interviews, Cultural Events & Mini-Reports",
        "badge_num": "43",
        "intro": "Follow short cultural podcasts and interviews with French authors, travelers, and artists.",
        "sections": [
            {
                "title": "1. Everyday Interviews & Street Polls (Micro-trottoir)",
                "items": [
                    "Understand what question people are being asked: « Êtes-vous pour ou contre le télétravail ? »",
                    "Identify if the speaker is positive or negative about the topic.",
                    "Catch key reasons given: « Pour moi, c'est génial parce que j'évite les transports en commun. »",
                    "Hear casual agreement phrases: « Tout à fait », « Absolument », « Pas du tout »."
                ]
            },
            {
                "title": "2. Cultural & Festival Reports",
                "items": [
                    "Understand announcements for local festivals, book fairs, and museum exhibitions.",
                    "Catch ticket prices and opening hours: « L'entrée est libre et gratuite tout le week-end. »",
                    "Identify where the event is happening: « Rendez-vous sur la place de la mairie dès quatorze heures. »",
                    "Understand recommendations: « Un spectacle magnifique à ne surtout pas manquer en famille ! »"
                ]
            }
        ]
    }

    # Page 45: Directions & Street Wayfinding
    pages[45] = {
        "page": 45,
        "type": "checklist",
        "title": "A2 Listening Mastery: Directions & Street Wayfinding",
        "subtitle": "Understanding Directions Given by Locals",
        "badge_num": "44",
        "intro": "When you ask someone on the street for directions, understand their step-by-step instructions easily.",
        "sections": [
            {
                "title": "1. Movement & Direction Words",
                "items": [
                    "« Continuez tout droit » (Keep going straight ahead).",
                    "« Tournez à gauche / à droite à la première intersection » (Turn left/right at first intersection).",
                    "« Traversez la rue / le pont » (Cross the street / bridge).",
                    "« Prenez la deuxième rue sur votre droite » (Take the second street on your right)."
                ]
            },
            {
                "title": "2. Landmarks and Relative Locations",
                "items": [
                    "« Vous allez passer devant la poste et la pharmacie » (You will pass in front of post office).",
                    "« C'est juste à côté de l'église / en face de la gare » (It's right next to the church).",
                    "« C'est au bout de la rue sur votre gauche » (It's at the end of the street on your left).",
                    "« C'est à environ cinq minutes à pied d'ici » (It's about a five-minute walk from here)."
                ]
            }
        ]
    }

    # Page 46: Catching Numbers, Prices, Times & Dates
    pages[46] = {
        "page": 46,
        "type": "checklist",
        "title": "A2 Listening Mastery: Numbers, Prices, Times & Dates",
        "subtitle": "Catching Numbers Quickly When Spoken Aloud",
        "badge_num": "45",
        "intro": "French numbers can be tricky, especially 70 to 99. Train your ear to catch prices, phone numbers, and dates instantly.",
        "sections": [
            {
                "title": "1. Tricky French Numbers (70 to 99)",
                "items": [
                    "Master soixante-dix (70), soixante-quinze (75), soixante-dix-neuf (79).",
                    "Master quatre-vingts (80), quatre-vingt-cinq (85), quatre-vingt-dix (90).",
                    "Master quatre-vingt-onze (91) to quatre-vingt-dix-neuf (99).",
                    "Hear the difference between 13 (treize) and 30 (trente), 14 (quatorze) and 40 (quarante)."
                ]
            },
            {
                "title": "2. Prices, Time & Phone Numbers",
                "items": [
                    "Catch prices with cents: « Ça fera vingt-quatre euros quatre-vingt-dix, s'il vous plaît. »",
                    "Hear the 24-hour clock: 14h30 (quatorze heures trente), 19h45 (dix-neuf heures quarante-cinq).",
                    "Hear French phone numbers spoken in pairs: 01 . 42 . 68 . 75 . 90.",
                    "Catch historical and birth years: dix-neuf cent quatre-vingt-dix (1990), deux mille vingt-quatre (2024)."
                ]
            }
        ]
    }

    # Page 47: Distinguishing Verb Tenses by Ear
    pages[47] = {
        "page": 47,
        "type": "checklist",
        "title": "A2 Listening Mastery: Distinguishing Verb Tenses by Ear",
        "subtitle": "Hearing the Difference Between Past, Present & Future",
        "badge_num": "46",
        "intro": "Train your ears to recognize whether a French speaker is talking about yesterday, today, or tomorrow.",
        "sections": [
            {
                "title": "1. Present vs Passé Composé",
                "items": [
                    "Listen for the helping verb (ai, as, a, est): « J'achète » (present) vs « J'ai acheté » (past).",
                    "Listen for movement verbs with être: « Je vais » (present) vs « Je suis allé » (past).",
                    "Hear irregular past participles: « Je fais » vs « J'ai fait », « Je prends » vs « J'ai pris ».",
                    "Notice time words that give away the tense: aujourd'hui vs hier matin."
                ]
            },
            {
                "title": "2. Imparfait vs Futur Simple",
                "items": [
                    "Imparfait endings have an open 'è' sound (-ais, -ait, -aient): « Je parlais », « Il habitait ».",
                    "Futur simple has a clear 'r' before the vowel (-rai, -ras, -ra): « Je parlerai », « Il habitera ».",
                    "Immediate future with aller: listen for « va / vais »: « Je vais faire » vs « Je faisais ».",
                    "Conditionnel of politeness: « Je voudrais » vs present « Je veux »."
                ]
            }
        ]
    }

    # Page 48: Recognizing Silent Letters & Blended Words
    pages[48] = {
        "page": 48,
        "type": "checklist",
        "title": "A2 Listening Mastery: Silent Letters & Blended Words",
        "subtitle": "How Native French Sounds When Spoken Casually",
        "badge_num": "47",
        "intro": "Native French speakers speak fast and drop letters. Learn how casual spoken French really sounds.",
        "sections": [
            {
                "title": "1. Dropped Letters in Everyday Speech",
                "items": [
                    "Dropping the negative 'ne': you will hear « J'sais pas » instead of « Je ne sais pas ».",
                    "Dropping 'tu' vowels before a vowel: « T'as l'heure ? » instead of « Tu as l'heure ? ».",
                    "Contracting 'il y a': sounds like « Y a »: « Y a quelqu'un ? », « Y a pas de problème. »",
                    "Dropping 'il' in everyday phrases: « Faut partir » instead of « Il faut partir »."
                ]
            },
            {
                "title": "2. Liaisons and Enchaînements",
                "items": [
                    "Liaison with -s sounds like 'z': « Les_amis » sounds like « lé-zami ».",
                    "Liaison with -n: « Un_enfant », « Bon_anniversaire ».",
                    "Liaison with -t: « C'est_un_ami » sounds like « cè-tun-nami ».",
                    "Remember that 'et' (and) NEVER has a liaison: say « et / après » with a clean pause."
                ]
            }
        ]
    }

    # Page 49: Listening Strategies: Key Word Detection
    pages[49] = {
        "page": 49,
        "type": "checklist",
        "title": "A2 Listening Mastery: Key Word Detection",
        "subtitle": "Smart Listening Techniques for Conversations and Tests",
        "badge_num": "48",
        "intro": "You don't need to understand every single word to understand the message. Learn smart listening strategies.",
        "sections": [
            {
                "title": "1. Focusing on the Core Message",
                "items": [
                    "Focus first on nouns and main verbs: they carry 80% of the message.",
                    "Identify the speaker's tone of voice: are they happy, upset, surprised, or in a rush?",
                    "Use context and background sounds: train whistle, cash register, or restaurant noise give clues.",
                    "Don't panic if you miss a word: keep listening to follow the rest of the sentence."
                ]
            },
            {
                "title": "2. Clarification Questions When Talking to Locals",
                "items": [
                    "Ask them to speak slower: « Pourriez-vous parler un peu plus lentement, s'il vous plaît ? »",
                    "Ask them to repeat: « Excusez-moi, je n'ai pas bien entendu. Pouvez-vous répéter ? »",
                    "Confirm what you understood: « Si j'ai bien compris, le musée ouvre à quatorze heures, c'est ça ? »",
                    "Ask what a word means: « Que veut dire ce mot, s'il vous plaît ? »"
                ]
            }
        ]
    }

    # Pages 50-59: Reading Comprehension
    # Page 50: Signs, Notices & Warning Boards
    pages[50] = {
        "page": 50,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Signs, Notices & Warnings",
        "subtitle": "Understanding Street Signs, Store Hours & Public Notices",
        "badge_num": "49",
        "intro": "Read signs, store windows, warnings, and safety rules easily in public spaces across France.",
        "sections": [
            {
                "title": "1. Store Hours & Entrance Signs",
                "items": [
                    "« Ouvert du lundi au samedi de 9h à 19h sans interruption » (Open continuously).",
                    "« Fermé les dimanches et jours fériés » (Closed on Sundays and public holidays).",
                    "« Entrée libre et gratuite » (Free admission for everyone).",
                    "« Poussez / Tirez » (Push / Pull on doors)."
                ]
            },
            {
                "title": "2. Rules, Warnings & Prohibitions",
                "items": [
                    "« Défense de fumer / Interdiction de stationner » (No smoking / No parking).",
                    "« Attention aux pickpockets / Attention à la marche » (Watch out for pickpockets / Mind the step).",
                    "« Sortie de secours / Issue de secours » (Emergency exit).",
                    "« Chiens interdits sauf chiens guides d'aveugles » (No dogs allowed except guide dogs)."
                ]
            }
        ]
    }

    # Page 51: Real Estate Listings & Apartment Ads
    pages[51] = {
        "page": 51,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Real Estate Listings",
        "subtitle": "Decoding Apartment Ads, Floor Space & Rent Terms",
        "badge_num": "50",
        "intro": "Understand French apartment classified ads, rental abbreviations, and descriptions of living spaces.",
        "sections": [
            {
                "title": "1. Common Real Estate Abbreviations",
                "items": [
                    "T2 / F2: two-room apartment (bedroom + living room + kitchen + bathroom).",
                    "Studio: single main living room with kitchenette and separate bathroom.",
                    "m² (mètres carrés): surface area (« Studio lumineux de 28 m² rénové »).",
                    "CC (charges comprises): rent includes monthly utility charges.",
                    "RDC (rez-de-chaussée): ground floor."
                ]
            },
            {
                "title": "2. Apartment Features & Descriptions",
                "items": [
                    "« Cuisine équipée avec plaques de cuisson et réfrigérateur » (Fitted kitchen).",
                    "« Balcon sans vis-à-vis avec vue dégagée » (Private balcony without overlooking neighbors).",
                    "« Proche de toutes commodités et transports » (Close to shops, services, and transit).",
                    "« Disponible immédiatement / Caution demandée : 1 mois de loyer » (Available right away)."
                ]
            }
        ]
    }

    # Page 52: Menus, Recipes & Food Ingredients
    pages[52] = {
        "page": 52,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Menus, Recipes & Food",
        "subtitle": "Reading Menus, Daily Specials & French Recipes",
        "badge_num": "51",
        "intro": "Read restaurant chalkboards, set menus, and simple recipe instructions without reaching for a dictionary.",
        "sections": [
            {
                "title": "1. Restaurant Menus & Formulas",
                "items": [
                    "« Formule midi : Entrée + Plat ou Plat + Dessert à 16,50 € » (Lunch special combo).",
                    "« Plat du jour : Filet de bar rôti aux herbes de Provence » (Daily special).",
                    "« Menu enfant avec boisson et glace incluses » (Kids menu with drink and ice cream).",
                    "« Boissons non comprises / Service compris » (Drinks not included / Service included)."
                ]
            },
            {
                "title": "2. Reading Recipe Instructions",
                "items": [
                    "Understand cooking action verbs: couper (cut), mélanger (mix), verser (pour), cuire (cook).",
                    "Understand oven instructions: « Préchauffer le four à 180 degrés pendant dix minutes. »",
                    "Understand ingredient measurements: 250 g de farine, 3 œufs, une cuillère à soupe d'huile.",
                    "Understand cooking durations: « Laisser mijoter à feu doux pendant vingt minutes. »"
                ]
            }
        ]
    }

    # Page 53: Transit Timetables, Tickets & Route Maps
    pages[53] = {
        "page": 53,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Transit Timetables & Tickets",
        "subtitle": "Understanding Train Schedules, Bus Stops & Metro Maps",
        "badge_num": "52",
        "intro": "Read French train tickets, bus timetables, and transit network maps easily when traveling.",
        "sections": [
            {
                "title": "1. Train Tickets & Boarding Passes",
                "items": [
                    "Identify departure and arrival stations: Départ (Gare de Lyon), Arrivée (Nice Ville).",
                    "Find coach and seat numbers: Voiture 5 (Coach 5), Place assise 42 (Seat 42), Fenêtre (Window).",
                    "Understand ticket conditions: « Billet non échangeable et non remboursable après le départ. »",
                    "Check boarding limits: « Accès au train fermé 2 minutes avant le départ. »"
                ]
            },
            {
                "title": "2. Bus & Metro Schedules",
                "items": [
                    "Read frequency charts: « Un bus toutes les 8 minutes aux heures de pointe. »",
                    "Check operating days: « Circule uniquement du lundi au vendredi sauf jours fériés. »",
                    "Identify terminus stations to know the direction of travel: « Direction : Mairie d'Ivry. »",
                    "Understand transit notices: « Arrêt temporairement non desservi pour cause de travaux. »"
                ]
            }
        ]
    }

    # Page 54: Tourist Guides & Travel Brochures
    pages[54] = {
        "page": 54,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Tourist Guides & Brochures",
        "subtitle": "Finding Key Info in City Guides and Museum Leaflets",
        "badge_num": "53",
        "intro": "Get the most out of your trips by reading French travel guides, castle brochures, and museum programs.",
        "sections": [
            {
                "title": "1. Museum Leaflets & City Maps",
                "items": [
                    "Find opening hours and quiet times: « Nocturne tous les jeudis jusqu'à 21h45. »",
                    "Check ticket prices: « Tarif plein : 12 € / Tarif réduit pour les moins de 26 ans : 8 €. »",
                    "Identify guided tour schedules: « Visites guidées en français à 11h et 15h. »",
                    "Look for audio guide information: « Audioguides disponibles en plusieurs langues à l'accueil. »"
                ]
            },
            {
                "title": "2. City Highlights & Walking Tours",
                "items": [
                    "Read brief historical overviews of famous monuments and historic city centers.",
                    "Follow walking path suggestions: « Départ de la fontaine, suivez le sentier balisé en bleu. »",
                    "Spot local tips and viewpoints: « Le plus beau panorama sur la baie au coucher du soleil. »",
                    "Understand dining recommendations: « Les meilleures adresses pour déguster des crêpes bretonnes. »"
                ]
            }
        ]
    }

    # Page 55: Press & Local News Highlights
    pages[55] = {
        "page": 55,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Press & Local News",
        "subtitle": "Reading Short Newspaper Stories and Community News",
        "badge_num": "54",
        "intro": "Read short articles in French newspapers, local town magazines, and online community news boards.",
        "sections": [
            {
                "title": "1. Local Community News (Les Faits Divers)",
                "items": [
                    "Catch the headline's main event: « Nouveau marché bio inauguré ce samedi au centre-ville. »",
                    "Find the 5 Ws: Qui (who), Quoi (what), Quand (when), Où (where), Pourquoi (why).",
                    "Understand simple reports on public works: « Rénovation de la bibliothèque municipale dès mars. »",
                    "Read local sports scores and achievements: « Belle victoire de l'équipe locale de handball. »"
                ]
            },
            {
                "title": "2. Cultural & Lifestyle Columns",
                "items": [
                    "Read book and movie recommendations in weekly magazines.",
                    "Understand event roundups: « Que faire ce week-end à Bordeaux ? Notre sélection de sorties. »",
                    "Read simple tips on health, gardening, or eco-habits.",
                    "Notice connectors that structure the news: selon, d'après, par ailleurs, enfin."
                ]
            }
        ]
    }

    # Page 56: Personal Emails, Postcards & Letters
    pages[56] = {
        "page": 56,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Personal Emails & Letters",
        "subtitle": "Reading Friendly Messages, Invitations & Updates",
        "badge_num": "55",
        "intro": "Read warm messages from French friends, family members, and coworkers with full understanding.",
        "sections": [
            {
                "title": "1. Personal Greetings & Email Openers",
                "items": [
                    "Friendly greetings: « Cher Julien », « Chère Marie », « Coucou tout le monde ! »",
                    "Warm opening lines: « J'espère que tu vas bien et que ta semaine se passe bien. »",
                    "Excuses for late replies: « Pardon de ne pas avoir répondu plus tôt, j'étais très occupé. »",
                    "Asking for news: « Quelles sont les nouvelles depuis la dernière fois ? »"
                ]
            },
            {
                "title": "2. Main Message Content & Sign-Offs",
                "items": [
                    "Understand personal stories about recent trips, family celebrations, or new jobs.",
                    "Spot invitations with dates and locations: « On fête mon anniversaire samedi soir chez moi. »",
                    "Friendly sign-offs: « Bises », « Grosses bises », « Amitiés », « À très bientôt j'espère ! »",
                    "Postscripts with extra thoughts: « P.S. N'oublie pas d'apporter ton maillot de bain ! »"
                ]
            }
        ]
    }

    # Page 57: Event Programs & Cinema Listings
    pages[57] = {
        "page": 57,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Event Programs & Cinema",
        "subtitle": "Reading Theater Programs, Concerts & Movie Schedules",
        "badge_num": "56",
        "intro": "Plan an evening out in France by reading cinema showtimes, theater brochures, and music festival posters.",
        "sections": [
            {
                "title": "1. Cinema Listings & Movie Formats",
                "items": [
                    "VF (Version Française): foreign movie dubbed into French.",
                    "VOST (Version Originale Sous-Titrée): foreign movie with French subtitles.",
                    "UGC / Gaumont / Cinéma d'art et d'essai (independent movie theater).",
                    "Understand movie summaries: « Une comédie touchante et drôle qui réunit toute la famille. »"
                ]
            },
            {
                "title": "2. Festival & Concert Programs",
                "items": [
                    "Check stage lineups and artist schedules: « Scène principale : concert à 21h30. »",
                    "Understand ticket options: « Pass 1 jour : 35 € / Pass 3 jours complet : 85 €. »",
                    "Look for practical advice: « Navettes de bus gratuites depuis le parking relais. »",
                    "Read safety guidelines: « Bouteilles en verre et objets tranchants interdits sur le site. »"
                ]
            }
        ]
    }

    # Page 58: Simple Job Postings & Classifieds
    pages[58] = {
        "page": 58,
        "type": "checklist",
        "title": "A2 Reading Comprehension: Job Postings & Classifieds",
        "subtitle": "Understanding Job Ads, Required Skills & Classifieds",
        "badge_num": "57",
        "intro": "Read simple job advertisements, understand contract types, and decode buy/sell classifieds.",
        "sections": [
            {
                "title": "1. Decoding Job Advertisements",
                "items": [
                    "CDI (Contrat à Durée Indéterminée): permanent contract.",
                    "CDD (Contrat à Durée Déterminée): fixed-term temporary contract.",
                    "Temps plein (full-time: 35 hours) vs Temps partiel (part-time: 20 hours).",
                    "Understand job tasks: « Vous serez en charge de l'accueil téléphonique et du classement. »",
                    "Understand required qualifications: « Débutant accepté, bon niveau d'anglais souhaité. »"
                ]
            },
            {
                "title": "2. Online Classifieds (Le Bon Coin, etc.)",
                "items": [
                    "Understand item conditions: « Comme neuf », « Très bon état », « Jamais servi avec emballage ». ",
                    "Understand pickup options: « À venir chercher sur place / Envoi postal possible. »",
                    "Understand price terms: « Prix ferme » (no bargaining) vs « Prix à débattre » (negotiable).",
                    "Contact instructions: « Premier contact par courriel ou par message privé uniquement. »"
                ]
            }
        ]
    }

    # Page 59: Reading Strategies: Skimming & Guessing Meaning
    pages[59] = {
        "page": 59,
        "type": "checklist",
        "title": "A2 Reading Strategies: Skimming & Guessing Meaning",
        "subtitle": "Smart Techniques for Fast and Effective Reading",
        "badge_num": "58",
        "intro": "Learn how to read French texts faster by spotting cognates, keywords, and structural clues.",
        "sections": [
            {
                "title": "1. Skimming & Scanning Techniques",
                "items": [
                    "Scan headings, bold words, and bullet points first to get the main idea.",
                    "Look for familiar French-English words (cognates): information, culture, restaurant, train.",
                    "Watch out for false friends (faux amis): « actuellement » means currently (not actually), « attendre » means to wait (not attend).",
                    "Look at pictures, dates, prices, and numbers to understand the context quickly."
                ]
            },
            {
                "title": "2. Guessing Words from Context",
                "items": [
                    "Look at the words right before and after an unknown word to guess its meaning.",
                    "Identify the part of speech: is the mystery word a noun, a verb, or an adjective?",
                    "Break down compound words and prefixes: in- (impossible), re- (refaire = to do again).",
                    "Keep moving: you do not need every word to understand the overall message."
                ]
            }
        ]
    }

    # Pages 60-67: Written Production & Interaction
    # Page 60: Informal Letters & Holiday Postcards
    pages[60] = {
        "page": 60,
        "type": "checklist",
        "title": "A2 Written Production: Informal Letters & Postcards",
        "subtitle": "Writing Fun Holiday Postcards and Personal Updates",
        "badge_num": "59",
        "intro": "Write friendly postcards and messages (60 to 80 words) telling friends about your holidays and travels.",
        "sections": [
            {
                "title": "1. Writing a Holiday Postcard",
                "items": [
                    "Warm opening: « Coucou de Marseille ! Un petit mot depuis le sud de la France. »",
                    "Describe the location and weather: « Il fait un soleil radieux et la mer est magnifique. »",
                    "Share two or three activities you did: « Hier, nous avons visité le vieux port et mangé des glaces. »",
                    "Share your plans for tomorrow: « Demain, nous allons faire une excursion en bateau dans les calanques. »",
                    "Warm sign-off: « Je pense fort à vous tous, je vous embrasse affectueusement ! »"
                ]
            },
            {
                "title": "2. Checking Word Count & Formatting",
                "items": [
                    "Aim for 60 to 80 words to meet CEFR A2 test requirements.",
                    "Use both passé composé (what you did) and futur proche (what you will do).",
                    "Link your sentences with simple connectors: et, puis, ensuite, mais.",
                    "Write clear, readable French handwriting or formatting."
                ]
            }
        ]
    }

    # Page 61: Friendly Emails: Invitations, Acceptance & Refusal
    pages[61] = {
        "page": 61,
        "type": "checklist",
        "title": "A2 Written Production: Friendly Emails & Invitations",
        "subtitle": "Inviting Friends, Saying Yes, and Declining Politely",
        "badge_num": "60",
        "intro": "Draft clear, friendly emails to invite people over, celebrate events, or reply to social invitations.",
        "sections": [
            {
                "title": "1. Writing an Invitation Message",
                "items": [
                    "State the occasion: « Samedi prochain, je fête mon anniversaire et ma crémaillère ! »",
                    "Give clear date, time, and address: « Rendez-vous chez moi à partir de 19h30 au 14 rue Victor Hugo. »",
                    "Explain what to bring: « J'offre le plat principal, mais vous pouvez apporter un dessert ou une boisson. »",
                    "Ask for an RSVP: « Merci de me confirmer ta présence avant jeudi soir pour que je m'organise. »"
                ]
            },
            {
                "title": "2. Writing a Reply (Accepting or Declining)",
                "items": [
                    "Accept with warmth: « Merci beaucoup pour l'invitation ! Je viendrai avec grand plaisir. »",
                    "Offer to help: « Dis-moi si tu as besoin d'aide pour préparer ou ranger la salle. »",
                    "Decline politely: « Merci pour l'invitation, mais malheureusement je ne pourrai pas venir ce samedi. »",
                    "Give a brief explanation: « J'ai déjà un repas de famille de prévu depuis plusieurs semaines. »",
                    "Send good wishes: « Amusez-vous bien et j'espère qu'on se verra très vite ! »"
                ]
            }
        ]
    }

    # Page 62: Formal Inquiries & Service Messages
    pages[62] = {
        "page": 62,
        "type": "checklist",
        "title": "A2 Written Production: Formal Inquiries & Inquiries",
        "subtitle": "Writing to Hotels, Schools, Landlords & Agencies",
        "badge_num": "61",
        "intro": "Write polite, professional short emails (60–80 words) to ask for information or book a service.",
        "sections": [
            {
                "title": "1. Formal Email Openings & Courtesies",
                "items": [
                    "Polite salutations: « Madame, Monsieur, », « Bonjour Madame Dubois, »",
                    "State your purpose clearly: « Je vous écris pour obtenir des informations au sujet de... »",
                    "Inquire about availability: « Serait-il possible de réserver une chambre du 10 au 14 mai ? »",
                    "Ask about rates and conditions: « Pourriez-vous m'indiquer vos tarifs et les pièces à fournir ? »"
                ]
            },
            {
                "title": "2. Polite Sign-Offs & Closings",
                "items": [
                    "Thanking the recipient: « En vous remerciant par avance pour votre aide et votre réponse. »",
                    "Standard formal closing: « Cordialement, », « Bien cordialement, », « Sincères salutations, »",
                    "Include your full contact details: prénom, nom, numéro de téléphone, adresse postale.",
                    "Keep sentences concise, clear, and grammatically accurate."
                ]
            }
        ]
    }

    # Page 63: Short Personal Stories
    pages[63] = {
        "page": 63,
        "type": "checklist",
        "title": "A2 Written Production: Short Personal Stories",
        "subtitle": "Telling a Memorable Story or Unforgettable Day",
        "badge_num": "62",
        "intro": "Write an engaging personal story (70–90 words) about a memorable trip, a surprise, or a funny day.",
        "sections": [
            {
                "title": "1. Building the Narrative Step by Step",
                "items": [
                    "Set the stage: « Il y a deux ans, j'ai vécu une journée tout à fait inoubliable à Lyon. »",
                    "Describe the setting with imparfait: « Le ciel était bleu et il y avait une ambiance festive dans les rues. »",
                    "Introduce the main event with passé composé: « Soudain, nous avons rencontré un vieil ami d'école par hasard ! »",
                    "Add dialogue or thoughts: « Nous avons discuté pendant des heures dans un petit café chaleureux. »"
                ]
            },
            {
                "title": "2. Concluding Your Story",
                "items": [
                    "Reflect on how it ended: « Finalement, nous avons dîné tous ensemble jusqu'à minuit. »",
                    "Express what it meant to you: « C'est un des plus beaux souvenirs de mes années d'études. »",
                    "Use chronological markers: d'abord, soudain, ensuite, après cela, enfin.",
                    "Verify agreement of past participles with être and reflexive verbs."
                ]
            }
        ]
    }

    # Page 64: Writing Online Reviews & Customer Feedback
    pages[64] = {
        "page": 64,
        "type": "checklist",
        "title": "A2 Written Production: Writing Online Reviews",
        "subtitle": "Reviewing Hotels, Restaurants & Tourist Attractions",
        "badge_num": "63",
        "intro": "Share your thoughts online by writing helpful 50 to 70-word customer reviews in clear French.",
        "sections": [
            {
                "title": "1. Praising a Great Restaurant or Hotel",
                "items": [
                    "Give a catchy headline: « Très belle découverte ! », « Un séjour parfait en famille ! »",
                    "Praise specific aspects: « Les plats faits maison sont délicieux et le serveur est très attentif. »",
                    "Comment on value: « Les prix sont très raisonnables par rapport à la qualité exceptionnelle. »",
                    "Give a clear recommendation: « Je recommande chaleureusement cet établissement à tout le monde ! »"
                ]
            },
            {
                "title": "2. Constructive Criticism & Points to Improve",
                "items": [
                    "State the issue politely: « L'hôtel est bien situé, mais la chambre était un peu bruyante la nuit. »",
                    "Mention room maintenance: « La climatisation ne fonctionnait pas très bien pendant notre séjour. »",
                    "Balance positive and negative: « Le petit-déjeuner était bon, mais le service était un peu trop lent. »",
                    "Conclude fairly: « Une expérience correcte dans l'ensemble, mais des améliorations sont nécessaires. »"
                ]
            }
        ]
    }

    # Page 65: Practical Notes, Instructions & To-Do Lists
    pages[65] = {
        "page": 65,
        "type": "checklist",
        "title": "A2 Written Production: Practical Notes & To-Do Lists",
        "subtitle": "Leaving Notes for Roommates, Family & Babysitters",
        "badge_num": "64",
        "intro": "Write practical notes, instructions, shopping lists, and reminders for people in your daily life.",
        "sections": [
            {
                "title": "1. Notes for Roommates & Family",
                "items": [
                    "Leave errand instructions: « Je suis parti faire des courses. Peux-tu nourrir le chat et arroser les plantes ? »",
                    "Give key updates: « Le plombier passera demain matin vers 10h. J'ai laissé les clés sur la table de l'entrée. »",
                    "Dinner notes: « J'ai préparé une quiche pour ce soir, elle est dans le réfrigérateur. Bon appétit ! »",
                    "Signing off: « À ce soir ! Bisous. »"
                ]
            },
            {
                "title": "2. Instructions for Babysitters or House Sitters",
                "items": [
                    "Bedtime rules: « Les enfants doivent se coucher à 20h30 après avoir brossé leurs dents. »",
                    "Emergency phone numbers: « En cas de problème urgent, appelez-moi sur mon portable au 06... »",
                    "Food and allergies: « Lucas ne doit pas manger de cacahuètes car il est très allergique. »",
                    "WiFi and entertainment details: « Le mot de passe du réseau WiFi est écrit sur le tableau blanc. »"
                ]
            }
        ]
    }

    # Page 66: Sentence Connectors & Paragraph Flow
    pages[66] = {
        "page": 66,
        "type": "checklist",
        "title": "A2 Writing Mechanics: Sentence Connectors & Flow",
        "subtitle": "Using Mais, Donc, Parce que, and Ensuite to Connect Sentences",
        "badge_num": "65",
        "intro": "Make your writing flow smoothly by connecting your thoughts instead of writing short, choppy sentences.",
        "sections": [
            {
                "title": "1. Connecting Ideas Logically",
                "items": [
                    "Cause with parce que: « J'ai pris le bus parce qu'il pleuvait des cordes ce matin. »",
                    "Result with donc / alors: « J'étais très fatigué, donc je suis resté à la maison me reposer. »",
                    "Contrast with mais: « Cet appartement est magnifique, mais le loyer est un peu trop élevé. »",
                    "Addition with et / aussi: « J'ai acheté des fruits et j'ai aussi pris du bon fromage. »"
                ]
            },
            {
                "title": "2. Ordering Your Paragraphs Chronologically",
                "items": [
                    "Start with d'abord (first): « D'abord, nous avons visité le musée d'art moderne. »",
                    "Continue with ensuite / puis (then / next): « Ensuite, nous avons déjeuné dans un bistrot typique. »",
                    "Add later events with plus tard / après (later / after): « Plus tard dans l'après-midi, nous avons fait du shopping. »",
                    "End with enfin / finalement (finally / at last): « Enfin, nous sommes rentrés à l'hôtel fatigués mais ravis. »"
                ]
            }
        ]
    }

    # Page 67: Writing Mechanics: Agreement & Spelling Checks
    pages[67] = {
        "page": 67,
        "type": "checklist",
        "title": "A2 Writing Mechanics: Agreement & Spelling Checks",
        "subtitle": "How to Self-Edit Your French Texts Before Submitting",
        "badge_num": "66",
        "intro": "Develop a quick proofreading routine to catch gender agreements, plural endings, and verb conjugations.",
        "sections": [
            {
                "title": "1. The 4-Step Self-Editing Checklist",
                "items": [
                    "Step 1: Check noun-adjective agreements (add -e for feminine, add -s for plural).",
                    "Step 2: Check verb endings for the subject (je parle, tu parles, nous parlons, ils parlent).",
                    "Step 3: Check passé composé participles: check if verbs using être agree with the subject.",
                    "Step 4: Check accents: é (aigu), è/à (grave), ê/ô (circonflexe) and c cédille (ç)."
                ]
            },
            {
                "title": "2. High-Frequency Traps to Avoid",
                "items": [
                    "Don't confuse 'a' (has) with 'à' (at/to): « Il a mal à la tête. »",
                    "Don't confuse 'ou' (or) with 'où' (where): « Tu préfères le thé ou le café ? », « Où habites-tu ? »",
                    "Don't confuse 'et' (and) with 'est' (is): « Marc est grand et très gentil. »",
                    "Don't confuse 'son/sa' (his/her) with 'leur' (their): « Ils aiment leur professeur. »"
                ]
            }
        ]
    }

    # Assessment & Readiness (Pages 68-71)
    # Page 68: Final Self-Evaluation: Speaking Readiness & Fluency
    pages[68] = {
        "page": 68,
        "type": "audit",
        "title": "Final Self-Evaluation: Speaking Readiness & Fluency",
        "subtitle": "Checking Your Spoken Communication Skills",
        "badge_num": "67",
        "intro": "Use this checklist to check if you can speak French smoothly and confidently in everyday situations.",
        "items": [
            "I can deliver an uninterrupted 2-minute monologue about my life, routine, and hobbies.",
            "I can recount a past journey or childhood memory combining passé composé and imparfait.",
            "I can explain my future career plans and personal ambitions using the futur simple.",
            "I can resolve everyday errands at train stations, post offices, and shops in French.",
            "I can exchange or return a defective product in a store, explaining the problem clearly.",
            "I can invite friends, accept invitations gladly, and decline politely with excuses.",
            "I can share my opinion, agree, or disagree politely in a friendly conversation.",
            "I can handle basic phone calls, spell contact details, and leave structured voicemails."
        ],
        "sections": [
            {
                "title": "1. Spoken Production Audit (Monologue en continu)",
                "items": [
                    "Continuous speech flow: Can you speak continuously for 90 to 120 seconds on a familiar everyday topic?",
                    "Telling past stories: Can you recount a past event clearly using both passé composé and imparfait?",
                    "Future plans: Can you describe your future projects and career plans using the futur proche and futur simple?",
                    "Comparing things: Can you compare two cities, apartments, or jobs using plus... que and moins... que?"
                ]
            },
            {
                "title": "2. Spoken Interaction Audit (Dialogue & Role-Plays)",
                "items": [
                    "Shopping & services: Can you buy train tickets, order meals, and return items in stores without help?",
                    "Everyday opinions: Can you share your thoughts, agree, or disagree politely in a conversation?",
                    "Asking for clarification: Can you ask people to slow down or repeat when you don't understand?",
                    "Handling phone calls: Can you make an appointment or leave a voicemail message on the phone?"
                ]
            }
        ]
    }

    # Page 69: Final Self-Evaluation: Receptive & Written Skills
    pages[69] = {
        "page": 69,
        "type": "audit",
        "title": "Final Self-Evaluation: Receptive & Written Skills",
        "subtitle": "Checking Your Listening, Reading & Writing Skills",
        "badge_num": "68",
        "intro": "Evaluate your listening comprehension, reading skills, and ability to write practical messages.",
        "items": [
            "I can catch key information in airport and train station announcements.",
            "I can follow clear everyday conversations between French speakers at normal speed.",
            "I can understand short radio weather forecasts, news flashes, and cultural reports.",
            "I can read restaurant menus, rental listings, recipes, and store flyers easily.",
            "I can understand personal emails and invitations from French friends.",
            "I can write a 60 to 80-word friendly email or postcard describing a trip or weekend.",
            "I can write a short polite message to a hotel, school, or agency asking for info.",
            "I can write a 50 to 70-word review about a hotel, restaurant, or product online."
        ],
        "sections": [
            {
                "title": "1. Listening & Reading Audit",
                "items": [
                    "Public announcements: Can you understand essential details in airport and train station announcements?",
                    "Catching fast numbers: Can you catch prices, times, and phone numbers on the first or second listen?",
                    "Everyday reading: Can you read restaurant menus, rental listings, recipes, and store flyers easily?",
                    "Personal correspondence: Can you understand personal emails and invitations from French friends?"
                ]
            },
            {
                "title": "2. Written Production Audit",
                "items": [
                    "Personal emails & postcards: Can you write a 60 to 80-word message describing a trip or weekend?",
                    "Invitations & replies: Can you invite someone, accept an invitation, or decline with a polite excuse?",
                    "Formal inquiries: Can you write a short polite message to a hotel, school, or agency asking for info?",
                    "Online reviews: Can you write a 50 to 70-word review about a hotel, restaurant, or product?"
                ]
            }
        ]
    }

    # Page 70: Final Self-Evaluation: Grammar & Vocabulary Mastery
    pages[70] = {
        "page": 70,
        "type": "audit",
        "title": "Final Self-Evaluation: Grammar & Vocabulary Mastery",
        "subtitle": "Checking Your Core Grammar Rules and 1,500+ Words",
        "badge_num": "69",
        "intro": "Verify that you have mastered the core grammar rules and essential vocabulary of the CEFR A2 level.",
        "items": [
            "I can conjugate regular and irregular verbs in the passé composé using avoir and être.",
            "I know when to use the imparfait for descriptions and habits versus passé composé for events.",
            "I can express future projects using both futur proche and futur simple.",
            "I can use object pronouns (COD & COI) and adverbial pronouns (Y & En) accurately.",
            "I can compare items using comparatives (plus/moins/aussi... que) and superlatives.",
            "I can use negative words like ne... plus, ne... jamais, ne... rien, ne... personne.",
            "I have an active vocabulary of over 1,500 words across all core daily life themes.",
            "I routinely check adjective agreements, verb endings, and silent letters in my writing."
        ],
        "sections": [
            {
                "title": "1. Core Grammar Audit",
                "items": [
                    "Tenses & modes: Passé composé (avoir & être), Imparfait, Futur simple, and Conditionnel de politesse.",
                    "Pronouns: Direct (COD), Indirect (COI), Pronoun Y (places), Pronoun En (quantities), and Qui/Que.",
                    "Negation & adverbs: Ne... plus, ne... jamais, ne... rien, ne... personne, and adverbs in -ment.",
                    "Prepositions of time: Depuis (still continuing), Pendant (completed duration), Il y a (ago), and Dans (future)."
                ]
            },
            {
                "title": "2. Thematic Vocabulary Audit (1,500+ Words)",
                "items": [
                    "Everyday domains: Personal identity, housing, chores, food, shopping, transit, health, work, and media.",
                    "Describing sensations: Avoir faim, soif, chaud, froid, sommeil, peur, mal à la tête.",
                    "Conversation fillers & idioms: Alors, donc, en fait, ça marche, pas de souci, c'est pas grave.",
                    "Self-correction: Automatically checking adjective agreements, verb endings, and silent letters in writing."
                ]
            }
        ]
    }

    # Page 71: Final Milestone: Ready to Move to B1 Certification
    pages[71] = {
        "page": 71,
        "type": "audit",
        "title": "Final Milestone: Ready to Move to B1 Certification",
        "subtitle": "Congratulations! You Have Reached CEFR A2 Independence",
        "badge_num": "70",
        "intro": "Review your final checklist items to confirm you are completely ready to step into Intermediate French (B1).",
        "items": [
            "Functional independence: You can travel across French-speaking countries and handle daily situations on your own.",
            "Spontaneous conversation: You can chat with locals, express your feelings, and share your personal stories.",
            "Reading & writing fluency: You can read everyday documents and write clear, well-connected messages.",
            "Solid grammar foundation: You confidently distinguish between past, present, and future tenses.",
            "Ready to move to B1: You are fully prepared to begin your CEFR B1 intermediate journey!"
        ],
        "sections": [
            {
                "title": "1. Final Independence Check",
                "items": [
                    "Functional independence: You can travel across French-speaking countries and handle daily situations on your own.",
                    "Spontaneous conversation: You can chat with locals, express your feelings, and share your personal stories.",
                    "Reading & writing fluency: You can read everyday documents and write clear, well-connected messages.",
                    "Solid grammar foundation: You confidently distinguish between past, present, and future tenses."
                ]
            }
        ]
    }

    return pages

if __name__ == "__main__":
    pages = get_a2_data()
    print(f"Generated {len(pages)} pages.")
    with open("a2_curriculum_data.py", "w", encoding="utf-8") as f:
        f.write("# a2_curriculum_data.py - CEFR A2 Curriculum Dataset\n")
        f.write("# Refined, simple learner-friendly English with complete authentic French\n\n")
        f.write("A2_PAGES_DATA = ")
        # Write formatted dictionary
        import pprint
        f.write(pprint.pformat(pages, width=120, sort_dicts=False))
        f.write("\n")
    print("Successfully wrote a2_curriculum_data.py")
