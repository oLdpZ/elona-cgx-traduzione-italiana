# -*- coding: utf-8 -*-
"""Le rese del lotto 066 — I GUANTI: `FILTER_GLOVES` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 066 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa066.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 066`: **10 righe su 10** con lo spazio prima del `\\n`,
10 su 10 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 066`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 066`: 0 su 10.

⭐⭐⭐ **E' IL PRIMO LOTTO CON `_122-sorelle-per-frase.py`**, lo strumento
scritto un'ora fa, e ha trovato **sette** frasi con una sorella altrove nel
file — cinque delle quali gia' rese. Le due famiglie:

    特殊な素材をかけ合わせてより強固な防護を得た◯  SEI membri:
      :100849 (058) 盾 scudo      reso     :99872  (063) 兜 elmo     reso
      :101769 (060) 鎧 corazza    reso     :101114 (066) 篭手 guanti  <- qui
      :100392 (---) 腰当 cintura  DA FARE  :130450 (---) 靴 stivali   DA FARE

    〜を守る為に作られた防具  QUATTRO membri:
      :99937 (063) 頭部 la testa   :99663 (064) 首 il collo
      :130582 (066) 手首から先     <- qui

⚠️ Nessuno dei due gruppi si vedeva prima: `_gia-reso` conta 0 su 10 e ha
ragione, perche' cerca la prosa intera.
"""

IT = {
    # =====================================================================
    # LA FAMIGLIA DEI MATERIALI SPECIALI — quarta riga di sei
    # =====================================================================
    # ⭐⭐⭐ L'apertura e' la stessa di :100849 (scudo), :101769 (corazza) e
    #    :99872 (elmo), al PLURALE perche' i guanti d'arme sono plurali:
    #    «Dei guanti d'arme che, incrociando materiali speciali, HANNO
    #    ottenuto una protezione più solida.»
    # ⚠️ Restano :100392 (la cintura) e :130450 (gli stivali), che i lotti
    #    prossimi devono rendere con la stessa apertura.
    # ⓘ 甲冑 e' l'armatura di piastre, come in :101899 del lotto 060
    #   («sovrappone le piastre alla cotta di maglia»).

    101114: "Dei guanti d'arme che, incrociando materiali speciali, hanno ottenuto una protezione più solida. Si portano soprattutto in accordo con l'armatura di piastre. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # LA FAMIGLIA DI 〜を守る為に作られた — terza riga di quattro
    # =====================================================================
    # ⭐⭐ :99937 (063)  頭部を守る為に作られた防具  -> «per proteggere la testa»
    #    :99663 (064)  首を守る為に作られた装身具  -> «per proteggere il collo»
    #    :130582 (066) 手首から先を守る為に作られた防具               <- qui
    #    L'apertura e' la stessa, cambia la parte del corpo.

    130582: "Un'armatura fatta per proteggere dal polso in avanti. Toglie un po' di libertà alle dita, ma è meglio che perdere una mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # GLI ALTRI GUANTI
    # =====================================================================
    # ⚠️ 篭手 e 小手 sono i «guanti d'arme» (plurale, come l'indice 3 di
    #   tutta la categoria), 手袋 sono i «guanti» e basta. Due parole
    #   diverse per due oggetti diversi, e il giocatore ha tutt'e due.
    # ⓘ 武骨 -> «rozzo», come la gorgiera del 064 e l'anello del drago del 065.
    # ⭐ やや重いがそれでも尚余りある: e' l'eco di :100849, lo scudo dello
    #   stesso libro («ma renderà molto più di quel poco che pesa in più»).
    101247: "Dei guanti d'arme rozzi, fatti mettendo la protezione davanti a tutto. Pesano un po', ma rendono molto più di quel poco che pesano in più. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    101180: "Dei guanti fatti per aderire perfettamente alla pelle. Sono leggerissimi, tanto che ci si dimentica di averli addosso. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ L'indice 3 gia' in gioco dice «Un'armatura che calza sul palmo»: la
    #   riga lunga aggiunge le due funzioni, il freddo e la presa sull'arma.
    101314: "Un'armatura che vale anche come riparo dal freddo. E non solo: dicono che serva non poco anche a non far scivolare l'arma di mano. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    130649: "Dei guanti d'arme di pregio, cosparsi di lavorazioni d'ogni sorta. Contano soprattutto per la cerimonia, ma anche così quegli ornamenti una qualche protezione la danno. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》
    # =====================================================================
    # ⓘ 隕鉄 non e' nel dizionario: e' il ferro meteorico, e l'inglese dice
    #   «meteoric iron». Il nome dell'oggetto — «Cesto delle Meteore» — ci va
    #   d'accordo, e l'indice 3 parla gia' di uno sciame di meteore.
    62801: "Una cinghia di cuoio bianca e robusta, con delle borchie di metallo conficcate dentro. Si equipaggia avvolgendola dall'avambraccio fino al pugno, come una fasciatura. Pare che nelle borchie, fatte di ferro meteorico, ci sia dentro del potere magico. \\n# ~Dizionario Fantastico di Irva~",

    # 富の神 -> «la dea della ricchezza», gia' in gioco sulla statua che la
    # raffigura (ed e' Yacatect, che nel gioco parla al femminile).
    # ⓘ 見てるだけで嫌になるくらい: il giapponese dice che a guardarla viene
    #   il voltastomaco, e l'inglese lo tiene. E' il senso della riga.
    75647: "Una catena vistosissima, che la dea della ricchezza si è fatta fare su misura. È di uno sfarzo tale che a guardarla viene il voltastomaco. \\n# ~Dizionario Fantastico di Irva~",

    75714: "Dei guanti d'arme azzurri, con un disegno misterioso sulla superficie. Ci abita dentro uno spirito. \\n# ~Dizionario Fantastico di Irva~",

    # 火炎竜 -> «il drago di fuoco» (dizionario: il drago di fuoco adulto, il
    # cucciolo di drago di fuoco). 噂に違わず e' «come vuole la voce».
    107527: "Dei guanti d'arme che dicono ricavati da un drago di fuoco. Come vuole la voce sono sempre avvolti nelle fiamme, eppure chi li porta, altro che bruciare, non sente nemmeno il caldo. \\n# ~Dizionario Fantastico di Irva~",
}
