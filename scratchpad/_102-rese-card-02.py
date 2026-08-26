# -*- coding: utf-8 -*-
"""102a - Lotto 2 di `db_card.hsp`: le carte fra la riga 601 e la 1100 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e per la
rete che lo misura (`scratchpad/_102-carta-conoscenza.py`).

⚠️⚠️ **QUATTRO CHIAVI DI QUESTA ZONA FINISCONO CON UNO SPAZIO** — `:810`,
`:836`, `:875`, `:940` — perche' l'inglese di monte ce l'ha. Chi ricopia la
chiave leggendola da un dossier lo perde, e la rete 1 dice «voce senza resa»
senza spiegare perche'.

⭐ **Il fungo e il batterio non sono la stessa cosa, e a distinguerli e'
l'inglese.** `glossario.md` fissa 菌 → «il fungo» quando e' **il Meshera visto
da dentro**. In questa zona 細菌 compare tre volte: a `:680` e a `:693`
l'inglese di monte scrive **Meshera** (quindi e' il fungo), a `:719` scrive
**bacteria** e la carta e' un batterio coltivato in laboratorio davvero. La
distinzione non si deduce dal giapponese, che dice 細菌 in tutt'e tre.

⚠️ **ギガモール non aveva un nome italiano** e in `db_card.hsp` compare tre
volte (`:628`, `:5516`, `:7206`). `メガモール` e' gia' «la talpa gigante», e
`:7206` dice che la ギガモール e' dieci volte piu' alta e mille volte piu'
pesante: qui diventa **«la talpa colossale»**, e le altre due carte dovranno
dire la stessa cosa. Va in `glossario.md`.

⚠️ `《ギガモールの骨鎌》` e' reso `<Falce della Bestia>` (`db_item.hsp:141477`):
li' il nome era stato aggirato, e resta com'e'.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :602 la ragazza mina
    (602, 'Mentally ill girl who lives in a minefield just for the appeal of \\"poor me\\". They are troublesome because they can easily let their emotions go out and try to die together with you. Likes the combination of pink and black.'):
        "Una ragazza dall'umore instabile che vive in un campo minato solo per far vedere quanto sia da compatire. Fa esplodere le emozioni per un nulla e cerca di morire insieme a chi le sta accanto: è una bella grana. Le piace l'abbinamento di rosa e nero.",

    # ---------------------------------------------------------- :615 il verme dei cunicoli
    (615, 'Giant worms that are proliferating and rampaging in other dimensions. Troubled by the damage, interdimensional people have been exterminating them by dumping them into wormholes. The worms do not die even if they pass through the wormhole, they adapt and mutate, and materialize in our dimension.'):
        "Un verme enorme che si moltiplica e semina rovina in un'altra dimensione. Stremati dai danni, gli abitanti di là se ne liberano gettandoli in un cunicolo spaziotemporale. Solo che attraversarlo non li uccide affatto: si adattano, mutano e sbucano nella dimensione di qua.",

    # ---------------------------------------------------------- :628 il verme della morte vindaliano
    (628, "A giant worm that grows underground in the Vindale Forest. They move so slowly that quakes don't even occur, and they are the ones who cultivate the earth, when they are about to be eaten by the Gigamoles, they flee underground in a panic."):
        "Un lombrico gigantesco cresciuto nel sottosuolo della Foresta Eretica. Si muove così piano da non provocare nemmeno un tremito e ara la terra per chi ci vive, ma quando la talpa colossale sta per mangiarlo scappa in superficie in preda al panico.",

    # ---------------------------------------------------------- :641 la vermarchesa
    # ⓘ 家来の忠告もムシして e' un gioco fra 無視 «ignorare» e 虫 «insetto»: in
    #    italiano il gioco si rifa' con l'orecchio, non con la parola.
    (641, "She is the young lady of the worm world who grew up extremely spoiled. She tends to go out to dangerous places without heeding the advice of her retainers. She is a selfish worm who thinks that it doesn't matter what terrible things she says as long as she has a noble heart."):
        "La signorina del mondo dei vermi, cresciuta con ogni vizio possibile. Fa orecchie da verme ai consigli dei servitori ed esce volentieri dove è pericoloso. È un vermaccio capriccioso, convinto che basti avere un cuore nobile per potersi permettere qualunque cattiveria.",

    # ---------------------------------------------------------- :654 il verme curativo
    (654, 'Caterpillars with high healing and reproductive capacity. Its flesh, in particular, is believed to be effective in curing diseases. The captive population has escaped and there were concerns about environmental destruction, but they have not proliferated to that extent because wild animals and adventurers are eating them up.'):
        "Un bruco con grandi capacità di guarigione e di riproduzione. La sua carne, in particolare, passa per efficace contro le malattie. Gli esemplari allevati sono scappati e si temeva un disastro ambientale, ma animali selvatici e avventurieri se li mangiano a quattro palmenti, e così non si sono moltiplicati poi tanto.",

    # ---------------------------------------------------------- :667 il gordio grossissimo
    (667, "Gordian worm that have evolved to be extremely thick. It grows as a parasite in the digestive organs of giants and giant creatures. When it grows enough, it emerges from the host's body, which is too thick. The host is then ripped open as it tries to force its way out."):
        "Un gordio che si è evoluto fino a diventare grossissimo. Cresce da parassita nell'apparato digerente dei giganti e delle creature enormi. Quando è cresciuto abbastanza esce dal corpo dell'ospite, ma è troppo grosso per passare; e siccome forza lo stesso, l'ospite si squarcia.",

    # ---------------------------------------------------------- :680 il refrattario all'assimilazione
    # ⚠️ 細菌 qui e' il Meshera: l'inglese lo dice. E 素体 e' «materiale di
    #    partenza», il termine da laboratorio fissato in `glossario.md`.
    (680, 'Its entire body has been corrupted and transformed by Meshera. He is now a full-blown monster, but his base body is resisting assimilation with the last of its guts, thus greatly suppresses its fighting ability.'):
        "Il corpo intero è stato corroso dal fungo e ne è uscito trasformato. È un mostro a tutti gli effetti, ma il materiale di partenza resiste all'assimilazione con l'ultimo filo di grinta che gli resta, e anche così la sua forza vera resta molto compressa.",

    # ---------------------------------------------------------- :693 il batterio mostruoso
    # ⚠️ Anche qui l'inglese dice Meshera: il nome della carta viene da
    #    モンスターバクテリア, che e' il nome proprio, non la sostanza.
    (693, 'It seems that it was originally a monster that was around, but for some reason the Meshera in its body went out of control and it multiplied massively, taking over its body. They want the bodies of other creatures in order to multiply more.'):
        "Pare fosse un mostro qualunque dei dintorni, ma per qualche motivo il fungo che aveva in corpo è impazzito, si è moltiplicato a dismisura e gli ha preso possesso della carne. Per moltiplicarsi ancora gli servono i corpi di altre creature.",

    # ---------------------------------------------------------- :706 il Meshera Izuhigiria
    (706, 'Form in the process of mutation due to infection. From here, the mycelium further multiplies and joins together to form new limbs. The person who has become the prime body has fainted due to mental shock, but the real hell begins when he or she wakes up.'):
        "La forma intermedia della mutazione da contagio. Da qui il micelio continua a moltiplicarsi e a saldarsi, e si formano arti nuovi. L'uomo che gli ha fatto da materiale di partenza è svenuto per lo choc, ma l'inferno vero comincia quando si sveglia.",

    # ---------------------------------------------------------- :719 il batterio saltatore
    # ⭐ Qui l'inglese dice `bacteria` e non `Meshera`: e' un batterio davvero,
    #    coltivato in laboratorio, e la parola resta «batterio».
    (719, "An unusually large mass of bacteria. This is the result of researchers' curiosity to see how far it can grow under special conditions. It swells its well-developed flagellum, leaps and pounces on its prey."):
        "Un ammasso di batteri ingigantito fuori misura. È il risultato di ricercatori che, per pura curiosità, hanno continuato a coltivarlo in condizioni particolari per vedere fin dove arrivava. Ondeggia il flagello ben sviluppato, spicca un balzo enorme e piomba sulla preda.",

    # ---------------------------------------------------------- :732 il pirata rissoso
    (732, 'A rugged pirate trained on the rough seas. He believes that seasickness is not a physical problem, but something that can be solved with guts. He is shunned by his colleagues because he is so crude, and the captain treats him as a problem child because he is intuitive and acts on his own initiative.'):
        "Un pirata rude, temprato dal mare in tempesta. È convinto che il mal di mare non sia una faccenda del corpo, ma qualcosa che si risolve con la grinta. È talmente sgraziato che i colleghi lo evitano, e siccome agisce di testa sua e d'impulso il capitano lo tratta da piantagrane.",

    # ---------------------------------------------------------- :745 il moschettiere pirata
    (745, "A pirate skilled with firearms. They fight with the ship's cannons except in hand-to-hand combat, where they are more of an artilleryman because that is their main weapon. However, there seems to be a tendency among them to think that musketeers sound cooler."):
        "Un pirata che maneggia bene le armi da fuoco. Fuori dal corpo a corpo combatte con i cannoni della nave, e siccome quella è l'arma principale sarebbe più un artigliere. Fra loro, però, gira l'idea che moschettiere suoni meglio.",

    # ---------------------------------------------------------- :758 l'istigatore degli Elea
    (758, 'Juere, who is instigating Elea. He is a rogue who takes advantage of the Elea, who are unfamiliar with the climate of South Tyris, under the guise of providing support. He uses the persecution of the Elea as a shield to forcefully solicit money and supplies, but he has embezzled all of it and not a single gold coin has reached the Elea in need. He plans to disappear before he is about to be discovered.'):
        "Un Juere che aizza gli Elea. È un delinquente che sfrutta gli Elea, poco pratici del clima di Tyris del Sud, con la scusa di dare loro sostegno. Si fa scudo delle persecuzioni per raccogliere denaro e provviste con le maniere forti, ma intasca tutto, e agli Elea in difficoltà non arriva una moneta d'oro. Conta di sparire prima che lo scoprano.",

    # ---------------------------------------------------------- :771 il rivoltoso degli Elea
    (771, 'A mob that riots, shouts, destroys and loots to the hilt. To complicate matters, not all of them are outraged at what they have been subjected to by Elea. Some of them are mixed in with idiots who want to riot and festive idiots, but it is difficult to distinguish them from the truly angry ones. They are disliked by their own people because they lower the dignity of Elea.'):
        "Una massa che si scatena, urla, distrugge e saccheggia senza misura. La cosa complicata è che non sono tutti infuriati per quello che gli Elea hanno subito: in mezzo ci sono anche imbecilli che vogliono solo far casino e cretini che la prendono per una sagra, e distinguerli da chi è davvero in collera è difficile. Fanno perdere dignità agli Elea, e i loro stessi simili li detestano.",

    # ---------------------------------------------------------- :784 il vendicatore degli Elea
    (784, "Elea originally lived outside the Vindale Forest. They lost thier family due to harassment and lynching as a result of Zanan's advocacy of the eradication of Elea and instigation of conflict. Revenge is now the only purpose of thier life. They are prepared for the emptiness that will only remain after their revenge, and that they will not be able to bear it at all."):
        "Un Elea che in origine viveva fuori dalla Foresta Eretica. Quando Zanan si mise a predicare lo sterminio degli Elea e a soffiare sul fuoco, subì angherie e linciaggi e perse la famiglia. Ormai vive solo per la vendetta. Sa già che dopo la vendetta resterà soltanto il vuoto, e sa già che non riuscirà a reggerlo: ci va lo stesso.",

    # ---------------------------------------------------------- :797 il vagabondo degli Elea
    (797, 'Elea wanders from place to place in search of a safe haven. They tend to flee to Nefia after being persecuted, get picked up by criminals, die in the field and generally end up in the wrong place.'):
        "Un Elea che vaga di terra in terra in cerca di un posto dove stare in pace. Perseguitati, finiscono per rifugiarsi in Nefia, o raccolti da qualche criminale, o morti in un fosso: in un modo o nell'altro va quasi sempre a finire male.",

    # ---------------------------------------------------------- :810 la principessa ibrida <salma celeste>
    # ⚠️⚠️ Chiave con lo spazio in coda. Le sette principesse ibride condividono
    #    le prime due frasi: la resa e' identica in tutte e sette.
    (810, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. She believes that death is the salvation for all, and wanders around the country killing with her lifeless eyes. '):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Per lei la morte è la salvezza di chiunque, e con gli occhi spenti vaga di terra in terra ripetendo la sua carneficina. ",

    # ---------------------------------------------------------- :823 <squama magica>
    (823, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. She is concerned about her long torso and short legs and gets really pissed off when teased about it. Her tongue is very long and can be moved with considerable precision.'):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Le pesa avere il busto lungo e le gambe corte, e se la stuzzicano su quello va davvero in bestia. Ha una lingua lunghissima e la muove con notevole precisione.",

    # ---------------------------------------------------------- :836 <roccia e macchina>
    # ⚠️⚠️ Chiave con lo spazio in coda.
    (836, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. Her biological tissue has been replaced by rocks and nanomachines, but despite her appearance, she has a passionate heart. '):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Il tessuto vivo le si è sostituito con roccia e nanomacchine, ma malgrado l'aspetto ha un cuore caldo. ",

    # ---------------------------------------------------------- :849 l'eteriano avanzato
    (849, 'The etheric disease continued to progress after he was transformed into an Etherian, and this is what happened to him. Not a shred of human consciousness remains. They can no longer be restored by any magic or medicine. Death is the only salvation.'):
        "Anche dopo essere diventato eteriano la malattia dell'etere ha continuato ad avanzare, ed è finito così. Della coscienza umana non resta un frammento. Ormai non c'è magia né medicina che lo riporti indietro. Solo la morte è una salvezza.",

    # ---------------------------------------------------------- :862 <bestia e piuma>
    (862, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. She has excellent hearing, leg, arm and flight abilities, but is most proud of her fluffiness. She has a body odour that is a mixture of various animal smells, which she is unaware of, but which is quite strong.'):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Ha udito, gambe, braccia e volo eccellenti, ma va soprattutto fiera della propria morbidezza. Non se ne accorge, ma ha addosso un odore di bestie diverse mescolate insieme che è piuttosto forte.",

    # ---------------------------------------------------------- :875 <acqua e melma>
    # ⚠️⚠️ Chiave con lo spazio in coda.
    (875, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. She was troubled by a viscous fluid, which she did not understand why, being secreted from her entire body when she was excited, but only recently realised that this was her sweat. '):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. La tormentava un liquido vischioso che le usciva da tutto il corpo quando si eccitava, senza capirne il motivo; solo di recente ha scoperto che era il suo sudore. ",

    # ---------------------------------------------------------- :888 <insetto e verme>
    (888, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. Her favourite type is someone who gives her lots of food. She tends to be so absorbed in her meals that she loses sight of her surroundings, and tends to eat too much and get a flabby belly.'):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Il suo tipo ideale è chi le dà da mangiare in quantità. Si concentra talmente sul pasto da perdere di vista quello che ha attorno, e finisce sempre per mangiare troppo e ritrovarsi la pancia gonfia.",

    # ---------------------------------------------------------- :901 <fiore e spora>
    (901, 'Her birthplace is near the Vindale Forest. She has suffered from disfigurement in various parts of her body and was driven out of the human village. She is aware that she is a shady person and prefers to be quiet in a gloomy place. In reality, however, she dreams of being in a sunny place where she can enjoy the company of others.'):
        "È nata vicino alla Foresta Eretica. Il corpo le è tornato indietro agli antenati in più punti, e per questo l'hanno cacciata dal paese. Si sa creatura d'ombra e preferisce starsene zitta in un posto umido. In realtà, però, sogna di stare al sole a far baldoria con tutti gli altri.",

    # ---------------------------------------------------------- :914 l'eteriano
    # ⚠️ L'inglese di monte salta due frasi del giapponese e salda la prima con
    #    l'ultima: il peggioramento, il mostro senza ragione e la cura che non
    #    c'e' spariscono tutti. Si traduce il giapponese.
    (914, 'Formerly human. Apparently he had a condition that made him particularly vulnerable to the ether wind, although at first he only suffered from a deformed face. The deterioration will not stop unless a miracle occurs.'):
        "Un tempo era umano. Pare avesse una costituzione particolarmente debole all'etere, ma all'inizio se l'era cavata con la sola deformazione del viso. Poi i sintomi sono peggiorati, il corpo intero è mutato alla rinfusa, e oggi è un mostro senza più personalità né ragione. Bisognerebbe intervenire prima di arrivare a questo punto, ma una cura non esiste, e senza un miracolo il peggioramento non si ferma.",

    # ---------------------------------------------------------- :927 lo SP Champion
    # ⓘ SP sta per Shark Punching: 鮫殴りセンター compare **una volta sola** in
    #    tutto il sorgente, ed e' la palestra da cui il nome della carta viene.
    (927, 'A sea champion who evolved to go head-to-head with the Shark Punching Centre. He delivers a powerful counter to challengers who believe the falsehood that he is vulnerable to being hit on the tip of the nose. He does not wear a mouthpiece because his teeth grow back quickly.'):
        "Il campione dei mari, evolutosi apposta per fare a pugni ad armi pari con il Centro Pugilistico Antisqualo. A chi lo sfida credendo alla frottola che abbia la punta del muso come punto debole riserva un contrattacco tremendo. Siccome i denti gli ricrescono in fretta, per principio non porta il paradenti.",

    # ---------------------------------------------------------- :940 il pesce gatto Dagon
    # ⚠️⚠️ Chiave con lo spazio in coda. ダゴンズイ玉 e' la palla che i pesci
    #    gatto formano davvero (ゴンズイ玉), col nome del dio del mare dentro.
    (940, 'A fish that has taken in a piece of the sea god. It is a type of catfish, but it is quite unique in that it lives in the sea, has poisoned needles with a return on its fins, and forms a school called the Dagonzui Ball. '):
        "Un pesce che ha assorbito una scheggia del dio del mare. È una specie di pesce gatto, ma vive in mare, tiene nascosti nelle pinne aculei velenosi con la punta uncinata e forma banchi compatti detti palle di Dagon: insomma, ha una sua personalità. ",

    # ---------------------------------------------------------- :953 la Scilla muscolosa
    (953, "The tentacles on the lower half of the body are a mass of strong muscles. When they are strained, the muscles rise up and look like a dog's face. They usually engage in high-intensity muscle training in the deep sea, but occasionally come above ground to show off their muscles."):
        "I tentacoli della parte inferiore sono un blocco di muscoli tenacissimi. Quando ci mette forza i muscoli si gonfiano e pare assomiglino a un muso di cane. Di solito si allena ad alto carico negli abissi, ma ogni tanto sale in superficie per mettere in mostra i muscoli.",

    # ---------------------------------------------------------- :966 l'anemone di mare libidinoso
    # ⚠️ Il nome della carta e' maschile: la resa non passa al femminile a meta'
    #    carta, anche se l'inglese di monte lo fa. E クマノミ e' il pesce
    #    pagliaccio: l'inglese ha letto 熊 e ha scritto `bearfish`.
    (966, 'An anemone that is not actually particularly skanky. It has been given an obscene name by academics just because of its appearance and has always suffered from rumour-mongering. She loves her bearfish-kun, who understands who she really is and is with her.'):
        "Un anemone che, in realtà, non è affatto porcello. Gli studiosi gli hanno appioppato un nome osceno solo per l'aspetto, e da allora soffre della cattiva fama. Vuole bene al suo pesce pagliaccio, l'unico che lo capisca per quello che è e che gli stia accanto.",

    # ---------------------------------------------------------- :979 il delfino soldato
    (979, 'They were the originally intelligent marine creatures, developed science and technology and embarked on an invasion of the surface. He is intelligent and has a bright personality, but he is a scum who is only happy if he is having fun. He enjoys group assaults and drugs for the fun of it.'):
        "In origine era una creatura marina di alta intelligenza, poi ha sviluppato scienza e tecnica e si è messo a invadere la terraferma. Ha testa e carattere allegro, ma è un rifiuto che bada solo a divertirsi: si dà a pestaggi di gruppo e a droghe per puro spasso.",

    # ---------------------------------------------------------- :992 il calamaro provocatore
    (992, 'Disliked squid. He tries to make fun of others and joke about it, but becomes enraged when he is made fun of. He was turned back by a female oyster in an agitated fight and fled from the sea, leaving behind a message of rejection.'):
        "Un calamaro che nessuno sopporta. Sfotte gli altri e poi se la cava dicendo che scherzava, ma se sfottono lui va su tutte le furie. In una gara di sfottò l'ha spuntata un'ostrica femmina, e allora è scappato dal mare lasciando l'ultima parola, come si fa quando si perde.",

    # ---------------------------------------------------------- :1005 <Sist> la suora maggiore
    # ⚠️ Qui il «tu» ci vuole: あなた e' il giocatore, e la riga non ha un gemello
    #    con un PNG al posto suo. Vedi `guida-stile.md`.
    (1005, 'She is an older sister who is not blood related to you, and uses a basement in Ludus as her base of operations. She has awakened to the Sistergy waves and devotes her life to their study and propagation. Although she is frustrated with your lack of understanding, she is always waiting for your return.'):
        "La sorella maggiore che non ha il tuo sangue, e che tiene la sua base nei sotterranei di Ludus. Si è risvegliata all'Onda Sororale e si spende tutta per studiarla e diffonderla. Le dispiace che tu capisca così poco, ma aspetta sempre che tu torni.",

    # ---------------------------------------------------------- :1018 l'alraune infernale
    (1018, "A species of arlaune that is native to the underworld. It sees the inferno flower as its rival and is eager to expand its habitat. It tries to pierce its enemies with its magnificent stamen or spray them with thick pollen. It is best to stay away from them if you don't want a taste of Hell."):
        "Un'alraune originaria dell'Oltretomba. Considera il fiore infernale una rivale e si dà da fare per allargare il proprio territorio. Infilza i nemici con lo stame maestoso, oppure cerca di rovesciare loro addosso un polline denso. Meglio non avvicinarsi, se non si vuole assaggiare l'inferno.",

    # ---------------------------------------------------------- :1031 l'ambrosia molesta reale
    (1031, "A large subspecies of hogweeder. The pollen has become so powerful that when it is sprayed on an Indian elephant, the elephant's nose swells up to a size larger than its body. It is spreading a considerable amount of strong pollen, but it blames the cedar trees for all its sins."):
        "La sottospecie di taglia grande dell'ambrosia molesta. Il polline ha guadagnato potenza: soffiato addosso a un elefante indiano, gli gonfia la proboscide fino a farla più grossa del corpo. Ne sparge in giro una quantità notevole, ma della colpa incarica sempre i cedri.",

    # ---------------------------------------------------------- :1044 l'ambrosia molesta
    (1044, 'He is a hated species of plant that unilaterally attacks and drives away other plants and animals that get in his way with pollen from a safe distance. He is not well known for spreading his strong pollen, but he takes advantage of this and blames it all on the cedars, and enjoys stirring up conflict between cedars and humans.'):
        "Un individuo detestato, che dalla distanza di sicurezza attacca a senso unico col polline le piante e gli animali che gli danno fastidio, finché non se ne vanno. Che sia lui a spargere il polline forte non si sa granché, e lui ne approfitta per dare la colpa ai cedri e si diverte a soffiare sulla lite fra i cedri e gli uomini.",

    # ---------------------------------------------------------- :1057 l'alraune
    (1057, 'A type of mandrake with well-developed flowers. It is said that its pistils became humanoid in order to communicate with humans. They like to be clean and secretive, so they are happy if you wash them regularly and ask them questions.'):
        "Una specie di mandragora dal fiore molto sviluppato. Pare che il pistillo abbia preso forma umana per poter comunicare con il genere umano. Ama la pulizia e ama i segreti: se la si lava di tanto in tanto e le si fanno domande, è contenta.",

    # ---------------------------------------------------------- :1070 il cedro rancoroso
    (1070, 'Because of their resentment over being planted and exploited since ancient times, they retaliate by tormenting the human race with an intense pollen. In the past, a band of adventurers went to burn down a cedar mountain, but they were later found dead with pollen stuffed into every bodily cavity.'):
        "Piantati e sfruttati fin dall'antichità, si vendicano del rancore tormentando il genere umano con un polline violentissimo. Un tempo certi avventurieri partirono per dare fuoco a un monte di cedri: gli alberi si strinsero attorno a loro tutti insieme e li riempirono di polline in ogni orifizio, e li ritrovarono cadaveri.",

    # ---------------------------------------------------------- :1083 il Pinocipresso
    (1083, 'A cypress (hinoki) monster. The older he is, the more evil he is considered to be. If you make a doll from his log, you will create a piece of junk that will betray your good intentions without a care and will not listen to your advice. He hates study and hard work. He has a rotten character, but he also has a rotten brain, so he is easy prey for devious crooks.'):
        "Il mostro del cipresso. Più è vecchio, più lo si ritiene malvagio. Chi ricava un burattino dal suo tronco ottiene un rifiuto che tradisce la buona fede senza batter ciglio e che non ascolta consigli. Detesta lo studio e la fatica. Ha un pessimo carattere, ma anche poca testa, ed è quindi la preda ideale dei furfanti scaltri.",

    # ---------------------------------------------------------- :1096 il soldato oscuro verde
    # ⚠️ L'inglese salta la frase sull'attacco mentale: si traduce il giapponese.
    (1096, 'A lesser god that possesses the power of an evil spirit. From its head, it emits a monstrous light that eats away at the spirit. Although she has two female personalities living together in one body, they seem to get along well without any particular quarrels.'):
        "Una divinità minore in cui abita la forza del dio oscuro. Dalla testa emette una luce mostruosa che corrode la mente. Attacca soprattutto lo spirito, quindi con gli avversari poco intelligenti fa fatica. In un corpo solo convivono due personalità femminili, ma pare che vadano d'accordo e non litighino affatto.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-002.jsonl'
DA, A = 601, 1100
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
