# -*- coding: utf-8 -*-
"""122a - Lotto 067 di `db_item.hsp`: I MANTELLI E LE ALI, e la categoria CHIUDE.

`FILTER_CLOAK`, righe da `:59062` a `:126777`: **10 righe**, tutte dell'indice
0, su 10 oggetti. Con questo lotto `FILTER_CLOAK` va a **0 da fare su 10 vive**,
ed e' la **ventiduesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 067`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 067`: 0 su 10. `_code.py 067`: 0 righe senza
resa in tabella. `_forma.py 067`: 10 su 10 con lo spazio prima del `\\n`.

### ⭐⭐ DUE COPPIE DENTRO IL LOTTO, E NESSUNO DEGLI STRUMENTI VECCHI LE VEDE

`_122-sorelle-per-frase` trova **sei frasi** con una sorella, e stavolta tutte
le sorelle stanno **dentro questo lotto**:

    :94022 (羽, il pipistrello)   —  DUE frasi su tre identiche parola per
    :96124 (翼, l'uccello)        —  parola. Cambia solo l'animale.

    :100197 (外套, il mantello)       —  la seconda frase identica:
    :126777 (軽外套, quello leggero)  —  幾多の素材を織り込むことで…

⚠️ **Che le sorelle siano dentro il lotto non toglie niente alla rete**, ed e' il
punto: `_gia-reso` conta 0 su 10, `_coerenza` non le accosta e
`_120-serie-bacchette` nemmeno, perche' guardano la **prosa intera** e queste
prose differiscono. La coppia del pipistrello e dell'uccello e' esattamente la
forma dei quattro diari del lotto 059 — righe che devono restare uguali — e
senza la rete si sarebbe vista solo rileggendo il dossier con attenzione.

ⓘ E gli indici 3 di `:94022` e `:96124` sono **gia' identici in gioco** («Un
ornamento di piume da mettere sulla schiena»): il giocatore vede la coppia
comunque, e due corpi divergenti sarebbero saltati all'occhio.

### ⚠️ IL VENTO CHE NON SI CHIAMA COME NELL'INDICE 3, E VA BENE COSI'

`:93692`, il mantello di Vindale. Il suo **indice 3**, gia' in gioco, dice «Un
mantello che protegge dal vento di etere» — ed e' una delle **due** voci che la
121a aveva segnalato come divergenti dalla forma del progetto, «vento d'etere»,
usata in venticinque.

Il corpo pero' non dice エーテル: dice 忌むべき風, il **vento maledetto**, e
異形の森, la Foresta Eretica. Reso alla lettera, quindi nel pannello le due
righe non si contraddicono e la divergenza di monte non viene amplificata.
⚠️ **La voce divergente resta li'** e non e' stata toccata: e' una riga
dell'indice 3, che e' chiuso, e cambiarla di straforo dentro un lotto del corpo
sarebbe il genere di modifica che nessun conteggio segnala. Va decisa a parte.

### ⓘ Le decisioni minori, e da dove vengono

  - 絶器 -> **«zekki»**, che non si traduce: sta gia' in gioco sull'indice 3
    dei guanti del lotto 066 («Dei guanti d'arme detti zekki»);
  - 異形の森 -> «la Foresta Eretica» (dizionario, due battute);
    コウモリ «pipistrello»; マニピュレーター «manipolatori»;
    イェルス軍 «l'esercito di Yerles» e 火炎竜 «drago di fuoco», come nei
    lotti 061, 066 e 067;
  - 変異 -> «mutazione», come il cappello da fata del lotto 063;
  - `:59062` e' un'**invocazione**, non una descrizione: le ultime due frasi
    giapponesi non hanno verbo finito, e la resa tiene quel ritmo spezzato
    invece di rimetterlo in prosa;
  - `:77354` gioca su 悪い意味でサマになる — gli sta bene, ma nel senso
    sbagliato — e su 渋い, che e' l'eleganza asciutta di chi ha vissuto, non la
    tristezza. La battuta sta tutta li' e va tenuta intera.

### ⓘ Il preflight ha segnalato due `equipaggiamento` (15), e non e' un difetto

Vale la misura del lotto 063: il tetto vero e' il budget da 77 del corpo
impaginato, e il cancello di `_107-descrizioni-item` legge 0 parole spezzate.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :59062
    (59062, 'Exquisite weapons said to have been created by a goddess from another world. It is a sword of light and protection. These golden wings are said to transcend the world, descend from the sky, and repel darkness. \\n# ~Irva Fantasy Encyclopedia~'):
        "Uno zekki che dicono creato da una dea di un altro mondo. È la spada dello splendore e della custodia. Ali d'oro che, dicono, scendono dal cielo attraversando i mondi e spazzano via le tenebre. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :63652
    (63652, 'Originally a prosthetic hand designed for combat, it has been developed into an easily replaceable piece of equipment. Electrical signals are read from the clothing without any neural connection, so depending on the situation, it may not work as desired. The manipulators are made to be sturdy, and by changing the gear ratio, powerful attacks can be unleashed. \\n# ~Irva Fantasy Encyclopedia~'):
        "Nasceva come protesi da combattimento, e da lì è stato sviluppato in un equipaggiamento che si cambia con facilità. Siccome legge i segnali elettrici da sopra i vestiti, senza collegarsi ai nervi, a seconda dei casi può non muoversi come si vorrebbe. I manipolatori sono costruiti robusti, e cambiando il rapporto degli ingranaggi si arriva a sferrare colpi violentissimi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76587
    (76587, 'Flight and propulsion unit developed by the Yerles military based on the wings of a flaming dragon. It is sturdy and can be used for defense. It was developed as personal equipment for soldiers, but lost in a competition to a leg-mounted flying unit and was not adopted. However, its flight capability was so strong that it was later used as a component in air combat weapons. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un'unità di volo e propulsione che l'esercito di Yerles ha sviluppato partendo dalle ali di un drago di fuoco. È robusta, e a difendersi non è che non serva. La svilupparono come equipaggiamento personale del soldato, ma in gara perse contro un'unità di volo da montare sulle gambe e non fu adottata. La capacità di volo però era solida, e più tardi l'hanno riutilizzata come pezzo per le armi da combattimento aereo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :77354
    (77354, 'A cloak worn by heroes in the past. Because it is tattered and shabby, it looks bad when worn by someone who seems to be less fortunate. A person who is austere may be able to wear it, though. \\n# ~Irva Fantasy Encyclopedia~'):
        "Il mantello che portava un eroe di un tempo. È tutto strappato e sformato, e addosso a chi ha già l'aria sfortunata sta bene nel senso peggiore. Uno con un certo stile asciutto, magari, riuscirebbe a portarlo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :93692
    (93692, 'This cloak is designed to protect against the abominable winds that arise from the Vindale Forest. It is designed to prevent etherwind-induced mutation, so it will not be able to withstand everyday mutation or rain and wind. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un mantello che, dicono, para il vento maledetto che si leva dalla Foresta Eretica. Serve unicamente a fermare le mutazioni portate da quel vento, e contro le mutazioni di tutti i giorni, o contro la pioggia e il vento, non riparerà. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :94022
    (94022, 'Ornaments that resemble the wings of a bat. It can prevent attacks on the back, but it is made only to decorate the appearance of the wearer. It allows floating in the air, albeit only slightly. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto da indossare, fatto a somiglianza delle ali di un pipistrello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :96124
    (96124, 'Ornaments that resemble the wings of a bird. It can prevent attacks on the back, but it is made only to decorate the appearance of the wearer. It allows floating in the air, albeit only slightly. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto da indossare, fatto a somiglianza delle ali di un uccello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100197
    (100197, 'A loose-fitting fabric that wraps around the body. The strength of the cloth itself is increased by weaving in a number of materials. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un tessuto ampio da avvolgersi attorno al corpo. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100262
    (100262, 'A cloak of hard metal attached to the back of a cloth made of interwoven materials. Wearing this cloak can protect the wearer from some attacks. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un mantello con del metallo duro applicato dietro a una stoffa in cui sono intrecciati dei materiali. Addosso, para una parte dei colpi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :126777
    (126777, 'A thin cloth fabric worn over armor. The strength of the cloth itself is increased by weaving in a number of materials. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un tessuto sottile da buttarsi sulle spalle sopra l'armatura. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-067.jsonl'
RIGHE = {
    59062, 63652, 76587, 77354, 93692, 94022, 96124, 100197, 100262, 126777,
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
