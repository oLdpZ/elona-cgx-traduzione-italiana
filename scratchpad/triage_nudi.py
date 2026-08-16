# -*- coding: utf-8 -*-
"""Il triage del quinto punto cieco: le righe nude, spaccate per classe e per ROUTINE.

`nudi_en.py` (49ª) conta i letterali inglesi che non passano da nessuna `lang()`:
913 di struttura, e dopo le sei toppe dell'inventario **866 ancora da fare**. Ma
866 e' un numero grezzo, e la 49ª chiudeva chiedendo proprio questo: spaccarlo in
*testo che il giocatore legge* e *dato*.

⚠️ **Le tre classi che non sono testo stanno nella FORMA, non in un elenco a
mano.** E' la stessa scelta di `nudi_en.py` con `listn(0,)`/`listn(1,)`: un
elenco scritto a mano invecchia in silenzio e dipende da chi si ricorda della
pagina in cui e' scritto.

    spenta   la riga sta dentro un `/* ... */` (riusa `commenti-blocco.py`).
    dbg      la routine che la contiene si chiama `dbg_*`. E' la console di
             debug di `system.hsp`, che risponde solo in modo mago.
    sigla    ogni letterale della riga e' un identificatore camelCase in un
             pezzo solo (`mcTown1`, `mcBoss2`): un nome di traccia o di risorsa,
             non una frase. Sono i titoli del jukebox.
    testo    tutto il resto.

⚠️⚠️ **Il nome della routine NON basta come prova, e la regola `dbg_` e' un
prefisso apposta.** `command.hsp:*dump_chara` sembra roba da sviluppatore e
invece contiene «superb», «great», «good», «bad», «hopeless», cioe' gli aggettivi
di rango che il giocatore legge. E' la lezione n. 2 della 49ª — «i nomi del
decompilatore non sono un'autorita'» — applicata prima di sbagliare, non dopo:
un `dbg_` iniziale e' una convenzione di scrittura, «contiene dump» e' una
sensazione.

💡 Il conto per routine e' la parte che serve a lavorare: le righe nude non sono
sparse, stanno **in blocchi**, e un blocco e' una schermata sola. Le prime cinque
routine da sole fanno piu' di un terzo del testo.

    python scratchpad/triage_nudi.py                 # il referto
    python scratchpad/triage_nudi.py --elenco sigla  # le righe di una classe
    python scratchpad/triage_nudi.py --routine com_journal
"""
import collections
import glob
import importlib.util
import io
import os
import re
import sys

_QUI = os.path.dirname(os.path.abspath(__file__))


def _carica(nome: str, percorso: str):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


nu = _carica('nudi_en', os.path.join(_QUI, 'nudi_en.py'))
cb = _carica('commenti_blocco', os.path.join(_QUI, 'commenti-blocco.py'))

# `*etichetta` oppure `#deffunc nome ...`: il nome e' SEMPRE il primo token dopo
# la parola chiave. ⚠️ Scritto `#def(?:c)?func\s+(?:\w+\s+)?(\w+)` il gruppo
# facoltativo si mangia il nome e restituisce il TIPO del primo argomento: mezzo
# `tcg.hsp` risultava dentro una routine che si chiama «int».
_ETICHETTA = re.compile(r'^\*(\w+)|^#def(?:c)?func\s+(\w+)')
# Un identificatore in un pezzo solo: minuscola in testa, almeno una maiuscola
# dentro, niente spazi. ⚠️ La minuscola in testa e' quello che salva «Silenced»,
# «Confused», «First Strike» del gioco di carte, che sono parole vere.
_SIGLA = re.compile(r'^[a-z]+[A-Z][A-Za-z0-9]*$')

CLASSI = ('testo', 'sigla', 'dbg', 'spenta')


def etichette(righe: list) -> list:
    """Per ogni riga, il nome della routine che la contiene."""
    fuori = []
    corrente = '(nessuna)'
    for riga in righe:
        m = _ETICHETTA.match(riga.strip())
        if m:
            corrente = m.group(1) or m.group(2)
        fuori.append(corrente)
    return fuori


