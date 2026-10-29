import json

batch3 = {}

# CHAPTER 23: Les produits laitiers et les boissons
batch3["23"] = {
    "ch_num": 23,
    "title_fr": "Les produits laitiers et les boissons",
    "title_en": "Dairy Products, Cheeses & Beverages",
    "word_count": 44,
    "traps": [
        "Partitive articles DU, DE LA, DE L', DES with uncountables: 'boire du lait', 'manger du fromage', 'boire de l'eau', 'acheter de la crème', 'commander des boissons'.",
        "Gender traps: 'le fromage' (m. ending in -e!), 'le beurre' (m.), 'le yaourt' (m.), 'le vin' (m.), 'le thé' (m.), 'le café' (m.), but 'la crème' (f.), 'l'eau' (f.), 'la bière' (f.).",
        "Coffee culture & false cognates: 'un café' in France is an ESPRESSO by default (not drip coffee). For milk coffee, say 'un café au lait' or 'un café crème'."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE GRAPHÈME 'EAU' ET LE 'T' FINAL DANS YAOURT",
        "phonetic_tip_text": "'L'eau' [loh] se compose de trois voyelles graphiques pour un seul son [o] pur ! 'Le yaourt' conserve la prononciation du 't' final [yah-oort] contrairement à la règle générale des consonnes finales.",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Boissons & Laitages [4 pts]",
        "ex1_headers": ["Produit laitier / Boisson", "Genre", "Consonne finale", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le yaourt (m.)", "Masculin", "Consonne 't' prononcée", "[ yah-oort ]", "Exception : 't' final sonore"],
            ["2. l'eau (f.)", "Féminin", "Graphème composite 'eau'", "[ loh ]", "Son [o] pur, zéro diphtongue"],
            ["3. le lait (m.)", "Masculin", "Consonne 't' muette", "[ lay ]", "Son [ɛ] ouvert, 't' muet"],
            ["4. le vin (m.)", "Masculin", "Graphème '-in' nasal", "[ vanh ]", "Voyelle nasale [ɛ̃] pure"],
            ["5. la crème (f.)", "Féminin", "Accent grave 'è'", "[ krem ]", "Son [ɛ] ouvert et franc"],
            ["6. le beurre (m.)", "Masculin", "Graphème 'eu' ouvert", "[ buhr ]", "Son [œ] avec 'r' sonore"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) de la creme fraiche -> ________________________",
            "b) un cafe au lait -> ________________________",
            "c) du the vert -> ________________________",
            "d) de l'eau gazeuse -> ________________________",
            "e) une boisson fraiche -> ________________________",
            "f) du fromage de chevre -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Partitifs [3 pts]",
        "ex3_items": [
            "1. un yaourt nature       -> [  ] 'Y' semi-consonne : PAS d'élision [  ] Élision obligatoire",
            "2. de l'eau minérale      -> [  ] Élision obligatoire 'de l''       [  ] Pas d'élision",
            "3. un excellent vin rouge -> [  ] Liaison [t] obligatoire           [  ] Pas de liaison",
            "4. des alcools forts      -> [  ] Liaison [z] obligatoire           [  ] Pas de liaison",
            "5. deux espressos         -> [  ] Liaison [z] obligatoire           [  ] Pas de liaison",
            "6. un grand café          -> [  ] Pas de liaison                    [  ] Liaison obligatoire"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES PRODUITS LAITIERS ET BOISSONS",
        "gender_rule_text": "'Le fromage' et 'le beurre' sont masculins bien qu'ils se terminent par un 'e'. Les boissons : le café, le thé, le vin, le jus de fruits, le soda sont masculins. Féminins : la bière, la limonade, l'eau (minérale/plate/gazeuse), la tisane, l'infusion.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Laitages & Breuvages [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ fromage (m.)", "[   ] M   [   ] F", "7. _______ vin (m.)", "[   ] M   [   ] F"],
            ["2. _______ beurre (m.)", "[   ] M   [   ] F", "8. _______ bière (f.)", "[   ] M   [   ] F"],
            ["3. _______ lait (m.)", "[   ] M   [   ] F", "9. _______ eau (f.)", "[   ] M   [   ] F"],
            ["4. _______ yaourt (m.)", "[   ] M   [   ] F", "10. _______ tisane (f.)", "[   ] M   [   ] F"],
            ["5. _______ crème (f.)", "[   ] M   [   ] F", "11. _______ jus (m.)", "[   ] M   [   ] F"],
            ["6. _______ café (m.)", "[   ] M   [   ] F", "12. _______ limonade (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. La fromage de chèvre est très appréciée sur un morceau de pain frais.\n   Correction : _____________________________________________________________________________",
            "2. Passe-moi la beurre salé pour tartiner sur ma tranche de brioche.\n   Correction : _____________________________________________________________________________",
            "3. Je bois toujours un bière fraîche en terrasse avec mes collègues.\n   Correction : _____________________________________________________________________________",
            "4. Nous commandons un carafe d'eau fraîche pour accompagner le déjeuner.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE BOISSONS : L'ARTICLE PARTITIF & LE CAFÉ",
        "colloc_tip_text": "Quantités indéterminées : 'boire DU café', 'prendre DE LA crème', 'commander DE L'eau minérale'. Au café : 'une carafe d'eau' (free tap water), 'un café serré', 'un café allongé', 'un verre de vin rouge'.",
        "ex1_title": "Exercice 3.1 — Syntaxe des Partitifs & Boissons [5 pts]",
        "ex1_sentences": [
            "1. Tous les matins au réveil, je bois une grande tasse _________ (de / du) café au lait.",
            "2. À midi au restaurant, nous demandons une carafe _________ (d' / de l') eau du robinet.",
            "3. En France, on mange souvent du fromage avec une tranche _________ (de / du) pain et du vin rouge.",
            "4. Pour son dessert, l'enfant prend un yaourt _________ (à la / au) vanille.",
            "5. Tu préfères boire de l'eau plate ou de l'eau _________ (gazeuse / pétillant) ?"
        ],
        "ex2_title": "Exercice 3.2 — Paires Boisson-Conditionnement [5 pts]",
        "ex2_headers": ["Conditionnement / Verre", "Boisson associée", "Code association"],
        "ex2_rows": [
            ["1. Une carafe...", "A. de vin rouge de Bordeaux", "1 -> [    ]"],
            ["2. Une tasse...", "B. d'eau du robinet bien fraîche", "2 -> [    ]"],
            ["3. Un verre...", "C. de bière blonde artisanale", "3 -> [    ]"],
            ["4. Une bouteille...", "D. de thé vert ou de café chaud", "4 -> [    ]"],
            ["5. Un demi (pression)...", "E. de champagne brut pour la fête", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : AU BISTROT & CHEZ LE FROMAGER",
        "cloze_tip_text": "Complétez les répliques en restituant le vocabulaire sans liste d'aide.",
        "dialogues": [
            {
                "title": "Situation A — Commande au comptoir d'un bistrot (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le serveur : Bonjour, qu'est-ce que je vous ___________________________ [serve / bring] ?",
                    "• La cliente : Un café ___________________________ [espresso / black], s'il vous plaît, et un verre d'eau.",
                    "• Le serveur : Tout de suite. Ça vous fera un ___________________________ [euro] et cinquante centimes."
                ]
            },
            {
                "title": "Situation B — Chez le fromager du marché (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le fromager : Bonjour Madame, quel type de ___________________________ [cheese] recherchez-vous ?",
                    "• La cliente : Je voudrais un morceau de ___________________________ [brie / camembert] bien crémeux et du comté.",
                    "• Le fromager : Le comté, vous le préférez jeune ou ___________________________ [aged / mature, 18 mois] ?",
                    "• La cliente : Bien affiné, et donnez-moi aussi un petit fromage de ___________________________ [goat]."
                ]
            },
            {
                "title": "Situation C — Au petit-déjeuner à l'hôtel (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• L'employé : Bonjour, vous désirez du thé ou du ___________________________ [coffee] ?",
                    "• Le client : Un chocolat chaud, s'il vous plaît, avec du ___________________________ [milk] demi-écrémé.",
                    "• L'employé : Parfait. Voici le ___________________________ [butter] doux et la confiture de fraises."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I drink coffee with milk every morning.", "-> __________________________________________________________________________________"],
            ["2. Can we have a carafe of tap water, please?", "-> __________________________________________________________________________________"],
            ["3. Do you have goat cheese or cow's milk cheese?", "-> __________________________________________________________________________________"],
            ["4. She prefers sparkling water with a slice of lemon.", "-> __________________________________________________________________________________"],
            ["5. Would you like a glass of red wine or a cold beer?", "-> __________________________________________________________________________________"],
            ["6. Put some salted butter on the warm bread.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le camembert  •  Le roquefort  •  Le brie  •  L'autocar", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le café  •  Le thé  •  Le vin  •  Le beurre", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. L'eau plate  •  L'eau gazeuse  •  L'eau minérale  •  Le steak", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Du lait  •  De la crème  •  Du yaourt  •  Du gazole", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le yaourt -> 't' final sonore exceptionnel [yah-oort] | 2. l'eau -> graphème 'eau' son [o] pur | 3. le lait -> 't' muet [lay] | 4. le vin -> voyelle nasale pure [vanh] | 5. la crème -> accent grave ouvert [krem] | 6. le beurre -> son [œ] avec 'r' sonore.\nExercice 1.2 — Orthographe [3 pts] :\na) de la crème fraîche | b) un café au lait | c) du thé vert | d) de l'eau gazeuse | e) une boisson fraîche | f) du fromage de chèvre.\nExercice 1.3 — Liaisons [3 pts] :\n1. un yaourt (y semi-consonne : pas d'élision) | 2. de l'eau (élision obligatoire) | 3. un excellent vin [t] | 4. des alcools [z] | 5. deux espressos [z] | 6. un grand café (pas de liaison).",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. le fromage (M) | 2. le beurre (M) | 3. le lait (M) | 4. le yaourt (M) | 5. la crème (F) | 6. le café (M) | 7. le vin (M) | 8. la bière (F) | 9. l'eau (F) | 10. la tisane (F) | 11. le jus (M) | 12. la limonade (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. LE fromage (fromage est masculin) | 2. LE beurre salé (beurre est masculin) | 3. UNE bière fraîche (bière est féminin) | 4. UNE carafe d'eau (carafe est féminin).",
        "tier3_text": "Exercice 3.1 — Partitifs & Boissons [5 pts] :\n1. de | 2. d' | 3. de | 4. à la | 5. gazeuse.\nExercice 3.2 — Paires Conditionnements [5 pts] :\n1 -> B (Carafe d'eau du robinet) | 2 -> D (Tasse de thé ou café) | 3 -> A (Verre de vin rouge) | 4 -> E (Bouteille de champagne) | 5 -> C (Demi de bière pression).",
        "tier4_text": "Situation A (3 pts) : sers | noir (ou express / classique) | euro.\nSituation B (4 pts) : fromage | camembert (ou brie) | affiné (ou vieux) | chèvre.\nSituation C (3 pts) : café | lait | beurre.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je bois du café au lait tous les matins. | 2. Pouvons-nous avoir une carafe d'eau, s'il vous plaît ? | 3. Avez-vous du fromage de chèvre ou du fromage au lait de vache ? | 4. Elle préfère l'eau gazeuse avec une tranche de citron. | 5. Aimeriez-vous un verre de vin rouge ou une bière fraîche ? | 6. Mettez du beurre salé sur le pain chaud.\nExercice 5.2 — Intrus [4 pts] :\n1. L'autocar (véhicule de transport, les autres sont des fromages français) | 2. Le beurre (produit gras solide, les autres sont des boissons liquides) | 3. Le steak (viande bovine, les autres sont des variétés d'eau de table) | 4. Du gazole (carburant routier pour automobile, les autres sont des produits laitiers).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 23",
        "anchors_text": "1. L'eau gratuite au restaurant : En France, la loi oblige tout restaurant à servir gratuitement une 'carafe d'eau' (eau du robinet potable). Si vous demandez 'une bouteille d'eau', le serveur vous apportera une eau minérale payante !\n2. Les partitifs DU, DE LA, DE L' : Dès que la boisson ou l'aliment n'est pas dénombrable, on utilise le partitif : boire DU café, DE LA bière, DE L'eau.\n3. Yaourt et le 'h' / 'y' : On dit 'le yaourt' sans élision (pas l'yaourt) en français courant standard."
    }
}

# CHAPTER 24: Les repas et mettre la table
batch3["24"] = {
    "ch_num": 24,
    "title_fr": "Les repas et mettre la table",
    "title_en": "Meals, Dining Times & Setting the Table",
    "word_count": 45,
    "traps": [
        "The 4 daily meals and their verbs: 'le petit-déjeuner' (prendre son petit-déjeuner), 'le déjeuner' (déjeuner), 'le goûter' (goûter), 'le dîner' (dîner). Note: In Belgium, Switzerland and Quebec, 'déjeuner' is breakfast, 'dîner' is lunch, 'souper' is dinner!",
        "Table setting items: 'l'assiette' (f.), 'la fourchette' (f.), 'la cuillère' (f.), 'la serviette' (f.), but 'le couteau' (m.), 'le verre' (m.), 'le plat' (m.), 'le bol' (m.).",
        "Collocation: 'Mettre la table' (to set the table) vs 'débarrasser la table' (to clear the table)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE GRAPHÈME 'EAU' DANS COUTEAU ET LE SON MOUILLÉ DANS CUILLÈRE",
        "phonetic_tip_text": "'Le couteau' [koo-toh] se termine par '-eau' son [o] pur fermé. 'La cuillère' [kwee-yair] combine la semi-voyelle [ɥi] et la consonne liquide [j] suivie de [ɛʁ] !",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Repas & du Couvert [4 pts]",
        "ex1_headers": ["Objet de table / Repas", "Genre", "Graphème clé", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le couteau (m.)", "Masculin", "Graphème '-eau'", "[ koo-toh ]", "Son [o] pur, 't' net"],
            ["2. la cuillère (f.)", "Féminin", "Graphème '-ll-' liquide", "[ kwee-yair ]", "Son mouillé [jɛʁ]"],
            ["3. l'assiette (f.)", "Féminin", "Double 'tt' avec 'e'", "[ ah-syet ]", "Son [ɛt] sans accent"],
            ["4. le déjeuner (m.)", "Masculin", "Suffixe '-er'", "[ day-zhuh-nay ]", "'r' muet, son [e] pur"],
            ["5. la fourchette (f.)", "Féminin", "Double 'tt' féminisant", "[ foor-shet ]", "Son [ʃɛt] net et sec"],
            ["6. le goûter (m.)", "Masculin", "Accent circonflexe 'û'", "[ goo-tay ]", "'r' muet, circonflexe étymologique"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) le dejeuner -> ________________________",
            "b) le diner -> ________________________",
            "c) le gouter des enfants -> ________________________",
            "d) une cuillere a soupe -> ________________________",
            "e) une assiette creuse -> ________________________",
            "f) debarrasser la table -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Couverts [3 pts]",
        "ex3_items": [
            "1. une assiette creuse     -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. des assiettes plates    -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un élégant couvert      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. mettre la table         -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux enfants à table    -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand appétit        -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DU COUVERT ET DES ÉLÉMENTS DE TABLE",
        "gender_rule_text": "Les couverts : le couteau (m.), mais la fourchette (f.), la cuillère (f.). La vaisselle : l'assiette (f.), la soupière (f.), la serviette (f.), la nappe (f.), la tasse (f.), la carafe (f.), mais le verre (m.), le bol (m.), le plat (m.), le saladier (m.).",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Couverts & Vaisselle [6 pts]",
        "ex1_headers": ["Élément avec article", "Genre (M/F)", "Élément avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ fourchette (f.)", "[   ] M   [   ] F", "7. _______ assiette (f.)", "[   ] M   [   ] F"],
            ["2. _______ couteau (m.)", "[   ] M   [   ] F", "8. _______ verre (m.)", "[   ] M   [   ] F"],
            ["3. _______ cuillère (f.)", "[   ] M   [   ] F", "9. _______ serviette (f.)", "[   ] M   [   ] F"],
            ["4. _______ plat (m.)", "[   ] M   [   ] F", "10. _______ nappe (f.)", "[   ] M   [   ] F"],
            ["5. _______ bol (m.)", "[   ] M   [   ] F", "11. _______ carafe (f.)", "[   ] M   [   ] F"],
            ["6. _______ tasse (f.)", "[   ] M   [   ] F", "12. _______ saladier (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Pose le grand fourchette à gauche de l'assiette pour le service du dîner.\n   Correction : _____________________________________________________________________________",
            "2. Ce couteau est très tranchante, fais attention en coupant la viande.\n   Correction : _____________________________________________________________________________",
            "3. N'oublie pas de mettre un serviette propre à côté de chaque convive.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons acheté une nouveau plat ovale pour servir le poisson rôti.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE TABLE : METTRE, DÉBARRASSER ET PASSER",
        "colloc_tip_text": "Expressions clés : 'mettre la table' (to lay the table), 'débarrasser la table' (to clear the table), 'passer le sel / le pain' (to pass the salt/bread), 'souhaiter bon appétit', 'se mettre à table' (to sit down for dinner).",
        "ex1_title": "Exercice 3.1 — Chunks Communicatifs Autour du Repas [5 pts]",
        "ex1_sentences": [
            "1. Les enfants, venez vous laver les mains, il est temps de se mettre _________ (à / sur la) table !",
            "2. Avant de commencer à manger, l'hôte sourit et dit chaleureusement : 'Bon _________ (appétit / repas) !'",
            "3. Peux-tu me _________ (passer / jeter) le sel et le poivre, s'il te plaît ?",
            "4. Après le repas, les enfants aident leurs parents à _________ (débarrasser / casser) la table.",
            "5. Les Français prennent leur dîner généralement vers 19h30 ou 20 _________ (heures / minutes)."
        ],
        "ex2_title": "Exercice 3.2 — Paires Objet de Table-Position [5 pts]",
        "ex2_headers": ["Élément de table", "Emplacement traditionnel français", "Code association"],
        "ex2_rows": [
            ["1. La fourchette...", "A. au centre, face au convive", "1 -> [    ]"],
            ["2. Le couteau...", "B. à droite de l'assiette, lame vers l'intérieur", "2 -> [    ]"],
            ["3. L'assiette...", "C. à gauche de l'assiette", "3 -> [    ]"],
            ["4. Le verre à eau...", "D. au-dessus de l'assiette ou sur le côté", "4 -> [    ]"],
            ["5. La serviette...", "E. sur l'assiette ou à gauche de la fourchette", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : LA CONVIVIALITÉ À TABLE",
        "cloze_tip_text": "Complétez les dialogues sans aide mémoire pour restituer la politesse française à table.",
        "dialogues": [
            {
                "title": "Situation A — Préparation du dîner en famille (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La mère : Thomas, s'il te plaît, viens ___________________________ [to set / lay] la table !",
                    "• Le fils : D'accord ! Combien d'___________________________ [plates / guests] est-ce que je dois disposer ?",
                    "• La mère : Quatre, avec les verres à eau et les ___________________________ [napkins]."
                ]
            },
            {
                "title": "Situation B — Au cours du dîner (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• L'invité : Ce plat de bœuf est absolument ___________________________ [delicious / excellent] !",
                    "• L'hôte : Merci beaucoup ! Tu veux bien me ___________________________ [pass] la carafe d'eau ?",
                    "• L'invité : Bien sûr, la voilà. Et reprends un peu de ___________________________ [bread] frais.",
                    "• L'hôte : Avec plaisir. Tu veux encore un peu de ___________________________ [cheese / salad] ?"
                ]
            },
            {
                "title": "Situation C — Fin du repas et débarrassage (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le père : Tout le monde a terminé ? On va ___________________________ [to clear] la table.",
                    "• La fille : Je m'occupe de mettre les couverts dans le ___________________________ [dishwasher].",
                    "• Le père : Merci, et apporte le ___________________________ [dessert] et les petites cuillères."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. Could you please pass me the bread and the butter?", "-> __________________________________________________________________________________"],
            ["2. Children, please help to clear the table after dinner.", "-> __________________________________________________________________________________"],
            ["3. Enjoy your meal! (Formal / traditional French blessing)", "-> __________________________________________________________________________________"],
            ["4. Place the knife to the right and the fork to the left.", "-> __________________________________________________________________________________"],
            ["5. In France, dinner is usually served around 8:00 PM.", "-> __________________________________________________________________________________"],
            ["6. We need four soup plates and four glasses.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La fourchette  •  Le couteau  •  La cuillère  •  L'oreiller", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le petit-déjeuner  •  Le déjeuner  •  Le dîner  •  L'autoroute", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. L'assiette  •  Le verre  •  La serviette  •  Le pneu", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Mettre la table  •  Débarrasser la table  •  Passer le sel  •  Conduire un camion", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le couteau -> '-eau' son [o] [koo-toh] | 2. la cuillère -> liquide [jɛʁ] [kwee-yair] | 3. l'assiette -> son [ɛt] sans accent [ah-syet] | 4. le déjeuner -> 'r' muet [day-zhuh-nay] | 5. la fourchette -> son net [foor-shet] | 6. le goûter -> circonflexe sur 'u' [goo-tay].\nExercice 1.2 — Orthographe [3 pts] :\na) le déjeuner | b) le dîner | c) le goûter | d) une cuillère à soupe | e) une assiette creuse | f) débarrasser la table.\nExercice 1.3 — Liaisons [3 pts] :\n1. une assiette [n] | 2. des assiettes [z] | 3. un élégant couvert [n] | 4. mettre la table (pas de liaison) | 5. deux enfants [z] | 6. un grand appétit [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la fourchette (F) | 2. le couteau (M) | 3. la cuillère (F) | 4. le plat (M) | 5. le bol (M) | 6. la tasse (F) | 7. l'assiette (F) | 8. le verre (M) | 9. la serviette (F) | 10. la nappe (F) | 11. la carafe (F) | 12. le saladier (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. LA grande fourchette (fourchette est féminin) | 2. Ce couteau est très TRANCHANT (couteau est masculin) | 3. UNE serviette propre (serviette est féminin) | 4. UN NOUVEAU plat (plat est masculin).",
        "tier3_text": "Exercice 3.1 — Chunks de Repas [5 pts] :\n1. à | 2. appétit | 3. passer | 4. débarrasser | 5. heures.\nExercice 3.2 — Paires Emplacements [5 pts] :\n1 -> C (Fourchette à gauche) | 2 -> B (Couteau à droite, lame vers l'intérieur) | 3 -> A (Assiette au centre) | 4 -> D (Verre au-dessus de l'assiette) | 5 -> E (Serviette sur l'assiette ou à gauche).",
        "tier4_text": "Situation A (3 pts) : mettre | assiettes | serviettes.\nSituation B (4 pts) : délicieux (ou succulent) | passer | pain | fromage.\nSituation C (3 pts) : débarrasser | lave-vaisselle | dessert.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Pourrais-tu me passer le pain et le beurre, s'il te plaît ? | 2. Les enfants, s'il vous plaît aidez à débarrasser la table après le dîner. | 3. Bon appétit ! | 4. Placez le couteau à droite et la fourchette à gauche. | 5. En France, le dîner est généralement servi vers 20 heures. | 6. Nous avons besoin de quatre assiettes creuses et de quatre verres.\nExercice 5.2 — Intrus [4 pts] :\n1. L'oreiller (literie de chambre, les autres sont des couverts de table) | 2. L'autoroute (infrastructure routière, les autres sont les repas de la journée) | 3. Le pneu (pièce de véhicule, les autres sont des éléments du couvert de table) | 4. Conduire un camion (action de conduite automobile, les autres sont des actions associées aux repas).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 24",
        "anchors_text": "1. L'art de la table à la française : En France, la fourchette se place toujours à gauche de l'assiette et le couteau à droite, la lame tournée vers l'assiette (signe de paix). Les verres sont disposés en haut à droite (verre à eau le plus grand, puis verre à vin).\n2. 'Le goûter' ou 'quatre-heures' : Institution sociale en France vers 16h30-17h00 pour les enfants à la sortie de l'école (pain au chocolat, fruits, tartines), souvent partagé aussi par les adultes !\n3. 'Bon appétit' : Formule incontournable que les convives s'échangent avant de porter la première bouchée à la bouche."
    }
}

# CHAPTER 25: Le restaurant et la carte
batch3["25"] = {
    "ch_num": 25,
    "title_fr": "Le restaurant et la carte",
    "title_en": "Dining Out, Menus & Ordering at the Bistro",
    "word_count": 45,
    "traps": [
        "False cognate: 'LA CARTE' (the complete menu list) vs 'LE MENU' (a fixed-price multi-course combo meal, e.g., 'Menu du jour' at 18 €).",
        "Ordering politeness: Never say 'Je veux' (rude). Always use conditional 'Je voudrais...', 'J'aimerais...', or 'Je vais prendre...'.",
        "The bill & service: 'L'addition, s'il vous plaît !' (The check). 'Le pourboire' (tip) is customary but optional because service (15%) is included by French law ('service compris')."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LE DOUBLE 'D' D'ADDITION ET LES SUFFIXES EN -TION",
        "phonetic_tip_text": "'L'addition' [lah-dee-syohn] combine une consonne 'd' ferme et le suffixe nasal [sjɔ̃]. 'Le pourboire' [poor-bwahr] s'articule avec deux diphtongues fluides [uʁ] et [waʁ].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique du Restaurant [4 pts]",
        "ex1_headers": ["Terme de restauration", "Genre", "Spécificité phonétique", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. l'addition (f.)", "Féminin", "Double 'dd', suffixe '-tion'", "[ lah-dee-syohn ]", "Son [sjɔ̃] nasal pur"],
            ["2. le pourboire (m.)", "Masculin", "Graphèmes 'ou' et 'oi'", "[ poor-bwahr ]", "Double consonne 'r' sonore"],
            ["3. le plat du jour (m.)", "Masculin", "Consonne 't' muette dans plat", "[ plah dyoo zhoor ]", "'t' muet, [y] net dans 'du'"],
            ["4. le serveur (m.)", "Masculin", "Suffixe '-eur'", "[ sair-vuhr ]", "Son [œʁ] ouvert"],
            ["5. la serveuse (f.)", "Féminin", "Suffixe '-euse'", "[ sair-vuhz ]", "'s' sonne [z], [ø] fermé"],
            ["6. la brasserie (f.)", "Féminin", "Double 'ss' sonore", "[ brah-sree ]", "E caduc muet, son [s]"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) l'addition s'il vous plait -> ________________________",
            "b) une reservation pour deux -> ________________________",
            "c) un apero en terrasse -> ________________________",
            "d) une entree chaude -> ________________________",
            "e) le service est compris -> ________________________",
            "f) une carafe d'eau fraiche -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons au Restaurant [3 pts]",
        "ex3_items": [
            "1. un excellent repas    -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison",
            "2. vous avez réservé     -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un autre verre        -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. l'addition s'il vous plaît -> [  ] Pas de liaison         [  ] Liaison obligatoire",
            "5. deux entrées          -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un grand appétit      -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES ÉLÉMENTS DE LA CARTE ET DU SERVICE",
        "gender_rule_text": "Structure du repas : l'entrée (f.), la formule (f.), l'addition (f.), la note (f.), la carte (f.), mais le menu (m.), le plat (m.), le plat du jour (m.), le dessert (m.), le café (m.), le pourboire (m.).",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Carte & Restauration [6 pts]",
        "ex1_headers": ["Terme avec article", "Genre (M/F)", "Terme avec article", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ addition (f.)", "[   ] M   [   ] F", "7. _______ pourboire (m.)", "[   ] M   [   ] F"],
            ["2. _______ menu (m.)", "[   ] M   [   ] F", "8. _______ carte (f.)", "[   ] M   [   ] F"],
            ["3. _______ entrée (f.)", "[   ] M   [   ] F", "9. _______ réservation (f.)", "[   ] M   [   ] F"],
            ["4. _______ plat (m.)", "[   ] M   [   ] F", "10. _______ serveur (m.)", "[   ] M   [   ] F"],
            ["5. _______ dessert (m.)", "[   ] M   [   ] F", "11. _______ table (f.)", "[   ] M   [   ] F"],
            ["6. _______ formule (f.)", "[   ] M   [   ] F", "12. _______ bistrot (m.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Garçon, apportez-moi le addition détaillée dès que possible, s'il vous plaît.\n   Correction : _____________________________________________________________________________",
            "2. Pour commencer, je vais choisir une entrée chaud : la soupe à l'oignon.\n   Correction : _____________________________________________________________________________",
            "3. Ce menu à 25 euros propose une délicieuse plat de saumon grillé.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons laissé un petite pourboire de deux euros sur la table.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS DE COMMANDE : LES FORMULES ET LE SERVICE",
        "colloc_tip_text": "Formules rituelles : 'Une table pour deux personnes', 'Quel est le plat du jour ?', 'Je voudrais / Je vais prendre...', 'À quelle cuisson ?', 'L'addition, s'il vous plaît !', 'Le service est compris'.",
        "ex1_title": "Exercice 3.1 — Formules Communicatives de Commande [5 pts]",
        "ex1_sentences": [
            "1. En arrivant au restaurant, le client demande : 'Bonjour, avez-vous une table _________ (pour / à) deux personnes ?'",
            "2. Pour commander poliment, on dit : 'Je _________ (voudrais / veux) le filet de bar et une salade.'",
            "3. En plat principal, je vais _________ (prendre / faire) le magret de canard au miel.",
            "4. À la fin du repas, le client demande au serveur : 'L'_________ (addition / entrée), s'il vous plaît !'",
            "5. En France, la note inclut légalement le service : 'Le service est _________ (compris / payé).'"
        ],
        "ex2_title": "Exercice 3.2 — Paires Étape du Repas-Contenu [5 pts]",
        "ex2_headers": ["Étape du menu", "Plat représentatif", "Code association"],
        "ex2_rows": [
            ["1. L'apéritif...", "A. Tarte tatin tiède avec crème fraîche", "1 -> [    ]"],
            ["2. L'entrée...", "B. Coupe de champagne ou kir cassis", "2 -> [    ]"],
            ["3. Le plat de résistance...", "C. Assiette de charcuterie ou soupe à l'oignon", "3 -> [    ]"],
            ["4. Le fromage...", "D. Pavé de saumon ou entrecôte-frites", "4 -> [    ]"],
            ["5. Le dessert...", "E. Chèvre cendré et comté affiné", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : DÎNER AU BISTROT PARISIEN",
        "cloze_tip_text": "Complétez les interactions au restaurant en restituant le registre de politesse adapté.",
        "dialogues": [
            {
                "title": "Situation A — Prise de commande (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le serveur : Vous avez ___________________________ [chosen / made up your mind] ?",
                    "• La cliente : Oui, je vais ___________________________ [take / have] la formule entrée plus plat.",
                    "• Le serveur : Très bien. Et quelle ___________________________ [cooking level] pour la viande : saignant ou à point ?"
                ]
            },
            {
                "title": "Situation B — Le plat du jour et les boissons (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le client : Excusez-moi, quel est le plat du ___________________________ [day] aujourd'hui ?",
                    "• Le serveur : C'est une blanquette de veau à l'ancienne avec du riz.",
                    "• Le client : Parfait, apportez-moi cela, avec une ___________________________ [carafe] d'eau.",
                    "• Le serveur : Et désirez-vous un ___________________________ [glass] de vin pour accompagner ?"
                ]
            },
            {
                "title": "Situation C — Demande de la note (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le client : S'il vous plaît ! Pourrions-nous avoir l'___________________________ [bill / check] ?",
                    "• Le serveur : Bien sûr. Vous réglez ensemble ou ___________________________ [separately] ?",
                    "• Le client : Ensemble, par carte ___________________________ [credit card]."
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. A table for two people on the terrace, please.", "-> __________________________________________________________________________________"],
            ["2. I would like the menu of the day with a glass of red wine.", "-> __________________________________________________________________________________"],
            ["3. What is the daily special today?", "-> __________________________________________________________________________________"],
            ["4. The bill, please! Is service included?", "-> __________________________________________________________________________________"],
            ["5. I will take the onion soup as a starter.", "-> __________________________________________________________________________________"],
            ["6. We left a three-euro tip for the waitress.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. L'entrée  •  Le plat  •  Le dessert  •  Le feu rouge", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. Le serveur  •  Le chef  •  Le maître d'hôtel  •  Le conducteur de train", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. L'addition  •  La note  •  Le pourboire  •  La valise", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La carte  •  Le menu  •  La formule  •  La bicyclette", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. l'addition -> suffixe [sjɔ̃] [lah-dee-syohn] | 2. le pourboire -> [poor-bwahr] | 3. le plat du jour -> 't' muet [plah dyoo zhoor] | 4. le serveur -> [sair-vuhr] | 5. la serveuse -> 's' sonne [z] [sair-vuhz] | 6. la brasserie -> e caduc muet [brah-sree].\nExercice 1.2 — Orthographe [3 pts] :\na) l'addition s'il vous plaît | b) une réservation pour deux | c) un apéro en terrasse | d) une entrée chaude | e) le service est compris | f) une carafe d'eau fraîche.\nExercice 1.3 — Liaisons [3 pts] :\n1. un excellent repas [t] | 2. vous avez réservé [z] | 3. un autre verre [n] | 4. l'addition s'il vous plaît (pas de liaison) | 5. deux entrées [z] | 6. un grand appétit [t].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. l'addition (F) | 2. le menu (M) | 3. l'entrée (F) | 4. le plat (M) | 5. le dessert (M) | 6. la formule (F) | 7. le pourboire (M) | 8. la carte (F) | 9. la réservation (F) | 10. le serveur (M) | 11. la table (F) | 12. le bistrot (M).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. L'addition (addition est féminin : 'une addition') | 2. Une entrée CHAUDE (accord féminin avec entrée) | 3. UN délicieux plat (plat est masculin) | 4. UN PETIT pourboire (pourboire est masculin).",
        "tier3_text": "Exercice 3.1 — Formules Commande [5 pts] :\n1. pour | 2. voudrais | 3. prendre | 4. addition | 5. compris.\nExercice 3.2 — Paires Étapes du Repas [5 pts] :\n1 -> B (Apéritif : champagne ou kir) | 2 -> C (Entrée : charcuterie ou soupe) | 3 -> D (Plat : saumon ou entrecôte) | 4 -> E (Fromage : chèvre et comté) | 5 -> A (Dessert : tarte tatin).",
        "tier4_text": "Situation A (3 pts) : choisi | prendre | cuisson.\nSituation B (4 pts) : jour | carafe | verre.\nSituation C (3 pts) : addition | séparément | bancaire.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Une table pour deux personnes en terrasse, s'il vous plaît. | 2. Je voudrais le menu du jour avec un verre de vin rouge. | 3. Quel est le plat du jour aujourd'hui ? | 4. L'addition, s'il vous plaît ! Est-ce que le service est compris ? | 5. Je vais prendre la soupe à l'oignon en entrée. | 6. Nous avons laissé un pourboire de trois euros pour la serveuse.\nExercice 5.2 — Intrus [4 pts] :\n1. Le feu rouge (signalisation routière, les autres sont des services d'un repas au restaurant) | 2. Le conducteur de train (métier des transports ferroviaires, les autres travaillent en restauration) | 3. La valise (bagage de voyage, les autres sont des termes de paiement de restaurant) | 4. La bicyclette (moyen de transport, les autres désignent les listes de plats proposés au restaurant).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 25",
        "anchors_text": "1. Le faux-ami 'Menu' vs 'Carte' : En France, 'la carte' est la liste complète de tous les plats avec leurs prix individuels. 'Le menu' désigne une formule à prix fixe combinant plusieurs plats (ex : Menu Entrée + Plat à 22 €).\n2. Le pourboire en France : Le service est légalement inclus à hauteur de 15% dans l'addition ('service compris'). Laisser un pourboire de 1 à 3 euros en pièces sur la table est un geste d'appréciation pour un bon accueil, mais jamais obligatoire.\n3. Politesse absolue : Ne dites jamais 'Garçon !' pour appeler un serveur (archaïque et condescendant). Levez discrètement la main et dites simplement : 'S'il vous plaît !' ou 'Monsieur / Madame !'"
    }
}

# CHAPTER 26: Les courses et les commerces
batch3["26"] = {
    "ch_num": 26,
    "title_fr": "Les courses et les commerces",
    "title_en": "Shops, Supermarkets, Errands & Shopping",
    "word_count": 45,
    "traps": [
        "False cognate: 'LA LIBRAIRIE' is a BOOKSHOP (where you BUY books). A public lending library is 'LA BIBLIOTHÈQUE'!",
        "Preposition CHEZ vs À LA: 'Je vais CHEZ le boulanger / CHEZ le boucher' (person/professional) vs 'Je vais À LA boulangerie / À LA boucherie' (shop/place).",
        "Shopkeeper pairs: le boulanger / la boulangère, le boucher / la bouchère, le pharmacien / la pharmacienne, l'épicier / l'épicière, le fleuriste (invariable)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LES ACCENTS GRAVES DES FÉMININS COMMERÇANTS (-ÈRE)",
        "phonetic_tip_text": "Le passage du masculin au féminin transforme la prononciation : 'le boucher' [boo-shay] (son [e] fermé, 'r' muet) devient 'la bouchère' [boo-shair] (son [ɛʁ] ouvert avec 'r' sonore).",
        "ex1_title": "Exercice 1.1 — Audit Phonétique des Métiers du Commerce [4 pts]",
        "ex1_headers": ["Commerçant", "Genre", "Terminaison", "Prononciation IPA", "Phénomène sonore"],
        "ex1_rows": [
            ["1. le boucher (m.)", "Masculin", "Suffixe '-er'", "[ boo-shay ]", "'r' muet, son [e] pur"],
            ["2. la bouchère (f.)", "Féminin", "Suffixe '-ère'", "[ boo-shair ]", "Accent grave, 'r' sonore [ɛʁ]"],
            ["3. le pharmacien (m.)", "Masculin", "Suffixe '-ien'", "[ fahr-mah-syanh ]", "Nasale [ɛ̃] pure"],
            ["4. la pharmacienne (f.)", "Féminin", "Suffixe '-ienne'", "[ fahr-mah-syen ]", "Dénasalisation [ɛn] claire"],
            ["5. la librairie (f.)", "Féminin", "Suffixe '-ie'", "[ lee-bray-ree ]", "'r' sonore, zéro consonne muette"],
            ["6. le supermarché (m.)", "Masculin", "Terminaison '-é'", "[ syoo-pair-mahr-shay ]", "Son [y] puis deux [e] fermés"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) faire les courses au supermarche -> ________________________",
            "b) une epicerie de quartier -> ________________________",
            "c) un reglement par carte bancaire -> ________________________",
            "d) une boulangere souriante -> ________________________",
            "e) la caisse du magasin -> ________________________",
            "f) un ticket de caisse -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons Commerciales [3 pts]",
        "ex3_items": [
            "1. un épicier aimable      -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "2. chez un commerçant      -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. aux caisses automatiques -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "4. un grand magasin        -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison",
            "5. faire des courses       -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "6. un euro cinquante       -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES COMMERCES ET ÉLÉMENTS DE VENTE",
        "gender_rule_text": "Les commerces de proximité en -ie sont TOUS féminins : la boulangerie, la boucherie, la poissonnerie, la pharmacie, la librairie, l'épicerie, la pâtisserie. Masculins : le supermarché, le magasin, le centre commercial, le kiosque, le marché.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Commerces & Rayons [6 pts]",
        "ex1_headers": ["Lieu de commerce", "Genre (M/F)", "Lieu de commerce", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ boulangerie (f.)", "[   ] M   [   ] F", "7. _______ supermarché (m.)", "[   ] M   [   ] F"],
            ["2. _______ boucherie (f.)", "[   ] M   [   ] F", "8. _______ magasin (m.)", "[   ] M   [   ] F"],
            ["3. _______ librairie (f.)", "[   ] M   [   ] F", "9. _______ chariot / caddie (m.)", "[   ] M   [   ] F"],
            ["4. _______ pharmacie (f.)", "[   ] M   [   ] F", "10. _______ caisse (f.)", "[   ] M   [   ] F"],
            ["5. _______ épicerie (f.)", "[   ] M   [   ] F", "11. _______ ticket de caisse (m.)", "[   ] M   [   ] F"],
            ["6. _______ fleuriste (m./f.)", "[   ] M   [   ] F", "12. _______ carte de fidélité (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Je vais au petite épicerie du coin pour acheter du sucre et des œufs.\n   Correction : _____________________________________________________________________________",
            "2. La caissier m'a donné le ticket de caisse et la monnaie en pièces.\n   Correction : _____________________________________________________________________________",
            "3. Mon père a acheté ce roman policier dans un nouveau librairie du centre.\n   Correction : _____________________________________________________________________________",
            "4. Nous avons rempli une grand chariot au supermarché ce samedi matin.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS MARCHANDES : CHEZ VS À & PAIEMENT",
        "colloc_tip_text": "Règle prépositionnelle majeure : CHEZ s'emploie avec les personnes (chez le boucher, chez le médecin), À s'emploie avec les lieux inanimés (à la boucherie, au supermarché). Expressions : 'faire les courses', 'passer à la caisse', 'payer par carte / en espèces', 'garder le ticket'.",
        "ex1_title": "Exercice 3.1 — Prépositions Commerciales & Moyens de Paiement [5 pts]",
        "ex1_sentences": [
            "1. Le samedi matin, je vais acheter les croissants _________ (chez / à la) le boulanger.",
            "2. Elle a oublié ses médicaments, elle doit passer d'urgence _________ (à la / chez) pharmacie.",
            "3. En arrivant au supermarché, le client prend un _________ (chariot / billet) pour mettre ses achats.",
            "4. À la caisse, vous pouvez payer par carte bancaire ou _________ (en / par) espèces.",
            "5. La caissière demande poliment : 'Désirez-vous votre _________ (ticket / passeport) de caisse ?'"
        ],
        "ex2_title": "Exercice 3.2 — Paires Produit-Commerce Dédié [5 pts]",
        "ex2_headers": ["Produit recherché", "Commerce spécialisé", "Code association"],
        "ex2_rows": [
            ["1. Des timbres et un journal...", "A. à la pharmacie", "1 -> [    ]"],
            ["2. Des médicaments et du désinfectant...", "B. à la librairie", "2 -> [    ]"],
            ["3. Un bouquet de roses fraîches...", "C. au bureau de tabac / presse", "3 -> [    ]"],
            ["4. Un beau roman et une bande dessinée...", "D. chez le fleuriste", "4 -> [    ]"],
            ["5. Un gigot d'agneau et des saucisses...", "E. à la boucherie artisanale", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : SITUATIONS D'ACHAT DE QUARTIER",
        "cloze_tip_text": "Complétez les dialogues d'emplettes en mobilisant le lexique des commerces sans aide.",
        "dialogues": [
            {
                "title": "Situation A — À la caisse du supermarché (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La caissière : Bonjour Madame. Avez-vous notre carte de ___________________________ [loyalty] ?",
                    "• La cliente : Non, je ne l'ai pas sur moi. Ça fait combien au ___________________________ [total] ?",
                    "• La caissière : 38 euros et 20 centimes. Vous réglez par ___________________________ [card / cash] ?"
                ]
            },
            {
                "title": "Situation B — À la librairie du centre-ville (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• Le client : Bonjour, je cherche le dernier ___________________________ [novel / book] de cet auteur français.",
                    "• Le libraire : Il se trouve au rayon littérature, juste à côté des ___________________________ [comics / BD].",
                    "• Le client : Merci beaucoup ! Est-ce que vous vendez aussi des ___________________________ [dictionaries] ?",
                    "• Le libraire : Oui, au fond près de la section des ___________________________ [magazines / guides]."
                ]
            },
            {
                "title": "Situation C — À la boulangerie le matin (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• La boulangère : Bonjour Monsieur, avec ceci ?",
                    "• Le client : Deux baguettes tradition et un croissant au ___________________________ [butter], s'il vous plaît.",
                    "• La boulangère : Voilà. Cela fera trois euros cinquante. Vous avez de la ___________________________ [small change / coins] ?"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. I am going to the bakery to buy two baguettes.", "-> __________________________________________________________________________________"],
            ["2. She buys her books at the neighborhood bookshop (not library).", "-> __________________________________________________________________________________"],
            ["3. Do you accept payments by contactless credit card?", "-> __________________________________________________________________________________"],
            ["4. We do our grocery shopping at the supermarket every Saturday.", "-> __________________________________________________________________________________"],
            ["5. Here is your receipt and your change, madam.", "-> __________________________________________________________________________________"],
            ["6. He went to the pharmacy to buy medicine for his cough.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. La boulangerie  •  La boucherie  •  La pharmacie  •  L'avion", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La caisse  •  Le chariot  •  Le ticket de caisse  •  La montagne", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. Payer en espèces  •  Payer par carte  •  Payer sans contact  •  Dormir à l'hôtel", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. La librairie  •  Le boulanger  •  Le boucher  •  Le fleuriste", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le boucher -> [boo-shay] 'r' muet | 2. la bouchère -> [boo-shair] 'r' sonore [ɛʁ] | 3. le pharmacien -> [fahr-mah-syanh] nasale | 4. la pharmacienne -> [fahr-mah-syen] dénasalisée | 5. la librairie -> [lee-bray-ree] | 6. le supermarché -> [syoo-pair-mahr-shay].\nExercice 1.2 — Orthographe [3 pts] :\na) supermarché | b) une épicerie | c) un règlement | d) une boulangère | e) la caisse | f) un ticket de caisse.\nExercice 1.3 — Liaisons [3 pts] :\n1. un épicier [n] | 2. chez un commerçant [z] | 3. aux caisses [z] | 4. un grand magasin [t] | 5. faire des courses (pas de liaison) | 6. un euro [n].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. la boulangerie (F) | 2. la boucherie (F) | 3. la librairie (F) | 4. la pharmacie (F) | 5. l'épicerie (F) | 6. le/la fleuriste (M/F) | 7. le supermarché (M) | 8. le magasin (M) | 9. le chariot (M) | 10. la caisse (F) | 11. le ticket (M) | 12. la carte (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. À LA petite épicerie (épicerie est féminin) | 2. LE caissier (ou LA caissière) | 3. UNE nouvelle librairie (librairie est féminin) | 4. UN GRAND chariot (chariot est masculin).",
        "tier3_text": "Exercice 3.1 — Prépositions Commerciales [5 pts] :\n1. chez | 2. à la | 3. chariot | 4. en | 5. ticket.\nExercice 3.2 — Paires Commerces [5 pts] :\n1 -> C (Timbres et journaux au bureau de tabac/presse) | 2 -> A (Médicaments à la pharmacie) | 3 -> D (Roses chez le fleuriste) | 4 -> B (Romans et BD à la librairie) | 5 -> E (Gigot d'agneau à la boucherie).",
        "tier4_text": "Situation A (3 pts) : fidélité | total | carte (ou espèces).\nSituation B (4 pts) : roman (ou livre) | bandes dessinées (ou BD) | dictionnaires | revues (ou guides).\nSituation C (3 pts) : beurre | monnaie.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Je vais à la boulangerie pour acheter deux baguettes. | 2. Elle achète ses livres à la librairie du quartier. | 3. Acceptez-vous les paiements par carte bancaire sans contact ? | 4. Nous faisons nos courses au supermarché tous les samedis. | 5. Voici votre ticket de caisse et votre monnaie, madame. | 6. Il est allé à la pharmacie pour acheter des médicaments pour sa toux.\nExercice 5.2 — Intrus [4 pts] :\n1. L'avion (moyen de transport aérien, les autres sont des commerces de proximité) | 2. La montagne (relief naturel, les autres sont des éléments d'achat au supermarché) | 3. Dormir à l'hôtel (action d'hébergement, les autres sont des modes de paiement marchand) | 4. La librairie (lieu de vente de livres, les trois autres sont des personnes / commerçants).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 26",
        "anchors_text": "1. Le piège absolu 'Librairie' vs 'Bibliothèque' : 'La librairie' est un commerce privé où l'on ACHÈTE des livres. 'La bibliothèque' est un bâtiment public municipal ou universitaire où l'on EMPRUNTE des livres gratuitement. Ne jamais confondre !\n2. 'Faire les courses' vs 'faire les magasins' / 'du shopping' : 'Faire les courses' désigne l'achat quotidien de nourriture et produits ménagers au supermarché ou au marché. 'Faire les magasins' désigne l'achat de vêtements, loisirs ou décoration.\n3. Règle CHEZ vs À : On va CHEZ une personne (chez le boucher, chez Pierre), mais À un lieu (à la boucherie, au supermarché)."
    }
}

# CHAPTER 27: Les vêtements, chaussures et accessoires
batch3["27"] = {
    "ch_num": 27,
    "title_fr": "Les vêtements, chaussures et accessoires",
    "title_en": "Clothing, Shoes, Colors & Dressing Style",
    "word_count": 46,
    "traps": [
        "Color agreement traps: Invariable color adjectives derived from nouns (marron, orange) NEVER take an 's' or 'e'! Compound colors are also invariable: 'des chemises bleu clair'.",
        "Size terminology: 'La taille' is clothing size (38, 40, S, M, L), but 'la pointure' is strictly SHOE SIZE (41, 42)!",
        "Gender traps: 'le pantalon' (m. singular in French, whereas 'pants' is plural in English!), 'le manteau' (m.), 'le costume' (m.), 'le chapeau' (m.), but 'la chemise' (f.), 'la robe' (f.), 'la veste' (f.), 'l'écharpe' (f.)."
    ],
    "target_time": "30–35 min",
    "total_marks": 50,
    "passing_mark": "80% (40/50)",
    "tier1": {
        "phonetic_tip_title": "LES GRAPHÈMES COMPOSITES -EAU ET LE 'S' DE CHAUSSURES",
        "phonetic_tip_text": "'Le manteau' et 'le chapeau' se terminent par '-eau' son [o] pur (pluriel en -x muet). 'Les chaussures' comportent un double 'ss' pour le son [s] pur et une terminaison '-ures' [yʁ].",
        "ex1_title": "Exercice 1.1 — Audit Phonétique de la Garde-Robe [4 pts]",
        "ex1_headers": ["Vêtement / Accessoire", "Genre", "Graphème clé", "Prononciation IPA", "Piège sonore"],
        "ex1_rows": [
            ["1. le manteau (m.)", "Masculin", "Graphème '-eau'", "[ mahn-toh ]", "Son [o] pur, pluriel en -x muet"],
            ["2. les chaussures (f. pl.)", "Féminin pl.", "Double 'ss' sonore", "[ shoh-soor ]", "Son [s] franc et consonne [yʁ]"],
            ["3. le pantalon (m.)", "Masculin", "Double nasale '-an-' '-on'", "[ pahn-tah-lohn ]", "Deux nasales [ɑ̃] et [ɔ̃] distinctes"],
            ["4. la chemise (f.)", "Féminin", "'s' intervocalique sonore", "[ shuh-meez ]", "Son [z] doux, 'e' final muet"],
            ["5. l'écharpe (f.)", "Féminin", "Consonne 'p' muette en finale", "[ ay-shahrp ]", "Accent aigu [e], 'p' sonore bref"],
            ["6. le pull (chandail) (m.)", "Masculin", "Voyelle 'u'", "[ pool ]", "Son [u] ou [yl] selon usage"]
        ],
        "ex2_title": "Exercice 1.2 — Rectification Orthographique & Accents [3 pts]",
        "ex2_items": [
            "a) un vetement d'hiver -> ________________________",
            "b) une echarpe en laine -> ________________________",
            "c) essayer dans la cabine d'essayage -> ________________________",
            "d) une jupe plisse -> ________________________",
            "e) des chaussures marron -> ________________________",
            "f) un impermeable pour la pluie -> ________________________"
        ],
        "ex3_title": "Exercice 1.3 — Détection des Liaisons et Accords [3 pts]",
        "ex3_items": [
            "1. un élégant costume      -> [  ] Liaison [t] obligatoire    [  ] Pas de liaison",
            "2. des habits d'été        -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "3. un imperméable noir     -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison",
            "4. porter un pantalon      -> [  ] Pas de liaison             [  ] Liaison obligatoire",
            "5. deux écharpes           -> [  ] Liaison [z] obligatoire    [  ] Pas de liaison",
            "6. un anorak chaud         -> [  ] Liaison [n] obligatoire    [  ] Pas de liaison"
        ]
    },
    "tier2": {
        "gender_rule_title": "LE GENRE DES VÊTEMENTS ET PIÈGES DU SINGULIER",
        "gender_rule_text": "Attention : En français, 'le pantalon' et 'le jean' s'emploient au SINGULIER (alors qu'ils sont pluriels en anglais). Masculins : le manteau, le pull, le costume, le t-shirt, le gilet, le chemisier. Féminins : la robe, la jupe, la veste, la chemise, la cravate, la ceinture, l'écharpe.",
        "ex1_title": "Exercice 2.1 — Matrice de Genre : Vêtements & Accessoires [6 pts]",
        "ex1_headers": ["Pièce d'habillement", "Genre (M/F)", "Pièce d'habillement", "Genre (M/F)"],
        "ex1_rows": [
            ["1. _______ pantalon (m.)", "[   ] M   [   ] F", "7. _______ manteau (m.)", "[   ] M   [   ] F"],
            ["2. _______ robe (f.)", "[   ] M   [   ] F", "8. _______ veste (f.)", "[   ] M   [   ] F"],
            ["3. _______ chemise (f.)", "[   ] M   [   ] F", "9. _______ cravate (f.)", "[   ] M   [   ] F"],
            ["4. _______ pull (m.)", "[   ] M   [   ] F", "10. _______ ceinture (f.)", "[   ] M   [   ] F"],
            ["5. _______ jupe (f.)", "[   ] M   [   ] F", "11. _______ chapeau (m.)", "[   ] M   [   ] F"],
            ["6. _______ costume (m.)", "[   ] M   [   ] F", "12. _______ écharpe (f.)", "[   ] M   [   ] F"]
        ],
        "ex2_title": "Exercice 2.2 — Détective de Genre & Accords : Repérez l'Erreur [4 pts]",
        "ex2_sentences": [
            "1. Elle porte un belle robe blanche en lin pour la cérémonie de mariage.\n   Correction : _____________________________________________________________________________",
            "2. J'ai acheté des chaussures marrons et des chaussettes noir.\n   Correction : _____________________________________________________________________________",
            "3. Il a mis une grand manteau en laine pour affronter le froid glacial.\n   Correction : _____________________________________________________________________________",
            "4. Cette chemise en coton est très élégant avec une cravate bleue.\n   Correction : _____________________________________________________________________________"
        ]
    },
    "tier3": {
        "colloc_tip_title": "COLLOCATIONS EN BOUTIQUE : METTRE, ESSAYER ET TAILLE",
        "colloc_tip_text": "Verbes d'action : 'mettre un vêtement' (to put on), 'porter une veste' (to wear), 'essayer dans la cabine d'essayage' (to try on). Distinguer : 'Quelle est votre taille ?' (vêtements) vs 'Quelle est votre pointure ?' (chaussures).",
        "ex1_title": "Exercice 3.1 — Verbes d'Habillement & Formules de Boutique [5 pts]",
        "ex1_sentences": [
            "1. En hiver quand il neige, n'oublie pas de _________ (mettre / faire) ton gros manteau chaud.",
            "2. Puis-je _________ (essayer / porter) cette veste bleue dans la cabine, s'il vous plaît ?",
            "3. Pour les vêtements, la vendeuse demande : 'Quelle est votre _________ (taille / pointure) ? Du 38 ou du 40 ?'",
            "4. Pour les chaussures en cuir, on demande : 'Quelle est votre _________ (pointure / taille) ? Du 42 ?'",
            "5. Ce pantalon vous va très bien : il est parfaitement à votre _________ (taille / couleur) !"
        ],
        "ex2_title": "Exercice 3.2 — Paires Vêtement-Matière Authentique [5 pts]",
        "ex2_headers": ["Vêtement / Accessoire", "Matière ou contexte", "Code association"],
        "ex2_rows": [
            ["1. Un pull bien chaud...", "A. en soie naturelle italienne", "1 -> [    ]"],
            ["2. Une chemise légère...", "B. en pure laine mérinos", "2 -> [    ]"],
            ["3. Une cravate élégante...", "C. en cuir marron véritable", "3 -> [    ]"],
            ["4. Des chaussures de ville...", "D. en coton blanc respirant", "4 -> [    ]"],
            ["5. Un imperméable...", "E. pour se protéger de la pluie d'automne", "5 -> [    ]"]
        ]
    },
    "tier4": {
        "cloze_tip_title": "RÉCUPÉRATION ACTIVE : DANS UNE BOUTIQUE DE VÊTEMENTS",
        "cloze_tip_text": "Complétez les échanges entre vendeur et client sans banque de mots.",
        "dialogues": [
            {
                "title": "Situation A — Choix de vêtement et taille (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le vendeur : Bonjour Monsieur, je peux vous ___________________________ [help / renseigner] ?",
                    "• Le client : Oui, je cherche un ___________________________ [suit / jacket] pour un entretien d'embauche.",
                    "• Le vendeur : Très bien. Quelle est votre ___________________________ [size] de veste ?"
                ]
            },
            {
                "title": "Situation B — En cabine d'essayage (4 pts)",
                "points": "4 pts",
                "lines": [
                    "• La cliente : Où se trouvent les ___________________________ [fitting rooms], s'il vous plaît ?",
                    "• La vendeuse : Tout au fond à droite. Est-ce que la taille vous ___________________________ [fits / suits] ?",
                    "• La cliente : La jupe est un peu trop ___________________________ [tight / small]. Avez-vous la taille au-dessus ?",
                    "• La vendeuse : Oui, je vous apporte la taille 40 en ___________________________ [color] bleu marine."
                ]
            },
            {
                "title": "Situation C — Au rayon chaussures (3 pts)",
                "points": "3 pts",
                "lines": [
                    "• Le client : Bonjour, je voudrais essayer ces ___________________________ [shoes] en cuir marron.",
                    "• Le vendeur : Certainement. Quelle est votre ___________________________ [shoe size] ?",
                    "• Le client : Je fais du 42. Est-ce qu'elles sont ___________________________ [comfortable / on sale] ?"
                ]
            }
        ]
    },
    "tier5": {
        "ex1_title": "Exercice 5.1 — Traduction Inverse Ciblée (Anglais -> Français) [6 pts]",
        "ex1_prompts": [
            ["1. Can I try on this coat in the fitting room?", "-> __________________________________________________________________________________"],
            ["2. What is your shoe size? I take size 41.", "-> __________________________________________________________________________________"],
            ["3. This blue dress suits you very well.", "-> __________________________________________________________________________________"],
            ["4. He is wearing black trousers and a white shirt.", "-> __________________________________________________________________________________"],
            ["5. In winter, I wear a woolen scarf and a warm hat.", "-> __________________________________________________________________________________"],
            ["6. These leather shoes are very comfortable for walking.", "-> __________________________________________________________________________________"]
        ],
        "ex2_title": "Exercice 5.2 — L'Intrus avec Justification Sémantique [4 pts]",
        "ex2_intrus": [
            ["1. Le manteau  •  La veste  •  L'anorak  •  Le fromage", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["2. La robe  •  La jupe  •  Le pantalon  •  La gare", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["3. La pointure  •  La taille  •  La cabine  •  Le billet de train", "• Intrus : ________________________  |  Justification : ______________________________________________________"],
            ["4. Les chaussures  •  Les bottes  •  Les sandales  •  La cuillère", "• Intrus : ________________________  |  Justification : ______________________________________________________"]
        ]
    },
    "corrige": {
        "tier1_text": "Exercice 1.1 — Audit Phonétique [4 pts] :\n1. le manteau -> [mahn-toh] '-eau' [o] | 2. les chaussures -> [shoh-soor] 'ss' sonne [s] | 3. le pantalon -> deux nasales [pahn-tah-lohn] | 4. la chemise -> [shuh-meez] 's' sonne [z] | 5. l'écharpe -> [ay-shahrp] | 6. le pull -> [pool].\nExercice 1.2 — Orthographe [3 pts] :\na) un vêtement d'hiver | b) une écharpe en laine | c) la cabine d'essayage | d) une jupe plissée | e) des chaussures marron (invariable) | f) un imperméable.\nExercice 1.3 — Liaisons [3 pts] :\n1. un élégant costume [t] | 2. des habits [z] | 3. un imperméable [n] | 4. porter un pantalon (pas de liaison) | 5. deux écharpes [z] | 6. un anorak [n].",
        "tier2_text": "Exercice 2.1 — Matrice de Genre [6 pts] :\n1. le pantalon (M) | 2. la robe (F) | 3. la chemise (F) | 4. le pull (M) | 5. la jupe (F) | 6. le costume (M) | 7. le manteau (M) | 8. la veste (F) | 9. la cravate (F) | 10. la ceinture (F) | 11. le chapeau (M) | 12. l'écharpe (F).\nExercice 2.2 — Détective de Genre [4 pts] :\n1. UNE BELLE robe (robe est féminin) | 2. des chaussures MARRON (invariable, pas de s) et des chaussettes NOIRES (accord f. pl.) | 3. UN GRAND manteau (manteau est masculin) | 4. Cette chemise est très ÉLÉGANTE (accord f. avec chemise).",
        "tier3_text": "Exercice 3.1 — Verbes & Formules [5 pts] :\n1. mettre | 2. essayer | 3. taille | 4. pointure | 5. taille.\nExercice 3.2 — Paires Matières [5 pts] :\n1 -> B (Pull en pure laine) | 2 -> D (Chemise en coton) | 3 -> A (Cravate en soie) | 4 -> C (Chaussures en cuir) | 5 -> E (Imperméable contre la pluie).",
        "tier4_text": "Situation A (3 pts) : aider (ou renseigner) | costume (ou veste) | taille.\nSituation B (4 pts) : cabines d'essayage | va (ou convient) | serrée (ou petite) | couleur.\nSituation C (3 pts) : chaussures | pointure | confortables.",
        "tier5_text": "Exercice 5.1 — Traductions [6 pts] :\n1. Puis-je essayer ce manteau dans la cabine d'essayage ? | 2. Quelle est votre pointure ? Je fais du 41. | 3. Cette robe bleue vous va très bien. | 4. Il porte un pantalon noir et une chemise blanche. | 5. En hiver, je porte une écharpe en laine et un bonnet (ou chapeau) chaud. | 6. Ces chaussures en cuir sont très confortables pour marcher.\nExercice 5.2 — Intrus [4 pts] :\n1. Le fromage (produit laitier alimentaire, les autres sont des vêtements chauds d'extérieur) | 2. La gare (lieu de transport, les autres sont des vêtements du bas ou d'une pièce) | 3. Le billet de train (titre de transport, les autres sont des termes de boutique d'habillement) | 4. La cuillère (couvert de table, les autres sont des types de chaussures pour les pieds).",
        "anchors_title": "ANCRES DE RÉTENTION & PIÈGES COGNITIFS — CHAPITRE 27",
        "anchors_text": "1. Taille vs Pointure : Ne jamais les confondre ! 'La taille' s'applique aux vêtements (pantalon, chemise, robe : 36, 38, 40, S, M, L). 'La pointure' s'applique exclusivement aux chaussures (39, 41, 43).\n2. Les couleurs invariables : Les adjectifs de couleur issus de noms concrets (comme 'marron' du fruit du marronnier, et 'orange' du fruit de l'oranger) sont STRICTEMENT INVARIABLES : des robes marron, des vestes orange.\n3. 'Le pantalon' au singulier : Contrairement à l'anglais 'pants / trousers' qui est pluriel, le français utilise le singulier pour désigner l'objet : 'Mon pantalon est bleu'."
    }
}

with open("chapters_batch_3_part1.json", "w", encoding="utf-8") as f:
    json.dump(batch3, f, ensure_ascii=False, indent=2)

print("Part 1 of Batch 3 created successfully! Chapters:", list(batch3.keys()))
