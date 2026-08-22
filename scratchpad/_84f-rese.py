# -*- coding: utf-8 -*-
"""I CANI E I GATTI, piu' Naive Kyle (84a). chat.hsp, cinque parlanti:

    :3464-:3491  Poppy il cagnolino      il cane smarrito
    :3492-:3536  Rilian che lo cerca     la bambina di Vernis
    :3537-:3580  Tam che odia i gatti    la casa infestata a Yowyn
    :3710-:3793  Mia la finta ingenua    il gatto d'argento
    :7191-:7269  Naive Kyle              le corna di unicorno

⭐⭐ KYLE NON ERA DEL LOTTO: e' entrato perche' condivide una FIRMA. La voce di
menu 「まかせて」/«Leave it to me.» sta in due menu lontani, `:3499` (Rilian) e
`:7217` (Kyle). Renderla per Rilian avrebbe messo una voce italiana sotto una
domanda inglese — il difetto della 79a — e `bilingui` non l'avrebbe visto,
perche' quel menu ha due voci sole e l'altra e' `strbye`, gia' resa: sarebbe
stato un menu TUTTO italiano dentro una schermata inglese. La risposta non e'
accorciare il lotto, e' allargarlo.

Il lessico e' venuto tutto dai DIARI dei quattro incarichi:

    text.hsp:10061  «[Lv. 4] Il cagnolino smarrito»
    text.hsp:10071  «Rilian, a Vernis», «Poppy, il suo cagnolino smarrito»,
                    «il cucciolo», «la grotta subito a est di Vernis»
    text.hsp:10221  «[Lv. 25] Sterminio di gatti»
    text.hsp:10231  «Tam, a Yowyn», «ripulire casa sua dai gatti», «dalle parti
                    dei campi a sud»
    text.hsp:10341  «[Lv. 1] Il sogno di Mia»
    text.hsp:10351  «un gatto d'argento, che e' raro»
    text.hsp:10877  «[Lv. 30] Lotta contro la follia»
    text.hsp:10887  «<Kyle>, a Melkawn», «CORNA di unicorno» (il plurale sta
                    anche nel campo `plurale` di db_item:143990)
    db_creature     «<Cacy> il domatore di gatti», «il gatto d'argento»
    db_item         «cuore di mostro», «corno di unicorno», «frigo portatile»
    text.hsp:88     «Insane» -> «Follia»; da li' «attacchi di follia»
    text.hsp:891    «healer» -> «la guaritrice»

⭐⭐⭐ MIA SI TRADUCE DAL GIAPPONESE, e non l'ho deciso io: e' una deroga di
FAMIGLIA gia' presa. L'inglese di monte le ha rifatto la voce da capo — le
mette in bocca un finto inglese pieno di «nyah» e una parodia di «Nobody knows
the trouble I've seen» — ma `db_creature.hsp:121290` ha gia' le sue battute
rese dal giapponese («Lallalla♪», «Fungo funghetto funghettino tutto allegro♪»,
«Uhm uhm uhm uhm, la pupu' del gatto♪»), e `db_card.hsp:14286` rende 猫かぶり
«la finta ingenua» — cioe' l'IDIOMA giapponese («far la gatta morta»), non il
gatto letterale che l'inglese ha visto. Il personaggio italiano esiste gia': si
continua quello. Vale la regola della 82a, il pantheon: la deroga si eredita.

⚠️ E li' dentro c'era anche la prova che ♪ si puo' scrivere: sta gia' nella
build, in quelle battute.

⚠️⚠️ La deroga che serve al GIOCATORE e' `:3770`: l'inglese butta via la
spiegazione del CUORE DI MOSTRO. Il giapponese dice che cosa fa — 「所持して
いるだけで、支配の確率を高めてくれるアーティファクト」 — l'inglese la sostituisce
con altri «nyah». E' una regola di gioco, non colore.

⚠️ `:3479` porta `is(tc)`, morfologia inglese: si toglie (74a). `:7211`,
`:7219` e `:7256` portano `_onii(cdata(CDATA_SEX, CHARA_PLAYER))`, che invece
NON e' morfologia: `text.hsp:111` lo rende «Fratellone» / «Sorellona» secondo
il sesso del giocatore, ed e' contenuto. Resta.

⚠️ Il genere del giocatore, due volte: `:7211` «watch out» non puo' diventare
«sta' attento» (-> «Occhio anche tu»), e «adventurer» rivolto al giocatore e'
«tu che vai all'avventura» (chat.hsp:1469), mai «avventuriero».
"""
import io, json, sys

