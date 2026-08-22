# -*- coding: utf-8 -*-
"""YERLES: Melkawn, Kurualm, Eirel, Melugas (84a). chat.hsp :6720-:7113.

    :6720-:6746  Heinrich il generale corazzato
    :6747-:6818  Zernard il mercenario capace   la caccia ai pirati
    :6819-:6895  il Cane poliziotto             i gattini smarriti
    :6896-:6964  Milis, capitano delle forze speciali   il diversivo
    :6965-:7113  Orville l'agente di sicurezza  il passaggio sotterraneo

45 firme su una zona di 72 (27 erano gia' rese: il sottosistema di gestione
della citta' di Orville).

Il lessico e' venuto tutto dai DIARI dei quattro incarichi e da db_card:

    text.hsp:10661  «<Cane poliziotto>, a Eirel», «i gattini smarriti»
    text.hsp:10679  «<Milis>, a Eirel», «attirare l'attenzione delle truppe di
                    Eulderna», «il diversivo»
    text.hsp:10713  «<Orville>, a Melugas», «l'esercito juere che occupa il
                    passaggio sotterraneo»
    text.hsp:10729  «[Lv. 100] Caccia ai pirati», «<Zernard>, di Kurualm»,
                    «il capo dei pirati»
    db_card:9968    ⭐ 決戦兵器 -> «l'arma della battaglia decisiva» (il nome
                    della carta <Yerleswood>): non «arma decisiva»
    db_card:8915    «<Gavela> l'ingegnere capo»
    action.hsp:16971 «il gatto randagio»
    action.hsp:16723 «la fanteria MECCANICA Yerles»: da li' «braccio meccanico»
                    per パワーアーム

⭐ IL REGISTRO DEL CANE POLIZIOTTO E' GIA' DECISO. In giapponese parla con
であります (finto militaresco) e con ワン attaccato ai verbi; in italiano
`db_creature.hsp:96598` gli fa gia' dire «Alt! Un altro passo e sparo, bau!».
Il tic e' quel «bau!» in coda, e si continua quello.

⚠️ DUE SESSI CONTROLLATI PRIMA DI SCRIVERE, e uno dei due cambiava le rese:
  - MILIS e' DONNA (`cdata(CDATA_SEX) = 1`), e il diario gia' reso lo conferma
    («Devo tornare a parlarLE», text.hsp:10679). Le sue rese si accordano.
  - GAVELA e' UOMO (`cdata(CDATA_SEX) = 0`), come dice il giapponese di `:6740`
    (「白衣を着た男」). Il nome di carta «<Gavela> l'ingegnere capo» non lo
    diceva.

⚠️ Il genere del GIOCATORE a `:6932`: «make sure to live so we can meet again»
non puo' diventare «resta viva/vivo». Diventa «torna indietro».

⚠️ `:6871` passa da `cnvtalk`, che mette le virgolette da se': la resa del
gattino va nuda. E il giapponese 「おうちかえれう？」 e' storpiato come parla un
cucciolo; l'italiano fa la stessa cosa con «casetta».

⚠️ `:6754` porta l'epiteto del giocatore: stessa forma della 84a a `:3594`,
«ma tu sei X!», senza articolo e senza aggettivi che si accordino.
"""
import io, json, sys

