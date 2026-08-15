# -*- coding: utf-8 -*-
"""Aggiunge a rinviate.jsonl `command.hsp:12636`, morta in TUTTI E QUATTRO i siti.

⚠️ E' il primo rinvio del progetto in cui la firma non e' spenta «qui e viva
altrove», ma spenta **ovunque sia scritta**. La rete 6 corretta nella 45a — che
boccia solo quando sono spente tutte le occorrenze — l'ha bocciata, ed e'
esattamente il lavoro per cui era stata corretta. Provato prima di scrivere
questo file: senza il rinvio il lotto 032 si ferma con «rete 6: riga 12636 sta
dentro un commento di BLOCCO, va rinviata».
"""
import io
import json

MOTIVO = (
    "L'intestazione della colonna delle resistenze, 「火 冷 雷 闇 幻 毒 獄 音 神 沌 魔」, "
    "e' scritta in QUATTRO siti di `command.hsp` — `:12636`, `:12645`, `:14127` e "
    "`:14136` — e tutti e quattro stanno dentro un commento di blocco. I due "
    "dispari sono il blocco `ORIGINAL`; i due pari sono il blocco `ANNA CUSTOM`, "
    "che e' spento anche lui. "
    "⚠️ E che l'`ANNA CUSTOM` sia spento si vede da un carattere solo: `:12639` e' "
    "`/********** ANNA CUSTOM - BEGINNING ********** // Show skills on 'z' toggle`, "
    "**senza la barra finale**, e a chiuderlo e' `********** ANNA CUSTOM - ENDING "
    "**********/` a `:12670`. Dove il blocco e' vivo il marcatore porta la barra da "
    "tutt'e due i lati e apre e chiude sulla stessa riga, come `:12673` "
    "(`/********** MMAH - ENDING **********/`) e `:14118`. "
    "✅ A disegnare davvero le resistenze e' MMAH: `:12672` e' "
    "`display_show_resist showresist, 260 + (showresist == 1) * 100`, riga viva fra "
    "due marcatori autochiusi. Le due versioni di monte sono state **sostituite**, "
    "non spente per sbaglio, e il giocatore non leggera' mai questa `lang()`. "
    "⚠️ Se un giorno servisse rendere quell'intestazione, il posto non e' qui: e' "
    "dentro `display_show_resist`, e li' il vincolo sara' che le undici sigle "
    "devono restare di **due caratteri** con **uno spazio** in mezzo, perche' i "
    "valori sotto si incolonnano su quel passo."
)

NUOVE = [(12636, 'Fi Co Li Da Mi Po Nt So Nr Ch Ma')]

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
        'rinviata_a': 'mai: riga dentro un blocco /* ... */ spento, in tutti e quattro i siti',
        'motivo': MOTIVO,
    })

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
firme = {json.loads(l)['firma'] for l in esistenti}
nuove = [r for r in righe if r['firma'] not in firme]
if not nuove:
    print('gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in nuove).encode('utf-8')
    with io.open('rinviate.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(nuove)} rinviate aggiunte (totale {len(esistenti) + len(nuove)})')
