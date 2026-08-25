# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl i due selettori di `custom_autopick.hsp` spenti da `//`."""
import io
import json

MOTIVO = (
    "La riga e' spenta da un commento di riga `//`, e questa e' la QUINTA "
    "famiglia di riga morta del progetto — dopo il `;`, il blocco `/* ... */`, "
    "il ramo `if ( jp )` e l'`if ( 0 )`. ⚠️⚠️ HSP3 accetta **due** commenti di "
    "riga e il progetto ne ha sempre guardato uno solo: fino alla 100a la rete 6 "
    "chiedeva `lstrip().startswith(';')` e basta, quindi questi due selettori "
    "— ` zombie ` (腐りきった) e ` dragon's ` (ドラゴンの), che monte ha tenuto "
    "scritti ma spenti a `custom_autopick.hsp:200`-`:217` — sarebbero stati "
    "tradotti come se fossero vivi. ✅ Misurata prima di correggere la rete "
    "(`scratchpad/_100-commento-barre.py`): **9 righe** con una `lang()` dopo un "
    "`//` in tutto il sorgente, di cui **una gia' tradotta**, "
    "`command.hsp:17515` — «This function is disabled in wizard mode.», lavoro "
    "speso su testo che il giocatore non legge. La regola sta ora in "
    "`strumenti/commenti.py` con tre test, e la rete 6 la usa in "
    "`scratchpad/modello-rete6-barre.py`. Non c'e' toppa da fare: non e' un "
    "difetto a schermo, e' testo morto."
)

NUOVE = [(200, ' zombie '), (207, ' zombie '),
         (210, " dragon's "), (217, " dragon's ")]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_custom_autopick.jsonl',
                                                 encoding='utf-8') if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'custom_autopick.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: riga spenta da un commento di riga `//`',
        'motivo': MOTIVO,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    with io.open('rinviate.jsonl', 'a', encoding='utf-8', newline='\n') as f:
        for r in nuove:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
