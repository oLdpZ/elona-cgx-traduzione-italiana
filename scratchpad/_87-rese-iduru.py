# -*- coding: utf-8 -*-
"""Le rese di IDURU, docente del corso di crescita (chat.hsp :14241-:14380),
terzo dei quattro conferenzieri del seminario.

Perimetro: 68 firme, **zona chiusa** (nessuna occorrenza fuori).

REGISTRO. Iduru Gumbye e' uomo — «<Iduru> il docente» (`db_creature.hsp:54897`)
— e parla da istruttore alla mano (だ / だぞ / だな), dando del tu. Come per
gli altri due: **saluto e congedo al plurale**, spiegazioni al singolare. Vedi
[[_87-rese-ajetalio]] per la famiglia dei quattro corsi.

⭐ **IL SOPRANNOME E' UNA CATENA DI TRE BATTUTE, e l'inglese la rompe.** Il
giapponese: gli volevano affibbiare «いづるん» (Idurino), lui si e' impuntato
per farsi chiamare 師範, «maestro» — e a `:14293` uno studente lo chiama
「いづるん」 lo stesso, al che lui sbotta 「恥ずかしいから師範と呼んでほしい…！！」
(`:14373`). L'inglese: a `:14245` sceglie «Mr. Gumbye», a `:14275` **si
arrende in faccia al lettore** («Is there some untranslatable Japanese pun with
your name?»), a `:14312` e' testo automatico che non vuol dire niente («because
it is an idle gumbah»), e a `:14293` chiama il docente «Iduru». In italiano la
catena si tiene tutta: **«maestro»** contro **«Idurino»**, e le tre battute si
scrivono insieme — e' l'ECO della 84a.

⭐⭐⭐ **LA LEZIONE DEL LOTTO: le sette etichette del potenziale non passano da
`lang()`.** `command.hsp:10676`-`:10700` le stampa come letterali nudi —
`mes "Supreme"`, `"Amazing"`, `"Superb"`, `"Great"`, `"Good"`, `"Bad"`,
`"Hopeless"` — quindi **nessun dizionario le raggiunge e sullo schermo restano
inglesi**, oggi e finche' non le tocca una toppa. E' la famiglia del punto
cieco della 74a, un gradino piu' sotto: li' erano `listn(...) = lang(...)`, qui
non c'e' nemmeno la `lang()`. Il tutorial copia i nomi dell'interfaccia, quindi
qui «Supreme» e «Hopeless» restano **in inglese**: sono le parole che il
giocatore legge davvero premendo c.
⚠️ Il giorno in cui quelle sette righe si toppano, questa resa va rifatta.

⭐⭐ **E il codice smentisce l'inglese sulla scala.** A `:14246` l'inglese dice
che «"Superb" is the best»: falso. `command.hsp:10676` mette **Supreme** in
cima (>= 400), e Superb e' il terzo gradino (>= 200). Il giapponese lo dice
giusto — Supreme（至高）— e si segue quello.

LESSICO. Gli attributi (`skill.hsp`): Forza, Costituzione; le abilita': Cucina,
Sollevamento pesi, Trattativa, Viaggio, Analisi, Scasso, Scavo, Dispositivi
magici, Apprendimento, Borseggio, Incantesimi, Memoria, Lettura, Controllo
magia, Ingegneria genetica. Gli oggetti: sfera dei mostri (`db_item:143296`),
pietra evolutiva (`item.hsp:110`), grimorio, pergamena di meraviglia, ripristino
del corpo / dello spirito, pozione di potenziale, guinzaglio, stetoscopio.
L'interfaccia: «Traccia abilita'» (`command.hsp:10379`, il tasto *),
«Interagire» (`help.hsp:40`, il tasto i), «Metti fra gli indispensabili»
(`command.hsp:6038`), «Simpatia» (`chat.hsp:25511`, il pannello del compagno),
«Anima gemella» (`text.hsp:34`), «Iniz.» per INIT (`command.hsp:10504`),
«talento» per フィート (`command.hsp:2113`). I posti: Vernis, Yowyn, Porto
Kapul (`text.hsp:2743`), Tyris del Nord (`:2737`), la Gilda dei Maghi.

⚠️ **スキル e 技能 in italiano sarebbero la stessa parola.** L'inglese le tiene
separate («skills» / «abilities») e l'italiano fa lo stesso: **abilita'** per
スキル, che e' il nome della linguetta (`module.hsp:5153`), e **capacita'** per
技能, con «capacita' ad area» per 広域技能 — la forma di `command.hsp:5673`,
gia' usata nel lotto di Cresce.

⚠️ LE DEROGHE DICHIARATE

1. **`:14246`** — l'inglese sbaglia il vertice della scala (vedi sopra): il
   giudice e' `command.hsp:10676`. E l'inglese taglia anche il perche' la cosa
   importi: col potenziale a terra l'attributo non sale piu'.
2. **`:14275`, `:14312`, `:14293`, `:14373`** — la catena del soprannome. A
   `:14312` l'inglese e' testo automatico rotto e non si puo' seguire; a
   `:14275` e' una domanda al lettore invece che allo studente.
3. **`:14336`** — l'inglese **aggiunge** in coda la frusta del domatore, che il
   giapponese non nomina. Si tiene: e' un'istruzione, ed e' la risposta pratica
   alla domanda.
4. **`:14315`** — l'inglese taglia il numero (fino a circa 200 di attributo col
   solo cibo) e ci mette il compagno col Borseggio che si paga l'allenamento.
   Si segue l'inglese: il numero torna comunque a `:14326`.
5. **`:14322`** — l'inglese aggiunge che gli istruttori delle citta' **non**
   insegnano niente ai compagni, che e' il motivo per cui la domanda esiste.
6. **`:14345`** — l'inglese da' un nome all'oggetto («Evolution Hearts») dove
   il giapponese dice solo 進化アイテム; il nome sta in `item.hsp:110`, ed e'
   «pietra evolutiva».
7. **`:14374`** — l'inglese aggiunge il numero (150 compagni) e dove sta il
   dojo (vicino al confine con Tyris del Sud). Si tiene.
"""

