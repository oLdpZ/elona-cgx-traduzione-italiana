# strumenti/applica.py
"""Costruisce l'albero di build iniettando il dizionario su una copia del sorgente.

SORGENTE non viene mai toccata: si copia in BUILD e si modifica la copia.

La scansione del sorgente non e' riscritta qui: viene da `estrai.siti()`, che e'
l'unica del progetto. Cosi' estrazione e applicazione camminano sugli stessi siti
per costruzione (vedi il test `test_scansione_condivisa`).
"""
import argparse
import json
import shutil

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.estrai import (_argomenti, avvii, normalizza_espressione, siti,
                              spezza_righe, virgola_nuda)


class SorgenteCorrotto(ValueError):
    """Una sostituzione ha prodotto una riga che non si rilegge come l'originale."""


def _profilo(riga: str) -> list[tuple[str | None, tuple[int, int] | None]]:
    """Per ogni `lang(` fuori dai letterali: il secondo argomento e le sue posizioni.

    `(None, None)` per una chiamata malformata, che va conservata com'e': se una
    riga del sorgente era gia' malformata prima di noi, non e' colpa nostra.
    """
    profilo = []
    for apertura in avvii(riga):
        argomenti = _argomenti(riga, apertura)
        if argomenti is None:
            profilo.append((None, None))
        else:
            profilo.append((argomenti[1], (argomenti[2], argomenti[3])))
    return profilo


def _riscontro(nome_file: str, numero_riga: int, riga_nuova: str,
               prima: list, inseriti: dict[int, str], chiavi: dict[int, str]) -> None:
    """Post-condizione strutturale: la riga prodotta si rilegge come quella di partenza.

    Quattro classi di traduzione passano `verifica` e producono comunque
    sorgente rotto: dinamica con virgoletta non chiusa, dinamica con parentesi
    non chiusa, dinamica con una virgola nuda (che produce un `lang()` a tre
    argomenti — virgolette pari, parentesi pari, riestrazione riuscita, nessun
    segnale) e statica che finisce con `\\` (che escapa la virgoletta di
    chiusura). Rifare il parsing della riga prodotta le copre tutte e quattro.

    Si pretende che: il numero di siti `lang()` sulla riga sia invariato;
    ogni chiamata che prima si leggeva si rilegga ancora; il secondo argomento
    coincida con quello inserito, o resti quello di partenza se non toccato.
    """
    def guasto(indice: int, motivo: str) -> SorgenteCorrotto:
        chiave = chiavi.get(indice) or next(iter(chiavi.values()), "?")
        return SorgenteCorrotto(
            f"{nome_file}:{numero_riga} firma {chiave}: {motivo}. "
            "La traduzione produce sorgente HSP non rileggibile: correggila nel dizionario."
        )

    dopo = _profilo(riga_nuova)
    if len(dopo) != len(prima):
        raise guasto(
            next(iter(inseriti), 0),
            f"il numero di chiamate lang() sulla riga passa da {len(prima)} a {len(dopo)}",
        )
    for indice, ((atteso_prima, _), (trovato, _)) in enumerate(zip(prima, dopo)):
        atteso = inseriti.get(indice, atteso_prima)
        if atteso_prima is None:
            continue  # gia' malformata in partenza: non l'abbiamo toccata
        if trovato is None:
            raise guasto(
                indice,
                f"la chiamata lang() numero {indice + 1} non si rilegge "
                "(virgolette o parentesi non chiuse)",
            )
        if trovato != atteso:
            raise guasto(
                indice,
                f"il secondo argomento riletto e' {trovato!r} invece di {atteso!r}",
            )
        if indice in inseriti and virgola_nuda(trovato):
            # virgolette pari, parentesi pari, riestrazione riuscita: senza
            # questo controllo il lang() a tre argomenti non da' alcun segnale
            raise guasto(
                indice,
                f"il secondo argomento {trovato!r} contiene una virgola di primo livello, "
                "cioe' produce un lang() a tre argomenti",
            )


