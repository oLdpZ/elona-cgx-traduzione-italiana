# -*- coding: utf-8 -*-
"""I letterali inglesi nudi che stanno sulla STESSA RIGA di una `lang()`.

Il punto cieco di `nudi_en.py`, trovato nella 61a aprendo `config.hsp`. Quel
referto salta la riga intera appena ci legge un `lang(`:

    if 'lang(' in s:
        continue

e la riga che l'ha fatto vedere e' `config.hsp:618`, l'elenco delle voci del
menu «Messaggi e registro»:

    s = lang("ログに時刻表示追加", "Add time info"), ..., "  Display log instead*",
        "Capitalize item names", ""

Quattro voci passano dal dizionario e **due no**: sono aggiunte del mod, scritte
in inglese per tutti e senza `lang()` intorno. Un lotto non le raggiunge —
`estrai.py` guarda solo dentro le `lang()` — e `nudi_en.py` non le conta, perche'
la riga «ha una lang()». Restano inglesi a schermo e nessun conteggio le nomina.

⚠️ **Non e' una classe nuova di letterale: e' la stessa di `nudi_en.py`**, vista
da un angolo che quel referto si era chiuso da solo. Per questo il filtro su che
cosa e' testo (`_e_testo`) e su quali righe disegnano (`_DISEGNA`, `_COMPONE`) si
importa da li' invece di riscriverlo: se un giorno quei filtri cambiano, questo
referto cambia con loro.

Come gli altri, struttura e lingua sono due misure diverse:

- **struttura**: quante righe cosi' fatte ci sono nel sorgente pinnato;
- **da fare**: quelle i cui **nudi** nella build sono ancora quelli del
  sorgente, cioe' che nessuna toppa ha toccato;
- **decise**: quelle guardate e lasciate in inglese col motivo scritto (vedi
  `DECISE`).

⚠️⚠️ **Il «da fare» si misura sui nudi, non sulla riga**, e la prima versione di
questo referto sbagliava proprio li'. Su una riga mista la riga cambia
**sempre** fra sorgente e build, perche' il dizionario ci ha riscritto le
`lang()`: misurando la riga, `config.hsp:805` e `:809` risultavano fatte appena
il file ha avuto un dizionario, e `MCI` non l'aveva toccato nessuno. Contava 7
da fare dove ce n'erano 15. E' la lezione della 60a — una misura presa su un
insieme piu' largo di quello che si vuole misurare — ripetuta dentro il referto
che la citava.

Atteso al 2026-08-18: **19 di struttura, 0 da fare, 6 decise**. Le nove che
mancavano sono state toppate lo stesso giorno, e tutte e nove hanno chiesto la
forma `prima` (`applica.py`), perche' una toppa scritta sul sorgente non ritrova
la riga dopo che il dizionario l'ha riscritta.
"""
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import nudi_en

SORGENTE = nudi_en.SORGENTE
BUILD = nudi_en.BUILD

# ⚠️ `"null"` e' il SECONDO argomento di `promptAdd`, cioe' la lettera di scelta
#    della voce: «null» vuol dire «nessuna scorciatoia». Non e' testo, e senza
#    questa regola sono 96 righe su 130 — il referto affogherebbe. `nudi_en.py`
#    non lo sa perche' non arriva mai a guardare una riga con `lang(` dentro, e
#    li' il letterale della lettera di scelta sta sempre accanto a una.
NON_TESTO = {'null'}

# I siti guardati e **decisi**: restano in inglese per scelta, col motivo scritto.
# Come le tabelle di `tabelle_en.py`, non stanno in `rinviate.jsonl`, perche' quel
# file indicizza per firma `lang()` e qui di firma non ce n'e' nessuna: il
# letterale e' nudo. Un referto che li contasse come lavoro direbbe per sempre
# «sei da fare» su una classe che invece e' chiusa.
DECISE = {
    ('command.hsp', 10659): "« cm» e « kg» sono unita' SI: in italiano si scrivono uguale",
    ('command.hsp', 14077): "«Tab» e' il nome di un tasto, non una parola",
    ('module.hsp', 5195): "«Tab» e' il nome di un tasto, non una parola",
    ('config.hsp', 805): "«MCI» e' il nome del driver audio, come «Direct sound» in invariati.md",
    ('config.hsp', 809): "«MCI» e «GuruGuruSMF4» sono nomi di driver",
    ('main.hsp', 4409): "«dead» e' il prefisso del messaggio che net_send manda al "
                        "server (main.hsp:4411), non testo che qualcuno legga",
}


def _e_testo(letterale: str) -> bool:
    if letterale.strip() in NON_TESTO:
        return False
    return nudi_en._e_testo(letterale)


