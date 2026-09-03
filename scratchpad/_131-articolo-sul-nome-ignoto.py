# -*- coding: utf-8 -*-
"""L'articolo che il gioco usa quando l'oggetto NON e' ancora identificato.

## Il difetto, trovato a schermo il 2026-09-03

La schermata «Raccogli» scriveva **«a borraccia filtrante»**: nome italiano,
articolo inglese. E `db_item.hsp` nella build ha la riga giusta —

    ioriginalnamearticolo(ITEM_ID_FILTRATION_BOTTLE) = "una "

Ce l'ha, ed e' corretta. Non viene mai usata. Il blocco che genera
`genera_toppe_nomi.py` in `item_func.hsp` fa cosi':

    if ( locvar_itemname_s8 == "" ) {
        locvar_itemname_s8 = ioriginalnamearticolo(...)      <- "una "
        if ( locvar_itemname_ignoto != "" ) {
            if ( locvar_itemname_s2 == "" ) {
                locvar_itemname_s8 = iknownnamearticolo(...) <- "", e SOVRASCRIVE

Quando l'oggetto e' `ITEM_KNOWN_NONE` l'articolo buono viene **sovrascritto**
da quello del nome ignoto, che per la maggior parte degli oggetti non e' mai
stato assegnato. Vuoto, si cade nel ripiego inglese `"a "`/`"an "`.

## ⚠️ La premessa che il progetto aveva gia' scritto, e che il codice smentiva

`strumenti/estrai.py`, sui 1.321 `iknownnameref` che non sono blocchi:

> 847 rimandano al nome identificato (`= ioriginalnameref(...)`, **e allora
> articolo e plurale di quello vanno bene anche qui**)

E' vero, ed e' esattamente quello che il codice **non** faceva: invece di
tenere l'articolo del nome identificato lo buttava via. La cura non aggiunge un
dato — rende vera una frase gia' scritta, mettendo una guardia sul
sovrascrivere.

## ⚠️⚠️ E la rete c'era, e rispondeva zero

`scratchpad/_83-banco-nome.py` stampa in coda «senza articolo (ripiegherebbero
sull'inglese a/an)». Il 2026-09-03 diceva **0**, mentre il gioco scriveva «a
borraccia filtrante». Il suo ciclo parte da `noti = d["iknownnameref"]`, cioe'
dai soli oggetti che hanno una **voce di dizionario** per quell'array: sono
261. Gli altri 1.050 non entrano nell'insieme, e chi non entra non puo' essere
contato fuori.

> Uno zero misurato sull'insieme sbagliato non e' un dato: e' una spia rotta.
> E' la 109a, e la 130a, da un terzo lato.

Percio' questo referto **non parte dal dizionario**: parte da `db_item.hsp`
nella **build**, cioe' dagli array come li trovera' il gioco, e simula il
blocco di `item_func.hsp` riga per riga. Si misura l'esito, non l'intenzione.

## Le tre famiglie del nome ignoto

    letterale proprio   `iknownnameref(X) = "liuto robusto"`      <- ha il suo articolo
    copia               `iknownnameref(X) = ioriginalnameref(X)`  <- articolo del nome vero
    composto            `iknownnameref(X) = strpotion + strblank + _namepotion(p)`

Sul composto la testa e' la **parola di famiglia** (pozione, grimorio,
pergamena, bacchetta, anello, amuleto), e `genera_toppe_casuali.py` dichiara
nella sua intestazione che l'articolo del nome vero va bene anche li', perche'
la testa del nome vero e' la stessa parola. Questo referto **non ci crede**: lo
verifica oggetto per oggetto, e stampa le divergenze.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_131-articolo-sul-nome-ignoto.py
    ... --elenco     ogni oggetto che ripiega, con nome e famiglia
"""
import io
import re
import sys

from strumenti import percorsi

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

FILE = "db_item.hsp"

# le sei parole di famiglia dei nomi casuali, con l'articolo che pretendono.
# Le rese stanno in `text.hsp:184`-`:189`; qui serve solo il genere della testa,
# che e' fisso per famiglia e non dipende dall'aggettivo che segue.
FAMIGLIE = {
    "stramulet":    ("amuleto",   "un "),
    "strring":      ("anello",    "un "),
    "strpotion":    ("pozione",   "una "),
    "strspellbook": ("grimorio",  "un "),
    "strscroll":    ("pergamena", "una "),
    "strstaff":     ("bacchetta", "una "),
}

