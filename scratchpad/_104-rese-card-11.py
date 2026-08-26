# -*- coding: utf-8 -*-
"""104a - Lotto 11 di `db_card.hsp`: le carte fra la riga 5101 e la 5600 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_103-rese-card-07.py` per le decisioni della 103a.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `かたつむり` → **la chiocciola**,
`スライム` → **la melma**, `イルヴァ` → **Irva**, `エウダーナ` → **Eulderna**,
`ジラ` → **lo zilla** (`db_card.hsp:10839`), `闇喰コアラ` → **il koala
mangiabuio** (`:6692`), `ギガモール` → **la talpa colossale** (glossario, 102a),
`ネクロマンシー` → **negromanzia** (`blend.hsp:778`), `合成獣` → **bestia
sintetica** (`:4697`), `生体兵器` → **arma biologica** (`chat.hsp:2015`),
`弩砲` → **balista** (`db_item.hsp:139184`), `気` → **il ki** (otto siti).

⚠️⚠️ **`キッカス` si scrive `Kikkasu`, e la decisione e' di oggi.** Il paese era
reso in due modi — `Kikkasu` in `chat.hsp` e `text.hsp` (7 volte), `Kikkas` in
`db_card.hsp` e `db_creature.hsp` (3) — perche' l'inglese di monte si spacca
allo stesso modo e ogni lotto ha seguito il file che aveva davanti. Unificato da
`scratchpad/correzione-kikkasu.py`, che tocca anche il **nome** della creatura
(`il pitone di Kikkasu`, due dizionari con la stessa firma).

⚠️⚠️ **Quattro errori di monte, tutti presi dal giapponese:**
- `:5139` 食べられないことはない vuol dire *non e' che non si possa mangiare*.
  L'inglese scrive «It's never eaten», che dice il contrario;
- `:5178` 後天的に植え付けられた e' *innestata dopo la nascita*. L'inglese
  scrive «born with», che e' l'opposto esatto di 後天的;
- `:5191` 当て馬 e' *l'esca*, il cavallo che si mette in pista per far correre
  gli altri. L'inglese lo rende alla lettera, «a guessing horse», che in inglese
  non vuol dire niente;
- `:5256` 少なくない e' una litote: *non pochi*. L'inglese scrive «there are
  few», che ribalta la frase.

⭐ **Due citazioni, e tutt'e due hanno gia' una forma italiana.** `:5243` e'
Gettysburg — ペンギンのペンギンによるペンギンのための国 ricalca *del popolo,
dal popolo, per il popolo* — e si rende con quella. `:5386` e' 迷える子羊, **la
pecorella smarrita** del Vangelo, che regge anche la carta gemella `:5373`.

⭐ **Il bisticcio di `:5373` si tiene, e cambia parola.** 外道 e' *fuori dalla
via*, e il nome della carta e' `la pecora smarrita`: in italiano *smarrire la
retta via* fa lo stesso doppio senso, morale e stradale, che l'inglese
(«truly an outsider») aveva perso.

⚠️ **`:5412` la coda persa dall'inglese va rimessa.** 石のように重い声で鳴く蛇。
**よって鳴蛇。** — *un serpente che stride: di qui il nome*. E' l'etimologia del
nome della carta, e l'inglese la salta.

⚠️ **I tre `鬼` di `:5529`, `:5542` e `:5555` aprono con la STESSA frase
giapponese** e vanno resi identici. Il loro nome e' gia' `il demone ...`, e
nella frase c'e' anche 悪魔, che nel progetto e' **il demone** della trama: per
non chiamarli tutt'e due allo stesso modo, 妖怪 diventa **creatura
soprannaturale** e 鬼の中でも → *fra i suoi simili*.

⚠️ **`:5464` e `:5477` sono due carte diverse con lo STESSO nome** (`仮装子`,
`il bambino in maschera`, `cardrefn` identico a `:5470` e `:5483`) e la stessa
prima frase: quella frase e' resa uguale in tutt'e due.
ⓘ E il `None` che il dossier stampa su `:5477` **non e' lavoro mancante**: il
dizionario indicizza per firma e la firma del nome e' una sola, quindi `applica`
scrive la stessa resa su tutt'e due le righe.

⚠️ **`疫病神` di `:5399` non e' una creatura del gioco**: unica occorrenza in
tutto il sorgente. Resta *il dio della pestilenza*, e **non** si aggancia al
`疫病の悪魔` della missione, che e' gia' «il demone della pestilenza».

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`. In CP932 il resto diventa doppia larghezza. Per questo le 「」
di `:5360`, `:5282`, `:5529`, `:5542` e `:5555` si sciolgono nella frase.
⚠️ E le cifre a doppia larghezza del giapponese (`５ｍ`, `20ｍ`, `4枚`) si
scrivono in italiano con le cifre normali.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :5113 la lepre di mare acida
    (5113, 'When meeting or being poked by an outside enemy the body spurts out an intense acidic liquid to protect itself. That acid attack often causes extra anger and gets them killed.'):
        "Quando incontra un nemico o si sente beccare, si difende schizzando dal corpo un liquido acido violentissimo. Spesso però quell'attacco non fa che aumentare la rabbia di chi ha davanti, e allora finisce ammazzata.",

    # ---------------------------------------------------------- :5126 la magicargot
    (5126, 'A rare snail that has accumulated magical power. Even though it is a snail it is able to use magic in its own way. It is often eaten because of its magical properties that make it stronger when eaten.'):
        "Una chiocciola rara che ha accumulato dentro di sé potere magico. Per essere una chiocciola, la magia sa pure usarla in modo dignitoso. Verrebbe da dire che allo stato brado se la cavi... e invece no: chi la mangia diventa più forte nella magia, e per questo finisce spesso in pentola.",

    # ---------------------------------------------------------- :5139 la lepre di mare gigante
    # ⚠️ 食べられないことはない: l'inglese scrive «It's never eaten», che e' il contrario.
    (5139, "The snail of the sea. The shell has degenerated and is housed in the body. It's never eaten but it has almost no flavor as it is and is poisonous. It is adaptable to seawater but it does not help if it is exposed to thick salt."):
        "La chiocciola del mare. Il guscio le si è ridotto e le è finito dentro il corpo. Mangiarla non è impossibile, ma così com'è non sa quasi di niente ed è pure velenosa. All'acqua salata si è adattata, però se le si rovescia addosso del sale forte non la salva nessuno.",

    # ---------------------------------------------------------- :5152 la ragazza zombi
    (5152, 'Using a type of slime it was created by piecing together the corpse of a girl. She has been wandering around since before the present civilization in search of memories of her past. Its perfection is a work of art level with powers that cannot be compared to mass-produced zombies.'):
        "È nata cucendo insieme il cadavere di una ragazza con l'aiuto di una specie di melma. Da prima dell'attuale civiltà vaga in cerca dei ricordi di quando era viva. La fattura è di livello artistico, e ha una forza che gli zombi di serie non le si avvicinano nemmeno.",

    # ---------------------------------------------------------- :5165 la gotica
    (5165, 'Using a type of slime it was created by piecing together the corpse of a girl. It has the ego as it was when it was alive. They have been instilled with a distorted appetite during manufacturing and instinctively prey on zombies or people against their will.'):
        "È nata cucendo insieme il cadavere di una ragazza con l'aiuto di una specie di melma. Ha ancora l'io che aveva da viva. Mentre la fabbricavano le hanno innestato un appetito storto, e così, zombi o persone che siano, se li divora d'istinto, contro la sua stessa volontà.",

    # ---------------------------------------------------------- :5178 il requiem
    # ⚠️ 後天的に植え付けられた e' *innestata dopo*: l'inglese scrive «born with».
    (5178, 'Using a type of slime it was created by piecing together the corpse of a girl. She takes on the persona of a girl who was alive but her mind is consumed by madness. She is the type who was born with a high shooting ability and works calmly from the rear.'):
        "È nato cucendo insieme il cadavere di una ragazza con l'aiuto di una specie di melma. Ha la personalità che la ragazza aveva da viva, ma la mente gliela rode la follia. È del tipo a cui la mira è stata innestata dopo, e lavora dalle retrovie, senza dare nell'occhio.",

    # ---------------------------------------------------------- :5191 la regina savant
    # ⚠️ 当て馬 e' l'esca: «a guessing horse» in inglese non vuol dire niente.
    (5191, "The strongest Savant made using a selection of human body parts. It can also use necromancy albeit briefly. It takes pride in being an elite but doesn't know that it's actually just a guessing horse."):
        "La savant più forte di tutte, fatta con pezzi di corpo umano scelti a uno a uno. Sa usare anche la negromanzia, se pure in forma rudimentale. Va fiera di essere fra le elette, e non sa che in realtà non è che un'esca.",

    # ---------------------------------------------------------- :5204 il lupo famelico leggendario
    (5204, 'A wolf with a legendary hunger for victory. He is a terrible loser. It is possible to harden the body by practicing chi but this seems to be the result of learning the giantization technique in a rather incorrect way.'):
        "Un lupo affamato di vittoria fino alla leggenda, e che a perdere non ci sta in modo spaventoso. Impastando il ki riesce a indurirsi il corpo, ma pare che sia il risultato di una tecnica di ingigantimento imparata parecchio male.",

    # ---------------------------------------------------------- :5217 <Inqtual> il demone della vendetta
    (5217, "A demon that peers into the minds of others and manipulates them with a vengeful spirit. Deep down she thinks revenge is a fool's errand and she has no intention of taking revenge on the gods who sealed her. When she meets someone who doesn't take her up on her offer she shows interest and becomes obsessed."):
        "Un demone che sbircia nel cuore degli altri, si nutre della loro sete di vendetta e li manovra. Dentro di sé però la vendetta la trova una sciocchezza, e non ne medita nemmeno contro gli dei che l'hanno sigillata. Quando incontra qualcuno che non abbocca al suo invito si incuriosisce, e non lo molla più.",

    # ---------------------------------------------------------- :5230 l'ultimo corvo
    (5230, 'A type of crow that has the tendency to kill each other in flocks. The last one to survive is called this. They are also called the dominant because they have congenital combat skills.'):
        "Una razza di corvi che dentro lo stormo si ammazzano fra loro. L'ultimo che resta vivo si chiama così. È portato per il combattimento fin dalla nascita, e lo chiamano anche il dominante.",

    # ---------------------------------------------------------- :5243 il pinguino errante
    # ⭐ Gettysburg: del popolo, dal popolo, per il popolo.
    (5243, "A penguin warrior who travels to make a country for penguins by penguins penguins. They prefer the cold but they will work with guts even in the heat. They can''t fly but they're very good swimmers."):
        "Un pinguino guerriero che viaggia per fondare un paese dei pinguini, dai pinguini, per i pinguini. Preferisce i posti freddi, ma anche al caldo tira avanti a forza di fegato. Volare non sa, ma nuotare sì, e benissimo.",

    # ---------------------------------------------------------- :5256 l'incantatore di corte
    # ⚠️ 少なくない e' una litote, *non pochi*: l'inglese scrive «there are few».
    (5256, 'He is a wizard at the royal palace. He is like a mass of talent and there are few who have been able to handle the enormous amount of magic at will since childhood. He is also the guardian of the royal palace in case of emergency.'):
        "Un mago al servizio della corte. Sono talento allo stato puro, e non pochi fra loro sapevano maneggiare a piacimento un potere magico immenso fin da bambini. Quando le cose si mettono male fanno anche da guardia al palazzo.",

    # ---------------------------------------------------------- :5269 l'arciere magico di Eulderna
    (5269, 'A soldier of Eulderna who was born with an inferior talent for magic. He supplemented his fighting power with a bow. He is not considered a wizard and his treatment in his home country is of the lowest class. Because of this he is frustrated and jealous.'):
        "Un soldato di Eulderna nato con poco talento per la magia. Quel che gli manca lo colma con l'arco. In patria non lo considerano un mago e lo trattano da ultimo degli ultimi, e per questo si porta dentro rancore e invidia.",

    # ---------------------------------------------------------- :5282 il Dobiel
    (5282, 'A bear that inherits a piece of power and a name from an angel that was scattered in the Great War of the Gods. Its name means God of the Bear. He has the power to use the crossbow but is completely incapable of using magic.'):
        "Un orso che ha ereditato il nome e una scheggia del potere di un angelo caduto nella grande guerra fra gli dei. Il suo nome vuol dire dio dell'orso. Ha la forza per maneggiare la balista come si deve, ma di magia non ne sa fare proprio.",

    # ---------------------------------------------------------- :5295 il maestro dei koala
    (5295, 'The strongest dark-eating koala leads a herd of dark-eating koalas. They are responsible for deciding where to feed and raid and guiding the herd. It has a habit of swinging a stick-shaped object. They seem to care about their skin and use a silky powder.'):
        "Il koala mangiabuio più forte di tutti, quello che comanda il branco. Decide dove si mangia e dove si va all'assalto, e guida gli altri. Ha il vizio di sbracciare con qualunque cosa abbia la forma di un bastone. E pare che si serva di una polvere finissima: chissà, forse ci tiene alla pelle.",

    # ---------------------------------------------------------- :5308 il wenkamui
    (5308, "A big bear has learned a taste for people. They appear actively around people's houses and are extremely obsessive. They are considered evil gods and have been hunted down by the people since time immemorial."):
        "Un orso enorme che ha preso il gusto della carne umana. Si spinge fin sotto le case senza farsi problemi, e a una preda che ha scelto non rinuncia più. Lo si ritiene un dio malvagio, e dai tempi più antichi la gente gli dà la caccia per sterminarlo.",

    # ---------------------------------------------------------- :5321 la tigre abbagliante
    (5321, 'Bioweapons discovered in the ruins. A tiger whose body has been partially replaced by a machine or armor. It\'s hard to avoid continuous rushes with the agility of a beast. It seems to have been named after the glittering lights.'):
        "Un'arma biologica ritrovata fra le rovine: una tigre a cui hanno sostituito parte del corpo con macchine e corazze. Sfrutta l'agilità della belva per caricare a ripetizione, ed è difficile scansarla. Il nome pare che le venga da quel suo luccicare accecante.",

    # ---------------------------------------------------------- :5334 la manticora della maledizione
    (5334, 'A synthetic beast based on a lion and spawned through magic. It has the intelligence of a human or rather the intelligence of a complete human and it is curious to know what was done when it was created.'):
        "Una bestia sintetica generata con le arti maledette a partire da un leone. Ha un'intelligenza pari a quella di un uomo... anzi, ha proprio l'intelligenza di un uomo, e vien voglia di sapere che cosa sia successo davvero mentre la creavano.",

    # ---------------------------------------------------------- :5347 il carbonchio rubino
    (5347, 'It is a subspecies of the carbuncle and is smaller. However its magic power is stronger than that of the normal species and it can summon a variety of monsters. It was once considered a fabled creature but today no one knows what the legend is.'):
        "Una sottospecie del carbonchio, più minuta. Il potere magico però ce l'ha più forte di quella comune, e riesce a evocare mostri di ogni sorta. È sempre stato considerato una creatura da leggenda, ma oggi non c'è più nessuno che sappia dire che cosa raccontasse quella leggenda.",

    # ---------------------------------------------------------- :5360 l'incarnazione dell'incubo
    (5360, "The nightmare took the form of a sheep. He chases a fleeing sheep but before he knows it he's lost in a nightmare. If...you have met this sheep in your dreams Never make eye contact."):
        "Un incubo che ha preso la forma di una pecora. Si dice che a inseguire la pecora che scappa ci si ritrovi smarriti dentro l'incubo senza nemmeno accorgersene. E se mai... se mai in sogno dovesse capitarti di incontrare questa pecora: non incrociare mai il suo sguardo.",

    # ---------------------------------------------------------- :5373 la pecora smarrita
    # ⭐ 外道 e' *fuori dalla via*: in italiano la retta via tiene il doppio senso.
    (5373, 'A black sheep that has been subjected to an excessive amount of magical modification in Eulderna. It can absorb visible light and disappear. They turn invisible and approach the enemy taking their life away. As the name implies it is truly an outsider.'):
        "Una pecora nera su cui a Eulderna hanno accanito le modifiche magiche fino all'eccesso. Assorbe la luce visibile e sparisce alla vista. Si fa invisibile, si accosta al nemico e gli succhia via il soffio vitale. Come dice il nome, ha proprio smarrito la retta via.",

    # ---------------------------------------------------------- :5386 il grande montone mai smarrito
    (5386, 'A lost lamb grows up in mind and body and overcomes his hesitation. If you look into those eyes you can see that they are full of determination and resolve. He is a gentle watcher and sometimes a guide to the lost lamb.'):
        "È la pecorella smarrita che, cresciuta nel corpo e nell'animo, ha vinto lo smarrimento. Basta guardarlo negli occhi per accorgersi che è colmo di decisione e di fermezza. Veglia con dolcezza sulle pecorelle smarrite, e ogni tanto le guida.",

    # ---------------------------------------------------------- :5399 l'oyaukamui
    # ⚠️ 疫病神 non e' una creatura del gioco: unica occorrenza nel sorgente.
    (5399, "A feathered and magical serpent god. It is relatively small only about 5 meters long. The stench and poison that is emanating from the body is so strong that even the pestilence god runs away and has actually been repelled. This is what it means to conquer poison with poison isn't it?"):
        "Un serpente divino, alato e pieno di potere magico. È piuttosto minuto: non arriva ai 5 metri. Il fetore e il veleno che gli escono dal corpo sono così violenti da mettere in fuga perfino il dio della pestilenza, e una volta è successo davvero. Ecco che cosa vuol dire vincere il veleno col veleno.",

    # ---------------------------------------------------------- :5412 la meida
    # ⚠️ L'inglese salta よって鳴蛇, che e' l'etimologia del nome. Rimessa.
    (5412, 'A snake with a voice as heavy as stone. They have four wings and build a nest in the water. As they occupy water source areas and absorb moisture in the clouds drought occurs in areas without natural enemies.'):
        "Un serpente che stride con una voce pesante come la pietra: di qui il suo nome. Ha quattro ali e fa il nido sott'acqua. Occupa le sorgenti e succhia via l'acqua dentro le nuvole, e così dove non ha nemici naturali arriva la siccità.",

    # ---------------------------------------------------------- :5425 il pitone di Kikkasu
    (5425, "This snake is native to Kikkas and its body can be as long as 20 meters. It's not poisonous but it's a tightening force and it strangles horses and bears. Those brought in as pets devour their owners escape and multiply and today attack livestock all over the world."):
        "Un serpente originario di Kikkasu, che arriva a una ventina di metri di lunghezza. Veleno non ne ha, ma stringe con una forza tale da strangolare cavalli e orsi. Quelli portati via come animali da compagnia si sono mangiati il padrone, sono scappati e si sono moltiplicati, e oggi assaltano il bestiame in tutto il mondo.",

    # ---------------------------------------------------------- :5438 il golem di fango dell'oltretomba
    (5438, 'A golem made from the mud of hell. It is powerful and normally dangerous but it is covered with the cold air of hell and even if it is grazed its life will be lost. It is said to have been created by an evil sorcerer sent to the other world.'):
        "Un golem fatto col fango dell'inferno. È forte, e già così sarebbe pericoloso, ma per giunta è avvolto nel gelo infernale: basta che ti sfiori e ti succhia via il soffio vitale. Si dice che l'abbia creato un mago malvagio spedito nell'aldilà.",

    # ---------------------------------------------------------- :5451 il golem muscoloso
    (5451, 'A mass of strong muscle. It is definitely categorized as a golem because of its structure and composition and it has a different flavor from an artificial person. They need to take the organism in to maintain their muscles but if the genes of other organisms get mixed in too much they run amok.'):
        "Un ammasso di muscoli tenacissimi. Per come è fatto e per come è nato va senza dubbio contato fra i golem, ed è tutt'altra cosa dagli uomini artificiali. Per mantenere i muscoli deve inglobare altri esseri viventi, ma se i geni degli altri si mescolano troppo perde il controllo e si scatena.",

    # ---------------------------------------------------------- :5464 il bambino in maschera
    (5464, 'On the 10th month they appear at other people\'s houses in costume. A mysterious rumor is spreading among children that there are more rare treats than a frontier house and it seems that the frontier is becoming more popular in turn. They are famous for their rather serious fancy dress.'):
        "Quando arriva ottobre si traveste e si presenta a casa d'altri. Fra i bambini gira una voce misteriosa, che più la casa è sperduta più i dolci sono rari, e così le zone fuori mano sono diventate le più ambite. È famoso per travestimenti fatti con una serietà notevole.",

    # ---------------------------------------------------------- :5477 il bambino in maschera (l'altra carta)
    (5477, "On the 10th month they appear at other people's houses in costume. They are fearless and will fight through a pack of demons for sweets even jumping into the homes of adventurers. There are many families who fear that they will be extremely vindictive."):
        "Quando arriva ottobre si traveste e si presenta a casa d'altri. Non conosce paura: per un dolce attraversa un branco di mostri e si butta perfino dentro casa di un avventuriero. Molte famiglie ne temono l'ostinazione smisurata e fanno finta di non essere in casa.",

    # ---------------------------------------------------------- :5490 il Meccazilla
    (5490, 'A mass-produced dinosaur mecha that was discovered in the ruins. Analysis revealed that it was built with Zilla as a model. He has power but is not good at fighting and uses his hover ability to gain distance and engage in gunfights.'):
        "Un dinosauro meccanico di serie, ritrovato fra le rovine. Analizzandolo si è scoperto che l'hanno costruito prendendo a modello lo zilla. La potenza ce l'ha, ma il corpo a corpo non fa per lui: si alza da terra per tenere le distanze e apre il fuoco da lontano.",

    # ---------------------------------------------------------- :5503 la bestia di nuvola
    (5503, 'A foggy monster several tens of meters in size. It is carnivorous and usually mimics a cloud to attack ships. During predation it solidifies parts of its body and produces organs such as its mouth.'):
        "Un mostro fatto di nebbia, grande alcune decine di metri. È carnivoro, e di solito si finge nuvola per assalire le navi e simili. Quando divora si solidifica una parte del corpo e si fabbrica una bocca e gli altri organi che gli servono.",

    # ---------------------------------------------------------- :5516 il dhole
    (5516, 'A huge slender creature with a body length of around one hundred meters. An invisible presence. It has devoured the earth with its voracious appetite and has even killed other stars. In Irva there is a natural enemy called Gigamor and it often runs away to the ground in desperation.'):
        "Un essere enorme e affusolato, lungo attorno ai cento metri. Alla vista non c'è. Con la sua fame smisurata divora la terra, e altri pianeti li ha già fatti morire. A Irva però ha un nemico naturale, la talpa colossale, e spesso non ce la fa più e scappa in superficie.",

    # ---------------------------------------------------------- :5529 il demone splendente
    (5529, 'They are originally human though they have aspects such as gods demons and earth spirits. It is a high ranking among the demons. It possesses a high level of magical power that is uncontrollable even by itself and the magical power leaking from its body gives off a glow.'):
        "Una creatura soprannaturale che ha lati da dio, da demone e da spirito della terra, ma in origine era un uomo. Fra i suoi simili sta in alto. Ha un potere magico così grande che nemmeno lui riesce a contenerlo, e quello che gli trabocca dal corpo manda un bagliore.",

    # ---------------------------------------------------------- :5542 il demone squartatore
    (5542, "They are originally human though they have aspects such as gods demons and earth spirits. They're cool and calm but they have wild impulses. They possess a combination of strength and skill and are skilled with blades and can cut through anything that gets in their way."):
        "Una creatura soprannaturale che ha lati da dio, da demone e da spirito della terra, ma in origine era un uomo. È freddo e pacato, ma dentro nasconde impulsi violenti. Mette insieme la forza e la tecnica, è maestro nel maneggiare le lame, e chi gli si mette in mezzo lo squarta e lo toglie di torno.",

    # ---------------------------------------------------------- :5555 il demone frantumatore
    (5555, 'They were originally human though they have aspects such as gods demons and earth spirits. They have a rugged personality and are extremely powerful shattering and eliminating anything that gets in their way. It is possible to hit it off with them and get to know them well.'):
        "Una creatura soprannaturale che ha lati da dio, da demone e da spirito della terra, ma in origine era un uomo. Ha un carattere rude ed è fortissimo: chi gli si mette in mezzo lo frantuma in mille pezzi e lo toglie di torno. Ogni tanto però si trova bene con qualcuno e ci fa amicizia.",

    # ---------------------------------------------------------- :5568 l'alieno da battaglia
    (5568, 'An alien that specializes more in combat. It has taken in the genes of a parasitic organism from the past and its intelligence and physical abilities are beyond those of ordinary aliens. It actively uses acidic mucus as a weapon.'):
        "Un alieno ancora più specializzato nel combattimento. Si è preso dentro i geni degli esseri che ha parassitato in passato, e per intelligenza e prestanza fisica un alieno comune non gli sta nemmeno vicino. Il suo muco acido lo usa volentieri come arma.",

    # ---------------------------------------------------------- :5581 l'insetto corazzato da guerra
    (5581, 'An ant-like behemoth that has been enhanced for combat by space technology. Overall ability has been increased with significant enhancements to the shell and acid eruption power. The stealth performance is down though due to the color.'):
        "Un essere gigantesco simile a una formica, potenziato per il combattimento con la tecnologia dello spazio. Le capacità gli sono cresciute su tutta la linea, ma soprattutto la corazza e la forza con cui schizza l'acido. In compenso, per via del colore, passa inosservato molto meno.",

    # ---------------------------------------------------------- :5594 il ragno feroce d'acciaio
    (5594, "A spider-like behemoth enhanced by space technology. It has a steel-like body and tremendous jumping power. It spits out a thread of kneaded acid but it is incompatible with Irva's atmosphere so the thread breaks down and only the acid splashes out."):
        "Un essere gigantesco simile a un ragno, potenziato con la tecnologia dello spazio. Ha un corpo che pare d'acciaio e un salto prodigioso. Sputa un filo impastato di acido, ma con l'aria di Irva non va d'accordo: il filo si disfa e resta solo l'acido, che schizza dappertutto.",

}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-011.jsonl'
DA, A = 5101, 5600
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_card.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_102-dacard.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
