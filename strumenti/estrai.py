# strumenti/estrai.py
"""Estrazione delle coppie lang(giapponese, inglese) dal sorgente HSP verso lotti JSONL."""
import argparse
import hashlib
import json
import re
from pathlib import Path

from strumenti import percorsi

# lang( arg1 , arg2 ) con stringhe fra virgolette ed eventuali concatenazioni.
# Le parentesi annidate delle chiamate di funzione richiedono una scansione, non una regex sola.
_INIZIO = re.compile(r"\blang\(")


def firma(giapponese: str, inglese: str) -> str:
    """Chiave stabile della stringa. Se l'inglese cambia a monte, la firma si rompe di proposito."""
    grezzo = giapponese.encode("utf-8") + b"\x00" + inglese.encode("utf-8")
    return hashlib.sha1(grezzo).hexdigest()


def e_dinamica(argomento_grezzo: str) -> bool:
    """Vero se l'argomento concatena qualcosa oltre a una stringa letterale."""
    return "+" in argomento_grezzo


def _argomenti(testo: str, apertura: int) -> tuple[str, str, int, int] | None:
    """Argomenti grezzi di lang( ... ) piu' le posizioni del secondo.

    Ritorna (grezzo_jp, grezzo_en, inizio_en, fine_en) oppure None se malformata.
    Le posizioni servono ad applica.py per sostituire senza ricerche fragili.
    """
    profondita = 0
    dentro_stringa = False
    virgola = -1
    indice = apertura
    while indice < len(testo):
        carattere = testo[indice]
        if carattere == '"':
            dentro_stringa = not dentro_stringa
        elif not dentro_stringa:
            if carattere == "(":
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
    """Concatena i letterali fra virgolette, che sono la parte traducibile."""
    return "".join(re.findall(r'"([^"]*)"', argomento_grezzo))


def estrai_da_testo(nome_file: str, testo: str) -> list[dict]:
    """Estrae tutte le coppie lang() da un sorgente gia' decodificato."""
    voci: list[dict] = []
    conteggio: dict[str, int] = {}
    for numero_riga, riga in enumerate(testo.splitlines(), start=1):
        for trovato in _INIZIO.finditer(riga):
            argomenti = _argomenti(riga, trovato.end() - 1)
            if argomenti is None:
                continue
            grezzo_jp, grezzo_en, _, _ = argomenti
            giapponese = _letterali(grezzo_jp)
            inglese = _letterali(grezzo_en)
            if not inglese:
                continue
            chiave = firma(giapponese, inglese)
            occorrenza = conteggio.get(chiave, 0)
            conteggio[chiave] = occorrenza + 1
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
                "contesto": riga if dinamica else "",
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
