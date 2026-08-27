# -*- coding: utf-8 -*-
"""112a - I nomi propri che le righe-fonte del corpo portano dentro, e la
resa che il progetto ha GIA' deciso per ognuno.

⚠️ Le reti del lotto non leggono `glossario.md`. I 224 titoli-fonte sono pieni
di nomi di divinita', di personaggi e di citta' che il progetto ha gia' reso
altrove — e renderli una seconda volta in un altro modo spacca la famiglia in
silenzio, perche' nessuna rete confronta un titolo con un nome di creatura.
Qui i nomi si estraggono dai titoli e si cercano **per inglese** in tutto il
dizionario, che e' il verso che `lotti-111/_cerca.py` non copre.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-nomi-fonti.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_112-nomi-fonti.py --parola Irva
"""
import argparse
import collections
import glob
import importlib.util
import json
import re
from pathlib import Path

_qui = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    '_112_corpo', _qui / '_112-corpo-descrizioni.py')
_112 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_112)

# i nomi che i titoli marcano con le parentesi angolari, e le maiuscole sciolte
_ANGOLARI = re.compile(r'<([^>]+)>')
_MAIUSCOLA = re.compile(r'\b([A-Z][a-z]{2,})\b')

# parole inglesi comuni che cominciano per maiuscola solo perche' stanno in un
# titolo: non sono nomi propri e cercarle non serve a niente
_COMUNI = {
    'The', 'Big', 'Book', 'Books', 'Great', 'Collection', 'Guide', 'Report',
    'Category', 'Edition', 'Issue', 'Extra', 'Special', 'Words', 'Note',
    'Encyclopedia', 'Catalogue', 'Compendium', 'Almanac', 'Alamanac', 'Food',
    'Item', 'Items', 'Plants', 'Seaweed', 'Volume', 'First', 'Winter',
    'Summer', 'Travels', 'Fashion', 'Art', 'Music', 'Tunes', 'Songs', 'Game',
    'Tricks', 'All', 'Ages', 'Version', 'Gifts', 'Cheap', 'Your', 'Kids',
    'Home', 'Daily', 'Necessities', 'Supporting', 'Roles', 'Kitchen',
    'Streets', 'Drinks', 'Drink', 'Not', 'You', 'Can', 'Use', 'Too',
    'Illustrated', 'Living', 'Iron', 'Stomach', 'Complete', 'Diet', 'Bureau',
    'Punditry', 'Lead', 'Developer', 'Monologue', 'Witch', 'Words', 'Worlds',
    'Never', 'Seen', 'Sickly', 'Taste', 'Smoke', 'Heated', 'Duelists',
    'Battles', 'Dragons', 'Swords', 'Magic', 'Magical', 'Ways', 'Waste',
    'Utilization', 'Mysterious', 'Ancient', 'Ornaments', 'Tools', 'Tool',
    'Interior', 'Paradise', 'Stylish', 'Sewing', 'Poison', 'Alchemy',
    'Introduction', 'Mineralogy', 'Necromancy', 'Noobs', 'Weird', 'Memo',
    'Bizarre', 'Gossip', 'Worried', 'Citizen', 'Close', 'Look', 'Rituals',
    'Forest', 'Economics', 'Sawmill', 'Pursuing', 'Mythical', 'Behind',
    'Favorites', 'Prophecy', 'Airlines', 'Sales', 'Real', 'Estate',
    'Unlisted', 'Listed', 'Legendary', 'Smith', 'Shady', 'Old', 'Shopkeeper',
    'Command', 'Control', 'Battlefield', 'Life', 'Saving', 'Aid', 'Top',
    'Most', 'Popular', 'Products', 'Among', 'Prisoners', 'Teacher',
    'Training', 'Machine', 'Center', 'Bondage', 'History', 'Historical',
    'Blacksmithing', 'Sister', 'Energy', 'Waves', 'Punched', 'Insect',
    'Footnote', 'Adult', 'Must', 'Watch', 'Everything', 'About', 'Savings',
    'Asset', 'Management', 'Discovery', 'Curiosities', 'World', 'Mystery',
    'Dangers', 'Road', 'Little', 'Girl', 'Bedtime', 'Story', 'Fool',
    'Twice', 'Shame', 'Public', 'Services', 'Relations', 'Pet', 'Trainer',
    'Slave', 'Armored', 'General', 'Captain', 'Special', 'Forces', 'Shark',
    'Believer', 'Bored', 'Necromancer', 'Fanatic', 'Embark', 'Occultists',
    'Evil', 'Wizard', 'Researcher', 'Goddess', 'Wealth', 'Ninja', 'Secret',
    'Survival', 'Anyone', 'Hazardous', 'Materials', 'Handling', 'Manual',
    'Fossil', 'Enthusiast', 'Whizzard', 'Administration', 'Medicines',
    'Agriculture', 'New', 'Possibilities', 'Wide', 'Alcohol', 'Wisdom',
    'Glimpse', 'Lost', 'Technology', 'Legacy', 'Mechanical', 'Civilization',
    'Weeds', 'Eat', 'Seaweed', 'Sea', 'Weed', 'Weapons', 'Excavated',
    'Battle', 'Hobby', 'Legend', 'Coins', 'This', 'Censored', 'Box', 'Mania',
    'Future', 'Monster', 'Damage', 'Countermeasures', 'Expert', 'Marksman',
    'Huntsman', 'Gift', 'Loved', 'Ones', 'Dying', 'For', 'Let', 'Today',
    'Slavery', 'Grave', 'Robber', 'Choosing', 'Best', 'Craftsmen',
    'Revenue', 'Livestock', 'Intel', 'Informant', 'Adventurer', 'Travelers',
    'Aiming', 'Better', 'Workmanship', 'Ore', 'Horticulture', 'Gardening',
    'Winning', 'Strategy', 'Trading', 'Trade', 'Junk', 'Love', 'Thousands',
    'Pieces', 'Melodious', 'Knowledge', 'Secrt', 'Armaments', 'Tomorrow',
    'Everchanging', 'Fantasy', 'Furnitures', 'North', 'Armor', 'Advertisements',
    'Cont', 'Merchant', 'Starting', 'Quitting', 'Totally', 'Made', 'Stories',
    'That', 'Are', 'Mistaken', 'Lies', 'Provocasquid', 'Defeated', 'Nefia',
    'Scholar', 'Puppy', 'Innocent', 'Bomber', 'Bearded', 'Guy', 'Thief',
    'Watchman', 'Kid', 'Messenger', 'Arsonist', 'Outcast', 'Cat', 'Hater',
    'Crooked', 'Daydreamer', 'Suffering', 'Novice', 'Knight', 'Womanizer',
    'Honest', 'Rogue', 'Note', 'Cover', 'Page', 'Instruction', 'Imouto',
    'Leading', 'Guildmaster', 'Notice', 'Good', 'Store', 'Cleaner',
    'Executioner', 'Excutioner', 'Pre', 'Censorship', 'Last', 'Noble',
    'Bag', 'Back', 'Written', 'Box', 'Critic', 'Fairy', 'Invoker',
    'Caramel', 'Maker', 'Indebted', 'Nausea', 'Victim', 'Curse', 'Sunbararian',
    'Destruction', 'God', 'Blanket', 'Wrapped', 'Girl', 'Younger', 'Grand',
    'Son', 'Blue', 'Haired', 'Great', 'Marks', 'Scene', 'Grimoire',
    'Technician', 'Proclaimed', 'Genius', 'Self', 'Fisherman', 'Proud',
    'Catch', 'Crimson', 'Eccentric', 'Bandit', 'Sockswordman', 'Poet',
    'Nameless', 'Scribbling', 'Notebook', 'Amateur', 'Bewildered', 'Nerd',
    'Plug', 'Potio', 'Attached', 'Mysterious', 'Chains', 'Showing', 'Off',
    'Aion', 'Extenders',
}


