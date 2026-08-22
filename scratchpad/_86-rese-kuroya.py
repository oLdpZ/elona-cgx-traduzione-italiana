# -*- coding: utf-8 -*-
"""Le rese del lotto KUROYA lo scrutatore del cosmo (chat.hsp :12633-:12757).

Il lotto e' stato aperto dal contraccolpo di Mizuki: 「あげないよ」/«No way.» e'
una VOCE DI MENU condivisa fra :8601 e :12697, e renderla sola avrebbe lasciato
a meta' il menu dei calzini di Kuroya. Il rifiuto (:12697) sta nel lotto di
Mizuki, che e' dove nasce la firma.

Registro: Kuroya e' un vecchio mite e malinconico (僕, ね), gia' reso in
`db_creature.hsp:71283` («Dicono che il cosmo sia sconfinato.», «A quei tempi
non si torna più, eh...»). Da' del tu al giocatore. E' maschio e il codice lo
nomina, quindi su di se' l'accordo si fa; sul GIOCATORE mai.

Lessico ereditato: «<Kuroya> lo scrutatore del cosmo» e «<Belphat> lo
spadaccino cosmico» (`db_creature.hsp`), 靴下 «calzini» (`db_item.hsp:134939`,
`text.hsp:11209`), 信仰の巻物 «pergamena di fede» (`db_item.hsp:146891`), 神艦
«Nave Divina» (`text.hsp:9828`, deroga di famiglia gia' in uso).

⚠️ I soprannomi sono il perno della scena del riconoscimento: ベルっち e クロやん
diventano «Bel» e «Kuro», perche' a :12656 e' proprio il modo di chiamarlo che
Kuroya riconosce. `screen.hsp:1780` scrive «Kuroya» per intero, ma li' il
soprannome non e' il punto.
"""

RESE = {}

# --- la Culla del Caos
RESE[12637] = ("Ah... se non hai fiducia nel tuo braccio, forse al piano successivo è meglio non "
               "avvicinarsi troppo.")
RESE[12641] = ("Eh... vale la pena provare a trattare, anche quando sai già che non serve. Ops, "
               "parlavo fra me e me.")

# --- l'incontro con Belphat, l'amico venuto da un altro pianeta
RESE[12653] = ("Da ragazzo avevo un amico di un altro pianeta. Da quando è tornato al suo mondo sono "
               "passati decenni... Ci eravamo giurati di rivederci, ma io intanto sono diventato un "
               "vecchio. Vorrei incontrarlo ancora una volta, finché sono vivo...")
RESE[12654] = "Scansione del DNA... l'aspetto è cambiato, ma non ci sono dubbi: sei tu, Kuro!"
RESE[12655] = "C-chi sei tu!?"
RESE[12656] = "...Aspetta. Chiamarmi Kuro... sei tu, amico mio, Bel?"
RESE[12657] = ("Proprio io. ...Ma come sei cambiato, Kuro. Pelo bianco e pelle raggrinzita. Non sarai "
               "malato?")
RESE[12658] = ("Sono invecchiato perché tu non tornavi! E senti chi parla: anche tu sei cambiato, Bel! "
               "Prima eri piccolo, tondo e mezzo addormentato! Altro che una muta.")
RESE[12659] = "Già. Ho cambiato pelle 82 volte."
RESE[12660] = "Un po' troppe, no..."
RESE[12661] = ("No, no, così andiamo per le lunghe. Prima devo ringraziare chi mi ha portato fin qui. "
               "Tieni, una parte dei miei doni... ops. Su questo pianeta si usa rotolarli ai piedi, "
               "giusto.")

# --- il baratto dei calzini
RESE[12698] = '"(Consegnare " + itemname(ci) + ")"'
RESE[12699] = ("Oh...? Mi pare che tu abbia dei calzini con te. Ho una proposta: che ne dici di "
               "scambiarmeli con tre pergamene di fede?")
RESE[12702] = "Ecco... che peccato."

# --- il ladro di calzini
# ⚠️ «Sei il ladro di calzini?» sta in 24 caratteri esatti: l'inglese «Are you
# the sock thief?» ne fa 23, e per la regola delle due colonne l'italiano non
# puo' sforare il tetto dove l'inglese ci sta.
RESE[12713] = "Sei il ladro di calzini?"
RESE[12716] = "Senza esagerare, però"
RESE[12717] = "Siamo anime gemelle"
# ⚠️ deroga: «It's a shame to make you turn it over» ha perso il soggetto. Il
# giapponese dice che a dispiacergli e' consegnarli al CLIENTE — cioe' a
# Urcaguary, che e' chi ha ordinato i trenta calzini (`text.hsp:11209`).
RESE[12718] = ("Eh, in questi tempi sono proprio schiavo dei calzini... Mi dispiace quasi doverli "
               "consegnare al cliente.")
RESE[12721] = ("Un piacere da perdere i sensi... è bello, no? Finché annuso i calzini, la fretta e il "
               "nervoso spariscono.")
# ⚠️ invariato dichiarato: 「！！」 non e' testo, e' un sussulto. Vedi
# `invariati.md`. Firma condivisa con :14528 (il lavoratore precario della
# spada rossa), che e' una BATTUTA e non una voce di menu: non accende nessun
# menu a meta'.
RESE[12725] = "!!"
RESE[12726] = "Allora va bene"
RESE[12727] = "Ormai non c'è più niente da dire"
RESE[12728] = ("Non avrei mai creduto che qualcuno mi inseguisse oltre i campi di neve... Ma lascia "
               "che ti corregga: io non li ho rubati. Ho solo messo in salvo dei poveri calzini "
               "buttati per terra senza pietà.")
RESE[12731] = ("...Le maniere forti, dunque! Non c'è altro da fare. Lo Spadaccino dei Calzini scende "
               "in campo!")
RESE[12738] = "Già. È il profumo dei calzini che mi chiama..."

# --- la Nave Divina, dopo il ricongiungimento
RESE[12748] = ("I racconti di viaggio di Bel sono di serie B come sempre, e mettono i brividi. "
               "Davvero... mi sento addosso che ci siamo ritrovati. Anche da bambino li ascoltavo "
               "così, perdendomi fra nomi propri che non capivo. Ah, che nostalgia... mi viene quasi "
               "da piangere.")
RESE[12751] = ("Questa Nave Divina vola, e pare che possa navigare anche fuori da Irva... nel cosmo. "
               "Il cosmo... mi piacerebbe andarci, un giorno.")
# ⚠️ stesso giapponese di :12653, due inglesi appena diversi: due firme, una
# resa sola. Non e' il caso della 84a (un giapponese, tre inglesi che
# interpretano contesti diversi): qui e' la stessa battuta in due rami del
# codice.
RESE[12752] = RESE[12653]
RESE[12753] = ("A guardarla, questa nave che può navigare il cosmo, mi prende una stretta al cuore e "
               "insieme mi pare di tornare a quando ascoltavo il mio amico e sognavo lo spazio... "
               "ecco, mi sento così.")
