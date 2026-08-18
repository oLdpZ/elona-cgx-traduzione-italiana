# -*- coding: utf-8 -*-
"""Le tre righe inglesi NUDE di `map_user.hsp`, che nessuna `lang()` copre.

Chiuso il dizionario (203 rese su 204, una rinviata), `nudi_en.py` dice che nel
file restano **tre letterali inglesi nudi**, cioe' testo che il giocatore legge
e che nessun conteggio di «non tradotte» include. E' la domanda «finito per
quale referto?» applicata subito invece che due sessioni dopo.

    :2362  X's charisma increased. Potential: Y      mod ANNA
    :2389  X's negotiation increased. Potential: Y   mod ANNA
    :2565  Duplicate found for: ... X: ... Y: ...    mod BLOODYSHADE

## ⚠️ Le prime due portano dentro la scala dei potenziali, un'altra volta

`StatPotential` non e' un numero quando arriva al `txt`: le venti righe sopra lo
riscrivono con **una parola inglese** — `Superb`, `Great`, `Good`, `Bad`,
`Hopeless`. E' la stessa scala che il lotto 002 ha reso per `:365`-`:405`, e le
parole devono essere le stesse, o la stessa cosa avrebbe due nomi nello stesso
negozio: **Ottimo, Notevole, Buono, Scarso, Nullo**.
💡 E' la famiglia di `variabili_en.py` (terzo punto cieco, 38a), ma quel referto
non poteva vederla: guarda le variabili interpolate **dentro una `lang()`**, e
qui di `lang()` non ce n'e' nessuna.

⚠️ I due blocchi sono **identici carattere per carattere** tranne la prima riga
e l'ultima: una toppa su `StatPotential = "Superb"` aggancerebbe due posti e
`applica` si fermerebbe. Per questo il `cerca` e' il **blocco intero**, dalla
riga di `sgrowth` a quella di `txt`.

⚠️ E gli accenti nelle toppe non li degrada nessuno (`applica` degrada solo il
dizionario): «e' cresciuto» si scrive gia' degradato.
"""
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi

SORGENTE = percorsi.SORGENTE_HSP / 'map_user.hsp'
righe = SORGENTE.read_bytes().decode('cp932').splitlines()

SCALA = {
    '"Superb"': '"Ottimo"',
    '"Great"': '"Notevole"',
    '"Good"': '"Buono"',
    '"Bad"': '"Scarso"',
    '"Hopeless"': '"Nullo"',
}

BLOCCHI = [
    # (prima riga, ultima riga, la parte inglese del txt, la resa)
    (2338, 2362,
     "\"'s charisma increased. Potential: \"",
     '": il carisma e\' cresciuto. Potenziale: "'),
    (2365, 2389,
     "\"'s negotiation increased. Potential: \"",
     '": la trattativa e\' cresciuta. Potenziale: "'),
]

toppe = []
for da, a, vecchio_txt, nuovo_txt in BLOCCHI:
    cerca = righe[da - 1:a]
    if 'sgrowth' not in cerca[0] or 'txt ' not in cerca[-1]:
        sys.exit(f'rete 0: il blocco {da}-{a} non e\' quello atteso')
    if vecchio_txt not in cerca[-1]:
        sys.exit(f'rete 0: {a} non contiene {vecchio_txt!r}')
    sostituisci = []
    for r in cerca:
        for prima, dopo in SCALA.items():
            r = r.replace(prima, dopo)
        sostituisci.append(r.replace(vecchio_txt, nuovo_txt))
    if sostituisci == cerca:
        sys.exit(f'rete 1: il blocco {da}-{a} non e\' cambiato')
    # rete 2: il blocco deve agganciare una volta sola
    quante = sum(1 for i in range(len(righe) - len(cerca) + 1)
                 if righe[i:i + len(cerca)] == cerca)
    if quante != 1:
        sys.exit(f'rete 2: il blocco {da}-{a} aggancia {quante} volte, non una')
    toppe.append({
        'file': 'map_user.hsp',
        'cerca': cerca,
        'sostituisci': sostituisci,
        'motivo': (
            f"map_user.hsp:{a}, mod ANNA: un letterale inglese NUDO, senza "
            "`lang()`, che nessun conteggio di non tradotte include. Porta "
            "dentro `StatPotential`, che le venti righe sopra riscrivono con "
            "una PAROLA inglese della scala dei potenziali — le stesse cinque "
            "che il lotto fase4-map_user-002 ha reso per `:365`-`:405`, e qui "
            "vanno rese uguali o la stessa cosa avrebbe due nomi nello stesso "
            "negozio. Il `cerca` e' il blocco intero perche' i due blocchi "
            "(carisma e trattativa) sono identici tranne la prima riga e "
            "l'ultima. Trovata nella 60a da `nudi_en.py`, chiudendo il file."),
    })

# --- la terza: la diagnostica dei doppioni del museo
RIGA_DUP = 2565
cerca = righe[RIGA_DUP - 1]
if 'Duplicate found for: ' not in cerca:
    sys.exit(f'rete 0: {RIGA_DUP} non e\' la riga dei doppioni')
sostituisci = (cerca
               .replace('"Duplicate found for: "', '"Doppione trovato: "')
               .replace('" at "', '" in "')
               .replace('" and X: "', '" e X: "'))
if sostituisci == cerca:
    sys.exit('rete 1: la riga dei doppioni non e\' cambiata')
if sum(r == cerca for r in righe) != 1:
    sys.exit('rete 2: la riga dei doppioni non e\' unica')
toppe.append({
    'file': 'map_user.hsp',
    'cerca': cerca,
    'sostituisci': sostituisci,
    'motivo': (
        "map_user.hsp:2565, mod BLOODYSHADE: un letterale inglese nudo che il "
        "gioco stampa in giallo nel registro quando trova due copie della "
        "stessa carta nel museo. Ha l'aria di una riga di diagnostica — dice "
        "le coordinate X e Y — ma esce a schermo come le altre e chi cura un "
        "museo la legge davvero. Trovata nella 60a da `nudi_en.py`."),
})

uscita = 'scratchpad/_toppe-map_user-nudi.jsonl'
io.open(uscita, 'w', encoding='utf-8', newline='\n').write(
    ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe))
print(f'{len(toppe)} toppe scritte in {uscita}')
for t in toppe:
    ultima = t['sostituisci'][-1] if isinstance(t['sostituisci'], list) else t['sostituisci']
    print('   ', ultima.strip()[:110])
