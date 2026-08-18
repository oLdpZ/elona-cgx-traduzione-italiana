# -*- coding: utf-8 -*-
"""L'undicesimo punto cieco: il CORPO della finestra dell'evento.

`*re_select` (`event.hsp:4119`) disegna tre cose: il titolo `s`, il corpo
`buff`, e la lista di `chatList`. Il progetto ha una rete per la terza (la 15,
`strumenti/menu_dialogo.py`) e il dizionario copre le `lang()` delle altre due.
Ma `buff` si puo' assegnare **senza** `lang()`, con un letterale inglese nudo, e
in quel caso non lo vede nessuno:

  - `nudi_en.py` guarda i letterali che **disegnano** (`txt`, `noteadd`, ...);
    qui il letterale sta in un'assegnazione, e a disegnarlo e' un'altra riga.
  - `variabili_en.py` guarda le variabili con un inglese dentro **che finiscono
    interpolate in una `lang()`**; `buff` non ci finisce mai: viene stampato
    tal quale.
  - `verifica --dizionario` indicizza per firma `lang()`, e qui la `lang()` non
    c'e'.

Cade esattamente **fra le due reti**, ed e' testo che il giocatore legge in
grande in mezzo allo schermo.

⚠️ Non e' una guardia: e' un metro. Se il numero sale, qualcuno ne ha scritta
una nuova; se scende, una e' stata resa.

💡 La forma e' quella gia' vista in `item_func.hsp` (34a): `tcg.hsp:2803` era
**gia' reso** e i diciotto fratelli intorno no. Qualcuno aveva toppato un caso
per volta senza sapere che era una famiglia.
"""
import re
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')
BUILD = Path(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx')

_ASSEGNA = re.compile(r'\bbuff\s*=\s*"([^"]*)"')
_LETTERE = re.compile(r'[A-Za-z]{2,}')

trovate: dict[str, list[tuple[int, str, str]]] = {}
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    build = (BUILD / percorso.name).read_bytes().decode('cp932', 'replace').split('\n')
    for i, riga in enumerate(righe, start=1):
        # con `lang()` sulla riga il testo passa dal dizionario: non e' nudo
        if 'lang(' in riga:
            continue
        trovato = _ASSEGNA.search(riga)
        if not trovato:
            continue
        testo = trovato.group(1)
        # `buff = ""` azzera il corpo, non lo scrive
        if not _LETTERE.search(testo):
            continue
        resa = ''
        if i - 1 < len(build):
            altro = _ASSEGNA.search(build[i - 1])
            if altro and altro.group(1) != testo:
                resa = altro.group(1)
        trovate.setdefault(percorso.name, []).append((i, testo, resa))

tutte = [(f, i, t, r) for f, v in trovate.items() for i, t, r in v]
rese = [x for x in tutte if x[3]]
print(f"corpi di finestra con un inglese nudo: {len(tutte)}  |  "
      f"gia' rese: {len(rese)}  |  ancora da fare: {len(tutte) - len(rese)}\n")

for file, voci in sorted(trovate.items(), key=lambda x: -len(x[1])):
    da_fare = sum(1 for _, _, r in voci if not r)
    print(f'  {file:<22} {len(voci):3d}   da fare {da_fare:3d}')
print()

for file, i, testo, resa in sorted(tutte):
    if resa:
        continue
    print(f'  {file}:{i}  {testo[:76]}')
