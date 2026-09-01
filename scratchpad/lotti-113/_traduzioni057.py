# -*- coding: utf-8 -*-
"""Le rese del lotto 057 — I CONTENITORI: `FILTER_CONTAINER` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 057 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa057.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 057`: **24 righe su 25** hanno lo spazio prima del
`\\n`; l'unica senza e' `:78658`. Tutte e 25 le code hanno lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`: **+25** per 25 rese, nessuna gemella.
`_gia-reso.py 057`: 0 su 25.

ⓘ `_120-serie-bacchette.py 057` dice che qui **serie non ce ne sono**: 25 righe
e 24 aperture distinte. L'unica coppia e' `:103233`/`:103295`, le due sfere,
che condividono la frase e cambiano una parola.
"""

IT = {
    # =====================================================================
    # LE DUE SFERE — una coppia dove cambia una parola sola
    # =====================================================================
    # ⭐ 欲望 (la brama) contro 期待 (l'attesa): la sfera RARA e quella
    #    normale. La frase e' la stessa, e la differenza sta tutta li'.

    103233: "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"brama\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    103295: "Una sfera in cui è stato riposto un oggetto qualunque. Dentro ci sta stipata una speranza che porta il nome di \\\"attesa\\\". \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",

    # =====================================================================
    # LE SCATOLE DEL MESTIERE — tasse, paga, consegne, casseforti
    # =====================================================================

    89821: "Una scatola apposita, per versare le tasse dovute. Una volta al mese conviene fare un salto all'ambasciata di Palmia. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    93483: "Una scatola apposita, per consegnare la merce richiesta. Pare che la fessura abbia qualche accorgimento, perché non ci si butti dentro di tutto. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    94381: "Una scatola per ritirare la paga, due volte al mese. Anche se un imprevisto la fa perdere, la paga viene versata lo stesso; conviene però ricordarsi che i funzionari di Palmia non fanno sconti a nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    93420: "Una cassaforte apposita, che raccoglie tutto l'incasso del negozio. Contro i furti, è congegnata in modo da non aprirsi mai fuori dal negozio. \\n# ~Vita da Mercante Dopo l'Avventura~",

    93422: "Una cassaforte indispensabile per mandare avanti un negozio. Qui dentro finisce tutto l'incasso. \\\"Se un incidente ve la fa perdere, state tranquilli: all'ambasciata di Palmia, cardine dell'economia, si trova tutto\\\" \\n# ~Grande Compendio delle Armi di Tyris: le Reclame~",

    107114: "Una borsa piena dei pezzi pregiati che un mercante ambulante ha raccolto con la propria fatica. Contro i furti, si dice porti addosso una magia che a chi la apre, e non sia l'intestatario, mette dentro un'inquietudine fortissima. \\n# ~Vita da Mercante Dopo l'Avventura~",

    # =====================================================================
    # LE SCATOLE CHE TENGONO IL CIBO
    # =====================================================================

    88147: "Una scatola a ingranaggi, che conserva il cibo senza farlo marcire. È comodissima, ma ci stanno solo quattro qualità di cibo: attenzione, quando si va a far merenda in molti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    92186: "Un frutto dell'ingegno, che conserva gli ingredienti quasi per sempre. C'è però un segreto in questo mobile: per quanti se ne posseggano, oltre lo sportello si arriva sempre e solo allo stesso spazio! \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # =====================================================================
    # I BAULI E LE CASSE
    # =====================================================================

    115196: "Una scatola che custodisce oggetti, e che si dice stia soprattutto nelle Nefia. È fatta pesantissima, perché l'avventuriero che non riesce ad aprirla non se la porti via a forza. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    115258: "Un baule splendente, ornato di gioielli. Contro le apparenze è insolitamente leggero, e con quel rivestimento sfavillante pare che ci siano clienti che lo comprano per tenerci le cianfrusaglie. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # ⚠️ マスター qui e' il MAESTRO della gilda dei ladri, che e' un
    #    personaggio del gioco («il maestro della Gilda dei Maghi», nel
    #    dizionario). L'inglese lo appiattisce in «a gentleman», e cosi' la
    #    battuta perde la persona: chi parla e' il guardiano della gilda, e
    #    la prima volta che si e' stupito e' stato per il proprio capo.
    115260: "\\\"Io sto qui da sempre a stimare la refurtiva, e in tutto questo tempo mi sarò stupito sì e no due volte. La prima per il maestro, che mi portò una statua d'oro di un gigante. La seconda per uno come te, che della refurtiva mi ha portato non il dentro, ma il fuori\\\" \\n# ~Parole di <Abyss> il guardiano della Gilda dei Ladri~",

    81941: "\\\"Un'esperienza sublime per una manciata di fortunati! Chiunque voglia tentare, si presenti col grimaldello\\\" \\n# ~Avvertenza Scritta sul Retro della Scatola~",

    104725: "Una scatola nera da cui, ad aprirla, saltano fuori i materiali. Ne esce di tutto in una volta sola, e si dice che come ci stiano dentro non lo sappia nessuno. \\n# ~Chiudeteci Pure! Box Mania, Numero Uno~",

    # =====================================================================
    # GLI OGGETTI PERDUTI, E LE TRE VOCI CHE LI RACCONTANO
    # =====================================================================

    96844: "Una borsa vecchiotta. Dentro ci stanno le cose lasciate da chi se n'è andato dal continente a metà del cammino. Per averle bisogna passare per la trafila dovuta. \\n# ~Libro in Dono a Chi Sta Morendo~",

    # ⭐ Il giapponese lo chiama ならずもののオネスト, «Onest il farabutto», e il
    #    nome e' la battuta: uno che si chiama Onesto e ruba portafogli.
    #    L'inglese perde il nome e ci mette un punto interrogativo («the
    #    honest? rogue»); la tabella dei titoli lo ha gia' recuperato.
    112196: "\\\"Oh, un portafoglio qui. Meno male, ero in pena perché credevo d'averlo perso. Dici che somiglia a quello che hai perso tu l'altro giorno? Ma certo che sì: è perché di portafogli io ne ho tanti\\\" \\n# ~Parole di <Onest> il farabutto~",

    112258: "\\\"Questa borsa è mia. Anzi no, ce l'avevo tempo fa. Anzi, mi ricordo d'averla avuta; anzi, la volevo comprare... anzi, aspetta. Ah, ecco, mi è tornato: era la borsa che aveva posato lì un vecchio signore. E dunque è mia\\\" \\n# ~Parole di <Gleed> il topo d'appartamento~",

    115134: "\\\"Dentro c'è la speranza, oppure la disperazione? L'unica cosa che si può sapere è che per chi la tiene chiusa lì non sarà altro che disperazione\\\" \\n# ~Parole di <Marks>, ladro senza pari~",

    # =====================================================================
    # LE QUATTRO CHE NON STANNO IN NESSUN GRUPPO
    # =====================================================================

    57125: "Una busta fatta di carta marrone e spessa. Chi la manda non c'è scritto, ma insieme c'è una lettera. \\n# ~Regali che Fa Piacere Ricevere~",

    # ⚠️ はく製 nel dizionario e' la «statuetta» (l'oggetto che il giocatore
    #    raccoglie ed espone), non l'animale impagliato — e l'inglese qui
    #    sbaglia in un terzo modo ancora, scrivendo «fossils». ユニーク sono
    #    le creature UNICHE del gioco: la lettera ringrazia per una
    #    collezione di statuette di personaggi unici, aperta al pubblico.
    57127: "\\\"La ringrazio d'aver aperto al pubblico, con tanta generosità, le sue statuette uniche. Sono tutte cose che una vita per bene non permetterebbe di vedere, e mi emozionano un giorno sì e l'altro pure. Continui così a raccogliere statuette uniche!\\\" \\n# ~Lettera di un Fissato di Tassidermia~",

    # ⚠️ SENZA lo spazio prima del `\n`.
    # ⚠️ L'inglese AGGIUNGE quello che il giapponese non dice: «Pack of 5
    #    collectible cards». Il conto delle cinque sta nell'indice 3, gia'
    #    reso; qui il giapponese dice una cosa sola, e la resa dice quella.
    78658: "Le carte che ci sono dentro non mostrano l'immagine finché non le metti nel mazzo.\\n# ~Duellanti Ardenti~",

    80736: "In certe zone c'è l'usanza di farne dono ai conoscenti all'inizio dell'anno. A chi si è amici ci si mette dentro roba buona in proporzione; a chi lo si è meno, invece, capita che ci si nasconda uno scherzo. Si dice che ci sia chi, solo per questo, si mette a fare il gentile con tutti. \\n# ~Regali che Fa Piacere Ricevere~",

    81260: "Una scatola dentro cui è stato messo un gatto. Se il gatto lì dentro sia vivo o morto, non lo si saprà finché non si prova ad aprirla. \\n# ~Dizionario Fantastico di Irva~",

    90832: "Un ceppo di metallo, enorme e saldo. A spingerlo o a tirarlo pare non muoversi di un dito, eppure a guardarlo bene la giuntura sembra un po' allentata. \\n# ~I 50 Prodotti Preferiti dai Detenuti~",
}
