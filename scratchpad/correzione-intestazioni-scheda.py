# -*- coding: utf-8 -*-
"""Le due intestazioni della scheda che il collaudo della 68a ha visto rotte.

Sono l'**ultima** intestazione della loro riga, e fino alla 68a la RETE 20 non
misurava quelle: il suo docstring diceva «il loro limite e' il bordo della
finestra, che sta altrove». Non era il bordo della finestra ne' nell'uno ne'
nell'altro caso.

    command.hsp:10431  «Benedizioni e malocchi»  22   tetto 18   il RITRATTO
    command.hsp:10429  «Tiri di combattimento»   21   tetto 16   una MES

Il ritratto e' `window2 wx + 557, wy + 23, 87, 120` (`command.hsp:10470`),
disegnato **quaranta righe dopo** le intestazioni e senza condizioni: ci passa
sopra. Sullo schermo si leggeva «Benedizioni e maloc», con la coda sotto la
cornice. L'altra e' `pos wx + 564 - en * 22, wy + 263` con «Pot. magia»
(`:10733`), trecento righe piu' in la': «Tiri di combattimento» ci finiva
sopra, e a schermo le due parole erano stampate una dentro l'altra.

## I due tetti, misurati e non dedotti

Il testo comincia a `x + 26` e avanza di **7 px** per carattere, misurato sulla
schermata del 2026-08-19: «Attributi base - Potenziale», 27 caratteri, dal primo
glifo (664) all'ultimo (847) fa 183 px su 26 intervalli, cioe' 7,038.

    (557 - 400 - 26) / 7 = 18       (542 - 400 - 26) / 7 = 16

## Le due rese

⭐ **`:10429` migliora tornando al giapponese.** 各種修正 vuol dire
«modificatori vari», e il blocco mostra proprio quelli: `Arma1 3d5-1 x2.6`,
`Mira 65%`, `Prot. 13% + 1d5`, `Pot. magia 100%`. «Tiri di combattimento» era
una resa dell'inglese «Combat Rolls», che a sua volta e' una resa libera del
giapponese. **Modificatori** e' piu' corto, piu' fedele e lungo esatto quanto
monte.

⚠️ **`:10431` sacrifica «Benedizioni», non «malocchi».** Il glossario tiene
`hex` → **malocchio** apposta, distinto da `curse` → maledizione, perche' il
gioco distingue i due 呪い (`skill.hsp:440` scrive `呪い(hex)`). Dei due sostantivi
solo «malocchio» porta una distinzione contesa: «benedizione» non ha un gemello
che gli faccia concorrenza, quindi e' quello che puo' cambiare parola.

💡 E la frase intera **resta a schermo lo stesso**: `command.hsp:10344` la scrive
per esteso nel suggerimento in cima alla finestra, «Cursore [Benedizioni e
malocchi]», che si legge nella stessa schermata. L'intestazione e' un'etichetta
di colonna, non l'unico posto dove il termine compare.

    Blessing and Hex        16        Combat Rolls    12
    Benedizioni e malocchi  22        Tiri di comb..  21
    Doni e malocchi         15        Modificatori    12

Tutt'e due stanno anche sotto la lunghezza di monte, che e' il metro del
progetto quando il tetto e' stretto.

⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

PERCORSO = "dizionario/command.hsp.jsonl"

CAMBI = {
    10429: ("Tiri di combattimento", "Modificatori", 16),
    10431: ("Benedizioni e malocchi", "Doni e malocchi", 18),
}

righe = []
fatte = 0
with open(PERCORSO, encoding="utf-8") as f:
    for l in f:
        if not l.strip():
            continue
        d = json.loads(l)
        atteso = CAMBI.get(d["riga"])
        if atteso and d["it"] == atteso[0]:
            vecchio, nuovo, tetto = atteso
            if len(nuovo) > tetto:
                raise SystemExit(
                    f"{nuovo!r} fa {len(nuovo)} caratteri e il tetto e' {tetto}")
            d["it"] = nuovo
            fatte += 1
        righe.append(json.dumps(d, ensure_ascii=False))

if fatte != len(CAMBI):
    raise SystemExit(f"attese {len(CAMBI)} voci, cambiate {fatte}: non scrivo niente")

io.open(PERCORSO, "w", encoding="utf-8", newline="").write("\n".join(righe) + "\n")
for riga, (vecchio, nuovo, tetto) in sorted(CAMBI.items()):
    print(f"command.hsp:{riga}  tetto {tetto}   "
          f"{vecchio!r} ({len(vecchio)}) -> {nuovo!r} ({len(nuovo)})")