_ASSEGNA = re.compile(
    r'^\s*(?P<array>ioriginalnameref|ioriginalnamearticolo|ioriginalnamearticolodet'
    r'|iknownnamearticolo|iknownnamearticolodet)'
    r'\((?P<id>[A-Z0-9_]+)\)\s*=\s*"(?P<valore>(?:[^"\\]|\\.)*)"\s*$')
_COPIA = re.compile(
    r'^\s*iknownnameref\((?P<id>[A-Z0-9_]+)\)\s*=\s*ioriginalnameref\((?P=id)\)\s*$')
# ⚠️ i due addendi non sono simmetrici e nemmeno due `\w+`: uno e' la parola di
# famiglia (`strpotion`), l'altro una CHIAMATA (`_namepotion(p)`). E l'ordine
# cambia fra sorgente e build, perche' `genera_toppe_casuali.py` li scambia:
# qui si accettano tutt'e due gli ordini, e la famiglia si riconosce dal nome.
_COMPOSTO = re.compile(
    r'^\s*iknownnameref\((?P<id>[A-Z0-9_]+)\)\s*=\s*'
    r'(?P<a>\w+(?:\(p\))?) \+ strblank \+ (?P<b>\w+(?:\(p\))?)\s*$')
_LETTERALE = re.compile(
    r'^\s*iknownnameref\((?P<id>[A-Z0-9_]+)\)\s*=\s*"(?P<valore>(?:[^"\\]|\\.)*)"\s*$')


def leggi(cartella):
    """Gli array come li trovera' il gioco, piu' la forma del nome ignoto.

    ⚠️ Si prende l'**ultima** assegnazione di ogni array per ogni oggetto:
    `db_item.hsp` scrive prima il ramo `if ( jp )` e poi il ramo `else`, e a
    contare vale quella che resta. Cosi' il giapponese non inquina il conto.
    """
    valori = {}   # (array, id) -> valore
    ignoto = {}   # id -> ("letterale"|"copia"|"composto", dettaglio)
    testo = (cartella / FILE).read_bytes().decode("cp932", "replace")
    for riga in testo.split("\n"):
        m = _ASSEGNA.match(riga)
        if m:
            valori[(m["array"], m["id"])] = m["valore"]
            continue
        m = _COPIA.match(riga)
        if m:
            ignoto[m["id"]] = ("copia", "")
            continue
        m = _COMPOSTO.match(riga)
        if m:
            # ⚠️ se nessuno dei due addendi e' una famiglia nota il sito NON si
            # butta in silenzio: si tiene con la famiglia vuota, e il referto lo
            # stampa. Una composizione nuova di upstream deve accendere una
            # spia, non sparire dal conto -- e' il modo in cui questo stesso
            # referto ha risposto «composto: 0» al primo giro.
            famiglia = m["a"] if m["a"] in FAMIGLIE else (
                m["b"] if m["b"] in FAMIGLIE else "")
            ignoto[m["id"]] = ("composto", famiglia)
            continue
        m = _LETTERALE.match(riga)
        if m:
            ignoto[m["id"]] = ("letterale", m["valore"])
    return valori, ignoto


GUARDIA = 'if ( iknownnamearticolo(inv(INV_ITEM_ID, itemname_itemid)) != "" ) {'


def guardia_presente(cartella):
    """Vero se `item_func.hsp` scavalca solo quando ha con che scavalcare.

    ⚠️ Non si assume: si legge dalla build. Questo referto ha senso solo se
    riproduce il codice che c'e' davvero — se un giorno la guardia sparisse e
    lui continuasse a contare come se ci fosse, direbbe zero mentre il gioco
    torna a scrivere «a borraccia filtrante». Sarebbe la stessa spia rotta che
    ha reso necessario scriverlo.
    """
    testo = (cartella / "item_func.hsp").read_bytes().decode("cp932", "replace")
    quante = testo.count(GUARDIA)
    if quante > 1:
        raise ValueError(f"la guardia compare {quante} volte in item_func.hsp: "
                         "il blocco dell'articolo dovrebbe essere uno solo")
    return quante == 1


