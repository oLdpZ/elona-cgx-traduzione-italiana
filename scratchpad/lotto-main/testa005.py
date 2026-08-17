# -*- coding: utf-8 -*-
"""Lotto fase4-main-005: il finale di Lesimas — la scena del Figlio del Caos e
il quadro del cammino (main.hsp, righe 4006-4105).

Ventidue rese, ed e' il pezzo di prosa piu' importante di `main.hsp`: la scena
che si vede **una volta sola per partita**, quando si arriva in fondo a Lesimas
e Zeome e' morto. Undici righe di racconto, poi il quadro riassuntivo con lo
sfondo `g1.bmp`, poi la stessa cosa per Remido.

⭐ **Cinque nomi propri erano gia' tutti decisi, e nessuno e' stato scelto qui:**

  - «Zeome» sta cosi' in `text.hsp:669`, e `db_card.hsp:10397` lo chiama
    «<Zeome> il falso profeta»;
  - il 「盟約」 e' il **«Patto Eterno»** (`db_creature.hsp:46255`,
    `text.hsp:9695` «Parte terza - Il patto eterno»);
  - 「ノースティリス」 e' **«Tyris del Nord»** (`text.hsp:2737`);
  - 「レミード」 e' **«le Rovine di Remido»** (`text.hsp:2979`), e la resa tiene
    le rovine perche' e' cosi' che il gioco nomina il posto ovunque;
  - 「レシマス」 resta **«Lesimas»**.

⭐⭐ **「秘宝」 non e' «il codice», ed e' il giapponese a dirlo.** L'inglese scrive
`the codex`, che in italiano non vuol dire niente di preciso; il giapponese dice
「レシマスの秘宝」, e 「秘宝」 e' gia' reso **«tesoro segreto»** in
`db_item.hsp:143525`. La resa e' «il tesoro segreto di Lesimas», che dice quel
che l'oggetto e' e riusa una parola gia' fissata invece di coniarne una.

⚠️ **La scena e' tutta al «tu», e nessuna riga puo' portare un participio.**
Il giocatore non ha genere: `:4006` dice «prima o poi doveva succedere» e non
«saresti arrivato», `:4065` mette l'arrivo come **voce di registro** («Anno 517,
12/8: arrivo a Tyris del Nord») invece di «sei sbarcato», `:4067` conta le
creature in una colonna invece di dire «hai raggiunto». E' la stessa disciplina
del lotto 003 e dei figli della 52ª, applicata a un testo lungo.

⭐ **`:4065`-`:4073` e' un QUADRO, non un paragrafo, e la resa lo scrive come
tale.** Le sei righe stanno dentro `display_window 60, 70, 680, 488` e sono
stampate una per una con `mes`, separate da `mes ""`: e' un tabellone. Il
giapponese e' una frase sola spezzata in tre (「…到達し、」「…殺して、」「…叩き出して
いる。」), l'inglese ha gia' rotto la catena, e l'italiano la rompe fino in fondo —
ogni riga sta in piedi da sola, con i due punti al posto del verbo. ⚠️ Il `\\n` di
`:4067` va tenuto: l'inglese ce l'ha messo perche' la riga non ci stava, e la
resa italiana e' piu' lunga, non piu' corta.

⭐⭐ **`:4050` fa parlare la rete 3, e la divergenza la impone UPSTREAM.** La rete
avverte che 「*勝利*」 e' gia' reso «<Vittoria>» in `skill.hsp:1780`, ed e' vero —
ma quel sito e' `skillname(SKILL_SPACT_WIN)`, cioe' il nome di una **mossa**, e
li' **l'inglese scrive `<Win>`**, con le parentesi angolari, mentre qui scrive
`*Win*`, con gli asterischi. Lo stesso giapponese, due forme inglesi diverse
scelte apposta per due mestieri diversi: la resa segue il mestiere, `<Vittoria>`
per la mossa e `*Vittoria*` per il cartello.
💡 E' la regola della 47ª — «quando la rete 3 accusa, si guarda il mestiere del
sito che cita» — in una forma piu' facile del solito: qui a distinguere i due
mestieri non serve un ragionamento, basta guardare che cosa ha fatto l'inglese.
⚠️ Gli asterischi restano per la stessa ragione di `:3024` nel lotto 004, dove
`*Loss on points*` e' diventato `*Sconfitta ai punti*`.

💡 **`:4048` riordina i due `cdatan`, e puo' farlo.** L'inglese scrive
«Blessing to NAME, AKA!», il giapponese «AKA NAME に祝福あれ！»: la rete 11
confronta l'**insieme** delle funzioni di contenuto, non la loro posizione
(misurato nella 40ª), quindi l'ordine e' una scelta di stile. Qui si tiene
quello inglese, perche' in italiano «Benedizione su Ary, il viandante!» suona e
«Benedizione sul viandante Ary!» no.
"""
