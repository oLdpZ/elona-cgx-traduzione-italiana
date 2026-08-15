# -*- coding: utf-8 -*-
"""Lotto `command-037`: **la finestra dell'inventario e il banco del negozio**.
Ventidue rese, da `:14211` a `:14717`.

⭐ **La zona 14000-14999 sta tutta dentro una routine sola**: `*com_inventory_loop`
va da `:13971` a `:15990`, e la 15000-15999 è già chiusa. Non c'è nessuna
famiglia tagliata a metà — la trappola del lotto 031 — e le due intestazioni
delle resistenze di `:14127`/`:14136`, che la 47ª segnalava come primo scoglio
della zona, sono **già rinviate**: la zona da fare comincia a `:14211`.

⭐⭐ **Le cinque etichette della finestra hanno tutte un tetto calcolabile, e per
la prima il carattere NON è quello di corpo 12.** `:14203` scrive
`font lang(cfg_font1, cfg_font2), 12 + en - en * 2, 0`, e `config.hsp:439` mette
`en = 1` nel ramo inglese: fa **corpo 11**, cioè 6,6 px a carattere e non 7,2.
È esattamente l'avvertimento che il collaudo della 47ª ha lasciato scritto —
**il corpo va letto sulla riga, non dato per scontato**.
- `:14211` «Equip:» sta fra `x = wx + 40` (`:14208`) e `x += 60` (`:14212`), da
  dove partono i `bodyn`: **60 px / 6,6 = 9 caratteri**. «Parti:» ne fa 6.
- `:14272` e `:14275` finiscono in `s(1)`, che `:14352` **allinea a destra** con
  `pos wx + 600 - strlen(s(1)) * 7`. ⚠️ Il 7 è di monte ed è **stretto**: il
  corpo lì è quello di `:14243`, `14 - en * 2` = 12, cioè 7,2 px. Una resa di L
  caratteri parte a `wx + 600 - 7L` e finisce davvero a `wx + 600 + 0,2L`:
  «30 medagliette» (14) sfora di **3 px**, e per toccare il nome dell'oggetto
  (che `cs_list` disegna da `wx + 88`) servirebbe un nome da 57 caratteri. Al
  banco delle medagliette non ce ne sono.
- `:14280` e `:14325` si **appendono al nome dell'oggetto**; a destra il peso
  occupa cinque o sei caratteri fino a `wx + 600`, quindi nome più coda devono
  stare sotto i ~65 caratteri. « (per terra)» costa due caratteri più di
  « (Ground)»; « (tiro)» ne costa due **meno** di « (Range)».

⭐ **Nessuna delle cinque parole si è dovuta scegliere: erano già decise tutte.**
「部位」 è «Parte» in `:12620` («Parte/Nome») e «Parti» in `:1273`; 「メダル」 è
«Medagliette» in `:13941` e in `:14105`, 「チケット」 «Biglietti» in `:13952` e in
`:14108`; 「足元」 è «per terra» in `:6703`, `:6707` e `map.hsp:9914`; 「遠隔」 è
**«Tiro»** in `text.hsp:136`, e `:15309`/`:15312` lo declinano già «da Tiro» e
«nel Tiro» parlando proprio di questo slot.

⚠️⚠️ **`:14531`, `:14643` e `:14646` sono tre inglesi IDENTICI dove il giapponese
distingue, e la distinzione si può riprendere senza toccare il contratto.**
Tutt'e tre dicono «How many? (1 to N)»; il giapponese dice 「いくつ落とす？」,
「いくつ買う？」, 「いくつ売る？」 — quante ne lasci, ne compri, ne vendi. Il
giapponese lo fa nominando l'oggetto con `itemname(ci, 1)`, e **quello non si
può fare**: la rete 11 non lascia aggiungere una funzione che l'inglese non ha.
Ma il verbo non è una funzione. ✅ Quindi «Quanti ne lasci?», «Quanti ne compri?»,
«Quanti ne vendi?»: la distinzione torna, il contratto resta `['inv']`.

⚠️ **`:14487` è l'unica resa che ha dovuto cambiare forma per un accordo.**
`name_of_seed_planted` viene da `ioriginalnameref` (`:14455`) ed è un nome
**singolare** — «seme di erba», «seme di frutto» — mentre
`number_of_seeds_planted` può valere 1 come 30. «Hai piantato 3 seme di erba» è
sgrammaticato in italiano quanto «You've planted 3 seed of herb» lo è in inglese,
ma qui si può evitare: «Semi piantati: 3 (seme di erba).» regge tutt'e due i
numeri, perché l'etichetta non concorda con niente. È la forma di `:78` nel lotto
001 («tipi di oggetti»), cioè un nome infilato fra il numero e la variabile.
💡 E le due variabili non sono chiamate: `funzioni_di_contenuto` dell'inglese è
vuota, quindi qui la rete 11 non chiede niente.

⭐ **Riscosse senza decidere due rese e una parola.** `:14717` ha lo **stesso
giapponese** di `action.hsp:3386` ed è ricopiata parola per parola — «Puoi ancora
reclamare … oggetti in eredità» — e da lì viene anche «eredità» per `:14616`.
⚠️ Nell'inglese di `:14717` c'è `_s3(...)`, che è morfologia: sparisce insieme al
suo argomento, e il contratto resta il solo `gdata` di testa.
La parola «portafogli» (`:14683`, `:14692`) la scrive così `proc.hsp` in cinque
righe — `:3389`, `:9474`, `:9482`, `:21991`, `:21994` — mentre
`db_item.hsp:148929` dice «portafoglio»: nel registro del log vince `proc.hsp`.
💡 E le due rese del portafoglio sono **la stessa frase in due persone**: `:14683`
è il giocatore («Apri il portafogli e chini la testa…»), `:14692` è chi vende
(`name(tc)` in tutt'e due le lingue, quindi terza persona per la regola di
`init.hsp:1704`).

💡 **Un inglese che copre due giapponesi diversi, e la rete 13 lo dirà.**
«The container is full.» sta per 「これ以上入らない。」 (`:14569`, non ci entra) e per
「これ以上置けない。」 (`:14583`, non ci si può posare): due contenitori diversi,
stesso evento per chi gioca. Le due rese sono **volutamente identiche**.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # Le cinque etichette della finestra dell'inventario (:14211-:14325)
    # ================================================================
    # ⚠️ Tetto 9 caratteri: 60 px fra `:14208` e `:14212`, corpo 11 (`:14203`,
    #    `12 + en - en * 2` con `en = 1`), cioe' 6,6 px a carattere.
    # ⭐ 「部位」 e' gia' «Parte» in :12620 e «Parti» in :1273.
    (14211, 'Equip:'):
        'Parti:',

    # ⚠️⚠️ Il giapponese e' lo STESSO 「 枚」 nei due rami — un puro classificatore
    #    — e la rete 4 pretende una resa sola. Ha ragione: a distinguere e'
    #    `invctrl(1)`, non il testo, e la distinzione la porta gia'
    #    l'INTESTAZIONE della colonna, che :14105 rende «Medagliette» e :14108
    #    «Biglietti». L'inglese, mettendo «Coins» e «Tickets», la ripete due
    #    volte. ✅ «pz.» e' il classificatore italiano e regge anche l'1, che
    #    «pezzi» non reggerebbe.
    (14272, ' Coins'):
        ' pz.',
    (14275, ' Tickets'):
        ' pz.',

    # ⭐ 「足元」 e' «per terra» in :6703, :6707 e map.hsp:9914.
    (14280, ' (Ground)'):
        ' (per terra)',
    # ⭐ 「遠隔」 e' «Tiro» in text.hsp:136, e :15309/:15312 dicono gia' «da Tiro»
    #    e «nel Tiro» parlando di questo stesso slot.
    (14325, ' (Range)'):
        ' (tiro)',

    # ================================================================
    # Piantare i semi (:14487)
    # ================================================================
    # ⚠️ `name_of_seed_planted` (`:14455`, ioriginalnameref) e' SINGOLARE e
    #    `number_of_seeds_planted` puo' valere 1: il numero non puo' stargli
    #    davanti. L'etichetta non concorda con niente e regge tutt'e due i casi.
    (14487, "You've planted  ."):
        '"Semi piantati: " + number_of_seeds_planted + " (" + name_of_seed_planted + ")."',

    # ================================================================
    # Lasciare per terra, i contenitori, il cimitero (:14517-:14595)
    # ================================================================
    # ⚠️ Il ramo e' `inv_getspace(-1) == 0`: e' il TERRENO che non ne prende piu'.
    (14517, "You can't drop items any more."):
        "Non c'è più spazio per terra.",
    (14569, 'The container is full.'):
        'Non ci entra altro.',
    # ⭐ 「霊園」 e' «Cimitero» in text.hsp:50.
    (14576, 'The cemetery is full.'):
        'Il cimitero è pieno.',
    # 💡 Stesso inglese di :14569 su un giapponese diverso (置けない contro
    #    入らない): due contenitori, stesso evento. Resa identica di proposito.
    (14583, 'The container is full.'):
        'Non ci entra altro.',
    # ⚠️ Il giapponese dice 以上, «da tanto in su»; l'inglese lo gira in «less
    #    than». Si segue il giapponese, che e' quello che il codice controlla
    #    (`inv(INV_ITEM_WEIGHT, ci) >= efp * 100`).
    (14590, 'The container can only hold items weighing less than .'):
        '"Non ci entra niente che pesi " + cnvweight(efp * 100) + " o più."',
    # ⭐ 「荷物」 e' la roba del carretto: :15923 dice «Le cose sul carretto».
    (14595, 'The container cannot hold cargos'):
        'Le cose del carretto non ci entrano.',

    # ================================================================
    # L'eredita' (:14616, :14717)
    # ================================================================
    (14616, "You don't have a claim."):
        'Non hai nessun diritto di eredità.',
    # ⭐ Stesso giapponese di action.hsp:3386, ricopiata parola per parola.
    # ⚠️ `_s3(...)` e' morfologia e sparisce col suo argomento: il contratto e'
    #    il solo `gdata` di testa.
    (14717, 'You can claim  more heirloom.'):
        '"Puoi ancora reclamare " + gdata(GDATA_HEIR_DEED) + " oggetti in eredità."',

    # ================================================================
    # Il banco del negozio (:14643-:14692)
    # ================================================================
    # ⚠️⚠️ Tre inglesi identici su tre giapponesi diversi. Il giapponese
    #    distingue nominando l'oggetto con `itemname(ci, 1)`, che la rete 11 non
    #    lascia aggiungere; il VERBO pero' non e' una funzione, e la
    #    distinzione torna con quello. Contratto: `['inv']` in tutt'e tre.
    (14531, 'How many? (1 to )'):
        '"Quanti ne lasci? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',
    (14643, 'How many? (1 to )'):
        '"Quanti ne compri? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',
    (14646, 'How many? (1 to )'):
        '"Quanti ne vendi? (da 1 a " + inv(INV_ITEM_NUM, ci) + ")"',

    (14668, 'Do you really want to buy  for gp?'):
        '"Vuoi davvero comprare " + itemname(ci, in) + " per " + '
        'in * calcitemvalue(ci, 0) + " gp?"',
    (14671, 'Do you really want to sell  for gp?'):
        '"Vuoi davvero vendere " + itemname(ci, in) + " per " + '
        'in * calcitemvalue(ci, 1) + " gp?"',

    # ⭐ «portafogli»: proc.hsp lo scrive cosi' in :3389, :9474, :9482, :21991
    #    e :21994. La seconda meta' segue l'inglese, che china la testa; il
    #    giapponese dice 「がっかりした」, che e' la stessa cosa detta d'umore.
    (14683, 'You check your wallet and shake your head.'):
        'Apri il portafogli e chini la testa...',
    (14683, 'You need to earn more money!'):
        'Devi guadagnare di più!',
    # ⚠️ `his(tc)` a un argomento e' morfologia e sparisce: resta il solo `name`.
    # 💡 Stessa frase di :14683 in terza persona, perche' qui c'e' `name(tc)`.
    (14692, ' checks  wallet and shakes  head.'):
        'name(tc) + " apre il portafogli e china la testa..."',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-037.jsonl'
DA, A = 14000, 14717
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
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
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
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
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
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
