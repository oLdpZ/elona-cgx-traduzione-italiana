# -*- coding: utf-8 -*-
"""Lotto `command-027`: **la bacheca degli avventurieri e la scelta del nome**.
Quindici rese e una rinviata, apre la zona 4000-4999 (76 firme, la più densa).

⚠️⚠️ **Tre voci di questo lotto non sono testo che si legge: sono parole che il
giocatore DIGITA.** `*wish_fix` (`:4325`-`:4337`) ripulisce quel che è stato
scritto nella finestra del desiderio, e `:4334`-`:4336` tolgono dalla stringa il
prefisso «item»/«skill» perché chi scrive «skill fishing» ottenga l'abilità.
✅ Vanno tradotte, perché il desiderio **si risolve in italiano**: `:4883` fa
`s = cnvitemname(cnt2)`, cioè confronta con il nome **tradotto** dell'oggetto, e
`:4332` mette tutto in minuscolo da tutt'e due le parti. Chi scrive «oggetto
spada» deve ritrovarsi con «spada».

⚠️⚠️ **E qui l'accento non si può scrivere, per una ragione che non è quella di
sempre.** Di solito l'accento si scrive vero nel dizionario e `accenti.py` lo
degrada in build: «abilità» diventerebbe «abilita'». Ma questa stringa non deve
**apparire**, deve **coincidere con quello che il giocatore batte sulla
tastiera** — e in CP932 la `à` non esiste, quindi nessuno può digitarla. Un
`del_str(inputlog, "abilita'")` non aggancerebbe mai niente.
✅ La resa è «abilita» **senza accento**, e non è un refuso: è l'unica forma che
il campo di input può contenere. 💡 È il rovescio esatto della regola degli
accenti: là l'apostrofo è come si scrive un accento che il carattere non ha, qui
l'accento non va scritto affatto perché la stringa non è testo da leggere.

⚠️⚠️ **Una rinviata, e la rete che la impone ha ragione in generale e torto qui.**
`:4335` e `:4336` sono la **stessa** `lang("スキル", …)` con due inglesi diversi —
«skill » con lo spazio e «skill» senza — e servono in quest'ordine: il primo
`del_str` porta via anche lo spazio, il secondo prende il caso senza. La rete 4
raggruppa per giapponese e pretende **una resa sola**, e in generale è quel che
deve fare (nel lotto 024 ha giustamente legato le due 「いらん」). Qui no: a
distinguerle non è il senso, è uno **spazio**, e il giapponese non ne ha bisogno
perché il ramo giapponese gli spazi li ha già tolti a `:4328`.
✅ Rinvio + toppa, la forma della 46ª: `:4336` prende la resa «abilita», `:4335`
esce dal dizionario e la toppa ci scrive «abilita ». ⚠️ **Senza, il taglio
lascerebbe uno spazio in testa**, e `:4887` fa il punteggio sui **prefissi** di
`inputlog`: con uno spazio davanti i prefissi diventano « », « s», « sp», e la
ricerca dell'oggetto si sfalda.

⚠️⚠️ **E la scoperta grossa di questo lotto è quello che NON si può tradurre.**
Da `:4481` a `:4780` il desiderio si risolve con una cinquantina di
`if ( inputlog == "lulwy" | inputlog == "ルルウィ" )`: gli dèi, le classi, le
razze, «money», «youth», «alias», «merry christmas». **Sono letterali nudi fuori
da `lang()`**, quindi il dizionario non li tocca — e la rete 7 ha ragione a
chiamarli operandi di confronto e non testo. La conseguenza però è che
**l'italiano può desiderare un oggetto o un'abilità in italiano, ma un dio, una
classe o una razza solo in inglese**. Non è un difetto della traduzione: è come
è fatto il gioco, e va scritto perché al collaudo non sembri un guasto.

⭐ Riscosso senza decidere: «Ignoto» per 不明 (`chara_func.hsp:172`,
`text.hsp:2969`). ⚠️ La rete 3 segnalerà anche `action.hsp:2608`, «classe
ignota»: lì il giapponese identico sta dentro una frase più lunga sulla classe,
qui è il nome di un luogo che la mappa non conosce. Restano due cose diverse.

💡 **Le larghezze di questa schermata non le misura nessuno strumento.**
`display_topic` (`module.hsp:4364`) scrive a `x + 26` con carattere in grassetto
da 10, e le tre colonne partono da `wx + 28`, `wx + 290` e `wx + 420` in una
finestra da 640. La colonna di mezzo ha quindi **104 pixel** e l'inglese
«Message(Impress)» ne prende già più di così — la sottolineatura di `:4372` è
lunga `strlen * 7 + 36` e sconfina nella colonna dopo. La regola qui è quella dei
siti non misurati: **mai più lunghi dell'inglese**. «Fama(amicizia)» sta in
quattordici, «Messaggio(amic.)» in sedici come l'inglese.
"""
