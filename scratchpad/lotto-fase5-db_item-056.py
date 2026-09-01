# -*- coding: utf-8 -*-
"""120a - Lotto 056 di `db_item.hsp`: LE BACCHETTE, e la categoria CHIUDE.

`FILTER_ITEM_ROD`, righe da `:61946` a `:130030`: **32 righe**, tutte
dell'indice 0, su 32 oggetti — la categoria intera in un lotto solo. Con questo
lotto `FILTER_ITEM_ROD` va a **0 da fare su 32 vive**, ed e' l'**undicesima**
categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 056`: **+32** per 32 rese,
nessuna gemella. ⓘ `_gia-reso.py 056`: 0 su 32. `_code.py 056`: 0 righe senza
resa in tabella, e tutte e 32 le code sono «~Compendio Completo degli Oggetti
Magici~».

### ⭐⭐⭐ E' UNA SERIE DI TRENTADUE, E STAVOLTA L'HO MISURATA INVECE DI GUARDARLA

Tutte e 32 le bacchette aprono con la stessa frase e poi descrivono **la
gemma** (o l'incisione, dove gemma non c'e'). Vederlo dal dossier e' facile;
rispondere alle tre domande che contano, no, perche' il dossier mostra una voce
per volta. Le ha risposte `scratchpad/_120-serie-bacchette.py`, scritto qui:

  - **31 righe su 32 aprono IDENTICHE**, 特定の魔法が封じ込められた杖。 Le 31
    rese italiane ripetono la stessa frase parola per parola, per la ragione
    della serie delle tre armi: la ripetizione **e' il testo**;
  - ⭐⭐ **una sola diverge, ed e' `:111777`** — la bacchetta dei **desideri**,
    la piu' rara del gioco. Il giapponese dice 貴重な杖, «una bacchetta
    **preziosa**», e **l'inglese lo lascia cadere**: «Rods encasing specific
    magic, a cat-eye-shaped gem is attached to it», identico agli altri
    trentuno. Chi rendesse dall'inglese scriverebbe trentadue righe uguali
    dove il giapponese ne ha trentuno piu' una;
  - ⚠️⚠️ **`:71856` e `:106766` hanno il giapponese IDENTICO** — l'eclissi e il
    silenzio, tutt'e due 黒く濁った宝石 — e due inglesi che differiscono per una
    **virgola** («a black and murky gem» / «a black, murky gem»). Le due rese
    devono essere identiche: altrimenti sarebbero due rese diverse per lo
    stesso originale, che e' il difetto che `battute --divergenti` misura. Nel
    file delle rese le due voci puntano a **una costante sola**, cosi' non
    possono divergere per distrazione.

⭐ **Perche' uno strumento e non l'occhio.** Il gradino di `:111777` sta in due
caratteri dentro una formula ripetuta trentadue volte: e' esattamente il tipo
di differenza che l'occhio salta, perche' l'occhio sta leggendo la parte che
cambia (la gemma) e da' per identica quella che si ripete. Il conto lo trova in
un secondo. ⚠️ E la coppia col giapponese identico non si vede affatto
leggendo: le due righe stanno a trentacinquemila righe di distanza, in due
punti diversi del dossier.

ⓘ E' la stessa lezione della scala delle navi (119a) e della serie delle tre
armi (120a), ma il metodo e' salito di un gradino: **la` la struttura si
cercava a mano, qui si conta**. La domanda «questa riga ha delle sorelle, e che
cosa cambia fra loro?» ha smesso di dipendere da quanto sto attento.

### ⓘ Due scelte di resa che il giapponese detta

  - `:96275`, la bacchetta dell'alchimia: il giapponese dice
    自分の尾を咥えた竜 — «un drago che si tiene in bocca la propria coda» — e
    **non lo nomina**; l'inglese scrive «a Uroboros». La resa **descrive**,
    come l'originale: chi non conosce l'uroboro se lo vede lo stesso, e chi lo
    conosce lo riconosce. Nominarlo sarebbe spiegare una figura che
    l'originale sceglie di mostrare;
  - `:93149`, la bacchetta del suolo acido, e' **l'unica delle 32 senza gemma**,
    e il giapponese lo dice esplicitamente (宝石が付いておらず, «di gemme non ne
    ha») prima di descrivere l'asta. La resa apre allo stesso modo, con la
    negazione: e' il secondo gradino della serie, dopo quello di `:111777`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61946
    (61946, 'Rods encasing specific magic, an ephemeral, yet fragile looking gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma fragile, che pare stia per rompersi da un momento all'altro.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :62314
    (62314, 'Rods encasing specific magic, an translucent, shining gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma traslucida che brilla.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :62394
    (62394, 'Rods encasing specific magic, a poison-tainted gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma di un colore che sa di veleno.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :70751
    (70751, 'Rods encasing specific magic, a shiny, glittering gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che manda scintille crepitando.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :71856
    (71856, 'Rods encasing specific magic, a black and murky gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma nera e torbida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :92062
    (92062, 'Rods encasing specific magic, an opaque white spherical gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e opaca, a forma di sfera.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :92797
    (92797, 'Rods encasing specific magic, an transparent gem, with a hint of red taint, is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, con dentro mescolato del rosso.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :93149
    (93149, 'Rods encasing specific magic, not jeweled, just a long, thin rod with a pointed end. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Di gemme non ne ha, e pare un'asta lunga e sottile con la punta aguzza. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94102
    (94102, 'Rods encasing specific magic, carved with a pattern resembling intertwined ivy. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di edera intrecciata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94534
    (94534, 'Rods encasing specific magic, mineralized shiny gemstones are attached to it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che luccica come un minerale. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96275
    (96275, 'Rods encasing specific magic, a Uroboros is carved on it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un drago che si tiene in bocca la propria coda.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96355
    (96355, 'Rods encasing specific magic, sacred geometric patterns are carved into it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci stanno incisi sopra motivi di geometria sacra. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :98576
    (98576, 'Rods encasing specific magic, not jeweled, latticed pattern is engraved on it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Sull'asta è intagliato un motivo a graticcio. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :98954
    (98954, "Rods encasing specific magic, a huge purple gem like a creature's eye is attached to it.\\n# ~Arcane Almanac~"):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma viola enorme, come l'occhio di un essere vivo.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :103505
    (103505, 'Rods encasing specific magic, carved with fine letter-like patterns.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di caratteri minuti.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104942
    (104942, 'Rods encasing specific magic, an octahedron shaped crimson gemstone is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rosso sangue, tagliata a otto facce. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105381
    (105381, 'Rods encasing specific magic, a cold blue gemstone is mounted on it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra che dà una sensazione di freddo. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105966
    (105966, 'Rods encasing specific magic, an opaque, blue gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :106766
    (106766, 'Rods encasing specific magic, a black, murky gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma nera e torbida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :111777
    (111777, 'Rods encasing specific magic, a cat-eye-shaped gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta preziosa, in cui è chiusa una magia precisa. Ci sta montata sopra una gemma come un occhio di gatto.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117679
    (117679, 'Rods encasing specific magic, three small red jewels are attached.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci stanno montate sopra tre piccole gemme rosse.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117759
    (117759, 'Rods encasing specific magic, carved with spiral-like patterns.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo a spirale.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :119541
    (119541, 'Rods encasing specific magic, an opaque, red gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :119621
    (119621, 'Rods encasing specific magic, an translucent, yellow gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma gialla e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :122821
    (122821, 'Rods encasing specific magic, carved with intertwined serpent-like patterns. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di serpenti intrecciati. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :122964
    (122964, 'Rods encasing specific magic, an translucent, red gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123044
    (123044, 'Rods encasing specific magic, an translucent, blue gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123124
    (123124, 'Rods encasing specific magic, a sphere made from some kind of bone is attached to it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una sfera ricavata dall'osso di qualcosa. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123204
    (123204, 'Rods encasing specific magic, an translucent, white gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123284
    (123284, 'Rods encasing specific magic, spherical small red gemstone is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una piccola gemma rossa a forma di sfera. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :129950
    (129950, 'Rods encasing specific magic, a green gemstone with clear quadrangulars is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma verde e trasparente, squadrata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130030
    (130030, 'Rods encasing specific magic, a crystal clear gemstone is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, che pare veda attraverso ogni cosa.\\n# ~Compendio Completo degli Oggetti Magici~",

# 32 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-056.jsonl'
RIGHE = {
    61946, 62314, 62394, 70751, 71856, 92062, 92797, 93149, 94102, 94534,
    96275, 96355, 98576, 98954, 103505, 104942, 105381, 105966, 106766, 111777,
    117679, 117759, 119541, 119621, 122821, 122964, 123044, 123124, 123204, 123284,
    129950, 130030,
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
