# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl le tre voci del menu d'uscita che stanno nel blocco
ORIGINAL spento e non rivivono nel blocco che il mod ha messo al suo posto.

⚠️ Le altre due dello stesso blocco — `:17285` 「ゲーム設定」 e `:17296`
「無事に記録された。」 — NON si rinviano: la stessa firma torna a `:17316` e
`:17330`, dentro il blocco vivo. E' il caso che ha fatto correggere la rete 6.
"""
import io
import json

MOTIVO = (
    "La riga sta nel blocco `ORIGINAL` che il mod ha spento, "
    "`command.hsp:17281`-`:17311`: il menu d'uscita e' stato riscritto in "
    "`ANNA/BLOODYSHADE CUSTOM` (`:17313`-`:17339`), che e' quello che gira. "
    "⚠️ **E la firma non rivive altrove**, che e' la differenza con le due "
    "sorelle dello stesso blocco: 「ゲーム設定」 (`:17285`) torna a `:17316` e "
    "「無事に記録された。」 (`:17296`) a `:17330`, e quelle si traducono. Qui no: "
    "il menu nuovo non ha piu' un si'/no — ha quattro voci con le proprie "
    "stringhe (「ゲームをやめる」, 「キャンセル」) — quindi 「はい」 e 「いいえ」 con "
    "l'inglese «Exit»/«Cancel» sono rimaste senza sito vivo. "
    "💡 `:17297` e' la gemella di `:17331` con i puntini di sospensione veri "
    "(…) invece dei tre punti: firma diversa, e la viva e' l'altra. "
    "✅ Sono le tre voci che hanno fatto correggere la rete 6, la quale "
    "guardava la riga d'ancoraggio invece della firma e le bocciava tutte e "
    "cinque."
)

NUOVE = [
    (17283, 'Exit'),
    (17284, 'Cancel'),
    (17297, 'You close your eyes and peacefully fade away. (Hit any key to exit)'),
]

# ⚠️ l'estrazione INTERA, non quella `--da-tradurre` (vedi rinvia-command-ramo-jp.py)
voci = {(v['riga'], v['en']): v
        for v in (json.loads(l) for l in io.open('lavoro/_command_tutto.jsonl', encoding='utf-8')
                  if l.strip())}

righe = []
for riga, en in NUOVE:
    if (riga, en) not in voci:
        raise SystemExit(f'chiave che non aggancia nessuna voce: {(riga, en)}')
    v = voci[(riga, en)]
    righe.append({
        'firma': v['firma'],
        'file': 'command.hsp',
        'en': v['en'],
        'rinviata_a': 'mai: dentro il blocco ORIGINAL spento, e la firma non rivive altrove',
        'motivo': MOTIVO,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    # ⚠️ si compone e si codifica prima di toccare il file (la 39a)
    dati = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove).encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
