# -*- coding: utf-8 -*-
"""111a - Lotto 022 di `db_item.hsp`: il rapporto dei GUANTI.

`FILTER_GLOVES`, `description(3)`: **10 righe del sorgente, 10 firme**, 10
giapponesi distinti.

### ⭐ DUE PAROLE PER LA MANO, E I NOMI LE HANNO GIA' DIVISE

    篭手   -> guanti d'arme   (合成篭手 «guanti d'arme compositi», 重層篭手
                               «guanti d'arme a piastre», 厚篭手 «guanti
                               d'arme spessi»)
    手袋   -> guanti          (軽手袋 «guanti leggeri», e la voce 手袋 «guanti»)

⚠️ E' la stessa forma di 鎧/アーマー nel lotto 015 e di 兜/帽子/ヘルメット nel
017: il giapponese distingue, i nomi italiani hanno gia' scelto, e la
descrizione segue i nomi.

### ⭐⭐ `:75717` — 絶器, IL «ZEKKI», RESTA

「絶器と呼ばれる篭手だ」: 絶器 non e' nel dizionario, non e' in `glossario.md`
e **l'inglese lo traslittera** («These are gloves that is called a 'zekki'»),
invece di scioglierlo. E' un termine coniato di Elona+, come i nomi dentro le
marche 《》 di `invariati.md`. Si tiene: «Dei guanti d'arme detti zekki».

⚠️ **Senza virgolette basse**: la rete dei caratteri sconosciuti ha bocciato il
lotto perche' CP932 **cancella** « e », e la resa sarebbe arrivata a schermo con
la parola nuda comunque, ma senza che nessuno lo sapesse.

⚠️ **Quando l'originale traslittera, non sta descrivendo**: e' la regola che
`invariati.md` scrive per `<Saber Tonfa>` e `<Mournblade>`, e qui vale dentro
una descrizione invece che dentro un nome. Da aggiungere a `invariati.md`.

### ⭐ 貫通 E' GIA' «PERFORA»

`:107530` e' 貫通能力に長けた篭手だ, e il gioco ha gia' 貫通 -> «perfora» nella
colonna dei danni, 貫通弾 «munizioni perforanti» e «Se piazzi un colpo che
perfora» in `chat.hsp`. Quindi «Dei guanti d'arme bravi a perforare».

### ⭐ 連続攻撃 TORNA, E LA RAFFICA E' GIA' A SCHERMO

`:62804` (il Cesto delle Meteore) e' 流星群を思わせる連続攻撃を可能とする腕装備
だ. 連続攻撃 e' gia' «raffica di colpi» nel messaggio d'attacco di
`chara_func.hsp`, e nel lotto 014 il tonfa 連続攻撃ができる e' «che attacca a
raffica». Qui: «raffiche di colpi come uno sciame di meteore».

ⓘ 腕装備 (l'«equipaggiamento da braccio») e' **«bracciale»** tutt'e due le
volte che compare — `:62804` e il dono divino `:75650` — e non «guanti
d'arme», che e' 篭手: sono due parole diverse nel sorgente.
"""
