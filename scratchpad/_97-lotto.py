# -*- coding: utf-8 -*-
"""Taglia una zona dal restante di command.hsp.

    python scratchpad/_97-lotto.py <uscita.jsonl> da a [da a ...]
"""
import io, json, sys
uscita, coppie = sys.argv[1], sys.argv[2:]
zone = [(int(coppie[i]), int(coppie[i + 1])) for i in range(0, len(coppie), 2)]
voci = [json.loads(l) for l in io.open('lavoro/_97-command-restante.jsonl', encoding='utf-8') if l.strip()]
scelte = [v for v in voci if any(da <= v['riga'] <= a for da, a in zone)]
with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
    for v in scelte:
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(scelte)} voci in {uscita}')
