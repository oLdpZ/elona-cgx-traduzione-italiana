# -*- coding: utf-8 -*-
"""Le rese del lotto 050 — LE POZIONI, il CORPO, seconda meta': la categoria CHIUDE.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 050 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa050.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 050`: **9** righe su 41 hanno lo spazio prima del `\\n` e
32 no; **32** code portano lo spazio dopo il `#` e 9 no. E **cinque** righe
chiudono con un `\\n` DOPO la coda: `:92522`, `:93554`, `:114277`, `:117531`,
`:129085`.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese, nessuna gemella.
`_gia-reso.py 050` dice 0 su 41.
"""

IT = {
    # =====================================================================
    # I CONTENITORI E I LIQUIDI DI CASA
    # =====================================================================

    90769: "Una bottiglia vuota, che ha contenuto qualcosa o che aspetta con impazienza di contenerlo. Così com'è non serve a niente, ma ci si può prendere l'acqua da un pozzo, come scorta per le emergenze. \\n#~Casalinghi che Danno Colore alla Casa~",

    91656: "Granelli bianchi che scendono dal cielo, raccolti e stretti in un pugno. È una materia freddissima: tirata, diventa acqua all'istante, ma finché la si tiene addosso non cambia mai, ed è una proprietà rara come poche. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    92323: "Una pozione pericolosa, fatta senza nascondere l'intenzione di dare fuoco al bersaglio. Tirandola si alza una colonna di fiamme nel punto scelto; ma con il fuoco non si scherza: meglio farlo accompagnati da un adulto e con l'acqua a portata di mano. \\n#~Bevande da Bere e Bevande da Non Bere~",

    92522: "Un liquido bianco latteo, che si ricava mungendo gli animali. È molto nutriente e si ritiene conti molto per la crescita. È la materia prima dei latticini, ma non sono pochi quelli che se lo bevono così com'è.\\n#~Il Cibo Mutevole di Tyris~\\n",

    # ⚠️⚠️ L'INGLESE È ROTTO: ricopia la chiusa del liquido IGNIFUGO
    #    (`:81811`, lotto 049) — «the burns that occur when you eat something
    #    hot» — su una riga che parla di ACIDO. Il giapponese dice
    #    飲みすぎた日の強烈な胃酸, i succhi gastrici del giorno dopo una bevuta.
    93069: "Una pozione che stende una pellicola resistente agli acidi su ciò che vi si immerge. Funziona solo sugli oggetti: a berla, le tue viscere non acquisteranno nessuna resistenza contro i succhi gastrici feroci del giorno dopo una bevuta. \\n#~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ La chiusa: il giapponese dice «e' roba preziosa, quindi almeno
    #    identificarla conviene sempre» — un consiglio di gioco. L'inglese
    #    scrive «keep in mind what a price such an item could fetch», cioe'
    #    il prezzo. Arbitra il giapponese, com'e' regola dalla 26a.
    93554: "L'unica pozione miracolosa che guarisce la malattia dell'etere, che a vivere si prende per forza. Che ti siano spuntati occhi in più o che dalle mani ti coli veleno, cura tutto sul momento; ma è roba preziosa, quindi almeno identificarla conviene sempre.\\n# ~Dizionario Fantastico di Irva~\\n",

    96195: "Un liquido che esiste in molti colori e che, immergendovi un oggetto, glielo tinge del proprio. Non è una bevanda, ovviamente, quindi meglio non berlo; ma se vuoi conoscere una versione più sgargiante di te, nessuno ti ferma.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    96426: "In Tyris l'acqua pura è una cosa preziosa. La tecnica della distillazione c'è, eppure l'acqua non si riesce a produrla, e la ragione è l'etere che si mescola di nascosto ai liquidi. Toglierlo dall'aria, dove ogni giorno abbonda, costa una fatica enorme.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ スライム e' «la melma» nel dizionario, non «slime»: il nome della
    #    creatura decide, e la frase lo nomina due volte.
    104862: "Una pozione con le stesse proprietà degli umori della melma. Come la melma scioglie qualunque cosa, questa corrode il materiale che tocca. Fa male anche al corpo umano, naturalmente: per quanta sete si abbia, non la si beva mai.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    113676: "Il veleno estratto dalla coda dello scorpione re, che si dice viva nelle piramidi, allungato con acqua sporca. A berlo ci si avvelena, com'è ovvio; ma con questa puzza di pesce marcio nessuno lo beve per suo piacere. \\n#~Bevande da Bere e Bevande da Non Bere~",

    129439: "L'acqua che in Tyris del Nord i cittadini usano tutti i giorni, messa in una bottiglia vuota. Sarà pure acqua per uso domestico, ma oggi in Tyris del Nord l'inquinamento è alto, e berla alla leggera non conviene.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # LE POZIONI DELL'ETERE E DELLE MUTAZIONI
    # =====================================================================

    102108: "Una pozione rara come poche, che permette di rimettere gli occhi su ciò che si è diventati. La malattia dell'etere, purtroppo, non la guarisce, ma i sintomi che ti sono piombati addosso li cura tutti. Sì: anche le mutazioni buone.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    102179: "Una pozione che, a berla, fa crescere di colpo qualcosa che umano non è. Berla per curiosità è meglio di no. Consigliata solo a te che vuoi smettere di essere umano.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ 悪夢 e 元素の傷 sono due incantesimi gia' resi: «Incubo» e «Cicatrice
    #    elementale» (lotto 048, dai grimori). Qui li nomina la prosa, e i
    #    nomi sono quelli — e' la stessa famiglia che nessuna rete vede.
    102392: "Una pozione molto pericolosa, che fa assaggiare Incubo e Cicatrice elementale nello stesso momento. Non tirarla mai addosso a un amico per curiosità.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # LE POZIONI CHE ALZANO E ABBASSANO
    # =====================================================================

    105596: "Una pozione pericolosa: a berla ti tornano in mente di colpo gli errori del passato e la guardia si abbassa. Come la si ricavi non si sa, ma di sicuro nella bottiglia ci sono stipati fino all'orlo gli insulti di una mietitrice dagli occhi d'argento.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    105813: "Una pozione che dà l'illusione che ti sia sceso addosso di colpo il dio della guerra. Dura poco, certo, ma l'effetto è reale, tanto che pare le guardie alle prime armi se la portino dietro giorno e notte per non farsi prendere dalla tensione sul lavoro. O almeno così si dice.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    106037: "Una pozione pericolosa: a berla il corpo si fa pesante come se avessi ingoiato del piombo e, di contro, sembra che il mondo intorno si sia messo a correre. Negli ultimi anni fa problema chi, preso da quel mondo fuori dall'ordinario, se la beve quasi per vizio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⓘ Niente lineetta lunga: CP932 non ce l'ha, e il preflight la ferma.
    106108: "Una pozione che dà l'illusione di sentire sulla pelle lo scorrere del tempo. È preziosissima, perché basta pensare un gesto e il gesto viene da sé, ma attenzione a non abusarne fino a diventare così pigri da dimenticarsi di respirare.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ ハウンド e' «segugio» (glossario), e la frase lo dice due volte.
    106325: "Dice di rendere forti contro gli elementi dei segugi, perché mette insieme il decotto delle zanne di ogni razza di segugio. L'effetto dura pochissimo: probabilmente è parecchio allungata.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    106469: "Una pozione che fa sentire di colpo un troll gagliardo. Che l'illusione prenda anche il corpo? Sta di fatto che, finché l'effetto dura, il ricambio di chi l'ha bevuta diventa una cosa mostruosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ 沈黙の霧 e' l'incantesimo «Nebbia di silenzio» (`skill.hsp`), gia' reso
    #    anche nel grimorio `:106686` del lotto 048.
    106613: "Una pozione fatta distillando la Nebbia di silenzio raccolta e macinando quel che resta di solido. Basta berla una volta e in gola resta la sensazione di un corpo estraneo: altro che recitare formule. Roba pericolosa.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    106910: "Una pozione che fa sentire di colpo uno scudo che protegge ogni cosa. Per via di quel che contiene, pare che anche un po' d'inquietudine smetta di dare fastidio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    111992: "Una pozione che fa crescere per sempre, stimolando dall'interno i nervi del corpo. Scalda a poco a poco, e la si ritiene ottima per campare a lungo: pare che i grandi ricchi scendano spesso in città apposta per comprarla.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⭐ Le due del ripristino sono una coppia: stessa frase, una per la mente
    #    e una per il corpo, e la battuta finale cambia — 格好よかったあの頃
    #    contro スラっとしていたあの頃. Nessuna delle due chiede il genere del
    #    giocatore, che non si conosce (`guida-stile.md`).
    112063: "Una pozione che, bevuta, riporta alla normalità i danni che avevano preso la mente. Riporta soltanto al te di sempre, quindi non serve, per dire, a tornare a quei tempi in cui facevi ancora la tua figura.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    112134: "Una pozione che, bevuta, riporta alla normalità i danni che avevano preso il corpo. Riporta soltanto al te di sempre, quindi non serve, per dire, a tornare a quei tempi in cui la linea era un'altra.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # I QUATTRO LIQUORI
    # =====================================================================

    114277: "Un liquore fatto fermentando l'orzo. Ha un modo di bere che formicola sulla lingua e un amaro pulito che resta a lungo. Alla taverna di Vernis si vedono i minatori che se la scolano come se fosse acqua.\\n#~Il Mondo Profondo dei Liquori~\\n",

    117531: "Un liquore che si ottiene facendo fermentare l'orzo e poi distillandolo. A Noyel se ne beve molto, ma va forte anche a Porto Kapul, che è il suo principale sbocco commerciale. Di modi per berlo ce n'è più d'uno, ma si dice che un vero uomo lo beva liscio.\\n#~Il Mondo Profondo dei Liquori~\\n",

    129085: "Un liquore di ingredienti ignoti, prodotto di nascosto a Derphy. Formicola come la birra, ma un profumo di frutta gli mette in ordine il retrogusto. Si dice anche che a berlo di continuo faccia venire le allucinazioni, ma i dettagli non si sanno.\\n#~Il Mondo Profondo dei Liquori~\\n",

    # =====================================================================
    # LE SETTE POZIONI DI CURA, IN SCALA
    # =====================================================================

    126007: "Una pozione da far tremare, che porta il nome della sacra guaritrice. Che cosa ci sia dentro non lo sa più nessuno, e il liquido ha il luccichio cangiante dell'iride; ma si dice che basti berne un sorso perché le ferite guariscano come se fossero state un sogno.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⓘ Niente caporali: nel dizionario non ce n'è uno su 25.000 rese, e
    #    CP932 non li ha. Il nome dell'oggetto si cita senza virgolette.
    126078: "Come dice il nome di <Eris>, la guarigione bianca, è una pozione di un bianco latteo. A differenza delle altre non nasce da un estratto: è potere magico legato direttamente all'acqua. Per questo agisce in fretta, e si dice tenga dentro la forza di guarire perfino chi è ferito in fin di vita. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    126149: "Una pozione cara, che porta il nome di <Odina>, grande fra i guaritori. Si dice che a immergere una ferita in quel liquido color mare trasparente, il taglio sparisca come una scritta sulla sabbia. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    126292: "Erbe medicinali che i guaritori custodiscono in silenzio da tempi antichi, ridotte in polvere e mescolate a una pozione. Ha un'aria molto sospetta, ma funziona sul serio: nelle emergenze conviene averne qualcuna dietro. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    126363: "Una pozione dall'aria credibile, con un nome che si capisce al volo. L'effetto è quel che è: contro una ferita che si allarga funziona, ma su un taglio che continua a sanguinare c'è poco da fidarsi.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    126434: "Acqua sgorgata da una montagna silenziosa, in cui sono stati messi l'estratto di cobra e le parole di preghiera di un guaritore. Cura discretamente davvero; ma se il merito sia dell'estratto o della preghiera non c'è modo di saperlo.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    126505: "Tutte le erbe che si dicono buone per ogni male, ammucchiate insieme e fatte bollire a forza fino a farne una pozione che ne ha tutta l'aria. Il sapore è amarissimo e dà l'idea di chissà quale effetto, ma in realtà non è granché.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    126576: "Una pozione ricavata estraendo il potere magico dal bastone di un goblin sciamano. Visto che il bastone è pur sempre di un goblin, l'efficacia si sa già dove arriva. Pare che certi avventurieri se la portino dietro solo per togliersi la sete. \\n# ~Bevande da Bere e Bevande da Non Bere~",

    # =====================================================================
    # LE POZIONI DEGLI STATI ALTERATI
    # =====================================================================

    129156: "Una pozione dal profumo dolce. Si dice che, spruzzata addosso, calmi all'istante anche la belva più feroce. E una bottiglia è quel che ci vuole anche per te che non riesci a dormire.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️ パラライザー e' «il paralizzatore», una creatura del gioco.
    129227: "Il decotto di paralizzatore mescolato a una pozione. A berlo viene un formicolio tale da bloccare il corpo. Se lo si beve per sbaglio non c'è da preoccuparsi, perché passa; ma un consiglio: che non diventi un vizio.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    129298: "Una pozione che, bevuta, scatena un dolore acuto alla testa. Il mal di testa passa, ma intanto fa crollare l'equilibrio, la capacità di leggere e quella di parlare. E siccome i sintomi somigliano a quelli della sbornia, chi la beve per sbaglio viene scambiato per un ubriaco fradicio: da maneggiare con attenzione.\\n# ~Bevande da Bere e Bevande da Non Bere~",

    # ⚠️⚠️ `:129299` NON C'E' PIU', ED E' RINVIATA. Giapponese e inglese sono
    #    tutt'e due `\\t\\t\\n\\n` — due tabulazioni e due a capo, uno slot
    #    vuoto e non una frase. Resa identica, `reimporta` l'ha **rifiutata**
    #    («traduzione identica all'inglese») e col lotto intero, perche' e'
    #    tutto-o-niente; resa vuota non sarebbe esprimibile. Sta in
    #    `rinviate.jsonl`, e le rinviate contano come fatte: la categoria
    #    chiude lo stesso. Vedi `testa050.py`.

    # ⚠️ パンプキン e' «la zucca» nel dizionario.
    129369: "Un fallimento nato durante gli studi per ricavare dall'estratto delle zucche una pozione che rendesse invisibili. Doveva far sparire alla vista chi la beveva, ma l'estratto del mostro reagisce prima di tutto con gli occhi, e finisce per non far più riconoscere nient'altro che se stessi.\\n# ~Bevande da Bere e Bevande da Non Bere~",
}
