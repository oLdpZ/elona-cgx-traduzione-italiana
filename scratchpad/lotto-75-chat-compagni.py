# -*- coding: utf-8 -*-
"""75a — `chat.hsp`, i comandi ai compagni: prezioso, oggetti, congedo, richiamo.

`chatval` 94 (istruzioni speciali), 33 (richiamare un compagno dalla stalla),
67 e 68 (segnare o togliere «prezioso»), 71 e 72 (raccogliere o no gli oggetti),
35 (abbandonare), 44 (licenziare), 48 (far tacere).

⭐⭐ **Due righe hanno il gemello in un ALTRO file, e vanno dette con le stesse
parole.** `command.hsp:6703` e `:6707` sono gli stessi due messaggi degli ordini
sugli oggetti, gia' resi: «`name` ha l'ordine di non raccogliere gli oggetti per
terra» e «`name` puo' fare come vuole con gli oggetti per terra». Il dizionario
e' **per file**, quindi la firma non li unisce: se non si va a cercarli, la
stessa frase esce in due modi. (E' la ragione per cui esiste `gemelle`.)

⚠️ **`his(tc)` e `him(tc)` SENZA secondo argomento sono morfologia inglese e si
tolgono**: `init.hsp:1956` mette la `lang()` solo nel ramo `his_arg2`, e senza
argomento restituisce `its`/`your`/`his`/`her` nudi. Solo `his(x, 1)` e'
contenuto. Cosi' «puffs out his chest» e' «gonfia il petto».

⚠️ **La preposizione davanti a `name()`** (`guida-stile.md:275`): «Hai dato
istruzioni **a** X» stamperebbe «a il putit». Il progetto ha gia' la via
d'uscita a `action.hsp:11810` — «Hai **istruito** X», col personaggio a
complemento oggetto — e `:20312` la riusa.

⚠️ **E dove l'inglese usa un pronome oggetto, l'italiano RIPETE IL NOME** (la
regola dei sogni, 74a): «Really abandon `him(tc)`?» non puo' diventare
«abbandonarlo», che sarebbe accordato sul genere del compagno; diventa
«abbandonare `name(tc)`?».

⚠️ Le espressioni del volto girano sul **nome**, non sull'aggettivo: «ha l'aria
abbattuta», «ha l'aria spaventata», «fa una faccia sorpresa» — l'accordo cade su
«aria» e «faccia», che sono nostre, non sul compagno, che non si conosce.
«sembra sovrappensiero» e' invariabile.

    python scratchpad/lotto-75-chat-compagni.py
"""
import io
import json
import sys

USCITA = 'lavoro/75-chat-compagni.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((20295, 20316), (20941, 20991), (21980, 22060), (22480, 22496), (23188, 23200))

RESE = {
    # --- 94: le istruzioni speciali
    (20308, 'What kind of instructions should I give...?'): 'Che istruzioni dare...?',
    (20312, 'You instructed .'): '"Hai istruito " + cdatan(CDATAN_NAME, tc) + "."',

    # --- 33: richiamare un compagno dalla stalla
    (20947, "Huh? You don't need to do that."): 'Eh? Non ce n\'è bisogno.',
    (20955, 'It can not be revived until you switch area.'):
        'Non si può richiamare finché non cambi zona.',
    (20965, 'Alright. We took good care of your pet. It will cost you  gold pieces.'):
        ('"D\'accordo. Ci siamo presi cura del tuo animale. Ti costa "'
         ' + calcresurrectvalue(rc) + " monete d\'oro."'),
    (20967, "I'll pay."): 'Richiamare',
    (20969, 'Never mind.'): 'Annulla',
    (20975, '( brings  from the stable.) There you go.'):
        '"(" + name(tc) + " porta " + name(rc) + " dalla stalla.) Ecco fatto."',

    # --- 67: segnare come prezioso
    (21982, '( puffs out  chest with pride.)'):
        '"(" + name(tc) + " gonfia il petto con orgoglio.)"',
    (21985, '( looks a little embarrassed.)'):
        '"(" + name(tc) + " sembra un po\' in imbarazzo.)"',
    (21988, '( looks surprised.)'):
        '"(" + name(tc) + " fa una faccia sorpresa.)"',
    (21991, '( clicks  tongue disapprovingly.)'):
        '"(" + name(tc) + " schiocca la lingua in segno di disapprovazione.)"',

    # --- 68: togliere «prezioso»
    (21998, '( looks depressed...)'): '"(" + name(tc) + " ha l\'aria abbattuta...)"',
    (22001, '( appears to be lost in thought...)'): '"(" + name(tc) + " sembra sovrappensiero...)"',
    (22004, '( looks scared...)'): '"(" + name(tc) + " ha l\'aria spaventata...)"',
    (22007, '( spits on the ground.)'): '"(" + name(tc) + " sputa per terra.)"',

    # --- 71, 72: gli oggetti per terra (gemelli di command.hsp:6703 e :6707)
    (22013, '(You instructed  to not pick up items off the ground.)'):
        '"(" + name(tc) + " ha l\'ordine di non raccogliere gli oggetti per terra.)"',
    (22018, '(You instructed  to do as they like with items on the ground.)'):
        '"(" + name(tc) + " può fare come vuole con gli oggetti per terra.)"',

    # --- 35: abbandonare un compagno
    (22024, '( looks at you with a sad expression. Really abandon ? )'):
        '"(" + name(tc) + " ti guarda con aria triste. Vuoi davvero abbandonare " + name(tc) + "? )"',
    (22025, 'Yes.'): 'Sì',
    (22026, 'No.'): 'No',
    (22030, 'You abandoned ...'): '"Hai abbandonato " + name(tc) + "..."',

    # --- 44: licenziare
    (22482, '( looks at you with a sad expression. Really dismiss ? )'):
        '"(" + name(tc) + " ti guarda con aria triste. Vuoi davvero licenziare " + name(tc) + "? )"',
    (22488, 'You dismiss .'): '"Hai licenziato " + name(tc) + "."',

    # --- 48: far tacere
    (23191, ' stops talking...'): 'name(tc) + " smette di parlare..."',
    (23194, ' hugs you.'): 'name(tc) + " ti abbraccia."',
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
