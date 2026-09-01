# -*- coding: utf-8 -*-
"""Le rese del lotto 070 — I RESTI: `FILTER_REMAINS` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 070 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa070.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Forma, da `_forma.py 070`: **7 righe su 7** con lo spazio prima del `\\n`;
code, **2 con lo spazio dopo il `#` e 5 senza**. Le due col ripiego sono quelle
del Catalogo d'Arte, le cinque senza sono quelle delle Cianfrusaglie.

⚠️⚠️⚠️ E `_forma.py` dice SI/NO, mentre il preflight confronta la spaziatura
**carattere per carattere**: `:97263` ha **DUE** spazi prima del `\\n`
nell'inglese, e la prima stesura ne aveva messo uno. Il primo giro del
preflight l'ha preso — «en '  ', it ' '». Un referto booleano non dice il
margine, e qui il margine era un byte.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 070`: **+7** per 7 rese,
nessuna gemella.

⭐⭐⭐ Il risultato del lotto: **l'inglese appiattisce cinque righe in una.**
Le cinque righe dei resti dicono in giapponese tre elenchi d'usi diversi con
**due verbi diversi**, e l'inglese scrive per tutte e cinque «can be used for
medicine and sorcery». Reso dall'inglese, il giocatore leggerebbe la stessa
frase cinque volte.

    :108519  骨片  osso    水薬や呪術に**使用**できる
    :108581  心臓  cuore   水薬や呪術に**使用**できる
    :108643  瞳    occhio  装飾品や薬に**加工**できる
    :108705  体液  sangue  水薬等に**加工**できる
    :108767  皮    pelle   服や鞄に**加工**できる

⭐ 使用できる e' «si usa» — la cosa entra intera in un procedimento; 加工できる
e' «si lavora» — la cosa e' materia prima che diventa altro. Il giapponese
sceglie, e sceglie due volte «usare» (osso, cuore) e tre volte «lavorare»
(occhio, sangue, pelle). ⚠️ Osso e cuore hanno il giapponese **identico** in
quella frase: sono quattro frasi diverse su cinque righe, non cinque.

⭐⭐ Le sorelle gia' rese stanno **fuori dal lotto** e sotto lo stesso titolo:
`ITEM_ID_ANIMAL_BONE` (:116408), `ITEM_ID_SKELETON` (:127669) e
`ITEM_ID_BONE_FRAGMENT` (:127731) sono le ossa sbiancate dal tempo, e dicono
呪術や水薬精製. Da li' si ricopiano le due parole: 呪術 -> **stregoneria**,
水薬 -> **pozioni**. ⓘ 薬 nudo (l'occhio) resta «medicine»: e' un'altra parola.

⚠️ `_122-sorelle-per-frase 070`: **32 frasi con una sorella, 0 gia' rese** —
tutte e trentadue stanno dentro il lotto. E' la famiglia piu' chiusa vista
finora, e per questo la testa e la coda si tengono **identiche parola per
parola** dove il giapponese le tiene identiche.
💡 Rimedio alla forma impersonale, come nel 069: 敵を破砕した際に non ha
soggetto, e «nel frantumare un nemico» regge tutti e quattro i soggetti
italiani senza cambiare una lettera.

⚠️ `:108705` NON ha 敵を破砕した際に: dice 飛び散った生物の体液を集めたもの,
cioe' i resti si **raccolgono** invece di schizzare via. La resa lo segue e non
uniforma. ⓘ E il NOME dell'oggetto e' «sangue», non «fluidi»: si dice sangue,
come vuole la regola del 069 — il pezzo si chiama col nome che il giocatore
legge in cima al pannello, e l'indice 3 dice gia' «Il sangue di una creatura».
"""

IT = {
    # =====================================================================
    # IL CATALOGO D'ARTE DI LUMIEST — DUE PEZZI DA COLLEZIONE
    # =====================================================================
    # ⓘ Sono gli unici due del lotto con lo spazio dopo il `#`.
    # 紙片 e' «foglietto» e non «foglio»: l'indice 3 della stessa voce dice
    # 紙 nudo, ed e' li' che sta «Un foglio con i dati di una creatura».
    # Il giapponese usa due parole, e la resa le tiene due.
    # ⓘ 遊戯用 e' il gioco di carte: «da gioco», non «da giocattolo».

    97263: "Un foglietto su cui le informazioni sono descritte per filo e per segno: altezza e peso, s'intende, ma anche i tratti particolari, scritti nei minimi dettagli. Eppure per raccogliere informazioni non si usa quasi mai; complice il materiale lucido, pare che serva soltanto da collezione e da gioco.  \\n# ~Catalogo d'Arte di Lumiest~",

    # 生き写し e' il modo di dire italiano «il ritratto vivente», che si dice
    # esattamente cosi' di una persona somigliantissima a un'altra.
    # ⚠️ 犠牲者 e' al singolare in giapponese e l'inglese lo mette al plurale
    # insieme al soggetto: qui vince il giapponese, una statua una vittima.
    # ⓘ Il NOME dell'oggetto e' «statuetta» (dizionario, tre voci), ma qui il
    # giapponese dice 像 e non はく製: «statua».

    97325: "Una statua fatta con tale finezza da sembrare il ritratto vivente della vittima. La figura è così piena di vita che pare stia per muoversi da un momento all'altro. \\n# ~Catalogo d'Arte di Lumiest~",

    # =====================================================================
    # LE MILLE CIANFRUSAGLIE — DOVE L'INGLESE APPIATTISCE CINQUE RIGHE
    # =====================================================================
    # ⭐⭐⭐ Testa condivisa da quattro righe su cinque, tenuta identica:
    #    «di una creatura, schizzat* via nel frantumare un nemico».
    #    Coda condivisa da tutte e cinque, tenuta identica:
    #    «Gran valore non ne ha/hanno, ma ... e così si vende/vendono a un
    #    prezzo discreto».
    #    In mezzo, l'unica cosa che il giapponese fa variare: l'uso.

    # 使用できる — l'osso e il cuore, giapponese identico nella frase d'uso.
    108519: "Schegge d'osso di una creatura, schizzate via nel frantumare un nemico. Gran valore non ne hanno, ma si usano per le pozioni e per la stregoneria, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    108581: "Il cuore di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si usa per le pozioni e per la stregoneria, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # 加工できる — l'occhio, il sangue e la pelle: materia prima, non ingrediente.
    # ⓘ 装飾品 -> «ornamenti» (dizionario: la collana misera e il lume).
    #   薬 nudo -> «medicine», che non e' 水薬 «pozione».
    108643: "L'occhio di una creatura, schizzato via nel frantumare un nemico. Gran valore non ne ha, ma si lavora in ornamenti e in medicine, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ⚠️ L'unica delle cinque che non schizza via: 集めたもの, si raccoglie.
    108705: "Il sangue di una creatura, schizzato via e raccolto. Gran valore non ne ha, ma si lavora in pozioni e simili, e così si vende a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ⓘ 皮 EN «skin patches»: «lembi di pelle», che e' anche il perche' del
    #   plurale contro il singolare del nome dell'oggetto.
    108767: "Lembi di pelle di una creatura, schizzati via nel frantumare un nemico. Gran valore non ne hanno, ma si lavorano in vestiti e in borse, e così si vendono a un prezzo discreto. \\n#~Le Mille Cianfrusaglie che Amo~",
}
