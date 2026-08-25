# scratchpad/_100-selettori-ombra.py
"""I selettori di `custom_autopick.hsp` che si fanno OMBRA l'uno con l'altro.

Le 78 `lang()` dentro `instr` non sono etichette: sono le **chiavi** con cui il
giocatore scrive `autopick.txt`. E `instr` e' un confronto per **sottostringa**,
non per parola: se una chiave e' contenuta in un'altra, il controllo della
chiave corta scatta sulla regola che nomina quella lunga.

Due catene, con due regole diverse:

  MODIFICATORI  (`:150`-`:353`, chiave con gli spazi attorno: ` all `)
      chi aggancia si **toglie** da `s` (`sreplace ... , " "`), quindi una
      chiave lunga che viene prima copre la corta. Il danno c'e' quando la
      **corta viene prima**: scatta lei sul testo della lunga, e il suo
      `continue` butta via l'oggetto.

  TIPI  (`:366`-`:560`, chiave nuda: `helm`)
      nessuno si toglie, e ogni `if` della catena viene provato. Qui basta che
      una chiave sia sottostringa di un'altra, **in qualunque ordine**: il
      controllo di quella sbagliata trova la sua parola e fa `continue`.

    python scratchpad/_100-selettori-ombra.py            # la build italiana
    python scratchpad/_100-selettori-ombra.py --en       # l'inglese di monte
    python scratchpad/_100-selettori-ombra.py --jp       # il giapponese

⚠️ **Prova al contrario**: `--en` deve accendersi due volte — `book` dentro
`spellbook` e `food` dentro `traveler's food` — perche' quelle due ombre in
inglese ci sono davvero. `--jp` deve tacere. Se `--en` tace, la rete non
guarda niente.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import percorsi

FILE = "custom_autopick.hsp"
# `instr(s, 0, lang("<jp>", "<altra>"))` — le sole `lang()` che sono chiavi
CHIAVE = re.compile(r'instr\(\s*s\s*,\s*0\s*,\s*lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')


def _siti(albero: Path) -> list[tuple[int, str, str]]:
    """(riga, giapponese, altra lingua) per ogni `instr` che confronta una chiave."""
    righe = (albero / FILE).read_bytes().decode("cp932").split("\r\n")
    trovate = []
    for numero, riga in enumerate(righe, 1):
        spoglia = riga.lstrip()
        if spoglia.startswith("//") or spoglia.startswith(";"):
            continue                      # `:200`-`:217`: due selettori spenti
        trovato = CHIAVE.search(riga)
        if trovato is not None:
            trovate.append((numero, trovato.group(1), trovato.group(2)))
    return trovate


def _classi() -> dict[str, str]:
    """La classe di ogni selettore, letta **dall'inglese di monte**.

    ⚠️ La classe non si deduce dalla stringa che si sta guardando: il
    giapponese scrive i modificatori **senza** gli spazi attorno (すべての), e
    chiedere `chiave != chiave.strip()` al giapponese li conta tutti come tipi.
    La chiave dell'indice e' il **giapponese**, che e' la colonna che nessuna
    build riscrive.
    """
    return {jp: ("modificatore" if en != en.strip() else "tipo")
            for _, jp, en in _siti(percorsi.SORGENTE_HSP)}


def chiavi(albero: Path, colonna: str) -> list[tuple[int, str, str]]:
    """(riga, classe, chiave) in ordine di catena, saltando le righe spente."""
    classe_di = _classi()
    return [(numero, classe_di[jp], jp if colonna == "jp" else altra)
            for numero, jp, altra in _siti(albero)]


def ombre(elenco: list[tuple[int, str, str]]) -> list[str]:
    guasti = []

    modificatori = [(n, c) for n, cl, c in elenco if cl == "modificatore"]
    for posizione, (numero, corta) in enumerate(modificatori):
        for numero2, lunga in modificatori[posizione + 1:]:
            if corta != lunga and corta in lunga:
                guasti.append(
                    f"  MODIFICATORE  :{numero} {corta!r} viene prima di "
                    f":{numero2} {lunga!r} e ne e' sottostringa: la regola che "
                    f"dice {lunga.strip()!r} la aggancia quella sbagliata")

    tipi = [(n, c) for n, cl, c in elenco if cl == "tipo"]
    for indice, (numero, uno) in enumerate(tipi):
        for numero2, altro in tipi[indice + 1:]:
            if uno == altro:
                continue
            if uno in altro:
                corta, lunga, riga_corta, riga_lunga = uno, altro, numero, numero2
            elif altro in uno:
                corta, lunga, riga_corta, riga_lunga = altro, uno, numero2, numero
            else:
                continue
            guasti.append(
                f"  TIPO          :{riga_corta} {corta!r} e' dentro "
                f":{riga_lunga} {lunga!r}: una regola che dice {lunga!r} "
                f"scatta anche sul controllo di {corta!r}, che fa `continue`")
    return guasti


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="I selettori di autopick che si fanno ombra a vicenda.")
    gruppo = analizzatore.add_mutually_exclusive_group()
    gruppo.add_argument("--en", action="store_true", help="l'inglese di monte")
    gruppo.add_argument("--jp", action="store_true", help="il giapponese di monte")
    argomenti = analizzatore.parse_args()

    if argomenti.jp:
        albero, colonna, etichetta = percorsi.SORGENTE_HSP, "jp", "giapponese di monte"
    elif argomenti.en:
        albero, colonna, etichetta = percorsi.SORGENTE_HSP, "en", "inglese di monte"
    else:
        albero, colonna, etichetta = percorsi.BUILD_HSP, "en", "build italiana"

    elenco = chiavi(albero, colonna)
    modificatori = sorted({c for _, cl, c in elenco if cl == "modificatore"})
    tipi = sorted({c for _, cl, c in elenco if cl == "tipo"})
    print(f"--- {etichetta}: {len(modificatori)} modificatori, {len(tipi)} tipi")

    guasti = ombre(elenco)
    for guasto in guasti:
        print(guasto)
    print(f"\nombre: {len(guasti)}")
    if not argomenti.en and guasti:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
