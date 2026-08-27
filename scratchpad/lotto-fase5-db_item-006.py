# -*- coding: utf-8 -*-
"""110a - Lotto 006 di `db_item.hsp`: il rapporto degli SCARTI.

`FILTER_JUNK`, `description(3)`: **97 righe del sorgente, 81 firme**. Sedici
righe portano una firma che un'altra riga ha gia' — i tre materium (superiore e
normale hanno lo stesso giapponese), i **dodici** materiali della sintesi, la
spada del teschio e il cesto vuoto — e una resa le copre tutte.

### ⚠️ `FILTER_JUNK` non e' una categoria, e' il cassetto degli avanzi

Le altre categorie dell'indice 3 sono famiglie: il cibo sazia, la pergamena si
legge, il mobile si usa. Qui dentro ci sono **sei famiglie vere** — i lanciabili,
i nove strumenti degli dei, le tre perle ricurve, i materiali, le ossa, i cesti
— e una ventina di solitari che non somigliano a niente. La formula della 108a
regge lo stesso, perche' la formula non descrive la categoria: descrive il
**referto**.

### ⭐⭐ DUE RESE DECISE LEGGENDO IL CODICE, E IL TESTO NON BASTAVA

- **`:59793`, l'ohuda: cancella UN potenziamento, non «i» potenziamenti.** Il
  giapponese scrive 「バフを消去する御札だ。」 e il numero non lo dice — il
  giapponese non lo deve dire, l'italiano si'. `action.hsp:752-766` scorre i
  potenziamenti, chiama `delbuff` sul primo che trova e poi **`break`**: ne
  cancella uno solo. L'inglese («erases buffs») avrebbe portato al plurale.
- **`:63586`, 「態勢を崩す」 e' la ROTTURA GUARDIA del gioco.** L'inglese dice
  «disorientates opponent», che non e' un termine e non aggancia niente.
  `action.hsp:745` chiama `chara_guardbreak tc, 15`: e' il meccanismo, e il
  dizionario ha gia' la parola — «Rottura guardia» (`command.hsp`), «Abbassa la
  rottura guardia». La resa usa il termine. ⭐ E lo stesso termine torna a
  `:47152`, il fischietto, dove il giapponese lo scrive per esteso
  (「ガードブレイクゲージ」): due righe lontane che ora dicono la stessa cosa
  con la stessa parola.

⚠️ Nessuna rete poteva vedere ne' l'una ne' l'altra: guardano forma, inglese di
monte e dizionario, e qui la fonte era il **comportamento del gioco**.

### ⚠️ TRE RIGHE DOVE L'INGLESE RACCONTA E IL GIAPPONESE NO

E' la regola di `decisioni.md`, «Quando l'inglese aggiunge un fatto», la stessa
che nella 108a ha taciuto le sette aggiunte del cibo:

  `:48738`  la cicala — 「死にかけのセミだ。」, *una cicala moribonda*. L'inglese
            racconta che spaventa chi colpisci. Il **nome dell'oggetto e' gia'**
            «cicala morente»;
  `:116668` la ciotola — l'inglese cita Laozi, «the empty space which makes the
            bowl useful, and it's full already». Il giapponese dice soltanto che
            dentro c'e' qualcosa, ed e' la meta' del paio con `:116730`, la
            ciotola vuota: reso quello, l'altro si legge;
  `:46013`  il fukagurumi — l'inglese aggiunge «Worth less than you think», il
            giapponese ha **solo la coda**: 「何度でも使用することができる。」.
            La resa e' la coda e basta, «Si puo' usare sempre.».

### ⓘ Una riga senza giapponese

`:89761`, l'esca: `description(3)` giapponese e' **vuota**, e l'inglese e' l'unica
fonte che c'e'. E' la prima dell'indice 3 in questo stato.

### ⓘ Le formule del lotto

    〜の時に自動で使うアイテムだ。 -> Un oggetto che si usa da se' quando ...
    投げてぶつけると〜を放つ〜だ。 -> Un ... che, lanciato, sprigiona ...
    投げてぶつけると〜爆発を起こす -> ... fa un'esplosione ...
    合成用のアイテムだ。           -> Un oggetto per la sintesi.   (12 firme)
    〜中間素材だ。                 -> Un materiale intermedio ...  (3 firme)
    所持していると〜勾玉だ。       -> Una perla ricurva: portandola, ...

⚠️ **La testa cade due volte**, per la regola della 108a: `:86738` («Portato
addosso, alza le probabilita' di dominare i mostri.») e `:69391` («Si usa da se',
sempre, quando accarezzi il bestiame.»). Il fatto riempiva i 69.

### ⚠️ Una resa che non poteva concordare col giocatore

`:66012`, la magaqua: 「所持していると濡れ状態になる勾玉だ。」. «ti tiene
bagnato» concorda col **genere del giocatore**, che non si conosce
(`guida-stile.md`, e la rete dei participi di `referti.py`). Reso con
l'impersonale: «portandola addosso, ci si bagna».

### ⓘ I termini del lotto, tutti verificati nel dizionario o nel sorgente

ガードブレイク → «rottura guardia» · 主従度 → «grado di sottomissione» ·
バフ → «potenziamento» (「全体バフ消去」 → «cancella tutti i potenziamenti») ·
支配 → «dominare» (`chat.hsp`, ed e' la battuta che regala **questo** oggetto) ·
合成用アイテム → «oggetti per la sintesi» (`chat.hsp`) · 勾玉 → «perla ricurva»
(`invariati.md`) · ラムネ → «gazzosa» · 電撃 → «fulmine» · 冷気 → «gelo» ·
暗黒 → «oscurita'» · 毒 → «velenosa» · 神経 → «neurale» (`glossario.md`) ·
学習書 → «libro di studio» · 戦術指示 → «ordini tattici» · 士気 → «morale» ·
調教 → «addestrare» · プラチナ → «platino» · 疫 → «pestilenza» ·
ペット → «compagno» (109a) · スキル → «abilita'».

### ⓘ `子宝` non era nel dizionario, e l'ha deciso `description(0)`

`:66326`, l'E.G.G: 「子宝だ。」 in due caratteri. La descrizione lunga dello
stesso oggetto (`db_item.hsp:66317`) dice che e' la capsula che la cicogna porta
**agli sposi**: e' la benedizione dei figli, non un tesoro qualunque, e la
categoria giapponese ＜秘宝＞ non basta a dirlo. Reso «Il dono dei figli.».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42917
    (42917, "It's a card that can be used to record info on a creature."):
        "Una carta che registra i dati di chi colpisci.",

    # ---------------------------------------------------------- :42979
    (42979, 'Throwable shit. Causes a poisonous explosion on impact.'):
        "Uno sterco che, lanciato, fa un'esplosione velenosa.",

    # ---------------------------------------------------------- :43177
    (43177, 'Throwable, inedible metal can. Causes a nerve explosion on impact.'):
        "Una scatoletta immangiabile. Lanciata, fa un'esplosione neurale.",

    # ---------------------------------------------------------- :43305
    (43305, 'Throwable, crystalized snowflakes. Causes an icy explosion on impact.'):
        "Un cristallo di neve che, lanciato, sprigiona gelo.",

    # ---------------------------------------------------------- :43367
    (43367, 'Throwable grenades that unleashes darkness explosion.'):
        "Un attrezzo che, lanciato, sprigiona oscurità.",

    # ---------------------------------------------------------- :43429
    (43429, 'Throwable batteries that discharges electrical shocks.'):
        "Un lungo ago che, lanciato, sprigiona fulmini.",

    # ---------------------------------------------------------- :43491
    (43491, "Throwable boxes packed with plagues, probably shouldn't open them."):
        "Una scatola piena di pestilenza. Meglio non aprirla.",

    # ---------------------------------------------------------- :43770
    (43770, 'It is a coupon covering basic pet training fees.'):
        "Paga l'addestramento di un compagno di LV non superiore al tuo.",

    # ---------------------------------------------------------- :43832
    (43832, "It's a bland potion cork."):
        "Un tappo di pozione come tanti.",

    # ---------------------------------------------------------- :43965
    (43965, 'It is an item rewarded to obedient slaves.'):
        "Una catena gradita a chi ha un alto grado di sottomissione.",

    # ---------------------------------------------------------- :46013
    (46013, '(Reusable) tool. Worth less than you think.'):
        "Si può usare sempre.",

    # ---------------------------------------------------------- :46216
    (46216, 'It is an edible plant that heals you.'):
        "Una pianta che, mangiata, cura un poco.",

    # ---------------------------------------------------------- :46278
    (46278, 'It is a bottle cap.'):
        "Il tappo di una bottiglia. Non serve ad altro.",

    # ---------------------------------------------------------- :46340
    (46340, "It is a bottle cap for Ramune soda. It's useless."):
        "Il tappo di una bottiglia di gazzosa. Non serve ad altro.",

    # ---------------------------------------------------------- :47152
    (47152, '(Reusable) tool that reduces the guard break gauge.'):
        "Un fischietto che abbassa la rottura guardia. Si usa sempre.",

    # ---------------------------------------------------------- :48738
    (48738, 'It is an insect that frightens the opponent when you hit them with it.'):
        "Una cicala moribonda.",

    # ---------------------------------------------------------- :50881
    (50881, 'These are materials for book publishing.'):
        "Un materiale per fare libri.",

    # ---------------------------------------------------------- :52582
    (52582, 'It is a bead that prevents objects from shattering due to low-temp.'):
        "Una perla ricurva: portandola, il gelo non spacca gli oggetti.",

    # ---------------------------------------------------------- :55276
    (55276, 'Threwable barrel that spews flame when burning.'):
        "Un barile che bruciando sputa fuoco. Lanciato, esplode in fiamme.",

    # ---------------------------------------------------------- :55862
    (55862, 'These are remains of ancient organisms.'):
        "La traccia di un essere vivente.",

    # ---------------------------------------------------------- :55924
    (55924, 'It is some sticky soil.'):
        "Della terra appiccicosa.",

    # ---------------------------------------------------------- :55986
    (55986, 'It is a yellow crystal.'):
        "Un cristallo giallo.",

    # ---------------------------------------------------------- :56536
    (56536, 'It is a device that keeps the holder in shape.'):
        "Un apparecchio che conserva la linea di chi lo porta.",

    # ---------------------------------------------------------- :57896
    (57896, 'It is a ticket that can be used instead of platinum when teaching skills.'):
        "Un foglio che sostituisce il platino quando impari un'abilità.",

    # ---------------------------------------------------------- :58027
    (58027, 'It is a sharp interim material.'):
        "Un materiale intermedio affilato.",

    # ---------------------------------------------------------- :58151
    (58151, 'It is a hard interim material.'):
        "Un materiale intermedio duro.",

    # ---------------------------------------------------------- :58275
    (58275, 'It is a soft interim material.'):
        "Un materiale intermedio morbido.",

    # ---------------------------------------------------------- :59731
    (59731, 'It is a bunch of fresh flowers. Used to convey feelings.'):
        "Un mazzo di fiori freschi. Si usa per dire quel che si prova.",

    # ---------------------------------------------------------- :59793
    (59793, 'It is a thrown talisman that erases buffs.'):
        "Un talismano che cancella un potenziamento. Si può lanciare.",

    # ---------------------------------------------------------- :60128
    (60128, "It is a box that can't be opened. But it can be thrown."):
        "Una scatola che non si può aprire. Ma si può lanciare.",

    # ---------------------------------------------------------- :60851
    (60851, 'These are cigarette butts that ignites when thrown.'):
        "Un mozzicone di sigaretta. Lanciato, prende fuoco.",

    # ---------------------------------------------------------- :61181
    (61181, '(Single-use) medicinal tool that is highly addictive.'):
        "Foglie di una pianta che dà dipendenza. Si usa (usa e getta).",

    # ---------------------------------------------------------- :61313
    (61313, 'These are red coins used for special services.'):
        "Una moneta rossastra. Dà diritto a certi servizi.",

    # ---------------------------------------------------------- :62735
    (62735, '(Reusable) tool that designates the target and raises the morale.'):
        "Un bastone che alza il morale dei compagni e sceglie il bersaglio.",

    # ---------------------------------------------------------- :62868
    (62868, '(Autoused) tool that helps with training.'):
        "Un oggetto che si usa da sé quando ti alleni.",

    # ---------------------------------------------------------- :62932
    (62932, '(Autoused) tool that cure your sickness.'):
        "Un oggetto che scatta da sé quando ti ammali.",

    # ---------------------------------------------------------- :62996
    (62996, '(Autoused) tool that helps with special training.'):
        "Un oggetto che si usa da sé quando addestri.",

    # ---------------------------------------------------------- :63060
    (63060, '(Autoused) tool that helps with tactical instruction.'):
        "Un oggetto che si usa da sé quando dai ordini tattici.",

    # ---------------------------------------------------------- :63124
    (63124, '(Autoused) tool that reveals extra character information.'):
        "Un oggetto che si usa da sé quando guardi una scheda.",

    # ---------------------------------------------------------- :63188
    (63188, '(Autoused) tool that helps reading.'):
        "Un oggetto che si usa da sé quando leggi un libro di studio.",

    # ---------------------------------------------------------- :63252
    (63252, '(Autoused) tool for drinking potions.'):
        "Un oggetto che si usa da sé quando bevi una pozione.",

    # ---------------------------------------------------------- :63316
    (63316, '(Autoused) tool that helps harvest.'):
        "Un oggetto che si usa da sé quando raccogli.",

    # ---------------------------------------------------------- :63586
    (63586, 'It is a throwable item that inflicts damage and disorientates opponent.'):
        "Un oggetto che all'urto ferisce e rompe la guardia.",

    # ---------------------------------------------------------- :64618
    (64618, 'It is a woven basket with no contents.'):
        "Un cesto di vimini senza niente dentro.",

    # ---------------------------------------------------------- :64872
    (64872, 'Throwable magic crystal that explodes thrice upon impact.'):
        "Un cristallo che, lanciato, esplode più volte.",

    # ---------------------------------------------------------- :64934
    (64934, 'Throwable magical crystal that explodes on impact.'):
        "Un cristallo che esplode all'urto.",

    # ---------------------------------------------------------- :66012
    (66012, 'It is a bead that soaks the holder in water.'):
        "Una perla ricurva: portandola addosso, ci si bagna.",

    # ---------------------------------------------------------- :66264
    (66264, 'It is an item used for artifact fusion.'):
        "Un oggetto per la sintesi.",

    # ---------------------------------------------------------- :66326
    (66326, 'It is a stork E.G.G, or S.E.G.Gs.'):
        "Il dono dei figli.",

    # ---------------------------------------------------------- :66768
    (66768, 'It is a large stone suitable for sculpture.'):
        "Una grande pietra buona per scolpire.",

    # ---------------------------------------------------------- :68048
    (68048, 'It is a bead that prevents objects from shattering due to high-temp.'):
        "Una perla ricurva: portandola, il fuoco non provoca incendi.",

    # ---------------------------------------------------------- :68391
    (68391, 'It is a tree processed into a carpentry material.'):
        "Del legno lavorato per farne materiale.",

    # ---------------------------------------------------------- :69391
    (69391, '(Autoused) tool for rubbing livestocks.'):
        "Si usa da sé, sempre, quando accarezzi il bestiame.",

    # ---------------------------------------------------------- :71646
    (71646, '(Autoused) tool that catches the fish automatically.'):
        "Un'esca automatica. Si usa da sé quando peschi.",

    # ---------------------------------------------------------- :75378
    (75378, 'They sell for a reasonable price.'):
        "Un oggetto che si vende a un prezzo discreto.",

    # ---------------------------------------------------------- :86738
    (86738, '(Autoused) tool that enhances your mastery of monsters.'):
        "Portato addosso, alza le probabilità di dominare i mostri.",

    # ---------------------------------------------------------- :89761
    (89761, 'It is bait for a fishing pole.'):
        "Un'esca per la canna da pesca.",

    # ---------------------------------------------------------- :91463
    (91463, 'It is a scarecrow covered in snow.'):
        "Uno spaventapasseri coperto di neve.",

    # ---------------------------------------------------------- :92454
    (92454, 'It is biological excrement.'):
        "Gli escrementi di un essere vivente.",

    # ---------------------------------------------------------- :109211
    (109211, "It is the remain's of a tree. It can be used as a seat."):
        "Quel che resta di un albero tagliato. Si può usare sempre.",

    # ---------------------------------------------------------- :111066
    (111066, 'It is a bundle of fresh flowers.'):
        "Un mazzo di fiori freschi.",

    # ---------------------------------------------------------- :112758
    (112758, 'It is an item for cleaning.'):
        "Un attrezzo per pulire.",

    # ---------------------------------------------------------- :112820
    (112820, 'It is a bird deterrent placed in the field.'):
        "Uno scacciauccelli da mettere nel campo.",

    # ---------------------------------------------------------- :112882
    (112882, 'It is dried wood ready for burning.'):
        "Pezzi di legno tagliati per il focolare.",

    # ---------------------------------------------------------- :116411
    (116411, 'These are bones of a dead animal.'):
        "Le ossa abbandonate di un animale.",

    # ---------------------------------------------------------- :116473
    (116473, 'It is a bundle of dried grass.'):
        "Erba secca legata in fascio.",

    # ---------------------------------------------------------- :116543
    (116543, 'It is a dried fish. Cannot be used.'):
        "Un pesce secco. Non si può usare.",

    # ---------------------------------------------------------- :116668
    (116668, "It is the empty space which makes the bowl useful, and it's full already."):
        "Un recipiente con qualcosa dentro.",

    # ---------------------------------------------------------- :116730
    (116730, 'It is an empty bowl.'):
        "Un recipiente senza niente dentro.",

    # ---------------------------------------------------------- :116792
    (116792, 'It is a woven basket.'):
        "Un cesto di vimini.",

    # ---------------------------------------------------------- :116854
    (116854, 'These are chipped empty bottles. Cannot be used.'):
        "Bottiglie vuote e scheggiate, tutte insieme. Non si possono usare.",

    # ---------------------------------------------------------- :116916
    (116916, 'These are minerals that are mostly made of rock.'):
        "Un minerale fatto quasi tutto di roccia.",

    # ---------------------------------------------------------- :127672
    (127672, 'These are abandoned human bones.'):
        "Le ossa abbandonate di una persona.",

    # ---------------------------------------------------------- :127734
    (127734, 'These are abandoned bones.'):
        "Le ossa abbandonate di qualcosa.",

    # ---------------------------------------------------------- :127796
    (127796, 'It is a useless damaged sword.'):
        "Una spada rotta che non serve a niente.",

    # ---------------------------------------------------------- :127858
    (127858, 'It is an ornament made of cloth.'):
        "Un ornamento fatto di stoffa.",

    # ---------------------------------------------------------- :127920
    (127920, 'It is a simple lighting fixture. Always illuminates the surroundings.'):
        "Una lampada semplice. Illumina sempre di luce viva.",

    # ---------------------------------------------------------- :127982
    (127982, 'These are dirty clothes in a basket.'):
        "Vestiti sporchi dentro un cesto.",

    # ---------------------------------------------------------- :128044
    (128044, 'It is a useless and damaged crucible.'):
        "Un vaso rotto che non serve a niente.",

    # ---------------------------------------------------------- :128106
    (128106, 'It is a bunch of dry grass.'):
        "Un fascio di erba secca.",

    # ---------------------------------------------------------- :128238
    (128238, 'It is a damaged piece of wood.'):
        "Una scheggia di legno rotto.",

# 81 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-006.jsonl'
RIGHE = {
    42917, 42979, 43177, 43305, 43367, 43429, 43491, 43770, 43832, 43965,
    46013, 46216, 46278, 46340, 47152, 48738, 50881, 52582, 55276, 55862,
    55924, 55986, 56536, 57896, 58027, 58151, 58275, 59731, 59793, 60128,
    60851, 61181, 61313, 62735, 62868, 62932, 62996, 63060, 63124, 63188,
    63252, 63316, 63586, 64618, 64872, 64934, 66012, 66264, 66326, 66768,
    68048, 68391, 69391, 71646, 75378, 86738, 89761, 91463, 92454, 109211,
    111066, 112758, 112820, 112882, 116411, 116473, 116543, 116668, 116730, 116792,
    116854, 116916, 127672, 127734, 127796, 127858, 127920, 127982, 128044, 128106,
    128238,
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
