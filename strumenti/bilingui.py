# strumenti/bilingui.py
"""I menu che il giocatore leggerebbe META' IN ITALIANO E META' IN INGLESE.

⚠️⚠️ **La rete che mancava, e le quattordici non potevano vederla** (76a). Le
voci di `chatList` che stanno una sotto l'altra sono **una schermata sola**: se
tre sono rese e undici no, quella finestra e' peggio di com'era prima che
qualcuno la toccasse — da inglese e coerente a meta' italiana e incoerente. E'
la lezione della 73a, che pero' viveva soltanto dentro `gemelle.annota_menu()`:
li' si misura quanto di un menu copre **un lotto**, mentre lo si prepara. Nessuno
guardava lo **stato del file**.

⚠️⚠️⚠️ **E un menu si buca anche senza che se ne tocchi una riga.** Il dizionario
e' indicizzato per **firma** — giapponese piu' inglese — e la stessa firma vive
in piu' punti del file: tradurre una voce in un menu ne traduce un'altra
diciottomila righe piu' in la', dentro una schermata che non si stava nemmeno
guardando. Nella 76a e' successo tre volte:

  * il «No.» di `chat.hsp:24653` ha aperto il menu del venditore di Jure a
    `:6277`, che era tutto inglese;
  * «Use Light of Memory.» a `:1327` non si poteva chiudere senza aprire il menu
    dell'**altro** Loyter a `:1268`;
  * 「習得する」 e 「訓練する」 di `:24954` stanno anche nella schermata
    dell'allenatore amico a `:390`.

Quindi la domanda non e' «questo lotto copre il suo menu?» ma «dopo questo lotto
esiste un menu a meta'?», e la si puo' fare solo al file intero.

⚠️ **Le rinviate contano come fatte.** `chat.hsp:19327` e `:19334` sono righe
**commentate** a monte (`// chatList 84, ...`): non le disegna nessuno, e stanno
in `rinviate.jsonl` per questo. Senza toglierle la rete lascerebbe un menu «a
meta'» per sempre, e l'unico modo di chiuderlo sarebbe tradurre codice morto —
che e' quel che il rinvio esiste per non fare.

💡 **Il limite noto: i menu si raggruppano per DISTANZA** (`gemelle.blocchi_menu`,
righe di `chatList` vicine). Un `chatList` che sta sedici righe sopra i suoi
fratelli — `chat.hsp:24945`, il bottone «Allenare» dell'addestratore — finisce in
un gruppo suo, e la rete non lo vede insieme agli altri. Sbaglia per **difetto**:
puo' tacere su una schermata rotta, non puo' inventarne una.

    python -m strumenti.bilingui            # tutti i file con dizionario
    python -m strumenti.bilingui chat.hsp   # uno solo
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from strumenti import estrai, gemelle, percorsi


def firme_tradotte(nome: str, dizionario: Path | None = None) -> set[str]:
    """Le firme che nel dizionario di questo file hanno una resa non vuota."""
    radice = dizionario or percorsi.DIZIONARIO
    percorso = radice / f"{nome}.jsonl"
    if not percorso.exists():
        return set()
    fatte = set()
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if riga.strip():
            voce = json.loads(riga)
            if (voce.get("it") or "").strip():
                fatte.add(voce["firma"])
    return fatte


def file_con_dizionario(dizionario: Path | None = None) -> list[str]:
    radice = dizionario or percorsi.DIZIONARIO
    return sorted(p.stem for p in radice.glob("*.jsonl"))


def menu_bilingui(nomi: list[str] | None = None,
                  dizionario: Path | None = None,
                  sorgente: Path | None = None,
                  rinviate: Path | None = None) -> list[dict]:
    """I gruppi di `chatList` con almeno una voce resa e almeno una no.

    Ogni voce del referto: `file`, `da`, `a`, `voci`, `fatte`, `restano` (le voci
    non ancora rese, come le estrae `estrai`).
    """
    radice = sorgente or percorsi.SORGENTE_HSP
    referto: list[dict] = []
    for nome in (nomi if nomi is not None else file_con_dizionario(dizionario)):
        percorso = radice / nome
        if not percorso.exists():
            continue
        testo = percorso.read_bytes().decode("cp932", errors="replace")
        fatte = (firme_tradotte(nome, dizionario)
                 | estrai.carica_rinviate(rinviate, nome))
        per_riga: dict[int, list[dict]] = {}
        for voce in estrai.estrai_da_testo(nome, testo):
            per_riga.setdefault(voce["riga"], []).append(voce)

        for blocco in gemelle.blocchi_menu(testo):
            voci = [v for n in blocco for v in per_riga.get(n, [])]
            if not voci:
                continue
            rese = [v for v in voci if v["firma"] in fatte]
            restano = [v for v in voci if v["firma"] not in fatte]
            if rese and restano:
                referto.append({
                    "file": nome, "da": blocco[0], "a": blocco[-1],
                    "voci": len(voci), "fatte": len(rese), "restano": restano,
                })
    return referto


def main(argv: list[str] | None = None) -> int:
    nomi = list(argv if argv is not None else sys.argv[1:]) or None
    referto = menu_bilingui(nomi)
    for menu in referto:
        print("%s:%d-%d   %d voci, %d rese, %d no"
              % (menu["file"], menu["da"], menu["a"], menu["voci"],
                 menu["fatte"], len(menu["restano"])))
        for voce in menu["restano"][:6]:
            print("        :%-6d %r" % (voce["riga"], (voce["en"] or "")[:60]))
        if len(menu["restano"]) > 6:
            print("        ... e altre %d" % (len(menu["restano"]) - 6))
    print()
    print("menu bilingui: %d" % len(referto))
    return 1 if referto else 0


if __name__ == "__main__":
    raise SystemExit(main())
