# -*- coding: utf-8 -*-
"""Le rese del lotto 028 — il MOBILIO, seconda parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 028 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa028.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.
"""

IT = {
    # === I DUE REGALI =====================================================
    80612: "Un balocco rosso che si tiene per portafortuna. In terra straniera vanno per lo più quelli senza occhi dipinti: ogni volta che un desiderio si avvera, gliene si disegna uno con l'inchiostro nero. \\n# ~Regali che Fa Piacere Ricevere~",
    82275: "Un dono che si usa per dire, al posto proprio, quel che si sente. Naturalmente non si può usare. \\n# ~Regali che Fa Piacere Ricevere~",

    80674: "Un mobile che scalda, per la stagione fredda. A infilarcisi sotto ci si sente esploratori di caverne, e pare che i bambini che lo dicono e poi si addormentano lì dentro non finiscano mai. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE DUE SCALE, che si rispondono ==================================
    80798: "Benvenuti nel sottosuolo! Questo attrezzo eccellente apre in un attimo una via che porta agli spazi sotterranei. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    80860: "Bentornati in superficie! Questo attrezzo eccellente apre in un attimo una via che porta al mondo di fuori. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    82875: "Un letto di qualità altissima, che qualcuno dice perduto da un dio. Quel tocco gentile, dicono, fa ricco il cuore di chi ci dorme.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    83764: "Il violino leggendario che, si dice, va a cercarsi i maestri dell'esecuzione. Il suo timbro risuona forte nel cuore di chi ascolta, e non finiscono mai quelli che fanno un dono di riconoscenza a chi suona. \\n# ~Dizionario Fantastico di Irva~",

    # === I QUATTRO STRUMENTI ==============================================
    84709: "Uno strumento a corde che si tiene con tutte e due le mani e suona a pizzico. Portarselo dietro non è comodo, ma il suo suono disteso metterà chi ascolta in uno stato d'animo elegante. \\n# ~Le Melodie della Limpida Irva~",
    84774: "Uno strumento particolare, che porta la melodia con un suono leggero. Il suono allegro che esce da quel corpo piccolo, dicono, mette allegria anche a chi ascolta. \\n# ~Le Melodie della Limpida Irva~",
    84839: "Uno strumento a corde che dà suono se lo si gratta. La forma singolare, come un uovo tagliato per il lungo, serve a far risuonare il suono all'interno e a dare profondità al timbro. \\n# ~Le Melodie della Limpida Irva~",
    84904: "Uno strumento a fiato fatto di più canne accostate. L'intonazione fa fatica a restare ferma, e chi lo suona deve accordarlo di continuo. \\n# ~Le Melodie della Limpida Irva~",

    # === I DUE DIVISORI ===================================================
    84644: "Un mobile che si usa per dividere le stanze. Dà alla casa un'aria di eleganza. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87002: "Un paravento pieghevole, di quelli che fanno atmosfera. Pare che in terra straniera un giovane monaco abbia provato una volta ad abbattere la tigre chiusa dentro uno di questi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I LUMI E LE FINESTRE =============================================
    87064: "Un lume fatto per portarlo in giro comodamente. Oltre a servire da ornamento, in terra straniera pare che le guardie se lo portino appresso per la ronda di notte. \\n# ~Casalinghi che Danno Colore alla Casa~",
    87126: "Una finestra tonda, tutta profumo di terre lontane. Montata in casa, dicono, mette addosso la sensazione di essere in viaggio all'estero. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87188: "Una costruzione di pietra fatta per posarci dentro un lume. Basta che ce ne sia una perché tutto intorno si riempia di un'aria solenne. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87955: "Una finestra da interni con un divisorio montato sopra. Dicono che le dame a cui dà noia essere spiate la comprino a gara. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    90074: "Una finestra che mette in scena uno spazio in cui riposare. La luce tiepida che entra dal telaio saprà dare un momento di quiete. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    90261: "Una finestra comune, di quelle che si vedono dappertutto. Non ha nessuna particolarità di rilievo, ma si trova facilmente e per questo circola molto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    90323: "Una finestra che si riconosce dal telaio di metallo duro. Tanto duro, dicono, che una volta lo adottarono in un campo di prigionia. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    91088: "Una grande opera che raccoglie il fior fiore dell'arte. La luce che entra passandoci attraverso commuove e stupisce. \\n# ~Catalogo d'Arte di Lumiest~",

    # === I DUE LETTI DI FAMA ==============================================
    87319: "Un letto un po' largo, per due. Il conto è di due persone, ma stringendosi ci si sta anche in quattro, e capita che una brigata di avventurieri al verde divida la spesa e ci dorma tutta insieme.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    90012: "Un letto di gran fama, fornitore del re. Del sonno morbido non c'è nemmeno da dire: fatto com'è con ogni sorta di lusso, è il sogno più grande di chi ama i mobili.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    87381: "Roba inutile raccattata e ammucchiata fin su, pesantissima. Non è cosa che di solito si porti in giro; ma se proprio tocca farlo, conviene stare attentissimi a non finire parte del mucchio.\\n#~Le Mille Cianfrusaglie che Amo~",

    # === LA CUCINA E LA CASA ==============================================
    87443: "Un lavello che si prende in carico tutto il lavoro dell'acqua. È enorme e pesa molto, quindi a portarlo in giro ci vuole attenzione. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87505: "Una credenza costruita con tutta l'anima da chi è maestro del mestiere. A prima vista sembra semplice, ma nelle parti che di solito non si vedono si nasconde l'estro dell'artigiano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87707: "Un divano ampio, di una stabilità eccellente. È il mobile giusto per starsene in pace a casa propria. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87893: "Una cassettiera di gran fama, fornitrice del re. È decorata così vivacemente da rimetterci in funzionalità. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    88083: "Un sacco di paglia pieno di granaglie. Si usa molto perché lascia passare l'aria e il grano si guasta poco. \\n# ~Casalinghi che Danno Colore alla Casa~",
    90449: "Un ottimo arnese da cucina che lavora a fiamma viva. Il profumo tostato che si spande cucinandoci sarà il miglior condimento per chi mangia. \\n# ~I Comprimari della Cucina~",
    90637: "Una poltrona autorevole, che offre una seduta distesa. A quel che si dice, il modo ufficiale di sedercisi è con un gatto d'argento nella mano sinistra e un whisky nella destra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE DUE TAVOLE SU CUI SI SCRIVE ===================================
    87769: "Una tavola enorme su cui si scrive col gesso bianco e si cancella. Quasi tutte le scuole ne hanno una. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    87831: "Una tavola con scritta la lista dei piatti. Ci sono le specialità del locale, ma di che città siano non è chiaro. \\n# ~I Grandi Comprimari della Città~",

    87644: "Un'aiuola a cui hanno montato una recinzione semplice, per proteggere i fiori piccoli. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I DUE PORTALI ====================================================
    88803: "Un portale che dà una sensazione di pericolo. Dicono che dentro quella luce che ondeggia inquieta si vedano a tratti figure deformi, o si sentano delle grida.\\n#~I Mondi che Non Hai Mai Visto~",
    89212: "Un portale di legno che, si dice, segna il dominio di un dio straniero. Tinto di rosso, ha in sé qualcosa che fa pensare allo slancio della vita.\\n#~I Mondi che Non Hai Mai Visto~",

    89946: "Una costruzione ad arco ornata di fiori. Come mai, a passarci sotto, si prova un po' di imbarazzo? \\n# ~I Grandi Comprimari della Città~",

    # === LE QUATTRO PIANTE ================================================
    90199: "Una pianta curata dall'uomo quanto basta. Se non perde mai la forma per quanto tempo passi, sarà perché c'è un giardiniere di strada che la pota per bene senza farsi vedere. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    90385: "Una pianta dalla forma simpatica. Di notte, quando tutti dormono, sguscerebbe piano dal vaso e correrebbe libera fuori città: è una frottola che in questi anni a Palmia fa ridere la gente. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    90511: "Una pianta in vaso che dà un'aria da paese tropicale. Quando i soldi non ci sono, si compri questo vaso e ci si immagini di essere ai tropici. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    90573: "Una pianta in vaso che, dicono, toglie la stanchezza dagli occhi. Se sia per via esterna o perché va ingerita, lo sa solo chi la vende. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # === LA PIETRA ========================================================
    91150: "Una colonna fatta apposta per sostenere il soffitto. La forma singolare le permette di reggere un peso molto maggiore di una colonna normale. \\n# ~Catalogo d'Arte di Lumiest~",
    91212: "Una suppellettile che incarna la forza e l'autorità di un essere sublime. È così grande, dicono, da schiacciare chi la guarda e fargli piegare le ginocchia da sé. \\n# ~I Mondi che Non Hai Mai Visto~",

    # === LA NEVE ==========================================================
    91274: "Un lampione che la neve ha reso ancora più elegante. Nelle notti di neve la luce che questo signore allampanato getta con dolcezza, dicono, accende il fuoco fra due innamorati. \\n# ~I Grandi Comprimari della Città~",
    91336: "Un barile posato sotto il cielo freddo, che si è truccato di bianco. A vederlo, lo si scambierebbe per un'opera d'arte. \\n# ~I Grandi Comprimari della Città~",
    91398: "Un pupazzo di neve piccolo, nato dall'idea di avere la neve a portata di mano. Quel muso adorabile non cambia nemmeno rimpicciolito, e continua a guardare il mondo. \\n# ~Viaggio in Tyris del Nord: Inverno~",
}
