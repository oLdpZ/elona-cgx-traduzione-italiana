# -*- coding: utf-8 -*-
"""122a - Lotto 061 di `db_item.hsp`: LE MERCI DA COMMERCIO, e la categoria CHIUDE.

`FILTER_CARGO_TRADE`, righe da `:56267` a `:104375`: **19 righe**, tutte
dell'indice 0, su 19 oggetti. Con questo lotto `FILTER_CARGO_TRADE` va a **0 da
fare su 19 vive**, ed e' la **sedicesima** categoria del corpo che si chiude —
e la prima da otto lotti che non e' un pezzo d'equipaggiamento.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 061`: **+19** per 19 rese,
nessuna gemella. ⓘ `_gia-reso.py 061`: 0 su 19. `_code.py 061`: 0 righe senza
resa in tabella. `_forma.py 061`: 19 su 19 con lo spazio prima del `\\n`, 19 su
19 con lo spazio dopo il `#`.

### ⭐⭐⭐ L'INGLESE DI `:56267` E' QUELLO DELL'OGGETTO DOPO, PAROLA PER PAROLA

E' la cosa piu' riusabile del lotto, e la piu' scomoda.

    db_item.hsp:56261  (jp)  実際に噴火の現場で描かれたという…版画。  <- il dipinto
    db_item.hsp:56267  (en)  In some parts of Gaius Vis, a rabbit's foot…  <- il CONIGLIO
    db_item.hsp:56333  (en)  In some parts of Gaius Vis, a rabbit's foot…  <- il coniglio

Le due stringhe inglesi sono **identiche**, e quella giusta e' la seconda:
`ITEM_ID_PAINTING_ERUPTION` ha preso l'inglese di `ITEM_ID_RABBIT_FOOT`, che nel
sorgente e' l'oggetto **immediatamente successivo**. Il giapponese e' a posto, e
anche la `description(3)` inglese della stessa voce («It is a cargo of
painting.»): monte ha sbagliato **una riga sola**.

⭐ **LA RETE 13 DEL LOTTO L'HA VISTA**, e va detto perche' e' il suo merito:
«l'inglese "In some parts of Gaius Vis…" sta per 2 giapponesi diversi: guarda
se la distinzione va tenuta». Le due righe stanno tutt'e due in questo lotto, e
li' la rete arriva.

⚠️⚠️⚠️ **MA LA STESSA DOMANDA SU TUTTO IL FILE NON LA FA NESSUNO.** E' il
difetto della 103a e della 104a — «l'inglese di monte slitta di una carta» — e
`_103-inglese-ripetuto.py` e `_104-inglese-slittato.py` lo cercano davvero, ma
leggono **solo** `db_card.hsp`: e' scritto nella prima riga di tutt'e due
(`FILE = 'db_card.hsp'`). Su `db_item.hsp` la rete esiste **solo dentro il
lotto**: se `:56267` e `:56333` fossero caduti in due lotti diversi — e sono
due categorie vicine, non la stessa — nessuno avrebbe detto niente. E le 1.374
rese del corpo gia' scritte non sono mai state misurate contro questa domanda.
💡 Lo strumento e' la cosa da costruire subito dopo questo lotto, e il
denominatore e' **tutto il file**, non il lotto: *due `description` inglesi
identiche (o quasi) con giapponesi diversi*. E' lo stesso allargamento che la
121a chiedeva per `_120-serie-bacchette`, dall'altro lato. Se ne esistono altre,
ogni resa presa dall'inglese su quelle righe descrive **l'oggetto sbagliato**, e
nessun cancello se ne accorgerebbe — la riga e' pulita in ogni senso
misurabile, esattamente come 神の間 della 121a.

ⓘ Qui il danno non c'e' stato perche' la resa viene dal giapponese, che e' la
regola del progetto; ma la regola vale finche' qualcuno legge il giapponese, e
una riga dove il giapponese manca (il caso `:89358` della 121a) si renderebbe
dall'inglese **sbagliato** senza nessun segnale.

### ⭐⭐ LA SERIE C'E' ANCHE QUANDO GLI STRUMENTI DICONO CHE NON C'E'

`_120-serie-bacchette 061` dice «nessun giapponese ripetuto» e «0 aggettivi che
distinguono», e ha ragione su quel che misura. Ma la categoria e' **una formula
sola** ripetuta:

    undici righe su diciannove aprono con  ◯な交易品。   (una merce da commercio ◯)
    cinque di quelle undici chiudono con   使用することはできない。

Le rese tengono la stessa impalcatura — la merce apre la frase, il divieto si
rende sempre «Non si può usare: <ragione>» — perche' il giocatore che ne legge
cinque di fila deve riconoscere la regola e leggere solo la parte che cambia.
⚠️ `_120-serie-bacchette` raggruppa per **prosa intera**: una formula con dentro
un aggettivo diverso ogni volta gli e' invisibile. E' lo stesso buco della riga
sorella fuori dal lotto, dall'altro lato.

### ⭐⭐ DUE PESCI TROPPO GROSSI, E DUE GRADI DI VALORE CHE NON VANNO APPIATTITI

La coppia sorella **dentro** il lotto:

    :103913  個人で食すには余りにも巨大なツナ。主に交易品として取引される。
    :104045  個人で食すには余りにも巨大なマンボー。主に交易品として取引される。

Giapponese identico tranne il nome del pesce, e le due rese lo sono di
proposito: «Un tonno / Un pesce luna decisamente troppo grosso perché una
persona sola se lo mangi.»

⚠️ E il rovescio, che e' la lezione della 119a: due righe della famiglia del
divieto d'uso dicono due cose **diverse** e vanno tenute distinte.

    :103847 (il whisky)   開封すると価値が大幅に落ちる  ->  il valore CROLLA
    :104375 (la bambola)  開封してしまうと価値が下がる  ->  il valore CALA

### ⓘ Le decisioni minori, e da dove vengono

  - 交易品 -> «merce da commercio», glossario della 111a, e gia' in gioco
    sull'indice 3 di tutta la categoria («Merce da commercio.»);
  - la scala del peso si tiene distinta come sull'indice 3: 重い e'
    «pesante», とても重い e' «molto pesante» (`:91026`, `:103979`, `:104243`);
  - 版画 e' la **stampa**, non il dipinto, e il progetto la rende gia' cosi'
    nel quadro di Ehekatl, in questo stesso file. Il NOME dell'oggetto resta
    «dipinto dell'eruzione»: la descrizione non lo contraddice, lo specifica;
  - i nomi di luogo vengono tutti dal dizionario: ガイアス・ヴィス «Gaius Vis»,
    サウスティリス «Tyris del Sud», イェルス軍 «l'esercito di Yerles»,
    ノイエル «Noyel», エウダーナ «Eulderna», イムウエル «Aimwell»;
  - マンボー «pesce luna» e 浮き輪 «salvagente» sono gia' nel dizionario come
    nomi di oggetto: la descrizione usa la parola che il giocatore legge
    nell'inventario;
  - `:103979` (la tomba) ripete la parola «tomba» come fa il giapponese —
    墓運びが墓に埋もれる — perche' la battuta sta nella ripetizione;
  - `:104111` (la bara) tiene la battuta nera di 先約がいる: «c'è già chi
    l'ha prenotata».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56267
    (56267, "In some parts of Gaius Vis, a rabbit's foot, not its tail, is a lucky charm. It has been handed down since ancient times and is a popular travel companion among adventurers. \\n# ~the Aimwell tale of trade~"):
        "Una stampa che dicono disegnata sul posto, durante l'eruzione: un pezzo leggendario, ma in un altro senso. Da quella scena, che pare la fine del mondo, arrivano un calore soffocante e tutto il suo furore. \\n# ~Racconti di Commercio di Aimwell~",

    # ---------------------------------------------------------- :56333
    (56333, "In some parts of Gaius Vis, a rabbit's foot, not its tail, is a lucky charm. It has been handed down since ancient times and is a popular travel companion among adventurers. \\n# ~the Aimwell tale of trade~"):
        "In certe zone di Gaius Vis il portafortuna è la zampa del coniglio, non la coda. Si tramanda da tempi antichi, e fra gli avventurieri va per la maggiore come compagna di viaggio. \\n# ~Racconti di Commercio di Aimwell~",

    # ---------------------------------------------------------- :73894
    (73894, "Marimo that grows in a lake in South Tyris, is ripped off and artificially rounded up. The lake's marimo is in danger of extinction due to the mass harvesting. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Marimo che cresce nel lago di Tyris del Sud, strappato e poi arrotondato a mano. Per fabbricarlo se ne raccoglie tanto che il marimo del lago rischia l'estinzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :73960
    (73960, "Old military ration that was dispensed to the civilian by the Yerles Army as an ornamental item. Long since ruined as food. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una vecchia razione militare che l'esercito di Yerles ha ceduto ai civili come soprammobile. Come cibo è andata a male da un pezzo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :86266
    (86266, "Trade goods filled with a set of painting tools. It cannot be used because paints and other materials will be scattered around when the package is opened. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio con dentro tutto l'occorrente per dipingere. Non si può usare: ad aprirla, i colori e il resto finiscono sparsi dappertutto. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :86332
    (86332, "The trade goods are a collection of paintings by various artists. Even so, they are kept in a minimum amount of storage, so there seems to be no trouble such as opening them at a trading partner and finding that they are worthless. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio che mette insieme alla rinfusa quadri di artisti diversi. Detto questo, il minimo della conservazione c'è, e non risulta che qualcuno l'abbia aperta davanti al compratore trovandoci dentro roba senza alcun valore. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :90960
    (90960, "Cute trading goods made of snow. Many of them feel comforted by their bland expressions and purchase them. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una graziosa merce da commercio fatta di neve. Quell'aria svagata consola, e pare che in molti la comprino per questo. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :91026
    (91026, "Very heavy traded goods made of felled fir trees decorated with many ornaments. It is said that people who cannot travel to Noyel buy it to celebrate at home. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio molto pesante: un abete abbattuto e carico di addobbi. La comprano, dicono, quelli che a Noyel non ci possono arrivare e vogliono festeggiare a casa loro. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103715
    (103715, "A trade item consisting of several bundles of lifebuoy. They cannot be sold separately because they are difficult to sell. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio fatta di salvagenti legati in più mazzi. Sciolti diventano difficili da smerciare, e infatti non si vendono a uno a uno. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103781
    (103781, "An intricately crafted trading item that is a joy to behold. It is heavy and should be handled with care. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio con dentro un congegno complicato, che diverte chi la guarda. È pesante, e a maneggiarla ci vuole attenzione. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103847
    (103847, "A trading item that is nice to receive. It cannot be used because its value drops dramatically once it is opened. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio che fa piacere ricevere. Non si può usare: ad aprirla, il valore crolla. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103913
    (103913, "Tuna is too huge to be eaten by individuals. It is mainly traded as a commodity. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Un tonno decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :103979
    (103979, "Very heavy trading goods made of stone. Do not be reckless and let the grave carrier be buried in the grave. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio di pietra, molto pesante. Meglio non strafare: non sia mai che chi porta la tomba finisca sepolto sotto la tomba. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104045
    (104045, "Mamboos that are too huge to be eaten by individuals. It is mainly traded as a commodity. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Un pesce luna decisamente troppo grosso perché una persona sola se lo mangi. Si tratta soprattutto come merce da commercio. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104111
    (104111, "A carefully crafted trade item made of high quality wood. It is not available for use because of prior commitments. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio fatta con cura, in legno di qualità. Non si può usare: c'è già chi l'ha prenotata. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104177
    (104177, "Tightly bound trade goods. You cannot use it because it would be very troublesome if it gets loose. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio legata stretta. Non si può usare: se si scioglie, sono guai. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104243
    (104243, "A brightly colored, very heavy trade item. Although it produces sound, it cannot be used properly because it was only made for ornamental purposes. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio dai colori vivaci, molto pesante. Il suono lo fa, ma in fondo è roba costruita per far scena, e a usarla sul serio non si va da nessuna parte. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104309
    (104309, "The trade goods are so polished that they mirror each other. Each one is handmade to a luxurious specification. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio lucidata al punto che ci si vede dentro. Ogni pezzo è fatto a mano, in versione di lusso. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

    # ---------------------------------------------------------- :104375
    (104375, "Carefully wrapped trade goods. Once opened, it cannot be used because its value will decrease. \\n# ~Eulderna's Winning Strategy for Trading~"):
        "Una merce da commercio impacchettata con cura. Non si può usare: ad aprirla, il valore cala. \\n# ~Il Commercio Vincente Secondo gli Eulderna~",

# 19 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-061.jsonl'
RIGHE = {
    56267, 56333, 73894, 73960, 86266, 86332, 90960, 91026, 103715, 103781,
    103847, 103913, 103979, 104045, 104111, 104177, 104243, 104309, 104375,
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
