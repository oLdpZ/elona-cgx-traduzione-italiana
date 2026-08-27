# -*- coding: utf-8 -*-
"""110a - Lotto 009 di `db_item.hsp`: il rapporto delle BACCHETTE.

`FILTER_ITEM_ROD`, `description(3)`: **32 righe del sorgente, 30 firme**. E' la
categoria piu' formulaica di tutto l'indice 3: **trenta righe su trenta** aprono
con 「振ることで」 e chiudono con 「魔法の杖だ。」. Quel che cambia sta in mezzo.

    振ることで〜魔法の杖だ。 -> Una bacchetta che, agitata, ...

### ⭐⭐ IL VERBO NON E' STATO SCELTO: ERA GIA' A SCHERMO

「を振った。」 sta nel dizionario da una sessione precedente come
«"Hai agitato " + itemname(ci, 1) + "."» — e' il messaggio che il giocatore
legge **ogni volta** che usa una bacchetta. Il rapporto d'identificazione e il
messaggio dell'azione adesso dicono la stessa parola, e la riga della scheda
spiega il tasto che si preme.

⚠️ Vale la stessa lezione del lotto 007 («模造品» era gia' «riproduzione») e
del lotto 008 (le due code dei libri): la parte cara del lavoro non e' scegliere,
e' **ricordarsi di guardare se qualcuno ha gia' scelto**.

### ⭐ E I NOMI DELLE MAGIE ERANO GIA' GIUSTI

`skill.hsp` dice «Saetta», e la 90a aveva corretto i quindici nomi di
`db_item.hsp` che dicevano «dardo». Il controllo qui e' **positivo**: i nomi
degli oggetti di questa stessa categoria dicono gia' «saetta di fulmine», «saetta
di fuoco», «saetta di gelo» — e i tre giapponesi che li accompagnano sono
電撃属性のボルト, 火炎属性のボルト, 冷気属性のボルト. La resa del rapporto usa
gli stessi tre nomi, cioe' la scheda chiama la magia come la chiama l'oggetto.
⭐ `:123207` fa eccezione ed e' giusto cosi': il giapponese dice 矢 (*freccia*),
non ボルト, e l'oggetto si chiama «dardo magico».

### ⚠️ DUE RIGHE CHE DIFFERISCONO PER LA LARGHEZZA DI DUE CARATTERI

`:94105` e `:122824` hanno l'**inglese identico** («heal wounds of nearby
target») e due giapponesi che si distinguono per **`HP` a mezza larghezza contro
`ＨＰ` a larghezza piena**. Non sono due frasi: e' la stessa frase scritta due
volte da due mani. Stessa resa.

ⓘ Se un giorno una rete cerca i giapponesi «quasi uguali», questo e' il caso di
prova: nessuna delle due reti d'apertura sull'inglese lo vede, perche' li'
l'inglese e' identico e non e' un difetto.

### ⓘ La struttura del lotto, in quattro famiglie

    attacchi ad area (4)     : PV/DV, veleno, fulmine, oscurita'
    saette e dardi (5)       : arcana, fulmine, fuoco, gelo, dardo magico
    cio' che si crea (6)     : porte, muri di fiamme, pozza d'acido, muri
                               magici, ragnatela, mostri ostili
    su di te o sui vicini (6): cura x2, MP, maledizioni levate, maledizioni
                               respinte, accelerazione

più quattro sul bersaglio e cinque solitari.

### ⓘ I termini, verificati nel dizionario

振る → «agitare» (`を振った。` -> «Hai agitato ...») · ボルト → «saetta»
(`skill.hsp`, `glossario.md`) · 沈黙 → «silenzio» · 加速 → «Accelerazione» ·
鈍足 → «Rallentamento» · 呪い → «maledizione» · 蜘蛛の巣 → «ragnatela» ·
鑑定 → «identificare» · テレポート → «teletrasporto» · `HP`, `MP`, `PV`, `DV`
invariati (il giapponese scrive le stesse sigle).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61949
    (61949, 'It is a rod that, when zapped, unleash an area-of-effect physical attack.'):
        "Una bacchetta che, agitata, fa un attacco ad area di tipo PV/DV.",

    # ---------------------------------------------------------- :62317
    (62317, 'It is a rod that, when zapped, unleashes a beam of magical torrent.'):
        "Una bacchetta che, agitata, tira una saetta arcana.",

    # ---------------------------------------------------------- :62397
    (62397, 'It is a rod that, when zapped, unleashes an area-of-effect poison attack.'):
        "Una bacchetta che, agitata, fa un attacco ad area di veleno.",

    # ---------------------------------------------------------- :70754
    (70754, 'It is a rod that, when zapped, unleash an area-of-effect electric shock.'):
        "Una bacchetta che, agitata, fa un attacco ad area di fulmine.",

    # ---------------------------------------------------------- :71859
    (71859, 'It is a rod that, when zapped, unleashes an area-of-effect dark pulse.'):
        "Una bacchetta che, agitata, fa un attacco ad area d'oscurità.",

    # ---------------------------------------------------------- :92065
    (92065, 'It is a rod that, when zapped, manifests doorways on nearby walls.'):
        "Una bacchetta che, agitata, apre porte nei muri vicini.",

    # ---------------------------------------------------------- :92800
    (92800, 'It is a rod that, when zapped, creates walls of flame at target location.'):
        "Una bacchetta che, agitata, alza muri di fiamme dove vuoi.",

    # ---------------------------------------------------------- :93152
    (93152, 'It is a rod that, when zapped, creates pools of acid at target location.'):
        "Una bacchetta che, agitata, crea una pozza d'acido dove vuoi.",

    # ---------------------------------------------------------- :94105
    (94105, 'It is a rod that, when zapped, heal wounds of nearby target.'):
        "Una bacchetta che, agitata, cura te o chi ti sta accanto.",

    # ---------------------------------------------------------- :94537
    (94537, 'It is a rod that, when zapped, creates magical walls at target location.'):
        "Una bacchetta che, agitata, alza muri magici dove vuoi.",

    # ---------------------------------------------------------- :96278
    (96278, 'It is a rod that, when zapped, reconstruct targeted items.'):
        "Una bacchetta che, agitata, ricostruisce l'oggetto scelto.",

    # ---------------------------------------------------------- :96358
    (96358, 'It is a rod that, when zapped, forcifully transforms target creature.'):
        "Una bacchetta che, agitata, ricostruisce il bersaglio.",

    # ---------------------------------------------------------- :98579
    (98579, 'It is a rod that, when zapped, creates spider webs at target location.'):
        "Una bacchetta che, agitata, tende una ragnatela sul bersaglio.",

    # ---------------------------------------------------------- :98957
    (98957, 'It is a rod that, when zapped, dominates target creature.'):
        "Una bacchetta che, agitata, ti sottomette il bersaglio.",

    # ---------------------------------------------------------- :103508
    (103508, 'It is a rod that, when zapped, uncurses nearby equipped items.'):
        "Una bacchetta che, agitata, purifica gli oggetti qui intorno.",

    # ---------------------------------------------------------- :104945
    (104945, 'It is a rod that, when zapped, restores your mana.'):
        "Una bacchetta che, agitata, ti recupera gli MP.",

    # ---------------------------------------------------------- :105384
    (105384, 'It is a rod that, when zapped, protects nearby target from curses.'):
        "Una bacchetta che, agitata, para le maledizioni a te e ai vicini.",

    # ---------------------------------------------------------- :105969
    (105969, 'It is a rod that, when zapped, puts nearby target in accelerated status.'):
        "Una bacchetta che, agitata, accelera te o chi ti sta accanto.",

    # ---------------------------------------------------------- :106769
    (106769, 'It is a rod that, when zapped, silences the target.'):
        "Una bacchetta che, agitata, mette il bersaglio in silenzio.",

    # ---------------------------------------------------------- :111780
    (111780, 'It is a rod that, when zapped, grants audience to the wish goddess.'):
        "Una bacchetta che, agitata, dà modo di esprimere un desiderio.",

    # ---------------------------------------------------------- :117762
    (117762, 'It is a rod that, when zapped, scan and maps undiscovered areas.'):
        "Una bacchetta che, agitata, rivela le zone non esplorate.",

    # ---------------------------------------------------------- :119544
    (119544, 'It is a rod that, when zapped, puts a nearby target in slow motion.'):
        "Una bacchetta che, agitata, rallenta il bersaglio.",

    # ---------------------------------------------------------- :119624
    (119624, 'It is a rod that, when zapped, unleashes a beam of electric torrent.'):
        "Una bacchetta che, agitata, tira una saetta di fulmine.",

    # ---------------------------------------------------------- :122824
    (122824, 'It is a rod that, when zapped, heal wounds of nearby target.'):
        "Una bacchetta che, agitata, cura te o chi ti sta accanto.",

    # ---------------------------------------------------------- :122967
    (122967, 'It is a rod that, when zapped, unleashes a beam of heat wave.'):
        "Una bacchetta che, agitata, tira una saetta di fuoco.",

    # ---------------------------------------------------------- :123047
    (123047, 'It is a rod that, when zapped, unleashes a beam of freezing air.'):
        "Una bacchetta che, agitata, tira una saetta di gelo.",

    # ---------------------------------------------------------- :123127
    (123127, 'It is a rod that, when zapped, opens a rift containing hostile creatures.'):
        "Una bacchetta che, agitata, evoca mostri ostili qui intorno.",

    # ---------------------------------------------------------- :123207
    (123207, 'It is a rod that, when zapped, shoots an arrow of concentrated magic.'):
        "Una bacchetta che, agitata, tira un dardo magico.",

    # ---------------------------------------------------------- :129953
    (129953, 'It is a rod that, when zapped, teleports nearby target.'):
        "Una bacchetta che, agitata, teletrasporta a caso.",

    # ---------------------------------------------------------- :130033
    (130033, 'It is a rod that, when zapped, reveal the structure of targeted item.'):
        "Una bacchetta che, agitata, identifica gli oggetti che porti.",

# 30 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-009.jsonl'
RIGHE = {
    61949, 62317, 62397, 70754, 71859, 92065, 92800, 93152, 94105, 94537,
    96278, 96358, 98579, 98957, 103508, 104945, 105384, 105969, 106769, 111780,
    117762, 119544, 119624, 122824, 122967, 123047, 123127, 123207, 129953, 130033,
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
