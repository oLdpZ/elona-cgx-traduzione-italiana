# -*- coding: utf-8 -*-
"""106a - Lotto 27 di `db_card.hsp`: le carte fra la riga 13101 e la 13600 (38).

ⓘ **Nessuna carta di questo lotto ha l'inglese che finisce con uno spazio.** E'
il primo lotto della sessione con zero: la proprieta' e' del blocco, non del
file, e va guardata lotto per lotto.

⚠️⚠️ **QUATTRO CARTE HANNO L'INGLESE ROTTO, E LA RESA VIENE DAL GIAPPONESE.**

    :13292  キングは**尻に敷かれている**   il Re e' **sotto il tallone** della
                                          Regina; l'inglese scrive `the King is
                                          a pain in the arse` e **rovescia** chi
                                          comanda, che e' tutta la battuta
    :13435  **地のオパートス**の真似        e' il dio **Opatos della terra**;
                                          l'inglese legge 地 come «locale» e
                                          scrive `an imitation of a local opus`
    :13409  すぐに**衛生兵**を呼ぶ          衛生兵 e' il **medico da campo**;
                                          l'inglese scrive `air supports`
    :13370  **センセイ**と呼ばれる          il guardaspalle lo chiamano «maestro»
                                          per vecchia usanza; l'inglese
                                          traslittera `senshi`, che e' un'altra
                                          parola

⭐ **I sette pezzi degli scacchi si tengono ai nomi italiani gia' scelti**:
`<Pedone>`, `<Torre>`, `<Alfiere>`, `<Cavallo>`, `<Regina>`, `<Re>`. ⚠️ Percio'
`僧正` («vescovo») nella prosa di `:13266` **non** diventa «alfiere»: la carta si
chiama gia' <Alfiere>, e la prosa dice di che cosa ha la **forma**. Stessa cosa
per `馬顔の騎士` a `:13279`, che e' il cavaliere dalla faccia da cavallo, e per
`城壁` a `:13253`, che e' la muraglia.
ⓘ `キャスリング` → **l'arrocco**, `鈍足` → **la lentezza** (lo stato del gioco).

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `イルヴァ` → **Irva**,
`ネフィア` → **le Nefia**, `ジューア` → **Juere** e `イェルス` → **Yerles**
(⚠️ e la `Yerles Military` dell'inglese e' semplicemente `イェルス`: la nazione,
non un corpo con un nome proprio), `ミスリル` → **mithril**, `アダマンタイト` →
**adamantio**, `灼熱の塔` → **la Torre Rovente**, `オパートス` → **Opatos**,
`吟遊詩人` → **il menestrello**, `猫族` → **il popolo dei gatti** (coniato nel
lotto 21, e `:13539` e' la carta dove torna), `ケシー` → **Cacy**.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :13110 il golem d'oro
    (13110, 'Its body radiates a dazzling golden glow. There is no end to the number of merchants who greedily target this golem in order to make a profit, and are beaten up by the mercenaries they have hired.'):
        "Il suo corpo manda un bagliore dorato che acceca. Non si contano i mercanti che, avidi di guadagno, puntano questo golem e finiscono spianati come stoccafissi insieme ai mercenari che hanno assoldato.",

    # ---------------------------------------------------------- :13123 il golem di mithril
    (13123, 'Golem made of mithril. Its blows are so heavy that they seem to blow away the image of mithril as strong but light. It appears to be incapable of using magic.'):
        "Un golem fatto di mithril. Il colpo che sferra è talmente pesante da spazzare via l'idea che il mithril sia robusto ma leggero. La magia, a quanto pare, non sa usarla.",

    # ---------------------------------------------------------- :13136 il golem del cielo
    (13136, 'It is made of a substance that does not exist in Irva. There have been eyewitness accounts of this golem falling from the sky, and it has even been debated whether another world exists in the sky.'):
        "È fatto di una sostanza che in Irva non esiste. C'è chi giura di aver visto questo golem cadere dal cielo, e la cosa ha fatto discutere se lassù non esista un altro mondo.",

    # ---------------------------------------------------------- :13149 il golem d'adamantio
    (13149, 'It was made using rare ores sparingly. For a long time, it was even considered the most advanced species of golem, so ordinary adventurers would not be able to stand up to it.'):
        "È stato costruito senza risparmiare un minerale rarissimo. Per molto tempo è stato considerato la specie più alta fra i golem, e quindi un avventuriero qualunque non ha niente da fargli.",

    # ---------------------------------------------------------- :13162 il granchio di fuoco
    (13162, 'The crab is encased in a red, glowing flame shell. Its meat is tender and tasty, and can heal a troubled heart. Although it is fire-based, it can also live near water, just like a crab.'):
        "Un granchio chiuso in un guscio di fiamma che brilla di rosso. La sua polpa è tenera e molto saporita, e sa consolare un cuore inasprito. È di attributo fuoco, ma da buon granchio pare che riesca a vivere anche in riva all'acqua.",

    # ---------------------------------------------------------- :13175 il millepiedi di fuoco
    (13175, 'It is characterised by its eye-watering red body. Their saliva is flammable and reacts with the air through the frictional heat of their bite, causing it to burn instantly. Although extremely rare, there have been cases of wildfires started by drool.'):
        "Si riconosce per il corpo rosso che sveglia dal sonno. La sua saliva è infiammabile, e con il calore dell'attrito quando morde reagisce con l'aria e brucia all'istante. È rarissimo, ma ci sono casi di incendi di bosco appiccati da una bava.",

    # ---------------------------------------------------------- :13188 il cultista del fuoco
    (13188, 'They summon red, lower-level monsters and golems and spread flames in a dubious ritual. They go on a pilgrimage to the Burning Tower once a year.'):
        "Con un rituale sospetto evoca mostri di rango basso e golem di colore rosso e sparge fiamme tutto intorno. Pare che una volta all'anno vada in pellegrinaggio alla Torre Rovente.",

    # ---------------------------------------------------------- :13201 lo scheletro guerriero
    (13201, 'The corpse of a dead warrior, still fighting. The completely weathered, scarred, white bones remind us of the years that have passed.'):
        "Il corpo di un guerriero che, anche da morto, passa le giornate a combattere. Le ossa bianchissime, sgretolate dal tempo e piene di intacchi, fanno sentire quanti anni siano passati.",

    # ---------------------------------------------------------- :13214 lo scheletro berserker
    (13214, 'The wreckage of a mad warrior who wanted nothing more than to kill the strong and continue to fight until death. Even after his life was over, he was happy to fight, and continued to kill on instinct.'):
        "Lo scheletro di un guerriero folle che non voleva altro che uccidere ed essere ucciso dai forti, e che ha combattuto fino alla morte. Perfino finita la vita prova gioia a potersi battere, e continua a massacrare seguendo l'istinto.",

    # ---------------------------------------------------------- :13227 il missionario dell'oscurità
    (13227, 'A fanatic who believes in a pagan god, who rules over death and decay. Those who hear these words will be greatly confused by the difference in what they believe.'):
        "Un fanatico che venera il dio di una fede empia, il dio che governa la morte e la putrefazione. Chi ascolta quelle parole resterà molto turbato dalla differenza fra ciò in cui crede lui e ciò in cui crede l'altro.",

    # ---------------------------------------------------------- :13240 <Pedone>
    (13240, 'Large pieces in the shape of soldiers. They often attack in numbers, so you can never be too careful. In fact, they can only move forward, so they do their best to change direction.'):
        "Un grande pezzo che ha la forma di un soldato. Spesso attacca in tanti, e quindi non conviene distrarsi. In verità sa solo andare avanti, e allora fa una gran fatica a cambiare direzione.",

    # ---------------------------------------------------------- :13253 <Torre>
    (13253, 'A large piece in the shape of a castle wall. It stands as a wall and undertakes attacks on others. Does not appear to adopt castling rules.'):
        "Un grande pezzo che ha la forma di una muraglia. Si pianta come un muro e si prende addosso gli attacchi diretti agli altri. La regola dell'arrocco, a quanto pare, non la adotta.",

    # ---------------------------------------------------------- :13266 <Alfiere>
    (13266, 'A large piece in the shape of a monk. Tricky pieces that wreak havoc on the board with their magic arrows, bluntness and teleportation, but they are not very flexible and fragile because they fly around.'):
        "Un grande pezzo che ha la forma di un vescovo. È un pezzo furbo, che sconvolge la scacchiera con la freccia magica, con la lentezza e con il teletrasporto, ma siccome sta sempre a svolazzare non è molto flessibile ed è fragile.",

    # ---------------------------------------------------------- :13279 <Cavallo>
    (13279, "Large pawns in the shape of horse-faced knights. They specialise in long-range attacks and utilise throwing weapons to escort the king's pawns from a distance. Although factual, please don't tell him he's horse-faced."):
        "Un grande pezzo che ha la forma di un cavaliere con la faccia da cavallo. È bravo negli attacchi da lontano e, servendosi delle armi da lancio, scorta il pezzo del Re anche stando distante. Sarà pure vero, ma la faccia da cavallo non stategliela a dire.",

    # ---------------------------------------------------------- :13292 <Regina>
    (13292, "Large piece in the shape of a queen. The most powerful piece, with high mobility and the ability to use two types of magic arrows. For this reason, the King is a pain in the arse. In case you are wondering, he doesn't have a kingdom."):
        "Un grande pezzo che ha la forma di una regina. È il pezzo più forte, con una grande mobilità e due tipi di freccia magica. Per questo il Re lo tiene sotto il tallone. Sia detto per inciso: un regno vero e proprio non ce l'ha.",

    # ---------------------------------------------------------- :13305 <Re>
    (13305, 'Large pawns in the shape of a king. He has an inexhaustible army and controls the battlefield with a large number of pieces. Although it has the appearance of a king, command seems to be held by another entity.'):
        "Un grande pezzo che ha la forma di un re. Ha truppe inesauribili e domina il campo di battaglia con una gran quantità di pezzi. Ha l'aspetto di un re, ma pare che il comando ce l'abbia qualcun altro.",

    # ---------------------------------------------------------- :13318 il guerriero mercenario
    (13318, 'Nomadic warriors who utilise their abilities as warriors by taking part in wars. Some operate out of conviction, but many live from one position to another in order to earn wages.'):
        "Un uomo d'arme errante che mette a frutto le proprie doti di guerriero prendendo parte alle guerre. C'è chi agisce per convinzione, ma i più cambiano bandiera di continuo, e vivono per il salario.",

    # ---------------------------------------------------------- :13331 l'arciere mercenario
    (13331, 'Archers who use their skills as archers to make a living by taking part in conflicts. Many of them survive, as it is easy for them to flee depending on the war situation.'):
        "Un uomo d'arme che si guadagna da vivere mettendo la propria bravura di arciere al servizio delle contese. A seconda di come va la battaglia gli è facile scappare, e per questo in molti sopravvivono a lungo.",

    # ---------------------------------------------------------- :13344 il mago mercenario
    (13344, 'He makes his living by applying his knowledge as a mage to warfare. He tends to fight using both his skills as a sorcerer and a warrior in order to adapt to the war situation.'):
        "Si guadagna da vivere applicando alla guerra il suo sapere di mago. Per adattarsi a come va la battaglia tende a combattere usando insieme le doti dello stregone e quelle del guerriero.",

    # ---------------------------------------------------------- :13357 il capo della banda
    (13357, 'A leader of a gang of ruffians who make their living by attacking peddlers and robbing them of their goods. They carry their stolen cargo around with them to sell it, and sometimes the adventurers who attack them take their earnings.'):
        "Il capo di una banda di malviventi che campa assalendo i mercanti ambulanti e portando via la merce. Si porta dietro il carico rubato per rivenderlo, e ogni tanto sono gli avventurieri che lo assalgono a portargli via il guadagno.",

    # ---------------------------------------------------------- :13370 il guardaspalle della banda
    (13370, "A mercenary crackpot, employed by a band of thieves for money. They are sometimes called senshi, according to an old custom. This may be because there is something appealing about the sound of 'bouncer'."):
        "Un mercenario finito male, assoldato con del denaro da una banda di ladri. Per una vecchia usanza c'è chi lo chiama maestro. Sarà perché la parola guardaspalle ha in sé qualcosa di attraente.",

    # ---------------------------------------------------------- :13383 il sicario della banda
    (13383, 'Hitmen who try to get as close as possible to fire due to their short-sightedness. Some of them are very good at it and fire their guns in rapid succession.'):
        "Un sicario che, essendo miope da non dirsi, cerca di sparare il più da vicino possibile. Il mestiere però lo sa, e fra loro c'è anche qualcuno che spara raffiche a una velocità spaventosa.",

    # ---------------------------------------------------------- :13396 lo stregone della banda
    (13396, 'A sorcerer in a group of ruffians who raid peddlers. He often gets angry when he inadvertently uses fire magic and burns looted goods. She performs strange rituals and dyes his skin white.'):
        "Lo stregone di un gruppo di malviventi che assale i mercanti ambulanti. Gli capita spesso di usare per sbaglio la magia del fuoco, di bruciare il bottino e di prendersi una lavata di capo. Fa riti strani, e si tinge la pelle di bianco.",

    # ---------------------------------------------------------- :13409 la fanteria meccanica Yerles
    (13409, 'Soldiers belonging to the Yerles Military. They are supplied with mechanical equipment and focus on firearms and other weapons in combat. They are not good at close combat, perhaps because they rely too much on firearms, and soon end up calling in air supports.'):
        "Un soldato che appartiene a Yerles. Gli danno in dotazione un equipaggiamento meccanico, e combatte puntando sulle armi da fuoco e simili. Alle armi da fuoco si affida forse troppo, perché nel corpo a corpo se la cava male e finisce subito per chiamare il medico da campo.",

    # ---------------------------------------------------------- :13422 la fanteria meccanica scelta Yerles
    (13422, 'Soldiers belonging to the Yerles Military, who are particularly good with firearms. They wear red-coloured equipment, but it does not mean that they are three times faster.'):
        "Fra i soldati che appartengono a Yerles, quelli particolarmente bravi a maneggiare le armi da fuoco. Portano un equipaggiamento di colore rosso, ma questo non vuol dire che vadano tre volte più veloci.",

    # ---------------------------------------------------------- :13435 <Colonnello Gilbert> l'eroe di frontiera
    (13435, 'He leads the Juere Liberation Army blockading the progress of the Yerles soldiers. His bold laugh is an imitation of a local opus. He is not averse to machines per se, and uses the guns he has taken from the Yerles soldiers.'):
        "Guida l'esercito di liberazione di Juere e blocca l'avanzata dei soldati di Yerles. Quella sua risata fragorosa è un'imitazione di Opatos della terra. Le macchine in sé non gli dispiacciono, e usa i fucili strappati ai soldati di Yerles.",

    # ---------------------------------------------------------- :13448 il cannone semovente di Yerles
    (13448, 'It was developed as a self-propelled artillery gun, but as a result of too much emphasis on low cost, it could not achieve the mobility of a self-propelled artillery gun due to insufficient power output. Nevertheless, it was deployed in actual combat and used as a fixed battery.'):
        "Lo avevano progettato come cannone semovente, ma a furia di badare al costo basso la potenza non è bastata, e la mobilità di un semovente non l'ha mai avuta. Lo hanno schierato lo stesso, e lo usano come batteria fissa.",

    # ---------------------------------------------------------- :13461 il fante juere
    (13461, 'A common soldier in Juere. As a country that originally started as a group of bandits and bad guys, they are uncoordinated and not good at controlled movements as soldiers.'):
        "Il soldato comune di Juere. Il paese è nato in origine da un'accozzaglia di ladri e malfattori, e quindi non sanno stare insieme: i movimenti ordinati del soldato non sono il loro forte.",

    # ---------------------------------------------------------- :13474 lo spadaccino juere
    (13474, 'A gladiator from Juere who used to fight monsters for his life in the arena, but came to the battlefield to break free from such a situation of his own. His eyes are filled with tragic determination.'):
        "Un gladiatore di Juere che prima si giocava la vita nell'arena contro i mostri e che, per uscire da quella condizione, è sceso sul campo di battaglia. In quegli occhi c'è una determinazione che fa male a guardarla.",

    # ---------------------------------------------------------- :13487 il lanciapietre
    (13487, 'He used to be a bard for a time, but he lacked any talent and was always stoned. He turned to stone-throwing man to avenge that grudge.'):
        "C'è stato un periodo in cui faceva il menestrello, ma di talento non ne aveva un briciolo e si prendeva sempre delle sassate. Per vendicarsi di quel rancore è passato dalla parte di chi le pietre le tira.",

    # ---------------------------------------------------------- :13500 il gatto
    (13500, 'A pet animal widely kept in Irva. Why they are so cute is a mystery, but they are also agile predators. Anyone who eats its flesh is struck with a strong sense of guilt.'):
        "L'animale da compagnia più diffuso in Irva. Perché sia così tremendamente carino resta un mistero, ma ha anche l'altra faccia del predatore agile. Chi ne mangia la carne viene assalito da un senso di colpa fortissimo.",

    # ---------------------------------------------------------- :13513 il gatto d'argento
    (13513, "With its docile character and white, flowing coat, it is a very popular cat among house-owners. They are small in stature, and as adults they are not so different in size from kittens, but this is the result of breed 'improvement' through repeated and quite reckless crossbreeding."):
        "Con il carattere mite e il pelo bianco che scorre come acqua, è un gatto amatissimo da chi lo tiene in casa. È piccolo, e da adulto non è tanto più grande di un gattino, ma questo è il frutto di un miglioramento della razza fatto incrociando e reincrociando in modo davvero sconsiderato.",

    # ---------------------------------------------------------- :13526 il gatto randagio
    (13526, 'They are very mischievous and curious and will go away as soon as the parent cat takes its eyes off them. They often wander into dangerous places such as Nefia.'):
        "È di una vivacità e di una curiosità enormi, e appena la gatta lo perde di vista sparisce chissà dove. Spesso finisce per smarrirsi in posti pericolosi come le Nefia.",

    # ---------------------------------------------------------- :13539 il leone
    (13539, 'A fierce animal of the cat tribe. According to old documents, only males once had manes, but it is not known when females started to grow manes as well.'):
        "Una belva del popolo dei gatti. Secondo i testi antichi un tempo la criniera ce l'avevano soltanto i maschi, ma da quando abbia cominciato a crescere anche alle femmine non si sa.",

    # ---------------------------------------------------------- :13552 <Cacy> il domatore di gatti
    (13552, 'Mischievous cat god. He repeatedly seeks out the homes of cat-hating humans and fills them with cats. Note that both ordinary cats and lions are equally cats to Cacy.'):
        "Il dio dei gatti, e gli piace fare dispetti. Cerca le case degli uomini che i gatti non li sopportano e le riempie di gatti, e lo rifà di continuo. Da notare che, per Cacy, il gatto comune e il leone sono gatti allo stesso modo.",

    # ---------------------------------------------------------- :13565 il carbonchio
    (13565, 'Cat with a flaming red treasure ball on its forehead. It uses a strange mewing sound to deceive its prey.It is able to use magic using its gaze as a medium, perhaps due to the power of the jewel.'):
        "Un gatto che porta in fronte una gemma rossa come il fuoco. Con un miagolio strano confonde la preda. Sarà il potere della gemma, ma sa usare una magia che passa per lo sguardo.",

    # ---------------------------------------------------------- :13578 il cane
    (13578, 'Dogs live in the habitat of humans. Dogs and humans have a long history, and studies have shown that they were with humans in all civilisations that died out in prehistoric times.They are said to have weaker tail muscles than wolves.'):
        "Il cane che vive dove vive l'uomo. La storia dei cani e degli uomini è antica, e le ricerche dicono che i cani stavano con gli uomini in tutte le civiltà estinte nei tempi remoti. Pare che abbiano i muscoli della coda più deboli di quelli del lupo.",

    # ---------------------------------------------------------- :13591 <Poppy> il cagnolino
    (13591, 'Poppy is a foolish puppy who is not afraid and keeps going deeper into Nefia. Adventurers who misjudge their own strength are just like this puppy.'):
        "Poppy è un cucciolo sciocco, che non conosce la paura e continua a spingersi in fondo alle Nefia. Però anche l'avventuriero che sbaglia a misurare le proprie forze è uguale a questo cucciolo.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-027.jsonl'
DA, A = 13101, 13600
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
