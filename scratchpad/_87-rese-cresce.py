# -*- coding: utf-8 -*-
"""Le rese di CRESCE, docente del corso sugli oggetti (chat.hsp :14099-:14240),
seconda dei quattro conferenzieri del seminario.

Perimetro: 71 firme dentro, **70 da fare**, zona chiusa (nessuna occorrenza
fuori). La settantunesima e' `...` (`:14171`), gia' resa e in `invariati.md`.

REGISTRO. Cresce Lucan parla in forma femminile e briosa (わ / のよ / かしら),
da' del tu alla classe e ci scherza sopra; a `:14213`, alla domanda sul suo
ragazzo, minaccia di ammazzare. E' donna e il dizionario lo fissa — «<Cresce>
la docente» (`db_creature.hsp:54981`) — quindi puo' parlare di se' al
femminile; il GIOCATORE resta senza genere. ⚠️ Il soprannome れっしぇー
l'inglese lo butta («call me Cresce»), e le due voci di menu che lo usano
(`:14134`, `:14146`) dicono «Cresce»: si segue l'inglese, come per «Ajira».
Vedi [[_87-rese-ajetalio]] per la famiglia dei quattro corsi.

LESSICO — quasi tutto e' un nome di oggetto o di stato, e sta gia' in
dizionario. Le pergamene (`db_item.hsp`): identificazione, cambio di
materiale, materiale superiore, mappa magica, individuazione degli oggetti,
ritorno, purificazione, potenziamento dell'arma / dell'armatura, meraviglia,
creazione di materiali, oracolo, crescita, acquisizione di attributi,
pergamena volante, maledizione, ricarica. Le pozioni: cura della corruzione,
potenziale, declino, evoluzione, sangue di Ermes, acceleratore, liquido
antiacido, liquido ignifugo. Le bacchette: creazione di muri, teletrasporto,
mutamento di creatura, identificazione, dominio. Gli oggetti: guinzaglio,
stetoscopio, bandiera di comando, fischietto, disco musicale (`text.hsp:2179`),
statuetta, rifugio, coperta ignifuga, coperta termica, specchio
quadridimensionale, lente dell'intuito, set da barbecue, letto della felicita',
kit di materiali, vaso della fusione, scaffale delle pozioni, libreria,
calzini, anello della velocita', mutandine, anello dell'aurora, mantello di
Vindale, stivali delle sette leghe, cappello da fata, anello e amuleto
nuziale. Le abilita' (`skill.hsp`): Dispositivi magici, Sollevamento pesi,
Alchimia, Falegnameria, Sartoria, Oreficeria, Ingegneria genetica,
Individuazione, Pesca, Scavo, Giardinaggio, Analisi (自然鑑定, «Sense
Quality»), Ricarica e Estrai carica. Gli stati: «con benedizione» / «con
maledizione» (`text.hsp:182`-`:183`), «acqua benedetta» (`action.hsp:1402`),
e i quattro pesi di `_burden` (`text.hsp:66`): **Fardello, Fardello!,
Sovraccarico, Sovraccarico!**. Il [Non posare] e' `command.hsp:14087`.

⭐⭐ **LA LEZIONE DEL LOTTO: a `:14124` il giapponese descrive una schermata
che il giocatore non vedra' mai.** Elenca i segni che marcano la qualita' —
☆ e 『』 per il miracolo, ☆ e 《》 per il神器, ★ e 《》 per il speciale — ma
quelli sono i segni del ramo GIAPPONESE. `item_func.hsp:1786`-`:1797` mostra
che nel ramo inglese, che e' quello su cui si costruisce l'italiano, il
miracolo prende `<...>` e tutto il resto `{...}`: esattamente quel che dice
l'inglese. 💡 *Il giudice non e' la lingua piu' ricca, e' il codice del ramo
che si compila.*

⚠️ LE DEROGHE DICHIARATE

1. **`:14124`** — i **nomi delle sei classi** si prendono dall'interfaccia e
   non dall'inglese di questa riga: `_quality` (`text.hsp:106`) dice scadente,
   comune, eccellente, eccezionale, celestiale, speciale, mentre qui l'inglese
   scrive «bad, normal, great, miracle, godly, unique». E' la regola del
   tutorial, che copia i nomi che il giocatore legge altrove.
2. **`:14207` e `:14208`** — l'inglese ha i due contenuti **scambiati**
   rispetto al giapponese: la riga del prezzo dice quel che il giapponese dice
   nella riga dopo (+6 con le pergamene, +10 in armeria) e viceversa. Lette in
   fila le due dicono tutto lo stesso, quindi si segue l'inglese riga per
   riga; ma il conto delle righe di finestra fra i due rami, li', non vale
   niente (e' la 85a, `:2184`).
3. **`:14108`** — l'inglese riscrive: dove il giapponese dice che nei piani
   oltre il primo c'e' sempre un mucchio di monete d'oro, l'inglese dice che
   piu' la Nefia e' pericolosa piu' vale il tesoro. Non si perde niente: il
   mucchio di monete lo dice gia' Ajetalio a `:14033`.
4. **`:14167`** — l'inglese **aggiunge** quel che il giapponese non dice (il
   set da barbecue e il letto della felicita' come i migliori della loro
   famiglia, e il tasto x per leggerne il rango). Si tiene: sono istruzioni.
5. **`:14119`, `:14120`** — l'inglese sposta di una riga la pergamena di
   purificazione che pulisce tutto lo zaino. Si segue l'inglese riga per riga.
6. **`:14151`, `:14150`** — 素材 e マテリアル in italiano sono la stessa
   parola. L'inglese le distingue («equipment materials» / «crafting
   materials») e l'italiano fa lo stesso: «il materiale dell'equipaggiamento»
   contro «i materiali da lavorazione», che e' la lista del tasto m.
"""

