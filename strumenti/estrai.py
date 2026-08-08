# strumenti/estrai.py
"""Estrazione delle coppie (giapponese, inglese) dal sorgente HSP verso lotti JSONL.

Questo modulo possiede **l'unica** scansione del sorgente del progetto: `siti()`.
`estrai_da_testo` ci costruisce sopra i dizionari e `applica.py` ci costruisce
sopra le sostituzioni, cosi' che i due moduli camminino sugli stessi siti per
costruzione e non per disciplina.

DUE TIPI DI SITO. Il primo e' la chiamata `lang(jp, en)`, che copre il 99% del
testo. Il secondo sono i **nomi degli oggetti** di `db_item.hsp`, che stanno
fuori da `lang()` in un blocco `if ( jp ) … else …` (vedi `_ASSEGNA_NOME` e
`contratto-nomi.md`). Sono entrati qui, e non in una catena a parte, perche'
questa e' l'unica scansione: cosi' i nomi ereditano firma, `verifica`, coda di
ritraduzione di SPEC 3.1 e la prova d'identita', che li attraversa come tutto
il resto.

ESCAPE. Nel sorgente HSP il backslash e' un escape dentro i letterali: `\\"` e'
una virgoletta che **non** chiude la stringa. Ogni scansione di questo modulo lo
onora (vedi `_dentro_stringa`). Ignorarlo produceva danni silenziosi: chiamate
`lang()` scartate, span di sostituzione sbagliati e testo inglese mutilato.

FINE RIGA. Le righe si separano con `spezza_righe()`, che usa `split()` sul
terminatore effettivo del file e **non** `splitlines()`: quest'ultimo spezzerebbe
anche su `\\x0b`, `\\x0c`, `\\x1c` e U+2028, sfalsando i numeri di riga e
impedendo di riunire il testo byte per byte come l'originale. E' l'unica gestione
dei fine riga del progetto.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Iterator

from strumenti import percorsi

# lang( arg1 , arg2 ) con stringhe fra virgolette ed eventuali concatenazioni.
# Le parentesi annidate delle chiamate di funzione richiedono una scansione, non una regex sola.
_INIZIO = re.compile(r"\blang\(")


# Il secondo tipo di sito: i nomi degli oggetti di `db_item.hsp`, che stanno
# fuori da `lang()` in un blocco `if ( jp ) … else …`. Vedi `contratto-nomi.md`
# §1-2. La forma e' una sola, misurata sul sorgente pinnato: 1.321 blocchi su
# 1.321, zero eccezioni.
#
#     if ( jp ) {
#         ioriginalnameref(ITEM_ID_BANANA) = "バナナ"
#     }
#     else {
#         ioriginalnameref(ITEM_ID_BANANA) = "banana"
#         ioriginalnameref2(ITEM_ID_BANANA) = ""
#     }
#
# Il riconoscimento e' tollerante sull'indentazione e severo sulla struttura:
# pretende le sette righe nell'ordine, e **lo stesso identificatore** in tutte
# e quattro le assegnazioni. Gli `if ( jp )` di `db_item.hsp` sono 2.902 e solo
# 1.321 riguardano i nomi: agganciare gli altri per analogia e' il modo di
# corrompere il sorgente in silenzio.
_IF_JP = re.compile(r"^\s*if\s*\(\s*jp\s*\)\s*\{\s*$")
_ELSE = re.compile(r"^\s*else\s*\{\s*$")
_CHIUSA = re.compile(r"^\s*\}\s*$")
# il letterale si cammina con la regola del backslash, come ogni scansione di
# questo modulo: `\"` non chiude la stringa
_ASSEGNA_NOME = re.compile(
    r'^\s*(ioriginalnameref2?)\((\w+)\)\s*=\s*("(?:[^"\\]|\\.)*")\s*$')

_SPAZI = re.compile(r"\s+")


def normalizza_espressione(espressione: str) -> str:
    """Riduce ogni sequenza di spazi a uno solo.

    Serve a non far dipendere la chiave dall'indentazione: reindentare una riga a
    monte non deve mandare la stringa in coda di ritraduzione a testo invariato.
    """
    return _SPAZI.sub(" ", espressione).strip()


def firma(giapponese: str, inglese: str, espressione: str | None = None) -> str:
    """Chiave stabile della stringa. Se l'inglese cambia a monte, la firma si rompe di proposito.

    `espressione` va passata **solo per le dinamiche**, ed e' l'argomento inglese
    grezzo. Senza di essa due espressioni diverse che condividono i letterali
    condividono anche la chiave — `name(gdata(GDATA_RIDER)) + " glare"` e
    `cdatan(CDATAN_NAME, ttc) + " glare"` — e la traduzione dell'una finirebbe
    sull'altra portandosi **le variabili sbagliate**: 77 firme, 327 occorrenze
    reali, oggi non traducibili perche' `applica.py` le rifiuta.

    Includerla rende la chiave piu' fragile: rinominare una variabile a monte la
    rompe a testo invariato. E' la scelta giusta lo stesso, perche' i due errori
    non costano uguale. Una chiave troppo debole scrive codice sbagliato **in
    silenzio**; una chiave troppo fragile manda la stringa in coda di
    ritraduzione, dove una persona la guarda. Vedi `decisioni.md` e SPEC §3.2.
    """
    pezzi = [giapponese, inglese]
    if espressione is not None:
        pezzi.append(normalizza_espressione(espressione))
    grezzo = b"\x00".join(pezzo.encode("utf-8") for pezzo in pezzi)
    return hashlib.sha1(grezzo).hexdigest()


def _dentro_stringa(testo: str) -> list[bool]:
    """Per ogni indice, vero se quel carattere sta dentro un letterale HSP.

    Le virgolette di apertura e chiusura contano come "dentro". Dentro un
    letterale un backslash consuma il carattere successivo, quindi `\\"` non
    chiude la stringa e `\\\\` non lascia il backslash a mangiarsi la virgoletta
    che segue.
    """
    stato = [False] * len(testo)
    dentro = False
    indice = 0
    while indice < len(testo):
        carattere = testo[indice]
        if dentro:
            stato[indice] = True
            if carattere == "\\" and indice + 1 < len(testo):
                stato[indice + 1] = True
                indice += 2
                continue
            if carattere == '"':
                dentro = False
        elif carattere == '"':
            dentro = True
            stato[indice] = True
        indice += 1
    return stato


def e_dinamica(argomento_grezzo: str) -> bool:
    """Vero se l'argomento concatena qualcosa oltre a una stringa letterale.

    Il `+` va cercato **fuori** dai letterali: nel corpus reale centinaia di
    stringhe statiche contengono un `+` nel testo (`"Enchantment Bonus + 4"`,
    `"RES+ magic"`) e classificarle dinamiche fa finire l'italiano nudo,
    senza virgolette, dentro il sorgente HSP.
    """
    stato = _dentro_stringa(argomento_grezzo)
    return any(
        carattere == "+" and not dentro
        for carattere, dentro in zip(argomento_grezzo, stato)
    )


def _argomenti(testo: str, apertura: int) -> tuple[str, str, int, int] | None:
    """Argomenti grezzi di lang( ... ) piu' le posizioni del secondo.

    Ritorna (grezzo_jp, grezzo_en, inizio_en, fine_en) oppure None se malformata.
    Le posizioni servono ad applica.py per sostituire senza ricerche fragili.
    `apertura` e' l'indice della parentesi aperta e deve stare fuori da un letterale.
    """
    profondita = 0
    dentro_stringa = False
    virgola = -1
    indice = apertura
    while indice < len(testo):
        carattere = testo[indice]
        if dentro_stringa:
            # dentro un letterale il backslash consuma il carattere seguente
            if carattere == "\\":
                indice += 2
                continue
            if carattere == '"':
                dentro_stringa = False
        elif carattere == '"':
            dentro_stringa = True
        elif carattere == "(":
            profondita += 1
        elif carattere == ")":
            profondita -= 1
            if profondita == 0:
                if virgola == -1:
                    return None
                grezzo_jp = testo[apertura + 1:virgola]
                crudo_en = testo[virgola + 1:indice]
                # scarta gli spazi attorno al secondo argomento, ma tieni le posizioni reali
                scarto_sinistra = len(crudo_en) - len(crudo_en.lstrip())
                scarto_destra = len(crudo_en) - len(crudo_en.rstrip())
                inizio_en = virgola + 1 + scarto_sinistra
                fine_en = indice - scarto_destra
                return grezzo_jp.strip(), crudo_en.strip(), inizio_en, fine_en
        elif carattere == "," and profondita == 1 and virgola == -1:
            virgola = indice
        indice += 1
    return None


def argomenti_di(testo: str, apertura: int) -> list[str] | None:
    """Argomenti grezzi (N-ari) di una chiamata `nome(...)`, dato l'indice della
    parentesi aperta (fuori da un letterale).

    Generalizza `_argomenti` — che vale solo per i due argomenti di `lang()` —
    a una chiamata con un numero qualsiasi di argomenti, usata da
    `strumenti/funzioni.py` per distinguere `his(tc)` (un argomento, morfologia
    inglese) da `his(tc, 1)` (due argomenti, si localizza con `init.hsp`).
    Riusa `_dentro_stringa` per lo stato dei letterali invece di riscrivere una
    terza scansione a parentesi bilanciate. Ritorna None se la chiamata non si
    chiude nella stessa riga.
    """
    stato = _dentro_stringa(testo)
    profondita = 0
    inizio_arg = apertura + 1
    argomenti: list[str] = []
    for indice in range(apertura, len(testo)):
        if stato[indice]:
            continue
        carattere = testo[indice]
        if carattere == "(":
            profondita += 1
        elif carattere == ")":
            profondita -= 1
            if profondita == 0:
                argomenti.append(testo[inizio_arg:indice].strip())
                return argomenti
        elif carattere == "," and profondita == 1:
            argomenti.append(testo[inizio_arg:indice].strip())
            inizio_arg = indice + 1
    return None


def _letterali(argomento_grezzo: str) -> str:
    """Concatena i letterali fra virgolette, che sono la parte traducibile.

    Onora l'escape: dentro un letterale `\\"` e' una virgoletta e non una
    chiusura. Gli escape restano nel testo restituito **cosi' come compaiono
    nel sorgente** (`\\"`, non `"`): la rappresentazione e' quella del sorgente
    HSP, e chi traduce deve riprodurre una forma valida per il compilatore.
    Un letterale non chiuso si scarta, come faceva la vecchia regex.
    """
    pezzi: list[str] = []
    corrente: list[str] = []
    dentro = False
    indice = 0
    lunghezza = len(argomento_grezzo)
    while indice < lunghezza:
        carattere = argomento_grezzo[indice]
        if dentro:
            if carattere == "\\" and indice + 1 < lunghezza:
                corrente.append(argomento_grezzo[indice:indice + 2])
                indice += 2
                continue
            if carattere == '"':
                pezzi.append("".join(corrente))
                corrente = []
                dentro = False
            else:
                corrente.append(carattere)
        elif carattere == '"':
            dentro = True
        indice += 1
    return "".join(pezzi)


def virgola_nuda(argomento_grezzo: str) -> bool:
    """Vero se l'argomento contiene una virgola di primo livello.

    Una virgola cosi' e' un argomento in piu': `lang(jp, a, b)` ha tre
    argomenti per il compilatore HSP, ma `_argomenti` legge `a, b` come
    secondo argomento e non se ne accorge. Le virgole dentro una chiamata
    annidata (`cdata(A, B)`) o dentro un letterale non contano.
    """
    stato = _dentro_stringa(argomento_grezzo)
    profondita = 0
    for indice, carattere in enumerate(argomento_grezzo):
        if stato[indice]:
            continue
        if carattere == "(":
            profondita += 1
        elif carattere == ")":
            profondita -= 1
        elif carattere == "," and profondita == 0:
            return True
    return False


def avvii(riga: str) -> list[int]:
    """Indici dei `lang(` della riga che stanno **fuori** da un letterale.

    Un `lang(` che compare dentro una stringa giapponese e' testo, non codice:
    agganciarlo produce span di sostituzione corrotti.
    """
    stato = _dentro_stringa(riga)
    return [
        trovato.end() - 1
        for trovato in _INIZIO.finditer(riga)
        if not stato[trovato.start()]
    ]


def avvio_nome(riga: str) -> tuple[str, int, int] | None:
    """(letterale grezzo, inizio, fine) se la riga assegna un nome, altrimenti None.

    E' il riconoscitore **per riga**, e da solo non distingue il ramo giapponese
    da quello inglese: le due righe hanno la stessa forma. Serve a `applica.py`
    per il riscontro strutturale, che confronta la riga prodotta con quella di
    partenza e non ha bisogno di sapere quale delle due sia — la riga giapponese
    non viene mai toccata, quindi si rilegge identica.

    Chi deve sapere **quale** letterale e' traducibile usa `siti()`, che guarda
    il blocco intero.
    """
    trovato = _ASSEGNA_NOME.match(riga)
    if trovato is None:
        return None
    return trovato.group(3), trovato.start(3), trovato.end(3)


def nomi_per_riga(righe: list[str]) -> dict[int, tuple[str, str, int, int, str, str]]:
    """Indice di riga (base 0) -> (jp_grezzo, en_grezzo, inizio_en, fine_en,
    array, oggetto).

    Una voce per ciascuno dei due letterali inglesi del ramo `else`, entrambi
    col giapponese del blocco: `ioriginalnameref2` non ha un giapponese proprio
    perche' il nome giapponese non si compone (`deed of camp` e' un pezzo solo
    in giapponese). Vedi `contratto-nomi.md` §1.

    `array` e `oggetto` (`ioriginalnameref`, `ITEM_ID_BANANA`) servono al
    plurale: `applica.py` scrive `ioriginalnamerefplur(ITEM_ID_BANANA)` accanto
    al singolare, e per farlo deve sapere quale array e quale oggetto.
    """
    trovati: dict[int, tuple[str, str, int, int, str, str]] = {}
    for indice in range(len(righe) - 6):
        if not _IF_JP.match(righe[indice]):
            continue
        giapponese = _ASSEGNA_NOME.match(righe[indice + 1])
        if giapponese is None or giapponese.group(1) != "ioriginalnameref":
            continue
        if not _CHIUSA.match(righe[indice + 2]) or not _ELSE.match(righe[indice + 3]):
            continue
        primo = _ASSEGNA_NOME.match(righe[indice + 4])
        secondo = _ASSEGNA_NOME.match(righe[indice + 5])
        if primo is None or secondo is None:
            continue
        if (primo.group(1), secondo.group(1)) != ("ioriginalnameref", "ioriginalnameref2"):
            continue
        # lo stesso oggetto in tutte e quattro le assegnazioni, o non e' un blocco
        if len({giapponese.group(2), primo.group(2), secondo.group(2)}) != 1:
            continue
        if not _CHIUSA.match(righe[indice + 6]):
            continue
        grezzo_jp = giapponese.group(3)
        for scarto, trovato in ((4, primo), (5, secondo)):
            trovati[indice + scarto] = (
                grezzo_jp, trovato.group(3), trovato.start(3), trovato.end(3),
                trovato.group(1), trovato.group(2),
            )
    return trovati


def spezza_righe(testo: str) -> tuple[list[str], str, bool]:
    """(righe, fine_riga, termina_con_a_capo) — l'unica gestione dei fine riga.

    I .hsp usano CRLF. Si separa con `split()` sul terminatore effettivo, non
    con `splitlines()`, perche' quest'ultimo spezza anche su altri separatori
    unicode: sfalserebbe i numeri di riga rispetto al file reale e impedirebbe
    di riunire il testo identico all'originale.
    """
    fine_riga = "\r\n" if "\r\n" in testo else "\n"
    termina_con_a_capo = testo.endswith(fine_riga)
    righe = testo.split(fine_riga)
    if termina_con_a_capo:
        # l'ultimo elemento dopo lo split e' una stringa vuota: va scartato
        # per non aggiungere una riga fantasma in coda al riunire.
        righe = righe[:-1]
    return righe, fine_riga, termina_con_a_capo


def siti(testo: str) -> Iterator[tuple]:
    """(riga, firma, occorrenza, jp, jp_grezzo, en, en_grezzo, inizio_en, fine_en)

    L'unica scansione del sorgente del progetto. Genera un elemento per ogni
    sito **traducibile** — ben formato e con l'inglese non vuoto — nell'ordine
    in cui compaiono nel testo. I siti sono di due tipi:

    - le chiamate `lang(jp, en)`, che coprono il 99% del testo;
    - i **nomi degli oggetti** di `db_item.hsp`, che stanno fuori da `lang()`
      nella forma canonica descritta sopra (vedi `contratto-nomi.md` §2).

    Il secondo tipo entra qui, e non in una catena a parte, proprio perche'
    questa e' l'unica scansione: cosi' i nomi ereditano firma, `verifica`, coda
    di ritraduzione e — soprattutto — la prova d'identita', che e' cio' che
    tiene in piedi la garanzia byte per byte.

    `riga` e' il numero di riga a base 1; `inizio_en` e `fine_en` sono posizioni
    **dentro quella riga**. `occorrenza` e' il contatore progressivo dei
    duplicati esatti nel testo: e' diagnostico e non entra nella chiave, perche'
    il dizionario e' indicizzato per sola firma.
    """
    conteggio: dict[str, int] = {}
    righe, _, _ = spezza_righe(testo)
    nomi = nomi_per_riga(righe)

    def emetti(numero_riga, grezzo_jp, grezzo_en, inizio_en, fine_en):
        giapponese = _letterali(grezzo_jp)
        inglese = _letterali(grezzo_en)
        if not inglese:
            return None
        # solo le dinamiche portano l'espressione nella chiave: per una
        # statica il grezzo e' il letterale stesso, e includerlo sarebbe churn
        chiave = firma(giapponese, inglese,
                       grezzo_en if e_dinamica(grezzo_en) else None)
        occorrenza = conteggio.get(chiave, 0)
        conteggio[chiave] = occorrenza + 1
        return (
            numero_riga, chiave, occorrenza,
            giapponese, grezzo_jp, inglese, grezzo_en,
            inizio_en, fine_en,
        )

    for numero_riga, riga in enumerate(righe, start=1):
        for apertura in avvii(riga):
            argomenti = _argomenti(riga, apertura)
            if argomenti is None:
                continue
            sito = emetti(numero_riga, *argomenti)
            if sito is not None:
                yield sito
        nome = nomi.get(numero_riga - 1)
        if nome is not None:
            sito = emetti(numero_riga, *nome[:4])
            if sito is not None:
                yield sito


def estrai_da_testo(nome_file: str, testo: str) -> list[dict]:
    """Estrae tutte le coppie lang() da un sorgente gia' decodificato."""
    voci: list[dict] = []
    righe, _, _ = spezza_righe(testo)
    nomi = nomi_per_riga(righe)
    for sito in siti(testo):
        numero_riga, chiave, occorrenza, giapponese, grezzo_jp, inglese, grezzo_en, _, _ = sito
        dinamica = e_dinamica(grezzo_en)
        voce = {
            "firma": chiave,
            "file": nome_file,
            "riga": numero_riga,
            "occorrenza": occorrenza,
            "jp": giapponese,
            "jp_grezzo": grezzo_jp,
            "en": inglese,
            # per le dinamiche si traduce l'espressione intera: in italiano
            # l'ordine dei pezzi concatenati cambia
            "en_grezzo": grezzo_en,
            "tipo": "dinamica" if dinamica else "statica",
            "contesto": righe[numero_riga - 1] if dinamica else "",
            "it": "",
        }
        # solo i nomi hanno un plurale e un genere da portare fino al gioco: in
        # `lang()` il plurale, dove serve, sta gia' dentro la stringa, e nessuna
        # `lang()` finisce dietro un articolo scelto dal codice. `oggetto` e
        # `array` dicono a `applica.py` dove scriverli.
        nome = nomi.get(numero_riga - 1)
        if nome is not None:
            voce["plurale"] = ""
            voce["genere"] = ""
            voce["array"] = nome[4]
            voce["oggetto"] = nome[5]
        voci.append(voce)
    return voci


