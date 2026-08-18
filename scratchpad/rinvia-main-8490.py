# -*- coding: utf-8 -*-
"""Rinvia `main.hsp:8490`, una `lang()` dentro un `if ( 0 )`.

⚠️⚠️ **E' la quarta famiglia di riga morta**, dopo il `;` (rete 6), il
`/* ... */` (`misura-blocchi-spenti.py`) e il ramo `if ( jp )` della 56a
(`rinvia-item_func-2581.py`). E stavolta non e' nemmeno un commento: e' un ramo
che il compilatore compila e che non e' mai vero.

    8489:  if ( 0 ) {
    8490:      txt lang(name(tc) + "は、" + gain1 + "で" + gain2 + "だ。", ...)
    8491:  }
    8492:  if ( gain2 < 900 ) {
    8493:      txt lang(name(tc) + "は特に得るものが無かったようだ。", ...)

Il giapponese di `:8490` stampa `gain1` e `gain2`, cioe' i **due numeri** del
calcolo dell'esperienza di viaggio: e' una stampa di debug che qualcuno ha
spento lasciandola dov'era. ⭐ La prova che non e' testo la da' anche l'inglese,
**copiato pari pari da `:8493`** — la riga viva tre righe sotto: chi l'ha spenta
non si e' curato di darle un inglese suo, perche' tanto non esce.

Tradurla vorrebbe dire scrivere una frase italiana su due variabili numeriche
che nessuno vedra' mai, e — peggio — darle la stessa resa della riga viva,
seppellendo la differenza.

⚠️ **Nessun referto del progetto guarda gli `if ( 0 )`.** Quanti altri ce ne
siano non lo sa nessuno: questo l'ha trovato il dossier, leggendo il sorgente
intorno alla voce.

La forma segue la regola della 39a: si compone tutto in memoria, si codifica, e
solo allora si apre il file in scrittura.
"""
import io
import json

FILE = 'main.hsp'
RIGA = 8490
FIRMA = 'a3c6c8cb014931430f3710889e927355f1b0a5be'

MOTIVO = (
    "La `lang()` sta dentro un `if ( 0 )` (`main.hsp:8489`), cioe' un ramo che "
    "non e' mai vero: e' una stampa di **debug** dei due numeri del calcolo "
    "dell'esperienza di viaggio (`gain1` e `gain2`), spenta lasciandola dov'era. "
    "⭐ Che non sia testo lo dice anche l'inglese, copiato pari pari da `:8493`, "
    "la riga viva tre righe sotto: chi l'ha spenta non le ha dato un inglese suo. "
    "⚠️ E' la QUARTA famiglia di riga morta dopo il `;` (rete 6), il `/* ... */` "
    "(`misura-blocchi-spenti.py`) e il ramo `if ( jp )` (56a). Nessun referto "
    "del progetto guarda gli `if ( 0 )`, e quanti ce ne siano non lo sa nessuno."
)

# --- la voce non e' nel dizionario: e' un rinvio prima della traduzione -----

percorso_diz = f'dizionario/{FILE}.jsonl'
voci = [json.loads(l) for l in io.open(percorso_diz, encoding='utf-8').read().splitlines()
        if l.strip()]
if any(v['firma'] == FIRMA for v in voci):
    raise SystemExit(f'la voce {FIRMA} e\' gia\' nel dizionario: '
                     f'questo rinvio va scritto come quello di item_func:2581')

# --- e la riga e' davvero dentro un `if ( 0 )` -----------------------------

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\main.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
sopra = righe[RIGA - 2].strip()
if sopra != 'if ( 0 ) {':
    raise SystemExit(f'la riga sopra la {RIGA} non e\' un `if ( 0 )`: {sopra!r}')

# --- il rinvio non c'e' gia' -----------------------------------------------

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
if any(json.loads(l)['firma'] == FIRMA for l in righe_rin):
    raise SystemExit('rinvio gia\' presente: niente da fare')

# --- si compone tutto, e solo allora si scrive ------------------------------

rin_nuovo = righe_rin + [json.dumps({
    'firma': FIRMA,
    'file': FILE,
    'en': " didn't seem to have anything to gain from the travel.",
    'rinviata_a': 'nessuna fase: la lang() sta dentro un `if ( 0 )`',
    'motivo': MOTIVO,
}, ensure_ascii=False)]

dati = ('\n'.join(rin_nuovo) + '\n').encode('utf-8')
with io.open('rinviate.jsonl', 'wb') as f:
    f.write(dati)

print(f'rinviate.jsonl: {len(righe_rin)} -> {len(rin_nuovo)}')
