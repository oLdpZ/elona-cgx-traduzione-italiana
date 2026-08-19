# -*- coding: utf-8 -*-
"""Le toppe a `etc.hsp` che fanno comporre gli epiteti all'italiana.

Il pezzo 2 del piano di `decisioni.md`. Si scrive **prima** del vocabolario,
perche' e' il pezzo che si butta se non regge: nessuno manda in traduzione 950
parole prima di sapere che la macchina che le assembla funziona.

## Che cosa fa upstream (etc.hsp:399-520, ramo non giapponese)

    parola1 = rnlist(rnd(14), riga1)           una colonna qualsiasi
    se parola1 sta nelle colonne 0-1:
        1 su 6  ->  parola1 + " of"
        se no, 1 su 6  ->  "the " + parola1, e finisce
    parola2 = rnlist(rnd(2), riga2)            sempre un sostantivo
    risultato = cnven(parola1) + " " + cnven(parola2)
    se il risultato arriva a 28 caratteri, si rifa' tutto

## Che cosa deve fare in italiano

L'inglese mette il modificatore **prima** della testa, l'italiano **dopo**. La
via che evita l'accordo di genere -- e quindi i «Fata corrotto» -- e' rendere
ogni modificatore come **sintagma preposizionale invariabile**:

    Corrupted Wolf   ->  Lupo della corruzione
    Elegance Fairy   ->  Fata dell'eleganza
    Axe wielding Serpent -> Serpente dell'ascia
    Dusk of Copper   ->  Crepuscolo di rame

Cosi' la testa resta la parola2 (forma nuda) e il modificatore e' la parola1
(forma preposizionale), **sempre**: le tre forme inglesi -- «A B», «A of B»,
«the A» -- collassano in una sola, e non serve nessun ramo.

## Perche' due file invece di un campo composto

Ogni parola serve in due forme (nuda come testa, preposizionale come
modificatore) e HSP non ha una funzione comoda per spezzare una stringa su un
separatore. La via che non chiede nessun parsing e' **due tabelle parallele**,
stessa griglia, caricate con lo stesso identico blocco:

    data\\ndata-i.csv    le forme nude          «lupo», «eleganza», «rame»
    data\\ndata-i2.csv   le preposizionali      «del lupo», «dell'eleganza», «di rame»

⚠️ E i file **si aggiungono** all'installazione, non sostituiscono
`ndata-e.csv`: l'originale del gioco resta intatto, come `cgx-test.exe` non
sovrascrive `elonapluscgx.exe`.

## Le cinque toppe

1. `*random_titleInit` carica `ndata-i.csv` invece di `ndata-e.csv` e, subito
   dopo, `ndata-i2.csv` in `rnlist2`.
2. `rnd(14)` -> `rnd(14 - en * 4)`: nel nostro CSV le colonne 10-13 restano
   vuote, e il ramo giapponese non cambia. Lo stile `- en * n` e' quello che il
   sorgente usa dappertutto.
3. La colonna della prima parola si salva prima che il `repeat 100` la
   sovrascriva.
4. Il blocco `else` non aggiunge piu' ne' « of» ne' «the ».
5. La composizione finale inverte l'ordine e pesca il modificatore da `rnlist2`.
   E il tetto passa da 28 a 36 caratteri, che la finestra regge: e' larga 400
   col testo a `wx + 64`, cioe' 45 caratteri a 7 px.

⚠️ **La prova si fa sull'inglese**, come vuole la 61a: con i due CSV riempiti
con le parole inglesi di monte, la toppa deve produrre epiteti scomponibili
esattamente come quelli di oggi. Se non sa riprodurre l'inglese, non e' pronta
per l'italiano.
"""
import io
import json
from pathlib import Path

SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\etc.hsp")
USCITA = "lavoro/toppe-etc-epiteti.jsonl"
T = "\t"


def righe(*testi):
    return list(testi)


