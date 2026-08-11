# strumenti/tests/test_verifica.py
import json

from strumenti import percorsi
from strumenti.estrai import estrai_da_testo
from strumenti.verifica import (carica_invariati, confronta_col_sorgente,
                                controlla_lotto, controlla_voce)


def voce(**sovrascritture):
    base = {
        "firma": "abc", "file": "text.hsp", "riga": 1, "occorrenza": 0,
        "jp": "バックパックが一杯だ。", "jp_grezzo": '"バックパックが一杯だ。"',
        "en": "Your inventory is full.", "en_grezzo": '"Your inventory is full."',
        "tipo": "statica", "contesto": "", "it": "Il tuo zaino e' pieno.",
    }
    base.update(sovrascritture)
    return base


def test_una_voce_valida_non_ha_problemi():
    assert controlla_voce(voce(it="Il tuo zaino è pieno.")) == []


def test_blocca_la_traduzione_vuota():
    problemi = controlla_voce(voce(it=""))
    assert any("vuota" in p for p in problemi)


def test_blocca_la_traduzione_identica_all_inglese():
    problemi = controlla_voce(voce(it="Your inventory is full."))
    assert any("identica" in p for p in problemi)


def test_blocca_l_apostrofo_scritto_a_mano():
    problemi = controlla_voce(voce(it="Il tuo zaino e' pieno."))
    assert any("apostrofo" in p for p in problemi)


def test_blocca_i_caratteri_che_cp932_cancellerebbe():
    problemi = controlla_voce(voce(it="Zaino pieno — davvero"))  # trattino lungo
    assert any("cp932" in p.lower() for p in problemi)


def test_le_dinamiche_devono_conservare_le_stesse_chiamate():
    pulita = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='name(tc) + " ha protetto " + name(x) + "."',
    )
    assert controlla_voce(pulita) == []

    rotta = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='"ha protetto"',
    )
    problemi = controlla_voce(rotta)
    assert any("interpolazion" in p for p in problemi)


def test_blocca_la_virgoletta_doppia_nuda_nelle_statiche():
    problemi = controlla_voce(voce(it='Ha detto "ciao".'))
    assert any("nuda" in p for p in problemi)


def test_non_blocca_la_virgoletta_doppia_nelle_dinamiche():
    pulita = voce(
        tipo="dinamica",
        en=" guarded .",
        en_grezzo='name(tc) + " guarded " + name(x) + "."',
        it='name(tc) + " ha protetto " + name(x) + "."',
    )
    problemi = controlla_voce(pulita)
    assert not any("virgolette" in p for p in problemi)


def test_la_virgoletta_protetta_passa_nelle_statiche():
    # e' la forma che usa l'inglese upstream (text.hsp:9879, \"Project LF\"):
    # applica.py avvolge la statica fra virgolette, ma HSP conosce l'escape.
    assert controlla_voce(voce(it='Ha detto \\"ciao\\".')) == []


def test_le_virgolette_tipografiche_ora_sono_bloccate():
    # ROVESCIA una decisione precedente, e la rovescia una misura: “” CP932 le
    # codifica (quindi `non_ascii_residuo` le lasciava passare) ma su DUE byte,
    # e la build inglese disegna un glifo per byte. Vedi doppi_byte_cp932().
    problemi = controlla_voce(voce(it="Ha detto “ciao”."))
    assert any("due byte" in p for p in problemi)


def test_i_puntini_di_sospensione_giapponesi_sono_bloccati():
    problemi = controlla_voce(voce(it="Aspetta…"))
    assert any("due byte" in p for p in problemi)


def test_i_puntini_ascii_passano():
    assert controlla_voce(voce(it="Aspetta...")) == []


def test_la_nota_musicale_resta_ammessa():
    # unico carattere a due byte che l'inglese upstream si permette, perche'
    # msg_write (init.hsp:1374) lo intercetta e ci disegna un'icona al posto.
    assert controlla_voce(voce(it="*blip♪*")) == []


