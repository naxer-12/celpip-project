import urllib.parse
import json

cards = [
    # Section 1: Salutations, Formules de Politesse & Premiers Contacts (1-15)
    {
        "num": 1,
        "french": "le bonjour",
        "english": "Hello / Good morning / Greeting",
        "pronunciation": "luh bohn-ZHOOR",
        "audio_query": "le bonjour",
        "gender": "Masculine (m.)",
        "sentence": "Bonjour madame, je m'appelle Thomas. *(Hello ma'am, my name is Thomas.)*",
        "plural_or_conj": "les bonjours *(regular)*",
        "liaison_notes": "Pronounced [bɔ̃ʒuʁ]. No liaison. **Teacher's Trap:** Never use 'bon après-midi' to greet someone; 'bonjour' is used all day until evening!"
    },
    {
        "num": 2,
        "french": "le bonsoir",
        "english": "Good evening",
        "pronunciation": "luh bohn-SWAHR",
        "audio_query": "le bonsoir",
        "gender": "Masculine (m.)",
        "sentence": "Bonsoir tout le monde, comment allez-vous ? *(Good evening everyone, how are you?)*",
        "plural_or_conj": "les bonsoirs *(regular)*",
        "liaison_notes": "Pronounced [bɔ̃swaʁ]. No liaison. Switch from 'bonjour' to 'bonsoir' starting around 18:00 (6 PM)."
    },
    {
        "num": 3,
        "french": "le salut",
        "english": "Hi / Bye (informal greeting)",
        "pronunciation": "luh sah-LYOO",
        "audio_query": "salut",
        "gender": "Masculine (m.)",
        "sentence": "Salut Alex ! Tu vas bien aujourd'hui ? *(Hi Alex! Are you doing well today?)*",
        "plural_or_conj": "les saluts *(noun) / Invariable (greeting)*",
        "liaison_notes": "Pronounced [saly]. **Silent final 't'**—never pronounce the 't'! Strictly for friends and peers."
    },
    {
        "num": 4,
        "french": "au revoir",
        "english": "Goodbye",
        "pronunciation": "oh ruh-VWAHR (often oh-rvwahr)",
        "audio_query": "au revoir",
        "gender": "N/A (Expression)",
        "sentence": "Merci pour votre accueil et au revoir ! *(Thank you for your welcome and goodbye!)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "In fast spoken French, the 'e' drops: [oʁvwaʁ]. Universal polite standard farewell."
    },
    {
        "num": 5,
        "french": "enchanté / enchantée",
        "english": "Nice to meet you / Delighted",
        "pronunciation": "ahn-shahn-TAY",
        "audio_query": "enchanté",
        "gender": "Adjective (m. / f.)",
        "sentence": "— Je m'appelle Claire. — Enchantée, Claire ! *(— My name is Claire. — Nice to meet you, Claire!)*",
        "plural_or_conj": "enchantés (m. pl.) / enchantées (f. pl.)",
        "liaison_notes": "Both genders sound identical [ɑ̃ʃɑ̃te]. Feminine adds silent '-e' in writing. No liaison."
    },
    {
        "num": 6,
        "french": "s'il vous plaît",
        "english": "Please (formal / plural)",
        "pronunciation": "seel voo PLEH",
        "audio_query": "s'il vous plaît",
        "gender": "N/A (Expression)",
        "sentence": "Un café et l'addition, s'il vous plaît. *(A coffee and the check, please.)*",
        "plural_or_conj": "Informal: s'il te plaît [seel tuh pleh]",
        "liaison_notes": "Silent final 't' in plaît [sil vu plɛ]. Liaison: 's'il‿vous' [sil-vu]. Circumflex on 'î' is historic."
    },
    {
        "num": 7,
        "french": "merci beaucoup",
        "english": "Thank you very much",
        "pronunciation": "mair-SEE boh-KOO",
        "audio_query": "merci beaucoup",
        "gender": "N/A (Expression)",
        "sentence": "Merci beaucoup pour votre aide précieuse. *(Thank you very much for your precious help.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Final 'p' in beaucoup is strictly silent [boku]. Never say 'beaucou-p'."
    },
    {
        "num": 8,
        "french": "comment allez-vous ?",
        "english": "How are you? (formal / plural)",
        "pronunciation": "koh-mahn-tah-lay-VOO",
        "audio_query": "comment allez-vous ?",
        "gender": "N/A (Expression / Verb)",
        "sentence": "Bonjour Monsieur Dupuis, comment allez-vous ? *(Good morning Mr. Dupuis, how are you?)*",
        "plural_or_conj": "Conjugation (aller): je vais, tu vas, il va, nous allons, vous allez, ils vont",
        "liaison_notes": "**Mandatory [t] liaison:** pronounced `comman-t-allez-vous` [kɔmɑ̃.t‿ale.vu]. High-priority exam test point!"
    },
    {
        "num": 9,
        "french": "ça va",
        "english": "How are things? / I'm fine",
        "pronunciation": "sah VAH",
        "audio_query": "ça va",
        "gender": "N/A (Idiom)",
        "sentence": "— Ça va ? — Oui, ça va très bien, merci ! *(— How's it going? — Yes, it's going very well, thanks!)*",
        "plural_or_conj": "Invariable (from verb aller)",
        "liaison_notes": "The cedilla (ç) produces soft [s] before 'a'. Without it, 'ca' would sound like 'ka'."
    },
    {
        "num": 10,
        "french": "la bienvenue",
        "english": "Welcome",
        "pronunciation": "lah byan-vuh-NYOO",
        "audio_query": "la bienvenue",
        "gender": "Feminine (f.)",
        "sentence": "Je vous souhaite la bienvenue à Paris ! *(I welcome you to Paris!)*",
        "plural_or_conj": "les bienvenues",
        "liaison_notes": "**Gender Alert:** As a standalone noun, it is strictly feminine (*la bienvenue*). Nasal [bjɛ̃] + [vny]."
    },
    {
        "num": 11,
        "french": "comment vous appelez-vous ?",
        "english": "What is your name? (formal)",
        "pronunciation": "koh-mahn voo-zah-play-VOO",
        "audio_query": "comment vous appelez-vous ?",
        "gender": "N/A (Expression / Verb)",
        "sentence": "Bonjour, entrez. Comment vous appelez-vous ? *(Hello, come in. What is your name?)*",
        "plural_or_conj": "Conjugates s'appeler with vous",
        "liaison_notes": "**Mandatory [z] liaison:** `vous‿appelez` [vu-z-aple-vu]. Notice single 'l' in 'appelez'."
    },
    {
        "num": 12,
        "french": "comment t'appelles-tu ?",
        "english": "What is your name? (informal)",
        "pronunciation": "koh-mahn tah-pel-TYOO",
        "audio_query": "comment t'appelles-tu ?",
        "gender": "N/A (Expression / Verb)",
        "sentence": "Salut ! Moi c'est Léo. Et toi, comment t'appelles-tu ? *(Hi! I'm Leo. And you, what's your name?)*",
        "plural_or_conj": "Conjugates s'appeler with tu",
        "liaison_notes": "Elision: `te` + `appelles` = `t'appelles` [ta.pɛl]. Notice double 'l' and silent final '-es'."
    },
    {
        "num": 13,
        "french": "je vous présente...",
        "english": "I introduce to you... / May I introduce...",
        "pronunciation": "zhuh voo pray-ZAHNT",
        "audio_query": "je vous présente",
        "gender": "N/A (Expression / Verb)",
        "sentence": "Je vous présente mon collègue Pierre. *(May I introduce to you my coworker Pierre.)*",
        "plural_or_conj": "Conjugation (présenter): je présente, tu présentes, il présente, nous présentons, vous présentez, ils présentent",
        "liaison_notes": "Pronounced [ʒə vu pʁezɑ̃t]. For friends/informal, use `je te présente...`."
    },
    {
        "num": 14,
        "french": "voici / voilà",
        "english": "Here is / There is (introducing)",
        "pronunciation": "vwah-SEE / vwah-LAH",
        "audio_query": "voici voilà",
        "gender": "N/A (Prepositions)",
        "sentence": "Voici ma collègue Marie, et voilà votre bureau. *(Here is my colleague Marie, and there is your desk.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "'Voici' points to what is near or being introduced; 'voilà' points to what is slightly further or just stated."
    },
    {
        "num": 15,
        "french": "à bientôt",
        "english": "See you soon",
        "pronunciation": "ah byan-TOH",
        "audio_query": "à bientôt",
        "gender": "N/A (Expression)",
        "sentence": "Merci pour la soirée, à bientôt ! *(Thanks for the evening, see you soon!)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Silent final 't' in bientôt [bjɛ̃to]. Grave accent on `à` distinguishes it from verb `a` (has)."
    },

    # Section 2: Noms, Identité & Sujets (16-28)
    {
        "num": 16,
        "french": "le prénom",
        "english": "First name / Given name",
        "pronunciation": "luh pray-NOHN",
        "audio_query": "le prénom",
        "gender": "Masculine (m.)",
        "sentence": "Mon prénom est Lucas et mon nom est Dupont. *(My first name is Lucas and my last name is Dupont.)*",
        "plural_or_conj": "les prénoms *(regular)*",
        "liaison_notes": "Nasal vowel [ɔ̃]. **False Friend:** 'prénom' = FIRST name; 'nom' = LAST name!"
    },
    {
        "num": 17,
        "french": "le nom",
        "english": "Last name / Surname / Family name",
        "pronunciation": "luh NOHN",
        "audio_query": "le nom",
        "gender": "Masculine (m.)",
        "sentence": "Quel est votre nom de famille, s'il vous plaît ? *(What is your last name, please?)*",
        "plural_or_conj": "les noms *(regular)*",
        "liaison_notes": "Nasal vowel [ɔ̃], silent 'm'. On administrative forms, 'Nom' always means surname."
    },
    {
        "num": 18,
        "french": "le surnom",
        "english": "Nickname",
        "pronunciation": "luh soor-NOHN",
        "audio_query": "le surnom",
        "gender": "Masculine (m.)",
        "sentence": "Mon vrai nom est Nicolas, mais mon surnom est Nico. *(My real name is Nicolas, but my nickname is Nico.)*",
        "plural_or_conj": "les surnoms *(regular)*",
        "liaison_notes": "**False Friend:** 'surnom' does NOT mean surname (last name); it strictly means nickname!"
    },
    {
        "num": 19,
        "french": "s'appeler",
        "english": "To be called / To be named",
        "pronunciation": "sah-puh-LAY",
        "audio_query": "s'appeler",
        "gender": "N/A (Reflexive Verb)",
        "sentence": "Je m'appelle Sarah et mes frères s'appellent Luc et Marc. *(My name is Sarah and my brothers are named Luc and Marc.)*",
        "plural_or_conj": "je m'appelle, tu t'appelles, il s'appelle, nous nous appelons, vous vous appelez, ils s'appellent",
        "liaison_notes": "**Spelling Change:** Doubles 'l' (`-ell-`) before silent endings, but keeps single 'l' with `nous` and `vous`! Liaison: `nous‿nous appelons` [nu-nu-z-aplɔ̃]."
    },
    {
        "num": 20,
        "french": "être",
        "english": "To be",
        "pronunciation": "EH-truh",
        "audio_query": "être",
        "gender": "N/A (Irregular Verb)",
        "sentence": "Je suis ravi de faire votre connaissance. *(I am delighted to make your acquaintance.)*",
        "plural_or_conj": "je suis, tu es, il est, nous sommes, vous êtes, ils sont",
        "liaison_notes": "**Essential Liaisons:** `vous‿êtes` [vu-z-ɛt] (mandatory [z]); `c'est‿un` [sɛ-t-œ̃] (mandatory [t]). **Trap:** contrast `ils sont` [il sɔ̃] with `ils ont` [il-z-ɔ̃]."
    },
    {
        "num": 21,
        "french": "la personne",
        "english": "Person",
        "pronunciation": "lah pair-SUHN",
        "audio_query": "la personne",
        "gender": "Feminine (f.)",
        "sentence": "Cette personne est très aimable avec nous. *(This person is very kind to us.)*",
        "plural_or_conj": "les personnes *(regular)*",
        "liaison_notes": "**Gender Alert:** Always feminine, even when referring to a man (*'Jean est une bonne personne'*). Double 'n' opens the 'o' [pɛʁsɔn]."
    },
    {
        "num": 22,
        "french": "l'homme",
        "english": "Man",
        "pronunciation": "LUHM",
        "audio_query": "l'homme",
        "gender": "Masculine (m.)",
        "sentence": "Cet homme s'appelle Monsieur Robert. *(This man is named Mr. Robert.)*",
        "plural_or_conj": "les hommes [lay-ZOHM]",
        "liaison_notes": "Mute 'h' (*h muet*): requires elision (`l'homme`) and mandatory **[z] liaison** in plural (`les‿hommes` [le-z-ɔm])."
    },
    {
        "num": 23,
        "french": "la femme",
        "english": "Woman / Wife",
        "pronunciation": "lah FAHM",
        "audio_query": "la femme",
        "gender": "Feminine (f.)",
        "sentence": "C'est une femme dynamique ; c'est la femme de Paul. *(She is a dynamic woman; she is Paul's wife.)*",
        "plural_or_conj": "les femmes *(regular)*",
        "liaison_notes": "**Pronunciation Trap:** Spelled with 'e' but pronounced [fam] ('fahm'). Means both 'woman' and 'wife'."
    },
    {
        "num": 24,
        "french": "le garçon",
        "english": "Boy",
        "pronunciation": "luh gahr-SOHN",
        "audio_query": "le garçon",
        "gender": "Masculine (m.)",
        "sentence": "Le petit garçon a huit ans. *(The little boy is eight years old.)*",
        "plural_or_conj": "les garçons *(regular)*",
        "liaison_notes": "Cedilla (ç) ensures [s] sound before 'o'. In modern France, never call a waiter 'garçon' (say 'monsieur')."
    },
    {
        "num": 25,
        "french": "la fille",
        "english": "Girl / Daughter",
        "pronunciation": "lah FEEY",
        "audio_query": "la fille",
        "gender": "Feminine (f.)",
        "sentence": "Ma fille s'appelle Juliette et elle a dix ans. *(My daughter is named Juliette and she is ten years old.)*",
        "plural_or_conj": "les filles *(regular)*",
        "liaison_notes": "Pronounced [fij] with glide [j]. Means 'girl' (une fille) or 'daughter' (ma fille)."
    },
    {
        "num": 26,
        "french": "l'ami (m.) / l'amie (f.)",
        "english": "Friend (male / female)",
        "pronunciation": "lah-MEE",
        "audio_query": "l'ami",
        "gender": "Masculine / Feminine",
        "sentence": "Thomas est mon ami et Claire est mon amie. *(Thomas is my friend and Claire is my friend.)*",
        "plural_or_conj": "les amis (m. pl.) / les amies (f. pl.)",
        "liaison_notes": "Mandatory **[z] liaison** in plural: `les‿amis` [le-z-ami]. **Possessive Rule:** Use masculine `mon` before vowel feminine nouns: `mon amie` [mɔ̃-n-ami] ([n] bridge)."
    },
    {
        "num": 27,
        "french": "le collègue / la collègue",
        "english": "Colleague / Coworker",
        "pronunciation": "luh koh-LEG / lah koh-LEG",
        "audio_query": "le collègue",
        "gender": "Epicene (m. / f.)",
        "sentence": "Je déjeune avec une collègue de travail. *(I am having lunch with a coworker.)*",
        "plural_or_conj": "les collègues *(regular)*",
        "liaison_notes": "Epicene noun: spelling doesn't change; only the article marks gender (`un collègue` / `une collègue`)."
    },
    {
        "num": 28,
        "french": "le monsieur",
        "english": "Gentleman / Sir / Mr.",
        "pronunciation": "luh muh-SYUH",
        "audio_query": "monsieur",
        "gender": "Masculine (m.)",
        "sentence": "Bonjour monsieur, comment allez-vous ? *(Good day sir, how are you?)*",
        "plural_or_conj": "**les messieurs** [lay may-SYUH] *(Irregular!)*",
        "liaison_notes": "**Irregular Pronunciation:** Singular is [məsjø] (never pronounce 'r' or 'n'). Plural changes prefix to `mes-` [mesjø]."
    },

    # Section 3: Âge & Nombres (29-42)
    {
        "num": 29,
        "french": "l'âge",
        "english": "Age",
        "pronunciation": "LAZH",
        "audio_query": "l'âge",
        "gender": "Masculine (m.)",
        "sentence": "Quel est votre âge exact ? *(What is your exact age?)*",
        "plural_or_conj": "les âges [lay-ZAHZH]",
        "liaison_notes": "**Gender Alert:** Masculine despite ending in -e (nouns ending in *-age* are almost all masculine). Plural [z] liaison."
    },
    {
        "num": 30,
        "french": "avoir",
        "english": "To have",
        "pronunciation": "ah-VWAHR",
        "audio_query": "avoir",
        "gender": "N/A (Irregular Verb)",
        "sentence": "J'ai vingt-cinq ans et j'ai deux enfants. *(I am 25 years old and I have two children.)*",
        "plural_or_conj": "j'ai, tu as, il a, nous avons, vous avez, ils ont",
        "liaison_notes": "**#1 Anglophone Trap:** Use **avoir** for age, NEVER être (*'J'ai 20 ans'*, NOT *'Je suis 20'*). Liaisons: `nous‿avons` [nu-z-avɔ̃], `vous‿avez` [vu-z-ave], `ils‿ont` [il-z-ɔ̃]."
    },
    {
        "num": 31,
        "french": "l'an",
        "english": "Year (unit of age/time)",
        "pronunciation": "LAHN",
        "audio_query": "un an",
        "gender": "Masculine (m.)",
        "sentence": "Mon fils a un an et ma fille a quatre ans. *(My son is one year old and my daughter is four years old.)*",
        "plural_or_conj": "les ans",
        "liaison_notes": "You **must** say 'ans' with age: *'J'ai 30 ans'*, never *'J'ai 30'*. Liaisons: `un‿an` [œ̃-n-ɑ̃] ([n] bridge), `deux‿ans` [dø-z-ɑ̃] ([z] bridge)."
    },
    {
        "num": 32,
        "french": "l'année",
        "english": "Year (duration / span of time)",
        "pronunciation": "lah-NAY",
        "audio_query": "l'année",
        "gender": "Feminine (f.)",
        "sentence": "Je passe une année formidable à Lyon. *(I am spending a wonderful year in Lyon.)*",
        "plural_or_conj": "les années [lay-zah-NAY]",
        "liaison_notes": "Difference: `an` is a count/age unit (masculine); `année` is the lived experience/duration (feminine)."
    },
    {
        "num": 33,
        "french": "l'anniversaire",
        "english": "Birthday / Anniversary",
        "pronunciation": "lah-nee-vair-SAIR",
        "audio_query": "l'anniversaire",
        "gender": "Masculine (m.)",
        "sentence": "C'est mon anniversaire aujourd'hui ! *(It's my birthday today!)*",
        "plural_or_conj": "les anniversaires [lay-zah-nee-vair-SAIR]",
        "liaison_notes": "**Gender Alert:** Masculine ending in -e. Elision: `l'anniversaire`. Liaison: `Joyeux‿anniversaire !` [ʒwa.jø.z‿a.ni.vɛʁ.sɛʁ] ([z] bridge)."
    },
    {
        "num": 34,
        "french": "la date de naissance",
        "english": "Date of birth",
        "pronunciation": "lah daht duh neh-SAHNS",
        "audio_query": "la date de naissance",
        "gender": "Feminine (f.)",
        "sentence": "Ma date de naissance est le 14 juillet. *(My date of birth is July 14th.)*",
        "plural_or_conj": "les dates de naissance",
        "liaison_notes": "French dates take masculine definite article `le`: *le 14 juillet* (use cardinal numbers, except *le premier*)."
    },
    {
        "num": 35,
        "french": "quel âge as-tu ? / quel âge avez-vous ?",
        "english": "How old are you? (informal / formal)",
        "pronunciation": "kel AHZH ah-TYOO / kel AHZH ah-vay-VOO",
        "audio_query": "quel âge avez-vous ?",
        "gender": "N/A (Question / Expression)",
        "sentence": "Excusez-moi madame, quel âge avez-vous ? *(Excuse me ma'am, how old are you?)*",
        "plural_or_conj": "Uses verb avoir in inversion",
        "liaison_notes": "Enchaînement & Liaison: `quel‿âge` [kɛ-laʒ], `âge‿avez-vous` [a-ʒa-ve-vu]."
    },
    {
        "num": 36,
        "french": "dix-huit",
        "english": "Eighteen (18)",
        "pronunciation": "deez-WEET",
        "audio_query": "dix-huit",
        "gender": "N/A (Numeral)",
        "sentence": "En France, on est majeur à dix-huit ans. *(In France, one is an adult at eighteen years old.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Pronounced [di.zɥit] ('x' sounds like [z]). When followed by ans: `dix-huit‿ans` [di-zɥi-t-ɑ̃] with **[t] liaison**!"
    },
    {
        "num": 37,
        "french": "vingt",
        "english": "Twenty (20)",
        "pronunciation": "VA(N) [vɛ̃]",
        "audio_query": "vingt",
        "gender": "N/A (Numeral)",
        "sentence": "Elle a exactement vingt ans. *(She is exactly twenty years old.)*",
        "plural_or_conj": "Invariable (unless multiplied: quatre-vingts)",
        "liaison_notes": "Alone: [vɛ̃] ('gt' silent). Before vowel: `vingt‿ans` [vɛ̃-t-ɑ̃]—**the 't' is sounded as a liaison [t]**!"
    },
    {
        "num": 38,
        "french": "vingt et un",
        "english": "Twenty-one (21)",
        "pronunciation": "va(n)-tay-UH(N) [vɛ̃teœ̃]",
        "audio_query": "vingt et un",
        "gender": "N/A (Numeral)",
        "sentence": "Il a vingt et un ans aujourd'hui. *(He is twenty-one years old today.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Pronounced [vɛ̃.te.œ̃]. **Forbidden Liaison:** Never make a liaison after `et`: say [e] | [œ̃], never *[e-t-œ̃]!"
    },
    {
        "num": 39,
        "french": "trente",
        "english": "Thirty (30)",
        "pronunciation": "TRAHNT [tʁɑ̃t]",
        "audio_query": "trente",
        "gender": "N/A (Numeral)",
        "sentence": "Mon frère aîné a trente ans. *(My older brother is thirty years old.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Pronounced [tʁɑ̃t]. When followed by ans: `trente‿ans` [tʁɑ̃-t-ɑ̃] (mute 'e' drops and 't' links to ans)."
    },
    {
        "num": 40,
        "french": "quarante",
        "english": "Forty (40)",
        "pronunciation": "kah-RAHNT [kaʁɑ̃t]",
        "audio_query": "quarante",
        "gender": "N/A (Numeral)",
        "sentence": "Notre professeur a quarante ans. *(Our teacher is forty years old.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Spelled 'qu' but pronounced [k], NOT English [kw]: [ka.ʁɑ̃t]."
    },
    {
        "num": 41,
        "french": "cinquante",
        "english": "Fifty (50)",
        "pronunciation": "sa(n)-KAHNT [sɛ̃kɑ̃t]",
        "audio_query": "cinquante",
        "gender": "N/A (Numeral)",
        "sentence": "Ma mère a cinquante ans ce mois-ci. *(My mother is fifty years old this month.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "Pronounced [sɛ̃.kɑ̃t]. Nasal [sɛ̃] followed by [kɑ̃t]."
    },
    {
        "num": 42,
        "french": "soixante",
        "english": "Sixty (60)",
        "pronunciation": "swah-SAHNT [swasɑ̃t]",
        "audio_query": "soixante",
        "gender": "N/A (Numeral)",
        "sentence": "Mon oncle va fêter ses soixante ans. *(My uncle is going to celebrate his sixtieth birthday.)*",
        "plural_or_conj": "Invariable",
        "liaison_notes": "**Pronunciation Trap:** The 'x' is pronounced [s], NOT [ks]! Say [swa.sɑ̃t]."
    },

    # Section 4: Nationalités, Pays & Langues (43-60)
    {
        "num": 43,
        "french": "la nationalité",
        "english": "Nationality",
        "pronunciation": "lah nah-syoh-nah-lee-TAY",
        "audio_query": "la nationalité",
        "gender": "Feminine (f.)",
        "sentence": "Quelle est votre nationalité d'origine ? *(What is your original nationality?)*",
        "plural_or_conj": "les nationalités *(regular)*",
        "liaison_notes": "Nouns ending in `-ité` are consistently feminine. Pronounced [na.sjɔ.na.li.te]."
    },
    {
        "num": 44,
        "french": "le pays",
        "english": "Country",
        "pronunciation": "luh pay-EE [pei]",
        "audio_query": "le pays",
        "gender": "Masculine (m.)",
        "sentence": "La France est un très beau pays. *(France is a very beautiful country.)*",
        "plural_or_conj": "**les pays** *(invariable in plural!)*",
        "liaison_notes": "Two distinct syllables: [pe.i]. Plural invariable (ends in -s). Liaison: `des pays‿européens` [pe.i-z-øʁɔpeɛ̃] ([z] bridge)."
    },
    {
        "num": 45,
        "french": "la langue",
        "english": "Language / Tongue",
        "pronunciation": "lah LAHNG [lɑ̃ɡ]",
        "audio_query": "la langue",
        "gender": "Feminine (f.)",
        "sentence": "Je parle deux langues étrangères. *(I speak two foreign languages.)*",
        "plural_or_conj": "les langues *(regular)*",
        "liaison_notes": "Pronounced [lɑ̃ɡ]. Note: specific names of languages are always masculine: *le français, l'anglais, le chinois*."
    },
    {
        "num": 46,
        "french": "habiter",
        "english": "To live / To reside",
        "pronunciation": "ah-bee-TAY",
        "audio_query": "habiter",
        "gender": "N/A (Regular Verb)",
        "sentence": "J'habite à Nice dans le sud de la France. *(I live in Nice in the south of France.)*",
        "plural_or_conj": "j'habite, tu habites, il habite, nous habitons, vous habitez, ils habitent",
        "liaison_notes": "Mute 'h' requires elision (`j'habite`). Mandatory [z] liaisons: `nous‿habitons` [nu-z-abitɔ̃], `vous‿habitez` [vu-z-abite], `ils‿habitent` [il-z-abit]. Silent `-ent`!"
    },
    {
        "num": 47,
        "french": "venir de",
        "english": "To come from (origin / nationality)",
        "pronunciation": "vuh-neer DUH",
        "audio_query": "venir",
        "gender": "N/A (Irregular Verb)",
        "sentence": "Je viens du Canada et elle vient de France. *(I come from Canada and she comes from France.)*",
        "plural_or_conj": "je viens, tu viens, il vient, nous venons, vous venez, ils viennent",
        "liaison_notes": "**Preposition Contractions:** `venir de` + `le` = `du` (*du Canada*); `de` + `la` = `de la` (*de la Chine*); `d'` before vowel (*d'Espagne*); `de` + `les` = `des` (*des États-Unis*). Double 'n' in `ils viennent` [vjɛn]."
    },
    {
        "num": 48,
        "french": "français / française",
        "english": "French (m. / f.)",
        "pronunciation": "frahn-SEH / frahn-SEHZ",
        "audio_query": "français",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Il est français et sa femme est française. *(He is French and his wife is French.)*",
        "plural_or_conj": "français (m. pl. invariable) / françaises (f. pl.)",
        "liaison_notes": "**Capitalization Rule:** Lowercase for adjective (`du vin français`), capital for demonym noun (`un Français`). Masculine silent 's' [fʁɑ̃sɛ]; feminine voiced [z] [fʁɑ̃sɛz]."
    },
    {
        "num": 49,
        "french": "américain / américaine",
        "english": "American (m. / f.)",
        "pronunciation": "ah-may-ree-KA(N) / ah-may-ree-KEN",
        "audio_query": "américain",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Mon ami John est américain ; il vit à Chicago. *(My friend John is American; he lives in Chicago.)*",
        "plural_or_conj": "américains / américaines",
        "liaison_notes": "Masculine nasal [ameʁikɛ̃]; feminine oral vowel + [n] [ameʁikɛn]. Mandatory [t] liaison: `il est‿américain` [i.lɛ.t‿ameʁikɛ̃]."
    },
    {
        "num": 50,
        "french": "canadien / canadienne",
        "english": "Canadian (m. / f.)",
        "pronunciation": "kah-nah-DYA(N) / kah-nah-DYEN",
        "audio_query": "canadien",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Céline Dion est canadienne. *(Céline Dion is Canadian.)*",
        "plural_or_conj": "canadiens / canadiennes",
        "liaison_notes": "Pattern `-ien` [jɛ̃] doubles the 'n' in feminine: `-ienne` [jɛn]. Plural liaison: `les Canadiens‿arrivent` [le kanadjɛ̃-z-aʁiv]."
    },
    {
        "num": 51,
        "french": "anglais / anglaise",
        "english": "English / British (m. / f.)",
        "pronunciation": "ahn-GLEH / ahn-GLEHZ",
        "audio_query": "anglais",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Paul est anglais mais il habite en France. *(Paul is English but he lives in France.)*",
        "plural_or_conj": "anglais (m. pl. invariable) / anglaises (f. pl.)",
        "liaison_notes": "Masculine ends in silent 's' [ɑ̃ɡlɛ] (invariable in plural); feminine ends in voiced [z] sound [ɑ̃ɡlɛz]."
    },
    {
        "num": 52,
        "french": "espagnol / espagnole",
        "english": "Spanish (m. / f.)",
        "pronunciation": "es-pah-NYOHL",
        "audio_query": "espagnol",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Carlos est espagnol et sa sœur est espagnole. *(Carlos is Spanish and his sister is Spanish.)*",
        "plural_or_conj": "espagnols / espagnoles",
        "liaison_notes": "Pronunciation identical for both genders: [ɛspaɲɔl]. Feminine adds silent '-e'."
    },
    {
        "num": 53,
        "french": "allemand / allemande",
        "english": "German (m. / f.)",
        "pronunciation": "ahl-MAHN / ahl-MAHND",
        "audio_query": "allemand",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Hans est allemand et sa femme est allemande. *(Hans is German and his wife is German.)*",
        "plural_or_conj": "allemands / allemandes",
        "liaison_notes": "Masculine has silent 'd' [almɑ̃]; feminine sounds the 'd' [almɑ̃d]. Formal liaison bridge sounds like [t]: `un Allemand‿aimable` [œ̃-n-almɑ̃-t-ɛmabl]."
    },
    {
        "num": 54,
        "french": "italien / italienne",
        "english": "Italian (m. / f.)",
        "pronunciation": "ee-tah-LYA(N) / ee-tah-LYEN",
        "audio_query": "italien",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Ce chef de cuisine est italien. *(This head chef is Italian.)*",
        "plural_or_conj": "italiens / italiennes",
        "liaison_notes": "Suffix `-ien` [jɛ̃] / `-ienne` [jɛn]. Liaison with masculine noun: `un‿Italien` [œ̃-n-italjɛ̃] ([n] bridge)."
    },
    {
        "num": 55,
        "french": "indien / indienne",
        "english": "Indian (m. / f.)",
        "pronunciation": "a(n)-DYA(N) / a(n)-DYEN",
        "audio_query": "indien",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Mon médecin est indien ; son assistante est indienne. *(My doctor is Indian; his assistant is Indian.)*",
        "plural_or_conj": "indiens / indiennes",
        "liaison_notes": "Nasal [ɛ̃djɛ̃] in masculine; oral vowel + [n] [ɛ̃djɛn] in feminine."
    },
    {
        "num": 56,
        "french": "chinois / chinoise",
        "english": "Chinese (m. / f.)",
        "pronunciation": "sheen-WAH / sheen-WAHZ",
        "audio_query": "chinois",
        "gender": "Adjective / Noun (m. / f.)",
        "sentence": "Li Na est chinoise ; elle apprend le français. *(Li Na is Chinese; she is learning French.)*",
        "plural_or_conj": "chinois (m. pl. invariable) / chinoises (f. pl.)",
        "liaison_notes": "Masculine silent 's' [ʃinwa]; feminine voiced [z] [ʃinwaz]. Masculine plural is invariable."
    },
    {
        "num": 57,
        "french": "la France",
        "english": "France",
        "pronunciation": "lah FRAHNS",
        "audio_query": "la France",
        "gender": "Feminine (f.)",
        "sentence": "J'habite en France avec toute ma famille. *(I live in France with my whole family.)*",
        "plural_or_conj": "N/A",
        "liaison_notes": "Countries ending in '-e' are feminine (*la France, l'Espagne*). Preposition: Use `en` for feminine countries (*en France*, never *à la France*)."
    },
    {
        "num": 58,
        "french": "les États-Unis",
        "english": "The United States",
        "pronunciation": "lay-zay-tah-zyoo-NEE",
        "audio_query": "les États-Unis",
        "gender": "Masculine Plural (m. pl.)",
        "sentence": "Mon frère fait ses études aux États-Unis. *(My brother is studying in the United States.)*",
        "plural_or_conj": "Masculine Plural",
        "liaison_notes": "**Mandatory Double Liaison:** pronounced [le.ze.ta.zy.ni] (two [z] bridges!). Preposition is `aux` (*aux États-Unis* [o.ze.ta.zy.ni])."
    },
    {
        "num": 59,
        "french": "le Canada",
        "english": "Canada",
        "pronunciation": "luh kah-nah-DAH",
        "audio_query": "le Canada",
        "gender": "Masculine (m.)",
        "sentence": "Nous partons en vacances au Canada en juillet. *(We are going on vacation to Canada in July.)*",
        "plural_or_conj": "N/A",
        "liaison_notes": "Masculine country (does not end in -e). Preposition: Use `au` (*au Canada* = à + le), never *en Canada*."
    },
    {
        "num": 60,
        "french": "le Japon",
        "english": "Japan",
        "pronunciation": "luh zhah-POHN",
        "audio_query": "le Japon",
        "gender": "Masculine (m.)",
        "sentence": "Mon amie travaille au Japon depuis trois ans. *(My friend has been working in Japan for three years.)*",
        "plural_or_conj": "N/A",
        "liaison_notes": "Masculine country. Preposition: `au Japon` (à + le). Nasal [ɔ̃] in 'Japon'."
    },

    # Section 5: Métiers, Emploi & Activité Professionnelle (61-80)
    {
        "num": 61,
        "french": "la profession",
        "english": "Profession / Occupation",
        "pronunciation": "lah proh-feh-SYOHN",
        "audio_query": "la profession",
        "gender": "Feminine (f.)",
        "sentence": "Quelle est votre profession actuelle ? *(What is your current occupation?)*",
        "plural_or_conj": "les professions *(regular)*",
        "liaison_notes": "Nouns ending in `-sion` / `-tion` are strictly feminine. Pronounced [pʁɔfesjɔ̃]."
    },
    {
        "num": 62,
        "french": "le travail",
        "english": "Work / Job",
        "pronunciation": "luh trah-VEYE [tʁavaj]",
        "audio_query": "le travail",
        "gender": "Masculine (m.)",
        "sentence": "Il commence son nouveau travail demain. *(He starts his new job tomorrow.)*",
        "plural_or_conj": "**les travaux** [lay trah-VOH] *(Major Irregular!)*",
        "liaison_notes": "Singular pronounced [tʁavaj], irregular plural `-aux` pronounced [tʁavo]."
    },
    {
        "num": 63,
        "french": "le métier",
        "english": "Trade / Profession / Craft",
        "pronunciation": "luh may-TYAY",
        "audio_query": "le métier",
        "gender": "Masculine (m.)",
        "sentence": "C'est un métier passionnant d'aider les gens. *(It is an exciting trade to help people.)*",
        "plural_or_conj": "les métiers *(regular)*",
        "liaison_notes": "Suffix `-er` pronounced [e]: [metje] (silent 'r')."
    },
    {
        "num": 64,
        "french": "travailler",
        "english": "To work",
        "pronunciation": "trah-veye-YAY [tʁavaje]",
        "audio_query": "travailler",
        "gender": "N/A (Regular Verb)",
        "sentence": "Je travaille du lundi au vendredi. *(I work Monday through Friday.)*",
        "plural_or_conj": "je travaille, tu travailles, il travaille, nous travaillons, vous travaillez, ils travaillent",
        "liaison_notes": "Regular -er verb. Phonetic: `-ille-` produces glide [aj] [tʁavaje]. Singular forms and 3rd person plural sound identical [tʁavaj]."
    },
    {
        "num": 65,
        "french": "le professeur / la professeure",
        "english": "Teacher / Professor",
        "pronunciation": "luh / lah proh-feh-SUHR",
        "audio_query": "le professeur",
        "gender": "Masculine / Feminine",
        "sentence": "Sophie est professeur de sciences dans un lycée. *(Sophie is a science teacher in a high school.)*",
        "plural_or_conj": "les professeurs / les professeures",
        "liaison_notes": "**#1 Profession Rule:** Do NOT use an article after **être** for jobs: say *'Je suis professeur'*, NOT *'Je suis un professeur'*. Short form: `le/la prof`."
    },
    {
        "num": 66,
        "french": "l'étudiant (m.) / l'étudiante (f.)",
        "english": "Student (higher education)",
        "pronunciation": "lay-tyoo-DYA(N) / lay-tyoo-DYAHNT",
        "audio_query": "l'étudiant",
        "gender": "Masculine / Feminine",
        "sentence": "Lucas est étudiant en droit à Paris. *(Lucas is a law student in Paris.)*",
        "plural_or_conj": "les étudiants / les étudiantes",
        "liaison_notes": "Masculine silent 't' [etydjɑ̃]; feminine pronounced 't' [etydjɑ̃t]. Liaisons: `un‿étudiant` [œ̃-n-etydjɑ̃] ([n] bridge); `les‿étudiants` [le-z-etydjɑ̃] ([z] bridge)."
    },
    {
        "num": 67,
        "french": "le médecin",
        "english": "Doctor / Physician",
        "pronunciation": "luh med-SA(N) [mɛtsɛ̃]",
        "audio_query": "le médecin",
        "gender": "Masculine (m.)",
        "sentence": "Je dois aller voir le médecin ce matin. *(I have to go see the doctor this morning.)*",
        "plural_or_conj": "les médecins *(regular)*",
        "liaison_notes": "Pronunciation: middle 'e' drops in natural speech: [mɛtsɛ̃]. Preposition: Go to a person using `chez` (*chez le médecin*, NOT *à le médecin*)."
    },
    {
        "num": 68,
        "french": "l'infirmier (m.) / l'infirmière (f.)",
        "english": "Nurse (m. / f.)",
        "pronunciation": "la(n)-feer-MYAY / la(n)-feer-MYEHR",
        "audio_query": "l'infirmier",
        "gender": "Masculine / Feminine",
        "sentence": "Marc est infirmier dans un service d'urgence. *(Marc is a nurse in an emergency department.)*",
        "plural_or_conj": "les infirmiers / les infirmières",
        "liaison_notes": "Masculine suffix `-ier` [e] [ɛ̃fiʁmje]; feminine `-ière` [ɛʁ] [ɛ̃fiʁmjɛʁ]. Plural [z] liaison: `les‿infirmiers` [le-z-ɛ̃fiʁmje]."
    },
    {
        "num": 69,
        "french": "l'ingénieur (m.) / l'ingénieure (f.)",
        "english": "Engineer",
        "pronunciation": "la(n)-zhay-NYUHR [ɛ̃ʒenjœʁ]",
        "audio_query": "l'ingénieur",
        "gender": "Masculine / Feminine",
        "sentence": "Mon père est ingénieur civil. *(My father is a civil engineer.)*",
        "plural_or_conj": "les ingénieurs / les ingénieures",
        "liaison_notes": "Elision: `l'ingénieur`. Pronounced [ɛ̃ʒenjœʁ]. Plural liaison: `les‿ingénieurs` [le-z-ɛ̃ʒenjœʁ]."
    },
    {
        "num": 70,
        "french": "l'informaticien / l'informaticienne",
        "english": "Computer scientist / IT specialist",
        "pronunciation": "la(n)-for-mah-tee-SYA(N) / -SYEN",
        "audio_query": "l'informaticien",
        "gender": "Masculine / Feminine",
        "sentence": "Elle travaille comme informaticienne chez Orange. *(She works as an IT specialist at Orange.)*",
        "plural_or_conj": "les informaticiens / les informaticiennes",
        "liaison_notes": "Suffix: masculine nasal `-ien` [ɛ̃fɔʁmatisjɛ̃] vs feminine doubled 'n' `-ienne` [ɛ̃fɔʁmatisjɛn]."
    },
    {
        "num": 71,
        "french": "l'avocat (m.) / l'avocate (f.)",
        "english": "Lawyer / Attorney (also: Avocado)",
        "pronunciation": "lah-voh-KAH / lah-voh-KAHT",
        "audio_query": "l'avocat",
        "gender": "Masculine / Feminine",
        "sentence": "Ma sœur consulte une avocate pour son contrat. *(My sister is consulting a lawyer for her contract.)*",
        "plural_or_conj": "les avocats / les avocates",
        "liaison_notes": "Masculine silent 't' [avɔka]; feminine voiced 't' [avɔkat]. Liaison: `un‿avocat` [œ̃-n-avɔka]. Double meaning: `un avocat` also means the fruit (avocado)!"
    },
    {
        "num": 72,
        "french": "le cuisinier / la cuisinière",
        "english": "Cook / Chef",
        "pronunciation": "luh kwee-zee-NYAY / lah kwee-zee-NYEHR",
        "audio_query": "le cuisinier",
        "gender": "Masculine / Feminine",
        "sentence": "Le cuisinier prépare une délicieuse soupe. *(The cook is preparing a delicious soup.)*",
        "plural_or_conj": "les cuisiniers / les cuisinières",
        "liaison_notes": "Pattern `-ier` [je] / `-ière` [jɛʁ]. Note: `une cuisinière` also means the kitchen stove appliance."
    },
    {
        "num": 73,
        "french": "le serveur / la serveuse",
        "english": "Waiter / Waitress (server)",
        "pronunciation": "luh sair-VUHR / lah sair-VUHZ",
        "audio_query": "le serveur",
        "gender": "Masculine / Feminine",
        "sentence": "La serveuse nous apporte la carte des desserts. *(The waitress brings us the dessert menu.)*",
        "plural_or_conj": "les serveurs / les serveuses",
        "liaison_notes": "Pattern `-eur` -> `-euse`. Feminine pronounced with [z] [sɛʁvøz]."
    },
    {
        "num": 74,
        "french": "le vendeur / la vendeuse",
        "english": "Salesperson / Shop assistant",
        "pronunciation": "luh vahn-DUHR / lah vahn-DUHZ",
        "audio_query": "le vendeur",
        "gender": "Masculine / Feminine",
        "sentence": "Le vendeur conseille bien les clients du magasin. *(The salesperson advises store customers well.)*",
        "plural_or_conj": "les vendeurs / les vendeuses",
        "liaison_notes": "Suffix pattern `-eur` -> `-euse` [vɑ̃dœʁ] / [vɑ̃døz]."
    },
    {
        "num": 75,
        "french": "l'artiste",
        "english": "Artist",
        "pronunciation": "lahr-TEEST [aʁtist]",
        "audio_query": "l'artiste",
        "gender": "Epicene (m. / f.)",
        "sentence": "C'est une jeune artiste très talentueuse. *(She is a very talented young artist.)*",
        "plural_or_conj": "les artistes *(regular)*",
        "liaison_notes": "Epicene noun (identical spelling for m. and f.): `un artiste` / `une artiste`. Liaisons: `un‿artiste` [œ̃-n-aʁtist] ([n] bridge); `les‿artistes` [le-z-aʁtist] ([z] bridge)."
    },
    {
        "num": 76,
        "french": "le bureau",
        "english": "Office / Desk",
        "pronunciation": "luh byoo-ROH [byʁo]",
        "audio_query": "le bureau",
        "gender": "Masculine (m.)",
        "sentence": "Mon bureau se trouve au deuxième étage. *(My office is on the second floor.)*",
        "plural_or_conj": "**les bureaux** *(Irregular: takes -x)*",
        "liaison_notes": "**Irregular Plural:** Words ending in `-eau` take `-x`. Dual meaning: desk (furniture) and office (workplace). Pronounced [byʁo]."
    },
    {
        "num": 77,
        "french": "l'entreprise",
        "english": "Company / Business / Enterprise",
        "pronunciation": "lahn-truh-PREEZ [ɑ̃tʁəpʁiz]",
        "audio_query": "l'entreprise",
        "gender": "Feminine (f.)",
        "sentence": "Elle travaille dans une entreprise informatique. *(She works in an IT company.)*",
        "plural_or_conj": "les entreprises",
        "liaison_notes": "**Gender Alert:** Feminine noun ending in -ise. Mandatory elision: `l'entreprise`. Liaisons: `une‿entreprise` [yn-ɑ̃tʁəpʁiz], `les‿entreprises` [le-z-ɑ̃tʁəpʁiz]."
    },
    {
        "num": 78,
        "french": "être au chômage",
        "english": "To be unemployed",
        "pronunciation": "EH-truh oh shoh-MAHZH",
        "audio_query": "être au chômage",
        "gender": "N/A (Verb phrase)",
        "sentence": "Il est au chômage et recherche un poste. *(He is unemployed and looking for a position.)*",
        "plural_or_conj": "Conjugates verb être + au chômage",
        "liaison_notes": "The noun `le chômage` is masculine. Circumflex on 'o' [ʃomaʒ]."
    },
    {
        "num": 79,
        "french": "être à la retraite",
        "english": "To be retired",
        "pronunciation": "EH-truh ah lah ruh-TRET",
        "audio_query": "être à la retraite",
        "gender": "N/A (Verb phrase)",
        "sentence": "Mes parents sont à la retraite et voyagent beaucoup. *(My parents are retired and travel a lot.)*",
        "plural_or_conj": "Conjugates verb être + à la retraite",
        "liaison_notes": "The noun `la retraite` is feminine. **False Friend:** Never say 'je suis retiré' (retiré = reclusive/isolated)."
    },
    {
        "num": 80,
        "french": "faire des études",
        "english": "To study / To pursue degrees",
        "pronunciation": "FEHR day-zay-TYOOD",
        "audio_query": "faire des études",
        "gender": "N/A (Verb phrase)",
        "sentence": "Julien fait des études de médecine. *(Julien is studying medicine.)*",
        "plural_or_conj": "je fais, tu fais, il fait, nous faisons, vous faites, ils font",
        "liaison_notes": "Mandatory [z] liaison: `des‿études` [de-z-etyd]. The noun `une étude` is feminine."
    },

    # Section 6: Loisirs, Passions, Sports & Temps Libre (81-100)
    {
        "num": 81,
        "french": "le passe-temps",
        "english": "Hobby / Pastime",
        "pronunciation": "luh pahs-TAHN [pastɑ̃]",
        "audio_query": "le passe-temps",
        "gender": "Masculine (m.)",
        "sentence": "La peinture est son passe-temps favori. *(Painting is his favorite pastime.)*",
        "plural_or_conj": "**les passe-temps** *(invariable compound)*",
        "liaison_notes": "Masculine noun. Silent final 's' in temps [pas.tɑ̃]. Compound noun remains invariable in the plural."
    },
    {
        "num": 82,
        "french": "le loisir",
        "english": "Leisure activity / Free-time pursuit",
        "pronunciation": "luh lwah-ZEER [lwaziʁ]",
        "audio_query": "le loisir",
        "gender": "Masculine (m.)",
        "sentence": "Quel est votre loisir préféré pendant le week-end ? *(What is your favorite hobby on the weekend?)*",
        "plural_or_conj": "les loisirs *(frequently plural: mes loisirs)*",
        "liaison_notes": "Pronounced [lwaziʁ]. Plural liaison in context: `ses loisirs‿incluent...` [lwaziʁ-z-ɛ̃kly]."
    },
    {
        "num": 83,
        "french": "aimer",
        "english": "To like / To love",
        "pronunciation": "eh-MAY [eme]",
        "audio_query": "aimer",
        "gender": "N/A (Regular Verb)",
        "sentence": "J'aime écouter de la musique pour me relaxer. *(I like listening to music to relax.)*",
        "plural_or_conj": "j'aime, tu aimes, il aime, nous aimons, vous aimez, ils aiment",
        "liaison_notes": "Mandatory elision: `j'aime` (never *je aime). Mandatory [z] liaisons: `nous‿aimons` [nu-z-ɛmɔ̃], `vous‿aimez` [vu-z-ɛme], `ils‿aiment` [il-z-ɛm]. **Grammar Rule:** Always use definite articles (`le/la/les`) for general likes: *j'aime le jazz*."
    },
    {
        "num": 84,
        "french": "adorer",
        "english": "To adore / To love deeply",
        "pronunciation": "ah-doh-RAY [adɔʁe]",
        "audio_query": "adorer",
        "gender": "N/A (Regular Verb)",
        "sentence": "J'adore voyager et découvrir de nouvelles cultures. *(I love traveling and discovering new cultures.)*",
        "plural_or_conj": "j'adore, tu adores, il adore, nous adorons, vous adorez, ils adorent",
        "liaison_notes": "Elision: `j'adore`. Liaisons: `nous‿adorons` [nu-z-adɔʁɔ̃], `vous‿adorez` [vu-z-adɔʁe], `ils‿adorent` [il-z-adɔʁ]. Stronger enthusiasm than aimer."
    },
    {
        "num": 85,
        "french": "préférer",
        "english": "To prefer",
        "pronunciation": "pray-fay-RAY [pʁefeʁe]",
        "audio_query": "préférer",
        "gender": "N/A (Stem-changing Verb)",
        "sentence": "Je préfère le café au thé le matin. *(I prefer coffee over tea in the morning.)*",
        "plural_or_conj": "je préfère, tu préfères, il préfère, nous préférons, vous préférez, ils préfèrent",
        "liaison_notes": "**Spelling Change Alert:** The acute accent `é` changes to grave `è` before silent syllables (`je préfère`, `ils préfèrent`), but reverts to `é` in `nous préférons` and `vous préférez`!"
    },
    {
        "num": 86,
        "french": "détester",
        "english": "To hate / To detest",
        "pronunciation": "day-tes-TAY [detɛste]",
        "audio_query": "détester",
        "gender": "N/A (Regular Verb)",
        "sentence": "Je déteste courir sous la pluie froide. *(I hate running in the cold rain.)*",
        "plural_or_conj": "je déteste, tu détestes, il déteste, nous détestons, vous détestez, ils détestent",
        "liaison_notes": "Regular -er verb. Followed by an infinitive or noun with definite article: *je déteste le froid*."
    },
    {
        "num": 87,
        "french": "faire",
        "english": "To do / To make / To practice (activities)",
        "pronunciation": "FEHR [fɛʁ]",
        "audio_query": "faire",
        "gender": "N/A (Irregular Verb)",
        "sentence": "Je fais du vélo tous les dimanches matin. *(I ride a bike every Sunday morning.)*",
        "plural_or_conj": "je fais, tu fais, il fait, nous faisons, vous faites, ils font",
        "liaison_notes": "**Irregular 3rd Group:** `nous faisons` is spelled 'ai' but pronounced [fəzɔ̃]! Watch irregular `vous faites` and `ils font`. **Grammar Rule:** Use partitives with faire: `faire du` (m.), `faire de la` (f.), `faire de l'` (vowel), `faire des` (pl.)."
    },
    {
        "num": 88,
        "french": "jouer",
        "english": "To play",
        "pronunciation": "zhoo-AY [ʒwe]",
        "audio_query": "jouer",
        "gender": "N/A (Regular Verb)",
        "sentence": "Tu joues au football ou à la pétanque ? *(Do you play soccer or boules?)*",
        "plural_or_conj": "je joue, tu joues, il joue, nous jouons, vous jouez, ils jouent",
        "liaison_notes": "**#1 Preposition Trap:** <br>• Sports/games: `jouer à` + article -> `jouer au foot`, `jouer aux échecs`. <br>• Instruments: `jouer de` + article -> `jouer du piano`, `jouer de la guitare`."
    },
    {
        "num": 89,
        "french": "le sport",
        "english": "Sport",
        "pronunciation": "luh SPOR [spɔʁ]",
        "audio_query": "le sport",
        "gender": "Masculine (m.)",
        "sentence": "Le sport est excellent pour la santé et le moral. *(Sport is excellent for health and morale.)*",
        "plural_or_conj": "les sports *(regular)*",
        "liaison_notes": "Silent final 't' in singular and '-ts' in plural [spɔʁ]. Never pronounce the 't'!"
    },
    {
        "num": 90,
        "french": "le football (le foot)",
        "english": "Soccer / Football",
        "pronunciation": "luh foot-BOHL (luh FOOT)",
        "audio_query": "le football",
        "gender": "Masculine (m.)",
        "sentence": "Nous regardons un match de football ce soir. *(We are watching a soccer match tonight.)*",
        "plural_or_conj": "Invariable in practice",
        "liaison_notes": "Abbreviated colloquially to `le foot`. Say `jouer au foot` or `faire du foot`."
    },
    {
        "num": 91,
        "french": "le tennis",
        "english": "Tennis",
        "pronunciation": "luh teh-NEES [tenis]",
        "audio_query": "le tennis",
        "gender": "Masculine (m.)",
        "sentence": "Elle joue au tennis trois fois par semaine. *(She plays tennis three times a week.)*",
        "plural_or_conj": "Invariable (ends in -s)",
        "liaison_notes": "**Pronunciation Exception:** The final 's' IS pronounced in 'tennis' [tenis]! Say `jouer au tennis`."
    },
    {
        "num": 92,
        "french": "la natation",
        "english": "Swimming",
        "pronunciation": "lah nah-tah-SYOHN [natasjɔ̃]",
        "audio_query": "la natation",
        "gender": "Feminine (f.)",
        "sentence": "La natation est mon activité sportive préférée. *(Swimming is my favorite athletic activity.)*",
        "plural_or_conj": "les natations *(rarely plural)*",
        "liaison_notes": "Suffix `-tion` is feminine. Collocation: Say `faire de la natation` (never *jouer à la natation)."
    },
    {
        "num": 93,
        "french": "la lecture",
        "english": "Reading",
        "pronunciation": "lah lek-TYOOR [lɛktyʁ]",
        "audio_query": "la lecture",
        "gender": "Feminine (f.)",
        "sentence": "La lecture d'un bon livre m'aide à dormir. *(Reading a good book helps me sleep.)*",
        "plural_or_conj": "les lectures *(regular)*",
        "liaison_notes": "Suffix `-ure` is feminine (*la nature, la culture, la peinture*)."
    },
    {
        "num": 94,
        "french": "lire",
        "english": "To read",
        "pronunciation": "LEER [liʁ]",
        "audio_query": "lire",
        "gender": "N/A (Irregular Verb)",
        "sentence": "Je lis un roman en français tous les mois. *(I read a French novel every month.)*",
        "plural_or_conj": "je lis, tu lis, il lit, nous lisons, vous lisez, ils lisent",
        "liaison_notes": "Irregular 3rd group verb. The stem shifts to `lis-` in plural: `nous lisons` [lizɔ̃], `vous lisez` [lize], `ils lisent` [liz]. Optional [t] liaison: `il lit‿un livre` [i-li-t-œ̃-livʁ]."
    },
    {
        "num": 95,
        "french": "la musique",
        "english": "Music",
        "pronunciation": "lah myoo-ZEEK [myzik]",
        "audio_query": "la musique",
        "gender": "Feminine (f.)",
        "sentence": "J'écoute de la musique classique pour travailler. *(I listen to classical music to work.)*",
        "plural_or_conj": "les musiques",
        "liaison_notes": "Feminine noun. Pronounced [myzik]. Collocation: `écouter de la musique` (uses partitive article)."
    },
    {
        "num": 96,
        "french": "écouter",
        "english": "To listen to",
        "pronunciation": "ay-koo-TAY [ekute]",
        "audio_query": "écouter",
        "gender": "N/A (Regular Verb)",
        "sentence": "Qu'est-ce que tu écoutes comme musique ? *(What kind of music do you listen to?)*",
        "plural_or_conj": "j'écoute, tu écoutes, il écoute, nous écoutons, vous écoutez, ils écoutent",
        "liaison_notes": "Elision: `j'écoute`. Mandatory [z] liaisons: `nous‿écoutons` [nu-z-ekutɔ̃], `vous‿écoutez` [vu-z-ekute], `ils‿écoutent` [il-z-ekut]. **Trap:** Directly transitive; do not add 'à' (*écouter la radio*, not *écouter à la radio)."
    },
    {
        "num": 97,
        "french": "le cinéma",
        "english": "Cinema / Movies",
        "pronunciation": "luh see-nay-MAH [sinema]",
        "audio_query": "le cinéma",
        "gender": "Masculine (m.)",
        "sentence": "On va au cinéma voir un film comique ? *(Shall we go to the movies to see a comedy?)*",
        "plural_or_conj": "les cinémas",
        "liaison_notes": "Contraction: `à` + `le` = `au cinéma`. Colloquially shortened to `le ciné`."
    },
    {
        "num": 98,
        "french": "voyager",
        "english": "To travel",
        "pronunciation": "vwah-yah-ZHAY [vwajaʒe]",
        "audio_query": "voyager",
        "gender": "N/A (Spelling-change Verb)",
        "sentence": "Nous voyageons en train à travers toute la France. *(We travel by train across all of France.)*",
        "plural_or_conj": "je voyage, tu voyages, il voyage, nous voyageons, vous voyagez, ils voyagent",
        "liaison_notes": "**Spelling Change Alert (-ger verbs like manger):** Keep silent 'e' before 'o' in `nous voyageons` to protect soft [ʒ] sound; without 'e', it would sound like [ɡ] ('voyagons')!"
    },
    {
        "num": 99,
        "french": "la cuisine / cuisiner",
        "english": "Cooking, kitchen / To cook",
        "pronunciation": "lah kwee-ZEEN / kwee-zee-NAY",
        "audio_query": "cuisiner",
        "gender": "Feminine (f.) / Verb",
        "sentence": "J'adore cuisiner des plats français pour ma famille. *(I love cooking French dishes for my family.)*",
        "plural_or_conj": "je cuisine, tu cuisines, il cuisine, nous cuisinons, vous cuisinez, ils cuisinent",
        "liaison_notes": "`la cuisine` has three meanings: the kitchen room, culinary tradition (*la cuisine française*), and the action (*faire la cuisine* = to cook). Regular -er verb `cuisiner`."
    },
    {
        "num": 100,
        "french": "le jeu vidéo",
        "english": "Video game",
        "pronunciation": "luh zhuh vee-day-OH [ʒø video]",
        "audio_query": "les jeux vidéo",
        "gender": "Masculine (m.)",
        "sentence": "Mon frère passe ses soirées à jouer aux jeux vidéo. *(My brother spends his evenings playing video games.)*",
        "plural_or_conj": "**les jeux vidéo** *(Irregular plural & invariable modifier!)*",
        "liaison_notes": "**Irregular Plural:** `le jeu` takes `-x` (`les jeux` [le ʒø]). The modifier `vidéo` is an invariable adjective in this compound (never add 's' to vidéo!). Liaison in context: `des jeux‿amusants` [de ʒø-z-amyzɑ̃] ([z] bridge)."
    }
]

