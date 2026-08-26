# -*- coding: utf-8 -*-
"""102a - Lotto 3 di `db_card.hsp`: le carte fra la riga 1101 e la 1600 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello.

⭐ **Le parole che erano gia' decise altrove, e non si reinventano:**
`冥宮` → **Palazzo Infero** (`map.hsp:6524`), `亜竜` → **draco**
(`db_race.hsp:3276`), `世界樹` → **l'albero del mondo** (`db_card.hsp:9643`),
`ロストイルヴァ` → **Irva Perduta**, `ノルン` → **Norne**, `蜂蜜酒` →
**idromele**, `MP` resta **MP** (`chat.hsp:14465`, «gli MP»).

⚠️ **Il sesso di Norne non si scrive.** `:1265` parla di lui/lei e l'inglese di
monte dice `he` in una riga dove il giapponese non dice niente; nel dizionario
`Norne dice: ...` non porta genere. La resa gira la frase per non deciderlo.

⭐ **Tre giochi di parole che l'inglese lascia cadere.** `:1135` ツインテール e'
insieme l'acconciatura a codini e la bestia a due code; `:1486` 邪拳王 suona
come ジャンケン, il gioco; `:1512` chiude sul modo di dire 猫の手も借りたい,
«tanto da farmi prestare perfino la zampa di un gatto».

⚠️ `:1564` e `:1109` hanno in giapponese una frase in piu' dell'inglese, e in
tutt'e due e' la battuta finale. Si traduce il giapponese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :1109 il soldato oscuro blu
    # ⚠️ L'inglese porta la battuta finale; il giapponese la fa piu' corta.
    (1109, 'A lesser god that possesses the power of an evil spirit. He fires a heat ray of magical power from his torso to burn away his enemies. He is good at cutting down opponents who come at him with force, but he is not proficient in spiritual attacks. Is it wrong for him to attack with high heat when his body is blue? He is troubled by this.'):
        "Una divinità minore in cui abita la forza del dio oscuro. Dal torso spara un raggio termico di potere magico e incenerisce i nemici. È bravo a consumare chi gli viene addosso di forza, ma con gli attacchi allo spirito fa fatica. Lo tormenta un dubbio: avere il corpo azzurro e attaccare col calore non stonerà un po'?",

    # ---------------------------------------------------------- :1122 il soldato oscuro cremisi
    (1122, 'A lesser god that possesses the power of an evil spirit. He excels at simple violence, but in some cases he can also spit acid storms. He has low intelligence and operates almost entirely on instinct. Although he takes the appearance of crab, his physical structure is of a completely different type.'):
        "Una divinità minore in cui abita la forza del dio oscuro. È bravo nella violenza pura e semplice, ma all'occorrenza sputa anche tempeste d'acido. Ha poca intelligenza e va quasi solo d'istinto. All'aspetto sembra un granchio, ma la struttura del corpo è tutt'altra cosa.",

    # ---------------------------------------------------------- :1135 <Talka> dai codini lunghi
    # ⓘ ツインテール e' l'acconciatura a due codini **e** la bestia a due code:
    #    la battuta e' che le code le sono rimaste in testa.
    (1135, 'A twin-tailed girl who, wanting to become human, began to believe in God. Her wish was too vague and she ended up with a half-baked human form. At first she was uncomfortable with the tail on her head, but upon realizing that it could be of some use, she is now happy with it.'):
        "Una bestia a due code che, per diventare umana, si è messa a pregare le divinità. Il desiderio era troppo vago, e ne è uscita una forma umana lasciata a metà. All'inizio le pareva strano avere le code attaccate alla testa, ma poi ha scoperto che così sono comode, e adesso è contenta.",

    # ---------------------------------------------------------- :1148 il gigante artificiale oscuro
    (1148, "Originally, it was a general-purpose humanoid defense weapon designed to protect humanity from hostile entities. It was created by the humans of the time, who admired the Titan of Light, by combining together several super-technologies. That's why it's so hard to control, ultimately falling to the side of darkness, and it is now on a violent rampage."):
        "In origine era un'arma difensiva umanoide polivalente, fatta per proteggere il genere umano dalle entità ostili. Gli uomini di allora, che ammiravano il gigante di luce, la crearono mettendo insieme tecnologie troppo avanzate per loro. Proprio per questo si controlla poco, ed è finita per cadere nell'oscurità e scatenarsi.",

    # ---------------------------------------------------------- :1161 il Surtr
    (1161, 'His name means \\"The Black One\\". He is a giant who claims to have burned down the entire world with flames. However, there is a theory that all he actually did was set fire to the world tree, while using the confusion of the Great War to push his exaggerated stories.'):
        "Il nome significa il Nero. È un gigante che si vanta di avere incenerito il mondo intero con le fiamme. C'è però chi sostiene che, approfittando della confusione della guerra, abbia soltanto dato fuoco all'albero del mondo, e che il resto sia esagerazione sua.",

    # ---------------------------------------------------------- :1174 il Gigantes
    (1174, 'A giant who boasts of his monstrous strength. There is a record of him grabbing an Indian elephant that was trying to fight him and throwing it ten miles. His ancestors had a unique constitution that prevented them from being killed by the gods, but they lost it over the generations.'):
        "Un gigante che va fiero della sua forza mostruosa. Risulta agli atti che afferrò un elefante indiano venuto a cercar rissa e lo scagliò per dieci miglia. I suoi antenati avevano una costituzione particolare che impediva alle divinità di ucciderli, ma di generazione in generazione l'hanno perduta.",

    # ---------------------------------------------------------- :1187 la signorina di ottanta piedi
    (1187, 'The young lady of the giant race. Her height grows explosively during her formative years, but until then, she can slip into human civilization unnoticed. She loves small, cute things and is morbidly obsessed with them, but often kills them by mistake. When the going gets tough, she tries to cover it up by imitating the cries of pigeons.'):
        "La signorina della stirpe dei giganti. Nell'età dello sviluppo cresce di statura in modo esplosivo, ma prima di allora può anche vivere mescolata fra gli uomini. Ama le cose piccole e carine di un'ossessione morbosa, e spesso, sbagliando la forza, le uccide senza volerlo. Quando la faccenda si mette male, chissà perché, prova a cavarsela imitando il verso del piccione.",

    # ---------------------------------------------------------- :1200 la donna di cristallo
    (1200, 'A crystal that absorbs magical power transforms into a crystalian after many years. She is confident in her beauty and tries to attract both men and women. The color of the crystal at birth is determined by the quality and quantity of magic power absorbed, but every individual crystalian seems to think that their own color is the most beautiful.'):
        "Un cristallo che, assorbendo potere magico per lunghissimi anni, si è trasformato. Ha fiducia nella propria bellezza e cerca di ammaliare uomini e donne senza distinzione. Il colore che ha alla nascita dipende dalla qualità e dalla quantità del potere assorbito, ma pare che ogni esemplare consideri il proprio il più bello di tutti.",

    # ---------------------------------------------------------- :1213 il duca elettromagnetico
    (1213, "A mag count that has absorbed electricity and developed a stronger magnetic force. Among his peers, he is called a duke, which is higher than a count. He can't maintain his current standing without sufficient electrical power, so he sometimes attacks cities in search of power sources."):
        "Il conte magnetico che, ottenuta l'elettricità, ha sviluppato una forza magnetica più forte. Fra i suoi simili lo dicono di grado ducale, che sta sopra a quello comitale. Senza elettricità a sufficienza la posizione non la tiene, e allora capita che assalti le città per procurarsela.",

    # ---------------------------------------------------------- :1226 il conte magnetico
    (1226, 'A rock monster that can manipulate magnetic forces at will. Among those of his kind, it is said that the one who can collect the most iron sand is the greatest, and they are granted the title of Count.'):
        "Un mostro di roccia che è arrivato a manovrare a piacere la forza magnetica. Fra i suoi simili vale il principio che conta di più chi riesce a raccogliere più sabbia ferrosa, e in quella scala questo qui è di grado comitale.",

    # ---------------------------------------------------------- :1239 la giovane rondine
    (1239, 'A swallow chick who can\'t fly yet. He is a nasty bird and spreads feces around. He is disgusted to see his father so absorbed in his work with a happy face, and wants to leech off of him instead of working in the future.'):
        "Un rondinotto che ancora non vola. È chiassoso e per giunta sparge escrementi in giro. Vedere il padre che si tuffa nel lavoro con quella faccia felice lo disgusta, e da grande vorrebbe non lavorare e farsi mantenere.",

    # ---------------------------------------------------------- :1252 l'ape magica
    (1252, "A worker bee born from a queen bee. She likes to dance, and when she finds a place to feed, she dances to let her sisters know. She has a serious sweet tooth, but she doesn't snack on the honey she collects and brings it home with her."):
        "Un'ape operaia nata dall'ape stregina. Le piace ballare, e quando trova un posto dove mangiare balla per avvisare le sorelle. È golosissima, ma il miele che raccoglie non lo assaggia: si trattiene e lo porta a casa tutto.",

    # ---------------------------------------------------------- :1265 <Yonorne> la guida novellina
    # ⚠️ Norne non prende genere: la frase gira apposta. Vedi il docstring.
    # ⚠️ rete 3: l'ultima proposizione giapponese sta anche in
    #    `tcg_custom.hsp:1936`, gia' resa. Si ricopia da li'.
    (1265, "Norn's sister, who's not related by blood. At first, Norn was very confused by her sister, since he didn't know where she came from, and even now he keeps her at a distance. She's not much of a fighter, but she does her best to guide people with her natural cheerfulness."):
        "La sorella minore di Norne, che non ne ha il sangue. All'inizio questa sorella spuntata da chissà dove ha messo Norne in grande imbarazzo, e un po' di distanza resta ancora oggi. In combattimento non vale nulla, ma fa del suo meglio per guidare la gente con quel buonumore che si ritrova.",

    # ---------------------------------------------------------- :1278 <Scard> la rondine felice
    (1278, 'A swallow who is a slave to his own happiness. His job is to strip rich people of their clothes and give their money to the poor. He convinces himself that he is happy, and drowns his sorrows over the loss of his wife in his childrearing and work.'):
        "Una rondine prigioniera del proprio essere felice. Il suo mestiere è spogliare i ricchi di tutto quello che hanno e passarne il denaro ai poveri. Si ripete che è felice, e annega nel lavoro e nella cura dei figli il dolore per la moglie perduta.",

    # ---------------------------------------------------------- :1291 <Oxode> l'ape stregina
    (1291, 'A widowed bee who runs a company that produces honey wine. Her saliva contains a special magical power that allows her to quickly process the honey she collects. She has a gentle personality, but is very strict when it comes to how she raises her children.'):
        "Un'ape vedova che manda avanti un'azienda di idromele. Nella saliva ha un potere magico speciale che lavora in un attimo il miele raccolto. Ha un carattere pacato, ma sull'educazione dei figli è piuttosto severa.",

    # ---------------------------------------------------------- :1304 <Imarituka> lo sberleffo di casa
    (1304, "A girl who walks from house to house making a fool of herself. It is said that she brings good luck as long as she smiles and lives there, and misfortune as soon as she leaves. She is actually a child spirit. It is said that she was killed and buried under the floor for taunting adults too much. Even now, it's been said that she tries to attract people's attention by being mean to them."):
        "Una bambina che va di casa in casa a prendere in giro chi ci abita. Si dice che finché ride e resta lì porti fortuna, e che appena se ne va arrivi la sciagura. In verità è lo spirito di una bambina: pare che a furia di sbeffeggiare i grandi l'abbiano uccisa e sepolta sotto il pavimento. Ancora oggi fa dispetti solo perché vorrebbe attenzione.",

    # ---------------------------------------------------------- :1317 <Telhureza> il geco di guardia
    (1317, "Also known as Menhera's Gecko. He takes advantage of his regenerative abilities to leisurely cut his wrists. He loves the household that took him in more than anything else, and sticks to the wall with his powerful suction cups to keep a focused and watchful eye on it."):
        "Detto anche il geco molesto dall'umore instabile. Sfrutta la sua grande capacità di rigenerarsi e si taglia i polsi con leggerezza. Ama sopra ogni cosa la casa che l'ha accolto, e finisce per attaccarsi al muro con le ventose potenti e sorvegliarla con una calma appiccicosa.",

    # ---------------------------------------------------------- :1330 il ghebardo di un altro mondo
    (1330, 'A cat that came from another world after being hit by a truck. For some unknown reason, he has gained the innate powers of cheating and can recite magic without consuming MP. He is held in unusually high regard by his own kind, but that is because he is unconsciously casting domination magic on them all.'):
        "Un gatto arrivato da un altro mondo nell'istante in cui un camion l'ha investito. Non si sa per quale ragione, ma ha acquisito una costituzione da baro e recita gli incantesimi senza consumare MP. I suoi simili lo stimano stranamente, ma è perché lancia magie di dominio senza nemmeno accorgersene.",

    # ---------------------------------------------------------- :1343 il ghebardo velocista
    (1343, 'A cat who has been celebrated since ancient times as an animal that can run extremely fast. As a result of recent research, it turned out that his abilities were merely the result of cheating, causing a huge firestorm of backlash.'):
        "Un gatto celebrato fin dall'antichità come l'animale che corre più veloce di tutti. Ricerche recenti hanno stabilito che era soltanto un imbroglio, e ne è nato un putiferio.",

    # ---------------------------------------------------------- :1356 il ghebardo dalla mira automatica
    (1356, 'He was once feared as a magic bullet archer who could hit a hundred targets with a hundred shots. However, after many years of slacking off, his skills have degraded to the level of a scum. In order to regain his past glory, he chose to turn to cheating.'):
        "Un tempo lo temevano come il tiratore dal proiettile magico che fa cento colpi su cento. Poi si è montato la testa, ha oziato per anni, e la lunga pausa gli ha ridotto la mira a una schifezza. Per riprendersi la gloria di un tempo ha scelto di darsi all'imbroglio: una schifezza vera e propria.",

    # ---------------------------------------------------------- :1369 il ghebardo passamuri
    (1369, 'In order to survive on the battlefield without effort, he has acquired the cheat ability to hide behind walls. However, he has an unbearable personality and tends to jump out of walls. He also floats in the air as a bonus.'):
        "Per sopravvivere sul campo di battaglia senza fare fatica si è procurato il trucco di infilarsi dentro i muri. Ma non ha pazienza, e finisce sempre per saltarne fuori. E già che c'è, fluttua anche a mezz'aria.",

    # ---------------------------------------------------------- :1382 il demone del palazzo infero
    (1382, "A demon with a very bad personality. He is the culprit behind the creation of the Underworld Palace, tricking and dragging in souls that should be going elsewhere. He harasses those who can't resist and smirks at them to no end."):
        "Un demone dal carattere pessimo. È lui il colpevole: ha creato il Palazzo Infero e ci trascina dentro con l'inganno le anime che dovrebbero andare altrove. Perseguita fino in fondo chi non può opporsi, e intanto ghigna.",

    # ---------------------------------------------------------- :1395 la nebbia della morte
    (1395, 'A fog-like monster that arises from the foggy magic of the dead. It likes damp places, but cannot choose where to stay because it is blown away by the wind.'):
        "Un mostro fatto di nebbia, nato dal potere magico disperso dei morti. Predilige i luoghi umidi, ma il vento se lo porta via e il posto dove stare non può sceglierlo.",

    # ---------------------------------------------------------- :1408 lo spirito che si aggrappa
    (1408, 'A giant spirit that clings to the living. They are harmful with their terrifying obsession and power, but in reality they are just desperately clinging to people because they want someone to save them.'):
        "Uno spirito enorme che si aggrappa ai vivi. Fa danno con un'ostinazione e una forza spaventose, ma in verità sta solo aggrappandosi con tutte le forze perché vorrebbe che qualcuno lo salvasse.",

    # ---------------------------------------------------------- :1421 l'anima smarrita
    (1421, "He was a child of a normal family, where nothing particularly went wrong. He is ignorant, pure, and innocent. That's why he's an easy target for deception by demons and often gets lost in the underworld."):
        "Era il bambino di una famiglia normale, senza niente di particolare. Ignorante, puro, innocente. E proprio per questo i mostri malvagi lo ingannano e lo fanno smarrire nel Palazzo Infero.",

    # ---------------------------------------------------------- :1434 il wyrm possente
    (1434, 'A monster that reigns as the strongest of the sub-dragons. He spits out a tremendous breath and is so powerful that he is said to shatter stars, but he also calls upon each one of his allies. He understands that it is important not to be too proud of his power, even if he is the strongest.'):
        "Il mostro che siede sul trono di draco più forte. Sputa un soffio tremendo ed è potente al punto che lo si dice capace di frantumare le stelle, eppure chiama i compagni uno dopo l'altro: ha capito che, per quanto si sia i più forti, non bisogna montarsi la testa.",

    # ---------------------------------------------------------- :1447 lo pteraiun
    (1447, "A pterosaur that can control electricity. It can't generate electricity on its own, so it periodically recharges itself by flying through thunderclouds. It is said that it risks his life because his body will be burnt or explode if it overcharges."):
        "Uno pterosauro che manovra le scariche elettriche. Da solo non produce corrente, e allora si ricarica periodicamente dentro le nubi temporalesche. Se si carica troppo il corpo gli si brucia o gli esplode: pare che ci rischi la vita.",

    # ---------------------------------------------------------- :1460 il wyrm selvatico
    (1460, 'A sub-dragon with the body of a snake, the head of a dragon, and the wings of a bat. It has a ferocious and belligerent personality. It is long and slender, so it can get into narrow spaces. However, once it gets entangled, it becomes unable to help itself and has no choice but to await death.'):
        "Un draco con il corpo di serpente, la testa di drago e le ali di pipistrello. Ha un carattere feroce e attaccabrighe. È lungo e sottile, quindi si infila anche negli spazi stretti; ma una volta che si aggroviglia non se ne cava più da solo, e non gli resta che aspettare la morte.",

    # ---------------------------------------------------------- :1473 il portaratti
    (1473, "A rare pterosaur that coexists with rats. It is confident in its carrying ability, but is weak and not good at fighting. It searches for its prey from above and drops a large number of rats, then gratefully consumes what's left over."):
        "Un raro pterosauro che vive in simbiosi con i ratti. Ha fiducia nella propria capacità di trasporto, ma è di animo debole e combattere non fa per lui. Cerca la preda dall'alto e le lascia cadere addosso una valanga di ratti; poi ringrazia e si prende gli avanzi.",

    # ---------------------------------------------------------- :1486 il re della morra
    # ⓘ 邪拳王 «il re del pugno malvagio» suona come ジャンケン, il nome giapponese
    #    della morra cinese: la carta racconta l'origine del gioco.
    (1486, 'An evil monster with three hands. A bard who saw a fight between this monster and a fighter recreated the scene and passed it around from place to place. Some have said that it later became a game, and was named rock-paper-scissors after the monster.'):
        "Un mostro malvagio fatto di tre mani. Un menestrello che vide lo scontro fra lui e un lottatore ne rifece la scena e la portò in giro di paese in paese. C'è chi dice che più tardi sia diventata un gioco, e che la morra abbia preso il nome da questo mostro.",

    # ---------------------------------------------------------- :1499 il lottatore maledetto
    (1499, "An incarnation of fateful end of those who seek too much power. It seems that he was given the power of the curse by a demon and became a monster. He has only his hands, but he's rather happy with them."):
        "Quel che resta di chi ha cercato troppo la forza. Pare che un demone di pessima specie gli abbia messo in mano il potere della maledizione, e che così sia diventato un mostro. Gli sono rimaste soltanto le mani, ma lui è abbastanza soddisfatto.",

    # ---------------------------------------------------------- :1512 la zampa del gatto divino
    # ⓘ L'ultima frase e' il modo di dire 猫の手も借りたい: si e' talmente indaffarati
    #    da farsi prestare perfino la zampa di un gatto.
    (1512, "A cat god who misbehaved too much had his hand cut off, and this what became of it. Also known as the God Cat Punch. The big paw is very soft to the touch. No matter how busy you are, it's going to be tricky having this hand on deck."):
        "Un dio gatto che aveva fatto troppe malefatte si vide tagliare la zampa, e da lì è nato. Detto anche il Divino Pugno di Gatto. I polpastrelli enormi sono meravigliosi da toccare. Ma per quanto si abbia da fare, farsi prestare questa zampa è un'impresa.",

    # ---------------------------------------------------------- :1525 la cortigiana dalla bocca in mano
    (1525, 'A giant hand demon that mimics humans out of admiration for them. It is usually dressed up and goes for a walk when in a good mood, but when it finds prey, its appetite wins out. It grabs the prey with its lower body and preys on it with the huge mouth in the palm of its hand.'):
        "Un demone dalla mano gigantesca che, per ammirazione verso gli uomini, ne ha preso le sembianze. Di solito si fa bella e passeggia di buon umore, ma quando trova una preda l'appetito ha la meglio: la ghermisce con la parte inferiore del corpo e la divora con la bocca enorme che ha nel palmo.",

    # ---------------------------------------------------------- :1538 la mano bianca che chiama
    (1538, 'A collection of eerie white hands. It is difficult to resist their magical beckoning. It grabs the living with its terrifying power and tries to drag them to the root. It is said that its root is connected to hell.'):
        "Un ammasso di mani bianche inquietanti. Al loro cenno, carico di potere magico, è difficile resistere. Afferrano i vivi con una forza spaventosa e cercano di trascinarli giù verso la radice. Pare che quella radice arrivi fino all'inferno.",

    # ---------------------------------------------------------- :1551 <Aime> la narratrice
    (1551, 'A mysterious storyteller. She has the ability to connect the world of possibilities through books. She claims to be from Lost Irva, but no one knows who she is. Perhaps she herself is from another world.'):
        "Una narratrice misteriosa. Ha il potere di collegare fra loro i mondi possibili attraverso i libri. Dice di venire da Irva Perduta, ma nessuno la conosce. Con ogni probabilità viene anche lei da un altro mondo.",

    # ---------------------------------------------------------- :1564 l'occhio del sorvegliante
    # ⚠️ L'inglese lascia cadere l'ultima frase, che e' il modo di dire su cui la
    #    carta si chiude: 「神様はみておるぞ！」
    (1564, "Gods' system. They monitor humanity and record their karma. However the standard of Gods' morality is a mystery. Even if they find something wrong they basically just watch and won't stop it unless they are attacked themselves."):
        "Il sistema delle divinità. Sorveglia il genere umano e ne registra il karma. Il criterio con cui le divinità giudicano, però, è piuttosto oscuro: anche quando scopre una malefatta, di regola si limita a guardare e non interviene, salvo che sia lui a essere aggredito. Quando si rimprovera un cattivo dicendo che le divinità guardano, è proprio lui che guarda.",

    # ---------------------------------------------------------- :1577 l'occhio di Horus
    (1577, 'It is a symbol of all-seeing wisdom and healing restoration and renewal. The god Horus was defeated in the Great War of the Gods and his left eye was carefully pulverized so that he could not regenerate. However countless pieces of his left eye regenerated individually and this demon was born.'):
        "È il simbolo della sapienza che vede ogni cosa, e insieme della guarigione, della riparazione e della rinascita. Il dio Horus fu sconfitto nella grande guerra delle divinità, e perché non potesse rinascere lo ridussero in polvere con cura, l'occhio sinistro compreso. Ma gli innumerevoli frammenti dell'occhio sinistro rinacquero ognuno per conto suo, e così nacque questo mostro.",

    # ---------------------------------------------------------- :1590 il mostro dai cento occhi
    (1590, 'A monster with a large amount of creepy eyes. It was given this name because it has many eyes but it was found that the number of eyes is not a hundred and there are individual differences. It seems like they have sharp points all over their body so their is not easy to be hit considering his size.'):
        "Un mostro con una gran quantità di occhi inquietanti. Il nome gli viene dal numero di occhi, ma a contarli davvero non sono cento, e per giunta variano da individuo a individuo. È come se avesse punti deboli su tutto il corpo, e per la mole che ha incassa poco.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-003.jsonl'
DA, A = 1101, 1600
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
