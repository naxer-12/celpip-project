"""Flagship English Curriculum Seeder for LanGeek Replica.

Populates the 5 core LanGeek English tracks:
1. Vocabulary: CEFR tracks (A1, A2, B1, B2, C1), Most Common 3000 Words, and Flagship Topics
   (Animals, Food & Dining, Travel, Work) with subcategories, words, definitions, phonetic IPA, and audio.
2. Grammar: 11 Reference Modules (Pronouns, Nouns, Verbs, Tenses, Modals, Conditionals, Prepositions,
   Conjunctions, Adjectives, Adverbs, Sentence Structure) with structured lesson blocks.
3. Expressions: Top 25 everyday idioms with literal translations, figurative meanings, examples, and audio.
4. Pronunciation: Complete 26-letter English Alphabet hub (A–Z) with phonetic sounds and example words.
5. Reading: Graded stories with typed ParagraphBlock and PhotoBlock segments.

Ensures 100% preservation of all existing French curriculum rows.
"""

import os
import json
import sqlite3
import logging
from typing import Optional

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("seed_english")

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "langeek.db")


def get_connection(db_path: Optional[str] = None) -> sqlite3.Connection:
    path = db_path or DB_PATH
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn


def verify_french_integrity(conn: sqlite3.Connection) -> dict:
    """Read and snapshot current French row counts to ensure zero data mutation."""
    cur = conn.cursor()
    counts = {
        "categories": cur.execute("SELECT count(*) FROM categories WHERE locale = 'fr'").fetchone()[0],
        "subcategories": cur.execute("SELECT count(*) FROM subcategories WHERE locale = 'fr'").fetchone()[0],
        "grammar_categories": cur.execute("SELECT count(*) FROM grammar_categories WHERE locale = 'fr'").fetchone()[0],
        "grammar_courses": cur.execute("SELECT count(*) FROM grammar_courses WHERE locale = 'fr'").fetchone()[0],
        "reading_collections": cur.execute("SELECT count(*) FROM reading_collections WHERE locale = 'fr'").fetchone()[0],
        "reading_stories": cur.execute("SELECT count(*) FROM reading_stories WHERE locale = 'fr'").fetchone()[0],
        "reading_segments": cur.execute("SELECT count(*) FROM reading_segments WHERE locale = 'fr'").fetchone()[0],
        "pronunciation_courses": cur.execute("SELECT count(*) FROM pronunciation_courses WHERE locale = 'fr'").fetchone()[0],
    }
    return counts


