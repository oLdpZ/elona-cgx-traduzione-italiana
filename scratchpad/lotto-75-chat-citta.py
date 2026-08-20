# -*- coding: utf-8 -*-
"""75a — `chat.hsp`, la gestione della citta': Orville, il sindaco, le due leggi.

Il menu di amministrazione esiste **due volte** nel file e i due blocchi sono la
stessa schermata:

  :6965-:7070    l'ufficiale Orville a Vernis, che ti passa la gestione
  :19563 + :22593-:24092   il ramo del sindaco (`chatval` 73, 74, 141)

⚠️ **E i due non sono gemelli per la firma.** `:7014` e' «Law development»,
`:23933` e' «Policy development» — stesso giapponese 法律整備, inglese diverso,
quindi due firme e due rese da scrivere. Sono **quasi gemelle** nel senso della
73a: si leggono, non si travasano, ma devono dire **le stesse parole** perche'
sono la stessa voce di menu.

⭐ **Le parole si prendono dal pannello della citta'** (`economy.hsp:331`-`:365`),
che il giocatore guarda mentre amministra: 運営予算 «Bilancio», 観光収入
«Entrate dal turismo», 支持率 «Gradimento». E 発言力 e' «autorita'», che e' il
glossario (`glossario.md:356`) — vedi la toppa a `economy.hsp:357`.

⚠️ **Tre siti hanno lo stesso inglese e tre giapponesi diversi**: «Sorry, this is
undeveloped.» sta a `:7067` (未実装らしいな «pare non sia implementato»), `:7070`
(開発中だってさ！ «dicono sia in lavorazione») e `:24089` (開発中！). L'inglese
li ha appiattiti; l'italiano li distingue, ed e' una **deroga dichiarata**: qui
l'inglese perde informazione che il giapponese ha.

⚠️ **Le reazioni dei cittadini stanno dentro `cnvtalk(...)`**, che mette le
virgolette da se' (`init.hsp:171`, la lezione della 74a): le rese vanno **nude**.

⚠️ **Genere**: il sindaco di `chat_default` e' generico e il giocatore pure.
«traditore» per il giocatore sarebbe accordato, quindi `:24080` gira la frase:
«Ci hai venduti!» — che per giunta tiene il gioco di parole del giapponese
売町奴 (su 売国奴, «venditore della patria»), che l'inglese ha buttato via.

    python scratchpad/lotto-75-chat-citta.py
"""
import io
import json
import sys

USCITA = 'lavoro/75-chat-citta.jsonl'
RESTANTE = 'scratchpad/chat-restante.jsonl'
ZONE = ((6968, 7070), (22593, 22615), (23920, 24092))

