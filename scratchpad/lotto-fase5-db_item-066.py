# -*- coding: utf-8 -*-
"""122a - Lotto 066 di `db_item.hsp`: I GUANTI, e la categoria CHIUDE.

`FILTER_GLOVES`, righe da `:62801` a `:130649`: **10 righe**, tutte dell'indice
0, su 10 oggetti. Con questo lotto `FILTER_GLOVES` va a **0 da fare su 10
vive**, ed e' la **ventunesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 066`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 066`: 0 su 10. `_code.py 066`: 0 righe senza
resa in tabella. `_forma.py 066`: 10 su 10 con lo spazio prima del `\\n`.

### ⭐⭐⭐ IL PRIMO LOTTO CON LA RETE DELLE SORELLE, E HA CAMBIATO DUE RESE

`scratchpad/_122-sorelle-per-frase.py` e' stato scritto un'ora fa, dopo che
questa sessione aveva incontrato **tre volte** una riga sorella in un altro
lotto e l'aveva trovata ogni volta a mano. Sul 066 ha risposto in due secondi e
mezzo con **sette frasi**, cinque delle quali gia' rese.

**La famiglia dei materiali speciali ha SEI membri, non tre.** Prima di oggi se
ne conoscevano due (`:100849` e `:101769`, la 121a), stamattina e' diventata
tre col lotto 063, e adesso si vede tutta:

    :100849 (058)  盾 lo scudo        reso
    :101769 (060)  鎧 la corazza      reso
    :99872  (063)  兜 l'elmo          reso
    :101114 (066)  篭手 i guanti      <- questo lotto
    :100392 (---)  腰当 la cintura    DA FARE, FILTER_GIRDLE
    :130450 (---)  靴 gli stivali     DA FARE, FILTER_BOOTS

⭐ **Le ultime due righe sono il vero risultato**: non sono un difetto trovato,
sono due lotti futuri che adesso sanno gia' con che frase devono aprire. Finora
questa cosa si scopriva **dopo**, e nella 121a il lotto 014 aveva reso una riga
in un modo che il lotto 024 aveva dovuto disfare.

**E la famiglia di 〜を守る為に作られた ha QUATTRO membri:**

    :99937  (063)  頭部を守る為に作られた防具      la testa
    :99663  (064)  首を守る為に作られた装身具      il collo
    :130582 (066)  手首から先を守る為に作られた防具  dal polso in avanti

⚠️ Questa la rete l'ha trovata solo dopo aver abbassato la soglia della frase
minima da 14 a 12 caratteri: 頭部を守る為に作られた防具 e' lungo **13**, e sotto
i 14 non entrava nemmeno nell'indice. Il conto e' stato fatto, non ipotizzato —
a 12 le frasi trovate passano da 5 a 7 e le due nuove sono tutt'e due vere,
zero rumore.

### ⭐ DUE PAROLE CHE IL GIOCATORE HA TUTT'E DUE IN INVENTARIO

篭手 e 小手 sono i **guanti d'arme**, 手袋 sono i **guanti** e basta: la
categoria contiene sia gli uni sia gli altri, e gli indici 3 gia' in gioco li
distinguono («Dei guanti d'arme duri», «Dei guanti sottili»). Le rese lunghe
tengono la stessa distinzione.
ⓘ E i guanti d'arme sono **plurali** in italiano: l'apertura della famiglia dei
materiali diventa «Dei guanti d'arme che… **hanno** ottenuto», dove lo scudo e
l'elmo dicono «ha ottenuto». Cambia l'accordo, non la frase.

### ⓘ Le decisioni minori, e da dove vengono

  - 富の神 (`:75647`) -> «la dea della ricchezza», gia' in gioco sulla statua
    che la raffigura; e' Yacatect, che nel gioco parla al femminile;
  - 火炎竜 (`:107527`) -> «il drago di fuoco», dal dizionario delle creature
    («il drago di fuoco adulto», «il cucciolo di drago di fuoco»);
  - 甲冑 (`:101114`) -> «l'armatura di piastre», la parola del lotto 060
    (`:101899`, «sovrappone le piastre alla cotta di maglia»);
  - 隕鉄 (`:62801`) non e' nel dizionario da nessuna parte: e' il **ferro
    meteorico**, e l'inglese lo dice pure. Il nome dell'oggetto — «Cesto delle
    Meteore» — e il suo indice 3, che parla gia' di uno sciame di meteore, ci
    vanno d'accordo;
  - 武骨 -> «rozzo», terza occorrenza dopo la gorgiera (064) e l'anello del
    drago d'acciaio (065);
  - `:101247` chiude con やや重いがそれでも尚余りある, che e' l'eco di
    `:100849`, lo scudo dello stesso libro: la resa riprende «rendono molto più
    di quel poco che pesano in più».

### ⓘ Il preflight ha segnalato una parola lunga, e non e' un difetto

`dall'avambraccio` (16). Vale la misura del lotto 063: il tetto vero e' il
budget da 77 del corpo impaginato, e il cancello di `_107-descrizioni-item`
legge 0 parole spezzate.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :62801
    (62801, 'Sturdy white leather strap with metal fittings hammered into it. It is worn around the forearm and fist like a bandage. The metal fittings made of meteoric iron are said to contain magical power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una cinghia di cuoio bianca e robusta, con delle borchie di metallo conficcate dentro. Si equipaggia avvolgendola dall'avambraccio fino al pugno, come una fasciatura. Pare che nelle borchie, fatte di ferro meteorico, ci sia dentro del potere magico. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75647
    (75647, 'Flashy chains that the God of Wealth had custom-made. It is so gorgeous that just looking at it makes you feel sick. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una catena vistosissima, che la dea della ricchezza si è fatta fare su misura. È di uno sfarzo tale che a guardarla viene il voltastomaco. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75714
    (75714, 'A blue glove with a mysterious pattern on its surface. It holds a spirit. \\n# ~Irva Fantasy Encyclopedia~'):
        "Dei guanti d'arme azzurri, con un disegno misterioso sulla superficie. Ci abita dentro uno spirito. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :101114
    (101114, 'A bracer made of a combination of special materials to provide stronger protection. It is mainly worn with armor. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme che, incrociando materiali speciali, hanno ottenuto una protezione più solida. Si portano soprattutto in accordo con l'armatura di piastre. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101180
    (101180, 'These gloves are made to stick snugly to the skin. They are so light that you may forget you are wearing them. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti fatti per aderire perfettamente alla pelle. Sono leggerissimi, tanto che ci si dimentica di averli addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101247
    (101247, 'These are warrior-style kote, made with an emphasis on protection above all else. They are somewhat heavy, but still have more than enough performance. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme rozzi, fatti mettendo la protezione davanti a tutto. Pesano un po', ma rendono molto più di quel poco che pesano in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :101314
    (101314, 'This armor is also meant to be a cold-weather gear. Not only that, it is also said to have no small effect as an anti-slip device for weapons. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura che vale anche come riparo dal freddo. E non solo: dicono che serva non poco anche a non far scivolare l'arma di mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :107527
    (107527, 'Made from parts of flame dragons. True to the rumor, it is always enveloped in flames, but the wearer does not feel the heat, let alone burn. \\n# ~Irva Fantasy Encyclopedia~'):
        "Dei guanti d'arme che dicono ricavati da un drago di fuoco. Come vuole la voce sono sempre avvolti nelle fiamme, eppure chi li porta, altro che bruciare, non sente nemmeno il caldo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :130582
    (130582, 'Armor made to protect the wrist and forearm. It does take away some of the freedom of the fingers, but it is better than losing a hand. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta per proteggere dal polso in avanti. Toglie un po' di libertà alle dita, ma è meglio che perdere una mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130649
    (130649, 'Fine gloves covered with assorted ornaments. Despite its ceremonial aspect, it still provides some protection through its decoration. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Dei guanti d'arme di pregio, cosparsi di lavorazioni d'ogni sorta. Contano soprattutto per la cerimonia, ma anche così quegli ornamenti una qualche protezione la danno. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-066.jsonl'
RIGHE = {
    62801, 75647, 75714, 101114, 101180, 101247, 101314, 107527, 130582, 130649,
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
