# -*- coding: utf-8 -*-
"""Le rese degli ULTIMI blocchi di `*chat_unique` (84 firme, zona chiusa).

    :2370  KARAM il lupo solitario di Karune — il messaggio a Erystia    7
    :4813  BALZAK il custode — le fogne di Lumiest                       9
    :5672  il CAPO DEI BANDITI — il pedaggio e la battaglia navale      13
    :5831  l'ISTIGATORE DEGLI ELEA — l'estorsione                       15
    :5921  la SCIENZIATA STRANA — le Little Sister                      12
    :6219  la MOTO DI KANEDA                                            10
    :6294  il GUERRIERO DALLA TESTA DI LEOPARDO — Silvia                 4
    :8194  SIRAHA e :8232 KURON — le due lettere mangiate                16

Le due firme che vivevano «fuori» erano RECIPROCHE: il capo dei banditi e
l'istigatore si dividono `:5713`, Siraha e Kuron si dividono `:8218`. Prese le
coppie insieme, il perimetro si chiude da solo.

⚠️⚠️ **Il CAPO DEI BANDITI e l'ISTIGATORE DEGLI ELEA non hanno un sesso.**
`db_creature.hsp:115501` e `:40979` non assegnano `CDATA_SEX`: leggono quello
che il gioco ha tirato a caso e cambiano solo la faccia. Quindi il divieto di
genere vale anche su di LORO, non solo sul giocatore — nessuna delle loro
battute puo' accordarsi con chi parla. Gli altri sono fissi: KARAM 0, BALZAK 0,
SIRAHA 0, la SCIENZIATA 1, KURON 1, il LEOPARDO 0.

Lessico ereditato: «<Balzak> il custode», «<Moto di Kaneda>», «<Siraha> la
pelle candida», «<Kuron> la veste nera», «il guerriero dalla testa di
leopardo» (`db_card.hsp`); «Karam», «Saimore», «<occhio delle tenebre
eterne>», «la Foresta Eretica», «Rehm-Ido», «Sierre Terre» (`chat.hsp:2255`,
`:2263`, `:2324`, `:2377`); «gli Elea» maiuscolo (glossario);
«<Little Sister>» invariato; «droga in capsula» (`db_item.hsp:141981`);
«Lumiest», «Ludus», «Palmia».

⚠️ `:5846` porta `cdata(CDATA_GOLD, CHARA_PLAYER) / 20` **senza parentesi**,
come monte. Provato al banco (`_85-banco-cnvrank.py`): in HSP la divisione nuda
dentro una concatenazione da' lo stesso risultato di quella fra parentesi.
Copiare la forma di monte tiene il comportamento identico.
"""

RESE = {}

# --- KARAM il lupo solitario di Karune
RESE[2374] = ("...Chi va là? Ah, ecco: Erystia ti ha mandato a cercarmi... Come vedi sono ferito e "
              "non riesco più nemmeno a muovermi. Ma grazie a te, essere arrivato vivo fino a qui "
              "un senso ce l'ha.")
# ⚠️ deroga: l'inglese dice «brother» e il giapponese 従弟, cugino — ed e' la
# resa gia' in dizionario a `:2263`, «il cugino del defunto re Zashim».
RESE[2375] = ("Ho una cosa da chiederti. Riferisci a Erystia le mie parole. Sembra incredibile, ma a "
              "guardia del tesoro segreto che dorme in fondo a Lesimas c'è Zeome, il cugino del "
              "defunto re Zashim. Forse è la magia del tesoro, anzi di tutta Lesimas, a manovrarlo. "
              "Un uomo in carne e ossa non è più.")
RESE[2376] = "E non è tutto. Saprai che Saimore, di Zanan, punta al tesoro. Ma per quale ragione?"
RESE[2377] = ("Il tesoro che Zeome possiede si chiama <occhio delle tenebre eterne>, e si dice che "
              "rifletta la verità del mondo. Saimore ha spiegato la fine di Rehm-Ido e l'inizio di "
              "Sierre Terre e con quella teoria ha raccolto un consenso enorme: perché adesso vuole "
              "il tesoro?")
