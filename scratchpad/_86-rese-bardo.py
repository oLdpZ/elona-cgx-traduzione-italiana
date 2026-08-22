# -*- coding: utf-8 -*-
"""Le rese di otto blocchi chiusi di `*chat_unique` (chat.hsp :7114-:7430,
:7597-:7644, :8253-:8308): 61 firme, nessuna con occorrenze fuori.

    :7114  MEFAN la pifferaia — il pifferaio di Hamelin, e i bambini    9
    :7270  ORPHE il seguace del caos — l'Irregolare                     3
    :7277  CAIM il riccone folle — otto monologhi di puro nonsenso     11
    :7320  SNAIL il pilota di androidi                                  2
    :7330  il PULITORE riconciliato                                     2
    :7340  il GERMOGLIO DI BAMBÙ — funghi, koala, Suginoko             16
    :7597  GUO il mercante fallito — la villa e il terreno             10
    :8253  NAPLUS l'alchimista — la coda di Estork                      8

Sessi letti in `db_creature.hsp`, non negli epiteti: MEFAN `CDATA_SEX = 1`
(femmina, e infatti «la pifferaia»), NAPLUS 1, GUO 0, CAIM 0.

Lessico ereditato: «<Mefan> la pifferaia», «<Caim> il riccone folle»,
«<Naplus> l'alchimista», «il mercante fallito <Guo>», «<Estork> la bianca
fiamma» (`db_card.hsp`); «germogli di bambù» e «funghi» (`chat.hsp:7394`, gia'
reso), «koala» (`db_card.hsp`), «Suginoko» (`map.hsp:8017`), «la Foresta del
Dio Cane» (`text.hsp:3030`), «il patto eterno» (`chat.hsp:10206`, `:15457`),
«il Libro della Verità» (`main.hsp:5181`), «la Foresta Eretica»
(`chat.hsp:1600`), «Irregolare» (glossario: la forma in -e non ha genere).

⚠️ Il diario del giocatore e' un VINCOLO: `text.hsp:11071` dice gia'
«<Naplus>, a Eirel, mi ha chiesto di portarle la coda di <Estork>, che vive
nella Foresta del Dio Cane».

⚠️ CAIM e' nonsenso VOLUTO: l'inglese di monte e' gia' una resa del nonsenso
giapponese, e si segue quello. Le sue battute non vanno «aggiustate».
"""

RESE = {}

# --- MEFAN la pifferaia
RESE[7117] = "D'accordo"
RESE[7118] = "Rifiuto"
RESE[7119] = ("Oh... viandante, non è che ascolti i miei lamenti? Un tempo questa città fu invasa da "
              "un'infinità di topi, e a ricevere l'incarico di sterminarli fui io. Con una splendida "
              "esecuzione di questo flauto ho ripulito quei sudici ratti... e questa gente non mi ha "
              "pagata! Ah, a parlarne mi torna la rabbia. Per vendetta, vammi a rapire qualche "
              "bambino di questa città.")
RESE[7122] = "Ah, ecco. E allora crepa!"
RESE[7126] = ("Hai capito, dunque! Ah, giusto: ho detto i bambini di questa città, ma a questo punto "
              "vanno bene quelli di qualunque città. Conto su di te.")
RESE[7131] = "Lasciar dire"
RESE[7134] = '"(Consegnare " + cdatan(CDATAN_NAME, rc) + ")"'
RESE[7136] = ("Portamene quanti più puoi. A questa gente farò rimpiangere di avermi preso in giro.")
# ⚠️ 「いい子だ」 e' rivolto al bambino rapito, che non ha sesso noto: la resa
# passa dal nome comune femminile «creatura», che vale per chiunque.
RESE[7169] = ("Vieni qui, creatura... così, brava. D'ora in poi ti farò sentire esecuzioni "
              "meravigliose tutti i giorni... Mh? Sei ancora qui? Ecco il compenso. Prendilo.")

# --- ORPHE il seguace del caos
RESE[7272] = ("Oh, ce l'hai fatta fin qui! Ma di qui in avanti non ti lascio passare. La tua "
              "avventura finiva quando hai portato via da Lesimas il Libro della Verità: qui non "
              "dovevi mettere piede mai più.")
RESE[7273] = (" (Il giovane scuote il capo con aria rassegnata) All'inizio ci hai anche divertiti, "
              "tu che fai sempre il contrario di quel che prevediamo... ma a quanto pare tu sei "
              "Irregolare. La strega della Foresta Eretica... doveva bruciare insieme al bosco e "
              "morire, e il contatto con te le ha cambiato il destino. Se ti lasciamo fare, rischi "
              "di interferire perfino col patto eterno.")
