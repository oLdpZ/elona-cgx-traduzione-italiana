# -*- coding: utf-8 -*-
"""L'elenco compatto delle firme di un lotto: riga, giapponese, inglese.

Il dossier di `_107-dossier-item.py` e' fatto per essere letto una volta; questo
serve a **scrivere** le rese, cioe' a tenere sott'occhio riga e giapponese di
tutte le firme insieme, senza le sei righe di contorno per ciascuna.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-109/_elenco.py \
        scratchpad/lotti-109/righe005.py

⚠️ Legge il **lavoro** (`lavoro/_107-daitem.jsonl`), cioe' la stessa estrazione
da cui il lotto prende le firme: se leggesse il dossier potrebbe selezionare in
modo diverso, che e' esattamente cio' che `--righe` esiste per impedire.
"""
import collections
import importlib.util
import io
import json
import os
import sys

LAVORO = 'lavoro/_107-daitem.jsonl'


def carica_righe(percorso):
    spec = importlib.util.spec_from_file_location('righe', percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.RIGHE


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    righe = carica_righe(sys.argv[1])
    voci = [json.loads(l) for l in io.open(LAVORO, encoding='utf-8') if l.strip()]
    zona = [v for v in voci if v['riga'] in righe]

    # quante firme condividono lo stesso giapponese: e' il numero che dice
    # quante rese saranno per forza identiche
    per_jp = collections.Counter(v['jp'] for v in zona)

    for v in sorted(zona, key=lambda v: v['riga']):
        jp = v['jp'].replace('\\t', '').replace('\\n', ' ⏎ ').strip()
        # la riga di categoria del rapporto non serve a chi traduce: e' fissa
        jp = jp.split('⏎')[0].strip()
        gemelle = per_jp[v['jp']]
        marchio = f'  ×{gemelle}' if gemelle > 1 else ''
        print(f"{v['riga']:>7}{marchio}")
        print(f"    JP {jp}")
        print(f"    EN {v['en']}")

    print()
    print(f'{len(zona)} firme, {len(per_jp)} giapponesi distinti; '
          f'{sum(1 for n in per_jp.values() if n > 1)} giapponesi condivisi')
    mancanti = righe - {v['riga'] for v in zona}
    if mancanti:
        sys.exit(f'⚠️ righe dichiarate ma non trovate nel lavoro: {sorted(mancanti)}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
