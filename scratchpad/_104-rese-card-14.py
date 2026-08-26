# -*- coding: utf-8 -*-
"""104a - Lotto 14 di `db_card.hsp`: le carte fra la riga 6601 e la 7100 (38).

⚠️⚠️⚠️ **NOVE CARTE DI QUESTO LOTTO SONO TRADOTTE SOLO DAL GIAPPONESE**, perche'
il loro inglese e' quello di un'altra carta. Da `:6972` a `:7063` l'inglese di
monte e' **indietro di un posto**: `:6985` porta la prosa dello spaghetto,
`:6998` quella della viverna, e cosi' via fino a `:7063`, che porta quella del
lanciabombe. Monte si riallinea a `:7076` **buttando via** l'inglese di `:7063`,
che nel sorgente non esiste da nessuna parte.

    :6972  il mostro di spaghetti          EN di :6959   ⚠️ solo dal giapponese
    :6985  la viverna folgorante           EN di :6972   ⚠️
    :6998  <Melugast type0>                EN di :6985   ⚠️
    :7011  <Norne> la guida                EN di :6998   ⚠️
    :7024  il Mara                         EN di :7011   ⚠️
    :7037  il mortaio semovente di Yerles  EN di :7024   ⚠️
    :7050  il lanciabombe                  EN di :7037   ⚠️
    :7063  lo Yerleswood di serie          EN di :7050   ⚠️
    :7076  il drago della nebbia           il suo        ✅ qui monte si riallinea

⭐⭐ **La 103a aveva chiamato `:6959`/`:6972` una coppia, e non lo e': e' la
testa di una catena di nove.** Il primo anello lo trova
`_103-inglese-ripetuto.py`, che cerca due inglesi uguali; dal secondo in poi
ogni inglese compare **una volta sola** e quella rete tace. La regola nuova sta
in `scratchpad/_104-inglese-slittato.py`: **quando salta fuori un doppione, il
dossier delle venti carte successive si legge a mano.** ⚠️ E i due segnali
automatici di quella rete, misurati su questo blocco, accendono su **cinque
carte su nove**: sono un aiuto alla lettura, non un cancello.
ⓘ Verificato che gli altri due doppioni **non** propagano: `:4138` e `:9650`
hanno il loro inglese. Sono due forme diverse dello stesso guasto.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `外法` → **le arti proibite**
(lotti 12 e 13), `異形の森` → **la Foresta Eretica** (`chat.hsp:1600`),
`追放者` → **l'esiliato** (`action.hsp:16868`), `地雷侍` → **il samurai
kamikaze** (`:11385`), `冥界ドラゴン` → **il drago dell'oltretomba** (`:12947`),
`用心棒` → **il guardaspalle** (`:13376`), `ロックスロアー` → **il lanciapietre**
(`:13493`), `竜窟` → **la Tana del Drago** (`text.hsp:2785`), `エーテル` →
**etere**, `レム・イド` → **Rehm-Ido** (`chat.hsp:8144`), `元素の神` → **il dio
degli elementi** (`text.hsp:542`), `中級神` → **divinita' di medio rango`.

⚠️⚠️ **`レム・イド` non e' `レミード`.** Rehm-Ido e' la **civilta'**, Remido sono
le **rovine**: due nomi diversi che si somigliano, e a `:7076` serve il primo.

⚠️⚠️ **`エルン` si scrive `Eln`, e la decisione e' di oggi.** Era reso in due
modi (`Eln` in `chat.hsp:7676`, `Elun` in `:9499`) perche' **anche l'inglese di
monte lo scrive in due modi**, e ogni lotto ha seguito il file che aveva davanti
— la stessa forma esatta del guasto di `キッカス`. Unificato da
`scratchpad/correzione-eln.py`. Serve a `:7011`, che apre proprio su
「エルンという種類の妖精」.

⚠️ **Un errore di monte fuori dal blocco:** `:6959` perde la **prima frase** del
giapponese — 集団で一撃離脱を繰り返す戦法を得意とする, *combatte in gruppo,
colpisce e si sfila* — che e' proprio quello che spiega il nome della carta.
Rimessa.

⭐ **`:6829` e `:6842` sono una coppia, e il bisticcio sta nel nome.**
`ケサランパサラン` e' il batuffolo del folklore giapponese, e `ダーティパサラン`
gli toglie il `ケサラン`: i nomi sono gia' resi `il kesaranpasaran` e `il pasaran
sudicio`, e la prosa dice la superstizione, che e' quello che fa il giapponese.

⚠️ **Niente virgolette, niente caporali, niente lineette lunghe**: le 「」 di
`:6829` si sciolgono nella frase. E le cifre a doppia larghezza si scrivono
normali (`10人に8人` → 8 su 10).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :6608 il fiore infernale
    (6608, 'A single flower that grows in the crater of hellish heat and sways in the heat of it. High heat is the source of energy and the excess heat is expelled as flame magic. As expected it seems to burn when exposed to lava.'):
        "Un fiore solitario che cresce dentro crateri caldi come l'inferno e ondeggia in quella vampa. Il calore altissimo è la sua fonte di energia, e quello che gli avanza lo butta fuori sotto forma di magia del fuoco. Se però gli si rovescia addosso della lava, allora sì che brucia.",

    # ---------------------------------------------------------- :6621 il verme proiettile
    (6621, "It swallows the minerals produces bullets in its body and spits them out of its mouth. If that's all it's no big deal but it's dangerous to approach them because they may shoot at you while biting you."):
        "Ingoia minerali, dentro il corpo se ne fabbrica pallottole e le sputa dalla bocca. Se fosse solo questo non sarebbe granché, ma capita che spari a bruciapelo mentre ti tiene addentato: avvicinarsi è pericoloso.",

    # ---------------------------------------------------------- :6634 il verme delle sabbie
    (6634, 'They are mainly sand bugs that live in sandy areas but they can get lost while burrowing on the ground and show their faces in out-of-place places. They move quickly for their size diving into a hole in an instant and coming out of it in an instant.'):
        "È un verme di sabbia e vive soprattutto sui terreni sabbiosi, ma mentre se ne va sottoterra capita che si perda e che spunti fuori in posti dove non c'entra niente. Per la mole che ha si muove svelto: in un attimo si infila nel buco e in un attimo rimette fuori la testa.",

    # ---------------------------------------------------------- :6647 il cinghiale distruttore
    (6647, "A giant wild boar so frenzied that it can't be touched. Some farmers are proud of the fact that this guy has come to their fields because gourmets aim for only delicious crops."):
        "Un cinghiale gigantesco e talmente furioso che non c'è verso di tenerlo. È un buongustaio e punta soltanto ai raccolti buoni, tanto che c'è perfino qualche contadino che si vanta di averlo visto nel proprio campo.",

    # ---------------------------------------------------------- :6660 il cinghiale scatenato
    (6660, 'A giant beast. He has no special powers but his rush after he puts on his main run is more than powerful enough. It\'s agile and can turn swiftly.'):
        "Una bestia selvatica enorme. Poteri particolari non ne ha nessuno, ma quando prende la rincorsa e carica la potenza è più che sufficiente. E chi lo credesse buono solo a caricare si sbaglia: è svelto e gira stretto.",

    # ---------------------------------------------------------- :6673 il cinghialetto
    (6673, "A wild boar cub with cute stripes. I don't think this thing will grow up and become such a ferocious beast. Even though he is a child the rush of a one-shot release is masterful."):
        "Un cinghiale piccolo, con certe righe che sono una tenerezza. Non si direbbe che crescendo diventi quella bestiaccia. Anche se è un cucciolo, il modo in cui carica e si sfila subito dopo è da manuale.",

    # ---------------------------------------------------------- :6686 il koala mangiabuio
    (6686, 'It continued to evolve in the direction of feeding on things that other animals would not and eventually came to eat dark matter. It is almost impossible to break down even if eaten so the body is black. They march in groups in the dark.'):
        "Si è evoluto continuando a puntare su quello che gli altri animali non mangiano, e alla fine è arrivato a nutrirsi di materia oscura. Mangiarla la mangia, ma digerirla quasi per niente, e per questo dentro è nero come la pece. Nelle notti senza luna marcia in gruppo.",

    # ---------------------------------------------------------- :6699 <Nein> la strega volante
    (6699, "A girl born into a family of talented wizards she is also blessed with talent. This has been greatly enhanced by the meritocratic education in Eulderna. She's trying to popularize the broom riding style but she's not making much progress."):
        "Una ragazza nata in una famiglia di ottimi maghi, e col talento in dote pure lei. Fra questo e l'istruzione di Eulderna, che premia solo chi vale, le è montata la testa per bene. Sta cercando di lanciare la moda di andare in scopa, ma finora i risultati sono scarsini.",

    # ---------------------------------------------------------- :6712 <Raizel> il vecchio incantatore
    (6712, 'He was once the strongest mage of Eulderna. He is currently unable to use most of his magic due to dementia. Even now however he still possesses magical powers that surpass those of advanced mages and it is said that the King of Eulderna respects him.'):
        "Fu il più forte incantatore di Eulderna. Adesso è caduto in demenza e la maggior parte delle sue magie non le sa più usare. Eppure il potere magico che si ritrova supera ancora quello di un incantatore di grado alto, e si dice che perfino il re di Eulderna gli porti rispetto.",

    # ---------------------------------------------------------- :6725 <Gigante Castagna>
    (6725, 'Chestnuts that were mistreated gather together to get rid of their resentment and transform themselves into giants. It has a strong body and does not burst from the heat even when exposed to fire. It has a companionate nature and its heart aches when it hits another chestnut.'):
        "Sono castagne trattate male che si sono radunate per prendersi la rivincita e si sono trasformate in un gigante. Ha un corpo robusto, e se lo si mette sul fuoco non scoppia per il calore. Tiene ai suoi simili, e quando gli tirano addosso una castagna ci soffre.",

    # ---------------------------------------------------------- :6738 l'insegnante
    (6738, 'He is a bouncer by profession but he can\'t make a living by himself so he also works as a tutor. His special skills are shrimp warping and swordsmanship. His tone is polite but his reaction is a little exaggerated.'):
        "Di mestiere fa il guardaspalle, ma di quello solo non si campa e allora arrotonda dando ripetizioni a domicilio. Le sue specialità sono l'inarcamento a gambero e la scherma. Parla in modo educatissimo, però reagisce a tutto un po' troppo.",

    # ---------------------------------------------------------- :6751 il mostro di tartufini
    (6751, 'The soul is in a mushroom-like chocolate called a truffle which looks a lot like a mushroom. They are aware that they were created to be eaten but they are unable to accept their fate meekly.'):
        "In un cioccolatino che somiglia molto a un fungo, e che per questo chiamano tartufo, si è insediata un'anima. Sa benissimo di essere stato fatto per essere mangiato, ma quel destino non riesce ad accettarlo di buon grado.",

    # ---------------------------------------------------------- :6764 <Sophia> la Saggia
    (6764, 'A mid-level god who presides over knowledge. There are few gods who know the whole story of the war between the gods. She is as intimate with the elemental god as grandfather and granddaughter and the exile is said to be modeled after her.'):
        "La divinità di medio rango che ha in mano la conoscenza. È una dei pochi del ceppo divino a sapere per intero come andò la grande guerra fra gli dei. Col dio degli elementi è in confidenza come una nipote col nonno, e dicono che su di lei sia modellato l'esiliato.",

    # ---------------------------------------------------------- :6777 l'erudito
    (6777, 'He has an unparalleled thirst for knowledge among the people of Euldera. It is not the wizard who systematized magic but the scholar although higher-level magic is not available to them.'):
        "Perfino fra i cittadini di Eulderna la sua sete di sapere spicca su tutte. Le magie di grado alto non sa usarle, però a mettere in ordine la magia e a farne un sistema non sono stati i maghi: sono stati gli eruditi.",

    # ---------------------------------------------------------- :6790 <Mary> l'entomologa
    (6790, 'A native of the strange forest. She is a scholar who is studying the effects of ether on bugs but her fighting power is high because she literally wrestles with violent bugs every day. A mother of one she is desperate not to be hated by her daughter these days.'):
        "Viene dalla Foresta Eretica. È una studiosa e si occupa degli effetti dell'etere sugli insetti, ma dato che ogni giorno finisce alle prese con insetti furiosi, e alle prese alla lettera, in combattimento se la cava benissimo. Ha una figlia, e ultimamente farebbe qualunque cosa pur di non farsi odiare da lei.",

    # ---------------------------------------------------------- :6803 <Alice> la formica gigante
    (6803, 'She runs around the forest with Mary to help her with her research. She has been rebellious lately but deep down she loves Mary very much. She loves sweets but she also usually eats caterpillars.'):
        "Ogni giorno gira il bosco al seguito di Mary e le dà una mano con la ricerca. Ultimamente fa un po' la ribelle, ma dentro di sé a Mary vuole un bene dell'anima. Va matta per i dolci, e comunque i bruchi e simili se li mangia senza farsi problemi.",

    # ---------------------------------------------------------- :6816 il corvo mercante
    (6816, 'A clever crow who learned basic business skills while being sent on an errand by the goddess of wealth. They are intelligent enough to see the value without being misled even if it is a shiny object.'):
        "Un corvo furbo, che a furia di essere mandato in giro a fare commissioni dalla dea della ricchezza ha imparato i rudimenti del mestiere. È abbastanza sveglio da valutare quanto vale una cosa senza lasciarsi abbagliare, e sì che parliamo di un corvo e di roba che luccica.",

    # ---------------------------------------------------------- :6829 il pasaran sudicio
    (6829, 'As a result of the superstition that Kesalanpatharan brings good fortune they have been subjected to the desires of humans and as a result they have become blackened and stained. Its mind is in a state of total disarray.'):
        "È un batuffolo stregato che si è preso addosso, tutta intera e per anni, l'avidità degli uomini, per via della superstizione secondo cui il kesaranpasaran porta fortuna. Alla fine si è annerito e insudiciato, e anche dentro gli si è inasprito tutto.",

    # ---------------------------------------------------------- :6842 il kesaranpasaran
    (6842, 'The hairball specter. On a windy day they can be seen desperately trying not to be blown away. They glare at their opponents when they are attacked because they use line-of-sight medium magic but their eyes are too small to tell if they are glaring.'):
        "Un batuffolo di pelo stregato. Nei giorni di vento lo si vede aggrapparsi con tutte le sue forze per non farsi portare via. La sua magia passa per lo sguardo, e quindi quando lo assalgono fulmina l'avversario con gli occhi, ma li ha così piccoli che non si capisce se stia fulminando qualcuno o no.",

    # ---------------------------------------------------------- :6855 la gigaformica regina
    (6855, "The parent of the ant-like giant creature. It sprays you with a lot of acid at a tremendous rate. There are too many kids and they have given up on identifying everyone's face."):
        "È la capostipite di quegli esseri giganteschi simili a formiche. Ti rovescia addosso acido a litri e a una velocità impressionante. Di figli ne ha talmente tanti che ha rinunciato a riconoscerli tutti in faccia.",

    # ---------------------------------------------------------- :6868 la samuraformica
    (6868, "Giant ant-like creatures. As a result of his interactions with the Jirai samurai he was awakened to his samurai spirit. When he realizes that he can't fulfill his role he boldly tries to kill himself. There will be no slave-hunting."):
        "Un essere gigantesco simile a una formica. A furia di frequentare i samurai kamikaze, fra una cosa e l'altra le si è risvegliato dentro lo spirito del samurai. Quando capisce di non poter più fare la sua parte, senza dire niente cerca di darsi la morte. Alla caccia agli schiavi e simili non partecipa.",

    # ---------------------------------------------------------- :6881 la gigaformica
    (6881, 'Giant ant-like creatures. It is difficult to see in the dark. These hard-working girls work hard every day to bring in people and animals to feed themselves. She also has a cute side in that she has an eye for sweets.'):
        "Un essere gigantesco simile a una formica. Al buio è difficile accorgersi che c'è. Sono ragazze gran lavoratrici, che ogni giorno si sfiancano a trascinare a casa uomini e animali da mangiare. E hanno anche un lato tenero: per i dolci vanno matte.",

    # ---------------------------------------------------------- :6894 il soldato demoniaco di Juere
    (6894, 'A soldier fused with a prototype magic item taken from Eulderna; 8 out of every 10 people die when their mana flow goes haywire due to failure to adapt during the fusion phase.'):
        "Un soldato fuso con un oggetto magico sperimentale rubato a Eulderna. Dicono che 8 su 10 non reggano la fase della fusione: il flusso del mana gli va per traverso, e muoiono.",

    # ---------------------------------------------------------- :6907 il granchio dell'oltretomba
    (6907, 'A crab that controls the power of the underworld. It is believed that the souls of the dead are eaten and it is said that if a person\'s soul is eaten he or she cannot be revived even by resurrection magic. It has a symbiotic relationship with the Underworld Dragon.'):
        "Un granchio che comanda la forza dell'oltretomba. Si crede che divori le anime dei morti, e gira voce che a chi si è fatto mangiare l'anima non lo riporti indietro nemmeno la magia di resurrezione. Col drago dell'oltretomba vive in simbiosi.",

    # ---------------------------------------------------------- :6920 <Spipha> la cacciatrice di draghi
    (6920, "More than half of her body has been transformed by the dragon's curse and she chooses low-exposure clothing to hide it. Her hatred of the dragon tribe is so strong that the dragon cave has been turned into a hunting ground."):
        "La maledizione del drago le ha trasformato più di metà del corpo, e per nasconderlo sceglie vestiti che coprono tutto. L'odio per la stirpe dei draghi ce l'ha così forte che dalla Tana del Drago, dopo che se l'è presa come riserva di caccia, i draghi sono spariti.",

    # ---------------------------------------------------------- :6933 il Telchine
    (6933, "A demon possessing a piece of the goddess. His lower body is a snake and he can't move well when his body temperature is low. As a byproduct it creates cold air which it uses to attack."):
        "Un mostro che porta dentro di sé una scheggia della dea. Ha il corpo dalla cintola in giù di serpente, e col freddo non riesce a muoversi bene. Per questo ruba il calore all'aria per potersi muovere, e come sottoprodotto genera gelo, che gli torna utile per attaccare.",

    # ---------------------------------------------------------- :6946 la Delphyne
    (6946, 'A demon in the form of a half-human half-snake that possesses a piece of a goddess. In exchange for the prophecy it asks for a sacrifice but keeps the one it likes alive and by its side as a servant.'):
        "Un mostro dal corpo mezzo umano e mezzo serpente, che porta dentro di sé una scheggia della dea. In cambio delle sue profezie pretende un sacrificio, ma la vittima che le piace la lascia in vita e se la tiene accanto come serva.",

    # ---------------------------------------------------------- :6959 il passero mozzatesta
    # ⚠️ L'inglese perde la PRIMA frase, che e' quella che spiega il nome.
    (6959, 'With one or two birds they are not much of a threat and are cute just by chirping but when there are more than three of them they bear their fangs.'):
        "La sua tattica è muoversi in gruppo, colpire e sfilarsi via, e ripetere. Uno o due non sono una gran minaccia: cinguettano e basta, e fanno pure tenerezza. Ma da tre in su tirano fuori le zanne.",

    # ---------------------------------------------------------- :6972 il mostro di spaghetti
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :6959.
    (6972, 'With one or two birds they are not much of a threat and are cute just by chirping but when there are more than three of them they bear their fangs.'):
        "Un mostro venuto da un altro pianeta, fatto a forma di spaghetti. Ha il vizio di posare i tentacoli sulla testa della gente e mettersi lì a riposare. C'è chi sostiene che sia stato l'incontro con questo mostro a dare l'idea da cui è nata una certa religione per burla.",

    # ---------------------------------------------------------- :6985 la viverna folgorante
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :6972.
    (6985, 'A spaghetti-like monster from a different universe. It has a habit of resting its tentacles on a person\'s head. There is a theory that this encounter with the monster was a catalyst for the birth of a parody religion...'):
        "È una sottospecie di drago nata lungo la strada dell'evoluzione, ed è la forma ultima della viverna. Va forte nel tiro di precisione e nel tiro rapido, e trapassa un bersaglio dopo l'altro come lampi che si susseguono.",

    # ---------------------------------------------------------- :6998 <Melugast type0> la nave interdimensionale
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :6985.
    (6998, 'The final form of Wyvern as a subspecies of the dragon that was born in the process of evolution. They excel at sniping and firing shooting out targets one after another like a flash of light.'):
        "È stata sviluppata per sfondare qualunque ostacolo e portare macchinari e uomini in qualunque posto. A differenza del modello definitivo, l'unità che piega le dimensioni è interamente incorporata.",

    # ---------------------------------------------------------- :7011 <Norne> la guida
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :6998.
    (7011, 'It was developed for the purpose of breaking through every obstacle and sending equipment and troops to every location. Unlike the official model the dimensional distortion unit is completely built-in.'):
        "Una fata della stirpe degli Eln. Sa sparire a piacimento, e compare e scompare dove meno te lo aspetti. Un'infinità di avventurieri, ai tempi in cui muovevano i primi passi, si sono fatti guidare da lui; poi, senza accorgersene, smettono di vederlo.",

    # ---------------------------------------------------------- :7024 il Mara
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :7011.
    (7024, 'A kind of fairy called Erun. He can disappear at will and is omnipresent. A number of adventurers have been guided by him in his fledgling days but he says that at some point he will cease to be seen.'):
        "Un demone che ha la forma di un fungo. È l'incarnazione dei desideri terreni, e trama per confondere gli uomini e portarli alla rovina. Quando si eccita, dalla testa gli sprizza fuori un liquido sospetto e appiccicoso.",

    # ---------------------------------------------------------- :7037 il mortaio semovente di Yerles
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :7024.
    (7037, 'A demon with a mushroom-like form. It is the incarnation of suffering and schemes to deceive and corrupt people. When aroused a suspiciously squishy liquid gushes from its head.'):
        "Un veicolo che monta un mortaio pesante. È mobile, spara rapido e costa poco, e per questo lo producono in serie. Il difetto è la gittata corta, ma è pur sempre un mortaio. Di norma fa tutto da solo, però un posto per l'equipaggio ce l'ha.",

    # ---------------------------------------------------------- :7050 il lanciabombe
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :7037.
    (7050, 'The vehicle is equipped with a heavy mortar gun. It is mass-produced because of its superior mobility and rapid-fire capabilities and its low cost. A disadvantage of the mortar is that it has a short range. Basically it is fully automated but there is still space for passengers.'):
        "Era un lanciapietre. Passare dalla parte di chi le pietre le tira era stata una bella soddisfazione, se non che troppi se le prendevano in faccia senza scomporsi: si è arrabbiato, e ha cambiato le pietre con le granate.",

    # ---------------------------------------------------------- :7063 lo Yerleswood di serie
    # ⚠️⚠️ SOLO DAL GIAPPONESE: l'inglese qui e' quello di :7050, e il suo
    #     inglese proprio nel sorgente NON ESISTE — e' qui che monte si riallinea.
    (7063, 'He was a former Rock Thrower. He went around to the stone throwing side which was fine but he snapped at the fact that so many of them were unfazed by the stones he was throwing at them and switched to grenades.'):
        "Il modello di serie, costruito sui dati del primo prototipo. Per tenere bassi i costi gli hanno montato armi e corazze di tipo comune, e qualche sistema di bordo gliel'hanno proprio tolto.",

    # ---------------------------------------------------------- :7076 il drago della nebbia
    (7076, 'It has a steam turbine on its back that is integrated with its outer shell from which it ejects bullets at high speed. Once extinct and restored in the time of the Rehmido it was unable to recreate the sturdy outer shell that was considered invincible.'):
        "Sulla schiena porta una turbina a vapore fusa col guscio esterno, e da lì spara proiettili ad altissima velocità. Una volta si era estinto, e ai tempi di Rehm-Ido lo hanno riportato in vita; il guscio robusto che lo rendeva imbattibile, però, non sono riusciti a rifarlo.",

    # ---------------------------------------------------------- :7089 il drago tiranno furioso
    (7089, 'Ether-loving high ranking species of great dragons and dragon tyrants. The roar also makes the surrounding demons go berserk. It is frequently angry draining its strength and making it emaciated.'):
        "Ama l'etere, sta un gradino sopra i grandi draghi ed è il tiranno della sua stirpe. Il suo ruggito fa infuriare anche i mostri che gli stanno attorno. Siccome è arrabbiato praticamente sempre, consuma energia in continuazione ed è ridotto pelle e ossa.",

}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-014.jsonl'
DA, A = 6601, 7100
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
