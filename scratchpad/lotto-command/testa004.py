# -*- coding: utf-8 -*-
"""Lotto `command-004`: le 46 origini di `*setHistory1`, la prima riga del
«Background».

La schermata sta in `chara.hsp:3265`-`:3336` e la vede **ogni personaggio
nuovo**: cinque righe tirate a sorte — origine, perche' sei partito, un pregio,
un difetto, un vizio privato — disegnate una sotto l'altra con `mes` a
`pos wx + 75, wy + 200 + n * 15`. Questo lotto e' la prima delle cinque.

⚠️⚠️ **Il soggetto non e' solo il giocatore: e' anche un ALLEATO.**
`chat.hsp:8588`-`:8593` rilegge gli stessi cinque valori da
`cdata(CDATA_BACKGROUND_PART_*, c)` e li fa raccontare a Mizuki, dove `c` e'
il compagno scelto con `*com_ally`. Quindi il genere e' ignoto in tutt'e due i
casi, e non c'e' una `lang()` gemella che distingua: **e' la stessa riga**.

✅ **Il giapponese il soggetto non ce l'ha proprio** — 「奴隷だった過去を持つ。」,
「王族の一員だった。」 — ed e' l'inglese che ci mette «You». Le rese sono
**nominali**, che e' la forma del giapponese e l'unica senza accordo: la stessa
strada che `guida-stile.md` prescrive per le etichette di stato («Inedia» e non
«Affamato»).

💡 **Le tre manovre che tolgono il participio dal soggetto**, e tornano in tutte
e cinque le righe della schermata:
  - il **nome astratto** al posto dell'aggettivo: 「奴隷だった」 -> «Un passato di
    schiavitu'», 「囚われの身」 -> «Anni di prigionia»;
  - il participio **appeso a una cosa**, non alla persona: «Genitori perduti
    troppo presto», «Il paese natale, distrutto dai mostri» — l'accordo cade su
    `genitori` e su `paese`, che un genere ce l'hanno;
  - il **nome di genere fisso** per chi la persona la nomina per forza: «Cavia»,
    «una creatura maledetta», «Un'arma nata da una tecnologia proibita»,
    «Il clone», «Un frutto nascosto». E' la strada della 40a e della 41a («Balia
    delle bestie»), qui usata quarantasei volte di fila.

⚠️ **Il tetto e' 54 caratteri**, ed e' misurato: nessuna guardia guarda questa
finestra — come per la scheda del personaggio della 43a — ma la finestra e'
larga 360 px e upstream ci fa stare `:9579`, «You were actually being raised by
your parents' enemy.». Il metro possibile e' quello di `tetti_buffdesc.py`,
l'italiano **contro l'inglese di monte**: nessuna resa supera la piu' lunga
delle 46 inglesi. Lo misura `scratchpad/misura-background.py`.

💡 **Zero copie**: `dossier.py` non trova nemmeno un giapponese o un inglese
gia' reso altrove. E' la prima zona del progetto che non pesca niente — il
generatore del passato non parla la lingua di nessun'altra schermata.
"""