RESE[2378] = ("Spinta da Saimore, sta per cominciare una guerra contro gli Elea. Che la Foresta "
              "Eretica sia la sciagura di Rehm-Ido, i <Meshera>, è poi davvero certo? E se la "
              "teoria di Saimore fosse falsa, qual è il suo vero scopo?... Ho un brutto "
              "presentimento.")
RESE[2379] = ("Il mio compito finisce qui. Con queste ferite alla superficie non ci arrivo comunque. "
              "Porta presto la notizia alla capitale... e che il dio del destino ti protegga!")
RESE[2393] = 'cdatan(CDATAN_NAME, tc) + " si toglie la vita..."'

# --- BALZAK il custode
RESE[4816] = "Anche oggi le strade di Lumiest sono pulite!"
RESE[4820] = "Aspetta, aspetta, aspettaaa!"
RESE[4821] = "Va bene"
RESE[4822] = "Non ne ho voglia"
RESE[4823] = ("Io sono Balzak, netturbino di mestiere da dieci anni, e della pulizia di Lumiest ho "
              "fatto la missione della mia vita. Non mi sfugge il rifiuto più piccolo: è orgoglio "
              "di professione. Ma quell'orgoglio me l'hanno ferito. Nelle fogne si è insediato un "
              "mostro spaventoso e da solo non ce la faccio più. Tu che mi capisci, ci vai a "
              "sistemarlo, vero?")
RESE[4826] = "Ah, così... Che tipo freddo..."
RESE[4830] = ("Aspettavo queste parole! L'ingresso delle fogne è vicino alla locanda. Occhio però: "
              "quelli là sono ostici!")
RESE[4836] = "Oh, sei tu. Come va la pulizia delle fogne?"
RESE[4854] = "Ma davvero!? Le hai purificate sul serio? Grande! Tieni il compenso: te lo meriti."

# --- il CAPO DEI BANDITI  ⚠️ sesso non assegnato: niente accordo su chi parla
RESE[5675] = "Bah, un pezzente senza un soldo. Che perdita di tempo! Fuori dai piedi!"
RESE[5713] = '"Hai consegnato " + itemname(cnt) + "."'
RESE[5719] = "Una decisione saggia."
RESE[5739] = ("Hai fegato... ma non si può dire che sia una scelta intelligente. Questa sarà la tua "
              "tomba.")
RESE[5747] = "Vuoi salire a bordo!? Hai fegato!"
RESE[5757] = "La nave ha urtato male e il salto è fallito..."
RESE[5759] = "Aaaah! La nostra nave affonda!?"
RESE[5772] = "Che pazzia! Vuoi finire in pasto ai pesci!?"
RESE[5779] = "Uoh!?"
RESE[5783] = "Hai vinto la battaglia navale e guadagni 1000 punti di fama."
RESE[5801] = "Adesso basta! Si contrattacca!"
RESE[5815] = '"Ce l\'hai fatta a scappare, ma hai perso " + p + " punti di fama."'
RESE[5816] = "Quello scappa! Ragazzi, una palla di cannone in poppa!!"

# --- l'ISTIGATORE DEGLI ELEA  ⚠️ sesso non assegnato
# ⚠️ stesso giapponese di :5675, due inglesi diversi: due firme, due rese.
RESE[5834] = "Bah, un pezzente senza un soldo. Che perdita di tempo! Sparisci dalla mia vista!"
RESE[5840] = "Che barbarie!"
RESE[5841] = "Rifiuto con la forza"
RESE[5842] = "Non ho mai perseguitato gli Elea"
RESE[5843] = "Ai miei soldi ci tengo"
RESE[5844] = "Mi puzza di losco"
RESE[5845] = "Verso quel che chiedi"
RESE[5846] = ('"Ehi, tu! Se gli Elea sono stati accusati ingiustamente e perseguitati è perché '
              'branchi come voi si sono fatti manovrare da Zanan! Anche adesso che la verità è '
              'nota, gli Elea a cui hanno tolto la terra vivono nella miseria! Non ti senti in '
              'colpa? Su, ammetti la tua parte nella congiura e versaci il carico del carretto e " + '
              'cdata(CDATA_GOLD, CHARA_PLAYER) / 20 + " monete d\'oro! Se no, ti faccio versare la '
              'tua sporca vita con la forza!"')
