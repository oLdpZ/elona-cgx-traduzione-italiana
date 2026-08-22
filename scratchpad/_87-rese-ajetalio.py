# -*- coding: utf-8 -*-
"""Le rese di AJETALIO, docente del corso di vita quotidiana (chat.hsp
:13950-:14098), primo dei quattro conferenzieri del seminario.

Perimetro: 77 firme, **zona chiusa** (nessuna occorrenza fuori), meno le
**quattro righe morte** rinviate (`:13991`, `:14036`-`:14038`, vedi
`_87-rinvia-morte.py`): **73 rese**.

⭐ **I quattro docenti sono un SISTEMA, non quattro parlanti**, e i nomi dei
corsi si decidono qui una volta per tutte, perche' Ajetalio cita gli altri due
(`:14084`, `:14086`):

    生活講座  Ajetalio Lanclis, «Ajira»   -> corso di vita quotidiana
    道具講座  Cresce Lucan                -> corso sugli oggetti
    育成講座  Iduru Gumbye, «il maestro»  -> corso di crescita
    戦闘講座  Mito Lydian, «Mitorin»      -> corso di combattimento

REGISTRO. Ajetalio parla a una classe in forma cortese (です/ます) e di se'
dice 僕. In italiano: **apertura e chiusura al plurale** (sta davanti a tutti:
«chiamatemi pure Ajira», «chi ha altre domande venga») e **spiegazioni al
singolare**, che e' la forma con cui il gioco parla al giocatore dappertutto.
⚠️ Il suo genere e' fissato dal dizionario — «<Ajetalio> il docente»
(`db_creature.hsp:55066`) — quindi «il mio piatto preferito» a `:14029` puo'
accordarsi; il GIOCATORE no, mai.

LESSICO, tutto ripreso e non deciso:
  incarico (`text.hsp:11875`), bacheca (`db_item.hsp:151223`), baule degli
  stipendi (`:145309`), diario e «tasto j» (`chat.hsp:1664`), Ambasciata di
  Palmia (`text.hsp:2830`), Terra di Tregua (`:2788`), altare (`db_item:150479`),
  Fede / Cucina / Scavo / Pesca / Esibizione / Giardinaggio / Anatomia /
  Trattativa / Carisma (`skill.hsp`), Predica (`skill.hsp:1348`), capacita' ad
  area (`command.hsp:5673`), incarnazione (`db_race.hsp:5553`), tesoro segreto
  (`db_item.hsp:143525`), noce di Api / castagna / foglia salutare / erba
  selvatica commestibile (`db_item`), cibo da viaggio (`:148280`), frigo
  portatile (`:143972`), tasca quadridimensionale (`skill.hsp:774`), frullatore
  (`db_item.hsp:138450`), stetoscopio (`:146254`), antisettico (`:139775`),
  salvadanaio (`:144872`), moneta di platino / di bronzo, pergamena
  (`text.hsp:188`), armeria (`map_user.hsp:334`), mercato nero (`text.hsp:456`),
  emporio (`text.hsp:428`), campo (`db_item.hsp:145378`), allevamento
  (`text.hsp:2821`), proprieta' (`map_user.hsp:39`), rango (`chat.hsp:25597`),
  <Forza liberata> (`custom_tweaks.hsp:1255`), Ragnatela / Nebbia d'oscurita' /
  Terreno acido / Crea muri (`skill.hsp`), malattia dell'etere, il riccio
  splendente, il fuoco fatuo, il putit, lo scorpione, Derphy, Irva, Nefia (al
  plurale «le Nefie», `main.hsp:1174`), labirinto (`init.hsp:357`).

⭐ **Il lessico di una statistica si e' deciso guardando quante volte il gioco
lo dice**: 発言力 e' «autorita'» in otto siti (`chat.hsp:7032`, `:19563`,
`:23940`, `:24008`, `:24011`, `action.hsp:8506`...) e «Influenza» in **uno**
solo, `economy.hsp:357`. Il tutorial e' il posto dove il giocatore impara la
parola, quindi qui si dice «autorita'» e il sito solitario si rifa'.

⚠️ LE DEROGHE DICHIARATE

1. **`:13970`** — l'inglese non e' una frase («there was a punishment to pick
   up the fictional god by making up the imaginary god»). Si segue il
   giapponese: c'era chi non sapeva darsi una regola senza appoggiarsi a
   esistenze incerte, e c'erano gli empi che inventavano divinita' per spremere
   soldi alla gente.
2. **`:13972`** — l'inglese chiude con «you'll be rewarded in due course» e
   perde COME si fa l'offerta (`Enter` sull'altare, con le cose che al dio
   piacciono). E' l'istruzione, e senza di quella `:13973` non ha causa.
3. **`:13973`** — l'inglese apre con una battuta che nel giapponese non c'e'
   («When in danger, pray and you'll be rescued») e mette la ricompensa in
   coda. Il giapponese dice quel che serve: arrivato l'annuncio, si prega e la
   ricompensa scende. Le tre soglie (15/25/40) coincidono nei due rami.
4. **`:14084`, `:14086`** — l'inglese taglia le due battute in cui Ajetalio si
   accorge di essere sconfinato nel corso di un collega («...これは育成講座の
   分野ですかね？», «...っと。これは道具講座の分野ですね»). Sono la voce del
   personaggio e l'unico punto in cui i quattro corsi si nominano fra loro.
5. **`:14085`** — l'inglese sfalsa la meccanica: dice «a +10 weapon is at least
   five times stronger, and each + on everything else makes you more durable»,
   mentre il giapponese dice che a pesare sulla <Forza liberata> e' la **media
   dei +** di tutto l'equipaggiamento, e che a media +10 il danno arriva a
   cinque volte tanto. E' un'istruzione, e il numero e' lo stesso.
6. **`:13998`** — l'inglese generalizza la voce di menu («Could you tell me
   about altars?») dove il giapponese chiede la cosa precisa a cui la risposta
   risponde: 祭壇がなくなったら？, «e se sparisce un altare?».
7. **`:14007`** — «If I become rich» darebbe un genere al giocatore. La voce
   passa dalla persona alla cosa: «E se i soldi mi avanzano?».

⚠️ **`:13961` e `:14020` hanno lo STESSO giapponese e due inglesi diversi** —
uno dice «If you have food to spare, feed them», l'altro «you should eat high
quality food», che e' un errore di lettura del 与えたほうが. Si rendono con la
**stessa** riga italiana: sono due firme, ma una battuta sola, e cosi'
`battute --divergenti` resta a 13.
"""

