# -*- coding: utf-8 -*-
"""Le voci GIA' RESE con almeno un'occorrenza in una zona: il registro del
parlante si legge, non si decide.

    python scratchpad/_84-gia-rese.py <estrazione> <file.hsp> da a [da a ...]
"""
import io, json, sys, collections


def main():
    est, nomefile = sys.argv[1], sys.argv[2]
    n = sys.argv[3:]
    zone = [(int(n[i]), int(n[i + 1])) for i in range(0, len(n), 2)]
    dentro = lambda r: any(a <= r <= b for a, b in zone)

    voci = [json.loads(l) for l in io.open(est, encoding='utf-8') if l.strip()]
    diz = {}
    for l in io.open('dizionario/%s.jsonl' % nomefile, encoding='utf-8'):
        if l.strip():
            v = json.loads(l)
            if v.get('it', '').strip():
                diz[v['firma']] = v

    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v['riga'])

    scelte = []
    for f, rr in per_firma.items():
        d = [r for r in rr if dentro(r)]
        if d and f in diz:
            scelte.append((min(d), diz[f]))
    scelte.sort()
    for riga, v in scelte:
        print('%6d  EN %s' % (riga, (v.get('en_grezzo') or v.get('en', ''))[:170]))
        print('        IT %s' % v['it'][:200])
    print()
    print('%d voci gia\' rese nella zona' % len(scelte))
    return 0


sys.exit(main())
