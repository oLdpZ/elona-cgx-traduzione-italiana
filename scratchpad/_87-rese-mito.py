# -*- coding: utf-8 -*-
"""Le rese di MITO, docente del corso di combattimento (chat.hsp :14381-:14524),
quarta e ultima dei conferenzieri del seminario.

Perimetro: 71 firme dentro, **70 da fare**, zona chiusa. La settantunesima e'
gia' resa altrove.

REGISTRO. Mito Lydian e' donna — «<Mito> la docente» (`db_creature.hsp:54812`)
— e parla allegra e diretta (だよ / ね / よ), incoraggiando la classe; a
`:14475` e `:14477`, alla domanda su chi le piace, va in confusione. Come per
gli altri tre: **saluto e congedo al plurale**, spiegazioni al singolare. Vedi
[[_87-rese-ajetalio]] per la famiglia dei quattro corsi.

⭐ **La conferma della lezione di Cresce arriva dall'inglese stesso.** A
`:14404`, `:14471` e `:14491` l'inglese scrive «<> or {}» dove il giapponese
scrive 『』 e 《》: sono gli stessi segni di `:14124`, e `item_func.hsp:1786`-
`:1797` dice che nel ramo inglese — quello su cui si costruisce l'italiano —
sono davvero `<>` e `{}`. Qui non c'e' niente da decidere: si copia l'inglese,
che per una volta sa che schermo sta descrivendo.

LESSICO. Le posizioni dei compagni sono nomi di interfaccia: **Assalto**
(`text.hsp:2457`) e **Intercettazione** (`:2463`). Le capacita': Chiama
famiglio (`skill.hsp:1204`), Furia collettiva (`:1144`), <Forza liberata>
(`custom_tweaks.hsp:1255`), Salto dimensionale (`skill.hsp:968`), Scudo
elementale (`:649`), Rigenerazione (`:644`), Dardo magico (`:479`), Crea muri,
Ragnatela. Gli stati: Furia (`text.hsp:72`), Eroismo e Concentrazione
(`buff.hsp`). Le abilita': Lancio (`skill.hsp:186`), Equitazione (`:403`),
Dispositivi magici. La scala delle resistenze e' quella di `text.hsp:107` —
Fatale, Debolezza, Nessuna, Scarsa, Normale, Forte, **Ottima**, Enorme,
Suprema — e l'inglese di `:14458` e `:14459` dice «Superb», che li' vuol dire
**Ottima**. I posti e i mostri: la Grotta dei Cuccioli (`text.hsp:2857`), il
paguro, lo scarabeo, il pipistrello, la roccia esplosiva. E la «barra di
potenza» e' la resa gia' in uso a `chat.hsp:24378`.

⚠️ **DV e PV restano DV e PV**: il gioco li scrive cosi' anche in italiano
(`db_item.hsp:134633`, «correttore di DV»).

⚠️ LE DEROGHE DICHIARATE

1. **`:14385`** — l'inglese butta il soprannome (「ミトリンこと」). Si tiene
   «Mitorin»: gli altri tre docenti il soprannome ce l'hanno tutti, e a
   `:14418` uno studente lo usa per rivolgersi a lei.
2. **`:14441`** — l'inglese taglia il modo che NON costa un oggetto raro:
   con l'Analisi alta, combattendo si arriva allo stato Complete e le
   caratteristiche dell'avversario si leggono lo stesso. E' l'istruzione.
3. **`:14448`** — l'inglese cambia discorso a meta': dove il giapponese dice
   dove si legge il proprio metro (la valutazione di forza, nella scheda del
   tasto c), l'inglese ci mette i materiali che si trovano solo in certe
   Nefie. Si segue il giapponese: la domanda era «con che difficolta' me la
   posso vedere?».
4. **`:14437`** — l'inglese riassume in «certain special enemies» due cose
   diverse: i mostri scavatori e le varianti col nome fra `<>` o `{}`. E
   taglia il fumogeno, che e' l'altra meta' della risposta.
5. **`:14465`** — l'inglese aggiunge il Ripristino del corpo per gli SP e
   perde le pergamene di mana. Si segue l'inglese: e' piu' completo.
6. **`:14470`** — l'inglese **aggiunge** quali buff parano quali stati
   (Eroismo contro paura e confusione, Concentrazione contro sonno e
   confusione) e taglia l'elenco dei pericoli. Si tiene l'inglese: sono nomi
   di oggetti che il giocatore puo' cercare.
7. **`:14507`** — l'inglese aggiunge la reazione a catena delle rocce
   esplosive, che il giapponese non dice ed e' il modo tipico di morire in
   quel caso.
8. **`:14486`** — «absolute piercing attack» e' il nome dell'incanto, e in
   italiano sta gia' scritto in `item_data.hsp:677`: «un attacco che perfora
   sempre».
"""

