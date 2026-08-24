# -*- coding: utf-8 -*-
"""91a - RAIZEL sulla Nave Magica (`chat.hsp:10391`-`:10434`, 6 firme).

「老魔導士『ライゼル』」, «<Raizel> il vecchio incantatore»
(`db_creature.hsp:76002`, `db_card.hsp:6718`). E' il vecchio mago di Eulderna,
l'unico che regge il confronto col demone della vendetta (`chat.hsp:2133`), e
questo blocco e' il momento in cui si parte dalla **Nave Magica** a riprendersi
la capitale.

⚠️ **QUESTO LOTTO NON ERA IN PROGRAMMA: L'HA CHIESTO UNA RETE.**
Chiudendo il lotto di REGULUS, `strumenti.bilingui` e' passato da **0 a 1**:

    chat.hsp:12832-12833   2 voci, 1 rese, 1 no
            :12832  'Hold on a minute.'

Il perche' e' scritto nel modulo di REGULUS: la firma di 「ちょっと待って」 ha
due occorrenze, `:10398` e `:12832`, e `--da-tradurre` la assegna alla prima —
che sta qui. Rendendo `:12833` («Partiamo») senza `:12832` il menu di Regulus
era rimasto **meta' in italiano e meta' in inglese**.

⭐ E rendere solo `:12832` non bastava: avrebbe spostato il difetto di
quaranta righe, perche' il menu di **questo** blocco (`:10398`-`:10399`) sarebbe
diventato bilingue a sua volta. La riparazione vera e' chiudere tutto il
blocchetto, che sono sei firme. 💡 *Una firma condivisa non appartiene al lotto
che la incontra per primo: appartiene a tutti i menu in cui compare, e si
chiude con loro.*

REGISTRO: vecchissimo e alto in grado — 「わし」/「おまえさん」/「〜じゃ」. E'
anche **smemorato**, e le due battute che contano sono proprio quelle: `:10401`
comincia con «che cosa dovevamo fare...?» e `:10429` chiede al giocatore chi
sia, dopo averglielo appena chiesto a `:10395`. La ripetizione non e' una
svista del gioco: e' il personaggio, e va lasciata suonare uguale.

LESSICO EREDITATO (non deciso qui):
  - «<Raizel> il vecchio incantatore»   db_creature.hsp:76002
  - «la Nave Magica (Eulderna)»       text.hsp:11149
  - «la capitale» (王都)              chat.hsp:2132
  - «Nefia», «Palmia»                 invariati

DEROGHE DICHIARATE
1. `:10396` - IL GENERE DEL GIOCATORE, due volte nella stessa riga.
   「協力者」 e 「強者」 sono due sostantivi che in italiano hanno un genere:
   «il collaboratore» e «uno in gamba» accorderebbero il giocatore. Si gira
   sul verbo e sulla cosa: «Sei tu che Palmia ci manda in aiuto» e «forza da
   espugnare una Nefia da N piani». Anche la chiusa: 「決定的な戦力になる」 ->
   «sarai **la forza** che decide questa battaglia», dove l'accordo cade su
   «forza».
2. `:10396` - l'espressione tiene `cdatan(CDATAN_AKA, ...)`, `cdatan(CDATAN_NAME,
   0)` e `gdata(GDATA_DEEPEST_LEVEL)` come l'inglese di monte: sono contenuto,
   non grammatica.
3. `:10399` - 「出撃！」 non e' «partiamo» (che e' `:12833`, di Regulus) ma un
   ordine militare: si sta muovendo una flotta. «All'attacco!».

PERIMETRO: 6 firme su 6 nel blocchetto. La firma condivisa `bd4fa9b7`
(「ちょっと待って」) copre anche `:12832`, e con questo lotto tutti e due i menu
tornano interi: `bilingui` da 1 a 0.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    10395: 'Mh... e tu chi saresti...?',
    10396: '"Ooh, " + cdatan(CDATAN_AKA, CHARA_PLAYER) + " " + '
           'cdatan(CDATAN_NAME, 0) + ". Sei tu che Palmia ci manda in aiuto, '
           'eh. Ne ho sentito parlare: forza da espugnare una Nefia da " + '
           'gdata(GDATA_DEEPEST_LEVEL) + " piani. Gli altri magari il tuo '
           'valore non lo riconosceranno, ma io ho la sensazione che sarai la '
           'forza che decide questa battaglia."',
    10398: 'Aspetta un attimo',
    10399: 'All\'attacco!',
    10401: 'Dunque, che dovevamo fare...? Ah, ecco. Andiamo a riprenderci la '
           'capitale. Gente! Preparatevi alla battaglia!',
    10429: 'Ah sì? A proposito, tu chi eri, scusa?',
}
