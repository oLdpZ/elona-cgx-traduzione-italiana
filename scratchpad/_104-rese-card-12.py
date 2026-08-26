# -*- coding: utf-8 -*-
"""104a - Lotto 12 di `db_card.hsp`: le carte fra la riga 5601 e la 6100 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_104-rese-card-11.py` per le decisioni della giornata.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `メシェーラ` → **il Meshera**
(`chat.hsp:7652`, maschile), `レミード遺跡` → **le Rovine di Remido**
(`chat.hsp:7903`), `ザナン` → **Zanan**, `イルヴァ` → **Irva**, `ジラ` → **lo
zilla**, `ミノタウロス` → **il minotauro**, `人狼` → **il lupo mannaro**,
`クトゥグア` → **il Cthugha** (`:6042`), `ナイアーラトテップ` → **il
Nyarlathotep** (`:9812`), `中級神` → **divinita' di medio rango**
(`chat.hsp:9460`), `黄金の騎士` → **il cavaliere dorato** (`action.hsp:16890`)
e il loro `騎士団` sono **i Cavalieri Dorati** (`chat.hsp:12337`, `:12520`),
`生体兵器` → **arma biologica**, `精霊` → **spirito** (`chat.hsp:2083`).

⚠️ **La sorella di `<Fron>` si chiama Leah, non Lia.** `リア` e' gia' reso
**Leah** in `chat.hsp:7763`, dove le due sono nominate insieme come cugine.

⚠️⚠️ **Quattro errori di monte, tutti presi dal giapponese:**
- `:5646` 破壊の神が再生のために破壊を行うのに対し、**こちら**は… mette a
  confronto il **dio della distruzione** e **questo demone**. L'inglese si
  inventa un «God of Creation» e attribuisce al dio della distruzione la frase
  che parla del demone: il paragone esce rovesciato;
- `:5672` 比較にならないほどのパワーファイター e' *incomparabilmente* piu'
  forte. L'inglese scrive «in comparison to the Minotaur», che dice il
  contrario di 比較にならない;
- `:5763` ほぼ全ての状態異常と属性が**効かない**巨人 e' *un gigante su cui
  quasi nessuna alterazione e nessun elemento fa presa*. L'inglese legge
  «A giant with almost all health problems and no attributes», cioe' un gigante
  malato: e' esattamente il rovescio della sua carta;
- `:5867` 外法 sono le **arti proibite**, non «foreign laws».

⭐ **Due citazioni con una forma italiana gia' fatta.** `:5802` e' Muhammad Ali
— 蝶のように舞い、蜂のように刺す, *vola come una farfalla, pungi come un'ape* —
e si rende con quella. `:5776` e' l'effetto farfalla, e il nome della carta
(`la farfalla dell'uragano`) lo dice gia'.

⚠️ **`:5620` e `:5659` hanno un bisticcio ciascuno, e uno solo si tiene.**
`夜更かしならぬ朝更かし` incastra *far le ore piccole* di notte e di mattina, e
in italiano regge tale e quale. `宇宙ミミズク` invece spiega perche' si chiama
cosi' — ミミ, *orecchie*, dentro ミミズク — e il nome e' gia' reso «il gufo
spaziale»: la prosa dice la ragione senza fingere il bisticcio.

⚠️ **`:5737` porta una glossa di lettura che l'inglese butta**: 妄人はワンニン
と読む, *妄人 si legge wangnin*. E' l'unica riga che spiega il nome della carta,
e in italiano diventa la nota sulla pronuncia.

⚠️ **`:5412`-stile: `:5685` chiude su un bisticcio che sta nel NOME.**
`クラーゲン` incastra クラゲ (medusa), クラーケン e コラーゲン (collagene). Il
nome e' gia' `la medusa kraken`; la coda sul collagene si rende dritta, che e'
anche quel che fa il giapponese.

⚠️ **`:5997` e `:6010` aprono con le STESSE DUE frasi giapponesi**, e vanno
rese identiche. Cosi' `:5711`, `:5841` e `:5854`, che condividono la formula
`精霊が◯◯を象って実体化した存在`.

⚠️ **`厄病神` di `:5828` e' il modo di dire**, non la creatura: *portasfortuna*.
E' il gemello di `疫病神` del lotto 11, che li' era letterale.

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`. Le 「」 di `:5893` si sciolgono nella frase, e le cifre a doppia
larghezza (`Ｇ`) si scrivono con la lettera normale.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :5607 lo spaziozilla
    (5607, 'A lone zilla caught in a hypergravity collapse. As it drifted through the unstable space its body took in various things and reconfigured itself. It absorbs energy and creates a duplicate of itself from the crystals in its body.'):
        "Uno zilla rimasto preso in un collasso di gravità estrema. Mentre andava alla deriva in uno spazio anomalo e instabile, il corpo gli si è ricomposto inglobando ogni sorta di cose. Assorbe energia e dai cristalli che ha dentro genera copie di sé stesso.",

    # ---------------------------------------------------------- :5620 il passero della notte
    (5620, "A sparrow demon that seeks its prey under the cover of darkness. It tracks the target takes away their sight and attacks them. Unlike the common sparrow it is nocturnal although there are many individuals who stay up late in the morning so don't let your guard down."):
        "Un passero stregato che punta la preda approfittando del buio. La insegue, le toglie la vista e le salta addosso. A differenza del passero comune è notturno, ma attenzione: non pochi, invece di fare le ore piccole la notte, le fanno la mattina.",

    # ---------------------------------------------------------- :5633 <Melget> l'informatrice
    (5633, 'An informant who covers a wide range of topics from state secrets to personal proclivities. She has been almost killed many times but she has become extremely strong as she has gone through the rounds. The weaknesses of those involved have been fully seized and she is now untouched.'):
        "Un'informatrice che copre di tutto, dai segreti di stato ai gusti privati della gente. L'hanno data per morta un'infinità di volte, ma a furia di uscire dai guai è diventata forte oltre ogni misura. Adesso che ha in mano i punti deboli di tutti gli interessati, non la tocca più nessuno.",

    # ---------------------------------------------------------- :5646 <Lazasye> il demone della distruzione
    # ⚠️ L'inglese inventa un «God of Creation» e rovescia il paragone.
    (5646, 'A demon like a mass of destructive impulses. It seems that the God of Creation destroys for the sake of rebirth while the God of Destruction only feels pleasure in destroying tangible things. He especially likes to ruthlessly shatter beautiful things.'):
        "Un demone che pare fatto tutto di impulso distruttivo. Il dio della distruzione distrugge per far rinascere, mentre a questo, a quanto pare, rompere le cose che hanno una forma dà soltanto piacere. Ridurre in pezzi le cose belle, e senza pietà, è quello che gli riesce meglio.",

    # ---------------------------------------------------------- :5659 il gufo spaziale
    (5659, 'It is called by this name because it has some of the characteristics of a bird plus some of the ears. There is a description of a machine that speaks very similarly to them in the past and it is rumored that a reconnaissance machine was sent in from long ago.'):
        "Si chiama così perché ha qualche tratto da uccello e per giunta due cose che sembrano orecchie. In certi scritti antichi si parla di una macchina che parlava in un modo somigliantissimo al suo, e c'è chi mormora che di lassù mandino macchine in ricognizione da tempi remoti.",

    # ---------------------------------------------------------- :5672 il toro d'acciaio
    # ⚠️ 比較にならない e' *incomparabilmente piu' forte*: l'inglese lo rovescia.
    (5672, 'A black ox-man boasting tremendous muscles that are built like steel. He is a power fighter in comparison to the Minotaur but he is not always on his feet and he is sometimes unable to fight due to injuries to his shins and knees.'):
        "Un uomo-toro nero che va fiero di una muscolatura spaventosa, temprata come l'acciaio. Come lottatore di potenza il primo minotauro che capita non gli sta nemmeno vicino, però ha la guardia bassa da terra in giù, e capita che si azzoppi a uno stinco o a un ginocchio e resti fuori combattimento.",

    # ---------------------------------------------------------- :5685 la medusa kraken
    (5685, 'A great great elder who has lived through repeated rebirth and division since long before even the first civilization was born. As it spent its eternity it accumulated magical power and evolved allowing it to operate in the air. In fact it is full of collagen and good for your beauty.'):
        "Un venerabile anziano che campa da molto prima che nascesse perfino la prima civiltà, rigenerandosi e dividendosi senza sosta. Nell'eternità che ha attraversato ha accumulato potere magico e si è evoluto, tanto da riuscire a muoversi anche in aria. E, per inciso, è pieno di collagene e fa bene alla pelle.",

    # ---------------------------------------------------------- :5698 lo squalo capitano
    (5698, "A descendant of the legendary brave shark that ventured across the seas of space. He's a law-breaking pirate who can operate in space in the air and at sea. While searching for his ancestral birthplace which is said to be the land of gold he found himself in Irva."):
        "Discende dal leggendario squalo valoroso che solcava i mari dello spazio. È un pirata che se ne infischia di ogni regola, e sa muoversi nello spazio, in cielo e in mare. Cercando la terra natale dei suoi antenati, che dicono sia la terra dell'oro, è finito a Irva.",

    # ---------------------------------------------------------- :5711 lo squalo furioso
    (5711, 'A being whose spirit has materialized in the form of a shark. It has the spirit of never-give-up and is tenacious but its combat power is not that high. Apparently the tip of its nose is harder than titanium and its sharp teeth can chew through even large rocks.'):
        "Uno spirito che ha preso corpo nella forma di uno squalo. Non molla mai ed è tenace, ma quanto a forza in combattimento non è che vada tanto in là. Comunque pare che abbia la punta del muso più dura del titanio, e che con quei denti aguzzi sbricioli anche i massi.",

    # ---------------------------------------------------------- :5724 lo squalo incubo
    (5724, 'A shark whose basic tactics are to cooperate with his companions. He has seen his comrades who attack directly on the front lines get hurt so badly that he often has nightmares himself because of his own remorse.'):
        "Uno squalo che come tattica di fondo si coordina con i compagni. Ha visto fin troppe volte farsi male quelli che stanno in prima linea e attaccano di persona, e il rimorso glielo fa rivedere di notte: gli incubi non gli danno tregua.",

    # ---------------------------------------------------------- :5737 il wangnin
    # ⚠️ 妄人はワンニンと読む: l'inglese butta la glossa di lettura.
    (5737, 'A person who has been invaded by evil spirits and has become half a refrigerator. It is in a state where if it does not continue to fantasize it will lose its ego and become a complete fridge. It absorbs some of the attribute attacks and can be immediately ejected.'):
        "Wangnin si scrive con i caratteri del delirio. È un uomo che, invaso dal soffio maligno, è diventato per metà un frigorifero: se smette di vaneggiare perde l'io e si trasforma in frigorifero del tutto. Assorbe una parte degli attacchi elementali e li può risputare all'istante.",

    # ---------------------------------------------------------- :5750 la cavia
    (5750, "As a result of human modification and medication to get the best out of Meshera's characteristics she was unable to adapt and mutated. Perhaps because it's based on fresh flesh it's much stronger than the original Meshera in the Rehmido Ruins."):
        "L'hanno rimaneggiata nel corpo e riempita di farmaci per tirar fuori il meglio dalle proprietà del Meshera, ma non ha retto e le è venuto un difetto. Forse perché è partita da carne fresca, è molto più forte del Meshera originale che sta nelle Rovine di Remido.",

    # ---------------------------------------------------------- :5763 il gigante dormiente
    # ⚠️⚠️ 効かない: l'inglese ne fa un gigante malato, cioe' il rovescio.
    (5763, 'A giant with almost all health problems and no attributes. It is said that his true power is comparable to that of a god but he is always sleeping and it is difficult to see him fight. According to the few witness accounts of the battle he was sleepy and struck with his bare hands without using a weapon.'):
        "Un gigante su cui non fa presa quasi nessuna alterazione e nessun elemento. Dicono che la sua vera forza sia pari a quella di un dio, ma dorme sempre ed è difficile vederlo combattere. Le poche testimonianze che ci sono raccontano che menava a mani nude, mezzo addormentato, senza nemmeno prendere un'arma.",

    # ---------------------------------------------------------- :5776 la farfalla dell'uragano
    (5776, 'It may look like just a large butterfly but it has the power to interfere with the future. The fluttering of the wings is extremely minute but it can be a decisive factor in causing a huge storm.'):
        "A vederla sembra soltanto una farfalla di taglia grossa, e invece nasconde il potere di interferire pesantemente col futuro. Quel suo battito d'ali è una cosa piccolissima, eppure pare che di rimando in rimando possa diventare la causa decisiva di una tempesta.",

    # ---------------------------------------------------------- :5789 la farfalla di luce lunare
    (5789, 'The descendants of biological weapons produced by past civilizations. What appears to be scales has the ability to alter its property becoming a poison to consume the body when used for offense and a medicine when used for defense. Apparently their ancestors were more powerful and destroyed one civilization.'):
        "Discende dalle armi biologiche costruite da una civiltà del passato. Quella che sembra la polvere delle ali ha la proprietà di rifare la materia: usata per attaccare è un veleno che rode il corpo, usata per difendere è una medicina. Pare che gli antenati fossero ben più potenti, e che una civiltà l'abbiano distrutta davvero.",

    # ---------------------------------------------------------- :5802 la farfalla sicaria
    # ⭐ Muhammad Ali: vola come una farfalla, pungi come un'ape.
    (5802, "Although it looks like just a large butterfly it is actually a trained assassin. It flutters like a harmless butterfly and stings like a bee. Don't be fooled by appearances."):
        "A vederla sembra soltanto una farfalla di taglia grossa, e invece è un'assassina addestrata. Vola come una farfalla innocua e punge come un'ape. Non bisogna farsi ingannare dall'aspetto.",

    # ---------------------------------------------------------- :5815 il lupo mannaro detective
    (5815, 'A werewolf disguised as a detective blends in with the city. They sway people with false testimony to keep their fellow wolves from being executed. They seem to be under a lot of stress because they try not to bark while they are disguised.'):
        "Un lupo mannaro che si traveste da detective e si confonde fra la gente in città. Con testimonianze false porta tutti da una parte e dall'altra, per evitare che i lupi suoi compagni finiscano giustiziati. Mentre sta travestito deve trattenersi dall'ululare, e a quanto pare gli si accumula un bel po' di nervoso.",

    # ---------------------------------------------------------- :5828 il detective
    # ⚠️ 厄病神 e' il modo di dire, non la creatura: portasfortuna.
    (5828, 'Instinctively he smells an incident. Because he always appears when an incident occurs he is often regarded by people as a god of disaster even though he has done nothing wrong. Some of them become mentally ill from this and try to make friends with wolves due to their madness.'):
        "L'odore di un caso lo fiuta d'istinto. Siccome quando succede qualcosa lui è immancabilmente lì, la gente lo tratta spesso da portasfortuna, e dire che non ha colpa di niente. C'è chi per questo si ammala nella testa e, uscito di senno, prova a farsi amico un lupo.",

    # ---------------------------------------------------------- :5841 il leone incandescente
    (5841, 'A being whose spirit has materialized in the form of a lion. A red lion running with the power of the flame. Perhaps by sharpening the five senses the power to sleep will open up and it will become huge or something. Sharp claws are their weapon.'):
        "Uno spirito che ha preso corpo nella forma di un leone. Un leone rosso che corre avvolto nella forza del fuoco. Dicono che affinando i cinque sensi gli si schiuda il potere che tiene addormentato dentro e diventi enorme, ma chi lo sa. La sua arma sono gli artigli aguzzi.",

    # ---------------------------------------------------------- :5854 il lupo d'argento sfolgorante
    (5854, "A being whose spirit has materialized in the form of a wolf. An agile wolf who fights with a saber and a ray gun. They are strong for sure but there is something off about them. It appears to be a shiny gray rather than a silvery color but maybe it's just my imagination."):
        "Uno spirito che ha preso corpo nella forma di un lupo. Un lupo svelto che combatte con una sciabola e una pistola a raggi. Che sia forte è fuori discussione, ma ha qualcosa che non gira per il verso giusto. Più che argento sembra un grigio che luccica, ma sarà un'impressione.",

    # ---------------------------------------------------------- :5867 la strega piangente
    # ⚠️ 外法 sono le arti proibite: l'inglese legge «foreign laws».
    (5867, 'A poor woman who has been turned into a zombie-like entity by foreign laws. In addition it is significantly enhanced by the curse of some one. Their emotions remain and they are often seen sitting and grieving. It will attack with its claws if approached.'):
        "Una povera donna a cui le arti proibite hanno ridotto il corpo a quello di uno zombi. E per giunta la maledizione di qualcuno l'ha resa molto più forte. I sentimenti le sono rimasti, e spesso la si vede seduta a terra che si dispera. Attenzione però: se le ci si avvicina, colpisce con le unghie.",

    # ---------------------------------------------------------- :5880 il necrodanzatore
    (5880, 'The dead dance like mad forever by a curse. Apparently they are really good at bon-dancing but to the living it looks like nothing more than an orgy. Still it seems to have been generally well received by the dead.'):
        "Un morto che una maledizione costringe a ballare all'infinito, come impazzito. Pare che sia bravissimo nel ballo dell'Obon, la festa dei morti, ma ai vivi sembra soltanto una baldoria sguaiata. Fra i morti, in compenso, riscuote un discreto successo.",

    # ---------------------------------------------------------- :5893 il necrolanciere
    (5893, 'A spearman who has become a spirit of death. It was once just a guard but when it lost its life it was cursed and reborn. It has no intelligence and only stabs at you with force perhaps a blunt instrument would be better suited.'):
        "Un lanciere diventato spettro. Prima era soltanto una guardia, ma quando ha perso la vita gli hanno gettato addosso una maledizione ed è rinato così. Di intelligenza non ne ha, e si limita a infilzare andando di forza bruta: c'è chi dice che gli starebbe meglio in mano un'arma contundente.",

    # ---------------------------------------------------------- :5906 <Signora Cicogna>
    (5906, 'A mysterious being with the same appearance and name as an ancient bird that has only just been preserved in lore. Their primary habitat and where they come from and where they go are unknown. Incidentally it has long been taboo to pursue the storks that visit you.'):
        "Un essere misterioso che ha l'aspetto e il nome di un uccello antico rimasto soltanto nei racconti. Non si sa dove viva, né da dove venga, né dove vada. Per inciso: seguire una cicogna che è venuta a trovarti è da sempre considerato tabù.",

    # ---------------------------------------------------------- :5919 il soldato corazzato di Zanan
    (5919, "Zanan's field-raised soldier. He is a war veteran but he has not graduated from officer's school and has a low rank and fame in the military. They are often sent out on dangerous missions without being informed."):
        "Un soldato di Zanan venuto su dalla gavetta, sul campo. È un veterano di tante battaglie, ma l'accademia militare non l'ha fatta, e nell'esercito conta poco e non se lo fila nessuno. Spesso lo mandano in missioni pericolose senza dirgli niente.",

    # ---------------------------------------------------------- :5932 <Ryutye> lo smemorato
    (5932, 'A boy with a head injury. He collapsed with Neres in a state where he had forgotten everything but his own name. He is polite and soft-spoken and it is said that he may have grown up in a very good family but the truth is unknown.'):
        "Un ragazzo con una ferita alla testa. L'hanno trovato svenuto insieme a Neres, e di sé non ricordava altro che il proprio nome. È educato e ha modi gentili, e c'è chi dice che sia cresciuto in una famiglia più che agiata, ma come stiano davvero le cose non si sa.",

    # ---------------------------------------------------------- :5945 <Neres> la smemorata
    (5945, "Although she has the appearance of a child her physical abilities are extremely high and she is used to fighting. She has amnesia she just can't remember the important parts but there are many fragments left. Apparently she isn't at all familiar with the landscape of Irva."):
        "Ha l'aspetto di una bambina, ma il fisico le risponde in modo fuori dal comune ed è abituata a combattere. Ha perso la memoria: solo che le sfugge proprio quello che conta, mentre i frammenti le sono rimasti a bizzeffe. E pare che i paesaggi di Irva non le dicano assolutamente niente.",

    # ---------------------------------------------------------- :5958 <Regulus> l'uomo modificato
    (5958, "He used to be a lumberjack but when he was forced into a debt he didn't recognize he went bankrupt and was abducted by a suspicious man to a research facility in Zanan's army. After enduring a bio-weapon modification surgery and the administration of heavy drugs he successfully escaped after gaining control of Meshera."):
        "Prima faceva il taglialegna, poi gli hanno addossato un debito che non aveva mai contratto: è fallito, e un uomo losco l'ha rapito e portato in un centro di ricerca dell'esercito di Zanan. Ha retto sia all'operazione che doveva farne un'arma biologica sia ai farmaci violenti, e quando ha ottenuto il controllo del Meshera è riuscito a fuggire.",

    # ---------------------------------------------------------- :5971 <Fron> l'organizzatrice di viaggi
    (5971, 'A tour planner who works for the convenience of tourism. When necessary she travels at supersonic speed to the wilderness and even negotiates with gods. She prides herself on being quick on her feet and quick to set up things but she is even quicker to get her hands on things. She has a sister named Leah.'):
        "Un'organizzatrice di viaggi che lavora perché il turista non abbia pensieri. Se serve raggiunge a velocità supersonica anche le terre inesplorate, e con gli dei tratta senza batter ciglio. Va fiera di avere il piede svelto e la scaletta pronta in un attimo, ma la mano ce l'ha ancora più svelta. Ha una sorella che si chiama Leah.",

    # ---------------------------------------------------------- :5984 <Kuroya> lo scrutatore del cosmo
    (5984, "When he was a child he became friends with an alien swordsman he met while running away from home and honed his sword skills. He carries a long sword with a design similar to his friend's beloved sword so that he won't forget it even after decades."):
        "Da bambino, scappato di casa, fece amicizia con uno spadaccino venuto da un altro pianeta, e da lui imparò a maneggiare la lama. Porta con sé uno spadone disegnato sul modello della spada a cui l'amico teneva tanto, perché nemmeno dopo decine d'anni gli venga da dimenticarla.",

    # ---------------------------------------------------------- :5997 il golem di legno minore
    (5997, "A miniature size golem. It's still about the same size as a human though. Many of them have a calm personality and sometimes a small bird is perched on their head before they notice."):
        "Un golem in formato ridotto. Che poi resta comunque grande all'incirca come un uomo. Quasi tutti hanno un carattere placido, e capita che si ritrovino un uccellino posato in testa senza essersene accorti.",

    # ---------------------------------------------------------- :6010 il golem di pietra minore
    (6010, "A miniature size golem. It's still about the same size as a human though. It's a blunt and stubborn individual but there are many craftsmen who devote themselves to their work."):
        "Un golem in formato ridotto. Che poi resta comunque grande all'incirca come un uomo. Ha modi bruschi e la testa dura come la pietra, ma sono in tanti ad avere l'animo dell'artigiano, e al lavoro ci si buttano anima e corpo.",

    # ---------------------------------------------------------- :6023 l'anello di fiamme vorace
    (6023, 'A fire god with power equal to that of Cthugha. It lurks in the shadows of the dimensional door and appears among the cthughas when they are summoned. They are very dangerous with only burning and consuming in their minds.'):
        "Un dio del fuoco che sta alla pari col Cthugha. Se ne sta acquattato nell'ombra della porta fra le dimensioni, e quando qualcuno evoca il Cthugha compare insieme a lui, confondendosi. In testa non ha altro che bruciare e mangiare, ed è pericolosissimo.",

    # ---------------------------------------------------------- :6036 il Cthugha
    (6036, 'A fire god from a different world. They are not antagonistic to humans and can communicate with them in some cases. But when it comes to battle the forest the city and the nyarlathotep will burn to the ground.'):
        "Un dio del fuoco arrivato da un altro pianeta. Con gli uomini non ce l'ha in modo particolare, e a volte ci si può perfino parlare. Ma se si arriva alle mani brucia tutto fino all'ultimo: la foresta, la città e anche il Nyarlathotep. Quindi resta pericoloso.",

    # ---------------------------------------------------------- :6049 il Basatan
    (6049, "A god who was worshipped as the ruler of the sea was defeated in a power struggle with the other sea gods. A piece of the power fell on the crab's nesting grounds and transformed into a crab-controlling demon. Because of this it is often mistakenly assumed that he has only been able to control crabs since he was a deity."):
        "Era un dio venerato come signore del mare, ma nella lotta per il potere con gli altri dei marini fu sconfitto. Una scheggia di quel potere piovve su un covo di granchi e rinacque come mostro che comanda i granchi. Per via di questa storia si crede spesso, a torto, che anche da dio non sapesse comandare altro che granchi.",

    # ---------------------------------------------------------- :6062 la scatola nera
    (6062, 'A jet-black cube. It is said to be an autonomous machine but its internal structure is completely unknown. In addition to emitting heat and destructive rays it also has the ability to create a disturbing fog around it.'):
        "Un cubo nero come la pece. Si dice che sia una macchina che si governa da sola, ma di come sia fatta dentro non si sa proprio niente. Oltre a sparare raggi ardenti e raggi distruttori, sa spandersi attorno una nebbia che confonde.",

    # ---------------------------------------------------------- :6075 il cubo G
    (6075, 'A mysterious machine discovered in the underground ruins. Because of its tremendous durability there is even a theory that it was originally a blunt instrument and the electronic components were built in later for some reason.'):
        "Una macchina misteriosa ritrovata in certe rovine sotterranee. Regge i colpi in un modo tale che c'è perfino chi sostiene, per via accademica, che in origine fosse un'arma contundente e che i pezzi elettronici gliel'abbiano montati dopo, chissà per quale ragione.",

    # ---------------------------------------------------------- :6088 <Urcaguary>
    (6088, 'She is mid-level god of metals and gems and the sister of the earth god. Using the power of the God of the Earth at her disposal she created a golden knight modeled after herself to lead the Order. It is said that the god of the earth laughs at her boldness.'):
        "È la divinità di medio rango che ha in mano i metalli e le gemme, ed è la sorella maggiore del dio della terra. Usando il potere del fratello senza chiedergli permesso si è fabbricata dei cavalieri dorati a propria immagine, e adesso guida i Cavalieri Dorati. Dicono che davanti a tanta sfrontatezza perfino il dio della terra rida amaro.",

}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-012.jsonl'
DA, A = 5601, 6100
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
