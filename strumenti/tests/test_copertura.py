# strumenti/tests/test_copertura.py
"""La rete che parte dal sorgente invece che dai dizionari.

Il caso vero che l'ha fatta nascere e' il gioco di carte: `tcg_mod.hsp` (809
stringhe inglesi distinte a schermo) e `tcg_skill.hsp` (142), dentro un
progetto in cui **quattro** contatori dicevano 100% perche' partivano tutti
dall'elenco delle cose gia' coperte. Vedi la testa di `strumenti/copertura.py`.

⚠️ Le prove che contano qui sono le due «al contrario»:
`test_il_caso_vero_si_accende_senza_la_sua_riga` e
`test_un_dizionario_di_otto_voci_non_copre_ottocento_stringhe`. Senza quelle,
una prova su un file finto direbbe soltanto che una regex funziona su una
stringa che ho scritto io.
"""
import pytest

from strumenti import copertura, percorsi
from strumenti.commenti import righe_in_commento

# La riga vera di `sound.hsp:998`, che il riconoscitore NON deve salvare:
# `close music` sono due parole inglesi, ma sono un comando MCI di Windows.
MCI = '\t\tmci "close music"\n'

# La riga vera di `tcg_skill.hsp`, che DEVE prendere.
SCHEDA = ('\t\t\t\t\tcarddetailneff@tcg(cextra@tcg) = "Puff Puff Bread   '
          'No.???   puffy puffy bread  Rare:None\\n[Command Card]\\nEffect: '
          'Feed the Puff Puff Bread to 1 of your Card."\n')


def test_una_frase_si_riconosce_e_un_identificatore_no():
    testo = (SCHEDA
             + '\tif ( cardn@tcg(TCG_CARDN_REF_RACE, cnt) == "dragon" ) { x@tcg++ }\n'
             + '\t{pic}\t"bg3"\n'
             + '\tioriginalnameref(ITEM_ID_BANANA) = "banana"\n')

    trovati = copertura.letterali_di_prosa(testo)

    assert len(trovati) == 1
    assert trovati[0].startswith("Puff Puff Bread")


def test_una_riga_spenta_da_barre_non_conta():
    """`tcg.hsp:1505` e' una `lang()` spenta da `//`, e le rinviate la chiamano
    «la quarta volta» che una rete del progetto guarda solo il `;`."""
    vivo = copertura.letterali_di_prosa('\tmes "Unsaved data will be lost."\n')
    spento = copertura.letterali_di_prosa('\t// mes "Unsaved data will be lost."\n')
    punto_e_virgola = copertura.letterali_di_prosa('\t; mes "Unsaved data will be lost."\n')

    assert len(vivo) == 1
    assert spento == []
    assert punto_e_virgola == []


def test_un_letterale_con_virgoletta_protetta_non_spezza_la_scansione():
    """La regola del backslash di `estrai.py`: `\\"` non chiude la stringa.

    Se la scansione si fermasse alla virgoletta protetta, il letterale
    finirebbe a `the sign reads \\` e la coda — «in red letters» — resterebbe
    fuori: e' il danno silenzioso che `estrai.py` documenta sotto ESCAPE.
    """
    trovati = copertura.letterali_di_prosa(
        '\tmes "the sign reads \\"no entry\\" in red letters"\n')

    assert trovati == ['the sign reads \\"no entry\\" in red letters']


def test_un_comando_del_sistema_operativo_e_prosa_e_questo_e_voluto():
    """La prova al contrario del riconoscitore: `close music` PASSA il filtro.

    Non e' un difetto da correggere in regex — e' il motivo per cui esistono
    le dichiarazioni. Un riconoscitore che sbaglia per eccesso costa una riga
    con scritto perche'; uno che sbaglia per difetto costa un'altra Fase 4
    chiusa al 100% con 951 stringhe inglesi dentro.
    """
    assert copertura.letterali_di_prosa(MCI) == ["close music"]
    assert copertura.DICHIARATI["sound.hsp"].tipo == "esente"


def test_una_stringa_dentro_lang_e_raggiunta_e_una_fuori_no():
    """La copertura si misura sulla singola stringa, e la sola scansione che
    dice dove sta una `lang()` e' `estrai.siti()`."""
    testo = ('\ttxt lang("こんにちは世界", "hello there world")\n'
             '\tmes "goodbye cruel world"\n')

    scoperte = copertura.scoperte_di("finto.hsp", testo, set())

    assert scoperte == ["goodbye cruel world"]


