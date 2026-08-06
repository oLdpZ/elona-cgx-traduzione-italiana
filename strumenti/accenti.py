"""Conversione fra italiano corretto (dizionario) e italiano CP932 (albero di build).

CP932 non contiene le vocali accentate italiane e le sostituisce silenziosamente
con la vocale nuda. La forma con apostrofo e' l'unica affidabile, ma il dizionario
conserva sempre l'accento vero: la degradazione avviene solo qui.
"""
import re

TABELLA = {
    "à": "a'", "è": "e'", "é": "e'", "ì": "i'", "ò": "o'", "ù": "u'",
    "À": "A'", "È": "E'", "É": "E'", "Ì": "I'", "Ò": "O'", "Ù": "U'",
}

# vocale nuda + apostrofo a fine parola: la forma che il traduttore non deve scrivere.
# L'elisione italiana (l'oggetto, dell'acqua) ha l'apostrofo dopo consonante,
# quindi non entra mai in questo pattern (che richiede una vocale prima).
# L'unica eccezione con vocale + apostrofo e' il troncamento "po'" (da "poco"),
# eventualmente preceduto da "un'": si esclude per elenco prima di applicare il pattern.
_TRONCAMENTI = {"po'", "Po'"}
_APOSTROFO_A_MANO = re.compile(r"[aeiouAEIOU]'(?![a-zA-Zà-ùÀ-Ù])")


def degrada(testo: str) -> str:
    """Sostituisce le vocali accentate italiane con la forma vocale + apostrofo."""
    for accentata, piana in TABELLA.items():
        testo = testo.replace(accentata, piana)
    return testo


def ha_apostrofo_scritto_a_mano(testo: str) -> bool:
    """Vero se il testo contiene una forma con apostrofo che doveva essere un accento.

    Distingue dall'elisione italiana, in cui l'apostrofo e' seguito da una
    lettera (l'oggetto, un'arma), e dal troncamento legittimo di "poco" (po').
    """
    for troncamento in _TRONCAMENTI:
        testo = testo.replace(troncamento, "")
    return _APOSTROFO_A_MANO.search(testo) is not None


def non_ascii_residuo(testo: str) -> list[str]:
    """Caratteri che CP932 non sa rappresentare: sarebbero cancellati in silenzio.

    Il giapponese preesistente non e' un residuo, perche' CP932 lo codifica.
    """
    residui = []
    for carattere in testo:
        if ord(carattere) < 128:
            continue
        try:
            ritorno = carattere.encode("cp932").decode("cp932")
        except (UnicodeEncodeError, UnicodeDecodeError):
            residui.append(carattere)
            continue
        if ritorno != carattere:
            residui.append(carattere)
    return residui
