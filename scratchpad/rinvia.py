# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl le tre code di frase di proc.hsp 3376/3383/3389."""
import io, json

MOTIVO = (
    "Coda di una frase la cui TESTA sta fuori da `lang()`. `proc.hsp:3372` e' "
    "`txt \"\\\"You are awesome!\", \"\\\"Oh my god...\", \"\\\"Okay, okay, you win!\", "
    "\"\\\"Holy...!\"` dentro un blocco `if ( en )`, con letterali **nudi**: "
    "estrai.py non li vede, quindi non sono nel dizionario. La frase che il "
    "giocatore legge e' la testa di :3372 piu' la coda di :3376 (se il bersaglio "
    "e' il giocatore), :3383 o :3389. Rendere la sola coda darebbe "
    "«\"You are awesome!Ecco, prendi questi.» ⚠️ Non e' un caso isolato: "
    "`proc.hsp` ha **23 righe** con letterali inglesi nudi dentro `if ( en )`, "
    "ognuna con piu' stringhe (scratchpad/blocchi_en.py le elenca). E' la stessa "
    "classe della scoperta 1 della 28ª su `bufftxt`, e come li' la strada e' una "
    "toppa, non una resa: il lavoro strutturale va fatto PRIMA delle rese e non "
    "dentro un lotto. Rinviate insieme a quella toppa."
)

NUOVE = [(3376, '\\"'), (3383, 'Here, take this.\\"'),
         (3389, "Take this money, it's all I have!\\\"")]

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
        'rinviata_a': 'con la toppa sui blocchi `if ( en )` di proc.hsp',
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