def applica_a_testo(nome_file: str, testo: str, dizionario: dict,
                    consumate: set | None = None) -> tuple[str, int]:
    """Sostituisce l'argomento inglese di lang() con l'italiano degradato.

    Conserva i fine riga originali: i .hsp usano CRLF e riscriverli in LF
    produrrebbe un diff totale e potrebbe disturbare il compilatore. Lo
    spezzettamento delle righe e' quello di `estrai.spezza_righe`, condiviso
    con l'estrazione.

    Se `consumate` e' un insieme, ci finiscono le firme del dizionario
    effettivamente applicate: quelle che restano fuori sono voci orfane.
    """
    righe, fine_riga, termina_con_a_capo = spezza_righe(testo)

    # i siti raggruppati per numero di riga, cosi' da lavorare una riga alla volta
    per_riga: dict[int, list[tuple]] = {}
    for sito in siti(testo):
        per_riga.setdefault(sito[0], []).append(sito)

    sostituzioni = 0
    righe_uscita = []

    for numero_riga, riga in enumerate(righe, start=1):
        elenco = per_riga.get(numero_riga)
        if not elenco:
            righe_uscita.append(riga)
            continue

        prima = _profilo(riga)
        # i siti traducibili sono un sottoinsieme delle chiamate lang() della riga
        # (le altre hanno l'inglese vuoto): si indicizzano per posizione del
        # secondo argomento, cosi' il riscontro confronta mela con mela.
        posizione = {span: indice for indice, (_, span) in enumerate(prima) if span}

        pezzi = []
        cursore = 0
        inseriti: dict[int, str] = {}
        chiavi: dict[int, str] = {}

        for sito in elenco:
            _, chiave, _, _, _, inglese, grezzo_en, inizio_en, fine_en = sito

            voce = dizionario.get(chiave)
            if voce is None or not voce.get("it"):
                continue
            if inizio_en < cursore:  # sovrapposizione: salta, non corrompere
                continue

            tipo = voce.get("tipo")
            if tipo not in ("statica", "dinamica"):
                raise ValueError(
                    f"{nome_file}:{numero_riga} firma {chiave}: campo 'tipo' assente o "
                    f"non valido ({tipo!r}); attesi 'statica' o 'dinamica'"
                )

            # Una statica il cui argomento inglese non e' un letterale nudo e'
            # avvolta in una chiamata: cnvtalk("..."), _(...). Sostituire l'intero
            # span con un letterale FAREBBE SPARIRE la chiamata dal sorgente.
            # Sono 3.499 occorrenze reali (2.726 in db_creature.hsp, 425 in file
            # di Fase 1). Finche' la sostituzione dentro l'involucro non e'
            # implementata, si rifiuta a voce alta invece di corrompere in
            # silenzio. Vedi il rapporto della revisione finale.
            if tipo == "statica" and grezzo_en != '"' + inglese + '"':
                raise SorgenteCorrotto(
                    f"{nome_file}:{numero_riga} firma {chiave}: l'argomento inglese "
                    f"{grezzo_en!r} non e' un letterale nudo ma una chiamata che lo "
                    "avvolge; sostituirlo la farebbe sparire dal sorgente. La "
                    "sostituzione dentro l'involucro non e' ancora implementata: "
                    "togli questa voce dal dizionario."
                )

            # Da quando l'espressione entra nella firma (SPEC 3.2) due espressioni
            # diverse non condividono piu' la chiave, quindi sul sorgente questo
            # controllo non scatta piu'. Resta come difesa contro una voce di
            # dizionario ritoccata a mano: e' l'unico punto in cui una traduzione
            # scritta su un'altra espressione verrebbe fermata.
            # Il confronto e' sulla forma normalizzata, la stessa che entra nella
            # chiave: differire di soli spazi non e' un motivo per rifiutare.
            atteso_grezzo = voce.get("en_grezzo")
            if (tipo == "dinamica" and atteso_grezzo is not None
                    and normalizza_espressione(atteso_grezzo) != normalizza_espressione(grezzo_en)):
                raise SorgenteCorrotto(
                    f"{nome_file}:{numero_riga} firma {chiave}: qui l'espressione inglese "
                    f"e' {grezzo_en!r} ma la voce di dizionario e' stata tradotta su "
                    f"{atteso_grezzo!r}. Stessa firma, espressioni diverse: la traduzione "
                    "porterebbe le variabili sbagliate su questa riga."
                )

            if tipo == "dinamica":
                # per le dinamiche l'italiano e' gia' un'espressione HSP completa
                nuovo = degrada(voce["it"])
            else:
                nuovo = '"' + degrada(voce["it"]) + '"'

            pezzi.append(riga[cursore:inizio_en])
            pezzi.append(nuovo)
            cursore = fine_en
            sostituzioni += 1
            indice_sito = posizione[(inizio_en, fine_en)]
            inseriti[indice_sito] = nuovo
            chiavi[indice_sito] = chiave
            if consumate is not None:
                consumate.add(chiave)

        pezzi.append(riga[cursore:])
        riga_nuova = "".join(pezzi)
        if inseriti:
            _riscontro(nome_file, numero_riga, riga_nuova, prima, inseriti, chiavi)
        righe_uscita.append(riga_nuova)

    risultato = fine_riga.join(righe_uscita)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, sostituzioni