RESE = {
    # ---------------------------------------------------------------- Orville
    (6968, 'Keep up the good work.'): 'Tieni duro',
    (6970, 'I want on behalf of the town management.'): 'Amministrare la città',
    (6973, 'I want to run the town management.'): 'Comandi di gestione',
    (6974, 'How popular is my management?'): 'Quanto sono popolare?',
    (6976, 'Man, the inspection of the underground passage is such a pain. Maybe the bare minimum will be enough.'):
        'Uffa... l\'ispezione del passaggio sotterraneo è una tale rottura. Vabbè, farò il minimo indispensabile.',
    (6998, 'Right now, your popularity is about . If you want keep increase it, you should try your hardest to please everyone!'):
        ('"Al momento il tuo gradimento è più o meno " + imp'
         ' + ". Se vuoi farlo salire, non ti resta che ingraziarti tutti quanti!"'),
    (7002, 'Hum...'): 'Eh eh...',
    (7007, 'By all means, please!'): 'Ma certo, te ne prego!',
    (7016, 'Oh? What sort of management are you going to do?'): 'Oh? Che genere di amministrazione hai in mente?',
    (7022, 'What the policy are you going to do ?'): 'Che politica vuoi attuare?',
    (7026, 'Your authority is insufficient.'): 'Non hai tutta questa autorità.',
    (7032, 'Authority : ->  '): '"Autorità: " + mdata(MDATA_CITY_AUTHORITY) + " -> " + afterau + " "',
    (7039, "We don't have that kind of operating budget."): 'Non abbiamo un bilancio del genere.',
    (7047, 'The mascot has already been placed.'): 'La mascotte è già stata messa.',
    (7056, 'Budget : ->  '): '"Bilancio: " + mdata(MDATA_CITY_BUDGET) + " -> " + afterau + " "',
    (7059, 'Tourism revenue : ->  '): '"Entrate dal turismo: " + mdata(MDATA_CITY_TOURISM_REVENUE) + " -> " + afterau + " "',
    (7067, 'Sorry, this is undeveloped.'): 'Pare che non sia ancora implementato.',
    (7070, 'Sorry, this is undeveloped.'): 'Dicono che sia ancora in lavorazione!',

    # ---------------------------------------------------------------- il sindaco
    (22613, 'Right now, your popularity is . If you do something that makes everyone happy, your popularity will increase, but there will be times when you have to do something even if you are hated...'):
        ('"Al momento il tuo gradimento è " + imp'
         ' + ". Se fai qualcosa che rende tutti contenti sale, ma ci saranno volte in cui dovrai agire anche a costo di farti odiare..."'),
    (23922, 'Please contribute to more town.'): 'Prima contribuisci di più alla città.',
    (23926, 'By all means, please!'): 'Ma certo, te ne prego!',
    (23933, 'Policy development'): 'Emanare leggi',
    (23935, 'What the management are you going to do ?'): 'Che genere di amministrazione hai in mente?',
    (23940, 'Revival of the right to vote(Authority:50) '): 'Voto in più a chi contribuisce (autorità 50) ',
    (23964, 'This town is still under preparation.'): 'In questa città non è ancora pronto.',
    (24008, 'Werewolf Prohibited Zone (Authority:500) '): 'Legge contro i lupi mannari (autorità 500) ',
    (24011, 'Werewolf Conservation Zone (Authority:750) '): 'Legge di convivenza coi lupi mannari (autorità 750) ',
    (24014, 'What the policy are you going to do ?'): 'Che legge vuoi far approvare?',
    (24089, 'Sorry, this is undeveloped.'): 'In lavorazione!',

    # ------------------------------- la legge ANTI lupi: chi la subisce protesta
    (24039, "I feel sorry for the werewolves who haven't killed anyone yet."):
        'Mi fanno pena i lupi mannari che non hanno ancora ucciso nessuno.',
    (24039, "It will make life difficult for werewolves! It's unacceptable discrimination!"):
        'Così la vita dei lupi mannari diventa impossibile! È una discriminazione inaccettabile!',
    (24039, 'Anyone who supports the town manager like this is a complete idiot.'):
        'Chi sostiene un amministratore del genere è un perfetto idiota.',
    (24039, 'This law will upset the werewolves and could lead to war. Repeal it for the sake of friendship.'):
        'Questa legge farà arrabbiare i lupi mannari e può portare alla guerra. Ritiratela, in nome della concordia.',
    (24039, "The conflict is ugly, so we shouldn't resist the werewolves."):
        'Lo scontro è una brutta cosa: non dovremmo opporci ai lupi mannari.',
    (24039, 'Werewolves want peace. Barbaric humans should regain tolerance.'):
        'I lupi mannari vogliono la pace. Gli umani barbari dovrebbero ritrovare la tolleranza.',
    (24039, 'There is no data that suggests that the presence of werewolves increases murder!'):
        'Non esiste nessun dato che dica che con i lupi mannari aumentano gli omicidi!',

    # ------------------------------- la legge ANTI lupi: chi la voleva ringrazia
    (24045, 'I hope I can sleep without being afraid of werewolves.'):
        'Spero di poter dormire senza avere paura dei lupi mannari.',
    (24045, 'I wish this law had been enacted sooner!'):
        'Questa legge dovevano farla molto prima!',
    (24045, "That's lukewarm, we should eradicate them all!"):
        'È troppo poco, bisognerebbe sterminarli tutti quanti!',
    (24045, "I don't like werewolves because they use our infrastructure without paying resident taxes."):
        'I lupi mannari non mi piacciono: usano i nostri servizi senza pagare le tasse comunali.',
    (24045, 'We may be able to live more safely than before.'):
        'Forse adesso si vivrà un po\' più tranquilli.',
    (24045, 'The only people who would oppose this are werewolves or madmen...'):
        'Gli unici a essere contrari sono lupi mannari o pazzi...',
    (24045, 'The manager seems to be on my side...'):
        'A quanto pare l\'amministratore sta dalla nostra parte...',

    # ------------------------------- la legge di CONVIVENZA: i favorevoli
    (24074, "Let's create a kind society that is considerate of werewolves."):
        'Costruiamo una società gentile, che tenga conto dei lupi mannari.',
    (24074, "It's a natural law, but it's still not enough."):
        'È una legge ovvia, anzi non basta nemmeno.',
    (24074, "First, let's try having a werewolf manage the town."):
        'Per cominciare, proviamo a far amministrare la città a un lupo mannaro.',

    # ------------------------------- la legge di CONVIVENZA: i contrari
    (24080, 'What are you doing, traitor?!'):
        'Ma che stai facendo? Ci hai venduti!',
    (24080, "It's not coexistence if citizens are being killed!"):
        'Non è convivenza se i cittadini vengono ammazzati!',
    (24080, 'The town manager is on the wolf side!'):
        'L\'amministratore sta dalla parte dei lupi!',
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
            errori.append('%d: voce senza resa | %s' % (v['riga'], v['en'][:70]))
            continue
        viste.add(k)
        v['it'] = RESE[k]
    for k in sorted(set(RESE) - viste):
        errori.append('%d: resa senza voce nel lotto | %s' % (k[0], k[1][:70]))
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
