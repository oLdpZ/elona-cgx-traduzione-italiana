# -*- coding: utf-8 -*-
"""La prova al contrario delle due reti della 130a.

Prende i **dati veri** e sposta di un passo la cosa che tiene il cancello
chiuso, poi pretende che il cancello si accenda **nominando il caso**. Non
stampa un ✅: stampa dove si e' acceso e dove no, perche' un esito booleano non
distingue «ho trovato il guasto» da «non l'ho cercato abbastanza» — lezione
della 107a, dove la prova al contrario c'era ed era spenta.

⚠️ Non tocca `toppe.jsonl`, non tocca la build vera, non tocca il dizionario:
copia in memoria, o in una cartella di lavoro sotto lo scratchpad.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-prova-al-contrario-reti-toppe.py
"""
import importlib.util as _u
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path

from strumenti import larghezze, percorsi

_QUI = Path(__file__).resolve().parent


def _carica(nome_file, nome):
    spec = _u.spec_from_file_location(nome, str(_QUI / nome_file))
    modulo = _u.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


L = _carica("_130-larghezze-sulla-build.py", "l130")
G = _carica("_130-glossario-nelle-toppe.py", "g130")

esiti = []


def pretende(nome: str, acceso: bool, dettaglio: str = "") -> None:
    esiti.append((nome, acceso, dettaglio))
    print("%-58s %s  %s" % (nome, "ACCESO" if acceso else "spento ⚠️", dettaglio))


# ---------------------------------------------------------------- larghezze
def prova_larghezze() -> None:
    """Cinque guasti, uno per famiglia, iniettati in una copia della build."""
    print("\nLARGHEZZE SULLA BUILD — la rete legge un albero, quindi si copia\n")
    with tempfile.TemporaryDirectory(prefix="_130-") as tmp:
        albero = Path(tmp) / "2.05-custom-gx"
        shutil.copytree(percorsi.BUILD_HSP, albero)

        def misura():
            fuori = []
            for nome, riga, sito, px, espressione, era_lang in L.voci_della_build(albero):
                testo = L._italiano(espressione)
                if testo and len(testo) > larghezze.budget(px):
                    fuori.append((nome, riga, testo))
            return fuori

        base = misura()
        print("   la copia, intatta: %d voci fuori misura (la build vera ne ha "
              "le stesse)\n" % len(base))

        def scrivi(nome_file, numero, nuova):
            percorso = albero / nome_file
            righe = percorso.read_bytes().decode("cp932", "replace").split("\n")
            vecchia = righe[numero - 1]
            righe[numero - 1] = nuova
            percorso.write_bytes("\n".join(righe).encode("cp932", "replace"))
            return vecchia

        def ripristina(nome_file, numero, vecchia):
            percorso = albero / nome_file
            righe = percorso.read_bytes().decode("cp932", "replace").split("\n")
            righe[numero - 1] = vecchia
            percorso.write_bytes("\n".join(righe).encode("cp932", "replace"))

        # 1. una voce di `text.hsp` dentro `lang()` allungata oltre il tetto
        riga_text = next(r for f, r, s, px, e, lang in L.voci_della_build(albero)
                         if f == larghezze.FILE)
        vecchia = scrivi(larghezze.FILE, riga_text,
                         '\ts(cnt) = lang("x", "%s")' % ("a" * 90))
        trovata = [x for x in misura() if x[:2] == (larghezze.FILE, riga_text)]
        pretende("1. voce di text.hsp dentro lang(), allungata",
                 bool(trovata), "%s:%d" % (larghezze.FILE, riga_text))
        ripristina(larghezze.FILE, riga_text, vecchia)

        # 2. la stessa voce SENZA lang(): la forma che solo questa rete vede
        vecchia = scrivi(larghezze.FILE, riga_text, '\ts(cnt) = "%s"' % ("b" * 90))
        trovata = [x for x in misura() if x[:2] == (larghezze.FILE, riga_text)]
        pretende("2. la stessa voce col letterale NUDO (senza lang())",
                 bool(trovata), "la forma che una toppa puo' lasciare")
        ripristina(larghezze.FILE, riga_text, vecchia)

        # 3. una voce della seconda strada, quella dei `promptAdd`
        f2, r2 = next((f, r) for f, r, s, px, e, lang in L.voci_della_build(albero)
                      if f != larghezze.FILE)
        vecchia = scrivi(f2, r2, '\tpromptAdd "%s", "null", 1' % ("c" * 90))
        trovata = [x for x in misura() if x[:2] == (f2, r2)]
        pretende("3. voce della strada promptAdd + *prompt_key",
                 bool(trovata), "%s:%d" % (f2, r2))
        ripristina(f2, r2, vecchia)

        # 4. il valore INTERPOLATO in testa: il caso che sbagliava
        #    (qui il guasto e' l'opposto — si pretende che NON si accenda)
        vecchia = scrivi(larghezze.FILE, riga_text,
                         '\ts(cnt) = mapname(i) + " " + cnvrank(x) + " liv."')
        trovata = [x for x in misura() if x[:2] == (larghezze.FILE, riga_text)]
        pretende("4. dinamica in TESTA: non deve accendersi (era il difetto)",
                 not trovata, "misurata %s"
                 % (L._italiano('mapname(i) + " " + cnvrank(x) + " liv."'),))
        ripristina(larghezze.FILE, riga_text, vecchia)

        # 5. il riquadro che si stringe, a testo fermo
        sito = next(s for f, r, s, px, e, lang in L.voci_della_build(albero)
                    if f != larghezze.FILE and ":" in s)
        nome_sito, riga_pk = sito.rsplit(":", 1)
        percorso = albero / nome_sito
        righe = percorso.read_bytes().decode("cp932", "replace").split("\n")
        indice = None
        for j in range(int(riga_pk) - 2, max(0, int(riga_pk) - 400), -1):
            if larghezze._VAL.match(righe[j]):
                indice = j
                break
        if indice is None:
            pretende("5. riquadro ristretto a testo fermo", False,
                     "non trovato il val = del sito")
        else:
            vecchia = righe[indice]
            campi = larghezze.campi(larghezze._VAL.match(vecchia).group(1))
            campi[2] = " 60"
            scrivi(nome_sito, indice + 1, "\tval = " + ",".join(campi))
            trovata = [x for x in misura() if x[0] == nome_sito]
            pretende("5. riquadro ristretto a testo fermo (280px -> 60px)",
                     bool(trovata), "%s, il val = a riga %d" % (sito, indice + 1))
            ripristina(nome_sito, indice + 1, vecchia)