def test_controlla_lotto_indicizza_per_firma():
    esito = controlla_lotto([voce(firma="uno", it=""), voce(firma="due", it="Zaino pieno.")])
    assert "uno" in esito
    assert "due" not in esito


# --- accessi coerenti (rilievo IMPORTANT 7) ---------------------------------

def test_una_voce_senza_tipo_non_solleva_un_keyerror_nudo():
    # un dizionario ritoccato a mano non deve far esplodere la validazione
    # di un lotto intero con un KeyError senza contesto
    problemi = controlla_voce({"file": "text.hsp", "riga": 42, "en": "Yes", "it": "Sì"})
    assert problemi
    assert "text.hsp:42" in problemi[0]
    assert "tipo" in problemi[0]


def test_un_tipo_non_valido_viene_segnalato_con_file_e_riga():
    problemi = controlla_voce({
        "file": "proc.hsp", "riga": 7, "tipo": "boh",
        "en": "Yes", "en_grezzo": '"Yes"', "it": "Sì",
    })
    assert problemi and "proc.hsp:7" in problemi[0] and "boh" in problemi[0]


# --- morfologia inglese vs contenuto (task 1, Fase 1) -----------------------

def test_togliere_la_morfologia_inglese_non_e_un_problema():
    # _s(tc) e' la desinenza della terza persona inglese: in italiano non
    # esiste. Sul sorgente vero (non sul file di lavoro, che e' un residuo):
    # i sei file di Fase 1 (text, command, action, proc, skill, trait) hanno
    # 1.522 dinamiche in tutto, di cui almeno 477 contengono una chiamata di
    # morfologia inglese pura (_s/_s2/_s3/_s4/is/was/your/your2/have/does/
    # him2/his3/its/its2/yourself) — verificato con
    # `strumenti.estrai.estrai_da_file` su
    # `C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\`. Il conteggio
    # esatto delle sole voci che il difetto rifiutava (serve la traduzione
    # italiana per saperlo, non disponibile in questa cartella) resta da
    # misurare quando il corpus tradotto di Fase 1 sara' pronto.
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": 'name(tc) + " attacca."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert controlla_voce(voce) == []


def test_perdere_una_funzione_di_contenuto_resta_un_problema():
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": '"Attacca."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert any("interpolazioni" in p for p in controlla_voce(voce))


def test_lasciare_la_morfologia_inglese_nell_italiano_e_un_problema():
    # scriverebbe "attacca s" a schermo
    voce = {
        "tipo": "dinamica", "en": " attacks.", "it": 'name(tc) + " attacca" + _s(tc) + "."',
        "en_grezzo": 'name(tc) + " attack" + _s(tc) + "."',
    }
    assert any("morfologia inglese" in p for p in controlla_voce(voce))


def test_un_pronome_con_due_argomenti_va_conservato_come_contenuto():
    # giro di correzione 1: he/his/him NON sono piu' facoltativi. Con due
    # argomenti passano da lang() (action.hsp:9631, sorgente vero) e vanno
    # trattati come name() o itemname(): perderli e' un problema come
    # perdere qualunque altro contenuto.
    grezzo = 'name(tc) + " changed " + his(tc, 1) + " elemental affinity."'
    conservato = {
        "tipo": "dinamica", "en": " changed  elemental affinity.",
        "it": 'name(tc) + " ha cambiato " + his(tc, 1) + " affinità elementale."',
        "en_grezzo": grezzo,
    }
    perso = {
        "tipo": "dinamica", "en": " changed  elemental affinity.",
        "it": 'name(tc) + " ha cambiato la sua affinità elementale."',
        "en_grezzo": grezzo,
    }
    assert controlla_voce(conservato) == []
    assert any("interpolazioni" in p for p in controlla_voce(perso))