RESE = {}

# ============ primo incontro: procurarsi da mangiare ============

RESE[13954] = ("Sono Ajetalio Lanclis, docente del corso di vita quotidiana. Il nome è "
               "lungo: chiamatemi pure Ajira. Benvenuti a tutti, e buon lavoro.")
RESE[13955] = ("Cominciamo dal principio dei principi dell'avventura: come ci si procura "
               "da mangiare.")
RESE[13956] = ("Le prime volte, fuori dalla città, entra nei campi con Enter e raccogli le "
               "noci di Api, le castagne e le foglie salutari che stanno per terra: non "
               "marciscono e pesano poco, quindi vanno bene sia da portarsi dietro sia da "
               "mettere via. Ci sono anche le erbe selvatiche commestibili, ma attenzione: "
               "quelle in due giorni marciscono. Anche i fiori si mangiano, però "
               "si vendono a buon prezzo: conviene venderli.")
RESE[13957] = ("Poi ci sono gli alberi da frutto: col tasto b li sfondi e la frutta cade. "
               "Secondo il tipo può pesare parecchio, e in mezza giornata marcisce, quindi "
               "consumala presto. Piuttosto che lasciarla marcire, posala per terra e falla "
               "mangiare ai compagni.")
RESE[13958] = ("Ah, giusto. Quando raccogli cibo là fuori, occhio agli animali selvatici. "
               "Se incontri qualcosa che sembra forte, o che forte lo è davvero, esci "
               "dall'area senza insistere: rientrando ne trovi dell'altro quante volte "
               "vuoi, quindi non farti accecare dal boccone che hai davanti.")