RESE[5863] = ("Oh, ammetti la colpa! Magnifico! Ma per quanto tu versi, il fatto che gli Elea "
              "abbiano sofferto non sparirà in eterno! Non credere di esserti fatto perdonare, "
              "feccia disumana! Continua a chiedere scusa fino all'ultima delle tue generazioni!")
RESE[5870] = ("Sentite, gente! Se uno trova scomoda la nostra attività, vuol dire che è un agente "
              "di Zanan! A un agente di Zanan non si deve dare ascolto in niente! Ammazzatelo!")
RESE[5874] = ("Noi raccogliamo denaro e beni per gli Elea perseguitati e ridotti alla fame! "
              "Opporsi è discriminazione bella e buona! Smettila di prendere in giro gli Elea! "
              "Quando siete voi a opporvi con la forza è violenza; quando siamo noi a raccogliere "
              "offerte con la forza non lo è! È il giudizio giusto concesso agli Elea, e una "
              "protesta contro il mondo!")
RESE[5878] = ("E allora tirala fuori, la prova che non li perseguiti! Non ce l'hai, vero, bugiardo? "
              "Anche se non hai mai perseguitato nessuno non cambia niente! Gli Elea finora ne "
              "hanno passate di brutte, quindi se colpiscono qualcuno che non c'entra sono "
              "perdonati! Non ci arrivi nemmeno a questo?")
RESE[5882] = ("Tu gli Elea li guardi dall'alto in basso, vero? Fino a oggi li avrai perseguitati, e "
              "riempiti di botte e di insulti! Perché tu gli Elea li disprezzi! Bella roba, "
              "disprezzare e perseguitare gli Elea fino a oggi! Feccia della peggior specie: "
              "adesso ti linciamo!")
RESE[5886] = ("Sospettare di noi solo perché siamo Elea è un'etichetta odiosa! Un razzista come te "
              "non ha il diritto di lamentarsi qualunque cosa gli si faccia! Perciò ti ammazziamo "
              "a poco a poco! Se muori come un cane la colpa è tutta tua!")

# --- la SCIENZIATA STRANA
RESE[5924] = ("Ascoltami bene. Se un giorno incontrerai una Little Sister, tendi la mano a quelle "
              "bambine. A vederle sembrano mostri, ma io continuo a studiare perché possano tornare "
              "al sorriso dolce di prima. Perciò ti prego: usa questo strumento e portami le Little "
              "da me. Un ringraziamento, prima o poi, arriverà di sicuro.")
RESE[5934] = "E il compenso promesso?"
RESE[5935] = "Rifornirmi di sfere"
RESE[5938] = "(Consegnare la Little Sister)"
RESE[5941] = ("C'è chi dice che le Little vadano liberate da un dolore senza fine. Ma quasi tutti le "
              "uccidono perché ne vogliono il potere. Sì: è vero che la carne delle Little fa "
              "evolvere il corpo umano. Io però credo che ci sia un'altra strada per salvarle. "
              "...E ricordati: se toglierai la vita a una Little, prima o poi il conto ti verrà "
              "presentato.")
RESE[5949] = ("Il compenso, già. Le Little hanno raccolto per te le cose che la gente perde in "
              "città. Scegli quello che ti piace. Se preferisci puoi anche tenerlo da parte, per "
              "quando perderai qualcosa di prezioso.")
