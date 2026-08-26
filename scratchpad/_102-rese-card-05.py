# -*- coding: utf-8 -*-
"""102a - Lotto 5 di `db_card.hsp`: le carte fra la riga 2101 e la 2600 (38).

Vedi `scratchpad/_102-rese-card-01.py` per il meccanismo del pannello.

⭐ **Gia' deciso altrove:** `ザイール` → **Zaile**, `パルミア` → **Palmia**,
`ノースティリス` → **Tyris del Nord**, `アストラル光` → **luce astrale**,
`タートルラビット` → **il coniglio tartaruga**, `アカシックレコード` → **la
rete akashica** (`chat.hsp:18102`), `蹴り` → **Calcio** (`chat.hsp:8993`),
`連続攻撃` → **Attacchi continui** (`chat.hsp:17704`).

⚠️⚠️ **`:2487`: l'inglese appiattisce due nomi diversi.** Il giapponese dice
`ザイエルン銀行` — la banca **Zaielun** — e la sua filiale sta a `ザイール`,
**Zaile**; l'inglese scrive «the Zaile branch of the Zaile Bank», cioe' lo
stesso nome due volte. In italiano i due nomi restano due.

⭐ **`:2240` regge su una metafora che l'italiano ha uguale**: il mediatore e'
una **colomba** ed e' un **falco**. Tradurre 鳩 con «piccione» avrebbe spento
la battuta a fine carta.

⚠️ `:2357` va accordata con la carta gemella: `少女` e' **la bambina** in tutto
il progetto (`action.hsp:17211` e altre tre), e la frase le mette a confronto.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :2110 <Nancy> la vagabonda
    (2110, 'A woman who was unable to stay in her hometown due to the devastation of Etherwind and moved to Zaile after drifting from place to place. But when Zaile also ceased to be functional as a city she gave up on it and now moved to a campground.'):
        "Il vento d'etere le ha fatto tanti di quei danni che al paese natale non poteva più restare; dopo aver girovagato di qua e di là si è trasferita a Zaile. Ma anche Zaile ha smesso di funzionare come città, e allora ha tagliato corto e si è spostata all'accampamento.",

    # ---------------------------------------------------------- :2123 <Carter> il piede esperto
    (2123, "He is a veteran adventurer who boasts a strong constitution. He specializes in a combination of kicking and continuous attack. He used to be active around Palmia but after a lot of toubles he's come to think that country living is enough for him."):
        "Un avventuriero navigato, fiero delle sue gambe tenaci. È bravo a combinare Calcio e Attacchi continui. Un tempo era attivo dalle parti di Palmia, ma dopo un po' di vicende ha concluso che la vita in campagna gli basta.",

    # ---------------------------------------------------------- :2136 il coboldo cannoniere
    (2136, "Kobold Saber with even more shooting power. Its sword-like spine is further developed yet it is characterized by an even longer tail. It may be that it's still in its infancy but it's too long and can be out of balance."):
        "Un coboldo sciabolatore con la capacità di tiro ancora più sviluppata. Il corno a forma di spada è cresciuto ancora, ma quel che si nota di più è la coda diventata lunghissima. E siccome a volte è tanto lunga da fargli perdere l'equilibrio, forse è ancora una specie in mezzo al guado.",

    # ---------------------------------------------------------- :2149 il coboldo duca
    (2149, 'In the pursuit of power kobold surrenders to evil. It has black armor and a respectable horn. They\'re usually powerful yet they can still move fast and use brainwashing sound waves.'):
        "Un coboldo che, a furia di cercare la forza, si è consegnato al male. Ha un'armatura nera e un corno maestoso. È forte già di suo, ma sa anche muoversi velocissimo e usare onde sonore che lavano il cervello.",

    # ---------------------------------------------------------- :2162 il coboldo fulmineo
    (2162, 'The awesome kobold is powered up with lightning bolts. His physical abilities have increased dramatically and he is feared by ordinary kobolds as the incarnation of lightning.'):
        "Uno straordinario coboldo potenziato da una scarica di fulmini. Le sue capacità fisiche sono cresciute di colpo, e i coboldi comuni lo temono come l'incarnazione del fulmine.",

    # ---------------------------------------------------------- :2175 il coboldo sciabolatore
    (2175, 'Kobold Saber stands out with their large sword-like horn. However this horn is used as a sensor not a weapon. What is truly remarkable is the special three claws. Apparently it has evolved into a shape suitable for using a gun.'):
        "Un coboldo che si nota per il grande corno a forma di spada. Quel corno, però, non è un'arma: lo usa come sensore. La cosa davvero degna di nota sono i tre artigli speciali, che pare si siano evoluti in una forma adatta a usare un'arma da fuoco.",

    # ---------------------------------------------------------- :2188 il coboldo blu
    (2188, 'The most poisonous kind of kobolds. The blue body is beautiful enough to see. It has a habit of exuding toxins from its body to be used for hunting.'):
        "La specie di coboldo con il veleno più forte di tutte. Il corpo azzurro intenso, a guardarlo, è bello. Ha l'abitudine di far uscire tossine da tutto il corpo e di servirsene per cacciare.",

    # ---------------------------------------------------------- :2201 la coboldina
    (2201, "A variant of kobold. Maybe it's because it has some human genes in it but it doesn't have a peculiar ugliness. The kobolds hate it and the humans mistake it for a werewolf and exterminate it. They are always frightened because they think they are surrounded by enemies."):
        "Una variante del coboldo. Forse perché ha dentro qualche gene umano, le manca la durezza tipica della specie. I coboldi la trovano disgustosa; gli uomini la scambiano per una licantropa e la sterminano. Convinta di essere circondata da nemici, vive in un terrore continuo.",

    # ---------------------------------------------------------- :2214 l'invasore dell'universo
    (2214, 'Bacterial life forms are roaming the universe in search of energy. It will eat both organic and inorganic substances and try to take them in. Be careful as they approach you with a large army.'):
        "Una forma di vita batterica che vaga per l'universo in cerca di energia. Divora e assorbe senza problemi tanto la materia organica quanto quella inorganica. Attenzione, perché avanza a passo lento e in grandi eserciti.",

    # ---------------------------------------------------------- :2227 la bambola di porcellana
    (2227, "This is a doll based on the technology of a golem. The doll's parts can be magically transformed at will and this mechanism allows for seamless facial changes. The leaked magic may act on your hair and cause it to grow a little bit but don't be scared."):
        "Una bambola costruita applicando la tecnica dei golem. Con la propria volontà può deformare magicamente i pezzi di cui è fatta, e questo meccanismo le permette di cambiare espressione senza stacchi. Può capitare che il potere magico che sfugge le faccia crescere i capelli a poco a poco, ma non c'è da spaventarsi.",

    # ---------------------------------------------------------- :2240 il pacificatore
    # ⭐ 鳩 e' la **colomba** e non il piccione, se no la carta perde la battuta:
    #    e' una colomba, ed e' un falco.
    (2240, 'A mediator in the form of a pigeon. Exhausted by a long history of strife they have come to the conclusion that true peace can only be achieved through the eradication of all life. They are hawks who will use nuclear warheads for the sake of peace.'):
        "Un mediatore in forma di colomba. Sfinito da una storia di lotte lunghissima, è arrivato alla conclusione che la vera pace si ottiene solo estirpando ogni forma di vita. È un falco: per la pace userebbe anche le testate nucleari.",

    # ---------------------------------------------------------- :2253 l'uccello caduto
    (2253, 'A flightless bird with a large body and well-developed muscles. They seriously believe that long ago they were made unable to fly by a god who feared their power. Be careful not to offend them by treating them like penguins or kiwis.'):
        "Un uccello che non vola, con un corpo grande e muscoli ben sviluppati. Sostiene sul serio che in un tempo lontanissimo una divinità, temendo la sua forza, gli tolse il volo. Attenzione a non farlo arrabbiare trattandolo da parente del pinguino o del kiwi.",

    # ---------------------------------------------------------- :2266 l'assassino della foresta
    (2266, 'An owl demon that lives in the forest. Even though he has good eyes and ears he still turns his neck 270 degrees to cover multiple directions. It is very dangerous when targeting from up high with its detection power and intelligence.'):
        "Un mostro-gufo che vive nel bosco. Ha già occhi e orecchie eccellenti, e per giunta gira il collo di duecentosettanta gradi e copre più direzioni insieme. Per quella capacità di individuare e per l'intelligenza che ha, esserne presi di mira è pericolosissimo.",

    # ---------------------------------------------------------- :2279 il codibugnolo malvagio
    (2279, "Although cute in appearance she is evil in nature and has the nickname of a snow demon. They slaughter their prey by catching them off guard with their cuteness and then burrow into their bodies to gobble up their favorite meat. There is a habit of shaking one's head when thinking about Yokoshima. But it's cute."):
        "All'aspetto è tenero, ma è il male in persona, e lo chiamano anche lo spiritello della neve. Con quella tenerezza abbassa la guardia della preda, la massacra, poi le si infila dentro e si abbuffa del grasso che tanto gli piace. Quando pensa a qualche perfidia ha il vizio di piegare la testa di lato. Però è tenero.",

    # ---------------------------------------------------------- :2292 l'anatra arciera
    (2292, "She was shot by a human with a bow and arrow which killed a child and severely injured herself when the arrow went through her. She' s learned how to handle a bow and arrow for revenge and goes around killing humans. She carries a doll that resembles her child."):
        "Ha alle spalle un uomo che l'ha colpita con arco e frecce: il suo piccolo è morto e lei stessa è rimasta ferita gravemente da una freccia che l'ha trapassata. Per vendetta ha imparato a usare arco e frecce, e va in giro ad ammazzare uomini. Quella che si porta dietro è una bambola che imita il suo piccolo.",

    # ---------------------------------------------------------- :2305 l'incocorito
    (2305, "A big parakeet that used to be human. Because he didn't work hard enough and was in a rut he was transformed by his wizard mother and kicked out of the house. He thought about making a living by imitating voices but he ended up just thinking about it."):
        "Un pappagallo enorme che un tempo era umano. Siccome non lavorava e se ne stava in ozio, sua madre, che era una maga, gli cambiò l'aspetto e lo cacciò di casa. Già che c'era ha anche pensato di campare imitando le voci, ma si è fermato al pensiero.",

    # ---------------------------------------------------------- :2318 il vecchio maggiordomo
    (2318, 'A butler who has served his master for many years and has gained experience. He is old but his skill is remarkable.'):
        "Un maggiordomo che ha servito il padrone per lunghissimi anni e ne ha accumulato esperienza. Vecchio lo è, ma la sua abilità ha ancora qualcosa che lascia a bocca aperta.",

    # ---------------------------------------------------------- :2331 il maggiordomo
    (2331, 'A senior servant who works in a high-status or wealthy house. He takes care of his master and supports his work by acting as a secretary. He is very unhappy when he has to serve a selfish master.'):
        "Un domestico di rango alto che lavora presso famiglie nobili o ricche. Si occupa della persona del padrone e ne sostiene il lavoro facendogli anche da segretario. Se gli capita un padrone capriccioso, sono guai.",

    # ---------------------------------------------------------- :2344 il bambino sadico
    (2344, "A special boy who handles the whip expertly. The attacks have improved in power but his personality has also become more aggressive. He doesn't show it but he is afraid that he will be attacked."):
        "Un bambino speciale che maneggia la frusta con maestria. In attacco è diventato più potente, ma anche il carattere gli si è fatto aggressivo. Non lo dà a vedere, ma ha paura di essere attaccato lui.",

    # ---------------------------------------------------------- :2357 il bambino
    (2357, 'The word boy can also be used as a term to describe a man who is not fully grown up.Compared to the taciturn and docile girl he is mischievous and boisterous making him a less common pet.'):
        "In generale un maschio che non è ancora diventato adulto... anche se la parola, a rigore, si può usare pure per una femmina. Rispetto alla bambina, che è silenziosa e tranquilla, è vivace e chiassoso, e per questo come animale da compagnia va meno di moda.",

    # ---------------------------------------------------------- :2370 la bestia dell'oblio
    (2370, 'The Goddess of Oblivion incarnate. They appear in a world where the flow of destiny is interrupted and multiply by eating all sorts of memories. The initial response is crucial. If left alone people and the world will die in the truest sense of the word.'):
        "L'incarnazione della dea dell'oblio. Compare nei mondi in cui il flusso del destino si è interrotto, e si moltiplica divorando ogni sorta di ricordi. Quel che conta è intervenire subito: se la si lascia fare, gli uomini e il mondo muoiono nel senso vero della parola.",

    # ---------------------------------------------------------- :2383 l'ombra residua
    (2383, 'The inhabitants were once alive and well but their memories have eaten away and their very existence has faded away. A state where the barely remaining remnants of existence create a shadow in the astral light.'):
        "Erano abitanti che vivevano pieni di vita, ma i ricordi glieli hanno divorati e la loro stessa esistenza sta svanendo. È lo stato in cui il residuo di esistenza rimasto a stento, illuminato dalla luce astrale, proietta un'ombra.",

    # ---------------------------------------------------------- :2396 il coniglio
    (2396, 'A wild animal that lives in North Tyris towards Gaius Vis. It looks a lot like the Turtle Rabbit with a turtle shell on its back... but unlike the synthetic beast this one is the result of natural evolution. Apparently the spine developed as an external skeleton.'):
        "Un animale selvatico che vive nella Tyris del Nord dalla parte di Gaius Vis. È identico al coniglio tartaruga, con il guscio di tartaruga sulla schiena... ma a differenza di quello, che è una bestia sintetica, questo è il risultato di un'evoluzione naturale: pare che la spina dorsale gli si sia sviluppata come esoscheletro.",

    # ---------------------------------------------------------- :2409 la volpe
    (2409, 'A wild animal that lives in North Tyris towards Gaius Vis. It is characterized by a mixture of red hair. An ordinary fox with mysterious red eyes but no magical powers.'):
        "Un animale selvatico che vive nella Tyris del Nord dalla parte di Gaius Vis. La si riconosce dal pelo rosso mescolato al resto. Gli occhi rossi sono misteriosi, ma è una volpe qualunque e di potere magico non ne ha.",

    # ---------------------------------------------------------- :2422 il ratto
    (2422, "A wild animal that lives in North Tyris towards Gaius Vis. His nerves are thick and he does not run away when people approach him. That's why they're often hunted by hungry travelers."):
        "Un animale selvatico che vive nella Tyris del Nord dalla parte di Gaius Vis. Ha i nervi saldi e non scappa nemmeno se qualcuno gli si avvicina. Proprio per questo capita che i viandanti affamati lo caccino.",

    # ---------------------------------------------------------- :2435 il cinghiale
    (2435, 'A wild animal that lives in North Tyris towards Gaius Vis. His body is large and his fangs are sharp but he is as calm as he looks. Don\'t attack in a hurry even if they are suddenly approaching.'):
        "Un animale selvatico che vive nella Tyris del Nord dalla parte di Gaius Vis. Ha un corpo grosso e zanne aguzze, ma malgrado l'aspetto è tranquillo. Anche se si avvicina all'improvviso, non bisogna attaccarlo per la fretta.",

    # ---------------------------------------------------------- :2448 il lupo
    (2448, "This is an aggressive wild animal that lives in North Tyris towards Gaius Vis. It's common sense to cast a cognitive disruption spell when you're out and about since you're hanging around outside the city normally. A number of strangers have been eaten to death who didn't know that."):
        "Un animale selvatico e aggressivo che vive nella Tyris del Nord dalla parte di Gaius Vis. Gironzola tranquillamente fuori dalle città, e per uscire è buonsenso lanciarsi addosso una magia che confonde la percezione. Più di un forestiero che non lo sapeva è finito sbranato.",

    # ---------------------------------------------------------- :2461 il leone
    (2461, 'This is an aggressive wild animal that lives in North Tyris towards Gaius Vis. It is more muscular than the lion of Irva and has a yellow body color. If you can beat this guy in a match you will be recognized as a full-fledged warrior.'):
        "Un animale selvatico e aggressivo che vive nella Tyris del Nord dalla parte di Gaius Vis. È più muscoloso del leone di Irva e ha il pelo più giallo. Chi arriva ad abbatterlo in un duello a due viene riconosciuto guerriero fatto e finito.",

    # ---------------------------------------------------------- :2474 <Bysymlha> il demone dagli occhi d'ambra
    (2474, 'She was an angel who risked her life against a demon but she was caught and her whole body was altered and turned into a demon. She had not lost the consciousness she had when she was an angel so she escaped and returned to her homeland. She is horrified to realize her own demonization after she unknowingly killed her friends. She decided to leave her hometown and live quietly as a stray demon.'):
        "Era un angelo che affrontò un demone a rischio della vita, ma fu catturata, le rifecero il corpo da cima a fondo e la trasformarono in demone. La coscienza che aveva da angelo non l'aveva perduta: fuggì e tornò in patria. Poi, dopo aver ucciso i compagni senza rendersene conto, si accorse di essere diventata demone e ne restò sconvolta. Ha lasciato la sua terra e ha deciso di vivere in disparte, come demone randagio.",

    # ---------------------------------------------------------- :2487 l'ex impiegata di banca
    # ⚠️⚠️ Due nomi diversi che l'inglese appiattisce: la banca e' **Zaielun**,
    #    la citta' e' **Zaile**. Vedi il docstring.
    (2487, 'He worked in the Zaile branch of the Zaile Bank. Even now that the bank is unsustainable due to global anomalies it still holds gold coins responsibly without embezzling them.'):
        "Lavorava alla filiale di Zaile della banca Zaielun. Adesso che uno sconvolgimento su scala mondiale ha reso impossibile mandare avanti la banca, custodisce ancora con senso di responsabilità le monete d'oro che le sono state affidate, senza appropriarsene.",

    # ---------------------------------------------------------- :2500 il mediatore della gilda
    (2500, 'A person who mediates requests made to the guild. They were taking brokerage fees from the people who would receive the requests and were using them for operating expenses. Now that the request itself is gone the request gate is no longer maintained.'):
        "La persona che smista gli incarichi che arrivano alla gilda. Prendeva una commissione da chi accettava l'incarico e la destinava alle spese di gestione. Adesso gli incarichi non ci sono più, e così nemmeno il portale degli incarichi si riesce a tenere in ordine.",

    # ---------------------------------------------------------- :2513 il commesso
    (2513, 'He is a clerk not a shopkeeper. He doesn\'t even remember his employer anymore. Apparently they are struggling to procure goods because the distribution of goods has been cut off. Even in such a state he tries to keep the shop running for everyone.'):
        "È un commesso, non il padrone del negozio. Del suo datore di lavoro non ha più memoria. Siccome la circolazione delle merci si è interrotta, pare che faccia una gran fatica a procurarsi da vendere. Eppure, anche così, cerca di tenere aperto il negozio per tutti.",

    # ---------------------------------------------------------- :2526 il barista
    (2526, 'To make you forget your fears he still serves alcohol to the survivors to this day. As he looks at the deserted tavern he wonders if he has a special ability to revive customers.'):
        "Anche oggi offre da bere ai sopravvissuti, perché dimentichino la paura. Guardando la taverna senza più vita, si perde a fantasticare: se avesse il potere speciale di far resuscitare i clienti...",

    # ---------------------------------------------------------- :2539 <Allen> il ricercatore
    (2539, 'He belongs to a survey team sent from Palmia. Initially they were investigating the effects of the Etherwinds around the valley of Raskilis.'):
        "Fa parte della squadra d'indagine mandata da Palmia. All'inizio indagava sugli effetti del vento d'etere nei dintorni della valle di Raskilis.",

    # ---------------------------------------------------------- :2552 <Burt> l'anima ardente d'avventuriero
    (2552, 'A passionate man with a soul that burns with adventure. He also has the kindness to advise travellers visiting North Tyris. It\'s the same in a dying world.'):
        "Un uomo ardente, che nell'avventura brucia l'anima. Ha anche la gentilezza di dare consigli ai viaggiatori che arrivano nella Tyris del Nord. E questo non cambia nemmeno in un mondo che sta finendo.",

    # ---------------------------------------------------------- :2565 <Loyter> il sangue cremisi di Dole
    (2565, "A talented military man with long red hair who is hailed as a hero in Dole. However he felt ashamed because he had an opponent that he wanted to beat with his own strength. It's not like he has a particularly strong shoulder."):
        "Un militare capace dai lunghi capelli rossi, che a Dole celebrano come un eroe. C'era qualcuno che voleva battere con le proprie forze, ma quello se n'è andato prima, e lui se ne porta dietro il rammarico. Non è che abbia una spalla particolarmente forte.",

    # ---------------------------------------------------------- :2578 l'ultimo danzatore
    (2578, 'The guardian angel of the Akashic Records. Apparently when distortions accumulate in the world one releases one\'s true power. The mission is to rewind the distortions by force termination before they are recorded. One who appears in every space time dimension everywhere and finally takes to the skies.'):
        "L'angelo che fa la guardia alla rete akashica. Pare che, quando nel mondo si accumulano le distorsioni, liberi la sua vera potenza. La sua missione è riavvolgere le distorsioni con un arresto forzato prima che vengano registrate. Compare in ogni spazio, in ogni tempo, in ogni dimensione... ed è colui che alla fine danza nel cielo.",

    # ---------------------------------------------------------- :2591 il driceradops
    (2591, 'Triceratops has been slightly exposed to the pollution waves unleashed by quantum biological weapons. The limbs and horns are beginning to degenerate slightly and parts of the body are fusing with the machine. Just thinking about what would have happened if I had been immersed in the waves is terrifying.'):
        "Un triceratopo sfiorato appena dall'onda di contaminazione emessa da un'arma biologica quantistica. Zampe e corna hanno cominciato a regredire un poco alla volta, e una parte del corpo si è fusa con la macchina. A pensare che cosa sarebbe successo se si fosse immerso del tutto in quell'onda, viene paura.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-005.jsonl'
DA, A = 2101, 2600
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
