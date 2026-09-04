"""Le prove delle parole che il giocatore DIGITA.

⚠️⚠️ La prova che conta di piu' e' `test_una_parola_nuova_di_monte_ferma_tutto`:
questa catena non ha nessun cancello naturale addosso, perche' tutti i cancelli
del progetto misurano il testo a schermo e un operando di `==` non e' testo a
schermo. Se il monte aggiungesse un desiderio, senza quella prova la parola
italiana mancherebbe e **nessuno se ne accorgerebbe**, esattamente come nessuno
si era accorto per centotrentanove sessioni che il desiderio non parlava
italiano.
"""
import json

import pytest

from strumenti import genera_toppe_desideri as desideri
from strumenti import percorsi
from strumenti.genera_toppe_desideri import (CLASSI, MonteMosso, alternative,
                                             nomi_classi, problemi,
                                             righe_bersaglio, toppe)


def _riga(condizione: str) -> str:
    return "\tif ( %s ) {" % condizione


# --- che cosa la tabella riconosce ----------------------------------------

def test_aggiunge_le_due_forme_del_nome_di_classe():
    """Il banco della classe non abbassa le maiuscole: servono tutt'e due."""
    nuove, tetto, _ = alternative(
        _riga('inputlog == "戦士" | inputlog == "warrior"'),
        {"warrior": "Guerriero"})
    assert nuove == ["Guerriero", "guerriero"]
    assert tetto == desideri.TETTO_CLASSE


def test_non_ripete_una_forma_che_la_riga_ha_gia():
    """«claymore» minuscolo e' gia' la chiave inglese: aggiungerlo di nuovo
    scriverebbe due volte lo stesso confronto sulla stessa riga."""
    nuove, _, _ = alternative(
        _riga('inputlog == "クレイモア" | inputlog == "claymore"'),
        {"claymore": "Claymore"})
    assert nuove == ["Claymore"]


def test_il_desiderio_prende_il_suo_tetto_e_non_quello_della_classe():
    nuove, tetto, _ = alternative(
        _riga('inputlog == "死" | inputlog == "death"'), {})
    assert nuove == ["morte"]
    assert tetto == desideri.TETTO_DESIDERIO


def test_una_riga_dichiarata_non_chiede_niente():
    """Gli otto dei si scrivono uguale in italiano: la riga e' dichiarata,
    non dimenticata."""
    nuove, _, motivo = alternative(
        _riga('inputlog == "ルルウィ" | inputlog == "lulwy"'), {})
    assert nuove == []
    assert "nome proprio" in motivo


def test_la_dichiarazione_non_scavalca_una_decisione():
    """⚠️ Il ramo giapponese non sta mai in `SENZA_ITALIANO`, quindi la
    dichiarazione si guarda **dopo** le tabelle: guardarla prima farebbe
    sparire una riga vera dietro un'omonimia."""
    nuove, _, _ = alternative(
        _riga('inputlog == "金" | inputlog == "money" | inputlog == "q"'), {})
    assert "soldi" in nuove


def test_una_parola_nuova_di_monte_ferma_tutto():
    """⭐ La prova al contrario. Una riga che nessuna tabella reclama non
    passa in silenzio: il generatore alza `KeyError`, e chi legge decide."""
    with pytest.raises(KeyError):
        alternative(_riga('inputlog == "夢" | inputlog == "dream"'), {})


# --- le misure -------------------------------------------------------------

def test_una_parola_piu_lunga_del_tetto_e_un_guaio(monkeypatch):
    """Oltre il tetto la casella smette di accettare caratteri: la parola non
    si potrebbe nemmeno digitare."""
    lunga = "x" * (desideri.TETTO_DESIDERIO + 1)
    monkeypatch.setitem(desideri.AGGIUNTE, "death", [lunga])
    guai = [g for g in problemi() if lunga in g]
    assert guai and "non riuscirebbe a scriverla" in guai[0]


def test_una_parola_accentata_e_un_guaio(monkeypatch):
    """CP932 non ha le vocali accentate: «età» non si digita."""
    monkeypatch.setitem(desideri.AGGIUNTE, "death", ["età"])
    assert any("non e' ASCII" in g for g in problemi())