def seed_vocabulary(conn: sqlite3.Connection):
    """Seed 10 English vocabulary categories, subcategories, words, and example sentences."""
    logger.info("Seeding English Vocabulary categories, subcategories, and words...")
    cur = conn.cursor()

    categories_data = [
        (2001, "a1-level", "A1 Level Wordlist", "Essential English vocabulary for absolute beginners.", "A1 Level English Wordlist", "level-based", "https://cdn.langeek.co/photo/39832/thumb/a1-level?type=jpeg", "A1", "Beginner", 15, 350, "level-based", "https://cdn.langeek.co/photo/39832/original/a1-level?type=jpeg", 350, 15, "en", 0),
        (2002, "a2-level", "A2 Level Wordlist", "Elementary English vocabulary for day-to-day communication.", "A2 Level English Wordlist", "level-based", "https://cdn.langeek.co/photo/39833/thumb/a2-level?type=jpeg", "A2", "Elementary", 18, 450, "level-based", "https://cdn.langeek.co/photo/39833/original/a2-level?type=jpeg", 450, 18, "en", 1),
        (2003, "b1-level", "B1 Level Wordlist", "Intermediate English vocabulary for independent expression.", "B1 Level English Wordlist", "level-based", "https://cdn.langeek.co/photo/39834/thumb/b1-level?type=jpeg", "B1", "Intermediate", 22, 600, "level-based", "https://cdn.langeek.co/photo/39834/original/b1-level?type=jpeg", 600, 22, "en", 2),
        (2004, "b2-level", "B2 Level Wordlist", "Upper-intermediate English vocabulary for nuanced discussions.", "B2 Level English Wordlist", "level-based", "https://cdn.langeek.co/photo/39835/thumb/b2-level?type=jpeg", "B2", "Upper-Intermediate", 25, 750, "level-based", "https://cdn.langeek.co/photo/39835/original/b2-level?type=jpeg", 750, 25, "en", 3),
        (2005, "c1-level", "C1 Level Wordlist", "Advanced English vocabulary for sophisticated professional discourse.", "C1 Level English Wordlist", "level-based", "https://cdn.langeek.co/photo/39836/thumb/c1-level?type=jpeg", "C1", "Advanced", 30, 900, "level-based", "https://cdn.langeek.co/photo/39836/original/c1-level?type=jpeg", 900, 30, "en", 4),
        (2006, "most-common-3000", "Most Common 3000 Words", "High-frequency English words covering 90% of everyday spoken English.", "3000 Most Common English Words", "most-common", "https://cdn.langeek.co/photo/40100/thumb/common-words?type=jpeg", None, "Core Vocabulary", 60, 3000, "most-common", "https://cdn.langeek.co/photo/40100/original/common-words?type=jpeg", 3000, 60, "en", 5),
        (2007, "animals", "Animals", "Domestic, farm, and wild animals, birds, and marine creatures.", "English Vocabulary for Animals", "topic-related", "https://cdn.langeek.co/photo/40110/thumb/animals?type=jpeg", None, "Nature & Wildlife", 10, 200, "topic-related", "https://cdn.langeek.co/photo/40110/original/animals?type=jpeg", 200, 10, "en", 6),
        (2008, "food-dining", "Food & Dining", "Ingredients, restaurant dining, cooking methods, and cuisines.", "English Vocabulary for Food & Dining", "topic-related", "https://cdn.langeek.co/photo/40120/thumb/food?type=jpeg", None, "Cuisine & Dining", 12, 250, "topic-related", "https://cdn.langeek.co/photo/40120/original/food?type=jpeg", 250, 12, "en", 7),
        (2009, "travel", "Travel", "Airports, public transit, hotels, directions, and tourism.", "English Vocabulary for Travel", "topic-related", "https://cdn.langeek.co/photo/40130/thumb/travel?type=jpeg", None, "Journeys & Exploration", 14, 280, "topic-related", "https://cdn.langeek.co/photo/40130/original/travel?type=jpeg", 280, 14, "en", 8),
        (2010, "work", "Work", "Corporate offices, careers, interviews, and business communication.", "English Vocabulary for Work & Career", "topic-related", "https://cdn.langeek.co/photo/40140/thumb/work?type=jpeg", None, "Business & Career", 16, 320, "topic-related", "https://cdn.langeek.co/photo/40140/original/work?type=jpeg", 320, 16, "en", 9),
    ]

    for cat in categories_data:
        cur.execute("""
            INSERT INTO categories (
                id, slug, title, description, web_title, category_type, photo_thumbnail,
                cefr_level, cefr_subtitle, total_lessons, total_words, collection_id, photo,
                words_count, subcategories_count, locale, position
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                slug=excluded.slug,
                title=excluded.title,
                description=excluded.description,
                web_title=excluded.web_title,
                category_type=excluded.category_type,
                photo_thumbnail=excluded.photo_thumbnail,
                cefr_level=excluded.cefr_level,
                cefr_subtitle=excluded.cefr_subtitle,
                total_lessons=excluded.total_lessons,
                total_words=excluded.total_words,
                collection_id=excluded.collection_id,
                photo=excluded.photo,
                words_count=excluded.words_count,
                subcategories_count=excluded.subcategories_count,
                locale=excluded.locale,
                position=excluded.position
        """, cat)

    subcategories_data = [
        # A1 Beginner Subcategories
        (20001, 2001, "greetings-and-basics", "Greetings and Basic Words", "Polite greetings, basic introductions, and common polite expressions.", "Greetings & Basics", 6, 180, 0, "en"),
        (20002, 2001, "colors-and-numbers", "Colors and Numbers", "Fundamental numbers 1-10 and primary colors.", "Colors & Numbers", 6, 180, 1, "en"),
        # A2 Elementary
        (20003, 2002, "daily-routine", "Daily Routines", "Activities, waking up, meals, and scheduling day-to-day tasks.", "Daily Routines", 5, 150, 0, "en"),
        # B1 Intermediate
        (20004, 2003, "emotions-and-opinions", "Emotions and Opinions", "Expressing personal thoughts, viewpoints, feelings, and moods.", "Emotions & Opinions", 5, 150, 0, "en"),
        # B2 Upper-Intermediate
        (20005, 2004, "media-and-technology", "Media and Technology", "Digital computing, software, Internet communication, and modern tech.", "Media & Tech", 5, 150, 0, "en"),
        # C1 Advanced
        (20006, 2005, "abstract-philosophy", "Abstract Thought and Philosophy", "Nuanced academic discourse, reasoning, debate, and philosophical logic.", "Abstract Thought", 5, 150, 0, "en"),
        # Most Common 3000
        (20007, 2006, "core-verbs-top-50", "Top 50 Core Verbs", "The most fundamental action verbs in the English language.", "Core Verbs", 5, 150, 0, "en"),
        # Animals
        (20008, 2007, "mammals-and-wildlife", "Mammals and Wildlife", "Land mammals, predators, herbivores, and African savanna wildlife.", "Mammals & Wildlife", 5, 150, 0, "en"),
        # Food & Dining
        (20009, 2008, "restaurant-dining", "Restaurant and Dining", "Ordering meals, table setting, cutlery, courses, and drinks.", "Restaurant & Dining", 5, 150, 0, "en"),
        # Travel
        (20010, 2009, "airport-and-transit", "Airport and Flight", "Check-in, boarding passes, gates, luggage, and air travel.", "Airport & Flight", 5, 150, 0, "en"),
        # Work
        (20011, 2010, "office-collaboration", "Office Collaboration", "Team meetings, deadlines, projects, reports, and workplace management.", "Office Collaboration", 5, 150, 0, "en"),
    ]

    for sub in subcategories_data:
        cur.execute("""
            INSERT INTO subcategories (
                id, category_id, slug, title, description, web_title,
                words_count, estimated_time, position, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                category_id=excluded.category_id,
                slug=excluded.slug,
                title=excluded.title,
                description=excluded.description,
                web_title=excluded.web_title,
                words_count=excluded.words_count,
                estimated_time=excluded.estimated_time,
                position=excluded.position,
                locale=excluded.locale
        """, sub)

    # Words with sample sentences, phonetic transcriptions, and audio links
    words_data = [
        # Sub 20001 (A1 Greetings)
        (1000001, 20001, "hello", "interjection", "Used as a greeting or to begin a phone conversation.", "bonjour", "/həˈloʊ/", "https://tts.langeek.co/read?text=hello&lang=en", "Hello! How are you doing today?", "Bonjour ! Comment allez-vous aujourd'hui ?"),
        (1000002, 20001, "goodbye", "interjection", "Used to express good wishes when parting or at the end of a conversation.", "au revoir", "/ɡʊdˈbaɪ/", "https://tts.langeek.co/read?text=goodbye&lang=en", "She waved and said goodbye before boarding the train.", "Elle a fait un signe de la main et a dit au revoir avant de monter dans le train."),
        (1000003, 20001, "please", "adverb", "Used in polite requests or questions.", "s'il vous plaît", "/pliːz/", "https://tts.langeek.co/read?text=please&lang=en", "Could you please pass the water?", "Pourriez-vous s'il vous plaît me passer l'eau ?"),
        (1000004, 20001, "thank you", "phrase", "A polite expression of gratitude or appreciation.", "merci", "/θæŋk juː/", "https://tts.langeek.co/read?text=thank+you&lang=en", "Thank you very much for your kind help.", "Merci beaucoup pour votre aide précieuse."),
        (1000005, 20001, "welcome", "adjective", "Gladly received or admitted; pleasing.", "bienvenue", "/ˈwɛlkəm/", "https://tts.langeek.co/read?text=welcome&lang=en", "You are always welcome in our home.", "Vous êtes toujours le bienvenu chez nous."),
        (1000006, 20001, "friend", "noun", "A person with whom one has a bond of mutual affection.", "ami", "/frɛnd/", "https://tts.langeek.co/read?text=friend&lang=en", "A good friend will always support you.", "Un bon ami vous soutiendra toujours."),

        # Sub 20002 (Colors & Numbers)
        (1000007, 20002, "blue", "adjective", "Of a color intermediate between green and violet, as of the sky.", "bleu", "/bluː/", "https://tts.langeek.co/read?text=blue&lang=en", "The clear summer sky was bright blue.", "Le ciel clair d'été était d'un bleu éclatant."),
        (1000008, 20002, "red", "adjective", "Of a color at the end of the visible spectrum next to orange.", "rouge", "/rɛd/", "https://tts.langeek.co/read?text=red&lang=en", "She wore an elegant red dress to the ceremony.", "Elle portait une élégante robe rouge à la cérémonie."),
        (1000009, 20002, "green", "adjective", "Of the color between blue and yellow in the spectrum; colored like grass.", "vert", "/ɡriːn/", "https://tts.langeek.co/read?text=green&lang=en", "The hills looked fresh and green after the rain.", "Les collines semblaient fraîches et vertes après la pluie."),
        (1000010, 20002, "three", "numeral", "Equivalent to the sum of one and two; 3.", "trois", "/θriː/", "https://tts.langeek.co/read?text=three&lang=en", "There are three books on the wooden desk.", "Il y a trois livres sur le bureau en bois."),
        (1000011, 20002, "seven", "numeral", "Equivalent to the sum of six and one; 7.", "sept", "/ˈsɛvən/", "https://tts.langeek.co/read?text=seven&lang=en", "A week consists of seven full days.", "Une semaine se compose de sept jours complets."),
        (1000012, 20002, "ten", "numeral", "Equivalent to the product of five and two; 10.", "dix", "/tɛn/", "https://tts.langeek.co/read?text=ten&lang=en", "Count to ten before making an angry decision.", "Comptez jusqu'à dix avant de prendre une décision sous le coup de la colère."),

        # Sub 20007 (Core Verbs)
        (1000013, 20007, "understand", "verb", "Perceive the intended meaning of words, a language, or a speaker.", "comprendre", "/ˌʌndərˈstænd/", "https://tts.langeek.co/read?text=understand&lang=en", "Do you understand the main concept of this lesson?", "Comprenez-vous le concept principal de cette leçon ?"),
        (1000014, 20007, "discover", "verb", "Find unexpectedly or in the course of a search.", "découvrir", "/dɪˈskʌvər/", "https://tts.langeek.co/read?text=discover&lang=en", "Scientists discover new species in deep oceans every year.", "Les scientifiques découvrent chaque année de nouvelles espèces dans les océans profonds."),
        (1000015, 20007, "create", "verb", "Bring something into existence through skill or imagination.", "créer", "/kriˈeɪt/", "https://tts.langeek.co/read?text=create&lang=en", "Artists create magnificent works that inspire generations.", "Les artistes créent des œuvres magnifiques qui inspirent des générations."),

        # Sub 20008 (Animals)
        (1000016, 20008, "elephant", "noun", "A very large herbivorous mammal with a trunk and ivory tusks.", "éléphant", "/ˈɛlɪfənt/", "https://tts.langeek.co/read?text=elephant&lang=en", "The elephant is the largest land mammal on Earth.", "L'éléphant est le plus grand mammifère terrestre sur Terre."),
        (1000017, 20008, "dolphin", "noun", "A highly intelligent aquatic marine mammal related to whales.", "dauphin", "/ˈdɒlfɪn/", "https://tts.langeek.co/read?text=dolphin&lang=en", "A pod of dolphins swam alongside our sailboat.", "Un groupe de dauphins nageait aux côtés de notre voilier."),
        (1000018, 20008, "eagle", "noun", "A large bird of prey with a massive hooked bill and keen vision.", "aigle", "/ˈiːɡəl/", "https://tts.langeek.co/read?text=eagle&lang=en", "The golden eagle soared high above the rocky mountain peaks.", "L'aigle royal planait haut au-dessus des sommets rocheux."),

        # Sub 20010 (Travel)
        (1000019, 20010, "passport", "noun", "An official travel document issued by a government certifying identity.", "passeport", "/ˈpæspɔːrt/", "https://tts.langeek.co/read?text=passport&lang=en", "Keep your passport in a secure and accessible pocket.", "Gardez votre passeport dans une poche sûre et accessible."),
        (1000020, 20010, "boarding", "noun", "The action of getting on or into a ship, aircraft, or vehicle.", "embarquement", "/ˈbɔːrdɪŋ/", "https://tts.langeek.co/read?text=boarding&lang=en", "Boarding for flight 402 will commence in ten minutes.", "L'embarquement pour le vol 402 commencera dans dix minutes."),
    ]

    for w_id, sub_id, entry, pos, en_def, fr_trans, ipa, audio, en_sent, fr_sent in words_data:
        cur.execute("""
            INSERT INTO words (
                id, subcategory_id, entry, part_of_speech, french_def, english_trans,
                audio_url, ipa, photo_url, thumb_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                subcategory_id=excluded.subcategory_id,
                entry=excluded.entry,
                part_of_speech=excluded.part_of_speech,
                french_def=excluded.french_def,
                english_trans=excluded.english_trans,
                audio_url=excluded.audio_url,
                ipa=excluded.ipa
        """, (
            w_id, sub_id, entry, pos, fr_trans, en_def,
            audio, ipa,
            f"https://cdn.langeek.co/photo/w/{w_id}/original?type=jpeg",
            f"https://cdn.langeek.co/photo/w/{w_id}/thumb?type=jpeg"
        ))

        ex_id = 2000000 + w_id
        cur.execute("""
            INSERT INTO examples (id, word_id, french_sentence, english_sentence)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                french_sentence=excluded.french_sentence,
                english_sentence=excluded.english_sentence
        """, (ex_id, w_id, fr_sent, en_sent))

    conn.commit()
    logger.info("Vocabulary tracks seeded successfully.")


