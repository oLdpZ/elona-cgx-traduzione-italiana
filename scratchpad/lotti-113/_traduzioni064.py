# -*- coding: utf-8 -*-
"""Le rese del lotto 064 — LE COLLANE: `FILTER_ACCESSORY_AMULET` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 064 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa064.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 064`: **14 righe su 14** con lo spazio prima del `\\n`,
14 su 14 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 064`: **+14** per 14 rese,
nessuna gemella. ⓘ `_gia-reso.py 064`: 0 su 14.

⚠️⚠️⚠️ **DUE PAROLE DA TENERE DISTINTE, E IL DIZIONARIO NE HA UNA SOLA.**
Il glossario dice 首輪 -> «collana», e in questa categoria l'indice 3 lo ripete
su tredici oggetti. Ma il corpo usa **装身具** (l'ornamento da indossare) dove
l'indice 3 usa 首輪, e a volte le due parole stanno nella stessa riga
(`:99519`: 装身具 … 宝飾品). Le rese tengono 首輪 «collana», 装身具
«ornamento», 宝飾品 «gioiello». ⓘ 装身具 non era nel dizionario: e' una parola
nuova di questo lotto.

⚠️⚠️⚠️ **`:99663` E' LA TERZA RIGA DELLA FAMIGLIA 〜を守る為に作られた**, dopo
`:99937` (兜, lotto 063, «Un'armatura fatta per proteggere la testa») e la riga
dell'indice 3 gia' in gioco. L'apertura italiana e' la stessa, cambia solo la
parte del corpo.
"""

