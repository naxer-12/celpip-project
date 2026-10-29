import os

batch1_code = '''# -*- coding: utf-8 -*-
"""
Curriculum Batch 1: Chapters 01 to 11
Exhaustive vocabulary, phonetic anchors, gender bindings, collocations, dialogues, and answer keys.
"""

BATCH_1 = {
    1: {
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
                ("1. Salut !", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ sah-lyoo ]"),
                ("2. Comment ça va ?", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ koh-mahn sah vah ]"),
                ("3. S'il vous plaît", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ seel voo pleh ]"),
                ("4. Bonsoir", "Consonne 'r'", "[  ] Oui", "[  ] Oui", "[ bohn-swahr ]"),
                ("5. Enchanté(e)", "Voyelle nasale 'en'", "[  ] Nasale [ɑ̃]", "[  ] Orale [an]", "[ ahn-shahn-tay ]"),
                ("6. De rien", "Voyelle nasale 'ien'", "[  ] Nasale [ɛ̃]", "[  ] Orale [jɛn]", "[ duh ryanh ]"),
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
                ("1. Monsieur", "-> ___________________", "[    ] Monsieur", "Mr. / Sir"),
                ("2. Un garçon", "-> ___________________", "[    ] fille", "Boy / Girl"),
                ("3. Un ami", "-> ___________________", "[    ] ami(e)", "Friend (m./f.)"),
                ("4. Le prénom", "-> (invariable neutre)", "[    ] prénom", "First name"),
                ("5. Le nom de famille", "-> (invariable neutre)", "[    ] nom", "Last name / Surname"),
                ("6. Le sexe masculin", "-> ___________________", "[    ] sexe féminin", "Sex / Gender (M/F)"),
            ],
            "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
            "ex2_sentences": [
                "1. Voici mon nouveau amie française, elle s'appelle Chloé.\\n   Correction : _____________________________________________________________________________",
                "2. Quel est votre signature sur le formulaire officiel ?\\n   Correction : _____________________________________________________________________________",
                "3. Je vous présente le dame du bureau numéro 4.\\n   Correction : _____________________________________________________________________________",
                "4. Mon prénom est Marc et mon nom de famille est une Dupont.\\n   Correction : _____________________________________________________________________________"
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
                ("1. S'appeler...", "A. son prénom lettre par lettre", "1 -> [    ]"),
                ("2. Épeler...", "B. par son nom de famille", "2 -> [    ]"),
                ("3. Présenter...", "C. Pierre Martin", "3 -> [    ]"),
                ("4. Donner...", "D. un collègue à son directeur", "4 -> [    ]"),
                ("5. Saluer...", "E. ses coordonnées téléphoniques", "5 -> [    ]"),
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
                ("1. What is your name? (polite / formal with 'vous')", "-> __________________________________________________________________________________"),
                ("2. Have a good evening and see you tomorrow!", "-> __________________________________________________________________________________"),
                ("3. You're welcome (formal expression).", "-> __________________________________________________________________________________"),
                ("4. My first name is Julien and my last name is Laurent.", "-> __________________________________________________________________________________"),
                ("5. Nice to meet you (spoken by a woman).", "-> __________________________________________________________________________________"),
                ("6. Please (informal, speaking to a classmate).", "-> __________________________________________________________________________________"),
            ],
            "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
            "ex2_intrus": [
                ("1. Bonjour  •  Bonsoir  •  Merci  •  Salut",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("2. S'il vous plaît  •  De rien  •  Je vous en prie  •  Avec plaisir",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("3. Le prénom  •  Le nom  •  La signature  •  La boulangerie",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("4. À bientôt  •  Au revoir  •  Bonjour  •  À demain",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
            ]
        },
        "corrige": {
            "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\\n1. Salut -> 't' muet [sah-lyoo] | 2. Comment -> 't' muet [koh-mahn] | 3. Plaît -> 't' muet [pleh] | 4. Bonsoir -> 'r' prononcé [bohn-swahr] (règle C-R-F-L) | 5. Enchanté -> nasale [ɑ̃] | 6. De rien -> nasale [ɛ̃].\\n\\nExercice 1.2 — Orthographe [3 pts] :\\na) enchanté | b) à bientôt (accent grave sur à, circonflexe sur ô) | c) s'il vous plaît (circonflexe sur î) | d) le prénom (accent aigu) | e) très bien (accent grave) | f) ça va (cédille ç).\\n\\nExercice 1.3 — Liaisons [3 pts] :\\n1. Comment allez-vous ? -> Liaison en [t] obligatoire | 2. Je vous en prie -> Liaison en [z] | 3. Vous vous appelez -> Liaison en [z] | 4. Au revoir -> Pas de liaison | 5. Un ami -> Liaison en [n] | 6. Salut Paul -> Pas de liaison.",
            "tier2_text": "Exercice 2.1 — Matrice d'Identité [6 pts] :\\n1. Madame / Le Monsieur | 2. Une fille / Le garçon | 3. Une amie / L'ami | 4. Le prénom | 5. Le nom de famille | 6. Le sexe féminin / Le sexe masculin.\\n\\nExercice 2.2 — Détective [4 pts] :\\n1. 'Voici mon amie' (devant voyelle, 'mon' remplace 'ma' pour éviter le choc vocalique : mon amie, pas mon nouveau amie -> ma nouvelle amie).\\n2. 'Quelle est votre signature' (signature est féminin : la signature).\\n3. 'la dame' (dame est féminin : la dame).\\n4. 'mon nom de famille est Dupont' (pas d'article indéfini devant un nom propre de famille).",
            "tier3_text": "Exercice 3.1 — Chunks de Politesse [5 pts] :\\n1. Madame / Monsieur | 2. vous | 3. beaucoup | 4. prie | 5. bientôt (ou à demain).\\n\\nExercice 3.2 — Paires Verbe-Nom [5 pts] :\\n1 -> C (S'appeler Pierre Martin) | 2 -> A (Épeler son prénom) | 3 -> D (Présenter un collègue) | 4 -> E (Donner ses coordonnées) | 5 -> B (Saluer par son nom).",
            "tier4_text": "Situation A (3 pts) : vous appelez | m'appelle | épeler.\\nSituation B (4 pts) : Salut | Enchantée (ou Enchanté) | va | merci beaucoup.\\nSituation C (3 pts) : Au revoir | bientôt (ou demain) | Bonne journée !",
            "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\\n1. Comment vous vous appelez ? (ou : Quel est votre nom ?)\\n2. Bonne soirée et à demain !\\n3. Je vous en prie. (ou : De rien.)\\n4. Mon prénom est Julien et mon nom de famille est Laurent.\\n5. Enchantée !\\n6. S'il te plaît.\\n\\nExercice 5.2 — L'Intrus [4 pts] :\\n1. Merci (expression de remerciement, les 3 autres sont des salutations).\\n2. S'il vous plaît (demande polie, les 3 autres sont des réponses à un remerciement).\\n3. La boulangerie (lieu de commerce, les 3 autres sont des rubriques d'identité civile).\\n4. Bonjour (salutation d'arrivée, les 3 autres sont des formules de départ/adieu).",
            "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 1",
            "anchors_text": "1. La politesse du commerçant : En France, il est impoli de ne pas dire 'Bonjour Madame/Monsieur' en franchissant le pas d'une boutique ou d'un café.\\n2. Le choc vocalique 'Mon amie' : Même si 'amie' est féminin, on dit 'mon amie' (et non 'ma amie') pour des raisons d'euphonie (éviter l'hiatus vocalique).\\n3. Tu vs Vous : Utilisez systématiquement 'vous' avec toute personne adulte inconnue, tout professionnel ou tout supérieur hiérarchique."
        }
    },

    2: {
        "ch_num": 2,
        "title_fr": "La date et le lieu de naissance",
        "title_en": "Numbers 0–100, Months, Seasons & Birthdays",
        "word_count": 48,
        "traps": [
            "Celtic Base-20 vigesimal system: 70 = soixante-dix (60+10), 80 = quatre-vingts (4x20), 90 = quatre-vingt-dix (4x20+10).",
            "The 'et-un' rule: 21 (vingt-et-un), 71 (soixante-et-onze), but 81 (quatre-vingt-un without 'et'!).",
            "Prepositions with months/seasons: 'en mai', 'en hiver', BUT 'au printemps'!"
        ],
        "target_time": "35 min",
        "total_marks": 50,
        "passing_mark": "80% (40/50)",
        "tier1": {
            "phonetic_tip_title": "PRONONCIATION DES CHIFFRES ET VOYELLES NASALES",
            "phonetic_tip_text": "Dans les nombres : 'sept' [set] a un 'p' muet silencieux. 'Huit' [weet] a un 'h' aspiré qui bloque l'élision. 'Vingt' [vanh] a 'gt' muets, sauf en liaison (vingt-deux [vant-duh]).",
            "ex1_title": "Exercice 1.1 — Audit Phonétique des Nombres & Mois [4 pts]",
            "ex1_headers": ["Terme chiffré", "Lettre / Piège", "Prononcée ?", "Muette ?", "Transcription A1"],
            "ex1_rows": [
                ("1. sept (7)", "Consonne 'p'", "[  ] Oui", "[  ] Oui", "[ set ]"),
                ("2. vingt (20)", "Consonnes 'gt'", "[  ] Oui", "[  ] Oui", "[ vanh ]"),
                ("3. huit (8)", "Consonne 't'", "[  ] Oui", "[  ] Oui", "[ weet ]"),
                ("4. juin (06)", "Voyelle nasale 'in'", "[  ] Nasale [ɛ̃]", "[  ] Orale [yn]", "[ zhwanh ]"),
                ("5. août (08)", "Diphtongue 'août'", "[  ] [oot]", "[  ] [ah-oo]", "[ oot ]"),
                ("6. printemps (m.)", "Consonnes 'mps'", "[  ] Oui", "[  ] Oui", "[ pranh-tahn ]"),
            ],
            "ex2_title": "Exercice 1.2 — Rectification Orthographique des Mois & Nombres [3 pts]",
            "ex2_items": [
                "a) zero -> ________________________",
                "b) fevrier -> ________________________",
                "c) aout -> ________________________",
                "d) decembre -> ________________________",
                "e) soixante-dix-huit -> ________________________",
                "f) quatre-vingts -> ________________________"
            ],
            "ex3_title": "Exercice 1.3 — Détection des Liaisons Numériques [3 pts]",
            "ex3_items": [
                "1. dix-huit ans     -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
                "2. neuf heures      -> [  ] Liaison [v] sonore      [  ] Pas de liaison",
                "3. six enfants      -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
                "4. quatre ans       -> [  ] Liaison [ʁ] sonore      [  ] Pas de liaison",
                "5. cent euros       -> [  ] Liaison [t] sonore      [  ] Pas de liaison",
                "6. deux mois        -> [  ] Liaison                 [  ] Pas de liaison"
            ]
        },
        "tier2": {
            "gender_rule_title": "LE GENRE DES MOIS, SAISONS ET DATES",
            "gender_rule_text": "Tous les mois de l'année et toutes les saisons sont MASCULINS en français (le mois de janvier, le printemps, l'été, l'automne, l'hiver). Pour la date, on utilise toujours l'article masculin 'le' : 'le 14 juillet'.",
            "ex1_title": "Exercice 2.1 — Matrice des Mois, Saisons et Articles [6 pts]",
            "ex1_headers": ["Saison / Période", "Article défini (le/l')", "Préposition temporelle", "Sens anglais"],
            "ex1_rows": [
                ("1. Printemps", "-> [    ] printemps", "-> [    ] printemps", "Spring / In spring"),
                ("2. Été", "-> [    ] été", "-> [    ] été", "Summer / In summer"),
                ("3. Automne", "-> [    ] automne", "-> [    ] automne", "Autumn / In autumn"),
                ("4. Hiver", "-> [    ] hiver", "-> [    ] hiver", "Winter / In winter"),
                ("5. Date du jour", "-> [    ] premier mai", "-> [    ] 1er mai", "The 1st of May"),
                ("6. Année de naissance", "-> [    ] année (f.)", "-> [    ] 1995", "Year / In 1995"),
            ],
            "ex2_title": "Exercice 2.2 — Détective de Genre & Dates : Repérez l'Erreur [4 pts]",
            "ex2_sentences": [
                "1. Je suis né en le printemps, le 15 avril.\\n   Correction : _____________________________________________________________________________",
                "2. La réunion aura lieu sur le deux juin.\\n   Correction : _____________________________________________________________________________",
                "3. Mon anniversaire est la premier octobre.\\n   Correction : _____________________________________________________________________________",
                "4. En France, le automne commence fin septembre.\\n   Correction : _____________________________________________________________________________"
            ]
        },
        "tier3": {
            "colloc_tip_title": "COLLOCATIONS D'ÂGE ET DE NAISSANCE (AVOIR VS ÊTRE)",
            "colloc_tip_text": "En français, on N'EST PAS son âge, ON A son âge ! Utilisez le verbe AVOIR : 'J'ai 25 ans' (et non 'Je suis 25'). Pour la naissance : 'Je suis né(e) le...' avec le verbe ÊTRE.",
            "ex1_title": "Exercice 3.1 — Prépositions Temporelles (EN vs AU vs LE) [5 pts]",
            "ex1_sentences": [
                "1. Mon frère fête son anniversaire ________ (le / en) 12 juillet.",
                "2. Nous partons en vacances à la mer ________ (en / au) été.",
                "3. Les fleurs s'épanouissent magnifiquement ________ (au / en) printemps.",
                "4. Elle est née ________ (en / au) décembre 1998.",
                "5. Aujourd'hui, nous sommes ________ (le / en) mardi 4 octobre."
            ],
            "ex2_title": "Exercice 3.2 — Paires Verbe-Âge & État Civil [5 pts]",
            "ex2_headers": ["Verbe", "Expression d'âge / Date", "Association"],
            "ex2_rows": [
                ("1. Avoir...", "A. son certificat de naissance à la mairie", "1 -> [    ]"),
                ("2. Être né(e)...", "B. 30 ans le mois prochain", "2 -> [    ]"),
                ("3. Fêter...", "C. le 28 février à Marseille", "3 -> [    ]"),
                ("4. Demander...", "D. son anniversaire en famille", "4 -> [    ]"),
                ("5. Présenter...", "E. la date de naissance d'un candidat", "5 -> [    ]"),
            ]
        },
        "tier4": {
            "cloze_tip_title": "CLOZE D'ÉTAT CIVIL ET D'ÂGE",
            "cloze_tip_text": "Complétez avec les expressions de date, d'âge et de mois exactes sans oublier le mot 'ans' après les chiffres !",
            "dialogues": [
                {
                    "title": "Situation A — Au bureau des inscriptions administratives",
                    "points": "3 pts",
                    "lines": [
                        "• L'agent : Quelle est votre date de ___________________________ [birth - f.] ?",
                        "• Marc : Je suis ___________________________ [born - m.] le 14 ___________________________ [July] 1995.",
                        "• L'agent : Quel âge ___________________________ [do you have / are you] ?"
                    ]
                },
                {
                    "title": "Situation B — Discussion entre amis sur les vacances",
                    "points": "4 pts",
                    "lines": [
                        "• Sarah : En quelle saison préfères-tu voyager ?",
                        "• David : J'adore partir ___________________________ [in summer] ou ___________________________ [in spring].",
                        "• Sarah : Et pendant ___________________________ [winter], tu fais du ski ?",
                        "• David : Oui, souvent en ___________________________ [January] ou en février."
                    ]
                },
                {
                    "title": "Situation C — Compter et donner son numéro de téléphone",
                    "points": "3 pts",
                    "lines": [
                        "• Julie : Quel est ton numéro de téléphone ?",
                        "• Paul : C'est le 06 ___________________________ [72 - soixante-douze] ___________________________ [84 - quatre-vingt-quatre] ___________________________ [91 - quatre-vingt-onze]."
                    ]
                }
            ]
        },
        "tier5": {
            "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
            "ex1_prompts": [
                ("1. I am 24 years old. (Attention: verbe avoir !)", "-> __________________________________________________________________________________"),
                ("2. She was born on the 1st of May in Paris.", "-> __________________________________________________________________________________"),
                ("3. In France, school starts in September.", "-> __________________________________________________________________________________"),
                ("4. My grandfather is eighty-five years old.", "-> __________________________________________________________________________________"),
                ("5. What is the date today? - Today is Thursday, October 9th.", "-> __________________________________________________________________________________"),
                ("6. We go to the mountains in autumn.", "-> __________________________________________________________________________________"),
            ],
            "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
            "ex2_intrus": [
                ("1. Janvier  •  Février  •  Printemps  •  Mars",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("2. Soixante-dix  •  Quatre-vingts  •  Quatre-vingt-dix  •  Cinquante",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("3. En été  •  En hiver  •  Au printemps  •  En automne",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("4. Dix  •  Vingt  •  Trente  •  Lundi",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
            ]
        },
        "corrige": {
            "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\\n1. sept -> 'p' muet [set] | 2. vingt -> 'gt' muets [vanh] | 3. huit -> 't' prononcé [weet] | 4. juin -> nasale [ɛ̃] | 5. août -> [oot] | 6. printemps -> 'mps' muets [pranh-tahn].\\n\\nExercice 1.2 — Orthographe [3 pts] :\\na) zéro | b) février | c) août (ou aout rectif. 1990) | d) décembre | e) soixante-dix-huit | f) quatre-vingts (prend un 's' car multiplié et termine le nombre).\\n\\nExercice 1.3 — Liaisons [3 pts] :\\n1. dix-huit ans -> Liaison en [z] | 2. neuf heures -> Liaison en [v] (neuf ans / neuf heures) | 3. six enfants -> Liaison en [z] | 4. quatre ans -> Enchaînement [ʁ] | 5. cent euros -> Liaison en [t] | 6. deux mois -> Pas de liaison devant consonne.",
            "tier2_text": "Exercice 2.1 — Matrice des Saisons [6 pts] :\\n1. Le printemps / au printemps | 2. L'été / en été | 3. L'automne / en automne | 4. L'hiver / en hiver | 5. Le premier mai / le 1er mai | 6. L'année / en 1995.\\n\\nExercice 2.2 — Détective [4 pts] :\\n1. 'au printemps' (et non 'en le printemps').\\n2. 'le deux juin' (sans 'sur').\\n3. 'LE premier octobre' (la date est toujours masculine).\\n4. 'L'automne' (élision obligatoire devant voyelle : l'automne).",
            "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\\n1. le | 2. en | 3. au | 4. en | 5. le.\\n\\nExercice 3.2 — Paires Verbe-Nom [5 pts] :\\n1 -> B (Avoir 30 ans) | 2 -> C (Être né le 28 février) | 3 -> D (Fêter son anniversaire) | 4 -> E (Demander la date de naissance) | 5 -> A (Présenter son certificat).",
            "tier4_text": "Situation A (3 pts) : naissance | né | juillet | avez-vous.\\nSituation B (4 pts) : en été | au printemps | l'hiver | janvier.\\nSituation C (3 pts) : soixante-douze | quatre-vingt-quatre | quatre-vingt-onze.",
            "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\\n1. J'ai 24 ans. (Ne jamais oublier 'ans' !)\\n2. Elle est née le 1er mai à Paris.\\n3. En France, la rentrée scolaire est en septembre.\\n4. Mon grand-père a quatre-vingt-cinq ans.\\n5. Quelle est la date aujourd'hui ? - Aujourd'hui, nous sommes le jeudi 9 octobre.\\n6. Nous allons à la montagne en automne.\\n\\nExercice 5.2 — L'Intrus [4 pts] :\\n1. Printemps (c'est une saison, les 3 autres sont des mois).\\n2. Cinquante (système décimal standard, les 3 autres utilisent le système vigésimal en base 20).\\n3. Au printemps (utilise la préposition 'au', les 3 autres utilisent 'en').\\n4. Lundi (c'est un jour de la semaine, les 3 autres sont des dizaines de nombres).",
            "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 2",
            "anchors_text": "1. Le piège de l'âge : En anglais, 'I AM 20'. En français, 'J'AI 20 ANS'. L'omission de 'ans' est incorrecte en français.\\n2. Le système celtique vigésimal : 70 = 60+10, 80 = 4x20, 90 = 4x20+10. Retenez que seul 80 prend un 's' (quatre-vingts), qui disparaît dès qu'un chiffre suit (quatre-vingt-un).\\n3. Les prépositions de saison : Retenez la règle d'or 'Au printemps', mais 'En été', 'En automne', 'En hiver' (car ces trois saisons commencent par une voyelle)."
        }
    },

    3: {
        "ch_num": 3,
        "title_fr": "La nationalité et l'adresse",
        "title_en": "Countries, Nationalities & Addresses",
        "word_count": 45,
        "traps": [
            "Country prepositions rule: Feminine countries take 'en' (en France, en Espagne). Masculine countries take 'au' (au Canada, au Japon). Plural countries take 'aux' (aux États-Unis).",
            "Nationalities as adjectives take lowercase in French (il est français), but capitalized when referring to the person as a proper noun (un Français).",
            "French address format: Number first, then road type, then name: '12, rue de la Paix', followed by a 5-digit postal code '75002 Paris'."
        ],
        "target_time": "30–35 min",
        "total_marks": 50,
        "passing_mark": "80% (40/50)",
        "tier1": {
            "phonetic_tip_title": "ACCORD PHONÉTIQUE DES NATIONALITÉS (MASCULIN VS FÉMININ)",
            "phonetic_tip_text": "Au masculin, la plupart des nationalités se terminent par une consonne muette ou une voyelle nasale : français [frahn-seh], espagnol [es-pah-nyohl], américain [ah-may-ree-kanh]. Au féminin, le 'e' réveille la consonne : française [frahn-sez], américaine [ah-may-ree-ken] !",
            "ex1_title": "Exercice 1.1 — Audit des Sons Masculin / Féminin des Nationalités [4 pts]",
            "ex1_headers": ["Nationalité", "Forme ciblée", "Consonne finale", "Son IPA A1", "Shift de son"],
            "ex1_rows": [
                ("1. français (m.)", "Masculin", "Consonne 's' muette", "[ frahn-seh ]", "Son [ɛ] fermé"),
                ("2. française (f.)", "Féminin", "Consonne 's' prononcée [z]", "[ frahn-sez ]", "Son [ɛz] voisé"),
                ("3. italien (m.)", "Masculin", "Voyelle nasale '-ien'", "[ ee-tah-lyanh ]", "Nasale [ɛ̃] pure"),
                ("4. italienne (f.)", "Féminin", "Dénasalisation '-ienne'", "[ ee-tah-lyen ]", "Orale [ɛn] claire"),
                ("5. allemand (m.)", "Masculin", "Consonne 'd' muette", "[ ahl-mahn ]", "Son [ɑ̃] nasal"),
                ("6. allemande (f.)", "Féminin", "Consonne 'd' prononcée", "[ ahl-mahnd ]", "Consonne [d] articulée"),
            ],
            "ex2_title": "Exercice 1.2 — Rectification Orthographique & Adresses [3 pts]",
            "ex2_items": [
                "a) un americain -> ________________________",
                "b) une bresilienne -> ________________________",
                "c) la Grece -> ________________________",
                "d) un numero de rue -> ________________________",
                "e) le code postale -> ________________________",
                "f) l'Espagne -> ________________________"
            ],
            "ex3_title": "Exercice 1.3 — Détection des Liaisons avec les Pays Pluriels [3 pts]",
            "ex3_items": [
                "1. aux États-Unis   -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
                "2. aux Pays-Bas     -> [  ] Liaison [z] sonore      [  ] Pas de liaison",
                "3. en Espagne       -> [  ] Liaison [n] sonore      [  ] Pas de liaison",
                "4. en Italie        -> [  ] Liaison [n] sonore      [  ] Pas de liaison",
                "5. au Japon         -> [  ] Liaison                 [  ] Pas de liaison",
                "6. au Maroc         -> [  ] Liaison                 [  ] Pas de liaison"
            ]
        },
        "tier2": {
            "gender_rule_title": "LE GENRE DES PAYS : LA RÈGLE DU '-E' FINAL",
            "gender_rule_text": "Règle générale : Si un nom de pays se termine par un 'e', il est FÉMININ (la France, l'Espagne, l'Italie, la Chine). S'il se termine par toute autre lettre, il est MASCULIN (le Canada, le Japon, le Brésil, le Portugal). Exceptions A1 : le Mexique, le Cambodge, le Mozambique.",
            "ex1_title": "Exercice 2.1 — Matrice Pays, Préposition et Nationalité [6 pts]",
            "ex1_headers": ["Pays (Genre)", "Préposition (en/au/aux)", "Nationalité Masc.", "Nationalité Fém."],
            "ex1_rows": [
                ("1. France (f.)", "-> en France", "français", "-> ___________________"),
                ("2. Canada (m.)", "-> au Canada", "canadien", "-> ___________________"),
                ("3. Espagne (f.)", "-> en Espagne", "espagnol", "-> ___________________"),
                ("4. Japon (m.)", "-> au Japon", "japonais", "-> ___________________"),
                ("5. Allemagne (f.)", "-> en Allemagne", "allemand", "-> ___________________"),
                ("6. États-Unis (pl.)", "-> aux États-Unis", "américain", "-> ___________________"),
            ],
            "ex2_title": "Exercice 2.2 — Détective de Genre & Prépositions de Pays [4 pts]",
            "ex2_sentences": [
                "1. Mon amie habite au France et travaille à Paris.\\n   Correction : _____________________________________________________________________________",
                "2. Ils voyagent en Canada pour les vacances d'hiver.\\n   Correction : _____________________________________________________________________________",
                "3. Sarah est une avocat canadien très brillante.\\n   Correction : _____________________________________________________________________________",
                "4. J'habite dans le rue Victor Hugo au Lyon.\\n   Correction : _____________________________________________________________________________"
            ]
        },
        "tier3": {
            "colloc_tip_title": "COLLOCATIONS GÉOGRAPHIQUES ET COORDONNÉES",
            "colloc_tip_text": "Pour indiquer la ville : préposition 'À' (à Paris, à Lyon, à Londres). Pour indiquer le pays : 'EN' (fém.), 'AU' (masc.), 'AUX' (pluriel). Pour donner son adresse : 'J'habite au 15, rue...'.",
            "ex1_title": "Exercice 3.1 — Prépositions Géographiques (À vs EN vs AU vs AUX) [5 pts]",
            "ex1_sentences": [
                "1. Pierre habite ________ (en / à) Nice, ________ (en / au) France.",
                "2. Kenji vit ________ (au / en) Japon, mais travaille souvent ________ (aux / en) États-Unis.",
                "3. Maria est née ________ (au / en) Espagne, mais elle étudie ________ (à / en) Montréal.",
                "4. Mon oncle a acheté une maison ________ (au / en) Portugal.",
                "5. Vous habitez ________ (dans / au) 25, boulevard Saint-Michel ?"
            ],
            "ex2_title": "Exercice 3.2 — Paires Vocabulaire Urbain & Adresse [5 pts]",
            "ex2_headers": ["Élément d'adresse", "Définition ou exemple", "Association"],
            "ex2_rows": [
                ("1. La rue...", "A. 75008 (Paris 8e arrondissement)", "1 -> [    ]"),
                ("2. Le boulevard...", "B. de la République (voie étroite urbaine)", "2 -> [    ]"),
                ("3. L'avenue...", "C. 3e étage, porte droite", "3 -> [    ]"),
                ("4. Le code postal...", "D. des Champs-Élysées (grande artère plantée d'arbres)", "4 -> [    ]"),
                ("5. L'appartement...", "E. Haussmann (large voie de circulation)", "5 -> [    ]"),
            ]
        },
        "tier4": {
            "cloze_tip_title": "CLOZE D'ENREGISTREMENT D'ADRESSE",
            "cloze_tip_text": "Complétez la fiche de renseignements avec les termes exacts d'adresse et de pays en respectant la casse et les accords.",
            "dialogues": [
                {
                    "title": "Situation A — À la réception de l'hôtel international",
                    "points": "3 pts",
                    "lines": [
                        "• Le réceptionniste : Bonjour Madame. Quelle est votre ___________________________ [nationality - f.] ?",
                        "• Maria : Je suis ___________________________ [Spanish - f.]. J'habite ___________________________ [in Spain - country preposition], à Madrid.",
                        "• Le réceptionniste : Parfait. Et votre ___________________________ [address], s'il vous plaît ?"
                    ]
                },
                {
                    "title": "Situation B — Remplir un bon de livraison en ligne",
                    "points": "4 pts",
                    "lines": [
                        "• Julien : Quel est ton ___________________________ [postal code] ?",
                        "• Thomas : C'est le 69002, à Lyon. J'habite au 18, ___________________________ [street] Victor Hugo.",
                        "• Julien : Tu es dans une maison ou un ___________________________ [apartment] ?",
                        "• Thomas : Dans un immeuble, au deuxième ___________________________ [floor]."
                    ]
                },
                {
                    "title": "Situation C — Présentation multiculturelle en classe de FLE",
                    "points": "3 pts",
                    "lines": [
                        "• La professeure : D'où venez-vous, Chen ?",
                        "• Chen : Je viens de Chine, je suis ___________________________ [Chinese - m.]. Mais aujourd'hui, je vis ___________________________ [in France] avec ma famille.",
                        "• La professeure : Bienvenue ! Et vous parlez ___________________________ [French] ?"
                    ]
                }
            ]
        },
        "tier5": {
            "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
            "ex1_prompts": [
                ("1. I live at 14, Pasteur street in Bordeaux.", "-> __________________________________________________________________________________"),
                ("2. He is Italian and his wife is Canadian.", "-> __________________________________________________________________________________"),
                ("3. They (m.) live in the United States, in New York.", "-> __________________________________________________________________________________"),
                ("4. What is your postal code, please?", "-> __________________________________________________________________________________"),
                ("5. We are traveling to Japan and to Germany.", "-> __________________________________________________________________________________"),
                ("6. Are you English or Australian? (formal with 'vous')", "-> __________________________________________________________________________________"),
            ],
            "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
            "ex2_intrus": [
                ("1. La France  •  L'Italie  •  L'Espagne  •  Le Canada",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("2. Rue  •  Avenue  •  Boulevard  •  Code postal",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("3. En France  •  En Chine  •  Au Portugal  •  En Suisse",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
                ("4. Paris  •  Lyon  •  Marseille  •  Allemagne",
                 "• Intrus : ________________________  |  Justification : ______________________________________________________"),
            ]
        },
        "corrige": {
            "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\\n1. français -> 's' muette [frahn-seh] | 2. française -> 's' voisée sonore [z] [frahn-sez] | 3. italien -> nasale pure [ɛ̃] | 4. italienne -> dénasalisée orale [ɛn] | 5. allemand -> 'd' muet | 6. allemande -> 'd' prononcé [ahl-mahnd].\\n\\nExercice 1.2 — Orthographe [3 pts] :\\na) un Américain (majuscule pour la personne, accent aigu) | b) une Brésilienne (accent aigu, deux 'n') | c) la Grèce (accent grave) | d) un numéro de rue | e) le code postal (masculin, sans 'e') | f) l'Espagne.\\n\\nExercice 1.3 — Liaisons [3 pts] :\\n1. aux États-Unis -> Liaison en [z] obligatoire [o-zay-tah-zyoo-nee] | 2. aux Pays-Bas -> Liaison en [z] | 3. en Espagne -> Liaison en [n] [ahn-nes-pahn-yuh] | 4. en Italie -> Liaison en [n] | 5. au Japon -> Pas de liaison | 6. au Maroc -> Pas de liaison.",
            "tier2_text": "Exercice 2.1 — Matrice des Pays [6 pts] :\\n1. française | 2. canadienne | 3. espagnole | 4. japonaise | 5. allemande | 6. américaine.\\n\\nExercice 2.2 — Détective [4 pts] :\\n1. 'EN France' (France est féminin : en France).\\n2. 'AU Canada' (Canada est masculin : au Canada).\\n3. 'Sarah est une avocate canadienne' (accords féminins nécessaires).\\n4. 'J'habite DANS LA rue Victor Hugo À Lyon' (rue est féminin, et les villes prennent 'à').",
            "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\\n1. à / en | 2. au / aux | 3. en / à | 4. au | 5. au.\\n\\nExercice 3.2 — Paires Vocabulaire Urbain [5 pts] :\\n1 -> B (La rue de la République) | 2 -> E (Le boulevard Haussmann) | 3 -> D (L'avenue des Champs-Élysées) | 4 -> A (Le code postal 75008) | 5 -> C (L'appartement 3e étage).",
            "tier4_text": "Situation A (3 pts) : nationalité | espagnole | en Espagne | adresse.\\nSituation B (4 pts) : code postal | rue | appartement | étage.\\nSituation C (3 pts) : chinois | en France | français.",
            "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\\n1. J'habite au 14, rue Pasteur à Bordeaux.\\n2. Il est italien et sa femme est canadienne.\\n3. Ils habitent aux États-Unis, à New York.\\n4. Quel est votre code postal, s'il vous plaît ?\\n5. Nous voyageons au Japon et en Allemagne.\\n6. Vous êtes anglais ou australien ?\\n\\nExercice 5.2 — L'Intrus [4 pts] :\\n1. Le Canada (pays masculin, les 3 autres sont féminins et se terminent par 'e').\\n2. Code postal (suite numérique, les 3 autres sont des types de voies de circulation).\\n3. Au Portugal (pays masculin avec 'au', les 3 autres sont des pays féminins avec 'en').\\n4. Allemagne (c'est un pays, les 3 autres sont des grandes villes françaises).",
            "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 3",
            "anchors_text": "1. Règle du 'e' des pays : Presque tous les pays terminés par 'e' sont féminins et prennent 'EN' (en France, en Italie, en Suisse). Les pays terminés par une autre lettre sont masculins et prennent 'AU' (au Canada, au Japon, au Brésil).\\n2. Villes vs Pays : Ne confondez jamais : 'À' pour les villes (à Paris, à Tokyo), mais 'EN/AU/AUX' pour les pays.\\n3. Majuscules des nationalités : En français, l'adjectif prend une minuscule ('Il est français', 'un vin français'), mais le nom de personne prend une majuscule ('Un Français a gagné')."
        }
    }
}
'''

with open("curriculum_batch_1.py", "w", encoding="utf-8") as f:
    f.write(batch1_code)

print("curriculum_batch_1.py initialized with Ch 1-3.")
