# -*- coding: utf-8 -*-
"""123a - Lotto 071 di `db_item.hsp`: LE ALGHE, e la categoria CHIUDE.

`FILTER_ENVIRONMENT_SEABED`, righe da `:44863` a `:44991`: **6 righe** —
3 dell'indice 0 e **3 dell'indice 2** — su 3 oggetti (mozuku, kombu, wakame).
Con questo lotto la categoria va a **0 da fare su 6 vive**, ed e' la
**ventiseiesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 071`: **+6** per 6 rese,
nessuna gemella. ⓘ `_code.py 071`: 0 righe senza resa in tabella.
`_forma.py 071`: 0 su 6 con lo spazio prima del `\\n`, 0 su 6 con lo spazio
dopo il `#` — tutte e sei senza. Preflight: **0 guasti, 0 parole lunghe**.
`_122-sorelle-per-frase 071`: **0 frasi con una sorella**, la prima volta.

### ⭐⭐⭐ TRE RIGHE COL GIAPPONESE VUOTO, E UNA RETE CHE PER QUESTO SBAGLIA

Le tre `description(2)` — `:44865`, `:44928`, `:44991` — **non hanno
giapponese**. L'inglese un testo ce l'ha, quindi si rendono: e' il caso di
`:89358` e non quello di `:129299`, e la domanda non e' «manca il giapponese?»
ma «esiste una fonte?».

⚠️⚠️⚠️ **Il seguito e' che `_120-serie-bacchette` da' un avviso FALSO.** La
rete dice:

    en :44928  Giant seaweed. You can eat it I guess.
    en :44991  Huge seaweed. You can eat it I guess.
    ⚠️ le rese di queste righe devono essere IDENTICHE: il giapponese e' lo
       stesso, e l'inglese differisce per una sciocchezza

Il giapponese e' lo stesso perche' e' **vuoto** in tutt'e due, e due stringhe
vuote sono uguali a ogni rete che le confronti. Seguito alla lettera, l'avviso
avrebbe cancellato una distinzione che il gioco fa davvero.

⭐ **L'arbitro sta nella `description(3)` degli stessi due oggetti**, che il
giapponese ce l'ha e che il dizionario ha gia' reso:

    :44929  巨大な海藻だ  ->  «Un'alga gigantesca»   (kombu,  en «Giant»)
    :44992  大きな海藻だ  ->  «Un'alga grande»       (wakame, en «Huge»)

Quindi le tre rese dell'indice 2 aprono con **la stessa parola dell'indice 3
dello stesso oggetto**, e il pannello si legge coerente dall'alto in basso.
E l'inglese, che qui e' l'unica fonte diretta, dice la stessa cosa: «Giant» e
«Huge» sono due parole, non una sciocchezza.

⚠️ **La regola generale.** Una rete che confronta due campi puo' dire «uguali»
perche' i campi **non ci sono**. Prima di seguire un avviso di uguaglianza si
guarda se il valore su cui l'ha dato e' vuoto — e se lo e', l'avviso non e' una
prova, e' un'assenza di prove.

### ⓘ Le parole del giapponese, e da dove vengono

- 海藻 -> **«alga»** (glossario). `mozuku`, `kombu` e `wakame` sono nomi
  **invariati** (`invariati.md`, tre voci): non compaiono nel corpo, che parla
  sempre di «un'alga», ed e' il nome in cima al pannello a dire quale sia.
- 具材 -> **«ingrediente»**, dal dizionario: le due righe del mochi.
- ダシ non e' nel dizionario, ma **«brodo»** ci sta gia' due volte, nelle
  stesse due righe del mochi. Si ricopia da li' invece di inventare.
- 喉越し non ha una voce, e l'italiano ce l'ha di suo: di un cibo o di una
  bevanda si dice che **«scende bene»**. L'inglese qui traduce a calco («an
  excellent texture and throat») e non aiuta.
- 酢漬け -> **«sott'aceto»**. 重宝されてきた -> «e' tenuta cara», col passato
  che dura, come fa l'inglese con «has long been valued».

### ▶ Il conto

Il corpo passa da **1.492 a 1.498 rese su 1.513**, e restano **15 righe** — di
cui una rinviata (`:129299`). Dopo il 071 mancano **sei** categorie:

    5  FILTER_AMMO             1  FILTER_PLATINUM
    4  FILTER_FURNITURE_WELL   1  FILTER_GOLD
    2  FILTER_FURNITURE_ALTAR  1  FILTER_CARGO_FOOD

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

    # ---------------------------------------------------------- :44863
    (44863, 'A seaweed with long, slender, branched bodies that can grow to over a meter in length. It has an excellent texture and throat, but is often pickled in vinegar and is not well-liked.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga dal corpo lungo, sottile e ramificato, che a volte passa il metro. La consistenza è ottima e scende bene in gola, ma la si mette quasi sempre sott'aceto, e per questo non piace a molti.\\n#~Alghe e Piante Marine: la Differenza~",

    # ---------------------------------------------------------- :44865
    (44865, "It's seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~"):
        "Un'alga. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ---------------------------------------------------------- :44926
    (44926, 'Seaweed that grows very long. It is also quite heavy due to its high water content. It takes some skill to dry it, but when it dries, it makes a good broth.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga che diventa lunghissima. Ha molta acqua dentro, e perciò pesa parecchio. Farla seccare richiede il suo mestiere, ma da secca se ne ricava un buon brodo.\\n#~Alghe e Piante Marine: la Differenza~",

    # ---------------------------------------------------------- :44928
    (44928, 'Giant seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~'):
        "Un'alga gigantesca. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ---------------------------------------------------------- :44989
    (44989, 'Large seaweed. It grows rapidly by absorbing nutrients from the sea. In some regions, it has long been valued as an ingredient in various dishes.\\n#~Seaweed is not Sea Weed~'):
        "Un'alga di taglia grande. Assorbe il nutrimento del mare e si moltiplica in fretta. In certe regioni, fin da tempi antichi, è tenuta cara come ingrediente di piatti d'ogni sorta.\\n#~Alghe e Piante Marine: la Differenza~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :44991
    (44991, 'Huge seaweed. You can eat it I guess.\\n#~Identification Report: <Seaweed> Category~'):
        "Un'alga grande. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

# 3 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-071.jsonl'
RIGHE = {
    44863, 44865, 44926, 44928, 44989, 44991,
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