IT = {
    # =====================================================================
    # LE COLLANE COMUNI — la raccolta di sempre
    # =====================================================================
    # ⭐⭐ :99663 e' la TERZA della famiglia 〜を守る為に作られた:
    #    :99937 (063)  頭部を守る為に作られた防具  -> «Un'armatura fatta per
    #                                                 proteggere la testa.»
    #    :99663 (064)  首を守る為に作られた装身具  -> «Un ornamento fatto per
    #                                                 proteggere il collo.»
    # ⓘ E il giapponese gioca su due verbi che il gioco distingue davvero:
    #   装着する e 装備する — indossare ed equipaggiare.

    99663: "Un ornamento fatto per proteggere il collo. Più che indossarlo si direbbe che lo si equipaggia, ed è di fattura piuttosto rozza. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ 装身具 «ornamento» e 宝飾品 «gioiello» nella stessa riga: il
    #   giapponese distingue, e la distinzione e' tutto il senso della frase.
    99519: "Un ornamento con la superficie lucidata a specchio. A dirla tutta è più un gioiello che altro, e spesso si usa per farne dono. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 想いのこめられた -> «racchiuso», come l'indice 3 gia' in gioco («Una
    # collana in cui è racchiuso un sentimento»).
    99591: "Un piccolo ornamento che vale soprattutto come scongiuro contro il male. Dicono che in quei fregi siano racchiusi i sentimenti più vari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # Stessa parola dell'indice 3 di QUESTO oggetto: «Una collana in cui è
    # racchiuso il potere magico».
    99735: "Un ornamento in cui è racchiusa una magia particolare. Una protezione diretta non c'è da aspettarsela, ma spesso, dicono, nasconde dentro qualche facoltà fuori dal comune. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    126647: "Un ornamento da portare intorno al collo. Ce n'è di ogni materiale e di ogni forma, e spesso i più cari sono quelli fatti con materiali rari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⓘ 伴侶 e' il compagno di vita, e la riga sta parlando del matrimonio
    #   del gioco: la collana passa al coniuge e non torna indietro, che e'
    #   esattamente quel che dice l'indice 3 («Non torna indietro»).
    99448: "Una collana carica d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento la collana appartiene a lui, e a strappargliela per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # IL PERIDOTO E LA RAGAZZA CHE FANTASTICA
    # =====================================================================
    99807: "Un ornamento con al centro una gemma di un verde acceso. Tagliata in quella caratteristica forma d'uovo, brilla anche di notte, e c'è chi la dice simbolo di una forza vitale senza pari. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐ 一面透明なキャンバスの様な彼: il «lui» di cui fantastica e' una
    #   creatura trasparente, e l'immagine della tela va tenuta perche' e'
    #   il perno della battuta. いやぁん e' lo strillo imbarazzato di chi si
    #   accorge di aver detto troppo.
    99809: "\\\"Oh, ma che forma graziosa. Tonda, verde, e dentro un rosso appena accennato: perfetta per lui, che è tutto una tela trasparente. Se quella persona vedesse questa collana, di sicuro... ohhh, che vergogna!\\\" \\n# ~Parole di <Rianna> la sognatrice~",

    # =====================================================================
    # I PEZZI UNICI 《…》
    # =====================================================================
    # ⚠️⚠️⚠️ :62463 — L'INGLESE FONDE DUE POPOLI IN UNO. Il giapponese
    #    nomina シャンの催眠術 e サキュバロリンの思念吸収, due specie
    #    diverse; l'inglese scrive «Sunbararian's hypnotism and mind
    #    absorption», che e' un terzo popolo ancora — quello del lotto 063.
    #    ⓘ I due nomi compaiono in TUTTO il sorgente **solo qui** (cercati:
    #    due occorrenze, le due lingue della stessa riga), quindi il
    #    giocatore giapponese e' opaco quanto il nostro e i nomi si tengono.
    # ⓘ 御利益 e' il beneficio che viene dal divino, non un effetto qualunque.

    62463: "Una sfera di cristallo fatta a immagine del dio supremo del pianeta Yekub, e porta in dono un rafforzamento dello spirito. A portarla addosso si resiste anche all'ipnosi degli Shan e all'assorbimento del pensiero dei Sakyubalorin: così dicono certi alieni, fra i quali è un souvenir molto apprezzato. \\n# ~Dizionario Fantastico di Irva~",

    # 風の神 -> «la dea del vento», gia' in gioco sull'arco lungo che dona.
    # ⓘ Qui 首輪 e' davvero un collare — l'oggetto si chiama «Collare della
    #   Tempesta» — e non una collana: la parola segue il nome.
    76247: "Un collare speciale che la dea del vento mette al suo animale prediletto. Ci sta attaccata una catena che non si vede. \\n# ~Dizionario Fantastico di Irva~",

    # ミカ e' la MICA, il minerale che si sfoglia: da li' la spirale.
    81536: "Un ornamento a forma di conchiglia, fatto di mica, con una spirale bellissima. Chi l'abbia fatto non si sa affatto, e c'è chi dice che sia roba caduta agli dei. Pare che accostandolo piano all'orecchio si senta qualcuno che parla. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ Le due collane del combattimento, che vanno lette come una coppia:
    #   一本の双剣 contro 折れたクロスボウ, il colpo in più contro il tiro in
    #   più. Gli indici 3 gia' in gioco dicono «un attacco extra in mischia»
    #   e «un attacco extra a distanza», e le due rese ci vanno d'accordo.
    82676: "Una collana che pare fatta di due piccole spade gemelle. Dicono che a portarla si acquisti un movimento svelto, come se le braccia fossero diventate due di più. \\n# ~Dizionario Fantastico di Irva~",

    82742: "Una collana viola che pare una balestra spezzata. Dicono che a portarla addosso, da chissà dove, arrivi un tiro di copertura. \\n# ~Dizionario Fantastico di Irva~",

    # 下賤な者達 e' la gente di bassa condizione, e 札 la targhetta: la riga
    # dice che il ciondolo e' un segno di riconoscimento, non un ornamento.
    83901: "Una collana misera, fatta di ferro. Più che un ornamento sembra una targhetta, e si dice sia perché alla gente di bassa condizione serve da segno per distinguere gli amici dai nemici. \\n# ~Le Notizie Raccolte da <Wiesem> l'informatore~",
}
