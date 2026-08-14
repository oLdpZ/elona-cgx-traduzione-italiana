# -*- coding: utf-8 -*-
"""Assembla uno script di lotto copiando le reti VERBATIM dal modello.

    python scratchpad/assembla-lotto.py 023 scratchpad/lotto-fase4-proc-022.py 24000 24999 <cartella>

`<cartella>` contiene due file scritti a mano, piu' uno facoltativo:

  - `testa023.py`  — la riga `# -*- coding: utf-8 -*-` e il docstring del lotto;
  - `rese023.py`   — gli `import`, il dizionario `RESE` e nient'altro;
  - `rinviate023.py` — **facoltativo**: la sola riga `RINVIATE = {...}`. Se
    manca, il lotto non rinvia niente, che e' il caso normale.

Il resto — le quattordici reti, la scrittura del JSONL — viene **copiato dal
modello**, e cambiano solo `USCITA`, `DA, A` e, quando serve, `RINVIATE`.

⚠️ **`RINVIATE` e' nato come terza ancora nella 39ª**, quando `proc.hsp:24107`
ha chiesto una toppa: il blocco copiato dal modello porta `RINVIATE = set()`, e
senza questa ancora l'unico modo di dichiarare una rinviata era **modificare a
mano il file generato**, cioe' esattamente la cosa che questo script esiste per
impedire.

⚠️ **Perche' esiste.** `RIPRESA-sessione.md` ripete da cinque sessioni «si copia
il file, non si riscrive a memoria», perche' le reti 3, 4 e 8 sono state
corrette **perche' sbagliavano loro** e riscriverle a memoria le riporterebbe
indietro. Questo script rende la regola meccanica invece che diligente: alla
fine **rilegge quel che ha scritto** e confronta il blocco delle reti col
modello, carattere per carattere, meno le due righe che devono cambiare. Se non
coincide, esce con un errore e non lascia il file mezzo buono.

Usato tre volte nella 38ª (lotti 020, 021, 022), sempre con esito «reti
identiche».

💡 **Nota su un difetto del modello, ancora aperto**: se una resa manca, il
messaggio della rete 1 («voce senza resa») **non si vede mai**, perche' la rete 8
dereferenzia `RESE` prima del controllo di `errori` e quel che esce e' un
`KeyError` nudo. Capitato nella 38ª su `:23654`, la cui chiave finisce col punto
esclamativo. Vale la pena spostare il blocco `if errori:` subito dopo la rete 2.
"""
import io
import os
import re
import sys

if len(sys.argv) != 6:
    sys.exit(__doc__)

numero, modello, da, a, cartella = sys.argv[1:6]

testa = io.open(os.path.join(cartella, f'testa{numero}.py'), encoding='utf-8').read()
rese = io.open(os.path.join(cartella, f'rese{numero}.py'), encoding='utf-8').read()

sorgente = io.open(modello, encoding='utf-8').read()
ANCORA = "# rete 5: l'accento"
if ANCORA not in sorgente:
    sys.exit(f'{modello} non contiene {ANCORA!r}: non e\' un modello di lotto')
reti = sorgente[sorgente.index(ANCORA):]

reti, quante_uscita = re.subn(r"USCITA = 'lavoro/fase4-proc-\d+\.jsonl'",
                              f"USCITA = 'lavoro/fase4-proc-{numero}.jsonl'", reti)
reti, quante_zona = re.subn(r'DA, A = \d+, \d+', f'DA, A = {da}, {a}', reti)
if quante_uscita != 1 or quante_zona != 1:
    sys.exit(f'ancore non trovate una volta sola: USCITA {quante_uscita}, DA/A {quante_zona}')

percorso_rinviate = os.path.join(cartella, f'rinviate{numero}.py')
if os.path.exists(percorso_rinviate):
    dichiarate = io.open(percorso_rinviate, encoding='utf-8').read().strip()
    if not dichiarate.startswith('RINVIATE = '):
        sys.exit(f'{percorso_rinviate} deve cominciare con "RINVIATE = "')
    reti, quante_rinviate = re.subn(r'RINVIATE = set\(\)', lambda _: dichiarate, reti)
    if quante_rinviate != 1:
        sys.exit(f'ancora RINVIATE trovata {quante_rinviate} volte, non una')

uscita = f'scratchpad/lotto-fase4-proc-{numero}.py'
io.open(uscita, 'w', encoding='utf-8', newline='\n').write(testa + rese + reti)


def spoglia(testo: str) -> str:
    """Il blocco delle reti senza le tre righe che possono cambiare."""
    senza = re.sub(r'(USCITA = .*|DA, A = .*)', '', testo[testo.index(ANCORA):])
    return re.sub(r'RINVIATE = (set\(\)|\{.*?\n?\})', '', senza, flags=re.S)


if spoglia(io.open(uscita, encoding='utf-8').read()) != spoglia(sorgente):
    sys.exit(f'⚠️ le reti di {uscita} NON sono identiche a quelle di {modello}')
print(f'scritto {uscita} — reti identiche a {modello}')
