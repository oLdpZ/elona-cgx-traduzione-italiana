# -*- coding: utf-8 -*-
"""Le intestazioni di colonna: chi le scrive e chi e' ancora in inglese.

`display_topic` disegna un'intestazione. Certe la ricevono per letterale
(`display_topic "Ver", …`), altre per variabile (`display_topic s, …`), e in
quel caso la parola sta in un'assegnazione poco sopra — spesso dentro il ramo
`else` di un `if ( jp )`, dove nessun `lang()` la protegge.

Confronta sorgente e build: se la riga e' identica, nessuno l'ha tradotta.

⭐ Nato nella 63a, dopo che il collaudo della finestra dei talenti ha mostrato
`Name` e `Detail` in inglese sopra una lista tutta italiana (`command.hsp:2601`,
dentro il ramo `else` di un `if ( jp )`). `nudi_en` quella riga la conosceva —
era una delle sue 445 — ma nessuno sapeva che pesava un'intestazione di colonna:
e' la lezione della 55a, *un referto dice che una riga esiste, solo lo schermo
dice quanto pesa*.

⭐ **Atteso: 2 assegnazioni, 0 intatte.** Sono due chiamate che leggono la stessa
riga (`display_topic s` e `display_topic s(2)`), quindi la riga e' una sola. Se
«intatte» sale, un aggiornamento CGX ha portato una finestra nuova con
l'intestazione in inglese.

⚠️ Guarda solo le chiamate `display_topic <variabile>`: quelle scritte
`display_topic lang("…", "…")` sono gia' al sicuro, e quelle con un letterale
nudo (`display_topic "Ver"`, `command.hsp:459`) le vede `nudi_en`.
"""
import io
import os
import re

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

CHIAMA = re.compile(r'^\s*display_topic\s+(\w+)(\(\d+\))?\s*,')
ASSEGNA = re.compile(r'^\s*(\w+)\s*=\s*"')
LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def leggi(percorso):
    with io.open(percorso, encoding='cp932', errors='replace') as f:
        return f.read().split('\n')


def main():
    totale = intatte = 0
    for nome in sorted(os.listdir(BUILD)):
        if not nome.endswith('.hsp'):
            continue
        b = leggi(os.path.join(BUILD, nome))
        s = leggi(os.path.join(SORGENTE, nome))
        trovate = []
        for n, riga in enumerate(b):
            m = CHIAMA.match(riga)
            if not m:
                continue
            var = m.group(1)
            # L'assegnazione della variabile, cercata all'indietro.
            for k in range(n - 1, max(n - 12, -1), -1):
                a = ASSEGNA.match(b[k])
                if a and a.group(1) == var:
                    testi = LETTERALE.findall(b[k])
                    if not testi:
                        break
                    uguale = k < len(s) and b[k] == s[k]
                    trovate.append((k + 1, b[k].strip(), uguale))
                    break
        if not trovate:
            continue
        print(f'=== {nome}')
        for riga, testo, uguale in trovate:
            totale += 1
            segno = 'INTATTA' if uguale else 'tradotta'
            if uguale:
                intatte += 1
            print(f'  {riga:>6} {segno:<9} {testo[:96]}')
    print()
    print(f'--- {totale} assegnazioni che finiscono in display_topic, '
          f'{intatte} ancora intatte')


if __name__ == '__main__':
    main()
