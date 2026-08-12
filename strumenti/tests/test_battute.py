# strumenti/tests/test_battute.py
"""Le due cose che `battute.py` puo' sbagliare in silenzio.

Non si prova il referto, che e' testo per un occhio umano: si prova la mappa
riga -> (dbmode, dbid), perche' un errore lì produce un lotto **plausibile e
sbagliato** — battute attribuite alla creatura accanto, o alla classe sbagliata.
"""
import json

from strumenti import percorsi
from strumenti.battute import (
    FILE,
    LIVELLO_IGNOTO,
    contesto_per_riga,
    livelli,
    repertori,
    rese_gia_decise,
)


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


SORGENTE_CON_LIVELLI = "\n".join([
    "\tif ( dbid == CREATURE_ID_ACCATTONE ) {",
    "\t\tif ( dbmode == DBMODE_FLAVOR_PASSIVE ) {",
    '\t\t\ttxt lang("「…」", cnvtalk("Alms"))',
    "\t\t}",
    "\t\tif ( dbmode == DBMODE_SET ) {",
    "\t\t\tif ( initlv != 0 ) {",
    "\t\t\t\tcdata(CDATA_LEVEL, rc) = initlv",
    "\t\t\t}",
    "\t\t\telse {",
    "\t\t\t\tcdata(CDATA_LEVEL, rc) = 2",
    "\t\t\t}",
    "\t\t\tcdata(CDATA_LEVEL, rc) = voidlv * (100 + cdata(CDATA_LEVEL, rc) * 2) / 100",
    "\t\t}",
    "\t}",
    "\tif ( dbid == CREATURE_ID_JURE ) {",
    "\t\tif ( dbmode == DBMODE_REF_SPEC ) {",
    "\t\t\tcdata(CDATA_LEVEL, rc) = 7",
    "\t\t}",
    "\t\tif ( dbmode == DBMODE_SET ) {",
    "\t\t\tcdata(CDATA_LEVEL, rc) = 1200",
    "\t\t}",
    "\t}",
])


def test_il_livello_e_quello_base_non_quello_di_una_generazione():
    """⚠️ Le tre forme che il sorgente usa non dicono la stessa cosa.

    `= initlv` ripete un livello imposto da chi chiama e la riscalatura per
    `voidlv` e' quella dei dungeon del Vuoto: prenderle darebbe il livello di una
    generazione particolare invece di quello della creatura. Nessuna delle due
    porta una cifra, ma la riga di `voidlv` **contiene** `* 2`, quindi un regex
    piu' largo la prenderebbe e direbbe che l'accattone e' di livello 2 per la
    ragione sbagliata — cioe' darebbe la risposta giusta per caso.

    E un `CDATA_LEVEL` fuori da `DBMODE_SET` non e' il livello di nascita: qui
    `<Jure>` ne ha uno in `DBMODE_REF_SPEC` che non deve vincere sul 1200.
    """
    modo_di, ident_di = contesto_per_riga(SORGENTE_CON_LIVELLI)
    trovati = livelli(SORGENTE_CON_LIVELLI, modo_di, ident_di)

    assert trovati["CREATURE_ID_ACCATTONE"] == 2
    assert trovati["CREATURE_ID_JURE"] == 1200


def test_una_creatura_senza_livello_finisce_in_coda():
    """Un dato mancante non deve scavalcare: vale il livello piu' alto.

    Se `LIVELLO_IGNOTO` fosse zero, una creatura di cui non sappiamo il livello
    aprirebbe l'elenco e si tradurrebbe per prima **proprio perche'** il sorgente
    non dice niente di lei.
    """
    assert LIVELLO_IGNOTO > 1200, "gli dei stanno a 1200: il default deve stare sopra"


