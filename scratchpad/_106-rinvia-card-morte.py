# -*- coding: utf-8 -*-
"""106a - le due righe spente della carta CREATURE_ID_HARD_GAY (`db_card.hsp`).

⚠️ Sono la PRIMA famiglia di riga morta del progetto, il `;`, e stanno tutt'e due
nello stesso blocco: `:11405` (la prosa) e `:11412` (il nome). Monte ha spento la
carta originale e le ha rimpiazzate una riga sotto — `:11406` e `:11413` — con
l'`エクスプロージョマン`, «l'uomo esplosivo», che e' la carta viva.
"""
import io
import json

MOTIVO = (
    "Riga spenta con `;` nel sorgente. `db_card.hsp:11403` apre il blocco di "
    "`CREATURE_ID_HARD_GAY`, e dentro il blocco monte ha commentato **due** "
    "righe — `:11405` la prosa e `:11412` il nome — sostituendole subito sotto "
    "con `:11406` e `:11413`, cioe' con `エクスプロージョマン` / `explosioman`, "
    "«l'uomo esplosivo». La carta e' la stessa, il testo che il giocatore legge "
    "e' quello nuovo: le due righe vecchie non le compila nessuno. "
    "⚠️ La rete 6 del lotto le ferma da sola, e lo fa guardando la FIRMA e non "
    "la riga; qui pero' entrambe le occorrenze della firma sono spente, quindi "
    "il rinvio e' definitivo e non un aggiramento."
)

NUOVE = [
    (11405, 'It was designated a hard gay species because it was the hardest of the gay '
            'species. They have a habit of being attracted to muscular muscles. The '
            'existence of soft gay species is debated in academic circles.'),
    (11412, 'hard gay'),
]

voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for k in NUOVE:
    if k not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {k}')
    v = voci[k]
    righe.append({
        'firma': v['firma'],
        'file': 'db_card.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: riga spenta con `;` nel sorgente, rimpiazzata una riga sotto',
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
