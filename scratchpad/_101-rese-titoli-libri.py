# -*- coding: utf-8 -*-
"""I 33 titoli del blocco `%DEFINE` di `data\\book.txt`.

    python scratchpad/_101-rese-titoli-libri.py lavoro/book-titoli-001.jsonl

⚠️ **Questi titoli non si leggono dentro il libro: si leggono nel NOME
DELL'OGGETTO.** `item.hsp:112`-`:124` legge il `%DEFINE` con `csvsort` e ne
riempie `booktitle`, che `item_func.hsp:907` incolla al nome: «un libro rosso
intitolato <...>». Sono l'etichetta del libro, non la sua intestazione.

⭐ **Quindici dei trentatre' erano gia' decisi e non si reinventano**: il loro
inglese e' **la stessa stringa** che la 99a ha reso dentro il libro (riga 1 del
blocco omonimo), e lo stesso inglese reso in due modi non ha nessuna scusa di
monte — e' quel che `scratchpad/misura-rete4.py` cerca all'indietro su tutto il
dizionario. Qui sotto stanno con la nota «= corpo».

Gli altri diciotto sono etichette che nel libro non compaiono, e si rendono con
**le parole che il corpo ha gia' scelto**: «museo» (libro 4), «crimberry»
(5, e `invariati.md` lo dichiara), «negozio» (8), «sotterranei» (15),
«difetto» per *bug* (2, la parola che il corpo di quel libro stesso usa).

⚠️ La chiave e' l'**inglese**, non la posizione: se monte riscrive un titolo la
resa non aggancia e questo script muore, invece di scivolare sul libro accanto.
"""
import io
import json
import sys

# inglese del %DEFINE -> titolo italiano
TITOLI = {
    "My Diary": "Il mio diario",
    "Beginner's Guide": "Guida del principiante",                       # = corpo
    "It's a bug": "È un difetto",
    "Don't read this": "Non leggermi",
    "Museum Guide": "Guida al museo",
    "Crimberry Addict": "Dipendenza da crimberry",
    "Cat's Cradle": "Gira la testa",                 # il JP dice 目が回る, non il gioco dello spago
    "Herb Effect": "L'effetto delle erbe",
    "Shopkeeper Guide": "Guida del negoziante",
    "Easy Gardening": "Coltivare è facile",
    "Water!": "Acqua!",
    "Breeder's Guide": "Guida dell'allevatore",
    "Strange Diary": "Diario misterioso",
    "Pyramid Invitation": "Invito alla piramide",
    "Card Game Manual": "Manuale del gioco di carte",
    "Dungeon Guide": "Guida ai sotterranei",
    "Wily Mujaf's Thesis": "La tesi dell'astuto Mujaf",                 # = corpo
    "A Review on Nefian Psychosis": "Studio sulla psicosi nefiana",     # = corpo
    "Gifting Gifts": "Fare regali",                                     # = corpo
    "An Exercise in Team-Building": "Esercizio di affiatamento",        # = corpo
    "Adventurers Quarterly Spring '18": "L'avventuriero trimestrale (prim. 518)",
    "Bitter Last Words": "Ultime parole amare",                         # = corpo
    "Mission Briefing": "Istruzioni per la missione",                   # = corpo
    "Get on my level": "Arriva al mio livello",                         # = corpo
    "Necromanual": "Manuale di negromanzia",                            # = corpo
    "Secrets of the journal": "I segreti del diario",
    "SOR110 Introduction to Sorcery": "SOR110 Introduzione alla stregoneria",   # = corpo
    "You dig mining?": "Lo scavo è una bellezza",                       # = corpo
    "What's in a performance?": "Che cos'è un'esibizione?",             # = corpo
    "Dimensional Energy Report": "Rapporto sull'energia dimensionale",
    "Quest Advice": "Consigli sugli incarichi",                         # = corpo
    "Fishing Introduction": "Introduzione alla pesca",                  # = corpo
    "Inmate Correction Manual": "Manuale di correzione dei prigionieri",  # = corpo
}


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]
    voci = [v for v in voci if v["blocco"] == "DEFINE"]
    if len(voci) != 33:
        raise SystemExit(f"{len(voci)} voci nel blocco DEFINE, attese 33")

    usate = set()
    for voce in voci:
        resa = TITOLI.get(voce["en"])
        if resa is None:
            raise SystemExit(f"titolo senza resa: {voce['en']!r} (libro {voce['riga'] - 1})")
        voce["it"] = resa
        usate.add(voce["en"])

    avanzate = set(TITOLI) - usate
    if avanzate:
        raise SystemExit(f"rese che non agganciano nessun titolo: {sorted(avanzate)}")

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in sorted(voci, key=lambda v: v["riga"]):
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"{len(voci)} titoli resi")


if __name__ == "__main__":
    main(sys.argv[1])