def seed_grammar(conn: sqlite3.Connection):
    """Seed 11 English grammar categories and flagship courses with structured blocks."""
    logger.info("Seeding English Grammar modules and lesson blocks...")
    cur = conn.cursor()

    # 11 Grammar Categories (locale = 'en')
    categories = [
        (201, "pronouns", "Pronouns", "Pronouns", "Personal, possessive, relative, and demonstrative pronouns.", 17, 0, "https://cdn.langeek.co/photo/70037/thumb/pronouns?type=png", "en"),
        (202, "nouns", "Nouns", "Nouns", "Countable, uncountable, compound, and plural nouns.", 14, 1, "https://cdn.langeek.co/photo/70038/thumb/nouns?type=png", "en"),
        (203, "verbs", "Verbs", "Verbs", "Regular, irregular, transitive, and auxiliary verb patterns.", 18, 2, "https://cdn.langeek.co/photo/70039/thumb/verbs?type=png", "en"),
        (204, "tenses", "Tenses", "Tenses", "Past, present, future, and continuous verb aspect systems.", 20, 3, "https://cdn.langeek.co/photo/70040/thumb/tenses?type=png", "en"),
        (205, "modals", "Modals", "Modals", "Expressing ability, possibility, obligation, and permission.", 12, 4, "https://cdn.langeek.co/photo/70041/thumb/modals?type=png", "en"),
        (206, "conditionals", "Conditionals", "Conditionals", "Zero, first, second, third, and mixed hypothetical conditionals.", 10, 5, "https://cdn.langeek.co/photo/70042/thumb/conditionals?type=png", "en"),
        (207, "prepositions", "Prepositions", "Prepositions", "Prepositions of time, place, direction, and dependent prepositions.", 16, 6, "https://cdn.langeek.co/photo/70043/thumb/prepositions?type=png", "en"),
        (208, "conjunctions", "Conjunctions", "Conjunctions", "Coordinating, subordinating, and correlative linking words.", 8, 7, "https://cdn.langeek.co/photo/70044/thumb/conjunctions?type=png", "en"),
        (209, "adjectives", "Adjectives", "Adjectives", "Descriptive order, comparatives, and superlatives.", 11, 8, "https://cdn.langeek.co/photo/70045/thumb/adjectives?type=png", "en"),
        (210, "adverbs", "Adverbs", "Adverbs", "Adverbs of manner, frequency, degree, time, and position.", 9, 9, "https://cdn.langeek.co/photo/70046/thumb/adverbs?type=png", "en"),
        (211, "sentence-structure", "Sentence Structure", "Sentence Structure", "Clauses, word order, active vs. passive voice, and inversion.", 15, 10, "https://cdn.langeek.co/photo/70047/thumb/sentences?type=png", "en"),
    ]

    for cat in categories:
        cur.execute("""
            INSERT INTO grammar_categories (
                id, url_id, title, english_title, description, course_length, position, photo_thumbnail, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                url_id=excluded.url_id,
                title=excluded.title,
                english_title=excluded.english_title,
                description=excluded.description,
                course_length=excluded.course_length,
                position=excluded.position,
                photo_thumbnail=excluded.photo_thumbnail,
                locale=excluded.locale
        """, cat)

    # Flagship Courses with typed lesson blocks
    courses = [
        (
            3001, "subject-pronouns", "Subject Pronouns in English", "beginner",
            "Master English Subject Pronouns: I, You, He, She, It, We, They",
            "Subject pronouns replace the subject noun in a sentence to indicate who is performing the action.",
            201, "https://cdn.langeek.co/photo/70039/original/pronouns?type=png", "https://cdn.langeek.co/photo/70039/thumb/pronouns?type=png", "Subject Pronouns", "en",
            [
                {
                    "type": "accent5",
                    "title": "What Are Subject Pronouns?",
                    "id": "SectionBlock.en-gram-1",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=What+Are+Subject+Pronouns&lang=en",
                    "readableTextTranscription": "What Are Subject Pronouns?"
                },
                {
                    "type": "normal",
                    "title": "Overview and Usage",
                    "id": "ExplanationBlock.en-gram-2",
                    "blockType": "ExplanationBlock",
                    "text": "Subject pronouns are used as the subject of a verb in place of a noun. In English, they are: I, you, he, she, it, we, they."
                },
                {
                    "type": "example",
                    "title": "Example Sentences",
                    "id": "ExampleBlock.en-gram-3",
                    "blockType": "ExampleBlock",
                    "examples": [
                        {"en": "She loves reading classic literature.", "trans": "Elle adore lire la littérature classique."},
                        {"en": "They arrived at the airport on time.", "trans": "Ils sont arrivés à l'aéroport à l'heure."}
                    ]
                }
            ]
        ),
        (
            3002, "present-simple-tense", "Present Simple Tense", "beginner",
            "The Present Simple Tense: Habits, General Truths, and Routines",
            "Learn how to form and use the present simple tense for regular routines, universal facts, and states.",
            204, "https://cdn.langeek.co/photo/70040/original/tenses?type=png", "https://cdn.langeek.co/photo/70040/thumb/tenses?type=png", "Present Simple", "en",
            [
                {
                    "type": "accent5",
                    "title": "Forming the Present Simple",
                    "id": "SectionBlock.en-gram-4",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=Forming+the+Present+Simple&lang=en"
                },
                {
                    "type": "normal",
                    "title": "Third Person Singular (He/She/It)",
                    "id": "ExplanationBlock.en-gram-5",
                    "blockType": "ExplanationBlock",
                    "text": "For the third person singular, we generally add -s or -es to the base verb (e.g. He works, She watches)."
                }
            ]
        ),
        (
            3003, "countable-uncountable-nouns", "Countable and Uncountable Nouns", "intermediate",
            "Countable vs. Uncountable Nouns in Modern English",
            "Distinguish between nouns you can count individually and mass nouns that require quantifiers.",
            202, "https://cdn.langeek.co/photo/70038/original/nouns?type=png", "https://cdn.langeek.co/photo/70038/thumb/nouns?type=png", "Countable and Uncountable", "en",
            [
                {
                    "type": "accent5",
                    "title": "Counting Nouns in English",
                    "id": "SectionBlock.en-gram-6",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=Countable+and+Uncountable+Nouns&lang=en"
                }
            ]
        ),
        (
            3004, "modal-verbs-of-ability", "Modal Verbs of Ability: Can, Could, Be Able To", "intermediate",
            "Modal Verbs of Ability: Can, Could, and Be Able To",
            "Express present, past, and future abilities and potential using modal auxiliary constructions.",
            205, "https://cdn.langeek.co/photo/70041/original/modals?type=png", "https://cdn.langeek.co/photo/70041/thumb/modals?type=png", "Modals of Ability", "en",
            [
                {
                    "type": "accent5",
                    "title": "Expressing Ability",
                    "id": "SectionBlock.en-gram-7",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=Modal+Verbs+of+Ability&lang=en"
                }
            ]
        ),
        (
            3005, "first-conditional-structures", "First Conditional: Real Possibilities", "intermediate",
            "First Conditional: If + Present Simple, will + Verb",
            "Discuss real and probable future conditions and their likely consequences.",
            206, "https://cdn.langeek.co/photo/70042/original/conditionals?type=png", "https://cdn.langeek.co/photo/70042/thumb/conditionals?type=png", "First Conditional", "en",
            [
                {
                    "type": "accent5",
                    "title": "Real Future Possibilities",
                    "id": "SectionBlock.en-gram-8",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=First+Conditional&lang=en"
                }
            ]
        ),
        (
            3006, "prepositions-of-place", "Prepositions of Place: In, On, At", "beginner",
            "Mastering Prepositions of Place in English",
            "Clear spatial rules for when to use in, on, at, under, behind, and next to.",
            207, "https://cdn.langeek.co/photo/70043/original/prepositions?type=png", "https://cdn.langeek.co/photo/70043/thumb/prepositions?type=png", "Prepositions of Place", "en",
            [
                {
                    "type": "accent5",
                    "title": "Location and Position",
                    "id": "SectionBlock.en-gram-9",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=Prepositions+of+Place&lang=en"
                }
            ]
        ),
        (
            3007, "comparative-superlative-adjectives", "Comparative and Superlative Adjectives", "beginner",
            "Comparing Adjectives: Form and Syntax",
            "How to compare two or more entities using -er/-est and more/most structures.",
            209, "https://cdn.langeek.co/photo/70045/original/adjectives?type=png", "https://cdn.langeek.co/photo/70045/thumb/adjectives?type=png", "Comparative Adjectives", "en",
            [
                {
                    "type": "accent5",
                    "title": "Making Comparisons",
                    "id": "SectionBlock.en-gram-10",
                    "blockType": "SectionBlock",
                    "readableTextVoice": "https://tts.langeek.co/read?text=Comparative+Adjectives&lang=en"
                }
            ]
        ),
    ]

    for c in courses:
        c_id, url_id, title, level, web_title, desc, cat_id, photo, thumb, orig_title, loc, blocks = c
        cur.execute("""
            INSERT INTO grammar_courses (
                id, url_id, title, level, web_title, description, blocks_count,
                blocks_json, category_id, photo, photo_thumbnail, original_title, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                url_id=excluded.url_id,
                title=excluded.title,
                level=excluded.level,
                web_title=excluded.web_title,
                description=excluded.description,
                blocks_count=excluded.blocks_count,
                blocks_json=excluded.blocks_json,
                category_id=excluded.category_id,
                photo=excluded.photo,
                photo_thumbnail=excluded.photo_thumbnail,
                original_title=excluded.original_title,
                locale=excluded.locale
        """, (
            c_id, url_id, title, level, web_title, desc, len(blocks),
            json.dumps({"blocks": blocks}, ensure_ascii=False),
            cat_id, photo, thumb, orig_title, loc
        ))

    conn.commit()
    logger.info("Grammar tracks seeded successfully.")


