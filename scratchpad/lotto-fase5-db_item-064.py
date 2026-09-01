# -*- coding: utf-8 -*-
"""122a - Lotto 064 di `db_item.hsp`: LE COLLANE, e la categoria CHIUDE.

`FILTER_ACCESSORY_AMULET`, righe da `:62463` a `:126647`: **14 righe** — 13
dell'indice 0 e **una dell'indice 2** (`:99809`, la battuta di <Rianna>) — su 13
oggetti. Con questo lotto `FILTER_ACCESSORY_AMULET` va a **0 da fare su 14
vive**, ed e' la **diciannovesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 064`: **+14** per 14 rese,
nessuna gemella. ⓘ `_gia-reso.py 064`: 0 su 14. `_code.py 064`: 0 righe senza
resa in tabella. `_forma.py 064`: 14 su 14 con lo spazio prima del `\\n`.

### ⭐⭐⭐ L'INGLESE FONDE DUE POPOLI IN UNO, E IL TERZO NON C'ENTRA NIENTE

`:62463`, la sfera di Yekub. Il giapponese nomina **due** specie aliene:

    シャンの催眠術        l'ipnosi degli Shan
    サキュバロリンの思念吸収  l'assorbimento del pensiero dei Sakyubalorin

L'inglese scrive «Sunbararian's hypnotism and mind absorption»: **un popolo
solo**, e per giunta un **terzo** — gli abitanti di Sunbararia, quelli del lotto
063, che nella riga giapponese non compaiono affatto.

⚠️ **I due nomi giapponesi stanno in TUTTO il sorgente solo qui.** Cercati:
due occorrenze, che sono le due lingue di questa stessa riga. Quindi non sono
nomi di creature che il giocatore incontra, e il lettore giapponese e' opaco
esattamente quanto quello italiano — il che rende la trascrizione la scelta
giusta, non un ripiego. ⓘ Non e' un errore di monte come `:56267`: e' una
**semplificazione** dell'intermedio, la stessa forma di 神の間 della 121a.

### ⭐⭐ UNA PAROLA NUOVA, E IL DIZIONARIO NE AVEVA UNA SOLA

Il glossario ha 首輪 -> «collana», e l'indice 3 di questa categoria lo ripete su
tredici oggetti. Ma il **corpo** usa 装身具 — l'ornamento che si porta addosso —
e in `:99519` le due parole diverse stanno nella stessa frase:

    表面を磨き上げた**装身具**。どちらかといえば**宝飾品**というべきもの…

Le rese tengono tre parole distinte: 首輪 «collana», 装身具 «ornamento»,
宝飾品 «gioiello». ⓘ 装身具 non era nel dizionario da nessuna parte —
`_cerca.py` dice «niente» — ed e' una parola nuova di questo lotto.
⚠️ **E in `:76247` 首輪 non e' una collana ma un collare**, perche' l'oggetto si
chiama 《暴風の首輪》 -> «Collare della Tempesta» ed e' quello che il giocatore
legge in cima al pannello. La parola segue il nome, non il glossario.

### ⭐ LA TERZA RIGA DELLA FAMIGLIA 〜を守る為に作られた

    :99937 (063)  頭部を守る為に作られた防具    Un'armatura fatta per proteggere la testa.
    :99663 (064)  首を守る為に作られた装身具    Un ornamento fatto per proteggere il collo.

Trovata con `_cerca.py` **prima** di scrivere, come le due famiglie del lotto
063. E' la terza sessione di fila in cui la ricerca a mano trova quel che
nessuno strumento cerca: la richiesta della 121a — la riga sorella **per
frase** su tutto `db_item.hsp` — resta la cosa piu' utile da costruire.

### ⓘ Le decisioni minori, e da dove vengono

  - 風の神 «la dea del vento», gia' in gioco sull'arco lungo che quella dea
    dona; 御利益 e' il beneficio che viene dal divino, non un effetto qualunque;
  - ミカ (`:81536`) e' la **mica**, il minerale che si sfoglia: da li' viene la
    spirale della conchiglia. L'inglese la tiene, ed e' giusta;
  - 装着する / 装備する (`:99663`) sono due verbi che il gioco distingue
    davvero — indossare ed equipaggiare — e la riga ci gioca sopra;
  - 〜のこめられた -> «racchiuso», che e' la parola dei due indici 3 gia' in
    gioco («Una collana in cui è racchiuso un sentimento», «…il potere magico»);
  - le due collane del combattimento (`:82676`, `:82742`) si leggono in coppia,
    e i loro indici 3 dicono gia' «un attacco extra in mischia» e «…a
    distanza»: le rese ci vanno d'accordo senza ripetere le stesse parole;
  - 下賤な者達 (`:83901`) e' la gente di bassa condizione, e 札 la targhetta:
    la riga dice che il ciondolo e' un **segno di riconoscimento**, non un
    ornamento — ed e' il contrario di quel che sembra.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62463
    (62463, "A crystal sphere in the image of the supreme deity of the planet Yekub, and has the power to strengthen one's spirit. It is a popular souvenir among some aliens, who say that wearing it enables one to resist Sunbararian's hypnotism and mind absorption. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una sfera di cristallo fatta a immagine del dio supremo del pianeta Yekub, e porta in dono un rafforzamento dello spirito. A portarla addosso si resiste anche all'ipnosi degli Shan e all'assorbimento del pensiero dei Sakyubalorin: così dicono certi alieni, fra i quali è un souvenir molto apprezzato. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76247
    (76247, 'Special collar that the Goddess of the wind puts on her prized pets. It has an invisible chain. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un collare speciale che la dea del vento mette al suo animale prediletto. Ci sta attaccata una catena che non si vede. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81536
    (81536, 'A shell-shaped ornament made of mica with beautiful spirals. It is said to have been left behind by the gods. It is said that if you hold it gently to your ear, you can hear someone talking. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un ornamento a forma di conchiglia, fatto di mica, con una spirale bellissima. Chi l'abbia fatto non si sa affatto, e c'è chi dice che sia roba caduta agli dei. Pare che accostandolo piano all'orecchio si senta qualcuno che parla. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82676
    (82676, 'Necklace that looks like a pair of tiny swords. When worn, it is said to give the wearer the ability to move quickly, as if he or she had two extra arms. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una collana che pare fatta di due piccole spade gemelle. Dicono che a portarla si acquisti un movimento svelto, come se le braccia fossero diventate due di più. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82742
    (82742, 'Purple necklace that looks like a broken crossbow. It is said that when you wear it, covering fire will come out of nowhere. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una collana viola che pare una balestra spezzata. Dicono che a portarla addosso, da chissà dove, arrivi un tiro di copertura. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :83901
    (83901, 'Shabby necklace made of iron. It looks more like some kind of tag than an ornament, but it is said that this is because it is a symbol for lower class people to distinguish between friend and foe. \\n# ~Intel of the Informant Wiesem~'):
        "Una collana misera, fatta di ferro. Più che un ornamento sembra una targhetta, e si dice sia perché alla gente di bassa condizione serve da segno per distinguere gli amici dai nemici. \\n# ~Le Notizie Raccolte da <Wiesem> l'informatore~",

    # ---------------------------------------------------------- :99448
    (99448, 'Amulet of love is given to the bride-to-be at the wedding ceremony. Naturally, this amulet is considered the property of the spouse, and forcible attempts to take it away from him or her will incur his or her wrath. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una collana carica d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento la collana appartiene a lui, e a strappargliela per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99519
    (99519, 'An ornament with a polished surface. It is more of a jewelry item and is often used as a gift. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento con la superficie lucidata a specchio. A dirla tutta è più un gioiello che altro, e spesso si usa per farne dono. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99591
    (99591, 'Small ornaments are meant to ward off evil spirits. The ornaments are said to carry a variety of feelings. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un piccolo ornamento che vale soprattutto come scongiuro contro il male. Dicono che in quei fregi siano racchiusi i sentimenti più vari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99663
    (99663, 'Armor made to protect the neck. It is more like a piece of armor than something to be worn. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento fatto per proteggere il collo. Più che indossarlo si direbbe che lo si equipaggia, ed è di fattura piuttosto rozza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99735
    (99735, 'Accessories with special magic inside. It is not expected to provide direct protection, but it is said to often contain special abilities. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento in cui è racchiusa una magia particolare. Una protezione diretta non c'è da aspettarsela, ma spesso, dicono, nasconde dentro qualche facoltà fuori dal comune. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99807
    (99807, 'An ornament with a bright green gemstone at its center. Cut into a distinctive oval shape, it glows even at night and is considered by some to be a symbol of exceptional vitality. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento con al centro una gemma di un verde acceso. Tagliata in quella caratteristica forma d'uovo, brilla anche di notte, e c'è chi la dice simbolo di una forza vitale senza pari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99809
    (99809, '\\"Well, what a lovely shape. It\'s round and green with a hint of red in it, perfect for him, who is like a transparent canvas. I bet when he sees this necklace...oh no!\\" \\n# ~Rianna the Daydreamer~'):
        "\\\"Oh, ma che forma graziosa. Tonda, verde, e dentro un rosso appena accennato: perfetta per lui, che è tutto una tela trasparente. Se quella persona vedesse questa collana, di sicuro... ohhh, che vergogna!\\\" \\n# ~Parole di <Rianna> la sognatrice~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :126647
    (126647, 'Ornaments worn around the neck. They can be made of a variety of materials and shapes, but those made of rare materials are often the most expensive. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un ornamento da portare intorno al collo. Ce n'è di ogni materiale e di ogni forma, e spesso i più cari sono quelli fatti con materiali rari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 13 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-064.jsonl'
RIGHE = {
    62463, 76247, 81536, 82676, 82742, 83901, 99448, 99519, 99591, 99663,
    99735, 99807, 99809, 126647,
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
