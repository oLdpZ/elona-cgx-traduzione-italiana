# -*- coding: utf-8 -*-
"""La toppa di migrazione di `map.hsp:1396`: i salvataggi vecchi che portano
«Your Home» scritto dentro.

⭐⭐ **E' la prima toppa di MIGRAZIONE del progetto.** Le 303 esistenti
correggono un errore di monte — un personaggio sbagliato, un inglese ricopiato
male, una chiave di `cnv_str` che non aggancia. Questa non corregge niente:
converte un **dato vecchio** scritto in un salvataggio prima che il file fosse
tradotto.

⚠️⚠️ **Il difetto lo ha trovato il collaudo della 42a**, e sono due righe
consecutive del log:

    [18:20] Vuoi lasciare Your Home?
            You left Casa tua.

La prima legge `mdatan(MDATAN_NAME)`, la seconda `mapname()`. `mapname()` e' la
tabella di `text.hsp`, calcolata a ogni chiamata e gia' tradotta; `mdatan` e'
**serializzato nel salvataggio** — `module.hsp:4598` fa `noteadd mdatan(cnt)` e
`:4601` fa `noteget mdatan(cnt)`.

💡 **E il caso e' UNO SOLO.** `map.hsp:1400`-`:1402` dice che per ogni area
tranne `AREA_HOME` il nome viene riletto da `mapname()` a ogni
`*map_init_main`, quindi tutte le altre mappe si traducono da sole. Casa tua e'
l'unica che il giocatore puo' **rinominare**, e per questo ha una guardia che
non sovrascrive un nome scelto: scatta solo se il nome memorizzato e' `""`
oppure «North Tyris».

⚠️ **Senza questa toppa la traduzione funzionerebbe solo per le partite nuove.**
Un salvataggio che porta gia' «Your Home» memorizzato non e' ne' `""` ne' «North
Tyris»: la guardia non scatta, `:1397` non viene mai eseguita, e la casa resta
inglese **per sempre**. ✅ La toppa aggiunge un terzo caso alla guardia, e alla
prima visita il nome vecchio diventa «Casa tua».

💡 **`:1396` resta RINVIATA, ed e' quel che rende stabile questa toppa.** La riga
e' un confronto contro un valore serializzato — la regola che la rete 7 ha
imposto ai nove `CDATAN_NEWSEX` nella 41a — quindi il dizionario non la tocca e
la stringa cercata qui non cambia sotto i piedi.

⚠️ **Il letterale «Your Home» aggiunto sta fuori da `lang()` apposta**: non e'
testo da leggere, e' il valore inglese che il salvataggio porta scritto. Come i
nove del genere, non si traduce mai.

⚠️ Le toppe **non passano da `degrada()`**: la sostituzione non porta accenti.
E si compone e si valida tutto in memoria prima di aprire un file in scrittura.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())

from strumenti import percorsi  # noqa: E402

CERCA = ('\t\tif ( mdatan(MDATAN_NAME) == "" | mdatan(MDATAN_NAME) == '
         'lang("ノースティリス", "North Tyris") ) {')
SOSTITUISCI = ('\t\tif ( mdatan(MDATAN_NAME) == "" | mdatan(MDATAN_NAME) == '
               'lang("ノースティリス", "North Tyris") | mdatan(MDATAN_NAME) == "Your Home" ) {')

MOTIVO = (
    "map.hsp:1396. **Prima toppa di MIGRAZIONE del progetto**: non corregge un errore "
    "di monte, converte un dato vecchio gia' scritto nel salvataggio. `mdatan` e' "
    "serializzato (`module.hsp:4598` noteadd, `:4601` noteget), quindi un salvataggio "
    "creato prima della traduzione porta «Your Home» scritto dentro. La guardia di "
    ":1396 sovrascrive il nome della casa solo se e' `\"\"` o «North Tyris», quindi "
    "senza questa toppa :1397 non verrebbe mai eseguita e la casa resterebbe inglese "
    "per sempre: le partite nuove direbbero «Casa tua», quelle vecchie no. \u26a0\ufe0f Il "
    "difetto e' stato visto a schermo nel collaudo della 42a, due righe consecutive: "
    "«Vuoi lasciare Your Home?» (che legge mdatan) e «You left Casa tua.» (che legge "
    "mapname(), la tabella di text.hsp, gia' tradotta). 💡 Il caso e' uno solo: "
    "map.hsp:1400-1402 rilegge mdatan da mapname() per ogni area TRANNE AREA_HOME, "
    "che e' l'unica mappa rinominabile dal giocatore. 💡 :1396 resta rinviata (e' un "
    "confronto contro un valore serializzato, regola della rete 7), ed e' quel che "
    "rende stabile la stringa cercata. Il letterale «Your Home» aggiunto sta fuori da "
    "lang() apposta: non e' testo da leggere, e' il valore inglese memorizzato."
)


def riscrivi(percorso, righe_nuove) -> int:
    """Compone, valida e solo allora scrive: un errore non deve troncare il file."""
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    dati = ('\n'.join(righe) + '\n').encode('utf-8')
    with io.open(percorso, 'wb') as f:
        f.write(dati)
    return len(righe)


sorgente = io.open(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\map.hsp',
                   encoding='cp932').read()
if sorgente.count(CERCA) != 1:
    sys.exit(f'la riga cercata compare {sorgente.count(CERCA)} volte nel sorgente, non una')
SOSTITUISCI.encode('cp932')

toppe = percorsi.PROGETTO / 'toppe.jsonl'
if any(json.loads(r).get('cerca') == CERCA
       for r in io.open(toppe, encoding='utf-8').read().splitlines() if r.strip()):
    sys.exit('toppa gia\' presente')
print('toppe.jsonl:', riscrivi(toppe, [json.dumps(
    {'file': 'map.hsp', 'cerca': CERCA, 'sostituisci': SOSTITUISCI, 'motivo': MOTIVO},
    ensure_ascii=False)]), 'toppe')
