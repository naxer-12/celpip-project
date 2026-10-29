import os
import sys

# Comprehensive Generator for:
# "Mastering Core French Syntax: Regular -ER Verbs, The Complete Article System, Contractions, and Nominal/Adjective Agreement"
# Builds both DOCX and PDF formats.

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ARIAL_PATH = "/System/Library/Fonts/Supplemental/Arial.ttf"
ARIAL_BOLD_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
ARIAL_ITALIC_PATH = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
ARIAL_BOLD_ITALIC_PATH = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
ARIAL_UNICODE_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"

if os.path.exists(ARIAL_UNICODE_PATH):
    pdfmetrics.registerFont(TTFont('Arial', ARIAL_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Bold', ARIAL_BOLD_PATH))
    pdfmetrics.registerFont(TTFont('Arial-Italic', ARIAL_ITALIC_PATH))
    pdfmetrics.registerFont(TTFont('Arial-BoldItalic', ARIAL_BOLD_ITALIC_PATH))
    pdfmetrics.registerFont(TTFont('ArialUnicode', ARIAL_UNICODE_PATH))
    pdfmetrics.registerFontFamily(
        'ArialUnicode',
        normal='ArialUnicode',
        bold='Arial-Bold',
        italic='Arial-Italic',
        boldItalic='Arial-BoldItalic'
    )
    BASE_FONT = "ArialUnicode"
    BOLD_FONT = "Arial-Bold"
    ITALIC_FONT = "Arial-Italic"
else:
    BASE_FONT = "Helvetica"
    BOLD_FONT = "Helvetica-Bold"
    ITALIC_FONT = "Helvetica-Oblique"

BASE_DIR = "/Users/jainamshah/Downloads/Learning French"
DOCX_PATH = os.path.join(BASE_DIR, "Mastering_Core_French_Syntax_Workbook.docx")
PDF_PATH = os.path.join(BASE_DIR, "Mastering_Core_French_Syntax_Workbook.pdf")

# Palette
NAVY_HEX = "0F172A"       # Slate 900
INDIGO_HEX = "1E1B4B"     # Deep Indigo / Oxford
BURGUNDY_HEX = "881337"   # Deep Crimson / Burgundy
AMBER_HEX = "9A3412"      # Rust / Burnt Amber
TEAL_HEX = "0F766E"       # Teal 700
LIGHT_BG = "F8FAFC"       # Slate 50
CALLOUT_BG = "F1F5F9"     # Slate 100
ALERT_BG = "FFFBEB"       # Amber 50
DANGER_BG = "FFF1F2"      # Rose 50
BORDER_HEX = "CBD5E1"     # Slate 300
DARK_TEXT_HEX = "0F172A"

NAVY_RGB = RGBColor(15, 23, 42)
INDIGO_RGB = RGBColor(30, 27, 75)
BURGUNDY_RGB = RGBColor(136, 19, 55)
AMBER_RGB = RGBColor(154, 52, 18)
TEAL_RGB = RGBColor(15, 118, 110)
DARK_RGB = RGBColor(15, 23, 42)
MUTED_RGB = RGBColor(71, 85, 105)

def style_cell(cell, fill_hex=None, borders=None, pad_tb=90, pad_lr=110):
    tcPr = cell._element.get_or_add_tcPr()
    if fill_hex:
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)
    if pad_tb or pad_lr:
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>'
            f'<w:top w:w="{pad_tb}" w:type="dxa"/>'
            f'<w:bottom w:w="{pad_tb}" w:type="dxa"/>'
            f'<w:left w:w="{pad_lr}" w:type="dxa"/>'
            f'<w:right w:w="{pad_lr}" w:type="dxa"/>'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)
    if borders is not None:
        tcBorders = parse_xml(f'<w:tcBorders {nsdecls("w")}/>')
        for edge in ('top', 'left', 'bottom', 'right'):
            if edge in borders:
                b = borders[edge]
                tcBorders.append(parse_xml(
                    f'<w:{edge} {nsdecls("w")} w:val="{b.get("val", "single")}" '
                    f'w:sz="{b.get("sz", "4")}" w:space="0" w:color="{b.get("color", BORDER_HEX)}"/>'
                ))
            else:
                tcBorders.append(parse_xml(f'<w:{edge} {nsdecls("w")} w:val="none"/>'))
        tcPr.append(tcBorders)

# =========================================================================
# DATA REPOSITORY FOR EXERCISES AND SOLUTIONS
# =========================================================================

LEVEL1_VERBS_PARADIGMS = [
    {
        "verb": "parler (to speak)",
        "rows": [
            ("je", "parle", "nous", "parlons"),
            ("tu", "parles", "vous", "parlez"),
            ("il / elle / on", "parle", "ils / elles", "parlent")
        ],
        "notes": "Base stem: parl-. Note silent 3rd plural '-ent' [paʁl]."
    },
    {
        "verb": "habiter (to live/reside)",
        "rows": [
            ("j'", "habite", "nous", "habitons"),
            ("tu", "habites", "vous", "habitez"),
            ("il / elle / on", "habite", "ils / elles", "habitent")
        ],
        "notes": "Mute h triggers mandatory elision: 'j'habite', never '*je habite'."
    },
    {
        "verb": "regarder (to watch/look at)",
        "rows": [
            ("je", "regarde", "nous", "regardons"),
            ("tu", "regardes", "vous", "regardez"),
            ("il / elle / on", "regarde", "ils / elles", "regardent")
        ],
        "notes": "Transitive verb: takes direct object without preposition ('regarder le film')."
    },
    {
        "verb": "travailler (to work)",
        "rows": [
            ("je", "travaille", "nous", "travaillons"),
            ("tu", "travailles", "vous", "travaillez"),
            ("il / elle / on", "travaille", "ils / elles", "travaillent")
        ],
        "notes": "Stem contains palatal approximant [j] spelled '-ill-'."
    },
    {
        "verb": "étudier (to study)",
        "rows": [
            ("j'", "étudie", "nous", "étudions"),
            ("tu", "étudies", "vous", "étudiez"),
            ("il / elle / on", "étudie", "ils / elles", "étudient")
        ],
        "notes": "Initial vowel triggers elision: 'j'étudie'. Stem ends in -i: 'nous étudions'."
    },
    {
        "verb": "écouter (to listen to)",
        "rows": [
            ("j'", "écoute", "nous", "écoutons"),
            ("tu", "écoutes", "vous", "écoutez"),
            ("il / elle / on", "écoute", "ils / elles", "écoutent")
        ],
        "notes": "Elision: 'j'écoute'. Direct transitive in French (no preposition like English 'to')."
    }
]

LEVEL1_PHONETIC_ITEMS = [
    ("1. il regarde vs. ils regardent", "Ending Sound:", "[ ] Identical sound [paʁl] / [ʁə.ɡaʁd]", "[ ] Distinct sounded consonant", "Identical /ʁə.ɡaʁd/ (verbal -ent is phonetically null)"),
    ("2. tu parles vs. vous parlez", "Acoustic Distinction:", "[ ] /e/ vs. silent /ø/", "[ ] Both silent", "tu parles = /paʁl/ (mute -es) vs. vous parlez = /paʁ.le/ (/e/)"),
    ("3. nous habitons vs. ils habitent", "Nasal vs. Non-Nasal:", "[ ] /ɔ̃/ nasal vs. mute /ø/", "[ ] Both nasal", "habitons = nasal /a.bi.tɔ̃/ vs. habitent = /a.bit/"),
    ("4. elle écoute vs. elles écoutent", "Acoustic Distinction:", "[ ] Exactly homophonous", "[ ] Audibly different", "Exact homophones: /e.kut/ for both 3rd sing and 3rd plur"),
    ("5. je travaille vs. nous travaillons", "Syllable Count:", "[ ] 2 syllables vs. 3 syllables", "[ ] Same syllable count", "je travaille = 2 syll (/tʁa.vaj/) vs. travaillons = 3 syll (/tʁa.va.jɔ̃/)"),
    ("6. on étudie vs. ils étudient", "Liaison & Ending:", "[ ] Homophonous verb root", "[ ] Different verb stem", "Verb root identical /e.ty.di/; subject on = /ɔ̃.n‿e.ty.di/ with [n] liaison")
]

LEVEL1_ARTICLES_TABLE = [
    # (Item, English, Gender/Category, Definite, Indefinite, Partitive)
    ("1. livre", "book", "Masc. Consonant", "le livre", "un livre", "[N/A count noun]"),
    ("2. table", "table", "Fem. Consonant", "la table", "une table", "[N/A count noun]"),
    ("3. ami", "male friend", "Masc. Vocalic", "l'ami", "un ami", "[N/A count noun]"),
    ("4. amie", "female friend", "Fem. Vocalic", "l'amie", "une amie", "[N/A count noun]"),
    ("5. eau", "water", "Fem. Vocalic / Mass", "l'eau", "[une eau = brand]", "de l'eau"),
    ("6. vin", "wine", "Masc. Consonant / Mass", "le vin", "un vin (vintage)", "du vin"),
    ("7. pain", "bread", "Masc. Consonant / Mass", "le pain", "un pain (loaf)", "du pain"),
    ("8. viande", "meat", "Fem. Consonant / Mass", "la viande", "une viande (type)", "de la viande"),
    ("9. café", "coffee", "Masc. Consonant / Mass", "le café", "un café (cup)", "du café"),
    ("10. argent", "money", "Masc. Vocalic / Mass", "l'argent", "[N/A un argent]", "de l'argent"),
    ("11. homme", "man", "Masc. Mute-H", "l'homme", "un homme", "[N/A count noun]"),
    ("12. héros", "hero", "Masc. Aspirate-H", "le héros", "un héros", "[N/A count noun]"),
    ("13. homard", "lobster", "Masc. Aspirate-H / Mass", "le homard", "un homard", "du homard"),
    ("14. histoire", "story/history", "Fem. Mute-H", "l'histoire", "une histoire", "[N/A count noun]"),
    ("15. haricot", "bean", "Masc. Aspirate-H", "le haricot", "un haricot", "des haricots"),
    ("16. fromage", "cheese", "Masc. Consonant / Mass", "le fromage", "un fromage (wheel)", "du fromage"),
    ("17. salade", "salad/lettuce", "Fem. Consonant / Mass", "la salade", "une salade", "de la salade"),
    ("18. bière", "beer", "Fem. Consonant / Mass", "la bière", "une bière (glass)", "de la bière"),
    ("19. huile", "oil", "Fem. Mute-H / Mass", "l'huile", "une huile (variety)", "de l'huile"),
    ("20. courage", "courage", "Masc. Abstract Mass", "le courage", "[N/A]", "du courage"),
    ("21. patience", "patience", "Fem. Abstract Mass", "la patience", "[N/A]", "de la patience"),
    ("22. ordinateur", "computer", "Masc. Vocalic", "l'ordinateur", "un ordinateur", "[N/A count noun]"),
    ("23. voiture", "car", "Fem. Consonant", "la voiture", "une voiture", "[N/A count noun]"),
    ("24. problème", "problem", "Masc. Consonant (-ème)", "le problème", "un problème", "[N/A count noun]"),
    ("25. système", "system", "Masc. Consonant (-ème)", "le système", "un système", "[N/A count noun]"),
    ("26. photo", "photograph", "Fem. Consonant (apocope)", "la photo", "une photo", "[N/A count noun]"),
    ("27. glace", "ice cream / ice", "Fem. Consonant / Mass", "la glace", "une glace (cone)", "de la glace"),
    ("28. sucre", "sugar", "Masc. Consonant / Mass", "le sucre", "un sucre (cube)", "du sucre"),
    ("29. sel", "salt", "Masc. Consonant / Mass", "le sel", "[N/A]", "du sel"),
    ("30. fruits", "fruits", "Masc. Plural", "les fruits", "des fruits", "des fruits")
]

LEVEL1_ADJECTIVES = [
    # Masc Sing, Fem Sing, Masc Plur, Fem Plur, English
    ("intelligent", "intelligente", "intelligents", "intelligentes", "intelligent"),
    ("grand", "grande", "grands", "grandes", "tall / big"),
    ("petit", "petite", "petits", "petites", "small"),
    ("content", "contente", "contents", "contentes", "happy / pleased"),
    ("lourd", "lourde", "lourds", "lourdes", "heavy"),
    ("vert", "verte", "verts", "vertes", "green"),
    ("chaud", "chaude", "chauds", "chaudes", "hot / warm"),
    ("froid", "froide", "froids", "froides", "cold"),
    ("amusant", "amusante", "amusants", "amusantes", "amusing / funny"),
    ("élégant", "élégante", "élégants", "élégantes", "elegant"),
    ("patient", "patiente", "patients", "patientes", "patient"),
    ("prudent", "prudente", "prudents", "prudentes", "careful / prudent")
]