RESE = {}

# ============ primo incontro: prepararsi prima di combattere ============

# ⚠️ deroga 1: il soprannome che l'inglese butta.
RESE[14385] = ("Ciao a tutti! Sono Mito Lydian, per gli amici Mitorin, e tengo il corso di "
               "combattimento. Cominciamo!")
RESE[14386] = ("Il combattimento viene dopo: prima ci si mette in piedi una vita, ci si "
               "procurano gli oggetti e si cresce. Quindi forse conviene sentire prima i "
               "corsi degli altri insegnanti.")
RESE[14387] = ("Tanto per cominciare, finché non sei pronto perfino gli incarichi di "
               "combattimento delle città sono pericolosi! Non metterti in una rissa che "
               "non puoi vincere, e non restare lì se le probabilità sono contro di te. Se "
               "incontri un nemico molto più forte, o se sono in tanti contro uno, "
               "ritirati!")
RESE[14388] = ("Se sei alle prime armi e non stai attento, rischi di ritrovarti circondato e "
               "pestato da nemici che a malapena scalfisci, o che non riesci nemmeno a "
               "toccare. Studia gli avversari, tieni a mente di che sono capaci e scegli "
               "l'ordine con cui affrontarli.")

# ============ secondo incontro: che cosa vuol dire essere forti ============

RESE[14391] = "Comincia il corso di combattimento! Diamoci da fare anche oggi!"
RESE[14392] = ("Mmh... Per prima cosa: un avventuriero forte non è uno che ha gli attributi "
               "alti. Puoi averli a 100 o a 1000, ma se vinci soltanto contro chi li ha più "
               "bassi dei tuoi, forte non sei. Così fanno anche gli animali selvatici.")
RESE[14393] = ("Un avventuriero davvero forte sa usare tutto quello che ha. Tira fuori il "
               "massimo da ogni singolo pezzo e ammazza senza scomporsi avversari che "
               "valgono parecchie volte lui. E anche davanti a uno che sembra imbattibile, "
               "sopravvive, capisce come si combatte quel nemico e alla fine lo batte.")
RESE[14394] = ("La parte più importante di uno scontro non è lo scontro: è quel che fai "
               "prima. Uscire senza difesa addosso, senza un modo per curarti e senza un "
               "modo per scappare non è andare all'avventura, è suicidarsi.")

# ============ terzo incontro: l'arma di riserva ============

RESE[14397] = ("Terzo incontro del corso di combattimento... A quest'ora avrete già trovato "
               "l'arma e lo stile che fanno per voi, no? La lezione di oggi è sulle armi di "
               "riserva, che contano ancora più dell'arma principale.")
RESE[14398] = ("Per adesso può bastare menare con un'arma o tirare una freccia magica, ma "
               "andando avanti incontrerai nemici forti contro il fisico, nemici forti "
               "contro la magia e nemici che annullano quasi del tutto gli attacchi "
               "elementali. Se a quel punto non hai un altro modo di colpire, sono guai.")
