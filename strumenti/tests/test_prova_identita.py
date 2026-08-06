# strumenti/tests/test_prova_identita.py
"""La prova d'identita' e' forte solo se esclude poco e per motivi noti.

Questi test fissano *cosa* viene escluso: se un domani l'esclusione si allargasse
in silenzio, la prova continuerebbe a stampare 72/72 misurando sempre meno.
"""
from strumenti.prova_identita import dizionario_identita, prova

STATICA = '\ttxt lang("バックパックが一杯だ。", "Your inventory is full.")\n'
AVVOLTA = '\ttxt lang("「うにーっ！」", cnvtalk("Urchinn!"))\n'
DINAMICA = '\ttxt lang("jp", cdatan(CDATAN_NAME, tc) + " ti guarda.")\n'


def test_una_statica_normale_entra_nel_dizionario():
    diz, avvolti, collidenti = dizionario_identita("text.hsp", STATICA)
    assert len(diz) == 1
    assert (avvolti, collidenti) == (0, 0)
    voce = next(iter(diz.values()))
    assert voce["it"] == voce["en"] == "Your inventory is full."


def test_una_statica_avvolta_e_esclusa_e_contata():
    diz, avvolti, collidenti = dizionario_identita("action.hsp", AVVOLTA)
    assert diz == {}
    assert (avvolti, collidenti) == (1, 0)


def test_per_una_dinamica_l_identita_e_l_espressione_intera():
    diz, _, _ = dizionario_identita("chat.hsp", DINAMICA)
    voce = next(iter(diz.values()))
    assert voce["it"] == voce["en_grezzo"]
    assert "cdatan" in voce["it"], "l'identita' deve conservare le variabili"


def test_due_espressioni_diverse_con_la_stessa_firma_sono_escluse_entrambe():
    # stessi letterali, variabili diverse: la firma coincide, l'espressione no
    testo = ('\ttxt lang("jp", name(gdata(GDATA_RIDER)) + " glare")\n'
             '\ttxt lang("jp", cdatan(CDATAN_NAME, ttc) + " glare")\n')
    diz, avvolti, collidenti = dizionario_identita("action.hsp", testo)
    assert diz == {}, "escludere una sola delle due la farebbe iniettare nell'altra"
    assert (avvolti, collidenti) == (0, 2)


def test_su_un_file_finto_la_prova_riproduce_i_byte(tmp_path):
    (tmp_path / "finto.hsp").write_bytes((STATICA + DINAMICA + AVVOLTA).encode("cp932"))
    esito = prova(tmp_path)
    assert esito.ok
    assert (esito.file_identici, esito.file_provati) == (1, 1)
    assert esito.sostituzioni == 2  # l'avvolta e' esclusa, non sostituita


def test_un_file_che_non_si_riproduce_viene_segnalato(tmp_path, monkeypatch):
    (tmp_path / "finto.hsp").write_bytes(STATICA.encode("cp932"))
    # una sostituzione che cambia il testo: la prova deve accorgersene
    import strumenti.prova_identita as modulo

    def sporca(nome, testo):
        diz, a, c = dizionario_identita(nome, testo)
        for voce in diz.values():
            voce["it"] = voce["it"] + "!"
        return diz, a, c

    monkeypatch.setattr(modulo, "dizionario_identita", sporca)
    esito = modulo.prova(tmp_path)
    assert not esito.ok
    assert esito.difformi == ["finto.hsp"]
