# -*- coding: utf-8 -*-
"""Le rese di LUNE, la capo cameriera (84a): chat.hsp :7431-:7596, zona chiusa.

Un sistema intero: la villa in vendita, i due milioni, il sotterraneo infestato,
e i tre contatori di simpatia (maidsikari, maidkimoti, maidhome).

Il lessico e' stato letto, non deciso, e quasi tutto stava nel DIARIO che
annota questi stessi eventi:

    ご主人様          Master              Padrone        text.hsp:112
    メイド            maid                cameriera      screen.hsp:1666
                                                         (Lune stessa, gia' resa)
    屋敷              mansion             villa          text.hsp:10825 (diario)
    金貨200万枚        2 million gp        due milioni di monete d'oro
                                                         text.hsp:10817 (diario)
    ルードゥス        Ludus               Ludus, «borgo rurale»  text.hsp:3003
    掃除人形          Cleaning Doll       Bambola delle Pulizie  db_item
    大きな...バスケット  large picnic basket cesto da picnic grande db_item

⚠️ La mappa si chiama «Villa Domestiche» (`text.hsp:3033`), ma Lune nella sua
riga gia' resa dice «cameriere». Dentro il dialogo si dice **cameriere**: e' la
parola che la usa il personaggio, e l'etichetta della mappa e' compressa per
stare nella sua colonna.

⚠️ Le due trappole del genere, e tutt'e due riguardano il GIOCATORE:
`:7435` «I'm glad you're safe» non puo' diventare «sei salvo», e `:7493` «So you
noticed» non puo' diventare «te ne sei accorto». Diventano «stai bene» e «l'hai
notato» — il participio si accorda con «lo», non con chi legge.

⚠️ La deroga dichiarata e' `:7592`: l'inglese dice «Ludus is a rural area ever
far from here» e ha perso il 東 del giapponese. La direzione e' un'indicazione
che serve al giocatore, e si segue il giapponese: «molto piu' a EST di qui».

💡 `:7463` e `:7484` sono una COPPIA: la voce di menu e' quella che Lune cita
dentro le virgolette due battute dopo. Le due rese si scrivono insieme, o la
citazione non cita niente.
"""
import io, json, sys

RESE = {
    # --- il finale della vicenda: i demoni scacciati, la bambola ---
    7435: 'Padrone, meno male, stai bene! Se ne stavano radunando altri, di '
          'quegli esseri ripugnanti, ma pare che alla morte del capo siano '
          'scappati tutti!',
    7436: "Ah, e davanti alle scale del sotterraneo c'era questa. L'avrà "
          'lasciata la disinfestazione? Comunque è giusto che la tenga tu, '
          'Padrone.',

    # --- il regalo delle cameriere ---
    7447: "Ehm... questo l'abbiamo preparato tutte insieme, noi cameriere. "
          'Assaggialo, se ti va. Spero che sia di tuo gusto...',

    # --- il menu della villa comprata ---
    7455: 'Scendere nel sotterraneo',
    7458: 'Scendere a disinfestare il sotterraneo',
    7461: 'Degli insetti hanno rovinato la cucina',
    7463: 'Ti va qualcosa di bello?',   # 24 esatti: il tetto delle due colonne
    7464: "Qui c'è ancora tutta questa polvere",
    7465: 'Stai lavorando bene',
    7466: "C'è qualcosa che posso fare per te?",

    # --- il rimprovero (maidsikari) ---
    7470: 'E-ehm... non infierire così, ti prego...',
    7473: 'Scusa! Scusami tanto! Rifaccio subito le pulizie!',

    # --- la proposta indecente (maidkimoti) ---
    7480: 'B-basta con questi discorsi!',
    7483: 'I-io penso che le cose sconce siano sbagliate!',
    7484: '...Eh? Come? Quando hai detto \\"qualcosa di bello\\", non intendevi '
          '\\"quello\\"...?',
    7487: 'Ghh!? N-no! Assolutamente no! T-torno al lavoro!',

    # --- gli insetti in cucina, e la discesa ---
    7493: "! Allora l'hai notato anche tu, Padrone... Quegli esseri ripugnanti "
          'salgono dal sotterraneo, e per quante volte li scacciamo non '
          'finiscono mai. Giorni fa abbiamo mandato giù dei disinfestatori, ma '
          'non è tornato nessuno... Non so proprio come fare...',
    7498: 'Il rischio me lo prendo',
    7499: 'Allora lascio stare',
    7500: 'Vuoi andarci tu, Padrone?! Non se ne parla! È troppo pericoloso!',
    7503: 'Meno male! Riproviamo con i disinfestatori.',
    7511: "...Vedo che non c'è verso di fermarti. Va bene, al sotterraneo ti "
          'accompagno io. Di qua, prego...',
    7528: 'Come...? Vuoi tornare nel sotterraneo? Devi sistemare la roba che c\'è '
          'laggiù? M-ma non è che ci sono ancora dei resti di quei demoni...?! '
          'C-comunque ti accompagno, di qua.',

    # --- il complimento (maidhome) ---
    7541: 'Uffa... non lodarmi così tanto, mi fai vergognare!',
    7544: 'Grazie mille... Ehehe, sono stata lodata.',
    7550: 'Buon lavoro là fuori, Padrone!',

    # --- la villa in vendita ---
    7554: 'Compro io la villa',
    7556: "Ahh... Eh? Che c'è? Be', il mio padrone ha mandato all'aria i suoi "
          'affari e adesso è sommerso dai debiti. Così ha messo in vendita la '
          'villa e insieme ha licenziato tutte noi cameriere. Ahh... Adesso devo '
          'trovarmi un altro lavoro, ma qui intorno non cerca nessuno...',
    7559: 'Arrivederci... Forse è meglio che torni a casa da mia madre... Ah, '
          'potrei sempre vendere gli organi!',
    7562: 'Il pensiero mi fa piacere, ma... la villa è in vendita a due milioni '
          'di monete d\'oro. Roba che se la può permettere solo un miliardario...',

    # --- i due milioni ---
    7569: 'Bastano questi soldi?',
    7572: 'Devo trovarmi un altro lavoro...',
    7575: 'Forse mi tocca davvero vendere gli organi...',
    7578: 'Non è caro',
    7579: 'Ci penso su',
    7580: 'Uaah!? ...S-scusa, mi è scappato un verso strano. È la prima volta che '
          'vedo tanti soldi tutti insieme! Con questi si può... Ah, ma però! Ci '
          'sono anche seimila monete d\'oro al mese di manutenzione e stipendi. '
          'Ti sta bene lo stesso?',
    7583: 'Lo sapevo che era troppo caro.',
    7586: 'I-io con i soldi ragiono in tutt\'altro modo...! ...Ehm. La villa la '
          'vende il mio padrone di prima, quindi vai a trattare con lui. '
          'Adesso vive a Ludus.',
    7592: 'Devo avvisare le colleghe licenziate insieme a me che forse c\'è '
          'qualcuno disposto ad assumerle. Ah, Ludus è un borgo rurale molto '
          'più a est di qui.',
}

LOTTO = 'lavoro/84-chat-lune.jsonl'

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