RESE[14399] = ("Un nemico con una difesa fisica solida si può danneggiare lo stesso col "
               "danno elementale dell'arma, quindi chi combatte di forza può coprire più "
               "fronti così. Se invece lanci magie, tieni un incantesimo di elemento magia "
               "come il Dardo magico più uno dell'elemento che preferisci. E procurati "
               "anche le magie a saetta e ad area.")
RESE[14400] = ("Ci sono altri modi di mettere insieme attacchi diversi e usarli come armi di "
               "riserva. Per dire: contro un nemico che resiste alla magia, chi lancia "
               "incantesimi può tirarsi indietro e pensare a curare il compagno che mena. "
               "Fa' come ti riesce meglio, purché tu sia pronto a nemici con difese di ogni "
               "genere.")

# ============ quarto incontro: i nemici difficili ============

RESE[14403] = ("Andando avanti incontrerai nemici di tutti i tipi. Nemici che schivano o "
               "parano i colpi, nemici che resistono alla magia, perfino nemici con "
               "capacità tutte loro: senza un piano di riserva finisci per trovarti in "
               "difficoltà.")
RESE[14404] = ("Se il nemico non ha il nome fra <> o {}, con una bacchetta di mutamento di "
               "creatura te la cavi in qualunque caso. In quest'ultimo incontro però vi "
               "insegno come si trattano certi nemici particolarmente fastidiosi.")

# ============ le voci di menu ============

RESE[14409] = "Come scappo da uno scontro?"
RESE[14410] = "Come capisco quanto è forte un nemico?"
RESE[14411] = "Con che difficoltà me la posso vedere?"
RESE[14412] = "E se il nemico è troppo veloce?"
RESE[14415] = "Come rinforzo la difesa?"
RESE[14416] = "Come mi curo?"
RESE[14417] = "Come mi tolgo un'alterazione?"
RESE[14418] = "Mitorin, c'è qualcuno che ti piace?"
RESE[14421] = "E i nemici che schivano tutto?"
RESE[14422] = "E i nemici con la difesa alta?"
RESE[14423] = "E i nemici che si curano?"
RESE[14424] = "Come si lanciano bene gli oggetti?"
RESE[14427] = "E i nemici che contrattaccano?"
RESE[14428] = "E i nemici che si fanno esplodere?"
RESE[14429] = "E i nemici che si dividono?"
RESE[14430] = "E i nemici invisibili?"

RESE[14432] = "Se avete altre domande, chiedete pure."

# ============ le risposte del secondo incontro ============

RESE[14435] = ("Il teletrasporto è la via più facile, ma si può bloccare. Le pergamene non "
               "si leggono se sei cieco, gli incantesimi non si lanciano se sei sotto "
               "silenzio e riescono male se sei confuso. Con buoni Dispositivi magici le "
               "bacchette di teletrasporto sono affidabili, ma certi posti il teletrasporto "
               "lo impediscono e basta.")
RESE[14436] = ("Però il teletrasporto ti butta in un punto a caso, quindi usalo prima che le "
               "cose si mettano troppo male, e guardati intorno che ci sia spazio. Il "
               "teletrasporto minore e il Salto dimensionale spesso ti spostano di pochi "
               "passi: non fidarti troppo.")
# ⚠️ deroga 4: l'inglese riassume in «certain special enemies» e taglia il fumogeno.
RESE[14437] = ("Se il nemico è lontano, è utile anche tagliargli la strada con Crea muri o "
               "con la creazione di porte, così non ti insegue. I mostri che scavano e le "
               "varianti col nome fra <> o {} però te li buttano giù. E se tiri un fumogeno "
               "e alzi una cortina, quasi tutti gli attacchi a distanza non ti prendono "
               "più.")