RESE[13959] = ("Per le spedizioni lunghe puoi anche fare scorta di cibo da viaggio alla "
               "locanda. Riempie lo stomaco e basta, non rende più forti, ma è sempre "
               "meglio che morire di fame. Un avventuriero esperto sa preparare cibo "
               "nutriente che non marcisce, e poi c'è l'antisettico, che il marciume lo "
               "ferma... ma sono tutt'e due fuori portata per chi comincia: tienili a mente "
               "per più avanti.")
RESE[13960] = ("Se ti viene fame in città... in certe città trovi pane appoggiato in giro e "
               "ortaggi piantati. È maleducazione, ma quando la fame è tanta mangiali di "
               "nascosto. E anche nella città più spoglia, se c'è una locanda da mangiare "
               "te lo danno. A pagamento, e senza rinforzarti.")
# ⚠️ stessa riga di `:14020`: stesso giapponese, due inglesi.
RESE[13961] = ("Ah, i compagni: dal padrone ricevono l'energia vitale che basta a tenerli in "
               "piedi, quindi finché non vomitano troppo di fame non muoiono. Detto questo, "
               "se li visiti con lo stetoscopio e vedi verde-azzurro, vuol dire che hanno la "
               "pancia vuota. Se di cibo ne hai d'avanzo, daglielo: mangiando si "
               "rinforzano.")

# ============ secondo incontro: incarichi, stipendio, tasse ============

RESE[13964] = "Oggi impariamo qualcosa sugli incarichi di città e dintorni."
RESE[13965] = ("Se tocchi la bacheca della città, ti accorgi che di incarichi ce n'è di ogni "
               "genere. Portandoli a termine ottieni oggetti, monete di platino, monete "
               "d'oro, fama, autorità, karma. Se invece fallisci, la fama cala; e con certi "
               "incarichi cala anche il karma, il che è pericoloso, quindi non accettarli a "
               "casaccio fin dal primo giorno.")
RESE[13966] = ("Parliamo anche di stipendio e tasse. Il primo e il quindici di ogni mese, "
               "stipendio e rifornimenti arrivano nel baule degli stipendi di casa tua. Pare "
               "che, se non sei indietro con le tasse, i rifornimenti siano di qualità "
               "migliore. E lo stipendio dipende dalle varie classifiche degli avventurieri: "
               "le classifiche si guardano nel diario, col tasto j.")
RESE[13967] = ("Poi, passato il primo gennaio, il primo di ogni mese insieme allo stipendio "
               "ti arriva anche la cartella delle tasse. Si paga portandola all'Ambasciata "
               "di Palmia, che sta a est di qui. Le tasse si calcolano sul denaro che porti "
               "addosso e sulle proprietà che hai. Anche se hai in mente di vivere da "
               "farabutto, all'inizio pagale ogni mese: con quattro mesi di arretrato perdi "
               "sessanta punti karma.")

# ============ terzo incontro: la fede ============

# ⚠️ deroga 1: l'inglese non e' una frase; si segue il giapponese.
RESE[13970] = ("Questa volta vi spiego la fede. Nell'epoca in cui le divinità quasi non "
               "intervenivano pare ci fosse chi non sapeva darsi una regola se non "
               "appoggiandosi a esistenze di cui nessuno sapeva niente, e c'erano pure gli "
               "empi che si inventavano un dio per spremere soldi alla gente. L'Irva di "
               "oggi, invece, è retta da otto divinità che esistono di sicuro.")
RESE[13971] = ("Credere in un dio e fargli offerte porta benefici concreti e sicuri: "
               "attributi e abilità rinforzati, poteri speciali, l'incarnazione del dio, "
               "tesori segreti, armi. Se non hai deciso in cuor tuo di non appoggiarti a "
               "nessun dio, tanto vale che per il momento tu ne segua uno.")
