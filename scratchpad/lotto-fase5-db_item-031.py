# -*- coding: utf-8 -*-
"""114a - Lotto 031 di `db_item.hsp`: IL MOBILIO, quinta parte.

`FILTER_FURNITURE`, righe 113.000-122.000: **36 righe** su 35 oggetti — 35
dell'indice 0 e una dell'indice 2 (`:115384`, la battuta di <Seth>). Del fronte
del mobilio restano **54 righe**, tutte sopra la riga 122.000.

### ⭐⭐⭐ CINQUE GRUPPI DICONO UNA FRASE IDENTICA, E LA RESA E' IDENTICA

Questo lotto e' il piu' ripetitivo del fronte, e la ripetizione **non e' nel
file**: sta nella stessa frase giapponese copiata in righe lontane, che nessuna
rete di lotto confronta perche' le stringhe intere sono diverse.

- **Le sette tombe** (`:119943`, `:120005`, `:120067`, `:120129`, `:120191`,
  `:120253`, `:120315`): la seconda frase e'
  当然ながら非常に重いので持ち上げてみようと思わない方がいいだろう in **tutte
  e sette**. Cambia solo la prima.
- **Il lavello e il bancone** (`:120947`, `:121011`): seconda frase identica.
- **I due mobili in vetrina** (`:121446` l'armatura, `:121508` l'abito):
  大きく試着不可と書かれている為、装備することはできない, identica.
- **Le armi e gli archi** (`:121570`, `:121632`):
  あくまでもまとめ売り用らしく、個別に売ることはしていないようだ, identica.
- **Le due colonne ornate** (`:121891`, `:121953`):
  これは古代の建築様式を復元したものであるという, identica.
- **I due mucchi di libri** (`:121260`, `:121322`): la coda
  特に読むべき情報はないだろう, identica.

⚠️⚠️ **E in tre casi su sei il genere italiano avrebbe rotto l'identita'.** Le
sette tombe non sono tutte tombe — `:120005` e' un **tumulo**, maschile — e le
armi non sono gli archi. La frase condivisa e' scritta **senza genere** apposta:
«non conviene nemmeno pensare di provare a sollevare una cosa simile», «e mai a
pezzo singolo». Scriverla al femminile avrebbe prodotto sei rese uguali e una
diversa, cioe' esattamente il difetto che il lotto 024 ha dovuto disfare.

### ⭐⭐ LA SESTA FONTE: UNA FRASE DI QUESTO LOTTO E' GIA' RESA NEL LOTTO 028

`:121136` (la libreria di pregio) e `:121198` (la cassettiera di pregio)
portano la formula
その道のプロが精魂込めて作り上げた… 一見シンプルに見えるが、普段見えない部分に匠の遊び心が隠れている,
che e' **parola per parola** quella di `:87505`, la credenza di pregio del lotto
028 — la riga a cui l'inglese aveva buttato via proprio quella seconda frase. Le
due rese nuove ricalcano quella: «costruita con tutta l'anima da chi è maestro
del mestiere» e «si nasconde l'estro dell'artigiano».

💡 `_gia-reso.py` **non** l'ha trovata, e non e' un difetto della rete: cerca la
prosa **intera**, e qui coincide solo la seconda frase su due. La rete trova le
righe gemelle, non le frasi gemelle. L'ha trovata `_cerca.py` cercando a mano
匠の遊び心.

### ⭐ I TERMINI CERCATI A MANO

    狂戦士     -> berserker        (`db_creature.hsp`; ma qui il giapponese
                                   dice 戦士 e basta: «guerriero»)
    匠の遊び心 -> l'estro dell'artigiano   (`db_item.hsp:87505`, lotto 028)
    燭台       -> candelabro       (`db_item.hsp:120698`, indice 3)
    売約済み   -> «è già venduto»  (`db_item.hsp:111697`, lotto 030)

⚠️ Il nome dell'oggetto di `:115382` e' «guerriero furioso statuetta», da
フィギア『狂戦士』 — ma la **descrizione** dice solo 戦士を模した, a immagine di
un guerriero, senza il 狂. La resa segue la descrizione, non il nome.

### ⚠️ L'inglese sbaglia poco, e in piccolo

`:115320` aggiunge una grandezza che il giapponese non ha («so large that they
could easily be mistaken»): 実際の武器と見紛う程 dice solo che si scambierebbe
per un'arma vera, non che sia grande.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :114206
    (114206, "A horn with a high-pitched sound. Basically, it can only produce a single note, but its heroic tone is sure to move people's hearts enough. \\n# ~Music of the Melodious Irva~"):
        "Un corno che manda un suono squillante. In sostanza sa fare una nota sola, ma quel timbro fiero basterà a scuotere il cuore della gente. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :115320
    (115320, 'The furnishings are so large that they could easily be mistaken for actual weapons. It was made in the image of a sword stuck in the earth, but some brave warrior may or may not have used it as a weapon in the past. \\n# ~Game Tricks, All Ages Version~'):
        "Una suppellettile che si potrebbe scambiare per un'arma vera. È fatta a immagine di una spada piantata nella terra, e si dice, ma chi lo sa, che in passato un prode l'abbia usata a forza come arma. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :115382
    (115382, "These are movable dolls that resemble elaborately crafted warriors. Although expensive, they are said to be the object of children's admiration because of their ability to respond to a variety of movements. \\n# ~Game Tricks, All Ages Version~"):
        "Un pupazzo snodabile fatto a immagine di un guerriero, lavorato con cura minuta. Costa caro, ma sa mettersi in ogni posa, e per questo, dicono, i bambini lo sognano. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :115384
    (115384, '\\"Muhahahaha! Great! Cool!\\" \\n# ~words of <Seth> the kid~'):
        "\\\"Uahahaha! Che forte! Che figo!\\\" \\n# ~Parole di <Seth>, ragazzino di città~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :118643
    (118643, "Furniture with plates of the same kind stacked on top of each other. They are useful when you have a sudden guest, but you probably shouldn't put them on the floor lest you trip over them in your haste and break them. \\n# ~Supporting Roles in Kitchen~"):
        "Un mobile con impilati piatti tutti dello stesso tipo. Comodo quando arrivano ospiti all'improvviso, ma meglio non posarlo per terra: basta inciampare nella fretta e va tutto in pezzi. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :119687
    (119687, 'Efficient bedding stacked vertically. They are often provided in inns, and when adventurers stay there, they often see fights over who gets to sleep on top. \\n#~ Great Encyclopedia of North Tyris Furnitures~'):
        "Un giaciglio efficiente, con un letto impilato sopra l'altro. Si trova spesso nelle locande, e dicono che quando ci dormono gli avventurieri capiti di vederli litigare su chi va di sopra. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :119943
    (119943, 'A tomb with a sense of history in it. Naturally it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba da cui si sente il passare della storia. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120005
    (120005, 'A huge tomb built for an ancient ruler. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Un tumulo enorme, costruito per un potente dei tempi antichi. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120067
    (120067, "The tomb is so large that you can't help but gasp and back away. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~"):
        "Una tomba davanti a cui si trattiene il fiato e si fa un passo indietro senza volerlo. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120129
    (120129, 'The tomb is so large that it could be mistaken for a magnificent stone monument. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che si potrebbe scambiare per un bel monumento di pietra. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120191
    (120191, 'A beautiful tomb covered in flowers. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una bella tomba, sepolta sotto i fiori. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120253
    (120253, 'The tomb that made one finally want a tomb for oneself. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che fa venire voglia, finalmente, di averne una propria. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120315
    (120315, 'The tomb has long since left human hands. Naturally, it is very heavy and you should not try to lift it. \\n# ~Book for the Dying Ones~'):
        "Una tomba che da parecchio nessuno cura più. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ---------------------------------------------------------- :120377
    (120377, "Woven silk antique. It is marked 'sold' in large letters and cannot be used. \\n# ~Palmian Summer Fashion~"):
        "Una pezza tessuta in seta. C'è scritto a lettere grandi che è già venduta, e perciò non si può usare. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :120439
    (120439, 'Clothes scattered on the ground. It is not certain whether they were taken off and scattered before washing or before tidying up after washing. \\n#~Thousands of pieces of Junk I love~'):
        "Vestiti sparsi per terra. Se siano stati buttati lì prima del bucato, o se il bucato sia fatto e manchi solo di piegarli, non è chiaro. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :120633
    (120633, 'For all intents and purposes, it is the shelf itself. Nothing more, nothing less. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Da qualunque parte lo si guardi, è uno scaffale e basta. Niente di più e niente di meno. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120695
    (120695, 'This is a candelabra with an emphasis on the decorative aspect. The base is also lavishly processed, it shines so brightly that candles are unnecessary. \\n# ~Daily Necessities for the Home~'):
        "Un candelabro pensato soprattutto come ornamento. Anche il piede è lavorato con un lusso senza risparmio, e risplende al punto che la candela non serve. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :120757
    (120757, "An atmospheric table that is every lady's dream. It is just a table, but it is full of elegance. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un tavolo pieno di atmosfera, il sogno delle signore. È un tavolo e nient'altro, eppure trabocca di nobiltà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120819
    (120819, 'This dining table has been miniaturized to meet the expectations of housewives. Unless you are eating a full course meal, this size is probably sufficient. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo da pranzo rimpicciolito, come le padrone di casa chiedevano. A meno di non mangiare un pranzo a tutte portate, una misura così basterà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :120883
    (120883, 'Cooking table equipped with a stove. Because two tasks can be done with a single stove, it is popular among ladies who are busy in the mornings. \\n# ~Supporting Roles in Kitchen~'):
        "Un bancone da cucina con i fornelli sopra. Un mobile solo fa due cose, e per questo va per la maggiore fra le signore che al mattino hanno fretta. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :120947
    (120947, "A sink suitable for food preparation. Some impatient people can't resist and cook their food right here. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un lavello adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121011
    (121011, "A table suitable for food preparation. Some impatient people can't resist and cook their food right here. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Un bancone adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121073
    (121073, 'So much booze that it is too much for both hands. Cannot be used because it is undrinkable. \\n# ~Gifts that I am Happy to Receive~'):
        "Tanto liquore che non sta in due mani. Non lo si finirebbe mai, e perciò non si può usare. \\n# ~Regali che Fa Piacere Ricevere~",

    # ---------------------------------------------------------- :121136
    (121136, 'A bookshelf created by professionals who put their heart and soul into their work. At first glance, it looks simple, but the playful spirit of a master craftsman is hidden in parts that are not usually seen. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una libreria costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma nelle parti che di solito non si vedono si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121198
    (121198, 'Cabinet made by craftsmen who put their hearts and souls into their work. At first glance, they may look simple, but the playful spirit of the artisan is hidden behind the scenes, hidden from view. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Una cassettiera costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma sul retro, che di solito non si vede, si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :121260
    (121260, 'These books were carefully stacked on the floor after reading. Most of the books are technical, so there will be nothing special to read. \\n# ~Daily Necessities for the Home~'):
        "Libri impilati con cura sul pavimento dopo la lettura. Sono quasi tutti libri da specialisti, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121322
    (121322, 'Books that one could not put away after reading. Mostly magazines, so there would be no special information to read. \\n# ~Daily Necessities for the Home~'):
        "Libri che dopo la lettura nessuno ha rimesso a posto. Sono quasi tutti rotocalchi, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :121384
    (121384, 'Full-body armor with a stern atmosphere. Although it looks like special equipment, it is in fact a replica and cannot be worn. \\n# ~Lumiest Art Catalogue~'):
        "Un'armatura completa che si porta addosso un'aria severa. Sembra proprio un pezzo con una storia dietro, ma in realtà è una copia e non si può indossare. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :121446
    (121446, "Armor placed for display. It is marked 'not for try-on' so you cannot equip it. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~"):
        "Un'armatura messa lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121508
    (121508, "Clothes placed for display. It is marked 'not for try-on' so you cannot equip it. \\n# ~Palmian Summer Fashion~"):
        "Un abito messo lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Palmia: Collezione Primavera-Estate~",

    # ---------------------------------------------------------- :121570
    (121570, 'Stack of weapons bundled for display. They seem to be for sale in bulk and not sold individually. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Armi e armature legate in fascio per l'esposizione. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121632
    (121632, 'Stacked bows of various sizes. They seem to be for bulk sale only and are not sold individually. \\n# ~Merchant Life Starting from a Quitting as a Adventurer~'):
        "Archi di ogni misura, impilati uno sull'altro. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :121696
    (121696, 'This is an excellent all-around cookware for baking, steaming, and stewing. It is very large and heavy, which may make people hesitate to purchase it, but it is a proven performer. \\n# ~Supporting Roles in Kitchen~'):
        "Un ottimo arnese da cucina che fa tutto: arrostisce, cuoce a vapore, lessa. È grandissimo e pesa molto, tanto che a comprarlo si esita, ma in cambio la sua bravura è garantita. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :121767
    (121767, 'A map of the entire continent. Adventurers and non-adventurers alike are encouraged to read this map and think of the lands yet to be discovered. \\n# ~an Adventurer is You! Guide for Travels~'):
        "Una mappa che disegna il continente intero. Avventurieri e non, leggendola, lasciano andare il pensiero alle terre che non hanno ancora visto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :121891
    (121891, 'Magnificent pillars with flowers decorated at the zenith. This is said to be a restoration of an ancient architectural style. \\n# ~Lumiest Art Catalogue~'):
        "Una bella colonna con dei fiori guarniti in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :121953
    (121953, 'Magnificent pillars decorated with plants at the zenith. This is said to be a restoration of an ancient architectural style. \\n# ~Lumiest Art Catalogue~'):
        "Una bella colonna con delle piante guarnite in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",

# 35 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-031.jsonl'
RIGHE = {
    114206, 115320, 115382, 115384, 118643, 119687, 119943, 120005, 120067, 120129,
    120191, 120253, 120315, 120377, 120439, 120633, 120695, 120757, 120819, 120883,
    120947, 121011, 121073, 121136, 121198, 121260, 121322, 121384, 121446, 121508,
    121570, 121632, 121696, 121767, 121891, 121953,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
