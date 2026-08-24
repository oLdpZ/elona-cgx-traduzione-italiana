# -*- coding: utf-8 -*-
"""94a - RAIZEL il vecchio mago, il resto del blocco (`chat.hsp:10335`-`:10441`, 7 su 26).

老魔導士のライゼル / `<Raizel> the old wizard`. Le altre **diciannove** firme del
blocco sono state rese nella 91a: questo e' il resto, e il registro **non si
decide qui** — sta gia' scritto in quelle rese e va solo riletto.

⭐ IL REGISTRO, DALLE SUE RIGHE DELLA 91a:
  - `:10339` «Bel lavoro, ragazzi. [...] Al resto ci pensa questo **vecchiaccio**.»
  - `:10395` «Mh... e **tu** chi saresti...?»  → da' del **tu**, familiare (おまえさん)
  - `:10401` «Dunque, che dovevamo fare...? Ah, ecco.»
  - `:10429` «Ah sì? A proposito, **tu chi eri, scusa?**»
⚠️ La **smemoratezza e' il suo tratto**, non una battuta isolata: tre delle sette
righe di oggi (`:10377`, `:10384`, `:10437`) sono la stessa gag, e vanno rese
con la stessa mano di `:10401` e `:10429` — non ognuna a modo suo.

LESSICO EREDITATO (non deciso qui):
  - 凶獣 / 邪悪なる化身  «la belva», «l'incarnazione del male»  `:10344` (91a)
  - 忘却の女神の化身     «l'incarnazione della dea dell'oblio»  `:10353` (91a)
  - 混沌の神             «il dio del caos»                      `:10131` e 30 siti
  - 王都                 «la capitale»                          `:10401` (91a)
  - エウダーナ           «Eulderna»                             ovunque
  - 魔導船               «nave magica»                          `text.hsp:9822`, `chat.hsp:2133`
  - 悪魔                 «il demone» (Inqtual, quello di Eulderna)  `:2048`, `:24473`
  - 「よいところに来た」 «Capiti proprio a proposito»           `:1502`, `:8734`

⚠️⚠️ DEROGA 1 — `:10376`, L'INGLESE BUTTA VIA LA MEZZA FRASE CHE CONTA.
Il giapponese e' 「おかげで混沌の神を相手にするまで温存することができるわい。
**邪悪な化身である凶獣の力を**、のう…。」 — cioe' dice **che cosa** ha potuto
tenere in serbo. L'inglese scrive «Thanks to you, that can be saved until the
confrontation with the God of Chaos. **When that time comes, we...**»: perde il
complemento oggetto e ci mette una frase sospesa che non c'e'. ⚠️ Quella e' la
stessa forza che a `:10344` (91a) Raizel scatena su di se': «È il momento di
usarla... la forza della belva, l'incarnazione del male!». Si rende **con le
stesse parole**, se no la riga di oggi e il suo sacrificio non si toccano piu'.

⚠️ DEROGA 2 — `:10375`, 守る NON E' «RETAKE».
L'inglese scrive «We were able to **retake** the castle»; il giapponese dice
王都を**守る**ことができた, cioe' difendere. La riconquista e' un'altra riga e
un altro momento — `:10401`, «Andiamo a **riprenderci** la capitale», che e' la
partenza; questa e' il dopo, e quello che si e' fatto e' **tenerla**.

⭐ DEROGA 3 — `:10384`, わがエウダーナの魔導船.
L'inglese perde il nome del paese («How was **our** magic ship?»). E' la **Nave
Magica Eulderna** che il diario nomina per esteso (`text.hsp:9822`, `:11149`,
`:11157`) e su cui sta anche <Nein>: il possessivo che se ne va porta con se'
l'unico aggancio fra la battuta e il posto in cui il giocatore si trova.

⭐ DEROGA 4 — `:10436`, IL GIOCATORE NON HA GENERE.
「おお、冒険者か。」 → formula del progetto **«chi va all'avventura»**
(`chat.hsp:257`, `:1595`, `:7843`), non «un avventuriero».

PERIMETRO: 7 firme da fare su 26 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 10335`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`. `:10437` porta `strbye`, cioe' chiude.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- dopo la battaglia per la capitale
    10375: 'Con il tuo aiuto siamo riusciti a difendere la capitale, grazie. '
           'Se attaccando con tutte queste forze non fossimo riusciti ad '
           'abbatterlo, allora sì che avremmo dovuto usare l\'ultima carta.',
    10376: 'Grazie a te posso tenerla in serbo fino a quando avremo davanti il '
           'dio del caos. La forza della belva, l\'incarnazione del male, '
           'dico...',
    10377: 'Mh. Ma io adesso di che cosa stavo parlando...?',

    # --- sulla Nave Magica, prima dell'assalto
    10384: 'Allora, che te ne pare della nostra nave magica di Eulderna? Un bel '
           'viaggio, eh? ...A proposito, noi qui eravamo venuti a fare che '
           'cosa?',
    10385: 'Ah, già: dobbiamo abbattere quel demone. I nemici sono tanti; '
           'appena la cosa si fa pericolosa, ritirati subito sulla nave.',

    # --- prima che la storia cominci
    10436: 'Oh, ecco chi va all\'avventura. Capiti proprio a proposito. Avrei '
           'una cosetta da chiederti.',
    10437: 'La cosa che volevo chiederti è... mh? Me la sono scordata...',
}
