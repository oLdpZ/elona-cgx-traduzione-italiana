# -*- coding: utf-8 -*-
"""119a - Lotto 052 di `db_item.hsp`: LE PERGAMENE, e la categoria CHIUDE.

`FILTER_ITEM_SCROLL`, righe da `:102250` a `:130314`: **23 righe**, tutte
dell'indice 0. Con questo lotto `FILTER_ITEM_SCROLL` va a **0 da fare su 73
vive**, ed e' l'**ottava** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`: **+23** per 23 rese, nessuna gemella.

### ⭐⭐ UNA COPPIA DOVE IL GIAPPONESE SI RIMANGIA LA PROMESSA E L'INGLESE NO

`:106981` e `:117256` sono la pergamena di purificazione superiore e quella
normale, la stessa frase con la coda opposta:

    :117256  呪いが強力すぎる場合解呪に失敗する      a volte fallisce
    :106981  失敗することはない、**はずだ**          non fallisce mai... **dovrebbe**

L'ultima parola del giapponese, はずだ, si rimangia la promessa che la frase ha
appena fatto: e' la battuta della riga. L'inglese scrive «never fails to break
the curse» e la toglie. La resa la tiene, e sta in una parola: «non fallisce
mai. Dovrebbe.»

### ⭐ IL GIAPPONESE CHIAMA SE STESSO «TERRA STRANIERA»

`:115001`, la pergamena di acquisizione: 「遠く、異国の地ではこれらの巻物のこと
を**ヒデンショ**と読んでいた」 — *in terre lontane e straniere queste pergamene
le chiamavano hidensho*. ヒデンショ e' 秘伝書, «libro dei segreti», scritto in
**katakana**, cioe' col vestito che il giapponese mette alle parole straniere:
la battuta e' che il paese straniero, visto da Irva, e' il Giappone.

L'inglese traduce («Master Recipe Tomes») e la battuta muore. La resa la tiene
traslitterata, per la regola della 111a — un termine coniato che l'inglese
traslittera resta traslitterato — applicata qui al **giapponese** che si
traslittera da solo.

### ⚠️ QUANDO UN TERMINE DEL PROGETTO NON CI STA A SCHERMO

Cinque righe di questo lotto parlano di 装備品, che il progetto rende
«equipaggiamento». Con la preposizione articolata sono **19-20 caratteri**, ben
oltre la finestra di rinculo di 15: l'impaginatore le avrebbe spezzate a meta'.

Rese **«un oggetto indossato»**, che e' la forma che il rapporto di
identificazione di queste stesse pergamene usa gia' («Toglie la maledizione a un
oggetto»). ⓘ Non e' una deroga al glossario: e' la stessa cosa detta con le
parole che il pannello lascia dire.

⭐ Nel lotto **051** la stessa parola si e' spezzata **una volta su due**:
`:81740` si', `:95990` no. Conta **dove cade il taglio**, non la lunghezza — la
lezione della 113a — e a dirlo e' solo `_107-descrizioni-item --peggiori`, che
stampa la riga. Il preflight da' l'indizio; il referto da' il nome.

### ⓘ I termini che il lotto porta, gia' decisi altrove

    マテリアル -> **materiale** (glossario, 111a)
    ネフィア   -> **Nefia**
    ホーリーヴェイル -> **velo sacro**, come il grimorio `:105525` del 048
    ＭＰ, マナ -> **MP**, **mana** (invariati)

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code sono **due**: `~Compendio Completo degli Oggetti Magici~` per 22 righe e
`~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~` per `:108327`. Il cancello
«titoli resi in PIU' modi» resta a **7**.

⚠️ La forma: **tutte e 23** le righe hanno lo spazio prima del `\\n`, e una sola
coda porta lo spazio dopo il `#`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :102250
    (102250, "A scroll that allows people to deepen their faith by conversing with God. It's probably more like a letter to God than a scroll. \\n#~Arcane Alamanac~"):
        "Una pergamena che permette di approfondire la fede parlando col proprio dio. Più che una pergamena sarà una specie di lettera indirizzata a lui. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :102321
    (102321, 'These precious scrolls are enchanted to develop your body. Reading it will make you even stronger. \\n#~Arcane Alamanac~'):
        "Una pergamena preziosa, su cui è posata una magia che fa crescere il corpo. A leggerla diventerai più tenace. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :103576
    (103576, 'Scrolls that allow the user to detect the location of objects. It can detect objects behind walls, or even invisible objects, so it should be readied when searching for something. \\n#~Arcane Alamanac~'):
        "Una pergamena che fa avvertire dove c'è qualcosa. Sente anche al di là di un muro, dove non si sa cosa ci sia, e perfino gli oggetti invisibili: conviene tenerne pronta una quando si esplora. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104446
    (104446, 'A scroll that makes you smarter temporarily. It is said that during the examination season, the tool shops are temporarily crowded with customers who rely on these scrolls without studying as far as they are concerned. \\n#~Arcane Alamanac~'):
        "Una pergamena che rende svegli per un po'. Si dice che nella stagione degli esami le botteghe si riempiano per un momento di clienti che, invece di studiare, contano su questa. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104663
    (104663, 'Strange scrolls that, when read, cause materials to fall from the sky. It is still unclear why materials fall from the sky when the scroll is read. \\n#~Arcane Alamanac~'):
        "Una strana pergamena che, a leggerla, fa cadere dei materiali dal cielo. Perché a leggere una pergamena piovano materiali, questo legame non si è ancora capito. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105013
    (105013, 'A scroll that, when read, instantly fills the body with mana. They say that having a scroll with you in an emergency is more useful than you think. \\n#~Arcane Alamanac~'):
        "Una pergamena che, letta, riempie di mana il corpo in un istante. Pare che averne una addosso nei momenti critici serva più di quanto si creda. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105084
    (105084, 'A scroll that cancels all curses on the body. It does not cancel curses on equipment. \\n#~Arcane Alamanac~'):
        "Una pergamena che annulla tutte le maledizioni che si hanno addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105155
    (105155, 'A scroll that cancels 1 curses on the body. It does not cancel curses on equipment. \\n#~Arcane Alamanac~'):
        "Una pergamena che annulla una maledizione che si ha addosso. Quelle su un oggetto indossato no: là, chissà perché, non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105452
    (105452, 'It is a scroll that temporarily deploys a sacred robe that is said to protect the body from curses. \\n#~Arcane Alamanac~'):
        "Una pergamena che stende per un po' un velo sacro, che si dice protegga dalle maledizioni che piombano addosso. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :106981
    (106981, 'Scrolls that break the curse of worn equipment. It is more powerful and thus never fails to break the curse. \\n#~Arcane Alamanac~'):
        "Una pergamena che toglie la maledizione a un oggetto indossato. Essendo più forte, la purificazione non fallisce mai. Dovrebbe. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :107052
    (107052, 'A scroll that appraises unappraised items. It is more powerful, but if the item still cannot be appraised, have it investigated by a mage instead. \\n#~Arcane Alamanac~'):
        "Una pergamena che identifica gli oggetti non identificati. È più forte del solito, ma se anche così l'oggetto non si lascia identificare, tanto vale farlo esaminare da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :108327
    (108327, 'A deed gives the right to a house. Even adventurers cannot always camp out in the wilderness. \\n# ~an Adventurer is You! Guide for Travels~'):
        "L'atto che serve come pratica per comprare una casa. Anche a essere avventurieri, non si può dormire sempre all'addiaccio. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ---------------------------------------------------------- :111921
    (111921, 'Dangerous scrolls that cast a curse on worn equipment. In some rare cases when it is used, it may not work and turn to dust, probably as a result of daily conduct. \\n#~Arcane Alamanac~'):
        "Una pergamena pericolosa, che getta una maledizione su un oggetto indossato. Certe rare volte, quando la si usa, non fa effetto e si sbriciola: sarà il frutto della condotta di tutti i giorni. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :114859
    (114859, 'A scroll that creates a small distortion in space, allowing a person to travel instantaneously. Because its potency is rather weak, there are some funny stories about people who used it when they were leaving someone, only to have it reappear nearby, causing them to feel awkward. \\n#~Arcane Alamanac~'):
        "Una pergamena che, creando una piccola piega nello spazio, sposta in un istante. Ha un effetto piuttosto debole, e si racconta per ridere di gente che l'ha usata per accomiatarsi da qualcuno e si è ritrovata a ricomparirgli accanto, con tutto l'imbarazzo del caso. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :114930
    (114930, 'Scrolls of magical knowledge. One theory is that they are fragments of pages that fell out of a book in which the gods had written down their magic so that they would not forget it. \\n#~Arcane Alamanac~'):
        "Una pergamena che fa affiorare di colpo nella testa una conoscenza magica. Secondo una teoria sono pezzi di pagina caduti dal libro in cui gli dei avevano messo per iscritto la propria magia, per non dimenticarla. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115001
    (115001, 'Precious scrolls that are said to give new abilities when read. In distant, far away foreign lands, these scrolls were called Master Recipe Tomes. \\n#~Arcane Alamanac~'):
        "Una pergamena preziosa, che a leggerla darebbe una capacità nuova. Si dice che in terre lontane e straniere queste pergamene le chiamassero hidensho. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115072
    (115072, "A scroll that instantly reads the surrounding terrain. This scroll is mainly for Nefia, so you can't use it to break into the house of that girl you're interested in. \\n#~Arcane Alamanac~"):
        "Una pergamena che legge in un istante il terreno intorno. Serve soprattutto dentro Nefia, quindi la trovata poco pulita di intrufolarsi in casa della ragazza che ti piace per usarla lì non funziona. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :115453
    (115453, 'A scroll that invokes a gate leading to the specified location. If used by mistake, it can be undone by reading it again. Naturally, two copies are consumed, but consider it a tuition fee. \\n#~Arcane Alamanac~'):
        "Una pergamena che chiama un portale collegato a un luogo preciso. Anche se la si usa per sbaglio, niente panico: rileggendola si annulla. Ovviamente se ne consumano due, ma pazienza: consideralo il prezzo della lezione. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117256
    (117256, 'Scrolls that break the curse of worn equipment. It sometimes fails on strong curses. \\n#~Arcane Alamanac~'):
        "Una pergamena che toglie la maledizione a un oggetto indossato. Se la maledizione è troppo forte la purificazione fallisce, e allora conviene pensare a un'altra strada. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130101
    (130101, 'A scroll that allows you to impersonate someone else in an instant. When you use it, you feel like a great thief who steals the country. \\n#~Arcane Alamanac~'):
        "Una pergamena che in un istante permette di farsi passare per un altro. Usandola ci si sente il grande ladro che tiene in scacco un regno. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130172
    (130172, 'A scroll that creates a distortion in space, allowing you to travel elsewhere instantaneously. It is useful in emergencies, but the destination cannot be specified, so it cannot be used if you are late for a meeting, for example. \\n#~Arcane Alamanac~'):
        "Una pergamena che, creando una piega nello spazio, porta in un istante da un'altra parte. Nei momenti critici è comoda, ma la meta non si può scegliere: per quando si è in ritardo a un appuntamento, non serve. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130243
    (130243, "The scrolls are supposed to tell you about the existence of legendary items. It doesn't even tell you who has it, God is not that friendly to you. \\n#~Arcane Alamanac~"):
        "Una pergamena che, si dice, faccia sapere dell'esistenza degli oggetti leggendari. Chi ce li abbia non lo dice: il dio non ti è amico fino a quel punto. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130314
    (130314, 'A scroll that appraises unappraised items. It is useless agains powerful items, you will need a mage instead. \\n#~Arcane Alamanac~'):
        "Una pergamena che identifica gli oggetti non identificati. Con gli oggetti potenti certe volte non ce la fa, e in quei casi conviene farsi dare una mano da un mago. \\n#~Compendio Completo degli Oggetti Magici~",

# 23 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-052.jsonl'
RIGHE = {
    102250, 102321, 103576, 104446, 104663, 105013, 105084, 105155, 105452, 106981,
    107052, 108327, 111921, 114859, 114930, 115001, 115072, 115453, 117256, 130101,
    130172, 130243, 130314,
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
