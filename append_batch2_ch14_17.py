import json

with open("chapters_batch_2.json", "r", encoding="utf-8") as f:
    batch2 = json.load(f)

# CHAPTER 14
batch2["14"] = {
    "ch_num": 14,
    "title_fr": "Le travail et les professions",
    "title_en": "Work, Professions & Corporate Environment",
    "word_count": 45,
    "traps": [
        "NO article after ÊTRE when stating professions: 'Je suis ingénieur' (NOT 'Je suis un ingénieur'), 'Elle est avocate'.",
        "Preposition distinction: 'travailler DANS un bureau / une usine' (physical workplace) vs 'travailler CHEZ Renault / Google' (company brand / person).",
        "Suffix morphology: -er -> -ère (infirmier/infirmière), -ien -> -ienne (pharmacien/pharmacienne), -teur -> -trice (acteur/actrice), -eur -> -euse (serveur/serveuse)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE DÉCALAGE PHONÉTIQUE DES MÉTIERS EN -ER ET -IEN",
        "phonetic_tip_text": "Au masculin, les métiers en -er se terminent par le son [e] avec 'r' silencieux (boulanger, cuisinier, infirmier). Au féminin (-ère), l'accent grave ouvre le son [ɛʁ] et réveille le 'r' ! En -ien, la nasale [ɛ̃] devient une voyelle orale claire [ɛn] en -ienne.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Métiers [4 pts]",
        "ex1_headers": ["Profession", "Genre", "Consonne finale", "Son IPA A1", "Shift de son"],
        "ex1_rows": [
            ["1. un infirmier (m.)", "Masculin", "Consonne 'r' muette", "[ anh-feer-myay ]", "Son [e] pur sans 'r'"],
            ["2. une infirmière (f.)", "Féminin", "Consonne 'r' réveillée", "[ anh-feer-myair ]", "Son [ɛʁ] avec 'r' sonore"],
            ["3. un avocat (m.)", "Masculin", "Consonne 't' muette", "[ ah-voh-kah ]", "Son [a] sans 't'"],
            ["4. une avocate (f.)", "Féminin", "Consonne 't' prononcée", "[ ah-voh-kaht ]", "Consonne [t] articulée"],
            ["5. un pharmacien (m.)", "Masculin", "Voyelle nasale '-ien'", "[ fahr-mah-syanh ]", "Nasale [ɛ̃] pure"],
            ["6. une pharmacienne (f.)", "Féminin", "Suffixe '-ienne' dénasalisé", "[ fahr-mah-syen ]", "Orale [ɛn] claire"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Métiers [3 pts]",
        "ex2_items": [
            "a) un ingenieur -> ________________________",
            "b) un medecin -> ________________________",
            "c) une secretaire -> ________________________",
            "d) un chomeur -> ________________________",
            "e) une cuisiniere -> ________________________",
            "f) une boite (entreprise) -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Professions [3 pts]",
        "ex3_items": [
            "1. un avocat      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. un ingénieur   -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "3. un employé     -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. un pompier     -> [  ] Liaison                    [  ] Pas de liaison",
            "5. deux ouvriers  -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un architecte  -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "ENCODAGE MORPHOLOGIQUE DES SUFFIXES DE MÉTIERS",
        "gender_rule_text": "Règles de dérivation féminine : -er -> -ère (boulangère), -ien -> -ienne (informaticienne), -teur -> -trice (directrice), -eur -> -euse (serveuse). Épicènes invariables en -e : le/la dentiste, le/la journaliste, le/la comptable, le/la secrétaire.",
        "ex1_title": "Exercice 2.1 — Matrice de Transformation Morphologique [6 pts]",
        "ex1_headers": ["Masculin (Donné)", "Féminin correspondant", "Masculin (Donné)", "Féminin correspondant"],
        "ex1_rows": [
            ["1. Le boulanger", "-> ___________________", "7. Le traducteur", "-> ___________________"],
            ["2. Un informaticien", "-> ___________________", "8. Un chirurgien", "-> ___________________"],
            ["3. Le serveur", "-> ___________________", "9. Le dentiste", "-> ___________________"],
            ["4. Un acteur", "-> ___________________", "10. Un patron", "-> ___________________"],
            ["5. Le coiffeur", "-> ___________________", "11. L'agent immobilier", "-> ___________________"],
            ["6. Le comptable", "-> ___________________", "12. Un employé", "-> ___________________"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Marie est une actrice réputée dans un grande entreprise.\n   Correction : _____________________________________________________________________________",
            "2. Claire travaille comme un doctoresse dans un hôpital public.\n   Correction : _____________________________________________________________________________",
            "3. Sarah est un serveuse sympathique dans ce bistrot parisien.\n   Correction : _____________________________________________________________________________",
            "4. Thomas est une pharmacien très compétent et attentif.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DU MONDE DU TRAVAIL : DANS VS CHEZ",
        "colloc_tip_text": "On travaille DANS un bureau, DANS une usine, DANS un magasin (lieu physique). On travaille CHEZ Renault, CHEZ Google, CHEZ Total (nom d'entreprise commerciale). Expressions clés : chercher un emploi, faire un stage, toucher un salaire, être au chômage, prendre sa retraite.",
        "ex1_title": "Exercice 3.1 — Prépositions Professionnelles (DANS vs CHEZ vs AU) [5 pts]",
        "ex1_sentences": [
            "1. Sophie est comptable ; elle travaille _________ (dans un / chez) bureau moderne.",
            "2. Antoine est ingénieur aéronautique ; il travaille _________ (chez / dans) Airbus.",
            "3. La chirurgienne opère ses patients _________ (à l' / chez l') hôpital central.",
            "4. Depuis son licenciement, Marc est malheureusement _________ (au / en) chômage.",
            "5. Ma cousine est vendeuse ; elle travaille _________ (dans un / chez) grand magasin."
        ],
        "ex2_title": "Exercice 3.2 — Paires Verbe-Carrière Authentiques [5 pts]",
        "ex2_headers": ["Verbe d'action", "Complément de carrière", "Association"],
        "ex2_rows": [
            ["1. Chercher...", "A. des heures supplémentaires pour boucler le budget", "1 -> [    ]"],
            ["2. Faire...", "B. un salaire décent à la fin de chaque mois", "2 -> [    ]"],
            ["3. Toucher...", "C. sa retraite après quarante ans d'activité", "3 -> [    ]"],
            ["4. Prendre...", "D. un stage en entreprise pour valider son diplôme", "4 -> [    ]"],
            ["5. Poser...", "E. sa candidature pour une offre d'emploi", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE SITUATIONS PROFESSIONNELLES",
        "cloze_tip_text": "Complétez les dialogues professionnels avec les termes exacts du travail en respectant la règle d'omission de l'article après être.",
        "dialogues": [
            {
                "title": "Situation A — Rencontre lors d'une réception d'affaires",
                "points": "3 pts",
                "lines": [
                    "• Thomas : Bonjour Madame. Qu'est-ce que vous ___________________________ [do for a living] ?",
                    "• Élodie : Bonjour ! Je ___________________________ [am an architect - f. : no article !] chez Vinci.",
                    "• Thomas : C'est formidable ! Et vous travaillez ___________________________ [in an office] ou sur le terrain ?"
                ]
            },
            {
                "title": "Situation B — L'entretien d'embauche en entreprise",
                "points": "4 pts",
                "lines": [
                    "• Le recruteur : Bonjour Julien. Vous ___________________________ [are looking for a job] actuellement ?",
                    "• Julien : Oui, tout à fait. J'ai terminé un ___________________________ [internship] de six mois chez Total.",
                    "• Le recruteur : Notre ___________________________ [company / firm] recherche un bon ___________________________ [IT developer] pour un temps plein."
                ]
            },
            {
                "title": "Situation C — Discussions informelles à la pause-café",
                "points": "3 pts",
                "lines": [
                    "• Julie : Tu as parlé avec ___________________________ [the boss - m.] ce matin ?",
                    "• Marc : Oui, il a dit que nous devons faire des ___________________________ [overtime hours] ce vendredi.",
                    "• Julie : Encore ? Décidément, j'ai hâte de prendre ma ___________________________ [retirement] !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. What do you do for a living? (formal with 'vous')", "-> __________________________________________________________________________________"],
            ["2. I am a lawyer (f.) and I work in a company in Lyon.", "-> __________________________________________________________________________________"],
            ["3. Nicolas is looking for a job in a bakery.", "-> __________________________________________________________________________________"],
            ["4. My colleague (f.) works full-time; she is very competent.", "-> __________________________________________________________________________________"],
            ["5. Are you an engineer? (informal with 'tu')", "-> __________________________________________________________________________________"],
            ["6. She does not work anymore; she is retired.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Un médecin  •  Un avocat  •  Un bureau  •  Un professeur",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Une actrice  •  Une boulangère  •  Une serveuse  •  Un cuisinier",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Une usine  •  Une entreprise  •  Un salaire  •  Un hôpital",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Travailler dans  •  Faire un stage  •  Prendre le bus  •  Chercher un emploi",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. infirmier -> 'r' muet [anh-feer-myay] | 2. infirmière -> 'r' prononcé [anh-feer-myair] | 3. avocat -> 't' muet [ah-voh-kah] | 4. avocate -> 't' prononcé [ah-voh-kaht] | 5. pharmacien -> nasale [ɛ̃] | 6. pharmacienne -> dénasalisée orale [ɛn].\n\nExercice 1.2 — Orthographe [3 pts] :\na) un ingénieur | b) un médecin | c) une secrétaire | d) un chômeur | e) une cuisinière | f) une boîte.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un avocat -> Liaison en [n] obligatoire [œ̃.na.vɔ.ka] | 2. un ingénieur -> Liaison en [n] [œ̃.nɛ̃.ʒe.njœʁ] | 3. un employé -> Liaison en [n] [œ̃.nɑ̃.plwa.je] | 4. un pompier -> Pas de liaison | 5. deux ouvriers -> Liaison en [z] [dø.zu.vʁi.je] | 6. un architecte -> Liaison en [n] [œ̃.naʁ.ʃi.tɛkt].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. la boulangère | 2. une informaticienne | 3. la serveuse | 4. une actrice | 5. la coiffeuse | 6. la comptable | 7. la traductrice | 8. une chirurgienne | 9. la dentiste | 10. une patronne | 11. l'agente immobilière | 12. une employée.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'DANS UNE grande entreprise' (entreprise est féminin : une grande entreprise).\n2. 'comme médecin / femme médecin' (doctoresse est vieilli / péjoratif, on dit une femme médecin ou un médecin).\n3. 'Sarah est UNE serveuse' (serveuse est féminin : une serveuse).\n4. 'Thomas est UN pharmacien' (Thomas est masculin : un pharmacien).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. dans un bureau | 2. chez Airbus | 3. à l'hôpital | 4. au chômage | 5. dans un grand magasin.\n\nExercice 3.2 — Paires Carrière [5 pts] :\n1 -> E (Chercher sa candidature / une offre) | 2 -> A (Faire des heures supplémentaires) | 3 -> B (Toucher un salaire) | 4 -> C (Prendre sa retraite) | 5 -> E (Poser sa candidature).",
        "tier4_text": "Situation A (3 pts) : vous faites dans la vie | suis architecte (pas d'article !) | dans un bureau.\nSituation B (4 pts) : cherchez un emploi (ou un travail) | stage | entreprise (ou boîte) | informaticien (ou développeur).\nSituation C (3 pts) : le patron | heures supplémentaires | retraite.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Qu'est-ce que vous faites dans la vie ? (ou : Quelle est votre profession ?)\n2. Je suis avocate et je travaille dans une entreprise à Lyon.\n3. Nicolas cherche un travail dans une boulangerie.\n4. Ma collègue travaille à temps plein ; elle est très compétente.\n5. Tu es ingénieur ?\n6. Elle ne travaille plus ; elle est à la retraite (ou retraitée).\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Un bureau (lieu physique / meuble inanimé, les 3 autres sont des personnes exerçant une profession).\n2. Un cuisinier (profession masculine, les 3 autres sont au féminin : actrice, boulangère, serveuse).\n3. Un salaire (rémunération financière immatérielle, les 3 autres sont des édifices / lieux de travail physiques).\n4. Prendre le bus (transport urbain du quotidien, les 3 autres sont des collocations spécifiques au monde de l'emploi).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 14",
        "anchors_text": "1. Pas d'article après ÊTRE : Règle d'or absolue en FLE A1 : 'Je suis médecin', 'Elle est avocate'. L'article est proscrit sauf si un adjectif qualifie le nom ('C'est un excellent médecin').\\n2. Dans vs Chez : 'Dans' s'emploie pour le lieu matériel clos (dans un bureau, dans une usine). 'Chez' s'emploie obligatoirement pour la marque ou le nom d'entreprise (chez Google, chez Renault, chez Carrefour).\\n3. Le mot polysémique 'bureau' : En français, 'le bureau' désigne à la fois le meuble physique (desk) et la pièce ou le bâtiment de travail (office)."
    }
}

# CHAPTER 15
batch2["15"] = {
    "ch_num": 15,
    "title_fr": "La maison et l'appartement",
    "title_en": "Housing Types, Architecture & Rooms",
    "word_count": 42,
    "traps": [
        "Floor numbering in France: Ground floor is 'le rez-de-chaussée' (Floor 0)! First floor 'le premier étage' is ONE flight up (equivalent to US 2nd floor).",
        "Gender of rooms: LA cuisine, LA chambre, LA salle de bains ; LE salon, LE séjour, LE couloir, LE balcon, LE jardin, LE garage.",
        "Real estate terms: le loyer (monthly rent), louer (to rent), un studio (single-room flat), un immeuble (apartment building)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE PIÈGE DE 'REZ-DE-CHAUSSÉE' ET 'IMMEUBLE'",
        "phonetic_tip_text": "Dans le logement : 'rez-de-chaussée' se prononce [ray-duh-shoh-say] avec 'z' muet. 'L'immeuble' [lee-muhbl] a un 'e' initial prononcé [i]. 'Salon' [sah-lohn] a la nasale [ɔ̃]. 'Chambre' [shahmbr] a la nasale [ɑ̃].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Logement [4 pts]",
        "ex1_headers": ["Terme de logement", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le rez-de-chaussée", "Consonne 'z' finale", "[  ] Oui", "[  ] Oui", "[ ray-duh-shoh-say ]"],
            ["2. le salon (m.)", "Voyelle nasale 'on'", "[  ] Nasale [ɔ̃]", "[  ] Orale [on]", "[ sah-lohn ]"],
            ["3. la chambre (f.)", "Voyelle nasale 'am'", "[  ] Nasale [ɑ̃]", "[  ] Orale [am]", "[ shahmbr ]"],
            ["4. l'immeuble (m.)", "Voyelle initiale 'i'", "[  ] [lee-muhbl]", "[  ] [lay-muhbl]", "[ lee-muhbl ]"],
            ["5. le premier étage", "Consonne 'r' muette", "[  ] Oui", "[  ] Oui", "[ pruh-myay ay-tahzh ]"],
            ["6. la cuisine (f.)", "Digraphe 'ui'", "[  ] [kwee-zeen]", "[  ] [koy-zeen]", "[ kwee-zeen ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique du Logement [3 pts]",
        "ex2_items": [
            "a) le rez-de-chaussee -> ________________________",
            "b) une piece de la maison -> ________________________",
            "c) le premier etage -> ________________________",
            "d) un batiment -> ________________________",
            "e) une fenetre -> ________________________",
            "f) le jardin -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons dans l'Immeuble [3 pts]",
        "ex3_items": [
            "1. un appartement    -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. un étage          -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "3. premier étage     -> [  ] Liaison [ʁ] sonore         [  ] Pas de liaison",
            "4. dans un immeuble  -> [  ] Liaison [n] sonore         [  ] Pas de liaison",
            "5. deux chambres     -> [  ] Liaison                    [  ] Pas de liaison",
            "6. un ascenseur      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES PIÈCES ET STRUCTURES DU LOGEMENT",
        "gender_rule_text": "Les pièces : LA cuisine, LA chambre, LA salle de bains, LA terrasse ; LE salon, LE séjour, LE couloir, LE garage, LE grenier. Les types d'habitat : LA maison, LA villa ; L'appartement (m.), LE studio (m.), L'immeuble (m.).",
        "ex1_title": "Exercice 2.1 — Matrice des Pièces & Fonctions [6 pts]",
        "ex1_headers": ["Pièce (Genre)", "Article défini (le/la/l')", "Fonction domestique", "Sens anglais"],
        "ex1_rows": [
            ["1. Cuisine (f.)", "-> la cuisine", "préparer et cuisiner les repas", "Kitchen"],
            ["2. Salon (m.)", "-> le salon", "se détendre et recevoir les amis", "Living room"],
            ["3. Chambre (f.)", "-> la chambre", "dormir et se reposer dans un lit", "Bedroom"],
            ["4. Salle de bains (f.)", "-> la salle de bains", "se doucher et faire sa toilette", "Bathroom"],
            ["5. Balcon (m.)", "-> le balcon", "prendre l'air à l'extérieur", "Balcony"],
            ["6. Jardin (m.)", "-> le jardin", "cultiver des plantes et des fleurs", "Garden / Yard"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'habite dans un grand maison ancienne avec un petit jardin.\n   Correction : _____________________________________________________________________________",
            "2. Mon appartement est situé au troisième cuisine de l'immeuble.\n   Correction : _____________________________________________________________________________",
            "3. La salon de cette villa est très lumineux et spacieux.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons loué un joli chambre d'amis au premier étage.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS IMMOBILIÈRES ET LOCALISATION D'ÉTAGE",
        "colloc_tip_text": "Pour indiquer l'étage : AU rez-de-chaussée, AU premier étage, AU deuxième étage, AVEC ascenseur. Pour le contrat : payer le loyer, signer un bail, chercher une colocation.",
        "ex1_title": "Exercice 3.1 — Prépositions de Localisation dans l'Immeuble [5 pts]",
        "ex1_sentences": [
            "1. Mon appartement est situé _________ (au / dans le) deuxième étage avec balcon.",
            "2. Les personnes âgées préfèrent habiter _________ (au / en) rez-de-chaussée pour éviter les marches.",
            "3. L'immeuble est moderne et dispose _________ (d'un / avec) ascenseur rapide.",
            "4. En France, le locataire paie son loyer au propriétaire _________ (à la / chaque) fin du mois.",
            "5. Les enfants jouent dans _________ (le / au) jardin derrière la maison."
        ],
        "ex2_title": "Exercice 3.2 — Paires Types de Logements & Caractéristiques [5 pts]",
        "ex2_headers": ["Type de logement", "Description architecturale", "Association"],
        "ex2_rows": [
            ["1. Le studio...", "A. grand bâtiment comportant plusieurs étages et appartements", "1 -> [    ]"],
            ["2. L'immeuble...", "B. habitation individuelle avec terrain privé", "2 -> [    ]"],
            ["3. La maison...", "C. logement d'une seule pièce principale avec kitchenette", "3 -> [    ]"],
            ["4. La colocation...", "D. appartement partagé entre plusieurs locataires", "4 -> [    ]"],
            ["5. La villa...", "E. maison spacieuse et luxueuse souvent en bord de mer", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE RECHERCHE DE LOGEMENT (ANNONCE IMMOBILIÈRE)",
        "cloze_tip_text": "Complétez les dialogues de visite d'appartement en utilisant les termes architecturaux exacts.",
        "dialogues": [
            {
                "title": "Situation A — Visite d'un appartement avec l'agent immobilier",
                "points": "3 pts",
                "lines": [
                    "• L'agent : Voici l'immeuble. L'appartement se trouve au ___________________________ [first floor - 1 flight up].",
                    "• Le client : Il y a un ___________________________ [elevator / lift] dans l'immeuble ?",
                    "• L'agent : Oui, tout à fait. Entrons dans le ___________________________ [living room], il est très lumineux."
                ]
            },
            {
                "title": "Situation B — Description des pièces à un colocataire",
                "points": "4 pts",
                "lines": [
                    "• Julie : Il y a combien de ___________________________ [rooms / pièces] dans l'appartement ?",
                    "• Lucas : C'est un trois pièces : il y a deux ___________________________ [bedrooms], une grande ___________________________ [kitchen], et une ___________________________ [bathroom] avec baignoire.",
                    "• Julie : Super, c'est parfait pour nous deux !"
                ]
            },
            {
                "title": "Situation C — Discussion sur le montant du logement",
                "points": "3 pts",
                "lines": [
                    "• Antoine : Quel est le montant du ___________________________ [rent / loyer] par mois ?",
                    "• Sophie : C'est 750 euros, charges comprises. Et il y a un petit ___________________________ [balcony] donnant sur le parc."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. I live in an apartment on the third floor.", "-> __________________________________________________________________________________"],
            ["2. The kitchen is modern and the bathroom is spacious.", "-> __________________________________________________________________________________"],
            ["3. We have a house with a big garden in the countryside.", "-> __________________________________________________________________________________"],
            ["4. The building has an elevator and a parking lot.", "-> __________________________________________________________________________________"],
            ["5. How much is the monthly rent? (informal with 'c'est combien')", "-> __________________________________________________________________________________"],
            ["6. She lives on the ground floor.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. La cuisine  •  La chambre  •  Le salon  •  Le stylo",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Une maison  •  Un appartement  •  Un studio  •  Une raquette",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le rez-de-chaussée  •  Le premier étage  •  Le loyer  •  Le deuxième étage",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. L'ascenseur  •  L'escalier  •  Le couloir  •  Le dentifrice",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. rez-de-chaussée -> 'z' muet [ray-duh-shoh-say] | 2. salon -> nasale [ɔ̃] [sah-lohn] | 3. chambre -> nasale [ɑ̃] [shahmbr] | 4. immeuble -> [lee-muhbl] | 5. premier étage -> 'r' muet dans premier [pruh-myay ay-tahzh] | 6. cuisine -> [kwee-zeen].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le rez-de-chaussée (accents aigus) | b) une pièce (accent grave sur è) | c) le premier étage (accent aigu) | d) un bâtiment (circonflexe sur 'î') | e) une fenêtre (circonflexe sur 'ê') | f) le jardin.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un appartement -> Liaison en [n] obligatoire [œ̃.na.paʁ.tə.mɑ̃] | 2. un étage -> Liaison en [n] [œ̃.ne.taʒ] | 3. premier étage -> Liaison en [ʁ] [pʁə.mje.ʁe.taʒ] | 4. dans un immeuble -> Liaison en [n] [dɑ̃.zœ̃.ni.mœbl] | 5. deux chambres -> Pas de liaison devant consonne | 6. un ascenseur -> Liaison en [n] [œ̃.na.sɑ̃.sœʁ].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. la cuisine | 2. le salon | 3. la chambre | 4. la salle de bains | 5. le balcon | 6. le jardin.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'DANS UNE grande maison' (maison est féminin : une grande maison).\n2. 'au troisième ÉTAGE' (cuisine est une pièce, pas un niveau de bâtiment).\n3. 'LE salon' (salon est masculin : le salon).\n4. 'loué UNE jolie chambre' (chambre est féminin : une jolie chambre).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. au deuxième étage | 2. au rez-de-chaussée | 3. d'un ascenseur | 4. à la fin du mois | 5. le jardin.\n\nExercice 3.2 — Paires Logements [5 pts] :\n1 -> C (Studio -> pièce unique avec kitchenette) | 2 -> A (Immeuble -> bâtiment à étages avec appartements) | 3 -> B (Maison -> habitation individuelle avec terrain) | 4 -> D (Colocation -> logement partagé) | 5 -> E (Villa -> maison spacieuse et luxueuse).",
        "tier4_text": "Situation A (3 pts) : premier étage | ascenseur | salon.\nSituation B (4 pts) : pièces | chambres | cuisine | salle de bains.\nSituation C (3 pts) : loyer | balcon.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. J'habite dans un appartement au troisième étage.\n2. La cuisine est moderne et la salle de bains est spacieuse.\n3. Nous avons une maison avec un grand jardin à la campagne.\n4. L'immeuble a un ascenseur et un parking.\n5. C'est combien le loyer par mois ? (ou : Quel est le loyer mensuel ?)\n6. Elle habite au rez-de-chaussée.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. Le stylo (fourniture de bureau d'écriture, les 3 autres sont des pièces à vivre d'une habitation).\n2. Une raquette (équipement de sport de balle, les 3 autres sont des types architecturaux de logements).\n3. Le loyer (notion financière de paiement locatif, les 3 autres sont des niveaux / étages d'un bâtiment).\n4. Le dentifrice (produit d'hygiène corporelle pour les dents, les 3 autres sont des parties communes de circulation d'un immeuble).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 15",
        "anchors_text": "1. Le piège de la numérotation des étages : En France, le rez-de-chaussée correspond au niveau zéro. Le 'premier étage' correspond donc au deuxième niveau américain (one flight of stairs up) !\\n2. Le genre des pièces d'eau et de repos : 'La chambre', 'la cuisine', 'la salle de bains' sont féminines. Mais 'le salon', 'le séjour', 'le garage', 'le jardin' sont masculins.\\n3. Studio vs F1/T1 : Un studio comporte une pièce principale intégrant le coin cuisine, tandis qu'un deux-pièces (T2 / F2) sépare impérativement le salon de la chambre."
    }
}

# CHAPTER 16
batch2["16"] = {
    "ch_num": 16,
    "title_fr": "Le mobilier et l'équipement",
    "title_en": "Furniture, Lighting & Household Appliances",
    "word_count": 42,
    "traps": [
        "Appliances genders: LE réfrigérateur / le frigo, LE congélateur, LE lave-vaisselle, LE four, LE micro-ondes, LE lave-linge (washing machine).",
        "Furniture genders: LE canapé (couch), LE fauteuil (armchair), LE lit (bed), LE placard (cupboard) ; LA table, LA chaise (chair), L'armoire (f. - wardrobe), L'étagère (f. - shelf).",
        "Dual meaning: 'une glace' means ice cream OR a mirror; 'un bureau' means desk OR office."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "PRONONCIATION DES DIGRAPHES DU MOBILIER",
        "phonetic_tip_text": "Dans les meubles : 'fauteuil' [foh-tuy] a la diphtongue [œj]. 'Lit' [lee] a un 't' muet. 'Placard' [plah-kahr] a un 'd' muet. 'Lampe' [lahmp] a la voyelle nasale [ɑ̃].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Mobilier et Électroménager [4 pts]",
        "ex1_headers": ["Meuble / Appareil", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le lit (m.)", "Consonne 't' finale", "[  ] Oui", "[  ] Oui", "[ lee ]"],
            ["2. le placard (m.)", "Consonne 'd' finale", "[  ] Oui", "[  ] Oui", "[ plah-kahr ]"],
            ["3. le fauteuil (m.)", "Diphtongue '-euil'", "[  ] [foh-tuy]", "[  ] [foh-teel]", "[ foh-tuy ]"],
            ["4. le tapis (m.)", "Consonne 's' finale", "[  ] Oui", "[  ] Oui", "[ tah-pee ]"],
            ["5. la lampe (f.)", "Voyelle nasale 'am'", "[  ] Nasale [ɑ̃]", "[  ] Orale [am]", "[ lahmp ]"],
            ["6. le canapé (m.)", "Accent aigu 'é'", "[  ] [ay] fermé", "[  ] [eh] ouvert", "[ kah-nah-pay ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique de l'Équipement [3 pts]",
        "ex2_items": [
            "a) le canape -> ________________________",
            "b) une etagere -> ________________________",
            "c) un refrigerateur -> ________________________",
            "d) une armoire -> ________________________",
            "e) une cuisiniere -> ________________________",
            "f) le lave-linge -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons des Meubles [3 pts]",
        "ex3_items": [
            "1. une armoire       -> [  ] Liaison [n] sonore      [  ] Pas de liaison",
            "2. un étagère        -> [  ] Liaison [n] sonore      [  ] Pas de liaison",
            "3. deux chaises      -> [  ] Liaison                 [  ] Pas de liaison",
            "4. un aspirateur     -> [  ] Liaison [n] obligatoire [  ] Pas de liaison",
            "5. de grands placards -> [  ] Liaison [t] sonore     [  ] Pas de liaison",
            "6. un oreiller       -> [  ] Liaison [n] obligatoire [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES MEUBLES ET APPAREILS MÉNAGERS",
        "gender_rule_text": "La quasi-totalité des appareils électroménagers composés avec 'lave-' sont MASCULINS : le lave-vaisselle, le lave-linge, le réfrigérateur, le four, le micro-ondes, le grille-pain. Pour les meubles : LA table, LA chaise, L'armoire (f.), L'étagère (f.) ; LE lit, LE canapé, LE bureau, LE buffet.",
        "ex1_title": "Exercice 2.1 — Matrice Meubles, Électroménager et Pièces [6 pts]",
        "ex1_headers": ["Équipement (Genre)", "Article défini (le/la/l')", "Pièce d'installation", "Sens anglais"],
        "ex1_rows": [
            ["1. Lit (m.)", "-> le lit", "la chambre", "Bed / Bedroom"],
            ["2. Réfrigérateur (m.)", "-> le réfrigérateur", "la cuisine", "Fridge / Kitchen"],
            ["3. Canapé (m.)", "-> le canapé", "le salon", "Sofa / Living room"],
            ["4. Lave-linge (m.)", "-> le lave-linge", "la buanderie / salle de bains", "Washing machine"],
            ["5. Armoire (f.)", "-> l'armoire", "la chambre", "Wardrobe / Closet"],
            ["6. Table (f.)", "-> la table", "la salle à manger", "Table / Dining room"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai acheté une nouveau canapé en cuir marron pour le salon.\n   Correction : _____________________________________________________________________________",
            "2. Elle a rangé toutes ses robes dans un grande armoire blanche.\n   Correction : _____________________________________________________________________________",
            "3. Mon frère a installé la réfrigérateur à côté de l'évier.\n   Correction : _____________________________________________________________________________",
            "4. Cette chaise est très confortable et son table est en bois.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DOMESTIQUES : MEUBLES ET USAGES",
        "colloc_tip_text": "Verbes d'aménagement : meubler un appartement (to furnish), allumer la lampe (turn on light), mettre au frais dans le frigo, faire cuire au four, laver le linge sale dans la machine.",
        "ex1_title": "Exercice 3.1 — Prépositions et Fonctions des Équipements [5 pts]",
        "ex1_sentences": [
            "1. Mets la bouteille de lait _________ (dans le / au) réfrigérateur pour la garder fraîche.",
            "2. Le chat adore dormir confortablement _________ (sur le / dans) canapé du salon.",
            "3. Les assiettes sales doivent être lavées _________ (dans le / au) lave-vaisselle.",
            "4. Elle pose ses livres d'art _________ (sur / à) l'étagère de sa chambre.",
            "5. Allume la lampe de chevet _________ (à côté du / sur) lit pour lire ce soir."
        ],
        "ex2_title": "Exercice 3.2 — Paires Appareils Ménagers & Rôles [5 pts]",
        "ex2_headers": ["Appareil électroménager", "Tâche ménagère accomplie", "Association"],
        "ex2_rows": [
            ["1. Le lave-linge...", "A. conserver les aliments périssables au froid", "1 -> [    ]"],
            ["2. Le lave-vaisselle...", "B. nettoyer les assiettes, verres et couverts", "2 -> [    ]"],
            ["3. Le four...", "C. laver et essorer les vêtements sales", "3 -> [    ]"],
            ["4. Le réfrigérateur...", "D. réchauffer rapidement un plat cuisiné", "4 -> [    ]"],
            ["5. Le micro-ondes...", "E. cuire rôtis, gratins, tartes et gâteaux", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE D'AMÉNAGEMENT ET ACHAT DE MEUBLES",
        "cloze_tip_text": "Complétez les conversations sur l'aménagement d'intérieur avec les termes de mobilier exacts.",
        "dialogues": [
            {
                "title": "Situation A — Visite dans un magasin de meubles",
                "points": "3 pts",
                "lines": [
                    "• Le vendeur : Bonjour. Quel type de mobilier recherchez-vous ?",
                    "• Le client : Bonjour. Nous cherchons un grand ___________________________ [sofa / couch - m.] pour notre salon et deux ___________________________ [armchairs - fauteuils].",
                    "• Le vendeur : Venez voir nos modèles en tissu et en cuir."
                ]
            },
            {
                "title": "Situation B — Aménagement de la cuisine équipée",
                "points": "4 pts",
                "lines": [
                    "• Julie : La cuisine est-elle déjà équipée ?",
                    "• Le propriétaire : Oui, il y a un grand ___________________________ [refrigerator / fridge], un ___________________________ [oven] traditionnel, et un ___________________________ [dishwasher] moderne.",
                    "• Julie : Et pour laver les vêtements ?",
                    "• Le propriétaire : Il y a un ___________________________ [washing machine] dans la buanderie."
                ]
            },
            {
                "title": "Situation C — Rangement de la chambre à coucher",
                "points": "3 pts",
                "lines": [
                    "• Sophie : Où est-ce que je peux poser ma valise ?",
                    "• Marc : Pose-la près du ___________________________ [bed], et tu peux ranger tes vêtements dans l'___________________________ [wardrobe / closet]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. There is a table and four chairs in the dining room.", "-> __________________________________________________________________________________"],
            ["2. I put the fresh milk in the refrigerator.", "-> __________________________________________________________________________________"],
            ["3. We bought a comfortable sofa for the living room.", "-> __________________________________________________________________________________"],
            ["4. The washing machine is in the bathroom.", "-> __________________________________________________________________________________"],
            ["5. Turn on the lamp on the desk, please.", "-> __________________________________________________________________________________"],
            ["6. She put her books on the shelf.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. La table  •  La chaise  •  L'armoire  •  L'autobus",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le réfrigérateur  •  Le four  •  Le lave-linge  •  Le cousin",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le lit  •  L'oreiller  •  La couverture  •  Le ballon",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Le canapé  •  Le fauteuil  •  Le tabouret  •  La fourchette",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. lit -> 't' muet [lee] | 2. placard -> 'd' muet [plah-kahr] | 3. fauteuil -> diphtongue [œj] [foh-tuy] | 4. tapis -> 's' muet [tah-pee] | 5. lampe -> nasale [ɑ̃] [lahmp] | 6. canapé -> 'é' fermé [kah-nah-pay].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le canapé | b) une étagère (accents aigus et graves) | c) un réfrigérateur (accents aigus) | d) une armoire | e) une cuisinière | f) le lave-linge.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. une armoire -> Liaison en [n] sonore [y.naʁ.mwaʁ] | 2. une étagère -> Liaison en [n] [y.ne.ta.ʒɛʁ] | 3. deux chaises -> Pas de liaison | 4. un aspirateur -> Liaison en [n] [œ̃.na.spi.ʁa.tœʁ] | 5. de grands placards -> Liaison en [t] [də.gʁɑ̃.pla.kaʁ] | 6. un oreiller -> Liaison en [n] [œ̃.nɔ.ʁɛ.je].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. le lit | 2. le réfrigérateur | 3. le canapé | 4. le lave-linge | 5. l'armoire | 6. la table.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'UN NOUVEAU canapé' (canapé est masculin : un nouveau canapé).\n2. 'UNE GRANDE armoire' (armoire est féminin : une grande armoire).\n3. 'LE réfrigérateur' (réfrigérateur est masculin : le réfrigérateur).\n4. 'SA table' (table est féminin : sa table en bois).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. dans le réfrigérateur | 2. sur le canapé | 3. dans le lave-vaisselle | 4. sur l'étagère | 5. à côté du lit.",
        "tier3_text": "Exercice 3.2 — Paires Appareils [5 pts] :\n1 -> C (Lave-linge -> laver le linge sale) | 2 -> B (Lave-vaisselle -> laver assiettes et couverts) | 3 -> E (Four -> cuire rôtis et gâteaux) | 4 -> A (Réfrigérateur -> conserver au froid) | 5 -> D (Micro-ondes -> réchauffer rapidement).",
        "tier4_text": "Situation A (3 pts) : canapé | fauteuils.\nSituation B (4 pts) : réfrigérateur (ou frigo) | four | lave-vaisselle | lave-linge.\nSituation C (3 pts) : lit | armoire.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Il y a une table et quatre chaises dans la salle à manger.\n2. Je mets le lait frais dans le réfrigérateur (ou frigo).\n3. Nous avons acheté un canapé confortable pour le salon.\n4. Le lave-linge est dans la salle de bains.\n5. Allume la lampe sur le bureau, s'il te plaît.\n6. Elle a posé ses livres sur l'étagère.\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. L'autobus (véhicule de transport collectif routier, les 3 autres sont des pièces de mobilier d'intérieur).\n2. Le cousin (membre de la famille élargie, les 3 autres sont des appareils électroménagers domestiques).\n3. Le ballon (jouet sportif sphérique, les 3 autres sont des éléments de literie de la chambre à coucher).\n4. La fourchette (couvert de table pour piquer les aliments, les 3 autres sont des sièges pour s'asseoir).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 16",
        "anchors_text": "1. Le genre des composés en 'Lave-' : En français, tous les appareils électroménagers construits avec 'lave-' sont MASCULINS : LE lave-linge (washing machine), LE lave-vaisselle (dishwasher).\\n2. Frigo vs Réfrigérateur : 'Le frigo' est l'abréviation familière universelle de 'réfrigérateur'. Ne confondez pas avec 'le congélateur' (freezer, température négative à -18°C).\\n3. Armoire vs Placard : 'L'armoire' est généralement un meuble mobile en bois avec portes battantes. 'Le placard' est souvent intégré directement dans le mur de la pièce."
    }
}

# CHAPTER 17
batch2["17"] = {
    "ch_num": 17,
    "title_fr": "Les transports publics",
    "title_en": "Public Transit Networks, Trains & Metro",
    "word_count": 40,
    "traps": [
        "Preposition rule: 'EN' for enclosed transport (en métro, en bus, en train, en avion) vs 'À' for open astride transport (à vélo, à pied, à moto).",
        "French transit rule: COMPOSTER SON BILLET ! You must punch/validate paper tickets in yellow stamping machines on platforms before boarding trains or face immediate fines.",
        "Stations & Stops: UNE STATION de métro / de tramway ; UN ARRÊT de bus ; LA GARE SNCF (trains) ; L'AÉROPORT (airplanes)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'T' FINAL SILENCIEUX DE TICKET ET BILLET",
        "phonetic_tip_text": "Dans les transports : 'un ticket' [tee-kay] et 'un billet' [bee-yay] ont tous deux un 't' muet silencieux. 'Quai' se prononce [kay] (rime avec café). 'Composter' [kohn-pohs-tay] a la nasale [ɔ̃].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Transports Publics [4 pts]",
        "ex1_headers": ["Terme de transport", "Piège phonétique", "Prononcée ?", "Muette ?", "Transcription A1"],
        "ex1_rows": [
            ["1. le quai (de gare)", "Diphtongue 'ai'", "[  ] [kay]", "[  ] [kwee]", "[ kay ]"],
            ["2. un ticket (m.)", "Consonne 't' finale", "[  ] Oui", "[  ] Oui", "[ tee-kay ]"],
            ["3. un billet (m.)", "Consonne 't' finale", "[  ] Oui", "[  ] Oui", "[ bee-yay ]"],
            ["4. le métro (m.)", "Voyelle finale 'o'", "[  ] [may-troh]", "[  ] [mee-troh]", "[ may-troh ]"],
            ["5. l'avion (m.)", "Voyelle nasale 'on'", "[  ] Nasale [ɔ̃]", "[  ] Orale [on]", "[ lah-vyohn ]"],
            ["6. le train (m.)", "Voyelle nasale 'ain'", "[  ] Nasale [ɛ̃]", "[  ] Orale [en]", "[ tranh ]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique des Transports [3 pts]",
        "ex2_items": [
            "a) le metro -> ________________________",
            "b) un arret de bus -> ________________________",
            "c) l'aeroport -> ________________________",
            "d) composter un billet -> ________________________",
            "e) la fermeture des portes -> ________________________",
            "f) une correspondance -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons du Réseau Transit [3 pts]",
        "ex3_items": [
            "1. un arrêt de bus   -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. en avion          -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "3. aux guichets      -> [  ] Liaison                    [  ] Pas de liaison",
            "4. les aéroports     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "5. deux tickets      -> [  ] Liaison                    [  ] Pas de liaison",
            "6. un aller-retour   -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES VÉHICULES ET TITRES DE TRANSPORT",
        "gender_rule_text": "Tous les moyens de transport urbain sont MASCULINS : LE métro, LE bus, LE tramway, LE train, LE TGV, L'avion (m.), LE taxi. Les titres de transport : LE ticket (métro/bus), LE billet (train/avion), LE passe Navigo ; LA carte d'embarquement.",
        "ex1_title": "Exercice 2.1 — Matrice Transports, Lieux d'Embarquement & Titres [6 pts]",
        "ex1_headers": ["Moyen de transport", "Préposition", "Lieu d'embarquement", "Titre requis"],
        "ex1_rows": [
            ["1. Le métro (m.)", "-> en métro", "une station de métro", "un ticket / passe Navigo"],
            ["2. Le bus (m.)", "-> en bus", "un arrêt de bus", "un ticket de bus validé"],
            ["3. Le tramway (m.)", "-> en tram", "une station de tram", "un ticket de tram"],
            ["4. Le train TGV (m.)", "-> en train", "la gare SNCF (sur le quai)", "un billet de train composté"],
            ["5. L'avion (m.)", "-> en avion", "l'aéroport (porte d'embarquement)", "une carte d'embarquement"],
            ["6. Le taxi (m.)", "-> en taxi", "une station de taxi", "une course payée"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Je vais à Lyon à train parce que c'est plus rapide.\n   Correction : _____________________________________________________________________________",
            "2. Nous attendons le train sur la quai numéro 4.\n   Correction : _____________________________________________________________________________",
            "3. Elle a oublié de valider sa ticket dans le bus.\n   Correction : _____________________________________________________________________________",
            "4. Mon père achète une carnet de dix tickets de métro.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE TRANSIT : COMPOSTER, MONTER & DESCENDRE",
        "colloc_tip_text": "Verbes de déplacement : MONTER dans le bus/train (get on), DESCENDRE du bus/train (get off), CHANGER de ligne (transfer/change), COMPOSTER son billet (stamp ticket), PRENDRE les transports en commun.",
        "ex1_title": "Exercice 3.1 — Prépositions de Moyens de Transport (EN vs À) [5 pts]",
        "ex1_sentences": [
            "1. Pour aller au travail au centre de Paris, je voyage _________ (en / à) métro.",
            "2. Quand il fait beau au printemps, mon fils préfère aller au collège _________ (en / à) vélo.",
            "3. Les touristes voyagent de Paris à Marseille _________ (en / à) TGV en trois heures.",
            "4. Nous rentrons chez nous le soir tranquillement _________ (en / à) pied.",
            "5. Pour partir en vacances au Japon, il faut voyager _________ (en / à) avion."
        ],
        "ex2_title": "Exercice 3.2 — Paires Actions de Transport & Conséquences [5 pts]",
        "ex2_headers": ["Action de transit", "Procédure obligatoire", "Association"],
        "ex2_rows": [
            ["1. Prendre le train...", "A. valider son titre devant la borne électronique", "1 -> [    ]"],
            ["2. Entrer dans le métro...", "B. composter obligatoirement son billet jaune sur le quai", "2 -> [    ]"],
            ["3. Arriver à destination...", "C. descendre du wagon à la prochaine station", "3 -> [    ]"],
            ["4. Monter dans le bus...", "D. acheter un billet à la borne ou au guichet", "4 -> [    ]"],
            ["5. Voyager sans titre...", "E. risquer une amende forfaitaire immédiate", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "CLOZE DE DÉPLACEMENT EN TRANSPORT EN COMMUN",
        "cloze_tip_text": "Complétez les dialogues d'achat de billets et de voyage en train avec les expressions authentiques.",
        "dialogues": [
            {
                "title": "Situation A — Au guichet de la gare SNCF",
                "points": "3 pts",
                "lines": [
                    "• Le voyageur : Bonjour. Je voudrais un ___________________________ [round-trip ticket : aller-retour] pour Lyon, s'il vous plaît.",
                    "• L'agent : En première ou en seconde classe ?",
                    "• Le voyageur : En seconde. Le train part de quel ___________________________ [platform - m.] ?",
                    "• L'agent : Du quai numéro 2. N'oubliez pas de ___________________________ [stamp / punch - composter] votre billet !"
                ]
            },
            {
                "title": "Situation B — Dans le métro parisien",
                "points": "4 pts",
                "lines": [
                    "• Un touriste : Pardon Madame, quelle est la ___________________________ [line / ligne] pour aller à la Tour Eiffel ?",
                    "• Une Parisienne : Prenez la ligne 6 direction Charles de Gaulle - Étoile, et descendez à la ___________________________ [station] Bir-Hakeim.",
                    "• Le touriste : Je dois changer de train ?",
                    "• La Parisienne : Non, c'est direct, il n'y a pas de ___________________________ [transfer / correspondance]."
                ]
            },
            {
                "title": "Situation C — À l'arrêt de bus urbain",
                "points": "3 pts",
                "lines": [
                    "• Marc : Le bus arrive dans combien de temps ?",
                    "• Sophie : Dans cinq minutes. Prépare ton ___________________________ [ticket] ou ton passe Navigo pour le ___________________________ [validate] à bord."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée [6 pts]",
        "ex1_prompts": [
            ["1. Which platform does the train leave from?", "-> __________________________________________________________________________________"],
            ["2. I take the subway every day to go to work.", "-> __________________________________________________________________________________"],
            ["3. Don't forget to stamp your ticket before boarding.", "-> __________________________________________________________________________________"],
            ["4. I would like a booklet of ten subway tickets, please.", "-> __________________________________________________________________________________"],
            ["5. We travel to Nice by train (TGV).", "-> __________________________________________________________________________________"],
            ["6. Watch out for the closing doors! (Métro announcement)", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification [4 pts]",
        "ex2_intrus": [
            ["1. Le métro  •  Le bus  •  Le tramway  •  La table",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. En train  •  En avion  •  En bus  •  À vélo",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le quai  •  La gare  •  L'arrêt de bus  •  La chambre",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Un billet  •  Un ticket  •  Le passe Navigo  •  Un sandwich",
             "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. quai -> [kay] | 2. ticket -> 't' muet [tee-kay] | 3. billet -> 't' muet [bee-yay] | 4. métro -> [may-troh] | 5. avion -> nasale [ɔ̃] [lah-vyohn] | 6. train -> nasale [ɛ̃] [tranh].\n\nExercice 1.2 — Orthographe [3 pts] :\na) le métro | b) un arrêt de bus (accent circonflexe sur 'ê') | c) l'aéroport (accent aigu sur é) | d) composter un billet | e) la fermeture des portes | f) une correspondance.\n\nExercice 1.3 — Liaisons [3 pts] :\n1. un arrêt de bus -> Liaison en [n] obligatoire [œ̃.na.ʁɛ.də.bys] | 2. en avion -> Liaison en [n] [ɑ̃.na.vjɔ̃] | 3. aux guichets -> Pas de liaison devant consonne | 4. les aéroports -> Liaison en [z] [le.za.e.ʁɔ.pɔʁ] | 5. deux tickets -> Pas de liaison | 6. un aller-retour -> Liaison en [n] [œ̃.na.le.ʁə.tuʁ].",
        "tier2_text": "Exercice 2.1 — Matrice [6 pts] :\n1. en métro / un ticket / station | 2. en bus / un ticket / arrêt | 3. en tram / un ticket / station | 4. en train / un billet / gare (quai) | 5. en avion / carte d'embarquement / aéroport | 6. en taxi / course payée / station de taxi.\n\nExercice 2.2 — Détective [4 pts] :\n1. 'EN train' (moyen de transport fermé avec en, pas à).\n2. 'LE quai numéro 4' (quai est masculin : sur le quai).\n3. 'SON ticket' (ticket est masculin : son ticket).\n4. 'UN carnet de dix tickets' (carnet est masculin : un carnet).",
        "tier3_text": "Exercice 3.1 — Prépositions [5 pts] :\n1. en métro | 2. à vélo (ouvre/à cheval sur l'engin) | 3. en TGV | 4. à pied | 5. en avion.",
        "tier3_text": "Exercice 3.2 — Paires Transit [5 pts] :\n1 -> B (Prendre le train -> composter son billet sur le quai) | 2 -> A (Entrer dans le métro -> valider devant la borne) | 3 -> C (Arriver à destination -> descendre à la station) | 4 -> D (Monter dans le bus -> acheter un billet) | 5 -> E (Voyager sans titre -> risquer une amende).",
        "tier4_text": "Situation A (3 pts) : aller-retour | quai | composter.\nSituation B (4 pts) : ligne | station | correspondance.\nSituation C (3 pts) : ticket | valider.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Le train part de quel quai ? (ou : De quel quai part le train ?)\n2. Je prends le métro tous les jours pour aller au travail.\n3. N'oubliez pas de composter votre billet avant de monter.\n4. Je voudrais un carnet de dix tickets de métro, s'il vous plaît.\n5. Nous voyageons à Nice en train (en TGV).\n6. Attention à la fermeture des portes !\n\nExercice 5.2 — L'Intrus [4 pts] :\n1. La table (meuble de repas, les 3 autres sont des véhicules de réseau de transport urbain).\n2. À vélo (utilise la préposition 'à' pour un transport non clos, les 3 autres utilisent 'en').\n3. La chambre (pièce domestique privée pour dormir, les 3 autres sont des infrastructures d'attente de transport public).\n4. Un sandwich (aliment de restauration rapide, les 3 autres sont des titres / titres de transport valides).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 17",
        "anchors_text": "1. La règle EN vs À dans les transports : Utilisez 'EN' dès que l'on pénètre À L'INTÉRIEUR d'un habitacle fermé (en voiture, en train, en bus, en avion, en métro). Utilisez 'À' quand on monte SUR un engin ouvert ou qu'on marche (à pied, à vélo, à moto, à cheval).\\n2. Le compostage des billets de train : En France, un billet papier de train non composté dans la borne jaune avant l'accès au quai est considéré comme invalide par les contrôleurs, entraînant une amende immédiate !\\n3. Le Passe Navigo : Titre de transport électronique sans contact emblématique de la région Île-de-France (Paris et banlieue)."
    }
}

with open("chapters_batch_2.json", "w", encoding="utf-8") as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

print("Batch 2 updated through Chapter 17.")
