# -*- coding: utf-8 -*-
"""Le rese del lotto 027 — il MOBILIO, prima parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 027 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa027.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.
"""

IT = {
    # === LE TRE CERAMICHE DEL CATALOGO D'ARTE =============================
    55673: "Bambole fatte di porcellana cotta due volte. Piacciono molto alle ragazze di nobile famiglia. Corre voce che, infondendovi il potere magico con una formula speciale, si mettano a muoversi. \\n# ~Catalogo d'Arte di Lumiest~",
    55735: "Ceramiche magnifiche, ornate con grande finezza. I pezzi più artistici si vendono a caro prezzo, e spesso non si usano come stoviglie ma come arredo. \\n# ~Catalogo d'Arte di Lumiest~",
    55797: "Riproduzione delle ceramiche che, si dice, stavano allineate nelle tombe delle civiltà antiche. La forma ha la sua grazia, ma al buio mette un po' di paura. \\n# ~Catalogo d'Arte di Lumiest~",

    # === I QUATTRO OGGETTI DEGLI DEI ======================================
    57446: "Un pendolo a forma di Opatos. Pare che un certo artigiano lo ricavi dalla roccia staccata da Opatos stesso. Reagisce ai minerali: gira su sé stesso e ride forte. Fra i minatori si dice che, a scavare, faccia sfuggire di meno il metallo sepolto. \\n# ~Scegliere Bene gli Attrezzi da Artigiano~",
    57508: "Un enorme peluche che Kumiromi ha fatto a propria immagine. Ne regalò alla precedente Ehekatl un numero incalcolabile, e lei li buttò tutti quaggiù. In verità è un oggetto maledetto, fatto per uccidere chi si avvicina a Ehekatl: si muove quando nessuno guarda e assale le creature intorno. Lasciato nel campo fa comodo, perché ammazza gli animali nocivi. \\n# ~Catalogo d'Arte di Lumiest~",
    57707: "Un arredo solenne che riproduce la figura di Itzpalt, e ne accentua il lato di demone del fuoco furioso. Si racconta che un fedele troppo devoto implorò in ginocchio di poter raccogliere la fiamma di Itzpalt, e poi ne fece produzione di massa come un forsennato. Dentro arde la fiamma primordiale carica di magia: applicata alla preparazione dei cibi, brucia via tanto le maledizioni quanto le benedizioni. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    57769: "Opera di un pittore ignoto che assistette a una scena rarissima al mondo: Ehekatl che stringe fra le braccia il pesce che porta fortuna. Entusiasta, l'artista si indebitò per stamparne una gran quantità, ma nessuno le apprezzò e lui morì sconosciuto. Dopo la sua morte si scoprì che questo quadro, appeso in casa, tiene lontani gli ospiti sgraditi, e ora c'è chi lo rivaluta. \\n# ~Catalogo d'Arte di Lumiest~",
    57831: "Un orologio che, passate otto ore di sonno, sveglia per forza. Si ferma dandogli un colpetto in testa. Pare che un tempo lo distribuissero ai fedeli al posto del tesoro sacro, ma i seguaci più accesi di Lulwy lo rubavano e lo distruggevano di continuo, e la produzione fu sospesa. Fra gli appassionati vale un premio; la gente comune non ne capisce il valore. \\n# ~Scoperta! Le Rarità del Mondo~",

    59997: "Un fiore straordinario, che continua a fiorire qualunque cosa gli capiti intorno. Pare che la tecnica della civiltà biochimica lo avesse migliorato perché non appassisse, e che poi sia tornato allo stato selvatico. Oltre che ornamentale ha un certo valore per gli studiosi. All'origine era una pianta antica, ma la forza vitale gli è cresciuta troppo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    63869: "Un utensile da cucina che tritura gli ingredienti e li spreme. Anche senza saper cucinare basta buttarci dentro la roba e premere il pulsante: il succo lo tira fuori da sé. Ottimo arnese per farsi un succo senza fatica. \\n# ~I Comprimari della Cucina~",

    # === IL CUSCINO A CUI L'INGLESE HA TOLTO IL SOGNO =====================
    65331: "Un enorme cuscino soffice a forma di pecora, per dormire bene. Pare che faccia sognare di essere una pecora che dorme in una prateria sconfinata, con addosso un vento gradevole. Ogni tanto però prende un senso di solitudine, e ci si sveglia di soprassalto sentendosi soli.\\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE STATUE ========================================================
    66385: "Una statua a forma di angelo candido. Le ali sono fragili e non vanno toccate alla leggera. Dicono che a salire sul piedistallo venga la sensazione di aver messo le ali. \\n# ~Catalogo d'Arte di Lumiest~",
    66451: "Un piccolo golem di pietra. Piccolo sì, ma se gli si infonde il potere magico si attiva come si deve. È un disegno classico, che oggi non si vede quasi più. \\n# ~Catalogo d'Arte di Lumiest~",
    66513: "Una statua di pietra che, si dice, avvolge chi soffre nella sua misericordia infinita e lo salva. In genere la si considera anche la divinità che protegge i bambini. Dicono che a metterle in testa un cappello di paglia contro la neve venga a sdebitarsi; o forse no. \\n# ~Catalogo d'Arte di Lumiest~",
    66575: "Una statua che riproduce l'oggetto di culto di una religione antica. A volte la si intaglia in un legno sacro, come quello degli alberi consacrati, ma a vederla non cambia niente. Ha valore artistico, e c'è chi le colleziona. \\n# ~Catalogo d'Arte di Lumiest~",
    66641: "Un piccolo golem di legno. Piccolo sì, ma se gli si infonde il potere magico si attiva come si deve. È un disegno classico, che oggi non si vede quasi più. \\n# ~Catalogo d'Arte di Lumiest~",

    66703: "Una casetta per gli animali domestici. È fatta con cura, perché non ci passi uno spiffero. Chi ama gli spazi stretti ci starà comodo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I QUATTRO STRUMENTI ==============================================
    68848: "Uno strumento di ceramica a forma di goccia. La forma e il numero dei fori non sono fissi. Ha un'imboccatura quasi identica a quella del flauto dolce, e il suono viene facile. \\n# ~Le Melodie della Limpida Irva~",
    68913: "Un flauto diritto: il nome che porta in un'altra lingua vuol dire chi registra. Una struttura particolare, il becco, tiene ferma la colonna d'aria e rende facile suonarlo. In compenso ha poco volume e un timbro difficile da colorare, e per questo lo si tiene per uno strumento da principianti. \\n# ~Le Melodie della Limpida Irva~",
    68978: "Un ottone molto grosso, molto lungo e nero lucente. Serve soprattutto a rinforzare il volume, ma in pratica lo si usa di rado ed è ormai uno strumento a rischio di estinzione. \\n# ~Le Melodie della Limpida Irva~",
    74568: "Uno strumento a percussione fatto di una cassa di legno con la pelle tesa sopra. In genere risuona benissimo, e la coda del suono resta a lungo. \\n# ~Le Melodie della Limpida Irva~",

    70127: "Una miniatura fuori scala che riproduce fedelmente una nave magica volante. Purtroppo non sta a galla.\\n# ~Catalogo di Vendita di Irva Airlines~",

    # === I DUE KOMA-INU, che l'inglese fa uguali ==========================
    72822: "Un koma-inu con la bocca aperta. C'è chi lo chiama leone. Va messo a destra, guardando il cancello. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    72884: "Un koma-inu con la bocca chiusa. Va messo a sinistra, guardando il cancello. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    73352: "Un attrezzo di tortura in legno. Fa male all'inguine sfruttando il peso di chi ci sta sopra. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    73354: "\\\"Nel nostro giro è un premio!\\\" \\n# ~Parole di un Avventuriero che si è Risvegliato~",

    76520: "Un magnifico castello fatto con la sabbia della spiaggia. Opera di qualcuno che era venuto per nuotare e si è perso a giocare con la sabbia. È ben compattato, e più solido di quanto sembri.\\n# ~Viaggio in Tyris del Nord: Estate~",

    78789: "Una stoviglia piatta su cui si mette il cibo. Ce n'è di ogni sorta, dalla migliore alla peggiore: certe si usano tutti i giorni, altre valgono tanto da poterci comprare un cavallo. \\n# ~I Comprimari della Cucina~",

    # === LE DUE BESTIE RIDOTTE A MOBILE ===================================
    78919: "La pelle di una bestia feroce abbattuta, conciata e ridotta a suppellettile. Usarne una intera è un lusso, e l'insieme dà l'impressione che là dentro sia rimasto qualcosa di selvatico. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    78981: "La testa di una bestia abbattuta, trattata in modo speciale e ridotta a suppellettile. C'è qualche nobile a cui non basta appenderla: si lavora da sé la preda che ha cacciato, e così si sazia la voglia di possesso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === IL MOBILIO DI CASA ===============================================
    79044: "Un divano dall'aria costosa, rivestito di una pelliccia morbidissima. Ci si sta benissimo seduti, ma è un mobile un po' delicato e tenerlo in ordine costerà parecchie attenzioni. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    79303: "Un armadietto di gran classe, piacevolissimo al tatto. Ha un che di adulto nell'aria che si porta dietro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    79366: "Una libreria in cui pare ci stiano libri di ogni sorta. A quanto si racconta, tutto cominciò quando uno storico ormai ritirato ordinò il mobile ideale per mettere in ordine i libri che gli traboccavano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    79950: "Un mobile che serve a parlare e a fare i conti, e insieme fa da divisorio. Dicono che a conversare da dietro venga la sensazione di aver aperto bottega. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE FESTE =========================================================
    79636: "Un piccolo albero di Natale. È l'albero per la famiglia comune, che vuole festeggiare ma non ha in casa lo spazio per un albero vero. \\n# ~Viaggio in Tyris del Nord: Inverno~",
    79698: "Un ornamento fatto apposta per le feste. Si ritiene che serva da segnale perché un dio straniero possa scendere. \\n# ~Viaggio in Tyris del Nord: Inverno~",
    80082: "Un ornamento fatto apposta per le feste. Ognuno lo intreccia con i fiori che preferisce, e così le forme sono le più varie. \\n# ~Viaggio in Tyris del Nord: Inverno~",
    79826: "Una bancarella tirata su alla svelta per vendere roba durante una festa. A passarci accanto, certe volte si sente un suono che dà fresco. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    79888: "Una bancarella tirata su alla svelta per vendere roba durante una festa. A passarci accanto, certe volte si sente un profumo tostato con dentro una punta di acido. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    79764: "Un cuscino da abbracciare, morbido, con sopra dipinta la dea della cura. Dicono che, stringendo quel lungo cilindro, la dea in persona porti al fondo del sonno non solo i fedeli ma chiunque lo usi, e che nel sogno gli guarisca il corpo e l'animo.\\n#~I Mondi che Non Hai Mai Visto~",

    80012: "Un gradino da poco che dà l'impressione di vedere il mondo un piano più su. Quando si vuole dire la propria, conviene salirci e parlare da lì. \\n# ~I Grandi Comprimari della Città~",

    80149: "Il pianoforte prediletto di un compositore geniale e solitario. Pare che abbia ereditato in potenza il suo modo tutto personale di leggere i pezzi altrui, e che a suonarlo quel modo riaffiori nel timbro. \\n# ~Dizionario Fantastico di Irva~",
}