RESE = {}

# ============ primo incontro: gli oggetti da procurarsi ============

RESE[14103] = ("Sono Cresce Lucan, e tengo il corso sugli oggetti. Chiamatemi pure "
               "Cresce!")
RESE[14104] = ("Chi ha appena cominciato ad andare all'avventura non sa quali oggetti "
               "contino e quali no. Quindi adesso vi spiego in breve che cosa serve "
               "procurarsi.")
RESE[14105] = ("Per prima cosa ti servono un guinzaglio, uno stetoscopio, una bandiera di "
               "comando e un fischietto. Si comprano dai venditori di cianfrusaglie, o ogni "
               "tanto si trovano nei labirinti.")
RESE[14106] = ("Dischi musicali, carte e statuette in combattimento non servono a niente, "
               "ma un giorno potrebbero servirti: vendi solo i doppioni.")
RESE[14107] = ("Gli effetti di un oggetto si scoprono identificandolo. Usa una magia, una "
               "pergamena o una bacchetta di identificazione, oppure fatti identificare la "
               "roba dal mago della città, a pagamento. Un oggetto che vedi per la prima "
               "volta identificalo prima di usarlo: e comunque, se resta sconosciuto, si "
               "vende per due soldi.")
RESE[14108] = ("E poi, quando esplori una Nefia, ricordati che più il labirinto è "
               "pericoloso, più vale il tesoro che ci trovi.")

# ============ secondo incontro: che cosa portarsi dietro ============

RESE[14111] = ("Oggi impariamo quali oggetti un avventuriero deve avere sempre con sé.")
RESE[14112] = ("Ricordati di portarti il cibo, e di avere sempre a portata di mano di che "
               "curarti e di che teletrasportarti, più una coperta ignifuga e una coperta "
               "termica. Quando affronti un nemico forte o entri in una terra sconosciuta, "
               "portati più scorte del solito.")
RESE[14113] = ("E non andare in un posto pericoloso mentre sei sotto peso. La roba pesante "
               "mettila nello specchio quadridimensionale. Con un buon Sollevamento pesi "
               "reggi di più, ma non perdere di vista il peso dello zaino mentre lo riempi "
               "di bottino.")