def test_una_parola_gia_di_un_altro_ramo_e_un_guaio(monkeypatch):
    """La catena non ha `else`: il secondo ramo resterebbe muto per sempre."""
    monkeypatch.setitem(desideri.AGGIUNTE, "death", ["soldi"])
    assert any("non si accenderebbe mai" in g for g in problemi())


def test_la_stessa_parola_nei_due_banchi_non_e_un_guaio():
    """⚠️ `command.hsp` e `action.hsp` sono due catene diverse: «Guerriero»
    deve valere in tutt'e due, e cercare la doppia fra i file dichiarerebbe
    guasto proprio il lavoro fatto bene."""
    assert problemi() == []


def test_i_tetti_vengono_dal_sorgente_e_non_da_un_numero_a_mano(monkeypatch):
    """Se il monte stringe la casella, il cancello si accende."""
    desideri._controlla_tetti_dichiarati()
    monkeypatch.setattr(desideri, "TETTI_DICHIARATI",
                        [("command.hsp", 4461, 99, 198)])
    with pytest.raises(MonteMosso):
        desideri._controlla_tetti_dichiarati()


# --- da dove vengono i nomi ------------------------------------------------

def test_i_nomi_delle_classi_vengono_dal_dizionario_non_da_qui():
    """⭐ La parola da digitare e' la stessa che la scheda mostra, per
    costruzione: se `db_class.hsp.jsonl` cambia, cambia anche questa."""
    voci = {}
    percorso = percorsi.PROGETTO / "dizionario" / "db_class.hsp.jsonl"
    for riga in percorso.read_text(encoding="utf-8").splitlines():
        voce = json.loads(riga)
        if voce.get("it"):
            voci.setdefault(voce["en"], voce["it"])
    nomi = nomi_classi()
    assert len(nomi) == 12
    for chiave in CLASSI:
        assert nomi[chiave] == voci[chiave.capitalize()]


def test_una_classe_senza_resa_ferma_tutto(monkeypatch):
    monkeypatch.setattr(desideri, "CLASSI", CLASSI + ["nonesiste"])
    with pytest.raises(KeyError):
        nomi_classi()


# --- e che cosa finisce nella build ---------------------------------------

def test_ogni_riga_della_catena_e_decisa_o_dichiarata():
    """Nessuna riga resta senza qualcuno che se ne sia occupato."""
    classi = nomi_classi()
    for nome, numero, riga in righe_bersaglio():
        alternative(riga, classi)  # alza KeyError su quella che nessuno vuole


def test_le_toppe_non_toccano_mai_l_operando_della_chiave():
    """⚠️⚠️ La cosa che avrebbe rotto il gioco: `cdatan(CDATAN_CLASS) =
    \"warrior\"` e' una CHIAVE. Le toppe allungano la CONDIZIONE e basta, e
    ogni confronto che c'era prima c'e' ancora dopo."""
    import re
    confronto = re.compile(r'inputlog\s*==\s*"((?:[^"\\]|\\.)*)"')
    for toppa in toppe():
        prima = confronto.findall(toppa["cerca"])
        dopo = confronto.findall(toppa["sostituisci"])
        assert dopo[:len(prima)] == prima
        assert len(dopo) > len(prima)
        # e fuori dai confronti la riga e' identica
        assert (confronto.sub("", toppa["cerca"]).replace(" | ", "")
                == confronto.sub("", toppa["sostituisci"]).replace(" | ", ""))


def test_nella_build_ogni_classe_si_digita_in_italiano():
    """La prova sulla BUILD, non sul sorgente: e' quello che il giocatore ha."""
    nomi = nomi_classi()
    for nome_file in ("command.hsp", "action.hsp"):
        testo = (percorsi.BUILD_HSP / nome_file).read_bytes().decode("cp932")
        for chiave, italiano in nomi.items():
            atteso = 'inputlog == "%s"' % italiano
            assert atteso in testo, (
                "%s: chi ha scelto %r alla creazione non puo' digitarlo al "
                "banco del cambio classe." % (nome_file, italiano))


def test_nella_build_il_desiderio_parla_italiano():
    """Le parole chiave del desiderio, sulla build."""
    testo = (percorsi.BUILD_HSP / "command.hsp").read_bytes().decode("cp932")
    for chiave, parole in desideri.AGGIUNTE.items():
        for parola in parole:
            assert 'inputlog == "%s"' % parola in testo, (
                "il desiderio %r non risponde a %r" % (chiave, parola))
