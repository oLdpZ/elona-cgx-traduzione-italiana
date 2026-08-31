# -*- coding: utf-8 -*-
"""Le rese del lotto 041 — LE ARMI, prima parte: gli artefatti e le armi base.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 041 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa041.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Tre eccezioni di spaziatura, che il preflight controlla e che qui si
   dichiarano perche' non si vedono leggendo:
     :43558  la coda e' `#~` SENZA spazio dopo il cancelletto (tutte le altre
             venticinque righe di Irva l'hanno)
     :63723  il corpo NON ha lo spazio prima del `\\n`
     :65265  idem

⚠️ Tutti gli accenti di questo lotto sono in FONDO alla parola: `degrada()` li
   scrive come apostrofo, e in fondo non spacca niente. Nessuna parola porta un
   accento in mezzo, che e' il difetto di «dei» del lotto 035.
"""

IT = {
    # === GLI ARTEFATTI DELLA PRIMA ZONA ===================================
    43558: "Una picca fatta a somiglianza di un osso. Di osso, però, non è. A morderla e rimorderla si scarica lo stress, e volendo si mangia come merenda. Come arma, si usa nel modo dell'ascia da battaglia. \\n#~Dizionario Fantastico di Irva~",
    51779: "Una spada nera, nata dall'idea di usare un male ancora più grande per scacciare il male. Ne esistono più d'una, oltre i confini del mondo, che si potrebbero dire suoi sdoppiamenti: ognuna ha forma e poteri appena diversi. \\n# ~Dizionario Fantastico di Irva~",
    51849: "La leggendaria lancia di bambù che è il simbolo di libertà e indipendenza. Dicono che, in mano a chi la merita, non solo uccide un ninja con un colpo solo, ma abbatte perfino i bombardieri e riesce ad ammazzare anche un dio. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ il nome che il giocatore vede e' <Mano del Kalpa>: la prosa lo ripete,
    #    come vuole il contratto dei nomi.
    51917: "La Mano del Kalpa. Il kalpa è il tempo che passa dalla nascita di un mondo alla sua fine. Sulla superficie della lama scorre un flusso di tempo smisurato. Chi la impugna caricandola di forza divina può squarciare lo spazio e il tempo, e c'è chi se ne serve anche per spostarsi. \\n# ~Il Libro della Sapienza~",

    # ⚠️ il giapponese scrive TRE volte 杏仁豆腐: l'oggetto, l'elsa e la lama
    #    sono tutti budino di mandorle, ed e' la battuta. L'inglese ne perde
    #    uno e scrive «Tofu attached to an Annin».
    52717: "Un budino di mandorle: a un budino di mandorle a forma d'elsa ne è attaccato un altro, lungo, sottile, luminoso e capace di trapassare. Taglia un po' meno di una spada laser. \\n# ~Dizionario Fantastico di Irva~",

    52787: "Una terza mano gigantesca che il granchio si è fatta a somiglianza della propria chela. È composta dai gusci delle creature che ha divorato e da muscoli finti, e pare che la muova con un innesto nervoso. Una cosa che sembra una chela di granchio e non è una chela di granchio. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ il giapponese dice ＳＰ; l'inglese scrive «stamina». Si segue il
    #    giapponese, come nei globi oscuri del lotto 034.
    52857: "Un kunai da lancio particolare, tramandato da una scuola di ninja. Pare che per averlo bisogni superare una prova in mezzo alla bufera, sulle montagne. Si lanciano tutti insieme e per questo colpiscono facile, ma sono ingombranti e pesanti. Hanno il potere di togliere SP a chi colpiscono. \\n# ~Dizionario Fantastico di Irva~",

    52927: "Un fioretto che, dicono, un giorno di tempesta cadde dal cielo insieme a un fulmine. Quel che lo distingue è che sa comandare nel minimo l'elettricità che produce. Può accumularla nella lama e scagliare scariche, e può perfino farla passare in chi lo impugna per spingergli a forza i riflessi, anche se il prezzo da pagare è alto. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ 水中潜航や飛行 sono DUE cose: immergersi e volare. L'inglese le
    #    fonde in «dive and fly underwater», che vuol dire un'altra cosa.
    52996: "Un trapano buono a tutto, fatto per sfondare ogni ostacolo e andare avanti in cielo, in terra e in mare. Sbriciola senza fatica la roccia dura e i blocchi di ghiaccio, e sa immergersi sott'acqua e volare. E poi, già che c'era, monta pure un cannone congelante. \\n# ~Dizionario Fantastico di Irva~",

    53067: "Un tomahawk deforme, lontanissimo dal tomahawk comune. Monta un sistema di controllo della traiettoria a nanomacchine. Gira su sé stesso, e per questo non perde slancio nemmeno quando prende il bersaglio. Al contrario, mentre torna in mano rallenta la rotazione perché sia facile riprenderlo. \\n# ~Dizionario Fantastico di Irva~",

    53137: "Una falce che si dice fatta da un artigiano uomo uccello, pensata anche per il combattimento in volo. Ha due lame che paiono un becco lungo e sottile. Essendo a doppio taglio, taglia anche premendo senza tirare, e può stringere il bersaglio in mezzo e reciderlo. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ l'inglese lascia cadere 見た目によらずかなりのハイテク武装で:
    #    «a dispetto dell'aspetto e' un'arma di alta tecnologia».
    53206: "Uno shakujo con la lama nascosta dentro, ritrovato fra le rovine. A dispetto dell'aspetto è un'arma di alta tecnologia, e la lama di nanomacchine arroventate vanta un taglio spaventoso. Perché si possa usare senza l'aiuto della vista, anche il suono degli anelli è studiato apposta. \\n# ~Dizionario Fantastico di Irva~",

    53278: "In origine erano tre bastoni, ciascuno con una benedizione diversa. Morti i tre guerrieri che li portavano, un discepolo che avevano in comune li lavorò e ne fece un nunchaku solo. Rafforza parecchie doti; poi, se fra loro si incastrino davvero, è un altro discorso. \\n# ~Dizionario Fantastico di Irva~",

    # === I CALZINI DI NAZUNA, CORPO E BATTUTA =============================
    53418: "Fra gli appassionati sono valutati altissimo: l'odore non se ne va nemmeno lavandoli, e di base valgono quanto un paio tenuto addosso sei mesi. Chi li porta li butta appena si accorge del fetore, ma qualcuno li recupera con la scusa di metterli al sicuro, e finiscono al mercato nero. \\n# ~Dizionario Fantastico di Irva~",
    53420: "\\\"Questo non è solo un oggetto che puzza. Da tutto quel sudore, entrato dentro fino a far tossire, si sente subito la fatica di ogni giorno. ...Devo darci dentro anch'io.\\\" \\n# ~Il Giudizio dello Spadaccino dei Calzini~",

    # === LE ARMI BASE, DALLA RACCOLTA DI ARMI E ARMATURE ==================
    53840: "Un coltello da sopravvivenza che viene dal mondo dei ninja. Pare che fin dall'antichità sia stato tenuto caro come attrezzo buono a tutto: portarne uno con sé mette tranquilli. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    53908: "Una spada sottile che deriva dalla rapiera. È alleggerita, così la maneggia anche chi ha poca forza. Sottile e all'apparenza fragile, uccide lo stesso se si mira preciso alle fessure dell'armatura. Quando la punta preme, ci passa dentro l'elettricità. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    53975: "Una macchina a spirale, a forma di cono, che gira. Conficcata la punta, le lame dentro le scanalature tritano e sbriciolano quel che trovano. Negli scritti antichi si incontra qua e là la descrizione di carri armati e navi da guerra che se ne servivano per infilarsi sottoterra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54042: "Una lancia disegnata per infilzare lasciando fare allo slancio del cavallo. Essendo da carica è fatta pesante e robusta, e nella mischia non va bene. Se la vuoi usare a piedi, il peso e la scomodità te li devi risolvere con la forza delle braccia. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54112: "Un'ascia maneggevole. Il baricentro e la forma del manico sono regolati perché, tirandola, si pianti bene. Non bisogna però dimenticare che l'uso principale resta tenerla in mano e colpire. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54180: "Una macchina che fa girare a gran velocità una catena piena di lame. Serve ad abbattere gli alberi. Se la usi per combattere, attento a non ferirti quando ti torna indietro di rimbalzo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54248: "Una falce a forma di forbice. Pesa, ma la lama secondaria arriva su una traiettoria appena diversa e per il nemico schivarla è difficile. Essendo a doppio taglio, a differenza della falce comune ferisce anche di punta. E ce n'è qualcuna che ha davvero il meccanismo per chiudersi e tranciare, come una forbice. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⚠️ l'inglese lascia cadere 一般的に見かけよりも軽く、鋭い: «di solito e'
    #    piu' leggera e piu' affilata di quel che sembra». Salta diritto al
    #    «However».
    54316: "Una falce fatta di ossa messe insieme. Di solito è più leggera e più affilata di quel che sembra. Regge però poco, e se non la si tiene in ordine il taglio se ne va in fretta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    54384: "Un'arma d'urto da combattimento che deriva da un attrezzo da lavoro. In cima ha una testa di martello innestata ad angolo retto: è quella che si batte per dare il colpo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54453: "È un tipo di mazza, ma la palla di ferro a stella, irta di punte, è legata al manico da una catena. Arriva più lontano, e la forza centrifuga ne aumenta anche la potenza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54521: "Un bastone che usano certe scuole religiose. Nell'anello grande in cima ne sono infilati altri, e a scuoterlo suona. Si crede che quel suono abbia effetti benedetti: tiene lontano il male e leva i desideri che tormentano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    54591: "Un bastone fatto di due o più sezioni. Sono legate fra loro da catene e si possono separare. Per girarlo da separato senza prendersi in faccia ci vuole la sua pratica. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # === GLI ARTEFATTI DELLA SECONDA ZONA =================================
    56808: "Un'arma naturale che un dinosauro si è fatta da sé. Pare che, per aumentarne la forza, l'abbia resa così pesante da rendersi difficile la vita di ogni giorno. È attaccata al corpo da fibre muscolari rivestite di gravitoni e da ossa, e per quanto la si giri con tutta la forza non si stacca. \\n# ~Dizionario Fantastico di Irva~",
    60195: "Un'ascia da battaglia leggera per quanto è grande. È regolata in modo da poterla girare anche con una mano sola. Oltre ad avere in ogni sua parte dei meccanismi che aiutano la magia, la lama disperde l'aria intorno e si fa il vuoto, così l'attrito dell'aria non la tocca. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ la riga di gioco: パワーゲージ e' «la barra di potenza» (`chat.hsp`),
    #    使役 e' «soggiogare», 棺 e' «la bara», アンデッド sono «i non morti».
    #    融合アンデッド nel dizionario non c'e': si scrive sulla forma
    #    dell'abilita' *Fusione dei morti*.
    60786: "Pare l'abbia fatta un dio di chissà dove, ma a un certo punto è finita nel mondo degli uomini ed è diventata il giocattolo di negromanti e potenti. Calando del 25% la barra di potenza, rimanda nella bara una combinazione stabilita di non morti al tuo servizio che hai in vista, e chiama un non morto di fusione. Dello stesso tipo, però, non se ne può soggiogare più d'uno per volta. Il non morto di fusione chiamato così non diventa bara, e si distrugge da sé quando chi l'ha evocato lascia la mappa. \\n# ~Dizionario Fantastico di Irva~",

    61248: "Un martello da guerra rifatto perché sembri un bastone da passeggio. Ha peso e robustezza che bastano a sfondare un cranio. A chi si distrae, la testa gliela stacca di netto. \\n# ~Dizionario Fantastico di Irva~",
    61793: "Una falce a catena rosa. La lama è tonda, il contrappeso è piccolo, e a vederla non pare capace di gran che. In realtà è un arnese da ninja che comanda vortici di energia, e fidarsi dell'aspetto è pericoloso. Di solito la parte della falce sta nascosta e il resto pende come una catenina alla moda. \\n# ~Dizionario Fantastico di Irva~",
    63454: "Un bastone che converte in forza d'attacco gli MP di chi lo usa. Con abbastanza MP tira fuori una potenza tale che chiamarlo l'arma più forte non sarebbe esagerato. Ma ogni colpo li consuma, e per servirsene bene ci vuole fiuto. E con pochi MP diventa un bastone e basta, robusto e nient'altro. \\n# ~Dizionario Fantastico di Irva~",

    # === IL FALCO BIANCO, CORPO E BATTUTA =================================
    # ⚠️ :63723 NON ha lo spazio prima del `\\n`.
    # ⚠️ il nome dell'oggetto resta <The White Hawk>, ma 白き鷹 e' il
    #    soprannome del SOLDATO e in giapponese non e' in katakana: si rende.
    63723: "Una spada lunga disegnata con la figura di un falco. Qualunque cosa tagli, non le si attacca addosso una goccia di sangue, e resta bianca fino a parere malata. In molti trovano la cosa inquietante. Il soldato di Zanan che trovò questa spada fra le rovine, di battaglia in battaglia, diventò famoso come \\\"il Falco Bianco\\\".\\n# ~Dizionario Fantastico di Irva~",
    63725: "\\\"Il taglio pare non abbia nulla da ridire... ma per me è un po' troppo pulita.\\\" \\n# ~Parole di <Loyter> l'eroe cremisi di Zanan~",

    # === GLI ULTIMI ARTEFATTI =============================================
    64485: "Porta un nome che vuol dire asso di picche. Pare sia il rifacimento di una pala che stava piantata in un campo di battaglia. Taglia e punge come un'alabarda, e la lama larga, fatta di acciaio antiproiettile, fa anche da scudo. Fuori dal combattimento serve a scavare buche e a tagliare i rami che intralciano la marcia. Per tenere insieme il manico allungabile e la robustezza è venuta pesantissima, ed è scomoda: questo è il difetto. \\n# ~Dizionario Fantastico di Irva~",
    65133: "Un'arma contundente rivestita di metallo nero, con incastonate schegge di metallo a forma di mandorle spezzate. Sorpresa: in origine non era un'arma, ma un ornamento che stava in mezzo a un villaggio. A quel che si dice, sarebbe la statua dell'eroe che nascose e salvò quel villaggio quando una guerra stava per cancellarlo. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ :65265 NON ha lo spazio prima del `\\n`.
    65265: "Una frusta scacciademoni, nata da un rito oscuro per annientare i mostri malvagi. Nel rito, dicono, furono spese moltissime vite, di uomini e di demoni senza distinzione. Ha qualcosa come una volontà propria, e si mostra a chi ha scelto. Pare che, insieme alla frusta delle origini e alla frusta ammazzavampiri, passi di mano in mano ancora oggi, attraverso il tempo.\\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ l'inglese lascia cadere 下手に触れると死にたくなるような痛みと激しい
    #    吐き気に襲われる: il dolore da morire e la nausea violenta.
    65879: "Un tralcio d'edera tagliato e ridotto a frusta. La superficie è tutta coperta di peluria fitta, ma ogni pelo è una spina acuminata e velenosissima: a toccarla male ti prende un dolore da farti venir voglia di morire e una nausea violenta. Anche solo un graffio, se lo si trascura, fa sprizzare sangue da tutte le mucose del corpo, quindi va maneggiata con attenzione. Come minimo, meglio non girarla a mani nude. \\n# ~Dizionario Fantastico di Irva~",

    66840: "Un pugnale che, dicono, suona il timbro che ti passa per la testa. Solo che per farne una melodia senza rumore in mezzo ci vuole una gran concentrazione, e da strumento è parecchio difficile. Come lama non uccide granché, ma in certe mani sa tirare fuori di tutto, dall'onda che addormenta al boato, e allora diventa un'arma spaventosa. \\n# ~Dizionario Fantastico di Irva~",
    66910: "Uno spadone che, tenendo insieme con la forza magica estratta da chi lo porta una lama divisa in più segmenti, si può girare e menare come una frusta. Da unito, i pezzi della lama stanno soltanto sovrapposti l'uno all'altro, e così com'è la lama andrebbe in pezzi al primo colpo. Per questo bisogna coprirla con la forza magica che il portatore le fornisce, e tenerla salda. \\n# ~Dizionario Fantastico di Irva~",
}
