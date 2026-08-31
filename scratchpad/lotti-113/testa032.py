# -*- coding: utf-8 -*-
"""114a - Lotto 032 di `db_item.hsp`: IL MOBILIO SI CHIUDE.

`FILTER_FURNITURE`, righe 122.000 in su: **54 righe** su 51 oggetti — 51
dell'indice 0 e tre dell'indice 2 (`:122025` <Noel>, `:122157` <Gwen>,
`:127609` <Erystia>). Con questo lotto il **corpo del mobilio e' finito**: 261
righe su 261, dal lotto 027 al 032.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **Le dieci piante in vaso** (`:122023` garofano, `:122085` coda di volpe,
  `:122155` anemone, `:122225` nerina, `:122295` gazania, `:122365` salvia,
  `:122427`, `:122489` rosa banksiae, `:122551`): tutte aprono con 鉢植え, e
  tutte e dieci le rese aprono con «Una pianta in vaso». Due di loro portano
  una battuta appresso — <Noel> sul garofano, <Gwen> sull'anemone — e sono le
  due che il gioco regala.
- **I tre ripiani che si spostano** (`:123866` i vestiti, `:123998` le
  cianfrusaglie, `:124060` la roba di casa): la **seconda frase giapponese e'
  identica** in tutti e tre, e in italiano lo e' altrettanto.
- **Le due tavole della strada** (`:123616` il segnavia, `:123678` l'insegna):
  seconda frase identica, e il testo dice proprio che i due si somigliano —
  類似品に注意, attenzione a non confonderli. Renderle in due modi avrebbe
  disfatto la battuta.
- **La sedia quadrata e lo sgabello tondo** (`:124434`, `:125936`): ciascuno
  nomina l'altro. Le due rese si rispondono parola per parola.
- **La sedia e il letto a buon mercato** (`:124371`, `:125748`): stessa
  formula 比較的安価な材質でできた + 市民の殆どは…ごく一般的な. Le due rese
  hanno la stessa struttura: «È la sedia / il letto comune per eccellenza:
  quasi tutti i cittadini...».
- **I due tavoli da bar** (`:125119`, `:125181`): **prima frase identica**,
  e cambia solo l'aria — losca l'una, da adulti l'altra.

### ⭐⭐ UNA FAMIGLIA ATTRAVERSA IL CONFINE DEL LOTTO

`:125432` (le armature esposte) porta
大きく試着不可と書かれている為、装備することはできない, che e' **la stessa
frase** di `:121446` e `:121508` del lotto **031**. La resa e' identica alle
due gia' scritte: «C'è scritto a lettere grandi che non si può provare, e
perciò non si può indossare».

⚠️ Nessuna rete l'avrebbe visto: `_coerenza.py` confronta le stringhe
**intere**, e queste tre differiscono nella prima frase. E' la lezione della
111a — le altre righe della stessa famiglia, anche se stanno in un altro lotto
— applicata a due lotti scritti nella stessa sessione.

### ⭐ I TERMINI CERCATI A MANO

    スライム       -> la melma           (`db_creature.hsp`)
    ノースティリス -> Tyris del Nord     (`chat.hsp`)
    ティリスの民   -> la gente di Tyris
    メッキ         -> una patina di metallo (non e' nel dizionario)
    飴細工         -> le figurine di zucchero (non e' nel dizionario)

### ⚠️ L'inglese sbaglia poco, e per omissione

`:122023` (il garofano) scrive due volte «modesty» dove il giapponese ha due
parole diverse — 慎ましやか (il fiore discreto) e 謙虚さ (l'umilta' come
virtu') — e la ripetizione fa sembrare la frase una tautologia. `:125057` (la
botte) traduce タル con «tar» invece che «barrel», che e' un refuso di monte.
"""
