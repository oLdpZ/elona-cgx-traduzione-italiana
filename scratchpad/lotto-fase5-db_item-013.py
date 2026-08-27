# -*- coding: utf-8 -*-
"""110a - Lotto 013 di `db_item.hsp`: il rapporto delle armi a DISTANZA.

`FILTER_RANGE`, `description(3)`: **56 righe del sorgente, 55 firme**, 53
giapponesi distinti. Come le armi da mischia del lotto 012, nessuna formula: un
vocabolario, e una scala.

### ⭐ LA SCALA DELLA GITTATA, quattro scalini e una parola sola

Il giapponese grada quanto un'arma da fuoco perde con la distanza usando sempre
**減衰**, *il calo*, e cambiando solo l'avverbio. In italiano tradotti uno per
uno darebbero quattro frasi che non si confrontano: la resa li mette in fila con
lo stesso verbo, cosi' l'ordine si vede leggendoli di seguito.

    遠距離でも安定した威力     -> tiene la forza anche a distanza  (:76392)
    距離による減衰が殆どない   -> con la distanza non cala quasi   (:96713)
    距離による減衰が少ない     -> con la distanza cala poco        (:115799)
    距離によって威力が減衰する -> con la distanza perde forza      (:127141)

E' la stessa mossa della **scala della luce** della 109a (cinque scalini, un
nome piu' un aggettivo) e per la stessa ragione: quattro righe che il giocatore
legge in schede diverse, e che devono restare confrontabili.

ⓘ Accanto ci sta `:97806`, 有効射程が短い, che non e' della scala — parla della
**gittata utile**, non del calo — e infatti dice un'altra cosa: «porta poco
lontano».

### ⚠️ DUE MITRAGLIATRICI, DUE MODI DI DIRE «MOLTO PESANTE»

`:77148` e' 非常に重い e `:77916` e' とても重い. Sono due giapponesi distinti,
quindi due rese distinte: **«pesantissima»** e **«molto pesante»**. Renderle
uguali sarebbe stato piu' liscio e avrebbe cancellato una differenza che il
sorgente scrive.

⚠️ **E il contrario e' altrettanto vero**: `:68185` e `:117188` hanno lo
**stesso** giapponese (「投擲用武器だ。」) e due inglesi diversi — «Difficult to
use. Hurt as hell when hit.» contro «It is just a stone.». Stessa resa. E
`:72354`, `:74238`, `:83345` sono **tre** righe con un giapponese solo: una resa
per tre.

### ⓘ Il vocabolario, dai nomi degli oggetti

弩/クロスボウ «balestra» · 弩砲 «balista» · 連弩 «arco a ripetizione» ·
短弓 «arco corto» · 長弓 «arco lungo» · 機械弓 «arco meccanico» ·
銃器 «arma da fuoco» · 拳銃 «pistola» · 双銃 «pistole gemelle» ·
狙撃銃 «fucile di precisione» · 散弾銃 «fucile a pompa» ·
機関銃 «mitragliatrice» · 光子銃 «pistola laser» · 手榴弾 «granata» ·
手裏剣 «shuriken» (`invariati.md`) · 投擲用武器 «arma da lancio».

### ⚠️ 風の神 e' una DEA, e a dirlo non e' il giapponese

`:86070`: 「風の神から下賜される長弓だ。」. Il giapponese scrive 神, che non ha
genere; l'inglese scrive «Goddess of Wind»; e Lulwy e' una divinita' femminile.
L'italiano il genere lo deve scegliere, e lo sceglie come lo ha gia' scelto
**questo stesso file**: 「風の女神の写真集」 e 「風の女神を模った彫像」 sono resi
«la dea del vento» da sessioni precedenti. Reso «la dea del vento».

ⓘ La gemella `:86000`, 機械の神, e' «il dio delle macchine» per la stessa strada
(「機械の神を模した目覚まし時計」).

⚠️ **Non e' un caso isolato ma il seguito del lotto 012**, dove le cinque armi
degli dei hanno preso i nomi dalle statue e dai pendoli. Sette righe in due
lotti, e nessuna ha avuto bisogno di una decisione nuova.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43634
    (43634, "It's a bunch of explosive leaves."):
        "Delle foglie che esplodono.",

    # ---------------------------------------------------------- :43708
    (43708, '(Reusable) throwable artefact.'):
        "Si può usare sempre. Vale anche da arma da lancio.",

    # ---------------------------------------------------------- :52651
    (52651, 'It is an exploding fried shrimp. Can be used as a grenade.'):
        "Un gambero fritto che esplode. Vale da granata.",

    # ---------------------------------------------------------- :53351
    (53351, 'It is an imperfect mechanical flame crossbow.'):
        "Una balestra di fuoco a ingranaggi, non finita.",

    # ---------------------------------------------------------- :53492
    (53492, 'It is a crossbow designed for extreme ranges.'):
        "Una balista fatta per il tiro di precisione.",

    # ---------------------------------------------------------- :53564
    (53564, 'It is a giant rock that reeks of death.'):
        "Una scheggia di roccia gigantesca.",

    # ---------------------------------------------------------- :53634
    (53634, 'It is a crossbow with the image of a viper.'):
        "Un arco a ripetizione ispirato a un serpente velenoso.",

    # ---------------------------------------------------------- :53704
    (53704, 'It is a very small shortbow.'):
        "Un arco corto piccolissimo.",

    # ---------------------------------------------------------- :54670
    (54670, 'It is a bow with a blade.'):
        "Un arco con le lame.",

    # ---------------------------------------------------------- :54746
    (54746, 'It is a crossbow with a mechanism to ignite the arrow.'):
        "Una balestra con un meccanismo che accende le frecce.",

    # ---------------------------------------------------------- :54822
    (54822, 'These are two-in-one small firearms.'):
        "Due armi da fuoco piccole che fanno una cosa sola.",

    # ---------------------------------------------------------- :57387
    (57387, 'It is a beetles made for throwing.'):
        "Uno scarabeo da lanciare.",

    # ---------------------------------------------------------- :61446
    (61446, 'It is a terrifying bone bow.'):
        "Un arco d'ossa che fa ribrezzo.",

    # ---------------------------------------------------------- :61516
    (61516, 'It is a slashing bow that can also release electric shocks.'):
        "Un arco tagliente che scaglia anche fulmini.",

    # ---------------------------------------------------------- :64416
    (64416, 'It is a wheel-shaped shuriken.'):
        "Uno shuriken a forma di anello.",

    # ---------------------------------------------------------- :65066
    (65066, 'It is a high-performance but heavy photon gun.'):
        "Una pistola laser potente, ma pesante.",

    # ---------------------------------------------------------- :67261
    (67261, 'It is a supersized crossbow.'):
        "Una balestra grandissima.",

    # ---------------------------------------------------------- :67393
    (67393, 'It is a large caliber sniper rifle.'):
        "Un fucile di precisione di grosso calibro.",

    # ---------------------------------------------------------- :68185
    (68185, 'It is a throwing weapon. Difficult to use. Hurt as hell when hit.'):
        "Un'arma da lancio.",

    # ---------------------------------------------------------- :68329
    (68329, 'It is a small crossbow with poison to compensate for their power.'):
        "Una balestra piccola, che al poco potere supplisce col veleno.",

    # ---------------------------------------------------------- :71582
    (71582, 'These are twin guns that look like they could combine somehow.'):
        "Due pistole gemelle che paiono voler diventare una.",

    # ---------------------------------------------------------- :72284
    (72284, 'It is a shotgun for close-quarter combat.'):
        "Un fucile a pompa per il corpo a corpo.",

    # ---------------------------------------------------------- :72354
    (72354, 'It is a thrown weapon that causes the opponent to bleed.'):
        "Un'arma da lancio che fa sanguinare il nemico.",

    # ---------------------------------------------------------- :72693
    (72693, 'It is a seven colored longbow.'):
        "Un arco lungo dai colori dell'arcobaleno.",

    # ---------------------------------------------------------- :72763
    (72763, 'It is a mechanical bow with enhanced firing rate.'):
        "Un arco meccanico che spara più colpi di fila.",

    # ---------------------------------------------------------- :73225
    (73225, 'It is a grenade with a powerful blast.'):
        "Una granata con uno scoppio potente.",

    # ---------------------------------------------------------- :74238
    (74238, 'It is a throwing weapon that causes the opponent to bleed.'):
        "Un'arma da lancio che fa sanguinare il nemico.",

    # ---------------------------------------------------------- :74506
    (74506, 'It is a throwing knife.'):
        "Un coltello da lancio.",

    # ---------------------------------------------------------- :75518
    (75518, 'It is a terrific to hold, very heavy stone coin.'):
        "Una moneta di pietra pesantissima: portarla basta a stupire.",

    # ---------------------------------------------------------- :76392
    (76392, 'It is a firearm that are stable and powerful even at long distances.'):
        "Un'arma da fuoco che tiene la forza anche a distanza.",

    # ---------------------------------------------------------- :76461
    (76461, 'It is a very customized sniper rifle.'):
        "Un fucile di precisione modificato parecchio.",

    # ---------------------------------------------------------- :77078
    (77078, 'It is a very heavy mechanical bow.'):
        "Un arco meccanico pesantissimo.",

    # ---------------------------------------------------------- :77148
    (77148, 'It is a very heavy machine gun.'):
        "Una mitragliatrice pesantissima.",

    # ---------------------------------------------------------- :77427
    (77427, 'These are twin guns that look exactly alike.'):
        "Due pistole gemelle uguali come due gocce d'acqua.",

    # ---------------------------------------------------------- :77846
    (77846, 'These are old money. Can be used for throwing.'):
        "Soldi d'una volta. Si possono lanciare come mance.",

    # ---------------------------------------------------------- :77916
    (77916, 'It is a very heavy machine gun.'):
        "Una mitragliatrice molto pesante.",

    # ---------------------------------------------------------- :78401
    (78401, 'It is a bow made of processed bone.'):
        "Un arco lavorato nell'osso.",

    # ---------------------------------------------------------- :80359
    (80359, 'It is a pistol that strikes down even those it cannot see.'):
        "Una pistola che passa da parte a parte anche chi non si vede.",

    # ---------------------------------------------------------- :82550
    (82550, 'It is a heavy piano for assassination.'):
        "Un pianoforte pesante, fatto per assassinare.",

    # ---------------------------------------------------------- :83018
    (83018, "It is Shena's used underwears."):
        "La biancheria che Shena ha portato.",

    # ---------------------------------------------------------- :83149
    (83149, 'It is a heavy pebble. Can be equipped.'):
        "Un sasso pesante. Si può equipaggiare.",

    # ---------------------------------------------------------- :83278
    (83278, 'It is a throwing weapon that creates a blast around it when it lands.'):
        "Un'arma da lancio che cadendo fa scoppiare l'aria intorno.",

    # ---------------------------------------------------------- :86000
    (86000, 'It is a shotgun bestowed by the God of Machine.'):
        "Un fucile a pompa donato dal dio delle macchine.",

    # ---------------------------------------------------------- :86070
    (86070, 'It is a longbow bestowed by the Goddess of Wind.'):
        "Un arco lungo donato dalla dea del vento.",

    # ---------------------------------------------------------- :88673
    (88673, 'It is an underwear worn by a woman.'):
        "La biancheria che ha portato una donna.",

    # ---------------------------------------------------------- :96570
    (96570, 'It is a photon gun with various magical effects.'):
        "Una pistola laser con effetti magici di ogni genere.",

    # ---------------------------------------------------------- :96713
    (96713, 'It is a firearm with little or no attenuation with distance.'):
        "Un'arma da fuoco che con la distanza non cala quasi.",

    # ---------------------------------------------------------- :97806
    (97806, 'It is a firearm with a short effective range.'):
        "Un'arma da fuoco che porta poco lontano.",

    # ---------------------------------------------------------- :98804
    (98804, 'It is a weapon to be equipped along with a bundle of crossbow bolts.'):
        "Un'arma da tiro che si equipaggia coi dardi da balestra.",

    # ---------------------------------------------------------- :115799
    (115799, 'It is a firearm with good medium range accuracy.'):
        "Un'arma da fuoco che con la distanza cala poco.",

    # ---------------------------------------------------------- :115875
    (115875, 'It is a bow specialized for short to medium range.'):
        "Un arco buono da vicino e a media distanza.",

    # ---------------------------------------------------------- :117188
    (117188, 'It is just a stone.'):
        "Un'arma da lancio.",

    # ---------------------------------------------------------- :117391
    (117391, 'It is a longbow with the power to draw in the enemy.'):
        "Un arco lungo che ha la forza di tirarti addosso i nemici.",

    # ---------------------------------------------------------- :127141
    (127141, 'It is a firearm made for short distances.'):
        "Un'arma da fuoco che con la distanza perde forza.",

    # ---------------------------------------------------------- :127283
    (127283, 'It is a bow specialized for medium to long range.'):
        "Un arco buono a media e lunga distanza.",

# 55 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-013.jsonl'
RIGHE = {
    43634, 43708, 52651, 53351, 53492, 53564, 53634, 53704, 54670, 54746,
    54822, 57387, 61446, 61516, 64416, 65066, 67261, 67393, 68185, 68329,
    71582, 72284, 72354, 72693, 72763, 73225, 74238, 74506, 75518, 76392,
    76461, 77078, 77148, 77427, 77846, 77916, 78401, 80359, 82550, 83018,
    83149, 83278, 86000, 86070, 88673, 96570, 96713, 97806, 98804, 115799,
    115875, 117188, 117391, 127141, 127283,
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
