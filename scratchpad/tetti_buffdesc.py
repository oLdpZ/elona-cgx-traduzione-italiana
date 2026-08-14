# I tetti dei `buffdesc`, uno per sito, italiano contro inglese di monte.
#
# `*skill_desc` (command.hsp:9004) compone `dur + "t " + buffdesc`, e la riga
# viene tagliata in QUATTRO posti con TRE misure diverse:
#
#   command.hsp:5389  *com_applySkill_loop        34   menu `a`
#   command.hsp:5599  *com_applyWideSkill_loop    34   menu `W`
#   command.hsp:8851  *com_spell_loop             40   menu di lancio
#   command.hsp:10996 *com_charainfo_loop_WHILE1  46   scheda, pagina incantesimi
#
# ⚠️ La ripresa ne registrava uno solo (34). Il conto della 33ª — «46 inglesi su
# 63 sfondano gia'» — vale per quel tetto, non per gli altri due.
import io, re

BUILD = r"C:\Games\Elona\_traduzione\build\2.05-custom-gx\buff.hsp"
SORG = r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\buff.hsp"

PREFISSO = 4  # "25t ": due cifre di durata, la `t` e lo spazio
TETTI = (34, 40, 46)


def ramo_inglese(riga):
    """Il secondo argomento di lang(), con le variabili ridotte a due cifre."""
    m = re.search(r"buffdesc\s*=\s*lang\((.*)\)\s*$", riga)
    if not m:
        return None
    corpo = m.group(1)
    # separa i due argomenti al livello di parentesi zero
    prof = 0
    dentro = False
    taglio = None
    for i, c in enumerate(corpo):
        if c == '"':
            dentro = not dentro
        elif not dentro:
            if c == "(":
                prof += 1
            elif c == ")":
                prof -= 1
            elif c == "," and prof == 0:
                taglio = i
                break
    if taglio is None:
        return None
    en = corpo[taglio + 1:]
    # i pezzi letterali si sommano; ogni espressione fra un pezzo e l'altro
    # e' un numero, che a schermo occupa due o tre cifre
    pezzi = re.findall(r'"((?:[^"\\]|\\.)*)"', en)
    variabili = en.count("+") - (len(pezzi) - 1 if pezzi else 0)
    return "".join(pezzi) + "NN" * max(0, variabili)


def buffdesc(path):
    """Rende {BUFF_X: testo} leggendo il file."""
    righe = io.open(path, encoding="cp932", errors="replace").read().split("\n")
    fuori = {}
    corrente = None
    for riga in righe:
        m = re.search(r"calcbuff_buffid\s*==\s*(BUFF_\w+)", riga)
        if m:
            corrente = m.group(1)
        if "buffdesc" in riga and "lang(" in riga:
            t = ramo_inglese(riga)
            if t is not None and corrente:
                fuori.setdefault(corrente, t)
    return fuori


it = buffdesc(BUILD)
en = buffdesc(SORG)

print(f"buffdesc misurati: {len(it)} italiani, {len(en)} inglesi\n")
for tetto in TETTI:
    budget = tetto - PREFISSO
    sfonda_it = sorted((len(v) - budget, k, v) for k, v in it.items() if len(v) > budget)
    sfonda_en = [k for k, v in en.items() if len(v) > budget]
    print(f"=== tetto {tetto} (budget {budget} al buffdesc) ===")
    print(f"    italiano {len(sfonda_it)}/{len(it)}   inglese {len(sfonda_en)}/{len(en)}")
    if tetto != 34:
        for extra, k, v in sfonda_it[-8:]:
            print(f"    +{extra:<3} {k:<28} {v[:budget]}|{v[budget:][:16]}")
    print()

print("=== dove il taglio cade dentro una parola (tetto 40) ===")
budget = 40 - PREFISSO
for k, v in sorted(it.items()):
    if len(v) <= budget:
        continue
    if v[budget - 1].isalpha() and v[budget].isalpha():
        print(f"    {k:<28} …{v[max(0,budget-14):budget]}|{v[budget:][:12]}")
