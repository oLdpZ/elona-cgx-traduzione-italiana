# -*- coding: utf-8 -*-
"""Le sei righe inglesi che si leggono a ogni apertura d'inventario.

⭐⭐⭐ **Il primo lotto di toppe contro il QUINTO punto cieco** (`nudi_en.py`,
49ª): letterali inglesi che non passano da **nessuna** `lang()`. Non c'e' ramo
di lingua — la riga e' la stessa per giapponese e inglese, ed e' inglese per
tutti — quindi `estrai` non le vede, `verifica --dizionario` non le conta e
nessun lotto puo' raggiungerle. Si toccano **solo** con una toppa.

Sono le sei che il collaudo della 49ª ha visto in faccia:

    command.hsp:14175   s = "" + listmax + " items"          il piede dell'inventario
    command.hsp:14366   mes "" + cdata(CDATA_GOLD, tc) + " gp"   l'oro nell'inventario
    command.hsp:3328    bmes "Page " + (page + 1) + ...      la bacheca degli incarichi
    module.hsp:4141     s = "Page." + (page + 1) + ...       showscroll
    module.hsp:4315     s = "Page." + (page + 1) + ...       display_window2
    module.hsp:4347     s = "Page." + (page + 1) + ...       display_window

## Le rese non sono nuove: due su tre sono gia' state decise altrove

⭐ **` gp` -> ` oro`** non e' una scelta di questa sessione. Lo stesso valore, la
stessa colonna d'oro, e' gia' `lang(" gold", " oro")` in due siti tradotti:
`command.hsp:3677` (la colonna «Paga» dell'elenco alleati) e `text.hsp:193`
(`strgold`, il suffisso che tutto il resto del gioco concatena). La riga 14366
diceva `gp` invece di `gold` **solo** perche' e' un letterale nudo che nessuno
ha mai messo in una `lang()`: allinearla non introduce un termine, ne toglie uno
fuori posto.

⭐ **`Page` -> `Pag.`** ha il suo appiglio in `text.hsp:114`, dove
`" [Page]  "` e' gia' `" [Pagina]  "`. Li' e' l'etichetta di un tasto e ci sta
per intero; qui e' un **contatore** (`Pag. 1/3`), e in italiano un contatore si
abbrevia. ⚠️ La forma segue quella di monte: dove il sorgente scrive `"Page "`
con lo spazio si mette `"Pag. "`, dove scrive `"Page."` col punto si mette
`"Pag."` — cosi' a schermo esce `Pag. 1/3` in tutt'e due i casi.

## La misura: nessuna delle tre resa allunga qualcosa che non abbia posto

⚠️ **`Page` si accorcia, e questo e' il verso giusto.** Le tre righe di
`module.hsp` sono allineate **a destra** — `pos ... - strlen(s) * 7 - 40` — e
stanno sulla **stessa riga** del piede scritto da `display_note`, che e'
anch'esso allineato a destra ma cento pixel piu' a sinistra (`- 140`,
`module.hsp:4360`). Fra i due c'e' un varco: `Page.1/2` sono otto caratteri, 56
px, e comincia a `ww - 96`, cioe' 44 px dopo la fine del piede. `Pag.1/2` e' un
carattere in meno e il varco **sale** a 51. Allungare sarebbe stato l'unico modo
di far danno, e non si allunga.

⚠️ **` items` -> ` oggetti` allunga di due caratteri, e li ha.** Il piede
dell'inventario esce da `display_note`, che allineandolo a destra lo fa crescere
**verso sinistra**, dove non c'e' nient'altro: la riga d'aiuto di
`display_window` sta ventidue pixel piu' in basso (`- 43` contro `- 65`), non
sulla stessa. Quattordici pixel in piu' su una finestra da 640 con la stringa
che parte intorno a `wx + 150`.

⚠️ **` gp` -> ` oro` allunga di sette pixel** e comincia a `wx + 368` in una
finestra larga 640: `30 oro` finisce a `wx + 410`.

⚠️ **`command.hsp:3328` non cambia nemmeno di lunghezza** (`"Page "` e `"Pag. "`
sono tutt'e due di cinque caratteri) ed e' per giunta disegnata **fuori** dalla
finestra, a `wx + ww + 20`.

## Perche' una toppa e non una resa

Non c'e' una resa possibile: non essendoci `lang()`, non c'e' firma, non c'e'
voce di dizionario, non c'e' lotto. ⚠️ E nessuna delle sei righe ne condivide
una con una `lang()`, quindi la regola della 46ª («una toppa e una resa non
stanno sulla stessa riga») e' rispettata senza bisogno di rinvii: il `lang()`
piu' vicino e' a `command.hsp:14176`, la riga dopo.

⚠️ **La toppa vale anche per il ramo giapponese**, perche' la riga e' una sola
per tutt'e due. E' la natura della classe: un letterale nudo non ha un posto
dove tenere il giapponese, e infatti oggi un giocatore giapponese legge
`17 items` come noi. La build e' comunque italiana.

## Due delle sei righe sono identiche fra loro

⚠️ `module.hsp:4315` e `:4347` sono **la stessa riga byte per byte**, due tab e
tutto: una toppa a riga singola sarebbe ambigua e `applica_toppe` si fermerebbe
(giustamente). Si agganciano come **blocco di due righe**, con la riga seguente
a distinguerle — `pos display_window2_arg1 ...` per la prima, `font lang(...)`
per la seconda. `:4141` invece e' rientrata di tre tab ed e' gia' unica da sola.

💡 **Dopo, `nudi_en.py` deve scendere da 872 a 866**: misura le righe della
build ancora **identiche** al sorgente, e queste sei non lo sono piu'.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

COMUNE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca "
    "solo con una toppa. E' il quinto punto cieco, misurato da `scratchpad/nudi_en.py` "
    "nella 49a. La riga e' unica per giapponese e inglese, quindi la toppa vale per "
    "tutt'e due i rami: e' la natura della classe, non una svista."
)

TOPPE = [
    {
        'file': 'command.hsp',
        'riga': 14175,
        'blocco': 1,
        'cerca': '" items"',
        'metti': '" oggetti"',
        'motivo': (
            "command.hsp:14175, il piede dell'inventario: `s = \"\" + listmax + \" items\"`, "
            "cioe' il «17 items» che si legge in fondo a OGNI apertura d'inventario, "
            "subito prima del «(Peso .../...)» della riga dopo (che invece e' una "
            "`lang()` regolare, gia' tradotta). "
            "⚠️ Allunga di due caratteri, e li ha: il piede esce da `display_note` "
            "(module.hsp:4360), che allinea a destra e quindi lo fa crescere verso "
            "SINISTRA, dove non c'e' nient'altro — la riga d'aiuto di `display_window` "
            "sta 22 px piu' in basso (`- 43` contro `- 65`), non sulla stessa riga. "
            "Quattordici pixel su una finestra da 640 con la stringa che parte intorno "
            "a wx+150. "
            "⚠️ Non viola la regola della 46a: la `lang()` piu' vicina e' a :14176, la "
            "riga dopo. " + COMUNE
        ),
    },
    {
        'file': 'command.hsp',
        'riga': 14366,
        'blocco': 1,
        'cerca': '" gp"',
        'metti': '" oro"',
        'motivo': (
            "command.hsp:14366, l'oro mostrato in cima all'inventario quando "
            "`showmoney` e' acceso (il «30 gp» accanto all'icona della moneta). "
            "⭐ La resa non e' nuova: lo stesso valore e' gia' `lang(\" gold\", \" oro\")` "
            "in due siti tradotti — command.hsp:3677 (la colonna «Paga» dell'elenco "
            "alleati) e text.hsp:193 (`strgold`, il suffisso che il resto del gioco "
            "concatena). Qui diceva `gp` invece di `gold` solo perche' e' un letterale "
            "nudo che nessuno ha mai messo in una `lang()`: la toppa non introduce un "
            "termine, ne toglie uno fuori posto. "
            "⚠️ Allunga di sette pixel: comincia a wx+368 in una finestra larga 640, "
            "«30 oro» finisce a wx+410. " + COMUNE
        ),
    },
    {
        'file': 'command.hsp',
        'riga': 3328,
        'blocco': 1,
        'cerca': '"Page "',
        'metti': '"Pag. "',
        'motivo': (
            "command.hsp:3328, il contatore di pagina della bacheca degli incarichi "
            "(`*com_quest_loop`), il «Page 1/3» che il collaudo della 49a ha letto in "
            "inglese. "
            "⭐ `Page` -> `Pag.` ha l'appiglio in text.hsp:114, dove `\" [Page]  \"` e' "
            "gia' `\" [Pagina]  \"`: li' e' l'etichetta di un tasto e ci sta per intero, "
            "qui e' un contatore, e in italiano un contatore si abbrevia. La forma "
            "segue quella di monte: `\"Page \"` con lo spazio -> `\"Pag. \"`, cosi' a "
            "schermo esce «Pag. 1/3». "
            "⚠️ Non cambia di lunghezza (cinque caratteri contro cinque) ed e' per "
            "giunta disegnata FUORI dalla finestra, a wx+ww+20. " + COMUNE
        ),
    },
    {
        'file': 'module.hsp',
        'riga': 4141,
        'blocco': 1,
        'cerca': '"Page."',
        'metti': '"Pag."',
        'motivo': (
            "module.hsp:4141, il contatore di pagina di `showscroll`: il «Page.1/2» in "
            "fondo alle finestre a scorrimento. "
            "⭐ Stessa resa di command.hsp:3328, con la forma di monte: qui il sorgente "
            "scrive `\"Page.\"` col punto e non con lo spazio, quindi `\"Pag.\"` — a "
            "schermo esce «Pag.1/2» come prima usciva «Page.1/2». "
            "⚠️ Il verso e' quello buono: la riga e' allineata a destra "
            "(`- strlen(s) * 7 - 40`) e sta sulla STESSA riga del piede di "
            "`display_note`, che e' allineato a destra cento pixel piu' a sinistra "
            "(`- 140`, :4360). Fra i due c'e' un varco: «Page.1/2» sono otto caratteri, "
            "56 px, e comincia a ww-96, cioe' 44 px dopo la fine del piede. «Pag.1/2» "
            "e' un carattere in meno e il varco sale a 51. Allungare sarebbe stato "
            "l'unico modo di far danno. "
            "⚠️ Questa delle tre e' rientrata di TRE tab ed e' quindi gia' unica da "
            "sola; le altre due sono identiche fra loro e vanno agganciate a coppie. "
            + COMUNE
        ),
    },
    {
        'file': 'module.hsp',
        'riga': 4315,
        'blocco': 2,
        'cerca': '"Page."',
        'metti': '"Pag."',
        'motivo': (
            "module.hsp:4315, il contatore di pagina di `display_window2`. Stessa resa "
            "e stessa misura di module.hsp:4141: `\"Page.\"` -> `\"Pag.\"`, un carattere "
            "in meno su una riga allineata a destra che divide la propria riga col "
            "piede di `display_note`. "
            "⚠️⚠️ Agganciata come BLOCCO DI DUE RIGHE, e non per pignoleria: la riga e' "
            "identica byte per byte a module.hsp:4347 (due tab e tutto), quindi da sola "
            "sarebbe ambigua e `applica_toppe` si fermerebbe. A distinguerla e' la riga "
            "dopo, `pos display_window2_arg1 ...`, dove :4347 ha invece un `font`. "
            + COMUNE
        ),
    },
    {
        'file': 'module.hsp',
        'riga': 4347,
        'blocco': 2,
        'cerca': '"Page."',
        'metti': '"Pag."',
        'motivo': (
            "module.hsp:4347, il contatore di pagina di `display_window`, cioe' quello "
            "che si vede piu' spesso di tutti: e' la finestra dell'inventario, dei menu "
            "e di mezzo gioco. Stessa resa e stessa misura di module.hsp:4141: "
            "`\"Page.\"` -> `\"Pag.\"`, un carattere in meno su una riga allineata a "
            "destra che divide la propria riga col piede di `display_note` (:4360) — "
            "gli stessi 44 px di varco che diventano 51. "
            "⚠️⚠️ Agganciata come BLOCCO DI DUE RIGHE: la riga e' identica byte per "
            "byte a module.hsp:4315 e da sola sarebbe ambigua. A distinguerla e' la "
            "riga dopo, `font lang(cfg_font1, cfg_font2), 12 + sizefix - en * 2, 1`, "
            "dove :4315 ha invece un `pos`. " + COMUNE
        ),
    },
]


def leggi(base: str, nome: str) -> list:
    return io.open(base + '\\' + nome, encoding='cp932').read().split('\n')


def occorrenze(righe: list, blocco: list) -> int:
    n = len(blocco)
    return sum(1 for i in range(len(righe) - n + 1) if righe[i:i + n] == blocco)


nuove = []
for t in TOPPE:
    sorg = leggi(SORGENTE, t['file'])
    build = leggi(BUILD, t['file'])
    inizio = t['riga'] - 1
    blocco = sorg[inizio:inizio + t['blocco']]

    if t['cerca'] not in blocco[0]:
        raise SystemExit(f"{t['file']}:{t['riga']} non ha la forma attesa: {blocco[0].strip()[:120]}")
    # ⚠️ Una toppa si aggancia al testo, non al numero di riga: il blocco dev'essere
    #    unico, e nel SORGENTE e nella BUILD insieme (li' e' dove verra' applicata).
    for righe, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = occorrenze(righe, blocco)
        if quante != 1:
            raise SystemExit(
                f"{t['file']}:{t['riga']} compare {quante} volte nel {eti}, non una: "
                "toppa ambigua, allarga il blocco"
            )
    # ⚠️ Nessuna delle righe agganciate puo' portare una RESA: e' la regola della
    #    46a (una toppa e una resa non stanno sulla stessa riga). Si guarda
    #    `lang("`, col letterale: `lang(cfg_font1, cfg_font2)` passa due VARIABILI
    #    e non e' un sito di dizionario.
    for riga in blocco:
        if 'lang("' in riga:
            raise SystemExit(f"{t['file']}:{t['riga']}: il blocco tocca una resa (`lang(\"...\")`)")

    nuovo = list(blocco)
    nuovo[0] = blocco[0].replace(t['cerca'], t['metti'])
    if nuovo == blocco:
        raise SystemExit(f"{t['file']}:{t['riga']}: la toppa non cambierebbe niente")
    if blocco[0].count(t['cerca']) != 1:
        raise SystemExit(f"{t['file']}:{t['riga']}: `{t['cerca']}` compare piu' di una volta nella riga")

    cerca = blocco[0] if t['blocco'] == 1 else blocco
    sostituisci = nuovo[0] if t['blocco'] == 1 else nuovo
    nuove.append({'file': t['file'], 'cerca': cerca, 'sostituisci': sostituisci,
                  'motivo': t['motivo'], '_riga': t['riga']})

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
da_scrivere = [t for t in nuove if _chiave(t) not in gia]

if not da_scrivere:
    print('toppe gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = ''.join(
        json.dumps({k: v for k, v in t.items() if not k.startswith('_')},
                   ensure_ascii=False) + '\n'
        for t in da_scrivere
    ).encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)})')
    for t in da_scrivere:
        print(f"  {t['file']}:{t['_riga']}")
        for r in (t['cerca'] if isinstance(t['cerca'], list) else [t['cerca']]):
            print(f"    - {r.strip()}")
        for r in (t['sostituisci'] if isinstance(t['sostituisci'], list) else [t['sostituisci']]):
            print(f"    + {r.strip()}")