def test_un_pronome_con_un_argomento_deve_sparire():
    # command.hsp:6667 (sorgente vero) — his(tc) non ha mai un ramo lang()
    # raggiungibile: se resta nell'italiano scrive "his"/"her" per sempre,
    # esattamente come _s(tc) scriverebbe "s"
    grezzo = 'name(tc) + " puffs out " + his(tc) + " chest with pride."'
    corretto = {
        "tipo": "dinamica", "en": " puffs out  chest with pride.",
        "it": 'name(tc) + " gonfia il petto con orgoglio."', "en_grezzo": grezzo,
    }
    lasciato = {
        "tipo": "dinamica", "en": " puffs out  chest with pride.",
        "it": 'name(tc) + " gonfia " + his(tc) + " petto con orgoglio."',
        "en_grezzo": grezzo,
    }
    assert controlla_voce(corretto) == []
    assert any("morfologia inglese" in p for p in controlla_voce(lasciato))


def test_una_stringa_negli_invariati_non_e_segnalata():
    v = voce(en="Vernis", en_grezzo='"Vernis"', it="Vernis")
    assert controlla_voce(v, invariati={"Vernis"}) == []


def test_senza_gli_invariati_resta_segnalata():
    v = voce(en="Vernis", en_grezzo='"Vernis"', it="Vernis")
    assert any("identica all'inglese" in p for p in controlla_voce(v))


def test_l_invariato_copre_la_stringa_intera_non_la_parola():
    # "Vernis" invariato non deve zittire una frase che lo contiene: quella
    # frase e' rimasta inglese, ed e' proprio cio' che la regola cerca
    v = voce(en="You arrive at Vernis.", en_grezzo='"You arrive at Vernis."',
             it="You arrive at Vernis.")
    assert any("identica all'inglese" in p for p in controlla_voce(v, invariati={"Vernis"}))


def test_carica_invariati_legge_la_tabella(tmp_path):
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "# Invariati\n\n| valore | motivo |\n|---|---|\n"
        "| Vernis | nome proprio |\n| Karma | termine acquisito |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"Vernis", "Karma"}


def test_carica_invariati_ignora_l_intestazione_e_i_separatori(tmp_path):
    percorso = tmp_path / "invariati.md"
    percorso.write_text("| valore | motivo |\n|---|---|\n| Vernis | x |\n", encoding="utf-8")
    assert carica_invariati(percorso) == {"Vernis"}


def test_carica_invariati_si_ferma_alla_prima_sezione(tmp_path):
    # il file vero ha una seconda tabella, "Da decidere nel glossario", che
    # elenca i candidati NON ancora accettati: leggerla li renderebbe
    # invariati di fatto, cioe' l'esatto contrario di cio' che dichiara
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n| Vernis | nome proprio |\n"
        "\n## Da decidere nel glossario\n\n"
        "| valore | occorrenze | nota |\n|---|---|---|\n| Larna | 3 | citta' |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"Vernis"}


def test_senza_il_file_non_si_rompe_niente(tmp_path):
    assert carica_invariati(tmp_path / "assente.md") == set()


def test_carica_i_valori_di_dato_che_stanno_dopo_la_prima_sezione(tmp_path):
    # il difetto del 2026-08-07: la sezione dei valori di dato fu inserita
    # DOPO il primo `##`, e la lettura si fermava li'. Le otto stringhe che
    # devono restare inglesi per non rompere i salvataggi non arrivavano a
    # `controlla_voce`, e un lotto che le lasciava inglesi -- cioe' corretto --
    # veniva rifiutato intero per "traduzione identica all'inglese"
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n| Vernis | nome proprio |\n"
        "\n## Valori di dato, non testo\n\n"
        "| valore | motivo |\n|---|---|\n| male | valore di CDATAN_NEWSEX |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"Vernis", "male"}


