# -*- coding: utf-8 -*-
"""Lotto fase4-tcg-001: il tavolo del duello e la fine della partita
(tcg.hsp, righe 0-2999).

33 rese, e sono le prime `lang()` mai tradotte dei file del gioco di carte.
⚠️ **`tcg.hsp` non era nel perimetro**, e non per una svista: i file del
dizionario erano diciannove e nessun `tcg` fra loro. La 52ª ha chiuso le righe
**nude** di `tcg.hsp` e `tcg_custom.hsp` e la ripresa li ha chiamati «finiti» —
che era vero per quel che il referto guardava, e falso a schermo.

⭐⭐⭐ **A dimostrarlo e' stato il collaudo, alla prima schermata.** La finestra
«a Proper Deck» — quella che esce quando il mazzo ha meno di 30 carte, cioe' la
prima che vede chiunque provi il gioco — mostra un paragrafo inglese con
**incollata in coda una frase italiana**:

    :2560  buff  = lang("…", "I should make sure my deck has at least 30…")
    :2563  buff += "A Miches di Vernis piacciono tutti i giochi da tavolo…"

⭐ **E' una classe nuova: un letterale nudo che si SOMMA a una `lang()`.** Le
«due letterali per riga» della 51ª stavano sulla stessa riga e si vedevano; qui
stanno a tre righe di distanza, in due reti diverse — una dentro il perimetro,
l'altra fuori — e finiscono nello **stesso paragrafo**. Tradurre solo la meta'
che il referto vede da' un risultato **peggiore** di lasciare tutto inglese.
💡 La stessa forma torna identica alla fine di ogni partita: `:2803` e' gia'
italiano («Esito imprevisto…») e i ventuno esiti veri di `:2804`-`:2821` sono
inglesi. Titolo italiano, corpo inglese, bottone inglese.

⚠️ **`:1505` e' rinviata perche' e' MORTA, e nessuna rete l'avrebbe fermata.**
La riga e' `// rtvaln += lang("  ランク:", "  Rank:") + cardrefcost`: un
commento `//`, che in HSP spegne la riga come il `;`. La rete 6 guarda il `;` e
i blocchi `/* … */` e **non guarda `//`** — quarta famiglia di riga morta dopo
il `;`, il blocco e il ramo `if ( jp )`. Misurata con `scratchpad/barre_spente.py`:
**9 in tutto il sorgente, e una gia' tradotta** (`command.hsp:17515`), cioe'
lavoro gia' speso su testo che nessuno legge.

⚠️ **`:2470` e' rinviata per l'ORDINE DELLE PAROLE, e vuole una toppa.** Il menu
dei mazzi si compone cosi': `s@tcg(cnt) = lang("白", "White")` e poi
`s@tcg(cnt) += lang("のデッキ", " Deck")`. In italiano il nome viene **prima** del
colore, quindi la resa sta tutta nel colore — «Mazzo bianco» — e a `:2470` non
resta niente da dire. Una resa vuota non e' esprimibile (`firme_tradotte` la
conta come non tradotta), quindi la riga si spegne con una toppa.
💡 E sulla stessa schermata ci sono altri tre letterali nudi che nessun referto
elencava — `" (NG 12/30)"` a `:2478` e `:2481`, `" [Use]"` a `:2484` — perche'
`s@tcg(cnt) +=` porta il **suffisso di modulo**: `s@tcg` non e' `s`.

⭐ **«Sarà per la prossima volta.» non e' stata scelta: e' stata trovata.**
`db_creature.hsp:46267` rende cosi' 「また今度ね」, ed e' lo stesso giapponese di
tutte e quattro le occorrenze qui. ⚠️ Ma `:2786` e `:2791` hanno **lo stesso
giapponese e un inglese diverso** — «To the Amur-cage you go!» e
«Noooooooooooooo!» — perche' il mod ha riusato la `lang()` senza toccare il
primo argomento: li' si segue l'inglese, che e' la lingua di monte della resa.

⭐ **«gabbia di Amur» viene dalla 52ª**, che l'aveva resa per la prima volta in
tutto il progetto a `tcg_custom.hsp:1608`.

⚠️ **«Noooooooooooooo!» resta identica, e va detto perche' non e' una
dimenticanza**: e' un urlo, si scrive uguale nelle due lingue. Stessa scelta di
«Mana», «Immune» e «Abnormal».

💡 **Il tetto dei due menu si misura, e `larghezze.py` non lo fa.** I menu di
`tcg.hsp` si costruiscono con `promptAdd` e non con `s(cnt) = lang()` dentro un
`#deffunc`, quindi la forma che lo strumento cerca non c'e'. Ma il riquadro e'
lo stesso — `*prompt_key@` in HSP e' l'etichetta del **modulo principale**, cioe'
proprio `*prompt_key` — e vale lo stesso metro, `(pixel − 46) / 7,7`:

    :2499  riquadro da 240px  ->  25 caratteri   «Costruisci il mazzo» (19)
                                                 «Imposta come principale» (23)
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :1167-:1173 la riga d'aiuto in fondo al tavolo, quando il cursore non
    #     e' su nessuna carta. `cardhelp` (:651), disegnata a :3497.
    (1167, 'End your main phase.'):
        'Chiudi la fase principale.',
    (1170, 'No blocker.'):
        'Non bloccare.',
    (1173, 'Choose Randomly.'):
        'Scegli a caso.',

    # --- :1495-:1610 la scheda della carta, composta in `rtvaln` da `card_ref`.
    # ⚠️ I due spazi davanti sono del sito e vanno tenuti: separano dal nome.
    (1495, '  No.'):
        '  N.',
    (1499, ' <Land>'):
        ' <Terreno>',
    (1503, ' <Spell>'):
        ' <Magia>',
    (1509, '  Rare:'):
        '  Rarità:',
    # ⚠️ Lo spazio in coda e' del sito: quel che segue si attacca qui.
    (1512, 'Data: '):
        'Dati: ',
    (1610, 'Effect: '):
        'Effetto: ',

    # --- :2181-:2273 i tre rifiuti e i due sacrifici, in mezzo al duello.
    (2181, 'You sacrifice the card.'):
        'Sacrifichi la carta.',
    (2184, 'The opponent sacrifices the card.'):
        "L'avversario sacrifica la carta.",
    # ⚠️ rete 13: lo stesso giapponese 「これ以上は場に出せない。」 per due inglesi.
    #    L'inglese distingue chi ha il campo pieno, il giapponese no: si segue
    #    l'inglese, che e' la lingua di monte della resa.
    (2238, 'Your field is full.'):
        'Il tuo campo è pieno.',
    (2264, "Your opponent's field is full."):
        "Il campo dell'avversario è pieno.",
    (2273, "You don't have enough mana."):
        'Non hai abbastanza mana.',

    # --- :2468-:2474 il menu di scelta del mazzo.
    # ⚠️ Il nome sta QUI e non in `:2470`: in italiano viene prima del colore.
    #    Vedi il docstring e la rinviata.
    (2468, 'White'):
        'Mazzo bianco',
    (2468, 'Blue'):
        'Mazzo blu',
    (2468, 'Silver'):
        'Mazzo argento',
    (2468, 'Red'):
        'Mazzo rosso',
    (2468, 'Black'):
        'Mazzo nero',
    # ⚠️ Lo spazio in testa e' del sito: si attacca al nome del mazzo.
    (2474, ' (New)'):
        ' (nuovo)',

    # --- :2497-:2498 il menu del mazzo scelto. Riquadro da 240px -> 25 caratteri.
    (2497, 'Edit Deck'):
        'Costruisci il mazzo',
    (2498, 'Set as Main Deck'):
        'Imposta come principale',

    # --- :2558-:2571 la finestra che esce col mazzo troppo piccolo.
    #     E' la prima schermata che vede chiunque provi il gioco.
    (2558, 'a Proper Deck'):
        'Un mazzo come si deve',
    # ⚠️ Lo spazio in coda e' del sito: `:2563` si attacca qui.
    (2560, 'I should make sure my deck has at least 30 cards before a duel. May be I should get more cards to put them in my deck. '):
        'Prima di un duello devo controllare che il mio mazzo abbia almeno 30 carte. Forse dovrei procurarmi altre carte da metterci dentro. ',
    # ⭐ 「また今度ね」 e' gia' reso a db_creature.hsp:46267.
    (2565, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2571, 'a Proper Deck (Lethal)'):
        'Un mazzo come si deve (mortale)',
    (2605, 'Maybe next time.'):
        'Sarà per la prossima volta.',
    (2776, 'Maybe next time.'):
        'Sarà per la prossima volta.',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(1505, '  Rank:'), (2470, ' Deck')}

USCITA = 'lavoro/fase4-tcg-001.jsonl'
DA, A = 0, 2780
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\tcg.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_tcg.jsonl', encoding='utf-8') if l.strip()]
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
# ⚠️⚠️ **CORRETTA nella 53ª, ed e' la quinta rete che si corregge** dopo la 8,
# la 4 (per le firme di contenuto), la 9 e la 6. Il raggruppamento era per
# giapponese soltanto, e dava per scontato che uno stesso primo argomento di
# `lang()` volesse dire uno stesso messaggio. Nei file del gioco di carte non e'
# vero: chi ha scritto il mod **riusa il giapponese senza toccarlo** e cambia
# solo l'inglese.
#
#     tcg.hsp:2238  lang("これ以上は場に出せない。", "Your field is full.")
#     tcg.hsp:2264  lang("これ以上は場に出せない。", "Your opponent's field is full.")
#     tcg.hsp:2565  lang("また今度ね", "Maybe next time.")
#     tcg.hsp:2786  lang("また今度ね", "To the Amur-cage you go!")
#     tcg.hsp:4432  lang("降参する", "Surrender")   e  :4433  lang("降参する", "No")
#
# Misurato prima di toccarla: **9 giapponesi su 123** dell'estrazione `tcg`
# portano piu' di un inglese, cioe' il 7%. La rete vecchia le bocciava tutte, e
# la resa che pretendeva — «Il tuo campo e' pieno» anche per il campo
# dell'avversario — sarebbe stata **sbagliata a schermo**.
#
# ✅ La regola giusta e' quella che il progetto applica da sempre: si sostituisce
# il SECONDO argomento, quindi la lingua di monte della resa e' l'INGLESE. Due
# voci con lo stesso giapponese e lo stesso inglese devono coincidere — e quelle
# la rete continua a bocciarle. Due voci con lo stesso giapponese e un inglese
# diverso sono una distinzione di monte, e vanno **lette**, non impedite.
#
# 💡 Cosi' la rete 4 diventa simmetrica alla rete 13, che e' la stessa domanda
# vista dall'altro lato — «stesso inglese, giapponesi diversi» — ed e' un
# referto da sempre. Non c'era motivo perche' una fosse un errore duro e l'altra
# no.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
inglesi_per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], v['en'], firma_di(v))].add(parole(RESE[chiave(v)]))
    inglesi_per_jp[v['jp']].add(v['en'])
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, en, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} / {en!r} con firma {firma} '
                         f'reso in {len(rese)} modi: {rese}')
for jp, inglesi in sorted(inglesi_per_jp.items()):
    if len(inglesi) > 1:
        print(f'💡 rete 4: il giapponese {jp!r} sta per {len(inglesi)} inglesi diversi '
              f'{sorted(inglesi)}: la resa segue l\'inglese, ma guarda che sia voluto')
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
