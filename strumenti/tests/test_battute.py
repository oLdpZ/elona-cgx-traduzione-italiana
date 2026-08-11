# strumenti/tests/test_battute.py
"""Le due cose che `battute.py` puo' sbagliare in silenzio.

Non si prova il referto, che e' testo per un occhio umano: si prova la mappa
riga -> (dbmode, dbid), perche' un errore lì produce un lotto **plausibile e
sbagliato** — battute attribuite alla creatura accanto, o alla classe sbagliata.
"""
import json

from strumenti import percorsi
from strumenti.battute import FILE, contesto_per_riga, repertori


SORGENTE_FINTO = "\n".join([
    "\tif ( dbid == CREATURE_ID_CANE ) {",
    "\t\tif ( dbmode == DBMODE_FLAVOR_PASSIVE ) {",
    '\t\t\ttxt lang("「ワン」", cnvtalk("Woof"))',
    "\t\t}",
    "\t\tif ( dbmode == DBMODE_FLAVOR_DEATH ) {",
    '\t\t\ttxt lang("「キャン」", cnvtalk("Yelp"))',
    "\t\t}",
    "\t}",
    "\tif ( dbid == CREATURE_ID_GATTO ) {",
    '\t\ttxt lang("「ニャー」", cnvtalk("Meow"))',
    "\t}",
])


def test_il_dbmode_si_azzera_sulla_creatura_nuova():
    """⚠️ Il difetto che questo test esiste per impedire.

    `dbid` apre la creatura e i `dbmode` si susseguono dentro. Se il modo non si
    azzerasse sul `dbid`, la prima riga di `CREATURE_ID_GATTO` — che non ha un
    `dbmode` sopra di sé — erediterebbe `DBMODE_FLAVOR_DEATH` dal cane: un
    referto che dice «il gatto lo dice morendo» e che nessuno metterebbe in
    dubbio leggendolo.
    """
    modo_di, ident_di = contesto_per_riga(SORGENTE_FINTO)

    assert ident_di[3] == "CREATURE_ID_CANE"
    assert modo_di[3] == "DBMODE_FLAVOR_PASSIVE"
    assert modo_di[6] == "DBMODE_FLAVOR_DEATH"

    assert ident_di[10] == "CREATURE_ID_GATTO"
    assert modo_di[10] == "?", "il modo del cane e' arrivato al gatto"


def test_ogni_voce_da_fare_riceve_una_creatura(tmp_path):
    """Nessuna battuta finisce nel gruppo `?`.

    Se una riga non ricevesse un `dbid`, le sue battute si accumulerebbero in un
    gruppo senza nome e il lotto le porterebbe insieme a quelle di altre
    creature, con registri diversi mescolati.
    """
    estrazione = percorsi.LAVORO_LOTTI / "_c.jsonl"
    if not estrazione.exists():
        import pytest
        pytest.skip("serve lavoro/_c.jsonl, che si rigenera con strumenti.estrai")

    ordinate, _, _ = repertori(estrazione=estrazione)
    orfane = [ident for ident, _ in ordinate if not ident.startswith("CREATURE_ID_")]
    assert orfane == []


def test_i_nomi_italiani_arrivano_dal_dizionario():
    """Il referto mostra il nome deciso in Fase 2, e quasi tutti ce l'hanno.

    Il numero non e' pinnato sull'uscita dello strumento: 1.131 nomi sono resi e
    stanno nel dizionario, quindi le creature **con battute da fare** che non
    hanno un nome italiano devono essere poche. Se diventassero molte vorrebbe
    dire che la mappa `dbid` si e' rotta, non che i nomi sono spariti.
    """
    estrazione = percorsi.LAVORO_LOTTI / "_c.jsonl"
    if not estrazione.exists():
        import pytest
        pytest.skip("serve lavoro/_c.jsonl")

    ordinate, nomi, _ = repertori(estrazione=estrazione)
    senza = [ident for ident, _ in ordinate if ident not in nomi]
    assert len(senza) < len(ordinate) / 5, (
        f"{len(senza)} creature su {len(ordinate)} senza nome italiano: "
        "la mappa dbid probabilmente non aggancia piu'"
    )


def test_il_dizionario_e_il_sorgente_parlano_dello_stesso_file():
    """Rete banale ma utile: il file che lo strumento legge esiste da entrambe le parti."""
    assert (percorsi.SORGENTE_HSP / FILE).exists()
    assert (percorsi.DIZIONARIO / f"{FILE}.jsonl").exists()
    voci = [json.loads(r) for r in
            (percorsi.DIZIONARIO / f"{FILE}.jsonl").read_text(encoding="utf-8").splitlines()
            if r.strip()]
    assert all(v["file"] == FILE for v in voci)
