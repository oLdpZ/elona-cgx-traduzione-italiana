# -*- coding: utf-8 -*-
"""Il raccolto, le piastrelle, il valore della casa, e chi sta dove.

`map_user.hsp:604`-`:985`, trentaquattro voci: quel che succede **dopo** aver
scelto una voce del menu del lotto 001. Tre gruppi — l'editor delle piastrelle
e il raccolto, la finestra del valore della casa, e lo spostamento di compagni,
ospiti e bestiame.

## ⚠️⚠️ `:730` — l'inglese ha la riga giusta dell'evento sbagliato, ed e' RINVIATA

    :718  txt lang(mdatan(MDATAN_NAME) + "を何と呼ぶ？ ",
                   "What do you want to call " + mdatan(MDATAN_NAME) + "? ")
    :729  mdatan(MDATAN_NAME) = "" + inputlog
    :730  txt lang("" + mdatan(MDATAN_NAME) + "という名前で呼ぶことにした。",
                   "You named " + him(tc) + " " + cdatan(CDATAN_NAME, tc) + ".")

La riga sopra chiede il nome della **proprieta'**, la riga in mezzo lo scrive in
`mdatan(MDATAN_NAME)`, e la conferma inglese nomina un **personaggio** con
`cdatan(CDATAN_NAME, tc)`. E' la riga della finestra che da' il nome a un
compagno, copiata qui: a schermo, in inglese, esce il nome di chi capita in `tc`.
E' la famiglia della 58a (`main.hsp:5684`), e la prova sta nelle due righe
intorno, non nella lingua.

⚠️ **Non e' toppabile dal dizionario**: la rete 11 pretende che le funzioni di
contenuto della resa siano quelle dell'inglese, e l'inglese ha `cdatan`, non
`mdatan`. Scrivere `mdatan` sarebbe **aggiungere** una funzione che l'inglese
non ha, che e' proprio quel che la rete esiste per impedire; scrivere `cdatan`
sarebbe copiare il difetto. Si fa come `action.hsp:9631`: **rinvio piu' toppa**.

## ⚠️ La finestra del valore della casa ha una geometria stretta

`:762` disegna quattro etichette e poi le stelle:

    map_user.hsp:766   font ..., 12 + sizefix - en * 2      il carattere e' 10
    map_user.hsp:769   pos x, y                             l'etichetta
    map_user.hsp:773   pos x + 35 + cnt * 13 + en * 8       la prima stella

cioe' **43 px** fra l'inizio dell'etichetta e la prima stella (il `cnt` del `pos`
delle stelle e' quello del ciclo **interno**, non delle etichette: le stelle
stanno in fila a 13 px l'una dall'altra). Con un carattere da 10 px ci stanno
sei o sette lettere: «Base», «Arredi», «Cimeli», «Totale» ne usano al massimo
sei. ⚠️ Il passo di quel carattere **non e' misurato** — le reti conoscono il 13
di `*prompt_key` e il 12 della pergamena — e sei lettere sono una stima prudente,
non un tetto provato. Va guardato a schermo.

## Quel che si e' copiato invece di scriverlo

    :672  stesso giapponese di main.hsp:8475, la domanda che questa voce apre
    :687  stesso giapponese di main.hsp:8493
    :724  stesso giapponese di command.hsp:7466
    :878  stesso giapponese di proc.hsp:10793
    :953  stesso giapponese di command.hsp:7098, su un'altra variabile
    :776  «★» resta «*», come main.hsp:980 e text.hsp:12: e' un segno, non testo

## ⚠️ E cinque righe portano un helper inglese che se ne va

`is(tc)` (`:863`, `:890`), `his(c)` a **un** argomento (`:895`) e `_s(c)`
(`:903`, `:907`, `:949`) sono morfologia inglese: `funzioni.py` li toglie, e in
italiano non lasciano buchi perche' il verbo si accorda da solo.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :604-:622 il campo e l'editor delle piastrelle.
    (604, 'You harvested all grown crops and fruits.'):
        'Hai raccolto tutta la frutta e le colture cresciute.',
    # 💡 «piastrelle» viene dal menu del lotto 001, «Cambia gruppo di piastrelle».
    (622, 'Left click to place the tile, right click to pick the tile under your'
          ' mouse cursor, movement keys to move current position, hit the enter'
          ' key to show the list of tiles, hit the cancel key to exit.'):
        'Clic sinistro per posare la piastrella, destro per prendere quella sotto'
        " il cursore, i tasti di movimento per spostare lo schermo, Invio per l'elenco"
        ' delle piastrelle, Esc per uscire.',

    # --- :672-:730 l'esperienza di viaggio e il nome della proprieta'.
    # 💡 Stesso giapponese di main.hsp:8475: si copia parola per parola.
    (672, 'Organize and share your accumulated  travelExp?'):
        '"Vuoi mettere in ordine e spartire i " + gdata(GDATA_TRAVEL_DISTANCE)'
        ' + " punti di esperienza di viaggio accumulati?"',
    # 💡 Stesso giapponese di main.hsp:8493.
    (687, " didn't seem to have anything to gain from the travel."):
        'name(tc) + " non sembra averci guadagnato granché."',
    # 💡 La forma «X: domanda» invece di «domanda a X» evita la preposizione
    #    davanti a un nome che porta gia' il suo articolo (contratto-nomi.md §4).
    (718, 'What do you want to call ? '):
        'mdatan(MDATAN_NAME) + ": che nome vuoi usare? "',
    # 💡 Stesso giapponese di command.hsp:7466.
    (724, 'You changed your mind.'): 'Hai cambiato idea.',

    # --- :749-:776 la finestra del valore della casa.
    (749, 'Home Value'): 'Valore della casa',
    # 💡 I tasti si abbreviano, come in command.hsp:11849 («Dx,Sx [Cambia]»).
    (749, 'Enter key,'): 'Invio,',
    (752, 'Value'): 'Valore',
    (753, 'Heirloom Rank'): 'Rango dei cimeli',
    # ⚠️ 43 px fra l'etichetta e la prima stella, con un carattere da 10: sei
    #    lettere sono il massimo prudente. Vedi il docstring.
    (762, 'Base'): 'Base',
    (762, 'Deco'): 'Arredi',
    (762, 'Heir'): 'Cimeli',
    (762, 'Total'): 'Totale',
    # 💡 Un segno, non testo: resta com'e', come main.hsp:980 e text.hsp:12.
    (776, '*'): '*',

    # --- :824-:907 spostare, ospitare, incaricare.
    (824, 'Move who?'): 'Chi vuoi spostare?',
    (834, " Don't touch me!"): '" " + cnvtalk("Non toccarmi!")',
    (842, 'Where do you want to move ?'):
        '"Dove vuoi spostare " + cdatan(CDATAN_NAME, tc) + "?"',
    (848, 'The location is invalid.'): 'Lì non si può spostare.',
    # ⚠️ `is(tc)` e' morfologia inglese e se ne va.
    (863, '  moved to the location.'):
        '"Hai spostato " + cdatan(CDATAN_NAME, tc) + "."',
    # 💡 Stesso giapponese di proc.hsp:10793.
    (878, 'You need to dissolve the tag-team.'): 'Prima devi sciogliere la coppia.',
    (885, "Your party is already full. You can't invite someone anymore."):
        'Hai già il massimo dei compagni: non puoi portarne altri.',
    (890, '  no longer staying at your home.'):
        'cdatan(CDATAN_NAME, c) + " non è più ospite in casa tua."',
    # ⚠️ `his(c)` a un argomento e' morfologia: in italiano il possessivo si
    #    omette, perche' concorda con la cosa posseduta e non con chi possiede.
    (895, 'You remove  from  job.'):
        '"Hai sollevato " + cdatan(CDATAN_NAME, c) + " dall\'incarico."',
    (903, ' stay at your home now.'):
        'cdatan(CDATAN_NAME, c) + " ora è ospite in casa tua."',
    (907, ' take charge of the job now.'):
        'cdatan(CDATAN_NAME, c) + " ora ha l\'incarico."',

    # --- :924-:985 l'allevamento e il mangime.
    (924, 'You can only leave 150 allies in this ranch.'):
        "Qui puoi lasciarne al massimo 150.",
    (937, "You can't release escort targets."):
        'Non puoi lasciare qui chi devi scortare.',
    (949, ' stay at this ranch.'):
        'cdatan(CDATAN_NAME, c) + " resta all\'allevamento."',
    # 💡 Stesso giapponese di command.hsp:7098, su un'altra variabile.
    (953, ' changed original cloth.'):
        'cdatan(CDATAN_NAME, c) + " riprende l\'aspetto di prima."',
    (974, 'You need a livestock feed.'): 'Non hai mangime per il bestiame.',
    (979, 'Really use ?'): '"Vuoi davvero usare " + itemname(ci, 1) + "?"',
    # ⚠️ Il giapponese non nomina nessuno, l'inglese nomina due cose: la rete 11
    #    pretende le funzioni dell'inglese, e sono `name` e `itemname`.
    (985, ' sprinkled .'):
        'name(CHARA_PLAYER) + " sparge " + itemname(ci, 1) + " qui intorno."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(730, 'You named  .')}

USCITA = 'lavoro/fase4-map_user-003.jsonl'
DA, A = 500, 999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\map_user.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_map_user.jsonl', encoding='utf-8') if l.strip()]
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

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `event.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
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
# `event.hsp:13` compone la lista degli oggetti sulla casella con
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
