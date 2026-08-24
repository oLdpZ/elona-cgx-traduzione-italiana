# -*- coding: utf-8 -*-
"""92a - BELPHAT (`chat.hsp:12560`-`:12632`, 15 firme).

宇宙剣客『ベルファート』 = **«<Belphat> lo spadaccino cosmico»**
(`db_creature.hsp:61195`, `db_card.hsp:4248`). Gira l'universo per **mangiare**
e cerca il vecchio amico クロやん, cioe' 『クロヤ』 = «<Kuroya> lo scrutatore del
cosmo» (`db_creature.hsp:71315`), che il progetto chiama gia' **«Kuro»** nel
soprannome affettuoso (`chat.hsp:12657`, gia' resa).

⭐ DIECI DELLE QUINDICI RIGHE SONO IL SUO DIARIO DI VIAGGIO, e sono un elenco
di **nomi del Ciclo di Cthulhu**. Non sono katakana inventati, e l'inglese li
traslittera a orecchio sbagliando quasi tutto — e' lo stesso caso dei ventotto
eoni di Mikraanesis, in questa stessa sessione:

    ユゴス           Yugos      ->  **Yuggoth**    il pianeta di Lovecraft
    バイアクヘー      Bayakhae   ->  **Byakhee**    le creature che portano
                                                   i viaggiatori nel vuoto
    サイクラノーシュ  Cyclanorch ->  **Cykranosh**  Saturno in Clark Ashton Smith
    ミ=ゴ            Mi-Go      ->  **Mi-Go**      (l'unico che l'inglese azzecca)

Il progetto le forme italiane del Ciclo le usa gia': «lo shoggoth»
(`db_creature.hsp:80712`), «la Grande Razza di **Yith**» (`db_card.hsp:14390`),
«classe Yith» (`action.hsp:2604`), e in `invariati.md` stanno `Necronomicon` e
`Liber Damnatus`. Qui si continua.

⭐⭐⭐ DEROGA 1 — `:12591`, イス焼き NON E' «FRIED ICE CREAM».
L'inglese ha letto イス come *ice*. Ma イス in questo progetto e' **Yith** — lo
dicono due file gia' tradotti (`db_card.hsp:14390` «la Grande Razza di Yith»,
`action.hsp:2604` «classe Yith») — e la riga sta in mezzo a Yuggoth, ai Mi-Go e
ai Byakhee. イス焼き e' costruito come たこやき, che sta nella stessa frase:
*polpo alla piastra* / *Yith alla piastra*, cioe' il cibo da bancarella fatto
con la creatura del mito.
💡 In italiano il paio si tiene con **«frittelle di polpo»** e **«frittelle di
Yith»**: quel che conta e' che le due voci abbiano la **stessa forma**, perche'
la battuta e' la sostituzione dell'ingrediente.
⚠️ E il polpo dev'essere **vivo**: 「あんまり暴れるものだから」, si dimenavano
tanto che se li e' mangiati per strada. L'inglese lo tiene («thrashing
around»), e senza quello la frase perde il motivo.

⚠️ DEROGA 2 — I NOMI CHE NON SONO DEL MITO RESTANO NELLA FORMA INGLESE.
ボッヘリト, デベロンダッタ, ジェラミス, ニャリン, スンバラリア, トゥンツァ non
sono di Lovecraft ne' di Smith: non c'e' una forma italiana da recuperare e non
si inventa. Si tiene la traslitterazione dell'inglese — Bohelito, Develondatta,
Geramis, Nyarin, Sumbalaria, Tunza — che e' anche quella con cui il giocatore
italiano li trova nelle guide del gioco.

💡 `:12594` — il giapponese dice che i **gatti** somigliano ai ニャリン星人 e che
quelli hanno invaso un pianeta: e' una battuta, e la si lascia dov'e' senza
spiegarla.

LESSICO DECISO QUI (va in glossario): 宇宙剣術 -> «la scherma cosmica», che sta
sotto il nome di carta gia' deciso, «lo spadaccino cosmico».

PERIMETRO: 15 firme su 16 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 12560`).

MENU: uno, 2 voci — una colonna sola, tetto 58.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- Kuro, l'amico ritrovato
    12565: "Anche Kuro è migliorato parecchio. Ha fatto sua la scherma cosmica che gli avevo mostrato appena appena, tanti anni fa, e per giunta ci ha messo del suo.",
    12573: "Ma dai, Kuro... si è fatto una copia della spada che è il cimelio di famiglia. Immagino la voglia uguale alla mia... e adesso sono in imbarazzo: l'altra volta mio padre mi ha sgridato perché avevo portato via il cimelio senza chiedere, e stavolta non me la sono portata dietro.",
    12602: "Kuro... ma dove sei, adesso...",

    # --- il diario di viaggio
    12576: "Quando sono passato dal pianeta Yuggoth, i cacciatori spaziali di Bohelito stavano sterminando i Mi-Go, che lì sono una specie importata. Qualche Mi-Go ha fatto resistenza, ma quelli di Bohelito valgono tre cani addestrati e li hanno presi uno dopo l'altro. E dopo aver dato una mano, che bontà il Mi-Go in pentola.",
    12579: "Ho usato anche il servizio di viaggi interstellari dei Byakhee, ma lì viaggia solo lo spirito, e per andare a mangiare in giro non va bene. E poi i preparativi da fare prima sono una noia.",
    12582: "Sul pianeta Cykranosh è stata dura. Fin lì tutto bene, mi avevano offerto i loro piatti di funghi; poi però mi hanno eletto consorte del loro capo senza chiedermelo. Sono scappato di corsa.",
    12585: "Quando sono andato sul pianeta Tunza c'era proprio la festa di nascita del loro dio. Che fortuna, ho pensato: e mi hanno servito una zuppa di acido solforoso. L'ho bevuta, sia chiaro, ma con la lingua che pizzicava non c'era da assaporare granché.",
    12588: "La creatura più feroce dell'universo, quella che gira per il cosmo divorando cose, persone e perfino i pianeti... i Develondatta. Mi scambiano spesso per uno di loro e mi attaccano. Andare a mangiare in giro per l'universo è pieno di pericoli.",
    12591: "Come regalo avevo preparato anche le frittelle di polpo dei Geramis, ma si dimenavano così tanto che me le sono mangiate tutte per strada. Non c'era rimedio, e allora ho comprato una montagna di frittelle di Yith.",
    12594: "Su questo pianeta c'è un sacco di creature chiamate gatti, che somigliano a quelli di Nyarin. L'altra volta che sono passato di qui mi sono preso uno spavento: mi avevano detto che erano quei fenomeni che hanno invaso il pianeta Sumbalaria...",

    # --- il menu, e la ricompensa
    12600: "Non ne so niente",
    12601: "Ti ci porto io",
    12611: "Davvero? Questo sì che mi aiuta! Se mi ci porti per bene, avrai la tua ricompensa.",

    # --- chi è, raccontato da lui
    12624: "Il mio nome è Belphat. Uno spadaccino cosmico qualunque, di quelli che si trovano dappertutto. Su questo pianeta ero passato una volta per caso e non sapevo nemmeno dove fosse, ma un tale che si dice guida cosmica mi ci ha accompagnato, e così ho potuto tornarci.",
    12625: "E così, mentre cercavo qui il mio vecchio amico, ho incontrato una fata che si spaccia per guida e le ho chiesto di lui. ...Mi ha liquidato dicendo che non lo conosce. Ma mentre insistevo, qualunque cosa, davvero non sai niente, mi sono accorto di un particolare: da costei viene odore di chi nasconde qualcosa. Ho intenzione di torchiarla a fondo, finché non si tradisce.",
}