LEVEL2_ORTHOGRAPHIC_VERBS = [
    ("1. (manger - nous)", "Nous ____________________ (manger) à la cantine universitaire à midi.", "mangeons", "-ger verb: mute 'e' inserted before -ons to keep soft [ʒ]"),
    ("2. (commencer - nous)", "Nous ____________________ (commencer) le cours de grammaire à neuf heures.", "commençons", "-cer verb: cédille 'ç' required before 'o' to maintain soft [s]"),
    ("3. (acheter - je)", "J'____________________ (acheter) ce manuel de syntaxe française.", "achète", "Stem change e -> è before mute syllable ending in -e"),
    ("4. (acheter - nous)", "Nous ____________________ (acheter) des fournitures pour le département.", "achetons", "No accent change before sounded syllable -ons: unstressed [ə] retained"),
    ("5. (acheter - ils)", "Ils ____________________ (acheter) de nouveaux ordinateurs portables.", "achètent", "Stem change e -> è before silent 3rd plural '-ent' [ɛt]"),
    ("6. (préférer - je)", "Je ____________________ (préférer) étudier dans le calme de la bibliothèque.", "préfère", "Stem change é -> è before mute ending in -e"),
    ("7. (préférer - nous)", "Nous ____________________ (préférer) lire les textes classiques.", "préférons", "Base stem préfér- retained before sounded -ons"),
    ("8. (préférer - elles)", "Elles ____________________ (préférer) la méthode communicative.", "préfèrent", "Stem change é -> è before silent 3rd plural '-ent'"),
    ("9. (appeler - j')", "J'____________________ (appeler) le secrétariat pour confirmer mon inscription.", "appelle", "Stem doubling l -> ll before silent -e to preserve open [ɛl]"),
    ("10. (appeler - nous)", "Nous ____________________ (appeler) les candidats un par un.", "appelons", "Single 'l' retained before sounded -ons: unstressed [ə]"),
    ("11. (appeler - ils)", "Ils ____________________ (appeler) le professeur par son titre.", "appellent", "Stem doubling l -> ll before silent 3rd plural '-ent'"),
    ("12. (jeter - je)", "Je ____________________ (jeter) les vieux brouillons dans la corbeille.", "jette", "Stem doubling t -> tt before silent -e to yield [ʒɛt]"),
    ("13. (jeter - nous)", "Nous ____________________ (jeter) un coup d'œil sur le calendrier des examens.", "jetons", "Single 't' retained before sounded -ons: unstressed [ə]"),
    ("14. (voyager - nous)", "Nous ____________________ (voyager) en train pour réduire l'empreinte carbone.", "voyageons", "-ger verb: retain 'e' before -ons: 'voyageons'"),
    ("15. (avancer - nous)", "Nous ____________________ (avancer) rapidement dans le programme théorique.", "avançons", "-cer verb: add cédille 'ç' before -ons: 'avançons'"),
    ("16. (lever - tu)", "Tu ____________________ (lever) la main pour poser une question.", "lèves", "Stem change e -> è before mute -es ending"),
    ("17. (espérer - vous)", "Vous ____________________ (espérer) obtenir une mention très bien.", "espérez", "Base stem espér- retained before sounded -ez"),
    ("18. (partager - nous)", "Nous ____________________ (partager) les documents de recherche avec les collègues.", "partageons", "-ger verb: retain 'e' before -ons: 'partageons'"),
    ("19. (remplacer - nous)", "Nous ____________________ (remplacer) l'ancien système par une plateforme moderne.", "remplaçons", "-cer verb: add cédille 'ç' before -ons: 'remplaçons'"),
    ("20. (peser - il)", "Ce dictionnaire ____________________ (peser) plus de deux kilogrammes.", "pèse", "Stem change e -> è before mute -e ending: 'pèse'")
]

LEVEL2_CONTRACTIONS_ITEMS = [
    ("1. aller + le restaurant", "Les étudiants vont ________ restaurant universitaire.", "au", "à + le -> au"),
    ("2. aller + la bibliothèque", "Claire marche ________ bibliothèque centrale.", "à la", "à + la -> à la (no contraction)"),
    ("3. aller + l'hôpital", "Le médecin se rend ________ hôpital militaire.", "à l'", "à + l' -> à l' (elision before vowel/mute h)"),
    ("4. aller + les archives", "Nous accédons ________ archives historiques.", "aux", "à + les -> aux"),
    ("5. parler + le doyen", "Le délégué parle ________ doyen de la faculté.", "au", "parler à + le -> au"),
    ("6. téléphoner + les directeurs", "La secrétaire téléphone ________ directeurs de laboratoire.", "aux", "téléphoner à + les -> aux"),
    ("7. penser + le problème", "Le mathématicien pense ________ problème de topologie.", "au", "penser à + le -> au"),
    ("8. répondre + les questions", "Le conférencier répond ________ questions des auditeurs.", "aux", "répondre à + les -> aux"),
    ("9. venir + le bureau", "Le professeur arrive tout droit ________ bureau administratif.", "du", "venir de + le -> du"),
    ("10. venir + la gare", "Le train arrive en provenance ________ gare Saint-Lazare.", "de la", "de + la -> de la (no contraction)"),
    ("11. venir + l'étranger", "Ces chercheurs reviennent ________ étranger après un an.", "de l'", "de + l' -> de l' (elision before vowel)"),
    ("12. venir + les États-Unis", "Ces spécialistes arrivent ________ États-Unis ce matin.", "des", "de + les -> des"),
    ("13. parler + le projet", "Les ingénieurs discutent et parlent ________ projet d'infrastructure.", "du", "parler de + le -> du"),
    ("14. avoir besoin + les notes", "L'étudiant a besoin ________ notes de cours pour réviser.", "des", "avoir besoin de + les -> des"),
    ("15. avoir peur + le bruit", "L'enfant a peur ________ bruit des feux d'artifice.", "du", "avoir peur de + le -> du"),
    ("16. se souvenir + les vacances", "Les amis se souviennent ________ vacances d'été en Provence.", "des", "se souvenir de + les -> des")
]

LEVEL2_DISAMBIGUATION_ITEMS = [
    ("1. Elle boit des jus de fruits le matin.", "[ ] Partitive (unspecified mass/plural)", "[ ] Contracted (de + les)", "[ ] Indefinite Plural", "Indefinite / Partitive plural: 'des jus' = plural mass drinks"),
    ("2. Le professeur parle des résultats de l'examen.", "[ ] Partitive", "[ ] Contracted preposition (de + les)", "[ ] Indefinite Plural", "Contracted: parler de + les résultats -> des résultats"),
    ("3. Il y a des arbres séculaires dans le parc.", "[ ] Partitive", "[ ] Contracted preposition (de + les)", "[ ] Indefinite Plural", "Indefinite plural: plural count noun (un arbre -> des arbres)"),
    ("4. Nous revenons des îles de la Méditerranée.", "[ ] Partitive", "[ ] Contracted preposition (de + les)", "[ ] Indefinite Plural", "Contracted: revenir de + les îles -> des îles"),
    ("5. Vous commandez des cafés pour toute l'équipe.", "[ ] Partitive", "[ ] Contracted preposition (de + les)", "[ ] Indefinite Plural", "Indefinite plural (plural of countable portions: un café -> des cafés)"),
    ("6. La peur des représailles paralyse les témoins.", "[ ] Partitive", "[ ] Contracted preposition (de + les)", "[ ] Indefinite Plural", "Contracted: la peur de + les représailles -> des représailles")
]

LEVEL2_PLURALS_ITEMS = [
    ("1. un journal national", "________________________________________", "des journaux nationaux", "-al -> -aux for both noun and adjective"),
    ("2. un animal loyal", "________________________________________", "des animaux loyaux", "-al -> -aux for both noun and adjective"),
    ("3. un cheval sauvage", "________________________________________", "des chevaux sauvages", "-al -> -aux for noun; regular +s for adjective"),
    ("4. un travail original", "________________________________________", "des travaux originaux", "-ail -> -aux (travail) and -al -> -aux (original)"),
    ("5. un festival naval", "________________________________________", "des festivals navals", "REGULAR EXCEPTION: festival -> festivals; naval -> navals (+s)"),
    ("6. un carnaval banal", "________________________________________", "des carnavals banals", "REGULAR EXCEPTION: carnaval -> carnavals; banal -> banals (+s)"),
    ("7. un beau tableau", "________________________________________", "de beaux tableaux", "-eau -> -eaux; note pre-nominal 'des' becomes 'de' !"),
    ("8. un nouveau château", "________________________________________", "de nouveaux châteaux", "-eau -> -eaux; note pre-nominal 'des' becomes 'de' !"),
    ("9. un oiseau rare", "________________________________________", "des oiseaux rares", "-eau -> -eaux for noun; regular +s for adjective"),
    ("10. un pays gris", "________________________________________", "des pays gris", "INVARIABLE: pays ends in -s, gris ends in -s"),
    ("11. une voix douce", "________________________________________", "des voix douces", "INVARIABLE: voix ends in -x; regular +s for feminine douces"),
    ("12. un gaz dangereux", "________________________________________", "des gaz dangereux", "INVARIABLE: gaz ends in -z, dangereux ends in -x"),
    ("13. un vieux choix", "________________________________________", "de vieux choix", "INVARIABLE: vieux ends in -x, choix ends in -x; note 'de vieux'"),
    ("14. un nez pointu", "________________________________________", "des nez pointus", "INVARIABLE: nez ends in -z; pointu takes +s"),
    ("15. un hôpital régional", "________________________________________", "des hôpitaux régionaux", "-al -> -aux for both noun and adjective")
]

LEVEL3_NEGATION_ITEMS = [
    ("1. Affirmative: J'ai un stylo noir.\nNegative:", "Je n'ai pas ____________________ stylo noir.", "de", "Direct transitive 'avoir': indefinite 'un' collapses to 'de'"),
    ("2. Affirmative: Nous mangeons du fromage de chèvre.\nNegative:", "Nous ne mangeons pas ____________________ fromage de chèvre.", "de", "Direct transitive 'manger': partitive 'du' collapses to 'de'"),
    ("3. Affirmative: Elle achète de la confiture de fraises.\nNegative:", "Elle n'achète pas ____________________ confiture de fraises.", "de", "Direct transitive 'acheter': partitive 'de la' collapses to 'de'"),
    ("4. Affirmative: Ils ont de l'argent pour voyager.\nNegative:", "Ils n'ont pas ____________________ argent pour voyager.", "d'", "Elision: 'de' elides to 'd'' before vowel: pas d'argent"),
    ("5. Affirmative: Vous commandez des boissons gazeuses.\nNegative:", "Vous ne commandez pas ____________________ boissons gazeuses.", "de", "Direct transitive: indefinite plural 'des' collapses to 'de'"),
    ("6. Affirmative: C'est un roman fascinant.\nNegative:", "Ce n'est pas ____________________ roman fascinant.", "un", "IDENTITY VERB 'ÊTRE': does NOT collapse! Remains 'un'"),
    ("7. Affirmative: C'est une erreur impardonnable.\nNegative:", "Ce n'est pas ____________________ erreur impardonnable.", "une", "IDENTITY VERB 'ÊTRE': preserves indefinite feminine 'une'"),
    ("8. Affirmative: Ce sont des professeurs de linguistique.\nNegative:", "Ce ne sont pas ____________________ professeurs de linguistique.", "des", "IDENTITY VERB 'ÊTRE': preserves indefinite plural 'des'"),
    ("9. Affirmative: J'aime le café sans sucre.\nNegative:", "Je n'aime pas ____________________ café sans sucre.", "le", "VERB OF PREFERENCE: 'aimer' takes definite article 'le' in negation"),
    ("10. Affirmative: Nous préférons la viande rouge.\nNegative:", "Nous ne préférons pas ____________________ viande rouge.", "la", "VERB OF PREFERENCE: 'préférer' retains definite article 'la'"),
    ("11. Affirmative: Il adore les épinards cuits.\nNegative:", "Il n'adore pas ____________________ épinards cuits.", "les", "VERB OF PREFERENCE: 'adorer' retains definite article 'les'"),
    ("12. Affirmative: Le touriste cherche une chambre d'hôtel.\nNegative:", "Le touriste ne cherche pas ____________________ chambre d'hôtel.", "de", "Direct transitive 'chercher': indefinite 'une' collapses to 'de'"),
    ("13. Affirmative: Elle boit de l'eau minérale.\nNegative:", "Elle ne boit pas ____________________ eau minérale.", "d'", "Direct transitive 'boire': partitive 'de l'' collapses to 'd''"),
    ("14. Affirmative: C'est du vin de Bordeaux.\nNegative:", "Ce n'est pas ____________________ vin de Bordeaux.", "du", "IDENTITY VERB 'ÊTRE': predicate identification preserves 'du'"),
    ("15. Affirmative: Nous possédons des dictionnaires rares.\nNegative:", "Nous ne possédons pas ____________________ dictionnaires rares.", "de", "Direct transitive 'posséder': indefinite 'des' collapses to 'de'")
]

