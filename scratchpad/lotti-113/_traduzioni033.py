# -*- coding: utf-8 -*-
"""Le rese del lotto 033 — gli ATTREZZI, prima parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 033 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa033.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️⚠️ **In questo lotto la spaziatura prima del `\\n` NON e' uniforme**: qui
l'inglese scrive ora uno spazio, ora nessuno, ora **due** (`:45549`, `:45615`,
`:45681`). Ogni riga copia il suo, e `:45944` porta perfino un `\\n` **in coda**
che nessun'altra riga ha.
⚠️ `:47287` e `:47288` non hanno il `#` davanti alla fonte: l'inglese l'ha
perso, e il cancello di `_112-corpo-descrizioni` conta i `#` **contro
l'inglese**. Si conserva com'e' — vedi `testa033.py`.
"""

IT = {
    # === I QUATTRO FUCILI ANESTETICI ======================================
    # ⚠️ le quattro descrizioni sono identiche a meno della fascia di peso, e
    #    le loro righe di indice 1 e 2 sono UNA firma sola per tutte e quattro.
    42415: "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 500 e i 1000 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",
    42491: "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 100 e i 500 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",
    42567: "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso fra i 30 e i 100 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",
    42643: "Un fucile anestetico a ripetizione. Spara dardi speciali che fanno svenire i bersagli di peso inferiore ai 30 chili, ma l'effetto ci mette un po' ad arrivare. Una dose eccessiva distrugge i nervi, e su chi supera il peso giusto l'effetto cala di molto. Per non ferire con l'urto il lancio è a gas e ha poca forza: da lontano il dardo non si pianta, ed è un altro difetto. \\n#~Difendersi dai Mostri, da Qui in Avanti~",
    42416: "\\\"Non c'è la seccatura di cambiare la miscela caso per caso; dentro la gittata utile il colpo va a segno e si pianta, l'effetto arriva puntuale dopo un tempo fisso, e per giunta si spara a ripetizione. È senza dubbio la miglior serie di fucili anestetici che ci sia oggi\\\" \\n# ~Parole del Tiratore Anestetista~",
    42417: "\\\"Se lo scopo è liberarsene, non è più rapido e più sicuro sparargli e basta?\\\" \\n# ~Parole del Cacciatore Esperto~",

    42709: "Bacchette di legno, ricavate dagli scarti della lavorazione del legname. Usate contro chi si ha davanti servono a fingere un colpo: abbassano la barra di potenza del nemico e gli impediscono di usare le tecniche che la consumano. Si possono anche piantare per terra. \\n#~I Comprimari della Cucina~",
    43240: "Un oggetto magico con dentro una pietra magica. Mettendo una carta nella cassetta in basso, dallo specchio in alto esce un raggio che trasforma nell'aspetto della creatura sulla carta. L'effetto non si scioglie finché non lo si usa di nuovo o non si muore, ma attenzione: non confonde chi guarda come fa il set da travestimento. È costruito sul meccanismo con cui il mimic si mimetizza, e per questo lo chiamano anche specchio mimetico.\\n#~Compendio Completo degli Oggetti Magici~",

    # === LA GABBIA E I DUE ARNESI DA SCHIAVI ==============================
    44097: "Uno strumento di costrizione messo a punto a Eulderna. Serviva soprattutto a portare via gli animali da esperimento e i maghi colpevoli di reati gravi. Da qualche anno le sfere dei mostri e la magia del dominio, che rendono obbedienti sul momento, si sono diffuse, e questa gabbia è diventata un pezzo da antiquario. Accendendola diventa azzurra, ma per risparmiare la magia di levitazione non resta accesa: la gabbia fluttua solo quando la si sposta. \\n#~Storia degli Strumenti di Costrizione~",
    44163: "Un arnese che ricava energia facendolo girare a uno schiavo. I modelli vecchi erano così pesanti che ci volevano più persone per muoverli, ma con la moda recente del risparmio di schiavi si è imposto il tipo leggero, che una persona sola riesce a far girare. \\n#~Gestire uno Schiavo, da Oggi~",
    44229: "Un arnese che ricava energia facendo correre uno schiavo. I criceti la fanno girare che sembrano divertirsi, e anche chi criceto non è ci trova un po' di moto e ci guadagna in salute. Quindi farci correre qualcuno a forza, probabilmente, non conta come maltrattamento. \\n#~Gestire uno Schiavo, da Oggi~",

    45481: "Una pietra bianca che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Spende potere abissale e piazza una trappola magica semplice dove sta chi la usa. Si dice anche che con una dote particolare la si possa far scattare da lontano, ma finora nessuno l'ha dimostrato. La forza della trappola dipende da Dispositivi magici, da Disarmo trappole e anche dalla profondità del piano. \\n#~Dizionario Fantastico di Irva~",

    # === LE TRE PIETRE, e i tre rapporti senza giapponese =================
    # ⚠️ `:45549`, `:45615` e `:45681` non hanno giapponese affatto: sono
    #    aggiunte del CGX, e la fonte e' l'inglese. Portano DUE spazi.
    45547: "L'esperienza di chi è forte, mezza fatta materia per il concorso di più condizioni. A usarla si riceve un'intuizione travolgente, come una scarica di corrente.\\n#~Dizionario Fantastico di Irva~",
    45549: "Una pietra che dà AP.  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",
    45613: "Il conduttore magico dentro le cellule, addensato dal contraccolpo del mana. Quel che succede è in sostanza una distruzione di cellule, e il processo fa un male tremendo. A usarla il conduttore si ripara un poco e la magia torna a circolare meglio.\\n#~Dizionario Fantastico di Irva~",
    45615: "Una pietra che dà poteri magici (MP).  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",
    45679: "Ardore di combattimento sprigionato di colpo, che si è combinato con l'etere e si è rappreso. Prende quella forma di fiamma, dicono, per come l'etere si distribuisce e per i sussulti dell'animo. È come un grumo di voglia di fare: a usarla la stanchezza si allenta e viene da credere di poter reggere ancora un po'.\\n#~Dizionario Fantastico di Irva~",
    45681: "La pietra dà costituzione e SP.  \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # === I TRE FARMACI ====================================================
    # ⭐ l'inglese del Res upper butta via che fine facevano le fate.
    45745: "Un farmaco messo a punto per adattarsi agli ambienti più duri. Attivando le difese del corpo, dicono, dà resistenze senza bisogno di quel che si porta addosso. Ci fu un periodo in cui girava la fandonia che si ricavasse dalla polvere delle ali delle fate, e le fate a cui la strapparono, con le ali spelacchiate e rade, furono parecchie: ma sono cose di molto tempo fa.\\n#~Veleno o Medicina: Modo e Dose~",
    45747: "Uno strumento che alza ogni resistenza fino a un certo livello. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",
    # ⚠️ `:45811` e `:45877` dicono la stessa seconda frase: resa identica.
    45811: "Un farmaco che rafforza per sempre la prontezza dei riflessi e alza l'evasione. Detto questo, se quel che si ha addosso è scadente non serve a molto: dà il meglio quando è roba buona ad amplificarlo. \\n#~Veleno o Medicina: Modo e Dose~",
    45813: "È uno strumento che alza il modificatore DV. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",
    45877: "Un farmaco che rafforza per sempre la tenuta della pelle e alza la difesa. Detto questo, se quel che si ha addosso è scadente non serve a molto: dà il meglio quando è roba buona ad amplificarlo. \\n#~Veleno o Medicina: Modo e Dose~",
    45879: "È uno strumento che alza il modificatore PV. \\n#~Rapporto di Identificazione: categoria <Oggetti>~",

    # === IL TELAIO X, e i due militari che non si mettono d'accordo =======
    # ⚠️ questa e' l'unica riga del lotto che porta un `\\n` IN CODA.
    45944: "Un pezzo che, smontato e rimontato, cambia prestazioni secondo la situazione: dalla forma a X si trasforma in altre sei. In origine era un accessorio per le grandi macchine da guerra, ma fu giudicato troppo complicato per servire a qualcosa e restò sulla carta. Ne fecero anche un modellino per spiegarne il meccanismo, e a trasformarlo come si deve riuscirono in pochi.\\n# ~Dizionario Fantastico di Irva~\\n",
    45945: "\\\"Le prestazioni non erano male e nella trasformazione ci sentivo del romanticismo: a dirla tutta il budget avrei voluto darglielo...\\\" \\n#~Parole di <Heinrich> il generale corazzato~",
    45946: "\\\"Un pezzo che dà pena a produrre in serie e pena a mantenere, e che per giunta è pesante e ingombra, non va bene neanche se rende\\\" \\n#~Parole di <Milis> la comandante delle forze speciali~",

    # === LA MUFFA E I PEZZI DI CADAVERE ===================================
    46076: "Un aggregato di muffe melmose particolari. Funziona come un calcolatore e si muove a piacere per segnali elettrici. La civiltà di un tempo sapeva perfino scaricare in questa muffa il carattere e le abilità di una persona. Le armi non morte fatte di muffa, dicono, cambiarono da cima a fondo le guerre di allora.\\n#~Tecnologia Perduta: un Barlume~",
    46142: "Un cadavere fatto a pezzi e riempito di muffa melmosa. Attaccato a qualcuno si muove a piacere, ma con la tecnica di oggi, se quella parte del corpo già c'è, il rigetto impedisce l'innesto.\\n#~Tecnologia Perduta: un Barlume~",
    46144: "\\\"Anche solo per farti crescere un braccio: lo vuoi bello? deforme? meccanico? Già che lo monti, vorrai curare anche i pezzi piccoli! Componitelo come piace a te e vinci le tue battaglie!\\\" \\n#~Parole di un Negromante Annoiato~",

    # === I TAPPI DI SUGHERO, e i due che litigano =========================
    46403: "Un assortimento di tappi di sughero, di quelli che chiudono le bottiglie delle pozioni. Siccome c'era, chissà perché, un certo numero di clienti che voleva solo i tappi, è nato un prodotto che ricicla gli scarti. A vederli sono quasi tutti uguali per forma e misura, ma l'alchimista o l'officina che li ha fatti ci mette un segno tutto suo, e cambia anche il materiale: un appassionato, pare, li riconosce tutti.\\n#~Quel che Brilla nel Mucchio dei Rifiuti~",
    46404: "\\\"Ma non sono tutti uguali?!\\\" \\n#~Parole di un Profano Disorientato~",
    46405: "\\\"Ecco perché i profani non vanno bene! Guarda meglio!\\\" \\n#~Parole di un Fissato in Piena Spiegazione~",

    46479: "Un cannone a fotoni di grosso calibro. Per questo, pur chiamandosi bazooka, non spara razzi, e per costruzione rientra fra i cannoni senza rinculo. D'altra parte anche il bazooka lanciarazzi si chiama così perché somigliava allo strumento musicale che porta quel nome: se la forma è quella, forse è giusto chiamarlo bazooka comunque sia fatto.\\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # === I QUATTRO SIGNORI DELLE CARTE ====================================
    # ⚠️ il giapponese delle quattro e' IDENTICO parola per parola; a
    #    distinguerle e' l'inglese, che nomina lo spirito del seme. Il
    #    giapponese dice «gli spiriti del seme dell'oggetto», che vale per
    #    tutt'e quattro — e il seme il giocatore lo legge nel NOME della
    #    carta. Le quattro rese sono identiche, e `_coerenza` resta a zero.
    46547: "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",
    46615: "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",
    46683: "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",
    46751: "Una carta in cui è chiusa una magia particolare. Si attiva spendendo il 10% degli MP massimi. (1) Se sulla mappa ci sono cinque spiriti delle carte che non sono compagni, alza di un grado tutti gli spiriti del seme dell'oggetto e li mette in attacco; se però un altro spirito ha lo stesso seme e lo stesso grado, il grado torna com'era. Uno spirito che subisce danno passa in difesa. (2) Se sulla mappa gli spiriti che non sono compagni sono meno di cinque, ne evoca cinque di seme e grado a caso, in difesa, a un livello che dipende da Dispositivi magici e Memoria. Quando chi gioca lascia la mappa, gli spiriti che non sono compagni spariscono tutti.\\n#~Dizionario Fantastico di Irva~",

    46818: "Un corpo metallico misterioso che, dicono, è caduto dal cielo. È bello e raro, e i ricchi lo trattano come un metallo prezioso. Emette onde mentali debolissime, e da qui la leggenda che premendoselo sulla testa cambi il carattere. L'ho provato su un conoscente per passare il tempo, e purtroppo è servito soltanto a fargli riconoscere il carattere che aveva. Che a uno molto suggestionabile venga l'autoipnosi, però, non lo escludo.\\n#~Avanti! Squadra Esploratrice dell'Occulto~",

    # === I DUE ESTENSORI DI SOPRAVVIVENZA =================================
    # ⚠️ il giapponese di `:46950` comincia con （未実装）, «non implementato»:
    #    e' fermo a una versione vecchia. Il CODICE dice il contrario
    #    (`action.hsp:8782` mette CDATA_PREGNANCY_MALE_CHILD), e il codice
    #    vince. Il marcatore non si rende, e le due rese restano identiche
    #    come lo sono i due inglesi.
    46884: "Metà dell'età delle macchine... l'ambiente peggiorava, e a ogni generazione il corpo umano si faceva più fragile. Si arrivò sull'orlo dell'estinzione, ma la scampammo grazie a una tecnica che allargava la capacità di sopravvivere. Nanomacchine che registrano e riproducono i tratti utili a sopravvivere, organici o no, e li riscrivono assimilandoli nelle cellule dei figli: ecco che cosa sono gli estensori di sopravvivenza. Con funzioni ridotte, nanomacchine simili restano nelle cellule di quasi tutti i viventi di oggi. Ed è proprio questo che c'entra molto col fenomeno per cui i geni passano oltre la specie.\\n#~Dizionario Fantastico di Irva~",
    46950: "Metà dell'età delle macchine... l'ambiente peggiorava, e a ogni generazione il corpo umano si faceva più fragile. Si arrivò sull'orlo dell'estinzione, ma la scampammo grazie a una tecnica che allargava la capacità di sopravvivere. Nanomacchine che registrano e riproducono i tratti utili a sopravvivere, organici o no, e li riscrivono assimilandoli nelle cellule dei figli: ecco che cosa sono gli estensori di sopravvivenza. Con funzioni ridotte, nanomacchine simili restano nelle cellule di quasi tutti i viventi di oggi. Ed è proprio questo che c'entra molto col fenomeno per cui i geni passano oltre la specie.\\n#~Dizionario Fantastico di Irva~",
    46885: "\\\"Dicono che le cellule della vita primordiale non avessero né mitocondri né nanomacchine né conduttori magici. La vita si è evoluta prendendo dentro di sé le cose che le davano un vantaggio a livello di cellula\\\" \\n#~Parole di un Ricercatore di Zanan~",
    46886: "\\\"Fra le forme di vita meccaniche, molte sono nate da un essere umano proprio grazie a queste nanomacchine. Certo, alcune vengono da tecniche di tutt'altra linea... ma alla fine sono sopravvissuti solo i tipi che mangiano, dormono, sanno guarire e sanno riprodursi. Sarà quella che chiamano evoluzione convergente\\\" \\n#~Parole di <Gavela> l'ingegnere capo~",
    46951: "\\\"Ih ih ih... con questo arnese ho tirato fuori una bestia composita incrociando un mucchio di creature, e va bene, ma allevarla era una fatica impossibile: e allora niente, mi tocca tornare a sgobbare con la magia di sintesi!\\\" \\n#~Parole di un Mago Malvagio~",
    46952: "\\\"Ho sentito una tradizione che racconta di un bambino nato coi tratti di una bestia, che non riuscendo a tenere a freno la parte selvatica se ne andò lontano dagli uomini. Fra gli uomini-bestia di oggi ci sarà pure qualche stirpe che viene di lì\\\" \\n#~Parole di <Icolle> il biochimico~",

    # ⭐ l'inglese butta via «da sola non serve a niente», che e' la frase che
    #   dice che cosa fa questo oggetto.
    47016: "Una sostanza filamentosa che ospita una forza miracolosa. Da sola non serve a niente. Ma se esistesse un'arma capace di assorbirla, le gioverebbe per crescere.\\n#~La Storia delle Armi Raccontata da un Artigiano~",

    47083: "Un cristallo sottile a forma di anello. Attenzione: c'è gente senza scrupoli che vende rondelle da vite molto simili e del tutto inutili a prezzi da rapina, spacciandole per schermo contro le radiazioni e contro chi ti legge nel pensiero. È una vergogna, perché campa su chi soffre di allucinazioni e di manie: invece di dire che tanto ci guadagnano tutti e due, si pentano in fretta. ...L'anering, quello vero, l'Onda Sororale ce l'ha dentro davvero, e a spezzarlo ci si può fare il bagno: state tranquilli.\\n#~Il Testo Sacro dell'Onda Sororale~",

    # === I CALZINI, e i due che non li lavano =============================
    # ⚠️ `:47287` e `:47288`: l'inglese ha perso il `#` davanti alla fonte, e
    #    il cancello conta i `#` contro l'inglese. Si conserva com'e'.
    47286: "Un capo di vestiario che va a coppie. Non è pensato per essere usato come arma e non fa nemmeno da armatura, ma c'è chi colleziona perfino questo. Attenzione: i calzini di chi non ha l'abitudine di lavarsi i piedi puzzano parecchio. E comunque, a lavarli rovesciati viene via meglio l'unto della parte che stava a contatto col piede.\\n# ~Palmia: Collezione Autunno-Inverno~",
    47287: "\\\"Lavarmi i piedi? Ma neanche per sogno\\\"\\n~Parole del Capo dei Briganti~",
    47288: "\\\"Lavare i calzini? Ma neanche per sogno!!!!\\\"\\n~Parole di un Amante del Calzino Appena Sfilato~",
}
