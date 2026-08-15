# -*- coding: utf-8 -*-
"""Lotto `command-012`: le 31 voci del «苦手なもの» e le due intestazioni di
`*com_knowSelf`.

E' la seconda sezione della finestra della telepatia — quel che il compagno
**non regge**: dodici elementi di attacco, sei stati, cinque cose fisiche e
**cinque scherzi**. Piu' il titolo della finestra e le due intestazioni della
schermata gemella, quella che legge gli effetti attivi.

⭐ **I cinque scherzi sono paure di creature precise**, e il sorgente le lega a
un `CREATURE_ID`: 「ふかふかパン」 al `CREATURE_ID_ALCHEMIST_NAPLUS`, poi il
sale, lo yeek, il gatto, lo squalo. La resa li prende **dal progetto, non
dall'inglese**: «pane soffice» sta gia' in `db_item.hsp:141763` e in
`ai.hsp:1163`, «lo yeek» in tre file, «il gatto» in quattro, «sale» in
`db_item.hsp:141789`. La rete 3 li avrebbe chiesti comunque.
💡 Coi nomi di creatura viene dentro anche **l'articolo**, che e' il contratto
dei nomi (`contratto-nomi.md` §4): in colonna si legge «lo yeek», «il gatto»,
«lo squalo», e va bene — sono le cose di cui ha paura, non etichette.

⚠️ **Undici elementi su dodici erano gia' decisi**, e non da una voce sola:
`action.hsp:6918`-`:7044` ha le ventiquattro righe di «Add X Resistance» e «Add
X Damage», e da li' vengono «fuoco», «gelo», «fulmine», «oscurita'», «mentale»,
«veleno», «oltretomba», «suono», «nervi», «caos», «magia». Cercare prima di
scrivere, di nuovo.

⚠️ **`:1985` ha `name(tc)` nel GIAPPONESE e non nell'inglese.** Il sorgente e'
`lang("<title1>◆ " + name(tc) + "の受けている影響<def>\\n", "*<title1> Your
bonuses and penalties.<def>\\n")`, e `estrai` la classifica **statica** perche'
il ramo inglese e' una stringa pura. ✅ Quindi la resa **non puo' nominare il
soggetto** anche volendo — e' la regola della 40a («se l'inglese non ha
`name()`, la resa italiana non puo' nominare il soggetto») in una forma nuova,
dove a nominare e' il giapponese.
⚠️ E il soggetto non e' sempre il giocatore: `:1981` fa `if ( tc ==
CHARA_PLAYER )` per un pezzo solo, quindi «i tuoi bonus» sarebbe sbagliato per
un alleato. ✅ «Effetti in corso», che non nomina nessuno.

💡 **E l'asterisco di `:1985` sta fuori dal tag.** L'inglese scrive
`"*<title1> Your bonuses…"` mentre `:1999` scrive `"<title1>*Effects…"` e il
giapponese mette il ◆ **dentro** in tutt'e due: a schermo, il primo asterisco
resta fuori dallo stile del titolo. La resa lo rimette dentro, come fa l'altra
riga.

⚠️ **La rete 3 su 「塩」 e' un falso positivo, e la colpa e' di come `db_item.hsp`
spezza i nomi.** `ITEM_ID_BOTTLE_SALT` in inglese ha **due** pezzi di nome —
`ioriginalnameref` = «salt» e `ioriginalnameref2` = «bottle» (`:141789`-`:141790`)
— e in giapponese uno solo, 「塩」 (`:141786`). L'estrazione appaia quindi lo
stesso giapponese sia a «salt» che a «bottle», e il dizionario ha 「塩」 reso
«sale» **e** «bottiglia». Qui la resa giusta e' «sale», che e' quella della
coppia vera. 💡 Ogni oggetto il cui nome inglese si spezza in due produrra' la
stessa segnalazione: e' un artefatto del sorgente, non un'incoerenza.

Tetto 46 caratteri (`:1999`, coi tag contati). Cinque copie di giapponese e due
di inglese trovate da `dossier.py`, tutte usate.
"""
