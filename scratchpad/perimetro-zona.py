# -*- coding: utf-8 -*-
"""Il perimetro VERO di una zona: firme non tradotte con almeno un'occorrenza
dentro la zona, piu' le loro occorrenze FUORI (che e' quel che `--da-tradurre`
nasconde, ancorando la firma alla prima occorrenza del file).

    python scratchpad/perimetro-zona.py <estrazione.jsonl> <file.hsp> da a [da a ...]

La 78a: `*chat_default` mostrava 77 voci e le firme vere erano 89.
"""
import io, json, sys, collections


def main() -> int:
    est, nomefile = sys.argv[1], sys.argv[2]
    n = sys.argv[3:]
    zone = [(int(n[i]), int(n[i + 1])) for i in range(0, len(n), 2)]

    voci = [json.loads(l) for l in io.open(est, encoding='utf-8') if l.strip()]
    dizf = 'dizionario/%s.jsonl' % nomefile
    rese = set()
    try:
        for l in io.open(dizf, encoding='utf-8'):
            if l.strip():
                v = json.loads(l)
                if v.get('it', '').strip():
                    rese.add(v['firma'])
    except FileNotFoundError:
        pass

    def dentro(r):
        return any(a <= r <= b for a, b in zone)

    per_firma = collections.defaultdict(list)
    for v in voci:
        per_firma[v['firma']].append(v)

    dentro_firme = {f for f, vs in per_firma.items() if any(dentro(v['riga']) for v in vs)}
    da_fare = sorted(dentro_firme - rese,
                     key=lambda f: min(v['riga'] for v in per_firma[f] if dentro(v['riga'])))

    occ_tot = sparse = 0
    for f in da_fare:
        vs = per_firma[f]
        fuori = [v for v in vs if not dentro(v['riga'])]
        occ_tot += len(vs)
        if fuori:
            sparse += 1
    print('zone: %s' % ' '.join('%d-%d' % z for z in zone))
    print('firme con almeno un\'occorrenza dentro : %d' % len(dentro_firme))
    print('  gia\' rese                           : %d' % len(dentro_firme & rese))
    print('  DA FARE (il perimetro vero)          : %d' % len(da_fare))
    print('  di cui con occorrenze anche FUORI    : %d  <- quelle che --da-tradurre puo\' nascondere' % sparse)
    print('occorrenze totali delle firme da fare  : %d' % occ_tot)
    print()
    for f in da_fare:
        vs = sorted(per_firma[f], key=lambda v: (v['riga'], v['occorrenza']))
        d = [v for v in vs if dentro(v['riga'])]
        fu = [v for v in vs if not dentro(v['riga'])]
        marca = '  FUORI ANCHE: ' + ', '.join('%d' % v['riga'] for v in fu[:6]) if fu else ''
        print('--- %s  righe %s%s' % (f[:8], ','.join(str(v['riga']) for v in d[:6]), marca))
        print('    [%s] EN %s' % (vs[0]['tipo'], vs[0]['en_grezzo'][:160]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
