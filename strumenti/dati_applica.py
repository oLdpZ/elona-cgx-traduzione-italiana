# strumenti/dati_applica.py
"""Costruisce i file dati italiani a partire dal dizionario.

Il file italiano si posa **accanto** a quello di monte, non al posto suo:
`board.txt` resta dov'e' e nasce `board_it.txt`. E' la disciplina di
`cgx-test.exe`, che non sovrascrive `elonapluscgx.exe` — l'eseguibile inglese
continua a girare col suo file, e un confronto e' sempre a portata di mano. A
farglielo leggere e' una toppa sul nome (`init.hsp:2574` per `board.txt`).

    python -m strumenti.dati_applica              # costruisce
    python -m strumenti.dati_applica --identita   # la prova d'identita'

⚠️ **La prova d'identita' e' la verifica piu' forte di questa catena**, per lo
stesso motivo per cui lo e' sugli `.hsp`: un dizionario che traduce ogni riga in
se' stessa deve riprodurre il file **byte per byte**, e non dipende da quali
casi qualcuno si e' ricordato di coprire. Byte, non righe: i CRLF sono il punto
(65a).
"""
from __future__ import annotations

import argparse
import json

from strumenti import dati, dati_estrai, percorsi
from strumenti.accenti import degrada


def nome_italiano(nome_file: str) -> str:
    radice, punto, coda = nome_file.rpartition(".")
    return f"{radice}_it{punto}{coda}" if punto else f"{nome_file}_it"


def applica_a_testo(nome_file: str, testo: str,
                    dizionario: dict) -> tuple[str, int, list[str]]:
    """Scrive le rese dentro il testo. Torna (testo nuovo, quante, orfane).

    Le **orfane** sono le voci che non agganciano nessuna riga: vuol dire che
    monte ha riscritto quella riga, e una resa non va applicata a un testo che
    non e' piu' quello. Si contano invece di applicarle a occhio.
    """
    documento = dati.analizza_file(nome_file, testo)
    # ⚠️ `degrada()` esiste perche' CP932 cancella le vocali accentate: dove il
    # file e' UTF-8 gli accenti veri ci stanno, e degradarli sarebbe un danno.
    aggiusta = degrada if dati.codifica(nome_file) == "cp932" else (lambda s: s)
    agganciate: set[str] = set()
    quante = 0

    for blocco in documento.blocchi:
        if blocco.lingua != "EN":
            continue
        for numero, indice in enumerate(blocco.indici_pieni(), 1):
            riga = documento.riga(indice)
            firma = dati_estrai.firma(nome_file, blocco.chiave, numero, riga)
            voce = dizionario.get(firma)
            if voce is None:
                continue
            agganciate.add(firma)
            if not voce.get("it"):
                continue
            documento.sostituisci(indice, aggiusta(voce["it"]))
            quante += 1

    orfane = sorted(set(dizionario) - agganciate)
    return dati.serializza(documento), quante, orfane


def dizionario_identita(nome_file: str, testo: str) -> dict:
    """Ogni riga inglese tradotta in se' stessa."""
    voci = dati_estrai.voci(nome_file, dati.analizza_file(nome_file, testo))
    for voce in voci:
        voce["it"] = voce["en"]
    return {v["firma"]: v for v in voci}


def _dizionari() -> list:
    cartella = percorsi.DIZIONARIO / "dati"
    return sorted(cartella.glob("*.jsonl")) if cartella.is_dir() else []


def costruisci() -> int:
    percorsi.BUILD_DATI.mkdir(parents=True, exist_ok=True)
    totale = 0
    for percorso in _dizionari():
        nome_file = percorso.stem                      # board.txt.jsonl -> board.txt
        origine = percorsi.DATI_SORGENTE / nome_file
        if not origine.exists():
            raise SystemExit(f"{origine} non c'e': pinna i file dati con "
                             "`python -m strumenti.dati_sorgente --pinna`")
        voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
        dizionario = {v["firma"]: v for v in voci}
        testo = dati.leggi(origine, nome_file)
        nuovo, quante, orfane = applica_a_testo(nome_file, testo, dizionario)
        bersaglio = percorsi.BUILD_DATI / nome_italiano(nome_file)
        dati.scrivi(bersaglio, nuovo, nome_file)
        tradotte = sum(1 for v in voci if v.get("it"))
        print(f"  {nome_file}: {quante} righe scritte su {tradotte} tradotte "
              f"({len(voci)} voci){', ' + str(len(orfane)) + ' ORFANE' if orfane else ''}")
        for firma in orfane:
            voce = dizionario[firma]
            print(f"      orfana  {voce['blocco']},{voce['riga']}  {voce['en'][:60]!r}")
        totale += quante
    return totale


def prova_identita() -> bool:
    """Ogni riga tradotta in se' stessa deve ridare il file byte per byte."""
    pulita = True
    provati = righe = 0
    for nome_file in ("autopick.txt", "board.txt", "book.txt", "exhelp.txt", "talk.txt"):
        origine = percorsi.DATI_SORGENTE / nome_file
        if not origine.exists():
            continue
        grezzo = origine.read_bytes()
        testo = grezzo.decode(dati.codifica(nome_file))
        dizionario = dizionario_identita(nome_file, testo)
        nuovo, quante, orfane = applica_a_testo(nome_file, testo, dizionario)
        identico = nuovo.encode(dati.codifica(nome_file)) == grezzo
        provati += 1
        righe += quante
        if not identico or orfane:
            pulita = False
            print(f"  DIFFORME  {nome_file}  ({len(orfane)} orfane)")
        else:
            print(f"  ok        {nome_file}  {quante} righe riprodotte")
    print(f"\nfile provati: {provati}   righe sostituite: {righe}")
    return pulita


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Costruisce i file dati italiani dal dizionario.")
    analizzatore.add_argument("--identita", action="store_true",
                              help="la prova d'identita' invece della costruzione")
    argomenti = analizzatore.parse_args()

    if argomenti.identita:
        if not prova_identita():
            raise SystemExit(1)
        return

    if not _dizionari():
        raise SystemExit(f"nessun dizionario in {percorsi.DIZIONARIO / 'dati'}")
    totale = costruisci()
    print(f"\n{totale} righe scritte in {percorsi.BUILD_DATI}")


if __name__ == "__main__":
    main()
