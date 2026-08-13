# Referto: i rami `else` di `if ( jp )` con letterali inglesi nudi.
# blocchi_en.py cerca `if ( en )`; questa forma gli sfugge.
import io, glob, os, re

BASE = r"C:\Games\Elona\_traduzione\build\2.05-custom-gx"
SORG = r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"


def blocchi(path):
    """Rende (riga_else, righe) per ogni `else` che segue un blocco `if ( jp )`."""
    L = io.open(path, encoding="cp932", errors="replace").read().split("\n")
    out = []
    for i, l in enumerate(L):
        if not re.match(r"\s*if \( jp \) \{", l):
            continue
        depth = 0
        for k in range(i, len(L)):
            depth += L[k].count("{") - L[k].count("}")
            if depth == 0 and k > i:
                break
        else:
            continue
        # il ramo else deve cominciare sulla riga della graffa che chiude, o subito dopo
        m = None
        for cand in (k, k + 1):
            if cand < len(L) and re.search(r"\belse\b", L[cand]):
                m = cand
                break
        if m is None:
            continue
        depth = 0
        corpo = []
        for k2 in range(m, len(L)):
            depth += L[k2].count("{") - L[k2].count("}")
            if k2 > m:
                corpo.append((k2 + 1, L[k2]))
            if depth == 0 and k2 > m:
                break
        out.append((m + 1, corpo))
    return out


def testo_nudo(riga):
    """Vero se la riga porta un letterale fuori da lang()."""
    if '"' not in riga:
        return False
    senza = re.sub(r"lang\(.*?\)", "", riga)
    for lit in re.findall(r'"((?:[^"\\]|\\.)*)"', senza):
        if re.search(r"[A-Za-z]{3}", lit):
            return True
    return False


tot_righe = tot_file = 0
for path in sorted(glob.glob(os.path.join(BASE, "*.hsp"))):
    nome = os.path.basename(path)
    righe = []
    for _, corpo in blocchi(path):
        for n, l in corpo:
            if testo_nudo(l):
                righe.append((n, l.strip()))
    if not righe:
        continue
    # intatte = identiche al sorgente pinnato
    orig = io.open(os.path.join(SORG, nome), encoding="cp932", errors="replace").read().split("\n")
    intatte = sum(1 for n, l in righe if n <= len(orig) and orig[n - 1].strip() == l)
    tot_file += 1
    tot_righe += len(righe)
    print(f"=== {nome}: {len(righe)} righe, {intatte} ancora intatte")
    for n, l in righe[:6]:
        print(f"    {n} | {l[:150]}")
    if len(righe) > 6:
        print(f"    ... e altre {len(righe) - 6}")
print(f"--- else-di-jp: {tot_righe} righe in {tot_file} file")