print(f"Total cards loaded: {len(cards)}")

# Generate Markdown
md_lines = [
    "# DELF A1 French Master Flashcards: Introductions, Identity, Age, Nationality, Jobs & Hobbies",
    "",
    "> **Teacher's Pronunciation & Grammar System for English Speakers**:",
    "> - **Phonetic Pronunciation**: Intuitive syllable-by-syllable respelling with capitalized stressed syllables (e.g., *luh bohn-ZHOOR*).",
    "> - **Audio Link**: Click **[🔊 Audio]** to hear high-fidelity native pronunciation directly.",
    "> - **Gender**: Marked directly with color/label on every noun card.",
    "> - **Liaisons & Sound Bridges**: **[z]** (from s/x), **[t]** (from t/d), and **[n]** (from nasals). No liaison after **et**.",
    "",
    "| # | French (with Article) | English Meaning | Pronunciation | Audio | Gender | Example Sentence (A1) | Plural / Conjugation Drill | Liaison & Teacher's Notes |",
    "|:--|:----------------------|:----------------|:--------------|:-----:|:------:|:----------------------|:---------------------------|:---------------------------|"
]

for c in cards:
    audio_encoded = urllib.parse.quote(c["audio_query"])
    audio_link = f"[🔊 Audio](https://translate.google.com/?sl=fr&tl=en&text={audio_encoded}&op=translate)"
    row = f"| {c['num']} | **{c['french']}** | {c['english']} | `{c['pronunciation']}` | {audio_link} | {c['gender']} | {c['sentence']} | {c['plural_or_conj']} | {c['liaison_notes']} |"
    md_lines.append(row)

