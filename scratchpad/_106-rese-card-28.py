# -*- coding: utf-8 -*-
"""106a - Lotto 28 di `db_card.hsp`: le carte fra la riga 13601 e la 14100 (39).

⚠️ **UNA sola carta ha l'inglese che finisce con uno SPAZIO**: `:13942`.

⭐⭐⭐ **`:14085` DICE CHE UN NOME DEL DIZIONARIO E' SBAGLIATO, E NON E' UNA
SVISTA DI OGGI.** La carta di `CREATURE_ID_PUPPY` (`パピー` / `puppy`, creatura
201) e' resa nel dizionario **«il cucciolo di cane»**, e la sua prosa dice
野菜の南瓜が変異して生まれた: e' una **zucca**. Non e' un doppione di monte —
il sorgente lo conferma tre volte:

    db_card.hsp:14092    `xy2pic(11, 8)` col tint GIALLO, cioe' **lo stesso
                         disegno** della パンプキン di `:14078`, ricolorato
    db_creature:120076   il blocco di `CREATURE_ID_PUPPY`
    db_creature:120100   `dbidn = "mandrake"` — la **razza** e' quella della
                         mandragora, come la zucca di `:120061`

⚠️ Quindi «cucciolo di cane» viene dalla parola inglese `puppy` e non dalla
creatura: e' la stessa forma dei quattro sbagli della 105a — una resa presa dove
il dato non sta. 🔶 **Il nome NON si cambia qui**: sta in due file e lo legge il
giocatore, e va deciso insieme al `かたつむり` del lotto 22. La **prosa** invece
si rende dal giapponese, e dice zucca.
ⓘ E' la carta stessa a smentire il nome: la prosa e' la sola cosa nel progetto
che dica cos'e' quella creatura.

⚠️ `:14072` e `:14085` aprono con la **stessa frase**, 野菜の南瓜が変異して生まれた,
e si scrivono uguali: «È nata dalla mutazione della zucca da orto».

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `イルヴァ` → **Irva**,
`ネフィア` → **le Nefia**, `ヨウィン` → **Yowyn**, `ミーア` → **Mia**
(`chat.hsp`), `ミラル` → **Miral** e `ガロク` → **Garok**, `ポピー` → **Poppy**
(ed e' il cagnolino del lotto 27, `:13591`: le due carte si leggono insieme),
`ブレイド` → **la lama**, `放電雲` → **la nube elettrica** (coniata nel lotto 25,
`:12226`, e `:14020` e' la carta che la richiama), `機械文明` → **la civiltà
meccanica**, `エーテル` → **l'etere**, `南瓜` → **la zucca**.

ⓘ **Coniato qui:** `邪眼` → **il malocchio** (`:14007`).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :13604 <Rilian> la bambina che adora i cani
    (13604, 'A dog-loving girl with a reputation in the neighbourhood. She loves her dog Poppy very much, but the dog seems a little depressed and sometimes escapes when she is out of sight.'):
        "Una bambina che ama i cani, e nel vicinato lo sanno tutti. Stravede per Poppy, il suo cane, ma il diretto interessato pare la trovi un po' soffocante, e ogni tanto, appena lei distoglie lo sguardo, scappa via.",

    # ---------------------------------------------------------- :13617 <Tam> il nemico dei gatti
    (13617, 'A young man who hates cats. Cats are very popular creatures in Irva, so he has a narrow shoulder to lean on. He used to live in Palmia but moved to Yowyn after neighbourhood problems with Mia.'):
        "Un giovane che non sopporta i gatti. In Irva i gatti sono creature amatissime, e per questo lui se ne sta con la coda fra le gambe. Prima viveva a Palmia, ma dopo i guai di vicinato con Mia si è trasferito a Yowyn.",

    # ---------------------------------------------------------- :13630 la bambina
    (13630, "Usually the term 'little girl' refers to all women who have not fully grown up. They are also common as pets in Irva, and can be bought as slaves. Escaped individuals can be captured in the wild."):
        "Il nome indica in generale le donne che non sono ancora diventate adulte. In Irva sono comuni anche come animali da compagnia, si possono comprare come schiave, e chi scappa e torna allo stato brado lo si può catturare.",

    # ---------------------------------------------------------- :13643 il ratto
    (13643, 'Small omnivorous animals. Due to their high fertility and their propensity to eat anything, they can breed in large numbers and devour crops.They are rather large and can challenge cats.'):
        "Un animaletto onnivoro. Con la sua grande capacità di riprodursi e con il vizio di mangiare qualunque cosa, ogni tanto si moltiplica a dismisura e divora i raccolti. Ha un corpo piuttosto grande, e capita che sfidi anche un gatto.",

    # ---------------------------------------------------------- :13656 il paguro
    (13656, 'A crustacean that makes shells and other objects its temporary home. They look like crabs but are actually prawns. Some of them carry very beautiful shells on their backs, which they may have picked up from somewhere.'):
        "Un crostaceo che si fa una casa provvisoria di una conchiglia o di quel che trova. All'aspetto sembra un granchio, ma in realtà è parente del gambero. Qualcuno se ne porta in spalla una bellissima, chissà dove raccolta.",

    # ---------------------------------------------------------- :13669 l'artista di strada
    (13669, "A wandering clown tries to perform juggling. The reason he doesn't do it in the city is apparently because he fears that the citizens will ruin it. He is so focused on power that he throws all sorts of things at the audience."):
        "Un pagliaccio errante che vuole esibirsi con la giocoleria. Non lo fa in città, pare, per paura delle critiche dei cittadini. E siccome tiene troppo all'effetto, finisce per tirare addosso al pubblico ogni sorta di cosa.",

    # ---------------------------------------------------------- :13682 <Frisia> la regina dei gatti
    (13682, 'Although she is a queen, she dislikes wearing noble clothes because they make it difficult to move around. The cats in her household also live a carefree life and do not feel like royalty. Perhaps because they have bad memories, they run away in a hurry when you try to touch their tails.'):
        "È una regina, ma i vestiti nobili non li sopporta perché le impediscono di muoversi. Anche i gatti del suo seguito vivono come gli pare, e di casa reale non hanno proprio l'aria. Sarà per qualche brutto ricordo, ma appena provi a toccarle la coda scappa via di corsa.",

    # ---------------------------------------------------------- :13695 la sorella minore
    (13695, 'A younger sister who is not blood-related to you. A younger sister is a younger sister because she is a younger sister, nothing more, nothing less. Therefore, she is definitely your younger sister.'):
        "La tua sorella minore, che non ha il tuo sangue. Una sorella minore è una sorella minore perché è una sorella minore, né più né meno. E quindi questa qui è senza ombra di dubbio la tua sorella minore.",

    # ---------------------------------------------------------- :13708 la sorella minore
    (13708, "Your younger sister, who is not blood-related to you, sells affectionate lunches in her sister's pavilion. She is the younger sister of all the older brothers and sisters in this world. It is unclear how long both the pavilion and the person in question have existed."):
        "La tua sorella minore, che non ha il tuo sangue, e che al padiglione delle sorelle vende pranzi al sacco pieni d'affetto. È, si potrebbe dire, la sorella minore di tutti i fratelli e le sorelle maggiori di questo mondo. Da quando esistano lei e il padiglione, non si sa.",

    # ---------------------------------------------------------- :13721 la sorella gatta minore
    (13721, 'A non-blood related younger sister-in-law of a capricious cat family. Very curious, but therefore often injured. Dislikes static electricity when she takes off her blazer.'):
        "Una sorella acquisita, di stirpe felina e capricciosa, che non ha il tuo sangue. È curiosissima, e proprio per questo si fa spesso male. Non sopporta la scossa di statica quando si toglie il blazer.",

    # ---------------------------------------------------------- :13734 la giovane dama
    (13734, 'A naive young lady. Having grown up in a venerable family, she tries to remember elegant gestures even if there is fighting. She enjoys concocting weird medicines.'):
        "Una signorina che non sa niente del mondo. È cresciuta in una famiglia di antico lignaggio, e perciò bada a non dimenticare i gesti eleganti nemmeno se si combatte. Il suo passatempo è mescolare medicine sospette.",

    # ---------------------------------------------------------- :13747 <Utima> l'arma distruttrice di Xeren
    (13747, 'A legacy of an ancient mechanical civilisation that has endlessly defended the Castle of Chaos south of Palmia. Although every part of the machine has deteriorated over the years as it has been running for many years, it still boasts an astonishing fighting power.'):
        "Un lascito dell'antica civiltà meccanica, che senza sosta continua a difendere il castello del caos a sud di Palmia. Sta in funzione da tanti anni e ogni sua parte è logorata dal tempo, eppure vanta ancora una potenza di combattimento prodigiosa.",

    # ---------------------------------------------------------- :13760 <Azzrssil> l'impuro
    (13760, 'He serves an old evil god. Under the name of his god, he is an abomination who has deviated from the boundaries of humanity with his impure external laws. He is now shut up in the Castle of Chaos, endlessly researching magic.'):
        "Serve un antico dio malvagio. Nel nome di quel dio, con arti immonde e proibite, è uscito dal recinto dell'uomo ed è diventato una presenza da aborrire. Adesso se ne sta chiuso nel castello del caos, a studiare magia senza fine.",

    # ---------------------------------------------------------- :13773 l'organizzatore dell'arena delle bestie
    (13773, 'The arena was set up for pets, inspired by the way aristocrats let their pets fight private battles to satisfy their self-esteem. Although they look like beastmen, they are actually stuffed mascot characters.'):
        "Ha aperto un'arena per gli animali da compagnia, prendendo spunto dai nobili che, per soddisfare il proprio orgoglio, fanno duellare i rispettivi animali. Ha l'aspetto di un uomo bestia, ma in verità è un costume da mascotte.",

    # ---------------------------------------------------------- :13786 <Garok> il fabbro leggendario
    (13786, 'A taciturn blacksmith with legendary skills. The objects he makes are rugged and uniform in form, but they are all highly practical equipment and items. He and Miral have been friends since childhood.'):
        "Un fabbro taciturno, con un'abilità da leggenda. Quel che fabbrica ha forme rozze e tutte uguali, ma sono equipaggiamenti e oggetti di grande utilità. Con Miral si trascina dietro un'amicizia scomoda fin da bambini.",

    # ---------------------------------------------------------- :13799 <Miral> il fabbro leggendario
    (13799, 'A cheerful blacksmith with legendary skills. He is capricious and only does work he likes, but his playful creations have many fans. Loves cats.'):
        "Un fabbro allegro, con un'abilità da leggenda. È lunatico e lavora solo a quel che gli piace, ma i suoi pezzi, pieni di estro, hanno molti ammiratori. Va matto per i gatti.",

    # ---------------------------------------------------------- :13812 il gatto dai due codini
    (13812, 'A cat with two tails. It is highly intelligent and was the first non-human creature confirmed to worship a deity. They do not taste like prawns when eaten.'):
        "Un gatto che si riconosce per le due code. Ha un'intelligenza alta, ed è il primo essere vivente non umano di cui si sia accertato che venera una divinità. A mangiarlo, comunque, non sa di gambero.",

    # ---------------------------------------------------------- :13825 il lupo d'argento
    (13825, 'Wolves with beautiful fur. In fact, despite its appearance, it has a milder temperament than a hound and its attacks are not as ferocious. It seems more grey than silver.'):
        "Un lupo dal pelo bellissimo. A dispetto dell'aspetto ha in realtà un temperamento più mite di quello di un segugio, e nemmeno i suoi attacchi sono così feroci. Più che argento, viene da dire grigio.",

    # ---------------------------------------------------------- :13838 l'infermiera
    (13838, 'An angel in white with a passion for healing the wounded. She was too motivated to wait for the wounded to show up, and as a result she threw herself into the battlefield.'):
        "Un angelo in camice bianco, che arde di passione per guarire chi è ferito. Aveva talmente voglia di darsi da fare che non riusciva ad aspettare l'arrivo dei feriti, e alla fine si è buttata lei stessa nel campo di battaglia.",

    # ---------------------------------------------------------- :13851 il riccone
    (13851, 'A person who has no rank but has acquired wealth and power in a variety of ways. Tales of the rise of the first generation are sometimes circulated and retold as very interesting and entertaining reading.'):
        "Uno che, pur senza avere un titolo, con i mezzi più vari si è procurato ricchezza e potere. Il racconto della scalata del capostipite ogni tanto circola come lettura curiosa e divertente, e si tramanda.",

    # ---------------------------------------------------------- :13864 il rampollo
    (13864, 'As they are often terrorised at the same time as making their social debut, a knowledge of combat is part of their mandatory education. Every day he looks out of the window at the children playing freely in the streets and envies them.'):
        "Siccome capita spesso di finire in un attentato proprio il giorno del debutto in società, saper combattere fa parte dell'istruzione obbligatoria. E ogni giorno guarda dalla finestra i bambini che giocano liberi per la città, e li invidia.",

    # ---------------------------------------------------------- :13877 il turista
    (13877, 'Driven by a strong sense of curiosity, there are people who travel around to see different parts of the country. Because they are easily distracted by objects of interest, being the victim of pickpocketing has become an everyday occurrence.'):
        "Gente che, spinta da una curiosità forte, va in giro a vedere posti su posti. La testa gli va subito dietro a quello che li incuriosisce, e così finire derubati da un borsaiolo è diventato pane quotidiano.",

    # ---------------------------------------------------------- :13890 il turista della festa
    (13890, "They came from faraway countries after hearing about a big festival. They don't seem to attach much importance to what the festival is about, but come to enjoy the stalls and atmosphere."):
        "È arrivato da un paese lontano, dopo aver sentito che c'era una gran festa. Di che festa sia gli importa poco: viene per godersi le bancarelle e l'aria che tira.",

    # ---------------------------------------------------------- :13903 la lama
    (13903, 'Mechanical soldiers excavated from ruins. A killer machine with sharp blades in both hands that mercilessly mutilate all living creatures.By inverting and transforming its arms, a humanoid hand appears, which can also hold other weapons.'):
        "Un soldato meccanico dissotterrato dalle rovine. È una macchina che uccide, con una lama affilata in ciascuna mano, e fa a pezzi senza pietà qualunque essere vivente. Ribaltando e trasformando le braccia gli spunta una mano come quella umana, e così può impugnare anche altre armi.",

    # ---------------------------------------------------------- :13916 la lama alfa
    (13916, 'A refurbished version of the Blade with improved capabilities. Only those who know the difference can tell the difference.It should be noted that a small number of the Blade series are equipped with a blade-resistant waistplate for testing purposes.'):
        "Una lama rimessa a punto e migliorata nelle capacità. La differenza la coglie soltanto chi se ne intende. Da notare che nella serie delle lame ne esistono alcune, poche, con un paraschiena resistente al taglio, montato per le prove.",

    # ---------------------------------------------------------- :13929 la lama omega
    (13929, 'A mechanical soldier improved to more efficiently and brutally slaughter living creatures. Its body is stained red from the blood returning to it, and even its original colour is no longer recognisable.When the blade becomes dull, it breaks off by itself and a new blade grows back.'):
        "Un soldato meccanico migliorato per massacrare gli esseri viventi in modo più efficiente e più crudele. Il corpo è tinto di rosso dal sangue schizzato addosso, e ormai non si capisce nemmeno di che colore fosse. Quando la lama perde il filo si spezza da sola, e ne spunta una nuova.",

    # ---------------------------------------------------------- :13942 <Moto di Kaneda>
    (13942, 'Legendary monster machine, with systems such as ABS, anti-obstacle radar and auto-navigation, plus an engine producing over 200 hp at 12,000 rpm. '):
        "La leggendaria macchina mostruosa. Oltre a sistemi come l'ABS, il radar contro gli ostacoli e la navigazione automatica, monta un motore che a dodicimila giri dà più di duecento cavalli. ",

    # ---------------------------------------------------------- :13955 il Cub
    (13955, 'Mechanical horses that are not only robust and fuel-efficient, but also have high vitality and speed. They are not handled in horse stalls because of the different way they are cared for.'):
        "Un cavallo meccanico che non è soltanto robusto e parco di carburante, ma ha anche una grande forza vitale e una bella velocità. Va accudito in un altro modo, e perciò nelle stalle non lo trattano.",

    # ---------------------------------------------------------- :13968 il cane mina
    (13968, 'Named after the dog-like appearance of the mines that it impatiently buries, adventurers who see it in the flesh usually twist their heads at its strange appearance. Has a built-in gravity generator.'):
        "Il nome gli viene dal fatto che, mentre sotterra mine una dopo l'altra, somiglia a un cane; ma gli avventurieri che lo vedono dal vivo di solito storcono la testa davanti a quella forma strana. Dentro ha un generatore di gravità.",

    # ---------------------------------------------------------- :13981 la vergine di ferro
    (13981, 'A mechanical, fully automatic execution tool. When attacked, it opens a door in its torso, and then counterattacks by piercing the attacker with a sharp needle attached to its interior.'):
        "Uno strumento di esecuzione meccanico e tutto automatico. Quando lo attacchi apre lo sportello del busto e risponde infilzando chi lo ha colpito con gli aghi affilati montati all'interno.",

    # ---------------------------------------------------------- :13994 l'occhio deforme
    (13994, 'Its body is so tainted with madness that just one bite would drive it insane. It has the special ability to change the body of its opponents.'):
        "Il suo corpo è intriso di follia, e basterebbe un morso solo per uscire di senno. Ha il potere speciale di trasformare il corpo di chi ha davanti.",

    # ---------------------------------------------------------- :14007 l'occhio impuro
    (14007, "It has a cloudy eye called the evil eye. Fairy hats are said to have been made to prevent physical changes caused by this monster's eye."):
        "Ha un occhio torbido, che chiamano il malocchio. Si dice che il cappello delle fate sia stato inventato apposta per impedire i mutamenti del corpo provocati dallo sguardo di questo mostro.",

    # ---------------------------------------------------------- :14020 il fuoco fatuo
    (14020, 'Discharge clouds that have exhausted their energy have taken in large amounts of ether as a replacement. It is feared as an omen of disaster and bad things are reported to happen if it is chased.'):
        "Una nube elettrica che, sputata via tutta l'energia, si è riempita in cambio di una gran quantità di etere. Lo si teme come presagio di sciagura, e si racconta che a inseguirlo succedano cose brutte.",

    # ---------------------------------------------------------- :14033 il riccio
    (14033, 'It has numerous sharp needles on its back made of body hair. A mole of the same name once existed, but this one is already extinct and is a completely different species.'):
        "Porta sulla schiena tanti aghi affilati, fatti di pelo. Un tempo esisteva una talpa con lo stesso nome, ma quella si è già estinta, ed erano comunque due specie del tutto diverse.",

    # ---------------------------------------------------------- :14046 il riccio splendente
    (14046, 'A hedgehog with a large amount of ether stored in its body due to its feeding habits. The needles on its back are hard but brittle, and if they puncture, they leave fragments in the body.'):
        "Un riccio che, per via di quello che mangia, ha accumulato in corpo una gran quantità di etere. Gli aghi della schiena sono duri ma fragili, e quando ti si conficcano dentro ci lasciano delle schegge.",

    # ---------------------------------------------------------- :14059 la gallina
    (14059, 'A popular domesticated bird because of its frequent egg-laying. Escaped individuals are often found in the wild. They have a rough temperament, but not so rough that they can repel a adventurer who messes with them.'):
        "Un uccello molto apprezzato come animale da cortile, perché fa uova di frequente. Chi scappa spesso torna allo stato brado. Ha un caratteraccio, ma non al punto da respingere un eroe che vada a stuzzicarlo.",

    # ---------------------------------------------------------- :14072 la zucca
    (14072, 'It is a mutated form of the vegetable pumpkin. It is customary for parents to feed it to their children as the rich nutritional content is good for the brain and makes them mentally lucid.'):
        "È nata dalla mutazione della zucca da orto. Le sostanze nutrienti che contiene in abbondanza fanno bene alla testa e schiariscono le idee, e per questo c'è l'usanza di darla da mangiare ai figli.",

    # ---------------------------------------------------------- :14085 ⚠️ la carta di «puppy», che e' una zucca
    (14085, 'It is a mutated form of the vegetable pumpkin. It uses its transparent appearance to throw potions from a distance, but its throwing technique is still in its infancy. This is apparently because the vines are not shaped in a way that is suitable for throwing.'):
        "È nata dalla mutazione della zucca da orto. Approfitta del proprio aspetto trasparente per tirare pozioni da lontano, ma nel lancio è ancora acerba. Pare che sia perché il tralcio non ha la forma adatta a tirare.",

    # ---------------------------------------------------------- :14098 la zucca maggiore
    (14098, 'A pumpkin that grew to the size of a monster developed an ego. It was named exactly as it was by a Yowyn farmer who encountered it for the first time. As a result of his carnivorous awakening and eating animals all over the place, the fruit lost its vegetable-like taste.'):
        "Una zucca cresciuta fino a una taglia da mostro, in cui si è destata una coscienza. Il nome gliel'ha dato tale e quale il contadino di Yowyn che per primo la incontrò. Poi si è svegliata carnivora, e a furia di mangiare animali dalla sua polpa il sapore di verdura è sparito.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-028.jsonl'
DA, A = 13601, 14100
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
