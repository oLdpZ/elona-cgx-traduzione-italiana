"""Le prove della catena di `scene2.hsp`.

⚠️ La prova che conta di piu' non e' l'identita': e' la sua **prova al
contrario**. Un `applica_a_righe` che non toccasse mai niente supererebbe
l'identita' a occhi chiusi, e il progetto ha gia' visto una rete che diceva zero
perche' non cercava (107a). Qui sotto ogni cancello ha la sua coppia: uno che
pretende che non succeda niente, e uno che pretende che succeda.
"""
import json

import pytest

from strumenti import percorsi
from strumenti.scene import (CODA_MASSIMA, COLONNA_CHAT, LARGHEZZA_TXT,
                             SOFFITTO_CHAT, applica_a_righe, avvisi, blocchi,
                             carico_inglese, firma, leggi, problemi,
                             righe_a_capo, voci)


def _righe(testo: str) -> list[str]:
    return testo.split("\r\n")


UN_FILE = _righe(
    "{0}\r\n"
    '{pic}\t"bg3"\r\n'
    "{txt}\r\n"
    "In times long past,\r\n"
    "the land of Ylva.\r\n"
    "\r\n"
    "{1}\r\n"
    '{actor_1}\t"<Saimore> The Crown Prince of Zanan,54"\r\n'
    "{chat_1}\r\n"
    "War... Can not these nations recognize the crisis?\r\n"
    "\r\n"
)


def _diz(*voci_piene):
    return {(v["scena"], v["blocco"]): v for v in voci_piene}


# --- il modello del gioco -------------------------------------------------

def test_solo_txt_chat_e_wait_aprono_un_testo():
    """`scene.hsp:70-105`: gli altri marcatori non raccolgono niente.

    E' la regola da cui discende tutto il resto del modulo: la prosa che segue
    un `{pic}` o un `{fade}` non finisce a schermo.
    """
    trovati, morte = blocchi(_righe(
        "{0}\r\n"
        '{pic}\t"bg3"\r\n'
        "didascalia che il gioco salta\r\n"
        "{txt}\r\n"
        "prosa che il gioco disegna\r\n"
    ))
    per_tipo = {b["tipo"]: b for b in trovati}
    assert per_tipo["pic"]["prosa"] == []
    assert len(per_tipo["txt"]["prosa"]) == 1
    assert morte == [2]


def test_un_marcatore_qualunque_chiude_il_testo_aperto():
    # `scene.hsp:64-67`: una volta che scidxtop e' posato, il PRIMO `{` che
    # arriva chiude la finestra e la manda a schermo -- anche un `{pic}`
    trovati, morte = blocchi(_righe(
        "{0}\r\n"
        "{txt}\r\n"
        "dentro\r\n"
        '{pic}\t"bg3"\r\n'
        "fuori\r\n"
    ))
    per_tipo = {b["tipo"]: b for b in trovati}
    assert [i for i in per_tipo["txt"]["prosa"]] == [2]
    assert morte == [4]


def test_le_quattro_righe_morte_del_file_vero():
    """La rete di sicurezza sul file del progetto, non su uno costruito.

    Quattro didascalie di luogo che l'autore ha scritto dopo un `{pic}`, un
    `{fade}` e un `{actor_2}`. ⚠️ Se questo numero cambia, o il monte si e'
    mosso o il modello del flusso e' sbagliato: in tutt'e due i casi si guarda,
    non si aggiorna il numero.
    """
    righe = leggi()
    _, morte = blocchi(righe)
    assert len(morte) == 4
    assert all("-" in righe[i] for i in morte)


# --- il cancello dell'identita', e la sua prova al contrario --------------

def test_col_dizionario_vuoto_il_file_vero_torna_identico():
    righe = leggi()
    rifatte, fatte = applica_a_righe(righe, {})
    assert fatte == 0
    assert rifatte == righe