RESE[14114] = ("Quel che non ti serve lo posi col tasto d. E se premi il tasto *, ne posi "
               "diversi uno dopo l'altro: è comodo quando devi sistemare la roba.")

# ============ terzo incontro: lo stato degli oggetti ============

RESE[14117] = "Nel terzo incontro vi racconto meglio lo stato degli oggetti."
RESE[14118] = ("Se posi una bottiglia d'acqua sull'altare del tuo dio, o su un altare senza "
               "padrone se un dio non ce l'hai, l'acqua viene benedetta. E mescolando "
               "l'acqua benedetta a un oggetto qualunque, quell'oggetto prende la "
               "benedizione. Una bottiglia sola benedice tutta una pila, quindi conviene "
               "mettere da parte qualche decina di pergamene e benedirle in un colpo solo.")
RESE[14119] = ("D'altra parte, un oggetto può prendersi una maledizione da un incubo o dalla "
               "magia di un nemico. Un equipaggiamento maledetto non si riesce più a "
               "togliere e può fare brutti scherzi. Usa una magia, una pergamena o una "
               "bacchetta di purificazione, oppure fatti togliere la maledizione dal "
               "guaritore della città. Una pergamena di purificazione superiore pulisce "
               "tutto quel che hai addosso.")
RESE[14120] = ("Il cibo maledetto lo vomiti, e pozioni, pergamene e bacchette maledette "
               "fanno un effetto più debole, o dannoso. E la roba maledetta si vende anche "
               "per meno, quindi la regola è starne alla larga.")

# ============ quarto incontro: l'equipaggiamento ============

RESE[14123] = "Nel quarto e ultimo incontro vi spiego qualcosa di più sull'equipaggiamento."
# ⚠️ deroghe 1 e la lezione del lotto: i nomi delle classi vengono da `_quality`,
# i segni dall'inglese, che e' il ramo che l'italiano compila.
RESE[14124] = ("L'equipaggiamento ha sei classi: scadente, comune, eccellente, eccezionale, "
               "celestiale e speciale. Gli eccellenti portano un prefisso o un suffisso; "
               "gli eccezionali e gli speciali hanno il nome chiuso fra <>; i celestiali "
               "l'hanno chiuso fra {}.")
RESE[14125] = ("Eccellenti, eccezionali e celestiali portano incanti casuali. Eccezionali e "
               "celestiali si chiamano artefatti casuali, e sono più forti di qualunque "
               "altro oggetto dello stesso tipo. Gli speciali si chiamano artefatti fissi, e "
               "i loro effetti non cambiano mai.")
RESE[14126] = ("Un eccellente si può far salire a eccezionale, quindi se ne vedi uno con un "
               "incanto buono mettilo da parte. Un giorno avrai addosso soltanto artefatti "
               "potenti...")

# ============ le voci di menu ============

RESE[14131] = "Quali pergamene conviene raccogliere?"
RESE[14132] = "Quali pozioni conviene raccogliere?"
RESE[14133] = "Che letti e utensili da cucina sono buoni?"
RESE[14134] = "Cresce, quanti anni hai?"
RESE[14137] = "Mi parli delle bacchette?"
RESE[14138] = "Che succede se porto troppo peso?"
RESE[14139] = "Dove metto la roba che non porto?"
RESE[14140] = "Che cos'è il [Non posare]?"
RESE[14143] = "Che altro conviene benedire?"
RESE[14144] = "A che serve un oggetto maledetto?"
RESE[14145] = "Che cosa vuol dire +1?"
# ⚠️ 24 caratteri e' il tetto delle due colonne (`menu_dialogo`), e l'inglese
# ne fa 16: qui la resa non puo' passarlo.
RESE[14146] = "Cresce, hai un amore?"
RESE[14149] = "Come trovo un buon equipaggiamento?"
RESE[14150] = "Il materiale dell'equipaggiamento?"
RESE[14151] = "Che cosa sono i materiali da lavorazione?"
RESE[14152] = "E il vaso della fusione?"

