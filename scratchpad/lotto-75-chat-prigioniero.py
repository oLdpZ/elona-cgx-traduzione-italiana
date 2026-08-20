# -*- coding: utf-8 -*-
"""75a — `chat.hsp`, il prigioniero: le minacce, il rilascio, l'esecuzione.

Un nemico catturato e appeso al sacco da botte apre un menu tutto suo, gia'
italiano dalla 73a, e ogni voce portava a una risposta inglese. Dieci blocchi:
`chatval` 149 (dargli da mangiare), 150, 151, 144, 145, 146, 147, 148 (le
minacce) e 133, 134 (liberarlo o giustiziarlo).

⚠️⚠️ **Il genere e' vietato tre volte**: il prigioniero e' un PNG qualunque, il
giocatore pure, e le battute parlano dell'uno all'altro. «D'ora in poi sei
libero» sarebbe accordato sul prigioniero -> «sei in liberta'»; «Sono libero!»
-> «Liberta'!»; «Che sfigato!» -> «Schiappa!», che e' un nome femminile e vale
per chiunque.

⚠️⚠️ **E due righe cadevano nella trappola della preposizione**
(`guida-stile.md:275`): `name()` si porta l'articolo, quindi «mozza la testa **a**
`name(tc)`» stampa «a il putit». Le due decapitazioni (`:20244` e `:22124`)
diventano «`name` **decapita** `name`», col personaggio a complemento oggetto —
che e' la via d'uscita che la guida indica per prima.

⚠️ `your(x)` e' morfologia inglese e **si toglie**: `init.hsp:2045` non ha
nessuna `lang()` dentro, restituisce `'s` oppure `r`. Sta accanto a `_s()` e
`is()`, non accanto a `his(x, 1)`.

⚠️ `:22124` e' un **frammento che il codice salda**: finisce con «and» e la
riga dopo e' il messaggio di morte prodotto da `dmghp`. L'italiano finisce con
«e», come monte.

⭐ Le parole vengono da dove il giocatore le ha gia' viste: `sandbag` e' «sacco
da botte» (`glossario.md:361`), e `*Gash*` e' «*spruzz*» come a
`proc.hsp:12280`, che ha lo stesso giapponese ブシュッ.

    python scratchpad/lotto-75-chat-prigioniero.py
"""
import io
import json
import sys

USCITA = 'lavoro/75-chat-prigioniero.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((20096, 20294), (22062, 22144))

RESE = {
    # --- 149: dare da mangiare al prigioniero
    (20107, 'It smells suspicious...'): 'Ha un odore sospetto...',
    (20110, 'It looks a little delicious...'): 'A dire il vero sembra quasi buono...',
    (20113, "I guess just a little bit won't hurt..."): 'In fondo un assaggino non fa male...',
    (20117, "It's not so bad being fed by you..."): 'Non è male farsi imboccare da te...',

    # --- 150: lo sberleffo
    (20127, 'You insulted  while jumping up and down at high speed.'):
        '"Hai insultato " + cdatan(CDATAN_NAME, tc) + " saltando su e giù a gran velocità."',
    (20144, 'Zaaaaako!'): 'Schiaaappa! Schiaaappa!',
    (20147, 'I wiiiiiin!'): 'E ho viiiinto!',
    (20150, 'Weeeeeee!'): 'Uheeeeeh!',
    (20152, 'People around you look at you with disgust. You should probably stop doing that...'):
        'Quelli intorno a te ti guardano con disgusto. Forse è meglio smetterla...',

    # --- 151: ordinargli di uccidere i suoi
    (20192, "It's hard to keep an eye on this prisoner of war, since you have so many allies..."):
        'Con tutti questi compagni è difficile tenere d\'occhio anche un prigioniero di guerra...',
    (20198, "I-I can't do that, but please forgive me..."): 'N-non posso farlo, ti prego, perdonami...',
    (20200, " doesn't seem to understand own current position."):
        'cdatan(CDATAN_NAME, tc) + " non sembra capire la propria situazione."',
    (20204, 'Sorry.. everyone...'): 'Scusatemi... tutti quanti...',

    # --- 144: il riscatto
    (20226, 'Eeeek!'): 'Iiiiih!',
    (20227, ' left gold pieces and ran away.'):
        'cdatan(CDATAN_NAME, tc) + " lascia le monete d\'oro e scappa via."',

    # --- 145, 146: il colpo di grazia
    (20234, 'Ugh...!'): 'Ngh...!',
    (20239, "I don't want to die! Plea..."): 'N-non voglio morire! Ti sup...',
    (20242, '*Gash*'): '*spruzz*',
    (20244, ' cut  head.'): 'name(0) + " decapita " + name(tc) + "."',

    # --- 147, 148: la grazia, vera e finta
    (20270, 'I was spared! Hahaha...!'): 'Mi hanno risparmiato! Ahahah...!',
    (20284, 'I was spared! Hahah...'): 'Mi hanno risparmiato! Ahah...',

    # --- 133: liberare il prigioniero
    (22065, 'You cannot release  when they are hanging on a sandbag.'):
        '"Non puoi liberare " + name(tc) + " finché pende dal sacco da botte."',
    (22068, 'Really?'): 'Davvero?',
    (22069, 'Just kidding~'): 'Scherzavo~',
    # ⚠️ questa voce sta in un menu a DUE COLONNE, tetto 24 (`chat.hsp:25167`
    # taglia con `strmid(..., 0, 24)`), e l'inglese lo tocca esatto: 24. La resa
    # si misura DOPO la degradazione, quindi «liberta'» sono 9 caratteri, non 8.
    (22070, "You're free from now on."): 'Adesso sei in libertà',
    (22076, 'It seems like  can no longer live without obeying someone...'):
        '"Pare che " + cdatan(CDATAN_NAME, tc) + " non sappia più vivere senza obbedire a qualcuno..."',
    (22079, 'Seeing you have a full party,  sigh and went somewhere else...'):
        '"Vedendo che la squadra è al completo, " + cdatan(CDATAN_NAME, tc) + " sospira e se ne va per la sua strada..."',
    (22090, 'Well then, I shall take my revenge on you!'): 'E allora mi vendicherò di te!',
    (22091, ' rebelled!'): 'name(tc) + " si ribella!"',
    (22102, "I'm freeeeeee!"): 'Liiiiibertà!',
    (22103, ' left this camp...'): 'name(tc) + " lascia il campo..."',

    # --- 134: giustiziarlo per dare l'esempio
    (22110, 'Really?!'): 'Davvero?!',
    (22124, ' cut  head and'): 'name(cc) + " decapita " + name(tc) + " e"',
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
            errori.append('%d: voce senza resa | %r' % (v['riga'], v['en'][:70]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %r' % (k[0], k[1][:70]))
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
