# -*- coding: utf-8 -*-
"""110a - Lotto 011 di `db_item.hsp`: il rapporto dei GRIMORI.

`FILTER_ITEM_SPELLBOOK`, `description(3)`: **82 righe del sorgente, 82 firme**,
79 giapponesi distinti. E' la seconda categoria dell'indice 3 per grandezza fra
quelle rimaste, e la terza per formulaicita' dopo le bacchette e i contenitori.

    〜を唱える為に必要な本。読むことができる。 -> Un libro per ... Si può leggere.
    〜を唱える為に必要な本だ。                 -> Un libro per ...   (senza coda)

### ⚠️⚠️ IL RANGO NON SI SCRIVE, E LA PROVA E' POSITIVA

**Ognuno degli 82 inglesi apre con «Book of Rank N Magic»**, e il giapponese non
lo dice mai — non su una sola delle 82 righe. E' l'aggiunta dell'inglese piu'
sistematica trovata finora in questo file: non una riga qua e la', ma una
colonna intera.

Si tace, e non perche' «la regola dice cosi'». Vale il controllo della 109a, che
trasforma la regola in un argomento: **questo file, altrove, dice la cosa che
l'inglese aggiunge?** Si' — `db_item.hsp` scrive 「（ランクN）」 quando vuole
dirlo, su **tutti** i letti e su **tutti** i fornelli. Il rango si sa dire; qui
l'autore ha scelto di non dirlo, ed e' la stessa scelta dei quattro strumenti
musicali.

ⓘ E il rango di una magia il giocatore lo legge nella lista degli
incantesimi, non nella scheda dell'oggetto.

### ⭐ LE TRE CLASSI DI MAGIA, che in italiano si leggono in scala

    〜属性の矢       -> una freccia ...        (12 firme)
    〜属性のボルト   -> una saetta ...         (12 firme)
    〜属性の範囲魔法 -> una magia ad area ...  (12 firme)

Trentasei righe su 82 sono questa griglia: **tre classi per dodici elementi**, e
il giapponese la scrive con la stessa frase cambiando due caratteri. In italiano
le tre teste sono tutte **femminili** — freccia, saetta, magia — quindi
l'aggettivo dell'elemento e' lo stesso in tutt'e tre le righe della colonna, e
la griglia si legge per righe e per colonne.

⭐ **I nomi degli elementi non sono stati scelti**: `skill.hsp` ha gia' tutta la
famiglia delle saette — gelo, fuoco, fulmine, d'oscurita', mentale,
d'oltretomba, velenosa, sonora, caotica, dei nervi, magica, d'acqua — ed e' la
famiglia che la 90a aveva riallineato quando `db_item.hsp` diceva «dardo».
Qui le altre due classi si agganciano a quella.

⚠️ **Un'eccezione dentro la griglia, e sta scritta qui perche' e' voluta.**
`:84516` e' 魔法属性 nella classe ad area, e «una magia ad area **magica**» e'
una parola che si morde la coda. Reso «arcana», che `glossario.md` da' come
sinonimo pieno di 魔法 (la riga «`冷気` gelo/ghiaccio, `暗黒` d'oscurita'/oscuro,
… `魔法` magica/arcano»). Sulla **saetta** (`:84443`) e sulla **freccia**
(`:114016`) resta «magica», perche' li' i nomi degli oggetti lo dicono —
«saetta magica grimorio», «freccia magica grimorio».

### ⚠️ LA CODA C'E' O NON C'E', E NON E' UNA SVISTA DA RIPARARE

Cinquantasei righe chiudono con 「読むことができる。」 e ventisei con
「…必要な本だ。」 e basta. Un grimorio si legge sempre, quindi la differenza non
e' un fatto di gioco: e' come e' stato scritto il file.

Si segue il giapponese **riga per riga**. ⭐ E il conto torna da solo: **tutte le
righe lunghe stanno fra quelle senza coda** — i tre grimori degli attributi, le
due resistenze abbassate, l'oracolo, la contingenza — e ci stanno nei 69 proprio
perche' non devono portarsi dietro i diciassette caratteri di «Si può leggere.».
Aggiungere la coda «per uniformita'» avrebbe sfondato il tetto su almeno sei
righe.

### ⓘ Due righe dove il giapponese e l'inglese non dicono la stessa cosa

- **`:105304`, la luce sacra**: il giapponese dice 「**自らの**呪いを一つ打ち消す」,
  *toglie una maledizione a se stessi*; l'inglese dice «It dispels one hex from
  **nearby people**». La gemella `:105231` (pioggia sacra) dice 自らの in
  giapponese e «on the user» in inglese, cioe' l'inglese li' e' d'accordo: e' la
  riga della luce sacra a essersi mossa. Vince il giapponese.
- **`:78730`, la ricetta**: non e' un libro, e' 「紙」, e non si legge — si **usa**
  e si consuma, 「使用することができる（使い捨て）」. E' l'unica riga del lotto
  con la coda della 108a invece di quella dei libri, ed e' anche l'unica che non
  parla di una magia.

### ⓘ I termini, verificati nel dizionario

Le sigle dei tre grimori degli attributi vengono dalle **righe di potenziamento**
degli stessi tre incantesimi (`buff.hsp`), che il dizionario ha gia':
「耐久・魅力を10%と上昇/耐麻痺/耐盲目」 → «Cos e Car +10% … Res+ paralisi,cecità»,
「筋力・器用…/耐恐怖/耐混乱」 → «For e Des … Res+ terrore,confusione»,
「感覚・意志…/耐睡眠/耐混乱」 → «Per e Vol … Res+ sonno,confusione». La scheda
dell'oggetto e la barra dello stato adesso usano le stesse sei sigle e le stesse
cinque parole.

★ → «artefatti» (`glossario.md`, 108ª: le stelle non si scrivono, si scrive quel
che significano) · 呪い → «maledizione» · 鈍足 → «rallentare» ·
加速 → «accelerare» · 沈黙 → «silenzio» · 蜘蛛の巣 → «ragnatela» ·
テレポート → «teletrasporto» · 鑑定 → «identificare» · `HP`, `PV`, `DV`
invariati.
"""
