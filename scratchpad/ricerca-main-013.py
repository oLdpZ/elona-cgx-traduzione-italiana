# -*- coding: utf-8 -*-
"""Il vocabolario del minigioco delle orecchie, che `action.hsp` ha gia' fissato."""
import glob
import io
import json
import re

print('=== action.hsp, il minigioco gemello (14500-14750) ===')
for linea in io.open('dizionario/action.hsp.jsonl', encoding='utf-8'):
    if not linea.strip():
        continue
    d = json.loads(linea)
    if d.get('it') and 14500 <= d['riga'] <= 14750:
        print(f"  :{d['riga']}  en: {d['en'][:72]}")
        print(f"           it: {d['it'][:72]}")

print()
print('=== ogni resa che parla di orecchio, timpano, cerume ===')
visti = set()
for percorso in sorted(glob.glob('dizionario/*.jsonl')):
    nome = percorso.replace('\\', '/').split('/')[-1]
    for linea in io.open(percorso, encoding='utf-8'):
        if not linea.strip():
            continue
        d = json.loads(linea)
        if not d.get('it'):
            continue
        if re.search(r'orecchi|timpano|cerume|condotto', d['it'], re.I):
            chiave = d['it'][:40]
            if chiave in visti:
                continue
            visti.add(chiave)
            print(f"  {nome}:{d['riga']}")
            print(f"      en: {d['en'][:70]}")
            print(f"      it: {d['it'][:70]}")