RESE[7274] = ("Anche il nostro re è di pessimo umore. Qui il caos ti inghiottirà, e sparirai.")

# --- CAIM il riccone folle: nonsenso voluto, si segue l'inglese
RESE[7280] = "Tutto a posto, sono tornato in me!"
RESE[7283] = ("E il motivo è che anche quella cassetta della posta è rossa, ed è per via dei raggi "
              "infiniti che piovono dal cosmo che il mio corpo si sbriciola in ogni sua parte. È "
              "preoccupante: se uno non si accorge dell'ovvio, che il ferro e il ferro non sono la "
              "stessa cosa, come fa a sostenere di capire un vaso da fiori? Però che questa guerra "
              "sia una cosa magnifica è un'opinione che ogni tanto sento dalle formiche soldato. "
              "Comunque sia, che dopo la fine restino pensieri romantici non ci si può fare "
              "niente... Perciò oggi sono di ottimo umore! È un paradiso messo a testa in giù!")
RESE[7286] = ("Era prevedibile. Del resto, anche quel che fino a un attimo fa sembrava un vaso, "
              "a fissarlo si attorciglia in un futon. Piangeva anche quel Rudolf. Vuoi sapere che "
              "ne è stato del corpo di Rudolf? Ai tempi in cui la fazione del fil di ferro e quella "
              "dei funghi andavano d'accordo... Un giorno, deciso che le teste andavano sepolte "
              "sottoterra, più o meno quando il pomodoro cominciava a pensare di germogliare... "
              "successe il fatto. L'esplosione sparse le camelie, e con le vongole rosse e blu già "
              "pronte, la rovina calò sul mondo degli scarabei. Ah, "
              "ormai è tardi per fermarsi, anche esaurite tutte le scelte... Era tutto falso, eheh.")
RESE[7289] = ("Lasciamelo dire... La seconda forma del mio tsuchinoko è in fin di vita, e mi strappo "
              "i capelli. Ah, capisco... Sì, è così. L'orologio non si tocca, "
              "eh... Il sentimento lo capisco, ma piantare sul soffitto l'antenna staccata non mi "
              "pare una buona idea. Di sicuro l'asciugacapelli prende il sole là! Pare che poco fa "
              "l'abbia bruciato io! Ma affamando 2 attraverserà 4 e guarderà 1. È... una cosa "
              "vuota. Ecco, ripensiamoci da capo. Persa questa, non ci saranno altre occasioni di "
              "raccogliere i pensieri! Rifletti: arrivare fin lì non serve a nessuno! Ah. A "
              "proposito, il parcheggio è macho, vero? Mi torna in mente il tofu alle mandorle.")
RESE[7292] = ("Sì, le onde inghiottono tutto. E poi compaiono il cavolo, la carota, la melanzana e "
              "pesci di tutti i colori come il pastore... Come andrà a finire questa battaglia? "
              "Guardando il cielo dell'altro ieri prevedevo un acquazzone, e invece alla fine pare "
              "sia una balista! ...Quello che preoccupa resta comunque il gruppo dei porcellini di "
              "terra. Allora oggi assaggeremo un piatto di porcellini di terra. Mitarashi dango, "
              "prego. Ah... Non dirmi che ti metti a piangere? Quante volte hai detto che non "
              "avresti pianto, bugiardo! Lo so che lo sai anche tu! Detto fra noi, però, con la "
              "porta ti devi riconciliare. Scusa, è tutto per l'armonia col cloroformio... Che "
              "emozione!")
RESE[7295] = ("Una cosa simile è già successa... È una storia di prima che i mari si "
              "prosciugassero e le stelle convergessero nell'infinito. Due vermi d'oro si "
              "gettarono nell'aria rovente. Ecco. La storia è tutta qui... Non può finire lì? Così "
              "non va bene! La causalità non si prende in giro! Ah, ma forse va bene lo stesso. "
              "Volevo solo tirarti dalla mia parte. E allora... dopo aver chiesto e richiesto alle "
              "bombe che bollivano \\\"Fa male?\\\", non hanno vomitato tutti verso il cielo? È una "
              "parte importante di questa recita. Grazie di tutto per oggi.")
RESE[7298] = ("Ecco una storia famosa. Quando Koruchien scoprì per primo il punto di rilascio, il "
              "barone Troubatsu morì per difficoltà respiratorie a causa della maschera. Aveva 57 "
              "anni... Credi davvero che sarei morto per così poco? Beh, conta quanto il bulbo "
              "oculare di una pila. Adesso l'importante è pagina 144. La parola chiave è il ruggito "
              "dell'orso spaziale, ma del contenuto non devi curarti. Eh? Di che stavo parlando? "
              "Ah, giusto. Ero appena caduto dalla rupe e avevo avuto con loro un commovente "
              "ricongiungimento. Ho rimbalzato un po', ma sono sopravvissuto. Il vincitore sono io. "
              "Magnifico.")
