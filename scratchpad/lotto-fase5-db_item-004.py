# -*- coding: utf-8 -*-
"""109a - Lotto 004 di `db_item.hsp`: il rapporto degli ATTREZZI.

`FILTER_ITEM_TOOL`, `description(3)`: **166 righe del sorgente, 143 firme**.
E' la seconda categoria per peso dopo il mobilio, e la prima dove la formula
della 108a incontra una coda **quadrupla** invece che doppia.

### Le code fisse, e perche' sono quattro

Il giapponese chiude quasi ogni rapporto di questa categoria con una delle
quattro frasi che dicono **quante volte** l'oggetto si usa, e sono un fatto di
gioco, non un riempitivo: 何度でも e' illimitato, 何度か sono cariche contate,
定期的に e' un tempo di ricarica, 使い捨て e' una volta sola.

    何度でも使用することができる   ->  Si può usare sempre.
    何度か使用することができる     ->  Si può usare più volte.
    定期的に使用することができる   ->  Si può usare ogni tanto.
    使用することができる（使い捨て） -> Si usa (usa e getta).
    投げつけて使う（使い捨て）     ->  Si lancia (usa e getta).
    投げることができる             ->  Si può lanciare.

⚠️ **La coda lunga costa fino a 27 caratteri degradati su 69**, e dove il fatto
di testa non ci sta nei quaranta che restano **il modale cade**: «Si usa
sempre», «Si usa ogni tanto», «Si usa più volte». Non e' una seconda formula, e'
la stessa che si stringe — la 108a lo aveva gia' fatto sulle pergamene, dove la
testa «Una pergamena che …» cadeva a favore del verbo.

### ⚠️ Le famiglie che l'inglese distingue e il giapponese no

Come i dieci atti dei mezzi di trasporto della 108a, e per la stessa ragione —
la distinzione la porta gia' il **nome dell'oggetto**:

- **i quattro fucili anestetici** (`:42418`-`:42646`): un giapponese solo,
  「対象の体重で効果変動する麻酔銃だ」, e quattro inglesi che ci scrivono la
  fascia di peso (500-1000, 100-500, 30-100, <30 kg). Ma le fasce **sono i nomi
  degli oggetti**: TZ500-K, TZC-500, TZ30-C, TZ-30. Una resa per quattro firme;
- **le quattro carte dei semi** (`:46550`), i **quattro Potioman** (`:50477`),
  i **tre globi oscuri** (`:50948`), i **cinque nuclei di transizione**
  (`:63940`), i **tre frammenti** (`:49850`), i **quattro attrezzi da fumo**
  (`:60917`): stesso giapponese **e** stesso inglese, quindi una firma sola —
  le raggruppa gia' l'estrattore.

### ⚠️⚠️ Un difetto di monte verificato nel sorgente

**`:62023`, il lanciamissili atomico: l'inglese dice «(Reusable)» e il
giapponese 「使用することができる（使い捨て）」.** Non e' un'aggiunta, e' una
contraddizione, e stavolta non serve dedurla: `action.hsp:10130`, dentro
`EFFECT_ATOMIC_LAUNCHER`, fa `inv(INV_ITEM_NUM, ci)--`. L'oggetto **si
consuma**. Vince il giapponese, come per la razione della 108a.

### ⓘ Tre righe dove l'inglese racconta un'altra cosa, e vince il giapponese

- **`:80927`**, la statua del Creatore: il giapponese dice 「ショウルーム用」,
  *serve nella sala d'esposizione*; l'inglese racconta il Creatore del mondo del
  Moongate e che «the power is lost now»;
- **`:83081`**, l'esperienza segreta di Lomias: l'inglese dice «changes the past
  of the future», che non vuol dire niente; il giapponese dice che qualcosa
  cambiera' piu' avanti;
- **`:92392`**, il disco video: per il giapponese e' un disco con dei filmati
  incisi, per l'inglese «seem's to play your memories».

⚠️ **`:116606`, la corda robusta:** il giapponese ha **solo la coda**,
「何度でも使用することができる。」 — e l'inglese ci ha infilato la riga della
categoria («<Category: Punishment») e un «you should use them NOW!» che non c'e'
da nessuna parte. La resa e' la coda e basta.

### ⓘ «(non attivo)» si tiene, e non e' un'eccezione alla regola

`:50948` (i globi oscuri) e `:73831` (lo scanner degli effetti) hanno
«(Unimplemented)» solo in inglese. La regola di `decisioni.md` direbbe di
tacerlo, ma il dizionario ha gia' un caso identico tenuto — «You can add a
recipe … (Not implemented yet)», il cui giapponese **non** ha 未実装 e che e'
reso «(non implementato)». Le altre tre occorrenze tenute hanno 未実装 anche in
giapponese. Si tiene, nella forma piu' corta gia' in uso, «(non attivo)».

### ⓘ I termini che il lotto porta, tutti gia' decisi altrove

労働エナジー → «energia da lavoro» · フィート → «talento» · ゲージ → «barra» ·
はく製 → «statuetta» · ショウルーム → «sala d'esposizione» ·
クラムベリー → «crimberry» · 生きている武器 → «arma vivente» ·
アーティファクト → «artefatto» · 補正 → «modificatore» · ランク → «rango» ·
職業 → «classe» · 種族 → «razza» · 部位 → «parte del corpo» ·
鍵開け → «scasso» · 発言力 → «autorita'» · 名声 → «fama» · スキル → «abilita'» ·
技能 → «capacita'» · 狂気度 → «Follia» · 素材 → «materiale» · 栓 → «tappo» ·
矢弾 → «munizioni» · 味方/仲間 → «compagni» · `<Little Sister>` invariato ·
`AP`, `HP`, `MP`, `DV`, `PV`, `SP` invariati.

⚠️ **ペット non aveva una voce**, e il dizionario lo rende dieci volte
«animale» e dodici «compagno». Qui e' reso **«compagno»** in tutt'e due i posti
dove compare (`:81133` la frusta del domatore, `:85301` la macchina genetica),
perche' in Elona+ un ペット puo' benissimo essere umano e «animale» sarebbe
falso su meta' dei casi. Va in `glossario.md`.

⚠️ **Le stelle non si scrivono** (`:80221`, il martello di Garok): il giapponese
dice 「☆化する」 e ☆ e' a doppia larghezza in CP932. Si scrive quel che la
stella significa — la qualita' 4 e 5, «eccezionale».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :42418
    (42418, '(Reusable) Dart rifle that tranquilizes target weight 500-1000 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42494
    (42494, '(Reusable) Dart rifle that tranquilizes target weight 100-500 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42570
    (42570, '(Reusable) Dart rifle that tranquilizes target weight 30-100 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42646
    (42646, '(Reusable) Dart rifle that tranquilizes target weight <30 kg.'):
        "Fucile anestetico: l'effetto varia col peso. Si usa più volte.",

    # ---------------------------------------------------------- :42712
    (42712, '(Single-use) chopsticks.'):
        "Bacchette di legno. Si usa (usa e getta).",

    # ---------------------------------------------------------- :43243
    (43243, "(Reusable) Magical item that changes one's form."):
        "Dà un altro aspetto, a chiunque. Si può usare sempre.",

    # ---------------------------------------------------------- :44100
    (44100, '(Reusable) tool cage that capture and transport a defeated victim.'):
        "Ci si porta via chi è in fin di vita o inerme. Si usa sempre.",

    # ---------------------------------------------------------- :44166
    (44166, '(Reusable) tool that generates work energy using human labor.'):
        "Genera energia da lavoro a forza di braccia. Si può usare sempre.",

    # ---------------------------------------------------------- :45484
    (45484, '(Reusable) tool that set up traps.'):
        "Una pietra che piazza trappole. Si può usare sempre.",

    # ---------------------------------------------------------- :45550
    (45550, '(Single-use) tool used to gain AP.'):
        "Una pietra che dà AP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45616
    (45616, '(Single-use) tool used to restore mana.'):
        "Una pietra che dà magia e MP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45682
    (45682, '(Single-use) tool used to restore stamina.'):
        "Una pietra che dà costituzione e SP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45748
    (45748, '(Single-use) tool used to increase your resistance.'):
        "Alza tutte le resistenze fino a un limite. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45814
    (45814, '(Single-use) tool used to increase your DV modifier.'):
        "Alza il modificatore DV. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45880
    (45880, '(Single-use) tool used to increase your PV modifier.'):
        "Alza il modificatore PV. Si usa (usa e getta).",

    # ---------------------------------------------------------- :45947
    (45947, '(Single-use) exo-skeleton upgrade kit for your Potioman.'):
        "Potenzia il Potioman. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46079
    (46079, '(Single-use) tool to be used on certain corpses.'):
        "Un materiale speciale, per certi cadaveri. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46145
    (46145, '(Single-use) tool that can graft new body parts.'):
        "Una protesi che dà una parte del corpo. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46406
    (46406, '(Single-use) tool containing a large sum of corks.'):
        "Dà una gran quantità di tappi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46482
    (46482, '(Reusable) large-calibre gun that shoots guard-breaking laser.'):
        "Un'arma che rompe la guardia. Si può usare più volte.",

    # ---------------------------------------------------------- :46550
    (46550, '(Reusable) tool that summons spirits.'):
        "Uno strumento che evoca gli spiriti. Si può usare sempre.",

    # ---------------------------------------------------------- :46821
    (46821, "(Reusable) tool for one to  discover one's personalities."):
        "Rivela una parte del carattere. Si può usare sempre.",

    # ---------------------------------------------------------- :46887
    (46887, '(Single-use) tool that give you a daughter.'):
        "Serve ad avere una figlia forte. Si usa (usa e getta).",

    # ---------------------------------------------------------- :46953
    (46953, '(Single-use) tool that give you a son.'):
        "Serve ad avere un figlio forte. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47019
    (47019, '(Single-use) tool that gives experience to a living weapon.'):
        "Dà esperienza alle armi viventi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47086
    (47086, '(Single-use) tool that restores your MP.'):
        "Un anello che ridà MP. Si usa (usa e getta).",

    # ---------------------------------------------------------- :47289
    (47289, '(Reusable) tool. But it really is just smelly socks.'):
        "Calzini che puzzano. Si può usare sempre.",

    # ---------------------------------------------------------- :49779
    (49779, '(Reusable) tool that drench your thirst. Can be refilled under water.'):
        "Disseta; si riempie sott'acqua. Si può usare sempre.",

    # ---------------------------------------------------------- :49850
    (49850, "(Reusable) tool that raises one's stats to a certain level."):
        "Alza gli attributi fino a un limite. Si può usare sempre.",

    # ---------------------------------------------------------- :50063
    (50063, '(Reusable) tool that turns a dying enemy into solid gold.'):
        "Trasforma in oro il nemico in fin di vita. Si può usare sempre.",

    # ---------------------------------------------------------- :50134
    (50134, '(Reusable) tool that grants fame and authority.'):
        "Dà fama o autorità. Si può usare sempre.",

    # ---------------------------------------------------------- :50205
    (50205, '(Reusable) tool that allow simutaneous activation of two skills.'):
        "Attiva due capacità insieme. Si può usare sempre.",

    # ---------------------------------------------------------- :50274
    (50274, '(Reusable) tool that allows you to marry non-allies.'):
        "Fa sposare anche chi non è tra i compagni. Si può usare sempre.",

    # ---------------------------------------------------------- :50344
    (50344, '(Reusable) tool used on the world map. May be used periodically.'):
        "Funziona sulla mappa del mondo. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :50411
    (50411, '(Single-use) tool crystal that half your skill to gain a slight bonus.'):
        "Dimezza un'abilità e dà un piccolo bonus. Si usa (usa e getta).",

    # ---------------------------------------------------------- :50477
    (50477, '(Reusable) tool that shoots out potion plugs at lethal velocity.'):
        "Spara tappi di pozione a gran velocità. Si può usare sempre.",

    # ---------------------------------------------------------- :50749
    (50749, '(Reusable) tool for processing vast amounts of information.'):
        "Elabora una mole enorme di informazioni. Si può usare sempre.",

    # ---------------------------------------------------------- :50948
    (50948, '(Unimplemented) (Reusable) tool used to set up or activate traps.'):
        "Piazza e innesca trappole (non attivo). Si può usare sempre.",

    # ---------------------------------------------------------- :51291
    (51291, '(Single-use) tool shard that grants you the memory of a skill.'):
        "Un frammento con la memoria di un'abilità. Si usa (usa e getta).",

    # ---------------------------------------------------------- :51982
    (51982, '(Single-use) throwing tool that creates a smoke screen.'):
        "Stende una cortina di fumo. Si lancia (usa e getta).",

    # ---------------------------------------------------------- :52048
    (52048, '(Reusable) tool that allows you to check and use your Yaca points.'):
        "Una carta per vedere e spendere i punti. Si può usare sempre.",

    # ---------------------------------------------------------- :52383
    (52383, '(Reusable) tool that give you weapon experience through training.'):
        "Allena le abilità con le armi. Si può usare sempre.",

    # ---------------------------------------------------------- :52449
    (52449, '(Reusable) tool that secure the harvest.'):
        "Fissa il raccolto. Si può usare sempre.",

    # ---------------------------------------------------------- :54888
    (54888, '(Single-use) tool that starts a fire.'):
        "Serve ad accendere il fuoco. Si usa (usa e getta).",

    # ---------------------------------------------------------- :55145
    (55145, '(Reusable) tool to enhance the shooting attack power.'):
        "Potenzia l'attacco a distanza. Si può usare sempre.",

    # ---------------------------------------------------------- :55484
    (55484, '(Single-use) tool that grants magic power.'):
        "Un frammento che contiene magia. Si usa (usa e getta).",

    # ---------------------------------------------------------- :56606
    (56606, '(Reusable) tool that cleans your ear.'):
        "Serve a pulirsi le orecchie. Si può usare sempre.",

    # ---------------------------------------------------------- :57066
    (57066, '(Single-use) tool that creates a cake for your allies to eat.'):
        "Non si mangia: usandolo, mangiano tutti i compagni (usa e getta).",

    # ---------------------------------------------------------- :57648
    (57648, '(Reusable) toy modeled after Goddess of Wealth. May be used periodically.'):
        "Riproduce la dea della ricchezza. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :58529
    (58529, "It is a sword made for Seppuku. (Reusable) tool that can't be equipped."):
        "Una spada per il seppuku. Non si equipaggia, ma si usa sempre.",

    # ---------------------------------------------------------- :59661
    (59661, '(Single-use) tool stardust that enhances an artifact.'):
        "Polvere di stelle che potenzia un artefatto (usa e getta).",

    # ---------------------------------------------------------- :59929
    (59929, '(Single-use) tool that 3d-prints target with biological materials.'):
        "Un apparecchio che fa statuette. Si usa (usa e getta).",

    # ---------------------------------------------------------- :60066
    (60066, '(Single-use) tool that brings out the true potential of t equipment.'):
        "Tira fuori le vere doti dell'equipaggiamento (usa e getta).",

    # ---------------------------------------------------------- :60652
    (60652, '(Reusable) tool that launches a ball of gunpowder.'):
        "Spara in aria palle di polvere. Si può usare più volte.",

    # ---------------------------------------------------------- :60917
    (60917, '(Single-use) smoking tool.'):
        "Un attrezzo per fumare. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62023
    (62023, '(Reusable) tactical nuclear weapon.'):
        "Un'arma nucleare tattica. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62099
    (62099, "(Reusable) tool that burns down the area around the target it's aimed at."):
        "Incendia tutto intorno al bersaglio. Si può usare più volte.",

    # ---------------------------------------------------------- :62175
    (62175, '(Reusable) weapon that temporarily lowers the PV of a target.'):
        "Abbassa per un po' il PV del bersaglio. Si usa più volte.",

    # ---------------------------------------------------------- :62237
    (62237, 'It is a blanket that prevents allies from getting up early.'):
        "Il compagno che la porta non riesce più ad alzarsi presto.",

    # ---------------------------------------------------------- :62603
    (62603, '(Single-use) tool box of first aid supplies.'):
        "Una scatola per il primo soccorso. Si usa (usa e getta).",

    # ---------------------------------------------------------- :62669
    (62669, '(Single-use) toolbox filled with specialized ammunitions.'):
        "Una cassa che ricarica le munizioni speciali (usa e getta).",

    # ---------------------------------------------------------- :63524
    (63524, '(Single-use) horrifying weapon of destruction from ancient times.'):
        "Dopo un po' esplode e devasta un'area vasta (usa e getta).",

    # ---------------------------------------------------------- :63940
    (63940, '(Reusable) tool that transforms you. Can be used with 50% gauge.'):
        "Dà un altro aspetto e altra forza. Si usa con la barra al 50%.",

    # ---------------------------------------------------------- :64556
    (64556, '(Reusable) tool that opens a pocket in another dimension to store item.'):
        "Apre una tasca quadridimensionale. Si può usare più volte.",

    # ---------------------------------------------------------- :64681
    (64681, '(Single-use) tool box that allows all your friends to eat together.'):
        "Usandolo, mangiano tutti i compagni (usa e getta).",

    # ---------------------------------------------------------- :64744
    (64744, '(Reusable) tool that holds 15 coffins of necromancy.'):
        "Contiene fino a 15 bare della negromanzia. Si può usare sempre.",

    # ---------------------------------------------------------- :64810
    (64810, '(Single-use) tool that grants a body part you want.'):
        "Dà la parte del corpo che si vuole. Si usa (usa e getta).",

    # ---------------------------------------------------------- :65198
    (65198, '(Single-use) throwing tool that initializes duel with your opponent.'):
        "Un guanto da duello: si lancia all'avversario (usa e getta).",

    # ---------------------------------------------------------- :65467
    (65467, '(Single-use) tool lenses that allow you to see information of the target.'):
        "Una lente che mostra i dati del bersaglio. Si usa (usa e getta).",

    # ---------------------------------------------------------- :66078
    (66078, '(Reusable) tool stone that confirms your faith.'):
        "Una pietra che dice la fede. Si può usare sempre.",

    # ---------------------------------------------------------- :67669
    (67669, '(Reusable) tool that plays any music you want.'):
        "Suona il brano che si vuole. Si può usare sempre.",

    # ---------------------------------------------------------- :68590
    (68590, '(Single-use) tool that used for inhaling dried crimberry smoke.'):
        "Serve a fumare crimberry essiccate. Si usa (usa e getta).",

    # ---------------------------------------------------------- :68786
    (68786, '(Single-use) tool to use in a Showroom.'):
        "Serve nella sala d'esposizione. Si usa (usa e getta).",

    # ---------------------------------------------------------- :69457
    (69457, '(Single-use) tool for crops.'):
        "Concime per le colture. Si usa (usa e getta).",

    # ---------------------------------------------------------- :70336
    (70336, '(Single-use) cooking tool set.'):
        "Un attrezzo da cucina limitato. Si usa (usa e getta).",

    # ---------------------------------------------------------- :70601
    (70601, '(Reusable) tool used for necromancy. May be used periodically.'):
        "Sveglia il mostro che dorme nella bara. Si usa ogni tanto.",

    # ---------------------------------------------------------- :70820
    (70820, '(Single-use) tool that duplicate the existence of target into your team.'):
        "Duplica il bersaglio e lo mette nel gruppo. Si usa (usa e getta).",

    # ---------------------------------------------------------- :71927
    (71927, '(Single-use) tool doll that is 10cm in height.'):
        "Una bambola alta una decina di centimetri. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72487
    (72487, '(Single-use) tool that changes your profession. Write in lower caption.'):
        "Un articolo che cambia la classe. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72553
    (72553, '(Single-use) tool that changes your race. Use in lower caption.'):
        "Un oggetto che cambia la razza. Si usa (usa e getta).",

    # ---------------------------------------------------------- :72623
    (72623, '(Reusable) tool for sound of certain frequency. May be used periodically.'):
        "Un fischietto a frequenza speciale. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :73023
    (73023, '(Single-use) tool that unlocks special abilities.'):
        "Una gemma che serba poteri speciali. Si usa (usa e getta).",

    # ---------------------------------------------------------- :73291
    (73291, '(Reusable) tool that switch between offensive and defensive instructions.'):
        "Alterna ordini d'attacco e di difesa. Si può usare sempre.",

    # ---------------------------------------------------------- :73701
    (73701, 'It is a statue of God of Elements. May be used periodically.'):
        "Una statua del dio degli elementi. Si usa ogni tanto.",

    # ---------------------------------------------------------- :73768
    (73768, 'It is a statue of Goddess of Wealth. May be used periodically.'):
        "Una statua della dea della ricchezza. Si usa ogni tanto.",

    # ---------------------------------------------------------- :73831
    (73831, '(Unimplemented) (Reusable) tool that apply the effect of the cards.'):
        "Tira fuori l'effetto delle carte (non attivo). Si usa sempre.",

    # ---------------------------------------------------------- :76317
    (76317, '(Reusable) tool used shoot every enemy nearby. May be used periodically.'):
        "Danno a tutti i nemici, secondo il Tiro. Si usa ogni tanto.",

    # ---------------------------------------------------------- :77776
    (77776, '(Reusable) tool for monthly allowence. May be used periodically.'):
        "Una volta al mese arriva la paghetta. Si usa ogni tanto.",

    # ---------------------------------------------------------- :78259
    (78259, '(Reusable) tool that allow using of complex fusion recipes.'):
        "Un attrezzo per le fusioni complesse. Si può usare sempre.",

    # ---------------------------------------------------------- :79114
    (79114, 'It is a statue of God of Machine. May be used periodically.'):
        "Una statua del dio delle macchine. Si usa ogni tanto.",

    # ---------------------------------------------------------- :79181
    (79181, 'It is a statue of God of Harvest. May be used periodically.'):
        "Una statua del dio del raccolto. Si usa ogni tanto.",

    # ---------------------------------------------------------- :80221
    (80221, '(Single-use) tool that raises the quality of the equipment.'):
        "Rende eccezionale un'arma o un'armatura. Si usa (usa e getta).",

    # ---------------------------------------------------------- :80927
    (80927, 'It is a statue of creator from the Moongate world. The power is lost now.'):
        "Serve nella sala d'esposizione. Si può usare sempre.",

    # ---------------------------------------------------------- :80995
    (80995, '(Reusable) tool used in showrooms. May be used to summon CNPCs.'):
        "Serve nella sala d'esposizione. Si può usare sempre.",

    # ---------------------------------------------------------- :81133
    (81133, '(Reusable) tool that forbids pet from doing certain actions.'):
        "Vieta ai compagni di raccogliere roba. Si può usare sempre.",

    # ---------------------------------------------------------- :81199
    (81199, '(Reusable) tool that analyzes the mind of the target.'):
        "Analizza l'animo del bersaglio. Si può usare sempre.",

    # ---------------------------------------------------------- :82007
    (82007, '(Reusable) tool that can tie up a weakened monster.'):
        "Ci si appende un mostro indebolito. Si può usare sempre.",

    # ---------------------------------------------------------- :82812
    (82812, 'It is a statue of Goddess of Luck. May be used periodically.'):
        "Una statua della dea della fortuna. Si usa ogni tanto.",

    # ---------------------------------------------------------- :83081
    (83081, '(Reusable?) gem that changes the past of the future.'):
        "Una gemma che, usata, cambierà qualcosa più avanti.",

    # ---------------------------------------------------------- :83212
    (83212, '(Single-use) tool that grants you a feat.'):
        "Una gemma che dà un talento nuovo (usa e getta).",

    # ---------------------------------------------------------- :84038
    (84038, '(Reusable) tool that creates a high pitch noise.'):
        "Manda un suono acuto tutt'intorno. Si può usare sempre.",

    # ---------------------------------------------------------- :84166
    (84166, '(Reusable) tool to store cards.'):
        "Una scatola per le carte. Si può usare sempre.",

    # ---------------------------------------------------------- :84299
    (84299, "It is a throwable tool that can be used to capture 'Little Sister'."):
        "Colpisce e cattura la <Little Sister>. Si può lanciare.",

    # ---------------------------------------------------------- :84970
    (84970, 'It is a horrible looking furniture. It is best not to touch it.'):
        "Un mobile orribile a vedersi. Meglio non toccarlo.",

    # ---------------------------------------------------------- :85171
    (85171, 'It is a statue of Goddess of Healing. May be used periodically.'):
        "Una statua della dea della guarigione. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85237
    (85237, 'It is a throwable tool that can be used to capture monsters.'):
        "Colpisce e cattura un mostro. Si può lanciare.",

    # ---------------------------------------------------------- :85301
    (85301, '(Reusable) tool that erases a pet and transfers its ability to another.'):
        "Cancella un compagno e dà le sue doti a un altro. Si usa sempre.",

    # ---------------------------------------------------------- :85370
    (85370, '(Reusable) tool used the reconstruct material. May be used periodically.'):
        "Ricompone la materia e la muta in altro. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85437
    (85437, '(Reusable) tool used to accelerate crop growth. May be used periodically.'):
        "Accelera la crescita delle colture. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85506
    (85506, "(Reusable) tool used to recover allies' health. May be used periodically."):
        "Cura gli HP dei compagni intorno. Si usa ogni tanto.",

    # ---------------------------------------------------------- :85575
    (85575, '(Reusable) tool used to raise speed. May be used periodically.'):
        "Alza la velocità per un po'. Si può usare ogni tanto.",

    # ---------------------------------------------------------- :86203
    (86203, '(Single-use) bomb that inflicts devastating destruction over a wide area.'):
        "Dopo un po' esplode e devasta un'area vasta (usa e getta).",

    # ---------------------------------------------------------- :86536
    (86536, 'It is a statue of Goddess of Wind. May be used periodically.'):
        "Una statua della dea del vento. Si usa ogni tanto.",

    # ---------------------------------------------------------- :86603
    (86603, 'It is a statue of God of Earth. May be used periodically.'):
        "Una statua del dio della terra. Si usa ogni tanto.",

    # ---------------------------------------------------------- :88024
    (88024, '(Reusable) Rank 4 bed of simple design.'):
        "Un letto semplice (rango 4). Si può usare sempre.",

    # ---------------------------------------------------------- :88213
    (88213, '(Single-use) tool that reduce the insanity level.'):
        "Abbassa la Follia tua e dei compagni intorno (usa e getta).",

    # ---------------------------------------------------------- :88413
    (88413, '(Autoused) tool that enhances your lockpicking capabilities.'):
        "Basta averlo addosso: lo scasso riesce molto più spesso.",

    # ---------------------------------------------------------- :88475
    (88475, '(Autoused) tool that is required for picking locks. It may break.'):
        "Serve per lo scasso. Certe volte si rompe.",

    # ---------------------------------------------------------- :88541
    (88541, '(Single-use) tool that destroys the ones stepped on it when armed.'):
        "Una bomba che dilania chi la calpesta. Si usa (usa e getta).",

    # ---------------------------------------------------------- :88607
    (88607, '(Reusable) tool to tie up friends and keep them from going too far away .'):
        "Lega un compagno perché non si allontani. Si usa sempre.",

    # ---------------------------------------------------------- :88872
    (88872, '(Single-use) tool that re-forge the material of target item.'):
        "Rifà l'oggetto nel materiale scelto (usa e getta).",

    # ---------------------------------------------------------- :88940
    (88940, '(Reusable) tool that reset non-monster hostile situations.'):
        "Azzera l'ostilità di chi non è un mostro. Si usa più volte.",

    # ---------------------------------------------------------- :90140
    (90140, '(Reusable) tool that allows you to change the decor of a room.'):
        "Cambia l'arredo della stanza. Si può usare sempre.",

    # ---------------------------------------------------------- :91912
    (91912, '(Reusable) hand-held simple light.'):
        "Una luce semplice da tenere in mano. Si può usare sempre.",

    # ---------------------------------------------------------- :92255
    (92255, '(Reusable) tool that allows you to save money.'):
        "Ci si mette da parte una somma alla volta. Si usa sempre.",

    # ---------------------------------------------------------- :92392
    (92392, "It is a mysterious disc that seem's to play your memories."):
        "Un disco con dei filmati incisi. Si può usare sempre.",

    # ---------------------------------------------------------- :92937
    (92937, 'It is a blanket that prevents items from being damaged by freezing.'):
        "Una coperta che protegge dal gelo, per qualche volta.",

    # ---------------------------------------------------------- :93001
    (93001, 'It is a blanket that prevents items from being damaged by burning.'):
        "Una coperta che protegge dal fuoco, per qualche volta.",

    # ---------------------------------------------------------- :93361
    (93361, '(Reusable) tool that change assignments.'):
        "Cambia l'incarico. Si può usare sempre.",

    # ---------------------------------------------------------- :93826
    (93826, '(Reusable) tool that can be used to build a shelter in a hurry.'):
        "Un rifugio che si monta in un po' di tempo. Si usa sempre.",

    # ---------------------------------------------------------- :94604
    (94604, 'It is an usable disc etched with music data.'):
        "Un disco con della musica incisa. Si può usare sempre.",

    # ---------------------------------------------------------- :99094
    (99094, "(Reusable) tool that visualizes an ally's health."):
        "Mostra gli HP dei compagni. Si può usare sempre.",

    # ---------------------------------------------------------- :102461
    (102461, '(Reusable) Rank 0 makeshift bed.'):
        "Un letto semplice (rango 0). Si può usare sempre.",

    # ---------------------------------------------------------- :104794
    (104794, '(Reusable) tool made for gem cutting, a necessity for jewelers.'):
        "Serve a lavorare le gemme. Si può usare sempre.",

    # ---------------------------------------------------------- :108460
    (108460, '(Reusable) tool made for fishing, a necessity for the fisherman.'):
        "Serve a pescare. Si può usare sempre.",

    # ---------------------------------------------------------- :114080
    (114080, 'It is a cooking tool allowing the preparation of dishes up to Rank 5.'):
        "Ci si cucinano i piatti fino al rango 5.",

    # ---------------------------------------------------------- :114144
    (114144, 'It is a glowing cooking tool allowing preparation of dishes up to Rank 3.'):
        "Ci si cucina fino al rango 3. Illumina sempre intorno.",

    # ---------------------------------------------------------- :116349
    (116349, 'It is a cooking tool allowing the preparation of dishes up to Rank 4.'):
        "Ci si cucinano i piatti fino al rango 4.",

    # ---------------------------------------------------------- :116606
    (116606, '(Reusable) tool that you should use them NOW! <Category: Punishment.'):
        "Si può usare sempre.",

    # ---------------------------------------------------------- :120508
    (120508, '(Reusable) tool made for carpentry, a necessity for carpenters.'):
        "Serve per i lavori di falegnameria. Si può usare sempre.",

    # ---------------------------------------------------------- :120574
    (120574, '(Reusable) tool made for tailoring, a necessity for the tailors.'):
        "Serve a cucire. Si può usare sempre.",

    # ---------------------------------------------------------- :121832
    (121832, 'It is a tool for painting. Cannot be used.'):
        "Serve a dipingere. Non si può usare.",

    # ---------------------------------------------------------- :122682
    (122682, '(Reusable) tool made for basic alchemy.'):
        "Serve per l'alchimia. Si può usare sempre.",

# 143 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-004.jsonl'
RIGHE = {
    42418, 42494, 42570, 42646, 42712, 43243, 44100, 44166, 45484, 45550,
    45616, 45682, 45748, 45814, 45880, 45947, 46079, 46145, 46406, 46482,
    46550, 46821, 46887, 46953, 47019, 47086, 47289, 49779, 49850, 50063,
    50134, 50205, 50274, 50344, 50411, 50477, 50749, 50948, 51291, 51982,
    52048, 52383, 52449, 54888, 55145, 55484, 56606, 57066, 57648, 58529,
    59661, 59929, 60066, 60652, 60917, 62023, 62099, 62175, 62237, 62603,
    62669, 63524, 63940, 64556, 64681, 64744, 64810, 65198, 65467, 66078,
    67669, 68590, 68786, 69457, 70336, 70601, 70820, 71927, 72487, 72553,
    72623, 73023, 73291, 73701, 73768, 73831, 76317, 77776, 78259, 79114,
    79181, 80221, 80927, 80995, 81133, 81199, 82007, 82812, 83081, 83212,
    84038, 84166, 84299, 84970, 85171, 85237, 85301, 85370, 85437, 85506,
    85575, 86203, 86536, 86603, 88024, 88213, 88413, 88475, 88541, 88607,
    88872, 88940, 90140, 91912, 92255, 92392, 92937, 93001, 93361, 93826,
    94604, 99094, 102461, 104794, 108460, 114080, 114144, 116349, 116606, 120508,
    120574, 121832, 122682,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
