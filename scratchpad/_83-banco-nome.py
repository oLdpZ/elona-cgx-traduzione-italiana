# -*- coding: utf-8 -*-
"""Banco: che cosa scrive `itemname()` per un oggetto NON identificato.

    PYTHONPATH=<radice> python scratchpad/_83-banco-nome.py

Non traduce niente: legge gli array dalla **build** (cioe' da quel che
`applica` ha davvero scritto sul disco) e rifa a mano i tre passaggi di
`item_func.hsp` che compongono il nome, nell'ordine in cui li fa il gioco:

  1. la parola-contatore (`:1217`, `:1259`) — `ioriginalnameref2`, che il gioco
     scrive **anche quando l'oggetto non e' identificato**;
  2. il nome (`:1499` per gli oggetti mai visti, `:1738` per i prodigiosi),
     al plurale se la parola-contatore manca;
  3. l'articolo (`:1876`-`:1971`), che pesca dagli array del nome identificato
     a meno che la spia sia accesa E la parola-contatore sia vuota.

⚠️ E' un banco, non una guardia: serve a LEGGERE 260 nomi in una volta invece
di ragionarci sopra uno per uno. Il giudice vero resta il gioco.
"""
import re
import sys
from pathlib import Path

BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx\db_item.hsp")
RIGHE = BUILD.read_bytes().decode("cp932").split("\r\n")

_ASSEGNA = re.compile(r'^(\w+)\((\w+)\)\s*=\s*"(.*)"$')
# le parole-contatore cablate in itemname(), che vincono sull'array
CABLATE = {"bottiglia": ("una ", "la "), "tazza": ("una ", "la "),
           "carico": ("un ", "il "), "paio": ("un ", "il "),
           "piatto": ("un ", "il ")}


def leggi():
    """array -> {oggetto: valore}, dal solo ramo `else` (l'italiano)."""
    dati = {}
    for indice, riga in enumerate(RIGHE):
        trovato = _ASSEGNA.match(riga.strip())
        if trovato is None:
            continue
        # si risale al piu' vicino `else {` / `if ( jp ) {` sopra il blocco
        ramo = None
        for indietro in range(indice - 1, max(-1, indice - 12), -1):
            testo = RIGHE[indietro].strip()
            if testo in ("else {", "if ( jp ) {"):
                ramo = testo
                break
            if not _ASSEGNA.match(testo):
                break
        if ramo != "else {":
            continue
        array, oggetto, valore = trovato.groups()
        dati.setdefault(array, {})[oggetto] = valore
    return dati


def main():
    d = leggi()
    noti = d.get("iknownnameref", {})
    print(f"oggetti con un nome non identificato proprio: {len(noti)}\n")
    righe = []
    for oggetto, nome in noti.items():
        contatore = d.get("ioriginalnameref2", {}).get(oggetto, "")
        if contatore:
            indeterminativo = CABLATE.get(contatore, (None,))[0]
            if indeterminativo is None:
                indeterminativo = d.get("ioriginalnamearticolo", {}).get(oggetto, "")
            singolare = f"{indeterminativo}{contatore} di {nome}"
            contatore_plur = d.get("ioriginalnameref2plur", {}).get(oggetto, contatore)
            plurale = f"2 {contatore_plur} di {nome}"
        else:
            indeterminativo = d.get("iknownnamearticolo", {}).get(oggetto, "")
            singolare = f"{indeterminativo}{nome}"
            plurale = f"2 {d.get('iknownnamerefplur', {}).get(oggetto, nome)}"
        righe.append((singolare, plurale, oggetto))
    for singolare, plurale, oggetto in sorted(righe):
        print(f"{singolare:52} {plurale:52} {oggetto}")
    senza = [o for o in noti
             if not d.get("ioriginalnameref2", {}).get(o)
             and not d.get("iknownnamearticolo", {}).get(o)]
    print(f"\nsenza articolo (ripiegherebbero sull'inglese a/an): {len(senza)}")
    for o in senza:
        print("   ", o)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
