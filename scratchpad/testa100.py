# -*- coding: utf-8 -*-
"""`custom_autopick.hsp` — le 86 voci vive, e sono quasi tutte CHIAVI.

⚠️⚠️ **Questo file non e' come i suoi dieci fratelli senza dizionario.** 78
delle sue 90 `lang()` non sono etichette da leggere: sono le **chiavi** con cui
il giocatore scrive le sue regole in `autopick.txt`, e `custom_autopick.hsp:358`
le confronta col **nome dell'oggetto**, che nella nostra build e' italiano. Il
guasto peggiore sta a meta' strada — file italiano e modello inglese — e per
questo il lotto va **nello stesso giro** della traduzione di
`data\\autopick.txt`. Per esteso in `decisioni.md` §98a.

⚠️ **Le chiavi si confrontano per SOTTOSTRINGA**, non per parola, e la catena
dei tipi non toglie quel che ha agganciato: se una chiave e' contenuta in
un'altra, il controllo di quella corta scatta sulla regola che nomina la lunga e
il suo `continue` butta via l'oggetto. In inglese questo succede **davvero due
volte** — `book` dentro `spellbook`, `food` dentro `traveler's food` — e in
giapponese mai. La rete e' `scratchpad/_100-selettori-ombra.py`, provata al
contrario su `--en` (deve accendersi due volte) e su `--jp` (deve tacere).
L'italiano ne vuole **zero**.

⚠️ **E le chiavi non hanno accenti, apposta.** `autopick.txt` e' l'unico file di
`data\\` scritto in **UTF-8** e non in CP932: una chiave accentata dovrebbe
esistere in due codifiche diverse — degradata nell'eseguibile, non degradata nel
modello — e le due non si aggancerebbero mai. Nessuna chiave porta un accento, e
la rete della sottostringa non basterebbe a dirlo.

Le tre scelte di resa che pesano:

1. **Le chiavi sono INVARIABILI dove l'italiano lo permette**, perche' il
   giocatore le scrive a mano e l'accordo di genere non c'e' chi lo faccia:
   `blessed`/`cursed`/`doomed` diventano « con benedizione », « con maledizione »
   e « con dannazione », che e' la deroga gia' decisa in `glossario.md` per
   `strblessed`/`strcursed`/`strdoomed` — e sono le stesse parole che compaiono
   **nel nome dell'oggetto**, cioe' proprio la stringa contro cui `:358`
   confronta. Le sei qualita' finiscono in `-e` da sole.
2. ⭐ **`good` non e' «buono»: e' « comune ».** La chiave inglese nomina
   `FIX_QUALITY_GOOD`, che e' l'indice **2** di `_quality` — e `text.hsp:106`
   quell'indice lo stampa a schermo come `common`, da noi «comune». Vale la
   regola del progetto: si dice quel che c'e' scritto sullo schermo, non quel
   che dice l'inglese di un'altra riga.
3. **`food` diventa « commestibile » e non « cibo », per non fare ombra a
   `traveler's food` = « cibo da viaggio »**, che e' il nome che l'oggetto ha
   davvero (`chat.hsp:13959`). E' la coppia su cui l'inglese si rompe: qui la
   parola generica si sposta, e quella specifica tiene il nome di schermo.

Quattro voci sono **rinviate perche' morte**: `:200`-`:217` sono due selettori
spenti con `//`, e il `//` e' la quinta famiglia di riga morta del progetto —
trovata in questa sessione, e la rete 6 di questo modello e' la prima che la
vede.
"""