def test_in_testa_stanno_le_creature_di_livello_piu_basso():
    """Il criterio nuovo, provato come proprieta' e non come numero.

    ⚠️ Non si pinna «la prima creatura e' l'accattone»: sarebbe una fotografia
    dell'uscita dello strumento, e cambierebbe a ogni lotto tradotto. Si prova
    che **il primo decimo e' piu' basso dell'ultimo**, che e' la cosa per cui il
    criterio esiste, e che resta vera mentre l'elenco si accorcia.
    """
    estrazione = percorsi.LAVORO_LOTTI / "_c.jsonl"
    if not estrazione.exists():
        import pytest
        pytest.skip("serve lavoro/_c.jsonl")

    testo = (percorsi.SORGENTE_HSP / FILE).read_bytes().decode("cp932")
    livello_di = livelli(testo, *contesto_per_riga(testo))
    ordinate, _, _ = repertori(estrazione=estrazione)

    quanti = max(1, len(ordinate) // 10)
    testa = [livello_di.get(i, LIVELLO_IGNOTO) for i, _ in ordinate[:quanti]]
    coda = [livello_di.get(i, LIVELLO_IGNOTO) for i, _ in ordinate[-quanti:]]

    assert max(testa) <= min(coda), (
        "l'ordine non e' per livello crescente: "
        f"in testa fino a {max(testa)}, in coda da {min(coda)}"
    )


def test_per_riga_rimette_l_ordine_del_sorgente():
    """L'opzione di ripiego deve davvero cambiare l'ordine, non solo esistere."""
    estrazione = percorsi.LAVORO_LOTTI / "_c.jsonl"
    if not estrazione.exists():
        import pytest
        pytest.skip("serve lavoro/_c.jsonl")

    per_riga, _, _ = repertori(estrazione=estrazione, per_riga=True)
    righe = [min(v["riga"] for v in voci) for _, voci in per_riga]
    assert righe == sorted(righe)

    per_livello, _, _ = repertori(estrazione=estrazione)
    assert [i for i, _ in per_livello] != [i for i, _ in per_riga], (
        "i due ordini coincidono: il criterio per livello non sta agganciando"
    )


def test_il_dizionario_e_il_sorgente_parlano_dello_stesso_file():
    """Rete banale ma utile: il file che lo strumento legge esiste da entrambe le parti."""
    assert (percorsi.SORGENTE_HSP / FILE).exists()
    assert (percorsi.DIZIONARIO / f"{FILE}.jsonl").exists()
    voci = [json.loads(r) for r in
            (percorsi.DIZIONARIO / f"{FILE}.jsonl").read_text(encoding="utf-8").splitlines()
            if r.strip()]
    assert all(v["file"] == FILE for v in voci)


def test_lo_stesso_giapponese_ritrova_le_rese_gia_decise():
    """⚠️ Il difetto che questa funzione esiste per rendere visibile.

    Il dizionario e' indicizzato per contenuto, e nel contenuto c'e' l'inglese:
    due creature che dicono la stessa identica frase giapponese ma che da monte
    hanno ricevuto due inglesi diversi sono **due voci da tradurre**. Il punk e
    il teppista hanno tredici battute giapponesi in comune e zero inglesi in
    comune. Se le due rese divergono la stessa frase esce in due modi, e
    nessun'altra guardia lo vede: sono entrambe italiano valido, entrambe
    diverse dal loro inglese, entrambe senza morfologia residua.

    Il test guarda il dizionario vero, perche' il valore della funzione sta
    nell'agganciare quello: una versione che leggesse il campo sbagliato
    tornerebbe una mappa vuota, e una mappa vuota non segnala mai niente.
    """
    rese = rese_gia_decise()
    assert rese, "il dizionario non aggancia piu': la mappa e' vuota"

    # una battuta che il punk e il teppista condividono, resa una volta sola
    condivisa = rese.get("「チキショー」")
    assert condivisa == {"Porca miseria!"}, (
        f"le due voci di 「チキショー」 divergono: {condivisa}"
    )


def test_le_divergenze_legittime_non_vengono_appianate():
    """⚠️ Perche' questo e' un referto e non una guardia che blocca.

    L'inglese SPECIALIZZA la stessa onomatopea giapponese secondo la creatura:
    「がおー」 e' `*creaking*` su un golem di legno e `*growl*` su una
    divinita' serpente, e le due rese italiane seguono l'inglese come devono.
    Una regola che pretendesse una resa sola per giapponese rifiuterebbe lavoro
    giusto — ed e' il motivo per cui `--divergenti` stampa e non fallisce.
    """
    rese = rese_gia_decise()
    ruggito = rese.get("「がおー」", set())
    assert len(ruggito) > 1, (
        "le due rese di 「がおー」 sono state appianate in una sola: "
        "erano diverse per una ragione, il legno scricchiola e la serpe ringhia"
    )
