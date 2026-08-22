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
schermo sarebbe spostata.

⭐ **87a: `:357` adesso porta un accento, e la precauzione che lo vietava e'
stata ritirata.** La riga diceva «Influenza» mentre il gioco chiama quella
statistica «autorita'» in **otto** altri siti (`chat.hsp:7026`, `:7032`,
`:19563`, `:23940`, `:24008`, `:24011`, `:22513`, `action.hsp:8506`), e il
tutorial del seminario (`chat.hsp:14047`) e' il posto dove il giocatore impara
la parola: due nomi per una statistica sola erano il difetto, non l'accento.
Il divieto nasceva da un timore ragionevole — *un'etichetta accentata
costringe a contare l'imbottitura su una forma che il file non mostra* — ma
quel conto non si fa piu' a mano: lo fa
`test_l_etichetta_italiana_e_lunga_come_l_inglese` a ogni giro, sulla forma
degradata, contro l'inglese di monte. La precauzione proteggeva da un conto
sbagliato; il conto adesso e' automatico. 💡 *Una precauzione si ritira quando
la cosa da cui proteggeva e' diventata una misura.*

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


# ⚠️ 87a: qui c'era `test_l_etichetta_italiana_non_porta_accenti`, dodici prove
# che vietavano l'accento in queste dodici etichette. E' stato tolto, non
# aggirato con un'eccezione: il motivo sta nel docstring del modulo. In breve,
# vietava una PAROLA per paura di un CONTO, e il conto lo fa gia'
# `test_l_etichetta_italiana_e_lunga_come_l_inglese` sulla forma degradata, a
# ogni giro. Un'eccezione per la sola `:357` sarebbe stata un debito da
# rileggere ogni volta che si tocca il prospetto.
