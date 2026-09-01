# -*- coding: utf-8 -*-
"""Le rese del lotto 072 — LE MUNIZIONI: `FILTER_AMMO` si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 072 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa072.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Forma, da `_forma.py 072`: **5 su 5** con lo spazio prima del `\\n`,
**5 su 5** con lo spazio dopo il `#`. Tutte sotto lo stesso titolo.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 072`: **+5** per 5 rese,
nessuna gemella. ⓘ `_gia-reso 072`: 0 su 5. `_122-sorelle-per-frase 072`: 0.
`_119-togli-rinviate 072`: nessuna rinviata.

⚠️⚠️⚠️ **L'INGLESE DI `:98725` E' ROTTO.** Dice «A thin rod-shaped **arrowhead**
with a square **arrowhead**»: 矢弾 (il dardo) e 矢じり (la punta) sono diventati
la stessa parola, e la frase si mangia la coda. Il giapponese e' chiaro — «un
dardo sottile a forma d'asta, con la punta quadrata» — e la resa viene da li'.

⚠️⚠️ **`機械弓` E' RESO IN DUE MODI NEL DIZIONARIO**, e qui vince «balestra»:
quattro voci su sei dicono balestra, fra cui il **nome dell'oggetto** e
l'**indice 3 di questa stessa voce**. Le altre due — due indici 3 di pezzi
unici — dicono «arco meccanico». La divergenza e' vera e va sistemata a parte,
non dentro questo lotto.

⭐ 加工 torna due volte e resta **«lavorato»**, la stessa scelta del lotto 070:
la cosa e' materia prima che diventa altro.
"""

IT = {
    # =====================================================================
    # LE DUE MUNIZIONI DA FUOCO
    # =====================================================================
    # 火薬 -> «polvere da sparo» (dizionario, il barile e il tubo dei fuochi).
    # 反動 -> «contraccolpo» (dizionario, cinque voci sul mana).
    # 威力 -> «potenza» (dizionario). 拳銃 -> «pistola» (dizionario).
    # ⓘ 口径はそのままに e' «a parita' di calibro»: il giapponese mette in
    #   contrasto quel che NON cambia con quel che cambia, e l'italiano ha
    #   la locuzione fatta apposta.
    65947: "Un proiettile che, a parità di calibro, porta molta più polvere da sparo. Anche da una pistola tira fuori una gran potenza, ma il contraccolpo è forte. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐ 加工 -> «lavorato», come nel lotto 070. 高エネルギー体 e' un «corpo ad
    #   alta energia»: il giapponese dice 体, corpo, e il nome dell'oggetto e'
    #   «cella energetica». 銃器 -> «arma da fuoco», come l'indice 3.
    96634: "Un corpo ad alta energia lavorato in proiettile da una tecnica speciale. Per adoperarlo serve un'arma da fuoco apposita. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LE DUE MUNIZIONI DA CORDA
    # =====================================================================
    # ⚠️ Qui l'inglese e' rotto: due volte «arrowhead» per due parole diverse.
    #   矢弾 e' il dardo, 矢じり e' la punta. Il nome dell'oggetto e' «dardi da
    #   balestra», e l'indice 3 dice gia' «insieme a una balestra».
    98725: "Un dardo sottile, a forma d'asta, con la punta quadrata, che si adopera nelle balestre. Pesa, ma è l'unica cosa che in una balestra si possa caricare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ 束ねたもの / 束ねているので: il giapponese ripete il legare, ed e' quello
    #   che spiega il peso. «Un fascio … Essendo in fascio» tiene il legame.
    127062: "Un fascio di frecce da adoperare con l'arco. Essendo in fascio, a seconda del materiale pesano moltissimo, e a portarsele dietro ci vuole attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # E IL PROIETTILE SEMPLICE
    # =====================================================================
    # ⭐ 加工 -> «lavorata», la seconda volta nel lotto. 筒 -> «tubo», dal
    #   dizionario (il tubo dei fuochi d'artificio, 筒).
    # ⓘ どれ程高名な銃であろうと e' concessivo: «per quanto famosa sia».
    126986: "Una piccola sfera lavorata per essere sparata da un'arma da fuoco. Senza di questa, per quanto famosa sia un'arma, non è che un tubo. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
