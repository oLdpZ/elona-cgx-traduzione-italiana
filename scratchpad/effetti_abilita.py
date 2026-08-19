"""Il tetto della colonna «Effetto» nella lista delle abilita'.

RETE 18. `command.hsp:10406` apre la finestra della lista abilita' larga **700**
px e scrive la descrizione a `pos wx + 330`; il `mes` non taglia e non va a capo,
quindi passata la larghezza il testo esce dal bordo destro della pergamena.

    display_window2 (windoww - 700) / 2 + inf_screenx, ..., 700, 400, 7
    pos wx + 330, wy + 66 + cnt * 19 + 2

    tetto = (700 - 330 - CORNICE) / 7 = 52 caratteri

⚠️ **Il tetto qui e' MISURATO, non dedotto**, e l'inglese di monte non fa da
prova come nella 63a: upstream sfora di suo su sei voci, fino a 56 caratteri.
Vale quindi la misura diretta sulla schermata della 64a: la finestra va da x=607
a x=1307, la colonna «Effetto» comincia a x=938 (cioe' wx+331) e la riga da 59
caratteri arriva a x=1342, il che da' **6,85 px per carattere**. Dal bordo:
(1307 - 938) / 6,85 = **53,9 caratteri toccano il bordo esterno** della
pergamena, e la cornice ne mangia uno o due. Da qui 52.

⭐ Il fatto certo non e' il tetto al carattere, e' lo sfondamento: la nostra
«Memorizza incantesimi. Migliora pergamene. Analizza nemici.» (59) si vede
uscire dalla pergamena di **35 px**, sul marmo nudo, nella schermata della 64a.

Misura `skilldesc`, che e' la colonna «Effetto» della lista. `skillencdesc` e'
un'altra cosa (la riga degli incantamenti) e non passa di qui.
"""
import re
from pathlib import Path

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx")
BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx")

LARGHEZZA = 700
COLONNA = 330
CORNICE = 13
PASSO = 7
TETTO = (LARGHEZZA - COLONNA - CORNICE) // PASSO

RIGA = re.compile(
    r'skilldesc\((\w+)\)\s*=\s*lang\(\s*"(?:[^"\\]|\\.)*"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)'
)


def voci(albero):
    testo = (albero / "skill.hsp").read_text(encoding="cp932", errors="replace")
    fuori = []
    for n, linea in enumerate(testo.splitlines(), 1):
        m = RIGA.search(linea)
        if m and m.group(2):
            fuori.append((n, m.group(1), m.group(2)))
    return fuori


def referto():
    print(f"tetto: ({LARGHEZZA} - {COLONNA} - {CORNICE}) / {PASSO} = {TETTO} caratteri")
    for etichetta, albero in (("inglese di monte", SORGENTE), ("build italiana", BUILD)):
        v = voci(albero)
        fuori = [x for x in v if len(x[2]) > TETTO]
        piu_lunga = max(v, key=lambda x: len(x[2])) if v else None
        print(f"\n--- {etichetta}: {len(v)} descrizioni, {len(fuori)} fuori misura")
        for n, chiave, t in sorted(fuori, key=lambda x: -len(x[2])):
            print(f"   {len(t):3d}  ({len(t) - TETTO:+3d})  skill.hsp:{n}  {t}")
        if piu_lunga:
            print(f"   la piu' lunga: {len(piu_lunga[2])} caratteri  ({piu_lunga[1]})")


if __name__ == "__main__":
    referto()
