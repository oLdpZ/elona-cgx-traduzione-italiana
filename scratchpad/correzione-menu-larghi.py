# -*- coding: utf-8 -*-
"""Le tre voci di menu che la rete 5 ha visto appena ha smesso di guardare solo text.hsp.

Il 2026-08-18 (60ª) `larghezze.py` ha preso la seconda strada — i 92 siti di
`*prompt_key` che non passano da `text.hsp`, con 261 voci dentro — e al primo
giro ne ha trovate **tre** gia' rese che sforano il riquadro. Nessuna delle tre
era mai stata guardata da nessuno.

    action.hsp:7814    350px, tetto 39   44 caratteri
    action.hsp:7816    350px, tetto 39   47 caratteri
    command.hsp:17535  240px, tetto 25   26 caratteri

⚠️ **E la seconda non era solo lunga: aveva la parola di un'altra cosa.**
`Spellbook` e' reso **grimorio** in tutto il progetto — 167 rese, tutte in
`db_item.hsp` — e `action.hsp:7816` era l'unico posto che diceva «libri
magici». La rete della larghezza ha trovato una divergenza di vocabolario, che
non e' il suo mestiere: e' quel che succede quando una rete nuova guarda righe
che nessuna rete guardava.

⚠️ **Il contrario per la terza**: «PNG personalizzato» e' il termine fissato, e
sta in tre siti (`command.hsp:7615`, `:7799`, `:17535`). Li' si tocca il
contorno — l'articolo — non il termine.

✅ **La misura dice anche che l'inglese ci sta per un pelo**: «Manuscript
production (999 inspiration) » fa 40 caratteri in un tetto da 39, e il
quarantesimo e' lo spazio in coda. Upstream ha speso l'ultimo carattere che
aveva, e questo e' il segno che il modello del riquadro e' giusto.

⚠️ Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura, per la ragione scritta in `LEGGIMI.md`.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti.larghezze import budget, menu_diretti, reso

CORREZIONI = {
    'dizionario/action.hsp.jsonl': {
        # 44 caratteri su 39: la resa nomina due volte quel che il menu fa
        7814: ('"Scrittura di manoscritti (ispirazione: "'
               ' + gdata(GDATA_FLAG_MANUSCRIPT_IDEAS) + ") "',
               '"Scrittura (ispirazione: "'
               ' + gdata(GDATA_FLAG_MANUSCRIPT_IDEAS) + ") "'),
        # 47 su 39, e «libri magici» dove il progetto dice grimorio da sempre
        7816: ('Conversione di libri magici (dimezza le copie) ',
               'Conversione di grimori (metà copie) '),
    },
    'dizionario/command.hsp.jsonl': {
        # 26 su 25: il termine resta, se ne va l'articolo
        17535: ('Crea un PNG personalizzato', 'Crea PNG personalizzato'),
    },
}

# rete 0: ogni resa nuova deve stare nel tetto del SUO riquadro, misurato dalla
# rete e non scritto qui a mano
diretti = menu_diretti()
for percorso, correzioni in CORREZIONI.items():
    nome_file = percorso.split('/')[-1][: -len('.jsonl')]
    for riga, (_, nuova) in correzioni.items():
        px = diretti.get((nome_file, riga))
        if px is None:
            sys.exit(f'rete 0: {nome_file}:{riga} non e\' in nessun riquadro misurato')
        tetto, testo = budget(px), reso(nuova)
        if len(testo) > tetto:
            sys.exit(f'rete 0: {nome_file}:{riga} fa {len(testo)} caratteri, '
                     f'il tetto e\' {tetto}: {testo!r}')
        print(f'rete 0: {nome_file}:{riga} {len(testo)}/{tetto} caratteri  {testo!r}')

fatte, saltate, corrette, da_scrivere = 0, 0, [], {}
for percorso, correzioni in CORREZIONI.items():
    righe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]
    viste = set()
    for d in righe:
        if d['riga'] not in correzioni:
            continue
        vecchia, nuova = correzioni[d['riga']]
        viste.add(d['riga'])
        if d.get('it') == nuova:
            saltate += 1
            continue
        # rete 1: si corregge solo quello che dice ancora la resa vecchia
        if d.get('it') != vecchia:
            sys.exit(f"rete 1: {percorso}:{d['riga']} non dice la resa attesa "
                     f"ma {d.get('it')!r}")
        print(f"{percorso.split('/')[-1]}:{d['riga']}\n    {d['it']}\n -> {nuova}")
        d['it'] = nuova
        corrette.append(dict(d))
        fatte += 1
    # rete 2: nessuna correzione deve restare senza voce
    if viste != set(correzioni):
        sys.exit(f'rete 2: correzioni senza voce -> {sorted(set(correzioni) - viste)}')
    # ⚠️ si compone e si codifica PRIMA di aprire il file in scrittura
    da_scrivere[percorso] = ''.join(
        json.dumps(d, ensure_ascii=False) + '\n' for d in righe).encode('utf-8')

# rete 3: le rese nuove devono passare `verifica` come se fossero un lotto
if corrette:
    from strumenti.verifica import controlla_lotto
    problemi = controlla_lotto(corrette)
    if problemi:
        for chiave, elenco in problemi.items():
            print(f'rete 3: {chiave}: ' + '; '.join(elenco))
        sys.exit('le rese nuove non passano verifica')
    print(f'rete 3: {len(corrette)} rese nuove passano verifica')

for percorso, dati in da_scrivere.items():
    with io.open(percorso, 'wb') as f:
        f.write(dati)

print(f"--- {fatte} rese corrette, {saltate} gia' a posto")
