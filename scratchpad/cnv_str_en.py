# -*- coding: utf-8 -*-
"""Il QUARTO punto cieco: `cnv_str` che riscrive una stringa gia' composta.

`blocchi_en.py` guarda dentro `if ( en )`, `else_jp.py` dentro
`if ( jp ) ... else`, `variabili_en.py` gli assegnamenti incondizionati che si
portano dentro un letterale inglese. Nessuno dei tre vede questo:

    ndeathcause = lang("罠にかかって死んだ。", "was killed by " + cdatan(...))
    cnv_str ndeathcause, "was killed by motuhegui", "was mauled to death by a bear"

`cnv_str` e' la sostituzione di sottostringa di HSP. Il mod la usa per riscrivere
una stringa **gia' composta**, e la chiave e' scritta nell'**inglese di monte**:
appena la resa italiana entra — o appena cambia una delle funzioni che compongono
la stringa — la chiave non aggancia piu' e la riscrittura **non avviene**.

⚠️ E il caso che l'ha fatta scoprire era gia' rotto: `db_creature.hsp:37656`
rende モツヘグイ «lo sbudellatore», quindi `cdatan(CDATAN_NAME, cc)` restituisce
«lo sbudellatore» e la chiave `"was killed by motuhegui"` non aggancia **da
mesi**. La battuta dell'orso e' morta quando si e' tradotto il bestiario, e
nessuna verifica l'ha detto.

Referto, non guardia: stampa ogni sito e dice se la chiave e' inglese.
"""
import glob
import io
import os
import re

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

# cnv_str <variabile>, <cerca>, <metti>
CHIAMATA = re.compile(r'^\s*cnv_str\s+([A-Za-z_@][\w@]*)\s*,\s*(.+)$')
LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
LATINO = re.compile(r'[A-Za-z]')
GIAPPONESE = re.compile(r'[\u3040-\u30ff\u4e00-\u9fff]')

siti = []
for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
    nome = os.path.basename(percorso)
    for numero, riga in enumerate(io.open(percorso, encoding='cp932').read().split('\n'), 1):
        trovato = CHIAMATA.match(riga)
        if not trovato:
            continue
        letterali = LETTERALE.findall(trovato.group(2))
        siti.append((nome, numero, trovato.group(1), letterali, riga.strip()))

print(f'{len(siti)} chiamate a cnv_str nel sorgente pinnato\n')

inglesi = []
for nome, numero, variabile, letterali, riga in siti:
    if not letterali:
        continue
    chiave = letterali[0]
    # La chiave e' inglese se ha lettere latine e nessun kana/kanji.
    if LATINO.search(chiave) and not GIAPPONESE.search(chiave):
        inglesi.append((nome, numero, variabile, letterali))

print(f'⚠️ {len(inglesi)} con la chiave scritta in INGLESE '
      f'(la resa italiana le spegne, o le ha gia\' spente):\n')
for nome, numero, variabile, letterali in inglesi:
    cerca = letterali[0]
    metti = letterali[1] if len(letterali) > 1 else '?'
    print(f'  {nome}:{numero}  {variabile}')
    print(f'      cerca  {cerca!r}')
    print(f'      metti  {metti!r}')

altre = len(siti) - len(inglesi)
print(f'\n{altre} chiamate con chiave non inglese (giapponese, marcatori, numeri): '
      f'quelle non dipendono dalla lingua della resa.')
