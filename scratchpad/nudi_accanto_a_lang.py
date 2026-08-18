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
- **da fare**: quelle che nella build sono ancora identiche al sorgente, cioe'
  che nessuna toppa ha ancora toccato.
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


def main(argv: list[str]) -> None:
    nomi = argv or sorted(os.path.basename(p) for p in glob.glob(SORGENTE + r'\*.hsp'))
    tot_struttura = tot_da_fare = 0
    for nome in nomi:
        sorg = io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')
        percorso_build = os.path.join(BUILD, nome)
        build = (io.open(percorso_build, encoding='cp932').read().split('\n')
                 if os.path.exists(percorso_build) else sorg)
        indici = righe_miste(sorg)
        if not indici:
            continue
        intatte = [i for i in indici
                   if i < len(build) and build[i] == sorg[i]]
        tot_struttura += len(indici)
        tot_da_fare += len(intatte)
        print(f'=== {nome}: {len(indici)} righe, {len(intatte)} ancora intatte')
        for i in indici:
            marca = ' ' if i in intatte else '.'
            nudi = [m for m in nudi_en._LETTERALE.findall(senza_lang(sorg[i].strip()))
                    if _e_testo(m)]
            print(f'  {marca}{i + 1:6d} | {" | ".join(repr(x) for x in nudi)}')
    print(f'\n--- struttura: {tot_struttura} righe | ancora da fare: {tot_da_fare}')


if __name__ == '__main__':
    main(sys.argv[1:])