def test_una_riga_riscritta_da_una_toppa_e_raggiunta():
    riga = '\tmes "goodbye cruel world"'
    testo = riga + "\n"

    assert copertura.scoperte_di("finto.hsp", testo, set()) == ["goodbye cruel world"]
    assert copertura.scoperte_di("finto.hsp", testo, {riga.strip()}) == []


def test_un_dizionario_di_otto_voci_non_copre_ottocento_stringhe():
    """⭐ LA PROVA AL CONTRARIO DEL PRIMO CENSIMENTO DELLA 135a.

    `tcg_mod.hsp` HA un dizionario (8 voci) e una toppa, e per questo la prima
    versione di questo modulo lo dava per coperto. Ha 809 stringhe che non
    raggiunge nessuno. Se un giorno qualcuno rimettesse la copertura a livello
    di file, questa prova cade.
    """
    assert (percorsi.DIZIONARIO / "tcg_mod.hsp.jsonl").exists()

    riga = next(r for r in copertura.censimento() if r["file"] == "tcg_mod.hsp")

    assert riga["distinte"] == 809


def test_il_sorgente_pinnato_non_ha_file_scoperti_e_non_dichiarati():
    """Il cancello vero, sul sorgente vero. Verde = ogni file con stringhe
    scoperte o ha un meccanismo suo, o ha una riga con scritto perche'."""
    assert copertura.problemi() == []


def test_il_caso_vero_si_accende_senza_la_sua_riga(monkeypatch):
    """⭐ LA PROVA AL CONTRARIO.

    Tolta la dichiarazione di `tcg_skill.hsp`, il cancello deve accendersi
    **sul file vero**. Cosi' la prova non passa perche' il caso e' sparito, ma
    perche' c'e' e viene riconosciuto.
    """
    senza = {n: d for n, d in copertura.DICHIARATI.items() if n != "tcg_skill.hsp"}
    monkeypatch.setattr(copertura, "DICHIARATI", senza)

    guai = copertura.problemi()

    assert len(guai) == 1
    assert guai[0].startswith("tcg_skill.hsp: 142 stringhe inglesi distinte")


def test_un_conto_dichiarato_che_non_torna_si_accende(monkeypatch):
    """Il monte e' pinnato a un tag apposta: se si muovesse, una dichiarazione
    vecchia coprirebbe un file diverso da quello che descriveva."""
    finto = dict(copertura.DICHIARATI)
    finto["tcg_skill.hsp"] = copertura.Dichiarazione("fronte", 141, "conto vecchio")
    monkeypatch.setattr(copertura, "DICHIARATI", finto)

    guai = copertura.problemi()

    assert len(guai) == 1
    assert "dichiarate 141 stringhe scoperte, nel sorgente ne sono 142" in guai[0]


def test_una_dichiarazione_diventata_inutile_si_accende():
    """Quando un fronte dichiarato viene lavorato, la sua riga va tolta. Senza
    questo la lista marcisce e dichiara aperto un fronte chiuso.

    ⚠️ Il file NON sparisce dal censimento: resta, con zero stringhe scoperte.
    E' come si e' presentato `custom_lib.hsp` alla 135a, appena scritta la sua
    toppa — due letterali di prosa, nessuno dei due scoperto — e la prima
    versione del ciclo, che guardava solo se la riga mancava, lo lasciava
    passare. Il caso vero l'ha trovato lui.
    """
    righe = []
    for riga in copertura.censimento():
        if riga["file"] == "tcg_skill.hsp":
            riga = riga | {"scoperte": 0, "distinte": 0}   # come se fosse lavorato
        righe.append(riga)

    guai = copertura.problemi(righe)

    assert len(guai) == 1
    assert guai[0].startswith("tcg_skill.hsp:")
    assert "La riga va tolta" in guai[0]