def classifica(nome_file: str) -> list:
    """(riga, classe, routine, testo) per ogni riga nuda ancora INTATTA nella build."""
    percorso = os.path.join(nu.SORGENTE, nome_file)
    sorg = io.open(percorso, encoding='cp932').read().split('\n')
    percorso_build = os.path.join(nu.BUILD, nome_file)
    build = (io.open(percorso_build, encoding='cp932').read().split('\n')
             if os.path.exists(percorso_build) else sorg)
    indici = nu.righe_nude(sorg)
    if not indici:
        return []
    # ⚠️ Stessa cautela di `nudi_en.py`: se la build ha piu' righe del sorgente
    #    l'allineamento per indice non vale e si confronta per contenuto.
    if len(build) == len(sorg):
        intatte = [i for i in indici if build[i] == sorg[i]]
    else:
        insieme = set(build)
        intatte = [i for i in indici if sorg[i] in insieme]
    if not intatte:
        return []

    spente = cb.righe_in_commento(percorso)
    eti = etichette(sorg)
    fuori = []
    for i in intatte:
        letterali = [x for x in nu._LETTERALE.findall(sorg[i]) if nu._e_testo(x)]
        if (i + 1) in spente:
            classe = 'spenta'
        elif eti[i].startswith('dbg_'):
            classe = 'dbg'
        elif letterali and all(_SIGLA.match(x.strip()) for x in letterali):
            classe = 'sigla'
        else:
            classe = 'testo'
        fuori.append((i + 1, classe, eti[i], sorg[i].strip()))
    return fuori


def main(argv: list) -> None:
    elenco = None
    routine = None
    if '--elenco' in argv:
        elenco = argv[argv.index('--elenco') + 1]
    if '--routine' in argv:
        routine = argv[argv.index('--routine') + 1]

    tutto = []
    for percorso in sorted(glob.glob(nu.SORGENTE + r'\*.hsp')):
        nome = os.path.basename(percorso)
        for riga, classe, eti, testo in classifica(nome):
            tutto.append((nome, riga, classe, eti, testo))

    if elenco or routine:
        scelte = [t for t in tutto
                  if (not elenco or t[2] == elenco) and (not routine or t[3] == routine)]
        for nome, riga, classe, eti, testo in scelte:
            print('%-20s %6d  %-8s %-26s %s' % (nome, riga, classe, eti, testo[:110]))
        print('--- %d righe' % len(scelte))
        return

    per_classe = collections.Counter(t[2] for t in tutto)
    print('=== le %d righe nude ancora da fare, per classe' % len(tutto))
    for classe in CLASSI:
        print('  %-8s %4d' % (classe, per_classe[classe]))

    testo = [t for t in tutto if t[2] == 'testo']
    per_routine = collections.Counter((t[0], t[3]) for t in testo)
    print()
    print('=== il TESTO, per routine: dove si lavora (%d righe in %d routine)'
          % (len(testo), len(per_routine)))
    for (nome, eti), quante in per_routine.most_common(30):
        print('  %4d  %-22s %s' % (quante, nome, eti))
    coda = sum(q for (_, _), q in per_routine.most_common()[30:])
    if coda:
        print('  %4d  (altre %d routine)' % (coda, len(per_routine) - 30))

    # ⚠️ Una toppa si aggancia al TESTO della riga e pretende che sia unica nel
    #    file: `applica_toppe` si ferma se il blocco compare due volte. Queste
    #    schermate ripetono le stesse righe a decine («Press F1 to show help.»,
    #    «Return to the previous menu.»), quindi il conto delle righe ambigue
    #    dice in anticipo quanta parte del lavoro vuole un blocco di piu' righe
    #    invece di una riga sola. Misurato la prima volta con le sei toppe
    #    dell'inventario, dove due delle sei erano identiche fra loro.
    ambigue = 0
    per_file = collections.defaultdict(list)
    for nome, riga, classe, eti, riga_testo in testo:
        per_file[nome].append(riga)
    for nome, righe_n in per_file.items():
        sorg = io.open(os.path.join(nu.SORGENTE, nome), encoding='cp932').read().split('\n')
        quante = collections.Counter(sorg)
        ambigue += sum(1 for n in righe_n if quante[sorg[n - 1]] > 1)
    print()
    print('=== quanto costa toparle: %d righe su %d NON sono uniche nel loro file'
          % (ambigue, len(testo)))
    print('    (una toppa a riga singola sarebbe ambigua: vogliono un blocco di piu\' righe)')

    print()
    print('=== le sigle: i letterali distinti (per controllare che non sia testo)')
    distinte = collections.Counter()
    for nome, riga, classe, eti, riga_testo in tutto:
        if classe != 'sigla':
            continue
        for x in nu._LETTERALE.findall(riga_testo):
            if nu._e_testo(x):
                distinte[x.strip()] += 1
    print('  ' + ', '.join(sorted(distinte)))


if __name__ == '__main__':
    main(sys.argv[1:])