# ⚠️ deroga 2: l'inglese taglia lo stato Complete, che e' il modo senza oggetto raro.
RESE[14441] = ("Col tasto * guardi il bersaglio e vedi più o meno che livello ha rispetto a "
               "te. È solo un'indicazione, però: uno scontro cambia moltissimo secondo "
               "l'equipaggiamento. Per sapere i numeri veri di chi hai davanti c'è la lente "
               "dell'intuito, ma è rara... e se hai l'Analisi alta, combattendo di forza "
               "contro qualcuno fino a portarlo allo stato Complete, i suoi attributi li "
               "leggi lo stesso.")
RESE[14442] = ("Dal nome e dall'aspetto qualcosa si indovina, ma l'unico modo sicuro di "
               "sapere che cosa sa fare un avversario è combatterlo e impararlo sulla "
               "pelle. Se abbatti i nemici senza badare a quel che sanno fare, però, più "
               "avanti rischi una brutta sorpresa. Imparare e ricordare quanto pesa ogni "
               "tipo di nemico è importante quanto menare.")
RESE[14446] = ("All'inizio dell'inizio, esci dalla città e nei campi combatti gli animali "
               "selvatici mentre raccogli da mangiare. Attento a non farti circondare, che "
               "ci resti! Poi, quando sei più forte, puoi provare la Grotta dei Cuccioli, "
               "qui subito a nord-ovest. E prima di scendere in fondo a un labirinto, "
               "portati cibo e scorte a sufficienza.")
RESE[14447] = ("Se la Grotta dei Cuccioli ti sembra facile, prova a esplorare le Nefie di "
               "livello basso qui intorno. Da avventuriero, tieni sempre presente fin dove "
               "puoi scendere senza rischiare troppo. Se fai fatica, ritirati e torna a "
               "Nefie meno pericolose.")
# ⚠️ deroga 3: l'inglese cambia discorso; il giapponese dice dove si legge il proprio metro.
RESE[14448] = ("E ricordati che il livello dell'ingresso di una Nefia non è il livello "
               "consigliato per andarci. Il livello dei nemici che sei riuscito ad abbattere "
               "è segnato come valutazione di forza nella scheda del personaggio, col tasto "
               "c: prendi quella come metro.")
RESE[14452] = ("È l'attributo Velocità a decidere quanto spesso agisci. Un nemico molto più "
               "veloce di te riesce a colpirti più volte di fila; e uno velocissimo può "
               "curarsi più in fretta di quanto tu riesca a fargli male. Alza la tua "
               "velocità con pozioni, bacchette e magie di accelerazione. Anche "
               "l'Equitazione è una strada.")
RESE[14453] = ("Però, se il nemico agisce spesso, vuol dire anche che veleno, ferite e "
               "terreno acido lo mangiano in fretta: quelli scattano sul suo tempo, non sul "
               "tuo. Un nemico veloce ma fragile lo puoi abbattere tirandogli addosso una "
               "tintura o un veleno. Provaci!")

# ============ le risposte del terzo incontro ============

RESE[14457] = ("Contro gli attacchi fisici hai due valori: il DV, che ti fa schivare, e il "
               "PV, che riduce il danno che incassi. Puoi specializzarti nell'uno o "
               "nell'altro, ma schivare proprio ogni colpo è difficile, quindi buttare via "
               "il PV non te lo consiglio.")
RESE[14458] = ("Più avanti ti conviene alzare anche le resistenze elementali: un elemento "
               "contro cui non hai nessuna resistenza può ammazzarti. E contro fuoco e "
               "gelo, se la resistenza è sotto Ottima, rischi perfino di perdere degli "
               "oggetti; con una coperta ignifuga e una coperta termica te li salvi. Se ne "
               "hai in più, dalle anche ai compagni.")
RESE[14459] = ("Sarebbe bello avere tutte le resistenze a Ottima, ma ci vuole tempo. "
               "Intanto ti danno una mano lo Scudo elementale e le pozioni di resistenza, "
               "oppure puoi cambiare equipaggiamento quando sai che davanti hai un nemico "
               "di un certo elemento.")
