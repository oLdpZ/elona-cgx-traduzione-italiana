# -*- coding: utf-8 -*-
"""L'ESERCITO (84a): tre militari, tre incarichi. chat.hsp

    :3581-:3648  Gilbert il colonnello    l'esercito di liberazione juere
    :3649-:3709  Arnord il soldato ferito lo squadrone kamikaze
    :5629-:5671  Conery il generale       il minotauro re

Tre zone chiuse, 34 firme, zero fuori. Il lessico e' tutto nei DIARI:

    text.hsp:10257  «Il Colonnello Gilbert, a Yowyn», «l'esercito di
                    liberazione juere»
    text.hsp:10317  «Arnord, a Porto Kapul», «lo squadrone kamikaze»
    text.hsp:10325  «reggere all'assalto dello squadrone kamikaze finche'
                    l'esercito di Palmia non avra' completato la ritirata»
    text.hsp:10583  «Il generale <Conery>, a Palmia», «il covo»
    init.hsp:386    «chief» -> «capovillaggio»
    action.hsp:16746 «minotaur king» -> «il minotauro re»
    command.hsp:15309 «ranged equipment» -> «equipaggiamento da TIRO»: e' il
                    nome che il giocatore legge sulla casella, quindi «arma da
                    Tiro» e non «arma a distanza»

⭐⭐ IL DIARIO HA GIA' DEROGATO, E LA DEROGA SI EREDITA. `:3684` in inglese
dice «I'll tell the Palmian army to begin a steady retreat», ma il giapponese
dice 「パルミア軍の撤退が完了次第、連絡を入れます」, «appena la ritirata sara'
completa ti faro' avvisare» — e `text.hsp:10325`, gia' reso, dice proprio «A
ritirata compiuta arrivera' l'avviso». La riga di dialogo non poteva
contraddire il diario che la annota. E' la regola della 82a (il pantheon) vista
da sotto: qui la deroga non e' stata scelta, e' stata IMPOSTA da una resa
vecchia.

⭐ L'EPITETO DEL GIOCATORE, `:3594`. `cdatan(CDATAN_AKA, CHARA_PLAYER)` e' un
sintagma intero e di genere qualunque («fragore della dipendenza»), quindi «il
famoso X» si romperebbe a ogni tiro. La forma che regge e' l'apposizione senza
articolo, gia' usata a `chat.hsp:16472` e `main.hsp:4048`: «Ma tu sei X in
persona!» — «in persona» e' invariabile.

⚠️ Il genere del GIOCATORE, cinque volte, e ogni volta una parola diversa:
  :3584  «the bravest of the brave» -> «il coraggio in persona» (non «il piu'
         valoroso»)
  :3600  «coward»                   -> «ti manca il fegato» (non «codardo»)
  :3604  «once you've prepared»     -> «quando sei in ordine» (non «pronto»)
  :3643  «your heroic figure»       -> «il tuo valore» (non «la tua figura
         d'eroe»)
  :3704  «you made it back alive»   -> «da quel massacro si potesse tornare»
         (non «tornato vivo»)
  :5654  «you've returned»          -> «eccoti» (non «sei tornato»)

⚠️ `:5637` e' `lang(strbye, "No way.")`: il ramo giapponese e' una MACRO, non
una stringa, quindi il campo `jp` esce vuoto. Si traduce lo stesso — quel che
`applica` riscrive e' il ramo inglese.

⚠️ Due nomi per la stessa creatura, controllati: il diario dice «il capo dei
minotauri» (descrizione), `action.hsp:16746` dice «il minotauro re» (nome). Nel
dialogo si usa il NOME, che e' quel che il giocatore legge sulla creatura.
"""
import io, json, sys

