# -*- coding: utf-8 -*-
"""Costruisce un lotto dalla ZONA (non da --da-tradurre, che mente sul perimetro).

    python scratchpad/_81-lotto.py <estrazione> <file.hsp> <uscita> da a [da a ...]
"""
import io, json, sys, collections

def main():
    est, nomefile, uscita = sys.argv[1], sys.argv[2], sys.argv[3]
    n = sys.argv[4:]
    zone = [(int(n[i]), int(n[i+1])) for i in range(0, len(n), 2)]
    dentro = lambda r: any(a <= r <= b for a, b in zone)

    voci = [json.loads(l) for l in io.open(est, encoding='utf-8') if l.strip()]
    rese = set()
    try:
        for l in io.open('dizionario/%s.jsonl' % nomefile, encoding='utf-8'):
            if l.strip():
                v = json.loads(l)
                if v.get('it', '').strip():
                    rese.add(v['firma'])
    except FileNotFoundError:
        pass

    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v)

    scelte = []
    for f, vs in per_firma.items():
        d = [v for v in vs if dentro(v['riga'])]
        if not d or f in rese:
            continue
        scelte.append(min(d, key=lambda v: (v['riga'], v['occorrenza'])))
    scelte.sort(key=lambda v: (v['riga'], v['occorrenza']))

    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in scelte:
            v = dict(v)
            v['it'] = ''
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d voci in %s' % (len(scelte), uscita))
    return 0

sys.exit(main())
