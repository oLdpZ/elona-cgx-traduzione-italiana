# strumenti/articolo.py
"""L'articolo italiano, derivato dal genere del nome e dalla sua prima parola.

Il dizionario porta **il genere**, non l'articolo: il genere e' cio' che non si
deduce (`pozione` femminile, `mantello` maschile, e nulla nella parola lo dice),
mentre la scelta fra `un` e `uno`, fra `la` e `l'`, e' una regola meccanica sulla
forma della parola che segue. Chiedere l'articolo a chi traduce vorrebbe dire
chiedergli di applicare a mano una regola che una macchina applica meglio, e
moltiplicare per due le occasioni di sbagliarlo.

Perche' qui e non in HSP: le regole dell'elisione sono una manciata di casi
(s impura, z, gn, ps, pn, x, y, semiconsonante, vocale, h muta) e in HSP
sarebbero un blocco di `strmid` da rileggere ogni volta. In Python si scrivono
una volta e si provano; nel gioco arriva la stringa gia' fatta, come per il
plurale.

I quattro generi sono `m`, `f`, `mp`, `fp`. Il numero fa parte del dato perche'
in italiano ci sono nomi che esistono **solo** al plurale, e in `db_item.hsp`
non sono pochi: «cianfrusaglie», «attrezzi», «vestiti», «armi». Su quelli
l'articolo indeterminativo non esiste e si usa il partitivo — «delle
cianfrusaglie» — che e' esattamente cio' che l'inglese sbaglia gia' oggi
scrivendo «a goods».
"""

GENERI = ("m", "f", "mp", "fp")

# Due insiemi, perche' le domande sono due e non coincidono.
#
# `_VOCALI_VERE` e' l'alfabeto: serve a chiedere «la lettera dopo la s e' una
# consonante?».
#
# `_ELIDONO` aggiunge la `h`, che a inizio di parola e' muta e quindi si comporta
# da vocale: «l'hotel», non «lo hotel».
#
# Tenerne uno solo, con la h dentro, fa leggere `sh` come s + vocale e produce
# «un shuriken» invece di «uno shuriken»: la h muta non rende pura la s impura.
_VOCALI_VERE = "aeiouàáèéìíòóùúAEIOUÀÁÈÉÌÍÒÓÙÚ"
_ELIDONO = _VOCALI_VERE + "hH"

# Le consonanti che chiedono `uno`/`gli`: s impura (s + consonante), z, gn, ps,
# pn, x, y. Non e' un elenco inventato: e' la regola scolastica, e i nomi del
# gioco la sollecitano davvero — «uno scudo da cavaliere», «uno sgabello tondo»,
# «uno scrittoio».
_DIGRAMMI = ("gn", "ps", "pn", "x", "y", "z")


def _vocale(carattere: str) -> bool:
    """Vero se il carattere fa elidere l'articolo. La h muta e' qui dentro."""
    return carattere in _ELIDONO


def _s_impura(parola: str) -> bool:
    """`s` seguita da consonante: «scudo», «stivale», «sgabello». Non «sale».

    Guarda le vocali vere, non quelle che elidono: «shuriken» ha una consonante
    dopo la `s`, per quanto muta.
    """
    return (len(parola) >= 2 and parola[0] in "sS"
            and parola[1] not in _VOCALI_VERE)


def _semiconsonante(parola: str) -> bool:
    """`i` seguita da vocale, come in «iato»: si comporta da consonante.

    Non tocca «identificazione» ne' «incudine», dove la `i` e' vocale piena.
    """
    return (len(parola) >= 2 and parola[0] in "iI"
            and parola[1] in "aeiouAEIOU")


def _vuole_uno(parola: str) -> bool:
    """Vero se la parola chiede `uno`/`lo`/`gli` invece di `un`/`il`/`i`."""
    if not parola:
        return False
    if _s_impura(parola) or _semiconsonante(parola):
        return True
    minuscola = parola.lower()
    return any(minuscola.startswith(d) for d in _DIGRAMMI)


def _prima_parola(nome: str) -> str:
    """La parola su cui si decide l'elisione: la prima del nome.

    E' la prima **del nome**, non della stringa che il gioco compone: quando
    l'oggetto e' composto la testa e' la parola-contatore («pozione di cura
    delle ferite lievi») e l'articolo si calcola su quella, perche' e' quella
    che sta davanti. Chi chiama passa la testa giusta.
    """
    return nome.strip().lstrip("<«“\"'([").strip()


def preposizione_di(nome: str) -> str:
    """`"di "` oppure `"d'"`, secondo la forma della parola che segue.

    Stessa famiglia dell'articolo, e per lo stesso motivo sta qui: e' una
    **derivata della forma**, non un dato da chiedere a chi traduce. Serve dove
    il giunto e' cablato nel codice del gioco invece di venire dal dizionario —
    il materiale degli oggetti, «un paio di stivali pesanti d'argento» — e
    dove percio' una preposizione sola dovrebbe coprire trentotto parole
    diverse.

    Divide le parole esattamente come `articoli`, e non e' un caso: la domanda
    e' la stessa. Se rispondessero in modo diverso il gioco direbbe «uno iato»
    e «d'iato» nella stessa riga.

        preposizione_di("ferro")     ->  "di "
        preposizione_di("argento")   ->  "d'"
        preposizione_di("iato")      ->  "di "
    """
    parola = _prima_parola(nome)
    if not parola:
        return ""
    if _vocale(parola[0]) and not _semiconsonante(parola):
        return "d'"
    return "di "


def articoli(genere: str, nome: str) -> tuple[str, str]:
    """(indeterminativo, determinativo) gia' pronti da concatenare al nome.

    Portano lo spazio dentro quando serve e non quando no: `"una "` ma `"un'"`,
    cosi' chi li usa concatena e basta. In HSP la concatenazione non sa nulla
    dell'apostrofo, e uno spazio di troppo si vedrebbe a schermo.

        articoli("f", "pozione")   ->  ("una ", "la ")
        articoli("f", "incudine")  ->  ("un'", "l'")
        articoli("m", "scudo")     ->  ("uno ", "lo ")
        articoli("m", "anello")    ->  ("un ", "l'")
        articoli("fp", "armi")     ->  ("delle ", "le ")
    """
    if genere not in GENERI:
        raise ValueError(
            f"genere {genere!r} non valido: attesi {', '.join(GENERI)}. "
            "Il numero fa parte del dato perche' in italiano ci sono nomi che "
            "esistono solo al plurale, e in db_item.hsp non sono pochi."
        )
    parola = _prima_parola(nome)
    if not parola:
        return "", ""
    vocale = _vocale(parola[0]) and not _semiconsonante(parola)
    uno = _vuole_uno(parola)

    if genere == "m":
        indeterminativo = "uno " if uno else "un "
        determinativo = "lo " if uno else ("l'" if vocale else "il ")
    elif genere == "f":
        indeterminativo = "un'" if vocale else "una "
        determinativo = "l'" if vocale else "la "
    elif genere == "mp":
        indeterminativo = "degli " if (uno or vocale) else "dei "
        determinativo = "gli " if (uno or vocale) else "i "
    else:  # fp
        indeterminativo = "delle "
        determinativo = "le "
    return indeterminativo, determinativo
