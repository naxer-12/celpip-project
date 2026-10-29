import json

with open("chapters_batch_1.json", "r", encoding="utf-8") as f:
    batch1 = json.load(f)

# CHAPTER 4
batch1["4"] = {
    "ch_num": 4,
    "title_fr": "Le corps humain et les âges de la vie",
    "title_en": "The Human Body & Stages of Life",
    "word_count": 42,
    "traps": [
        "Irregular singular/plural: 'un œil' [uhn oy] -> 'les yeux' [lay zyuh] (complete root shift).",
        "False cognate / spelling trap: 'bras' has a silent 's' in singular and plural [brah]. 'Doigt' has silent 'gt' [dwah].",
        "Aches formula: 'Avoir mal à' contracts with articles: au (m.), à la (f.), à l' (vowel), aux (pluriel) -> 'mal au ventre', 'mal aux dents'."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'S' ET LE 'GT' SILENCIEUX DES PARTIES DU CORPS",
        "phonetic_tip_text": "Le corps humain regorge de consonnes silencieuses : le bras [brah] (pas de son s), le doigt [dwah] (pas de son gt), le pied [pyay] (pas de son d), le nez [nay] (pas de son z).",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de l'Anatomie Humaine [4 pts]",
        "ex1_headers": ["Partie du corps", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le bras (m.)", "Consonne 's'", "[  ] Oui", "[  ] Oui", "[ brah ]"],
            ["2. le doigt (m.)", "Consonnes 'gt'", "[  ] Oui", "[  ] Oui", "[ dwah ]"],
            ["3. le pied (m.)", "Consonne 'd'", "[  ] Oui", "[  ] Oui", "[ pyay ]"],
            ["4. le nez (m.)", "Consonne 'z'", "[  ] Oui", "[  ] Oui", "[ nay ]"],
            ["5. les yeux (pl.)", "Liaison 's+y'", "[  ] [lay zyuh]", "[  ] [lay yuh]", "[ lay zyuh ]"],
            ["6. la bouche (f.)", "Digraphe 'ou'", "[  ] [boosh]", "[  ] [bowk]", "[ boosh ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique de l'Anatomie [3 pts]",
        "ex2_items": [
            "a) un oeil -> ________________________",
            "b) la tete -> ________________________",
            "c) le dos -> ________________________",
            "d) le coeur -> ________________________",
            "e) une jambe -> ________________________",
            "f) les cheveux -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Anatomiques [3 pts]",
        "ex3_items": [
            "1. les yeux        -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "2. les oreilles    -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un enfant       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. deux bras       -> [  ] Liaison                    [  ] Pas de liaison",
            "5. les mains       -> [  ] Liaison                    [  ] Pas de liaison",
            "6. un adulte       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "GENRE ET ARTICLES OBLIGATOIRES DES ORGANES",
        "gender_rule_text": "Attention aux genres contre-intuitifs : LA tête (f.), LA main (f.), LA jambe (f.), LA bouche (f.) ; mais LE dos (m.), LE ventre (m.), LE cou (m.), LE bras (m.), LE pied (m.).",
        "ex1_title": "Exercice 2.1 — Matrice des Parties du Corps & Articles Définis [6 pts]",
        "ex1_headers": ["Organe / Partie", "Article défini (le/la/l'/les)", "Organe / Partie", "Article défini (le/la/l'/les)"],
        "ex1_rows": [
            ["1. tête (f.)", "-> [    ] tête", "7. ventre (m.)", "-> [    ] ventre"],
            ["2. main (f.)", "-> [    ] main", "8. dos (m.)", "-> [    ] dos"],
            ["3. bras (m.)", "-> [    ] bras", "9. oreille (f.)", "-> [    ] oreille"],
            ["4. pied (m.)", "-> [    ] pied", "10. œil (m.)", "-> [    ] œil"],
            ["5. jambe (f.)", "-> [    ] jambe", "11. yeux (pl.)", "-> [    ] yeux"],
            ["6. nez (m.)", "-> [    ] nez", "12. dents (pl. f.)", "-> [    ] dents"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Il a mal à le ventre après le repas.\n   Correction : _____________________________________________________________________________",
            "2. Elle a cassé son jambe droite au ski.\n   Correction : _____________________________________________________________________________",
            "3. Mon grand-père a un mal de le dos terrible.\n   Correction : _____________________________________________________________________________",
            "4. L'enfant s'est lavé le main avant de manger.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE DOULEUR : LA FORMULE 'AVOIR MAL À'",
        "colloc_tip_text": "Pour exprimer une douleur physique : AVOIR MAL + contraction (à + le = au, à + la = à la, à + l' = à l', à + les = aux). Exemples : J'ai mal au dos, mal à la tête, mal aux yeux.",
        "ex1_title": "Exercice 3.1 — Contractions Prépositionnelles de Douleur [5 pts]",
        "ex1_sentences": [
            "1. J'ai trop lu sur mon écran ; j'ai mal _________ (les yeux).",
            "2. Après le marathon, le coureur a mal _________ (la jambe droite).",
            "3. Marc a trop mangé de chocolat ; il a mal _________ (le ventre).",
            "4. La chanteuse a mal _________ (la gorge) depuis hier soir.",
            "5. Vous devez aller chez le dentiste si vous avez mal _________ (les dents)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Âges de la Vie & Actions [5 pts]",
        "ex2_headers": ["Étape de la vie", "Caractéristique / Définition", "Association"],
        "ex2_rows": [
            ["1. Un bébé...", "A. personne âgée de plus de 75 ans", "1 -> [    ]"],
            ["2. Un enfant...", "B. nourrisson de moins d'un an", "2 -> [    ]"],
            ["3. Un adolescent...", "C. individu majeur responsable de 18 ans et plus", "3 -> [    ]"],
            ["4. Un adulte...", "D. jeune scolarisé entre 12 et 17 ans", "4 -> [    ]"],
            ["5. Un senior...", "E. petit garçon ou fillette de 6 ans", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE CONSULTATION MÉDICALE COMMUNICATIVE",
        "cloze_tip_text": "Complétez avec les parties du corps et expressions d'âge exactes guidées par l'indice contextuel.",
        "dialogues": [
            {
                "title": "Situation A — Chez le médecin de garde",
                "points": "3 pts",
                "lines": [
                    "• Le médecin : Bonjour Madame. Où avez-vous ___________________________ [pain / ache] exactement ?",
                    "• La patiente : Docteur, j'ai très mal à la ___________________________ [head] et j'ai mal à la ___________________________ [throat].",
                    "• Le médecin : Ouvrez la ___________________________ [mouth], s'il vous plaît."
                ]
            },
            {
                "title": "Situation B — Accident de sport sur le terrain",
                "points": "4 pts",
                "lines": [
                    "• L'entraîneur : Que s'est-il passé, Thomas ?",
                    "• Thomas : Je suis tombé sur le ___________________________ [arm] gauche et j'ai mal au ___________________________ [foot].",
                    "• L'entraîneur : Tu peux bouger les ___________________________ [fingers] de la main ?",
                    "• Thomas : Oui, mais la ___________________________ [leg] me fait très mal."
                ]
            },
            {
                "title": "Situation C — Présentation des membres de la famille par âge",
                "points": "3 pts",
                "lines": [
                    "• Sophie : Mon fils est encore un ___________________________ [baby] de six mois.",
                    "• Lucas : Et ta fille a quel âge ?",
                    "• Sophie : C'est une ___________________________ [teenager / adolecent] de quinze ans."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. I have a stomachache and a headache.", "-> __________________________________________________________________________________"],
            ["2. Close your eyes and open your mouth.", "-> __________________________________________________________________________________"],
            ["3. He has blond hair and blue eyes.", "-> __________________________________________________________________________________"],
            ["4. The baby is sleeping peacefully.", "-> __________________________________________________________________________________"],
            ["5. My back hurts after carrying the boxes.", "-> __________________________________________________________________________________"],
            ["6. She broke her right arm while playing tennis.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. La tête  •  Le bras  •  La jambe  •  La table",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Les yeux  •  Les oreilles  •  Le nez  •  Le genou",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Un bébé  •  Un enfant  •  Un adulte  •  Un hôpital",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La main  •  Le pied  •  Le doigt  •  Le rhume",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. bras -> 's' muet [brah] | 2. doigt -> 'gt' muets [dwah] | 3. pied -> 'd' muet [pyay] | 4. nez -> 'z' muet [nay] | 5. les yeux -> liaison en [z] sonore [lay zyuh] | 6. la bouche -> [boosh].\n\nExercice 1.2 — Orthographe [3 pts] :\na) un œil (ligature œ) | b) la tête (accent circonflexe sur le premier 'e') | c) le dos | d) le cœur (ligature œ) | e) une jambe | f) les cheveux.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. les yeux -> Liaison en [z] | 2. les oreilles -> Liaison en [z] | 3. un enfant -> Liaison en [n] | 4. deux bras -> Pas de liaison | 5. les mains -> Pas de liaison devant consonne | 6. un adulte -> Liaison en [n].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. la tête | 2. la main | 3. le bras | 4. le pied | 5. la jambe | 6. le nez | 7. le ventre | 8. le dos | 9. l'oreille | 10. l'œil | 11. les yeux | 12. les dents.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'mal AU ventre' (à + le = au).\n2. 'sa jambe droite' (jambe est féminin : sa jambe).\n3. 'mal AU dos' (dos est masculin : au dos).\n4. 'les mains' (ou 'la main', main est féminin : la main).",
        "tier3_text": "Exercice 3.1 — Contractions [5 pts] :\n1. aux yeux | 2. à la jambe | 3. au ventre | 4. à la gorge | 5. aux dents.\n\nExercice 3.2 — Paires Âges [5 pts] :\n1 -> B (Un bébé nourrisson) | 2 -> E (Un enfant de 6 ans) | 3 -> D (Un adolescent de 12-17 ans) | 4 -> C (Un adulte de 18 ans et plus) | 5 -> A (Un senior de 75 ans).",
        "tier4_text": "Situation A (3 pts) : mal | tête | gorge | bouche.\nSituation B (4 pts) : bras | pied | doigts | jambe.\nSituation C (3 pts) : bébé | adolescente (ou ado).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. J'ai mal au ventre et à la tête.\n2. Fermez les yeux et ouvrez la bouche.\n3. Il a les cheveux blonds et les yeux bleus.\n4. Le bébé dort paisiblement.\n5. J'ai mal au dos après avoir porté les cartons.\n6. Elle s'est cassé le bras droit en jouant au tennis.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. La table (meuble inanimé, les 3 autres sont des parties du corps humain).\n2. Le genou (articulation du membre inférieur, les 3 autres sont des organes des sens situés sur le visage).\n3. Un hôpital (bâtiment médical, les 3 autres sont des étapes de la vie humaine).\n4. Le rhume (maladie / infection, les 3 autres sont des membres / extrémités du corps).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 4",
        "anchors_text": "1. L'irrégularité œil / yeux : C'est le cas d'hétéroclisie le plus spectaculaire en français A1 : un œil au singulier, mais les yeux au pluriel avec liaison obligatoire en [z] !\n2. Le genre de la main : Alors que presque tous les membres sont masculins (le bras, le pied, le doigt, le coude, le genou), 'LA MAIN' est féminine !\n3. La formule 'avoir mal à' : Pensez toujours aux contractions obligatoires : à + le = AU (au dos, au ventre) ; à + les = AUX (aux yeux, aux dents)."
    }
}

# CHAPTER 5
batch1["5"] = {
    "ch_num": 5,
    "title_fr": "Les caractéristiques physiques et morales",
    "title_en": "Physical & Moral Characteristics, Colors",
    "word_count": 40,
    "traps": [
        "Adjective agreement: Feminine adds silent '-e' (grand -> grande, petit -> petite). Irregular feminine: beau -> belle, nouveau -> nouvelle, vieux -> vieille.",
        "Colors: 'marron' and 'orange' are invariable (des chaussures marron, des robes orange).",
        "BAGS adjectives placed BEFORE the noun: Beauty, Age, Goodness, Size (un beau livre, un vieux monsieur, un grand appartement)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'E' MUET QUI RÉVEILLE LA CONSONNE",
        "phonetic_tip_text": "Au masculin, la consonne finale est silencieuse : grand [grahn], petit [puh-tee]. Au féminin, l'ajout du 'e' réveille la consonne : grande [grahnd], petite [puh-teet] !",
        "ex1_title": "Exercice 1.1 — Audit des Adjectifs Masculin vs Féminin [4 pts]",
        "ex1_headers": ["Adjectif", "Genre", "Consonne finale", "Son IPA A1", "Éveil phonétique"],
        "ex1_rows": [
            ["1. grand (m.)", "Masculin", "Consonne 'd' muette", "[ grahn ]", "Son [ɑ̃] nasal"],
            ["2. grande (f.)", "Féminin", "Consonne 'd' prononcée", "[ grahnd ]", "Consonne [d] articulée"],
            ["3. petit (m.)", "Masculin", "Consonne 't' muette", "[ puh-tee ]", "Son [i] pur"],
            ["4. petite (f.)", "Féminin", "Consonne 't' prononcée", "[ puh-teet ]", "Consonne [t] articulée"],
            ["5. gentil (m.)", "Masculin", "Consonne 'l' muette", "[ zhahn-tee ]", "Son [i] pur"],
            ["6. gentille (f.)", "Féminin", "Suffixe '-ille' liquide", "[ zhahn-teey ]", "Son [ij] liquide"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Adjectifs [3 pts]",
        "ex2_items": [
            "a) intelligent (f.) -> ________________________",
            "b) timide (m.) -> ________________________",
            "c) drole -> ________________________",
            "d) paresseux (f.) -> ________________________",
            "e) roux (f.) -> ________________________",
            "f) beau (f.) -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Adjectifs Antéposés [3 pts]",
        "ex3_items": [
            "1. un grand ami     -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
            "2. un petit homme   -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
            "3. un vieux monsieur -> [  ] Liaison                [  ] Pas de liaison",
            "4. un vieil homme   -> [  ] Liaison [l] sonore      [  ] Pas de liaison",
            "5. de beaux yeux    -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "6. une grande fille -> [  ] Liaison                 [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "ACCORD EN GENRE ET EN NOMBRE DES ADJECTIFS",
        "gender_rule_text": "L'adjectif qualificatif s'accorde toujours en genre et en nombre avec le nom qu'il qualifie. Les adjectifs terminés par un 'e' au masculin ne changent pas au féminin (timide, sympathique, drôle, jeune).",
        "ex1_title": "Exercice 2.1 — Matrice d'Accord Masculin / Féminin / Pluriel [6 pts]",
        "ex1_headers": ["Masculin Singulier", "Féminin Singulier", "Masculin Pluriel", "Féminin Pluriel"],
        "ex1_rows": [
            ["1. grand", "grande", "grands", "-> ___________________"],
            ["2. brun", "brune", "bruns", "-> ___________________"],
            ["3. beau", "belle", "beaux", "-> ___________________"],
            ["4. travailleur", "travailleuse", "travailleurs", "-> ___________________"],
            ["5. sérieux", "sérieuse", "sérieux", "-> ___________________"],
            ["6. blanc", "blanche", "blancs", "-> ___________________"]
        ],
        "ex2_title": "Exercice 2.2 — Détective d'Accord : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Ma sœur a acheté des chaussures marronnes très élégantes.\n   Correction : _____________________________________________________________________________",
            "2. Marie est une femme très beau et intelligent.\n   Correction : _____________________________________________________________________________",
            "3. Les étudiants de cette classe sont tous très travailleur.\n   Correction : _____________________________________________________________________________",
            "4. Il porte un pull vert et des pantalons noirs.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "LA POSITION DES ADJECTIFS : RÈGLE 'BAGS'",
        "colloc_tip_text": "En français, la plupart des adjectifs se placent APRÈS le nom (une robe rouge, un homme intelligent). Mais les adjectifs 'BAGS' (Beauty, Age, Goodness, Size : beau, joli, jeune, vieux, bon, mauvais, grand, petit) se placent AVANT le nom !",
        "ex1_title": "Exercice 3.1 — Placement de l'Adjectif (Avant vs Après le Nom) [5 pts]",
        "ex1_sentences": [
            "1. C'est une (belle / robe) ____________ ____________ que tu portes là !",
            "2. Mon oncle habite dans un (appartement / grand) ____________ ____________.",
            "3. Nous avons rencontré un (monsieur / vieux) ____________ ____________ dans le train.",
            "4. Elle a les (cheveux / noirs) ____________ ____________ et bouclés.",
            "5. C'est un (film / drôle) ____________ ____________ que nous avons adoré."
        ],
        "ex2_title": "Exercice 3.2 — Paires Traits Moraux & Comportements [5 pts]",
        "ex2_headers": ["Trait moral", "Comportement observé", "Association"],
        "ex2_rows": [
            ["1. Gentil(le)...", "A. travaille avec acharnement et rigueur", "1 -> [    ]"],
            ["2. Timide...", "B. aide volontiers les autres avec le sourire", "2 -> [    ]"],
            ["3. Travailleur(-euse)...", "C. n'aime pas parler devant un public inconnu", "3 -> [    ]"],
            ["4. Drôle...", "D. ne s'énerve jamais et prend son temps", "4 -> [    ]"],
            ["5. Patient(e)...", "E. fait rire tout son entourage avec humour", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE DESCRIPTION PHYSIQUE ET DE PERSONNALITÉ",
        "cloze_tip_text": "Complétez le portrait avec les adjectifs exacts en accordant obligatoirement le genre et le nombre.",
        "dialogues": [
            {
                "title": "Situation A — Décrire un nouvel ami à ses parents",
                "points": "3 pts",
                "lines": [
                    "• Maman : Comment est ton ami Thomas physiquement ?",
                    "• Hugo : Il est très ___________________________ [tall - m.] et il est ___________________________ [slim / thin]. Il a les cheveux ___________________________ [brown / dark-haired].",
                    "• Maman : Et moralement, il est sympa ?"
                ]
            },
            {
                "title": "Situation B — Portrait d'une collègue de bureau",
                "points": "4 pts",
                "lines": [
                    "• Julie : Tu connais la nouvelle directrice ?",
                    "• Marc : Oui, elle est très ___________________________ [kind / nice - f.] et extrêmement ___________________________ [intelligent / smart - f.].",
                    "• Julie : Elle est jeune ou ___________________________ [old - f.] ?",
                    "• Marc : Elle est assez ___________________________ [young - invariable]."
                ]
            },
            {
                "title": "Situation C — Choix d'une tenue vestimentaire par couleur",
                "points": "3 pts",
                "lines": [
                    "• Sophie : Quelle robe préfères-tu pour la soirée ?",
                    "• Léa : La robe ___________________________ [black - f.] ou la robe ___________________________ [red - f.] ?",
                    "• Sophie : Je préfère la noire avec des chaussures ___________________________ [brown - invariable !]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. My sister is small and very funny.", "-> __________________________________________________________________________________"],
            ["2. He has short hair and green eyes.", "-> __________________________________________________________________________________"],
            ["3. She is a beautiful and kind woman.", "-> __________________________________________________________________________________"],
            ["4. These students are hardworking and serious (m. pl.).", "-> __________________________________________________________________________________"],
            ["5. We have bought a big red car.", "-> __________________________________________________________________________________"],
            ["6. He is shy, but his brother is very outgoing / nice.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Grand  •  Petit  •  Gros  •  Sympathique",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Rouge  •  Bleu  •  Marron  •  Vert",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Beau  •  Vieux  •  Nouveau  •  Intelligent",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Drôle  •  Gentil  •  Patient  •  Blond",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. grand -> 'd' muet [grahn] | 2. grande -> 'd' articulé [grahnd] | 3. petit -> 't' muet [puh-tee] | 4. petite -> 't' articulé [puh-teet] | 5. gentil -> 'l' muet [zhahn-tee] | 6. gentille -> [zhahn-teey].\n\nExercice 1.2 — Orthographe [3 pts] :\na) intelligente | b) timide (invariable au masculin comme au féminin) | c) drôle (accent circonflexe sur 'ô') | d) paresseuse | e) rousse | f) belle.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un grand ami -> Liaison en [t] obligatoire [œ̃.gʁɑ̃.ta.mi] | 2. un petit homme -> Liaison en [t] [œ̃.pə.ti.tɔm] | 3. un vieux monsieur -> Pas de liaison | 4. un vieil homme -> Liaison en [l] [œ̃.vjɛ.jɔm] | 5. de beaux yeux -> Liaison en [z] [də.bo.zjø] | 6. une grande fille -> Pas de liaison devant consonne.",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. grandes | 2. brunes | 3. belles | 4. travailleuses | 5. sérieuses | 6. blanches.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'des chaussures MARRON' (marron est invariable en genre et en nombre).\n2. 'une femme très BELLE et INTELLIGENTE' (accords au féminin).\n3. 'très TRAVAILLEURS' (accord au pluriel avec les étudiants).\n4. 'un pull vert et un pantalon noir' (ou 'des pantalons noirs').",
        "tier3_text": "Exercice 3.1 — Placement [5 pts] :\n1. belle robe (BAGS : Beauty -> avant) | 2. grand appartement (BAGS : Size -> avant) | 3. vieux monsieur (BAGS : Age -> avant) | 4. cheveux noirs (Couleur -> après) | 5. film drôle (Adjectif long/moral -> après).\n\nExercice 3.2 — Paires Traits Moraux [5 pts] :\n1 -> B (Gentille aide avec le sourire) | 2 -> C (Timide n'aime pas parler en public) | 3 -> A (Travailleur s'acharne au travail) | 4 -> E (Drôle fait rire) | 5 -> D (Patient ne s'énerve jamais).",
        "tier4_text": "Situation A (3 pts) : grand | mince | bruns.\nSituation B (4 pts) : gentille | intelligente | vieille | jeune.\nSituation C (3 pts) : noire | rouge | marron.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Ma sœur est petite et très drôle.\n2. Il a les cheveux courts et les yeux verts.\n3. C'est une belle et gentille femme.\n4. Ces étudiants sont travailleurs et sérieux.\n5. Nous avons acheté une grande voiture rouge.\n6. Il est timide, mais son frère est très sympa / sociable.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Sympathique (trait moral / personnalité, les 3 autres sont des caractéristiques physiques de taille/corpulence).\n2. Marron (adjectif de couleur invariable ne prenant jamais de 's', les 3 autres s'accordent en nombre).\n3. Intelligent (adjectif placé APRÈS le nom, les 3 autres sont des adjectifs BAGS placés AVANT le nom).\n4. Blond (caractéristique physique de couleur de cheveux, les 3 autres sont des traits de caractère moraux).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 5",
        "anchors_text": "1. Les adjectifs de couleur invariables : 'Marron' et 'Orange' dérivent de noms de fruits/graines et sont donc INVARIABLES (des yeux marron, des chemises orange).\n2. La règle BAGS : Beauty (beau, joli), Age (jeune, vieux, nouveau), Goodness (bon, mauvais), Size (grand, petit) se placent TOUJOURS AVANT le nom en français !\n3. Le trio irrégulier : beau -> bel (devant voyelle) -> belle ; vieux -> vieil -> vieille ; nouveau -> nouvel -> nouvelle."
    }
}

with open("chapters_batch_1.json", "w", encoding="utf-8") as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print("Saved chapters 4 and 5 to JSON.")
