# -*- coding: utf-8 -*-
"""110a - Lotto 006 di `db_item.hsp`: il rapporto degli SCARTI.

`FILTER_JUNK`, `description(3)`: **97 righe del sorgente, 81 firme**. Sedici
righe portano una firma che un'altra riga ha gia' — i tre materium (superiore e
normale hanno lo stesso giapponese), i **dodici** materiali della sintesi, la
spada del teschio e il cesto vuoto — e una resa le copre tutte.

### ⚠️ `FILTER_JUNK` non e' una categoria, e' il cassetto degli avanzi

Le altre categorie dell'indice 3 sono famiglie: il cibo sazia, la pergamena si
legge, il mobile si usa. Qui dentro ci sono **sei famiglie vere** — i lanciabili,
i nove strumenti degli dei, le tre perle ricurve, i materiali, le ossa, i cesti
— e una ventina di solitari che non somigliano a niente. La formula della 108a
regge lo stesso, perche' la formula non descrive la categoria: descrive il
**referto**.

### ⭐⭐ DUE RESE DECISE LEGGENDO IL CODICE, E IL TESTO NON BASTAVA

- **`:59793`, l'ohuda: cancella UN potenziamento, non «i» potenziamenti.** Il
  giapponese scrive 「バフを消去する御札だ。」 e il numero non lo dice — il
  giapponese non lo deve dire, l'italiano si'. `action.hsp:752-766` scorre i
  potenziamenti, chiama `delbuff` sul primo che trova e poi **`break`**: ne
  cancella uno solo. L'inglese («erases buffs») avrebbe portato al plurale.
- **`:63586`, 「態勢を崩す」 e' la ROTTURA GUARDIA del gioco.** L'inglese dice
  «disorientates opponent», che non e' un termine e non aggancia niente.
  `action.hsp:745` chiama `chara_guardbreak tc, 15`: e' il meccanismo, e il
  dizionario ha gia' la parola — «Rottura guardia» (`command.hsp`), «Abbassa la
  rottura guardia». La resa usa il termine. ⭐ E lo stesso termine torna a
  `:47152`, il fischietto, dove il giapponese lo scrive per esteso
  (「ガードブレイクゲージ」): due righe lontane che ora dicono la stessa cosa
  con la stessa parola.

⚠️ Nessuna rete poteva vedere ne' l'una ne' l'altra: guardano forma, inglese di
monte e dizionario, e qui la fonte era il **comportamento del gioco**.

### ⚠️ TRE RIGHE DOVE L'INGLESE RACCONTA E IL GIAPPONESE NO

E' la regola di `decisioni.md`, «Quando l'inglese aggiunge un fatto», la stessa
che nella 108a ha taciuto le sette aggiunte del cibo:

  `:48738`  la cicala — 「死にかけのセミだ。」, *una cicala moribonda*. L'inglese
            racconta che spaventa chi colpisci. Il **nome dell'oggetto e' gia'**
            «cicala morente»;
  `:116668` la ciotola — l'inglese cita Laozi, «the empty space which makes the
            bowl useful, and it's full already». Il giapponese dice soltanto che
            dentro c'e' qualcosa, ed e' la meta' del paio con `:116730`, la
            ciotola vuota: reso quello, l'altro si legge;
  `:46013`  il fukagurumi — l'inglese aggiunge «Worth less than you think», il
            giapponese ha **solo la coda**: 「何度でも使用することができる。」.
            La resa e' la coda e basta, «Si puo' usare sempre.».

### ⓘ Una riga senza giapponese

`:89761`, l'esca: `description(3)` giapponese e' **vuota**, e l'inglese e' l'unica
fonte che c'e'. E' la prima dell'indice 3 in questo stato.

### ⓘ Le formule del lotto

    〜の時に自動で使うアイテムだ。 -> Un oggetto che si usa da se' quando ...
    投げてぶつけると〜を放つ〜だ。 -> Un ... che, lanciato, sprigiona ...
    投げてぶつけると〜爆発を起こす -> ... fa un'esplosione ...
    合成用のアイテムだ。           -> Un oggetto per la sintesi.   (12 firme)
    〜中間素材だ。                 -> Un materiale intermedio ...  (3 firme)
    所持していると〜勾玉だ。       -> Una perla ricurva: portandola, ...

⚠️ **La testa cade due volte**, per la regola della 108a: `:86738` («Portato
addosso, alza le probabilita' di dominare i mostri.») e `:69391` («Si usa da se',
sempre, quando accarezzi il bestiame.»). Il fatto riempiva i 69.

### ⚠️ Una resa che non poteva concordare col giocatore

`:66012`, la magaqua: 「所持していると濡れ状態になる勾玉だ。」. «ti tiene
bagnato» concorda col **genere del giocatore**, che non si conosce
(`guida-stile.md`, e la rete dei participi di `referti.py`). Reso con
l'impersonale: «portandola addosso, ci si bagna».

### ⓘ I termini del lotto, tutti verificati nel dizionario o nel sorgente

ガードブレイク → «rottura guardia» · 主従度 → «grado di sottomissione» ·
バフ → «potenziamento» (「全体バフ消去」 → «cancella tutti i potenziamenti») ·
支配 → «dominare» (`chat.hsp`, ed e' la battuta che regala **questo** oggetto) ·
合成用アイテム → «oggetti per la sintesi» (`chat.hsp`) · 勾玉 → «perla ricurva»
(`invariati.md`) · ラムネ → «gazzosa» · 電撃 → «fulmine» · 冷気 → «gelo» ·
暗黒 → «oscurita'» · 毒 → «velenosa» · 神経 → «neurale» (`glossario.md`) ·
学習書 → «libro di studio» · 戦術指示 → «ordini tattici» · 士気 → «morale» ·
調教 → «addestrare» · プラチナ → «platino» · 疫 → «pestilenza» ·
ペット → «compagno» (109a) · スキル → «abilita'».

### ⓘ `子宝` non era nel dizionario, e l'ha deciso `description(0)`

`:66326`, l'E.G.G: 「子宝だ。」 in due caratteri. La descrizione lunga dello
stesso oggetto (`db_item.hsp:66317`) dice che e' la capsula che la cicogna porta
**agli sposi**: e' la benedizione dei figli, non un tesoro qualunque, e la
categoria giapponese ＜秘宝＞ non basta a dirlo. Reso «Il dono dei figli.».
"""
