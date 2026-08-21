# -*- coding: utf-8 -*-
"""76a — `chat.hsp`, «Dove si trova X?» e, per forza, la conversione a Jure.

Due famiglie in un lotto solo, e la ragione e' una **firma condivisa**.

La prima e' `chatval >= 10000` (`:24590`-`:24677`), la risposta alla voce «Dove
si trova " + nome + "?» (`:19650`, resa dalla 73a): il PNG dice in che direzione
cercare, e poi si offre di accompagnarti. La finestra si compone **in due
pezzi** — `s` prende la frase della distanza e a `:24650` ci si somma l'offerta,
che infatti in inglese comincia con uno **spazio**: e' la giuntura, e va tenuta.

⚠️⚠️ **E il menu dell'offerta ha tirato dentro una scena che sta a diciottomila
righe di distanza.** Il «No.» di `:24653` ha la stessa firma del «No.» di
`:6277`, cioe' e' **una sola voce di dizionario**: tradurre l'una traduce
l'altra. Ma `:6277` sta nel menu di conferma del **venditore porta a porta di
Jure** a Noyel, che era tutto inglese: tradurre solo il «No.» avrebbe lasciato
quella finestra meta' e meta'. Quindi la scena di Jure (`:6261`-`:6293`) entra
in questo lotto **intera**, nove rese. E' la regola della 73a — un menu si
traduce intero — nella forma nuova in cui a scoprirlo non e' `annota_menu` ma la
firma condivisa fra due punti lontani del file.

⭐ **Le quattro direzioni sono nude** («ovest», «est», «nord», «sud»): entrano
dentro `s` e la preposizione la mettono le frasi che le ospitano, come in
inglese. Nel dizionario non ce n'erano ancora.

⚠️ **Nessuna delle cinque frasi puo' mettere una preposizione davanti al nome**
(`guida-stile.md:275`): «accompagnare **a** X» stamperebbe «a il cittadino».
Le rese fanno del nome un complemento oggetto — «troverai X», «Se vuoi
incontrare X», «Vuoi che ti accompagni a cercare X?».

⚠️ **`:24617` non puo' dire «e' morto»**: il cercato e' un PNG qualunque e il
participio si accorderebbe. «non e' piu' di questo mondo» non accorda niente.

⚠️ **`:6272` non puo' dire «diventa un fratello di Jure»** («Be a brother of
Jure today»): e' il giocatore, e il nome predicativo maschile sarebbe sbagliato
meta' delle volte. La resa gira su «Convertiti oggi». E il premio si chiama col
nome che ha nello zaino — «cuscino di Jure» (`db_item.hsp:142043`) — con le
parole che il fanatico di Jure usa gia' in `db_creature.hsp:103116`, «formato
abbraccio, in omaggio».

    python scratchpad/lotto-76-chat-indicazioni.py
"""
import io
import json
import sys

USCITA = 'lavoro/76-chat-indicazioni.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((6261, 6293), (24590, 24660))

RESE = {
    # --- il venditore di Jure a Noyel (tirato dentro dalla firma di «No.»)
    (6267, 'Ah, you already believe in Jure right? Sorry bro, but we are only looking for new converts.'):
        'Ah, ma tu sei già credente, no? Mi spiace, accettiamo solo nuove conversioni.',
    (6270, 'I will become a faithful servant of Jure.'): 'Convertirsi a Jure',
    (6271, 'Not interested.'): 'Non mi interessa',
    (6272, "We are running a special campaign to help you join our religion! Be a brother of Jure today and win free body pillow of Jure! During the festival, you won't have to pay penalty to convert your religion neither. So what are you waiting? Sign up now!"):
        ('Il culto di Jure ha in corso una campagna per chi cambia dio! Convertiti oggi e '
         'ti porti a casa il cuscino di Jure formato abbraccio, in omaggio! E durante il '
         'festival la conversione non costa nessuna penitenza. Che aspetti? Firma qui!'),
    (6276, 'Yes.'): 'Sì',
    (6277, 'No.'): 'No',
    (6278, 'Okie, just making sure. Do you really want to convert your religion?'):
        'Va bene, giusto per essere sicuri: vuoi davvero cambiare religione?',
    (6282, 'Thanks, bro! I finally filled my daily quota.'):
        'Grazie mille! Finalmente ho raggiunto la quota di oggi.',
    (6291, 'Shit!'): 'Merda!',

    # --- le quattro direzioni, nude
    (24595, 'west'): 'ovest',
    (24599, 'east'): 'est',
    (24603, 'north'): 'nord',
    (24606, 'south'): 'sud',

    # --- le cinque risposte, per distanza crescente
    (24617, 'Oh forget it, dead for now.'): "Lascia perdere, non è più di questo mondo.",
    (24621, 'Oh look carefully before asking, just turn .'):
        '"Ma guardati intorno prima di chiedere: gira verso " + s + "."',
    (24625, 'I saw  just a minute ago. Try .'):
        '"Ho visto " + cdatan(CDATAN_NAME, rc) + " poco fa. Prova verso " + s + "."',
    (24629, "Walk to  for a while, you'll find ."):
        '"Cammina un po\' verso " + s + " e troverai " + cdatan(CDATAN_NAME, rc) + "."',
    (24633, 'If you want to meet , you have to considerably walk to .'):
        ('"Se vuoi incontrare " + cdatan(CDATAN_NAME, rc)'
         ' + ", devi camminare parecchio verso " + s + "."'),
    (24636, 'You need to walk long way to  to meet .'):
        ('"Per incontrare " + cdatan(CDATAN_NAME, rc)'
         ' + " devi fare parecchia strada verso " + s + "."'),

    # --- l'offerta che si somma alla frase di sopra: lo spazio davanti e' la giuntura
    (24650, ' May I guide you to ?'):
        '" Vuoi che ti accompagni a cercare " + cdatan(0, rc) + "?"',
    (24652, 'Please.'): 'Sì, grazie',
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
