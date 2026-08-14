# I file del sorgente che hanno `lang()` e nessun file di dizionario.
#
# La domanda della 26ª — «esistono file che gli strumenti sanno leggere e che
# nessun elenco nomina?» — era stata chiusa con un no leggendo `SPEC.md`. La 34ª
# l'ha riaperta due volte in un'ora: `calculation.hsp` (44 lang(), la follia
# uscita in inglese a schermo) e `chips.hsp` (3 lang(), «a field si trova ai tuoi
# piedi»). Un elenco scritto a mano non e' una misura: questa lo e'.
import io, os, re, glob

SORG = r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx"
DIZ = r"C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana\dizionario"

righe = []
for path in sorted(glob.glob(os.path.join(SORG, "*.hsp"))):
    nome = os.path.basename(path)
    testo = io.open(path, encoding="cp932", errors="replace").read()
    quanti = len(re.findall(r"lang *\(", testo))
    if quanti == 0:
        continue
    jsonl = os.path.join(DIZ, nome + ".jsonl")
    if os.path.exists(jsonl):
        voci = sum(1 for l in io.open(jsonl, encoding="utf-8") if l.strip())
        righe.append((quanti, nome, voci, "in dizionario"))
    else:
        righe.append((quanti, nome, 0, "⚠️ FUORI"))

fuori = [r for r in righe if r[3] != "in dizionario"]
print(f"file con lang(): {len(righe)}   di cui senza dizionario: {len(fuori)}\n")
print("=== fuori da ogni elenco ===")
for quanti, nome, _, _ in sorted(fuori, reverse=True):
    print(f"  {quanti:>5} lang()   {nome}")
print(f"\n  totale lang() mai estratti: {sum(r[0] for r in fuori)}")
print("\n=== dentro, per riferimento ===")
for quanti, nome, voci, _ in sorted(righe, reverse=True):
    if (quanti, nome) in [(r[0], r[1]) for r in fuori]:
        continue
    print(f"  {quanti:>5} lang()   {nome:<28} {voci} voci in dizionario")
