# -*- coding: utf-8 -*-
"""IRVA PERDUTA e i suoi ospiti (84a): chat.hsp :7645-:7794, sei parlanti.

    :7645-:7657  la pianta Meshera        il nido dell'originale
    :7658-:7688  Milos del Mondo Dimenticato
    :7689-:7739  Carla del Mondo Dimenticato
    :7740-:7758  Stoke il riccone         i biglietti per il concerto
    :7759-:7778  Arma la guida turistica
    :7779-:7794  Aile l'assistente di volo

36 firme, zona chiusa. Il lessico dal dato:

    db_creature:91226  «<Milos> del Mondo Dimenticato»
    db_creature:91132  «<Carla> del Mondo Dimenticato»
    db_creature:91112  «re Zabi» (e' una battuta di Carla stessa)
    db_creature:71217  «<Fron> l'organizzatrice di viaggi»
    db_card:8928/9227  «<Arma> la guida turistica», «<Aile> l'assistente di volo»
    chat.hsp:15454     «la collana di Elsia»
    chat.hsp:24422     «il vento d'etere»
    chat.hsp:1751      «rovine chiamate <<Nefia>>»
    db_item:142700     «biglietto per il concerto»
    main.hsp:4209      «il dio del caos»
    db_race            «stirpe» per i popoli

⭐⭐⭐ IL CONTROLLO CHE VALEVA PIU' DEL LOTTO: `:7662` e `:7693` NON SONO TESTO,
SONO CHIAVI. Il codice fa
`strmid(cdatan(CDATAN_NAME, tc), 0, strlen(evold)) == evold` e, se combacia,
riscrive il nome della creatura. Quindi `evold` deve essere ESATTAMENTE il nome
che `db_creature.hsp` da' alla creatura. In italiano combacia — tutt'e due
dicono «<Milos> del Mondo Dimenticato» — perche' una sessione vecchia le aveva
gia' rese tutt'e due allo stesso modo.

⚠️⚠️ In INGLESE non combaciano affatto: `db_creature.hsp:91226` dice «<Milos>
Of The Forgotten World», `chat.hsp:7662` dice «<Miros> hail flom Erusia» —
altro nome, e per giunta con due refusi. Nella build inglese quel rinomino e'
CODICE MORTO: il giocatore inglese non vede mai i due diventare «del Mondo
Indimenticabile». In italiano funziona, come in giapponese. E' la faccia buona
della classe di difetto della 81a: la `lang()` che e' una chiave.

⚠️ Le tre deroghe:
1. `:7648` — l'inglese «(Ethers were discharged to crystallize some.)» non
   c'entra niente col giapponese 「(不気味に胎動している…。)」, che descrive il
   nido che si muove. E' una riga di un altro posto finita li'.
2. `:7706` — il giapponese non ha soggetto nella prima frase; l'inglese ce ne
   mette uno («my appearance... about me») e sceglie Carla, ma la storia del
   principe trasformato in bestia parla del GIOCATORE, che e' il viandante che
   la salvo' e che da allora e' cambiato. Si lascia il soggetto sospeso come in
   giapponese.
3. `:7776`-`:7788` — nessuna, ma vedi sotto il genere.

⚠️ Il genere del giocatore a `:7734`: «I thought you were someone else» non puo'
diventare «ti ho scambiato per un altro». Diventa «mi sono sbagliata» — dove il
participio si accorda con CARLA, che e' donna e la cui riga in
`db_creature.hsp:91100` («Chissa' se Milos sta bene...») lo conferma.

💡 Coniata una cosa sola: 生魂の儀 / «Healing Ceremony» -> «Cerimonia di
Guarigione». Non c'era da nessuna parte.
"""
import io, json, sys

