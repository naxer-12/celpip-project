# build_full_vocab.py
# Comprehensive dataset generation for French Noun Gender Vocabulary A1-C2

import json

VOCAB_DATABASE = []

def add(id_num, french, gender, cefr, english, rule_cat, phonetic, mnemonic, ex_fr, ex_en, is_exc=False, exc_note=""):
    VOCAB_DATABASE.append({
        "id": id_num,
        "french": french,
        "gender": gender,
        "cefr": cefr,
        "english": english,
        "rule_category": rule_cat,
        "phonetic": phonetic,
        "mnemonic": mnemonic,
        "example_fr": ex_fr,
        "example_en": ex_en,
        "is_exception": is_exc,
        "exception_note": exc_note
    })

# ==========================================
# LEVEL A1: BEGINNER FOUNDATIONS & ESSENTIAL TRAPS
# ==========================================
add(1, "le fromage", "masculine", "A1", "cheese", "MASC: Ending -age", "[luh froh-MAHZH]",
    "Rule: -age is masculine! Think: fine French cheeses age in caves for men.",
    "J'adore manger du fromage avec une baguette.", "I love eating cheese with a baguette.")

add(2, "le voyage", "masculine", "A1", "trip / journey", "MASC: Ending -age", "[luh vwah-YAHZH]",
    "Rule: -age is masculine! Think of 'bon voyage' (bon is masculine).",
    "Nous préparons un beau voyage en France cet été.", "We are planning a wonderful trip to France this summer.")

add(3, "le message", "masculine", "A1", "message", "MASC: Ending -age", "[luh meh-SAHZH]",
    "Rule: -age is masculine! A message sent through the mail.",
    "J'ai reçu un message important ce matin.", "I received an important message this morning.")

add(4, "la plage", "feminine", "A1", "beach", "TRAP: Feminine in -age", "[lah PLAHZH]",
    "TRAP: Ending in -age but FEMININE! Think: Ladies love sunbathing on la plage.",
    "Les enfants jouent au ballon sur la plage.", "The children are playing ball on the beach.",
    True, "Key exception to the masculine -age rule!")

add(5, "l’image", "feminine", "A1", "image / picture", "TRAP: Feminine in -age", "[lee-MAHZH]",
    "TRAP: Ending in -age but FEMININE! Think of a lovely feminine image.",
    "Cette image illustre parfaitement la leçon.", "This picture illustrates the lesson perfectly.",
    True, "Key exception to the masculine -age rule!")

add(6, "la page", "feminine", "A1", "page (of a book)", "TRAP: Feminine in -age", "[lah PAHMZ]",
    "TRAP: Ending in -age but FEMININE! Turn the feminine page.",
    "Ouvrez votre livre à la page dix, s'il vous plaît.", "Open your book to page ten, please.",
    True, "Key exception to the masculine -age rule!")

add(7, "la cage", "feminine", "A1", "cage", "TRAP: Feminine in -age", "[lah KAHZH]",
    "TRAP: Ending in -age but FEMININE! The bird in la cage.",
    "L'oiseau chante joyeusement dans sa cage.", "The bird sings merrily in its cage.",
    True, "Key exception to the masculine -age rule!")

add(8, "le bateau", "masculine", "A1", "boat / ship", "MASC: Ending -eau", "[luh bah-TOH]",
    "Rule: -eau is overwhelmingly masculine! A sturdy masculine boat.",
    "Le bateau quitte le port de Marseille à midi.", "The boat leaves the port of Marseille at noon.")

add(9, "le château", "masculine", "A1", "castle", "MASC: Ending -eau", "[luh shah-TOH]",
    "Rule: -eau is masculine! Kings rule from le château.",
    "Nous avons visité un magnifique château médiéval.", "We visited a magnificent medieval castle.")

add(10, "le chapeau", "masculine", "A1", "hat", "MASC: Ending -eau", "[luh shah-POH]",
    "Rule: -eau is masculine! A gentleman wears le chapeau.",
    "Il porte un grand chapeau noir sous la pluie.", "He is wearing a big black hat in the rain.")

add(11, "le cadeau", "masculine", "A1", "gift / present", "MASC: Ending -eau", "[luh kah-DOH]",
    "Rule: -eau is masculine! A birthday gift wrapped in blue.",
    "Merci pour ce merveilleux cadeau d'anniversaire !", "Thank you for this wonderful birthday gift!")

add(12, "le couteau", "masculine", "A1", "knife", "MASC: Ending -eau", "[luh koo-TOH]",
    "Rule: -eau is masculine! A sharp knife beside the plate.",
    "Passe-moi le couteau pour couper le pain, s'il te plaît.", "Pass me the knife to cut the bread, please.")

add(13, "l’eau", "feminine", "A1", "water", "TRAP: Feminine in -eau", "[LOH]",
    "TRAP: Ending in -eau but FEMININE! Water (l'eau) and skin (la peau) are life's feminine duo.",
    "Tu veux un grand verre d'eau fraîche ?", "Do you want a big glass of cold water?",
    True, "One of the two most famous feminine -eau words!")

add(14, "la peau", "feminine", "A1", "skin", "TRAP: Feminine in -eau", "[lah POH]",
    "TRAP: Ending in -eau but FEMININE! Soft feminine skin.",
    "Cette crème hydrate la peau sèche en hiver.", "This cream hydrates dry skin in winter.",
    True, "One of the two most famous feminine -eau words!")

add(15, "le pain", "masculine", "A1", "bread", "MASC: Ending -ain", "[luh PAN]",
    "Rule: -ain is masculine! The daily French loaf.",
    "Va acheter du pain frais à la boulangerie.", "Go buy fresh bread at the bakery.")

add(16, "le train", "masculine", "A1", "train", "MASC: Ending -ain", "[luh TRAN]",
    "Rule: -ain is masculine! The high-speed TGV train.",
    "Le train pour Lyon part de la voie 4.", "The train for Lyon leaves from platform 4.")

add(17, "le bain", "masculine", "A1", "bath", "MASC: Ending -ain", "[luh BAN]",
    "Rule: -ain is masculine! A warm relaxing bath.",
    "L'enfant prend son bain avant de dormir.", "The child takes his bath before sleeping.")

add(18, "la main", "feminine", "A1", "hand", "TRAP: Feminine in -ain", "[lah MAN]",
    "TRAP: Ending in -ain but FEMININE! A woman's gentle hand holding a child.",
    "Donne-moi la main pour traverser la rue.", "Give me your hand to cross the street.",
    True, "The primary feminine exception to -ain!")

add(19, "le journal", "masculine", "A1", "newspaper", "MASC: Ending -al", "[luh zhoor-NAHL]",
    "Rule: -al ending is always masculine! Morning newspaper.",
    "Mon père lit le journal tous les matins au petit-déjeuner.", "My father reads the newspaper every morning at breakfast.")

add(20, "le cheval", "masculine", "A1", "horse", "MASC: Ending -al", "[luh shuh-VAHL]",
    "Rule: -al is masculine! A strong stallion.",
    "Le cheval blanc galope à travers les champs.", "The white horse gallops across the fields.")

add(21, "le travail", "masculine", "A1", "work / job", "MASC: Ending -ail", "[luh trah-VYE]",
    "Rule: -ail is 100% masculine! Daily work.",
    "Il part au travail à huit heures chaque matin.", "He leaves for work at eight o'clock every morning.")

add(22, "le fauteuil", "masculine", "A1", "armchair", "MASC: Ending -euil", "[luh foh-TUH-ee]",
    "Rule: -euil is masculine! Cozy armchair by the fire.",
    "Grand-père s'est endormi dans son grand fauteuil.", "Grandpa fell asleep in his big armchair.")

add(23, "le médicament", "masculine", "A1", "medicine / pill", "MASC: Ending -ment", "[luh may-dee-kah-MAHN]",
    "Rule: -ment is always masculine! Medicine prescribed by a doctor.",
    "Prends ce médicament trois fois par jour après les repas.", "Take this medicine three times a day after meals.")

add(24, "l’argent", "masculine", "A1", "money / silver", "MASC: Ending -ent", "[lahr-ZHAHN]",
    "Rule: -ent is masculine! Silver coins and paper cash.",
    "Il n'a pas assez d'argent pour acheter cette montre.", "He doesn't have enough money to buy this watch.")

add(25, "le restaurant", "masculine", "A1", "restaurant", "MASC: Ending -ant", "[luh rehs-toh-RAHN]",
    "Rule: -ant is masculine! A dining establishment.",
    "Nous dînons dans un excellent restaurant ce soir.", "We are having dinner at an excellent restaurant tonight.")

add(26, "la dent", "feminine", "A1", "tooth", "TRAP: Feminine in -ent", "[lah DAHN]",
    "TRAP: Ending in -ent but FEMININE! Latin dens is feminine.",
    "L'enfant a perdu sa première dent de lait.", "The child lost his first baby tooth.",
    True, "Classic feminine exception to -ent!")