LEVEL3_BAGS_ITEMS = [
    ("1. un + beau + appartement", "________________________________________", "un bel appartement", "Pre-vocalic masculine singular: 'beau' -> 'bel' before vowel"),
    ("2. un + nouveau + étudiant", "________________________________________", "un nouvel étudiant", "Pre-vocalic masculine singular: 'nouveau' -> 'nouvel' before vowel"),
    ("3. un + vieux + homme", "________________________________________", "un vieil homme", "Pre-vocalic masculine singular: 'vieux' -> 'vieil' before mute-h"),
    ("4. un + beau + arbre", "________________________________________", "un bel arbre", "Pre-vocalic masculine singular: 'beau' -> 'bel' before vowel"),
    ("5. des + beau + tableaux", "________________________________________", "de beaux tableaux", "Pre-nominal plural: 'des' reduces to 'de' before preceding adjective"),
    ("6. des + grand + édifices", "________________________________________", "de grands édifices", "Pre-nominal plural: 'des' reduces to 'de' before BAGS adjective"),
    ("7. des + vieux + amis", "________________________________________", "de vieux amis", "Pre-nominal plural: 'des' reduces to 'de' before BAGS adjective"),
    ("8. des + jeune + filles", "________________________________________", "de jeunes filles", "Pre-nominal plural: 'des' reduces to 'de' before BAGS adjective")
]

LEVEL3_MOBILE_ADJECTIVES_ITEMS = [
    ("1. grand: (a) un homme de haute taille / (b) un homme illustre dans l'Histoire",
     "(a) un ____________________ | (b) un ____________________",
     "(a) un homme grand | (b) un grand homme",
     "Post-nominal = literal physical stature; Pre-nominal = historical greatness/distinction"),
    ("2. propre: (a) mes mains qui ne sont pas sales / (b) mes mains personnelles",
     "(a) des ____________________ | (b) mes ____________________",
     "(a) des mains propres | (b) mes propres mains",
     "Post-nominal = clean/unsoiled; Pre-nominal = own/personal possession"),
    ("3. pauvre: (a) un homme sans ressources financières / (b) un homme digne de pitié",
     "(a) un ____________________ | (b) un ____________________",
     "(a) un homme pauvre | (b) un pauvre homme",
     "Post-nominal = indigent/destitute; Pre-nominal = pitiful/unfortunate"),
    ("4. ancien: (a) mon professeur de l'année dernière / (b) un meuble du dix-septième siècle",
     "(a) mon ____________________ | (b) un ____________________",
     "(a) mon ancien professeur | (b) un meuble ancien",
     "Pre-nominal = former/previous; Post-nominal = antique/ancient in age"),
    ("5. certain: (a) une victoire indiscutable et prouvée / (b) une timidité ressentie mais diffuse",
     "(a) une ____________________ | (b) une ____________________",
     "(a) une victoire certaine | (b) une certaine timidité",
     "Post-nominal = definite/sure/proven; Pre-nominal = a particular/moderate unspecified")
]

LEVEL3_CONCORD_ITEMS = [
    ("1. Marc et Claire sont très ____________________ (attentif) pendant la conférence.", "attentifs", "Mixed-gender compound subject: masculine plural dominates (attentifs)"),
    ("2. La directrice et sa secrétaire sont ____________________ (épuisé) par le travail.", "épuisées", "All-feminine compound subject: feminine plural (épuisées)"),
    ("3. Une foule de manifestants ____________________ (être - singulier) ____________________ (rassemblé).", "est rassemblée / sont rassemblés", "Grammatical agreement with collective sing: 'est rassemblée' (or semantic plur)"),
    ("4. La plupart des étudiants ____________________ (être) ____________________ (prêt) pour l'examen.", "sont prêts", "'La plupart de' takes plural verb agreement and plural predicate (prêts)"),
    ("5. Ces nouvelles théories paraissent tout à fait ____________________ (crédible).", "crédibles", "Copular verb 'paraître': predicate adjective agrees with fem plural (crédibles)"),
    ("6. Les deux robes qu'elle porte semblent très ____________________ (élégant).", "élégantes", "Copular verb 'sembler': agrees with feminine plural subject (robes -> élégantes)"),
    ("7. Elle a acheté des vestes ____________________ (marron) et des foulards ____________________ (orange).", "marron / orange", "INVARIABLE COLOR NOUNS: colors derived from nouns (marron, orange) never agree!"),
    ("8. Les rideaux du salon sont ____________________ (bleu clair).", "bleu clair", "COMPOUND COLOR ADJECTIVE: modified by 'clair', remains strictly invariable"),
    ("9. Le père et la fille sont ____________________ (fier) de leurs accomplissements scientifiques.", "fiers", "Mixed-gender compound subject: masculine plural (fiers)"),
    ("10. Cette proposition de loi demeure ____________________ (inacceptable) pour les députés.", "inacceptable", "Copular verb 'demeurer': agrees with fem singular subject (inacceptable)"),
    ("11. Des chaussures ____________________ (vert foncé) ont été trouvées dans le vestiaire.", "vert foncé", "COMPOUND COLOR ADJECTIVE: invariable ('vert foncé', never *vertes foncées)"),
    ("12. La majorité des membres a voté et est ____________________ (favorable) au projet.", "favorable", "Predicative agreement with singular grammatical collective 'majorité'")
]

LEVEL4_PASSAGE_TEXT = (
    "Hier matin, Paul et sa collègue Marie ont décidé d'aller déjeuner ensemble. "
    "Nous mangons souvent dans un petit bistrot du quartier, mais aujourd'hui nous commencions un nouveau projet important. "
    "Les étudiants de première année parlent fort et ils regardes le tableau d'affichage. "
    "Paul a dit : « Allons à le nouveau bistrot près de l'université ! » "
    "Marie a répondu : « Attention, nous n'avons pas des euros liquides sur nous, et le gérant refuse les chèques de les clients inconnus. "
    "En outre, ce n'est pas de bon restaurant gastronomique, c'est juste une cafétéria ordinaire. "
    "Et Paul ne préfère pas de thé noir, il boit seulement du café espresso. "
    "Regarde là-bas, c'est un beau édifice avec des beaux tableaux modernes dans la vitrine ! » "
    "Dans la salle, un homme grand célèbre discutait avec des journalistes. "
    "Marie, Paul et Sophie étaient assises à une table en bois massif. "
    "La serveuse avait une voix très doux et a apporté les journal nationaux du matin. "
    "Paul a chuchoté : « Le patron achete toujours ses produits locaux au marché central. »"
)

LEVEL4_PASSAGE_ERRORS = [
    ("1. nous mangons", "Orthographe verbe -ger", "Missed 'e' before -ons: hard [ɡ] instead of soft [ʒ]", "nous mangeons"),
    ("2. nous commencions", "Orthographe / Temps", "Incorrect imperfect ending or missing cédille; present indicative requires -çons", "nous commençons"),
    ("3. ils regardes", "Conjugaison verbe -ER", "Spurious 2nd pers '-es' on 3rd person plural subject 'ils'", "ils regardent"),
    ("4. à le nouveau bistrot", "Contraction obligatoire", "Illegal uncontracted form: 'à + le' must contract to 'au'", "au nouveau bistrot"),
    ("5. pas des euros", "Effondrement sous négation", "Direct transitive verb 'avoir' in negative: indefinite 'des' collapses to 'd''", "pas d'euros"),
    ("6. de les clients", "Contraction obligatoire", "Illegal uncontracted form: 'de + les' must contract to 'des'", "des clients"),
    ("7. ce n'est pas de bon restaurant", "Exception verbe d'identité être", "Linking verb 'être' in negation preserves indefinite article: 'un'", "ce n'est pas un bon restaurant"),
    ("8. ne préfère pas de thé", "Verbe de préférence en négation", "Verbs of preference ('préférer') retain definite article: 'le'", "ne préfère pas le thé"),
    ("9. un beau édifice", "Forme pré-vocalique euphonique", "Masculine 'beau' before vowel-initial noun must become 'bel'", "un bel édifice"),
    ("10. des beaux tableaux", "Réduction de l'indéfini pluriel", "Indefinite plural 'des' reduces to 'de' before pre-nominal adjective", "de beaux tableaux"),
    ("11. un homme grand célèbre", "Position adjectif mobile", "Intended historical greatness requires pre-nominal 'grand homme'", "un grand homme"),
    ("12. étaient assises", "Accord sujet mixte", "Mixed-gender compound subject (Marie, Paul, Sophie) requires masc plural", "étaient assis"),
    ("13. une voix très doux", "Morphologie féminin irrégulier", "Adjective 'doux' irregular feminine is 'douce', not invariant", "une voix très douce"),
    ("14. les journal nationaux", "Pluriel irrégulier en -al", "Noun 'journal' pluralizes to 'journaux', not 'journal'", "les journaux nationaux"),
    ("15. achete", "Alternance accentuelle stem-change", "Verb 'acheter' requires grave accent è before mute -e syllable: 'achète'", "achète")
]

LEVEL4_TRANSLATIONS = [
    {
        "en": "1. We are eating some delicious bread at the restaurant, but we are not ordering any wine.",
        "fr": "Nous mangeons du pain délicieux au restaurant, mais nous ne commandons pas de vin.",
        "notes": "-ger spelling (mangeons) + partitive (du pain) + contraction (au restaurant) + negative reduction (pas de vin)."
    },
    {
        "en": "2. The former professor does not call the new male student because he does not have enough time.",
        "fr": "L'ancien professeur n'appelle pas le nouvel étudiant parce qu'il n'a pas assez de temps.",
        "notes": "Mobile adjective (ancien professeur) + stem doubling (appelle) + pre-vocalic (nouvel étudiant) + adverb quantity (assez de temps)."
    },
    {
        "en": "3. Are these not ancient monuments? Yes, but they do not speak of the country's dark secrets.",
        "fr": "Ne sont-ce pas des monuments anciens ? Oui, mais ils ne parlent pas des secrets sombres du pays.",
        "notes": "Negative être preserves 'des' + post-nominal 'anciens' + parler de + contraction (des secrets, du pays)."
    },
    {
        "en": "4. We are beginning to buy some beautiful antique tables for the director's new office.",
        "fr": "Nous commençons à acheter de belles tables anciennes pour le nouveau bureau du directeur.",
        "notes": "-cer spelling (commençons) + infinitive acheter + pre-nominal 'des' -> 'de' (de belles tables) + contraction (du directeur)."
    },
    {
        "en": "5. Sophie and Marc are proud of the national newspapers, but they never throw their old books away.",
        "fr": "Sophie et Marc sont fiers des journaux nationaux, mais ils ne jettent jamais leurs vieux livres.",
        "notes": "Compound mixed subject (fiers masc plur) + contraction (des journaux) + -al -> -aux (nationaux) + stem doubling (jettent) + BAGS (vieux livres)."
    },
    {
        "en": "6. The head of the company does not like dark chocolate, so he prefers fresh milk from the farm.",
        "fr": "Le chef de l'entreprise n'aime pas le chocolat noir, donc il préfère le lait frais de la ferme.",
        "notes": "Preference verb negation retains definite (le chocolat) + stem change (préfère) + irregular fem/masc (frais) + preposition (de la ferme)."
    },
    {
        "en": "7. My own sister bought some light-blue dresses and some orange shoes at the market.",
        "fr": "Ma propre sœur a acheté des robes bleu clair et des chaussures orange au marché.",
        "notes": "Mobile adjective (ma propre sœur) + compound color invariable (bleu clair) + noun-derived color invariable (orange) + contraction (au marché)."
    },
    {
        "en": "8. A crowd of angry tourists is answering the police officer's questions near the train station.",
        "fr": "Une foule de touristes en colère répond aux questions du policier près de la gare.",
        "notes": "Collective singular concord (répond) + verb governing à + contraction (aux questions) + contraction (du policier, de la gare)."
    },
    {
        "en": "9. We are sharing some fresh water with our friends, but we don't have any glasses.",
        "fr": "Nous partageons de l'eau fraîche avec nos amis, mais nous n'avons pas de verres.",
        "notes": "-ger spelling (partageons) + partitive vocalic (de l'eau fraîche) + direct negative reduction (pas de verres)."
    },
    {
        "en": "10. The great general lives in an old hotel, but he does not fear the dangerous wolves of the forest.",
        "fr": "Le grand général habite dans un vieil hôtel, mais il n'a pas peur des loups dangereux de la forêt.",
        "notes": "Mobile adjective greatness (grand général) + pre-vocalic mute-h (vieil hôtel) + avoir peur de + contraction (des loups) + contraction (de la forêt)."
    }
]