def nomi_dai_titoli():
    voci = _112.carica_corpo()
    titoli = collections.Counter()
    for riga, idx, en, it in voci:
        voluta = _112.voluta_fonte(en)
        if voluta:
            titoli[voluta.strip()] += 1

    angolari = collections.Counter()
    sciolti = collections.Counter()
    for t, quante in titoli.items():
        for nome in _ANGOLARI.findall(t):
            angolari[nome.strip()] += quante
        senza = _ANGOLARI.sub(' ', t)
        for parola in _MAIUSCOLA.findall(senza):
            if parola not in _COMUNI:
                sciolti[parola] += quante
    return titoli, angolari, sciolti


def cerca_per_inglese(termine, massimo=6):
    """Le voci del dizionario il cui INGLESE contiene il termine, con l'italiano."""
    fuori = []
    visti = set()
    for percorso in sorted(glob.glob('dizionario/*.jsonl')):
        nome = Path(percorso).stem
        with open(percorso, encoding='utf-8') as f:
            for riga in f:
                if not riga.strip():
                    continue
                d = json.loads(riga)
                en, it = d.get('en') or '', d.get('it') or ''
                if termine not in en or not it:
                    continue
                # le voci corte sono i NOMI: quelle lunghe sono prosa che lo cita
                if len(en) > 60:
                    continue
                chiave = (en, it)
                if chiave in visti:
                    continue
                visti.add(chiave)
                fuori.append((nome, en, it))
    fuori.sort(key=lambda t: len(t[1]))
    return fuori[:massimo], len(fuori)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--parola', help='cerca un singolo termine per inglese')
    args = ap.parse_args()

    if args.parola:
        righe, quante = cerca_per_inglese(args.parola, massimo=20)
        print(f'### {args.parola}  ({quante} voci)')
        for nome, en, it in righe:
            print(f'  [{nome}] {en}  ->  {it}')
        return

    titoli, angolari, sciolti = nomi_dai_titoli()
    print(f'titoli-fonte distinti: {len(titoli)}')
    print()

    print('=== I NOMI FRA PARENTESI ANGOLARI <...>')
    print('   sono la marca che il gioco usa per i personaggi con un nome proprio')
    for nome, quante in angolari.most_common():
        righe, totale = cerca_per_inglese(nome)
        if righe:
            reso = righe[0][2]
            print(f'  {nome:<22} ({quante:>3} righe)  GIA\' RESO: {reso}'
                  f'   [{righe[0][0]}]')
        else:
            print(f'  {nome:<22} ({quante:>3} righe)  ⚠️ NON TROVATO nel dizionario')
    print()

    print('=== GLI ALTRI NOMI PROPRI, sciolti nel titolo')
    for nome, quante in sciolti.most_common():
        righe, totale = cerca_per_inglese(nome)
        if righe:
            print(f'  {nome:<22} ({quante:>3} righe)  GIA\' RESO: {righe[0][2]}'
                  f'   [{righe[0][0]}]')
        else:
            print(f'  {nome:<22} ({quante:>3} righe)  ⚠️ NON TROVATO nel dizionario')


if __name__ == '__main__':
    main()
