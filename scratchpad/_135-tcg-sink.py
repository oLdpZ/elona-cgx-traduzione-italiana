"""Le stringhe di `tcg_skill.hsp` divise per SINK: dove finisce ognuna.

Non basta sapere che sono 142: una parte va a schermo, una parte e' chiave di
confronto (tradurla rompe il gioco) e una parte e' traccia di debug. Il
progetto ha gia' pagato questa distinzione una volta, con `strmale` in
`text.hsp`: la stessa stringa era etichetta a schermo E operando di confronto
contro il salvataggio, e ci e' voluta una toppa sulla sola riga di display.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import copertura, percorsi

SINK = [
    # (nome, regex sulla riga, va a schermo?)
    ("scheda carta",   re.compile(r"carddetail\w*@tcg\([^)]*\)\s*(\+?=)"), True),
    ("battuta",        re.compile(r"efllistaddchat\w*\s"), True),
    ("cnvtalk",        re.compile(r"cnvtalk\("), True),
    ("randomchat",     re.compile(r"randomchat@tcg\s*="), True),
    ("dialogo manytia", re.compile(r"manytiadialog@tcg\s*="), True),
    ("tag carta",      re.compile(r"cardn@tcg\(TCG_CARDN_REF_TAG"), True),
    ("markerwords",    re.compile(r"markerwords\s*="), True),
    ("debug proctcg",  re.compile(r"^\s*proctcg\s"), False),
    ("chiave razza",   re.compile(r"TCG_CARDN_REF_RACE|rndrace@tcg|racebk@tcg"), False),
    ("chiave sesso",   re.compile(r"TCG_CARDN_REF_SEX|rndsex@tcg"), False),
]


def main() -> None:
    percorso = percorsi.SORGENTE_HSP / "tcg_skill.hsp"
    testo = percorso.read_bytes().decode("cp932")

    per_sink = defaultdict(list)
    non_classificate = []
    for n, riga in enumerate(testo.split("\n"), 1):
        spoglia = riga.lstrip()
        if spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        letterali = [m.group(1) for m in copertura._LETTERALE.finditer(riga)
                     if copertura._PROSA.search(m.group(1))]
        if not letterali:
            continue
        for nome, regex, schermo in SINK:
            if regex.search(riga):
                per_sink[(nome, schermo)].extend((n, s) for s in letterali)
                break
        else:
            non_classificate.append((n, riga.strip()[:110], letterali))

    print("  SINK                    righe  distinte  a schermo")
    print("  " + "-" * 52)
    totale_schermo = set()
    for (nome, schermo), voci in sorted(per_sink.items(), key=lambda kv: -len(kv[1])):
        distinte = {s for _, s in voci}
        print(f"  {nome:<22} {len(voci):>6} {len(distinte):>9}  {'SI' if schermo else 'no':>9}")
        if schermo:
            totale_schermo |= distinte

    print(f"\n  DA TRADURRE (distinte, a schermo): {len(totale_schermo)}")

    if non_classificate:
        print(f"\n  ⚠️ righe non classificate: {len(non_classificate)}")
        for n, riga, letterali in non_classificate:
            print(f"     :{n}  {riga}")

    # il vincolo che va misurato prima di scrivere una resa
    print("\n  --- OPERANDI CERCATI DENTRO IL TESTO DELLE CARTE ---")
    for m in re.finditer(r'instr\(carddetail\w*@tcg[^,]*,\s*0,\s*"([^"]*)"', testo):
        print(f"     instr(...card..., {m.group(1)!r})  <- la resa deve contenerlo")

    # e le righe piu' alte, perche' un {txt} ha un soffitto e una carta pure
    print("\n  --- ALTEZZA DELLE SCHEDE (righe separate da \\n) ---")
    altezze = Counter()
    for s in totale_schermo:
        altezze[s.count("\\n") + 1] += 1
    for h in sorted(altezze):
        print(f"     {h} righe: {altezze[h]} stringhe")


if __name__ == "__main__":
    main()
