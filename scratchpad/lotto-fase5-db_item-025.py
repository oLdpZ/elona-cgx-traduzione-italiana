# -*- coding: utf-8 -*-
"""111a - Lotto 025 di `db_item.hsp`: LA CODA, e l'indice 3 si chiude.

`description(3)`, tutto quel che resta: **25 righe del sorgente, 23 firme**,
sparse in nove categorie minuscole piu' una voce che categoria non ha.

⚠️ **Lo scheletro non l'ha fatto `_107-chiavi-item.py`**, che seleziona per
categoria: l'ha fatto `lotti-111/_coda.py`, che prende lo scheletro intero
dell'indice 3 dallo strumento di sempre — cosi' i filtri restano gli stessi — e
tiene solo le righe che nel dizionario non hanno ancora una resa.

💡 **E la prima versione di `_coda.py` diceva «l'indice 3 e' chiuso» quando
restavano venticinque righe**, perche' cercava nel dizionario le voci con
l'italiano **vuoto**: quelle righe nel dizionario non ci sono affatto, e il
conto giusto e' il **positivo** — le righe che una resa ce l'hanno gia'. Un
elenco vuoto non e' una risposta.

### ⭐ TRE FAMIGLIE, E SI SCRIVONO IN FILA

**Le munizioni**, 「〜と共に装備する武器だ」, quattro righe in tre firme:

    銃と共に装備する武器          -> insieme a un'arma da fuoco   (:96637, :126989)
    銃と共に装備する武器（拳銃専用）-> ... (solo pistole)          (:65950)
    弓と共に装備する武器          -> insieme a un arco            (:127065)
    機械弓と共に装備する武器      -> insieme a una balestra       (:98728)

**I resti di creatura**, 「生物の〜だ」, cinque righe: osso, cuore, occhio,
sangue, pelle — i **nomi** degli oggetti, gia' resi. ⓘ `:108708` e' 体液, un
umore del corpo, e l'oggetto si chiama gia' «sangue»: si segue il nome.

**L'acqua**, tre righe che il giapponese distingue e l'inglese no:

    水を使用する設備。何度か飲むことができる。 -> che usa l'acqua, più volte
    水を湛える設備。飲むことができる。         -> che raccoglie l'acqua
    聖なる水を湛えた井戸。飲むことができる。   -> un pozzo pieno d'acqua santa

⚠️ L'inglese scrive **«(Re-drinkable) facility that supplies water»** su tutt'e
tre, gabinetto compreso. Il giapponese dice 使用する (la usa) contro 湛える (la
raccoglie) e 何度か (qualche volta) contro il bere semplice. Si segue il
giapponese, e le tre righe restano tre.

### ⭐ 飲むことができる ERA GIA' «SI PUO' BERE»

Due volte nel dizionario. 食べることができる non c'era: prende la stessa forma,
«Si può mangiare». Come 読むことができる «Si legge» della 108a.

### ⚠️⚠️ `:131247` — LA VOCE CHE NON ESISTE

`ITEM_ID_DUMMY` (il lingotto d'oro) ha il **giapponese vuoto** e l'inglese dice
letteralmente «not used in the game». Non e' un'estrazione rotta: e' cosi' nel
sorgente. Resa **«Non è usato nel gioco.»**, cioe' l'inglese, perche' li'
l'inglese e' l'unica fonte che c'e' e quel che dice e' vero.

💡 E' la stessa voce che nella 110a aveva fatto sbagliare `_coerenza.py`: il
giapponese vuoto raggruppava trenta voci che di comune avevano solo il non
avere una fonte.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :44866
    (44866, 'It is seaweed.'):
        "Un'alga. Si può mangiare.",

    # ---------------------------------------------------------- :44929
    (44929, 'It is seaweed.'):
        "Un'alga gigantesca. Si può mangiare.",

    # ---------------------------------------------------------- :44992
    (44992, 'It is seaweed.'):
        "Un'alga grande. Si può mangiare.",

    # ---------------------------------------------------------- :65950
    (65950, 'These are ammos to be equipped with guns (pistols only).'):
        "Un'arma da equipaggiare insieme a una pistola (solo pistole).",

    # ---------------------------------------------------------- :87577
    (87577, '(Re-drinkable) facility that supplies water.'):
        "Un impianto che usa l'acqua. Si può bere più volte.",

    # ---------------------------------------------------------- :90710
    (90710, '(Drinkable) well that contains holy water.'):
        "Un pozzo pieno d'acqua santa. Si può bere.",

    # ---------------------------------------------------------- :96637
    (96637, 'It is a weapon to be equipped together with a gun.'):
        "Un'arma da equipaggiare insieme a un'arma da fuoco.",

    # ---------------------------------------------------------- :97266
    (97266, 'It is a card with information about creature. You can put them in decks.'):
        "Un foglio con i dati di una creatura. Si mette nel mazzo.",

    # ---------------------------------------------------------- :97328
    (97328, 'These are statues in the shape of monsters.'):
        "Una statua che riproduce un mostro.",

    # ---------------------------------------------------------- :98728
    (98728, 'It is a weapon to be equipped together with a crossbow.'):
        "Un'arma da equipaggiare insieme a una balestra.",

    # ---------------------------------------------------------- :108522
    (108522, 'It is the bone of a creature.'):
        "L'osso di una creatura.",

    # ---------------------------------------------------------- :108584
    (108584, 'It is the heart of a creature.'):
        "Il cuore di una creatura.",

    # ---------------------------------------------------------- :108646
    (108646, 'It is the eye of a creature.'):
        "L'occhio di una creatura.",

    # ---------------------------------------------------------- :108708
    (108708, 'It is the blood of a creature.'):
        "Il sangue di una creatura.",

    # ---------------------------------------------------------- :108770
    (108770, 'It is the skin of a creature.'):
        "La pelle di una creatura.",

    # ---------------------------------------------------------- :109023
    (109023, 'It is a cargo of travel rations often used by merchants.'):
        "Un cibo del tipo che si carica sul carretto.",

    # ---------------------------------------------------------- :119822
    (119822, "It is an altar for ritual's to give tribute to the gods."):
        "Un altare semplice. Ci si possono fare offerte.",

    # ---------------------------------------------------------- :119884
    (119884, "It is a podium for ritual's to give tribute to the gods."):
        "Un piedistallo in lode del dio. Ci si possono fare offerte.",

    # ---------------------------------------------------------- :123939
    (123939, '(Re-drinkable) facility that supplies water.'):
        "Un impianto che raccoglie l'acqua. Si può bere.",

    # ---------------------------------------------------------- :127065
    (127065, 'It is a weapon to be equipped together with a bow.'):
        "Un'arma da equipaggiare insieme a un arco.",

    # ---------------------------------------------------------- :127486
    (127486, 'These are rare coins used by the guilds as currency.'):
        "Una moneta speciale e lucente. Serve a pagare l'istruttore.",

    # ---------------------------------------------------------- :127548
    (127548, 'It is the standard currency of Irva.'):
        "La moneta corrente in tutto il mondo.",

    # ---------------------------------------------------------- :131247
    (131247, 'not used in the game'):
        "Non è usato nel gioco.",

# 1131 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-025.jsonl'
RIGHE = {
    44866, 44929, 44992, 65950, 87577, 90710, 96637, 97266, 97328, 98728,
    108522, 108584, 108646, 108708, 108770, 109023, 119822, 119884, 123939, 127065,
    127486, 127548, 131247,
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
