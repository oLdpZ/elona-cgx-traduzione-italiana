# -*- coding: utf-8 -*-
"""116a - Lotto 043 di `db_item.hsp`: LE ARMI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_WEAPON`, righe da `:82945` a `:131182`: **34 righe** su 33 oggetti — 32
dell'indice 0, nessuna dell'indice 1 e 2 dell'indice 2. Con questo lotto
`FILTER_WEAPON` passa a **0 da fare su 110 vive**: e' la **quarta categoria
chiusa** del corpo dopo il mobilio (114a), gli attrezzi e gli scarti (115a), e
ci sono voluti tre lotti, dal 041 al 043, tutti nella stessa sessione.

⚠️ Come per il 037 e il 040, la coda di una categoria **non e' un intervallo
stretto**: le ultime 34 righe stanno sparse fra `:82945` e `:131182`, e ci e'
voluto `82000 200000`.

### ⭐⭐⭐ LA PREVISIONE DI `applica` SI E' FATTA CONTANDO, NON SPERANDO

Il 042 aveva chiuso con «previsione +35, misurato +36», e il colpevole era una
riga gemella che nessuna tabella nomina. La lezione si e' applicata **subito**,
prima di scrivere una sola resa: per ognuna delle 34 righe si e' contato quante
volte il suo giapponese compare nel sorgente pinnato.

    righe del lotto: 34   righe in piu' che applica tocchera': 0
    PREVISIONE applica: +34

⭐ E' una riga di script, e trasforma la previsione da speranza in misura. Va
fatta **ogni volta**, perche' la riga gemella non si vede ne' nel dossier ne'
nella tabella delle categorie: si vede solo nel sorgente.

### ⭐⭐⭐ LA GEMELLA DEL 042 SI E' RIEMPITA DA SOLA, E IL DOSSIER LO MOSTRA

`:126849` e' **Mournblade**, ed e' la riga che nel 042 aveva fatto salire
`applica` di uno in piu'. Nel dossier di questo lotto compare **gia' tradotta**,
con la resa scritta ieri per <Stormbringer>, e **non** e' fra le 34 righe da
fare: `_corpo.py` non la vede perche' non e' in `lavoro/_107-daitem.jsonl`.

⭐ E la coppia si legge tutta: l'indice 3 di Stormbringer dice «ha per gemella
Mournblade», quello di Mournblade dice «ha per gemella Stormbringer». Le due
prose sono la stessa perche' il giapponese e' lo stesso; i due indici 3 restano
distinti perche' il giapponese e' diverso. La firma ha fatto la cosa giusta.

### ⭐⭐⭐ L'INGLESE DELLA LANCIA E' QUELLO DEL BASTONE, COPIATO

`:116982` (長槍, la lancia) e `:117051` (杖, il bastone) portano lo **stesso
inglese, byte per byte**:

    A stick born to assist magic. Despite its everyday look, if you hit with
    it with all your might, your opponent will probably fall unconscious.

che e' la descrizione del **bastone**. Il giapponese della lancia dice tutt'altro
— 長い柄の先に尖った切っ先を持つ武器 — e l'indice 3 inglese della lancia e'
invece giusto («a polearm with a sharp point»). Quindi il difetto e' in una
riga sola del ramo inglese di monte, non in tutta la voce.

⭐ **Due giapponesi diversi fanno due firme diverse** (lezione della 115a):
le rese sono **due**, ciascuna scritta dal proprio giapponese, e chi gioca in
italiano vede la lancia descritta come una lancia — cosa che chi gioca in
inglese non vede.

⚠️⚠️ **PREVISIONE: `_coerenza` dira' «lo stesso INGLESE, rese diverse: 1».**
Non e' un guasto, e' il referto che si accende su questa coppia, ed e' atteso.
Se dicesse 0, vorrebbe dire che le due rese sono uguali, cioe' che abbiamo
copiato l'errore di monte.

### ⭐⭐ IL CANCELLO DEI TITOLI: LA PREVISIONE E' **6**, ANCORA INVARIATO

    ~Collection of Armaments...~   17 righe
    ~Irva Fantasy Encyclopedia~    15 righe  (gia' uno dei sei, per Aimwell)
    ~words of <Renton> the suffering wizard~   1 riga
    ~words of <Loyter> the crimson of Zanan~   1 riga

Nessuno di questi inglesi copre due giapponesi. E la domanda della 116a —
*questo titolo contraddice un nome gia' a schermo?* — e' stata fatta su tutt'e
quattro: <Renton> e <Loyter> sono nomi invariati, e «mago» e' la forma che il
dizionario usa per 魔術士.

### ⚠️ L'INGLESE ROVESCIA UNA FRASE, E STAVOLTA E' UNA PAROLA SOLA

`:127421` (<Diablos>): il giapponese dice che la lama nera scombina la mente di
**斬られた者**, «chi viene tagliato». L'inglese scrive «the spirit of the
cutter», cioe' **chi taglia** — il contrario. E' un rovesciamento come quelli
della 114a, e nessun cancello lo puo' vedere.

### ⓘ I CINQUE DONI DEGLI DEI, E PERCHE' NON C'ERA NIENTE DA DECIDERE

`:85642`, `:85714`, `:85785`, `:85857` e `:85927` sono i doni di Opatos, Ehekatl,
Jure, Itzpalt e Kumiromi, e ciascuna prosa nomina il proprio dio. I nomi **non
si sono scelti**: i cinque indici 3 di quegli stessi oggetti sono resi da tempo
e dicono gia' «il dio della terra», «la dea della fortuna», «la dea della
guarigione», «il dio degli elementi», «il dio del raccolto». Si sono copiati.

### ⓘ Due parole riscritte dal preflight, e una era la meno ovvia

    dell'oltretomba   15  -> «le fiamme che l'oltretomba manda» (12)
    un'organizzazione 17  -> «un gruppo di spie»

⚠️ La prima e' istruttiva: `dell'oltretomba` **esiste gia'** nel dizionario,
nell'indice 3 di quest'arma. Non e' un errore li': l'indice 3 **non si
impagina**, e la finestra di rinculo non lo riguarda. La stessa parola e'
legittima in un campo e troppo lunga nell'altro, e a saperlo e' il cancello,
non l'occhio.

### ⚠️ Un heredoc vuoto ha bloccato il terminale, per la settima volta

Scritto `python - << 'FINE'` con il corpo vuoto per saltare un passo. Due minuti
di terminale fermo, chiuso con `TaskStop`. E' esattamente il caso che i
documenti descrivono dalla 104a e che la 115a aveva gia' ripetuto. Le due
correzioni sono state fatte con lo strumento di modifica, che e' quello che la
regola dice di usare.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :82945
    (82945, 'Huge, unadorned silver cross-sword. The sword has no decoration except for a mysterious engraving on the blade, and its design, which is solely dedicated to cutting down the enemy, is breathtaking. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada a croce d'argento, enorme e senza ornamenti. A parte un'incisione misteriosa sulla lama non ha decorazione nessuna, e quella fattura, fatta solo per abbattere il nemico e nient'altro, mette perfino una specie di soggezione. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :84582
    (84582, 'A great red axe that looks as if it is painted with blood. The blow from it is said to pierce and shatter anything. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'ascia lunga rossa, come fosse imbrattata di sangue. Dicono che il colpo che ne esce passi e sbricioli qualunque cosa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85642
    (85642, 'Huge, heavy hammer with an imposing appearance. The figure wielding the hammer seems to be a manifestation of the God of Earth. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un martello enorme e pesante, di aspetto maestoso. Chi lo gira sembra il dio della terra che si mostra in carne e ossa. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85714
    (85714, 'Dagger carved out of mica, an ancient sign of good fortune. According to one theory, it was accidentally dropped to the mortal world by the Goddess of Fortune when she was cutting up a fish. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale ricavato scavando la mica, che fin dai tempi antichi è segno di fortuna. Secondo una versione, la dea della fortuna lo lasciò cadere per sbaglio sulla terra mentre puliva il pesce. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85785
    (85785, 'A holy spear, without a trace of shadow. Once you strike your enemy, you might have a glimpse of the power of the Goddess of Healing. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lancia sacra senza un'ombra addosso. Basta che tu infilzi il nemico una volta, e ci vedrai un frammento della forza della dea della guarigione. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85857
    (85857, 'Black staff decorated with three types of gemstones. Each gemstone is said to symbolize an element, which dramatically increases the magic power of the wielder. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un bastone nero ornato di tre specie di pietre preziose. Ciascuna pietra è il simbolo di un elemento, e dicono che facciano crescere di colpo la forza magica di chi lo maneggia. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :85927
    (85927, "There are probably no farmers who doen't know this fairy tale. In the past, when there was no harvest due to continuous drought, this appeared out of nowhere and the surrounding area was covered with greenery eventually. \\n# ~Irva Fantasy Encyclopedia~"):
        "Fra chi lavora la terra non c'è nessuno che non conosca questa favola. Ai tempi in cui la siccità non finiva e il raccolto non veniva, quella comparve da chissà dove, e poi tutt'intorno si coprì di verde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107252
    (107252, 'This amazing spear is said to have been forged in the flames of the netherworld. It is said that as it is forged, the spear gradually absorbs the power of hell, and when wielded, opens the gates of hell. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una lancia prodigiosa che, si dice, fu forgiata con le fiamme che l'oltretomba manda. Forgiandola, si è bevuta a poco a poco la forza che l'oltretomba dà; e dicono che, a girarla, apra le porte che l'oltretomba tiene chiuse. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107324
    (107324, 'It is said that only those who have fallen into darkness are qualified to hold this staff. It is said to contain the souls of its past owners, which often come back to haunt them in nightmares when they attack. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un bastone che, dicono, solo chi è caduto nelle tenebre ha il diritto di impugnare. Dentro ci starebbero chiuse le anime di chi lo ha posseduto prima, e quando colpisce spesso quelle piombano addosso al nemico come un incubo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :107326
    (107326, '\\"I heard that in the past, the staff was in the hands of a mage who wished to destroy himself. At the time, I laughed at what a foolish person he was, but now I think I understand somewhat how he felt. He must have lost too much.\\" \\n# ~words of <Renton> the suffering wizard~'):
        "\\\"Ho sentito dire che è il bastone che, tanto tempo fa, tenne in mano un mago che voleva la propria rovina. Allora ridevo, e pensavo che uomini sciocchi ci fossero al mondo; adesso invece mi pare quasi di capire come si sentiva. Anche lui avrà perso troppo.\\\" \\n# ~Parole di <Renton> il mago tormentato~",

    # ---------------------------------------------------------- :107460
    (107460, 'A club with an iron ball attached to it that looks like a bloody full moon. The sphere is said to be enchanted to absorb the spirit of the opponent and convert its energy into flames. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un randello con attaccata una palla di ferro che pare una luna piena imbrattata di sangue. Sulla sfera, dicono, sta un incantesimo che assorbe lo spirito del nemico e ne rende la forza in fiamme. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :113386
    (113386, "This is a shortsword used by an intelligence organization that grew up in secrecy in a foreign land, and is processed to fit comfortably in one's hand. The blade is said to be dyed black so that it does not reflect light. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una spada corta che usa un gruppo di spie cresciuto in segreto in un paese straniero: è piuttosto piccola, ma lavorata per stare bene in mano. La lama, dicono, è tinta di nero perché non rifletta la luce. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115521
    (115521, 'A spear that can be used in a variety of fighting styles such as slashing, thrusting, and striking all by itself. In ancient times, when people were constantly fighting each other, this weapon was used by various races as well as its usage. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una lancia che da sola permette di combattere in molti modi: taglia, punge e batte. Nei tempi antichi, quando gli uomini non smettevano mai di combattersi, quest'arma la usavano razze diverse, tante quante erano i suoi usi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115589
    (115589, 'An axe with a blade larger than a battle-axe. It even looks like a wide sword attached to a long pole, but because of its weight, it is mainly used for smashing rather than slashing. It can also be used for felling trees. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia con una lama ancora più grande di quella dell'ascia da battaglia. Ormai pare quasi una spada larga infilata in cima a un palo lungo, ma per via del peso pare che si usi più per schiacciare che per tagliare. Serve anche ad abbattere gli alberi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115720
    (115720, 'A huge sword designed to be handled with both hands. Although heavy, it is a sharp weapon whose purpose is not to crush the enemy with its weight, but to cut them down. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada enorme, fatta perché si maneggi a due mani. Pesa, ma non è affatto un'arma che schiaccia il nemico lasciando fare al peso: taglia bene, ed è fatta per recidere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115941
    (115941, 'A stick with a considerable length. It has no blades, so its lethality is low, but because of its lightness, it is often wielded or used as a medium to put magic power into. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone di una certa lunghezza. Non ha lame, quindi uccide poco; ma è leggero, e per questo spesso lo si gira in mano o lo si usa come tramite in cui mettere la forza magica. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116010
    (116010, 'The spear originally invented to catch fish. The three-parted end of the handle makes it easier to hit an opponent, and it is also thought to have the effect of delaying healing due to wounds inflicted in close proximity. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una lancia pensata all'origine per prendere il pesce. La punta del manico si divide in tre, e questo la rende più facile da mandare a segno; e pare che sia stato studiato anche l'effetto di ritardare la guarigione, con le ferite prese così da vicino. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116078
    (116078, "A large hammer, fashioned from a blacksmith's hammer for use in battle. The blow struck from the tip of a large hammer is said to crush any enemy. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un martello grande, ricavato da quello del fabbro e lavorato per il combattimento. Dicono che il colpo, calato da un braccio alzato per bene, schiacci qualunque nemico. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116146
    (116146, 'Axes developed for combat use. The blade is larger and heavier, so it must be handled with both hands. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia sviluppata per il combattimento. Anche la lama è fatta piuttosto grande, e questo ne ha aumentato il peso: alla fine bisogna per forza maneggiarla a due mani. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116215
    (116215, 'A double-edged sword used by the bandit groups that plague the seas. It is made to be easy to handle on the battlefield, with a rather small blade and a broad hilt to defend against swords. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada a doppio taglio che usano le bande di predoni che infestano il mare. Perché stia bene in mano anche in battaglia, ha la lama piuttosto piccola e larga di costa, così da poter parare le spade. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116282
    (116282, "Longswords said to have been favored by exotic fighting groups. It has a unique curve, and each is said to have a unique design and bears the swordsmith's soul. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una spada lunga che, dicono, i gruppi di guerrieri di un paese straniero preferivano a ogni altra. Ha una curva tutta sua, e dicono che in ognuna stiano chiusi una firma tutta sua e l'anima del fabbro che l'ha battuta. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :116982
    (116982, 'A stick born to assist magic. Despite its everyday look, if you hit with it with all your might, your opponent will probably fall unconscious. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma con la punta acuminata in cima a un manico lungo. Ha una struttura semplice e la può usare chiunque, e il manico lungo permette di combattere a mezza distanza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117051
    (117051, 'A stick born to assist magic. Despite its everyday look, if you hit with it with all your might, your opponent will probably fall unconscious. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un bastone nato per dare una mano alla magia. A vederlo non lo chiameresti un'arma, eppure, se ci batti con tutta la forza, probabilmente il nemico va giù svenuto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117119
    (117119, 'Originally, this weapon was used to cut grass. On the battlefield, this weapon is used to hunt for heads and is considered an object of fear. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arnese che serve, di suo, a tagliare l'erba e simili. Sul campo di battaglia lo si usa per mietere teste, e per questo fa paura. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117460
    (117460, 'Dagger made from an unknown mineral. It is said to be extremely light, and the quick sword flashes from it look as if they are swinging a cord. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pugnale fatto con un minerale sconosciuto. È leggerissimo, e dicono che i lampi rapidi della lama sembrino un nastro che si gira in aria. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :126221
    (126221, 'A long sword that was said to have been quietly stuck in a small hill. How many enemies has the black blade slaughtered? The sword does not speak silently. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una spada lunga che, dicono, stava piantata in silenzio su una collinetta. Quanti nemici avrà macellato quella lama nera? La spada tace e non risponde. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :126918
    (126918, 'A scythe with multiple layers of enhancement magic. It was said to strengthen the magic of the wielder and bring him closer to the ultimate existence, but it has long since been lost to the world. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una falce su cui sono stati stesi strati e strati di incantesimi di rinforzo. Dicevano che rafforzasse la magia di chi la maneggia e lo avvicinasse all'essere supremo, ma è sparita dal mondo da moltissimo tempo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127349
    (127349, 'It is said that there is nothing in this world that cannot be cut. As rumor has it, it can cut through anything, but it is said to be unable to cut through only gray food, which is rich in elasticity. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un miracolo di lama, di cui si canta che a questo mondo non c'è cosa che non tagli. Come dice la voce, passa qualunque cosa; ma a quel che raccontano, l'unica che non riesce a tagliare è un cibo grigio e pieno di elasticità. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127421
    (127421, "This is a breathtaking sword bearing the name 'Diablos'. It is said that its black blade disrupts not only the spirit of the cutter, but even the flow of time. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una spada che incute timore e porta il nome di \\\"demone\\\". Dicono che la sua lama nera scombini non soltanto la mente di chi viene tagliato, ma perfino lo scorrere del tempo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127423
    (127423, '\\"I have heard about that weapon. I have heard that it is a sword born of a black dragon that harbors evil, and that its cutting blade cuts through time. I don\'t know if this is true or not, but if it is, I would love to see it. It may be a weapon worthy of my power.\\" \\n# ~words of <Loyter> the crimson of Zanan~'):
        "\\\"Di quell'arma ho sentito parlare. Sarebbe una spada nata da un drago nero che porta sventura, e la sua lama taglierebbe perfino il tempo. Non so se sia vero, ma se lo è mi piacerebbe proprio vederla. Potrebbe essere un'arma degna della mia forza.\\\" \\n# ~Parole di <Loyter> l'eroe cremisi di Zanan~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :130977
    (130977, 'A simple weapon designed for striking. It is very simple to make and use, and many adventurers are said to be its favorite users. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma semplice, fatta per picchiare. Il modo di farla e quello di usarla sono tutt'e due semplicissimi, e per questo dicono che anche fra chi va all'avventura ci sia chi non la lascia mai. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131045
    (131045, 'Axe light enough to be handled with one hand. It is more of an everyday tool than a weapon, but its lightness makes it versatile enough to be used like a club. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'ascia fatta leggera perché si maneggi con una mano sola. Nella fattura si sente ancora forte il lato di ogni giorno, spaccare la legna più che combattere; ma è leggera, e per questo è buona a tutto: si può usare anche come un randello. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131114
    (131114, 'Originating from an ancient domain, it is a short and light sword that can be easily handled with one hand. Its simple shape is still in use today. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada corta e leggera, nata presso un clan antico, fatta per maneggiarsi facile anche con una mano sola. La sua forma semplice è arrivata fino a oggi senza cambiare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :131182
    (131182, 'A sword with a long blade, widely used for killing. The variety of these swords is said to be still evolving. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una spada dalla lama lunga, fatta in generale per tagliare. Dicono che le sue varietà, che sono tantissime, continuino a evolversi ancora adesso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 32 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-043.jsonl'
RIGHE = {
    82945, 84582, 85642, 85714, 85785, 85857, 85927, 107252, 107324, 107326,
    107460, 113386, 115521, 115589, 115720, 115941, 116010, 116078, 116146, 116215,
    116282, 116982, 117051, 117119, 117460, 126221, 126918, 127349, 127421, 127423,
    130977, 131045, 131114, 131182,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
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