RESE = {}

# ============ primo incontro: gli attributi ============

# ⚠️ deroga 2: la catena del soprannome comincia qui.
RESE[14245] = ("Sono Iduru Gumbye e tengo il corso di crescita, piacere. Chiamatemi pure "
               "maestro. Bene: per cominciare vi spiego in breve gli attributi, quelli che "
               "si leggono col tasto c.")
# ⚠️ deroga 1: «Superb is the best» e' falso, `command.hsp:10676` mette Supreme in cima.
# ⚠️ Le sette etichette restano in inglese: sono letterali nudi, senza `lang()`.
RESE[14246] = ("Roba come Forza e Costituzione sono i tuoi attributi base. Il potenziale "
               "dice quanto è facile farli salire: Supreme è il massimo, Hopeless è il "
               "minimo. Gli attributi salgono da sé usando le abilità e le capacità che "
               "gli corrispondono; ma se lasci scendere il potenziale e non lo rimetti su, "
               "l'attributo smette del tutto di crescere.")
RESE[14247] = ("Il potenziale degli attributi si recupera dormendo, e più il letto è di "
               "rango alto più ne recupera. I negozi di magia di rango alto ogni tanto "
               "hanno le pozioni di potenziale, ma sono troppo rare per farci conto.")
RESE[14248] = ("Gli attributi con un * accanto sono sostenuti dall'equipaggiamento, che li "
               "protegge dai colpi che li abbassano. Se un attributo ti cala, usa una magia "
               "o una pozione di ripristino del corpo per quelli fisici, di ripristino "
               "dello spirito per quelli mentali, oppure paga il guaritore della città "
               "perché te li rimetta a posto.")