# ---------------------------------------------------------------- glossario
def prova_glossario() -> None:
    """Quattro guasti sulle coppie vere, senza toccare `toppe.jsonl`."""
    print("\nGLOSSARIO NELLE TOPPE — la rete legge coppie, quindi si copiano\n")
    termini = G.glossario()
    coppie = list(G.coppie_delle_toppe())

    def divergenze(elenco):
        fuori = []
        for dove, inglese, italiano in elenco:
            it_stem = G.degrada(italiano).lower()
            for termine in termini:
                if not G.usato_da_termine(termine, inglese):
                    continue
                if not any(all(s in it_stem for s in stems)
                           for stems in termini[termine]):
                    fuori.append((dove, termine))
        return fuori

    base = divergenze(coppie)
    print("   le coppie vere: %d divergenze\n" % len(base))

    # 1. una resa buona guastata: si toglie il termine giusto dall'italiano
    buona = None
    for dove, inglese, italiano in coppie:
        it_stem = G.degrada(italiano).lower()
        for termine in termini:
            if G.usato_da_termine(termine, inglese) and any(
                    all(s in it_stem for s in stems) for stems in termini[termine]):
                buona = (dove, inglese, italiano, termine)
                break
        if buona:
            break
    if buona:
        dove, inglese, italiano, termine = buona
        stems = sorted(termini[termine])[0]
        guasto = re.sub(r"(?i)%s\w*" % re.escape(stems[0]), "PIPPO", G.degrada(italiano))
        trovata = [d for d in divergenze([(dove, inglese, guasto)]) if d[1] == termine]
        pretende("1. resa buona guastata (il termine sparisce dall'italiano)",
                 bool(trovata), "%s, «%s»" % (dove, termine))
    else:
        pretende("1. resa buona guastata", False, "nessuna resa buona trovata")

    # 2. il termine passa da minuscolo a MAIUSCOLO: la regola del filtro
    minuscolo = None
    for dove, inglese, italiano in coppie:
        it_stem = G.degrada(italiano).lower()
        for termine in termini:
            if re.search(r"\b%s\b" % re.escape(termine), inglese.lower()) \
                    and not G.usato_da_termine(termine, inglese) \
                    and not any(all(s in it_stem for s in stems)
                                for stems in termini[termine]):
                minuscolo = (dove, inglese, italiano, termine)
                break
        if minuscolo:
            break
    if minuscolo:
        dove, inglese, italiano, termine = minuscolo
        alzato = re.sub(r"(?i)\b(%s)\b" % re.escape(termine),
                        lambda m: m.group(1).capitalize(), inglese)
        if alzato.strip().lower().startswith(termine):
            alzato = "The " + alzato
        prima = [d for d in divergenze([(dove, inglese, italiano)]) if d[1] == termine]
        dopo = [d for d in divergenze([(dove, alzato, italiano)]) if d[1] == termine]
        pretende("2. lo stesso termine alzato a maiuscolo: spento -> acceso",
                 not prima and bool(dopo), "%s, «%s»" % (dove, termine))
    else:
        pretende("2. termine minuscolo alzato a maiuscolo", False,
                 "nessun termine minuscolo divergente trovato")

    # 3. a inizio frase la maiuscola non conta
    pretende("3. termine maiuscolo a INIZIO frase: resta spento",
             not G.usato_da_termine("will", "Will you go?")
             and G.usato_da_termine("will", "Your Will is high"),
             "«Will you go?» spento, «Your Will is high» acceso")

    # 4. l'inflessione italiana non e' una divergenza
    finte = [("prova", "Your Level is high", "Il tuo Livello e' alto"),
             ("prova", "Your Level is high", "I tuoi Livelli sono alti")]
    pretende("4. l'inflessione (Livello/Livelli) non boccia",
             not divergenze(finte), "lo stem regge il plurale")


def main() -> int:
    prova_larghezze()
    prova_glossario()
    spenti = [n for n, acceso, _ in esiti if not acceso]
    print("\n%d prove su %d si accendono." % (len(esiti) - len(spenti), len(esiti)))
    if spenti:
        print("⚠️ SPENTE: %s" % "; ".join(spenti))
    return 1 if spenti else 0


if __name__ == "__main__":
    sys.exit(main())
