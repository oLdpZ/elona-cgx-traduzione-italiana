# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, i servizi che si pagano: identificare, curare, viaggiare.

Sette `chatval` piccoli, tutti dietro una voce di menu gia' resa dalla 73a:
14-16 (l'identificazione, `:20457`), 19 (il ripristino degli attributi,
`:20536`), 20 (lo scambio, `:20562`), 43 (il rifugio, `:22459`), 53 (il
servizio di ritorno, `:23300`), 75 (la lezione di magia, `:24093`) e 99 (la
rottamazione del veicolo, `:24196`).

⚠️ **`:20514` non puo' dire «studiarlo»**: il pronome porterebbe il genere
dell'oggetto, che non si sa. «Serve un'indagine piu' accurata» non si accorda
con niente — regola (3) della 75a.

⚠️ **`:20576` e' la firma di TUTTI i «Thanks!» del file** (`_thanks(2)`): la
riga rappresentante e' questa, e la resa vale anche per `:22385`, `:23237`,
`:23293` e gli altri. E' l'altra faccia della lezione della 76a: qui la firma
condivisa fa lavorare **una resa per dieci siti**, invece di rompere un menu.

💡 **«world-vehicle» e' «il veicolo»**, come in `map.hsp:1045` («Scendi dal
veicolo»); i quattro veicoli veri hanno gia' il loro nome in `db_item.hsp`
(carrozza, locomotiva magica, corazzata terrestre).

⚠️⚠️ **E il «Cancel.» di `:24147` si e' tirato dietro due menu.** La firma di
「いいよ」/«Sure.» ha la rappresentante a `:8197` e vive anche a `:8736`: chiudere
la coppia della lezione di magia lasciava a meta' il menu della **lettera di
Siraha** e quello della **tartaruga della principessa** (che il lotto del dojo
aveva gia' toccato). Tre rese in piu' e si chiudono tutt'e due. E' la terza
volta in questa sessione: la firma condivisa e' la regola, non l'eccezione.

⚠️ 「だめ」 resta **«No»** come a `:2631`, e 「やめておく」 resta «Lascio stare»
come a `:3032`: stessa parola giapponese, stessa resa, anche dove monte scrive
due inglesi diversi («Cancel.» e «I'll stop it.»).

    python scratchpad/lotto-77-chat-servizi.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-servizi.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((8197, 8198), (8737, 8737), (20457, 20520), (20536, 20578),
        (22459, 22479), (23300, 23304), (24093, 24195), (24196, 24229))

RESE = {
    # --- i due menu che la firma di 「いいよ」 si e' tirata dietro
    (8197, 'Sure.'): 'Va bene',
    (8198, 'Not a chance.'): 'Non se ne parla',
    (8737, 'No way.'): 'Non mi va',

    # --- 14-16: l'identificazione
    (20473, 'Your items have already been identified.'):
        'Non mi pare che tu abbia oggetti da identificare.',
    (20494, ' out of  unknown items are fully identified.'):
        ('"Su " + p(1) + " oggetti sconosciuti, " + p + " sono ora identificati'
         ' del tutto."'),
    (20495, 'Here, I have finished identifying your stuff.'):
        'Ecco qua, ho finito di identificare la tua roba.',
    (20514, 'You need to investigate it to gain more knowledge.'):
        "Per saperne di più serve un'indagine più accurata.",

    # --- 19 e 20: la cura e lo scambio
    (20559, 'Treatment done. Take care!'): 'Cura completata. Riguardati!',
    (20576, 'Thanks!'): 'Grazie!',

    # --- 43 e 53: il rifugio e il ritorno
    (22466, 'The shelter is free to use for anyone. Here, come in.'):
        'Il rifugio è gratis e aperto a tutti. Vieni, al riparo!',
    (23301, "I'm practicing a spell of return. Would you like to take my service?"):
        ('Mi sto esercitando con la magia del ritorno. Vuoi che la usi anche '
         'per te?'),

    # --- 75: la lezione di magia
    (24147, 'Cancel.'): 'No',
    (24148, 'This practice will cost you  platinum pieces.'):
        '"La lezione ti costa " + plat + " monete di platino, va bene?"',
    (24189, 'The practice is now complete.'): 'La lezione è finita.',

    # --- 99: rottamare il veicolo
    (24198, 'You do not have a world-vehicle.'):
        'Non mi pare che tu abbia un veicolo da rottamare.',
    (24202, "I'll stop it."): 'Lascio stare',
    (24203, "I don't need the vehicle."): 'Non mi serve più',
    (24204, 'Do you return to walk discard your world-vehicle?'):
        'Vuoi rottamare il veicolo e tornare ad andare a piedi?',
    (24222, 'understood. I will handle.'):
        "D'accordo, alle pratiche ci penso io.",
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
