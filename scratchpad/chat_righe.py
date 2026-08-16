# -*- coding: utf-8 -*-
"""Referto: quante righe occupa una descrizione nella finestra della
chiacchierata, e quante ce ne stanno prima dei bottoni.

⭐ **Nato nella 54ª, per il negozio delle carte** (`tcg_custom.hsp`). Le 28
descrizioni dei mazzi non passano da nessun menu: finiscono in `buff` e le
disegna la finestra del dialogo, che nessuno degli strumenti misura.
`larghezze.py` guarda i menu di `*prompt_key`, `diario.py` il diario,
`riquadri.py` le piastrelle: la finestra del dialogo era scoperta.

**Il tetto viene da tre righe del sorgente, non da un'occhiata:**

    chat.hsp:25226   talk_conv buff, 56 - en * 3      l'a capo: 53 caratteri
    chat.hsp:25725   repeat noteinfo(0)               le disegna TUTTE
    chat.hsp:25728   y = wy + 43 + cnt * 19           la prima a 43, passo 19
    chat.hsp:25161   y = wy + wh - 56 - keyrange * 19 i bottoni, dal basso

Con `wh = 380` il primo bottone sta a `324 - opzioni * 19`. Il testo puo'
arrivare fin dove comincia il primo bottone: con **due** opzioni — che e' il
caso del negozio, «prendi i biglietti» e «non ho abbastanza» — il primo bottone
e' a 286 e l'ultima riga di testo che ci sta tutta e' la **dodicesima**
(43 + 19*11 + 19 = 271 ≤ 286). Con una sola opzione le righe diventano 13.

⚠️ **`talk_conv` non e' un `textwrap`**, e le differenze contano:
- taglia sugli **spazi** (`instr(msgtemp, 0, " ")`), quindi una parola piu'
  lunga della larghezza **sfonda** la riga invece di spezzarsi;
- la coda dopo l'ultimo spazio non viene mai spezzata (`+= msgtemp` alla fine);
- il `\\n` esplicito manda a capo, ma solo se cade **prima** del prossimo
  spazio; e se la riga era gia' piena il `\\n` viene consumato **due volte**
  (una per chiudere la riga, una per se stesso), che e' come nascono le righe
  vuote nella finestra.

Uso:
    python scratchpad/chat_righe.py            # sorgente e build, tutte
    python scratchpad/chat_righe.py --solo-fuori
"""
import argparse
import io
import re
import sys
from pathlib import Path

LARGHEZZA = 53          # 56 - en * 3, con en = 1
CAP_2_OPZIONI = 12      # (324 - 2*19 - 43) // 19 = 12
CAP_1_OPZIONE = 13

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx')
BUILD = Path(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx')


def talk_conv(testo: str, larghezza: int = LARGHEZZA) -> list:
    """Replica esatta del ramo inglese di `init.hsp:1326`-`:1368`.

    Restituisce le righe come le disegna `chat.hsp:25725`.
    """
    msg = testo
    righe = []
    corrente = ''
    for _ in range(1000):
        lung = 0
        p = -1
        for _ in range(1000):
            i = msg.find(' ')
            p = 0 if i < 0 else i + 1
            if p == 0:
                break
            j = msg.find('\n')
            nl = 0 if j < 0 else j + 1
            if nl != 0 and nl < p:
                if lung + nl > larghezza:
                    righe.append(corrente)
                    corrente = ''
                    break
                corrente += msg[:nl - 1]
                righe.append(corrente)
                corrente = ''
                lung += nl
                msg = msg[nl:]
                break
            if lung + p > larghezza:
                righe.append(corrente)
                corrente = ''
                break
            corrente += msg[:p]
            lung += p
            msg = msg[p:]
        if p == 0:
            break
    corrente += msg
    righe.append(corrente)
    return righe


LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
DESC = re.compile(r'^\s*cardsetdesc@tcg\([^)]*\)\s*=\s*(.*)$')


def descrizioni(percorso: Path) -> list:
    fuori = []
    righe = io.open(percorso, encoding='cp932').read().split('\n')
    for n, riga in enumerate(righe, 1):
        m = DESC.match(riga)
        if not m:
            continue
        l = LANG.search(m.group(1))
        if not l:
            continue
        testo = l.group(2).replace('\\n', '\n').replace("\\'", "'").replace('\\"', '"')
        fuori.append((n, testo))
    return fuori


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--solo-fuori', action='store_true')
    ap.add_argument('--cap', type=int, default=CAP_2_OPZIONI)
    args = ap.parse_args()

    esito = 0
    for nome, radice in (('SORGENTE', SORGENTE), ('BUILD', BUILD)):
        percorso = radice / 'tcg_custom.hsp'
        if not percorso.exists():
            print(f'{nome}: {percorso} non c\'e\'')
            continue
        voci = descrizioni(percorso)
        fuori = 0
        print(f'\n=== {nome} — {len(voci)} descrizioni, tetto {args.cap} righe')
        for n, testo in voci:
            righe = talk_conv(testo, LARGHEZZA)
            larga = max((len(r) for r in righe), default=0)
            male = len(righe) > args.cap
            if male:
                fuori += 1
                esito = 1
            if args.solo_fuori and not male:
                continue
            segno = '⚠️' if male else '  '
            print(f'{segno} :{n:5d}  {len(righe):3d} righe, la piu\' larga {larga:3d} car.')
            if male:
                for i, r in enumerate(righe):
                    marca = '<<<' if i >= args.cap else '   '
                    print(f'          {i+1:3d} {marca} {r}')
        print(f'--- {nome}: {fuori} fuori misura su {len(voci)}')
    return esito


if __name__ == '__main__':
    sys.exit(main())
