# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, cinque schermate a meta': la richiesta e le due risposte.

⚠️⚠️ **Il lotto nasce da una rete nuova**, `scratchpad/menu-meta.py`: elenca i
menu in cui **almeno una voce e' tradotta e almeno una no**, cioe' le schermate
che il giocatore leggerebbe meta' in italiano e meta' in inglese. In `chat.hsp`
ne ha trovati **quindici**. Questi sono i cinque che hanno la stessa forma: un
PNG chiede un favore e offre due bottoni, di cui uno («Accetto», 「引き受ける」)
era gia' reso da mesi e l'altro no.

    :3544-:3545   i gatti in casa                  «Accetto» / [manca]
    :6503-:6504   la H Sister nello scantinato     [manca] / «Accetto»
    :7077-:7078   i soldati di Juere               «Accetto» / [manca]
    :7392-:7393   i funghi e i germogli di bambu'  «Accetto» / [manca]
    :9775-:9776   la caccia al drago               [manca] / «Non mi interessa»

⭐ **Tre bottoni su cinque sono UNA VOCE SOLA**: 「面倒だ」/«Too much trouble.» sta
a `:3545`, `:6503` e `:7078` con la stessa firma, quindi il dizionario ne tiene
una e le tre schermate si chiudono insieme. E' il rovescio buono della trappola
della 76a — la firma condivisa che buca un menu lontano ne chiude anche tre.

⭐ **La schermata non e' il menu: e' il menu PIU' la domanda.** Chiudere le voci
e lasciare inglese il `buff` che le sta sopra sposta il difetto di una riga
invece di toglierlo, quindi ogni schermata porta con se' la sua richiesta.

⚠️⚠️ **Il genere, tre volte.** (1) `:7079` non dice «Avventuriero, arrivi giusto
in tempo!»: e' un vocativo rivolto al giocatore, ed e' la stessa ragione per cui
la 58a lo aveva tolto a `:5194`. (2) Sempre `:7079`, «I didn't realize» diventa
«ho scoperto solo adesso» — passato prossimo con **avere**, che non accorda —
perche' il parlante e' un tecnico di cui non si sa il sesso. (3) `:7394` non
dice «sono rimasto solo io» ma «non e' rimasto nessun altro».

💡 **`:9775` cita una parola della domanda, quindi le due rese vanno scritte
insieme**: il giapponese 「いるみたい？」 ripete l'「いるみたい」 (*pare che ci sia*)
del PNG. In italiano il bottone e' «"Pare"?» e la domanda dice «Pare che...»:
tradotte separatamente, la citazione non citerebbe piu' niente.

⭐ I nomi vengono dal gioco, non dall'inglese: «H Sister» resta invariato
(`text.hsp:10851`) e i 「たけのこ」 sono «germogli di bambu'» (`<Germoglio di
Bambu'>`, `db_creature.hsp:94909`).

    python scratchpad/lotto-76-chat-incarichi.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-incarichi.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((3544, 3547), (6503, 6506), (7077, 7080), (7392, 7395), (9775, 9778))

RESE = {
    # --- i tre bottoni (uno solo nel dizionario) e il quarto
    (3545, 'Too much trouble.'): 'Troppa fatica',
    (7393, 'Serves you right.'): 'Ben ti sta',
    (9775, '\\"Seems like\\"?'): '\\"Pare\\"?',

    # --- :3544 i gatti in casa
    (3546, "Hey you, are you... uh... alright with cats? Well, those filthy creatures took over my house! I've been asking adventurers to remove the cats from my house ever since, but none returned. What's happening in my house? You... could you take a look?"):
        ('Ehi, tu... i gatti ti danno fastidio? Ecco, vedi, quelle bestiacce si sono prese '
         'casa mia! Da allora chiedo agli avventurieri di liberarmene, ma non ne è tornato '
         'nessuno. Che cosa sta succedendo là dentro? Tu... andresti a dare un\'occhiata?'),

    # --- :6503 la H Sister nello scantinato
    (6505, "H-Help me, ! An H Sister settled in my basement recently... I think she's aiming to kill me. Please, get rid of her!"):
        ('"A-aiuto, " + cdatan(CDATAN_NAME,0) + "! Da poco si è installata una H Sister '
         'nel mio scantinato... e ho l\'impressione che ce l\'abbia con me. Ti prego, '
         'liberamene!"'),

    # --- :7077 i soldati di Juere nel passaggio sotterraneo
    (7079, "W-w-what am I going to do?! This is bad, this is seriously bad...!? Gah...! Adventurer, you came at just the right time! The truth is the power to our defense systems has been cut... I didn't realize that the underground passage was occupied by Juere soldiers until just a moment ago. This needs to be secretly taken care of before everyone finds out!"):
        ('C-c-che faccio adesso?! Va male, va malissimo...?! Ah...! Arrivi giusto in tempo! '
         'Il fatto è che il sistema di difesa è rimasto senza corrente... e ho scoperto '
         'solo adesso che il passaggio sotterraneo è occupato dai soldati di Juere. '
         'Sistema la cosa in silenzio, prima che se ne accorgano tutti!'),

    # --- :7392 i funghi che hanno bruciato il villaggio dei germogli
    (7394, "At once time we bamboo sprouts had a peaceful village in this land... But our village was burned when the mushrooms suddenly attacked us. My fellows were all destroyed in the flames... I'm the only one left... Please, destroy the mushrooms living in what used to be our mountain! Avenge my friends!"):
        # ⚠️ accorciata: la prima stesura faceva 7 righe contro le 6 dell'inglese
        ('Un tempo qui c\'era il villaggio dove noi germogli di bambù vivevamo in pace... '
         'poi i funghi ci hanno attaccati e l\'hanno bruciato. I miei compagni sono finiti '
         'tutti nel fuoco, non è rimasto nessun altro... Ti prego, distruggi i funghi che '
         'vivono sul monte che era nostro! Vendica i miei compagni!'),

    # --- :9775 la caccia al drago: la domanda che il bottone cita
    (9777, "Ooh, ooh, are you interested in a dragon hunt? Seems like there's a dragon in the inner parts of the volcano that's south of these ruins."):
        ('Ehi, ehi, ti interessa una caccia al drago? Pare che nel cuore del vulcano a sud '
         'di queste rovine ci sia un drago.'),
}


def main() -> int:
    voci = []
    for l in io.open(RESTANTE, encoding='utf-8'):
        v = json.loads(l)
        if any(a <= v['riga'] <= b for a, b in ZONE):
            voci.append(v)

    errori = []
    viste = set()
    for v in voci:
        k = (v['riga'], v['en'])
        if k not in RESE:
            errori.append('%d: voce senza resa | %r' % (v['riga'], v['en'][:80]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:80]))
    if errori:
        for e in errori:
            print(e)
        return 1

    with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%s: %d voci' % (USCITA, len(voci)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