RESE[14249] = ("Le abilità si imparano, e il loro potenziale si recupera, pagando monete di "
               "platino agli istruttori delle città. È la cosa più importante per farsi più "
               "forte. E col tasto * puoi seguire un'abilità con la Traccia abilità, così "
               "tieni d'occhio il suo potenziale.")

# ============ secondo incontro: i compagni ============

RESE[14252] = ("L'argomento di oggi sono i compagni... o gli animali, come li chiama "
               "qualcuno.")
RESE[14253] = ("Quanti compagni puoi avere cresce a poco a poco col tuo Carisma. Alla fine "
               "arrivi al massimo di quindici, ma senza un posto libero non puoi accettare "
               "gli incarichi di scorta: tienine sempre almeno uno vuoto.")
RESE[14254] = ("I compagni si trovano leggendo una pergamena di rinforzi, con la magia o le "
               "bacchette di dominio, oppure tirando una sfera dei mostri. Certi mostri si "
               "uniscono a te se li abbatti, e chi ha fede può ricevere compagni divini dal "
               "proprio dio.")
RESE[14255] = ("Il dominio riesce solo se la tua abilità di magia, per gli incantesimi, o i "
               "Dispositivi magici, per le bacchette, hanno la meglio sul nemico; però ha "
               "effetto subito. La sfera dei mostri non chiede nessuna abilità particolare, "
               "ma funziona solo se l'avversario è in fin di vita. Tienilo a mente.")

RESE[14258] = ("Riprendo da dove ho lasciato l'ultima volta: ancora sui compagni, e stavolta "
               "più a fondo.")
RESE[14259] = ("Se trascuri il loro equipaggiamento, i compagni non ce la fanno a "
               "sopravvivere. Equipaggiali come si deve.")
RESE[14260] = ("Avere tanti compagni va benissimo, ma non prenderne di nuovi se non hai "
               "l'equipaggiamento pronto per loro. Se un compagno muore, la simpatia che "
               "prova per te cala. E per tenerli vivi, ricordati di usare su ognuno il "
               "guinzaglio e lo stetoscopio.")
RESE[14261] = ("Una squadra allenata e ben equipaggiata è fortissima: perché in tanti si "
               "fa più danno, e perché una folla di nemici non si accanisce tutta su una "
               "persona sola. Se non sei un tipo che ama la solitudine, un compagno o due "
               "prendili davvero!")

# ============ quarto incontro: il potenziale e l'esperienza ============

RESE[14264] = ("Già il quarto incontro... come vola il tempo. Da quel che ci siamo detti "
               "finora, quanto conta il potenziale quando si cresce?")
RESE[14265] = ("L'esperienza che entra in un'abilità cresce o cala secondo il potenziale e "
               "il livello dell'abilità stessa. Su un'abilità bassa bastano poca esperienza "
               "e poco potenziale per vederla salire.")
RESE[14266] = ("Ma quando l'abilità è salita un po', la crescita rallenta o si ferma del "
               "tutto, a meno che tu non alzi il potenziale o non faccia qualcosa di più "
               "impegnativo. Per tenere d'occhio i progressi, usa la Traccia abilità di cui "
               "vi ho parlato in un incontro passato.")
RESE[14267] = ("E poi, secondo il tuo Apprendimento, ogni tanto l'esperienza guadagnata "
               "aumenta. Attenzione però: i mostri evocati e quelli nati dalla divisione di "
               "un altro mostro non danno nessuna esperienza.")

# ============ le voci di menu ============

