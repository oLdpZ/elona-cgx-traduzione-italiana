# -*- coding: utf-8 -*-
"""Lotto `command-016`: le 23 voci finali della zona — le quattro carte, le
reazioni alla frase insegnata, e la notte con chi hai sposato.

Chiude 6000-6999. Dentro ci sono tre cose che non c'entrano niente fra loro e
stanno vicine solo perche' il menu del compagno le raccoglie tutte.

⭐ **I quattro nomi di carta erano gia' decisi, e con l'articolo dentro.**
`db_creature.hsp` rende 「スペード・ウォリアー」 «il guerriero di picche»
(`:38006`), 「クラブフェザー」 «la piuma di fiori» (`:37943`), 「ダイヤアイズ」
«gli occhi di quadri» (`:37880`) e 「ハート・ウィッチ」 «la strega di cuori»
(`:37816`). ⚠️ La rete 3 non li avrebbe pescati — qui il giapponese e' la frase
intera, non il nome — ma `dossier.py` per l'inglese si'.
💡 E «is treated as» non puo' diventare «e' trattato come», che concorderebbe
con la creatura: **«conta come»**, che e' anche la lingua vera dei giochi di
carte.

⭐ **«Il tuo diario e' stato aggiornato.» sta in CINQUE file**, e questo e' il
sesto: `action.hsp:8282`, `chara_func.hsp:3964`, `map.hsp:1197`,
`proc.hsp:4228`, `text.hsp:4`. Copiata parola per parola.

⚠️ **Un errore di monte che ribalta il senso**: `:6901` 「まんざらでもないようだ」
vuol dire «non gli dispiace affatto», cioe' **gli fa piacere**, e l'inglese
scrive «doesn't seem to be very happy about that». La resa segue il giapponese —
«non sembra dispiacersene affatto» — che e' anche la forma senza participio.

⚠️ **Tutta la scena finale ha il giapponese PARLATO e l'inglese DESCRITTO**, e
qui vince l'inglese. `:6939` e' 「「まだ眠くない〜」」, una battuta fra virgolette;
`:6947` e' 「「いやん、あなたったら…」」 e l'inglese lo riduce a «\\*blush\\*»;
`:6998` e' 「「はい…喜んで」」 e diventa «X blushed and nodded!». ✅ Non e' un
appiattimento da disfare: e' che **le battute giapponesi sono costruite con le
funzioni del tono** — `_yo(3)`, `_ga(3)`, `_ore(3)`, `_kure(3)` — che l'inglese
non ha e l'italiano nemmeno. Se rendessi le battute, dovrei inventare un
registro che il gioco non sa scegliere. La descrizione lo evita.

⭐ **E 「ジュア様」 e' «Jure», non «Jua».** L'inglese scrive «Lady Jua», ma il
progetto rende ジュア «Jure» in quattro file — `db_creature.hsp:72943`,
`:72961`, `:100613`, `action.hsp:14058` — che e' il nome canonico della dea
della guarigione. Il 様 cade, come cade gia' in `db_creature.hsp:72943`.

Tetto 61 caratteri (`:6863`). Una copia di giapponese e tre di inglese.
"""
