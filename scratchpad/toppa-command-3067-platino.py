# -*- coding: utf-8 -*-
"""L'ultima riga del diario: rinvio della firma, poi toppa su tutta la riga.

`command.hsp:3067` e' l'unica riga della «Cronaca delle avventure» che il lotto
del diario non poteva prendere:

    noteadd "@BL   Total Platinum: " + gdata(GDATA_FLAG_TOTAL_PLATINUM) + lang("枚", " Plat")

Porta un letterale **nudo** (`"@BL   Total Platinum: "`, che nessuna `lang()`
raggiunge) e una **resa** (`lang("枚", " Plat")`, che il dizionario raggiungerebbe
eccome) sulla stessa riga. La regola della 46ª dice che una toppa e una resa non
ci stanno insieme, e il motivo e' concreto: la toppa aggancia il testo del
sorgente pinnato, il dizionario riscriverebbe quella riga prima che la toppa
arrivi, e la catena si spezzerebbe.

## Il rinvio c'era gia', e aveva scritto lui stesso quando sarebbe scaduto

⭐⭐⭐ **Questa toppa non ha dovuto rinviare niente: la firma era gia' in
`rinviate.jsonl` da una sessione precedente**, e il motivo scritto allora
finiva cosi': «*Si sblocca il giorno in cui qualcuno **traduce il ramo `else`**,
che e' lavoro da toppa e non da dizionario*». Quel giorno e' oggi. E' l'opposto
della toppa dell'orso della 49ª — li' una toppa si era congelata addosso una
resa che stava altrove ed era scaduta senza che nessuno se ne accorgesse; qui un
rinvio ha nominato la propria condizione di sblocco, e la condizione e' arrivata.
💡 La differenza fra le due sta tutta nel fatto che una **dipendeva da un valore
copiato** e l'altra **da un fatto verificabile**.

⚠️ Il rinvio era stato scritto guardando `:2982`, cioe' l'occorrenza nel ramo
`if ( jp )`, che in italiano non gira mai. La stessa firma pero' vive **anche
qui**, nel ramo `else`, dove gira eccome — e per fortuna il rinvio vale per
firma, quindi copre tutt'e due. ⚠️ **Il rinvio e' per FIRMA, e la firma e'
contenuto**: `carica_rinviate` filtra per file, quindi fuori da `command.hsp`
non tocca nulla, e dentro tocca due righe sole.

## La resa

    Total Platinum: 123 Plat   ->   Platino raccolto: 123 pz.

Il giapponese (`:2982`) dice 「ﾌﾟﾗﾁﾅ硬貨入手数」, cioe' **quante** monete di platino
si sono prese in tutto: «Platino raccolto» dice la stessa cosa senza ripetere
«monete», che il contatore 「枚」 gia' porta. ⭐ E ` pz.` non e' inventato: e' la
resa che `command.hsp:14272` da' gia' a 「枚」 nella lista delle medaglie.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'command.hsp'
RIGA = 3067
FIRMA = 'ccb7b2605ca17423291218f6d3fefd5d2f0cabeb'
EN = ' Plat'

SOSTITUZIONI = [
    ('"@BL   Total Platinum: "', '"@BL   Platino raccolto: "'),
    ('" Plat"', '" pz."'),
]

MOTIVO_RINVIO = (
    "Rinviata per lasciare il posto alla toppa su command.hsp:3067, l'ultima riga del "
    "diario che il lotto della 50a non poteva prendere. La riga porta un letterale "
    "INGLESE NUDO (`\"@BL   Total Platinum: \"`, che nessuna `lang()` raggiunge, quinto "
    "punto cieco) e questa resa sulla STESSA riga, e la regola della 46a vieta toppa e "
    "resa insieme: la toppa aggancia il sorgente pinnato, il dizionario riscriverebbe "
    "la riga prima che la toppa arrivi e la catena si spezzerebbe. Tolta la firma dal "
    "perimetro, la toppa puo' riscrivere tutta la riga — etichetta e argomento inglese "
    "della lang() insieme — e diventa «Platino raccolto: 123 pz.». "
    "⚠️ La firma e' contenuto e tocca due sole righe di command.hsp: la :3067 e la "
    ":2982, che e' la stessa voce nel ramo giapponese, che non si traduce mai. Fuori da "
    "command.hsp non tocca nulla, perche' `carica_rinviate` filtra per file."
)

MOTIVO_TOPPA = (
    "command.hsp:3067, l'ultima riga della «Cronaca delle avventure» del diario. "
    "⚠️ E' l'unica riga della schermata che porta un letterale INGLESE NUDO "
    "(`\"@BL   Total Platinum: \"`) e una RESA (`lang(\"枚\", \" Plat\")`) insieme, e per "
    "questo non stava nel lotto delle 54: la regola della 46a vieta toppa e resa sulla "
    "stessa riga. ⭐ Ma la firma della resa era GIA' rinviata (rinviate.jsonl, firma "
    "ccb7b26…) da una sessione precedente, che l'aveva vista nel ramo `if ( jp )` di "
    ":2982 e aveva scritto da se' quando sarebbe scaduta: «si sblocca il giorno in cui "
    "qualcuno traduce il ramo else, che e' lavoro da toppa e non da dizionario». Quel "
    "giorno e' la 50a. Il dizionario non passa di qui, e la toppa puo' riscrivere tutta "
    "la riga. "
    "⭐ La resa: il giapponese (:2982) dice 「ﾌﾟﾗﾁﾅ硬貨入手数」, cioe' quante monete di "
    "platino si sono prese in tutto — «Platino raccolto» lo dice senza ripetere "
    "«monete», che il contatore 「枚」 gia' porta. E ` pz.` non e' inventato: e' la resa "
    "che command.hsp:14272 da' gia' a 「枚」 nella lista delle medaglie. "
    "⚠️ Il rinvio tocca due righe sole (:3067 e :2982, il ramo giapponese che non si "
    "traduce mai) e `carica_rinviate` filtra per file, quindi fuori da command.hsp non "
    "toglie niente a nessuno."
)

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')
originale = sorg[RIGA - 1]

if build[RIGA - 1] != originale:
    raise SystemExit(f"{NOME}:{RIGA}: la build ha gia' riscritto questa riga: rinvio non applicato?")
for righe, eti in ((sorg, 'sorgente'), (build, 'build')):
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit(f'{NOME}:{RIGA} compare {quante} volte nel {eti}: toppa ambigua')

nuova = originale
for cerca, metti in SOSTITUZIONI:
    if nuova.count(cerca) != 1:
        raise SystemExit(f'{NOME}:{RIGA}: `{cerca}` compare {nuova.count(cerca)} volte, non una')
    nuova = nuova.replace(cerca, metti)
if nuova == originale:
    raise SystemExit(f'{NOME}:{RIGA}: la toppa non cambierebbe niente')
try:
    nuova.encode('cp932')
except UnicodeEncodeError as errore:
    raise SystemExit(f'{NOME}:{RIGA}: testo che CP932 non sa scrivere ({errore})')

# ── il rinvio ────────────────────────────────────────────────────────────────
rinviate = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in rinviate}
if FIRMA in firme:
    print('rinvio gia presente')
else:
    voce = {'firma': FIRMA, 'file': NOME, 'en': EN,
            'rinviata_a': 'con la toppa su command.hsp:3067 (Total Platinum)',
            'motivo': MOTIVO_RINVIO}
    dati = (json.dumps(voce, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'1 rinviata aggiunta (totale {len(rinviate) + 1})')

# ── la toppa ─────────────────────────────────────────────────────────────────
toppe = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova, 'motivo': MOTIVO_TOPPA}
if _chiave(toppa) in {_chiave(json.loads(l)) for l in toppe}:
    print('toppa gia presente')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = (json.dumps(toppa, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'1 toppa aggiunta (totale {len(toppe) + 1})')
    print(f'  - {originale.strip()}')
    print(f'  + {nuova.strip()}')
