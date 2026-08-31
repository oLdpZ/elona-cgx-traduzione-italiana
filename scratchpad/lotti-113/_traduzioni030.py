# -*- coding: utf-8 -*-
"""Le rese del lotto 030 — il MOBILIO, quarta parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 030 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa030.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ `:111511` e' l'unica riga del lotto dove l'inglese **non** mette lo spazio
prima del `\\n`. Si conserva com'e'.
⚠️ `:112509` non ha giapponese affatto: e' un'aggiunta del CGX, e la fonte e'
l'inglese.
"""

IT = {
    # === LA RUNA E L'ORO ==================================================
    108393: "Una pietra con sopra scritti caratteri antichi. A usarla, dicono, si apre l'ingresso di un posto che non sta in questo mondo. \\n#~I Mondi che Non Hai Mai Visto~",
    108829: "Una statua d'oro dal luccichio vistoso, fatta a immagine della ricchezza. A tenerne in casa parecchie, dicono, l'amico che torna dopo tanto ti dà del nuovo ricco. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",
    108891: "Un'opera d'arte sfolgorante: una colonna d'oro guarnita di erbe e fiori. Belli gli intagli minuti, ma è il materiale che conta: di notte, dicono, prende la luce intorno e brilla ancora di più. \\n# ~Catalogo d'Arte di Lumiest~",

    # === IL TRONO E IL TAVOLO, che l'inglese confonde =====================
    108954: "Una sedia magnifica, fatta perché ci si sieda il re e nessun altro. Nessuno ha pensato a produrla in serie, e così è lavorata con ogni lusso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    # ⭐ l'inglese di questa riga e' la COPIA di quello del trono. Il
    #    giapponese parla d'altro, e vince lui.
    109083: "Un tavolo con sopra della roba. A giudicare dalla grandezza, più che un tavolo sarebbe giusto chiamarlo scrivania. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    109145: "Un bel tessuto dell'ultimo modello. È fatto in modo così delicato che non lo si può nemmeno provare. \\n# ~Palmia: Collezione Autunno-Inverno~",
    109270: "Una suppellettile da cui si sente la maestà. Sarà la sua virtù miracolosa, o forse che la lucidano ogni giorno: di notte fa una luce viva tutto intorno. \\n# ~I Mondi che Non Hai Mai Visto~",

    # ⭐ l'inglese perde la negazione: 長旅には適さない, per un viaggio lungo
    #   NON va bene.
    109335: "Uno strumento a tasti che pare una scatola nera rettangolare. È più leggero del pianoforte a coda, ma pesa comunque anche troppo, e per un viaggio lungo non va bene. \\n# ~Le Melodie della Limpida Irva~",

    109398: "Una sedia lunga di traverso, fatta di materiale duro. Quando ne mettono una all'aperto, dicono, ogni tanto ci si trova qualcuno che ci schiaccia un pisolino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I SETTE SCAFFALI E LE DUE TOELETTE ===============================
    109460: "Uno scaffale che insegue fino in fondo la bellezza dell'utile. Non ha nemmeno una funzione di troppo: un mobile di una nettezza esemplare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    109713: "Una toeletta che insegue all'estremo la bellezza dell'utile. Un mobile così risoluto da far pensare che basti lo specchio e nient'altro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    109775: "Uno scaffale pulito, senza un granello di polvere. Ha fama di restare così per anni, e per questo, dicono, lo compra spesso il cliente pigro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    109966: "Una libreria tanto vecchia che perfino i libri dentro sembrano avere una storia. Quel modo tutto suo di essersi rovinata, dicono, manda in visibilio chi ama le cose antiche. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110028: "Uno scaffale che ha addosso, chissà da dove, un'aria di cose passate. Al tatto somiglia al tepore del legno che da bambini si è toccato di sicuro. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110603: "Uno scaffale di fattura spartana. Costa poco, e per chi vive da solo tanto basta. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110541: "Una toeletta di quelle che usano tutti. È un mobile il cui valore si misura in fondo su quanti ornamenti porta, e quanto a servire allo scopo questa non ha niente da farsi perdonare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111188: "Una toeletta che dà l'idea di costare parecchio. È uno dei mobili che le donne sognano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    109588: "Un piccolo altare che risplende. Conta più come suppellettile che come altare, e infatti pare che non ci si possano fare offerte. \\n# ~Casalinghi che Danno Colore alla Casa~",
    109650: "Una credenza fatta più grande del solito. È un mobile pensato per i nobili, che invitano molta gente e danno feste. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    109837: "Un tavolo a cui hanno dato apposta un piano tutto gobbe, per un'intenzione d'arte. Fatto così, per il lavoro di precisione non va. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I SETTE GIACIGLI =================================================
    109526: "Un giaciglio così morbido che la mano ci affonda. Quando il letto che cede al punto giusto si unisce a una coperta piena di odore di sole, dicono, ti prende una sensazione strana, come di essere tornato neonato. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    # ⭐ l'inglese rovescia la frase: 余り疲れは取れない, la stanchezza NON se
    #   ne va. L'inglese scrive «you will probably not get very fatigued».
    109903: "Un giaciglio con il minimo indispensabile e nient'altro. C'è chi dice che serva più a passare il tempo a occhi chiusi che a dormire, e infatti a usarlo la stanchezza non se ne va granché. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110478: "Un giaciglio ben teso fin sull'orlo del lenzuolo. È così pulito che spesso, dicono, per venderlo lo paragonano alla bianca guaritrice. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110669: "Un giaciglio dai colori riposanti, che calmano l'animo. È un letto semplice, senza una funzione di troppo, e forse per questo pare piaccia molto anche agli uomini. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110865: "Un giaciglio che qua e là comincia a cedere. Basta stendercisi che scricchiola e fa baccano, e chi ha il sonno delicato non riuscirà a dormirci. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    110931: "Un giaciglio dove ci si sdraia a gambe e braccia larghe e avanza ancora posto. Comodo quando arrivano ospiti all'improvviso e bisogna far dormire tutti insieme. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111324: "Un giaciglio di gran classe, fatto di materiali pregiati senza risparmiarne un filo. Al tatto è così liscio da far credere per un attimo di avere davanti un'opera d'arte. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    110090: "Una pianta in vaso che si fa notare per il fogliame folto e verdissimo. Le foglie tenere, allungate proprio di lato, traboccano davvero di vita. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # === I QUATTRO TAVOLI DA GIOCO ========================================
    110155: "Un tavolo da gioco dove ci si diverte a piantare la freccetta dove si mira. Pare che qualche avventuriero ci giochi per mettersi alla prova e vedere se è migliorato nel lancio. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    # ⭐ l'inglese butta via la prima frase e sbaglia la seconda: i sette
    #   devono venire TUTTI E TRE (７が揃った), non uno qualunque.
    110220: "Un tavolo da gioco dove ci si diverte a far combaciare le figure. Pare ci sia una leggenda: quando nei tre riquadri escono tre sette, dal cielo rimbomba uno strano grido che nessuno sa spiegare. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    110285: "Un tavolo da gioco con ogni sorta di svaghi da adulti. Si vanta che ci si può fare di tutto, ma il commesso non demorde e ti lascia giocare solo a blackjack. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    110350: "Un tavolo da gioco che va a palline di metallo. Ci si gioca anche da soli e in poco tempo, ma pare che a volte ci si scaldi troppo e ci si accorga solo dopo che è venuta notte. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    110412: "Un mobile che si riempie d'acqua calda e cura il corpo di chi ci si immerge. Fra i nobili, pare, va di moda farci galleggiare sopra la schiuma. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    110733: "Un ottimo arnese da cucina che sminuzza i cibi con lame affilate. A Palmia, un tempo, pare ci fosse una coppia di mercanti che per vendere questo arnese carissimo si metteva a recitare una scenetta un po' finta. \\n# ~I Comprimari della Cucina~",

    # === LA BARA, e chi ci ha provato =====================================
    110799: "Un giaciglio che chi è vivo di regola non usa. Almeno ripara dalla pioggia e dal vento, e pare che qualche avventuriero, non avendo di meglio, ci si adatti. \\n#~Libro in Dono a Chi Sta Morendo~",
    110801: "\\\"È così duro che tenerlo per giaciglio è quasi uno spreco, e finché ci stai dentro non ti arriva un colpo da nessuna parte. Il difetto, semmai, è che per colpire devi uscirne\\\" \\n# ~Parole di <Ainc> il cavaliere novizio~",

    110993: "Una cassettiera che serve solo a riporre i vestiti. È fatta un po' più larga del solito, così da tenerli divisi per stagione. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111125: "Un tavolo di pregio, fatto apposta per stare in una taverna. Ci sta dentro più roba di prima, e intanto la misura è rimasta quella. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111258: "Un vaso cotto in un materiale che ha tutta l'aria di costare caro. La superficie è lucida al punto di brillare. \\n# ~Catalogo d'Arte di Lumiest~",
    111386: "Un armadietto costruito per tenerci i liquori. Tirarne fuori una bottiglia di nascosto e berla fa odiare a morte da chi la teneva da parte per il piacere: meglio lasciar perdere. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111449: "Un tavolo consumato da anni di uso, che qua e là comincia a cedere. Se lo si tiene lo stesso è anche perché ci si è abituati, ma soprattutto per affetto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ⚠️ l'unica riga del lotto senza lo spazio prima del `\\n`.
    111511: "Un tessuto di filo che assorbe molto bene l'acqua. Ammorbidente non ne ha visto.\\n# ~Palmia: Collezione Autunno-Inverno~",

    # === I DUE SCAFFALI GEMELLI, che dicono la stessa seconda frase =======
    111573: "Uno scaffale stipato di ninnoli di ogni genere, che non ci sta più niente. Il mucchio sta su per un equilibrio così preciso che di lì non si può tirare fuori niente. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    111635: "Uno scaffale stipato di roba di tutti i giorni, che non ci sta più niente. Il mucchio sta su per un equilibrio così preciso che di lì non si può tirare fuori niente. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    111697: "Un'armatura lucidata a dovere e pronta a ogni evenienza. Su ogni pezzo c'è scritto che è già venduto, e perciò non la si può indossare di propria iniziativa. \\n# ~Vita da Mercante Dopo l'Avventura~",
    112320: "Una mappa che si porta addosso un'aria di mistero. Ha solo quell'aria, dicono: un effetto degno di nota non ce l'ha. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    112382: "Un attrezzo che aumenta il galleggiamento, usato soprattutto da chi non sa nuotare. A Porto Kapul capita spesso di vederlo addosso ai bambini del posto. \\n# ~Casalinghi che Danno Colore alla Casa~",
    112445: "Un tavolo rotondo che ha qualcosa di caldo. Come mai viene voglia di usarlo senza sedie, o di prenderlo per il bordo e rovesciarlo? Chi lo sa. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LA TINOZZA, e l'appunto senza giapponese =========================
    112507: "Un attrezzo pesantissimo, colmo d'acqua fino all'orlo. Serve soprattutto per il bestiame, e pare che nemmeno l'avventuriero più intraprendente ci metta le mani. \\n# ~I Grandi Comprimari della Città~",
    112509: "\\\"Non adatto ai golem\\\" \\n# ~un appunto misterioso~",

    112569: "È il secondo chiaro di luna. Loro, senza mai riposare, disegnano l'ombra della gente che passa per la strada. \\n# ~I Grandi Comprimari della Città~",

    # === LE DUE COLONNE ===================================================
    112631: "Una colonna pesantissima, spezzata alla base per chissà quale ragione. Quella forma che è solo sua ha, chissà come, qualcosa d'arte. \\n# ~Catalogo d'Arte di Lumiest~",
    112693: "Una colonna pesantissima e fiera, che sale dritta verso il cielo. Quella figura che non si muove di un capello fa venire in mente il dio della terra. \\n# ~Catalogo d'Arte di Lumiest~",
}
