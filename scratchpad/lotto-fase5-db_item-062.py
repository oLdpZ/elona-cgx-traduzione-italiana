# -*- coding: utf-8 -*-
"""122a - Lotto 062 di `db_item.hsp`: GLI ALBERI, e la categoria CHIUDE.

`FILTER_ENVIRONMENT`, righe da `:68450` a `:95920`: **13 righe** — 12
dell'indice 0 e **una dell'indice 2** (`:95672`, la battuta di <Barius>) — su
11 oggetti. Con questo lotto `FILTER_ENVIRONMENT` va a **0 da fare su 13 vive**,
ed e' la **diciassettesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 062`: **+13** per 13 rese,
nessuna gemella. ⓘ `_gia-reso.py 062`: 0 su 13. `_code.py 062`: 0 righe senza
resa in tabella. `_forma.py 062`: 13 su 13 con lo spazio prima del `\\n`.

### ⭐⭐⭐ LA RETE NUOVA ARRIVA PRIMA DEL DANNO, E QUESTO E' IL PUNTO

Il lotto 061 aveva scoperto per fortuna che l'inglese di `:56267` era quello
dell'oggetto successivo, e la fortuna era che le due righe fossero cadute nello
stesso lotto. Da li' e' nato `scratchpad/_122-inglese-doppio-item.py`, che fa la
stessa domanda su **tutto `db_item.hsp`** invece che dentro un lotto. Fra i
dieci gruppi che ha trovato, uno solo riguardava righe **non ancora tradotte**:

    :91522  (モミ, l'abete)  実を落とさない常緑樹。…ノイエルで祭りが行われる
    :95858  (スギ, il cedro) 実を落とさない常緑樹。…この木の花粉だった

    en (tutt'e due)  «…festivals are held in Noyel to celebrate the Saint by
                       decorating these trees with various ornaments.»

Il giapponese del cedro non parla di feste: parla del **polline**, e della
battuta di chi crede che qualcuno gli stia intralciando gli incantesimi e
scopre che era l'albero. Tradotto dall'inglese, il cedro avrebbe portato la
festa di Noyel dell'abete, e **nessun cancello lo avrebbe visto**: la riga
sarebbe stata pulita in ogni senso misurabile.

⭐ E' la differenza fra una rete che spiega un difetto vecchio e una che ne
impedisce uno nuovo. Il conto della rete: **10 gruppi, 27 righe, 25 gia' rese**
— e tutte e 25 sono salve, perche' il progetto rende dal giapponese. Le due che
non lo erano sono queste.

### ⭐⭐ LA COPPIA CHE CAMBIA UNA PAROLA SOLA, E STAVOLTA E' L'INGLESE AD AVER RAGIONE

    :95484  (トネリコ, il frassino)  実を落とさない落葉樹。**非常に硬く**、…
    :95608  (ケヤキ, la zelkova)     実を落とさない落葉樹。**非常に良質で**、…

Il resto della frase e' identico. Qui l'inglese le distingue davvero («very
hard» / «very high quality»), quindi il rischio di appiattirle e' **nostro**:
le due rese sono identiche tranne quella parola — «È durissimo» contro «È di
ottima qualità» — esattamente come il giapponese.
ⓘ E' la 119a al rovescio, la stessa forma dei quattro diari del lotto 059.

### ⓘ Le decisioni minori, e da dove vengono

  - 常緑樹 «sempreverde» e 落葉樹 «albero che perde le foglie» sono gia' in
    gioco sull'**indice 3 di questi stessi oggetti**: la descrizione lunga usa
    la parola che il rapporto di identificazione usa gia';
  - 詠唱を妨害する -> «intralciare gli incantesimi», forma gia' in gioco sulla
    veste dei monaci (`:130714`, lotto 060 di ieri sera);
  - モミの木 «abete» e 飾り «addobbi» sono le stesse parole del lotto **061**
    (`:91026`, l'albero di Natale da commercio): sono lo stesso oggetto visto
    da due parti, ed e' la lezione della riga sorella fra lotti diversi
    applicata a mano;
  - 水薬 «pozione» e 魔術士ギルド «Gilda dei Maghi» dal dizionario;
    ノースティリス «Tyris del Nord», ノイエル «Noyel»;
  - `:68450`, il ciliegio del mondo dei morti, tiene tutt'e due le parole del
    gioco giapponese — 狂い咲き, il fiorire fuori stagione, e
    儚さを通り越して狂気, oltre la caducita' la follia;
  - ⓘ 映写機 (`:95672`) non e' nel dizionario da nessuna parte: e' il
    proiettore, e l'inglese dice «projector».

### ⚠️ Il preflight ha preso una resa, ed era un carattere

`Càpita` — accento **dentro** la parola, che `reimporta` rifiuta. Preso prima
del montaggio e riscritto «Succede spesso»: e' il punto 4 di
`_preflight034.py`, quello per cui tre lotti su otto della 115a erano stati
respinti.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :68450
    (68450, 'Mysterious cherry tree blooms and then falls forever in the world of the dead. The petals that fall to the ground disappear like a phantom. This phenomenon of the cycle of flowers is more maddening than transient. \\n# ~Special Edition: Pursuing Mythical Plants~'):
        "Un ciliegio misterioso che nel mondo dei morti fiorisce e sfiorisce, fiorisce e sfiorisce, per sempre. I petali che toccano terra svaniscono piano, come un'illusione. In quel fiorire fuori stagione si va oltre la caducità: quello che si sente è follia. \\n# ~Speciale: sulle Tracce delle Piante Leggendarie~",

    # ---------------------------------------------------------- :90894
    (90894, 'A fir tree with numerous decorations. The bright ornaments attached to the tree brightly illuminate its surroundings as if it were glowing with its own power. \\n# ~North Tyris Travels, Winter Edition~'):
        "Un abete a cui hanno attaccato addobbi a non finire. Gli ornamenti sgargianti illuminano tutt'intorno, come se l'albero splendesse di luce propria. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    # ---------------------------------------------------------- :91522
    (91522, 'Evergreen tree that does not produce any fruit. It is said that in the cold season, festivals are held in Noyel to celebrate the Saint by decorating these trees with various ornaments. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un sempreverde che non lascia cadere frutti. Pare che nella stagione fredda, a Noyel, questi alberi li carichino di addobbi d'ogni sorta e si faccia una festa per un certo santo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :91584
    (91584, 'Trees with all their leaves fallen off. They look very frigid, but this is their way of surviving the winter. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero a cui sono cadute tutte le foglie. Sembra infreddolito, ma è il suo modo di passare l'inverno. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95484
    (95484, 'Deciduous tree that does not produce fruit. It is very hard and is primarily used as wood to make various types of furniture. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che perde le foglie e non lascia cadere frutti. È durissimo, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95546
    (95546, 'Trees of tropical origin. It is said that its fruit is hard and looks like a huge cannonball, but these trees do not seem to bear fruit in North Tyris. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che viene dai paesi caldi. Dicono che il suo frutto sia duro e grosso come una palla di cannone, ma a Tyris del Nord questi alberi pare non ne portino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95608
    (95608, 'Deciduous trees that does not produce any fruit. It has very high quality and is mainly used as wood to make various types of furniture. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero che perde le foglie e non lascia cadere frutti. È di ottima qualità, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95670
    (95670, 'Completely dead old tree. It is highly flammable, so do not play with fire in the vicinity. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un albero vecchio, seccato del tutto. Prende fuoco con niente: meglio non giocare con le fiamme lì vicino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95672
    (95672, '\\"It makes you think a lot. Of course, this is just a rotting tree, but with a different perspective, it could be us or it could be a forest. I wonder who this projector will capture as time goes by.\\" \\n# ~words of <Barius> the blue haired~'):
        "\\\"Fa pensare a molte cose. Questo di sicuro è solo un legno marcito, ma basta cambiare sguardo e diventa noi, o quel bosco. Col tempo che passa, chissà quale delle due cose finirà per riprendere, questo proiettore.\\\" \\n# ~Parole di <Barius> dai capelli blu~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :95734
    (95734, "This is a tree that drops fruit when you bash it. Be careful not to get carried away and hit yourself too many times, because you won't be able to get unlimited fruits this way. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che, a dargli una spallata, lascia cadere i frutti. Ma se ci si prende gusto e si insiste, per un po' di frutti non se ne avranno più: occhio. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95796
    (95796, "A tree that hasn't been producing any fruit even after years of waiting. Forget about it and look for a tree that has borne fruit. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che, per quanto lo si aspetti, non ha nessuna intenzione di dare frutti. Meglio rassegnarsi e cercarne uno che i frutti li abbia. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95858
    (95858, 'Evergreen tree that does not produce any fruit. It is said that in the cold season, festivals are held in Noyel to celebrate the Saint by decorating these trees with various ornaments. \\n# ~Illustrated Guide to Tyris Horticulture~'):
        "Un sempreverde che non lascia cadere frutti. Succede spesso di credere che qualcuno stia intralciando i propri incantesimi e scoprire poi che era il polline di questo albero. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ---------------------------------------------------------- :95920
    (95920, "A deciduous tree that does not produce fruit. In recent years, it has been discovered that as it grows, it releases toxins from its roots and kills the surrounding trees. The Mages' Guild is currently researching the possibility of using it as a potion. \\n# ~Illustrated Guide to Tyris Horticulture~"):
        "Un albero che perde le foglie e non lascia cadere frutti. Di recente si è scoperto che, crescendo, dalle radici emette tossine che fanno seccare gli alberi intorno, e la Gilda dei Maghi sta studiando se se ne possa ricavare una pozione. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

# 12 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-062.jsonl'
RIGHE = {
    68450, 90894, 91522, 91584, 95484, 95546, 95608, 95670, 95672, 95734,
    95796, 95858, 95920,
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
