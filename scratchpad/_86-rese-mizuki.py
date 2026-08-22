# -*- coding: utf-8 -*-
"""Le rese del lotto MIZUKI la principessa dell'abisso (chat.hsp :8459-:8694).

Registro: Mizuki e' 深海の姫 — una principessa antichissima che parla da vecchia
(わし, じゃ, のう, おぬし). Il precedente e' `db_creature.hsp:86751`
(«Anche questa vecchia se la cava ancora, eh.») e i due fabbri della 84a: NON
si fa l'italiano finto arcaico, si fa un italiano piano con una punta di
solennita' anziana. Da' del tu al giocatore.

Mizuki e' femmina (`db_creature.hsp:86765`, «la principessa dell'abisso»),
quindi su se stessa l'accordo si fa; sul GIOCATORE mai — niente participi che
si accordino, e le voci di menu in prima persona restano senza genere.

Lessico ereditato: 地上 «la superficie» (`db_creature.hsp:86826`), 小さなメダル
«medaglietta» (`db_item.hsp:144256`), 精神波 «onde mentali» (`chat.hsp:24451`),
精神崩壊 «la mente spezzata» (`map.hsp:15070`), i tre 弁当 «pranzo dell'abisso /
dell'invecchiamento / del ringiovanimento» (`db_item.hsp`), e il diario del
giocatore (`text.hsp:9804`): «Dal fondo del mare e' emerso un castello».
"""

RESE = {}

# --- dopo la fine: l'antenato dorme di nuovo (flag 275 == 2)
# ⚠️ deroga: l'inglese qui e' rotto in due punti. Dice «My ancestors are
# falling asleep» al plurale, ma l'antenato e' uno solo e lo dice l'inglese
# stesso a :8536 («My ancestor is inside. His strength...»); e chiude con «There
# is only a person who will come to talk from the surface like this... enough.»,
# che non e' una frase. Si segue il giapponese.
RESE[8462] = ("Il mio antenato è tornato pietra e dorme di nuovo. Non si sveglierà per altre decine di "
              "migliaia di anni. Io... io sto bene. Perciò non stare in pena. Mi basta che qualcuno scenda "
              "dalla superficie a farmi due chiacchiere... mi basta davvero.")
RESE[8463] = ("Volevo ringraziarti, ma in questo castello non c'è niente che possa far piacere a chi viene "
              "dalla superficie. Ecco... è una miseria, lo so, ma sono riuscita a preparare soltanto un "
              "pranzo. Dopo la fatica che hai fatto un pranzo è ben poca cosa, ma ti prego, accettalo lo "
              "stesso.")
# ⚠️ deroga: «Stop smart talking and I will switch over!» non vuol dire niente.
# Il giapponese e' 辛気臭い話はやめて、切り替えてゆくぞ — «basta discorsi tristi,
# cambiamo aria».
RESE[8467] = "Su! Basta con i discorsi tristi, cambiamo aria!"

# --- il congedo: il castello torna in fondo al mare (flag main 400)
RESE[8472] = ("L'hai fermato... ti sono davvero grata. Alla gente di quest'isola abbiamo fatto un male "
              "terribile, e il mio potere non basta a rimetterla com'era... Almeno adesso lascerò la "
              "superficie il prima possibile e tornerò in fondo al mare insieme al castello.")
RESE[8473] = ('"" + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", nel castello non c\'è niente di interessante, '
              'ma se ti va vieni a trovarmi... Ti aspetterò. Anche per decine di migliaia di anni."')

# --- il menu prima dell'ultima salita (flag main 399)
RESE[8488] = "Vorrei prima tornare"
RESE[8489] = "Lascia fare a me"
RESE[8490] = "Ti sto dando un bel po' di pensieri, eh..."
RESE[8498] = "Certo, avrai da prepararti in tanti modi. Ma non dimenticare che di tempo non ne resta molto."
RESE[8506] = "Perdonami... perdonami..."

# --- il primo incontro sull'isola (flag main 398)
RESE[8510] = "Ho sentito una voce chiedere aiuto"
RESE[8511] = "...Voglio tornare subito"
RESE[8512] = "È stata la tartaruga a portarmi qui"
RESE[8513] = "T-tu... chi sei!?"
RESE[8516] = "M-ma che combina, Leiki!? Perdona la mia tartaruga..."
RESE[8525] = "...Lo capisco. In una situazione così chiunque vorrebbe andarsene..."
RESE[8534] = "Dunque il mio richiamo è arrivato a qualcuno..."
RESE[8535] = ("Guarda che disastro. L'ultima volta che il castello emerse, qui intorno non c'erano isole. "
              "Sarà colpa dei movimenti della crosta... Qualcuno sono riuscita a farlo scappare, ma quasi "
              "tutti gli isolani hanno avuto la mente spezzata. Noi... noi siamo una stirpe che fa male "
              "alla gente della superficie. E io ho sospirato per la superficie tutta la vita senza "
              "saperlo. Sono stata... proprio una sciocca...")
