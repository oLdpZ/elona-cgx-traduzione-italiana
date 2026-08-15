# -*- coding: utf-8 -*-
"""La toppa di migrazione di `map.hsp:1328`: la casa CARICATA da disco.

⚠️⚠️ **Corregge un errore mio, non di monte: la toppa di `:1396` non basta,
perche' quella riga per una casa gia' salvata non viene mai eseguita.**
`map.hsp:1325`-`:1344` e' il bivio fra caricare e generare:

    existwrapper exedir + "tmp\\\\mdata_" + mid + ".s2"
    if ( strsize != (-1) ) {        ; la mappa esiste su disco
        gosub *game_ctrlFile        ; la carica, mdatan compreso
        ...
        goto *map_preBegin          ; <-- SALTA *map_init_main
    }
    *map_init_main                  ; <-- la guardia di :1396 sta qui

Casa tua e' una mappa **persistente**: dalla seconda visita in poi il file
`mdata_*.s2` c'e', quindi si passa sempre dal ramo di sinistra e `:1396` resta
lettera morta. La guardia serve solo alla **generazione** e al giro di
`mapupdate` (`:1332`, cambio di versione della mappa), che e' il motivo per cui
la toppa di `:1396` resta buona e non si toglie.

💡 **A dirlo e' stato lo schermo, non il codice.** Dopo la prima toppa il log
diceva «Entri qui: **Casa tua**.» — che e' `:1048`, cioe' il ramo `mapname()` —
e due righe piu' giu' ancora «Vuoi lasciare **Your Home**?», che e'
`action.hsp:2183` e legge `mdatan(MDATAN_NAME)`. Le due fonti erano ancora
disallineate, e nessuna misura poteva dirlo.

⭐ **E la sostituzione non aggiunge nessuna `lang()`.** Il valore giusto lo
sa gia' `mapname()`, che `map.hsp:1401` usa per tutte le altre aree: copiarlo
da li' evita di scrivere l'italiano dentro il sorgente, evita una firma nuova
che il dizionario non avrebbe, e tiene la migrazione allineata alla tabella di
`text.hsp` qualunque cosa succeda a quella resa in futuro.

⚠️ Il solo letterale inglese e' `"Your Home"`, che e' il valore **memorizzato**
nel salvataggio, non testo da leggere: sta fuori da `lang()` apposta, come i
nove valori del genere.

⚠️⚠️ **`cerca` e `sostituisci` vogliono una LISTA DI RIGHE, non una stringa con
i fine-riga dentro.** Il primo giro le ha scritte come un'unica stringa con
`\\n`, poi con `\\r\\n`, e non ha agganciato niente nessuna delle due volte:
`applica_toppe` spezza il testo in righe **da se'** (`applica.py:536`) e
confronta liste, quindi un `\\n` dentro la stringa finisce nel corpo di una riga
e non combacia mai. ✅ La forma a lista c'era gia' dal plurale della
parola-contatore di `item_func.hsp` (`applica.py:507`-`:516`), che e' l'unico
altro posto del progetto a usarla.
💡 **E a fermarmi e' stato il guardiano di `applica.py`**, che dice «non esiste
piu'» invece di sostituire a caso: le due volte sbagliate non hanno prodotto un
sorgente rotto, hanno prodotto un errore.

⚠️ Le toppe **non passano da `degrada()`**: la sostituzione non porta accenti.
E si compone e si valida tutto in memoria prima di aprire un file in scrittura.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())

from strumenti import percorsi  # noqa: E402

CERCA = [
    '\t\tfmode = 1',
    '\t\tgosub *game_ctrlFile',
    '\t\tif ( mdata(MDATA_CAN_SAVE) == 0 ) {',
]
SOSTITUISCI = [
    '\t\tfmode = 1',
    '\t\tgosub *game_ctrlFile',
    '\t\tif ( gdata(GDATA_AREA) == AREA_HOME ) {',
    '\t\t\tif ( mdatan(MDATAN_NAME) == "Your Home" ) {',
    '\t\t\t\tmdatan(MDATAN_NAME) = mapname(gdata(GDATA_AREA))',
    '\t\t\t}',
    '\t\t}',
    '\t\tif ( mdata(MDATA_CAN_SAVE) == 0 ) {',
]

MOTIVO = (
    "map.hsp:1328. **Seconda meta' della migrazione di casa tua**, e corregge un errore "
    "di analisi della 42a, non un errore di monte. La toppa di :1396 allarga la guardia "
    "che rinomina la casa, ma quella guardia sta in *map_init_main e per una casa gia' "
    "salvata NON viene mai eseguita: :1325-:1344 carica mdata_*.s2 e fa "
    "`goto *map_preBegin`, saltando il blocco. Casa tua e' persistente, quindi dalla "
    "seconda visita in poi si passa sempre di li'. \u26a0\ufe0f Il difetto e' stato visto a "
    "schermo: dopo la prima toppa il log diceva «Entri qui: Casa tua.» (:1048, ramo "
    "mapname()) e due righe sotto ancora «Vuoi lasciare Your Home?» (action.hsp:2183, "
    "che legge mdatan). \u2705 La migrazione va messa subito dopo il caricamento. 💡 La "
    "sostituzione non aggiunge nessuna lang(): copia il nome da mapname(), che e' quel "
    "che map.hsp:1401 fa gia' per tutte le altre aree, cosi' non si scrive italiano nel "
    "sorgente e non nasce una firma che il dizionario non ha. 💡 La toppa di :1396 resta "
    "e non e' inutile: copre la generazione e il giro di mapupdate (:1332, cambio di "
    "versione della mappa)."
)


def riscrivi(percorso, righe_nuove) -> int:
    """Compone, valida e solo allora scrive: un errore non deve troncare il file."""
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    dati = ('\n'.join(righe) + '\n').encode('utf-8')
    with io.open(percorso, 'wb') as f:
        f.write(dati)
    return len(righe)


# il sorgente si legge a righe, che e' come `applica_toppe` lo guarda
righe_sorgente = io.open(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\map.hsp',
                         encoding='cp932').read().split('\n')
righe_sorgente = [r.rstrip('\r') for r in righe_sorgente]
quante = sum(1 for i in range(len(righe_sorgente) - len(CERCA) + 1)
             if righe_sorgente[i:i + len(CERCA)] == CERCA)
if quante != 1:
    sys.exit(f'il blocco cercato compare {quante} volte nel sorgente, non una')
'\n'.join(SOSTITUISCI).encode('cp932')

toppe = percorsi.PROGETTO / 'toppe.jsonl'
righe = [r for r in io.open(toppe, encoding='utf-8').read().splitlines() if r.strip()]
# toglie i due giri sbagliati, scritti come stringa unica invece che come lista
rotte = {'\n'.join(CERCA), '\r\n'.join(CERCA)}


def e_rotta(riga: str) -> bool:
    """Una toppa scritta come stringa unica invece che come lista di righe."""
    cerca = json.loads(riga).get('cerca')
    return isinstance(cerca, str) and cerca in rotte


tenute = [r for r in righe if not e_rotta(r)]
if len(tenute) != len(righe):
    dati = ('\n'.join(tenute) + '\n').encode('utf-8')
    with io.open(toppe, 'wb') as f:
        f.write(dati)
    print(f'tolte {len(righe) - len(tenute)} toppe scritte nella forma sbagliata')
if any(json.loads(r).get('cerca') == CERCA for r in tenute):
    sys.exit('toppa gia\' presente')
print('toppe.jsonl:', riscrivi(toppe, [json.dumps(
    {'file': 'map.hsp', 'cerca': CERCA, 'sostituisci': SOSTITUISCI, 'motivo': MOTIVO},
    ensure_ascii=False)]), 'toppe')