RESE = {
    # ---------------- HEINRICH, il generale corazzato ----------------
    6723: 'La richiesta te la spiega Gavela, senti da lui. La ricompensa però '
          'l\'ho scelta io: vedrai che scossa.',
    6727: 'È stato un bel momento, quando l\'arma della battaglia decisiva è '
          'emersa spaccando le acque; ma ogni volta che deve partire ci vuole '
          'un\'eternità. Finché non sappiamo quando arriverà il prossimo '
          'attacco, non resta che tenerla a terra. Pare che verso la capitale '
          'stiano comparendo mostri anche più forti: non abbiamo il fiato per '
          'metterci a litigare con Eulderna o con Juere.',
    6731: 'Col rischio di essere contaminati o assimilati, mandargli contro '
          'uomini in carne e ossa non è una buona idea. Bisogna accelerare i '
          'lavori sullo Yerleswood Mk II...',
    6735: 'La squadra d\'indagine sta scendendo verso il fondo delle rovine. '
          'Raggiungila e mettiti di scorta. Anche il nostro reparto partirà a '
          'breve.',
    6739: 'Come? Vuoi entrare a Remido? Uhm... sembri in gamba, però. Se ti '
          'prendi la scorta della squadra d\'indagine, posso pensarci.',
    6740: 'Nel laboratorio accanto alla taverna c\'è un uomo in camice bianco, '
          'Gavela. Se fai da scorta, fatti fare da lui la tessera per il '
          'passaggio. È un tipo strano, però: dovrai saperci fare.',
    6744: 'Guarda qua, questo braccio meccanico. Fa impressione, eh? La scienza '
          'di Yerles non ha rivali.',

    # ---------------- ZERNARD, il mercenario ----------------
    6750: 'Farmi stendere dal mal di mare... si vede che devo ancora allenarmi.',
    6754: '"Oh, ma tu sei " + cdatan(CDATAN_AKA, CHARA_PLAYER) + "! Da queste '
          'parti si comincia a parlare parecchio di te."',
    6755: 'Ci sto!',
    6756: 'Le navi mi fanno venire i brividi',
    6757: 'Ecco: che ne dici di venire a caccia di pirati con me? Da queste '
          'parti i pirati brulicano, e io ho intenzione di prendere una barca e '
          'andare a fregargli il tesoro. La barca la pago io, quindi del bottino '
          'sette a me e tre a te.',
    6760: 'Come? Ti è affondata sotto anche l\'ultima?',
    6769: 'E allora andiamo! Io e te li spazziamo via, quei pirati.',
    6781: 'Torniamo a caccia',
    6782: 'Tutto bene?',
    6783: 'U-urgh... ma quanto beccheggia, questa barca...',
    6786: 'N-nessun problema. Però fammi riposare ancora un po\'...',
    6795: 'Ah... ah...? G-giusto...',
    6813: 'Urgh... come, hai abbattuto il capo dei pirati? Roba da matti... Ma '
          'tu il mal di mare non ce l\'hai? Io sono rimasto steso in coperta '
          'tutto il tempo... Eh? Il tesoro? Chi se ne importa, strofinami la '
          'schiena...',

    # ---------------- IL CANE POLIZIOTTO ----------------
    6822: 'Negli ultimi anni i gattini che si perdono sono aumentati a vista '
          'd\'occhio! Se ne vedi uno smarrito, portalo qui da me, bau! '
          'Ricompense non ne posso dare... ma per i gattini e per le loro '
          'famiglie, ti chiedo di darci una mano!',
    6828: 'Accarezzargli la testa',
    6830: '(Consegnare il gattino smarrito)',
    6832: 'Anche i genitori dei gattini sono in pena! Vorrei trovarli presto e '
          'togliergli il pensiero...',
    6835: 'Bau?',
    6847: 'Deve ancora crescere.',
    6871: '"Consegni il gattino smarrito al Cane poliziotto. " + '
          'cnvtalk("Torno a casetta?")',
    6890: 'Questo cucciolo... sì, è uno di quelli segnalati come scomparsi! Lo '
          'riporterò ai suoi genitori, ne rispondo io. Grazie della '
          'collaborazione, bau! Ce ne sono ancora tanti smarriti: se ne trovi '
          'altri, portameli!',

    # ---------------- MILIS, capitano delle forze speciali (donna) --------
    6899: 'I guerrieri in gamba come te non mi dispiacciono. Perché non provi '
          'l\'esame di arruolamento da noi? Aspetto il giorno in cui '
          'combatteremo insieme.',
    6903: 'Sono Milis, capitano della settima unità speciale dell\'esercito di '
          'Yerles! Cerco qualcuno che vada all\'avventura, come te, per prendere '
          'parte a un\'operazione.',
    6904: 'D\'accordo',
    6905: 'Passo',
    6906: 'Le rovine che stiamo esplorando fanno gola anche a Eulderna. Vorrei '
          'tagliare la loro linea di rifornimento, ma il reparto che hanno di '
          'stanza qui vicino è d\'intralcio, e di truppe non ne ho abbastanza '
          'per occuparmi di tutt\'e due le cose. Potresti attirare tu la loro '
          'attenzione? La ricompensa, naturalmente, ci sarà.',
    6909: 'Peccato... Se dovessi cambiare idea, torna pure a parlarmi.',
    6913: 'Ti ringrazio di aver accettato. Quando sei in ordine fammi un cenno: '
          'ti accompagneranno i miei uomini.',
    6918: 'Nessun problema',
    6919: 'Mi è venuta in mente una cosa',
    6920: 'Basta che li tenga occupati per un po\'. I preparativi sono a posto?',
    6923: 'Fai presto, mi raccomando.',
    6932: 'Pare che fra le truppe nemiche ci siano anche nostri soldati '
          'soggiogati con la magia. Non esitare: liberali in fretta. E... torna '
          'indietro, così ci rivediamo qui. E adesso... operazione avviata!',
    6959: 'Grazie a te anche la nostra operazione è andata a buon fine... Come? '
          'Non li hai solo distratti, li hai sterminati? Ci hai risparmiato la '
          'fatica di farlo noi. E allora la ricompensa la aumento.',

    # ---------------- ORVILLE, l'agente di sicurezza ----------------
    7082: 'Va bene, ma quel che ti ho appena detto non andarlo a raccontare in '
          'giro!',
    7085: 'M-mi hai salvato...! Ti apro le scale che scendono al passaggio '
          'sotterraneo: vacci subito, ti prego!',
    7092: 'C\'è già chi va in giro a dire che dal sottosuolo si sentono rumori! '
          'Sbrigati a sterminarli!',
    7108: 'Uff, ce l\'abbiamo fatta per un pelo. C\'è mancato poco... Tieni, '
          'come ringraziamento. È equipaggiamento difettoso che prendeva '
          'polvere nel magazzino sotterraneo, ma dovrebbe rendere. Credo.',
}

LOTTO = 'lavoro/84-chat-yerles.jsonl'

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
