# -*- coding: utf-8 -*-
"""Lotto `command-025`: **identificare, scambiare, consegnare**.
Dodici rese e una rinviata, la seconda fetta della zona 15000-15999.

⭐⭐ **Un letterale inglese nudo attaccato in coda a una `lang()`, e nessuno dei
cinque punti ciechi lo vede.** `:15489` e'

    txt lang(itemname(ci) + "を納入した", "You deliver " + itemname(ci) + ". ")
        + "(" + (inv(INV_ITEM_PARAM1, ci) + 5) * inv(INV_ITEM_NUM, ci) + " Guild Point)"

cioe' la `lang()` finisce, e **fuori** dalla parentesi c'e' « Guild Point)» in
inglese, sempre, in tutt'e due le lingue. La resa italiana non lo puo'
raggiungere: e' fuori dal perimetro della voce. ⚠️ E i referti non lo prendono
per un motivo preciso ciascuno — `blocchi_en.py` cerca `if ( en )`, `else_jp.py`
cerca il ramo `else`, `variabili_en.py` cerca l'**assegnamento** di una
variabile, e qui non c'e' ne' un ramo ne' una variabile: c'e' una concatenazione.
✅ Sta a `toppe.jsonl`, e la voce e' **rinviata**: vedi
`scratchpad/toppa-command-15489.py`.
💡 **E il termine era gia' deciso**: `:14115` e' `lang("ギルドポイント", "Guild Point")`
resa «Punti gilda» in un lotto passato. Lo stesso testo, quaranta righe piu' su,
dentro una `lang()` vera. La differenza non e' il testo: e' dove sta.

⚠️⚠️ **E la prima toppa che ho scritto era della specie sbagliata, per una
ragione che vale per tutte.** `applica.py` fa girare le toppe **dopo** il
dizionario (`applica.py:530`), quindi agganciare `cerca` alla riga gia' tradotta
funziona in build — e infatti funzionava. Ma `strumenti/tests/test_toppe.py:104`
pretende che **ogni toppa si applichi al SORGENTE pinnato**, ed e' quella prova a
diventare rossa il giorno in cui upstream riscrive la riga: una toppa agganciata
al testo italiano non ha piu' nessun rapporto col sorgente, e quella prova non
varrebbe piu' niente. Ha parlato la catena, non io.
✅ La forma giusta e' **rinvio + toppa insieme**, gia' in tabella in `LEGGIMI.md`
(`toppa-action-15221.py`, `toppa-proc-24107.py`, `toppa-chara_func-3037.py`).
💡 **La regola generale, che nessuno aveva ancora scritta**: una toppa e una resa
non possono stare sulla stessa riga. O la riga la sistema il dizionario, o la
sistema la toppa — e chi sceglie la toppa deve rinviare la voce.

⚠️ **«Quota» qui non e' una quantita', e' l'incarico della gilda.** L'inglese
usa la stessa parola per la riga di stato (`:15499`, «Quota (40.0s)») e per il
messaggio di compimento (`:15493`, «You fulfill the quota!»), e il progetto l'ha
gia' resa **«Obiettivo»** tre volte — `chara_func.hsp:7247`, `proc.hsp:241` e
`command.hsp:13895` («Al momento non hai nessun obiettivo per la Gilda dei
Maghi»). Si riscuote, non si ridecide.

💡 **Le due righe dell'identificazione prendono la stessa forma, e non per
simmetria estetica.** L'inglese dice «The item is half-identified as X» e «is
fully identified as X»: un participio, che in italiano si accorderebbe col
genere dell'oggetto — e `itemname()` restituisce tanto «la spada» quanto «lo
scudo». ✅ Il nome astratto toglie l'accordo di mezzo: «È X: identificazione
incompleta.» e «È X: identificazione completa.» Stessa manovra del lotto 024,
applicata a una cosa invece che a una persona.

⚠️ **`:15309` e `:15312` nominano gli spazi dell'equipaggiamento, e i nomi
esistono**: `text.hsp:136` fissa 「遠隔」/`Shoot` = «Tiro» e 「手」/`Hand` = «Mano».
Sono le etichette che il giocatore ha davanti mentre legge la domanda, quindi la
resa le scrive maiuscole come le legge sullo schermo, non come parole comuni.

⭐ Copiate senza decidere: «identificazione superiore» (`db_item.hsp:147871`),
«Punti gilda» (`command.hsp:14115`, che serve alla toppa e non alla resa), e
«Obiettivo » per `Quota ` (`chara_func.hsp:7247`, `proc.hsp:241`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :15309-:15312 l'oggetto che sta in due spazi. I nomi degli spazi sono
    #     quelli di text.hsp:136 — «Tiro» e «Mano» — e vanno maiuscoli perché
    #     sono le etichette che il giocatore ha davanti.
    (15309, 'Although this is a ranged equipment it can be equipped in your hands. Which will you choose?'):
        'È equipaggiamento da Tiro, ma si può portare anche in Mano. Quale scegli?',
    (15312, 'Although this is a short distance equipment it can be equipped as ranged. Which will you choose?'):
        'È equipaggiamento da Mano, ma si può portare anche nel Tiro. Quale scegli?',
    # 「何番目の手？」: le creature con più di due mani
    (15332, 'Which hand?'): 'Quale mano?',

    # --- :15364 l'alleato che non prende l'oggetto.
    #     `_s(tc)` è morfologia inglese e sparisce; restano name e itemname.
    (15364, ' refuse to take .'):
        'name(tc) + " non accetta " + itemname(ci, 1) + "."',

    # --- :15372-:15379 l'identificazione.
    (15372, 'You need higher identification to gain new knowledge.'):
        "Non hai scoperto niente di nuovo: serve un'identificazione superiore.",
    # ⚠️ «identificato» accorderebbe col genere dell'oggetto: il nome astratto
    #    toglie l'accordo di mezzo, ed è la stessa manovra del lotto 024.
    (15376, 'The item is half-identified as .'):
        '"È " + itemname(ci, 1) + ": identificazione incompleta."',
    (15379, 'The item is fully identified as .'):
        '"È " + itemname(ci, 1) + ": identificazione completa."',

    # --- :15444 lo scambio. Due itemname, e la rete 11 guarda l'insieme.
    (15444, 'You receive  in exchange for .'):
        '"Hai scambiato " + itemname(ci) + " con " + itemname(citrade) + "."',

    # --- :15489 è RINVIATA: fuori dalla lang() il sorgente attacca
    #     « Guild Point)», che il dizionario non raggiunge. La riga la riscrive
    #     tutta la toppa. Vedi il docstring e scratchpad/toppa-command-15489.py.

    # ⭐ «quota» è l'incarico della gilda, e il progetto lo chiama «obiettivo»
    #    da chara_func.hsp:7247, proc.hsp:241 e command.hsp:13895.
    (15493, 'You fulfill the quota!'): 'Obiettivo raggiunto!',

    # --- :15499 la consegna della missione di raccolta, con la riga di stato.
    (15499, 'You deliver .'):
        '"Hai consegnato " + itemname(ci) + "."',
    # gli spazi sono quel che stacca l'etichetta dai due conti fra parentesi
    (15499, ' Delivered '): ' Consegnato ',
    (15499, 'Quota '): 'Obiettivo ',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(15489, 'You deliver . ')}

USCITA = 'lavoro/fase4-command-025.jsonl'
DA, A = 15301, 15500
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
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
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
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
