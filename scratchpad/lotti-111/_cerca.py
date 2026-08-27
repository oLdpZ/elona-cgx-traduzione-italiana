# -*- coding: utf-8 -*-
"""Cerca un termine giapponese (o italiano) in tutto il dizionario e stampa
jp | en | it, per il controllo a mano prima di chiudere un lotto.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-111/_cerca.py 防具 防御力
"""
import glob
import json
import sys

termini = sys.argv[1:]
for t in termini:
    print("### " + t)
    visti = set()
    n = 0
    for percorso in sorted(glob.glob("dizionario/*.jsonl")):
        with open(percorso, encoding="utf-8") as f:
            for riga in f:
                d = json.loads(riga)
                campi = (d.get("jp") or "") + "\x00" + (d.get("it") or "")
                if t not in campi:
                    continue
                chiave = (d.get("jp"), d.get("it"))
                if chiave in visti:
                    continue
                visti.add(chiave)
                n += 1
                if n > 8:
                    continue
                print("  {} | {} | {}".format(
                    (d.get("jp") or "")[:60],
                    (d.get("en") or "")[:60],
                    (d.get("it") or "")[:70]))
    if n > 8:
        print("  ... e altre {} voci".format(n - 8))
    if n == 0:
        print("  (niente)")
