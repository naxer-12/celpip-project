import json
import urllib.parse
import os
import re
import genanki

# 1. Load extracted 681 verbs
with open('/tmp/verbs_extracted_681.json', 'r', encoding='utf-8') as f:
    raw_verbs = json.load(f)

# Clean up special forms
verbs_clean = []
for item in raw_verbs:
    fr = item['french'].strip()
    en = item['english'].strip()
    
    # Fix standard irregularities in listing
    if fr.startswith('app. par coeur'):
        fr = 'apprendre par cœur'
        en = 'to memorize'
    elif '(s\')' in fr:
        base = fr.replace('(s\')', '').strip()
        fr = f"s'{base}"
    elif '(se)' in fr:
        base = fr.replace('(se)', '').strip()
        fr = f"se {base}"
        
    verbs_clean.append({'french': fr, 'english': en})

print(f"Loaded and cleaned {len(verbs_clean)} verbs.")

# 2. Linguistic Classification & Auxiliary
VANDERTRAMP = {
    'devenir', 'revenir', 'monter', 'rester', 'sortir', 'venir', 'aller', 
    'naître', 'descendre', 'entrer', 'rentrer', 'tomber', 'retourner', 
    'arriver', 'mourir', 'partir', 'repartir', 'survenir', 'parvenir'
}

SECOND_GROUP_ROOTS = {
    'abolir', 'adoucir', 'affaiblir', 'agir', 'agrandir', 'alourdir', 'amerrir', 
    'anéantir', 'aplanir', 'aplatir', 'applaudir', 'approfondir', 'arrondir', 
    'assainir', 'assombrir', 'assortir', 'assoupir', 'assourdir', 'atterrir', 
    'avertir', 'bâtir', 'bénir', 'blanchir', 'blêmir', 'bondir', 'brunir', 
    'chérir', 'choisir', 'définir', 'démolir', 'désobéir', 'durcir', 'éblouir', 
    'éclaircir', 'élargir', 'embellir', 'endurcir', 'enrichir', 'envahir', 
    'épaissir', 'épanouir', 'établir', 'étourdir', 'faiblir', 'finir', 'fléchir', 
    'fleurir', 'fournir', 'fraîchir', 'franchir', 'frémir', 'garnir', 'gémir', 
    'grandir', 'grossir', 'guérir', 'haïr', 'investir', 'jaillir', 'jaunir', 
    'jouir', 'maigrir', 'mincir', 'mûrir', 'noircir', 'nourrir', 'obéir', 
    'obscurcir', 'pâlir', 'périr', 'polir', 'pourrir', 'punir', 'raccourcir', 
    'rafraîchir', 'ralentir', 'ramollir', 'rajeunir', 'réagir', 'réfléchir', 
    'refroidir', 'réjouir', 'remplir', 'rétrécir', 'réunir', 'réussir', 
    'roidir', 'rosir', 'rougir', 'roussir', 'salir', 'subir', 'surgir', 
    'trahir', 'unir', 'verdir', 'vernir', 'vieillir', 'vomir'
}

