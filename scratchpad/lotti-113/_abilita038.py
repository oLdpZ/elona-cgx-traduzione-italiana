# -*- coding: utf-8 -*-
"""115a - I nomi delle abilita' come il giocatore li vede, presi da `skill.hsp`.

Le descrizioni degli scarti nominano di continuo coppie di abilita' («la sua
potenza dipende da X e Y»), e quei nomi sono gia' decisi: stanno in
`dizionario/skill.hsp.jsonl`. Cercarli a mano uno per uno e' il modo di
sbagliarne uno.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_abilita038.py 宝石細工 生化学
"""
import glob
import io
import json
import sys

DIZIONARI = 'dizionario/*.jsonl'


def main():
    volute = sys.argv[1:]
    trovate = {}
    for f in glob.glob(DIZIONARI):
        for r in io.open(f, encoding='utf-8'):
            d = json.loads(r)
            jp = d.get('jp') or ''
            for v in volute:
                if jp == v:
                    trovate.setdefault(v, []).append(
                        (f.replace('dizionario\\', '').replace('dizionario/', ''),
                         d.get('en'), d.get('it')))
    for v in volute:
        righe = trovate.get(v)
        if not righe:
            print('%-10s  ⚠️ NON C\'E\' come voce intera' % v)
            continue
        for f, en, it in righe:
            print('%-10s  %-22s  %-24s  %s' % (v, f, en, it))


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