add(27, "le cahier", "masculine", "A1", "notebook", "MASC: Ending -ier", "[luh kah-YAY]",
    "Rule: -ier is masculine! Student's writing book.",
    "Écris la réponse dans ton cahier d'exercices.", "Write the answer in your exercise notebook.")

add(28, "le café", "masculine", "A1", "coffee / café", "MASC: Ending -é", "[luh kah-FAY]",
    "Rule: Consonants and bare vowels are masculine! Morning espresso.",
    "Un café noir s'il vous plaît, sans sucre.", "A black coffee please, without sugar.")

add(29, "le problème", "masculine", "A1", "problem", "MASC: Greek in -ème", "[luh proh-BLEHM]",
    "TRAP FOR BEGINNERS: Ends in -e but MASCULINE due to Greek -ma origin!",
    "Il n'y a aucun problème, tout va bien se passer.", "There is no problem at all; everything will go well.",
    False, "Greek neuter origin makes -ème masculine despite ending in -e.")

add(30, "le système", "masculine", "A1", "system", "MASC: Greek in -ème", "[luh sees-TEHM]",
    "Rule: Greek -ma derivatives are masculine (system, problem, theme).",
    "Ce nouveau système informatique fonctionne très vite.", "This new computer system works very fast.")

add(31, "la question", "feminine", "A1", "question", "FEM: Ending -tion", "[lah kehs-TYOHN]",
    "Rule: -tion is 99% FEMININE! Asking a question.",
    "J'ai une petite question sur les devoirs.", "I have a quick question about the homework.")

add(32, "la solution", "feminine", "A1", "solution", "FEM: Ending -tion", "[lah soh-loo-SYOHN]",
    "Rule: -tion is feminine! Solving a puzzle.",
    "Nous avons enfin trouvé la bonne solution.", "We finally found the right solution.")

add(33, "la maison", "feminine", "A1", "house / home", "TRAP: Feminine in -on", "[lah may-ZOHN]",
    "TRAP: Ends in -on but is FEMININE! The sweet family house.",
    "Ma maison a un joli toit rouge et un petit jardin.", "My house has a nice red roof and a small garden.",
    True, "Key feminine exception to masculine -on!")

add(34, "la bicyclette", "feminine", "A1", "bicycle", "FEM: Ending -ette", "[lah bee-see-KLEHT]",
    "Rule: -ette is always feminine! Riding a bike.",
    "Elle va à l'école tous les jours à bicyclette.", "She goes to school every day by bicycle.")

add(35, "la fourchette", "feminine", "A1", "fork", "FEM: Ending -ette", "[lah foor-SHEHT]",
    "Rule: -ette is feminine! Table utensil.",
    "Mets la fourchette à gauche de l'assiette.", "Put the fork to the left of the plate.")

add(36, "la journée", "feminine", "A1", "day / daytime duration", "FEM: Ending -ée", "[lah zhoor-NAY]",
    "Rule: -ée denotes span of time and is feminine!",
    "Passez une très bonne journée !", "Have a wonderful day!")

add(37, "la soirée", "feminine", "A1", "evening / party", "FEM: Ending -ée", "[lah swah-RAY]",
    "Rule: -ée denotes duration and is feminine!",
    "Nous sommes invités à une soirée entre amis.", "We are invited to an evening party among friends.")

add(38, "l’idée", "feminine", "A1", "idea", "FEM: Ending -ée", "[lee-DAY]",
    "Rule: -ée is feminine! Having a bright idea.",
    "C'est une excellente idée pour le week-end !", "That's an excellent idea for the weekend!")

add(39, "le musée", "masculine", "A1", "museum", "TRAP: Masculine in -ée", "[luh moo-ZAY]",
    "TRAP: Ends in -ée but is MASCULINE! The Greek Museum trap.",
    "Le musée du Louvre est fermé le mardi.", "The Louvre museum is closed on Tuesdays.",
    True, "Major masculine exception to feminine -ée!")

add(40, "la voiture", "feminine", "A1", "car", "FEM: Ending -ure", "[lah vwah-TYOOR]",
    "Rule: -ure is feminine! Driving a car.",
    "Sa nouvelle voiture est très confortable et silencieuse.", "His new car is very comfortable and quiet.")

add(41, "la ville", "feminine", "A1", "city / town", "FEM: Ending -ille", "[lah VEEL]",
    "Rule: -ille is feminine! Paris is a grand city.",
    "Paris est une ville magnifique riche en histoire.", "Paris is a magnificent city rich in history.")

add(42, "la nuit", "feminine", "A1", "night", "TRAP: Feminine in -t", "[lah NWEE]",
    "TRAP: Ends in consonant -t but is FEMININE! Latin nox.",
    "La nuit est douce et étoilée en été.", "The night is mild and starry in summer.",
    True, "Classic feminine exception to consonant rule!")

add(43, "la mer", "feminine", "A1", "sea / ocean", "TRAP: Feminine in -er", "[lah MEHR]",
    "TRAP: Ends in -er but is FEMININE! Mother nature's sea.",
    "Nous passons nos vacances d'été au bord de la mer.", "We spend our summer vacation by the sea.",
    True, "Key exception to masculine -er!")

add(44, "la fin", "feminine", "A1", "end", "TRAP: Feminine in -in", "[lah FAN]",
    "TRAP: Ends in -in but is FEMININE! The movie's happy end.",
    "C'est la fin du film ; tout le monde applaudit.", "It's the end of the movie; everyone is clapping.",
    True, "Feminine exception to masculine -in!")

add(45, "la photo", "feminine", "A1", "photo", "TRAP: Feminine in -o", "[lah foh-TOH]",
    "TRAP: Ends in -o but is FEMININE because it's short for la photographie!",
    "Montre-moi la photo de tes vacances à Nice.", "Show me the photo of your vacation in Nice.",
    True, "Feminine abbreviation exception!")

# ==========================================
# LEVEL A2: ELEMENTARY EXPANSION & THEMATIC GROUPS
# ==========================================
add(46, "le mariage", "masculine", "A2", "marriage / wedding", "MASC: Ending -age", "[luh mah-ree-YAHZH]",
    "Rule: -age is masculine! A wedding ceremony.",
    "Ils ont célébré leur mariage dans un château de la Loire.", "They celebrated their wedding in a Loire Valley castle.")

add(47, "le courage", "masculine", "A2", "courage / bravery", "MASC: Ending -age", "[luh koo-RAHZH]",
    "Rule: -age is masculine! Having the heart (cœur) of courage.",
    "Il faut beaucoup de courage pour changer de métier.", "It takes a lot of courage to change professions.")

add(48, "le tableau", "masculine", "A2", "painting / blackboard", "MASC: Ending -eau", "[luh tah-BLOH]",
    "Rule: -eau is masculine! A painting hanging on the wall.",
    "Le professeur écrit les phrases clés sur le tableau.", "The teacher writes the key sentences on the board.")

add(49, "le sentiment", "masculine", "A2", "feeling / sentiment", "MASC: Ending -ment", "[luh sahn-tee-MAHN]",
    "Rule: -ment forms masculine abstract nouns from verbs (sentir &rarr; sentiment).",
    "J'ai le sentiment que nous allons réussir ce projet.", "I have a feeling that we are going to succeed in this project.")

add(50, "le gouvernement", "masculine", "A2", "government", "MASC: Ending -ment", "[luh goo-vehr-nuh-MAHN]",
    "Rule: -ment is masculine! The state leadership.",
    "Le gouvernement a annoncé de nouvelles mesures économiques.", "The government announced new economic measures.")

add(51, "le chêne", "masculine", "A2", "oak tree", "MASC: Trees & Shrubs", "[luh SHEHN]",
    "Rule: Trees are 100% MASCULINE in French! The mighty oak.",
    "Le vieux chêne dans le parc a plus de deux cents ans.", "The old oak in the park is over two hundred years old.")

add(52, "le pommier", "masculine", "A2", "apple tree", "MASC: Trees & Shrubs", "[luh poh-MYAY]",
    "Rule: Fruit trees formed with -ier are always masculine! Apple tree.",
    "Le pommier du verger donne des fruits délicieux en automne.", "The apple tree in the orchard gives delicious fruit in autumn.")

add(53, "la pomme", "feminine", "A2", "apple", "FEM: Fruits in -e", "[lah POHM]",
    "Rule: Most fruits ending in -e are feminine! Red apple.",
    "Manger une pomme par jour est excellent pour la santé.", "Eating an apple a day is great for your health.")

add(54, "le citron", "masculine", "A2", "lemon", "MASC: Fruits in consonant", "[luh see-TROHN]",
    "Rule: Fruits ending in consonants are masculine! Sour yellow lemon.",
    "Ajoute un peu de jus de citron sur le poisson grillé.", "Add a bit of lemon juice over the grilled fish.")

