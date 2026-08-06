import pytest

from strumenti import percorsi
from strumenti.applica import SorgenteCorrotto, applica_a_testo
from strumenti.estrai import estrai_da_testo, firma, siti, spezza_righe

STATICA = '	txt lang("バックパックが一杯だ。", "Your inventory is full.")'


def dizionario_con(jp, en, it, tipo="statica"):
    chiave = firma(jp, en)
    return {chiave: {
        "firma": chiave, "jp": jp, "jp_grezzo": f'"{jp}"',
        "en": en, "en_grezzo": f'"{en}"',
        "it": it, "tipo": tipo, "occorrenza": 0,
    }}


def test_sostituisce_l_inglese_con_l_italiano():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Il tuo zaino e' pieno.")
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, diz)
    assert sostituzioni == 1
    assert '"Il tuo zaino e\' pieno."' in testo
    assert "Your inventory is full." not in testo


def test_conserva_il_giapponese():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert "バックパックが一杯だ。" in testo


def test_degrada_gli_accenti_in_fase_di_applicazione():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "È già pieno.")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    assert '"E\' gia\' pieno."' in testo
    assert "È" not in testo


def test_lascia_intatte_le_stringhe_non_tradotte():
    testo, sostituzioni = applica_a_testo("text.hsp", STATICA, {})
    assert sostituzioni == 0
    assert testo == STATICA


def test_il_risultato_e_codificabile_in_cp932():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Perché è così")
    testo, _ = applica_a_testo("text.hsp", STATICA, diz)
    ritorno = testo.encode("cp932").decode("cp932")
    assert ritorno == testo


def test_conserva_i_fine_riga_crlf():
    sorgente = STATICA + "\r\n" + "	mes \"altro\"" + "\r\n"
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    testo, _ = applica_a_testo("text.hsp", sorgente, diz)
    assert "\r\n" in testo
    assert "\n" not in testo.replace("\r\n", "")
    assert testo.endswith("\r\n")


def test_la_dinamica_non_viene_messa_fra_virgolette():
    # per le dinamiche l'italiano e' gia' un'espressione HSP completa: se viene
    # avvolta fra virgolette come una statica, il codice HSP finisce a schermo.
    sorgente = (
        '	txt lang(name(tc) + "を守った。" + name(x) + "。", '
        'name(tc) + " guarded " + name(x) + ".")'
    )
    espressione = 'name(tc) + " ha protetto " + name(x) + "."'
    diz = dizionario_con("を守った。。", " guarded .", espressione, tipo="dinamica")
    testo, sostituzioni = applica_a_testo("text.hsp", sorgente, diz)
    assert sostituzioni == 1
    assert espressione in testo
    assert '"' + espressione + '"' not in testo


def test_due_lang_sulla_stessa_riga_con_lunghezze_diverse():
    # due lang() sulla stessa riga, con traduzioni di lunghezza diversa
    # dall'inglese originale (una piu' lunga, una piu' corta): verifica che
    # le posizioni di sostituzione non si sfalsino tra la prima e la seconda.
    sorgente = '	txt lang("jp1", "en1") + "  " + lang("jp2", "en2")'
    diz = {}
    diz.update(dizionario_con("jp1", "en1", "Una traduzione molto piu' lunga dell'originale"))
    diz.update(dizionario_con("jp2", "en2", "corta"))
    testo, sostituzioni = applica_a_testo("text.hsp", sorgente, diz)
    assert sostituzioni == 2
    atteso = (
        '	txt lang("jp1", "Una traduzione molto piu\' lunga dell\'originale") + "  " '
        '+ lang("jp2", "corta")'
    )
    assert testo == atteso


# --- estrai e applica camminano sugli stessi siti (rilievo IMPORTANT 3) ------

def test_scansione_condivisa_su_un_file_vero():
    """estrai.py e applica.py non riscrivono piu' a mano la stessa scansione.

    La coincidenza dev'essere strutturale, non frutto di disciplina: qui si
    asserisce su un file reale che le voci estratte e i siti che applica.py
    percorre sono gli stessi, nello stesso ordine, con gli stessi span.
    """
    percorso = percorsi.SORGENTE_HSP / "text.hsp"
    if not percorso.exists():
        pytest.skip("il clone del sorgente non e' disponibile")
    testo = percorso.read_bytes().decode("cp932")

    voci = estrai_da_testo("text.hsp", testo)
    elenco = list(siti(testo))
    assert len(voci) == len(elenco) > 2000

    righe, _, _ = spezza_righe(testo)
    for voce, sito in zip(voci, elenco):
        numero_riga, chiave, occorrenza, jp, _, en, grezzo_en, inizio, fine = sito
        assert (voce["riga"], voce["firma"], voce["occorrenza"]) == (numero_riga, chiave, occorrenza)
        assert (voce["jp"], voce["en"], voce["en_grezzo"]) == (jp, en, grezzo_en)
        # lo span e' quello che applica.py sostituisce: deve ritagliare
        # esattamente il secondo argomento della riga reale
        assert righe[numero_riga - 1][inizio:fine] == grezzo_en

    # e applica.py, guidato dal dizionario completo, li tocca tutti
    diz = {v["firma"]: dict(v, it="X") for v in voci}
    _, sostituzioni = applica_a_testo("text.hsp", testo, diz)
    assert sostituzioni == len(voci)


