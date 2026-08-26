# -*- coding: utf-8 -*-
"""108a - Lotto 001 di `db_item.hsp`: il RAPPORTO DI IDENTIFICAZIONE dei cibi.

`FILTER_ITEM_FOOD`, `description(3)`: **133 righe del sorgente, 56 firme**. E' il
lotto piu' economico del file, ed e' quello da cui si comincia perche' fissa la
**formula** del rapporto di identificazione, che poi si ripete su tutte le
2.580 firme rimaste.

⚠️⚠️ **E' IL PRIMO LOTTO CHE NON E' UN INTERVALLO DI RIGHE.** Le descrizioni di
una categoria sono sparse per settantacinquemila righe (42.785 -> 117.602),
quindi la zona si dichiara con `RIGHE = {...}`, emesso da
`_107-chiavi-item.py --solo-righe` e non scritto a mano. Il contratto del lotto
— «ogni voce della zona e' resa, ogni resa aggancia una voce» — e' identico, e
lo controllano le stesse reti 1 e 2.

⚠️⚠️ **IL TETTO E' SECCO: 69 CARATTERI, E SI MISURA DEGRADATO.** L'indice 3 non
passa da nessun impaginatore: `command.hsp:16275` fa
`cnven(trimdesc(description(3), 1))`, tronca al primo `#` e mette la riga in
`listn`. Non va a capo, non si taglia: **sfora e basta**. E «perche'» occupa 7
caratteri dove «perché» ne occupa 6, quindi il numero che conta e' quello dopo
`accenti.degrada()`. La rete e' `scratchpad/_107-descrizioni-item.py`.

### La formula, e perche' e' una formula

Il giapponese scrive **la stessa frase** su tutta la categoria — 「満腹度を回復
することができる食物。調理することができる。」 — e cambia solo quando cambia il
fatto. Non e' prosa: e' un referto. L'italiano tiene la forma del referto:

    Un cibo che sazia.                      il caso base
    ... e che si può cucinare.              quando il giapponese lo dice
    Un cibo di mare / Una verdura /         quando l'INGLESE riempie la casella
    Un frutto / Frutti a guscio / Un uovo   della categoria, che e' parte del referto

⭐ **Dove l'inglese, invece di riempire la casella, si mette a raccontare, si
torna alla formula.** Sette righe: il tonno «carnivoro», il salmone «dalle
abitudini di deposizione uniche», il pesce sciabola «che somiglia a un'anguilla»,
la farina «da forno», la pasta «che verrebbe meglio cotta», il cadavere «che si
puo' cucinare in piatti di carne». Il giapponese di tutte e sette e' la formula
generica, e un referto che dice cose diverse per il tonno e per la sardina ha
smesso di essere un referto. E' la regola di `decisioni.md`, «Quando l'inglese
aggiunge un fatto»: si segue il giapponese e si tace l'aggiunta.

### ⭐⭐ Tre difetti di monte che l'italiano ripara gratis

1. **`:115655`, la razione — l'inglese dice il CONTRARIO del giapponese.**
   「調理することができる。」 e' «si puo' cucinare»; l'inglese scrive «it cannot
   be cooked». In gioco la razione **si cucina**. Non e' un'aggiunta: e' una
   negazione.
2. **`:80490`, il mochi — l'inglese ha perso una frase intera.**
   「のどに詰まることがある。」, «certe volte va di traverso», che sulla gemella
   `:80553` (il kagami mochi) l'inglese ce l'ha, in maiuscolo: «CHOKE WARNING».
   I due giapponesi sono identici e adesso lo sono anche i due italiani.
3. **`:113943`, il filoncino — l'inglese ha perso 「調理することができる。」**,
   che il giapponese ha e che le altre righe della stessa forma dicono.

ⓘ **`:60517`, le tre bottiglie del condimento**: il giapponese dice solo
「調味料だ。使用することができる（使い捨て）。」. L'inglese aggiunge che qualcuno
lo versa sul bestiame prima della macellazione — vero in gioco, ma non e' quel
che il referto dice, e nei 69 caratteri non ci starebbe insieme al resto.

ⓘ **`:74301`, il pranzo del ringiovanimento**: «ti riporta all'infanzia» e non
«ti fa tornare bambino», perche' il genere del giocatore non si conosce
(`guida-stile.md`).

ⓘ **I termini gia' fissati altrove, e qui si ubbidisce:** 「エーテル病」 → «la
malattia dell'etere» (`command.hsp:2336` e altre otto), 「狂気度」 → «Follia»
(`command.hsp:10517`), 「運勢」 → «fortuna» (`skill.hsp:64`), 「マナ」 → mana
(`invariati.md:50`), e i nomi d'attributo dal glossario — apprendimento,
carisma, destrezza, percezione, magia, volonta', forza, costituzione.
`alraunia`, `spenseweed`, `mareilon`, `morgia`, `stomafillia` e `curaria` sono
in `invariati.md` e qui non compaiono: il nome dell'oggetto sta altrove, il
referto dice solo che cosa fa.
"""
