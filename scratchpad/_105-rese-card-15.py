# -*- coding: utf-8 -*-
"""105a - Lotto 15 di `db_card.hsp`: le carte fra la riga 7101 e la 7600 (39).

Il blocco viene subito dopo la catena dell'inglese slittato della 104a, che si
richiude a `:7076`: qui l'inglese di monte e' di nuovo il suo, carta per carta.
Verificato leggendo il dossier riga per riga, e `_104-inglese-slittato` non
segnala nessuna testa in questa zona.

⭐ **Gia' deciso altrove, e qui si ubbidisce:**
`神の欠片` → **una scheggia di divinita'** (`:1772`, `:3943`),
`冥界` → **l'oltretomba** (`:1018`, `:12947`),
`亜竜` → **il draco** (`:1434`, `:1460`),
`魔獣` → **la belva magica** (`:2747`, `:4177`),
`サウスティリス` → **Tyris del Sud**, `メルカーン` → **Melkawn**,
`メルカ地方` → **la regione di Merca** (`map.hsp:3619`, «Palude di Merca»),
`ギルドマスター` → **il maestro / la maestra della Gilda dei ...**
(`db_card.hsp:14663`, `:14689`, `:14715`), `調査員` → **l'investigatrice**
(`chat.hsp:9247`, e le tre carte di questo lotto sono le stesse tre persone),
`迷宮` → **il labirinto**, `牧場` → **l'allevamento** e `ブリーダー` → **la
riproduzione** (`command.hsp:1259`, `map_user.hsp:412`),
`ミミック` → **il mimic**, `ギガモール` → **la talpa colossale** (coniata nella
103a, e qui il suo blocco si apre davvero, a `:7206`).

⚠️ **`ロストテクノロジー` e `第一紀` non erano mai comparsi**: resi **la
tecnologia perduta** (`:7310`, `:7323`) e **la Prima Era** (`:7505`).
⚠️ **`超獣` compare UNA VOLTA SOLA in tutto il sorgente** (`:7193`, l'inglese
dice `superbeast`): coniato **la superbestia**. Se tornasse altrove, si ubbidisce
a questa.

ⓘ `:7310` e `:7323` (i due moai) hanno la **stessa prima frase** in giapponese e
in inglese, e il resto diverso: le due rese condividono la prima frase e
divergono dopo, come diverge il giapponese.

⚠️ Niente `«»` e niente `…` nelle rese: sono nella lista dei proibiti di
`scratchpad/guardie.py`. I due nomi che il giapponese cita (lo scorpione nero
dell'Ek Chuah, il significato della dominazione) si sciolgono senza virgolette.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :7102 il riccio dell'inferno di aghi
    (7102, 'A rodent-shaped beast that gathers together to form a hell of needles. The sinners who have fallen into the underworld are being tormented by sticking needles into them so that they can get rid of their sins. Some individuals are separated from the group and wander to the ground.'):
        "Una belva magica a forma di riccio, che si raduna con le sue simili fino a formare un inferno di aghi. Infilza sugli aghi i peccatori precipitati nell'oltretomba e li tormenta: così salda i conti che quelli hanno con la loro colpa. Qualcuno si stacca dal branco e finisce per smarrirsi in superficie.",

    # ---------------------------------------------------------- :7115 il riccio dai mille aghi
    (7115, 'When it gets aroused it deploys its needles sucking in air and making its body swell. It is also possible to fire the stored magic power from a needle like an arrow. There was a scholar who looked into whether the needle was really a thousand needles and sure enough it turned out to be worse than being minced.'):
        "Quando si agita drizza gli aghi, tira aria e si gonfia. Dagli aghi può anche scagliare come frecce la magia che ha messo da parte. Ci fu uno studioso che volle accertare se gli aghi fossero davvero mille: come da copione, di lui restò qualcosa di peggio della carne tritata.",

    # ---------------------------------------------------------- :7128 il martello indaco
    (7128, 'A lobster carrying giant pincers that look like a sledgehammer. They live mainly on the ocean floor but can also be found on land. It has a ghastly color but if you cook it it turns a delicious red color.'):
        "Un'aragosta armata di chele enormi, che paiono due mazze. Vive soprattutto sui fondali, ma anche a terra se la cava. Ha un colore che toglie l'appetito, però basta passarla sul fuoco e diventa rossa e invitante.",

    # ---------------------------------------------------------- :7141 il capibara
    (7141, 'A giant rat that is said to be the master of the prairie. They are not intolerant but they do not like the cold. They also have a gentle human-friendly nature and are sometimes found soaking in hot springs in the countryside.'):
        "Un roditore enorme, che c'è perfino chi lo chiama il signore della prateria. Non è che il freddo non lo regga, ma non lo sopporta. Ha un carattere mite e si affeziona agli uomini: capita di trovarlo a mollo nelle terme dei villaggi.",

    # ---------------------------------------------------------- :7154 il tanuki mutaforma
    (7154, 'A badger with the ability to change. They can turn into powerful demons to surprise humans or they can turn into weak demons to catch their prey off guard. They are rivals to Mimics who are also able to transform.'):
        "Un tanuki capace di trasformarsi. Si fa mostro potente per spaventare gli uomini, oppure mostro da poco per far abbassare la guardia alla preda. Col mimic sono rivali, e passano il tempo a ingannarsi a vicenda.",

    # ---------------------------------------------------------- :7167 la campana a martello
    (7167, 'A bell demon that wanders around with unusual speed. It clings to others at high speed and presents itself with a gaudy colored body. When it is hit it emits a loud alarm sound and attracts demons in the area.'):
        "Un mostro a forma di campana, che vaga con una rapidità che non è normale. Ti si appiccica addosso a tutta velocità e mette in mostra il corpo dai colori sgargianti perché nessuno possa ignorarlo. Se lo si percuote lancia un allarme fortissimo e richiama tutti i mostri dei dintorni.",

    # ---------------------------------------------------------- :7180 il Ragnarocca
    (7180, 'They were born in the wake of an enormous amount of divine power during the final war of the gods. They stab anything they touch call for doomsday and blow themselves up in the end.'):
        "È nato durante la guerra ultima degli dei, investito dall'onda di un potere divino smisurato. Infilza qualunque cosa gli capiti a tiro senza guardare in faccia nessuno, chiama la fine del mondo e per finire si fa saltare in aria: un fanatico della rovina, e senza mezze misure.",

    # ---------------------------------------------------------- :7193 la talpa oscura
    (7193, 'A superbeast that has developed a resistance to darkness while living in a dark den. Their eyes have degenerated but they are not blinded. They prefer not to go over a wall that stands in their way but to dig through it.'):
        "Una superbestia che, a furia di vivere in tane buie, si è fatta resistente alle tenebre. Gli occhi le si sono atrofizzati, tanto che accecarla non serve a niente. Un muro che le si para davanti non lo scavalca: lo sfonda scavando.",

    # ---------------------------------------------------------- :7206 la talpa gigante
    (7206, "A giant mole. It has a nest as vast as Nefia's and is actually inhabited by other monsters. There's also a species called the gigamole which is 10 times the height and 1000 times the weight but it doesn't come to the surface."):
        "Una talpa enorme. Scava tane vaste quanto una Nefia, e infatti capita che ci vengano ad abitare altri mostri. Esiste anche una specie alta dieci volte tanto e mille volte più pesante, la talpa colossale, ma quella in superficie non sale mai.",

    # ---------------------------------------------------------- :7219 lo spadaccino magico degli Elea
    (7219, 'Elea honed their sword skills in order to fight the unreasonable violence that accompanies persecution. They were harassed in their home forest where many of the anti-war protesters were and were persecuted outside the forest eventually being forced to live in Nefia.'):
        "Un Elea che ha affinato la spada per battersi contro la violenza insensata delle persecuzioni. Nella foresta natia, dove quasi nessuno ama la guerra, lo guardavano storto; fuori dalla foresta lo perseguitavano; e alla fine non gli è restato che andare a vivere nelle Nefia.",

    # ---------------------------------------------------------- :7232 il gran saggio degli Elea
    (7232, 'They are the wisest of the Elea. Not caring about the persecution of the world they travel to Nefia and seek to unravel its secrets.'):
        "Sono i più sapienti fra gli Elea. Delle persecuzioni del mondo non si curano affatto: girano le Nefia di ogni angolo della terra e cercano di strapparne i segreti.",

    # ---------------------------------------------------------- :7245 il Mishaguji
    (7245, 'A white serpent that harbors a piece of a god. Because of its rarity and beauty it is regarded as a good omen in some areas but it attacks ruthlessly.'):
        "Un grande serpente bianco che porta in sé una scheggia di divinità. Per quanto è raro e per quanto è bello lo tengono di buon auspicio, e in certe regioni arrivano perfino a venerarlo; però attacca senza pietà.",

    # ---------------------------------------------------------- :7258 l'Ek Chuah
    (7258, 'A descendant of a fallen war god who was defeated by Tezcatlipoca. Its name means black scorpion. They are large and fearsome but not poisonous. Chocolate is their favorite.'):
        "Discende dal dio della guerra che un tempo fu sconfitto da Tezcatlipoca e cadde dal cielo. Il suo nome vuol dire scorpione nero. È grosso e ha un aspetto spaventoso, ma velenoso non è. Va matto per il cioccolato.",

    # ---------------------------------------------------------- :7271 l'ambystoma
    (7271, 'An amphibian native to the Melkawn region of South Tyris. Because of their cute idiot appearance they are exported all over the world as pets and emergency food. It has a weak toxic mucous membrane that stings when touched with bare hands.'):
        "Un anfibio originario della regione di Merca, a Tyris del Sud. Ha un'aria così scema da riuscire tenera, e per questo lo esportano in tutto il mondo come animale da compagnia e come scorta per la fame. La sua mucosa è un po' velenosa: a toccarlo a mani nude formicolano.",

    # ---------------------------------------------------------- :7284 l'anima del demone
    (7284, 'The end of the soul that was sold to the devil. It is said that the pain of death is experienced by the demon over and over again but at some point it turns into a pleasure.'):
        "È quel che resta di un'anima venduta al demonio. Il demone le fa assaggiare il dolore della morte una volta dopo l'altra, e si dice che a un certo punto quel dolore si tramuti in piacere.",

    # ---------------------------------------------------------- :7297 l'ipomicete
    (7297, 'A horrible-looking child entity that is born as a parasite of another mushroom family. Lacking self-awareness as a decomposer they try to capture the creature with sticky spores and mycelium and feed on it directly.'):
        "Un corpo fruttifero dall'aspetto orribile, che nasce parassitando gli altri funghi. Che il suo mestiere sia decomporre pare non essersene accorto: con spore e micelio appiccicosi cattura le creature vive e cerca di nutrirsene direttamente.",

    # ---------------------------------------------------------- :7310 il moai blu
    (7310, 'A mysterious human-faced rock powered by lost technology. The laser fired like crazy from the eyes is so powerful that at maximum power an Indian elephant would vaporize in two seconds.'):
        "Un misterioso masso dal volto umano, mosso da una tecnologia perduta. Il laser che spara dagli occhi come un forsennato è potente: alla massima potenza fa evaporare un elefante indiano in due secondi.",

    # ---------------------------------------------------------- :7323 il moai
    (7323, 'A mysterious human-faced rock powered by lost technology. A laser cannon is hollowed out of the rock and built into the interior and people are wondering when in the world such a thing was made.'):
        "Un misterioso masso dal volto umano, mosso da una tecnologia perduta. Qualcuno si è preso la briga di scavare la roccia e di montarci dentro un cannone laser: chi l'abbia fatto, e quando, resta un mistero per tutti.",

    # ---------------------------------------------------------- :7336 il draco maledetto
    (7336, "Using its dragon complex as a springboard it has finally become stronger than the higher ranked dragons. However the world's perception of it as lower class than a dragon did not change and it cursed everything in despair."):
        "Un draco che, facendo leva sul complesso che aveva verso i draghi, si è dato da fare fino a diventare più forte dei draghi di rango alto. Ma per il mondo è rimasto una cosa di grado inferiore al drago, e allora, disperato, ha preso a maledire e a odiare ogni cosa.",

    # ---------------------------------------------------------- :7349 il drago di sangue dagli occhi morti
    (7349, 'The idea that the rotting decaying muscles of a corpse would literally only make it a dead weight was given a skulling. Naturally as the name implies the eyes are dead.'):
        "Lo hanno ridotto a scheletro perché si è pensato che, coi muscoli marci e sfiniti di un cadavere, sarebbe stato alla lettera soltanto peso morto. E, come dice il nome, ha gli occhi morti: c'era da aspettarselo.",

    # ---------------------------------------------------------- :7362 la necrobambola
    (7362, "It improved the resurrection spell to auto-activate on death and cast it on itself but it failed. This is what it's become. It had absolute confidence in its magical skills and didn't experiment much."):
        "Aveva perfezionato la magia di resurrezione perché scattasse da sola alla morte e se l'era lanciata addosso; ma qualcosa è andato storto, ed è finita così. La colpa è della fiducia cieca che aveva nella propria arte: di prove, in pratica, non ne aveva fatte.",

    # ---------------------------------------------------------- :7375 <Lenas> l'investigatrice della Gilda dei Maghi
    (7375, 'She is on secondment from the headquarters of the Mage Guild to investigate the workings of the guild staff in South Tyris. Her dream is to start a chapter one day and become its president.'):
        "È distaccata qui dalla sede centrale della Gilda dei Maghi per controllare come lavorano gli iscritti a Tyris del Sud. Il suo sogno è aprire prima o poi una filiale e dirigerla.",

    # ---------------------------------------------------------- :7388 <Naga> l'investigatrice della Gilda dei Ladri
    (7388, 'She is on secondment from the Thieves Guild headquarters to investigate the workings of the guild staff in South Tyris. She grew up in a favela and adapted to the slums of Melkawn without difficulty.'):
        "È distaccata qui dalla sede centrale della Gilda dei Ladri per controllare come lavorano gli iscritti a Tyris del Sud. È cresciuta in un quartiere di poveri e ai bassifondi di Melkawn si è abituata senza fatica.",

    # ---------------------------------------------------------- :7401 <Ratin> l'investigatrice della Gilda dei Guerrieri
    (7401, 'She is on secondment from Warrior Guild Headquarters to investigate the workings of guild staff in South Tyris. She joined because of her admiration for Guildmaster Fray and is unhappy with the current situation of not being able to see her.'):
        "È distaccata qui dalla sede centrale della Gilda dei Guerrieri per controllare come lavorano gli iscritti a Tyris del Sud. Si era iscritta per l'ammirazione che aveva verso Fray, la maestra della gilda, e che adesso non possa vederla le va di traverso.",

    # ---------------------------------------------------------- :7414 il serafino
    (7414, 'An angel with three pairs of wings totaling six wings. Belonging to the highest ranks of the Angel Tribe they can hover by flapping their six wings skillfully but it is said to be quite tiring.'):
        "Un angelo con tre paia di ali, sei in tutto. Appartiene al grado più alto della stirpe angelica. Battendo con destrezza le sei ali riesce a restare fermo a mezz'aria, ma pare che sia parecchio faticoso.",

    # ---------------------------------------------------------- :7427 la dominazione
    (7427, 'When viewed as a whole angels belong to the upper middle class. Its name means to rule and control but it is actually a middle management position. Today they are still suffering from the unreasonable demands of their bosses and the care of their subordinates.'):
        "Fra tutti gli angeli sta in un grado medio-alto. Il suo nome significa governare e dominare, ma di fatto è un quadro intermedio. Anche oggi si strugge fra le pretese impossibili dei superiori e le grane dei sottoposti.",

    # ---------------------------------------------------------- :7440 il principato
    (7440, 'An angel of a rather low rank. They are still immature and like humans they fail and grow. They even burp and fart. Even angels are not perfect and fastidious.'):
        "Un angelo di grado piuttosto basso. È ancora acerbo e, come gli uomini, sbaglia e cresce. Rutta e scoreggia pure. Perché nemmeno un angelo è una creatura perfetta e immacolata.",

    # ---------------------------------------------------------- :7453 il padangu
    (7453, 'The wolf was originally released into the labyrinth to kill criminals but after receiving food from animal-loving criminals it became friendly. It continued to fight other demons in cooperation with the sinners and acquired a high fighting power.'):
        "In origine era un lupo lasciato nel labirinto perché facesse fuori i condannati, ma a furia di ricevere cibo da quelli che amavano gli animali è diventato affettuoso. Ha continuato a battersi contro gli altri mostri insieme ai condannati, e così ha messo su una gran forza in combattimento.",

    # ---------------------------------------------------------- :7466 il cane pastore
    (7466, 'It combines outstanding agility speed and patience. As a trainer they use their agility to guide the scattered flocks of sheep and bring them to the farm.'):
        "Mette insieme agilità, velocità e pazienza fuori dal comune. Se lo si mette alla riproduzione, sfrutta la sua prontezza per radunare le pecore sparse e riportarle all'allevamento.",

    # ---------------------------------------------------------- :7479 il fantasma galattico
    (7479, 'The armor in which the ghosts dwelt and began to move. Awakening to the power of the galaxy the solitary wave generated by its punch accelerates a 10000-volt plasma spiral to the theoretical limit of infinity.'):
        "Un'armatura in cui si è insediato uno spettro e che ha cominciato a muoversi. Risvegliata alla forza della galassia, dal suo pugno nasce un'onda solitaria che accelera una spirale di plasma da diecimila volt fino, in teoria, all'infinito.",

    # ---------------------------------------------------------- :7492 il mimic del caos
    (7492, "A demon that mimics an item. It strikes inattentive adventurers with an attack that has the power of chaos. There's nothing more pleasurable than watching an adventurer stunned by what's going on."):
        "Un mostro che si camuffa da oggetto. Quando un avventuriero distratto gli si avvicina tutto tranquillo, lo assale con un attacco che nasconde dentro la forza del caos. Non c'è piacere più grande, per lui, che vederlo lì impalato senza capire cosa gli stia succedendo.",

    # ---------------------------------------------------------- :7505 lo shoggoth
    (7505, 'A viscous creature that was used as a slave in the early First Age civilizations. Although they revolted and were subdued after a fierce battle many individuals have survived to this day due to their high survival ability.'):
        "Una creatura vischiosa che nella civiltà della Prima Era veniva usata come schiava. Si ribellò e, dopo una battaglia durissima, fu piegata; ma sa sopravvivere così bene che molti esemplari sono arrivati fino a oggi.",

    # ---------------------------------------------------------- :7518 il dragonewt supremo
    (7518, 'A half-dragon warrior awakened by fury. Its power surpasses man and dragon even approaching gods. In recent years there have been an increasing number of cases of awakening as the hybridization of humans and dragons has increased.'):
        "Un guerriero mezzo drago che si è risvegliato per un'ira violentissima. La sua forza supera quella degli uomini, supera quella dei draghi e arriva a sfiorare quella degli dei. Negli ultimi tempi i casi di risveglio aumentano, di pari passo col sangue di uomini e draghi che si mescola.",

    # ---------------------------------------------------------- :7531 l'Ah Mucencab
    (7531, "The goddess bee not the queen bee stands at the top of all bees. It's believed by ordinary bees to be devoted to a substance with the somewhat awesome name of Godroyal Jelly."):
        "Sta in cima a tutte le api: non è un'ape regina, è un'ape dea. Le api comuni la venerano e le offrono una sostanza dal nome che promette molto: pappa reale divina.",

    # ---------------------------------------------------------- :7544 <Super Gran Maestro>
    (7544, 'The strongest of grandmasters. Due to the increase in the number of Grandmasters the higher ranked ones are called by this name in order to distinguish them.'):
        "È il più potente fra i gran maestri. Siccome i gran maestri sono diventati tanti, quelli di rango più alto li chiamano così per distinguerli.",

    # ---------------------------------------------------------- :7557 l'Ungoliant
    (7557, 'A spider monster with a terrifying appetite. It eats the light and spins darkness. It became so hungry that it devoured its own offspring and mutated into a more powerful being.'):
        "Un mostro ragno dall'appetito spaventoso. Divora la luce e tesse il buio. Una volta, per la fame, fece a pezzi la propria discendenza e la mangiò: da allora è mutato in qualcosa di ancora più potente.",

    # ---------------------------------------------------------- :7570 la Kali
    (7570, 'It harbors a piece produced from the head of the goddess of battle. They love blood booze and slaughter especially blood and they love to shed it and drink it.'):
        "Porta in sé una scheggia nata dalla fronte della dea della guerra. Va matta per il sangue, per il vino e per la strage; e il sangue in particolare le piace versarlo, farlo versare e berlo.",

    # ---------------------------------------------------------- :7583 il malocchio di Balor
    (7583, 'One eye of God. Even if it is gouged out and weakened its magic power is tremendous and it is said to be able to cause storms and burn the sea.'):
        "È l'occhio di un dio. Per quanto sia stato cavato via e si sia indebolito, il suo potere magico resta tremendo: si dice che possa scatenare tempeste e bruciare il mare fino a prosciugarlo.",

    # ---------------------------------------------------------- :7596 il Sugaar
    (7596, 'A great serpent born from a piece of the god who controls storms and thunder. It is a womanizer and when it is aroused it storms around transforming its own body into a lightning bolt.'):
        "Un grande serpente nato da una scheggia del dio che comanda le tempeste e il fulmine. È un donnaiolo, e quando si accende scatena una tempesta, tramuta il proprio corpo in una saetta e sfreccia dappertutto.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-015.jsonl'
DA, A = 7101, 7600
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
