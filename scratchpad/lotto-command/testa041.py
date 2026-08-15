# -*- coding: utf-8 -*-
"""Lotto `command-041`: **le capacità, le direzioni e il resto della zona
5000-5999**. Ventiquattro rese, da `:5015` a `:5892`. Con questo la zona si
chiude.

⭐⭐⭐ **La scoperta di questo lotto è che `sizefix` NON è zero, e questo corregge
un numero che la 47ª aveva scritto come corretto.** La 47ª, dopo il collaudo,
aveva stabilito che `12 + sizefix - en * 2` valesse **10** «con `sizefix` assente
da `config.txt` e quindi 0». Ma `sizefix` in `config.txt` c'è, dieci righe sotto
il `font2. "Courier New"` che quella stessa sessione aveva letto:

    config.txt:84   fontSfix1.  "1"     fixes font size
    config.hsp:180  cfgRead "fontSfix1.", sizefix = int(rtvaln)
    config.hsp:436  sizefix = 0     <- solo nel ramo GIAPPONESE

Il ramo inglese (`config.hsp:439`) non lo azzera: `sizefix` resta **1**, e il
corpo è **11**, cioè **6,6 px** a carattere. Non 10 e non 6.
✅ **Nessuna resa già spedita ne esce sbagliata**: l'unico tetto che la 47ª aveva
ricavato dal corpo 10 è quello di 「命中」, 27 px, che fa 4 caratteri tanto a 6 px
quanto a 6,6 — e «Mira» ne fa 4.
⚠️ **Ma cambia il tetto della riga di aiuto di `display_window`**, che la 47ª
calcolava a 7,2 px: la formula giusta è `(larghezza − 58 − 40) / 6,6`, cioè
**42** caratteri per una finestra da 380 e non 39, **76** per una da 600 e non
69. La stessa correzione vale per `display_topic` (`module.hsp:4365`) e
`display_note` (`:4359`), che usano tutt'e tre quella riga di `font`.
💡 E la decisione della 47ª su `:11849` **resta giusta lo stesso**: la resa ovvia
faceva 44 caratteri, che sfora anche i 42 veri.

⭐ **E la riga di aiuto di questa finestra è il primo caso misurato in cui
l'italiano ci sta per tre caratteri.** `:5342` compone `s(1)` con quattro pezzi
già spediti — `strhint2` «[Pagina]», `strhint3` «Shift,Esc [Chiudi]»,
`strhint7` «0~9 [Scorciatoia]», `strhint8` «* [NASC.] / [MOSTRA]» — più i due
tasti di `key_pageup`/`key_pagedown`: **73 caratteri su 76**. L'inglese ne usa
65. Chi allungasse una di quelle quattro stringhe di quattro caratteri farebbe
sparire l'ultima parola da questo menu e da ogni altro che le concatena.

⚠️⚠️ **`:5015` e `:5096` hanno lo STESSO giapponese, la stessa firma di funzioni
e una resa già decisa altrove**: 「足元に<item>が転がってきた。」 è `:4837`, «itemname(ci)
+ " rotola fino ai tuoi piedi."». La rete 4 pretende che le due siano uguali fra
loro e la rete 3 che siano uguali a `:4837`: si ricopia, e l'inglese
«from nowhere» di `:5096` — che il giapponese non dice — si perde come si è
perso in giapponese.

⚠️ **`:5892` è la rete 11 nella forma stretta, la seconda in due lotti.**
L'inglese è `"What action do you want to perform to " + him(tc) + "? "`, e `him`
a un argomento è morfologia: funzioni di contenuto **zero**, mentre il giapponese
ha `name(tc)`. La resa non nomina nessuno — «Che cosa vuoi fare? » — ed è
un'espressione perché la voce è dinamica. Gemella di `:14852` nel lotto 039.

⭐ **Sei rese riscosse senza decidere.** 「どの方向に…？」 è «In che direzione vuoi
…? » in `proc.hsp:7607` e `:7610`; 体当たり è «caricare» in `action.hsp:1732` e
`:1740` («Carichi la porta»); ショートカット è «Scorciatoia» in `text.hsp:10` e
`:121`; 能力 è «capacità» in `:6144` e `:7218`; 広域 è «in area» in
`skill.hsp:1913`; e 「上達」 ha la sua forma in `text.hsp:3205`, «migliora in
<abilità>», che `:5072` ripete in seconda persona.

⚠️ **Due volte l'inglese dice una cosa che il giapponese non dice, e vince il
giapponese.** `:5457` parla di «sealed» dove 非表示 vuol dire **nascondere** — ed
è quel che fa il codice, `spact(p) = 2` — e la riga di aiuto lo chiama già
«[NASC.]». `:5725` dice «sort by **increasing** freshness and value» dove il
giapponese dice 「低いほうにあわせて」, cioè si allinea alla **più bassa**: è anche
l'unica lettura che spiega perché il gioco lo chieda con un sì/no.

💡 **Le tre etichette a colonna di `:5344`-`:5346` hanno margine largo**, adesso
che il corpo è noto: «Nome» ha 25 caratteri di spazio (da `wx + 28` a `wx + 220`,
meno i 26 px che `display_topic` spende per la sua icona), «Costo» ne ha 11,
«Effetto» 32. Le stesse tre etichette servono anche il menu delle capacità ad
area (`:5554`-`:5556`), che sono seconde occorrenze della stessa firma.
"""
