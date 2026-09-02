# -*- coding: utf-8 -*-
"""Il terzo lotto della 128a: una sola riga, e la traduzione l'aveva rotta.

⚠️⚠️⚠️ **`text.hsp:362` NON E' TESTO: E' UN OPERANDO, E IL DIZIONARIO L'HA
TRADOTTO LO STESSO** — non per una svista di chi ha reso la voce, ma perche' in
`text.hsp` il letterale `lang("なし", "none")` compare **due volte**, e le due
occorrenze non sono la stessa cosa:

    text.hsp:49    _dengon = lang("なし", "none"), lang("協調", "Cooperation"), …
                   la prima voce dell'elenco dei tipi di messaggio, che il
                   giocatore LEGGE: «Nessuna» e' giusto

    text.hsp:362   if ( cdatan(CDATAN_NEWSEX, tc) == lang("なし", "none") ) {
                   il confronto dentro *txttargetsex, che decide come si scrive
                   il sesso di chi si guarda: e' un OPERANDO

Il dizionario e' indicizzato per **contenuto**, non per riga: una voce sola,
`firma 2007e5b7`, e `applica` la sostituisce ovunque quel letterale compaia nel
file. Quindi rendere la voce dell'elenco ha tradotto anche il confronto.

⚠️⚠️ **E il confronto e' morto**, perche' chi ASSEGNA sta in altri file e non e'
tradotto: `chara.hsp:4390` e `item.hsp:4181` scrivono `lang("なし", "none")`, e
il valore memorizzato resta «none». A schermo: guardando un personaggio che si
dichiara di sesso «nessuno», `*txttargetsex` non entra in nessuno dei sei rami
e **`s` resta quel che era prima**, cioe' una parola di un'altra frase.

✅ La toppa **allarga il confronto**, esattamente come la migrazione di «Your
Home»: la `lang()` non si tocca — il dizionario ci mettera' «Nessuna» come deve
— e accanto si aggiunge, **fuori** da `lang()`, il confronto contro il valore
che davvero sta scritto in memoria, «none». L'elenco di `:49` resta «Nessuna» e
il ramo torna vivo.

⚠️⚠️ **E la toppa e' dichiarata `prima`, e non poteva essere altrimenti.** Una
toppa normale gira DOPO il dizionario, ma il contratto del progetto
(`test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato`) pretende che la
riga cercata esista nel **sorgente pinnato**. Le due cose stanno insieme solo
finche' la riga e' inglese nuda, cioe' finche' il dizionario non la tocca —
e questa la tocca. La prima stesura di questa toppa cercava la riga della build
(«Nessuna») ed e' stata **respinta da quel test**: l'invariante ha fatto quel
che doveva. ⓘ `prima` e' ammessa qui perche' i letterali dentro `lang()` non
cambiano, che e' l'unica cosa che la guardia di `prima` pretende
(`applica.letterali_di_lang`).

⭐ Trovata da `scratchpad/_128-confronti-contro-un-nome-assegnato.py`, il referto
scritto un'ora prima per un'altra famiglia: cercava i nomi di mappa e ha trovato
anche questa.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\text.hsp'
righe = io.open(SORGENTE, encoding='cp932').read().split('\n')

CERCA = '\tif ( cdatan(CDATAN_NEWSEX, tc) == lang("なし", "none") ) {'
SOSTITUISCI = ('\tif ( cdatan(CDATAN_NEWSEX, tc) == lang("なし", "none")'
               ' | cdatan(CDATAN_NEWSEX, tc) == "none" ) {')

quante = sum(1 for r in righe if r == CERCA)
if quante != 1:
    raise SystemExit('text.hsp: la riga cercata compare {} volte'.format(quante))
if sum(1 for r in righe if '_dengon = lang("なし", "none")' in r) != 1:
    raise SystemExit('text.hsp:49 non e\' piu\' la voce dell\'elenco: la premessa e\' cambiata')

toppa = {
    'file': 'text.hsp',
    'cerca': CERCA,
    'sostituisci': SOSTITUISCI,
    'prima': True,
    'motivo': (
        "⚠️⚠️⚠️ OPERANDO TRADOTTO PER COLLISIONE DENTRO UN FILE SOLO, e il ramo "
        "e' morto. `text.hsp:*txttargetsex` (:362) confronta "
        "`cdatan(CDATAN_NEWSEX, tc)` con `lang(\"なし\", \"none\")` per scegliere "
        "come scrivere il sesso di chi si guarda; chi ASSEGNA quel valore sta in "
        "altri file e non e' tradotto (`chara.hsp:4390`, `item.hsp:4181` scrivono "
        "«none»), quindi il confronto contro «Nessuna» non e' mai vero e `s` resta "
        "la stringa della frase precedente. "
        "⚠️ Non e' una svista di chi ha reso la voce: in `text.hsp` il letterale "
        "`lang(\"なし\", \"none\")` compare DUE volte — `:49`, la prima voce "
        "dell'elenco `_dengon` dei tipi di messaggio, che il giocatore LEGGE e "
        "dove «Nessuna» e' giusto, e `:362`, l'operando — e il dizionario e' "
        "indicizzato per CONTENUTO, non per riga: una firma sola (2007e5b7) e "
        "`applica` la sostituisce in tutt'e due. "
        "✅ La toppa ALLARGA il confronto nella forma della migrazione di «Your "
        "Home» (toppa di map.hsp:1396): la `lang()` non si tocca — il dizionario "
        "ci mettera' «Nessuna» come deve, e `:49` resta giusto — e accanto si "
        "aggiunge FUORI da lang() il confronto contro il valore che davvero sta "
        "in memoria, «none». "
        "⚠️⚠️ DICHIARATA `prima`, e non poteva essere altrimenti: una toppa "
        "normale gira dopo il dizionario, ma il contratto del progetto "
        "(`test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato`) pretende "
        "che la riga cercata esista nel SORGENTE PINNATO, e le due cose stanno "
        "insieme solo finche' il dizionario non tocca quella riga — qui la tocca. "
        "La prima stesura cercava la riga della build («Nessuna») ed e' stata "
        "RESPINTA da quel test. ⓘ `prima` e' ammessa perche' i letterali dentro "
        "`lang()` non cambiano, che e' l'unica cosa che la sua guardia pretende "
        "(`applica.letterali_di_lang`). "
        "⭐ Trovata da `scratchpad/_128-confronti-contro-un-nome-assegnato.py`, "
        "scritto per la famiglia dei nomi di mappa e che ha trovato anche questa."
    ),
}

dati = (json.dumps(toppa, ensure_ascii=False) + '\n').encode('utf-8')
with io.open('lavoro/toppe-128-none.jsonl', 'wb') as f:
    f.write(dati)
print('1 toppa -> lavoro/toppe-128-none.jsonl')
print('  ', SOSTITUISCI.strip())