RESE[7301] = ("Che io sia ridotto così è cominciato tutto da una sola storia commovente. Gli uomini "
              "senza respirare non vivono. Ma sarà poi vero? Forse è solo un'impressione che ti dà "
              "qualcosa di grande che avvolge il mondo. Un premio ci sarebbe stato, ma la storia ha "
              "preso una deviazione e lui è diventato un cactus. Costava anche parecchio! Quanto "
              "sono sciocchi gli uomini... Alla fine Rudolf esclamò \\\"Un momento, perché tutti "
              "portano addosso la pelle dei vermi assassini?\\\". E poi morì. Lo disse anche la "
              "figlia. E poi morì. E tu? Lo dirai? È un trucco, faresti meglio a protestare! "
              "Esatto! Qui non c'è niente...")
RESE[7306] = ("A dire il vero finora l'ho tenuto segreto, ma sale e pepe la devono piantare una "
              "buona volta! Comunque sono tre punti, ma non ti sembra che fare un pisolino per il "
              "mio bene e per il bene del mondo non abbia senso? Un dilettante magari si metterebbe "
              "a discutere a vuoto della fine del mondo, ma questo e quello sono due fenomeni "
              "diversi. A dirla tutta, i fenomeni sono il mio cibo preferito! Se hai ancora "
              "qualcosa da ridire, l'unica soluzione è rivolgersi all'egoismo riunito del mondo "
              "intero e perdere! Combatti! Getta le armi e arrenditi! Ti abbiamo circondato da ogni "
              "lato, ma un coniglietto che saltella è pur sempre carino!")
RESE[7310] = "(Non si capisce perché, ma ha ferite gravi su tutto il corpo...)"
RESE[7311] = "Qualcosa cade dalle mani di Caim."

# --- SNAIL il pilota di androidi
RESE[7323] = ("Gli stati di Irva si sono uniti solo per difendersi ciascuno da una minaccia. Finché "
              "non verrà il giorno in cui i paesi si riconcilieranno davvero, la nostra battaglia "
              "va avanti.")
RESE[7326] = "Secondo me è ora che gli Yerles e Juere facciano pace."

# --- il PULITORE riconciliato
RESE[7333] = ("Devo allenare la velocità, per stare dietro all'androide col propulsore. Non "
              "sopporto l'idea di essere di peso.")
RESE[7336] = "Nell'amore il sesso e la razza non c'entrano niente, vero?"

# --- il GERMOGLIO DI BAMBÙ
RESE[7343] = ("La guerra contro la forza schiacciante dei koala... è stata una dura lotta per "
              "sopravvivere. I koala rimasti... i conti con i funghi... la ricostruzione del "
              "villaggio... i problemi si accumulano. Ma per adesso godiamoci questa pace di un "
              "momento...")
RESE[7347] = ("Respingere i koala in quel numero: sei in gamba davvero! È una cosa di cui andare "
              "fieri. Tu hai difeso la luce di questa terra e i profughi. E ci hai mostrato una forza "
              "che non cede al buio della disperazione. Questo è il mio ringraziamento... accettalo.")
RESE[7359] = "Ma no, non fare complimenti. L'ho recuperata tutta fra le rovine di Suginoko."
RESE[7364] = ("Con i koala, a differenza dei funghi, non ci si ragiona nemmeno. Bruciano la terra "
              "con fiamme oscure e ne fanno terra bruciata oscura. I semi oscuri sparsi su quella "
              "terra coprono la luce intorno e crescono in alberi oscuri. La zona avvolta dal buio "
              "diventa così una terra oscura dove piante e animali normali non crescono più. Gli "
              "alberi oscuri fioriscono e fanno frutti, e tutto diventa cibo per i koala. Quando "
              "sono abbastanza, una parte parte in marcia per crearsi un nuovo pascolo, e tutto "
              "ricomincia da capo!! E il buio si prende ogni cosa...")
RESE[7369] = ("Brutta storia. Il villaggio alleato dei suginoko, che teneva testa ai koala a costo "
              "della vita, non dà più notizie... Che tocchi anche a noi è solo questione di tempo.")
RESE[7372] = ("I koala sono nemici che con i funghi non hanno niente da spartire! Ma con la tua "
              "forza dovresti riuscire a fermarli. Ti prego...! Se va avanti così, tutta la zona "
              "diventa una fattoria di materia oscura a furia di agricoltura bruciata oscura...")
RESE[7375] = ("Almeno i profughi sarebbe meglio farli scappare, no? Anche se non so proprio dove "
              "potremmo andare...")