def test_una_sezione_non_classificata_si_fa_sentire(tmp_path):
    # il cuore della correzione: il modo in cui il difetto e' nato non deve
    # poter succedere di nuovo. Chi aggiunge una sezione la classifica, oppure
    # rompe. Il silenzio non e' fra le possibilita'
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n| Vernis | nome proprio |\n"
        "\n## Una sezione che nessuno ha classificato\n\n"
        "| valore | motivo |\n|---|---|\n| Qualcosa | boh |\n",
        encoding="utf-8",
    )
    try:
        carica_invariati(percorso)
    except ValueError as errore:
        assert "Una sezione che nessuno ha classificato" in str(errore)
    else:
        raise AssertionError("una sezione non classificata deve alzare ValueError")


def test_una_sezione_senza_tabella_non_va_classificata(tmp_path):
    # solo le sezioni che portano una tabella sono una decisione da prendere:
    # una sezione di sola prosa non ha valori, quindi non ha nulla da dire
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n| Vernis | nome proprio |\n"
        "\n## Note\n\nSolo prosa, nessun valore.\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"Vernis"}


def test_il_file_vero_ha_tutte_le_sezioni_classificate():
    # la rete di sicurezza vera: gira sul file del progetto, non su un
    # tmp_path costruito ad arte. Se domani qualcuno aggiunge una sezione a
    # `invariati.md` senza dire da che parte sta, questo test lo dice subito
    carica_invariati()


def test_il_file_vero_protegge_le_stringhe_che_sono_dati():
    caricati = carica_invariati()
    for valore in ("male", "female", "hermaphrodite", "trans-female"):
        assert valore in caricati, f"{valore} deve restare inglese e non essere sollecitato"


def test_un_lotto_che_lascia_inglesi_i_valori_di_dato_passa():
    # la conseguenza vera del difetto, che nessun test copriva: `controlla_voce`
    # non riceveva `male`, quindi la voce corretta -- lasciata inglese, come
    # `invariati.md` prescrive -- inciampava in "traduzione identica
    # all'inglese", e `controlla_lotto` rifiutava il lotto INTERO. L'unico modo
    # di farlo passare era tradurla, cioe' rompere il genere dei personaggi
    # gia' creati in ogni salvataggio esistente
    voci = [voce(firma=f"sex{i}", file="init.hsp", en=valore,
                 en_grezzo=f'"{valore}"', jp=valore, jp_grezzo=f'"{valore}"', it=valore)
            for i, valore in enumerate(("male", "female", "none", "hermaphrodite",
                                        "male?", "female?", "trans-male", "trans-female"))]
    assert controlla_lotto(voci) == {}


def test_il_file_vero_del_progetto_si_legge():
    # l'esclusione dei "Da decidere" e' coperta, sul meccanismo, dal test su
    # tmp_path qui sopra, che non invecchia. Qui si verifica solo che il file
    # vero si legga e porti le decisioni prese: `Larna` stava fra i da
    # decidere fino al 2026-08-07, poi e' stato deciso invariato, e
    # l'asserzione che lo escludeva e' invecchiata insieme alla decisione.
    caricati = carica_invariati()
    assert "Vernis" in caricati
    assert "Larna" in caricati


def test_controlla_lotto_propaga_gli_invariati_a_tutte_le_voci():
    voci = [voce(firma=f"f{i}", en="Vernis", en_grezzo='"Vernis"', it="Vernis")
            for i in range(3)]
    assert controlla_lotto(voci, invariati={"Vernis"}) == {}
    assert len(controlla_lotto(voci, invariati=set())) == 3


# --- il plurale dei nomi (buco chiuso il 2026-08-07) -------------------------
#
# Le voci dei nomi di `db_item.hsp` portano quattro campi in piu' -- `plurale`,
# `genere`, `array`, `oggetto` -- e fino a qui `verifica.py` non ne guardava nessuno. Un
# lotto con `it` pieno e `plurale` vuoto passava senza un fiato: il gioco
# ripiegava sul singolare («2 spada lunga») e nessuno lo sapeva finche' non lo
# vedeva a schermo. E' lo stesso difetto di forma gia' corretto due volte in
# questo progetto: una difesa che non copre un campo nuovo tace invece di
# parlare.