def test_e_col_dizionario_pieno_il_file_vero_CAMBIA():
    """⚠️ La prova al contrario dell'identita'.

    Senza di lei, un `applica_a_righe` che non facesse mai niente passerebbe il
    cancello qui sopra a occhi chiusi. Puntata dove il difetto ci sarebbe di
    sicuro, deve accendersi -- e dice **di quanto**, non un booleano.
    """
    righe = leggi()
    tutte = voci(righe)
    prima = next(v for v in tutte if v["tipo"] == "chat_1")
    prima["it"] = "Una resa italiana qualunque, che non somiglia all'inglese."
    rifatte, fatte = applica_a_righe(righe, _diz(prima))
    assert fatte == 1
    diverse = [i for i, (a, b) in enumerate(zip(righe, rifatte)) if a != b]
    assert len(diverse) == 1, "una resa sola deve toccare una riga sola"
    assert "Una resa italiana" in rifatte[diverse[0]]


def test_il_dizionario_vero_non_sposta_un_marcatore():
    """La rete di struttura, sul file vero e col dizionario vero.

    Un `{txt}` italiano puo' avere piu' o meno righe dell'inglese, quindi il
    file si accorcia o si allunga -- e un diff testuale, li', mente: fa
    sembrare *aggiunti* i marcatori che sono solo scivolati. Cio' che non deve
    cambiare non e' il numero di righe, sono tre cose:

      la sequenza dei blocchi   (scena, ordinale, tipo)
      gli argomenti dei marcatori che non sono attori  (`{pic}`, `{mc}`, ...)
      il numero di ritratto dopo la virgola di ogni `{actor_N}`

    ⚠️ E le righe che il gioco non disegna devono restare **quattro**: se
    l'iniezione ne creasse una quinta, avremmo scritto italiano in un punto
    che nessuno legge, e nessun conteggio lo direbbe.
    """
    from strumenti.scene import applica_a_righe, carica_dizionario

    prima = leggi()
    dopo, fatte = applica_a_righe(prima, carica_dizionario())
    if fatte == 0:
        pytest.skip("dizionario di scene2.hsp ancora vuoto")
    blocchi_prima, morte_prima = blocchi(prima)
    blocchi_dopo, morte_dopo = blocchi(dopo)

    def forma(elenco):
        return [(b["scena"], b["blocco"], b["tipo"]) for b in elenco]

    def non_attori(elenco):
        return [b["argomento"] for b in elenco if not b["tipo"].startswith("actor_")]

    def ritratti(elenco):
        return [b["argomento"].rpartition(",")[2]
                for b in elenco if b["tipo"].startswith("actor_")]

    assert forma(blocchi_dopo) == forma(blocchi_prima)
    assert non_attori(blocchi_dopo) == non_attori(blocchi_prima)
    assert ritratti(blocchi_dopo) == ritratti(blocchi_prima)
    assert len(morte_dopo) == len(morte_prima) == 4


def test_il_dizionario_vero_si_riscrive_in_cp932():
    """Cio' che non entra in CP932 sparisce in silenzio alla build.

    `degrada` toglie gli accenti, ma non tutto: le virgolette basse «» non
    esistono in CP932, e il progetto per questo usa `"` nelle rese (10.626
    volte). Se una resa portasse un carattere non rappresentabile, l'errore
    va visto qui e non a compilazione.
    """
    from strumenti.scene import applica_a_righe, carica_dizionario

    dopo, fatte = applica_a_righe(leggi(), carica_dizionario())
    if fatte == 0:
        pytest.skip("dizionario di scene2.hsp ancora vuoto")
    "\r\n".join(dopo).encode("cp932")


# --- le tre iniezioni -----------------------------------------------------

def test_un_txt_italiano_puo_avere_un_numero_di_righe_diverso():
    # e' il motivo per cui `applica_a_righe` lavora all'indietro: se il blocco
    # si allunga, tutti gli indici sotto di lui slittano
    tutte = voci(UN_FILE)
    testo = next(v for v in tutte if v["tipo"] == "txt")
    testo["it"] = "Molto tempo fa,\nla terra di Ylva\nvide dieci civiltà."
    rifatte, _ = applica_a_righe(UN_FILE, _diz(testo))
    # ⚠️ nel dizionario l'accento e' vero; a degradarlo e' l'iniezione
    assert rifatte[3:6] == ["Molto tempo fa,", "la terra di Ylva",
                            "vide dieci civilta'."]
    # e cio' che stava sotto non si e' perso ne' spostato di senso
    assert "{chat_1}" in rifatte
    assert rifatte.count("{1}") == 1


