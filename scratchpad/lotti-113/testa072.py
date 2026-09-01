# -*- coding: utf-8 -*-
"""123a - Lotto 072 di `db_item.hsp`: LE MUNIZIONI, e la categoria CHIUDE.

`FILTER_AMMO`, righe da `:65947` a `:127062`: **5 righe**, tutte dell'indice 0,
su 5 oggetti (proiettile magnum, cella energetica, dardi da balestra,
proiettile, freccia). Con questo lotto la categoria va a **0 da fare su 5
vive**, ed e' la **ventisettesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 072`: **+5** per 5 rese,
nessuna gemella. ⓘ `_code.py 072`: 0 righe senza resa in tabella.
`_forma.py 072`: 5 su 5 con lo spazio prima del `\\n`, 5 su 5 con lo spazio
dopo il `#`. Preflight: **0 guasti, 0 parole lunghe**.
`_122-sorelle-per-frase 072`: 0. `_gia-reso 072`: 0 su 5.

### ⚠️⚠️⚠️ L'INGLESE DI `:98725` E' ROTTO, E LO DICE DA SOLO

    EN  A thin rod-shaped **arrowhead** with a square **arrowhead** used in
        mechanical bows.
    JP  機械弓に用いられる四角い矢じりのついた細い棒状の矢弾。

矢弾 e' il **dardo**, 矢じり e' la **punta**: due parole, e monte le ha rese
tutt'e due «arrowhead». La frase inglese e' senza soggetto — un «arrowhead»
con un «arrowhead» — e chi la traducesse scriverebbe qualcosa che non e' un
oggetto.

⭐ Non e' il difetto della 122a (l'inglese di un altro oggetto): e' l'inglese
di **questo** oggetto, scritto male. Il rimedio e' lo stesso, cioe' la fonte
giapponese, ma la rete che cerca l'inglese doppio non lo prende, perche' la
riga non e' duplicata da nessuna parte.

### ⚠️⚠️ `機械弓` E' RESO IN DUE MODI NEL DIZIONARIO — QUATTRO CONTRO DUE

    balestra         機械弓 (il NOME dell'oggetto)
                     閃光の機械弓 -> «balestra rapida»
                     機械弓と共に装備する武器だ -> «insieme a una balestra»
                     (e' l'indice 3 di QUESTA voce, :98728)

    arco meccanico   連射力を高めた機械弓だ -> «Un arco meccanico che spara…»
                     非常に重い機械弓だ     -> «Un arco meccanico pesantissimo»

Le due dell'«arco meccanico» sono indici 3 di **pezzi unici** della categoria
＜秘宝＞. Qui vince «balestra», perche' e' quel che dicono il nome in cima al
pannello e l'indice 3 della stessa voce — la regola del 069 e del 070.

⚠️ **Ma la divergenza resta, ed e' vera**: due righe del gioco chiamano
«arco meccanico» l'arma che tutto il resto chiama «balestra». Va sistemata a
mano, fuori da un lotto del corpo, come «vento di etere» della 122a.
E' la **settima** cosa aperta.

### ⭐ 加工 TORNA DUE VOLTE, E RESTA «LAVORATO»

`:96634` (il corpo ad alta energia lavorato in proiettile) e `:126986` (la
piccola sfera lavorata per essere sparata) usano tutt'e due 加工. E' lo stesso
verbo che il lotto 070 ha distinto da 使用: la cosa e' materia prima che
diventa altro. Due lotti di fila, stessa parola italiana.

### ⓘ Le altre parole, e da dove vengono

- 火薬 -> **«polvere da sparo»** (dizionario: il barile e il tubo dei fuochi).
- 反動 -> **«contraccolpo»** (dizionario: cinque voci sul contraccolpo del mana).
- 威力 -> **«potenza»** (dizionario). 拳銃 -> **«pistola»** (dizionario).
- 銃器 / 銃 -> **«arma da fuoco»**, come gli indici 3 di questi stessi oggetti.
- 筒 -> **«tubo»**, dal dizionario: il tubo che spara palle di polvere.
- 口径はそのままに -> **«a parita' di calibro»**: il giapponese mette in
  contrasto quel che non cambia con quel che cambia, e l'italiano ha la
  locuzione fatta apposta.
- 束ねたもの / 束ねているので: il giapponese **ripete** il legare, ed e' quello
  che spiega il peso. «Un fascio … Essendo in fascio» tiene il legame in piedi;
  l'inglese lo tiene pure («A bundle … Because they are bundled»).

### ▶ Il conto

Il corpo passa da **1.498 a 1.503 rese su 1.513**, e restano **10 righe** — di
cui una rinviata (`:129299`). Dopo il 072 mancano **cinque** categorie:

    4  FILTER_FURNITURE_WELL   1  FILTER_PLATINUM
    2  FILTER_FURNITURE_ALTAR  1  FILTER_GOLD
                               1  FILTER_CARGO_FOOD

⚠️ La tabella si rilegge con `_114-corpo-da-fare`, non si eredita da qui.
"""