add(55, "la décision", "feminine", "A2", "decision", "FEM: Ending -sion", "[lah day-see-ZYOHN]",
    "Rule: -sion is feminine! Making up one's mind.",
    "C'est une décision difficile mais nécessaire pour l'équipe.", "It is a difficult but necessary decision for the team.")

add(56, "la liberté", "feminine", "A2", "liberty / freedom", "FEM: Ending -té", "[lah lee-behr-TAY]",
    "Rule: -té (from Latin -tas) is feminine! Universal freedom.",
    "La statue de la Liberté est un symbole mondial de démocratie.", "The Statue of Liberty is a global symbol of democracy.")

add(57, "la vérité", "feminine", "A2", "truth", "FEM: Ending -té", "[lah vay-ree-TAY]",
    "Rule: -té is feminine! Telling the truth.",
    "Il est toujours préférable de dire la vérité à ses amis.", "It is always preferable to tell the truth to one's friends.")

add(58, "la beauté", "feminine", "A2", "beauty", "FEM: Ending -té", "[lah boh-TAY]",
    "Rule: -té is feminine! Splendor and beauty.",
    "La beauté de ce coucher de soleil nous a tous émus.", "The beauty of this sunset moved us all.")

add(59, "la chance", "feminine", "A2", "luck / chance", "FEM: Ending -ance", "[lah SHAHNS]",
    "Rule: -ance is feminine! Good fortune.",
    "Bonne chance pour ton examen de français demain !", "Good luck on your French exam tomorrow!")

add(60, "la différence", "feminine", "A2", "difference", "FEM: Ending -ence", "[lah dee-fay-RAHNS]",
    "Rule: -ence is feminine! Telling things apart.",
    "Quelle est la différence principale entre ces deux mots ?", "What is the main difference between these two words?")

add(61, "le silence", "masculine", "A2", "silence", "TRAP: Masculine in -ence", "[luh see-LAHNS]",
    "TRAP: Ends in -ence but is MASCULINE! Golden silence is masculine in French.",
    "Un silence complet régnait dans la bibliothèque silencieuse.", "Complete silence reigned in the quiet library.",
    True, "Famous masculine exception to feminine -ence!")

add(62, "la chaleur", "feminine", "A2", "heat / warmth", "FEM: Abstract -eur", "[lah shah-LUHR]",
    "Rule: Sensations and emotional qualities in -eur are FEMININE!",
    "La chaleur de l'après-midi était presque insupportable.", "The afternoon heat was almost unbearable.")

add(63, "la couleur", "feminine", "A2", "color", "FEM: Abstract -eur", "[lah koo-LUHR]",
    "Rule: -eur denoting visual/physical quality is FEMININE!",
    "Quelle est ta couleur préférée pour la chambre ?", "What is your favorite color for the bedroom?")

add(64, "le bonheur", "masculine", "A2", "happiness", "TRAP: Masculine in -eur", "[luh boh-NUHR]",
    "TRAP: Ends in -eur but is MASCULINE! Bon + heur = good omen.",
    "La naissance de leur enfant a comblé la famille de bonheur.", "The birth of their child filled the family with happiness.",
    True, "Key exception to the feminine abstract -eur rule!")

add(65, "la saison", "feminine", "A2", "season", "TRAP: Feminine in -on", "[lah say-ZOHN]",
    "TRAP: Ends in -on but is FEMININE! Four seasons of the year.",
    "Le printemps est ma saison préférée pour faire du vélo.", "Spring is my favorite season for cycling.",
    True, "Feminine exception to masculine -on!")

add(66, "la chanson", "feminine", "A2", "song", "TRAP: Feminine in -on", "[lah shahn-SOHN]",
    "TRAP: Ends in -on but is FEMININE! Singing a French melody.",
    "Cette jolie chanson me rappelle mon voyage à Paris.", "This pretty song reminds me of my trip to Paris.",
    True, "Feminine exception to masculine -on!")

add(67, "la boisson", "feminine", "A2", "drink / beverage", "TRAP: Feminine in -on", "[lah bwah-SOHN]",
    "TRAP: Ends in -on but is FEMININE! A cool drink.",
    "Le serveur nous a apporté une boisson rafraîchissante.", "The waiter brought us a refreshing drink.",
    True, "Feminine exception to masculine -on!")

add(68, "le tire-bouchon", "masculine", "A2", "corkscrew", "MASC: Verb+Noun Compound", "[luh teer-boo-SHOHN]",
    "Rule: Verb + Noun compounds are ALWAYS MASCULINE! (tirer + bouchon).",
    "Où as-tu rangé le tire-bouchon pour ouvrir le vin ?", "Where did you put the corkscrew to open the wine?")

add(69, "le porte-monnaie", "masculine", "A2", "wallet / coin purse", "MASC: Verb+Noun Compound", "[luh pohrt-moh-NAY]",
    "Rule: Verb + Noun compound is MASCULINE even though monnaie is feminine!",
    "J'ai oublié mon porte-monnaie sur la table de nuit.", "I left my wallet on the nightstand.")

add(70, "la France", "feminine", "A2", "France", "GEO: Country ending in -e", "[lah FRAHNS]",
    "Rule: Countries ending in -e are FEMININE! La République.",
    "La France est célèbre pour sa gastronomie et sa culture.", "France is famous for its gastronomy and culture.")

add(71, "le Canada", "masculine", "A2", "Canada", "GEO: Country ending in non-e", "[luh kah-nah-DAH]",
    "Rule: Countries ending in consonants or non-e vowels are MASCULINE!",
    "Mon frère vit au Canada depuis maintenant trois ans.", "My brother has been living in Canada for three years now.")

add(72, "le Mexique", "masculine", "A2", "Mexico", "TRAP: Country in -e (MASC)", "[luh mehk-SEEK]",
    "TRAP: Ends in -e but is MASCULINE! One of the 6 famous masculine -e countries.",
    "Nous partons en vacances au Mexique en décembre.", "We are going on vacation to Mexico in December.",
    True, "High-frequency exception to geographic -e rule!")

add(73, "l’infirmier", "masculine", "A2", "nurse (male)", "PROF: Ending -ier", "[lan-feer-MYAY]",
    "Rule: Masculine profession in -ier becomes -ière in feminine.",
    "L'infirmier a pris la température du patient avec soin.", "The male nurse took the patient's temperature carefully.")

add(74, "l’infirmière", "feminine", "A2", "nurse (female)", "PROF: Ending -ière", "[lan-feer-MYEHR]",
    "Rule: Feminine counterpart of -ier is -ière.",
    "L'infirmière lui a fait une piqûre sans douleur.", "The female nurse gave him a painless injection.")

add(75, "le serveur", "masculine", "A2", "waiter", "PROF: Ending -eur", "[luh sehr-VUHR]",
    "Rule: Agent noun in -eur becomes -euse in feminine.",
    "Le serveur nous a recommandé le plat du jour.", "The waiter recommended the special of the day to us.")

add(76, "la serveuse", "feminine", "A2", "waitress", "PROF: Ending -euse", "[lah sehr-VUHZ]",
    "Rule: Feminine form of -eur agent noun.",
    "La serveuse a pris notre commande avec le sourire.", "The waitress took our order with a smile.")

add(77, "l’acteur", "masculine", "A2", "actor", "PROF: Ending -teur", "[lahk-TUHR]",
    "Rule: -teur becomes -trice in feminine when based on Latin -tor.",
    "Cet acteur joue un rôle dramatique dans la nouvelle pièce.", "This actor plays a dramatic role in the new play.")

add(78, "l’actrice", "feminine", "A2", "actress", "PROF: Ending -trice", "[lahk-TREES]",
    "Rule: Feminine of -teur is -trice.",
    "L'actrice a reçu un prix prestigieux pour sa performance.", "The actress received a prestigious award for her performance.")

add(79, "le livre", "masculine", "A2", "book", "DUAL: Meaning-Shift (Masc)", "[luh LEEVR]",
    "DUAL GENDER: Le livre = a reading book (masculine).",
    "Ce livre de grammaire explique clairement toutes les règles.", "This grammar book explains all the rules clearly.")

add(80, "la livre", "feminine", "A2", "pound (weight/currency)", "DUAL: Meaning-Shift (Fem)", "[lah LEEVR]",
    "DUAL GENDER: La livre = 500 grams of weight or British £ currency.",
    "J'ai acheté une livre de fraises mûres au marché.", "I bought a pound of ripe strawberries at the market.",
    True, "Dual gender shift: meaning changes completely with article!")

add(81, "le tour", "masculine", "A2", "turn / tour / trick", "DUAL: Meaning-Shift (Masc)", "[luh TOOR]",
    "DUAL GENDER: Le tour = a circuit, turn, or magician's trick.",
    "Le magicien a réussi un tour de cartes incroyable.", "The magician performed an incredible card trick.")