RESE[14463] = ("Avere modi pratici di curarsi è importantissimo. Se non hai come recuperare "
               "almeno metà degli HP in un colpo, a un'imboscata non ti rialzi più. "
               "Bacchette, magie, pergamene, pozioni e certe capacità curano: ognuna ha i "
               "suoi pro e i suoi contro, quindi impara a usarne almeno due. Le pergamene "
               "però vanno bene solo all'inizio: curano sempre la stessa quantità.")
RESE[14464] = ("Tenere d'occhio gli HP è la base per non morire. E sui compagni ricordati di "
               "usare lo stetoscopio. Se sei alle strette, con la capacità Chiama famiglio "
               "puoi rimandarli a casa.")
# ⚠️ deroga 5: l'inglese aggiunge il Ripristino del corpo per gli SP.
RESE[14465] = ("Gli MP si recuperano con una pergamena o una bacchetta di mana, ma gli SP "
               "sono difficili da rimettere su. Un po' te ne torna da sé con la "
               "Rigenerazione, oppure li recuperi lanciando il ripristino del corpo. Come "
               "ultima risorsa, se hai un dio e la preghiera è carica, col tasto p ti "
               "riprendi tutti gli HP, gli MP e gli SP.")
RESE[14469] = ("Le alterazioni arrivano da tante cose, ma in combattimento quasi sempre "
               "vengono dagli attacchi elementali. Con poca resistenza, o prendendone "
               "tante, durano di più. Passano da sé col tempo, ma quasi tutte si tolgono "
               "sul colpo con un effetto di cura.")
# ⚠️ deroga 6: l'inglese aggiunge quali buff parano quali stati.
RESE[14470] = ("L'ideale sarebbe portare equipaggiamento con un incanto che le rende "
               "innocue; finché non ce l'hai, restano i buff che le prevengono. Per dire: "
               "l'Eroismo para paura e confusione, la Concentrazione para sonno e "
               "confusione.")
RESE[14471] = ("Rovesciando il discorso: se riesci tu a paralizzare o accecare un "
               "avversario, lo scontro diventa facile. Sui nemici col nome fra <> o {} non "
               "funziona quasi mai, ma sugli altri funziona al primo colpo: è un modo "
               "sicuro di metterli fuori gioco.")
RESE[14475] = "Eeeh!?"
RESE[14477] = "È... è un segreto..."

# ============ le risposte del quarto incontro ============

RESE[14480] = ("Certi tipi di nemici, come i pipistrelli, hanno una schivata altissima per "
               "razza: i colpi normali li scansano quasi tutti, quindi usa la magia o le "
               "capacità.")
RESE[14481] = ("Puoi anche menare finché non lo prendi, ma in uno scontro serio quel tempo "
               "non ce l'hai. Le capacità e gli incantesimi non sbagliano mai un colpo: usa "
               "quelli. E naturalmente un nemico addormentato non schiva...")
RESE[14485] = ("Certi tipi di nemici, come i paguri, sono quasi immuni agli attacchi "
               "fisici. Le magie di chi lancia incantesimi, però, quelle difese le passano "
               "come niente.")
# ⚠️ deroga 8: il nome dell'incanto sta in `item_data.hsp:677`.
RESE[14486] = ("Se piazzi un colpo che perfora, gran parte della difesa salta; ma perché "
               "capiti ci vuole addosso l'incanto dell'attacco che perfora sempre. E ci "
               "sono anche magie e pozioni da tirare per indebolire la difesa del nemico.")
RESE[14490] = ("Ti capiterà di trovarti davanti a uno che si cura ogni volta che sta per "
               "cadere. Contro un tipo così serve la Furia, che raddoppia il danno che fai "
               "e quello che prendi. La Furia la dai alla tua squadra con la capacità Furia "
               "collettiva, e la appiccichi al nemico tirandogli un pomodoro. ...Ci sei "
               "arrivato?")
