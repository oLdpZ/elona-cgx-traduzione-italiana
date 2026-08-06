# strumenti/prova_identita.py
"""La prova d'identita': un dizionario che traduce ogni stringa in se' stessa
deve riprodurre i file byte per byte.

E' la verifica piu' forte disponibile su questa catena, perche' non dipende da
quali casi qualcuno si e' ricordato di coprire: attraversa ogni sito del corpus
reale. Ha trovato i due difetti peggiori del progetto mentre 83 test erano verdi.

Finora era una procedura a mano, e una procedura a mano non si rifa' a ogni giro.
Qui e' un comando:

    python -m strumenti.prova_identita

Due classi di voci sono **escluse per costruzione**, non per comodita': sono
esattamente quelle che `applica.py` rifiuta con un errore esplicito (statiche
avvolte in una chiamata, firme che collidono su espressioni diverse). Includerle
farebbe fallire la prova sul rifiuto invece che sulla corruzione, che e' il
contrario di quello che deve misurare. I conteggi vengono stampati: se calano
senza che nessuno abbia implementato niente, e' un segnale.
"""
import argparse
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from strumenti import percorsi
from strumenti.applica import applica_a_testo
from strumenti.estrai import estrai_da_testo


@dataclass
class Esito:
    file_provati: int = 0
    file_identici: int = 0
    sostituzioni: int = 0
    esclusi_avvolti: int = 0
    esclusi_collidenti: int = 0
    difformi: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.file_provati > 0 and not self.difformi


def dizionario_identita(nome_file: str, testo: str) -> tuple[dict, int, int]:
    """Ogni stringa tradotta in se' stessa, meno le voci che `applica` rifiuta."""
    voci = estrai_da_testo(nome_file, testo)

    # una firma che compare con espressioni grezze diverse e' il caso 4: la
    # traduzione dell'una finirebbe sull'altra portandosi le variabili sbagliate
    espressioni = defaultdict(set)
    for voce in voci:
        espressioni[voce["firma"]].add(voce["en_grezzo"])
    collidenti = {f for f, e in espressioni.items() if len(e) > 1}

    dizionario: dict[str, dict] = {}
    avvolti = 0
    for voce in voci:
        if voce["firma"] in collidenti:
            continue
        if voce["tipo"] == "statica":
            # caso 3: l'inglese non e' un letterale nudo ma una chiamata che lo avvolge
            if voce["en_grezzo"] != '"' + voce["en"] + '"':
                avvolti += 1
                continue
            identita = voce["en"]
        else:
            # per le dinamiche si sostituisce l'espressione intera
            identita = voce["en_grezzo"]
        dizionario[voce["firma"]] = {**voce, "it": identita}

    scartati_collidenti = sum(1 for v in voci if v["firma"] in collidenti)
    return dizionario, avvolti, scartati_collidenti


def prova(radice: Path | None = None) -> Esito:
    radice = radice or percorsi.SORGENTE_HSP
    esito = Esito()
    for percorso in sorted(radice.glob("*.hsp")):
        grezzo = percorso.read_bytes()
        testo = grezzo.decode("cp932")
        dizionario, avvolti, collidenti = dizionario_identita(percorso.name, testo)
        nuovo, sostituzioni = applica_a_testo(percorso.name, testo, dizionario)

        esito.file_provati += 1
        esito.sostituzioni += sostituzioni
        esito.esclusi_avvolti += avvolti
        esito.esclusi_collidenti += collidenti
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
    print(f"escluse, statiche avvolte     : {esito.esclusi_avvolti}")
    print(f"escluse, firme collidenti     : {esito.esclusi_collidenti}")
    if esito.difformi:
        print("\nFILE DIFFORMI — la catena corrompe il sorgente:")
        for nome in esito.difformi:
            print(f"  {nome}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
