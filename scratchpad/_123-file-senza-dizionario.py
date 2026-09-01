# -*- coding: utf-8 -*-
"""123a - Quali file hanno `lang()` nel sorgente e NON hanno un dizionario.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-file-senza-dizionario.py

⚠️⚠️⚠️ **PERCHE' ESISTE.** Dalla 123a **ogni file con un dizionario dice
`⭐ CHIUSO`**: `_97-quanto-resta` legge «TOTALE da fare 0» e `verifica
--dizionario` legge zero da ritradurre dappertutto. Ma `perimetro.py` dice
**90%**, e i due numeri non si contraddicono: `_97-quanto-resta` guarda **solo i
file che HANNO un dizionario**, e i file che non ce l'hanno non compaiono
nemmeno come riga.

⭐ E' la forma peggiore di zero: non «zero perche' e' finito», ma **zero perche'
non e' stato chiesto**. Questo strumento fa la domanda al posto giusto — quali
file portano `lang()` e nessuno ha mai estratto — e stampa **quante** stringhe
ci sono dentro, cosi' lo zero di `_97-quanto-resta` si legge accanto al numero
che gli manca.

⚠️⚠️ **LE FIRME DISTINTE E LE OCCORRENZE SONO DUE NUMERI DIVERSI**, e la prima
stesura di questo strumento contava le seconde: diceva **447** dove
`perimetro.py` dice **355**, e i due referti non si potevano confrontare.
`perimetro.firme_lang()` raccoglie gli argomenti inglesi in un **insieme**,
quindi due `lang()` con lo stesso inglese sono **una** firma — ed e' giusto
cosi', perche' una resa le copre tutt'e due. Qui si riusa quella funzione
invece di riscriverla: la colonna «firme» deve sommare **esattamente** al «di
cui in file mai estratti» del perimetro, e la colonna «lang()» sta accanto solo
per far vedere quante ripetizioni ci sono.
"""
import glob
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DIZIONARIO = os.path.join(RADICE, 'dizionario')
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

sys.path.insert(0, QUI)
import perimetro  # noqa: E402  — per `firme_lang`, che e' la definizione buona

LANG = re.compile(r'\blang\s*\(')


def main():
    con_dizionario = {os.path.basename(p).replace('.jsonl', '')
                      for p in glob.glob(os.path.join(DIZIONARIO, '*.jsonl'))}

    senza, con = [], []
    for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
        nome = os.path.basename(percorso)
        testo = io.open(percorso, encoding='cp932', errors='replace').read()
        firme = len(perimetro.firme_lang(testo))
        if firme == 0:
            continue
        (con if nome in con_dizionario else senza).append(
            (firme, len(LANG.findall(testo)), nome))

    senza.sort(reverse=True)
    print()
    print('  I FILE CON `lang()` E SENZA DIZIONARIO')
    print()
    print('   firme   lang()   file')
    print('  ' + '-' * 50)
    for firme, occorrenze, nome in senza:
        print('  %6d   %6d   %s' % (firme, occorrenze, nome))
    print('  ' + '-' * 50)
    print('  %6d   %6d   TOTALE in %d file'
          % (sum(f for f, _, _ in senza),
             sum(o for _, o, _ in senza), len(senza)))
    print()
    print('  ⓘ referto, non cancello. Il valore atteso NON e\' zero: e\' il')
    print('    numero che `_97-quanto-resta` non puo\' vedere, e la colonna')
    print('    «firme» deve fare il «di cui in file mai estratti» del perimetro.')
    print()

    # ⚠️ Prova al contrario: si CERCA il caso peggiore invece di ipotizzarlo.
    # Se la rete confondesse i due insiemi, il file con dizionario piu' carico
    # comparirebbe nell'elenco qui sopra. Si stampa quale e' e quanto pesa, non
    # un ✅: un esito booleano nasconde la differenza fra «ho cercato il caso
    # peggiore» e «non l'ho cercato abbastanza».
    if con:
        peggiore = max(con)
        nomi_senza = [n for _, _, n in senza]
        print('  prova al contrario: il file CON dizionario piu\' carico e\' %s'
              % peggiore[2])
        print('    (%d firme, %d lang()), e la rete %s'
              % (peggiore[0], peggiore[1],
                 'lo TACE, com\'e\' giusto'
                 if peggiore[2] not in nomi_senza else '⚠️ LO STAMPA: e\' rotta'))
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
