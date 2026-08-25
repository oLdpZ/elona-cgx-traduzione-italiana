# -*- coding: utf-8 -*-
"""95a - La coda di `chat.hsp`: le ultime sei firme del file.

`NEW_CITIZEN` (`:8775`-`:8780`, 2), `MOBILE_COMMUNICATION_EQUIPMENT`
(`:8781`-`:8794`, 2), `RATIN` (`:9322`-`:9366`, 1) e `SHELL_KING_OF_VINDALE`
(`:10014`-`:10021`, 1).

⭐⭐⭐ CON QUESTE SEI **`chat.hsp` SI CHIUDE**: 0 da ritradurre, 0 da fare, e le
uniche voci che restano nel conto sono le **cinque rinviate** dell'87a — le
righe commentate a monte del blocco di AJETALIO — piu' `:22500`, che una toppa
della 64a gia' sistema.

⭐⭐ CHI PARLA DALL'APPARECCHIO E' GAVELA, E LO DICE `text.hsp`.
`MOBILE_COMMUNICATION_EQUIPMENT` non ha un nome di parlante: e' una radio. Ma
dice 「メルガスの俺のラボ」, e `text.hsp:9729` — gia' reso — dice «Devo mettermi
in contatto con un uomo di nome **Gavela**, nel **laboratorio di Melugas**».
E' lui, e il suo registro e' fissato da undici rese fra la 85a e la 94a: brusco,
tecnico, da' del **tu** («Ehi, ... Qui Gavela.», `:9604`; «Allora ti spiego.»,
`:7913`). ⚠️ Cercare **chi** parla prima di scegliere il tono, anche quando il
blocco si chiama come un oggetto.

⭐⭐⭐ DEROGA 1 — `:8777`, LA BATTUTA E' UN CAMBIO DI REGISTRO A META' FRASE, E
IN ITALIANO IL PERNO E' UN ALTRO.
「僕になにか…こほん。私に何か用でしょうか。」 — il nuovo cittadino comincia col
**僕** confidenziale, si schiarisce la voce, e ricomincia col **私** formale.
E' un ex ninja che finge di non esserlo (`:8778`: «Ninja? Che roba e'?»), e
tutta la battuta e' quel mezzo passo falso.
In italiano i due pronomi sono lo stesso «io» e il perno non c'e'. Ma la
**seconda persona** ce l'ha: la frase si rompe su un **tu** che si corregge in
**lei**, che e' esattamente lo stesso scivolone nello stesso punto. Non e' una
resa piu' libera: e' lo stesso scherzo sul dispositivo che questa lingua ha.
💡 E' la regola delle fusioni («si rende il gioco, non le sillabe») applicata a
un registro invece che a un gioco di parole.

⚠️ DEROGA 2 — `:10017`, L'INGLESE HA CAPITO ALL'INCONTRARIO.
「神には神の思惑があって動いている」 vuol dire che *gli dei si muovono seguendo
disegni loro*; l'inglese scrive «The gods' expectations **change**», che e' un
altro senso e toglie il perno alla frase dopo — se gli dei hanno un disegno loro
allora seguirli alla cieca e' sbagliato, e da li' viene 我ら定命. Si segue il
giapponese (57a).

⚠️ DEROGA 3 — `:9362`, L'INGLESE BUTTA LA PAROLA CHE CONTA.
「確かにノルマの達成を確認した」 diventa «You've done very well»: sparisce
**ノルマ**, che e' il nome della meccanica — «obiettivo» in dodici rese fra
`chat.hsp` e `command.hsp`, «Quota della Gilda dei Guerrieri» nel diario
(`text.hsp:10537`). La riga chiude un incarico e deve nominarlo.

LESSICO EREDITATO (non deciso qui):
  - ノルマ      «l'obiettivo»            `chat.hsp:5354`, `command.hsp:15493`
  - 本部        «il quartier generale»   `db_creature.hsp:79879`
  - メルガス    «Melugas»                `text.hsp:768` e venti siti
  - ラボ        «il laboratorio»         `chat.hsp:6740`, `text.hsp:9729`
  - 遺跡 (questo) «le rovine»            `main.hsp:4105`, `text.hsp:2979`
  - 定命        «i mortali»              `chat.hsp:10142`, `:18105` e altri
  - 忍者        «ninja»                  parola tenuta, `decisioni.md`

⚠️ Il 本部 di `:9362` **non** e' «il consiglio» di `:5423`: quella riga rende
審査会, la commissione d'esame della Gilda dei Maghi, che e' un'altra cosa e ha
un'altra parola in giapponese. Le due frasi si somigliano molto e vanno tenute
distinte apposta.

PERIMETRO: 6 firme su 6 dentro i quattro blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 8775 8781 9322 10014`), zero gia' rese
altrove.

MENU: nessuno da fare. Le voci di RATIN (`:9326`, `:9329`) sono gia' rese.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- IL NUOVO CITTADINO, che ninja non è mai stato, giuriamo
    8777: 'Che vuoi da... ehm-ehm. Desidera qualcosa da me?',
    8778: 'Eh...? Ninja? C-che roba è?',

    # --- L'APPARECCHIO DI COMUNICAZIONE, cioè Gavela
    8784: 'Sta\' attento. Pare che le macchine dentro le rovine siano '
          'impazzite per via di certe onde strane. Se ti vedi male, risali '
          'subito le scale e scappa. Però quello con cui stai parlando '
          'adesso, quello col monitor, è un apparecchio che avevamo messo lì '
          'per raccogliere dati e per le comunicazioni: distruggigli la parte '
          'motrice senza toccare quella dove stanno i dati, e portamelo al '
          'mio laboratorio a Melugas.',
    8788: 'Scusa se ti interrompo l\'esplorazione, ma vieni subito al mio '
          'laboratorio a Melugas. ...Anche se a dirlo così un avventuriero è '
          'capacissimo di fare finta di niente. Ho chiuso a distanza la porta '
          'che porta al piano dopo. Più avanti non ci vai.',

    # --- RATIN, l'investigatore della Gilda dei Guerrieri
    9362: 'Obiettivo raggiunto, confermo. Riferisco subito al quartier '
          'generale quello che hai fatto.',

    # --- IL RE DEI GUSCI DI VINDALE
    10017: 'Gli dei si muovono seguendo disegni loro. Noi mortali non dobbiamo '
           'andargli dietro alla cieca: dobbiamo avere un pensiero nostro e '
           'agire di conseguenza.',
}
