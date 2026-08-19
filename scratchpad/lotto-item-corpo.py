# -*- coding: utf-8 -*-
"""Compone lavoro/fase4-item-004.jsonl: i cibi che cambiano il corpo.

`item.hsp:4066`-`:4217`. Quarto lotto: invecchiare di colpo, tornare
all'infanzia, la zuppa del paese delle meraviglie, la carne proibita che cambia
il sesso, il cibo avvelenato e quello drogato d'amore.

⚠️⚠️ **SEI VOCI RESTANO INGLESI, ED E' UNA DECISIONE, NON UNA DIMENTICANZA.**
`male`, `female`, `male?`, `female?`, `hermaphrodite`, `none` non sono
etichette: sono i **valori** di `cdatan(CDATAN_NEWSEX, cc)`, che questo blocco
scrive (`:4118`, `:4122`, `:4128`…) e insieme **confronta** (`:4116`, `:4139`,
`:4163`, `:4170`), e che altri file confrontano a loro volta
(`command.hsp:3639`-`:3654`, `text.hsp:123`, `:359`, `:371`). Tradurne uno solo
scollega la scrittura dalla rilettura. Stanno gia' tutti e sei in
`invariati.md:459`-`:466`, dichiarati dalla 48a. E' la regola generale delle
convenzioni: **quel che serve a un CONFRONTO non e' testo, e si guarda il sito.**
A schermo ci arrivano per toppa, non da qui.

⚠️ NIENTE NOMI NE' AGGETTIVI CHE PORTINO UN GENERE, che qui e' la trappola piu'
fitta del file — il blocco parla proprio di eta' e di sesso:

    :4093  «torna bambino» direbbe che ogni creatura e' maschio  -> «torna all'infanzia»
    :4184  «e' avvelenato» concorda col cibo, che puo' essere femminile -> «c'e' del veleno dentro»
    :4212  «ti senti eccitato» concorda con chi gioca -> «senti montare l'eccitazione»
    :4217  «mi sento strana» concorda con chi parla -> «che strana sensazione»

⚠️ `:4106` non puo' dire «il corpo di » + `name(cc)`: `name()` si porta
l'articolo (`contratto-nomi.md` §4) e verrebbe «il corpo di il viandante». Il
nome torna soggetto e il possesso si perde, che in italiano e' la forma normale
per le parti del corpo.

⭐ `:4217` **guadagna lo spazio che l'inglese di monte ha perso**: la seconda
battuta scrive `"gasps "` senza spazio iniziale, attaccato al nome
(«il viandanteansima»), mentre la prima ce l'ha. E' un difetto di spaziatura di
monte, e non c'e' nessuna ragione di copiarlo: la resa italiana mette lo spazio
in tutt'e due.

Legge le voci gia' estratte da lavoro/_item.jsonl e ci scrive dentro la resa.
"""
import io
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from strumenti import accenti

# I valori di CDATAN_NEWSEX: operandi, non testo. Vedi il docstring.
INVARIATI = {"male", "female", "male?", "female?", "hermaphrodite", "none"}

# (riga, inglese) -> italiano.  Per le dinamiche l'italiano e' l'espressione HSP intera.
RESE = {
    # ------------------------------------------------------------- l'eta' e il corpo
    (4066, " suddenly aged."):                       # …は一気に歳をとった。
        'name(cc) + " invecchia di colpo."',
    (4093, " became a child."):                      # …は子供になってしまった。
        'name(cc) + " torna all\'infanzia."',
    (4106, "After eating, 's body violently expanded and contracted."):
        'name(cc) + " finisce il boccone, e subito il corpo si allunga e si accorcia di scatto."',
    # --------------------------------------- la carne proibita: gli operandi restano
    (4116, "male"): "male",
    (4118, "female"): "female",
    (4139, "female?"): "female?",
    (4140, "male?"): "male?",
    (4163, "hermaphrodite"): "hermaphrodite",
    (4170, "none"): "none",
    (4135, " became the opposite sex!"):             # …は性転換した！
        'name(cc) + " cambia sesso!"',
    (4160, " became the opposite sex...?"):          # …は性転換した…？
        'name(cc) + " cambia sesso...?"',
    # ------------------------------------------------------------------- il veleno
    (4184, "It's poisoned!  writhe in agony!"):      # これは毒されている！…はもがき苦しみのたうちまわった！
        '"C\'è del veleno dentro! " + name(cc) + " si contorce dal dolore!"',
    (4186, "Gyaaaaa...!"):                           # 「ギャァァ…！」
        "Gyaaaah...!",
    (4186, "Ugh!"):                                  # 「ブッ！」
        "Urgh!",
    # -------------------------------------------------------------- il filtro d'amore
    (4212, "You are excited!"):                      # あなたは興奮した！
        "Senti montare l'eccitazione!",
    (4217, " gasps, I f-feel...strange..."):         # 「なんだか…変な気分なの…」
        '" ansima: " + cnvtalk("Che strana sensazione...")',
    (4217, "gasps Uh.. uh.. What is this feeling..."):   # 「あれ…なにこの感じは…」
        '" ansima: " + cnvtalk("Ma... che cos\'è questa sensazione...")',
}

USCITA = "fase4-item-004.jsonl"


def main():
    radice = pathlib.Path(__file__).resolve().parent.parent
    voci = []
    with io.open(radice / "lavoro" / "_item.jsonl", encoding="utf-8") as f:
        for riga in f:
            d = json.loads(riga)
            chiave = (d["riga"], d["en"])
            if chiave in RESE:
                d["it"] = RESE[chiave]
                voci.append(d)

    mancanti = set(RESE) - {(d["riga"], d["en"]) for d in voci}
    if mancanti:
        raise SystemExit("chiavi non trovate nel lotto: %s" % sorted(mancanti))
    if len(voci) != len(RESE):
        raise SystemExit("attese %d voci, riempite %d" % (len(RESE), len(voci)))

    # ⚠️ Una resa identica all'inglese e' legittima SOLO se la stringa e'
    # dichiarata in invariati.md. Qui il conto si fa a mano prima che lo faccia
    # `verifica`, cosi' un invariato aggiunto per distrazione si vede subito.
    identiche = {d["en"] for d in voci if d["it"] == d["en"]}
    if identiche != INVARIATI:
        raise SystemExit("identiche all'inglese: %s, attese %s"
                         % (sorted(identiche), sorted(INVARIATI)))

    voci.sort(key=lambda d: (d["riga"], d["occorrenza"]))
    dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
    with io.open(radice / "lavoro" / USCITA, "wb") as f:
        f.write(dati)

    guasti = {it: sorted(accenti.doppi_byte_cp932(it)) for it in RESE.values()
              if accenti.doppi_byte_cp932(it)}
    print("%d voci scritte in lavoro/%s" % (len(voci), USCITA))
    print("caratteri a due byte: %s" % (guasti or "nessuno"))
    print("invariate dichiarate: %d" % len(identiche))
    for d in voci:
        print("   :%-6d %s" % (d["riga"], d["it"]))


if __name__ == "__main__":
    main()
