# -*- coding: utf-8 -*-
"""106a - Lotto 19 di `db_card.hsp`: le carte fra la riga 9101 e la 9600 (39).

⚠️⚠️ **VENTITRE carte su trentanove hanno l'inglese che finisce con uno SPAZIO**,
e la resa deve finire con lo spazio anche lei (`verifica` lo pretende): `:9104`,
`:9117`, `:9130`, `:9143`, `:9195`, `:9247`, `:9286`, `:9299`, `:9325`, `:9338`,
`:9351`, `:9364`, `:9377`, `:9442`, `:9468`, `:9494`, `:9507`, `:9520`, `:9533`,
`:9546`, `:9559`, `:9572`, `:9598`. ⓘ Guardato PRIMA di scrivere, come insegna
il lotto 18: e' una proprieta' del blocco, non la svista di una riga.

⭐⭐ **`:9351` — DUE GIAPPONESI DIVERSI CADONO SULLA STESSA RESA ITALIANA, E LA
CARTA SI CONTRADDICE.** La carta del dragonewt dice 屈強な竜人の戦士…下級戦士の
リザードマンと間違われる事をとても嫌う, cioe' «guerriero 竜人 … detesta essere
scambiato per un リザードマン di rango inferiore». Ma nel progetto:

    竜人        la RAZZA (`dbidn:911`, inglese `lizardman`)  ->  «Uomo lucertola»
    リザードマン  la CREATURA (`db_card:11634`)                 ->  «l'uomo lucertola»

e quattro carte gia' rese scrivono 竜人 «uomo lucertola» nella prosa (`:4255`,
`:4281`, `:4294`, `:4320`). Applicando il precedente, questa carta direbbe «un
guerriero uomo lucertola … detesta essere scambiato per un uomo lucertola»: vera
parola per parola e falsa come frase. ✅ Qui 竜人 si rende col **nome della
creatura stessa**, «dragonewt» — che il progetto usa gia' per 超竜人 → «il
dragonewt supremo» (`db_card:7524`) — e リザードマン resta «uomo lucertola».
⚠️ Nessuna rete poteva vederlo: la rete 3 confronta i **giapponesi interi**, e
qui i giapponesi sono diversi; la rete 4 guarda dentro il lotto. L'ha trovato la
lettura del dizionario prima di scrivere, come le quattro della 105a.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `イルヴァ` → **Irva**
(`chat.hsp:2238`; ⚠️ l'inglese di `:9143` scrive `Ylva` e quello di `:9130`
`Irva`, e si traduce dal giapponese), `サウスティリス` → **Tyris del Sud**
(`chat.hsp:9247`), `ネフィア` → **Nefia**, femminile e numerabile — «le antiche
rovine chiamate Nefia», `chat.hsp:1751` —, `地殻変動` → **i movimenti della
crosta** (stessa voce), `レム・イド` → **Rehm-Ido** (glossario della 104a, ⚠️
**non** `Remido`, che sono le rovine: e' uno dei quattro sbagli della 105a),
`メサイア` → **Messia** (`chat.hsp:10237`), `エルシアの民` → **popolo di Elsia**
(`chara.hsp:2793`), `ガイアス・ヴィス` → **Gaius Vis** (`chat.hsp:7683`),
`黄泉の谷` → **la Valle degli Inferi** (`chat.hsp:8134`), `モンスターボール` →
**la sfera dei mostri** (`db_item.hsp:143296`), `リッチ` → **il lich**
(`invariati.md`), `トロール` → **il troll**, `ハーピー` → **l'arpia**,
`スライム` → **la melma**, `妖精` → **la fata**, `機械文明` → **la civilta'
meccanica** e `自律回路` → **i circuiti autonomi** (`db_card:3358`, `:3410`),
`ブレス` → **il soffio** (`db_card:8220`), `悪魔` → **il demone**, `魔物` → **il
mostro** (`db_card:7765`).

ⓘ **Coniati qui:** `冥王` → **il signore dell'oltretomba** (`:9325`, hapax come
persona; il progetto ha gia' 冥王の咆哮 → «ruggito dell'oltretomba»,
`skill.hsp:814`), `不死鳥` → **l'araba fenice** e `鳳凰` → **la fenice
d'oriente** (`:9260`: ⚠️ l'inglese le appiattisce tutt'e due su `phoenixes and
phoenixes`, e il senso della carta e' proprio che sono due uccelli diversi).

⚠️⚠️ **DUE CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**
`:9338` dice 人間の腕程度なら輪切りに出来てしまう — «un braccio d'uomo» — e
l'inglese scrive `a Indian Elephant`; `:9377` dice 下位の巨人 — «un gigante di
rango inferiore» — e l'inglese scrive di nuovo `a Indian Elephant`. E' lo stesso
segnaposto sbagliato in due carte a venti righe di distanza: monte, non noi.

ⓘ Le frasi fra 「」 e 『』 si sciolgono in discorso indiretto, come fanno tutte le
carte gia' rese (`:9273` «si dice perfino che chi incrocia i suoi occhi muore»,
`:9520` il proverbio del topo alle strette): in `db_card.hsp` non c'e' una sola
resa con le virgolette basse.

⚠️ **CORRETTA DOPO IL LOTTO 22:** `:9897` diceva «ha fatto pace con una lumaca».
Il 清掃員 fa pace con una `かたつむり` **base**, che nel progetto e' «la chiocciola»;
«lumaca» e' il nome delle tre uniche. Vedi la testa del lotto 22.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :9104 il mimic kamikaze
    (9104, 'A demon whose hobby is to mimic items and ridicule adventurers. However, it does not seem to think about what happens after its mimicry is discovered, and when it is, it explodes in a panic. '):
        "Un mostro che per passatempo si finge un oggetto e si fa beffe degli avventurieri. Pare però che non abbia pensato a che cosa fare quando lo smascherano: appena succede va nel panico e finisce per esplodere. ",

    # ---------------------------------------------------------- :9117 il pescatore
    (9117, 'People living with the sea, reaping the bounty of the sea. Among fishermen, there is a custom to treat turtles with care, as they are considered to be messengers from the sea. '):
        "Gente che raccoglie i doni del mare e con il mare vive. Fra i pescatori c'è l'usanza di considerare le tartarughe messaggere del mare, e di trattarle con ogni riguardo. ",

    # ---------------------------------------------------------- :9130 il pirata
    (9130, 'Those who travel the great seas of Irva in search of adventure and romance. But romance alone is not enough to feed them, so they regularly attack merchant ships. '):
        "Gente che solca il grande mare di Irva in cerca di avventura e di romanticismo. Ma di solo romanticismo non si campa, e così ogni tanto assaltano una nave mercantile. ",

    # ---------------------------------------------------------- :9143 il cittadino
    (9143, 'Ordinary citizens living in South Tyris. They are often given rotten food on their request, or beaten to a pulp by demons, but they are still surviving in Ylva today. '):
        "Cittadini comuni che abitano a Tyris del Sud. C'è chi per un incarico si vede consegnare cibo marcio e chi finisce tritato da un mostro aizzato contro di lui, eppure anche oggi tirano avanti in Irva con la loro tenacia. ",

    # ---------------------------------------------------------- :9156 il cittadino
    (9156, 'People living in the city. They submit requests for various daily problems. Recently, there have been invasions from neighbouring countries, and they are very much concerned about the state of affairs in the city.'):
        "Gente che abita in città. I guai di ogni giorno, uno per uno, li mettono a bando come incarichi. Di recente ci sono state incursioni dai paesi vicini, e l'aria pesante che tira la sentono addosso tutta.",

    # ---------------------------------------------------------- :9169 il gokiburi
    (9169, 'A fearsome insect given the title of demon. Although its fighting ability is low, its tenacity, resilience and ability to multiply are fearsome. Frustratingly, they are also very friendly.'):
        "Un insetto tremendo, a cui è stato conferito il titolo di demone. In combattimento vale poco, ma la sua ostinazione, la sua resistenza e la sua capacità di moltiplicarsi meritano davvero paura. E la cosa fastidiosa è che è pure affettuoso.",

    # ---------------------------------------------------------- :9182 <Carla> del Mondo Dimenticato
    (9182, 'A girl from a world called Gaius Vis. She once saved a traveller who was dying when his ship was shipwrecked. Elea.'):
        "Una ragazza venuta da un mondo chiamato Gaius Vis. Una volta ha salvato un viaggiatore che stava morendo dopo un naufragio. È del popolo di Elsia.",

    # ---------------------------------------------------------- :9195 <Milos> del Mondo Dimenticato
    (9195, "He comes from a world called Gaius Vis. He used to be a hard-headed man, but has recently become much more matured, probably due to Carla's influence. "):
        "Viene da un mondo chiamato Gaius Vis. Un tempo era un uomo di testa dura, ma ultimamente si è parecchio smussato, forse per l'influenza di Carla. ",

    # ---------------------------------------------------------- :9208 la sorella minore maliziosa
    (9208, 'A younger sister who is desperate for love. She has a habit of daydreaming and gets nosebleeds alone when she fantasises about an ecchi life with her brother (or sister). She seems to be anaemic because of this.'):
        "Una sorellastra affamata d'affetto. Ha il vizio di fantasticare, e mentre si immagina una vita spinta con il fratello (o la sorella) le viene da sola l'emorragia dal naso. Forse è per questo che tende all'anemia.",

    # ---------------------------------------------------------- :9221 <Meshera Mudo> il semenzaio della calamità
    (9221, 'The original swarm of artificial bacteria, which were being researched at Remido. It was originally intended to strengthen all life forms and counter certain threats. Code name during research was Messiah.'):
        "La colonia originale dei batteri artificiali che si studiavano a Rehm-Ido. In origine dovevano potenziare ogni forma di vita per opporsi a una certa minaccia. Durante le ricerche il nome in codice era Messia.",

    # ---------------------------------------------------------- :9234 il dio a cinque teste
    (9234, 'It was born from the fusion of five dragons. They are revered by those who are fascinated by their overwhelming power, and even have the aspect of gods now. If they all breathe out their breath at the same time, they run out of oxygen, so they breathe out one by one in turn.'):
        "È nato dalla fusione di cinque draghi. La sua forza schiacciante affascina la gente e ne raccoglie il timore, tanto che ormai ha perfino un lato divino. Se lanciassero il soffio tutte insieme le teste resterebbero senz'aria, e così soffiano a turno, una per volta.",

    # ---------------------------------------------------------- :9247 la lumaca parassitata
    (9247, "A snail parasitised by something. It unleashes attacks without regard for its own physical vulnerability, but this is due to the parasite's will to change its host by daring to prey on it. "):
        "Una lumaca in cui si è annidato qualcosa. Attacca senza alcun riguardo per la fragilità del proprio corpo, ma è la volontà del parassita, che si fa predare apposta per cambiare ospite. ",

    # ---------------------------------------------------------- :9260 l'uccello vermiglio
    (9260, 'Mutated age-old birds. It hates being identified with phoenixes and phoenixes. Although its name is Vermilion Sparrow, it does not seem to be mistaken for a sparrow, as one would expect.'):
        "È un uccello molto vecchio che è mutato. Odia da morire che lo si confonda con l'araba fenice o con la fenice d'oriente. Il suo nome dice passero vermiglio, ma per un passero, questo è certo, non lo scambia nessuno.",

    # ---------------------------------------------------------- :9273 la coccatrice
    (9273, "Chicken monster. Those who are exposed to its gaze are rendered immobile as if their bodies had turned to stone. It is even said that 'if you make eye contact with it, you will die'."):
        "Un mostro a forma di gallo. Chi ne riceve lo sguardo non riesce più a muoversi, come se il corpo gli si fosse fatto di pietra. Per questo si dice perfino che chi incrocia i suoi occhi muore.",

    # ---------------------------------------------------------- :9286 l'ariete dorato
    (9286, 'A rare sheep with a golden fleece. Its delicate, pure white fleece, which appears golden in the light, once caused people to fight over it. '):
        "Una pecora rara, dal vello che riluce d'oro. Quel pelo candido e sottile, che alla luce sembra oro colato, un tempo arrivò a far scoppiare una guerra fra gli uomini. ",

    # ---------------------------------------------------------- :9299 l'arpia domestica del drago
    (9299, 'A bird race bred by the dragon tribe. They are more ferocious than regular harpies, and their tendency to split apart when attacked, as if hit with a kaleidoscope, has caused many adventurers distress. '):
        "Una razza di uomini uccello allevata dai draghi. È più feroce di un'arpia comune, e per giunta, se la si attacca, si moltiplica come in un caleidoscopio: due doti che hanno fatto penare molti avventurieri. ",

    # ---------------------------------------------------------- :9312 la roccia esplosiva al deuterio
    (9312, 'A moving rock with a tremendous energy source. It produces large bursts of light and explosions when stimulated from the outside. The explosions can be mistaken for a small sun.'):
        "Una roccia semovente che nasconde dentro di sé una fonte di energia enorme. A uno stimolo esterno produce una gran luce e un'esplosione, e quell'esplosione la si scambia per un piccolo sole.",

    # ---------------------------------------------------------- :9325 l'olog
    (9325, 'Titans created by the Dark Lord, who planned to rule the earth from hell. They look like trolls, but are incomparably more intelligent and can speak their own language. '):
        "Un gigante creato dal signore dell'oltretomba, che dall'inferno puntava a dominare la superficie. Somiglia al troll, ma è intelligente in un modo che non regge il confronto, e sa conversare in una lingua tutta sua. ",

    # ---------------------------------------------------------- :9338 il granchio del cocco mangiauomini
    (9338, 'Its well-developed scissors have a very strong pinching force and can slice a Indian Elephant in a circle. Despite their name, they are omnivorous and will eat anything they can get their mouths on, including fruit, grass and animals. '):
        "Le chele, molto sviluppate, stringono con una forza tale da tranciare a fette un braccio d'uomo. A dispetto del nome è onnivoro: frutta, erba, animali, tutto quel che gli entra in bocca. ",

    # ---------------------------------------------------------- :9351 il dragonewt
    (9351, 'A formidable dragon-man warrior. They have extremely high intelligence and a robust body covered with scales, and they very much dislike being mistaken for lower-ranked warrior lizardmen. '):
        "Un guerriero dragonewt di gran vigore. Ha un'intelligenza altissima e un corpo robusto coperto di scaglie, e detesta moltissimo essere scambiato per un uomo lucertola, che è un guerriero di rango inferiore. ",

    # ---------------------------------------------------------- :9364 la Titania
    (9364, 'She is skilled in a variety of magic and is herself resistant to many different attributes. Even after becoming a respectable queen, she still has the mischievous spirit of a fairy. '):
        "Padroneggia magie di ogni sorta, e lei stessa resiste a parecchi elementi. Anche diventata una regina in piena regola non dimentica lo spirito burlone: è il buon gusto delle fate. ",

    # ---------------------------------------------------------- :9377 il coboldo diabolico
    (9377, 'A kobold with the strength of a demon. They are powerful enough to wrangle an Indian Elephant with ease, and they also attack in packs. '):
        "Un coboldo con la forza di un demone. Ha una potenza che gli basta a piegare senza fatica un gigante di rango inferiore, e per giunta assale in branco. ",

    # ---------------------------------------------------------- :9390 la Heqet
    (9390, 'Frog hunter named after the water goddess. It will try to kill its target while planting eggs on them. The strong ones that survive will give birth to their strong offspring.'):
        "Una cacciatrice rana che porta il nome della dea dell'acqua. Alla preda che ha puntato impianta le uova, e insieme cerca di ucciderla. Da chi è tanto forte da sopravviverle nasceranno figli fortissimi, c'è da crederci.",

    # ---------------------------------------------------------- :9403 <Lumaca> alata
    (9403, 'A snail that has grown wings under the influence of the ether wind. Surprisingly foul-mouthed. It seems that it is not only his movements that are slow, and he does not easily notice when favours are shown to him.'):
        "Una lumaca a cui l'etere ha fatto spuntare le ali. Ha una linguaccia che non ti aspetti. E a quanto pare non è lenta soltanto nei movimenti: se qualcuno le mostra dell'affetto, ci mette un bel po' ad accorgersene.",

    # ---------------------------------------------------------- :9416 il velivolo da combattimento Yerles
    (9416, 'It was developed by capturing and analysing flight units from the age of mechanical civilisation. It is mainly used as flying equipment and cover for soldiers. It can also act independently using autonomous circuits.'):
        "L'hanno sviluppato catturando e analizzando le unità di volo della civiltà meccanica. Serve soprattutto ai soldati come equipaggiamento di volo e come copertura. Grazie ai circuiti autonomi può agire anche da solo.",

    # ---------------------------------------------------------- :9429 <Exossil> l'ala del caos
    (9429, 'A god of the dead, born from the amalgamation of the spirits of angels and demons, respectively. The power hidden in its wings is immeasurable. Its birth is said to be related to a certain sorcerer.'):
        "Un dio degli spiriti dei morti, nato dalla fusione dello spirito di un angelo e di quello di un demone. La potenza nascosta in quelle ali non si può misurare. Si dice che alla sua nascita abbia preso parte un mago.",

    # ---------------------------------------------------------- :9442 <Metal Vesda> il drago di fuoco meccanico
    (9442, 'A large air combat weapon developed by the Yerles military. It was stored in the basement of the fortress, but was thrown out into the central core when the fortress was fused with Nefia by a tectonic movement. '):
        "Una grande arma da combattimento aereo sviluppata dall'esercito di Yerles. Era custodita nei sotterranei della fortezza, ma quando i movimenti della crosta fusero la fortezza con una Nefia, finì scaraventata nel suo cuore. ",

    # ---------------------------------------------------------- :9455 <Anubis> il signore della morte
    (9455, 'Guardian of the underworld who controls the light of the sun while underground. He leads the dead to the Valley of the Dead, where he reigns, and weighs their sins. He used to have god-like powers, but not so much nowadays.'):
        "Il guardiano dell'oltretomba che, pur stando sottoterra, governa la luce del sole. Conduce i morti alla Valle degli Inferi, su cui regna, e ne pesa le colpe. Un tempo aveva poteri da dio, oggi non più di tanto.",

    # ---------------------------------------------------------- :9468 il drago zombi
    (9468, 'Rotting dragon corpses brought to life by high-level lich. Although magically enhanced, they are not very strong due to rotting muscles. '):
        "Il cadavere putrefatto di un drago a cui un lich di alto livello ha soffiato dentro la vita. La magia lo rinforza, ma con i muscoli marci di forza ne ha poca. ",

    # ---------------------------------------------------------- :9481 la forma di vita quantistica
    (9481, 'This creature is not of this world. Mysterious power seems to emanate out of it from somewhere. Its power source is also unknown. It cries, but where does it get its voice from?'):
        "Questa creatura non è di questo mondo. Pare che da qualche parte le sgorghi un potere misterioso. E nemmeno si sa che cosa la muova. Squittisce, ma da dove esca quella voce è un mistero.",

    # ---------------------------------------------------------- :9494 <Lend> il venditore di sfere
    (9494, 'He has managed to get hold of stubborn ball-makers and buys monster balls directly from them. As they are not widely distributed, they have a near-monopoly on them. '):
        "È riuscito in qualche modo a ingraziarsi un testardo artigiano di sfere, e da lui compra le sfere dei mostri di prima mano. In commercio se ne trovano poche, e così ha quasi il monopolio. ",

    # ---------------------------------------------------------- :9507 il mercante fallito <Guo>
    (9507, 'He had a country-born complex and left his village when he was young to become a merchant. He became very rich for a while but got overzealous and his business failed. '):
        "Aveva il complesso delle proprie origini di campagna, e da giovane scappò dal villaggio per farsi mercante. Per un po' fu ricchissimo, ma montandosi troppo la testa mandò in rovina i suoi affari. ",

    # ---------------------------------------------------------- :9520 il ratto sanguinario
    (9520, "It has body hair darkened by the reflux of blood that it is continually exposed to and soaks up. The old saying goes 'a cornered rat will bite a cat', and with this rat, the cat is the prey. "):
        "Ha il pelo incupito dal sangue altrui, che gli schizza addosso di continuo e gli si è impregnato dentro. C'è un vecchio detto per cui il topo alle strette morde il gatto, ma con questo ratto è il gatto a diventare la preda. ",

    # ---------------------------------------------------------- :9533 il sistema di difesa di Yerles
    (9533, 'They are mainly installed in defensive positions. Prototype aircraft equipped with Gatling guns with seemingly excessive firepower exist, as a hobby of the chief developer. '):
        "Lo si installa soprattutto nelle postazioni di difesa. Ne esiste un prototipo che, per il gusto personale del capo progettista, monta un cannone Gatling dalla potenza di fuoco che pare eccessiva. ",

    # ---------------------------------------------------------- :9546 la melma metamorfica
    (9546, 'The slime has taken in a mysterious object from outer space and mutated. The cells are severely unstable and a slight shock causes them to transform. '):
        "Una melma che ha inglobato un oggetto misterioso venuto dallo spazio ed è mutata. Le sue cellule sono di un'instabilità tremenda, e basta un piccolo urto perché si trasformi. ",

    # ---------------------------------------------------------- :9559 la pecora elettrica
    (9559, 'A sheep whose body hair, originally prone to storing static electricity, has somehow become so charged that it can be used to attack. Whenever it moves, it emits a loud, crackling sound. '):
        "Una pecora il cui pelo, già di suo incline ad accumulare elettricità statica, chissà come si è caricato al punto da poter servire per attaccare. A ogni movimento manda un crepitio violento. ",

    # ---------------------------------------------------------- :9572 <Lune> la cameriera
    (9572, 'A very restless and fidgety maid. She came to the city as a migrant worker, but soon afterwards she found herself on the street because her owner went bankrupt. '):
        "Una cameriera irrequieta e sbadata da non dirsi. Era venuta in città a cercare lavoro, ma poco dopo il suo padrone è fallito e adesso si ritrova sulla strada. ",

    # ---------------------------------------------------------- :9585 la cameriera
    (9585, 'Blossoms that adorn the mansion. A professional who can appraise, train and investigate her peers with perfection, but she is not a great chef. Only male maids are treated badly by some masters.'):
        "Il fiore che adorna la magione. È una professionista che sbriga senza sbavature l'identificazione, l'addestramento e l'esame dei compagni, ma in cucina è negata. E con certi padroni sono solo le cameriere maschio a essere trattate male.",

    # ---------------------------------------------------------- :9598 l'Atlante
    (9598, 'Descendants of the gods who once ruled the earth. They carry intense resentment because their brethren have been forced underground by the current gods. '):
        "Discendenti delle divinità che un tempo dominavano la superficie. I loro fratelli sono stati ricacciati nelle viscere della terra dalle divinità di adesso, e per questo covano un rancore feroce. ",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-019.jsonl'
DA, A = 9101, 9600
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
