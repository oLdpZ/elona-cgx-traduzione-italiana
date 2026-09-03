# -*- coding: utf-8 -*-
"""Quanti oggetti il gioco presenta ancora con l'articolo inglese `a`/`an`.

Fratello di `_131-articolo-sul-nome-ignoto.py`, e piu' largo di lui: quello
guarda solo lo stato NON IDENTIFICATO, perche' li' stava il difetto della
borraccia. Ma il ripiego inglese di `item_func.hsp` non e' una proprieta' dello
stato: e' quel che succede ogni volta che `locvar_itemname_s8` resta vuoto, e
puo' restare vuoto anche su un oggetto identificato da sempre.

## La quarta famiglia: il nome che `db_item.hsp` non scrive

Per una manciata di oggetti `ioriginalnameref` e' la **stringa vuota** in
tutt'e due i rami di lingua, e il nome lo compone `item_func.hsp` con un `if`
sull'identita' dell'oggetto:

    if ( inv(INV_ITEM_ID, itemowner_itemid) == ITEM_ID_COFFEE ) {
        if ( ibit(ITEM_BIT_ACIDPROOF, itemowner_itemid) == 1 ) {
            locvar_itemowner_s += lang("カフェオーレ", "caffelatte")
        }
        ...

Un nome che non sta nell'array non ha un articolo nell'array: `ioriginalnamearticolo`
e' vuoto per costruzione, e il gioco scrive «a caffe'». ⓘ E' la stessa forma
del pesce, che infatti ha gia' una cura sua (`articolo_del_pesce` in
`genera_toppe_nomi.py`): li' la specie sta in `SUB_NAME` e ha un array
dedicato. Qui il nome sta in un `if`, e non ha nessun array.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-quanti-articoli-inglesi.py
"""
import io
import re
import sys

from strumenti import percorsi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

_NOME = re.compile(
    r'^\s*ioriginalnameref\((?P<id>[A-Z0-9_]+)\)\s*=\s*"(?P<v>(?:[^"\\]|\\.)*)"\s*$')
_ART = re.compile(
    r'^\s*ioriginalnamearticolo\((?P<id>[A-Z0-9_]+)\)\s*=\s*"(?P<v>(?:[^"\\]|\\.)*)"\s*$')
# il ramo di `item_func.hsp` che compone un nome a mano
_COMPONE = re.compile(
    r'inv\(INV_ITEM_ID, itemowner_itemid\) == (?P<id>ITEM_ID_[A-Z0-9_]+)')

# I due che hanno gia' una cura loro, che non passa dall'array del nome.
CURATI_ALTROVE = {
    "ITEM_ID_FISH": "articolo_del_pesce: la specie sta in SUB_NAME e ha "
                    "fishdatanarticolo, un array suo",
    "ITEM_ID_FISH_JUNK": "idem",
}

# ⭐ I quattro che restano, LETTI e DICHIARATI. Come in `strumenti/maiuscole.py`:
# questo referto non chiede che l'elenco sia vuoto, chiede che **non si allunghi
# da solo**. Un oggetto nuovo di monte col nome composto a mano deve comparire
# come SCONOSCIUTO, non sciogliersi in un numero.
#
# Sono quattro e non sei perche' i sei col genere costante li cura
# `genera_toppe_nomi.py` (§12). Questi non hanno un genere costante: la testa
# del sintagma cambia da oggetto a oggetto, quindi l'articolo non e' un dato del
# tipo d'oggetto e non puo' stare in un array indicizzato per ITEM_ID.
DICHIARATI = {
    "ITEM_ID_JUICE":
        "la testa e' il FRUTTO: `iknownnameref(SUB_NAME) + \" \" + mix/milk`, "
        "cioe' il nome di un altro oggetto. Genere variabile",
    "ITEM_ID_NECRO_PARTS":
        "la testa e' la PARTE DEL CORPO (le nove lang() di item_func.hsp:1034, "
        "oggi nel ramo `& jp` -- vedi la 129a), e il nome della creatura segue "
        "dopo « di ». Genere variabile",
    "ITEM_ID_PRODUCED_BOOK":
        "la testa e' il titolo GENERATO dal gioco (`_bookselfs`), diverso a ogni "
        "libro scritto dal giocatore. Genere variabile",
    "ITEM_ID_EVITEM":
        "il nome sta fra parentesi angolari — `\"<\" + evitemn(...)` — ed e' un "
        "nome proprio d'oggetto d'evoluzione. ⓘ Prima di dargli un articolo va "
        "deciso se una marca <> lo vuole: e' la domanda dei nomi in 《》, non "
        "quella dell'articolo",
}


