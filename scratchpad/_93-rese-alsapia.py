# -*- coding: utf-8 -*-
"""93a - ALSAPIA la maschera bianca (`chat.hsp:15101`-`:15122`, 9 firme su 9).

白面の『アルサピア』 / `<Alsapia>` (`db_card.hsp:2844`, reso **«<Alsapia> la
maschera bianca»**) e' la **sicaria** che aspetta il giocatore in fondo a
Lesimas. ⚠️ L'identificativo dice `MURDERER_MASK`, ma il nome italiano viene dal
giapponese 白面 e non dall'inglese: e' gia' deciso e non si tocca.

⭐ IL REGISTRO E' GIA' FISSATO da `chat.hsp:24351`-`:24353`, il bollettino che
la descrive (reso nella 88a): «Alsapia la maschera bianca e' di livello 35. Non
e' invisibile, ma dicono che schivi gli attacchi normali come se ballasse»,
«Se non riesci a **costringerla**...». ⚠️ **E' donna**, e parla come chi fa un
rapporto: frasi brevi, nessun trasporto, il tu asciutto (あなた).

LESSICO EREDITATO (non deciso qui):
  - レシマス      «Lesimas»              text.hsp:2770 e 30 siti
  - 秘宝          «tesoro segreto»       chat.hsp:2316, :2359
  - パルミア      «Palmia»               ovunque
  - 刺客          «sicari»               db_card.hsp:5808 (la farfalla sicaria)

⚠️⚠️ DEROGA 1 — `:15107`, 冒険者発見 SENZA IL NOME DEL MESTIERE.
La riga e' un **rapporto**: «avventuriero avvistato». Ma «avventuriero» in
italiano porta un genere e qui il bersaglio e' il giocatore. Si tiene la forma
del rapporto e si usa la formula del progetto: «Individuato chi va
all'avventura» (`chat.hsp:1469`, `:3495`, e oggi NORNE e LEIKI).

⭐⭐ DEROGA 2 — `:15107`, I DUE SQUADRONI CHE L'INGLESE CANCELLA.
Il giapponese dice 「第一陣と第二陣を突破して」: il giocatore e' arrivato fin li'
**sfondando la prima e la seconda ondata** di sicari. L'inglese scrive solo «I
am surprised that you are already here», e con la frase se ne va l'unica riga
che dice che gli agguati di Lesimas erano organizzati a ondate — cioe' quello
che il bollettino di `:24347` racconta dall'altra parte («una squadra di
assassini di Zanan sta invadendo Lesimas»). Torna dentro.

⭐ DEROGA 3 — `:15104`, LA BATTUTA DELLA GABBIA DI AMUR NON E' UN
RINGRAZIAMENTO. L'inglese scrive «I met my parents here again. **Thanks**, I can
kill them many times», e quel «thanks» non c'e' nel giapponese: 「死んだことで
両親と再会できるなんて」 e' lo stupore di chi **da morta** ha ritrovato i
genitori, e la riga dopo e' il piacere di poterli uccidere **all'infinito**
(何度でも). Non ringrazia nessuno: e' sola, e la frase e' rivolta a se stessa.
⚠️ La Gabbia di Amur e' il posto di <Amurdad> (reso nella 92a), dove finisce chi
e' morto: il vicinato conferma la lettura.

⚠️ DEROGA 4 — `:15116` e `:15119` DEVONO RESTARE **GEMELLE**.
Sono la stessa frase con l'incipit diverso (「…そう。やっぱり」 contro
「…？？？とりあえず」), perche' la prima risponde alle tre risposte serie e la
seconda alla battuta («Per incontrare te»). La parte comune —
「あなたにはここで消えてもらう」 — si rende con le **stesse parole** in tutt'e
due, se no il gioco del menu non si sente. L'inglese le fa gia' diverse
(«your graveyard» / «your grave»): non lo si segue.

PERIMETRO: 9 firme su 9 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15101`) e **zero firme gia' rese altrove**.

MENU: uno, da 4 voci (`:15108`-`:15111`), tutte nuove. ⚠️ `chatesc = 0`: da
questo menu **non si esce col tasto di fuga**, quindi le quattro voci si leggono
sempre tutte.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- l'agguato in fondo a Lesimas
    15107: 'Individuato chi va all\'avventura. Aver sfondato il primo e il '
           'secondo squadrone, e arrivare fin qui...',
    15112: 'Nefia è già pericolosa di suo, e hai i sicari alle calcagna. '
           'Perché vai avanti? È un ordine di Palmia?',
    15108: 'Perché lì c\'è l\'avventura',
    15109: 'Punto alla ricompensa, è ovvio',
    15110: 'Per impadronirmi del tesoro segreto di Lesimas',
    15111: 'Per incontrare te',
    15116: '...Capisco. Come pensavo, tu di qui non esci.',
    15119: '...??? Comunque sia, tu di qui non esci.',

    # --- nella Gabbia di Amur, dopo la morte
    15104: 'Chi l\'avrebbe detto: è morendo che ho ritrovato i miei genitori. '
           'Adesso posso ucciderli quante volte voglio...',
}
