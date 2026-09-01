# -*- coding: utf-8 -*-
"""Le rese del lotto 051 — LE PERGAMENE E GLI ATTI, il CORPO, prima parte.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 051 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa051.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Previsione di `applica`: **+56** per 50 rese — il moltiplicatore c'e', e
sono quattro firme che coprono sei righe in piu':

    :45132 -> anche :45203        la nota della nave, かなり弱い
    :45345 -> anche :45416        la nota della nave, 弱い
    :51360 -> anche :51431, :51502, :51573   la nota del mezzo di terra
    :58396 -> anche :58458        il certificato fiscale, 12 milioni e 1,2

⚠️ Forma, da `_forma.py 051`: **37** righe su 50 hanno lo spazio prima del `\\n`
e 13 no; **26** code portano lo spazio dopo il `#` e 24 no.
"""

IT = {
    # =====================================================================
    # I MEZZI DI MARE, e la NOTA che l'inglese appiattisce
    #   Le sei note dell'indice 1 sono la stessa frase, tranne UNA parola:
    #   il grado di debolezza contro i temporali. Vedi `testa051.py`.
    # =====================================================================

    45060: "Un atto che dà la proprietà di una zattera. È enorme, ma galleggia solo per la spinta del legname, quindi carica poco. Una vela ce l'ha, tanto per dire, ma senza remare di buona lena andare contro le onde è dura.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # とてつもなく弱い — il gradino più basso della scala.
    45061: "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È debolissima contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    45131: "Un atto che dà la proprietà di un peschereccio. Ha le reti da pesca, e i pesci si prendono tutti in un colpo. Ma meglio stare attenti... davanti a un mostro che affonda una barca con un buffetto, la preda sei tu.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # かなり弱い — e questa resa copre ANCHE :45203, la nave pirata.
    45132: "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È parecchio debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    45202: "Un atto che dà la proprietà di una nave pirata. Ha un cannone d'altri tempi e può bombardare. La bandiera nera issata bene in alto è piena di romanticismo. Il problema, semmai, è che i mercantili che incontri scappano a gambe levate.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    45273: "Un atto che dà la proprietà di una nave da crociera. Le installazioni sono comodissime, ma il personale che ti serve non è compreso.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # 結構弱い — il gradino di mezzo.
    45274: "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È abbastanza debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    45344: "Un atto che dà la proprietà di una nave da guerra. È un reperto antico rimesso in sesto, e come venisse usata non è tanto chiaro. Ha una corazza e un armamento discreti e non resta indietro nemmeno davanti ai mostri di mare, ma contro le tempeste non ce la fa.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # 弱い, senza avverbio — il gradino più alto, e questa resa copre ANCHE
    # :45416, il sottomarino.
    45345: "Tingendo l'atto si sceglie la vernice. Letto in una città sul mare, chiama la nave. Attenzione: le tasse si calcolano sulla nave più cara che hai usato nel periodo. È debole contro i temporali e i venti d'etere, ma se affonda, con l'assicurazione pagata il diritto non si perde.\\n#~Note al Manuale di Viaggio~",

    45415: "Un atto che dà la proprietà di un sottomarino. Non lo chiamano l'arma furtiva definitiva per niente: né le altre navi né i mostri riescono a scovarlo. Ha i siluri, ma a lanciarli si scopre proprio quel che teneva nascosto, cioè di esserci e dove.\\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # =====================================================================
    # I MEZZI DI TERRA
    # =====================================================================

    # ⚠️ ちょっとした金持ち程度では維持費を工面できない e' «uno appena
    #    benestante non riesce a mantenerla». L'inglese scrive «even the
    #    richest person cannot afford», che e' il contrario del ceto.
    51359: "Un atto che dà la proprietà di una corazzata terrestre. Pare l'abbiano dissotterrata dalle rovine dell'età delle macchine e che un rigattiere l'abbia rimessa a posto per conto suo. Un ammasso di romanticismo, che uno appena benestante non riesce a mantenere. Le prestazioni dei tempi d'oro non le ha più, ma corazzata resta: un mostro di passaggio lo spazza via col primo colpo. Porta carichi molto pesanti, e anche caricata troppo non rallenta facilmente. Ha pure l'aria condizionata, quindi nel deserto si sta comodi. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ⚠️⚠️ Questa resa copre QUATTRO righe: :51360, :51431, :51502, :51573 —
    #    corazzata, locomotiva, autocarro e carrozza hanno la stessa nota.
    51360: "Tingendo l'atto si sceglie la vernice. Col tasto s si fa suonare il clacson, ma non serve a niente. Se ti torna voglia di viaggiare a piedi, rileggi lo stesso tipo di atto. Attenzione: le tasse si calcolano sul mezzo più caro che hai usato nel periodo. \\n#~Note al Manuale di Viaggio~",

    51361: "\\\"Proprio questo dovevano tirare fuori, fra tutte le cose. ...Vabbè, di questi tempi non sarà un problema.\\\" \\n# ~Parole di un Esperto che ha Visto la Scena~",

    51430: "Un atto che dà la proprietà di una locomotiva che va a magia. Stende da sé rotaie magiche, quindi anche sulle nevi il viaggio non ne risente. Traina carichi piuttosto pesanti e, se sono troppo pesanti, non rallenta facilmente. Ha però un punto debole: se il forno magico non è acceso, la corsa ne soffre, e bisogna continuare a metterci MP, sia pure pochi. Regolare la potenza e farne la manutenzione è una noia, tanto che perfino a Eulderna è merce rara. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # ⚠️ ベルム家 e' «casa Bellum» (`chat.hsp`), non «Belm».
    51432: "\\\"Io sono un genio! Se il mio motore magico non lo apprezza nessuno è per un complotto di casa Bellum!\\\" \\n# ~Parole di un Sedicente Genio degli Arnesi Magici~",

    # ⓘ Il giapponese ripete qui la frase della vernice; l'inglese la butta.
    51501: "Un atto che dà la proprietà di un autocarro. È fatto per correre abbastanza anche sulle strade brutte, ma su una strada tenuta bene va più forte. Tingendo l'atto si sceglie la vernice. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    51572: "Un atto che dà la proprietà di una carrozza grande. Cavalli addestrati apposta compresi. Il viaggio andrà meglio che a piedi. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    # =====================================================================
    # GLI ATTI DEGLI IMMOBILI
    # =====================================================================

    44031: "Un atto che dà il diritto di aprire un accampamento. Che cosa ci si tenga dentro e che cosa ci si faccia è lasciato a chi lo possiede. \\n# ~Immobiliare Derphy: Catalogo~",

    55211: "Serve per spostare una tua proprietà che non sia la casa. Bisogna registrarla prima, leggendo l'atto dentro quella proprietà, e poi te la spostano a poco prezzo lasciando fuori e dentro come stanno. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    70197: "L'atto di un grande allevamento abbandonato. Un tempo era un allevamento di mostri in grande stile, oggi è poco più che spazzatura. \\n# ~Immobiliare Derphy: Immobili Dismessi~",

    71028: "L'atto che serve come pratica per traslocare. Costa caro, ma con il servizio compreso: se è una casa te la spostano com'è, dentro e fuori, foss'anche una caverna. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    83411: "Un atto che dà il diritto di creare un sotterraneo in quel luogo. Pare lo comprino gli avventurieri diventati dipendenti dai sotterranei. \\n# ~Immobiliare Derphy: Catalogo~",

    92654: "Un atto che dà il diritto di creare un allevamento. Lo slogan scritto in grande su quest'atto dice: la tua nuova storia comincia qui. \\n# ~Immobiliare Derphy: Catalogo~",

    94670: "Un atto che dà il diritto di costruire un magazzino. Quando le mani cominciano a essere piene, conviene prenderne uno in affitto. E non dimenticare il canone mensile. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    94739: "Un atto che dà il diritto di fare un campo. Non sarebbe male dimenticare qui l'avventura e prendersi un po' di riposo. \\n# ~Immobiliare Derphy: Catalogo~",

    95990: "Un atto che dà il diritto di aprire un negozio. Si racconta di un avventuriero che, presosi troppo dalla foga, finì per vendere anche il proprio equipaggiamento e restò lì a fare il bottegaio. \\n# ~Immobiliare Derphy: Catalogo~",

    # ⚠️⚠️ L'INGLESE È ROTTO: scrive «A deed gives the right to create a shop»
    #    su un atto che il giapponese dice 博物館, il MUSEO — e' la riga del
    #    negozio (`:95990`) ricopiata. La seconda meta' dell'inglese parla
    #    infatti di collezionisti.
    96060: "Un atto che dà il diritto di costruire un museo. Lo stipendio che passa lo Stato è una miseria, ma mostrare al pubblico la collezione che ti sei fatto da solo è la gioia più grande per chi colleziona. \\n# ~Immobiliare Derphy: Catalogo~",

    96782: "Un atto che dà il diritto di ricevere quel che c'è nella borsa dei ricordi. Leggendolo, la consegna definitiva del ricordo viene accettata. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ⚠️ 1200万納税書 e 120万納税書 hanno la STESSA prosa: una firma, due
    #    righe (:58396 e :58458), una resa.
    58396: "Fatto per alleggerire la fatica di emettere e sbrigare la fattura ogni mese. Pagando tutto in anticipo, finché quella somma non finisce le fatture ordinarie non arrivano. Su quelle già arrivate non ha effetto. \\n# ~Come Andare d'Accordo con le Tasse~",

    # ⓘ すくつ e' il refuso voluto di 巣窟, e nel progetto quel luogo e' «il
    #    Vuoto» — lo dice il rapporto di identificazione di questa stessa
    #    licenza. L'inglese scrive «the sanctuary», che e' un terzo nome.
    81399: "Una licenza che permette di esplorare il Vuoto. Si dice che là dentro dormano tesori a non finire e cadaveri a migliaia. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # LE PERGAMENE
    # =====================================================================

    44300: "Una pergamena che racchiude la magia di raccogliere monete d'oro. Da dove vengano quelle monete è meglio non pensarci troppo.\\n#~Compendio Completo degli Oggetti Magici~",

    44371: "Una pergamena che tira gli ostili intorno a sé. Serve a stanare i nemici che scappano e si nascondono, e a farli fuori. Attenzione a non usarla nel momento sbagliato: ritrovarsi circondati è pericoloso.\\n#~Compendio Completo degli Oggetti Magici~",

    52517: "Una pergamena che, ai tempi della civiltà magica, una strega lasciò per crescere i suoi giovani discepoli. Ci sono scritte, in modo chiarissimo, le conoscenze magiche che si era guadagnata in una vita intera. Le notizie sono divise in parti che si leggono facilmente, e il congegno è questo: se ne leggi una, nella pergamena dopo ne esce un'altra. \\n#~Compendio Completo degli Oggetti Magici~",

    52519: "\\\"Qualunque potere, secondo come lo si usa, rende le persone felici o infelici... ti prego, non dimenticarlo.\\\" \\n#~Parole di una Strega Scritte in un Angolo~",

    # ⚠️ Qui «equipaggiamento» l'impaginatore lo **spezzava** (misurato da
    #    `_107-descrizioni-item --peggiori`, non dedotto): sciolta in «arma o
    #    armatura», che e' la coppia che usa gia' il rapporto di questa stessa
    #    pergamena. A `:95990` la stessa parola non si spezza — conta dove
    #    cade il taglio, non la lunghezza (113a).
    81740: "Una pergamena preziosa, che permette di ribattezzare un'arma o un'armatura. Si usa nelle occasioni più diverse: quando si ha voglia di cambiare aria, o quando è l'arma stessa a chiederti di cambiarle nome. \\n#~Compendio Completo degli Oggetti Magici~",

    # ⚠️ 死神 e' «la Morte» nel dizionario (`item_func.hsp`: «stringe un patto
    #    con la Morte»), femminile e con la maiuscola.
    83626: "Una pergamena preziosa che, stringendo un patto con la Morte, di suo capricciosa, annulla una volta sola una ferita mortale. Ma attenzione: la Morte è lunatica. Guardarsi bene dal guastarle l'umore...\\n#~Compendio Completo degli Oggetti Magici~",

    88346: "Una pergamena che chiama un portale verso l'esterno. Se la si usa per sbaglio, rileggendola si annulla. Ovviamente se ne consumano due, ma pazienza: consideralo il prezzo della lezione. \\n#~Compendio Completo degli Oggetti Magici~",

    88741: "Una pergamena preziosa che alleggerisce un oggetto fra quelli che porti. C'è chi sostiene che se ne vedano così poche perché questa pergamena vola per aria come un uccello migratore. \\n#~Compendio Completo degli Oggetti Magici~",

    89490: "Una mappa con su il luogo di un tesoro nascosto, sepolto da qualche parte nel mondo. Le notizie sono a pezzi e tirarlo fuori è difficilissimo, ma quando in qualche modo trovi il posto provi una commozione che somiglia alla soddisfazione. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",

    89884: "Una carta diabolica che a scadenza fissa chiede soldi. Bruciarla o farla sparire non serve: quelli tornano un mese dopo, e con i compari... \\n#~Compendio Completo degli Oggetti Magici~",

    94246: "Una pergamena che fa cadere sui compagni intorno una pioggia che cura. Si racconta ancora oggi che tanto tempo fa una dea guaritrice, tutta vergognosa, l'abbia donata a dei contadini stremati dalla siccità. \\n#~Compendio Completo degli Oggetti Magici~",

    96497: "Una pergamena capace di soffiare di nuovo il potere magico dentro un oggetto che l'ha perso. È difficilissima da maneggiare: se non si riesce a leggerla per bene, per l'oggetto è la fine. \\n#~Compendio Completo degli Oggetti Magici~",

    99025: "Una pergamena da cui arriva, non si sa da dove, un compagno che dà una mano. A guardare bene, in un angolo della pergamena ci sarebbe scritto in piccolo: costi a parte. O almeno così si dice. \\n#~Compendio Completo degli Oggetti Magici~",

    # =====================================================================
    # LE QUATTRO COPPIE DEL POTENZIAMENTO E DEL MATERIALE
    #   Normale contro superiore: il giapponese oppone 一段階強くなる
    #   («sale di un gradino») a 性能の限界を超えて («oltre il limite»).
    # =====================================================================

    96915: "Una pergamena che, letta, veste l'armatura di un abito d'oro. È più forte di quelle normali, e si dice che porti la forza oltre il limite di ciò che l'armatura può dare. \\n#~Compendio Completo degli Oggetti Magici~",

    96986: "Una pergamena che, letta, veste l'armatura di un abito d'oro. Così l'armatura diventa più robusta, e si dice che salga di un gradino. \\n#~Compendio Completo degli Oggetti Magici~",

    97057: "Una pergamena che, letta, avvolge l'arma in un abito d'oro. È più forte di quelle normali, e si dice che porti la forza oltre il limite di ciò che l'arma può dare. \\n#~Compendio Completo degli Oggetti Magici~",

    # ⚠️⚠️ L'INGLESE È ROTTO: «increases the strength of the armour» sulla
    #    pergamena dell'ARMA — e' la riga dell'armatura (`:96986`) ricopiata.
    #    Il giapponese dice 武器の強度.
    97128: "Una pergamena che, letta, avvolge l'arma in un abito d'oro. Così l'arma diventa più robusta, e si dice che salga di un gradino. \\n#~Compendio Completo degli Oggetti Magici~",

    97396: "Una pergamena che cambia il materiale. Tende a cambiarlo in uno più forte e più prezioso, ma come la pergamena agisca sul materiale non bisogna chiederlo: sono tutte cose che fa la magia. \\n#~Compendio Completo degli Oggetti Magici~",

    97467: "Una pergamena che cambia il materiale. Va da sé che quasi tutti gli alchimisti si servano di questa pergamena come trampolino per le proprie ricerche. \\n#~Compendio Completo degli Oggetti Magici~",

    97538: "Una pergamena che cambia il materiale. Di solito lo cambia in uno scadente, ma pare che certi avventurieri sappiano rigirare la cosa a proprio vantaggio. \\n#~Compendio Completo degli Oggetti Magici~",
}
