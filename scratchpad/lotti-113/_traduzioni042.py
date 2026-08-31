# -*- coding: utf-8 -*-
"""Le rese del lotto 042 — LE ARMI, seconda parte: i cinque «capricci».

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 042 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa042.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

ⓘ A differenza del 041, qui la spaziatura e' **uniforme**: tutte e trentacinque
le righe hanno lo spazio prima del `\\n` e tutte e trentacinque la coda `# ~`
con lo spazio dopo il cancelletto. Controllato con `_scheda034.py 042`.

⚠️⚠️ **DUE FAMIGLIE ATTRAVERSANO I LOTTI, E VANNO SCRITTE UGUALI.**

  1. i **cinque artefatti pesantissimi** (`:75445`, `:77005`, `:77215`,
     `:77285`, `:81606`) portano in giapponese la stessa identica frase, e
     cambia solo l'attributo donato. L'inglese la riscrive **cinque volte in
     modo diverso**; l'italiano no. La forma e' senza genere apposta, perche'
     i cinque oggetti sono un libro, una spada, un'ascia, una falce e un
     bastone: «E' di un peso che un uomo non regge, ma quando comparira' chi sa
     servirsene, quest'arma gli donera' <X>. E, insieme, un pizzico di
     capriccio.»
  2. `:76863` (<Stormbringer>) apre con la **stessa prima frase** di `:51779`
     (<Ravenbrand>), che sta nel **lotto 041**. Copiata parola per parola.
"""

