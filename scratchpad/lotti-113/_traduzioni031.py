# -*- coding: utf-8 -*-
"""Le rese del lotto 031 — il MOBILIO, quinta parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 031 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa031.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Cinque gruppi di questo lotto condividono una frase giapponese **identica**
parola per parola, e in italiano quella frase e' identica altrettanto. Dove il
genere lo impedirebbe, la frase e' scritta **senza genere** apposta: le sette
tombe non sono tutte femminili (`:120005` e' un tumulo), e le armi e gli archi
neanche.
"""

IT = {
    114206: "Un corno che manda un suono squillante. In sostanza sa fare una nota sola, ma quel timbro fiero basterà a scuotere il cuore della gente. \\n# ~Le Melodie della Limpida Irva~",

    # === LE DUE STATUETTE, e il bambino che le guarda =====================
    115320: "Una suppellettile che si potrebbe scambiare per un'arma vera. È fatta a immagine di una spada piantata nella terra, e si dice, ma chi lo sa, che in passato un prode l'abbia usata a forza come arma. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    115382: "Un pupazzo snodabile fatto a immagine di un guerriero, lavorato con cura minuta. Costa caro, ma sa mettersi in ogni posa, e per questo, dicono, i bambini lo sognano. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    115384: "\\\"Uahahaha! Che forte! Che figo!\\\" \\n# ~Parole di <Seth>, ragazzino di città~",

    118643: "Un mobile con impilati piatti tutti dello stesso tipo. Comodo quando arrivano ospiti all'improvviso, ma meglio non posarlo per terra: basta inciampare nella fretta e va tutto in pezzi. \\n# ~I Comprimari della Cucina~",
    119687: "Un giaciglio efficiente, con un letto impilato sopra l'altro. Si trova spesso nelle locande, e dicono che quando ci dormono gli avventurieri capiti di vederli litigare su chi va di sopra. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE SETTE TOMBE ===================================================
    # ⚠️ la seconda frase e' la STESSA in tutte e sette, parola per parola:
    #    当然ながら非常に重いので持ち上げてみようと思わない方がいいだろう。
    #    In italiano e' identica, e senza genere perche' `:120005` e' un
    #    tumulo e non una tomba.
    119943: "Una tomba da cui si sente il passare della storia. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120005: "Un tumulo enorme, costruito per un potente dei tempi antichi. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120067: "Una tomba davanti a cui si trattiene il fiato e si fa un passo indietro senza volerlo. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120129: "Una tomba che si potrebbe scambiare per un bel monumento di pietra. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120191: "Una bella tomba, sepolta sotto i fiori. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120253: "Una tomba che fa venire voglia, finalmente, di averne una propria. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",
    120315: "Una tomba che da parecchio nessuno cura più. Naturalmente il peso è enorme, e non conviene nemmeno pensare di provare a sollevare una cosa simile. \\n# ~Libro in Dono a Chi Sta Morendo~",

    120377: "Una pezza tessuta in seta. C'è scritto a lettere grandi che è già venduta, e perciò non si può usare. \\n# ~Palmia: Collezione Primavera-Estate~",
    120439: "Vestiti sparsi per terra. Se siano stati buttati lì prima del bucato, o se il bucato sia fatto e manchi solo di piegarli, non è chiaro. \\n#~Le Mille Cianfrusaglie che Amo~",
    120633: "Da qualunque parte lo si guardi, è uno scaffale e basta. Niente di più e niente di meno. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    120695: "Un candelabro pensato soprattutto come ornamento. Anche il piede è lavorato con un lusso senza risparmio, e risplende al punto che la candela non serve. \\n# ~Casalinghi che Danno Colore alla Casa~",
    120757: "Un tavolo pieno di atmosfera, il sogno delle signore. È un tavolo e nient'altro, eppure trabocca di nobiltà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    120819: "Un tavolo da pranzo rimpicciolito, come le padrone di casa chiedevano. A meno di non mangiare un pranzo a tutte portate, una misura così basterà. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LA CUCINA ========================================================
    120883: "Un bancone da cucina con i fornelli sopra. Un mobile solo fa due cose, e per questo va per la maggiore fra le signore che al mattino hanno fretta. \\n# ~I Comprimari della Cucina~",
    # ⚠️ `:120947` e `:121011` dicono la stessa seconda frase.
    120947: "Un lavello adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    121011: "Un bancone adatto a preparare gli ingredienti. C'è chi, impaziente, non resiste e finisce per cucinare lì sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    121696: "Un ottimo arnese da cucina che fa tutto: arrostisce, cuoce a vapore, lessa. È grandissimo e pesa molto, tanto che a comprarlo si esita, ma in cambio la sua bravura è garantita. \\n# ~I Comprimari della Cucina~",

    121073: "Tanto liquore che non sta in due mani. Non lo si finirebbe mai, e perciò non si può usare. \\n# ~Regali che Fa Piacere Ricevere~",

    # === I DUE MOBILI DEL MAESTRO =========================================
    # ⚠️ la formula e' quella della credenza `:87505` del lotto 028, e la resa
    #    la ricalca: «costruita con tutta l'anima da chi è maestro del
    #    mestiere» + «si nasconde l'estro dell'artigiano».
    121136: "Una libreria costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma nelle parti che di solito non si vedono si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    121198: "Una cassettiera costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma sul retro, che di solito non si vede, si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I DUE MUCCHI DI LIBRI ============================================
    121260: "Libri impilati con cura sul pavimento dopo la lettura. Sono quasi tutti libri da specialisti, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",
    121322: "Libri che dopo la lettura nessuno ha rimesso a posto. Sono quasi tutti rotocalchi, e non ci sarà granché da leggere. \\n# ~Casalinghi che Danno Colore alla Casa~",

    121384: "Un'armatura completa che si porta addosso un'aria severa. Sembra proprio un pezzo con una storia dietro, ma in realtà è una copia e non si può indossare. \\n# ~Catalogo d'Arte di Lumiest~",

    # === LE DUE COSE IN VETRINA, e i due fasci in blocco ==================
    121446: "Un'armatura messa lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Vita da Mercante Dopo l'Avventura~",
    121508: "Un abito messo lì per esposizione. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Palmia: Collezione Primavera-Estate~",
    121570: "Armi e armature legate in fascio per l'esposizione. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",
    121632: "Archi di ogni misura, impilati uno sull'altro. Pare si vendano solo in blocco, e mai a pezzo singolo. \\n# ~Vita da Mercante Dopo l'Avventura~",

    121767: "Una mappa che disegna il continente intero. Avventurieri e non, leggendola, lasciano andare il pensiero alle terre che non hanno ancora visto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # === LE DUE COLONNE ORNATE ============================================
    121891: "Una bella colonna con dei fiori guarniti in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",
    121953: "Una bella colonna con delle piante guarnite in cima. È il ripristino, dicono, di un antico modo di costruire. \\n# ~Catalogo d'Arte di Lumiest~",
}
