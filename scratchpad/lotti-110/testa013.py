# -*- coding: utf-8 -*-
"""110a - Lotto 013 di `db_item.hsp`: il rapporto delle armi a DISTANZA.

`FILTER_RANGE`, `description(3)`: **56 righe del sorgente, 55 firme**, 53
giapponesi distinti. Come le armi da mischia del lotto 012, nessuna formula: un
vocabolario, e una scala.

### ⭐ LA SCALA DELLA GITTATA, quattro scalini e una parola sola

Il giapponese grada quanto un'arma da fuoco perde con la distanza usando sempre
**減衰**, *il calo*, e cambiando solo l'avverbio. In italiano tradotti uno per
uno darebbero quattro frasi che non si confrontano: la resa li mette in fila con
lo stesso verbo, cosi' l'ordine si vede leggendoli di seguito.

    遠距離でも安定した威力     -> tiene la forza anche a distanza  (:76392)
    距離による減衰が殆どない   -> con la distanza non cala quasi   (:96713)
    距離による減衰が少ない     -> con la distanza cala poco        (:115799)
    距離によって威力が減衰する -> con la distanza perde forza      (:127141)

E' la stessa mossa della **scala della luce** della 109a (cinque scalini, un
nome piu' un aggettivo) e per la stessa ragione: quattro righe che il giocatore
legge in schede diverse, e che devono restare confrontabili.

ⓘ Accanto ci sta `:97806`, 有効射程が短い, che non e' della scala — parla della
**gittata utile**, non del calo — e infatti dice un'altra cosa: «porta poco
lontano».

### ⚠️ DUE MITRAGLIATRICI, DUE MODI DI DIRE «MOLTO PESANTE»

`:77148` e' 非常に重い e `:77916` e' とても重い. Sono due giapponesi distinti,
quindi due rese distinte: **«pesantissima»** e **«molto pesante»**. Renderle
uguali sarebbe stato piu' liscio e avrebbe cancellato una differenza che il
sorgente scrive.

⚠️ **E il contrario e' altrettanto vero**: `:68185` e `:117188` hanno lo
**stesso** giapponese (「投擲用武器だ。」) e due inglesi diversi — «Difficult to
use. Hurt as hell when hit.» contro «It is just a stone.». Stessa resa. E
`:72354`, `:74238`, `:83345` sono **tre** righe con un giapponese solo: una resa
per tre.

### ⓘ Il vocabolario, dai nomi degli oggetti

弩/クロスボウ «balestra» · 弩砲 «balista» · 連弩 «arco a ripetizione» ·
短弓 «arco corto» · 長弓 «arco lungo» · 機械弓 «arco meccanico» ·
銃器 «arma da fuoco» · 拳銃 «pistola» · 双銃 «pistole gemelle» ·
狙撃銃 «fucile di precisione» · 散弾銃 «fucile a pompa» ·
機関銃 «mitragliatrice» · 光子銃 «pistola laser» · 手榴弾 «granata» ·
手裏剣 «shuriken» (`invariati.md`) · 投擲用武器 «arma da lancio».

### ⚠️ 風の神 e' una DEA, e a dirlo non e' il giapponese

`:86070`: 「風の神から下賜される長弓だ。」. Il giapponese scrive 神, che non ha
genere; l'inglese scrive «Goddess of Wind»; e Lulwy e' una divinita' femminile.
L'italiano il genere lo deve scegliere, e lo sceglie come lo ha gia' scelto
**questo stesso file**: 「風の女神の写真集」 e 「風の女神を模った彫像」 sono resi
«la dea del vento» da sessioni precedenti. Reso «la dea del vento».

ⓘ La gemella `:86000`, 機械の神, e' «il dio delle macchine» per la stessa strada
(「機械の神を模した目覚まし時計」).

⚠️ **Non e' un caso isolato ma il seguito del lotto 012**, dove le cinque armi
degli dei hanno preso i nomi dalle statue e dai pendoli. Sette righe in due
lotti, e nessuna ha avuto bisogno di una decisione nuova.
"""