def estrai_da_file(percorso: Path) -> list[dict]:
    testo = percorso.read_bytes().decode("cp932")
    return estrai_da_testo(percorso.name, testo)


_CAMPI_RINVIATA = ("firma", "file", "en", "motivo")


def carica_rinviate(percorso: Path | None = None,
                    nome_file: str | None = None) -> set[str]:
    """Le firme rinviate a una fase successiva, da `rinviate.jsonl`.

    Non sono tradotte e non lo saranno in questa fase: dipendono da una
    decisione che questa fase dichiara di non prendere. Senza questo elenco
    tornerebbero in testa a ogni estrazione e andrebbero riscartate a mano.

    `nome_file` limita l'elenco al file che il rinvio riguarda, ed e' cosi' che
    lo chiama l'estrazione. La firma e' **contenuto**, non porta il file: le 157
    voci rinviate di `text.hsp` — risposte del quiz, nomi casuali — hanno per
    costruzione lo stesso contenuto dei nomi veri, e senza il filtro toglievano
    **15 nomi di `db_item.hsp`** da ogni lotto, per sempre e in silenzio
    (`ring`, `lemon`, `cherry`, `gold bar`, `broken sword`, `flag`...).

    Non c'e' nessun accoppiamento da rispettare: i dizionari sono per file,
    quindi tradurre il nome in `db_item.hsp` non tocca la risposta del quiz in
    `text.hsp`. Era una decisione presa su un file che toglieva lavoro alla coda
    di un altro. Senza `nome_file` si leggono tutte, che serve per contarle.

    `verifica --dizionario` continua a contarle fra le non tradotte, ed e'
    giusto: sono lavoro che resta, non lavoro chiuso.

    Il `motivo` e' obbligatorio, come per le toppe. Una riga senza motivo e' un
    pezzo di lavoro saltato di cui fra sei mesi nessuno sa il perche'.
    """
    percorso = percorso or (percorsi.PROGETTO / "rinviate.jsonl")
    if not percorso.exists():
        return set()
    firme = set()
    for indice, riga in enumerate(percorso.read_text(encoding="utf-8").splitlines(), start=1):
        if not riga.strip():
            continue
        voce = json.loads(riga)
        mancanti = [campo for campo in _CAMPI_RINVIATA if not voce.get(campo)]
        if mancanti:
            raise ValueError(
                f"{percorso.name}, riga {indice}: campi mancanti o vuoti: "
                f"{', '.join(mancanti)}. Una voce rinviata senza motivo e' lavoro "
                "saltato di cui fra sei mesi nessuno sa il perche'."
            )
        if nome_file is None or voce["file"] == nome_file:
            firme.add(voce["firma"])
    return firme