RESE[14272] = "Che abilità mi consigli?"
RESE[14273] = "Mi parli delle capacità?"
# ⚠️ 24 e' il tetto delle due colonne e l'inglese ne fa 23: la resa non lo passa.
RESE[14274] = "Dove trovo il platino?"
# ⚠️ deroga 2: l'inglese si arrende al lettore, il giapponese chiede il titolo.
RESE[14275] = "Perché proprio maestro?"
RESE[14278] = "Come alzo gli attributi dei compagni?"
RESE[14279] = "Come alzo le abilità dei compagni?"
RESE[14280] = "Come alzo il potenziale dei compagni?"
RESE[14281] = "E se un compagno muore?"
RESE[14284] = "Che cos'è la simpatia?"
RESE[14285] = "Che cos'è la coppia?"
RESE[14286] = "Come faccio evolvere un compagno?"
RESE[14287] = "Come insegno un'abilità a un compagno?"
RESE[14290] = "Come si impara la magia?"
RESE[14291] = "Come si allena la magia?"
RESE[14292] = "Mi parli di AP e Iniz.?"
# ⚠️ deroga 2: lo studente usa lo stesso il soprannome che il maestro ha rifiutato.
RESE[14293] = "Idurino, la tua famiglia che fa?"

RESE[14295] = "Allora, ci sono domande?"

# ============ le risposte del primo incontro ============

RESE[14298] = ("Non ragionare così: contano tutte, una per una. Detto questo, qualcuna viene "
               "prima delle altre. Cucina, per far salire gli attributi; Sollevamento pesi, "
               "per portare più roba; Trattativa, per non svenarti; e Viaggio, che aiuta "
               "tutte le altre a crescere.")
RESE[14299] = ("Quando hai quelle, ti conviene prendere le abilità che servono a esplorare: "
               "Analisi, Scasso, Scavo, Dispositivi magici, e poi quelle dello stile di "
               "combattimento che preferisci. ...Be', non farne un dramma. Come ho detto, "
               "alla lunga le vuoi tutte, quindi anche cambiare stile di sana pianta non "
               "sarebbe un problema.")
RESE[14300] = ("Ogni città ha un istruttore che insegna abilità diverse. Quelle di cui "
               "parlavo prima si imparano a Vernis, qui subito a nord, a Yowyn a sud-est e "
               "a Porto Kapul a nord-ovest; ma va' a vedere anche gli istruttori delle "
               "altre città.")
RESE[14304] = ("Quasi tutte le capacità si imparano salendo di livello con un attributo o "
               "un'abilità sopra un certo valore. Le capacità normali si usano col tasto a, "
               "quelle ad area col tasto W. Quelle che non usi le puoi nascondere col tasto "
               "*.")
RESE[14308] = ("Le monete di platino arrivano soprattutto portando a termine gli incarichi "
               "delle città, e più l'incarico è difficile più ne danno. Se ne prendono anche "
               "conquistando una Nefia o abbattendo una campana di platino, ma il grosso "
               "sono gli incarichi.")
# ⚠️ deroga 2: l'inglese qui e' testo automatico rotto; si segue il giapponese.
RESE[14312] = ("Ah... quello? All'inizio stavano per affibbiarmi il soprannome Idurino, "
               "visto che mi chiamo Iduru Gumbye. Alla mia età era una vergogna, così ho "
               "fatto i capricci finché non mi hanno chiamato maestro, che poi è come mi "
               "chiamano a casa mia.")

# ============ le risposte del secondo incontro ============

# ⚠️ deroga 4: l'inglese taglia il numero e mette il compagno col Borseggio.
RESE[14315] = ("Se vuoi alzare gli attributi dei compagni, dagli spesso da mangiare piatti "
               "cucinati bene. Anche le erbe vanno benissimo! E fa' in modo che possano "
               "pagarsi l'allenamento: un compagno col Borseggio raccoglie soldi in più dai "
               "nemici abbattuti, e ci copre la spesa.")
RESE[14316] = ("Con lo stetoscopio su un compagno capisci quando ha fame: la sua barra rosa "
               "diventa verde-azzurra. Tieni sempre da parte del cibo e daglielo appena ha "
               "fame. Se sei a corto, raccogli la frutta dagli alberi o compra dal "
               "fornaio.")
