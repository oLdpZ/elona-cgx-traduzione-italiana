# -*- coding: utf-8 -*-
"""Impagina un paragrafo italiano in un NUMERO FISSO di righe.

⚠️⚠️ **Perche' il numero di righe non si puo' scegliere.** `dati_applica`
**sostituisce** righe, non ne aggiunge e non ne toglie, e una resa vuota non e'
una riga vuota: e' una voce «da fare», che nella build resta **in inglese**
(`dati_applica.applica_a_testo`, il `continue` sul campo `it`). Quindi un
paragrafo inglese di quattro righe vuole un paragrafo italiano di **quattro
righe**, non tre e non cinque.

⭐ E la larghezza non e' una taglierina ma un **prezzo**: `gmes` manda a capo da
solo a 73 caratteri (`_101-manual-gmes.py`), e ogni a capo costa 16 px
all'altezza della sezione, che ne ha 436. Quindi una riga di 80 caratteri non si
perde — si paga.

Il conto e' quello classico dell'impaginazione: si spezzano le parole in
**esattamente** k righe rendendo minima la riga piu' lunga. Cosi' il testo si
distribuisce da solo invece di ammassarsi in cima e lasciare l'ultima riga con
due parole, che e' quel che fa un `textwrap` qualunque.

    >>> impagina("uno due tre quattro cinque sei", 3)
    ['uno due', 'tre quattro', 'cinque sei']
"""
from __future__ import annotations


def impagina(testo: str, righe: int) -> list[str]:
    """Il testo in **esattamente** `righe` righe, con la piu' lunga piu' corta possibile.

    Solleva se le parole sono meno delle righe: li' non c'e' impaginazione che
    tenga, e vuol dire che la resa e' troppo corta per il posto che deve
    riempire — va allungata, non spezzata.
    """
    parole = testo.split()
    if righe < 1:
        raise ValueError(f"{righe} righe: non ha senso")
    if len(parole) < righe:
        raise ValueError(
            f"{len(parole)} parole in {righe} righe: la resa e' troppo corta "
            f"per il paragrafo che deve riempire ({testo!r})")

    n = len(parole)
    lunghezza = [len(p) for p in parole]
    # somme parziali: la larghezza di parole[i:j] e' pref[j]-pref[i] + (j-i-1)
    pref = [0] * (n + 1)
    for i, l in enumerate(lunghezza):
        pref[i + 1] = pref[i] + l

    def larga(i, j):
        return pref[j] - pref[i] + (j - i - 1)

    # costo(i, k) = la riga piu' lunga impaginando parole[i:] in k righe
    INFINITO = float("inf")
    costo = [[INFINITO] * (righe + 1) for _ in range(n + 1)]
    taglio = [[0] * (righe + 1) for _ in range(n + 1)]
    costo[n][0] = 0
    for i in range(n - 1, -1, -1):
        for k in range(1, righe + 1):
            migliore = INFINITO
            for j in range(i + 1, n - (k - 1) + 1):
                se = max(larga(i, j), costo[j][k - 1])
                if se < migliore:
                    migliore, taglio[i][k] = se, j
            costo[i][k] = migliore

    uscita, i = [], 0
    for k in range(righe, 0, -1):
        j = taglio[i][k]
        uscita.append(" ".join(parole[i:j]))
        i = j
    return uscita


if __name__ == "__main__":
    # la prova al contrario: un testo che sta in due righe, chiesto in tre,
    # non si ammassa — si distribuisce
    assert impagina("uno due tre quattro cinque sei", 3) == \
        ["uno due", "tre quattro", "cinque sei"]
    # ⓘ Di impaginazioni ottime ce n'e' piu' d'una — `a bb / ccc dddd` e
    # `a bb ccc / dddd` costano 8 tutt'e due — quindi si prova il **costo**,
    # non la spezzatura scelta.
    assert max(len(r) for r in impagina("a bb ccc dddd", 2)) == 8
    try:
        impagina("una parola", 3)
    except ValueError as errore:
        assert "troppo corta" in str(errore)
    else:
        raise AssertionError("due parole in tre righe dovevano sollevare")
    print("le tre prove passano")
