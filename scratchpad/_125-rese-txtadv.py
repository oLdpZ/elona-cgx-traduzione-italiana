# -*- coding: utf-8 -*-
"""125a - Le 117 firme di `txtadv.hsp`: l'esplorazione e il casino'.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-rese-txtadv.py

Il file tiene tre schermate: l'**esplorazione** del sito casuale (`*atx_RE`),
il **blackjack** (`*adv_casinoBlackJack`) e le **slot** (`*adv_casinoSlots`, che
e' roba di Custom-GX). Chiude l'ultimo fronte di `lang()` del progetto insieme a
`net.hsp`.

⚠️⚠️⚠️ **LE SLOT SONO INGLESE SCRITTO SU GIAPPONESE RICOPIATO A CASO.** Come in
`custom_itemenchantment.hsp` (125a), ma qui il segnaposto non e' nemmeno la riga
giusta: per le voci nuove Custom-GX ha riusato il giapponese della **prima riga
che gli capitava**. Non e' un'ipotesi, lo dice il codice:

    :1183  jp «il blackjack e' il gioco in cui ci si avvicina a 21»
           en «In Slots, stop the spinning at right time…»   -> e' la slot
    :1253  jp «che faccio?»            en «Wheel of Fortune»  -> e' il titolo
    :1254  jp «esplora»                en «Pull»              -> tira la leva
    :1256  jp «esplora»                en «(Cheat) Slow time using X!»
    :799   jp «blackjack»              en «I want to play Slots.»
    :1527  jp «non c'e' niente...»     en «Nothing... scut!»

Su tutte queste **vince l'inglese**, perche' e' la fonte scritta: la regola
della 109a («si guarda quale fonte e' stata copiata e quale e' stata scritta»),
la stessa usata per il fabbro degli incantamenti.

⚠️⚠️⚠️ **E TRE PUNTI DELL'ESPLORAZIONE SONO LO STESSO CASO, NEL CODICE DI
MONTE.** `:507`, `:516` e `:525` aggiungono tre tipi di sito nuovi riusando il
giapponese di `:498` («ho trovato dei resti»), e le **abilita' controllate**
dicono qual e' la verita':

    :507  CARPENTRY / WEIGHT_LIFTING  «heavy wood blocking the path»  legname
    :516  TACTICS / STEALTH           «kamikaze-yeeks ahead»          yeek
    :525  LITERACY / MEMORIZATION     «familiar magical inscriptions» iscrizioni

Le voci di menu che seguono lo confermano riga per riga: «Chop»/«Lift»,
«Approach»/«Sneak attack», «Just read it»/«Try to recall», tutte su un
giapponese che dice «fruga»/«seziona». **Nessuna rete puo' vederlo**: bisogna
leggere le due righe di `atxskillcheck` sopra la `noteadd`.

⚠️⚠️ **`:665` E' UN DIFETTO DI MONTE CHE SI VEDE SOLO NEL CODICE.** Il
giapponese e' `lang("叩き割る(筋力: ", "Smash it. ")`, e la riga poi ci attacca
`"(" + skillname(SKILL_ATTR_STR) + ": " + sdata(...) + ")"`: in giapponese
esce **«叩き割る(筋力: (筋力: 12)»**, con la parentesi aperta due volte. L'inglese
ha buttato il pezzo di troppo, e l'italiano fa lo stesso.

⚠️⚠️ **`:825` E `:826` SONO SCAMBIATE FRA LE DUE LINGUE** (la forma della 104a,
«inglese slittato»). Il giapponese dice prima «dichiara la puntata» e poi «piu'
fiche punti, meglio e' il premio»; l'inglese le rovescia. Le due frasi sono due
firme e si rendono ciascuna dal **suo** giapponese, quindi in italiano l'ordine
a schermo torna quello di monte giapponese. ⓘ L'ordine inglese e' forse piu'
comodo — la domanda finisce attaccata al menu — ma non e' un difetto da
correggere: e' una riscrittura, e il giapponese qui e' la fonte scritta.

⚠️ **`:823` e `:824` sono una frase sola spezzata a mano dall'inglese**, perche'
la riga di messaggio ha un tetto: monte non supera mai i **71 caratteri**
(`pos 170`, `font 14`). L'italiano sta sotto lo stesso tetto senza spezzare
niente, perche' il giapponese le aveva gia' scritte come due frasi intere.
La misura e' in `scratchpad/_125-larghezze-txtadv.py`.

⭐ **Le quattro «戻る» si rendono in tre modi, e a distinguerle e' il CODICE.**
Il giapponese dice «torna indietro» in tutt'e quattro; l'inglese colora
(«Return», «Bah...!», «Great.»), e la colorazione non e' arbitraria: `:937` si
raggiunge con `winner == 0`, cioe' dopo aver **perso**, `:1170` e `:1529` dopo
aver **incassato il premio**, `:763` alla fine di un'esplorazione qualunque.
Sono tre situazioni diverse per costruzione, non tre capricci del traduttore.

Termini presi dal dizionario invece che inventati:
  カジノチップ  «fiche da casinò»   `material_data.hsp:14`, cioe' `matname(1)`
  景品          «premio»            `chat.hsp` (il suggerimento sul casino')
  ディーラー    «il banco»          idem
  イカサマ      «barare»            `chat.hsp` «Hai barato, vero!?»
  フォーチュンクッキー «biscotto della fortuna»  `db_item.hsp`
  Lv            «Lv»                85 rese su 85
  カミカゼ・イーク «lo yeek kamikaze»  `db_creature.hsp`
  Destrezza / Fortuna                `skill.hsp:29`, `:64`
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DENTRO = os.path.join(QUI, '_125-txtadv.jsonl')
FUORI = os.path.join(RADICE, 'lavoro', 'fase6-txtadv-001.jsonl')

# la coda comune delle voci di menu dell'esplorazione: il gioco ci attacca
# "(" + skillname(...) + ": " + valore + ")", quindi la resa e' solo il verbo.
RESE = {
    # ---------------------------------------------------------- l'ingresso
    (95, 'You talk to the dealer.'): 'Ti rivolgi al banco.',
    (331, "There're some items you can acquire."):
        'C\'è un po\' di bottino da raccogliere.',

    # ------------------------------------------------- il sito d'esplorazione
    (352, 'Random Site'): 'Sito casuale',
    (392, 'You see a jumble of debris and remains left by the dead.'):
        'Qui intorno è tutto un ammasso di rottami e di resti.',
    (398, 'You see many plants you have never seen before.'):
        'Qui intorno crescono tante piante mai viste prima.',
    (404, 'You see an abundance of natural ores.'):
        'È un giacimento di minerali naturali.',
    (410, 'You see a beautiful spring.'): 'C\'è una bella sorgente.',
    (437, 'What will you do?'): 'Che facciamo?',
    (438, 'Search'): 'Esplora',
    (439, 'Leave'): 'Vattene',
    (440, 'Remaining Actions: \\n'):
        '"Azioni rimaste: " + atxap + "\\n"',
    (442, ' Danger-Lv: '): '" Pericolo: Lv" + atxlv + ""',

    # --- i sette tipi di sito. La resa segue le ABILITA' controllate, non il
    #     giapponese ricopiato: vedi il commento in testa.
    (471, 'You found a bush.'): 'Hai trovato un cespuglio.',
    (472, 'Investigate '): 'Esamina ',
    (473, 'Harvest '): 'Raccogli ',
    (480, 'You see a vein of ore in the rocks.'):
        'Nella roccia c\'è una vena di minerale.',
    (482, 'Dig '): 'Scava ',
    (489, 'You found a spring of water.'): 'Hai trovato una sorgente.',
    (490, 'Drink'): 'Bevi',
    (491, 'Fish '): 'Pesca ',
    (498, 'You found some remains.'): 'Hai trovato dei resti.',
    (499, 'Scavenge '): 'Fruga ',
    (500, 'Dissect '): 'Seziona ',
    # ⚠️ CARPENTRY + WEIGHT_LIFTING: è legname, non resti
    (507, 'You found heavy wood blocking the path.'):
        'Un tronco pesante ti sbarra la strada.',
    (508, 'Chop '): 'Taglia ',
    (509, 'Lift '): 'Solleva ',
    # ⚠️ TACTICS + STEALTH: sono yeek kamikaze
    (516, 'You found some kamikaze-yeeks ahead.'):
        'Più avanti ci sono degli yeek kamikaze.',
    (517, 'Approach '): 'Avvicinati ',
    (518, 'Sneak attack '): 'Attacca di sorpresa ',
    # ⚠️ LITERACY + MEMORIZATION: sono iscrizioni magiche
    (525, 'You found some familiar magical inscriptions.'):
        'Hai trovato delle iscrizioni magiche che ti dicono qualcosa.',
    (526, 'Just read it '): 'Leggile ',
    (527, 'Try to recall '): 'Ricorda ',
    (531, 'There is some kind of suspicious crack on the wall...'):
        'Nel muro c\'è una crepa che ha qualcosa di strano...',
    (532, 'Whack'): 'Picchia',
    (533, 'Investigate'): 'Esamina',
    (550, 'Ugh! You hurt yourself during the process.'):
        'Ahi! Ti fai male nel farlo.',

    # --- gli incontri casuali
    (580, 'Wait.. what?'): 'Ehi... e adesso?',
    (581, 'You got lost! (Actions -2)'): 'Hai perso la strada! (Azioni -2)',
    (588, 'You got spooked by a ghost! (Actions -1)'):
        'Un fantasma ti ha fatto prendere uno spavento! (Azioni -1)',
    (596, 'You tripped and fell on a pebble! (Actions -1)'):
        'Inciampi in un sasso e cadi! (Azioni -1)',
    (606, 'I found a pile of fluffy straw.'):
        'Hai trovato un mucchio di paglia soffice.',
    (607, 'Fluffy, mmmm, fluffy. (Actions +3)'):
        'Che bello, tutta morbida. (Azioni +3)',
    (614, 'You found a stump.'): 'C\'è un ceppo d\'albero.',
    (615, 'You sat back and relaxed from the fatigue. (Actions +2)'):
        'Ti siedi e riprendi fiato. (Azioni +2)',
    (622, 'You found a beautiful flower.'): 'Hai trovato un bel fiore.',
    (623, 'Your heart is comforted. (Actions +2)'):
        'Il cuore si è rasserenato... (Azioni +2)',
    (632, 'Aha! Some healing herbs.'): 'Ah, erbe che curano.',
    (638, 'Oh! Vines for bandaging.'): 'Oh! Liane buone per bendare.',
    (648, 'Ouch! Mosquito bites.'): 'Ahi! Ti ha punto una zanzara.',
    (654, 'Ugh! Snake bite.'): 'Ahi! Ti ha morso un serpente.',

    # --- il forziere
    (663, 'You found a chest!'): 'C\'è un forziere.',
    (664, 'Dismantle the lock. '): 'Smonta la serratura. ',
    # ⚠️ il giapponese porta un "(筋力: " di troppo che la riga poi ripete:
    #    monte lo stampa due volte, l'inglese l'ha buttato e l'italiano pure.
    (665, 'Smash it. '): 'Sfondalo. ',
    (667, 'Remaining actions: \\n'):
        '"Azioni rimaste: " + atxap + "\\n"',
    (670, ' Chest-Rank: '): '" Premio: Lv" + keihin + ""',
    (679, "You don't have lockpicks."): 'Non hai grimaldelli.',
    (684, 'You fail to unlock it.'): 'Non riesci ad aprirla.',
    (703, '@GR has been added to your loot list!'):
        '"@GR" + itemname(ci, inv(INV_ITEM_NUM, ci)) + " va nel bottino!"',
    (704, 'You successfully unlock it.'): 'L\'hai aperta.',
    (710, 'You hurt your muscles.'): 'Ti stiri un muscolo.',
    (716, 'You bash up chest. The content is destroyed.'):
        'L\'hai sfondato a spallate, e dentro si è rotto tutto.',
    (746, '@BLYou get  (s)! (Total:)'):
        '"@BLHai preso " + 1 + " " + matname(p) + "! (in tutto: "'
        ' + mat(p) + ")"',
    (751, 'You found nothing...'): 'Non hai trovato niente...',
    (762, 'Finished searching.'): 'Hai finito di esplorare.',
    (763, 'Return'): 'Torna indietro',
    (766, 'Aieeeeeeeee...'): 'Ghh...',
    (767, '(Death Cry)'): '(rantolo di morte)',

    # ------------------------------------------------------------ il casino'
    (780, 'Casino <<Fortune Cookie>>'): 'Casinò <<Biscotto della Fortuna>>',
    (782, 'Welcome to the casino, Fortune cookie!'):
        'Benvenuto al casinò <<Biscotto della Fortuna>>.',
    (783, 'You can bet the casino chips you have and play some games.'):
        'Con le fiche da casinò puoi giocare alle nostre partite.',
    (784, 'Enjoy your stay.'): 'Si diverta con comodo.',
    (787, 'Looks like you play for the first time, sir.'):
        'Mi pare che sia la prima volta che viene da noi.',
    (788, "We're offering you 10 free casino chips to try our games."):
        'La casa le regala dieci fiche da casinò.',
    (792, '@BLYou get  (s)! (Total:)'):
        '"@BLHai preso " + 10 + " " + matname(1) + "! (in tutto: "'
        ' + mat(1) + ")"',
    (794, 'Casino chips left: \\n'):
        '"Fiche rimaste: " + mat(1) + "\\n"',
    (796, 'Later.'): 'Esci dal locale',
    (797, 'I want to play Blackjack.'): 'Vorrei giocare a blackjack',
    # ⚠️ giapponese ricopiato («blackjack»): l'inglese e' la fonte scritta
    (799, 'I want to play Slots.'): 'Vorrei giocare alle slot',

    # --- il blackjack
    (823, 'In Blackjack, the hand with the highest total wins as long as it'):
        'Il blackjack è il gioco in cui ci si avvicina a 21 con le carte.',
    (824, "doesn't exceed 21. J,Q,K are counted as 10 and A is counted as 1 or 11."):
        'J, Q e K valgono 10, l\'asso 1 oppure 11. Oltre 21 si perde.',
    # ⚠️ l'inglese scambia questa con la prossima: ciascuna segue il SUO
    #    giapponese, e l'ordine a schermo torna quello di monte.
    (825, 'More bets means better rewards.'):
        'E allora, dica quante fiche vuole puntare.',
    (826, 'How many tips would you like to bet?'):
        'Più fiche punta, migliore è il premio.',
    (832, "Sorry sir, you don't seem to have casino chips."):
        'Mi dispiace, ma lei non ha fiche.',
    (834, 'I quit.'): 'Lascia perdere',
    (836, 'Bet  chips.'): '"Punta " + 1 + " fiche"',
    (839, 'Bet  chips.'): '"Punta " + 5 + " fiche"',
    (842, 'Bet  chips.'): '"Punta " + 10 + " fiche"',
    (845, 'Bet  chips.'): '"Punta " + 20 + " fiche"',
    (864, 'You lose  (s). (Total:)'):
        '"Hai perso " + stake + " " + matname(1) + " (ne restano "'
        ' + mat(1) + ")"',
    (876, 'Dealer'): 'Banco',
    # lo scarto in testa e' quello di monte: allinea «Tu» sotto «Banco»
    (878, '   You'): '  Tu',
    (900, 'Your hand is .'): '"Il tuo totale è " + cpscore(1) + "."',
    (902, "The dealer's hand is ."):
        '"Il totale del banco è " + cpscore(0) + "."',
    (915, 'The match is a draw.'): 'La mano finisce pari.',
    (918, 'You lose.'): 'Ha perso lei.',
    (921, 'Congratulations, you win.'): 'Complimenti, ha vinto lei.',
    (927, 'Bets:  Wins: '):
        '"Puntata: " + stake + " Vittorie di fila: " + winrow + ""',
    (928, 'Alert-Lv:  Rewards-Lv: '):
        '"Sospetto: Lv" + ikasama + " Premio: Lv" + keihin + ""',
    (934, 'To the next round.'): 'Alla mano seguente',
    # ⚠️ le quattro «戻る»: a distinguerle e' il codice, non il traduttore
    (937, 'Bah...!'): 'Vabbè...',
    (949, 'Stay.'): 'Sto così',
    (952, 'Hit me. (Luck)'): 'Un\'altra carta (Fortuna)',
    (954, 'Cheat. (Dex:'): 'Bara. (Destrezza: ',
    (956, "I'm out. (costs 1 chip)"): 'Mi ritiro (ti costa 1 fiche)',
    (975, 'I have a bad feeling about this card...'):
        'Questa carta non mi piace per niente...',
    (993, 'Cheater!'): 'Hai barato!',
    (998, 'You are caught cheating...'): 'Ti hanno visto barare...',
    (1000, "I didn't do it!"): 'Sono innocente!',
    (1017, 'Congratulations! Your Rewards-Lv was !'):
        '"Complimenti! Il suo premio era di Lv" + keihin + "!"',
    (1170, 'Great.'): 'Benissimo',

    # --- le slot (Custom-GX): sopra il giapponese ricopiato vince l'inglese
    (1183, 'In Slots, stop the spinning at right time to connect patterns.'):
        'Alle slot devi fermare i rulli al momento giusto per fare figura.',
    (1193, 'Use  chips.'): '"Punta " + 1 + " fiche"',
    (1253, 'Wheel of Fortune'): 'Ruota della fortuna',
    (1254, 'Pull'): 'Tira la leva',
    (1256, '(Cheat) Slow time using !'):
        '"(Trucco) Rallenta con "'
        ' + itemname(sandevistanci@txtadv) + "!"',
    (1347, 'Checking the wheel...'): 'Vediamo com\'è andata...',
    (1527, 'Nothing... scut!'): 'Niente di niente!',
}


def main():
    voci = [json.loads(l) for l in io.open(DENTRO, encoding='utf-8')]
    assert len(voci) == len(RESE), (len(voci), len(RESE))
    for v in voci:
        chiave = (v['riga'], v['en'])
        assert chiave in RESE, chiave
        v['it'] = RESE[chiave]
    with io.open(FUORI, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d rese in %s' % (len(voci), FUORI))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
