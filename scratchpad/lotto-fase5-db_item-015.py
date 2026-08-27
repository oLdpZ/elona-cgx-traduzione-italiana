# -*- coding: utf-8 -*-
"""111a - Lotto 015 di `db_item.hsp`: il rapporto delle ARMATURE del corpo.

`FILTER_ARMOR`, `description(3)`: **20 righe del sorgente, 20 firme**, 20
giapponesi distinti. Il seguito diretto del lotto 014: stesse scale, stesse
parole, e due formule nuove.

### ⭐ TRE PAROLE GIAPPONESI PER «COSA CHE SI INDOSSA», TENUTE DISTINTE

    服     -> vestito     (sei righe)
    鎧     -> corazza     (i nomi lo dicono gia': 軽鎧 «corazza leggera»,
                           輪鎧 «corazza ad anelli», 重層鎧 «corazza a
                           piastre», 厚鎧 «corazza a bande»)
    アーマー / スーツ -> armatura / tuta   (i katakana, cioe' i moderni)
    防具   -> armatura    (:130782, come nel lotto 014)

⚠️ 衣服 e' gia' «vestiti» in questo stesso file (i vestiti sporchi nel cesto):
服 segue quella parola, non i nomi degli oggetti — che sono tutti diversi
(giubbotto, cappotto, veste papale) proprio perche' il giapponese e' generico.

### ⭐ DUE FORMULE, e si scrivono in fila o non si leggono come formule

**「〜ために作られた服だ」, tre righe:**

    銃弾を防ぐために作られた服 -> fatto per fermare i proiettili  (:101382)
    攻撃を防ぐために作られた服 -> fatto per parare i colpi         (:101512)
    法王のために作られた服     -> fatto per il papa                (:101642)

**「〜を束ねて作った鎧だ」, due righe** — 束ねて e' gia' «legando insieme» nel
dizionario (il mostro-occhio che lega insieme nervi e muscoli):

    薄片を束ねて作った鎧 -> fatta legando insieme delle lamelle  (:101707)
    輪を束ねて作った鎧   -> fatta legando insieme degli anelli   (:101837)

### ⭐ LA SCALA DEL PESO E DELLA DUREZZA CONTINUA DAL LOTTO 014

Scudi e corazze usano le **stesse** parole, e le rese devono combaciare o la
scala si spezza a meta' categoria:

    非常に重い  -> pesantissimo/a   (:100720 scudo, :101902 corazza)
    固い        -> duro/a           (:100852 scudo, :101772 corazza)
    分厚い      -> spessa           (:101967), gia' «spesso» nel dizionario
                                     (分厚い魔法書 «libro spesso»)

### ⭐⭐ `:75986` — 拘束具 ERA GIA' «GABBIA», E LA RIGA E' LA GEMELLA DI `:57965`

`chat.hsp` ha gia' 「これは装甲板ではない、拘束具だ。…これを身に着け抑え込む
がいい」 reso **«Questa non è una piastra d'armatura: è una gabbia»** — stesso
verbo (身に着ける), stesso oggetto. Quindi:

    :57965  身に着けると変形して手枷になる   -> si trasforma in ceppi  (lotto 014)
    :75986  身に着けると変形して拘束具になる -> si trasforma in una gabbia

Sono due artefatti gemelli, 《神々の枷鎖》 e 《機械拘束具》, e la coppia si
legge solo se la costruzione resta la stessa e cambia **solo** il nome della
cosa — che e' quel che fa il giapponese.

### ⚠️ 何度でも使用することができる ERA GIA' RESO, PIU' DI OTTANTA VOLTE

`:51643` porta la coda 「何度でも使用することができる。」, che il dizionario
rende **«Si può usare sempre.»**. Non e' una scelta di questo lotto: e' un
ritrovamento, come le cinque code su sei della 110a.

### ⓘ Una parola su 高性能

`:70533` e' 高性能な特殊スーツだ e diventa «ad alte prestazioni». Il lotto 013
rendeva 高性能だが重い光子銃 con «potente, ma pesante»: li' la parola stava in
una coppia contrapposta e «potente» reggeva il contrasto; qui e' sola, e la
tuta non e' potente — e' fatta bene.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :51643
    (51643, "(Reusable) clothes that changes it's appearance."):
        "Un vestito che cambia aspetto. Si può usare sempre.",

    # ---------------------------------------------------------- :51710
    (51710, 'It is a bamboo armor that makes cracking sounds.'):
        "Un'armatura di bambù che sbatacchia forte.",

    # ---------------------------------------------------------- :56673
    (56673, 'It is an outfit has many belts attached to it.'):
        "Un vestito pieno di cinghie.",

    # ---------------------------------------------------------- :65812
    (65812, 'It is an armor for colder regions of Irva.'):
        "Una corazza fatta per le terre fredde.",

    # ---------------------------------------------------------- :70466
    (70466, 'It is a very fragile suit in terms of molecular structure.'):
        "Una tuta fragilissima nella struttura molecolare.",

    # ---------------------------------------------------------- :70533
    (70533, 'It is a high-performance special suit.'):
        "Una tuta speciale ad alte prestazioni.",

    # ---------------------------------------------------------- :75986
    (75986, 'It is a godly gift that when worn, transforms and becomes a restraint.'):
        "Se lo indossi, si trasforma in una gabbia.",

    # ---------------------------------------------------------- :77564
    (77564, 'It is a special suit that look like a swimwear.'):
        "Una tuta speciale che sembra un costume da bagno.",

    # ---------------------------------------------------------- :101382
    (101382, 'These clothes are made to protect against bullets, and much more.'):
        "Un vestito fatto per fermare i proiettili.",

    # ---------------------------------------------------------- :101447
    (101447, 'It is an armor designed to protect the chest.'):
        "Un vestito con del metallo sul davanti.",

    # ---------------------------------------------------------- :101512
    (101512, 'These are clothings designed to protect against attacks.'):
        "Un vestito fatto per parare i colpi.",

    # ---------------------------------------------------------- :101577
    (101577, 'It is a mail with thin plating.'):
        "Una corazza leggera.",

    # ---------------------------------------------------------- :101642
    (101642, 'These clothes were made for high-ranked priests.'):
        "Un vestito fatto per il papa.",

    # ---------------------------------------------------------- :101707
    (101707, 'It is an armor made of small linked rings.'):
        "Una corazza fatta legando insieme delle lamelle.",

    # ---------------------------------------------------------- :101772
    (101772, 'It is a sturdy armor reinforced with composite mesh.'):
        "Una corazza dura.",

    # ---------------------------------------------------------- :101837
    (101837, 'It is an armor made of a bundle of rings.'):
        "Una corazza fatta legando insieme degli anelli.",

    # ---------------------------------------------------------- :101902
    (101902, 'It is a very heavy armor.'):
        "Una corazza pesantissima.",

    # ---------------------------------------------------------- :101967
    (101967, 'It is a form of reinforced mail armor.'):
        "Una corazza spessa.",

    # ---------------------------------------------------------- :130717
    (130717, 'It is a common robe for monks.'):
        "Un vestito da monaco.",

    # ---------------------------------------------------------- :130782
    (130782, "It is an armor that offer's decent protection to the torso."):
        "Un'armatura da combattimento, per proteggere il corpo.",

# 20 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-015.jsonl'
RIGHE = {
    51643, 51710, 56673, 65812, 70466, 70533, 75986, 77564, 101382, 101447,
    101512, 101577, 101642, 101707, 101772, 101837, 101902, 101967, 130717, 130782,
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
