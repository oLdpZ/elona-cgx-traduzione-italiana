# -*- coding: utf-8 -*-
"""«1 oggetti»: il piede dell'inventario non aveva il singolare.

Visto a schermo il 2026-09-03, nella finestra «Raccogli» con un oggetto solo.

    command.hsp:14175   s = "" + listmax + " items"   -> " oggetti"   (toppa a mano)
    blend.hsp:1390      idem

⚠️ **L'inglese sbagliava allo stesso modo** — «1 items» — quindi non c'era
niente da cui accorgersene leggendo il sorgente: e' un difetto che la
traduzione ha **ricopiato**, non uno che ha aggiunto. E il `motivo` della toppa
di `command.hsp` e' lungo quindici righe, misura i pixel del piede, l'allineamento
a destra di `display_note`, la regola della 46a e il quinto punto cieco della
49a — e **non nomina il numero**. Si puo' guardare a lungo la larghezza di una
riga senza mai guardarne la grammatica.

Il rimedio e' un `if` sul numero, non una parola diversa: in italiano
«1 oggetto» e «2 oggetti» sono due stringhe, e nessuna delle due copre l'altra.
Lo zero sta con il plurale («0 oggetti»), che e' gia' quel che fa il ramo `else`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-il-singolare-del-piede.py
    ... --prova    non scrive: stampa le toppe come diventerebbero
"""
import io
import json
import sys

from strumenti import percorsi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

CERCA = '\ts = "" + listmax + " items"'
NUOVO_MOTIVO = (
    " ⚠️⚠️ 2026-09-03, visto a schermo: con un oggetto solo scriveva «1 oggetti»."
    " In inglese la riga sbagliava uguale («1 items»), quindi il difetto non e'"
    " stato aggiunto dalla traduzione ma ricopiato: leggere il sorgente non"
    " bastava, ci voleva la schermata. Adesso il numero sceglie fra le due"
    " stringhe. Lo zero resta col plurale, che e' il ramo `else`. ⓘ La resa non"
    " cambia larghezza: «oggetto» e «oggetti» hanno le stesse sette lettere,"
    " quindi la misura del piede scritta qui sopra vale ancora."
)


def blocco(indentazione, singolare, plurale):
    return [
        f"{indentazione}if ( listmax == 1 ) {{",
        f'{indentazione}\ts = "" + listmax + " {singolare}"',
        f"{indentazione}}}",
        f"{indentazione}else {{",
        f'{indentazione}\ts = "" + listmax + " {plurale}"',
        f"{indentazione}}}",
    ]


def main():
    prova = "--prova" in sys.argv
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    toppe = [json.loads(r) for r in
             percorso.read_text(encoding="utf-8").splitlines() if r.strip()]

    toccate = 0
    for t in toppe:
        if t.get("cerca") != CERCA:
            continue
        # ⚠️ si pretende che la toppa sia ancora quella a riga singola che
        # conosciamo: se qualcuno l'ha gia' cambiata, ci si ferma invece di
        # sovrascrivere un lavoro altrui.
        atteso = '\ts = "" + listmax + " oggetti"'
        if t.get("sostituisci") != atteso:
            print(f"!! {t['file']}: `sostituisci` non e' piu' {atteso!r}, "
                  f"ma {t.get('sostituisci')!r}. Non tocco niente.")
            return 1
        t["sostituisci"] = blocco("\t", "oggetto", "oggetti")
        t["motivo"] = t["motivo"] + NUOVO_MOTIVO
        toccate += 1
        print(f"ok  {t['file']}")
        for r in t["sostituisci"]:
            print("      " + r.replace("\t", "    "))

    if toccate != 2:
        print(f"\n!! toppe trovate: {toccate}, attese 2 (command.hsp e blend.hsp)")
        return 1

    if prova:
        print("\n--prova: non ho scritto niente")
        return 0

    with percorso.open("w", encoding="utf-8", newline="\n") as f:
        for t in toppe:
            f.write(json.dumps(t, ensure_ascii=False) + "\n")
    print(f"\nscritto {percorso}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
