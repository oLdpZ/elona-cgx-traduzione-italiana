# -*- coding: utf-8 -*-
"""Rinvia `item_func.hsp:2581`, una `lang()` chiusa nel ramo giapponese.

⚠️ Questo rinvio TOGLIE anche la voce dal dizionario, ed e' il primo che lo fa:
gli altri rinviano una voce mai tradotta. Qui la voce era stata resa nella 56ª
— con `*`, cioe' identica all'inglese — e finche' resta nel dizionario il
referto `scratchpad/lang-nel-ramo-jp.py` conta 1 «gia' tradotta» invece di 0.
Quel referto e' una **spia**: il suo valore atteso e' zero, e una spia ferma su
uno non segnala piu' niente.

La forma dello script segue la regola della 39ª: si compone tutto in memoria,
si codifica, e solo allora si aprono i file in scrittura.
"""
import io
import json

FILE = 'item_func.hsp'
RIGA = 2581
FIRMA = '465b70bb521ca8854776d70335486a76504d353d'

MOTIVO = (
    "La `lang()` sta dentro un ramo `if ( jp )` (`item_func.hsp:2579`), e "
    "l'italiano non ci passa mai: quando la lingua non e' il giapponese il "
    "codice va all'`else` di `:2582` e disegna un **cerchio** con `circle`, "
    "invece di stampare un carattere. Il pallino 「●」 e' il segno che il "
    "giapponese usa per marcare le resistenze attive nella fila in cima alla "
    "finestra dell'equipaggiamento; in inglese quel segno non e' un carattere, "
    "e' un disegno. L'asterisco del secondo argomento non arriva a schermo "
    "nemmeno una volta. "
    "⚠️ E' la terza famiglia di riga morta oltre al `;` e al `/* ... */`: la "
    "riga e' viva, il file e' vivo, la `lang()` e' vera — a spegnerla e' il "
    "**ramo della lingua**. La rete 6 non la vede perche' guarda i commenti, "
    "e a trovarla e' stato `scratchpad/lang-nel-ramo-jp.py` all'apertura della "
    "57a, salito da 0 a 1 dopo il lotto `fase4-item_func-002` della 56a. "
    "⭐ Il costo del rinvio e' zero a schermo — la resa era `*`, identica "
    "all'inglese — e il guadagno e' la spia che torna a zero."
)

# --- la voce esiste, ed e' quella che diciamo -------------------------------

percorso_diz = f'dizionario/{FILE}.jsonl'
righe_diz = [l for l in io.open(percorso_diz, encoding='utf-8').read().splitlines()
             if l.strip()]
voci = [json.loads(l) for l in righe_diz]

bersagli = [v for v in voci if v['firma'] == FIRMA]
if len(bersagli) != 1:
    raise SystemExit(f'attesa 1 voce con firma {FIRMA}, trovate {len(bersagli)}')
v = bersagli[0]
if v['riga'] != RIGA or v['en'] != '*' or v['it'] != '*':
    raise SystemExit(f'la voce non e\' quella attesa: {v!r}')

# --- il rinvio non c'e' gia' -----------------------------------------------

righe_rin = [l for l in io.open('rinviate.jsonl', encoding='utf-8').read().splitlines()
             if l.strip()]
if any(json.loads(l)['firma'] == FIRMA for l in righe_rin):
    raise SystemExit('rinvio gia\' presente: niente da fare')

# --- si compone tutto, e solo allora si scrive ------------------------------

diz_nuovo = [l for l, w in zip(righe_diz, voci) if w['firma'] != FIRMA]
if len(diz_nuovo) != len(righe_diz) - 1:
    raise SystemExit('tolte piu\' voci di una: fermo tutto')

rin_nuovo = righe_rin + [json.dumps({
    'firma': FIRMA,
    'file': FILE,
    'en': v['en'],
    'rinviata_a': 'nessuna fase: la lang() sta nel ramo `if ( jp )`',
    'motivo': MOTIVO,
}, ensure_ascii=False)]

dati_diz = ('\n'.join(diz_nuovo) + '\n').encode('utf-8')
dati_rin = ('\n'.join(rin_nuovo) + '\n').encode('utf-8')

with io.open(percorso_diz, 'wb') as f:
    f.write(dati_diz)
with io.open('rinviate.jsonl', 'wb') as f:
    f.write(dati_rin)

print(f'dizionario {FILE}: {len(righe_diz)} -> {len(diz_nuovo)} voci')
print(f'rinviate.jsonl: {len(righe_rin)} -> {len(rin_nuovo)}')