def test_l_attore_conserva_il_ritratto():
    tutte = voci(UN_FILE)
    attore = next(v for v in tutte if v["tipo"] == "actor_1")
    assert attore["en"] == "<Saimore> The Crown Prince of Zanan"
    attore["it"] = "<Saimore> il principe ereditario di Zanan"
    rifatte, _ = applica_a_righe(UN_FILE, _diz(attore))
    assert rifatte[7] == '{actor_1}\t"<Saimore> il principe ereditario di Zanan,54"'


def test_l_attore_conserva_anche_uno_spazio_prima_del_ritratto():
    """`{Itzpalt} Of Element, 61` ha uno spazio che `int()` regge.

    Non e' pulito, ma e' del monte: la coda dopo la virgola si ricopia
    verbatim, non si normalizza. Normalizzarla sarebbe una modifica al
    sorgente travestita da traduzione.
    """
    righe = _righe('{0}\r\n{actor_1}\t"{Itzpalt} Of Element, 61"\r\n')
    attore = voci(righe)[0]
    assert attore["en"] == "{Itzpalt} Of Element"
    attore["it"] = "{Itzpalt} dell'Elemento"
    rifatte, _ = applica_a_righe(righe, _diz(attore))
    assert rifatte[1] == '{actor_1}\t"{Itzpalt} dell\'Elemento, 61"'


def test_gli_accenti_si_degradano_come_in_tutto_il_resto():
    tutte = voci(UN_FILE)
    chiacchiera = next(v for v in tutte if v["tipo"] == "chat_1")
    chiacchiera["it"] = "Perché la guerra?"
    rifatte, _ = applica_a_righe(UN_FILE, _diz(chiacchiera))
    assert "Perche' la guerra?" in rifatte


# --- il monte che si muove sotto una resa ---------------------------------

def test_una_firma_che_non_torna_ferma_tutto():
    tutte = voci(UN_FILE)
    chiacchiera = next(v for v in tutte if v["tipo"] == "chat_1")
    chiacchiera["it"] = "Una resa qualunque."
    chiacchiera["firma"] = firma("un inglese che non c'e' piu'")
    with pytest.raises(ValueError, match="il monte non e' piu' quello"):
        applica_a_righe(UN_FILE, _diz(chiacchiera))


# --- l'a capo del gioco ---------------------------------------------------

def test_l_a_capo_spezza_sugli_spazi_e_mai_dentro_una_parola():
    testo = "a " * 40
    for riga in righe_a_capo(testo.strip()):
        assert len(riga) <= COLONNA_CHAT + 1


def test_una_parola_piu_lunga_della_colonna_non_si_spezza():
    # `init.hsp:1332`: si cerca lo spazio, non la colonna. Una parola che non
    # ci sta esce dal riquadro, ed e' l'unico modo di sforare in LARGHEZZA
    lunghissima = "x" * 80
    assert righe_a_capo(lunghissima) == [lunghissima]


def test_l_inglese_di_monte_supera_il_soffitto_in_un_blocco_solo():
    """⚠️ Il fatto scomodo su cui poggia tutta la misura dell'altezza.

    Il blocco piu' lungo del file (scena 11) fa **14** righe, cioe' **una in
    piu'** del soffitto che il progetto usa dalla 70a. Non e' un permesso: e' la
    stessa cosa che la 70a aveva gia' notato su `chat.hsp:7289`, l'inglese di
    monte che sfora. Serve saperlo per due ragioni opposte:

    - non si «corregge» il soffitto per far entrare quel blocco -- l'inglese
      che sfora non prova che il riquadro sia piu' alto;
    - non si prende quel blocco come esempio di impaginazione.

    ⓘ Se questo test si accende sono cambiate due cose diverse, e vanno
    distinte: il monte (il blocco non fa piu' 14) oppure il soffitto (qualcuno
    l'ha ritoccato). Il messaggio dice quale.
    """
    righe = leggi()
    peggiore, scena = max(
        (len(righe_a_capo(v["en"])), v["scena"])
        for v in voci(righe) if v["tipo"].startswith("chat_")
    )
    assert (peggiore, scena) == (14, "11"), "il monte e' cambiato"
    assert SOFFITTO_CHAT == 13, "il soffitto e' stato ritoccato"
    assert peggiore == SOFFITTO_CHAT + 1


