# -*- coding: utf-8 -*-
"""79a — `chat.hsp`, `*chat_event` (`:302`-`:944`) chiuso intero.

Il blocco degli **eventi**: chi bussa alla porta, chi passa a trovarti, chi ti
assalta per strada, le feste. Come gli evochat e' una zona **chiusa**: 103 firme
da fare, 109 occorrenze, **zero** con occorrenze fuori
(`scratchpad/perimetro-zona.py`).

Le famiglie, in ordine di riga:

    310-317   il regalo di CAPODANNO
    321-336   il rancoroso che ti tira una molotov
    356       chi ha bevuto troppo
    367-372   il bambino che regala qualcosa
    403-425   il compagno che ti allena e ti lascia un pegno
    444-460   la visita col regalo e il sacco di materiali
    471-508   le chiacchiere, il brindisi, il saluto
    514-561   il maestro di gilda e l'allenatore: il POTENZIALE
    575-587   il mendicante
    633-694   HALLOWEEN: dolcetto o scherzetto
    726-758   la guardia, l'ospite e il produttore
    764-856   i CINQUE aspiranti inquilini della casa
    893       il mercante che se ne va
    905-936   il caposquadra del Dock

⭐⭐ **I cinque inquilini: il registro non si e' deciso, si e' ripreso da
`db_creature.hsp`** (chiuso dalla 31a), con `scratchpad/repertorio.py`.

| chi | nome reso | come parla |
|---|---|---|
| `SCARD_THE_HAPPY_SWALLOW` | «<Scard> la rondine felice» | «Felice! FELICE!», «Che daffare! Che FELICITA'!» |
| `OXODE_THE_QUEEN_BEE` | «<Oxode> l'ape stregina» | «Ara ara, tesoro~», «dolce miele», «padrone di casa» |
| `IMARITUKA_THE_ZASIKI_WARAI` | «<Imarituka> lo sberleffo di casa» | «lmao», «a scrocco», «Che imbarazzo!», la tilde |
| `TELHUREZA_THE_HOUSE_GUARD` | «<Telhureza> il geco di guardia» | «Fuehehe~», «gli insetti cattivi», «la casa che proteggo» |
| `MOMALARIA_THE_BLOODSUCKER` | «<Momalaria> la gravida succhiasangue» | il giapponese le spezza le parole in katakana |

💡 E le loro figlie, le **api magiche** che Oxode porta in casa, dicono «mamma»
e «Paaapa!»: e' la stessa famiglia, e la resa di Oxode va letta accanto a
quella.

⚠️ **L'inglese di monte appiattisce le cinque risposte del giocatore.** «Welcome!»
sta su cinque righe diverse e «Get out!» pure, ma il giapponese ne ha cinque
forme distinte, tarate sul personaggio: 「いいよ」, 「いいね」, 「そんなぁ」,
「これからよろしく」, 「【ちょっとだけよ】」. Si segue il giapponese, come nel lotto
degli evochat. Stessa cosa per «Okay, no turning back now!» a `:754`
(giapponese 「よい心がけだな」), che a `:740` era gia' reso «E allora andiamo, non si
torna indietro!»: la firma e' diversa perche' il giapponese e' diverso.

⚠️⚠️ **E a Halloween l'inglese ha scambiato le due voci.** `chatList 2` e'
「イタズラされる」 — *farsi* fare lo scherzetto — e infatti porta alla pioggia di
molotov di `:699`; `chatList 1` e' 「イタズラする」, ed e' il giocatore che fa lo
scherzetto (karma -2, «Guardie! Guardie!»). Monte le ha etichettate «Trick.» e
«Treat.», che in inglese vogliono dire il contrario. Si segue il codice.

⚠️ **Il lessico gia' fissato che questo lotto riusa**: «monete di platino»
(`:24935`), «monete d'oro», «allenare» / «potenziale» (`:394`, `:9104`), «zaino»
(il tutorial della 78a), e `guildname()` che rende «Gilda dei Maghi / dei
Guerrieri / dei Ladri» (`init.hsp:373`-`:379`). ⚠️ `guildname()` **non porta
l'articolo**, quindi la preposizione la scrive la resa: «della " + guildname()».

⚠️ `name(CHARA_PLAYER)` rende **«il viandante»** (`init.hsp:1704`), quindi `:559`
va in terza persona. `your()`, `him()` e `is()` a un argomento sono morfologia e
si tolgono; `cnvtalk()` porta le virgolette da fuori.

⚠️ **Il divieto di genere colpisce due volte in questo blocco**: chi parla e'
sempre un PNG a caso (niente «sono contento», «mi sono fermato», «vado fiero di
quanto sono bravo»), e chi ascolta e' il giocatore (niente «sei pronto?», «che
spilorcio!», «bastardo!» — e per l'insulto la guida di stile aveva gia' la
strada: «**la canaglia**» e' uno dei nomi a genere grammaticale fisso).
"""
import io
import json
import sys

