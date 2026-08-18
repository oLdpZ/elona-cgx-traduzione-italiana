# -*- coding: utf-8 -*-
"""Il menu di casa: negozio, allevamento, campo di prigionia, casa, campo.

`map_user.hsp:433`-`:515`, cioe' le trentadue voci del menu che si apre premendo
il tasto delle strutture dentro una proprieta'. E' la **prima apertura di
`map_user.hsp`**: il file non aveva nessun dizionario, e quindi
`verifica --dizionario` non lo nominava — 204 `lang()` che nessun conteggio
guardava. Dopo questo lotto il file entra nel referto con 174 voci da fare.

⭐ **Il lotto nasce da una misura, non da un elenco.** La 60a ha portato la
rete 5 fuori da `text.hsp`, e il referto ha detto che `map_user.hsp` ha
**trentaquattro voci di menu senza dizionario**: sono il gruppo piu' grosso di
tutto il gioco in un riquadro solo.

## ⚠️ Il riquadro e' 280 px, e il tetto e' 30 caratteri

`map_user.hsp:537` chiude la corsa dei `promptAdd`, e sopra ci sono **tre**
`val =`:

    :522   val = promptx, prompty, 280, 1          dentro /* ... */   MORTO
    :529   val = promptx, prompty, 280 + (en * 50), 1   se e' un negozio: 330
    :532   val = promptx, prompty, 280, 1               altrimenti: 280

⚠️ **Le sette voci del negozio vivono davvero in un riquadro da 330** (tetto 36),
perche' stanno dentro la stessa `if ( adata(ADATA_ID, ...) == AREA_SHOP )` che lo
allarga — il mod lo dice nel commento, «Increase the size of the shopkeeper
window». La rete pero' tiene il **piu' stretto**, che e' la regola giusta per una
guardia, e tutte le rese di questo lotto stanno **dentro 30**: la piu' lunga ne
usa 28. Nessuna ha avuto bisogno del riquadro largo.

## Il vocabolario, tutto gia' deciso altrove

    negoziante          店主, da db_creature.hsp:74301 e ai.hsp:1834
    talento             フィート, da command.hsp:2113 «[Talenti disponibili]»
    bestiame            家畜, da chara_func.hsp:2067 e db_item.hsp:137486
    allevatore          ブリーダー, da proc.hsp:21819 «Effetto allevatore»
    prigioniero         収容者/連行者, da command.hsp:1197 e adv.hsp:197
    rinchiudere         収容する, da command.hsp:1196 «Chi vuoi rinchiudere?»
    Energia da Lavoro   労働エナジー, da map.hsp:12281 e proc.hsp:4135
    moneta di bronzo    ブロンズ硬貨, da db_item.hsp:137911
    compagno            仲間, la resa dominante in tutto il dizionario

💡 **Quattro voci su trentadue erano gia' decise**, e cercarle e' costato meno
che scriverle: `:456` porta al menu di `text.hsp:1646` («15 al giorno (Esp.
Trattativa+)»), `:480` a quello di `text.hsp:2213` («<Livello 0> lavora chi ne
ha voglia»), e le rese di questo lotto ne prendono le parole invece di
inventarne altre.

## ⚠️ Le due coppie simmetriche

`:465`/`:468` e `:471`/`:474` sono attiva/annulla dello stesso codice, e in
giapponese cambia una parola sola (発動 / 解除). Le rese sono una coppia anche in
italiano — «Blocca» / «Sblocca» — invece di due frasi diverse: un menu dove due
voci opposte non si somigliano si legge due volte.
⚠️ Ci si perde コード, «codice»: sta nel giapponese e nell'inglese, ma dire
«Attiva il codice antiriproduzione» costa 33 caratteri su 30. Si tiene quel che
il giocatore deve capire — che cosa succede — e si lascia andare il come.

## ⚠️ Dove il giapponese dice piu' dell'inglese

    :461  家畜・ブリーダー移動  sposta il bestiame **e** gli allevatori;
          l'inglese dice solo «Move a livestock». La resa segue il giapponese.
    :462  餌を撒く（家畜の餌消費）  l'azione e' «spargere il mangime», il
          consumo e' la nota fra parentesi. L'inglese tiene solo la nota.
    :463  場内消毒（浄化消毒薬消費）  stessa forma: l'azione e' disinfettare.
    :489  家の情報 dice «informazioni», l'inglese «Home rank». La schermata
          mostra il rango dentro le informazioni: la resa tiene la piu' larga.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :433 il primo, e vale fuori da ogni struttura. 旅経験 e' «esperienza
    #     di viaggio» da main.hsp:8475, che e' la finestra di conferma di
    #     questa stessa voce: li' c'e' spazio per la frase intera, qui no.
    (433, 'Organize and share travelExp'): 'Ordina i punti di viaggio',

    # --- :443-:457 il negozio. Sette voci, e sono quelle che vivono nel
    #     riquadro largo 330: nessuna ne ha avuto bisogno.
    # 💡 仲間に…頼む e' «chiedere a un compagno», non «assumere uno sconosciuto».
    (443, 'Assign a shopkeeper'): 'Metti un compagno al negozio',
    # ⚠️ La lang() e' il solo «Extend»: il « (N GP)» sta FUORI, concatenato dopo
    #    (`:445`). Una resa lunga qui sfora il riquadro senza che il dizionario
    #    lo veda, perche' la rete misura la lang() e non la riga.
    (445, 'Extend'): 'Ingrandisci',
    (447, 'Change shop type'): 'Cambia tipo di negozio',
    # ⚠️ dinamica: `kunren` e' il costo, e vale 1000000 quando il negoziante non
    #    ha la trattativa — sette cifre. Con la resa corta ci stanno lo stesso.
    (450, 'Train shopkeeper for  bronze coins'):
        '"Addestra (" + kunren + " di bronzo)"',
    (454, 'Get shopkeeper feat'): 'Prendi il talento da negozio',
    # 💡 Porta al menu di text.hsp:1646, gia' reso «15 al giorno (Esp. Trattativa+)».
    (456, 'Limit sales per day'): 'Limita le vendite al giorno',
    # ⚠️ 未実装 / «Unimplemented»: la voce c'e' e non fa niente. Va detto, o
    #    chi gioca la prova ogni volta.
    (457, 'Hire part time worker (Unimplemented)'): 'Assumi un aiuto (non attivo)',

    # --- :460-:474 l'allevamento.
    (460, 'Assign a breeder'): 'Nomina un allevatore',
    # 💡 Il giapponese sposta 家畜・ブリーダー, tutt'e due; l'inglese dimentica
    #    gli allevatori.
    (461, 'Move a livestock'): 'Sposta bestiame e allevatori',
    # 💡 L'azione e' 餌を撒く, «spargere il mangime»; il consumo e' la nota fra
    #    parentesi, ed e' l'unica cosa che l'inglese tiene.
    (462, 'Consume livestock feed'): 'Spargi il mangime',
    (463, 'Consume disinfectant'): 'Disinfetta i locali',
    # ⚠️ Le due coppie: in giapponese cambia una parola sola (発動 / 解除), e in
    #    italiano cambia una lettera. Due voci opposte devono somigliarsi.
    #    Si perde コード, «codice»: «Attiva il codice antiriproduzione» fa 33.
    (465, 'Activate breeding-prevent code'): 'Blocca la riproduzione',
    (468, 'Cancel breeding-prevent code'): 'Sblocca la riproduzione',
    (471, 'Activate production-prevent code'): 'Blocca la produzione',
    (474, 'Cancel production-prevent code'): 'Sblocca la produzione',

    # --- :478-:481 il campo di prigionia. «rinchiudere» e «prigioniero» sono
    #     di command.hsp:1196-:1197 e adv.hsp:197; «Energia da Lavoro» di
    #     map.hsp:12281.
    (478, 'Contain a inmate'): 'Rinchiudi un prigioniero',
    (479, 'Move a inmate'): 'Sposta un prigioniero',
    # 💡 Porta al menu di text.hsp:2213, dove 強度N e' gia' «<Livello N>».
    (480, 'Change Toil-Lv'): 'Cambia il livello di lavoro',
    (481, 'Exchange Toil-Energy'): "Scambia l'Energia da Lavoro",

    # --- :484-:504 la casa.
    (484, 'Release ally'): 'Libera un compagno',
    (485, 'Move a stayer'): 'Sposta un ospite',
    (487, 'Design'): 'Ridecora la casa',
    # ⚠️ Il giapponese dice 家の情報, «informazioni»; l'inglese «Home rank». La
    #    schermata mostra il rango dentro le informazioni: si tiene la piu' larga.
    (489, 'Home rank'): 'Informazioni sulla casa',
    (490, 'Allies in your home'): 'Compagni in casa',
    (492, 'Recruit a servant'): 'Assumi un domestico',
    (499, 'Change door type'): 'Cambia tipo di porta',
    (500, 'Change tile group'): 'Cambia gruppo di piastrelle',
    (501, 'Change Map Icon'): "Cambia l'aspetto esterno",
    (504, 'Change Map Name'): 'Cambia nome alla struttura',
    # ⚠️ :507 e` scritta nella forma ESPANSA della macro — `promptl(0, promptmax)
    #    = lang(...)` invece di `promptAdd lang(...)` — ed e` la trentatreesima
    #    voce dello stesso riquadro. La rete 5 non la vedeva: e` stata questa
    #    riga a farlo scoprire, ed erano 37 righe in sette file.
    # 💡 お片付け e` mettere in ordine, non raccogliere il raccolto: «riordino»
    #    la tiene distinta da «Raccogli il prodotto» due voci piu` sotto.
    (507, 'Collecting function'): 'Funzione di riordino',

    # --- :514-:515 il campo.
    (514, 'Plant seeds'): 'Pianta dei semi',
    (515, 'Collect yield'): 'Raccogli il prodotto',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map_user-001.jsonl'
DA, A = 433, 515
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
