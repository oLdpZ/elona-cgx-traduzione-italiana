# -*- coding: utf-8 -*-
"""111a - Lotto 015 di `db_item.hsp`: il rapporto delle ARMATURE del corpo.

`FILTER_ARMOR`, `description(3)`: **20 righe del sorgente, 20 firme**, 20
giapponesi distinti. Il seguito diretto del lotto 014: stesse scale, stesse
parole, e due formule nuove.

### ⭐ TRE PAROLE GIAPPONESI PER «COSA CHE SI INDOSSA», TENUTE DISTINTE

    服     -> vestito     (sei righe)
    鎧     -> corazza     (i nomi lo dicono gia': 軽鎧 «corazza leggera»,
                           輪鎧 «corazza ad anelli», 重層鎧 «corazza a
                           piastre», 厚鎧 «corazza a bande»)
    アーマー / スーツ -> armatura / tuta   (i katakana, cioe' i moderni)
    防具   -> armatura    (:130782, come nel lotto 014)

⚠️ 衣服 e' gia' «vestiti» in questo stesso file (i vestiti sporchi nel cesto):
服 segue quella parola, non i nomi degli oggetti — che sono tutti diversi
(giubbotto, cappotto, veste papale) proprio perche' il giapponese e' generico.

### ⭐ DUE FORMULE, e si scrivono in fila o non si leggono come formule

**「〜ために作られた服だ」, tre righe:**

    銃弾を防ぐために作られた服 -> fatto per fermare i proiettili  (:101382)
    攻撃を防ぐために作られた服 -> fatto per parare i colpi         (:101512)
    法王のために作られた服     -> fatto per il papa                (:101642)

**「〜を束ねて作った鎧だ」, due righe** — 束ねて e' gia' «legando insieme» nel
dizionario (il mostro-occhio che lega insieme nervi e muscoli):

    薄片を束ねて作った鎧 -> fatta legando insieme delle lamelle  (:101707)
    輪を束ねて作った鎧   -> fatta legando insieme degli anelli   (:101837)

### ⭐ LA SCALA DEL PESO E DELLA DUREZZA CONTINUA DAL LOTTO 014

Scudi e corazze usano le **stesse** parole, e le rese devono combaciare o la
scala si spezza a meta' categoria:

    非常に重い  -> pesantissimo/a   (:100720 scudo, :101902 corazza)
    固い        -> duro/a           (:100852 scudo, :101772 corazza)
    分厚い      -> spessa           (:101967), gia' «spesso» nel dizionario
                                     (分厚い魔法書 «libro spesso»)

### ⭐⭐ `:75986` — 拘束具 ERA GIA' «GABBIA», E LA RIGA E' LA GEMELLA DI `:57965`

`chat.hsp` ha gia' 「これは装甲板ではない、拘束具だ。…これを身に着け抑え込む
がいい」 reso **«Questa non è una piastra d'armatura: è una gabbia»** — stesso
verbo (身に着ける), stesso oggetto. Quindi:

    :57965  身に着けると変形して手枷になる   -> si trasforma in ceppi  (lotto 014)
    :75986  身に着けると変形して拘束具になる -> si trasforma in una gabbia

Sono due artefatti gemelli, 《神々の枷鎖》 e 《機械拘束具》, e la coppia si
legge solo se la costruzione resta la stessa e cambia **solo** il nome della
cosa — che e' quel che fa il giapponese.

### ⚠️ 何度でも使用することができる ERA GIA' RESO, PIU' DI OTTANTA VOLTE

`:51643` porta la coda 「何度でも使用することができる。」, che il dizionario
rende **«Si può usare sempre.»**. Non e' una scelta di questo lotto: e' un
ritrovamento, come le cinque code su sei della 110a.

### ⓘ Una parola su 高性能

`:70533` e' 高性能な特殊スーツだ e diventa «ad alte prestazioni». Il lotto 013
rendeva 高性能だが重い光子銃 con «potente, ma pesante»: li' la parola stava in
una coppia contrapposta e «potente» reggeva il contrasto; qui e' sola, e la
tuta non e' potente — e' fatta bene.
"""