def da_tradurre(voci: list[dict], gia_tradotte: set[str],
                rinviate: set[str] | None = None) -> list[dict]:
    """Il lavoro che resta: una voce per firma, escluse quelle gia' tradotte.

    `estrai_da_testo` emette una voce per **occorrenza**, ed e' giusto: la prova
    d'identita' e `verifica` devono attraversare tutti i siti. Ma tradurre si
    conta in **firme** — il dizionario e' indicizzato cosi', e una stringa che
    compare tre volte e' una voce da tradurre e tre sostituzioni in fase di
    build. Senza questo filtro un lotto da 250 ne conterrebbe alcune identiche,
    e rieseguire il comando dopo la reimportazione ridarebbe le stesse voci:
    il ciclo del Task 7 non avanzerebbe.

    L'ordine del sorgente si conserva: i lotti si leggono in ordine di file, e
    per le dinamiche il contesto della riga e' spesso l'unica cosa che c'e'.
    """
    saltare = gia_tradotte | (rinviate or set())
    viste: set[str] = set()
    resta: list[dict] = []
    for voce in voci:
        chiave = voce["firma"]
        if chiave in saltare or chiave in viste:
            continue
        viste.add(chiave)
        resta.append(voce)
    return resta


def firme_tradotte(nome_file: str) -> set[str]:
    """Le firme che nel dizionario hanno gia' una traduzione non vuota."""
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    if not percorso.exists():
        return set()
    fatte = set()
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if voce.get("it"):
            fatte.add(voce["firma"])
    return fatte


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Estrae un lotto JSONL dal sorgente HSP.")
    analizzatore.add_argument("file", nargs="+", help="nomi dei file .hsp, es. text.hsp")
    analizzatore.add_argument("--uscita", required=True, help="percorso del lotto JSONL da scrivere")
    analizzatore.add_argument("--max", type=int, default=0, help="numero massimo di voci (0 = tutte)")
    analizzatore.add_argument(
        "--da-tradurre", action="store_true",
        help="solo il lavoro che resta: una voce per firma, escluse le gia' tradotte",
    )
    argomenti = analizzatore.parse_args()

    voci: list[dict] = []
    for nome in argomenti.file:
        estratte = estrai_da_file(percorsi.SORGENTE_HSP / nome)
        if argomenti.da_tradurre:
            estratte = da_tradurre(estratte, firme_tradotte(nome),
                                   carica_rinviate(None, nome))
        voci.extend(estratte)
    if argomenti.max:
        voci = voci[:argomenti.max]

    uscita = Path(argomenti.uscita)
    uscita.parent.mkdir(parents=True, exist_ok=True)
    with uscita.open("w", encoding="utf-8") as scrittura:
        for voce in voci:
            scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")
    print(f"{len(voci)} voci in {uscita}")


if __name__ == "__main__":
    main()
