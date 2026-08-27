# -*- coding: utf-8 -*-
"""110a - Lotto 012 di `db_item.hsp`: il rapporto delle ARMI.

`FILTER_WEAPON`, `description(3)`: **105 righe del sorgente, 105 firme, 105
giapponesi distinti**. Zero doppioni, zero famiglie, zero formule: e' la
categoria **meno** formulaica dell'indice 3, e l'unica dove il numero delle
righe e quello delle rese coincidono.

### ⓘ Che cos'e' un rapporto quando non c'e' una formula

Le altre categorie hanno una frase che si ripete e un fatto che cambia. Qui il
giapponese scrive, per ognuna delle 105, **che arma e'** e **una cosa sola** su
di lei — una forma, un materiale, un potere, una storia. E' un referto lo
stesso: la struttura c'e', ma sta nella **sintassi**, non nel lessico.

    〈una cosa sola〉 + 〈il tipo d'arma〉だ。

L'italiano tiene lo stesso ordine rovesciato che ha sempre — «Un'ascia da
battaglia che pare fatta d'osso» — e ogni riga sta in una frase.

### ⭐⭐ IL VOCABOLARIO DELLE ARMI NON SI E' DOVUTO INVENTARE

Trentatre parole di tipo d'arma, e c'erano **tutte** nei nomi degli oggetti,
resi in sessioni precedenti. La ricerca e' costata un comando; inventarle
avrebbe prodotto un rapporto che chiama «spadone» quel che il nome chiama
«spada lunga»:

    長剣 spada lunga · 短剣 pugnale · 大剣 spadone · 細剣 fioretto · 刀 katana
    忍刀 wakizashi · 海賊刀 scimitarra · 大斧 ascia lunga · 戦斧 ascia da
    battaglia · 手斧 accetta · 投斧 tomahawk · 鎌 falcetto · 大鎌 falce ·
    骨鎌 falce d'ossa · 鎖鎌 falce a catena · 鋏鎌 cesoie · 長槍 lancia ·
    鉾槍 alabarda · 三叉槍 tridente · 騎士槍 lancia da cavaliere · 棍棒 randello
    大槌 martello · 戦槌 martello da guerra · 星球槌 mazza ferrata · 杖 bastone
    長棒 bastone lungo · 錫杖 shakujo · 節棍 nunchaku · 鞭 frusta ·
    螺旋機 trapano · 鎖鋸 motosega · 包丁 coltello da cucina · 苦無 kunai

⚠️ **E il tipo d'arma va letto nel giapponese, non nel nome.** `:52720` e'
un budino di mandorle a forma di spada laser, e il giapponese dice
「長剣として装備可能」: si impugna come **spada lunga**. `:67533` e' un
大太刀 e il giapponese si prende la briga di avvertire che
「刀だが大剣に属する」 — *e' un katana, ma sta fra gli spadoni*. Due righe dove
la categoria di gioco e la forma dell'oggetto non coincidono, e il giapponese lo
dice apposta.

### ⭐ LE CINQUE ARMI DEGLI DEI, e le divinita' erano gia' decise

`:85645`, `:85717`, `:85788`, `:85860`, `:85930`:
「〜の神から下賜される〜だ。」 — il martello, il pugnale, la lancia, il bastone
e la falce che le cinque divinita' concedono. I nomi delle divinita' stanno
**nello stesso file**, dalle statue e dai pendoli resi prima:

    大地の神     -> il dio della terra        (「大地の神を模したペンデュラム」)
    収穫の神     -> il dio del raccolto       (「収穫の神のぬいぐるみ」)
    元素の神     -> il dio degli elementi     (「元素の神を模した胸像」)
    幸運の女神   -> la dea della fortuna      (「幸運の女神を描いた絵」)
    癒しの女神   -> la dea della guarigione   (「癒しの女神を模った彫像」)

⚠️ **Non sono gli epiteti.** Il dizionario ha anche «Jure della Cura»,
«Ehekatl della Sorte», «Kumiromi della Messe»: quelli sono **nomi**, e si usano
dove il giapponese scrive il nome. Qui il giapponese scrive la **perifrasi**
(癒しの女神, *la dea che guarisce*), e la perifrasi ha gia' la sua resa in
questo stesso file. Confondere le due avrebbe fatto dire alla scheda «donata da
Jure della Cura» dove il giapponese non nomina Jure.

### ⓘ Tre righe dove l'inglese aggiunge e il giapponese no

- `:53911`, la spada leggerissima: l'inglese aggiunge «with electric
  properties», il giapponese dice solo 「非常に軽くて細い剣だ。」;
- `:66843`, il pugnale che suona: l'inglese precisa «Rank 0-6 instrument», il
  giapponese dice 「一応、楽器としても使える」 — *volendo, vale anche da
  strumento*. E' il **rango taciuto** della 109a e del lotto 011, per la terza
  volta;
- `:117463`, il pugnale del tuono: l'inglese dice «wind and lightning», il
  giapponese solo 雷.

### ⓘ I termini, verificati nel dizionario

クリティカル → «colpi critici» (`buff.hsp`, «Ottiene più colpi critici») ·
主能力 → «attributi base» (109ª) · マナ → «mana» (`invariati.md`) ·
地獄 → «oltretomba» · 混沌 → «caos» · `MP` invariato.
"""
