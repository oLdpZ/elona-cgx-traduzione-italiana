# -*- coding: utf-8 -*-
"""Le rese del lotto 054 — LE ARMI A DISTANZA, seconda meta': la categoria CHIUDE.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 054 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa054.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 054`: **9 righe su 10** hanno lo spazio prima del `\\n`;
l'unica senza e' `:127280`. Tutte e dieci le code hanno lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`: **+10** per 10 rese, nessuna gemella.
`_gia-reso.py 054`: 0 su 10.

⭐⭐ LA SCALA DELL'ATTENUAZIONE COLLA DISTANZA. Sei armi base di questo lotto
dicono, ciascuna a modo suo, quanto la loro forza cali allontanandosi — ed e'
un fatto di gioco, non un ornamento. L'indice 3, gia' reso e chiuso, la porta
per intero, e le rese del corpo ci si appoggiano sopra invece di reinventare
il verbo:

    光子銃    pistola laser    殆どない  -> «con la distanza non cala quasi»
    機関銃    mitragliatrice   少ない    -> «con la distanza cala poco»
    拳銃      pistola          減衰する  -> «con la distanza perde forza»
    散弾銃    fucile a pompa   射程が短い -> «porta poco lontano»

Il corpo dell'arco corto e dell'arco lungo chiude la scala dall'altro capo
(近～中距離 / 中～遠距離). Tutte e sei le rese del corpo usano **calare**, che e'
il verbo dell'indice 3: cambiarlo qui avrebbe spezzato in due il pannello, che
i due indici li disegna uno sotto l'altro.
"""

IT = {
    # =====================================================================
    # LE ARMI DA FUOCO, e la scala dell'attenuazione
    # =====================================================================

    # ⚠️ 超重量装置 e 軽量化に成功 non si contraddicono: l'apparecchio pesa di
    #    suo un'enormita', e nonostante questo sono riusciti ad alleggerirlo.
    #    どちらも sono le DUE tecniche — il meccanismo e la lavorazione — ed
    #    e' per questo che il plurale conta.
    96567: "Un apparecchio pesantissimo, che scaglia materia portata ad altissima velocità. Oltre al meccanismo complicato, lavorando materiali speciali si è riusciti anche ad alleggerirlo. Ma tutt'e due sono ormai tecniche perdute, e produrlo in serie sarebbe impossibile. \\n# ~Dizionario Fantastico di Irva~",

    96710: "Un'arma da fuoco che, caricata con un proiettile speciale, scaglia dal foro di sparo un raggio di luce dotato di massa. A differenza delle altre armi da tiro, che perdono forza a mano a mano che la distanza cresce, questa non cala quasi per niente: un pezzo notevole. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    97803: "Un'arma da fuoco fatta per sparare proiettili che si sparpagliano su un'area larga. Da vicino ha una forza senza pari, ma allontanandosi quella forza cala sempre più in fretta, e va maneggiata con attenzione. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    115796: "Un'arma da fuoco a canna lunga, fatta per sparare di continuo. Per taglia e peso non è arma per tutti, ma anche così, a differenza dell'arco, si può dire che sia molto più facile da manovrare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    127138: "Un'arma da fuoco piccola, che si sente pesante in mano. È progettata perché chiunque la sappia usare, ma con la canna corta che ha la gittata non sarà granché lunga. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # GLI ARCHI E LA BALESTRA
    # =====================================================================

    # 機械弓 e' «balestra» nel dizionario, ma il giapponese di questa riga
    # parla di 弓, l'arco: la resa tiene l'arco, che e' cio' che la riga dice.
    98801: "Un arco pensato per scagliare frecce senza fatica. Il pregio è che lo usa chiunque, senza bisogno di pratica; il rovescio, che preparare la carica costa parecchia forza e parecchio tempo. Insomma, ha un pregio e un difetto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    115872: "Un arco di lunghezza contenuta, messo a punto per la caccia. Usarlo richiede pratica, ma una volta presa la mano può diventare per i cacciatori un amico di cui fidarsi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 森の民: il giapponese abbrevia 異形の森の民, la gente della Foresta
    # Eretica — che e' il nome che il dizionario da' a 異形の森, e che il
    # nome dell'oggetto porta come «Vindale». La resa dice «la foresta»,
    # cosi' il legame regge senza scegliere fra i due nomi.
    117388: "Un arco lungo che si dice racchiuda tutto il sapere della gente della foresta. Pare che ci sia dentro più di un accorgimento perché la preda presa di mira non scappi. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ SENZA spazio prima del `\n`.
    127280: "Un arco che, per allungare la gittata, è cresciuto fino a superare la statura di un uomo. Già così arriva abbastanza lontano, ma dandogli l'angolo giusto si dice che possa colpire il nemico da distanze lunghissime.\\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I SASSI
    # =====================================================================

    # こけおどし e' lo spauracchio: fa scena e non fa niente. E' la battuta
    # della riga, ed e' la ragione per cui il sasso resta l'arma da lancio
    # piu' misera del gioco.
    117185: "Un pugno di sassi duri come il ferro, raccolti sul ciglio della strada e messi insieme come arma. A prenderli in faccia fanno male davvero, ma sassi restano: poco più di uno spauracchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