def nome(**sovrascritture):
    """Una voce dei nomi: quella che `estrai` emette per `db_item.hsp`."""
    base = voce(
        file="db_item.hsp", riga=1200,
        jp="ロングソード", jp_grezzo='"ロングソード"',
        en="long sword", en_grezzo='"long sword"',
        it="spada lunga", plurale="spade lunghe", genere="f",
        array="ioriginalnameref", oggetto="ITEM_ID_LONG_SWORD",
    )
    base.update(sovrascritture)
    return base


def test_un_nome_col_suo_plurale_non_ha_problemi():
    assert controlla_voce(nome()) == []


def test_un_nome_tradotto_senza_plurale_e_un_problema():
    # il buco vero: `it` pieno, `plurale` vuoto, e il lotto passava
    problemi = controlla_voce(nome(plurale=""))
    assert any("plurale" in p for p in problemi)


def test_un_plurale_di_soli_spazi_non_e_un_plurale():
    assert any("plurale" in p for p in controlla_voce(nome(plurale="   ")))


def test_un_nome_non_ancora_tradotto_non_reclama_il_plurale():
    # `it` vuoto significa "non ancora tradotta": il problema e' gia' la
    # traduzione mancante, e chiedere anche il plurale sarebbe rumore
    problemi = controlla_voce(nome(it="", plurale=""))
    assert any("vuota" in p for p in problemi)
    assert not any("plurale" in p for p in problemi)


def test_un_nome_lasciato_inglese_deve_comunque_dichiarare_il_plurale():
    # il pluralizzatore inglese e' spento da una toppa: se il nome resta
    # inglese il suo plurale non lo fa piu' nessuno. Una coincidenza fra
    # singolare e plurale si dichiara, non si deduce -- e' la stessa regola
    # per cui il plurale e' un dato e non una funzione
    v = nome(en="putit", en_grezzo='"putit"', it="putit", plurale="")
    assert any("plurale" in p for p in controlla_voce(v, invariati={"putit"}))
    assert controlla_voce(nome(en="putit", en_grezzo='"putit"', it="putit",
                               plurale="putit"), invariati={"putit"}) == []


def test_una_voce_che_non_e_un_nome_non_deve_portare_il_plurale():
    # la regola non deve straripare sulle 27.813 voci di `lang()`, dove il
    # plurale -- quando serve -- sta gia' dentro la stringa
    assert controlla_voce(voce(it="Il tuo zaino è pieno.")) == []


def test_mezzo_nome_e_una_voce_rotta():
    # `array` e `oggetto` dicono a `applica.py` dove scrivere la riga gemella:
    # una voce che porta il plurale senza di loro e' stata ritoccata a mano, e
    # va detto invece di lasciarla passare
    v = nome()
    del v["array"]
    problemi = controlla_voce(v)
    assert problemi and "db_item.hsp:1200" in problemi[0] and "array" in problemi[0]


def test_il_plurale_finisce_in_una_stringa_hsp_come_il_singolare():
    # `applica_dati_nome` scrive ioriginalnamerefplur(...) = "<plurale>": una
    # virgoletta doppia chiude la stringa in anticipo, esattamente come nel
    # singolare, e il sorgente non compila piu'
    assert any("plurale" in p for p in controlla_voce(nome(plurale='spade "lunghe"')))


def test_il_plurale_passa_dal_controllo_di_cp932():
    assert any("plurale" in p and "CP932" in p
               for p in controlla_voce(nome(plurale="spade — lunghe")))


def test_l_apostrofo_scritto_a_mano_nel_plurale_si_vede():
    # nel dizionario va l'accento vero: la degradazione la fa applica.py, sul
    # plurale come sul singolare
    assert any("plurale" in p and "apostrofo" in p
               for p in controlla_voce(nome(it="città", plurale="citta'")))


