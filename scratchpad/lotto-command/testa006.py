# -*- coding: utf-8 -*-
"""Lotto `command-006`: i 45 pregi di `*setHistory3`, la TESTA della terza frase
del «Background».

⭐⭐ **Questa riga e' meta' di una frase, e l'altra meta' e' `*setHistory4`.**
`chara.hsp:3322`-`:3330` disegna `ohanasi3` e `ohanasi4` su due righe
consecutive, e in giapponese la prima finisce in 「〜が、」 — la congiuntiva
avversativa — mentre la seconda chiude il periodo col punto:

    温厚で慈悲深いが、          ->  Mitezza e generosità, ma
    熱中すると周りが見えなくなる。 ->  la passione fa perdere di vista tutto il resto.

⚠️⚠️ **E le due meta' si tirano a sorte SEPARATAMENTE**: `ohanasi3` e `ohanasi4`
sono due `rnd(45) + 1` indipendenti (`chara.hsp:3261`-`:3262`), quindi ognuno dei
45 pregi deve saldarsi a ognuno dei 43 difetti — 1.935 frasi possibili. La resa
non puo' concordare la testa con la coda in niente: ne' genere, ne' numero, ne'
soggetto. ✅ Il nominale lo garantisce per costruzione, ed e' il motivo per cui
questa riga il registro nominale lo pretende invece di limitarsi a preferirlo.

✅ **Ogni testa finisce in «, ma»**, che e' il posto in cui il giapponese mette
「が、」. L'inglese fa il contrario e mette «Though» in **testa** — «Though you
are gentle and merciful,» — che in italiano vorrebbe «Per quanto mite e
generoso,», cioe' due aggettivi accordati col giocatore. La congiunzione in coda
e' la stessa manovra della rete 9, applicata a una avversativa invece che a
una copulativa.

💡 **I pregi sono AGGETTIVI in inglese e SOSTANTIVI in italiano**, ed e' la
tabella di `guida-stile.md` («Starving» -> «Inedia») usata quarantacinque volte:
«Though you are calm and collected» -> «Sangue freddo e buon giudizio».
⚠️ Dove il pregio nomina per forza la persona, torna il nome di genere fisso:
`:9837` «strong leadership» -> «Una **guida** forte per gli altri».

Tetto 57 caratteri (`:9831`), misurato con `scratchpad/misura-background.py`;
la resa piu' lunga ne fa 47. Zero copie da `dossier.py`.
"""