# ⚠️ deroga 2: l'inglese perde COME si fa l'offerta.
RESE[13972] = ("Per scegliere un dio, il posto giusto è la Terra di Tregua, a nord di "
               "Palmia, cioè a nord-est di questo seminario. Sali su un altare e premi il "
               "tasto p: vedi le informazioni di quel dio e poi decidi se seguirlo o no. "
               "Quando lo segui, offrigli sull'altare, con Enter, le cose che gli piacciono: "
               "prima o poi arriverà l'annuncio di una ricompensa.")
# ⚠️ deroga 3: l'inglese apre con una battuta che il giapponese non ha.
RESE[13973] = ("Arrivato l'annuncio, prega e la ricompensa scende dal cielo. Certo, "
               "l'incarnazione del dio vuole almeno 15 di Fede, il tesoro segreto 25 e "
               "l'arma 40.")

# ============ quarto incontro: mettere in piedi un sostentamento ============

RESE[13976] = ("Bene, in questo quarto e ultimo incontro studiamo come si mette in piedi un "
               "sostentamento vero.")
RESE[13977] = ("Scendere nei labirinti a raccogliere monete d'oro non basta a campare. Di "
               "questi tempi, di solo labirinto ci campa giusto quel mostro di persona che "
               "si fa senza fatica labirinti da centinaia di livelli. E anche quel mostro, "
               "per arrivare a tanto, ha racimolato soldo su soldo. Quando arrivi a quella "
               "forza, di soldi non ne hai già più bisogno.")
RESE[13978] = ("Forse un giorno arriverai a tanto anche tu, ma per adesso conviene fare gli "
               "incarichi di città e mettere da parte i soldi per un negozio tuo. "
               "L'equipaggiamento venduto nel tuo negozio rende molto più di quanto ti "
               "darebbero i negozianti delle città.")
RESE[13979] = ("Quando apri un negozio, procurati anche un compagno con Carisma e Trattativa "
               "a cui affidare il banco. Un negozio solo basta e avanza, quindi è una "
               "proprietà da prendere presto. Più avanti, se ti va, con più negozi "
               "specializzati i guadagni salgono ancora.")
RESE[13980] = ("Insieme a questo, negli intervalli fra un'avventura e l'altra coltiva le "
               "abilità produttive: Scavo, Pesca, Esibizione, quelle che ti piacciono. "
               "Vendi quel che ne ricavi. Anche quando non hai la forza per andare a "
               "raccogliere oggetti in un labirinto, questa strada resta aperta.")

# ============ le voci di menu ============

RESE[13985] = "Che cosa non si può mangiare?"
RESE[13986] = "Che succede se ho fame?"
RESE[13987] = "Come si cucina?"
RESE[13988] = "Ajira, il tuo cibo preferito?"
RESE[13992] = "Che tipi di Nefia ci sono?"
RESE[13993] = "Che succede se cala il karma?"
RESE[13994] = "Che cos'è l'autorità?"
RESE[13995] = "E se in città succede il finimondo?"
# ⚠️ deroga 6: l'inglese generalizza, il giapponese chiede quel che la risposta risponde.
RESE[13998] = "E se sparisce un altare?"
RESE[13999] = "Come si alza la Fede?"
RESE[14000] = "Che dio mi consigli?"
RESE[14001] = "Ajira, la frangia ti è marcita?"
RESE[14004] = "Quali proprietà, oltre al negozio?"
RESE[14005] = "Mi spieghi il commercio?"
RESE[14006] = "Se ho qualche soldo in più?"
# ⚠️ deroga 7: «If I become rich» darebbe un genere al giocatore.
RESE[14007] = "E se i soldi mi avanzano?"

RESE[14009] = "Ci sono domande?"

# ============ le risposte del primo incontro ============

RESE[14012] = ("Bella domanda! Se mangi roba maledetta la vomiti, e il risultato è che la "
               "fame aumenta invece di passare; in certi casi si muore di fame sul colpo. "
               "Se una cosa è maledetta lo scopri identificandola, ma anche posandola "
               "davanti a un compagno affamato e guardando se ci si butta: per quanta fame "
               "abbia, il cibo maledetto un compagno non lo tocca.")
RESE[14013] = ("E se mangi roba marcia, gli attributi calano per sempre. C'è "
               "dell'equipaggiamento che permette di digerire anche il marcio, ma è meglio "
               "mettere il cibo nel frigo portatile o nella tasca quadridimensionale, così "
               "che non marcisca affatto.")
