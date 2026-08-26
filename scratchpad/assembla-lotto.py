# -*- coding: utf-8 -*-
"""Assembla uno script di lotto copiando le reti VERBATIM dal modello.

Due modi di dichiarare la **zona**, e il modello e' lo stesso per tutt'e due:

    # per intervallo di righe (il modo storico, dalla 38a)
    python scratchpad/assembla-lotto.py 023 scratchpad/lotto-fase4-proc-022.py 24000 24999 <cartella>
    python scratchpad/assembla-lotto.py 001 scratchpad/lotto-fase4-proc-026.py 3000 3999 <cartella> chara_func.hsp

    # per INSIEME di righe (dalla 108a)
    python scratchpad/assembla-lotto.py 001 scratchpad/_102-rese-card-06.py <cartella> \\
        --righe <cartella>/righe001.py --hsp db_item.hsp --lavoro lavoro/_107-daitem.jsonl

⚠️ **Il sesto argomento e' il file `.hsp`**, e senza si intende `proc.hsp`. Serve
dalla 39ª, quando `proc.hsp` si e' chiuso e il lavoro e' passato a
`chara_func.hsp`: il blocco copiato dal modello porta **quattro** costanti che
parlano del file di partenza — `USCITA`, `SORGENTE`, il percorso
dell'estrazione e `DA, A` — e riscriverne a mano tre su quattro era il modo piu'
comodo di sbagliarne una. La convenzione dei nomi e' meccanica: il file
`nome.hsp` vuole l'estrazione in `lavoro/_nome.jsonl` e produce i lotti
`lavoro/fase4-nome-NNN.jsonl`.

⚠️⚠️ **Dalla 108a la convenzione meccanica non basta piu', e le eccezioni sono
esplicite invece che impossibili.** Tre cose che prima erano dedotte e adesso si
possono dichiarare:

  - `--lavoro`  il file di estrazione, quando non si chiama `lavoro/_<stem>.jsonl`
                (`db_card.hsp` legge `lavoro/_102-dacard.jsonl`, `db_item.hsp`
                legge `lavoro/_107-daitem.jsonl`: la convenzione era gia' rotta
                da sei sessioni, e i lotti si scrivevano a mano per questo);
  - `--fase`    il numero di fase nel nome del lotto; senza, si prende **quello
                del modello**, che e' il comportamento giusto per definizione —
                un lotto assemblato dal modello della fase 5 sta nella fase 5;
  - `--righe`   la zona per **insieme di righe** invece che per intervallo.

⚠️⚠️⚠️ **PERCHE' ESISTE `--righe`.** Le descrizioni di `db_item.hsp` (107a) non
sono un intervallo: quelle di una categoria sono sparse per novantamila righe —
i cinque cibi del primo dossier stanno a 42.785, 44.659, 44.731, 44.803 e
52.111. Il modello seleziona la zona con `DA <= riga <= A`, e su un intervallo
cosi' prenderebbe dentro mezzo file. Con `--righe` l'assemblatore riscrive
**due** righe del modello:

    DA, A = 2601, 3100                                 ->  RIGHE = {...}
    zona = [v for v in tutte if DA <= v['riga'] <= A]   ->  zona = [... if v['riga'] in RIGHE]

e le reti restano identiche carattere per carattere, che e' l'unica cosa che
questo script esiste per garantire. Il `RIGHE = {...}` lo emette
`scratchpad/_107-chiavi-item.py --solo-righe`: non si scrive a mano, cosi' il
lotto e il suo dossier non possono selezionare in modo diverso.

`<cartella>` contiene due file scritti a mano, piu' due facoltativi:

  - `testa023.py`  — la riga `# -*- coding: utf-8 -*-` e il docstring del lotto;
  - `rese023.py`   — gli `import`, il dizionario `RESE` e nient'altro;
  - `rinviate023.py` — **facoltativo**: la sola riga `RINVIATE = {...}`. Se
    manca, il lotto non rinvia niente, che e' il caso normale;
  - `righe023.py` — **facoltativo**, e si passa con `--righe`: il solo blocco
    `RIGHE = {...}`.

Il resto — le quattordici reti, la scrittura del JSONL — viene **copiato dal
modello**, e cambiano solo `USCITA`, la zona e, quando serve, `RINVIATE`.

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
modello, carattere per carattere, meno le righe che devono cambiare. Se non
coincide, esce con un errore e non lascia il file mezzo buono.

Usato tre volte nella 38ª (lotti 020, 021, 022), sempre con esito «reti
identiche».

💡 **Nota su un difetto del modello, ancora aperto**: se una resa manca, il
messaggio della rete 1 («voce senza resa») **non si vede mai**, perche' la rete 8
dereferenzia `RESE` prima del controllo di `errori` e quel che esce e' un
`KeyError` nudo. Capitato nella 38ª su `:23654`, la cui chiave finisce col punto
esclamativo. Vale la pena spostare il blocco `if errori:` subito dopo la rete 2.
"""
import argparse
import io
import os
import re
import sys

ANCORA = "# rete 5: l'accento"
ZONA_INTERVALLO = "zona = [v for v in tutte if DA <= v['riga'] <= A]"
ZONA_RIGHE = "zona = [v for v in tutte if v['riga'] in RIGHE]"


