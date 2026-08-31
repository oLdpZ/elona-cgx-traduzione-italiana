# -*- coding: utf-8 -*-
"""Le rese del lotto 034 — gli ATTREZZI, seconda parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 034 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa034.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ La spaziatura prima del `\\n` non e' uniforme: `:50474` e `:50540` non hanno
lo spazio, tutte le altre si'. Ogni riga copia il suo.
⚠️ `:52047` e' l'unica fonte che l'inglese scrive **senza tilde**
(`# Words of the Goddess of Wealth`): il `#` e il suo spazio si conservano,
le tilde tornano perche' il giapponese ce le ha. Vedi `testa034.py`.
"""

IT = {
    # === LA BORRACCIA ======================================================
    49776: "Una borraccia costruita alla fine della civiltà biochimica. Monta un filtro di grado avanzato, e anche l'acqua sporca, se ce n'è in quantità, riesce in qualche modo a renderla bevibile. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === I TRE FRAMMENTI DI CATALIZZATORE =================================
    # ⚠️ famiglia: stesse tre frasi finali, cambia solo da dove viene il
    #    cristallo. Le rese cambiano solo li'.
    49847: "Un cristallo deforme caduto da Tezcatlipoca. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",
    49918: "Un cristallo deforme trovato nel corpo di un angelo mostruoso. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",
    49989: "Un cristallo deforme che Zeome teneva in custodia. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # === I SETTE OGGETTI DIVINI ===========================================
    50060: "Una mano in cui alberga la forza di un dio. È fin troppo nota la storia del re d'oro dalle orecchie d'asino che, avendo un tempo avuto in mano la stessa forza, spezzò la tragedia con la forza dell'amore. \\n# ~Dizionario Fantastico di Irva~",
    50131: "Un programma di pattuglia fatto di fotoni. Vola in giro alla velocità della luce e raccoglie informazioni, oppure al contrario le diffonde. \\n# ~Dizionario Fantastico di Irva~",
    50202: "Una medaglia divina. Simboleggia due forze: quella di tenere fede a sé stessi fino in fondo e quella di difendere fino in fondo ciò che va difeso, anche a costo di rinunciare a sé. Racchiude un gran potere, ma se non la si usa con giudizio si finisce col morire senza aver difeso né tenuto fede a niente. \\n# ~Dizionario Fantastico di Irva~",
    50271: "Un permesso preparato da un dio. Nell'Irva di oggi non ci si può sposare se prima non si è compagni. Ma sbattendo in faccia questo foglio il matrimonio diventa possibile. Certo, l'altro ha sempre il diritto di dire di no. \\n# ~Dizionario Fantastico di Irva~",
    50341: "La chiave d'accesso che richiama la fortezza volante immersa nello spazio. Qualcuno però l'ha modificata: ci sono attaccati fuori dei pezzi elettronici palesemente fuori standard. \\n# ~Dizionario Fantastico di Irva~",

    # === IL CONVERTITORE DI MEMORIA =======================================
    50408: "Un cristallo misterioso che si trova nel corpo dei guardiani. Dicono che generi forza combinandosi con la memoria. C'è anche un referto di quando fu aperto il corpo di un malato terminale di sindrome di Nefia: dentro gli si stava formando un cristallo uguale. \\n# ~Dizionario Fantastico di Irva~",
    # ⚠️ :50410 e' l'unica riga del lotto SENZA giapponese: l'inglese e' la
    #    sola fonte, e qui e' quello giusto (parla del convertitore). La
    #    riga gemella :51289 dice tutt'altro, e il perche' sta in testa034.
    50410: "Pare che se l'abilità in questione è troppo bassa non si converta in bonus e sparisca del tutto. E siccome abilità inutili non ce ne sono, sfruttarlo sembra difficile. \\n# ~Appunti di un Predone di Rovine~",

    # === I QUATTRO POTIO-MAN ==============================================
    # ⚠️ l'inglese appiattisce in «Its wielder is called a Potioner» quattro
    #    seconde frasi DIVERSE. Si segue il giapponese: vedi testa034.py.
    # ⚠️ :50474 e :50540 non hanno lo spazio prima del `\\n`.
    50474: "Un pezzo di artigianato tradizionale. Chi lo maneggia lo chiamano pozionista. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che ha una coscienza propria, e la forza magica assorbita la usa con criterio.\\n# ~Cronache del Battle Hobby~",
    50540: "Un pezzo di artigianato tradizionale. Nel tempo, dicono, come proiettili sono stati usati i tappi delle bevande più varie. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che, se lo si sincronizza, spara una granata montata fuori.\\n# ~Cronache del Battle Hobby~",
    50606: "Un pezzo di artigianato tradizionale. In certe zone lo chiamano anche uomo di sughero. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo con lo scudo mezzo trasparente, pensato per gli scontri a fuoco: dopo il colpo la difesa sale per un po'. \\n# ~Cronache del Battle Hobby~",
    50672: "Un pezzo di artigianato tradizionale. I colpi crescono col numero di pozioni usate, ma i tappi dei contenitori fuori dal comune hanno un altro diametro e non vanno. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il primo tipo, che non bada a dosare la forza: con la presa salda la potenza sale in fretta. \\n# ~Cronache del Battle Hobby~",

    # === IL PANNELLO DI COMANDO ===========================================
    50746: "Un pannello con sopra strumenti di misura, quadri e schermi a cristalli liquidi. Per usarne bene tutte le funzioni ci vuole una gran capacità di elaborare informazioni. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === I TRE GLOBI OSCURI ===============================================
    # ⚠️ la resa e' modellata sul fratello bianco :45481 (lotto 033).
    # ⚠️ l'inglese scrive «SP» in tutt'e tre: il giapponese dice SP, MP, HP.
    # ⚠️ la coda qui e' `#~`, senza lo spazio.
    50945: "Una pietra verde che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di SP. (non implementato) \\n#~Dizionario Fantastico di Irva~",
    51012: "Una pietra blu che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di MP. (non implementato) \\n#~Dizionario Fantastico di Irva~",
    51079: "Una pietra cremisi che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di HP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # === I DETRITI (le tre righe di uno stesso oggetto) ====================
    # ⚠️⚠️ l'inglese di :51288 e :51289 e' SLITTATO di una posizione: quello di
    #    :51288 e' la traduzione del giapponese di :51289, e quello di :51289
    #    e' la memoria che appartiene a :50410. Si segue il giapponese.
    51288: "I detriti che lascia chi è diventato guardiano. Ci abita ancora un poco del sapere che la Nefia gli ha dato, delle tecniche di un tempo, dei ricordi del guardiano stesso. Se ne possono assorbire tecniche e sapere, ma insieme entra la memoria di un altro e c'è da uscire di senno. E se li usasse un malato terminale di sindrome di Nefia, perderebbe conoscenza e diventerebbe lui il nuovo guardiano della Nefia. \\n# ~Dizionario Fantastico di Irva~",
    51289: "Un tesoro che, se l'abilità già ce l'hai, ti dà esperienza, e se non ce l'hai te la fa imparare. Pare che di rado ci sia chi per rigetto non riesce a impararle: sarà vero? \\n# ~Appunti di un Predone di Rovine~",
    51290: "\\\"Chi ha resistenza non viene inghiottito dalla Nefia e può farsi forte raccogliendo detriti. Una falla c'è sempre, in ogni cosa. ...No, aspetta. E se lo scopo vero fosse proprio concentrare la forza su chi resiste...?\\\" \\n# ~Parole di <Melochea>, studiosa di rovine~",

    # === IL KEMURIDAMA ====================================================
    51979: "Un apparecchio che genera cortine di fumo, usato e affinato dai ninja fin dall'antichità. I modelli vecchi andavano accesi, quelli di oggi no. Lanciandolo stende una cortina che toglie la vista. La cortina ferma quasi tutti gli attacchi da lontano, e in quel varco si può fuggire oppure piombare addosso al nemico e farlo fuori uno per volta. Dicono che fra le arti ninja ci sia anche qualche scuola che il fumo se lo fa da sé, senza questo. \\n# ~Illustrato: Cento Segreti del Ninja~",

    # === LA CARTA YACAPOINT ===============================================
    52045: "La carta che emette la dea della ricchezza. Pare che serva a proteggere e far crescere i mercanti e a dare una spinta all'economia. I YacaPoint si accumulano in base agli incassi del negozio e a quanta gente ci entra. Il tetto è di centomila punti, quindi conviene spenderli ogni tanto. \\n#~Vita da Mercante Dopo l'Avventura~",
    52047: "\\\"Ogni anno a dicembre i YacaPoint valgono cinque volte tanto! Le vendite di fine anno organizzatele bene!\\\" \\n# ~Parole della Dea del Tesoro~",

    # === IL MOKU-JIN ======================================================
    # ⚠️ la fonte e' il Dizionario di AIMWELL, non di Irva: l'inglese
    #    appiattisce イムウエル su イルヴァ. Vedi testa034.py.
    52380: "Una bambola di legno fatta a somiglianza di una figura umana. Prendendola per avversario ci si allena nelle abilità con le armi. \\n# ~Dizionario Fantastico di Aimwell~",
    52382: "\\\"Tu in quella grotta hai aspettato tutto il tempo... padroni che non tornavano, tanti, per anni e anni.\\\" \\n# ~Parole di <Norne> la guida~",

    # === GLI ATTREZZI PER LE COLTURE ======================================
    52446: "Un assortimento di attrezzi da campo. Fa crescere prima le colture e ne alza la qualità. Si sceglie il modo di lavorare e si prepara il terreno perché una certa varietà cresca avvantaggiata; per questo le altre varietà mescolate perdono la gara e finiscono per farle da concime. Attenzione: il lavoro consuma resistenza. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",

    # === IL RAMETTO =======================================================
    54885: "Un ramo di misura giusta, che chissà come sta lì per terra. Serve ad accendere il fuoco. \\n# ~La Sopravvivenza Alla Portata di Tutti~",

    # === L'ANCORA DI STABILITÀ ============================================
    55142: "Un fermo che tiene ferma la mano e scarica il rinculo che prendono il tiratore e l'affusto. Rende possibile il tiro di precisione, e permette anche di sparare a più non posso senza badare al rinculo. Si pianta a terra da sé, e dopo un certo tempo si sgancia. Attenzione: nel frattempo non si può scappare. \\n# ~Dizionario Fantastico di Irva~",

    # === IL FRAMMENTO DI DEMONE ===========================================
    55481: "Un frammento che brilla in modo torbido, come per attizzare il desiderio. È abbastanza bello da servire al posto di una gemma. Gira anche la voce che dia a chi lo usa la forza magica di manovrare le trappole, e che in cambio gli roda la vita... ma non ci crede nessuno. C'è una leggenda per cui, tanto tempo fa, un dio demoniaco che voleva distruggere gli uomini fu sconfitto e si sparse in schegge rosse: di lì gli viene il nome. \\n# ~Dizionario Fantastico di Irva~",

    # === IL NYOI MIMIKAKI =================================================
    56603: "Il leggendario nettaorecchie che cambia misura secondo il pensiero di chi lo usa. Che tu sia una fata o un gigante ne basta uno, ma se pensi a vanvera ti sfugge di mano. Con la pratica si arriva a cavare tutto il cerume in un colpo solo: è un pezzo pregiato, e non resta che allenarsi. Il batuffolo in punta è un kesaranpasaran artificiale, e dopo l'uso, se non lo si lascia riposare con calma, muore. \\n# ~Dizionario Fantastico di Irva~",

    # === IL SET DI DOLCI NATALIZI =========================================
    57063: "Un dolce enorme per il Natale. A dicembre le mercerie cominciano a venderlo, ma qualcuno resta invenduto. È grande, e ci si sazia tutti insieme. Certo, uno può anche tenerselo per sé, ma che tristezza. A dicembre fa crescere l'abilità Fede e porta anche fortuna. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # === IL SALVADANAIO DI YACATECT =======================================
    57645: "Un pupazzo di Yacatect che tiene in braccio un'oca. Pare che lo facciano in una fabbrica ufficiale degli dei. Se ci metti dentro monete d'oro, muove le ali e parla. Le monete le fa fruttare Yacatect: non al decimo giorno, ma al centesimo... un decimo di interesse ogni cento giorni circa. In cambio del tasso alto non si può né mettere né togliere fino al centesimo giorno, e dopo gli interessi non crescono se non si versa altro. E quando le tiri fuori, le monete escono dal sedere. Dell'oca, s'intende. \\n# ~Da Vedere! Tutto sul Risparmio e sugli Investimenti~",

    # === HARAKIRI =========================================================
    58526: "Una spada corta insanguinata. Ci resta addosso il pensiero dei guerrieri che se ne sono andati col seppuku, chiedendo scusa, e a tenerla in mano la lama va da sola verso la pancia. Dicono che usarla per scusarsi faccia arrivare all'altro quanto sei serio. Come forza di scusa vale molto più di un inchino a terra, e perfino chi ti è nemico ti lascia in pace per un po'. Se ci si medica subito non si muore. \\n# ~Dizionario Fantastico di Irva~",

    # === IL CUORE DEL CREPUSCOLO ==========================================
    59523: "Una gemma che manovra la vena del drago che porta alle Nefia e ne cambia la difficoltà. Serve a regolarla man mano che cresce chi è candidato a Fattore Decisivo. \\n# ~Dizionario Fantastico di Irva~",

    # === LA POLVERE DI STELLE =============================================
    59658: "Una scheggia di stella che si è spezzata non reggendo più a esistere. Manda una luce azzurra e cupa, misteriosa. C'è chi la tratta da scarto, ma prima o poi, girando di mano in mano, diventa la base di un'altra stella. \\n# ~Dizionario Fantastico di Irva~",

    # === LA BIO-STAMPANTE =================================================
    59926: "L'apparecchio proibito dell'età della civiltà biochimica. Strappa a forza dal soggetto la materia che lo compone, la fa crescere in fretta e, sui dati di una scansione in tre dimensioni, ne cava una copia umana. Oggi gli impianti che trasferivano la materia non ci sono più, quindi ne esce solo un pezzo di carne senza vita dentro, e l'apparecchio stesso è di fatto usa e getta. Con tutto ciò, fra certi appassionati va come macchina per statuette. Attenzione: se lo usi su qualcuno senza il suo permesso, si arrabbia. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # === IL KIT DI RIPARAZIONE DI PREGIO ==================================
    60063: "Un insieme di paste abrasive usa e getta, materiali da riparo e attrezzi da lavoro fine. Con le istruzioni. Lo vende in piccola quantità un pugno di gente delle colline. Ripara le rotture e gli scarti minimi, quelli che l'occhio non vede, e tira fuori il meglio da armi e armature. Contro una ruggine forte non c'è niente da fare: meglio cercare un'altra strada. \\n# ~Scegliere Bene gli Attrezzi da Artigiano~",

    # === HANABI ===========================================================
    60649: "Un tubo che ogni tanto si trova nelle rovine insieme alle sue palle di polvere. Visto che non punta a ferire e che spara solo dritto in alto, gli esperti pensano fosse un razzo di segnale dell'epoca. Lo scoppio è piuttosto bello, e negli ultimi anni lo si usa alle feste per far spettacolo. \\n# ~All'Inseguimento del Mistero degli Arnesi Antichi!~",

    # === I QUATTRO OGGETTI DA FUMO ========================================
    # ⚠️ famiglia: cambia solo la prima parte e l'attributo che cresce.
    # ⚠️ l'inglese del kiseru dice «beneficial to the skin»: il giapponese
    #    dice 魅力, il Carisma. Si segue il giapponese.
    60914: "Una variante della pipa da fumo. Al contrario della pipa, il fumo si tira tutto in un fiato, senza aromi. Contiene sostanze che fanno crescere l'attributo Carisma, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",
    60980: "Un attrezzo da fumo di legno. Ci si trita e ci si pigia dentro la foglia di tabacco, e ci si mescola per gusto un aroma di erbe. Rispetto alla sigaretta è fatta per gustare il tabacco con calma. Contiene sostanze che fanno crescere l'attributo Apprendimento, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",
    61046: "Foglia di tabacco arrotolata a tubo. In origine la punta si taglia con una lama, ma per chi ha poca voglia l'hanno lavorata in modo da poterla staccare a mano. Contiene sostanze che fanno crescere l'attributo Destrezza, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",
    61112: "Foglia di tabacco tritata e arrotolata nella carta. Ha già l'innesco, e si accende anche senza un accendino. Contiene sostanze che fanno crescere l'attributo Percezione, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",
}
