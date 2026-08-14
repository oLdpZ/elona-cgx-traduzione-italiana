# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl i due nomi di nave di proc.hsp:5584, che non sono
testo ma operandi di confronto con map.hsp."""
import io, json

MOTIVO = (
    "Non e' testo, e' un operando di confronto fra due file, ed e' la seconda "
    "volta in `proc.hsp` dopo «Party Room» della 27ª. `map.hsp` ASSEGNA il nome "
    "della mappa — `mdatan(0) = lang(\"商船内部\", \"Merchant ship\")` a "
    "`map.hsp:4087`, `mdatan(0) = lang(\"海賊船内部\", \"Pirate ship\")` a "
    "`:4099`, e `mdatan(MDATAN_NAME) = lang(...)` a `:8291` — e `proc.hsp` lo "
    "CONFRONTA in due siti, `:5584` e `:5685`, per sapere se stai scavando "
    "dentro una nave: li' il bottino diventa spazzatura, schegge di legno e "
    "legname invece di minerali. Tradurre solo il confronto lo fa fallire per "
    "sempre, in silenzio, e nessuna guardia lo vede perche' `map.hsp` non e' nel "
    "dizionario e ogni strumento misura un file solo (vedi "
    "coerenza-fra-due-file-uno-solo-tracciato). Va tradotto INSIEME a "
    "`map.hsp`, come `evold`/`evname` con `db_creature.hsp`: non prima. "
    "⚠️ Da qui la rete 7 dello script del lotto, che muore se la riga di una "
    "voce contiene `==` o `!=` prima della `lang()`."
)

NUOVE = [(5584, 'Merchant ship'), (5584, 'Pirate ship')]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'proc.hsp',
        'en': v['en'],
        'rinviata_a': 'con map_.hsp (map.hsp:4087, :4099, :8291)',
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
