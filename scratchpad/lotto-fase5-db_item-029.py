# -*- coding: utf-8 -*-
"""114a - Lotto 029 di `db_item.hsp`: IL MOBILIO, terza parte.

`FILTER_FURNITURE`, righe 91.500-108.000: **30 righe** su 27 oggetti — 27
dell'indice 0 e **tre dell'indice 2** (`:94927`, `:98007`, `:98358`), che sono
le prime citazioni che il corpo del mobilio porta dentro.

⚠️ **E il mobilio che resta sta tutto DOPO, non prima.** Le 137 righe
dell'indice 0 e le 6 dell'indice 2 che restano vanno da **:108393 a :127609**:
sotto la riga 91.500 non ne resta **nessuna**. La prima stesura di questo
docstring diceva l'opposto — «tutte sotto la riga 91.500» — perche' il numero
veniva dalla tabella della 113a, che era scritta a mano e contava all'indietro.
Da qui `scratchpad/_114-corpo-da-fare.py`, che quel conto lo fa da se'.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **I tre lumi** (`:91718` il lampione moderno, `:91780` la lampada
  stravagante, `:91842` la candela): tre oggetti che fanno luce e nessuno dei
  tre la fa per lo stesso motivo — l'ornamento, il vanto dei nobili,
  l'atmosfera. Le rese restano tre.
  ⓘ `:91842` dice 恋する二人 come `:91274` del lotto 028 (il lampione innevato):
  li' era «accende il fuoco fra due innamorati», qui «la distanza fra due
  innamorati». Stesso termine, stessa resa.
- **I tre quadri** (`:94987` i girasoli, `:95049` il paesaggio, `:95111` la
  dama): stessa apertura 高名な画家が描いたとされる, che resta identica in tutte
  e tre — «che si dice dipinto da un pittore famoso» — e cambia solo il genere.
- **Le due macchine dei tesori** (`:103360` blu, `:103425` rossa): la **prima
  frase e' la stessa parola per parola**, e la seconda no. La resa della prima
  frase e' identica nelle due righe, come vuole `_107-firme-gemelle.py`.
- **Il gatto e chi non lo sopporta** (`:94925` e `:94927`): la statua e la
  battuta di <Tam>. La battuta nomina 石柱, la **colonna**, che e' la parola con
  cui la descrizione dell'indice 0 chiama l'oggetto: le due rese si tengono.
- **L'attrezzo da palestra** (`:98356` la reclame, `:98358` la prosa): due
  indici dello stesso oggetto, uno sotto l'altro nello stesso pannello.

### ⭐⭐ L'INGLESE SBAGLIA UNA VOLTA, E BUTTA VIA UNA FRASE

**`:94863`, il cristallo nero.** Il giapponese ha tre pezzi:
邪気を祓う (scaccia gli influssi maligni), 日の光を乱反射し燦然と輝く (rifrange
la luce del sole e sfolgora) e 古来から魔術において重要な位置を占める (occupa da
sempre un posto importante nella magia). L'inglese tiene il primo e il terzo e
**butta via il secondo**, che e' l'unico che dice come l'oggetto si vede. E' la
stessa forma del `:87505` del lotto 028, la credenza a cui l'inglese toglieva
l'estro nascosto del maestro.

⚠️ E due appiattimenti piu' piccoli, tutti e due sul quadro dei girasoli
(`:94987`): l'inglese scrive «The canvas is said to be filled with many
sunflowers» come se il *si dice* riguardasse i girasoli, mentre in giapponese
riguarda quello che i girasoli **fanno** — prendono l'occhio e il cuore di chi
guarda e non li lasciano piu'. E scrive 静物画 come «Still-life painting»
appiattendo il tipo di quadro, che invece distingue i tre: natura morta,
paesaggio, ritratto.

### ⭐ I TERMINI CERCATI A MANO

    サイバードーム   -> la Cupola Cibernetica   (`glossario.md:192`)
    ヴェルニース     -> Vernis                  (`invariati.md:40`, nome opaco)
    ヨウィン         -> Yowyn                   (`invariati.md:44`)
    パルミア         -> Palmia                  (`invariati.md:41`)
    警備部隊         -> corpo di guardia        (`db_creature.hsp`, <Orville>)
    マテリアル       -> materiale               (`chat.hsp`, «materiali da lavorazione»)
    大富豪           -> il riccone              (gia' nel dizionario)
    観葉植物         -> pianta ornamentale      (quattro nomi di oggetto)
    ガシャポンの玉   -> sfera del tesoro        (gia' nel dizionario)

⚠️ **パルミア警備隊 non e' nel dizionario**, ma 警備部隊 si': `<Orville> il
comandante della sicurezza` e «la scarsa preparazione del **corpo di guardia**».
Qui la resa e' «le guardie di Palmia», che e' la stessa cosa detta corta —
la riga e' gia' lunga e il pannello si impagina.

⚠️ **異国の硬貨 non e' nel dizionario in nessuna forma**: e' «una moneta
straniera», reso a lettera. Le monete che il dizionario conosce sono di bronzo
e di platino, e non sono queste.

### ⭐ LE TRE CITAZIONI PORTANO LE VIRGOLETTE CON L'ESCAPE

`:94927`, `:98007` e `:98356` sono discorso diretto, e nel sorgente HSP la
citazione sta dentro `\\"..\\"`. Il modello e' `_traduzioni026.py:23` (il
mesugaki): nella tabella si scrive `\\\\\\"`, che e' un backslash e una
virgoletta veri.

### ⭐ LA SETTIMA FONTE, PER IL CORPO

`scratchpad/lotti-113/_gia-reso.py` fa per la **prosa** la domanda che
`_113-fonti-gia-rese.py` fa per i titoli: questo giapponese e' gia' reso da
qualche altra parte? Per il lotto 029 la risposta e' **0 su 30** — nessuna di
queste trenta prose torna altrove nel gioco — e la prova al contrario e' il
lotto **028**, gia' reso, dove la stessa rete si accende **46 su 46**.

⚠️ La prima versione della rete diceva «30 su 30» e non voleva dire niente:
cercava il contenimento con la soglia su **un lato solo**, e ogni voce del
dizionario col giapponese corto — una particella, un `。` — sta dentro
qualunque prosa. La soglia va sui due lati.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :91718
    (91718, 'A streetlight with a stylish decoration. At night, they glow faintly with their own light, making the area look gorgeous. \\n# ~Supporting Roles on the Streets~'):
        "Un lampione ornato con un tocco di eleganza. Quando viene notte brilla di luce propria, tenue, e dà a tutto quello che ha intorno un'aria sfarzosa. \\n# ~I Grandi Comprimari della Città~",

    # ---------------------------------------------------------- :91780
    (91780, 'This lighting fixture was once created by a genius of the century. Its innovative construction is still one of the most popular among aristocrats. \\n# ~Daily Necessities for the Home~'):
        "Un apparecchio per fare luce che si dice costruito, un tempo, da un genio del secolo. La sua fattura ardita è ancora oggi fra le più amate dai nobili. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :91842
    (91842, 'Atmospheric lighting made of wax. Its small flickering flame is said to bring two people in love even closer together. \\n# ~Daily Necessities for the Home~'):
        "Un lume di cera, di quelli che fanno atmosfera. Quella piccola fiamma che ondeggia, dicono, accorcia ancora di più la distanza fra due innamorati. \\n# ~Casalinghi che Danno Colore alla Casa~",

    # ---------------------------------------------------------- :92124
    (92124, "A shelf that is widely used by the masses. It is a safe piece of furniture that can't be used for more than you expect, but does the bare minimum of what you need it to do. \\n# ~Great Encyclopedia of North Tyris Furnitures~"):
        "Uno scaffale di quelli che circolano dappertutto. Non serve a niente di più di quel che ci si aspetta, ma il minimo indispensabile lo fa: un mobile senza rischi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :94801
    (94801, 'Very funny looking snow sculptures. When it snows, children gather to make snowmen of their own design and show them to each other. \\n# ~North Tyris Travels, Winter Edition~'):
        "Una statua di neve dall'espressione buffissima. Quando nevica, dicono, i bambini si radunano, fanno ciascuno il pupazzo che ha in mente e poi se li mostrano a vicenda. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :94863
    (94863, 'Giant mineral that is said to purge evil spirits. It is said to have occupied an important position in magic since ancient times. \\n#~Arcane Almanac~'):
        "Un minerale enorme che, dicono, scaccia gli influssi maligni. Rifrange la luce del sole in ogni direzione e sfolgora, e fin dall'antichità occupa un posto importante nelle arti magiche. \\n#~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94925
    (94925, "Pillar with an adorable cat modeled at the top. It is said that the charming rear figure was carved by an artist who sensed the cat's inherent whimsy. \\n# ~Lumiest Art Catalogue~"):
        "Una colonna di pietra con in cima un gatto grazioso. Quella schiena piena di garbo, si dice, l'artista l'ha scolpita dopo aver colto il capriccio che è proprio dei gatti. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :94927
    (94927, '\\"I went to Vernis before, and there it was, that thing! The horrible tail and those ears, I can\'t stop shaking just thinking about it.... Who in the world could have made a stone pillar like that? The only relief was that it wasn\'t facing me.\\" \\n# ~<Tam> the cat hater~'):
        "\\\"Tempo fa sono stato a Vernis, e c'era quella cosa! La coda spaventosa, e quelle orecchie: solo a pensarci non smetto di tremare... Ma chi mai avrà fatto una colonna del genere? L'unica consolazione è che non era girata verso di me\\\" \\n# ~Parole di <Tam> il nemico dei gatti~",

    # ---------------------------------------------------------- :94987
    (94987, "Still-life painting said to have been painted by a famous artist. The canvas is said to be filled with many sunflowers, attracting the viewer's eyes and heart. \\n# ~Lumiest Art Catalogue~"):
        "Una natura morta che si dice dipinta da un pittore famoso. I molti girasoli che riempiono la tela, dicono, prendono l'occhio e il cuore di chi guarda e non li lasciano più. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95049
    (95049, 'Landscape painting said to have been painted by a famous artist. It is said that this painting, which evokes a nostalgic atmosphere, reminds people of their hometowns. \\n# ~Lumiest Art Catalogue~'):
        "Un paesaggio che si dice dipinto da un pittore famoso. In questo quadro, che desta un'aria di nostalgia venuta chissà da dove, ognuno finisce per rivedere il proprio paese. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95111
    (95111, "Portrait painting said to have been painted by a famous artist. The melancholy expression on her face possesses something that moves the viewer's heart. \\n# ~Lumiest Art Catalogue~"):
        "Un ritratto che si dice dipinto da un pittore famoso. Quella sua espressione velata di malinconia, dicono, ha in sé qualcosa che smuove il cuore di chi guarda. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :95174
    (95174, 'The table is big enough to accommodate unexpected guests. One should learn from the depth of this open-mindedness. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un tavolo generoso, capace di far posto anche all'ospite che arriva all'improvviso. Quella larghezza di cuore sarebbe da imparare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95236
    (95236, 'Potted plants are so tall that they almost reach the ceiling. Every stem is growing toward the sun single-mindedly. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Una pianta in vaso così alta da sfiorare il soffitto. Ogni stelo, tutti quanti, si allunga verso il sole e non guarda altro. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95298
    (95298, 'Equipment used to cook food. It is not allowed to cook as it is being used anytime you see it. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un'attrezzatura per cuocere e bollire i cibi. Ogni volta che la si guarda è occupata, e perciò non ci si può cucinare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95360
    (95360, 'A heating device used to warm a room. The crackling flames inside the furnace will slowly melt your hearty cold body. \\n# ~Great Encyclopedia of North Tyris Furnitures~'):
        "Un apparecchio che serve a scaldare gli ambienti. La fiamma che divampa crepitando dentro il focolare scioglierà piano il corpo intirizzito fino al midollo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # ---------------------------------------------------------- :95422
    (95422, 'Furnace for melting metals. The inside is always heated by red-hot wood. \\n# ~Aiming for Better Workmanship~'):
        "Un forno per fondere i metalli. Dentro è tenuto caldo di continuo da legna arroventata. \\n# ~Verso una Lama Migliore~",

    # ---------------------------------------------------------- :97873
    (97873, 'A disk in unused condition. It is a worthless item because it cannot be used, but it is said to be bought as a souvenir by Yowyn farmers on rare occasions when they visit the area for sightseeing. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un disco ancora da usare. Non essendo utilizzabile non vale niente, ma di rado, dicono, qualche contadino di Yowyn venuto in gita se lo compra per ricordo. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :97943
    (97943, 'A mysterious small piece with a regular pattern engraved on it. It is presumed to be very beautiful and ornamental, but cannot be equipped. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un piccolo frammento misterioso, inciso con un disegno regolare. Tanto è bello che lo si suppone un ornamento, ma non si può equipaggiare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98005
    (98005, 'A container made to hold specific waste materials. It is said that if you put anything other than specific items in this in the cyberdome, the residents will look at you with disgust. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una scatola fatta per raccogliere certi rifiuti e non altri. In quella della Cupola Cibernetica, dicono, a metterci dentro qualcosa di diverso gli abitanti fanno una faccia storta. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98007
    (98007, '\\"This is one of those things that I\'ve witnessed and gotten. It\'s not just any old thing. First of all, the color is nice, and the shape. There\'s something fun about it. And between you and me, it has a secret...oops, you\'ll have to wait until after you buy it.\\" \\n# ~<Moyer> the crooked~'):
        "\\\"Avvicinatevi, avvicinatevi! Guardate che pezzo mi sono procurato. Roba che non si trova in giro, eh. Intanto il colore, e poi questa forma. Ha un'aria allegra. E, detto fra noi, questo qui ha un segreto... ehi, ehi, quello ve lo godete dopo che l'avete comprato\\\" \\n# ~La Cantilena di <Moyer> l'imbonitore~",

    # ---------------------------------------------------------- :98075
    (98075, 'Cylindrical metal objects used to store something. Its purpose is now lost, so it is usually filled with garbage. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un corpo di metallo a forma di cilindro, che serviva a conservare qualcosa. A che cosa di preciso ormai è perduto, e così di solito dentro ci si trova spazzatura. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98145
    (98145, 'Mysterious memory device that is said to contain ancient memories. Such is the rumor, but there is still no one who has been able to open the memory. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un misterioso apparecchio di memoria in cui, si dice, sono sigillati i ricordi antichi. Così vuole la voce; ma finora nessuno è riuscito ad aprirli. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98215
    (98215, 'Amazing box that destroys stored items by applying powerful heat to them. It is currently broken and unusable. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Una scatola prodigiosa che, dicono, distrugge quello che le si mette dentro sottoponendolo a un calore fortissimo. Adesso è rotta, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98285
    (98285, 'Amazing device that can contain ones existence. Currently it is broken and cannot be used. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Un apparecchio prodigioso che, dicono, sa imprigionare l'esistenza di una cosa. Adesso è rotto, o così pare, e non si può usare. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98356
    (98356, '\\"Try this for 5 minutes a day, 5 minutes a day! That fat, ugly body of yours will somehow get rid of itself just by working out with this for 5 minutes a day! The results are unknown!\\" \\n# ~Mysterious Memo on the Training Machine~'):
        "\\\"Cinque minuti al giorno, bastano cinque minuti al giorno, provate! Anche quel vostro corpo grasso e sgraziato, con cinque minuti al giorno qui sopra, in qualche modo si sistema! L'efficacia? Tutta da vedere!\\\" \\n# ~Istruzioni Misteriose in un Angolo dell'Attrezzo~",

    # ---------------------------------------------------------- :98358
    (98358, 'A machine that, when used, can stimulate growth in the body. Some of the Palmia Guard, whose bodies are their most important assets, have even gone to the trouble of purchasing the machine and using it at home. \\n# ~Daily Necessities for the Home~'):
        "Una macchina che, a usarla, fa crescere il fisico. Fra le guardie di Palmia, che sul corpo ci campano, c'è perfino chi se l'è comprata apposta per usarla in casa. \\n# ~Casalinghi che Danno Colore alla Casa~",

# 3 voci, 0 ambigue

    # ---------------------------------------------------------- :98426
    (98426, "A strange box with a dull sound. There is no place to open it, so you can't stuff things inside. \\n# ~The Yowyn Book of Secrt Knowledge!~"):
        "Una scatola strana che manda un suono sordo. Non ha nessun punto da cui aprirla, e perciò dentro non ci si può mettere niente. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :98496
    (98496, 'Strange object with a flickering light. Its use is unknown, but it is said to be bought by wealthy people on rare occasions as a decorative item for their rooms. \\n# ~The Yowyn Book of Secrt Knowledge!~'):
        "Uno strano oggetto che manda lampi. A che serva non si sa, ma passa per ornamento da stanza, e di rado, dicono, qualche riccone se lo compra. \\n# ~Speciale Yowyn: a Caccia del Sapere Ignoto!~",

    # ---------------------------------------------------------- :103360
    (103360, 'A machine that ejects spheres containing items by using exotic coins. It requires more valuable materials than the red ones, but you can expect better items to come out of it. \\n# ~Game Tricks, All Ages Version~'):
        "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Vuole un materiale di più valore di quella rossa, ma in cambio da quel che ne esce c'è da aspettarsi di più. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # ---------------------------------------------------------- :103425
    (103425, "A machine that ejects spheres containing items by using exotic coins. I don't know why, but I hear there are a lot of kids hanging out in that area. \\n# ~Game Tricks, All Ages Version~"):
        "Una macchina che, a metterci una moneta straniera, sputa fuori una sfera con dentro un oggetto. Chissà perché, pare che lì attorno ci siano spesso dei bambini a bighellonare. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

# 27 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-029.jsonl'
RIGHE = {
    91718, 91780, 91842, 92124, 94801, 94863, 94925, 94927, 94987, 95049,
    95111, 95174, 95236, 95298, 95360, 95422, 97873, 97943, 98005, 98007,
    98075, 98145, 98215, 98285, 98356, 98358, 98426, 98496, 103360, 103425,
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
