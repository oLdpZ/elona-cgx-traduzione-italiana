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

# La h iniziale sta qui perche' in italiano e' muta: «l'hotel», «un'hostess».
# Per l'elisione si comporta come una vocale, e tenerla fuori darebbe «lo hotel».
_VOCALI = "aeiouàáèéìíòóùúAEIOUÀÁÈÉÌÍÒÓÙÚhH"

# Le consonanti che chiedono `uno`/`gli`: s impura (s + consonante), z, gn, ps,
# pn, x, y. Non e' un elenco inventato: e' la regola scolastica, e i nomi del
# gioco la sollecitano davvero — «uno scudo da cavaliere», «uno sgabello tondo»,
# «uno scrittoio».
_DIGRAMMI = ("gn", "ps", "pn", "x", "y", "z")


def _vocale(carattere: str) -> bool:
    return carattere in _VOCALI


def _s_impura(parola: str) -> bool:
    """`s` seguita da consonante: «scudo», «stivale», «sgabello». Non «sale»."""
    return (len(parola) >= 2 and parola[0] in "sS"
            and not _vocale(parola[1]))


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
