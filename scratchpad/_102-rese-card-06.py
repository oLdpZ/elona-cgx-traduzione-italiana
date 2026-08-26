# -*- coding: utf-8 -*-
"""102a - Lotto 6 di `db_card.hsp`: le carte fra la riga 2601 e la 3100 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello.

⭐ **Gia' deciso altrove:** `ゼーム` → **Zeome**, `レシマス` → **Lesimas**,
`常闇の眼` → **l'occhio delle tenebre eterne** (`chat.hsp:1236`), `サイモア` →
**Saimore**, `メイルーン` → **Mayroon**, `ローラン` → **Roran**
(`db_race.hsp:4589`), `エヘカトル` → **Ehekatl**, `ツァトゥグァ` → **il
Tsathoggua**, `オセロメー` → **l'ocelome**, `ルビナス` → **rubynus**,
`リビングアーマー` → **l'armatura vivente**, `弟狐` → **il fratello volpe**,
`異星主` → **Yith** (`db_race.hsp:5485`).

⭐ **Coniato qui:** `泡はきドラゴン` → **il drago sputabolle** (`:2903`). Non
sta ancora nel dizionario e in `db_card.hsp` torna piu' avanti: quando il suo
blocco si apre, il nome dev'essere questo.

⚠️ **`:2903` chiude su un rimando che l'inglese sfigura.** 「パズルに対して
複雑な感情を抱いている」: un drago che sputa bolle e ha «sentimenti complicati
verso i puzzle» e' Puzzle Bobble. Si tiene il rimando e non si spiega.

⚠️ **`:2877` e' la carta che ha deciso il genere di `病兄`** (vedi
`avanzamento.md`): i maschi di Roran sono malati sul serio, e per quello la
resa non segue quella di `病妹`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :2604 il brontosauro
    (2604, 'Long-necked dinosaurs. The head is a lightning rod that stores electricity when it is struck by lightning. They have a big figure and a big attitude and they look down on other animals completely. Even the giraffe can\'t be compared to these creatures.'):
        "Un dinosauro dal collo lungo. La testa gli fa da parafulmine: prende la folgore e ne accumula la carica. Ha una stazza grande e un'arroganza altrettanto grande, e guarda tutti gli altri animali dall'alto in basso. Pare che perfino la signora giraffa, davanti a lui, non alzi la testa.",

    # ---------------------------------------------------------- :2617 il triceratopo
    (2617, 'This dinosaur is characterized by three horns. Apparently it was restored with genetic technology from the old civilization. They are large and mature. They hate the unruly tyrannosaurus.'):
        "Un dinosauro che si riconosce dalle tre corna. Pare che sia stato ricostruito con la tecnica genetica della civiltà antica. Ha un corpo grande ma è tranquillo. Detesta il tirannosauro, che è un violento.",

    # ---------------------------------------------------------- :2630 <Beilgena> il drago artificiale
    (2630, 'It was created by genetic adjustments in the midst of the impending doom of a biochemical civilization. A being with enhanced ether-loving qualities and regenerative abilities and who was supposed to be the guardian of the etheric source. They liked the ether so much that they started killing other creatures to monopolize it and they liked it so much that they tried to eat the entire world so it was sealed as a failure.'):
        "Fu creata per aggiustamento genetico mentre sulla civiltà biochimica incombeva la fine. Le avevano rafforzato l'attrazione per l'etere e la capacità di rigenerarsi, e sarebbe dovuta diventare la guardiana della sorgente d'etere. Ma l'etere le piaceva talmente che si mise a uccidere le altre creature per averlo tutto, e talmente che provò a mangiarsi la foresta: così la sigillarono come esemplare mal riuscito.",

    # ---------------------------------------------------------- :2643 <Graveed> il signore della valle gravitazionale
    (2643, 'A synthetic dinosaur asleep in a culture tank at the site of a biochemical civilization. The vandals who awakened him out of curiosity were crushed by his magnificent tail and he escaped. It can create gravitational waves but its control is incomplete and it has trouble crushing things around it.'):
        "Un dinosauro sintetico che dormiva dentro una vasca di coltura, in un sito della civiltà biochimica. Quando i saccheggiatori di rovine lo svegliarono per curiosità, li polverizzò con la coda maestosa e scappò. Sa emettere onde gravitazionali, ma le controlla male, e si trova in imbarazzo perché schiaccia quello che ha attorno.",

    # ---------------------------------------------------------- :2656 <Dorothia> la reietta della palude
    (2656, "Long ago a clay golem was marooned in a marsh forest. It was discarded because the budding emotional golem was shunned at the time. She doesn't know that and she's been waiting for her master's return. As she armed herself with the dirt of the swamp forest to protect herself she became a kind of mud golem."):
        "Un golem d'argilla abbandonato tanto tempo fa in una palude boscosa. La lasciarono lì perché allora i golem in cui spuntava un sentimento facevano paura. Lei non lo sa, e da allora aspetta che il padrone torni. A furia di armarsi con il fango della palude per difendersi, è finita per somigliare in tutto a un golem di fango.",

    # ---------------------------------------------------------- :2669 <Sunrise> il drago dell'arcipelago
    (2669, 'Normally they live in the ocean as adults but sometimes they ascend from the sea to the sky at sunrise. It is said that in ancient times there were individuals so huge that when they lay in the sea their bodies would protrude from the surface.'):
        "Di solito vive tranquillo in mare, ma capita che al sorgere del sole salga dall'acqua verso il cielo. Nell'antichità, si dice, ne esistevano esemplari smisuratamente più grandi: quando si distendevano in mare il corpo sporgeva fuori dalla superficie.",

    # ---------------------------------------------------------- :2682 l'hamburger furioso
    (2682, "The burger monster. Lacking self-awareness as a dish We don't exist to be eaten by humans! and angrily turned into a monster. They are resented by their kindred spirits and french fries that are left to be eaten."):
        "Il mostro dell'hamburger. Gli manca la coscienza di essere un piatto, e a furia di gridare che loro non esistono per farsi mangiare dagli uomini si è trasformato in mostro per la rabbia. Se la prende anche con i suoi simili e con le patatine fritte, che si lasciano mangiare senza fiatare.",

    # ---------------------------------------------------------- :2695 <Melugast AO-I> la macchina da combattimento
    (2695, "All Options-Implemented i.e. All Options-Implemented Melugast. It's not because it' s blue but it was prepared for a fully equipped balnce test the moving parts were added to the body to increase armor. It is not suitable for riding because it is too lumpy."):
        "All Options-Implemented, cioè il Melugast con tutte le opzioni montate. Non è perché è blu. Fu allestito con la scusa di provare l'equilibrio a pieno carico, ma nella corazza aggiuntiva e nel corpo gli hanno messo parti mobili misteriose. È talmente carico di roba che a montarci sopra non ci si sta comodi.",

    # ---------------------------------------------------------- :2708 <Nagarew> la belva dell'oblio
    (2708, "A captured and altered incarnation of the Goddess of Oblivion that appeared in Eulderna. Dangerous magic has been applied to control special abilities and improve physical abilities. A skilled magician can use the memory wiping ability but the magician's memory will also be eroded by the reaction."):
        "L'incarnazione della dea dell'oblio comparsa a Eulderna, catturata e rimaneggiata. Applicandole una magia pericolosa le hanno dato il controllo dei poteri speciali e migliorato le capacità fisiche. Un mago capace può anche farle usare il potere di cancellare i ricordi, ma è rischioso: il contraccolpo corrode anche la memoria di chi la comanda.",

    # ---------------------------------------------------------- :2721 <Il Figlio del Caos>
    (2721, "A child created by Enthumesis with an imaginary pregnancy. A monster with the upper body of a lion and the lower body of a snake not unlike his mother. As a result of being neglected he created his own warped world and withdrew. He'd been pretending to be a ruler all along but before he knew it he'd returned to his mother's womb."):
        "Il figlio che Enthumesis ha messo al mondo con una gravidanza immaginaria. Non somiglia alla madre: è un mostro con la parte superiore di leone e quella inferiore di serpente. Abbandonato a sé stesso, si è creato un mondo storto tutto suo e ci si è chiuso dentro. Lì dentro faceva la parte del sovrano, finché senza accorgersene non è tornato nel ventre della madre.",

    # ---------------------------------------------------------- :2734 il gashadokuro
    (2734, "A giant skeleton born from the fusion of the grudges of the war victims and their remains. It crushes the living and chews the head off. It's small but apparently it has a stomach."):
        "Uno scheletro gigantesco, nato dalla fusione fra il rancore dei caduti in guerra e le loro ossa. Stritola i vivi e li mastica cominciando dalla testa. È piccolo, ma pare che uno stomaco ce l'abbia.",

    # ---------------------------------------------------------- :2747 la bestia d'ossa
    (2747, 'Originally there was a mass outbreak in a certain region. They say they were able to eradicate it at great cost. But a foreigner envious of the exploits of the squad resurrected them from their bones just for the sake of harassment.'):
        "In origine era una belva magica che in una certa regione si era diffusa a dismisura. Con enormi sacrifici, dicono, riuscirono a sterminarla. Ma un miserabile invidioso delle imprese della squadra di caccia la fece risorgere dalle ossa, solo per fare un dispetto.",

    # ---------------------------------------------------------- :2760 lo schiavo del denaro
    (2760, "The end of an adventurer who lived and died for money. He didn't trust anyone for fear of being robbed of his money so his last act was a lonely death. He is obsessed with the delusion that everyone has taken the money from his corpse and is desperate to get it back."):
        "Quel che resta di un avventuriero che ha vissuto ed è morto per il denaro. Per paura che glielo portassero via non si fidava di nessuno, e la fine gli è venuta in solitudine. Ora è ossessionato dall'idea fissa che tutti gli abbiano rubato il denaro dal cadavere, e si affanna a riprenderselo.",

    # ---------------------------------------------------------- :2773 l'antico ricognitore
    (2773, 'A sorcerer who was conducting an investigation of Nefia long ago. He fought a demon to free his companions and died but was revived as an undead. He is unaware that he has become ossified and continues to do research.'):
        "Un soldato-mago che tantissimo tempo fa indagava su Nefia. Combatté contro un mostro per far scappare i compagni e ci morì, ma è risorto come non morto. Non si è accorto di essere ridotto a ossa, e l'indagine la porta avanti ancora.",

    # ---------------------------------------------------------- :2786 l'armatura cremisi
    (2786, 'Performance has been greatly enhanced crimson living armor. He continues to wander in search of a strong man worthy of the Lord. It seems to be a dream to replace his entire body with Rubinus one day.'):
        "Un'armatura vivente rosso sangue, con le prestazioni potenziate di parecchio. Continua a vagare in cerca di un forte degno di esserle padrone. Pare che il suo sogno sia sostituirsi un giorno tutto il corpo con il rubynus.",

    # ---------------------------------------------------------- :2799 il guerriero evanescente
    (2799, 'The cursed armor has forcefully possessed a human being. It has a body that allows it to move powerfully. When the person inside fails in many ways it starts looking for the next wearer.'):
        "È un'armatura maledetta che si è impossessata a forza di un essere umano. Siccome ha un corpo, può muoversi con grande potenza. Quando la persona dentro comincia a cedere da tutte le parti, si mette a cercare chi la indosserà dopo.",

    # ---------------------------------------------------------- :2812 l'armatura dello sconfitto
    (2812, 'The spirit of a fallen warrior a warrior of a foreign land was reborned into his equipment. It is a demon with a bad nature roaming around and wielding a sword. The blue flame on his entire body is not hot at all.'):
        "È nata quando l'anima di un guerriero sconfitto, venuto da una terra straniera, è andata ad abitare nel suo equipaggiamento. È uno spiritello di pessima indole: gira di qua e di là menando fendenti. Le fiamme azzurre che ha su tutto il corpo non scottano affatto.",

    # ---------------------------------------------------------- :2825 <Gilphem> la sentinella d'acciaio magico
    (2825, "Using the knowledge gained from the Eye of Everlasting Darkness the watchman was created by Zeome just in case. A spell from the deepest layer of Lesimas with the armor built on another level. That's why he' s never met his parent Zeome. His job is to sense and eliminate those who have come to break the seal."):
        "La sentinella che Zeome ha creato per prudenza, servendosi del sapere ricavato dall'occhio delle tenebre eterne. È un'armatura di un altro piano, ricomposta con una stregoneria che viene dal fondo di Lesimas. Per come è andata, Zeome, che le fa da genitore, non l'ha mai incontrata. Il suo mestiere è accorgersi di chi viene a spezzare il sigillo, ed eliminarlo.",

    # ---------------------------------------------------------- :2838 <Alsapia> la maschera bianca
    (2838, "She entered this path after the assassination of her own abusive parents. She deliberately stands out with her strange appearance allowing her companions to attack while she attracts attention. She wears a mask because she doesn't want people to see the look on her face when she kills someone. In private it is removed."):
        "Ha imboccato questa strada dopo aver assassinato i genitori che la maltrattavano. Si fa notare apposta con un abbigliamento bizzarro, e mentre attira l'attenzione lascia attaccare i compagni. La maschera la porta perché non vuole che le si veda la faccia mentre uccide. In privato la toglie.",

    # ---------------------------------------------------------- :2851 il sicario di Zanan
    (2851, "A unit that has been secretly organized in Zanan since ancient times. Apparently it has grown in size since Saimore took over the reigns. When the dagger can't inflict a fatal wound on an opponent it breaks off and flashes a sharp light."):
        "Un reparto che a Zanan si organizzava in segreto fin dai tempi antichi. Pare che da quando Saimore ha preso il potere si sia molto ingrandito. Con chi non riesce a ferire a morte col pugnale, sbotta e lo trafigge con uno sguardo tagliente.",

    # ---------------------------------------------------------- :2864 <Enthumesis>
    (2864, 'Another Sophia. While wandering the lower world as a prostitute she was pregnant with human children many times but all of them ended in miscarriage. The white and black feathers are the embodiment of the souls of male and female fetuses. Her mind is broken and she tries to take in every life in search of information about her father.'):
        "L'altra Sophia. Vagando per il mondo di sotto come prostituta rimase incinta di figli umani più volte, ma tutte le gravidanze finirono in un aborto. Le ali bianche e nere sono le anime dei feti maschi e femmine, raccolte e fatte corpo. Ha la mente spezzata, e per cercare notizie del padre prova ad assorbire dentro di sé ogni forma di vita.",

    # ---------------------------------------------------------- :2877 il fratello maggiore malato
    (2877, "A brother with whom you are not related. Roran's males are so sickly that they usually die as children but he miraculously resists the disease with only his sense of duty to protect his brothers and sisters. Normally he would be in such serious condition that he would have bled out his entire body and exploded into four pieces right now."):
        "Il tuo fratello maggiore, che non ha il tuo sangue. I maschi di Roran sono tanto malaticci che di solito muoiono da bambini, ma lui resiste per miracolo al morbo tenendosi in piedi solo sul senso del dovere di proteggere i fratelli minori. A rigore dovrebbe essere così grave da schizzare sangue da tutto il corpo ed esplodere in quattro pezzi all'istante.",

    # ---------------------------------------------------------- :2890 il fratello volpe d'argento
    (2890, "The brother fox in Mayroon. They are adapted to cold climates with smaller ears and tails and a lower ratio of surface area to volume. However even though he is smaller his fox ears are in the way and he can't cover the hood of his winter clothing. He admires and imitates cool people but he is lonely at heart."):
        "Il fratello volpe come si presenta a Mayroon. Adattandosi al freddo ha orecchie e coda più piccole, e un rapporto più basso fra superficie e volume. Ma anche rimpicciolite, le orecchie da volpe danno fastidio e non gli lasciano mettere il cappuccio della giacca invernale. Ammira i tipi impassibili e li imita, ma in fondo soffre la solitudine.",

    # ---------------------------------------------------------- :2903 la bolla drago
    (2903, "His origins are complicated given that he was born with evil energy dwelling in the bubbles emitted by his foam-eating dragon form that was transformed by humans. While spitting bubbles he smashes his enemies with fighting techniques. I have mixed feelings about the puzzle."):
        "Ha una nascita complicata: è nato quando il male è andato ad abitare in una bolla emessa dal drago sputabolle, che a sua volta era un uomo trasformato. Sputa bolle a raffica e intanto stritola i nemici a mani nude. Verso i giochi di puzzle nutre sentimenti complicati.",

    # ---------------------------------------------------------- :2916 la progenie senza forma
    (2916, "He has the intelligence of a human being. A formless monster that was spawned in large numbers by an alien overlord somewhere. He was abandoned by his parents and was dying when he was picked up by Tsathoggua and out of gratitude he served them for many years. Now he' s looking for a way to complain to his parents."):
        "Ha un'intelligenza pari a quella di un uomo. È un mostro senza forma, messo al mondo in gran quantità da qualche Yith. Abbandonato dai genitori, stava per morire quando il Tsathoggua lo raccolse, e per riconoscenza restò a lungo al suo servizio. Adesso, per andare a lamentarsi con i genitori, li cerca insieme agli altri dividendosi il lavoro.",

    # ---------------------------------------------------------- :2929 il sangue vivente
    (2929, 'A magical creature created by an evil wizard by mixing his own blood. They capture their prey and suck the blood out of it. It prefers greasy and muddy blood to slippery blood.'):
        "Una creatura magica che un mago malvagio ha fatto mescolandoci il proprio sangue. Cattura la preda e le succhia il sangue fino all'ultima goccia. Al sangue fluido preferisce quello grasso e denso.",

    # ---------------------------------------------------------- :2942 il tentacolare
    (2942, 'It has a number of rope-like thin tentacles. The surface of the tentacles is slimy and they entangle their prey with them. It strangles its prey after the prey has exhausted its strength by resisting in vain.'):
        "Ha parecchi tentacoli sottili come corde. La loro superficie è viscida, e con quella avviluppa la preda. La palpa da cima a fondo, e la strangola dopo che si è sfinita a resistere inutilmente.",

    # ---------------------------------------------------------- :2955 lo Shin Gorilla
    (2955, 'A giant gorilla with a natural nuclear generator in its body. It was created and sealed in the biochemical civilization. They go to the limit of destruction to vent their overflowing energy.'):
        "Un gorilla gigantesco che ha in corpo un generatore nucleare naturale. Fu creato ai tempi della civiltà biochimica e poi sigillato. Distrugge tutto quello che può per sfogare l'energia che gli trabocca.",

    # ---------------------------------------------------------- :2968 il Ganesha
    (2968, 'An Indian elephant that has obtained a piece of God and become a deity. The existing Indian elephants are so fragile and weak that it takes weeks to recover from a minor injury and they are weaker than the Snail so they are sheltered by this one. Do I really need to protect such an assortment of creatures? Ganesha has been wondering about this lately.'):
        "Un elefante indiano che, ottenuta una scheggia di divinità, si è fatto dio. Gli elefanti indiani rimasti sono così fragili che per rimettersi da una ferita leggera ci mettono settimane, e sono più deboli di una lumaca: se campano ancora è solo perché lui li tiene al riparo. Ma vale la pena proteggere quella marmaglia? Pare che il Ganesha, di recente, abbia cominciato a chiederselo.",

    # ---------------------------------------------------------- :2981 il cavalceronte
    (2981, 'A heavy beast warrior who fights with hard skin and sharp horns. The charge with its huge body is intense. There was a scam for a while where the horn was cut off and sold as a unicorn horn but it was soon discovered that the size and shape were too different.'):
        "Un guerriero bestia dalla corazza pesante, che combatte con la pelle dura e le corna aguzze. La carica di quel corpo enorme è tremenda. Per un po' andò di moda una truffa che gli tagliava il corno e lo vendeva per corno di unicorno, ma la scoprirono subito: misura e forma erano troppo diverse.",

    # ---------------------------------------------------------- :2994 l'ippopotamo elettrico
    (2994, "The hippo is cyborgized as a vehicle. It works by breaking down cellulose and turning it into electricity. It has a good speed and stability but it can be difficult to control if it's an older model."):
        "Un ippopotamo reso cyborg per servire da cavalcatura. Funziona scomponendo la cellulosa e trasformandola in elettricità. Ha una discreta velocità e una buona stabilità, ma i modelli vecchi possono essere difficili da governare.",

    # ---------------------------------------------------------- :3007 il formichiere ammazzapadroni
    (3007, "When it senses danger it swings its sharp claws but it's very timid. The boss of the dark organization wants it as a lapdog and there is a request to capture it behind the scenes. There are many cases where the migrant workers who tried to work for the organization were found dead the next day."):
        "Quando fiuta il pericolo mena gli artigli aguzzi, ma è perché è paurosissimo. Il capo di un'organizzazione oscura lo vuole come animale da compagnia, e c'è una richiesta di cattura che gira sottobanco. Capita spesso che i braccianti che ci provano si ritrovino, il giorno dopo, tagliati in due.",

    # ---------------------------------------------------------- :3020 <Tezcatlipoca>
    (3020, 'The God of Night Smoke and War who uses the Jaguar. He used to go on a rampage just for the fun of fighting the strong but now he is aware of his sins in the Great War and works diligently behind the scenes. When his minion Jaguar is treated as a cat by Ehekatl he immediately gets in a bad mood.'):
        "Il dio della notte, del fumo e della guerra, che si serve del giaguaro. Un tempo si scatenava solo per il gusto di battersi con i forti; adesso è consapevole delle sue colpe nella grande guerra e lavora sul serio dietro le quinte. Se Ehekatl tratta da gatto il giaguaro che ha ai suoi ordini, gli si guasta subito l'umore.",

    # ---------------------------------------------------------- :3033 il coccodrillo pinnato
    (3033, 'This crocodile with fish-like fins throughout its body. Its identity is a descendant of the goddess that was once killed by Ehekatl and Tezcatlipoca. They are supposed to be taken care of them generation to generation as atonement for their sins but it seems that the number of them has increased too much recently.'):
        "Un coccodrillo che qua e là ha pinne da pesce. In verità è il discendente della dea che la prima Ehekatl e Tezcatlipoca uccisero. Per espiare, di generazione in generazione se ne devono prendere cura, ma di recente pare che gli esemplari siano cresciuti troppo e la cosa sia diventata dura.",

    # ---------------------------------------------------------- :3046 il soldato artiglio
    (3046, 'A soldier armed with fur and claws in the likeness of a jaguar. It was apparently created during the Great War by Tezcatlipoca using one of the gods under his control as a model. Due to his competitive nature and pride he often gets into fights with his rival over who is better.'):
        "Un soldato armato di pelliccia e artigli fatti a somiglianza del giaguaro. Pare che Tezcatlipoca l'abbia creato durante la grande guerra prendendo a modello una delle divinità ai suoi ordini. È attaccabrighe e pieno d'orgoglio, e con l'ocelome finisce spesso a litigare su chi dei due valga di più.",

    # ---------------------------------------------------------- :3059 l'imperatore delle locuste
    (3059, "A grasshopper prince transformed by a phase mutation. His body turns black and his abilities increase. What's more it can regenerate by absorbing light even if it is slightly damaged. They're a nightmare as they fly around in groups and eat everything."):
        "Il principe delle locuste, trasformato per mutamento di fase. Il corpo gli è diventato nero e tutte le capacità gli sono cresciute. E per giunta, anche se si ferisce un poco, si rigenera assorbendo la luce. Vederlo volare in gruppo e divorare ogni cosa è ormai un incubo.",

    # ---------------------------------------------------------- :3072 la libellula rossa d'assalto
    (3072, "An insect weapon with the Red Dragon's genes embedded in it. They have become frenzied and if there is anything that can be destroyed they will attack in packs with a desperate charge. Their bodies aren't that strong so shoot them down quickly."):
        "Un'arma insetto in cui hanno innestato i geni del drago rosso. È imbestialita, e se vede qualcosa che potrebbe distruggere si lancia in branco in una carica suicida: una gran seccatura. Il corpo non è poi così robusto, quindi conviene abbatterla subito.",

    # ---------------------------------------------------------- :3085 la locusta da sella
    (3085, "Formerly a big grasshopper who underwent alteration surgery at Zanan's secret laboratory. They escaped before being brainwashed as a weapon and bred en masse. The grasshoppers are fighting against the humans to protect their freedom."):
        "Era una locusta enorme, operata e modificata nel laboratorio segreto di Zanan. È fuggita prima che le lavassero il cervello per farne un'arma, e si è riprodotta a dismisura. Per difendere la libertà delle locuste, sfida il genere umano.",

    # ---------------------------------------------------------- :3098 la sfinge maligna
    (3098, 'A type of moth it is characterized by transparent wings and a body that looks like a shrimp fly. They are loved as cute and cuddly and reign as the demon king of the insect idol world. A hovering dance is their specialty.'):
        "È una specie di falena, ma si riconosce per le ali trasparenti, poco da falena, e per il corpo che pare un gambero fritto. La celebrano come carinissima e regna come sovrana dei demoni nel mondo degli idoli fra gli insetti. Il suo numero è la danza a mezz'aria.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-006.jsonl'
DA, A = 2601, 3100
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
