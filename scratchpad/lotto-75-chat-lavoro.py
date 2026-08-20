# -*- coding: utf-8 -*-
"""75a — `chat.hsp`, «Parliamo di lavoro»: il capo del Dock.

`chatval == 108` (10 rese) e `chatval == 107` (85) sono una scena sola: il capo
reparto della nave-fabbrica, la sotto-missione di Garziem. Il giocatore e' una
matricola appena assegnata, il capo lo maltratta, e il menu che porta qui e'
gia' italiano dalla 73a.

⚠️ **Il genere e' vietato DUE volte in questo lotto.**

1. **Il giocatore** puo' essere maschio o femmina: mai un aggettivo o un
   participio accordato su «tu» (`guida-stile.md`). La via d'uscita e' il **nome
   predicativo**, che non accorda: «sei una mezza calzetta», «un pezzo di merda
   come te», «la fortuna qui e' TUA» invece di «il fortunato sei tu».
2. ⚠️⚠️ **E in `chatval == 107` anche il PARLANTE**: il blocco non ha nessun
   ramo su `CDATA_SEX`, quindi il capo puo' essere l'uno o l'altra. «Quando sono
   arrivato io» sarebbe sbagliato meta' delle volte: si dice «ai miei tempi».
   In `chatval == 108` invece il ramo c'e' (`:22618`), quindi li' il parlante si
   puo' accordare.

⭐ **Registro**: `elona-convenzioni-traduzione` dice che il registro volgare si
tiene. Il capo insulta, e l'italiano insulta. Le voci di menu del giocatore
seguono il **giapponese**, che qui e' in forma cortese (ですます), ma con il
«tu» che il progetto usa dappertutto.

⭐ **Le due schermate che dicono la stessa scelta usano le stesse parole**: le
voci del voto (`:22715`, `:22716`) sono «Serve migliorare» / «Nessun problema»,
e lo spoglio (`:22720`-`:22729`) ripete quelle due, non sinonimi.

**Le misure lette nel sorgente, non a occhio:**

    chat.hsp:25226   talk_conv buff, 56 - en * 3      la battuta va a capo a 53
    chat.hsp:25728   y = wy + 43 + cnt * 19           prima riga a 43, passo 19
    chat.hsp:25161   y = wy + wh - 56 - keyrange*19   i bottoni risalgono dal basso
    menu_dialogo     chat_select                      voce di menu: tetto 58

Quindi le righe di battuta che ci stanno sono `(324 - opzioni*19 - 43) // 19`:
13 con un bottone solo (`chatMore`), 12 con due, 11 con tre, 8 con sei.

    python scratchpad/lotto-75-chat-lavoro.py
"""
import io
import json
import sys

USCITA = 'lavoro/75-chat-lavoro.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
DA, A = 22616, 22961

