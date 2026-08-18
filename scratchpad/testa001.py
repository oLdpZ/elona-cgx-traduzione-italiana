# -*- coding: utf-8 -*-
"""Il menu di casa: negozio, allevamento, campo di prigionia, casa, campo.

`map_user.hsp:433`-`:515`, cioe' le trentadue voci del menu che si apre premendo
il tasto delle strutture dentro una proprieta'. E' la **prima apertura di
`map_user.hsp`**: il file non aveva nessun dizionario, e quindi
`verifica --dizionario` non lo nominava — 204 `lang()` che nessun conteggio
guardava. Dopo questo lotto il file entra nel referto con 174 voci da fare.

⭐ **Il lotto nasce da una misura, non da un elenco.** La 60a ha portato la
rete 5 fuori da `text.hsp`, e il referto ha detto che `map_user.hsp` ha
**trentaquattro voci di menu senza dizionario**: sono il gruppo piu' grosso di
tutto il gioco in un riquadro solo.

## ⚠️ Il riquadro e' 280 px, e il tetto e' 30 caratteri

`map_user.hsp:537` chiude la corsa dei `promptAdd`, e sopra ci sono **tre**
`val =`:

    :522   val = promptx, prompty, 280, 1          dentro /* ... */   MORTO
    :529   val = promptx, prompty, 280 + (en * 50), 1   se e' un negozio: 330
    :532   val = promptx, prompty, 280, 1               altrimenti: 280

⚠️ **Le sette voci del negozio vivono davvero in un riquadro da 330** (tetto 36),
perche' stanno dentro la stessa `if ( adata(ADATA_ID, ...) == AREA_SHOP )` che lo
allarga — il mod lo dice nel commento, «Increase the size of the shopkeeper
window». La rete pero' tiene il **piu' stretto**, che e' la regola giusta per una
guardia, e tutte le rese di questo lotto stanno **dentro 30**: la piu' lunga ne
usa 28. Nessuna ha avuto bisogno del riquadro largo.

## Il vocabolario, tutto gia' deciso altrove

    negoziante          店主, da db_creature.hsp:74301 e ai.hsp:1834
    talento             フィート, da command.hsp:2113 «[Talenti disponibili]»
    bestiame            家畜, da chara_func.hsp:2067 e db_item.hsp:137486
    allevatore          ブリーダー, da proc.hsp:21819 «Effetto allevatore»
    prigioniero         収容者/連行者, da command.hsp:1197 e adv.hsp:197
    rinchiudere         収容する, da command.hsp:1196 «Chi vuoi rinchiudere?»
    Energia da Lavoro   労働エナジー, da map.hsp:12281 e proc.hsp:4135
    moneta di bronzo    ブロンズ硬貨, da db_item.hsp:137911
    compagno            仲間, la resa dominante in tutto il dizionario

💡 **Quattro voci su trentadue erano gia' decise**, e cercarle e' costato meno
che scriverle: `:456` porta al menu di `text.hsp:1646` («15 al giorno (Esp.
Trattativa+)»), `:480` a quello di `text.hsp:2213` («<Livello 0> lavora chi ne
ha voglia»), e le rese di questo lotto ne prendono le parole invece di
inventarne altre.

## ⚠️ Le due coppie simmetriche

`:465`/`:468` e `:471`/`:474` sono attiva/annulla dello stesso codice, e in
giapponese cambia una parola sola (発動 / 解除). Le rese sono una coppia anche in
italiano — «Blocca» / «Sblocca» — invece di due frasi diverse: un menu dove due
voci opposte non si somigliano si legge due volte.
⚠️ Ci si perde コード, «codice»: sta nel giapponese e nell'inglese, ma dire
«Attiva il codice antiriproduzione» costa 33 caratteri su 30. Si tiene quel che
il giocatore deve capire — che cosa succede — e si lascia andare il come.

## ⚠️ Dove il giapponese dice piu' dell'inglese

    :461  家畜・ブリーダー移動  sposta il bestiame **e** gli allevatori;
          l'inglese dice solo «Move a livestock». La resa segue il giapponese.
    :462  餌を撒く（家畜の餌消費）  l'azione e' «spargere il mangime», il
          consumo e' la nota fra parentesi. L'inglese tiene solo la nota.
    :463  場内消毒（浄化消毒薬消費）  stessa forma: l'azione e' disinfettare.
    :489  家の情報 dice «informazioni», l'inglese «Home rank». La schermata
          mostra il rango dentro le informazioni: la resa tiene la piu' larga.
"""
