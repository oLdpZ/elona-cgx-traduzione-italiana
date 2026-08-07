# strumenti/applica.py
"""Costruisce l'albero di build iniettando il dizionario su una copia del sorgente.

SORGENTE non viene mai toccata: si copia in BUILD e si modifica la copia.

La scansione del sorgente non e' riscritta qui: viene da `estrai.siti()`, che e'
l'unica del progetto. Cosi' estrazione e applicazione camminano sugli stessi siti
per costruzione (vedi il test `test_scansione_condivisa`).
"""
import argparse
import json
import re
import shutil
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.estrai import (_argomenti, avvii, avvio_nome,
                              normalizza_espressione, siti, spezza_righe,
                              virgola_nuda)


class SorgenteCorrotto(ValueError):
    """Una sostituzione ha prodotto una riga che non si rilegge come l'originale."""


# Gli involucri sono due, misurati sul sorgente pinnato: cnvtalk 3.390,
# cnven 76. Non e' una famiglia aperta, ed e' giusto che un terzo involucro
# faccia fermare la catena invece di essere gestito per analogia.
INVOLUCRI = frozenset({"cnvtalk", "cnven"})

# Il gruppo 2 e' greedy fino all'ultima virgoletta prima della parentesi
# chiusa apposta: cosi' cattura tutto quello che c'e' oltre al primo letterale
# (`cnvtalk("x", "y")`, `cnvtalk("x"), cnvtalk("y")`), che va rifiutato
# esplicitamente invece di sparire in silenzio — vedi `_e_letterale_singolo`
# sotto. Il prezzo del greedy e' che il contenuto catturato puo' avere le
# parentesi sbilanciate, quindi il controllo non puo' contare su una
# profondita' sensata. `\s*` intorno alle
# parentesi accetta anche `cnvtalk( "..." )`, ma la ricostruzione in
# `riscrivi_statica` normalizza sempre a `nome("...")` senza gli spazi
# interni: e' sicuro solo perche' quella forma non esiste nel sorgente
# pinnato (0 occorrenze verificate su 3.853 chiamate). Se un domani comparisse,
# la prova d'identita' smetterebbe di riprodurre il file byte per byte e lo
# segnalerebbe.
_AVVOLTA = re.compile(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(\s*(".*")\s*\)\s*$', re.DOTALL)


def _analizza_involucro(grezzo_en: str) -> tuple[str | None, str | None]:
    """Nome dell'involucro e contenuto fra parentesi, o `(None, None)` se
    `grezzo_en` non ha la forma `nome(...)`.

    Un solo punto che applica `_AVVOLTA`: sia `riscrivi_statica` sia il
    messaggio d'errore del chiamante lo usano, cosi' la diagnosi del rifiuto
    non puo' disallinearsi dalla logica che accetta.
    """
    trovato = _AVVOLTA.match(grezzo_en)
    if not trovato:
        return None, None
    return trovato.group(1), trovato.group(2)


def _e_letterale_singolo(contenuto: str) -> bool:
    """Vero se `contenuto` e' **un solo** letterale HSP e nient'altro.

    E' la condizione esatta perche' rimpiazzare il gruppo catturato con
    `"italiano"` non perda niente: se fuori dai letterali resta anche un solo
    carattere, quel carattere sparisce nella ricostruzione.

    Non si usa `virgola_nuda` qui: quella cerca una virgola di **primo
    livello**, e il contenuto che il greedy cattura puo' essere sbilanciato.
    In `cnvtalk("x"), cnvtalk("y")` il gruppo e' `"x"), cnvtalk("y"`, dove la
    parentesi porta la profondita' a -1 prima della virgola e la virgola non
    risulta piu' di primo livello: il caso passerebbe, e la seconda chiamata
    sparirebbe. Contare i letterali invece di interpretare la struttura non ha
    quel punto cieco.
    """
    if not contenuto.startswith('"'):
        return False
    # si cammina il primo letterale con la regola del backslash e si pretende
    # che la sua chiusura sia l'ultimo carattere: cosi' `"x""y"` (due letterali
    # adiacenti, che un semplice "tutto dentro una stringa" accetterebbe) cade
    indice = 1
    while indice < len(contenuto):
        carattere = contenuto[indice]
        if carattere == "\\":
            indice += 2
            continue
        if carattere == '"':
            return indice == len(contenuto) - 1
        indice += 1
    return False


def riscrivi_statica(grezzo_en: str, italiano: str) -> str | None:
    """L'HSP da mettere al posto di `grezzo_en`, con l'italiano al posto dell'inglese.

    L'involucro si prende **dal sito**, non dalla voce di dizionario: cosi' la
    stessa traduzione serve sia `"Ciao."` sia `cnvtalk("Ciao.")`, che nel
    sorgente convivono e condividono la firma.

    `None` se la forma non e' riconosciuta, se l'involucro non e' fra quelli
    gestiti, o se fra le parentesi non c'e' esattamente un letterale
    (`cnvtalk("x", "y")`, `cnvtalk("x"), cnvtalk("y")`): in quest'ultimo caso
    sostituire il gruppo catturato con un solo letterale farebbe sparire il
    resto in silenzio, la stessa classe di corruzione che questo modulo esiste
    per evitare. Il chiamante rifiuta.
    """
    letterale = '"' + italiano + '"'
    nome, contenuto = _analizza_involucro(grezzo_en)
    if nome is not None:
        if nome in INVOLUCRI and _e_letterale_singolo(contenuto):
            return f"{nome}({letterale})"
        return None
    # una statica senza involucro e' per definizione un letterale nudo: non ha
    # un `+` di primo livello, altrimenti sarebbe classificata dinamica
    nudo = grezzo_en.strip()
    if nudo.startswith('"') and nudo.endswith('"') and len(nudo) >= 2:
        return letterale
    return None


def _profilo(riga: str) -> list[tuple[str | None, tuple[int, int] | None]]:
    """Per ogni sito della riga: il testo sostituibile e le sue posizioni.

    Copre i due tipi di sito di `estrai.siti()`: il secondo argomento di ogni
    `lang(` fuori dai letterali, e — in coda — il letterale di un'assegnazione
    `ioriginalnameref`/`ioriginalnameref2`.

    Il riconoscitore dei nomi e' quello **per riga**, che aggancia anche il ramo
    giapponese del blocco. E' voluto: qui non serve sapere quale dei due sia,
    perche' il confronto e' fra la riga di partenza e quella prodotta, e la riga
    giapponese non viene mai toccata — si rilegge identica e passa.

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
    nome = avvio_nome(riga)
    if nome is not None:
        grezzo, inizio, fine = nome
        profilo.append((grezzo, (inizio, fine)))
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

    Si pretende che: il numero di siti sulla riga sia invariato; ogni sito che
    prima si leggeva si rilegga ancora; il testo sostituibile coincida con
    quello inserito, o resti quello di partenza se non toccato. Vale per
    entrambi i tipi di sito, `lang()` e nomi (vedi `_profilo`).
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
            f"il numero di siti traducibili sulla riga passa da {len(prima)} a {len(dopo)}",
        )
    for indice, ((atteso_prima, _), (trovato, _)) in enumerate(zip(prima, dopo)):
        atteso = inseriti.get(indice, atteso_prima)
        if atteso_prima is None:
            continue  # gia' malformata in partenza: non l'abbiamo toccata
        if trovato is None:
            raise guasto(
                indice,
                f"il sito numero {indice + 1} non si rilegge "
                "(virgolette o parentesi non chiuse)",
            )
        if trovato != atteso:
            raise guasto(
                indice,
                f"il testo riletto e' {trovato!r} invece di {atteso!r}",
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
            _, chiave, _, _, _, _, grezzo_en, inizio_en, fine_en = sito

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
            # avvolta in una chiamata: cnvtalk("..."), cnven("..."). L'involucro
            # si prende dal sito (vedi riscrivi_statica), non dalla voce di
            # dizionario: cosi' la stessa voce serve sia il sito nudo sia
            # quello avvolto.
            if tipo == "statica":
                nuovo = riscrivi_statica(grezzo_en, degrada(voce["it"]))
                if nuovo is None:
                    nome_involucro, contenuto = _analizza_involucro(grezzo_en)
                    if nome_involucro in INVOLUCRI and contenuto is not None:
                        raise SorgenteCorrotto(
                            f"{nome_file}:{numero_riga} firma {chiave}: l'involucro "
                            f"{nome_involucro!r} in {grezzo_en!r} non racchiude un solo "
                            "letterale; sostituirlo con un solo letterale farebbe "
                            "sparire il resto."
                        )
                    raise SorgenteCorrotto(
                        f"{nome_file}:{numero_riga} firma {chiave}: involucro non "
                        f"riconosciuto in {grezzo_en!r}. Gli involucri gestiti sono "
                        f"{sorted(INVOLUCRI)}: se il sorgente ne ha introdotto un "
                        "altro va guardato, non gestito per analogia."
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


_CAMPI_TOPPA = ("file", "cerca", "sostituisci", "motivo")


def carica_toppe(percorso: Path | None = None) -> list[dict]:
    """Le sostituzioni fuori da `lang()`, che il dizionario non raggiunge.

    Il dizionario copre i siti `lang(jp, en)`, che sono il 99% del testo. Restano
    fuori i letterali inglesi concatenati nel codice — su tutto il sorgente gli
    articoli nudi di questo tipo sono dieci, in quattro file. `init.hsp:1718`
    (`"the " + cdatan(...)`) e' l'unico che la Fase 1 non puo' aggirare.

    Non e' una deroga alla SPEC 3.1: come il dizionario, le toppe sono **dati
    esterni applicati all'albero di build**. Il clone upstream resta intatto.

    Il file e' un'aggiunta, non un requisito: se manca, la build non ne applica
    nessuna.
    """
    percorso = percorso or (percorsi.PROGETTO / "toppe.jsonl")
    if not percorso.exists():
        return []
    toppe = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    for indice, toppa in enumerate(toppe, start=1):
        mancanti = [campo for campo in _CAMPI_TOPPA if not toppa.get(campo)]
        if mancanti:
            raise SorgenteCorrotto(
                f"{percorso.name}, toppa {indice}: campi mancanti o vuoti: "
                f"{', '.join(mancanti)}. Una toppa senza motivo e' una modifica al "
                "sorgente di cui fra sei mesi nessuno sa piu' il perche'."
            )
    return toppe


def righe_di_toppa(valore: str | list[str]) -> list[str]:
    """Le righe di `cerca`/`sostituisci`: una stringa e' un blocco di una riga.

    Le toppe sono nate per una riga sola, e la stragrande maggioranza lo resta.
    La forma a lista e' arrivata quando la composizione del nome degli oggetti
    ha chiesto uno `switch` (`item_func.hsp`, plurale della parola-contatore):
    una riscrittura che sta su piu' righe non si esprime riga per riga senza
    passare da stati intermedi che non compilano.
    """
    return list(valore) if isinstance(valore, list) else [valore]


def applica_toppe(nome_file: str, testo: str, toppe: list[dict]) -> tuple[str, int]:
    """Applica a `testo` le toppe che riguardano `nome_file`. (testo, quante).

    Una toppa si aggancia al **testo intero** delle righe, non al numero di
    riga: i numeri scivolano a ogni release CGX, il testo no. Se il blocco
    atteso non c'e' piu' o compare due volte la catena si ferma, invece di
    toppare a caso: e' la stessa scelta che governa le sostituzioni di `lang()`.

    `cerca` e `sostituisci` sono una riga sola oppure una **lista di righe
    consecutive**, e le due liste possono avere lunghezze diverse. Lo
    scivolamento dei numeri di riga che ne deriva non fa danni: le toppe girano
    dopo il dizionario, e nessuno legge piu' quei numeri dopo.
    """
    mie = [t for t in toppe if t["file"] == nome_file]
    if not mie:
        return testo, 0

    righe, fine_riga, termina_con_a_capo = spezza_righe(testo)
    for toppa in mie:
        cerca = righe_di_toppa(toppa["cerca"])
        sostituisci = righe_di_toppa(toppa["sostituisci"])
        quante_righe = "la riga" if len(cerca) == 1 else f"il blocco di {len(cerca)} righe"
        if cerca == sostituisci:
            raise SorgenteCorrotto(
                f"{nome_file}: la toppa {toppa['motivo']!r} ha cerca identica a "
                "sostituisci: non cambierebbe niente e resterebbe muta."
            )
        indici = [
            i for i in range(len(righe) - len(cerca) + 1)
            if righe[i:i + len(cerca)] == cerca
        ]
        if not indici:
            raise SorgenteCorrotto(
                f"{nome_file}: {quante_righe} della toppa {toppa['motivo']!r} non "
                f"esiste piu': {toppa['cerca']!r}. Se upstream l'ha riscritta, la "
                "toppa va rifatta sulla nuova versione, non applicata alla cieca."
            )
        if len(indici) > 1:
            raise SorgenteCorrotto(
                f"{nome_file}: {quante_righe} della toppa {toppa['motivo']!r} compare "
                f"{len(indici)} volte (righe {[i + 1 for i in indici]}): e' ambigua, "
                "e indovinare significa toppare quella sbagliata una volta su due."
            )
        righe[indici[0]:indici[0] + len(cerca)] = sostituisci

    risultato = fine_riga.join(righe)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, len(mie)


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

    # le toppe hanno un giro proprio: riguardano siti fuori da lang(), quindi
    # file che possono non avere nessuna voce di dizionario (init.hsp oggi non
    # ne ha) e che il ciclo qui sopra non visiterebbe mai
    toppe = carica_toppe()
    for nome_file in sorted({t["file"] for t in toppe}):
        bersaglio = percorsi.BUILD_HSP / nome_file
        if not bersaglio.exists():
            raise SystemExit(
                f"{nome_file}: una toppa nomina un file assente dall'albero di build "
                f"({bersaglio}). Rigenera l'albero senza --salta-copia."
            )
        testo = bersaglio.read_bytes().decode("cp932")
        try:
            nuovo, quante = applica_toppe(nome_file, testo, toppe)
        except ValueError as errore:
            raise SystemExit(str(errore))
        bersaglio.write_bytes(nuovo.encode("cp932"))
        print(f"{nome_file}: {quante} toppe")

    print(f"totale: {totale} sostituzioni in {percorsi.BUILD_HSP}")
    if totale_orfane:
        print(
            f"ATTENZIONE: {totale_orfane} voci di dizionario tradotte non hanno trovato "
            "la firma nel sorgente. Sono stringhe cambiate o sparite a monte: vanno ritradotte."
        )


if __name__ == "__main__":
    main()
