# -*- coding: utf-8 -*-
"""Lotto fase4-chips-001: i nomi delle caselle di terreno (chips.hsp 833-835).

Tre voci, ed e' tutto il file. Trovate a schermo il 2026-08-14: escono da
`action.hsp:2681`, dentro una frase gia' tradotta, e a schermo si leggeva
«a field si trova ai tuoi piedi.» — meta' inglese e meta' italiana, a ogni passo
mentre si coltiva.

⚠️ **Il codice arbitra**, non l'inglese:
  - DRYROCK (日干し岩): al ranch, col bel tempo, quel che ci lasci sopra si secca;
    un cadavere diventa carne secca (`item.hsp:1819-1835`);
  - CROP (畑の土): la casella dove si semina (`action.hsp:18815`);
  - COMPOST (コンポスト): materia grezza, trucioli e rifiuti ci diventano
    fertilizzante organico (`map.hsp:12313-12321`).

💡 **Due rese su tre sono copie, non invenzioni** — il progetto le aveva gia'
decise altrove, e la regola «cercare prima di scrivere» qui ha reso due volte su
tre:
  - `action.hsp` «You can not fertilize non-field tiles.» -> «Si concima solo
    **il campo coltivato**.»
  - `action.hsp` «The composite only works in Crop properties» -> «Il **compost**
    funziona solo nei campi di tua proprieta'.»
  - la famiglia dell'essiccazione e' gia' `pesce essiccato` / `verdura essiccata`
    in `db_item.hsp`.

⚠️ Ogni resa porta il proprio articolo, perche' l'inglese lo porta (`a field`) e
la frase che le ospita non ne mette: `tname(p) + " si trova ai tuoi piedi."`.
⚠️ `sdim tname, 16` da' 16 byte a voce e la piu' lunga ne occupa 26. Per la
scoperta 2 della 28ª `sdim` non e' un tetto in scrittura su un array a una
dimensione — la controprova e' `sdim buffname, 20` col giapponese da 22 — ma va
guardato a schermo.
"""
import collections, glob, io, json

RESE = {
    # 日干し岩 — la roccia dove si essicca al sole. «essiccazione» tiene la
    # famiglia gia' decisa in db_item.hsp (pesce essiccato, verdura essiccata).
    (833, 'a dryrock'): 'una pietra da essiccazione',
    # 畑の土 — copiata da action.hsp, «Si concima solo il campo coltivato.»
    (834, 'a field'): 'un campo coltivato',
    # コンポスト — copiata da action.hsp, «Il compost funziona solo nei campi».
    # Partitivo: e' un mucchio, non un oggetto numerabile.
    (835, 'a compost'): 'del compost',
}

USCITA = 'lavoro/fase4-chips-001.jsonl'

tutte = [json.loads(l) for l in io.open('lavoro/_chips.jsonl', encoding='utf-8') if l.strip()]

errori = []
# rete 0: la chiave (riga, en) identifica una voce sola
for k, n in collections.Counter((v['riga'], v['en']) for v in tutte).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in tutte}
# rete 1: nessuna voce senza resa
for v in tutte:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
# rete 2: nessuna resa che non aggancia niente
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2')

# rete 3: divergenza da una resa gia' decisa per lo stesso giapponese.
# Stampa, non uccide: la resa vecchia potrebbe essere quella sbagliata.
gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in tutte:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it != resa:
            print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
                  f"      qui      {resa!r}\n"
                  f"      {nome}:{riga}  {it!r}")

# rete 4: lo stesso giapponese reso in due modi dentro il lotto
per_jp = collections.defaultdict(set)
for v in tutte:
    per_jp[v['jp']].add(RESE[(v['riga'], v['en'])])
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi: {rese}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in tutte:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(tutte)} voci in {USCITA}')
for v in tutte:
    print(f"  {v['riga']}  {v['jp']:<8} {v['en']:<12} -> {v['it']}")