RESE[6030] = "Puoi prendere un oggetto smarrito."
RESE[6036] = "L'hai trovato, quello che cercavi?"
RESE[6040] = ('"Non ne hai ancora il diritto. Portami altre " + p + " Little Sister, e del compenso '
              'parliamo dopo."')
RESE[6045] = "Su, prendi questo. È pesante: fa' attenzione."
RESE[6082] = "Hai consegnato la Little Sister."
RESE[6096] = ("Grazie. Ti sono riconoscente per quello che fai. Il ringraziamento arriverà presto, "
              "promesso.")

# --- la MOTO DI KANEDA
RESE[6222] = "Allora, ti va di montarmi in groppa?"
RESE[6223] = "Sì!"
RESE[6224] = "Non particolarmente"
RESE[6230] = "Ops, a quanto pare non puoi portarti dietro altri compagni."
RESE[6232] = "Così mi piaci!"
RESE[6238] = "Vabbè, fa lo stesso."
RESE[6243] = "Quella è una droga in capsula! ...Senti, non è che me la cedi?"
RESE[6251] = "Gli hai dato una pastiglia di droga in capsula."
RESE[6253] = "Grande. Sei grande."
RESE[6258] = "Non attaccare bottone con me."

# --- il GUERRIERO DALLA TESTA DI LEOPARDO
RESE[6297] = ("Un tempo... Silvia fu rapita da un seduttore. La liberammo dalla stanza dove la "
              "tenevano chiusa, ma la sua mente era ormai a pezzi.")
RESE[6298] = ("E quando tornai da una lunga spedizione, aveva preso a darsi a chiunque in "
              "città...")
RESE[6299] = "E io, nonostante tutto, Silvia la..."
RESE[6303] = "Da un po' Silvia delira sempre peggio. Che cosa mai la riduce così...?"

# --- SIRAHA e KURON: le due lettere mangiate
# ⚠️ `_onii()` sembra morfologia e invece si CONSERVA: passa da `lang()` e
# rende l'appellativo che il gioco sceglie sul sesso del giocatore.
RESE[8199] = ('_onii(cdata(CDATA_SEX, CHARA_PLAYER)) + ", tu vai all\'avventura, vero? Una mia '
              'amica che stava qui si è trasferita a Palmia, in Tyris del Nord: vorrei che le '
              'portassi una lettera!"')
RESE[8202] = "Ehh... e adesso che faccio..."
RESE[8206] = '"Evviva! Grazie mille, " + _onii(cdata(CDATA_SEX, CHARA_PLAYER)) + "!"'
RESE[8207] = "Hai preso la lettera."
RESE[8214] = "Eh? Una lettera per me?"
RESE[8215] = "Evviva, avevo giusto fame! Gnam gnam gnam..."
RESE[8216] = "Mmh!? O-oddio. Mi sono mangiato la lettera di Kuron..."
RESE[8217] = ("Vediamo un po' che diceva la lettera... Porta questa a Kuron. Mica gratis, eh: ti do "
              "una moneta di platino, per favore!")
RESE[8218] = "Hai preso la lettera..."
RESE[8227] = "Mi raccomando, consegnala all'amica: è Kuron, quella che vive a Palmia."
RESE[8235] = "Eh? Una lettera per me?"
RESE[8236] = "Evviva, avevo giusto fame! Gnam gnam gnam..."
# ⚠️ l'inglese scrive «Shiraha» qui e «Siraha» nel nome della creatura
# (`db_creature.hsp:88124`). Il nome buono e' quello della creatura.
RESE[8237] = "Buonaaa! Mmh!? O-oddio. Ho mangiato la lettera di Siraha..."
RESE[8238] = ("Vediamo un po' che diceva la lettera... Porta questa a Siraha. Mica gratis, eh: ti "
              "do una moneta di platino, per favore!")
RESE[8248] = "Mi raccomando, consegnala all'amico: è Siraha, quello che vive a Ludus."
