# -*- coding: utf-8 -*-
"""Scrive le rese di un modulo RESE[riga] dentro il campo `it` di un lotto.

    python scratchpad/_85-applica-rese.py <modulo.py> <lotto.jsonl>

Rifiuta di scrivere se il modulo non copre esattamente le righe del lotto.
"""
import importlib.util
import io
import json
import sys


def main() -> int:
    modulo, lotto = sys.argv[1], sys.argv[2]
    spec = importlib.util.spec_from_file_location('rese', modulo)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    voci = [json.loads(l) for l in io.open(lotto, encoding='utf-8') if l.strip()]
    righe = {v['riga'] for v in voci}
    if righe != set(m.RESE):
        print('perimetro diverso: mancanti %s, in piu %s'
              % (sorted(righe - set(m.RESE)), sorted(set(m.RESE) - righe)))
        return 1

    with io.open(lotto, 'w', encoding='utf-8', newline='\n') as fh:
        for v in voci:
            v['it'] = m.RESE[v['riga']]
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese scritte in %s' % (len(voci), lotto))
    return 0


if __name__ == '__main__':
    sys.exit(main())
