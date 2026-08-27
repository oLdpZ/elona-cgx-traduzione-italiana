# -*- coding: utf-8 -*-
"""110a - Lotto 011 di `db_item.hsp`: il rapporto dei GRIMORI.

`FILTER_ITEM_SPELLBOOK`, `description(3)`: **82 righe del sorgente, 82 firme**,
79 giapponesi distinti. E' la seconda categoria dell'indice 3 per grandezza fra
quelle rimaste, e la terza per formulaicita' dopo le bacchette e i contenitori.

    〜を唱える為に必要な本。読むことができる。 -> Un libro per ... Si può leggere.
    〜を唱える為に必要な本だ。                 -> Un libro per ...   (senza coda)

### ⚠️⚠️ IL RANGO NON SI SCRIVE, E LA PROVA E' POSITIVA

**Ognuno degli 82 inglesi apre con «Book of Rank N Magic»**, e il giapponese non
lo dice mai — non su una sola delle 82 righe. E' l'aggiunta dell'inglese piu'
sistematica trovata finora in questo file: non una riga qua e la', ma una
colonna intera.

Si tace, e non perche' «la regola dice cosi'». Vale il controllo della 109a, che
trasforma la regola in un argomento: **questo file, altrove, dice la cosa che
l'inglese aggiunge?** Si' — `db_item.hsp` scrive 「（ランクN）」 quando vuole
dirlo, su **tutti** i letti e su **tutti** i fornelli. Il rango si sa dire; qui
l'autore ha scelto di non dirlo, ed e' la stessa scelta dei quattro strumenti
musicali.

ⓘ E il rango di una magia il giocatore lo legge nella lista degli
incantesimi, non nella scheda dell'oggetto.

### ⭐ LE TRE CLASSI DI MAGIA, che in italiano si leggono in scala

    〜属性の矢       -> una freccia ...        (12 firme)
    〜属性のボルト   -> una saetta ...         (12 firme)
    〜属性の範囲魔法 -> una magia ad area ...  (12 firme)

Trentasei righe su 82 sono questa griglia: **tre classi per dodici elementi**, e
il giapponese la scrive con la stessa frase cambiando due caratteri. In italiano
le tre teste sono tutte **femminili** — freccia, saetta, magia — quindi
l'aggettivo dell'elemento e' lo stesso in tutt'e tre le righe della colonna, e
la griglia si legge per righe e per colonne.

⭐ **I nomi degli elementi non sono stati scelti**: `skill.hsp` ha gia' tutta la
famiglia delle saette — gelo, fuoco, fulmine, d'oscurita', mentale,
d'oltretomba, velenosa, sonora, caotica, dei nervi, magica, d'acqua — ed e' la
famiglia che la 90a aveva riallineato quando `db_item.hsp` diceva «dardo».
Qui le altre due classi si agganciano a quella.

⚠️ **Un'eccezione dentro la griglia, e sta scritta qui perche' e' voluta.**
`:84516` e' 魔法属性 nella classe ad area, e «una magia ad area **magica**» e'
una parola che si morde la coda. Reso «arcana», che `glossario.md` da' come
sinonimo pieno di 魔法 (la riga «`冷気` gelo/ghiaccio, `暗黒` d'oscurita'/oscuro,
… `魔法` magica/arcano»). Sulla **saetta** (`:84443`) e sulla **freccia**
(`:114016`) resta «magica», perche' li' i nomi degli oggetti lo dicono —
«saetta magica grimorio», «freccia magica grimorio».

### ⚠️ LA CODA C'E' O NON C'E', E NON E' UNA SVISTA DA RIPARARE

Cinquantasei righe chiudono con 「読むことができる。」 e ventisei con
「…必要な本だ。」 e basta. Un grimorio si legge sempre, quindi la differenza non
e' un fatto di gioco: e' come e' stato scritto il file.

Si segue il giapponese **riga per riga**. ⭐ E il conto torna da solo: **tutte le
righe lunghe stanno fra quelle senza coda** — i tre grimori degli attributi, le
due resistenze abbassate, l'oracolo, la contingenza — e ci stanno nei 69 proprio
perche' non devono portarsi dietro i diciassette caratteri di «Si può leggere.».
Aggiungere la coda «per uniformita'» avrebbe sfondato il tetto su almeno sei
righe.

### ⓘ Due righe dove il giapponese e l'inglese non dicono la stessa cosa

- **`:105304`, la luce sacra**: il giapponese dice 「**自らの**呪いを一つ打ち消す」,
  *toglie una maledizione a se stessi*; l'inglese dice «It dispels one hex from
  **nearby people**». La gemella `:105231` (pioggia sacra) dice 自らの in
  giapponese e «on the user» in inglese, cioe' l'inglese li' e' d'accordo: e' la
  riga della luce sacra a essersi mossa. Vince il giapponese.
- **`:78730`, la ricetta**: non e' un libro, e' 「紙」, e non si legge — si **usa**
  e si consuma, 「使用することができる（使い捨て）」. E' l'unica riga del lotto
  con la coda della 108a invece di quella dei libri, ed e' anche l'unica che non
  parla di una magia.

### ⓘ I termini, verificati nel dizionario

Le sigle dei tre grimori degli attributi vengono dalle **righe di potenziamento**
degli stessi tre incantesimi (`buff.hsp`), che il dizionario ha gia':
「耐久・魅力を10%と上昇/耐麻痺/耐盲目」 → «Cos e Car +10% … Res+ paralisi,cecità»,
「筋力・器用…/耐恐怖/耐混乱」 → «For e Des … Res+ terrore,confusione»,
「感覚・意志…/耐睡眠/耐混乱」 → «Per e Vol … Res+ sonno,confusione». La scheda
dell'oggetto e la barra dello stato adesso usano le stesse sei sigle e le stesse
cinque parole.

★ → «artefatti» (`glossario.md`, 108ª: le stelle non si scrivono, si scrive quel
che significano) · 呪い → «maledizione» · 鈍足 → «rallentare» ·
加速 → «accelerare» · 沈黙 → «silenzio» · 蜘蛛の巣 → «ragnatela» ·
テレポート → «teletrasporto» · 鑑定 → «identificare» · `HP`, `PV`, `DV`
invariati.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47362
    (47362, 'Book of Rank 6 Magic. Area of Effect spell that does lightning damage.'):
        "Un libro per una magia ad area di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :47435
    (47435, 'Book of Rank 7 Magic. Area of Effect spell that does darkness damage.'):
        "Un libro per una magia ad area d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :47508
    (47508, 'Book of Rank 7 Magic. Area of Effect spell that does nether damage.'):
        "Un libro per una magia ad area d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :47581
    (47581, 'Book of Rank 7 Magic. Area of Effect spell that does poison damage.'):
        "Un libro per una magia ad area velenosa. Si può leggere.",

    # ---------------------------------------------------------- :47654
    (47654, 'Book of Rank 8 Magic. Area of Effect spell that does physical damage.'):
        "Un libro per una magia ad area di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :47727
    (47727, 'Book of Rank 7 Magic. Area of Effect spell that does mind damage.'):
        "Un libro per una magia ad area mentale. Si può leggere.",

    # ---------------------------------------------------------- :47800
    (47800, 'Book of Rank 7 Magic. Area of Effect spell that does nerve damage.'):
        "Un libro per una magia ad area dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :47873
    (47873, 'Book of Rank 5 Magic. Bolt type spell that does nether damage.'):
        "Un libro per una saetta d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :47946
    (47946, 'Book of Rank 5 Magic. Bolt type spell that does poison damage.'):
        "Un libro per una saetta velenosa. Si può leggere.",

    # ---------------------------------------------------------- :48019
    (48019, 'Book of Rank 5 Magic. Bolt type spell that does sound damage.'):
        "Un libro per una saetta sonora. Si può leggere.",

    # ---------------------------------------------------------- :48092
    (48092, 'Book of Rank 5 Magic. Bolt type spell that does chaos damage.'):
        "Un libro per una saetta caotica. Si può leggere.",

    # ---------------------------------------------------------- :48165
    (48165, 'Book of Rank 5 Magic. Bolt type spell that does nerve damage.'):
        "Un libro per una saetta dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :48238
    (48238, 'Book of Rank 2 Magic. Arrow type spell that does fire damage.'):
        "Un libro per una freccia di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :48311
    (48311, 'Book of Rank 2 Magic. Arrow type spell that does cold damage.'):
        "Un libro per una freccia di gelo. Si può leggere.",

    # ---------------------------------------------------------- :48384
    (48384, 'Book of Rank 2 Magic. Arrow type spell that does lightning damage.'):
        "Un libro per una freccia di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :48457
    (48457, 'Book of Rank 3 Magic. Arrow type spell that does mind damage.'):
        "Un libro per una freccia mentale. Si può leggere.",

    # ---------------------------------------------------------- :48530
    (48530, 'Book of Rank 3 Magic. Arrow type spell that does poison damage.'):
        "Un libro per una freccia velenosa. Si può leggere.",

    # ---------------------------------------------------------- :48603
    (48603, 'Book of Rank 3 Magic. Arrow type spell that does sound damage.'):
        "Un libro per una freccia sonora. Si può leggere.",

    # ---------------------------------------------------------- :48676
    (48676, 'Book of Rank 3 Magic. Arrow type spell that does physical damage.'):
        "Un libro per una freccia di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :58996
    (58996, 'Book of Rank 1 Magic. Increases CON/CHR, give resist to Paralysis/Blind.'):
        "Un libro per alzare Cos e Car e resistere a paralisi e cecità.",

    # ---------------------------------------------------------- :61869
    (61869, 'Book of Rank 5 Magic. Bolt type spell that does physical damage.'):
        "Un libro per una saetta di tipo PV/DV. Si può leggere.",

    # ---------------------------------------------------------- :65603
    (65603, 'Book of Rank 1 Magic. Increases PER/WIL, give resist to Sleep/Confuse.'):
        "Un libro per alzare Per e Vol e resistere a sonno e confusione.",

    # ---------------------------------------------------------- :72960
    (72960, 'Book of Rank 2 Magic. It lets you float and dodge inaccurate attacks.'):
        "Un libro per liberarsi dal peso e schivare meglio.",

    # ---------------------------------------------------------- :78730
    (78730, '(Single-use) paper that teaches you new recipes.'):
        "Un foglio per imparare un piatto difficile. Si usa (usa e getta).",

    # ---------------------------------------------------------- :82080
    (82080, 'Book of Rank 4 Magic. It makes gold pieces rain from the sky.'):
        "Un libro per far piovere monete d'oro dal cielo. Si può leggere.",

    # ---------------------------------------------------------- :82153
    (82153, 'Book of Rank 7 Magic. It summons a rift of pocket realm to storage items.'):
        "Un libro per evocare uno spazio dove tenere gli oggetti.",

    # ---------------------------------------------------------- :83558
    (83558, 'Book of Rank 12 Magic. The blessing negates fatal damage occasionally.'):
        "Un libro per azzerare, a volte, un colpo mortale.",

    # ---------------------------------------------------------- :84443
    (84443, 'Book of Rank 2 Magic. Bolt type spell that does magic damage.'):
        "Un libro per una saetta magica. Si può leggere.",

    # ---------------------------------------------------------- :84516
    (84516, 'Book of Rank 5 Magic. Area of Effect spell that does magical damage.'):
        "Un libro per una magia ad area arcana. Si può leggere.",

    # ---------------------------------------------------------- :85104
    (85104, '(Readable) book with ancient knowledge.'):
        "Un libro con dentro un sapere antico. Si può leggere.",

    # ---------------------------------------------------------- :86943
    (86943, 'Book of Rank 4 Magic. Arrow type spell that does darkness damage.'):
        "Un libro per una freccia d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :89013
    (89013, 'Book of Rank 3 Magic. It reset memories of hostile situations.'):
        "Un libro per far dimenticare l'ostilità a chi non è un mostro.",

    # ---------------------------------------------------------- :91985
    (91985, 'Book of Rank 3 Magic. It manifests a door on target object.'):
        "Un libro per aprire una porta dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :92873
    (92873, 'Book of Rank 6 Magic. It can generate walls of flame on targeted spot.'):
        "Un libro per alzare muri di fiamme dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :93225
    (93225, 'Book of Rank 5 Magic. It can generate pools of acid on targeted spot.'):
        "Un libro per creare una pozza d'acido dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :94178
    (94178, 'Book of Rank 5 Magic. It can restore HP of the touched ally.'):
        "Un libro per curare te o un compagno che ti sta accanto.",

    # ---------------------------------------------------------- :94322
    (94322, 'Book of Rank 5 Magic. It can restore HP of every nearby ally.'):
        "Un libro per curare i compagni qui intorno. Si può leggere.",

    # ---------------------------------------------------------- :94457
    (94457, 'Book of Rank 3 Magic. It manifests a wall at target location.'):
        "Un libro per alzare un muro dove vuoi. Si può leggere.",

    # ---------------------------------------------------------- :98652
    (98652, 'Book of Rank 2 Magic. It creates spider webs on the targeted spot.'):
        "Un libro per tendere una ragnatela sul bersaglio. Si può leggere.",

    # ---------------------------------------------------------- :98877
    (98877, "Book of Rank 20 Magic. It bends target's will, making them join you."):
        "Un libro per tirare il bersaglio dalla tua parte. Si può leggere.",

    # ---------------------------------------------------------- :102040
    (102040, 'Book of Rank 20 Magic. It lets you mutate yourself.'):
        "Un libro per farsi venire una mutazione. Si può leggere.",

    # ---------------------------------------------------------- :103652
    (103652, 'Book of Rank 3 Magic. It highlights hidden objects around you.'):
        "Un libro per scoprire gli oggetti qui intorno. Si può leggere.",

    # ---------------------------------------------------------- :104522
    (104522, 'Book of Rank 4 Magic. Helps handling various anomalies created by tomes.'):
        "Un libro per farsi aiutare nella lettura. Si può leggere.",

    # ---------------------------------------------------------- :104595
    (104595, 'Book of Rank 5 Magic. It reduces various magical resistance of target.'):
        "Un libro per abbassare per un po' le resistenze mentali altrui.",

    # ---------------------------------------------------------- :105231
    (105231, 'Book of Rank 8 Magic. It dispels various hex on the user.'):
        "Un libro per togliersi di dosso tutte le maledizioni.",

    # ---------------------------------------------------------- :105304
    (105304, 'Book of Rank 5 Magic. It dispels one hex from nearby people.'):
        "Un libro per togliersi di dosso una maledizione.",

    # ---------------------------------------------------------- :105528
    (105528, 'Book of Rank 8 Magic. It enhances your resistance against curses.'):
        "Un libro per resistere un po' alle maledizioni. Si può leggere.",

    # ---------------------------------------------------------- :105672
    (105672, 'Book of Rank 6 Magic. It reduces elemental magical resistance of target.'):
        "Un libro per abbassare per un po' le resistenze elementali altrui.",

    # ---------------------------------------------------------- :105745
    (105745, 'Book of Rank 4 Magic. It reduces physical resilience of target.'):
        "Un libro per abbassare per un po' il PV del bersaglio.",

    # ---------------------------------------------------------- :105889
    (105889, 'Book of Rank 1 Magic. Increases STR/DEX, give resist to Fear/Confuse.'):
        "Un libro per alzare For e Des e resistere a terrore e confusione.",

    # ---------------------------------------------------------- :106184
    (106184, 'Book of Rank 5 Magic. It reduces the speed of the target..'):
        "Un libro per rallentare il bersaglio. Si può leggere.",

    # ---------------------------------------------------------- :106257
    (106257, 'Book of Rank 9 Magic. It increases the speed of user.'):
        "Un libro per accelerare. Si può leggere.",

    # ---------------------------------------------------------- :106401
    (106401, 'Book of Rank 4 Magic. It raises various magical resistance of user.'):
        "Un libro per alzare per un po' le resistenze. Si può leggere.",

    # ---------------------------------------------------------- :106545
    (106545, 'Book of Rank 5 Magic. It activates the healing factor of the user.'):
        "Un libro per alzare per un po' la guarigione. Si può leggere.",

    # ---------------------------------------------------------- :106689
    (106689, 'Book of Rank 6 Magic. It silences the target.'):
        "Un libro per mettere il bersaglio in silenzio. Si può leggere.",

    # ---------------------------------------------------------- :106842
    (106842, 'Book of Rank 2 Magic. Raise ones dodge abilities and give resist to fear.'):
        "Un libro per alzare per un po' il DV e resistere al terrore.",

    # ---------------------------------------------------------- :111853
    (111853, 'Book of Rank 50 Magic. It grants the user a chance to say their wishes.'):
        "Un libro per poter esprimere un desiderio. Si può leggere.",

    # ---------------------------------------------------------- :112955
    (112955, 'Book of Rank 7 Magic. Area of Effect spell that does chaos damage.'):
        "Un libro per una magia ad area caotica. Si può leggere.",

    # ---------------------------------------------------------- :113028
    (113028, 'Book of Rank 7 Magic. Area of Effect spell that does sound damage.'):
        "Un libro per una magia ad area sonora. Si può leggere.",

    # ---------------------------------------------------------- :113101
    (113101, 'Book of Rank 6 Magic. Area of Effect spell that does fire damage.'):
        "Un libro per una magia ad area di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :113174
    (113174, 'Book of Rank 6 Magic. Area of Effect spell that does cold damage.'):
        "Un libro per una magia ad area di gelo. Si può leggere.",

    # ---------------------------------------------------------- :113247
    (113247, 'Book of Rank 6 Magic. Bolt type spell that does mind damage.'):
        "Un libro per una saetta mentale. Si può leggere.",

    # ---------------------------------------------------------- :113320
    (113320, 'Book of Rank 6 Magic. Bolt type spell that does darkness damage.'):
        "Un libro per una saetta d'oscurità. Si può leggere.",

    # ---------------------------------------------------------- :113462
    (113462, 'Book of Rank 3 Magic. Arrow type spell that does nerve damage.'):
        "Un libro per una freccia dei nervi. Si può leggere.",

    # ---------------------------------------------------------- :113535
    (113535, 'Book of Rank 3 Magic. Arrow type spell that does chaos damage.'):
        "Un libro per una freccia caotica. Si può leggere.",

    # ---------------------------------------------------------- :113608
    (113608, 'Book of Rank 3 Magic. Arrow type spell that does nether damage.'):
        "Un libro per una freccia d'oltretomba. Si può leggere.",

    # ---------------------------------------------------------- :114016
    (114016, 'Book of Rank 1 Magic. Arrow type spell that does magical damage.'):
        "Un libro per una freccia magica. Si può leggere.",

    # ---------------------------------------------------------- :114353
    (114353, 'Book of Rank 12 Magic. It heals the spell user greatly.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114426
    (114426, 'Book of Rank 8 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114499
    (114499, 'Book of Rank 4 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114572
    (114572, 'Book of Rank 1 Magic. It heals the spell user.'):
        "Un libro per recuperare HP. Si può leggere.",

    # ---------------------------------------------------------- :114645
    (114645, 'Book of Rank 6 Magic. It teleports user to location across the continent.'):
        "Un libro per tornare in un posto preciso. Si può leggere.",

    # ---------------------------------------------------------- :114718
    (114718, 'Book of Rank 15 Magic. It shows the user location of powerful artifacts.'):
        "Un libro per sapere dove sono finiti gli artefatti apparsi.",

    # ---------------------------------------------------------- :114791
    (114791, 'Book of Rank 5 Magic. It illuminates nearby walls to create a map.'):
        "Un libro per rivelare le zone non esplorate. Si può leggere.",

    # ---------------------------------------------------------- :123360
    (123360, 'Book of Rank 3 Magic. It summons several monsters from a nearby Nefia.'):
        "Un libro per evocare mostri. Si può leggere.",

    # ---------------------------------------------------------- :123495
    (123495, 'Book of Rank 1 Magic. It teleports user for a short distance.'):
        "Un libro per un teletrasporto corto. Si può leggere.",

    # ---------------------------------------------------------- :128871
    (128871, 'Book of Rank 4 Magic. Bolt type spell that does lightning damage.'):
        "Un libro per una saetta di fulmine. Si può leggere.",

    # ---------------------------------------------------------- :128944
    (128944, 'Book of Rank 4 Magic. Bolt type spell that does fire damage.'):
        "Un libro per una saetta di fuoco. Si può leggere.",

    # ---------------------------------------------------------- :129017
    (129017, 'Book of Rank 4 Magic. Bolt type spell that does ice damage.'):
        "Un libro per una saetta di gelo. Si può leggere.",

    # ---------------------------------------------------------- :129727
    (129727, 'Book of Rank 7 Magic. It uncursed equipped items.'):
        "Un libro per purificare gli oggetti. Si può leggere.",

    # ---------------------------------------------------------- :129800
    (129800, 'Book of Rank 8 Magic. It identifies an item for the user.'):
        "Un libro per identificare un oggetto. Si può leggere.",

    # ---------------------------------------------------------- :129873
    (129873, 'Book of Rank 5 Magic. It teleports user for a distance.'):
        "Un libro per il teletrasporto. Si può leggere.",

# 82 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-011.jsonl'
RIGHE = {
    47362, 47435, 47508, 47581, 47654, 47727, 47800, 47873, 47946, 48019,
    48092, 48165, 48238, 48311, 48384, 48457, 48530, 48603, 48676, 58996,
    61869, 65603, 72960, 78730, 82080, 82153, 83558, 84443, 84516, 85104,
    86943, 89013, 91985, 92873, 93225, 94178, 94322, 94457, 98652, 98877,
    102040, 103652, 104522, 104595, 105231, 105304, 105528, 105672, 105745, 105889,
    106184, 106257, 106401, 106545, 106689, 106842, 111853, 112955, 113028, 113101,
    113174, 113247, 113320, 113462, 113535, 113608, 114016, 114353, 114426, 114499,
    114572, 114645, 114718, 114791, 123360, 123495, 128871, 128944, 129017, 129727,
    129800, 129873,
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
