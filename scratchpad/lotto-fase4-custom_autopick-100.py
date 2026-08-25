# -*- coding: utf-8 -*-
"""`custom_autopick.hsp` — le 86 voci vive, e sono quasi tutte CHIAVI.

⚠️⚠️ **Questo file non e' come i suoi dieci fratelli senza dizionario.** 78
delle sue 90 `lang()` non sono etichette da leggere: sono le **chiavi** con cui
il giocatore scrive le sue regole in `autopick.txt`, e `custom_autopick.hsp:358`
le confronta col **nome dell'oggetto**, che nella nostra build e' italiano. Il
guasto peggiore sta a meta' strada — file italiano e modello inglese — e per
questo il lotto va **nello stesso giro** della traduzione di
`data\\autopick.txt`. Per esteso in `decisioni.md` §98a.

⚠️ **Le chiavi si confrontano per SOTTOSTRINGA**, non per parola, e la catena
dei tipi non toglie quel che ha agganciato: se una chiave e' contenuta in
un'altra, il controllo di quella corta scatta sulla regola che nomina la lunga e
il suo `continue` butta via l'oggetto. In inglese questo succede **davvero due
volte** — `book` dentro `spellbook`, `food` dentro `traveler's food` — e in
giapponese mai. La rete e' `scratchpad/_100-selettori-ombra.py`, provata al
contrario su `--en` (deve accendersi due volte) e su `--jp` (deve tacere).
L'italiano ne vuole **zero**.

⚠️ **E le chiavi non hanno accenti, apposta.** `autopick.txt` e' l'unico file di
`data\\` scritto in **UTF-8** e non in CP932: una chiave accentata dovrebbe
esistere in due codifiche diverse — degradata nell'eseguibile, non degradata nel
modello — e le due non si aggancerebbero mai. Nessuna chiave porta un accento, e
la rete della sottostringa non basterebbe a dirlo.

Le tre scelte di resa che pesano:

1. **Le chiavi sono INVARIABILI dove l'italiano lo permette**, perche' il
   giocatore le scrive a mano e l'accordo di genere non c'e' chi lo faccia:
   `blessed`/`cursed`/`doomed` diventano « con benedizione », « con maledizione »
   e « con dannazione », che e' la deroga gia' decisa in `glossario.md` per
   `strblessed`/`strcursed`/`strdoomed` — e sono le stesse parole che compaiono
   **nel nome dell'oggetto**, cioe' proprio la stringa contro cui `:358`
   confronta. Le sei qualita' finiscono in `-e` da sole.
2. ⭐ **`good` non e' «buono»: e' « comune ».** La chiave inglese nomina
   `FIX_QUALITY_GOOD`, che e' l'indice **2** di `_quality` — e `text.hsp:106`
   quell'indice lo stampa a schermo come `common`, da noi «comune». Vale la
   regola del progetto: si dice quel che c'e' scritto sullo schermo, non quel
   che dice l'inglese di un'altra riga.
3. **`food` diventa « commestibile » e non « cibo », per non fare ombra a
   `traveler's food` = « cibo da viaggio »**, che e' il nome che l'oggetto ha
   davvero (`chat.hsp:13959`). E' la coppia su cui l'inglese si rompe: qui la
   parola generica si sposta, e quella specifica tiene il nome di schermo.

Quattro voci sono **rinviate perche' morte**: `:200`-`:217` sono due selettori
spenti con `//`, e il `//` e' la quinta famiglia di riga morta del progetto —
trovata in questa sessione, e la rete 6 di questo modello e' la prima che la
vede.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ------------------------------------------------------------ i messaggi
    # :61 il modello non c'e' e il gioco propone di crearlo. Il nome del file
    # nel salvataggio resta `autopick.txt`: la toppa cambia solo quello di
    # `data\`, che e' il modello da cui si copia.
    (61, "There's no autopick.txt for this save. Create one?"):
        "Per questo salvataggio non c'è un autopick.txt. Crearlo?",
    # :76 «raccolta automatica» e' il nome che la voce ha a schermo
    # (`action.hsp:1067`, `main.hsp:3343`, `screen.hsp:1004`).
    (76, 'Which autopickup file do you want to load?'):
        'Quale file di raccolta automatica vuoi caricare?',
    (90, 'Reloaded autopick.txt.'):
        'autopick.txt ricaricato.',
    (93, 'Reloaded autopick_.txt.'):
        '"autopick_" + rtval + ".txt ricaricato."',

    # ------------------------------------------------- i modificatori (:150-:353)
    # ⚠️ La chiave porta gli spazi attorno e vanno tenuti: `:149` fa
    # `s = " " + s + " "` apposta, perche' senza di quelli `instr` aggancerebbe
    # la parola in mezzo a un'altra.
    (150, ' all '): ' ogni ',
    (152, ' all '): ' ogni ',
    (153, ' all '): ' ogni ',
    # i tre gradini dell'identificazione: invariabili, e paralleli fra loro
    (155, ' unknown '): ' senza nome ',
    (159, ' unknown '): ' senza nome ',
    (162, ' name identified '): ' con nome noto ',
    (166, ' name identified '): ' con nome noto ',
    (169, ' quality identified '): ' con pregio noto ',
    (173, ' quality identified '): ' con pregio noto ',
    (176, ' fully identified '): ' del tutto noto ',
    (180, ' fully identified '): ' del tutto noto ',
    # ⚠️ « senza valore » e' la coda che `db_item.hsp:149970` da' gia' al
    # lingotto falso: «lingotto d'oro falso e senza valore».
    (183, ' worthless '): ' senza valore ',
    (187, ' worthless '): ' senza valore ',
    # `rotten` vale solo sul cibo (`:191` chiede FILTER_ITEM_FOOD), e «marcio» e'
    # la parola che il gioco usa gia' (`command.hsp:2230`, «cibo marcio»).
    (190, ' rotten '): ' marcio ',
    (197, ' rotten '): ' marcio ',
    # `empty` vale sui contenitori (`:221` chiede FILTER_CONTAINER)
    (220, ' empty '): ' vuoto ',
    (227, ' empty '): ' vuoto ',
    # ⭐ le sei qualita' vengono da `_quality` (`text.hsp:106`), che e' la scala
    # che il giocatore legge nel pannello — e finiscono tutte in `-e`, cioe'
    # non si accordano. ⚠️ `good` e' l'indice 2, che a schermo dice `common`.
    (230, ' bad '): ' scadente ',
    (237, ' bad '): ' scadente ',
    (240, ' good '): ' comune ',
    (247, ' good '): ' comune ',
    (250, ' great '): ' eccellente ',
    (257, ' great '): ' eccellente ',
    (260, ' miracle '): ' eccezionale ',
    (267, ' miracle '): ' eccezionale ',
    (270, ' godly '): ' celestiale ',
    (277, ' godly '): ' celestiale ',
    (280, ' special '): ' speciale ',
    (287, ' special '): ' speciale ',
    # `precious` non e' un gradino della scala: e' ITEM_BIT_PRECIOUS
    (290, ' precious '): ' prezioso ',
    (297, ' precious '): ' prezioso ',
    # ⭐ i quattro stati sono la deroga gia' decisa in `glossario.md` per
    # `strblessed`/`strcursed`/`strdoomed`: complemento invariabile, e le stesse
    # parole che stanno **dentro il nome dell'oggetto** contro cui `:358`
    # confronta quel che resta della regola.
    (300, ' blessed '): ' con benedizione ',
    (307, ' blessed '): ' con benedizione ',
    (310, ' uncursed '): ' senza maledizione ',
    (317, ' uncursed '): ' senza maledizione ',
    (320, ' cursed '): ' con maledizione ',
    (327, ' cursed '): ' con maledizione ',
    (330, ' doomed '): ' con dannazione ',
    (337, ' doomed '): ' con dannazione ',
    (340, ' alive '): ' in vita ',
    (344, ' alive '): ' in vita ',
    # «oggetto evolutivo» sta in `glossario.md`, ma qui la chiave e' un
    # complemento per non accordarsi col genere di quel che segue.
    (347, ' evolution '): ' di evoluzione ',
    (351, ' evolution '): ' di evoluzione ',

    # ------------------------------------------------------- i tipi (:366-:555)
    # ⚠️ Chiavi **nude**, senza spazi, e nessuna si toglie da `s` quando
    # aggancia: bastano due chiavi di cui una e' dentro l'altra per rompere
    # tutt'e due. Le parole vengono dai nomi che gli oggetti hanno gia'.
    (366, 'item'): 'oggetto',
    (369, 'equipment'): 'equipaggiamento',
    # «Mischia» e «Tiro» sono i nomi delle due caselle a schermo
    # (`command.hsp:10517`, `:15309`).
    (375, 'melee weapon'): 'arma da mischia',
    (381, 'helm'): 'elmo',
    (387, 'shield'): 'scudo',
    (393, 'armor'): 'armatura',
    (399, 'boot'): 'stivali',
    (405, 'belt'): 'cintura',
    (411, 'cloak'): 'mantello',
    (417, 'glove'): 'guanti',
    (423, 'ranged weapon'): 'arma da tiro',
    (429, 'ammo'): 'dardi',
    (435, 'ring'): 'anello',
    (441, 'necklace'): 'collana',
    (447, 'potion'): 'pozione',
    (453, 'scroll'): 'pergamena',
    # ⭐ «grimorio» e «libro» non si fanno ombra, dove `spellbook` e `book` se
    # la fanno: la coppia inglese e' rotta e la nostra no, senza fare niente.
    (459, 'spellbook'): 'grimorio',
    (465, 'book'): 'libro',
    (471, 'rod'): 'bacchetta',
    # ⚠️ « commestibile » e non « cibo »: vedi il docstring, e `:549`.
    (477, 'food'): 'commestibile',
    (483, 'tool'): 'attrezzo',
    (489, 'furniture'): 'mobilio',
    (495, 'well'): 'pozzo',
    (501, 'altar'): 'altare',
    (507, 'remains'): 'resti',
    (513, 'junk'): 'cianfrusaglie',
    (519, 'gold piece'): "moneta d'oro",
    (525, 'platinum coin'): 'moneta di platino',
    (531, 'chest'): 'baule',
    (537, 'ore'): 'minerale',
    (543, 'tree'): 'albero',
    (549, "traveler's food"): 'cibo da viaggio',
    (555, 'cargo'): 'merce da commercio',

    # --------------------------------------------- le domande e i due avvisi
    # ⚠️ Il compagno fa da SOGGETTO e non da complemento: «far distruggere X a
    # Y» metterebbe la preposizione davanti a un nome proprio, e « a Erystia »
    # vuole «ad» mentre « a Kuroya » no — la rete 8 lo boccia, e ha ragione.
    (567, 'Destroy ?'):
        '"Distruggere " + itemname(cnt2) + "?"',
    (579, 'Let  destroy ?'):
        'name(cnt3) + " distrugge " + itemname(cnt2) + "?"',
    # ⚠️ Chi ha distrutto l'inglese lo butta via, e la rete 11 pretende le
    # **stesse funzioni di contenuto** dell'inglese: qui `name(cnt3)` non ci
    # puo' entrare, per quanto il giapponese ce l'abbia.
    # ⭐ «non esiste più» invece di «è stato distrutto» perche' il participio si
    # accorderebbe col genere dell'oggetto: e' la resa gemella che
    # `chara_func.hsp:1294` da' gia' allo stesso inglese («March was destroyed»).
    # Lo spazio in coda e' dell'inglese e si tiene.
    (596, ' was destroyed. '):
        'itemname(cnt2) + " non esiste più. "',
    (608, 'Pick up ?'):
        '"Raccogliere " + itemname(cnt2) + "?"',
    # ⭐ gemella di `action.hsp:946`, che rende « pick up » con lo stesso
    # impianto: `name(cc) + " raccoglie " + itemname(...)`.
    (620, 'Let  pick up ?'):
        'name(cnt3) + " raccoglie " + itemname(cnt2) + "?"',
    # ⭐ gemella di `command.hsp:15853`, che ha lo stesso inglese: la resa e'
    # gia' approvata, e «[Non posare]» e' il nome della linguetta.
    (644, 'You set  as no-drop.'):
        '"Non poserai più " + itemname(cnt2) + "."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {
    # I due selettori spenti con `//` a `:200`-`:217`: ` zombie ` (腐りきった) e
    # ` dragon's ` (ドラゴンの). Sono codice che il compilatore non vede, e sono
    # il caso che ha fatto scoprire la quinta famiglia di riga morta.
    (200, ' zombie '),
    (207, ' zombie '),
    (210, " dragon's "),
    (217, " dragon's "),
}

USCITA = 'lavoro/fase4-custom_autopick-100.jsonl'
DA, A = 0, 999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\custom_autopick.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_custom_autopick.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

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