RESE[14154] = "Avete qualche domanda?"

# ============ le risposte del primo incontro ============

RESE[14157] = ("Le pergamene pesano pochissimo e si usano anche senza abilità, quindi a chi "
               "comincia fanno comodo. Tieni da parte quelle di identificazione, cambio di "
               "materiale, mappa magica, individuazione degli oggetti, ritorno, "
               "purificazione, potenziamento dell'arma e dell'armatura, e meraviglia. Le "
               "pergamene di oracolo valgono care: si vendono o si scambiano con la roba "
               "degli altri avventurieri.")
RESE[14158] = ("Le pergamene di base più avanti contano meno, ma pesano poco e si tengono "
               "per le emergenze. Le rare sono crescita, acquisizione di attributi e la "
               "pergamena volante: se le trovi, tienile da parte finché non ti servono "
               "davvero. E la libreria di casa è un modo comodo di tenere in ordine libri e "
               "pergamene.")
RESE[14162] = ("Le pozioni pesano poco e se ne porta un mucchio. Certe si rinforzano con "
               "l'abilità Alchimia. Ce ne sono che curano o rinforzano te, ce ne sono da "
               "tirare addosso al nemico per fargli male o indebolirlo, e ce ne sono che "
               "rendono l'equipaggiamento resistente al fuoco o agli acidi... insomma, "
               "c'è di tutto.")
RESE[14163] = ("E poi acqua, cura della corruzione, declino, evoluzione, sangue di Ermes e "
               "acceleratore sono rare, quindi non lasciartele scappare. E se in casa hai "
               "uno scaffale delle pozioni, le pozioni le puoi riporre lì.")
RESE[14167] = ("Letti e utensili da cucina hanno un rango, e più il rango è alto meglio "
               "riesce quel che ci fai. Se li identifichi, col tasto x ne leggi il rango. "
               "Il migliore degli utensili è il set da barbecue, e il migliore dei letti è "
               "il letto della felicità. E ricordati che i pezzi di rango alto li trovi in "
               "giro per le città, e li puoi usare anche se non sono tuoi.")
# `:14171` non e' nel lotto: il silenzio `...` e' gia' reso e sta in `invariati.md`.
RESE[14172] = ("In casi così l'attrezzo giusto è la lente dell'intuito! Non ti dice solo "
               "l'età di chi hai davanti: anche altezza, peso, razza, attributi, abilità e "
               "resistenze elementali! Non trovi che il progresso sia una cosa "
               "meravigliosa?")

# ============ le risposte del secondo incontro ============

RESE[14175] = ("Con le bacchette, l'abilità Dispositivi magici pesa sull'effetto e anche "
               "sulla probabilità di riuscita. Pesano più delle pergamene e non si "
               "impilano se hanno cariche diverse, ma si ricaricano con le pergamene di "
               "ricarica e con la capacità Ricarica. Estrai carica e Ricarica si imparano "
               "salendo di livello, se hai Dispositivi magici almeno a 20.")
RESE[14176] = ("Le bacchette di cura, creazione di muri, teletrasporto, mutamento di "
               "creatura e identificazione sono comode. Se invece non ti interessa "
               "combattere con la magia, sulle bacchette d'attacco usa Estrai carica, "
               "oppure offrile a Itzpalt.")
RESE[14177] = ("Le bacchette di dominio sono rare e trasformano un nemico in un compagno per "
               "sempre, ma perché funzionino su un avversario di livello alto ti serve un "
               "buon livello di Dispositivi magici.")
RESE[14181] = ("Secondo quanto pesa lo zaino passi da Fardello a Fardello!, poi a "
               "Sovraccarico e a Sovraccarico!. Con Fardello non c'è problema, ma da "
               "Sovraccarico in poi la velocità crolla e il danno arriva di continuo. "
               "Portare troppo peso ti ammazza, prima o poi, e in viaggio è ancora più "
               "facile: sta' attento.")