RESE = {
    # ---------------- POPPY, il cagnolino ----------------
    3467: 'Bau bau!',
    3470: 'Portarlo via con me',
    3472: 'Bau...?',
    3476: 'Il gruppo è al completo: non puoi portare con te nessun altro...',
    3479: 'name(tc) + " è sotto la tua protezione. Bisogna riportarlo a casa '
          'sano e salvo."',

    # ---------------- RILIAN, la bambina di Vernis ----------------
    3495: "Ah, ecco chi va all'avventura! Ciao... bau!",
    3499: 'Ci penso io',
    3501: 'Ohh no, Poppy è sparito un\'altra volta... Si sarà perso di nuovo in '
          'quella grotta. E adesso? Il papà è troppo occupato per darmi retta... '
          'Ah, tu che vai all\'avventura, me lo cerchi tu Poppy? Poppy? È il mio '
          'cagnolino, il mio migliore amico.',
    3504: 'Poppy mio...',
    3508: 'Che bello! Poppy si sarà perso nella grotta dove gioca sempre. È '
          'subito fuori città, a est. Mi raccomando!',
    3514: 'E Poppy? Ancora niente?',
    3517: 'Poppy! Stai bene! Grazie, tu che vai all\'avventura. Tieni, è per te...',

    # ---------------- TAM, che odia i gatti ----------------
    3540: 'Ecco... a dire il vero... ho scoperto che questa locanda è più comoda '
          'di casa mia.',
    3549: 'Ah... capisco...',
    3553: 'Grazie al cielo. Casa mia sta a sud, dai campi. Occhio: non so che '
          'cosa ci si sia messo dentro.',
    3559: 'Allora? I gatti se ne sono andati?',
    3575: 'Come? Un domatore di gatti? Santo cielo... Non ho idea di che cosa ci '
          'facesse in casa mia una creatura simile. Comunque... grazie lo stesso.',

    # ---------------- MIA, la finta ingenua (dal giapponese) ----------------
    3713: 'Ah, ecco chi va all\'avventura! Buon lavoro, signorsì♪',
    3717: 'Vado a catturarlo',
    3718: 'A-arrivederci',
    3719: 'Lallalla♪ gatto gattino gattetto♪ Oooh, ecco chi va all\'avventura~. '
          'Un gatto d\'argento, l\'hai mai visto? Il sogno di Mia è farci il '
          'bagno insieme! Gatto gattino♪',
    3722: 'Sì, sì♪ Arrivederciii♪',
    3726: 'Ahiahi. Davvero~?! Non vedo l\'ora♪ Gatto gattino gattetto~♪',
    3732: 'Mmm mmm♪ gatto gattino~ ancora niente~?♪ Nihihi!',
    3761: 'Ahiahi? Ma quello è... un gatto d\'argento! Ooh♪ Mia è felicissima! '
          'Vieni qua~ in braccio♪ Nihihi!',
    3770: 'Ah, giusto: questo è per te! Si chiama cuore di mostro: basta '
          'portarlo addosso e alza le probabilità di dominare le creature♪',

    # ---------------- NAIVE KYLE, le corna di unicorno ----------------
    7194: 'Che strano... gliene ho conficcate addosso dappertutto, di corna di '
          'unicorno, e non è servito a niente. Che non ne bastino ancora...?',
    7197: 'Eh? Mi hai portato altre corna di unicorno?',
    7198: 'Sì, ecco',
    7199: 'No, veramente',
    7205: 'Consegni un corno di unicorno.',
    7208: 'Grazie! Speriamo che stavolta guarisca...',
    7211: '"Occhio anche tu agli attacchi di follia, " + '
          '_onii(cdata(CDATA_SEX, CHARA_PLAYER)) + "."',
    7219: '"Uuh... il papà... il papà è diventato strano... La guaritrice dice '
          'che le corna di unicorno lo curano, ma io non ne ho. Ti prego, " + '
          '_onii(cdata(CDATA_SEX, CHARA_PLAYER)) + "! Portamene un po\'!"',
    7222: 'Ti do una ricompensa. Ti prego!',
    7226: 'Che sollievo... Ma la follia del papà è messa proprio male. Per '
          'sicurezza, portamene tante.',
    7248: 'Mi hai portato delle corna di unicorno? Grazie!',
    7251: 'Se trovi delle corna di unicorno, portamele.',
    7256: '"Con tutte queste il papà starà meglio di sicuro... Grazie, " + '
          '_onii(cdata(CDATA_SEX, CHARA_PLAYER)) + "! Adesso gliele provo '
          'subito. Tieni, la ricompensa!"',
}

LOTTO = 'lavoro/84-chat-cani-gatti.jsonl'

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