def test_applica_consuma_tutte_le_firme_del_dizionario():
    consumate = set()
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    applica_a_testo("text.hsp", STATICA, diz, consumate)
    assert consumate == set(diz)


def test_le_firme_orfane_restano_fuori_dalle_consumate():
    # SPEC 3.1: al riallineamento a una nuova versione CGX le firme sparite
    # a monte sono la coda di ritraduzione, non voci da ignorare in silenzio.
    consumate = set()
    diz = dizionario_con("non", "esiste piu' a monte", "sparita")
    applica_a_testo("text.hsp", STATICA, diz, consumate)
    assert consumate == set()


# --- post-condizione strutturale (rilievo IMPORTANT 4) ----------------------
# Quattro classi di traduzione passano verifica.py e producono sorgente rotto.

DINAMICA = (
    '	txt lang(name(tc) + "を守った。", name(tc) + " guarded.")'
)


def dinamica_con(it):
    return dizionario_con("を守った。", " guarded.", it, tipo="dinamica")


def test_rifiuta_una_dinamica_con_virgoletta_non_chiusa():
    with pytest.raises(SorgenteCorrotto, match="text.hsp:1"):
        applica_a_testo("text.hsp", DINAMICA, dinamica_con('name(tc) + " ha protetto'))


def test_rifiuta_una_dinamica_con_parentesi_non_chiusa():
    with pytest.raises(SorgenteCorrotto, match="text.hsp:1"):
        applica_a_testo("text.hsp", DINAMICA, dinamica_con('name(tc + " ha protetto."'))


def test_rifiuta_una_dinamica_con_una_virgola_nuda():
    # il caso senza segnale: virgolette pari, parentesi pari, riestrazione
    # riuscita — ma lang() si ritrova a tre argomenti.
    with pytest.raises(SorgenteCorrotto, match="tre argomenti"):
        applica_a_testo("text.hsp", DINAMICA, dinamica_con('name(tc) + " ha protetto", x'))


def test_rifiuta_una_statica_che_finisce_con_un_backslash():
    # il backslash escapa la virgoletta di chiusura che applica.py aggiunge
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.\\")
    with pytest.raises(SorgenteCorrotto):
        applica_a_testo("text.hsp", STATICA, diz)


def test_l_errore_nomina_file_riga_e_firma():
    chiave = firma("を守った。", " guarded.")
    with pytest.raises(SorgenteCorrotto) as errore:
        applica_a_testo("proc.hsp", "\r\n" + DINAMICA, dinamica_con('f( + "rotta'))
    messaggio = str(errore.value)
    assert "proc.hsp:2" in messaggio
    assert chiave in messaggio


def test_una_riga_gia_malformata_a_monte_non_e_colpa_nostra():
    # una lang() malformata gia' nel sorgente non deve far fallire la
    # sostituzione di una lang() sana sulla stessa riga
    sorgente = '	txt lang("jp1", "en1") + lang("rotta"'
    diz = dizionario_con("jp1", "en1", "tradotta")
    testo, sostituzioni = applica_a_testo("text.hsp", sorgente, diz)
    assert sostituzioni == 1
    assert '"tradotta"' in testo


# --- accessi coerenti (rilievo IMPORTANT 7) ---------------------------------

def test_una_voce_senza_tipo_nomina_file_e_riga():
    diz = dizionario_con("バックパックが一杯だ。", "Your inventory is full.", "Zaino pieno.")
    for voce in diz.values():
        del voce["tipo"]
    with pytest.raises(ValueError, match="text.hsp:1.*tipo"):
        applica_a_testo("text.hsp", STATICA, diz)


def test_una_virgola_dentro_una_chiamata_annidata_e_legittima():
    # cdata(CDATA_SEX, CHARA_PLAYER) e' un solo argomento, non due
    espressione = 'name(tc) + " e\' " + _onii(cdata(CDATA_SEX, CHARA_PLAYER))'
    testo, sostituzioni = applica_a_testo("text.hsp", DINAMICA, dinamica_con(espressione))
    assert sostituzioni == 1
    assert espressione in testo
