# -*- coding: utf-8 -*-
"""`command.hsp:15489` attacca « Guild Point)» FUORI dalla `lang()`: rinvio + toppa.

⚠️⚠️ La riga del sorgente e'

    txt lang(itemname(ci) + "を納入した", "You deliver " + itemname(ci) + ". ")
        + "(" + (inv(INV_ITEM_PARAM1, ci) + 5) * inv(INV_ITEM_NUM, ci) + " Guild Point)"

cioe' la consegna dei libri antichi alla Gilda dei Maghi. La `lang()` si chiude,
e **fuori** dalla parentesi c'e' un letterale inglese che vale per tutt'e due le
lingue: anche il giocatore giapponese legge «Guild Point». Il dizionario non lo
raggiunge, perche' sostituisce il **secondo argomento di `lang()`** e quello sta
dopo.

⚠️ **E non lo vede nessuno dei cinque punti ciechi**, ognuno per un motivo suo:
`blocchi_en.py` cerca `if ( en )`, `else_jp.py` il ramo `else` di un `if ( jp )`,
`lang-nel-ramo-jp.py` la `lang()` chiusa nel ramo giapponese, `variabili_en.py`
l'**assegnamento** di una variabile con dentro un letterale inglese, e
`cnv_str_en.py` le chiavi di `cnv_str`. Qui non c'e' ne' un ramo ne' una
variabile ne' una conversione: c'e' una **concatenazione in coda a una `lang()`**,
che e' una famiglia nuova.

⚠️⚠️ **E la prima toppa che ho scritto era della specie sbagliata.** Siccome
`applica.py` fa girare le toppe **dopo** il dizionario (`applica.py:530`), avevo
agganciato `cerca` alla riga **gia' tradotta**, e in build funzionava. Ma
`strumenti/tests/test_toppe.py:104` pretende che ogni toppa si applichi al
**sorgente pinnato**, ed e' quella prova a diventare rossa il giorno in cui
upstream riscrive la riga: una toppa agganciata al testo italiano non ha piu'
nessun rapporto col sorgente e quella prova non varrebbe piu' niente.
✅ La forma giusta e' quella che `LEGGIMI.md` chiama **rinvio + toppa insieme**
(`toppa-action-15221.py`, `toppa-proc-24107.py`, `toppa-chara_func-3037.py`): il
rinvio toglie la voce dal dizionario, cosi' `applica` non tocca la riga, e la
toppa la riscrive tutta intera partendo dal sorgente. 💡 **La regola generale**:
una toppa e una resa non possono stare sulla stessa riga. O la riga la sistema
il dizionario, o la sistema la toppa.

💡 **Il termine era gia' deciso quaranta righe piu' su**: `:14115` e'
`lang("ギルドポイント", "Guild Point")`, reso «Punti gilda» in un lotto passato. Lo
stesso testo, dentro una `lang()` vera, e percio' gia' tradotto da un pezzo. La
differenza non e' il testo: e' dove sta scritto.

⚠️ Sostituzione 1:1 sulle righe, e il ramo giapponese resta intatto.
"""
import io
import json

from strumenti.accenti import degrada

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\command.hsp'
NOME = 'command.hsp'
RIGA = 15489

INGLESE = '"You deliver " + itemname(ci) + ". "'
ITALIANO = '"Hai consegnato " + itemname(ci) + ". "'
PUNTI_EN = ' Guild Point)'
PUNTI_IT = ' punti gilda)'

MOTIVO = (
    "command.hsp:15489, la consegna dei libri antichi alla Gilda dei Maghi. "
    "La riga attacca « Guild Point)» **fuori** dalla `lang()`: "
    "`txt lang(...) + \"(\" + punti + \" Guild Point)\"`, e quel letterale vale per "
    "tutt'e due le lingue — anche il giocatore giapponese legge «Guild Point». Il "
    "dizionario non lo raggiunge, perche' sostituisce il secondo argomento di "
    "`lang()` e quello sta dopo. "
    "⚠️ Non lo vede nessuno dei cinque punti ciechi: `blocchi_en.py` cerca "
    "`if ( en )`, `else_jp.py` il ramo `else`, `lang-nel-ramo-jp.py` la `lang()` nel "
    "ramo giapponese, `variabili_en.py` l'assegnamento di una variabile, "
    "`cnv_str_en.py` le chiavi di `cnv_str`. Qui c'e' una **concatenazione in coda a "
    "una `lang()`**, che e' una famiglia nuova. "
    "✅ Rinvio + toppa insieme, come action.hsp:15221: la voce e' fuori dal "
    "dizionario, cosi' `applica` non tocca la riga, e la toppa riscrive il ramo "
    "inglese per intero — resa piu' punti. Una toppa e una resa non possono stare "
    "sulla stessa riga. "
    "💡 Il termine era gia' deciso a `:14115`, `lang(\"ギルドポイント\", \"Guild Point\")` "
    "reso «Punti gilda»: stesso testo, dentro una `lang()` vera. "
    "⚠️ Sostituzione 1:1 sulle righe; il ramo giapponese resta intatto."
)

righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
originale = righe[RIGA - 1]

if INGLESE not in originale or PUNTI_EN not in originale:
    raise SystemExit(f'{NOME}:{RIGA} non ha la forma attesa: {originale.strip()[:120]}')

nuova = degrada(originale.replace(INGLESE, ITALIANO).replace(PUNTI_EN, PUNTI_IT))
if nuova == originale:
    raise SystemExit('la toppa non cambierebbe niente')

quante = sum(1 for r in righe if r == originale)
if quante != 1:
    raise SystemExit(f'la riga compare {quante} volte, non una: toppa ambigua')

nuova_toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
if _chiave(nuova_toppa) in gia:
    print('toppa gia presente')
else:
    dati = (json.dumps(nuova_toppa, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'toppa aggiunta (totale {len(esistenti) + 1})')
    print(f'  - {originale.strip()[-90:]}')
    print(f'  + {nuova.strip()[-90:]}')

# --- il rinvio, che e' l'altra meta' --------------------------------------
CHIAVE = (RIGA, 'You deliver . ')
voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip())}
if CHIAVE not in voci:
    raise SystemExit(f'chiave che non aggancia nessuna voce: {CHIAVE}')
v = voci[CHIAVE]
rinviata = {
    'firma': v['firma'],
    'file': NOME,
    'en': v['en'],
    'rinviata_a': 'mai: la riga la sistema la toppa su command.hsp:15489',
    'motivo': MOTIVO,
}

esistenti_r = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti_r}
if rinviata['firma'] in firme:
    print('rinvio gia presente')
else:
    dati = (json.dumps(rinviata, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'rinvio aggiunto (totale {len(esistenti_r) + 1})')