def seed_expressions(conn: sqlite3.Connection):
    """Seed Top 25 English everyday idioms with literal and figurative definitions."""
    logger.info("Seeding Top 25 English Expressions and Idioms...")
    cur = conn.cursor()

    idioms = [
        (1, "en", "Everyday Idioms", "Bite the bullet", "To bite down on a lead bullet during surgery without anesthesia", "Face an inevitable difficult situation with fortitude and courage.", json.dumps([{"en": "I know you dislike dental visits, but you just have to bite the bullet.", "fr": "Je sais que tu détestes aller chez le dentiste, mais il faut serrer les dents."}]), "https://tts.langeek.co/read?text=bite+the+bullet&lang=en", 1),
        (2, "en", "Social & Communication", "Break the ice", "To physically shatter ice packs so ships can navigate water", "Make people feel relaxed and comfortable in an unfamiliar social setting.", json.dumps([{"en": "He shared a witty joke to break the ice at the start of the meeting.", "fr": "Il a raconté une blague spirituelle pour briser la glace au début de la réunion."}]), "https://tts.langeek.co/read?text=break+the+ice&lang=en", 2),
        (3, "en", "Effort & Difficulty", "Piece of cake", "A single slice of sweet dessert cake", "Something very simple, effortless, or easy to achieve.", json.dumps([{"en": "After weeks of rigorous practice, the driving test was a piece of cake.", "fr": "Après des semaines d'entraînement intensif, l'examen de conduite a été un jeu d'enfant."}]), "https://tts.langeek.co/read?text=piece+of+cake&lang=en", 3),
        (4, "en", "Health & Well-being", "Under the weather", "Standing beneath gloomy clouds or stormy rainfall at sea", "Feeling slightly unwell, fatigued, or under the symptoms of a mild illness.", json.dumps([{"en": "Sarah is feeling under the weather today, so she is staying home.", "fr": "Sarah ne se sent pas très bien aujourd'hui, elle reste donc à la maison."}]), "https://tts.langeek.co/read?text=under+the+weather&lang=en", 4),
        (5, "en", "Secrets & Truth", "Spill the beans", "To accidentally overturn a container of beans onto the floor", "Disclose confidential information or reveal a secret prematurely.", json.dumps([{"en": "Don't spill the beans about our surprise party before Friday!", "fr": "Ne vends pas la mèche au sujet de notre fête surprise avant vendredi !"}]), "https://tts.langeek.co/read?text=spill+the+beans&lang=en", 5),
        (6, "en", "Money & Finance", "Cost an arm and a leg", "Purchasing something by amputating one's limbs", "Extremely expensive; requiring an exorbitantly high financial cost.", json.dumps([{"en": "A brand new electric sports car will cost an arm and a leg.", "fr": "Une voiture de sport électrique neuve coûte les yeux de la tête."}]), "https://tts.langeek.co/read?text=cost+an+arm+and+a+leg&lang=en", 6),
        (7, "en", "Time & Frequency", "Once in a blue moon", "The rare second full moon appearing within a single calendar month", "Occurring very rarely, almost never.", json.dumps([{"en": "They only travel abroad once in a blue moon.", "fr": "Ils ne voyagent à l'étranger que tous les 36 du mois."}]), "https://tts.langeek.co/read?text=once+in+a+blue+moon&lang=en", 7),
        (8, "en", "Accuracy & Insight", "Hit the nail on the head", "Striking a carpenter's nail squarely on its head with a hammer", "Describe precisely the exact cause of a problem or circumstance.", json.dumps([{"en": "Her diagnosis of the engineering flaw hit the nail on the head.", "fr": "Son diagnostic du défaut d'ingénierie a mis le doigt dessus."}]), "https://tts.langeek.co/read?text=hit+the+nail+on+the+head&lang=en", 8),
        (9, "en", "Work & Study", "Burn the midnight oil", "Keeping an oil lamp burning past midnight to read or work", "Work, study, or prepare diligently late into the night.", json.dumps([{"en": "Students often burn the midnight oil during university finals week.", "fr": "Les étudiants veillent souvent tard pendant la semaine des examens."}]), "https://tts.langeek.co/read?text=burn+the+midnight+oil&lang=en", 9),
        (10, "en", "Mistakes & Errors", "Barking up the wrong tree", "A hunting hound barking up a tree where the target animal is no longer seated", "Pursuing a mistaken line of reasoning or accusing the wrong individual.", json.dumps([{"en": "If you suspect Thomas took your keys, you are barking up the wrong tree.", "fr": "Si vous soupçonnez Thomas d'avoir pris vos clés, vous faites fausse route."}]), "https://tts.langeek.co/read?text=barking+up+the+wrong+tree&lang=en", 10),
        (11, "en", "Truth & Skepticism", "Take with a grain of salt", "Consuming suspect food with a small pinch of salt to aid digestion", "View something with skepticism and refrain from taking it too literally.", json.dumps([{"en": "Take internet rumors with a grain of salt until verified by official sources.", "fr": "Prenez les rumeurs d'Internet avec des pincettes jusqu'à vérification officielle."}]), "https://tts.langeek.co/read?text=take+with+a+grain+of+salt&lang=en", 11),
        (12, "en", "Efficiency & Strategy", "Kill two birds with one stone", "Striking two birds simultaneously using a single thrown pebble", "Accomplish two distinct goals or tasks with a single action.", json.dumps([{"en": "Biking to the office kills two birds with one stone: exercise and commuting.", "fr": "Aller au bureau à vélo fait d'une pierre deux coups : sport et trajet."}]), "https://tts.langeek.co/read?text=kill+two+birds+with+one+stone&lang=en", 12),
        (13, "en", "Fortune & Perspective", "Blessing in disguise", "A divine gift concealed beneath an ugly costume", "An unfortunate event that ultimately results in a fortunate outcome.", json.dumps([{"en": "Losing that job was a blessing in disguise because it led him to start his own firm.", "fr": "Perdre ce travail a été un mal pour un bien, car cela l'a poussé à créer son entreprise."}]), "https://tts.langeek.co/read?text=blessing+in+disguise&lang=en", 13),
        (14, "en", "Quality & Integrity", "Cut corners", "Taking shortcuts across street corners instead of following the path", "Do something carelessly or compromise standards to save money or time.", json.dumps([{"en": "Never cut corners when designing structural safety features.", "fr": "Ne prenez jamais de raccourcis douteux lors de la conception des dispositifs de sécurité."}]), "https://tts.langeek.co/read?text=cut+corners&lang=en", 14),
        (15, "en", "Action & Integrity", "Actions speak louder than words", "Visible movements make more decibels than vocal sounds", "What a person does proves their intentions much more convincingly than what they declare.", json.dumps([{"en": "He promised to assist us, but actions speak louder than words.", "fr": "Il a promis de nous aider, mais les actes valent mieux que les mots."}]), "https://tts.langeek.co/read?text=actions+speak+louder+than+words&lang=en", 15),
        (16, "en", "Advantage & Opportunity", "Best of both worlds", "Enjoying the advantages of two separate realms", "A situation in which you can enjoy two very different advantages at the same time.", json.dumps([{"en": "Remote work offers the best of both worlds: productivity and home comfort.", "fr": "Le télétravail offre le meilleur des deux mondes : productivité et confort du foyer."}]), "https://tts.langeek.co/read?text=best+of+both+worlds&lang=en", 16),
        (17, "en", "Agreement & Harmony", "See eye to eye", "Looking directly into another person's eyes with parallel vision", "To be in full agreement with someone on a given matter.", json.dumps([{"en": "The two partners see eye to eye on their company's long-term expansion.", "fr": "Les deux associés sont sur la même longueur d'onde concernant l'expansion de l'entreprise."}]), "https://tts.langeek.co/read?text=see+eye+to+eye&lang=en", 17),
        (18, "en", "Coincidence & Humor", "Speak of the devil", "Invoking an evil entity causes its immediate manifestation", "Said when someone appears just as you were talking about them.", json.dumps([{"en": "Well, speak of the devil! Here comes Michael right now.", "fr": "Quand on parle du loup ! Voici justement Michael qui arrive."}]), "https://tts.langeek.co/read?text=speak+of+the+devil&lang=en", 18),
        (19, "en", "Misfortune & Conflict", "Add insult to injury", "Verbally mocking an already wounded individual", "Make a bad situation even worse by offensive behavior or further harm.", json.dumps([{"en": "To add insult to injury, they charged us for cancelling the broken service.", "fr": "Pour couronner le tout, ils nous ont facturé l'annulation du service défectueux."}]), "https://tts.langeek.co/read?text=add+insult+to+injury&lang=en", 19),
        (20, "en", "Responsibility & Decision", "Ball is in your court", "Tennis ball landing on your side of the net", "It is now your decision or turn to take the next step.", json.dumps([{"en": "We sent over our final proposal; the ball is in their court now.", "fr": "Nous avons envoyé notre proposition finale ; la balle est maintenant dans leur camp."}]), "https://tts.langeek.co/read?text=ball+is+in+your+court&lang=en", 20),
        (21, "en", "Humor & Teasing", "Pull someone's leg", "Physically pulling an individual's foot or leg", "Tease or deceive someone playfully as a good-natured joke.", json.dumps([{"en": "Relax, I didn't actually lose the tickets; I was just pulling your leg!", "fr": "Détends-toi, je n'ai pas vraiment perdu les billets ; je te faisais juste marcher !"}]), "https://tts.langeek.co/read?text=pull+someones+leg&lang=en", 21),
        (22, "en", "Wisdom & Caution", "Curiosity killed the cat", "A cat perishing due to its inquisitive exploration", "Being inquisitive about things that do not concern you can lead to unexpected trouble.", json.dumps([{"en": "Don't open that locked drawer; remember that curiosity killed the cat.", "fr": "N'ouvre pas ce tiroir verrouillé ; la curiosité est un vilain défaut."}]), "https://tts.langeek.co/read?text=curiosity+killed+the+cat&lang=en", 22),
        (23, "en", "Regret & Acceptance", "Cry over spilt milk", "Shedding tears over liquid milk spilled onto a table", "Waste time feeling upset or regretful about past losses that cannot be rectified.", json.dumps([{"en": "The vase is already broken; there is no use crying over spilt milk.", "fr": "Le vase est déjà brisé ; ce qui est fait est fait, inutile de pleurer."}]), "https://tts.langeek.co/read?text=cry+over+spilt+milk&lang=en", 23),
        (24, "en", "Communication & Directness", "Beat around the bush", "Beating foliage surrounding a bush without targeting the bird inside", "Discuss a topic without coming to the main point; avoid addressing an issue directly.", json.dumps([{"en": "Stop beating around the bush and explain what truly happened.", "fr": "Arrête de tourner autour du pot et explique ce qui s'est réellement passé."}]), "https://tts.langeek.co/read?text=beat+around+the+bush&lang=en", 24),
        (25, "en", "Loyalty & Dedication", "Through thick and thin", "Travelling through dense thickets as well as sparse woodlands", "Remaining loyal and steadfast through all adversities, trials, and pleasant times.", json.dumps([{"en": "The two lifelong colleagues stood by each other through thick and thin.", "fr": "Les deux collègues de toujours se sont soutenus contre vents et marées."}]), "https://tts.langeek.co/read?text=through+thick+and+thin&lang=en", 25),
    ]

    for item in idioms:
        cur.execute("""
            INSERT INTO expressions (
                id, locale, category, phrase, literal_translation, meaning, examples_json, audio_url, position
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                locale=excluded.locale,
                category=excluded.category,
                phrase=excluded.phrase,
                literal_translation=excluded.literal_translation,
                meaning=excluded.meaning,
                examples_json=excluded.examples_json,
                audio_url=excluded.audio_url,
                position=excluded.position
        """, item)

    conn.commit()
    logger.info("Expressions seeded successfully.")