ZONE = [(302, 944)]
ESTRAZIONE = 'scratchpad/_79-chat-tutte.jsonl'
USCITA = 'lavoro/fase4-chat-evento.jsonl'

RESE = {
    # ---- capodanno ----
    (310, 'Happy new year!'): 'Buon anno!',
    (311, "I've brought you a gift today, here."): 'Ti ho portato un regalo, tieni.',
    (317, ' throws you .'): 'name(tc) + " ti lascia " + itemname(ci, 1) + "."',

    # ---- il rancoroso e la molotov ----
    # ⚠️ l'insulto e' rivolto al GIOCATORE: «la canaglia» ha genere grammaticale fisso
    (321, "You scum! You won't get away from me now!"): 'Canaglia! Stavolta non mi sfuggi!',
    (323, 'Eat this!'): 'Prendi questo!',
    (336, ' throws a molotov.'): 'name(tc) + " lancia una molotov."',

    # ---- chi ha bevuto troppo ----
    (356, ' vomits.'): 'name(tc) + " vomita."',

    # ---- il bambino ----
    (367, 'Here, take this!'): 'Tieni, questo è per te!',
    (371, 'You receive .'): 'name(tc) + " ti regala " + itemname(ci, 1) + "."',
    (372, 'I hope I can make 100 friends♪'): 'Chissà se riesco a farmi cento amici!',

    # ---- il compagno che allena ----
    (403, "I see. I'll ask you again at some time in the future."):
        'Va bene. Te lo richiederò più avanti.',
    (411, "Fantastic! You've learned the skill in no time. I'm glad I could help."):
        "Magnifico! Hai imparato l'abilità in un attimo. Mi fa piacere aver dato una mano.",
    (416, "Marvelous! The training is now complete. I think you've improved your potential."):
        "Ecco fatto: l'allenamento è finito. Il tuo potenziale è cresciuto parecchio.",
    (423, "As a pledge of friendship, here's something for you!"):
        "In pegno d'amicizia, questo è per te!",
    (425, 'Your home has no empty spot...'): "In casa non c'è più un posto libero...",

    # ---- la visita col regalo ----
    (444, 'I just stopped by to see you. Oh, I happen to have a gift for you too.'):
        'Ero di passaggio e ho voluto salutarti. E già che ci sono, ho un regalo per te.',
    (446, 'Your inventory is full...'): 'Lo zaino è pieno...',
    (451, 'You receive .'): '"Ricevi " + itemname(ci, 1) + "."',
    (459, 'I found these during my journey. Thought you could find them useful.'):
        'Ho trovato questa roba durante il viaggio. Ho pensato che ti potesse servire.',
    (460, ' gives you a bag full of materials.'):
        'name(tc) + " ti consegna un sacco pieno di materiali."',

    # ---- le chiacchiere e il brindisi ----
    (471, ' is one of my favorite skills.'):
        'skillname(csskill) + " è una delle abilità in cui me la cavo meglio."',
    (477, "I'm proud of my good ."):
        '"Il mio orgoglio è " + skillname(csskill) + "."',
    (482, "Hey , how's your journey? I was bored to death so I decided to make a visit to you!"):
        '"Ehi, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", come va il viaggio? Mi annoiavo a morte e ho deciso di venirti a trovare!"',
    (483, 'You hold an amusing conversation with !'):
        '"Fai due chiacchiere in allegria con " + name(tc) + "!"',
    (489, "Let's have a drink and deepen our friendship!"):
        "Beviamoci sopra: l'amicizia ne guadagna!",
    (492, 'Cheers!'): 'Cin cin!',
    (508, 'I just wanted to say hi.'): 'Volevo solo salutarti.',

    # ---- il maestro di gilda e l'allenatore: il POTENZIALE ----
    (514, 'No more training in this month.'): "Per questo mese l'allenamento è finito.",
    # ⚠️ guildname() non porta l'articolo: la preposizione la scrive la resa
    (519, 'As a member of  you have to forge your talent to live up to our reputation. For only  '
          "platinum coins, I'll improve the potential of your talent."):
        '"Chi porta il nome della " + guildname() + " deve limare la propria arte senza sosta. '
        'A te che ne fai parte, per sole " + plat + " monete di platino, alzo il potenziale."',
    (538, 'Training! Training! At the end, only thing that saves your life is training! For only  '
          "platinum coins, I'll improve the potential of your talent."):
        '"Allenamento! Allenamento! Alla fine è l\'allenamento che ti salva la pelle! Per sole '
        '" + plat + " monete di platino ti alzo il potenziale."',
    (547, 'I want to improve .'): '"Allenare " + skillname(p(cnt))',
    (550, 'Not today.'): 'Non oggi',
    (553, "You'll regret this!"): 'Te ne pentirai!',
    # ⚠️ name(CHARA_PLAYER) rende «il viandante»: terza persona
    (559, ' potential of  greatly expands.'):
        'name(CHARA_PLAYER) + " vede crescere di molto il potenziale in " + skillname(chatval) + "."',
    (561, 'Good. You show a lot of potential.'): 'Bene. Hai molto da dare.',

    # ---- il mendicante ----
    (575, 'I got no money to buy food. Will you spare me some coins?'):
        'Non ho un soldo per mangiare. Mi dai due monete?',
    # him(tc) a un argomento e' morfologia: il destinatario lo nomina il giapponese
    (579, 'You spare   gold pieces.'):
        '"Dai " + p + " monete d\'oro al mendicante."',
    (584, "Thanks! I'll never forget this."): 'Grazie! Non lo dimenticherò mai.',
    (587, "You're so cheap!"): 'Quanta avarizia!',

    # ---- HALLOWEEN ----
    (633, 'Here, take my .'): '"Ti do " + itemname(tri10, 1)',
    (636, 'Here, take my .'): '"Ti do " + itemname(tri9, 1)',
    (639, 'Here, take my .'): '"Ti do " + itemname(tri8, 1)',
    (642, 'Here, take my .'): '"Ti do " + itemname(tri7, 1)',
    (645, 'Here, take my .'): '"Ti do " + itemname(tri6, 1)',
    (648, 'Here, take my .'): '"Ti do " + itemname(tri5, 1)',
    (651, 'Here, take my .'): '"Ti do " + itemname(tri4, 1)',
    (654, 'Here, take my .'): '"Ti do " + itemname(tri3, 1)',
    # ⚠️ monte ha scambiato le due etichette: si segue il codice
    (656, 'Trick.'): 'Farsi fare lo scherzetto',
    (657, 'Treat.'): 'Fare lo scherzetto',
    (658, 'Trick or Treat?'): 'Dolcetto o scherzetto?',
    (686, 'Yeah!'): 'Evviva!',
    (686, 'Happy Halloween!'): 'Buon Halloween!',
    (687, "As a pledge of friendship, here's something for you!"): 'Questo è per te!',
    (694, 'You receive .'): '"Ricevi " + itemname(ci, 1) + "!"',

    # ---- la guardia, l'ospite, il produttore ----
    (726, 'Ouch... Guards! Guards!'): 'Ahi... Guardie! Guardie!',
    (726, 'Come on!'): "Ma guarda un po'!",
    (737, 'So, are you ready?'): 'Allora, ci siamo?',
    (744, 'Hump!'): 'Pff!',
    (751, 'You want to be a star?'): 'Vuoi diventare una stella?',
    (754, 'Okay, no turning back now!'): "Ecco un bell'atteggiamento!",

    # ---- <Scard> la rondine felice ----
    (764, 'Welcome!'): 'Va bene, resta',
    (765, 'Get out!'): 'No, vattene',
    (766, 'You have to pay the rent.'): "Ma l'affitto lo paghi",
    (767, 'Let we live here! My wife was killed by the cat punch and our house was destroyed by '
          'the human punch...'):
        'Un pugno di gatto: moglie morta. Un pugno d\'uomo: casa distrutta. Ci ospitate sotto '
        'la tettoia?',
    (770, 'Thanks! I and my children are happy.'):
        'Grazie! Adesso io e i miei piccoli siamo felici.',
    (777, 'Oh...Where is happiness?'):
        "Ah... e dov'è, la felicità?",

    # ---- <Oxode> l'ape stregina ----
    (783, 'Welcome!'): 'Mi sta bene',
    (784, 'Get out!'): 'Non se ne parla',
    (785, 'I expect it.'): 'Aspetto il compenso',
    (786, "Let we live here! It's been a few years since my husband died of sex. I will give you "
          'a monthly reward, so please let me and my daughters live here...'):
        'Mio marito è morto di piacere qualche anno fa. Perdona la richiesta a bruciapelo: un '
        'compenso posso darlo, quindi lascia vivere qui me e le mie figlie.',
    (789, 'Thanks to you, my daughters will be less likely to fight enemies...'):
        'Mi salvi la vita. Così le mie figlie avranno meno bisogno di battersi con i nemici...',
    (797, 'Oh...Do you hate sweet honey?'): 'Oh, cielo... il dolce miele non ti piace?',

    # ---- <Imarituka> lo sberleffo di casa ----
    (803, 'Welcome!'): 'Ma dai...',
    (804, 'Get out!'): 'Fuori di qui, moccioso',
    (805, 'You will regret it.'): 'Ti faccio vedere io...',
    (806, 'Hehehe! This house is too nonsense and nonsense and interestiiiiing! I decided to live '
          'here！'):
        'Sgrunf! Uuuh~ ma che salotto senza gusto lmao! Fa troppo ridere, quindi resto qui un '
        "po'~",
    (809, 'Hehehe! Think about the arrangement of furniture properly...Oooooh, do you know what '
          'the furniture is???'):
        'Ma pensaci un attimo, a come disponi i mobili~ Ah, lmao, ma lo sai che cosa sono i '
        'mobili???',
    (813, 'I will come agaaaaain! Hehehe!'):
        'Sì, sì, va benissimo~ Tanto io ripasso lmaooo ahahahah!',

    # ---- <Telhureza> il geco di guardia ----
    (819, 'Welcome!'): 'Conto su di te',
    (820, 'Get out!'): 'Che schifo',
    (821, 'If you like this kind of house...'): 'Se ti basta questa casa...',
    (822, "I...I've always liked t...this house since I first saw it! Let me protect this "
          'house...Please!'):
        'Ah... da quando l\'ho vista la prima volta, io... io ho sempre amato questa casa! '
        'Lasciate che sia io a proteggerlaaa...!',
    (825, "I'm happy...like a dream! Pests approaching this house, I'll get rid of them...!"):
        'Evvivaaa... sembra un sogno! Gli insetti cattivi che si avvicinano li faccio fuori io~',
    (828, "I...I haven't given up yet!"): 'Io... io non mi arrendo mica! Veglierò su di lei per sempre!',

    # ---- <Momalaria> la gravida succhiasangue ----
    (835, '<Welcome!>'): '<Solo un goccio>',
    (837, 'Get out, monster!'): 'Vattene, mostro!',
    (838, "I feel like you'll suck all my blood out, so no."): 'No, mi prosciugheresti',
    (839, 'Please...donate blood...for the sake of my unborn babies...'):
        'Per i piccOli che ho in pAncia... donatemi il sAngue...',
    (843, "Yaaaaaay! I'll take all the bloooooooood!!"):
        'Ghiiiaaaaa! Me lo prEndo tuuuutto!!',
    (849, 'The real monster...might be you...'):
        'Il mostro vEro... chi sarà, di noi due?',
    (854, 'Wait a moment...10 liters...no, even 8 liters would be fine...!'):
        'AspEtta! Dieci litri! Va bEne anche otto, dai!',

    # ---- il mercante che se ne va ----
    (893, "I hope you won't regret it later."): 'Poi non venirmi a dire che te ne penti.',

    # ---- il caposquadra del Dock ----
    (905, 'I had something come up, so...'): 'Mi è venuta una cosa urgente...',
    (906, 'I decided that returning home would improve my efficiency.'):
        'Ho valutato che tornando a casa renderei di più.',
    (907, "Hey, YOU! Why are you leaving NOW while everyone else here is working their asses off? "
          "So you think that YOU'RE the only person that matters here, is that it? ...HEY! Are you "
          'LISTENING to me!?'):
        'Ehi, TU! Qui si spaccano tutti la schiena e tu te ne vai?? Ah, ho capito: basta che stia '
        'bene TU, e chi se ne frega degli altri, eh? ...Ehi! Mi stai ASCOLTANDOOO!?',
    (911, '\\"But I\'m new here, and I\'m so scared, and blah blah blah...\\" BULLSHIT! That\'s not '
          'how things work here, dumbass! There\'s this thing called \\"common sense\\", yeah? '
          'Might have heard of it somewhere? USE IT!'):
        '\\"Eh, ma io sono nuovo, ho paura, bla bla bla...\\" STRONZATE! Qui non funziona così, '
        'testa di rapa! C\\"è una cosa che si chiama buonsenso, sai? Mai sentita nominare? USALA!',
    (915, 'What the HELL are you doing going off and deciding that on your own? Oh, for the sweet '
          "love of... Alright! So you'll be more efficient that way? Is that right? FINE! Go right "
          "ahead! But don't blame ME when you come groveling back and get smacked across the face "
          'with a pink slip!'):
        'Ma chi sei tu per decidere da solo?! Basta, fa\' come ti pare! Renderesti di più così, eh? '
        'Ah sì? E allora prova! Ma se il tuo lavoro non finisce, io non ne so niente!!!',
    (924, "Ah, so you're the new guy the captain recommended. If you've got any questions, ask me. "
          "I'm the leader of this joint."):
        'Ohò. Saresti tu la recluta che ha raccomandato il capitano. Se c\'è qualcosa che non ti '
        'torna, la chiedi a me, che qui sono il caposquadra.',
    (925, 'Please tell me about each of the jobs.'): 'Mi spiega in che consistono i lavori?',
    (926, 'I heard there were some malfunctioning machines.'):
        'Ho sentito che ci sono macchine impazzite.',
    (927, "I'll cut to the chase. Here's your work assignment. Work A:  units. Work B:  units. "
          'Work C: units. Get to it.'):
        '"Andiamo al sodo: quel che ti tocca è lavoro A: " + gdata(GDATA_FLAG_WORK_A_REMAINING) + '
        '", lavoro B: " + gdata(GDATA_FLAG_WORK_B_REMAINING) + ", lavoro C: " + '
        'gdata(GDATA_FLAG_WORK_C_REMAINING) + ". Conto su di te."',
    (931, "What? You don't even know THAT? Couldn't you at least look it up yourself before trying "
          'to waste my time?'):
        'Ah? Non lo sai neanche questo? Almeno guardatelo da solo, prima di venire a chiedere???',
    (936, 'What the hell are you talking about? Shut up and do your job. You came late to the '
          "party, so you'd better be a speedy one or you're never gonna finish!"):
        'Ma che stai dicendo? Chiudi il becco e lavora. Sei arrivato per ultimo, quindi se non '
        'corri non finisci più!',
}


def main() -> int:
    voci = []
    for l in io.open(ESTRAZIONE, encoding='utf-8'):
        v = json.loads(l)
        if not any(a <= v['riga'] <= b for a, b in ZONE):
            continue
        if (v['riga'], v['en']) in RESE:
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        k = (v['riga'], v['en'])
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:90]))
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci, %d firme' % (USCITA, len(voci), len({v['firma'] for v in voci})))
    return 0


if __name__ == '__main__':
    sys.exit(main())
