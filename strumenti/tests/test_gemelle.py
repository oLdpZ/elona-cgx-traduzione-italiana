# strumenti/tests/test_gemelle.py
"""Il dizionario e' per file, e una firma resa in un file non arriva all'altro.

Nata nella 73a dal collaudo della 72a: nel registro dei messaggi
`You displace Tomdecker il cittadino.` stava cinque righe sotto «Ti scambi di
posto con Chur il cane», **con la stessa firma** — `action.hsp:1929` resa,
`chat.hsp:22587` no.
"""
import pytest

from strumenti import percorsi
from strumenti.gemelle import (
    DIVERGENTE,
    FILE_DELICATI,
    GEMELLA,
    QUASI,
    annota_menu,
    blocchi_menu,
    confronta,
    indice,
    lotto,
)
from strumenti.verifica import estrai_da_testo


def voci(nome_file: str, testo: str) -> list[dict]:
    return estrai_da_testo(nome_file, testo)


def resa(voce: dict, it: str) -> dict:
    """Una voce di dizionario tradotta, cioe' com'e' fatta una riga di `dizionario/*.jsonl`."""
    return dict(voce, it=it)


def test_una_firma_resa_in_un_altro_file_e_una_gemella():
    """Il caso di `You displace`: stessa firma, un file la rende e l'altro no."""
    altrove = voci("action.hsp", '\ttxt lang("と位置を入れ替えた。", " displace .")\n')
    qui = voci("chat.hsp", '\ttxt lang("と位置を入れ替えた。", " displace .")\n')

    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "Ti scambi di posto con.")]))

    assert [r["classe"] for r in righe] == [GEMELLA]
    assert righe[0]["rese"][0]["it"] == "Ti scambi di posto con."
    assert (righe[0]["rese"][0]["file"], righe[0]["rese"][0]["riga"]) == ("action.hsp", 1)


def test_una_firma_gia_resa_nel_proprio_file_non_e_una_gemella():
    """Quel che il dizionario del file copre gia' non e' lavoro: `tradotte` lo toglie."""
    qui = voci("chat.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    altrove = voci("action.hsp", '\ttxt lang("こんにちは", "Hello.")\n')

    righe = confronta(
        "chat.hsp", qui, {qui[0]["firma"]}, indice([resa(altrove[0], "Salve.")]))

    assert righe == []


def test_stesso_giapponese_ma_inglese_diverso_e_una_quasi_gemella():
    """La classe che non si travasa.

    ⚠️ La firma include l'inglese **e l'espressione**: se combacia solo il
    giapponese, la resa dell'altro sito puo' portarsi dietro le **variabili**
    dell'altro sito — `chara_func.hsp:4369` contro `map.hsp:14821`.
    """
    altrove = voci("map.hsp", '\ttxt lang("はをかばった！", name(tc) + " guarded " + name(tt) + ".")\n')
    qui = voci("chara_func.hsp", '\ttxt lang("はをかばった！", name(cc) + " guards " + name(ci) + ".")\n')

    righe = confronta(
        "chara_func.hsp", qui, set(),
        indice([resa(altrove[0], 'name(tc) + " protegge " + name(tt) + "."')]))

    assert [r["classe"] for r in righe] == [QUASI]


def test_una_firma_resa_in_due_modi_e_divergente():
    """«il cane» e «Cane» sono la stessa firma in due file: la rete non sceglie."""
    uno = voci("db_creature.hsp", '\ttxt lang("犬", "dog")\n')
    due = voci("chat.hsp", '\ttxt lang("犬", "dog")\n')
    qui = voci("event.hsp", '\ttxt lang("犬", "dog")\n')

    righe = confronta(
        "event.hsp", qui, set(),
        indice([resa(uno[0], "Cane"), resa(due[0], "il cane")]))

    assert [r["classe"] for r in righe] == [DIVERGENTE]
    assert sorted(r["it"] for r in righe[0]["rese"]) == ["Cane", "il cane"]


def test_la_gemella_identica_al_proprio_inglese_e_marcata():
    """`none`, `male?`, `hermaphrodite`: gia' decise da `invariati.md`, quindi gratis."""
    altrove = voci("command.hsp", '\ttxt lang("なし", "none")\n')
    qui = voci("chara.hsp", '\ttxt lang("なし", "none")\n')

    righe = confronta("chara.hsp", qui, set(), indice([resa(altrove[0], "none")]))

    assert righe[0]["classe"] == GEMELLA
    assert righe[0]["invariata"] is True


def test_il_giapponese_vuoto_non_fa_quasi_gemella():
    """⚠️ Una dinamica di sola morfologia ha `jp` **vuoto**, e il vuoto combacia con tutti.

    Misurato: `action.hsp:4584` (`The `) contro `blend.hsp:469` (`Selected `)
    hanno lo stesso giapponese — cioe' nessuno — e non hanno niente in comune.
    """
    altrove = voci("blend.hsp", '\ttxt lang(name(tc), "Selected " + name(tc))\n')
    qui = voci("action.hsp", '\ttxt lang(name(cc), "The " + name(cc))\n')

    righe = confronta(
        "action.hsp", qui, set(), indice([resa(altrove[0], '"Scelto " + name(tc)')]))

    assert righe == []


def test_una_firma_che_nessuno_ha_reso_non_compare():
    """La rete elenca il lavoro gia' fatto altrove, non il lavoro da fare."""
    qui = voci("chat.hsp", '\ttxt lang("こんにちは", "Hello.")\n')

    assert confronta("chat.hsp", qui, set(), indice([])) == []


def test_lo_stesso_sito_su_due_righe_si_conta_una_volta_sola():
    """La firma e' la chiave: due occorrenze sono una resa sola da scrivere."""
    altrove = voci("action.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    qui = voci("chat.hsp", '\ttxt lang("こんにちは", "Hello.")\n\ttxt lang("こんにちは", "Hello.")\n')

    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "Salve.")]))

    assert len(righe) == 1
    assert righe[0]["riga"] == 1


