# -*- coding: utf-8 -*-
"""Ogni regola del modello `autopick.txt` aggancia davvero qualcosa?

⚠️⚠️ **E' la rete che il difetto della 98a chiedeva e che non esisteva.**
`custom_autopick.hsp:358` confronta le regole col **nome dell'oggetto**, che
nella nostra build e' italiano, mentre il modello che il gioco copia nel
salvataggio porta i nomi **inglesi**: `gold piece` non aggancia «moneta d'oro»,
e quelle righe non pescano niente da quando `db_item.hsp` e' tradotto. Nessun
conteggio del progetto lo vedeva, perche' `autopick.txt` non stava in nessuno.

La rete rifa' a mano quel che fa `*AutoPickTest` (`:115`-`:361`):

    toglie i marcatori `~ ! !! ? % = :sound123`, poi `strtrim` e gli spazi
    doppi, poi mette uno spazio davanti e uno dietro; passa la catena dei
    MODIFICATORI, che si tolgono da `s` quando agganciano; e su quel che resta
    chiede o un TIPO o un pezzo di NOME di oggetto.

    python scratchpad/_100-modello-aggancia.py             # italiano contro italiano
    python scratchpad/_100-modello-aggancia.py --en        # inglese contro inglese
    python scratchpad/_100-modello-aggancia.py --scaduto   # chiavi ITA, modello INGLESE

⚠️ **Prova al contrario**: `--scaduto` e' lo stato in cui il gioco si troverebbe
se si traducesse il solo `.hsp`, e deve accendersi su **tutt'e undici** le regole
d'esempio — non sei, come stimava la 98a: i sei nomi di oggetto piu' le cinque
righe che cominciano con un selettore, perche' anche quelle diventano parole che
l'eseguibile non cerca piu'. Se tace, la rete non guarda niente.
`--en` e' monte contro se stesso e deve dare **uno** (vedi `attese`).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from strumenti import dati, percorsi

sys.path.insert(0, str(Path(__file__).resolve().parent))
_ombra = __import__("importlib").import_module("importlib.util")
_spec = _ombra.spec_from_file_location(
    "ombra", Path(__file__).resolve().parent / "_100-selettori-ombra.py")
ombra = _ombra.module_from_spec(_spec)
_spec.loader.exec_module(ombra)


def marcatori_via(riga: str) -> str:
    """Quel che resta della riga dopo i marcatori, come fa `:119`-`:145`."""
    testo = riga.split("#")[0]
    if "!!" in testo:
        testo = testo.split("!!", 1)[1]
    elif "!" in testo or "~" in testo:
        testo = re.sub(r"^[^!~]*[!~]", "", testo, count=1)
    testo = testo.split("?")[0].split(":sound")[0]
    return re.sub(r" +", " ", testo.strip())


def nomi_di_oggetto(colonna: str) -> list[str]:
    percorso = percorsi.DIZIONARIO / "db_item.hsp.jsonl"
    voci = [json.loads(r) for r in percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    campo = "en" if colonna == "en" else "it"
    return [v[campo].lower() for v in voci if v.get(campo)]


def main() -> None:
    analizzatore = argparse.ArgumentParser(
        description="Le regole del modello contro le chiavi dell'eseguibile.")
    gruppo = analizzatore.add_mutually_exclusive_group()
    gruppo.add_argument("--en", action="store_true",
                        help="monte contro se stesso: chiavi e modello inglesi")
    gruppo.add_argument("--scaduto", action="store_true",
                        help="chiavi italiane e modello inglese: il difetto della 98a")
    argomenti = analizzatore.parse_args()

    if argomenti.en:
        albero, colonna = percorsi.SORGENTE_HSP, "en"
        modello = dati.leggi(percorsi.DATI_SORGENTE / "autopick.txt")
        etichetta = "monte contro se stesso"
        # ⚠️ **Uno, e non zero**: `bottle of water` non e' il nome di nessun
        # oggetto nemmeno in inglese — l'oggetto si chiama `water` — quindi
        # quella riga d'esempio non aggancia niente **nella build di monte**.
        # E' un difetto di upstream, trovato dalla rete il giorno in cui e'
        # nata: l'italiano scrive `acqua?`, che il nome ce l'ha.
        attese = 1
    elif argomenti.scaduto:
        albero, colonna = percorsi.BUILD_HSP, "en"
        modello = dati.leggi(percorsi.DATI_SORGENTE / "autopick.txt")
        etichetta = "chiavi italiane, modello inglese (il difetto della 98a)"
        attese = None
    else:
        albero, colonna = percorsi.BUILD_HSP, "en"
        italiano = percorsi.BUILD_DATI / "autopick_it.txt"
        if not italiano.exists():
            raise SystemExit(f"{italiano} non c'e': lancia `python -m strumenti.dati_applica`")
        modello = dati.leggi(italiano, "autopick.txt")
        etichetta = "italiano contro italiano"
        attese = 0

    elenco = ombra.chiavi(albero, colonna)
    modificatori = [(n, c) for n, cl, c in elenco if cl == "modificatore"]
    tipi = sorted({c for _, cl, c in elenco if cl == "tipo"}, key=len, reverse=True)
    nomi = nomi_di_oggetto("en" if argomenti.en else "it")

    guasti = []
    provate = 0
    for numero, riga in enumerate(modello.splitlines(), 1):
        nuda = marcatori_via(riga)
        if not nuda:
            continue
        provate += 1
        s = f" {nuda} "
        agganciati = []
        for _, chiave in modificatori:
            if chiave in s:
                agganciati.append(chiave.strip())
                s = s.replace(chiave, " ")
        resto = re.sub(r" +", " ", s.strip())

        tipo = next((t for t in tipi if t in resto), None)
        per_nome = bool(resto) and any(resto.lower() in nome for nome in nomi)

        if tipo is None and not per_nome:
            guasti.append(f"  :{numero:<4} {riga.strip()!r}\n"
                          f"        modificatori: {agganciati or 'nessuno'}   "
                          f"resta {resto!r}: non e' un tipo e non e' dentro nessun nome di oggetto")
        elif tipo is None and not agganciati:
            # `:363` pretende almeno un modificatore per agganciare per TIPO,
            # ma per NOME no: questa riga vive solo finche' il nome resta quello
            pass

    print(f"--- {etichetta}: {len(modificatori)} modificatori, {len(tipi)} tipi, "
          f"{provate} regole nel modello")
    for guasto in guasti:
        print(guasto)
    print(f"\nregole che non agganciano niente: {len(guasti)}")
    if attese is not None and len(guasti) != attese:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