RESE[14014] = ("Attenzione però: certi pezzi di cadavere di non morti, anche se marci non "
               "sembrano, marci lo sono per natura. Le ossa vanno bene, ma il resto del "
               "cadavere è marcio.")
RESE[14015] = ("Poi: mangiare cadaveri di alieni e di altri parassiti te li fa venire "
               "addosso, mentre il riccio splendente e il fuoco fatuo fanno avanzare la "
               "malattia dell'etere. Ci sono cadaveri che fanno impazzire e cadaveri che "
               "avvelenano. Ti ho spaventato? Però ce ne sono anche di speciali: il putit e "
               "il cavallo danno esperienza agli attributi, lo scorpione e la fata danno "
               "resistenze elementali. Prepara le contromisure, prova un po' di tutto e "
               "impara.")
RESE[14019] = ("Si muore, ecco che succede. Di avventurieri che camminano senza accorgersi "
               "della fame e ci restano ce ne sono tanti. Dirai che nessuno è così sciocco, "
               "e invece capita spesso. Prima di arrivare alla fame nera, mettiti qualcosa "
               "nello stomaco. Durante un combattimento mangiare è difficile, quindi "
               "rifocillati quando puoi.")
# ⚠️ stessa riga di `:13961`.
RESE[14020] = RESE[13961]
RESE[14024] = ("Se hai l'abilità Cucina, con gli utensili da cucina puoi cucinare. Il cibo "
               "cucinato ci mette molto di più a marcire e rinforza molto di più, quindi è "
               "un'abilità che conviene avere. Secondo gli utensili c'è un limite a quanto "
               "può venire buono un piatto: guardane la scheda col tasto x.")
RESE[14025] = ("È un po' diverso dal cucinare, ma col frullatore puoi ridurre frutta e "
               "verdura in succo. Riempie poco lo stomaco, però in cambio nutre di più. E "
               "anche le cose maledette o marce diventano innocue e tornano utili.")
RESE[14029] = ("Eeeh... il mio piatto preferito? B-be', direi le erbe. Non marciscono, "
               "pesano poco e rinforzano corpo e mente. E unite a un piatto cucinato sono il "
               "massimo.")

# ============ le risposte del secondo incontro ============

RESE[14032] = ("In generale sono di due tipi: le Nefie casuali, che compaiono e spariscono "
               "coi movimenti della crosta terrestre, e quelle fisse, che non spariscono.")
RESE[14033] = ("Una Nefia casuale ha tre piani, e con la sconfitta del capo dell'ultimo "
               "piano la conquista è compiuta e il tesoro è tuo. Se scappi dall'ultimo piano "
               "prima di abbattere il capo, è un fallimento e quella Nefia non si può più "
               "fare. E in ogni piano che non sia il primo c'è sempre un punto dove sono "
               "ammucchiate monete d'oro. Sembra quasi che la Nefia stia adescando gli "
               "avventurieri, il che è inquietante... ma raccogliamole volentieri.")
RESE[14034] = ("Le Nefie fisse stanno sempre nello stesso posto. Quasi tutte hanno aspetto e "
               "nome propri, ed è da lì che le distingui da quelle casuali. Vanno dalle più "
               "corte, sui due piani, a quelle di quaranta piani e oltre. Alcune hanno "
               "regole o ambienti tutti loro.")
RESE[14035] = ("Le Nefie casuali sono di otto tipi, secondo le rovine da cui nascono. In "
               "ognuna si insediano razze diverse, quindi se cerchi un certo mostro conviene "
               "cercare il tipo di Nefia che gli corrisponde. Nelle Nefie fisse di solito "
               "c'è un miscuglio di razze, ma non sempre: una regola non si può dare.")
RESE[14042] = ("Sotto i -31 di karma sei un criminale ricercato. Le guardie della città ti "
               "si buttano addosso tutte insieme e i negozianti non ti vendono più niente. "
               "Finché non hai la forza per spazzare via una guardia e un modo per "
               "travestirti, muoviti con prudenza e non far calare troppo il karma.")