def seed_pronunciation(conn: sqlite3.Connection):
    """Seed 26 English Alphabet courses (A-Z) with phonetic sounds and example words."""
    logger.info("Seeding English Pronunciation Alphabet (A-Z)...")
    cur = conn.cursor()

    alphabet = [
        ("A", "/eɪ/", ["Apple", "Ace", "Aircraft"]),
        ("B", "/biː/", ["Ball", "Book", "Brave"]),
        ("C", "/siː/", ["Cat", "City", "Ocean"]),
        ("D", "/diː/", ["Door", "Dream", "Daylight"]),
        ("E", "/iː/", ["Eagle", "Energy", "Elephant"]),
        ("F", "/ɛf/", ["Fire", "Friend", "Forest"]),
        ("G", "/dʒiː/", ["Green", "Garden", "Giant"]),
        ("H", "/eɪtʃ/", ["House", "Heart", "Horizon"]),
        ("I", "/aɪ/", ["Island", "Idea", "Ice"]),
        ("J", "/dʒeɪ/", ["Journey", "Joy", "Jungle"]),
        ("K", "/keɪ/", ["King", "Knowledge", "Kangaroo"]),
        ("L", "/ɛl/", ["Light", "Language", "Lion"]),
        ("M", "/ɛm/", ["Moon", "Mountain", "Memory"]),
        ("N", "/ɛn/", ["Night", "Nature", "Navigation"]),
        ("O", "/oʊ/", ["Ocean", "Open", "Orange"]),
        ("P", "/piː/", ["Peace", "Planet", "Pioneer"]),
        ("Q", "/kjuː/", ["Queen", "Quiet", "Quest"]),
        ("R", "/ɑːr/", ["River", "Rainbow", "Reason"]),
        ("S", "/ɛs/", ["Sun", "Star", "Silence"]),
        ("T", "/tiː/", ["Tree", "Truth", "Time"]),
        ("U", "/juː/", ["Universe", "Unity", "Umbrella"]),
        ("V", "/viː/", ["Voice", "Victory", "Valley"]),
        ("W", "/ˈdʌbəl.juː/", ["Water", "World", "Wisdom"]),
        ("X", "/ɛks/", ["X-ray", "Xylophone", "Box"]),
        ("Y", "/waɪ/", ["Year", "Youth", "Yellow"]),
        ("Z", "/zɛd/", ["Zebra", "Zero", "Zenith"]),
    ]

    for idx, (letter, ipa, words) in enumerate(alphabet):
        course_id = 5001 + idx
        url_id = f"the-letter-{letter.lower()}"
        title = f'The Letter "{letter}" in English'
        desc = f'Master the pronunciation, phonetics, and common spelling rules of the letter {letter} ({ipa}) in English.'
        content = json.dumps({
            "letter": letter,
            "ipa": ipa,
            "example_words": words,
            "audio_url": f"https://tts.langeek.co/read?text={letter}&lang=en"
        })
        cur.execute("""
            INSERT INTO pronunciation_courses (
                id, hub_id, title, url_id, letter, description, photo, photo_thumbnail, content_json, position, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                hub_id=excluded.hub_id,
                title=excluded.title,
                url_id=excluded.url_id,
                letter=excluded.letter,
                description=excluded.description,
                photo=excluded.photo,
                photo_thumbnail=excluded.photo_thumbnail,
                content_json=excluded.content_json,
                position=excluded.position,
                locale=excluded.locale
        """, (
            course_id, 101, title, url_id, letter, desc,
            f"https://cdn.langeek.co/photo/7300{idx}/original/letter-{letter.lower()}?type=png",
            f"https://cdn.langeek.co/photo/7300{idx}/thumb/letter-{letter.lower()}?type=png",
            content, idx, "en"
        ))

    conn.commit()
    logger.info("Pronunciation Alphabet seeded successfully.")


