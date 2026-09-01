# -*- coding: utf-8 -*-
"""122a - Lotto 063 di `db_item.hsp`: GLI ELMI E I CAPPELLI, e la categoria CHIUDE.

`FILTER_HELM`, righe da `:43044` a `:130909`: **16 righe** — 15 dell'indice 0 e
**una dell'indice 2** (`:66979`, il verso dell'alieno) — su 15 oggetti. Con
questo lotto `FILTER_HELM` va a **0 da fare su 16 vive**, ed e' la
**diciottesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 063`: **+16** per 16 rese,
nessuna gemella. ⓘ `_gia-reso.py 063`: 0 su 16. `_code.py 063`: 0 righe senza
resa in tabella. `_forma.py 063`: 16 su 16 con lo spazio prima del `\\n`.

### ⭐⭐⭐ DUE FAMIGLIE ATTRAVERSANO ALTRI LOTTI, E STAVOLTA SI SONO CERCATE

Il lotto 060 aveva trovato la riga sorella nel lotto di un'ora prima **per
fortuna**, perche' le rese erano ancora sotto gli occhi. Qui la fortuna non
c'era — i lotti 058 e 060 sono di ieri sera — e le due famiglie sono uscite
solo perche' `_cerca.py` e' stato lanciato **prima** di scrivere, sulla prima
frase di ogni riga.

**La famiglia dei materiali, terza occorrenza:**

    :100849 (058)  特殊な素材をかけ合わせてより強固な防護を得た盾。
    :101769 (060)  特殊な素材をかけ合わせてより強固な防護を得た鎧。
    :99872  (063)  特殊な素材をかけ合わせてより強固な防護を得た兜。   <- questa

Le tre aperture italiane sono la stessa frase, cambia il nome del pezzo: «Uno
scudo / Una corazza / Un elmo che, incrociando materiali speciali, ha ottenuto
una protezione più solida.»

**La famiglia del segreto, tre righe in DUE categorie diverse:**

`:43044` e `:43112` (le due parrucche) aprono e chiudono con le stesse due
frasi, e le stesse due frasi stanno gia' in gioco su un **terzo** oggetto —
l'oggetto d'infiltrazione, un'altra categoria, reso in una sessione passata.
Sono state **copiate dal dizionario**, non riscritte:

    «Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista
     del mondo.»
    «Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto
     da qualche artigiano.»

⚠️ **Nessuno strumento del lotto poteva dirlo**: `_gia-reso` cerca la prosa
intera e dice 0 su 16, `_120-serie-bacchette` raggruppa dentro il lotto,
`_coerenza` fa lo stesso, e `_122-inglese-doppio-item` guarda l'inglese, non il
giapponese. ⭐ **Lo strumento che manca resta quello**: la ricerca della riga
sorella per **frase** — non per prosa intera — su tutto `db_item.hsp`. E' la
richiesta della 121a, e questo lotto e' la seconda prova che serve.

### ⭐ Le due righe che il giapponese costruisce sulla ripetizione

  - `:66977`, la testa dell'alieno di Sunbararia, accumula **tre** esitazioni
    di fila e chiude con はず — たぶん完全に死んでいるので、おそらく被っても
    きっと大丈夫なはず. La battuta sta nel mucchio, non in una parola: la resa
    tiene «Probabilmente… quasi di sicuro… non dovrebbe… si spera»;
  - `:130909`, il cappello magico, dice 何となく賢くなった気分 — un vago senso
    di essere piu' saggi. Togliere quel «vago» toglierebbe la riga.

### ⓘ Le decisioni minori, e da dove vengono

  - スンバラリア星人 «l'alieno di Sunbararia», 吟遊詩人 «menestrello»,
    定命 «mortale», 変異 «mutazione», 防弾チョッキ «giubbotto antiproiettile»
    (quest'ultimo dal lotto 060): tutti dal dizionario;
  - 幸運の神 (`:76181`) e' **Ehekatl**, e in gioco il suo epiteto e' «Ehekatl
    della Sorte»: la riga dice «la dea della sorte», non «della fortuna»,
    perche' e' la parola che il giocatore ha gia' letto. Il genere femminile
    viene dal gioco, dove Ehekatl parla al femminile («Mi hai chiamata?»);
  - `:66979` e' un **verso**, non una frase: monte lo lascia identico in tutt'e
    tre le lingue. Solo il titolo-fonte si traduce, e viene da `_code.py`;
  - le descrizioni lunghe usano le parole dell'**indice 3 gia' in gioco** degli
    stessi oggetti — «Un'armatura per proteggere la testa», «Un elmo per i
    cavalieri», «Un elmo di un certo peso».

### ⚠️⚠️ `reimporta` HA RESPINTO IL LOTTO INTERO PER UN VERSO DI DICIOTTO LETTERE

`:66979` e' 「ＡＳＤＪＵＲＨＦＫ＞ＲＯＷＲＷ＜ＭＷ！」, il verso dell'alieno, e
monte lo scrive uguale in tutt'e tre le lingue. **Copiarlo com'era e' costato
16 rese su 16**: quei caratteri sono a **doppia larghezza**, CP932 li scrive su
due byte e la build ne disegna **uno per byte** — a schermo sarebbero uscite
lettere latine a caso, come il 「・」 diventato «E» in una sessione passata.

⭐ E' `reimporta` che l'ha preso, non il preflight: la sua regola dei caratteri
guarda quel che CP932 spezza, mentre il punto 4 del preflight guarda gli accenti
dentro la parola. Sono due reti diverse, e la seconda non copre la prima.
💡 Il verso e' stato riscritto **a larghezza singola, lettera per lettera**:
`ASDJURHFK>ROWRW<MW!`. Non e' una traduzione — e' la stessa cosa scritta con
caratteri che la build sa disegnare.
⚠️ E vale in generale: **una stringa che si copia da monte perche' «non si
traduce» va comunque guardata carattere per carattere.** L'idea che copiare sia
l'operazione sicura e' esattamente sbagliata qui.

### ⓘ Il preflight ha segnalato quattro parole lunghe, e non erano un difetto

`un'organizzazione` (17), `sorprendentemente` (17) e il verso dell'alieno (22).
La finestra di rinculo del preflight e' 15, ma il tetto vero e' il budget da 77
del corpo impaginato: nel dizionario ci sono gia' **19 rese** con una parola da
17 caratteri o piu', e il cancello di `_107-descrizioni-item` legge 0 parole
spezzate. Verificato prima di proseguire, non dato per scontato.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :43044
    (43044, "Once upon a time, an evil secret society developed this hairpiece as part of their world domination scheme. It can change into various hairstyles, and once dyed, it's nearly impossible to identify the wearer. Even more terrifying, it can be controlled with brainwaves and used like a whip or drill to mercilessly kill unsuspecting victims. Only a few have been unearthed and restored by skilled craftsmen to this day. \\n# ~Irva Fantasy Encyclopedia~"):
        "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura, e se poi viene pure tinta riconoscere chi la porta diventa quasi impossibile. Per giunta si comanda con le onde cerebrali, e ci sono casi di gente che l'ha adoperata come una frusta o un trapano per ammazzare uno dopo l'altro gli avversari distratti. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :43112
    (43112, "Once upon a time, an evil secret society developed this hairpiece as part of their world domination scheme. It can change into various hairstyles and was used for disguises, but cleverly, it could also double as a makeshift bulletproof helmet, concealing the fact that it was even being worn on one's head. Nowadays, only a few have been salvaged and painstakingly restored by skilled craftsmen. \\n# ~Irva Fantasy Encyclopedia~"):
        "Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista del mondo. È una parrucca che si trasforma in ogni acconciatura. La usavano per travestirsi, ma siccome protegge la testa senza lasciar vedere che la si porta, a volte serviva anche da giubbotto antiproiettile per il capo. Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto da qualche artigiano. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :65398
    (65398, 'Recovered from drifting in space. Analysis revealed that it was a helmet-shaped mechanical life form, but it was already unconscious when it was found. Part of its system has been successfully restored, and it is capable of simple gravity control and body function assistance. \\n# ~Irva Fantasy Encyclopedia~'):
        "L'hanno recuperato mentre andava alla deriva nello spazio. Dalle analisi è risultato una forma di vita meccanica a forma di casco, ma quando è stato trovato pare non avesse più coscienza di sé. Una parte dei suoi sistemi è stata rimessa in funzione, e riesce a controllare la gravità in modo elementare e ad assistere le funzioni del corpo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66977
    (66977, 'The head of a Sunbararian. Shaped like a nautilus, it is covered with a hard shell and is surprisingly protective. Since it is probably completely dead, it is surely safe to wear, probably. \\n# ~Irva Fantasy Encyclopedia~'):
        "La testa di un alieno di Sunbararia. Fatta come un nautilo, è coperta da un guscio duro e difende sorprendentemente bene. Probabilmente è morta del tutto, quindi a mettersela in testa quasi di sicuro non dovrebbe succedere niente, si spera. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66979
    (66979, '\\"ＡＳＤＪＵＲＨＦＫ＞ＲＯＷＲＷ＜ＭＷ！\\" \\n# ~words of a Sunbararian~'):
        "\\\"ASDJURHFK>ROWRW<MW!\\\" \\n# ~Parole di un alieno di Sunbararia~",

# 1 voci, 0 ambigue

    # ---------------------------------------------------------- :72418
    (72418, 'Special magical hats made of mana of wizards who were contacted by the abyss of magic. It is worn by wizards who have been resurrected as the undead, but there are rare wizards who create it while still alive. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un cappello magico speciale, fatto da un mago che in punto di morte ha sfiorato l'abisso della magia e ci ha messo dentro il mana che aveva da vivo. Lo portano i maghi tornati come non morti, ma qualche raro mago se lo fabbrica ancora da vivo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76181
    (76181, 'Favorite toy of the Goddess of Fortune. If you touch it, your luck will be sucked out of you. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il giocattolo preferito della dea della sorte. Se un mortale lo tocca male, la sorte gliela succhia via. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :80424
    (80424, 'Shiny black helmet characterized by its horns protruding forward. It is said that only one horn is unusually long because it mimics the characteristics of the creature from which it was devised. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un elmo di un nero lucido, che si riconosce dalle corna sporgenti in avanti. Dicono che una sola delle corna sia lunga in modo anomalo perché hanno copiato pari pari il tratto della creatura da cui l'hanno pensato. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :89077
    (89077, "Helmet made by a sage to attain a higher level. It is said that by wearing it, one can deepen one's knowledge and even see invisible beings. \\n# ~Irva Fantasy Encyclopedia~"):
        "Un elmo che un saggio si fabbricò per puntare più in alto. A portarlo la conoscenza si fa più profonda, e dicono che si arrivi a vedere perfino ciò che non si potrebbe vedere. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :99872
    (99872, 'Helmets that combine special materials to provide stronger protection. While many of these examples exist, there seem to be few examples that compensate for the inimitable weakness of weight. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Di pezzi che sfruttano i pregi di un materiale e ne coprono i difetti se ne vedono tanti, ma pare che pochi riescano a coprire il difetto senza pari che è il peso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99937
    (99937, 'Armor made to protect the head. It has a wider range of protection than a hat, but is naturally heavier. There are some funny stories about people getting stiff shoulders after using it for a long time. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura fatta per proteggere la testa. Copre più di un cappello, ma è chiaro che pesa anche di più. Girano perfino le storielle di chi, a portarlo per ore, si è ritrovato con le spalle indolenzite. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100002
    (100002, 'A prestigious helmet made for a knight. It is elaborately carved and decorated to suit the user, but it is not merely ceremonial and offers a certain degree of protection. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo di gran classe, fatto per i cavalieri. Porta cesellature e ornamenti studiati su misura di chi lo indossa, ma non è roba da sola cerimonia: una certa protezione la dà davvero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100067
    (100067, 'A helmet built thicker than normal helmets. The defensive power is certainly improved, but the weight is sacrificed, so care must be taken when wearing it. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un elmo fatto più spesso del normale. La difesa sale di sicuro, ma in cambio ci si rimette in peso, e a indossarlo conviene starci attenti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100132
    (100132, 'A fashionable hat with bird feathers. It is often worn by bards because they liken their singing voice to that of birds. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello elegante, ornato di penne d'uccello. Lo portano spesso i menestrelli, e pare sia perché paragonano la propria voce a quella degli uccelli. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130844
    (130844, 'A very light hat worn by fairies. Perhaps because they consider themselves fragile, these hats have the ability to protect them from the mutations of the outside world. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello leggerissimo che dicono portino le fate. Forse perché si ritengono creature fragili, quel cappello ha la facoltà di proteggere dalle mutazioni che vengono da fuori. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :130909
    (130909, 'A tall pointed cone hat that a mage would wear. There is no special effect of this shape, but wearing it makes you feel somewhat smarter. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un cappello a punta come quelli che uno si aspetta addosso a un mago. Effetti non ne dà nessuno, ma a metterlo in testa un vago senso di essere diventati più saggi lo mette. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 15 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-063.jsonl'
RIGHE = {
    43044, 43112, 65398, 66977, 66979, 72418, 76181, 80424, 89077, 99872,
    99937, 100002, 100067, 100132, 130844, 130909,
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
