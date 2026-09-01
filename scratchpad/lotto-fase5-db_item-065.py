# -*- coding: utf-8 -*-
"""122a - Lotto 065 di `db_item.hsp`: GLI ANELLI, e la categoria CHIUDE.

`FILTER_ACCESSORY_RING`, righe da `:56737` a `:130385`: **11 righe**, tutte
dell'indice 0, su 11 oggetti. Con questo lotto `FILTER_ACCESSORY_RING` va a
**0 da fare su 11 vive**, ed e' la **ventesima** categoria del corpo che si
chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 065`: **+11** per 11 rese,
nessuna gemella. ⓘ `_gia-reso.py 065`: 0 su 11. `_code.py 065`: 0 righe senza
resa in tabella. `_forma.py 065`: 11 su 11 con lo spazio prima del `\\n`.

### ⭐⭐⭐ LA RIGA SORELLA STAVA NEL LOTTO DI VENTI MINUTI FA. DI NUOVO.

    :99448 (064)  婚礼の儀において、伴侶となる者へ送られる愛のこめられた**首輪**。
                  当然ながらこの**首輪**は伴侶の所有物となるので、無理やり…
    :99162 (065)  婚礼の儀において、伴侶となる者へ送られる愛のこめられた**指輪**。
                  当然ながらこの**指輪**は伴侶の所有物となるので、無理やり…

Identiche in giapponese tranne **una parola**, e le rese lo sono in italiano.

⚠️ **E' la terza volta in questa sessione**, dopo le due famiglie del lotto 063,
e la seconda volta in due sessioni che la sorella sta in un lotto **chiuso
poche ore prima**. `_gia-reso.py` dice 0 su 11 e ha ragione — cerca la prosa
intera, e le due stringhe differiscono di un carattere.
⭐ Stavolta non e' stata la fortuna: il dossier del 064 era ancora aperto e la
frase e' stata riconosciuta a occhio. **Su una sessione che riprendesse domani
non lo sarebbe.** Lo strumento che manca resta quello: la riga sorella **per
frase** su tutto `db_item.hsp`, non per prosa intera e non dentro il lotto.
ⓘ Il conto di questa sessione: tre famiglie trovate a mano, zero trovate da uno
strumento.

### ⭐ TRE ESPRESSIONI CHE TORNANO DA LOTTI PRECEDENTI, CERCATE PRIMA DI SCRIVERE

  - より高みを目指した (`:99377`) e' la stessa di `:89077`, l'elmo del saggio
    del lotto 063: «puntare più in alto», stessa resa;
  - 武骨 (`:107390`) e' la stessa parola di `:99663`, la gorgiera del lotto
    064: «rozzo»;
  - 〜のこめられた (`:86671`) -> «racchiuso», come i due indici 3 delle collane
    e le rese del 064.

### ⓘ Le decisioni minori, e da dove vengono

  - 元素の神 «il dio degli elementi», gia' in gioco sul busto che lo raffigura;
    鋼鉄竜 «drago d'acciaio», che e' anche il nome italiano dell'oggetto e il
    nome di <Corgon> in gioco; 螺旋 «spirale»;
  - 気品 (`:107181`) -> **«eleganza»**, la parola che il gioco usa gia' nel
    tratto «Eleganza [clientela migliore]». ⚠️ L'indice 3 dello stesso oggetto
    parla invece di 運勢, la **fortuna**: sono due cose diverse nello stesso
    pannello e restano due parole diverse. Appiattirle sarebbe un errore che
    nessuna rete vedrebbe;
  - `:86671` dice 老化するという弊害はない, e non e' una figura retorica: nel
    gioco l'accelerazione fa invecchiare, e la riga sta dicendo che questo
    anello no. E' un fatto di gioco e va detto chiaro;
  - `:99233` riprende le parole del suo indice 3 gia' in gioco, «Un cerchio da
    infilare al dito».

### ⓘ Il preflight ha segnalato una parola lunga, e non e' un difetto

`controindicazione` (17 caratteri). Vale quel che si e' misurato nel lotto 063:
il tetto vero e' il budget da 77 del corpo impaginato, nel dizionario ci sono
gia' 19 rese con parole da 17 caratteri o piu', e il cancello di
`_107-descrizioni-item` legge 0 parole spezzate.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :56737
    (56737, 'The ring possesses two different elemental powers. It also assists the regenerative capabilities. The red and blue lines intertwine like a spiral. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello in cui abitano due forze diverse. Ha anche il compito di dare una mano alla capacità di rigenerarsi. Nel disegno, una linea rossa e una azzurra si intrecciano come una spirale. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :75581
    (75581, 'Ring that seals magic power, created by the God of Elements. It suppresses immense amounts of magical power. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello che sigilla il potere magico, nato dal dio degli elementi. Tiene a bada anche un potere magico immenso. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :86671
    (86671, 'This ring is filled with magical power that constantly accelerates a person. Since it has no harmful effects of aging, many adventurers seem to love using it. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello in cui è racchiuso un potere magico che tiene una persona sempre accelerata. Non ha la controindicazione di far invecchiare, e pare che molti avventurieri se ne servano volentieri. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :93627
    (93627, 'The ring senses the surrounding seasonal weather and is effective in bad weather. In doing so, the ring emits a soft light and creates a force field that maintains tranquility in the surrounding area. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello che sente il clima intorno e fa effetto quando il tempo si guasta. In quel momento, dicono, manda una luce morbida e crea attorno a sé un campo di forza che tiene la calma. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :99162
    (99162, 'Rings of love are given to the spouse at the wedding ceremony. Naturally, the ring belongs to the spouse, and forcibly taking it away from him or her will provoke his or her fury. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello carico d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento l'anello appartiene a lui, e a strapparglielo per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99233
    (99233, 'Rings of ornaments worn on the fingers. There are a variety of types, including simple ones used for ceremonial purposes and ones in which significant magical power is enclosed. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un oggetto a forma di cerchio che si infila al dito. Ce n'è di ogni specie: dai più semplici, buoni per le cerimonie, a quelli in cui è sigillato un potere magico grave. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99305
    (99305, 'This ring is more specialized in protecting the finger. Although less valuable as an ornament, this is a better choice when protecting oneself. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello fatto apposta per proteggere meglio il dito. Come ornamento vale poco, ma quando si tratta di difendersi è questo che conviene. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :99377
    (99377, 'Rings made by mixing a variety of materials to achieve a higher level of performance. Many of them are more expensive than ordinary rings because of their durability and novelty. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello che punta più in alto mescolando materiali di ogni sorta. Siccome dura molto se ne vedono parecchi nati da tentativi arditi, e pare che costino un po' più dei soliti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :107181
    (107181, "Lovely small ring with a blue-green gemstone. It is said to enhance the owner's nobility through its hidden power. \\n# ~Lumiest Art Catalogue~"):
        "Un anello piccolo e grazioso, che porta una gemma verde-azzurra. Dicono che, con una forza nascosta, alzi l'eleganza di chi lo possiede. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :107390
    (107390, 'Ring said to have been made from the bones of a steel dragon. It is said to be so powerful that the wearer is made to believe he or she has become a steel dragon. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un anello rozzo, che dicono ricavato dalle ossa di un drago d'acciaio. A portarlo si acquista una forza tanto immensa da far credere di essere diventati un drago d'acciaio. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :130385
    (130385, 'Beautiful ring with a variety of decorations. It is said that once there was a competition among craftsmen to see how much color they could put onto this small ring. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un anello reso bellissimo da ornamenti d'ogni sorta. Dicono che un tempo gli artigiani si sfidassero a chi riuscisse a stipare più colore dentro quel piccolo cerchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 11 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-065.jsonl'
RIGHE = {
    56737, 75581, 86671, 93627, 99162, 99233, 99305, 99377, 107181, 107390,
    130385,
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
