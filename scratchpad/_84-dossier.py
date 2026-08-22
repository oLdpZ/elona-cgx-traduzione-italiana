# -*- coding: utf-8 -*-
"""Il dossier di un lotto: per ogni voce, giapponese + inglese + tutte le sue
occorrenze nel file, e per quelle FUORI dalla zona anche la riga di codice.

    python scratchpad/_84-dossier.py <lotto.jsonl> <estrazione> da a [da a ...]
"""
import io, json, sys, collections

SORG = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chat.hsp'


def main():
    lotto, est = sys.argv[1], sys.argv[2]
    n = sys.argv[3:]
    zone = [(int(n[i]), int(n[i + 1])) for i in range(0, len(n), 2)]
    dentro = lambda r: any(a <= r <= b for a, b in zone)

    righe = io.open(SORG, encoding='cp932', errors='replace').read().split('\n')
    voci = [json.loads(l) for l in io.open(est, encoding='utf-8') if l.strip()]
    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v['riga'])

    for l in io.open(lotto, encoding='utf-8'):
        if not l.strip():
            continue
        v = json.loads(l)
        occ = sorted(set(per_firma[v['firma']]))
        fuori = [r for r in occ if not dentro(r)]
        print('=== %s  riga %d  [%s]' % (v['firma'], v['riga'], v.get('classe', '?')))
        print('  JP  %s' % v.get('jp', ''))
        print('  EN  %s' % v.get('en', ''))
        if v.get('espressione'):
            print('  ESP %s' % v['espressione'])
        if len(occ) > 1:
            print('  occorrenze: %s' % ' '.join(str(r) for r in occ))
        for r in fuori:
            print('  ⚠ FUORI  %d: %s' % (r, righe[r - 1].strip()[:200]))
        print()
    return 0


sys.exit(main())