add(82, "la tour", "feminine", "A2", "tower", "DUAL: Meaning-Shift (Fem)", "[lah TOOR]",
    "DUAL GENDER: La tour = a tall tower (e.g., la tour Eiffel).",
    "La tour Eiffel scintille de mille feux chaque soir.", "The Eiffel Tower sparkles with a thousand lights every evening.",
    True, "Dual gender shift!")

add(83, "le chat", "masculine", "A2", "male cat", "ANIM: Suffix Pair (Masc)", "[luh SHAH]",
    "Rule: Male animal with female counterpart in -te.",
    "Le chat dort paisiblement sur le coussin du canapé.", "The male cat is sleeping peacefully on the sofa cushion.")

add(84, "la chatte", "feminine", "A2", "female cat", "ANIM: Suffix Pair (Fem)", "[lah SHAHT]",
    "Rule: Double consonant + e for feminine animal.",
    "La chatte prend tendrement soin de ses petits chatons.", "The female cat tenderly cares for her little kittens.")

add(85, "la forêt", "feminine", "A2", "forest", "TRAP: Feminine in -êt", "[lah foh-REH]",
    "TRAP: Ends in -êt but is FEMININE! The enchanted forest.",
    "Nous avons fait une longue promenade dans la forêt.", "We took a long walk in the forest.",
    True, "Feminine exception to consonant/t ending!")

add(86, "la voix", "feminine", "A2", "voice", "TRAP: Feminine in -x", "[lah VWAH]",
    "TRAP: Ends in -x but is FEMININE! The soprano's melodious voice.",
    "Cette cantatrice a une voix absolument magnifique.", "This opera singer has an absolutely magnificent voice.",
    True, "Feminine exception to masculine -x!")

add(87, "la paix", "feminine", "A2", "peace", "TRAP: Feminine in -x", "[lah PEH]",
    "TRAP: Ends in -x but is FEMININE! Peace across nations.",
    "Les peuples du monde aspirent tous à vivre dans la paix.", "The peoples of the world all yearn to live in peace.",
    True, "Feminine exception to masculine -x!")

add(88, "le squelette", "masculine", "A2", "skeleton", "TRAP: Masculine in -ette", "[luh skuh-LEHT]",
    "TRAP: Ends in -ette but is MASCULINE! Bones are hard and masculine.",
    "Le squelette humain comprend plus de deux cents os.", "The human skeleton comprises more than two hundred bones.",
    True, "Famous masculine exception to feminine -ette!")

add(89, "le parapluie", "masculine", "A2", "umbrella", "TRAP: Masculine in -ie", "[luh pah-rah-PLWEE]",
    "TRAP: Compound (parer + la pluie) makes it MASCULINE despite -ie!",
    "Prends ton parapluie car il risque de pleuvoir cet après-midi.", "Take your umbrella because it might rain this afternoon.",
    True, "Masculine compound exception to feminine -ie!")

add(90, "le lycée", "masculine", "A2", "high school", "TRAP: Masculine in -ée", "[luh lee-SAY]",
    "TRAP: Ends in -ée but is MASCULINE! From Greek Lykeion.",
    "Ma fille aînée entre au lycée en septembre prochain.", "My eldest daughter enters high school next September.",
    True, "Key masculine exception to -ée!")

# ==========================================
# LEVEL B1: INTERMEDIATE FUNCTIONAL INDEPENDENCE
# ==========================================
add(91, "le comportement", "masculine", "B1", "behavior / demeanor", "MASC: Ending -ment", "[luh kohn-pohr-tuh-MAHN]",
    "Rule: Abstract nouns in -ment are masculine.",
    "Son comportement exemplaire a été salué par ses collègues.", "His exemplary behavior was praised by his colleagues.")

add(92, "le réchauffement", "masculine", "B1", "warming", "MASC: Ending -ment", "[luh ray-shohf-MAHN]",
    "Rule: -ment is masculine! Climate warming.",
    "Le réchauffement climatique est un défi majeur de notre époque.", "Global warming is a major challenge of our era.")

add(93, "le sondage", "masculine", "B1", "opinion poll / survey", "MASC: Ending -age", "[luh sohn-DAHZH]",
    "Rule: -age is masculine! Political polling.",
    "Le dernier sondage révèle une nette évolution des mentalités.", "The latest poll reveals a clear shift in attitudes.")

add(94, "le recueil", "masculine", "B1", "anthology / collection", "MASC: Ending -euil", "[luh ruh-KUH-ee]",
    "Rule: -euil is always masculine! Poetry collection.",
    "Elle lit un recueil de poèmes romantiques dans le train.", "She is reading an anthology of romantic poems on the train.")

add(95, "le compromis", "masculine", "B1", "compromise", "MASC: Ending -is", "[luh kohn-proh-MEE]",
    "Rule: -is is masculine! Finding middle ground.",
    "Les deux partis ont finalement trouvé un compromis équitable.", "Both parties finally found a fair compromise.")

add(96, "le stéthoscope", "masculine", "B1", "stethoscope", "MASC: Ending -scope", "[luh stay-toh-SKOHP]",
    "Rule: Greek instrument ending in -scope is 100% masculine!",
    "Le médecin pose son stéthoscope pour écouter le cœur.", "The doctor places his stethoscope to listen to the heart.")

add(97, "le télescope", "masculine", "B1", "telescope", "MASC: Ending -scope", "[luh tay-leh-SKOHP]",
    "Rule: Greek instrument in -scope is masculine!",
    "Le télescope spatial a capturé des images d'une galaxie lointaine.", "The space telescope captured images of a distant galaxy.")

add(98, "le schéma", "masculine", "B1", "diagram / scheme", "MASC: Greek in -a", "[luh shay-MAH]",
    "Rule: Scientific nouns from Greek in -ma are masculine!",
    "Ce schéma explicatif simplifie le fonctionnement du moteur.", "This explanatory diagram simplifies how the engine works.")

add(99, "le phénomène", "masculine", "B1", "phenomenon", "MASC: Greek in -ème", "[luh fay-noh-MEHN]",
    "Rule: Greek neuter roots in -ène / -ème are masculine!",
    "Une éclipse totale est un phénomène astronomique rare.", "A total eclipse is a rare astronomical phenomenon.")

add(100, "le dilemme", "masculine", "B1", "dilemma", "MASC: Greek in -emme", "[luh dee-LEHM]",
    "Rule: Greek -lemma becomes masculine in French!",
    "Il fait face à un dilemme moral particulièrement complexe.", "He faces a particularly complex moral dilemma.")

add(101, "le diplôme", "masculine", "B1", "diploma / degree", "MASC: Greek in -ôme", "[luh dee-PLOHM]",
    "Rule: Greek -ma derivative ending in -ôme is masculine!",
    "Elle recevra son diplôme universitaire à la fin de l'année.", "She will receive her university diploma at the end of the year.")

add(102, "le fleuve", "masculine", "B1", "river (flowing to sea)", "MASC: Ending -e", "[luh FLUHV]",
    "Rule: Distinguish fleuve (masc, flows into ocean) from rivière (fem, tributary).",
    "Le fleuve Saint-Laurent traverse des paysages spectaculaires.", "The St. Lawrence River crosses spectacular landscapes.")

add(103, "la rivière", "feminine", "B1", "river (tributary)", "FEM: Ending -ière", "[lah ree-VYEHR]",
    "Rule: Suffix -ière is feminine! A winding tributary river.",
    "La rivière serpente à travers la verte vallée boisée.", "The river winds through the green wooded valley.")

add(104, "le poêle", "masculine", "B1", "wood stove / heater", "DUAL: Meaning-Shift (Masc)", "[luh PWAHL]",
    "DUAL GENDER: Le poêle = a heating stove (masc).",
    "Ils ont allumé le poêle à bois pour réchauffer le salon.", "They lit the wood stove to warm the living room.")

add(105, "la poêle", "feminine", "B1", "frying pan / skillet", "DUAL: Meaning-Shift (Fem)", "[lah PWAHL]",
    "DUAL GENDER: La poêle = cooking skillet (fem).",
    "Faites dorer les oignons émincés dans la poêle avec du beurre.", "Brown the minced onions in the frying pan with butter.",
    True, "Dual gender shift!")

add(106, "le manche", "masculine", "B1", "tool handle / broomstick", "DUAL: Meaning-Shift (Masc)", "[luh MAHN-sh]",
    "DUAL GENDER: Le manche = handle of a knife, broom, or guitar (masc).",
    "Le manche en bois de ce vieux couteau est très solide.", "The wooden handle of this old knife is very sturdy.")

add(107, "la manche", "feminine", "B1", "sleeve / English Channel", "DUAL: Meaning-Shift (Fem)", "[lah MAHN-sh]",
    "DUAL GENDER: La manche = shirt sleeve OR the English Channel (La Manche).",
    "Il a déchiré la manche de sa chemise en grimpant.", "He tore the sleeve of his shirt while climbing.",
    True, "Dual gender shift!")