# ⚠️ deroga: l'inglese riassume in «His strength hasn't fully returned yet» due
# informazioni che al giocatore servono per combattere — che nel corpo non e'
# forte e che appena sveglio la magia non gli riesce. Si riprendono dal
# giapponese: e' l'istruzione della missione.
RESE[8536] = ("...Non è il momento di lamentarsi. Il castello è dall'altra parte dell'isola: ci si "
              "arriva guadando le secche. Il mio antenato è in fondo. Nel corpo non è forte, e appena "
              "sveglio la magia non gli riesce. Con la tua forza puoi fermarlo, ne sono certa.")
RESE[8537] = ("Però il mio antenato manda onde mentali a intermittenza, per telepatia. Fino a ieri le "
              "fermava tutta quell'acqua di mare, ma adesso non c'è più niente a fare da schermo. Ho "
              "ordinato a Leiki di riportarti indietro all'istante, se la tua mente comincia a cedere. "
              "Tieni sempre d'occhio il tuo stato mentale.")

# --- l'incarico secondario: raccontarle il mondo di sopra
RESE[8544] = "Non fare complimenti. Su, su, raccontami com'è il mondo lassù in superficie!"
RESE[8553] = " (Le hai raccontato le tue avventure e come vanno le cose nel mondo...) "
# ⚠️ deroga: «How many thousands of years has it been since someone last floated
# up here...?» e' un'altra frase rispetto al giapponese, che dice quando e'
# emerso il CASTELLO l'ultima volta — ed e' il dato che regge :8535.
RESE[8555] = ("Uff... che invidia, tu che puoi girare il mondo all'avventura. Io ho un compito e da "
              "questo castello non posso muovermi... L'ultima volta che è emerso, dicono, fu decine di "
              "migliaia di anni fa.")
RESE[8557] = "Comunque sia, hai fatto un buon lavoro. Torna a trovarmi. Questo è il mio ringraziamento!"

# --- il menu di tutti i giorni
RESE[8566] = "Solo una visita"
RESE[8567] = "Raccontare la mia storia"
RESE[8568] = "Raccontare la storia di un compagno"
RESE[8569] = "Che c'è, hai qualche storia interessante da raccontare?"
RESE[8587] = "Oh, non vedo l'ora! Su, racconta!"
RESE[8595] = "Anche così mi fa piacere. Qui non c'è granché, ma fermati quanto vuoi."

# --- le medagliette
# ⚠️ «Dare le medagliette» sta in 19 caratteri: l'inglese «Here, take these
# medals.» ne fa 24 esatti, e per la regola delle due colonne l'italiano non
# puo' sforare dove l'inglese ci sta.
RESE[8600] = "Dare le medagliette"
# ⚠️ firma condivisa: la stessa riga e' il rifiuto del menu dei calzini di
# Kuroya (:12697). «Non se ne parla» regge in tutt'e due.
RESE[8601] = "Non se ne parla"
RESE[8602] = ("Quel coso che luccica... si chiama medaglietta, no? Com'è bello... ti prego, non me lo "
              "cedi?")
RESE[8605] = "Ngh... scusami, ho chiesto troppo."
RESE[8610] = ("Oh... che gioia, grazie! Uhm, prenderla per niente non sta bene. Ho solo questo, ma lo "
              "accetti?")

# --- *chat_unique_mizuki: il menu del racconto
RESE[8633] = "Rifare la prima metà"
RESE[8636] = "Rifare la seconda metà"
RESE[8638] = "Rifare tutto"
RESE[8639] = "Raccontare così"
RESE[8640] = "Tenerlo per me"
RESE[8641] = "Lasciar perdere"
RESE[8642] = "(Decidi il contenuto)"
RESE[8646] = "Ah, ecco com'è andata... A pensarci, ognuno ha la sua storia..."
# ⚠️ deroga: l'inglese butta via イケイケのピチピチじゃ, cioe' la seconda meta'
# della battuta — ed e' la battuta.
RESE[8649] = ("Però questa storia mi pare già sentita, uguale... C-che c'è? Non sono rimbambita, sono "
              "giovane e arzilla!")
RESE[8691] = "Ma... così mi lasci con la curiosità!"
