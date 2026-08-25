# -*- coding: utf-8 -*-
"""97a - Disfa la resa di `map.hsp:1396` e la rinvia, come la 42a aveva deciso.

⚠️⚠️⚠️ **ERRORE MIO, TROVATO DA `applica` CHE SI E' RIFIUTATO DI ANDARE
AVANTI.** Ho reso `map.hsp:1396` con «Tyris del Nord», convinto di riparare un
difetto vivo: `mapname()` per la mappa del mondo passa da `text.hsp:2737`, che e'
gia' reso, quindi il confronto contro «North Tyris» non riesce mai e la casa del
giocatore resta col nome sbagliato.

Il difetto e' vero, **ma era gia' riparato dalla 42a**, e non con una resa: con
la **prima toppa di migrazione del progetto**. `mdatan` e' serializzato
(`module.hsp:4598` `noteadd`, `:4601` `noteget`), quindi un salvataggio nato
prima della traduzione porta dentro «Your Home» in inglese, e la toppa aggiunge
un terzo operando alla guardia per riconoscerlo. Il motivo della toppa lo dice
in una riga: **«:1396 resta rinviata (e' un confronto contro un valore
serializzato, regola della rete 7), ed e' quel che rende stabile la stringa
cercata.»**

Traducendola ho spostato la riga sotto i piedi della sua toppa, e `applica` ha
detto «la riga della toppa … non esiste piu'» ed e' uscito con **1**.

⭐⭐⭐ LA LEZIONE, ED E' QUELLA DELLA 96a VISTA DALL'ALTRO LATO. La 96a aveva
imparato che **l'ancora di una toppa non va dove arriva la lingua**: una toppa
agganciata a una `lang()` esplode il giorno che qualcuno la traduce. Qui la toppa
e' agganciata a una `lang()` per forza — e' proprio quella riga che deve
cambiare — e la difesa scelta allora era **rinviare la riga**, cioe' promettere
che nessuno l'avrebbe tradotta. Io quella promessa non l'ho vista, perche' non
l'ho cercata: prima di rendere una riga non guardavo `toppe.jsonl`.

⭐ E si e' vista solo perche' `applica` **e' uscito con 1 e ho cercato il segnale
di guasto** invece di guardare la coda dell'output: `compila --eseguibile` ha
prodotto lo stesso un eseguibile, dal solito albero incompleto. E' esattamente
la forma del guasto della 96a, e stavolta la rete l'ha presa.

💡 Il seguito e' `scratchpad/_97-toppe-sotto.py`, la guardia che manca.
"""
import io
import json

FILE = 'map.hsp'
RIGA, EN = 1396, 'North Tyris'

MOTIVO = (
    "⚠️ **E' l'operando di un confronto contro un valore serializzato**, e la "
    "riga la governa una toppa. `map.hsp:1396` chiede se il nome della mappa "
    "sia vuoto o «North Tyris» per poterlo sostituire con «Casa tua» "
    "(`:1397`); `mdatan` finisce nel salvataggio (`module.hsp:4598` `noteadd`, "
    "`:4601` `noteget`), quindi una partita nata prima della traduzione porta "
    "dentro la stringa **inglese**. La **prima toppa di migrazione del "
    "progetto** (42a) aggiunge per questo un terzo operando, "
    "`| mdatan(MDATAN_NAME) == \"Your Home\"`, e il suo `cerca` e' la riga "
    "intera: tradurre la `lang()` la fa sparire e `applica` si ferma. "
    "⚠️ **La 97a l'ha tradotta davvero** — «Tyris del Nord», per riparare un "
    "difetto che era gia' riparato — e `applica` e' uscito con 1. La resa e' "
    "stata disfatta e la riga rinviata, che e' quel che la 42a aveva deciso e "
    "scritto nel motivo della toppa. "
    "✅ Si sblocca solo insieme alla toppa: se un giorno quella riga si tocca, "
    "si toccano tutt'e due nello stesso momento."
)

percorso = 'dizionario/map.hsp.jsonl'
tenute, tolte = [], []
for l in io.open(percorso, encoding='utf-8'):
    if not l.strip():
        continue
    v = json.loads(l)
    if v['riga'] == RIGA and v['en'] == EN:
        tolte.append(v)
    else:
        tenute.append(l)
if len(tolte) != 1:
    raise SystemExit(f'attese 1 voce da togliere, trovate {len(tolte)}: non tocco niente')
print(f'tolta dal dizionario: :{RIGA} en={EN!r} it={tolte[0]["it"]!r}')

esistenti = [l for l in io.open('rinviate.jsonl', encoding='utf-8') if l.strip()]
if any(json.loads(l)['firma'] == tolte[0]['firma'] for l in esistenti):
    raise SystemExit('gia rinviata: tolgo solo dal dizionario')

nuova = {
    'firma': tolte[0]['firma'],
    'file': FILE,
    'en': EN,
    'rinviata_a': 'mai da sola: e\' l\'ancora della toppa di migrazione della 42a, '
                  'e un operando contro un valore serializzato',
    'motivo': MOTIVO,
}

# ⚠️ si compone e si codifica prima di toccare i file (la 39a)
dati_dizionario = ''.join(tenute).encode('utf-8')
dati_rinviate = (json.dumps(nuova, ensure_ascii=False) + '\n').encode('utf-8')
with io.open(percorso, 'wb') as f:
    f.write(dati_dizionario)
with io.open('rinviate.jsonl', 'ab') as f:
    f.write(dati_rinviate)
print(f'dizionario: {len(tenute)} voci restano')
print(f'rinviate.jsonl: {len(esistenti) + 1} righe')