add(108, "le voile", "masculine", "B1", "veil (bridal/face covering)", "DUAL: Meaning-Shift (Masc)", "[luh VWAHL]",
    "DUAL GENDER: Le voile = cloth veil covering face or head (masc).",
    "La mariée portait un long voile blanc en dentelle fine.", "The bride wore a long white veil made of fine lace.")

add(109, "la voile", "feminine", "B1", "sail (boat) / sailing", "DUAL: Meaning-Shift (Fem)", "[lah VWAHL]",
    "DUAL GENDER: La voile = cloth sail of a ship or the sport of sailing.",
    "Il hisse la grand-voile pour profiter du vent marin.", "He hoists the mainsail to catch the sea breeze.",
    True, "Dual gender shift!")

add(110, "le poste", "masculine", "B1", "job position / radio set", "DUAL: Meaning-Shift (Masc)", "[luh POHST]",
    "DUAL GENDER: Le poste = an employment post or receiving set (masc).",
    "Il a postulé pour un poste de responsable des ventes.", "He applied for a sales manager position.")

add(111, "la poste", "feminine", "B1", "post office / mail service", "DUAL: Meaning-Shift (Fem)", "[lah POHST]",
    "DUAL GENDER: La poste = the mail institution / postal building (fem).",
    "Je dois passer à la poste avant dix-huit heures pour envoyer un colis.", "I have to stop by the post office before 6 PM to mail a package.",
    True, "Dual gender shift!")

add(112, "le maire", "masculine", "B1", "city mayor", "HOMOPHONE: [mɛʁ] (Masc)", "[luh MEHR]",
    "HOMOPHONE: Le maire (mayor, masc) vs la mer (sea, fem) vs la mère (mother, fem).",
    "Le maire de notre ville a inauguré la nouvelle école.", "The mayor of our city inaugurated the new school.")

add(113, "le comte", "masculine", "B1", "count / nobleman", "HOMOPHONE: [kɔ̃t] (Masc)", "[luh KOHNT]",
    "HOMOPHONE: Le comte (nobleman) vs le conte (fairy tale) vs le compte (bank account).",
    "Le comte de Monte-Cristo est un chef-d'œuvre littéraire d'Alexandre Dumas.", "The Count of Monte Cristo is a literary masterpiece by Alexandre Dumas.")

add(114, "le conte", "masculine", "B1", "tale / fairy story", "HOMOPHONE: [kɔ̃t] (Masc)", "[luh KOHNT]",
    "HOMOPHONE: A magical fairy tale.",
    "Grand-mère nous lisait un conte de fées avant de nous coucher.", "Grandmother used to read us a fairy tale before bedtime.")

add(115, "le compte", "masculine", "B1", "bank account / count", "HOMOPHONE: [kɔ̃t] (Masc)", "[luh KOHNT]",
    "HOMOPHONE: Bank or financial balance account.",
    "J'ai vérifié le solde de mon compte bancaire ce matin.", "I checked the balance of my bank account this morning.")

add(116, "la victime", "feminine", "B1", "victim (male or female)", "HUMAN: Fixed Feminine", "[lah veek-TEEM]",
    "Rule: Always FEMININE, even when referring exclusively to a man!",
    "Cet homme courageux a été la victime d'un vol à main armée.", "This brave man was the victim of an armed robbery.",
    True, "Fixed grammatical gender applies regardless of biological sex!")

add(117, "la personne", "feminine", "B1", "person (male or female)", "HUMAN: Fixed Feminine", "[lah pehr-SOHN]",
    "Rule: Always FEMININE in French! Cet homme est une personne généreuse.",
    "C'est une personne très cultivée et bienveillante.", "She/he is a very cultivated and benevolent person.",
    True, "Fixed feminine gender!")

add(118, "la vedette", "feminine", "B1", "star / headliner", "HUMAN: Fixed Feminine", "[lah vuh-DEHT]",
    "Rule: Fixed FEMININE gender for celebrities, male or female.",
    "Ce jeune acteur est la nouvelle vedette du cinéma français.", "This young actor is the new headliner of French cinema.")

add(119, "le témoin", "masculine", "B1", "witness (male or female)", "HUMAN: Fixed Masculine", "[luh tay-MWAN]",
    "Rule: Fixed MASCULINE noun: Cette femme est un témoin capital.",
    "Le témoin a prêté serment devant le tribunal.", "The witness took an oath before the court.")

add(120, "le mannequin", "masculine", "B1", "fashion model", "HUMAN: Fixed Masculine", "[luh mahn-KAN]",
    "Rule: Always MASCULINE even when designating a top female model!",
    "Elle travaille comme mannequin pour de grandes maisons de couture.", "She works as a model for major fashion houses.")

add(121, "le taureau", "masculine", "B1", "bull", "ANIM: Distinct Root (Masc)", "[luh toh-ROH]",
    "Rule: Distinct biological animal root from cow (la vache).",
    "Le taureau noir charge avec une puissance impressionnante.", "The black bull charges with impressive power.")

add(122, "la vache", "feminine", "B1", "cow", "ANIM: Distinct Root (Fem)", "[lah VAHSH]",
    "Rule: Distinct female counterpart to bull (le taureau).",
    "La vache broute paisiblement dans la verte prairie normande.", "The cow grazes peacefully in the green Normandy meadow.")

add(123, "le bélier", "masculine", "B1", "ram", "ANIM: Distinct Root (Masc)", "[luh bay-LYAY]",
    "Rule: Distinct biological root from ewe (la brebis).",
    "Le bélier aux cornes recourbées guide le troupeau.", "The ram with curved horns guides the flock.")

add(124, "la brebis", "feminine", "B1", "ewe / female sheep", "ANIM: Distinct Root (Fem)", "[lah bruh-BEE]",
    "Rule: Distinct female counterpart to ram (le bélier).",
    "La brebis protège son agneau contre les rigueurs du froid.", "The ewe protects her lamb against the bitter cold.")

add(125, "le Cambodge", "masculine", "B1", "Cambodia", "GEO: Country in -e (MASC)", "[luh kahn-BOHDZH]",
    "TRAP: Ends in -e but is MASCULINE! One of the 6 masculine -e countries.",
    "Le Cambodge possède des temples d'une beauté architecturale inouïe.", "Cambodia possesses temples of incredible architectural beauty.",
    True, "Masculine country ending in -e exception!")

add(126, "le Mozambique", "masculine", "B1", "Mozambique", "GEO: Country in -e (MASC)", "[luh moh-zahm-BEEK]",
    "TRAP: Ends in -e but is MASCULINE!",
    "Le Mozambique est situé sur la côte sud-est de l'Afrique.", "Mozambique is located on the southeast coast of Africa.",
    True, "Masculine country ending in -e exception!")

add(127, "le comité", "masculine", "B1", "committee", "TRAP: Masculine in -té", "[luh koh-mee-TAY]",
    "TRAP: Ends in -té but is MASCULINE! The executive committee.",
    "Le comité directeur se réunit chaque premier lundi du mois.", "The steering committee meets every first Monday of the month.",
    True, "Masculine exception to feminine -té!")

add(128, "le traité", "masculine", "B1", "treaty", "TRAP: Masculine in -té", "[luh tray-TAY]",
    "TRAP: Ends in -té but is MASCULINE! Peace treaty.",
    "Les deux pays ont ratifié un traité de paix historique.", "Both countries ratified a historic peace treaty.",
    True, "Masculine exception to feminine -té!")

add(129, "l’incendie", "masculine", "B1", "fire / wildfire", "TRAP: Masculine in -ie", "[lan-sahn-DEE]",
    "TRAP: Ends in -ie but is MASCULINE! Raging blaze.",
    "Les pompiers ont lutté toute la nuit contre l'incendie de forêt.", "The firefighters fought all night against the forest fire.",
    True, "Masculine exception to feminine -ie!")

add(130, "le sosie", "masculine", "B1", "lookalike / double", "TRAP: Masculine in -ie", "[luh soh-ZEE]",
    "TRAP: Ends in -ie but is MASCULINE! Identical double.",
    "Cet acteur a un sosie parfait qui le remplace lors des cascades.", "This actor has a perfect double who replaces him during stunts.",
    True, "Masculine exception to feminine -ie!")

add(131, "le génie", "masculine", "B1", "genius / engineering", "TRAP: Masculine in -ie", "[luh zhay-NEE]",
    "TRAP: Ends in -ie but is MASCULINE! Artistic or intellectual genius.",
    "Le génie de Léonard de Vinci fascine encore aujourd'hui.", "The genius of Leonardo da Vinci still fascinates today.",
    True, "Masculine exception to feminine -ie!")

add(132, "la souris", "feminine", "B1", "mouse (animal & tech)", "TRAP: Feminine in -is", "[lah soo-REE]",
    "TRAP: Ends in -is but is FEMININE! Computer mouse and rodent.",
    "La souris sans fil de mon ordinateur n'a plus de batterie.", "My computer's wireless mouse ran out of battery.",
    True, "Feminine exception to masculine -is!")

