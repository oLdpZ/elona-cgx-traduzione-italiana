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

⚠️⚠️ **L'articolo E' un terzo problema, e fino al 2026-09-03 questa
intestazione diceva di no.** Diceva: «la testa del nome vero e' la stessa parola
di famiglia, quindi `ioriginalnamearticolo` porta gia' l'articolo giusto anche
per il nome casuale». E' vero su 208 oggetti su 213, e **falso su cinque**:

    ITEM_ID_ACIDPROOF_LIQUID   «liquido antiacido» (un )  ma ignoto e' «pozione …»
    ITEM_ID_FIREPROOF_LIQUID   idem
    ITEM_ID_POISON             idem
    ITEM_ID_SLEEPING_DRUG      idem
    ITEM_ID_NECK_GUARD         «gorgiera» (una )         ma ignoto e' «amuleto …»

Il nome vero di quei cinque **non e'** una pozione ne' un amuleto: e' un
liquido, un veleno, un farmaco, una gorgiera. La coincidenza su cui l'articolo
si appoggiava non e' una regola, e chi ci si appoggia scrive «un pozione
torbida» e «una amuleto d'ambra».

Percio' adesso l'articolo del nome casuale **si emette**, per tutti e 213 e non
per i cinque: si deriva dalla parola di famiglia, che e' la testa vera del
sintagma, e finisce in `iknownnamearticolo`/`iknownnamearticolodet`, che
`item_func.hsp` legge proprio li'. Niente piu' coincidenze da verificare.

ⓘ Il genere delle sei parole sta qui sotto in `GENERI`, perche' il genere e'
l'unica cosa che non si deduce (`articolo.py`). La **parola** invece si legge
dal dizionario per firma: se un giorno «pozione» diventasse «ampolla»,
l'articolo la seguirebbe da solo.

Da rilanciare a ogni versione CGX nuova, come il suo gemello: se upstream
aggiunge un oggetto a nome casuale, la toppa nuova esce da qui.
"""
import io
import json
import re
import sys

from strumenti import percorsi
from strumenti.articolo import articoli
from strumenti.reimporta import carica_dizionario

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
GENERATA = "casuali"
FILE = "db_item.hsp"

# Le sei parole di famiglia: la variabile HSP, la firma della sua resa in
# `text.hsp` (:184-:189) e il **genere**, che e' l'unica cosa da dichiarare.
# La parola si legge dal dizionario, l'articolo lo deriva `articolo.py`.
GENERI = {
    "stramulet":    ("94efdfa9a0a88c587b3d402a808bdf7736a78401", "m"),
    "strring":      ("27ec642f813c9dab15b1b9441c2944672a85b02c", "m"),
    "strpotion":    ("025ce284f2ee32bae292cd8e6d75de15906c5d55", "f"),
    "strspellbook": ("b64a84337ca9f20b80fa38263bc0df48a5798175", "m"),
    "strscroll":    ("d50a7b89f3c4110a8a3442914c17a1ab29aa378e", "f"),
    "strstaff":     ("a6433b437a8e5b809530c843d72744a82594e79b", "f"),
}

TESTO = carica_dizionario("text.hsp")


def articolo_di_famiglia(variabile):
    """(indeterminativo, determinativo) della parola di famiglia.

    ⚠️ Se la resa manca dal dizionario ci si ferma: un articolo calcolato sulla
    stringa vuota sarebbe `("", "")`, cioe' un ripiego sull'inglese scritto da
    noi invece che ereditato — la cosa che questo giro sta togliendo di mezzo.
    """
    firma, genere = GENERI[variabile]
    voce = TESTO.get(firma)
    if voce is None or not voce.get("it"):
        raise ValueError(
            f"{variabile}: la resa della parola di famiglia manca dal "
            f"dizionario (firma {firma[:12]}, text.hsp). Senza la parola "
            f"l'elisione non si puo' calcolare e l'articolo verrebbe vuoto."
        )
    return articoli(genere, voce["it"]), voce["it"]

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
    oggetto = re.search(r"iknownnameref\(([A-Z0-9_]+)\)", riga).group(1)
    (indeterminativo, determinativo), parola = articolo_di_famiglia(m["nome"])
    toppe.append({
        "file": FILE,
        "cerca": riga,
        "sostituisci": [
            girata,
            f'{m["ind"]}iknownnamearticolo({oggetto}) = "{indeterminativo}"',
            f'{m["ind"]}iknownnamearticolodet({oggetto}) = "{determinativo}"',
        ],
        "motivo": (
            f"nome casuale dell'oggetto non identificato: in inglese e' "
            f"aggettivo + nome ({m['agg']} + strblank + {m['nome']}), in "
            f"italiano l'aggettivo SEGUE il nome. L'ordine sta nel codice e non "
            f"nelle stringhe, quindi il dizionario non lo raggiunge. Il genere e' "
            f"una proprieta' dell'array, non della riga: {m['agg'][:-3]} serve una "
            f"famiglia sola e le rese si accordano una volta per tutte. "
            f"⭐ Le due righe dell'articolo sono nate il 2026-09-03: la testa del "
            f"sintagma qui e' «{parola}», non il nome vero. Appoggiarsi a "
            f"`ioriginalnamearticolo`, come faceva questo strumento fino a ieri, "
            f"sbagliava su cinque oggetti su 213 — ITEM_ID_ACIDPROOF_LIQUID e' "
            f"«liquido antiacido», maschile, ma da non identificato e' una "
            f"pozione. L'articolo si emette per tutti e 213, non per i cinque: "
            f"una coincidenza che regge sul 97% non e' una regola"
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
