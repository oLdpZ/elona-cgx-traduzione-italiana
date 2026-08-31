import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :49776
    (49776, 'Water bottles manufactured at the end of the biochemical civilization. It is equipped with an advanced filtration mechanism and can somehow make contaminated water drinkable. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una borraccia costruita alla fine della civiltà biochimica. Monta un filtro di grado avanzato, e anche l'acqua sporca, se ce n'è in quantità, riesce in qualche modo a renderla bevibile. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :49847
    (49847, 'Distorted crystals spilled from Tezcatlipoca. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme caduto da Tezcatlipoca. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :49918
    (49918, 'Distorted crystals found inside the body of the deformed angel. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme trovato nel corpo di un angelo mostruoso. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :49989
    (49989, 'Distorted crystals kept by Zeome. Unlike the shards left behind by ordinary Nefia guardians, this object has no magical power of its own, but it is a powerful catalyst. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cristallo deforme che Zeome teneva in custodia. Somiglia ai frammenti che lasciano i comuni guardiani delle Nefia, ma è tutt'altra cosa. Di suo non ha forza magica, però è un catalizzatore potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50060
    (50060, 'The hand that holds the power of God. The story of the Golden King of Donkey Ears, who once held the same power in his hands, who defeated tragedy with the power of love, is all too well known. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una mano in cui alberga la forza di un dio. È fin troppo nota la storia del re d'oro dalle orecchie d'asino che, avendo un tempo avuto in mano la stessa forza, spezzò la tragedia con la forza dell'amore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50131
    (50131, 'Patrol program composed of photons. It flies around at the speed of light to collect information or, conversely, to spread information. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un programma di pattuglia fatto di fotoni. Vola in giro alla velocità della luce e raccoglie informazioni, oppure al contrario le diffonde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50202
    (50202, "Divine medal of honor. It symbolizes the strength to carry oneself through and the strength to protect what needs to be protected, even to the point of abandoning oneself. It has strong power, but if you don't use it thoughtfully, you will die without being able to protect or carry through anything. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una medaglia divina. Simboleggia due forze: quella di tenere fede a sé stessi fino in fondo e quella di difendere fino in fondo ciò che va difeso, anche a costo di rinunciare a sé. Racchiude un gran potere, ma se non la si usa con giudizio si finisce col morire senza aver difeso né tenuto fede a niente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50271
    (50271, 'A license prepared by God. In modern Irva, marriage is not permitted without first becoming partners. However, if the couple confronts the marriage partner with this, the marriage is possible. Of course, the other party has the right to refuse. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un permesso preparato da un dio. Nell'Irva di oggi non ci si può sposare se prima non si è compagni. Ma sbattendo in faccia questo foglio il matrimonio diventa possibile. Certo, l'altro ha sempre il diritto di dire di no. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50341
    (50341, 'An access key that calls up a floating fortress in spatial submergence. However, it has been modified in some way, with obviously non-standard electronic components attached externally. \\n# ~Irva Fantasy Encyclopedia~'):
        "La chiave d'accesso che richiama la fortezza volante immersa nello spazio. Qualcuno però l'ha modificata: ci sono attaccati fuori dei pezzi elettronici palesemente fuori standard. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50408
    (50408, "Mysterious crystals found inside a Nefia guardian's body. It is said to generate power by compounding with memories. Similar crystals were reportedly found inside the bodies of patients suffering from Nephia Syndrome. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un cristallo misterioso che si trova nel corpo dei guardiani. Dicono che generi forza combinandosi con la memoria. C'è anche un referto di quando fu aperto il corpo di un malato terminale di sindrome di Nefia: dentro gli si stava formando un cristallo uguale. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :50410
    (50410, 'It seems that if the relevant skill is too low, it cannot be converted into a bonus and the skill itself will be gone. There is no such thing as an unnecessary skill, so it seems difficult to utilize. \\n# ~memo of a grave robber~'):
        "Pare che se l'abilità in questione è troppo bassa non si converta in bonus e sparisca del tutto. E siccome abilità inutili non ce ne sono, sfruttarlo sembra difficile. \\n# ~Appunti di un Predone di Rovine~",

    # ---------------------------------------------------------- :50474
    (50474, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. This Potio-man is the self-powered type, and it uses the absorbed magical power efficiently.\\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. Chi lo maneggia lo chiamano pozionista. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che ha una coscienza propria, e la forza magica assorbita la usa con criterio.\\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50540
    (50540, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Potio-man of this model can be synchronized to fire an attached grenade.\\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. Nel tempo, dicono, come proiettili sono stati usati i tappi delle bevande più varie. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo che, se lo si sincronizza, spara una granata montata fuori.\\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50606
    (50606, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Potio-man of this model is equipped with a transparent shield, and raises one's defensive power for a while after firing. \\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. In certe zone lo chiamano anche uomo di sughero. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il tipo con lo scudo mezzo trasparente, pensato per gli scontri a fuoco: dopo il colpo la difesa sale per un po'. \\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50672
    (50672, "Traditional crafts toys. Its wielder is called a Potioner. When mixed with a potion, it absorbs magical power and temporarily increases its power. Its basic power depends on one's grip and marksmanship, and its magical impact can pierce through any armor and even damages MP. Prototype Potioman that has no consideration of holding back power, it is easy to increase its power by grip strength. \\n# ~Battle-Hobby Legend~"):
        "Un pezzo di artigianato tradizionale. I colpi crescono col numero di pozioni usate, ma i tappi dei contenitori fuori dal comune hanno un altro diametro e non vanno. Se ci si mescola una pozione assorbe la forza magica e per un po' si potenzia. La potenza di base dipende dalla forza della presa e dalla mira, e l'urto che porta la magia non lo ferma nessuna armatura: fa danno perfino agli MP. Questo è il primo tipo, che non bada a dosare la forza: con la presa salda la potenza sale in fretta. \\n# ~Cronache del Battle Hobby~",

    # ---------------------------------------------------------- :50746
    (50746, 'Board with various instruments, panels, and LCDs. A high level of information processing capability is required to handle all the functions. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un pannello con sopra strumenti di misura, quadri e schermi a cristalli liquidi. Per usarne bene tutte le funzioni ci vuole una gran capacità di elaborare informazioni. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :50945
    (50945, "Green stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra verde che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di SP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51012
    (51012, "Blue stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra blu che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di MP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51079
    (51079, "Red stone said to have the power of a demon god. Classified as a type of magic stone, the manufacturing process is very different. Magical traps are placed in the user's current location, and the traps are activated by reusing the stone. The activation of the trap is instantaneous and no turn elapses, but it consumes a small amount of SP. \\n#~Irva Fantasy Encyclopedia~"):
        "Una pietra cremisi che, dicono, racchiude la forza di un dio demoniaco. Per classificazione è una pietra magica, ma il modo di farla è tutt'altro. Piazza una trappola magica dove si trova chi la usa, e riusando la pietra la trappola scatta. Lo scatto è immediato e non fa passare il turno, ma consuma un po' di HP. (non implementato) \\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51288
    (51288, 'These are treasures that provide experience, or even knowledge of the skill. In rare cases, some people are incapable of acquiring skills this way due to body rejection? \\n# ~Irva Fantasy Encyclopedia~'):
        "I detriti che lascia chi è diventato guardiano. Ci abita ancora un poco del sapere che la Nefia gli ha dato, delle tecniche di un tempo, dei ricordi del guardiano stesso. Se ne possono assorbire tecniche e sapere, ma insieme entra la memoria di un altro e c'è da uscire di senno. E se li usasse un malato terminale di sindrome di Nefia, perderebbe conoscenza e diventerebbe lui il nuovo guardiano della Nefia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :51289
    (51289, 'It seems that if the relevant skill is too low, it cannot be converted into a bonus and the skill itself will be gone. There is no such thing as an unnecessary skill, so it seems difficult to utilize. \\n# ~memo of a grave robber~'):
        "Un tesoro che, se l'abilità già ce l'hai, ti dà esperienza, e se non ce l'hai te la fa imparare. Pare che di rado ci sia chi per rigetto non riesce a impararle: sarà vero? \\n# ~Appunti di un Predone di Rovine~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :51290
    (51290, '\\"Those who are resistant won\'t be taken in by Nefia and can gather memory fragments to make them stronger. There are loopholes in everything. ...No, wait. What if the original purpose of this item is to concentrate power on those who are resistant?\\" \\n# ~words of <Melochea> the Nefia Researcher~'):
        "\\\"Chi ha resistenza non viene inghiottito dalla Nefia e può farsi forte raccogliendo detriti. Una falla c'è sempre, in ogni cosa. ...No, aspetta. E se lo scopo vero fosse proprio concentrare la forza su chi resiste...?\\\" \\n# ~Parole di <Melochea>, studiosa di rovine~",

    # ---------------------------------------------------------- :51979
    (51979, 'Smoke screen generators have been used and developed by the ninja since ancient times. Older models required a fire to be lit, but modern ones no longer require ignition. When thrown, it deploys a smoke screen to block vision. The smoke screen blocks most long-range attacks, allowing the ninja to escape or surprise the enemy and destroy them individually. Some schools of ninjutsu do not use this method, but instead generate smoke by themselves. \\n# ~100 Secret of the Ninja - Illustrated~'):
        "Un apparecchio che genera cortine di fumo, usato e affinato dai ninja fin dall'antichità. I modelli vecchi andavano accesi, quelli di oggi no. Lanciandolo stende una cortina che toglie la vista. La cortina ferma quasi tutti gli attacchi da lontano, e in quel varco si può fuggire oppure piombare addosso al nemico e farlo fuori uno per volta. Dicono che fra le arti ninja ci sia anche qualche scuola che il fumo se lo fa da sé, senza questo. \\n# ~Illustrato: Cento Segreti del Ninja~",

    # ---------------------------------------------------------- :52045
    (52045, 'Cards issued by the Goddess of Wealth. They are apparently aimed at protecting and fostering merchants and promoting economic activity. Yaca points are added according to shop sales and customer traffic. The maximum amount of points is 100,000, so use them in moderation. \\n#~Merchant Life Starting from a Quitting as a Adventurer~'):
        "La carta che emette la dea della ricchezza. Pare che serva a proteggere e far crescere i mercanti e a dare una spinta all'economia. I YacaPoint si accumulano in base agli incassi del negozio e a quanta gente ci entra. Il tetto è di centomila punti, quindi conviene spenderli ogni tanto. \\n#~Vita da Mercante Dopo l'Avventura~",

    # ---------------------------------------------------------- :52047
    (52047, '\\"You get five times the Yaca points every December! Plan your year-end sales!\\" \\n# Words of the Goddess of Wealth'):
        "\\\"Ogni anno a dicembre i YacaPoint valgono cinque volte tanto! Le vendite di fine anno organizzatele bene!\\\" \\n# ~Parole della Dea del Tesoro~",

    # ---------------------------------------------------------- :52380
    (52380, 'A wooden person made to resemble a humanoid. You can train your weapon skills by using this wooden person as a combatant. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una bambola di legno fatta a somiglianza di una figura umana. Prendendola per avversario ci si allena nelle abilità con le armi. \\n# ~Dizionario Fantastico di Aimwell~",

    # ---------------------------------------------------------- :52382
    (52382, '\\"You\'ve been waiting in that cave for years... for your master who never returned, for years.\\" \\n# ~<Norne> the guide~'):
        "\\\"Tu in quella grotta hai aspettato tutto il tempo... padroni che non tornavano, tanti, per anni e anni.\\\" \\n# ~Parole di <Norne> la guida~",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :52446
    (52446, 'Assorted farming tools. Provides growth acceleration and quality improvement to crops. Selects work methods and creates an environment in which certain varieties grow to their advantage. For this reason, other varieties in the mix will lose the growth competition and become nutrients. Note that the work consumes stamina. \\n# ~Agriculture and its New Possibilities~'):
        "Un assortimento di attrezzi da campo. Fa crescere prima le colture e ne alza la qualità. Si sceglie il modo di lavorare e si prepara il terreno perché una certa varietà cresca avvantaggiata; per questo le altre varietà mescolate perdono la gara e finiscono per farle da concime. Attenzione: il lavoro consuma resistenza. \\n# ~L'Agricoltura e le sue Nuove Possibilità~",

    # ---------------------------------------------------------- :54885
    (54885, 'A reasonably sized branch that for some reason has fallen around. It can start a fire. \\n# ~Survival that Anyone Can Do~'):
        "Un ramo di misura giusta, che chissà come sta lì per terra. Serve ad accendere il fuoco. \\n# ~La Sopravvivenza Alla Portata di Tutti~",

    # ---------------------------------------------------------- :55142
    (55142, "A stabilizing device used to suppress hand shaking and to absorb the recoil received by the shooter and the gun mount. In addition to enabling precise shooting, it also makes it possible to fire with all one's might without worrying about the recoil. Once the automatic weapon is stuck in the ground, it is released after a certain period of time. Note that you cannot escape during this time. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un fermo che tiene ferma la mano e scarica il rinculo che prendono il tiratore e l'affusto. Rende possibile il tiro di precisione, e permette anche di sparare a più non posso senza badare al rinculo. Si pianta a terra da sé, e dopo un certo tempo si sgancia. Attenzione: nel frattempo non si può scappare. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :55481
    (55481, "Fragments that shine suspiciously to incite desire. Because it is so beautiful, it is sometimes used as a substitute for jewelry. There are rumors that it gives the user the magical power to manipulate traps, and in return, it eats away at one's life... but no one believes it. There is a legend that a long time ago, a demonic god attempting to destroy humanity was defeated and scattered into red fragments, hence the name. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un frammento che brilla in modo torbido, come per attizzare il desiderio. È abbastanza bello da servire al posto di una gemma. Gira anche la voce che dia a chi lo usa la forza magica di manovrare le trappole, e che in cambio gli roda la vita... ma non ci crede nessuno. C'è una leggenda per cui, tanto tempo fa, un dio demoniaco che voleva distruggere gli uomini fu sconfitto e si sparse in schegge rosse: di lì gli viene il nome. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :56603
    (56603, "Legendary ear picks that change size according to the user's thoughts. Whether you are a fairy or a giant, you only need one of these, but you will lose control of it if you are thinking about the wrong thing. If you master the use of this masterpiece, you can remove all the earwax at once, so you just have to train yourself. The fluffy thing attached to the end is artificial kesalanpatharan, which will die if it is not allowed to rest slowly after use. \\n# ~Irva Fantasy Encyclopedia~"):
        "Il leggendario nettaorecchie che cambia misura secondo il pensiero di chi lo usa. Che tu sia una fata o un gigante ne basta uno, ma se pensi a vanvera ti sfugge di mano. Con la pratica si arriva a cavare tutto il cerume in un colpo solo: è un pezzo pregiato, e non resta che allenarsi. Il batuffolo in punta è un kesaranpasaran artificiale, e dopo l'uso, se non lo si lascia riposare con calma, muore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :57063
    (57063, "A large Christmas cake, sold at grocery stores in December, but sometimes left unsold. It's so big that everyone can eat a whole lot of it. Of course, you can have it all to yourself, but that's wasteful; in December, you can develop the art of faith and bring good luck by eating it. \\n# ~North Tyris Travels, Winter Edition~"):
        "Un dolce enorme per il Natale. A dicembre le mercerie cominciano a venderlo, ma qualcuno resta invenduto. È grande, e ci si sazia tutti insieme. Certo, uno può anche tenerselo per sé, ma che tristezza. A dicembre fa crescere l'abilità Fede e porta anche fortuna. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :57645
    (57645, "Plushie of Yacatect holding a goose. It is said to be manufactured at the God's official factory. When gold coins are inserted, it speaks and moves its wings. The gold coins are invested by Yacatect, and generate interest at a rate of 10% per 100 days. In exchange for the high interest rate, the coins cannot be taken out until the 100th day, and after that, the interest will not increase unless additional deposits are made. And when you take it out, a gold coin comes out of its butt. The goose's butt, of course. \\n# ~Must Watch! Everything About Savings and Asset Management~"):
        "Un pupazzo di Yacatect che tiene in braccio un'oca. Pare che lo facciano in una fabbrica ufficiale degli dei. Se ci metti dentro monete d'oro, muove le ali e parla. Le monete le fa fruttare Yacatect: non al decimo giorno, ma al centesimo... un decimo di interesse ogni cento giorni circa. In cambio del tasso alto non si può né mettere né togliere fino al centesimo giorno, e dopo gli interessi non crescono se non si versa altro. E quando le tiri fuori, le monete escono dal sedere. Dell'oca, s'intende. \\n# ~Da Vedere! Tutto sul Risparmio e sugli Investimenti~",

    # ---------------------------------------------------------- :58526
    (58526, 'Bloodstained kodachi, a small dagger. It contains the thoughts of warriors who committed seppuku (ritual suicide) and died with an apology, and when held, the blade will naturally aim at your stomach. When used to apologize, it is reputed to convey one\'s true intentions to the other party. It has much more apologetic power than the \\"Kneeling on the Ground\\" method, and even enemies will let you off the hook for a while. If treated immediately, it will not kill you. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada corta insanguinata. Ci resta addosso il pensiero dei guerrieri che se ne sono andati col seppuku, chiedendo scusa, e a tenerla in mano la lama va da sola verso la pancia. Dicono che usarla per scusarsi faccia arrivare all'altro quanto sei serio. Come forza di scusa vale molto più di un inchino a terra, e perfino chi ti è nemico ti lascia in pace per un po'. Se ci si medica subito non si muore. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59523
    (59523, 'Treasure that manipulates the dragon vein leading to Nefia and changes the difficulty level of Nefia. Designed to adjust to the growth of the decisive factor candidate. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma che manovra la vena del drago che porta alle Nefia e ne cambia la difficoltà. Serve a regolarla man mano che cresce chi è candidato a Fattore Decisivo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59658
    (59658, 'A piece of shattered star. They emit a mysterious deep blue light. They are just dust at the beginning, and eventually they will become the foundation of another star. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una scheggia di stella che si è spezzata non reggendo più a esistere. Manda una luce azzurra e cupa, misteriosa. C'è chi la tratta da scarto, ma prima o poi, girando di mano in mano, diventa la base di un'altra stella. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59926
    (59926, "Forbidden device in the era of biochemical civilization. It forcibly extracts the constituent materials from the subject, cultivates them at high speed, and creates a duplicate human being based on the scan data. Since there are no dedicated material transfer facilities left today, the human is reduced to a lump of flesh with no life in it, and the device itself is practically disposable. It is still used by some enthusiasts as a fabricator. Be careful not to use it without the person's permission, as it will make them angry. \\n# ~The Yowyn Book of Secrt Knowledge!~"):
        "L'apparecchio proibito dell'età della civiltà biochimica. Strappa a forza dal soggetto la materia che lo compone, la fa crescere in fretta e, sui dati di una scansione in tre dimensioni, ne cava una copia umana. Oggi gli impianti che trasferivano la materia non ci sono più, quindi ne esce solo un pezzo di carne senza vita dentro, e l'apparecchio stesso è di fatto usa e getta. Con tutto ciò, fra certi appassionati va come macchina per statuette. Attenzione: se lo usi su qualcuno senza il suo permesso, si arrabbia. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :60063
    (60063, 'A collection of disposable abrasives, repair materials, and crafting tools. Comes with instructions. Sold in small quantities by a small number of hill people. Repairing invisible minor damages and misalignments to maximize the performance of the armor. As expected, heavy rust and the like cannot be helped, and we will need some other method. \\n# ~Choosing the Best Tools for the Best Craftsmen~'):
        "Un insieme di paste abrasive usa e getta, materiali da riparo e attrezzi da lavoro fine. Con le istruzioni. Lo vende in piccola quantità un pugno di gente delle colline. Ripara le rotture e gli scarti minimi, quelli che l'occhio non vede, e tira fuori il meglio da armi e armature. Contro una ruggine forte non c'è niente da fare: meglio cercare un'altra strada. \\n# ~Scegliere Bene gli Attrezzi da Artigiano~",

    # ---------------------------------------------------------- :60649
    (60649, 'A cylinder that is sometimes found in archaeological sites along with a special gunpowder ball. Because it does not emphasize killing power, and it can only be shot straight up, experts believe that it may have been a signal bullet in those days. Because the explosion is quite beautiful, it is sometimes used as an ornamental object during festivals in recent years. \\n# ~Mystery of the Ancient Tools!~'):
        "Un tubo che ogni tanto si trova nelle rovine insieme alle sue palle di polvere. Visto che non punta a ferire e che spara solo dritto in alto, gli esperti pensano fosse un razzo di segnale dell'epoca. Lo scoppio è piuttosto bello, e negli ultimi anni lo si usa alle feste per far spettacolo. \\n# ~All'Inseguimento del Mistero degli Arnesi Antichi!~",

    # ---------------------------------------------------------- :60914
    (60914, 'A variant of the smoking pipe. In contrast to the pipe, the smoke is inhaled in a single breath without the use of flavoring. It contains ingredients thats beneficial to the skin, and activate brain cells, and make it possible to tolerate light sleepiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Una variante della pipa da fumo. Al contrario della pipa, il fumo si tira tutto in un fiato, senza aromi. Contiene sostanze che fanno crescere l'attributo Carisma, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :60980
    (60980, 'Wooden smoking utensil. Tobacco leaves are chopped and packed, and then blended with herbs and other flavoring agents. Compared to paper cigars, it is better suited for slowing down and savoring tobacco. It contains ingredients that help grow mastery, activates brain cells, and makes light drowsiness tolerable. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Un attrezzo da fumo di legno. Ci si trita e ci si pigia dentro la foglia di tabacco, e ci si mescola per gusto un aroma di erbe. Rispetto alla sigaretta è fatta per gustare il tabacco con calma. Contiene sostanze che fanno crescere l'attributo Apprendimento, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61046
    (61046, 'Tobacco leaf rolled into a cylindrical shape. Originally, the tip is cut off with a knife, but for those who are lazy, it has been processed so that it can be cut by hand. In addition to containing ingredients that help develop dexterity, it also activates brain cells and makes it possible to tolerate light sleepiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Foglia di tabacco arrotolata a tubo. In origine la punta si taglia con una lama, ma per chi ha poca voglia l'hanno lavorata in modo da poterla staccare a mano. Contiene sostanze che fanno crescere l'attributo Destrezza, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

    # ---------------------------------------------------------- :61112
    (61112, 'A tobacco leaf is chopped and rolled up in paper. It has an igniter and can be ignited without any particular ignition device. It contains ingredients that grow the senses, activate brain cells, and make it possible to tolerate light drowsiness. However, there is a risk of addiction, so use in moderation. \\n# ~Sickly Taste of Smoke~'):
        "Foglia di tabacco tritata e arrotolata nella carta. Ha già l'innesco, e si accende anche senza un accendino. Contiene sostanze che fanno crescere l'attributo Percezione, e in più risveglia le cellule del cervello, così si regge un po' di sonnolenza. Attento però: c'è il rischio di prenderci il vizio, quindi con moderazione. \\n# ~Il Sapore del Fumo che Dà Dipendenza~",

# 39 voci, 0 ambigue
}
