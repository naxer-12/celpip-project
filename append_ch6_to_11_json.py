import json

with open("chapters_batch_1.json", "r", encoding="utf-8") as f:
    batch1 = json.load(f)

# CHAPTER 6
batch1["6"] = {
    "ch_num": 6,
    "title_fr": "Les sens et les émotions",
    "title_en": "The 5 Senses, Sensations & Emotions",
    "word_count": 40,
    "traps": [
        "AVOIR vs ÊTRE sensations trap: In French you 'HAVE' hunger, thirst, cold, heat, fear, sleepiness (J'ai faim, J'ai soif, J'ai froid, J'ai chaud, J'ai peur, J'ai sommeil) - never 'Je suis faim'!",
        "Silent final consonants in sensations: 'chaud' [shoh] (silent 'd'), 'froid' [frwah] (silent 'd').",
        "Emotional adjectives take ÊTRE: 'Je suis heureux / heureuse', 'Il est triste', 'Elle est en colère'."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'D' SILENCIEUX DE CHAUD ET FROID",
        "phonetic_tip_text": "Dans les sensations physiques, le 'd' final de 'chaud' [shoh] et 'froid' [frwah] ne se prononce JAMAIS, sauf en liaison rare. 'Faim' se prononce avec la nasale [fanh] et 'soif' avec la consonne sonore [swahf].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Sensations [4 pts]",
        "ex1_headers": ["Sensation / Émotion", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. J'ai chaud", "Consonne 'd'", "[  ] Oui", "[  ] Oui", "[ zhay shoh ]"],
            ["2. J'ai froid", "Consonne 'd'", "[  ] Oui", "[  ] Oui", "[ zhay frwah ]"],
            ["3. J'ai faim", "Voyelle nasale 'aim'", "[  ] Nasale [ɛ̃]", "[  ] Orale [am]", "[ zhay fanh ]"],
            ["4. J'ai soif", "Consonne 'f'", "[  ] Oui", "[  ] Oui", "[ zhay swahf ]"],
            ["5. heureux (m.)", "Consonne 'x'", "[  ] Oui", "[  ] Oui", "[ uh-ruh ]"],
            ["6. heureuse (f.)", "Consonne 's' voisée", "[  ] Oui [z]", "[  ] Non", "[ uh-ruhz ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Sensations [3 pts]",
        "ex2_items": [
            "a) le gout -> ________________________",
            "b) l'ouie -> ________________________",
            "c) en colere -> ________________________",
            "d) fatigue (f.) -> ________________________",
            "e) le sommeil -> ________________________",
            "f) la peur -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Émotions [3 pts]",
        "ex3_items": [
            "1. Il est amoureux     -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
            "2. Elle est heureuse   -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
            "3. Nous sommes tristes -> [  ] Liaison                 [  ] Pas de liaison",
            "4. Ils ont faim        -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "5. Vous avez peur      -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "6. J'ai sommeil        -> [  ] Liaison                 [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES 5 SENS ET ACCORD DES ÉMOTIONS",
        "gender_rule_text": "Les cinq sens : LA vue (f.), L'ouïe (f.), LE goût (m.), L'odorat (m.), LE toucher (m.). Les adjectifs d'émotion s'accordent avec le sujet : heureux/heureuse, surpris/surprise, fatigué/fatiguée.",
        "ex1_title": "Exercice 2.1 — Matrice des Cinq Sens & Organes Associés [6 pts]",
        "ex1_headers": ["Sens (Genre)", "Verbe d'action", "Organe associé", "Sens en anglais"],
        "ex1_rows": [
            ["1. La vue (f.)", "voir / regarder", "-> les yeux", "Sight / To see"],
            ["2. L'ouïe (f.)", "entendre / écouter", "-> les oreilles", "Hearing / To hear"],
            ["3. L'odorat (m.)", "sentir", "-> le nez", "Smell / To smell"],
            ["4. Le goût (m.)", "goûter", "-> la bouche / la langue", "Taste / To taste"],
            ["5. Le toucher (m.)", "toucher", "-> la main / les doigts", "Touch / To touch"],
            ["6. L'émotion (f.)", "ressentir", "-> le cœur", "Emotion / To feel"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre & Sensations : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Quand l'hiver arrive, je suis très froid dans ma chambre.\n   Correction : _____________________________________________________________________________",
            "2. Elle est très faim après sa longue journée de travail.\n   Correction : _____________________________________________________________________________",
            "3. Les deux sœurs sont très heureux d'être à Paris.\n   Correction : _____________________________________________________________________________",
            "4. Il n'aime pas le odeur du fromage fort.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS PHYSIQUES : LE VERBE AVOIR OBLIGATOIRE",
        "colloc_tip_text": "Ne dites jamais 'Je suis chaud' (qui a une connotation tout autre en français !) : dites toujours 'J'ai chaud'. Pour les émotions, utilisez ÊTRE : 'Je suis triste', 'Je suis content(e)'.",
        "ex1_title": "Exercice 3.1 — Discrimination Verbale (AVOIR vs ÊTRE) [5 pts]",
        "ex1_sentences": [
            "1. Il est midi passé et nous n'avons pas déjeuné ; nous ________ (avons / sommes) faim.",
            "2. Ferme la fenêtre s'il te plaît, j'________ (ai / suis) froid.",
            "3. Après dix kilomètres de marche, les randonneurs ________ (ont / sont) très fatigués.",
            "4. L'enfant pleure parce qu'il ________ (a / est) peur du noir.",
            "5. Bravo pour ton examen ! Nous ________ (avons / sommes) très contents pour toi."
        ],
        "ex2_title": "Exercice 3.2 — Paires Sensations & Remèdes Immédiats [5 pts]",
        "ex2_headers": ["Sensation physique", "Réaction appropriée", "Association"],
        "ex2_rows": [
            ["1. Avoir soif...", "A. mettre un pull chaud ou allumer le radiateur", "1 -> [    ]"],
            ["2. Avoir sommeil...", "B. manger un sandwich ou un fruit", "2 -> [    ]"],
            ["3. Avoir froid...", "C. boire un grand verre d'eau fraîche", "3 -> [    ]"],
            ["4. Avoir faim...", "D. aller se coucher et dormir", "4 -> [    ]"],
            ["5. Avoir chaud...", "E. ouvrir la fenêtre ou enlever sa veste", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE SITUATIONS ÉMOTIONNELLES",
        "cloze_tip_text": "Complétez avec les expressions de sensation et d'émotion adéquates sans confondre avoir et être.",
        "dialogues": [
            {
                "title": "Situation A — Rentrée de randonnée en montagne",
                "points": "3 pts",
                "lines": [
                    "• Marc : Ouf ! Quelle marche difficile ! J'ai très ___________________________ [thirsty]. Tu as de l'eau ?",
                    "• Julie : Oui, tiens. Moi, j'ai ___________________________ [hungry] ; je veux manger.",
                    "• Marc : En plus, le vent souffle, j'ai ___________________________ [cold]."
                ]
            },
            {
                "title": "Situation B — Annonce d'une bonne nouvelle",
                "points": "4 pts",
                "lines": [
                    "• Paul : J'ai réussi mon examen de français !",
                    "• Léa : Félicitations ! Je suis tellement ___________________________ [happy - f.] pour toi !",
                    "• Paul : Mes parents étaient très ___________________________ [surprised - m. pl.] et fiers.",
                    "• Léa : Tu n'es plus ___________________________ [stressed - m.] maintenant ?"
                ]
            },
            {
                "title": "Situation C — Fin de soirée entre amis",
                "points": "3 pts",
                "lines": [
                    "• Thomas : Il est minuit passé, je commence à avoir ___________________________ [sleepy].",
                    "• Sophie : Moi aussi, je suis très ___________________________ [tired - f.]. On rentre ?",
                    "• Thomas : Oui, bonne nuit !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. I am hungry and thirsty.", "-> __________________________________________________________________________________"],
            ["2. Are you cold? - No, I am hot.", "-> __________________________________________________________________________________"],
            ["3. She is very angry with her brother.", "-> __________________________________________________________________________________"],
            ["4. The little boy is afraid of dogs.", "-> __________________________________________________________________________________"],
            ["5. We are very tired after the trip.", "-> __________________________________________________________________________________"],
            ["6. Why are you sad today? (informal with 'tu')", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. J'ai faim  •  J'ai soif  •  J'ai froid  •  Je suis grand",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La vue  •  L'ouïe  •  L'odorat  •  Le genou",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Heureux  •  Content  •  Joyeux  •  En colère",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Le goût  •  Le toucher  •  Le sommeil  •  La vue",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. chaud -> 'd' muet [shoh] | 2. froid -> 'd' muet [frwah] | 3. faim -> nasale [ɛ̃] [fanh] | 4. soif -> 'f' prononcé [swahf] | 5. heureux -> 'x' muet [uh-ruh] | 6. heureuse -> 's' voisée sonore [z] [uh-ruhz].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le goût (circonflexe sur 'û') | b) l'ouïe (tréma sur 'ï') | c) en colère (accent grave sur 'è') | d) fatiguée | e) le sommeil | f) la peur.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. Il est amoureux -> Liaison en [t] obligatoire | 2. Elle est heureuse -> Liaison en [t] | 3. Nous sommes tristes -> Pas de liaison | 4. Ils ont faim -> Liaison en [z] | 5. Vous avez peur -> Liaison en [z] | 6. J'ai sommeil -> Pas de liaison.",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. La vue | 2. L'ouïe | 3. L'odorat | 4. Le goût | 5. Le toucher | 6. L'émotion.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'J'AI très froid' (avoir froid, pas être froid).\n2. 'Elle A très faim' (avoir faim, pas être faim).\n3. 'très HEUREUSES' (deux sœurs = féminin pluriel : heureuses).\n4. 'L'ODEUR' (élision obligatoire : l'odeur).",
        "tier3_text": "Exercice 3.1 — Verbes [5 pts] :\n1. avons faim | 2. j'ai froid | 3. sont fatigués | 4. a peur | 5. sommes contents.\n\nExercice 3.2 — Paires Sensations [5 pts] :\n1 -> C (Avoir soif -> boire de l'eau) | 2 -> D (Avoir sommeil -> dormir) | 3 -> A (Avoir froid -> mettre un pull) | 4 -> B (Avoir faim -> manger) | 5 -> E (Avoir chaud -> ouvrir la fenêtre).",
        "tier4_text": "Situation A (3 pts) : soif | faim | froid.\nSituation B (4 pts) : heureuse | surpris | stressé.\nSituation C (3 pts) : sommeil | fatiguée.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. J'ai faim et soif.\n2. Tu as froid ? - Non, j'ai chaud.\n3. Elle est très en colère contre son frère.\n4. Le petit garçon a peur des chiens.\n5. Nous sommes très fatigués après le voyage.\n6. Pourquoi es-tu triste aujourd'hui ?\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Je suis grand (description physique avec être, les 3 autres sont des sensations physiologiques avec avoir).\n2. Le genou (articulation de la jambe, les 3 autres sont les 5 sens humains).\n3. En colère (émotion de frustration/fureur négative, les 3 autres sont des sentiments de joie positive).\n4. Le sommeil (état physiologique de repos, les 3 autres sont les cinq sens de la perception).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 6",
        "anchors_text": "1. L'inversion AVOIR / ÊTRE : Retenez que le français considère la faim, la soif, le froid et le chaud comme des éléments physiques que l'on POSSÈDE : 'J'ai faim', 'J'ai froid'.\n2. Le piège de 'Je suis chaud' : En français, dire 'Je suis chaud' ne signifie JAMAIS 'I feel hot' ! Cela signifie soit 'I'm ready/up for it' en argot, soit a une connotation suggestive. Pour la température corporelle, dites TOUJOURS 'J'ai chaud' !\n3. Les terminaisons en -eux / -euse : Heureux -> heureuse, peureux -> peureuse, curieux -> curieuse."
    }
}

# CHAPTER 7
batch1["7"] = {
    "ch_num": 7,
    "title_fr": "La famille et le couple",
    "title_en": "The Family Tree, Relatives & Marital Status",
    "word_count": 44,
    "traps": [
        "Pronunciation trap of 'fils' [feess]: the final 's' IS PRONOUNCED, while 'l' is completely silent! 'Fille' [feey] means daughter or girl.",
        "Possessive adjectives agreement: 'mon/ton/son' used before FEMININE singular nouns starting with a vowel: 'mon amie', 'son épouse'.",
        "Marital status: célibataire (single), marié(e), divorcé(e), pacsé(e) (civil union under French law PACS)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE PIÈGE HISTORIQUE DU MOT 'FILS' ET 'SŒUR'",
        "phonetic_tip_text": "Le mot 'fils' se prononce [feess] : le 'l' est muet et le 's' est sonné ! 'Sœur' utilise la voyelle ouverte [suhr] avec la ligature 'œ'. 'Père' [pair] et 'mère' [mair] ont un accent grave ouvert.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Noms de Famille [4 pts]",
        "ex1_headers": ["Membre de la famille", "Piège de prononciation", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le fils (m.)", "Consonne 's' finale", "[  ] Oui [s]", "[  ] Non", "[ feess ]"],
            ["2. la fille (f.)", "Digraphe 'ille'", "[  ] [feey]", "[  ] [feel]", "[ feey ]"],
            ["3. la sœur (f.)", "Ligature 'œu'", "[  ] [suhr]", "[  ] [sohr]", "[ suhr ]"],
            ["4. le grand-père (m.)", "Consonne 'd'", "[  ] Oui", "[  ] Oui", "[ grahn-pair ]"],
            ["5. les parents (pl.)", "Consonne 'ts'", "[  ] Oui", "[  ] Oui", "[ pah-rahn ]"],
            ["6. l'oncle (m.)", "Voyelle nasale 'on'", "[  ] Nasale [ɔ̃]", "[  ] Orale [on]", "[ ohn-kl ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique de la Famille [3 pts]",
        "ex2_items": [
            "a) le pere -> ________________________",
            "b) la mere -> ________________________",
            "c) le grand-pere -> ________________________",
            "d) la soeur -> ________________________",
            "e) celibataire -> ________________________",
            "f) marie (f.) -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Adjectifs Possessifs [3 pts]",
        "ex3_items": [
            "1. mon enfant       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. son oncle        -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "3. mes parents      -> [  ] Liaison                    [  ] Pas de liaison",
            "4. ses enfants      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "5. nos grands-parents -> [  ] Liaison                  [  ] Pas de liaison",
            "6. leurs amis       -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "BINÔMES DE PARENTÉ ET ADJECTIFS POSSESSIFS",
        "gender_rule_text": "Les couples de parenté s'apprennent en binômes indissociables : le père / la mère, le fils / la fille, le frère / la sœur, l'oncle / la tante, le cousin / la cousine, le grand-père / la grand-mère.",
        "ex1_title": "Exercice 2.1 — Matrice des Paires Masculin / Féminin de la Famille [6 pts]",
        "ex1_headers": ["Masculin (Donné)", "Féminin correspondant", "Possessif (Mon / Ma)", "Sens anglais"],
        "ex1_rows": [
            ["1. Le père", "-> ___________________", "Mon père / Ma mère", "Father / Mother"],
            ["2. Le fils", "-> ___________________", "Mon fils / Ma fille", "Son / Daughter"],
            ["3. Le frère", "-> ___________________", "Mon frère / Ma sœur", "Brother / Sister"],
            ["4. L'oncle", "-> ___________________", "Mon oncle / Ma tante", "Uncle / Aunt"],
            ["5. Le grand-père", "-> ___________________", "Mon grand-père / Ma grand-mère", "Grandfather / Grandmother"],
            ["6. Le mari / époux", "-> ___________________", "Mon mari / Ma femme", "Husband / Wife"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre & Possessifs : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Voici ma épouse Claire, nous sommes mariés depuis cinq ans.\n   Correction : _____________________________________________________________________________",
            "2. Mon sœur habite à Lyon avec ses deux enfants.\n   Correction : _____________________________________________________________________________",
            "3. Antoine a présenté sa nouveau petit amie à ses parents.\n   Correction : _____________________________________________________________________________",
            "4. Le grand-mère de Lucas prépare de très bons gâteaux.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE STATUT CIVIL ET DE PARENTÉ",
        "colloc_tip_text": "Statut civil en France : être célibataire, être marié(e), être divorcé(e), être pacsé(e) (Pacte Civil de Solidarité). Nicknames affectifs : papa, maman, papi, mamie, tonton, tata.",
        "ex1_title": "Exercice 3.1 — Formules de Situation Matrimoniale [5 pts]",
        "ex1_sentences": [
            "1. Marc vit seul et n'est pas en couple ; il est _________ (célibataire).",
            "2. Sophie et Pierre ont signé un contrat civil à la mairie ; ils sont _________ (pacsés).",
            "3. Après dix ans de mariage, ils se sont séparés légalement ; ils sont _________ (divorcés).",
            "4. Mes grands-parents ont fêté leurs 50 ans de _________ (mariage).",
            "5. Elle a rencontré son nouveau petit _________ (ami / copain) à l'université."
        ],
        "ex2_title": "Exercice 3.2 — Paires Arbre Généalogique & Définitions [5 pts]",
        "ex2_headers": ["Lien de parenté", "Définition généalogique", "Association"],
        "ex2_rows": [
            ["1. La tante...", "A. le frère de mon père ou de ma mère", "1 -> [    ]"],
            ["2. Le cousin...", "B. la mère de mon père ou de ma mère", "2 -> [    ]"],
            ["3. L'oncle...", "C. la sœur de mon père ou de ma mère", "3 -> [    ]"],
            ["4. La grand-mère...", "D. le fils de mon oncle ou de ma tante", "4 -> [    ]"],
            ["5. Le neveu...", "E. le fils de mon frère ou de ma sœur", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE PRÉSENTATION DE LA FAMILLE",
        "cloze_tip_text": "Complétez la description de la famille en accordant les possessifs et les adjectifs de parenté.",
        "dialogues": [
            {
                "title": "Situation A — Album photo de famille",
                "points": "3 pts",
                "lines": [
                    "• Nicolas : Qui est sur cette photo ?",
                    "• Émilie : C'est mon ___________________________ [grandfather] et ma ___________________________ [grandmother].",
                    "• Nicolas : Et le petit garçon à côté ?",
                    "• Émilie : C'est mon petit ___________________________ [brother], Léo."
                ]
            },
            {
                "title": "Situation B — Présentation du conjoint à un dîner",
                "points": "4 pts",
                "lines": [
                    "• Julien : Je te présente mon ___________________________ [wife], Chloé.",
                    "• Chloé : Enchantée, Julien ! Vous êtes ___________________________ [married - m. pl.] depuis longtemps ?",
                    "• Julien : Oui, et nous avons deux ___________________________ [children] : un ___________________________ [son] et une fille."
                ]
            },
            {
                "title": "Situation C — Discussion sur la situation familiale",
                "points": "3 pts",
                "lines": [
                    "• Antoine : Tu as des frères et ___________________________ [sisters] ?",
                    "• Sarah : Non, je suis fille ___________________________ [only child - f. : unique]. Et toi ?",
                    "• Antoine : J'ai un frère aîné, il est ___________________________ [single - m.]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. My parents live in a big house in Bordeaux.", "-> __________________________________________________________________________________"],
            ["2. He has two brothers and one sister.", "-> __________________________________________________________________________________"],
            ["3. Are you married or single? (formal with 'vous')", "-> __________________________________________________________________________________"],
            ["4. My uncle is the brother of my mother.", "-> __________________________________________________________________________________"],
            ["5. Her son is eight years old and her daughter is four.", "-> __________________________________________________________________________________"],
            ["6. We are celebrating my grandfather's birthday.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Le père  •  La mère  •  Le fils  •  Le voisin",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Marié  •  Célibataire  •  Divorcé  •  Gentil",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La tante  •  L'oncle  •  Le cousin  •  La voiture",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Mon père  •  Sa mère  •  Mes cousins  •  Un train",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. fils -> 's' prononcé [feess], 'l' muet ! | 2. fille -> [feey] liquide | 3. sœur -> ligature 'œ' [suhr] | 4. grand-père -> 'd' muet [grahn-pair] | 5. parents -> 'ts' muets [pah-rahn] | 6. oncle -> nasale [ohn-kl].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le père | b) la mère | c) le grand-père | d) la sœur (ligature œu) | e) célibataire | f) mariée.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. mon enfant -> Liaison en [n] obligatoire [mɔ̃.nɑ̃.fɑ̃] | 2. son oncle -> Liaison en [n] [sɔ̃.nɔ̃.kl] | 3. mes parents -> Pas de liaison devant consonne | 4. ses enfants -> Liaison en [z] [se.zɑ̃.fɑ̃] | 5. nos grands-parents -> Pas de liaison | 6. leurs amis -> Liaison en [z] [lœ.ʁza.mi].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. La mère | 2. La fille | 3. La sœur | 4. La tante | 5. La grand-mère | 6. La femme (ou l'épouse).\n\nExercice 2.2 — Détective [4 pts] :\n1. 'MON épouse' (devant voyelle, 'mon' remplace 'ma' pour éviter le choc vocalique : mon épouse).\n2. 'MA sœur' (sœur est féminin : ma sœur).\n3. 'sa NOUVELLE petite amie' (accords féminins nécessaires).\n4. 'LA grand-mère' (grand-mère est féminin : la grand-mère).",
        "tier3_text": "Exercice 3.1 — Formules Matrimoniales [5 pts] :\n1. célibataire | 2. pacsés | 3. divorcés | 4. mariage | 5. ami (ou copain).\n\nExercice 3.2 — Paires Famille [5 pts] :\n1 -> C (La tante = la sœur du père/mère) | 2 -> D (Le cousin = fils de l'oncle/tante) | 3 -> A (L'oncle = frère du père/mère) | 4 -> B (La grand-mère = mère du père/mère) | 5 -> E (Le neveu = fils du frère/sœur).",
        "tier4_text": "Situation A (3 pts) : grand-père | grand-mère | frère.\nSituation B (4 pts) : femme (ou épouse) | mariés | enfants | fils.\nSituation C (3 pts) : sœurs | unique | célibataire.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Mes parents habitent dans une grande maison à Bordeaux.\n2. Il a deux frères et une sœur.\n3. Vous êtes marié ou célibataire ?\n4. Mon oncle est le frère de ma mère.\n5. Son fils a huit ans et sa fille a quatre ans.\n6. Nous fêtons l'anniversaire de mon grand-père.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Le voisin (personne extérieure au foyer, les 3 autres sont des membres de la famille nucléaire direct).\n2. Gentil (trait de caractère moral, les 3 autres sont des statuts matrimoniaux civils légaux).\n3. La voiture (moyen de transport mécanique, les 3 autres sont des membres de la famille élargie).\n4. Un train (nom avec article indéfini sans lien familial, les 3 autres combinent adjectif possessif et parent).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 7",
        "anchors_text": "1. Le cas unique de 'fils' : Le mot 'fils' est l'une des rares exceptions où le 's' final est prononcé et le 'l' est totalement silencieux [feess].\n2. Le choc vocalique du possessif : Devant tout nom féminin commençant par une voyelle ou un 'h' muet, 'ma/ta/sa' se transforme en 'mon/ton/son' (mon amie, mon épouse, son histoire).\n3. Le PACS : Institution juridique française créée en 1999 (Pacte Civil de Solidarité), le statut de 'pacsé' est extrêmement courant dans les formulaires administratifs."
    }
}

# CHAPTER 8
batch1["8"] = {
    "ch_num": 8,
    "title_fr": "Les activités sportives",
    "title_en": "Sports Disciplines, Equipment & Facilities",
    "word_count": 38,
    "traps": [
        "The Golden Sports Rule: JOUER À (au, à la, aux) for team sports and ball games (jouer au foot, jouer au tennis). FAIRE DE (du, de la, des) for individual sports, athletics, cycling, fitness (faire du vélo, faire de la natation).",
        "Silent final consonants: 'foot' [foot], 'tennis' [tay-nees] (final 's' sounded!), 'ski' [skee], 'stade' [stahd].",
        "Sports facilities: la piscine (swimming pool), le stade (stadium), le gymnase (gym), le court de tennis (tennis court), la patinoire (ice rink)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "PRONONCIATION DES ANGLICISMES SPORTIFS",
        "phonetic_tip_text": "Les sports empruntés à l'anglais s'adaptent : le football [foot-bahl] (ou le foot), le basket-ball [bahs-ket], le tennis [tay-nees] (le 's' final est prononcé !). La natation [nah-tah-syohn] a le son nasal [ɔ̃].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Noms de Sports [4 pts]",
        "ex1_headers": ["Discipline sportive", "Phénomène phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le tennis (m.)", "Consonne 's' finale", "[  ] Oui [s]", "[  ] Non", "[ tay-nees ]"],
            ["2. le football (m.)", "Anglicisme 'foot'", "[  ] [foot]", "[  ] [foh-oh]", "[ foot ]"],
            ["3. le ski (m.)", "Voyelle finale 'i'", "[  ] [skee]", "[  ] [sky]", "[ skee ]"],
            ["4. le cyclisme (m.)", "Suffixe '-isme'", "[  ] [see-kleezm]", "[  ] [sy-kleezm]", "[ see-kleezm ]"],
            ["5. la natation (f.)", "Suffixe '-tion'", "[  ] [nah-tah-syohn]", "[  ] [syuhn]", "[ nah-tah-syohn ]"],
            ["6. la course (f.)", "Consonne 'r' uvulaire", "[  ] Oui [ʁ]", "[  ] Non", "[ koors ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Sports [3 pts]",
        "ex2_items": [
            "a) le velo -> ________________________",
            "b) le gymnase -> ________________________",
            "c) l'equitation -> ________________________",
            "d) l'athletisme -> ________________________",
            "e) la petanque -> ________________________",
            "f) la randonnee -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Activités Sportives [3 pts]",
        "ex3_items": [
            "1. faire de l'équitation -> [  ] Élision obligatoire    [  ] Pas d'élision",
            "2. jouer aux cartes      -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "3. aux échecs            -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "4. un match de tennis    -> [  ] Liaison                 [  ] Pas de liaison",
            "5. deux équipes          -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "6. faire du ski          -> [  ] Liaison                 [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES DISCIPLINES SPORTIVES ET DE LEURS LIEUX",
        "gender_rule_text": "La majorité des sports de balle sont MASCULINS : le football, le tennis, le basket, le rugby, le golf. Les activités se terminant par '-tion' ou '-ée' sont FÉMININES : la natation, l'équitation, la randonnée.",
        "ex1_title": "Exercice 2.1 — Matrice des Disciplines, Formules et Lieux [6 pts]",
        "ex1_headers": ["Discipline (Genre)", "Verbe + Préposition", "Lieu où on pratique", "Sens anglais"],
        "ex1_rows": [
            ["1. Football (m.)", "-> jouer au foot", "le stade", "Soccer / Stadium"],
            ["2. Natation (f.)", "-> faire de la natation", "la piscine", "Swimming / Pool"],
            ["3. Tennis (m.)", "-> jouer au tennis", "le court de tennis", "Tennis / Tennis court"],
            ["4. Vélo / Cyclisme (m.)", "-> faire du vélo", "la route / piste cyclable", "Biking / Bike lane"],
            ["5. Basket-ball (m.)", "-> jouer au basket", "le gymnase", "Basketball / Gym"],
            ["6. Ski (m.)", "-> faire du ski", "la montagne / les pistes", "Skiing / Mountain slopes"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Le week-end, j'adore jouer du football avec mes collègues.\n   Correction : _____________________________________________________________________________",
            "2. Elle va à le piscine tous les mardis soirs.\n   Correction : _____________________________________________________________________________",
            "3. Mon frère fait au vélo sur la piste cyclable.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons réservé un terrain dans la grand gymnase.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "LA RÈGLE D'OR : JOUER À VS FAIRE DE",
        "colloc_tip_text": "JOUER À (au, à la, aux) s'emploie UNIQUEMENT pour les sports collectifs, jeux avec balle ou jeux de société (jouer au foot, jouer aux échecs). FAIRE DE (du, de la, de l', des) s'emploie pour les sports individuels et l'effort physique (faire du vélo, faire de la musculation).",
        "ex1_title": "Exercice 3.1 — Discrimination Verbale (JOUER AU vs FAIRE DU) [5 pts]",
        "ex1_sentences": [
            "1. Mon fils ________ (joue au / fait du) rugby dans le club municipal.",
            "2. Pour garder la forme, elle ________ (joue à la / fait de la) natation.",
            "3. Tous les dimanches matin, nous ________ (jouons au / faisons du) vélo.",
            "4. Est-ce que tu ________ (joues au / fais du) tennis avec Marc ce soir ?",
            "5. En hiver, ils partent dans les Alpes pour ________ (jouer au / faire du) ski."
        ],
        "ex2_title": "Exercice 3.2 — Paires Disciplines & Équipements [5 pts]",
        "ex2_headers": ["Sport", "Équipement indispensable", "Association"],
        "ex2_rows": [
            ["1. Le tennis...", "A. le maillot de bain et les lunettes", "1 -> [    ]"],
            ["2. Le football...", "B. le ballon rond et les crampons", "2 -> [    ]"],
            ["3. Le cyclisme...", "C. la raquette et la balle jaune", "3 -> [    ]"],
            ["4. La natation...", "D. le casque et la bicyclette", "4 -> [    ]"],
            ["5. Le ski...", "E. les bâtons, les skis et les chaussures", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE D'ACTIVITÉS SPORTIVES",
        "cloze_tip_text": "Complétez les conversations sportives en appliquant rigoureusement les prépositions contractées.",
        "dialogues": [
            {
                "title": "Situation A — Organisation du week-end sportif",
                "points": "3 pts",
                "lines": [
                    "• Lucas : Tu veux faire du sport samedi ?",
                    "• Thomas : Oui, avec plaisir ! Tu préfères ___________________________ [play tennis] ou ___________________________ [go biking] ?",
                    "• Lucas : Je préfère aller à la ___________________________ [swimming pool] pour nager."
                ]
            },
            {
                "title": "Situation B — Inscription au club de sport",
                "points": "4 pts",
                "lines": [
                    "• La secrétaire : Bonjour. Quelles activités souhaitez-vous pratiquer ?",
                    "• Julie : Je voudrais faire de la ___________________________ [running / jogging] et jouer au ___________________________ [basketball].",
                    "• La secrétaire : Très bien. Les entraînements ont lieu au ___________________________ [gymnasium]. N'oubliez pas vos baskets de ___________________________ [sport]."
                ]
            },
            {
                "title": "Situation C — Discussion sur les vacances à la montagne",
                "points": "3 pts",
                "lines": [
                    "• Marc : Vous partez à la montagne cet hiver ?",
                    "• Sophie : Oui, pour faire du ___________________________ [skiing]. Les enfants adorent dévaler les ___________________________ [slopes / pistes].",
                    "• Marc : C'est génial, profitez bien de la neige !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. I play soccer with my friends on Saturdays.", "-> __________________________________________________________________________________"],
            ["2. She swims twice a week at the pool.", "-> __________________________________________________________________________________"],
            ["3. We do cycling in the forest every Sunday.", "-> __________________________________________________________________________________"],
            ["4. Do you play tennis or basketball? (informal with 'tu')", "-> __________________________________________________________________________________"],
            ["5. They go skiing in the Alps in February.", "-> __________________________________________________________________________________"],
            ["6. Where is the gymnasium, please?", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Le football  •  Le basket  •  Le tennis  •  La natation",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Jouer au foot  •  Jouer au tennis  •  Jouer au basket  •  Jouer au vélo",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le stade  •  Le gymnase  •  La piscine  •  Le restaurant",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La raquette  •  La balle  •  Le ballon  •  Le roman",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. tennis -> 's' prononcé [tay-nees] | 2. foot -> [foot] | 3. ski -> [skee] | 4. cyclisme -> [see-kleezm] | 5. natation -> [nah-tah-syohn] | 6. course -> 'r' articulé [koors].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le vélo (accent aigu) | b) le gymnase | c) l'équitation (accent aigu) | d) l'athlétisme (accent aigu) | e) la pétanque (accent aigu) | f) la randonnée (deux 'e').\n\nExercice 1.3 — Liaisons [3 pts] :\n1. faire de l'équitation -> Élision obligatoire devant voyelle [də.le.ki.ta.sjɔ̃] | 2. jouer aux cartes -> Pas de liaison | 3. aux échecs -> Liaison en [z] [o.ze.ʃɛk] | 4. un match de tennis -> Pas de liaison | 5. deux équipes -> Liaison en [z] [dø.ze.kip] | 6. faire du ski -> Pas de liaison.",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. jouer au foot / le stade | 2. faire de la natation / la piscine | 3. jouer au tennis / le court | 4. faire du vélo / la piste cyclable | 5. jouer au basket / le gymnase | 6. faire du ski / la montagne.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'JOUER AU football' (sport collectif de ballon avec jouer à, pas jouer de).\n2. 'À LA piscine' (piscine est féminin : à la piscine).\n3. 'FAIT DU vélo' (cyclisme = sport individuel avec faire de, pas jouer à).\n4. 'LE grand gymnase' (gymnase est masculin : le grand gymnase).",
        "tier3_text": "Exercice 3.1 — Discrimination [5 pts] :\n1. joue au rugby | 2. fait de la natation | 3. faisons du vélo | 4. joues au tennis | 5. faire du ski.\n\nExercice 3.2 — Paires Équipements [5 pts] :\n1 -> C (Tennis -> raquette et balle jaune) | 2 -> B (Football -> ballon rond et crampons) | 3 -> D (Cyclisme -> casque et bicyclette) | 4 -> A (Natation -> maillot de bain et lunettes) | 5 -> E (Ski -> bâtons, skis et chaussures).",
        "tier4_text": "Situation A (3 pts) : jouer au tennis | faire du vélo | piscine.\nSituation B (4 pts) : course à pied (ou course) | basket (ou basket-ball) | gymnase | sport.\nSituation C (3 pts) : ski | pistes.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je joue au football avec mes amis le samedi.\n2. Elle fait de la natation deux fois par semaine à la piscine.\n3. Nous faisons du vélo dans la forêt tous les dimanches.\n4. Tu joues au tennis ou au basket ?\n5. Ils font du ski dans les Alpes en février.\n6. Où est le gymnase, s'il vous plaît ?\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. La natation (sport individuel aquatique utilisant 'faire de la', les 3 autres sont des sports de balle avec 'jouer au').\n2. Jouer au vélo (expression grammaticalement fausse, on dit 'faire du vélo', le vélo n'est pas un jeu de balle).\n3. Le restaurant (lieu de restauration gastronomique, les 3 autres sont des infrastructures sportives municipales).\n4. Le roman (livre de lecture littéraire, les 3 autres sont des pièces d'équipement de jeux de balle/raquette).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 8",
        "anchors_text": "1. La règle d'or Jouer vs Faire : Jouer À + sport collectif ou sport de balle (au foot, au tennis, au basket). Faire DE + sport individuel, endurance ou fitness (du vélo, de la natation, du ski, de la gymnastique).\n2. Le court de tennis : En français, le terrain de tennis s'appelle spécifiquement 'un court de tennis' (orthographe avec un 't'), tandis que le terrain de football s'appelle 'un terrain' ou 'une pelouse'.\n3. Les contractions d'articles : à + le = AU (jouer au foot) ; de + le = DU (faire du vélo) ; de + la = DE LA (faire de la natation)."
    }
}

# CHAPTER 9
batch1["9"] = {
    "ch_num": 9,
    "title_fr": "Les activités culturelles",
    "title_en": "Music, Cinema, Theatre & Cultural Arts",
    "word_count": 42,
    "traps": [
        "Playing an instrument uses JOUER DE (de + le = du, de + la = de la): 'jouer du piano', 'jouer de la guitare' - completely different from playing a sport (jouer au foot)!",
        "Cinema terms: 'un film', 'une séance' (screening/showtime), 'une place de cinéma / un billet', 'un acteur / une actrice'.",
        "Silent consonants in culture: 'concert' [kohn-sair] (silent 't'), 'billet' [bee-yay] (silent 't'), 'théâtre' [tay-ahtr]."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'T' FINAL SILENCIEUX DE CONCERT ET BILLET",
        "phonetic_tip_text": "Dans le monde culturel : 'un concert' [kohn-sair] a un 't' muet silencieux. 'Un billet' [bee-yay] a 'et' prononcé [e] avec 't' muet. 'Théâtre' se prononce [tay-ahtr] avec un son 't' franc (pas de 'th' anglais !).",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Termes Culturels [4 pts]",
        "ex1_headers": ["Terme culturel", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. un concert (m.)", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ kohn-sair ]"],
            ["2. un billet (m.)", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ bee-yay ]"],
            ["3. le théâtre (m.)", "Digraphe 'th'", "[  ] [t] franc", "[  ] [th] anglais", "[ tay-ahtr ]"],
            ["4. le violon (m.)", "Voyelle nasale 'on'", "[  ] Nasale [ɔ̃]", "[  ] Orale [on]", "[ vyoh-lohn ]"],
            ["5. la guitare (f.)", "Consonne 'g' dure", "[  ] [gee-tahr]", "[  ] [zhee-tahr]", "[ gee-tahr ]"],
            ["6. une comédie (f.)", "Accent aigu 'é'", "[  ] [ay] fermé", "[  ] [eh] ouvert", "[ koh-may-dee ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Mots Culturels [3 pts]",
        "ex2_items": [
            "a) le theatre -> ________________________",
            "b) le cinema -> ________________________",
            "c) la flute -> ________________________",
            "d) une seance -> ________________________",
            "e) une comedie -> ________________________",
            "f) un chanteur -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Événements Culturels [3 pts]",
        "ex3_items": [
            "1. un acteur       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. un grand artiste -> [  ] Liaison [t] obligatoire   [  ] Pas de liaison",
            "3. deux billets     -> [  ] Liaison                   [  ] Pas de liaison",
            "4. aller au concert -> [  ] Liaison                   [  ] Pas de liaison",
            "5. aux artistes     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un opéra         -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES INSTRUMENTS ET SPECTACLES",
        "gender_rule_text": "Les instruments : LE piano, LE violon, LE saxophone ; LA guitare, LA flûte, LA batterie. Les spectacles : LE concert, LE film, LE spectacle ; LA pièce de théâtre, LA séance, LA chanson.",
        "ex1_title": "Exercice 2.1 — Matrice des Instruments & Formule 'Jouer DE' [6 pts]",
        "ex1_headers": ["Instrument (Genre)", "Formule avec Jouer DE", "Musicien(ne)", "Sens anglais"],
        "ex1_rows": [
            ["1. Piano (m.)", "-> jouer du piano", "le/la pianiste", "Piano / Pianist"],
            ["2. Guitare (f.)", "-> jouer de la guitare", "le/la guitariste", "Guitar / Guitarist"],
            ["3. Violon (m.)", "-> jouer du violon", "le/la violoniste", "Violin / Violinist"],
            ["4. Batterie (f.)", "-> jouer de la batterie", "le/la batteur(-euse)", "Drums / Drummer"],
            ["5. Flûte (f.)", "-> jouer de la flûte", "le/la flûtiste", "Flute / Flutist"],
            ["6. Saxophone (m.)", "-> jouer du saxophone", "le/la saxophoniste", "Saxophone / Saxophonist"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Mon frère adore jouer au piano tous les soirs.\n   Correction : _____________________________________________________________________________",
            "2. Nous avons acheté deux places pour le pièce de théâtre.\n   Correction : _____________________________________________________________________________",
            "3. À quelle heure commence le prochain séance de cinéma ?\n   Correction : _____________________________________________________________________________",
            "4. Elle écoute un nouvelle chanson française à la radio.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "LA DIFFÉRENCE CRUCIALE : JOUER DU PIANO VS JOUER AU FOOT",
        "colloc_tip_text": "Retenez cette règle fondamentale : JOUER + À = SPORTS & JEUX (jouer au foot). JOUER + DE = INSTRUMENTS DE MUSIQUE (jouer du piano, jouer de la guitare). Pour les sorties : aller au concert, aller au cinéma.",
        "ex1_title": "Exercice 3.1 — Prépositions Musicales (DU vs DE LA vs AU) [5 pts]",
        "ex1_sentences": [
            "1. Claire a appris la musique au conservatoire ; elle joue ________ (du / au) violon.",
            "2. Dans son groupe de rock, Maxime joue ________ (de la / à la) batterie.",
            "3. Thomas n'aime pas le sport ; il préfère jouer ________ (du / au) piano plutôt que jouer ________ (du / au) football.",
            "4. Sophie prend des cours chaque semaine pour jouer ________ (de la / du) guitare classique.",
            "5. Samedi soir, nous allons tous ensemble ________ (au / en) concert de jazz."
        ],
        "ex2_title": "Exercice 3.2 — Paires Genres Culturels & Définitions [5 pts]",
        "ex2_headers": ["Genre culturel", "Définition / Exemple", "Association"],
        "ex2_rows": [
            ["1. Une comédie...", "A. spectacle où les comédiens jouent sur scène", "1 -> [    ]"],
            ["2. Un film d'action...", "B. film léger destiné à faire rire les spectateurs", "2 -> [    ]"],
            ["3. Une pièce de théâtre...", "C. film dynamique avec cascades et aventures", "3 -> [    ]"],
            ["4. Un concert...", "D. représentation musicale d'un chanteur ou orchestre", "4 -> [    ]"],
            ["5. Un musée...", "E. lieu d'exposition d'œuvres d'art et de sculptures", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE SORTIE CULTURELLE COMMUNICATIVE",
        "cloze_tip_text": "Complétez les dialogues d'achat de billets et de sortie au cinéma en récupérant directement les termes exacts.",
        "dialogues": [
            {
                "title": "Situation A — Au guichet du cinéma de quartier",
                "points": "3 pts",
                "lines": [
                    "• L'employé : Bonjour. Pour quel ___________________________ [movie / film] désirez-vous des places ?",
                    "• Marc : Bonjour. Deux billets pour la ___________________________ [screening / showtime] de 20 heures, s'il vous plaît.",
                    "• L'employé : Ce sera en salle numéro 3. Bonne ___________________________ [screening / viewing] !"
                ]
            },
            {
                "title": "Situation B — Discussion sur les talents musicaux",
                "points": "4 pts",
                "lines": [
                    "• Julie : Tu joues d'un ___________________________ [instrument] de musique ?",
                    "• Lucas : Oui, je joue de la ___________________________ [guitar] depuis cinq ans, et mon frère joue du ___________________________ [piano].",
                    "• Julie : Vous avez un groupe ?",
                    "• Lucas : Oui, nous répétons pour faire un ___________________________ [concert] le mois prochain."
                ]
            },
            {
                "title": "Situation C — Proposition de sortie culturelle le week-end",
                "points": "3 pts",
                "lines": [
                    "• Antoine : Tu as envie d'aller au ___________________________ [theatre] samedi soir ?",
                    "• Sophie : C'est quelle ___________________________ [play - pièce de...] ?",
                    "• Antoine : C'est une ___________________________ [comedy] très amusante de Molière."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. She plays the guitar very well.", "-> __________________________________________________________________________________"],
            ["2. I would like two tickets for the concert, please.", "-> __________________________________________________________________________________"],
            ["3. What time does the movie screening start?", "-> __________________________________________________________________________________"],
            ["4. We are going to the theatre to see a play.", "-> __________________________________________________________________________________"],
            ["5. He is a very famous actor in France.", "-> __________________________________________________________________________________"],
            ["6. Do you play the piano? (informal with 'tu')", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Le piano  •  La guitare  •  Le violon  •  Le football",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Jouer du piano  •  Jouer de la guitare  •  Jouer du violon  •  Jouer au tennis",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le cinéma  •  Le théâtre  •  La salle de concert  •  L'hôpital",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Une comédie  •  Un film policier  •  Un film d'action  •  Une fourchette",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. concert -> 't' muet [kohn-sair] | 2. billet -> 't' muet [bee-yay] | 3. théâtre -> 't' franc [tay-ahtr] | 4. violon -> nasale [vyoh-lohn] | 5. guitare -> 'g' dur [gee-tahr] | 6. comédie -> 'é' fermé [koh-may-dee].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le théâtre (accent aigu, accent circonflexe) | b) le cinéma | c) la flûte (circonflexe sur 'û') | d) une séance (accent aigu) | e) une comédie | f) un chanteur.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un acteur -> Liaison en [n] obligatoire [œ̃.nak.tœʁ] | 2. un grand artiste -> Liaison en [t] [œ̃.gʁɑ̃.taʁ.tist] | 3. deux billets -> Pas de liaison devant consonne | 4. aller au concert -> Pas de liaison | 5. aux artistes -> Liaison en [z] [o.zaʁ.tist] | 6. un opéra -> Liaison en [n] [œ̃.nɔ.pe.ʁa].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. jouer du piano | 2. jouer de la guitare | 3. jouer du violon | 4. jouer de la batterie | 5. jouer de la flûte | 6. jouer du saxophone.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'jouer DU piano' (instrument de musique avec jouer de, pas jouer à).\n2. 'LA pièce de théâtre' (pièce est féminin : la pièce).\n3. 'LA prochaine séance' (séance est féminin : la prochaine séance).\n4. 'une NOUVELLE chanson' (chanson est féminin : une nouvelle chanson).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. du violon | 2. de la batterie | 3. du piano / au football | 4. de la guitare | 5. au concert.\n\nExercice 3.2 — Paires Culturelles [5 pts] :\n1 -> B (Comédie -> film léger destiné à faire rire) | 2 -> C (Film d'action -> film dynamique avec cascades) | 3 -> A (Pièce de théâtre -> comédiens sur scène) | 4 -> D (Concert -> représentation musicale) | 5 -> E (Musée -> exposition d'œuvres d'art).",
        "tier4_text": "Situation A (3 pts) : film | séance | séance (ou soirée).\nSituation B (4 pts) : instrument | guitare | piano | concert.\nSituation C (3 pts) : théâtre | pièce | comédie.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Elle joue très bien de la guitare.\n2. Je voudrais deux billets pour le concert, s'il vous plaît.\n3. À quelle heure commence la séance de cinéma ?\n4. Nous allons au théâtre pour voir une pièce.\n5. C'est un acteur très célèbre en France.\n6. Tu joues du piano ?\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Le football (sport de balle collectif, les 3 autres sont des instruments de musique acoustiques).\n2. Jouer au tennis (seule collocation utilisant la préposition 'à' pour un sport, les 3 autres utilisent 'de' pour un instrument).\n3. L'hôpital (établissement médical de soins, les 3 autres sont des lieux de diffusion culturelle et artistique).\n4. Une fourchette (ustensile de table pour manger, les 3 autres sont des genres cinématographiques).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 9",
        "anchors_text": "1. Le contraste Jouer à vs Jouer de : Retenez fermement la distinction : 'Je joue AU football' (sport avec à + le = au), mais 'Je joue DU piano' (musique avec de + le = du) et 'Je joue DE LA guitare' (musique féminine).\n2. Séance vs Film : On ne dit pas 'acheter un film', mais 'acheter une place pour la séance de 20 heures'. Le mot 'séance' désigne l'horaire de projection publique.\n3. Billets vs Tickets : En français, pour le train, l'avion, le théâtre ou le concert, on emploie 'un billet'. Pour le métro et le bus, on emploie 'un ticket'."
    }
}

# CHAPTER 10
batch1["10"] = {
    "ch_num": 10,
    "title_fr": "Les jours de la semaine et les moments de la journée",
    "title_en": "Weekdays, Moments of the Day & Telling Time",
    "word_count": 40,
    "traps": [
        "Telling time formula: 'Il est huit heures' (always 'Il est', never 'C'est'). Minutes past the hour: 'et quart' (15 min), 'et demie' (30 min - with 'e' for feminine heure), 'moins le quart' (45 min with article 'le'!).",
        "Days of the week are all MASCULINE and take NO article for a single occurrence: 'Lundi, j'ai cours' (this Monday). With article 'le', it expresses recurrence: 'Le lundi, je fais du sport' (every Monday).",
        "Times of day: le matin, le midi, l'après-midi, le soir, la nuit. Official 24h clock: 14h30 = quatorze heures trente."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LA LIAISON TEMPORELLE EN [Z] AVEC HEURES",
        "phonetic_tip_text": "Dans l'heure, la liaison en [z] est obligatoire : deux heures [duh-zuhr], trois heures [trwah-zuhr], six heures [see-zuhr], dix heures [dee-zuhr]. 'Neuf heures' se lie en [v] : [nuh-vuhr] !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de l'Heure et des Jours [4 pts]",
        "ex1_headers": ["Expression temporelle", "Phénomène phonétique", "Liaison sonore", "Son IPA A1", "Règle clé"],
        "ex1_rows": [
            ["1. deux heures", "Liaison 'x+h'", "[  ] Liaison [z]", "[ duh-zuhr ]", "Liaison obligatoire"],
            ["2. six heures", "Liaison 'x+h'", "[  ] Liaison [z]", "[ see-zuhr ]", "Liaison obligatoire"],
            ["3. neuf heures", "Liaison 'f->v'", "[  ] Liaison [v]", "[ nuh-vuhr ]", "Shift de consonne 'f' en [v]"],
            ["4. midi (12h00)", "Consonne finale 'i'", "[  ] Pas de liaison", "[ mee-dee ]", "Heure fixe invariable"],
            ["5. minuit (00h00)", "Consonne 't' muette", "[  ] [mee-nwee]", "[ mee-nweet ]", "Consonne 't' silencieuse"],
            ["6. mercredi", "Consonne 'r' uvulaire", "[  ] [mair-kruh-dee]", "[ mair-kree-dee ]", "Troisième jour"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Jours et Heures [3 pts]",
        "ex2_items": [
            "a) huit heures et demi -> ________________________",
            "b) moins le quart -> ________________________",
            "c) l'apres-midi -> ________________________",
            "d) a quelle heure -> ________________________",
            "e) tot le matin -> ________________________",
            "f) tard le soir -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Temporelles [3 pts]",
        "ex3_items": [
            "1. trois heures     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "2. huit heures      -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison",
            "3. dix heures       -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "4. sept heures      -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison",
            "5. midi et quart    -> [  ] Liaison                    [  ] Pas de liaison",
            "6. vers huit heures -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES JOURS ET ACCORD DE DEMIE",
        "gender_rule_text": "Tous les jours de la semaine sont MASCULINS : le lundi, le mardi, etc. Dans l'expression de l'heure, 'demie' s'accorde au féminin avec le mot sous-entendu 'heure' : 'huit heures et demie' (avec un 'e'). En revanche, 'midi et demi' s'écrit au masculin !",
        "ex1_title": "Exercice 2.1 — Matrice des Heures Clés (Style Parlé vs 24h Officiel) [6 pts]",
        "ex1_headers": ["Heure chiffrée", "Style parlé courant", "Horloge 24h officielle", "Sens anglais"],
        "ex1_rows": [
            ["1. 08:00", "Il est huit heures", "08h00", "8 o'clock"],
            ["2. 08:15", "Il est huit heures et quart", "08h15", "Quarter past eight"],
            ["3. 08:30", "Il est huit heures et demie", "08h30", "Half past eight"],
            ["4. 08:45", "Il est neuf heures moins le quart", "08h45", "Quarter to nine"],
            ["5. 12:00", "Il est midi", "12h00", "Noon / Midday"],
            ["6. 00:00", "Il est minuit", "00h00", "Midnight"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre & Heures : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. C'est huit heures et demi du matin.\n   Correction : _____________________________________________________________________________",
            "2. Le train part à midi et demie précise.\n   Correction : _____________________________________________________________________________",
            "3. Je fais du jogging à chaque le dimanche.\n   Correction : _____________________________________________________________________________",
            "4. Il est dix heures moins quart.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS CHRONOLOGIQUES ET HABITUDES",
        "colloc_tip_text": "Nuance capitale en FLE : 'Lundi, je travaille' = ce lundi prochain uniquement. 'LE lundi, je travaille' = tous les lundis par habitude récurrente ! Pour les périodes : 'le matin', 'le midi', 'l'après-midi', 'le soir', 'la nuit'.",
        "ex1_title": "Exercice 3.1 — Prépositions et Marqueurs Temporels [5 pts]",
        "ex1_sentences": [
            "1. Le cours de français commence _________ (à / en) neuf heures et quart.",
            "2. _________ (Le / En) samedi, les enfants ne vont pas à l'école.",
            "3. Nous mangeons habituellement en famille _________ (au / le) soir vers vingt heures.",
            "4. Le spectacle se termine _________ (vers / sur) minuit.",
            "5. Quelle heure est-il ? - _________ (Il est / C'est) quatorze heures trente."
        ],
        "ex2_title": "Exercice 3.2 — Paires Moments de la Journée & Activités [5 pts]",
        "ex2_headers": ["Moment de la journée", "Activité typique associée", "Association"],
        "ex2_rows": [
            ["1. Le matin (7h00)...", "A. dîner en famille et regarder les nouvelles", "1 -> [    ]"],
            ["2. Le midi (12h30)...", "B. se réveiller et prendre son café", "2 -> [    ]"],
            ["3. L'après-midi (16h00)...", "C. faire une pause déjeuner entre collègues", "3 -> [    ]"],
            ["4. Le soir (20h00)...", "D. dormir et se reposer au calme", "4 -> [    ]"],
            ["5. La nuit (02h00)...", "E. prendre le goûter et travailler au bureau", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE GESTION D'EMPLOI DU TEMPS",
        "cloze_tip_text": "Complétez les dialogues d'horaires et de rendez-vous avec les formules temporelles précises.",
        "dialogues": [
            {
                "title": "Situation A — Demander l'heure dans la rue",
                "points": "3 pts",
                "lines": [
                    "• Le passant : Pardon Monsieur, quelle ___________________________ [time is it / heure est-il], s'il vous plaît ?",
                    "• Marc : Il est dix heures et ___________________________ [quarter past / et quart].",
                    "• Le passant : Merci beaucoup !"
                ]
            },
            {
                "title": "Situation B — Fixer un rendez-vous professionnel",
                "points": "4 pts",
                "lines": [
                    "• La secrétaire : Le docteur peut vous recevoir ___________________________ [on Thursday] à quatorze heures.",
                    "• Le patient : Je préfère en fin de journée. Il a de la place à dix-sept heures et ___________________________ [half past] ?",
                    "• La secrétaire : Oui, à dix-sept heures trente. C'est noté pour jeudi ___________________________ [afternoon]."
                ]
            },
            {
                "title": "Situation C — Organisation des activités hebdomadaires",
                "points": "3 pts",
                "lines": [
                    "• Sophie : Tu fais du sport quel jour ?",
                    "• Thomas : ___________________________ [On Wednesdays - recurring], je vais à la piscine, et ___________________________ [on Saturdays], je fais du vélo.",
                    "• Sophie : Et le dimanche ? - Le dimanche, je me repose !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. What time is it? - It is 8:30 AM.", "-> __________________________________________________________________________________"],
            ["2. The train leaves at a quarter to ten.", "-> __________________________________________________________________________________"],
            ["3. On Mondays, I wake up early in the morning.", "-> __________________________________________________________________________________"],
            ["4. The meeting is scheduled for Friday at noon.", "-> __________________________________________________________________________________"],
            ["5. We have dinner at eight o'clock in the evening.", "-> __________________________________________________________________________________"],
            ["6. See you on Tuesday at quarter past three!", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Lundi  •  Mardi  •  Mercredi  •  Janvier",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le matin  •  Le midi  •  Le soir  •  La fourchette",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Et quart  •  Et demie  •  Moins le quart  •  Beaucoup",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Midi  •  Minuit  •  Quatorze heures  •  La chambre",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. deux heures -> Liaison en [z] [duh-zuhr] | 2. six heures -> Liaison en [z] [see-zuhr] | 3. neuf heures -> Liaison avec mutation de son en [v] [nuh-vuhr] | 4. midi -> [mee-dee] | 5. minuit -> 't' muet [mee-nwee] | 6. mercredi -> [mair-kruh-dee].\n\nExercice 1.2 — Orthographe [3 pts] :\na) huit heures et demie (demie s'accorde au féminin avec heure) | b) moins le quart (avec l'article 'le') | c) l'après-midi (accent grave, trait d'union) | d) à quelle heure (accent grave sur à) | e) tôt le matin (accent circonflexe sur 'ô') | f) tard le soir.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. trois heures -> Liaison en [z] [tʁwa.zœʁ] | 2. huit heures -> Liaison en [t] [ɥi.tœʁ] | 3. dix heures -> Liaison en [z] [di.zœʁ] | 4. sept heures -> Liaison en [t] [sɛ.tœʁ] | 5. midi et quart -> Pas de liaison | 6. vers huit heures -> Liaison en [z] [vɛʁ.zɥi.tœʁ].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. Il est huit heures / 08h00 | 2. Il est huit heures et quart / 08h15 | 3. Il est huit heures et demie / 08h30 | 4. Il est neuf heures moins le quart / 08h45 | 5. Il est midi / 12h00 | 6. Il est minuit / 00h00.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'IL EST huit heures et DEMIE' (on utilise 'il est' pour l'heure, et 'demie' avec un 'e').\n2. 'midi et DEMI' (midi est masculin, donc demi sans 'e').\n3. 'LE dimanche' (l'article 'le' suffit à marquer l'habitude, pas de 'à chaque le').\n4. 'moins LE quart' (l'article défini 'le' est obligatoire).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. à | 2. Le | 3. le | 4. vers | 5. Il est.\n\nExercice 3.2 — Paires Moments [5 pts] :\n1 -> B (Le matin -> réveil et café) | 2 -> C (Le midi -> pause déjeuner) | 3 -> E (L'après-midi -> goûter et travail) | 4 -> A (Le soir -> dîner et nouvelles) | 5 -> D (La nuit -> dormir).",
        "tier4_text": "Situation A (3 pts) : heure | quart | journée (ou séance).\nSituation B (4 pts) : jeudi | demie | après-midi.\nSituation C (3 pts) : Le mercredi | le samedi.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Quelle heure est-il ? - Il est huit heures et demie du matin.\n2. Le train part à dix heures moins le quart.\n3. Le lundi, je me réveille tôt le matin.\n4. La réunion est prévue vendredi à midi.\n5. Nous dînons à vingt heures le soir (ou à huit heures du soir).\n6. À mardi à quinze heures et quart !\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Janvier (mois de l'année, les 3 autres sont des jours de la semaine).\n2. La fourchette (ustensile de couvert de table, les 3 autres sont des moments de la journée).\n3. Beaucoup (adverbe de quantité indéfinie, les 3 autres sont des fractions de l'horloge : quart, demie).\n4. La chambre (pièce de la maison pour dormir, les 3 autres sont des repères horaires précis de la journée).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 10",
        "anchors_text": "1. La formule impersonnelle de l'heure : Pour demander ou dire l'heure, on emploie TOUJOURS 'IL EST' ('Quelle heure est-il ?', 'Il est trois heures'). L'emploi de 'C'est trois heures' est une erreur courante chez les anglophones.\n2. L'accord de 'demie' : Retenez la règle : 'huit heures et demie' prend un 'e' (accord avec heure, féminin). Mais 'midi et demi' et 'minuit et demi' restent masculins SANS 'e' !\n3. L'article 'le' d'habitude : Dire 'Dimanche, je dors' = ce dimanche précis. Dire 'LE dimanche, je dors' = tous les dimanches par rituel récurrent."
    }
}

# CHAPTER 11
batch1["11"] = {
    "ch_num": 11,
    "title_fr": "Les activités quotidiennes & tâches ménagères",
    "title_en": "Daily Routine, Bathroom Hygiene & Household Chores",
    "word_count": 42,
    "traps": [
        "Reflexive verbs pronouns: je me, tu te, il/elle se, nous nous, vous vous, ils/elles se (se réveiller, se lever, se doucher, se brosser les dents, s'habiller).",
        "Body parts in hygiene take DEFINITE articles, NEVER possessives: 'Je me brosse LES dents' (not 'mes dents'!), 'Il se lave LES mains' (not 'ses mains'!).",
        "Household chores collocations: faire la vaisselle (wash dishes), passer l'aspirateur (vacuum), faire le ménage (clean up), faire les courses (groceries)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "L'ÉLISION DU PRONOM RÉFLÉCHI DEVANT VOYELLE",
        "phonetic_tip_text": "Devant un verbe commençant par une voyelle ou un 'h' muet, les pronoms réfléchis s'élident : 'je m'habille' [zhmah-beey], 'il s'endort' [eel sahn-dohr]. 'Savon' a la voyelle nasale [sah-vohn], 'shampoing' [shahm-pwanh].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de la Routine [4 pts]",
        "ex1_headers": ["Verbe pronominal", "Phénomène phonétique", "Prononciation A1", "Élision ?", "Formule"],
        "ex1_rows": [
            ["1. je me réveille", "Pronom 'me' plein", "[ zhuh muh ray-vay ]", "[  ] Non", "Action du matin"],
            ["2. je m'habille", "Élision 'm' + h'", "[  ] [zhmah-beey]", "[  ] Oui", "Vêtement"],
            ["3. le shampoing", "Diphtongue 'oing'", "[  ] [shahm-pwanh]", "[  ] [shahm-pwohn]", "Hygiène cheveux"],
            ["4. le dentifrice", "Digraphe 'en'+'i'", "[  ] [dahn-tee-frees]", "[  ] [den-tee-freek]", "Brossage dents"],
            ["5. l'aspirateur", "Consonne 'r' finale", "[  ] [lah-spee-rah-tuhr]", "[  ] [lah-spee-rah-tur]", "Ménage sol"],
            ["6. se coucher", "Digraphe 'ou'", "[  ] [suh koo-shay]", "[  ] [suh koh-shay]", "Action du soir"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique de la Routine [3 pts]",
        "ex2_items": [
            "a) se reveiller -> ________________________",
            "b) se lever -> ________________________",
            "c) se secher -> ________________________",
            "d) une serviette -> ________________________",
            "e) la vaisselle -> ________________________",
            "f) l'aspirateur -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Verbes Réfléchis [3 pts]",
        "ex3_items": [
            "1. nous nous levons  -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "2. vous vous lavez   -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. ils se réveillent -> [  ] Liaison                    [  ] Pas de liaison",
            "4. ils s'endorment   -> [  ] Liaison [z] sonore         [  ] Pas de liaison",
            "5. vous vous habillez -> [  ] Liaison [z] sonore        [  ] Pas de liaison",
            "6. elle se brosse    -> [  ] Liaison                    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES PRODUITS D'HYGIÈNE ET DU MÉNAGE",
        "gender_rule_text": "Objets de la salle de bains : LE savon (m.), LE shampoing (m.), LE dentifrice (m.), LE rasoir (m.) ; mais LA brosse à dents (f.), LA serviette (f.), LA douche (f.).",
        "ex1_title": "Exercice 2.1 — Matrice des Objets de Toilette et Tâches [6 pts]",
        "ex1_headers": ["Objet / Tâche (Genre)", "Article défini (le/la/l')", "Action réflexive associée", "Sens anglais"],
        "ex1_rows": [
            ["1. Savon (m.)", "-> le savon", "se laver les mains", "Soap / Wash hands"],
            ["2. Brosse à dents (f.)", "-> la brosse à dents", "se brosser les dents", "Toothbrush / Brush teeth"],
            ["3. Shampoing (m.)", "-> le shampoing", "se laver les cheveux", "Shampoo / Wash hair"],
            ["4. Rasoir (m.)", "-> le rasoir", "se raser la barbe", "Razor / Shave"],
            ["5. Serviette (f.)", "-> la serviette", "se sécher le corps", "Towel / Dry oneself"],
            ["6. Aspirateur (m.)", "-> l'aspirateur", "passer l'aspirateur", "Vacuum cleaner"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Chaque matin, je me brosse mes dents avec un dentifrice.\n   Correction : _____________________________________________________________________________",
            "2. Après sa douche, elle utilise un grande serviette blanche.\n   Correction : _____________________________________________________________________________",
            "3. Mon frère oublie souvent de faire le vaisselle après le dîner.\n   Correction : _____________________________________________________________________________",
            "4. Il se lave son visage avec de l'eau fraîche.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS FIGÉES DU MÉNAGE : LE VERBE FAIRE",
        "colloc_tip_text": "La majorité des tâches domestiques se forment avec FAIRE : faire le lit, faire la vaisselle, faire les courses, faire la cuisine, faire le ménage, faire la lessive. Exception notable : PASSER l'aspirateur / la serpillière.",
        "ex1_title": "Exercice 3.1 — Verbes d'Action Domestique (FAIRE vs PASSER) [5 pts]",
        "ex1_sentences": [
            "1. Après le repas, nous devons _________ (faire / passer) la vaisselle.",
            "2. Il y a de la poussière sur le tapis ; je vais _________ (passer / faire) l'aspirateur.",
            "3. Tous les samedis matin, mes parents vont au supermarché pour _________ (faire / passer) les courses.",
            "4. Avant de partir au travail, n'oublie pas de _________ (faire / passer) ton lit !",
            "5. Le dimanche après-midi, elle s'occupe de _________ (faire / passer) la lessive."
        ],
        "ex2_title": "Exercice 3.2 — Paires Chronologiques de la Routine [5 pts]",
        "ex2_headers": ["Étape de la journée", "Action suivante logique", "Association"],
        "ex2_rows": [
            ["1. Le réveil sonne à 7h...", "A. s'habiller et mettre ses chaussures", "1 -> [    ]"],
            ["2. Sortir du lit...", "B. se réveiller et ouvrir les yeux", "2 -> [    ]"],
            ["3. Prendre sa douche...", "C. aller dans la salle de bains et se laver", "3 -> [    ]"],
            ["4. Après s'être séché...", "D. prendre son petit-déjeuner dans la cuisine", "4 -> [    ]"],
            ["5. Une fois habillé...", "E. partir de la maison et prendre le bus", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE CHRONOLOGIE DE LA JOURNÉE",
        "cloze_tip_text": "Complétez le récit de journée avec les verbes pronominaux et les tâches ménagères exacts.",
        "dialogues": [
            {
                "title": "Situation A — Raconter sa matinée à un collègue",
                "points": "3 pts",
                "lines": [
                    "• Nicolas : À quelle heure tu te ___________________________ [wake up] le matin ?",
                    "• Marc : En semaine, je me réveille à 6h30, puis je me ___________________________ [get up / out of bed] immédiatement.",
                    "• Nicolas : Et tu as le temps de te ___________________________ [take a shower] avant de partir ?",
                    "• Marc : Oui, bien sûr !"
                ]
            },
            {
                "title": "Situation B — Répartition des corvées dans la colocation",
                "points": "4 pts",
                "lines": [
                    "• Julie : Ce soir, c'est mon tour de cuisiner.",
                    "• Thomas : D'accord ! Moi, je m'occupe de faire la ___________________________ [dishes] après le repas.",
                    "• Julie : Super. Et qui passe ___________________________ [the vacuum cleaner] dans le salon ?",
                    "• Thomas : Lucas va le faire demain matin, et il fera aussi les ___________________________ [groceries]."
                ]
            },
            {
                "title": "Situation C — Rituel du coucher",
                "points": "3 pts",
                "lines": [
                    "• Maman : Les enfants, il est 21 heures. Allez vous brosser les ___________________________ [teeth] !",
                    "• Paul : On met nos pyjamas maintenant ?",
                    "• Maman : Oui, et ensuite vous allez vous ___________________________ [go to bed / sleep]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. Every morning, I wash my face and brush my teeth.", "-> __________________________________________________________________________________"],
            ["2. He wakes up at seven o'clock and takes a shower.", "-> __________________________________________________________________________________"],
            ["3. We do the dishes together after dinner.", "-> __________________________________________________________________________________"],
            ["4. She vacuums her bedroom on Saturdays.", "-> __________________________________________________________________________________"],
            ["5. What time do you go to bed? (informal with 'tu')", "-> __________________________________________________________________________________"],
            ["6. I have to do the groceries this afternoon.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Se réveiller  •  Se lever  •  Se doucher  •  Prendre l'avion",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le savon  •  Le shampoing  •  Le dentifrice  •  Le marteau",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Faire la vaisselle  •  Faire le lit  •  Passer l'aspirateur  •  Regarder un film",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La serviette  •  Le rasoir  •  La brosse à dents  •  Le cahier",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. réveille -> [zhuh muh ray-vay] | 2. habille -> élision 'm' + 'h' [zhmah-beey] | 3. shampoing -> nasale [shahm-pwanh] | 4. dentifrice -> [dahn-tee-frees] | 5. aspirateur -> 'r' prononcé [lah-spee-rah-tuhr] | 6. coucher -> [suh koo-shay].\n\nExercice 1.2 — Orthographe [3 pts] :\na) se réveiller (accents aigus) | b) se lever | c) se sécher (accent aigu puis grave) | d) une serviette (deux 't') | e) la vaisselle (deux 's', deux 'l') | f) l'aspirateur.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. nous nous levons -> Pas de liaison devant consonne 'l' | 2. vous vous lavez -> Pas de liaison devant 'l' | 3. ils se réveillent -> Pas de liaison | 4. ils s'endorment -> Liaison en [z] [il.sɑ̃.dɔʁm] | 5. vous vous habillez -> Liaison en [z] [vu.vu.za.bi.je] | 6. elle se brosse -> Pas de liaison.",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. le savon / se laver les mains | 2. la brosse à dents / se brosser les dents | 3. le shampoing / se laver les cheveux | 4. le rasoir / se raser la barbe | 5. la serviette / se sécher | 6. l'aspirateur / passer l'aspirateur.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'je me brosse LES dents' (pas d'adjectif possessif avec les parties du corps lors d'une action réflexive).\n2. 'UNE grande serviette' (serviette est féminin : une grande serviette).\n3. 'faire LA vaisselle' (vaisselle est féminin : la vaisselle).\n4. 'il se lave LE visage' (pas de possessif : le visage).",
        "tier3_text": "Exercice 3.1 — Verbes Domestiques [5 pts] :\n1. faire la vaisselle | 2. passer l'aspirateur | 3. faire les courses | 4. faire ton lit | 5. faire la lessive.\n\nExercice 3.2 — Paires Chronologiques [5 pts] :\n1 -> B (Le réveil sonne -> se réveiller) | 2 -> C (Sortir du lit -> salle de bains) | 3 -> A (Douche -> s'habiller) | 4 -> D (Une fois séché -> petit-déjeuner) | 5 -> E (Habillé -> partir au bus).",
        "tier4_text": "Situation A (3 pts) : réveilles | lève | doucher.\nSituation B (4 pts) : vaisselle | l'aspirateur | courses.\nSituation C (3 pts) : dents | coucher.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Chaque matin, je me lave le visage et je me brosse les dents.\n2. Il se réveille à sept heures et prend une douche (ou se douche).\n3. Nous faisons la vaisselle ensemble après le dîner.\n4. Elle passe l'aspirateur dans sa chambre le samedi.\n5. À quelle heure tu te couches ?\n6. Je dois faire les courses cet après-midi.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Prendre l'avion (voyage international longue distance, les 3 autres sont des étapes de la routine matinale au réveil).\n2. Le marteau (outil de bricolage manuel, les 3 autres sont des produits d'hygiène corporelle dans la salle de bains).\n3. Regarder un film (activité de loisir et de divertissement, les 3 autres sont des corvées ménagères indispensables).\n4. Le cahier (fourniture de papeterie scolaire, les 3 autres sont des accessoires de toilette intime et corporelle).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 11",
        "anchors_text": "1. L'omission du possessif avec les parties du corps : En français, le pronom réfléchi ('me', 'te', 'se') indique déjà à qui appartient le membre. On dit donc 'Je me lave LES mains', 'Elle se brosse LES dents' (et JAMAIS 'mes mains' ou 'ses dents').\n2. Se réveiller vs Se lever : 'Se réveiller' = ouvrir les yeux après le sommeil (to wake up). 'Se lever' = sortir physiquement du lit pour se mettre debout (to get up).\n3. Les collocations du ménage : Mémorisez que 'faire' gouverne presque toutes les tâches ('faire la vaisselle', 'faire le lit', 'faire la cuisine', 'faire les courses'), SAUF 'passer l'aspirateur'."
    }
}

with open("chapters_batch_1.json", "w", encoding="utf-8") as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print(f"Success! Batch 1 completely saved with {len(batch1)} chapters.")
