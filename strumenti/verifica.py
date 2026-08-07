# strumenti/verifica.py
"""Regole di blocco sui lotti e sul dizionario. Vedi SPEC.md paragrafo 7."""
import argparse
import json
from pathlib import Path

from strumenti import percorsi
from strumenti.accenti import degrada, ha_apostrofo_scritto_a_mano, non_ascii_residuo
from strumenti.estrai import estrai_da_testo
from strumenti.funzioni import funzioni_di_contenuto, morfologia_residua

_RICHIESTI = ("tipo", "en", "en_grezzo")


# Le sezioni di `invariati.md` che portano una tabella, classificate per
# prefisso del titolo. Non c'e' un default: una sezione con valori che non
# compare qui alza `ValueError`.
#
# Il motivo e' un difetto vero, trovato il 2026-08-07. Prima si leggeva "la
# tabella fino al primo `##`", e quando la sezione dei valori di dato fu
# inserita in mezzo eredito' l'esclusione **in silenzio**: le otto stringhe di
# `CDATAN_NEWSEX`, che devono restare inglesi per non rompere i salvataggi,
# non arrivavano a `controlla_voce`. Un lotto che le lasciava inglesi -- cioe'
# che faceva esattamente cio' che `invariati.md` prescrive -- inciampava nella
# regola "traduzione identica all'inglese", e `controlla_lotto` rifiutava il
# lotto **intero**. L'unico modo di far passare il lotto era tradurle: il
# controllo spingeva verso la trappola che il cancello della Fase 0 doveva
# impedire.
#
# Spostare il confine avrebbe corretto il sintomo: il prossimo che aggiunge una
# sezione avrebbe rifatto il buco. Quello che non deve piu' essere possibile e'
# il silenzio.
_SEZIONI_INVARIANTI = ("Valori di dato",)
_SEZIONI_NON_INVARIANTI = ("Da decidere", "Nomi di creatura")


def _e_invariante(titolo: str) -> bool:
    """Da che parte sta una sezione. Nessun default: o e' scritto, o si rompe."""
    for prefisso in _SEZIONI_INVARIANTI:
        if titolo.startswith(prefisso):
            return True
    for prefisso in _SEZIONI_NON_INVARIANTI:
        if titolo.startswith(prefisso):
            return False
    raise ValueError(
        f"invariati.md: la sezione {titolo!r} porta dei valori ma non e'"
        " classificata. Aggiungi il suo prefisso a _SEZIONI_INVARIANTI (i suoi"
        " valori restano inglesi per scelta) oppure a _SEZIONI_NON_INVARIANTI"
        " (sono candidati, e verifica.py deve continuare a segnalarli)."
    )


def _valore_di_riga(riga: str) -> str | None:
    """La prima cella di una riga di tabella, se e' una riga di dati.

    Un valore fra apici inversi si prende **verbatim**, spazi compresi. Serve
    perche' una cella markdown si legge con `strip()`, e alcuni invariati hanno
    uno spazio che conta: `text.hsp:62` allinea le sigle delle statistiche con
    `lang("感覚", " PER")`, e la sigla italiana e' " PER" identica — una
    coincidenza legittima, non una traduzione dimenticata. Gli apici inversi
    sono gia' la convenzione del progetto per il codice dentro la prosa.
    """
    spoglia = riga.strip()
    if not spoglia.startswith("|"):
        return None
    celle = [cella.strip() for cella in spoglia.strip("|").split("|")]
    if len(celle) < 2 or not celle[0] or celle[0] == "valore":
        return None
    if set(celle[0]) <= {"-", ":"}:  # riga separatrice
        return None
    valore = celle[0]
    if len(valore) >= 2 and valore.startswith("`") and valore.endswith("`"):
        return valore[1:-1]
    return valore


def carica_invariati(percorso: Path | None = None) -> set[str]:
    """I valori che possono restare identici all'inglese senza che sia un difetto.

    Il file e' un'aggiunta, non un requisito: se manca, la regola si comporta
    come prima. Un progetto senza eccezioni e' un progetto senza il file.

    Si legge **sezione per sezione**. La tabella iniziale, prima di ogni
    titolo, sono gli invariati per scelta esplicita. Le sezioni successive
    valgono secondo `_SEZIONI_INVARIANTI` e `_SEZIONI_NON_INVARIANTI`: alcune
    elencano valori che devono restare inglesi (i valori di dato), altre
    elencano candidati non ancora accettati, e leggerle li renderebbe
    invariati di fatto, cioe' l'opposto di cio' che dichiarano.

    Una sezione che porta valori senza essere classificata alza `ValueError`.
    Una sezione di sola prosa non e' una decisione da prendere, e si ignora.
    """
    percorso = percorso or (percorsi.PROGETTO / "invariati.md")
    if not percorso.exists():
        return set()

    # prima si raccoglie per sezione, poi si classifica: cosi' una sezione di
    # sola prosa non deve essere classificata, perche' non ha valori da dare
    titolo = ""  # la tabella iniziale, che non ha titolo
    per_sezione: dict[str, list[str]] = {titolo: []}
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        spoglia = riga.strip()
        # solo `##` e oltre aprono una sezione: `#` e' il titolo del
        # documento, e la tabella che lo segue e' la prima, senza sezione
        if spoglia.startswith("##"):
            titolo = spoglia.lstrip("#").strip()
            per_sezione.setdefault(titolo, [])
            continue
        valore = _valore_di_riga(spoglia)
        if valore is not None:
            per_sezione[titolo].append(valore)

    valori: set[str] = set()
    for titolo, trovati in per_sezione.items():
        if not trovati:
            continue
        if titolo == "" or _e_invariante(titolo):
            valori.update(trovati)
    return valori


