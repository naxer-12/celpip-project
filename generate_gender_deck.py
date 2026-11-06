import urllib.parse
import genanki
import os

MODEL_ID = 1882390142
DECK_ID = 2024110501

FRONT_TEMPLATE = """<div class="card-container">
  <div class="instruction">Complete with the correct article (Un / Une) or identify the gender:</div>
  <div class="prompt-word">____ {{Noun}}</div>
  
  {{#English Translation}}
  <div class="clue-translation">Meaning: {{English Translation}}</div>
  {{/English Translation}}
</div>"""

BACK_TEMPLATE = """<div class="card-container">
  <!-- Revealed Answer with Dynamic Color Block -->
  <div class="answer-block {{Gender}}">
    <span class="article">{{Article}}</span> <span class="target-noun">{{Noun}}</span>
  </div>

  <hr id="answer-splitter">

  <!-- Audio Pronunciation if available -->
  {{#Audio}}
  <div class="audio-player">{{Audio}}</div>
  {{/Audio}}

  <!-- Rule & Pattern Recognition Section -->
  <div class="metadata-container">
    <div class="meta-row">
      <span class="meta-label">English:</span>
      <span class="meta-value">{{English Translation}}</span>
    </div>
    
    <div class="meta-row rule-highlight">
      <span class="meta-label">Pattern/Rule:</span>
      <span class="meta-value"><strong>{{Suffix/Category}}</strong> &rarr; {{Rule Explanation}}</span>
    </div>

    {{#Example Sentence}}
    <div class="meta-row sentence-block">
      <span class="meta-label">In Context:</span>
      <span class="meta-value-italic">{{Example Sentence}}</span>
    </div>
    {{/Example Sentence}}
  </div>
</div>"""

CSS_STYLING = """/* Global Card Styles */
.card {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 18px;
  text-align: center;
  color: #2D3748;
  background-color: #F7FAFC;
  margin: 0;
  padding: 10px;
}

/* Night Mode Compatibility */
.nightMode .card, .night_mode .card {
  color: #E2E8F0;
  background-color: #1A202C;
}

/* Main Container */
.card-container {
  max-width: 500px;
  margin: 20px auto;
  padding: 25px;
  background: #FFFFFF;
  border-radius: 16px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.nightMode .card-container, .night_mode .card-container {
  background: #2D3748;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
}

/* Front Elements */
.instruction {
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: #718096;
  margin-bottom: 20px;
}

.prompt-word {
  font-size: 36px;
  font-weight: 700;
  color: #4A5568;
  margin-bottom: 15px;
}

.nightMode .prompt-word, .night_mode .prompt-word {
  color: #EDF2F7;
}

.clue-translation {
  font-size: 15px;
  color: #A0AEC0;
  font-style: italic;
}

/* Back Elements: Dynamic Color Blocks */
.answer-block {
  font-size: 38px;
  font-weight: 800;
  padding: 15px;
  border-radius: 12px;
  margin-bottom: 15px;
  display: inline-block;
  width: 90%;
  box-sizing: border-box;
}

/* Masculine Theme Styling */
.answer-block.Masculine, .answer-block.masculine, .answer-block.M, .answer-block.m {
  background-color: #EBF8FF;
  color: #2B6CB0;
  border: 2px solid #BEE3F8;
}
.nightMode .answer-block.Masculine, .nightMode .answer-block.masculine, .nightMode .answer-block.M, .nightMode .answer-block.m,
.night_mode .answer-block.Masculine, .night_mode .answer-block.masculine, .night_mode .answer-block.M, .night_mode .answer-block.m {
  background-color: #2A4365;
  color: #90CDF4;
  border-color: #2B6CB0;
}

/* Feminine Theme Styling */
.answer-block.Feminine, .answer-block.feminine, .answer-block.F, .answer-block.f {
  background-color: #FFF5F5;
  color: #C53030;
  border: 2px solid #FED7D7;
}
.nightMode .answer-block.Feminine, .nightMode .answer-block.feminine, .nightMode .answer-block.F, .nightMode .answer-block.f,
.night_mode .answer-block.Feminine, .night_mode .answer-block.feminine, .night_mode .answer-block.F, .night_mode .answer-block.f {
  background-color: #653B3B;
  color: #FEB2B2;
  border-color: #9B2C2C;
}

.article {
  text-decoration: underline;
}

/* Divider Line */
#answer-splitter {
  border: 0;
  height: 1px;
  background: #E2E8F0;
  margin: 20px 0;
}
.nightMode #answer-splitter, .night_mode #answer-splitter {
  background: #4A5568;
}

/* Audio Player */
.audio-player {
  margin: 12px 0 16px 0;
}
.audio-player a {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  background-color: #EDF2F7;
  color: #2D3748;
  text-decoration: none;
  font-size: 13px;
  font-weight: 600;
  border-radius: 20px;
  transition: all 0.2s ease;
}
.audio-player a:hover {
  background-color: #E2E8F0;
}
.nightMode .audio-player a, .night_mode .audio-player a {
  background-color: #3A4454;
  color: #EDF2F7;
}
.nightMode .audio-player a:hover, .night_mode .audio-player a:hover {
  background-color: #4A5568;
}

/* Metadata Layout */
.metadata-container {
  text-align: left;
  margin-top: 15px;
}

.meta-row {
  display: flex;
  margin-bottom: 12px;
  font-size: 15px;
  line-height: 1.4;
}

.meta-label {
  font-weight: 600;
  min-width: 100px;
  color: #718096;
}
.nightMode .meta-label, .night_mode .meta-label {
  color: #A0AEC0;
}

.meta-value {
  color: #2D3748;
}
.nightMode .meta-value, .night_mode .meta-value {
  color: #E2E8F0;
}

.rule-highlight {
  background-color: #F7FAFC;
  padding: 8px 12px;
  border-radius: 6px;
  border-left: 4px solid #CBD5E0;
}
.nightMode .rule-highlight, .night_mode .rule-highlight {
  background-color: #3A4454;
  border-left-color: #4A5568;
}

.sentence-block {
  border-top: 1px dashed #E2E8F0;
  padding-top: 10px;
  margin-top: 10px;
}
.nightMode .sentence-block, .night_mode .sentence-block {
  border-top-color: #4A5568;
}

.meta-value-italic {
  font-style: italic;
  color: #4A5568;
}
.nightMode .meta-value-italic, .night_mode .meta-value-italic {
  color: #CBD5E0;
}
"""

