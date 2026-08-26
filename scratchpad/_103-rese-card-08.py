# -*- coding: utf-8 -*-
"""103a - Lotto 8 di `db_card.hsp`: le carte fra la riga 3601 e la 4100 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_103-rese-card-07.py` per le decisioni della giornata.

⭐ **Gia' deciso altrove:** `異形の森` → **Vindale** (`db_card.hsp:10579`,
«il messaggero di Vindale»), `ロスリア` → **Lothria**, `ニーサ` → **Niesa**
(`chat.hsp:2132`), `キッカス` → **Kikkas** (`db_card.hsp:5431`), `メイルーン`
→ **Mayroon**, `冥界蟹` → **il granchio dell'oltretomba** (`:6913`),
`白銀龍蟲` → **il millepiedi drago argenteo** (`:7992`), `魔王` → **il re dei
demoni** (`:8239`), `インプ` → **il folletto**, `マンドレイク` → **la
mandragora**, `やどかり` → **il paguro**, `ハムスター` → **il criceto**,
`クイックリング` → **il quickling**, `エーテルの風` → **il vento d'etere**.

⚠️⚠️ **`ヴァリウス` e' Barius anche qui** (`:3696`): l'inglese scrive
*Vallius* due volte nella stessa riga. Vedi il lotto 7.

⚠️ **`:3878` perde un gioco di parole e non c'e' modo di tenerlo.** La stella
marina si vanta di essere la ビッグスター del mare e sale a terra perche' ha
saputo che lassu' e' popolare un ハムスター — che finisce in **スター**. In
italiano «criceto» non contiene «stella», e la battuta non si ricostruisce: si
tiene il criceto, che e' la cosa che il giocatore puo' verificare (e' una
creatura del gioco), e si lascia cadere il bisticcio. L'inglese di monte aveva
risolto togliendo il criceto del tutto, e cosi' la carta non dice piu' niente.

⚠️ **`:3891` gioca su 高飛び**, che vuol dire insieme *volare alto* e *darsela
a gambe*: il pesce volante e' un latitante. In italiano si tiene la fuga, che
e' il senso, e il volo lo porta gia' il nome della carta.

⚠️ **`:4008` e' censurato in giapponese** con 「爪や指や××や×××」. Il segno di
moltiplicazione non passa in CP932 senza diventare doppia larghezza: si scrive
`xx` e `xxx`, che e' la strada che aveva preso anche l'inglese.

⚠️ **`:4034` scivola in prima persona nell'inglese** («I'm also in charge of
cleaning up the intruders»): il giapponese parla di lei.

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
    # ---------------------------------------------------------- :3605 il tempestello
    (3605, "This special quickling is created by a storm of miasma that blew into a remote area of the underworld. They've felt a sense of destiny after hearing that there was a black sword called Stormbringer from rumors in the wind."):
        "Un quickling speciale, che nasce dentro le tempeste di miasma che si dice infurino nelle terre remote dell'oltretomba. Da quando il vento gli ha portato la voce che esiste una spada nera chiamata Stormbringer, si sente addosso qualcosa che somiglia a un destino.",

    # ---------------------------------------------------------- :3618 l'ammazzaerba
    (3618, 'A midget running through a meadow. It has extraordinary leg strength and a shockwave is generated with a single swing of the leg. As a quid pro quo it was born with a charge in its knee and if it runs or kicks with all its might it will be unable to withstand the recoil and explode.'):
        "Un ometto che corre per le praterie. Ha nelle gambe una forza fuori dal comune, e gli basta un colpo di piede per sollevare un'onda d'urto. Il prezzo lo paga alla nascita: ha una carica esplosiva nel ginocchio, e se corre o calcia a tutta forza non regge il contraccolpo e scoppia. Una creatura scomoda.",

    # ---------------------------------------------------------- :3631 il danzaerba
    (3631, 'A close relative of Quickling. A midget dancing in the meadow. He has a dexterous hand and a cheerful personality. Usually the steps are too fast to know what kind of dance they are doing but sometimes their charming movements and mysterious gazes will bewitch the audience in an instant.'):
        "Parente stretto del quickling. Un ometto che balla come un forsennato nelle praterie. Ha le mani abili e il carattere allegro. Di solito i passi vanno troppo veloci per capire che ballo sia, ma i gesti pieni di grazia che si lascia sfuggire ogni tanto, e quello sguardo ambiguo, confondono il pubblico in un istante.",

    # ---------------------------------------------------------- :3644 il soldato potenziato di Zanan
    (3644, 'A soldier who has been subjected to harsh treatment at a secret experimental facility in Zanan. He was able to flee and defect but he was suffering from a physical disorder. With the recent development of a palliative in Lothria he seems to have gained stability although his abilities are slightly less.'):
        "Un soldato sfruttato fino all'osso nel centro sperimentale segreto di Zanan. Fuggire e passare dall'altra parte gli è riuscito, ma il corpo gli è rimasto guasto e non gli dava pace. Pare che con il farmaco lenitivo messo a punto di recente a Lothria abbia guadagnato stabilità, in cambio di un po' di quello che sa fare.",

    # ---------------------------------------------------------- :3657 il veterano
    (3657, 'He was a skilled soldier but he was forced out of the army long ago when it was decided that he was no match given to his age. He realizes that he has become too stained with blood and can only live on the battlefield so he goes into exile in another country. He was able to re-enter the workforce because of his experience.'):
        "Era un soldato provetto, ma decisero che contro il peso degli anni non c'era niente da fare e da un pezzo lo misero in congedo a forza. Capito che ormai si era sporcato di troppo sangue e che vivere poteva solo sul campo di battaglia, se n'è andato in un altro paese. L'esperienza gliel'hanno comprata volentieri, e ha trovato un altro ingaggio.",

    # ---------------------------------------------------------- :3670 l'infermiera assassina
    (3670, 'The nurses tire of nursing and awaken to the pleasures of murder. They fire a machine gun and go on a series of murders. Their compassionate hearts revived for a moment after the killing and they treat the corpse gently.'):
        "Un'infermiera che, a furia di stancarsi nel curare, si è risvegliata al piacere di uccidere. Spara raffiche di mitragliatrice e ammazza a ripetizione. Dopo il colpo, per un istante, il cuore pietoso le torna: e allora tratta il cadavere con dolcezza.",

    # ---------------------------------------------------------- :3683 <Lankata> il fulmine del cielo azzurro
    (3683, 'Daughter of the former Commander of the Knights of Lothria. Although her father kept her from fighting she became a corpsman at her own insistence. While her father was away on a mission her high fighting talent blossomed and she rose to the rank of Acting Commander. The spiky hair that is inherited from her parents bothers her.'):
        "Figlia del precedente comandante dell'ordine cavalleresco di Lothria. Il padre la teneva lontana dai combattimenti, ma lei ha voluto a tutti i costi fare almeno l'infermiera di reparto. Mentre lui era via in missione le è sbocciato un talento notevole per la battaglia, e si è arrampicata fino a comandante facente funzione. I capelli ribelli, quelli sì, li ha presi in famiglia, e le danno pensiero.",

    # ---------------------------------------------------------- :3696 l'agente speciale di Lothria
    # ⚠️ ヴァリウス → Barius, due volte. L'inglese scrive «Vallius».
    (3696, 'The parent company is the Knights of Lothria which was disbanded when Vallius was deposed. He was secretly recalled with the return of Vallius and carried out various missions in the shadows. He wears a modified version of the magical armor that came in from Eulderna.'):
        "Nasce dall'ordine cavalleresco di Lothria, sciolto quando Barius cadde in disgrazia. Con il ritorno di Barius al potere il reparto fu richiamato di nascosto, e ha portato a termine ogni sorta di missione restando nell'ombra. Indossa una versione rimaneggiata dell'armatura magica arrivata da Eulderna.",

    # ---------------------------------------------------------- :3709 l'Elea oscuro
    (3709, 'A subspecies that has the same roots as a normal Elea but has adapted to life outside the strange forest. They have strong magical powers dark skin and are reluctant to form groups. In terms of personality they are more warlike and worldly than normal Elea.'):
        "Ha le stesse radici degli Elea comuni, ma è la sottospecie che si è adattata alla vita fuori dal bosco di Vindale. Ha un forte potere magico e la pelle scura, e non ama mettersi in gruppo. Di carattere, rispetto agli Elea comuni, è più bellicoso e più attaccato alle cose del mondo.",

    # ---------------------------------------------------------- :3722 <Manytia> la mercante avventuriera
    (3722, 'Hillfolk who traded near the border of Kikkas. A self-proclaimed adventurer she sells her wares on the battlefield and in other dangerous places. It seems that her style is to sell things at high prices where there is a high demand so she changes the products she deals with from place to place.'):
        "Viene dal popolo delle colline, e commerciava dalle parti del confine fra Kikkas e Niesa. Si proclama mercante avventuriera, e smercia la sua roba nei campi di battaglia e in altri posti pericolosi. Il suo stile pare essere vendere caro dove c'è richiesta, e infatti cambia merce a seconda del posto.",

    # ---------------------------------------------------------- :3735 il granchio spaziale oscuro
    (3735, 'A space crab that inhabited a black hole. It was captured by an alien species and bred for use in invasions. Mainly fighting with scissors and liquid solvents. In recent years some of them have been kept as space pets because of their adorable calls and movements.'):
        "Un granchio spaziale che viveva dentro un buco nero. Una specie aliena lo catturò e lo selezionò per usarlo nelle invasioni. Combatte soprattutto con le chele e con un liquido che scioglie. Il verso e i movimenti sono così graziosi che negli ultimi tempi c'è chi lo tiene come animale da compagnia spaziale.",

    # ---------------------------------------------------------- :3748 <Re Porcellino> il sovrano dei crostacei
    (3748, 'A giant sowbug that lived in a bizarre forest. He reigns as the king of the forest with an intelligence beyond that of humans and a generous heart. He also lives in symbiosis with Elea and when the forest was burned he led the people amidst the flames with his strength. In reality he is a relic of a biochemical civilization.'):
        "Un porcellino di terra gigantesco che viveva nel bosco di Vindale. Ha un'intelligenza superiore a quella degli uomini e un cuore magnanimo, e regna sul bosco come suo sovrano. Vive in simbiosi anche con gli Elea, e quando il bosco fu dato alle fiamme fece scudo col proprio corpo per guidare fuori la gente circondata dal fuoco. In verità è un lascito della civiltà biochimica.",

    # ---------------------------------------------------------- :3761 il chiamamorte
    (3761, 'A close relative of the underworld crab. It is widely found from the riverbed of the Sanzu River to the shore of the Underworld and is more popular than the Underworld crab on the other side. It has a habit of guiding the dead with one arm but it is dangerous to the living because their souls will be pulled away.'):
        "Parente stretto del granchio dell'oltretomba. È diffuso su un tratto largo, dalle golene del fiume Sanzu fino alle coste del mare dei morti, e di là è più comune del granchio dell'oltretomba. Ha l'abitudine di guidare i defunti con la chela che ha sviluppato, ma per un vivo è pericoloso: verrebbe tirato via con tutta l'anima.",

    # ---------------------------------------------------------- :3774 l'insetto coronato
    (3774, 'It has an outer shell that is shaped like an overlapping crown. Because of its appearance it was regarded as the judge of kingly qualities in ancient Cyronia and climbing on its back was a ritual of succession to the throne. Remnants of the ritual can still be seen in festivals today.'):
        "Ha il guscio fatto a corone sovrapposte. Per quell'aspetto, nell'antica Cyronia lo tenevano per il giudice che riconosceva la stoffa di un re, e salirgli in groppa era il rito con cui si saliva al trono. Ancora oggi, nelle feste, di quel rito si vede qualche residuo.",

    # ---------------------------------------------------------- :3787 l'aromalocaris
    (3787, 'Marine life thought to have gone extinct in extreme antiquity survived by adapting and evolving to live underground. It got its name from the fact that the female ingests the roots of the plant and produces essential oil in her body which she uses as a pheromone in her courtship behavior.'):
        "Una creatura marina che si credeva estinta in un'antichità remotissima, e che invece era sopravvissuta adattandosi alla vita sottoterra. Il nome le viene dal fatto che la femmina si nutre di radici di piante, se ne ricava dentro il corpo un olio essenziale e lo usa come feromone nel corteggiamento.",

    # ---------------------------------------------------------- :3800 il paguro cecchino
    (3800, 'They have a sniper rifle on their shells. Due to the strength of the shell it is strong enough to shoot at a standstill. Because of its slow legs it is easily preyed upon by creatures that can withstand the sniping.'):
        "Un paguro che si è montato un fucile di precisione dentro il guscio. Il guscio è robusto, e quindi nello scambio di colpi a piede fermo se la cava bene. Ma le zampe sono lente: chi regge il tiro di precisione se lo mangia senza fatica.",

    # ---------------------------------------------------------- :3813 l'umanoide trasparente
    (3813, "It has an upper body that resembles a human and is called a ningen or hitokata but it is a member of the snail family. They've lived on land since ancient times but have gone unnoticed because they're so transparent and when they're found in the ocean they've been misidentified as marine mammals."):
        "Ha il busto simile a quello di una persona, e infatti lo chiamano Ningen o Hitogata, ma è parente delle chiocciole. Fin dall'antichità viveva anche sulla terraferma, solo che nessuno se n'era accorto perché è trasparente; e quando qualcuno lo avvistava in mare, si diceva che avesse scambiato per altro un mammifero marino.",

    # ---------------------------------------------------------- :3826 l'aguglia dai nove dardi
    (3826, "A fish that rushes at high speed and pierces you with its sharp maw. It can penetrate a person's skull at will. It has sharp teeth and in some cases it has bitten off the nose of an Indian elephant. They're perfectionists and if they can't finish off their opponents they'll go on a rampage stabbing and spinning."):
        "Un pesce che carica ad alta velocità e infilza con le mascelle affilate. Un cranio umano lo passa da parte a parte senza sforzo. Ha i denti aguzzi, e si sono visti casi in cui ha staccato con un morso la proboscide a un elefante indiano. È perfezionista: se non riesce a finire l'avversario, resta infilzato e si mette a girare su se stesso come un ossesso.",

    # ---------------------------------------------------------- :3839 il demone marino Orcinus
    (3839, 'He is from the Land of the Dead the terminus of the Sanzu River. He has a strong curiosity and innocently plays games with strangers but is no joke. Few would be able to withstand the goofy rush of a huge body and the sweet bite that crushes armor.'):
        "Viene dal mare dei morti, il capolinea del fiume Sanzu. È di una curiosità insaziabile, e fa festa con innocenza anche a chi non conosce, solo che di festoso ha poco. Alla carica per gioco di quel corpaccione, e al morsetto affettuoso che sfonda un'armatura, resiste poca gente.",

    # ---------------------------------------------------------- :3852 la manta torpedine
    (3852, "They are mild-mannered and have no poisonous needles. Normally they live off of mana and winged insects in the air as they swim low in the etheric winds but they are not incapable of eating meat either. When it comes to combat it stops the enemy's movement by scattering threads and discharging them."):
        "Una razza di indole mite, e per giunta senza aculeo velenoso. Di solito vive nuotando bassa sul vento d'etere e mangiando il mana e i moscerini che trova nell'aria, ma la carne non è che non la mangi. Se si arriva alle mani, sparge fili per bloccare il nemico sul posto e poi scarica la corrente.",

    # ---------------------------------------------------------- :3865 il corallo fiorito
    (3865, 'A single flower resting on the sea floor. In fact it is a group of coral worms. It lives in symbiosis with algae and is also capable of photosynthesis. It forms a multi-colored exoskeleton but it is not easily seen because it sprays seawater around it to make it habitable.'):
        "Un fiore solitario che se ne sta in fondo al mare. In realtà è una colonia di polipi di corallo. Vive in simbiosi con le alghe e sa anche fare la fotosintesi. Costruisce uno scheletro esterno di tutti i colori, ma come ornamento non vale molto: per stare comodo sparge acqua di mare tutt'intorno.",

    # ---------------------------------------------------------- :3878 la stella marina abissale
    # ⚠️ Il bisticcio ハムスター / スター si perde: vedi la testa del file.
    (3878, 'A giant starfish that calls itself the Big Star of the Sea. Recently it heard that there was a popular creature so he came up to not be outdone. He thinks of shuriken as a taciturn kindred spirit.'):
        "Una stella marina enorme che si proclama la grande stella del mare. Di recente ha sentito dire che sulla terraferma c'è un beniamino di nome criceto, e per non essere da meno è salita anche lei all'asciutto. È convinta che gli shuriken siano parenti suoi, solo un po' taciturni.",

    # ---------------------------------------------------------- :3891 il pesce volante rapace
    # ⚠️ 高飛び: insieme «volare alto» e «darsela a gambe». Vedi la testa.
    (3891, "They are called the Criminals of the Sea. They''re mainly pickpockets and food runners but one day they commit a terrible crime and are now flying overland. They are thinking of returning to the sea when the heat has cooled down."):
        "Lo chiamano il delinquente del mare. Di mestiere fa il borseggiatore e mangia senza pagare, ma un giorno ha combinato un guaio troppo grosso, e adesso è alla macchia sulla terraferma. Conta di tornarsene in mare quando le acque si saranno calmate.",

    # ---------------------------------------------------------- :3904 il pesce cannone
    (3904, 'A sea gunslinger who wanders at the direction of the waves and at his own whim. He loves to soak up the sun and deliberately goes to lie down on the rocks on the land with a series of short teleports. And struggle on the way home.'):
        "Un pistolero del mare che vaga dove lo portano le onde e dove gli gira. Va matto per il bagno di sole, e per andare a sdraiarsi sugli scogli a riva si spara una raffica di teletrasporti corti. Poi, al ritorno, sono guai.",

    # ---------------------------------------------------------- :3917 <Kunoichi alla moda>
    (3917, "Her natural talent blossomed when she was no longer bound by existing ninjutsu. She goes by a code name that nobody understands and is in high spirits. ...In later years she's going to be burying her face in the cushion and lazing around."):
        "Il talento naturale le è sbocciato quando ha smesso di stare legata alle arti ninja come si erano sempre fatte. Adesso si presenta con un nome in codice che non si capisce bene e si diverte un mondo. ...C'è da scommettere che fra qualche anno finirà a ficcare la faccia in un cuscino e a sbattere braccia e gambe per la vergogna.",

    # ---------------------------------------------------------- :3930 <Saimef> il bianco ghiaccio
    (3930, 'A dog god who is friendly to humans. He got into a fight with his brother who hates humans and wandered out of the forest resulting in his arrival in Mayroon. While guiding travelers who were lost in a blizzard the god came to be worshipped in some areas but it seems that it is still a minor god.'):
        "Un dio cane, e in buoni rapporti con gli uomini. Litigò con il fratello minore, che gli uomini invece li detesta, e uscì dal bosco: girovagando finì a Mayroon. A furia di guidare i viaggiatori sperduti nella tormenta si è guadagnato il culto di qualche zona, ma resta un dio piuttosto minore.",

    # ---------------------------------------------------------- :3943 il sepa
    (3943, "A giant centipede that harbors a piece of God. Apparently the pieces belonged to the guardian gods of venom and the dead but they don't care about that and go on a rampage drowning in power. It dislikes the white silver dragon bugs that are being flattered by humans."):
        "Un millepiedi gigantesco che porta in sé una scheggia di divinità. La scheggia pare fosse del nume che protegge i veleni e i morti, ma di questo a lui non importa niente: si ubriaca della forza e mette tutto a soqquadro. Non sopporta il millepiedi drago argenteo, che gli uomini si tengono caro.",

    # ---------------------------------------------------------- :3956 il verme demoniaco dei vincoli
    (3956, "The worm is said to have been born from the demons of bondage. It's almost like a child. Their specialty is playing with impatience weakening their sluggish prey bit by bit and swallowing them head first when they are exhausted."):
        "Un verme che si dice nato dal demone dei vincoli. È poco più che un bambino. La specialità è farla lunga: prende la preda che non riesce a muoversi, la indebolisce un po' alla volta e, quando è allo stremo, se la inghiotte cominciando dalla testa.",

    # ---------------------------------------------------------- :3969 la sanguisuga collinare
    (3969, 'A huge leech that could be mistaken for a hill at a distance. Since most of its massive frame is sucked blood it becomes quite small when it dries up. They desperately suck blood to maintain their body shape.'):
        "Una sanguisuga gigantesca, che da lontano capita di scambiare per una collina. Quel corpaccione è quasi tutto sangue succhiato, e infatti quando si secca diventa piuttosto piccola. Per tenersi la linea succhia sangue con accanimento.",

    # ---------------------------------------------------------- :3982 il verme tentacolare
    (3982, "A worm that looks like a giant tentacle. Growing out of the sides are the elastic sub-tentacles not legs. They kill their prey with their sticky sub-tentacles slowly and deliberately sucking their lifeblood while pecking at their prey's body."):
        "Un verme che ha l'aspetto di un tentacolo enorme. Quelli che gli spuntano ai fianchi sono tentacoli secondari, che si allungano e si accorciano a piacere, e non zampe. Con quei tentacoli appiccicosi palpa il corpo della preda e intanto, con tutta calma, le succhia il sangue fino a ucciderla.",

    # ---------------------------------------------------------- :3995 la spettacameriera stregaccia
    (3995, 'She is a self-proclaimed night entertainer. A demon maid who transforms the partners she works with one after another stripping them of their bones and taking away their magical power. She is disliked by the other maids and is derisively referred to as a witch. Being small is her biggest annoyance.'):
        "Si presenta da sé come intrattenitrice della notte. È una cameriera demoniaca che cambia padrone uno dopo l'altro, lo riduce senza più volontà e gli porta via il potere magico. Le altre cameriere non la sopportano e la chiamano la strega, con tutto il veleno che ci sta dentro. Il suo cruccio più grande è essere bassa.",

    # ---------------------------------------------------------- :4008 la spettacameriera pinzacapo
    # ⚠️ La censura giapponese ××/××× diventa xx/xxx: vedi la testa del file.
    (4008, "She is the one who binds the demon maids. She puts on a savage show to entertain her master who is always bored. She is particularly good at torture and when she snatches people up she uses pliers to twist their nails fingers x's and x's without mercy."):
        "È lei che tiene insieme le cameriere demoniache. Per divertire il padrone, che si annoia sempre, mette in scena spettacoli di crudeltà. La tortura in particolare le riesce benissimo: rapisce qualcuno e poi, con le pinze, gli stritola senza pietà le unghie, le dita, il xx e il xxx.",

    # ---------------------------------------------------------- :4021 la spettacameriera cuocrudele
    (4021, 'A demon maid in charge of cooking. They put on a gruesome show to entertain their master who is always bored. They savagely butcher and cook their prey alive. In their spare time they are looking for a lively prey.'):
        "La cameriera demoniaca che si occupa della cucina. Per divertire il padrone, che si annoia sempre, mette in scena spettacoli di crudeltà. La preda la fa a pezzi e la cucina viva, e nel modo più atroce che sa. Quando non ha da fare, va in giro a cercare prede belle vispe.",

    # ---------------------------------------------------------- :4034 la spettacameriera spazzamorte
    (4034, "A demon maid who is in charge of cleaning. She puts on a gruesome show to entertain her master who is always bored. I'm also in charge of cleaning up the intruders."):
        "La cameriera demoniaca che si occupa delle pulizie. Per divertire il padrone, che si annoia sempre, mette in scena spettacoli di crudeltà. Pulizie sì, ma si occupa anche di quell'altra pulizia: quella degli intrusi.",

    # ---------------------------------------------------------- :4047 la spettacameriera vestisangue
    (4047, 'A demon maid who is in charge of the laundry. They put on a gruesome show to entertain their master who is always bored. It is more about washing blood with blood than it is washing clothes.'):
        "La cameriera demoniaca che si occupa del bucato. Per divertire il padrone, che si annoia sempre, mette in scena spettacoli di crudeltà. Più che lavare i panni, però, le capita di lavare il sangue col sangue.",

    # ---------------------------------------------------------- :4060 l'avanguardia del re dei demoni
    (4060, "An imp soldier in the service of the Demon King. They are loyal and obedient but they don't deserve to be treated well because they are an uninteresting bunch of stiffs. They are concerned about it but they are awkward and can't do anything about it."):
        "Un soldato folletto al servizio del re dei demoni. È fedele e obbediente, ma di trattamento ne riceve poco: sono tutti tipi rigidi e senza un briciolo di spirito. Anche a loro la cosa pesa, solo che sono impacciati e non ci sanno fare niente.",

    # ---------------------------------------------------------- :4073 la zuccampira
    (4073, "As a result of absorbing the weakened vampire's entire body as nourishment the pumpkin monster has awakened to the pleasure of drinking a creature's blood. The blood he has taken in causes him to grow abnormally and he targets more prey."):
        "Un mostro di zucca che, avendo assorbito come nutrimento un vampiro indebolito, corpo compreso, si è risvegliato al piacere di succhiare il sangue delle creature. Con il sangue che si prende si fa crescere in modo abnorme, e poi punta la preda successiva.",

    # ---------------------------------------------------------- :4086 la carota ninja
    (4086, 'A type of mandrake that resembles a carrot. He is armed with ninja skills which he learned at some point but he has no intention of becoming a ninja. He has a habit of going ahead and not thinking ahead.'):
        "Una specie di mandragora che somiglia a una carota. Le arti ninja le ha addosso, anche se non si sa dove le abbia imparate, ma di nascondersi non ha la minima intenzione. Ha il vizio di partire in quarta senza pensare a quel che viene dopo.",

    # ---------------------------------------------------------- :4099 il cetriolo guerriero
    (4099, 'A brave cucumber with the soul of a warrior. It is believed that the legendary creature Kappa perished due to the resistance of these cucumber species. In reality however they were destroyed by humans because of a shortage of food which caused them to wreak havoc in the countryside.'):
        "Un cetriolo valoroso, con dentro l'anima di un guerriero. Si racconta che il kappa, creatura leggendaria, si sia estinto per la resistenza di questi cetrioli. In verità furono gli uomini a sterminarlo: mancava il cibo, e il kappa aveva preso a devastare i villaggi.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-008.jsonl'
DA, A = 3601, 4100
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
