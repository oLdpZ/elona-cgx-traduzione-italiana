# -*- coding: utf-8 -*-
"""114a - Lotto 031 di `db_item.hsp`: IL MOBILIO, quinta parte.

`FILTER_FURNITURE`, righe 113.000-122.000: **36 righe** su 35 oggetti — 35
dell'indice 0 e una dell'indice 2 (`:115384`, la battuta di <Seth>). Del fronte
del mobilio restano **54 righe**, tutte sopra la riga 122.000.

### ⭐⭐⭐ CINQUE GRUPPI DICONO UNA FRASE IDENTICA, E LA RESA E' IDENTICA

Questo lotto e' il piu' ripetitivo del fronte, e la ripetizione **non e' nel
file**: sta nella stessa frase giapponese copiata in righe lontane, che nessuna
rete di lotto confronta perche' le stringhe intere sono diverse.

- **Le sette tombe** (`:119943`, `:120005`, `:120067`, `:120129`, `:120191`,
  `:120253`, `:120315`): la seconda frase e'
  当然ながら非常に重いので持ち上げてみようと思わない方がいいだろう in **tutte
  e sette**. Cambia solo la prima.
- **Il lavello e il bancone** (`:120947`, `:121011`): seconda frase identica.
- **I due mobili in vetrina** (`:121446` l'armatura, `:121508` l'abito):
  大きく試着不可と書かれている為、装備することはできない, identica.
- **Le armi e gli archi** (`:121570`, `:121632`):
  あくまでもまとめ売り用らしく、個別に売ることはしていないようだ, identica.
- **Le due colonne ornate** (`:121891`, `:121953`):
  これは古代の建築様式を復元したものであるという, identica.
- **I due mucchi di libri** (`:121260`, `:121322`): la coda
  特に読むべき情報はないだろう, identica.

⚠️⚠️ **E in tre casi su sei il genere italiano avrebbe rotto l'identita'.** Le
sette tombe non sono tutte tombe — `:120005` e' un **tumulo**, maschile — e le
armi non sono gli archi. La frase condivisa e' scritta **senza genere** apposta:
«non conviene nemmeno pensare di provare a sollevare una cosa simile», «e mai a
pezzo singolo». Scriverla al femminile avrebbe prodotto sei rese uguali e una
diversa, cioe' esattamente il difetto che il lotto 024 ha dovuto disfare.

### ⭐⭐ LA SESTA FONTE: UNA FRASE DI QUESTO LOTTO E' GIA' RESA NEL LOTTO 028

`:121136` (la libreria di pregio) e `:121198` (la cassettiera di pregio)
portano la formula
その道のプロが精魂込めて作り上げた… 一見シンプルに見えるが、普段見えない部分に匠の遊び心が隠れている,
che e' **parola per parola** quella di `:87505`, la credenza di pregio del lotto
028 — la riga a cui l'inglese aveva buttato via proprio quella seconda frase. Le
due rese nuove ricalcano quella: «costruita con tutta l'anima da chi è maestro
del mestiere» e «si nasconde l'estro dell'artigiano».

💡 `_gia-reso.py` **non** l'ha trovata, e non e' un difetto della rete: cerca la
prosa **intera**, e qui coincide solo la seconda frase su due. La rete trova le
righe gemelle, non le frasi gemelle. L'ha trovata `_cerca.py` cercando a mano
匠の遊び心.

### ⭐ I TERMINI CERCATI A MANO

    狂戦士     -> berserker        (`db_creature.hsp`; ma qui il giapponese
                                   dice 戦士 e basta: «guerriero»)
    匠の遊び心 -> l'estro dell'artigiano   (`db_item.hsp:87505`, lotto 028)
    燭台       -> candelabro       (`db_item.hsp:120698`, indice 3)
    売約済み   -> «è già venduto»  (`db_item.hsp:111697`, lotto 030)

⚠️ Il nome dell'oggetto di `:115382` e' «guerriero furioso statuetta», da
フィギア『狂戦士』 — ma la **descrizione** dice solo 戦士を模した, a immagine di
un guerriero, senza il 狂. La resa segue la descrizione, non il nome.

### ⚠️ L'inglese sbaglia poco, e in piccolo

`:115320` aggiunge una grandezza che il giapponese non ha («so large that they
could easily be mistaken»): 実際の武器と見紛う程 dice solo che si scambierebbe
per un'arma vera, non che sia grande.
"""