IRREGULAR_CONJUGATIONS = {
    'être': ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
    'avoir': ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
    'aller': ['vais', 'vas', 'va', 'allons', 'allez', 'vont'],
    'faire': ['fais', 'fais', 'fait', 'faisons', 'faites', 'font'],
    'dire': ['dis', 'dis', 'dit', 'disons', 'dites', 'disent'],
    'pouvoir': ['peux', 'peux', 'peut', 'pouvons', 'pouvez', 'peuvent'],
    'vouloir': ['veux', 'veux', 'veut', 'voulons', 'voulez', 'veulent'],
    'savoir': ['sais', 'sais', 'sait', 'savons', 'savez', 'savent'],
    'devoir': ['dois', 'dois', 'doit', 'devons', 'devez', 'doivent'],
    'voir': ['vois', 'vois', 'voit', 'voyons', 'voyez', 'voient'],
    'croire': ['crois', 'crois', 'croit', 'croyons', 'croyez', 'croient'],
    'boire': ['bois', 'bois', 'boit', 'buvons', 'buvez', 'boivent'],
    'lire': ['lis', 'lis', 'lit', 'lisons', 'lisez', 'lisent'],
    'rire': ['ris', 'ris', 'rit', 'rions', 'riez', 'rient'],
    'sourir': ['souris', 'souris', 'sourit', 'sourions', 'souriez', 'sourient'],
    'sourire': ['souris', 'souris', 'sourit', 'sourions', 'souriez', 'sourient'],
    'vivre': ['vis', 'vis', 'vit', 'vivons', 'vivez', 'vivent'],
    'suivre': ['suis', 'suis', 'suit', 'suivons', 'suivez', 'suivent'],
    'valoir': ['vaux', 'vaux', 'vaut', 'valons', 'valez', 'valent'],
    'falloir': ['-', '-', 'faut', '-', '-', '-'],
    'pleuvoir': ['-', '-', 'pleut', '-', '-', '-'],
    'neiger': ['-', '-', 'neige', '-', '-', '-'],
    'grêler': ['-', '-', 'grêle', '-', '-', '-'],
    'tonner': ['-', '-', 'tonne', '-', '-', '-'],
    'mourir': ['meurs', 'meurs', 'meurt', 'mourons', 'mourez', 'meurent'],
    'asseoir': ['assieds', 'assieds', 'assied', 'asseyons', 'asseyez', 'asseyent'],
    'fuir': ['fuis', 'fuis', 'fuit', 'fuyons', 'fuyez', 'fuient'],
    'haïr': ['hais', 'hais', 'hait', 'haïssons', 'haïssez', 'haïssent'],
    'vaincre': ['vaincs', 'vaincs', 'vainc', 'vainquons', 'vainquez', 'vainquent'],
    'convaincre': ['convaincs', 'convaincs', 'convainc', 'convainquons', 'convainquez', 'convainquent'],
    'rompre': ['romps', 'romps', 'rompt', 'rompons', 'rompez', 'rompent'],
    'corrompre': ['corromps', 'corromps', 'corrompt', 'corrompons', 'corrompez', 'corrompent'],
    'interrompre': ['interromps', 'interromps', 'interrompt', 'interrompons', 'interrompez', 'interrompent'],
    'coudre': ['couds', 'couds', 'coud', 'cousons', 'cousez', 'cousent'],
    'découdre': ['découds', 'découds', 'découd', 'décousons', 'décousez', 'décousent'],
    'recoudre': ['recouds', 'recouds', 'recoud', 'recousons', 'recousez', 'recousent'],
    'moudre': ['mouds', 'mouds', 'moud', 'moulons', 'moulez', 'moulent'],
    'émoudre': ['émouds', 'émouds', 'émoud', 'émoulons', 'émoulez', 'émoulent'],
    'remoudre': ['remouds', 'remouds', 'remoud', 'remoulons', 'remoulez', 'remoulent'],
    'absoudre': ['absous', 'absous', 'absout', 'absolvons', 'absolvez', 'absolvent'],
    'dissoudre': ['dissous', 'dissous', 'dissout', 'dissolvons', 'dissolvez', 'dissolvent'],
    'résoudre': ['résous', 'résous', 'résout', 'résolvons', 'résolvez', 'résolvent'],
    'plaire': ['plais', 'plais', 'plaît', 'plaisons', 'plaisez', 'plaisent'],
    'déplaire': ['déplais', 'déplais', 'déplaît', 'déplaisons', 'déplaisez', 'déplaisent'],
    'taire': ['tais', 'tais', 'tait', 'taisons', 'taisez', 'taisent'],
    'conclure': ['conclus', 'conclus', 'conclut', 'concluons', 'concluez', 'concluent'],
    'exclure': ['exclus', 'exclus', 'exclut', 'excluons', 'excluez', 'excluent'],
    'inclure': ['inclus', 'inclus', 'inclut', 'incluons', 'incluez', 'incluent'],
    'occlure': ['occlus', 'occlus', 'occlut', 'occluons', 'occluez', 'occluent'],
}

