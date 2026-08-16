# -*- coding: utf-8 -*-
"""L'OTTAVO punto cieco: `nudi_en` decide dal NOME, e la lista dei nomi e' chiusa.

`nudi_en._COMPONE` (`nudi_en.py:47`) riconosce una riga che compone testo
guardando come si chiama la variabile a sinistra, e l'elenco e' di sette nomi:
`s`, `buff`, `valn`, `strhint*`, `locvar_*_s*`, `refstr`, `cardrefskill`.
Qualunque **variabile nuova** che porti testo e' invisibile per costruzione — non
per un difetto di scrittura della regola, ma perche' la regola e' un elenco.

⭐ **A dimostrarlo e' stato `effdesc@tcg`**, trovato dalla 53ª aprendo il negozio
delle carte: `tcg_mod.hsp` ha **835 righe** cosi'

    effdesc@tcg(TCG_EFF_BATTLECRY_DRAW1CARD) = "Battlecry: Draw 1 Card."

e sono le descrizioni degli effetti che si leggono **su ogni carta**:
`tcg.hsp:1473` scrive `"Effect: " + effdesc@tcg(…)`, `:3935` e `:4170` le
passano a `cardhelp`. Ottocentotrentacinque righe di testo inglese che nessun
conteggio del progetto ha mai nominato — piu' di quante ne abbia mai avute
qualunque altro punto cieco.

⚠️⚠️ **E una almeno e' anche un CONFRONTO**: `tcg_skill.hsp:618` fa
`instr(effdesc@tcg(dbid@tcg), 0, "Battlecry")`, cioe' cerca la parola dentro la
descrizione. Tradurre «Battlecry» vuol dire toppare anche quel letterale, o
`cancopyeffect` smette di riconoscere gli effetti copiabili. E' la famiglia
della 46ª e della 52ª in una forma nuova: qui il testo e' **insieme** roba da
leggere e roba da confrontare.

## Che cosa conta questo referto, e che cosa no

Conta le assegnazioni `<nome>[@modulo][(indice)] = "…"` con un letterale che
sembra inglese, **tolte** quelle che `nudi_en` e `nudi_dopo_if` gia' vedono, e
le raggruppa per nome. ⚠️ **Non e' una guardia: e' un metro.** La maggior parte
dei nomi che trova NON e' testo, ed e' giusto che non lo sia:

    dbidn              3330   la chiave della creatura in db_creature.hsp
    cardrefrace/class  3334   le chiavi di razza e classe (vedi tcg.hsp:3757)
    ioriginalnameref   1308   i nomi degli oggetti, che stanno GIA' nel perimetro
                              come secondo tipo di sito di `estrai` (contratto-nomi.md)
    listn(1, …)         88    la chiave del dato, non la colonna che si legge
    file / fileext      ~190  nomi di file

Il valore del referto e' l'elenco dei nomi, non il totale: **si legge una volta,
si decide nome per nome, e quel che resta e' lavoro.** I nomi che portano testo
misurati dalla 53ª:

    effdesc@tcg          835   le descrizioni degli effetti delle carte
    carddetailneff@tcg    77   il testo d'effetto composto per la carta in gioco
    TweakData(x, 0)       77   i titoli delle categorie del pannello dei ritocchi
    ErrorMsg              41   i messaggi d'errore di init.hsp (coppie jp/en)
    StatPotential         10   le etichette del potenziale (map_user.hsp:2340)

💡 **`description(…)` e' un caso a parte, gia' noto**: sono le 2.831 descrizioni
degli oggetti, e `perimetro.py` le conta gia' fra le «5.284 descrizioni MAI
contate» del testo fuori perimetro. Non e' una scoperta di questo referto — e'
la conferma che il conto di `perimetro.py` diceva il vero.
"""
import collections
import glob
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import re

from nudi_en import SORGENTE, _LETTERALE, _PER_CHIAVE, _e_testo, righe_nude
from nudi_dopo_if import righe_cieche

# `nome`, `nome@modulo`, `nome(indice)`, `nome@modulo(indice)`, `=` o `+=`
ASSEGNA = re.compile(r'^([A-Za-z_]\w*)(@\w*)?\s*(\([^)]*\))?\s*\+?=\s*"')


def main(argv: list[str]) -> None:
    quanti = int(argv[0]) if argv else 25
    per_nome = collections.Counter()
    per_file = collections.Counter()
    esempi: dict[str, str] = {}

    for percorso in sorted(glob.glob(str(SORGENTE) + r'\*.hsp')):
        nome_file = os.path.basename(percorso)
        righe = io.open(percorso, encoding='cp932').read().split('\n')
        # ⚠️ Si tolgono le righe che gli altri due referti gia' elencano: questo
        #    misura il RESTO, non il totale.
        viste = set(righe_nude(righe)) | set(righe_cieche(righe))
        for i, riga in enumerate(righe):
            if i in viste:
                continue
            s = riga.strip()
            if not s or s[0] == ';' or s.startswith('//') or s.startswith('#') or s.startswith('/*'):
                continue
            if 'lang(' in s or _PER_CHIAVE.search(s):
                continue
            m = ASSEGNA.match(s)
            if not m:
                continue
            if not any(_e_testo(t) for t in _LETTERALE.findall(s)):
                continue
            chiave = m.group(1) + (m.group(2) or '')
            per_nome[chiave] += 1
            per_file[nome_file] += 1
            esempi.setdefault(chiave, f'{nome_file}:{i+1} | {s[:86]}')

    print(f'=== per NOME di variabile (i primi {quanti})')
    for nome, n in per_nome.most_common(quanti):
        print(f'  {n:6d}  {nome:24s} {esempi[nome]}')
    print(f'=== per FILE (i primi {quanti})')
    for f, n in per_file.most_common(quanti):
        print(f'  {n:6d}  {f}')
    print(f'--- {sum(per_nome.values())} righe, {len(per_nome)} nomi diversi')


if __name__ == '__main__':
    main(sys.argv[1:])
