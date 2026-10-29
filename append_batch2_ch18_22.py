import json

with open("chapters_batch_2.json", "r", encoding="utf-8") as f:
    batch2 = json.load(f)

# CHAPTER 18: Les transports privés et la circulation
batch2["18"] = {
    "ch_num": 18,
    "title_fr": "Les transports privés et la circulation",
    "title_en": "Private Vehicles, Road Rules & Driving",
    "word_count": 42,
    "traps": [
        "Preposition rule EN vs À: 'en voiture / en moto / en taxi' (interior/enclosed) vs 'à vélo / à moto / à pied' (on top/open air). Note: both 'en moto' and 'à moto' are used in France, but 'à vélo' and 'à pied' strictly require 'à'.",
        "Gender traps: 'la voiture' (f.), 'la bicyclette' (f.), but 'le vélo' (m.), 'le volant' (m.), 'le feu' (m.), 'le permis' (m.).",
        "False friend / liaison: 'un embouteillage' / 'un bouchon' (traffic jam); silent letters in 'le permis' (silent -s), 'le feu' (silent -x in pl. feux)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "CONSONNES FINALES SILENCIEUSES & VOYELLES COMPOSÉES",
        "phonetic_tip_text": "Attention aux terminaisons : 'le permis' (le 's' final ne se prononce jamais [pair-mee]), 'le feu' ([fuh] avec le son [ø], pluriel feux sans 'x' sonore), et 'le frein' (nasale [ɛ̃] dans [franh]).",
        "ex1_title": "Exercice 1.1 — Audit Phonétique & Lettres Muettes [4 pts]",
        "ex1_headers": ["Terme routier", "Genre", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le permis (m.)", "Masculin", "Consonne 's' muette", "[ pair-mee ]", "'s' final muet absolu"],
            ["2. le frein (m.)", "Masculin", "Graphème '-ein' nasal", "[ franh ]", "Voyelle nasale [ɛ̃] pure"],
            ["3. le feu rouge (m.)", "Masculin", "Graphème 'eu' fermé", "[ fuh roozh ]", "Son [ø] sans consonne"],
            ["4. le rond-point (m.)", "Masculin", "Consonne 't' muette", "[ rohn-pwanh ]", "Double nasale [ɔ̃] et [wɛ̃]"],
            ["5. un arrêt (m.)", "Masculin", "Consonne 't' muette", "[ ah-reh ]", "Accent circonflexe [ɛ]"],
            ["6. le pneu (m.)", "Masculin", "Consonne 'u' finale", "[ pnuh ]", "Son [ø], 'pn-' sonore"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un velo -> ________________________",
            "b) une ceinture de securite -> ________________________",
            "c) un arret de bus -> ________________________",
            "d) un accelerateur -> ________________________",
            "e) un garagiste -> ________________________",
            "f) un peage d'autoroute -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Élidations [3 pts]",
        "ex3_items": [
            "1. un embouteillage   -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. les autoroutes     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un accident        -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. en voiture         -> [  ] Liaison                    [  ] Enchaînement simple",
            "5. deux amendes       -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un agent de police -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES VÉHICULES ET PIÈCES MÉCANIQUES",
        "gender_rule_text": "La majorité des véhicules motorisés sont masculins (le camion, le scooter, le taxi, le van), sauf la voiture/l'auto et la moto (abréviation de motocyclette). Les pièces du véhicule : le moteur, le volant, le coffre, mais la roue, la portière, la ceinture.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Véhicules & Équipements [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ voiture (f.)", "[   ] M   [   ] F", "7. _______ casque (m.)", "[   ] M   [   ] F"],
            ["2. _______ volant (m.)", "[   ] M   [   ] F", "8. _______ ceinture (f.)", "[   ] M   [   ] F"],
            ["3. _______ vélo (m.)", "[   ] M   [   ] F", "9. _______ frein (m.)", "[   ] M   [   ] F"],
            ["4. _______ route (f.)", "[   ] M   [   ] F", "10. _______ autoroute (f.)", "[   ] M   [   ] F"],
            ["5. _______ station-service (f.)", "[   ] M   [   ] F", "11. _______ essence (f.)", "[   ] M   [   ] F"],
            ["6. _______ parking (m.)", "[   ] M   [   ] F", "12. _______ feu rouge (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. J'ai garé le voiture rouge dans le premier parking du centre.\n   Correction : _____________________________________________________________________________",
            "2. Il faut attacher un ceinture de sécurité avant de démarrer le moteur.\n   Correction : _____________________________________________________________________________",
            "3. Le moto roule très vite sur la grand autoroute du Sud.\n   Correction : _____________________________________________________________________________",
            "4. Tournez à droite au première feu tricolore après le pont.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE CONDUITE : EN VS À & VERBES D'ACTION",
        "colloc_tip_text": "On dit : 'monter en voiture', 'mettre sa ceinture', 'passer les vitesses', 'tourner à droite/gauche', 'être coincé dans un bouchon', 'faire le plein d'essence'.",
        "ex1_title": "Exercice 3.1 — Prépositions Modales & Verbes Routiers [5 pts]",
        "ex1_sentences": [
            "1. Pour aller au travail sans polluer, Julien se déplace toujours _________ (à/en) vélo.",
            "2. Nous partons en vacances en Bretagne _________ (à/en) voiture avec toute la famille.",
            "3. Avant de prendre la route le matin, mon père fait _________ (le plein / la clé) d'essence.",
            "4. À l'approche du carrefour, le conducteur ralentit et s'arrête _________ (au / dans le) feu rouge.",
            "5. Les piétons doivent obligatoirement traverser la chaussée sur le passage _________ (piéton / trottoir)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Verbe-Action Routière [5 pts]",
        "ex2_headers": ["Verbe d'action", "Complément d'objet", "Code association"],
        "ex2_rows": [
            ["1. Attacher...", "A. son permis de conduire et sa carte grise", "1 -> [    ]"],
            ["2. Présenter...", "B. sa ceinture de sécurité", "2 -> [    ]"],
            ["3. Respecter...", "C. sa voiture sur une place autorisée", "3 -> [    ]"],
            ["4. Garer...", "D. la limitation de vitesse sur l'autoroute", "4 -> [    ]"],
            ["5. Klaxonner...", "E. uniquement en cas de danger immédiat", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : CONDUITE & CONTRÔLE ROUTIER",
        "cloze_tip_text": "Complétez les dialogues sans regarder de lexique, en mobilisant les collocations réelles du code de la route.",
        "dialogues": [
            {
                "title": "Situation A — À la station-service d'autoroute (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le conducteur : Bonjour, je voudrais faire ___________________________ [the full tank] de sans-plomb 95, s'il vous plaît.",
                    "• L'employé : Bien sûr, la pompe numéro 4 est libre. Vous voulez vérifier la pression des ___________________________ [tires] ?",
                    "• Le conducteur : Oui merci, et je vais aussi nettoyer mon ___________________________ [windshield / glass]."
                ]
            },
            {
                "title": "Situation B — Contrôle de police sur la route (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le policier : Bonjour Madame. Vos papiers s'il vous plaît : votre ___________________________ [driver's license] et les papiers du véhicule.",
                    "• La conductrice : Voilà Monsieur l'agent. Est-ce que j'ai commis une ___________________________ [traffic violation / infraction] ?",
                    "• Le policier : Vous rouliez à 70 km/h au lieu de 50. Vous n'avez pas vu le ___________________________ [speed limit sign] ?",
                    "• La conductrice : Excusez-moi, j'étais distraite par le GPS. Voici mon attestation d'___________________________ [insurance]."
                ]
            },
            {
                "title": "Situation C — Louer une bicyclette en ville (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le touriste : Bonjour, je voudrais louer un ___________________________ [bicycle] pour la journée.",
                    "• Le loueur : Très bien. Préférez-vous un vélo classique ou un vélo à assistance ___________________________ [electric] ?",
                    "• Le touriste : Électrique, s'il vous plaît ! Est-ce que le ___________________________ [helmet] est fourni ?"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. Fasten your seatbelt before starting the car.", "-> __________________________________________________________________________________"],
            ["2. I go to work by bicycle every morning.", "-> __________________________________________________________________________________"],
            ["3. We are stuck in a huge traffic jam on the highway.", "-> __________________________________________________________________________________"],
            ["4. You must stop at the red light.", "-> __________________________________________________________________________________"],
            ["5. Where can I park my car for free?", "-> __________________________________________________________________________________"],
            ["6. He forgot his driver's license at home.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le volant  •  Le frein  •  La roue  •  Le billet de train", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La voiture  •  Le camion  •  Le vélo  •  L'autocar", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. L'essence  •  Le gazole  •  L'électricité  •  L'amende", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. À vélo  •  À pied  •  À cheval  •  En avion", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le permis -> 's' muet [pair-mee] | 2. le frein -> voyelle nasale [franh] | 3. le feu -> son [ø] fermé | 4. le rond-point -> double nasale [rohn-pwanh] | 5. un arrêt -> 't' muet [ah-reh] | 6. le pneu -> son [ø] avec pn- articulé.\nExercice 1.2 — Orthographe [3 pts] :\na) un vélo | b) une ceinture de sécurité | c) un arrêt de bus | d) un accélérateur | e) un garagiste | f) un péage.\nExercice 1.3 — Liaisons [3 pts] :\n1. un embouteillage [n] | 2. les autoroutes [z] | 3. un accident [n] | 4. en voiture (enchaînement) | 5. deux amendes [z] | 6. un agent [n].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la voiture (F) | 2. le volant (M) | 3. le vélo (M) | 4. la route (F) | 5. la station-service (F) | 6. le parking (M) | 7. le casque (M) | 8. la ceinture (F) | 9. le frein (M) | 10. l'autoroute (F) | 11. l'essence (F) | 12. le feu rouge (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. LA voiture (voiture est féminin) | 2. UNE ceinture (ceinture est féminin) | 3. LA moto (moto est féminin) | 4. AU PREMIER feu (feu est masculin singulier).",
        "tier3_text": "Exercice 3.1 — Prépositions & Verbes [5 pts] :\n1. à vélo | 2. en voiture | 3. le plein | 4. au feu rouge | 5. piéton.\nExercice 3.2 — Paires Verbe-Action [5 pts] :\n1 -> B (Attacher sa ceinture) | 2 -> A (Présenter son permis) | 3 -> D (Respecter la limitation) | 4 -> C (Garer sa voiture) | 5 -> E (Klaxonner en cas de danger).",
        "tier4_text": "Situation A (3 pts) : le plein | pneus | pare-brise.\nSituation B (4 pts) : permis de conduire | infraction (ou excès de vitesse) | panneau (de limitation de vitesse) | assurance.\nSituation C (3 pts) : vélo | électrique | casque.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Attachez votre ceinture avant de démarrer la voiture. | 2. Je vais au travail à vélo tous les matins. | 3. Nous sommes coincés dans un énorme embouteillage (ou bouchon) sur l'autoroute. | 4. Vous devez vous arrêter au feu rouge. (ou : Tu dois t'arrêter...) | 5. Où puis-je garer ma voiture gratuitement ? | 6. Il a oublié son permis de conduire à la maison.\nExercice 5.2 — Intrus [4 pts] :\n1. Le billet de train (transport ferroviaire/public, les autres sont des pièces de voiture) | 2. Le vélo (véhicule sans moteur / deux-roues non motorisé) | 3. L'amende (sanction financière, les autres sont des carburants/énergies) | 4. En avion (utilise la préposition 'en' et véhicule fermé dans les airs, les autres utilisent 'à').",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 18",
        "anchors_text": "1. Règle d'or des prépositions de transport : On utilise EN pour les véhicules fermés où l'on entre à l'intérieur (en voiture, en train, en bus, en taxi, en avion). On utilise À pour les moyens ou véhicules sur lesquels on monte ou à l'air libre (à pied, à vélo, à cheval, à moto).\n2. Attention au genre de moto : 'Une moto' est féminin car c'est le diminutif d'une motocyclette. De même, 'une auto' est féminin (abréviation d'automobile).\n3. Vocabulaire routier familier : 'Un bouchon' est le terme quotidien le plus fréquent pour désigner un embouteillage."
    }
}

# CHAPTER 19: Le tourisme et la météo
batch2["19"] = {
    "ch_num": 19,
    "title_fr": "Le tourisme et la météo",
    "title_en": "Tourism, Sightseeing, Weather & Climate",
    "word_count": 44,
    "traps": [
        "The formula 'IL FAIT + adjectif' for weather: 'Il fait beau / chaud / froid / mauvais' vs 'IL Y A + article partitif/indéfini': 'Il y a du soleil / du vent / du brouillard / de la pluie / des nuages'.",
        "Verbs of precipitation: 'Il pleut' (pleuvoir) and 'Il neige' (neiger) are strictly impersonal; never say 'le ciel pleut'.",
        "Gender traps: 'le musée' (m. despite ending in -ée!), 'le monument' (m.), 'le château' (m.), 'la valise' (f.), 'la météo' (f.), 'le soleil' (m.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "DIPHTONGUES FRANÇAISES & GRAPHÈMES MÉTÉO (-EAU, -EUX)",
        "phonetic_tip_text": "'Château' et 'beau' se terminent par '-eau' qui donne le son [o] pur fermé. 'Nuageux' et 'pluvieux' se terminent par '-eux' avec le son [ø] et un 'x' final muet !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique & Décryptage Météo [4 pts]",
        "ex1_headers": ["Terme touristique", "Genre", "Graphème clé", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le château (m.)", "Masculin", "Graphème '-eau'", "[ shah-toh ]", "Son [o] sans diphtongue"],
            ["2. le musée (m.)", "Masculin", "Suffixe '-ée' masculin", "[ myoo-zay ]", "Masculin en '-ée' !"],
            ["3. nuageux (adj.)", "Adjectif", "Terminaison '-eux'", "[ nyoo-ah-zhuh ]", "'x' final muet"],
            ["4. le soleil (m.)", "Masculin", "Graphème '-eil'", "[ soh-lay ]", "Son [ɛj] liquide"],
            ["5. la pluie (f.)", "Féminin", "Voyelle 'ui'", "[ plyoo-ee ]", "Semi-consonne [ɥi]"],
            ["6. le brouillard (m.)", "Masculin", "Graphème '-illard'", "[ broo-yahr ]", "'d' final muet, [j] liquide"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) la meteo -> ________________________",
            "b) un musee -> ________________________",
            "c) un chateau -> ________________________",
            "d) la temperature -> ________________________",
            "e) un appareil photo -> ________________________",
            "f) une station balneaire -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Touristiques [3 pts]",
        "ex3_items": [
            "1. un office de tourisme -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des anciens châteaux  -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. il y a du soleil      -> [  ] Enchaînement vocalique    [  ] Pas d'élision",
            "4. un orage violent      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "5. les îles bretonnes    -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand hôtel        -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES SITES TOURISTIQUES ET PHÉNOMÈNES MÉTÉO",
        "gender_rule_text": "'Le musée' est un piège majeur : c'est un masculin qui finit en -ée ! Les éléments naturels : le soleil, le vent, le ciel, l'orage (m.), le brouillard (m.), mais la pluie (f.), la neige (f.), la tempête (f.). Lieux : le monument, le palais, mais la plage, la montagne, la cathédrale.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Tourisme & Nature [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ musée (m.)", "[   ] M   [   ] F", "7. _______ plage (f.)", "[   ] M   [   ] F"],
            ["2. _______ château (m.)", "[   ] M   [   ] F", "8. _______ montagne (f.)", "[   ] M   [   ] F"],
            ["3. _______ pluie (f.)", "[   ] M   [   ] F", "9. _______ orage (m.)", "[   ] M   [   ] F"],
            ["4. _______ soleil (m.)", "[   ] M   [   ] F", "10. _______ valise (f.)", "[   ] M   [   ] F"],
            ["5. _______ vent (m.)", "[   ] M   [   ] F", "11. _______ guide (m.)", "[   ] M   [   ] F"],
            ["6. _______ neige (f.)", "[   ] M   [   ] F", "12. _______ carte postale (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Nous avons visité une magnifique musée d'art moderne au cœur de Paris.\n   Correction : _____________________________________________________________________________",
            "2. Le pluie tombe sans arrêt depuis ce matin sur toute la côte normande.\n   Correction : _____________________________________________________________________________",
            "3. Mon frère a acheté un grande valise noire pour son voyage en Italie.\n   Correction : _____________________________________________________________________________",
            "4. Demain, une violent orage d'été va éclater au-dessus des Alpes.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS MÉTÉOROLOGIQUES & D'ACTIVITÉS TOURISTIQUES",
        "colloc_tip_text": "Distinction cruciale : 'Il fait chaud/froid/beau' vs 'Il y a du vent/du soleil'. Pour les vacances : 'faire sa valise' (to pack), 'prendre des photos', 'visiter un monument', 'faire une randonnée', 'se baigner'.",
        "ex1_title": "Exercice 3.1 — Formules Météorologiques & Vacances [5 pts]",
        "ex1_sentences": [
            "1. En été dans le sud de la France, il _________ (fait / a) très chaud et le soleil brille.",
            "2. Regarde par la fenêtre : il y a _________ (du / le) vent violent et beaucoup de nuages gris.",
            "3. Prends ton parapluie car aujourd'hui il _________ (pleut / neige) sur toute la région parisienne.",
            "4. La veille du départ en vacances, nous faisons toujours nos _________ (valises / chambres).",
            "5. Les touristes aiment visiter les monuments et _________ (prendre / faire) de jolies photos."
        ],
        "ex2_title": "Exercice 3.2 — Paires Verbe-Activité Touristique [5 pts]",
        "ex2_headers": ["Activité / Verbe", "Lieu / Complément", "Code association"],
        "ex2_rows": [
            ["1. Se baigner et bronzer...", "A. dans une station de ski en hiver", "1 -> [    ]"],
            ["2. Faire des randonnées...", "B. au syndicat d'initiative / office de tourisme", "2 -> [    ]"],
            ["3. Demander un plan de ville...", "C. sur la plage au bord de la mer Méditerranée", "3 -> [    ]"],
            ["4. Acheter des souvenirs...", "D. sur les sentiers balisés de montagne", "4 -> [    ]"],
            ["5. Faire du ski alpin...", "E. dans les petites boutiques du centre historique", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : PLANIFIER SES VACANCES & MÉTÉO",
        "cloze_tip_text": "Complétez les dialogues sans regarder de lexique, en mobilisant les collocations réelles du tourisme.",
        "dialogues": [
            {
                "title": "Situation A — À l'office de tourisme de Nice (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La touriste : Bonjour, je voudrais un ___________________________ [city map] et la liste des musées à visiter.",
                    "• L'agent : Bonjour Madame. Voici le plan. Je vous conseille le ___________________________ [castle hill] pour une vue magnifique.",
                    "• La touriste : Merci ! Quels sont les ___________________________ [opening hours / schedules] de la cathédrale ?"
                ]
            },
            {
                "title": "Situation B — Consulter le bulletin météo à la radio (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le présentateur : Demain matin sur le nord du pays, il fera ___________________________ [cold] avec seulement 4 degrés.",
                    "• Le présentateur : L'après-midi, il y aura du ___________________________ [fog] et quelques averses de ___________________________ [rain].",
                    "• Le présentateur : Dans le sud au contraire, le ciel sera ___________________________ [sunny / clear] et très agréable."
                ]
            },
            {
                "title": "Situation C — Départ en week-end et bagages (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Thomas : Tu as fini de faire ta ___________________________ [suitcase] ?",
                    "• Sophie : Presque ! N'oublie pas tes ___________________________ [sunglasses] et ton maillot de bain.",
                    "• Thomas : Parfait, et j'emporte aussi mon ___________________________ [camera] pour immortaliser le paysage."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. What is the weather like today in Paris?", "-> __________________________________________________________________________________"],
            ["2. It is sunny but it is very windy.", "-> __________________________________________________________________________________"],
            ["3. We want to visit the castle and the historical museum.", "-> __________________________________________________________________________________"],
            ["4. Take a raincoat because it is going to rain this afternoon.", "-> __________________________________________________________________________________"],
            ["5. Where is the tourism office located?", "-> __________________________________________________________________________________"],
            ["6. We spent our summer holidays at the beach.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le musée  •  Le château  •  Le monument  •  L'orage", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La pluie  •  La neige  •  Le soleil  •  La valise", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Il fait beau  •  Il fait chaud  •  Il fait froid  •  Il y a un musée", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La plage  •  La montagne  •  La mer  •  L'embouteillage", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le château -> '-eau' son [o] | 2. le musée -> masculin malgré la fin en '-ée' | 3. nuageux -> 'x' muet [ø] | 4. le soleil -> terminaison [ɛj] | 5. la pluie -> son [ɥi] | 6. le brouillard -> 'd' muet et liquide [j].\nExercice 1.2 — Orthographe [3 pts] :\na) la météo | b) un musée | c) un château | d) la température | e) un appareil photo | f) une station balnéaire.\nExercice 1.3 — Liaisons [3 pts] :\n1. un office [n] | 2. des anciens châteaux [z] | 3. il y a (enchaînement) | 4. un orage [n] | 5. les îles [z] | 6. un grand hôtel [t] (le 'd' se lie en 't').",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. le musée (M) | 2. le château (M) | 3. la pluie (F) | 4. le soleil (M) | 5. le vent (M) | 6. la neige (F) | 7. la plage (F) | 8. la montagne (F) | 9. l'orage (M) | 10. la valise (F) | 11. le guide (M) | 12. la carte postale (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UN magnifique musée (musée est masculin) | 2. LA pluie (pluie est féminin) | 3. UNE grande valise (valise est féminin) | 4. UN violent orage (orage est masculin).",
        "tier3_text": "Exercice 3.1 — Formules Météo [5 pts] :\n1. fait | 2. du | 3. pleut | 4. valises | 5. prendre.\nExercice 3.2 — Paires Activités [5 pts] :\n1 -> C (Se baigner sur la plage) | 2 -> D (Faire des randonnées en montagne) | 3 -> B (Demander un plan à l'office) | 4 -> E (Acheter des souvenirs) | 5 -> A (Faire du ski en station).",
        "tier4_text": "Situation A (3 pts) : plan de ville | château (ou colline du château) | horaires (d'ouverture).\nSituation B (4 pts) : froid | brouillard | pluie | ensoleillé (ou dégagé).\nSituation C (3 pts) : valise | lunettes de soleil | appareil photo.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Quel temps fait-il aujourd'hui à Paris ? | 2. Il y a du soleil mais il y a beaucoup de vent. (ou : Il fait beau mais il fait du vent). | 3. Nous voulons visiter le château et le musée d'histoire. | 4. Prends un imperméable car il va pleuvoir cet après-midi. | 5. Où se trouve l'office de tourisme ? | 6. Nous avons passé nos vacances d'été à la plage.\nExercice 5.2 — Intrus [4 pts] :\n1. L'orage (phénomène météo, les autres sont des sites touristiques) | 2. La valise (bagage de voyage, les autres sont des éléments météo) | 3. Il y a un musée (phrase de localisation, les autres sont des expressions de météo avec 'il fait') | 4. L'embouteillage (terme de circulation routière, les autres sont des destinations de vacances/nature).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 19",
        "anchors_text": "1. La règle d'or de la météo : 'IL FAIT' s'emploie avec des adjectifs (il fait beau, chaud, froid, mauvais). 'IL Y A' s'emploie avec l'article partitif + nom (il y a du soleil, du vent, de la pluie, du brouillard, des nuages). Ne jamais dire 'Il fait soleil' en bon français !\n2. Le piège de 'musée' : Bien qu'il se termine par un 'e' accentué suivi d'un 'e' muet (-ée), 'le musée' est rigoureusement masculin, tout comme 'le lycée' et 'le trophée'.\n3. 'La valise' : En français, pour dire 'to pack', on utilise la colocation vivante 'faire sa valise' (faire ses bagages)."
    }
}

# CHAPTER 20: L'hôtellerie, le camping et les gîtes
batch2["20"] = {
    "ch_num": 20,
    "title_fr": "L'hôtellerie, le camping et les gîtes",
    "title_en": "Accommodations, Hotels, Campsites & Gîtes",
    "word_count": 42,
    "traps": [
        "Vocabulary distinction: 'la chambre simple' (single room with 1 single bed) vs 'la chambre double' (room with 1 double bed) vs 'la chambre twin' (two separate beds).",
        "False friend / concept: 'Le gîte rural' is a uniquely French furnished holiday home in the countryside, self-catering.",
        "Gender traps: 'l'hôtel' (m.), 'l'hébergement' (m.), 'le séjour' (m.), 'l'emplacement' (m.), 'la clé' (f.), 'la tente' (f.), 'la réception' (f.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'H' MUET D'HÔTEL ET L'ACCENT CIRCONFLEXE DE GÎTE",
        "phonetic_tip_text": "'Hôtel' commence par un 'h' muet : l'élision est obligatoire ('l'hôtel' [loh-tel]) ainsi que la liaison ('les hôtels' [lay-zoh-tel]). 'Gîte' comporte un accent circonflexe sur le 'i' rappelant l'ancien français (gésir).",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de l'Hôtellerie [4 pts]",
        "ex1_headers": ["Terme hébergement", "Genre", "Caractéristique phonétique", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. l'hôtel (m.)", "Masculin", "H muet avec élision", "[ loh-tel ]", "Jamais d'aspiration"],
            ["2. le gîte (m.)", "Masculin", "Circonflexe sur 'i'", "[ zheet ]", "Son [ʒ] doux sans 'd'"],
            ["3. la clé / clef (f.)", "Féminin", "Graphème '-é' ou '-ef'", "[ klay ]", "Consonne 'f' muette en 'clef'"],
            ["4. le petit-déjeuner (m.)", "Masculin", "E caduc dans 'petit'", "[ puh-tee day-zhuh-nay ]", "Rythme ternaire fluide"],
            ["5. la réception (f.)", "Féminin", "Suffixe '-tion'", "[ ray-sep-syohn ]", "Son [sjɔ̃] nasal pur"],
            ["6. la tente (f.)", "Féminin", "Graphème '-en-' nasal", "[ tahnt ]", "Nasale [ɑ̃], 'te' muet"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un hotel -> ________________________",
            "b) un gite rural -> ________________________",
            "c) reserver une nuit -> ________________________",
            "d) la reception -> ________________________",
            "e) une cle -> ________________________",
            "f) le reglement (paiement) -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Hôtelières [3 pts]",
        "ex3_items": [
            "1. un hôtel trois étoiles -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. trois étoiles          -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un emplacement         -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. petit-déjeuner inclus  -> [  ] Liaison [r] ou enchaînement [  ] Pas de liaison",
            "5. deux adultes           -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un accueil chaleureux  -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES TYPES D'HÉBERGEMENT ET SERVICES",
        "gender_rule_text": "Types d'hébergement : l'hôtel (m.), le camping (m.), le gîte (m.), l'appartement (m.), mais l'auberge de jeunesse (f.). Équipements de chambre : le lit (m.), le drap (m.), le balcon (m.), mais la douche (f.), la salle de bains (f.), la climatisation (f.), la serviette (f.).",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Hôtellerie & Camping [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ chambre (f.)", "[   ] M   [   ] F", "7. _______ camping (m.)", "[   ] M   [   ] F"],
            ["2. _______ hôtel (m.)", "[   ] M   [   ] F", "8. _______ tente (f.)", "[   ] M   [   ] F"],
            ["3. _______ lit (m.)", "[   ] M   [   ] F", "9. _______ serviette (f.)", "[   ] M   [   ] F"],
            ["4. _______ clé (f.)", "[   ] M   [   ] F", "10. _______ facture (f.)", "[   ] M   [   ] F"],
            ["5. _______ ascenseur (m.)", "[   ] M   [   ] F", "11. _______ climatisation (f.)", "[   ] M   [   ] F"],
            ["6. _______ gîte (m.)", "[   ] M   [   ] F", "12. _______ parking (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Nous avons réservé un chambre double avec vue sur la mer pour trois nuits.\n   Correction : _____________________________________________________________________________",
            "2. Le réceptionniste m'a donné le clé magnétique de la chambre 204.\n   Correction : _____________________________________________________________________________",
            "3. Cet hôtel possède une magnifique ascenseur vitré dans le hall principal.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons loué un gîte rustique avec une grand terrasse en bois.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS D'ACCUEIL & DE SÉJOUR EN FRANCE",
        "colloc_tip_text": "'Réserver une chambre pour deux personnes', 'régler la note / l'addition', 'monter la tente sur un emplacement', 'le petit-déjeuner est compris', 'remettre la clé'.",
        "ex1_title": "Exercice 3.1 — Formules de Réservation & Prestations [5 pts]",
        "ex1_sentences": [
            "1. Le prix de la nuitée est de 85 euros, petit-déjeuner _________ (compris / fini) dans la formule.",
            "2. À votre arrivée à l'hôtel, veuillez vous présenter à la _________ (réception / poste) pour l'enregistrement.",
            "3. En quittant la chambre à midi, n'oubliez pas de rendre la _________ (clé / valise) à l'accueil.",
            "4. Au camping municipal, nous avons planté notre _________ (tente / maison) sur l'emplacement numéro 12.",
            "5. Les touristes aiment louer un gîte pour profiter du calme de la _________ (campagne / chambre)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Verbe-Procédure Hôtelière [5 pts]",
        "ex2_headers": ["Verbe d'action", "Objet / Procédure", "Code association"],
        "ex2_rows": [
            ["1. Réserver...", "A. la note par carte bancaire au check-out", "1 -> [    ]"],
            ["2. Remplir...", "B. une chambre double pour deux nuitées", "2 -> [    ]"],
            ["3. Régler...", "C. la fiche de police / d'enregistrement", "3 -> [    ]"],
            ["4. Déposer...", "D. ses bagages à la consigne de l'hôtel", "4 -> [    ]"],
            ["5. Planter...", "E. sa tente sur un emplacement ombragé", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : SITUATIONS D'ENREGISTREMENT EN HÔTEL",
        "cloze_tip_text": "Complétez les dialogues d'hébergement en récupérant le lexique précis sans liste de mots.",
        "dialogues": [
            {
                "title": "Situation A — Enregistrement (Check-in) à la réception (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le réceptionniste : Bonjour Monsieur, vous avez une ___________________________ [reservation] ?",
                    "• Le client : Oui, au nom de Martin. Une chambre ___________________________ [double] pour trois nuits.",
                    "• Le réceptionniste : Très bien. Voici votre ___________________________ [key] pour la chambre 312 au troisième étage."
                ]
            },
            {
                "title": "Situation B — Renseignements au camping (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le campeur : Bonjour, est-ce qu'il vous reste un ___________________________ [pitch / campsite spot] pour une tente et une voiture ?",
                    "• La gérante : Oui, il nous reste une place avec branchement ___________________________ [electric / electricity].",
                    "• Le campeur : Parfait. Où se trouvent les ___________________________ [sanitary facilities / showers] ?",
                    "• La gérante : Tout droit après la piscine. Voici le badge d'entrée pour la ___________________________ [gate / barrier]."
                ]
            },
            {
                "title": "Situation C — Départ de l'hôtel (Check-out) (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La cliente : Bonjour, je voudrais régler la ___________________________ [bill / invoice], s'il vous plaît.",
                    "• Le réceptionniste : Certainement. Avez-vous consommé des boissons du ___________________________ [minibar] ?",
                    "• La cliente : Non, rien. Je vais payer par ___________________________ [credit card]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I would like to book a room for two nights.", "-> __________________________________________________________________________________"],
            ["2. Is breakfast included in the price of the room?", "-> __________________________________________________________________________________"],
            ["3. We prefer to rent a cottage in the countryside.", "-> __________________________________________________________________________________"],
            ["4. Can you give me the key to room 105, please?", "-> __________________________________________________________________________________"],
            ["5. There is no air conditioning in our bedroom.", "-> __________________________________________________________________________________"],
            ["6. We have set up our tent near the river.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. L'hôtel  •  Le gîte  •  Le camping  •  L'aéroport", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La chambre simple  •  La chambre double  •  La suite  •  Le volant", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La clé  •  La carte d'accès  •  Le digicode  •  La tente", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La douche  •  Le lavabo  •  La baignoire  •  Le passeport", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. l'hôtel -> 'h' muet avec élision [loh-tel] | 2. le gîte -> circonflexe sur 'i' [zheet] | 3. la clé -> son [klay] | 4. le petit-déjeuner -> e caduc [puh-tee day-zhuh-nay] | 5. la réception -> suffixe nasal [sjɔ̃] | 6. la tente -> nasale [ɑ̃] avec 'te' muet.\nExercice 1.2 — Orthographe [3 pts] :\na) un hôtel | b) un gîte rural | c) réserver | d) la réception | e) une clé (ou clef) | f) le règlement.\nExercice 1.3 — Liaisons [3 pts] :\n1. un hôtel [n] | 2. trois étoiles [z] | 3. un emplacement [n] | 4. petit-déjeuner inclus (enchaînement) | 5. deux adultes [z] | 6. un accueil [n].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la chambre (F) | 2. l'hôtel (M) | 3. le lit (M) | 4. la clé (F) | 5. l'ascenseur (M) | 6. le gîte (M) | 7. le camping (M) | 8. la tente (F) | 9. la serviette (F) | 10. la facture (F) | 11. la climatisation (F) | 12. le parking (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UNE chambre double (chambre est féminin) | 2. LA clé magnétique (clé est féminin) | 3. UN magnifique ascenseur (ascenseur est masculin) | 4. UNE GRANDE terrasse (terrasse est féminin).",
        "tier3_text": "Exercice 3.1 — Formules Réservation [5 pts] :\n1. compris | 2. réception | 3. clé | 4. tente | 5. campagne.\nExercice 3.2 — Paires Procédures [5 pts] :\n1 -> B (Réserver une chambre) | 2 -> C (Remplir la fiche) | 3 -> A (Régler la note) | 4 -> D (Déposer ses bagages) | 5 -> E (Planter sa tente).",
        "tier4_text": "Situation A (3 pts) : réservation | double | clé.\nSituation B (4 pts) : emplacement | électrique | sanitaires (ou douches) | barrière.\nSituation C (3 pts) : facture (ou note) | minibar | carte bancaire (ou carte de crédit).",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je voudrais réserver une chambre pour deux nuits. | 2. Est-ce que le petit-déjeuner est compris dans le prix de la chambre ? | 3. Nous préférons louer un gîte à la campagne. | 4. Pouvez-vous me donner la clé de la chambre 105, s'il vous plaît ? | 5. Il n'y a pas de climatisation dans notre chambre. | 6. Nous avons monté (ou installé) notre tente près de la rivière.\nExercice 5.2 — Intrus [4 pts] :\n1. L'aéroport (infrastructure de transport, les autres sont des lieux d'hébergement touristique) | 2. Le volant (pièce de voiture, les autres sont des types de chambres d'hôtel) | 3. La tente (abri de camping, les autres sont des dispositifs pour ouvrir une porte de chambre) | 4. Le passeport (document d'identité officiel, les autres sont des équipements sanitaires de salle de bains).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 20",
        "anchors_text": "1. Le concept typique du 'gîte' : En France, un gîte rural est une maison ou un appartement de vacances meublé et équipé (avec cuisine), situé à la campagne ou dans un village, souvent labellisé par 'Gîtes de France'.\n2. 'Petit-déjeuner compris' : Formule consacrée équivalente à 'bed and breakfast' ou 'breakfast included'. Si ce n'est pas inclus, on dit 'petit-déjeuner en supplément'.\n3. Clé ou clef : Les deux orthographes existent en français, mais 'clé' est la forme moderne la plus courante. Le genre est invariable : toujours féminin (la clé)."
    }
}

# CHAPTER 21: Les fruits, les légumes et le marché
batch2["21"] = {
    "ch_num": 21,
    "title_fr": "Les fruits, les légumes et le marché",
    "title_en": "Fruits, Vegetables & The Open-Air Market",
    "word_count": 46,
    "traps": [
        "Gender of common produce: 'la pomme', 'la fraise', 'la banane', 'l'orange' (f.), 'la tomate' (f.), 'la carotte' (f.), 'la salade' (f.), but 'le citron' (m.), 'le raisin' (m.), 'le melon' (m.), 'l'oignon' (m.), 'le poivron' (m.), 'l'ail' (m.).",
        "Quantities and Partitives: 'un kilo DE pommes', '500 grammes DE fraises', 'une livre DE cerises' (DE without article after quantity expressions!).",
        "Liaison and silent letters: 'les haricots' has an ASPIRATED H ('le haricot', 'les [no liaison!] haricots'), while 'l'oignon' has a silent 'g' and nasal [ɔ̃]."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE 'H' ASPIRÉ DE HARICOT ET LA PHONÉTIQUE DE L'OIGNON",
        "phonetic_tip_text": "Attention maximale : 'le haricot' a un 'h' aspiré ! Jamais de liaison ni d'élision : on dit 'le haricot' (pas l'haricot) et 'les haricots' [lay ah-ree-koh] sans liaison en [z] ! 'Oignon' se prononce [oh-nyohn] sans prononcer le 'g' dur.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Marché [4 pts]",
        "ex1_headers": ["Légume / Fruit", "Genre", "Particularité sonore", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. les haricots (m. pl.)", "Masculin pl.", "H aspiré : ZÉRO liaison", "[ lay ah-ree-koh ]", "Interdiction de liaison [z]"],
            ["2. l'oignon (m.)", "Masculin", "Graphème '-gn-' liquide", "[ oh-nyohn ]", "'g' silencieux, son [ɲ]"],
            ["3. l'ail (m.)", "Masculin", "Graphème '-il' liquide", "[ ahy ]", "Son [aj] très bref"],
            ["4. le raisin (m.)", "Masculin", "Graphème '-in' nasal", "[ ray-zanh ]", "Nasale [ɛ̃] pure"],
            ["5. la pomme (f.)", "Féminin", "Voyelle 'o' ouverte", "[ pohm ]", "Son [ɔ] bref et franc"],
            ["6. la fraise (f.)", "Féminin", "'s' intervocalique sonore", "[ frez ]", "Son [z] et non [s]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un legume -> ________________________",
            "b) une peche (fruit) -> ________________________",
            "c) un ananas -> ________________________",
            "d) un concombre -> ________________________",
            "e) un kilo de pommes de terre -> ________________________",
            "f) une botte de radis -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Piège du H Aspiré [3 pts]",
        "ex3_items": [
            "1. les haricots verts    -> [  ] Liaison [z] interdite (H aspiré) [  ] Liaison obligatoire",
            "2. un oignon jaune       -> [  ] Liaison [n] obligatoire          [  ] Pas de liaison",
            "3. des oranges bio       -> [  ] Liaison [z] obligatoire          [  ] Pas de liaison",
            "4. un avocat bien mûr    -> [  ] Liaison [n] obligatoire          [  ] Pas de liaison",
            "5. deux ananas           -> [  ] Liaison [z] obligatoire          [  ] Pas de liaison",
            "6. un kilo de fraises    -> [  ] Pas de liaison                   [  ] Liaison obligatoire"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES FRUITS ET LÉGUMES SUR LES ÉTALS",
        "gender_rule_text": "Fruits féminins fréquents : la pomme, la poire, la banane, la fraise, la cerise, l'orange, la pêche. Fruits masculins : le citron, le melon, le raisin, l'ananas, l'abricot, le pamplemousse. Légumes féminins : la tomate, la carotte, la salade, la courgette, l'aubergine. Légumes masculins : le poivron, le concombre, l'oignon, le champignon, le poireau, l'ail.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Fruits & Légumes [6 pts]",
        "ex1_headers": ["Aliment avec article", "Genre (M/F)", "Aliment avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ pomme (f.)", "[   ] M   [   ] F", "7. _______ poivron (m.)", "[   ] M   [   ] F"],
            ["2. _______ raisin (m.)", "[   ] M   [   ] F", "8. _______ courgette (f.)", "[   ] M   [   ] F"],
            ["3. _______ tomate (f.)", "[   ] M   [   ] F", "9. _______ oignon (m.)", "[   ] M   [   ] F"],
            ["4. _______ citron (m.)", "[   ] M   [   ] F", "10. _______ aubergine (f.)", "[   ] M   [   ] F"],
            ["5. _______ carotte (f.)", "[   ] M   [   ] F", "11. _______ champignon (m.)", "[   ] M   [   ] F"],
            ["6. _______ melon (m.)", "[   ] M   [   ] F", "12. _______ salade (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Donnez-moi un belle pomme rouge et deux citrons verts bien frais.\n   Correction : _____________________________________________________________________________",
            "2. Ce melon est très parfumée et sucrée, goûtez-en une tranche !\n   Correction : _____________________________________________________________________________",
            "3. J'ai acheté une kilo de poivrons jaunes pour préparer la ratatouille.\n   Correction : _____________________________________________________________________________",
            "4. La carotte râpé est une entrée classique des bistrots français.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS MARCHANDES & QUANTITÉS AVEC 'DE'",
        "colloc_tip_text": "Règle de syntaxe essentielle : après une expression de quantité (un kilo, 500 grammes, une livre, une barquette, une botte), l'article disparaît au profit de 'DE' ou 'D'' (un kilo DE pommes, une barquette DE fraises, une botte DE radis).",
        "ex1_title": "Exercice 3.1 — Quantités & Expressions d'Achat au Marché [5 pts]",
        "ex1_sentences": [
            "1. Je voudrais un kilo _________ (de / des) carottes des sables, s'il vous plaît.",
            "2. Donnez-moi aussi une barquette _________ (de / du) fraises bien mûres de Plougastel.",
            "3. Pour la soupe, le client demande une belle botte _________ (de / des) poireaux frais.",
            "4. Ces abricots coûtent 4 euros _________ (le / au) kilo sur le marché de Provence.",
            "5. Le marchand demande à la fin : 'Et avec ceci, ce _________ (sera / fera) tout ?'"
        ],
        "ex2_title": "Exercice 3.2 — Paires Produit-Unité Marchande [5 pts]",
        "ex2_headers": ["Unité de mesure / contenant", "Produit du marché", "Code association"],
        "ex2_rows": [
            ["1. Une barquette...", "A. de radis croquants avec leurs fanes", "1 -> [    ]"],
            ["2. Un kilo...", "B. de fraises gariguettes parfumées", "2 -> [    ]"],
            ["3. Une botte...", "C. d'oranges à jus", "3 -> [    ]"],
            ["4. Une tête / gousse...", "D. de pommes de terre nouvelles", "4 -> [    ]"],
            ["5. Un filet...", "E. d'ail de Lautrec", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : DIALOGUES AU MARCHÉ FORAIN",
        "cloze_tip_text": "Complétez les interactions chez le marchand de fruits et légumes sans liste de choix.",
        "dialogues": [
            {
                "title": "Situation A — Commande de fruits de saison (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le primeur : Bonjour Madame, qu'est-ce qui vous ferait ___________________________ [pleasure / would you like] aujourd'hui ?",
                    "• La cliente : Bonjour ! Je voudrais deux ___________________________ [kilos] de belles pommes et un melon.",
                    "• Le primeur : Très bien. Le melon, vous le voulez pour consommer ___________________________ [today] ou pour ce week-end ?"
                ]
            },
            {
                "title": "Situation B — Légumes pour la soupe d'hiver (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le client : Je vais vous prendre une livre de ___________________________ [carrots] et deux poireaux.",
                    "• Le primeur : Parfait. Voulez-vous aussi un kilo de ___________________________ [potatoes] pour lier le potage ?",
                    "• Le client : Oui, et ajoutez un ___________________________ [onion] et deux gousses d'___________________________ [garlic]."
                ]
            },
            {
                "title": "Situation C — Pesée et règlement au stand (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La marchande : Voilà, cela nous fait un total de 14 euros et 50 ___________________________ [cents].",
                    "• La cliente : Est-ce que vous prenez la ___________________________ [credit card] ou seulement les espèces ?",
                    "• La marchande : Nous prenons la carte sans ___________________________ [contact / contactless] dès un euro !"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I would like a kilo of tomatoes and a bunch of carrots, please.", "-> __________________________________________________________________________________"],
            ["2. How much does a kilo of strawberries cost?", "-> __________________________________________________________________________________"],
            ["3. These peaches are ripe, sweet and delicious.", "-> __________________________________________________________________________________"],
            ["4. Do you have green beans today on your stall?", "-> __________________________________________________________________________________"],
            ["5. That will be all, thank you very much.", "-> __________________________________________________________________________________"],
            ["6. We buy our fresh fruits at the Sunday market.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La pomme  •  La fraise  •  La poire  •  La carotte", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La courgette  •  L'aubergine  •  Le poivron  •  Le croissant", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Un kilo  •  Une livre  •  Une barquette  •  Un musée", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Le citron  •  L'orange  •  Le pamplemousse  •  Le poulet", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. les haricots -> 'h' aspiré, zéro liaison [lay ah-ree-koh] | 2. l'oignon -> 'g' muet, son [oh-nyohn] | 3. l'ail -> liquide bref [ahy] | 4. le raisin -> nasale pure [ray-zanh] | 5. la pomme -> son ouvert [pohm] | 6. la fraise -> 's' intervocalique sonne [z].\nExercice 1.2 — Orthographe [3 pts] :\na) un légume | b) une pêche | c) un ananas | d) un concombre | e) pommes de terre | f) une botte de radis.\nExercice 1.3 — Liaisons [3 pts] :\n1. les haricots (interdite - H aspiré) | 2. un oignon [n] | 3. des oranges [z] | 4. un avocat [n] | 5. deux ananas [z] | 6. un kilo de fraises (pas de liaison).",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la pomme (F) | 2. le raisin (M) | 3. la tomate (F) | 4. le citron (M) | 5. la carotte (F) | 6. le melon (M) | 7. le poivron (M) | 8. la courgette (F) | 9. l'oignon (M) | 10. l'aubergine (F) | 11. le champignon (M) | 12. la salade (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UNE belle pomme (pomme est féminin) | 2. Ce melon est très PARFUMÉ et SUCRÉ (melon est masculin) | 3. UN kilo de poivrons (kilo est masculin) | 4. La carotte RÂPÉE (accord au féminin avec carotte).",
        "tier3_text": "Exercice 3.1 — Quantités & Expressions [5 pts] :\n1. de | 2. de | 3. de | 4. le | 5. sera.\nExercice 3.2 — Paires Unités [5 pts] :\n1 -> B (Une barquette de fraises) | 2 -> D (Un kilo de pommes de terre) | 3 -> A (Une botte de radis) | 4 -> E (Une tête d'ail) | 5 -> C (Un filet d'oranges).",
        "tier4_text": "Situation A (3 pts) : plaisir | kilos | aujourd'hui.\nSituation B (4 pts) : carottes | pommes de terre | oignon | ail.\nSituation C (3 pts) : centimes | carte bancaire | contact.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je voudrais un kilo de tomates et une botte de carottes, s'il vous plaît. | 2. Combien coûte un kilo de fraises ? | 3. Ces pêches sont mûres, sucrées et délicieuses. | 4. Avez-vous des haricots verts aujourd'hui sur votre étal ? | 5. Ce sera tout, merci beaucoup. | 6. Nous achetons nos fruits frais au marché du dimanche.\nExercice 5.2 — Intrus [4 pts] :\n1. La carotte (légume / racine, alors que les autres sont des fruits sucrés) | 2. Le croissant (viennoiserie de boulangerie, les autres sont des légumes méditerranéens) | 3. Un musée (lieu culturel, les autres sont des mesures/conditionnements marchands) | 4. Le poulet (viande de volaille, les autres sont des agrumes).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 21",
        "anchors_text": "1. Le piège d'or du H aspiré : 'Le haricot' a un H aspiré d'origine germanique. On ne dit jamais 'l'haricot' ni 'les-z-haricots' ! De même pour 'le hors-d'œuvre'.\n2. La syntaxe des quantités en DE : Dès qu'une quantité précise est exprimée (un kilo, une barquette, beaucoup, peu), l'article partitif ou défini devient systématiquement DE ou D' (un kilo DE pommes, et non des pommes).\n3. 'Une livre' : Dans les marchés français, une livre désigne traditionnellement un demi-kilo (500 grammes) : 'une livre de cerises'."
    }
}

# CHAPTER 22: Les viandes, les poissons, les œufs et les céréales
batch2["22"] = {
    "ch_num": 22,
    "title_fr": "Les viandes, les poissons, les œufs et les céréales",
    "title_en": "Meats, Seafood, Eggs, Grains & Bakery",
    "word_count": 45,
    "traps": [
        "Plural pronunciation of ŒUF: singular 'un œuf' pronounces the 'f' [un nuff], but plural 'des œufs' is silent [day zuh]! Same for 'un bœuf' [un buff] vs 'des bœufs' [day buh].",
        "Meat types vs live animals: 'le bœuf' (beef / steer), 'le porc' (pork / pig), 'le veau' (veal / calf), 'le poulet' (chicken), 'l'agneau' (lamb).",
        "Gender traps: 'le poisson' (m.), 'le saumon' (m.), 'le steak' (m.), 'le jambon' (m.), 'le riz' (m.), but 'la viande' (f.), 'la crevette' (f.), 'la baguette' (f.), 'la farine' (f.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LA MUTATION PHONÉTIQUE SPECTACULAIRE : UN ŒUF VS DES ŒUFS",
        "phonetic_tip_text": "Au singulier, le 'f' final de 'œuf' se prononce avec liaison obligatoire : 'un œuf' [uhn nuff]. Au pluriel, le 'f' et le 's' deviennent totalement SILENCIEUX : 'des œufs' [day zuh] ! Même phénomène pour 'le bœuf' [buff] et 'les bœufs' [buh].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Protéines [4 pts]",
        "ex1_headers": ["Aliment", "Nombre", "Consonne finale", "Prononciation IPA", "Phénomène sonore"],
        "ex1_rows": [
            ["1. un œuf (m.)", "Singulier", "Consonne 'f' prononcée", "[ uhn nuff ]", "Liaison [n] et 'f' sonore"],
            ["2. des œufs (m. pl.)", "Pluriel", "Consonnes 'fs' muettes", "[ day zuh ]", "Liaison [z] et 'fs' muets"],
            ["3. le bœuf (m.)", "Singulier", "Consonne 'f' prononcée", "[ buff ]", "Son [œ] avec 'f' sonore"],
            ["4. le porc (m.)", "Singulier", "Consonnes 'rc' muettes", "[ pohr ]", "'c' final muet, [ɔʁ] net"],
            ["5. le saumon (m.)", "Singulier", "Graphème '-on' nasal", "[ soh-mohn ]", "Double [o] fermé et [ɔ̃]"],
            ["6. le poulet (m.)", "Singulier", "Suffixe '-et'", "[ poo-lay ]", "'t' muet, son [e] fermé"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un oeuf -> ________________________",
            "b) une cereale -> ________________________",
            "c) un pate de campagne -> ________________________",
            "d) une cotelette d'agneau -> ________________________",
            "e) des pates fraiches -> ________________________",
            "f) une poissonnerie -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Enchaînements [3 pts]",
        "ex3_items": [
            "1. un œuf frais          -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des œufs durs         -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un steak haché        -> [  ] H aspiré : PAS de liaison  [  ] Liaison obligatoire",
            "4. du porc rôti          -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux agneaux          -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un excellent poisson  -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES VIANDES, POISSONS, CÉRÉALES ET RAYONS",
        "gender_rule_text": "Boucherie & poissons : la viande (f.), la volaille (f.), la côtelette (f.), mais le bœuf, le porc, le veau, le gigot, le poisson, le thon, le saumon, le crabe sont masculins. Féminins marins : la crevette, l'huître, la moule. Féculents : le riz, le blé, le maïs, mais la farine, les pâtes (f. pl.).",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Boucherie & Pêcherie [6 pts]",
        "ex1_headers": ["Produit avec article", "Genre (M/F)", "Produit avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ viande (f.)", "[   ] M   [   ] F", "7. _______ saumon (m.)", "[   ] M   [   ] F"],
            ["2. _______ bœuf (m.)", "[   ] M   [   ] F", "8. _______ crevette (f.)", "[   ] M   [   ] F"],
            ["3. _______ poulet (m.)", "[   ] M   [   ] F", "9. _______ riz (m.)", "[   ] M   [   ] F"],
            ["4. _______ jambon (m.)", "[   ] M   [   ] F", "10. _______ farine (f.)", "[   ] M   [   ] F"],
            ["5. _______ œuf (m.)", "[   ] M   [   ] F", "11. _______ pain (m.)", "[   ] M   [   ] F"],
            ["6. _______ poisson (m.)", "[   ] M   [   ] F", "12. _______ baguette (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Le viande de bœuf est très tendre lorsqu'elle est cuite à basse température.\n   Correction : _____________________________________________________________________________",
            "2. Le poissonnier m'a vendu un belle dorade royale pêchée ce matin.\n   Correction : _____________________________________________________________________________",
            "3. Je vais préparer une plat de riz blanc avec du poulet rôti.\n   Correction : _____________________________________________________________________________",
            "4. Nous mangeons des pâtes italien avec une sauce bolognaise maison.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS CULINAIRES & COMMERCES SPÉCIALISÉS",
        "colloc_tip_text": "On achète : la viande à la boucherie, le porc à la charcuterie, le poisson à la poissonnerie, le pain à la boulangerie. Cuisson de la viande : bleu, saignant, à point, bien cuit. Œufs : œuf au plat, œuf dur, œuf à la coque, omelette.",
        "ex1_title": "Exercice 3.1 — Préparations & Cuissons des Protéines [5 pts]",
        "ex1_sentences": [
            "1. Comment aimez-vous votre steak de bœuf ? Je le préfère _________ (saignant / cuit) avec des frites.",
            "2. Pour le petit-déjeuner à la française, mon père mange un œuf à la _________ (coque / poêle) avec des mouillettes.",
            "3. On achète le rôti de porc et les saucisses artisanales à la _________ (charcuterie / poissonnerie).",
            "4. Pour accompagner le filet de saumon, le chef sert du _________ (riz / pain) basmati vapeur.",
            "5. Les Français achètent leur baguette bien dorée tous les matins à la _________ (boulangerie / boucherie)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Produit-Commerce d'Origine [5 pts]",
        "ex2_headers": ["Produit alimentaire", "Commerce spécialisé", "Code association"],
        "ex2_rows": [
            ["1. Deux filets de saumon frais...", "A. à la boulangerie-pâtisserie", "1 -> [    ]"],
            ["2. Un rôti de veau et un poulet fermier...", "B. à la poissonnerie du port", "2 -> [    ]"],
            ["3. Du saucisson sec et du pâté...", "C. à l'épicerie fine ou au rayon bio", "3 -> [    ]"],
            ["4. Deux baguettes tradition croustillantes...", "D. à la charcuterie artisanale", "4 -> [    ]"],
            ["5. Un paquet de riz complet et de lentilles...", "E. à la boucherie de quartier", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : CHEZ LE BOUCHER ET LE POISSONNIER",
        "cloze_tip_text": "Complétez les dialogues d'achat de protéines sans consulter d'aide lexicale.",
        "dialogues": [
            {
                "title": "Situation A — À la boucherie de quartier (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le boucher : Bonjour Monsieur, qu'est-ce que je vous sers aujourd'hui ?",
                    "• Le client : Je voudrais deux steaks de ___________________________ [beef] bien tendres.",
                    "• Le boucher : Parfait. Vous désirez aussi un beau rôti de ___________________________ [pork / veal] pour dimanche ?"
                ]
            },
            {
                "title": "Situation B — À la poissonnerie (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• La poissonnière : Bonjour ! Regardez nos beaux poissons frais, nous avons du ___________________________ [salmon] et du cabillaud.",
                    "• La cliente : Donnez-moi deux pavés de saumon et 300 grammes de ___________________________ [shrimp / prawns].",
                    "• La poissonnière : Voulez-vous que je nettoie et que j'enlève la ___________________________ [skin / head] du poisson ?",
                    "• La cliente : Oui s'il vous plaît, c'est très ___________________________ [kind / polite] de votre part."
                ]
            },
            {
                "title": "Situation C — À la boulangerie pour le pain quotidien (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le boulanger : Bonjour, que désirez-vous ?",
                    "• Le client : Une ___________________________ [traditional baguette] pas trop cuite, s'il vous plaît.",
                    "• Le boulanger : Et avec ceci ? Deux ___________________________ [croissants] au beurre ?",
                    "• Le client : Oui, et un pain au ___________________________ [chocolate] pour le goûter."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I would like a dozen fresh eggs and a roast chicken.", "-> __________________________________________________________________________________"],
            ["2. How do you want your steak cooked? Medium, please.", "-> __________________________________________________________________________________"],
            ["3. We eat fresh fish twice a week.", "-> __________________________________________________________________________________"],
            ["4. Two traditional baguettes and three croissants, please.", "-> __________________________________________________________________________________"],
            ["5. Do you prefer white rice or Italian pasta with dinner?", "-> __________________________________________________________________________________"],
            ["6. She does not eat pork because of her diet.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le bœuf  •  Le poulet  •  Le porc  •  La baguette", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le saumon  •  La crevette  •  Le thon  •  L'agneau", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Le riz  •  Les pâtes  •  Le blé  •  Le garagiste", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Saignant  •  À point  •  Bien cuit  •  Ensoleillé", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. un œuf -> liaison [n] et 'f' prononcé [uhn nuff] | 2. des œufs -> liaison [z] et 'fs' muets [day zuh] | 3. le bœuf -> 'f' sonore [buff] | 4. le porc -> 'c' muet [pohr] | 5. le saumon -> voyelles [soh-mohn] | 6. le poulet -> 't' muet [poo-lay].\nExercice 1.2 — Orthographe [3 pts] :\na) un œuf (ligature œ) | b) une céréale | c) un pâté de campagne | d) une côtelette d'agneau | e) des pâtes fraîches | f) une poissonnerie.\nExercice 1.3 — Liaisons [3 pts] :\n1. un œuf [n] | 2. des œufs [z] | 3. un steak haché (H aspiré : pas de liaison) | 4. du porc rôti (pas de liaison) | 5. deux agneaux [z] | 6. un excellent poisson [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la viande (F) | 2. le bœuf (M) | 3. le poulet (M) | 4. le jambon (M) | 5. l'œuf (M) | 6. le poisson (M) | 7. le saumon (M) | 8. la crevette (F) | 9. le riz (M) | 10. la farine (F) | 11. le pain (M) | 12. la baguette (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. LA viande de bœuf (viande est féminin) | 2. UNE belle dorade royale (dorade est féminin) | 3. UN plat de riz (plat est masculin) | 4. des pâtes ITALIENNES (pâtes est féminin pluriel).",
        "tier3_text": "Exercice 3.1 — Préparations & Cuissons [5 pts] :\n1. saignant | 2. coque | 3. charcuterie | 4. riz | 5. boulangerie.\nExercice 3.2 — Paires Commerces [5 pts] :\n1 -> B (Saumon à la poissonnerie) | 2 -> E (Rôti et poulet à la boucherie) | 3 -> D (Saucisson à la charcuterie) | 4 -> A (Baguettes à la boulangerie) | 5 -> C (Riz et lentilles à l'épicerie).",
        "tier4_text": "Situation A (3 pts) : bœuf | porc (ou veau).\nSituation B (4 pts) : saumon | crevettes | peau | gentil (ou aimable).\nSituation C (3 pts) : baguette tradition | croissants | chocolat.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je voudrais une douzaine d'œufs frais et un poulet rôti. | 2. Comment voulez-vous votre steak cuit ? À point, s'il vous plaît. | 3. Nous mangeons du poisson frais deux fois par semaine. | 4. Deux baguettes tradition et trois croissants, s'il vous plaît. | 5. Préférez-vous du riz blanc ou des pâtes italiennes avec le dîner ? | 6. Elle ne mange pas de porc à cause de son régime alimentaire.\nExercice 5.2 — Intrus [4 pts] :\n1. La baguette (produit de boulangerie à base de farine, les autres sont des viandes animales) | 2. L'agneau (viande rouge de mammifère terrestre, les autres sont des produits de la mer / poissons / crustacés) | 3. Le garagiste (métier de l'automobile, les autres sont des céréales et féculents) | 4. Ensoleillé (qualificatif de météo, les autres sont des degrés de cuisson de la viande bovine).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 22",
        "anchors_text": "1. La métamorphose de l'œuf : Un œuf [uhn nuff] avec consonne finale sonore, mais des œufs [day zuh] où le son 'f' s'efface totalement au pluriel ! Ce phénomène est unique en français avec 'le bœuf / les bœufs'.\n2. Les degrés de cuisson de la viande en France : Bleu (très peu cuit, tiède au cœur), Saignant (rare / bloody), À point (medium, idéal pour les Français), Bien cuit (well done).\n3. La baguette tradition : En France, la 'baguette tradition' (protégée par décret depuis 1993) est pétrie sans additifs, contrairement à la baguette ordinaire."
    }
}

with open("chapters_batch_2.json", "w", encoding="utf-8") as f:
    json.dump(batch2, f, ensure_ascii=False, indent=2)

print("Batch 2 successfully updated! Chapters now present:", sorted([int(k) for k in batch2.keys()]))
