# -*- coding: utf-8 -*-
"""Le rese del lotto 037 — gli ATTREZZI, la coda: la categoria si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 037 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa037.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Niente virgolette a caporale, niente accenti in mezzo a una parola, niente
numeri cerchiati: le tre lezioni dei lotti 035 e 036.
"""

IT = {
    # === LA BACHECA E LA TORCIA ===========================================
    90137: "Una tavola con sopra disegnati per esteso vari progetti. Usata in un edificio di tua proprietà, cambia la disposizione della casa senza sprecare forza nelle braccia: un bell'arnese. \\n# ~I Grandi Comprimari della Città~",
    91909: "In ogni tempo l'uomo è stato insieme al fuoco. Dal fuoco il calore che scalda lo spazio, dal fuoco la luce che rischiara la notte. E ora la scintilla della civiltà è nelle tue mani! \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    91911: "\\\"Basta stringerla in una mano e la tua vita nelle Nefia diventa molto più da avventuriero. Prova anche tu questo ottimo arnese per far luce!\\\" \\n# ~Reclame Affissa al Bazar di Vernis~",

    # === IL SALVADANAIO E I DUE DISCHI ====================================
    92252: "Una cassetta dove a ogni uso si mette dentro una certa somma e la si tiene da parte. Che a ogni uso si faccia un po' più pesante sarà di sicuro merito della felicità di mettere da parte. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    92389: "Un disco con dentro delle immagini. Usandolo si richiamano in forma di filmato le memorie del passato, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    # ⚠️ :94601 non ha lo spazio prima del `\\n`; :92389, che gli somiglia, si'.
    94601: "Un disco con dentro della musica. Usandolo suona il brano che ci hanno chiuso, ma purtroppo oggi, di tutta quella tecnica, non è rimasto che il modo di usarlo.\\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === LE DUE COPERTE ===================================================
    # ⚠️ famiglia: stessa forma, cambia l'elemento e il danno che evita.
    92934: "Una coperta messa a punto contro le lame di ghiaccio che sferzano. Impedisce del tutto che il gelo rovini le pozioni, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Autunno-Inverno~",
    92998: "Una coperta messa a punto contro le fiamme che avanzano. Impedisce del tutto che gli oggetti, bruciando, si riducano in carbone, ma tutto ha un limite e fidarsi troppo è vietato. \\n# ~Palmia: Collezione Primavera-Estate~",

    # === IL REGISTRATORE DI CASSA =========================================
    93358: "Una macchina indispensabile quando si comprano e si vendono denaro e merci. Per sicurezza il sistema la rende usabile a una sola persona, quella registrata. \\n# ~Vita da Mercante Dopo l'Avventura~",
    93360: "Una macchina indispensabile per assegnare la gente. Qui si cambia l'incarico dei compagni. \\\"Se per un caso sfortunato la perdete, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto.\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    # === IL RIFUGIO =======================================================
    93823: "Un rifugio semplice che si può montare in caso di bisogno. Passato il pericolo lo si raccoglie e si riusa: un arnese buono a tutto. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # === LO STETOSCOPIO E IL SACCO A PELO =================================
    99091: "Un arnese da medico che, a usarlo, dice sul momento come sta il corpo. Da bambini tutti avranno giocato al dottore, ma un avventuriero di buon senso non lo adoperi mai per fini poco puliti. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    102458: "Un giaciglio semplice, pensato soprattutto per dormire all'aperto. Quando hai sonno ti ci infili tutto e resti chiuso fuori dal mondo: per un poco è pace. \\n#~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # === I QUATTRO ATTREZZI DI MESTIERE ===================================
    # ⚠️ famiglia: il giapponese ha la stessa seconda frase in tutt'e quattro
    #    (当然ながら技術が無ければ扱うことはできない) e cambia solo il
    #    mestiere e la parola per «attrezzo». Le rese seguono.
    104791: "L'attrezzo di base che serve per lavorare le gemme. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",
    120505: "L'attrezzo di base che serve per i lavori di falegname. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",
    120571: "Il set di base che serve per cucire. Va da sé che senza l'abilità non si può adoperare. \\n# ~Casalinghi che Danno Colore alla Casa~",
    122679: "Il kit di base che serve a fare alchimia. Va da sé che senza l'abilità non si può adoperare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # === LA CANNA DA PESCA ================================================
    108457: "L'arnese che serve per pescare. Nei giorni di festa, sulla banchina di Port Kapul, si dice che parecchi pescatori, anzi turisti, se lo stringano in mano sognando di tirare su un pesce grosso, e combattano da soli la loro battaglia. \\n# ~Casalinghi che Danno Colore alla Casa~",
    108459: "\\\"Per pescare conta l'esca, certo, ma più di tutto conta questo. Il resto è facile: butti la lenza e stai fermo ad aspettare. Ah, e va da sé: se l'abilità non ce l'hai, aspetti e basta.\\\" \\n# ~Parole di un Pescatore Fiero della Sua Preda~",

    # === I TRE ATTREZZI DA CUCINA =========================================
    114077: "Un piccolo set da cucina con cui, solo a usarlo, si prepara un po' di tutto. Detto questo, il suo unico pregio è quanto pesa poco: se punti a diventare un professionista, meglio comprare attrezzi da cucina più cari. \\n# ~I Comprimari della Cucina~",
    114141: "Non serve solo da attrezzo da cucina: fa anche luce, e basta posarlo perché aggiunga il suono gentile della fiamma. Tre cose in una. Come attrezzo da cucina però è un po' debole, e finisce che lo si tiene per arredo. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    116346: "Un attrezzo da cucina che cambia tutto: ci butti dentro gli ingredienti, lo usi, e il piatto è fatto. Però, come c'era da aspettarsi, siccome li butti dentro e basta, i piatti complicati vengono male. \\n# ~I Comprimari della Cucina~",

    # === LA CORDA ROBUSTA =================================================
    116603: "Una corda forte che, per quanto la si tiri, non si sfilaccia. È un arnese da usare sulle cose, quindi per legarci una persona pare che non vada bene. \\n# ~Cose Lunghe Fatte per Essere Avvolte~",
    116605: "\\\"Ehi, ehi, che cos'è che ti fa arrabbiare? Io ho risposto a quel che mi è stato chiesto. Semmai mi si dovrebbe ringraziare; prendermi a male parole mi pare fuori luogo. E poi io non ho detto di usarla: ho detto che provare è una delle tante scelte che hai.\\\" \\n# ~Parole di <Lomias> il messaggero di Vindale~",

    # === GLI ATTREZZI DA PITTORE ==========================================
    121829: "Un insieme con tutti gli arnesi che servono per dipingere. Se hai mano per il disegno, provalo. Sempre che tu ce l'abbia, la mano. \\n# ~Regali che Fa Piacere Ricevere~",
}