with open("/Users/jainamshah/Downloads/Learning French/French_A1_100_Flashcards_Introductions_Hobbies.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print("Markdown updated successfully.")

# Also generate an exquisite standalone HTML file for browser viewing & 1-click printing to PDF
html_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>DELF A1 French 100 Flashcards - Master Reference</title>
    <style>
        @page {
            size: A4 landscape;
            margin: 12mm 10mm 12mm 10mm;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 20px;
            color: #1e293b;
            background: #f8fafc;
        }
        .header {
            margin-bottom: 24px;
            padding: 20px 24px;
            background: linear-gradient(135deg, #1e3a8a, #3b82f6);
            color: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        h1 { margin: 0 0 8px 0; font-size: 24px; }
        p.subtitle { margin: 0; opacity: 0.9; font-size: 14px; }
        .legend {
            display: flex;
            gap: 16px;
            margin-top: 14px;
            font-size: 12px;
            background: rgba(255,255,255,0.15);
            padding: 8px 14px;
            border-radius: 6px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            font-size: 12px;
        }
        th {
            background: #0f172a;
            color: white;
            text-align: left;
            padding: 10px 8px;
            font-weight: 600;
            letter-spacing: 0.02em;
        }
        td {
            padding: 8px 8px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
            line-height: 1.4;
        }
        tr:nth-child(even) { background: #f8fafc; }
        tr:hover { background: #f1f5f9; }
        .badge {
            display: inline-block;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 600;
        }
        .badge-m { background: #dbeafe; color: #1e40af; }
        .badge-f { background: #fce7f3; color: #9d174d; }
        .badge-v { background: #fef3c7; color: #92400e; }
        .badge-x { background: #e2e8f0; color: #475569; }
        .phonetic {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            background: #f1f5f9;
            color: #0f172a;
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 11px;
            font-weight: 500;
        }
        .audio-btn {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            padding: 3px 7px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 600;
        }
        .audio-btn:hover { background: #1d4ed8; }
        .french-term {
            font-weight: 700;
            font-size: 13px;
            color: #0f172a;
        }
        .trap {
            color: #b91c1c;
            font-weight: 600;
        }
        @media print {
            body { margin: 0; background: white; }
            .header { border-radius: 0; box-shadow: none; padding: 12px 16px; margin-bottom: 12px; }
            .audio-btn { display: none; }
            table { box-shadow: none; }
            th, td { padding: 6px 6px; font-size: 10.5px; }
            tr { page-break-inside: avoid; }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>DELF A1 French 100 Flashcards - Teacher's Master Study Deck</h1>
        <p class="subtitle">Topics: Greetings, Personal Identity, Age, Nationalities, Occupations, and Hobbies</p>
        <div class="legend">
            <span>🔵 Masculine</span>
            <span>🟣 Feminine</span>
            <span>🟡 Verbs / Conjugations</span>
            <span>⚪ Expressions / Numbers</span>
            <span>🔊 Click audio button to hear native pronunciation</span>
        </div>
    </div>
    <table>
        <thead>
            <tr>
                <th style="width: 28px;">#</th>
                <th style="width: 140px;">French (with Article)</th>
                <th style="width: 130px;">English Meaning</th>
                <th style="width: 135px;">Pronunciation</th>
                <th style="width: 60px; text-align: center;">Audio</th>
                <th style="width: 85px;">Gender</th>
                <th style="width: 220px;">Example Sentence (A1)</th>
                <th style="width: 180px;">Plural / Conjugation</th>
                <th>Liaison & Pitfalls</th>
            </tr>
        </thead>
        <tbody>
"""

for c in cards:
    audio_encoded = urllib.parse.quote(c["audio_query"])
    g_class = "badge-x"
    if "Masculine" in c["gender"] and "Feminine" not in c["gender"]:
        g_class = "badge-m"
    elif "Feminine" in c["gender"] and "Masculine" not in c["gender"]:
        g_class = "badge-f"
    elif "Verb" in c["gender"]:
        g_class = "badge-v"

    html_content += f"""            <tr>
                <td>{c['num']}</td>
                <td><span class="french-term">{c['french']}</span></td>
                <td>{c['english']}</td>
                <td><span class="phonetic">{c['pronunciation']}</span></td>
                <td style="text-align: center;">
                    <a class="audio-btn" href="https://translate.google.com/?sl=fr&tl=en&text={audio_encoded}&op=translate" target="_blank">🔊 Listen</a>
                </td>
                <td><span class="badge {g_class}">{c['gender']}</span></td>
                <td>{c['sentence']}</td>
                <td>{c['plural_or_conj']}</td>
                <td>{c['liaison_notes']}</td>
            </tr>\n"""

html_content += """        </tbody>
    </table>
</body>
</html>
"""

with open("/Users/jainamshah/Downloads/Learning French/French_A1_100_Flashcards_Printable.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML printable table generated successfully.")