def _dove(voce: dict) -> str:
    """`file:riga` per un messaggio d'errore che si possa seguire."""
    return f"{voce.get('file', '?')}:{voce.get('riga', '?')}"


def controlla_voce(voce: dict, invariati: set[str] | None = None) -> list[str]:
    """Ritorna la lista dei problemi. Lista vuota significa voce pulita.

    L'accesso ai campi e' coerente e difensivo: un dizionario ritoccato a mano
    con un campo mancante produce un problema che nomina file e riga, non un
    `KeyError` nudo a meta' della validazione di un lotto.

    `invariati` sono i valori che possono restare identici all'inglese senza
    che sia un difetto. Il default `None` non legge il disco e non cambia il
    comportamento dei chiamanti esistenti: il file lo carica `controlla_lotto`
    una volta sola.
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

    # Un invariato fatto di soli spazi non e' una traduzione vuota: `text.hsp:198`
    # e' `strblank = lang("", " ")`, uno spazio di RIEMPIMENTO. Senza questa
    # eccezione la regola scattava prima di quella sugli invariati, e quel valore
    # era irraggiungibile per costruzione — nessuna traduzione lo faceva passare,
    # nemmeno quella giusta. La regola resta per tutto il resto, dove una
    # traduzione vuota e' quasi sempre una riga dimenticata.
    if not italiano.strip() and italiano not in (invariati or set()):
        problemi.append("traduzione vuota")
        return problemi

    # per le dinamiche il termine di paragone e' l'espressione intera
    originale = voce["en_grezzo"] if tipo == "dinamica" else voce["en"]
    # il confronto e' sulla stringa intera: `Vernis` fra gli invariati zittisce
    # la voce che vale esattamente "Vernis", non una frase che lo contiene —
    # quella, se e' rimasta inglese, e' proprio cio' che la regola cerca
    if italiano == originale and italiano not in (invariati or set()):
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


def controlla_lotto(voci: list[dict], invariati: set[str] | None = None) -> dict[str, list[str]]:
    """Mappa firma -> problemi, per le sole voci con almeno un problema.

    Gli invariati si caricano una volta sola qui, non a ogni voce: rileggere il
    file per ognuna delle 6.688 voci di un lotto sarebbe assurdo. I test lo
    passano gia' risolto per non toccare il disco.
    """
    invariati = carica_invariati() if invariati is None else invariati
    esito: dict[str, list[str]] = {}
    for voce in voci:
        problemi = controlla_voce(voce, invariati)
        if problemi:
            esito[voce.get("firma", _dove(voce))] = problemi
    return esito


def confronta_col_sorgente(nome_file: str) -> tuple[list[dict], int]:
    """Coda di ritraduzione per un file: SPEC 3.1.

    Ritorna le voci tradotte la cui firma **non esiste piu'** nel sorgente — la
    stringa e' cambiata o sparita a monte, e la traduzione va rifatta — e quante
    firme del sorgente non hanno ancora una traduzione.

    Sono due domande diverse e vanno lette insieme: un dizionario puo' essere
    completo e tutto da ritradurre.

    Una voce con `it` vuoto non e' orfana: non c'e' nessun lavoro da rifare, e
    contarla gonfierebbe il numero che decide se la catena si ferma.
    """
    percorso = percorsi.DIZIONARIO / f"{nome_file}.jsonl"
    voci = []
    if percorso.exists():
        voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    tradotte = {v["firma"]: v for v in voci if v.get("it")}

    # un .hsp puo' sparire a monte fra due versioni CGX: e' il caso che SPEC 3.1
    # contempla, e un read_bytes nudo lo trasformerebbe in un FileNotFoundError
    # a meta' scansione invece che in una coda da ritradurre
    sorgente = percorsi.SORGENTE_HSP / nome_file
    if sorgente.exists():
        nel_sorgente = {v["firma"] for v in estrai_da_testo(nome_file, sorgente.read_bytes().decode("cp932"))}
    else:
        nel_sorgente = set()

    orfane = [v for f, v in tradotte.items() if f not in nel_sorgente]
    non_tradotte = len(nel_sorgente - set(tradotte))
    return sorted(orfane, key=lambda v: v.get("riga", 0)), non_tradotte


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Verifica un lotto JSONL tradotto.")
    analizzatore.add_argument("lotto", nargs="?", help="percorso del lotto JSONL")
    analizzatore.add_argument(
        "--dizionario", action="store_true",
        help="confronta il dizionario col sorgente invece di validare un lotto")
    argomenti = analizzatore.parse_args()

    if argomenti.dizionario:
        totale_orfane = 0
        for percorso in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
            orfane, non_tradotte = confronta_col_sorgente(percorso.stem)
            totale_orfane += len(orfane)
            print(f"{percorso.stem}: {len(orfane)} da ritradurre, {non_tradotte} non ancora tradotte")
            for voce in orfane[:5]:
                print(f"    {voce['firma'][:10]} (riga {voce.get('riga', '?')}): {voce.get('en', '')[:60]!r}")
            if len(orfane) > 5:
                print(f"    ... e altre {len(orfane) - 5}")
        raise SystemExit(1 if totale_orfane else 0)

    if argomenti.lotto is None:
        analizzatore.error("serve il percorso di un lotto, oppure --dizionario")

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