def misura(cartella):
    """(nomi, articoli, composti) letti dall'albero passato.

    Presa a parte da `main` perche' la prova al contrario deve poterla puntare
    su un albero guastato apposta.
    """
    nomi, articoli_ = {}, {}
    testo = (cartella / "db_item.hsp").read_bytes().decode("cp932", "replace")
    for riga in testo.split("\n"):
        m = _NOME.match(riga)
        if m:
            nomi[m["id"]] = m["v"]
            continue
        m = _ART.match(riga)
        if m:
            articoli_[m["id"]] = m["v"]
    funz = (cartella / "item_func.hsp").read_bytes().decode("cp932", "replace")
    return nomi, articoli_, set(_COMPONE.findall(funz))


def referto(cartella, stampa=True):
    nomi, articoli_, composti = misura(cartella)
    vuoti = sorted(k for k, v in nomi.items() if not v)
    senza_articolo = sorted(k for k in nomi if not articoli_.get(k))
    orfani = [k for k in vuoti if k not in composti]
    nuovi = [k for k in senza_articolo
             if k not in CURATI_ALTROVE and k not in DICHIARATI]
    stantii = [k for k in DICHIARATI if k not in senza_articolo]
    buchi = [k for k in senza_articolo if nomi[k]]
    return nomi, senza_articolo, vuoti, orfani, nuovi, stantii, buchi


def main():
    nomi, articoli_, composti = misura(percorsi.BUILD_HSP)

    vuoti = sorted(k for k, v in nomi.items() if not v)
    senza_articolo = sorted(k for k in nomi if not articoli_.get(k))

    print("oggetti con una riga di nome in db_item.hsp : %d" % len(nomi))
    print("  col nome VUOTO (lo compone item_func.hsp) : %d" % len(vuoti))
    print("senza articolo italiano                     : %d" % len(senza_articolo))
    print("  di quelli, col nome vuoto                 : %d"
          % len([k for k in senza_articolo if not nomi[k]]))
    print("  di quelli, con un nome e nessun articolo  : %d   <- questi sarebbero un buco vero"
          % len([k for k in senza_articolo if nomi[k]]))
    print()

    # chi non e' nominato da nessuna parte e' il caso che nessuno ha previsto
    orfani = [k for k in vuoti if k not in composti]
    for k in orfani:
        print("ORFANO    %-34s ⚠️ nome vuoto e NESSUN ramo che lo componga" % k)

    nuovi = [k for k in senza_articolo
             if k not in CURATI_ALTROVE and k not in DICHIARATI]
    for k in nuovi:
        print("SCONOSCIUTO  %-31s «%s»   <- da leggere e dichiarare" % (k, nomi[k]))
    if nuovi:
        print()

    print("CURATI ALTROVE (%d):" % len(CURATI_ALTROVE))
    for k, perche in CURATI_ALTROVE.items():
        print("  %-34s %s" % (k, perche))
    print("DICHIARATI, testa di genere variabile (%d):" % len(DICHIARATI))
    for k, perche in sorted(DICHIARATI.items()):
        stato = "" if k in senza_articolo else "   ⚠️ NON ripiega piu': la riga e' da togliere"
        print("  %-34s %s%s" % (k, perche, stato))
    print()
    print("SCONOSCIUTI da leggere : %d   <- il numero che deve restare a zero"
          % len(nuovi))
    print("orfani                 : %d" % len(orfani))

    # ⚠️ si fallisce anche se un DICHIARATO ha smesso di ripiegare: vorrebbe dire
    # che qualcuno l'ha curato e la riga qui sotto e' diventata una bugia.
    stantii = [k for k in DICHIARATI if k not in senza_articolo]
    for k in stantii:
        print("STANTIO   %-34s ha un articolo: toglilo dai DICHIARATI" % k)
    return 1 if (nuovi or orfani or stantii) else 0


if __name__ == "__main__":
    sys.exit(main())
