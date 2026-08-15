# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl `command.hsp:10825`, dentro un blocco spento."""
import io
import json

MOTIVO = (
    "command.hsp:10825. Riga dentro un commento di **BLOCCO** — "
    "`/********** ORIGINAL - BEGINNING **********` a `:10817`, chiuso da "
    "`********** ORIGINAL - ENDING **********/` a `:10827` — cioe' la versione "
    "di monte del piede della scheda del personaggio, che il mod ha sostituito "
    "col blocco `ANNA CUSTOM` di `:10829`-`:10839`. La riga viva e' `:10837`, "
    "che ha lo **stesso giapponese** 「説明:」 e un inglese diverso (`Desc:` "
    "invece di `Hint:`), ed e' resa «Info:» nel lotto `fase4-command-003`. "
    "⭐ **E il rinvio non e' solo igiene: senza, la rete 4 avrebbe preteso una "
    "resa sola per tutt'e due** — lo stesso giapponese non puo' avere due rese "
    "— cioe' un vincolo sulla riga viva imposto da testo morto. E' la prima "
    "volta che una rinviata della rete 6 toglie di mezzo un vincolo della rete "
    "4 invece di limitarsi a saltare una riga. "
    "Non c'e' toppa da fare: non e' un difetto a schermo, e' testo morto."
)

NUOVE = [(10825, 'Hint:')]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'command.hsp',
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
    testo = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove)
    dati = testo.encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
