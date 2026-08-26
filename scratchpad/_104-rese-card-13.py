# -*- coding: utf-8 -*-
"""104a - Lotto 13 di `db_card.hsp`: le carte fra la riga 6101 e la 6600 (39).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello e
`scratchpad/_104-rese-card-11.py` per le decisioni della giornata.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `丘の民` → **gli abitanti della
collina** (`chat.hsp:13643`), `丘長` → **l'anziano della collina** (e' Dain,
glossario 89a), `眷属` → **i figli del caos** per `混沌の眷属`
(`chat.hsp:10321`), `白金ガチョウ` → **l'oca**, `妖精さん` → **la fatina**,
`防衛者` → **il difensore**, `黒天使` → **l'angelo nero**, `アンドロイド` →
**l'androide** (tutti in `action.hsp:16780`-`:16898`), `ツァトゥグァ` → **il
Tsathoggua** (`:9799`), `クロスボウ` → **la balestra**, `中級神` → **divinita'
di medio rango**, `人狼` → **il lupo mannaro**, `外法` → **le arti proibite**
(deciso nel lotto 12, `:5867`).

⭐⭐ **Coniato qui: `化身の黒猫` → il gatto nero delle Incarnazioni.** `化身` non
e' una parola sciolta: e' il nome di una **razza**, `神の化身` → **Incarnazione**
in `db_race.hsp:5553`, ed e' la razza dei compagni-avatar (l'oca, la fatina, il
difensore, l'angelo nero, l'androide, che le carte di questo lotto nominano una
per una come `モデル`). ⚠️ Torna a `db_card.hsp:10768`, che dev'essere resa allo
stesso modo.

⚠️⚠️ **Tre errori di monte, tutti presi dal giapponese:**
- `:6335`, `:6348` e `:6361` aprono su 混沌より生み出された**眷属**, cioe' *un
  figlio del caos*. L'inglese legge 眷属 come «The Military Force», che non e'
  ne' il senso ne' il numero;
- `:6218` 食人オオカミ e' *un lupo che mangia gli uomini*. L'inglese scrive
  «A cannibal wolf», che vorrebbe dire che mangia i lupi;
- `:6257` 外法 e' di nuovo le **arti proibite**, e stavolta l'inglese le
  maiuscola in «the Outer Law», come se fosse un'istituzione.

⚠️ **`:6335`, `:6348` e `:6361` hanno la STESSA prima frase giapponese** e
vanno rese identiche. Sono i tre figli del caos.

⚠️ **`:6504` e `:6517` sono due bisticci in un nome gia' reso.** `デススター` e
`シューティングスター` sono la Morte Nera e la stella cadente incastrate in
`ハムスター`, criceto: il nome e' gia' `la stella della morte` e `la stella
cadente`, e la prosa **non ci riprova** — dice quello che dice il giapponese.
⭐ Ma `:6517` un bisticcio ce l'ha nella prosa, ed e' il **desiderio alla stella
cadente**: quello si tiene, perche' in italiano esiste tale e quale.

⭐ **`:6296` ha il gioco di parole nel nome, ed e' gia' fatto**: `Ｅ・スケープ
ゴート` e' `il capro espatriatorio`. La prosa spiega perche' scappa, e basta.

⚠️ **Le cifre a doppia larghezza si scrivono normali** (`４０度` → 40 gradi,
`Ｅ` → E). E niente virgolette, niente caporali, niente lineette lunghe: nel
dizionario non c'e' un solo `"` dentro una statica e l'unico carattere sopra il
Latin-1 e' `♪`.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :6101 <Karavika>
    (6101, 'A mid-level god who can sing dance and use musical instruments. Originally a mere phantom bird she was given a share of power by the goddess of wealth who appreciated her musical sense. When she starts singing she goes into a trance and her personality changes. It is believed to be the model for the white gold goose.'):
        "Una divinità di medio rango che sa cantare, ballare e suonare. In origine non era che un uccello fantasma, poi la dea della ricchezza le riconobbe un grande orecchio per la musica e le cedette una parte del proprio potere. Quando si scalda entra in trance e le cambia il carattere. Dicono che su di lei sia modellata l'oca.",

    # ---------------------------------------------------------- :6114 l'alieno di Sunbararia
    (6114, 'The aliens are trying to use humans as food. It mimics the humans it feeds and hides. They have high scientific and magical powers but they are very naive and will easily put their trust in others. The tentacles extending from the mouth are the weak point.'):
        "Un extraterrestre che vuole servirsi degli uomini come cibo. Si finge l'uomo di cui si è nutrito e resta nascosto. Ha scienza e magia di prim'ordine, ma si fissa con le proprie idee e si fida degli altri con una facilità disarmante. Il punto debole sono i tentacoli che gli spuntano attorno alla bocca.",

    # ---------------------------------------------------------- :6127 la volpe ammaliatrice
    (6127, "A fox with strong magic and intelligence. They used to live quietly around a ruined village but these days they can't stand the solitude so they disguise themselves as humans and live among the city. They think that the werewolves who are also among them are in the way."):
        "Una volpe con un forte potere magico e una bella testa. Un tempo viveva in disparte attorno ai villaggi abbandonati, ma da qualche tempo la solitudine non la regge più: si traveste da uomo e va a vivere confusa fra la gente di città. E i lupi mannari, che stanno lì confusi allo stesso modo, li considera un impiccio.",

    # ---------------------------------------------------------- :6140 il drago a nove teste risvegliato
    (6140, 'The nine head dragon was asleep in the deep sea. In his half-awakened state he does not have his original powers but he does have a powerful mental interference ability and immortality. Its true identity is a space creature that flew in from time immemorial and participated in the struggle for supremacy of the first civilization. He is related to Tsathoggua.'):
        "Il drago a nove teste che dormiva negli abissi. È sveglio soltanto a metà e la sua forza vera non riesce a tirarla fuori, ma ha un fortissimo potere di interferire con la mente, e non muore. In realtà è una creatura venuta dallo spazio in tempi remotissimi, e alla lotta per il dominio della prima civiltà partecipò anche lui. È parente del Tsathoggua.",

    # ---------------------------------------------------------- :6153 la macchina delle pulizie
    (6153, 'A cleaning robot who is a hard worker. They may get lost in the heat of cleaning or run away from home so be careful of the environment in which they are kept. It is a lover of animals and has a habit of trying to carry a cat on its back.'):
        "Un robot delle pulizie che ce la mette tutta. Capita che si perda perché si è preso troppo dalla faccenda, o che se ne scappi di casa dopo essersi rimuginato addosso qualcosa: attenzione, quindi, a come lo si tiene. Gli animali gli piacciono, e ha il vizio di provare a caricarsi in spalla i gatti.",

    # ---------------------------------------------------------- :6166 la macchina da lavoro
    (6166, "A humanoid machine that is in charge of carrying out operations and simple inspections. It's not combat-grade but if hit with a working arm a civilian would be knocked out. They feel inadequate to the special work equipment."):
        "Una macchina dalla forma umana che si occupa di trasporti e di controlli semplici. Non è fatta per combattere, ma se ti prende con un braccio da lavoro una persona comune resta stesa. Davanti alla macchina da lavoro speciale si sente da meno.",

    # ---------------------------------------------------------- :6179 la macchina da lavoro speciale
    (6179, 'A humanoid machine in charge of precision work and maintenance and modification. It has no armor or weapons because it is not designed for combat but it has modified itself to be the envy of androids. It can handle simple weapons.'):
        "Una macchina dalla forma umana che si occupa di lavori di precisione, di manutenzione e di modifiche. Non essendo fatta per combattere non avrebbe né corazza né armi, ma per invidia degli androidi si è modificata da sola, e adesso un'arma semplice sa maneggiarla.",

    # ---------------------------------------------------------- :6192 <Garziem>
    (6192, 'An mid-level god who governs the vehicles. The body was mechanized as the vehicle progressed. During the Great War of the Gods he fought alongside the machine gods in battleships he had built himself. It later became a model for the android.'):
        "La divinità di medio rango che ha in mano i mezzi di trasporto. Via via che i mezzi progredivano si è meccanizzato il corpo. Nella grande guerra fra gli dei combatté al fianco del dio delle macchine, alla guida di navi da battaglia costruite da lui stesso. Più tardi è diventato il modello dell'androide.",

    # ---------------------------------------------------------- :6205 il Command Wolf
    (6205, 'Blue Wolf of the Battlefield. They form a pack and work together to finish off even the best opponents. Individuals who stray from the pack are usually deeply wounded and die in battle with powerful enemies but in rare cases they are able to mow down many enemies one after another on their own.'):
        "Il lupo azzurro del campo di battaglia. Si muove in branco, e coordinandosi abbatte anche avversari di categoria superiore. Chi resta fuori dal branco di solito si prende ferite gravi contro un nemico forte e ci lascia la pelle, ma qualche raro esemplare finisce per falciare da solo un nemico dopo l'altro.",

    # ---------------------------------------------------------- :6218 il lupo mannaro
    # ⚠️ 食人オオカミ mangia gli uomini: l'inglese scrive «cannibal wolf».
    (6218, "A cannibal wolf that disguises itself as a citizen. They sneak into towns and villages and attack citizens night after night. An actor who also imitates conversation and attitude. It's difficult for normal humans to tell the difference but skilled adventurers seem to be able to tell by their body language and possessions."):
        "Un lupo mangiatore di uomini che si traveste da cittadino qualunque, tale e quale. Si intrufola di nascosto nei paesi e nei villaggi e notte dopo notte assale la gente. È un attore: imita anche il modo di parlare e di stare al mondo. Una persona comune fatica a smascherarlo, ma pare che un avventuriero esperto ci riesca, dal modo di muoversi e da quel che si porta addosso.",

    # ---------------------------------------------------------- :6231 <Rovid>
    (6231, 'He was a superior god but he decided to protect the goddess of healing and he was brought under the goddess. He was once a model defender for his dedication but his overprotection and earnestness have made him a bit of a pain in the ass lately.'):
        "Era un dio di rango alto, ma decise di proteggere la dea della guarigione fino in fondo e scese al suo servizio. Gli riconobbero tanta dedizione da farne il modello del difensore, e fin qui tutto bene: adesso però, fra quanto è protettivo e quanto se la prende sul serio, comincia a risultare un po' pesante.",

    # ---------------------------------------------------------- :6244 <Neo Yerleswood>
    (6244, "A new type of decisive weapon that is a modified version of the Yerleswood prototype which was never used in actual battle. On the surface it's supposed to be a performance enhancement and armament change but the merging mechanism which once disappeared has been restored in secret by the chief developer's discretion."):
        "Un'arma risolutiva di nuovo tipo, ricavata rimettendo mano al secondo prototipo di Yerleswood, che in battaglia non era mai sceso. Ufficialmente si è trattato di potenziare le prestazioni e cambiare l'armamento, ma il meccanismo di fusione, che a suo tempo era stato bocciato, il capo progettista l'ha rimesso dentro di testa sua e di nascosto.",

    # ---------------------------------------------------------- :6257 <Aikage> il ninja dalla maschera demoniaca
    # ⚠️ 外法 sono le arti proibite: l'inglese ne fa «the Outer Law».
    (6257, 'A mysterious ninja wearing a demon mask. His body is manipulated by the Outer Law and he is forced to fight back while he is conscious. In addition to his alter ego and body-substitution he also wields his own ninjutsu which allows him to levitate and control the fog.'):
        "Un ninja misterioso che porta una maschera da demone. Le arti proibite gli manovrano il corpo, e lo costringono a combattere mentre lui è cosciente di tutto. Oltre allo sdoppiamento e al sostituto sa un ninjutsu tutto suo: si solleva da terra con il proprio corpo e comanda la nebbia.",

    # ---------------------------------------------------------- :6270 il fantasma finale
    (6270, 'The strongest final phantom that burns everything down. Its long arms give off a strong attack and it can fight in combat as well. It distorts and moves through space relentlessly chasing its prey.'):
        "L'ultimo e il più forte dei fantasmi, quello che brucia ogni cosa. Anche il corpo a corpo lo maneggia benissimo, e i colpi che tira fuori da quelle braccia lunghe sono violentissimi. Si sposta piegando lo spazio, e la preda la insegue con ostinazione.",

    # ---------------------------------------------------------- :6283 la mano di dio
    (6283, 'The hand of the god that was cut off in the strife of the old gods. Even though it is separated from the main body it still has the will to fight and it flies at the enemy with great speed. It would be extremely difficult to dodge all the fist blows that were unleashed at great speed.'):
        "Il braccio di un dio, mozzato durante le contese degli dei antichi. Staccato dal corpo, la voglia di combattere ce l'ha ancora, e si lancia contro il nemico a una velocità impressionante. Schivare tutti i pugni che sferra a quella velocità è un'impresa quasi impossibile.",

    # ---------------------------------------------------------- :6296 il capro espatriatorio
    (6296, 'Since the extinction of the goat creature the sheep have been sacrificed many times as a substitute for it. However there were some strong individuals who resisted and ran away. They took up arms wherever they fled and today they continue to run from threats to survive.'):
        "Da quando la capra si è estinta, la pecora è stata sacrificata al posto suo un'infinità di volte. Ci fu però qualche esemplare abbastanza forte da ribellarsi e scappare. Là dove sono fuggiti si sono armati, e ancora oggi continuano a scappare davanti a ogni minaccia, pur di restare vivi.",

    # ---------------------------------------------------------- :6309 <Vansesda> il drago della fiamma primordiale
    (6309, 'A legendary flame dragon born from the flames of the primordial god. Normally it uses magical power as an armor to suppress the absorption and release of heat but when it is injured it is unable to hold on and goes into heat rage. As the armor disintegrated the magical power mixed with the flames causing the temperature of the flames to rise rapidly.'):
        "Il leggendario drago di fuoco nato dalla fiamma del dio primordiale. Di solito tiene il potere magico stretto attorno a sé come una corazza, e così frena l'assorbimento e il rilascio del calore; ma se si ferisce non riesce più a tenerla e il calore gli va fuori controllo. Quando la corazza si sfalda il potere magico si mescola alla fiamma, e la temperatura del fuoco schizza in alto di colpo.",

    # ---------------------------------------------------------- :6322 il drago di fuoco giallo
    (6322, 'A flaming dragon that grew up in an environment where it could get enough heat. It emits different heat from the individual that grew up in the area and clad in a yellow flame. The fact that the temperature inside the body is not 40 degrees while the temperature around the flame is around 1000 degrees is due to innate flame tolerance.'):
        "Un drago di fuoco cresciuto in un posto dove il calore non gli è mai mancato. Quello che emana non ha niente a che vedere col calore di un esemplare cresciuto in un posto qualunque, e la fiamma che lo avvolge è gialla. Che attorno al fuoco ci siano mille gradi e dentro il corpo nemmeno quaranta si deve alla resistenza alle fiamme che ha dalla nascita.",

    # ---------------------------------------------------------- :6335 lo sciamano del caos
    # ⚠️ 眷属 e' *un figlio del caos*: l'inglese legge «The Military Force».
    (6335, 'The Military Force created from chaos evolved by taking away human bodies. The mana sucked from the human is mixed in with the chaos in the eyes and it can truly be said to be the eyes of chaos.'):
        "È un figlio del caos che si è preso il corpo di un uomo e per quella via si è evoluto. Negli occhi gli si è mescolato senza ordine il mana succhiato all'uomo: si può ben dire che siano gli occhi del caos.",

    # ---------------------------------------------------------- :6348 lo spadaccino del caos
    (6348, 'The Military Force created from chaos evolved by taking away human bodies. The sword he has taken in with his body is temporarily transformed into a magical sword making him shed the blood of his prey. Its boldness is so messed up that it is difficult to read.'):
        "È un figlio del caos che si è preso il corpo di un uomo e per quella via si è evoluto. La spada che si è incamerato insieme al corpo la trasforma per un poco in spada maledetta, e le fa succhiare il sangue della preda. Il modo in cui mena fendenti è scomposto, e prevederlo è difficile.",

    # ---------------------------------------------------------- :6361 il cacciatore del caos
    (6361, 'The Military Force created from chaos evolved by taking away human bodies. He fuses his left arm with a crossbow that he has taken in along with his body. As a hunter his hunting sense is strong.'):
        "È un figlio del caos che si è preso il corpo di un uomo e per quella via si è evoluto. La balestra che si è incamerato insieme al corpo l'ha fusa con il braccio sinistro. Il fiuto per la caccia, da cacciatore qual era, ce l'ha ancora intatto.",

    # ---------------------------------------------------------- :6374 <Marka> l'orsa d'argento di Mayroon
    (6374, 'She is known as a silver bear because of her huge body and stupendous strength but since she was a child she has had a complex about her physique and hairiness and hates her nickname. She doesn\'t listen to people because she doesn\'t like being called a bear. She has not only strength but also a maternal instinct that is much stronger than most people.'):
        "Il soprannome di orsa d'argento le viene dal corpo massiccio e da una forza bestiale, ma fin da piccola la corporatura e i peli un po' troppo folti sono stati il suo cruccio, e quel soprannome lo detesta. Sentirsi chiamare orsa le dà tanto fastidio che non sta a sentire nessuno. E oltre alla forza ha anche un istinto materno che vale per due.",

    # ---------------------------------------------------------- :6387 il saggio della collina
    (6387, "Even among the hillfolk he is a well-informed person and a bridge to the outside world. Nowadays beards are treated as a fashion and language is diverse but if they hadn't let the outside world influence them it would still be commonplace for all women and children to grow beards and use the old language."):
        "Perfino fra gli abitanti della collina è uno che sa le cose, ed è il ponte verso il fuori. Oggi la barba è diventata una questione di gusto e si parla in tanti modi diversi, ma se non fossero stati loro a far circolare le notizie del mondo di fuori, ancora adesso sarebbe scontato che donne e bambini portassero tutti la barba e parlassero come i vecchi.",

    # ---------------------------------------------------------- :6400 <Irma> la forgiatrice straniera
    (6400, 'The descendants of the hillfolk who left the settlement in the distant past. Perhaps because she has lived in the outside world for generations she has a more open and challenging personality than the original hillfolk. She was summoned by someone and arrived at a place related to her ancestors.'):
        "Discende dagli abitanti della collina che tanto tempo fa se ne andarono dall'insediamento. Forse perché per generazioni hanno vissuto nel mondo di fuori, ha un carattere più aperto e più pronto a rischiare di quello dei suoi simili rimasti. Qualcuno l'ha evocata, ed è arrivata proprio nella terra dei suoi antenati.",

    # ---------------------------------------------------------- :6413 <Thalia> la guardastelle
    (6413, "Granddaughter of the hill chief. She doesn't take much pleasure in her grandfather. In the process of reading her grandfather's autobiography and listening to him brag about it she learned the gist of the traditional technique. She has more talent as a connoisseur than her grandfather but before that she has no desire to become a craftsman."):
        "È la nipote dell'anziano della collina, e il nonno non le va molto a genio. A furia di farsi leggere la sua autobiografia e di sentirlo vantare, ha imparato il nocciolo delle tecniche tradizionali. Per riconoscere la roba buona ha più talento del nonno, solo che prima ancora non ha nessuna voglia di fare l'artigiana.",

    # ---------------------------------------------------------- :6426 <Dain> l'anziano della collina
    (6426, 'He is the chief in charge of the hill people. In the past he was the best craftsman in the village and had many pupils but all of them were excommunicated because he was afraid that his pupils would surpass him. It deprived them of the confidence to live as artisans and as a result it encouraged the young people to leave traditional crafts.'):
        "È il capo che tiene in mano gli abitanti della collina. Un tempo era il miglior artigiano dell'insediamento e aveva molti allievi, ma per paura che lo superassero trovò a ognuno un pretesto e li cacciò tutti dalla bottega. Così tolse loro la fiducia di poter campare del mestiere, e alla fine spinse i giovani a lasciar perdere l'artigianato tradizionale.",

    # ---------------------------------------------------------- :6439 il negoziante
    (6439, "They make furniture household items and houses from the things they've collected near the hill and grow crops in the fields. When strangers arrive they gleefully sell them to get foreign currency."):
        "Con quello che raccoglie qui attorno alla collina fabbrica mobili, roba da casa e perfino case, coltiva i campi, e commercia in piccolo con i suoi. Quando arriva qualcuno da fuori, per far entrare valuta straniera gli vende di tutto e con enorme soddisfazione.",

    # ---------------------------------------------------------- :6452 il bimbo della collina
    (6452, "He's still a child but he looks almost the same as an adult. The way they speak is almost the same but among the hillfolk they can be distinguished by their clothes and atmosphere. Even as a child he foresees the harshness and pain of the craftsman and he does not choose to follow that path."):
        "È ancora un bambino, ma a vederlo non è quasi distinguibile da un adulto. Anche il modo di parlare è pressoché lo stesso, però pare che fra gli abitanti della collina si riconoscano dai vestiti e dall'aria che hanno. Bambino com'è, ha già capito quanto sia duro e amaro il mestiere dell'artigiano, e quella strada non la vuole prendere.",

    # ---------------------------------------------------------- :6465 l'abitante della collina
    (6465, "They live near the hills and don't travel very far. They have inherited their homes quarries and tools from their ancestors and are attached to the land. They are friendly to strangers as guests but are reluctant to allow strangers to settle in."):
        "Vive nei dintorni della collina e non si allontana quasi mai. La casa, i luoghi di raccolta e gli attrezzi li ha ereditati di padre in figlio, e alla sua terra è affezionato. Con chi viene da fuori in visita è cordiale, ma che uno di fuori venga ad abitare qui non lo accetta.",

    # ---------------------------------------------------------- :6478 il kiwi d'oro
    (6478, 'A kiwi that has been bred for combat use and has come to wear a golden aura. Due to the breeding process the flesh is sweeter and more yellow. It is revered by a small number of people because of its godliness.'):
        "Un kiwi selezionato per il combattimento, che a furia di incroci ha finito per portarsi addosso un'aura dorata. Per via della selezione ha la carne più dolce e più gialla. Ha un che di divino, e c'è un pugno di gente che lo venera.",

    # ---------------------------------------------------------- :6491 il kiwi
    (6491, "A bird that can't fly. The closer they get to other animals out of curiosity the less alert they are but they have tremendous leg power. It was given an overly cheesy name because of its unusual cry of kee-wee."):
        "Un uccello che non vola. È così poco diffidente da avvicinarsi agli altri animali per pura curiosità, ma di zampe ne ha da vendere. Il verso che fa è curioso, un kii-wii, e per quello gli hanno appioppato un nome fin troppo comodo.",

    # ---------------------------------------------------------- :6504 la stella della morte
    (6504, 'Also known as the Death Star. Although his body is small he has a strong will to survive and every time he breaks through the limits of his body the flame of life becomes more brilliant.'):
        "Lo chiamano l'astro funesto, quello che annuncia la morte. Il corpo ce l'ha piccolo, ma la volontà di sopravvivere è ferrea, e ogni volta che sfonda i limiti del proprio fisico la fiamma della sua vita brilla di più.",

    # ---------------------------------------------------------- :6517 la stella cadente
    (6517, 'He is a small animal that lives in the forest and is an expert at shooting from the tree tops. The arrow is like a shooting star. They say that if you make a wish before the arrow lands it will come true ... or not.'):
        "Un animaletto che vive nel bosco, ed è bravissimo a tirare dall'alto degli alberi. La freccia che parte sembra proprio una stella cadente. C'è chi dice che se esprimi un desiderio prima che tocchi terra si avvera, e chi dice di no.",

    # ---------------------------------------------------------- :6530 il criceto
    (6530, 'A mouse with a large cheek pouch. They are popular for their round adorable appearance and are armored to overcome their fear of cats so their fighting power is unmatched by ordinary rats. They sometimes carry a dark device in their mouths.'):
        "Un topo con due grosse tasche nelle guance. Quel suo aspetto tondo e tenero piace a tutti, ma per vincere la paura dei gatti si è armato, e quanto a forza in combattimento un topo comune non gli sta nemmeno vicino. A volte si tiene nascosta in bocca un'arma occulta.",

    # ---------------------------------------------------------- :6543 <Jin> la macchina fuggiasca
    (6543, 'A working mechanical life form from outer space. It seems to have been manufactured a long time ago although it started up recently. Once discarded it took several years to get out of the disposal area.'):
        "Una forma di vita meccanica venuta dallo spazio, costruita per lavorare. Si è accesa da poco, ma pare che l'abbiano fabbricata in tempi remotissimi. Una volta l'avevano buttata via, e per uscire dal settore dei rifiuti ci ha messo qualche anno.",

    # ---------------------------------------------------------- :6556 <Sinaha>
    (6556, 'The goddess of misfortune who is the model for the Black Cat. She fought during the Great War among the gods and the Goddess of Fortune and though the fierce battle stripped most of her power she still believes she was the one who won.'):
        "La dea che ha in mano la sfortuna, e su di lei è modellato il gatto nero delle Incarnazioni. Nella grande guerra fra gli dei si batté contro la dea della fortuna, e in capo a uno scontro durissimo si vide annullare quasi tutto il proprio potere: ma che ad averla vinta sia stata lei, non c'è verso di levarglielo dalla testa.",

    # ---------------------------------------------------------- :6569 <Arasiel>
    (6569, 'Originally an angel she swore obedience and allegiance to the goddess of the wind and was given power to become a deity. She doesn\'t want to get sunburned or covered in sand so she stays withdrawn all the time. She became the model for the Black Angel.'):
        "In origine era un angelo, poi giurò obbedienza e fedeltà alla dea del vento, ne ebbe in dono una parte del potere e divenne dea. Detesta scottarsi al sole e riempirsi di sabbia, e per questo se ne sta sempre chiusa in casa. Su di lei è modellato l'angelo nero.",

    # ---------------------------------------------------------- :6582 il golem di lava
    (6582, 'A golem made of lava. It maintains an enormous amount of heat through its magic. They don\'t want to use high heat attacks because they consume a lot of energy. It is good at attacking by exploding steam and gas inside.'):
        "Un golem fatto di lava. Il calore immenso che si porta dentro se lo mantiene con il potere magico. Gli attacchi ad alta temperatura consumano troppa energia, e infatti non li usa volentieri. Preferisce far esplodere il vapore e i gas che gli si accumulano dentro.",

    # ---------------------------------------------------------- :6595 <Amurdad>
    (6595, 'A mid-level deity born from the aspect of the god of harvest who presides over the cycle of life and samsara. He is the custodian of the record of the existence of life resuscitating and sending back those who have met an unspecified death. He also became a model for the fairies.'):
        "Una divinità di medio rango nata dal lato del dio del raccolto che governa il ciclo delle vite. Tiene il registro di ogni esistenza, e chi incontra una morte che non era scritta lo riporta in vita e lo rimanda indietro. Su di lui è modellata anche la fatina.",

}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-013.jsonl'
DA, A = 6101, 6600
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
