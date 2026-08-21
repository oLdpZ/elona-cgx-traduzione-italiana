# -*- coding: utf-8 -*-
import io, json

RESE = {
 # --- Aime la narratrice (bambina, parla di sé in terza persona) ---
 15768: '"Ahah! " + _onii(cdata(CDATA_SEX, CHARA_PLAYER)) + ", se riesci a finire la tua storia, Aime ti fa sentire la sua."',
 15771: "Quando mi va",
 15772: "Raccontamela",
 15773: "Aime conosce un sacco di storie. Se dai ad Aime cinque pezzi di polvere di stelle, te ne racconta una!",
 # i tredici titoli: menu a due colonne, tetto 24
 15780: "《Il diario di Aime》 (Lv???)",
 15781: "Il sorriso sotto la maschera (Lv200)",
 15782: "Il bambino che scordò il sogno (Lv250)",
 15783: "Le mani di fango (Lv300)",
 15784: "Pianto d'argento (Lv400)",
 15785: "Nel labirinto del dio gigante (Lv500)",
 15786: "Fine del caos (Lv600)",
 15787: "I sette misteri del liceo di Irva (Lv700)",
 15788: "La grande rissa del tonfa furioso (Lv800)",
 15789: "Tabù: il dominio dei demoni celesti (Lv900)",
 15790: "Yerleswood contro Zeirennou (Lv1000)",
 15791: "Il mito della distruzione (Lv1100)",
 15792: "L'eroe eterno (Lv1200)",
 15793: "Però non ne è ancora stata fatta nessuna, eh.",
 15798: "Mi prendi in giro? Porta ad Aime cinque pezzi di polvere di stelle.",
 # --- Jaldabaoth: la sconfitta (flag 990) ---
 15807: "Impossibile... in potenza ero nettamente superiore... doveva essere così...",
 15808: "Ma... un miracolo si paga caro... fra pochi secondi la reazione lasciata dalla mia distruzione ti annienterà il corpo, e il tuo io andrà in frantumi...!",
 15809: "Ghh... e quella tua faccia odiosa... non la sopporto più. Io torno per primo nel vuoto...",
 15810: "Davvero... non pensavo che sarebbe finita così...",
 # --- Jaldabaoth: la lancia divina (flag 890) ---
 15826: "Riesci ancora a muoverti... non ti basta? Hai resistito ben oltre il necessario. Almeno la caparbietà te la riconosco.",
 15827: "E con questo?!",
 15828: "Non posso proprio arrendermi",
 15829: "Ti ammazzo lo stesso",
 15830: "Spegniti in silenzio e basta. Per quanto tu soffra, per quanto ti sforzi, non hai nessuna speranza di vincere.",
 15833: "Hai ancora la sfacciataggine di rispondermi. E va bene. In segno di rispetto, mi prenderò il mio tempo per ridurti in cenere e disperderla nel nulla.",
 15835: "Le fiamme convergono in un punto solo...!",
 # --- Jaldabaoth: la luce dei desideri ---
 15908: '"Rialzati! I " + gdata(GDATA_FLAG_COLLECTED_WISHES) + " desideri di tutti: falli diventare forza!"',
 15909: "Che sta succedendo...!?",
 15910: "L'ho trafitto con un fuoco che cancellerebbe senza sforzo persino un dio supremo. Perché un mortale qualunque è protetto da un miracolo di questa portata?",
 15911: "Vado solo all'avventura",
 15912: "Questo è un desiderio! È la luce che nasce dai legami!",
 15913: "Ti faccio assaggiare che paura fa un avventuriero...",
 15914: "Non so che cosa sia, ma ti butto giù lo stesso!",
 15915: "Non capisco... che cos'è quella luce? Tu chi sei davvero...",
 15918: "Kh... ahahahahahah!",
 15919: "Mi hai davvero mandato all'aria i piani! Sì, proprio così! Eppure non sei che un moribondo che ha afferrato un miracolo passeggero! E io lo faccio a pezzi di petto, con una forza schiacciante!",
 15920: "Fatti sotto... IRREGOLAREEEEE!!!",
 16006: "La zanna della luce nascente lasciata da Tezcatlipoca evapora e si scioglie nella rete akashica...",
 16037: "Si sente una voce...",
}

src = 'lavoro/81-chat-aime-jaldabaoth.jsonl'
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