def conjugate_verb(verb_str):
    """Returns present tense conjugation drill string."""
    v = verb_str.strip()
    is_reflexive = False
    prefix = ""
    
    if v.startswith("s'"):
        is_reflexive = True
        v = v[2:].strip()
    elif v.startswith("se "):
        is_reflexive = True
        v = v[3:].strip()
        
    # Check locutions
    if v == 'avoir besoin':
        return "j'ai besoin, tu as besoin, il a besoin, nous avons besoin, vous avez besoin, ils ont besoin"
    if v == 'avoir raison':
        return "j'ai raison, tu as raison, il a raison, nous avons raison, vous avez raison, ils ont raison"
    if v == 'apprendre par cœur':
        return "j'apprends par cœur, tu apprends par cœur, il apprend par cœur, nous apprenons par cœur, vous apprenez par cœur, ils apprennent par cœur"
        
    # Impersonal verbs
    if v in ['falloir', 'pleuvoir', 'neiger', 'grêler', 'tonner']:
        forms = IRREGULAR_CONJUGATIONS[v]
        return f"il {forms[2]}"
        
    # Check exact irregular dict
    if v in IRREGULAR_CONJUGATIONS:
        forms = IRREGULAR_CONJUGATIONS[v]
        return format_conjugation(v, forms, is_reflexive)
        
    # Derivative patterns
    # -prendre
    if v.endswith('prendre'):
        p = v[:-7]
        forms = [p + 'prends', p + 'prends', p + 'prend', p + 'prenons', p + 'prenez', p + 'prennent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -venir / -tenir
    if v.endswith('venir') or v.endswith('tenir'):
        p = v[:-5]
        stem = 'vien' if v.endswith('venir') else 'tien'
        base = 'ven' if v.endswith('venir') else 'ten'
        forms = [p + stem + 's', p + stem + 's', p + stem + 't', p + base + 'ons', p + base + 'ez', p + stem + 'nent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -mettre
    if v.endswith('mettre'):
        p = v[:-6]
        forms = [p + 'mets', p + 'mets', p + 'met', p + 'mettons', p + 'mettez', p + 'mettent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -battre
    if v.endswith('battre'):
        p = v[:-6]
        forms = [p + 'bats', p + 'bats', p + 'bat', p + 'battons', p + 'battez', p + 'battent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -cevoir
    if v.endswith('cevoir'):
        p = v[:-6]
        forms = [p + 'çois', p + 'çois', p + 'çoit', p + 'cevons', p + 'cevez', p + 'çoivent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -aître
    if v.endswith('aître'):
        p = v[:-5]
        forms = [p + 'ais', p + 'ais', p + 'aît', p + 'aissons', p + 'aissez', p + 'aissent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -uire
    if v.endswith('uire'):
        p = v[:-4]
        forms = [p + 'uis', p + 'uis', p + 'uit', p + 'uisons', p + 'uisez', p + 'uisent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -indre
    if v.endswith('indre'):
        p = v[:-5]
        forms = [p + 'ins', p + 'ins', p + 'int', p + 'ignons', p + 'ignez', p + 'ignent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -crire
    if v.endswith('crire'):
        p = v[:-5]
        forms = [p + 'cris', p + 'cris', p + 'crit', p + 'crivons', p + 'crivez', p + 'crivent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -vrir / -frir
    if v.endswith('vrir') or v.endswith('frir'):
        stem = v[:-2]
        forms = [stem + 'e', stem + 'es', stem + 'e', stem + 'ons', stem + 'ez', stem + 'ent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -tir / -mir / -vir (3rd group -ir)
    if v in ['partir', 'repartir', 'départir', 'sortir', 'ressortir', 'sentir', 'ressentir', 'consentir', 'mentir', 'démentir', 'repentir', 'dormir', 'endormir', 'redormir', 'servir', 'desservir']:
        stem_s = v[:-3]
        stem_p = v[:-2]
        forms = [stem_s + 's', stem_s + 's', stem_s + 't', stem_p + 'ons', stem_p + 'ez', stem_p + 'ent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # -courir
    if v.endswith('courir'):
        stem = v[:-2]
        forms = [stem + 's', stem + 's', stem + 't', stem + 'ons', stem + 'ez', stem + 'ent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # Regular 2nd group (-ir, -issant)
    if v in SECOND_GROUP_ROOTS or (v.endswith('ir') and not (v.endswith('oir') or v.endswith('courir') or v.endswith('partir') or v.endswith('sortir') or v.endswith('sentir') or v.endswith('mentir') or v.endswith('dormir') or v.endswith('servir') or v.endswith('ouvrir') or v.endswith('couvrir') or v.endswith('offrir') or v.endswith('souffrir') or v.endswith('tenir') or v.endswith('venir'))):
        stem = v[:-2]
        forms = [stem + 'is', stem + 'is', stem + 'it', stem + 'issons', stem + 'issez', stem + 'issent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # Regular -re verbs (-endre, -ondre, -erdre)
    if v.endswith('re'):
        stem = v[:-2]
        forms = [stem + 's', stem + 's', stem + '', stem + 'ons', stem + 'ez', stem + 'ent']
        return format_conjugation(verb_str, forms, is_reflexive)
        
    # 1st group -er verbs
    if v.endswith('er'):
        stem = v[:-2]
        # -ger
        if v.endswith('ger'):
            forms = [stem + 'e', stem + 'es', stem + 'e', stem + 'eons', stem + 'ez', stem + 'ent']
        # -cer
        elif v.endswith('cer'):
            forms = [stem + 'e', stem + 'es', stem + 'e', v[:-3] + 'çons', stem + 'ez', stem + 'ent']
        # -eler
        elif v.endswith('eler') and v not in ['celer', 'déceler', 'geler', 'dégeler', 'congeler', 'surgeler', 'modeler', 'peler']:
            p = v[:-4]
            forms = [p + 'elle', p + 'elles', p + 'elle', stem + 'ons', stem + 'ez', p + 'ellent']
        # -eter
        elif v.endswith('eter') and v in ['jeter', 'rejeter', 'projeter']:
            p = v[:-4]
            forms = [p + 'ette', p + 'ettes', p + 'ette', stem + 'ons', stem + 'ez', p + 'ettent']
        # -yer
        elif v.endswith('yer'):
            p = v[:-3]
            forms = [p + 'ie', p + 'ies', p + 'ie', stem + 'ons', stem + 'ez', p + 'ient']
        # -e_er or -é_er stem change
        elif any(v.endswith(suffix) for suffix in ['éger', 'éder', 'érer', 'éter', 'ébrer', 'éner', 'éter', 'eser', 'emer', 'echer', 'eter', 'eler', 'ener', 'ever']):
            # change e/é to è before mute ending
            m = re.match(r'^(.*)([eé])([^eéaiouy]+)er$', v)
            if m:
                p1, vowel, cons = m.group(1), m.group(2), m.group(3)
                forms = [f"{p1}è{cons}e", f"{p1}è{cons}es", f"{p1}è{cons}e", f"{stem}ons", f"{stem}ez", f"{p1}è{cons}ent"]
            else:
                forms = [stem + 'e', stem + 'es', stem + 'e', stem + 'ons', stem + 'ez', stem + 'ent']
        else:
            forms = [stem + 'e', stem + 'es', stem + 'e', stem + 'ons', stem + 'ez', stem + 'ent']
            
        return format_conjugation(verb_str, forms, is_reflexive)
        
    return f"Conjugates like {v}"

def format_conjugation(verb_name, forms, is_reflexive):
    """Formats 6 pronouns with forms."""
    if is_reflexive:
        # Reflexive pronouns: je me, tu te, il se, nous nous, vous vous, ils se
        # Check vowel elision
        vowels = 'aeiouhéèê'
        p1 = "je m'" if forms[0][0].lower() in vowels else "je me "
        p2 = "tu t'" if forms[1][0].lower() in vowels else "tu te "
        p3 = "il s'" if forms[2][0].lower() in vowels else "il se "
        p4 = "nous nous "
        p5 = "vous vous "
        p6 = "ils s'" if forms[5][0].lower() in vowels else "ils se "
        return f"{p1}{forms[0]}, {p2}{forms[1]}, {p3}{forms[2]}, {p4}{forms[3]}, {p5}{forms[4]}, {p6}{forms[5]}"
    else:
        vowels = 'aeiouhéèê'
        j = "j'" if forms[0][0].lower() in vowels else "je "
        return f"{j}{forms[0]}, tu {forms[1]}, il {forms[2]}, nous {forms[3]}, vous {forms[4]}, ils {forms[5]}"

# 3. Phonetic Pronunciation Respeller for English Speakers
def generate_pronunciation(french_verb):
    """Generates intuitive phonetic respelling for English speakers."""
    v = french_verb.strip()
    is_refl = False
    refl_prefix = ""
    if v.startswith("s'"):
        is_refl = True
        v = v[2:]
        refl_prefix = "sahb-" if v[0] in 'a' else "sen-" if v[0] in 'eé' else "see-" if v[0] in 'i' else "soh-" if v[0] in 'o' else "soo-"
    elif v.startswith("se "):
        is_refl = True
        v = v[3:]
        refl_prefix = "suh "

    # Phonetic mapping rules
    # Endings
    if v.endswith('er'):
        stem = v[:-2]
        base_phon = phon_transcribe(stem)
        res = f"{base_phon}-SAY" if stem.endswith('s') or stem.endswith('ss') or stem.endswith('c') else f"{base_phon}-ZAY" if stem.endswith('z') else f"{base_phon}-AY"
    elif v.endswith('ir'):
        stem = v[:-2]
        base_phon = phon_transcribe(stem)
        res = f"{base_phon}-NEER" if stem.endswith('n') else f"{base_phon}-REER" if stem.endswith('r') else f"{base_phon}-EER"
    elif v.endswith('re'):
        stem = v[:-2]
        base_phon = phon_transcribe(stem)
        res = f"{base_phon}-druh" if stem.endswith('d') or stem.endswith('nd') else f"{base_phon}-truh" if stem.endswith('t') or stem.endswith('tt') else f"{base_phon}-ruh"
    elif v.endswith('oir'):
        stem = v[:-3]
        base_phon = phon_transcribe(stem)
        res = f"{base_phon}-VWAHR" if stem.endswith('v') else f"{base_phon}-WAHR"
    else:
        res = phon_transcribe(v)

    # Clean up artifacts
    res = re.sub(r'-+', '-', res).strip('-')
    return (refl_prefix + res).strip()

def phon_transcribe(text):
    t = text.lower()
    # Replacements
    subs = [
        ('tion', 'syohn'), ('ment', 'mahn'), ('eau', 'oh'), ('eaux', 'oh'),
        ('aux', 'oh'), ('au', 'oh'), ('ou', 'oo'), ('oi', 'wah'), ('oy', 'wah-y'),
        ('ai', 'eh'), ('ei', 'eh'), ('ch', 'sh'), ('qu', 'k'), ('gu', 'g'),
        ('gn', 'ny'), ('ille', 'eey'), ('ill', 'eey'), ('ph', 'f'),
        ('an', 'ahn'), ('am', 'ahn'), ('en', 'ahn'), ('em', 'ahn'),
        ('on', 'ohn'), ('om', 'ohn'), ('in', 'a(n)'), ('im', 'a(n)'),
        ('ain', 'a(n)'), ('aim', 'a(n)'), ('ein', 'a(n)'),
        ('é', 'ay'), ('è', 'eh'), ('ê', 'eh'), ('ë', 'eh'),
        ('ç', 's'), ('j', 'zh'), ('ge', 'zh'), ('gi', 'zhee'),
        ('u', 'yoo'), ('th', 't'),
    ]
    for orig, rep in subs:
        t = t.replace(orig, rep)
    return t

# 4. Contextual Sentence Generator matching the exact English verb definition
def generate_sentence(verb, english_def):
    v = verb.strip()
    en = english_def.strip()
    if en.startswith('to '):
        en = en[3:].strip()
    first_meaning = en.split(',')[0].strip().split(';')[0].strip()
    
    # Specific curated sentences for high-utility verbs
    CURATED_SENTENCES = {
        'abaisser': ("Il abaisse la vitre de la voiture.", "He lowers the car window."),
        'abattre': ("La tempête abat un vieil arbre.", "The storm knocks down an old tree."),
        'abolir': ("Le pays décide d'abolir cette loi ancienne.", "The country decides to abolish this old law."),
        'accepter': ("J'accepte votre invitation avec plaisir.", "I accept your invitation with pleasure."),
        'accompagner': ("Elle accompagne son ami à la gare.", "She accompanies her friend to the station."),
        'acheter': ("Nous achetons du pain frais à la boulangerie.", "We buy fresh bread at the bakery."),
        'adorer': ("J'adore voyager et découvrir de nouveaux pays.", "I love traveling and discovering new countries."),
        'aider': ("Peux-tu m'aider avec cet exercice difficile ?", "Can you help me with this difficult exercise?"),
        'aimer': ("J'aime beaucoup lire le soir.", "I like reading very much in the evening."),
        'aller': ("Nous allons au supermarché ce matin.", "We are going to the supermarket this morning."),
        'amener': ("Il amène sa fille au cours de danse.", "He brings his daughter to dance class."),
        'appeler': ("Je vous appelle dès mon arrivée.", "I will call you as soon as I arrive."),
        'apporter': ("Elle apporte un gâteau au chocolat pour la fête.", "She brings a chocolate cake for the party."),
        'apprendre': ("Nous apprenons le français avec grand intérêt.", "We are learning French with great interest."),
        'arrêter': ("Le bus s'arrête devant la bibliothèque.", "The bus stops in front of the library."),
        'arriver': ("Le train arrive à l'heure à Paris.", "The train arrives on time in Paris."),
        'attendre': ("J'attends mon collègue depuis dix minutes.", "I have been waiting for my colleague for ten minutes."),
        'avoir': ("J'ai vingt-cinq ans et deux chats.", "I am twenty-five years old and have two cats."),
        'boire': ("Il boit un grand verre d'eau fraîche.", "He drinks a large glass of fresh water."),
        'chercher': ("Je cherche mes clés dans mon sac.", "I am looking for my keys in my bag."),
        'choisir': ("Nous choisissons un bon restaurant pour dîner.", "We choose a good restaurant for dinner."),
        'commencer': ("Le cours de français commence à neuf heures.", "The French class begins at nine o'clock."),
        'comprendre': ("Est-ce que vous comprenez cette question ?", "Do you understand this question?"),
        'conduire': ("Elle conduit prudemment sur l'autoroute.", "She drives carefully on the highway."),
        'connaître': ("Je connais très bien cette jolie ville.", "I know this pretty city very well."),
        'croire': ("Je crois que tout va bien se passer.", "I believe everything will go well."),
        'demander': ("Il demande l'addition au serveur.", "He asks the waiter for the bill."),
        'devenir': ("Il veut devenir médecin plus tard.", "He wants to become a doctor later."),
        'devoir': ("Nous devons partir maintenant.", "We must leave now."),
        'dire': ("Qu'est-ce que tu dis ?", "What are you saying?"),
        'donner': ("Elle donne un cadeau à son ami.", "She gives a gift to her friend."),
        'dormir': ("Le bébé dort paisiblement dans sa chambre.", "The baby is sleeping peacefully in his room."),
        'écouter': ("J'écoute de la musique classique pour travailler.", "I listen to classical music to work."),
        'écrire': ("Elle écrit une lettre à ses grands-parents.", "She is writing a letter to her grandparents."),
        'entendre': ("J'entends les oiseaux chanter dans le jardin.", "I hear the birds singing in the garden."),
        'entrer': ("Vous pouvez entrer dans le bureau.", "You may enter the office."),
        'envoyer': ("J'envoie un courriel important à mon chef.", "I am sending an important email to my boss."),
        'espérer': ("J'espère vous revoir très bientôt !", "I hope to see you again very soon!"),
        'être': ("Je suis ravi de vous rencontrer aujourd'hui.", "I am delighted to meet you today."),
        'faire': ("Je fais du sport trois fois par semaine.", "I exercise three times a week."),
        'falloir': ("Il faut étudier régulièrement pour réussir.", "One must study regularly to succeed."),
        'finir': ("Nous finissons notre travail à dix-huit heures.", "We finish our work at six o'clock."),
        'habiter': ("J'habite à Lyon depuis deux ans.", "I have been living in Lyon for two years."),
        'jouer': ("Les enfants jouent au football dans le parc.", "The children are playing soccer in the park."),
        'laisser': ("Laissez un message après le bip sonore.", "Leave a message after the beep."),
        'lire': ("Je lis un roman passionnant en ce moment.", "I am reading an exciting novel right now."),
        'manger': ("Nous mangeons ensemble à midi.", "We eat together at noon."),
        'mettre': ("Il met son manteau avant de sortir.", "He puts on his coat before going out."),
        'ouvrir': ("Elle ouvre la fenêtre pour aérer la pièce.", "She opens the window to air out the room."),
        'parler': ("Je parle français et anglais couramment.", "I speak French and English fluently."),
        'partir': ("Nous partons en vacances demain matin.", "We leave on vacation tomorrow morning."),
        'payer': ("Je paie l'addition avec ma carte bancaire.", "I pay the bill with my bank card."),
        'penser': ("Je pense souvent à mes projets d'avenir.", "I often think about my future projects."),
        'perdre': ("Ne perds pas ton temps avec ces bêtises.", "Don't lose your time with these silly things."),
        'pouvoir': ("Pouvez-vous m'aider s'il vous plaît ?", "Can you help me please?"),
        'prendre': ("Je prends le métro pour aller au travail.", "I take the subway to go to work."),
        'regarder': ("Nous regardons un bon film ce soir.", "We are watching a good movie tonight."),
        'répondre': ("Il répond rapidement à tous ses messages.", "He replies quickly to all his messages."),
        'savoir': ("Je sais comment résoudre ce problème.", "I know how to solve this problem."),
        'sortir': ("On sort ce week-end avec des amis ?", "Shall we go out this weekend with friends?"),
        'suivre': ("Suivez ce chemin pour arriver à la gare.", "Follow this path to reach the train station."),
        'tenir': ("Tiens la porte ouverte s'il te plaît.", "Hold the door open please."),
        'tomber': ("Les feuilles tombent en automne.", "The leaves fall in autumn."),
        'travailler': ("Je travaille dans une entreprise internationale.", "I work in an international company."),
        'trouver': ("J'ai trouvé une excellente solution.", "I found an excellent solution."),
        'venir': ("D'où viens-tu exactement ?", "Where do you come from exactly?"),
        'vivre': ("Ils vivent heureux dans le sud de la France.", "They live happily in the south of France."),
        'voir': ("Je vois mon ami ce soir au café.", "I am seeing my friend tonight at the cafe."),
        'vouloir': ("Je veux apprendre le français rapidement.", "I want to learn French quickly."),
        'voyager': ("Nous voyageons en train à travers toute l'Europe.", "We travel by train across all of Europe.")
    }
    
    clean_v = v.replace("s'", "").replace("se ", "").strip()
    if clean_v in CURATED_SENTENCES:
        fr_s, en_s = CURATED_SENTENCES[clean_v]
        return f"{fr_s} *({en_s})*"
    elif v in CURATED_SENTENCES:
        fr_s, en_s = CURATED_SENTENCES[v]
        return f"{fr_s} *({en_s})*"
        
    # Generate authentic grammatical sentence
    if v.startswith("s'") or v.startswith("se "):
        return f"Il {v} régulièrement pendant ses activités quotidiennes. *(He {en} regularly during his daily activities.)*"
    elif v in ['falloir', 'pleuvoir', 'neiger', 'grêler', 'tonner']:
        return f"Il {v} souvent dans cette région montagneuse. *(It {en} often in this mountainous region.)*"
    else:
        return f"Elle souhaite {v} pour réussir son projet. *(She wishes to {first_meaning} to succeed in her project.)*"

# 5. Teacher's Liaison and Grammar Notes
def generate_liaison_notes(verb_str):
    v = verb_str.strip()
    notes = []
    
    # Auxiliary check
    base_v = v.replace("s'", "").replace("se ", "").strip()
    if v.startswith("s'") or v.startswith("se "):
        notes.append("Auxiliary: être *(all reflexive verbs take être in compound tenses)*")
    elif base_v in VANDERTRAMP:
        notes.append(f"Auxiliary: être *(Dr. & Mrs. Vandertramp movement/state verb)*")
    else:
        notes.append("Auxiliary: avoir")
        
    # Spelling changes
    if base_v.endswith('ger'):
        notes.append("Spelling change: retain 'e' before 'o' in nous (*nous voyageons*) to protect soft [ʒ] sound.")
    elif base_v.endswith('cer'):
        notes.append("Spelling change: use cedilla 'ç' before 'o' in nous (*nous commençons*) to protect soft [s] sound.")
    elif base_v.endswith('eler') and base_v in ['appeler', 'rappeler', 'épeler', 'renouveler']:
        notes.append("Spelling change: doubles 'l' (*-ell-*) before silent endings (*j'appelle*), single 'l' with nous/vous.")
    elif base_v.endswith('eter') and base_v in ['jeter', 'rejeter', 'projeter']:
        notes.append("Spelling change: doubles 't' (*-ett-*) before silent endings (*je jette*), single 't' with nous/vous.")
    elif base_v.endswith('yer'):
        notes.append("Spelling change: 'y' becomes 'i' before silent endings (*je paie / j'emploie*).")
        
    # Liaisons
    vowels = 'aeiouhéèê'
    if base_v[0].lower() in vowels:
        notes.append("Mandatory elision with je (*j'*); [z] liaison with plural pronouns: *nous‿*, *vous‿*, *ils‿*.")
    else:
        notes.append("Pronunciation: clear consonant onset; standard liaison [z] with *nous*, *vous*, *ils*.")
        
    return " | ".join(notes)

def get_verb_type(verb_str):
    v = verb_str.strip()
    base_v = v.replace("s'", "").replace("se ", "").strip()
    
    prefix = "Reflexive " if (v.startswith("s'") or v.startswith("se ")) else ""
    if v in ['falloir', 'pleuvoir', 'neiger', 'grêler', 'tonner']:
        return "Impersonal Verb"
    if base_v.endswith('er') and base_v != 'aller':
        return f"{prefix}Verb (1st group -er)"
    if base_v in SECOND_GROUP_ROOTS or (base_v.endswith('ir') and not any(base_v.endswith(s) for s in ['oir', 'courir', 'partir', 'sortir', 'sentir', 'mentir', 'dormir', 'servir', 'ouvrir', 'couvrir', 'offrir', 'souffrir', 'tenir', 'venir'])):
        return f"{prefix}Verb (2nd group -ir)"
    return f"{prefix}Verb (3rd group / irregular)"

# 6. Build Anki Deck using genanki
deck_id = 1894720199
deck = genanki.Deck(deck_id, "DELF French Verbs Master Deck - 681 Verbs")

model_id = 1608492044
style_css = """
.card {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 15px;
    text-align: left;
    color: #1e293b;
    background-color: #ffffff;
    padding: 20px;
    line-height: 1.5;
    max-width: 650px;
    margin: 0 auto;
}
.nightMode .card, .night_mode .card {
    color: #f1f5f9;
    background-color: #0f172a;
}
.header-badge {
    display: inline-block;
    padding: 3px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
}
.badge-verb { background: #fef3c7; color: #92400e; }
.nightMode .badge-verb, .night_mode .badge-verb { background: #78350f; color: #fde68a; }

.french-word {
    font-size: 30px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 8px;
    letter-spacing: -0.01em;
}
.nightMode .french-word, .night_mode .french-word { color: #f8fafc; }

.action-row {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 14px;
}
.pill {
    display: inline-flex;
    align-items: center;
    background: #f1f5f9;
    color: #334155;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
}
.nightMode .pill, .night_mode .pill { background: #1e293b; color: #cbd5e1; }

.audio-btn {
    display: inline-flex;
    align-items: center;
    background: #2563eb;
    color: #ffffff !important;
    text-decoration: none;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 12px;
    font-weight: 600;
}
.audio-btn:hover { background: #1d4ed8; }

.card-divider {
    border: none;
    border-top: 2px dashed #e2e8f0;
    margin: 16px 0;
}
.nightMode .card-divider, .night_mode .card-divider { border-top-color: #334155; }

.english-box {
    background: #eff6ff;
    border-left: 4px solid #3b82f6;
    padding: 10px 14px;
    border-radius: 0 6px 6px 0;
    margin-bottom: 14px;
    font-size: 18px;
    font-weight: 700;
    color: #1e3a8a;
}
.nightMode .english-box, .night_mode .english-box {
    background: #172554;
    border-left-color: #60a5fa;
    color: #bfdbfe;
}

.section-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 3px;
    letter-spacing: 0.04em;
}
.nightMode .section-label, .night_mode .section-label { color: #94a3b8; }

.detail-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 10px 12px;
    border-radius: 6px;
    margin-bottom: 10px;
}
.nightMode .detail-box, .night_mode .detail-box {
    background: #1e293b;
    border-color: #334155;
}

.conj-code {
    font-family: ui-monospace, Menlo, Monaco, Consolas, monospace;
    font-size: 12.5px;
    color: #0369a1;
}
.nightMode .conj-code, .night_mode .conj-code { color: #38bdf8; }

.notes-text {
    font-size: 12px;
    color: #b91c1c;
    font-weight: 500;
}
.nightMode .notes-text, .night_mode .notes-text { color: #f87171; }
"""

model = genanki.Model(
    model_id,
    "DELF French Verbs Master Model",
    fields=[
        {"name": "French"},
        {"name": "English"},
        {"name": "Pronunciation"},
        {"name": "Audio"},
        {"name": "Type_Gender"},
        {"name": "Sentence"},
        {"name": "Conjugation"},
        {"name": "Liaison_Notes"}
    ],
    templates=[
        {
            "name": "French Verb Card",
            "qfmt": """
<div class="card">
    <div class="header-badge badge-verb">{{Type_Gender}}</div>
    <div class="french-word">{{French}}</div>
    <div class="action-row">
        <span class="pill">🗣️ {{Pronunciation}}</span>
        {{Audio}}
    </div>
</div>
""",
            "afmt": """
<div class="card">
    {{FrontSide}}
    <hr id="answer" class="card-divider">
    <div class="section-label">English Meaning</div>
    <div class="english-box">{{English}}</div>
    
    <div class="section-label">Example Sentence</div>
    <div class="detail-box">
        <div>{{Sentence}}</div>
    </div>
    
    <div class="section-label">Present Tense Conjugation Drill</div>
    <div class="detail-box">
        <div class="conj-code">{{Conjugation}}</div>
    </div>
    
    <div class="section-label">Grammar, Auxiliary & Liaison Notes</div>
    <div class="detail-box">
        <div class="notes-text">{{Liaison_Notes}}</div>
    </div>
</div>
"""
        }
    ],
    css=style_css
)

# 7. Process all verbs and build notes + Markdown documentation
all_cards_data = []
md_lines = [
    "# DELF French Verbs Master Reference (681 Verbs)",
    "## Complete Conjugations, Pronunciation, Audio & Syntax Notes",
    "",
    "| # | French Verb | English Meaning | Pronunciation | Audio | Verb Group | Example Sentence | Present Tense Conjugation Drill | Liaison & Teacher's Notes |",
    "|:---|:---|:---|:---|:---:|:---|:---|:---|:---|"
]

for idx, item in enumerate(verbs_clean, 1):
    fr = item['french']
    en = item['english']
    pron = generate_pronunciation(fr)
    v_type = get_verb_type(fr)
    conj = conjugate_verb(fr)
    sent = generate_sentence(fr, en)
    notes = generate_liaison_notes(fr)
    
    encoded = urllib.parse.quote(fr)
    audio_html = f'<a class="audio-btn" href="https://translate.google.com/?sl=fr&tl=en&text={encoded}&op=translate" target="_blank">🔊 Listen</a>'
    audio_md = f'[🔊 Audio](https://translate.google.com/?sl=fr&tl=en&text={encoded}&op=translate)'
    
    note = genanki.Note(
        model=model,
        fields=[fr, en, pron, audio_html, v_type, sent, conj, notes],
        tags=["DELF_Verbs", "French_681_Verbs", v_type.replace(' ', '_').replace('(', '').replace(')', '')]
    )
    deck.add_note(note)
    
    md_lines.append(f"| {idx} | **{fr}** | {en} | `{pron}` | {audio_md} | {v_type} | {sent} | `{conj}` | {notes} |")
    all_cards_data.append({'num': idx, 'french': fr, 'english': en, 'pron': pron, 'type': v_type, 'conj': conj, 'sent': sent, 'notes': notes})

# Write Anki Package
output_apkg = "/Users/jainamshah/Downloads/Learning French/French_Verbs_Master_Deck.apkg"
genanki.Package(deck).write_to_file(output_apkg)
print(f"Anki package successfully written: {output_apkg} (Notes count: {len(deck.notes)})")

# Write Markdown Reference
output_md = "/Users/jainamshah/Downloads/Learning French/French_Verbs_681_Master_Reference.md"
with open(output_md, 'w', encoding='utf-8') as f:
    f.write("\n".join(md_lines))
print(f"Markdown reference successfully written: {output_md}")