def articolo_usato(oggetto, valori, guardia):
    """Quel che il blocco di `item_func.hsp` mettera' davvero davanti al nome.

    Riproduce le righe che contano, nell'ordine in cui il gioco le esegue:
    l'array del nome identificato e' il default, quello del nome ignoto lo
    scavalca — **sempre** senza la guardia, **solo se pieno** con la guardia.
    La `s2` (parola-contatore) non entra: questo referto guarda il ramo
    `locvar_itemname_s2 == ""`, che e' quello dove la sovrascrittura avviene.
    """
    articolo = valori.get(("ioriginalnamearticolo", oggetto), "")
    scavalco = valori.get(("iknownnamearticolo", oggetto), "")
    if guardia and not scavalco:
        return articolo, articolo
    return scavalco, articolo


def misura(cartella):
    """(ripiegano, divergenti, guardia, per_famiglia, oggetti, ignoto).

    Separata da `main` perche' la prova al contrario deve poterla puntare su un
    albero **guasto apposta**: una rete che si misura solo sulla build vera non
    e' mai stata vista accendersi.
    """
    valori, ignoto = leggi(cartella)
    guardia = guardia_presente(cartella)
    oggetti = sorted(ignoto)
    ripiegano, divergenti, per_famiglia = [], [], {}
    for oggetto in oggetti:
        forma, dettaglio = ignoto[oggetto]
        per_famiglia[forma] = per_famiglia.get(forma, 0) + 1
        usato, articolo = articolo_usato(oggetto, valori, guardia)
        # vuoto vuol dire che il gioco non ha un articolo italiano da mettere,
        # e cade nel ripiego inglese `"a "`/`"an "` di `item_func.hsp`
        if not usato:
            ripiegano.append((forma, dettaglio, oggetto, articolo,
                              valori.get(("ioriginalnameref", oggetto), "")))
        # sul composto l'articolo giusto e' quello della parola di famiglia:
        # si controlla comunque, anche quando non ripiega
        if forma == "composto" and dettaglio in FAMIGLIE:
            parola, atteso = FAMIGLIE[dettaglio]
            effettivo = usato or articolo
            if effettivo != atteso:
                divergenti.append((oggetto, parola, atteso, effettivo))
    return ripiegano, divergenti, guardia, per_famiglia, oggetti, ignoto


def main():
    elenco = "--elenco" in sys.argv
    ripiegano, divergenti, guardia, per_famiglia, oggetti, ignoto = misura(
        percorsi.BUILD_HSP)

    if elenco:
        for forma, dettaglio, oggetto, articolo, nome in ripiegano:
            print("%-10s %-34s %-40s articolo del nome vero: %r"
                  % (forma, oggetto[:34], nome[:40], articolo))
        print()

    for oggetto, parola, atteso, effettivo in divergenti:
        print("DIVERGE   %-34s testa «%s», atteso %r, avrebbe %r"
              % (oggetto, parola, atteso, effettivo))
    if divergenti:
        print()

    senza_articolo_vero = [r for r in ripiegano if not r[3]]
    ignote = [o for o in oggetti
              if ignoto[o][0] == "composto" and not ignoto[o][1]]

    for forma, dettaglio, oggetto, articolo, nome in senza_articolo_vero:
        print("NUDO      %-34s (%s) «%s»" % (oggetto, forma, nome))
    if senza_articolo_vero:
        print()
    for oggetto in ignote:
        print("FAMIGLIA SCONOSCIUTA  %s   ⓘ composizione nuova di monte" % oggetto)
    if ignote:
        print()

    print("guardia sullo scavalco in item_func.hsp     : %s"
          % ("c'e'" if guardia else "NON C'E'   <- lo scavalco e' incondizionato"))
    print("oggetti con un nome NON identificato       : %d" % len(oggetti))
    for forma in ("letterale", "copia", "composto"):
        print("  %-40s: %4d" % (forma, per_famiglia.get(forma, 0)))
    print("di cui l'articolo del nome ignoto ce l'ha  : %d"
          % (len(oggetti) - len(ripiegano)))
    print("RIPIEGANO SULL'INGLESE a/an                : %d" % len(ripiegano))
    print("  di quelli, senza nemmeno l'articolo del")
    print("  nome vero da cui ereditare               : %4d   <- questi non li cura la guardia"
          % len(senza_articolo_vero))
    print("composti con la testa di famiglia sbagliata: %d" % len(divergenti))
    return 1 if (ripiegano or divergenti) else 0


if __name__ == "__main__":
    sys.exit(main())
