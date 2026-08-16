# -*- coding: utf-8 -*-
"""53a, lotto `tcg-schede`: le linguette dell'editor del mazzo, e le fasi del turno.

Le linguette in cima all'editor sono letterali **nudi** dentro un'assegnazione di
array (`cfname@tcg = lang(…), lang(…), "0-150", "151-300", …`): sono la famiglia
del **sesto** punto cieco, quello che `tabelle_en.py` ha aperto nella 52ª, ma
quel referto conta solo le tabelle **senza** `lang()` dentro — qui le due
`lang()` iniziali ci sono, e la riga non compare in nessun elenco.

⚠️⚠️ **NOVE righe su diciassette NON si toccano, e non e' una rinuncia: e' una
misura.** Le linguette di razza e classe (`:3577`-`:3632`) portano le **chiavi
interne** — `seamonster`, `kobolt`, `eulderna`, `yerles`, `warmage`,
`classless` — e ci sono **89 righe** che le confrontano:

    tcg.hsp:3757   if ( … cardn@tcg(TCG_CARDN_REF_RACE, cnt) != "seamonster" ) { continue }
    tcg.hsp:3853   if ( … cardn@tcg(TCG_CARDN_REF_CLASS, cnt) != "warrior" )   { continue }

E c'e' di piu': `:1508` scrive `rtvaln += " " + cardrefrace + " " + cardrefclass`,
cioe' la **carta stessa mostra la chiave cruda**. Tradurre la linguetta e non la
carta darebbe «rana» in cima e «frog» sulla carta. E la carta non si puo'
tradurre, perche' quella chiave viene da `db_race.hsp`, dove il progetto ha gia'
deciso che `listn(1, …)` e' un identificativo e non testo.
💡 E' la lezione della 52ª sulle dodici classi di `custom_ai.hsp`, terza volta:
**quel che serve a un confronto non e' testo, e si guarda il sito.**

✅ **Le altre si toccano, e il motivo e' misurabile**: dominio e costo filtrano
per **numero** — `card@tcg(TCG_CARD_REF_DOMAIN, cnt) != cflist@tcg(ccf@tcg) - 2`
a `:3705`, lo stesso a `:3712` per il costo — quindi li' la parola e' solo
un'etichetta.

⚠️ **`1 HP`…`9+ HP` non hanno toppa**: «HP» non si traduce, l'ha deciso la 51ª
insieme a `DV` e `Dojo`. Il conteggio dei nudi continuera' a contarle.

💡 **Il tetto della linguetta e' l'immagine.** `tcg.hsp:3300` disegna
`gcopy 7, 360, 96, 63, 20`, cioe' **63 px**, col testo a `x+1` e corpo 9
(`:3283`, `10 + en - en * 2`). Col metro delle carte della 52ª — corpo 9, 72 px,
15 caratteri — vengono **una dozzina** di caratteri: «Leggendario» ne fa 11.

⭐ **E le quattro fasi del turno erano l'altra meta' della stessa riga.**
`tcg_mod.hsp:3478` e' `phasen@tcg = "Begin", "Draw", "Main", "End", ""`, disegnate
a `tcg.hsp:3450` nella colonna a sinistra del tavolo. Il riquadro e' quello da
**106x18 px** (`gcopy 7, 360, 216, 106, 18`) dove la 52ª ha gia' fatto stare
«Avversario», dieci caratteri: «Principale» ne fa dieci esatti.

⚠️⚠️⚠️ **E QUI IL LOTTO SI E' DIMEZZATO, per un limite dell'architettura che
nessuno aveva ancora incontrato.** Le quattro righe `cfname@tcg` di `tcg.hsp`
portano insieme **due `lang()` e una decina di letterali nudi**:

    cfname@tcg = lang("候補", "List"), lang("デッキ", "Deck"), "Blue", "Green", …

`applica.py` fa **prima tutto il dizionario e poi le toppe** (`:701`, «le toppe
hanno un giro proprio»), quindi al momento della toppa quella riga dice gia'
«Elenco» e «Mazzo». Ma `test_toppe.py::test_le_toppe_del_progetto_si_applicano_
al_sorgente_pinnato` pretende che **ogni toppa agganci il sorgente pinnato**, e
per una buona ragione: e' la guardia che diventa rossa quando upstream riscrive
una riga, prima che la build produca qualcosa di sbagliato.

Le due pretese insieme dicono una cosa sola: **una riga che il dizionario
riscrive non e' toppabile.** Ancorata al sorgente non aggancia la build;
ancorata alla build non passa il test. Ho provato tutt'e due, in quest'ordine,
e la seconda ha fatto diventare rosso il test — che e' esattamente il suo
mestiere.

✅ **La quinta toppa resta perche' e' l'eccezione che lo conferma**:
`tcg_mod.hsp:3478` di `lang()` non ne ha nemmeno una, quindi sorgente e build
coincidono e l'ancora vale in tutt'e due.

💡 **Il difetto della toppa a `:2470` era un altro** (`toppa-tcg-mazzi.py`), e
per questo quella funziona: la riga ha una `lang()`, ma la sua firma e'
**rinviata**, quindi il dizionario non la tocca e sorgente e build restano
identici. E' la stessa regola vista dal verso buono.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUILD = Path(r"C:\Games\Elona\_traduzione\build\2.05-custom-gx")

# (file, riga, [(vecchio, nuovo), …], motivo). Il `cerca` e' la riga INTERA;
# i frammenti sono virgolettati apposta, cosi' «All» non aggancia per sbaglio un
# pezzo di un'altra parola.
#
# ⚠️⚠️ **Le quattro righe `cfname@tcg` di `tcg.hsp` NON sono qui, e non possono
# esserci.** Sono `:3552` (gli intervalli di numero, con «All»), `:3557` (i
# domini), `:3562` (il costo) e `:3567` (l'attacco): erano scritte, provate e
# applicate, e le ha tolte il test. Vedi il docstring.
LOTTO = [
    ("tcg_mod.hsp", 3478, [('"Begin"', '"Inizio"'), ('"Draw"', '"Pesca"'),
                           ('"Main"', '"Principale"'), ('"End"', '"Fine"')],
     "Le quattro fasi del turno, nella colonna a sinistra del tavolo "
     "(`tcg.hsp:3450`). ⚠️ «Pesca» e non «Pescata»: e' la fase in cui si pesca, e "
     "il gioco di carte italiano la chiama cosi'. Riquadro da 106x18 px, lo "
     "stesso dove «Avversario» ci sta gia'."),
]


def main() -> None:
    toppe, problemi = [], []
    testi = {}
    for nome, n, coppie, motivo in LOTTO:
        if nome not in testi:
            # ⚠️ `.splitlines()` e non `.split("\n")`: i file sono CRLF, e uno
            #    split sul solo `\n` lascia il `\r` in coda a ogni riga. Ancorare
            #    una riga col `\r` dentro non aggancia niente, perche'
            #    `applica.spezza_righe` il terminatore lo toglie — costato una
            #    build, e l'errore lo dice per intero mostrando il `\r` finale.
            testi[nome] = (BUILD / nome).read_bytes().decode("cp932").splitlines()
        righe = testi[nome]
        cerca = righe[n - 1]
        resa = cerca
        for vecchio, nuovo in coppie:
            if vecchio not in resa:
                problemi.append(f"{nome}:{n} non contiene {vecchio!r}")
                continue
            if resa.count(vecchio) != 1:
                problemi.append(f"{nome}:{n} {vecchio!r} compare "
                                f"{resa.count(vecchio)} volte nella riga")
                continue
            # ⚠️ L'ASCII si pretende sul pezzo NUOVO: la riga porta gia' dentro
            #    il giapponese delle `lang()`, che non e' roba nostra.
            for c in nuovo:
                if ord(c) > 0x7F:
                    problemi.append(f"{nome}:{n} carattere fuori ASCII: {c!r}")
            resa = resa.replace(vecchio, nuovo, 1)
        if resa == cerca:
            problemi.append(f"{nome}:{n} nessuna sostituzione: la toppa sarebbe muta")
            continue
        quante = righe.count(cerca)
        toppa = {"file": nome, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    print(f"{len(toppe)} toppe")
    uscita = REPO / "lavoro" / "_toppe-tcg-schede.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