def senza_lang(riga: str) -> str:
    """La riga con ogni `lang( ... )` sostituita da uno spazio.

    Si cammina a carattere perche' dentro una `lang()` ci possono stare
    parentesi, virgole e virgolette protette: una regex qui sbaglierebbe.
    """
    fuori = []
    i = 0
    n = len(riga)
    while i < n:
        if riga.startswith('lang(', i):
            profondita = 0
            j = i + 4
            dentro_stringa = False
            while j < n:
                c = riga[j]
                if dentro_stringa:
                    if c == '\\':
                        j += 2
                        continue
                    if c == '"':
                        dentro_stringa = False
                elif c == '"':
                    dentro_stringa = True
                elif c == '(':
                    profondita += 1
                elif c == ')':
                    profondita -= 1
                    if profondita == 0:
                        j += 1
                        break
                j += 1
            fuori.append(' ')
            i = j
            continue
        if riga[i] == '"':
            # un letterale fuori da lang(): si copia intero, virgolette comprese
            j = i + 1
            while j < n:
                if riga[j] == '\\':
                    j += 2
                    continue
                if riga[j] == '"':
                    j += 1
                    break
                j += 1
            fuori.append(riga[i:j])
            i = j
            continue
        fuori.append(riga[i])
        i += 1
    return ''.join(fuori)


def righe_miste(righe: list[str]) -> list[int]:
    """Gli indici (0-based) delle righe che hanno una `lang()` E un nudo."""
    trovati = []
    for i, riga in enumerate(righe):
        s = riga.strip()
        if not s or s.startswith('//') or s.startswith('#') or s.startswith('/*'):
            continue
        if 'lang(' not in s:
            continue          # quelle le conta gia' nudi_en.py
        if s.startswith('cnv_str'):
            continue
        if nudi_en._PER_CHIAVE.search(s):
            continue
        if not (nudi_en._DISEGNA.match(s) or nudi_en._COMPONE.match(s)):
            continue
        resto = senza_lang(s)
        if any(_e_testo(m) for m in nudi_en._LETTERALE.findall(resto)):
            trovati.append(i)
    return trovati


def nudi_di(riga: str) -> list[str]:
    """I letterali di testo che stanno FUORI da ogni `lang()` su questa riga."""
    return [m for m in nudi_en._LETTERALE.findall(senza_lang(riga.strip()))
            if _e_testo(m)]


def ancora_intatta(riga_sorgente: str, riga_build: str) -> bool:
    """Vero se i nudi di quella riga non li ha toccati nessuna toppa.

    ⚠️⚠️ **Non si confronta la riga intera**, ed e' la correzione piu'
    importante di questo referto. Su una riga mista la riga cambia **sempre**
    fra sorgente e build, perche' il dizionario ci ha riscritto le `lang()`:
    misurare la riga faceva risultare fatte tutte e tre le righe di
    `config.hsp` appena il dizionario del file e' entrato, comprese `:805` e
    `:809`, dove `MCI` e `GuruGuruSMF4` non li aveva toccati nessuno. Il metro
    giusto sono i **nudi**, che sono la cosa che il referto conta.

    E' la stessa forma di difetto della rete 5 nella 60a: una misura presa su
    un insieme piu' largo di quello che si voleva misurare.
    """
    return nudi_di(riga_sorgente) == nudi_di(riga_build)


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_struttura = tot_da_fare = tot_decise = 0
    for nome in nomi:
        sorg = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        percorso_build = os.path.join(BUILD, nome)
        build = (io.open(percorso_build, encoding='cp932').read().split('\n')
                 if os.path.exists(percorso_build) else sorg)
        indici = righe_miste(sorg)
        if not indici:
            continue
        intatte = [i for i in indici
                   if i >= len(build) or ancora_intatta(sorg[i], build[i])]
        decise = [i for i in indici if (nome, i + 1) in DECISE]
        da_fare = [i for i in intatte if i not in decise]
        tot_struttura += len(indici)
        tot_da_fare += len(da_fare)
        tot_decise += len(decise)
        print(f'=== {nome}: {len(indici)} righe, {len(da_fare)} da fare, '
              f'{len(decise)} decise')
        for i in indici:
            marca = '=' if i in decise else (' ' if i in intatte else '.')
            nudi = nudi_di(sorg[i])
            print(f'  {marca}{i + 1:6d} | {" | ".join(repr(x) for x in nudi)}')
            if i in decise:
                print(f'           DECISA: {DECISE[(nome, i + 1)]}')
    print(f'\n--- struttura: {tot_struttura} righe | da fare: {tot_da_fare} '
          f'| decise: {tot_decise}')


if __name__ == '__main__':
    main(sys.argv[1:])
