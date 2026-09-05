"""Le prove delle sei qualita' del CNPC evocato.

⚠️⚠️ La prova che spiega il modulo e' `test_la_resa_non_butta_piu_l_operando`:
il difetto non era una parola non tradotta, era una resa che **scartava `s`**,
cioe' il nome e la qualita' del CNPC. Se un domani qualcuno riscrivesse quella
riga senza `s`, il giocatore italiano tornerebbe a leggere «Qualcosa» e nessun
conto se ne accorgerebbe.

⚠️ E quella che pesa di piu' e' `test_nessuna_qualita_concorda_col_genere`: `s`
esce attaccato al nome di un CNPC, che lo scrive il giocatore, e un aggettivo
maschile davanti a «Maria» e' sbagliato in un modo che nessuna rete vede.
"""
import json

import pytest

from strumenti import percorsi, salti
from strumenti import genera_toppe_qualita_cnpc as qualita
from strumenti.genera_toppe_qualita_cnpc import (GIUNTURA, MonteMosso, QUALITA,
                                                 dal_dizionario, problemi,
                                                 rese, sorgente, toppe)


def test_sono_sei_e_la_tabella_le_copre_tutte():
    nel_sorgente = sorgente()
    assert len(nel_sorgente) == 6
    assert set(nel_sorgente) == set(QUALITA)
    assert all(nel_sorgente[n] == QUALITA[n][0] for n in QUALITA)


def test_ogni_qualita_ha_la_sua_parola():
    assert problemi() == []


def test_nessuna_qualita_concorda_col_genere():
    """⚠️⚠️ `s` esce attaccato al nome di un CNPC, e il sesso lo decide il
    giocatore che lo scrive. `guida-stile.md` («l'etichetta si legge dove
    esce») e `contratto-nomi.md` §3: un aggettivo attaccato a un nome di genere
    ignoto va invariabile. «leggendario» diventerebbe «leggendaria»; «da
    leggenda» no."""
    for numero, parola in rese().items():
        ultima = parola.rstrip().rsplit(" ", 1)[-1]
        assert not (ultima.endswith("o") and ultima != "professionista"), \
            "%d -> %r concorda al maschile" % (numero, parola)


def test_una_resa_che_concorda_si_accende(monkeypatch):
    finto = dict(QUALITA)
    finto[7720] = ("Legendary ", ", leggendario", "prova")
    monkeypatch.setattr(qualita, "QUALITA", finto)
    assert any("concorda al maschile" in g for g in problemi())


def test_ogni_resa_comincia_con_la_virgola():
    """⭐ La giuntura mette il nome DAVANTI: senza la virgola in testa un CNPC
    senza qualita' uscirebbe «Fulano, » con la virgola penzoloni."""
    assert all(v.startswith(", ") for v in rese().values())


def test_una_resa_senza_virgola_si_accende(monkeypatch):
    finto = dict(QUALITA)
    finto[7718] = ("Skilled ", "abile", "prova")
    monkeypatch.setattr(qualita, "QUALITA", finto)
    assert any("deve cominciare con" in g for g in problemi())


def test_due_parole_si_leggono_dal_dizionario_e_non_si_riscrivono():
    """⭐ `scadente` e `comune` sono gia' le qualita' dell'oggetto di
    `text.hsp:106`: se le due schermate le chiamassero con parole diverse, il
    giocatore penserebbe a due scale diverse."""
    lette = dal_dizionario()
    assert lette == {7716: ", scadente", 7717: ", comune"}


def test_una_voce_sparita_dal_dizionario_ferma_tutto(monkeypatch):
    monkeypatch.setitem(qualita.DAL_DIZIONARIO, 7716, "non-esiste")
    with pytest.raises(KeyError):
        dal_dizionario()


def test_la_giuntura_e_una_riga_del_sorgente_e_non_una_speranza():
    """La toppa che sposta il nome davanti si regge su quella riga: se il monte
    la cambia, l'apposizione non si compone piu' e il cancello lo dice."""
    righe = qualita._righe_file("command.hsp")
    assert righe[GIUNTURA[0] - 1].strip() == GIUNTURA[1]


def test_la_giuntura_spostata_ferma_tutto(monkeypatch):
    monkeypatch.setattr(qualita, "GIUNTURA",
                        (GIUNTURA[0], "s += qualcosaltro", GIUNTURA[2]))
    assert any("l'apposizione non si compone" in g for g in problemi())


def test_sono_sette_toppe_sei_rese_e_un_ordine():
    mie = toppe()
    assert len(mie) == 7
    assert sum(1 for t in mie if "userdatan(3, knowCNPC) + s" in t["sostituisci"]) == 1


# --- il sorgente vero e la build -------------------------------------------

def test_la_resa_non_butta_piu_l_operando():
    """⚠️⚠️ IL DIFETTO VERO. La resa era «Qualcosa di un altro mondo e' stato
    evocato!» e `s` — nome e qualita' — non ci arrivava. ⭐ E la resa nuova
    evita l'accordo: «arriva» non concorda, «e' stato evocato» sì."""
    percorso = percorsi.PROGETTO / "dizionario" / "command.hsp.jsonl"
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce["riga"] == 7724 and voce.get("tipo") == "dinamica":
            assert "+ s +" in voce["it"], "la resa butta via `s`"
            assert voce["it"] == '"Da un altro mondo arriva " + s + "!"'
            return
    raise AssertionError("la voce di command.hsp:7724 non c'e' piu'")


def test_nella_build_il_CNPC_evocato_ha_nome_e_qualita():
    testo = (percorsi.BUILD_HSP / "command.hsp").read_bytes().decode("cp932")
    for parola in (", scadente", ", comune", ", abile", ", professionista",
                   ", da leggenda", ", celebre"):
        assert '"%s"' % parola in testo, parola
    assert "s = userdatan(3, knowCNPC) + s" in testo
    assert '"Legendary "' not in testo
    assert "Da un altro mondo arriva " in testo


# --- perche' questo modulo esiste ------------------------------------------

def test_queste_qualita_sono_il_TERZO_punto_cieco():
    """⚠️⚠️ Non era un salto in piu': era un'ancora. `disegnate` e `salti`
    prendevano il **primo** simbolo dopo il comando che disegna, e qui il primo
    simbolo e' `lang`: `s` sta dentro l'argomento, concatenato."""
    testo = (percorsi.SORGENTE_HSP / "command.hsp").read_bytes().decode("cp932")
    inglesi = {v[0] for v in QUALITA.values()}
    da_salti = {t[3] for t in salti.scoperte_di("command.hsp", testo)}
    assert inglesi <= da_salti
    # ⭐ e la prova al contrario: con la vecchia regola non ne vedeva nessuna
    riga = '\ttxt lang("x", "A " + s + " is summoned!")'
    assert salti._ARGOMENTO.match(riga.split("txt ")[1]).group(1) == "lang"
