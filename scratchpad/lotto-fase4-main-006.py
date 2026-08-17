# -*- coding: utf-8 -*-
"""Lotto fase4-main-006: gli altri due finali e la morte del giocatore
(main.hsp, righe 4128-4409).

Ventun rese: la vittoria su Tyris del Sud (le Rovine di Remido) e quella sul
Sigillo Eterno, poi tutto il rito della morte — le ultime parole, la lapide, il
menu che decide se si ricomincia.

⚠️⚠️⚠️ **Questo lotto ha corretto la RETE 4, ed e' la QUINTA rete che si
corregge** dopo la 8, la 4 (una prima volta), la 9 e la 6. `:4151` e `:4232`
hanno **lo stesso giapponese** — 「あなたは「」とコメントした。」, «hai commentato
"X"» — e lo stesso `cnvtalk`, ma l'inglese di monte ci mette il nome del boss:
«Upon killing Meshera Alpha» e «Upon killing Enthumesis». Sono i due finali, e
le rese devono differire. La rete raggruppava per `(giapponese, funzioni)` e
bocciava il lotto.

La chiave le mancava per una ragione storica: la 37ª le aveva insegnato che la
**rete 11** pretende le funzioni dell'inglese, quindi due giapponesi uguali con
un numero diverso di `name()` non possono coincidere. Ma upstream distingue
anche con le **parole**, e quelle non erano nella chiave.
✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`, in
`scratchpad/modello-rete4.py`.

⭐⭐ **E la correzione e' stata misurata prima di usarla**, con
`scratchpad/misura-rete4.py`, che passa la rete 4 all'indietro su tutto il
dizionario — come `rete8_dizionario.py` fa con la rete 8. Su **11.982 gruppi**,
467 sono resi in piu' di un modo:

    con inglese diverso   458   <- la rete vecchia li bocciava a torto
    con lo stesso inglese   9   <- la famiglia per cui la rete e' nata

La rete nuova prende ancora tutti e nove, e i due Yerleswood del lotto 039 —
stesso giapponese **e** stesso inglese — restano bocciati. Non perde niente.
⚠️ E i nove sono un referto da leggere: uno e' un difetto vero, «Tiro oltre il
limite» (`buff.hsp:263`) contro «Lancio oltre il limite» (`skill.hsp:1240`), che
sono la **stessa mossa** vista dal potenziamento e dall'elenco.

⚠️ **`:4282` e' la prima chiave lunga di `main.hsp`.** Le due `lang()` sulla riga
sono `lang("「", "\\"")` e `lang("」", "\\"")` — le virgolette che aprono e chiudono
le ultime parole — e hanno **lo stesso inglese**, quindi la chiave corta
`(riga, en)` ne identifica due. Si danno con `(riga, en, jp)`, come la 41ª ha
insegnato su `init.hsp:2225`. Tutt'e due restano `\\"`: e' punteggiatura, ed e'
gia' dichiarata in `invariati.md` per `proc.hsp:3376`.

⭐ **`:4296` non usa nessuna preposizione, e non e' pignoleria.** L'inglese e'
`cnven(ndeathcause) + " in " + mdatan(MDATAN_NAME) + "."`, ma i nomi di mappa
italiani non stanno tutti dietro la stessa preposizione: «a Vernis» ma «nelle
Rovine di Remido», «al Sigillo Eterno» ma «in Prigione». La riga e' la **seconda
del referto della lapide** (`noteadd s, 2`), cioe' una voce di registro, e si
scrive come tale: «Prigione - Morì di fame.» ⚠️ `ndeathcause` arriva gia' reso da
`chara_func.hsp:6850`-`:7039` come un verbo alla **terza persona del passato
remoto senza soggetto** («morì di fame», «si impiccò», «perse la vita contro il
putit»), e `cnven` gli alza la prima lettera: la resa deve incastrarcisi, non
riscriverlo.

⚠️ **Le quattro voci del menu della morte sono `promptAdd` con
`val = promptx, 100, 400, 1`**, cioe' **400 px = (400 − 46) / 7,7 = 45
caratteri**. La piu' lunga, «Ricarica l'ultimo salvataggio», ne fa 28.
⚠️⚠️ **Ma nessuna rete lo misura**: `larghezze.py` guarda i menu di `*prompt_key`
**solo in `text.hsp`** (`FILE = "text.hsp"` a `larghezze.py`). I `promptAdd` di
`main.hsp`, `command.hsp` e degli altri file sono fuori da ogni referto — e' un
punto cieco di geometria, misurato qui a mano.
💡 Le quattro rese sono tutte all'imperativo — «Rialzati», «Lasciati
seppellire» — anche perche' e' l'unica forma che non porta genere: «Resta
disteso» sarebbe stato un aggettivo riferito al giocatore.

⭐ **I nomi propri erano gia' decisi:** 「災厄」 e' **«la calamità»**
(`text.hsp:9692` «Parte seconda - L'ombra della calamità», `db_card.hsp:9227`
«il semenzaio della calamità»), 「混沌の神」 e' **«il dio del caos»**
(`text.hsp:9852`), il Sigillo Eterno e le Rovine di Remido vengono dal lotto 005.

💡 **`:4293` tiene l'ordine anno/mese/giorno dell'inglese**, che non e' quello
italiano, perche' e' l'ordine con cui `init.hsp:2225` compone **tutte** le date
del gioco — e li' il dizionario non puo' cambiarlo, perche' l'ordine sta nel
codice e non nelle `lang()`. Due formati di data nello stesso gioco sarebbero
peggio di uno straniero. La voce va quindi in `invariati.md` con l'espressione
intera, come la 56ª ha imparato su `Karma()`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4128-:4151 il finale di Tyris del Sud. 「災厄」 e' «la calamità»
    # (text.hsp:9692, db_card.hsp:9227).
    (4128, "Blessing to , ! You've finally destroyed the source of disaster!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente distrutto la radice della calamità!"',
    (4150, 'In the year , /, you conquered Remido.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista delle Rovine di Remido."',
    # ⚠️ Stesso giapponese di :4232 e di :4071: a distinguerli e' il nome del
    # boss, che ce l'ha solo l'inglese. Vedi la correzione della rete 4.
    (4151, 'Upon killing Meshera Alpha, you said, '):
        '"Uccidendo Meshera Alpha hai detto: " + cnvtalk("" + wincomment)',

    # --- :4186-:4232 il finale del Sigillo Eterno. 「混沌の神」 e' «il dio del
    # caos» (text.hsp:9852).
    (4186, 'Unbelievable! You conquered the Eternal Seal!'):
        'Incredibile! Hai conquistato il Sigillo Eterno!',
    (4209, "Blessing to , ! You've finally beat the god of chaos!"):
        '"Benedizione a te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", " '
        '+ cdatan(CDATAN_AKA, CHARA_PLAYER) '
        '+ "! Hai finalmente abbattuto il dio del caos!"',
    (4231, 'In the year , /, you conquered the Eternal Seal.'):
        '"Anno " + gdata(GDATA_YEAR) + ", " + gdata(GDATA_DAY) + "/" '
        '+ gdata(GDATA_MONTH) + ": conquista del Sigillo Eterno."',
    (4232, 'Upon killing Enthumesis, you said, '):
        '"Uccidendo Enthumesis hai detto: " + cnvtalk("" + wincomment)',

    # --- :4272-:4274 le ultime parole. Lo spazio finale di :4272 c'e' anche
    # nell'inglese e serve a chi concatena.
    (4272, 'Good bye... '):
        'Addio... ',
    (4274, 'You leave a dying message.'):
        'Lasci un ultimo messaggio.',

    # --- :4282 ⚠️ CHIAVE LUNGA: due `lang()` sulla riga con lo stesso inglese.
    # Sono le virgolette che aprono e chiudono, non testo: gia' in invariati.md.
    (4282, '\\"', '「'):
        '\\"',
    (4282, '\\"', '」'):
        '\\"',

    # --- :4291-:4296 la lapide, tre righe di `noteadd`.
    (4291, ' '):
        ' ',
    # ⚠️ Ordine anno/mese/giorno come l'inglese: e' quello con cui init.hsp:2225
    # compone tutte le date del gioco, e li' il dizionario non puo' cambiarlo.
    (4293, '//'):
        '"" + gdata(GDATA_YEAR) + "/" + gdata(GDATA_MONTH) + "/" + gdata(GDATA_DAY)',
    # ⚠️ Nessuna preposizione davanti a mdatan: «a Vernis» ma «in Prigione».
    # `ndeathcause` arriva gia' reso come verbo al passato remoto senza soggetto.
    (4296, ' in .'):
        'mdatan(MDATAN_NAME) + " - " + cnven(ndeathcause) + "."',

    # --- :4349-:4353 la sepoltura.
    (4349, 'You are about to be buried...'):
        'Stanno per seppellirti...',
    (4353, 'You have been buried. Bye...(Hit any key to exit)'):
        'Sei sottoterra. Addio... (premi un tasto per uscire)',

    # --- :4361-:4371 il menu della morte. `val = promptx, 100, 400, 1`, cioe'
    # 400 px = 45 caratteri; la piu' lunga ne fa 28. Tutte all'imperativo, che
    # e' anche l'unica forma senza genere.
    (4361, 'Reload last save'):
        "Ricarica l'ultimo salvataggio",
    (4365, 'Crawl up'):
        'Rialzati',
    (4368, 'Crawl up from hell'):
        "Rialzati dall'inferno",
    (4371, 'Lie on your back'):
        'Lasciati seppellire',

    # --- :4409 la riga che va al tabellone in rete. Stessa forma della lapide.
    (4409, '   in  '):
        'cdatan(CDATAN_AKA, CHARA_PLAYER) + " " '
        '+ cdatan(CDATAN_NAME, CHARA_PLAYER) + " " + ndeathcause + " - " '
        '+ mdatan(MDATAN_NAME) + " " + lastword',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-main-006.jsonl'
DA, A = 4111, 4420
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\main.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_main.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

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

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
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
