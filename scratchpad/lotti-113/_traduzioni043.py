# -*- coding: utf-8 -*-
"""Le rese del lotto 043 — LE ARMI, la coda: LA CATEGORIA SI CHIUDE.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 043 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa043.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

ⓘ Spaziatura uniforme come nel 042: tutte e trentaquattro le righe hanno lo
spazio prima del `\\n` e la coda `# ~` con lo spazio dopo il cancelletto.

⚠️ I cinque doni degli dei (`:85642`, `:85714`, `:85785`, `:85857`, `:85927`)
   nominano ciascuno il proprio dio, e i nomi sono quelli che i loro indici 3
   usano gia': il dio della terra, la dea della fortuna, la dea della
   guarigione, il dio degli elementi, il dio del raccolto.

⚠️ `:116010` porta ３ a **larghezza intera** nel giapponese. In italiano si
   scrive «tre»: i numeri a due byte sono fra i caratteri che `reimporta`
   rifiuta.
"""

IT = {
    # === I DONI DEGLI DEI E GLI ARTEFATTI DELLA ZONA ALTA ==================
    82945: "Una spada a croce d'argento, enorme e senza ornamenti. A parte un'incisione misteriosa sulla lama non ha decorazione nessuna, e quella fattura, fatta solo per abbattere il nemico e nient'altro, mette perfino una specie di soggezione. \\n# ~Dizionario Fantastico di Irva~",
    84582: "Un'ascia lunga rossa, come fosse imbrattata di sangue. Dicono che il colpo che ne esce passi e sbricioli qualunque cosa. \\n# ~Dizionario Fantastico di Irva~",
    85642: "Un martello enorme e pesante, di aspetto maestoso. Chi lo gira sembra il dio della terra che si mostra in carne e ossa. \\n# ~Dizionario Fantastico di Irva~",
    85714: "Un pugnale ricavato scavando la mica, che fin dai tempi antichi è segno di fortuna. Secondo una versione, la dea della fortuna lo lasciò cadere per sbaglio sulla terra mentre puliva il pesce. \\n# ~Dizionario Fantastico di Irva~",
    85785: "Una lancia sacra senza un'ombra addosso. Basta che tu infilzi il nemico una volta, e ci vedrai un frammento della forza della dea della guarigione. \\n# ~Dizionario Fantastico di Irva~",
    85857: "Un bastone nero ornato di tre specie di pietre preziose. Ciascuna pietra è il simbolo di un elemento, e dicono che facciano crescere di colpo la forza magica di chi lo maneggia. \\n# ~Dizionario Fantastico di Irva~",
    85927: "Fra chi lavora la terra non c'è nessuno che non conosca questa favola. Ai tempi in cui la siccità non finiva e il raccolto non veniva, quella comparve da chissà dove, e poi tutt'intorno si coprì di verde. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ 地獄 e' «l'oltretomba» come nell'indice 3 di quest'arma, e il
    #    giapponese lo ripete tre volte di seguito: si ripete anche in italiano.
    107252: "Una lancia prodigiosa che, si dice, fu forgiata con le fiamme che l'oltretomba manda. Forgiandola, si è bevuta a poco a poco la forza che l'oltretomba dà; e dicono che, a girarla, apra le porte che l'oltretomba tiene chiuse. \\n# ~Dizionario Fantastico di Irva~",

    # === IL BASTONE DELLA FOLLIA, CORPO E BATTUTA =========================
    107324: "Un bastone che, dicono, solo chi è caduto nelle tenebre ha il diritto di impugnare. Dentro ci starebbero chiuse le anime di chi lo ha posseduto prima, e quando colpisce spesso quelle piombano addosso al nemico come un incubo. \\n# ~Dizionario Fantastico di Irva~",
    107326: "\\\"Ho sentito dire che è il bastone che, tanto tempo fa, tenne in mano un mago che voleva la propria rovina. Allora ridevo, e pensavo che uomini sciocchi ci fossero al mondo; adesso invece mi pare quasi di capire come si sentiva. Anche lui avrà perso troppo.\\\" \\n# ~Parole di <Renton> il mago tormentato~",

    107460: "Un randello con attaccata una palla di ferro che pare una luna piena imbrattata di sangue. Sulla sfera, dicono, sta un incantesimo che assorbe lo spirito del nemico e ne rende la forza in fiamme. \\n# ~Dizionario Fantastico di Irva~",

    # === LE ARMI BASE, LA CODA DELLA RACCOLTA =============================
    113386: "Una spada corta che usa un gruppo di spie cresciuto in segreto in un paese straniero: è piuttosto piccola, ma lavorata per stare bene in mano. La lama, dicono, è tinta di nero perché non rifletta la luce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    115521: "Una lancia che da sola permette di combattere in molti modi: taglia, punge e batte. Nei tempi antichi, quando gli uomini non smettevano mai di combattersi, quest'arma la usavano razze diverse, tante quante erano i suoi usi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    115589: "Un'ascia con una lama ancora più grande di quella dell'ascia da battaglia. Ormai pare quasi una spada larga infilata in cima a un palo lungo, ma per via del peso pare che si usi più per schiacciare che per tagliare. Serve anche ad abbattere gli alberi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    115720: "Una spada enorme, fatta perché si maneggi a due mani. Pesa, ma non è affatto un'arma che schiaccia il nemico lasciando fare al peso: taglia bene, ed è fatta per recidere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    115941: "Un bastone di una certa lunghezza. Non ha lame, quindi uccide poco; ma è leggero, e per questo spesso lo si gira in mano o lo si usa come tramite in cui mettere la forza magica. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⚠️ il giapponese scrive ３ a larghezza intera: in italiano «tre».
    116010: "Una lancia pensata all'origine per prendere il pesce. La punta del manico si divide in tre, e questo la rende più facile da mandare a segno; e pare che sia stato studiato anche l'effetto di ritardare la guarigione, con le ferite prese così da vicino. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    116078: "Un martello grande, ricavato da quello del fabbro e lavorato per il combattimento. Dicono che il colpo, calato da un braccio alzato per bene, schiacci qualunque nemico. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    116146: "Un'ascia sviluppata per il combattimento. Anche la lama è fatta piuttosto grande, e questo ne ha aumentato il peso: alla fine bisogna per forza maneggiarla a due mani. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    116215: "Una spada a doppio taglio che usano le bande di predoni che infestano il mare. Perché stia bene in mano anche in battaglia, ha la lama piuttosto piccola e larga di costa, così da poter parare le spade. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    116282: "Una spada lunga che, dicono, i gruppi di guerrieri di un paese straniero preferivano a ogni altra. Ha una curva tutta sua, e dicono che in ognuna stiano chiusi una firma tutta sua e l'anima del fabbro che l'ha battuta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⚠️⚠️ :116982 e :117051 portano lo STESSO INGLESE, byte per byte: quello
    #    del bastone, copiato sulla lancia da chi ha scritto il ramo inglese.
    #    I giapponesi sono diversi, quindi le firme sono diverse e le rese sono
    #    DUE, ciascuna dal proprio giapponese. `_coerenza` si accendera' con
    #    «stesso inglese, rese diverse: 1», ed e' atteso.
    116982: "Un'arma con la punta acuminata in cima a un manico lungo. Ha una struttura semplice e la può usare chiunque, e il manico lungo permette di combattere a mezza distanza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    117051: "Un bastone nato per dare una mano alla magia. A vederlo non lo chiameresti un'arma, eppure, se ci batti con tutta la forza, probabilmente il nemico va giù svenuto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    117119: "Un arnese che serve, di suo, a tagliare l'erba e simili. Sul campo di battaglia lo si usa per mietere teste, e per questo fa paura. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # === GLI ULTIMI ARTEFATTI =============================================
    117460: "Un pugnale fatto con un minerale sconosciuto. È leggerissimo, e dicono che i lampi rapidi della lama sembrino un nastro che si gira in aria. \\n# ~Dizionario Fantastico di Irva~",
    126221: "Una spada lunga che, dicono, stava piantata in silenzio su una collinetta. Quanti nemici avrà macellato quella lama nera? La spada tace e non risponde. \\n# ~Dizionario Fantastico di Irva~",
    126918: "Una falce su cui sono stati stesi strati e strati di incantesimi di rinforzo. Dicevano che rafforzasse la magia di chi la maneggia e lo avvicinasse all'essere supremo, ma è sparita dal mondo da moltissimo tempo. \\n# ~Dizionario Fantastico di Irva~",
    127349: "Un miracolo di lama, di cui si canta che a questo mondo non c'è cosa che non tagli. Come dice la voce, passa qualunque cosa; ma a quel che raccontano, l'unica che non riesce a tagliare è un cibo grigio e pieno di elasticità. \\n# ~Dizionario Fantastico di Irva~",

    # === DIABLOS, CORPO E BATTUTA =========================================
    # ⚠️ 斬られた者 e' «chi viene tagliato»; l'inglese scrive «the cutter»,
    #    cioe' chi taglia, e rovescia la frase.
    127421: "Una spada che incute timore e porta il nome di \\\"demone\\\". Dicono che la sua lama nera scombini non soltanto la mente di chi viene tagliato, ma perfino lo scorrere del tempo. \\n# ~Dizionario Fantastico di Irva~",
    127423: "\\\"Di quell'arma ho sentito parlare. Sarebbe una spada nata da un drago nero che porta sventura, e la sua lama taglierebbe perfino il tempo. Non so se sia vero, ma se lo è mi piacerebbe proprio vederla. Potrebbe essere un'arma degna della mia forza.\\\" \\n# ~Parole di <Loyter> l'eroe cremisi di Zanan~",

    # === LE QUATTRO ARMI CHE CHIUDONO LA CATEGORIA ========================
    130977: "Un'arma semplice, fatta per picchiare. Il modo di farla e quello di usarla sono tutt'e due semplicissimi, e per questo dicono che anche fra chi va all'avventura ci sia chi non la lascia mai. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    131045: "Un'ascia fatta leggera perché si maneggi con una mano sola. Nella fattura si sente ancora forte il lato di ogni giorno, spaccare la legna più che combattere; ma è leggera, e per questo è buona a tutto: si può usare anche come un randello. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    131114: "Una spada corta e leggera, nata presso un clan antico, fatta per maneggiarsi facile anche con una mano sola. La sua forma semplice è arrivata fino a oggi senza cambiare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    131182: "Una spada dalla lama lunga, fatta in generale per tagliare. Dicono che le sue varietà, che sono tantissime, continuino a evolversi ancora adesso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
