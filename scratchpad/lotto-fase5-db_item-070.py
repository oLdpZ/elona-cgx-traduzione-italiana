# -*- coding: utf-8 -*-
"""123a - Lotto 070 di `db_item.hsp`: I RESTI, e la categoria CHIUDE.

`FILTER_REMAINS`, righe da `:97263` a `:108767`: **7 righe**, tutte dell'indice
0, su 7 oggetti. Con questo lotto `FILTER_REMAINS` va a **0 da fare su 7 vive**,
ed e' la **venticinquesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 070`: **+7** per 7 rese,
nessuna gemella. ⓘ `_code.py 070`: 0 righe senza resa in tabella.
`_119-togli-rinviate 070`: nessuna rinviata. `_gia-reso 070`: 0 su 7.
`_120-serie-bacchette 070`: nessuna riga col giapponese identico.

### ⭐⭐⭐ IL CASO PIU' FORTE DELL'INGLESE CHE APPIATTISCE

E' quello che la 122a aveva visto e lasciato in eredita', ed e' l'ottavo posto
dove guardare (119a: la riga gemella per costruzione) nella sua forma piu'
netta. Cinque righe in fila, cinque volte la stessa frase inglese:

    «It is not particularly valuable, but can be used for medicine and
     sorcery, so it can be sold for a modest price.»

Il giapponese dice **quattro cose diverse**, con **due verbi diversi**:

    :108519  骨片  osso    水薬や呪術に**使用**できる     pozioni, stregoneria
    :108581  心臓  cuore   水薬や呪術に**使用**できる     pozioni, stregoneria
    :108643  瞳    occhio  装飾品や薬に**加工**できる     ornamenti, medicine
    :108705  体液  sangue  水薬等に**加工**できる         pozioni e simili
    :108767  皮    pelle   服や鞄に**加工**できる         vestiti, borse

⭐ **使用 contro 加工.** 使用できる e' «si usa»: la cosa entra intera in un
procedimento. 加工できる e' «si lavora»: la cosa e' materia prima che diventa
altro. Il giapponese sceglie, e sceglie «usare» due volte e «lavorare» tre.
L'inglese scrive «be used» cinque volte su cinque, e per tre righe su cinque
dice il verbo sbagliato.

⚠️ **Sono quattro frasi su cinque righe, non cinque.** Osso e cuore hanno il
giapponese **identico** in quella frase, e le due rese lo tengono identico. Chi
avesse letto «cinque usi diversi» e cercato cinque rese diverse avrebbe
introdotto una divergenza che il giapponese non ha.

### ⭐⭐ LE SORELLE GIA' RESE STANNO FUORI DAL LOTTO, SOTTO LO STESSO TITOLO

`_122-sorelle-per-frase 070` dice **32 frasi con una sorella, 0 gia' rese**:
tutte e trentadue stanno dentro il lotto, ed e' la famiglia piu' chiusa vista
finora. Ma le parole che servivano stavano gia' nel dizionario, in tre righe che
la rete **non** poteva accostare perche' la frase e' diversa — e che portano lo
stesso titolo, `#~Le Mille Cianfrusaglie che Amo~`:

    :116408  ITEM_ID_ANIMAL_BONE    風化した動物の骨。呪術や水薬精製など…
    :127669  ITEM_ID_SKELETON       風化した人間の骨。呪術や水薬精製など…
    :127731  ITEM_ID_BONE_FRAGMENT  風化した何かの骨。呪術や水薬精製など…

    IT  «…dalla stregoneria al distillare pozioni…»

Da li' si ricopiano le due parole: 呪術 -> **stregoneria**, 水薬 -> **pozioni**.
⭐ E' il settimo posto (113a: il giapponese di cio' che stai per scrivere puo'
essere gia' reso altrove) trovato **per titolo** invece che per frase: le tre
ossa sbiancate dal tempo sono lo stesso libro immaginario, e chi lo scrive usa
le sue parole.
⚠️ 薬 nudo (l'occhio) NON e' 水薬: resta «medicine», non «pozioni». Il
giapponese ha due parole e il dizionario le tiene due — `potion` -> pozione sta
nel glossario.

### ⭐⭐ LA TESTA E LA CODA SI TENGONO IDENTICHE, IN FORMA IMPERSONALE

Quattro righe su cinque aprono con 敵を破砕した際に飛び散った生物の…, che non
ha soggetto. In italiano i soggetti sarebbero quattro e diversi — «schegge»,
«il cuore», «l'occhio», «lembi di pelle» — e la frase condivisa si sarebbe
spezzata in quattro. 💡 **«schizzat* via nel frantumare un nemico»**: il
gerundio regge tutti e quattro senza cambiare una lettera oltre l'accordo.
E' lo stesso rimedio del 069, dove la coppia 靴/履物 aveva costretto a
«c'è poco da fidarsi».

Lo stesso vale per la coda, condivisa da tutte e cinque: «Gran valore non ne
ha/hanno, ma … e così si vende/vendono a un prezzo discreto».

⚠️ **Il rovescio, e c'e' anche qui.** `:108705` NON dice 敵を破砕した際に: dice
飛び散った生物の体液を集めたもの — il sangue si **raccoglie** invece di
schizzare via, e l'inglese ci mette pure «scattered» al posto di «shattered».
La resa lo segue e non uniforma: «schizzato via e raccolto».

### ⓘ IL NOME CHE IL GIOCATORE LEGGE IN CIMA AL PANNELLO VINCE

体液 e' «fluido corporeo», ma il NOME dell'oggetto nel dizionario e' **sangue**,
e l'indice 3 dice gia' «Il sangue di una creatura». La resa dice sangue.
E' la regola del 069 (gli stivali contro le scarpe), applicata al contrario:
li' il nome era piu' specifico del giapponese, qui e' meno.

⚠️ **Ma non vale meccanicamente.** `:97325` ha il nome «statuetta» (はく製,
tassidermia) e il giapponese del corpo dice 像, «statua»: li' la resa segue il
**giapponese della riga**, perche' il giapponese ha cambiato parola apposta.
Il nome vince quando la riga usa la stessa parola del nome, non quando ne usa
un'altra.

### ⚠️⚠️ IL PREFLIGHT HA PRESO UN GUASTO CHE `_forma.py` NON VEDE

`_forma.py 070` dice «7 righe su 7 con lo spazio prima del `\\n`»: e' un SI/NO.
L'inglese di `:97263` ne ha **due**, di spazi, e la prima stesura ne aveva messo
uno. Il preflight lo ha stampato — «en '  ', it ' '» — e il lotto e' ripartito
da li'.

⭐ **Un referto booleano non dice il margine.** E' la stessa lezione della 107a
sulla prova al contrario che stampa il punto in cui si accende invece di un ✅,
e qui il margine era **un byte**. `_forma.py` non e' sbagliato: risponde a
un'altra domanda, e la sua risposta verde non copre quella del preflight.

### ⓘ E DUE PEZZI DA COLLEZIONE, CHE NON C'ENTRANO CON I RESTI

`FILTER_REMAINS` tiene dentro anche la carta (`:97263`) e la statuetta
(`:97325`), che stanno sotto `# ~Catalogo d'Arte di Lumiest~` e sono gli unici
due del lotto con lo spazio dopo il `#`.

- 紙片 e' «foglietto» e non «foglio»: l'indice 3 della stessa voce dice 紙 nudo,
  ed e' li' che sta «Un foglio con i dati di una creatura». Due parole in
  giapponese, due in italiano, dentro lo stesso pannello.
- 遊戯用 e' il gioco di carte — デッキ e' gia' «mazzo» nel dizionario, ventitre
  voci — quindi «da gioco», non «da giocattolo».
- 生き写し e' il modo di dire italiano «il ritratto vivente», che si dice
  esattamente cosi'. ⚠️ 犠牲者 e' singolare in giapponese e l'inglese lo mette
  al plurale insieme al soggetto: vince il giapponese, una statua una vittima.

### ▶ Il conto

Il corpo passa da **1.485 a 1.492 rese su 1.513**, e restano **21 righe** — di
cui una rinviata (`:129299`). Dopo il 070 mancano **sette** categorie:

    6  FILTER_ENVIRONMENT_SEABED     2  FILTER_FURNITURE_ALTAR
    5  FILTER_AMMO                   1  FILTER_PLATINUM
    4  FILTER_FURNITURE_WELL         1  FILTER_GOLD
                                     1  FILTER_CARGO_FOOD

⚠️ La tabella si rilegge con `_114-corpo-da-fare`, non si eredita da qui.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :97263
    (97263, 'A piece of paper on which information is clearly described. It contains detailed descriptions of height and weight as well as characteristics, but it is rarely used for collecting such information and is said to be used exclusively for collecting and playing with, helped by its shiny material.  \\n# ~Lumiest Art Catalogue~'):
        "Un foglietto su cui le informazioni sono descritte per filo e per segno: altezza e peso, s'intende, ma anche i tratti particolari, scritti nei minimi dettagli. Eppure per raccogliere informazioni non si usa quasi mai; complice il materiale lucido, pare che serva soltanto da collezione e da gioco.  \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :97325
    (97325, 'The statues are so elaborately crafted that they seem to be living replicas of their victims. The figure is so lifelike that it looks as if it could start moving at any moment. \\n# ~Lumiest Art Catalogue~'):
        "Una statua fatta con tale finezza da sembrare il ritratto vivente della vittima. La figura è così piena di vita che pare stia per muoversi da un momento all'altro. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :108519
    (108519, 'Bone fragments of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Schegge d'osso di una creatura, schizzate via nel frantumare un nemico. Gran valore non ne hanno, ma si usano per le pozioni e per la stregoneria, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108581
    (108581, 'Heart of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Il cuore di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si usa per le pozioni e per la stregoneria, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108643
    (108643, 'Eyes of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "L'occhio di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si lavora in ornamenti e in medicine, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108705
    (108705, 'Collected body fluids of scattered creatures. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Il sangue di una creatura, schizzato via e raccolto. Gran valore non ne ha, ma si lavora in pozioni e simili, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :108767
    (108767, 'Skin patches of a shattered creature. It is not particularly valuable, but can be used for medicine and sorcery, so it can be sold for a modest price. \\n#~Thousands of pieces of Junk I love~'):
        "Lembi di pelle di una creatura, schizzati via nel frantumare un nemico. Gran valore non ne hanno, ma si lavorano in vestiti e in borse, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

# 7 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-070.jsonl'
RIGHE = {
    97263, 97325, 108519, 108581, 108643, 108705, 108767,
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
