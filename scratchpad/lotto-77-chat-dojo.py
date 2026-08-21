# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, il dojo di Nazuna, chiuso intero (`:8812`-`:9186`).

Nazuna e' un personaggio fisso e **donna** — «<Nazuna> la maestra d'armi»
(`db_creature.hsp:84393`, `db_card.hsp:8135`) — quindi qui il genere di chi
parla si sa e si accorda. Registro da istruttrice di arti marziali: imperativi,
「貴様」, urla di kendo.

⚠️⚠️ **La firma di 「やめる」/«No way!» si tira dietro il blocco 47** (`:22538`,
`:22540`, «Indagare su un compagno»): l'unica riga rappresentante e' `:9051`,
quindi tradurre il bottone del dojo traduce anche quello dell'informatore, e il
menu di la' resterebbe meta' e meta'. Due rese in piu' e si chiude anche quello.
E' la lezione della 76a, terza volta.

⚠️⚠️⚠️ **E 「断る」/«I refuse.» (`:9110`) sta in CINQUE menu, non in due.** La
riga rappresentante e' `:2351`, dentro il menu con cui Erystia chiede aiuto per
Palmia; ma la stessa firma la portano anche `:2996` (le monete di bronzo),
`:6245` (la droga in capsula) e `:8703` (la tartaruga della principessa). Tradurre
il bottone di Nazuna li ha accesi tutt'e quattro, e a dirlo e' stata `bilingui`
DOPO la reimportazione, non una lettura del codice: **tre menu erano tutti
inglesi, quindi non c'era niente da vedere finche' la firma non e' diventata
italiana.** Costa quattro rese chiuderli, e si chiudono. La battuta di Erystia
sopra resta inglese — e' un `buff`, non una voce di menu — ed e' lo stato che la
73a ha gia' accettato per tutti i menu di `*chat_default`.

⚠️⚠️⚠️ **E la chiusura si e' propagata di un altro passo: chiudere un menu ne
apre un altro.** La resa di 「ブロンズ硬貨を渡す」 (`:2993`, scritta per chiudere
il menu di `:2996`) ha la stessa firma di `:3029`, dentro il menu del
**potioman** — e li' e' rimasta a meta' finche' non e' entrata anche 「やめておく」
(`:3032`). Cioe': ogni resa nuova puo' accendere un menu spento, e la rete va
rilanciata **dopo ogni giro**, non una volta sola. Tre giri per arrivare a zero.

⚠️ **E `:8825` e' stato accorciato da `menu_dialogo`**: «Iscrivere un compagno
(10000 oro)» fa 33 caratteri contro i 22 dell'inglese, e la regola del menu a due
colonne e' «se l'inglese ci sta in 24, l'italiano ci deve stare». «Iscrivere
(10000 oro)» ne fa 21: chi si iscrive lo si sceglie nella schermata dopo.

⚠️⚠️⚠️ **`:8850` e `:9128` sono la riga giusta dell'evento sbagliato** (58a).
L'inglese dice «You've no desire to improve! You wuss!», che e' la battuta di
`:9115`; il giapponese dice 「ここは護衛対象の面倒を見る場所ではないぞ」 e il
**codice** gli da' ragione — il ramo scatta su `CHARA_BIT_BODYGUARD` e
`CHARA_BIT_GUARD_TEMP`, cioe' quando il compagno e' sotto scorta. Si segue il
codice: «Ehi! Qui non si fa la balia a chi devi scortare!».

⚠️⚠️ **Deroga dichiarata a `:8970`: l'inglese ha perso la battuta.** 気合 e'
diventato «cool yells» e 「足が無かろうと気合次第で蹴りが可能」 («anche senza
gambe, con la grinta, tiri calci») e' diventato «Your feet will be able to
annihilate», che non vuol dire niente. Il senso e' la **grinta** che sostituisce
il corpo, e senza quello il paragrafo non sta in piedi.

⚠️ **`:9115` non puo' dire «rammollito»**: e' un insulto al giocatore e
l'aggettivo si accorda. «Che pappamolle!» e' invariabile — la via d'uscita (1)
della 75a, il nome al posto dell'aggettivo.

⚠️ **`:8903` e `:9181` nominano l'animale prima di riprenderlo col pronome**:
«quando rivuoi il tuo animale, vieni a riprendertelo» sta in piedi perche'
l'antecedente e' una parola nostra, «animale»; un «lo» nudo si accorderebbe col
sesso della bestia, che non si sa. E' la regola (3) della 75a, l'OGGETTO.