RESE[14182] = ("Fra l'altro, l'abilità Sollevamento pesi cresce solo da Fardello in su, e "
               "con carichi più pesanti non cresce più in fretta. Se devi combattere con lo "
               "zaino carico, conviene posare qualcosa e tornare alla velocità normale.")
RESE[14186] = ("La roba che non ti serve addosso tienila a casa o in un magazzino: così non "
               "la perdi e non te la bruciano. Però il numero di oggetti che si possono "
               "posare dipende dal tipo di edificio: se la casa è piena, costruisci un "
               "magazzino, oppure lascia la roba in qualche altro posto sicuro.")
RESE[14187] = ("Non lasciare la tua roba in una città! Nel giro di una settimana te la "
               "portano via, almeno nella maggior parte delle città. Certe però hanno dei "
               "sotterranei, e lì la roba si può tenere.")
RESE[14188] = ("Ascolta bene! Quanti oggetti si possono tenere in un posto dipende dal tipo "
               "di edificio. Quando sei al limite e ne compaiono di nuovi, qualcuno dei "
               "vecchi viene distrutto. E vale anche per la cassaforte di un negozio e per "
               "il baule degli stipendi. Occhio a come tieni la roba!")
RESE[14192] = ("Apri il menu Esamina col tasto x e poi premi il tasto * per mettere e "
               "togliere il [Non posare] sull'oggetto scelto.")
RESE[14193] = ("Un oggetto col [Non posare] non si può posare, né vendere, né mangiare, né "
               "prendere con Estrai carica, e via dicendo. Non c'è un limite, quindi segna "
               "tutti gli attrezzi a cui tieni: così non li perdi per sbaglio.")

# ============ le risposte del terzo incontro ============

RESE[14196] = ("Benedire bacchette e pergamene ne rinforza l'effetto. Vale soprattutto per "
               "le pergamene di crescita, per quelle di cambio di materiale e di materiale "
               "superiore, e per le pergamene volanti.")
RESE[14197] = ("Ogni tanto, a mangiare cibo benedetto, la fortuna sale per un po'; ma non "
               "sprecarci l'acqua benedetta. Benedire una pozione ne alza l'effetto, e vale "
               "soprattutto per le pozioni di ripristino del corpo e dello spirito, di "
               "potenziale e di sangue di Ermes.")
RESE[14198] = ("Un'arma benedetta è più precisa e più potente, e un'armatura benedetta alza "
               "un pochino DV e PV. Ma la maledizione sovrascrive la benedizione, e "
               "l'equipaggiamento non si benedice tutto in un colpo: se l'acqua benedetta "
               "non ti avanza, meglio tenerla per altro.")
RESE[14202] = ("Se vuoi che il tuo equipaggiamento pesi di più, usa una pergamena volante "
               "maledetta. E se hai bisogno di maledire un oggetto, leggi una pergamena di "
               "maledizione o mescolaci dell'acqua maledetta.")
RESE[14203] = ("Fra l'altro, la pergamena di maledizione colpisce un oggetto a caso fra "
               "quelli che porti addosso. Quindi... e se posassi tutto tranne qualche "
               "bottiglia d'acqua?")
# ⚠️ deroga 2: l'inglese ha i contenuti scambiati rispetto al giapponese.
RESE[14207] = ("Il valore di potenziamento. Più il numero è alto, più l'oggetto è forte e "
               "più vale. Il cibo ti rinforza di più, l'arma diventa più precisa, e il resto "
               "dell'equipaggiamento alza un pochino DV e PV. Fino a +6 ci arrivi con le "
               "pergamene, fino a +10 in armeria.")
RESE[14208] = ("E poi, l'abilità Cucina alza qualità e prezzo del cibo, mentre "
               "equipaggiamento e mobili si migliorano con una pergamena che ne cambia il "
               "materiale in uno più pregiato.")