add(133, "la vis", "feminine", "B1", "screw", "TRAP: Feminine in -is", "[lah VEES]",
    "TRAP: Ends in -is but is FEMININE! Hardware screw.",
    "Resserre cette petite vis métallique avec un tournevis adapté.", "Tighten this small metal screw with a suitable screwdriver.",
    True, "Feminine exception to masculine -is!")

add(134, "la clé (clef)", "feminine", "B1", "key", "TRAP: Feminine in -é/-ef", "[lah KLAY]",
    "TRAP: Feminine ending in -ef / -é! Door key.",
    "J'ai égaré la clé de mon appartement dans le métro.", "I lost my apartment key in the subway.",
    True, "Feminine exception!")

add(135, "la faim", "feminine", "B1", "hunger", "TRAP: Feminine in -aim", "[lah FAN]",
    "TRAP: Ending in -aim is FEMININE! Avoir faim.",
    "Après cette longue marche, nous avions tous une faim de loup.", "After this long walk, we all had a wolf's hunger.",
    True, "Feminine exception!")

# ==========================================
# LEVEL B2: VANTAGE & NUANCED MASTERY
# ==========================================
add(136, "le préjudice", "masculine", "B2", "injury / legal damage", "MASC: Ending -ice", "[luh pray-zhoo-DEES]",
    "Rule: From Latin neuter praejudicium &rarr; masculine in French!",
    "La cour lui a accordé une indemnité pour le préjudice subi.", "The court awarded him compensation for the damage suffered.")

add(137, "le bénéfice", "masculine", "B2", "profit / financial gain", "MASC: Ending -ice", "[luh bay-nay-FEES]",
    "Rule: Latin neuter beneficium &rarr; masculine in French!",
    "L'entreprise a enregistré un bénéfice record au dernier trimestre.", "The company recorded a record profit in the last quarter.")

add(138, "le sacrifice", "masculine", "B2", "sacrifice", "MASC: Ending -ice", "[luh sah-kree-FEES]",
    "Rule: Latin neuter sacrificium &rarr; masculine!",
    "Ce projet a exigé un immense sacrifice personnel de sa part.", "This project demanded an immense personal sacrifice on his part.")

add(139, "l’édifice", "masculine", "B2", "edifice / monumental building", "MASC: Ending -ice", "[lay-dee-FEES]",
    "Rule: Latin aedificium &rarr; masculine!",
    "Cet édifice gothique du douzième siècle domine toute la place.", "This twelfth-century Gothic edifice dominates the entire square.")

add(140, "l’avarice", "feminine", "B2", "greed / miserliness", "FEM: Ending -ice", "[lah-vah-REES]",
    "Rule: From Latin feminine avaritia &rarr; feminine in French!",
    "L'avarice d'Harpagon est le thème central de la pièce de Molière.", "Harpagon's greed is the central theme of Molière's play.",
    True, "Contrasts with masculine neuter-derived -ice nouns!")

add(141, "la cicatrice", "feminine", "B2", "scar", "FEM: Ending -ice", "[lah see-kah-TREES]",
    "Rule: From Latin feminine cicatrix &rarr; feminine in French!",
    "La cicatrice sur son bras s'est estompée avec le temps.", "The scar on his arm faded over time.",
    True, "Feminine Latin root!")

add(142, "la notice", "feminine", "B2", "instructions / user guide", "FEM: Ending -ice", "[lah noh-TEES]",
    "Rule: Feminine -ice noun.",
    "Lisez attentivement la notice de montage avant de commencer.", "Read the assembly instructions carefully before starting.",
    True, "Feminine -ice!")

add(143, "le dictionnaire", "masculine", "B2", "dictionary", "MASC: Ending -aire", "[luh deek-syoh-NEHR]",
    "Rule: Suffix -aire is overwhelmingly masculine!",
    "Consultez le dictionnaire pour vérifier l'étymologie du mot.", "Consult the dictionary to verify the word's etymology.")

add(144, "le répertoire", "masculine", "B2", "directory / repertoire", "MASC: Ending -oire", "[luh ray-pehr-TWAHR]",
    "Rule: Suffix -oire is predominantly masculine!",
    "Cette troupe de théâtre possède un répertoire classique très étendu.", "This theater troupe possesses a very extensive classical repertoire.")

add(145, "la trajectoire", "feminine", "B2", "trajectory / path", "FEM: Ending -oire", "[lah trah-zhehk-TWAHR]",
    "TRAP: Ends in -oire but is FEMININE! Missile trajectory.",
    "La fusée a parfaitement suivi sa trajectoire orbitale prévue.", "The rocket perfectly followed its planned orbital trajectory.",
    True, "Feminine exception to -oire!")

add(146, "la gloire", "feminine", "B2", "glory", "FEM: Ending -oire", "[lah GLWAHR]",
    "TRAP: Ending in -oire is FEMININE! Crown of glory.",
    "Ce général cherchait la gloire sur tous les champs de bataille.", "This general sought glory on all battlefields.",
    True, "Feminine exception to -oire!")

add(147, "l’histoire", "feminine", "B2", "history / story", "FEM: Ending -oire", "[lees-TWAHR]",
    "TRAP: Ends in -oire but is FEMININE! Latin historia.",
    "L'histoire de France est riche en bouleversements politiques.", "The history of France is rich in political upheavals.",
    True, "Feminine exception!")

add(148, "le mémoire", "masculine", "B2", "academic thesis / legal memo", "DUAL: Meaning-Shift (Masc)", "[luh may-MWAHR]",
    "DUAL GENDER: Le mémoire = written research thesis or memorandum.",
    "Il a soutenu son mémoire de maîtrise avec la mention très bien.", "He defended his master's thesis with highest honors.")

add(149, "la mémoire", "feminine", "B2", "cognitive memory / recall", "DUAL: Meaning-Shift (Fem)", "[lah may-MWAHR]",
    "DUAL GENDER: La mémoire = human faculty of remembering or computer RAM.",
    "Elle a une excellente mémoire pour les noms et les visages.", "She has an excellent memory for names and faces.",
    True, "Dual gender shift!")

add(150, "le mode", "masculine", "B2", "mode / method / mood", "DUAL: Meaning-Shift (Masc)", "[luh MOHD]",
    "DUAL GENDER: Le mode = method, grammatical mood (le subjonctif).",
    "Ce mode de fonctionnement assure une rentabilité optimale.", "This operating mode ensures optimal profitability.")

add(151, "la mode", "feminine", "B2", "fashion / trend", "DUAL: Meaning-Shift (Fem)", "[lah MOHD]",
    "DUAL GENDER: La mode = clothing trend or cultural vogue.",
    "La haute couture parisienne dicte la mode internationale.", "Parisian haute couture dictates international fashion.",
    True, "Dual gender shift!")

add(152, "le moule", "masculine", "B2", "baking mold / cake pan", "DUAL: Meaning-Shift (Masc)", "[luh MOOL]",
    "DUAL GENDER: Le moule = casting shape or baking tin.",
    "Versez la préparation chocolatée dans le moule beurré.", "Pour the chocolate mixture into the buttered mold.")

add(153, "la moule", "feminine", "B2", "mussel (shellfish)", "DUAL: Meaning-Shift (Fem)", "[lah MOOL]",
    "DUAL GENDER: La moule = edible seafood mussel.",
    "Nous avons commandé une grande casserole de moules marinières.", "We ordered a big pot of marinière mussels.",
    True, "Dual gender shift!")

add(154, "le pendule", "masculine", "B2", "physical pendulum", "DUAL: Meaning-Shift (Masc)", "[luh pahn-DOOL]",
    "DUAL GENDER: Le pendule = swinging weight used in physics or divination.",
    "Le pendule de Foucault démontre la rotation de la Terre.", "Foucault's pendulum demonstrates the rotation of the Earth.")

add(155, "la pendule", "feminine", "B2", "mantel clock / wall clock", "DUAL: Meaning-Shift (Fem)", "[lah pahn-DOOL]",
    "DUAL GENDER: La pendule = decorative household clock.",
    "La pendule du salon sonne les heures avec un carillon mélodieux.", "The living room clock strikes the hours with a melodious chime.",
    True, "Dual gender shift!")

add(156, "le vase", "masculine", "B2", "decorative vase", "DUAL: Meaning-Shift (Masc)", "[luh VAHZ]",
    "DUAL GENDER: Le vase = decorative floral vessel.",
    "Ce délicat vase de porcelaine de Chine date du dix-huitième siècle.", "This delicate Chinese porcelain vase dates from the eighteenth century.")

add(157, "la vase", "feminine", "B2", "mud / river silt", "DUAL: Meaning-Shift (Fem)", "[lah VAHZ]",
    "DUAL GENDER: La vase = wetland silt, mud, or river slime.",
    "Le bateau à fond plat est resté enlisé dans la vase à marée basse.", "The flat-bottomed boat remained bogged down in the mud at low tide.",
    True, "Dual gender shift!")