RESE[14043] = ("Se ti capita di diventare criminale senza volerlo, prendi come base Derphy, "
               "la città a sud-ovest di questo seminario, e rialza il karma con gli "
               "incarichi. A Derphy guardie non ce ne sono, e i negozi li puoi usare anche "
               "da criminale.")
RESE[14047] = ("L'autorità è la prova di quanto hai contribuito a una città. Parlando col "
               "suo amministratore o col suo capo, puoi spendere autorità per amministrare "
               "la città al posto loro. ...Detto fra noi, è un istituto appena nato e ci si "
               "fa ancora poco. Per adesso consideralo qualcosa che si accumula facendo gli "
               "incarichi.")
RESE[14051] = ("Grandi incendi in città, mostri che spuntano e cominciano il massacro: "
               "capita spesso. È una brutta cosa, ma è una cosa che capita. ...Ehm. Vi "
               "insegno come si spengono gli incendi e come si ferma la comparsa dei "
               "mostri.")
RESE[14052] = ("Prima gli incendi. Se il fuoco è uno o due, ci lanci sopra col tasto T "
               "(shift+t) una delle pozioni che hai e si spegne. Se qualcuno pesta la "
               "pozzanghera che hai fatto se la prende, quindi calpestala tu e falla "
               "sparire. Se i fuochi diventano quattro o cinque, usa magie o bacchette di "
               "Ragnatela, Nebbia d'oscurità o Terreno acido: spengono i fuochi di tutta "
               "l'area. Se non hai niente del genere, o l'incendio è ormai troppo esteso, il "
               "consiglio è di non avvicinarti a quella città fino a un giorno di pioggia.")
RESE[14053] = ("Poi, i mostri che spuntano. Quelli usciti bevendo da un pozzo finiscono lì: "
               "li abbatti e via. Ma a volte gira un avventuriero che porta addosso un "
               "equipaggiamento che evoca mostri all'infinito: in quel caso trova il "
               "colpevole e requisiscigli quell'equipaggiamento.")
RESE[14054] = ("Può anche succedere che parassiti come gli alieni escano dalla pancia della "
               "gente. Finché stanno dentro si eliminano del tutto bevendo veleno, tintura o "
               "acido solforico: se lo dai a chi è infestato, se lo beve senza storie. Anzi, "
               "se non glielo fai bere, finché l'ospite è vivo ne nascono all'infinito.")
RESE[14055] = ("Ci sono anche casi in cui i parassiti sono già nati troppi, o in cui i "
               "mostri evocano altri mostri, o si dividono e si moltiplicano. Se sono alla "
               "tua portata, chiudili con Crea muri e abbattili uno per uno. Se non ce la "
               "fai, scappa dalla città: torna a dare un'occhiata cinque giorni dopo e non "
               "ci dovrebbero essere più. Se ne resta ancora qualcuno, rimanda di qualche "
               "altro giorno.")

# ============ le risposte del terzo incontro ============

RESE[14059] = ("Facendo offerte sull'altare di un altro dio, puoi prendertelo e riscriverlo "
               "col tuo. Dà anche più devozione, ma attenzione: rischi di restare senza "
               "l'altare del dio che volevi seguire dopo! Poi per trovargliene un altro ti "
               "tocca setacciare le Nefie per giornate intere. Con gli altari della Terra di "
               "Tregua non scherzare, intesi?")
RESE[14063] = ("La Fede sale da sé, sentendo nei sogni la grandezza del dio. E se sali di "
               "livello con Fede 10 o più, impari la Predica, che è una capacità ad area. "
               "Se con la Predica riesci a soddisfare il pubblico, la Fede la fai salire "
               "quando vuoi tu.")
RESE[14067] = ("All'inizio vanno bene Opatos e Jure, che hanno offerte facili e rinforzano "
               "la sopravvivenza, e Yacatect, che dà una mano col sostentamento. Mani, "
               "Lulwy e Itzpalt diventano facili quando hai i soldi per comprare a bracciate "
               "gli oggetti da offrire. Ehekatl conviene dopo che sai pescare, Kumiromi dopo "
               "che sai coltivare e hai un campo.")
