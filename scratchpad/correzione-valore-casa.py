# -*- coding: utf-8 -*-
"""La voce di menu e la finestra che apre non si chiamavano allo stesso modo.

    map_user.hsp:489   voce di menu, en «Home rank»   -> «Informazioni sulla casa»
    map_user.hsp:749   titolo della finestra, en «Home Value» -> «Valore della casa»

Il **giapponese e' lo stesso**, 家の情報, e la rete 3 lo ha detto appena il lotto
003 ha reso il titolo. E' esattamente il difetto della 52a — la voce di menu
diceva «Regolazioni» e il pannello «Ritocchi» — trovato pero' da una rete invece
che da una schermata, perche' li' i due giapponesi erano diversi e qui no.

⚠️ **A dividerle era stato l'inglese di monte**, che chiama la stessa finestra
«Home rank» dalla porta e «Home Value» dentro. Il giapponese non fa questa
distinzione, e la finestra mostra un valore in monete: quel che ci sta scritto
dentro decide, e si allinea la porta.

💡 La finestra elenca 価値 / 家宝ランク / 基本 / 家具 / 家宝 / 総合: e' il valore
della casa scomposto. «Informazioni» prometteva una scheda che non c'e'.

⚠️ Lo script compone e valida tutto in memoria prima di aprire un file in
scrittura, per la ragione scritta in `LEGGIMI.md`.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti.larghezze import budget, menu_diretti, reso

NUOVA = 'Valore della casa'

CORREZIONI = {
    'dizionario/map_user.hsp.jsonl': {
        489: ('Informazioni sulla casa', NUOVA),
    },
}

# rete 0: la resa nuova deve stare nel riquadro del menu, misurato dalla rete
px = menu_diretti()[('map_user.hsp', 489)]
if len(reso(NUOVA)) > budget(px):
    sys.exit(f'rete 0: {NUOVA!r} fa {len(reso(NUOVA))} caratteri, '
             f'il tetto e\' {budget(px)}')
print(f'rete 0: {NUOVA!r} {len(reso(NUOVA))}/{budget(px)} caratteri')

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