RESE = {
    # ---------------- GILBERT, il colonnello ----------------
    3584: 'Ah, il coraggio in persona! Una bevuta? Muahahah!',
    3588: 'Vattene. I deboli non mi interessano. Muahahah!',
    3594: '"Per Opatos! Ma tu sei " + cdatan(CDATAN_AKA, CHARA_PLAYER) + " in '
          'persona! Ho un favore da chiedere a chi vale come te."',
    3595: '(Stare a sentire)',
    3596: '(Non immischiarsi)',
    3597: 'Sono Gilbert, colonnello dell\'esercito di liberazione juere. Non '
          'siamo l\'esercito regolare, ma abbiamo tutta l\'intenzione di '
          'liberare i territori juere dall\'occupazione di quei cani di Yerles. '
          'Solo che al confine di Palmia le nostre truppe faticano contro una '
          'linea difensiva formidabile: loro hanno armi all\'avanguardia, noi '
          'soltanto le spade. Di questo passo rischiamo di essere annientati. '
          'Perciò te lo chiedo: vuoi prestarci la tua forza?',
    3600: 'Muahahah! Ti manca il fegato!',
    3604: 'Muahahah! Così mi piace. Contiamo su di te. Quando sei in ordine '
          'torna a parlarmi.',
    3609: 'Sono a posto',
    3610: 'Non ancora',
    3611: 'I preparativi sono a posto, dunque?',
    3614: 'Ti aspettiamo.',
    3623: 'Ahah! Che la protezione di Opatos sia con te!',
    3643: 'Muahahahah! Muahahahahah! Mu-mu... ah...! *tosse* *tosse* Chiedo... '
          'chiedo scusa. Il tuo valore sul campo di battaglia mi ha scosso fin '
          'nelle ossa. Adesso l\'esercito di liberazione può varcare il confine '
          'di Palmia. Accetta questa ricompensa, come segno della mia '
          'gratitudine.',

    # ---------------- ARNORD, il soldato ferito ----------------
    3652: '"Spero che ci sia occasione di riparlare, " + cdatan(CDATAN_NAME, '
          'CHARA_PLAYER) + "!"',
    3656: 'In questo momento il decimo reggimento dell\'esercito di Palmia è '
          'impegnato in battaglia contro lo squadrone kamikaze! Il nemico ha '
          'sfondato il nostro fuoco di sbarramento e ci assale con attentatori '
          'suicidi: sanno di morire e vogliono portarci con loro. Come si '
          'combatte un nemico che non tiene alla propria vita? Di questo passo '
          'saremo annientati! Ci serve che tu ci dia una mano e guidi i '
          'rinforzi.',
    3657: 'Accetto',
    3658: 'Sembra pericoloso... no, grazie',
    3661: 'Mi dispiace sentirlo.',
    3665: 'Grazie al cielo. Chiamami quando sei in ordine. E mi raccomando: '
          'porta un\'arma da Tiro!',
    3670: 'Bene, si parte',
    3671: 'Non ancora, aspetta',   # 19: sotto il tetto delle due colonne
    3672: 'Sei in ordine? Ci serve che tu regga all\'assalto dello squadrone '
          'kamikaze e guadagni tempo per la ritirata dell\'esercito di Palmia.',
    3675: 'Sbrigati!',
    3684: 'Allora un messo ti porterà sul posto. Qualunque cosa succeda, non '
          'lasciarli avvicinare! Ti farò avvisare appena la ritirata sarà '
          'completa.',
    3704: 'Ottimo lavoro. Non credevo che da quel massacro si potesse tornare! '
          'I miei commilitoni sono salvi: non ho parole per ringraziarti. '
          'Accetta la ricompensa.',

    # ---------------- CONERY, il generale ----------------
    5632: 'Ah, sei tu. Per quel favore ti devo molto. Che ne dici, non ti va di '
          'entrare nel mio reparto?',
    5636: 'Ci penso io!',
    5637: 'Neanche per sogno',
    5638: 'Che guaio... che brutto guaio. Ehi, tu: non potevi capitare in un '
          'momento migliore. Yowyn rischia di essere rasa al suolo '
          'dall\'esercito dei minotauri. Il capovillaggio di Yowyn è un caro '
          'amico e non voglio lasciarlo nei guai, ma un distaccamento non posso '
          'mandarlo: l\'aria che tira a Palmia è troppo pesante e le truppe '
          'devono restare al castello. Per questo mi rivolgo a te, che vai '
          'all\'avventura. Vuoi andare tu ad attaccare il covo dei minotauri? '
          'La ricompensa, naturalmente, sarà all\'altezza.',
    5641: 'Lo sapevo... e in fondo, chi non rifiuterebbe?',
    5645: '"Come? Davvero?! Magnifico! Va\' al covo dei minotauri, a sud di '
          'Yowyn, e portami la testa del minotauro re. Che le divinità ti '
          'accompagnino, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "."',
    5650: 'Che c\'è? Devi fare in fretta: Yowyn è in grave pericolo.',
    5654: 'Eccoti, ti aspettavo. Non serve il rapporto: la voce di chi ha '
          'abbattuto il minotauro re mi è già arrivata all\'orecchio. Prendi '
          'questo, come segno della mia gratitudine.',
}

LOTTO = 'lavoro/84-chat-esercito.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
mancanti = [v['riga'] for v in voci if v['riga'] not in RESE]
in_piu = [r for r in RESE if r not in {v['riga'] for v in voci}]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print('in piu\' : %s' % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[v['riga']]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