gender_model = genanki.Model(
    MODEL_ID,
    "French Noun Gender Mastery",
    fields=[
        {"name": "Noun"},
        {"name": "Article"},
        {"name": "Gender"},
        {"name": "English Translation"},
        {"name": "Suffix/Category"},
        {"name": "Rule Explanation"},
        {"name": "Example Sentence"},
        {"name": "Audio"},
    ],
    templates=[
        {
            "name": "French Noun Gender Recognition",
            "qfmt": FRONT_TEMPLATE,
            "afmt": BACK_TEMPLATE,
        }
    ],
    css=CSS_STYLING
)

deck = genanki.Deck(
    DECK_ID,
    "French::Noun Gender Intuition Mastery (A1 CEFR)"
)

# Curated dataset of 60 high-yield cards
cards_data = [
    # --- MASCULINE SUFFIX PATTERNS ---
    {
        "noun": "appartement",
        "article": "un / l'",
        "gender": "Masculine",
        "english": "apartment / flat",
        "suffix": "-ment",
        "rule": "Nouns ending in -ment are >99% masculine.",
        "sentence": "J'habite dans un bel appartement au centre-ville.",
        "tag": "Pattern_Masc_ment"
    },
    {
        "noun": "médicament",
        "article": "un / le",
        "gender": "Masculine",
        "english": "medicine / medication",
        "suffix": "-ment",
        "rule": "Nouns ending in -ment are >99% masculine.",
        "sentence": "Prenez ce médicament avec un grand verre d'eau.",
        "tag": "Pattern_Masc_ment"
    },
    {
        "noun": "fromage",
        "article": "un / le",
        "gender": "Masculine",
        "english": "cheese",
        "suffix": "-age",
        "rule": "Nouns ending in -age are overwhelmingly masculine (over 95%).",
        "sentence": "Ce fromage de chèvre a une saveur délicate.",
        "tag": "Pattern_Masc_age"
    },
    {
        "noun": "voyage",
        "article": "un / le",
        "gender": "Masculine",
        "english": "trip / journey",
        "suffix": "-age",
        "rule": "Nouns ending in -age are overwhelmingly masculine.",
        "sentence": "Bon voyage et profitez bien de votre séjour!",
        "tag": "Pattern_Masc_age"
    },
    {
        "noun": "mariage",
        "article": "un / le",
        "gender": "Masculine",
        "english": "wedding / marriage",
        "suffix": "-age",
        "rule": "Nouns ending in -age are masculine.",
        "sentence": "Le mariage de ma cousine aura lieu en plein air.",
        "tag": "Pattern_Masc_age"
    },
    {
        "noun": "château",
        "article": "un / le",
        "gender": "Masculine",
        "english": "castle / palace",
        "suffix": "-eau",
        "rule": "Nouns ending in -eau are masculine (exceptions: la peau, l'eau).",
        "sentence": "Nous avons visité un magnifique château de la Loire.",
        "tag": "Pattern_Masc_eau"
    },
    {
        "noun": "bateau",
        "article": "un / le",
        "gender": "Masculine",
        "english": "boat",
        "suffix": "-eau",
        "rule": "Nouns ending in -eau are consistently masculine.",
        "sentence": "Un petit bateau blanc navigue sur le lac.",
        "tag": "Pattern_Masc_eau"
    },
    {
        "noun": "couteau",
        "article": "un / le",
        "gender": "Masculine",
        "english": "knife",
        "suffix": "-eau",
        "rule": "Nouns ending in -eau are masculine.",
        "sentence": "Passe-moi un couteau bien aiguisé pour couper le pain.",
        "tag": "Pattern_Masc_eau"
    },
    {
        "noun": "chapeau",
        "article": "un / le",
        "gender": "Masculine",
        "english": "hat",
        "suffix": "-eau",
        "rule": "Nouns ending in -eau are masculine.",
        "sentence": "Il porte un chapeau noir élégant.",
        "tag": "Pattern_Masc_eau"
    },
    {
        "noun": "bijou",
        "article": "un / le",
        "gender": "Masculine",
        "english": "jewel / piece of jewelry",
        "suffix": "-ou",
        "rule": "Nouns ending in -ou are masculine.",
        "sentence": "Elle a reçu un précieux bijou en or pour son anniversaire.",
        "tag": "Pattern_Masc_ou"
    },
    {
        "noun": "tourisme",
        "article": "le / un",
        "gender": "Masculine",
        "english": "tourism",
        "suffix": "-isme",
        "rule": "Nouns ending in -isme (systems, doctrines, concepts) are always masculine.",
        "sentence": "Le tourisme international est en plein essor.",
        "tag": "Pattern_Masc_isme"
    },
    {
        "noun": "téléphone",
        "article": "un / le",
        "gender": "Masculine",
        "english": "telephone",
        "suffix": "-phone",
        "rule": "Instruments and acoustic devices ending in -phone are masculine.",
        "sentence": "Mon téléphone sonne constamment au bureau.",
        "tag": "Pattern_Masc_phone"
    },
    {
        "noun": "télescope",
        "article": "un / le",
        "gender": "Masculine",
        "english": "telescope",
        "suffix": "-scope",
        "rule": "Optical and viewing devices ending in -scope are masculine.",
        "sentence": "Nous observons les étoiles avec un puissant télescope.",
        "tag": "Pattern_Masc_scope"
    },
    {
        "noun": "calendrier",
        "article": "un / le",
        "gender": "Masculine",
        "english": "calendar",
        "suffix": "-ier",
        "rule": "Nouns ending in -ier are overwhelmingly masculine.",
        "sentence": "J'ai noté tous nos rendez-vous sur le calendrier mural.",
        "tag": "Pattern_Masc_ier"
    },
    {
        "noun": "cahier",
        "article": "un / le",
        "gender": "Masculine",
        "english": "notebook / exercise book",
        "suffix": "-ier",
        "rule": "Nouns ending in -ier are masculine.",
        "sentence": "Écrivez chaque nouveau mot dans un cahier propre.",
        "tag": "Pattern_Masc_ier"
    },
    {
        "noun": "journal",
        "article": "un / le",
        "gender": "Masculine",
        "english": "newspaper / journal",
        "suffix": "-al",
        "rule": "Nouns ending in -al are masculine.",
        "sentence": "Mon père lit le journal tous les matins au petit-déjeuner.",
        "tag": "Pattern_Masc_al"
    },
    {
        "noun": "cheval",
        "article": "un / le",
        "gender": "Masculine",
        "english": "horse",
        "suffix": "-al",
        "rule": "Nouns ending in -al are masculine.",
        "sentence": "Un magnifique cheval blanc court dans le pré.",
        "tag": "Pattern_Masc_al"
    },
    {
        "noun": "travail",
        "article": "un / le",
        "gender": "Masculine",
        "english": "work / job",
        "suffix": "-ail",
        "rule": "Nouns ending in -ail are masculine.",
        "sentence": "Il a trouvé un travail intéressant dans le marketing.",
        "tag": "Pattern_Masc_ail"
    },
    {
        "noun": "fauteuil",
        "article": "un / le",
        "gender": "Masculine",
        "english": "armchair",
        "suffix": "-euil",
        "rule": "Nouns ending in -euil / -ueil are masculine.",
        "sentence": "Le grand-père s'est endormi dans son fauteuil douillet.",
        "tag": "Pattern_Masc_euil"
    },
    {
        "noun": "jardin",
        "article": "un / le",
        "gender": "Masculine",
        "english": "garden",
        "suffix": "-in",
        "rule": "Nouns ending in -in are masculine (exception: la fin, la main).",
        "sentence": "Les enfants jouent dans un grand jardin ombragé.",
        "tag": "Pattern_Masc_in"
    },
    {
        "noun": "dessin",
        "article": "un / le",
        "gender": "Masculine",
        "english": "drawing",
        "suffix": "-in",
        "rule": "Nouns ending in -in are masculine.",
        "sentence": "C'est un dessin coloré réalisé par un élève de CP.",
        "tag": "Pattern_Masc_in"
    },
    {
        "noun": "miroir",
        "article": "un / le",
        "gender": "Masculine",
        "english": "mirror",
        "suffix": "-oir",
        "rule": "Nouns ending in -oir are masculine.",
        "sentence": "Elle ajuste son collier devant un grand miroir doré.",
        "tag": "Pattern_Masc_oir"
    },
    {
        "noun": "salon",
        "article": "un / le",
        "gender": "Masculine",
        "english": "living room / lounge",
        "suffix": "-on",
        "rule": "Nouns ending in -on (not -tion/-sion) are typically masculine.",
        "sentence": "Nous prenons le thé dans un salon lumineux.",
        "tag": "Pattern_Masc_on"
    },
    {
        "noun": "billet",
        "article": "un / le",
        "gender": "Masculine",
        "english": "ticket / banknote",
        "suffix": "-et",
        "rule": "Diminutive suffix -et is masculine.",
        "sentence": "N'oubliez pas d'acheter un billet de train à l'avance.",
        "tag": "Pattern_Masc_et"
    },
    {
        "noun": "problème",
        "article": "un / le",
        "gender": "Masculine",
        "english": "problem",
        "suffix": "-ème (Greek root)",
        "rule": "Scientific/academic nouns from Greek ending in -ème/-me are masculine.",
        "sentence": "C'est un problème complexe mais nous avons une solution.",
        "tag": "Pattern_Masc_Greek"
    },
    {
        "noun": "système",
        "article": "un / le",
        "gender": "Masculine",
        "english": "system",
        "suffix": "-ème (Greek root)",
        "rule": "Greek-origin nouns ending in -ème are masculine.",
        "sentence": "Le nouveau système d'exploitation fonctionne à merveille.",
        "tag": "Pattern_Masc_Greek"
    },
    {
        "noun": "poème",
        "article": "un / le",
        "gender": "Masculine",
        "english": "poem",
        "suffix": "-ème (Greek root)",
        "rule": "Greek-origin nouns ending in -ème are masculine.",
        "sentence": "L'auteur a récité un poème émouvant sur la paix.",
        "tag": "Pattern_Masc_Greek"
    },

    # --- FEMININE SUFFIX PATTERNS ---
    {
        "noun": "situation",
        "article": "une / la",
        "gender": "Feminine",
        "english": "situation",
        "suffix": "-tion",
        "rule": "Nouns ending in -tion are >99% feminine (derived from Latin -tio).",
        "sentence": "Nous faisons face à une situation tout à fait inédite.",
        "tag": "Pattern_Fem_tion"
    },
    {
        "noun": "station",
        "article": "une / la",
        "gender": "Feminine",
        "english": "station / resort",
        "suffix": "-tion",
        "rule": "Nouns ending in -tion are feminine.",
        "sentence": "Descendez à la prochaine station de métro.",
        "tag": "Pattern_Fem_tion"
    },
    {
        "noun": "décision",
        "article": "une / la",
        "gender": "Feminine",
        "english": "decision",
        "suffix": "-sion",
        "rule": "Nouns ending in -sion are feminine.",
        "sentence": "C'est une sage décision que nous soutenons tous.",
        "tag": "Pattern_Fem_sion"
    },
    {
        "noun": "connexion",
        "article": "une / la",
        "gender": "Feminine",
        "english": "connection",
        "suffix": "-xion",
        "rule": "Nouns ending in -xion are feminine.",
        "sentence": "Cette connexion wifi est particulièrement stable et rapide.",
        "tag": "Pattern_Fem_xion"
    },
    {
        "noun": "beauté",
        "article": "la / une",
        "gender": "Feminine",
        "english": "beauty",
        "suffix": "-té",
        "rule": "Abstract nouns ending in -té (English -ty) are feminine.",
        "sentence": "La beauté de cette cathédrale gothique impressionne.",
        "tag": "Pattern_Fem_te"
    },
    {
        "noun": "vérité",
        "article": "la / une",
        "gender": "Feminine",
        "english": "truth",
        "suffix": "-té",
        "rule": "Abstract nouns ending in -té are feminine.",
        "sentence": "La vérité finit toujours par triompher.",
        "tag": "Pattern_Fem_te"
    },
    {
        "noun": "santé",
        "article": "la / une",
        "gender": "Feminine",
        "english": "health",
        "suffix": "-té",
        "rule": "Abstract nouns ending in -té are feminine.",
        "sentence": "Manger équilibré est indispensable pour une bonne santé.",
        "tag": "Pattern_Fem_te"
    },
    {
        "noun": "amitié",
        "article": "l' / une",
        "gender": "Feminine",
        "english": "friendship",
        "suffix": "-tié",
        "rule": "Abstract nouns ending in -tié are feminine.",
        "sentence": "Ils partagent une sincère amitié depuis l'enfance.",
        "tag": "Pattern_Fem_tie"
    },
    {
        "noun": "bicyclette",
        "article": "une / la",
        "gender": "Feminine",
        "english": "bicycle",
        "suffix": "-ette",
        "rule": "Diminutive suffix -ette is consistently feminine.",
        "sentence": "Elle se promène sur une jolie bicyclette jaune.",
        "tag": "Pattern_Fem_ette"
    },
    {
        "noun": "fourchette",
        "article": "une / la",
        "gender": "Feminine",
        "english": "fork",
        "suffix": "-ette",
        "rule": "Nouns ending in -ette are feminine.",
        "sentence": "Posez une fourchette et un couteau de chaque côté de l'assiette.",
        "tag": "Pattern_Fem_ette"
    },
    {
        "noun": "serviette",
        "article": "une / la",
        "gender": "Feminine",
        "english": "towel / napkin",
        "suffix": "-ette",
        "rule": "Nouns ending in -ette are feminine.",
        "sentence": "Prenez une serviette propre pour la salle de bain.",
        "tag": "Pattern_Fem_ette"
    },
    {
        "noun": "politesse",
        "article": "la",
        "gender": "Feminine",
        "english": "politeness",
        "suffix": "-esse",
        "rule": "State and moral nouns ending in -esse are feminine.",
        "sentence": "La politesse facilite grandement la vie en société.",
        "tag": "Pattern_Fem_esse"
    },
    {
        "noun": "jeunesse",
        "article": "la / une",
        "gender": "Feminine",
        "english": "youth",
        "suffix": "-esse",
        "rule": "Nouns ending in -esse are feminine.",
        "sentence": "Il a passé toute sa jeunesse dans un petit village normand.",
        "tag": "Pattern_Fem_esse"
    },
    {
        "noun": "boulangerie",
        "article": "une / la",
        "gender": "Feminine",
        "english": "bakery",
        "suffix": "-rie",
        "rule": "Place of craft/trade ending in -rie are feminine.",
        "sentence": "Je passe à la boulangerie chercher une baguette fraîche.",
        "tag": "Pattern_Fem_rie"
    },
    {
        "noun": "pharmacie",
        "article": "une / la",
        "gender": "Feminine",
        "english": "pharmacy / chemist",
        "suffix": "-ie",
        "rule": "Nouns ending in -ie are feminine.",
        "sentence": "Il y a une pharmacie ouverte juste en face de la gare.",
        "tag": "Pattern_Fem_ie"
    },
    {
        "noun": "voiture",
        "article": "une / la",
        "gender": "Feminine",
        "english": "car",
        "suffix": "-ure",
        "rule": "Nouns ending in -ure are overwhelmingly feminine.",
        "sentence": "Nous montons dans une voiture confortable et spacieuse.",
        "tag": "Pattern_Fem_ure"
    },
    {
        "noun": "peinture",
        "article": "une / la",
        "gender": "Feminine",
        "english": "painting / paint",
        "suffix": "-ure",
        "rule": "Nouns ending in -ure are feminine.",
        "sentence": "C'est une peinture impressionniste d'une grande valeur.",
        "tag": "Pattern_Fem_ure"
    },
    {
        "noun": "différence",
        "article": "une / la",
        "gender": "Feminine",
        "english": "difference",
        "suffix": "-ence",
        "rule": "Nouns ending in -ence / -ance are feminine (exception: le silence).",
        "sentence": "Pouvez-vous m'expliquer la différence entre ces deux concepts?",
        "tag": "Pattern_Fem_ence"
    },
    {
        "noun": "chance",
        "article": "une / la",
        "gender": "Feminine",
        "english": "luck / chance",
        "suffix": "-ance",
        "rule": "Nouns ending in -ance are feminine.",
        "sentence": "Quelle chance d'avoir une place au premier rang!",
        "tag": "Pattern_Fem_ance"
    },
    {
        "noun": "journée",
        "article": "une / la",
        "gender": "Feminine",
        "english": "day (span/duration)",
        "suffix": "-ée",
        "rule": "Nouns of duration ending in -ée are feminine (exceptions: musée, lycée).",
        "sentence": "Nous avons passé une agréable journée ensoleillée au bord de la mer.",
        "tag": "Pattern_Fem_ee"
    },
    {
        "noun": "idée",
        "article": "une / l'",
        "gender": "Feminine",
        "english": "idea",
        "suffix": "-ée",
        "rule": "Nouns ending in -ée are feminine.",
        "sentence": "C'est une brillante idée que tout le monde approuve.",
        "tag": "Pattern_Fem_ee"
    },
    {
        "noun": "maison",
        "article": "une / la",
        "gender": "Feminine",
        "english": "house",
        "suffix": "-aison",
        "rule": "Nouns ending in -aison are feminine.",
        "sentence": "Leurs grands-parents possèdent une jolie maison avec jardin.",
        "tag": "Pattern_Fem_aison"
    },
    {
        "noun": "saison",
        "article": "une / la",
        "gender": "Feminine",
        "english": "season",
        "suffix": "-aison",
        "rule": "Nouns ending in -aison are feminine.",
        "sentence": "Le printemps est ma saison préférée de l'année.",
        "tag": "Pattern_Fem_aison"
    },
    {
        "noun": "salade",
        "article": "une / la",
        "gender": "Feminine",
        "english": "salad / lettuce",
        "suffix": "-ade",
        "rule": "Nouns ending in -ade are feminine (exception: le stade).",
        "sentence": "Le serveur nous apporte une salade fraîche composée.",
        "tag": "Pattern_Fem_ade"
    },
    {
        "noun": "surprise",
        "article": "une / la",
        "gender": "Feminine",
        "english": "surprise",
        "suffix": "-ise",
        "rule": "Nouns ending in -ise are feminine.",
        "sentence": "Elle a eu une agréable surprise en recevant ce cadeau.",
        "tag": "Pattern_Fem_ise"
    },
    {
        "noun": "valise",
        "article": "une / la",
        "gender": "Feminine",
        "english": "suitcase",
        "suffix": "-ise",
        "rule": "Nouns ending in -ise are feminine.",
        "sentence": "Ne préparez pas une valise trop lourde pour l'avion.",
        "tag": "Pattern_Fem_ise"
    },

    # --- HIGH-YIELD CRITICAL EXCEPTIONS (TRAPS FOR A1) ---
    {
        "noun": "musée",
        "article": "un / le",
        "gender": "Masculine",
        "english": "museum",
        "suffix": "Exception: -ée",
        "rule": "Masculine exception to the feminine -ée ending (from Greek mouseion).",
        "sentence": "Le musée du Louvre attire des millions de visiteurs.",
        "tag": "Exception_Masc"
    },
    {
        "noun": "lycée",
        "article": "un / le",
        "gender": "Masculine",
        "english": "high school",
        "suffix": "Exception: -ée",
        "rule": "Masculine exception to the feminine -ée ending (from Greek lykeion).",
        "sentence": "Mon frère aîné est élève dans un grand lycée parisien.",
        "tag": "Exception_Masc"
    },
    {
        "noun": "silence",
        "article": "le / un",
        "gender": "Masculine",
        "english": "silence",
        "suffix": "Exception: -ence",
        "rule": "Major masculine exception to the feminine -ence pattern (Latin silentium).",
        "sentence": "Un profond silence règne dans la salle d'examen.",
        "tag": "Exception_Masc"
    },
    {
        "noun": "plage",
        "article": "une / la",
        "gender": "Feminine",
        "english": "beach",
        "suffix": "Exception: -age",
        "rule": "Key feminine exception to the masculine -age ending rule.",
        "sentence": "Nous posons nos serviettes sur une belle plage de sable fin.",
        "tag": "Exception_Fem"
    },
    {
        "noun": "image",
        "article": "une / l'",
        "gender": "Feminine",
        "english": "picture / image",
        "suffix": "Exception: -age",
        "rule": "Feminine exception to the masculine -age ending rule.",
        "sentence": "Ce livre pour enfants contient une magnifique image par page.",
        "tag": "Exception_Fem"
    },
    {
        "noun": "page",
        "article": "une / la",
        "gender": "Feminine",
        "english": "page",
        "suffix": "Exception: -age",
        "rule": "Feminine exception to the masculine -age ending rule.",
        "sentence": "Ouvrez votre cahier d'exercices à la page trente.",
        "tag": "Exception_Fem"
    },
    {
        "noun": "main",
        "article": "une / la",
        "gender": "Feminine",
        "english": "hand",
        "suffix": "Exception: -ain",
        "rule": "Feminine exception to the masculine -ain ending (from Latin manus).",
        "sentence": "L'enfant donne la main à sa mère pour traverser la rue.",
        "tag": "Exception_Fem"
    },
    {
        "noun": "eau",
        "article": "de l' / l'",
        "gender": "Feminine",
        "english": "water",
        "suffix": "Exception: -eau",
        "rule": "Crucial feminine exception to -eau ending (from Latin aqua).",
        "sentence": "Avez-vous de l'eau bien fraîche pour les invités?",
        "tag": "Exception_Fem"
    },
    {
        "noun": "peau",
        "article": "la / une",
        "gender": "Feminine",
        "english": "skin",
        "suffix": "Exception: -eau",
        "rule": "Feminine exception to the -eau ending rule (from Latin pellis).",
        "sentence": "Cette crème hydratante protège la peau contre le froid.",
        "tag": "Exception_Fem"
    },
    {
        "noun": "nuit",
        "article": "la / une",
        "gender": "Feminine",
        "english": "night",
        "suffix": "Exception: -t",
        "rule": "Feminine exception to consonant ending -t (from Latin nox/noctis).",
        "sentence": "La nuit tombe de plus en plus tôt en décembre.",
        "tag": "Exception_Fem"
    },

    # --- CATEGORIES, COMPOUNDS & HOMOGRAPHS ---
    {
        "noun": "gratte-ciel",
        "article": "un / le",
        "gender": "Masculine",
        "english": "skyscraper",
        "suffix": "Compound (Verb + Noun)",
        "rule": "Compound nouns composed of Verb + Noun are consistently masculine.",
        "sentence": "Ils admirent un immense gratte-ciel illuminé dans la nuit.",
        "tag": "Compound_Masc"
    },
    {
        "noun": "lave-vaisselle",
        "article": "un / le",
        "gender": "Masculine",
        "english": "dishwasher",
        "suffix": "Compound (Verb + Noun)",
        "rule": "Compound appliance nouns (Verb + Noun) are masculine.",
        "sentence": "Mettez les verres sales dans le lave-vaisselle.",
        "tag": "Compound_Masc"
    },
    {
        "noun": "lundi",
        "article": "le",
        "gender": "Masculine",
        "english": "Monday",
        "suffix": "Calendar: Days",
        "rule": "All days of the week in French are grammatically masculine.",
        "sentence": "Le lundi est le début de la semaine scolaire en France.",
        "tag": "Category_Days"
    },
    {
        "noun": "printemps",
        "article": "le / un",
        "gender": "Masculine",
        "english": "spring (season)",
        "suffix": "Calendar: Seasons",
        "rule": "All seasons in French are masculine.",
        "sentence": "Au printemps, les arbres reverdissent et les oiseaux chantent.",
        "tag": "Category_Seasons"
    },
    {
        "noun": "français",
        "article": "le",
        "gender": "Masculine",
        "english": "French (language)",
        "suffix": "Languages",
        "rule": "All names of languages in French are masculine and written in lowercase.",
        "sentence": "J'apprends le français avec enthousiasme chaque jour.",
        "tag": "Category_Languages"
    },
    {
        "noun": "personne",
        "article": "une / la",
        "gender": "Feminine",
        "english": "person (individual)",
        "suffix": "Fixed Gender Noun",
        "rule": "Une personne is always feminine, even when referring to a male individual.",
        "sentence": "C'est une personne très polie et serviable.",
        "tag": "Category_People"
    },
    {
        "noun": "livre",
        "article": "un / le",
        "gender": "Masculine",
        "english": "book",
        "suffix": "Homograph (Masc)",
        "rule": "Le livre = book (Masculine). Note: la livre (Feminine) = pound/currency.",
        "sentence": "Je termine un livre passionnant sur la cuisine française.",
        "tag": "Homograph"
    },
    {
        "noun": "tour",
        "article": "une / la",
        "gender": "Feminine",
        "english": "tower",
        "suffix": "Homograph (Fem)",
        "rule": "La tour = architectural tower (Feminine). Contrast with le tour = turn/lap (Masc).",
        "sentence": "La tour Eiffel s'élève au cœur de Paris.",
        "tag": "Homograph"
    }
]

