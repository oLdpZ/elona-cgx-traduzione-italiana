# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, il rito del lupo mannaro: l'accusa e l'indagine.

`chatval` 69 («Sei un lupo mannaro?», `:19744`) e 70 («Indagine sul passato»,
`:19735`), tutt'e due voci di menu gia' rese dalla 73a.

⭐ **Le sette risposte di `:69` sono i sette `CDATA_TONE`**, cioe' sette modi di
parlare dello stesso cittadino, non sette personaggi: il registro cambia, il
contenuto no. E il primo ramo (`:23870`) e' il **detective**, che si riconosce
dall'ID e non dal tono.

⚠️⚠️ **Il sesso del parlante non si sa mai** (e' un cittadino estratto a caso),
quindi nessun participio riferito a chi parla. `:23889` diceva «se hai le prove
che vada giustiziato» — accordato — ed e' diventato «per mandarmi al
patibolo»; `:23892` regge perche' il passato prossimo e' con **avere**, che non
accorda («non avevo mai visto»). E' la regola (2) della 75a, il PARLANTE.

⚠️ **`:23911` e le due dell'indagine girano attorno alla preposizione.**
`cdatan(CDATAN_NAME, ...)` non e' garantito nudo, e «sospettare **di** X»
stamperebbe «di il cittadino»: la resa fa del nome un **complemento oggetto**
(«Tutti guardano X con sospetto») o un **soggetto** («X e' un essere umano in
tutto e per tutto»). E' `guida-stile.md:275`.

⭐ **«kitsune» non si lascia in giapponese: e' una creatura che il giocatore ha
gia' visto chiamare in un altro modo.** `CREATURE_ID_FOX_SPIRIT` e' «la volpe
ammaliatrice» in `db_creature.hsp`, `db_card.hsp`, `ai.hsp` ed `event.hsp:601`.
E' la regola della 74a: una voce che nomina una cosa dice il nome che quella
cosa ha nel gioco.

⚠️ **`:23895` e' quasi gemella di `chat.hsp:22112` e `text.hsp:127`**: stesso
giapponese 「さようなら」, inglese diverso («Bye.» contro «Bye bye.»), gia' reso
«Arrivederci». Stesse parole, senza il punto perche' e' una voce di menu.

💡 Le due `lang()` che restano nel blocco non sono qui perche' hanno gia' la
loro resa: 「…。」 a `:23883` e la riga dell'autorita' a `:23907`, che ha la
firma di `:7032` («Autorita': N -> M»).

    python scratchpad/lotto-76-chat-lupo.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-lupo.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((23868, 23919), (24540, 24589))

RESE = {
    # --- 69: «Sei un lupo mannaro?» — il detective, poi i sette toni
    (23870, "That's an interesting deduction. I recommend you to become a novelist."):
        'Una deduzione interessante. Ti consiglio di darti alla narrativa.',
    (23874, "Ridiculous. There's no way there'd be a werewolf here. Think about it, they're quite rare."):
        'Ridicolo. Non è possibile che qui ci sia un lupo mannaro. Pensaci: sono piuttosto rari.',
    (23877, "I-I'm not! I'm not a werewolf! Please believe me!"):
        'N-non è vero! Io non sono un lupo mannaro! Devi credermi!',
    (23880, "You can only execute one person a day. If you don't want to be wasteful, you should consider all the possibilities."):
        ('Si può giustiziare una persona sola al giorno. Se non vuoi sprecare '
         "l'occasione, valuta bene tutte le possibilità."),
    (23886, "Why even bother asking? Even if I say no, you're still going to be suspicious of me."):
        'Perché me lo chiedi? Anche se ti dico di no, continuerai a sospettare di me.',
    (23889, 'If you have evidence saying I should be executed then do something already.'):
        'Se hai le prove per mandarmi al patibolo, allora muoviti.',
    (23892, "Come to think of it, there is someone I haven't seen before. But maybe it's a kitsune instead of a werewolf?"):
        # ⚠️ accorciata: la prima stesura faceva 3 righe contro le 2 dell'inglese
        ('A pensarci bene, c\'era una faccia mai vista prima. Ma forse '
         'è una volpe ammaliatrice, non un lupo mannaro?'),
    (23895, 'Bye.'): 'Arrivederci',
    (23899, 'This person is a werewolf!'): 'Questa persona è un lupo mannaro!',
    (23911, ' was suspected around.'):
        '"Tutti guardano " + cdatan(CDATAN_NAME, tc) + " con sospetto."',

    # --- 70: l'indagine sul passato
    (24570, "From what we've gathered from our investigation,  is most definitely a genuine human."):
        ('"Da quel che abbiamo raccolto con le indagini, "'
         ' + cdatan(CDATAN_NAME, cdata(CDATA_ROLE_SHOP_LEVEL, tc))'
         ' + " è un essere umano in tutto e per tutto."'),
    (24575, "From what we've gathered from our investigation,  is a monster disguising itself as a human."):
        ('"Da quel che abbiamo raccolto con le indagini, "'
         ' + cdatan(CDATAN_NAME, cdata(CDATA_ROLE_SHOP_LEVEL, tc))'
         ' + " è un mostro travestito da essere umano."'),
    (24585, "We're not presently investigating anyone."):
        'Al momento non stiamo indagando su nessuno.',
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
