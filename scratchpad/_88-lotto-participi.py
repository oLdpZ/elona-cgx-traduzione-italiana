# -*- coding: utf-8 -*-
"""Cinque rese vecchie che il REFERTO trova e nessuna guardia vede.

`python scratchpad/referti.py` gira su tutto il dizionario e all'apertura della
88a segnalava **14 participi** dove la 86a ne contava 6. Lette una per una:
**otto sono falsi positivi legittimi** e **quattro sono difetti veri** — tre
scritti nella 87a, nel seminario, e **uno che stava li' dalla 82a** (`0a05f2b`)
e che sei referti di fila non avevano letto fino in fondo. Piu' una
segnalazione che participio non e' ma che nasconde un difetto di lessico.

⚠️⚠️⚠️ **Il quinto e' la lezione piu' scomoda**: `:16586` era gia' nella lista
della 86a, e li' e' stato messo fra i falsi positivi perche' **la stessa riga
contiene un modo di dire** — «se le fallisci la paghi cara». Il referto pero'
non segnalava quello: segnalava «sei ricercato», dodici parole dopo. 💡 Un
referto si legge sulla PAROLA che segnala, non sulla riga.

⚠️⚠️ **La 87a non ha rilanciato `referti.py` in chiusura.** Le sue 281 rese
sono le uniche del progetto che nessun referto ha riletto, ed e' esattamente il
punto n.1 che la sua stessa ripresa lascia aperto («rileggere TUTTO il
dizionario con le regole di oggi»). Lo strumento c'era gia'.

GLI OTTO FALSI POSITIVI, per non ricontrollarli la prossima volta:

  `:1417`   «non te la sei data a gambe»  modo di dire, «la» e' fisso
  `:3152`   «dove sei finita, mamma»      rivolto alla madre
  `:6420`   «dove sei finito?»            rivolto a Eurypides (`:6418`)
  `:9498`   «finalmente libero»           Norne che parla di se' (CDATA_SEX 0)
  `:12657`  «sei cambiato» / «malato»     Belphat che parla a Kuroya
  `:12658`  «sono invecchiato»            Kuroya che parla di se' e a Belphat
  `:22872`  «te la sei cavata»            modo di dire

⭐ Sette righe su otto sono **il genere di qualcun altro**, e il codice lo dice:
`findchara(...)` a `:12657`-`:12658`, il blocco della creatura a `:9498`, il
menu a `:6418`. La regola della 63a ha una sola faccia — non ci si accorda con
un genere che non si conosce — e qui si conosce.

I QUATTRO DIFETTI VERI, e uno in piu'

1. **`:14435`** — «le pergamene non si leggono se sei **cieco** [...] riescono
   male se sei **confuso**»: due participi che accordano col giocatore, in una
   riga del tutorial. ⭐ E la resa giusta non e' solo quella che non accorda:
   il giapponese scrive 「盲目の時」 e 「混乱の時」, cioe' i **nomi degli stati**
   — `_conblind` e `_conconfuse` (`text.hsp:96` e `:99`), che in italiano sono
   **Cecita'** e **Confusione**. Il tutorial copia i nomi dell'interfaccia
   (87a), e qui il giapponese lo dice esplicitamente. Un difetto solo, due
   ragioni per la stessa correzione.

2. **`:14448`** — «i nemici che **sei riuscito** ad abbattere». Il giapponese e'
   「今まで倒せた敵のレベル」: si tiene il passato con `avere`, che col
   participio non accorda col soggetto.

3. **`:14490`** — «...Ci **sei arrivato**?» per 「…あとはわかるかな？」.

3-bis. **`:16586`** (82a) — «sotto il -31 **sei ricercato**». La resa giusta
   non e' un giro di parole: e' la frase che il gioco stesso grida quando una
   guardia ti riconosce, «C'e' una taglia sulla tua testa!»
   (`db_creature.hsp:98449` e `:115178`, per 「お尋ね者だ！」).

4. ⚠️ **`:14113`** — «non andare in un posto pericoloso mentre sei **sotto
   peso**». Participio non ce n'e' (il referto l'ha pescata su «sotto»), ma la
   resa dice **il contrario**: in italiano «sotto peso» vuol dire che se ne
   pesa troppo poco, e l'inglese di monte dice «while burdened», cioe' troppo.
   Lo stato in interfaccia si chiama **Fardello** (`_burden`, `text.hsp:66`) —
   di nuovo il nome che il giocatore legge sullo schermo.

    python scratchpad/_88-lotto-participi.py [uscita.jsonl]
"""
import io
import json
import sys

