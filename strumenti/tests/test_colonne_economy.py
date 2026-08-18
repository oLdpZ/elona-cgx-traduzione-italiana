# strumenti/tests/test_colonne_economy.py
"""Il prospetto cittadino allinea le colonne con gli SPAZI, e nessuno lo guarda.

`economy.hsp:319`-`:365` scrive dodici righe fatte cosi':

    mes lang("...", "Water pollution     " + mdata(...) + " (dead " + ... )

L'etichetta e' imbottita a mano fino a una colonna fissa, e il numero comincia
sempre li'. Non e' una tabella: se una resa italiana e' lunga un carattere in
piu' o in meno, quella riga esce disallineata dalle altre undici — e non lo
segnala niente, perche' non e' un taglio ne' uno sforo. `verifica.py` guarda le
interpolazioni e il glossario, le quattro reti di geometria guardano i tetti.

⚠️⚠️ **E la misura va fatta sulla forma DEGRADATA.** Nel dizionario si scrive
«Autorità»; `applica.py` scrive «Autorita'», che e' un carattere piu' lungo. Un
test che contasse i caratteri del dizionario direbbe che va bene e la colonna a
schermo sarebbe spostata. E' la stessa ragione per cui la resa di `:357` e'
«Influenza» e non «Autorita'»: un'etichetta accentata costringe a contare
l'imbottitura su una cosa che il file non mostra.

La prova e' contro l'INGLESE di monte, non contro un numero scritto qui: e'
upstream a decidere dove sta la colonna, e se un aggiornamento CGX la sposta
questo test lo dice.
"""
import json
import re

import pytest

from strumenti import percorsi
from strumenti.accenti import degrada

# le dodici righe del prospetto (economy.hsp:319-:365)
RIGHE = {319, 323, 327, 331, 335, 339, 343, 347, 353, 357, 361, 365}

_TESTA = re.compile(r'^"((?:[^"\\]|\\.)*)"')


def _testa(espressione: str) -> str | None:
    """Il primo letterale dell'espressione, cioe' l'etichetta imbottita."""
    trovato = _TESTA.match(espressione.strip())
    return trovato.group(1) if trovato else None


def voci_del_prospetto() -> list[dict]:
    percorso = percorsi.DIZIONARIO / "economy.hsp.jsonl"
    if not percorso.exists():
        return []
    fuori = []
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        if voce["riga"] in RIGHE and voce.get("it"):
            fuori.append(voce)
    return fuori


def test_il_prospetto_e_nel_dizionario():
    """Se un domani sparisce, gli altri test passerebbero a vuoto."""
    assert len(voci_del_prospetto()) == len(RIGHE)


@pytest.mark.parametrize("voce", voci_del_prospetto(),
                         ids=lambda v: str(v["riga"]))
def test_l_etichetta_italiana_e_lunga_come_l_inglese(voce):
    inglese = _testa(voce["en_grezzo"])
    italiano = _testa(voce["it"])
    assert inglese is not None, f"{voce['riga']}: l'inglese non comincia con un letterale"
    assert italiano is not None, f"{voce['riga']}: la resa non comincia con un letterale"
    assert len(degrada(italiano)) == len(inglese), (
        f"economy.hsp:{voce['riga']} sposta la colonna: "
        f"{degrada(italiano)!r} ({len(degrada(italiano))}) contro "
        f"{inglese!r} ({len(inglese)})"
    )


@pytest.mark.parametrize("voce", voci_del_prospetto(),
                         ids=lambda v: str(v["riga"]))
def test_l_etichetta_italiana_non_porta_accenti(voce):
    """Un accento si allunga in build, e contarlo a mano e' come non contarlo.

    Non e' una regola di stile: e' che l'imbottitura andrebbe misurata su una
    forma che il file del dizionario non mostra. Meglio un sinonimo.
    """
    italiano = _testa(voce["it"])
    assert italiano == degrada(italiano), (
        f"economy.hsp:{voce['riga']}: l'etichetta {italiano!r} ha un accento, "
        "e in build diventa piu' lunga di quel che si legge qui"
    )