RESE[14068] = ("Molti avventurieri seguono più divinità per raccoglierne le ricompense, e "
               "solo dopo decidono la fede definitiva; e c'è pure chi le completa tutte e "
               "otto. Ogni divinità ha poteri e carattere ben suoi, quindi alla fine "
               "conviene scegliere quella che si intona al tuo stile. Poi certo, si può "
               "scegliere anche per simpatia.")
RESE[14072] = "...Questa è moda. Non è marcia né scolorita."

# ============ le risposte del quarto incontro ============

RESE[14075] = ("Oltre al negozio, le proprietà buone sono il campo e l'allevamento. Il primo "
               "vuole Giardinaggio, il secondo Anatomia, ma tutt'e due danno una bella "
               "entrata. Il campo soprattutto: con abbastanza Giardinaggio ci coltivi anche "
               "le erbe.")
RESE[14079] = ("Per commerciare servono le merci da commercio, che si vendono solo negli "
               "empori sparsi qua e là. Sono gli oggetti da carretto, tutti tranne il cibo "
               "da viaggio, e viaggiano nel carretto. Ogni città ha merci che costano poco e "
               "merci che costano tanto: carichi il carretto fino al limite, porti la merce "
               "in un'altra città e guadagni sulla differenza. Se le merci te le fabbrichi "
               "con gli attrezzi, o le strappi ai briganti, il guadagno sale ancora.")
RESE[14080] = ("Però campare di solo commercio è dura. Le spese di tutti i giorni le copri "
               "senza problemi, ma in fondo è una cosa da fare insieme al resto, mentre giri "
               "da una città all'altra. E poi, quando vendi merci che vengono da lontano, "
               "l'economia della città si ravviva in proporzione e per un po' anche gli "
               "altri negozi hanno più roba: si può commerciare anche solo per quello.")
# ⚠️ deroga 4: l'inglese taglia la battuta sul corso del collega.
RESE[14084] = ("Se di soldi ne hai d'avanzo, le monete d'oro per terra lascia che le "
               "raccolgano i compagni invece di raccoglierle tu: così se ne vanno ad "
               "allenarsi per conto loro. ...Ma questa è materia del corso di crescita, mi "
               "sa?")
# ⚠️ deroga 5: l'inglese sfalsa la meccanica della <Forza liberata>.
RESE[14085] = ("Poi c'è da rinforzare l'equipaggiamento, per alzarne le prestazioni. Fino a "
               "+6 ci arrivi con le pergamene apposite, ma in armeria si arriva a +10. Su "
               "un'armatura che per adesso ti va bene non lesinare: rinforzata, più avanti "
               "diventa preziosa da passare ai compagni. E poi la media dei + di quel che "
               "hai addosso pesa sulla potenza della <Forza liberata>, la tecnica della "
               "barra: con una media di +10 il danno arriva a cinque volte tanto e oltre. "
               "Ricordatelo.")
# ⚠️ deroga 4: come `:14084`.
RESE[14086] = ("...Ecco, e questa è materia del corso sugli oggetti. Il punto è che i soldi "
               "non servono solo a campare: entrano anche in tutti i modi di farsi più "
               "forte. Spendili senza rimpianti, che se prima ti costruisci una base di "
               "entrate stabile, poi li rifai.")
RESE[14090] = ("Quando i soldi ti avanzano, investi nei negozi che usi spesso. Se investi in "
               "negozi che hai invitato a casa tua, puoi anche traslocare senza restare "
               "legato a una città sola. Investire migliora qualità e quantità della roba "
               "trattata. Un rango di 150 basta e avanza.")
RESE[14091] = ("E se avanzano ancora? Mah... prendi altri compagni, oppure investi ancora in "
               "qualche armeria o nel mercato nero? Se proprio non hai niente da farci, "
               "mettili nel salvadanaio: sul denaro che porti addosso ti crescono solo le "
               "tasse.")

RESE[14095] = "Allora, chi ha altre domande venga pure a chiedermele di persona."
