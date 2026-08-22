# -*- coding: utf-8 -*-
"""Il lotto di correzione dei quattro siti che portavano `cnvrank` nella resa.

`cnvrank` e' la desinenza ordinale inglese (init.hsp:149: `if ( jp ) return ""
+ rank`, altrimenti `st`/`nd`/`rd`/`th`). Dalla 85a e' dichiarata morfologia in
`funzioni.MORFOLOGIA_INGLESE`, quindi la resa concatena l'argomento nudo — e
quando l'argomento e' un'espressione va fra PARENTESI, perche' HSP valuta senza
precedenza fra gli operatori (provato al banco: `_85-banco-cnvrank.py`).
"""
import io
import json
import os
import sys
from pathlib import Path

NUOVE = {
    ('command.hsp', 2911):
        '"Arena EX: " + gdata(GDATA_EX_BATTLE_WIN) + " vittorie  livello massimo "'
        ' + gdata(GDATA_EX_BATTLE_MAX_LVL)',
    ('main.hsp', 4067):
        '"Creature uccise: " + gdata(GDATA_KILLED) + ".\\nLivello di sotterraneo più profondo: "'
        ' + gdata(GDATA_DEEPEST) + "."',
    ('map_user.hsp', 2594):
        '"Rango del museo: " + (rankorg / 100) + " -> " + (rankcur / 100)'
        ' + " Adesso il tuo museo è <" + ranktitle(3) + ">."',
    ('map_user.hsp', 2775):
        '"Arredi: " + (gdata(GDATA_HOME_FURNITURE) / 100) + " Cimeli: "'
        ' + (gdata(GDATA_HOME_VALUE) / 100) + " Rango della casa: " + (rankorg / 100)'
        ' + " -> " + (rankcur / 100) + " Adesso la tua casa è <" + ranktitle(4) + ">."',
}


def main() -> int:
    uscita = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_85-cnvrank.jsonl'
    fuori = []
    for percorso in sorted(Path('dizionario').glob('*.jsonl')):
        nome = percorso.name[:-len('.jsonl')]
        for riga in io.open(percorso, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            chiave = (nome, v['riga'])
            if chiave in NUOVE and 'cnvrank' in (v.get('it') or ''):
                v = dict(v)
                v['it'] = NUOVE[chiave]
                fuori.append(v)
    if len(fuori) != len(NUOVE):
        print('attesi %d siti, trovati %d' % (len(NUOVE), len(fuori)))
        return 1
    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in fuori:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d voci in %s' % (len(fuori), uscita))
    return 0


if __name__ == '__main__':
    sys.exit(main())
