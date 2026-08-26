# -*- coding: utf-8 -*-
"""103a - Lotto 10 di `db_card.hsp`: le carte fra la riga 4601 e la 5100 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_103-rese-card-07.py` per le decisioni della giornata.

⭐ **Gia' deciso altrove:** `ミノタウロス` → **il minotauro**, `ケンタウロス`
→ **il centauro** (`db_card.hsp:4924`), `ウィスプ` → **il fuoco fatuo**
(`:14026`), `バフォメット` → **il Baphomet**, `地雷犬` → **il cane mina**
(`:13974`), `ブルーバブル` → **la bolla azzurra** (`:10917`), `なめくじ` →
**la lumaca**, `かたつむり` → **la chiocciola**, `イルヴァ` → **Irva**,
`シズルコード` → **il Codice di Ssil** (deciso nel lotto 9, `:4580`).

⚠️ **`ハム将軍` non e' una creatura del gioco**: compare **solo** dentro questa
prosa (`grep` su `db_card.hsp`, `db_creature.hsp` e `action.hsp`: un solo sito).
Non c'e' un nome gia' reso da rispettare, quindi segue il fratello maggiore
`ハム大老` → «il criceto gran anziano»: qui e' **il criceto generale**.

⚠️⚠️ **Tre errori di monte, tutti presi dal giapponese:**
- `:4788` 老いたハムスターが化けたもの vuol dire *un criceto invecchiato che
  si e' trasformato* (in uno yokai). L'inglese scrive «An elderly hamster
  disguised as an older hamster», che non dice niente.
- `:4879` 胴体に乗せることを嫌う: il centauro non vuole **nessuno in groppa**.
  L'inglese legge «doesn't like to be put on his armor».
- `:5074` 野生のかたつむり sono **chiocciole**, non «wild beetles».

⚠️ **Tre giochi di parole che l'italiano non puo' tenere, e uno che tiene.**
`イリス` e' la dea Iris **dentro** リス, scoiattolo; `テロリス` e' テロリスト
col medesimo innesto; `ブルーブル` incastra ブルー (avvilito), ブルブル震える
(tremare) e la ブルーバブル che nomina in coda. Tutt'e tre stanno **nel nome**,
non nella prosa, e i nomi sono gia' resi: la prosa non ci prova.
⭐ Tiene invece `:4697`: 全ては亀のみぞ…もとい、神のみぞ知る e' 亀 (tartaruga)
al posto di 神 (dio) nel modo di dire, e in italiano *lo sa soltanto la
tartaru... pardon, soltanto il cielo* fa esattamente lo stesso scherzo.

⚠️ **`:4931` ha un materiale inventato**: ショクパンヨリフランスパン, cioe'
«pancarre'-piuttosto-baguette». E' un nome, e va reso come nome, non spiegato.

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`. In CP932 il resto diventa doppia larghezza.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :4606 <Bethel> il falco bianco
    (4606, 'A white hawk that shakes off the urge to flee to drugs and deep sorrow and flutters into the sky again. Despite being affected by the aftereffects he is steadily regaining the power he had in his prime.'):
        "Il falco bianco che si è scrollato di dosso il dolore profondo e la voglia di rifugiarsi nella droga, e ha ripreso a battere le ali verso il cielo. Gli strascichi si fanno ancora sentire, ma sta tornando senza incertezze alla forza dei suoi anni migliori.",

    # ---------------------------------------------------------- :4619 <Egelveil> il demone dei vincoli
    (4619, 'She is a perverted demon who loves to be both bound and treated. She was thrown into a giant castle by the gods but her powers are not as limited as the other demons. It seems that the effect was less effective because of the ability she possessed.'):
        "Un demone dai gusti rovesciati: adora legare e adora essere legato. Gli dei l'hanno sbattuta dentro il castello immenso, ma i suoi poteri non sono limitati quanto quelli degli altri demoni. Si pensa che il sigillo abbia fatto meno presa proprio per via della facoltà che si ritrova.",

    # ---------------------------------------------------------- :4632 il coniglio del terrore
    (4632, 'The embodiment of fear. It is a caring person and when it gets lonely it will die etc. A lie of course. So it attracts everyone and creates a hell of a scene.'):
        "Il terrore fatto carne. È uno di quelli che vogliono attenzione a tutti i costi: con la scusa che se resta solo muore, che è una bugia bella e buona, si tira addosso chiunque gli capiti e ne ricava un inferno di urla e di strazio.",

    # ---------------------------------------------------------- :4645 l'iris
    # ⚠️ Il nome incastra la dea Iris nello scoiattolo (リス): sta nel nome, e
    #    il nome e' gia' reso. La prosa non ci prova.
    (4645, 'The goddess of the rainbow once defeated by the goddess of the wind in a great war between the gods which tore her body apart...these squirrels houses the pieces. When they are newborn their bodies glow a rainbow of colors due to the dominance of the fragments.'):
        "Ai tempi della grande guerra fra gli dei, la dea dell'arcobaleno fu sconfitta dalla dea del vento e ne ebbe il corpo squarciato: questo scoiattolo ospita una di quelle schegge. Appena nato la scheggia lo domina più che mai, e allora il corpo gli si accende dei colori dell'arcobaleno.",

    # ---------------------------------------------------------- :4658 il dio lepre bianca
    (4658, 'A pure white rabbit. It has a weak but divine power because it was raised as a god. Ancestral memories are strongly imprinted in its genes and it is not good at sharks. They are said to be good at matching couples.'):
        "Un coniglio bianchissimo. A furia di essere innalzato a divinità si ritrova un potere divino, debole ma vero. La memoria degli antenati gli è rimasta stampata a fondo nel sangue, e per questo con gli squali non se la sente. Pare che la sua specialità sia far nascere le coppie.",

    # ---------------------------------------------------------- :4671 il coniglio ghoul
    (4671, 'A monster lurking in rabbit society. They are also called corpse-eating rabbits because they dig up graves at night and devour the bodies. It attracts not only rabbits but also other creatures and uses them as food.'):
        "Un mostro che si nasconde dentro la società dei conigli. Notte dopo notte scava nelle tombe e divora i corpi, e per questo lo chiamano anche il coniglio mangiacadaveri. Non attira soltanto i conigli: adesca anche le altre creature e se le mangia.",

    # ---------------------------------------------------------- :4684 lo scoiattolo terrorista
    (4684, 'They act on the idea that squirrels are the most noble creatures on earth. They demanded land surrender and unconditional surrender but were naturally refused so they went on an indiscriminate subversive campaign.'):
        "Agisce partendo dal principio che lo scoiattolo sia la creatura più nobile che ci sia sulla terra. Ha preteso qua e là la consegna delle terre e la resa senza condizioni; naturalmente gli hanno detto di no, e allora si è dato alla distruzione a casaccio.",

    # ---------------------------------------------------------- :4697 il coniglio tartaruga
    # ⭐ Il bisticcio 亀のみぞ / 神のみぞ知る si tiene di peso in italiano.
    (4697, 'A synthetic beast of a rabbit and a tortoise. There was a race between a rabbit and a tortoise a long time ago and I wonder what the outcome would have been if this creature had been there. All things are in the hands of the tortoise... and God knows.'):
        "Una bestia sintetica, metà coniglio e metà tartaruga. Tanto tempo fa pare ci sia stata una gara di corsa fra una lepre e una tartaruga: chissà come sarebbe andata a finire se quel giorno ci fosse stata anche questa creatura. Lo sa soltanto la tartaru... pardon, soltanto il cielo.",

    # ---------------------------------------------------------- :4710 il razziatore oscuro
    (4710, 'The giant bat lives in the mirror world. It has adapted to this side of the world through repeated survival. It flies in the sky like a swift wind. They are obsessive and once they have attempted to prey on their prey they target them thoroughly.'):
        "Un pipistrello gigantesco che abita il mondo dello specchio. A furia di sopravvivere una volta dopo l'altra si è adattato anche al mondo di qua. Corre per il cielo come una raffica di vento. È di quelli che non mollano: la preda che ha deciso di mangiarsi una volta se la tiene di mira fino in fondo.",

    # ---------------------------------------------------------- :4723 il kapapukamui
    (4723, "The bat god. A hero who under the cover of darkness protects people from disease and demons. It often gets mistaken for a normal bat and is attacked by the people it is supposed to protect. It's good at playing dead."):
        "Il dio dei pipistrelli. Un eroe che, confondendosi con il buio, difende la gente dalle malattie e dai demoni. Il suo cruccio è che lo scambiano spesso per un pipistrello qualunque e finisce attaccato proprio da quelli che dovrebbe proteggere. La sua specialità è fingersi morto.",

    # ---------------------------------------------------------- :4736 il combattistrello
    (4736, 'Bats have learned their own fighting skills by observing the humans at war from a distance. They learned how to handle the guns and even learned the foul-mouthed abuse of the soldiers.'):
        "Un pipistrello che, osservando da lontano gli uomini che si facevano la guerra, si è imparato da sé la tecnica del combattimento. Ha imparato a maneggiare le armi da fuoco, e insieme a quelle si è imparato anche il turpiloquio dei soldati.",

    # ---------------------------------------------------------- :4749 il momotuka
    (4749, "It looks to be a very large bat but it seems to be a monster. They live in a hole in the tree and lure people in with the cries of children. Kids who like it will be snatched and kids and adults who don't will be bitten by it."):
        "Sembrava un pipistrello smisuratamente grosso, e invece pare che sia uno spirito. Abita nel cavo di un albero e attira la gente col pianto di un bambino. I bambini che gli piacciono se li porta via; quelli che non gli piacciono, e gli adulti, li morde e basta.",

    # ---------------------------------------------------------- :4762 il ratto sommo
    (4762, "The rats have awakened to their ultimate power. It's no different in size from a normal rat but it's fighting power is much different. In addition there is a saying that they bite and kill the ultimate rat cat and eventually kill the Indian elephant."):
        "Un topo che si è risvegliato alla forza suprema. Di taglia non è granché diverso da un topo comune, ma la forza in combattimento è un'altra cosa. Ed è talmente feroce che c'è perfino un detto: il ratto sommo ammazza il gatto a morsi, e già che c'è ammazza anche l'elefante indiano.",

    # ---------------------------------------------------------- :4775 il disastro
    (4775, 'A giant hamster that is considered a symbol of disaster. Its voracious appetite and fecundity will devour the food in the area. In addition the trees and pillars are gnawed by the ever-growing front teeth so no forests or buildings are left behind.'):
        "Un criceto gigantesco, che passa per il simbolo della calamità. Con quell'appetito smisurato e quella facilità a riprodursi divora tutto il cibo della zona. E siccome per limarsi gli incisivi, che gli crescono senza mai fermarsi, si mette a rosicchiare alberi e pilastri, non restano in piedi né i boschi né gli edifici.",

    # ---------------------------------------------------------- :4788 il criceto gran anziano
    # ⚠️ 化けたもの = trasformato in uno spirito, non «disguised as an older
    #    hamster» come legge l'inglese.
    (4788, 'An elderly hamster disguised as an older hamster. In the hamster world he is the highest ranking being in the service of General Ham. They often escape to play so there are a number of substitutes.'):
        "È un criceto che, invecchiando, si è trasformato in altro. Nel mondo dei criceti è il grado più alto al servizio del criceto generale. Siccome scappa di continuo per andare a giocare e non lo si trova mai, di sostituti ce n'è più d'uno.",

    # ---------------------------------------------------------- :4801 l'Asterio
    (4801, 'A cattleman with the same name as the alias of the first Minotaur. The name means star or thunderbolt. Only those with divine strength among the minotaurs are allowed to call themselves so.'):
        "Un uomo toro che porta lo stesso nome con cui si chiamava anche il primo minotauro. È un nome che vuol dire stella, e anche lampo. Fra i minotauri, a chiamarsi così sono ammessi soltanto quelli che hanno una forza da far pensare a un dio.",

    # ---------------------------------------------------------- :4814 lo Chiyou
    (4814, 'A human body with the head and hooves of a cow. He is now a monster but he was once a god of weapons. His personality is brave and patient and he has the ability to control the fog.'):
        "Ha corpo d'uomo, testa e zoccoli di bue. Oggi lo trattano da mostro, ma in origine era il dio delle armi. Di carattere è coraggioso e paziente, e ha la facoltà di comandare la nebbia.",

    # ---------------------------------------------------------- :4827 il toro blu
    # ⚠️ Il nome incastra ブルー (avvilito), ブルブル (tremare) e la bolla
    #    azzurra che nomina in coda. In italiano resta la sola immagine.
    (4827, "A bull with a blue body and tremendous power. They are blue from not being able to control their own power and are often burbling and shaking. I've never spoken to them directly but I feel somehow familiar with the Blue Bubble."):
        "Un toro dal corpo azzurro, che dentro nasconde una forza spaventosa. Non riuscendo a controllarla gli viene il magone, e se ne sta lì a tremare come una foglia. Con la bolla azzurra non ci ha mai parlato di persona, ma prova per lei una specie di simpatia.",

    # ---------------------------------------------------------- :4840 il bovino
    (4840, 'They have been domesticated for milking and for meat since ancient times. The cattle are considered sacred as ancestors by the minotaurs and the minotaurs sometimes attack people in order to free the cattle.'):
        "Fin dall'antichità più remota lo tengono come bestia da allevamento, per il latte e per la carne. I minotauri lo venerano come antenato, e pare che a volte assalgano gli uomini proprio per liberare i bovini.",

    # ---------------------------------------------------------- :4853 il mastallone
    (4853, 'Rare among the centaurs he excels in magic and melee combat. He has a flair for flamboyance making his original shiny armor glow with even more magical power. Basically there are only males.'):
        "Fra i centauri è raro: eccelle insieme nella magia e nel combattimento ravvicinato. Ama farsi notare, e l'armatura, che è già lucida di suo, se la fa pure risplendere con il potere magico. Di regola ne esistono soltanto maschi.",

    # ---------------------------------------------------------- :4866 il cavallo nero
    (4866, "A horse that has been strengthened with the power of darkness. His abilities are unknown and he does not receive much attention or expectation from the general public. Dark Horse itself on the other hand isn't concerned about that assessment."):
        "Un cavallo rinforzato dalla forza delle tenebre. Quanto valga davvero non lo sa nessuno, e la gente non gli bada e non si aspetta niente da lui. Al cavallo nero, però, quel giudizio non fa né caldo né freddo: gli entra da un orecchio ed esce dall'altro.",

    # ---------------------------------------------------------- :4879 il centauro cavaliere
    # ⚠️ 胴体に乗せる = farsi montare in groppa. L'inglese legge «armor».
    (4879, "A centaur wearing full body armor. He prefers to fight alone and has a high level of pride and fighting power. He doesn't like to be put on his armor unless his opponent is very skilled."):
        "Un centauro coperto da un'armatura completa. Preferisce combattere da solo, e ha tanto orgoglio quanta forza. A meno che non si tratti di qualcuno con cui ha davvero confidenza, non sopporta di farselo montare in groppa.",

    # ---------------------------------------------------------- :4892 il ballistallone
    (4892, 'A military horse trained to handle a small ballista on its own. Even with the muscle strength of a horse the ballista seems to be quite heavy and it cannot be shot unless it stops its feet and takes a posture.'):
        "Un cavallo da guerra addestrato a servire da solo una balista, purché sia di quelle piccole. Nemmeno con i muscoli di un cavallo la balista è leggera, a quanto pare: per sparare deve fermarsi e mettersi in posizione.",

    # ---------------------------------------------------------- :4905 il pistolauro
    (4905, 'The centaurs have switched from bows and arrows to guns. It excels in reflexes and athleticism such as shooting a distant Indian elephant between the eyebrows while sprinting. Their favorite thing is bolt action.'):
        "Un centauro che ha lasciato l'arco per l'arma da fuoco. Ha riflessi e prontezza fuori dal comune: mentre corre a perdifiato prende un elefante indiano lontanissimo in mezzo agli occhi. La cosa che gli piace di più è l'otturatore a scorrimento.",

    # ---------------------------------------------------------- :4918 il centauro
    (4918, 'A half-man half-horse creature. Their center of gravity is more forward than a normal horse so if they try to lean forward they might fall over. They live by hunting and farming in herds.'):
        "Una creatura metà uomo e metà cavallo. Ha il baricentro più avanti di un cavallo normale, e se prova a sporgersi in avanti rischia di ribaltarsi. Vive in gruppo, di caccia e di agricoltura.",

    # ---------------------------------------------------------- :4931 lo spirito del pane
    # ⚠️ ショクパンヨリフランスパン e' un nome inventato, non una spiegazione.
    (4931, "A spirit who loved the bread too much became one with the freshly baked bread. Sixty percent of the bread's constituents have been transformed into a mysterious super-hard substance called shoku panyori French bread. He uses his hardness to destroy objects with his body hit."):
        "Uno spirito che amava il pane troppo, e che si è fatto tutt'uno con una pagnotta appena sfornata. Il sessanta per cento di quello che compone il pane si è mutato in una misteriosa sostanza durissima chiamata megliobaguettechepancarré. Quella durezza se la sfrutta: distrugge le cose prendendole a testate.",

    # ---------------------------------------------------------- :4944 il fuoco fatuo selvaggio
    (4944, 'A wisp fused with countless souls. It burns fiercely under the influence of a soul crazed with anger and hatred. Its movements are slow but it is difficult to escape because it pulls the body and soul of the opponent towards it.'):
        "Un fuoco fatuo che si è fuso con anime a non finire. Sotto l'influenza di quelle impazzite di rabbia e di odio arde con una violenza tremenda. Si muove lento, ma scappargli via è difficile: tira a sé il corpo dell'avversario con tutta l'anima dentro.",

    # ---------------------------------------------------------- :4957 il nuvoldrago
    (4957, 'An extremely developed discharge cloud that has been transformed by taking in a large amount of water vapor. It has a huge impact on the weather. They live by hunting birds while hovering in the air as if they were being swept away by the wind whenever the wind blows.'):
        "È una nube temporalesca cresciuta fino all'estremo, che a forza di inghiottire vapore acqueo ha cambiato forma. Sul tempo atmosferico pesa parecchio. Vive cacciando uccelli mentre galleggia lassù in alto, portato dove tira il vento e dove gli gira, come se lo trascinasse la corrente.",

    # ---------------------------------------------------------- :4970 il nucleo dei moai
    (4970, "It features a moai extending from the core on all four sides. The moai part is a strong shield as well as a propulsion device. To prevent the core from taking damage the moai's stone head parries the attack."):
        "Lo si riconosce dai moai che gli si allungano dal nucleo verso i quattro lati. La parte dei moai è insieme il propulsore e uno scudo solido. Perché il nucleo non prenda danno, sono le teste di pietra dei moai a incassare i colpi.",

    # ---------------------------------------------------------- :4983 il monolito di mana
    (4983, 'A complex magic circuit is carved into the board and a huge amount of magic can be stored in the board. It has been given a provisional life and is capable of autonomous action. It is secretly tested and operated as a magical power supply device for the front lines and as a magical power battery for facilities.'):
        "Porta inciso un circuito magico complicato, e nella lastra può accumulare una quantità enorme di potere magico. Gli hanno dato una vita provvisoria, e così si muove da sé. Lo stanno provando di nascosto come rifornitore di potere magico per la prima linea e come batteria magica per gli impianti.",

    # ---------------------------------------------------------- :4996 il minamoai
    (4996, "A troubled moai scattering landmines. With sensors that are more powerful than necessary he doesn't get caught by mines himself. He is regarded as a rival by landmine dogs but he doesn't seem to care about that."):
        "Un moai fastidioso che semina mine a più non posso. Monta sensori più potenti del necessario, e nelle mine non ci finisce mai lui. Il cane mina lo tratta da rivale, ma a lui della faccenda pare non importi niente.",

    # ---------------------------------------------------------- :5009 il mietitore
    (5009, 'A demon that was used by the previous god of harvest. It is said that on a night of heavy rains a batch of headless corpses grew out of them. Many related lore survives throughout the world and today the term reaper generally refers to this demon.'):
        "Un mostro che il precedente dio del raccolto teneva al proprio servizio. Si racconta che in una notte di pioggia battente ne siano spuntati tutti insieme da certi cadaveri senza testa. Di leggende su di lui ne restano tante in ogni parte del mondo, e oggi, quando si dice la morte, di solito si intende lui.",

    # ---------------------------------------------------------- :5022 il non morto blasfemo
    (5022, 'It is the result of those who try to transcend death and meddle with the taboo. He deciphered a part of a magic book called the Ssil Code and used its magic to bring the undead into his body but failed. In truth they should have fused beautifully and sprouted three pairs of wings.'):
        "È il punto d'arrivo di chi ha voluto superare la morte e ha messo le mani sul proibito. Decifrò una parte del libro di magia che chiamano il Codice di Ssil e, con quell'arte segreta, si fece entrare in corpo un non morto: ma andò male. Nelle intenzioni i due dovevano fondersi alla perfezione, e sarebbero dovute spuntare tre paia d'ali.",

    # ---------------------------------------------------------- :5035 la mikscxifona
    (5035, "A gnarled ghost created by a necromancer somewhere. The name is also intact meaning Tsugihagi in an ancient artificial language. The body is unbalanced due to the forced installation. The ego is far from unbalanced it's broken."):
        "Uno spettro rattoppato, opera di un negromante di chissà dove. Anche il nome dice quello e nient'altro: in un'antica lingua artificiale vuol dire proprio rattoppato. I pezzi glieli hanno attaccati a forza, e il corpo è tutto sbilanciato. L'io, più che sbilanciato, è andato in pezzi da un pezzo.",

    # ---------------------------------------------------------- :5048 <Shuraida> il mercenario veterano
    (5048, "Concerned about being consumed by the war between the nations he gathered his comrades and formed a mercenary group. He has saved his comrades many times with his superior survivorship and many mercenaries look up to him as a mentor. When he's not working as a mercenary he's farming at his parents' house."):
        "Si chiese perché mai dovesse lasciarsi consumare nelle liti fra un paese e l'altro, e allora raccolse dei compagni e mise in piedi una compagnia di ventura. Ha salvato i commilitoni infinite volte, tanto sa cavarsela, e non pochi mercenari lo prendono per maestro. Quando non c'è lavoro da mercenario, torna a casa dei suoi a fare il contadino.",

    # ---------------------------------------------------------- :5061 <Roatonis> il demone della pestilenza
    (5061, 'The black aura is the main body. It operates by manipulating the corpse of Baphomet. The germs are generated and controlled by magic to cause great damage. But the infection is based on germs from the time of the sealing and without control it is almost ineffective against modern creatures in Irva.'):
        "Quello vero è l'alone nero: si muove manovrando il cadavere di un Baphomet. Genera e governa i batteri con la magia, e i danni che ne vengono sono enormi. Solo che i batteri da cui parte sono quelli di quando lo sigillarono, e senza il suo governo sulle creature della Irva di oggi non fanno quasi niente.",

    # ---------------------------------------------------------- :5074 la lumaca dell'oscurità
    # ⚠️ 野生のかたつむり sono chiocciole, non «wild beetles».
    (5074, "A slug that has been thoroughly enhanced with dark magic. A vicious wizard somewhere created it for fun and released it into the open air where it multiplied greatly. The wild beetles think it's dark and unapproachable."):
        "Una lumaca rinforzata da cima a fondo con la magia oscura. Un mago malintenzionato di chissà dove la creò per puro divertimento e la liberò all'aperto, e quella si moltiplicò a dismisura. Le chiocciole selvatiche dicono di lei che è un tipo cupo, e che avvicinarla mette soggezione.",

    # ---------------------------------------------------------- :5087 la chiocciola fortezza
    (5087, 'Originally an ordinary shell the snail was equipped with a high-powered cannon and machine gun at the request of humans. Unfortunately the balance control is too difficult to handle and it seems that it is all it can do is shoot the machine gun in single shots.'):
        "Il guscio in origine era di quelli normali, poi la chiocciola si è fatta montare dagli uomini un cannone e una mitragliatrice di tutto rispetto. Purtroppo tenere l'equilibrio è troppo difficile e non riesce a governarli: pare che il massimo che sappia fare sia sparare colpi singoli con la mitragliatrice.",

    # ---------------------------------------------------------- :5100 la chiocciola kamikaze
    (5100, 'They believe that this will lead to the prosperity of the Snail family and they are willing to put their lives on the line. They charge at you with explosives packed into their shells but most of the time they are dealt with before you can approach them. Its life is so light that it flutters in the wind...'):
        "Ci mette la vita, convinta che così la stirpe delle chiocciole prospererà. Si riempie il guscio di esplosivo e carica, ma quasi sempre la sistemano prima ancora che sia arrivata. La sua vita è leggera al punto di volare via nel vento...",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-010.jsonl'
DA, A = 4601, 5100
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
