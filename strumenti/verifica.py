# strumenti/verifica.py
"""Regole di blocco sui lotti e sul dizionario. Vedi SPEC.md paragrafo 7."""
import argparse
import json
from pathlib import Path

from strumenti.accenti import degrada, ha_apostrofo_scritto_a_mano, non_ascii_residuo
from strumenti.funzioni import funzioni_di_contenuto, morfologia_residua

_RICHIESTI = ("tipo", "en", "en_grezzo")


def _dove(voce: dict) -> str:
    """`file:riga` per un messaggio d'errore che si possa seguire."""
    return f"{voce.get('file', '?')}:{voce.get('riga', '?')}"


def controlla_voce(voce: dict) -> list[str]:
    """Ritorna la lista dei problemi. Lista vuota significa voce pulita.

    L'accesso ai campi e' coerente e difensivo: un dizionario ritoccato a mano
    con un campo mancante produce un problema che nomina file e riga, non un
    `KeyError` nudo a meta' della validazione di un lotto.
    """
    problemi: list[str] = []
    italiano = voce.get("it", "")

    mancanti = [nome for nome in _RICHIESTI if nome not in voce]
    if mancanti:
        problemi.append(f"{_dove(voce)}: campi mancanti nella voce: {', '.join(mancanti)}")
        return problemi

    tipo = voce["tipo"]
    if tipo not in ("statica", "dinamica"):
        problemi.append(f"{_dove(voce)}: tipo {tipo!r} non valido, attesi 'statica' o 'dinamica'")
        return problemi

    if not italiano.strip():
        problemi.append("traduzione vuota")
        return problemi

    # per le dinamiche il termine di paragone e' l'espressione intera
    originale = voce["en_grezzo"] if tipo == "dinamica" else voce["en"]
    if italiano == originale:
        problemi.append("traduzione identica all'inglese")

    if ha_apostrofo_scritto_a_mano(italiano):
        problemi.append(
            "apostrofo scritto a mano: nel dizionario va l'accento vero, "
            "la degradazione la fa applica.py"
        )

    # per le statiche applica.py avvolge l'italiano fra virgolette doppie
    # ("...") per farne una stringa letterale HSP: una " dentro il testo
    # chiude la stringa in anticipo e produce sorgente non compilabile.
    # Per le dinamiche invece l'italiano e' gia' un'espressione HSP intera
    # (es. name(tc) + " ha protetto " + name(x) + "."), dove le virgolette
    # doppie sono legittime e necessarie: la regola non si applica li'.
    if tipo != "dinamica" and '"' in italiano:
        problemi.append(
            'le traduzioni statiche non possono contenere il carattere " '
            "perche' romperebbe la stringa HSP generata da applica.py "
            '(lang("...", "...") si chiuderebbe in anticipo); '
            "usa le virgolette doppie tipografiche “” al suo posto "
            "(es. “ciao”) — sopravvivono al round-trip CP932, a "
            "differenza delle virgolette caporali «» che CP932 non "
            "sa codificare (UnicodeEncodeError)"
        )

    # gli accenti veri (perche') si degradano regolarmente in fase di build:
    # non sono un residuo. Il residuo vero e' cio' che resta non rappresentabile
    # anche dopo la degradazione (es. un trattino lungo, virgolette tipografiche).
    residui = non_ascii_residuo(degrada(italiano))
    if residui:
        problemi.append(f"caratteri che CP932 cancellerebbe: {residui}")

    if tipo == "dinamica":
        # la morfologia inglese (_s, is, was, your, ... e he/his/him quando
        # chiamate con un solo argomento) non e' contenuto: non passa mai da
        # lang(), quindi non si localizzera' mai, e pretendere che l'italiano
        # la conservi tal quale e' il difetto che questa funzione correggeva.
        # Il confronto vero e' sulle sole chiamate di contenuto (nomi,
        # oggetti, dati... e he/his/him quando chiamate con due argomenti);
        # i pronomi non entrano nel confronto in nessuno dei due sensi.
        attese = funzioni_di_contenuto(voce["en_grezzo"])
        trovate = funzioni_di_contenuto(italiano)
        if attese != trovate:
            problemi.append(f"interpolazioni non conservate: attese {attese}, trovate {trovate}")

        # la morfologia inglese non si localizza mai: _s(tc) scrive "s" a
        # schermo anche dentro una frase italiana, e cosi' his(tc) senza
        # secondo argomento scrive "his" per sempre
        residue = morfologia_residua(italiano)
        if residue:
            problemi.append(
                f"morfologia inglese rimasta nella traduzione: {residue}. "
                "Sono desinenze e possessivi inglesi (\"s\", \"is\", \"'s\"): "
                "in italiano vanno tolti e la frase va riscritta."
            )

    return problemi


def controlla_lotto(voci: list[dict]) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema."""
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce)
        if problemi:
            esito[voce.get("firma", _dove(voce))] = problemi
    return esito


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Verifica un lotto JSONL tradotto.")
    analizzatore.add_argument("lotto", help="percorso del lotto JSONL")
    argomenti = analizzatore.parse_args()

    voci = [json.loads(riga) for riga in Path(argomenti.lotto).read_text(encoding="utf-8").splitlines() if riga.strip()]
    esito = controlla_lotto(voci)
    if not esito:
        print(f"{len(voci)} voci, nessun problema")
        return
    for chiave, problemi in esito.items():
        print(f"{chiave}: " + "; ".join(problemi))
    raise SystemExit(f"{len(esito)} voci con problemi su {len(voci)}")


if __name__ == "__main__":
    main()
