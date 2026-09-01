# -*- coding: utf-8 -*-
"""Le rese del lotto 053 — LE ARMI A DISTANZA, prima meta' di `FILTER_RANGE`.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 053 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa053.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri** — a degradarli e' `applica.py`.

⚠️ Forma, da `_forma.py 053`: **47 righe su 50** hanno lo spazio prima del
`\\n` — le tre senza sono `:43632`, `:43705` e `:75515`. Due code non hanno lo
spazio dopo il `#`: `:43631` e `:83146`.

⚠️⚠️ Previsione di `applica`: **+50** per 50 rese, nessuna gemella.
`_gia-reso.py 053`: 0 su 50.

⭐⭐ LA SERIE DELLE TRE ARMI CHE NESSUN UOMO SOLLEVA (`:75515`, `:77075`,
`:77145`). Il giapponese chiude tutt'e tre con la stessa formula —
「人では扱えない程の重さだが、使いこなす者が現れた時この武器は使用者に◯◯を
授けるだろう。それと少しばかりの気まぐれを。」 — e a cambiare e' **una parola
sola**, che e' un **attributo del gioco**: 魅力 carisma, 器用さ destrezza,
超感覚 percezione. Le tre rese ripetono la formula parola per parola e cambiano
solo quella, perche' la ripetizione **e' il testo**: sono tre pezzi di una
serie, e chi ne trova un secondo deve riconoscerla.
⚠️ I tre nomi vengono dal dizionario, non dall'inglese: `_cerca.py` da'
「魅力の成長」 -> «Cresce carisma» e 「器用の成長」 -> «Cresce destrezza». L'inglese
scrive «charm» dove il gioco dice CHR, e chi rendesse dall'inglese scriverebbe
«fascino» su una statistica che a schermo si chiama carisma.
"""

