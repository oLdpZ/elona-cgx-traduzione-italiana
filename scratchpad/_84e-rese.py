# -*- coding: utf-8 -*-
"""Le rese di ICOLLE il biochimico (84a): chat.hsp :3971-:4812.

Due sistemi in un parlante solo: l'incarico delle cinque cavie (che paga con la
macchina genetica) e, a incarico finito, il menu che TOGLIE parti del corpo.

Il lessico letto dal dato:

    ITEM_ID_MONSTER_BALL   monster ball    «sfera dei mostri»   db_item
    ITEM_ID_GENE_MACHINE   gene machine    «macchina genetica»  db_item:143309
    text.hsp:10431   il diario: «Icolle, a Porto Kapul, mi ha chiesto di
                     catturare 5 creature per i suoi esperimenti. Devono stare
                     dentro una sfera dei mostri.»
    chat.hsp:16648   il lotto di Leold, 80a: «slot d'equipaggiamento»
    action.hsp:12530 e chat.hsp:16811, la famiglia gemella e opposta:
                     `name(r1) + " ha una parte nuova: " + bodyn(...)` — qui la
                     parte si PERDE, e la resa e' lo specchio di quella.
    screen.hsp:1588  Icolle nell'arena, gia' reso: «Su, su! Se ti arrendi
                     l'esperimento finisce li'!»

⚠️ Icolle e' MASCHIO: `db_creature.hsp:123563` gli mette `cdata(CDATA_SEX) = 0`,
e il nome gia' reso dice «il biochimico». Controllato prima di scrivere, per la
regola della 82a (Orphe).

⭐⭐ LA DEROGA CHE CONTA E' `:3978`, ed e' l'inglese che nasconde al giocatore
la CONSEGUENZA di una scelta. Quel testo e' il cartello sopra un menu, e il
menu e' una trappola: accettando, si PERDONO parti del corpo. Il giapponese lo
dice — 「後天的身体部位の削除実験と書かれた紙が散らばっている」, «fogli con su
scritto: esperimento di rimozione delle parti del corpo acquisite» — l'inglese
lo annacqua in «an experiment to remove body parts», senza dire quali ne' che
sono le tue. Si segue il giapponese, ma solo per la PAROLA che serve al
giocatore: «(Un esperimento per togliere le parti ACQUISITE...)», 51 caratteri,
una riga come l'inglese. La scenografia dei fogli sparsi si perde; la
conseguenza no, ed era quella il motivo della deroga.

⭐ `:4360` e `:4741` sono il caso GIRATO di quello di Silvia: li' un solo
giapponese diventava tre inglesi diversi, qui due giapponesi diversi diventano
lo STESSO inglese («Sacrifice is inherent to the advancement of science~»).
Sono due firme, e si rendono diverse come il giapponese le fa diverse.

⚠️ `:4360` e `:4741` passano da `cnvtalk`, che mette le virgolette da se': la
resa va NUDA. (Il ramo giapponese le ha scritte a mano, 「...」.)

⚠️ `:4739` porta `his(r1)` a UN argomento: morfologia inglese, si toglie (74a).
E `name(r1)` vuole la terza persona.

⚠️⚠️ `:4783` e' condivisa con TRE incarichi lontani (`:7242` il corno di
unicorno, `:12366` il kit di materiali, `:12458` le calze): il testo segue
`itemname(cnt, 1)`, cioe' un nome con l'articolo indeterminativo e di genere
qualunque. Nessun participio regge — «consegnato» si romperebbe su «una sfera
dei mostri» — e la resa e' costruita apposta per non accordarsi: «: consegna
fatta.»
"""
import io, json, sys

RESE = {
    # ---------- il menu che toglie le parti (a incarico finito) ----------
    3974: 'Che c\'è? Non venirmi a parlare, sono occupato con gli esperimenti!',
    3975: 'Far aiutare un compagno nell\'esperimento',
    3976: 'Aiutarlo io nell\'esperimento',
    3978: '(Un esperimento per togliere le parti acquisite...)',
    3982: 'Va bene',
    3983: 'Ooh, davvero?! E allora subito, mi fai da cavia! Su, spogliati di tutto!',
    3988: 'Questo lo mettiamo così... e poi... eh? Vabbè, andrà bene lo stesso. '
          'E già che ci siamo, anche questo qua...',
    4353: 'Ti accorgi che certi oggetti non li puoi più equipaggiare...',
    4360: 'Il progresso della Scienza vuole le sue vittime!',
    4366: 'Ooh, benissimo! E chi mi dà una mano?',
    4375: 'E allora subito, mi fa da cavia! Su, spogliarsi di tutto!',
    4376: 'Questo lo mettiamo così... e poi... uhm? Ah, era questo? Vabbè, '
          'intanto facciamo così...',
    4739: 'name(r1) + " perde delle parti acquisite..."',
    4741: 'Il progresso e lo sviluppo della Scienza vogliono le loro vittime!',

    # ---------- l'incarico delle cinque cavie ----------
    4751: 'Dare una mano',
    4753: 'Oh oh oh! Arrivi proprio al momento giusto. Sono così indaffarato '
          'che mi farei aiutare anche da un gatto. Sto conducendo una ricerca '
          'nel campo più straordinario che ci sia, l\'ingegneria genetica: '
          'prendo due creature viventi e le combino per ottenerne una più '
          'forte! Hai mai sentito niente di più meraviglioso? Per l\'ultima '
          'fase mi servono cinque cavie: non è che me le vai a prendere tu? '
          'Come ricompensa ti do la macchina genetica che sto costruendo.',
    4756: 'Che razza di sciocco! Levati di torno!',
    4766: 'Bene, bene! Prendi queste sfere dei mostri. Sai come si usano? Sì, '
          'sì: le tiri addosso a un mostro quando è in fin di vita. Occhio '
          'però: sulle creature che superano il livello della sfera non '
          'funzionano. Portamene cinque catturate. E mi raccomando: portamele '
          'DENTRO le sfere!',
    4783: ': consegna fatta.',
    4790: 'Oh oh! Ecco la merce che aspettavo. Adesso l\'esperimento può andare '
          'avanti.',
    4793: 'Ripetiamolo un\'ultima volta... per procedere mi servono cinque '
          'cavie. CINQUE.',
    4798: 'Riuscito! L\'esperimento è riuscito alla grande! Hai fatto un ottimo '
          'lavoro, e per ringraziarti ti regalo la macchina genetica numero '
          'uno, quella storica. Trattala con riguardo!',
}

LOTTO = 'lavoro/84-chat-icolle.jsonl'

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
