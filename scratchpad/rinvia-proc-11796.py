# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl `proc.hsp:11796`, che sta dentro un blocco spento."""
import io
import json

MOTIVO = (
    "La riga sta dentro un commento di BLOCCO — "
    "`/********** ORIGINAL - BEGINNING ********** // Remove skill bonus limit.` "
    "a `proc.hsp:11776`, chiuso da `********** ORIGINAL - ENDING **********/` a "
    "`:11799` — cioe' il codice di monte che il mod ha spento per togliere il "
    "tetto di 100 ai punti bonus incantesimi. Il giocatore non leggera' mai "
    "questa riga: le uniche righe vive di quel tratto sono `:11773` (il "
    "messaggio che i 5 punti li da') e `:11787` (il `+= 5` che li assegna). "
    "E' la stessa classe di `:4958`, il blocco `MANUSCRIPT HINT` del lotto 006, "
    "ma in una forma che la rete 6 NON vedeva: quella guardava solo le righe che "
    "cominciano per `;`. ⚠️ Da qui la rete 6 allargata ai blocchi `/* ... */` "
    "(`scratchpad/commenti-blocco.py`) e la misura sul dizionario intero: 7 voci "
    "gia' tradotte stanno dentro un blocco spento — 6 in `action.hsp` e "
    "`proc.hsp:1000`, la versione originale dell'incasso delle esibizioni che il "
    "blocco `ANNA CUSTOM` ha sostituito. Non c'e' toppa da fare: non e' un "
    "difetto a schermo, e' testo morto."
)

NUOVE = [(11796, 'Caution! While the spell bonus is 100 or more, you cannot get new.')]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'proc.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: riga dentro un blocco /* ... */ spento dal mod',
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