def test_il_lotto_riempie_it_con_la_resa_gemella():
    altrove = voci("action.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    qui = voci("chat.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "Salve.")]))

    voce = lotto(righe)[0]

    assert voce["it"] == "Salve."
    assert voce["file"] == "chat.hsp"
    assert voce["firma"] == qui[0]["firma"]


def test_il_lotto_porta_la_provenienza_in_gemella():
    """Il campo con l'underscore e' annotazione, come `_chiave` in `skill.hsp`.

    Serve a chi legge il lotto: la resa arriva da un altro sito, e il registro
    di quel sito puo' non essere quello di questo.
    """
    altrove = voci("action.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    qui = voci("chat.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "Salve.")]))

    assert lotto(righe)[0]["_gemella"] == "action.hsp:1"


def test_il_lotto_lascia_vuota_la_divergente_e_ci_mette_i_candidati():
    """Due rese per la stessa firma: sceglie chi legge, non la rete."""
    uno = voci("db_creature.hsp", '\ttxt lang("犬", "dog")\n')
    due = voci("chat.hsp", '\ttxt lang("犬", "dog")\n')
    qui = voci("event.hsp", '\ttxt lang("犬", "dog")\n')
    righe = confronta(
        "event.hsp", qui, set(), indice([resa(uno[0], "Cane"), resa(due[0], "il cane")]))

    voce = lotto(righe)[0]

    assert voce["it"] == ""
    assert sorted(voce["_gemelle"]) == ["chat.hsp:1 il cane", "db_creature.hsp:1 Cane"]


def test_il_lotto_non_porta_le_quasi_gemelle():
    """Sono un elenco da leggere, mai un lotto da reimportare."""
    altrove = voci("map.hsp", '\ttxt lang("はをかばった！", name(tc) + " guarded " + name(tt) + ".")\n')
    qui = voci("chara_func.hsp", '\ttxt lang("はをかばった！", name(cc) + " guards " + name(ci) + ".")\n')
    righe = confronta(
        "chara_func.hsp", qui, set(),
        indice([resa(altrove[0], 'name(tc) + " protegge " + name(tt) + "."')]))

    assert lotto(righe) == []


def test_il_lotto_di_un_file_delicato_si_rifiuta_senza_forza():
    """`custom_autopick.hsp` confronta le sue `lang()` contro il file del giocatore."""
    altrove = voci("db_race.hsp", '\ttxt lang("鎧", "armor")\n')
    qui = voci("custom_autopick.hsp", '\ttxt lang("鎧", "armor")\n')
    righe = confronta(
        "custom_autopick.hsp", qui, set(), indice([resa(altrove[0], "Armatura")]))

    with pytest.raises(ValueError, match="custom_autopick.hsp"):
        lotto(righe)

    assert lotto(righe, forza=True)[0]["it"] == "Armatura"


def test_custom_autopick_confronta_davvero_contro_il_file_del_giocatore():
    """Il motivo scritto in `FILE_DELICATI` e' un fatto del sorgente, non un ricordo.

    ⚠️ Tradurre una di quelle `lang()` cambia una **chiave di confronto**, non
    un'etichetta: il giocatore scrive `autopick.txt` a mano.
    """
    assert "custom_autopick.hsp" in FILE_DELICATI
    testo = (percorsi.SORGENTE_HSP / "custom_autopick.hsp").read_bytes().decode("cp932")
    dentro_instr = [r for r in testo.splitlines() if "instr(" in r and "lang(" in r]
    assert len(dentro_instr) > 50