tsv_lines = ["Noun\tArticle\tGender\tEnglish Translation\tSuffix/Category\tRule Explanation\tExample Sentence\tAudio"]

for item in cards_data:
    n = item["noun"]
    art = item["article"]
    g = item["gender"]
    en = item["english"]
    suf = item["suffix"]
    rule = item["rule"]
    sent = item["sentence"]
    tag = item["tag"]
    
    # Audio tag with web TTS audio fallback
    audio_query = f"{art.split('/')[0].strip()} {n}".strip()
    encoded_audio = urllib.parse.quote(audio_query)
    audio_field = f'<a href="https://translate.google.com/?sl=fr&tl=en&text={encoded_audio}&op=translate" target="_blank">🔊 Listen: [{audio_query}]</a>'
    
    note = genanki.Note(
        model=gender_model,
        fields=[n, art, g, en, suf, rule, sent, audio_field],
        tags=["French_Gender", "A1_CEFR", tag]
    )
    deck.add_note(note)
    
    # Also save TSV row
    tsv_lines.append(f"{n}\t{art}\t{g}\t{en}\t{suf}\t{rule}\t{sent}\t{audio_field}")

output_apkg = "French_Noun_Gender_Mastery.apkg"
genanki.Package(deck).write_to_file(output_apkg)
print(f"Successfully generated {output_apkg} with {len(cards_data)} cards.")

output_tsv = "French_Noun_Gender_Mastery_Cards.txt"
with open(output_tsv, "w", encoding="utf-8") as f:
    f.write("\n".join(tsv_lines))
print(f"Successfully generated {output_tsv} for TSV import.")
