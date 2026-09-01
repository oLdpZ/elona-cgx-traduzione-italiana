# -*- coding: utf-8 -*-
"""Le rese del lotto 067 — I MANTELLI E LE ALI: `FILTER_CLOAK` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 067 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa067.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 067`: **10 righe su 10** con lo spazio prima del `\\n`,
10 su 10 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 067`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 067`: 0 su 10.

⭐⭐ **`_122-sorelle-per-frase` trova sei frasi con una sorella, e stavolta le
sorelle stanno TUTTE DENTRO QUESTO LOTTO** — nessuna e' ancora resa. Sono due
coppie, e vanno rese come coppie:

    :94022 / :96124   DUE frasi identiche su tre. Cambia solo コウモリの羽
                      (il pipistrello) contro 鳥の羽 (l'uccello)
    :100197 / :126777 la seconda frase identica parola per parola

ⓘ Che le sorelle siano dentro il lotto non toglie valore alla rete: nel 060
`_coerenza` e `_120-serie-bacchette` **non** le avevano viste, perche' guardano
la prosa intera e queste due prose differiscono.
"""

IT = {
    # =====================================================================
    # LA COPPIA CHE CAMBIA SOLO L'ANIMALE
    # =====================================================================
    # ⭐⭐⭐ コウモリの羽を模した装具 contro 鳥の羽を模した装具, e poi due
    #    frasi IDENTICHE. Le rese sono identiche tranne l'animale, di
    #    proposito: il giocatore ha tutt'e due gli oggetti e li confronta.
    # ⓘ コウモリ -> «pipistrello» (dizionario). Gli indici 3 dei due oggetti
    #   sono a loro volta identici («Un ornamento di piume da mettere sulla
    #   schiena»), quindi la coppia si vede gia' in gioco.

    94022: "Un oggetto da indossare, fatto a somiglianza delle ali di un pipistrello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    96124: "Un oggetto da indossare, fatto a somiglianza delle ali di un uccello. Para i colpi che arrivano alla schiena, ma è costruito unicamente per far bella figura. Ha anche, per quanto minimo, l'effetto di sollevare un po' da terra. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA COPPIA CHE CONDIVIDE LA SECONDA FRASE
    # =====================================================================
    # ⭐⭐ 幾多の素材を織り込むことで布自体の強度を増している, parola per
    #    parola in tutt'e due. Cambia la prima frase: 体に巻きつけるゆったり
    #    とした (il mantello) contro 鎧の上から羽織る薄い (quello leggero).
    # ⓘ 羽織る e' il verbo dell'indice 3 del mantello, gia' in gioco:
    #   «Un'armatura da buttarsi sulle spalle».

    100197: "Un tessuto ampio da avvolgersi attorno al corpo. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    126777: "Un tessuto sottile da buttarsi sulle spalle sopra l'armatura. Intrecciandoci dentro materiali di ogni sorta, la stoffa stessa ne esce più resistente. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ Terza riga della stessa stoffa: 素材を織り込んだ布 senza 幾多の, e la
    #   rete non l'ha accostata perche' la frase e' troppo diversa. Ma la
    #   parola «intrecciati» resta la stessa, ed e' il punto.
    100262: "Un mantello con del metallo duro applicato dietro a una stoffa in cui sono intrecciati dei materiali. Addosso, para una parte dei colpi. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》
    # =====================================================================
    # 絶器 -> «zekki», gia' in gioco sull'indice 3 dei guanti del lotto 066
    # («Dei guanti d'arme detti zekki»): la parola non si traduce.
    # ⓘ Le tre frasi del giapponese sono un'invocazione, non una descrizione:
    #   niente verbi finiti nelle ultime due. L'italiano tiene il ritmo.
    59062: "Uno zekki che dicono creato da una dea di un altro mondo. È la spada dello splendore e della custodia. Ali d'oro che, dicono, scendono dal cielo attraversando i mondi e spazzano via le tenebre. \\n# ~Dizionario Fantastico di Irva~",

    # マニピュレーター -> «manipolatori» (dizionario). 義手 e' la protesi di
    # braccio: il gioco ne parla altrove come slot d'equipaggiamento in piu'.
    63652: "Nasceva come protesi da combattimento, e da lì è stato sviluppato in un equipaggiamento che si cambia con facilità. Siccome legge i segnali elettrici da sopra i vestiti, senza collegarsi ai nervi, a seconda dei casi può non muoversi come si vorrebbe. I manipolatori sono costruiti robusti, e cambiando il rapporto degli ingranaggi si arriva a sferrare colpi violentissimi. \\n# ~Dizionario Fantastico di Irva~",

    # イェルス軍 -> «l'esercito di Yerles» e 火炎竜 -> «drago di fuoco», come
    # nei lotti 061 e 066. コンペ e' la gara d'appalto fra due prototipi.
    76587: "Un'unità di volo e propulsione che l'esercito di Yerles ha sviluppato partendo dalle ali di un drago di fuoco. È robusta, e a difendersi non è che non serva. La svilupparono come equipaggiamento personale del soldato, ma in gara perse contro un'unità di volo da montare sulle gambe e non fu adottata. La capacità di volo però era solida, e più tardi l'hanno riutilizzata come pezzo per le armi da combattimento aereo. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ 悪い意味でサマになる: gli sta bene, ma nel senso sbagliato. E' la
    #   battuta della riga e va tenuta intera. 渋い e' l'eleganza asciutta di
    #   chi ha vissuto, non la tristezza.
    77354: "Il mantello che portava un eroe di un tempo. È tutto strappato e sformato, e addosso a chi ha già l'aria sfortunata sta bene nel senso peggiore. Uno con un certo stile asciutto, magari, riuscirebbe a portarlo. \\n# ~Dizionario Fantastico di Irva~",

    # ⚠️ 異形の森 -> «la Foresta Eretica» (dizionario, due battute). Il
    #   giapponese qui NON dice «vento di etere» ma 忌むべき風, il vento
    #   maledetto: la resa lo tiene, e cosi' non entra in conflitto con
    #   l'indice 3 dello stesso oggetto, che dice gia' «vento di etere».
    # ⓘ 変異 -> «mutazione», come il cappello da fata del lotto 063.
    93692: "Un mantello che, dicono, para il vento maledetto che si leva dalla Foresta Eretica. Serve unicamente a fermare le mutazioni portate da quel vento, e contro le mutazioni di tutti i giorni, o contro la pioggia e il vento, non riparerà. \\n# ~Dizionario Fantastico di Irva~",
}
