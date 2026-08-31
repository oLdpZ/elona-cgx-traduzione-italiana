# -*- coding: utf-8 -*-
"""Monta `reseNNN.py` da `chiaviNNN.txt` (l'inglese verbatim) e `_traduzioniNNN.py`.

Generalizza `_monta004.py`, che aveva il numero del lotto scritto dentro.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 005
    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 006 scratchpad/lotti-110

⚠️ La cartella del lotto e' il **secondo argomento**, e senza di lui e' quella
dello script. Fino alla 109a i tre file stavano accanto a `_monta.py`, e la 110a
li ha messi in `lotti-110/`: senza l'argomento lo script cercava `_traduzioni006`
in `lotti-109/` e moriva dicendo che non c'era. Copiare lo script nella cartella
nuova sarebbe stata la quarta copia di un file che la 108a ha gia' pagato caro
(vedi `modello-rete4.py`).

L'inglese e' la meta' della chiave e non si ricopia a mano: `_107-chiavi-item.py`
lo emette dal sorgente, e questo script si limita a sostituire la resa vuota.

Tre guasti silenziosi che qui diventano rumorosi, e lo script muore invece di
scrivere un file mezzo buono:

  1. una riga del template senza resa, o una resa senza riga nel template;
  2. ⚠️⚠️ una **chiave ripetuta** nel dizionario `IT`. Python non protesta e
     tiene l'ultima: due rese diverse per la stessa riga sparirebbero una
     nell'altra senza che niente lo dica. Si conta sul TESTO del file, non sul
     dizionario, perche' nel dizionario il doppione non c'e' piu';
  3. una resa vuota rimasta tale.
"""
import importlib.util
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))

INTESTAZIONE = """import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
"""


def _in_letterale(resa):
    """La resa, pronta da mettere fra virgolette doppie in un file Python.

    ⚠️⚠️ **Fino alla 113a questo script inseriva la resa GREZZA**, e andava bene
    finche' i lotti erano l'indice 3 — righe corte, senza backslash. Il CORPO
    delle descrizioni porta dentro `\\n#~fonte~`: un **backslash vero** seguito da
    `n`, che nel sorgente HSP e' l'a capo prima della riga-fonte e che il
    dizionario conserva tale e quale (53 rese ce l'hanno gia', 188 hanno `\\"`).
    Scritto grezzo dentro `"..."`, Python lo rileggeva come un a capo VERO: la
    resa sarebbe entrata nel dizionario spezzata in due, e a valle nessuno
    l'avrebbe piu' riconosciuta per quello che era.

    Sulle rese senza backslash e senza virgolette — cioe' tutti i lotti fino al
    025 — questa funzione non cambia un carattere.
    """
    return resa.replace('\\', '\\\\').replace('"', '\\"')


def carica_traduzioni(numero, cartella):
    percorso = os.path.join(cartella, f'_traduzioni{numero}.py')
    testo = io.open(percorso, encoding='utf-8').read()

    # (2) il doppione si cerca nel TESTO, prima che Python lo faccia sparire
    chiavi = re.findall(r'^\s{4}(\d+):', testo, re.M)
    ripetute = sorted({k for k in chiavi if chiavi.count(k) > 1})

    spec = importlib.util.spec_from_file_location(f'traduzioni{numero}', percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.IT, ripetute


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    numero = sys.argv[1]
    cartella = sys.argv[2] if len(sys.argv) == 3 else QUI
    template = os.path.join(cartella, f'chiavi{numero}.txt')
    uscita = os.path.join(cartella, f'rese{numero}.py')

    it, ripetute = carica_traduzioni(numero, cartella)
    righe = io.open(template, encoding='utf-8').read().splitlines()
    inizio = next(i for i, r in enumerate(righe) if r.startswith('# ') and 'righe, da' in r)
    corpo = righe[inizio + 1:]

    fuori = [f'riga {k}: chiave RIPETUTA nel dizionario IT' for k in ripetute]
    viste = set()
    for i, riga in enumerate(corpo):
        # ⚠️ l'inglese col carattere `'` dentro esce fra virgolette doppie
        m = re.match(r"^    \((\d+), ['\"]", riga)
        if not m:
            continue
        n = int(m.group(1))
        viste.add(n)
        if n not in it:
            fuori.append(f'riga {n}: nel template ma senza resa')
            continue
        if not it[n].strip():
            fuori.append(f'riga {n}: la resa e\' vuota')
            continue
        successiva = corpo[i + 1]
        if successiva != '        "",':
            fuori.append(f'riga {n}: la riga dopo non e\' la resa vuota ({successiva!r})')
            continue
        corpo[i + 1] = '        "' + _in_letterale(it[n]) + '",'

    for n in sorted(set(it) - viste):
        fuori.append(f'riga {n}: c\'e\' una resa ma il template non ha quella riga')

    if fuori:
        sys.exit('\n'.join(['⚠️ montaggio fermo:'] + fuori))

    testo = INTESTAZIONE + '\n'.join(corpo).rstrip() + '\n}\n'
    io.open(uscita, 'w', encoding='utf-8', newline='\n').write(testo)

    # ⚠️ IL GIRO DI RITORNO, dalla 113a: si rilegge quel che si e' scritto e si
    #    confronta con le rese di partenza. E' la prova che `_in_letterale()`
    #    ha fatto il suo mestiere — senza, un backslash tornava indietro come
    #    un a capo e nessuno lo diceva.
    spec = importlib.util.spec_from_file_location(f'rese{numero}', uscita)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    tornate = {chiave[0]: valore for chiave, valore in modulo.RESE.items()}
    diverse = [n for n in sorted(it) if tornate.get(n) != it[n]]
    if diverse:
        sys.exit('⚠️ il giro di ritorno non torna, righe: %s'
                 % ', '.join(str(n) for n in diverse[:10]))

    print(f'{len(viste)} rese montate in {uscita}   (giro di ritorno: {len(tornate)} identiche)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
