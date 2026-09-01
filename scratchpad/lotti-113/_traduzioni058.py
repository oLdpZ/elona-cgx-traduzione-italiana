# -*- coding: utf-8 -*-
"""Le rese del lotto 058 — GLI SCUDI: `FILTER_SHIELD` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 058 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa058.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 058`: **21 righe su 24** hanno lo spazio prima del
`\\n`; le tre senza sono `:42852`, `:71439` e `:71509`. Tutte e 24 le code hanno
lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`: **+24** per 24 rese, nessuna gemella.
`_gia-reso.py 058`: 0 su 24. `_code.py 058`: 0 righe senza resa in tabella.

⭐⭐ `_120-serie-bacchette.py 058` ha trovato **una serie di cinque**: i cinque
tonfa ST-01..ST-05, che aprono tutti con 攻防一体の装備。 La formula si ripete
**identica** in tutte e cinque le rese, come le tre armi della 120a.
"""

IT = {
    # =====================================================================
    # I CINQUE TONFA — la serie, e l'apertura che NON cambia
    # =====================================================================
    # ⭐ 攻防一体の装備。apre tutte e cinque le righe, ed e' cosi' che il
    #    giocatore riconosce l'ST-01 come parente dell'ST-05. Variare i
    #    verbi cancellerebbe la serie: la resa e' la stessa parola per
    #    parola, e cambia solo quel che viene dopo.

    # ST-05 SONIC — 推進装置 e' «propulsore» (glossario 111a), e l'indice 3
    #   gia' reso dice «Un tonfa con un propulsore incorporato».
    71233: "Un equipaggiamento che unisce attacco e difesa. Ha un piccolo propulsore incorporato, e l'accelerazione dà al colpo più forza di perforare. Siccome per un attimo accelera oltre la velocità del suono, regge anche il calore e gli urti. \\n# ~Dizionario Fantastico di Irva~",

    # ST-04 SABER — 光子 e' «laser» dalla 110a, e l'indice 3 gia' reso dice
    #   «Un tonfa da cui escono lame laser»: nello stesso pannello.
    71302: "Un equipaggiamento che unisce attacco e difesa. Sa convertire il mana di chi lo impugna e formarne una lama laser. Se trova un varco, dalla botta passa dritto al fendente. \\n# ~Dizionario Fantastico di Irva~",

    # ST-03 SMASH — 次々と粉砕する sta accanto all'indice 3 gia' reso
    #   «Un tonfa che attacca a raffica».
    71371: "Un equipaggiamento che unisce attacco e difesa. Leggero e saldo. Si può anche allentare un poco la presa e colpire facendolo roteare. Permette attacchi corpo a corpo raccolti e svelti, e sbriciola i bersagli uno dopo l'altro. \\n# ~Dizionario Fantastico di Irva~",

    # ST-02 SHIELD — ⚠️ senza lo spazio prima del \\n.
    71439: "Un equipaggiamento che unisce attacco e difesa. Ci è montato sopra un generatore di scudo repulsivo, e così, pur essendo un tonfa, tiene una difesa alta.\\n# ~Dizionario Fantastico di Irva~",

    # ST-01 SACRIFICE — ⚠️⚠️ il giapponese dice SOLO la formula. L'inglese ci
    #   aggiunge «It allows it's user to sac», che e' tagliato a meta' di
    #   parola: la resa viene dal giapponese e finisce li'. L'indice 3, gia'
    #   reso in una sessione passata, ha fatto la stessa cosa («Un tonfa.»
    #   contro «It is a tonfa that suc»). ⚠️ senza lo spazio prima del \\n.
    71509: "Un equipaggiamento che unisce attacco e difesa.\\n# ~Dizionario Fantastico di Irva~",

    # L'ST-01 ha anche un description(2): un appunto degli autori.
    # ⭐ 第三部 e' «Parte terza» nel nome della missione @QM[第三部 永遠の盟約]
    #    -> «Parte terza - Il patto eterno». L'inglese scrive «ACT III», che
    #    in italiano il giocatore non ha mai letto.
    71511: "Per la parte terza. \\n# ~Appunto Misterioso~",

    # =====================================================================
    # GLI ARTIGLI — quattro oggetti che stanno fra gli scudi
    # =====================================================================
    # ⚠️ :42852 e' senza lo spazio prima del \\n.
    # インド象 e' «elefante indiano», la bestia-metro delle descrizioni di
    #   Elona+; 現代イルヴァ e' «l'Irva di oggi», gia' reso sulla zanzara.
    42852: "Gli artigli di un grande orso mangiatore d'uomini. Sono così robusti da lacerare una lastra di ferro: con un colpo solo spazzano via la faccia, ossa comprese, a una creatura dell'Irva di oggi, e l'onda d'urto arriva ad ammazzare perfino l'elefante indiano lì accanto.\\n# ~Dizionario Fantastico di Irva~",

    # 秘術 e' «arti segrete» (gia' reso sulla non morta e sul ninja di carta).
    67599: "Artigli temprati con le arti segrete dei ninja. Vibrano entrando in risonanza con certe onde sonore, e così tagliano meglio. Pare che sappiano anche amplificare un incantesimo recitato e renderlo più potente. \\n# ~Dizionario Fantastico di Irva~",

    # 鉤爪, l'oggetto comune: 防具 e' «armatura», 格闘 e' il «corpo a corpo».
    68250: "Un equipaggiamento che imita gli artigli delle bestie, dei rapaci, degli insetti. In origine serviva ad aggrapparsi agli alberi e al terreno; ma siccome fa da armatura per deviare i colpi e insieme da arma per rendere più forte il corpo a corpo, oggi lo si usa soltanto per combattere. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 不幸 e' «sfortuna» (la dea che ha in mano la sfortuna), e 幸運の女神 e'
    #   la «dea della fortuna»: le due stanno nella stessa frase.
    69256: "Un'arma a forma di artiglio, che porta sfortuna a chi squarcia. Un tempo era roba capace di portare sfortuna eterna a chiunque la sfiorasse, ma nella battaglia contro la dea della fortuna ha perso quasi tutta la sua forza. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # I QUATTRO PEZZI UNICI, dove il giapponese porta nomi gia' resi altrove
    # =====================================================================
    # ⭐⭐ 神の間 NON e' «tra gli dei»: e' il **Sigillo Eterno**, il luogo del
    #    gioco (inglese `Eternal Seal`), reso in una quarantina di battute.
    #    手枷 e' «manette», dall'indice 3 gia' reso di questo stesso oggetto.
    57962: "Manette con la catena, forgiate dagli dei antichi. Pensate per l'uso al Sigillo Eterno, sono fatte robuste sul piano fisico e basta, senza l'aiuto di alcun potere divino. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ 冒険ゼミ e' il «Seminario d'Avventura» e 赤剣先生 il «maestro Spada
    #   Rossa»: due nomi che il giocatore legge nelle battute della gilda.
    #   がんばりシールド e' un bisticcio — シール, il bollino che il maestro
    #   dava a chi passava, piu' ド: in italiano lo scudetto e' insieme lo
    #   scudo piccolo e il bollino del bravo.
    59592: "Un oggetto che si dona agli allievi del Seminario d'Avventura. Un tempo lo si dava solo a chi superava la prova del maestro Spada Rossa. Allora si chiamava Scudetto Bravo, e pare che oltre alla corona ci fossero anche altri motivi. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ テスカトリポカ e' «Tezcatlipoca» e 初代 e' «il primo» (dal gia' reso
    #   先代 «che vennero prima»). 黒曜石 dell'indice 3 e' «ossidiana».
    59860: "Uno specchio misterioso che, se lo si carica di potere divino, sputa fumo. Si racconta che il primo Tezcatlipoca, cui una dea aveva staccato una gamba a morsi mentre la uccideva, per un certo tempo se lo sia attaccato addosso al posto della protesi. Il suo nome, in lingua antica, vuol dire \\\"lo specchio della notte\\\". \\n# ~Dizionario Fantastico di Irva~",

    # 騎士盾 e' «scudo da cavaliere», il nome dell'oggetto comune del lotto.
    73560: "Uno scudo da cavaliere in cui è stato sigillato il potere di una maledizione. Così agisce soltanto l'\\\"anima del cavaliere che vuole difendere il suo signore\\\" rimasta nello scudo, e ne esce una difesa altissima. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ クイーン・セドナ号 e' la «<Regina Sedona>», che il giocatore conosce
    #   come persona (`<Regina Sedona> la fanciulla delle vele`) e come nave:
    #   la sua carta racconta lo stesso naufragio, «per il vento d'etere
    #   durante il viaggio inaugurale verso Porto Kapul».
    81328: "Un pezzo della <Regina Sedona>, la nave affondata per il vento d'etere. Come scudo si può anche usare, ma la difesa che dà è poca cosa. Galleggia, però al massimo tiene a galla una persona sola che stia annegando. \\n# ~Dizionario Fantastico di Irva~",

    # 出血 e' «sanguinamento» (l'etichetta di stato), e sta nell'indice 3.
    82410: "Uno scudo pieno di spine grandi e piccole sulla faccia, che a guardarlo fa già male. Per difendersi non basta del tutto, ma quando lo si sbatte addosso con tutta la forza, il povero nemico si contorcerà dal dolore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # リュート e' «liuto», dal nome non identificato «liuto robusto».
    82478: "Un liuto che nei tempi antichi, si dice, mandava un suono meraviglioso. Oggi però lo si tratta soltanto come un ottimo scudo, ricavato da un legno fortissimo su cui gli anni non si vedono, e un suono come quello d'allora non lo darà più. \\n# ~Dizionario Fantastico di Irva~",

    # =====================================================================
    # I SEI SCUDI COMUNI — e il nome dell'oggetto detta la parola
    # =====================================================================
    # ⚠️ 分厚い e' «spesso» (glossario 111a), e 非常に... e' il grado alto
    #   della scala del peso: l'indice 3 gia' reso dice «Uno scudo
    #   pesantissimo», quindi qui il corpo dice SPESSO e non ripete pesante.
    100717: "Uno scudo fatto spessissimo. Il peso, va da sé, non è cosa da poco: si dice che una volta caduto a terra ci voglia la forza di più persone per rimetterlo in mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100783: "Uno scudo grande e rettangolare. È tanto largo da coprire il corpo, e può fare da muro improvvisato per ripararsi dal nemico; ma proprio per questo dà anche parecchi impicci, e si dice che a maneggiarlo ci voglia esperienza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100849: "Uno scudo che, incrociando materiali speciali, ha ottenuto una protezione più solida. Ha il difetto di essere un po' pesante, ma renderà molto più di quel poco che pesa in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⚠️ 防具 e' «armatura» e 鎧 e' «corazza»: il glossario le tiene distinte,
    #   e qui il giapponese le mette una contro l'altra nella stessa frase.
    100915: "Un'armatura pensata per parare i colpi. A differenza della corazza la si tiene con la propria mano, e così si può fronteggiare la violenza che ti si getta addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    100981: "Uno scudo tondo, col baricentro messo al centro. Si dice che quella forma tonda così particolare sia nata perché, andando al fronte, non battesse per terra e non impedisse di camminare. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    101047: "Uno scudo più piccolo del normale. Legandolo al braccio si è riusciti a togliere di mezzo la scomodità di portarlo e il peso che ne veniva, ma in cambio lo spazio che si riesce a difendere si è fatto parecchio stretto. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 用 e' «per», come nei tre modi di dire «per» del glossario.
    127204: "Uno scudo di gran pregio, fatto per i cavalieri. Porta cesellature e ornamenti lavorati con cura, scelti su misura di chi lo impugna; ma non è soltanto da cerimonia, e una certa protezione ce l'ha. \\n# ~Raccolta di Armi e Armature da Usare Domani~",
}
