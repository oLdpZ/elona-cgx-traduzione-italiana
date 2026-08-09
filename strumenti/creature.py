# strumenti/creature.py
"""La classe che il sorgente dichiara per ogni stringa di `db_creature.hsp`.

Il file mescola due corpora che non pongono la stessa domanda:

    return lang("吸血妊婦『ママラリア』", "<Momalaria> the bloodsucker")
    cdatan(CDATAN_NAME, rc) = lang("ビッグモスキート", "big mosquito")   ← nome
    txt lang("「ガウッ」", "*gulp*")                                     ← voce

I **nomi** sono dati che finiscono nel salvataggio e che la rinomina
dell'evoluzione taglia per prefisso o per suffisso (`action.hsp:18640`): hanno
genere, plurale, e due proprieta' da rispettare che nessun occhio verifica su
mille voci. La **voce** e' prosa fra virgolette, e non ha nessuno di quei
vincoli.

Un lotto e' una classe, e una classe pone la stessa domanda: mescolarli
significherebbe tradurre mille nomi col metodo della prosa.

⚠️ **La classe la dichiara il sito, non il contenuto.** Lo stesso nome compare
due volte — una come `return`, una come assegnazione a `cdatan` — e sono la
stessa firma: e' voluto, ed e' la ragione per cui la classe si legge dalla
riga e non dalla stringa. La stessa lezione di `categorie.py` per `db_item.hsp`.

La rete e' `nessuna_firma_in_due_classi()`: oggi le due classi sono disgiunte,
e se un domani una stringa comparisse come nome **e** come voce il criterio
tornerebbe a essere un occhio in silenzio. Meglio saperlo dal test.
"""
import argparse
import collections
import json
import re
import sys
from pathlib import Path

from strumenti import percorsi

FILE = "db_creature.hsp"

# le tre forme, misurate sul sorgente pinnato: 1.297 assegnazioni a cdatan,
# 1.144 `return` dentro *db_creature2, 1.565 `txt`. Non ce ne sono altre.
_NOME = re.compile(r"^\s*(return lang\(|cdatan\(CDATAN_NAME,\s*\w+\)\s*=\s*lang\()")
_VOCE = re.compile(r"^\s*txt\s+lang\(")
_LANG = re.compile(r'lang\("((?:[^"\\]|\\.)*)", "((?:[^"\\]|\\.)*)"\)')


def classi_da_testo(testo: str) -> dict[tuple[str, str], str]:
    """(giapponese, inglese) -> 'nome' | 'voce'.

    Le righe che non sono ne' l'una ne' l'altra forma non entrano nella mappa:
    chi le chiede se le trova assenti, invece che classificate per sbaglio.
    """
    fuori: dict[tuple[str, str], str] = {}
    for riga in testo.split("\n"):
        if _NOME.match(riga):
            classe = "nome"
        elif _VOCE.match(riga):
            classe = "voce"
        else:
            continue
        for jp, en in _LANG.findall(riga):
            fuori.setdefault((jp, en), classe)
    return fuori


def classi(percorso: Path | None = None) -> dict[tuple[str, str], str]:
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    return classi_da_testo(percorso.read_bytes().decode("cp932"))


def nessuna_firma_in_due_classi(percorso: Path | None = None) -> set[tuple[str, str]]:
    """Le coppie che compaiono sia come nome sia come voce. Oggi: nessuna.

    `classi_da_testo` tiene la prima classe vista, quindi da sola non lo direbbe:
    qui si guarda davvero riga per riga.
    """
    percorso = percorso or (percorsi.SORGENTE_HSP / FILE)
    testo = percorso.read_bytes().decode("cp932")
    viste: dict[tuple[str, str], set[str]] = collections.defaultdict(set)
    for riga in testo.split("\n"):
        if _NOME.match(riga):
            classe = "nome"
        elif _VOCE.match(riga):
            classe = "voce"
        else:
            continue
        for coppia in _LANG.findall(riga):
            viste[coppia].add(classe)
    return {k for k, v in viste.items() if len(v) > 1}


def main() -> None:
    sys.stdout = __import__("io").TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    p = argparse.ArgumentParser(description=f"Classi delle stringhe di {FILE}.")
    p.add_argument("--classe", choices=("nome", "voce"), help="elenca le voci di una classe")
    p.add_argument("--uscita", help="scrive la classe scelta come lotto JSONL")
    a = p.parse_args()

    mappa = classi()
    conto = collections.Counter(mappa.values())
    for k, v in sorted(conto.items()):
        print(f"{k:8} {v:5} firme")
    doppie = nessuna_firma_in_due_classi()
    print(f"firme in due classi: {len(doppie)}")

    if a.classe:
        from strumenti.estrai import estrai_da_file
        voci = [v for v in estrai_da_file(FILE) if mappa.get((v["jp"], v["en"])) == a.classe]
        viste, unici = set(), []
        for v in voci:
            if v["firma"] not in viste:
                viste.add(v["firma"])
                unici.append(v)
        print(f"{a.classe}: {len(unici)} firme, {len(voci)} occorrenze")
        if a.uscita:
            with open(a.uscita, "w", encoding="utf-8", newline="\n") as f:
                for v in unici:
                    f.write(json.dumps(v, ensure_ascii=False) + "\n")
            print("scritto", a.uscita)


if __name__ == "__main__":
    main()