# ------------------------------------------------------------------ i menu
#
# ⚠️⚠️ Una gemella dentro un menu non e' gratis. Le voci di `chatList` che
# stanno una sotto l'altra sono UNA schermata, e il giocatore le legge insieme:
# tradurne tre su dodici porta il menu da inglese e coerente a meta' italiano e
# incoerente, che e' la trappola della 64a (`db_race.hsp`) in un'altra forma.
# Misurato in `chat.hsp`: 82 delle 194 gemelle stanno dentro un menu, e nessuno
# dei 18 menu toccati sarebbe completo.

MENU = (
    '\t\t\tchatList 0, lang("殴打", "punch")\n'
    '\t\t\tchatList 1, lang("引っ掻き", "claw")\n'
    '\t\t\tchatList 2, lang("蹴り", "kick")\n'
)


def test_le_chatList_vicine_sono_un_menu_solo():
    assert blocchi_menu(MENU) == [[1, 2, 3]]


def test_un_if_in_mezzo_non_spezza_il_menu():
    """Il menu dei materiali di `chat.hsp:2637` ha tre righe di `if` fra una voce e l'altra."""
    testo = (
        '\t\t\tchatList 1, lang("革", "leather")\n'
        '\t\t\t}\n'
        '\t\t\tif ( x == 1 ) {\n'
        '\t\t\tchatList 2, lang("鱗", "scale")\n'
    )
    assert blocchi_menu(testo) == [[1, 4]]


def test_due_menu_lontani_sono_due_menu():
    testo = MENU + "\n" * 30 + '\t\t\tchatList 0, lang("いい", "Yes.")\n'
    assert [len(b) for b in blocchi_menu(testo)] == [3, 1]


def test_una_gemella_dentro_un_menu_dice_quanto_del_menu_copre():
    """Il numero che serve a decidere: tre voci su tre, o tre su dodici?"""
    altrove = voci("text.hsp", '\ttxt lang("引っ掻き", "claw")\n')
    qui = voci("chat.hsp", MENU)
    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "graffia")]))

    annota_menu(righe, MENU, tradotte=set())

    assert righe[0]["menu"] == {"da": 1, "a": 3, "voci": 3, "coperte": 1, "mancanti": 2}


def test_una_gemella_fuori_da_un_menu_non_ha_menu():
    altrove = voci("action.hsp", '\ttxt lang("こんにちは", "Hello.")\n')
    testo = '\ttxt lang("こんにちは", "Hello.")\n'
    righe = confronta("chat.hsp", voci("chat.hsp", testo), set(),
                      indice([resa(altrove[0], "Salve.")]))

    annota_menu(righe, testo, tradotte=set())

    assert righe[0]["menu"] is None


def test_una_voce_del_menu_gia_tradotta_non_manca():
    """Quel che il dizionario copre gia' non e' un buco nel menu."""
    altrove = voci("text.hsp", '\ttxt lang("引っ掻き", "claw")\n')
    qui = voci("chat.hsp", MENU)
    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "graffia")]))

    gia = {v["firma"] for v in qui if v["jp"] in ("殴打", "蹴り")}
    annota_menu(righe, MENU, tradotte=gia)

    assert righe[0]["menu"]["mancanti"] == 0


def test_il_lotto_porta_l_annotazione_del_menu():
    altrove = voci("text.hsp", '\ttxt lang("引っ掻き", "claw")\n')
    qui = voci("chat.hsp", MENU)
    righe = confronta("chat.hsp", qui, set(), indice([resa(altrove[0], "graffia")]))
    annota_menu(righe, MENU, tradotte=set())

    assert lotto(righe)[0]["_menu"] == "1-3: 1 di 3, ne mancano 2"


def test_una_quasi_gemella_nel_menu_conta_fra_le_mancanti():
    """⚠️ La quasi gemella non finisce nel lotto: nel menu resta un buco.

    Trovato confrontando il conto della rete con quello di un sondaggio scritto
    a mano — 44 mancanti contro 91 — ed e' la differenza fra «il menu si
    chiude» e «il menu resta meta' inglese». Contare fra le coperte una voce
    che nessuno scrivera' e' esattamente il difetto che la rete deve impedire.
    """
    menu = (
        '\t\t\tchatList 0, lang("引っ掻き", "claw")\n'
        '\t\t\tchatList 1, lang("蹴り", "kick")\n'
    )
    gemella = voci("text.hsp", '\ttxt lang("引っ掻き", "claw")\n')
    quasi = voci("text.hsp", '\ttxt lang("蹴り", "kicking")\n')
    qui = voci("chat.hsp", menu)

    righe = confronta("chat.hsp", qui, set(),
                      indice([resa(gemella[0], "graffio"), resa(quasi[0], "calcio")]))
    annota_menu(righe, menu, tradotte=set())

    assert [r["classe"] for r in righe] == [GEMELLA, QUASI]
    assert righe[0]["menu"]["coperte"] == 1
    assert righe[0]["menu"]["mancanti"] == 1
