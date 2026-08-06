# strumenti/prova_identita.py
"""La prova d'identita': un dizionario che traduce ogni stringa in se' stessa
deve riprodurre i file byte per byte.

E' la verifica piu' forte disponibile su questa catena, perche' non dipende da
quali casi qualcuno si e' ricordato di coprire: attraversa ogni sito del corpus
reale. Ha trovato i due difetti peggiori del progetto mentre 83 test erano verdi.

Finora era una procedura a mano, e una procedura a mano non si rifa' a ogni giro.
Qui e' un comando:

    python -m strumenti.prova_identita

Una classe di voci resta **esclusa per costruzione**, non per comodita': le
firme a cui il sorgente associa piu' di un'espressione (le dinamiche con
variabili diverse dietro la stessa firma). Includerle farebbe fallire la
prova sul rifiuto invece che sulla corruzione, che e' il contrario di quello
che deve misurare. Le statiche avvolte in `cnvtalk(`/`cnven(` non sono piu'
escluse: l'involucro si prende dal sito, quindi si sostituiscono come le
altre.

I conteggi vengono stampati apposta. Se calano senza che nessuno abbia
implementato niente, la prova sta misurando meno di prima e nessun test lo
direbbe.
"""
import argparse
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from strumenti import percorsi
from strumenti.applica import applica_a_testo
from strumenti.estrai import estrai_da_testo, normalizza_espressione


@dataclass
class Esito:
    file_provati: int = 0
    file_identici: int = 0
    sostituzioni: int = 0
    esclusi_ambigui: int = 0
    difformi: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.file_provati > 0 and not self.difformi


def dizionario_identita(nome_file: str, testo: str) -> tuple[dict, int]:
    """Ogni stringa tradotta in se' stessa, meno le voci che `applica` rifiuta."""
    voci = estrai_da_testo(nome_file, testo)

    # Una firma che compare con espressioni diverse non ha una sostituzione sola.
    # Per le statiche l'involucro non entra nella firma per progetto, e non deve
    # entrare neppure qui: `applica.py` lo prende dal sito, quindi lo stesso
    # inglese nudo o avvolto in cnvtalk( e' la stessa identita', non una
    # collisione. Il confronto vero e' sul testo inglese estratto (`en`), non
    # sull'espressione grezza che include l'involucro. Per le dinamiche resta
    # l'espressione grezza normalizzata: li' le variabili contano.
    espressioni = defaultdict(set)
    for voce in voci:
        confronto = voce["en"] if voce["tipo"] == "statica" else voce["en_grezzo"]
        espressioni[voce["firma"]].add(normalizza_espressione(confronto))
    ambigue = {f for f, e in espressioni.items() if len(e) > 1}

    dizionario: dict[str, dict] = {}
    for voce in voci:
        if voce["firma"] in ambigue:
            continue
        if voce["tipo"] == "statica":
            identita = voce["en"]
        else:
            # per le dinamiche si sostituisce l'espressione intera
            identita = voce["en_grezzo"]
        dizionario[voce["firma"]] = {**voce, "it": identita}

    scartati_ambigui = sum(1 for v in voci if v["firma"] in ambigue)
    return dizionario, scartati_ambigui


def prova(radice: Path | None = None) -> Esito:
    radice = radice or percorsi.SORGENTE_HSP
    esito = Esito()
    for percorso in sorted(radice.glob("*.hsp")):
        grezzo = percorso.read_bytes()
        testo = grezzo.decode("cp932")
        dizionario, ambigue = dizionario_identita(percorso.name, testo)
        nuovo, sostituzioni = applica_a_testo(percorso.name, testo, dizionario)

        esito.file_provati += 1
        esito.sostituzioni += sostituzioni
        esito.esclusi_ambigui += ambigue
        if nuovo.encode("cp932") == grezzo:
            esito.file_identici += 1
        else:
            esito.difformi.append(percorso.name)
    return esito


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--radice", type=Path, default=None,
                    help="cartella con gli .hsp da provare (default: SORGENTE)")
    argomenti = ap.parse_args(argv)

    esito = prova(argomenti.radice)
    print(f"file riprodotti byte per byte : {esito.file_identici}/{esito.file_provati}")
    print(f"sostituzioni eseguite         : {esito.sostituzioni}")
    print(f"escluse, firme ambigue        : {esito.esclusi_ambigui}")
    if esito.difformi:
        print("\nFILE DIFFORMI — la catena corrompe il sorgente:")
        for nome in esito.difformi:
            print(f"  {nome}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
