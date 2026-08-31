# -*- coding: utf-8 -*-
"""Le rese del lotto 040 — gli SCARTI, la coda: la categoria si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 040 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa040.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nell'inglese,
e gli **accenti si scrivono veri**.
"""

IT = {
    # === IL CUORE DI MOSTRO ===============================================
    86735: "Un cuore misterioso che ancora adesso continua a battere. Dicono che, solo a portarlo addosso, si fa proprio anche il cuore dei nemici. \\n# ~Dizionario Fantastico di Irva~",

    # === I DUE SPAVENTAPASSERI ============================================
    91460: "Uno spaventapasseri elegante, con in testa un cappello bianco. Dicono che sia uno di quelli stanchi di fare la guardia ai campi, che si è deciso a esordire in città. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",
    112817: "Il guardiano dei campi che, spalancate le braccia, mette paura alle bestie nocive. Che abbia i piedi piantati nel terreno sarà il segno della volontà di non lasciare mai il posto e di eseguire l'ordine. \\n# ~Storie Inventate Scambiate per Bugie, Volume 2~",

    # === LO STERCO E IL CEPPO =============================================
    92451: "Un oggetto bruno partorito da un essere vivente. Ha anche un odore, ed è cosa da schifare; eppure pare che qualcuno, forse preso dalla follia, ne raccolga di una certa specie come se ne fosse posseduto. \\n#~Le Mille Cianfrusaglie che Amo~",
    109208: "Un ceppo d'albero senza niente di speciale. C'è chi te lo vende con l'astuzia dicendo che nel suo essere rozzo c'è l'asprezza della natura ed è perfetto da usare per sedia in casa; ma sederti ci puoi sedere, e per il resto è ciarpame: non cascarci. \\n#~Le Mille Cianfrusaglie che Amo~",

    # === IL MAZZO DI FIORI ================================================
    111063: "Un articolo fatto di fiori recisi messi insieme. Spesso si usa come dono che viene dal cuore. \\n# ~Regali che Fa Piacere Ricevere~",
    111065: "\\\"Quando sei bello come me sono le donne a venirti incontro; ma quando voglio essere io ad avvicinarmi, di solito uso questo. Le donne cedono alle cose, sai: me lo diceva anche la donna che amo di più.\\\" \\n# ~Parole di <Raphael> il donnaiolo~",

    # === LA SCOPA E LA LEGNA ==============================================
    112755: "L'attrezzo che si usa per pulire. Dai tempi antichi la si è schifata perché è il simbolo dei maghi, ma oggi è ridotta a un gioco per le spade finte dei bambini. \\n# ~Casalinghi che Danno Colore alla Casa~",
    112879: "Legno tagliato a una certa altezza e fatto seccare per farne combustibile. Siccome brucia molto bene ha un suo valore nella vita di ogni giorno; ma essendo roba d'uso comune, caro non si può dire che sia. \\n#~I Comprimari della Cucina~",

    # === LE TRE OSSA ======================================================
    # ⚠️ famiglia: il giapponese ripete la stessa seconda frase in tutt'e tre
    #    e cambia solo di chi sono le ossa (animale, umane, di qualcosa).
    116408: "Ossa d'animale sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",
    127669: "Ossa umane sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",
    127731: "Ossa di qualcosa, sbiancate dal tempo. Di occasioni per usarle ce n'è parecchie, dalla stregoneria al distillare pozioni, ma ce n'è talmente tante che come valore non contano niente. \\n#~Le Mille Cianfrusaglie che Amo~",
    127733: "\\\"Uuuh, bau bau! Bau! ...mugolio.\\\" \\n#~Parole di <Poppy> il cagnolino~",

    # === LA PAGLIA E IL PESCE SECCO =======================================
    116470: "Erba fatta seccare e legata in fascio. Ha una certa elasticità e sembrerebbe buona per dormirci, ma poi la giornata se ne va a togliersi la paglia di dosso: meglio non riposarci sopra. \\n#~Le Mille Cianfrusaglie che Amo~",
    116540: "La carcassa secca di un pesce. Anche a metterla in acqua non si mangia di certo, e non vale niente; ma dandola a un bambino, dicono, se la tiene in mano e ci gioca muovendola come fosse una bestia leggendaria. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # === I RECIPIENTI VUOTI E PIENI =======================================
    116665: "Un recipiente fatto più largo e più basso di una scodella. Dentro c'è qualcosa, ma non è cibo, quindi anche se hai fame non lo puoi mangiare. \\n# ~Casalinghi che Danno Colore alla Casa~",
    116727: "Un recipiente vuoto, senza niente dentro. C'è chi lo usa per la tavola e chi ci mette una pianta per ornamento: ognuno a modo suo. \\n# ~I Comprimari della Cucina~",
    116789: "Un cesto intrecciato con tralci di piante. Qualcosa la tiene, ma ha le maglie larghe, quindi per cose come attingere acqua non si può usare. \\n# ~I Comprimari della Cucina~",
    123419: "Un cesto senza niente dentro. Si usa soprattutto da contenitore quando si mangia all'aperto, e quasi tutti sono usa e getta. \\n# ~I Comprimari della Cucina~",
    116851: "Bottiglie vuote di ogni misura. Per tenere l'acqua sono un po' troppo piccole, ma per attirare l'occhio di un bambino bastano e avanzano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # === IL PEZZO DI MINERALE =============================================
    116913: "Un pezzo di roccia con dentro un poco di minerale. Ce n'è così poco che di valore in denaro non ne ha, ma pare che a scaldarlo fino al rosso qualche uso lo trovi, in cucina o al bagno. \\n#~Le Mille Cianfrusaglie che Amo~",
    # ⚠️ :116915 non ha giapponese: l'inglese e' la sola fonte.
    116915: "\\\"Questo pezzo di minerale è proprio un pezzo di spazzatura.\\\" \\n#~un tizio con la barba~",

    # === LA SPADA ROTTA E LA BANDIERA =====================================
    127793: "Una spada spezzata in due a metà. Sbattuta da vento e pioggia, con la lama tutta sbeccata, non vale più un briciolo; eppure, a darla a un bambino, si mette a fare il guerriero con tutto se stesso, ed è divertente. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",
    127855: "Un telo che prende il vento e sventola. I colori e i disegni sono tanti e ogni città ha i suoi, così è uno degli articoli che piacciono ai turisti come ricordo del viaggio. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # === IL BRACIERE E IL BUCATO ==========================================
    127917: "Una lampada semplice: in cima a un palo, una gabbia di ferro dove si tiene la fiamma. La fattura rozza dà un'aria un po' selvatica. Da qualche anno, pare, certe trattorie la mettono nel locale proprio per quell'effetto. \\n# ~Da Oggi Avventuriero Anche Tu: Manuale di Viaggio~",
    127979: "Una tinozza con dentro ficcati dei vestiti sporchi. C'è da stupirsi che qualcuno voglia una cosa simile, eppure pare che per certi patiti delle pulizie sia irresistibile. \\n#~Le Mille Cianfrusaglie che Amo~",

    # === IL VASO ROTTO, LA SPAZZATURA, LA SCHEGGIA ========================
    128041: "Un vaso rotto che non si può più usare. Non vale proprio niente, ma pare che qualche artista ci veda una possibilità e lo compri quasi per sfida. \\n#~Le Mille Cianfrusaglie che Amo~",
    128103: "Erba secca appallottolata tutta insieme. È durissima e come foraggio non va, ma dandola a un bambino, dicono, si mette a prenderla a calci senza fermarsi mai. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",
    128235: "Schegge di legno spaccato. Non servono proprio a niente, ma per incuriosire un bambino bastano. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",
}
