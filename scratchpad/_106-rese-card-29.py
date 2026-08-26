# -*- coding: utf-8 -*-
"""106a - Lotto 29 di `db_card.hsp`: le carte fra la riga 14101 e la 14600 (38).

⚠️ **TRE carte hanno l'inglese che finisce con uno SPAZIO**: `:14293`, `:14358`,
`:14371`.

⭐⭐⭐ **QUESTO LOTTO HA FATTO USCIRE IL TERZO NOME SDOPPIATO DELLA SESSIONE, E
QUESTO SI E' POTUTO CORREGGERE.** `:14514` nomina 元素のイツパロトル, e cercando
il nome nel dizionario prima di scriverlo e' saltato fuori che `イツパロトル` era
reso in **due** modi: **Itzpalt** 52 volte in nove file (il nome del dio in
`god.hsp:84`, la carta `:8590`, la creatura `db_creature:87235`) e **Itzparotl**
due volte, tutt'e due in `db_card.hsp` — `:8220` e `:8597`.

⚠️ **La causa e' l'inglese di monte**: solo in quelle due carte l'inglese scrive
`Itzparotl`, e chi le ha rese ha preso il nome dalla riga che aveva davanti
invece che dal dizionario. ✅ Corrette da
`scratchpad/_106-correzione-itzpalt.py`, che si ferma se le righe toccate non
sono esattamente quelle due.
ⓘ ⚠️ **Le tre grafie storpiate di `text.hsp` non si toccano**: `:549`, `:552` e
`:555` sono le risposte **sbagliate** del quiz sul nome del dio degli elementi.

⭐ **Otto carte aprono con la STESSA formula, e si scrivono uguali.**
「〜の一部にしてその下僕」 apre `:14449`, `:14462`, `:14475`, `:14488`, `:14501`,
`:14514`, `:14527` e `:14540`: «Una parte di X e insieme il suo servo». Sono gli
otto servitori delle otto divinita', e a schermo si leggono uno dietro l'altro
nel mazzo.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `イツパロトル` → **Itzpalt**,
`ヤカテクト` → **Yacatect**, `エヘカトル` → **Ehekatl**, `クミロミ` →
**Kumiromi**, `マニ` → **Mani**, `ルルウィ` → **Lulwy**, `オパートス` →
**Opatos**, `ジュア` → **Jure**, `エーテル病` → **la malattia dell'etere**
(`chat.hsp`), `ポート・カプール` → **Porto Kapul**, `ルミエスト` → **Lumiest**,
`ノイエル` → **Noyel**, `ヨウィン` → **Yowyn**, `イルヴァ` → **Irva**, `プチ` →
**il putit**, `イーク` → **lo yeek**, `妖精` → **la fata**.

ⓘ **`:14176` dice «domestica», non «cameriera».** La battuta e' la stessa di
`:9585` — in Irva si chiama cosi' anche un uomo — ma le due creature hanno nomi
italiani diversi (`メイド` e' «la domestica», `メイドさん` e' «la cameriera»), e
la prosa segue il nome della **propria** carta.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :14111 l'incubo di Halloween
    (14111, "It was born when the grudges of pumpkins that were thrown away because they were not eaten gathered together to form the shape of a pumpkin again. Perhaps that's why it doesn't taste like a pumpkin when you eat it. in October, tension rises and the smile never ceases to grow."):
        "È nato quando il rancore delle zucche buttate via senza essere mangiate si è raccolto e ha ripreso la forma di una zucca. Sarà per questo che, a mangiarlo, di zucca non sa. In ottobre gli sale l'entusiasmo e il sorriso non gli si spegne mai.",

    # ---------------------------------------------------------- :14124 il figlio del buio
    (14124, 'An aggregate of the grudges of unwanted children buried in the darkness. They take in those in the same situation as themselves, and then, in the darkness, clear out their resentment one after the other.'):
        "L'ammasso dei rancori dei bambini indesiderati, sepolti nel buio. Assorbe chi ha avuto la sua stessa sorte e, confondendosi con il buio, si toglie quelle voglie una dopo l'altra.",

    # ---------------------------------------------------------- :14137 l'eremita del buio
    (14137, 'The grudge of an old man, once called a hermit, buried in darkness. The methods he mastered during his life for eliminating signs have not diminished, and no half-hearted adventurer will be able to capture them.'):
        "Il rancore di un vecchio sepolto nel buio, che un tempo qualcuno aveva chiamato eremita. L'arte di cancellare la propria presenza, imparata da vivo, non si è indebolita, e un avventuriero mediocre non riuscirà nemmeno a stanarlo.",

    # ---------------------------------------------------------- :14150 <Ebon> il gigante di fuoco
    (14150, 'A giant who used to rule the labyrinth. He is always shivering in the snowy weather without being given any warm clothing, on the theory that he is a fire giant so he should be fine even if it is a little cold.'):
        "Un gigante che un tempo, dicono, dominava il labirinto. Con il ragionamento che, essendo un gigante di fuoco, un po' di freddo lo reggerà, lo lasciano sotto la neve senza dargli nemmeno di che coprirsi, e lui trema sempre.",

    # ---------------------------------------------------------- :14163 <Moyer> l'imbonitore
    (14163, 'He buys the giants that used to be the masters of the Belon labyrinth and makes a spectacle of them. Due to sloppy management, the giants are often unleashed as a prank and, as a result, he is often the first to be burnt.'):
        "Compra i giganti che erano padroni del labirinto di Belon e li mette in mostra. Li tiene con tanta trascuratezza che qualcuno per scherzo glieli libera, e il risultato è che il primo a essere bruciato è quasi sempre lui.",

    # ---------------------------------------------------------- :14176 la domestica
    (14176, 'There is concern that quality is declining as a result of recent cheapening. In Irva, even men are called maids. No matter how strong the adventurer, they have the determination not to let their master enter the doorway until he says he will see them.'):
        "Da quando le svendono, si teme che la qualità stia calando. Da notare che in Irva si chiama domestica anche un uomo. Per quanto sia robusto l'avventuriero, ha il fegato di non lasciarlo entrare in casa finché il padrone non dice che lo riceve.",

    # ---------------------------------------------------------- :14189 il putit corazzato
    (14189, 'Additional armaments improve their mobility and defence, and they are often more powerful than elite machine soldiers, despite being petit. To prevent them from getting lost, they use joints when marching and run like a train.'):
        "Con l'armamento aggiuntivo la mobilità e la difesa sono cresciute, e capita spesso che, pur essendo un putit, valga in battaglia più di un soldato meccanico scelto. Per non perdersi, quando marciano si agganciano con dei giunti e corrono in fila come un treno.",

    # ---------------------------------------------------------- :14202 <Gwen> l'innocente
    (14202, 'Innocent and straightforward, she run around and follows strangers. Sometimes she is badly beaten up by bad adventurers, but she still follows them to this day. What fate awaits her in the future...'):
        "È ingenua e docile, e così segue chiunque, anche chi non conosce. Ogni tanto un avventuriero cattivo le fa passare dei brutti momenti, eppure anche oggi va dietro a qualcuno. E il destino che l'aspetta più avanti...",

    # ---------------------------------------------------------- :14215 <Pael> la solitaria
    (14215, 'Her mother contracted ether disease, and while she spent all her time looking after her, she missed the opportunity to play with children her own age and became isolated. She puts her mother above all else.'):
        "Alla madre è venuta la malattia dell'etere, e a furia di passare le giornate ad accudirla ha perso le occasioni di giocare con i bambini della sua età, e si è ritrovata sola. La madre viene prima di ogni altra cosa.",

    # ---------------------------------------------------------- :14228 <Lily> la madre di Pael
    (14228, 'She was raising her only daughter by herself after her husband was eaten by putits. However, she was not immune to the ether as much as other people, and one day she fell ill with ether disease.'):
        "Il marito se l'è mangiato un putit, e da allora tirava su la figlia unica con le sue sole forze. Ma pare che all'etere fosse meno resistente di chiunque altro, perché un giorno è caduta malata della malattia dell'etere.",

    # ---------------------------------------------------------- :14241 <Raphael> il donnaiolo
    (14241, "Port Kapul's womanizer. He has a tragic backstory of not having the love of his mother when he was a child and looks for her in married women. Many people sympathise with him, but he remains an annoying, erotic old man."):
        "Il libertino di Porto Kapul. Ha un passato triste, senza l'amore della madre da bambino, e in ogni donna sposata cerca il volto di lei. In molti lo compatiscono, ma resta comunque un vecchio sporcaccione e molesto.",

    # ---------------------------------------------------------- :14254 <Ainc> il cavaliere novizio
    (14254, 'Once he properly challenged the target for elimination, but failed miserably due to the stress caused by the strain of the promotion exam. He is now traumatised by the yeeks and has nightmares every time he sleeps.'):
        "Una volta il bersaglio da abbattere lo ha affrontato per davvero, ma la tensione dell'esame di promozione gli ha messo addosso uno stress tale che ne è uscito con una sconfitta rovinosa. Adesso gli yeek sono il suo trauma, e ogni volta che dorme fa gli incubi.",

    # ---------------------------------------------------------- :14267 <Arnord> il soldato ferito
    (14267, 'He was injured in the onslaught of the Kamikaze suicide attack. His injuries at the time had long since healed, but he was reassigned and this time he was sent to defeat mutants, which resulted in constant injuries.'):
        "Si è ferito sotto l'assalto furioso del reparto suicida dei kamikaze. Quelle ferite lì sono guarite da un pezzo, ma con un cambio di destinazione adesso lo mandano ad abbattere le specie mutate, e le ferite non gli finiscono mai.",

    # ---------------------------------------------------------- :14280 <Mia> la finta ingenua
    (14280, 'As much as she loves cats, she is famous for being a bratty girl. Her true nature is... oh? Someone is knocking on my door.'):
        "Tanto quanto è famosa per amare i gatti, è famosa per fare la svenevole. La sua vera natura è... oh? Pare sia arrivato qualcuno, a quest'ora.",

    # ---------------------------------------------------------- :14293 <Renton> il mago tormentato
    (14293, 'She suffered a mental breakdown after the suicide of her younger sister, whose dreams were dashed. She is on a retreat, watching the beautiful Lumiest scenery and attending parties as a distraction. '):
        "Il suicidio della sorella minore, con i suoi sogni infranti, gli ha fatto ammalare la mente. Adesso è a riposo, e per distrarsi guarda i bei paesaggi di Lumiest e va alle feste. ",

    # ---------------------------------------------------------- :14306 <Marks> il ladro leggendario
    (14306, 'A thief of rare distinction, he was even described as a thief who could steal anything. He is the third Marks, as his grandfather Marks was also a renowned thief. He is forced to wear a mask that has been cut in half, as he is still only half a man in his father\'s eyes.'):
        "Un ladro di razza rara, di cui si diceva che non ci fosse niente che non sapesse rubare. Anche il nonno Marks era un ladro famoso, e quindi lui è il terzo Marks. A sentire il padre non vale ancora un uomo intero, e per questo gli tocca portare una maschera tagliata a metà.",

    # ---------------------------------------------------------- :14319 <Noel> la dinamitarda
    (14319, 'Her life has always been coloured by the flames of explosions and she now instinctively seeks fire. She makes bombs today in order to one day engulf everything in flames.'):
        "La sua vita è sempre stata dipinta di fiamme d'esplosione, e ormai il fuoco lo cerca d'istinto. Per avvolgere un giorno ogni cosa in una fiammata, anche oggi costruisce bombe.",

    # ---------------------------------------------------------- :14332 <Conery> il generale di Palmia
    (14332, "A serious soldier who is concerned about Palmia's national security. He asks adventurers he sees to help him defeat dangerous individuals. He is feared by his subordinates because he has a very angry temper."):
        "Un militare serissimo, in pena per la difesa di Palmia. Agli avventurieri su cui punta affida l'incarico di abbattere gli elementi pericolosi. Si arrabbia con facilità, e i sottoposti lo temono.",

    # ---------------------------------------------------------- :14345 il ladro
    (14345, "Stingy pickpocket apprenticeship. No matter what type of work you do, it's hard to get an apprenticeship. He is a fool who, perhaps lacking confidence in his own skills, returns to check on the result after he has already done the job."):
        "Un apprendista borsaiolo da quattro soldi. In qualunque mestiere, la gavetta è una cosa dura. Sarà che della propria mano non si fida, ma dopo aver svuotato una tasca torna indietro a controllare: un babbeo.",

    # ---------------------------------------------------------- :14358 il rapinatore
    (14358, 'Bandit who uses force to extort gold. They are quite annoying, as they forcefully take the money and then persistently follow you to see if you still have it. '):
        "Un ladro di infimo rango, che si prende i soldi facendo parlare la forza. Ti strappa via il denaro con le brutte e poi ti sta dietro insistendo che qualcosa devi ancora avere, e la cosa è parecchio molesta. ",

    # ---------------------------------------------------------- :14371 il ladro maestro
    (14371, 'Professional thief with numerous experiences. Very well-spoken as a result of continually selling dubious goods obtained by stealing. '):
        "Un professionista del furto, con parecchie esperienze alle spalle. A furia di rivendere la merce sospetta che si procura rubando, ha imparato a parlare benissimo. ",

    # ---------------------------------------------------------- :14384 la Grande Razza di Yith
    (14384, 'A spirit life-form that arrived from another planet. It is said to have taken over the body of a conical life-form that currently inhabits Irva and has sealed its natural enemy species deep underground.'):
        "Una forma di vita spirituale arrivata da un altro pianeta. Adesso si è impadronita del corpo delle creature coniche che abitavano in Irva, e si dice tenga sigillata nel profondo della terra la stirpe che le è nemica.",

    # ---------------------------------------------------------- :14397 la Shub-Niggurath
    (14397, 'The fertility mother goddess of the Otherworld, also known as the Black Goat of the Forest, who conceives a thousand pups. She has a history of withdrawing after a fierce battle with Kumiromi, and currently sends her weak alter ego to watch over her.'):
        "La dea madre della fertilità di un altro mondo, che chiamano anche la capra nera dei boschi dai mille figli. In passato, dopo uno scontro furioso con Kumiromi, si è ritirata, e adesso manda avanti dei suoi doppioni deboli e sta a guardare.",

    # ---------------------------------------------------------- :14410 il gug
    (14410, 'A giant who was banished to the depths of underground when he incurred the wrath of the gods. As a result of adapting to life in the narrow subterranean depths, they became somewhat smaller when they returned to the surface.'):
        "Un gigante scacciato nelle viscere della terra per aver toccato la collera delle divinità. A furia di adattarsi alla vita stretta del sottosuolo, quando è tornato in superficie si era fatto un po' più piccolo.",

    # ---------------------------------------------------------- :14423 il re della spirale
    (14423, 'In the distant past, the pagan Virgin and Child were oppressed as pagans and died by fire. The god despised as an evil god added the power of the spiral to their grudge and created the dreaded King of Monsters.'):
        "In un passato remoto, una madre e un figlio di una fede straniera, perseguitati come eretici, morirono sul rogo. Il dio che disprezzavano come dio malvagio aggiunse al rancore dei due la forza della spirale, e creò un re dei mostri spaventoso.",

    # ---------------------------------------------------------- :14436 la fata
    (14436, 'Free-spirited stray fairy. She confuses passer-by travellers with illusions and steals their wallets. Enjoys watching them panic.'):
        "Una fata randagia, libera e capricciosa. Al viandante che passa mostra allucinazioni per confonderlo, oppure gli ruba il borsellino. Il suo passatempo è guardarlo mentre si agita.",

    # ---------------------------------------------------------- :14449 l'oca
    (14449, 'A part of the Yacatect of Wealth and her servant. A goose with shining white fur, it lays eggs filled with platinum coins when it is full. There are no platinum lumps in its body.'):
        "Una parte di Yacatect della ricchezza e insieme il suo servo. È un'oca dal piumaggio bianco e splendente, e quando è sazia depone uova con dentro monete di platino. Blocchi di platino, nel corpo, non ne ha.",

    # ---------------------------------------------------------- :14462 il gatto nero
    (14462, 'A part of the Ehekatl of Luck and her servant. A lustrous black cat with shiny jet-black fur. It is said that any armour licked by this cat is blessed by Ehekatl and given new powers.'):
        "Una parte di Ehekatl della fortuna e insieme il suo servo. È un gatto nero dal pelo corvino e lucente, di una bellezza sfrontata. Si dice che l'arma o l'armatura leccata da questo gatto riceva la benedizione di Ehekatl e un potere nuovo.",

    # ---------------------------------------------------------- :14475 la fatina
    (14475, 'Part of the Kumiromi of Harvest and his servant. A fairy who looks like something out of a fairy tale. Reincarnates food and produces crop seeds.'):
        "Una parte di Kumiromi del raccolto e insieme il suo servo. È una fatina che sembra uscita da una fiaba. Fa rinascere il cibo e ne ricava i semi delle colture.",

    # ---------------------------------------------------------- :14488 l'androide
    (14488, 'A part of and servant of the Mani of Machines. It is frequently improved by Mani, with the latest versions having sturdier armour.'):
        "Una parte di Mani della macchina e insieme il suo servo. Mani lo migliora di continuo, e la versione più recente ha una corazza robusta.",

    # ---------------------------------------------------------- :14501 l'angelo nero
    (14501, 'Part of Lulwy of Wind and her servant. A beautiful angel with black wings and dress, but like her Lord, she is erotic, sadistic and egotistical.'):
        "Una parte di Lulwy del vento e insieme il suo servo. È un angelo bellissimo, con le ali e l'abito neri, ma somiglia alla padrona: erotico, sadico ed egoista.",

    # ---------------------------------------------------------- :14514 l'esiliato
    (14514, 'Part of the Itzpalt of Element and his servant. A robed wizard. When they practised magic of other attributes in preference to elemental magic, Itzpalt were angered, and they are banished.'):
        "Una parte di Itzpalt degli elementi e insieme il suo servo. È un mago in veste lunga. Trascurava la magia degli elementi per esercitarsi in quella di altri attributi, si è tirato addosso l'ira del dio ed è stato scacciato.",

    # ---------------------------------------------------------- :14527 il cavaliere dorato
    (14527, 'Part of the Opatos of Earth and his servant. A beautiful blonde female knight who looks as if she were spun from a thread made of gold itself. She has a physical strength that is unimaginable from her slender appearance.'):
        "Una parte di Opatos della terra e insieme il suo servo. È una cavaliera bionda e bellissima, come se l'avessero filata con un filo d'oro vero. Ha una forza nelle braccia che quel corpo esile non lascia nemmeno immaginare.",

    # ---------------------------------------------------------- :14540 il difensore
    (14540, 'Part of the Jure of Healing and her servant. Even when driven to the brink of death, he continues to protect his friends with his body as the only shield.'):
        "Una parte di Jure della guarigione e insieme il suo servo. Anche spinto sull'orlo della morte, continua a proteggere i compagni facendo del proprio corpo un unico scudo.",

    # ---------------------------------------------------------- :14553 il cavallo zoppo
    (14553, 'A wild mongrel horse that seems to have escaped from somewhere. Although they are derided as spoiled horses, they would make excellent companions for fledgling adventurers with limited riding skills.'):
        "Un cavallo bastardo tornato allo stato brado, che a quanto pare è scappato da qualche parte. Lo deridono come un ronzino, ma per un avventuriero alle prime armi, che di cavalcare non sa granché, sarà il compagno migliore.",

    # ---------------------------------------------------------- :14566 il cavallo selvatico
    (14566, 'A wild horse that has been in the Irva for a long time. Many improved breeds, such as the Noyel horse and the Yowyn horse, have been created from this breed, and it can be said to be the origin of all horses.'):
        "Il cavallo selvatico che vive in Irva da tempi antichi. Da questa razza ne hanno ricavate molte migliorate, come il cavallo di Noyel e quello di Yowyn, e si può dire che sia l'origine di tutti i cavalli.",

    # ---------------------------------------------------------- :14579 il cavallo di Noyel
    (14579, 'Horses bred to adapt to the cold climate of Noyel. Their legs have evolved to allow them to move nimbly through snowfields, and they can run faster than their wild counterparts.'):
        "Un cavallo migliorato per adattarsi al clima freddo di Noyel. Le zampe si sono evolute per avanzare leggere sulla neve, e riescono a correre più veloci di quelle dei cavalli selvatici.",

    # ---------------------------------------------------------- :14592 il cavallo di Yowyn
    (14592, 'A horse bred in Yowyn. They are known for their strength, strength and speed, and their meat is also prized as a tasty foodstuff that is good for the soul.'):
        "Un cavallo migliorato a Yowyn. È noto come cavallo di razza pregiata, forte e veloce, ma anche la sua carne è ricercata come alimento saporito che rimette in forze.",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-029.jsonl'
DA, A = 14101, 14600
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
