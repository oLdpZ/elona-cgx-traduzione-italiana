# -*- coding: utf-8 -*-
"""93a - ARIBEL la monella (`chat.hsp:9983`-`:10013`, 10 firme su 10).

腕白少女『アリベル』 / `<Aribel>` (`db_card.hsp:4521`, reso **«<Aribel> la
monella»**) e' la **figlia di MARY l'entomologa** (resa nella 90a) e la sorella
adottiva di **<Alice> la formica gigante** (resa nella 92a): questo blocco e'
il terzo lato di quella famiglia, e si legge insieme agli altri due.

⭐ IL REGISTRO E' GIA' FISSATO da `db_creature.hsp:62712`-`:62724`, le sue
battute: **«Le sette regole di <Aribel>, numero uno. Mai abbassare la guardia.»**
e «Ah... Le sette regole di <Aribel>, numero quattro! Se si cade... si cade...
in avanti...!». E' una ragazzina in viaggio d'allenamento che parla per
proclami, con le esclamazioni in fila.

LESSICO EREDITATO (non deciso qui):
  - アリス      «<Alice> la formica gigante»  db_card.hsp:6809
  - 巨大蟻      «formica gigante»             db_card.hsp:6809
  - 虫図鑑      «atlante degli insetti»       db_creature.hsp:76544 (昆虫図鑑)
  - ネフィア    «Nefia»                       ovunque

⭐⭐⭐ DEROGA 1 — `:9986`, L'INGLESE ROVESCIA LA BATTUTA IN DUE PUNTI.
Il giapponese e' 「逆境上等！覚悟は上々！」, cioe' **due vanti**: *le avversita'
sono benvenute* e *la mia determinazione e' ottima*. L'inglese legge il primo
come «This is bad!» e il secondo come «Prepare yourself!», e la spavalderia di
una ragazzina diventa l'avvertimento di qualcuno che ha paura. ⚠️ E 拳で語り合う
non e' «Father speaks through his powerful fists»: e' **parlarsi a suon di
pugni**, reciproco, ed e' quello che lei vuole poter fare col padre quando sara'
abbastanza forte. Si segue il giapponese in tutt'e tre i punti.

⭐⭐ DEROGA 2 — `:9990`, 何億種 SONO SPECIE, NON LIBRI.
Il giapponese dice che negli atlanti «chissa' quante centinaia di milioni di
**specie** saranno scritte»; l'inglese scrive «there must be millions of those
kinds of books written». E' la madre che legge un libro solo da mesi, non una
biblioteca: e la battuta e' che gli insetti sono infiniti. Si segue il
giapponese.

⚠️ DEROGA 3 — `:9996`, LA VOCE DI MENU E' UN FORMULARIO, E RESTA TALE.
「巨大蟻の管理不行届き」 e' lingua da verbale amministrativo (管理不行届き =
*custodia negligente*) applicata a una formica gigante: la comicita' sta
nell'attrito fra il registro e la bestia. L'inglese la appiattisce in
«Incompetence at taking care of large ants». Si tiene il formulario.

💡 CONTROLLO DEL VICINATO: `:9993` fa dire ad Aribel che **Alice biascica** se
interrogata — e Alice, resa nella 92a, e' la formica che nella missione di Mary
si esprime a versi. L'accordo italiano si appoggia al nome della creatura
(femminile), non al genere del giocatore.

PERIMETRO: 10 firme su 10 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 9983`) e **zero firme gia' rese altrove**.

MENU: uno, da 3 voci (`:9994`-`:9996`), tutte nuove.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- nella Culla del Caos, in viaggio d'allenamento
    9986: 'Le avversità? Ben vengano! La determinazione? Al massimo! Anche '
          'per diventare forte abbastanza da parlare a suon di pugni con '
          'papà, mi alleno qui a Nefia!',

    # --- a missione finita, di ritorno a casa
    9990: 'Torno dal viaggio d\'allenamento e trovo la mamma ancora '
          'sprofondata negli atlanti degli insetti. Uff... se ci metti dentro '
          'anche le civiltà del passato, chissà quante centinaia di milioni '
          'di specie ci saranno scritte. Quasi quasi, per ammazzare il tempo, '
          'mi infilo in qualche Nefia qui intorno...',

    # --- il sospetto sulla madre, e il menu delle tre risposte
    9993: 'Strano. Non la vedevo da un pezzo e la mamma si comporta in modo '
          'troppo sospetto. E anche Alice, se le chiedo, biascica. Che stiano '
          'nascondendo qualcosa...?',
    9997: 'Ehm, scusa. Non è che sai se mia madre nasconde qualcosa?',
    9994: 'Non ne so niente',
    9995: 'Mi hanno fatto giurare di tacere...',
    9996: 'Custodia negligente di formica gigante',
    10001: 'Ah sì...? Allora non resta che parlarne a suon di pugni!',
    10004: 'Okay, okay, ho capito. Consiglio di famiglia, e la torchio finché '
           'non parla!',
    10007: 'Un\'altra volta?! E la mamma che diceva che stavolta ad Alice ci '
           'badava lei! Uffa, che sbadata!',
}
