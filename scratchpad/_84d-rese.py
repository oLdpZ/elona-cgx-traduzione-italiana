# -*- coding: utf-8 -*-
"""Le rese dei TRE NINJA DI TYRIS (84a): chat.hsp :8309-:8400, tre zone chiuse.

Un sistema di tre parlanti che sono due persone e mezzo:

    :8309-:8317  Getuei il maestro ninja        il fratello maggiore
    :8318-:8335  Kunoichi alla moda             Eila DOPO l'incarico
    :8336-:8400  Eila la kunoichi fuggiasca     la sorella minore

⭐ Il lessico stava tutto nel DIARIO dell'incarico e nei nomi delle creature:

    text.hsp:10949   «[Lv. 120] La legge dei ninja»
    text.hsp:10959   «una BANDA DI NINJA», «Kurualm», «Sara' lei ad accompagnarmi»
    db_creature      «<Getuei> il maestro ninja», «<Eila> la kunoichi fuggiasca»,
                     «<Kunoichi alla moda>»
    db_creature:59182  la battuta della Kunoichi alla moda, gia' resa e gia' al
                     FEMMINILE: «Nascosta nel buio, colpisco il male...» — in
                     giapponese Eila dice 僕, ma il progetto ha gia' deciso.
    screen.hsp:1690  «Eila prega: Che tu possa ritrovare una vita tranquilla...»

⚠️ «adventurer» rivolto al GIOCATORE non e' «avventuriero»: il progetto ha gia'
la forma che non ha genere, «tu che vai all'avventura» (chat.hsp:1469, :1595).

⭐⭐ La deroga di famiglia: il でござる. `:8346` e `:8347` sono le due voci di
menu con cui il GIOCATORE risponde a Eila, e in giapponese sono in finto
parlare da samurai (「御意」, 「無理でござる」); `:8351` e' Eila che gli va dietro
con lo stesso でござる. L'inglese ha buttato via lo scherzo tutt'e tre le volte
(«With pleasure.», «Impossible.», «That's a troubling thing to hear.»). Si
segue il giapponese e le tre rese si scrivono insieme, in un italiano
appositamente arcaico: «Come comandate» / «Non e' cosa» / «Cotesta risposta mi
mette in imbarazzo». ⚠️ E' una TERZA coppia-eco della giornata, dopo :7463/:7484
di Lune e :6378/:6382 di Silvia.

⚠️ La seconda deroga e' `:8322`: くぅ～！ e' un verso di ENTUSIASMO e l'inglese
l'ha reso «Oh, no!», che dice il contrario. La riga sta in bocca a una che ha
appena descritto la propria vita ideale.

⚠️ La terza e' `:8348`: l'inglese dice «I stopped telling him that I don't want
to be a ninja» dove il giapponese dice il contrario — 「僕が忍者やめたいって
いくら言っても」, «per quante volte glielo dica». Il seguito inglese («but it's
still true») e' una toppa su quel controsenso.

⭐ E il lotto porta con se' una FAMIGLIA che non e' di questa zona: le cinque
righe rosse «Required Fame: N» (`:1366`, `:3590`, `:3876`, `:3936`, `:8341`).
Sono cinque firme diverse perche' cambia il numero, ma sono la stessa
ETICHETTA DI SISTEMA — non la voce di un personaggio — e renderne una sola
avrebbe fatto leggere allo stesso giocatore la stessa riga una volta in
italiano e una in inglese. E' il difetto della sorella H (82a) in piccolo, e si
evita rendendole tutte e cinque.
"""
import io, json, sys

RESE = {
    # ---------- GETUEI, il fratello maggiore (Culla del Caos) ----------
    8312: 'Mia sorella aveva un gran talento, ma l\'addestramento le stava '
          'stretto e scappava di casa in continuazione. Le ho perfino '
          'inscenato la morte, per farla uscire dal mondo shinobi. E invece, a '
          'furia di giocare, è diventata più forte di me e si è inventata un '
          'ninjutsu tutto suo... Bel fratello maggiore che sono.',
    8313: '...Be\', però. Quella mia sorella che nell\'età ribelle era un '
          'flagello, adesso si affida a me! Sono felicissimo! E allora il '
          'fratello maggiore ci si mette d\'impegno.',

    # ---------- LA KUNOICHI ALLA MODA, cioe' Eila dopo ----------
    8322: 'Di giorno, una ragazza qualunque che ama la moda e le chiacchiere. '
          'Di notte si confonde col buio e usa il ninjutsu per la gente... '
          'Aaah! È questo, è proprio questo! Il mio ideale di vita da ninja!',
    8326: 'Ma guarda... ci sei anche tu? Ah, già, vai all\'avventura.',
    8327: 'Grazie di allora. Volevo venire io a ringraziarti, prima o poi... '
          'Sai com\'è, in mezzo alla gente mi tocca fare la cittadina per bene.',
    8328: 'La scuola di famiglia l\'ho lasciata quella volta, ma adesso in giro '
          'se ne vedono di tutti i colori. Combatto il caos con un ninjutsu '
          'tutto mio! Ed è bellissimo: comunque mi vesta, nessuno viene a '
          'farmi la predica sulla disciplina. Il massimo!',

    # ---------- EILA, la kunoichi fuggiasca ----------
    8339: 'Ehm... e tu chi saresti?',
    8345: 'Uhm... tu sì che sembri in gamba. Forse posso chiederlo a te.',
    8346: 'Come comandate',
    8347: "Non è cosa",
    8348: 'Mio fratello maggiore comanda una banda di ninja, e non c\'è verso '
          'di farlo ragionare! Gli ho detto mille volte che voglio smettere, e '
          'lui giù con la storia dei segreti... Un testardo simile non lo '
          'considero più un fratello! Va\' a spazzarla via tu, quella banda!',
    8351: 'Cotesta risposta mi mette in imbarazzo.',
    8355: 'Evviva! Fammi un cenno quando è il momento: ti accompagno io alla '
          'tenuta.',
    8360: '(Chiudere gli occhi)',
    8361: 'Che cosa hai in mente?!',
    8362: 'Tutto pronto? Ti accompagno io, ma tieni gli occhi chiusi un '
          'momento...',
    8365: 'Ma cosa... ti accompagno e basta, ecco!',
    8392: 'Già, hai battuto mio fratello: sei davvero in gamba. Non mi ero '
          'sbagliata sul tuo conto.',
    8393: 'Ehehe... Comunque adesso posso finalmente smettere di fare la '
          'ninja. A dirla tutta il mio sogno era girare per le strade con dei '
          'vestiti carini, senza niente che mi leghi... Ho anche comprato '
          'degli accessori: quando torni mi dirai se mi stanno bene.',
    8394: '...! Questa presenza...?!',

    # ---------- l'etichetta di sistema, tutte e cinque ----------
    8341: 'Fama richiesta: 40000 ',
    1366: 'Fama richiesta: 20000 ',
    3590: 'Fama richiesta: 5000 ',
    3876: 'Fama richiesta: 3000 ',
    3936: 'Fama richiesta: 7000 ',
}

LOTTO = 'lavoro/84-chat-ninja.jsonl'

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
