# -*- coding: utf-8 -*-
"""75a — `chat.hsp`, l'artigiano: munizioni, maledizioni, rinforzo, peso, tappi.

Sei servizi che si chiedono a un PNG e che il menu della 73a nomina gia' in
italiano: `chatval` 54 (ricaricare le munizioni), 62 (togliere le maledizioni),
63 (rinforzare), 115 (i tappi di pozione), 64 e 95 (alleggerire e appesantire).

⚠️⚠️ **Qui il genere che non si conosce e' quello dell'OGGETTO.** `itemname(ci)`
puo' essere «la pozione» o «il mantello», quindi «diventa piu' leggero» sarebbe
accordato: le due rese diventano «perde peso» e «prende peso», che sono verbo e
nome e non accordano niente. Stessa ragione per cui `:23687` e' «Non si puo'
rinforzare oltre» invece di «Non posso rinforzarlo di piu'», e `:23702` e' «si
avvolge in un'aura dorata».

⚠️ `_s()`, `_s2()` e `is2()` sono morfologia inglese e si tolgono: il progetto
lo fa gia' in 22 rese con `_s2`, tutte in terza persona singolare del presente
(`action.hsp:6662` «itemname(ci) + " brilla d'argento."»).

⭐ **Le parole vengono dai siti gemelli, non da capo**: «tappi di pozione» col
formato «[Tappi rimasti: N]» e' `action.hsp:8708`, che dice la stessa cosa;
`gold pieces` e' «monete d'oro» (`glossario.md:186` piu' 34 rese); e やめる e'
«Annulla», come in `chat.hsp:17702`, `god.hsp:350`, `text.hsp:1467`.

⚠️ **Una deroga dichiarata a «si traduce dall'inglese», `:23722`.** Il giapponese
e' 何に使うのか知らないが…廃棄品なら持って行っていいよ, «non so che te ne farai,
ma se e' roba da buttare prendila pure»; l'inglese l'ha girato in «Bring what I
was supposed to dispose of», che nel contesto **non sta in piedi** — il
giocatore i tappi li sta ricevendo, non portando. E' il caso che `decisioni.md`
prevede: l'inglese perde informazione e la resa letterale non avrebbe senso.

    python scratchpad/lotto-75-chat-equipaggiamento.py
"""
import io
import json
import sys

USCITA = 'lavoro/75-chat-equipaggiamento.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((23313, 23348), (23454, 23478), (23675, 23840))

RESE = {
    # --- 54: ricaricare le munizioni
    (23315, "Reload what? You don't have any ammo in your inventory."):
        'Ricaricare cosa? Non hai munizioni nello zaino.',
    (23319, 'It is currently in preparation.'): 'Al momento è ancora in preparazione.',
    (23322, 'Sure, let me check what type of ammo you need... Okay, reloading all of your ammo will cost  gold pieces.'):
        ('"Vediamo di che munizioni hai bisogno... Ecco: ricaricarle tutte ti costa "'
         ' + calccostreload(CHARA_PLAYER) + " monete d\'oro."'),
    (23324, 'Alright.'): 'Procedi',
    (23326, 'Another time.'): 'Annulla',

    # --- 62: togliere le maledizioni
    (23473, 'Curses removed. Take care!'): 'Maledizioni tolte. Riguardati!',

    # --- 63: rinforzare l'equipaggiamento
    (23687, "I can't enhance it anymore."): 'Non si può rinforzare oltre.',
    (23692, 'Enhance equipment.'): 'Rinforzare',
    (23695, 'It will cost you  gold.'): '"Ti costa " + wcost + " monete d\'oro."',
    (23702, '  surrounded by a golden aura.'): 'itemname(ci) + " si avvolge in un\'aura dorata."',
    (23706, 'Enhancement done!'): 'Rinforzo completato!',

    # --- 115: i tappi di pozione
    (23719, "I don't have anymore of these left now."): 'Non me ne restano più.',
    (23722, "I don't know what you're going to use it for...Bring what I was supposed to dispose of."):
        'Non so che cosa te ne farai... ma se è roba da buttare, prendila pure.',
    (23727, ' get  potion plug. [Remaining plug ]'):
        ('name(0) + " ottiene " + plug + " tappi di pozione. [Tappi rimasti: "'
         ' + gdata(GDATA_FLAG_TOTAL_POTION_PLUGS) + "]"'),

    # --- 64: alleggerire
    (23739, 'It is sort of impossible at this stage.'): 'Con questo non ci posso fare niente.',
    (23744, 'Make equipment 0.1s lighter.'): 'Alleggerire di 0.1s',
    (23747, 'Make equipment 1.0s lighter.'): 'Alleggerire di 1.0s',
    (23750, 'You will cost gp per 0.1s.'): '"Ci vogliono " + wcost + " monete d\'oro ogni 0.1s. Va bene?"',
    (23757, ' becomes lighter.'): 'itemname(ci) + " perde peso."',
    (23764, 'Weight reduction completed!'): 'Alleggerimento completato!',

    # --- 95: appesantire
    (23803, 'Make equipment 0.1s heavier.'): 'Appesantire di 0.1s',
    (23806, 'Make equipment 1.0s heavier.'): 'Appesantire di 1.0s',
    (23809, 'It will cost you gp per 0.1s.'): '"Ci vogliono " + wcost + " monete d\'oro ogni 0.1s. Va bene?"',
    (23816, ' becomes heavier.'): 'itemname(ci) + " prende peso."',
    (23820, 'Weighting completed!'): 'Appesantimento completato!',
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
