# -*- coding: utf-8 -*-
"""Disfa la resa di `command.hsp:15489` e la toppa sbagliata che le stava dietro.

⚠️⚠️ **Una toppa non puo' agganciarsi a una riga che il dizionario riscrive.**
`applica.py` fa girare le toppe **dopo** il dizionario (`applica.py:530`), quindi
la prima idea era scrivere `cerca` sulla riga gia' tradotta — e funziona in
build. Ma `strumenti/tests/test_toppe.py:104` pretende che **ogni toppa si
applichi al SORGENTE pinnato**, ed e' quella prova a rendere rosso il giorno in
cui upstream riscrive la riga. Una toppa agganciata al testo italiano non ha
piu' nessun rapporto col sorgente, e quella prova non varrebbe piu' niente.

✅ La forma giusta e' quella gia' scritta nella tabella di `LEGGIMI.md`: **rinvio
+ toppa insieme**, come `toppa-action-15221.py` e `toppa-proc-24107.py`. Il
rinvio toglie la voce dal dizionario, cosi' `applica` non tocca la riga, e la
toppa la riscrive tutta intera partendo dal sorgente.

Questo script fa i due passi che vanno disfatti: toglie l'ultima toppa da
`toppe.jsonl` e la voce `:15489` da `dizionario/command.hsp.jsonl`.
"""
import io
import json

MARCATORE = ' Guild Point)'
RIGA = 15489

# --- 1. la toppa sbagliata -------------------------------------------------
righe = [l for l in io.open('toppe.jsonl', encoding='utf-8').read().splitlines() if l.strip()]
tengo = [l for l in righe if MARCATORE not in json.loads(l)['cerca']]
tolte = len(righe) - len(tengo)
if tolte > 1:
    raise SystemExit(f'{tolte} toppe col marcatore: non e\' quella che ho scritto io')
if tolte:
    # ⚠️ si compone e si codifica prima di aprire (la 39a)
    dati = ('\n'.join(tengo) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'wb') as f:
        f.write(dati)
    print(f'toppa tolta: {len(righe)} -> {len(tengo)}')
else:
    print('nessuna toppa da togliere')

# --- 2. la voce di dizionario ----------------------------------------------
percorso = 'dizionario/command.hsp.jsonl'
voci = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
resta = [v for v in voci if v['riga'] != RIGA]
tolte_voci = len(voci) - len(resta)
if tolte_voci != 1:
    raise SystemExit(f'{tolte_voci} voci a riga {RIGA}: mi aspettavo una sola')
dati = ('\n'.join(json.dumps(v, ensure_ascii=False) for v in resta) + '\n').encode('utf-8')
with io.open(percorso, 'wb') as f:
    f.write(dati)
print(f'voce :{RIGA} tolta dal dizionario: {len(voci)} -> {len(resta)}')
