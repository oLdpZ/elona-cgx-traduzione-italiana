# -*- coding: utf-8 -*-
"""Assembla uno script di lotto copiando le reti VERBATIM dal modello.

    python scratchpad/assembla-lotto.py 023 scratchpad/lotto-fase4-proc-022.py 24000 24999 <cartella>
    python scratchpad/assembla-lotto.py 001 scratchpad/lotto-fase4-proc-026.py 3000 3999 <cartella> chara_func.hsp

⚠️ **Il sesto argomento e' il file `.hsp`**, e senza si intende `proc.hsp`. Serve
dalla 39ª, quando `proc.hsp` si e' chiuso e il lavoro e' passato a
`chara_func.hsp`: il blocco copiato dal modello porta **quattro** costanti che
parlano del file di partenza — `USCITA`, `SORGENTE`, il percorso
dell'estrazione e `DA, A` — e riscriverne a mano tre su quattro era il modo piu'
comodo di sbagliarne una. La convenzione dei nomi e' meccanica: il file
`nome.hsp` vuole l'estrazione in `lavoro/_nome.jsonl` e produce i lotti
`lavoro/fase4-nome-NNN.jsonl`.

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

if len(sys.argv) not in (6, 7):
    sys.exit(__doc__)

numero, modello, da, a, cartella = sys.argv[1:6]
hsp = sys.argv[6] if len(sys.argv) == 7 else 'proc.hsp'
stem = hsp[:-len('.hsp')] if hsp.endswith('.hsp') else hsp

testa = io.open(os.path.join(cartella, f'testa{numero}.py'), encoding='utf-8').read()
rese = io.open(os.path.join(cartella, f'rese{numero}.py'), encoding='utf-8').read()

sorgente = io.open(modello, encoding='utf-8').read()
ANCORA = "# rete 5: l'accento"
if ANCORA not in sorgente:
    sys.exit(f'{modello} non contiene {ANCORA!r}: non e\' un modello di lotto')
reti = sorgente[sorgente.index(ANCORA):]

ANCORE = [
    (r"USCITA = 'lavoro/fase4-[a-z_]+-\d+\.jsonl'",
     f"USCITA = 'lavoro/fase4-{stem}-{numero}.jsonl'"),
    (r'DA, A = \d+, \d+', f'DA, A = {da}, {a}'),
    (r"SORGENTE = r'[^']*\\[a-z_]+\.hsp'",
     f"SORGENTE = r'C:\\\\Games\\\\Elona\\\\_traduzione\\\\sorgente\\\\2.05-custom-gx\\\\{hsp}'"),
    (r"io\.open\('lavoro/_[a-z_]+\.jsonl'",
     f"io.open('lavoro/_{stem}.jsonl'"),
]
for cerca, metti in ANCORE:
    reti, quante = re.subn(cerca, lambda _, m=metti: m, reti)
    if quante != 1:
        sys.exit(f'ancora {cerca!r} trovata {quante} volte, non una')

percorso_rinviate = os.path.join(cartella, f'rinviate{numero}.py')
if os.path.exists(percorso_rinviate):
    dichiarate = io.open(percorso_rinviate, encoding='utf-8').read().strip()
    if not dichiarate.startswith('RINVIATE = '):
        sys.exit(f'{percorso_rinviate} deve cominciare con "RINVIATE = "')
    reti, quante_rinviate = re.subn(r'RINVIATE = set\(\)', lambda _: dichiarate, reti)
    if quante_rinviate != 1:
        sys.exit(f'ancora RINVIATE trovata {quante_rinviate} volte, non una')

uscita = f'scratchpad/lotto-fase4-{stem}-{numero}.py'
io.open(uscita, 'w', encoding='utf-8', newline='\n').write(testa + rese + reti)


def spoglia(testo: str) -> str:
    """Il blocco delle reti senza le righe che possono cambiare."""
    senza = re.sub(r'(USCITA = .*|DA, A = .*|SORGENTE = .*|.*lavoro/_[a-z_]+\.jsonl.*)',
                   '', testo[testo.index(ANCORA):])
    return re.sub(r'RINVIATE = (set\(\)|\{.*?\n?\})', '', senza, flags=re.S)


if spoglia(io.open(uscita, encoding='utf-8').read()) != spoglia(sorgente):
    sys.exit(f'⚠️ le reti di {uscita} NON sono identiche a quelle di {modello}')
print(f'scritto {uscita} — reti identiche a {modello}')
