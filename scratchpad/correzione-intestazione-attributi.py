# -*- coding: utf-8 -*-
"""«Attributi (base) - Potenziale» e' due caratteri piu' lungo dell'inglese.

`command.hsp:10410`, la prima intestazione della scheda del personaggio. La
colonna va da `wx + 28` a `wx + 240`, dove nelle partite in modalita' speciale
comincia la casella «Modalita' <nome>»: tolti i 26 px dell'icona restano 186 px,
e a **7 px** per carattere (RETE 20, `intestazioni_larghezze.py`) il tetto e'
**26**.

⚠️ **Li' sfora anche l'inglese**, che ne fa 27: e' una delle due sole colonne
del gioco dove upstream non sta dentro. Dove monte sfora, il perimetro del
progetto non e' il tetto ma **«non piu' lungo di monte»** — e la resa scritta
nel lotto `fase4-command-044` ne faceva **29**.

    Attributes(Org) - Potential     27
    Attributi (base) - Potenziale   29   <- due di troppo
    Attributi base - Potenziale     27   <- pari a monte

💡 La resa era stata scelta quando la rete 20 dichiarava il passo **6** invece
di 7: col passo sbagliato il tetto risultava 31 e 29 ci stava comodo. Il passo
vero e' misurato a schermo nella 65a. **Un tetto sbagliato non fa sbagliare la
misura: fa scrivere una resa che non ci sta, e la si scopre dopo.**

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

PERCORSO = "dizionario/command.hsp.jsonl"
RIGA = 10410
VECCHIO = "Attributi (base) - Potenziale"
NUOVO = "Attributi base - Potenziale"

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
print(f"cambiata {fatte} voce: {VECCHIO!r} ({len(VECCHIO)}) -> {NUOVO!r} ({len(NUOVO)})")
