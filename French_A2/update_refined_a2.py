with open("make_refined_a2.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Ensure 'pronoms' is present in page 10
content = content.replace(
    '"title": "A2 Grammar: Object Pronouns (COD & COI)"',
    '"title": "A2 Grammar: Object Pronouns (Les Pronoms COD & COI)"'
)
content = content.replace(
    '"title": "A2 Grammar: Pronouns \'Y\', \'En\' & Relative Pronouns"',
    '"title": "A2 Grammar: Les Pronoms \'Y\', \'En\' & Relative Pronouns"'
)

# 2. Add 'items' to audit pages 68, 69, 70, 71
page68_replacement = '''    # Page 68: Final Self-Evaluation: Speaking Readiness & Fluency
    pages[68] = {
        "page": 68,
        "type": "audit",
        "title": "Final Self-Evaluation: Speaking Readiness & Fluency",
        "subtitle": "Checking Your Spoken Communication Skills",
        "badge_num": "67",
        "intro": "Use this checklist to check if you can speak French smoothly and confidently in everyday situations.",
        "items": [
            "I can deliver an uninterrupted 2-minute monologue about my life, routine, and hobbies.",
            "I can recount a past journey or childhood memory combining passé composé and imparfait.",
            "I can explain my future career plans and personal ambitions using the futur simple.",
            "I can resolve everyday errands at train stations, post offices, and shops in French.",
            "I can exchange or return a defective product in a store, explaining the problem clearly.",
            "I can invite friends, accept invitations gladly, and decline politely with excuses.",
            "I can share my opinion, agree, or disagree politely in a friendly conversation.",
            "I can handle basic phone calls, spell contact details, and leave structured voicemails."
        ],
        "sections": [
            {
                "title": "1. Spoken Production Audit (Monologue en continu)",
                "items": [
                    "Continuous speech flow: Can you speak continuously for 90 to 120 seconds on a familiar everyday topic?",
                    "Telling past stories: Can you recount a past event clearly using both passé composé and imparfait?",
                    "Future plans: Can you describe your future projects and career plans using the futur proche and futur simple?",
                    "Comparing things: Can you compare two cities, apartments, or jobs using plus... que and moins... que?"
                ]
            },
            {
                "title": "2. Spoken Interaction Audit (Dialogue & Role-Plays)",
                "items": [
                    "Shopping & services: Can you buy train tickets, order meals, and return items in stores without help?",
                    "Everyday opinions: Can you share your thoughts, agree, or disagree politely in a conversation?",
                    "Asking for clarification: Can you ask people to slow down or repeat when you don't understand?",
                    "Handling phone calls: Can you make an appointment or leave a voicemail message on the phone?"
                ]
            }
        ]
    }'''

page69_replacement = '''    # Page 69: Final Self-Evaluation: Receptive & Written Skills
    pages[69] = {
        "page": 69,
        "type": "audit",
        "title": "Final Self-Evaluation: Receptive & Written Skills",
        "subtitle": "Checking Your Listening, Reading & Writing Skills",
        "badge_num": "68",
        "intro": "Evaluate your listening comprehension, reading skills, and ability to write practical messages.",
        "items": [
            "I can catch key information in airport and train station announcements.",
            "I can follow clear everyday conversations between French speakers at normal speed.",
            "I can understand short radio weather forecasts, news flashes, and cultural reports.",
            "I can read restaurant menus, rental listings, recipes, and store flyers easily.",
            "I can understand personal emails and invitations from French friends.",
            "I can write a 60 to 80-word friendly email or postcard describing a trip or weekend.",
            "I can write a short polite message to a hotel, school, or agency asking for info.",
            "I can write a 50 to 70-word review about a hotel, restaurant, or product online."
        ],
        "sections": [
            {
                "title": "1. Listening & Reading Audit",
                "items": [
                    "Public announcements: Can you understand essential details in airport and train station announcements?",
                    "Catching fast numbers: Can you catch prices, times, and phone numbers on the first or second listen?",
                    "Everyday reading: Can you read restaurant menus, rental listings, recipes, and store flyers easily?",
                    "Personal correspondence: Can you understand personal emails and invitations from French friends?"
                ]
            },
            {
                "title": "2. Written Production Audit",
                "items": [
                    "Personal emails & postcards: Can you write a 60 to 80-word message describing a trip or weekend?",
                    "Invitations & replies: Can you invite someone, accept an invitation, or decline with a polite excuse?",
                    "Formal inquiries: Can you write a short polite message to a hotel, school, or agency asking for info?",
                    "Online reviews: Can you write a 50 to 70-word review about a hotel, restaurant, or product?"
                ]
            }
        ]
    }'''

page70_replacement = '''    # Page 70: Final Self-Evaluation: Grammar & Vocabulary Mastery
    pages[70] = {
        "page": 70,
        "type": "audit",
        "title": "Final Self-Evaluation: Grammar & Vocabulary Mastery",
        "subtitle": "Checking Your Core Grammar Rules and 1,500+ Words",
        "badge_num": "69",
        "intro": "Verify that you have mastered the core grammar rules and essential vocabulary of the CEFR A2 level.",
        "items": [
            "I can conjugate regular and irregular verbs in the passé composé using avoir and être.",
            "I know when to use the imparfait for descriptions and habits versus passé composé for events.",
            "I can express future projects using both futur proche and futur simple.",
            "I can use object pronouns (COD & COI) and adverbial pronouns (Y & En) accurately.",
            "I can compare items using comparatives (plus/moins/aussi... que) and superlatives.",
            "I can use negative words like ne... plus, ne... jamais, ne... rien, ne... personne.",
            "I have an active vocabulary of over 1,500 words across all core daily life themes.",
            "I routinely check adjective agreements, verb endings, and silent letters in my writing."
        ],
        "sections": [
            {
                "title": "1. Core Grammar Audit",
                "items": [
                    "Tenses & modes: Passé composé (avoir & être), Imparfait, Futur simple, and Conditionnel de politesse.",
                    "Pronouns: Direct (COD), Indirect (COI), Pronoun Y (places), Pronoun En (quantities), and Qui/Que.",
                    "Negation & adverbs: Ne... plus, ne... jamais, ne... rien, ne... personne, and adverbs in -ment.",
                    "Prepositions of time: Depuis (still continuing), Pendant (completed duration), Il y a (ago), and Dans (future)."
                ]
            },
            {
                "title": "2. Thematic Vocabulary Audit (1,500+ Words)",
                "items": [
                    "Everyday domains: Personal identity, housing, chores, food, shopping, transit, health, work, and media.",
                    "Describing sensations: Avoir faim, soif, chaud, froid, sommeil, peur, mal à la tête.",
                    "Conversation fillers & idioms: Alors, donc, en fait, ça marche, pas de souci, c'est pas grave.",
                    "Self-correction: Automatically checking adjective agreements, verb endings, and silent letters in writing."
                ]
            }
        ]
    }'''

page71_replacement = '''    # Page 71: Final Milestone: Ready to Move to B1 Certification
    pages[71] = {
        "page": 71,
        "type": "audit",
        "title": "Final Milestone: Ready to Move to B1 Certification",
        "subtitle": "Congratulations! You Have Reached CEFR A2 Independence",
        "badge_num": "70",
        "intro": "Review your final checklist items to confirm you are completely ready to step into Intermediate French (B1).",
        "items": [
            "Functional independence: You can travel across French-speaking countries and handle daily situations on your own.",
            "Spontaneous conversation: You can chat with locals, express your feelings, and share your personal stories.",
            "Reading & writing fluency: You can read everyday documents and write clear, well-connected messages.",
            "Solid grammar foundation: You confidently distinguish between past, present, and future tenses.",
            "Ready to move to B1: You are fully prepared to begin your CEFR B1 intermediate journey!"
        ],
        "sections": [
            {
                "title": "1. Final Independence Check",
                "items": [
                    "Functional independence: You can travel across French-speaking countries and handle daily situations on your own.",
                    "Spontaneous conversation: You can chat with locals, express your feelings, and share your personal stories.",
                    "Reading & writing fluency: You can read everyday documents and write clear, well-connected messages.",
                    "Solid grammar foundation: You confidently distinguish between past, present, and future tenses."
                ]
            }
        ]
    }'''

# Replace in content
import re
content = re.sub(r'    # Page 68:.*?pages\[68\] = \{.*?\n    \}', page68_replacement, content, flags=re.DOTALL)
content = re.sub(r'    # Page 69:.*?pages\[69\] = \{.*?\n    \}', page69_replacement, content, flags=re.DOTALL)
content = re.sub(r'    # Page 70:.*?pages\[70\] = \{.*?\n    \}', page70_replacement, content, flags=re.DOTALL)
content = re.sub(r'    # Page 71:.*?pages\[71\] = \{.*?\n    \}', page71_replacement, content, flags=re.DOTALL)

with open("make_refined_a2.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated make_refined_a2.py")
