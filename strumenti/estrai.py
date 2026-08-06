# strumenti/estrai.py
"""Estrazione delle coppie lang(giapponese, inglese) dal sorgente HSP verso lotti JSONL.

Questo modulo possiede **l'unica** scansione del sorgente del progetto: `siti()`.
`estrai_da_testo` ci costruisce sopra i dizionari e `applica.py` ci costruisce
sopra le sostituzioni, cosi' che i due moduli camminino sugli stessi siti per
costruzione e non per disciplina.

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


def firma(giapponese: str, inglese: str) -> str:
    """Chiave stabile della stringa. Se l'inglese cambia a monte, la firma si rompe di proposito."""
    grezzo = giapponese.encode("utf-8") + b"\x00" + inglese.encode("utf-8")
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
    chiamata `lang()` **traducibile** — cioe' ben formata e con l'argomento
    inglese non vuoto — nell'ordine in cui compaiono nel testo.

    `riga` e' il numero di riga a base 1; `inizio_en` e `fine_en` sono posizioni
    **dentro quella riga**. `occorrenza` e' il contatore progressivo dei
    duplicati esatti nel testo: e' diagnostico e non entra nella chiave, perche'
    il dizionario e' indicizzato per sola firma.
    """
    conteggio: dict[str, int] = {}
    righe, _, _ = spezza_righe(testo)
    for numero_riga, riga in enumerate(righe, start=1):
        for apertura in avvii(riga):
            argomenti = _argomenti(riga, apertura)
            if argomenti is None:
                continue
            grezzo_jp, grezzo_en, inizio_en, fine_en = argomenti
            giapponese = _letterali(grezzo_jp)
            inglese = _letterali(grezzo_en)
            if not inglese:
                continue
            chiave = firma(giapponese, inglese)
            occorrenza = conteggio.get(chiave, 0)
            conteggio[chiave] = occorrenza + 1
            yield (
                numero_riga, chiave, occorrenza,
                giapponese, grezzo_jp, inglese, grezzo_en,
                inizio_en, fine_en,
            )


def estrai_da_testo(nome_file: str, testo: str) -> list[dict]:
    """Estrae tutte le coppie lang() da un sorgente gia' decodificato."""
    voci: list[dict] = []
    righe, _, _ = spezza_righe(testo)
    for sito in siti(testo):
        numero_riga, chiave, occorrenza, giapponese, grezzo_jp, inglese, grezzo_en, _, _ = sito
        dinamica = e_dinamica(grezzo_en)
        voci.append({
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
        })
    return voci


def estrai_da_file(percorso: Path) -> list[dict]:
    testo = percorso.read_bytes().decode("cp932")
    return estrai_da_testo(percorso.name, testo)


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Estrae un lotto JSONL dal sorgente HSP.")
    analizzatore.add_argument("file", nargs="+", help="nomi dei file .hsp, es. text.hsp")
    analizzatore.add_argument("--uscita", required=True, help="percorso del lotto JSONL da scrivere")
    analizzatore.add_argument("--max", type=int, default=0, help="numero massimo di voci (0 = tutte)")
    argomenti = analizzatore.parse_args()

    voci: list[dict] = []
    for nome in argomenti.file:
        voci.extend(estrai_da_file(percorsi.SORGENTE_HSP / nome))
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
