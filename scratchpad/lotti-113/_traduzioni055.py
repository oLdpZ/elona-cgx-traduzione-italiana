# -*- coding: utf-8 -*-
"""Le rese del lotto 055 — I MINERALI: `FILTER_ORE` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 055 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa055.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 055`: **tutte e 33** le righe hanno lo spazio prima del
`\\n`. Le code sono **27 senza** lo spazio dopo il `#` e **6 con**: `:49708`,
`:52170`, `:66137`, `:66199`, `:82610`, `:89419`.

⚠️⚠️ Previsione di `applica`: **+33** per 33 rese, nessuna gemella.
`_gia-reso.py 055`: 0 su 33.

⭐⭐⭐ LE DODICI PIETRE DEI MESI (`:48805`-`:49575`) sono una serie, e il
giapponese le scrive **identiche** parola per parola: cambia solo il nome della
pietra e il mese. Le dodici rese fanno lo stesso. Vedi `testa055.py`.
"""

IT = {
    # =====================================================================
    # LE DODICI PIETRE DEI MESI — formula identica, due parole che cambiano
    # =====================================================================
    # ⚠️ Il giapponese nomina la pietra col nome NOSTRANO nella descrizione
    #    (ザクロ石, 紫水晶, 藍玉…) mentre il nome dell'oggetto e' in katakana
    #    (ガーネット…). In italiano le due parole coincidono quasi sempre, e
    #    dove NON coincidono la resa segue il giapponese: メノウ e' l'agata
    #    (:49295, l'oggetto e' la sardonice) e 金緑石 e' il crisoberillo
    #    (:49155, l'oggetto e' l'alessandrite). Sono varieta' di quelle due
    #    famiglie, e il giapponese lo dice: chi rende dall'inglese scrive due
    #    volte la stessa parola.

    48805: "Un granato lavorato ad arte. È la pietra che rappresenta gennaio, e regalarla a chi ha una ricorrenza in gennaio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    48875: "Un'ametista lavorata ad arte. È la pietra che rappresenta febbraio, e regalarla a chi ha una ricorrenza in febbraio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    48945: "Un'acquamarina lavorata ad arte. È la pietra che rappresenta marzo, e regalarla a chi ha una ricorrenza in marzo farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49015: "Un diamante lavorato ad arte. È la pietra che rappresenta aprile, e regalarlo a chi ha una ricorrenza in aprile farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49085: "Uno smeraldo lavorato ad arte. È la pietra che rappresenta maggio, e regalarlo a chi ha una ricorrenza in maggio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # 金緑石 e' il crisoberillo, di cui l'alessandrite e' una varieta'.
    49155: "Un crisoberillo lavorato ad arte. È la pietra che rappresenta giugno, e regalarlo a chi ha una ricorrenza in giugno farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49225: "Un rubino lavorato ad arte. È la pietra che rappresenta luglio, e regalarlo a chi ha una ricorrenza in luglio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # メノウ e' l'agata, di cui la sardonice e' una varieta'.
    49295: "Un'agata lavorata ad arte. È la pietra che rappresenta agosto, e regalarla a chi ha una ricorrenza in agosto farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49365: "Uno zaffiro lavorato ad arte. È la pietra che rappresenta settembre, e regalarlo a chi ha una ricorrenza in settembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49435: "Un opale lavorato ad arte. È la pietra che rappresenta ottobre, e regalarlo a chi ha una ricorrenza in ottobre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49505: "Un topazio lavorato ad arte. È la pietra che rappresenta novembre, e regalarlo a chi ha una ricorrenza in novembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    49575: "Un lapislazzuli lavorato ad arte. È la pietra che rappresenta dicembre, e regalarlo a chi ha una ricorrenza in dicembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # =====================================================================
    # LE TRE PIETRE GREZZE — anche queste una serie identica
    # =====================================================================

    128305: "Un minerale raro, che contiene molto degli elementi del diamante. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    128375: "Un minerale raro, che contiene molto degli elementi dello smeraldo. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    128515: "Un minerale raro, che contiene molto degli elementi del rubynus. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # =====================================================================
    # I TRE CRISTALLI DEGLI ELEMENTI — la terza serie, e due su tre
    # condividono anche il «guardandoli in controluce»
    # =====================================================================

    128655: "Un cristallo giallo, che si dice racchiuda la forza del sole. Guardandolo in controluce, dentro il minerale si scorge appena un movimento come di aria che ondeggia. \\n#~Atlante dei Minerali di Vernis~",

    128725: "Un cristallo rosso, che si dice racchiuda la forza magica. Il minerale in sé è trasparente quanto il mana puro. Si racconta che nei momenti critici i maghi lo frantumino per accoglierlo nel proprio corpo. \\n#~Atlante dei Minerali di Vernis~",

    128795: "Un cristallo arancione, che si dice racchiuda la forza della terra. Guardandolo in controluce, la luce si riflette sulle molte crepe che lo percorrono dentro, ed è bellissimo. \\n#~Atlante dei Minerali di Vernis~",

    # =====================================================================
    # LE PIETRE LAVORATE, E LA TAVOLETTA CHE L'INGLESE HA SCAMBIATO
    # =====================================================================

    69048: "Un rubynus di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Anche se preso uno per uno nessuno di quei grezzi varrebbe la fatica di lucidarlo, a raccoglierli e lavorarli l'uno con l'altro ne esce una gemma di tutto rispetto, che brilla. \\n#~Atlante dei Minerali di Vernis~",

    69188: "Un diamante di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Per grandezza e per bellezza è perfetto, e gli si dà un prezzo che supera perfino quello di un artefatto. \\n#~Atlante dei Minerali di Vernis~",

    # ⚠️⚠️⚠️ QUI L'INGLESE HA RICOPIATO LA RIGA GEMELLA, ed e' la quinta volta
    #    che succede (quattro le ha trovate la 119a). Il giapponese dice
    #    錬金術の基本思想を記したエメラルドの碑文 — «l'iscrizione di smeraldo
    #    che riporta il pensiero fondamentale dell'alchimia», cioe' la Tavola
    #    Smeraldina. L'inglese ci scrive parola per parola la frase del
    #    rubynus e del diamante («Large emerald are cut from collected
    #    gemstones…»), che qui non ha alcun senso: una tavoletta non e' una
    #    gemma tagliata. ⭐ E l'indice 3, gia' reso e chiuso, lo conferma:
    #    «Una tavoletta fatta di smeraldo».
    69118: "Un'iscrizione su smeraldo, dove è riportato il pensiero fondamentale dell'alchimia. È roba per chi va matto per l'alchimia, ma vale molto anche come opera d'arte. \\n#~Atlante dei Minerali di Vernis~",

    # =====================================================================
    # I MINERALI COMUNI
    # =====================================================================

    128445: "Un minerale piccolo e bianco, che manda una luce tenue. Attraverso ere e ere costruisce con calma una sfera quasi ovale, e a vederlo così è tanto bello che lo chiamano la perla di pietra. \\n#~Atlante dei Minerali di Vernis~",

    128585: "Un minerale splendente, che non arrugginisce mai. È facilissimo da lavorare, e quel suo colore chiaro e inconfondibile è caro fin dall'antichità a chi ha il potere, come segno di ricchezza e di forza. Pare che per quel suo che di misterioso finisca spesso sotto studio. \\n#~Atlante dei Minerali di Vernis~",

    # ⚠️ La coda giapponese dice ザイール — l'atlante di ZAILE, non di Vernis —
    #    e l'inglese scrive «Vernis Ore Catalogue». `_code.py`, che passa dal
    #    giapponese, assegna correttamente «Atlante dei Minerali di Zaile».
    52313: "Questo minerale, che tende al rosso, così com'è è più tenero del ferro; ma una volta scaldato e lavorato il colore vira all'argento e diventa duro da stupire. \\n#~Atlante dei Minerali di Zaile~",

    128173: "Un pezzo di pietra che di raro non ha proprio niente. Ce n'è quante se ne vuole in giro, eppure pare che di bambini che le raccolgono ce ne siano parecchi. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # 罪作りな e' «che fa peccato», detto di chi mette gli altri nei guai
    # senza volerlo: il minerale non inganna, inganna chi lo regala.
    117318: "Un minerale che fa peccato: a farlo esaminare non si può che restarci male. Brilla in un modo così plateale da parere apposta, e lo si regala soprattutto ai bambini, o a chi non ne capisce il valore, per dire grazie. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # =====================================================================
    # L'ARTE, LE CARTE E LE MONETE
    # =====================================================================

    49708: "Una statua che luccica d'oro. È modellata in modo straordinariamente vivo, come se una persona vera fosse stata mutata in oro così com'era. \\n# ~Catalogo d'Arte di Lumiest~",

    52170: "Il bello scheletro che formano i polipi del corallo. È calcareo e duro, eppure i pesci robusti se lo sgranocchiano o se lo inghiottono intero. \\n# ~Catalogo d'Arte di Lumiest~",

    82213: "Un pezzo di carta che si dice valga più di quanto il denaro possa comprare. Sopra c'è scritto \\\"amicizia\\\", con una grafia che pare il tracciato di un lombrico. \\n#~Le Mille Cianfrusaglie che Amo~",

    82610: "Un biglietto misterioso, con disegnati sopra alcuni strumenti. Dentro ci stanno il sogno di chi suona e la riconoscenza di chi ascolta. \\n# ~Le Melodie della Limpida Irva~",

    89419: "Una monetina che si dice fosse in uso nell'antichità. Non circola più, perché ha ormai solo un valore di studio, ma pare che proprio per quanto è rara siano in molti i collezionisti che se ne occupano. \\n# ~Le Monete del Mondo: Tyris~",

    # =====================================================================
    # LE DUE PIETRE DIVINE
    # =====================================================================

    66137: "Una gemma a forma di goccia, nata dal cristallizzarsi di una stilla di forza divina. Per quanto poca, dentro nasconde la stessa forza di un artefatto. Viene fuori così, senza preavviso, quando la forza di un dio cresce per un momento; e al contrario, volerla far uscire pare sia difficile. \\n# ~Dizionario Fantastico di Irva~",

    66199: "Un frammento di forza divina, e insieme il nucleo che forma il labirinto e dà potere ai suoi guardiani. La forza che vi era nascosta è stata ormai spesa quasi tutta, e di fatto è un residuo. Ma siccome di norma dopo la nascita di una Nefia non ne resta nessuno, è raro e per questo prezioso. Si scambia a caro prezzo anche perché quel che avanza della forza divina resta lì sotto forma di incantamento. \\n# ~Dizionario Fantastico di Irva~",
}