NUOVE = {
    ('chat.hsp', 14113):
        'E non andare in un posto pericoloso col Fardello addosso. La roba pesante '
        'mettila nello specchio quadridimensionale. Con un buon Sollevamento pesi reggi '
        'di più, ma non perdere di vista il peso dello zaino mentre lo riempi di bottino.',
    ('chat.hsp', 14435):
        'Il teletrasporto è la via più facile, ma si può bloccare. Le pergamene non si '
        'leggono con la Cecità addosso, gli incantesimi non si lanciano sotto silenzio e '
        'riescono male con la Confusione. Con buoni Dispositivi magici le bacchette di '
        'teletrasporto sono affidabili, ma certi posti il teletrasporto lo impediscono e '
        'basta.',
    ('chat.hsp', 14448):
        "E ricordati che il livello dell'ingresso di una Nefia non è il livello "
        'consigliato per andarci. Il livello dei nemici che hai abbattuto finora è '
        'segnato come valutazione di forza nella scheda del personaggio, col tasto c: '
        'prendi quella come metro.',
    ('chat.hsp', 16586):
        'Nelle città si accettano incarichi, ma finché non hai un equipaggiamento '
        'decente lascia perdere quelli di caccia e prendi i più semplici. Le consegne, '
        'per dire, sono facili, ma se le fallisci la paghi cara: occhio alla scadenza. '
        'Ogni crimine ti abbassa il karma, e sotto il -31 ti ritrovi una taglia sulla '
        'testa.',
    ('chat.hsp', 14490):
        'Ti capiterà di trovarti davanti a uno che si cura ogni volta che sta per '
        'cadere. Contro un tipo così serve la Furia, che raddoppia il danno che fai e '
        'quello che prendi. La Furia la dai alla tua squadra con la capacità Furia '
        'collettiva, e la appiccichi al nemico tirandogli un pomodoro. ...Il resto lo '
        'immagini, no?',
}

VECCHIE = {
    ('chat.hsp', 14113): 'sei sotto peso',
    ('chat.hsp', 14435): 'se sei cieco',
    ('chat.hsp', 14448): 'sei riuscito ad abbattere',
    ('chat.hsp', 14490): 'Ci sei arrivato?',
    ('chat.hsp', 16586): 'sotto il -31 sei ricercato',
}


def main() -> int:
    uscita = sys.argv[1] if len(sys.argv) > 1 else 'lavoro/_88-participi.jsonl'
    scelte = []
    for nome in sorted({f for f, _ in NUOVE}):
        for riga in io.open('dizionario/%s.jsonl' % nome, encoding='utf-8'):
            if not riga.strip():
                continue
            v = json.loads(riga)
            chiave = (nome, v['riga'])
            if chiave not in NUOVE:
                continue
            if VECCHIE[chiave] not in (v.get('it') or ''):
                print('%s:%d non dice piu\' %r: %r'
                      % (nome, v['riga'], VECCHIE[chiave], v.get('it')))
                return 1
            v['it'] = NUOVE[chiave]
            scelte.append(v)

    if len(scelte) != len(NUOVE):
        print('trovate %d voci su %d' % (len(scelte), len(NUOVE)))
        return 1

    with io.open(uscita, 'w', encoding='utf-8', newline='\n') as fh:
        for v in scelte:
            fh.write(json.dumps(v, ensure_ascii=False) + '\n')
    print('%d voci in %s' % (len(scelte), uscita))
    return 0


raise SystemExit(main())
