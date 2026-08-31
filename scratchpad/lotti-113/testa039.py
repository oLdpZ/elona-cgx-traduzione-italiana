# -*- coding: utf-8 -*-
"""115a - Lotto 039 di `db_item.hsp`: GLI SCARTI, seconda parte.

`FILTER_JUNK`, righe 62.000-76.000: **51 righe** su 34 oggetti — 34 dell'indice
0, 8 dell'indice 1 e 9 dell'indice 2. E' il lotto con piu' righe di indice 1 e 2
di tutta la sessione, e la ragione e' una famiglia sola.

### ⭐⭐⭐ GLI OTTO OGGETTI DEGLI DEI: UN PANNELLO E' UNA SCENETTA A DUE VOCI

`:62865`, `:62929`, `:62993`, `:63057`, `:63121`, `:63185`, `:63249`, `:63313`
sono oggetti personali di otto divinita', e hanno tutti la stessa forma:
l'indice 0 e' la voce d'enciclopedia, e gli indici 1 e 2 sono **due battute di
due dei diversi**, che si rispondono.

    il manubrio    Urcaguary «me lo prendo un attimo» / Opatos «ridammelo»
    l'amuleto      Rovid mostra la scritta / Jure si vergogna
    la candela     Arasiel ride dello schiavo / Lulwy «la prossima sei tu»

⚠️ **Vanno rese come una scena, non come tre righe**: la seconda battuta e' la
risposta alla prima, e nel manubrio la risposta e' perfino un gioco fonetico —
「フゥハハハハハハハハハー！かえして」, dove la risata **diventa** «ridammelo».
L'inglese lo tiene («Muwahahahahahahave it back!»), l'italiano pure
(«Muahahahaha ridammelo»).
⚠️ Ma non attaccato: 15 caratteri di fila li spezza l'impaginatore, e il
preflight l'ha visto. Lo spazio e' quello che salva la battuta.

### ⭐⭐⭐ I NOMI DEGLI DEI SI COPIANO, E UNO NON E' QUELLO CHE SEMBRA

Tutti e otto i nomi sono gia' nel dizionario nella forma `<Nome>`, e si trovano
con `lotti-111/_cerca.py`. ⚠️⚠️ **ネヘルタード e' `<Amurdad>`**, non
«Nehertard»: e' il nome che l'inglese di monte gli da', ed e' gia' a schermo in
`chat.hsp` e nelle chiamate di soccorso. Traslitterare il giapponese avrebbe
prodotto un dio nuovo.

⭐ Gli **epiteti in prosa** (剛石の女神, 砂嵐の女神…) non stanno nel dizionario
come voci a se': si ricavano dalle righe di livello 150, che sono gia' rese —
`<Urcaguary> la gemma tenace`, `<Arasiel> della tempesta di sabbia`,
`<Karavika> del canto e della danza`, `<Sophia> la Saggia`.

⚠️ **Quattro epiteti non hanno nessun precedente** e sono stati coniati qui:
守護の神 «il dio della protezione», 鉄騎の神 «il dio dei cavalieri di ferro»,
不幸の女神 «la dea della sventura», 永遠の神 «il dio dell'eternita'». Sta
scritto perche' una passata futura sull'elenco degli dei li trovi e li accordi,
invece di scoprirli per caso.

### ⭐⭐ L'INGLESE SALTA DUE FRASI, E TUTT'E DUE DICONO A CHE SERVE L'OGGETTO

  - `:62865`, il manubrio: il giapponese dice «usandolo mentre ti alleni
    l'effetto sale di parecchio», che e' **l'unica frase che spieghi l'oggetto**.
    L'inglese la salta e tiene solo l'aneddoto sui due fratelli;
  - `:63249`, la tazza: il giapponese racconta che la dea della sventura ha
    continuato ad assalirla e che oggi ne ha in quantita'. L'inglese salta al
    referto finale.

### ⭐⭐ E SULLA SPADA L'INGLESE INVENTA DUE VOLTE NELLA STESSA RIGA

`:63583`, la spada del teschio furiosa:

    giapponese   il taglio e' migliorato, ma l'impugnatura succhia la vita;
                 la potenza dipende dall'**Alchimia di quando e' stata fatta**
    inglese      «powered up with the power of nether and magic»;
                 la potenza dipende da «throwing techniques and their
                 magical device experience»

Nessuna delle due invenzioni e' innocua: la seconda dice al giocatore di
allenare le abilita' sbagliate. Si segue il giapponese, e la riga gemella
`:64993` (la spada non furiosa) lo conferma, perche' li' l'inglese la frase
sull'alchimia la traduce giusta.

### ⭐ LE TRE PERLE RICURVE, E L'INGLESE CHE SI CONTRADDICE DENTRO UNA RIGA

`:66009` (acqua), `:68045` (fuoco) e `:52579` (gelo, lotto 038) sono la stessa
frase con l'elemento cambiato. L'inglese di `:68045` e di `:52579` e' la stessa
copia: dice «absorb **hot** air», poi «suppress **freezing** damage» in uno e
«burning damage» nell'altro, e chiude in tutt'e due con «the **cold** air that
covers the surroundings». Una riga che si smentisce da sola in tre punti.

Il giapponese dice 火 in uno e 冷気 nell'altro, e i nomi degli oggetti — 火吸
e 冷吸, «che assorbe il fuoco» e «che assorbe il freddo» — lo confermano.

### ⓘ I dodici materiali da sintesi

`:74693`-`:75375` sono dodici oggetti che hanno tutti lo stesso indice 3 («un
oggetto per la sintesi») e un indice 0 di **una o due frasi**, ognuno da un
libro diverso. Sono le rese piu' corte del lotto e non hanno trappole; l'unica
cosa da guardare e' che l'inglese di `:74817` porta una **«s» spaiata** prima
del `\\n` («The slight brightness is stylish. s»), che non si riporta.
"""
