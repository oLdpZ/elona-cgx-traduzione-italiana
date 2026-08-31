# -*- coding: utf-8 -*-
"""Le rese del lotto 032 — il MOBILIO, sesta e ultima parte del corpo.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 032 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa032.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.

⚠️ `:125432` porta la stessa frase di `:121446` e `:121508` del lotto 031, e la
resa e' la stessa parola per parola. Le famiglie non finiscono col lotto.
"""

IT = {
    # === LE DIECI PIANTE IN VASO ==========================================
    122023: "Una pianta in vaso che dà fiori discreti. Quel suo modo sommesso passa per prova di umiltà, e capita che la si regali negli anniversari. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122025: "\\\"Questo fiore mi piace da matti. Perché, guarda: i petali non sembrano sangue fresco schizzato dappertutto?\\\" \\n# ~Parole di <Noel> la dinamitarda~",
    122085: "Una pianta in vaso che attira certi animali e non li lascia più. A metterla in un posto qualunque, dicono, senza accorgersene ci si ritrova un capannello di gatti. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122155: "Una pianta in vaso che dà fiori dai colori vivaci. I colori sono i più diversi e, dicono, rallegrano molto chi li guarda. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122157: "\\\"Eh, me lo regali? Evviva, mi piace tantissimo!\\\" \\n# ~Parole di <Gwen> l'innocente~",
    122225: "Una pianta in vaso che per crescere vuole un po' di mano. La chiamano anche la gemma dei fiori, e dicono che dia fiori di un colore bello come le figurine di zucchero. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122295: "Una pianta in vaso che dà fiori di un giallo vivo, da svegliare gli occhi. E ha anche questo di suo: cresce fino a fare fiori così grandi da scambiarli per una spilla. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122365: "Una pianta in vaso che da un solo stelo tira fuori molti fiori. Si dice che abbia un nettare dolce, ma in Tyris del Nord quel nettare spesso diventa un veleno feroce: non provate mai a leccarlo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122427: "Una pianta in vaso cresciuta in bellezza. Pare che in certe regioni questa specie, che viene su svelta, la prendano per segno di prosperità e la regalino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122489: "Una pianta in vaso che dà fiori di colore tenue. Regge bene le malattie e gli insetti, e si può dire che sia piuttosto facile da tenere. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",
    122551: "Una pianta in vaso dalle foglie graziose. In casa di una signorina che vive da sola, dicono, questa pianta di solito c'è. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    122613: "Un cerchio particolare, inciso con caratteri antichi. Oggi è rimasto solo il guscio, e lo si usa unicamente per far bello un ambiente. \\n# ~Compendio Completo degli Oggetti Magici~",
    122741: "Un recipiente che serve a tenere i liquidi. Che cosa ci fosse dentro non lo sa nessuno, e conviene lasciar perdere l'idea di usarlo. \\n# ~Casalinghi che Danno Colore alla Casa~",
    122884: "Uno scaffale da fornaio, studiato perché lo si possa mettere dove si vede bene. I cartellini del prezzo sono attaccati bene in vista, quindi meglio non allungare la mano. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE TRE TAVOLE DELLA STRADA =======================================
    # ⚠️ `:123616` e `:123678` dicono la stessa seconda frase.
    123554: "Una tavola con su scritte le notizie della gente comune. Ci sono attaccati i fatterelli e le chiacchiere che girano in città. \\n# ~I Grandi Comprimari della Città~",
    123616: "Una tavola che indica dove portano le strade. Ne esiste una col nome molto simile, quindi attenzione a non confonderle. \\n# ~I Grandi Comprimari della Città~",
    123678: "Una tavola che si usa come segnale. Ne esiste una col nome molto simile, quindi attenzione a non confonderle. \\n# ~I Grandi Comprimari della Città~",

    123742: "Un arnese da cucina che cuoce i cibi al chiuso, fra vapore e calore. Si cucina mettendo dentro gli ingredienti, e perciò più di tutto conta il colpo d'occhio di chi cucina. \\n# ~I Comprimari della Cucina~",
    123804: "Un forno in cui è colato del metallo fuso. Quel metallo arde di un rosso violentissimo e illumina tutto intorno. \\n# ~Verso una Lama Migliore~",

    # === I TRE RIPIANI CHE SI SPOSTANO ====================================
    # ⚠️ la seconda frase e' identica in tutti e tre.
    123866: "Un ripiano con sopra vestiti d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    123998: "Un ripiano con sopra cianfrusaglie d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124060: "Un ripiano con sopra roba di casa d'ogni sorta. È un mobile che si sposta, e lo si può regolare dove cade più facilmente l'occhio. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    124122: "Uno scaffale con i ripiani ben distanziati, così da farci stare qualunque cosa. Insieme allo scaffale comune, è un mobile che tutti usano volentieri. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124184: "Uno scaffale fatto perché ci stiano anche i libri. È un mobile che lascia molta libertà, e nel modo di riporre si vede il gusto di chi l'ha comprato. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124246: "Un mobile dove mettere via le cose che per adesso non servono. Dentro è già pieno, e perciò non si può usare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124308: "Uno scaffale costruito per riporci le stoviglie. Ha divisori che si spostano a piacere, e così ci stanno stoviglie di ogni tipo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LE DUE SEDIE CHE SI RISPONDONO, e la sedia di tutti ==============
    124371: "Una sedia fatta con un materiale piuttosto a buon mercato. È la sedia comune per eccellenza: quasi tutti i cittadini usano questa. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124434: "Una sedia con la seduta quadrata. Se sia meglio di quella tonda è quasi solo questione di gusti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125936: "Uno sgabello con la seduta tonda. Se sia meglio di quella quadrata è quasi solo questione di gusti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    124497: "Uno scaffale un po' piccolo, costruito per tenerci le pozioni. Quale sia quale lo sa solo chi le ha disposte, e meglio non tirarne fuori una a caso. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    124560: "Un tavolo adatto a chi si applica allo studio. È di materiale duro, ma a guardare bene, in un angolo, c'è inciso lo scarabocchio di qualcuno, fatto, a quanto pare, con un coltellino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === I DUE VASI =======================================================
    124622: "Un vaso con la bocca aperta. È fragilissimo, e perciò non lo si può usare per metterci dentro qualcosa. \\n# ~Casalinghi che Danno Colore alla Casa~",
    124684: "Un vaso sigillato ben stretto. La curiosità di sapere che c'è dentro viene, ma è chiuso così saldamente che non si apre. \\n# ~Casalinghi che Danno Colore alla Casa~",

    124746: "Un banco di metallo che serve a forgiare i metalli. Oltre all'uso suo proprio, pare ce ne sia un altro che sembra inventato: batterlo col martello e farne uno strumento musicale. \\n# ~Verso una Lama Migliore~",
    124808: "Un'armatura lucidata con cura. Ma a guardarla bene sembra roba scadente, appena ricoperta da una patina di metallo. \\n# ~Vita da Mercante Dopo l'Avventura~",
    124870: "Un lume da tenere in mano, che fa una luce tenue. Basta averlo in pugno per sentirsi un grande esploratore. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    124932: "Un attrezzo per scavare. Però, a dirla tutta, si scava anche senza. La gente di Tyris è di tempra dura. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    124995: "Una sedia che, dicono, per un attimo rapisce chiunque. Anche al tatto è morbida e vellutata: la sedia ideale, si può ben dire. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125057: "Un recipiente costruito per conservare i liquidi. Di solito è pieno di vino, ma si racconta di un avventuriero che, volendo berne di nascosto, ha aperto per sbaglio una botte piena di melma: meglio non aprirne a casaccio. \\n# ~I Grandi Comprimari della Città~",

    # === I DUE TAVOLI DA BAR, che aprono uguale ===========================
    125119: "Un tavolo fatto apposta per stare in una taverna. Un mobile sobrio, con addosso un'aria un po' losca. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125181: "Un tavolo fatto apposta per stare in una taverna. Un mobile sobrio, con addosso un'aria da adulti. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    125246: "Uno strumento a tasti di un peso enorme. Dicono che un tempo ci fu un musicista che continuò il suo viaggio portandosi questo pianoforte sulla schiena. \\n# ~Le Melodie della Limpida Irva~",
    125308: "Un ripiano con i soprammobili esposti con ordine. È su due piani, perché si vedano bene. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125370: "Uno scaffale con una montagna di articoli riposti in bell'ordine. Sono raccolti per tipo, così che scegliere sia facile. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    # ⚠️ stessa frase di `:121446` e `:121508` del lotto 031: stessa resa.
    125432: "Armature esposte tutte in fila. C'è scritto a lettere grandi che non si può provare, e perciò non si può indossare. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    125494: "Un tavolo che si usa per mangiare. È largo il giusto, e anche mettendoci su un bel po' di piatti non c'è da temere che si accavallino. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125557: "Un tavolo all'ultima moda, con addosso un'aria elegante. Adesso, pare, va per la maggiore il tipo semplice, tinto tutto di un colore solo. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125619: "Un gioco che serve soprattutto ai bambini per divertirsi. Col passare del tempo si fa sempre più complicato e sempre più caro, ed è in ogni epoca il cruccio dei grandi. \\n# ~Grande Compendio dei Giochi: Per Tutte le Età~",
    125682: "Una bambola cucita riempiendo la stoffa di ovatta. Dentro, dicono, oltre all'ovatta è stipata una quantità di ricordi. \\n# ~Regali che Fa Piacere Ricevere~",

    # ⚠️ la coppia di `:124371`: stessa formula giapponese, stessa resa.
    125748: "Un giaciglio fatto con un materiale piuttosto a buon mercato. È il letto comune per eccellenza: quasi tutti i cittadini dormono in questo. \\n#~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    125810: "Una cassettiera di gran classe, dall'aspetto morbido e pacato. Dicono che ognuno, nessuno escluso, tenga in una di queste il proprio tesoro nascosto. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",
    125873: "Uno scaffale per riporre i libri, di quelli che si trovano spesso dai mobilieri. Non ha difetti né pregi che saltino all'occhio: una fattura senza rischi. \\n# ~Grande Enciclopedia dei Mobili di Tyris del Nord~",

    # === LA LAPIDE, che chiude il mobilio =================================
    127607: "Una tavola dura, incisa in una lingua antica. Non si riesce a decifrarla, ma pare che ogni tanto la compri qualche cittadino che vuole toccare la storia con mano. \\n# ~I Mondi che Non Hai Mai Visto~",
    127609: "\\\"Chissà che effetto fa sapere che le parole che hai pronunciato diventeranno una cosa eterna\\\" \\n# ~Parole di <Erystia> la studiosa di storia~",
}
