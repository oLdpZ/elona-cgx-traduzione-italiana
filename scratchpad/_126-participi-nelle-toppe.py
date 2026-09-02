# -*- coding: utf-8 -*-
"""Le due rese al maschile che il referto delle toppe ha trovato appena acceso.

`_126-referti-toppe.py` gira sulle toppe i due referti che `referti.py` gira sul
dizionario, e alla prima passata ha trovato **due participi maschili riferiti al
giocatore**, che in Elona puo' essere donna. Non erano rese di oggi: stavano li'
da sessioni vecchie, dietro una catena tutta verde, perche' nessuna rete leggeva
le toppe.

⭐ **E il rimedio e' quello della 125a: si toglie il participio, non si aggiunge
una perifrasi.** Tutt'e due si risolvono con un sostantivo, e il testo ci
guadagna in brevita'.

    command.hsp        «Come sei andato finora:»        -> «Il tuo cammino finora:»
    custom_tweaks.hsp  «in base a come sei andato»      -> «in base al risultato»

ⓘ Sull'intestazione del diario la larghezza conta — il libro e' 736x448 con due
colonne da 306 px — e la resa nuova ha **gli stessi 22 caratteri** di quella
vecchia. Sull'altra la riga si accorcia di sette.

ⓘ Il giapponese dell'intestazione e' 「これまでのあなた」, «tu fino a qui»: e' un
cammino, non un tabellone di statistiche, e il sostantivo lo dice meglio del
participio.

⚠️ Si compone tutto in memoria e si riscrive il file alla fine: regola della 39a.
"""
import io
import json
import os

_PROGETTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PERCORSO = os.path.join(_PROGETTO, 'toppe.jsonl')

# (file, prima, dopo)
CORREZIONI = [
    ('command.hsp', 'Come sei andato finora:', 'Il tuo cammino finora:'),
    ('custom_tweaks.hsp', 'in base a come sei andato.', 'in base al risultato.'),
]


def righe(valore):
    return list(valore) if isinstance(valore, list) else [valore]


toppe = [json.loads(l) for l in io.open(PERCORSO, encoding='utf-8') if l.strip()]

for nome, prima, dopo in CORREZIONI:
    colpite = 0
    for toppa in toppe:
        if toppa['file'] != nome:
            continue
        valore = toppa['sostituisci']
        if isinstance(valore, list):
            if not any(prima in r for r in valore):
                continue
            toppa['sostituisci'] = [r.replace(prima, dopo) for r in valore]
        else:
            if prima not in valore:
                continue
            toppa['sostituisci'] = valore.replace(prima, dopo)
        colpite += 1
    if colpite != 1:
        raise SystemExit(f'{nome}: {prima!r} trovata in {colpite} toppe, attesa 1')

for toppa in toppe:
    for r in righe(toppa['sostituisci']):
        r.encode('cp932')

testo = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe)
io.open(PERCORSO, 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{len(CORREZIONI)} rese corrette in {len(toppe)} toppe')