RESE[14320] = ("Tieni alto il potenziale delle loro abilità e falli esercitare, esercitare, "
               "esercitare. Se vuoi allenargli le abilità di combattimento devi lasciarli "
               "combattere. E ricorda: le abilità difensive non crescono se abbatti i "
               "nemici deboli con un colpo solo.")
RESE[14321] = ("Con l'abilità Viaggio, andando da una città all'altra tutte le abilità "
               "salgono un pochino. Il Viaggio da solo però non basta a farli più forti: è "
               "un aiuto che si somma col tempo. Ogni poco fa.")
# ⚠️ deroga 5: l'inglese aggiunge il perche' la domanda esiste.
RESE[14322] = ("Purtroppo gli istruttori delle città ai compagni non insegnano niente di "
               "nuovo: un modo per riuscirci c'è, ma ve lo spiego in un'altra lezione. "
               "Intanto lavora sulle abilità che hanno già.")
RESE[14326] = ("Senza potenziale, i compagni non diventano più forti. Lascia che raccolgano "
               "le monete d'oro, oppure dagli minerali da vendere come la mica e il "
               "rubynus: quando sono in città si pagano l'allenamento da soli e si alzano il "
               "potenziale di attributi e abilità.")
RESE[14327] = ("Quanto costa l'allenamento dipende da Iniz., la forza iniziale del compagno. "
               "Anche quando diventa più forte il costo non sale; anzi, man mano che gli "
               "cresce il Carisma, cala.")
RESE[14331] = ("Un compagno morto te lo resuscita il barista della città, a pagamento. Se "
               "hai un libro di resurrezione, o sai lanciare la Resurrezione, puoi farlo da "
               "te; ma il primo è raro e la seconda non è roba da tutti.")
RESE[14335] = ("La simpatia sale lasciando che i compagni combattano per te e facendogli "
               "regali. Quando è alta, un compagno con Cucina ti prepara la colazione, e uno "
               "con Sartoria o Falegnameria ti fabbrica armature. E se diventate anime "
               "gemelle, ti ci puoi anche sposare. Con un afrodisiaco fai in modo che "
               "qualcuno ti prenda in simpatia, ma non te lo consiglio.")
# ⚠️ deroga 3: l'inglese aggiunge la frusta del domatore, che il giapponese non nomina.
RESE[14336] = ("Un compagno a cui hai detto di non toccare la roba per terra a volte ci mette "
               "le mani lo stesso: uno che ha fame, per dire, si mette a mangiare quel che "
               "trova. Se lo scacci o se lo lasci fare cambia il vostro rapporto fra padrone "
               "e servitore. Lo vuoi obbediente o lo vuoi con la sua testa? ...O magari non "
               "te ne importa niente e vuoi solo che la smetta di combinare guai: in quel "
               "caso usagli addosso la frusta del domatore.")
RESE[14340] = ("Con una coppia, un compagno sta nella stessa casella tua o di un altro "
               "compagno. Chi forma la coppia si muove e agisce come sempre, così l'altro "
               "non deve muoversi e può pensare solo a colpire.")
RESE[14341] = ("Quando formi una coppia, tieni conto di come combattono i due: se li accoppi "
               "bene diventano molto più forti. E siccome si proteggono a vicenda, puoi "
               "mettere un compagno debole con uno forte per tenerlo in vita.")
# ⚠️ deroga 6: il nome dell'oggetto viene da `item.hsp:110`.
RESE[14345] = ("L'evoluzione ha bisogno di certe pietre speciali, le pietre evolutive, che "
               "lasciano cadere certi nemici. Si può far evolvere solo qualche tipo di "
               "creatura, e solo se avete stretto un bel legame di simpatia.")
RESE[14346] = ("L'evoluzione alza gli attributi e a volte porta capacità nuove. Cambia "
               "l'aspetto e il nome del compagno, ma il compagno resta lo stesso di prima: "
               "non preoccuparti.")
