# -*- coding: utf-8 -*-
"""La prova al contrario delle due reti dell'articolo, e della toppa del piede.

Prende la build **vera**, sposta di un passo la cosa che tiene chiuso il
cancello, e pretende che il cancello si accenda **nominando il caso**. Non
stampa un ✅: stampa dove si e' acceso e dove no, perche' un esito booleano non
distingue «ho trovato il guasto» da «non l'ho cercato abbastanza».

⚠️ Una delle prove pretende che un cancello **NON** si accenda: rimettere la
guardia dove c'era gia' non deve produrre nulla. Una prova al contrario che sa
dire anche «qui deve restare spento» e' l'unica che protegge da una correzione
esagerata — la lezione della 130a.

⚠️ Non tocca la build vera: copia in una cartella temporanea e guasta li'.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-prova-al-contrario-articolo.py
"""
import importlib.util as _u
import json
import shutil
import sys
import tempfile
from pathlib import Path

from strumenti import percorsi

_QUI = Path(__file__).resolve().parent


def _carica(nome_file, nome):
    spec = _u.spec_from_file_location(nome, str(_QUI / nome_file))
    modulo = _u.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


# ⚠️ Tutt'e due i referti riavvolgono `sys.stdout` in un `TextIOWrapper` appena
# vengono importati, e tutt'e due avvolgono **lo stesso** flusso binario. Il
# primo dei due, appena nessuno lo nomina piu', viene raccolto dal garbage
# collector e chiudendosi **chiude il binario sotto**: la prima `print` di
# questo file moriva con «I/O operation on closed file», con le due reti a posto
# e la prova che non riusciva a dire nulla. Si tengono vivi i wrapper in una
# variabile globale e si riprende lo stdout di partenza.
_ORIGINALE = sys.stdout
IGN = _carica("_131-articolo-sul-nome-ignoto.py", "ign131")
_VIVI = [sys.stdout]
TUT = _carica("_131-quanti-articoli-inglesi.py", "tut131")
_VIVI.append(sys.stdout)
sys.stdout = _ORIGINALE

esiti = []


def pretende(nome, acceso, atteso=True, dettaglio=""):
    ok = (acceso == atteso)
    esiti.append((nome, ok))
    verso = "ACCESO" if acceso else "spento"
    marca = "" if ok else ("  ⚠️⚠️ ATTESO %s" % ("ACCESO" if atteso else "spento"))
    print("%-56s %-7s %s%s" % (nome, verso, dettaglio, marca))


def _scrivi(percorso, testo):
    percorso.write_bytes(testo.encode("cp932", "replace"))


def _leggi(percorso):
    return percorso.read_bytes().decode("cp932", "replace")


