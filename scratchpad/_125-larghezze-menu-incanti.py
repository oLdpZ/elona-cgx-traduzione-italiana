# -*- coding: utf-8 -*-
"""125a - Le tre voci di menu della finestra degli incantamenti, misurate col
nome dell'oggetto DENTRO.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-larghezze-menu-incanti.py

⚠️⚠️⚠️ **PERCHE' SERVE UN CANCELLO A PARTE.** `strumenti/menu_dialogo.py` dice
«0 su 1383» su questa finestra e non la sta guardando, per due motivi diversi:

  1. legge il **dizionario** (`voci_di_menu`, `:491`), e `:278` e `:280` sono
     letterali inglesi nudi messi da una toppa: voce di dizionario non ne hanno,
     quindi non entrano nemmeno nel denominatore;
  2. `:276` nel dizionario c'e', ma `reso()` scioglie i segnaposto e una
     **chiamata di funzione non porta caratteri**: `cnvitemname(p_item1)` viene
     misurata come lunga zero, dove a schermo sono fino a 38.

E' la forma di guasto della 124a («un cancello booleano non dice il margine»)
con un'aggravante: qui il cancello non era booleano, era **verde**.

⭐ **Il nome dell'oggetto non e' una variabile qualunque: e' enumerabile.**
`p_item1` e `p_item2` prendono tre soli valori in tutto il file
(`*extrachat_calculate_enhance_cost`, `:192`-`:236`), e i loro nomi italiani
stanno nel dizionario. Percio' qui non si stima: si prova ogni combinazione.

    p_item1   POTION_EVOLUTION, POTION_MUTATION        (a DUMMY la voce
                                                        non compare, :275)
    p_item2   POTION_EVOLUTION, SCROLL_GAIN_ATTRIBUTE  (:227, :232)

⚠️ **Il caso peggiore non e' quello che viene in mente.** «pozione di
evoluzione» sono 21 caratteri e sembra il metro; la **pergamena di acquisizione
di attributi** ne fa **38**, contro i 24 di «scroll of gain attribute». E'
l'unico posto del progetto misurato finora dove l'italiano di un nome d'oggetto
costa **quattordici caratteri** piu' dell'inglese dentro un tetto stretto.

⚠️ **La prova al contrario non e' una stringa finta**: sono le tre stesure vere
scartate nella 125a, che su questo stesso metro devono accendersi.
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
sys.path.insert(0, RADICE)

from strumenti.menu_dialogo import TETTO  # noqa: E402

# I tre oggetti, per ID sorgente e riga del nome in db_item.hsp. I nomi si
# leggono dal dizionario invece di scriverli qui: se un giorno cambiassero, il
# cancello misurerebbe i nomi veri e non quelli che avevo in mente oggi.
NOMI = {
    'POTION_EVOLUTION': (142915, 142914),      # "pozione" + " di " + "evoluzione"
    'POTION_MUTATION': (146877, 146876),
    'SCROLL_GAIN_ATTRIBUTE': (149508, 149507),
}

# chi puo' finire in ciascuna voce, letto dal sorgente
CANDIDATI = {
    276: ('POTION_EVOLUTION', 'POTION_MUTATION'),
    278: ('POTION_EVOLUTION', 'SCROLL_GAIN_ATTRIBUTE'),
    280: ('POTION_EVOLUTION', 'SCROLL_GAIN_ATTRIBUTE'),
}

VOCI = {
    276: 'Potenziare? (%s)',
    278: 'Indebolire? (%s)',
    280: 'Cancellare? (%s)',
}

# Le tre stesure scartate: la prova al contrario. Su questo metro si accendono.
SCARTATE = {
    276: 'Potenziare l\'incanto? (%s)',
    278: 'Provare a cancellare l\'incanto? (%s)',
    280: 'Cancellare l\'incanto? (%s)',
}

# L'inglese di monte, per il confronto: il metro non e' lui, ma dice da dove
# viene il danno (la stessa forma di `fuori_misura_inglese`).
INGLESE = {
    276: 'Enhance the enchantment? (%s)',
    278: 'Try to remove the enchantment? (%s)',
    280: 'Remove the enchantment? (%s)',
}
NOMI_EN = {
    'POTION_EVOLUTION': 'potion of evolution',
    'POTION_MUTATION': 'potion of mutation',
    'SCROLL_GAIN_ATTRIBUTE': 'scroll of gain attribute',
}


def nomi_italiani():
    """cnvitemname() in italiano: ioriginalnameref2 + " di " + ioriginalnameref
    (`init.hsp:186`-`:189`, e nella build il « of » e' gia' « di »)."""
    per_riga = {}
    percorso = os.path.join(RADICE, 'dizionario', 'db_item.hsp.jsonl')
    for r in io.open(percorso, encoding='utf-8'):
        v = json.loads(r)
        per_riga[v['riga']] = v.get('it') or ''
    fuori = {}
    for chiave, (riga_tipo, riga_nome) in NOMI.items():
        tipo, nome = per_riga.get(riga_tipo), per_riga.get(riga_nome)
        assert tipo and nome, (chiave, riga_tipo, riga_nome)
        fuori[chiave] = tipo + ' di ' + nome
    return fuori


def misura(modelli, nomi, etichetta):
    fuori = 0
    for riga in sorted(modelli):
        for chiave in CANDIDATI[riga]:
            testo = modelli[riga] % nomi[chiave]
            quanto = len(testo)
            segno = ' ' if quanto <= TETTO else '✗'
            if quanto > TETTO:
                fuori += 1
            print('  %s :%d  %3d  %s' % (segno, riga, quanto, testo))
    print('  --- %s: %d fuori misura, tetto %d\n' % (etichetta, fuori, TETTO))
    return fuori


def main():
    nomi = nomi_italiani()
    print('cnvitemname() in italiano:')
    for chiave, nome in sorted(nomi.items()):
        print('  %-24s %2d  %s' % (chiave, len(nome), nome))
    print('  %-24s %2d  %s (il piu\' lungo in inglese)\n'
          % ('SCROLL_GAIN_ATTRIBUTE', len(NOMI_EN['SCROLL_GAIN_ATTRIBUTE']),
             NOMI_EN['SCROLL_GAIN_ATTRIBUTE']))

    print('LE RESE IN GIOCO')
    fuori = misura(VOCI, nomi, 'rese')

    print('L\'INGLESE DI MONTE, per confronto')
    misura(INGLESE, NOMI_EN, 'monte')

    print('LA PROVA AL CONTRARIO: le tre stesure scartate nella 125a')
    accese = misura(SCARTATE, nomi, 'scartate')
    if accese == 0:
        print('⚠️ LA PROVA AL CONTRARIO NON SI E\' ACCESA: il cancello non misura.')
        return 2

    print('rese fuori misura: %d   (prova al contrario accesa su %d)'
          % (fuori, accese))
    return 1 if fuori else 0


if __name__ == '__main__':
    raise SystemExit(main())
