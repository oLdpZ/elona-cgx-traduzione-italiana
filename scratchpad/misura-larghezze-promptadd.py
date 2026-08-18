# scratchpad/misura-larghezze-promptadd.py
"""Quanto vale il punto cieco di `larghezze.py` (rete 5): i menu fuori da text.hsp.

`larghezze.py` misura solo `text.hsp`, e ci arriva per una strada indiretta: i
`#deffunc txtset*` riempiono `s(cnt)`, il chiamante fa `promptAdd s(cnt)` e poco
sotto dichiara il riquadro con `val = promptx, prompty, W`.

Ma un menu si puo' scrivere anche **senza** passare da text.hsp: una corsa di
`promptAdd lang(...)` diretti, chiusa dallo stesso `val = ...` e dallo stesso
`gosub *prompt_key`. Stesso riquadro, stesso carattere (`15 - en * 2` = 13,
`system.hsp:4259`), stesso taglio -- e nessuna rete che lo guardi.

## Il metro sta in *prompt_key, non nel nome dei parametri

    system.hsp:4272   sx = val - val(2) / 2          val   = x
    system.hsp:4273   sy = val(1) - promptmax * 10   val(1)= y
    system.hsp:4275   gfini val(2) - 17, ...         val(2)= LARGHEZZA

Quindi la larghezza e' il **terzo campo**, comunque siano scritti i primi due:
`promptx, prompty, 300` ma anche `promptx, 240, 160` (chara.hsp) e
`basex@tcg + 420, basey@tcg + 230, 200` (tcg.hsp). ⚠️ E ci sono `val =` a
cinque campi che non sono riquadri affatto (`winposy(90), 12, 1, 0`): per questo
il referto parte da `gosub *prompt_key` e cammina **all'indietro**, invece di
fidarsi della forma del `val =`.

⚠️ La larghezza puo' dipendere dalla lingua in tutt'e due i versi: `450 - 50 * en`
(400 in inglese) ma anche `280 + (en * 140)` (420 in inglese). La build e' quella
inglese, cioe' `en = 1`.

Questo referto non tocca niente: misura e basta.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi
from strumenti.larghezze import MARGINE, PIXEL_PER_CARATTERE, budget, reso

_ADD = re.compile(r"\bpromptAdd\s+(.+?)\s*$")
_LANG = re.compile(r"\blang\s*\(")
_PROMPT_KEY = re.compile(r"gosub\s+\*prompt_key\b")
_VAL = re.compile(r"^\s*val\s*=\s*(.+?)\s*$")
_NUMERO = re.compile(r"^[\d\s+\-*/()]+$")

# quanto indietro si cerca il `val =` che dichiara il riquadro
FINESTRA = 400


def righe(percorso: Path) -> list[str]:
    return percorso.read_bytes().decode("cp932", "replace").split("\n")


def campi(espressione: str) -> list[str]:
    """Spezza `a, b(c, d), e` sulle virgole di primo livello."""
    fuori, corrente, prof = [], "", 0
    for c in espressione:
        if c in "([":
            prof += 1
        elif c in ")]":
            prof -= 1
        if c == "," and prof == 0:
            fuori.append(corrente)
            corrente = ""
        else:
            corrente += c
    fuori.append(corrente)
    return fuori


def larghezza(campo: str) -> int | None:
    """Il terzo campo valutato nella build inglese (`en = 1`), se e' un numero."""
    testo = re.sub(r"\ben\b", "1", campo).strip()
    if not _NUMERO.match(testo):
        return None
    try:
        valore = eval(testo, {"__builtins__": {}}, {})
    except Exception:
        return None
    return int(valore) if isinstance(valore, (int, float)) else None