add(158, "le gratte-ciel", "masculine", "B2", "skyscraper", "MASC: Verb+Noun Compound", "[luh graht-SYEHL]",
    "Rule: Verb (gratter) + Noun (ciel) = ALWAYS MASCULINE!",
    "Ce nouveau gratte-ciel en verre s'élève à plus de trois cents mètres.", "This new glass skyscraper rises over three hundred meters high.")

add(159, "le pare-brise", "masculine", "B2", "windshield", "MASC: Verb+Noun Compound", "[luh pahr-BREEZ]",
    "Rule: Verb (parer) + Noun (brise) = MASCULINE even though brise is feminine!",
    "Un gravillon sur l'autoroute a fendu le pare-brise de ma voiture.", "A gravel stone on the highway cracked my car's windshield.")

add(160, "la crapule", "feminine", "B2", "scoundrel / villain", "HUMAN: Fem noun for Men", "[lah krah-POOL]",
    "Rule: Historical FEMININE noun applied insultingly to a man! Ce type est une crapule.",
    "La police a enfin arrêté cette dangereuse crapule notoire.", "The police finally arrested this notorious dangerous scoundrel.",
    True, "Feminine noun applied to men!")

add(161, "la brute", "feminine", "B2", "brute / bully", "HUMAN: Fem noun for Men", "[lah BROOT]",
    "Rule: FEMININE noun applied to violent men.",
    "Cet individu agressif se comporte comme une véritable brute.", "This aggressive individual behaves like a real brute.",
    True, "Feminine noun applied to men!")

add(162, "le bastion", "masculine", "B2", "bastion / fortress", "TRAP: Masculine in -tion", "[luh bahs-TYOHN]",
    "TRAP: Ends in -tion but is MASCULINE! Root is bastione.",
    "La vieille citadelle servait de bastion défensif imprenable.", "The old citadel served as an impregnable defensive bastion.",
    True, "Rare masculine exception to -tion!")

add(163, "le satellite", "masculine", "B2", "satellite", "TRAP: Masculine in -ite", "[luh sah-tay-LEET]",
    "TRAP: Ends in -ite but is MASCULINE! Orbiting body.",
    "Le satellite de télécommunication a été mis en orbite avec succès.", "The telecommunications satellite was successfully placed into orbit.",
    True, "Masculine exception to feminine -ite!")

add(164, "le murmure", "masculine", "B2", "whisper / murmur", "TRAP: Masculine in -ure", "[luh moor-MOOR]",
    "TRAP: Ends in -ure but is MASCULINE! Whispering sound.",
    "Le doux murmure de la brise dans les feuilles apaisait nos esprits.", "The soft murmur of the breeze in the leaves calmed our minds.",
    True, "Masculine exception to feminine -ure!")

add(165, "l’amour", "masculine", "B2", "love", "SHIFTER: Masc sing, Fem pl", "[lah-MOOR]",
    "GENDER SHIFTER: Masculine in singular (un grand amour), FEMININE in plural (des amours passionnées)!",
    "Ils ont vécu un amour passionné qui a inspiré ce roman.", "They lived a passionate love that inspired this novel.",
    True, "Unique gender shifter in plural!")

add(166, "le délice", "masculine", "B2", "delight", "SHIFTER: Masc sing, Fem pl", "[luh day-LEES]",
    "GENDER SHIFTER: Masculine in singular (un vrai délice), FEMININE in plural (de délicieuses délices)!",
    "Ce dessert au chocolat fondant est un pur délice gastronomique.", "This molten chocolate dessert is pure gastronomic delight.",
    True, "Unique gender shifter in plural!")

add(167, "l’orgue", "masculine", "B2", "pipe organ", "SHIFTER: Masc sing, Fem pl", "[LOHRG]",
    "GENDER SHIFTER: Masculine in singular (un bel orgue), FEMININE in plural (les grandes orgues de Notre-Dame)!",
    "L'organiste joue sur le grand orgue de la cathédrale historique.", "The organist plays on the historic cathedral's great organ.",
    True, "Unique gender shifter in plural!")

add(168, "le chêne", "masculine", "B2", "oak tree", "HOMOPHONE: [ʃɛn] (Masc)", "[luh SHEHN]",
    "HOMOPHONE: Le chêne (oak tree, masc) vs la chaîne (chain/channel, fem).",
    "Ce chêne séculaire a résisté à toutes les tempêtes hivernales.", "This centuries-old oak has withstood all winter storms.")

add(169, "la chaîne", "feminine", "B2", "chain / TV channel", "HOMOPHONE: [ʃɛn] (Fem)", "[lah SHEHN]",
    "HOMOPHONE: Metal chain or broadcast channel (fem).",
    "La chaîne de télévision diffuse un documentaire sur la faune sauvage.", "The television channel broadcasts a documentary on wild fauna.")

add(170, "le péché", "masculine", "B2", "moral sin", "HOMOPHONE: [pe.ʃe] (Masc)", "[luh pay-SHAY]",
    "HOMOPHONE: Le péché (sin, masc) vs le pêcher (peach tree, masc) vs la pêche (peach/fishing, fem).",
    "La gourmandise est parfois considérée avec malice comme un péché mignon.", "Gluttony is sometimes considered with amusement as a minor indulgence / guilty pleasure.")

# ==========================================
# LEVEL C1 / C2: ADVANCED PROFICIENCY & LITERARY NUANCE
# ==========================================
add(171, "l’éloge", "masculine", "C1", "high praise / panegyric", "MASC: Ending -oge", "[lay-LOHZH]",
    "Rule: Suffix -oge is masculine! Speaking high praise.",
    "L'académicien a prononcé un brillant éloge de son prédécesseur.", "The academician delivered a brilliant eulogy in praise of his predecessor.")

add(172, "l’apanage", "masculine", "C1", "prerogative / exclusive right", "MASC: Ending -age", "[lah-pah-NAHZH]",
    "Rule: -age is masculine! Exclusive historical heritage.",
    "La rigueur intellectuelle n'est pas l'apanage des seuls scientifiques.", "Intellectual rigor is not the exclusive preserve of scientists alone.")

add(173, "l’anathème", "masculine", "C1", "anathema / solemn curse", "MASC: Greek in -ème", "[lah-nah-TEHM]",
    "Rule: Greek neuter anathema &rarr; masculine in French!",
    "Le concile a jeté l'anathème sur ces propositions doctrinales hérétiques.", "The council pronounced anathema on these heretical doctrinal propositions.")

add(174, "le mausolée", "masculine", "C1", "mausoleum", "TRAP: Masculine in -ée", "[luh moh-zoh-LAY]",
    "TRAP: Ends in -ée but is MASCULINE! From Greek Mausoleion.",
    "Le mausolée d'Halicarnasse comptait parmi les sept merveilles du monde.", "The Mausoleum at Halicarnassus was numbered among the seven wonders of the ancient world.",
    True, "Masculine Greek -ée trap!")

add(175, "le scarabée", "masculine", "C1", "scarab / sacred beetle", "TRAP: Masculine in -ée", "[luh skah-rah-BAY]",
    "TRAP: Ends in -ée but is MASCULINE! Ancient Egyptian beetle.",
    "Le scarabée sculpté dans la cornaline servait d'amulette protectrice.", "The scarab carved in carnelian served as a protective amulet.",
    True, "Masculine Greek -ée trap!")

add(176, "le colosse", "masculine", "C1", "colossus / giant statue", "TRAP: Masculine in -osse", "[luh koh-LOHS]",
    "TRAP: Ends in -osse but is MASCULINE! The Colossus of Rhodes.",
    "Le colosse de Rhodes surplombait l'entrée majestueuse du port antique.", "The Colossus of Rhodes towered over the majestic entrance of the ancient harbor.",
    True, "Masculine exception to feminine -osse!")

add(177, "le vestibule", "masculine", "C1", "entrance hall / vestibule", "MASC: Ending -ule", "[luh vehs-tee-BOOL]",
    "Rule: Latin vestibulum &rarr; masculine -ule noun!",
    "Les hôtes furent chaleureusement accueillis dès le vaste vestibule d'honneur.", "The guests were warmly received upon entering the vast vestibule of honor.")

add(178, "le parjure", "masculine", "C1", "perjury / oath-breaker", "TRAP: Masculine in -ure", "[luh pahr-ZHOOR]",
    "TRAP: Ends in -ure but is MASCULINE! Latin perjurium.",
    "Témoigner faussement sous serment constitue un crime de parjure.", "Bearing false witness under oath constitutes a crime of perjury.",
    True, "Masculine exception to feminine -ure!")

add(179, "l’effervescence", "feminine", "C1", "effervescence / excitement", "FEM: Ending -ence", "[lay-fehr-veh-SAHNS]",
    "Rule: Abstract state in -ence is feminine!",
    "Une effervescence intellectuelle extraordinaire régnait dans le Paris des années vingt.", "An extraordinary intellectual effervescence reigned in 1920s Paris.")

