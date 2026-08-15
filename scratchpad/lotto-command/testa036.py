# -*- coding: utf-8 -*-
"""Lotto `command-036`: **dare un nome a un alleato, il menu del tono di voce e
l'evocazione dei PNG personalizzati**. Ventidue rese, e con queste **la zona
7000-7999 è chiusa**.

⭐⭐⭐ **La scoperta del lotto è una variabile che compone una frase inglese a
pezzi, e l'ha trovata il sorgente, non il referto.** `:7724` è
`txt lang("別世界の何かを召喚した！", "A " + s + " is summoned from another world!")`,
e quel `s` non è un nome: a `:7716`-`:7721` si carica **sei aggettivi inglesi
nudi** — `"Bad "`, `"Common "`, `"Skilled "`, `"Professional "`, `"Legendary "`,
`"Well-Known "` — uno per rango, ognuno dentro un `if ( … ) { … }` su una riga
sola, e solo a `:7722` ci aggiunge il nome vero.
⚠️⚠️ **E `variabili_en.py` non lo vedeva**, perché fino a stanotte prendeva solo
la forma `nome = "testo"` e non `nome += "testo"`. Corretto in questa sessione:
il conto passa da **66 variabili e 3 trappole** a **60 e 4**, e il quarto sito è
proprio questo. È il gemello esatto di `cnv_str_en.py` nella 45ª — **un referto
che non ha mai trovato niente in una famiglia non prova che la famiglia sia
pulita** — e anche stavolta il caso è saltato fuori leggendo il sorgente.
✅ **La resa segue il giapponese, che non nomina niente**: «Qualcosa di un altro
mondo è stato evocato!». È la stessa strada che la 38ª ha preso per `studybuddy`,
cioè il precedente di casa per questa famiglia di trappola. ⭐ Il rango si
potrebbe recuperare con **sei toppe** su `:7716`-`:7721` — e la regola della 46ª
non lo vieta, perché le toppe starebbero su righe diverse dalla resa — ma c'è un
nodo aperto: quegli aggettivi precedono un nome **che scrive il giocatore**, di
genere ignoto, e «Leggendario Anna» è sbagliato quanto l'inglese. Chi ci torna
deve prima decidere quello.

⭐⭐ **Due termini riscossi, e il secondo è la stessa espressione parola per
parola.** «Custom NPC» è già **«PNG personalizzato»** in `command.hsp:17535`; e
`:7626` — `"Piety: " + cdata(CDATA_PIETY, …) + "/" + sdata(SKILL_NORMAL_FAITH, …)
* 100` — è **identico carattere per carattere** a un pezzo di
`action.hsp:12722`, che lo rende già «**Devozione:** …». Non c'era niente da
scegliere.

⚠️⚠️ **E qui il tetto della riga di aiuto morde per la seconda volta, con una
differenza: stavolta lo sfora già l'inglese.** Tutt'e due le finestre sono da
**500 px**, quindi il tetto è (500 − 58 − 40) / 7,2 = **55 caratteri**. Ma la
riga non è solo la `lang()`: ci si sommano `strhint2` (**14** in italiano: due
tasti, una virgola e « [Pagina]  ») e `strhint3` (**20**, «Shift,Esc [Chiudi]  »),
e a `:7615` anche un `"* [Eq-Lvl] "` **fuori da qualunque `lang()`**.
- `:7505` — coda 34, quindi la `lang()` ha 21 caratteri. «Invio [cambia tono] »
  ne fa 20: totale **54**, dentro.
- `:7615` — coda **46**, quindi ne resterebbero 9. Impossibile. ⚠️ **Ma
  l'inglese è già a 59**, cioè quattro oltre il tetto, e a farlo sforare è
  proprio quel `"* [Eq-Lvl] "` che nessun dizionario raggiunge. La resa italiana
  è «Invio [evoca] », **due caratteri più corta dell'inglese**: il totale arriva
  a 60 solo perché `strhint2` e `strhint3` in italiano sono più lunghi, ed erano
  già spediti così.
⭐ **E `"* [Eq-Lvl] "` è il secondo membro della famiglia che la 46ª voleva
misurare con un `coda_en.py`** — un letterale inglese concatenato fuori dalla
parentesi di una `lang()`. Il primo era `:15489`, i «Guild Point». Questo, in
più, **è la causa dello sforamento**.

⚠️ **Tre volte l'inglese dice un'altra cosa, e tutt'e tre sono statiche senza
contratto, quindi la resa segue il giapponese**: `:7615` scrive «[Details]» dove
il giapponese ha 「召喚」, cioè **evoca** — ed è quel che il tasto fa davvero;
`:7608` scrive «Check which CNPC?» dove il giapponese chiede
「どの者を召喚したいと願うか？」, «chi desideri evocare?».

⭐⭐ **E su `:7784` la rete 3 ha parlato e aveva ragione, con un dettaglio che
non avrei trovato da solo.** 「足りないんよ」 — il rifiuto quando le monete di platino
non bastano — è già reso «Non bastano!» in `action.hsp:14356`, e lì la
condizione è `gdata(GDATA_FLAG_YACA_POINTS) < 100`: è **Yacatect**. Il dialetto
che si sente nel 「んよ」 non è un colore generico, è la sua voce, la stessa che il
lotto 028 ha reso popolana. Avevo scritto «Eh, non bastano.» prima di guardare;
la resa giusta esisteva già.

⚠️ **`:7818`, `:7823` e `:7828` sono la stessa riga giapponese sotto due inglesi
diversi, e la rete 4 pretende una resa sola — a ragione.**
「name(rc)は興奮して襲い掛かってきた。」 è identico in tutt'e tre i siti; l'inglese
distingue solo il terzo («is confused and attacks you» invece di «is excited!»).
I tre rami cambiano il valore di `CDATA_RELATION` (0, −1, −3), non il testo: è
l'autore giapponese ad aver scelto **una frase per tutti e tre**, e la rete 4
raggruppa per `(giapponese, funzioni di contenuto)`, che qui coincidono.
💡 È il rovescio del lotto 035, dove a distinguere era il giapponese e ad
appiattire l'inglese. Qui è l'inglese ad aggiungere una distinzione che
l'originale non fa, e non c'è nessuna rete che autorizzi a tenerla.

⚠️ Due accordi evitati: `:7460` è «Che nome vuoi usare?» e non «Come vuoi
chiamarlo?», perché `him(tc)` è morfologia e sparisce; `:7471` è «D'ora in poi si
chiamerà …», che vale per chiunque.
"""
