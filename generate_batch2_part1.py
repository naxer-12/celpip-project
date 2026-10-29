import json

batch2 = {}

# CHAPTER 12
batch2["12"] = {
    "ch_num": 12,
    "title_fr": "L'éducation et le système scolaire",
    "title_en": "The French School System & Studies",
    "word_count": 40,
    "traps": [
        "French school ladder acronyms & names: l'école maternelle (ages 3-6), l'école primaire (6-11), le collège (11-15, leads to Brevet), le lycée (15-18, leads to Baccalauréat), l'université / la fac.",
        "False cognate: 'Le collège' is middle school / junior high, NOT college/university! College is 'l'université' or 'l'école supérieure'.",
        "Student titles: un élève (primary/secondary school student), un étudiant / une étudiante (university student)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'C' ET LE 'T' FINAL DU BACCALAURÉAT ET BREVET",
        "phonetic_tip_text": "Dans les diplômes : 'le baccalauréat' [bah-kah-loh-ray-ah] a un 't' muet (souvent abrégé en 'le bac' [bahk] avec 'c' sonné). 'Le brevet' [bruh-vay] a 'et' prononcé [e]. 'Étudiant' [ay-too-dyanh] a la nasale [ɑ̃].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Vocabulaire Scolaire [4 pts]",
        "ex1_headers": ["Terme scolaire", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le baccalauréat", "Consonne 't' finale", "[  ] Oui", "[  ] Oui", "[ bah-kah-loh-ray-ah ]"],
            ["2. le bac (abréviation)", "Consonne 'c' finale", "[  ] Oui [k]", "[  ] Non", "[ bahk ]"],
            ["3. le brevet", "Consonne 't' finale", "[  ] Oui", "[  ] Oui", "[ bruh-vay ]"],
            ["4. un étudiant (m.)", "Voyelle nasale 'an'", "[  ] Nasale [ɑ̃]", "[  ] Orale [an]", "[ ay-too-dyanh ]"],
            ["5. une étudiante (f.)", "Consonne 't' réveillée", "[  ] Oui [t]", "[  ] Non", "[ ay-too-dyahnt ]"],
            ["6. le collège (m.)", "Consonne 'g' douce", "[  ] [koh-lezh]", "[  ] [koh-layg]", "[ koh-lezh ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique de l'Éducation [3 pts]",
        "ex2_items": [
            "a) l'ecole primaire -> ________________________",
            "b) le lycee -> ________________________",
            "c) le diplome -> ________________________",
            "d) l'universite -> ________________________",
            "e) etudier -> ________________________",
            "f) reussir un examen -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Scolaires [3 pts]",
        "ex3_items": [
            "1. un élève         -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. un étudiant      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "3. les examens      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "4. passer un examen -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "5. deux écoles      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. grand amphithéâtre -> [  ] Liaison [t] obligatoire  [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES ÉTABLISSEMENTS SCOLAIRES",
        "gender_rule_text": "Les établissements scolaires : L'école (f.), l'université (f.), la faculté / la fac (f.) ; mais LE collège (m.), LE lycée (m.), LE rectorat (m.). Les diplômes sont masculins : LE brevet, LE bac, LE diplôme, LE master.",
        "ex1_title": "Exercice 2.1 — Matrice des Niveaux Scolaires & Âges en France [6 pts]",
        "ex1_headers": ["Établissement (Genre)", "Tranche d'âge", "Diplôme visé", "Titre de l'apprenant"],
        "ex1_rows": [
            ["1. L'école maternelle (f.)", "3 à 6 ans", "Aucun (initiation)", "l'écolier / l'écolière"],
            ["2. L'école primaire (f.)", "6 à 11 ans", "Passage en 6e", "l'élève"],
            ["3. Le collège (m.)", "11 à 15 ans", "Le Brevet des collèges", "le/la collégien(ne)"],
            ["4. Le lycée (m.)", "15 à 18 ans", "Le Baccalauréat (Bac)", "le/la lycéen(ne)"],
            ["5. L'université (f.)", "18 ans et plus", "Licence / Master / Doctorat", "l'étudiant(e)"],
            ["6. Les grandes écoles (f.)", "Bac+2 à Bac+5", "Diplôme d'ingénieur/commerce", "l'élève ingénieur"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Mon fils aîné étudie dans un grande université à Toulouse.\n   Correction : _____________________________________________________________________________",
            "2. Elle a obtenu son baccalauréat dans la prestigieux lycée Henri IV.\n   Correction : _____________________________________________________________________________",
            "3. Sarah est un étudiante très sérieuse en première année.\n   Correction : _____________________________________________________________________________",
            "4. Il a réussi son examen et a reçu une beau diplôme.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS D'EXAMENS : PASSER VS RÉUSSIR",
        "colloc_tip_text": "Faux-ami critique en FLE : 'Passer un examen' = se présenter à l'examen (to take an exam), cela ne veut PAS dire qu'on a réussi ! Pour dire qu'on l'a réussi, on emploie : 'Réussir un examen' (to pass an exam) !",
        "ex1_title": "Exercice 3.1 — Verbes Scolaires (PASSER vs RÉUSSIR vs ÉTUDIER) [5 pts]",
        "ex1_sentences": [
            "1. Demain matin, les lycéens vont _________ (passer / réussir) leur épreuve de philosophie.",
            "2. Félicitations ! Tu as _________ (réussi / passé) ton bac avec mention très bien !",
            "3. Mon frère aîné _________ (étudie / passe) le droit à l'université de la Sorbonne.",
            "4. Malheureusement, s'il a de mauvaises notes, il va devoir _________ (redoubler / réussir) son année.",
            "5. Les étudiants doivent _________ (réviser / redoubler) leurs cours avant la session de partiels."
        ],
        "ex2_title": "Exercice 3.2 — Paires Actions Scolaires & Résultats [5 pts]",
        "ex2_headers": ["Action scolaire", "Conséquence académique", "Association"],
        "ex2_rows": [
            ["1. Travailler avec rigueur...", "A. redoubler sa classe et reprendre l'année", "1 -> [    ]"],
            ["2. Obtenir 18/20...", "B. réussir son examen avec mention", "2 -> [    ]"],
            ["3. Avoir de mauvaises notes...", "C. valider son diplôme d'études supérieures", "3 -> [    ]"],
            ["4. Terminer son master...", "D. avoir d'excellents résultats au bulletin", "4 -> [    ]"],
            ["5. Sécher les cours...", "E. être convoqué par le directeur d'école", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE PARCOURS SCOLAIRE ET UNIVERSITAIRE",
        "cloze_tip_text": "Complétez les conversations sur le système scolaire français en évitant le faux-ami du mot 'collège'.",
        "dialogues": [
            {
                "title": "Situation A — Orientation scolaire après la 3e",
                "points": "3 pts",
                "lines": [
                    "• Le professeur : Quel âge a votre fils maintenant ?",
                    "• La mère : Il a 14 ans ; il termine le ___________________________ [middle school - m.] cette année.",
                    "• Le professeur : Parfait. L'année prochaine, il va entrer au ___________________________ [high school - m.] pour préparer son ___________________________ [Baccalaureate / Bac]."
                ]
            },
            {
                "title": "Situation B — Rentrée à l'université",
                "points": "4 pts",
                "lines": [
                    "• Julie : Tu es inscrite dans quelle ___________________________ [university / fac] ?",
                    "• Léa : À l'université Paris 1. Je suis ___________________________ [student - f.] en sciences politiques.",
                    "• Julie : Tu as beaucoup de cours magistraux en ___________________________ [lecture hall - amphi] ?",
                    "• Léa : Oui, et des travaux dirigés en petits groupes."
                ]
            },
            {
                "title": "Situation C — Résultats d'examen de fin d'année",
                "points": "3 pts",
                "lines": [
                    "• Marc : Alors, tu as ___________________________ [passed / succeeded in] ton examen ?",
                    "• Thomas : Oui ! J'ai eu mon ___________________________ [diploma] avec mention !",
                    "• Marc : Bravo, c'est formidable !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. My daughter is a university student in Lyon.", "-> __________________________________________________________________________________"],
            ["2. He goes to high school by bus every morning.", "-> __________________________________________________________________________________"],
            ["3. She took her Baccalaureate exam in June.", "-> __________________________________________________________________________________"],
            ["4. My younger brother is in middle school (collège).", "-> __________________________________________________________________________________"],
            ["5. Did you pass your history exam? (informal with 'tu')", "-> __________________________________________________________________________________"],
            ["6. We have class from Monday to Friday.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. L'école primaire  •  Le collège  •  Le lycée  •  L'usine",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le brevet  •  Le baccalauréat  •  Le diplôme  •  Le stylo",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Un élève  •  Un étudiant  •  Un collégien  •  Un médecin",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Réviser  •  Étudier  •  Apprendre  •  Dormir",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. baccalauréat -> 't' muet [bah-kah-loh-ray-ah] | 2. bac -> 'c' articulé franc [bahk] | 3. brevet -> 't' muet [bruh-vay] | 4. étudiant -> nasale [ɑ̃] [ay-too-dyanh] | 5. étudiante -> 't' prononcé [ay-too-dyahnt] | 6. collège -> 'g' doux [koh-lezh].\n\nExercice 1.2 — Orthographe [3 pts] :\na) l'école primaire (accent aigu sur é) | b) le lycée (accent aigu) | c) le diplôme (circonflexe sur 'ô') | d) l'université | e) étudier (accent aigu) | f) réussir un examen.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un élève -> Liaison en [n] obligatoire [œ̃.ne.lɛv] | 2. un étudiant -> Liaison en [n] [œ̃.ne.ty.djɑ̃] | 3. les examens -> Liaison en [z] [le.zɛg.za.mɛ̃] | 4. passer un examen -> Liaison en [n] | 5. deux écoles -> Liaison en [z] [dø.ze.kɔl] | 6. grand amphithéâtre -> Liaison en [t] [gʁɑ̃.tɑ̃.fi.te.atʁ].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. l'écolier | 2. l'élève | 3. le/la collégien(ne) | 4. le/la lycéen(ne) | 5. l'étudiant(e) | 6. l'élève ingénieur.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'UNE grande université' (université est féminin : une grande université).\n2. 'LE prestigieux lycée' (lycée est masculin : le lycée).\n3. 'Sarah est UNE étudiante' (accord féminin avec Sarah).\n4. 'UN BEAU diplôme' (diplôme est masculin : un beau diplôme).",
        "tier3_text": "Exercice 3.1 — Verbes Scolaires [5 pts] :\n1. passer (se présenter à l'épreuve) | 2. réussi (avoir l'examen avec succès) | 3. étudie | 4. redoubler | 5. réviser.\n\nExercice 3.2 — Paires Actions [5 pts] :\n1 -> D (Travailler -> excellents résultats au bulletin) | 2 -> B (Avoir 18/20 -> mention) | 3 -> A (Mauvaises notes -> redoubler) | 4 -> C (Terminer son master -> valider son diplôme) | 5 -> E (Sécher les cours -> convoqué par le directeur).",
        "tier4_text": "Situation A (3 pts) : collège | lycée | bac (ou baccalauréat).\nSituation B (4 pts) : université (ou fac) | étudiante | amphithéâtre (ou amphi).\nSituation C (3 pts) : réussi | diplôme.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Ma fille est étudiante à l'université à Lyon (ou : étudiante à Lyon).\n2. Il va au lycée en bus tous les matins.\n3. Elle a passé son baccalauréat en juin.\n4. Mon petit frère est au collège.\n5. Tu as réussi ton examen d'histoire ?\n6. Nous avons cours du lundi au vendredi.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. L'usine (site de production industrielle, les 3 autres sont des institutions d'enseignement scolaire).\n2. Le stylo (outil d'écriture de papeterie, les 3 autres sont des diplômes / certifications académiques).\n3. Un médecin (professionnel de santé en exercice, les 3 autres sont des statuts d'élèves / étudiants apprenants).\n4. Dormir (action de repos biologique, les 3 autres sont des verbes cognitifs de travail scolaire).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 12",
        "anchors_text": "1. Le faux-ami du Collège : Ne confondez jamais : en France, 'le collège' accueille les élèves de 11 à 15 ans (Junior High / Middle School) ! L'université s'appelle 'l'université' ou 'la faculté' (la fac).\\n2. Passer vs Réussir : 'Passer un examen' = to sit / take an exam (sans présumer du résultat). 'Réussir un examen' = to pass an exam with success !\\n3. Le Baccalauréat (Le Bac) : C'est le diplôme national emblématique qui clôture le lycée à 18 ans et ouvre obligatoirement les portes des études universitaires supérieures."
    }
}

# CHAPTER 13
batch2["13"] = {
    "ch_num": 13,
    "title_fr": "Le matériel scolaire et les matières",
    "title_en": "School Supplies, Stationery & Academic Subjects",
    "word_count": 42,
    "traps": [
        "Stationery genders: LA trousse (pencil case), LA règle (ruler), LA gomme (eraser), LA calculatrice (calculator) ; LE stylo (pen), LE crayon (pencil), LE cahier (notebook), LE sac à dos (backpack).",
        "School subjects prepositions: 'être bon/fort en' (en mathématiques, en histoire, en français), 'être nul en' (en sciences).",
        "Subject abbreviations: les maths (mathématiques), l'histoire-géo (histoire-géographie), les SVT (sciences de la vie et de la terre), l'EPS (éducation physique et sportive)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "PRONONCIATION DES DIGRAPHES ET VOYELLES NASALES DU MATÉRIEL",
        "phonetic_tip_text": "Dans la trousse : 'le crayon' [kray-yohn] a le son [jɔ̃]. 'Le cahier' [kah-yay] se termine en [e] avec 'r' silencieux. 'La règle' [reh-gl] a l'accent grave ouvert [ɛ]. 'Les ciseaux' [see-zoh] ont un 'x' muet.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de la Trousse et des Matières [4 pts]",
        "ex1_headers": ["Objet scolaire", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le cahier (m.)", "Consonne 'r' finale", "[  ] Oui", "[  ] Oui", "[ kah-yay ]"],
            ["2. les ciseaux (pl.)", "Consonne 'x' finale", "[  ] Oui", "[  ] Oui", "[ see-zoh ]"],
            ["3. le crayon (m.)", "Voyelle nasale 'on'", "[  ] Nasale [ɔ̃]", "[  ] Orale [on]", "[ kray-yohn ]"],
            ["4. la règle (f.)", "Accent grave 'è'", "[  ] [ɛ] ouvert", "[  ] [e] fermé", "[ reh-gl ]"],
            ["5. les maths (pl.)", "Consonne 'ths'", "[  ] Oui", "[  ] Oui", "[ maht ]"],
            ["6. la trousse (f.)", "Digraphe 'ou'", "[  ] [troos]", "[  ] [trows]", "[ troos ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique du Matériel [3 pts]",
        "ex2_items": [
            "a) la regle -> ________________________",
            "b) les mathematiques -> ________________________",
            "c) la geographie -> ________________________",
            "d) un classeur -> ________________________",
            "e) une calculatrice -> ________________________",
            "f) les ciseaux -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Fournitures [3 pts]",
        "ex3_items": [
            "1. un effaceur       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des crayons      -> [  ] Liaison                    [  ] Pas de liaison",
            "3. les enfants      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "4. un sac à dos     -> [  ] Liaison                    [  ] Pas de liaison",
            "5. deux affiches    -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un agenda        -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES FOURNITURES SCOLAIRES",
        "gender_rule_text": "Objets de papeterie : LA trousse, LA règle, LA gomme, LA colle, LA feuille ; LE stylo, LE crayon, LE feutre, LE cahier, LE livre, LE taille-crayon, LE classeur.",
        "ex1_title": "Exercice 2.1 — Matrice des Objets Scolaires & Usages [6 pts]",
        "ex1_headers": ["Fourniture (Genre)", "Article défini (le/la/l')", "Action scolaire associée", "Sens anglais"],
        "ex1_rows": [
            ["1. Trousse (f.)", "-> la trousse", "ranger stylos et crayons", "Pencil case"],
            ["2. Règle (f.)", "-> la règle", "tracer un trait droit", "Ruler"],
            ["3. Gomme (f.)", "-> la gomme", "effacer une erreur", "Eraser"],
            ["4. Stylo (m.)", "-> le stylo", "écrire à l'encre bleue", "Pen"],
            ["5. Cahier (m.)", "-> le cahier", "prendre des notes de cours", "Notebook"],
            ["6. Sac à dos (m.)", "-> le sac à dos", "porter ses manuels scolaires", "Backpack"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai oublié mon trousse de crayons à la maison.\n   Correction : _____________________________________________________________________________",
            "2. Prête-moi ton règle pour souligner le titre en rouge.\n   Correction : _____________________________________________________________________________",
            "3. Il a acheté une nouveau cahier d'exercices de mathématiques.\n   Correction : _____________________________________________________________________________",
            "4. Ma gomme est bleu et mon taille-crayon est vert.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE MATIÈRES : 'ÊTRE FORT EN' VS 'ÊTRE NUL EN'",
        "colloc_tip_text": "Pour exprimer son niveau dans une discipline : ÊTRE BON / FORT EN (en maths, en histoire, en anglais) ; à l'inverse : ÊTRE NUL EN (en physique, en sciences). Notez la préposition 'EN' obligatoire !",
        "ex1_title": "Exercice 3.1 — Prépositions et Niveaux dans les Matières [5 pts]",
        "ex1_sentences": [
            "1. Lucas adore les chiffres ; il est très fort _________ (en / à la) mathématiques.",
            "2. Sophie a des difficultés avec les dates ; elle est un peu faible _________ (en / aux) histoire.",
            "3. Mon frère bilingue a toujours 20/20 _________ (en / au) anglais.",
            "4. Nous avons cours d'EPS _________ (au / dans le) gymnase le mardi après-midi.",
            "5. Pour demain, nous devons lire le chapitre 4 _________ (de / en) français."
        ],
        "ex2_title": "Exercice 3.2 — Paires Matières Scolaires & Contenus [5 pts]",
        "ex2_headers": ["Matière scolaire", "Contenu étudié", "Association"],
        "ex2_rows": [
            ["1. Les mathématiques...", "A. cartes de géographie, fleuves et dates historiques", "1 -> [    ]"],
            ["2. L'histoire-géo...", "B. théorèmes de géométrie, calculs et algèbre", "2 -> [    ]"],
            ["3. Les sciences (SVT)...", "C. grammaire, lecture de romans et dictées", "3 -> [    ]"],
            ["4. Le français...", "D. anatomie des plantes, corps humain et biologie", "4 -> [    ]"],
            ["5. Les arts plastiques...", "E. dessin, peinture et histoire des chefs-d'œuvre", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE LA CLASSE ET DES FOURNITURES",
        "cloze_tip_text": "Complétez les dialogues scolaires avec les noms exacts de fournitures et de matières scolaires.",
        "dialogues": [
            {
                "title": "Situation A — Prêt de matériel en plein cours",
                "points": "3 pts",
                "lines": [
                    "• Thomas : Tu peux me prêter un ___________________________ [pen / stylo] rouge, s'il te plaît ?",
                    "• Camille : Oui, regarde dans ma ___________________________ [pencil case]. Tu as aussi besoin d'une ___________________________ [ruler] ?",
                    "• Thomas : Non merci, j'ai ce qu'il faut."
                ]
            },
            {
                "title": "Situation B — Préparer son cartable le soir",
                "points": "4 pts",
                "lines": [
                    "• Maman : Tu as mis tous tes livres dans ton ___________________________ [backpack] ?",
                    "• Hugo : Oui, j'ai pris mon ___________________________ [notebook] de français et mon livre de ___________________________ [maths / mathematics].",
                    "• Maman : N'oublie pas ta ___________________________ [calculator] pour le cours de sciences !"
                ]
            },
            {
                "title": "Situation C — Discussion sur les matières préférées",
                "points": "3 pts",
                "lines": [
                    "• Léa : Quelle est ta ___________________________ [subject - matière] préférée au collège ?",
                    "• Antoine : J'adore ___________________________ [history-geography] et les langues vivantes. Et toi ?",
                    "• Léa : Moi, je préfère les ___________________________ [sciences / biology]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. Open your notebook and take a blue pen.", "-> __________________________________________________________________________________"],
            ["2. I have an eraser and a pair of scissors in my pencil case.", "-> __________________________________________________________________________________"],
            ["3. She is very good at mathematics and sciences.", "-> __________________________________________________________________________________"],
            ["4. What is your favorite school subject?", "-> __________________________________________________________________________________"],
            ["5. He has forgotten his backpack in the classroom.", "-> __________________________________________________________________________________"],
            ["6. We have a geography test tomorrow morning.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Le stylo  •  Le crayon  •  La gomme  •  L'avion",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Les mathématiques  •  L'histoire  •  La géographie  •  Le canapé",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La trousse  •  La règle  •  La colle  •  Le professeur",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Être fort en  •  Être bon en  •  Être nul en  •  Prendre le métro",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. cahier -> 'r' muet [kah-yay] | 2. ciseaux -> 'x' muet [see-zoh] | 3. crayon -> nasale [ɔ̃] [kray-yohn] | 4. règle -> [ɛ] ouvert [reh-gl] | 5. maths -> [maht] | 6. trousse -> [troos].\n\nExercice 1.2 — Orthographe [3 pts] :\na) la règle (accent grave sur è) | b) les mathématiques (accent aigu sur é) | c) la géographie (accent aigu sur é) | d) un classeur | e) une calculatrice | f) les ciseaux (avec 'x').\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un effaceur -> Liaison en [n] obligatoire [œ̃.ne.fa.sœʁ] | 2. des crayons -> Pas de liaison | 3. les enfants -> Liaison en [z] [le.zɑ̃.fɑ̃] | 4. un sac à dos -> Pas de liaison | 5. deux affiches -> Liaison en [z] [dø.za.fiʃ] | 6. un agenda -> Liaison en [n] [œ̃.na.ʒɛ̃.da].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. la trousse | 2. la règle | 3. la gomme | 4. le stylo | 5. le cahier | 6. le sac à dos.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'MA trousse' (trousse est féminin : ma trousse).\n2. 'TA règle' (règle est féminin : ta règle).\n3. 'UN NOUVEAU cahier' (cahier est masculin : un nouveau cahier).\n4. 'Ma gomme est BLEUE' (accord féminin avec gomme).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. en mathématiques | 2. en histoire | 3. en anglais | 4. au gymnase | 5. de français.\n\nExercice 3.2 — Paires Matières [5 pts] :\n1 -> B (Mathématiques -> géométrie et calculs) | 2 -> A (Histoire-géo -> cartes et dates) | 3 -> D (Sciences SVT -> biologie et corps humain) | 4 -> C (Français -> grammaire et dictées) | 5 -> E (Arts plastiques -> dessin et peinture).",
        "tier4_text": "Situation A (3 pts) : stylo | trousse | règle.\nSituation B (4 pts) : sac à dos | cahier | maths (ou mathématiques) | calculatrice.\nSituation C (3 pts) : matière | l'histoire-géographie (ou l'histoire) | sciences (ou SVT).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Ouvre ton cahier et prends un stylo bleu.\n2. J'ai une gomme et une paire de ciseaux dans ma trousse.\n3. Elle est très forte en mathématiques et en sciences.\n4. Quelle est ta matière scolaire préférée ?\n5. Il a oublié son sac à dos dans la salle de classe.\n6. Nous avons une interrogation de géographie demain matin.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. L'avion (moyen de transport aérien, les 3 autres sont des petits outils d'écriture de papeterie scolaire).\n2. Le canapé (meuble de salon pour s'asseoir, les 3 autres sont des disciplines scolaires d'apprentissage).\n3. Le professeur (personne humaine enseignante, les 3 autres sont des fournitures scolaires matérielles inanimées).\n4. Prendre le métro (action de mobilité dans les transports urbains, les 3 autres sont des locutions de niveau scolaire avec 'en').",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 13",
        "anchors_text": "1. La préposition des disciplines : On utilise systématiquement 'EN' pour indiquer son niveau de performance scolaire : 'Je suis fort EN maths', 'Elle est nulle EN anglais' (et non 'dans' ou 'à').\\n2. Le genre des fournitures : Presque tous les outils de mesure et de correction sont féminins (LA règle, LA gomme, LA colle, LA trousse), tandis que les instruments d'écriture sont masculins (LE crayon, LE stylo, LE feutre, LE taille-crayon).\\n3. Les sigles scolaires courants : EPS = Éducation Physique et Sportive (gym) ; SVT = Sciences de la Vie et de la Terre (biologie/géologie)."
    }
}

with open("chapters_batch_2.json", "w", encoding="utf-8") as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

print("Batch 2 part 1 (Ch 12 & 13) saved.")
