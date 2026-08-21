# -*- coding: utf-8 -*-
"""77a — `chat.hsp`, le due arene: il duello, la rissa e l'arena delle bestie.

`chatval` 21/22 (`:20579`, «In arena [Duello]» e «[Rissa]»), 40/41/49
(`:20699`, «Duello fra animali», «Battaglia a squadre», «Battaglia EX») e i due
`chatval` gemelli del punteggio, 23 e 42 (`:20799`, `:20795`), che dicono la
stessa frase con due contatori diversi. Tutte voci di menu gia' rese dalla 73a:
il giocatore clicca italiano e riceve inglese.

⭐ **Il parlante e' uno solo per arena e ha gia' un nome nel gioco**: «il padrone
dell'arena» (`db_creature.hsp`, `text.hsp:885`) e «l'organizzatore dell'arena
delle bestie» (`:118259`). Registro da imbonitore, «tu» al giocatore.

⚠️⚠️ **Il saluto al campione porta il genere del GIOCATORE, in tutt'e tre le
righe.** 「ようこそアリーナのチャンピオン！」 e 「ようこそペットの王！」 sono
vocativi: «benvenuto», «campione», «re» si accordano tutti. La via d'uscita e' la
**relativa senza nome**, che non accorda — «Ecco chi regna nell'arena!» — ed e'
la regola (1) della 75a in una forma nuova: invece del nome predicativo, il
verbo alla terza persona.

⚠️⚠️ **E il genere morde una seconda volta su un TERZO**, `:20758`: chi ha
montato la squadra EX e' un avventuriero estratto a caso e il suo nome sta
stampato nella stessa frase, quindi «un avventuriero di nome Marka» sbaglia meta'
delle volte. Reso con «un'altra persona in cerca d'avventura», che tiene il
mestiere e non accorda. E' la 70a (il genere di chi PARLA) spostata a chi non
parla affatto.

⚠️ **«pet» qui e' «animale», non «bestia»**: le tre voci del menu che portano a
questi blocchi dicono gia' «Duello fra animali» (`:19611`) e «Battaglia a
squadre» (`:19612`). «Arena delle bestie» resta solo dov'e' il **nome della
mappa** (`init.hsp:356`, `map.hsp:5478`).

⚠️ **La coppia si SCIOGLIE**: `:20593` e' la stessa frase di `map_user.hsp:878` e
`proc.hsp:10793`, gia' rese «Prima devi sciogliere la coppia.» — qui pero' e' la
mancanza di spazio, quindi «Non c'e' spazio per sciogliere la coppia.», sulla
falsariga di `:20583` che sta sei righe sopra («Non c'e' spazio per scendere.»).

💡 `:20604` e `:20721` sono la **stessa frase con due firme**: monte scrive
«tomorrow» in un ramo e «tommorow» nell'altro. Stessa resa.

💡 `:19614` («I miei risultati» del menu delle bestie) sembra non tradotta a
`chatval-mappa.py`, che legge il dizionario per RIGA: ha la stessa firma di
`:19608` ed e' gia' italiana in build.

    python scratchpad/lotto-77-chat-arena.py
"""
import io
import json
import sys

USCITA = 'lavoro/77-chat-arena.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((20579, 20698), (20699, 20794), (20795, 20798), (20799, 20802))

# la coda del contatore dei tentativi, identica nelle due righe delle bestie
TENTATIVI = (' + (petArenaMatchLimit - adata(ADATA_ARENA_MATCHES_FOUGHT,'
             ' gdata(GDATA_AREA))) + " tentativi."')

RESE = {
    # --- 21/22: l'arena dei duelli e delle risse
    (20593, "There's not enough space to dissolve the tag-team."):
        "Non c'è spazio per sciogliere la coppia.",
    (20604, 'The game is over today. Come again tomorrow.'):
        'Per oggi i combattimenti sono finiti. Torna domani.',
    (20654, 'Welcome! A challenger has come to fight with you!'):
        "Ecco chi regna nell'arena! Oggi hai un altro sfidante!",
    (20656, "You got someone around level  today. What'ya say?"):
        '"Oggi l\'avversario è di livello " + aitelv + ". Te la senti?"',
    (20668, 'Welcome! Challengers have come to fight with you!'):
        "Ecco chi regna nell'arena! Oggi hai altri sfidanti!",
    (20670, 'Your play is a group of monster around level . Sounds easy huh?'):
        ('"Stavolta affronti un gruppo di mostri di livello " + arenaop(1)'
         ' + ". Facile, no?"'),
    (20672, 'Alright.'): 'Accetto la sfida',
    (20673, "I'll pass."): 'Annulla',
    (20677, 'Alright. Call me if you changed your mind.'):
        'Va bene. Se cambi idea, fammi un fischio.',

    # --- 40/41/49: l'arena delle bestie
    (20721, 'The game is over today. Come again tommorow.'):
        'Per oggi i combattimenti sono finiti. Torna domani.',
    (20729, 'Welcome! A challenger has come to fight with your pet!'):
        "Ecco chi regna qui! Oggi sfidano il tuo animale!",
    (20731, 'The opponent is around level . Want to give it a try? You have  attempts left today.'):
        ('"L\'avversario è di livello " + arenaop(2) + ". Vuoi provare?'
         ' Oggi ti restano "' + TENTATIVI),
    (20751, "It's a  vs  match. The opponent's group is formed by the pets less than  levels. What do you say? You have  attempts left today."):
        ('"Si combatte " + arenaop(1) + " contro " + arenaop(1) + ". Gli avversari'
         ' sono animali sotto il livello " + arenaop(2) + ". Che ne dici?'
         ' Oggi ti restano "' + TENTATIVI),
    (20758, "That team was put together by an adventurer by the name of . This will be a v match. The opponent's group is formed by pets with an average level of . What do you say?"):
        ('"Quella squadra l\'ha messa insieme un\'altra persona in cerca'
         ' d\'avventura, " + locvar_arena_creator + ". Si combatte " + arenaop(1)'
         ' + " contro " + arenaop(1) + ", e gli animali avversari hanno livello'
         ' medio " + arenaop(2) + ". Che ne dici?"'),
    (20760, "I'll send my pet."): 'Mando il mio animale',

    # --- 42 e 23: il punteggio, due contatori per la stessa frase
    (20796, 'Your winning record has reached  matchs now. Keep the audience excited. You get nice bonus at every 3th,5th,10th,20th,30th,50th,100th wins in a row.'):
        ('"Al momento sei a " + adata(ADATA_PET_ARENA_WIN, gdata(GDATA_AREA))'
         ' + " vittorie. Tieni il pubblico col fiato sospeso: c\'è un bel premio'
         ' ogni 3, 5, 10, 20, 30, 50 e 100 vittorie di fila."'),
    (20800, 'Your winning record has reached  matchs now. Keep the audience excited. You get nice bonus at every 3th,5th,10th,20th,30th,50th,100th wins in a row.'):
        ('"Al momento sei a " + adata(ADATA_ARENA_WIN, gdata(GDATA_AREA))'
         ' + " vittorie. Tieni il pubblico col fiato sospeso: c\'è un bel premio'
         ' ogni 3, 5, 10, 20, 30, 50 e 100 vittorie di fila."'),
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
