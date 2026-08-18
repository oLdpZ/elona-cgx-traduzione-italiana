# -*- coding: utf-8 -*-
"""L'undicesimo punto cieco: il CORPO della finestra, composto fuori da `lang()`.

`*re_select` (`event.hsp:4119`) disegna tre cose: il titolo `s`, il corpo
`buff`, e la lista di `chatList`. Il progetto ha una rete per la terza (la 15,
`strumenti/menu_dialogo.py`) e il dizionario copre le `lang()` delle altre due.
Ma `buff` si puo' scrivere **senza** `lang()`, con un letterale inglese nudo, e
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

## ⚠️⚠️ Le due forme, e la seconda e' la piu' grossa (corretta il 2026-08-18)

La prima versione di questo referto guardava solo `buff = "..."` e ne trovava
44. **Non vedeva `buff += "..."`**, cioe' la forma con cui un corpo si compone
**a pezzi** — ed e' esattamente lo stesso difetto che la 47a aveva corretto in
`variabili_en.py`, nello stesso progetto e per la stessa ragione. Col `+=`
saltano fuori **altre 80 righe fuori da un ramo di lingua**, e 79 sono un
pannello intero:

    command.hsp:8049-:8175   la scheda dell'avventuriero conosciuto (`knowCNPC`)

«Level», «Male», «Female», «Bad», «Common», «Skilled», «Legendary», «Likes to:
Kill Snails.», «Prefered Distance:», «Immune to Paralyze.», «Goes Kamikaze.»,
«VERY ANGRY» — una finestra da capo a fondo, in inglese, e nessun conteggio del
progetto la nominava.

💡 **Le due forme vanno tenute distinte nel referto**, perche' il `+=` dentro un
ramo `if ( jp ) … else …` e' gia' materia di `else_jp.py` e contarlo qui
sarebbe contarlo due volte. La colonna «ramo» dice quante sono.

## ⚠️ E lo ESCAPE, che e' il terzo inciampo dello stesso referto

`command.hsp:8073` scrive una riga che contiene una **virgoletta protetta**. Una
regex che si ferma alla prima virgoletta la legge come fine della stringa,
cattura un backslash solo, e il filtro «almeno due lettere» butta via la riga:
sparisce dal conto senza dire niente. Nello HSP il backslash e' un escape dentro
i letterali — sta scritto nel docstring di `estrai.py` da sempre, e questo
referto lo aveva ignorato. La forma giusta legge la stringa intera saltando le
coppie protette, ed e' la stessa che il progetto usa gia' altrove.

💡 **Tre correzioni in un giorno allo stesso referto**, e nessuna delle tre era
un'idea nuova: il `+=` lo aveva gia' imparato `variabili_en.py` nella 47a, lo
escape lo dice `estrai.py`, e la distinzione dal ramo di lingua e' `else_jp.py`.
**Un referto nuovo sbaglia dove il progetto ha gia' sbagliato**, e conviene
rileggere gli altri prima di scriverne uno.

⚠️ Non e' una guardia: e' un metro. Se il numero sale, qualcuno ne ha scritta
una nuova; se scende, una e' stata resa.

💡 E la forma di `tcg.hsp` e' quella gia' vista in `item_func.hsp` (34a):
`tcg.hsp:2803` era **gia' reso** e i diciotto fratelli intorno no. Qualcuno
aveva toppato un caso per volta senza sapere che era una famiglia.
"""
import re
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')
BUILD = Path(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx')

# ⚠️ Nel sorgente HSP il backslash e' un escape dentro i letterali: una
#    virgoletta protetta NON chiude la stringa (vedi il docstring di
#    `estrai.py`). Una regex che si ferma alla prima virgoletta legge un solo
#    backslash e la riga sparisce dal conto: e' successo a `command.hsp:8073`.
_ASSEGNA = re.compile(r'\bbuff\s*=\s*"((?:[^"\\]|\\.)*)"')
_AGGIUNGE = re.compile(r'\bbuff\s*\+=\s*"((?:[^"\\]|\\.)*)"')
_LETTERE = re.compile(r'[A-Za-z]{2,}')
# un ramo di lingua: la' il letterale inglese e' gia' contato da `else_jp.py`
_RAMO = re.compile(r'\bif\s*\(\s*jp\s*\)|\bif\s*\(\s*en\s*\)|\belse\b')


def _spenta(riga: str) -> bool:
    return riga.lstrip().startswith(';')


trovate: list[dict] = []
for percorso in sorted(SORGENTE.glob('*.hsp')):
    righe = percorso.read_bytes().decode('cp932', 'replace').split('\n')
    build = (BUILD / percorso.name).read_bytes().decode('cp932', 'replace').split('\n')
    for i, riga in enumerate(righe, start=1):
        # con `lang()` sulla riga il testo passa dal dizionario: non e' nudo
        if 'lang(' in riga:
            continue
        for forma, quale in ((_ASSEGNA, '='), (_AGGIUNGE, '+=')):
            trovato = forma.search(riga)
            if not trovato:
                continue
            testo = trovato.group(1)
            # `buff = ""` azzera il corpo, `buff += "\n"` va a capo: non scrivono
            if not _LETTERE.search(testo):
                continue
            resa = ''
            if i - 1 < len(build):
                altro = forma.search(build[i - 1])
                if altro and altro.group(1) != testo:
                    resa = altro.group(1)
            trovate.append({
                'file': percorso.name, 'riga': i, 'testo': testo, 'forma': quale,
                'resa': resa, 'spenta': _spenta(riga),
                'ramo': any(_RAMO.search(righe[j])
                            for j in range(max(0, i - 7), i - 1)),
            })
            break

vive = [v for v in trovate if not v['spenta'] and not v['ramo']]
rese = [v for v in vive if v['resa']]
print(f"corpi di finestra con un inglese nudo, fuori da un ramo di lingua: {len(vive)}")
print(f"    gia' rese: {len(rese)}   |   ancora da fare: {len(vive) - len(rese)}")
print(f"    (escluse: {sum(1 for v in trovate if v['ramo'])} dentro un ramo di lingua "
      f"— materia di else_jp.py — e {sum(1 for v in trovate if v['spenta'])} righe spente)\n")

per_file: dict[str, list] = {}
for v in vive:
    per_file.setdefault(v['file'], []).append(v)
for nome, voci in sorted(per_file.items(), key=lambda x: -len(x[1])):
    da_fare = sum(1 for v in voci if not v['resa'])
    forme = ' '.join(sorted({v['forma'] for v in voci}))
    print(f'  {nome:<18} {len(voci):3d}   da fare {da_fare:3d}   forma {forme}')
print()

for v in sorted(vive, key=lambda v: (v['file'], v['riga'])):
    if v['resa']:
        continue
    print(f"  {v['file']}:{v['riga']}  [{v['forma']:>2}]  {v['testo'][:74]}")