RESE[7378] = ('"Ti lascio fuori le solite scale magiche... da lì puoi entrare. Conto su di te, " + '
              'cdatan(CDATAN_NAME, CHARA_PLAYER) + "! Sei la nostra ultima speranza!!"')
RESE[7386] = "Corre voce che verso questa terra stia marciando un'orda di koala."
RESE[7387] = ("Quelli sono pericolosi. Forti, certo, ma soprattutto hanno l'aria carina e dentro "
              "sono neri come la pece... Ci tocca aspettare che i koala ci travolgano...?")
RESE[7397] = "Sparisci, prima che ti prenda a calci."
RESE[7401] = ("Grazie. Si vede che dalla parte dei germogli di bambù c'è solo brava gente. I funghi "
              "sono così stupidi che le scale magiche dell'invasione le hanno lasciate lì. Entra "
              "da quelle!")
RESE[7407] = ("Eh? Vuoi sapere come fanno funghi e germogli di bambù a spostarsi? Non ci hai mai "
              "visti camminare? Piuttosto sbrigati a sterminare i funghi della montagna.")
RESE[7423] = ("Li hai distrutti, i funghi della montagna! Finalmente... finalmente abbiamo vinto la "
              "guerra fra germogli di bambù e funghi che durava da prima della storia. E però... "
              "che cos'è questo vuoto...?")
RESE[7424] = ("Noi... li abbiamo sempre odiati e detestati, e non abbiamo pensato ad altro che a "
              "combattere. Ma era un errore, di sicuro. Se prima di distruggerli ci fossimo fatti "
              "avanti a parlare, forse potevamo anche riconciliarci...")
RESE[7425] = "Vabbè, ormai sono distrutti e non ci si può far niente."

# --- GUO il mercante fallito
RESE[7601] = "Comprare il terreno"
RESE[7604] = ("Oh, sei tu. Detto fra noi, avrei un bel terreno: non lo compri? È in disordine, ma è "
              "tanto grande che ci puoi lasciare liberi quanti animali vuoi. E per giunta non ci "
              "paghi le tasse! Costa la bellezza di 300.000 monete d'oro! Allora? Lo compri, no?")
RESE[7607] = "Sciò, sciò, che la miseria si attacca."
RESE[7612] = ("Ecco il documento: mettilo dove ti pare. Di terreni così ne ho altri, quindi quando "
              "te ne serve un altro torna a comprarlo!")
RESE[7619] = "Cucucù... poveracci. Gli faccio rimpiangere di avermi preso in giro."
RESE[7622] = ("Maledizione! Maledizione! Tutti quanti... Fanno finta di compatirmi, ma dietro mi "
              "sfottono di sicuro! Vi faccio vedere io, morti di fame... appena vendo la villa e "
              "mi entra del denaro...")
RESE[7625] = "Comprare la villa"
RESE[7628] = ("Ooooh!? Denaro! È denaro! Mi compri la villa!? ...Uhm... di listino farebbe 2.400.000 "
              "monete d'oro, ma te la lascio a 2.000.000. E ringrazia.")
RESE[7631] = "Sciò, sciò. Io e un morto di fame come te siamo diversi in sostanza."
RESE[7636] = "Il denaro l'ho preso. Quella villa adesso è tua. Fanne quel che vuoi."

# --- NAPLUS l'alchimista
RESE[8259] = ("Hiii!? Q-quello è... un puf-puf... n-nooooo! T-ti prego, mettilo via subito!!!")
RESE[8265] = ("La prossima volta che vado a raccogliere materiali in una Nefia, fatti assumere come "
              "guardia del corpo. Ogni tanto ci scappa qualche oggetto che ho sintetizzato, o un "
              "servizio, eh?")
RESE[8269] = "È la coda di Estork! Ora supero la maestra...!"
RESE[8279] = ("Ah, il compenso, non te l'ho ancora dato. Sono oggetti che ho sintetizzato tempo fa: "
              "provali!")
RESE[8296] = "Non voglio forzarti, ma dai una mano: è per il progresso dell'alchimia!"
RESE[8300] = "Questo è l'atelier di Naplus♪ Mi fai un favore?"
RESE[8301] = ("C'è un oggetto che voglio sintetizzare e mi serve un materiale... vorrei che andassi "
              "a prendermelo. È la coda di Estork: bisogna abbattere il signore della Foresta del "
              "Dio Cane, a sud-ovest di Tyris del Sud.")
RESE[8302] = ("A dire il vero dovrei andarci io... ma ho altre richieste da sbrigare, e comunque "
              "Estork non è un avversario alla mia altezza. È un incarico peeeericolosissimo, ma se "
              "te la senti mi piacerebbe che lo accettassi.")
