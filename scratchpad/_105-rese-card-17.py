# -*- coding: utf-8 -*-
"""105a - Lotto 17 di `db_card.hsp`: le carte fra la riga 8101 e la 8600 (39).

⚠️⚠️ **Tre carte dove l'inglese di monte dice il contrario o un'altra cosa**, e
si traducono **dal giapponese**:

    :8129  <Nazuna>   やる気が空回りした, «la voglia le gira a vuoto» -> l'inglese
                      scrive «her lack of motivation», che e' il contrario:
                      non le manca la voglia, e' che la spende male
    :8246  il signore 調子に乗った部下を一喝する, «zittire con un urlo il
                      sottoposto che si monta la testa» -> l'inglese scrive
                      «cheer up a subordinate who's in a bad mood»
    :8311  la viverna 竜の亜種, «una sottospecie di drago» -> l'inglese ci mette
                      i puntini in mezzo alla frase, che il giapponese non ha

ⓘ **Tre carte diverse si chiamano tutte `旧人類`** (`:8181`, `:8194`, `:8207`):
il dossier per due di loro stampa `IT None` perche' il nome e' reso una volta
sola, non perche' manchi. Le prose sono tre e divergono dopo la prima frase.

⭐ **Gia' deciso altrove, e qui si ubbidisce:** `エーテル` → **l'etere**
(`chara_func.hsp:2864`, «la malattia dell'etere»), `メシェーラ` → **i Meshera**
(`action.hsp:17270`), `レム・イド` → **Rehm-Ido** (glossario della 104a: ⚠️ **non
`Rehmido`**, che e' come lo scrive l'inglese di monte, e ⚠️ **non `Remido`**, che
sono le **rovine** レミード — due nomi simili per due cose diverse. Preso in
fallo qui: la prima stesura diceva `Rehmido`, sull'inglese, e la correzione l'ha
imposta il glossario), `ゼイレン` → **Xeren** (`db_creature`, «il carro umanoide Xeren»),
`イルヴァ` → **Irva**, `九頭竜` → **il drago a nove teste**, `混沌` → **il
caos**, `イツパロトル` → **Itzparotl** (il nome della carta resta `<Itzpalt>`,
che e' come lo scrive il gioco).

ⓘ `ボコノン教` → **il bokononismo** e `カラース` → **il karass**: il nome della
carta, `il guardiano del karass`, era gia' reso cosi' e la prosa gli va dietro.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :8103 il ragazzo <Wel>
    (8103, "His parents are performers and have moved around the world and they don't care for him at all. For that reason he is very fond of his grandfather who frequently sends him letters and sweets."):
        "I genitori fanno i musicisti e girano il mondo senza mai fermarsi, e di lui non si occupa nessuno. Anche per questo si è affezionato moltissimo al nonno, che gli manda spesso lettere e dolciumi.",

    # ---------------------------------------------------------- :8116 il drago azzurro
    (8116, 'An aged lizard has mutated. Its appearance is similar to that of a dragon but it is closer to that of a god. It uses lightning and its accompanying roar to attack the enemy.'):
        "È una lucertola che, con gli anni, è mutata. Nell'aspetto somiglia molto a un drago, ma se si deve scegliere sta più dalla parte degli dei. Attacca il nemico comandando il fulmine e il fragore che gli va dietro.",

    # ---------------------------------------------------------- :8129 <Nazuna> la maestra d'armi
    (8129, "She took over the dojo in her father's footsteps. However as a result of her lack of motivation she is abandoned by all her students. The bamboo sword was given to her by her father and when she loses it she immediately becomes weak."):
        "Ha preso il posto del padre e si è vista lasciare la palestra. Ma la voglia di fare le è girata a vuoto, e alla fine gli allievi sono scappati tutti quanti. La spada di bambù gliel'ha data il padre: se la perde, all'istante si perde d'animo.",

    # ---------------------------------------------------------- :8142 la mascotte a ore
    (8142, 'He applied for the job without reading the job description carefully. He regret it because his part-time job description was the person in the mascot who is often beaten up to call the rain.'):
        "Si è candidato senza leggere per bene l'annuncio. Adesso se ne pente: il lavoro consisteva nello stare dentro la mascotte che, per chiamare la pioggia, viene presa a bastonate.",

    # ---------------------------------------------------------- :8155 <Estork> la bianca fiamma
    (8155, 'For a long time he protected the forest and the creatures that live in it. At the end of his life he was reincarnated as a god enveloped in white fire by the faith of the creatures of the forest.'):
        "Per lunghissimo tempo ha protetto la foresta e le creature che ci vivono. E quando la sua vita è arrivata al termine, la fede di quelle creature lo ha avvolto in una fiamma bianca e lo ha fatto rinascere dio.",

    # ---------------------------------------------------------- :8168 <Ether Generator>
    (8168, 'Genetically engineered artificial life forms. It has an ether generation and dispersal organ and can spread to a wide range of areas. It was a trump card against Meshera but Rehmido was destroyed before it could be mass-produced.'):
        "Una forma di vita artificiale nata dalla manipolazione dei geni. Ha un organo che produce e diffonde l'etere, e purifica aree molto vaste. Era la carta vincente contro i Meshera, ma Rehm-Ido cadde prima che se ne potessero fare in quantità.",

    # ---------------------------------------------------------- :8181 l'umano arcaico
    (8181, 'The surviving descendants of the Rehmido civilization. They all live in a shelter and only go out to the garden about once a month.'):
        "Discende da chi sopravvisse alla civiltà di Rehm-Ido. Vivono tutti dentro il rifugio, e nel giardino escono si e no una volta al mese.",

    # ---------------------------------------------------------- :8194 l'umano arcaico
    (8194, 'The surviving descendants of the Rehmido civilization. His main job is to tell the next generation about the threat of Meshera and the blessings of the ether.'):
        "Discende da chi sopravvisse alla civiltà di Rehm-Ido. Il suo compito principale è raccontare a chi verrà dopo che cosa sono la minaccia dei Meshera e la protezione dell'etere.",

    # ---------------------------------------------------------- :8207 l'umano arcaico
    (8207, 'The surviving descendants of the Rehmido civilization. He is not familiar with the threats of Meshera and has a longing for the outside world.'):
        "Discende da chi sopravvisse alla civiltà di Rehm-Ido. Che cosa sia la minaccia dei Meshera non l'ha ben capito, e il mondo di fuori lo attira.",

    # ---------------------------------------------------------- :8220 il drago elementale
    (8220, 'He was originally three dragons but with the blessing of the elemental Itzparotl he became a deity. It does not have the ability to merge the conflicting attributes of fire and ice breaths.'):
        "In origine erano tre draghi, poi la protezione di Itzparotl degli elementi li ha fatti diventare un dio. Ma la stoffa per fondere in un soffio solo due elementi opposti come il fuoco e il ghiaccio non ce l'ha.",

    # ---------------------------------------------------------- :8233 il re dei demoni
    (8233, "The king who stands at the top of all the demon races. They come to Irva to pass the time due to boredom. Without strong magic and a deep bond it would be difficult to repel the king's brainwashing."):
        "Il re che sta in cima a tutte le stirpi demoniache. Si annoia, e viene a Irva tanto per passare il tempo. Ha un potere magico forte: senza un legame profondo, scrollarsi di dosso il lavaggio del cervello del re è difficile.",

    # ---------------------------------------------------------- :8246 il signore dei demoni
    (8246, "A lord who unites and reigns over the lower demons. It's part of the job to cheer up a subordinate who's in a bad mood. They don't like to get under people so they try their best to shake them off."):
        "Il signore che tiene insieme e governa i demoni di grado inferiore. Zittire con un urlo il sottoposto che si monta la testa fa parte del mestiere. Stare sotto qualcuno non gli va giù, e pare che faccia di tutto per scrollarselo di dosso.",

    # ---------------------------------------------------------- :8259 il demone
    (8259, 'A general devil who loves depravity and original sin immensely. Their fighting ability is high as they prefer to bully others. They would outperform the average human both in physical combat and in magic.'):
        "Un demone qualunque, che ama alla follia la corruzione e il peccato d'origine. Poiché il suo gusto è calpestare gli altri, in combattimento vale molto: nel corpo a corpo e nella magia batte l'uomo comune.",

    # ---------------------------------------------------------- :8272 <Apparato di comunicazione mobile>
    (8272, 'Special radio waves can be used to communicate even in deep caves. It is designed and developed directly by the chief developer and is very high performance. While on standby it automatically performs combat actions and also collects data.'):
        "Con le sue onde speciali riesce a comunicare perfino in fondo a una grotta. L'ha progettato e costruito di persona il capo dello sviluppo, e infatti rende una cosa esagerata. Quando è in attesa combatte da solo e intanto raccoglie dati.",

    # ---------------------------------------------------------- :8285 il calabrone nero
    (8285, 'It is renowned as the most poisonous creature in Irva. They do not have a specific nest and live in groups repeatedly moving and attacking. They are fierce aggressive and very dangerous.'):
        "È famoso come la creatura dal veleno più forte di tutta Irva. Un nido suo non ce l'ha: vive in sciame e passa la vita a spostarsi e a piombare addosso a qualcuno. È feroce e aggressivo, e pericolosissimo.",

    # ---------------------------------------------------------- :8298 l'uccisore di Orione
    (8298, 'A scorpion mutated with the blessings of the gods and stars. At first glance it appears to be an ordinary scorpion but there is no shortage of adventurers who are paralyzed and killed by its neurotoxin.'):
        "Uno scorpione mutato sotto la protezione degli dei e delle stelle. A prima vista è uno scorpione come tanti, ma il suo veleno prende i nervi, e di avventurieri che restano immobili e ci lasciano la pelle non si finisce mai di contarne.",

    # ---------------------------------------------------------- :8311 la viverna valorosa
    (8311, 'A further mutant of a subspecies of the dragon...born in the process of evolution. It has a special bone and muscle structure and even a single-winged attack can be unusually destructive.'):
        "Una sottospecie di drago nata lungo il cammino dell'evoluzione, e poi mutata un'altra volta ancora. Ha ossa e muscoli fatti in modo particolare: perfino un colpo dato con una sola ala sprigiona una potenza distruttiva fuori dal comune.",

    # ---------------------------------------------------------- :8324 <Unicorno del Caos> il re del caos
    (8324, "A black unicorn that controls the power of chaos. An incarnation of chaos where multiple monsters have taken each other in and fused together. It must be a huge feat but the god of chaos doesn't seem to like it that much."):
        "Un unicorno nero che comanda la forza del caos. È l'incarnazione del caos, nata da più mostri che si sono divorati a vicenda e poi fusi insieme. Che sia una gran cosa non c'è dubbio, ma pare che al dio del caos non stia poi tanto simpatico.",

    # ---------------------------------------------------------- :8337 lo spirito del caos
    (8337, 'The spawn of chaos. The consciousness of those who have been swallowed by chaos and made into material is blended. The material is mixed with the warriors who stood up to the chaos.'):
        "Un figlio del caos, generato dal caos stesso. Dentro di lui si mescolano le coscienze di quelli che il caos ha inghiottito e usato come materia prima. E fra quella materia, dicono, ci sono anche i valorosi che gli tennero testa.",

    # ---------------------------------------------------------- :8350 il terminale d'attacco Xeren
    (8350, 'It attacks from multiple directions while disrupting the enemy with its quick movements. It comes standard with a language feature for supporting soldiers. There are also many soldiers who follow along and treat it as a pet.'):
        "Si muove svelto, scompiglia il nemico e intanto lo attacca da più parti insieme. Di serie ha la funzione della lingua, per dare una mano ai soldati. E siccome trotterella dietro a tutti, molti soldati lo trattano come un animale di casa.",

    # ---------------------------------------------------------- :8363 il semovente a fulmini di Xeren
    (8363, 'The legacy of mechanical civilization. It is equipped with a lightning cannon that was created during the development of the railgun. Since it is basically a self-propelled artillery it is equipped with only minimal armor.'):
        "Un lascito della civiltà delle macchine. Monta il cannone a fulmini che venne fuori mentre si metteva a punto il cannone elettromagnetico. In sostanza è un pezzo semovente, e infatti di corazza ne ha il minimo indispensabile.",

    # ---------------------------------------------------------- :8376 il guardiano del karass
    (8376, 'They exist to defend Bokononism. When the congregation is about to deviate from the original purpose of Kalas they cancel out the thought and render it foolish.'):
        "Esiste per difendere il bokononismo. Quando un fedele sta per allontanarsi dallo scopo vero del karass, gli cancella il pensiero e glielo riduce a una sciocchezza.",

    # ---------------------------------------------------------- :8389 <Gwen> la guerriera spietata
    (8389, 'For three years Gwen has been held captive by a heartless adventurer. She manages to escape with her life but the harsh environment has turned her into a ruthless warrior.'):
        "Per tre anni interi Gwen è rimasta prigioniera di un avventuriero senza cuore. È riuscita a fuggire per il rotto della cuffia, ma quella vita durissima aveva ormai fatto della ragazzina una guerriera spietata.",

    # ---------------------------------------------------------- :8402 <Scudo del Dolore>
    (8402, "The lament and despair of the knight's failure to protect the Lord gave rise to a curse that transformed the shield in his possession. It wanders in search of things to protect. However no one wants to be escorted because the knight's face is so creepy."):
        "Il lamento e la disperazione di un cavaliere che non era riuscito a proteggere il suo signore generarono una maledizione, e la maledizione trasformò lo scudo che teneva in mano. Vaga in cerca di qualcosa da proteggere; ma il viso del cavaliere ci è rimasto appiccicato sopra, e fa un effetto tale che nessuno lo vuole come scorta.",

    # ---------------------------------------------------------- :8415 la sanguisuga silenziosa
    (8415, "They creep up on their prey quietly and without sound. But because of its figure it was soon discovered. It's trying to create a fog but..."):
        "Si avvicina alla preda in silenzio, senza fare il minimo rumore. Solo che, con quel corpaccione, la scoprono subito. Qualcosa per rimediare la fa, tipo tirare fuori la nebbia, ma insomma.",

    # ---------------------------------------------------------- :8428 la sanguisuga volante
    (8428, 'They leap long distances in pursuit of their prey some jumping over 200 meters. After jumping it sucks blood. It has the skill to land brilliantly even when its prey avoids it.'):
        "Spicca salti lunghissimi puntando alla preda, e ce n'è che supera i duecento metri. Una volta arrivata addosso, succhia sangue e basta. E anche quando la preda si scansa, sa atterrare con eleganza.",

    # ---------------------------------------------------------- :8441 la cittadina
    (8441, "It's a strange citizen who is just strolling around town but somehow seems very happy about it. In addition to being as agile as a ninja she has a hidden shuriken."):
        "Una cittadina strana: passeggia per la città e nient'altro, eppure ha un'aria felicissima. Oltre a essere svelta come una ninja, tiene nascosti addosso degli shuriken.",

    # ---------------------------------------------------------- :8454 la bambina masochista
    (8454, "A girl who sacrificed many things to protect her master and mastered magic. She doesn't care at all what kind of pain she's been through even though she's been through some pretty bad things."):
        "Una bambina che ha imparato la magia sacrificando ogni sorta di cosa, pur di proteggere il suo padrone. Chissà quali dolori ha passato: per quanto la concino male, a lei non fa né caldo né freddo.",

    # ---------------------------------------------------------- :8467 la sorella maggiore buona a nulla
    (8467, "She's a very bad sister. Not only does she have no interest in grooming or dressing up she doesn't even bother to fix her sleeping habits. Recently she's started to think that she doesn't have to wear a jersey as long as she's wearing at least some underwear."):
        "Una sorella maggiore buona a nulla, ma proprio a nulla. Non solo di curarsi e di vestirsi bene non le importa niente: non ha nemmeno voglia di aggiustarsi i capelli schiacciati dal cuscino. Di recente ha cominciato a pensare che, purché addosso ci sia almeno la biancheria, la tuta si potrebbe anche non metterla.",

    # ---------------------------------------------------------- :8480 <Pascal>
    (8480, 'The dog was separated from her master by an accident. As a result of repeatedly mutating and fighting external enemies at the point where she got separated she became powerful enough to fend off demons.'):
        "Una cagna che un incidente ha separato dal suo padrone. Là dove si era persa ha continuato a battersi contro i nemici, mutando una volta dopo l'altra, e alla fine si è ritrovata forte abbastanza da respingere un demone.",

    # ---------------------------------------------------------- :8493 <Leiki> la tartaruga nera
    (8493, 'A tortoise that has mutated over the years. It is so fast that it is hard to believe that it was originally a tortoise. Its limbs can change shape at will. When a naughty kid comes close to it, it spits out plasma to obliterate the kid.'):
        "È una tartaruga che, con gli anni, è mutata. È così svelta che non si direbbe mai che tartaruga lo fosse davvero. Le zampe può cambiarle di forma quando le pare. E se le si avvicina un monello, gli sputa addosso il plasma e lo riduce in cenere.",

    # ---------------------------------------------------------- :8506 <Mizuki> la principessa dell'abisso
    (8506, 'Descendant of the nine-headed dragon. She is skilled in manipulating her tentacle-like hair. Having lived at the bottom of the sea for tens of thousands of years, she is deeply interested in the world above ground. She enjoys making lunch boxes and sometimes asks Leiki to go shopping for ingredients.'):
        "Discende dal drago a nove teste. Maneggia con maestria quei suoi capelli che paiono tentacoli. Ha vissuto decine di migliaia di anni in fondo al mare, e il mondo di sopra la incuriosisce moltissimo. Il suo passatempo è preparare cestini da pranzo, e ogni tanto manda Leiki a comprare gli ingredienti.",

    # ---------------------------------------------------------- :8519 la creatura dei fondali
    (8519, "Originally an normal fish, they were transformed by Mizuki's divine energy. They are now a service tribe that worships her and her ancestors."):
        "Era un pesce come tanti, poi il soffio divino di Mizuki lo ha investito e lo ha cambiato. Adesso è una stirpe di servitori, che venera lei e i suoi antenati.",

    # ---------------------------------------------------------- :8532 l'eroe cadaverico
    (8532, 'The last of the warriors of a kingdom destroyed by a magical kingdom. A hero who fought to the last for his country, undaunted by the magic that was hurled at him one after another.'):
        "È quel che resta del guerriero di un regno che una nazione di maghi ha distrutto. Un eroe che non si perse d'animo sotto le magie che gli piovevano addosso una dopo l'altra, e si batté per la patria fino all'ultimo.",

    # ---------------------------------------------------------- :8545 lo spirito delle armi
    (8545, "The love for one's comrades-in-arms is embodied in one's favourite gun, which combines with the soul after the owner's death and transforms into a spirit. Even in death, he continues to fight for someone somewhere."):
        "Il pensiero rivolto ai compagni d'arme si annidò nel fucile che il padrone aveva sempre con sé; poi il padrone morì, l'anima si unì all'arma e ne venne fuori uno spirito. Anche da morto continua a battersi per qualcuno, da qualche parte.",

    # ---------------------------------------------------------- :8558 l'abitante dell'abisso
    (8558, "Indigenous Irva inhabitants of the deep sea. Originally worshipped other deities, but converted due to the strong divine spirit of Mizuki's ancestors. At birth, they are almost human in appearance, but as they age they become more fish-like."):
        "Gente degli abissi, nativa di Irva. Un tempo venerava un altro dio, poi il soffio divino potente degli antenati di Mizuki la investì e la fece convertire. Alla nascita ha quasi la forma di un uomo, ma invecchiando somiglia sempre di più a un pesce.",

    # ---------------------------------------------------------- :8571 la signorina dal cuore nero
    (8571, 'A young lady of very noble birth. She has a soft manner, but her nature is cruel and cold-hearted. She kills all her servants for fun and is looking for a sturdier servant. Her clothes are white, but in reality she is endlessly black.'):
        "Di nascita nobilissima. I modi sono garbati, ma il carattere è crudele e gelido. Per gioco ha ammazzato tutta la servitù, e adesso cerca servitori un po' più robusti. Il vestito che porta è bianco; quello che c'è sotto è nero senza fondo.",

    # ---------------------------------------------------------- :8584 <Itzpalt>
    (8584, 'Head of the current group of deities. Governs the three elements. He is somewhat avoided because of his difficult and long story. He originally has a youthful appearance and more power than the other gods, but both of these are now partly the properties of Tezcatlipoca.'):
        "È lui che tiene insieme gli dei di adesso, e governa i tre elementi. Parla difficile e parla lungo, e per questo lo evitano un po' tutti. Di suo avrebbe un aspetto giovane e una forza superiore a quella degli altri dei, ma oggi l'uno e l'altra sono in parte roba di Tezcatlipoca.",

    # ---------------------------------------------------------- :8597 <L'Elemento>
    (8597, "Itzparotl has sublimated the power of the three elements he controls to the utmost limit. The total amount of mana has swelled as a result of the body's link with the surrounding elements. "):
        "È Itzparotl che ha portato all'estremo la forza dei tre elementi su cui comanda. Il corpo gli si è legato agli elementi che ha intorno, e per questo la sua mana è cresciuta a dismisura. ",
}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_card-017.jsonl'
DA, A = 8101, 8600
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
