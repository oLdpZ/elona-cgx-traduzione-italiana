# -*- coding: utf-8 -*-
"""Le rese del lotto 016 (le MERCI DA COMMERCIO, `FILTER_CARGO_TRADE`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 016 scratchpad/lotti-111

**19 righe del sorgente, 18 firme**, e **tre** soli giapponesi distinti. E' la
categoria piu' formulaica dell'indice 3, l'opposto delle armi del lotto 012.

    交易品だ。            16 righe -> Merce da commercio.
    重い交易品だ。         2 righe -> Merce da commercio pesante.
    とても重い交易品だ。   1 riga  -> Merce da commercio molto pesante.

⭐ **交易品 e' gia' «merce da commercio»**: sta nel dizionario come voce sua
(`交易品` -> `merce da commercio`) e nel **manuale**, dove la riga che spiega il
commercio e' gia' resa cosi'. Nessuna scelta da fare: un ritrovamento.

⚠️⚠️ **QUI L'INGLESE DICE DICIANNOVE COSE DIVERSE E IL GIAPPONESE UNA SOLA.**
«It is a cargo of rabbit foot», «of seafood», «of high value children's toys»…
cioe' l'inglese ripete **il nome dell'oggetto**, che nel rapporto di
identificazione sta gia' scritto una riga sopra. Il giapponese dice soltanto
che e' merce da commercio, ed e' l'unica cosa che la descrizione aggiunge.
Si segue il giapponese, e sedici righe prendono la stessa resa.

💡 E' la prova al contrario della regola della 110a: li' l'inglese scioglieva un
termine di gioco in una parola comune e bisognava andare nel codice; qui
l'inglese **aggiunge** e quel che aggiunge e' gia' a schermo.

### ⚠️ La scala del peso, terza volta in tre lotti

    重い        -> pesante          (:91029, :104246)
    とても重い  -> molto pesante    (:103982)
    非常に重い  -> pesantissimo/a   (lotti 014 e 015)

La 110a l'aveva fissata sulle due mitragliatrici (非常に重い «pesantissima»,
とても重い «molto pesante»); da allora regge quattro categorie.

ⓘ **Le firme sono 18 e le righe 19**: `:103916` (il tonno) e `:104048` (il
pesce luna) hanno **lo stesso** giapponese e **lo stesso** inglese («It is a
cargo of seafood»), quindi sono una firma sola che copre due righe.
"""

MERCE = "Merce da commercio."

IT = {
    # === 交易品だ。 — sedici righe, quindici chiavi, una resa
    #     ⚠️ `:104048` NON si dichiara: `_monta.py` si ferma con «c'e' una resa
    #     ma il template non ha quella riga», perche' l'estrazione ancora la
    #     firma alla PRIMA occorrenza e :103916 la copre gia' tutt'e due.
    56270: MERCE,
    56336: MERCE,
    73897: MERCE,
    73963: MERCE,
    86269: MERCE,
    86335: MERCE,
    90963: MERCE,
    103718: MERCE,
    103784: MERCE,
    103850: MERCE,
    103916: MERCE,   # ⚠️ copre anche :104048, che e' la STESSA firma
    104114: MERCE,
    104180: MERCE,
    104312: MERCE,
    104378: MERCE,

    # === 重い交易品だ。
    91029: "Merce da commercio pesante.",
    104246: "Merce da commercio pesante.",

    # === とても重い交易品だ。
    103982: "Merce da commercio molto pesante.",
}