TOPPE = [
    # 1. i due file
    {
        "cerca": righe(
            T + 'noteload exedir + lang("data\\\\ndata.csv", "data\\\\ndata-e.csv")',
            T + "sdim rnlist, 20, 15, noteinfo(0)",
            T + "repeat noteinfo(0)",
            T * 2 + "noteget msgtemp, cnt",
            T * 2 + "csvsort randn1, msgtemp, 44",
            T * 2 + "cnt2 = cnt",
            T * 2 + "repeat 15",
            T * 3 + "rnlist(cnt, cnt2) = randn1(cnt)",
            T * 2 + "loop",
            T + "loop",
        ),
        "sostituisci": righe(
            T + 'noteload exedir + lang("data\\\\ndata.csv", "data\\\\ndata-i.csv")',
            T + "sdim rnlist, 40, 15, noteinfo(0)",
            T + "repeat noteinfo(0)",
            T * 2 + "noteget msgtemp, cnt",
            T * 2 + "csvsort randn1, msgtemp, 44",
            T * 2 + "cnt2 = cnt",
            T * 2 + "repeat 15",
            T * 3 + "rnlist(cnt, cnt2) = randn1(cnt)",
            T * 2 + "loop",
            T + "loop",
            T + "; TOPPA IT: la seconda tabella, le forme preposizionali",
            T + "notesel titlebuff",
            T + 'noteload exedir + lang("data\\\\ndata.csv", "data\\\\ndata-i2.csv")',
            T + "sdim rnlist2, 40, 15, noteinfo(0)",
            T + "repeat noteinfo(0)",
            T * 2 + "noteget msgtemp, cnt",
            T * 2 + "csvsort randn1, msgtemp, 44",
            T * 2 + "cnt2 = cnt",
            T * 2 + "repeat 15",
            T * 3 + "rnlist2(cnt, cnt2) = randn1(cnt)",
            T * 2 + "loop",
            T + "loop",
        ),
        "motivo": (
            "Epiteti, toppa 1 di 5. Carica il vocabolario italiano e, accanto, la "
            "tabella delle forme preposizionali. Due tabelle parallele invece di un "
            "campo composto perche' HSP non ha un modo comodo di spezzare una stringa "
            "su un separatore: cosi' non serve nessun parsing. `sdim` sale da 20 a 40 "
            "byte perche' le forme italiane sono piu' lunghe (HSP riespande in "
            "assegnazione, ma tanto vale dichiararlo giusto)."
        ),
    },
    # 2. la colonna della prima parola: 0-9 in inglese, 0-13 in giapponese
    {
        "cerca": righe(T * 2 + "locvar_randomname_p(1) = rnd(14)"),
        "sostituisci": righe(
            T * 2 + "locvar_randomname_p(1) = rnd(14 - en * 4)  ; TOPPA IT: 10 colonne piene"
        ),
        "motivo": (
            "Epiteti, toppa 2 di 5. Nel vocabolario italiano le colonne 10-13 restano "
            "vuote come in quello inglese, ma il codice ci pesca dentro e poi scarta: "
            "limitare la scelta alle dieci colonne piene toglie giri a vuoto. La forma "
            "`- en * n` e' quella che il sorgente usa dappertutto, e lascia intatto il "
            "ramo giapponese."
        ),
    },
    # 3. salvare la colonna prima che il repeat 100 la sovrascriva
    {
        "cerca": righe(
            T + "locvar_random_title_rtval = -1",
            T + "repeat 100",
            T * 2 + "locvar_randomname_p(4) = rnd(length2(rnlist))",
        ),
        "sostituisci": righe(
            T + "locvar_random_title_rtval = -1",
            T + "locvar_random_title_col1 = locvar_randomname_p(1)  ; TOPPA IT",
            T + "repeat 100",
            T * 2 + "locvar_randomname_p(4) = rnd(length2(rnlist))",
        ),
        "motivo": (
            "Epiteti, toppa 3 di 5. Il `repeat 100` riusa `p(1)` per la colonna della "
            "SECONDA parola, quindi la colonna della prima va messa da parte prima: "
            "serve alla toppa 5 per pescare il modificatore dalla tabella "
            "preposizionale. `p(2)` invece non viene toccato e resta la riga della "
            "prima parola."
        ),
    },
    # 4. niente piu' « of» ne' «the »
    {
        "cerca": righe(
            T * 2 + "repeat 1",
            T * 3 + "if ( locvar_randomname_p(1) == 0 | locvar_randomname_p(1) == 1 ) {",
            T * 4 + "if ( rnd(6) == 0 ) {",
            T * 5 + 'locvar_random_title_randn2 += " of"',
            T * 4 + "}",
            T * 4 + "else {",
            T * 5 + "if ( rnd(6) == 0 ) {",
            T * 6 + 'locvar_random_title_randn2 = "the " + locvar_random_title_randn2',
            T * 6 + "locvar_random_title_rtval = 1",
            T * 6 + "break",
            T * 5 + "}",
            T * 4 + "}",
            T * 3 + "}",
            T * 3 + 'locvar_random_title_randn2 += " "',
            T * 2 + "loop",
            T * 2 + "locvar_random_title_randn2 = cnven(locvar_random_title_randn2)",
        ),
        "sostituisci": righe(
            T * 2 + "; TOPPA IT: in italiano il modificatore va DOPO la testa e porta",
            T * 2 + "; gia' la sua preposizione, quindi qui non si compone niente: le",
            T * 2 + "; tre forme inglesi (A B / A of B / the A) collassano in una sola,",
            T * 2 + "; che la toppa 5 monta alla fine.",
            T * 2 + "locvar_random_title_randn2 = \"\"",
        ),
        "motivo": (
            "Epiteti, toppa 4 di 5. L'inglese ha tre forme perche' mette il "
            "modificatore prima della testa; l'italiano lo mette dopo e con la "
            "preposizione dentro la parola stessa, quindi le tre forme diventano una. "
            "⚠️ Il ramo `the` spariva comunque: in italiano l'articolo dipende dal "
            "genere e dall'iniziale della parola, che qui non si conoscono."
        ),
    },
    # 5. la composizione finale, e il tetto
    {
        "cerca": righe(
            T + "if ( en ) {",
            T * 2 + "rnlist(locvar_randomname_p(1), locvar_randomname_p(4)) = cnven(rnlist(locvar_randomname_p(1), locvar_randomname_p(4)))",
            T + "}",
            T + "locvar_random_title_randn2 += rnlist(locvar_randomname_p(1), locvar_randomname_p(4))",
            T + "locvar_randomname_s = locvar_random_title_randn2",
            T + "if ( strlen(locvar_randomname_s) >= 28 ) {",
        ),
        "sostituisci": righe(
            T + "if ( en ) {",
            T * 2 + "; TOPPA IT: testa (forma nuda) + modificatore (forma preposizionale)",
            T * 2 + "locvar_random_title_randn2 = cnven(rnlist(locvar_randomname_p(1), locvar_randomname_p(4)))",
            T * 2 + 'locvar_random_title_randn2 += " " + rnlist2(locvar_random_title_col1, locvar_randomname_p(2))',
            T + "}",
            T + "else {",
            T * 2 + "locvar_random_title_randn2 += rnlist(locvar_randomname_p(1), locvar_randomname_p(4))",
            T + "}",
            T + "locvar_randomname_s = locvar_random_title_randn2",
            T + "if ( strlen(locvar_randomname_s) >= 28 + en * 8 ) {",
        ),
        "motivo": (
            "Epiteti, toppa 5 di 5. Monta l'epiteto nell'ordine italiano e alza il "
            "tetto da 28 a 36 caratteri, che la finestra regge: e' larga 400 col testo "
            "a wx+64, cioe' 45 caratteri a 7 px. ⚠️ Sparisce anche l'effetto "
            "collaterale di monte, che scriveva la parola capitalizzata DENTRO la "
            "tabella (`rnlist(...) = cnven(rnlist(...))`): la maiuscola adesso si "
            "applica alla copia, non al vocabolario."
        ),
    },
]


def main():
    testo = SORGENTE.read_text(encoding="cp932")
    guai = []
    for n, t in enumerate(TOPPE, 1):
        blocco = "\n".join(t["cerca"]) + "\n"
        quante = testo.count(blocco)
        print(f"toppa {n}: {quante} occorrenze, {len(t['cerca'])} righe")
        if quante != 1:
            guai.append(f"la toppa {n} trova {quante} occorrenze")
            for r in t["cerca"][:3]:
                print(f"    cerca: {r!r}")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("non scrivo niente")

    fuori = "".join(
        json.dumps({"file": "etc.hsp", **t}, ensure_ascii=False) + "\n" for t in TOPPE
    )
    io.open(USCITA, "w", encoding="utf-8", newline="").write(fuori)
    print(f"\n{len(TOPPE)} toppe in {USCITA}")


if __name__ == "__main__":
    main()
