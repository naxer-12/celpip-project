# enrich_vocab_pronunciation.py
# Systematically upgrades all 200 vocabulary entries with intuitive syllable breakdowns,
# IPA-adjacent respellings, and explicit English sound keys.

import json
import re

def enrich_database():
    with open("/Users/jainamshah/Downloads/Learning French/vocab_data.py") as f:
        content = f.read()

    # We can extract the ALL_VOCABULARY list
    import vocab_data
    items = vocab_data.ALL_VOCABULARY

    # Specific phonetic map for high precision
    pronunciation_map = {
        "fromage": ("froh • MAHZH", "Soft 'zh' like 's' in measure/treasure; final 'e' silent."),
        "voyage": ("vwah • YAHZH", "'vwah' + 'YAHZH'; rhymes with garage."),
        "message": ("meh • SAHZH", "'meh' + 'SAHZH'; soft 'zh'."),
        "plage": ("PLAHZH", "Rhymes with lodge with a soft 'zh' glide; final 'e' silent."),
        "image": ("ee • MAHZH", "Stress on second syllable: 'ee' + 'MAHZH'."),
        "page": ("PAHZH", "'ah' vowel like father + 'zh'."),
        "cage": ("KAHZH", "Rhymes with 'dodge' with a smooth 'zh' glide."),
        "bateau": ("bah • TOH", "'eau' sounds like 'oh' in boat or show."),
        "château": ("shah • TOH", "'ch' sounds like 'sh'; 'eau' sounds like 'oh'."),
        "chapeau": ("shah • POH", "'ch' sounds like 'sh'; rhymes with 'go'."),
        "cadeau": ("kah • DOH", "Hard 'k' sound + 'DOH'."),
        "couteau": ("koo • TOH", "'ou' sounds like 'oo' in soup + 'TOH'."),
        "eau": ("LOH", "Sounds identical to the English word 'low'."),
        "peau": ("POH", "Sounds identical to English 'Poe' (Edgar Allan Poe)."),
        "pain": ("PAN", "Nasal vowel like 'can' through the nose; do NOT pronounce the 'n'!"),
        "train": ("TRAN", "Nasal vowel; do not speak the 'n' consonant."),
        "bain": ("BAN", "Nasal vowel; rhymes with French 'pain' and 'vin'."),
        "main": ("MAN", "Nasal vowel; 'n' is not pronounced; hand."),
        "journal": ("zhoor • NAHL", "'zh' like vision + 'oor' + 'NAHL'."),
        "cheval": ("shuh • VAHL", "'shuh' + 'VAHL' like valve without the 'v'."),
        "travail": ("trah • VYE", "'vye' rhymes with eye / pie."),
        "fauteuil": ("foh • TUH-ee", "'tuh' with rounded lips + 'ee' glide."),
        "médicament": ("may • dee • kah • MAHN", "Nasal 'mahn' like haunt; final 't' is silent."),
        "argent": ("ahr • ZHAHN", "Nasal 'zhahn'; final 't' is silent."),
        "restaurant": ("rehs • toh • RAHN", "Nasal 'rahn'; final 't' is silent."),
        "dent": ("DAHN", "Nasal 'dahn'; final 't' is completely silent!"),
        "cahier": ("kah • YAY", "Two syllables: 'kah' + 'YAY'."),
        "café": ("kah • FAY", "Both syllables crisp: 'kah' + 'FAY'."),
        "problème": ("proh • BLEHM", "Rhymes with 'hem' or 'gem'; final 'e' silent."),
        "système": ("sees • TEHM", "Rhymes with 'stem'; final 'e' silent."),
        "question": ("kehs • TYOHN", "Nasal 'tyohn' like yawn through the nose."),
        "solution": ("soh • loo • SYOHN", "Nasal 'syohn' at the end."),
        "maison": ("may • ZOHN", "Nasal 'zohn' like zone through the nose."),
        "bicyclette": ("bee • see • KLEHT", "Rhymes with 'bet'; 'ette' makes crisp 't'."),
        "fourchette": ("foor • SHEHT", "'foor' like poor + 'SHEHT'."),
        "journée": ("zhoor • NAY", "'zhoor' + 'NAY' like neigh."),
        "soirée": ("swah • RAY", "'swah' + 'RAY' like ray of light."),
        "idée": ("ee • DAY", "'ee' + 'DAY' like day."),
        "musée": ("mew • ZAY", "Round lips as if whistling while saying 'ee' for 'u'."),
        "voiture": ("vwah • TYOOR", "'vwah' + 'tyoor'; 'ure' with rounded French 'u'."),
        "ville": ("VEEL", "Sounds like 'veal' in English."),
        "nuit": ("NWEE", "One syllable: 'nwee'; final 't' is completely silent!"),
        "mer": ("MEHR", "Open 'eh' sound; throaty French 'r'."),
        "fin": ("FAN", "Nasal vowel; do NOT pronounce the 'n'!"),
        "photo": ("foh • TOH", "Two round 'oh' sounds: 'foh' + 'TOH'."),
        "mariage": ("mah • ree • YAHZH", "Three syllables: 'mah' + 'ree' + 'YAHZH'."),
        "courage": ("koo • RAHZH", "'koo' like coo + 'RAHZH'."),
        "tableau": ("tah • BLOH", "'tah' + 'BLOH'."),
        "sentiment": ("sahn • tee • MAHN", "Two nasal vowels; final 't' silent."),
        "gouvernement": ("goo • vehr • nuh • MAHN", "'goo' + 'vehr' + 'nuh' + nasal 'MAHN'."),
        "chêne": ("SHEHN", "Open 'eh' sound; rhymes with 'rain' without the 'i'."),
        "pommier": ("poh • MYAY", "'poh' + 'MYAY' like yay."),
        "pomme": ("POHM", "Short open 'o'; rhymes with 'from'."),
        "citron": ("see • TROHN", "Nasal 'trohn' like drone through the nose."),
        "décision": ("day • see • ZYOHN", "Nasal 'zyohn' at the end."),
        "liberté": ("lee • behr • TAY", "'lee' + 'behr' + 'TAY'."),
        "vérité": ("vay • ree • TAY", "'vay' + 'ree' + 'TAY'."),
        "beauté": ("boh • TAY", "'boh' like beau + 'TAY'."),
        "chance": ("SHAHNS", "Nasal 'shahns' like haunt."),
        "différence": ("dee • fay • RAHNS", "Nasal 'rahns' at the end."),
        "silence": ("see • LAHNS", "Nasal 'lahns'; final 'e' silent."),
        "chaleur": ("shah • LUHR", "'luhr' rhyming with fur or purr."),
        "couleur": ("koo • LUHR", "'koo' like cool + 'LUHR'."),
        "bonheur": ("boh • NUHR", "'boh' + 'nuhr' rhyming with fur."),
        "saison": ("say • ZOHN", "'say' + nasal 'ZOHN'."),
        "chanson": ("shahn • SOHN", "Two nasals: 'shahn' + 'SOHN'."),
        "boisson": ("bwah • SOHN", "'bwah' + nasal 'SOHN'."),
        "tire-bouchon": ("teer • boo • SHOHN", "'teer' + 'boo' + nasal 'SHOHN'."),
        "porte-monnaie": ("pohrt • moh • NAY", "'pohrt' + 'moh' + 'NAY'."),
        "France": ("FRAHNS", "Nasal 'frahns'."),
        "Canada": ("kah • nah • DAH", "All three 'a' vowels open and crisp."),
        "Mexique": ("mehk • SEEK", "'mehk' + 'SEEK'; final 'que' is a crisp 'k'."),
        "infirmier": ("an • feer • MYAY", "Nasal 'an' + 'feer' + 'MYAY'."),
        "infirmière": ("an • feer • MYEHR", "'myehr' rhyming with care."),
        "serveur": ("sehr • VUHR", "'sehr' + 'VUHR' rhyming with fur."),
        "serveuse": ("sehr • VUHZ", "'vuhz' with soft 'zh'."),
        "acteur": ("ahk • TUHR", "'ahk' + 'TUHR' rhyming with purr."),
        "actrice": ("ahk • TREES", "'ahk' + 'TREES' like peace with 'tr'."),
        "livre": ("LEEVR", "'lee' + soft 'vr' blend."),
        "tour": ("TOOR", "Sounds like 'tour' in English."),
        "chat": ("SHAH", "Sounds like 'shah' of Iran; final 't' is silent!"),
        "chatte": ("SHAHT", "Crisp 't' pronounced at the end."),
        "forêt": ("foh • REH", "Circumflex 'ê' is open 'eh'; final 't' is silent!"),
        "voix": ("VWAH", "'vwah'; final 'x' is completely silent!"),
        "paix": ("PEH", "'peh' rhyming with bed without the 'd'; final 'x' silent!"),
        "squelette": ("skuh • LEHT", "'skuh' + 'LEHT' rhyming with pet."),
        "parapluie": ("pah • rah • PLWEE", "'plwee' rhyming with tree."),
        "lycée": ("lee • SAY", "Sounds like 'lease' + 'say'.")
    }

    for item in items:
        noun = item["french"].split()[-1].replace("'", "").replace("’", "")
        # Strip punctuation
        noun_clean = re.sub(r'[^a-zA-Zàâäéèêëîïôöùûüç-]', '', noun).lower()

        if noun_clean in pronunciation_map:
            syll, tip = pronunciation_map[noun_clean]
            item["syllables"] = syll
            item["sound_tip"] = tip
        else:
            # Generate smart syllables and tip based on endings
            base_phon = item["phonetic"].replace("[", "").replace("]", "").strip()
            # remove 'luh ' or 'lah '
            words = base_phon.split()
            noun_phon = words[-1] if len(words) > 1 else words[0]
            item["syllables"] = " • ".join(noun_phon.split("-")) if "-" in noun_phon else noun_phon

            if item["french"].endswith("e"):
                item["sound_tip"] = "Final silent 'e'; stress falls on the preceding syllable."
            elif item["french"].endswith(("t", "d", "s", "x")):
                last_letter = item["french"][-1]
                item["sound_tip"] = f"Final '{last_letter}' is completely silent!"
            elif any(item["french"].endswith(s) for s in ["on", "an", "en", "in", "ain"]):
                item["sound_tip"] = "Nasal vowel sound; do not pronounce the consonant 'n'!"
            else:
                item["sound_tip"] = "Pronounce clearly with standard French syllable cadence."

    # Write back to vocab_data.py
    new_code = f"""# vocab_data.py
# Fully enriched master vocabulary dataset with intuitive syllable breakdowns,
# phonetic transcriptions, explicit English sound tips, and memory anchors.

ALL_VOCABULARY = {json.dumps(items, indent=2, ensure_ascii=False)}
"""
    # Replace json booleans with Python booleans
    new_code = new_code.replace(': false,', ': False,').replace(': true,', ': True,')

    with open("/Users/jainamshah/Downloads/Learning French/vocab_data.py", "w") as f:
        f.write(new_code)

    print(f"Successfully enriched all {len(items)} vocabulary items in vocab_data.py!")

if __name__ == "__main__":
    enrich_database()
