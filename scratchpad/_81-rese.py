# -*- coding: utf-8 -*-
import io, json

RESE = {
 # --- Telhureza, il geco di guardia (donna, SEX=1) ---
 15493: "Per ora è tutto a posto",
 15494: "Ti piace così tanto questa casa?",
 15495: "Ci sono insetti cattivi!",
 15496: "E-ehi, senti...! Se ci sono insetti cattivi che rovinano questa casa, non farti problemi a dirmelo, eh? Tanto li ammazzo.",
 15499: "Ah... davvero...? Ti metti a difendere degli insetti? Come sei gentile. Ma se li lasci vivere questa casa va in rovina... e secondo te io posso perdonarglielo...?",
 15503: "Sì, non so perché ma mi viene voglia di proteggerla... All'inizio mi bastava guardarla. Ma a forza di guardarla giorno dopo giorno mi si è scaldato il corpo... Uhihihi! Sarà il sangue del geco di guardia che mi scorre nelle vene!?",
 15508: "Ma guarda... e chi sarebbe?",
 15514: "Chi vuoi che attacchi?",
 15523: '" " + cnvtalk("Ma dai... come faccio a essere io l\'insetto cattivo, se sono io che proteggo questa casa?")',
 15531: '" " + cnvtalk("A morteeeee!!")',
 # --- Imarituka, lo sberleffo di casa (donna) ---
 15543: "Farò del mio meglio...",
 15544: "Adesso ti faccio vedere io!",
 15545: "Non è poi così terribile!",
 15546: "lol lol lol. ma il gusto dov'è finito? G-U-S-T-O! dai, usalo quel cervello: la prossima volta ti verrà in mente qualcosa di meno orrendo~ forse. ahahahah",
 15549: '"ma sì, rilassati lol. la polvere negli angolini te la spolvero anch\'io, ma per i lavori pesanti muovi le chiappe e falli da te, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ". ahahah"',
 15553: "ahah, mitico. non è che poi ti tocca rimangiarti tutto? dimostramelo, dai. anche se ne dubito forte. lol",
 15557: '"ah, quindi te ne rendi conto anche tu, ahahah. sei tipo da prendere per oro colato le classifiche, eh? scusa scusa lol. figurati se una persona di gusto raffinato come te si lascia rovinare l\'autostima da una valutazione da quattro soldi. lol"',
 # --- Oxode, l'ape stregina (donna) ---
 15566: "È bello avervi qui",
 15567: "Guehehe...",
 15568: "Quand'è che paghi l'affitto?",
 15569: "Ah, sei di ritorno. Grazie del lavoro là fuori.",
 15572: "Sì, sì. Le mie figlie si sono affezionate a questa casa e a chi la tiene. Ne parliamo spesso, e sempre volentieri. Ufufu.",
 15576: "S-sembri proprio a pezzi... tutto bene? Perché non ti riposi ancora un po'?",
 15582: '"La prossima riscossione è " + cnvdate(cdata(CDATA_RENT_REFRESH, tc), 1) + "."',
 15585: "Oh, giusto. Scusa il ritardo. Prendi pure questi: li ho fatti insieme alle mie figlie.",
 # --- Scard, la rondine felice (uomo, SEX=0) ---
 15599: "Sono felice",
 15600: "Sono infelice",
 15601: "Pensa piuttosto a pagare l'affitto",
 15602: "Sei felice?",
 15605: "La felicità è un dovere, no?! Per quanto faccia male il corpo, per quanto soffra l'animo, finché c'è vita c'è felicità: non ho il minimo dubbio!!!",
 15609: "Chi è vivo deve essere felice anche per chi è morto. Ahahahahahah! Guarda! Guaaardaaa!! Io sono così feliceeeeee!!!!",
 15618: "Ah, sì. Certo.",
 # --- Talka, dai codini lunghi (donna) ---
 15687: "Vorrei sapere della devozione",
 15688: "Vorrei sapere delle offerte",
 15689: "Vorrei sapere delle incarnazioni",
 15690: "Vorrei sapere del libro nero nell'angolo",
 15691: "Che c'è da guardare così... ho qualcosa in faccia?",
 15694: "Il massimo della devozione che puoi avere con ciascun dio dipende dalla tua abilità Fede. Far crescere l'abilità non basta ad approfondire la fede, quindi ricordati di portare offerte all'altare.",
 15695: "La devozione cala poco alla volta mentre ti sposti, quindi conviene portare offerte con regolarità. E, ovviamente, la devozione si azzera se cambi dio.",
 15699: "Ogni divinità ha le sue preferenze in fatto di offerte. Prima di abbracciare una fede, accertati di poter fornire offerte in quantità.",
 15700: "I cadaveri pesanti piacciono un po' a tutti, quindi se il tuo scopo è offrirli meglio non cucinarli. Attenzione però: un cadavere che marcisce non vale più niente.",
 15704: "Man mano che la fede si approfondisce, ogni dio ti concede la propria incarnazione. Pare che siano modellate sui parenti del dio e cose così.",
 15705: "Approfondendo ancora la fede, dicono che si riceva anche più di un'incarnazione... C'è pure chi cambia dio e poi torna indietro apposta per farsene dare un'altra, ma non credo valga la pena arrivare a tanto.",
 15709: "Quel libro... ho chiesto a tutti, ma pare che nessuno ne sappia niente. Un giorno, all'improvviso, era lì.",
 15710: "Sembra un oggetto magico dalla natura oscura, ma un avventuriero di prim'ordine saprebbe di sicuro come usare perfino una cosa del genere...",
 # --- Kyu-bi, <Nove Code Dorate> (donna) ---
 15719: "Meglio una città governata dalle volpi che una città ridotta a pascolo dei lupi mannari, non credi?",
 15724: "Offrire il tofu fritto",
 15727: "Te lo porto la prossima volta",
 15728: "Questa città è sotto il mio dominio. Su, su, adorami come si conviene. E portami il tofu fritto in offerta.",
 15733: "Evviva! ...Ehm. Offrimene quanto ti pare. Ti darò una ricompensa, fanne buon uso. E torna da me quando avrai altro tofu in tasca.",
 15742: "Ah, che peccato. Un po' di tofu fritto in tasca si tiene sempre, lo sai, no?",
 # --- Boyciana, <Signora Cicogna> (dà del lei) ---
 15753: "Ma no... non sto mica aspettando il momento buono per portare via il bambino, eh...",
 15756: "Ah... vorrei tanto portare un bambino a una coppia che non può averne, e farmi coccolare...",
 15759: "Crescere un figlio è così faticoso da far venire l'esaurimento. Vuole che me ne occupi io?",
}

src = 'lavoro/81-chat-inquilini.jsonl'
voci = [json.loads(l) for l in io.open(src, encoding='utf-8') if l.strip()]
mancanti = [v['riga'] for v in voci if v['riga'] not in RESE]
extra = [r for r in RESE if r not in {v['riga'] for v in voci}]
if mancanti or extra:
    print('MANCANTI %s' % mancanti)
    print('EXTRA    %s' % extra)
with io.open(src, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[v['riga']]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte' % len(voci))