def prove_sull_albero():
    with tempfile.TemporaryDirectory(prefix="_131-") as tmp:
        albero = Path(tmp) / "2.05-custom-gx"
        shutil.copytree(percorsi.BUILD_HSP, albero)
        item = albero / "item_func.hsp"
        db = albero / "db_item.hsp"
        item_originale = _leggi(item)
        db_originale = _leggi(db)

        # 0. l'albero intatto: tutt'e due le reti devono stare ferme sui numeri
        #    veri. E' il controllo che dice se le prove che seguono misurano
        #    qualcosa o si accendono da sole.
        ripiegano, divergenti, guardia, _, _, _ = IGN.misura(albero)
        base_ripiegano = len(ripiegano)
        pretende("0. albero intatto: la guardia c'e'", guardia, True)
        pretende("0. albero intatto: divergenze zero", not divergenti, True,
                 "ripiegano %d (i quattro dichiarati)" % base_ripiegano)

        # 1. TOLGO LA GUARDIA. E' la riga nata oggi: senza, lo scavalco torna
        #    incondizionato e gli 847 «copia» ricadono sull'inglese.
        _scrivi(item, item_originale.replace(
            IGN.GUARDIA, 'if ( 1 == 1 ) {'))
        ripiegano, _, guardia, _, _, _ = IGN.misura(albero)
        pretende("1. tolta la guardia dallo scavalco", len(ripiegano) > 800, True,
                 "ripiegano %d (erano %d)" % (len(ripiegano), base_ripiegano))
        pretende("1-bis. e il referto lo DICE, non lo indovina", not guardia, True,
                 "stampa «NON C'E'»")
        _scrivi(item, item_originale)

        # 1-ter. rimessa la guardia, tutto torna com'era: il cancello deve
        #        RESTARE SPENTO. Senza questa, una correzione esagerata (per
        #        esempio togliere del tutto lo scavalco) passerebbe inosservata.
        ripiegano, divergenti, guardia, _, _, _ = IGN.misura(albero)
        pretende("1-ter. rimessa la guardia: nulla si accende",
                 len(ripiegano) != base_ripiegano or bool(divergenti), False,
                 "ripiegano %d" % len(ripiegano))

        # 2. SBAGLIO IL GENERE di una famiglia casuale: «un pozione».
        _scrivi(db, db_originale.replace(
            'iknownnamearticolo(ITEM_ID_POTION_GEM) = "una "',
            'iknownnamearticolo(ITEM_ID_POTION_GEM) = "un "'))
        _, divergenti, _, _, _, _ = IGN.misura(albero)
        pretende("2. articolo sbagliato su una pozione",
                 any(o == "ITEM_ID_POTION_GEM" for o, *_ in divergenti), True,
                 "divergenze %d" % len(divergenti))
        _scrivi(db, db_originale)

        # 3. SVUOTO l'articolo di un composto: con la guardia non ripiega piu'
        #    sull'inglese ma sull'articolo del NOME VERO, che su quell'oggetto
        #    e' di genere sbagliato. E' il difetto dei cinque, rimesso in piedi.
        # ⚠️ si COMMENTA, non si cancella. Il primo tentativo cercava la riga
        # con un «\n» in coda: la build ha fine riga CRLF, il `replace` non
        # trovava niente e la prova restava **spenta**, come se la rete non
        # vedesse il caso. Era la prova a non guastare niente. Un guasto che non
        # guasta e' un successo finto, ed e' proprio la cosa contro cui serve
        # questo file.
        _scrivi(db, db_originale.replace(
            '\tiknownnamearticolo(ITEM_ID_ACIDPROOF_LIQUID) = "una "',
            '\t; iknownnamearticolo(ITEM_ID_ACIDPROOF_LIQUID) = "una "'))
        _, divergenti, _, _, _, _ = IGN.misura(albero)
        pretende("3. tolto l'articolo del composto che divergeva",
                 any(o == "ITEM_ID_ACIDPROOF_LIQUID" for o, *_ in divergenti), True,
                 "torna a «un pozione»")
        _scrivi(db, db_originale)

        # 4. TOLGO l'articolo a un oggetto che ha un nome: e' il buco vero, e
        #    l'altra rete deve chiamarlo SCONOSCIUTO invece di sommarlo.
        _scrivi(db, db_originale.replace(
            '\tioriginalnamearticolo(ITEM_ID_FILTRATION_BOTTLE) = "una "',
            '\t; ioriginalnamearticolo(ITEM_ID_FILTRATION_BOTTLE) = "una "'))
        *_, nuovi, stantii, buchi = TUT.referto(albero)
        pretende("4. tolto l'articolo alla borraccia",
                 "ITEM_ID_FILTRATION_BOTTLE" in nuovi, True,
                 "sconosciuti %d, buchi %d" % (len(nuovi), len(buchi)))
        _scrivi(db, db_originale)

        # 5. DO un articolo a un DICHIARATO: la riga che lo dichiara diventa
        #    una bugia, e il referto deve dirlo invece di tacere.
        _scrivi(db, db_originale.replace(
            'ioriginalnameref2(ITEM_ID_JUICE) = ""',
            'ioriginalnameref2(ITEM_ID_JUICE) = ""\n'
            '\t\tioriginalnamearticolo(ITEM_ID_JUICE) = "un "'))
        *_, nuovi, stantii, buchi = TUT.referto(albero)
        pretende("5. curato un DICHIARATO senza togliere la riga",
                 "ITEM_ID_JUICE" in stantii, True, "stantii %d" % len(stantii))
        _scrivi(db, db_originale)

        # 6. SVUOTO il nome di un oggetto senza dargli un ramo che lo componga:
        #    e' l'orfano, cioe' il caso che nessuno ha previsto.
        _scrivi(db, db_originale.replace(
            'ioriginalnameref(ITEM_ID_FILTRATION_BOTTLE) = "borraccia filtrante"',
            'ioriginalnameref(ITEM_ID_FILTRATION_BOTTLE) = ""'))
        _, _, _, orfani, *_ = TUT.referto(albero)
        pretende("6. nome vuoto senza nessuno che lo componga",
                 "ITEM_ID_FILTRATION_BOTTLE" in orfani, True,
                 "orfani %d" % len(orfani))
        _scrivi(db, db_originale)


def prova_del_piede():
    """La toppa del singolare: c'e' o non c'e', e si legge da `toppe.jsonl`."""
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    toppe = [json.loads(r) for r in
             percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    piedi = [t for t in toppe if t.get("cerca") == '\ts = "" + listmax + " items"']
    pretende("7. le due toppe del piede ci sono", len(piedi) == 2, True,
             "trovate %d" % len(piedi))
    con_singolare = [t for t in piedi
                     if isinstance(t.get("sostituisci"), list)
                     and any('" oggetto"' in r for r in t["sostituisci"])
                     and any("listmax == 1" in r for r in t["sostituisci"])]
    pretende("7-bis. e scelgono fra singolare e plurale",
             len(con_singolare) == 2, True, "col singolare %d" % len(con_singolare))
    # ⚠️ e il plurale non deve essere sparito: «2 oggetto» sarebbe il difetto
    #    speculare, ed e' esattamente quel che produce una correzione frettolosa
    col_plurale = [t for t in piedi
                   if isinstance(t.get("sostituisci"), list)
                   and any('" oggetti"' in r for r in t["sostituisci"])]
    pretende("7-ter. e il plurale e' rimasto", len(col_plurale) == 2, True,
             "col plurale %d" % len(col_plurale))


def main():
    prove_sull_albero()
    prova_del_piede()
    passate = sum(1 for _, ok in esiti if ok)
    print()
    print("prove: %d su %d" % (passate, len(esiti)))
    return 0 if passate == len(esiti) else 1


if __name__ == "__main__":
    sys.exit(main())
