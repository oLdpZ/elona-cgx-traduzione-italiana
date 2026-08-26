# -*- coding: utf-8 -*-
"""106a - Lotto 20 di `db_card.hsp`: le carte fra la riga 9601 e la 10100 (38).

⚠️⚠️ **`:9637` PORTA L'INGLESE DI `:9624`, E SI TRADUCE SOLO DAL GIAPPONESE.**
`:9624` e' il `kabuto`, `:9637` e' `世界樹`, l'albero del mondo: l'inglese di
`:9637` racconta lo scarabeo. E' la testa segnalata da `_103-inglese-ripetuto` e
da `_104-inglese-slittato`, ed e' un **doppione isolato**: la catena non parte,
perche' `:9650` (l'Ouroboros) ha il suo inglese. Riverificato oggi leggendo il
dossier. ⓘ I due inglesi differiscono per una virgola (`beetle and` contro
`beetle, and`), quindi le due chiavi restano distinte e la rete 0 tace: se
fossero stati identici avrebbe parlato lei.

⚠️ **SEDICI carte su trentotto hanno l'inglese che finisce con uno SPAZIO**:
`:9611`, `:9624`, `:9637`, `:9663`, `:9689`, `:9702`, `:9741`, `:9767`, `:9780`,
`:9819`, `:9832`, `:9897`, `:9923`, `:9936`, `:9949`, `:10092`.

⚠️⚠️ **QUATTRO CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**

    :9728   一撃で頚動脈をかき切る      l'inglese aggiunge `of an Indian Elephant`
    :9845   獣類の長とされる幻獣で…     l'inglese ha PERSO la prima frase e comincia
                                        a meta': «infinitely close to being a god.»
    :10027  母親が適当な教育をしていた   l'inglese lo ROVESCIA: «her mother's proper
                                        upbringing». 適当 qui e' «alla come viene»,
                                        ed e' la ragione per cui il ragazzo e' ingenuo
    :9897   清掃員 non ha genere in jp   l'inglese la fa femmina (`her`); il nome
                                        italiano e' «<Ex spazzino>», e si tiene quello

ⓘ `Indian Elephant` e' lo stesso segnaposto sbagliato del lotto 19 (`:9338`,
`:9377`): **tre carte in due lotti**. Non e' una svista, e' un difetto di monte
che si ripete — quando compare, la misura vera sta nel giapponese.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `イルヴァ` → **Irva**,
`ネフィア` → **Nefia** (femminile, numerabile), `エント` → **Ent**
(`db_race.hsp:2449`), `幻獣` → **bestia fantastica** (`db_race.hsp:3964`),
`ビア` → **birra** (`db_item.hsp:149354`), `プチ` → **il putit**
(`action.hsp:16907`), `機械のマニ` → **Mani della Macchina**, `ルルウィ` →
**Lulwy** e `風神` → **la dea del vento** (`db_card:1720`: la forza gliel'ha
tolta Lulwy, ed e' lei la divinita' del vento di Irva), `眷属 (混沌の—)` → **i
figli del caos** (`chat.hsp:10321`), `ジューア` → **Juere** e `エウダーナ` →
**Eulderna** (⚠️ `ジューア` non e' `ジュア`: la nazione, non la dea),
`決戦兵器` → **l'arma della battaglia decisiva** (glossario della 105a),
`ブレス` → **il soffio**, `悪魔` → **il demone**.

ⓘ **Due giochi di parole del giapponese non passano, e la resa dice il senso.**
`:9611` gioca su モロク (Moloch) e モーロク (耄碌, «rimbambito»): in italiano
resta solo «rimbambito». `:9624` gioca su てんとう虫 (la coccinella, scritta
天道虫, «insetto della via del cielo») e 天の道を行く: l'inglese se l'e' cavata
inventando un `Tendou beetle`, l'italiano dice la coccinella e perde il ponte.
ⓘ てんとう虫 non compare in nessun'altra voce del dizionario: non c'e' un
precedente da rispettare.

🔶 **E il terzo non si puo' risolvere qui, e va guardato a schermo.** `:9858`
dice 同名の幻獣が存在する — «esiste una bestia fantastica con lo stesso nome» —
e in giapponese e' vero, perche' la giraffa e' キリンさん e il 麒麟 e' キリン. In
italiano sono **«la giraffa»** e **«il Kirin»**, e la frase resta vera solo per
chi conosce il giapponese. Le strade sono due: tradurre fedele (fatto qui, la
battuta non atterra) o rinominare la giraffa, che pero' collide col Kirin vero.
⚠️ Da mettere nella lista del collaudo: e' una carta che il giocatore legge.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :9611 il Moloch
    (9611, 'Cattlemen who have been driven from the throne of God. It is said that in the past they could be appeased by offering sacrifices, but now they are moloch and do not even realise that they have been offered sacrifices. '):
        "Un uomo toro cacciato dal trono divino. Pare che un tempo lo si potesse placare offrendogli un sacrificio, ma ormai è tanto rimbambito che non si accorge nemmeno di averne ricevuto uno. ",

    # ---------------------------------------------------------- :9624 il kabuto
    (9624, 'It has internalised the genes of an ancient insect called a Tendou beetle and is considered to be on the path of heaven as it flies towards the sun. It uses its acceleration ability against strong enemies. '):
        "Racchiude in sé i geni di un insetto antico, la coccinella, e poiché vola verso il sole si dice che percorra la via del cielo. Ai nemici forti risponde con la sua capacità di accelerare. ",

    # ---------------------------------------------------------- :9637 l'albero del mondo (⚠️ inglese di :9624)
    (9637, 'It has internalised the genes of an ancient insect called a Tendou beetle, and is considered to be on the path of heaven as it flies towards the sun. It uses its acceleration ability against strong enemies. '):
        "Un ent gigantesco che fa la guardia alle Nefia. I geni dell'albero del mondo sono gli stessi del grande albero che porta in sé una Nefia, e per questo si dice che, una volta cresciuto del tutto, vanti una mole che con l'uomo non ha proprio confronto. ",

    # ---------------------------------------------------------- :9650 l'Ouroboros
    (9650, 'Alchemical symbol for destruction and regeneration. It has a very high capacity for regeneration. When hungry, it has the habit of biting its own tail and starting to spin round and round, but what does this mean?'):
        "Il simbolo alchemico della distruzione e della rigenerazione. La sua capacità di rigenerarsi è altissima. Quando ha fame prende l'abitudine di mordersi la coda e di girare in tondo, ma un senso ce l'avrà?",

    # ---------------------------------------------------------- :9663 il viashivan
    (9663, "A subspecies that has continued to evolve in its own way and has acquired a power comparable to that of a dragon. However, hidden in its name is the meaning 'half lizard', indicating that it could not become a dragon no matter how strong it became. "):
        "Una sottospecie che ha continuato a evolversi per conto suo fino a ottenere una forza che davanti a un drago non sfigura. Ma nel suo nome si nasconde il significato di mezza lucertola, e dice che per quanto sia diventato forte drago non è mai riuscito a diventarlo. ",

    # ---------------------------------------------------------- :9676 la lussuriosa
    (9676, 'A type of demon that likes to mimic people. It approaches people in the form of a glamorous woman and plays with them. It is said to decide how to play, whether to kill by surprise or to parasitize with a miasma, depending on its mood.'):
        "Una specie di demone a cui piace prendere le sembianze degli uomini. Si avvicina alla gente nella figura di una donna procace e ci gioca. Se ucciderla di sorpresa o farle annidare dentro un corpo estraneo, pare che lo decida secondo l'umore.",

    # ---------------------------------------------------------- :9689 il battezzatore nero
    (9689, 'A person who is enthralled by and worships a black demon that is said to be sealed somewhere. From the gouged-out eye sockets, the screams of a trapped heart can be heard. '):
        "Uno a cui il demone nero, che si dice sigillato da qualche parte, ha rapito il cuore, e che adesso lo adora. Dalle orbite scavate e vuote si sente il grido del cuore prigioniero. ",

    # ---------------------------------------------------------- :9702 il cupido assassino
    (9702, 'Cupid has been poisoned by the love that consists of delusion, possessiveness and proprietary desire. The heavy, distorted arrows of love corrode and destroy the hearts of those who are shot through them. '):
        "Un cupido avvelenato da un amore fatto di ossessione, di possesso e di gelosia. Le sue frecce d'amore, pesanti e storte, corrodono e distruggono il cuore di chi trafiggono. ",

    # ---------------------------------------------------------- :9715 il fantasma voltaico
    (9715, 'A mysterious phantom that suddenly appears with lightning. The energy stored inside causes a runaway when the main body is damaged, resulting in a huge explosion. Equipped with a flame cannon.'):
        "Un fantasma misterioso che compare all'improvviso insieme al fulmine. L'energia che tiene dentro, se il corpo si danneggia, si scatena senza controllo e provoca una grande esplosione. È armato di un cannone a fiamma.",

    # ---------------------------------------------------------- :9728 il coniglio vorpal
    (9728, 'A rabbit with sharply developed front teeth. Its teeth are so sharp that a single blow can cut through the carotid artery of an Indian Elephant. It may look like just a cute rabbit, but if you try to take advantage of it, you will inevitably lose.'):
        "Un coniglio dagli incisivi lunghi e affilati. L'attacco di quei denti taglia da fare paura: recide la carotide in un colpo solo. A vederlo è soltanto un coniglietto grazioso, ma chi lo prende sottogamba le prende di sicuro.",

    # ---------------------------------------------------------- :9741 il tiranno demolitore
    (9741, 'In order to compete for survival with dragon races that share their food and habitat, they have acquired the ability to release their breath in opposition. Their speed and power have also increased, making them overwhelming to dragons. '):
        "Per vincere la lotta per la vita con le stirpi dei draghi, che gli contendono il cibo e il territorio, ha imparato a rispondere lanciando il soffio. Sono cresciute anche la velocità e la potenza, e ormai i draghi li travolge. ",

    # ---------------------------------------------------------- :9754 l'Atlach-Nacha
    (9754, 'An incarnation of the spider god. The main body is said to be imprisoned in a vast abyss, where it continues to build its web with single-minded devotion. The truth is unknown, but there is a theory that the apocalypse will come when the web is fully completed.'):
        "Una parte staccata dal dio ragno. Il corpo vero è rinchiuso in un abisso sterminato, dove si dice continui a tessere la tela senza distrarsi un attimo. Come stiano le cose non si sa, ma c'è chi sostiene che quando la tela sarà finita arriverà la fine del mondo.",

    # ---------------------------------------------------------- :9767 il gran drago
    (9767, 'A higher form of the great dragons, with a preference for the ether wind. The blows delivered from its huge body are simple but extremely powerful and they no longer require breath. '):
        "La specie superiore dei grandi draghi, e ha un debole per l'etere. I colpi che sferra con quel corpo enorme sono semplici ma di una potenza estrema, e ormai del soffio non ha più bisogno. ",

    # ---------------------------------------------------------- :9780 il cacciatore di taglie
    (9780, 'They make a living by pursuing bounties. As bandits are more likely to appear in towns where merchants congregate, hunters who come to hunt them often settle directly in the area. '):
        "Si guadagna da vivere dando la caccia a chi ha una taglia sulla testa. Nelle città dove si radunano i mercanti i ladri saltano fuori con facilità, e così i cacciatori che ci arrivano per stanarli spesso finiscono per stabilircisi. ",

    # ---------------------------------------------------------- :9793 il Tsathoggua
    (9793, 'One of the gods worshipped in the underworld. He is relatively tolerant and even lends his power to pious believers. Because of the strength of other deities in this Irva, he is unable to descend in full form.'):
        "Una delle divinità venerate nel mondo sotterraneo. È piuttosto tollerante, e ai fedeli devoti presta perfino la sua forza. Qui in Irva la forza delle altre divinità è grande, e per questo non riesce a discendere nella sua forma piena.",

    # ---------------------------------------------------------- :9806 il Nyarlathotep
    (9806, 'A mighty divinity with a thousand faces and no face. He is the kind of person who treasures chaos above all else, spreads madness and confusion, and leads people to their doom. He is the type of person who spread misinformation just for the fun of it.'):
        "Una divinità possente, senza volto e insieme con mille volti. Sopra ogni cosa tiene al caos: sparge follia e confusione e conduce gli uomini alla rovina. È il tipo che mette scompiglio per mezzo divertimento.",

    # ---------------------------------------------------------- :9819 il Re in Giallo
    (9819, 'Husband of Shub-Niggurath, divinity of the other world who governs the wind. He has been unable to descend fully due to the interference of the indigenous Irva wind goddess. '):
        "Marito di Shub-Niggurath, divinità di un altro mondo che governa il vento. La dea del vento nativa di Irva gli ostacola la strada, e così non riesce a discendere del tutto e resta con le mani in mano. ",

    # ---------------------------------------------------------- :9832 <Germoglio di Bambù>
    (9832, "Remnants of the Bamboo Tribe. They are trying to destroy the Mushroom Tribe's villages, but as they have never left their villages, they are unaware of the fact that the Mushroom Tribe, which has increased through spores, has spread all over the Tyris region. "):
        "Il superstite della gente dei germogli di bambù. Vuole distruggere la montagna della gente dei funghi, ma dal suo villaggio non è mai uscito, e non sa che i funghi, moltiplicandosi con le spore, si sono ormai sparsi per tutta la regione di Tyris. ",

    # ---------------------------------------------------------- :9845 il Kirin
    (9845, 'infinitely close to being a god. They are mild-mannered at heart, but will attack their opponents mercilessly. Their favourite drink is beer, but is that really true?'):
        "Una bestia fantastica ritenuta il capo degli animali, e vicina a un dio quanto più si può. In fondo è mite, ma su chi gli si oppone piomba senza pietà. Dicono che la sua bevanda preferita sia la birra: sarà vero?",

    # ---------------------------------------------------------- :9858 la giraffa
    (9858, 'A strange beast with an incredibly long neck and legs. It is very popular with children, but is said to be defeated by animals with long noses and large ears. There is also a phantom beast of the same name.'):
        "Una bestia strana, dal collo e dalle zampe lunghissimi. Piace moltissimo ai bambini, ma pare che perda il confronto con l'animale dal naso lungo e dalle orecchie grandi. Ed esiste anche una bestia fantastica che porta lo stesso nome.",

    # ---------------------------------------------------------- :9871 <Cavaliere Assassino>
    (9871, 'The soul of a knight, controlled by the urge to kill, is dwelling in his armour. A dangerous one who is calmed by the sight of blood. He is concerned that he still cannot remember his name when he was alive.'):
        "L'anima di un cavaliere dominata dall'impulso di uccidere, annidata dentro la sua armatura. Un tipo pericoloso, che si calma soltanto alla vista del sangue. Gli pesa non riuscire ancora a ricordare il nome che portava da vivo.",

    # ---------------------------------------------------------- :9884 <Lityou> la tigre bianca
    (9884, 'An age-old tiger has mutated. Its roar under the blue moonlight is somehow sad. When he hears poetry, he weeps without knowing why.'):
        "È una tigre molto vecchia che è mutata. Nel suo ruggito sotto la luna azzurra c'è qualcosa di malinconico. Quando sente una poesia piange, e non sa nemmeno perché.",

    # ---------------------------------------------------------- :9897 <Ex spazzino>
    (9897, 'A cleaner who reconciled with a snail at the end of a battle. Through her long years of training with the snail, she has developed unparalleled fighting skills as a human. '):
        "Uno spazzino che alla fine di una battaglia ha fatto pace con una lumaca. Dopo un lungo allenamento insieme alla lumaca ha acquistato una potenza di combattimento fuori misura per un essere umano. ",

    # ---------------------------------------------------------- :9910 <Lumaca> in sella all'androide
    (9910, 'Snail on a android. Close friends with the machine god Mani. His salt-resist defences are perfect and the android is equipped with a system that nullifies salt thrown at it.'):
        "Una lumaca in sella a un androide. Va d'accordo con Mani della Macchina. La sua difesa contro il sale è perfetta: l'androide monta un sistema che annulla il sale che gli tirano addosso.",

    # ---------------------------------------------------------- :9923 <Caim> il riccone folle
    (9923, 'He was a rich but mild-mannered man with no sarcasm, but one day he began to speak and behave as if he had gone mad. The cause is still unknown. '):
        "Era un uomo mite, ricco ma senza niente di antipatico, poi da un certo giorno in poi ha cominciato a dire e a fare cose da pazzo. La causa non si è ancora capita. ",

    # ---------------------------------------------------------- :9936 <Orphe> il servo del caos
    (9936, 'Orphe whose power has been amplified by the intervention of the Will of Chaos. He gained further power and a new sword of chaos, and also awakened his ability to use his lower level servants. '):
        "Orphe, la cui forza è stata amplificata dall'intervento della volontà del caos. Ha ottenuto altro potere e una nuova spada del caos, e in lui si è svegliata anche la capacità di comandare i figli del caos di rango inferiore. ",

    # ---------------------------------------------------------- :9949 <Siva> il dio della distruzione
    (9949, 'Although they look like just giant Shiba Inu, it is said that when the end of the world is near, they will show their true power and destroy the world in order to regenerate it. '):
        "A vederlo è soltanto un cane shiba gigantesco, ma si dice che quando la fine del mondo si avvicina mostri la sua vera forza e distrugga il mondo per farlo rinascere. ",

    # ---------------------------------------------------------- :9962 <Yerleswood> l'arma della battaglia decisiva
    (9962, 'It was the decisive weapon developed by the Yerles Army, but its overly superior AI refused to be treated as a weapon and escaped. A mass-produced version exists, with reduced costs and revised operational methods.'):
        "Era l'arma della battaglia decisiva sviluppata dall'esercito di Yerles, ma la sua intelligenza artificiale, fin troppo eccellente, si è rifiutata di essere trattata come un'arma ed è fuggita. Ne esiste un modello di serie, con i costi contenuti e l'impiego ripensato.",

    # ---------------------------------------------------------- :9975 <Ulzassil> il dio degli spettri
    (9975, "He was once a great mage, the pride of Eulderna, but he abandoned people and gave his soul to evil spirits and was reincarnated. He uses people's negative emotions as energy."):
        "Un tempo era il grande maestro dei maghi, il vanto di Eulderna, ma ha abbandonato la condizione umana, ha affidato l'anima agli spiriti maligni ed è rinato. Trae la sua energia dai sentimenti neri della gente.",

    # ---------------------------------------------------------- :9988 il cavaliere evocatore di Eulderna
    (9988, "A magic warrior with a knight's title who specialises in summoning magic. Because of their absolute confidence in their own magical power, many of them behave in a very snobbish manner."):
        "Un guerriero magico che porta il titolo di cavaliere e che eccelle nella magia di evocazione. Della propria forza magica sono sicurissimi, e per questo in molti hanno modi che non si sopportano.",

    # ---------------------------------------------------------- :10001 il berserker di Juere
    (10001, 'Jua warrior who has lost his sanity. In an attempt to compensate for his weak muscles, he tried to strengthen them with drugs, but the side effects amplified his destructive impulses.'):
        "Un guerriero di Juere che ha perso il senno. Per rimediare al suo punto debole, la forza fisica, ha provato a potenziarsi con dei farmaci, e l'effetto collaterale gli ha amplificato l'impulso di distruggere.",

    # ---------------------------------------------------------- :10014 <Mefan> la pifferaia
    (10014, 'She has absolute confidence in her own musical taste. Even when an audience member dies after hearing a devastatingly poor performance, she assumes that they died of shock because they were so impressed.'):
        "Del proprio gusto musicale è sicura in modo assoluto. Se qualcuno del pubblico muore dopo aver sentito un'esecuzione rovinosa, lei si convince che sia morto per l'emozione, tanto ne era rimasto colpito.",

    # ---------------------------------------------------------- :10027 l'ingenuo <Kyle>
    (10027, "Because of her mother's proper upbringing, he is not familiar with common sense and does not know how to use items well. He is heartbroken by his father's madness and tries to do something about it, even though he doesn't understand it well."):
        "La madre lo ha educato alla come viene, e così è digiuno di buon senso e non sa nemmeno bene come si usano gli oggetti. La follia del padre gli fa male al cuore, e pur senza capirci granché cerca in qualche modo di rimediare.",

    # ---------------------------------------------------------- :10040 il putit militare
    (10040, 'Putits trained to perform simple military tasks. They are not very good at fighting, but can be easily assembled in numbers and are widely used for reconnaissance, emergency rations, bullet repellent, suicide attacks, mine clearance, etc.'):
        "Putit addestrati a svolgere semplici mansioni militari. In combattimento valgono poco, ma è facile metterne insieme tanti, e così li sfruttano senza pietà per l'esplorazione, come razione d'emergenza, come parapalle, per gli assalti suicidi, per sminare e per altro ancora.",

    # ---------------------------------------------------------- :10053 <Orville> il comandante della sicurezza
    (10053, 'Because he is so incompetent, he was given the position of head of the security force, a guard of the fully automated security system. He feels guilty about it, but he never stops slacking off.'):
        "Siccome è di un'incapacità totale, gli hanno affidato il posto di comandante del corpo di guardia, o meglio di sorvegliante del sistema di sicurezza tutto automatico. Un po' se ne sente in colpa, ma non per questo smette di battere la fiacca.",

    # ---------------------------------------------------------- :10066 <Milis> la comandante delle forze speciali
    (10066, 'Professional special forces commander. She is faithful to her duties and strictly disciplined, but is stressed out because of this, and is secretly soothed by glancing at Putits with a sideways glance.'):
        "Una professionista che comanda le forze speciali. È fedele agli ordini e severa sulla disciplina, ma proprio per questo accumula tensione, e si consola di nascosto sbirciando i putit con la coda dell'occhio.",

    # ---------------------------------------------------------- :10079 <Cane poliziotto>
    (10079, 'It carries a handgun but will not fire unless cornered. If someone is crying, it gets distressed and cries with them. Friend of the military putits.'):
        "Porta con sé una pistola, ma non spara a meno che non lo mettano alle strette. Se qualcuno piange lui si mette in imbarazzo e finisce per piangere insieme a lui. Con i putit militari va d'accordo.",

    # ---------------------------------------------------------- :10092 <Ebarth> il capo dei pirati
    (10092, 'A leader of a band of rough-and-tumble pirates. In his youth, he was a man of the sea, burning with more romance and passion than any other man, but as he repeatedly plundered for a living, he somehow forgot his original intentions. '):
        "È lui a tenere insieme i pirati più turbolenti. Da giovane era un uomo di mare che ardeva di romanticismo e di passione più di chiunque altro, ma a furia di saccheggiare per campare, un po' alla volta si è scordato come aveva cominciato. ",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-020.jsonl'
DA, A = 9601, 10100
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