print("Data definitions successfully compiled.")

# =========================================================================
# DOCX BUILDER IMPLEMENTATION
# =========================================================================

def build_docx():
    doc = docx.Document()
    
    # Page setup: 0.75 in margins
    for s in doc.sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)
        
        # Header / Footer
        header = s.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("Mastering Core French Syntax  |  Applied Linguistics Division")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = MUTED_RGB
        
        footer = s.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("University Syntax Series  •  Zero-Tolerance Diagnostic Assessment  •  Level 1 to 5")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = MUTED_RGB

    def add_p(text="", space_before=0, space_after=3, bold=False, italic=False, color=DARK_RGB, size=10, align=WD_ALIGN_PARAGRAPH.LEFT):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        if text:
            r = p.add_run(text)
            r.font.name = "Calibri"
            r.font.size = Pt(size)
            r.font.bold = bold
            r.font.italic = italic
            r.font.color.rgb = color
        return p

    def add_h1(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(4)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = INDIGO_RGB
        
        # Divider line
        t = doc.add_table(rows=1, cols=1)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t.columns[0].width = Inches(7.0)
        c = t.cell(0, 0)
        style_cell(c, fill_hex=INDIGO_HEX, borders={}, pad_tb=15, pad_lr=0)
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    def add_h2(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(3)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(11.5)
        r.font.bold = True
        r.font.color.rgb = BURGUNDY_RGB
        return p

    def add_callout(title, text, callout_type="info"):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(7.0)
        cell = tbl.cell(0, 0)
        
        if callout_type == "alert":
            b_col = AMBER_HEX
            bg_col = ALERT_BG
            t_col = AMBER_RGB
        elif callout_type == "danger":
            b_col = BURGUNDY_HEX
            bg_col = DANGER_BG
            t_col = BURGUNDY_RGB
        elif callout_type == "teal":
            b_col = TEAL_HEX
            bg_col = "F0FDFA"
            t_col = TEAL_RGB
        else:
            b_col = INDIGO_HEX
            bg_col = CALLOUT_BG
            t_col = INDIGO_RGB

        borders = {'left': {'val': 'single', 'sz': 24, 'color': b_col}}
        style_cell(cell, fill_hex=bg_col, borders=borders, pad_tb=100, pad_lr=140)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        rt = p.add_run(title)
        rt.font.name = "Calibri"
        rt.font.size = Pt(10)
        rt.font.bold = True
        rt.font.color.rgb = t_col
        
        p2 = cell.add_paragraph()
        p2.paragraph_format.space_before = Pt(2)
        p2.paragraph_format.space_after = Pt(0)
        rc = p2.add_run(text)
        rc.font.name = "Calibri"
        rc.font.size = Pt(9.5)
        rc.font.color.rgb = DARK_RGB
        
        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    # ------------------ COVER HEADER ------------------
    cover_tbl = doc.add_table(rows=1, cols=1)
    cover_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cover_tbl.autofit = False
    cover_tbl.columns[0].width = Inches(7.0)
    c_cell = cover_tbl.cell(0, 0)
    style_cell(c_cell, fill_hex=INDIGO_HEX, borders={}, pad_tb=260, pad_lr=200)
    
    cp1 = c_cell.paragraphs[0]
    cp1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp1.paragraph_format.space_before = Pt(0)
    cp1.paragraph_format.space_after = Pt(4)
    rt = cp1.add_run("MASTERING CORE FRENCH SYNTAX")
    rt.font.name = "Calibri"
    rt.font.size = Pt(18)
    rt.font.bold = True
    rt.font.color.rgb = RGBColor(255, 255, 255)
    
    cp2 = c_cell.add_paragraph()
    cp2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp2.paragraph_format.space_before = Pt(2)
    cp2.paragraph_format.space_after = Pt(4)
    rs = cp2.add_run("Regular -ER Verbs, The Complete Article System, Contractions, and Nominal/Adjective Agreement")
    rs.font.name = "Calibri"
    rs.font.size = Pt(11)
    rs.font.bold = True
    rs.font.color.rgb = RGBColor(254, 240, 138) # Soft yellow/gold

    cp3 = c_cell.add_paragraph()
    cp3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp3.paragraph_format.space_before = Pt(2)
    cp3.paragraph_format.space_after = Pt(0)
    rm = cp3.add_run("University Division of Applied Linguistics • Rigorous Tiered Practice Workbook (Levels 1 to 5)")
    rm.font.name = "Calibri"
    rm.font.size = Pt(9)
    rm.font.italic = True
    rm.font.color.rgb = RGBColor(226, 232, 240)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    add_callout(
        "CURRICULUM ARCHITECTURE & PEDAGOGICAL PROTOCOL",
        "This practice workbook is structured as an uncompromising progression from isolated morphosyntactic mechanics "
        "to multi-variable communicative synthesis. Each level isolates specific phonological and syntactic friction points "
        "often misdiagnosed by intermediate learners: the silent third-person plural inflection, velar-stop preservation in -ger/-cer stems, "
        "prepositional rection triggers, quantitative collapse under direct negation versus identity predicates, and euphonic pre-vocalic adjective alternations. "
        "Work sequentially without external references; verify against Level 5 only upon section completion.",
        "danger"
    )

    # =============================================================
    # LEVEL 1
    # =============================================================
    add_h1("LEVEL 1: ELEMENTARY DRILLS (Isolated Foundations)")
    
    add_h2("Part A: Regular -ER Verb Paradigm Isolation & Silent-Ending Discrimination")
    add_p("Supply the correct present-indicative inflection for each subject pronoun. Maintain strict orthographic elision where required.")

    for v_info in LEVEL1_VERBS_PARADIGMS:
        add_p(f"Target Verb: {v_info['verb'].upper()} — {v_info['notes']}", bold=True, color=DARK_RGB, space_before=4, space_after=2)
        v_tbl = doc.add_table(rows=4, cols=4)
        v_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        v_tbl.columns[0].width = Inches(1.5)
        v_tbl.columns[1].width = Inches(2.0)
        v_tbl.columns[2].width = Inches(1.5)
        v_tbl.columns[3].width = Inches(2.0)
        
        # Header
        headers = ["Pronoun", "Write-in Conjugation", "Pronoun", "Write-in Conjugation"]
        for ci, h in enumerate(headers):
            c = v_tbl.cell(0, ci)
            style_cell(c, fill_hex=CALLOUT_BG, pad_tb=40, pad_lr=60)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(h)
            r.font.bold = True
            r.font.size = Pt(9)
            r.font.color.rgb = INDIGO_RGB

        for ri, (p1, ans1, p2, ans2) in enumerate(v_info["rows"]):
            row_idx = ri + 1
            # Col 0
            c0 = v_tbl.cell(row_idx, 0)
            style_cell(c0, pad_tb=40, pad_lr=60)
            p = c0.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.add_run(p1).font.size = Pt(9.5)
            # Col 1
            c1 = v_tbl.cell(row_idx, 1)
            style_cell(c1, pad_tb=40, pad_lr=60)
            p = c1.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.add_run("____________________").font.size = Pt(9.5)
            # Col 2
            c2 = v_tbl.cell(row_idx, 2)
            style_cell(c2, pad_tb=40, pad_lr=60)
            p = c2.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.add_run(p2).font.size = Pt(9.5)
            # Col 3
            c3 = v_tbl.cell(row_idx, 3)
            style_cell(c3, pad_tb=40, pad_lr=60)
            p = c3.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.add_run("____________________").font.size = Pt(9.5)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

    add_p("Acoustic Discrimination: Silent Ending & Pronunciation Stress-Test", bold=True, color=INDIGO_RGB, space_before=6)
    add_p("Check the box that accurately reflects the acoustic phonology of the pair:")
    for pair, prompt, opt1, opt2, _ in LEVEL1_PHONETIC_ITEMS:
        add_p(f"• {pair} — {prompt} {opt1}   {opt2}", space_before=1, space_after=2)

    # Part B
    add_h2("Part B: The Complete Article Classification Matrix (Definite, Indefinite, Partitive)")
    add_p("Assign the precise Definite (le, la, l', les), Indefinite (un, une, des), and Partitive (du, de la, de l', des / N/A) article to each noun. Classify its morphophonological class.")

    art_tbl = doc.add_table(rows=len(LEVEL1_ARTICLES_TABLE)+1, cols=5)
    art_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    art_tbl.columns[0].width = Inches(1.5)
    art_tbl.columns[1].width = Inches(1.5)
    art_tbl.columns[2].width = Inches(1.3)
    art_tbl.columns[3].width = Inches(1.3)
    art_tbl.columns[4].width = Inches(1.4)

    art_headers = ["Noun & Gloss", "Morphological Class", "Definite [le/la/l']", "Indefinite [un/une/des]", "Partitive [du/de la/de l']"]
    for ci, h in enumerate(art_headers):
        c = art_tbl.cell(0, ci)
        style_cell(c, fill_hex=INDIGO_HEX, pad_tb=40, pad_lr=50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    for ri, (n_w, gloss, cls_w, d_a, i_a, p_a) in enumerate(LEVEL1_ARTICLES_TABLE):
        row_idx = ri + 1
        bg = LIGHT_BG if ri % 2 == 1 else "FFFFFF"
        # Noun
        c0 = art_tbl.cell(row_idx, 0)
        style_cell(c0, fill_hex=bg, pad_tb=30, pad_lr=40)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        p0.add_run(f"{n_w} ({gloss})").font.size = Pt(8)
        # Class
        c1 = art_tbl.cell(row_idx, 1)
        style_cell(c1, fill_hex=bg, pad_tb=30, pad_lr=40)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        p1.add_run(cls_w).font.size = Pt(8)
        # Definite
        c2 = art_tbl.cell(row_idx, 2)
        style_cell(c2, fill_hex=bg, pad_tb=30, pad_lr=40)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        p2.add_run("[  ] ____________").font.size = Pt(8)
        # Indefinite
        c3 = art_tbl.cell(row_idx, 3)
        style_cell(c3, fill_hex=bg, pad_tb=30, pad_lr=40)
        p3 = c3.paragraphs[0]
        p3.paragraph_format.space_before = Pt(0)
        p3.paragraph_format.space_after = Pt(0)
        p3.add_run("[  ] ____________").font.size = Pt(8)
        # Partitive
        c4 = art_tbl.cell(row_idx, 4)
        style_cell(c4, fill_hex=bg, pad_tb=30, pad_lr=40)
        p4 = c4.paragraphs[0]
        p4.paragraph_format.space_before = Pt(0)
        p4.paragraph_format.space_after = Pt(0)
        p4.add_run("[  ] ____________").font.size = Pt(8)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Part C
    add_h2("Part C: Foundational Adjective Morphology (Regular Concord: +e, +s)")
    add_p("Supply all four inflectional forms (Masculine Singular, Feminine Singular, Masculine Plural, Feminine Plural) for each regular descriptive adjective.")

    adj_tbl = doc.add_table(rows=len(LEVEL1_ADJECTIVES)+1, cols=5)
    adj_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    adj_tbl.columns[0].width = Inches(1.4)
    adj_tbl.columns[1].width = Inches(1.4)
    adj_tbl.columns[2].width = Inches(1.4)
    adj_tbl.columns[3].width = Inches(1.4)
    adj_tbl.columns[4].width = Inches(1.4)

    adj_headers = ["Base Masc. Sing.", "Feminine Sing. (+e)", "Masc. Plural (+s)", "Feminine Plural (+es)", "Gloss / Root"]
    for ci, h in enumerate(adj_headers):
        c = adj_tbl.cell(0, ci)
        style_cell(c, fill_hex=CALLOUT_BG, pad_tb=40, pad_lr=50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = INDIGO_RGB

    for ri, (ms, fs, mp, fp, gl) in enumerate(LEVEL1_ADJECTIVES):
        row_idx = ri + 1
        bg = LIGHT_BG if ri % 2 == 1 else "FFFFFF"
        # Masc Sing
        c0 = adj_tbl.cell(row_idx, 0)
        style_cell(c0, fill_hex=bg, pad_tb=30, pad_lr=40)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_before = Pt(0)
        p0.paragraph_format.space_after = Pt(0)
        p0.add_run(ms).font.size = Pt(8.5)
        # Fem Sing
        c1 = adj_tbl.cell(row_idx, 1)
        style_cell(c1, fill_hex=bg, pad_tb=30, pad_lr=40)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(0)
        p1.add_run("__________________").font.size = Pt(8.5)
        # Masc Plur
        c2 = adj_tbl.cell(row_idx, 2)
        style_cell(c2, fill_hex=bg, pad_tb=30, pad_lr=40)
        p2 = c2.paragraphs[0]
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(0)
        p2.add_run("__________________").font.size = Pt(8.5)
        # Fem Plur
        c3 = adj_tbl.cell(row_idx, 3)
        style_cell(c3, fill_hex=bg, pad_tb=30, pad_lr=40)
        p3 = c3.paragraphs[0]
        p3.paragraph_format.space_before = Pt(0)
        p3.paragraph_format.space_after = Pt(0)
        p3.add_run("__________________").font.size = Pt(8.5)
        # Gloss
        c4 = adj_tbl.cell(row_idx, 4)
        style_cell(c4, fill_hex=bg, pad_tb=30, pad_lr=40)
        p4 = c4.paragraphs[0]
        p4.paragraph_format.space_before = Pt(0)
        p4.paragraph_format.space_after = Pt(0)
        p4.add_run(gl).font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =============================================================
    # LEVEL 2
    # =============================================================
    add_h1("LEVEL 2: INTERMEDIATE SYNTACTIC MECHANICS (Spelling Shifts & Contractions)")
    
    add_callout(
        "ORTHOGRAPHIC PRESERVATION MECHANISM: VELAR STOPS & ACCENT ALTERNATIONS",
        "1. In -ger verbs, the stem ends in soft [ʒ]. Before 'a' and 'o' (e.g. nous mangeons), an unaccented 'e' must be maintained "
        "to prevent the letter 'g' from hardening into [ɡ].\n"
        "2. In -cer verbs, the stem ends in soft [s]. Before 'a' and 'o' (e.g. nous commençons), a cédille 'ç' is obligatory "
        "to prevent hardening into [k].\n"
        "3. Stem-changing verbs (acheter, préférer, appeler, jeter) adjust their stem vowel or double the consonant to guarantee "
        "an open [ɛ] sound before a mute syllable ending in silent -e, -es, or -ent.",
        "teal"
    )

    add_h2("Part A: Orthographic & Phonetic Preservation Boot-Camp (20 Targeted Inflections)")
    add_p("Conjugate the verb in parentheses to complete each academic sentence. Pay rigorous attention to nous, je, and ils/elles forms.")

    for item_lbl, sent, _, _ in LEVEL2_ORTHOGRAPHIC_VERBS:
        add_p(f"{sent}", space_before=1, space_after=3)

    add_h2("Part B: Contraction Triggers & Prepositional Rection (16 Rapid Completions)")
    add_p("Complete each sentence by applying mandatory contraction for prepositions 'à' and 'de' with definite articles (au, à la, à l', aux / du, de la, de l', des).")

    for trig, sent, _, _ in LEVEL2_CONTRACTIONS_ITEMS:
        add_p(f"• [{trig}] -> {sent}", space_before=1, space_after=2)

    add_p("Disambiguation Drill: Partitive 'des' vs. Contracted 'des' (de + les) vs. Indefinite 'des'", bold=True, color=INDIGO_RGB, space_before=6)
    add_p("Analyze each occurrence of 'des'. Mark the correct grammatical classification and explain the syntactic trigger:")
    for sent, o1, o2, o3, _ in LEVEL2_DISAMBIGUATION_ITEMS:
        add_p(f"• {sent}\n   {o1}   {o2}   {o3}\n   Syntactic Justification: __________________________________________________________________", space_before=2, space_after=3)

    add_h2("Part C: Morphological Pluralization of Irregular Nouns & Adjectives (15 Conversions)")
    add_p("Convert each singular noun phrase into the plural. Be vigilant of invariable endings (-s, -x, -z), -al -> -aux alternations, and regular exceptions.")

    for sing_phr, _, _, _ in LEVEL2_PLURALS_ITEMS:
        add_p(f"• {sing_phr}  ===>  ____________________________________________________________", space_before=1, space_after=2)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =============================================================
    # LEVEL 3
    # =============================================================
    add_h1("LEVEL 3: ADVANCED APPLICATION & SEMANTIC DISAMBIGUATION")
    
    add_callout(
        "THE SYNTACTIC COLLAPSE PARADOX: NEGATION, IDENTITY, AND PREFERENCE",
        "Rule 1 (The Quantitative Collapse): Under direct transitive negation (avoir, manger, acheter, vouloir), indefinite (un, une, des) "
        "and partitive (du, de la, de l', des) articles collapse into the preposition of depleted quantity 'de / d''.\n"
        "Rule 2 (The Identity Verb Exception): When negated across the equative copula 'être' (ce n'est pas / ce ne sont pas), "
        "the article DOES NOT collapse. The predicate nominal establishes ontological identity, not depleted quantity: 'Ce n'est pas un problème.'\n"
        "Rule 3 (The Preference Exception): Verbs of preference (aimer, adorer, détester, préférer) denote total categorical entities and "
        "ALWAYS govern definite articles (le, la, l', les). Definite articles NEVER reduce to 'de' in the negative: 'Je n'aime pas le café.'",
        "alert"
    )

    add_h2("Part A: The Partitive vs. Negation Trap (15 Contrastive Transformations)")
    add_p("Transform each affirmative statement into the negative. Choose between 'de', 'd'', or retaining the full article:")

    for aff_prompt, blank_sent, _, _ in LEVEL3_NEGATION_ITEMS:
        add_p(f"• {aff_prompt}\n  {blank_sent}", space_before=2, space_after=3)

    add_h2("Part B: Adjective Placement Dynamics (BAGS & Mobile Semantic Shifts)")
    add_p("Sub-Part 1: BAGS Placement, Pre-Vocalic Euphonic Alternations (beau/bel, nouveau/nouvel, vieux/vieil) & Plural Reduction:")
    add_p("Combine the determiner, adjective, and noun into a grammatically flawless noun phrase:")
    for prompt_phr, _, _, _ in LEVEL3_BAGS_ITEMS:
        add_p(f"• {prompt_phr}  ===>  ____________________________________________________________", space_before=1, space_after=2)

    add_p("Sub-Part 2: Mobile Adjectives with Position-Dependent Semantic Divergence (5 Minimal Pairs):", bold=True, color=INDIGO_RGB, space_before=4)
    add_p("Insert the adjective before or after the noun according to the semantic gloss provided:")
    for cue, blank_str, _, _ in LEVEL3_MOBILE_ADJECTIVES_ITEMS:
        add_p(f"• Adjective: {cue}\n  Form: {blank_str}", space_before=2, space_after=3)

    add_h2("Part C: Tri-Variable Concord (Gender, Number, & Syntactic Hierarchy — 12 Challenges)")
    add_p("Complete each sentence by calculating the precise agreement of verbs and predicate adjectives. Address mixed-gender compound subjects, collective nouns, copulas, and invariant color compounds:")

    for sent, _, _ in LEVEL3_CONCORD_ITEMS:
        add_p(f"• {sent}", space_before=2, space_after=3)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # =============================================================
    # LEVEL 4
    # =============================================================
    add_h1("LEVEL 4: BRUTAL SYNTHESIS & ERROR HUNTING")
    
    add_h2("Exercise 1: Passage Correction (250-Word Deceptive Academic Narrative)")
    add_p("The passage below contains exactly 15 deliberately engineered syntactic, morphological, and orthographic violations. Read closely, identify each error, and complete the Diagnostic Error Log below:")

    # Box for narrative text
    narr_tbl = doc.add_table(rows=1, cols=1)
    narr_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    narr_tbl.columns[0].width = Inches(7.0)
    n_cell = narr_tbl.cell(0, 0)
    style_cell(n_cell, fill_hex=LIGHT_BG, borders={'left': {'val': 'single', 'sz': 16, 'color': INDIGO_HEX}}, pad_tb=100, pad_lr=120)
    np = n_cell.paragraphs[0]
    np.paragraph_format.space_before = Pt(0)
    np.paragraph_format.space_after = Pt(0)
    nr = np.add_run(LEVEL4_PASSAGE_TEXT)
    nr.font.size = Pt(9.5)
    nr.font.italic = True
    nr.font.color.rgb = DARK_RGB

    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    add_p("DIAGNOSTIC ERROR LOG (Record all 15 violations):", bold=True, color=BURGUNDY_RGB, space_before=4)

    err_tbl = doc.add_table(rows=16, cols=4)
    err_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    err_tbl.columns[0].width = Inches(1.8)
    err_tbl.columns[1].width = Inches(1.6)
    err_tbl.columns[2].width = Inches(2.0)
    err_tbl.columns[3].width = Inches(1.6)

    err_hdrs = ["Faulty Word / Segment", "Grammatical Category", "Underlying Linguistic Violation", "Corrected Surface Form"]
    for ci, h in enumerate(err_hdrs):
        c = err_tbl.cell(0, ci)
        style_cell(c, fill_hex=BURGUNDY_HEX, pad_tb=40, pad_lr=50)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(255, 255, 255)

    for ri in range(1, 16):
        bg = LIGHT_BG if ri % 2 == 1 else "FFFFFF"
        for ci in range(4):
            c = err_tbl.cell(ri, ci)
            style_cell(c, fill_hex=bg, pad_tb=25, pad_lr=35)
            p = c.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            if ci == 0:
                p.add_run(f"Error {ri}: ________________").font.size = Pt(8)
            else:
                p.add_run("________________________").font.size = Pt(8)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    add_h2("Exercise 2: English to French Translation Gauntlet (10 Multi-Clause Stress-Tests)")
    add_p("Translate each complex sentence into standard literary French. Every sentence requires the simultaneous coordination of verb stems, contractions, article shifts, and adjective concord:")

    for t_data in LEVEL4_TRANSLATIONS:
        add_p(f"• {t_data['en']}", bold=True, space_before=4, space_after=1)
        add_p("   Traduction : ____________________________________________________________________________________________", space_before=1, space_after=1)
        add_p("   _________________________________________________________________________________________________________", space_before=0, space_after=2)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # =============================================================
    # LEVEL 5: UNCOMPROMISING TECHNICAL ANSWER KEY
    # =============================================================
    doc.add_page_break()
    add_h1("LEVEL 5: UNCOMPROMISING TECHNICAL ANSWER KEY & ANNOTATIONS")
    
    add_callout(
        "DIAGNOSTIC VERIFICATION PROTOCOL",
        "This master key contains verbatim solutions, morphological paradigms, and analytical grammatical justifications "
        "designed to eradicate persistent fossilized errors. Cross-reference every error against the linguistic margins below.",
        "alert"
    )

    add_h2("Level 1 Solutions: Elementary Drills")
    add_p("1.1 Regular -ER Verb Conjugations:\n"
          "• parler : je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent.\n"
          "• habiter : j'habite (élision obligatoire), tu habites, il habite, nous habitons, vous habitez, ils habitent.\n"
          "• regarder : je regarde, tu regardes, il regarde, nous regardons, vous regardez, ils regardent.\n"
          "• travailler : je travaille, tu travailles, il travaille, nous travaillons, vous travaillez, ils travaillent.\n"
          "• étudier : j'étudie (élision), tu étudies, il étudie, nous étudions, vous étudiez, ils étudient.\n"
          "• écouter : j'écoute (élision), tu écoutes, il écoute, nous écoutons, vous écoutez, ils écoutent.")
    
    add_p("1.2 Phonetic Discrimination Solutions:\n"
          "1. regarde vs regardent : Identique /ʁə.ɡaʁd/ (la désinence verbale -ent est strictement muette).\n"
          "2. parles vs parlez : Distinction /paʁl/ vs /paʁ.le/ (/e/ fermé).\n"
          "3. habitons vs habitent : Voyelle nasale /ɔ̃/ (/a.bi.tɔ̃/) vs consonne orale articulée /t/ (/a.bit/).\n"
          "4. écoute vs écoutent : Homophonie totale /e.kut/.\n"
          "5. travaille vs travaillons : Dissyllabique /tʁa.vaj/ vs trisyllabique /tʁa.va.jɔ̃/.\n"
          "6. on étudie vs ils étudient : Liaison obligatoire en [n] (/ɔ̃.n‿e.ty.di/) vs liaison facultative en [z] (/il.z‿e.ty.di/).")

    add_p("1.3 Article Matrix Complete Solutions (30 Items):\n"
          "1. livre : le, un, [N/A] | 2. table : la, une, [N/A] | 3. ami : l', un, [N/A] | 4. amie : l', une, [N/A] | 5. eau : l', [N/A], de l' | "
          "6. vin : le, un, du | 7. pain : le, un, du | 8. viande : la, une, de la | 9. café : le, un, du | 10. argent : l', [N/A], de l' | "
          "11. homme : l' (h muet), un, [N/A] | 12. héros : le (h aspiré, pas d'élision !), un, [N/A] | 13. homard : le (h aspiré), un, du | "
          "14. histoire : l' (h muet), une, [N/A] | 15. haricot : le (h aspiré), un, des | 16. fromage : le, un, du | 17. salade : la, une, de la | "
          "18. bière : la, une, de la | 19. huile : l' (h muet), une, de l' | 20. courage : le, [N/A], du | 21. patience : la, [N/A], de la | "
          "22. ordinateur : l', un, [N/A] | 23. voiture : la, une, [N/A] | 24. problème : le (masculin d'origine grecque), un, [N/A] | "
          "25. système : le (masculin grec), un, [N/A] | 26. photo : la (apocope de photographie), une, [N/A] | 27. glace : la, une, de la | "
          "28. sucre : le, un, du | 29. sel : le, [N/A], du | 30. fruits : les, des, des.")

    add_p("1.4 Regular Adjective Morphology Paradigms:\n"
          "intelligent -> intelligente, intelligents, intelligentes | grand -> grande, grands, grandes | "
          "petit -> petite, petits, petites | content -> contente, contents, contentes | "
          "lourd -> lourde, lourds, lourdes | vert -> verte, verts, vertes | "
          "chaud -> chaude, chauds, chaudes | froid -> froide, froids, froides | "
          "amusant -> amusante, amusants, amusantes | élégant -> élégante, élégants, élégantes | "
          "patient -> patiente, patients, patientes | prudent -> prudente, prudents, prudentes.")

    add_h2("Level 2 Solutions: Intermediate Mechanics")
    add_p("2.1 Orthographic Preservation Boot-Camp (20 Items):\n"
          "1. mangeons (maintien du 'e' muet devant 'o') | 2. commençons (cédille 'ç' devant 'o') | 3. achète (accent grave devant syllabe muette) | "
          "4. achetons (accent aigu/muet non modifié devant syllabe prononcée) | 5. achètent (accent grave devant désinence muette -ent) | "
          "6. préfère (changement é -> è) | 7. préférons (maintien du radical préfér-) | 8. préfèrent (changement é -> è) | "
          "9. j'appelle (doublement l -> ll pour son [ɛl]) | 10. appelons (un seul 'l' devant -ons) | 11. appellent (doublement l -> ll) | "
          "12. jette (doublement t -> tt pour son [ɛt]) | 13. jetons (un seul 't' devant -ons) | 14. voyageons (e intercalaire) | "
          "15. avançons (cédille) | 16. lèves (e -> è) | 17. espérez (radical intact) | 18. partageons (e intercalaire) | "
          "19. remplaçons (cédille) | 20. pèse (e -> è).")

    add_p("2.2 Contractions & Prepositional Rection:\n"
          "1. au (à + le) | 2. à la | 3. à l' | 4. aux (à + les) | 5. au (parler à + le) | 6. aux (téléphoner à + les) | "
          "7. au (penser à + le) | 8. aux (répondre à + les) | 9. du (venir de + le) | 10. de la | 11. de l' | 12. des (de + les) | "
          "13. du (parler de + le) | 14. des (avoir besoin de + les) | 15. du (avoir peur de + le) | 16. des (se souvenir de + les).")

    add_p("2.3 Disambiguation of 'des':\n"
          "1. Indéterminé / Partitif pluriel (quantité non comptable de liquides) | "
          "2. Article contracté (préposition de exigée par 'parler de' + article défini les) | "
          "3. Article indéfini pluriel (pluriel de 'un arbre') | "
          "4. Article contracté (revenir de + les îles) | "
          "5. Article indéfini pluriel (portions dénombrables : des tasses de café) | "
          "6. Article contracté (le nom 'peur' régit 'de' + les représailles).")

    add_p("2.4 Pluralization of Irregular Nouns & Adjectives:\n"
          "1. des journaux nationaux (-al -> -aux) | 2. des animaux loyaux (-al -> -aux) | 3. des chevaux sauvages (cheval -> chevaux ; sauvage -> sauvages) | "
          "4. des travaux originaux (travail -> travaux ; original -> originaux) | 5. des festivals navals (EXCEPTIONS régulières en +s) | "
          "6. des carnavals banals (EXCEPTIONS en +s) | 7. de beaux tableaux (-eau -> -eaux ; 'des' réduit en 'de' devant adjectif antéposé !) | "
          "8. de nouveaux châteaux (-eau -> -eaux ; réduction en 'de') | 9. des oiseaux rares (-eau -> -eaux) | 10. des pays gris (invariable en -s) | "
          "11. des voix douces (voix invariable en -x ; féminin pluriel douces) | 12. des gaz dangereux (invariable en -z et -x) | "
          "13. de vieux choix (invariable en -x ; réduction 'de vieux') | 14. des nez pointus (nez invariable en -z) | "
          "15. des hôpitaux régionaux (-al -> -aux).")

    add_h2("Level 3 Solutions: Advanced Application & Semantic Disambiguation")
    add_p("3.1 The Partitive vs. Negation Trap (15 Solutions):\n"
          "1. de (verbe transitif direct 'avoir' -> effondrement) | 2. de (manger -> effondrement) | 3. de (acheter -> effondrement) | "
          "4. d' (élision devant voyelle) | 5. de (commander -> effondrement) | "
          "6. UN (VERBE D'IDENTITÉ ÊTRE : pas d'effondrement !) | 7. UNE (VERBE ÊTRE : maintien de 'une') | "
          "8. DES (VERBE ÊTRE : maintien de 'des') | 9. LE (VERBE DE PRÉFÉRENCE 'aimer' : article défini obligatoire et maintenu) | "
          "10. LA (VERBE DE PRÉFÉRENCE 'préférer' : maintien de 'la') | 11. LES (VERBE 'adorer' : maintien de 'les') | "
          "12. de (chercher -> effondrement) | 13. d' (boire -> effondrement en d') | 14. DU (VERBE ÊTRE : prédicat d'identification) | "
          "15. de (posséder -> effondrement).")

    add_p("3.2 BAGS & Mobile Adjectives:\n"
          "Sub-Part 1 (Euphonia & Reduction):\n"
          "1. un bel appartement (beau -> bel devant voyelle) | 2. un nouvel étudiant (nouveau -> nouvel) | 3. un vieil homme (vieux -> vieil devant h muet) | "
          "4. un bel arbre (beau -> bel) | 5. de beaux tableaux (des -> de devant adjectif antéposé) | 6. de grands édifices (des -> de) | "
          "7. de vieux amis (des -> de) | 8. de jeunes filles (des -> de).\n\n"
          "Sub-Part 2 (Mobile Adjectives Semantic Contrasts):\n"
          "1. (a) un homme grand (taille physique) | (b) un grand homme (grandeur historique/morale)\n"
          "2. (a) des mains propres (propres/nettoyées) | (b) mes propres mains (possession personnelle)\n"
          "3. (a) un homme pauvre (indigent/démuni) | (b) un pauvre homme (pitoyable/malheureux)\n"
          "4. (a) mon ancien professeur (précédent/ex-) | (b) un meuble ancien (d'époque/antique)\n"
          "5. (a) une victoire certaine (indiscutable/prouvée) | (b) une certaine timidité (un degré modéré).")

    add_p("3.3 Tri-Variable Concord (12 Solutions):\n"
          "1. attentifs (le masculin pluriel l'emporte sur le groupe mixte Marc et Claire) | "
          "2. épuisées (accord féminin pluriel) | "
          "3. est rassemblée (accord grammatical avec le collectif singulier 'foule' ; l'accord de sens pluriel 'sont rassemblés' est toléré) | "
          "4. sont prêts (l'expression 'la plupart de' impose le verbe et l'adjectif au pluriel) | "
          "5. crédibles (verbe attributif paraître -> accord fém. plur.) | "
          "6. élégantes (verbe sembler -> accord sujet fém. plur. robes) | "
          "7. marron / orange (INVARIABLES : adjectifs de couleur dérivés de noms concrets ne s'accordent jamais !) | "
          "8. bleu clair (INVARIABLE : adjectif de couleur composé modifié par 'clair') | "
          "9. fiers (masculin pluriel l'emporte sur père et fille) | "
          "10. inacceptable (verbe attributif demeurer -> accord fém. sing.) | "
          "11. vert foncé (INVARIABLE : couleur composée) | "
          "12. favorable (accord avec 'la majorité').")

    add_h2("Level 4 Solutions: Brutal Synthesis & Error Hunting")
    add_p("Exercise 1 Solutions: Diagnostic Error Hunting Log (15 Violations Analyzed):", bold=True, color=BURGUNDY_RGB)
    
    for err_txt, cat_txt, rule_txt, fix_txt in LEVEL4_PASSAGE_ERRORS:
        add_p(f"• Erreur repérée : « {err_txt} »\n   - Catégorie : {cat_txt}\n   - Justification : {rule_txt}\n   - Correction obligatoire : « {fix_txt} »", space_before=1, space_after=3)

    add_p("Exercise 2 Solutions: Translation Gauntlet (10 Technical Master Translations):", bold=True, color=INDIGO_RGB, space_before=6)
    for t_data in LEVEL4_TRANSLATIONS:
        add_p(f"• Phrase {t_data['en']}\n   Version française : « {t_data['fr']} »\n   Analyse syntaxique : {t_data['notes']}", space_before=2, space_after=3)

    # Technical Linguistics Callout
    add_callout(
        "PHILOLOGICAL AND SYNTACTIC APPENDIX: THE 'DES -> DE' PRE-NOMINAL REDUCTION",
        "Why standard French requires 'de beaux arbres' instead of *'des beaux arbres':\n"
        "Historically, the indefinite plural 'des' is an agglutination of the preposition 'de' and the definite article 'les'. "
        "When an adjective precedes the noun, the noun phrase is not directly determined by the substantive; "
        "rather, the preposition 'de' acts as a pure partitive marker indicating an indefinite quantity of items possessing the quality. "
        "The Académie française and authoritative reference grammars (Grevisse, Le Bon Usage §589) maintain that the article 'les' is dropped, "
        "leaving only the particle 'de' (or 'd'' before vowel: 'd'anciens amis'). While spoken colloquial French often retains 'des', "
        "formal register, university examination standards, and literary syntax strictly enforce 'de + [adjectif antéposé] + [nom pluriel]'.",
        "info"
    )

    # Save DOCX
    doc.save(DOCX_PATH)
    print(f"Successfully generated DOCX at: {DOCX_PATH}")


# =========================================================================
# PDF BUILDER IMPLEMENTATION
# =========================================================================

def build_pdf():
    class NumberedCanvas(canvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._saved_page_states = []

        def showPage(self):
            self._saved_page_states.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            num_pages = len(self._saved_page_states)
            for state in self._saved_page_states:
                self.__dict__.update(state)
                self.draw_page_decorations(num_pages)
                super().showPage()
            super().save()

        def draw_page_decorations(self, page_count):
            if self._pageNumber > 1:
                self.saveState()
                self.setFont(BASE_FONT, 8)
                self.setFillColor(colors.HexColor("#475569"))
                # Running header
                self.drawString(45, letter[1] - 32, "Mastering Core French Syntax  |  Applied Linguistics Division  •  FREN-201-SYN")
                self.setStrokeColor(colors.HexColor("#CBD5E1"))
                self.setLineWidth(0.5)
                self.line(45, letter[1] - 38, letter[0] - 45, letter[1] - 38)
                
                # Footer
                page_str = f"Page {self._pageNumber} of {page_count}"
                self.drawRightString(letter[0] - 45, 28, page_str)
                self.drawString(45, 28, "Zero-Tolerance Diagnostic Assessment  •  Precision French Morphosyntax Series")
                self.line(45, 36, letter[0] - 45, 36)
                self.restoreState()

    pdf_doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=45,
        bottomMargin=45
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CoverTitle', parent=styles['Normal'],
        fontName=BOLD_FONT, fontSize=16, leading=20,
        textColor=colors.white, alignment=1, spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'CoverSubtitle', parent=styles['Normal'],
        fontName=BOLD_FONT, fontSize=10, leading=13,
        textColor=colors.HexColor('#FEF08A'), alignment=1, spaceAfter=4
    )
    meta_style = ParagraphStyle(
        'CoverMeta', parent=styles['Normal'],
        fontName=ITALIC_FONT, fontSize=8, leading=10,
        textColor=colors.HexColor('#E2E8F0'), alignment=1
    )
    h1_style = ParagraphStyle(
        'DocH1', parent=styles['Normal'],
        fontName=BOLD_FONT, fontSize=12, leading=15,
        textColor=colors.HexColor('#1E1B4B'), spaceBefore=10, spaceAfter=3
    )
    h2_style = ParagraphStyle(
        'DocH2', parent=styles['Normal'],
        fontName=BOLD_FONT, fontSize=10, leading=12,
        textColor=colors.HexColor('#881337'), spaceBefore=7, spaceAfter=2
    )
    body_style = ParagraphStyle(
        'DocBody', parent=styles['Normal'],
        fontName=BASE_FONT, fontSize=8, leading=10.5,
        textColor=colors.HexColor('#0F172A'), spaceBefore=1, spaceAfter=2
    )
    body_bold = ParagraphStyle(
        'DocBodyBold', parent=body_style,
        fontName=BOLD_FONT
    )
    muted_style = ParagraphStyle(
        'DocMuted', parent=body_style,
        fontName=BASE_FONT, textColor=colors.HexColor('#475569')
    )
    tbl_cell_style = ParagraphStyle(
        'TblCell', parent=styles['Normal'],
        fontName=BASE_FONT, fontSize=7.5, leading=9.5,
        textColor=colors.HexColor('#0F172A')
    )
    tbl_hdr_style = ParagraphStyle(
        'TblHdr', parent=styles['Normal'],
        fontName=BOLD_FONT, fontSize=8, leading=10,
        textColor=colors.white, alignment=1
    )

    def make_callout(title, text, callout_type="info"):
        if callout_type == "alert":
            b_col = colors.HexColor('#9A3412')
            bg_col = colors.HexColor('#FFFBEB')
        elif callout_type == "danger":
            b_col = colors.HexColor('#881337')
            bg_col = colors.HexColor('#FFF1F2')
        elif callout_type == "teal":
            b_col = colors.HexColor('#0F766E')
            bg_col = colors.HexColor('#F0FDFA')
        else:
            b_col = colors.HexColor('#1E1B4B')
            bg_col = colors.HexColor('#F1F5F9')

        c_t = Paragraph(f"<b>{title}</b>", ParagraphStyle('CT', parent=body_bold, textColor=b_col, fontSize=8.5, leading=11))
        c_b = Paragraph(text.replace('\n', '<br/>'), ParagraphStyle('CB', parent=body_style, fontSize=7.8, leading=10))
        
        t = Table([[c_t], [c_b]], colWidths=[522])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), bg_col),
            ('LINEBEFORE', (0,0), (0,-1), 2.5, b_col),
            ('TOPPADDING', (0,0), (-1,-1), 4),
            ('BOTTOMPADDING', (0,0), (-1,-1), 4),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ]))
        return t

    story = []

    # Cover Table
    cp1 = Paragraph("MASTERING CORE FRENCH SYNTAX", title_style)
    cp2 = Paragraph("Regular -ER Verbs, The Complete Article System, Contractions, and Nominal/Adjective Agreement", subtitle_style)
    cp3 = Paragraph("University Division of Applied Linguistics • Rigorous Tiered Practice Workbook (Levels 1 to 5)", meta_style)
    cover_t = Table([[cp1], [cp2], [cp3]], colWidths=[522])
    cover_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#1E1B4B')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(cover_t)
    story.append(Spacer(1, 6))

    story.append(make_callout(
        "CURRICULUM ARCHITECTURE & PEDAGOGICAL PROTOCOL",
        "This practice workbook is structured as an uncompromising progression from isolated morphosyntactic mechanics "
        "to multi-variable communicative synthesis. Each level isolates specific phonological and syntactic friction points: "
        "silent inflectional endings, velar-stop preservation, contraction rules, negative reduction vs identity verbs, "
        "and euphonic pre-vocalic alternations. Complete all sections actively before consulting Level 5.",
        "danger"
    ))
    story.append(Spacer(1, 6))

    # LEVEL 1
    story.append(Paragraph("LEVEL 1: ELEMENTARY DRILLS (Isolated Foundations)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=4))
    story.append(Paragraph("<b>Part A: Regular -ER Verb Paradigm Isolation & Silent-Ending Discrimination</b>", h2_style))
    story.append(Paragraph("Supply the correct present-indicative inflection for each subject pronoun:", body_style))

    for v_info in LEVEL1_VERBS_PARADIGMS:
        story.append(Paragraph(f"<b>Target: {v_info['verb'].upper()}</b> — <font color='#475569'>{v_info['notes']}</font>", body_style))
        tbl_data = [
            [Paragraph("<b>Pronoun</b>", tbl_hdr_style), Paragraph("<b>Conjugation</b>", tbl_hdr_style),
             Paragraph("<b>Pronoun</b>", tbl_hdr_style), Paragraph("<b>Conjugation</b>", tbl_hdr_style)]
        ]
        for p1, _, p2, _ in v_info["rows"]:
            tbl_data.append([
                Paragraph(f"<b>{p1}</b>", tbl_cell_style), Paragraph("______________________", tbl_cell_style),
                Paragraph(f"<b>{p2}</b>", tbl_cell_style), Paragraph("______________________", tbl_cell_style)
            ])
        vt = Table(tbl_data, colWidths=[90, 171, 90, 171])
        vt.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E1B4B')),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
            ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(vt)
        story.append(Spacer(1, 3))

    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Acoustic Discrimination: Silent Ending & Pronunciation Stress-Test</b>", h2_style))
    for pair, prompt, opt1, opt2, _ in LEVEL1_PHONETIC_ITEMS:
        story.append(Paragraph(f"• <b>{pair}</b> — {prompt} &nbsp;&nbsp; {opt1} &nbsp;&nbsp;&nbsp;&nbsp; {opt2}", body_style))

    # Level 1 Part B
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part B: The Complete Article Classification Matrix (30 Target Nouns)</b>", h2_style))
    story.append(Paragraph("Assign the correct Definite, Indefinite, and Partitive articles; identify the morphophonological class:", body_style))

    art_tbl_data = [
        [Paragraph("<b>Noun & Gloss</b>", tbl_hdr_style),
         Paragraph("<b>Class</b>", tbl_hdr_style),
         Paragraph("<b>Definite [le/la/l']</b>", tbl_hdr_style),
         Paragraph("<b>Indefinite [un/une/des]</b>", tbl_hdr_style),
         Paragraph("<b>Partitive [du/de la/de l']</b>", tbl_hdr_style)]
    ]
    for n_w, gloss, cls_w, _, _, _ in LEVEL1_ARTICLES_TABLE:
        art_tbl_data.append([
            Paragraph(f"<b>{n_w}</b> ({gloss})", tbl_cell_style),
            Paragraph(cls_w, tbl_cell_style),
            Paragraph("[  ] ____________", tbl_cell_style),
            Paragraph("[  ] ____________", tbl_cell_style),
            Paragraph("[  ] ____________", tbl_cell_style),
        ])
    atbl = Table(art_tbl_data, colWidths=[112, 110, 100, 100, 100])
    atbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E1B4B')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 1.8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.8),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(atbl)

    # Level 1 Part C
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part C: Foundational Adjective Morphology (Regular Concord: +e, +s)</b>", h2_style))
    story.append(Paragraph("Supply all four inflectional forms for each base descriptive adjective:", body_style))

    adj_tbl_data = [
        [Paragraph("<b>Masc. Sing.</b>", tbl_hdr_style),
         Paragraph("<b>Fem. Sing. (+e)</b>", tbl_hdr_style),
         Paragraph("<b>Masc. Plur. (+s)</b>", tbl_hdr_style),
         Paragraph("<b>Fem. Plur. (+es)</b>", tbl_hdr_style),
         Paragraph("<b>Gloss</b>", tbl_hdr_style)]
    ]
    for ms, _, _, _, gl in LEVEL1_ADJECTIVES:
        adj_tbl_data.append([
            Paragraph(f"<b>{ms}</b>", tbl_cell_style),
            Paragraph("________________", tbl_cell_style),
            Paragraph("________________", tbl_cell_style),
            Paragraph("________________", tbl_cell_style),
            Paragraph(gl, tbl_cell_style)
        ])
    adj_t = Table(adj_tbl_data, colWidths=[104, 105, 105, 105, 103])
    adj_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E1B4B')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(adj_t)

    # LEVEL 2
    story.append(PageBreak())
    story.append(Paragraph("LEVEL 2: INTERMEDIATE SYNTACTIC MECHANICS (Spelling Shifts & Contractions)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=4))
    story.append(make_callout(
        "ORTHOGRAPHIC PRESERVATION MECHANISM: VELAR STOPS & ACCENT ALTERNATIONS",
        "• -ger verbs: Stem ends in soft [ʒ]. An unaccented 'e' is obligatory before 'a' and 'o' (nous mangeons) to prevent [ɡ].<br/>"
        "• -cer verbs: Stem ends in soft [s]. A cédille 'ç' is obligatory before 'a' and 'o' (nous commençons) to prevent [k].<br/>"
        "• Stem-changing verbs: Adjust stem vowel or double consonant (j'achète, j'appelle, je jette) to produce open [ɛ] before mute syllables.",
        "teal"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part A: Orthographic & Phonetic Preservation Boot-Camp (20 Items)</b>", h2_style))
    for _, sent, _, _ in LEVEL2_ORTHOGRAPHIC_VERBS:
        story.append(Paragraph(f"• {sent}", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part B: Contraction Triggers & Prepositional Rection (16 Items)</b>", h2_style))
    for trig, sent, _, _ in LEVEL2_CONTRACTIONS_ITEMS:
        story.append(Paragraph(f"• <b>[{trig}]</b> &nbsp;&nbsp; {sent}", body_style))

    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Disambiguation Drill: Partitive vs. Contracted vs. Indefinite 'des' (6 Items)</b>", h2_style))
    for sent, o1, o2, o3, _ in LEVEL2_DISAMBIGUATION_ITEMS:
        story.append(Paragraph(f"• <i>{sent}</i><br/>&nbsp;&nbsp;&nbsp;&nbsp;{o1} &nbsp;&nbsp;&nbsp;&nbsp; {o2} &nbsp;&nbsp;&nbsp;&nbsp; {o3}<br/>&nbsp;&nbsp;&nbsp;&nbsp;Syntactic Trigger: ____________________________________________________________________", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part C: Morphological Pluralization of Irregular Nouns & Adjectives (15 Items)</b>", h2_style))
    for sing_phr, _, _, _ in LEVEL2_PLURALS_ITEMS:
        story.append(Paragraph(f"• <b>{sing_phr}</b> &nbsp;&nbsp;=====&gt;&nbsp;&nbsp; ________________________________________________________", body_style))

    # LEVEL 3
    story.append(PageBreak())
    story.append(Paragraph("LEVEL 3: ADVANCED APPLICATION & SEMANTIC DISAMBIGUATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=4))
    story.append(make_callout(
        "THE SYNTACTIC COLLAPSE PARADOX: NEGATION, IDENTITY, AND PREFERENCE",
        "• Transitive Negation: Indefinite/partitives collapse to 'de / d'' (Je n'ai pas de pain).<br/>"
        "• Identity Verb Exception: Across linking 'être', articles DO NOT collapse (Ce n'est pas un problème).<br/>"
        "• Preference Exception: 'Aimer / préférer' take definite articles which NEVER become 'de' (Je n'aime pas le vin).",
        "alert"
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part A: The Partitive vs. Negation Trap (15 Transformations)</b>", h2_style))
    for aff_prompt, blank_sent, _, _ in LEVEL3_NEGATION_ITEMS:
        story.append(Paragraph(f"• <b>{aff_prompt.replace(chr(10), ' ')}</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;{blank_sent}", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part B: Adjective Placement Dynamics (BAGS & Mobile Semantic Shifts)</b>", h2_style))
    story.append(Paragraph("<b>Sub-Part 1: Euphonic Alternations & Pre-Nominal Plural Reduction:</b>", body_style))
    for prompt_phr, _, _, _ in LEVEL3_BAGS_ITEMS:
        story.append(Paragraph(f"• <b>{prompt_phr}</b> &nbsp;&nbsp;=====&gt;&nbsp;&nbsp; ________________________________________________________", body_style))

    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Sub-Part 2: Mobile Adjectives with Meaning Shifts (5 Pairs):</b>", body_style))
    for cue, blank_str, _, _ in LEVEL3_MOBILE_ADJECTIVES_ITEMS:
        story.append(Paragraph(f"• <b>Adjective:</b> {cue}<br/>&nbsp;&nbsp;&nbsp;&nbsp;Forms: {blank_str}", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Part C: Tri-Variable Concord (Gender, Number, & Syntactic Hierarchy — 12 Items)</b>", h2_style))
    for sent, _, _ in LEVEL3_CONCORD_ITEMS:
        story.append(Paragraph(f"• {sent}", body_style))

    # LEVEL 4
    story.append(PageBreak())
    story.append(Paragraph("LEVEL 4: BRUTAL SYNTHESIS & ERROR HUNTING", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=4))
    story.append(Paragraph("<b>Exercise 1: Passage Correction (250-Word Deceptive Academic Narrative)</b>", h2_style))
    story.append(Paragraph("Read the text below, detect all 15 intentional violations, and log them in the matrix:", body_style))

    narr_p = Paragraph(f"<i>« {LEVEL4_PASSAGE_TEXT} »</i>", ParagraphStyle('NP', parent=body_style, fontSize=8, leading=10.5, textColor=colors.HexColor('#0F172A')))
    narr_t = Table([[narr_p]], colWidths=[522])
    narr_t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8FAFC')),
        ('LINEBEFORE', (0,0), (0,-1), 2.5, colors.HexColor('#1E1B4B')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(narr_t)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>DIAGNOSTIC ERROR LOG (15 Violations):</b>", body_style))
    err_tbl_data = [
        [Paragraph("<b>Faulty Segment</b>", tbl_hdr_style),
         Paragraph("<b>Category</b>", tbl_hdr_style),
         Paragraph("<b>Violation Rationale</b>", tbl_hdr_style),
         Paragraph("<b>Correction</b>", tbl_hdr_style)]
    ]
    for ri in range(1, 16):
        err_tbl_data.append([
            Paragraph(f"Error {ri}: ____________", tbl_cell_style),
            Paragraph("____________________", tbl_cell_style),
            Paragraph("____________________", tbl_cell_style),
            Paragraph("____________________", tbl_cell_style)
        ])
    et = Table(err_tbl_data, colWidths=[120, 110, 162, 130])
    et.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#881337')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(et)

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Exercise 2: English to French Translation Gauntlet (10 Multi-Clause Stress-Tests)</b>", h2_style))
    for t_data in LEVEL4_TRANSLATIONS:
        story.append(Paragraph(f"• <b>{t_data['en']}</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;Traduction : ______________________________________________________________________________________<br/>&nbsp;&nbsp;&nbsp;&nbsp;_________________________________________________________________________________________________", body_style))

    # LEVEL 5
    story.append(PageBreak())
    story.append(Paragraph("LEVEL 5: UNCOMPROMISING TECHNICAL ANSWER KEY & ANNOTATIONS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#1E1B4B'), spaceAfter=4))
    story.append(make_callout(
        "DIAGNOSTIC VERIFICATION PROTOCOL",
        "Verify your answers against the solutions below. Study the grammatical annotations to eliminate fossilized errors.",
        "alert"
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>Level 1 Solutions: Elementary Drills</b>", h2_style))
    story.append(Paragraph("<b>1.1 Conjugations:</b> parler (parle, parles, parle, parlons, parlez, parlent) | habiter (j'habite, habites, habite, habitons, habitez, habitent) | regarder (regarde, regardes, regarde, regardons, regardez, regardent) | travailler (travaille, travailles, travaille, travaillons, travaillez, travaillent) | étudier (j'étudie, étudies, étudie, étudions, étudiez, étudient) | écouter (j'écoute, écoutes, écoute, écoutons, écoutez, écoutent).", body_style))
    story.append(Paragraph("<b>1.2 Phonetics:</b> 1. Identical /ʁə.ɡaʁd/ (mute -ent) | 2. /paʁl/ vs /paʁ.le/ | 3. Nasal /a.bi.tɔ̃/ vs oral /a.bit/ | 4. Homophonous /e.kut/ | 5. 2 syll (/tʁa.vaj/) vs 3 syll (/tʁa.va.jɔ̃/) | 6. [n] liaison (/ɔ̃.n‿e.ty.di/).", body_style))
    story.append(Paragraph("<b>1.3 Article Matrix (30 Items):</b> 1. le, un, [N/A] | 2. la, une, [N/A] | 3. l', un, [N/A] | 4. l', une, [N/A] | 5. l', [N/A], de l' | 6. le, un, du | 7. le, un, du | 8. la, une, de la | 9. le, un, du | 10. l', [N/A], de l' | 11. l' (h muet), un, [N/A] | 12. le (h aspiré), un, [N/A] | 13. le (h aspiré), un, du | 14. l' (h muet), une, [N/A] | 15. le (h aspiré), un, des | 16. le, un, du | 17. la, une, de la | 18. la, une, de la | 19. l' (h muet), une, de l' | 20. le, [N/A], du | 21. la, [N/A], de la | 22. l', un, [N/A] | 23. la, une, [N/A] | 24. le (masc grec), un, [N/A] | 25. le (masc grec), un, [N/A] | 26. la (photo), une, [N/A] | 27. la, une, de la | 28. le, un, du | 29. le, [N/A], du | 30. les, des, des.", body_style))
    story.append(Paragraph("<b>1.4 Adjectives:</b> intelligente(s), intelligents | grande(s), grands | petite(s), petits | contente(s), contents | lourde(s), lourds | verte(s), verts | chaude(s), chauds | froide(s), froids | amusante(s), amusants | élégante(s), élégants | patiente(s), patients | prudente(s), prudents.", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Level 2 Solutions: Intermediate Mechanics</b>", h2_style))
    story.append(Paragraph("<b>2.1 Verbs (20 Items):</b> 1. mangeons | 2. commençons | 3. achète | 4. achetons | 5. achètent | 6. préfère | 7. préférons | 8. préfèrent | 9. j'appelle | 10. appelons | 11. appellent | 12. jette | 13. jetons | 14. voyageons | 15. avançons | 16. lèves | 17. espérez | 18. partageons | 19. remplaçons | 20. pèse.", body_style))
    story.append(Paragraph("<b>2.2 Contractions (16 Items):</b> 1. au | 2. à la | 3. à l' | 4. aux | 5. au | 6. aux | 7. au | 8. aux | 9. du | 10. de la | 11. de l' | 12. des | 13. du | 14. des | 15. du | 16. des.", body_style))
    story.append(Paragraph("<b>2.3 Disambiguation of 'des':</b> 1. Partitif / Indéfini pluriel | 2. Contracté (parler de + les) | 3. Indéfini pluriel (des arbres) | 4. Contracté (revenir de + les îles) | 5. Indéfini pluriel (des cafés) | 6. Contracté (peur de + les).", body_style))
    story.append(Paragraph("<b>2.4 Irregular Plurals (15 Items):</b> 1. des journaux nationaux | 2. des animaux loyaux | 3. des chevaux sauvages | 4. des travaux originaux | 5. des festivals navals (exceptions +s) | 6. des carnavals banals (+s) | 7. de beaux tableaux (des -> de !) | 8. de nouveaux châteaux (des -> de !) | 9. des oiseaux rares | 10. des pays gris (invariable) | 11. des voix douces (invariable -x) | 12. des gaz dangereux (invariable) | 13. de vieux choix (invariable ; de vieux) | 14. des nez pointus (invariable) | 15. des hôpitaux régionaux.", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Level 3 Solutions: Advanced Application & Semantic Disambiguation</b>", h2_style))
    story.append(Paragraph("<b>3.1 Negation Transformations (15 Items):</b> 1. de stylo | 2. de fromage | 3. de confiture | 4. d'argent | 5. de boissons | 6. UN roman (être : pas d'effondrement !) | 7. UNE erreur (être) | 8. DES professeurs (être) | 9. LE café (verbe de préférence aimer) | 10. LA viande (préférer) | 11. LES épinards (adorer) | 12. de chambre | 13. d'eau | 14. DU vin (être : prédicat d'identification) | 15. de dictionnaires.", body_style))
    story.append(Paragraph("<b>3.2 BAGS & Mobile Adjectives:</b> Sub-Part 1: 1. un bel appartement | 2. un nouvel étudiant | 3. un vieil homme | 4. un bel arbre | 5. de beaux tableaux (des -> de) | 6. de grands édifices | 7. de vieux amis | 8. de jeunes filles. Sub-Part 2: 1. (a) un homme grand (physique) / (b) un grand homme (illustre) | 2. (a) des mains propres (nettoyées) / (b) mes propres mains (possession) | 3. (a) un homme pauvre (démuni) / (b) un pauvre homme (pitoyable) | 4. (a) mon ancien professeur (ex-) / (b) un meuble ancien (antique) | 5. (a) une victoire certaine (prouvée) / (b) une certaine timidité (modérée).", body_style))
    story.append(Paragraph("<b>3.3 Tri-Variable Concord (12 Items):</b> 1. attentifs (masc. pluriel domine) | 2. épuisées | 3. est rassemblée / sont rassemblés | 4. sont prêts | 5. crédibles | 6. élégantes | 7. marron / orange (invariables) | 8. bleu clair (invariable) | 9. fiers | 10. inacceptable | 11. vert foncé (invariable) | 12. favorable.", body_style))

    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Level 4 Solutions: Brutal Synthesis & Error Hunting</b>", h2_style))
    story.append(Paragraph("<b>Exercise 1 Solutions: 15 Errors Analyzed:</b>", body_style))
    for err_txt, cat_txt, rule_txt, fix_txt in LEVEL4_PASSAGE_ERRORS:
        story.append(Paragraph(f"• <b>« {err_txt} »</b> [{cat_txt}] — <i>{rule_txt}</i> ===&gt; <b>« {fix_txt} »</b>", body_style))

    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>Exercise 2 Solutions: 10 Master Translations:</b>", body_style))
    for t_data in LEVEL4_TRANSLATIONS:
        story.append(Paragraph(f"• <b>{t_data['en']}</b><br/>&nbsp;&nbsp;&nbsp;&nbsp;<b>Traduction :</b> « {t_data['fr']} »<br/>&nbsp;&nbsp;&nbsp;&nbsp;<font color='#475569'><b>Notes :</b> {t_data['notes']}</font>", body_style))

    story.append(Spacer(1, 4))
    story.append(make_callout(
        "PHILOLOGICAL AND SYNTACTIC APPENDIX: THE 'DES -> DE' PRE-NOMINAL REDUCTION",
        "The Académie française and reference grammars (Grevisse §589) maintain that when an adjective precedes a plural noun, "
        "the indefinite plural 'des' reduces to 'de / d'' (de beaux arbres, d'anciens édifices). The particle 'de' marks pure indeterminate quantification.",
        "info"
    ))

    # Build PDF
    pdf_doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF at: {PDF_PATH}")

if __name__ == "__main__":
    build_docx()
    build_pdf()