RESE[14350] = ("Non lo sa quasi nessuno, ma con l'Ingegneria genetica si può insegnare "
               "un'abilità nuova a un compagno. È una tecnica dell'epoca della civiltà "
               "biochimica: si scompone una creatura e se ne trapiantano le doti. Me ne ha "
               "parlato uno studioso che conosco, a Porto Kapul.")
RESE[14351] = ("In teoria puoi trapiantare in un compagno abilità nuove, e perfino parti del "
               "corpo, e per giunta rinforzarlo. Va da sé che, prima di fare una cosa così "
               "pericolosa, quello che vuoi tenere lo apri col tasto i e lo metti fra gli "
               "indispensabili: altrimenti rischi di scomporre proprio lui!")
RESE[14355] = ("La magia si impara nei sogni, con le pergamene di meraviglia o dai grimori. "
               "I primi due modi sono casuali, quindi di regola il grosso delle scorte di "
               "incantesimi arriva dai grimori.")
RESE[14356] = ("Ogni tipo di grimorio ha la sua difficoltà, e più è difficile più Lettura "
               "vuole. Se la decifrazione va male puoi perdere un mucchio di MP o ritrovarti "
               "con dei mostri intorno, quindi sta' attento a dove leggi, e non intestardirti "
               "su un libro che continua a resisterti.")
RESE[14357] = ("Leggere un grimorio ti dà scorte di incantesimi in base a Memoria. E se "
               "entri nella Gilda dei Maghi, puoi ordinare al loro scrivano la copia di un "
               "grimorio preciso: tutti tranne quelli del Raccolto del mago e del "
               "Desiderio.")
RESE[14361] = ("Lanciare un incantesimo abbastanza volte ne alza il livello, e con quello la "
               "potenza e la probabilità di riuscita. Il potenziale degli incantesimi lo "
               "guardi nel pannello del personaggio, col tasto c. E il potenziale degli "
               "incantesimi si recupera dormendo.")
RESE[14362] = ("Pagando monete di platino al mago di una città puoi fare una lezione pratica "
               "di magia. La lezione allena più incantesimi insieme senza consumare scorte: "
               "è un modo rapido di migliorarli. Attenzione però: un incantesimo di livello "
               "più alto costa anche un po' più di MP.")
RESE[14363] = ("Fra l'altro, per i compagni che lanciano magie non serve preoccuparsi di "
               "niente di tutto questo: a loro basta l'abilità Incantesimi. Ah, e se tu o i "
               "tuoi compagni usate magie a saetta o ad area, il Controllo magia è "
               "indispensabile.")
RESE[14367] = ("Gli AP sono i punti di risveglio, e si prendono abbattendo nemici forti. "
               "Quando ne guadagni vedi un lampo, quindi te ne accorgi.")
RESE[14368] = ("A farla semplice, gli AP dipendono soprattutto da Iniz., e in particolare "
               "dall'Iniz. di velocità. Vuol dire che chi è partito debole e lento è "
               "avvantaggiato nel raccoglierli.")
RESE[14369] = ("Si dice in giro che con gli AP si possano rinforzare le abilità, prendere "
               "capacità nuove e sbloccare poteri unici... Però qui a Tyris del Nord non "
               "conosco nessuno capace di farlo. Forse un giorno, se andrai in terre nuove, "
               "scoprirai il segreto degli AP...")
# ⚠️ deroga 2: la battuta che chiude la catena del soprannome.
RESE[14373] = "Chiamatemi maestro, per favore... mi vergogno...!"
# ⚠️ deroga 7: l'inglese aggiunge il numero e dove sta il dojo.
RESE[14374] = ("...Ah, i miei tengono un dojo laggiù a sud, vicino al confine con Tyris del "
               "Sud. Si paga, ma ci puoi lasciare fino a centocinquanta compagni: col tempo "
               "si irrobustiscono un pochino, e pagando un extra gli si può anche rimettere "
               "su il potenziale. Ah, scusate: non volevo sembrare un imbonitore...")

RESE[14377] = "Se avete altre domande, venite pure a chiedere."