IT = {
    # === LE ARMI BASE ======================================================
    67045: "Una frusta da combattimento, con la punta della corda rinforzata di metallo. In origine la frusta era un arnese per dare dolore più che per uccidere, ma il rinforzo le ha dato la forza di spezzare almeno le ossa. Lo schiocco è il rumore della punta che raggiunge la velocità del suono e batte l'aria: non è il rumore che fa quando colpisce qualcosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
    67113: "Un calzino di fattura robusta che, dicono, un esperto ha disegnato perché servisse anche da arma. È roba di prima qualità: riempilo di sabbia o di monete e giralo con tutta la forza, non perde la forma. Il difetto è che la trama è troppo fitta, quindi dentro si suda e l'odore ci si attacca. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⚠️ l'inglese lascia cadere la frase del 護拳, la guardia sul manico.
    67181: "Un'arma da difesa nata dalla falce, che è un attrezzo da campo. Ha una guardia sul manico perché il contraccolpo del colpo di catena non ti faccia ferire la mano sulla lama. Di solito si rallenta il nemico con la catena, poi ci si avvicina e si colpisce con la falce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # === IL TRIDENTE DEL DIO DELLA DISTRUZIONE, CORPO E BATTUTA ============
    # ⓘ 守護者 e' il guardiano della storia gia' raccontata in `db_card.hsp`:
    #    «decise di proteggere la dea della guarigione fino in fondo».
    67460: "Tanto tempo fa, quando il dio della distruzione assalì la dea della guarigione, il guardiano fece scudo del proprio corpo e la difese fino in fondo dal colpo. Resse l'attacco pur essendo ridotto a brandelli, e alla dea non toccò un graffio; il dio della distruzione ne fu ammirato, gli lasciò quest'arma e se ne andò. \\n# ~Dizionario Fantastico di Irva~",
    67462: "\\\"Attacco e difesa sono le due facce della stessa cosa. Se hai qualcosa da proteggere, devi avere la forza che ci vuole.\\\" \\n# ~Parole del Dio della Distruzione~",

    # ⚠️ l'inglese scrive «larger and more powerful»; il giapponese dice
    #    大型兵器用にした, «la destino' alle armi pesanti». E ホウセンカ sputa
    #    i semi: 種を放つ, che l'inglese perde.
    67530: "Una lama enorme ad alta frequenza, a forma di katana. In origine era un'arma per un uomo solo, ma era difficile da maneggiare; allora il capo dello sviluppo, non sapendo più che pesci pigliare, la fece ancora più grande e la destinò alle armi pesanti. Quando converte il calore in eccesso in proiettili di fuoco e li fa scoppiare, pare una balsamina che sputa i semi. E per via di questo effetto pesa ancora di più. \\n# ~Dizionario Fantastico di Irva~",

    69326: "Una falce la cui lama è luce astrale raccolta in un fascio. Si separa in corrispondenza dei nodi, che paiono ossa, e prende la forma di una frusta a più sezioni: così il colpo diventa flessibile. È il simbolo del ciclo delle rinascite spezzato, del riposo eterno. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ 常闇の眼 nel dizionario e' «l'occhio delle tenebre eterne», non
    #    «Origin of Vice» come lo chiama l'inglese.
    70267: "Un bastone tramandato di generazione in generazione fra gli dei che presiedono alla sapienza. Ha il potere di percepire e registrare in un istante quel che accade in tutto il mondo, ma solo pochissimi dei sanno usarlo. Ha molto a che fare anche con l'occhio delle tenebre eterne, perduto tanto tempo fa. \\n# ~Il Libro della Sapienza~",

    70887: "Un'accetta che racchiude il potere di comandare la gravità. Chiude chi ha colpito dentro una sfera di gravità e lo schiaccia. E anche il colpo in sé, con la gravità addosso, è pesante. \\n# ~Dizionario Fantastico di Irva~",
    70958: "Un'arma a forma di bastone che racchiude la forza della stirpe dei draco. Essendo un bastone non ha una potenza distruttiva particolare, se la confronti con altre armi. Ma si maneggia benissimo, e permette attacchi rapidi e di tecnica. \\n# ~Dizionario Fantastico di Irva~",
    71776: "Una bella spada lunga di luce, fatta usando come oscillatore una pietra che, si dice, viene dalla luna. L'energia in eccesso che produce la converte in onde di luce. \\n# ~Dizionario Fantastico di Irva~",
    73090: "Una lancia fatta con il corno di un unicorno nero. Lungo la spirale della superficie vortica la forza del caos, che scava e passa da parte a parte chi le si oppone. \\n# ~Dizionario Fantastico di Irva~",
    73422: "Uno spadone che, si dice, nacque dentro il fuoco di un dio. Porta nella lama una fiamma sacra, e i non morti corrotti li brucia fino in fondo e li purifica. \\n# ~Dizionario Fantastico di Irva~",
    73492: "È nato da un incrocio andato male. Ha una durezza che non gli serve a niente, e per questo si usa da arma; e visto che la punta è piena di sostanze nutrienti, uno solo è buono due volte. Chissà perché, a tenerlo in mano vengono più colpi critici. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ l'inglese lascia cadere la SECONDA FRASE INTERA: le ossa e gli occhi
    #    della bestia leggendaria, e le migliaia di maghi morti per abbatterla.
    73631: "Un bastone che sacrifica le doti fisiche di chi lo porta per aumentare di molto la forza magica. È fatto con le ossa e gli occhi di una bestia magica leggendaria che, si dice, fu abbattuta a fatica al prezzo di migliaia di vite di maghi. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ il giapponese e' in lingua da televisione (なんということでしょう…
    #    ました), che l'inglese appiattisce in «What a surprise!».
    74030: "Ma guarda un po' che roba. Uno strumento leggendario, per mano di un maestro artigiano, è rinato come arma contundente. Uno sfarzo tale che chi capisce il valore degli strumenti sviene sul posto. \\n# ~Dizionario Fantastico di Irva~",

    # === I CINQUE ARTEFATTI PESANTISSIMI ==================================
    # ⚠️ stessa frase in tutt'e cinque, cambia solo l'attributo donato.
    #    習得 -> apprendimento, 意志 -> volontà, パワー -> forza,
    #    耐久 -> costituzione, 魔力 -> magia (i nomi del dizionario).
    75445: "Un libro enorme. Così spesso che nemmeno un dio riuscirebbe a leggerlo tutto. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una capacità di apprendimento smisurata. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",
    77005: "Una spada a croce, enorme, fatta per dare una morte dolce. Ci sono cose che solo la morte può guarire. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una volontà ferma. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",
    77215: "Un'ascia da battaglia enorme, che distrugge ogni cosa. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una forza smisurata. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",
    77285: "Una falce ricavata dalle ossa di una bestia sotterranea gigantesca. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una costituzione senza fine. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",
    81606: "Un bastone talmente grande da scambiarlo per la statua della coda di un gatto gigantesco. È di un peso che un uomo non regge, ma quando comparirà chi sa servirsene, quest'arma gli donerà una magia senza pari. E, insieme, un pizzico di capriccio. \\n# ~Dizionario Fantastico di Irva~",

    # === GLI ALTRI ARTEFATTI ==============================================
    75784: "Una lama maledetta dalla quale il veleno trasuda senza fine. È un segreto dei ninja, e quasi nessuno ne conosce i particolari. \\n# ~Dizionario Fantastico di Irva~",
    75917: "L'oggetto con cui la dea della guarigione si difende. Serve a bloccare qualcuno senza fargli male. \\n# ~Dizionario Fantastico di Irva~",
    76656: "Un bastoncino che il figlio del dio del sole ha ricavato facendo cristallo della luce. Sembra una spada, e in effetti si usa anche come una spada, ma resta comunque un bastone lungo. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ la prima frase e' COPIATA da `:51779` (<Ravenbrand>, lotto 041): il
    #    giapponese e' identico. Cambia solo la seconda, e li' il giapponese
    #    dice 兄弟剣 dove il 041 diceva 分身.
    76863: "Una spada nera, nata dall'idea di usare un male ancora più grande per scacciare il male. Ne esiste una che si potrebbe dire sua gemella, e dicono che, a stringerle tutt'e due, una per mano, si ottenga una forza capace di distruggere perfino il mondo. \\n# ~Dizionario Fantastico di Irva~",

    # === IL COLTELLO DELLA SORELLA MINORE, CORPO E BATTUTA ================
    77494: "Un coltello da cucina in cui stanno chiusi amore, rabbia e dolore. Taglia via una testa dopo l'altra, e a vederlo viene in mente il fiore della camelia che cade a terra tutto intero, uno dietro l'altro. \\n# ~Dizionario Fantastico di Irva~",
    77496: "\\\"Senti... spostati. Se non ti sposti non posso ammazzarla, no? A quella ladra bisogna pure insegnarglielo, che cosa succede a prendersi la roba degli altri... quindi smettila di difenderla... ti prego. Se no io...!\\\" \\n# ~Parole della Sorella Minore che si Fa Sotto~",

    # ⚠️ 振るうと力が湧いてくる e' «a girarla, ti monta dentro la forza»;
    #    l'inglese inventa «it produces a shockwave of power».
    77706: "La sciabola che usava un eroe a cui avevano affibbiato il marchio di pirata. Per ironia della sorte, adesso è finita in mano a dei banditi veri. A girarla, ti monta dentro la forza. \\n# ~Dizionario Fantastico di Irva~",

    77983: "Una motosega che taglia in modo spaventoso. Potrebbe fare a pezzi perfino un dio. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ ロマンチスト e' «un romantico»; l'inglese scrive «maniac», che e'
    #    un'altra parola e un altro senso.
    78052: "Un'arma che uccide sparando in avanti una lancia a forma di palo, carica di elettricità. È scomodissima da usare, e a sceglierla di gusto ci sarà solo un fedele accanito di Mani o un romantico. \\n# ~Dizionario Fantastico di Irva~",

    78187: "Uno spadone enorme. È talmente grande, spesso, pesante e rozzo che chiamarlo blocco di ferro è più giusto che chiamarlo spada. \\n# ~Dizionario Fantastico di Irva~",

    # === LE ULTIME ARMI BASE ==============================================
    78857: "Un coltellino corto che serve a preparare quel che si mangia. L'uso per cui è fatto è quello di casa, ma la lama è affilata per bene, quindi si potrà usare anche per combattere. \\n# ~I Comprimari della Cucina~",
    80286: "Una spada lunga fuori dall'ordinario, con la lama che splende di luce viva. Come si faccia non si sa proprio, ma a quel che si dice i cavalieri di un altro mondo, quando diventano adulti, se la costruiscono da soli per mostrare quanto valgono. \\n# ~Dizionario Fantastico di Irva~",
    81469: "Una lama speciale, fatta per respingere i draghi. Il suo acciaio luccica in modo inquietante, come fosse bagnato di sangue fresco, e dicono che notte e giorno faccia strage di draghi con colpi tanto affilati da produrre scariche elettriche. \\n# ~Dizionario Fantastico di Irva~",
    81879: "Una falce grande, dal manico lungo. La lama è meno ricurva di quella di un falcetto, ma dicono che, afferrando il manico a due mani e girandolo con slancio, si mietono insieme la voglia di combattere del nemico e i pezzi del suo corpo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
