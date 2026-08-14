# -*- coding: utf-8 -*-
"""Lotto fase4-ai-001: il sacco da pugni, il pubblico dell'arena, i compagni che
mangiano e bevono, la canzone rumena (ai.hsp, righe 79-1468).

48 rese, ed e' il **primo lotto di `ai.hsp`**, il file dell'intelligenza
artificiale: quel che gli alleati e i nemici fanno e dicono da soli, senza che il
giocatore lo chieda. E' testo di **log ad alta frequenza** — chi ti segue mangia,
beve, contratta col mercante, si medica — e per questo e' entrato prima di
`init.hsp`, che ha piu' firme (133 contro 94) ma si legge quasi tutto nella
scheda del personaggio.

⚠️⚠️ **L'inglese di monte ha rimescolato le battute in DUE punti, e la serie
degli errori di monte passa da trentasei a trentotto.** Non e' la famiglia del
«personaggio sbagliato» ne' quella della «riga ricopiata»: qui l'ordine dei
`lang()` sulla stessa riga e' giusto, ma le coppie giapponese-inglese **non si
corrispondono**.

- `:472` e' il blocco del **sacco da pugni** (`CHARA_BIT_SANDBAG`), e il
  giapponese lo dice: 「もっとぶって」 e' «picchiami ancora», la battuta del
  masochista che ti ha chiesto lui di essere preso a pugni. L'inglese ci mette
  «`Release me now.`», che e' la battuta del **prigioniero** di `:482` dieci
  righe piu' sotto, e sposta «`Hit me!`» sulla terza, dove il giapponese dice
  「何をする」, «ma che fai?». Due battute su tre finite sulla riga sbagliata;
- `:658` e' il **pubblico dell'arena**, e le ultime due sono scambiate:
  「頑張って！」 («forza!») porta «`Use your brain!`» e 「頭を使えよ」 («usa la
  testa») porta «`Good fighting.`».

✅ Rese tutte sul giapponese, che e' la regola del progetto dal lotto 019 della
38a — *si copia sul giapponese, mai sull'inglese*.

⚠️ **`:406` e' un «personaggio sbagliato» in piena regola**: il giapponese dice
`name(cc)` e l'inglese `name(tc)`, e il codice sta col giapponese — le tre righe
sopra (`snd`, `animeload 8, cc`) e le quattro sorelle `:381`-`:399` parlano tutte
di `cc`. ✅ La resa usa `name(cc)`, che `verifica` accetta perche' l'argomento
viene da **uno dei due rami di monte**, non per forza dall'inglese.

⭐ **Tre rese erano gia' decise altrove, e `dossier.py` ne ha pescata una per
giapponese intero**: `:865` («キットを使い…応急手当») e' parola per parola
`action.hsp:11146`, e la resa e' **copiata** — «ha usato il kit di pronto
soccorso». Le altre due sono termini, non frasi, e il dossier non le vede: la
ふかふかパン e' il **«pane soffice»** di `db_item.hsp:141763`, e la パートナー
della tag-team e' il **«compagno di coppia»** di `action.hsp:1024`-`:1889`. E' la
lezione del lotto 005 della 40a: il dossier prende le frasi intere e manca i
termini annegati.

⚠️ **`he(cc, 1)` e' contenuto e va conservato, e in italiano dice «lui»/«lei».**
`:381` e' l'unica voce del lotto che lo porta (`init.hsp:1819`-`:1838`, gia'
tradotto): il ramo con **due** argomenti passa da `lang()`, quello a un argomento
no. La resa se lo tiene dentro la frase — «non ricorda piu' perche' lui
combatte» — perche' la rete 11 lo pretende. ⚠️ E per chi si dichiara maschio o
femmina senza esserlo restituisce «lui?» / «lei?», col punto interrogativo
dentro: e' l'upstream, non la resa.

⚠️⚠️ **Due divergenze nuove e legittime — e la misura ha smentito la previsione,
che e' la cosa piu' utile del lotto.** Erano state annunciate come «`battute
--divergenti` passa da 13 a 15», e invece il referto e' rimasto **13**: quel
comando legge `dizionario/db_creature.hsp.jsonl` **e basta** (`battute.py:143`,
`percorsi.DIZIONARIO / f"{FILE}.jsonl"`), quindi un giapponese reso in due modi
in **due file diversi** non lo vede nessuno. L'unica cosa che l'ha visto e' la
**rete 3 dentro il lotto**, che pero' gira solo mentre si scrive un lotto nuovo e
non e' mai stata passata all'indietro su tutto il dizionario. 💡 E' esattamente
la situazione della rete 8 prima della 37a, quando `rete8_dizionario.py` trovo'
sei rese gia' entrate che stampavano «di il»: **e' il candidato naturale al
prossimo referto**, insieme al `termini.py` della 40a.

Le due divergenze sono lo stesso giapponese reso in due modi perche' i due siti
sono di **tipo** diverso:

- 「痛っ！」 qui e' una **statica** fra virgolette che il personaggio grida
  (`chatc@DP = cc`), «Ahi!»; ad `action.hsp:8778` e' una **dinamica** che
  descrive dal di fuori, «name(tc) + " si contorce dal dolore."»;
- 「いいぞ！」 qui e' il pubblico dell'**arena** che incita, «Cosi' si fa!»; a
  `proc.hsp:850` e' il pubblico di un **concerto**, «Bel pezzo!».

⭐ **La canzone rumena, e la scelta piu' discutibile del lotto.**
`:1452`-`:1468` sono *Dragostea din tei*, e il giapponese non la traduce: la
scrive in **soramimi**, cioe' in parole giapponesi vere che suonano come il
rumeno — 「飲ま飲まイェイ」, «bevi bevi yay», che in Giappone e' il modo in cui la
canzone e' conosciuta. L'inglese ha rinunciato e ha stampato il rumeno vero piu'
il ritornello famoso. ✅ La resa italiana fa quel che ha fatto il giapponese, cioe'
usa la forma con cui la canzone e' conosciuta **qui**: «Numa numa iei!!». E i due
gradini piu' assurdi (`:1456` e `:1460`) fanno il soramimi vero e proprio, cioe'
**parole italiane esistenti che suonano come il rumeno**: «Brie♪ sale♪ pece♪
dai♪» per «Vrei sa pleci dar», «Numera♪ numera♪ ehi!♪» e «Una mano♪ una mano♪
ehi!♪» per «nu ma nu ma iei». La scala dei tre gradini regge come in giapponese:
il primo e' la forma famosa, gli altri due sono sempre piu' scemi.
⚠️ **«Vrei sa pleci dar♪» resta invariato** e va dichiarato in `invariati.md`:
e' un verso in una terza lingua, ed e' il caso di «Ensemble!» e «*Kamikakushi*»
della 38a.

💡 **Le tre coppie di `rnd` sono una scala, non tre righe sparse.** `:1207` e
`:1252` («non resiste e si avvicina al cibo / all'acqua») sono la stessa frase
per i due bisogni, come le sei della sete e della fame di `calculation.hsp`: le
rese sono parallele apposta, cosi' la scala si sente.
"""
