# -*- coding: utf-8 -*-
"""Lotto `command-033`: **togliere l'equipaggiamento e i gesti sulla mappa** —
i tre messaggi di `*com_wear`, la raccolta delle piante e della neve, la
demolizione di un edificio del mondo. Dodici rese, e con queste **la zona
12000-12999 è chiusa**.

⭐⭐⭐ **L'inglese butta via un avviso che protegge il salvataggio, e la resa se
lo riprende.** `:12955` in giapponese è
「本当にこの建物を撤去する？（注意！建物と中の物は完全に失われます）」 — «Demolire davvero
questo edificio? (Attenzione! L'edificio e quello che c'è dentro andranno persi
del tutto)» — e in inglese diventa **«Really remove this building?»**, cioè la
domanda senza la parte che conta. E quel che segue non è reversibile: `:12963`
fa `adata(ADATA_ID, area) = AREA_NONE`, `:12964` `removeworker area`, `:12967`
**salva** (`fmode = 13`, `*game_ctrlFile`). Chi risponde di sì al prompt inglese
non sa che sta perdendo il contenuto, e non può tornare indietro.
✅ È una **statica**: nessun contratto di funzioni, quindi la resa può seguire il
giapponese, come `:4764` nel lotto 030.
⭐ **E il registro non l'ho inventato: c'era già.** `map.hsp:1297` è la stessa
specie — una conferma distruttiva con l'avviso fra parentesi — ed è resa «Vuoi
reinizializzare questa mappa? (Attenzione: può avere conseguenze sulla partita.
…)». Duecentoventidue caratteri, già spediti: la forma «Vuoi …? (Attenzione: …)»
è quella di casa, e il registro del log regge frasi di questa lunghezza.

⭐⭐ **E `init.hsp:1704` decide la persona di tutto il lotto.** `name()` per il
giocatore non è «tu»: è **«il viandante»**, un sintagma di terza persona
maschile. Quindi una frase che interpola `name(cc)` va scritta in **terza**
(`:12795`, «il viandante ha la mente annebbiata…»), e regge identica sul
compagno; una frase che dice «You …» **senza** funzioni va in **seconda**, che è
quel che il progetto fa già da sempre — `action.hsp:3255`, «Usi anche il
passe-partout». Le due persone convivono nello stesso lotto perché a decidere
non è il gusto ma se c'è o no una funzione.

⚠️ **E a `:12795` gli helper da togliere sono due, non uno.** L'inglese è
`name(cc) + " " + is(cc) + " confused and can't change " + his(cc) + "
equipment."`: `is` e `his` a **un** argomento stanno tutt'e due in
`MORFOLOGIA_INGLESE` e se ne vanno. Resta `name`, e `name` soltanto, che è quel
che la rete 11 pretende.

⚠️ **`:12804` è il caso in cui l'inglese sbaglia e la resa non lo può
correggere.** «You unequip …» è in seconda persona, ma `*com_wear` si apre
**anche su un alleato** — lo dimostra `:12795`, che di `cc` fa il soggetto — e
allora non sei tu a toglierti niente. ⚠️ La correzione vorrebbe `name(cc)`, cioè
una funzione che l'inglese non ha: **è la rete 11, e non lascia scampo**. La resa
resta in seconda persona come l'inglese. È un difetto di monte che si eredita, e
va scritto qui perché al collaudo sembrerà un errore di traduzione.

⚠️ **Tre rese su dodici sono accordi evitati**, ed è sempre `itemname()` a
imporlo: «non si può togliere» invece di «non è togliibile», l'impersonale
invece del participio. `itemname(ci)` può essere «la spada» o «il martello».

⭐ Riscosso senza decidere: «Il tuo zaino è pieno.» (`text.hsp:14`, e il gemello
`command.hsp:15708`) e «Troppa stanchezza: il tentativo fallisce!»
(`proc.hsp:3467`). Due su dodici che la rete 3 ha nominato da sola.
"""
