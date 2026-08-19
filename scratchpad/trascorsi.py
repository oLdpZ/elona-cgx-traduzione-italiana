"""Il tetto delle cinque righe dei trascorsi, nella finestra della creazione.

RETE 17. `chara.hsp:3305` disegna la finestra dei trascorsi larga **360** px e ci
scrive le cinque righe con `pos wx + 75` e un `mes`, che non taglia e non va a
capo: passata la larghezza il testo esce dal bordo destro della pergamena, sul
marmo nudo.

    display_window (windoww - 360) / 2 + inf_screenx, ..., 360, 352
    pos wx + 75, wy + 200 + i * 15
    mes s

Il carattere e' quello lasciato dal giro precedente del ciclo -- `font ..., 15 -
en * 2, 1`, cioe' **13** in inglese -- e avanza **7 px** per carattere, misurato
sulla schermata della 64a: la riga da 46 caratteri va da x=858 a x=1176, 318 px.

    tetto = (360 - 75 - CORNICE) / 7

Le cinque righe vengono da cinque blocchi di `command.hsp` (`*setHistory1..5`),
una `lang()` per ogni valore di `ohanasi<n>`.

⚠️ Provato prima sull'inglese di monte, come vuole la 61a. Qui l'inglese NON
tocca il tetto: lo sfonda, e di parecchio. La finestra e' dimensionata sul
giapponese (14 px per carattere, ma frasi da 14 caratteri) e upstream ci ha
messo dentro un inglese che non ci sta. Vedi il conto stampato in fondo.
"""
import re
import sys
from pathlib import Path

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx")
BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx")

LARGHEZZA = 360
SINISTRA = 75
CORNICE = 15
PASSO = 7
TETTO = (LARGHEZZA - SINISTRA - CORNICE) // PASSO

BLOCCHI = [
    ("setHistory1", 9454, 9595),
    ("setHistory2", 9595, 9733),
    ("setHistory3", 9733, 9871),
    ("setHistory4", 9871, 10009),
    ("setHistory5", 10009, 10145),
]

LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')


def righe(albero):
    testo = (albero / "command.hsp").read_text(encoding="cp932", errors="replace")
    linee = testo.splitlines()
    fuori = []
    for nome, da, a in BLOCCHI:
        for n in range(da, min(a, len(linee))):
            m = LANG.search(linee[n - 1])
            if m:
                fuori.append((nome, n, m.group(2)))
    return fuori


def referto():
    print(f"tetto: ({LARGHEZZA} - {SINISTRA} - {CORNICE}) / {PASSO} = {TETTO} caratteri")
    for etichetta, albero in (("inglese di monte", SORGENTE), ("build italiana", BUILD)):
        voci = righe(albero)
        fuori = [(b, n, t) for b, n, t in voci if len(t) > TETTO]
        print(f"\n--- {etichetta}: {len(voci)} righe, {len(fuori)} fuori misura")
        for b, n, t in sorted(fuori, key=lambda v: -len(v[2]))[:12]:
            print(f"   {len(t):3d}  ({len(t) - TETTO:+3d})  {b}:{n}  {t}")
        if len(fuori) > 12:
            print(f"   ... e altre {len(fuori) - 12}")
        if voci:
            print(f"   la piu' lunga: {max(len(t) for _, _, t in voci)} caratteri")


if __name__ == "__main__":
    referto()
