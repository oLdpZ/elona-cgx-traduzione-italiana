# -*- coding: utf-8 -*-
"""120a - Lotto 054 di `db_item.hsp`: LE ARMI A DISTANZA, e la categoria CHIUDE.

`FILTER_RANGE`, righe da `:96567` a `:127280`: **10 righe**, tutte dell'indice
0, su 10 oggetti. Con questo lotto `FILTER_RANGE` va a **0 da fare su 60
vive**, ed e' la **nona** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 054`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 054`: 0 su 10. `_code.py 054`: 0 righe senza
resa in tabella.

### ⭐⭐⭐ LE DIECI SONO LE ARMI BASE, E PORTANO UNA SCALA DI GIOCO

Non e' un lotto di pezzi unici come il 053: qui ci sono l'arco corto, l'arco
lungo, la balestra, la pistola, il fucile a pompa, la mitragliatrice, la
pistola laser e i sassi — cioe' le armi che ogni giocatore impugna nelle prime
ore, e le cui descrizioni si leggono piu' di ogni altra di questa categoria.

Sei di loro dicono, ciascuna a modo suo, **quanto la forza cali allontanandosi**.
E' un fatto di gioco, non un ornamento, e la scala e' gia' resa **nell'indice
3**, che e' chiuso da sessioni:

    光子銃    pistola laser     殆どない   -> «con la distanza non cala quasi»
    機関銃    mitragliatrice    少ない     -> «con la distanza cala poco»
    拳銃      pistola           減衰する   -> «con la distanza perde forza»
    散弾銃    fucile a pompa    射程が短い -> «porta poco lontano»

⚠️ Il pannello disegna il corpo e l'indice 3 **uno sotto l'altro**: usare qui
un verbo diverso — «diminuire», «scemare», «indebolirsi» — avrebbe spezzato in
due la stessa scala **nella stessa schermata**. Tutte le rese del corpo dicono
**calare**, che e' il verbo dell'indice 3.

⭐ E i due archi chiudono la scala dall'altro capo: 近～中距離 per l'arco corto,
中～遠距離 per il lungo. E' la stessa forma della scala delle navi della 119a —
un gradino per oggetto, che si vede solo mettendo le righe in fila — ma qui il
lavoro non e' stato ricostruirla: e' stato **non romperla**, perche' meta' era
gia' in gioco.

### ⓘ Due punti dove il giapponese sembra contraddirsi e non si contraddice

  - `:96567`, il rail gun: 超重量装置 «apparecchio di peso enorme» e tre righe
    dopo 軽量化に成功している «e' riuscito ad alleggerirsi». Non e' un errore:
    pesa un'enormita' di suo, e **nonostante questo** sono riusciti a
    scaricarne un po' lavorando materiali speciali. Il どちらも che segue sono
    le **due** tecniche — il meccanismo e la lavorazione — ed e' per questo
    che la resa deve dire «tutt'e due»;
  - `:98801`, la balestra: il dizionario rende 機械弓 «balestra», ma il
    giapponese di questa riga parla di 弓, **l'arco**, e ne descrive il
    compromesso (chiunque la usa, ma caricarla costa forza e tempo). La resa
    tiene l'arco, che e' cio' che la riga dice; il nome dell'oggetto resta
    «balestra» dove il nome si legge.

### ⓘ 森の民 e il nome che il giapponese abbrevia

`:117388`, l'arco di Vindale. Il giapponese dice 森の民, «la gente del bosco»;
il nome dell'oggetto e' 異形の森の弓, e 異形の森 il dizionario lo rende **«la
Foresta Eretica»** — l'inglese invece la chiama Vindale, e da li' viene il
nome reso `<Arco di Vindale>`. Le due forme convivono gia' nel gioco
(`_cerca.py` trova tutt'e due), e questa riga non e' il posto per sceglierne
una: la resa dice «la gente della foresta», che regge il legame senza
decidere.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :96567
    (96567, 'A super-heavyweight device that ejects a substance at high speed. In addition to the complex mechanism, it has succeeded in reducing weight by processing special materials. However, since both of these technologies are now lost, it would be impossible to mass produce them. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un apparecchio pesantissimo, che scaglia materia portata ad altissima velocità. Oltre al meccanismo complicato, lavorando materiali speciali si è riusciti anche ad alleggerirlo. Ma tutt'e due sono ormai tecniche perdute, e produrlo in serie sarebbe impossibile. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :96710
    (96710, 'Firearms that shoot a massive beam of light by loading a special bullet. Unlike other ranged weapons whose power diminishes as the distance increases, this is an excellent weapon whose power hardly diminishes at all. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco che, caricata con un proiettile speciale, scaglia dal foro di sparo un raggio di luce dotato di massa. A differenza delle altre armi da tiro, che perdono forza a mano a mano che la distanza cresce, questa non cala quasi per niente: un pezzo notevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :97803
    (97803, 'Firearms used to fire projectiles that scatter over a wide area. It is incomparably powerful at close range, but its power decreases at an accelerated rate as you move away from it, so it must be handled with care. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco fatta per sparare proiettili che si sparpagliano su un'area larga. Da vicino ha una forza senza pari, ma allontanandosi quella forza cala sempre più in fretta, e va maneggiata con attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :98801
    (98801, 'Bows are designed for easy firing of arrows. The advantage  is that it can be handled by anyone without the need for bow skill, but on the other hand, it takes a lot of strength and time to prepare for loading, so it has its advantages and disadvantages. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco pensato per scagliare frecce senza fatica. Il pregio è che lo usa chiunque, senza bisogno di pratica; il rovescio, che preparare la carica costa parecchia forza e parecchio tempo. Insomma, ha un pregio e un difetto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115796
    (115796, 'Firearms with a long barrel designed for continuous firing. Although its size and weight make it somewhat maneuverable, it is still much easier to operate than a bow. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'arma da fuoco a canna lunga, fatta per sparare di continuo. Per taglia e peso non è arma per tutti, ma anche così, a differenza dell'arco, si può dire che sia molto più facile da manovrare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :115872
    (115872, 'Short bow developed for hunting. Requires skill to handle, but once you get the hang of it, it will be a reliable friend to hunters. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco di lunghezza contenuta, messo a punto per la caccia. Usarlo richiede pratica, ma una volta presa la mano può diventare per i cacciatori un amico di cui fidarsi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117185
    (117185, 'A collection of roadside pebbles, hard as iron, used as weapons. They certainly do hurt when thrown, but since they are only pebbles, they are little more than a scare tactic. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un pugno di sassi duri come il ferro, raccolti sul ciglio della strada e messi insieme come arma. A prenderli in faccia fanno male davvero, ma sassi restano: poco più di uno spauracchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :117388
    (117388, 'Longbows are said to be filled with the wisdom of the Vindalian folk. It seems to have been devised in several ways to keep the prey from escaping. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un arco lungo che si dice racchiuda tutto il sapere della gente della foresta. Pare che ci sia dentro più di un accorgimento perché la preda presa di mira non scappi. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :127138
    (127138, "A heavy, compact firearm. It is designed to be handled by any person, but due to the short barrel, its range won't be very long. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Un'arma da fuoco piccola, che si sente pesante in mano. È progettata perché chiunque la sappia usare, ma con la canna corta che ha la gittata non sarà granché lunga. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :127280
    (127280, 'A bow longer than the body size, designed to extend the range of a bow. By angling the shot, it can snipe the enemy from a very long range.\\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un arco che, per allungare la gittata, è cresciuto fino a superare la statura di un uomo. Già così arriva abbastanza lontano, ma dandogli l'angolo giusto si dice che possa colpire il nemico da distanze lunghissime.\\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 10 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-054.jsonl'
RIGHE = {
    96567, 96710, 97803, 98801, 115796, 115872, 117185, 117388, 127138, 127280,
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
