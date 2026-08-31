# -*- coding: utf-8 -*-
"""Le rese del lotto 035 — gli ATTREZZI, terza parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 035 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa035.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ Tre righe non hanno lo spazio prima del `\\n`: `:65195`, `:73020`, `:73828`.
⚠️ Niente virgolette a caporale: nel dizionario non ce n'e' **nessuna** su
24.940 rese, e CP932 non le ha.
"""

IT = {
    # === LE TRE ARMI RIESUMATE ============================================
    62020: "Un'arma che spara razzi nucleari. È pensata per la prima linea e per distruggere un bersaglio preciso, quindi la gittata e il raggio dello scoppio sono piuttosto contenuti. La forza per area però è alzata, e bisogna stare attenti a non restarci dentro. Non si ricarica, e per come regge la canna è comunque usa e getta. Col peso che ha, portarla addosso è dura: di solito la si carica su un veicolo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",
    62096: "Un'arma portatile che spara razzi incendiari uno alla volta da quattro canne. È molto migliorata, e sulla distanza corta è precisa. La miscela speciale che ci bruciano dentro scalda in modo tremendo, e gli schizzi addosso danno ustioni gravi. Ha fuoco da bruciare un'intera area, ma è ingombrante e fra gli Yerles non la usa quasi nessuno. Per la forma che ha, ogni tanto ci si sbaglia su da che parte esca il colpo. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",
    62098: "\\\"Sparare in direzione del nemico.\\\" \\n# ~Il Foglietto delle Istruzioni Allegato~",
    62172: "Un lanciarazzi anticarro che, dicono, si usava nelle civiltà passate. La spinta speciale del razzo tiene bene il vento di lato, e il tiro è preciso. La testata a carica cava buca la corazza e le armature di metallo, ci infila dentro lo scoppio e fa danno. Il difetto è che pesa molto per quanti colpi porta. \\n# ~Puoi Usarle Anche Tu! Le Armi Riesumate~",

    # === LA COPERTA =======================================================
    62234: "Una coperta sottile e però soffice. Fa dormire bene, ma alzarsi la mattina diventa dura. Molto dura. \\n# ~Palmia: Collezione Autunno-Inverno~",
    62236: "\\\"Ora devo alzarmi e fare colazione... e finire i guanti di ieri sera... No... ho sonno... ancora un po'... solo un altro pochino.\\\" \\n# ~Parole di una Bambina Avvolta in una Coperta~",

    # === IL PRONTO SOCCORSO E LE MUNIZIONI ================================
    62600: "Una cassetta con dentro medicine e attrezzi da medico usa e getta. Cura le ferite secondo la destrezza di chi la usa e quanta biochimica sa. E riduce di molto i sintomi di paralisi, cecità, veleno e sanguinamento. \\n#~Primo Soccorso in Casa~",
    62666: "Una cassa con dentro frecce e munizioni. Ricarica al massimo tutto tranne le munizioni fermatempo, ma pesa parecchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # === IL LEONE MORTO ===================================================
    63521: "Un leone che, se lo si usa, dopo un conto alla rovescia fa un'esplosione nucleare. Il leone è morto, ma siccome funziona da bomba atomica non è un problema. \\n# ~Dizionario Fantastico di Irva~",
    63523: "\\\"Un leone morto val più di un cane vivo.\\\" \\n# ~Scarabocchi su un Quaderno Misterioso~",

    # === I CINQUE NUCLEI DI TRANSIZIONE ===================================
    # ⚠️ l'inglese salta una frase intera del giapponese (che cosa cambia:
    #    a volte solo un pezzo di vestiario, a volte tutto il corpo).
    # ⚠️ 魔石 e' «pietra magica», non «special gemstone»: la formula
    #    d'apertura e' quella di :43240, gia' resa nel lotto 033.
    63937: "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Forza e la Percezione di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",
    64005: "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la Magia e la Destrezza di chi lo usa. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",
    64073: "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco rende più veloci e alza la Schivata. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",
    64141: "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza la difesa e la capacità di recupero. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",
    64209: "Un oggetto magico con dentro una pietra magica. Si collega a chi lo usa e ne cambia aspetto e capacità. Il cambio d'aspetto dipende molto dallo stato di chi lo usa: a volte cambia solo un pezzo del vestiario, a volte il corpo diventa tutt'altra cosa. Per un poco alza tutte le doti di chi lo usa, ma il carico è forte e rode la vita. Una volta usato, per un po' non si può riusare. \\n# ~Compendio Completo degli Oggetti Magici~",

    # === LO SPECCHIO E IL CESTO ===========================================
    64553: "Uno specchio che, con la forza magica di cui è carico, si collega allo spazio a quattro dimensioni. Si usa un numero limitato di volte, ma è comodo per mettere in ordine il carico. Gira una leggenda di città: se piaci allo specchio, dalla superficie esce una mano e ti tira dentro. E infatti c'è il rapporto di una ragazza che, mentre metteva in ordine, si è vista afferrare per la manica e l'ha respinta rompendo alla mano tutte le dita. \\n# ~Compendio Completo degli Oggetti Magici~",
    64678: "Un bel cesto pieno zeppo di cibo. Ci si sazia tutti insieme. È l'ideale per un picnic in tanti, ma preparare tutto quel cibo è una fatica e, per la quantità, pesa. \\n# ~I Comprimari della Cucina~",

    # === LA CHIAVE DEL CIMITERO E IL RIMODELLATORE ========================
    64741: "La chiave del cimitero DD, che starebbe fra questo mondo e l'oltretomba. Da quando è stata fatta si sentono storie strane di gente finita per sbaglio in un mondo sinistro pieno di bare. Forse l'interferenza apre un ingresso anche altrove. \\n# ~Compendio Completo degli Oggetti Magici~",
    64807: "Una materia misteriosa che la tecnica di oggi non sa spiegare. Basta pensare a un braccio, o a una gamba, e quel pezzo, dicono, ti si attacca addosso senza accorgersene, come se ci fosse sempre stato. I pochi che l'hanno trovata dicono tutti solo che se la sono vista rotolare ai piedi, e da dove venga non si sa. La usano soltanto loro e sparisce appena usata: per questo studiarla è difficile. \\n# ~Dicerie Bizzarre~",

    # === IL GUANTO DI SFIDA ===============================================
    # ⚠️ l'inglese salta la frase sul karma. Si segue il giapponese.
    # ⚠️ :65195 non ha lo spazio prima del `\\n`.
    65195: "Il guanto che si usa per sfidare a duello. Che nel duello l'altro resti ferito o ci muoia, il karma non ne risente. Ha una forza come di maledizione: chi lancia il guanto non può più fuggire da quella mappa finché la cosa non è decisa. Chi vince il duello si prende una parte più grossa delle cose dell'altro.\\n# ~Duellanti Ardenti~",
    # ⚠️ «bugiardo» direbbe il genere di chi legge: la battuta e' rivolta a
    #    chi ha lanciato il guanto, cioe' al giocatore. Si riscrive al verbo.
    65197: "\\\"Menti.\\\" \\n# ~Parole di Chi è Stato Maledetto~",

    # === LA LENTE DELL'INTUITO ============================================
    65464: "Un oggetto magico che porta il nome di Intuito. Tenendolo all'occhio e guardandoci dentro un bersaglio, la lente ne imprime per un poco i dati. Costa il suo e si usa una volta sola, quindi gli informatori non lo adoperano. \\n# ~Compendio Completo degli Oggetti Magici~",
    65466: "\\\"M-ma non è scortese fissare la gente con un affare simile?\\\" \\n# ~Parole di un Cittadino in Affanno~",

    # === IL SIGILLO E IL JUKEBOX ==========================================
    66075: "Un amuleto che ha la protezione delle otto divinità che reggono l'Irva di oggi e di una nona, misteriosa. Al centro c'è disegnato piccolo un segno che non si capisce se sia un occhio o un pilastro. Non ha una vera forza contro i demoni, ma pare che a portarlo addosso non ci si lasci più confondere dalla voce che spinge a cambiare dio. \\n# ~Compendio Completo degli Oggetti Magici~",
    67666: "Una macchina con dentro tanti dischi musicali. Ha una fila di titoli e di pulsanti, e si sceglie il brano da far suonare. Brilla bella di luci colorate. \\n# ~Le Melodie della Limpida Irva~",

    # === LA PIPA DA OPPIO =================================================
    # ⚠️ l'inglese dice «disguised as a pack of cigarettes»: il giapponese
    #    dice キセル, una pipa normale. Si segue il giapponese.
    68587: "Un attrezzo da fumo fuorilegge, di quelli che passano dal mercato nero. Chi lo usa viene punito. Nelle trattative, di nome, lo mascherano da kiseru comune. Dentro ha una droga fatta di crimberry essiccate, e a usarlo l'umore si alza di colpo. Si sa che come effetto secondario porta malinconia, quindi offrirlo a chi non ti obbedisce non serve: rifiuterà. \\n# ~Selezione! I Piaceri Clandestini~",

    # === LE DUE GEMME =====================================================
    68717: "Una gemma che attiva il nucleo della Nefia e ne sveglia la vera forza. Quella forza agisce anche sui mostri dentro la Nefia, e li fa imbestialire. \\n# ~Dizionario Fantastico di Irva~",
    68783: "Il filo rosso del destino, filato con le anime di chi è legato da un vincolo. Per quante volte il mondo cambi e il tempo giri, in capo al tempo, di là dai mondi infiniti, li legherà di nuovo l'uno all'altro. \\n# ~La Profezia di Aion~",

    # === IL CONCIME E IL KIT DI CIOCCOLATO ================================
    69454: "Dà nutrimento alle piante, e porta crescita rapida e qualità migliore. Molte colture di Irva assorbono il nutrimento a una velocità fuori dal comune, quindi l'effetto è immediato ma non dura. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",
    70333: "Un attrezzo usa e getta con dentro tutto, dagli ingredienti agli arnesi. Anche senza una briciola di Cucina il cioccolato fatto in casa viene bene. Purché non ci si metta a fare gli scemi. \\n# ~I Comprimari della Cucina~",

    # === LA BARA DELLA NEGROMANZIA ========================================
    70598: "Con un cristallo di forza magica per nucleo, dentro la bara si costruisce un corpo provvisorio con i resti coltivati. Finito che è, serve soprattutto da recipiente per portarlo in giro. Quanto è forte il non morto che ne esce dipende da Anatomia e Alchimia di chi lo fa. \\n# ~Negromanzia per Principianti~",

    # === LA PENNA DI LUCE ASTRALE =========================================
    70817: "Una penna d'oca intrisa di luce astrale. Interviene, entro un limite, sul registro akashico, dove sta scritta l'esistenza di ogni vita di questo mondo, e lo riscrive perché del soggetto ne esista un secondo. Quello in più è la stessa persona, con gli stessi ricordi e lo stesso carattere, ma è sciolto dal ruolo e dal destino che aveva. Chi la usa però deve avere almeno metà del grado di esistenza del soggetto. E l'intervento chiede, secondo quel grado, l'inchiostro magico come materia: se il soggetto non lo vuole con tutto il cuore, fallisce. \\n# ~Dizionario Fantastico di Irva~",

    # === LA BAMBOLA DELLE PULIZIE =========================================
    71924: "Una bambola che fra gli addetti alle pulizie si tramanda da tempo come amuleto. Si dice che nel cuore della notte si metta in moto da sola e vada a caccia dei demoni neri e marroni. \\n# ~Dizionario Fantastico di Irva~",

    # === IL BIGLIETTO E LA MASCHERA =======================================
    72484: "Se dopo il nome ci si scrive un mestiere, per quanto assurdo sia scritto, quel mestiere lo si ottiene. Non è detto però che vengano anche le doti che gli si addicono. \\n# ~Speciale: Oggetti Sospetti Comprati e Provati~",
    72486: "\\\"Come usare questo articolo sta al cliente deciderlo.\\\" \\n# ~Parole del Vecchio Bottegaio del Vicolo~",
    72550: "Una maschera misteriosa. Dicono che, per la forza della pietra rossa del saggio che ci è incastonata, a portarla il corpo si ricompone e si rinasce in un'altra razza. \\n# ~Alchimia: Grande Compendio dei Divieti~",
    # ⚠️ :72552 non ha giapponese: l'inglese e' la sola fonte, ed e' un gioco
    #    di parole («race card») che l'italiano tiene per intero.
    72552: "\\\"E piantala di giocarti la carta della razza!\\\" \\n# ~<Jonah> l'avventuriero~",

    # === IL FISCHIETTO E LA GEMMA DELL'EVOLUZIONE =========================
    72620: "Un fischietto che fa un suono che sentono solo i cani. Sembra un fischietto qualunque, ma è un oggetto magico a tutti gli effetti, e a parte i cani non lo sente proprio nessuno, mai, in nessun modo. \\n# ~Dizionario Fantastico di Irva~",
    # ⚠️ :73020 non ha lo spazio prima del `\\n`.
    73020: "È una gemma che, usata su certi compagni che ne abbiano i requisiti, porterebbe un'evoluzione.\\n# ~Dizionario Fantastico di Irva~",

    # === LA BANDIERA E LE DUE STATUE ======================================
    73288: "Una bandiera che i comandanti e simili usano per trasmettere gli ordini. Serve a dare istruzioni ai compagni anche quando la voce non arriva. \\n# ~Comando e Controllo sul Campo di Battaglia~",
    73698: "Una statua che raffigura il dio degli elementi, opera di un artista famoso. Il portamento è pieno di dignità. \\n# ~Catalogo d'Arte di Lumiest~",
    73765: "Una statua che raffigura la dea della ricchezza, opera di un artista famoso. Per farla, l'artista fu costretto a firmare un patto: tre decimi del prezzo di vendita vanno a Yacatect. \\n# ~Catalogo d'Arte di Lumiest~",

    # === LO SCANNER DEGLI EFFETTI =========================================
    # ⚠️ l'inglese riscrive il punto 3) («you lose the Duel») e lascia cadere
    #    il （効果未実装） di testa. Si segue il giapponese.
    # ⚠️ :73828 non ha lo spazio prima del `\\n`.
    73828: "(effetto non attivo) 1) All'inizio del turno peschi dal mazzo fino ad avere cinque carte in mano. 2) Una volta per turno puoi scartare una carta dalla mano e attivarne l'effetto; poi scarti dal mazzo tante carte quanto vale la carta attivata. 3) Alla fine del turno in cui il mazzo resta a zero carte, chi comanda questo oggetto va a 0 HP. Dopo, tutte le carte scartate tornano nel mazzo e si mescola. 4) Per 30 turni puoi saltare il tuo agire. Se riesce, tutte le carte scartate tornano nel mazzo e si mescola; poi scegli un mazzo qualunque fra quelli che puoi usare, e da lì in avanti giochi con quello.\\n# ~Duellanti Ardenti~",
}
