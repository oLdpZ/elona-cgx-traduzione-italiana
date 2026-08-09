# strumenti/genera_toppe_casuali.py
"""Genera le toppe che ribaltano i nomi casuali degli oggetti non identificati.

    python -m strumenti.genera_toppe_casuali

`db_item.hsp` compone il nome che il giocatore legge **prima** di identificare
un oggetto cosi':

    iknownnameref(ITEM_ID_POTION_GEM) = _namepotion(p) + strblank + strpotion

cioe' aggettivo, spazio, nome — «a clear potion». In italiano l'aggettivo segue
il nome, e la sola strada e' scambiare i due addendi: «una pozione trasparente».
Non si puo' fare dal dizionario, perche' l'ordine sta nel codice e non nelle
stringhe, e non si puo' fare svuotando il nome di famiglia, perche' `_namering`
ne serve **due** (`strring` e `stramulet`).

I siti sono 213 e hanno tutti la stessa forma: si generano, non si scrivono.
Ogni riga porta il proprio `ITEM_ID`, quindi ognuna e' un aggancio unico, e
questo strumento rifiuta di emettere una toppa il cui blocco non compaia
esattamente una volta — la stessa regola di `genera_toppe_nomi`.

⚠️ Il genere e' una proprieta' dell'**array**, non della riga: `_namepotion`
serve solo pozioni, `_namespellbook` solo grimori. Le rese si accordano una
volta per famiglia. L'unica eccezione la risolve una toppa a mano su
`_namescroll`, perche' `mossy` e `old` hanno la stessa firma in due famiglie di
genere diverso.

⚠️ L'articolo non e' un terzo problema: la testa del nome vero e' la stessa
parola di famiglia (`ioriginalnameref2` vale `potion`, `spellbook`, …), quindi
`ioriginalnamearticolo` porta gia' l'articolo giusto anche per il nome casuale.

Da rilanciare a ogni versione CGX nuova, come il suo gemello: se upstream
aggiunge un oggetto a nome casuale, la toppa nuova esce da qui.
"""
import io
import json
import re
import sys

from strumenti import percorsi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
GENERATA = "casuali"
FILE = "db_item.hsp"

# aggettivo + spazio + nome -> nome + spazio + aggettivo
COMPOSIZIONE = re.compile(
    r"^(?P<ind>\s*)(?P<sinistra>iknownnameref\([A-Z0-9_]+\) = )"
    r"(?P<agg>_name\w+\(p\)) \+ strblank \+ (?P<nome>str\w+)\s*$"
)

righe = (percorsi.SORGENTE_HSP / FILE).read_bytes().decode("cp932").split("\r\n")

toppe = []
for riga in righe:
    m = COMPOSIZIONE.match(riga)
    if not m:
        continue
    girata = (
        f"{m['ind']}{m['sinistra']}{m['nome']} + strblank + {m['agg']}"
    )
    toppe.append({
        "file": FILE,
        "cerca": riga,
        "sostituisci": girata,
        "motivo": (
            f"nome casuale dell'oggetto non identificato: in inglese e' "
            f"aggettivo + nome ({m['agg']} + strblank + {m['nome']}), in "
            f"italiano l'aggettivo SEGUE il nome. L'ordine sta nel codice e non "
            f"nelle stringhe, quindi il dizionario non lo raggiunge. Il genere e' "
            f"una proprieta' dell'array, non della riga: {m['agg'][:-3]} serve una "
            f"famiglia sola e le rese si accordano una volta per tutte"
        ),
    })

for t in toppe:
    quante = sum(1 for r in righe if r == t["cerca"])
    if quante != 1:
        print(f"!! {quante} VOLTE !!  {t['cerca'].strip()}")
    assert quante == 1, t["cerca"]
    t["generata"] = GENERATA

famiglie = {}
for t in toppe:
    chiave = re.search(r"_name\w+", t["cerca"]).group(0)
    famiglie[chiave] = famiglie.get(chiave, 0) + 1
for k, v in sorted(famiglie.items()):
    print(f"ok         {k:16} {v:3} siti")

percorso = percorsi.PROGETTO / "toppe.jsonl"
esistenti = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
altre = [t for t in esistenti if t.get("generata") != GENERATA]
print(f"\naltre toppe: {len(altre)}, generate: {len(toppe)} "
      f"(ne sostituiscono {len(esistenti) - len(altre)})")
with percorso.open("w", encoding="utf-8", newline="\n") as f:
    for t in altre + toppe:
        f.write(json.dumps(t, ensure_ascii=False) + "\n")
print("scritto", percorso)