RESE[14209] = ("Se ti prendi un attacco acido, l'equipaggiamento perde valore di "
               "potenziamento, e può anche andare sotto zero. Il che, naturalmente, lo rende "
               "meno efficace. Certi materiali resistono agli acidi per natura, e cambiare "
               "materiale può dare la resistenza, ma non toglierla. Oppure puoi mescolarci "
               "il liquido antiacido.")
RESE[14213] = "Non costringermi ad ammazzarti. Poi mi tagliano lo stipendio."

# ============ le risposte del quarto incontro ============

RESE[14216] = ("Gli incanti sono casuali, quindi quel che conta è il numero dei pezzi. Non "
               "basta prendere tutto dall'armeria o dagli incarichi: puoi scambiare con "
               "altri avventurieri, ma la roba migliore sta nelle Nefie di livello alto. Con "
               "una magia, una pergamena o una bacchetta di identificazione, i pezzi li "
               "guardi mano a mano che li trovi.")
RESE[14217] = ("Se un pezzo che trovi pesa poco, tienitelo addosso e lascia che l'Analisi lo "
               "identifichi da sé. Ma un pezzo pesante, se non è almeno di qualità "
               "eccellente, tanto vale lasciarlo lì e portare via qualcosa che valga di "
               "più.")
RESE[14218] = ("Anelli e amuleti nuziali, ali e piume, calzini, anelli della velocità, "
               "mutandine, anelli dell'aurora, mantelli di Vindale, stivali delle sette "
               "leghe e cappelli da fata pesano poco e hanno effetti tutti loro, molto "
               "utili: quelli io li raccoglierei di qualunque qualità. Gli anelli e gli "
               "amuleti nuziali soprattutto, perché servono anche a stringere un rapporto.")
RESE[14222] = ("Ogni materiale ha un effetto suo, e rinforza o indebolisce lati diversi "
               "dell'equipaggiamento. Per i gioielli scegli un materiale che alzi le "
               "resistenze; per armi e armature, uno che ne alzi le prestazioni.")
RESE[14223] = ("Le pergamene che cambiano materiale girano su un giro fisso di materiali, e "
               "quelle che non sono di materiale inferiore, se benedette, aggiungono due "
               "materiali al giro. Ci sono anche i kit di materiali, che cambiano un oggetto "
               "in un materiale preciso, ma sono rari.")
RESE[14227] = ("I materiali da lavorazione non pesano niente e stanno in una lista tutta "
               "loro, che guardi col tasto m. Non si maneggiano come gli altri oggetti: "
               "servono con le abilità Alchimia, Falegnameria, Oreficeria e Sartoria.")
RESE[14228] = ("I punti di raccolta dei materiali stanno dentro le Nefie e si sfruttano "
               "cercando col tasto s. Secondo il tipo di punto ti servono Pesca, Scavo, "
               "Giardinaggio, Ingegneria genetica o Individuazione. Per i materiali migliori "
               "devi scendere in fondo alla Nefia, e quel che si trova cambia col tipo di "
               "Nefia. Anche quando la raccolta va male, l'abilità corrispondente prende "
               "esperienza.")
RESE[14229] = ("Più salgono Falegnameria, Alchimia, Sartoria e Oreficeria, più cose puoi "
               "fabbricarti e più tipi di materiale puoi usare, e così le abilità salgono "
               "ancora: quindi raccogli tutti i materiali che riesci. E se i tuoi compagni "
               "hanno certe abilità, i materiali te li raccolgono anche loro.")
RESE[14233] = ("Col vaso della fusione puoi unire due oggetti per farne uno nuovo, oppure "
               "aggiungere un effetto speciale a un oggetto. Servono abilità e attrezzi "
               "precisi, ma ci si fanno un mucchio di cose utili. Provaci almeno una "
               "volta.")

RESE[14237] = "Qualcuno ha altre domande? Se sì, venite pure a chiedere."
