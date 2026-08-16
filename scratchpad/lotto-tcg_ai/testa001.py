# -*- coding: utf-8 -*-
"""Lotto fase4-tcg_ai-001: la domanda per uscire dal duello automatico, e
**chiude `tcg_ai.hsp`** (tcg_ai.hsp, righe 308-309).

Due rese, ed e' tutto il testo che quel file ha: 5.347 righe di gioco di carte
e due sole `lang()`.

⚠️ **Le due righe hanno lo STESSO giapponese**, 「降参する」 — «arrendersi» —
anche per il bottone che dice «No». E' il terzo posto del gioco di carte dove il
mod riusa il primo argomento senza toccarlo, e prima della correzione alla rete 4
di oggi questo lotto non sarebbe stato scrivibile.

⭐ **«Scappi?» e non «Ti arrendi?».** Il giapponese dice arrendersi, ma il ramo
mette `gameresult@tcg = -2` (`:313`), che `tcg.hsp:2779` chiama «Fuggito!» e
`:2805` «hai rovesciato il tavolo di corsa». La resa vera e' -1, ed e' un altro
tasto. L'inglese ha corretto il giapponese, e la resa segue l'inglese.

⚠️ **«No» resta «No»**, e sta in `invariati.md`: la parola e' identica nelle due
lingue. Non e' il caso di «Yes», che si traduce.

💡 Riquadro da 200px -> 20 caratteri col metro di `larghezze.py`.
"""
