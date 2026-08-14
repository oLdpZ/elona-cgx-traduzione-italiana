# -*- coding: utf-8 -*-
"""Lotto fase4-init-001: il bottone Ok, l'errore di rete, e i primi quattro
ranghi — arena, arena delle bestie, Nefia, museo (init.hsp, righe 23-358).

46 rese, ed e' il **primo lotto di `init.hsp`**, che e' il file piu' delicato del
progetto: ci stanno le `#defcfunc` che restituiscono inglese fuori da `lang()` —
`he()`, `his()`, `him()`, `gendername()` — e i valori di `CDATAN_NEWSEX`, che
sono **scritti nel salvataggio**. Questo lotto tiene tutto quello, e prende
soltanto la parte che e' testo puro.

⭐⭐ **E' il primo lotto che usa la CHIAVE LUNGA `(riga, en, jp)`**, e il modello
l'ha imparata apposta per questo file: `:358` ha **«Great museum» due volte**,
perche' il giapponese distingue 大人気の博物館 («amatissimo») da
来客の絶えない博物館 («sempre affollato») e l'inglese ha appiattito i due gradini
in uno. Con la chiave corta la rete 0 fermava la zona; adesso le due voci si
dichiarano col giapponese accanto e il lotto passa. Vedi
`scratchpad/modello-chiave-lunga.py`.

⚠️⚠️ **Gli otto ranghi sono scale, e vanno lette come scale.** `rankn(t, c)` e'
un array `11 x 9`: per ogni categoria ci sono **dieci gradini** dal migliore al
peggiore piu' un'**undicesima voce, che non e' un gradino ma il NOME della
categoria**. `ranktitle()` (`:337`-`:351`) restituisce solo gli indici 0-9;
l'indice 10 lo legge `module.hsp:264` per scrivere «Cambio di rango (**Museo**
5° → 4°)». Tradurre l'undicesima come se fosse un titolo di rango — «Novizio»
invece di «Gilda» — e' esattamente l'errore che ha fatto l'inglese di monte.

⚠️⚠️ **La serie degli errori di monte passa da trentanove a quarantatre'**, e
sono tutti e quattro nella stessa famiglia: **l'inglese ha sbagliato gradino**.

- `:358` mette «Great museum» sul terzo gradino **e** sul quinto, e il museo
  perde una distinzione che il giapponese fa;
- `:358` chiama «Unknown **Ruin**» il decimo gradino, dove il giapponese dice
  無名の博物館, «museo senza nome». Non e' una rovina, e' un museo;
- `:357` chiama «Famous tourist» il nono gradino, dove il giapponese dice
  ちんけな遺跡荒らし, «predone di rovine da strapazzo» — cioe' l'inglese ha messo
  un complimento dove il giapponese fa uno sfottò — e chiama «Tomb robber»
  l'ottavo, dove il giapponese dice 探検者, «esploratore»;
- `:356` mette «New hope» sul settimo gradino copiandolo da `:355`, dove il
  giapponese dice ペットの母, «madre delle bestie».

✅ Tutti resi sul giapponese, che e' la regola del progetto dal lotto 019 della
38a.

⚠️ **«Madre delle bestie» non si puo' scrivere, e la ragione e' il giocatore.**
`:356` gradino 7 e' un titolo che il gioco appiccica a **te**, e meta' dei
giocatori sono femmine mentre l'altra meta' non lo e': «madre» sarebbe sbagliato
per gli uni, «padre» per gli altri. ✅ «**Balia** delle bestie»: e' un nome di
**ruolo**, grammaticalmente femminile ma applicabile a chiunque, come «una
guida» o «una spia». E' la strada del nome di genere fisso della 40a («si sente
la **pelle**…») usata su un titolo invece che su un complemento.

⚠️ **Gli accenti dentro la parola sono vietati, e qui e' la prima volta che
conta.** `accenti.py` degrada **ogni** accento in lettera + apostrofo, non solo
quelli finali: «élite» diventerebbe «e'lite» a schermo. Nei ranghi la parola era
la prima che veniva in mente — «gladiatore d'élite» — ed e' stata evitata
ovunque: «Gladiatore **scelto**», «Domatore **scelto**». 💡 Gli accenti finali
vanno benissimo — «piu'», «perche'» — perche' l'apostrofo li' e' quello che
l'italiano scrive comunque.

💡 **I termini di mondo erano tutti gia' fissati altrove**, e nessuno di loro sta
in una frase intera che `dossier.py` possa agganciare: ティリス e' **Tyris**
(`proc.hsp:9996`), イルヴァ e' **Irva** (`text.hsp:2917`), ダンジョン e' il
**sotterraneo** (`action.hsp:2180`), 博物館 il **museo** (`db_item.hsp:145651`),
ペットアリーナ l'**arena delle bestie** (`db_creature.hsp:118259`), 遺跡 le
**rovine** (`text.hsp:3021`). E' di nuovo il caso del `termini.py` che manca.

⚠️ **Una divergenza nuova e legittima: 観光客 e' «il turista» a
`db_creature.hsp:118924` e «Turista» qui.** Li' e' il **nome di una creatura**, e
il contratto dei nomi vuole che porti il proprio articolo; qui e' un **gradino di
rango** che il gioco appiccica al giocatore, e un titolo l'articolo non lo porta.
E' la stessa distinzione di 「痛っ！」 nel lotto `ai-001`: lo stesso giapponese in
due tipi di sito diversi. ⚠️ E come quella, **nessuno strumento la vede**:
`battute --divergenti` legge solo `db_creature.hsp.jsonl`.

⚠️ **Due invariati nuovi, tutt'e due dichiarati in `invariati.md`**: `Ok`
(`:23`, il bottone di `promptOk` — parola italiana identica all'inglese, come
`bonus`) e `Arena` (`:355` gradino 11, il nome della categoria — l'italiano ha
la stessa parola, e viene dallo stesso latino).
"""
