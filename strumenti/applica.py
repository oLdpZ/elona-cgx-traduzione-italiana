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
import stat
from pathlib import Path

from strumenti import percorsi, scene
from strumenti.accenti import degrada
from strumenti.articolo import GENERI, articoli
from strumenti.estrai import (ARRAY_IN_LANG, _argomenti, _letterali, avvii, avvio_descrizione,
                              avvio_nome, nomi_per_riga,
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
    # il terzo tipo di sito, con la stessa logica: il riconoscitore per riga
    # aggancia anche il ramo giapponese, che non viene mai toccato e si rilegge
    # identico. Nessuna riga porta insieme una `lang()`, un nome e una
    # descrizione: le tre forme si escludono per costruzione.
    descrizione = avvio_descrizione(riga)
    if descrizione is not None:
        grezzo, inizio, fine = descrizione
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


# L'array dell'articolo e' una proprieta' della **famiglia**, non della riga: la
# testa di un nome composto sta in `ioriginalnameref2`, ma il suo articolo resta
# in `ioriginalnamearticolo`, perche' l'articolo il nome ce l'ha uno solo.
ARTICOLO_DI = {
    "ioriginalnameref": "ioriginalname",
    "ioriginalnameref2": "ioriginalname",
    "fishdatan": "fishdatan",
    # il nome non identificato ha i propri: articolo e plurale appartengono al
    # sostantivo che il giocatore LEGGE, e quello e' un altro sostantivo, con un
    # altro genere. «un artefatto misterioso» prima, «una pozione di cura» dopo.
    "iknownnameref": "iknownname",
}


def _teste(nomi: dict) -> set[int]:
    """Gli indici di riga (base 0) dei siti che sono la **testa** del nome.

    La testa e' il sostantivo che sta davanti nella stringa composta, ed e'
    quello che regge l'articolo: `ioriginalnameref2` quando c'e' («pozione» di
    «pozione di cura delle ferite lievi»), altrimenti `ioriginalnameref` («spada
    lunga»). Il plurale invece riguarda **tutti** i siti, perche' il gioco puo'
    flettere l'uno o l'altro a seconda che il nome sia composto.

    ⚠️ Il composto si riconosce dal **letterale vuoto**, non dalla presenza
    della riga: `nomi_per_riga` emette sempre tutte e due le righe del ramo
    inglese, anche quando la seconda e' `ioriginalnameref2(...) = ""`. E' invece
    `estrai.siti()` a scartare i letterali vuoti, e i due non vanno confusi —
    prendere la riga per buona faceva finire l'articolo su un sito che non
    esiste, cioe' da nessuna parte, in silenzio.
    """
    teste = set()
    for riga, dati in nomi.items():
        array, oggetto = dati[4], dati[5]
        # i nomi su una riga sola non si compongono: la testa e' la riga stessa
        if array in ARRAY_IN_LANG:
            teste.add(riga)
            continue
        # nemmeno il nome non identificato si compone: `iknownnameref` non ha un
        # secondo riferimento, quindi la testa e' sempre lui
        if array == "iknownnameref":
            teste.add(riga)
            continue
        if array != "ioriginalnameref":
            continue
        gemella = nomi.get(riga + 1)
        composto = (gemella is not None
                    and gemella[4] == "ioriginalnameref2"
                    and gemella[5] == oggetto
                    and _letterali(gemella[1]) != "")
        teste.add(riga + 1 if composto else riga)
    return teste


def applica_dati_nome(nome_file: str, testo: str, dizionario: dict,
                      tradotto: str | None = None) -> tuple[str, int]:
    """Scrive plurale e articolo accanto al singolare. (testo, quante righe).

    `item_func.hsp` costruisce il plurale col **suffisso inglese** in due punti:
    sulla parola-contatore (`scroll` + "s ") e sul nome dell'oggetto
    (`long sword` + "s"). In italiano non si deduce — «paio → paia», «asse →
    assi», e l'aggettivo si accorda col nome («spada lunga → spade lunghe») —
    quindi il plurale e' un **dato**, scritto una volta per nome nel dizionario.

    Qui viaggia fino al gioco: per ogni nome tradotto che porta un `plurale` non
    vuoto si inserisce, subito sotto la riga del singolare, la riga gemella
    nell'array del plurale:

        ioriginalnameref(ITEM_ID_BANANA) = "banana"
        ioriginalnamerefplur(ITEM_ID_BANANA) = "banane"       <- inserita
        ioriginalnamearticolo(ITEM_ID_BANANA) = "una "        <- inserita
        ioriginalnamearticolodet(ITEM_ID_BANANA) = "la "      <- inserita

    L'articolo va **solo sulla testa** del nome (vedi `_teste`), perche' e' il
    sostantivo che sta davanti nella stringa composta: su «pozione di cura delle
    ferite lievi» l'articolo lo regge «pozione», non «cura». E non e' un dato del
    dizionario ma una derivata: il dizionario porta il **genere**, che non si
    deduce, e `strumenti/articolo.py` ne ricava «un/uno/una/un'» applicando le
    regole dell'elisione alla prima parola della testa.

    Gli array nuovi li dichiara una toppa su `init.hsp`, **dimensionati a
    MAX_DB** e non lasciati autoespandere come quelli che affiancano: quelli
    `db_item.hsp` li assegna per ogni oggetto, questi sono sparsi per
    costruzione, e in lettura un indice mai assegnato e' un Array overflow.
    Un plurale che manca **non e' un errore**: il
    gioco ripiega sul singolare, cosi' lo stato intermedio resta leggibile e
    migliora man mano che i lotti arrivano.

    L'ordine dei due passaggi non e' libero, ed e' il motivo dei due testi:

    - **prima** dell'inserimento, perche' le righe aggiunte spezzano la forma
      canonica del blocco (sette righe esatte) e `applica_a_testo` non
      riconoscerebbe piu' i nomi;
    - **dopo** la sostituzione, perche' i siti si cercano per firma e nel testo
      tradotto la firma non c'e' piu': l'inglese e' diventato italiano.

    Percio' `testo` e' il **sorgente**, da cui si leggono siti e firme, e
    `tradotto` e' dove le righe si inseriscono davvero. Le due versioni hanno lo
    stesso numero di righe per costruzione — la sostituzione non ne aggiunge
    mai — e se non ce l'hanno la catena si ferma invece di scrivere a caso.

    L'inserimento si fa dal fondo verso l'alto: lavorando dall'alto ogni riga
    aggiunta sfalserebbe tutte quelle sotto.
    """
    righe_sorgente, _, _ = spezza_righe(testo)
    righe, fine_riga, termina_con_a_capo = spezza_righe(
        testo if tradotto is None else tradotto)
    if len(righe) != len(righe_sorgente):
        raise SorgenteCorrotto(
            f"{nome_file}: il sorgente ha {len(righe_sorgente)} righe e il tradotto "
            f"{len(righe)}. Il plurale si aggancia per numero di riga: con i due "
            "testi sfalsati finirebbe sull'oggetto sbagliato."
        )
    nomi = nomi_per_riga(righe_sorgente)
    teste = _teste(nomi)

    inserimenti: list[tuple[int, list[str]]] = []
    for sito in siti(testo):
        numero_riga, chiave = sito[0], sito[1]
        nome = nomi.get(numero_riga - 1)
        if nome is None:
            continue
        voce = dizionario.get(chiave)
        if voce is None:
            continue
        _, _, _, _, array, oggetto = nome
        riga = righe_sorgente[numero_riga - 1]
        indentazione = riga[:len(riga) - len(riga.lstrip())]

        nuove: list[str] = []
        if voce.get("plurale"):
            plurale = degrada(voce["plurale"])
            nuove.append(f'{indentazione}{array}plur({oggetto}) = "{plurale}"')
        # l'articolo solo sulla testa, e solo se il genere c'e': un genere che
        # manca non e' un errore a valle, il gioco ripiega sull'articolo inglese
        # e lo stato intermedio resta leggibile — come per il plurale
        if (numero_riga - 1) in teste and voce.get("genere") in GENERI:
            indeterminativo, determinativo = articoli(voce["genere"], voce["it"])
            if indeterminativo:
                famiglia = ARTICOLO_DI[array]
                nuove.append(
                    f'{indentazione}{famiglia}articolo({oggetto}) = "{degrada(indeterminativo)}"')
                nuove.append(
                    f'{indentazione}{famiglia}articolodet({oggetto}) = "{degrada(determinativo)}"')
        if nuove:
            inserimenti.append((numero_riga, nuove))

    quante = sum(len(nuove) for _, nuove in inserimenti)
    for numero_riga, nuove in reversed(inserimenti):
        righe[numero_riga:numero_riga] = nuove

    risultato = fine_riga.join(righe)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, quante


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
        # `tutte` e' una deroga all'ambiguita', e una deroga si dichiara: un
        # `"si"` o un `1` letti come veri sarebbero una decisione presa per caso.
        if "tutte" in toppa and not isinstance(toppa["tutte"], bool):
            raise SorgenteCorrotto(
                f"{percorso.name}, toppa {indice}: `tutte` dev'essere true o false, "
                f"non {toppa['tutte']!r}."
            )
        if "prima" in toppa and not isinstance(toppa["prima"], bool):
            raise SorgenteCorrotto(
                f"{percorso.name}, toppa {indice}: `prima` dev'essere true o false, "
                f"non {toppa['prima']!r}."
            )
        if toppa.get("prima"):
            _controlla_toppa_prima(percorso.name, indice, toppa)
    return toppe


def letterali_di_lang(righe: list[str]) -> list[str]:
    """I letterali che stanno DENTRO una `lang(...)`, in ordine.

    Serve alla sola guardia di `prima`: una toppa che gira prima del dizionario
    non puo' toccare quel che il dizionario deve ancora agganciare.
    """
    dentro: list[str] = []
    for riga in righe:
        i = 0
        while True:
            i = riga.find("lang(", i)
            if i < 0:
                break
            profondita = 0
            j = i + 4
            in_stringa = False
            inizio = None
            while j < len(riga):
                c = riga[j]
                if in_stringa:
                    if c == "\\":
                        j += 2
                        continue
                    if c == '"':
                        in_stringa = False
                        dentro.append(riga[inizio:j + 1])
                elif c == '"':
                    in_stringa = True
                    inizio = j
                elif c == "(":
                    profondita += 1
                elif c == ")":
                    profondita -= 1
                    if profondita == 0:
                        j += 1
                        break
                j += 1
            i = j
    return dentro


def _controlla_toppa_prima(nome_file: str, indice: int, toppa: dict) -> None:
    """Una toppa `prima` non puo' cambiare il contenuto di una `lang()`.

    Se lo facesse, il dizionario — che gira dopo e cerca i siti per firma, cioe'
    per contenuto — non troverebbe piu' quel sito e lo dichiarerebbe orfano: una
    riga tornerebbe in inglese senza che nessuna guardia se ne accorga. Il caso
    per cui `prima` esiste e' l'opposto: un letterale **fuori** da ogni `lang()`
    su una riga che ne porta anche una (`config.hsp:618`).
    """
    prima = letterali_di_lang(righe_di_toppa(toppa["cerca"]))
    dopo = letterali_di_lang(righe_di_toppa(toppa["sostituisci"]))
    if prima != dopo:
        raise SorgenteCorrotto(
            f"{nome_file}, toppa {indice}: e' dichiarata `prima` ma cambia il "
            f"contenuto di una lang(): {prima} -> {dopo}. Il dizionario gira dopo e "
            "cerca i siti per contenuto: quel sito diventerebbe orfano. Una toppa "
            "che deve toccare una lang() non va dichiarata `prima`."
        )


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

    Con `"tutte": true` la toppa si applica a **ogni** occorrenza invece che
    fermarsi sull'ambiguita'. Non e' un allentamento della regola: e' una deroga
    che si dichiara una toppa alla volta, e vale dove chi la scrive ha guardato
    tutte le occorrenze e ha deciso che vogliono la stessa resa. Senza il campo
    l'ambiguita' resta un errore, perche' il caso pericoloso — stessa riga, rese
    diverse a seconda del posto — deve continuare a fermare la catena.

    ⚠️ Nata nella 50a: **125 righe su 717** di testo inglese nudo non erano
    raggiungibili da nessuna toppa, non perche' mancasse la resa ma perche' la
    schermata ripete se' stessa. Gli otto menu di `custom_tweaks.hsp` hanno lo
    stesso titolo, le dodici schermate di creazione del personaggio ripetono
    «Press F1 to show help.», e `command.hsp:2901` (« Rank.») compare nel diario
    e nella scheda. Nessuna riga di contorno le distingue: le uniche righe
    diverse portano rese che il dizionario riscrive, quindi un blocco che le
    raggiunge aggancia il sorgente pinnato ma non la build.
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
        if len(indici) > 1 and not toppa.get("tutte"):
            raise SorgenteCorrotto(
                f"{nome_file}: {quante_righe} della toppa {toppa['motivo']!r} compare "
                f"{len(indici)} volte (righe {[i + 1 for i in indici]}): e' ambigua, "
                "e indovinare significa toppare quella sbagliata una volta su due. "
                "Se tutte le occorrenze vogliono la stessa resa, dichiaralo con "
                '`"tutte": true`.'
            )
        if not toppa.get("tutte"):
            righe[indici[0]:indici[0] + len(cerca)] = sostituisci
            continue
        # ⚠️ Le occorrenze sovrapposte non si contano due volte: con `cerca` di
        #    due righe uguali fra loro e tre righe uguali nel file gli inizi
        #    possibili sono due, ma i blocchi veri sono uno solo, e sostituire
        #    dentro un pezzo gia' sostituito e' un modo di rompere in silenzio.
        #    Si prende il primo e si riparte DOPO di lui.
        scelti = []
        prossimo = 0
        for i in indici:
            if i >= prossimo:
                scelti.append(i)
                prossimo = i + len(cerca)
        # ⚠️ Si sostituisce dall'ultimo al primo: `sostituisci` puo' avere un
        #    numero di righe diverso da `cerca`, e partendo dall'inizio ogni
        #    sostituzione sposterebbe gli indici di quelle dopo.
        for i in reversed(scelti):
            righe[i:i + len(cerca)] = sostituisci

    risultato = fine_riga.join(righe)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, len(mie)


def _togli_sola_lettura(funzione, percorso, _errore) -> None:
    """Toglie la sola lettura e ritenta. Handler di `shutil.rmtree`.

    Tutte le cartelle del clone portano l'attributo di sola lettura e
    `copytree` lo copia su quelle di BUILD. Su Windows `os.rmdir` rifiuta una
    cartella con quell'attributo **anche quando e' vuota** — verificato il
    2026-08-11 su una cartella vuota in `%TEMP%` — e `rmtree` muore a meta'.

    Il guaio e' che lascia l'albero **incompleto**: `applica` si ferma, e la
    `compila` successiva dice «#Error: in line 112 [main.hsp]», che e' la riga
    dell'`#include "init.hsp"` e non dice niente della vera causa. Si perde
    tempo a cercare un difetto nella traduzione appena scritta.

    ⚠️ **Quell'attributo non e' la protezione del sorgente.** Verificato: i
    3.374 file del clone sono tutti scrivibili, solo le 34 cartelle hanno il
    flag — su Windows e' quasi sempre acceso, e non impedisce nulla. La regola
    «il sorgente upstream non si scrive mai» la tengono la disciplina e il
    **manifesto SHA-256**, non un permesso. Togliere il flag qui non toglie
    nessuna difesa: la difesa e' il manifesto, e va ricontrollato lo stesso.

    ⚠️ Si tocca **solo BUILD**, che e' usa e getta (`percorsi.BUILD`, cartella
    distinta da `percorsi.SORGENTE`): il sorgente non passa mai di qui.
    """
    percorso = Path(percorso)
    if not percorso.exists():
        return
    percorso.chmod(percorso.stat().st_mode | stat.S_IWRITE)
    funzione(percorso)


def prepara_albero() -> None:
    """Copia SORGENTE in BUILD da zero. BUILD e' usa e getta."""
    if percorsi.BUILD.exists():
        shutil.rmtree(percorsi.BUILD, onexc=_togli_sola_lettura)
    shutil.copytree(percorsi.SORGENTE, percorsi.BUILD, ignore=shutil.ignore_patterns(".git"))


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Costruisce l'albero di build col dizionario applicato.")
    analizzatore.add_argument("--salta-copia", action="store_true", help="riusa l'albero di build esistente")
    argomenti = analizzatore.parse_args()

    if not argomenti.salta_copia:
        prepara_albero()

    # ⚠️ Le toppe dichiarate `prima` girano qui, sull'albero appena copiato e
    # ancora in inglese: il loro `cerca` e' la riga del sorgente pinnato, come
    # per tutte le altre, e cosi' resta vera la guardia contro la deriva di
    # upstream (test_le_toppe_del_progetto_si_applicano_al_sorgente_pinnato).
    # Servono quando un letterale FUORI da ogni lang() vive sulla stessa riga di
    # una lang(): dopo il dizionario quella riga non e' piu' quella del sorgente,
    # e una toppa scritta sul sorgente non la troverebbe. Vedi config.hsp:618.
    toppe_tutte = carica_toppe()
    toppe_prima = [t for t in toppe_tutte if t.get("prima")]
    toppe_dopo = [t for t in toppe_tutte if not t.get("prima")]
    for nome_file in sorted({t["file"] for t in toppe_prima}):
        bersaglio = percorsi.BUILD_HSP / nome_file
        if not bersaglio.exists():
            raise SystemExit(
                f"{nome_file}: una toppa `prima` nomina un file assente dall'albero di "
                f"build ({bersaglio}). Rigenera l'albero senza --salta-copia."
            )
        testo = bersaglio.read_bytes().decode("cp932")
        try:
            nuovo, quante = applica_toppe(nome_file, testo, toppe_prima)
        except ValueError as errore:
            raise SystemExit(str(errore))
        bersaglio.write_bytes(nuovo.encode("cp932"))
        print(f"{nome_file}: {quante} toppe prima del dizionario")

    totale = 0
    totale_orfane = 0
    totale_plurali = 0  # righe di plurale e articolo
    for percorso_dizionario in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        nome_file = percorso_dizionario.stem
        # ⚠️⚠️ `scene2.hsp` NON passa di qui: le sue voci non sono firme di
        # `lang()` ma blocchi di scena, e le inietta `strumenti.scene
        # --applica` in un giro suo. Lasciandolo nel ciclo ogni resa nuova
        # diventava una «voce orfana»: alla 132a l'ATTENZIONE in coda diceva
        # 86, alla 133a diceva 258, e sarebbe salita a 1.701 a fase finita.
        # Un allarme che suona sempre e cresce e' peggio di nessun allarme,
        # perche' seppellisce l'orfana VERA -- quella che dice che il monte si
        # e' mosso sotto una resa. Vedi `strumenti/scene.py`.
        if nome_file == scene.FILE:
            continue
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
            # plurale e articolo si leggono dal sorgente (li' ci sono le firme)
            # e si scrivono nel tradotto: vedi applica_dati_nome
            nuovo, plurali = applica_dati_nome(nome_file, testo, dizionario, nuovo)
        except ValueError as errore:
            raise SystemExit(str(errore))
        bersaglio.write_bytes(nuovo.encode("cp932"))
        totale += sostituzioni
        totale_plurali += plurali

        # SPEC 3.1: al riallineamento a una nuova versione CGX le firme che non
        # esistono piu' nel sorgente sono la coda di ritraduzione. Sparire in
        # silenzio significherebbe tornare in inglese a macchia di leopardo.
        orfane = sorted(tradotte - consumate)
        totale_orfane += len(orfane)
        avviso = f", {len(orfane)} voci orfane" if orfane else ""
        avviso += f", {plurali} righe di plurale e articolo" if plurali else ""
        print(f"{nome_file}: {sostituzioni} sostituzioni{avviso}")
        for chiave in orfane[:5]:
            voce = dizionario[chiave]
            print(f"    orfana {chiave} (riga {voce.get('riga', '?')}): {voce.get('en', '')[:60]!r}")
        if len(orfane) > 5:
            print(f"    ... e altre {len(orfane) - 5}")

    # le toppe hanno un giro proprio: riguardano siti fuori da lang(), quindi
    # file che possono non avere nessuna voce di dizionario (init.hsp oggi non
    # ne ha) e che il ciclo qui sopra non visiterebbe mai
    toppe = toppe_dopo
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

    # ⚠️ I file dati si costruiscono QUI e non con un comando a parte, e non e'
    # comodita': `prepara_albero()` fa `rmtree(BUILD)`, quindi un
    # `dati_applica` lanciato prima verrebbe cancellato senza un rumore. E poi
    # la toppa che fa leggere `board_it.txt` la applica questo giro: il file e
    # l'eseguibile che lo cerca devono nascere insieme.
    if (percorsi.DIZIONARIO / "dati").is_dir():
        from strumenti import dati_applica
        dati_applica.costruisci()

    print(f"totale: {totale} sostituzioni in {percorsi.BUILD_HSP}")
    if totale_orfane:
        print(
            f"ATTENZIONE: {totale_orfane} voci di dizionario tradotte non hanno trovato "
            "la firma nel sorgente. Sono stringhe cambiate o sparite a monte: vanno ritradotte."
        )


if __name__ == "__main__":
    main()