⭐ **Il menu e la sua schermata dicono le stesse parole**: la voce «Cambiare
modo di lanciare le magie» (`:8832`) apre il prompt «Scegli il nuovo modo di
lanciare le magie!» (`:8945`, gia' reso nella 76a), e «Cambiare modo di
combattere» (`:8835`) apre `:8990`. E' la regola della 73a.

💡 **Le due battute del cambio d'abito sono la stessa frase con due firme**:
`:8888` dice «no need for fancy clothing», `:9166` «no need of fancy wear».
Stessa resa. Cosi' `:8883` e `:9161`, che pero' condividono la firma.

⚠️ Dentro `cnvtalk` va **solo la battuta e senza virgolette**, che le mette
`init.hsp:171` (74a); «Nazuna urla: » sta fuori, come `screen.hsp:1708`
(«Nazuna osserva: ») e `screen.hsp:1588`.

    python scratchpad/lotto-77-chat-dojo.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-dojo.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((2350, 2351), (2993, 2996), (3029, 3032), (6244, 6245), (8703, 8705),
        (8812, 9186), (22538, 22540))

CAMBIATI = ('"Nazuna urla: " + cnvtalk("Per allenarsi non serve la moda!'
            ' Su, cambiati!")')

RESE = {
    # --- i QUATTRO menu che la firma di 「断る」 si e' tirata dietro
    (2350, 'I will gladly pledge my strength to Palmia.'): 'Do il mio aiuto',
    (2351, 'I refuse.'): 'Rifiuto',
    (2993, 'Here, take these bronze coins.'): 'Dare le monete di bronzo',
    (6244, 'Take it.'): 'Cedere la capsula',
    (8704, '(Hop on the tortoise)'): '(Salire sulla tartaruga)',
    (8705, "I'm not a substitute."): 'Non faccio da rimpiazzo',
    (3032, 'I think not.'): 'Lascio stare',

    # --- il dojo: l'ingresso e il menu
    (8815, "Hey you! This isn't a dojo!"): 'Ehi tu! Questo non è un dojo!',
    (8822, "It's nothing."): 'Niente, niente',
    (8825, 'Entrust ally (10000gp)'): 'Iscrivere (10000 oro)',
    (8829, 'Special training'): 'Addestramento speciale',
    (8832, 'Change Magic Style (200gp)'):
        'Cambiare modo di lanciare le magie (200 oro)',
    (8835, 'Change Melee Style (200gp)'):
        'Cambiare modo di combattere (200 oro)',
    (8837, 'Gah!! Hm? State your business!'):
        'Haaaaa! Hmpf!! ...Eh? Che cosa vuoi?',

    # --- iscrivere un compagno
    (8850, "You've no desire to improve! You wuss!"):
        'Ehi! Qui non si fa la balia a chi devi scortare!',
    (8883, ' stay here.'): 'cdatan(CDATAN_NAME, c) + " resta qui."',
    (8888, "Nazuna yells, You've no need for fancy clothing in training! Now, go change!"):
        CAMBIATI,
    (9166, "Nazuna yells, You've no need of fancy wear in training! Now, go change!"):
        CAMBIATI,
    (8903, "Ohh, they seem worthy of my time. I'll take care of them. If you want them back then feel free to take them."):
        ("Oh, c'è della stoffa! Tengo qui il tuo animale per un po'; quando lo "
         'rivuoi, vieni pure a riprendertelo.'),
    (9181, "What's the meaning of this half-hearted pet! I'll take them. I'll train them from the ground up!"):
        ('Ma che roba è questo animale mezzo cotto?! Me lo tengo io. '
         'Lo rifaccio da capo a piedi!'),

    # --- il cambio di stile: magia e corpo a corpo
    (8910, 'ally'): 'Un compagno',
    (8911, 'myself'): 'Io',
    (8912, 'Did you know that wizards usually chant as their medium for exercising control over magic? However, with my guidance you can change your way of controlling mana and with sight and feeling a person can learn to use their own willpower as the medium. Now then, who wants to receive my guidance!?'):
        ('Lo sai che di solito i maghi usano la voce come tramite per governare '
         'la magia? Ma con la mia guida si cambia il modo di raccogliere il mana: '
         'sguardo, tentacoli, quel che vuoi, il resto lo fa la grinta. Allora, '
         'chi la vuole la mia guida?'),
    (8950, "Well... this shouldn't take long!"): 'Bene... facciamo in fretta!',
    (8962, "It's done. Come again!"): 'Ecco fatto. Torna quando vuoi!',
    (8970, 'Martial arts is all about cool yells. With my guidance in cool yelling your whole body can become a weapon! Your feet will be able to annihilate through the use of cool yelling. Your fighting spirit will soar and you will be able to kill using only your cool yells and glares! Now then, who wants to receive my guidance!?'):
        ('Il corpo a corpo, alla fine, è tutto grinta. Con la mia guida la metti '
         'nel colpo e diventi un\'arma da capo a piedi! Anche senza gambe, se hai '
         'grinta tiri calci! E se sprigioni lo spirito di lotta, con la grinta '
         'ammazzi anche solo guardando! Allora, chi la vuole la mia guida?'),
    (8990, 'Select new melee style!'): 'Scegli il nuovo modo di combattere!',

    # --- l'addestramento speciale
    (9049, 'Too expensive, but okay.'): 'Allenali pure',
    (9051, 'No way!'): 'Annulla',
    (9052, "You want the ones I'm watching to take special training... That's the spirit! That'll cost , not a problem?"):
        ('"Addestramento speciale per quelli che tengo qui? Bello spirito! '
         'Fanno " + trcost + " monete d\'oro, va bene?"'),
    (9056, 'This is for the sake of continuing this dojo. Go and get me the money!'):
        "Anche questo dojo deve tirare avanti. Va' a procurarti i soldi!",
    (9104, 'Nazuna yells, I trained all their attributes and skill potentials!'):
        ('"Nazuna urla: " + cnvtalk("Ho allenato gli attributi e il potenziale '
         'di tutti quanti!")'),

    # --- il primo incontro: iscriviti o offri qualcun altro
    # (il «Rifiuto» del bottone :9110 e' la voce :2351 qui sopra: stessa firma)
    (9111, '(Make a pet take the bullet for you)'):
        '(Offrire un compagno al posto tuo)',
    (9112, "Why aren't any pupils joining!? Hey you, I'm going to retrain you so enroll now!"):
        ('Cheeeestooooo!! Perché non arriva nessun allievo?! Ehi, tu là: '
         'ti rimetto in sesto io, iscriviti subito!'),
    (9115, "You've no desire to improve! You wuss!"):
        'Non hai nessuna voglia di migliorare?! Che pappamolle!',

    # --- il blocco 47, tirato dentro dalla firma di 「やめる」
    (22538, 'It will cost you 100 gold pieces.'):
        "Ti costa 100 monete d'oro, va bene?",
    (22540, 'Investigate.'): 'Indagare',
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
