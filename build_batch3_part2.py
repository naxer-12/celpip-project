import json

with open("chapters_batch_3_part1.json", "r", encoding="utf-8") as f:
    batch3 = json.load(f)

# CHAPTER 28: Les maladies et les accidents
batch3["28"] = {
    "ch_num": 28,
    "title_fr": "Les maladies et les accidents",
    "title_en": "Illnesses, Symptoms & Physical Ailments",
    "word_count": 45,
    "traps": [
        "The grammatical formula 'AVOIR MAL À + article défini': 'avoir mal AU ventre' (à + le), 'avoir mal À LA tête', 'avoir mal À L'estomac', 'avoir mal AUX dents' (à + les).",
        "Expression of physical state: 'ÊTRE enrhumé / fatigué / blessé' vs 'AVOIR de la fièvre / la grippe / un rhume / de la toux'.",
        "Gender traps: 'la maladie' (f.), 'la fièvre' (f.), 'la douleur' (f.), 'la toux' (f.), but 'le rhume' (m.), 'le médicament' (m.), 'l'accident' (m.), 'le pansement' (m.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'X' FINAL SILENCIEUX DE TOUX ET L'ACCENT GRAVE DE FIÈVRE",
        "phonetic_tip_text": "'La toux' se prononce [too] : le 'x' final est totalement muet ! 'La fièvre' [fyevr] s'articule avec un accent grave ouvrant la voyelle [ɛ] suivie du groupe consonantique [vʁ].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Symptômes & Douleurs [4 pts]",
        "ex1_headers": ["Terme médical", "Genre", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. la toux (f.)", "Féminin", "Consonne 'x' muette", "[ too ]", "'x' final muet absolu"],
            ["2. le rhume (m.)", "Masculin", "Graphème 'rh-'", "[ reom ]", "'h' muet, son [ym]"],
            ["3. la fièvre (f.)", "Féminin", "Accent grave 'è'", "[ fyevr ]", "Son [ɛ] ouvert, [vʁ] final"],
            ["4. le mal de tête (m.)", "Masculin", "Consonne 'l' sonore", "[ mahl duh tet ]", "'l' articulé, circonflexe sur 'e'"],
            ["5. le ventre (m.)", "Masculin", "Graphème '-en-' nasal", "[ vahntr ]", "Nasale [ɑ̃] pure"],
            ["6. la blessure (f.)", "Féminin", "Double 'ss' sonore", "[ blay-soor ]", "Son [s] franc et [yʁ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) avoir de la fievre -> ________________________",
            "b) un medicament contre la douleur -> ________________________",
            "c) etre blesse a la jambe -> ________________________",
            "d) avoir mal a l'estomac -> ________________________",
            "e) une piqure de guepe -> ________________________",
            "f) une ordonnance du medecin -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Élidations Médicales [3 pts]",
        "ex3_items": [
            "1. un accident grave       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. aux urgences médicales   -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un estomac douloureux    -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. avoir de la fièvre       -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux ordonnances         -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un appel d'urgence       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES PATHOLOGIES ET TRAITEMENTS",
        "gender_rule_text": "Pathologies & symptômes : la maladie (f.), la fièvre (f.), la grippe (f.), la toux (f.), la douleur (f.), la blessure (f.), la brûlure (f.), mais le rhume (m.), le mal (m.), le vertige (m.). Traitements : le médicament, le comprimé, le sirop, le pansement, mais la pommade, la piqûre, l'ordonnance.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Symptômes & Remèdes [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ fièvre (f.)", "[   ] M   [   ] F", "7. _______ médicament (m.)", "[   ] M   [   ] F"],
            ["2. _______ rhume (m.)", "[   ] M   [   ] F", "8. _______ pommade (f.)", "[   ] M   [   ] F"],
            ["3. _______ grippe (f.)", "[   ] M   [   ] F", "9. _______ comprimé (m.)", "[   ] M   [   ] F"],
            ["4. _______ toux (f.)", "[   ] M   [   ] F", "10. _______ sirop (m.)", "[   ] M   [   ] F"],
            ["5. _______ blessure (f.)", "[   ] M   [   ] F", "11. _______ ordonnance (f.)", "[   ] M   [   ] F"],
            ["6. _______ douleur (f.)", "[   ] M   [   ] F", "12. _______ pansement (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre & Contractions : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai très mal à le ventre depuis hier soir après le dîner.\n   Correction : _____________________________________________________________________________",
            "2. Le patient a une fort fièvre et il tousse beaucoup depuis deux jours.\n   Correction : _____________________________________________________________________________",
            "3. Le médecin m'a prescrit une efficace médicament contre les maux de gorge.\n   Correction : _____________________________________________________________________________",
            "4. Elle a mal à les yeux à force de travailler sur l'ordinateur sans lunettes.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS MÉDICALES : LA FORMULE 'AVOIR MAL À'",
        "colloc_tip_text": "Formules indispensables : 'avoir mal au dos / au ventre / à la gorge / à la tête / aux dents', 'avoir 38 de fièvre', 'prendre un comprimé', 'poser un pansement', 'se casser la jambe', 'prendre sa température'.",
        "ex1_title": "Exercice 3.1 — Contractions 'À + Article' avec les Parties du Corps [5 pts]",
        "ex1_sentences": [
            "1. Thomas a trop mangé de chocolat : il a très mal _________ (au / à la) ventre ce matin.",
            "2. Sophie a crié toute la soirée au concert, elle a maintenant mal _________ (à la / au) gorge.",
            "3. Après avoir lu pendant des heures sans lumière, j'ai mal _________ (aux / à les) yeux.",
            "4. L'infirmière utilise un thermomètre pour _________ (prendre / faire) la température du malade.",
            "5. Le pharmacien me conseille de prendre un comprimé d'aspirine contre le _________ (mal / malheur) de tête."
        ],
        "ex2_title": "Exercice 3.2 — Paires Symptôme-Remède Adapté [5 pts]",
        "ex2_headers": ["Symptôme ressenti", "Remède ou action préconisée", "Code association"],
        "ex2_rows": [
            ["1. Une forte fièvre à 39 °C...", "A. Appliquer une pommade apaisante", "1 -> [    ]"],
            ["2. Une toux sèche persistante...", "B. Prendre du paracétamol et se reposer au lit", "2 -> [    ]"],
            ["3. Une coupure au doigt...", "C. Prendre une cuillère de sirop antitussif", "3 -> [    ]"],
            ["4. Une brûlure superficielle...", "D. Poser un pansement adhésif stérile", "4 -> [    ]"],
            ["5. Une rage de dents aiguë...", "E. Prendre rendez-vous d'urgence chez le dentiste", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : EXPRIMER SES DOULEURS AU MÉDECIN",
        "cloze_tip_text": "Complétez la consultation médicale sans support d'aide.",
        "dialogues": [
            {
                "title": "Situation A — Consultation chez le médecin généraliste (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le médecin : Bonjour Madame, qu'est-ce qui ne ___________________________ [goes well / va pas] ?",
                    "• La patiente : Docteur, j'ai très ___________________________ [fever / hot] et j'ai mal à la ___________________________ [head].",
                    "• Le médecin : D'accord. Ouvrez la bouche, je vais examiner votre ___________________________ [throat]."
                ]
            },
            {
                "title": "Situation B — À la pharmacie avec une ordonnance (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le pharmacien : Bonjour, vous avez une ___________________________ [prescription] ?",
                    "• Le client : Oui, voici la feuille du docteur. J'ai aussi besoin de ___________________________ [band-aids] pour mon fils.",
                    "• Le pharmacien : Prenez deux ___________________________ [pills / tablets] de cet antalgique par jour, pendant les ___________________________ [meals].",
                    "• Le client : Merci beaucoup pour vos conseils bienveillants."
                ]
            },
            {
                "title": "Situation C — Accident léger à la maison (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La mère : Qu'est-ce qui s'est passé ? Tu t'es ___________________________ [injured / hurt] ?",
                    "• L'enfant : Je suis tombé dans l'escalier et j'ai mal au ___________________________ [knee / foot].",
                    "• La mère : Ne bouge pas, je vais mettre de la ___________________________ [ice / cream] sur le bleu."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I have a bad headache and a sore throat.", "-> __________________________________________________________________________________"],
            ["2. My son has a fever; his temperature is 38.5 degrees.", "-> __________________________________________________________________________________"],
            ["3. Take this pill three times a day with a glass of water.", "-> __________________________________________________________________________________"],
            ["4. He hurt his arm during the soccer game.", "-> __________________________________________________________________________________"],
            ["5. You need to see a doctor and get a prescription.", "-> __________________________________________________________________________________"],
            ["6. Put a clean bandage on the wound.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La fièvre  •  Le rhume  •  La grippe  •  Le restaurant", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Mal au ventre  •  Mal à la tête  •  Mal aux dents  •  Mal à la valise", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le comprimé  •  Le sirop  •  Le pansement  •  Le couteau", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Être enrhumé  •  Avoir de la fièvre  •  Tousser  •  Acheter un billet de train", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. la toux -> 'x' muet [too] | 2. le rhume -> 'h' muet [reom] | 3. la fièvre -> accent grave [fyevr] | 4. le mal de tête -> 'l' sonore [mahl duh tet] | 5. le ventre -> nasale [vahntr] | 6. la blessure -> double 'ss' sonore [blay-soor].\nExercice 1.2 — Orthographe [3 pts] :\na) avoir de la fièvre | b) un médicament | c) blessé à la jambe | d) à l'estomac | e) une piqûre de guêpe | f) une ordonnance du médecin.\nExercice 1.3 — Liaisons [3 pts] :\n1. un accident [n] | 2. aux urgences [z] | 3. un estomac [n] | 4. avoir de la fièvre (pas de liaison) | 5. deux ordonnances [z] | 6. un appel [n].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la fièvre (F) | 2. le rhume (M) | 3. la grippe (F) | 4. la toux (F) | 5. la blessure (F) | 6. la douleur (F) | 7. le médicament (M) | 8. la pommade (F) | 9. le comprimé (M) | 10. le sirop (M) | 11. l'ordonnance (F) | 12. le pansement (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. AU ventre (à + le = au) | 2. Une FORTE fièvre (fièvre est féminin) | 3. Un médicament EFFICACE (médicament est masculin) | 4. AUX yeux (à + les = aux).",
        "tier3_text": "Exercice 3.1 — Contractions 'À + Article' [5 pts] :\n1. au | 2. à la | 3. aux | 4. prendre | 5. mal.\nExercice 3.2 — Paires Symptôme-Remède [5 pts] :\n1 -> B (Fièvre : paracétamol et repos) | 2 -> C (Toux sèche : sirop antitussif) | 3 -> D (Coupure : pansement stérile) | 4 -> A (Brûlure : pommade apaisante) | 5 -> E (Rage de dents : rendez-vous dentiste).",
        "tier4_text": "Situation A (3 pts) : va pas | chaud (ou de la fièvre) | tête | gorge.\nSituation B (4 pts) : ordonnance | pansements | comprimés | repas.\nSituation C (3 pts) : blessé (ou fait mal) | genou (ou pied) | glace (ou pommade).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. J'ai très mal à la tête et mal à la gorge. | 2. Mon fils a de la fièvre ; sa température est de 38,5 degrés. | 3. Prenez ce comprimé trois fois par jour avec un verre d'eau. | 4. Il s'est fait mal au bras pendant le match de football. | 5. Vous devez consulter un médecin et obtenir une ordonnance. | 6. Mettez un pansement propre sur la blessure.\nExercice 5.2 — Intrus [4 pts] :\n1. Le restaurant (lieu de restauration, les autres sont des maladies ou états de santé) | 2. Mal à la valise (objet inanimé absurde, les trois autres sont des maux corporels réels) | 3. Le couteau (couvert de table, les autres sont des remèdes médicaux) | 4. Acheter un billet de train (action de transport ferroviaire, les autres sont des symptômes de maladie).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 28",
        "anchors_text": "1. La règle d'or d'AVOIR MAL À : 'À' se contracte obligatoirement avec l'article défini : à + le = AU (au dos, au ventre, au bras) ; à + les = AUX (aux yeux, aux oreilles, aux dents) ; à la tête (féminin) ; à l'estomac (devant voyelle).\n2. Fièvre et température : En France, la température corporelle s'exprime en degrés Celsius. On dit couramment 'avoir de la fièvre' dès 38 °C (trente-huit degrés).\n3. Toux : Le mot 'toux' se prononce [too] sans jamais faire sonner le 'x'."
    }
}

# CHAPTER 29: Les métiers et les lieux de la santé
batch3["29"] = {
    "ch_num": 29,
    "title_fr": "Les métiers et les lieux de la santé",
    "title_en": "Medical Professionals, Clinics & Emergency Care",
    "word_count": 44,
    "traps": [
        "French Emergency Numbers: 15 (SAMU - Urgences médicales), 18 (Sapeurs-Pompiers - Incendies / Secours routiers), 17 (Police-Secours), 112 (Numéro européen général d'urgence)!",
        "Health professional titles: 'le médecin généraliste' (GP), 'le spécialiste', 'le chirurgien / la chirurgienne', 'l'infirmier / l'infirmière', 'le pharmacien / la pharmacienne'. Note: 'médecin' is traditionally epicene in France (un/une médecin).",
        "Health insurance card: 'La Carte Vitale' is the essential French social security smart card for doctor visits and pharmacy reimbursements."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'C' DUR ET DOUX DE MÉDECIN ET LA NASALE D'HÔPITAL",
        "phonetic_tip_text": "'Le médecin' [may-duh-sanh] se prononce avec un e caduc muet ou semi-muet et une nasale [ɛ̃]. 'L'hôpital' commence par un 'h' muet obligeant l'élision et comporte un circonflexe sur 'o' [loh-pee-tahl].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Personnel Médical [4 pts]",
        "ex1_headers": ["Professionnel / Lieu", "Genre", "Caractéristique phonétique", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le médecin (m.)", "Masculin", "E caduc dans 'de'", "[ may-duh-sanh ]", "Nasale [ɛ̃] pure, pas de 'k'"],
            ["2. l'hôpital (m.)", "Masculin", "H muet avec élision", "[ loh-pee-tahl ]", "Circonflexe 'ô', 'l' sonore"],
            ["3. l'infirmier (m.)", "Masculin", "Suffixe '-ier'", "[ anh-feer-myay ]", "'r' muet, son [e] pur"],
            ["4. l'infirmière (f.)", "Féminin", "Suffixe '-ière'", "[ anh-feer-myair ]", "Accent grave, 'r' sonore [ɛʁ]"],
            ["5. la pharmacie (f.)", "Féminin", "Graphème 'ph-' son [f]", "[ fahr-mah-see ]", "'ph' sonne [f] net"],
            ["6. le dentiste (m./f.)", "Épicène", "Suffixe '-iste'", "[ dahn-teest ]", "Nasale [ɑ̃] puis [tist]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un hopital public -> ________________________",
            "b) une infirmiere de garde -> ________________________",
            "c) un medecin generaliste -> ________________________",
            "d) un chirurgien a la clinique -> ________________________",
            "e) la Carte Vitale de securite sociale -> ________________________",
            "f) le service des urgences -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Urgences [3 pts]",
        "ex3_items": [
            "1. un appel d'urgence      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des infirmiers dévoués  -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un hôpital moderne      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. aux urgences du CHU     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "5. deux ambulanciers       -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand médecin        -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES LIEUX DE SOIN ET DES PROFESSIONS MÉDICALES",
        "gender_rule_text": "Lieux de soin : l'hôpital (m.), le cabinet médical (m.), le centre de santé (m.), le laboratoire d'analyses (m.), mais la clinique (f.), la maternité (f.), la pharmacie (f.). Métiers invariables en -e : le/la dentiste, le/la kinésithérapeute (kiné), le/la pédiatre, le/la psychologue.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Praticiens & Infrastructures [6 pts]",
        "ex1_headers": ["Professionnel / Lieu", "Genre (M/F)", "Professionnel / Lieu", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ médecin (m.)", "[   ] M   [   ] F", "7. _______ hôpital (m.)", "[   ] M   [   ] F"],
            ["2. _______ infirmier (m.)", "[   ] M   [   ] F", "8. _______ clinique (f.)", "[   ] M   [   ] F"],
            ["3. _______ infirmière (f.)", "[   ] M   [   ] F", "9. _______ pharmacie (f.)", "[   ] M   [   ] F"],
            ["4. _______ chirurgien (m.)", "[   ] M   [   ] F", "10. _______ cabinet médical (m.)", "[   ] M   [   ] F"],
            ["5. _______ dentiste (m./f.)", "[   ] M   [   ] F", "11. _______ ambulance (f.)", "[   ] M   [   ] F"],
            ["6. _______ pédiatre (m./f.)", "[   ] M   [   ] F", "12. _______ Carte Vitale (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai pris rendez-vous dans une nouvel hôpital situé près de la gare.\n   Correction : _____________________________________________________________________________",
            "2. Le infirmière est venue à domicile pour faire une piqûre de vaccin.\n   Correction : _____________________________________________________________________________",
            "3. N'oubliez pas d'insérer votre Carte Vitale vert dans le lecteur du médecin.\n   Correction : _____________________________________________________________________________",
            "4. Une chirurgien réputé a opéré le genou du footballeur avec succès.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS MÉDICALES : RENDEZ-VOUS & NUMÉROS D'URGENCE",
        "colloc_tip_text": "Expressions administratives : 'prendre rendez-vous chez le médecin', 'consulter son médecin traitant', 'présenter sa Carte Vitale', 'composer le 15 pour le SAMU', 'aller aux urgences'.",
        "ex1_title": "Exercice 3.1 — Démarches Médicales & Urgences [5 pts]",
        "ex1_sentences": [
            "1. En France, en cas de détresse médicale vitale, on compose immédiatement le _________ (15 / 17) pour joindre le SAMU.",
            "2. Avant de vous examiner, le secrétaire médical vous demande de présenter votre Carte _________ (Vitale / Postale).",
            "3. Je dois absolument prendre _________ (rendez-vous / place) chez le dentiste pour soigner une carie.",
            "4. Après l'accident sur la route, les blessés ont été transportés en _________ (ambulance / train) à l'hôpital.",
            "5. Pour renouveler mon traitement, je consulte mon médecin _________ (traitant / privé) de famille."
        ],
        "ex2_title": "Exercice 3.2 — Paires Praticien-Domaine d'Intervention [5 pts]",
        "ex2_headers": ["Professionnel de santé", "Mission médicale", "Code association"],
        "ex2_rows": [
            ["1. Le dentiste...", "A. Réalise des opérations chirurgicales au bloc", "1 -> [    ]"],
            ["2. L'ophtalmologiste...", "B. Soigne les dents, caries et gencives", "2 -> [    ]"],
            ["3. Le pédiatre...", "C. Effectue les soins quotidiens et les pansements", "3 -> [    ]"],
            ["4. L'infirmier...", "D. Spécialiste de la santé des bébés et des enfants", "4 -> [    ]"],
            ["5. Le chirurgien...", "E. Contrôle la vue et prescrit des lunettes", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : PRENDRE RENDEZ-VOUS ET CONSULTER",
        "cloze_tip_text": "Complétez les situations d'accueil médical sans liste de mots.",
        "dialogues": [
            {
                "title": "Situation A — Prise de rendez-vous téléphonique au cabinet (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le patient : Bonjour Madame, je voudrais prendre ___________________________ [an appointment] avec le docteur Bernard.",
                    "• La secrétaire : Bonjour. Est-ce que c'est une ___________________________ [emergency] ou pour un contrôle de routine ?",
                    "• Le patient : C'est pour une grippe avec fièvre. Avez-vous une place ___________________________ [today / this afternoon] ?"
                ]
            },
            {
                "title": "Situation B — À l'accueil des urgences hospitalières (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• L'infirmière : Bonjour Monsieur, qu'est-ce qui vous amène aux ___________________________ [emergency room] ?",
                    "• Le patient : Je suis tombé et je pense que je me suis ___________________________ [broken] le poignet.",
                    "• L'infirmière : Avez-vous votre pièce d'identité et votre Carte ___________________________ [health card] ?",
                    "• Le patient : Oui, les voici. Le médecin va me faire passer une ___________________________ [X-ray / radio] ?"
                ]
            },
            {
                "title": "Situation C — Appel d'urgence au SAMU (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• L'opérateur : SAMU, bonjour. Quel est le lieu de l'___________________________ [accident / emergency] ?",
                    "• Le témoin : Nous sommes au 14 rue de la Paix. Une personne a perdu ___________________________ [consciousness].",
                    "• L'opérateur : Restez en ligne, nous envoyons une équipe avec une ___________________________ [ambulance]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. In France, call 15 for the medical emergency services (SAMU).", "-> __________________________________________________________________________________"],
            ["2. I have an appointment with the doctor at 3:30 PM.", "-> __________________________________________________________________________________"],
            ["3. Do not forget your green Carte Vitale for the consultation.", "-> __________________________________________________________________________________"],
            ["4. The nurse gave a vaccination injection to the child.", "-> __________________________________________________________________________________"],
            ["5. The hospital is located next to the university clinic.", "-> __________________________________________________________________________________"],
            ["6. The dentist treated two cavities this morning.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. L'hôpital  •  La clinique  •  Le cabinet médical  •  Le cinéma", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le médecin  •  L'infirmier  •  Le dentiste  •  Le boulanger", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le 15  •  Le 18  •  Le 112  •  Le 204", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La Carte Vitale  •  L'ordonnance  •  Le stéthoscope  •  La fourchette", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le médecin -> [may-duh-sanh] nasale pure | 2. l'hôpital -> 'h' muet avec circonflexe [loh-pee-tahl] | 3. l'infirmier -> [anh-feer-myay] 'r' muet | 4. l'infirmière -> [anh-feer-myair] 'r' sonore | 5. la pharmacie -> 'ph' sonne [f] [fahr-mah-see] | 6. le dentiste -> épicène [dahn-teest].\nExercice 1.2 — Orthographe [3 pts] :\na) un hôpital public | b) une infirmière de garde | c) un médecin généraliste | d) un chirurgien à la clinique | e) la Carte Vitale | f) le service des urgences.\nExercice 1.3 — Liaisons [3 pts] :\n1. un appel [n] | 2. des infirmiers [z] | 3. un hôpital [n] | 4. aux urgences [z] | 5. deux ambulanciers [z] | 6. un grand médecin [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. le médecin (M) | 2. l'infirmier (M) | 3. l'infirmière (F) | 4. le chirurgien (M) | 5. le/la dentiste (M/F) | 6. le/la pédiatre (M/F) | 7. l'hôpital (M) | 8. la clinique (F) | 9. la pharmacie (F) | 10. le cabinet médical (M) | 11. l'ambulance (F) | 12. la Carte Vitale (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UN NOUVEL hôpital (hôpital est masculin commençant par voyelle/h muet) | 2. L'infirmière (élision obligatoire devant voyelle) | 3. Carte Vitale VERTE (carte est féminin) | 4. UN chirurgien (ou UNE chirurgienne).",
        "tier3_text": "Exercice 3.1 — Démarches Médicales [5 pts] :\n1. 15 | 2. Vitale | 3. rendez-vous | 4. ambulance | 5. traitant.\nExercice 3.2 — Paires Praticiens [5 pts] :\n1 -> B (Dentiste : dents et caries) | 2 -> E (Ophtalmologiste : vue et lunettes) | 3 -> D (Pédiatre : santé des enfants) | 4 -> C (Infirmier : soins et pansements) | 5 -> A (Chirurgien : opérations au bloc).",
        "tier4_text": "Situation A (3 pts) : rendez-vous | urgence | aujourd'hui (ou cet après-midi).\nSituation B (4 pts) : urgences | cassé (ou fracturé) | Vitale | radiographie (ou radio).\nSituation C (3 pts) : urgence (ou accident) | connaissance | ambulance.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. En France, appelez le 15 pour les urgences médicales (SAMU). | 2. J'ai un rendez-vous chez le médecin à 15h30. | 3. N'oubliez pas votre Carte Vitale verte pour la consultation. | 4. L'infirmière a fait une piqûre de vaccin à l'enfant. | 5. L'hôpital est situé à côté de la clinique universitaire. | 6. Le dentiste a soigné deux caries ce matin.\nExercice 5.2 — Intrus [4 pts] :\n1. Le cinéma (lieu de loisirs et divertissement, les autres sont des structures de santé) | 2. Le boulanger (artisan de bouche, les autres sont des professionnels de santé) | 3. Le 204 (numéro quelconque, les autres sont les numéros d'urgence officiels en France) | 4. La fourchette (couvert de table, les autres sont des instruments ou documents médicaux).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 29",
        "anchors_text": "1. Les numéros d'urgence indispensables en France : Le 15 (SAMU, détresses médicales vitales), le 18 (Pompiers, feux, accidents de la route), le 17 (Police-Secours), le 112 (Numéro d'urgence européen polyvalent).\n2. La Carte Vitale : Carte à puce verte distribuée par l'Assurance Maladie contenant les droits de sécurité sociale du patient pour la télétransmission et le remboursement des soins médicaux.\n3. 'Le médecin traitant' : En France, chaque citoyen déclare un 'médecin traitant' de référence qui coordonne son parcours de soins vers les spécialistes."
    }
}

# CHAPTER 30: La ville et les services publics
batch3["30"] = {
    "ch_num": 30,
    "title_fr": "La ville et les services publics",
    "title_en": "City Life, Public Services & Asking for Directions",
    "word_count": 45,
    "traps": [
        "Giving directions formulas: 'Tourner à gauche / à droite', 'Aller tout droit' (straight ahead - NOT 'à droite'!), 'Prendre la première rue à gauche', 'Traverser le pont / le carrefour'.",
        "Town hall terminology: 'La mairie' is the neighborhood/small town hall; in large cities like Paris, the central city hall is 'l'Hôtel de Ville' (which is NOT a hotel!).",
        "Gender traps: 'la ville' (f.), 'la rue' (f.), 'la place' (f.), 'la mairie' (f.), 'la poste' (f.), 'la bibliothèque' (f.), but 'le quartier' (m.), 'le pont' (m.), 'le parc' (m.), 'le musée' (m.), 'le commissariat' (m.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE PIÈGE HOMOPHONIQUE : 'TOUT DROIT' VS 'À DROITE'",
        "phonetic_tip_text": "Danger numéro 1 en compréhension orale FLE : 'Tout droit' [too drwah] (straight ahead, 't' muet) ressemble à 'À droite' [ah drwaht] (to the right, 't' prononcé) ! La consonne finale sonore [t] fait toute la différence !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Repères Urbains [4 pts]",
        "ex1_headers": ["Terme de direction / Lieu", "Direction", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. tout droit", "En face", "Consonne 't' muette", "[ too drwah ]", "Zéro 't' sonore : 'straight'"],
            ["2. à droite", "Virage", "Consonne 't' prononcée", "[ ah drwaht ]", "Son [t] net : 'right'"],
            ["3. à gauche", "Virage", "Consonne 'ch' son [ʃ]", "[ ah gohsh ]", "Son [o] fermé, [ʃ] doux"],
            ["4. le pont (m.)", "Lieu", "Consonne 't' muette", "[ pohn ]", "Nasale [ɔ̃] pure, 't' muet"],
            ["5. la mairie (f.)", "Édifice", "Voyelle 'ai'", "[ may-ree ]", "Son [ɛ] ouvert, 'r' sonore"],
            ["6. la poste (f.)", "Édifice", "Consonne 't' prononcée", "[ pohst ]", "Son [ɔ] bref, [st] articulé"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) la mairie de quartier -> ________________________",
            "b) un batiment municipal -> ________________________",
            "c) un commissariat de police -> ________________________",
            "d) une bibliotheque municipale -> ________________________",
            "e) un rond-point a la sortie de la ville -> ________________________",
            "f) traverser le carrefour -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons en Ville [3 pts]",
        "ex3_items": [
            "1. un arrêt d'autobus     -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des anciens monuments  -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un hôtel de ville      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. aller tout droit       -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux avenues           -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand parc          -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES ESPACES ET ÉDIFICES URBAINS",
        "gender_rule_text": "Voirie & espaces publics féminins : la rue, l'avenue, la place, la route, la fontaine, la passerelle. Masculins : le boulevard, le pont, le carrefour, le rond-point, le quartier, le square, le trottoir. Services publics : la mairie, la poste, la préfecture, la banque, mais le commissariat, le tribunal, l'office.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Lieux & Voies Urbaines [6 pts]",
        "ex1_headers": ["Lieu urbain", "Genre (M/F)", "Lieu urbain", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ rue (f.)", "[   ] M   [   ] F", "7. _______ pont (m.)", "[   ] M   [   ] F"],
            ["2. _______ boulevard (m.)", "[   ] M   [   ] F", "8. _______ place (f.)", "[   ] M   [   ] F"],
            ["3. _______ avenue (f.)", "[   ] M   [   ] F", "9. _______ parc (m.)", "[   ] M   [   ] F"],
            ["4. _______ mairie (f.)", "[   ] M   [   ] F", "10. _______ commissariat (m.)", "[   ] M   [   ] F"],
            ["5. _______ poste (f.)", "[   ] M   [   ] F", "11. _______ carrefour (m.)", "[   ] M   [   ] F"],
            ["6. _______ bibliothèque (f.)", "[   ] M   [   ] F", "12. _______ fontaine (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Pour trouver la pharmacie, prenez le première rue à gauche après le feu.\n   Correction : _____________________________________________________________________________",
            "2. Nous habitons dans une vieux quartier historique très pittoresque.\n   Correction : _____________________________________________________________________________",
            "3. Le mairie de Paris organise une grande fête musicale sur le parvis.\n   Correction : _____________________________________________________________________________",
            "4. Traversez une grand pont en pierre pour rejoindre la rive opposée.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE GUIDAGE : VERBES DE DÉPLACEMENT & REPÈRES",
        "colloc_tip_text": "Verbes d'orientation : 'tourner à droite/gauche', 'continuer tout droit jusqu'au carrefour', 'prendre la deuxième rue', 'traverser le pont/la place', 'longer le fleuve', 'se trouver en face de / à côté de'.",
        "ex1_title": "Exercice 3.1 — Verbes d'Orientation & Prépositions Spatiales [5 pts]",
        "ex1_sentences": [
            "1. Pour aller à la poste, continuez _________ (tout droit / à droite) pendant 200 mètres.",
            "2. Au carrefour, vous devez _________ (tourner / prendre) à droite dans l'avenue Victor Hugo.",
            "3. L'office de tourisme se trouve juste _________ (en face de / par) la cathédrale gothique.",
            "4. Les piétons doivent marcher sur le _________ (trottoir / feu) pour leur sécurité.",
            "5. Pour aller sur l'autre rive, il faut _________ (traverser / voler) le grand pont suspendu."
        ],
        "ex2_title": "Exercice 3.2 — Paires Demande d'Itinéraire-Instruction [5 pts]",
        "ex2_headers": ["Question du touriste", "Indication du passant", "Code association"],
        "ex2_rows": [
            ["1. Où se trouve la mairie ?", "A. Prenez la deuxième rue à droite, c'est juste là", "1 -> [    ]"],
            ["2. Pour aller à la gare, s'il vous plaît ?", "B. En face du musée, sur la grande place centrale", "2 -> [    ]"],
            ["3. Y a-t-il une pharmacie près d'ici ?", "C. Continuez tout droit et traversez le pont", "3 -> [    ]"],
            ["4. Est-ce que le parc est loin ?", "D. Non, c'est à cinq minutes à pied en longeant le quai", "4 -> [    ]"],
            ["5. Où puis-je poster cette lettre ?", "E. Au bureau de poste situé à l'angle du boulevard", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : DEMANDER SON CHEMIN EN VILLE",
        "cloze_tip_text": "Complétez les dialogues d'orientation sans aide lexicale.",
        "dialogues": [
            {
                "title": "Situation A — Demander son chemin dans la rue (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le touriste : Pardon Monsieur, je cherche la ___________________________ [town hall], s'il vous plaît ?",
                    "• Le passant : Ce n'est pas loin. Allez tout ___________________________ [straight], puis tournez à ___________________________ [left].",
                    "• Le touriste : Merci beaucoup pour votre aide !"
                ]
            },
            {
                "title": "Situation B — Localiser le bureau de poste (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• La dame : Excusez-moi Madame, où est le bureau de ___________________________ [post office] le plus proche ?",
                    "• L'habitante : Prenez cette ___________________________ [street], traversez le ___________________________ [bridge], et c'est sur votre ___________________________ [right].",
                    "• La dame : C'est juste à côté de la banque ?",
                    "• L'habitante : Exactement, en face de la ___________________________ [fountain / square]."
                ]
            },
            {
                "title": "Situation C — Au commissariat de police (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le touriste : Bonjour, je voudrais déclarer la perte de mon ___________________________ [passport / wallet].",
                    "• L'agent de police : Asseyez-vous. Quel est votre ___________________________ [name and surname] ?",
                    "• Le touriste : Je m'appelle Paul Taylor, je suis touriste canadien."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. Go straight ahead, then turn right at the traffic lights.", "-> __________________________________________________________________________________"],
            ["2. Where is the nearest post office located?", "-> __________________________________________________________________________________"],
            ["3. Cross the stone bridge and take the first street on the left.", "-> __________________________________________________________________________________"],
            ["4. The town hall is located across from the central park.", "-> __________________________________________________________________________________"],
            ["5. Is there a pharmacy in this historic neighborhood?", "-> __________________________________________________________________________________"],
            ["6. The public library is open from Tuesday to Saturday.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La rue  •  Le boulevard  •  L'avenue  •  La saucisse", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Tout droit  •  À gauche  •  À droite  •  À la vanille", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La mairie  •  La poste  •  Le commissariat  •  Le pyjama", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Le pont  •  Le trottoir  •  Le carrefour  •  Le rôti de porc", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. tout droit -> 't' muet [too drwah] (straight) | 2. à droite -> 't' prononcé [ah drwaht] (right) | 3. à gauche -> [ah gohsh] | 4. le pont -> nasale pure [pohn] | 5. la mairie -> [may-ree] | 6. la poste -> [pohst].\nExercice 1.2 — Orthographe [3 pts] :\na) la mairie | b) un bâtiment municipal | c) un commissariat de police | d) une bibliothèque municipale | e) un rond-point | f) traverser le carrefour.\nExercice 1.3 — Liaisons [3 pts] :\n1. un arrêt [n] | 2. des anciens monuments [z] | 3. un hôtel de ville [n] | 4. aller tout droit (pas de liaison) | 5. deux avenues [z] | 6. un grand parc [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la rue (F) | 2. le boulevard (M) | 3. l'avenue (F) | 4. la mairie (F) | 5. la poste (F) | 6. la bibliothèque (F) | 7. le pont (M) | 8. la place (F) | 9. le parc (M) | 10. le commissariat (M) | 11. le carrefour (M) | 12. la fontaine (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. LA PREMIÈRE rue (rue est féminin) | 2. UN VIEUX quartier (quartier est masculin) | 3. LA mairie (mairie est féminin) | 4. UN GRAND pont (pont est masculin).",
        "tier3_text": "Exercice 3.1 — Verbes & Prépositions [5 pts] :\n1. tout droit | 2. tourner | 3. en face de | 4. trottoir | 5. traverser.\nExercice 3.2 — Paires Demandes-Indications [5 pts] :\n1 -> B (Mairie sur la place centrale) | 2 -> C (Gare : tout droit et traversez le pont) | 3 -> A (Pharmacie : 2e rue à droite) | 4 -> D (Parc : à 5 minutes à pied) | 5 -> E (Poste : angle du boulevard).",
        "tier4_text": "Situation A (3 pts) : mairie | droit | gauche.\nSituation B (4 pts) : poste | rue | pont | droite (et fontaine).\nSituation C (3 pts) : passeport (ou portefeuille) | nom et prénom.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Allez tout droit, puis tournez à droite aux feux de signalisation. | 2. Où se trouve le bureau de poste le plus proche ? | 3. Traversez le pont en pierre et prenez la première rue à gauche. | 4. La mairie est située en face du parc central. | 5. Y a-t-il une pharmacie dans ce quartier historique ? | 6. La bibliothèque municipale est ouverte du mardi au samedi.\nExercice 5.2 — Intrus [4 pts] :\n1. La saucisse (produit de charcuterie, les autres sont des voies urbaines de circulation) | 2. À la vanille (parfum culinaire, les autres sont des directions de guidage spatial) | 3. Le pyjama (vêtement de nuit, les autres sont des édifices publics municipaux) | 4. Le rôti de porc (aliment carné, les autres sont des éléments de la voirie urbaine).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 30",
        "anchors_text": "1. Le piège fatal 'Tout droit' vs 'À droite' : 'Tout droit' [too drwah] signifie straight ahead (le 't' ne se prononce pas). 'À droite' [ah drwaht] signifie to the right (le 't' est fortement articulé). Un apprenant anglophone qui confond les deux se perd systématiquement !\n2. 'Mairie' vs 'Hôtel de Ville' : En France, chaque commune possède sa 'mairie'. Dans les très grandes métropoles ou villes historiques, le bâtiment principal s'appelle l'Hôtel de Ville, mais n'a strictement aucun rapport avec un hôtel touristique !\n3. 'La place' : Faux-ami courant : une place dans une ville désigne une grande esplanade piétonne publique (ex : Place de la Concorde, Place du Capitole), pas un simple siège."
    }
}

# CHAPTER 31: La campagne, la nature et les animaux
batch3["31"] = {
    "ch_num": 31,
    "title_fr": "La campagne, la nature et les animaux",
    "title_en": "Countryside, Nature, Flora & Fauna",
    "word_count": 46,
    "traps": [
        "Gender of animals & nature: 'la campagne' (f.), 'la forêt' (f.), 'la montagne' (f.), 'la rivière' (f.), but 'le champ' (silent -p!), 'le bois' (silent -s!), 'le fleuve' (m.), 'le village' (m.).",
        "Fleuve vs Rivière: 'Un fleuve' flows directly into the sea or ocean (la Seine, la Loire, le Rhône), whereas 'une rivière' flows into another river/fleuve!",
        "Animal gender pairs: le chat / la chatte, le chien / la chienne, le cheval / la jument, le coq / la poule, le taureau / la vache, le mouton / la brebis."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'P' FINAL DE CHAMP ET LES VOYELLES DE CAMPAGNE",
        "phonetic_tip_text": "'Le champ' se termine par un 'p' muet [shahn] avec voyelle nasale pure [ɑ̃]. 'La campagne' [kahm-pahny] combine la nasale [ɑ̃] et le son mouillé [ɲ]. 'L'oiseau' [wah-zoh] contient le [w] initial et le son [z] intervocalique.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de la Faune & des Paysages [4 pts]",
        "ex1_headers": ["Animal / Paysage", "Genre", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le champ (m.)", "Masculin", "Consonne 'p' muette", "[ shahn ]", "'p' muet, voyelle nasale [ɑ̃]"],
            ["2. le bois (m.)", "Masculin", "Consonne 's' muette", "[ bwah ]", "'s' muet, semi-consonne [wa]"],
            ["3. l'oiseau (m.)", "Masculin", "Graphème '-eau'", "[ wah-zoh ]", "'s' sonne [z], son [o] pur"],
            ["4. la campagne (f.)", "Féminin", "Graphème '-gn-' liquide", "[ kahm-pahny ]", "Son [ɲ] liquide mouillé"],
            ["5. le cheval (m.)", "Masculin", "Pluriel irrégulier", "[ shuh-vahl ]", "Pluriel : des chevaux [shuh-voh]"],
            ["6. la chienne (f.)", "Féminin", "Suffixe '-ienne'", "[ shyen ]", "Dénasalisée, [ɛn] sonore"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) la foret et les arbres -> ________________________",
            "b) une riviere sauvage -> ________________________",
            "c) un ane gris dans le pre -> ________________________",
            "d) un champ de ble dore -> ________________________",
            "e) des animaux domestiques -> ________________________",
            "f) une randonnee en pleine nature -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Animalières [3 pts]",
        "ex3_items": [
            "1. un animal sauvage      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des oiseaux chanteurs   -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un arbre centenaire     -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. monter à cheval         -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux ours bruns         -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand éléphant       -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES ÉLÉMENTS DE LA NATURE ET DES ANIMAUX",
        "gender_rule_text": "Nature : la forêt, la colline, la plaine, la rivière, la vallée, la mer, mais le champ, le bois, le fleuve, le lac, le ruisseau, le sentier. Animaux familiers : le chien, le chat, le cheval, le canard, le lapin, mais la vache, la poule, la souris, la grenouille.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Animaux & Milieux Naturels [6 pts]",
        "ex1_headers": ["Élément naturel", "Genre (M/F)", "Élément naturel", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ forêt (f.)", "[   ] M   [   ] F", "7. _______ cheval (m.)", "[   ] M   [   ] F"],
            ["2. _______ champ (m.)", "[   ] M   [   ] F", "8. _______ vache (f.)", "[   ] M   [   ] F"],
            ["3. _______ rivière (f.)", "[   ] M   [   ] F", "9. _______ oiseau (m.)", "[   ] M   [   ] F"],
            ["4. _______ fleuve (m.)", "[   ] M   [   ] F", "10. _______ mouton (m.)", "[   ] M   [   ] F"],
            ["5. _______ lac (m.)", "[   ] M   [   ] F", "11. _______ poule (f.)", "[   ] M   [   ] F"],
            ["6. _______ colline (f.)", "[   ] M   [   ] F", "12. _______ arbre (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. La Seine est un grand rivière qui traverse la ville de Paris.\n   Correction : _____________________________________________________________________________",
            "2. Nous avons ramassé des champignons dans un belle forêt de chênes.\n   Correction : _____________________________________________________________________________",
            "3. Le fermier possède une cheval blanc et dix vaches laitières.\n   Correction : _____________________________________________________________________________",
            "4. Ce champ de tournesols est très magnifique sous le soleil d'août.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS NATURE : FLEUVE VS RIVIÈRE & ACTIVITÉS RURALES",
        "colloc_tip_text": "Collocations : 'vivre à la campagne', 'se promener dans les bois', 'faire une randonnée en forêt', 'monter à cheval', 'nourrir les animaux de la ferme', 'adopter un chien/chat'.",
        "ex1_title": "Exercice 3.1 — Chunks Communicatifs de la Campagne [5 pts]",
        "ex1_sentences": [
            "1. Pour fuir le bruit et la pollution de la ville, ils ont choisi d'habiter à la _________ (campagne / forêt).",
            "2. En France, un cours d'eau qui se jette directement dans la mer est un _________ (fleuve / ruisseau).",
            "3. Le dimanche après-midi, nous adorons faire des _________ (randonnées / valises) sur les sentiers balisés.",
            "4. Ma petite sœur monte à _________ (cheval / voiture) au club équestre du village.",
            "5. Le fermier se lève très tôt pour s'occuper des animaux et traire les _________ (vaches / chevaux)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Animal Domestique-Habitat / Caractéristique [5 pts]",
        "ex2_headers": ["Animal", "Habitat / Rôle traditionnel", "Code association"],
        "ex2_rows": [
            ["1. Le chien...", "A. Ronronne près du poêle et chasse les souris", "1 -> [    ]"],
            ["2. La poule...", "B. Produit du lait pour fabriquer le fromage", "2 -> [    ]"],
            ["3. Le chat...", "C. Monte la garde et aboie quand un inconnu approche", "3 -> [    ]"],
            ["4. La vache...", "D. Donne de la laine douce en été", "4 -> [    ]"],
            ["5. Le mouton...", "E. Pond des œufs frais chaque matin dans le poulailler", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : SÉJOUR À LA FERME PÉDAGOGIQUE",
        "cloze_tip_text": "Complétez les récits champêtres sans aide lexicale.",
        "dialogues": [
            {
                "title": "Situation A — Promenade dans la nature (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Julien : Regarde ces magnifiques ___________________________ [trees / oaks] centenaires dans la ___________________________ [forest] !",
                    "• Claire : Oui, et écoute le chant des ___________________________ [birds] au bord de la ___________________________ [river]."
                ]
            },
            {
                "title": "Situation B — Visite des animaux de la ferme (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le fermier : Venez voir nos ___________________________ [horses] dans le pré, et voici le poulailler.",
                    "• L'enfant : Est-ce qu'on peut ramasser les ___________________________ [eggs] des poules ?",
                    "• Le fermier : Bien sûr ! Ensuite nous irons voir les ___________________________ [cows] pour la traite du ___________________________ [milk]."
                ]
            },
            {
                "title": "Situation C — Adopter un animal de compagnie (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le fils : Papa, est-ce qu'on peut adopter un petit ___________________________ [dog / puppy] ou un chaton ?",
                    "• Le père : Oui, mais il faudra le promener tous les ___________________________ [days / mornings] et bien le nourrir.",
                    "• Le fils : Je promets de m'en occuper avec beaucoup d'___________________________ [love / care] !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. We spent the weekend walking in the forest.", "-> __________________________________________________________________________________"],
            ["2. The Loire is the longest river in France that flows into the ocean.", "-> __________________________________________________________________________________"],
            ["3. My grandparents live in a small quiet village in the countryside.", "-> __________________________________________________________________________________"],
            ["4. There are cows, sheep and horses in this meadow.", "-> __________________________________________________________________________________"],
            ["5. He has a black cat and two loyal dogs.", "-> __________________________________________________________________________________"],
            ["6. We hear birds singing early in the morning.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le cheval  •  La vache  •  Le mouton  •  Le métro", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La forêt  •  Le bois  •  L'arbre  •  L'ordinateur", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le fleuve  •  La rivière  •  Le lac  •  L'addition", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Le chien  •  Le chat  •  Le lapin  •  L'hélicoptère", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le champ -> 'p' muet [shahn] | 2. le bois -> 's' muet [bwah] | 3. l'oiseau -> 's' sonne [z] [wah-zoh] | 4. la campagne -> [kahm-pahny] [ɲ] liquide | 5. le cheval -> pluriel chevaux [shuh-voh] | 6. la chienne -> [shyen].\nExercice 1.2 — Orthographe [3 pts] :\na) la forêt et les arbres | b) une rivière sauvage | c) un âne gris dans le pré | d) un champ de blé doré | e) animaux domestiques | f) une randonnée.\nExercice 1.3 — Liaisons [3 pts] :\n1. un animal [n] | 2. des oiseaux [z] | 3. un arbre [n] | 4. monter à cheval (pas de liaison) | 5. deux ours [z] | 6. un grand éléphant [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la forêt (F) | 2. le champ (M) | 3. la rivière (F) | 4. le fleuve (M) | 5. le lac (M) | 6. la colline (F) | 7. le cheval (M) | 8. la vache (F) | 9. l'oiseau (M) | 10. le mouton (M) | 11. la poule (F) | 12. l'arbre (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. La Seine est UN GRAND FLEUVE (fleuve est masculin et se jette dans la mer) | 2. UNE BELLE forêt (forêt est féminin) | 3. UN cheval blanc (cheval est masculin) | 4. Ce champ est très BEAU / magnifique (supprimer pléonasme 'très magnifique').",
        "tier3_text": "Exercice 3.1 — Chunks Campagne [5 pts] :\n1. campagne | 2. fleuve | 3. randonnées | 4. cheval | 5. vaches.\nExercice 3.2 — Paires Animaux [5 pts] :\n1 -> C (Chien garde et aboie) | 2 -> E (Poule pond des œufs) | 3 -> A (Chat ronronne et chasse les souris) | 4 -> B (Vache produit du lait) | 5 -> D (Mouton donne de la laine).",
        "tier4_text": "Situation A (3 pts) : arbres (ou chênes) | forêt (ou bois) | oiseaux | rivière.\nSituation B (4 pts) : chevaux | œufs | vaches | lait.\nSituation C (3 pts) : chien (ou chiot) | jours (ou matins) | amour (ou attention).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Nous avons passé le week-end à marcher en forêt. | 2. La Loire est le plus long fleuve de France qui se jette dans l'océan. | 3. Mes grands-parents vivent dans un petit village calme à la campagne. | 4. Il y a des vaches, des moutons et des chevaux dans ce pré. | 5. Il a un chat noir et deux chiens fidèles. | 6. Nous entendons les oiseaux chanter tôt le matin.\nExercice 5.2 — Intrus [4 pts] :\n1. Le métro (transport urbain souterrain, les autres sont des animaux d'élevage de la ferme) | 2. L'ordinateur (appareil technologique numérique, les autres sont des éléments de la forêt végétale) | 3. L'addition (document de paiement au restaurant, les autres sont des plans d'eau naturels) | 4. L'hélicoptère (aéronef mécanique, les autres sont des animaux familiers domestiques).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 31",
        "anchors_text": "1. Distinction géographique Fleuve vs Rivière : En français, un 'fleuve' se jette obligatoirement dans la mer ou l'océan (la Seine dans la Manche, la Loire dans l'Atlantique, le Rhône dans la Méditerranée). Une 'rivière' est un affluent qui se jette dans un autre cours d'eau.\n2. Le pluriel irrégulier -AL -> -AUX : 'Un cheval' devient 'des chevaux', tout comme 'un animal' devient 'des animaux'. Attention à ne jamais dire 'des chevals' !\n3. Champ avec P silencieux : 'Le champ' conserve un 'p' muet hérité du latin 'campus'. On retrouve la consonne dans les dérivés : champignon, champagne."
    }
}

# CHAPTER 32: La communication et le numérique
batch3["32"] = {
    "ch_num": 32,
    "title_fr": "La communication et le numérique",
    "title_en": "Digital Life, Smartphones, Internet & Postal Mail",
    "word_count": 45,
    "traps": [
        "French computer terminology vs English loanwords: 'un courriel' or 'un email/mail', 'un texto' or 'un SMS', 'un fichier' (file), 'le mot de passe' (password), 'la souris' (mouse).",
        "AZERTY keyboard layout: French keyboards use AZERTY instead of QWERTY, placing accented keys (é, è, ç, à) on the top numeric row.",
        "Gender traps: 'l'ordinateur' (m.), 'le smartphone' (m.), 'l'écran' (m.), 'le clavier' (m.), 'le mot de passe' (m.), 'le lien' (m.), but 'la souris' (f.), 'l'imprimante' (f.), 'l'adresse' (f.), 'la connexion' (f.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "L'ÉLISION D'ÉCRAN ET LA CONSONNE LIQUIDE DE CLAVIER",
        "phonetic_tip_text": "'L'écran' [lay-krahn] commence par une voyelle avec élision obligatoire et se termine par la voyelle nasale pure [ɑ̃]. 'Le clavier' [klah-vyay] se termine par le son [e] fermé avec consonne 'r' muette !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de l'Informatique [4 pts]",
        "ex1_headers": ["Terme numérique", "Genre", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. l'écran (m.)", "Masculin", "Graphème '-an' nasal", "[ lay-krahn ]", "Nasale [ɑ̃] pure, élision 'l''"],
            ["2. le clavier (m.)", "Masculin", "Suffixe '-er'", "[ klah-vyay ]", "'r' muet, son [e] pur"],
            ["3. la souris (f.)", "Féminin", "Consonne 's' muette", "[ soo-ree ]", "'s' final muet, son [u] doux"],
            ["4. le courriel (m.)", "Masculin", "Graphème '-iel'", "[ koor-yel ]", "'l' sonore, semi-voyelle [j]"],
            ["5. le smartphone (m.)", "Masculin", "Consonne 'ne'", "[ smaht-fohn ]", "Consonne [n] finale nette"],
            ["6. le mot de passe (m.)", "Masculin", "Consonne 't' muette", "[ moh duh pahs ]", "'t' muet dans 'mot'"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un ecran tactile -> ________________________",
            "b) un telephone portable -> ________________________",
            "c) un mot de passe securise -> ________________________",
            "d) une imprimante multifonction -> ________________________",
            "e) telecharger un fichier -> ________________________",
            "f) envoyer un message electronique -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Numériques [3 pts]",
        "ex3_items": [
            "1. un écran d'ordinateur  -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des e-mails importants -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un appel vidéo         -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. cliquer sur un lien    -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "5. deux applications      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand site web      -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DU MATÉRIEL INFORMATIQUE ET D'INTERNET",
        "gender_rule_text": "Matériel informatique : l'ordinateur (m.), l'écran (m.), le clavier (m.), le câble (m.), le chargeur (m.), le disque dur (m.), mais la souris (f.), l'imprimante (f.), la webcam (f.), la tablette (f.). Web : le site (m.), le lien (m.), le réseau (m.), le courriel (m.), mais la page web (f.), la connexion (f.), l'application (f.).",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Numérique & Télécoms [6 pts]",
        "ex1_headers": ["Élément numérique", "Genre (M/F)", "Élément numérique", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ ordinateur (m.)", "[   ] M   [   ] F", "7. _______ écran (m.)", "[   ] M   [   ] F"],
            ["2. _______ souris (f.)", "[   ] M   [   ] F", "8. _______ clavier (m.)", "[   ] M   [   ] F"],
            ["3. _______ imprimante (f.)", "[   ] M   [   ] F", "9. _______ smartphone (m.)", "[   ] M   [   ] F"],
            ["4. _______ mot de passe (m.)", "[   ] M   [   ] F", "10. _______ mot (m.)", "[   ] M   [   ] F"],
            ["5. _______ connexion (f.)", "[   ] M   [   ] F", "11. _______ site web (m.)", "[   ] M   [   ] F"],
            ["6. _______ application (f.)", "[   ] M   [   ] F", "12. _______ boîte mail (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai acheté un nouvelle souris sans fil avec connexion Bluetooth.\n   Correction : _____________________________________________________________________________",
            "2. Mon ordinateur portable a un écran très grand et lumineux.\n   Correction : _____________________________________________________________________________",
            "3. Il a tapé une faux mot de passe et son compte a été bloqué.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons installé une nouvelle imprimante laser dans le bureau.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS NUMÉRIQUES : VERBES DU WEB & DE LA TÉLÉPHONIE",
        "colloc_tip_text": "Verbes digitaux : 'envoyer un texto / un mail', 'cliquer sur un lien', 'télécharger une pièce jointe', 'taper son mot de passe', 'recharger la batterie', 'naviguer sur internet'.",
        "ex1_title": "Exercice 3.1 — Actions Numériques & Vocabulaire d'Internet [5 pts]",
        "ex1_sentences": [
            "1. Pour ouvrir le document PDF reçu, il faut _________ (cliquer / nager) sur le lien bleu.",
            "2. Avant de quitter la maison, n'oublie pas de _________ (recharger / jeter) la batterie de ton portable.",
            "3. Pour sécuriser votre compte, choisissez un _________ (mot / nom) de passe avec des chiffres et symboles.",
            "4. Tu peux m'envoyer un petit _________ (texto / timbre) dès que tu arrives à la gare ?",
            "5. Pour imprimer mon billet, je connecte mon ordinateur à l'_________ (imprimante / écran)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Outil Numérique-Fonction Pratique [5 pts]",
        "ex2_headers": ["Outil / Action digitale", "Usage pratique", "Code association"],
        "ex2_rows": [
            ["1. Le clavier d'ordinateur...", "A. Permet de cliquer et de naviguer sur l'écran", "1 -> [    ]"],
            ["2. La souris optique...", "B. Sert à taper des textes, chiffres et courriels", "2 -> [    ]"],
            ["3. Le chargeur...", "C. Connecte les appareils au réseau Internet sans fil", "3 -> [    ]"],
            ["4. La connexion Wi-Fi...", "D. Alimente la batterie du smartphone en électricité", "4 -> [    ]"],
            ["5. La pièce jointe...", "E. Fichier annexé à un courrier électronique", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : DÉPANNAGE INFORMATIQUE & MESSAGES",
        "cloze_tip_text": "Complétez les situations technologiques sans liste de vocabulaire.",
        "dialogues": [
            {
                "title": "Situation A — Problème de connexion au bureau (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Julien : Est-ce que tu as du réseau ? Ma ___________________________ [connection / Wi-Fi] ne fonctionne plus.",
                    "• Sara : Vérifie si le ___________________________ [cable / router] est bien branché sur ton ordinateur.",
                    "• Julien : Ah oui ! Et je dois aussi retaper mon ___________________________ [password]."
                ]
            },
            {
                "title": "Situation B — Envoi de documents par courriel (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le directeur : Avez-vous envoyé le ___________________________ [email] au client ce matin ?",
                    "• La secrétaire : Oui, avec le contrat en ___________________________ [attachment / pièce jointe].",
                    "• Le directeur : Très bien. Pouvez-vous aussi imprimer une copie sur l'___________________________ [printer] ?",
                    "• La secrétaire : Tout de suite, je vais cliquer sur le bouton ___________________________ [print]."
                ]
            },
            {
                "title": "Situation C — Appel sur smartphone (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Thomas : Allô Sophie ? Je t'entends très mal, mon ___________________________ [battery] est presque vide.",
                    "• Sophie : Pas de problème, envoie-moi un simple ___________________________ [text message / SMS].",
                    "• Thomas : D'accord, je t'écris dès que je trouve mon ___________________________ [charger]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. Click on the link to download the document.", "-> __________________________________________________________________________________"],
            ["2. I received an email with a photo attachment.", "-> __________________________________________________________________________________"],
            ["3. My cell phone battery is completely dead.", "-> __________________________________________________________________________________"],
            ["4. What is the Wi-Fi password in this café?", "-> __________________________________________________________________________________"],
            ["5. Send me a text message as soon as you arrive at the airport.", "-> __________________________________________________________________________________"],
            ["6. I need a new wireless mouse for my laptop.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. L'ordinateur  •  Le clavier  •  L'écran  •  La carotte", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le texto  •  L'email  •  Le coup de fil  •  Le gâteau au chocolat", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La souris  •  L'imprimante  •  Le scanner  •  Le poulet rôti", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Télécharger  •  Cliquer  •  Naviguer  •  Dormir à l'hôtel", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. l'écran -> élision et nasale [lay-krahn] | 2. le clavier -> 'r' muet [klah-vyay] | 3. la souris -> 's' muet [soo-ree] | 4. le courriel -> 'l' sonore [koor-yel] | 5. le smartphone -> consonne [n] [smaht-fohn] | 6. le mot de passe -> 't' muet [moh duh pahs].\nExercice 1.2 — Orthographe [3 pts] :\na) un écran tactile | b) un téléphone portable | c) un mot de passe sécurisé | d) une imprimante multifonction | e) télécharger un fichier | f) un message électronique.\nExercice 1.3 — Liaisons [3 pts] :\n1. un écran [n] | 2. des e-mails [z] | 3. un appel [n] | 4. sur un lien [r] et [n] | 5. deux applications [z] | 6. un grand site [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. l'ordinateur (M) | 2. la souris (F) | 3. l'imprimante (F) | 4. le mot de passe (M) | 5. la connexion (F) | 6. l'application (F) | 7. l'écran (M) | 8. le clavier (M) | 9. le smartphone (M) | 10. le mot (M) | 11. le site web (M) | 12. la boîte mail (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UNE nouvelle souris (souris est féminin) | 2. Phrase déjà correcte (ordinateur est masculin, écran est masculin) -> ou : 'un écran TRÈS GRAND' | 3. UN FAUX mot de passe (mot est masculin) | 4. Phrase correcte (imprimante est féminin).",
        "tier3_text": "Exercice 3.1 — Actions Numériques [5 pts] :\n1. cliquer | 2. recharger | 3. mot | 4. texto (ou SMS) | 5. imprimante.\nExercice 3.2 — Paires Outils Numériques [5 pts] :\n1 -> B (Clavier : taper textes et courriels) | 2 -> A (Souris : cliquer et naviguer) | 3 -> D (Chargeur : alimente la batterie) | 4 -> C (Wi-Fi : connexion Internet sans fil) | 5 -> E (Pièce jointe : fichier annexé au mail).",
        "tier4_text": "Situation A (3 pts) : connexion (ou Wi-Fi) | câble (ou routeur) | mot de passe.\nSituation B (4 pts) : courriel (ou email) | pièce jointe | imprimante | imprimer.\nSituation C (3 pts) : batterie | texto (ou message / SMS) | chargeur.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Cliquez sur le lien pour télécharger le document. | 2. J'ai reçu un courriel (ou email) avec une photo en pièce jointe. | 3. La batterie de mon téléphone portable est complètement à plat (ou vide). | 4. Quel est le mot de passe du Wi-Fi dans ce café ? | 5. Envoie-moi un texto dès que tu arrives à l'aéroport. | 6. J'ai besoin d'une nouvelle souris sans fil pour mon ordinateur portable.\nExercice 5.2 — Intrus [4 pts] :\n1. La carotte (légume alimentaire, les autres sont des composants d'ordinateur) | 2. Le gâteau au chocolat (pâtisserie sucrée, les autres sont des moyens de communication) | 3. Le poulet rôti (viande cuisinée, les autres sont des périphériques informatiques) | 4. Dormir à l'hôtel (action d'hébergement touristique, les autres sont des verbes d'action sur Internet).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 32",
        "anchors_text": "1. Le clavier AZERTY : En France, les ordinateurs utilisent la disposition de touches AZERTY (et non QWERTY). Les lettres A et Q ainsi que Z et W sont interverties, et les chiffres nécessitent d'appuyer sur la touche Majuscule !\n2. Texto vs SMS vs Mail : 'Un texto' est le terme familier et officiel français pour désigner un message court par téléphone (SMS). 'Un courriel' est le terme francophone recommandé pour un email.\n3. Batterie 'à plat' : Expression idiomatique très courante pour dire qu'un téléphone ou un ordinateur n'a plus de batterie : 'Mon portable est à plat'."
    }
}

# CHAPTER 33: L'administration française et les démarches
batch3["33"] = {
    "ch_num": 33,
    "title_fr": "L'administration française et les démarches",
    "title_en": "French Bureaucracy, Visas, Forms & Official Paperwork",
    "word_count": 46,
    "traps": [
        "Major institutions: 'La préfecture' (visa, residency permit / titre de séjour), 'la mairie' (civil registry, marriage, address attestations), 'la CAF' (housing subsidies / APL), 'la Sécurité sociale' (healthcare / Carte Vitale), 'France Travail' (unemployment agency).",
        "Administrative verbs: 'Remplir un formulaire' (to fill in a form), 'fournir un justificatif de domicile' (proof of address), 'signer en bas à droite', 'prendre un rendez-vous en ligne'.",
        "Gender traps: 'le document' (m.), 'le formulaire' (m.), 'le dossier' (m.), 'le titre de séjour' (m.), 'le justificatif' (m.), but 'la préfecture' (f.), 'la démarche' (f.), 'la pièce d'identité' (f.), 'la demande' (f.), 'la signature' (f.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'C' ET 'T' SILENCIEUX DE RESPECT ET DE JUSTIFICATIF",
        "phonetic_tip_text": "'Le justificatif' [zhyoo-stee-fee-kah-teef] fait sonner son 'f' final. 'Le dossier' [doh-syay] a un double 'ss' sonore pour [s] pur et une terminaison en '-er' avec 'r' silencieux !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Termes Administratifs [4 pts]",
        "ex1_headers": ["Terme officiel", "Genre", "Caractéristique phonétique", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le dossier (m.)", "Masculin", "Suffixe '-ier'", "[ doh-syay ]", "'r' muet, double 'ss' sonne [s]"],
            ["2. le formulaire (m.)", "Masculin", "Suffixe '-aire'", "[ fohr-myoo-lair ]", "Son [y] puis voyelle [ɛʁ]"],
            ["3. la préfecture (f.)", "Féminin", "Accent aigu 'é'", "[ pray-fek-tyoor ]", "Accent aigu [e], son [yʁ]"],
            ["4. le titre de séjour (m.)", "Masculin", "Consonne 'r' sonore", "[ teetr duh say-zhoor ]", "'r' sonore doux, son [ʒ]"],
            ["5. le justificatif (m.)", "Masculin", "Consonne 'f' sonore", "[ zhyoo-stee-fee-kah-teef ]", "'f' final bien articulé"],
            ["6. la signature (f.)", "Féminin", "Graphème '-gn-' liquide", "[ see-nyah-tyoor ]", "Son mouillé [ɲ], [yʁ] final"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) la prefecture du departement -> ________________________",
            "b) une piece d'identite officielle -> ________________________",
            "c) un justificatif de domicile recent -> ________________________",
            "d) renouveler son titre de sejour -> ________________________",
            "e) remplir un formulaire en ligne -> ________________________",
            "f) signer le document administratif -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Officielles [3 pts]",
        "ex3_items": [
            "1. un acte de naissance    -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des avis d'imposition   -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un étranger en France   -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. sans aucun justificatif -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "5. deux exemplaires        -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand bureau public  -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES DOCUMENTS OFFICIELS ET INSTITUTIONS",
        "gender_rule_text": "Documents masculins majeurs : le passeport, le visa, le formulaire, le dossier, le titre de séjour, l'acte de naissance, le justificatif de domicile, le certificat. Féminins : la préfecture, la mairie, la pièce d'identité, la démarche, la signature, la demande, la photocopie, l'attestation.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Papiers & Administration [6 pts]",
        "ex1_headers": ["Terme administratif", "Genre (M/F)", "Terme administratif", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ passeport (m.)", "[   ] M   [   ] F", "7. _______ préfecture (f.)", "[   ] M   [   ] F"],
            ["2. _______ pièce d'identité (f.)", "[   ] M   [   ] F", "8. _______ formulaire (m.)", "[   ] M   [   ] F"],
            ["3. _______ titre de séjour (m.)", "[   ] M   [   ] F", "9. _______ dossier (m.)", "[   ] M   [   ] F"],
            ["4. _______ signature (f.)", "[   ] M   [   ] F", "10. _______ attestation (f.)", "[   ] M   [   ] F"],
            ["5. _______ justificatif (m.)", "[   ] M   [   ] F", "11. _______ démarche (f.)", "[   ] M   [   ] F"],
            ["6. _______ demande (f.)", "[   ] M   [   ] F", "12. _______ acte de naissance (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai déposé une nouveau dossier complet pour ma demande de passeport.\n   Correction : _____________________________________________________________________________",
            "2. Veuillez apporter un justificatif de domicile récente de moins de trois mois.\n   Correction : _____________________________________________________________________________",
            "3. Le préfecture m'a envoyé une convocation pour le retrait de ma carte.\n   Correction : _____________________________________________________________________________",
            "4. N'oubliez pas d'apposer votre signature officiel au bas de chaque page.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS BUREAUCRATIQUES : LES DÉMARCHES EN PRÉFECTURE",
        "colloc_tip_text": "Expressions indispensables de l'administration française : 'remplir un formulaire', 'fournir un justificatif de domicile', 'déposer un dossier', 'prendre rendez-vous sur le site de la préfecture', 'renouveler son titre de séjour', 'pièce d'identité en cours de validité'.",
        "ex1_title": "Exercice 3.1 — Formules Administratives & Verbes de Procédure [5 pts]",
        "ex1_sentences": [
            "1. Pour toute démarche officielle, vous devez fournir un _________ (justificatif / menu) de domicile de moins de 3 mois.",
            "2. Avant de vous présenter au guichet, veuillez _________ (remplir / chanter) soigneusement ce formulaire Cerfa.",
            "3. Les résidents étrangers doivent renouveler leur titre de _________ (séjour / voyage) chaque année.",
            "4. N'oubliez pas d'apposer votre _________ (signature / valise) en bas à droite de la déclaration.",
            "5. L'agent administratif vérifie que toutes les pièces du dossier sont bien _________ (conformes / cassées)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Institution-Démarche Assignée [5 pts]",
        "ex2_headers": ["Organisme public français", "Démarche correspondante", "Code association"],
        "ex2_rows": [
            ["1. La Préfecture...", "A. Demande d'allocations de logement familial (APL)", "1 -> [    ]"],
            ["2. La Mairie...", "B. Délivrance des titres de séjour et permis de conduire", "2 -> [    ]"],
            ["3. La CAF...", "C. Inscription sur les listes électorales et mariages", "3 -> [    ]"],
            ["4. La Sécurité sociale...", "D. Recherche d'emploi et indemnisation chômage", "4 -> [    ]"],
            ["5. France Travail...", "E. Remboursement des frais médicaux et Carte Vitale", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : AU GUICHET DE L'ADMINISTRATION",
        "cloze_tip_text": "Complétez les interactions administratives sans banque de mots.",
        "dialogues": [
            {
                "title": "Situation A — Dépôt de dossier en préfecture (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• L'agent : Bonjour Monsieur, vous venez pour le ___________________________ [renewal] de votre titre de séjour ?",
                    "• L'usager : Oui, voici mon ___________________________ [file / folder] complet avec toutes les pièces demandées.",
                    "• L'agent : Très bien. Avez-vous une ___________________________ [proof of address] récente ?"
                ]
            },
            {
                "title": "Situation B — À la mairie pour un acte d'état civil (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• La dame : Bonjour, je voudrais un extrait d'___________________________ [birth certificate] pour mon fils.",
                    "• L'employé : Certainement. Pouvez-vous me présenter votre pièce d'___________________________ [identity card] ?",
                    "• La dame : La voici. Faut-il aussi ___________________________ [to fill] un formulaire de demande ?",
                    "• L'employé : Non, c'est immédiat. Veuillez juste apposer votre ___________________________ [signature] ici."
                ]
            },
            {
                "title": "Situation C — Rendez-vous à la CAF pour les aides au logement (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le conseiller : Bonjour, vous avez créé votre compte sur le ___________________________ [website / internet] de la CAF ?",
                    "• L'étudiant : Oui, et j'ai téléchargé mon attestation de ___________________________ [housing / rent].",
                    "• Le conseiller : Parfait, votre demande d'aide personnalisée au ___________________________ [housing / APL] est validée."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. You must fill out this official form and sign at the bottom.", "-> __________________________________________________________________________________"],
            ["2. I have an appointment at the prefecture to renew my residency permit.", "-> __________________________________________________________________________________"],
            ["3. Please bring a valid proof of address less than three months old.", "-> __________________________________________________________________________________"],
            ["4. The town hall issued my official birth certificate.", "-> __________________________________________________________________________________"],
            ["5. Do you have a photocopy of your passport and visa?", "-> __________________________________________________________________________________"],
            ["6. My social security file is currently being processed.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La préfecture  •  La mairie  •  Le commissariat  •  La boulangerie", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le passeport  •  La carte d'identité  •  Le titre de séjour  •  Le croissant", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Remplir un formulaire  •  Fournir un justificatif  •  Signer un document  •  Prendre un café en terrasse", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La CAF  •  La Sécurité sociale  •  France Travail  •  La Tour Eiffel", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le dossier -> [doh-syay] 'r' muet | 2. le formulaire -> [fohr-myoo-lair] | 3. la préfecture -> [pray-fek-tyoor] | 4. le titre de séjour -> [teetr duh say-zhoor] | 5. le justificatif -> [zhyoo-stee-fee-kah-teef] 'f' sonore | 6. la signature -> [see-nyah-tyoor] [ɲ] liquide.\nExercice 1.2 — Orthographe [3 pts] :\na) la préfecture du département | b) une pièce d'identité officielle | c) un justificatif de domicile récent | d) renouveler son titre de séjour | e) remplir un formulaire | f) signer le document administratif.\nExercice 1.3 — Liaisons [3 pts] :\n1. un acte [n] | 2. des avis [z] | 3. un étranger [n] | 4. sans aucun [n] | 5. deux exemplaires [z] | 6. un grand bureau [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. le passeport (M) | 2. la pièce d'identité (F) | 3. le titre de séjour (M) | 4. la signature (F) | 5. le justificatif (M) | 6. la demande (F) | 7. la préfecture (F) | 8. le formulaire (M) | 9. le dossier (M) | 10. l'attestation (F) | 11. la démarche (F) | 12. l'acte de naissance (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UN NOUVEAU dossier (dossier est masculin) | 2. Un justificatif RÉCENT (justificatif est masculin) | 3. LA préfecture (préfecture est féminin) | 4. Votre signature OFFICIELLE (signature est féminin).",
        "tier3_text": "Exercice 3.1 — Formules Administratives [5 pts] :\n1. justificatif | 2. remplir | 3. séjour | 4. signature | 5. conformes.\nExercice 3.2 — Paires Institutions [5 pts] :\n1 -> B (Préfecture : titres de séjour) | 2 -> C (Mairie : état civil et élections) | 3 -> A (CAF : allocations logement APL) | 4 -> E (Sécurité sociale : frais médicaux) | 5 -> D (France Travail : recherche d'emploi).",
        "tier4_text": "Situation A (3 pts) : renouvellement | dossier | justificatif de domicile (ou attestation).\nSituation B (4 pts) : naissance | identité | remplir | signature.\nSituation C (3 pts) : site (ou portail) | loyer (ou hébergement) | logement (APL).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Vous devez remplir ce formulaire officiel et signer en bas. | 2. J'ai un rendez-vous à la préfecture pour renouveler mon titre de séjour. | 3. Veuillez apporter un justificatif de domicile valide de moins de trois mois. | 4. La mairie a délivré mon acte de naissance officiel. | 5. Avez-vous une photocopie de votre passeport et de votre visa ? | 6. Mon dossier de sécurité sociale est actuellement en cours de traitement.\nExercice 5.2 — Intrus [4 pts] :\n1. La boulangerie (commerce de bouche privé, les autres sont des administrations publiques d'État ou municipales) | 2. Le croissant (viennoiserie alimentaire, les autres sont des titres d'identité officiels) | 3. Prendre un café en terrasse (activité de loisir et détente, les autres sont des actes administratifs formels) | 4. La Tour Eiffel (monument historique touristique, les autres sont des organismes publics sociaux français).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 33",
        "anchors_text": "1. Le justificatif de domicile de moins de 3 mois : En France, c'est le document obligatoire numéro 1 pour presque toutes les démarches (facture d'électricité EDF, facture Internet, quittance de loyer).\n2. Le 'Titre de Séjour' : Pour un étranger non européen résidant en France, le titre de séjour (délivré par la Préfecture) est le document clé qui atteste de son droit légal de résider et de travailler en France.\n3. La CAF et les APL : La Caisse d'Allocations Familiales gère l'Aide Personnalisée au Logement (APL), une subvention mensuelle essentielle versée aux étudiants et familles pour payer leur loyer."
    }
}

with open("chapters_batch_3.json", "w", encoding="utf-8") as f:
    json.dump(batch3, f, ensure_ascii=False, indent=2)

print("Batch 3 successfully finalized! All chapters present:", sorted([int(k) for k in batch3.keys()]))