def leggi_argomenti(argv):
    """La forma storica a posizionali, piu' quella a opzioni della 108a.

    ⚠️ La forma vecchia — `numero modello da a cartella [hsp]` — resta valida
    tal quale: sta scritta nei documenti di sei sessioni, e un assemblatore che
    la rompe manda a riscrivere a mano i lotti, che e' il difetto che cura.
    """
    vecchia = (len(argv) in (5, 6)
               and argv[2].isdigit() and argv[3].isdigit())
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument('numero')
    ap.add_argument('modello')
    if vecchia:
        ap.add_argument('da', type=int)
        ap.add_argument('a', type=int)
    ap.add_argument('cartella')
    ap.add_argument('hsp', nargs='?', default='proc.hsp')
    ap.add_argument('--da', dest='da_opt', type=int)
    ap.add_argument('--a', dest='a_opt', type=int)
    ap.add_argument('--righe')
    ap.add_argument('--hsp', dest='hsp_opt')
    ap.add_argument('--lavoro')
    ap.add_argument('--fase', type=int)
    scelte = ap.parse_args(argv)
    if scelte.hsp_opt:
        scelte.hsp = scelte.hsp_opt
    if not vecchia:
        scelte.da = scelte.da_opt
        scelte.a = scelte.a_opt
    if scelte.righe is None and (scelte.da is None or scelte.a is None):
        sys.exit('serve una zona: `da a` posizionali, oppure --da/--a, oppure --righe')
    if scelte.righe is not None and scelte.da is not None:
        sys.exit('la zona si dichiara in UN modo solo: --righe oppure --da/--a')
    return scelte


def spoglia(testo: str) -> str:
    """Il blocco delle reti senza le righe che possono cambiare."""
    senza = re.sub(r'(USCITA = .*|DA, A = .*|SORGENTE = .*|.*lavoro/_[A-Za-z0-9_-]+\.jsonl.*)',
                   '', testo[testo.index(ANCORA):])
    senza = re.sub(r'RIGHE = \{.*?\n\}', '', senza, flags=re.S)
    senza = senza.replace(ZONA_INTERVALLO, '').replace(ZONA_RIGHE, '')
    return re.sub(r'RINVIATE = (set\(\)|\{.*?\n?\})', '', senza, flags=re.S)


def main():
    scelte = leggi_argomenti(sys.argv[1:])
    numero, modello, cartella = scelte.numero, scelte.modello, scelte.cartella
    hsp = scelte.hsp
    stem = hsp[:-len('.hsp')] if hsp.endswith('.hsp') else hsp

    testa = io.open(os.path.join(cartella, f'testa{numero}.py'), encoding='utf-8').read()
    rese = io.open(os.path.join(cartella, f'rese{numero}.py'), encoding='utf-8').read()

    sorgente = io.open(modello, encoding='utf-8').read()
    if ANCORA not in sorgente:
        sys.exit(f'{modello} non contiene {ANCORA!r}: non e\' un modello di lotto')
    reti = sorgente[sorgente.index(ANCORA):]

    # ⚠️ La fase la decide il MODELLO, non una convenzione scritta qui: un lotto
    # assemblato dal modello della fase 5 sta nella fase 5. `--fase` la forza.
    trovata = re.search(r"USCITA = 'lavoro/fase(\d)-", reti)
    if trovata is None:
        sys.exit(f'{modello} non ha un USCITA della forma "lavoro/faseN-...": non e\' un modello')
    fase = scelte.fase if scelte.fase is not None else int(trovata.group(1))
    lavoro = scelte.lavoro or f'lavoro/_{stem}.jsonl'

    ancore = [
        (r"USCITA = 'lavoro/fase\d-[a-z_]+-\d+\.jsonl'",
         f"USCITA = 'lavoro/fase{fase}-{stem}-{numero}.jsonl'"),
        (r"SORGENTE = r'[^']*\\[a-z_]+\.hsp'",
         f"SORGENTE = r'C:\\\\Games\\\\Elona\\\\_traduzione\\\\sorgente\\\\2.05-custom-gx\\\\{hsp}'"),
        (r"io\.open\('lavoro/_[A-Za-z0-9_-]+\.jsonl'", f"io.open('{lavoro}'"),
    ]
    if scelte.righe is None:
        ancore.append((r'DA, A = \d+, \d+', f'DA, A = {scelte.da}, {scelte.a}'))
    else:
        dichiarate = io.open(scelte.righe, encoding='utf-8').read().strip()
        if not dichiarate.startswith('RIGHE = {'):
            sys.exit(f'{scelte.righe} deve cominciare con "RIGHE = {{"')
        ancore.append((r'DA, A = \d+, \d+', dichiarate))
        ancore.append((re.escape(ZONA_INTERVALLO), ZONA_RIGHE))
    for cerca, metti in ancore:
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

    uscita = f'scratchpad/lotto-fase{fase}-{stem}-{numero}.py'
    io.open(uscita, 'w', encoding='utf-8', newline='\n').write(testa + rese + reti)

    if spoglia(io.open(uscita, encoding='utf-8').read()) != spoglia(sorgente):
        sys.exit(f'⚠️ le reti di {uscita} NON sono identiche a quelle di {modello}')
    print(f'scritto {uscita} — reti identiche a {modello}')


if __name__ == '__main__':
    main()
