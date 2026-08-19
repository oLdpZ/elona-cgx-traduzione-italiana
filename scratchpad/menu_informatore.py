# -*- coding: utf-8 -*-
"""Quante voci del menu dell'informatore sui boss stanno a schermo INSIEME?

La domanda non e' oziosa. `chat.hsp:25166` taglia le voci di `chatList` a **24
caratteri** — duro, con `strmid` — ma solo quando `keyrange > 10`, cioe' quando
il menu passa a due colonne. La memoria del progetto segnala quel taglio dalla
55a come «mai collaudato», e il menu dell'informatore (`chat.hsp:24239`-`:24319`)
e' il piu' grande del gioco: **ventisei** `chatList` dichiarate.

Ventisei dichiarate non vuol dire ventisei a schermo: ogni voce e' guardata da un
intervallo di `GDATA_FLAG_MAIN`, cioe' dal punto della trama in cui si e'
arrivati. Questo referto prende gli intervalli dal sorgente (letti a mano, la
riga e' accanto a ciascuno) e cerca il valore di `GDATA_FLAG_MAIN` che ne accende
di piu'.

I sotto-flag (`GDATA_FLAG_MAIN_SAGE`, `..._KING`, `..._FOOL`,
`GDATA_FLAG_SUB_REGULUS_*`, `..._ASSASSIN_EVENTS_*`) sono messi tutti a zero:
e' il caso **peggiore**, quello che accende il massimo di voci.

Esito: **sei**, a `GDATA_FLAG_MAIN = 135`. Il taglio a 24 non scatta mai qui, e
vale il tetto ordinario della rete 15 (58 caratteri), che `menu_dialogo.py`
controlla da se'.
"""

# (nome, riga di chat.hsp, minimo incluso, massimo escluso) di GDATA_FLAG_MAIN
VOCI = [
    ("Cancel",             24239,   0, 10 ** 9),   # nessuna condizione
    ("Torre Rovente",      24241,   0, 180),
    ("Castello Antico",    24244,   0, 180),
    ("grotta dei morti",   24247,   0, 180),
    ("Lesimas 1",          24251,   0, 136),       # <= 135
    ("Lesimas 2",          24256, 135, 141),       # >= 135 & <= 140
    ("Lesimas 3",          24261, 140, 151),       # >= 140 & <= 150
    ("Lesimas boss",       24265, 150, 180),
    ("Tempio Caos",        24268, 210, 290),
    ("Fortezza Meccanica", 24271, 210, 290),
    ("Valle degli Inferi", 24274, 210, 290),
    ("Remido 1",           24277, 260, 266),
    ("Remido 2",           24280, 266, 270),
    ("Passo di Montagna",  24283, 295, 320),
    ("Remido boss",        24286, 290, 340),
    ("Culla 1",            24289, 378, 455),
    ("Acque di Valm",      24292, 396, 400),
    ("Zanan",              24295, 404, 440),
    ("Mayroon",            24298, 404, 440),
    ("Eulderna",           24301, 404, 440),
    ("Kikkasu",            24304, 404, 440),
    ("Culla 2",            24307, 455, 480),
    ("Culla 3",            24310, 550, 590),
    ("Culla 4",            24313, 590, 620),
    ("Tezcatlipoca",       24316, 645, 680),
    ("Culla boss",         24319, 680, 760),
]

TAGLIO_DURO = 24     # chat.hsp:25167, strmid(listn(0,cnt), 0, 24)
SOGLIA_COLONNE = 10  # chat.hsp:25166, keyrange > 10


def main():
    peggio, dove, quali = 0, None, []
    for flag in range(0, 800):
        accese = [n for n, _, a, b in VOCI if a <= flag < b]
        if len(accese) > peggio:
            peggio, dove, quali = len(accese), flag, accese
    print("voci dichiarate            : %d" % len(VOCI))
    print("massimo accese insieme     : %d  (GDATA_FLAG_MAIN = %d)" % (peggio, dove))
    print("                             %s" % ", ".join(quali))
    print("soglia delle due colonne   : keyrange > %d" % SOGLIA_COLONNE)
    scatta = peggio > SOGLIA_COLONNE
    print("il taglio a %d caratteri %s" % (TAGLIO_DURO,
          "SCATTA: le rese vanno tenute sotto" if scatta else "NON scatta mai in questo menu"))
    if not scatta:
        print()
        print("=> vale il tetto ordinario della rete 15 (58), gia' controllato da")
        print("   strumenti/menu_dialogo.py: qui non serve nessun vincolo in piu'.")


if __name__ == "__main__":
    main()
