# -*- coding: utf-8 -*-
"""Un giapponese, due rese: 祝福と呪い era «malocchi» in due file e «maledizioni» in uno.

Il glossario su `hex` e' esplicito: **«malocchio», non «maledizione», che e' gia'
`curse`**. Il gioco tiene i due 呪い separati — `cursed` sta sull'**oggetto** e si
oppone a `blessed`, `hex` sta sulla **persona** e si oppone a un buff — e
l'italiano li separa sullo stesso asse.

Il dizionario lo seguiva in due siti su tre:

    config.hsp:636   'Hexes/Buffs'    -> 'Buff e malocchi'          ✅
    skill.hsp:444    'Vanquish Hex'   -> 'Scaccia i malocchi'       ✅
    command.hsp:1999 '...Blessings and Hexes' -> '...e maledizioni' ❌

⚠️ **E il terzo e' la descrizione dello stesso riquadro** che il lotto
`fase4-command-044` intitola «Benedizioni e malocchi» (`command.hsp:10431`, lo
stesso 祝福と呪い): lasciarlo avrebbe messo due nomi diversi per la stessa cosa
a due centimetri di distanza sulla stessa finestra.

💡 Trovato dalla rete 3 mentre si cercava una resa da riscuotere, non da un
referto: cercare *se una parola e' gia' stata resa* trova anche le volte che e'
stata resa in due modi.

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

PERCORSO = "dizionario/command.hsp.jsonl"
RIGA = 1999
VECCHIO = "<title1>*Benedizioni e maledizioni<def>\\n"
NUOVO = "<title1>*Benedizioni e malocchi<def>\\n"

righe = []
fatte = 0
with open(PERCORSO, encoding="utf-8") as f:
    for l in f:
        if not l.strip():
            continue
        d = json.loads(l)
        if d["riga"] == RIGA and d["it"] == VECCHIO:
            d["it"] = NUOVO
            fatte += 1
        righe.append(json.dumps(d, ensure_ascii=False))

if fatte != 1:
    raise SystemExit(f"attesa 1 voce, cambiate {fatte}: non scrivo niente")

io.open(PERCORSO, "w", encoding="utf-8", newline="").write("\n".join(righe) + "\n")
print(f"cambiata {fatte} voce: {VECCHIO!r} -> {NUOVO!r}")