# --- i controlli sulle rese -----------------------------------------------

def test_un_txt_troppo_largo_si_accende():
    voce = {"tipo": "txt", "it": "x" * (LARGHEZZA_TXT + 1)}
    assert any("oltre i %d" % LARGHEZZA_TXT in p for p in problemi(voce))


def test_un_txt_largo_esatto_NON_si_accende():
    # la prova al contrario del cancello della larghezza: al limite passa
    assert problemi({"tipo": "txt", "it": "x" * LARGHEZZA_TXT}) == []


def test_una_riga_vuota_dentro_un_txt_si_accende():
    # il gioco la cancella (scene.hsp:410-415): chi la scrive crede di aver
    # separato un capoverso e non ha separato niente
    voce = {"tipo": "txt", "it": "prima\n\ndopo"}
    assert any("vuota" in p for p in problemi(voce))


def test_un_chat_troppo_alto_si_accende():
    voce = {"tipo": "chat_1", "it": "parola " * 200}
    assert any("il riquadro ne tiene" in p for p in problemi(voce))


def test_un_chat_esattamente_al_soffitto_NON_si_accende():
    # la prova al contrario del cancello dell'altezza: a 13 righe esatte passa
    righe = leggi()
    al_limite = next(v for v in voci(righe)
                     if v["tipo"].startswith("chat_")
                     and len(righe_a_capo(v["en"])) == SOFFITTO_CHAT)
    assert problemi({"tipo": "chat_1", "it": al_limite["en"]}) == []


def test_una_resa_che_si_allunga_piu_dell_inglese_si_accende():
    """⭐ La regola della 73a, e vale piu' del tetto assoluto.

    Il tetto puo' essere sbagliato di una riga -- e questa fase ha gia' visto
    due letture che differiscono di uno. Questo confronto no: se l'inglese
    stava in tre righe e l'italiano ne fa quattro, l'italiano si e' allungato
    dove il monte era gia' impaginato, quale che sia il numero giusto.
    """
    inglese = "parola " * 7                      # 48 caratteri: una riga sola
    italiano = "parola " * 9                      # 62: il gioco ne fa due
    assert len(righe_a_capo(inglese.strip())) == 1
    assert len(righe_a_capo(italiano.strip())) == 2
    voce = {"tipo": "chat_1", "en": inglese.strip(), "it": italiano.strip()}
    # ⚠️ e' un AVVISO, non un rifiuto: `problemi` deve restare muto
    assert problemi(voce) == []
    assert any("dell'inglese" in a for a in avvisi(voce))


def test_una_resa_lunga_come_l_inglese_NON_si_accende():
    inglese = "Una battuta corta che sta in una riga."
    assert avvisi({"tipo": "chat_1", "en": inglese, "it": inglese}) == []


def test_una_virgola_nel_nome_dell_attore_si_accende():
    # `csvsort` taglia sulla virgola: una virgola in piu' si porta via il
    # ritratto e il gioco disegna la faccia sbagliata
    voce = {"tipo": "actor_1", "it": "<Saimore>, principe di Zanan"}
    assert any("virgola" in p for p in problemi(voce))


def test_le_forme_sbagliate_si_riconoscono():
    assert any("stringa sola" in p
               for p in problemi({"tipo": "txt", "it": ["una", "lista"]}))
    assert any("non porta a capo" in p
               for p in problemi({"tipo": "chat_1", "it": "una\nriga"}))


# --- il lotto -------------------------------------------------------------

def test_una_voce_porta_tutto_cio_che_serve_a_ritrovarla():
    voce = voci(UN_FILE)[0]
    for campo in ("firma", "file", "riga", "scena", "blocco", "tipo", "en", "it"):
        assert campo in voce
    assert json.loads(json.dumps(voce, ensure_ascii=False)) == voce


def test_si_estrae_una_scena_alla_volta():
    solo_zero = voci(UN_FILE, {"0"})
    assert {v["scena"] for v in solo_zero} == {"0"}
    assert len(solo_zero) < len(voci(UN_FILE))


def test_il_carico_di_un_blocco_senza_testo_e_niente():
    trovati, _ = blocchi(UN_FILE)
    immagine = next(b for b in trovati if b["tipo"] == "pic")
    assert carico_inglese(immagine, UN_FILE) is None