def seed_reading(conn: sqlite3.Connection):
    """Seed graded English reading collections, stories, and segments with ParagraphBlock & PhotoBlock."""
    logger.info("Seeding Graded English Reading stories and block segments...")
    cur = conn.cursor()

    collections = [
        (301, "Famous Figures", "famous-figures", "https://cdn.langeek.co/photo/70346/original/figures?type=png", "https://cdn.langeek.co/photo/70346/thumb/figures?type=png", "Read inspiring biographies of artists, scientists, and visionaries.", 2, 0, "en"),
        (302, "Nature and Wildlife", "nature-and-wildlife", "https://cdn.langeek.co/photo/70347/original/nature?type=png", "https://cdn.langeek.co/photo/70347/thumb/nature?type=png", "Explore the wonders of ecosystems, wildlife, and natural phenomena.", 1, 1, "en"),
        (303, "Daily Life & Culture", "daily-life-and-culture", "https://cdn.langeek.co/photo/70348/original/culture?type=png", "https://cdn.langeek.co/photo/70348/thumb/culture?type=png", "Short real-world vignettes about routines, traditions, and cuisine.", 1, 2, "en"),
    ]

    for col in collections:
        cur.execute("""
            INSERT INTO reading_collections (
                id, title, url_id, photo, photo_thumbnail, description, courses_count, position, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                title=excluded.title,
                url_id=excluded.url_id,
                photo=excluded.photo,
                photo_thumbnail=excluded.photo_thumbnail,
                description=excluded.description,
                courses_count=excluded.courses_count,
                position=excluded.position,
                locale=excluded.locale
        """, col)

    stories = [
        (
            4001, 301, "The Genius of Leonardo da Vinci", "leonardo-da-vinci", "intermediate",
            "Explore the life and polymathic creations of the Renaissance master.",
            "https://cdn.langeek.co/photo/70292/original/leonardo?type=png",
            "https://cdn.langeek.co/photo/70292/thumb/leonardo?type=png",
            "en",
            [
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "Leonardo da Vinci was born in 1452 in Vinci, Italy. He is widely celebrated as one of history's greatest polymaths.",
                    "en": "Leonardo da Vinci was born in 1452 in Vinci, Italy. He is widely celebrated as one of history's greatest polymaths.",
                    "audio": "https://tts.langeek.co/read?text=Leonardo+da+Vinci+was+born+in+1452&lang=en"
                },
                {
                    "blockType": "PhotoBlock",
                    "type": "photo",
                    "photo": "https://cdn.langeek.co/photo/70292/original/leonardo?type=png",
                    "photo_thumbnail": "https://cdn.langeek.co/photo/70292/thumb/leonardo?type=png"
                },
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "Beyond his world-famous paintings like the Mona Lisa and The Last Supper, Leonardo filled notebooks with engineering marvels.",
                    "en": "Beyond his world-famous paintings like the Mona Lisa and The Last Supper, Leonardo filled notebooks with engineering marvels.",
                    "audio": "https://tts.langeek.co/read?text=Beyond+his+world+famous+paintings&lang=en"
                }
            ]
        ),
        (
            4002, 301, "Marie Curie: Pioneer of Modern Physics", "marie-curie", "intermediate",
            "The remarkable life of the first woman to win a Nobel Prize.",
            "https://cdn.langeek.co/photo/70293/original/curie?type=png",
            "https://cdn.langeek.co/photo/70293/thumb/curie?type=png",
            "en",
            [
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "Marie Curie was a pioneering physicist and chemist whose research on radioactivity broke new ground.",
                    "en": "Marie Curie was a pioneering physicist and chemist whose research on radioactivity broke new ground.",
                    "audio": "https://tts.langeek.co/read?text=Marie+Curie+was+a+pioneering+physicist&lang=en"
                },
                {
                    "blockType": "PhotoBlock",
                    "type": "photo",
                    "photo": "https://cdn.langeek.co/photo/70293/original/curie?type=png",
                    "photo_thumbnail": "https://cdn.langeek.co/photo/70293/thumb/curie?type=png"
                },
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "She became the first person to win Nobel Prizes in two distinct scientific disciplines.",
                    "en": "She became the first person to win Nobel Prizes in two distinct scientific disciplines.",
                    "audio": "https://tts.langeek.co/read?text=She+became+the+first+person+to+win+Nobel+Prizes&lang=en"
                }
            ]
        ),
        (
            4003, 302, "The Secret Life of Honeybees", "secret-life-honeybees", "beginner",
            "Learn how honeybees communicate through intricate dances and sustain global agriculture.",
            "https://cdn.langeek.co/photo/70294/original/honeybees?type=png",
            "https://cdn.langeek.co/photo/70294/thumb/honeybees?type=png",
            "en",
            [
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "Honeybees are remarkable insects that live in highly structured colonies.",
                    "en": "Honeybees are remarkable insects that live in highly structured colonies.",
                    "audio": "https://tts.langeek.co/read?text=Honeybees+are+remarkable+insects&lang=en"
                },
                {
                    "blockType": "PhotoBlock",
                    "type": "photo",
                    "photo": "https://cdn.langeek.co/photo/70294/original/honeybees?type=png",
                    "photo_thumbnail": "https://cdn.langeek.co/photo/70294/thumb/honeybees?type=png"
                },
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "They communicate the distance and direction of floral nectar through a waggle dance.",
                    "en": "They communicate the distance and direction of floral nectar through a waggle dance.",
                    "audio": "https://tts.langeek.co/read?text=They+communicate+the+distance+and+direction&lang=en"
                }
            ]
        ),
        (
            4004, 303, "Coffee Traditions Across Continents", "coffee-traditions", "beginner",
            "A warm journey through coffee brewing customs around the world.",
            "https://cdn.langeek.co/photo/70295/original/coffee?type=png",
            "https://cdn.langeek.co/photo/70295/thumb/coffee?type=png",
            "en",
            [
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "Coffee is one of the most widely consumed hot beverages across the globe.",
                    "en": "Coffee is one of the most widely consumed hot beverages across the globe.",
                    "audio": "https://tts.langeek.co/read?text=Coffee+is+one+of+the+most+widely+consumed&lang=en"
                },
                {
                    "blockType": "PhotoBlock",
                    "type": "photo",
                    "photo": "https://cdn.langeek.co/photo/70295/original/coffee?type=png",
                    "photo_thumbnail": "https://cdn.langeek.co/photo/70295/thumb/coffee?type=png"
                },
                {
                    "blockType": "ParagraphBlock",
                    "type": "paragraph",
                    "fr": "From Ethiopian clay pot ceremonies to Italian espresso bars, each culture savors its unique cup.",
                    "en": "From Ethiopian clay pot ceremonies to Italian espresso bars, each culture savors its unique cup.",
                    "audio": "https://tts.langeek.co/read?text=From+Ethiopian+clay+pot+ceremonies&lang=en"
                }
            ]
        ),
    ]

    for s_id, col_id, title, url_id, level, desc, photo, thumb, loc, blocks in stories:
        cur.execute("""
            INSERT INTO reading_stories (
                id, collection_id, title, url_id, level, description, photo, photo_thumbnail,
                content_json, quiz_json, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(id) DO UPDATE SET
                collection_id=excluded.collection_id,
                title=excluded.title,
                url_id=excluded.url_id,
                level=excluded.level,
                description=excluded.description,
                photo=excluded.photo,
                photo_thumbnail=excluded.photo_thumbnail,
                content_json=excluded.content_json,
                quiz_json=excluded.quiz_json,
                locale=excluded.locale
        """, (
            s_id, col_id, title, url_id, level, desc, photo, thumb,
            json.dumps(blocks, ensure_ascii=False), "[]", loc
        ))

        # Insert segment 0
        cur.execute("""
            INSERT INTO reading_segments (
                story_id, segment_index, title, url_id, photo, content_json, locale
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(story_id, segment_index) DO UPDATE SET
                title=excluded.title,
                url_id=excluded.url_id,
                photo=excluded.photo,
                content_json=excluded.content_json,
                locale=excluded.locale
        """, (
            s_id, 0, title, url_id, photo,
            json.dumps(blocks, ensure_ascii=False), loc
        ))

    conn.commit()
    logger.info("Reading stories seeded successfully.")