def test_le_due_toppe_della_135a_chiudono_i_loro_file():
    """`custom_lib.hsp` sparisce dai file con stringhe scoperte, e
    `custom_itemlist.hsp` resta con la sola intestazione TSV, che non si
    traduce. E' il giro completo — misura, resa, cancello — su un caso vero."""
    per_nome = {r["file"]: r for r in copertura.censimento()}

    assert per_nome["custom_lib.hsp"]["distinte"] == 0
    assert "custom_lib.hsp" not in copertura.DICHIARATI

    assert per_nome["custom_itemlist.hsp"]["distinte"] == 1
    assert copertura.DICHIARATI["custom_itemlist.hsp"].tipo == "esente"


def test_scene2_ha_un_meccanismo_suo_e_non_una_esenzione():
    """Le sue 99 sono le etichette `{actor_N}`, che `scene.py:45` tratta come
    un tipo di blocco: coperte da `scene --applica`, sorvegliate da
    `scene --referto`. Chiamarle «esenti» direbbe il falso."""
    assert "scene2.hsp" in copertura.MECCANISMI
    assert "scene2.hsp" not in copertura.DICHIARATI
    assert "scene2.hsp" not in copertura.DA_TRIARE

    riga = next(r for r in copertura.censimento() if r["file"] == "scene2.hsp")

    assert riga["distinte"] == 99          # le vede, e non le conta come guaio


@pytest.mark.parametrize("nome", sorted(copertura.DICHIARATI))
def test_ogni_dichiarazione_dice_perche(nome):
    """Una riga senza ragione e' una riga che nessuno potra' rivedere."""
    dichiarata = copertura.DICHIARATI[nome]

    assert dichiarata.tipo in ("esente", "fronte")
    assert dichiarata.scoperte > 0
    assert len(dichiarata.motivo) > 80


def test_un_elenco_dentro_un_commento_di_blocco_non_e_un_fronte():
    """⭐ LA PROVA AL CONTRARIO DEL RICONOSCITORE DI RIGHE MORTE.

    `custom_tweaks.hsp` apre con un `/*` a riga 1, lo chiude a riga 85, e in
    mezzo tiene l'elenco documentativo delle 75 voci del menu Tweaks. Erano
    tutte e 75 le sue «stringhe scoperte», e per mezz'ora sono state il secondo
    fronte piu' grosso del progetto — il file ha 264 toppe, quindi sembrava
    perfino plausibile che il menu fosse restato indietro.

    La prima asserzione e' la prova al contrario: senza le righe morte il caso
    si riaccende, cosi' questa prova non passa perche' il file e' cambiato ma
    perche' il salto funziona.
    """
    percorso = percorsi.SORGENTE_HSP / "custom_tweaks.hsp"
    testo = percorso.read_bytes().decode("cp932")
    morte = righe_in_commento(percorso)
    toppe = copertura._righe_con_toppa()["custom_tweaks.hsp"]

    assert len(copertura.scoperte_di("custom_tweaks.hsp", testo, toppe)) == 75
    assert copertura.scoperte_di("custom_tweaks.hsp", testo, toppe, morte) == []
    # ⓘ `righe_in_commento` marca l'apertura e il corpo ma NON la riga che
    # chiude: la :85 di `*/` resta viva. E' la sua convenzione, e sbaglia
    # dalla parte giusta — una stringa su quella riga verrebbe contata, non
    # persa.
    assert 1 in morte and 84 in morte
    assert 85 not in morte and 86 not in morte

    # e il file non deve comparire da nessuna parte: non e' un fronte
    assert "custom_tweaks.hsp" not in copertura.DICHIARATI
    assert "custom_tweaks.hsp" not in copertura.DA_TRIARE


def test_ogni_file_con_stringhe_scoperte_e_dichiarato():
    """Alla 135a `DA_TRIARE` e' stato svuotato: non resta un file misurato e
    non guardato. Se questa cade, qualcuno ha aggiunto un file senza ragione."""
    non_dichiarati = [r["file"] for r in copertura.censimento()
                      if r["distinte"] and r["file"] not in copertura.MECCANISMI
                      and r["file"] not in copertura.DICHIARATI]

    assert non_dichiarati == []


def test_il_debito_non_triato_non_si_confonde_coi_fronti():
    """`DA_TRIARE` e' una misura, non un giudizio: nessuno di quei file deve
    avere anche una Dichiarazione, o si leggerebbero due verita' diverse."""
    doppi = set(copertura.DA_TRIARE) & set(copertura.DICHIARATI)

    assert doppi == set()
