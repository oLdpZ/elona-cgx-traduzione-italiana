# -*- coding: utf-8 -*-
"""53a, lotto `tcg-mazzi`: il menu di scelta del mazzo, che nessun referto vedeva.

Quattro toppe su una schermata sola — quella che si apre usando un «mazzo di
carte» — e tutte e quattro su righe che **nessun conteggio elencava**.

⚠️ **Tre stanno nel SETTIMO punto cieco**, misurato oggi con
`scratchpad/nudi_dopo_if.py`: `s@tcg(cnt) +=` porta il **suffisso di modulo**, e
la regola `_COMPONE` di `nudi_en.py:47` elenca `s`, `buff`, `valn`… senza
ammetterlo. **`s@tcg` non e' `s`**, quindi ` (NG 12/30)` e ` [Use]` non sono mai
comparsi fra le righe da fare.

⚠️ **La quarta e' il rovescio di una rinviata, e sistema l'ordine delle parole.**
Il nome del mazzo si compone in due tempi:

    :2468   s@tcg(cnt)  = lang("白", "White")
    :2470   s@tcg(cnt) += lang("のデッキ", " Deck")

In italiano il nome viene **prima** del colore, quindi il lotto `fase4-tcg-001`
mette tutto nel colore — «Mazzo bianco» — e a `:2470` non resta niente da dire.
Una resa **vuota** non e' esprimibile, perche' `estrai.firme_tradotte` conta come
non tradotta ogni voce con `it` falso: la voce e' rinviata e la riga si spegne
qui, svuotando il secondo argomento della `lang()` e lasciando intatto il primo.
💡 E' la stessa forma delle rinviate «mai: la riga la sistema la toppa su …» che
`command.hsp` ha gia' due volte.

⚠️⚠️ **Il `cerca` di una toppa e' fatto di RIGHE INTERE, e non di frammenti.**
Provato per sbaglio e imparato dall'errore: ancorare `, " Deck")` sembra piu'
preciso, e invece `applica.py:569` confronta `righe[i:i+len(cerca)] == cerca`,
cioe' **liste di righe**. Un frammento non aggancia niente e la build si ferma
con «la riga della toppa non esiste piu'». E' il motivo per cui
`genera-toppe-en.py` allarga il blocco *aggiungendo righe*, non caratteri.

⚠️ E la riga di `:2470` porta dentro il giapponese 「のデッキ」, quindi il
controllo dell'ASCII — che c'e' perche' in build gli accenti vanno degradati —
si fa sul **pezzo che si introduce**, non su tutta la riga: il giapponese e'
gia' li' e non e' roba nostra.

💡 **E le toppe si applicano DOPO il dizionario**, sulla build gia' sostituita
(`applica.py`: prima le firme, poi le toppe). Qui non cambia niente — nessuna
delle quattro righe ha una `lang()` che il dizionario tocchi, perche' `:2470` e'
rinviata — ma l'ancora va sempre pensata sulla build, non sul sorgente.

⭐ **«KO» e non «NG»**: `NG` e' l'abbreviazione giapponese di *no good*, e in
italiano non vuol dire niente. Serve un marcatore corto perche' la voce sta in
un riquadro da 300px — 32 caratteri col metro di `larghezze.py` — e «Mazzo
argento (KO 12/30)» ne fa 24. ⚠️ E dev'essere **neutro**: i due rami dicono
cose opposte, `:2478` che le carte sono troppo poche e `:2481` che sono troppe.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg.hsp")
FILE = "tcg.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932")
RIGHE = TESTO.splitlines()

# (riga, vecchio, nuovo, motivo). `vecchio` e `nuovo` sono i due frammenti che
# cambiano; il `cerca` della toppa e' la RIGA INTERA che li contiene.
LOTTO = [
    (2470, ', " Deck")', ', "")',
     "Il secondo tempo del nome del mazzo, svuotato perche' in italiano il nome "
     "sta gia' nel colore («Mazzo bianco»). La voce e' rinviata nel dizionario. "
     "⚠️ Il primo argomento della `lang()` resta intatto: si spegne l'inglese, "
     "non la riga."),
    (2478, '" (NG "', '" (KO "',
     "Il mazzo con TROPPO POCHE carte: «Mazzo bianco (KO 12/30)». ⚠️ `NG` e' "
     "l'abbreviazione giapponese di *no good* e in italiano non dice niente. "
     "⭐ Riga nel settimo punto cieco: `s@tcg(cnt) +=` ha il suffisso di modulo."),
    (2481, '" (NG "', '" (KO "',
     "Lo stesso marcatore per il mazzo con TROPPE carte. Il marcatore dev'essere "
     "neutro proprio perche' i due rami dicono cose opposte."),
    (2484, '" [Use]"', '" [in uso]"',
     "Il mazzo principale, quello che il duello usera'. ⭐ Anche questa nel "
     "settimo punto cieco."),
]


def main() -> None:
    toppe, problemi = [], []
    viste = {}
    for n, vecchio, nuovo, motivo in LOTTO:
        cerca = RIGHE[n - 1]
        if vecchio not in cerca:
            problemi.append(f":{n} non contiene {vecchio!r}: {cerca.strip()[:70]!r}")
            continue
        resa = cerca.replace(vecchio, nuovo, 1)
        # ⚠️ L'ASCII si pretende sul pezzo NUOVO, non su tutta la riga: `:2470`
        #    porta dentro il giapponese della `lang()`, che e' gia' li'.
        for c in nuovo:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII nel sostituto: {c!r}")
        quante = RIGHE.count(cerca)
        if cerca in viste:
            if viste[cerca] != resa:
                problemi.append(f":{n} stessa riga di prima ma resa diversa")
            continue
        viste[cerca] = resa
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa,
                 "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    print(f"{len(toppe)} toppe")
    uscita = REPO / "lavoro" / "_toppe-tcg-mazzi.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
