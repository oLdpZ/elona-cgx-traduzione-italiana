# -*- coding: utf-8 -*-
"""94a - MELUGAST type0, la nave a distorsione dimensionale (`chat.hsp:9601`-`:9692`, 6 su 8).

`CREATURE_ID_MELUGAST_TYPE0_THE_DIMENSION_DRIVER`. E' la **macchina** che porta
a Irva Perduta e al continente fluttuante: un passaggio obbligato della trama,
non un personaggio che si incontra per caso.

⭐⭐⭐ IL BLOCCO HA **DUE BOCCHE**, E LA 93a AVEVA GIA' TROVATO LA STESSA COSA.
Nella 93a il blocco `MELUGAST_AO_I` sembrava di una creatura e invece era una
**radio**: a parlare era Gavela, e lo diceva `:13187`, «Qui Gavela». Qui succede
di nuovo, e stavolta dentro **un blocco solo**:

    :9604 - :9606   e' **GAVELA**, in un messaggio registrato — lo dichiara
                    `:9604`: 「こちらはガベラだ」
    :9637 - :9686   e' **LA MACCHINA**, che parla di se' come 本機 e risponde
                    a comandi

⚠️ I due registri non si mescolano. Gavela e' quello gia' reso nell'85a e nella
93a: rude, ingegnere, da' del tu, «Qui Gavela.» (`:13187`), «Con questo possiamo
vincere!» (`:13189`), «Se stiamo a dire impossibile di qua, impossibile di la',
la scienza non fa un passo!» (`:13198`). La macchina no: frasi mozze, niente
soggetto, nessuna cortesia.

⭐ E LA FORMULA D'APERTURA SI RICOPIA, NON SI RIFA': 「こちらはガベラだ」 e'
la stessa di `:13182`-`:13215` — **«Qui Gavela.»** — che e' la formula italiana
della radio. Cambiarla qui darebbe due incipit diversi alla stessa voce
registrata.

LESSICO EREDITATO (non deciso qui):
  - 次元歪曲航法  «navigazione dimensionale»   `chat.hsp:7879`, `:7913`
  - 次元歪曲ユニット  «unità a distorsione dimensionale»  `chat.hsp:13201` (93a)
  - メルガスト    «il Melugast»                `chat.hsp:7902`, `:7913`
  - 浮遊大陸      «continente fluttuante»      `chat.hsp:2184`, `:2199`, `:7928`
  - 結界          «barriera»                   `chat.hsp:7879`, `:7913`
  - エウダーナ    «Eulderna»                   ovunque

⚠️ DEROGA 1 — `:9605`, 浮遊大陸 NON E' UN'ISOLA.
L'inglese di `:9604` scrive «the floating **island** above Eulderna» e quello di
`:9605` «the floating **continent**»: due nomi per la stessa cosa, nella stessa
battuta. Il giapponese dice 浮遊大陸 tutt'e due le volte, e il progetto l'ha gia'
reso **«continente fluttuante»** in tre siti della catena delle missioni. Si
tiene uno solo dei due, come fa il giapponese.

⚠️⚠️ DEROGA 2 — `:9645`, L'INGLESE AGGIUNGE UNA BATTUTA DA HOSTESS.
«Please keep limbs inside the vehicle at all times.» **non esiste** nel
giapponese, che finisce a 「到着まで約2時間を要する」. E' proprio la frase che
darebbe alla macchina un'ironia che non ha: le sue tre righe sono tutte
referto, e questa e' la sola che la farebbe scherzare. Buttata.

⚠️ DEROGA 3 — `:9637`, «Identity confirmed.» E' DELL'INGLESE.
Il giapponese e' 「登録データとの照合完了。次元歪曲シーケンスを開始するか？」:
due frasi, non tre. La macchina dice che il confronto e' finito, non che
l'identita' e' confermata — e con `:9686` («冷やかしか…？», se si risponde di no)
si capisce che non sta autenticando nessuno, sta aspettando un ordine.

💡 `:9637` e' un **buff** e `:9635`/`:9636` sono le due voci del menu, gia' rese
altrove («Do it.» / «Nope.»): sono voci comunissime e la loro resa non e' di
questo lotto.

PERIMETRO: 6 firme da fare su 8 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9601`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- il messaggio registrato di GAVELA
    9604: '"Ehi, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ". Qui Gavela. Ah, '
          'questo messaggio l\'ho impostato perché parta da solo nel caso ti '
          'si trovi sul continente fluttuante sopra Eulderna."',
    9605: 'Mi sono stupito: le tue coordinate si sono spostate di colpo sopra '
          'Eulderna. In questo momento il continente fluttuante è circondato da '
          'una barriera speciale, e non ci passano né gli uomini né le macchine '
          'né i mostri. Questo Melugast però, con la navigazione dimensionale, '
          'la barriera la ignora e va e viene lo stesso...',
    9606: 'Un\'altra cosa: trenta secondi dopo questo messaggio l\'apparecchio '
          'lascia lo spazio aereo. Sarai anche in mezzo all\'esplorazione, ma '
          'se non vuoi restare a terra ti conviene salire in fretta.',

    # --- LA MACCHINA
    9637: 'Confronto con i dati registrati completato. Avviare la sequenza di '
          'distorsione dimensionale?',
    9645: 'Ricevuto. Alla conferma dell\'imbarco, partenza. Tempo previsto '
          'all\'arrivo: circa due ore.',
    9686: 'Semplice curiosità...? Passaggio allo stato di riposo.',
}
