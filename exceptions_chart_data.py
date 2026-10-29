# exceptions_chart_data.py
# The Visual Atlas & Master Chart of French Gender Traps and Exceptions
# Each entry features word, translation, deceptive rule, intuitive pronunciation breakdown,
# mnemonic story, bilingual sentence, and a minimalist inline SVG illustration.

EXCEPTIONS_DATABASE = [
    {
        "id": 1,
        "french": "la plage",
        "article": "la",
        "noun": "plage",
        "gender": "feminine",
        "english": "beach",
        "trap_type": "Feminine ending in masculine -age",
        "deceptive_rule": "Nouns in -age are 95% MASCULINE (le fromage, le voyage), but plage is strictly FEMININE!",
        "phonetic": "lah PLAHZH",
        "syllables": "PLAHZH",
        "sound_tip": "Soft 'zh' sound like the 's' in 'measure' or 'vision'. The final 'e' is completely silent.",
        "mnemonic": "Think: Sunbathers relaxing in pink bikinis on LA PLAGE.",
        "example_fr": "Les enfants courent joyeusement sur la plage ensoleillée.",
        "example_en": "The children are running merrily on the sunny beach.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 52c8-4 16-4 24 0s16 4 24 0" stroke="#0284c7" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M8 58c10-3 18-3 28 0s18 3 24 0" stroke="#38bdf8" stroke-width="2" stroke-linecap="round"/>
          <circle cx="48" cy="18" r="8" fill="#f59e0b"/>
          <path d="M32 20l-16 14h32L32 20z" fill="#f43f5e"/>
          <path d="M32 20v28" stroke="#78350f" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 2,
        "french": "la cage",
        "article": "la",
        "noun": "cage",
        "gender": "feminine",
        "english": "cage",
        "trap_type": "Feminine ending in masculine -age",
        "deceptive_rule": "Ends in -age, yet is strictly FEMININE.",
        "phonetic": "lah KAHZH",
        "syllables": "KAHZH",
        "sound_tip": "Rhymes with 'dodge' but with a smooth 'zh' glide.",
        "mnemonic": "A fragile canary sings inside LA CAGE.",
        "example_fr": "L'oiseau apprivoisé chante dans sa petite cage dorée.",
        "example_en": "The tame bird sings in its little golden cage.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="18" y="20" width="28" height="34" rx="4" stroke="#475569" stroke-width="2"/>
          <path d="M25 20v34M32 20v34M39 20v34" stroke="#94a3b8" stroke-width="1.5"/>
          <path d="M22 20c0-6 4.5-10 10-10s10 4 10 10" stroke="#475569" stroke-width="2"/>
          <circle cx="32" cy="7" r="3" stroke="#475569" stroke-width="1.5"/>
        </svg>"""
    },
    {
        "id": 3,
        "french": "l’image",
        "article": "l’ (la)",
        "noun": "image",
        "gender": "feminine",
        "english": "image / picture",
        "trap_type": "Feminine ending in masculine -age",
        "deceptive_rule": "Ends in -age, but is FEMININE (une belle image).",
        "phonetic": "lee-MAHZH",
        "syllables": "ee • MAHZH",
        "sound_tip": "Stress on the second syllable: 'ee' + 'MAHZH'.",
        "mnemonic": "A vivid imagination paints a colorful feminine picture.",
        "example_fr": "Cette image en noir et blanc capture l'émotion du moment.",
        "example_en": "This black and white picture captures the emotion of the moment.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="12" y="14" width="40" height="36" rx="3" stroke="#64748b" stroke-width="2.5" fill="#f8fafc"/>
          <circle cx="24" cy="26" r="4" fill="#fbbf24"/>
          <path d="M16 44l12-14 8 8 6-6 10 12H16z" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1.5"/>
        </svg>"""
    },
    {
        "id": 4,
        "french": "la page",
        "article": "la",
        "noun": "page (of a book)",
        "gender": "feminine",
        "english": "page",
        "trap_type": "Feminine ending in masculine -age",
        "deceptive_rule": "Ends in -age, yet is strictly FEMININE.",
        "phonetic": "lah PAHMZ",
        "syllables": "PAHZH",
        "sound_tip": "'ah' vowel like 'father' + 'zh'.",
        "mnemonic": "Turn to LA PAGE dix to read the story.",
        "example_fr": "J'ai corné le coin de la page pour ne pas perdre ma lecture.",
        "example_en": "I dog-eared the corner of the page so as not to lose my place.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 12h20l12 12v28H18V12z" stroke="#475569" stroke-width="2.5" fill="#ffffff"/>
          <path d="M38 12v12h12" stroke="#475569" stroke-width="2" fill="#e2e8f0"/>
          <path d="M24 28h16M24 36h16M24 44h10" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 5,
        "french": "l’horloge",
        "article": "l’ (la)",
        "noun": "horloge",
        "gender": "feminine",
        "english": "clock",
        "trap_type": "Feminine ending in masculine -oge",
        "deceptive_rule": "Ends in -oge (like l'éloge, masc), but l'horloge is FEMININE!",
        "phonetic": "lohr-LOHZH",
        "syllables": "ohr • LOHZH",
        "sound_tip": "Silent 'h'! Say 'ohr' + 'LOHZH'. Deep round 'oh'.",
        "mnemonic": "The clock on the wall ticks away the hours (l'heure is also fem!).",
        "example_fr": "L'horloge du grand salon sonne les douze coups de minuit.",
        "example_en": "The grandfather clock strikes the twelve chimes of midnight.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="32" r="22" stroke="#475569" stroke-width="2.5" fill="#ffffff"/>
          <circle cx="32" cy="32" r="2.5" fill="#0f172a"/>
          <path d="M32 32V20M32 32l8 5" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
          <path d="M32 10v3M32 51v3M10 32h3M51 32h3" stroke="#94a3b8" stroke-width="2"/>
        </svg>"""
    },
    {
        "id": 6,
        "french": "la main",
        "article": "la",
        "noun": "main",
        "gender": "feminine",
        "english": "hand",
        "trap_type": "Feminine ending in masculine -ain",
        "deceptive_rule": "Nouns in -ain are masculine (le pain, le train), but la main is FEMININE (Latin manus, 4th declension fem).",
        "phonetic": "lah MAN",
        "syllables": "MAN",
        "sound_tip": "Nasal 'an' like 'can' through the nose; do NOT pronounce the 'n' consonant!",
        "mnemonic": "A woman's delicate hand (la main) wearing a wedding ring.",
        "example_fr": "Elle a tendu la main pour saluer son nouvel invité.",
        "example_en": "She extended her hand to greet her new guest.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M22 36V22a3 3 0 016 0v12M28 22V16a3 3 0 016 0v18M34 18a3 3 0 016 0v16M40 22a3 3 0 016 0v16c0 8-6 16-16 16s-14-6-14-14v-6a3 3 0 016 0v4" stroke="#e11d48" stroke-width="2.2" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 7,
        "french": "l’eau",
        "article": "l’ (la)",
        "noun": "eau",
        "gender": "feminine",
        "english": "water",
        "trap_type": "Feminine ending in masculine -eau",
        "deceptive_rule": "Nouns in -eau are masculine (le bateau, le château), but l'eau is strictly FEMININE (Latin aqua).",
        "phonetic": "LOH",
        "syllables": "LOH",
        "sound_tip": "Sounds identically to the English word 'low'.",
        "mnemonic": "Life-giving water (l'eau) and human skin (la peau) are nature's feminine pair.",
        "example_fr": "Un verre d'eau fraîche est indispensable après l'effort physique.",
        "example_en": "A glass of cold water is essential after physical exercise.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M32 10c0 0-14 18-14 28a14 14 0 0028 0c0-10-14-28-14-28z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
          <path d="M26 34a7 7 0 007 7" stroke="#bae6fd" stroke-width="2" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 8,
        "french": "la peau",
        "article": "la",
        "noun": "peau",
        "gender": "feminine",
        "english": "skin",
        "trap_type": "Feminine ending in masculine -eau",
        "deceptive_rule": "Ends in -eau, yet is strictly FEMININE.",
        "phonetic": "lah POH",
        "syllables": "POH",
        "sound_tip": "Sounds identically to 'Poe' (as in Edgar Allan Poe).",
        "mnemonic": "Soft feminine skin protected with lotion.",
        "example_fr": "Cette crème hydrate intensément la peau sèche en hiver.",
        "example_en": "This cream intensely hydrates dry skin in winter.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="28" r="16" stroke="#e11d48" stroke-width="2.2" fill="#fff1f2"/>
          <path d="M20 54c4-8 10-10 12-10s8 2 12 10" stroke="#e11d48" stroke-width="2.2" stroke-linecap="round"/>
          <path d="M26 28s2 2 6 2 6-2 6-2" stroke="#fb7185" stroke-width="1.8" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 9,
        "french": "la dent",
        "article": "la",
        "noun": "dent",
        "gender": "feminine",
        "english": "tooth",
        "trap_type": "Feminine ending in masculine -ent",
        "deceptive_rule": "Ends in consonant cluster -ent (like l'argent, le vent), but is FEMININE (Latin dens).",
        "phonetic": "lah DAHN",
        "syllables": "DAHN",
        "sound_tip": "Nasal 'dahn' like 'haunt' through the nose. The final 't' is completely silent!",
        "mnemonic": "Dentist drills a cavity in a white feminine tooth.",
        "example_fr": "L'enfant montre fièrement sa première dent tombée.",
        "example_en": "The child proudly shows his first lost tooth.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 18c0-6 6-6 12-4 6-2 12-2 12 4 0 10-4 18-4 32-1 0-4-12-8-12s-7 12-8 12c0-14-4-22-4-32z" fill="#ffffff" stroke="#475569" stroke-width="2.5"/>
        </svg>"""
    },
    {
        "id": 10,
        "french": "la nuit",
        "article": "la",
        "noun": "nuit",
        "gender": "feminine",
        "english": "night",
        "trap_type": "Feminine ending in consonant -t",
        "deceptive_rule": "Consonant -t terminations default to masculine, but la nuit is FEMININE (Latin nox, noctis).",
        "phonetic": "lah NWEE",
        "syllables": "NWEE",
        "sound_tip": "'Nwee' in one syllable. The final 't' is completely silent!",
        "mnemonic": "The famous proverb: 'La nuit, tous les chats sont gris.'",
        "example_fr": "La nuit était silencieuse et baignée par la lueur des étoiles.",
        "example_en": "The night was quiet and bathed in the glow of the stars.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M38 12a18 18 0 1014 26 20 20 0 01-14-26z" fill="#312e81" stroke="#4338ca" stroke-width="2"/>
          <circle cx="20" cy="18" r="1.5" fill="#fbbf24"/>
          <circle cx="16" cy="30" r="1.5" fill="#fbbf24"/>
          <circle cx="26" cy="44" r="1.5" fill="#fbbf24"/>
        </svg>"""
    },
    {
        "id": 11,
        "french": "la forêt",
        "article": "la",
        "noun": "forêt",
        "gender": "feminine",
        "english": "forest",
        "trap_type": "Feminine ending in consonant -êt",
        "deceptive_rule": "Ends in consonant -t, yet is strictly FEMININE.",
        "phonetic": "lah foh-REH",
        "syllables": "foh • REH",
        "sound_tip": "'foh' + open 'reh' like 'red'. The 't' is silent!",
        "mnemonic": "Mother Nature's deep green enchanted forest.",
        "example_fr": "Une promenade vivifiante dans la forêt apaise l'esprit.",
        "example_en": "An invigorating walk in the forest calms the mind.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M22 46l10-18 10 18H22zM12 52l10-14 10 14H12zM32 52l10-14 10 14H32z" fill="#15803d" stroke="#166534" stroke-width="1.8"/>
          <path d="M32 46v6" stroke="#78350f" stroke-width="2.5"/>
        </svg>"""
    },
    {
        "id": 12,
        "french": "la mer",
        "article": "la",
        "noun": "mer",
        "gender": "feminine",
        "english": "sea / ocean",
        "trap_type": "Feminine ending in masculine -er",
        "deceptive_rule": "Nouns in -er are predominantly masculine (le fer, le verger), but la mer is FEMININE (Latin mare).",
        "phonetic": "lah MEHR",
        "syllables": "MEHR",
        "sound_tip": "Open 'eh' sound with rolled/throaty French 'r'.",
        "mnemonic": "The French call the sea 'La Grande Bleue' (feminine blue).",
        "example_fr": "Le voilier fend les vagues agitées de la mer Méditerranée.",
        "example_en": "The sailboat cuts through the rough waves of the Mediterranean Sea.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 38c8-6 16 6 24 0s16-6 24 0" stroke="#0284c7" stroke-width="3" stroke-linecap="round"/>
          <path d="M8 48c8-6 16 6 24 0s16-6 24 0" stroke="#0369a1" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M28 26l8-12v12h-8z" fill="#f43f5e"/>
          <path d="M24 26h16l-3 4H27l-3-4z" fill="#475569"/>
        </svg>"""
    },
    {
        "id": 13,
        "french": "la fin",
        "article": "la",
        "noun": "fin",
        "gender": "feminine",
        "english": "end / finale",
        "trap_type": "Feminine ending in masculine -in",
        "deceptive_rule": "Nouns in -in are masculine (le vin, le jardin), but la fin is FEMININE (Latin finis).",
        "phonetic": "lah FAN",
        "syllables": "FAN",
        "sound_tip": "Nasal 'an' like 'can' through the nose; do not say the 'n'!",
        "mnemonic": "The famous screen banner at the close of vintage French films: 'FIN' (la fin).",
        "example_fr": "La fin du roman a surpris tous les lecteurs par son audace.",
        "example_en": "The end of the novel surprised all readers with its audacity.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="12" y="16" width="40" height="32" rx="4" fill="#0f172a" stroke="#334155" stroke-width="2"/>
          <text x="32" y="37" fill="#fbbf24" font-family="'Playfair Display', serif" font-weight="bold" font-size="14" text-anchor="middle">FIN</text>
        </svg>"""
    },
    {
        "id": 14,
        "french": "la souris",
        "article": "la",
        "noun": "souris",
        "gender": "feminine",
        "english": "mouse (animal & computer)",
        "trap_type": "Feminine ending in masculine -is",
        "deceptive_rule": "Nouns in -is are masculine (le devis, le croquis), but la souris is FEMININE.",
        "phonetic": "lah soo-REE",
        "syllables": "soo • REE",
        "sound_tip": "'soo' as in soup + 'ree'. The final 's' is completely silent!",
        "mnemonic": "A tiny mouse squeaks before clicking the computer mouse.",
        "example_fr": "Je clique deux fois avec la souris sans fil de mon bureau.",
        "example_en": "I double-click with my desk's wireless mouse.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="22" y="14" width="20" height="36" rx="10" stroke="#475569" stroke-width="2.2" fill="#ffffff"/>
          <path d="M32 14v12" stroke="#94a3b8" stroke-width="2"/>
          <path d="M32 10V6" stroke="#475569" stroke-width="1.8" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 15,
        "french": "la vis",
        "article": "la",
        "noun": "vis",
        "gender": "feminine",
        "english": "screw (hardware)",
        "trap_type": "Feminine ending in masculine -is",
        "deceptive_rule": "Ends in -is, yet is strictly FEMININE.",
        "phonetic": "lah VEES",
        "syllables": "VEES",
        "sound_tip": "Unlike souris, here the final 's' IS pronounced: 'VEES' like geese with a 'v'.",
        "mnemonic": "Fasten the hinge with a small feminine screw.",
        "example_fr": "Serre fermement la vis pour maintenir solidement l'étagère.",
        "example_en": "Tighten the screw firmly to hold the shelf securely.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="24" y="10" width="16" height="6" rx="2" fill="#64748b"/>
          <path d="M28 16v34l4 6 4-6V16H28z" fill="#94a3b8" stroke="#475569" stroke-width="2"/>
          <path d="M28 24l8-4M28 32l8-4M28 40l8-4" stroke="#475569" stroke-width="1.8"/>
        </svg>"""
    },
    {
        "id": 16,
        "french": "la voix",
        "article": "la",
        "noun": "voix",
        "gender": "feminine",
        "english": "voice",
        "trap_type": "Feminine ending in masculine -x",
        "deceptive_rule": "Nouns in -x are masculine (le choix, le prix), but la voix is FEMININE (Latin vox).",
        "phonetic": "lah VWAH",
        "syllables": "VWAH",
        "sound_tip": "'Vwah' like 'voyage' without the yage. Final 'x' is silent!",
        "mnemonic": "The soprano sings with a golden operatic voice.",
        "example_fr": "Sa voix douce et mélodieuse a captivé l'ensemble de l'auditoire.",
        "example_en": "Her sweet and melodious voice captivated the entire audience.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="26" y="14" width="12" height="22" rx="6" fill="#e11d48"/>
          <path d="M20 28a12 12 0 0024 0M32 40v12M24 52h16" stroke="#475569" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 17,
        "french": "la paix",
        "article": "la",
        "noun": "paix",
        "gender": "feminine",
        "english": "peace",
        "trap_type": "Feminine ending in masculine -x",
        "deceptive_rule": "Ends in -x, but is FEMININE (Latin pax).",
        "phonetic": "lah PEH",
        "syllables": "PEH",
        "sound_tip": "Open 'peh' rhyming with 'bed' without the 'd'. Final 'x' is silent!",
        "mnemonic": "The dove of peace bringing harmony to the world.",
        "example_fr": "Les traités diplomatiques visent à préserver la paix mondiale.",
        "example_en": "Diplomatic treaties aim to preserve world peace.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M16 36c6-10 16-16 28-14-4 6-4 14 0 20-8 0-16-2-28-6z" fill="#ffffff" stroke="#0284c7" stroke-width="2.2"/>
          <path d="M44 22c2-4 6-6 10-6" stroke="#16a34a" stroke-width="2" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 18,
        "french": "la clé (clef)",
        "article": "la",
        "noun": "clé",
        "gender": "feminine",
        "english": "key",
        "trap_type": "Feminine ending in consonant -f / -é",
        "deceptive_rule": "Hard consonants default to masculine, but la clé is FEMININE (Latin clavis).",
        "phonetic": "lah KLAY",
        "syllables": "KLAY",
        "sound_tip": "Sounds identically to the English name 'Clay'.",
        "mnemonic": "Turn the golden key in the lock of the door.",
        "example_fr": "N'oublie pas de prendre la clé avant de fermer la porte.",
        "example_en": "Don't forget to take the key before closing the door.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="22" cy="32" r="10" stroke="#f59e0b" stroke-width="2.5" fill="none"/>
          <path d="M32 32h22v6M46 32v4" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 19,
        "french": "le silence",
        "article": "le",
        "noun": "silence",
        "gender": "masculine",
        "english": "silence",
        "trap_type": "Masculine ending in feminine -ence",
        "deceptive_rule": "Nouns in -ence are overwhelmingly FEMININE (la présence, la différence), but le silence is MASCULINE!",
        "phonetic": "luh see-LAHNS",
        "syllables": "see • LAHNS",
        "sound_tip": "'see' + deep nasal 'LAHNS'. The golden silence.",
        "mnemonic": "Silence is golden, and in French, silence is MASCULINE!",
        "example_fr": "Un silence solennel s'est abattu sur la salle d'audience.",
        "example_en": "A solemn silence fell over the courtroom.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M16 26h8l12-10v32L24 38h-8V26z" fill="#475569"/>
          <path d="M42 24l12 16M54 24L42 40" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 20,
        "french": "le musée",
        "article": "le",
        "noun": "musée",
        "gender": "masculine",
        "english": "museum",
        "trap_type": "Masculine ending in feminine -ée",
        "deceptive_rule": "Nouns in -ée are feminine (la journée, l'idée), but le musée is MASCULINE (from Greek mouseion).",
        "phonetic": "luh mew-ZAY",
        "syllables": "mew • ZAY",
        "sound_tip": "Round lips tightly saying 'ee' to produce French 'u' &rarr; 'mew' + 'ZAY'.",
        "mnemonic": "The famous Louvre is LE MUSÉE le plus visité du monde.",
        "example_fr": "Le musée d'Orsay abrite des chefs-d'œuvre impressionnistes majeurs.",
        "example_en": "The Orsay museum houses major Impressionist masterpieces.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 24l20-10 20 10H12z" fill="#4f46e5"/>
          <path d="M16 24v22M26 24v22M38 24v22M48 24v22" stroke="#4338ca" stroke-width="2"/>
          <rect x="10" y="46" width="44" height="6" fill="#1e1b4b"/>
        </svg>"""
    },
    {
        "id": 21,
        "french": "le lycée",
        "article": "le",
        "noun": "lycée",
        "gender": "masculine",
        "english": "high school",
        "trap_type": "Masculine ending in feminine -ée",
        "deceptive_rule": "Ends in -ée, yet is strictly MASCULINE (Greek lykeion).",
        "phonetic": "luh lee-SAY",
        "syllables": "lee • SAY",
        "sound_tip": "'lee' + 'SAY' like 'say' in English.",
        "mnemonic": "French teenagers attend LE LYCÉE before university.",
        "example_fr": "Mon fils aîné prépare son baccalauréat au lycée Victor-Hugo.",
        "example_en": "My eldest son is preparing for his baccalaureate at Victor Hugo high school.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M32 14L10 24l22 10 22-10-22-10z" fill="#4f46e5"/>
          <path d="M46 29v14M18 29v12c0 8 6 12 14 12s14-4 14-12V29" stroke="#312e81" stroke-width="2" fill="none"/>
        </svg>"""
    },
    {
        "id": 22,
        "french": "le squelette",
        "article": "le",
        "noun": "squelette",
        "gender": "masculine",
        "english": "skeleton",
        "trap_type": "Masculine ending in feminine -ette",
        "deceptive_rule": "Nouns in -ette are feminine (la bicyclette, la fourchette), but le squelette is MASCULINE (bones are tough!).",
        "phonetic": "luh skuh-LEHT",
        "syllables": "skuh • LEHT",
        "sound_tip": "Rhymes with 'net' or 'bet': 'skuh' + 'LEHT'.",
        "mnemonic": "The anatomy teacher hung LE SQUELETTE in the laboratory.",
        "example_fr": "Le squelette humain est composé de deux cent six os distincts.",
        "example_en": "The human skeleton is composed of two hundred and six distinct bones.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="18" r="8" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
          <circle cx="29" cy="18" r="1.5" fill="#0f172a"/>
          <circle cx="35" cy="18" r="1.5" fill="#0f172a"/>
          <path d="M32 26v22M24 32h16M26 38h12M28 44h8M32 48l-8 10M32 48l8 10" stroke="#475569" stroke-width="2.2" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 23,
        "french": "le bonheur",
        "article": "le",
        "noun": "bonheur",
        "gender": "masculine",
        "english": "happiness",
        "trap_type": "Masculine ending in abstract -eur",
        "deceptive_rule": "Abstract nouns in -eur are feminine (la chaleur, la peur), but le bonheur is MASCULINE (bon + heur).",
        "phonetic": "luh boh-NUHR",
        "syllables": "boh • NUHR",
        "sound_tip": "'boh' + 'nuhr' rhyming with 'purr' or 'fur'.",
        "mnemonic": "True happiness (le bonheur) and good fortune.",
        "example_fr": "Le vrai bonheur se trouve souvent dans les plaisirs simples du quotidien.",
        "example_en": "True happiness is often found in the simple pleasures of daily life.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M32 50s-16-10-16-22a10 10 0 0116-8 10 10 0 0116 8c0 12-16 22-16 22z" fill="#f43f5e"/>
          <circle cx="32" cy="20" r="12" fill="#fbbf24" opacity="0.3"/>
        </svg>"""
    },
    {
        "id": 24,
        "french": "le parapluie",
        "article": "le",
        "noun": "parapluie",
        "gender": "masculine",
        "english": "umbrella",
        "trap_type": "Masculine ending in feminine -ie",
        "deceptive_rule": "Nouns in -ie are feminine (la vie, la pharmacie), but le parapluie is MASCULINE because it is a verb compound (parer + la pluie).",
        "phonetic": "luh pah-rah-PLWEE",
        "syllables": "pah • rah • PLWEE",
        "sound_tip": "'PLWEE' rhyming with 'free' with a 'w' glide.",
        "mnemonic": "Open LE PARAPLUIE to shield against the falling rain.",
        "example_fr": "N'oublie pas ton parapluie car le ciel s'assombrit rapidement.",
        "example_en": "Don't forget your umbrella because the sky is darkening quickly.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 36c0-12 9-20 20-20s20 8 20 20H12z" fill="#0284c7" stroke="#0369a1" stroke-width="2"/>
          <path d="M32 16v30a4 4 0 01-8 0" stroke="#78350f" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 25,
        "french": "le Mexique",
        "article": "le",
        "noun": "Mexique",
        "gender": "masculine",
        "english": "Mexico",
        "trap_type": "Masculine country ending in silent -e",
        "deceptive_rule": "Countries ending in -e are feminine (la France, l'Italie), but le Mexique is MASCULINE!",
        "phonetic": "luh mehk-SEEK",
        "syllables": "mehk • SEEK",
        "sound_tip": "'mehk' + 'SEEK' like 'seek' in English.",
        "mnemonic": "One of the famous 6 masculine -e countries (along with Cambodge, Mozambique, Zimbabwe, Zaïre, Bélize).",
        "example_fr": "Le Mexique possède un patrimoine archéologique précolombien exceptionnel.",
        "example_en": "Mexico possesses exceptional pre-Columbian archaeological heritage.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 50h40L44 26H20L12 50z" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
          <rect x="26" y="18" width="12" height="8" fill="#b45309"/>
          <path d="M28 50V36h8v14" fill="#78350f"/>
        </svg>"""
    },
    {
        "id": 26,
        "french": "le problème",
        "article": "le",
        "noun": "problème",
        "gender": "masculine",
        "english": "problem",
        "trap_type": "Masculine Greek neuter in -ème",
        "deceptive_rule": "Ends in silent -e, but is MASCULINE from ancient Greek neuter in -ma (problema).",
        "phonetic": "luh proh-BLEHM",
        "syllables": "proh • BLEHM",
        "sound_tip": "'proh' + 'BLEHM' rhyming with 'hem' or 'gem'.",
        "mnemonic": "No problem! Say 'Pas de problème' (problème is always masculine).",
        "example_fr": "Nous avons analysé ce problème complexe sous tous ses angles.",
        "example_en": "We analyzed this complex problem from all angles.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="32" r="22" stroke="#4f46e5" stroke-width="2.5" fill="#eef2ff"/>
          <text x="32" y="42" fill="#4338ca" font-family="'Playfair Display', serif" font-weight="bold" font-size="28" text-anchor="middle">?</text>
        </svg>"""
    },
    {
        "id": 27,
        "french": "le système",
        "article": "le",
        "noun": "système",
        "gender": "masculine",
        "english": "system",
        "trap_type": "Masculine Greek neuter in -ème",
        "deceptive_rule": "Ends in -e, but is MASCULINE from Greek systema.",
        "phonetic": "luh sees-TEHM",
        "syllables": "sees • TEHM",
        "sound_tip": "'sees' + 'TEHM' rhyming with 'stem'.",
        "mnemonic": "Greek scientific systems are MASCULINE.",
        "example_fr": "Ce nouveau système solaire miniature est fascinant à observer.",
        "example_en": "This new miniature solar system is fascinating to observe.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="28" cy="28" r="10" stroke="#0284c7" stroke-width="2.5" fill="none"/>
          <circle cx="42" cy="40" r="7" stroke="#0ea5e9" stroke-width="2" fill="none"/>
          <path d="M28 14v4M28 38v4M14 28h4M38 28h4" stroke="#0284c7" stroke-width="2"/>
        </svg>"""
    },
    {
        "id": 28,
        "french": "le bastion",
        "article": "le",
        "noun": "bastion",
        "gender": "masculine",
        "english": "bastion / stronghold",
        "trap_type": "Masculine ending in -tion",
        "deceptive_rule": "Nouns in -tion are 99% feminine, but le bastion is MASCULINE (Italian bastione).",
        "phonetic": "luh bahs-TYOHN",
        "syllables": "bahs • TYOHN",
        "sound_tip": "Nasal 'tyohn'. A stone fortress bastion.",
        "mnemonic": "A masculine stone fortress standing against enemy attack.",
        "example_fr": "La vieille forteresse médiévale servait de dernier bastion de défense.",
        "example_en": "The old medieval fortress served as the last bastion of defense.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M14 50V24l8-4v30M42 50V20l8 4v26M22 28h20v22H22V28z" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
          <path d="M28 50V38h8v12" fill="#1e293b"/>
        </svg>"""
    },
    {
        "id": 29,
        "french": "la maison",
        "article": "la",
        "noun": "maison",
        "gender": "feminine",
        "english": "house / home",
        "trap_type": "Feminine ending in masculine -on",
        "deceptive_rule": "Nouns in -on are predominantly masculine (le salon, le pont), but la maison is FEMININE (Latin mansio).",
        "phonetic": "lah may-ZOHN",
        "syllables": "may • ZOHN",
        "sound_tip": "'may' + nasal 'ZOHN' like 'zone' through the nose.",
        "mnemonic": "Home sweet home: LA MAISON de famille.",
        "example_fr": "Notre maison de campagne possède un vaste verger de pommiers.",
        "example_en": "Our country house possesses a vast apple orchard.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M32 14L12 30h8v20h24V30h8L32 14z" fill="#fee2e2" stroke="#e11d48" stroke-width="2.2"/>
          <rect x="28" y="38" width="8" height="12" fill="#e11d48"/>
          <rect x="38" y="20" width="4" height="6" fill="#94a3b8"/>
        </svg>"""
    },
    {
        "id": 30,
        "french": "la chanson",
        "article": "la",
        "noun": "chanson",
        "gender": "feminine",
        "english": "song",
        "trap_type": "Feminine ending in masculine -on",
        "deceptive_rule": "Ends in -on, yet is strictly FEMININE (Latin cantio).",
        "phonetic": "lah shahn-SOHN",
        "syllables": "shahn • SOHN",
        "sound_tip": "Two nasal vowels: 'shahn' + 'SOHN'.",
        "mnemonic": "Singing a melodious French chanson d'amour.",
        "example_fr": "Elle fredonne une chanson entraînante tout en cuisinant.",
        "example_en": "She hums a catchy song while cooking.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="22" cy="46" r="6" fill="#ec4899"/>
          <circle cx="44" cy="38" r="6" fill="#ec4899"/>
          <path d="M28 46V20l22-8v26" stroke="#db2777" stroke-width="3"/>
          <path d="M28 20l22-8" stroke="#db2777" stroke-width="4"/>
        </svg>"""
    },
    {
        "id": 31,
        "french": "la boisson",
        "article": "la",
        "noun": "boisson",
        "gender": "feminine",
        "english": "drink / beverage",
        "trap_type": "Feminine ending in masculine -on",
        "deceptive_rule": "Ends in -on, yet is strictly FEMININE.",
        "phonetic": "lah bwah-SOHN",
        "syllables": "bwah • SOHN",
        "sound_tip": "'bwah' (like 'boire') + nasal 'SOHN'.",
        "mnemonic": "A refreshing feminine beverage on a hot summer terrace.",
        "example_fr": "Le café sert une boisson fraîche à base de menthe et de citron.",
        "example_en": "The café serves a chilled beverage made of mint and lemon.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M20 16h24l-4 36H24L20 16z" stroke="#0284c7" stroke-width="2.2" fill="#e0f2fe"/>
          <path d="M36 10l-4 12" stroke="#f43f5e" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 32,
        "french": "la saison",
        "article": "la",
        "noun": "saison",
        "gender": "feminine",
        "english": "season",
        "trap_type": "Feminine ending in masculine -on",
        "deceptive_rule": "Ends in -on, yet is strictly FEMININE (Latin satio).",
        "phonetic": "lah say-ZOHN",
        "syllables": "say • ZOHN",
        "sound_tip": "'say' + nasal 'ZOHN'.",
        "mnemonic": "The four seasons (les quatre saisons) of the turning year.",
        "example_fr": "L'automne est une saison magnifique aux couleurs flamboyantes.",
        "example_en": "Autumn is a magnificent season with flamboyant colors.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="32" r="14" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
          <path d="M32 10v6M32 48v6M10 32h6M48 32h6" stroke="#f59e0b" stroke-width="2.5" stroke-linecap="round"/>
        </svg>"""
    },
    {
        "id": 33,
        "french": "le comité",
        "article": "le",
        "noun": "comité",
        "gender": "masculine",
        "english": "committee",
        "trap_type": "Masculine ending in feminine -té",
        "deceptive_rule": "Nouns in -té are feminine (la liberté, la vérité), but le comité is MASCULINE!",
        "phonetic": "luh koh-mee-TAY",
        "syllables": "koh • mee • TAY",
        "sound_tip": "'koh' + 'mee' + 'TAY'.",
        "mnemonic": "The steering committee (le comité) meets in the boardroom.",
        "example_fr": "Le comité scientifique a validé les conclusions de cette étude.",
        "example_en": "The scientific committee validated the conclusions of this study.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="14" y="24" width="36" height="20" rx="3" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
          <circle cx="22" cy="18" r="3" fill="#4f46e5"/>
          <circle cx="32" cy="18" r="3" fill="#4f46e5"/>
          <circle cx="42" cy="18" r="3" fill="#4f46e5"/>
        </svg>"""
    },
    {
        "id": 34,
        "french": "le traité",
        "article": "le",
        "noun": "traité",
        "gender": "masculine",
        "english": "treaty",
        "trap_type": "Masculine ending in feminine -té",
        "deceptive_rule": "Ends in -té, yet is MASCULINE (past participle noun derivative).",
        "phonetic": "luh tray-TAY",
        "syllables": "tray • TAY",
        "sound_tip": "'tray' + 'TAY'.",
        "mnemonic": "Diplomats sign a formal peace treaty (le traité).",
        "example_fr": "Le traité de Versailles a marqué un tournant géopolitique majeur.",
        "example_en": "The Treaty of Versailles marked a major geopolitical turning point.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M18 14h28v36H18V14z" stroke="#475569" stroke-width="2" fill="#ffffff"/>
          <path d="M24 24h16M24 32h16M24 40h10" stroke="#94a3b8" stroke-width="1.8"/>
          <circle cx="40" cy="42" r="4" fill="#dc2626"/>
        </svg>"""
    },
    {
        "id": 35,
        "french": "la crapule",
        "article": "la",
        "noun": "crapule",
        "gender": "feminine",
        "english": "scoundrel / crook (applied to men)",
        "trap_type": "Feminine noun applied to a male person",
        "deceptive_rule": "Grammatically FEMININE even when describing a villainous man!",
        "phonetic": "lah krah-POOL",
        "syllables": "krah • POOL",
        "sound_tip": "'krah' + 'POOL' like swimming pool.",
        "mnemonic": "Historical feminine insult for a corrupt male villain.",
        "example_fr": "Ce malfaiteur sans scrupules est une crapule de la pire espèce.",
        "example_en": "This unscrupulous criminal is a scoundrel of the worst kind.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <circle cx="32" cy="32" r="18" fill="#1e293b"/>
          <rect x="18" y="26" width="28" height="10" rx="3" fill="#ffffff"/>
          <circle cx="26" cy="31" r="2.5" fill="#0f172a"/>
          <circle cx="38" cy="31" r="2.5" fill="#0f172a"/>
        </svg>"""
    },
    {
        "id": 36,
        "french": "le Cambodge",
        "article": "le",
        "noun": "Cambodge",
        "gender": "masculine",
        "english": "Cambodia",
        "trap_type": "Masculine country ending in silent -e",
        "deceptive_rule": "Ends in -e, but is MASCULINE!",
        "phonetic": "luh kahn-BOHDZH",
        "syllables": "kahn • BOHDZH",
        "sound_tip": "Nasal 'kahn' + 'BOHDZH' with soft 'zh'.",
        "mnemonic": "Ancient Angkor Wat rises in LE CAMBODGE.",
        "example_fr": "Le Cambodge attire des voyageurs du monde entier pour ses temples.",
        "example_en": "Cambodia attracts travelers from all over the world for its temples.",
        "svg": """<svg viewBox="0 0 64 64" width="48" height="48" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M16 48h32M24 48V28l8-10 8 10v20M32 18v30" stroke="#4f46e5" stroke-width="2.2" stroke-linecap="round"/>
        </svg>"""
    }
]
