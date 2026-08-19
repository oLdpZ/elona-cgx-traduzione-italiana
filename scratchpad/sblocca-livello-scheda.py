# -*- coding: utf-8 -*-
"""Toglie da `rinviate.jsonl` la firma di « level», rinviata «a mai» per sbaglio.

⭐⭐⭐ **Un rinvio si registra per FIRMA, ma il motivo vale per un SITO.**

`lang("階相当", " level")` compare **due volte** in `command.hsp` con la stessa
firma:

    :2956   dentro il ramo `if ( jp )` del diario -- non gira mai in italiano
    :10710  la scheda del personaggio, percorso comune -- si vede sempre

Il rinvio fu scritto guardando il primo e conclude: «questa `lang()` non viene
valutata mai». E' vero per `:2956` e **falso per `:10710`**, che e' la riga
«Potenza 0 level» in fondo alla seconda colonna della scheda del personaggio —
una finestra che il giocatore apre di continuo. Il rinvio, indicizzato per
firma, ha tenuto ferma anche l'occorrenza viva.

💡 **Il difetto non l'ha trovato un referto: l'ha trovato lo schermo.** Nessuno
strumento poteva accorgersene, perche' per tutti gli strumenti quella firma era
«decisa». La verifica che manca — e che vale la pena scrivere — e' *una firma
rinviata per il ramo della lingua ha tutte le sue occorrenze in quel ramo?*

⚠️ Verificato prima di toccare niente: fra `command.hsp:10600` e `:10711` non
c'e' nessun `if ( jp )` ne' `if ( en )`. La riga sta sul percorso comune.

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

FIRMA = "aa641c0418272ffb3a18fc8e6a045ffa367b1d4d"

tenute, tolte = [], 0
with io.open("rinviate.jsonl", encoding="utf-8") as f:
    for l in f:
        if not l.strip():
            continue
        v = json.loads(l)
        if v.get("firma") == FIRMA:
            tolte += 1
            continue
        tenute.append(json.dumps(v, ensure_ascii=False))

if tolte != 1:
    raise SystemExit(f"attesa 1 firma da togliere, trovate {tolte}: non scrivo niente")

io.open("rinviate.jsonl", "w", encoding="utf-8",
        newline="").write("\n".join(tenute) + "\n")
print(f"tolta 1 firma; rinviate.jsonl passa a {len(tenute)} voci")
