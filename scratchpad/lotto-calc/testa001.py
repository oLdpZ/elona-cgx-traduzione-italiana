# -*- coding: utf-8 -*-
"""Lotto fase4-calculation-001: il vortice di mana, la sete e la fame, i
recuperi di stato (calculation.hsp, tutto il file).

44 rese, e **`calculation.hsp` si chiude in un lotto solo**: e' il quattordicesimo
file al 100% e il **quindicesimo dei 54 con `lang()` ad avere un dizionario**.
Il file non era in nessun elenco nominato — `SPEC.md` §6 lo copre con la
designazione collettiva «i restanti 63 file `.hsp` minori» — ed e' entrato per la
stessa ragione di `chara_func.hsp`: `stands up` e `released from bind` erano nel
**collaudo della 39ª**, fra le righe inglesi rimaste nel log.
✅ Con questo, **le tre fonti inglesi dello screenshot sono tutte chiuse**:
`proc.hsp` (39ª), `chara_func.hsp` e `calculation.hsp` (40ª).

⭐ **Sette rese su quarantaquattro erano gia' scritte, e `dossier.py` le ha
pescate tutte e sette per GIAPPONESE.** «si libera dalla costrizione»
(`action.hsp:9515`), «torna in se'» (`chara_func.hsp:3884`), «se la fa addosso»
(`chara_func.hsp:3377` e `:8317`) e i **quattro versi dello stimolo** —
「そわそわ」, 「身をよじって」, 「必死におしっこを我慢」, 「微かに震えながら」 —
che stanno a `proc.hsp:6926`-`:6935` parola per parola. 💡 E' il rovescio esatto
del lotto 005 di ieri: li' otto rese gia' decise erano **invisibili** al dossier
perche' il termine stava dentro una frase piu' lunga; qui sette frasi **intere**
coincidono e lo strumento le trova tutte. Lo stesso strumento, i due estremi, in
due giorni.

⚠️⚠️ **`:1556` e' la seconda «`:26940`» del progetto: il TIPO della voce decide
la resa, non il senso.** `lang(name(cc) + "は奇妙な力に捻じ曲げられた！", "A
dimensional door opens in front of you.")` — il ramo **giapponese nomina** il
personaggio, quello inglese no, e `estrai.py` classifica sul ramo che la resa
sostituisce. Quindi la voce e' **statica**, la resa e' testo nudo, e **non puo'
portare il nome** per quanto il giapponese ce l'abbia. ✅ Resa impersonale sul
fatto, che il codice conferma: due righe sotto c'e' `efid = SKILL_SPELL_TELEPORT`,
quindi la forza strana e' un teletrasporto — «Una forza strana distorce lo
spazio!» ⚠️ **E l'inglese di monte qui non e' un errore, e' una riscrittura
completa**: parla di una porta dimensionale che si apre davanti a te, cioe' di
un'altra immagine. Reso sul giapponese, come sempre.

⚠️ **`:1821` e `:1854` sono un inglese solo per due giapponesi, e la rete 13 li
prende.** «`X is weakened.`» sta per 「瘴気の**毒で**弱くなった」 — il **veleno**
del miasma — e per 「瘴気に**蝕まれて**弱くなった」 — il miasma che **corrode**.
Il codice li separa col colore: `COLOR_LIGHT_GREEN` il primo, `COLOR_BLUE` il
secondo. ✅ «Il veleno del miasma indebolisce X» e «Il miasma consuma X e **ne**
fiacca le forze». 💡 E il secondo ha chiesto il **`-ne` enclitico** della 37ª,
perche' «lo indebolisce» e «indebolirlo» portano tutt'e due un clitico che
concorda.

⚠️ **I quattordici gradini della sete e della fame sono a coppie e a terne, e
vanno letti come una scala.** `:1689`/`:1732` (il pericolo), `:1693`/`:1736`
(il capogiro), `:1697`/`:1740` (il fastidio): tre soglie per due bisogni, con due
o **tre** varianti pescate a caso. ✅ Rese in seconda persona come tutto il resto
del giocatore, e la scala si sente: «Hai la gola arsa» → «La sete ti fa girare la
testa…» → «Di questo passo la disidratazione ti stenderà!»
💡 E l'ultima variante di ognuna delle due terne e' una **domanda al giocatore**
— 「さて何を飲もうか。」 — che l'italiano rende meglio con l'impersonale: «E
adesso, che si beve?»

⚠️ **`:1511` e `:1972` sono due genitivi, e la strada e' quella dei ventidue di
resistenza del lotto 002.** «il mana **di** X», «la difesa **di** X» non si
possono scrivere. ✅ Il dativo riflessivo per il primo — «X **si vede
risucchiare** il mana!» — e il verbo per il secondo, «X allenta la guardia».

💡 **Nota su quel che NON e' entrato**: `calculation.hsp:2352` porta
「Forgive me! Forgive me!」, 「P-P-Pika!」, 「You snail!」 dentro un
`if ( jp ) … else`, **fuori da `lang()`**. Sono la scoperta di `else_jp.py` della
34ª — uscite in inglese a schermo durante quel collaudo — e **non hanno firma**:
non entrano in questo lotto e il file resta «100%» lo stesso. Vanno per toppa,
come le 23 righe di `proc.hsp`.
"""