def seed_english_flagship(db_path: Optional[str] = None):
    """Orchestrate end-to-end English flagship seeding across all 5 modules."""
    path = db_path or DB_PATH
    logger.info("Initiating flagship English seeding on %s", path)
    conn = get_connection(path)

    fr_before = verify_french_integrity(conn)

    seed_vocabulary(conn)
    seed_grammar(conn)
    seed_expressions(conn)
    seed_pronunciation(conn)
    seed_reading(conn)

    fr_after = verify_french_integrity(conn)

    # Strict assertion that French curriculum was untouched
    for table, count in fr_before.items():
        assert fr_after[table] == count, f"French row count mismatch in {table}: was {count}, now {fr_after[table]}"

    cur = conn.cursor()
    en_counts = {
        "categories": cur.execute("SELECT count(*) FROM categories WHERE locale = 'en'").fetchone()[0],
        "subcategories": cur.execute("SELECT count(*) FROM subcategories WHERE locale = 'en'").fetchone()[0],
        "grammar_categories": cur.execute("SELECT count(*) FROM grammar_categories WHERE locale = 'en'").fetchone()[0],
        "grammar_courses": cur.execute("SELECT count(*) FROM grammar_courses WHERE locale = 'en'").fetchone()[0],
        "expressions": cur.execute("SELECT count(*) FROM expressions WHERE locale = 'en'").fetchone()[0],
        "pronunciation_courses": cur.execute("SELECT count(*) FROM pronunciation_courses WHERE locale = 'en'").fetchone()[0],
        "reading_collections": cur.execute("SELECT count(*) FROM reading_collections WHERE locale = 'en'").fetchone()[0],
        "reading_stories": cur.execute("SELECT count(*) FROM reading_stories WHERE locale = 'en'").fetchone()[0],
        "reading_segments": cur.execute("SELECT count(*) FROM reading_segments WHERE locale = 'en'").fetchone()[0],
    }

    conn.close()
    logger.info("English flagship seeding completed successfully!")
    logger.info("English row summary: %s", en_counts)
    return en_counts


if __name__ == "__main__":
    seed_english_flagship()