RESE = {
    # ---------------- la pianta Meshera ----------------
    7648: '(Qualcosa si agita là dentro, e mette i brividi...)',
    7651: '(Al centro della sala scopri un enorme ammasso di carne, posato come '
          'su un altare.)',
    7652: '(È il Meshera originale, nato qui in un\'epoca remota. Assimila senza '
          'distinzione ogni forma di vita, ed è il vivaio della calamità che ha '
          'minacciato il mondo: ancora oggi continua a evolversi.)',

    # ---------------- MILOS ----------------
    7666: 'Non mi pento di aver scelto, quel giorno, la Cerimonia di '
          'Guarigione. E non importa se era già scritto nel disegno del destino.',
    7667: 'La collana di Elsia è un artefatto con una lunga storia. Si dice che '
          'sia una preghiera per la sicurezza del viaggio, e che leghi chi la '
          'porta al ricordo delle persone incontrate lungo la strada. '
          '...All\'epoca la ritenevo solo una consolazione, ma a quanto pare mi '
          'sbagliavo.',
    7672: 'Che leggenda?',
    7673: 'Quando la luce ci ha avvolti e ci ha scagliati in questo mondo, '
          'qualcuno è comparso davanti a noi. Non ne ho distinto né la voce né '
          'la figura, ma parlava di destino. Forse era la leggendaria Norne.',
    7676: 'Ah, chiedo scusa: da questa parte del mondo la leggenda di Gaius Vis '
          'non la conoscete. \\"Norne\\" è il nome collettivo della dea del '
          'destino e della sua discendenza: gli Ahlung, stirpe dei giganti; gli '
          'Eln, stirpe delle fate; i Dovarn, stirpe dei nani. La Guerra delle '
          'Divinità Antiche ne ha sterminati quasi tutti, ma si dice che i '
          'sopravvissuti leggano il destino e guidino gli uomini.',
    7682: 'Palmia, Eulderna, il vento d\'etere...',
    7683: 'Questo mondo... Irva, si chiama. A quanto pare non è del tutto '
          'estraneo al mio, a Gaius Vis. Se non avessi una missione, mi ci '
          'metterei a indagare con calma.',
    7684: 'Eppure qualcosa non torna, qui. I morti e i moribondi si rimettono '
          'da soli, senza Cerimonia di Guarigione. Possibile che nessuno se lo '
          'chieda?',

    # ---------------- CARLA ----------------
    7698: 'Io...? Sì, stavo solo pensando a una cosa.',
    7700: 'Me l\'hai raccontata tu',
    7701: 'È una fiaba che mi ha raccontato Larnneire',
    7702: 'Non l\'ho capita bene',
    7703: 'Te la ricordi la storia del principe trasformato in bestia?',
    7706: 'Anche se l\'aspetto... no, anche se tutto è cambiato. Che tu fossi '
          'tu, questo non cambia. Adesso lo penso davvero.',
    7710: 'Anche da questa parte la raccontano, allora. O forse è proprio per '
          'via di lei.',
    7714: '...Perdonami. Il senso di quella storia, tu, non l\'hai ancora '
          'afferrato.',
    7721: 'Quella collana... me la fai vedere un momento?',
    7722: 'Questi graffi, questi intagli... Non ci sono dubbi: è proprio '
          'l\'oggetto che diedi al viandante che quel giorno mi salvò... no, ai '
          '\\"viandanti\\".',
    7723: 'Ecco. Eri tu, vero?',
    7729: 'Ritrovare Milos è stato bello, ma da quando sono arrivata qui sono '
          'passati parecchi anni. Se il tempo scorre allo stesso modo... chissà '
          'a che punto è adesso la sciagura della foresta. A pensarci mi si '
          'gela il sangue.',
    7733: 'M-ma tu...?!',
    7734: '...Perdonami, mi sono sbagliata. Assomigli a chi, tanto tempo fa, mi '
          'diede una mano.',
    7735: 'Da quando sono approdata qui ho parlato con molta gente, e a quanto '
          'pare questo non è il mio mondo. Dovrei tornare in fretta a Gaius '
          'Vis, ho udienza da re Zabi... ma come ci si torna? E poi ho perso '
          'anche Milos...',

    # ---------------- STOKE, il riccone ----------------
    7742: 'Scambiare i biglietti',   # 20: come «Scambiare le medagliette» di Miral
    7744: 'Ahimè... una volta questa era una città bella e tranquilla. Da quando '
          'arrivano i turisti, un baccano insopportabile. Mio nipote, però, è '
          'contento che ci sia vita.',
    7747: 'Hai dei biglietti per il concerto? Restarne senza quando voglio dare '
          'una festa è sempre una seccatura. Ti andrebbe di scambiarli con '
          'qualcosa della mia collezione speciale?',

    # ---------------- ARMA, la guida turistica ----------------
    7763: 'A pensarci adesso, avrei dovuto farmi accompagnare anche dalle '
          'cugine, Fron e Leah. Fra un sopralluogo e l\'altro magari '
          'abbattevamo pure il dio del caos: due piccioni con una fava.',
    7767: 'Sono venuta con mia sorella minore Aile per un sopralluogo del '
          'percorso, ma combattere proteggendo dei clienti così fragili è '
          'un\'impresa disperata...',
    7768: 'Anzi: mia sorella tirava dritto e mi ha seminata. Che ragionamenti '
          'fa, a piantare qui la sua povera sorella maggiore?!',
    7774: 'Una guida turistica deve saper accompagnare i clienti dovunque. Solo '
          'chi si è temprato al punto da guidarli in qualunque ambiente, e da '
          'trasformare lo scontro con banditi e mostri in uno spettacolo per i '
          'clienti, può fare la guida turistica qui a Irva.',

    # ---------------- AILE, l'assistente di volo ----------------
    7783: 'Le Nefia non sono roba da assistente di volo...',
    7787: 'Uhm. Mi guardo intorno e mia sorella non c\'è più...',
    7788: 'Mia sorella maggiore è sempre stata la più imbranata di noi. Si sarà '
          'persa a girellare da qualche parte. Che pazienza...',
}

LOTTO = 'lavoro/84-chat-irva-perduta.jsonl'

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