IT = {
    # =====================================================================
    # LA FOGLIA DELLA VOLPE, e il gioco di parole che l'italiano tiene
    # =====================================================================

    # ⚠️ Coda SENZA spazio dopo il `#`.
    # 妖気 non e' nel dizionario: e' l'aura sinistra che emana uno spirito, e
    # l'inglese la lascia in giapponese («Yokai energy»). Qui e' descritta.
    43631: "Una foglia dorata che le Nove Code Dorate hanno creato trasformando il proprio pelo. Dentro ci sta chiusa un'aura sinistra fuori dal comune, ed esplode. Resta una leggenda: chi si presenta al sacello con la foglia d'argento che le fa il paio vede comparire il nume che veglia sul bosco. \\n#~Dizionario Fantastico di Irva~",

    # ⚠️ SENZA spazio prima del `\n`.
    # ⭐ 「ハッパをかける」 e' un doppio senso che l'italiano rende per intero:
    #    ハッパ e' insieme 葉っぱ «la foglia» e 発破 «la carica esplosiva» —
    #    che e' poi il nome dell'oggetto, 金毛発破 — e la locuzione vuol dire
    #    «dare la carica, incitare». «Ti do io la carica» le tiene tutt'e
    #    due, e il BUM che segue la fa scattare.
    #    L'inglese («Lemme give you a little nudge») ne perde una.
    43632: "\\\"Adesso ti do io la carica... BUM!\\\"\\n# ~Parole della Volpe a Nove Code dal Manto d'Oro~",

    # =====================================================================
    # LE CARTE, LE LAME E GLI OGGETTI DA LANCIO
    # =====================================================================

    # ⚠️ SENZA spazio prima del `\n`.
    43705: "Una carta antica e misteriosa. Ci sono intessute dentro una magia segreta e fibre speciali, ed è tanto robusta da servire come arma nascosta da lancio. Ma la sua capacità vera è un'altra, e si dice che possa liberarla solo chi ha imparato l'antica magia che governa la carta magica.\\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ Il giapponese chiude con 「悪魔の兵器」の別称 — «lo chiamano anche
    #    l'arma del diavolo». L'inglese lo butta e ci mette un gioco di
    #    parole suo («shrimply devilish»): qui vale il giapponese.
    52648: "Negli ingredienti non è quasi diverso da un gambero fritto normale, ma provoca il fenomeno detto effetto gambero fritto e, per un motivo o per l'altro, finisce con l'esplodere: è materiale pericoloso. Sparso in aria, o vola via come un missile o resta a terra come una mina. Cadono vittime soprattutto i bambini, incuriositi dall'aspetto, e per questo lo chiamano anche l'arma del diavolo. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ L'inglese qui e' un'altra battuta, in bocca a un altro personaggio
    #    («a eccentric bandit», che gioca su shrimp/shrimping). Il giapponese
    #    e' un commesso confuso che minaccia coi gamberi, e la coda della
    #    tabella dice gia' «Parole di un Commesso Confuso»: rendere
    #    dall'inglese avrebbe messo la battuta del bandito sotto il titolo
    #    del commesso.
    52650: "\\\"Guarda che te ne tiro addosso cinque, di gamberi fritti!\\\" \\n# ~Parole di un Commesso Confuso~",

    # =====================================================================
    # LE BALESTRE E LE BALISTE
    # =====================================================================

    53348: "Una balestra di fuoco costruita da un'organizzazione criminale dell'ombra. Pare che acceleri e scagli i dardi per induzione elettromagnetica, e che li accenda col calore in più che la corrente lascia. La struttura non è perfetta, e ogni tanto il punto d'incrocio manda scintille: quando succede è pericolosissima, e non va toccata. \\n# ~Dizionario Fantastico di Irva~",

    53489: "L'opera degli ultimi anni di un artigiano di baliste che non c'è più. Una balista leggera, fatta per il tiro di precisione. L'artigiano ci ha versato dentro tutto il suo sapere, e ne è uscita una gittata pari a quella di un fucile di precisione. Migliorano anche la forza di penetrazione e il maneggio. Un pezzo da far venire l'acquolina a chi colleziona baliste. \\n# ~Dizionario Fantastico di Irva~",

    53631: "Dormiva in fondo a una grotta piena di serpenti velenosi. Pare un arco a ripetizione pensato per colpire il viso col veleno: la punta delle frecce si spalma di un veleno che schizza, e si tira colpo su colpo. Se il veleno entra negli occhi, il dolore è violento. \\n# ~Dizionario Fantastico di Irva~",

    54743: "Una balestra con in punta una canna che serve ad accendere. Al momento del tiro il dardo prende fuoco e vola via come freccia infuocata. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    67258: "Un tipo di balestra di grande taglia. Le più piccole si riesce in qualche modo a portarle in spalla o a tracolla, ma di suo è un pezzo d'artiglieria da postazione fissa. Sotto ha dei sostegni pieghevoli, ma restare comoda da maneggiare non ci riesce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    68326: "Una balestra che tende la corda con una manovella invece che con l'argano. Ha un caricatore, quindi si ricarica più in fretta, ma colpo per colpo forza e precisione calano di parecchio. Bucare un'armatura non può: alla forza che le manca supplisce col veleno spalmato sui dardi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    72760: "Un tipo di balestra rapida. Un pezzo pregiato, progettato ripensando da capo la struttura della balestra. Eccelle nel tiro veloce e di fila. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # GLI ARCHI
    # =====================================================================

    53701: "Un arco corto che si tramanda fra i quickling. È molto più piccolo di un arco normale, ma pare che per un quickling questa misura sia quella giusta. Al resto rimedia la magia, e per quanto piccolo la forza ce l'ha. \\n# ~Dizionario Fantastico di Irva~",

    54667: "Un arco che tiene conto anche del corpo a corpo improvviso. La parte curva ha una doppia struttura, e di fuori porta una lama con la sua guardia. I flettenti restano dentro, staccati, così anche quando l'esterno si piega nell'incrociare le guardie la freccia parte lo stesso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    61443: "Un arco d'ossa che scaglia frecce cariche d'odio. Si ricava dalle ossa di una bestia torturata fino a farle odiare ogni cosa al mondo, e poi uccisa in modo atroce. Per chi si prende la freccia, ricevere addosso quell'odio è una bella seccatura. Quasi tutti vengono dall'antichità, ma pare che ancora oggi qualche tribù continui a farne di nascosto. \\n# ~Dizionario Fantastico di Irva~",

    61513: "Un arco a lame che parte da un arco magico di Eulderna e lo rinforza innestandoci la tecnica meccanica di Yerles. Regge anche il corpo a corpo, e a premere il grilletto dagli stabilizzatori parte una scarica elettrica. \\n# ~Dizionario Fantastico di Irva~",

    72690: "Il grande arco che la dea del vento creò e portò a lungo con sé. La luce che scaglia cambia sette volte, come un cuore di donna volubile e capriccioso. Se ne è disfatta perché si era stancata di quanto fosse vistoso. \\n# ~Dizionario Fantastico di Irva~",

    78398: "Un arco corto che mette insieme flessibilità e tenacia: alla base ci sono ossa d'animale intagliate, e sopra si sovrappongono altri materiali. Un pezzo pregiato, lavorato in modo che nel tenderlo non si sprechi forza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    86067: "Un arco lungo fatto di un materiale sconosciuto. Dà a chi lo porta addosso la protezione del vento, e si dice che, una volta teso l'arco, là si veda la figura della dea del vento. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # LE ARMI DA FUOCO
    # =====================================================================

    54819: "Un paio di pistole. Sono studiate per frenare il rinculo, così da tenerne una per mano. Sparare con tutt'e due insieme su nemici diversi non conviene: non si prende niente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 光子銃 e' «pistola laser» nel dizionario, non «cannone a fotoni»: e' la
    # forma con cui il giocatore vede il nome dell'oggetto.
    65063: "Una pistola laser che si ritrova in certe rovine. È pesante più di quanto sembri. Chissà perché, capita che ce l'abbiano addosso i corvi, e per questo, mettendoci insieme la sigla, la chiamano karasuwa. Come si chiami davvero non si sa. \\n# ~Dizionario Fantastico di Irva~",

    67390: "Un'arma che il dio delle macchine mise insieme lì per lì, nel folto della mischia, coi pezzi di ricambio del cannone secondario di una corazzata. Si racconta che il colpo, carico di forza divina, passasse da parte a parte lo scafo della flotta del caos, e che l'onda d'urto riducesse in nebbia i suoi servitori. \\n# ~Dizionario Fantastico di Irva~",

    71579: "Due pistole che fanno una cosa sola, nate da un grifone, e che sparano di fila a gran velocità. Le distingue l'impugnatura grande, comoda da tenere. \\n# ~Dizionario Fantastico di Irva~",

    72281: "Il rifacimento di un raro fucile a pompa trovato fra le rovine, capace di tiro tutto automatico e di lanciare piccole granate apposite. Chi lo trovò propose all'esercito di produrlo in serie, ma pesante, ingombrante e con troppa potenza di fuoco com'era, nessuno lo degnò di uno sguardo. Allora, presala di petto, lo rifece apposta per il combattimento ravvicinato, accorciando calcio e canna. Per forza distruttiva e capacità di tenere a bada il nemico è tripla A come dice il nome, ma in cambio ha perso per strada parecchie cose che a un fucile servono. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ Garok e' il fabbro leggendario: la sua e' l'unica voce del lotto che
    #    giudica un altro artigiano, e il giapponese e' brusco (気が狂っとる,
    #    con la desinenza dialettale). L'italiano tiene la bruschezza.
    72283: "\\\"Ma che roba è questo piano di rifacimento?! Qui è da matti...\\\" \\n# ~Parole di <Garok> il fabbro leggendario~",

    76389: "Un'arma da fuoco fatta apposta per il tiro di precisione. Adatta a sparare da lontano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 異名 e' il soprannome: il giapponese intitola l'arma con quello di un
    # tiratore famoso (ベーラヤ・スメルチ; l'inglese ne usa un altro). Il fatto
    # e' che quel nome NON e' dell'arma, ed e' questo che si rende.
    76458: "Un fucile di precisione che porta il soprannome di un tiratore formidabile. Non ha il cannocchiale da tiro, e per un profano prendere il bersaglio è difficilissimo. La canna, poi, è un po' corta e pesante. \\n# ~Dizionario Fantastico di Irva~",

    77424: "Due pistole che fanno una cosa sola. Si racconta che un tempo le usassero due gemelli, una per uno. Quando il maggiore cadde in battaglia, la sua pistola passò al minore come ricordo. E si dice che il minore abbia speso la vita intera a mettere a punto le basi dell'arte delle due pistole. \\n# ~Dizionario Fantastico di Irva~",

    77913: "Un tipo di mitragliatrice che, facendo ruotare e sparare più canne insieme, è riuscita a smorzare il calore d'attrito del tiro e a spingere più in alto la rapidità di fuoco. Ma per frenare rinculo e vibrazioni la cadenza è stata abbassata un poco di proposito. \\n# ~Dizionario Fantastico di Irva~",

    80356: "Il perfezionamento di una pistola che era riuscita a meccanizzare il lavoro di caricare i colpi. Nel lunghissimo tempo passato da allora, purtroppo, gli esemplari da cui viene sono andati tutti perduti: solo questa è ancora in forma. \\n# ~Dizionario Fantastico di Irva~",

    # 詠唱 nel dizionario e' «incantesimi» (la voce «Incantesimi» della
    # scheda: 詠唱スキル上昇 -> «bonus in Incantesimi»), non «canto».
    85997: "Un fucile a pompa che rimanda la luce in ogni direzione, e che si dice sia opera di un maestro armaiolo. Il fumo di polvere speciale che erompe con forza dalla bocca dell'arma avrebbe il potere singolare di disturbare il lancio degli incantesimi. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # LE TRE ARMI CHE NESSUN UOMO SOLLEVA — la serie, vedi il docstring
    # =====================================================================

    # ⚠️ SENZA spazio prima del `\n`.
    75515: "Una moneta di pietra gigantesca. È il pezzo vero che circolava nella civiltà antica, ed è preziosissima. Pesa troppo perché un uomo la maneggi, ma quando comparirà qualcuno capace di usarla, quest'arma gli donerà un carisma smisurato. E insieme un pizzico di capriccio.\\n# ~Dizionario Fantastico di Irva~",

    77075: "Una balestra gigantesca. Pesa troppo perché un uomo la maneggi, ma quando comparirà qualcuno capace di usarla, quest'arma gli donerà una destrezza fuori dal comune. E insieme un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    77145: "Un enorme cannone a gravità con le granate. Per rimediare all'instabilità del cannone a gravità gli hanno montato sopra un lanciagranate. Pesa troppo perché un uomo lo maneggi, ma quando comparirà qualcuno capace di usarlo, quest'arma gli donerà una percezione fuori dall'umano. E insieme un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # GLI SHURIKEN, LE MONETE E IL RESTO DEL LANCIO
    # =====================================================================

    57384: "Uno scarabeo che tanto tempo fa fu reso cibernetico solo per farlo lottare con altri insetti. Un tempo se ne allevavano molti; oggi restano soltanto quelli abbandonati, inselvatichiti, che vivono nascosti. A lanciarlo spazza via perfino una belva, e se va all'unisono con chi lo usa scaglia raggi misteriosi e soffi di scoppio. Non parla, ma un io ce l'ha: dagli un nome e vogliagli bene. \\n# ~Dizionario Fantastico di Irva~",

    64413: "Un tipo di shuriken, avvolto in un'energia potente. Se coglie in pieno taglia tanto da passare da parte a parte anche la corazza di un aereo da combattimento. Di ioni non è fatto affatto: lo chiamano così perché è stato lavorato con un fascio di ioni. Secondo lo stato dell'energia il colore vira all'azzurro o al celeste. \\n# ~Dizionario Fantastico di Irva~",

    68182: "Un grosso blocco di roccia. Prendersene uno addosso non finisce con un semplice male. È pesante, e per giunta ha una forma storta che lo rende difficile da tirare: più ancora delle altre armi da lancio, la sua forza si vede solo da vicino. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    72351: "Un'arma nascosta a forma di carta da gioco. Il bordo è una lama affilata, e un collo umano lo taglia senza fatica. È fatta un po' pesante per restare stabile quando la si lancia. \\n# ~Dizionario Fantastico di Irva~",

    73222: "Una granata potente, che vanta la forza più alta di tutte. Proprio per questo bisogna badare con la massima attenzione a non restare presi nello scoppio. \\n# ~Dizionario Fantastico di Irva~",

    74235: "Uno shuriken che ha cercato la forza sacrificando il poco ingombro e la segretezza. Grande com'è non è più un'arma nascosta, ma ha il pregio di servire anche a parare. La lama è di metallo raro, e taglia anche le cose dure. \\n# ~Dizionario Fantastico di Irva~",

    74503: "Un pugnale che recide gli incubi. Non taglia granché, ma a lanciarlo vola lontano e dritto. \\n# ~Dizionario Fantastico di Irva~",

    77843: "Una moneta che si usava in un paese d'isole tanto tempo fa da far girare la testa. Stando a testi più recenti, pare che fra le guardie di allora ci fosse chi combatteva lanciandola. \\n# ~Dizionario Fantastico di Irva~",

    82547: "Un'arma da lancio che di strumento musicale ha solo il nome. Quella cosa, che si scambierebbe per un enorme lingotto d'oro, si dice abbia macellato in passato un gran numero di musicisti. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ Coda SENZA spazio dopo il `#`.
    83146: "Una scheggia di minerale d'adamantio. È di qualità piuttosto scadente, quindi non va bene neanche da ornamento, e usarla così come arma da lancio è il massimo che se ne possa fare. \\n#~Dizionario Fantastico di Irva~",

    83275: "Una bomba piccola, fatta per essere lanciata. Cade dopo un arco e scoppia su un'area larga, quindi l'effetto arriva lontano; ma la forza la scarica su amici e nemici allo stesso modo, e va maneggiata con attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    83342: "Un'arma da lancio con la lama, in uso presso i servizi segreti di un paese straniero. Le forme sono le più varie, ma su tutte è spalmato per bene un veleno che ritarda la chiusura delle ferite, e si dice che faccia sanguinare chi viene colpito. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LE DUE VOCI DELLA BIANCHERIA
    # =====================================================================

    83015: "Un pezzo di stoffa graziosa e per bene, con un nastrino sul davanti. Il più delle volte non ce l'ha lei, ma qualcun altro, e pare che l'unica a non essersene accorta sia proprio Shena. \\n# ~Le Notizie Raccolte da <Wiesem> l'informatore~",

    # 炭鉱街 e' «la citta' mineraria» e basta: il nome Vernis lo aggiunge
    # l'inglese. Chi parla e' un nobile alle sue ultime parole, e il
    # giapponese chiude con una vanteria rivolta a chi ascolta.
    83017: "\\\"Quando andai nella città mineraria, mi innamorai. Ma non ebbi il coraggio di rivolgerle la parola, e allora chiesi a un certo ladro famoso di procurarmi questo. Così io e lei siamo sempre insieme. Ebbene, mi invidiate, vero?\\\" \\n# ~Le Ultime Parole di <Luster> il nobile~",

    88670: "Un'\\\"arma\\\" che a quanto si dice un artigiano apposito tesse per le fanciulle. Perché mai la biancheria sia un'arma, lo si capisce da sé una volta che la si è presa in faccia. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LO YOMI-TO
    # =====================================================================

    53561: "Una scheggia dello Yomi-To. È il frammento del masso che chiudeva il passaggio verso l'Oltretomba. Per quante volte lo si rimetta i morti lo riducono in pezzi, e pare che chi ne ha la cura sia in grande difficoltà. \\n# ~Dizionario Fantastico di Irva~",
}