def prepara_albero() -> None:
    """Copia SORGENTE in BUILD da zero. BUILD e' usa e getta."""
    if percorsi.BUILD.exists():
        shutil.rmtree(percorsi.BUILD)
    shutil.copytree(percorsi.SORGENTE, percorsi.BUILD, ignore=shutil.ignore_patterns(".git"))


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Costruisce l'albero di build col dizionario applicato.")
    analizzatore.add_argument("--salta-copia", action="store_true", help="riusa l'albero di build esistente")
    argomenti = analizzatore.parse_args()

    if not argomenti.salta_copia:
        prepara_albero()

    totale = 0
    totale_orfane = 0
    for percorso_dizionario in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        nome_file = percorso_dizionario.stem
        voci = [json.loads(r) for r in percorso_dizionario.read_text(encoding="utf-8").splitlines() if r.strip()]
        dizionario = {v["firma"]: v for v in voci}
        tradotte = {c for c, v in dizionario.items() if v.get("it")}

        bersaglio = percorsi.BUILD_HSP / nome_file
        if not bersaglio.exists():
            raise SystemExit(
                f"{nome_file}: il dizionario nomina un file assente dall'albero di build "
                f"({bersaglio}). Rigenera l'albero con `python -m strumenti.applica` senza "
                "--salta-copia; se il file non esiste piu' nel sorgente CGX, la voce di "
                "dizionario va ritradotta sulla nuova versione."
            )
        testo = bersaglio.read_bytes().decode("cp932")
        consumate: set[str] = set()
        try:
            nuovo, sostituzioni = applica_a_testo(nome_file, testo, dizionario, consumate)
        except ValueError as errore:
            raise SystemExit(str(errore))
        bersaglio.write_bytes(nuovo.encode("cp932"))
        totale += sostituzioni

        # SPEC 3.1: al riallineamento a una nuova versione CGX le firme che non
        # esistono piu' nel sorgente sono la coda di ritraduzione. Sparire in
        # silenzio significherebbe tornare in inglese a macchia di leopardo.
        orfane = sorted(tradotte - consumate)
        totale_orfane += len(orfane)
        avviso = f", {len(orfane)} voci orfane" if orfane else ""
        print(f"{nome_file}: {sostituzioni} sostituzioni{avviso}")
        for chiave in orfane[:5]:
            voce = dizionario[chiave]
            print(f"    orfana {chiave} (riga {voce.get('riga', '?')}): {voce.get('en', '')[:60]!r}")
        if len(orfane) > 5:
            print(f"    ... e altre {len(orfane) - 5}")

    print(f"totale: {totale} sostituzioni in {percorsi.BUILD_HSP}")
    if totale_orfane:
        print(
            f"ATTENZIONE: {totale_orfane} voci di dizionario tradotte non hanno trovato "
            "la firma nel sorgente. Sono stringhe cambiate o sparite a monte: vanno ritradotte."
        )


if __name__ == "__main__":
    main()
