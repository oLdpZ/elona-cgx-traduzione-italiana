# -*- coding: utf-8 -*-
"""Gli atti di proprieta', il pannello della struttura e la scala dei potenziali.

`map_user.hsp:39`-`:431`, cinquantacinque voci: leggere un atto e costruire
(`:39`-`:227`), e poi il pannello che il gioco stampa **prima** del menu di casa
del lotto 001 — quanti oggetti ci sono, che negozio e', chi ci lavora e quanto
vale (`:286`-`:431`).

## ⭐ La scala dei potenziali non esisteva, e adesso c'e'

Sedici voci su cinquantacinque sono la stessa scala scritta due volte, per la
trattativa (`:365`-`:383`) e per il carisma (`:387`-`:405`). ⚠️ **Nessuna delle
sette parole era mai stata resa nel progetto**: `Supreme`, `Amazing`, `Superb`,
`Great`, `Good`, `Bad`, `Hopeless` non compaiono in nessun dizionario, e il
giapponese le tiene **in inglese** dentro le quadre.

    Supreme -> Supremo    Great -> Notevole    Hopeless -> Nullo
    Amazing -> Enorme     Good  -> Buono
    Superb  -> Ottimo     Bad   -> Scarso

⭐ Le prime tre le detta `text.hsp:107`, la scala delle **resistenze**, gia' resa
«Suprema / Enorme / Ottima»: sono le stesse parole al maschile, perche' qui
concordano con «potenziale». Le altre quattro sono nuove, e stanno sotto.

## ⚠️ Il giapponese conta i prigionieri, l'inglese no

`:321` interpola **tre** valori in giapponese — 収容者 (quanti), 労働強度,
労働エナジー — e solo **due** in inglese: il conto dei prigionieri sparisce.
Non e' una scelta: le venti righe sopra (`:310`-`:320`) esistono **solo** per
calcolare `pet`, e senza quella riga il ciclo non serve a niente. Si segue il
giapponese, cioe' il codice.
💡 `pet` e' una variabile, non una funzione: la rete 11 confronta le funzioni di
contenuto e non se ne accorge. E' la stessa famiglia dell'«inglese che sa di
meno» della 57a, con la differenza che qui la prova sta nel ciclo di sopra.

## ⚠️ L'articolo lo porta il nome, e otto nomi lo portano

`:227` e' «あなたは + s + を建設した！», dove `s` e' uno degli otto edifici di
`:178`-`:223`. In italiano la frase vuole un articolo, e `contratto-nomi.md` §4
dice che **lo porta il nome**: `s` diventa «un museo», «un campo di prigionia»,
«un sotterraneo». Scrivere «Hai costruito un " + s + "!» funzionerebbe **oggi**,
perche' tutt'e otto sono maschili e cominciano per consonante, e si romperebbe
il giorno che CGX aggiunge un atto per una fattoria.

⚠️ **Non sono i nomi di `text.hsp:2806`**, che pure hanno lo stesso giapponese:
li' sono i **nomi propri** della proprieta' sulla mappa («Museo», «Campo di
prigionia»), qui sono nomi comuni dentro una frase. L'inglese di monte lo dice
scrivendoli in due modi, «My Museum» contro «museum».

## Quel che si e' copiato invece di scriverlo

    :54   ha lo stesso inglese di action.hsp:14742, gia' reso
    :91   e' la nona copia di «Hai imparato una nuova capacita': ...»
    :178-:216  gli edifici, dal contesto gia' reso di text.hsp:2806-:2821
    :325-:343  i tipi di negozio, dagli epiteti di text.hsp:424-:460 —
               «bazar», «drogheria», «bottega magica», «armeria», «locanda»
    :431  «Che cosa vuoi fare?», da command.hsp:17531

Restano nuovi solo 装飾家具店 e ジャンク屋, che nessun epiteto nomina.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :39-:153 leggere un atto, costruire, traslocare.
    (39, 'Property No.  has been registered. ()'):
        '"Registrata la proprietà n. " + inv(INV_ITEM_PARAM2, ci) + " ("'
        ' + adata(ADATA_ARENA_WIN, gdata(GDATA_AREA)) + ")"',
    (48, 'You must read it inside a building to register your property.'):
        'Per registrare la proprietà, va letto dentro la struttura.',
    # 💡 Stesso inglese di action.hsp:14742, gia' reso: si copia.
    (54, 'You can only use it in the world map.'):
        'Si usa sulla mappa del mondo.',
    (60, "You can't build it here."): 'Qui non si può costruire.',
    (72, "You can't build a building anymore."):
        'Non puoi costruire altri edifici.',
    (77, 'Really build it here? '): 'Vuoi davvero costruire qui? ',
    (80, 'Really move it here? '): 'Vuoi davvero spostarlo qui? ',
    # 💡 La nona copia della stessa riga: action.hsp:12012 e altre otto.
    (91, 'You have learned a new ability, .'):
        '"Hai imparato una nuova capacità: " + skillname(SKILL_SPACT_MARKING) + "."',
    (111, "You've built a new house!"): 'Hai costruito una casa nuova! ',
    (130, "You've moved your house!"): 'Trasloco completato! ',
    (153, 'Property relocation finished!'): 'Spostamento completato! ',

    # --- :178-:227 gli otto edifici, e la frase che li nomina.
    # ⚠️ L'articolo lo porta il nome (contratto-nomi.md §4): scrivere
    #    «un " + s + "» reggerebbe solo finche' tutti sono maschili.
    # ⚠️ Non sono i nomi propri di text.hsp:2806 («My Museum» contro «museum»):
    #    li' e' il nome della proprieta' sulla mappa, qui un nome comune.
    (178, 'museum'): 'un museo',
    (184, 'camp'): 'un campo di prigionia',
    (190, 'shop'): 'un negozio',
    (196, 'crop'): 'un campo',
    (202, 'storage'): 'un magazzino',
    (209, 'ranch'): 'un allevamento',
    (216, 'dungeon'): 'un sotterraneo',
    (223, 'discarded ranch'): 'un allevamento abbandonato',
    (227, "You've built a !"): '"Hai costruito " + s + "!"',

    # --- :286-:321 il pannello della struttura.
    # 💡 Il giapponese dice «questo non e' casa tua», l'inglese il contrario
    #    dalla stessa parte. Si segue il giapponese, che e' la colonna che si
    #    legge accanto alla resa.
    (286, 'You can only use it in your home.'): 'Questa non è casa tua.',
    (306, 'There are  items and  furniture in .(Max: ) '):
        'mapname(gdata(GDATA_AREA)) + " contiene " + p + " oggetti e " + p(1)'
        ' + " mobili (al massimo " + p(2) + ") "',
    # ⚠️ L'inglese perde il conto dei prigionieri, che il giapponese ha e che le
    #    venti righe di sopra esistono solo per calcolare. Si segue il codice.
    (321, 'Current Toil-Lv is , Toil-Energy is .'):
        '"I prigionieri sono " + pet + ", il livello di lavoro è "'
        ' + adata(ADATA_LABOR_CAMP_TOIL_LEVEL, gdata(GDATA_AREA))'
        ' + " e l\'Energia da Lavoro accumulata è "'
        ' + adata(ADATA_LABOR_CAMP_TOIL_ENERGY, gdata(GDATA_AREA)) + "."',

    # --- :325-:359 il negozio. I nomi vengono dagli epiteti di text.hsp:424+,
    #     che il progetto ha gia' fissato: «del bazar», «della drogheria»,
    #     «della bottega magica», «dell'armeria», «della locanda».
    (325, 'Goods shop'): 'bazar',
    (328, 'Food shop'): 'drogheria',
    (331, 'Magic shop'): 'bottega magica',
    (334, 'Blacksmith'): 'armeria',
    (337, 'Inn shop'): 'locanda',
    (340, 'Decorative arts shop'): 'negozio di arredi',
    (343, 'Junk shop'): 'rigattiere',
    (345, 'Shop type: .'): '"Tipo di negozio: " + shops + "."',
    (347, 'No sale restrictions.'): 'Nessun limite di vendita.',
    (350, 'Sales limited to 15 items.'): 'Vendita limitata a 15 pezzi al giorno.',
    (353, 'Sales limited to 5 items.'): 'Vendita limitata a 5 pezzi al giorno.',
    (356, 'Current shopkeeper is .'):
        '"Il negoziante è " + cdatan(CDATAN_NAME, getworker(gdata(GDATA_AREA))) + "."',
    (359, "You haven't assigned a shopkeeper yet."):
        "Al momento non c'è nessun negoziante.",

    # --- :365-:405 la scala dei potenziali, due volte.
    # ⭐ Le prime tre parole le detta text.hsp:107, la scala delle resistenze,
    #    gia' resa «Suprema / Enorme / Ottima»: qui concordano con
    #    «potenziale», che e' maschile. Le altre quattro sono nuove.
    (365, '[Trade potential : Supreme]'): '[Potenziale trattativa: Supremo]',
    (368, '[Trade potential : Amazing]'): '[Potenziale trattativa: Enorme]',
    (371, '[Trade potential: Superb]'): '[Potenziale trattativa: Ottimo]',
    (374, '[Trade potential: Great]'): '[Potenziale trattativa: Notevole]',
    (377, '[Trade potential: Good]'): '[Potenziale trattativa: Buono]',
    (380, '[Trade potential: Bad]'): '[Potenziale trattativa: Scarso]',
    (383, '[Trade potential: Hopeless]'): '[Potenziale trattativa: Nullo]',
    (387, '[Charisma potential : Supreme]'): '[Potenziale carisma: Supremo]',
    (390, '[Charisma potential : Amazing]'): '[Potenziale carisma: Enorme]',
    (393, '[Charisma potential: Superb]'): '[Potenziale carisma: Ottimo]',
    (396, '[Charisma potential: Great]'): '[Potenziale carisma: Notevole]',
    (399, '[Charisma potential: Good]'): '[Potenziale carisma: Buono]',
    (402, '[Charisma potential: Bad]'): '[Potenziale carisma: Scarso]',
    (405, '[Charisma potential: Hopeless]'): '[Potenziale carisma: Nullo]',
    # 営業実績 e' il venduto accumulato dal negoziante.
    (407, '[Sales exp: ]'):
        '"[Vendite: " + cdata(CDATA_SALES_EXP, sc) + "]"',

    # --- :412-:431 l'allevamento, la casa, e la domanda che apre il menu.
    (412, 'Current breeder is .'):
        '"L\'allevatore è " + cdatan(CDATAN_NAME, getworker(gdata(GDATA_AREA))) + "."',
    (415, "You haven't assigned a breeder yet."):
        "Al momento non c'è nessun allevatore.",
    (428, ' members are staying at your home. (Max: ).'):
        '"In casa ci sono " + p + " ospiti (al massimo "'
        ' + (gdata(GDATA_HOME_LEVEL) + 2) + ")."',
    # 💡 Da command.hsp:17531, «[Personalizzazione] Che cosa vuoi fare?».
    (431, 'What do you want to do?'): 'Che cosa vuoi fare?',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-map_user-002.jsonl'
DA, A = 1, 499
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