def menu_del_file(percorso: Path):
    """[(riga_di_prompt_key, pixel|None, [(riga, argomento)])] per ogni menu."""
    fuori = []
    linee = righe(percorso)
    confine = 0  # dove finisce il menu precedente
    for i, riga in enumerate(linee):
        if not _PROMPT_KEY.search(riga):
            continue
        px = None
        for j in range(i - 1, max(confine, i - FINESTRA) - 1, -1):
            m = _VAL.match(linee[j])
            if m:
                pezzi = campi(m.group(1))
                if len(pezzi) >= 3:
                    px = larghezza(pezzi[2])
                break
        voci = []
        for j in range(max(confine, i - FINESTRA), i):
            if linee[j].lstrip().startswith(";"):
                continue
            m = _ADD.search(linee[j])
            if m:
                voci.append((j + 1, m.group(1)))
        fuori.append((i + 1, px, voci))
        confine = i + 1
    return fuori


def dizionario_per_riga(nome_file: str) -> dict[int, list[dict]]:
    percorso = percorsi.DIZIONARIO / (nome_file + ".jsonl")
    fuori: dict[int, list[dict]] = {}
    if not percorso.exists():
        return fuori
    for linea in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(linea)
        fuori.setdefault(voce["riga"], []).append(voce)
    return fuori


def main() -> int:
    sorgente = percorsi.SORGENTE_HSP
    tot = dict(menu=0, senza_px=0, voci=0, lang=0, rese=0, sfori=0, sfori_en=0)
    sfori: list[tuple] = []
    senza_dizionario: dict[str, int] = {}
    senza_px: list[tuple[str, int, int]] = []

    print("%-26s %5s %7s %6s %6s %5s %6s"
          % ("file", "menu", "no px", "voci", "lang()", "rese", "sfori"))
    for percorso in sorted(sorgente.glob("*.hsp")):
        menu = menu_del_file(percorso)
        if not menu:
            continue
        diz = dizionario_per_riga(percorso.name)
        n = dict(senza_px=0, voci=0, lang=0, rese=0, sfori=0)
        for riga_pk, px, voci in menu:
            if px is None:
                n["senza_px"] += 1
                senza_px.append((percorso.name, riga_pk, len(voci)))
                continue
            tetto = budget(px)
            for riga, arg in voci:
                n["voci"] += 1
                if not _LANG.search(arg):
                    continue
                n["lang"] += 1
                for voce in diz.get(riga, []):
                    testo = reso(voce.get("it") or "")
                    if not testo:
                        continue
                    n["rese"] += 1
                    if len(testo) > tetto:
                        n["sfori"] += 1
                        en = reso(voce.get("en_grezzo") or voce.get("en") or "")
                        if len(en) > tetto:
                            tot["sfori_en"] += 1
                        sfori.append((percorso.name, riga, px, tetto,
                                      len(testo), testo, len(en), en))
        if n["lang"] and not diz:
            senza_dizionario[percorso.name] = n["lang"]
        tot["menu"] += len(menu)
        for chiave in n:
            tot[chiave] += n[chiave]
        print("%-26s %5d %7d %6d %6d %5d %6d"
              % (percorso.name, len(menu), n["senza_px"], n["voci"],
                 n["lang"], n["rese"], n["sfori"]))

    print("\n%-26s %5d %7d %6d %6d %5d %6d"
          % ("TOTALE", tot["menu"], tot["senza_px"], tot["voci"],
             tot["lang"], tot["rese"], tot["sfori"]))
    print("di cui rotte anche in inglese: %d" % tot["sfori_en"])
    print("passo del carattere: %s px, margine %d px"
          % (PIXEL_PER_CARATTERE, MARGINE))

    if senza_px:
        print("\nmenu di cui NON si e' trovata la larghezza:")
        for nome, riga, quante in senza_px:
            print("   %-16s:%-6d  %d voci" % (nome, riga, quante))

    if senza_dizionario:
        print("\nfile con voci di menu e NESSUN dizionario:")
        for nome, quante in sorted(senza_dizionario.items()):
            print("   %-24s %4d voci lang()" % (nome, quante))

    if sfori:
        print("\nle voci fuori misura:")
        for nome, riga, px, tetto, n_it, testo, n_en, en in sorted(sfori):
            print("   %-14s:%-6d %3dpx tetto %2d" % (nome, riga, px, tetto))
            print("        it %3d  %s" % (n_it, testo))
            print("        en %3d  %s" % (n_en, en))
    return 0


if __name__ == "__main__":
    sys.exit(main())
