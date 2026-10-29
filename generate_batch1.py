import json

batch1 = {}

# -------------------------------------------------------------
# CHAPTER 1
# -------------------------------------------------------------
batch1["1"] = {
    "ch_num": 1,
    "title_fr": "Les présentations et les salutations",
    "title_en": "Greetings, Politeness & Identity",
    "word_count": 42,
    "traps": [
        "Silent final 't' in 'salut' [sah-lyoo] vs pronounced 't' in English 'salute'.",
        "Nasal vowels in 'bonjour' [ohn], 'bien' [yanh], 'rien' [yanh], 'enchanté' [ahn].",
        "Tu vs Vous distinction: 'S'il te plaît' (friends/peers) vs 'S'il vous plaît' (elders/clerks)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'T' FINAL SILENCIEUX ET LES NASALES",
        "phonetic_tip_text": "En français, la plupart des consonnes finales sont silencieuses (salut, comment, plaît, vous). La terminaison 'en'/'an'/'on' produit un son nasal par le nez, sans articulation linguale de la lettre 'n'.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique & Décodage des Salutations [4 pts]",
        "ex1_headers": ["Expression", "Consonne finale", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. Salut !", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ sah-lyoo ]"],
            ["2. Comment ça va ?", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ koh-mahn sah vah ]"],
            ["3. S'il vous plaît", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ seel voo pleh ]"],
            ["4. Bonsoir", "Consonne 'r'", "[  ] Oui", "[  ] Oui", "[ bohn-swahr ]"],
            ["5. Enchanté(e)", "Voyelle nasale 'en'", "[  ] Nasale [ɑ̃]", "[  ] Orale [an]", "[ ahn-shahn-tay ]"],
            ["6. De rien", "Voyelle nasale 'ien'", "[  ] Nasale [ɛ̃]", "[  ] Orale [jɛn]", "[ duh ryanh ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) enchante (m.) -> ________________________",
            "b) a bientot -> ________________________",
            "c) s'il vous plait -> ________________________",
            "d) le prenom -> ________________________",
            "e) tres bien -> ________________________",
            "f) ca va -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Obligatoires [3 pts]",
        "ex3_items": [
            "1. Comment allez-vous ? -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
            "2. Je vous en prie      -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "3. Vous vous appelez    -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
            "4. Au revoir            -> [  ] Liaison                 [  ] Pas de liaison",
            "5. Un ami               -> [  ] Liaison [n] sonore      [  ] Pas de liaison",
            "6. Salut Paul           -> [  ] Liaison                 [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES TITRES & DE L'ÉTAT CIVIL",
        "gender_rule_text": "Tous les substantifs d'identité requièrent un article : le prénom, le nom, la signature, la nationalité. Ne jamais employer un terme d'identité isolé.",
        "ex1_title": "Exercice 2.1 — Matrice des Titres et Documents d'Identité [6 pts]",
        "ex1_headers": ["Masculin / Neutre", "Féminin correspondant", "Article défini (le/la/l')", "Sens en anglais"],
        "ex1_rows": [
            ["1. Monsieur", "-> ___________________", "[    ] Monsieur", "Mr. / Sir"],
            ["2. Un garçon", "-> ___________________", "[    ] fille", "Boy / Girl"],
            ["3. Un ami", "-> ___________________", "[    ] ami(e)", "Friend (m./f.)"],
            ["4. Le prénom", "-> (invariable neutre)", "[    ] prénom", "First name"],
            ["5. Le nom de famille", "-> (invariable neutre)", "[    ] nom", "Last name / Surname"],
            ["6. Le sexe masculin", "-> ___________________", "[    ] sexe féminin", "Sex / Gender (M/F)"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Voici mon nouveau amie française, elle s'appelle Chloé.\n   Correction : _____________________________________________________________________________",
            "2. Quel est votre signature sur le formulaire officiel ?\n   Correction : _____________________________________________________________________________",
            "3. Je vous présente le dame du bureau numéro 4.\n   Correction : _____________________________________________________________________________",
            "4. Mon prénom est Marc et mon nom de famille est une Dupont.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE POLITESSE & D'ACCUEIL",
        "colloc_tip_text": "En France, on ne dit pas seulement 'bonjour' : on l'associe toujours au titre de civilité ('Bonjour Madame / Monsieur'). Pour remercier : 'Merci beaucoup', et en réponse formelle : 'Je vous en prie'.",
        "ex1_title": "Exercice 3.1 — Chunks Communicatifs et Formules de Politesse [5 pts]",
        "ex1_sentences": [
            "1. En entrant dans une boulangerie le matin, on dit : 'Bonjour ___________' (Madame/Monsieur).",
            "2. Pour demander poliment l'addition au serveur : 'L'addition, s'il ___________ plaît.'",
            "3. Après avoir reçu de l'aide, on remercie chaleureusement : 'Merci ___________ !'",
            "4. En réponse polie et formelle à un remerciement : 'Je vous en ___________.'",
            "5. Avant de quitter des amis qu'on reverra dans deux jours : 'À ___________ !'"
        ],
        "ex2_title": "Exercice 3.2 — Paires Verbe-Identité Authentiques [5 pts]",
        "ex2_headers": ["Verbe / Formule", "Complément d'identité", "Association"],
        "ex2_rows": [
            ["1. S'appeler...", "A. son prénom lettre par lettre", "1 -> [    ]"],
            ["2. Épeler...", "B. par son nom de famille", "2 -> [    ]"],
            ["3. Présenter...", "C. Pierre Martin", "3 -> [    ]"],
            ["4. Donner...", "D. un collègue à son directeur", "4 -> [    ]"],
            ["5. Saluer...", "E. ses coordonnées téléphoniques", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE SANS BANQUE DE MOTS",
        "cloze_tip_text": "Complétez les répliques en récupérant directement la structure française exacte exigée par l'indice contextuel en anglais.",
        "dialogues": [
            {
                "title": "Situation A — Au guichet d'accueil (Formal Interaction)",
                "points": "3 pts",
                "lines": [
                    "• L'employé : Bonjour Monsieur. Comment vous vous ___________________________ [is your name - formal] ?",
                    "• Le client : Bonjour. Je ___________________________ [my name is] Alexandre Mercier.",
                    "• L'employé : Parfait. Vous pouvez ___________________________ [spell] votre nom de famille, s'il vous plaît ?"
                ]
            },
            {
                "title": "Situation B — Rencontre informelle entre étudiants",
                "points": "4 pts",
                "lines": [
                    "• Lucas : ___________________________ [Hi - informal] ! Moi, c'est Lucas. Et toi ?",
                    "• Camille : Salut Lucas ! Je m'appelle Camille. ___________________________ [Nice to meet you] !",
                    "• Lucas : Comment ça ___________________________ [is it going] aujourd'hui ?",
                    "• Camille : Ça va très bien, ___________________________ [thank you very much] !"
                ]
            },
            {
                "title": "Situation C — Prendre congé à la fin d'un rendez-vous",
                "points": "3 pts",
                "lines": [
                    "• Mme Martin : Merci pour votre visite, Monsieur Dubois.",
                    "• M. Dubois : C'est moi qui vous remercie. ___________________________ [Goodbye] Madame, et à ___________________________ [see you soon] !",
                    "• Mme Martin : ___________________________ [Have a good day] !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. What is your name? (polite / formal with 'vous')", "-> __________________________________________________________________________________"],
            ["2. Have a good evening and see you tomorrow!", "-> __________________________________________________________________________________"],
            ["3. You're welcome (formal expression).", "-> __________________________________________________________________________________"],
            ["4. My first name is Julien and my last name is Laurent.", "-> __________________________________________________________________________________"],
            ["5. Nice to meet you (spoken by a woman).", "-> __________________________________________________________________________________"],
            ["6. Please (informal, speaking to a classmate).", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Bonjour  •  Bonsoir  •  Merci  •  Salut",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. S'il vous plaît  •  De rien  •  Je vous en prie  •  Avec plaisir",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le prénom  •  Le nom  •  La signature  •  La boulangerie",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. À bientôt  •  Au revoir  •  Bonjour  •  À demain",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. Salut -> 't' muet [sah-lyoo] | 2. Comment -> 't' muet [koh-mahn] | 3. Plaît -> 't' muet [pleh] | 4. Bonsoir -> 'r' prononcé [bohn-swahr] (règle C-R-F-L) | 5. Enchanté -> nasale [ɑ̃] | 6. De rien -> nasale [ɛ̃].\n\nExercice 1.2 — Orthographe [3 pts] :\na) enchanté | b) à bientôt (accent grave sur à, circonflexe sur ô) | c) s'il vous plaît (circonflexe sur î) | d) le prénom (accent aigu) | e) très bien (accent grave) | f) ça va (cédille ç).\n\nExercice 1.3 — Liaisons [3 pts] :\n1. Comment allez-vous ? -> Liaison en [t] obligatoire | 2. Je vous en prie -> Liaison en [z] | 3. Vous vous appelez -> Liaison en [z] | 4. Au revoir -> Pas de liaison | 5. Un ami -> Liaison en [n] | 6. Salut Paul -> Pas de liaison.",
        "tier2_text": "Exercice 2.1 — Matrice d'Identité [6 pts] :\n1. Madame / Le Monsieur | 2. Une fille / Le garçon | 3. Une amie / L'ami | 4. Le prénom | 5. Le nom de famille | 6. Le sexe féminin / Le sexe masculin.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'Voici mon amie' (devant voyelle, 'mon' remplace 'ma' pour éviter le choc vocalique : mon amie, pas mon nouveau amie -> ma nouvelle amie).\n2. 'Quelle est votre signature' (signature est féminin : la signature).\n3. 'la dame' (dame est féminin : la dame).\n4. 'mon nom de famille est Dupont' (pas d'article indéfini devant un nom propre de famille).",
        "tier3_text": "Exercice 3.1 — Chunks de Politesse [5 pts] :\n1. Madame / Monsieur | 2. vous | 3. beaucoup | 4. prie | 5. bientôt (ou à demain).\n\nExercice 3.2 — Paires Verbe-Nom [5 pts] :\n1 -> C (S'appeler Pierre Martin) | 2 -> A (Épeler son prénom) | 3 -> D (Présenter un collègue) | 4 -> E (Donner ses coordonnées) | 5 -> B (Saluer par son nom).",
        "tier4_text": "Situation A (3 pts) : vous appelez | m'appelle | épeler.\nSituation B (4 pts) : Salut | Enchantée (ou Enchanté) | va | merci beaucoup.\nSituation C (3 pts) : Au revoir | bientôt (ou demain) | Bonne journée !",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Comment vous vous appelez ? (ou : Quel est votre nom ?)\n2. Bonne soirée et à demain !\n3. Je vous en prie. (ou : De rien.)\n4. Mon prénom est Julien et mon nom de famille est Laurent.\n5. Enchantée !\n6. S'il te plaît.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Merci (expression de remerciement, les 3 autres sont des salutations).\n2. S'il vous plaît (demande polie, les 3 autres sont des réponses à un remerciement).\n3. La boulangerie (lieu de commerce, les 3 autres sont des rubriques d'identité civile).\n4. Bonjour (salutation d'arrivée, les 3 autres sont des formules de départ/adieu).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 1",
        "anchors_text": "1. La politesse du commerçant : En France, il est impoli de ne pas dire 'Bonjour Madame/Monsieur' en franchissant le pas d'une boutique ou d'un café.\n2. Le choc vocalique 'Mon amie' : Même si 'amie' est féminin, on dit 'mon amie' (et non 'ma amie') pour des raisons d'euphonie (éviter l'hiatus vocalique).\n3. Tu vs Vous : Utilisez systématiquement 'vous' avec toute personne adulte inconnue, tout professionnel ou tout supérieur hiérarchique."
    }
}

with open("chapters_batch_1.json", "w", encoding="utf-8") as f:
    json.dump(batch1, f, ensure_ascii=False, indent=2)

print("chapters_batch_1.json started with Ch 1.")
