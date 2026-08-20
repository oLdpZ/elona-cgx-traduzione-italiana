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
# Il troncamento va tolto solo quando e' parola a se stante, non quando e' la
# coda di una parola piu' lunga (es. "rida'" contiene "da'" ma non e' un
# troncamento legittimo: e' la forma sbagliata di "ridà"). Il confine va
# controllato PRIMA del troncamento: un lookbehind negativo su una lettera,
# perche' un \b subito dopo l'apostrofo finale non si comporta come un
# confine di parola normale (l'apostrofo non e' un carattere di parola).
_TRONCAMENTI_PATTERN = re.compile(
    r"(?<![a-zA-Zà-ùÀ-Ù])(?:"
    + "|".join(re.escape(t) for t in sorted(_TRONCAMENTI, key=len, reverse=True))
    + ")"
)
_APOSTROFO_A_MANO = re.compile(r"[aeiouAEIOU]'(?![a-zA-Zà-ùÀ-Ù])")


def degrada(testo: str) -> str:
    """Sostituisce le vocali accentate italiane con la forma vocale + apostrofo."""
    for accentata, piana in TABELLA.items():
        testo = testo.replace(accentata, piana)
    return testo


# ⚠️⚠️ L'ACCENTO SI DEGRADA ANCHE QUANDO STA IN MEZZO ALLA PAROLA, E LI' NON
# SI PUO' LEGGERE. La degradazione ad apostrofo funziona perche' in italiano
# l'accento cade quasi sempre sull'ULTIMA lettera, e li' l'apostrofo e' quel che
# la lingua scrive comunque: «piu'», «citta'», «perche'». Ma «élite» e «dèi»
# portano l'accento DENTRO, e a schermo diventano «e'lite» e «de'i»: illeggibili.
#
# La lezione e' della 41a (2026-08-14), che concludeva «si evita la parola, non
# si toglie l'accento» — e per settantuno sessioni non e' stata una rete, ma una
# cosa da ricordarsi. Nella 71a la misura sul dizionario intero ha trovato
# **quindici** «dèi», tutti scritti dopo quella lezione.
_ACCENTATE = "àèéìòùÀÈÉÌÒÙ"
# `[^\W\d_]` e' "una lettera": esclude cifre e trattini, quindi «cosi'-cosi'» e
# «Perché?» non entrano — l'accento e' l'ultimo carattere della loro parola.
_ACCENTO_INTERNO = re.compile(r"[^\W\d_]*[" + _ACCENTATE + r"][^\W\d_]+")


def accenti_interni(testo: str) -> list[str]:
    """Le parole con una vocale accentata seguita da altre lettere.

    Sono quelle che `degrada` rende illeggibili: l'apostrofo finisce in mezzo
    alla parola. Le parole con l'accento sull'ultima lettera - la stragrande
    maggioranza dell'italiano - non entrano.
    """
    return sorted(set(_ACCENTO_INTERNO.findall(testo)))


def ha_apostrofo_scritto_a_mano(testo: str) -> bool:
    """Vero se il testo contiene una forma con apostrofo che doveva essere un accento.

    Distingue dall'elisione italiana, in cui l'apostrofo e' seguito da una
    lettera (l'oggetto, un'arma), e dai troncamenti legittimi elencati in
    `_TRONCAMENTI` (imperativi monosillabici e "po'"), riconosciuti solo
    come parola a se stante e non come coda di una parola piu' lunga
    (es. "rida'" resta segnalato). Vedi il docstring del modulo per il
    compromesso noto su "da'" e "di'".
    """
    testo = _TRONCAMENTI_PATTERN.sub("", testo)
    return _APOSTROFO_A_MANO.search(testo) is not None


# L'unico carattere a due byte che la build inglese disegna bene, perche' non lo
# disegna affatto: `msg_write` (init.hsp:1374) lo cerca nella stringa e ci mette
# un'icona al posto suo. E' anche l'unico che l'inglese upstream si permette, una
# volta sola in tutto il sorgente (`*beep♪*`, db_creature.hsp).
_DOPPI_AMMESSI = frozenset("♪")


def doppi_byte_cp932(testo: str) -> list[str]:
    """Caratteri che CP932 codifica su due byte: illeggibili nella build inglese.

    Misurato a schermo il 2026-08-11. `init.hsp:1391` sceglie il font con
    `lang(cfg_font1, cfg_font2)`, e per l'inglese `cfg_font2` e' `Courier New`
    (`config.txt:75`), un font latino: `mes` disegna **un glifo per byte**, cosi'
    「・」 (0x81 0x45) e' uscito come nulla + `E` — «EVisitare le Terre selvagge».
    I quattro punti che sanno riconoscere un byte guida (`init.hsp:1295`,
    `module.hsp:57` e `:4932`, `system.hsp:4050`) fanno il controllo solo dentro
    `if ( jp )`.

    Diverso da `non_ascii_residuo`, che guarda cosa CP932 **non sa codificare**:
    「…」 e 「“”」 CP932 le codifica benissimo, e infatti passavano — ma a due
    byte, quindi a schermo erano `...c` e `g`. Il round-trip non basta come prova:
    va contato il numero di byte.
    """
    residui = []
    for carattere in testo:
        if ord(carattere) < 128 or carattere in _DOPPI_AMMESSI:
            continue
        try:
            if len(carattere.encode("cp932")) > 1:
                residui.append(carattere)
        except UnicodeEncodeError:
            # non codificabile: e' un problema, ma lo nomina non_ascii_residuo
            continue
    return residui


def virgolette_non_protette(testo: str) -> bool:
    """Vero se il testo porta una `"` che chiuderebbe la stringa HSP.

    `applica.py` avvolge la statica fra virgolette doppie, ma HSP conosce
    l'escape `\\"` e upstream lo usa (`text.hsp:9879` scrive `\\"Project LF\\"`),
    quindi la virgoletta protetta e' legittima: e' l'unico modo di citare, dopo
    che le tipografiche 「“”」 si sono rivelate illeggibili nella build inglese.
    Si cammina la stringa con la regola del backslash, come `applica.py`.
    """
    indice = 0
    while indice < len(testo):
        if testo[indice] == "\\":
            indice += 2
            continue
        if testo[indice] == '"':
            return True
        indice += 1
    return False


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
