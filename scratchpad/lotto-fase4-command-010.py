# -*- coding: utf-8 -*-
"""Lotto `command-010`: i 39 pensieri di `*com_knowOther`, prima meta'.

E' la telepatia: quel che un compagno sta pensando, letto col comando che apre
la finestra «こころの中» / «In the heart» (`:1928`). Il sorgente e' una cascata
di `if` che si sovrascrivono a vicenda — l'ultima condizione vera vince — e
questo lotto prende i primi cinque blocchi:

| blocco | quando | voci |
|---|---|---|
| generico | sempre, `rnd(17)` | 17 |
| fame | `CDATA_HUNGER <= 10000` | 5 |
| sete | `CDATA_THIRST <= 10000` | 4 |
| affetto | `CDATA_EVOCHAT_POINTS > 0`, poi `== 10` | 6 |
| combattimento | `CDATA_AI_AGGRO > 0`, uno per `CDATA_TONE` | 7 |

✅ **Il registro e' il monologo interiore in prima persona**, che e' quel che il
giapponese fa senza soggetto — 「もっと刺激がほしい」, 「昔のことを思い出して
いる」 — e che in italiano non ha genere finche' si resta al **presente e senza
participio**: «Voglio piu' emozioni», «Sto ripensando ai vecchi tempi». Il
compagno puo' essere di qualunque genere, come nel «Background» della stessa
sessione.
⚠️ Due rese sono state girate proprio per questo: 「もっと自分のことを理解して
ほしい」 non e' «vorrei essere capito» ma «vorrei che mi capissi di piu'», e
「愛を感じていたい」 non e' «vorrei sentirmi amato» ma «ho bisogno di sentire
l'amore».

⚠️ **L'inglese cambia persona a meta' elenco, e il giapponese no.** Dentro lo
stesso blocco della fame ci sono «Want to eat anything» (prima persona
sottintesa) e «Wants to eat a lot» / «Wants a sweet one» (terza), e nel blocco
generico «Hungry and has no strength.» e' terza persona con tanto di punto.
Il giapponese e' uniforme: sono tutti pensieri, e in italiano sono tutti in
prima persona.

⚠️ **I sette pensieri di combattimento sono lo stesso momento in sette
caratteri**, uno per valore di `CDATA_TONE`, cioe' il tono che si sceglie col
comando «Change Tone». Vanno tenuti distinti fra loro: `:1678` e `:1690` dicono
tutt'e due «non perdo», ma il primo e' una promessa e il secondo un'arroganza —
「絶対負けない」 contro 「負けるわけがない」. E `:1693` 「いざ尋常に勝負！」 e'
lingua da duello antico.

💡 **Tetto 42 caratteri** (`:1590`), misurato con `scratchpad/tetto-en.py`.
⚠️ Anche questa finestra non la guarda nessuna guardia: `*com_knowOther` disegna
con `gmes` a `wx + 54` dentro una finestra da 400 px (`:1929`, `:1942`), quindi
non passa da `*prompt_key` e `larghezze.py` — che comunque legge solo
`text.hsp` — non c'entra niente.

💡 Zero copie da `dossier.py`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1575-:1623 i diciassette pensieri di sempre, `rnd(17)`.
    (1575, 'Not thinking anything in particular'):
        'Non sto pensando a niente in particolare',
    (1578, 'Want more stimulation'):
        'Voglio più emozioni',
    (1581, 'Remember old things'):
        'Sto ripensando ai vecchi tempi',
    (1584, 'Am I OK?'):
        'Ma vado bene così come sono?',
    # ⚠️ il giapponese e' la barzelletta: PENSA di non pensare a niente
    (1587, 'Do not think about anything!'):
        'Sto pensando di non pensare a niente',
    (1590, 'I know that you are looking into my heart!'):
        'Lo so che mi stai leggendo nel pensiero!',
    # ⚠️ «vorrei essere capito» concorderebbe col compagno
    (1593, 'Want you to understand more about myself'):
        'Vorrei che mi capissi di più',
    (1596, 'Concerned about the weather!'):
        'Mi preoccupa il tempo',
    (1599, 'Worried about my family'):
        'Sono in pensiero per la famiglia',
    (1602, 'Very bored'):
        'Che noia mortale',
    (1605, 'Forgetting something...'):
        'Ho la sensazione di scordare qualcosa...',
    (1608, 'Eyes slightly itchy'):
        'Mi prudono gli occhi',
    (1611, 'Why will the gaps not disappear?'):
        'Perché le disuguaglianze non spariscono?',
    (1614, 'Thinking about the meaning of living'):
        'Sto pensando al senso della vita',
    (1617, 'Absolutely want it...'):
        'Voglio quella cosa, a tutti i costi...',
    # ⚠️ «vorrei sentirmi amato» concorderebbe col compagno
    (1620, 'Want to feel love'):
        "Ho bisogno di sentire l'amore",
    (1623, 'What was the dream last time?'):
        'Che voleva dire quel sogno?',

    # --- :1626-:1638 la fame. ⚠️ l'inglese passa alla terza persona a meta'
    #     blocco («Wants to eat a lot»), il giapponese no.
    (1626, 'Hungry and has no strength.'):
        'Ho fame, non ho più forze',
    (1629, 'Want to eat anything'):
        'Qualunque cosa, purché sia cibo',
    (1632, 'Wants to eat a lot'):
        'Voglio mangiare qualcosa di sostanzioso',
    (1635, 'Wants a sweet one'):
        'Voglio qualcosa di dolce',
    (1638, 'Want to eat delicious home cooking'):
        'Voglio un piatto fatto in casa, e buono',

    # --- :1643-:1652 la sete.
    (1643, 'Looks completely dried up'):
        'Sto per seccarmi',
    # ⚠️ 「喉がカラカラ」 e' la gola secca, non la gola che fa male
    (1646, 'My throat hurts'):
        'Ho la gola secca',
    (1649, 'Seems disoriented from the lack of water'):
        'Mi gira la testa dalla sete',
    (1652, 'W-Water...'):
        'A-Acqua...',

    # --- :1657-:1673 l'affetto: tre pensieri se ti vuole bene, tre se e' al
    #     massimo (`EVOCHAT_POINTS == 10`).
    (1657, 'I can work hard today'):
        'Oggi mi sento di dare il massimo',
    (1660, 'Happy'):
        'Non sto più nella pelle',
    (1663, 'Such a life is not bad either'):
        'Anche una vita così non è male',
    # ⚠️ 「のろけたい」 e' vantarsi del proprio amore, non di una persona
    (1667, 'Want to brag about someone'):
        'Vorrei raccontare a tutti il mio amore',
    (1670, 'Very happy!'):
        'Sono al settimo cielo!',
    (1673, 'I am glad that I am alive'):
        'Ne è valsa la pena, di vivere fin qui',

    # --- :1678-:1696 i sette caratteri in combattimento, uno per `CDATA_TONE`.
    #     ⚠️ vanno tenuti distinti fra loro: vedi il docstring.
    (1678, 'I will never lose'):
        'Non perderò mai',
    (1681, 'Only enemies are beaten'):
        'I nemici si abbattono e basta',
    (1684, 'I will fight as usual'):
        'Faccio come sempre e andrà bene',
    (1687, 'Anxious about defeat'):
        'E se non ce la faccio?',
    (1690, 'No possibility of lose'):
        'Non posso perdere',
    # ⚠️ 「いざ尋常に勝負！」 e' lingua da duello antico
    (1693, "Let's fight squarely"):
        'E ora, un duello leale!',
    (1696, 'Sure works well'):
        'Qualcosa si risolverà',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-010.jsonl'
DA, A = 1575, 1698
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
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

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