add(180, "la désuétude", "feminine", "C1", "disuse / obsolescence", "FEM: Ending -tude", "[lah day-zoo-ay-TOOD]",
    "Rule: Suffix -tude (from Latin -tudo) is universally FEMININE!",
    "Cette loi archaïque est progressivement tombée en désuétude au fil des siècles.", "This archaic law gradually fell into disuse over the centuries.")

add(181, "la pérennité", "feminine", "C1", "durability / permanence", "FEM: Ending -té", "[lah pay-reh-nee-TAY]",
    "Rule: Suffix -té is feminine!",
    "Le développement durable vise à assurer la pérennité des écosystèmes fragiles.", "Sustainable development aims to ensure the longevity of fragile ecosystems.")

add(182, "la turpitude", "feminine", "C1", "turpitude / baseness", "FEM: Ending -tude", "[lah toor-pee-TOOD]",
    "Rule: Suffix -tude is feminine!",
    "L'histoire a impitoyablement consigné les turpitudes morales de ce tyran déchu.", "History relentlessly recorded the moral turpitude of this fallen tyrant.")

add(183, "la toison", "feminine", "C1", "fleece / pelt", "FEM: Ending -oison", "[lah twah-ZOHN]",
    "Rule: Suffix -oison (from Latin -onem) is feminine! The Golden Fleece.",
    "Jason et les Argonautes se mirent en quête de la Toison d'or.", "Jason and the Argonauts set out in quest of the Golden Fleece.")

add(184, "la cloison", "feminine", "C1", "partition / dividing wall", "FEM: Ending -oison", "[lah klwah-ZOHN]",
    "Rule: -oison is feminine!",
    "Les ouvriers ont abattu la cloison mitoyenne pour agrandir l'espace de vie.", "The workmen tore down the partition wall to enlarge the living space.")

add(185, "la nef", "feminine", "C1", "nave (church) / ancient ship", "TRAP: Feminine in -f", "[lah NEHF]",
    "TRAP: Ends in -f but is FEMININE! Latin navis.",
    "La nef grandiose de la cathédrale est illuminée par les rayons du couchant.", "The grandiose nave of the cathedral is illuminated by the rays of the setting sun.",
    True, "Rare feminine consonant -f trap!")

add(186, "la poix", "feminine", "C1", "pitch / black tar", "TRAP: Feminine in -x", "[lah PWAH]",
    "TRAP: Ends in -x but is FEMININE! Dense black resin.",
    "Les charpentiers marins utilisaient de la poix pour calfater la coque du navire.", "Shipwrights used pitch to caulk the hull of the vessel.",
    True, "Feminine -x trap!")

add(187, "le mousse", "masculine", "C2", "cabin boy (ship apprentice)", "DUAL: Meaning-Shift (Masc)", "[luh MOOS]",
    "DUAL GENDER: Le mousse = a novice sailor boy on a ship.",
    "Le jeune mousse nettoyait inlassablement le pont sous les ordres du capitaine.", "The young cabin boy tirelessly scrubbed the deck under the captain's orders.")

add(188, "la mousse", "feminine", "C2", "moss / froth / mousse", "DUAL: Meaning-Shift (Fem)", "[lah MOOS]",
    "DUAL GENDER: La mousse = forest bryophyte moss, shaving froth, or chocolate dessert.",
    "Une mousse verte et humide recouvrait les rochers au fond du ravin.", "A green, damp moss blanketed the rocks at the bottom of the ravine.",
    True, "Dual gender shift!")

add(189, "le trompette", "masculine", "C2", "trumpeter (musician)", "DUAL: Meaning-Shift (Masc)", "[luh trohn-PEHT]",
    "DUAL GENDER: Le trompette = the male musician who plays trumpet.",
    "Le premier trompette de l'orchestre a exécuté un solo d'une virtuosité éclatante.", "The orchestra's principal trumpeter performed a dazzlingly virtuosic solo.")

add(190, "la trompette", "feminine", "C2", "trumpet (instrument)", "DUAL: Meaning-Shift (Fem)", "[lah trohn-PEHT]",
    "DUAL GENDER: La trompette = brass musical instrument.",
    "Il nettoie soigneusement les pistons dorés de sa trompette après chaque concert.", "He carefully cleans the golden valves of his trumpet after each concert.",
    True, "Dual gender shift!")

add(191, "le critique", "masculine", "C2", "reviewer / critic (person)", "DUAL: Meaning-Shift (Masc)", "[luh kree-TEEK]",
    "DUAL GENDER: Le critique = the person reviewing art or books.",
    "Le critique littéraire du Figaro a rédigé un article dithyrambique sur ce premier roman.", "The literary critic of Le Figaro wrote a glowing review of this debut novel.")

add(192, "la critique", "feminine", "C2", "review / critique / criticism", "DUAL: Meaning-Shift (Fem)", "[lah kree-TEEK]",
    "DUAL GENDER: La critique = analytical assessment or fault-finding.",
    "La critique élogieuse de la presse a propulsé la pièce au sommet du box-office.", "The laudatory press review propelled the play to the top of the box office.",
    True, "Dual gender shift!")

add(193, "le somme", "masculine", "C2", "nap / short snooze", "DUAL: Meaning-Shift (Masc)", "[luh SOHM]",
    "DUAL GENDER: Le somme = brief sleep (faire un petit somme).",
    "Après un copieux déjeuner dominical, il a fait un petit somme d'une demi-heure.", "After a hearty Sunday lunch, he took a quick half-hour nap.")

add(194, "la somme", "feminine", "C2", "sum / monetary amount", "DUAL: Meaning-Shift (Fem)", "[lah SOHM]",
    "DUAL GENDER: La somme = mathematical total or amount of money.",
    "La somme recueillie lors du gala de charité permettra de rénover l'hospice.", "The sum raised during the charity gala will allow the hospice to be renovated.",
    True, "Dual gender shift!")

add(195, "le mort", "masculine", "C2", "dead person / dummy (bridge)", "DUAL: Meaning-Shift (Masc)", "[luh MOHR]",
    "DUAL GENDER: Le mort = deceased individual or dummy card player.",
    "Le médecin légiste a examiné le corps du mort avec une précision méticuleuse.", "The medical examiner scrutinized the dead man's body with meticulous precision.")

add(196, "la mort", "feminine", "C2", "death (concept/phenomenon)", "DUAL: Meaning-Shift (Fem)", "[lah MOHR]",
    "DUAL GENDER: La mort = physical death (from Latin mors, mortis).",
    "La mort fait partie du cycle naturel et inéluctable de toute existence humaine.", "Death is part of the natural and inescapable cycle of all human existence.",
    True, "Dual gender shift!")

add(197, "le fard", "masculine", "C2", "makeup / cosmetic paint", "HOMOPHONE: [faʁ] (Masc)", "[luh FAHR]",
    "HOMOPHONE: Le fard (makeup, masc) vs le phare (lighthouse/headlight, masc).",
    "L'actrice a retiré son fard de scène avec une lotion démaquillante douce.", "The actress removed her stage makeup with a gentle cleansing lotion.")

add(198, "le phare", "masculine", "C2", "lighthouse / car headlight", "HOMOPHONE: [faʁ] (Masc)", "[luh FAHR]",
    "HOMOPHONE: Le phare (lighthouse) sweeps the ocean at night.",
    "Le faisceau lumineux du phare guide les navires à travers le récif dangereux.", "The lighthouse's beam of light guides ships through the treacherous reef.")

add(199, "l’apothéose", "feminine", "C2", "apotheosis / climax / crowning peak", "FEM: Ending -ose", "[lah-poh-tay-OHZ]",
    "Rule: Ending -ose is feminine! Grand crowning finale.",
    "Le feu d'artifice final constitua l'apothéose spectaculaire du festival d'Avignon.", "The final fireworks display constituted the spectacular climax of the Avignon festival.")

add(200, "l’acrimonie", "feminine", "C2", "acrimony / bitterness of tone", "FEM: Ending -ie", "[lah-kree-moh-NEE]",
    "Rule: Abstract quality in -ie is feminine!",
    "Le débat parlementaire s'est déroulé dans une atmosphère d'une acrimonie déplorable.", "The parliamentary debate unfolded in an atmosphere of deplorable acrimony.")

# Save to vocab_data.py
output_content = f'''# vocab_data.py
# Auto-generated comprehensive master vocabulary dataset for French Noun Gender (A1 -> C2)

ALL_VOCABULARY = {json.dumps(VOCAB_DATABASE, indent=2, ensure_ascii=False)}
'''

with open("/Users/jainamshah/Downloads/Learning French/vocab_data.py", "w") as f:
    f.write(output_content)

print(f"Successfully generated vocab_data.py with {len(VOCAB_DATABASE)} comprehensive entries.")
