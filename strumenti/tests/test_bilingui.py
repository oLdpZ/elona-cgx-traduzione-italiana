# strumenti/tests/test_bilingui.py
"""La rete dei menu bilingui: un menu si legge intero o non si legge.

Nata nella 76a, dopo che tre lotti di fila hanno scoperto la stessa cosa da tre
lati diversi: le firme sono condivise, quindi tradurre una voce di menu ne
traduce un'altra in una schermata lontana, che nessuno stava guardando. Alla
nascita ha trovato **quindici** menu a meta' in `chat.hsp`.
"""
import json

import pytest

from strumenti import estrai
from strumenti.bilingui import menu_bilingui

SORGENTE = """\
*finto_negoziante
\tchatList 0, lang("かいたい", "I want to buy.")
\tchatList 1, lang("うりたい", "I want to sell.")
\tbuff = lang("いらっしゃい", "Welcome!")
\tgosub *chat_select
\treturn

\t// le due chatList di sotto sono un ALTRO menu, e per blocchi_menu lo sono
\t// solo se distano piu' di sei righe: il raggruppamento e' per distanza
\t// (niente accenti ne' emoji qui dentro: il finto sorgente si scrive in cp932)
\t//
\t//
*finto_altrove
\tchatList 0, lang("はい", "Yes.")
\tchatList 1, lang("いいえ", "No.")
\tgosub *chat_select
\treturn
"""


@pytest.fixture
def finto(tmp_path):
    """Sorgente finto, piu' una fabbrica di dizionari con le firme vere."""
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    (sorgente / "finto.hsp").write_bytes(SORGENTE.encode("cp932"))
    dizionario = tmp_path / "dizionario"
    dizionario.mkdir()

    voci = estrai.estrai_da_testo("finto.hsp", SORGENTE)
    per_en = {v["en"]: v for v in voci}

    def scrivi(*inglesi: str) -> None:
        righe = []
        for inglese in inglesi:
            voce = dict(per_en[inglese])
            voce["it"] = "resa"
            righe.append(json.dumps(voce, ensure_ascii=False))
        (dizionario / "finto.hsp.jsonl").write_text(
            "\n".join(righe) + "\n", encoding="utf-8")

    scrivi()
    return sorgente, dizionario, scrivi, per_en


def _bilingui(finto, rinviate=None):
    sorgente, dizionario, _, _ = finto
    return menu_bilingui(["finto.hsp"], dizionario=dizionario,
                         sorgente=sorgente, rinviate=rinviate)


def test_un_menu_tutto_inglese_non_e_bilingue(finto):
    """Non e' un difetto: e' lavoro che non e' ancora cominciato."""
    assert _bilingui(finto) == []


def test_un_menu_tutto_reso_non_e_bilingue(finto):
    _, _, scrivi, _ = finto
    scrivi("I want to buy.", "I want to sell.")
    assert _bilingui(finto) == []


def test_un_menu_a_meta_e_bilingue(finto):
    """La regressione che questa rete esiste per impedire."""
    _, _, scrivi, _ = finto
    scrivi("I want to buy.")
    referto = _bilingui(finto)
    assert len(referto) == 1
    menu = referto[0]
    assert (menu["file"], menu["da"], menu["a"]) == ("finto.hsp", 2, 3)
    assert menu["voci"] == 2 and menu["fatte"] == 1
    assert [v["en"] for v in menu["restano"]] == ["I want to sell."]


def test_il_buff_non_e_una_voce_di_menu(finto):
    """`buff` disegna la domanda, non un bottone: non entra nel conto.

    Se ci entrasse, ogni menu con una domanda ancora inglese risulterebbe
    bilingue, e la rete direbbe «rotto» di tutto il file.
    """
    _, _, scrivi, _ = finto
    scrivi("I want to buy.", "I want to sell.")
    assert _bilingui(finto) == []


def test_una_rinviata_conta_come_fatta(finto, tmp_path):
    """⚠️ `chat.hsp:19327` e `:19334` sono righe COMMENTATE a monte.

    Non le disegna nessuno. Senza questa regola l'unico modo di chiudere il loro
    menu sarebbe tradurre codice morto — che e' quel che il rinvio esiste per non
    fare, e che nella 76a e' costato due numeri veri nei referti di
    `menu_dialogo` (la coda inglese fra le voci rotte a monte, la resa italiana
    fra quelle fuori misura).
    """
    _, _, scrivi, per_en = finto
    scrivi("I want to buy.")
    rinviate = tmp_path / "rinviate.jsonl"
    rinviate.write_text(json.dumps({
        "firma": per_en["I want to sell."]["firma"],
        "file": "finto.hsp",
        "en": "I want to sell.",
        "rinviata_a": "mai",
        "motivo": "prova",
    }, ensure_ascii=False) + "\n", encoding="utf-8")
    assert _bilingui(finto, rinviate=rinviate) == []


# --- la rete vera ------------------------------------------------------------

def test_nessun_menu_bilingue_nel_progetto():
    """Il valore atteso e' zero, su tutti i file che hanno un dizionario.

    ⚠️ Quando questo test diventa rosso non c'e' niente da «sistemare» nella
    rete: c'e' una schermata che il giocatore leggerebbe meta' in italiano e
    meta' in inglese, e va chiusa. Puo' diventarlo **senza che si sia toccato
    quel menu**, perche' la firma di una voce vive in piu' punti del file.
    """
    referto = menu_bilingui()
    assert referto == [], "\n".join(
        "%s:%d-%d  %d voci, %d rese, %d no"
        % (m["file"], m["da"], m["a"], m["voci"], m["fatte"], len(m["restano"]))
        for m in referto)