RESE = {
    # --- chatval 108: le cinque battute del capo maschio (:22618, ramo SEX==0)
    22620: 'Adesso ti educo io, con tutto comodo. E il \\"grazie mille\\", dov\'è?',
    22623: 'A guardarti bene, però, hai un bel fisico... Ehi, ehi, calma, è solo un po\' di confidenza, non fare storie. Gheh gheh.',
    22626: 'Ehi, matricola. Se mi rovini la reputazione, la paghi cara.',
    22629: 'Falla giusta al primo colpo! Porca miseria! Ma com\'è che in questo reparto hanno preso un pezzo di merda come te?!',
    22632: 'Mi sa che non hai ancora capito come gira qui dentro. Che ne dici se te lo faccio entrare in testa a suon di botte?',
    # --- chatval 108: le cinque del capo femmina (ramo else)
    22637: 'Uffa, voi matricole non servite proprio a niente! Ehi, gente! Questa mezza calzetta ci sta tirando giù tutti!',
    22640: 'E che me ne importa se ti lamenti? Faccio rapporto al capo che la matricola ha marinato il lavoro!',
    22643: 'Pulire questo schifo per terra è compito della matricola! Non capisci nemmeno una cosa così semplice? Nel reparto di prima dovevano trattarti coi guanti!',
    22646: 'Ti leggo dentro come un libro aperto! Stai solo cercando di ingraziarti il capo, vero?! Che meschinità! CHE MESCHINITÀ! Mi viene da vomitare solo a guardarti quella faccia schifosa!',
    22649: 'Chi c\'era prima di te rendeva un po\' di più. Peccato che ad andare in pezzi sia stato lui e non tu...',

    # --- chatval 107: il menu del lavoro (3 voci -> la battuta ha 11 righe)
    22683: 'Farò del mio meglio!',
    22684: 'In realtà c\'è una cosa che non ho ben capito...',
    22686: 'Serve migliorare le condizioni di lavoro',
    22688: ('"Ti resta da fare... Lavoro A: " + gdata(GDATA_FLAG_WORK_A_REMAINING)'
            ' + ", Lavoro B: " + gdata(GDATA_FLAG_WORK_B_REMAINING)'
            ' + ", Lavoro C: " + gdata(GDATA_FLAG_WORK_C_REMAINING) + "."'),
    22692: 'Ah sì? E ci mancherebbe altro. Impegnarsi lo sanno fare tutti! Non ti entra in testa che uno vale i risultati che porta? Ma del resto, da te che altro potevo aspettarmi?',
    22697: 'Tu sei qui su raccomandazione del capitano. Ma che diavolo stai dicendo? Non ti vergogni? Torna là fuori e spaccati la schiena con un po\' d\'orgoglio, matricola!',

    # --- chatval 107: il menu delle riforme (6 voci -> la battuta ha 8 righe)
    22704: 'Parlerò coi superiori per farci ridurre l\'orario!',
    22705: 'Perché non ci scambiamo le competenze di lavoro?',
    22706: 'Bisognerebbe sentire il parere di tutti!',
    22707: 'Perché non andiamo tutti in manutenzione?',
    22708: 'Qui è tutto fuori norma, non so da dove cominciare...',
    22709: 'Ti faccio fuori e divento io il nuovo capo!',
    22710: 'Come sarebbe a dire \\"serve\\"? Ci diamo tutti da fare e tiriamo avanti lo stesso! Che altro ti SERVIREBBE, di grazia?!',

    # --- chatval 107: il voto
    22714: 'Eh? Quindi se ti dico quello che vuoi sentire te ne vai, giusto?',
    22715: 'Serve migliorare!',
    22716: 'Nessun problema',
    22717: 'Comunicazione di servizio. Avvio della procedura di voto. Si prega di votare al più presto.',
    22720: 'Inizio dello spoglio. Serve migliorare: 1 voto. Nessun problema: 1 voto. Affluenza: 10%.',
    22721: 'Serve migliorare: 3 voti. Nessun problema: 2 voti. Affluenza: 25%.',
    22722: 'Serve migliorare: 7 voti. Nessun problema: 3 voti. Affluenza: 50%.',
    22723: 'Serve migliorare: 9 voti. Nessun problema: 5 voti. Affluenza: 70%.',
    22726: 'Spoglio completato. Il risultato è il seguente:',
    22727: 'È un broglio!',
    22728: 'Un\'affluenza del 600% non è un errore di conteggio?',
    22729: 'Serve migliorare: 15 voti. Nessun problema: 105 voti. Affluenza: 600%. Se ne conclude che l\'ambiente di lavoro attuale non presenta problemi. Visto? Non c\'era niente di cui preoccuparsi.',
    22733: '...Me l\'hai appena detto in faccia? DAVVERO?! E le prove dove sono? ...Niente? E allora STAI ZITTO! Non si contesta una cosa che è già stata messa ai voti! Ma PORCA MISERIA! Che cos\'hai che non va?! Ogni volta che hai torto ti metti a fare i capricci... Dovresti vergognarti.',
    22738: 'Come sarebbe? Nemmeno io sono infallibile, quindi può darsi che abbia sbagliato e contato i voti di qualcuno che è già stato rottamato, o contato più volte il voto della stessa persona.',
    22739: 'Ma anche se avessi sbagliato, non basterebbe a cambiare il risultato, mica come gli errori che fai TU! E tanto per essere chiari, non ho nessuna intenzione di rifare lo spoglio: non cambierebbe niente.',

    # --- chatval 107: ridurre l'orario
    22746: 'Piantala, testa di rapa! Cosa, staresti dicendo a ME e a tutti quelli là fuori che non siamo capaci di fare il nostro lavoro? Non metterci nello stesso sacco con te e la tua pigrizia!',
    22747: 'Sì, è vero che il carico di lavoro di questo reparto cresce ogni anno. Ma anche se aumenta il carico per macchina, e anche se qualche macchina va in pezzi, quel lavoro qualcuno lo deve fare lo stesso.',
    22748: 'E se qualcuno deve venire a dirci come si manda avanti questo posto, perché diavolo dovresti essere proprio TU? Sei qui da quattro giorni e non distingui la destra dalla sinistra! Piantala con le stronzate e smettila di farci la lezione! Mi vergogno solo a stare nella stessa stanza di un pezzo di merda come te.',

    # --- chatval 107: scambiarsi le competenze
    22752: 'Ehi, tu. Siediti.',
    22753: 'Non me ne frega niente se ti piazzi per terra. Adesso ascoltami beeeene.',
    22754: 'Credi davvero di poterti ficcare tutto il mestiere in quel cervello da quattro soldi solo stando a chiacchierare? No che non ci riesci. Per farlo come si deve, ognuno dovrebbe portarsi appunti e materiale alla riunione.',
    22755: 'Certo, per una matricola come te, che ha pochi incarichi e un sacco di tempo libero, sarebbe un affarone. Ma tutti gli altri qui dentro? ...Ma non ci vedi? Ce li hai due occhi che FUNZIONANO?',
    22756: 'Capirei il discorso se uno avesse tempo da buttare. Ma sai che c\'è? Ogni singolo incarico su cui tutti gli altri si stanno spaccando la schiena ha una cosa che si chiama \\"scadenza\\". Ne avrai sentito parlare, no? Qui dentro sei l\'unica persona che può lavorare col proprio comodo.',
    22757: 'Sì, ho capito che è importante mettere per iscritto il prezioso mestiere. Ma messe così le cose, non è solo altro lavoro che nessuno ha bisogno di fare? L\'unico risultato è costringere tutti ad adattarsi ai TUOI tempi e a rincorrere le ore perse. Un piano geniale, non c\'è che dire. Smettila di farti tanti pensieri e torna a lavorare.',

    # --- chatval 107: la manutenzione
    22762: 'Lo dici solo per battere la fiacca, vero? Puoi ripetere \\"manutenzione, manutenzione\\" quanto ti pare, ma è una faccenda lunga, lo sai? Secondo te che cosa conta di più: il lavoro da consegnare adesso, o la tua salute in un domani che non si sa quando? Quello che sto cercando di ficcarti in quella zucca vuota è: decidi quali sono le TUE priorità e difendile!',
    22765: 'Anche gli altri non sembrano stare bene',
    22766: 'Potrebbe essere una brutta malattia, per sicurezza!',
    22767: '...Lo dico solo a te: da un po\' non mi sento tanto bene neanch\'io. Tutto il reparto va avanti così a rilento che mi fa girare le scatole. Ed è proprio per questo che non credo possiamo permetterci di andare in manutenzione.',
    22771: 'Puah! Come fanno a stare male se non hanno quasi niente da fare? Ai miei tempi si lavorava molto di più. Se l\'unica cosa che sanno fare è lamentarsi per QUESTA quantità di lavoro, allora non valevano niente fin dall\'inizio!',
    22775: '...A tirar fuori questa cosa mi metti in agitazione.',
    22776: 'Va bene, per adesso facciamo una scansione rapida, dieci secondi, e solo chi risulta sospetto passa al controllo approfondito. E dopo *quello*, solo chi non lo supera va in manutenzione. Mi pare un buon piano.',
    22777: 'Del resto, mica conosco qualcuno messo così male da non superare una scansione del genere!',

    # --- chatval 107: «non so da dove cominciare»
    22793: 'Sì...',
    22794: 'Se il metodo è fuori norma, è fuori norma',
    22795: 'Cioè, certo, se paragoni questo posto al negozietto di fiori di tua madre, allora sì, magari qui si va un po\' più fuori norma. Ma pensaci. Anche tu capisci che serve tutto questo per portare a casa il lavoro, no?',
    22799: 'Non prendermi in giro. Se davvero pensassi che c\'è qualcosa che non va, non verresti a frignare da me, giusto? Porca miseria... Sei una gran rottura di scatole da starti a sentire. Non è che puoi farci qualcosa?',

    # --- chatval 107: la sfida al capo
    22803: 'Tu... PEZZO DI MERDA! FUORI DAI PIEDI!!!!',
    22810: 'IMBECILLE!!',
    22811: 'Anche se riuscissi a farmi fuori, una mezza calzetta come TE, che è già stufa del proprio lavoro, sarebbe MAI in grado di reggere tutto il lavoro di cui rispondo IO?! Pensaci DUE volte prima di ripetermi certe stronzate!',

    # --- chatval 107: il lavoro finito, e il giro dei tre incarichi
    22823: 'Allora hai finito il lavoro assegnato, eh? Visto che se ti impegni ci riesci. Però hai buttato via un sacco di tempo. La prossima volta mi aspetto che tu faccia più in fretta.',
    22827: 'Bene, ecco il prossimo incarico. Fatti una bella sorsata di questo, poi torna là fuori e fammi fare bella figura.',

    22843: 'Il Lavoro A è aumentato...',
    22844: 'Dove ho sbagliato di preciso?',
    22845: 'Come faccio a non sbagliare la prossima volta?',
    22846: 'Non stai facendo un po\' troppi errori? Ricomincia da capo. Per quanto uno si impegni, basta un solo errore e tutto quel tempo non è servito a niente.',
    22850: 'Arrangiati. Se devo indicarti io ogni minima cosa, tu qui a fare che ci stai?',
    22855: 'Se avessi davvero capito che cosa devi fare, non faresti tutti questi errori! Ti agiti a vuoto senza capire niente e speri che alla fine si aggiusti tutto! Non c\'è da stupirsi se è venuta fuori questa robaccia! Se non capisci che cosa devi fare, CHIEDI!!!',

    22865: 'Il Lavoro B è aumentato...',
    22866: 'Non è meglio lasciarlo com\'era?',
    22867: 'Cambiamo formato, così poi si modifica facilmente',
    22868: 'Allora, per il Lavoro B, dimentica tutto quello che hai fatto. Rifallo in un altro modo. E poi cambia il formato del documento e aggiungi un\'altra sezione.',
    22872: 'Forse fino a oggi te la sei cavata così, ma qui dentro non attacca! Chiudi il becco e datti da fare, una buona volta!!!',
    22878: 'E va bene, allora te ne occupi tu. Ma non farmi perdere tempo a rigirartelo troppo a lungo.',

    22887: 'Il Lavoro C è aumentato...',
    22888: 'Va bene...',
    22889: 'Veramente ho ancora altro lavoro da fare...',
    22890: 'Tu, sbrigati a darmi una mano anche col mio lavoro.',
    22894: '*sospiro*... Ma posso davvero fidarmi di te? Vedi di portare dei risultati, o ti salto addosso.',
    22899: 'Ma che diavolo ti prende? Io qui mi sto spaccando la schiena per fare in modo che a TE, che non ringrazi mai, tocchino meno incarichi in più possibile, chiaro? Il minimo che puoi fare è portare avanti questo, intanto! Ma guarda te... Ti credi chissà chi, vero?!',

    # --- chatval 107: il ritardo
    22909: 'Chiedo scusa',
    22910: 'Stavo solo mettendo un po\' in ordine',
    22911: 'Perché nessuno mi spiega come si fa',
    22912: 'Ma che DIAVOLO ci metti tanto a fare!!!',
    22916: 'Ai miei tempi il carico di lavoro era TRE VOLTE quello che hai tu! Allora i criteri erano molto più larghi, quindi non c\'era da rifare tutto ogni volta: la fortuna qui è TUA.',
    22921: 'Fatti un favore e smettila subito di tirare fuori scuse del genere. Mettere in ordine è importante, ma ci stai perdendo troppo tempo! Fatti una tabella di marcia come si deve e rispettala, per l\'amor del...',
    22926: 'Ma senti che insolenza! Esatto, sei solo una piaga che frigna in continuazione. Devo davvero rubare tempo alla MIA agenda per insegnarti da zero quali sono le TUE responsabilità? Basterebbe che ci PENSASSI una volta e ci arriveresti anche tu!!!',

    # --- chatval 107: licenziarsi
    22936: 'Vorrei licenziarmi',
    22937: 'Neanche il dio delle macchine vorrebbe un posto così!',
    22938: 'Sai benissimo che cosa ti aspetta, no? Dal momento in cui ti hanno assegnato qui, sei una bestia da soma dell\'azienda! La tua esistenza si regge sulla devozione assoluta alla ditta! È la volontà divina!',
    22942: 'E non guardarmi con quella faccia. Credi di poter dire tutto quello che ti pare! Fai la parte di chi se la passa male, ma nemmeno a me fa piacere stare qui a parlarti!',
    22948: 'Ti rendi conto che il mondo funziona così, vero? Dovunque tu vada a lavorare dopo, non sarà più facile. Se basta questo per farti frignare, non hai nessuna speranza di cavartela là fuori!',
    22953: 'Una bestia da soma non ha bisogno di nessun dio!! E per i robot non esiste nessuno statuto dei lavoratori...!!',
}


def main() -> int:
    voci = []
    for l in io.open(RESTANTE, encoding='utf-8'):
        v = json.loads(l)
        if DA <= v['riga'] <= A:
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        r = v['riga']
        if r not in RESE:
            errori.append('%d: voce senza resa' % r)
            continue
        viste.add(r)
        v['it'] = RESE[r]
    for r in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto' % r)
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci' % (USCITA, len(voci)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
