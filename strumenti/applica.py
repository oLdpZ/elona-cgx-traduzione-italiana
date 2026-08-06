# strumenti/applica.py
"""Costruisce l'albero di build iniettando il dizionario su una copia del sorgente.

SORGENTE non viene mai toccata: si copia in BUILD e si modifica la copia.
"""
import argparse
import json
import shutil

from strumenti import percorsi
from strumenti.accenti import degrada
from strumenti.estrai import _argomenti, _letterali, firma, _INIZIO


def applica_a_testo(nome_file: str, testo: str, dizionario: dict) -> tuple[str, int]:
    """Sostituisce l'argomento inglese di lang() con l'italiano degradato.

    Conserva i fine riga originali: i .hsp usano CRLF e riscriverli in LF
    produrrebbe un diff totale e potrebbe disturbare il compilatore.
    """
    sostituzioni = 0
    conteggio: dict[str, int] = {}

    # i .hsp usano CRLF; si separano le righe a mano (non con splitlines(),
    # che tratterebbe come fine riga anche altri separatori unicode) cosi'
    # da poter riunire il testo con l'identico terminatore originale.
    fine_riga = "\r\n" if "\r\n" in testo else "\n"
    termina_con_a_capo = testo.endswith(fine_riga)
    righe = testo.split(fine_riga)
    if termina_con_a_capo:
        # l'ultimo elemento dopo lo split e' una stringa vuota: va scartato
        # per non aggiungere una riga fantasma in coda al riunire.
        righe = righe[:-1]

    righe_uscita = []

    for riga in righe:
        pezzi = []
        cursore = 0
        for trovato in _INIZIO.finditer(riga):
            argomenti = _argomenti(riga, trovato.end() - 1)
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

            voce = dizionario.get(chiave)
            if voce is None or not voce.get("it"):
                continue
            if inizio_en < cursore:  # sovrapposizione: salta, non corrompere
                continue

            if voce["tipo"] == "dinamica":
                # per le dinamiche l'italiano e' gia' un'espressione HSP completa
                nuovo = degrada(voce["it"])
            else:
                nuovo = '"' + degrada(voce["it"]) + '"'

            pezzi.append(riga[cursore:inizio_en])
            pezzi.append(nuovo)
            cursore = fine_en
            sostituzioni += 1
        pezzi.append(riga[cursore:])
        righe_uscita.append("".join(pezzi))

    risultato = fine_riga.join(righe_uscita)
    if termina_con_a_capo:
        risultato += fine_riga
    return risultato, sostituzioni


def prepara_albero() -> None:
    """Copia SORGENTE in BUILD da zero. BUILD e' usa e getta."""
    if percorsi.BUILD.exists():
        shutil.rmtree(percorsi.BUILD)
    shutil.copytree(percorsi.SORGENTE, percorsi.BUILD, ignore=shutil.ignore_patterns(".git"))


def main() -> None:
    analizzatore = argparse.ArgumentParser(description="Costruisce l'albero di build col dizionario applicato.")
    analizzatore.add_argument("--salta-copia", action="store_true", help="riusa l'albero di build esistente")
    argomenti = analizzatore.parse_args()

    if not argomenti.salta_copia:
        prepara_albero()

    totale = 0
    for percorso_dizionario in sorted(percorsi.DIZIONARIO.glob("*.jsonl")):
        nome_file = percorso_dizionario.stem
        voci = [json.loads(r) for r in percorso_dizionario.read_text(encoding="utf-8").splitlines() if r.strip()]
        dizionario = {v["firma"]: v for v in voci}

        bersaglio = percorsi.BUILD_HSP / nome_file
        testo = bersaglio.read_bytes().decode("cp932")
        nuovo, sostituzioni = applica_a_testo(nome_file, testo, dizionario)
        bersaglio.write_bytes(nuovo.encode("cp932"))
        totale += sostituzioni
        print(f"{nome_file}: {sostituzioni} sostituzioni")

    print(f"totale: {totale} sostituzioni in {percorsi.BUILD_HSP}")


if __name__ == "__main__":
    main()
