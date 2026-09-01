# -*- coding: utf-8 -*-
"""121a - Lotto 058 di `db_item.hsp`: GLI SCUDI, e la categoria CHIUDE.

`FILTER_SHIELD`, righe da `:42852` a `:127204`: **24 righe** — 23 dell'indice 0
e 1 dell'indice 2 — su 23 oggetti. Con questo lotto `FILTER_SHIELD` va a **0 da
fare su 24 vive**, ed e' la **tredicesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 058`: **+24** per 24 rese,
nessuna gemella. ⓘ `_gia-reso.py 058`: 0 su 24. `_code.py 058`: 0 righe senza
resa in tabella — e le ventiquattro code sono state **copiate** dalla sua
uscita, non ricostruite (la lezione del lotto 057, otto su otto sbagliate).

### ⭐⭐⭐ UNA SERIE DI CINQUE, E QUESTA VOLTA L'HA TROVATA LO STRUMENTO

`_120-serie-bacchette.py 058` — nato nella 120a, al suo secondo lotto — ha
stampato in un secondo quel che le tre sessioni prima cercavano a mano:

    5 x  攻防一体の装備。

Sono i cinque tonfa **ST-01 SACRIFICE, ST-02 SHIELD, ST-03 SMASH, ST-04 SABER
e ST-05 SONIC**, che stanno nel dossier a righe lontane (`:71233`-`:71509`) ma
che il giocatore incontra come una famiglia: cinque numeri di serie in fila.

⭐ La formula si ripete **identica** in tutte e cinque le rese — «Un
equipaggiamento che unisce attacco e difesa.» — e cambia solo quel che viene
dopo. E' la stessa decisione delle tre armi della 120a: variare i verbi per non
ripetersi avrebbe cancellato la serie, che e' il modo in cui il giocatore
riconosce l'ST-01 come parente dell'ST-05.

ⓘ **Il valore atteso dello strumento resta «nessuna serie»**: in cinque lotti
su sei non ne ha trovate. Qui ne ha trovata una da cinque, e l'ha trovata
prima che scrivessi la prima resa.

### ⭐⭐⭐ 神の間 NON E' «TRA GLI DEI»: E' UN LUOGO, E IL GIOCATORE LO CONOSCE

`:57962`, le manette del 《神々の枷鎖》, dice 神の間での使用を想定し.

Letto come lingua, 神の間 e' «fra gli dei», e la frase suona benissimo: manette
pensate per essere usate fra dei. **E' sbagliato.** 神の間 e' il **Sigillo
Eterno**, il luogo dell'atto finale del gioco — inglese `Eternal Seal` — e sta
in una quarantina di battute gia' rese: «Al Sigillo Eterno non ci andare», «il
Sigillo Eterno e' in mano a qualcuno che non si sa chi sia».

⚠️ **Nessuna rete poteva vederlo.** La riga e' pulita in ogni senso: il
giapponese c'e', l'inglese c'e' («Intended for the gods» — anche lui l'ha letto
come lingua e non come nome), la forma e' a posto. Il difetto sarebbe esistito
solo nella testa del giocatore, che quel nome lo ha letto quaranta volte.
A trovarlo e' stata la quinta fonte della 110a — *il codice e il resto del
gioco* — interrogata con `_cerca.py` su una parola che sembrava non averne
bisogno.
💡 La regola che ne esce: **una parola composta di kanji comuni puo' essere un
nome proprio**, e il modo di scoprirlo e' cercarla, non guardarla.

### ⭐⭐ IL TONFA CHE IL GIAPPONESE NON DESCRIVE, E L'INGLESE TAGLIA A META'

`:71509`, l'ST-01 SACRIFICE, in giapponese dice **soltanto** la formula della
serie: 攻防一体の装備。 e basta. L'inglese ci aggiunge una frase, e quella
frase e' **troncata a meta' di parola**:

    Offensive-and-defensive equipment. It allows it's user to sac

Chi rende dall'inglese qui deve inventare la fine («...to sacrifice its own
durability»?). La resa viene dal giapponese e finisce dove finisce lui.

⭐ **E la riga gemella lo aveva gia' deciso**: l'indice 3 dello stesso oggetto,
reso in una sessione passata, sta davanti allo stesso troncamento
(`It is a tonfa that suc`) e ha scritto «Un tonfa.». Le due meta' del pannello
fanno la stessa cosa perche' una delle due l'aveva gia' fatta.

### ⭐ IL BOLLINO DEL BRAVO, CHE IN ITALIANO E' ANCHE UNO SCUDO

`:59592`, il 《クラウンポイント》, racconta che l'oggetto si dava agli allievi
del **Seminario d'Avventura** che superavano la prova del **maestro Spada
Rossa** (due nomi gia' resi, presi dal dizionario e non reinventati), e che
allora si chiamava がんばりシールド, «con motivi anche diversi dalla corona».

がんばりシールド e' un bisticcio: がんばりシール e' il **bollino** che in
Giappone il maestro attacca sul quaderno a chi ha fatto bene — e con un ド in
fondo diventa シールド, lo scudo. L'inglese lo traslittera («Ganbari Shield») e
non tiene niente.

⭐ L'italiano ha una parola che tiene tutt'e due i sensi: **scudetto** e'
insieme lo scudo piccolo e il bollino che si dava a scuola. La resa e'
«Scudetto Bravo», e la frase dopo — i motivi diversi dalla corona — conferma da
sola che si parla di bollini e non di armi.

### ⓘ Tre punti dove l'inglese e il giapponese non dicono la stessa cosa

  - `:100717`, lo scudo a torre. Il giapponese dice 重量は半端なものではなく,
    «il peso non e' cosa da mezza misura», cioe' **e' enorme**; l'inglese scrive
    «it is not half as heavy as it should be», che dice il **contrario**. La
    resa segue il giapponese, e l'indice 3 gia' reso («Uno scudo pesantissimo»)
    conferma da che parte sta il gioco;
  - `:71511`, l'appunto degli autori dentro l'ST-01: 第三部用, «per la parte
    terza». L'inglese scrive «Reserved for ACT III», ma in italiano gli atti si
    chiamano **parti** — la missione e' `@QM[第三部 永遠の盟約]` ->
    «Parte terza - Il patto eterno». Chi legge «ATTO III» non lo ritrova da
    nessuna parte;
  - `:81328`, l'asse di 《カルネアデスの板》. クイーン・セドナ号 non e' una nave
    qualunque: e' la **<Regina Sedona>**, che il giocatore conosce anche come
    persona («<Regina Sedona> la fanciulla delle vele») e la cui carta racconta
    lo stesso naufragio, «per il vento d'etere durante il viaggio inaugurale
    verso Porto Kapul». La resa la nomina come la nomina il resto del gioco.

### ⚠️ Le parole lunghe: sette a quindici caratteri, e sei sono la stessa

`_preflight034.py 058` segnala **7** parole nella finestra di rinculo, contro le
2 del 057 e le 2 del 055 (che ne aveva anche una da **18**, ed e' passata).
Sei delle sette sono «equipaggiamento», cioe' la **prima parola della formula
dei cinque tonfa**: se l'impaginatore la spezza, la spezza cinque volte.

⚠️ Il preflight e' un referto, non un cancello: il cancello vero e'
`_107-descrizioni-item`, «parole spezzate introdotte dall'italiano: 0», e si
misura **dopo** il reimporta. Se quello si accende, si cambia la formula — non
prima, perche' «equipaggiamento» e' la resa di 装備 gia' usata nella stessa
categoria (`:68250`, gli artigli).

### ⓘ Un difetto NON di questo lotto, visto passando

Il **nome** di 《カルネアデスの板》 sta nel dizionario spezzato in due voci —
「Carneades」 -> «Carneade» e 「plank」 -> «asse» — e a schermo si legge
**«Carneade asse»**. In italiano l'oggetto ha un nome suo, ed e' famoso: la
**tavola di Carneade**, il dilemma del naufrago che ne salva uno solo — che e'
esattamente quel che la descrizione dice («al massimo tiene a galla una persona
sola che stia annegando»). ⚠️ E' una riga di **nomi**, non di corpo: non la
tocca questo lotto, e va decisa a parte.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42852
    (42852, "The claws of a giant man-eating bear. They are incredibly robust and can even tear through iron sheets. A single strike can blow off an Irva creature's face along with its skull, and the shockwave alone can kill nearby Indian elephants.\\n# ~Irva Fantasy Encyclopedia~"):
        "Gli artigli di un grande orso mangiatore d'uomini. Sono così robusti da lacerare una lastra di ferro: con un colpo solo spazzano via la faccia, ossa comprese, a una creatura dell'Irva di oggi, e l'onda d'urto arriva ad ammazzare perfino l'elefante indiano lì accanto.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :57962
    (57962, 'Chained shackles created by the ancient gods. Intended for the gods, they are made physically sturdy even without supplying divine power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Manette con la catena, forgiate dagli dei antichi. Pensate per l'uso al Sigillo Eterno, sono fatte robuste sul piano fisico e basta, senza l'aiuto di alcun potere divino. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59592
    (59592, 'Gift given to students of the Adventurer Seminar. In the past, it was given only to those who had broken through the comprehensive questions given by Prof. Redsword. At that time, it was called \\"Ganbari Shield\\", and there were other patterns besides the crown. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un oggetto che si dona agli allievi del Seminario d'Avventura. Un tempo lo si dava solo a chi superava la prova del maestro Spada Rossa. Allora si chiamava Scudetto Bravo, e pare che oltre alla corona ci fossero anche altri motivi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :59860
    (59860, 'Mysterious mirror that exhales smoke when imbued with divine power. The first Tezcatlipoca had his leg bitten off while killing a certain goddess, and he attached this mirror to him as a prosthetic leg. Its name means \\"Mirror of the Night\\" in the ancient language. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno specchio misterioso che, se lo si carica di potere divino, sputa fumo. Si racconta che il primo Tezcatlipoca, cui una dea aveva staccato una gamba a morsi mentre la uccideva, per un certo tempo se lo sia attaccato addosso al posto della protesi. Il suo nome, in lingua antica, vuol dire \\\"lo specchio della notte\\\". \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :67599
    (67599, 'Claws forged by the secret arts of the ninja. They vibrate in resonance with specific sound waves, enhancing their sharpness. They can also amplify the power of chanted spells. \\n# ~Irva Fantasy Encyclopedia~'):
        "Artigli temprati con le arti segrete dei ninja. Vibrano entrando in risonanza con certe onde sonore, e così tagliano meglio. Pare che sappiano anche amplificare un incantesimo recitato e renderlo più potente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68250
    (68250, 'Equipment that imitates the claws of a beast, bird of prey, insect, etc.Its original use is to hook onto a tree or the ground. However, since it can be used as armor to repel attacks or to enhance the power of weapons, it is used exclusively for combat purposes. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un equipaggiamento che imita gli artigli delle bestie, dei rapaci, degli insetti. In origine serviva ad aggrapparsi agli alberi e al terreno; ma siccome fa da armatura per deviare i colpi e insieme da arma per rendere più forte il corpo a corpo, oggi lo si usa soltanto per combattere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :69256
    (69256, 'Claw-shaped weapon that brings misfortune to the target it slices open. It used to bring eternal misfortune to those it touched, but lost most of its power during the battle with the Goddess of Fortune. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'arma a forma di artiglio, che porta sfortuna a chi squarcia. Un tempo era roba capace di portare sfortuna eterna a chiunque la sfiorasse, ma nella battaglia contro la dea della fortuna ha perso quasi tutta la sua forza. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71233
    (71233, 'Offensive-and-defensive equipment. It incorporates a small propulsion device to increase the penetration power of the attack through acceleration. Since it temporarily accelerates above the speed of sound, it is also heat and shock resistant. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Ha un piccolo propulsore incorporato, e l'accelerazione dà al colpo più forza di perforare. Siccome per un attimo accelera oltre la velocità del suono, regge anche il calore e gli urti. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71302
    (71302, "Offensive-and-defensive equipment. It has the ability to convert the user's mana to form a photon blade. If there is an opportunity, it can be connected directly from a strike to a slash. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un equipaggiamento che unisce attacco e difesa. Sa convertire il mana di chi lo impugna e formarne una lama laser. Se trova un varco, dalla botta passa dritto al fendente. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71371
    (71371, 'Offensive-and-defensive equipment. Light and sturdy. It can be struck by slightly loosening its grip and then rotating it. It enables compact and quick combat attacks, smashing targets one after another. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Leggero e saldo. Si può anche allentare un poco la presa e colpire facendolo roteare. Permette attacchi corpo a corpo raccolti e svelti, e sbriciola i bersagli uno dopo l'altro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71439
    (71439, 'Offensive-and-defensive equipment. A repulsive shield generator is attached, which provides high defense despite being a tonfa.\\n# ~Irva Fantasy Encyclopedia~'):
        "Un equipaggiamento che unisce attacco e difesa. Ci è montato sopra un generatore di scudo repulsivo, e così, pur essendo un tonfa, tiene una difesa alta.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71509
    (71509, "Offensive-and-defensive equipment. It allows it's user to sac\\n# ~Irva Fantasy Encyclopedia~"):
        "Un equipaggiamento che unisce attacco e difesa.\\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :71511
    (71511, '\\"Reserved for ACT III.\\" \\n# ~Weird Memo~'):
        "Per la parte terza. \\n# ~Appunto Misterioso~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :73560
    (73560, 'Knight\'s shield that seals a curse. As a result, the \\"knight\'s soul that tries to protect the lord\\" that resides in the shield works to produce a high defensive power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno scudo da cavaliere in cui è stato sigillato il potere di una maledizione. Così agisce soltanto l'\\\"anima del cavaliere che vuole difendere il suo signore\\\" rimasta nello scudo, e ne esce una difesa altissima. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :81328
    (81328, 'Part of the Queen Sedona, which sank in the etheric wind. It can be used as a shield, but its defensive capability is not so good. It floats on water, but it can only support one drowning person. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un pezzo della <Regina Sedona>, la nave affondata per il vento d'etere. Come scudo si può anche usare, ma la difesa che dà è poca cosa. Galleggia, però al massimo tiene a galla una persona sola che stia annegando. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82410
    (82410, 'A shield with thorns of various sizes on its surface. It is not strong enough to protect itself, but when it is struck with full force, the poor enemy will scream in agony. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo pieno di spine grandi e piccole sulla faccia, che a guardarlo fa già male. Per difendersi non basta del tutto, ma quando lo si sbatte addosso con tutta la forza, il povero nemico si contorcerà dal dolore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :82478
    (82478, 'In ancient times, the lute was said to have sounded wonderful. Today, however, it is simply treated as an excellent shield made of very strong wood that does not show its age, and it will never sound as good as it did back then. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un liuto che nei tempi antichi, si dice, mandava un suono meraviglioso. Oggi però lo si tratta soltanto come un ottimo scudo, ricavato da un legno fortissimo su cui gli anni non si vedono, e un suono come quello d'allora non lo darà più. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :100717
    (100717, 'An extremely bulky shield. Naturally, it is not half as heavy as it should be, and it is said that once it is dropped to the ground, it will require the strength of several people to lift it back up. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo fatto spessissimo. Il peso, va da sé, non è cosa da poco: si dice che una volta caduto a terra ci voglia la forza di più persone per rimetterlo in mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100783
    (100783, 'A large rectangular shield. It is large enough to cover the body and can be used as a simple wall to shield the enemy, but it also has many harmful effects and requires skill to handle. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo grande e rettangolare. È tanto largo da coprire il corpo, e può fare da muro improvvisato per ripararsi dal nemico; ma proprio per questo dà anche parecchi impicci, e si dice che a maneggiarlo ci voglia esperienza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100849
    (100849, 'Shields made from a combination of special materials to provide stronger protection. It has the disadvantage of being somewhat heavy, but it just works. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Ha il difetto di essere un po' pesante, ma renderà molto più di quel poco che pesa in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100915
    (100915, "Protective gear designed to prevent attacks. Unlike armor, it can be held in one's own hands to oppose violence. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'armatura pensata per parare i colpi. A differenza della corazza la si tiene con la propria mano, e così si può fronteggiare la violenza che ti si getta addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100981
    (100981, 'Shield with its center of gravity attached to the center. It is said that the round shape of the shield was designed so that it would not hit the ground and impede walking when going into battle. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo tondo, col baricentro messo al centro. Si dice che quella forma tonda così particolare sia nata perché, andando al fronte, non battesse per terra e non impedisse di camminare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101047
    (101047, 'Shields smaller than normal shields. By attaching it to the arm, it succeeds in reducing the inconvenience of carrying it and its weight, but at the same time, the range in which it can be used for defense is considerably narrowed. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo più piccolo del normale. Legandolo al braccio si è riusciti a togliere di mezzo la scomodità di portarlo e il peso che ne veniva, ma in cambio lo spazio che si riesce a difendere si è fatto parecchio stretto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :127204
    (127204, 'A prestigious shield made for knights. They are elaborately engraved and decorated to suit the user, but they are not merely ceremonial and offer a certain degree of protection. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Uno scudo di gran pregio, fatto per i cavalieri. Porta cesellature e ornamenti lavorati con cura, scelti su misura di chi lo impugna; ma non è soltanto da cerimonia, e una certa protezione ce l'ha. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 23 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-058.jsonl'
RIGHE = {
    42852, 57962, 59592, 59860, 67599, 68250, 69256, 71233, 71302, 71371,
    71439, 71509, 71511, 73560, 81328, 82410, 82478, 100717, 100783, 100849,
    100915, 100981, 101047, 127204,
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
