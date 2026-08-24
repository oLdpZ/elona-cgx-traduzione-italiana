# -*- coding: utf-8 -*-
"""93a - MELUGAST AO-I (`chat.hsp:13182`-`:13215`, 12 firme su 12).

⚠️ **IL BLOCCO NON E' DI UNA CREATURA: E' UNA RADIO.** L'identificativo e'
`CREATURE_ID_MELUGAST_AO_I_THE_DIMENSION_DRIVER` — «<Melugast AO-I> la macchina
da combattimento» (`db_card.hsp:2701`, `db_creature.hsp:52005`) — ma chi parla
e' **Gavela**, che dal drone fa da radio: lo dice la riga stessa, `:13187`,
«こちらガベラだ» («Qui Gavela»). La macchina non ha voce propria.

⭐ QUINDI IL REGISTRO E' GIA' DECISO DA UN ALTRO LOTTO, quello dell'85a
(`scratchpad/_85-rese-gavela.py`, `chat.hsp:7795`-`:8193`): Gavela da' del tu,
parla svelto e sbrigativo, e **quando spiega la tecnica diventa preciso**. Le
sue righe gia' rese sono il metro:

    chat.hsp:7820  «Col corpo a pezzi e non mollare... sei un idiota.»
    chat.hsp:7821  «Nemmeno io mollo, sta' tranquillo. Dimostrero' che l'AO-I...»
    chat.hsp:7876  «Vuoi sapere della navigazione dimensionale?! Bene...»

LESSICO EREDITATO (non deciso qui):
  - AO-I                «l'AO-I», maschile     chat.hsp:7821, :7830, :7833, :7861
  - メルガスト          «il Melugast»          action.hsp:17242, chat.hsp:7913
  - 次元歪曲航法        «navigazione dimensionale»  chat.hsp:7876, :7883
  - 空間歪曲            «distorsione spaziale»      chat.hsp:7883
  - イェルス超重力砲    «cannone a supergravita' di Yerles»  db_card.hsp:7693
  - 束縛の悪魔          «il demone dei vincoli»     db_card.hsp:4625 (<Egelveil>)
  - テスカトリポカ      «Tezcatlipoca»         db_card.hsp:3026 e 20 siti
  - ロスリア            «Lothria»              db_card.hsp:3351, chat.hsp:10131

⭐⭐⭐ DEROGA 1 — `:13191`, «A0-I» E' UN REFUSO DI MONTE E NON SI RICOPIA.
La voce di menu scrive **A0-I con lo zero**, in giapponese e in inglese. In
tutto il resto del sorgente — `chat.hsp:7821`, `:7830`, `:7833`, `:7861`,
`db_card.hsp:2701`, `db_creature.hsp:52005`, e l'identificativo stesso
`MELUGAST_AO_I` — la sigla e' **AO-I con la lettera O**, sempre in tutt'e due le
lingue. E' un sito solo contro sei: si scrive AO-I, perche' chi legge deve
riconoscere la macchina di cui Gavela parla per tutta la trama. ⚠️ Ricopiare lo
zero avrebbe dato **due nomi alla stessa macchina** a distanza di un menu, che e'
il difetto che la 92a ha trovato tre volte rileggendo il vicinato.

⭐⭐ DEROGA 2 — `:13192`, 畳みかける NON E' «INTERROGATE HIM».
L'inglese scrive «I've sealed his movements. Interrogate him!», ma 畳みかける
vuol dire **incalzare senza dare respiro**, ed e' un ordine d'attacco: il
giocatore e' in mezzo a un combattimento e ha appena visto l'ancora dimensionale
inchiodare il mostro. Interrogarlo non c'entra niente e non e' nemmeno possibile.
Si segue il giapponese: «non dargli tregua».

⭐ DEROGA 3 — `:13201`, LA FILA DEGLI EQUIPAGGIAMENTI SI TIENE INTERA.
E' la battuta piu' lunga del blocco ed e' un elenco tecnico di nove voci: e' il
punto in cui Gavela «diventa preciso», e ogni pezzo ha gia' un nome nel progetto
(il cannone a supergravita', il demone dei vincoli, la navigazione dimensionale).
Accorciare l'elenco toglierebbe la battuta, che e' proprio lo sproloquio da cui
si interrompe da solo.

⚠️ MISURA: `:13201` e' l'unica riga del blocco che ha **sfondato il tetto**, e
non di poco: 15 righe contro le 13 di `chatMore` (un bottone solo). ⭐ E
l'inglese ci sta **esattamente** — 13 su 13 — quindi il tetto non e' rotto di
suo: la riga in piu' era mia. Rientrata in due giri di potatura senza togliere
nessuna delle nove voci dell'elenco, che sono la battuta. 💡 Vale la pena
saperlo per il prossimo sproloquio tecnico: l'italiano su un elenco di termini
composti paga circa il 15% in piu' dell'inglese, e su una battuta gia' al tetto
diventano due righe.

PERIMETRO: 12 firme su 12 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 13182`) e **zero firme gia' rese altrove**.

MENU: uno, da 3 voci (`:13189`-`:13191`), tutte nuove.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- l'ancora dimensionale inchioda il mostro
    13186: 'Allora, che te ne pare della potenza dell\'ancora dimensionale? '
           'Con la forza fisica non se ne esce, mai.',
    13187: '"Qui Gavela. Il collegamento sembra buono. " '
           '+ cdatan(CDATAN_NAME, CHARA_PLAYER) + '
           '", quel mostro è Tezcatlipoca?"',
    13188: 'Eh, non è lui?? Vabbè, poco importa. Subito dopo lo scontro a '
           'Lothria mi è presa un\'ansia improvvisa, e ho fatto bene a farlo '
           'volare fin qui.',

    # --- il menu delle tre risposte
    13192: 'I suoi movimenti sono bloccati. Sotto, non diamogli tregua!',
    13189: 'Con questo possiamo vincere!',
    13190: 'È impossibile, indietro!',
    13191: 'Che cos\'è l\'AO-I?',
    13195: 'Eccome se vinciamo, noi insieme!',
    13198: 'Se stiamo a dire impossibile di qua, impossibile di là, la '
           'scienza non fa un passo!',
    13201: 'Bella domanda. C\'è l\'unità a distorsione dimensionale, ovvio, e '
           'poi armamento pesante, apparati di guerra elettronica, corazza '
           'aggiuntiva, propulsori in più, il sistema radio speciale del '
           'ricetrasmettitore autonomo, una versione ridotta e potenziata '
           'del cannone a supergravità di Yerles... e l\'ancora dimensionale, '
           'teorizzata sui dati dello scontro col demone dei vincoli! Un '
           'Melugast con tutte queste opzioni addosso: ecco l\'AO-I. Tanta '
           'roba insieme si è potuta montare grazie ai dati della teoria dei '
           'punti d\'aggancio biologici: è la summa della mia tecnica, e in '
           'particolare... ops, non è il momento di fare lezione.',

    # --- i due commenti più avanti nello scontro
    13206: 'Tipo tosto... Metterlo del tutto fuori uso sarà dura.',
    13210: 'Pare che sia finita... tutto quanto.',
}
