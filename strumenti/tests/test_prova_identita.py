# strumenti/tests/test_prova_identita.py
"""La prova d'identita' e' forte solo se esclude poco e per motivi noti.

Questi test fissano *cosa* viene escluso: se un domani l'esclusione si allargasse
in silenzio, la prova continuerebbe a stampare 72/72 misurando sempre meno.

Le statiche avvolte in cnvtalk(/cnven( non sono piu' tra le esclusioni: da
quando applica.py prende l'involucro dal sito, si sostituiscono come le altre.
"""
from strumenti.prova_identita import dizionario_identita, prova

STATICA = '\ttxt lang("バックパックが一杯だ。", "Your inventory is full.")\n'
AVVOLTA = '\ttxt lang("「うにーっ！」", cnvtalk("Urchinn!"))\n'
DINAMICA = '\ttxt lang("jp", cdatan(CDATAN_NAME, tc) + " ti guarda.")\n'


def test_una_statica_normale_entra_nel_dizionario():
    diz, collidenti = dizionario_identita("text.hsp", STATICA)
    assert len(diz) == 1
    assert collidenti == 0
    voce = next(iter(diz.values()))
    assert voce["it"] == voce["en"] == "Your inventory is full."


def test_una_statica_avvolta_ora_entra_nel_dizionario():
    # l'involucro si prende dal sito (applica.riscrivi_statica), non dalla
    # voce di dizionario: l'identita' e' semplicemente l'inglese estratto.
    diz, collidenti = dizionario_identita("action.hsp", AVVOLTA)
    assert len(diz) == 1
    assert collidenti == 0
    voce = next(iter(diz.values()))
    assert voce["it"] == voce["en"] == "Urchinn!"


def test_per_una_dinamica_l_identita_e_l_espressione_intera():
    diz, _ = dizionario_identita("chat.hsp", DINAMICA)
    voce = next(iter(diz.values()))
    assert voce["it"] == voce["en_grezzo"]
    assert "cdatan" in voce["it"], "l'identita' deve conservare le variabili"


def test_due_espressioni_diverse_ora_hanno_chiavi_diverse():
    # stessi letterali, variabili diverse: prima condividevano la firma e
    # venivano escluse entrambe. Da SPEC 3.2 l'espressione entra nella chiave,
    # quindi sono due voci distinte e tornano traducibili.
    testo = ('\ttxt lang("jp", name(gdata(GDATA_RIDER)) + " glare")\n'
             '\ttxt lang("jp", cdatan(CDATAN_NAME, ttc) + " glare")\n')
    diz, ambigue = dizionario_identita("action.hsp", testo)
    assert len(diz) == 2
    assert ambigue == 0


def test_la_stessa_statica_nuda_e_avvolta_si_scioglie_da_sola():
    # per le statiche l'involucro non entra nella firma, e non entra neppure
    # nel confronto di ambiguita': queste due condividono la firma e vogliono
    # la stessa identita' inglese, quindi non sono piu' ambigue. Sono le 3
    # occorrenze residue in db_creature.hsp.
    testo = ('\ttxt lang("jp", "Ciao.")\n'
             '\ttxt lang("jp", cnvtalk("Ciao."))\n')
    diz, ambigue = dizionario_identita("db_creature.hsp", testo)
    assert len(diz) == 1
    assert ambigue == 0
    voce = next(iter(diz.values()))
    assert voce["it"] == "Ciao."


def test_su_un_file_finto_la_prova_riproduce_i_byte(tmp_path):
    (tmp_path / "finto.hsp").write_bytes((STATICA + DINAMICA + AVVOLTA).encode("cp932"))
    esito = prova(tmp_path)
    assert esito.ok
    assert (esito.file_identici, esito.file_provati) == (1, 1)
    assert esito.sostituzioni == 3  # l'avvolta si sostituisce anche lei ora


def test_un_file_che_non_si_riproduce_viene_segnalato(tmp_path, monkeypatch):
    (tmp_path / "finto.hsp").write_bytes(STATICA.encode("cp932"))
    # una sostituzione che cambia il testo: la prova deve accorgersene
    import strumenti.prova_identita as modulo

    def sporca(nome, testo):
        diz, c = dizionario_identita(nome, testo)
        for voce in diz.values():
            voce["it"] = voce["it"] + "!"
        return diz, c

    monkeypatch.setattr(modulo, "dizionario_identita", sporca)
    esito = modulo.prova(tmp_path)
    assert not esito.ok
    assert esito.difformi == ["finto.hsp"]
