# -*- coding: utf-8 -*-
"""Il rinvio e la toppa di `map_user.hsp:730`: l'inglese nomina la cosa sbagliata.

    :718  txt lang(mdatan(MDATAN_NAME) + "を何と呼ぶ？ ",
                   "What do you want to call " + mdatan(MDATAN_NAME) + "? ")
    :729  mdatan(MDATAN_NAME) = "" + inputlog
    :730  txt lang("" + mdatan(MDATAN_NAME) + "という名前で呼ぶことにした。",
                   "You named " + him(tc) + " " + cdatan(CDATAN_NAME, tc) + ".")

La riga sopra chiede il nome della **proprieta'**, quella in mezzo lo scrive in
`mdatan(MDATAN_NAME)`, e la conferma inglese nomina un **personaggio** con
`cdatan(CDATAN_NAME, tc)` — che qui non e' stato nemmeno impostato. E' la riga
della finestra che da' il nome a un compagno, copiata dentro un'altra finestra:
e' la famiglia della 58a (`main.hsp:5684`), e la prova sta nelle due righe
intorno.

⚠️ **Perche' una toppa e non una resa.** La rete 11 pretende che le funzioni di
contenuto della resa siano **quelle dell'inglese**, e l'inglese ha `cdatan`.
Scrivere `mdatan` sarebbe aggiungere una funzione che l'inglese non ha, che e'
proprio quel che la rete esiste per impedire; scrivere `cdatan` sarebbe copiare
il difetto a schermo. Stessa uscita di `action.hsp:4584` e `:9631`: la `lang()`
si **rinvia**, cosi' sorgente e build coincidono, e la riga diventa toppabile.

⚠️ Il `cerca` di una toppa e' fatto di righe intere del sorgente **pinnato** e
va letto con `.splitlines()`, o il `\\r` del CRLF resta in coda e non aggancia.
⚠️ E gli accenti nelle toppe non li degrada nessuno: qui non ce ne sono.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi

RIGA = 730
SORGENTE = percorsi.SORGENTE_HSP / 'map_user.hsp'

righe = SORGENTE.read_bytes().decode('cp932').splitlines()
cerca = righe[RIGA - 1]
if 'You named ' not in cerca or 'cdatan(CDATAN_NAME, tc)' not in cerca:
    sys.exit(f'rete 0: {SORGENTE.name}:{RIGA} non e\' la riga attesa: {cerca!r}')
if sum(r == cerca for r in righe) != 1:
    sys.exit(f'rete 1: il blocco non e\' unico nel file')

sostituisci = cerca.replace(
    '"You named " + him(tc) + " " + cdatan(CDATAN_NAME, tc) + "."',
    '"Adesso si chiama " + mdatan(MDATAN_NAME) + "."')
if sostituisci == cerca:
    sys.exit('rete 2: la sostituzione non ha cambiato niente')

toppa = {
    'file': 'map_user.hsp',
    'cerca': cerca,
    'sostituisci': sostituisci,
    'motivo': (
        "L'inglese di monte porta la riga di un'altra finestra: `:730` conferma "
        "il nome dato alla PROPRIETA' (che `:729` ha appena scritto in "
        "`mdatan(MDATAN_NAME)`), e la stringa inglese nomina un PERSONAGGIO con "
        "`cdatan(CDATAN_NAME, tc)`, che in questo punto non e' impostato. Il "
        "giapponese interpola `mdatan`, cioe' la cosa giusta. Non e' rendibile "
        "dal dizionario: la rete 11 pretende le funzioni di contenuto "
        "dell'inglese, e usare `mdatan` vorrebbe dire aggiungerne una che "
        "l'inglese non ha. La `lang()` e' rinviata e la riga toppata. "
        "Trovata nella 60a aprendo `map_user.hsp`."),
}

rinvio = {
    'firma': None,  # riempito sotto dal dizionario di lavoro
    'file': 'map_user.hsp',
    'en': '"You named " + him(tc) + " " + cdatan(CDATAN_NAME, tc) + "."',
    'rinviata_a': 'nessuna fase: risolta da toppa',
    'motivo': toppa['motivo'],
}

# la firma la da' l'estrazione, che e' l'unica scansione del progetto
for l in io.open('lavoro/_map_user.jsonl', encoding='utf-8'):
    v = json.loads(l)
    if v['riga'] == RIGA:
        rinvio['firma'] = v['firma']
if rinvio['firma'] is None:
    sys.exit(f'rete 3: nessuna voce a riga {RIGA} nell\'estrazione')

io.open('scratchpad/_toppa-map_user-730.jsonl', 'w', encoding='utf-8', newline='\n').write(
    json.dumps(toppa, ensure_ascii=False) + '\n')

esistenti = [json.loads(l) for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
if any(r['firma'] == rinvio['firma'] for r in esistenti):
    print('la rinviata c\'e\' gia\'')
else:
    dati = ''.join(json.dumps(r, ensure_ascii=False) + '\n'
                   for r in esistenti + [rinvio]).encode('utf-8')
    with io.open('rinviate.jsonl', 'wb') as f:
        f.write(dati)
    print(f'rinviate.jsonl: {len(esistenti) + 1} voci')

print('toppa scritta in scratchpad/_toppa-map_user-730.jsonl')
print('  cerca      ', cerca.strip()[:100])
print('  sostituisci', sostituisci.strip()[:100])