def test_controlla_lotto_ferma_il_lotto_dei_nomi_senza_plurale():
    # la conseguenza che conta: `reimporta` chiama `controlla_lotto`, quindi un
    # lotto di nomi a meta' non entra nel dizionario
    voci = [nome(firma="a"), nome(firma="b", plurale="")]
    esito = controlla_lotto(voci, invariati=set())
    assert "a" not in esito
    assert any("plurale" in p for p in esito["b"])


def _prepara(tmp_path, monkeypatch, sorgente_hsp: dict, dizionario_jsonl: dict):
    """Un sorgente e un dizionario finti, montati al posto di quelli veri."""
    sorgente = tmp_path / "sorgente"
    sorgente.mkdir()
    for nome, testo in sorgente_hsp.items():
        (sorgente / nome).write_bytes(testo.encode("cp932"))
    diz = tmp_path / "diz"
    diz.mkdir()
    for nome, voci in dizionario_jsonl.items():
        (diz / nome).write_text(
            "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in voci),
            encoding="utf-8",
        )
    monkeypatch.setattr(percorsi, "SORGENTE_HSP", sorgente)
    monkeypatch.setattr(percorsi, "DIZIONARIO", diz)
    return sorgente, diz


RIGA = '\ttxt lang("jp", "Ciao.")\r\n'


def test_una_firma_sparita_dal_sorgente_finisce_in_coda(tmp_path, monkeypatch):
    _prepara(
        tmp_path, monkeypatch,
        {"text.hsp": RIGA},
        {"text.hsp.jsonl": [{"firma": "sparita", "jp": "vecchio", "en": "Old.",
                             "it": "Vecchio.", "tipo": "statica",
                             "en_grezzo": '"Old."', "riga": 1, "occorrenza": 0}]},
    )
    orfane, non_tradotte = confronta_col_sorgente("text.hsp")
    assert [v["firma"] for v in orfane] == ["sparita"]
    assert non_tradotte == 1


def test_un_dizionario_allineato_non_ha_coda(tmp_path, monkeypatch):
    voci = estrai_da_testo("text.hsp", RIGA)
    _prepara(tmp_path, monkeypatch, {"text.hsp": RIGA},
             {"text.hsp.jsonl": [{**voci[0], "it": "Salve."}]})
    orfane, non_tradotte = confronta_col_sorgente("text.hsp")
    assert orfane == []
    assert non_tradotte == 0


def test_una_voce_senza_traduzione_non_e_una_orfana(tmp_path, monkeypatch):
    # "it" vuoto significa "non ancora tradotta", non "da ritradurre": non c'e'
    # nessun lavoro da rifare, e metterla in coda gonfierebbe il numero che
    # decide se la catena si ferma
    _prepara(
        tmp_path, monkeypatch,
        {"text.hsp": RIGA},
        {"text.hsp.jsonl": [{"firma": "sparita", "en": "Old.", "it": "",
                             "tipo": "statica", "en_grezzo": '"Old."', "riga": 1}]},
    )
    orfane, non_tradotte = confronta_col_sorgente("text.hsp")
    assert orfane == []
    assert non_tradotte == 1


def test_un_file_sparito_a_monte_manda_in_coda_tutte_le_sue_voci(tmp_path, monkeypatch):
    # il caso che SPEC 3.1 contempla e che un read_bytes nudo trasformerebbe in
    # FileNotFoundError a meta' scansione: upstream ha rimosso il .hsp, quindi
    # nessuna delle sue traduzioni ha piu' un sito
    _prepara(
        tmp_path, monkeypatch,
        {"text.hsp": RIGA},
        {"rimosso.hsp.jsonl": [{"firma": "a", "en": "Old.", "it": "Vecchio.",
                                "tipo": "statica", "en_grezzo": '"Old."', "riga": 1}]},
    )
    orfane, non_tradotte = confronta_col_sorgente("rimosso.hsp")
    assert [v["firma"] for v in orfane] == ["a"]
    assert non_tradotte == 0


