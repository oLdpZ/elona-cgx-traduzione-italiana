# -*- coding: utf-8 -*-
"""106a - Lotto 26 di `db_card.hsp`: le carte fra la riga 12601 e la 13100 (39).

⚠️⚠️ **`:12733` E' LA TRAPPOLA DELLA 105a, RIPRESENTATA IDENTICA.** Il giapponese
dice **レム・イド時代**, cioe' l'epoca di **Rehm-Ido**, e l'inglese scrive
`during the Remido era`. `Remido` (レミード) sono le **rovine**; `レム・イド` e'
la **civilta'** — il glossario della 104a lo dice, e nella 105a mi ero fermato a
«frammento di Rehmido» nel dizionario, che e' indicizzato sull'inglese. Qui la
resa dice **Rehm-Ido**, letta dal giapponese.

⚠️ **DODICI carte hanno l'inglese che finisce con uno SPAZIO**: `:12681`,
`:12694`, `:12720`, `:12759`, `:12824`, `:12863`, `:12967`, `:12993`, `:13006`,
`:13019`, `:13032`, `:13084`.

⚠️⚠️ **QUATTRO CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**

    :12876  半人半鳥の**姦しい**魔物   姦しい e' «chiassoso», dai tre 女 del kanji;
                                       l'inglese legge `fornicating` e cambia la
                                       carta di registro
    :12785  死と**悪阻**を撒き散らす    悪阻 e' la **nausea**, e Elona ce l'ha come
                                       stato; l'inglese scrive `malice`
    :12811  **蛇とのコンビネーション**   la combinazione e' fra la creatura e i suoi
                                       serpenti; l'inglese scrive `the combination
                                       of the snakes and the snakes`
    :12720  別名は**ハイイログマ**      e' l'orso grigio; l'inglese traslittera
                                       `the hylog bear`, che non vuol dire niente

⭐ **Sei carte aprono con la STESSA formula, e si scrivono uguali.**
エーテルを好む、竜族の一種 apre `:12889`, `:12902`, `:12915`, `:12928`, `:12941`
e `:12954`: «Una specie della stirpe dei draghi, con un debole per l'etere».
ⓘ E si tiene il «debole per l'etere» gia' usato a `:9767` nel lotto 19 per
エーテルを好む del gran drago. ⚠️ Nessuna rete lo pretende: i giapponesi interi
sono diversi, quindi la coerenza qui e' a carico di chi scrive.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `レム・イド` → **Rehm-Ido**,
`ブレス` → **il soffio**, `エーテル` → **l'etere**, `ネフィア` → **le Nefia**,
`冥界` → **l'oltretomba**, `ケルベロス` → **il Cerbero** (`:12967` e' la sua
carta, e il segugio dell'oltretomba del lotto 25 dice che sono due specie
diverse), `トロール` → **il troll**, `インド象` → **l'elefante indiano**
(`:12993`, e qui sta nel giapponese).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :12603 <Tuwen> il signore della piramide
    (12603, 'An ancient king who lives in this world until the forbidden arts turn him into a living corpse. He occasionally lures dumb grave robbers with invitations and replenishes the soldiers guarding the pyramids.'):
        "Un re antico che, per restare a vivere in questo mondo, con un'arte proibita si è ridotto a cadavere che cammina. Ogni tanto attira con un invito qualche sciocco che saccheggia le rovine, e così rimpiazza i soldati che sorvegliano la piramide.",

    # ---------------------------------------------------------- :12616 il sarcofago antico
    (12616, 'The end result of a civilisation that flourished in ancient times, where noblemen were placed as dummies around a coffin in which they were enshrined. The corpse in which they were placed has fused with the coffin.'):
        "Quel che resta dei sarcofagi che, in una civiltà fiorita nell'antichità, venivano messi come esca intorno a quello dove riposavano i nobili. Il cadavere che ci avevano messo dentro si è fuso con il sarcofago.",

    # ---------------------------------------------------------- :12629 il goblin
    (12629, 'Goblins attack people in swarms. They speak their own language and have established an underground goblin-only society. Although they do not speak the same language as trolls, they seem to get on well with them.'):
        "Un piccolo essere che assale gli uomini in gruppo. Parlano una lingua tutta loro e sottoterra si sono costruiti una società di soli goblin. Con i troll non si capiscono a parole, eppure pare che vadano d'accordo e stiano in buoni rapporti.",

    # ---------------------------------------------------------- :12642 il goblin guerriero
    (12642, 'Trained in melee combat among the goblin tribe. He uses his eye of mind to accurately aim for the vital spot, and his muscular body shows more strength than it appears.'):
        "Fra i goblin, quelli che si sono addestrati al corpo a corpo. Con l'occhio della mente punta il punto debole con precisione, e quel corpo tutto muscoli tira fuori più forza di quanta ne dia a vedere.",

    # ---------------------------------------------------------- :12655 il goblin sciamano
    (12655, 'Goblin tribe sorcerer. When this monster was discovered, the world was astonished to learn that goblins also had a practice of believing in spirits and gods. It was later discovered that they were, in a manner of speaking, imitating the humans.'):
        "Lo stregone della stirpe dei goblin. Quando questo mostro fu scoperto, il mondo restò sbalordito che anche i goblin avessero l'usanza di venerare gli spiriti e le divinità. Poi si scoprì che, in fondo, non facevano che scimmiottare gli uomini.",

    # ---------------------------------------------------------- :12668 il goblin mago
    (12668, 'A goblin tribe member who is skilled in magic. He is a simple but powerful man behind the scenes who uses magic arrows to hunt down his prey with confidence. He seems to have a nose to taking advantage of his magical abilities.'):
        "Fra i goblin, quello portato per la forza magica. Senza dare nell'occhio mette la preda alle strette con la freccia magica, un colpo dopo l'altro: è la forza che lavora dietro le quinte. Pare che di saper usare la magia se ne vanti un po' troppo.",

    # ---------------------------------------------------------- :12681 il battezzatore rosso
    (12681, 'A person who has become fascinated by and worships the red devil, which is now sealed away somewhere. His face, hidden by his dressing gown, is so burnt that it has lost all trace of its original appearance. '):
        "Uno a cui il demone rosso, che adesso dicono sigillato da qualche parte, ha rapito il cuore e che ha finito per adorarlo. Il volto nascosto sotto la veste è bruciato al punto da non conservare più niente della forma di prima. ",

    # ---------------------------------------------------------- :12694 il battezzatore blu
    (12694, 'A person who has become enthralled by and worships the blue devil, which is now sealed away somewhere. His face, hidden by a dressing gown, is horribly frozen and his eyeballs are entirely clouded with blue. '):
        "Uno a cui il demone blu, che adesso dicono sigillato da qualche parte, ha rapito il cuore e che ha finito per adorarlo. Il volto nascosto sotto la veste è congelato in modo orribile, e il bulbo degli occhi è tutto torbido di azzurro. ",

    # ---------------------------------------------------------- :12707 l'orso bruno
    (12707, 'A bear that has been tamed by people. They learn tricks, but few are given the opportunity to perform them. Those that are abandoned become wild and attack people in packs.'):
        "Un orso addomesticato dagli uomini. Impara anche i numeri da spettacolo, ma pochi hanno l'occasione di mostrarli. Quelli che vengono abbandonati tornano selvatici e assalgono la gente in branco.",

    # ---------------------------------------------------------- :12720 il grizzly
    (12720, 'A rabid bear that particularly likes to attack humans. It is also known as the hylog bear, and as its name suggests, its body hair is grey, but occasionally some individuals seem to have their fur stained red by returned blood. '):
        "Un orso feroce che ha una particolare preferenza per gli uomini. L'altro suo nome è orso grigio, e come dice il nome ha il pelo grigio, ma ogni tanto pare ci sia qualche esemplare che ce l'ha tinto di rosso dal sangue schizzato addosso. ",

    # ---------------------------------------------------------- :12733 il mammut
    (12733, 'A super-ancient creature that is believed to have been revived by genetic restoration technology during the Remido era. Its meat has fed humans since ancient times. Even today, mammoth meat is considered a delicacy.'):
        "Una creatura antichissima che, dicono, fu riportata in vita al tempo di Rehm-Ido con la tecnica che ricostruisce i geni. La sua carne è stata cibo per gli uomini fin dai tempi remoti, e ancora oggi la carne di mammut è considerata una leccornia.",

    # ---------------------------------------------------------- :12746 l'armatura vivente
    (12746, 'The remorse of the dead warriors began to wander about in their cast-off armour. Unless someone destroys them, they continue to search for the enemy they could not defeat. They are not satisfied because they are empty inside.'):
        "Il rimpianto di un guerriero caduto si è annidato nell'armatura buttata via e ha cominciato a vagare. Se qualcuno non la distrugge continua a cercare il nemico che non è riuscita a battere. Sarà perché dentro è vuota, ma non si sente mai sazia.",

    # ---------------------------------------------------------- :12759 la massa d'acciaio
    (12759, 'The evil spirit of the dead warrior has taken over the masterless heavy-layered armour and has run amok, regarding everything that lives as an enemy. After being vanquished, they will continue to wander in search of the next vessel. '):
        "Il pensiero malvagio di un guerriero caduto è passato in un'armatura pesante rimasta senza padrone e si è scatenato, prendendo per nemico tutto quello che vive. Anche dopo essere stata abbattuta continuerà a vagare in cerca del prossimo contenitore. ",

    # ---------------------------------------------------------- :12772 l'armatura dorata
    (12772, 'A beautiful armour, projected with the thoughts of ancient heroes. It keeps running, drowning in the joys of battle, until it meets the owner of a power that surpasses its own. It is not made of gold, so its value as an armour is not that high.'):
        "Una bellissima armatura in cui si è proiettato il pensiero di un eroe antico. Corre e corre, ubriaca del piacere della battaglia, finché non incontra qualcuno con una forza che supera la sua. D'oro però non è fatta, e come armatura non vale poi molto.",

    # ---------------------------------------------------------- :12785 l'armatura della morte
    (12785, 'Armour attached to the grudge of an evil knight who died an untimely death and decayed without burial. It spreads death and malice on impulse. Do not wear it by mistake.'):
        "Un'armatura in cui si è annidato il rancore di un cavaliere malvagio, morto di una morte ingiusta e marcito senza sepoltura. Sparge morte e nausea seguendo l'impulso. Guai a indossarla, nemmeno per sbaglio.",

    # ---------------------------------------------------------- :12798 la medusa
    (12798, 'They have snake hair. Their ancestors had the power to turn what they saw into stone, but it was so inconvenient in their daily lives that the power degenerated over the generations. Now it only temporarily stiffens the opponent.'):
        "Ha serpenti al posto dei capelli. Gli antenati avevano il potere di trasformare in pietra quello che guardavano, ma nella vita di tutti i giorni era così scomodo che di generazione in generazione il potere si è ridotto. Adesso irrigidisce l'avversario, e solo per un poco.",

    # ---------------------------------------------------------- :12811 l'euriale
    (12811, 'Each one of these snakes-hair, is self-aware and has occasionally been seen fighting with the main body. During the moult season, their heads become amazing. The combination of the snakes and the snakes is used to disorientate the opponent.'):
        "I serpenti che le fanno da capelli hanno ciascuno una coscienza sua, e li si è visti più volte litigare con la padrona. Nella stagione della muta la testa diventa uno spettacolo. Confonde l'avversario giocando in combinazione con i suoi serpenti.",

    # ---------------------------------------------------------- :12824 la stenno
    (12824, 'When she protested against seeing her sister turned into a monster by the wrath of God, she was turned into a monster along with her other sister. This is one of her descendants. '):
        "C'era una donna che, vedendo la sorella trasformata in mostro dall'ira del dio, protestò, e per questo fu trasformata in mostro anche lei insieme all'altra sorella. Questa è una delle sue discendenti. ",

    # ---------------------------------------------------------- :12837 il cupido dell'amore
    (12837, 'A monster that has gained the power of some love god. When pierced by its arrows, it falls in love and loses the words it should speak. He is quite a screw-up and sometimes accidentally shoots his target dead by releasing an ordinary arrow.'):
        "Un mostro che ha ottenuto la forza di un qualche dio dell'amore. Chi viene trafitto da quelle frecce si innamora e perde le parole che dovrebbe dire. È parecchio imbranato, e ogni tanto scocca una freccia normale e ammazza il bersaglio per sbaglio.",

    # ---------------------------------------------------------- :12850 il fantasma minore
    (12850, 'Armour in which ghosts dwell and move. It keeps muttering curses against the living. Because it has taken up residence in interior armour, it is surprisingly fragile.'):
        "Un'armatura in cui si è annidato uno spettro e che ha cominciato a muoversi. Continua a mormorare parole di maledizione contro chi è vivo. Siccome si è annidato in un'armatura da arredamento, è sorprendentemente fragile.",

    # ---------------------------------------------------------- :12863 il tirannosauro
    (12863, 'Dinosaurs are a species that died out in prehistoric times but were apparently restored by the genetic technology of an old civilisation. They are said to have been powerful and highly agile, and to have preyed on other dinosaurs. '):
        "I dinosauri sono una stirpe estinta in tempi remotissimi, ma pare che la tecnica genetica della vecchia civiltà li abbia ricostruiti. Aveva forza e grande agilità, e si dice che predasse gli altri dinosauri. ",

    # ---------------------------------------------------------- :12876 l'arpia
    (12876, 'A half-human, half-bird, fornicating monster. Instead of arms, they have bird wings, but they are not as agile as they appear. It was fashionable to use its wings as broomsticks, but this is now prohibited by law.'):
        "Un mostro chiassoso, mezzo uomo e mezzo uccello. Al posto delle braccia ha ali da uccello, ma non è agile quanto sembra. Un tempo andava di moda farne scope con le penne, ma adesso la legge lo vieta.",

    # ---------------------------------------------------------- :12889 il drago verde
    (12889, 'A type of dragon tribe with a fondness for the ether. They are less aggressive than other dragons, but their breath is very powerful and they cannot be underestimated. They are omnivorous but often eat grass.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. È meno aggressivo degli altri draghi, ma il suo soffio è potentissimo e non lo si può prendere alla leggera. È onnivoro, ma mangia spesso erba.",

    # ---------------------------------------------------------- :12902 il drago rosso
    (12902, 'A type of dragon tribe with a fondness for the ether. They have a flammable gas-producing organ in their bodies called a flaming sac. Many individuals inadvertently burn their nests with the flames they exhale.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. Nel corpo ha un organo che produce un gas infiammabile, chiamato sacca di fuoco. Non sono pochi quelli che, senza volerlo, con la fiamma che sputano si bruciano il nido.",

    # ---------------------------------------------------------- :12915 il drago bianco
    (12915, 'A type of dragon tribe with a fondness for the ether. They have organs filled with refrigerant, which take heat from the air they inhale and convert it into cold air. As a result, their body temperature is actually higher than that of other dragons.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. Ha un organo pieno di refrigerante, che toglie il calore all'aria che respira e la trasforma in gelo. Per questo, a conti fatti, ha una temperatura del corpo più alta degli altri draghi.",

    # ---------------------------------------------------------- :12928 il drago elettrico
    (12928, 'A type of dragon tribe with a fondness for the ether. They have an organ in their bodies called an electric bag that produces static electricity, which they discharge from their mouths during battle. When they run out of electricity, they go out of their way to be struck by lightning.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. Nel corpo ha un organo che genera elettricità statica, chiamato sacca elettrica, e in battaglia scarica dalla bocca. Quando finisce l'elettricità va apposta a farsi colpire da un fulmine.",

    # ---------------------------------------------------------- :12941 il drago dell'oltretomba
    (12941, 'A type of dragon tribe with a fondness for the ether. Their breath contains magical powers and robs the living of their life force. How they come from the underworld is still unknown.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. Il suo alito contiene forza magica e ruba ai vivi la forza vitale. Come faccia ad arrivare dall'oltretomba non si sa ancora.",

    # ---------------------------------------------------------- :12954 il drago del caos
    (12954, 'A type of dragon tribe with a fondness for the ether. It has various energy sacks fused together and breathes chaos breath from its mouth. They have no likes or dislikes and eat everything well, so they may be easy to breed.'):
        "Una specie della stirpe dei draghi, con un debole per l'etere. Ha diverse sacche di energia fuse insieme, e dalla bocca sputa un soffio di caos. Non ha gusti difficili e mangia di tutto con appetito: forse è facile da allevare.",

    # ---------------------------------------------------------- :12967 il Cerbero
    (12967, 'A beast with three heads. Each head sleeps in turn, but the fire-breathing head is on strike and lazy, so the head that breathes magical breath has been working hard recently. '):
        "Una bestia con tre teste. Le teste dormono a turno, ma quella che sputa fuoco è in sciopero e batte la fiacca, e così ultimamente tocca darsi da fare a quella che sputa il soffio magico. ",

    # ---------------------------------------------------------- :12980 lo scorpione
    (12980, 'An arthropod characterised by a large tail with needles. They look fearsome but are not very poisonous and their shells are surprisingly soft. They are also used as food, as they are said to be quite tasty.'):
        "Un artropode che si riconosce per la coda grossa con il pungiglione. All'aspetto fa paura, ma il veleno non è poi così forte e anche il guscio è sorprendentemente morbido. Dicono sia parecchio buono, e infatti lo si mangia.",

    # ---------------------------------------------------------- :12993 lo scorpione re
    (12993, 'Although large in size, they are not very strong, so hunting is still dependent on poison. More than half of its body has been converted into poison-producing organs, and its venom can easily poison an Indian elephant. '):
        "Il corpo è grande, ma la forza non è granché, e per cacciare si affida come sempre al veleno. Più di metà del corpo l'ha convertito in organi che producono veleno, e quel veleno avvelena senza fatica perfino un elefante indiano. ",

    # ---------------------------------------------------------- :13006 il ragno
    (13006, 'Its mottled body is poisonous and alarming, but despite its appearance it is not poisonous. It uses threads to entangle its prey and feed on them. '):
        "Il corpo screziato ha colori che sembrano velenosi e mettono in guardia, ma a dispetto dell'aspetto veleno non ne ha. Impiglia la preda nei fili e se la mangia. ",

    # ---------------------------------------------------------- :13019 la vedova nera
    (13019, 'Many associate them with women because of their slender, shiny, black limbs, which are among the most slender of spiders. This may be partly due to the fact that they carry dangerous hidden venom. '):
        "Fra i ragni è di corporatura sottile, e in molti, guardando quelle zampe nere e lucide, pensano a una donna. Forse ci mette del suo anche il fatto che nasconda un veleno pericoloso. ",

    # ---------------------------------------------------------- :13032 il paralizzatore
    (13032, 'A spider with a venom that acts on nerves. When it finds prey, it first pours paralysing venom into it and then shaves the immobilised parts into small pieces for easier eating later. '):
        "Un ragno che ha un veleno che agisce sui nervi. Quando trova una preda le versa dentro per prima cosa il veleno paralizzante, e poi la sminuzza dove non si muove più, così da mangiarla comoda in seguito. ",

    # ---------------------------------------------------------- :13045 la tarantola
    (13045, 'It is so well known that it is probably the first thing people associate with poisonous spiders. They are rarely described as being surprisingly adorable looking. They may or may not be bothered by their bristly hair.'):
        "È tanto famosa che, a dire ragno velenoso, è la prima a cui si pensa. Di rado c'è perfino chi la descrive come sorprendentemente graziosa. Che poi ci tenga o no ad avere il pelo ispido, non si sa.",

    # ---------------------------------------------------------- :13058 il ragno di sangue
    (13058, 'A peculiar species of spider that likes to consume the blood of living creatures. It uses its threads to suck up the bodily fluids of its prey until it dries up. If there is a wrinkled corpse of a creature, it is probably the work of this one.'):
        "Una specie particolare che si nutre volentieri del sangue delle creature vive. Con i fili cattura la preda e le succhia i liquidi del corpo finché non si secca. Se trovi il cadavere raggrinzito di una bestia, è opera sua.",

    # ---------------------------------------------------------- :13071 il golem di legno
    (13071, 'They have the body of a tree. In past literature, they are described as beings who follow the orders of their creator, but whose orders are they protecting Nefia?'):
        "Ha un corpo d'albero. Nei testi antichi si legge che obbedisce agli ordini di chi l'ha costruito, ma per ordine di chi starà a fare la guardia alle Nefia?",

    # ---------------------------------------------------------- :13084 il golem di pietra
    (13084, 'It is said that erasing the writing on its forehead in an foreign language will stop its function, but there would be very little time to aim for such an object if confronted properly. '):
        "Si dice che cancellandogli dalla fronte i caratteri scritti in una lingua straniera se ne fermi la funzione, ma trovandoselo davvero davanti non ci sarà proprio il tempo di mirare a una cosa del genere. ",

    # ---------------------------------------------------------- :13097 il golem d'acciaio
    (13097, 'They have a wrought iron physique. The material used to make it is robust because it is designed for frequent combat, and it has a high level of combat ability to match. Its weaknesses are its joints.'):
        "Ha un corpo di ferro battuto. Il materiale l'hanno fatto robusto perché è pensato per combattere spesso, e in effetti ha una capacità di combattimento all'altezza. Il punto debole sono le giunture.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-026.jsonl'
DA, A = 12601, 13100
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
