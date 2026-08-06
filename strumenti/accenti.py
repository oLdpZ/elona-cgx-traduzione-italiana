"""Conversione fra italiano corretto (dizionario) e italiano CP932 (albero di build).

CP932 non contiene le vocali accentate italiane e le sostituisce silenziosamente
con la vocale nuda. La forma con apostrofo e' l'unica affidabile, ma il dizionario
conserva sempre l'accento vero: la degradazione avviene solo qui.

COMPROMESSO NOTO in `ha_apostrofo_scritto_a_mano`: l'elenco `_TRONCAMENTI` esclude
gli imperativi monosillabici italiani (va', fa', da', di', sta', to', mo', be', po')
dal rilevamento, perche' sono forme legittime con vocale + apostrofo. Per la maggior
parte di questi l'esclusione e' sicura, perche' la vocale accentata corrispondente
non esiste o e' errata in italiano. Per due casi pero' l'esclusione puo' mascherare
un errore vero:
- "da'" e' l'imperativo di "dare", ma "dà" (terza persona, "lui dà") e' molto piu'
  frequente nel testo di un gioco. Un traduttore che scrive "da'" intendendo "dà"
  non verra' segnalato.
- "di'" e' l'imperativo di "dire", mentre "dì" significa "giorno".
Si accetta questo compromesso perche' un falso positivo e' piu' dannoso di questo
falso negativo: il falso positivo colpirebbe traduzioni corrette e frequenti (e
insegnerebbe al traduttore a ignorare gli avvisi del verificatore), mentre il falso
negativo colpisce un errore raro. Scelta deliberata, non una svista.
"""
import re

TABELLA = {
    "à": "a'", "è": "e'", "é": "e'", "ì": "i'", "ò": "o'", "ù": "u'",
    "À": "A'", "È": "E'", "É": "E'", "Ì": "I'", "Ò": "O'", "Ù": "U'",
}

# vocale nuda + apostrofo a fine parola: la forma che il traduttore non deve scrivere.
# L'elisione italiana (l'oggetto, dell'acqua) ha l'apostrofo dopo consonante,
# quindi non entra mai in questo pattern (che richiede una vocale prima).
# Le eccezioni con vocale + apostrofo sono l'elenco chiuso degli imperativi
# monosillabici italiani (e "po'", troncamento di "poco"): si escludono per
# elenco prima di applicare il pattern. Vedi il docstring del modulo per il
# compromesso noto su "da'" e "di'".
_TRONCAMENTI = {
    "va'", "Va'", "fa'", "Fa'", "da'", "Da'", "di'", "Di'",
    "sta'", "Sta'", "to'", "To'", "mo'", "Mo'", "be'", "Be'", "po'", "Po'",
}
_APOSTROFO_A_MANO = re.compile(r"[aeiouAEIOU]'(?![a-zA-Zà-ùÀ-Ù])")


def degrada(testo: str) -> str:
    """Sostituisce le vocali accentate italiane con la forma vocale + apostrofo."""
    for accentata, piana in TABELLA.items():
        testo = testo.replace(accentata, piana)
    return testo


def ha_apostrofo_scritto_a_mano(testo: str) -> bool:
    """Vero se il testo contiene una forma con apostrofo che doveva essere un accento.

    Distingue dall'elisione italiana, in cui l'apostrofo e' seguito da una
    lettera (l'oggetto, un'arma), e dai troncamenti legittimi elencati in
    `_TRONCAMENTI` (imperativi monosillabici e "po'"). Vedi il docstring del
    modulo per il compromesso noto su "da'" e "di'".
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