def test_le_orfane_escono_ordinate_per_riga(tmp_path, monkeypatch):
    _prepara(
        tmp_path, monkeypatch,
        {"text.hsp": RIGA},
        {"text.hsp.jsonl": [
            {"firma": "b", "en": "B", "it": "B.", "tipo": "statica", "en_grezzo": '"B"', "riga": 90},
            {"firma": "a", "en": "A", "it": "A.", "tipo": "statica", "en_grezzo": '"A"', "riga": 7},
        ]},
    )
    orfane, _ = confronta_col_sorgente("text.hsp")
    assert [v["firma"] for v in orfane] == ["a", "b"]


def test_un_invariato_fra_apici_inversi_conserva_gli_spazi(tmp_path):
    # text.hsp:62 allinea le sigle delle statistiche con uno spazio iniziale:
    # lang("感覚", " PER"). La sigla italiana e' " PER" identica, ed e' una
    # coincidenza legittima, non una traduzione dimenticata. Ma la cella di una
    # tabella markdown si legge con strip(), e lo spazio non e' esprimibile:
    # gli apici inversi lo proteggono, e sono gia' la convenzione del progetto
    # per il codice dentro la prosa
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n"
        "| ` PER` | sigla di Percezione, con lo spazio di allineamento |\n"
        "| MAG | sigla di Magia, identica in italiano |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {" PER", "MAG"}


def test_gli_apici_inversi_non_si_mangiano_il_contenuto(tmp_path):
    # un valore che contiene davvero un apice inverso non deve sparire
    percorso = tmp_path / "invariati.md"
    percorso.write_text(
        "| valore | motivo |\n|---|---|\n| `a`b` | strano ma legittimo |\n",
        encoding="utf-8",
    )
    assert carica_invariati(percorso) == {"a`b"}


def test_un_invariato_fatto_di_spazi_non_e_una_traduzione_vuota():
    # text.hsp:198 e' strblank = lang("", " "): uno spazio di RIEMPIMENTO, non
    # testo. La regola "traduzione vuota" scattava prima di quella sugli
    # invariati, quindi un invariato fatto di soli spazi era irraggiungibile
    # per costruzione: nessun valore lo faceva passare, nemmeno quello giusto
    v = voce(en=" ", en_grezzo='" "', jp="", jp_grezzo='""', it=" ")
    assert controlla_voce(v, invariati={" "}) == []


def test_una_traduzione_vuota_resta_un_problema_se_non_e_invariata():
    # la regola serve ancora: quasi sempre una traduzione vuota e' una riga
    # dimenticata, ed e' proprio cio' che deve continuare a fermare il lotto
    assert any("vuota" in p for p in controlla_voce(voce(it="   "), invariati={" "}))
    assert any("vuota" in p for p in controlla_voce(voce(it="")))


# ---------------------------------------------------------------------------
# Il genere, secondo dato dei nomi. Stessa natura del plurale e stesso momento
# buono per scriverlo: quello in cui qualcuno sta guardando quel nome.
# ---------------------------------------------------------------------------

def test_un_nome_senza_genere_e_un_problema():
    problemi = controlla_voce(nome(genere=""))
    assert any("genere" in p for p in problemi)


def test_un_genere_inventato_non_passa():
    problemi = controlla_voce(nome(genere="maschile"))
    assert any("genere" in p for p in problemi)


def test_i_quattro_generi_validi_passano():
    for genere in ("m", "f", "mp", "fp"):
        assert controlla_voce(nome(genere=genere)) == []


def test_il_genere_non_si_chiede_alle_voci_di_lang():
    """Nessuna `lang()` finisce dietro un articolo scelto dal codice."""
    assert controlla_voce(voce(it="Sei sicuro?")) == []


def test_controlla_lotto_ferma_il_lotto_dei_nomi_senza_genere():
    """La conseguenza che conta: un lotto a meta' non entra nel dizionario."""
    esito = controlla_lotto([nome(firma="a"), nome(firma="b", genere="")],
                            invariati=set())
    assert "a" not in esito
    assert "b" in esito
