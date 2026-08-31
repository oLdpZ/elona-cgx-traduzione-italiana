# -*- coding: utf-8 -*-
"""Le rese del lotto 039 — gli SCARTI, seconda parte: gli OGGETTI DEGLI DEI.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 039 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa039.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ I nomi degli dei si copiano dal dizionario, non si traslitterano: si cercano
con `scratchpad/lotti-111/_cerca.py`. ネヘルタード e' `<Amurdad>`, non
«Nehertard».
"""

IT = {
    # === LA BACCHETTA DEL DIRETTORE =======================================
    62732: "La cosiddetta bacchetta del direttore. Ingrandendo il movimento della mano, rende facile dare indicazioni a gesti. In origine serve a dirigere la musica, ma indicare ai compagni chi attaccare sarà una sciocchezza. \\n# ~Le Melodie della Limpida Irva~",

    # === GLI OTTO OGGETTI DEGLI DEI =======================================
    # ⚠️ ognuno ha l'indice 0 dall'enciclopedia e DUE battute, una per dio.
    #    I nomi vengono dal dizionario; gli epiteti in prosa dalle righe di
    #    livello 150, dove ci sono. Vedi testa039.py.
    # --- il manubrio di Opatos
    # ⚠️ l'inglese salta la frase che dice a che serve (l'effetto in
    #    allenamento). Si segue il giapponese.
    62865: "Il manubrio che la dea della gemma tenace si è fatta prestare a forza dal fratello minore, il dio della terra. Usandolo mentre ti alleni l'effetto sale di parecchio. Da sempre le pesa cercare la propria roba e si porta via quella del fratello che le capita sott'occhio, così il dio della terra è in imbarazzo. Ma alla sorella maggiore non si può dire di no.\\n# ~Dizionario Fantastico di Irva~",
    62866: "\\\"Muahaha! Questo manubrio me lo prendo un attimo in prestito!\\\" \\n# ~Parole di <Urcaguary>~",
    62867: "\\\"Muahahahaha ridammelo.\\\" \\n# ~Parole di <Opatos>~",
    # --- l'amuleto di Jure
    62929: "L'amuleto distribuito al dio della protezione e ai difensori con la scusa che se si ammalano e stanno a letto è un disturbo. Non ha il potere di prevenire le malattie, ma se la malattia non è complicata la cura in un lampo, appena viene, e la guarisce del tutto. \\n# ~Dizionario Fantastico di Irva~",
    62930: "\\\"Ecco, guardate quest'amuleto. In mezzo ha scritto Salute a lettere così grandi che poi non ci stavano più, e da lì in avanti, per farle entrare nello spazio, si fanno di colpo minute... Si immagina benissimo la fretta di Jure mentre lo scriveva. Ah, che pace, vero?\\\" \\n# ~Parole di <Rovid>~",
    62931: "\\\"E-ehi, scemo! Che vergogna, smettila!\\\" \\n# ~Parole di <Jure>~",
    # --- la candela di Lulwy
    62993: "Una candela rossa inquietante, con dentro una medicina sospetta. Bruciando, le sostanze evaporano e si spargono, e a chi le respira monta l'eccitazione. La dea del vento ne aveva preparate in quantità per un supplizio di candele senza fine, ma la dea della tempesta di sabbia è andata giù con una sola. Alla dea del vento è passata la voglia e dopo, si dice, le buttò tutte nel deserto... \\n# ~Dizionario Fantastico di Irva~",
    62994: "\\\"Ahah! Lo schiavo sta godendo con gli occhi all'insù! Questa candela è incredibile, sorellona!\\\" \\n# ~Parole di <Arasiel>~",
    62995: "\\\"Arasiel, la prossima sei tu.\\\" \\n# ~Parole di <Lulwy>~",
    # --- la pistola lanciarazzi di Mani
    63057: "Viene insieme ai suoi razzi di segnale. Sa cambiare facilmente colore e disegno del colpo. Il dio delle macchine l'ha data al dio dei cavalieri di ferro, che penava a condurre le operazioni dove le onde arrivano male. Manda una luce che si riconosce anche di giorno e brilla perfino dentro la tempesta, così l'ordine arriva in fretta anche a chi sta dove la voce non giunge. E non consuma il turno. \\n# ~Dizionario Fantastico di Irva~",
    63058: "\\\"Anche se le onde sono disturbate, da vicino con questa gli ordini si danno. È un mezzo primitivo, però.\\\" \\n# ~Parole di <Mani>~",
    63059: "\\\"Il signor Mani non delude mai!\\\" \\n# ~Parole di <Garziem>~",
    # --- gli occhiali di Yacatect
    63121: "Gli occhiali che la dea della ricchezza si mette quando vuole giudicare bene quanto vale chi ha davanti. Pare li portasse anche quando scoprì il talento della dea del canto e della danza. Di solito li tiene via perché le stancano gli occhi, e ogni tanto li dimentica in giro. \\n# ~Dizionario Fantastico di Irva~",
    63122: "\\\"Sono occhiali che ai miei occhi vanno proprio bene!\\\" \\n# ~Parole di <Yacatect>~",
    63123: "\\\"Sorella Yaca, ha di nuovo lasciato gli occhiali in camerino...\\\" \\n# ~Parole di <Karavika>~",
    # --- il segnalibro di Itzpalt
    63185: "Il segnalibro che, dicono, il dio degli elementi mandò alla dea della sapienza. Si era messo d'impegno e ne aveva fatti per qualche migliaio; tornato in sé non sapeva più che farne, ma la dea della sapienza li accettò tutti volentieri e li usa tutti, normalmente. Dicono che, a infilarlo, venga una voglia matta di sapere come va avanti il libro. \\n# ~Dizionario Fantastico di Irva~",
    63186: "\\\"Leggere fa bene. Non è solo prendere sapere: si legge e si pensa. Lì c'è un tempo pieno.\\\" \\n# ~Parole di <Sophia>~",
    63187: "\\\"Capisco, ami i libri. Allora il dono che ti concedo è questo.\\\" \\n# ~Parole di <Itzpalt>~",
    # --- la tazza di Ehekatl
    # ⚠️ l'inglese salta la frase centrale (che la dea della sventura ha
    #    continuato ad assalirla e ne ha in quantità). Si segue il giapponese.
    63249: "Era la tazza della dea della fortuna, ma un giorno la dea della sventura, che passava di lì a spasso, ci mise gli occhi e se la portò via senza lasciarle il tempo di opporsi. Alla dea della sventura dev'essere piaciuta parecchio, perché ha continuato ad assalirla e a derubarla, e il sospetto che oggi ne abbia in quantità tutte uguali è forte assai. Stando alle indagini, questa tazza ha la virtù di rendere bevibile senza rischio perfino l'acqua cattiva di un pozzo. \\n# ~Dizionario Fantastico di Irva~",
    63250: "\\\"Ehekatl! Questa è carina, me la prendo io, miao! Dammela buona buona, miao!\\\" \\n# ~Parole di <Sinaha>~",
    63251: "\\\"Uau! Ti piace la tazza col gattino? Ti piace? Te la regalo!\\\" \\n# ~Parole di <Ehekatl>~",
    # --- le cesoie di Kumiromi
    63313: "Le cesoie che, dicono, il dio del raccolto ricavò da una propria piuma e consegnò al dio dell'eternità. Servono a staccare del tutto dal corpo l'anima che ha avuto la morte che le spettava, e a rimetterla nel flusso delle rinascite. Anche senza la forza divina che ci vorrebbe se ne può tirare fuori una parte, e usandole per raccogliere i frutti i germogli nuovi vengono più facili. \\n# ~Dizionario Fantastico di Irva~",
    63314: "\\\"Queste... puoi... usarle...\\\" \\n# ~Parole di <Kumiromi>~",
    63315: "\\\"L'anima si stacca dal corpo... e torna dentro la luce...\\\" \\n# ~Parole di <Amurdad>~",

    # === LE DUE SPADE DEL TESCHIO =========================================
    # ⚠️ l'inglese di :63583 inventa due volte: dice che la spada e' stata
    #    potenziata «with the power of nether and magic» (il giapponese dice
    #    che TAGLIA meglio e che l'impugnatura succhia la vita) e attribuisce
    #    la potenza a Lancio e Dispositivi magici (il giapponese dice
    #    l'Alchimia di quando e' stata fatta). Si segue il giapponese.
    63583: "Fusa di nuovo dall'alchimia, è rinata come una bella spada magica. Taglia meglio, ma a tenerla in mano a lungo l'impugnatura ti succhia la vita: meglio scagliarla contro il nemico. La potenza dell'urto dipende dalla tecnica di Alchimia di quando è stata fatta.\\n# ~Compendio Completo degli Oggetti Magici~",
    64993: "Una spada che una volta si era spezzata e che l'alchimia ha fatto rinascere. Ha paura di rompersi di nuovo, e appena la impugni si dimena. Non è fatta per essere brandita: lanciala senza darle il tempo di agitarsi. Non avere pietà. La potenza dell'urto dipende dalla tecnica di Alchimia di quando è stata fatta. \\n# ~Compendio Completo degli Oggetti Magici~",

    # === IL CESTO VUOTO ===================================================
    64615: "Un cesto grande senza niente dentro. Si usa soprattutto da contenitore quando si mangia all'aperto. È intrecciato con cura e molto robusto. \\n# ~I Comprimari della Cucina~",

    # === LE DUE BOMBE MAGICHE =============================================
    64869: "Una potente bomba magica fatta con l'alchimia. Pare l'abbia messa a punto per difendersi un alchimista di un tempo. La sua particolarità è che la forza magica liberata esplode a più riprese. La potenza dipende dalle tecniche di Controllo magia e di Dispositivi magici. \\n# ~Compendio Completo degli Oggetti Magici~",
    64931: "Un cristallo di forza magica a cui l'alchimia ha rimescolato la composizione. La magia chiusa dentro è instabile, e togliendo la spina e dandogli un colpo scoppia in un'esplosione magica. La potenza dipende dalle tecniche di Controllo magia e di Dispositivi magici. È famoso come materiale pericoloso facile da fare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # === LE TRE PERLE RICURVE =============================================
    # ⚠️ famiglia con :52579 (lotto 038): stessa forma, cambia l'elemento.
    #    L'inglese di :68045 e :52579 e' la stessa copia sbagliata, che dice
    #    «hot air» e poi «cold air» dentro la stessa riga.
    66009: "Una pietra ricurva che ha forza magica. Ha la proprietà di rispondere alla mana e di raccogliere l'umidità dell'aria: appena te la metti in tasca, è sicuro che ti bagni tutto. Per come funziona, nelle terre secche come il deserto non rende bene. \\n#~Misteriosi Ornamenti Antichi~",
    68045: "Una pietra ricurva con la forza magica di assorbire il fuoco. Quando si manda fuoco, facendoci passare la magia come attraverso una lente, si trattiene la combustione. Ma il raggio in cui agisce è strettissimo, e per ripararsi dal fuoco che si allarga non serve. \\n#~Misteriosi Ornamenti Antichi~",

    # === IL DISCO MENTALE E L'E.G.G =======================================
    66261: "Un disco su cui hanno copiato e inciso ogni informazione di una persona, ricordi e pensieri compresi. È una tecnica perduta di cui resta solo il modo di fabbricarlo; come si legga e a che serva non si sa. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",
    66323: "La capsula organica a forma di uovo che la cicogna porta agli sposi. Gira anche la voce che si raccolga in certi campi, ma chi si è avvicinato alla verità è sparito, senza eccezioni. \\n# ~Dizionario Fantastico di Irva~",

    # === LA PIETRA E IL LEGNAME ===========================================
    66765: "Un blocco di pietra tagliato dalla cava. Serve soprattutto a fare sculture e muri. \\n# ~Catalogo d'Arte di Lumiest~",
    68388: "Alberi abbattuti e lavorati per farne materiale da costruzione e arnesi. Il legno non seccato abbastanza è pesante, marcisce facilmente, si ritira e si deforma, e come resistenza è peggio di quello secco. \\n# ~Foreste ed Economia: la Segheria~",

    # === LA SPAZZOLA E LA SUPER ESCA ======================================
    69388: "Una spazzola grande da allevamento. Spazzolare spesso migliora la circolazione e il pelo, e togliendo sporco e insetti fa anche bene alla salute. \\n# ~Vivere Insieme al Bestiame~",
    71643: "Usa come fonte d'energia la normale esca montata insieme, e in un attimo cerca da sé la preda e la cattura. Anche dopo torna su da solo, così all'uomo non resta quasi niente da fare e nella pesca non si migliora quasi per niente. \\n# ~Casalinghi che Danno Colore alla Casa~",
    71645: "\\\"Comodo lo è di sicuro, ma si muove che è una furia e a chi tiene la canna consuma un mucchio di resistenza. Io preferisco pescare con calma, alla maniera normale.\\\" \\n# ~Parole di un Pescatore Fiero della Sua Preda~",

    # === I DODICI MATERIALI DA SINTESI ====================================
    # ⓘ hanno tutti lo stesso indice 3 («un oggetto per la sintesi») e un
    #    indice 0 breve, ognuno da un libro diverso.
    74693: "Acqua con dentro forza magica, congelata. Fa bene ai dolori dei nervi.\\n# ~Il Primo Soccorso che Salva la Vita~",
    74755: "Una goccia nera. Sembra faccia male, e invece è il contrario: toglie il veleno.\\n# ~Dizionario dei Veleni e dei Farmaci~",
    74817: "Una lampada fatta con erba che brilla. Quella luce appena accennata è elegante.\\n# ~Interior Paradise: Numero Straordinario~",
    74879: "Un minerale con dentro mescolate sostanze di ogni sorta, poi lavorato. \\n#~Atlante dei Minerali di Vernis~",
    74941: "Uno specchio fatto d'etere. Manda un bagliore misterioso.\\n# ~Grande Speciale sugli Oggetti alla Moda~",
    75003: "Ali fatte cucendo insieme penne d'uccello. Non sono tenute insieme dalla cera, quindi a scaldarle non si sfasciano. \\n# ~Grande Enciclopedia del Cucito~",
    75065: "Cellule di troll coltivate. Le avevano messe a punto per curare, ma siccome divorano le altre cellule non si sono rivelate pratiche. \\n# ~Rapporto Misterioso~",
    75127: "A farlo suonare esce una musica che ti fa girare la testa. Più uno è sano di mente, più il danno è grosso. \\n# ~Le Melodie della Limpida Irva~",
    75189: "Un apparecchio da riscaldamento di una volta. Siccome fa molto gas nocivo, ossido di carbonio compreso, arieggia spesso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    75251: "Una batteria. Ricaricandola si usa più volte. \\n# ~Speciale: l'Eredità della Civiltà Meccanica~",
    75313: "Le sostanze contenute in tracce dentro i sassi, raccolte e ricomposte con l'alchimia. Non si lavora se non a un calore parecchio alto. \\n# ~Atlante dei Minerali di Zaile~",
    75375: "Una statua di drago fatta di scarti. A furia di granelli si fa una montagna: anche gli scarti, lavorati, diventano arte. \\n# ~Catalogo d'Arte di Lumiest~",
}
