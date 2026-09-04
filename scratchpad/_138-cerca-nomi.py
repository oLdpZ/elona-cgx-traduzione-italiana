"""Cerca nei dizionari le rese gia' decise per un elenco di monte."""
import glob
import json
import os
import sys

VOGLIO = {s.lower() for s in (sys.argv[1:] or [
    "Beer", "Ale", "Whiskey", "Sake", "Tequila", "Cola", "Hangover",
    "Love Potion", "Wa'ah", "Aqua Parti-o", "Ryutye", "Kuroya", "socks",
    "here", "shoot me", "this guy", "No Effect.",
])}

for percorso in glob.glob("dizionario/*.jsonl") + glob.glob("dizionario/carte/*.jsonl"):
    for riga in open(percorso, encoding="utf-8"):
        if not riga.strip():
            continue
        voce = json.loads(riga)
        inglese = (voce.get("en") or "").strip()
        if inglese.lower() in VOGLIO:
            print("%-22s %-28r -> %r"
                  % (os.path.basename(percorso), inglese, voce.get("it")))