RESE[14491] = ("Anche non lasciargli il turno funziona: così hai il tempo di rimetterti in "
               "sesto. I nemici col nome fra <> o {} alle alterazioni resistono parecchio, "
               "quindi contro di loro conviene piuttosto alzare la tua velocità.")
RESE[14492] = ("Lo sai che, quando la barra di potenza sotto gli HP arriva al 100%, con la "
               "<Forza liberata> sferri un colpo potentissimo? E che i compagni in Assalto "
               "la usano, mentre quelli in Intercettazione no? Vuol dire che, usando la "
               "bandiera di comando al momento giusto, tutta la squadra può caricare e poi "
               "scaricare i colpi tutti insieme.")
RESE[14493] = ("Per finire: è una guerra lunga, ma con armi o capacità che assorbono MP "
               "puoi arrivare ad ammazzare un nemico prosciugandogli tutto il mana, perché "
               "il contraccolpo lo uccide. È una tattica che però va preparata prima.")
RESE[14497] = ("Gli oggetti che hai addosso li tiri col tasto T. È il Lancio a decidere come "
               "va, e tirando lo alleni. Pozioni, sfere dei mostri e altra roba si lanciano "
               "direttamente dallo zaino. Finché il Lancio non è buono, mettiti vicino al "
               "nemico prima di tirare.")
RESE[14498] = ("Tirare addosso una cosa pesante è utile in modi che non ti aspetti, perché "
               "passa la difesa. E ci sono anche oggetti con effetti speciali quando li "
               "lanci, come le castagne.")
RESE[14502] = ("Certi nemici sono coperti di spine e ti tagliano se li meni da vicino: "
               "contro quelli usa una magia o un attacco a distanza. C'è anche chi si "
               "difende allo stesso modo dalle magie, ma è roba rara.")
RESE[14503] = ("E poi ci sono nemici che al tiro rispondono subito con un tiro loro. Contro "
               "quelli basta metterli in condizione di non poter attaccare, con "
               "un'alterazione! Un contrattacco solo fa poco danno, ma si sommano: non "
               "combatterli alla leggera.")
# ⚠️ deroga 7: l'inglese aggiunge la reazione a catena delle rocce esplosive.
RESE[14507] = ("Certi nemici esplodono quando sono ridotti male, e di solito esplodono anche "
               "quando esplode qualcuno lì accanto. Quelle che si chiamano rocce esplosive "
               "compaiono in gruppo e possono innescare una catena enorme e micidiale. I "
               "nemici che esplodono affrontali da lontano; se non puoi, tirategli una "
               "pozione o bagnali con una magia d'acqua: bagnati non esplodono.")
RESE[14511] = ("Certi nemici, se li colpisci, si dividono in più nemici. Qualcuno di questi "
               "non si divide se ha addosso un'alterazione, ma non tutti. Puoi indebolirlo "
               "piano piano e poi finirlo con un colpo solo, oppure usare Crea muri, con "
               "una magia o una bacchetta, così non gli resta spazio per dividersi.")
RESE[14512] = ("Fra l'altro, i mostri nati dalla divisione di un altro non lasciano cadere "
               "niente e non danno esperienza: non vale la pena farli dividere apposta.")
RESE[14516] = ("Trovare un elmo o un anello che ti facciano vedere i nemici invisibili è "
               "importante; finché non ce l'hai, usa una pergamena o una magia di "
               "individuazione degli oggetti. Come rimedio provvisorio va bene.")
RESE[14517] = ("E poi, bagnandoli, i nemici invisibili si vedono per un po'. Puoi tirargli "
               "addosso delle pozioni da poco, oppure usare la magia d'acqua con un "
               "incantesimo o una bacchetta.")

RESE[14521] = "Chi ha domande venga pure a chiedere!"
