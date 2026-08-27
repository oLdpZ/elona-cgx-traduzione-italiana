# -*- coding: utf-8 -*-
"""109a - Lotto 005 di `db_item.hsp`: il rapporto del MOBILIO.

`FILTER_FURNITURE`, `description(3)`: **251 righe del sorgente, 218 firme**. E'
la categoria piu' grossa dell'indice 3, e la piu' formulaica: 199 giapponesi
distinti su 218 firme, e sette famiglie che ne coprono da sole trentacinque.

### ⚠️⚠️ Il mobilio e' dove il giapponese TACE e l'inglese INVENTA

Nelle altre categorie l'inglese aggiungeva un fatto ogni tanto. Qui e' la
regola, e le famiglie lo mostrano tutte insieme:

- **le sette tombe** (`:119946`-`:120318`) hanno **un solo giapponese**,
  「とても重い建造物だ。」 — *una costruzione molto pesante* — e sette inglesi
  che raccontano ciascuno una storia: stile Norland, stile Eulderna, la tomba di
  un eroe, «the name is still readable», i fiori per il defunto. Una resa per
  sette firme;
- **le sette sedute** (`:79047`, `:87710`, `:90640`, `:108957`, `:124374`,
  `:124437`, `:125939`): un giapponese, 「座る為の家具。」, e sette inglesi —
  chair, sofa, rare chair, royal chair, stool, everyday chair, small chair. **Il
  tipo di seduta e' gia' il nome dell'oggetto**;
- **i quattro strumenti musicali** (`:68851`, `:68916`, `:68981`, `:74571`): un
  giapponese, 「演奏用の道具。」, e l'inglese ci mette il **rango**.

⚠️⚠️ **Il rango degli strumenti si tace, e non e' una svista.** Il giapponese di
questo file scrive 「（ランクN）」 quando vuole dirlo — lo fa su **tutti** i letti
(`:87322` rango 7, `:110934` rango 3, `:119690` rango 2, e cosi' via) e su tutti
i fornelli. Sugli strumenti musicali non lo scrive. Non e' che il rango non si
sappia dire: e' che li' l'autore ha scelto di non dirlo, e la scelta si segue,
come per i dieci atti dei mezzi della 108a.

### ⚠️⚠️ L'UNICA RIGA DEL PROGETTO DOVE IL GIAPPONESE PERDE, E PERDE CONTRO SE STESSO

**`:66516`, lo zizou** (地蔵, la statua di Jizo). Il giapponese dice
「和風の間仕切りだ。」, *un paravento in stile orientale* — che e' **la stessa
identica frase** di `:87005`, la パーティション. Ma la riga di categoria di
`:66516`, che sta dentro la **stessa stringa giapponese**, dice ＜彫像＞
(*statua*), mentre quella di `:87005` dice ＜家具＞; e l'inglese di `:66516` dice
«austere statue».

Non e' l'inglese contro il giapponese: e' **il giapponese contro se stesso**, e
a decidere e' la sua riga di categoria. E' lo stesso tipo di prova con cui la
razione della 108a ha dato torto all'inglese — una fonte interna che contraddice
il testo. Reso «Una statua austera.»; `:87005` tiene il paravento.

### ⭐ La scala della LUCE, cinque scalini, e in italiano si legge in ordine

Il giapponese grada l'illuminazione con avverbi che in italiano diventano
illeggibili se si traducono uno per uno («illumina un po' debolmente»). La resa
usa un **nome con un aggettivo**, cosi' l'ordine e' visibile a colpo d'occhio:

    常に周囲を照らす。           ->  Illumina sempre intorno.
    常に周囲を明るく照らす。     ->  Illumina sempre di luce viva.
    夜間、周囲を弱く照らす。     ->  Di notte fa una luce fioca.
    夜間、周囲をやや弱く照らす。 ->  Di notte fa una luce un po' fioca.
    夜間、周囲をやや明るく照らす。-> Di notte fa una luce abbastanza viva.
    夜間、周囲を明るく照らす。   ->  Di notte fa una luce viva.

⚠️ «Illumina sempre intorno.» e' **gia' in uso** dalla 108a (il falo',
`:114144`) e dal lotto 004: la scala si aggancia li' invece di ricominciare.

### ⓘ Le altre formule fisse

    座る為の家具。         ->  Un mobile per sedersi.
    眠る為の家具（ランクN）->  Un letto (rango N).
    演奏用の道具。         ->  Uno strumento per suonare.
    観賞用の鉢植えだ。     ->  Una pianta ornamentale in vaso.  (una dozzina di piante)
    観賞用の植物だ。       ->  Una pianta ornamentale.
    その身を映す鏡。       ->  Uno specchio per guardarsi.
    とても重い建造物だ。   ->  Una costruzione molto pesante.
    使用することはできない -> Non si può usare.
    装備することはできない -> Non si può equipaggiare.
    本類を100種類まで…     ->  Ci stanno fino a 100 tipi di libri.
    所持していると自動で使う-> Si usa da sé se lo porti.
    ランクNまでの料理…     ->  Ci si cucinano i piatti fino al rango N.  (dal lotto 004)

### ⚠️ Una parola vietata, e non dalla lunghezza

`:89215`, il portale del santuario: 「異国の神を迎える門だ」 chiede *gli dèi
stranieri*, e **«dèi» porta l'accento in mezzo alla parola** — a schermo
diventa «de'i». E' la lezione della 41a, misurata sul dizionario nella 71a. Si
evita la parola: «le divinità straniere».

### ⓘ I termini che il lotto porta, verificati nel dizionario

魔導船 → «nave magica» (`chat.hsp`) · ガシャポンの玉 → «sfera del tesoro» ·
狂戦士 → «berserker» · 主能力 → «attributi base» · おひねり → «mance» ·
友好度 → «la simpatia» · ショウルーム → «sala d'esposizione» ·
木の実 → «frutti a guscio» (glossario della 108a) · ランク → «rango».
"""
