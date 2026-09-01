# -*- coding: utf-8 -*-
"""Le rese del lotto 065 — GLI ANELLI: `FILTER_ACCESSORY_RING` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 065 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa065.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 065`: **11 righe su 11** con lo spazio prima del `\\n`,
11 su 11 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 065`: **+11** per 11 rese,
nessuna gemella. ⓘ `_gia-reso.py 065`: 0 su 11.

⚠️⚠️⚠️ **`:99162` E' LA RIGA SORELLA DI `:99448`, CHIUSA NEL LOTTO DI VENTI
MINUTI FA.** Il giapponese e' identico parola per parola tranne **首輪 -> 指輪**:
l'anello nuziale e l'amuleto nuziale sono la stessa frase. Le due rese sono la
stessa frase anche in italiano, e cambia solo il nome dell'oggetto. ⚠️ Nessuno
strumento lo dice — `_gia-reso` cerca la prosa intera e conta 0 su 11 — ed e'
esattamente la forma del guasto della 121a: due lotti della stessa sessione.
"""

IT = {
    # =====================================================================
    # LA RIGA SORELLA DEL LOTTO 064
    # =====================================================================
    # ⭐⭐⭐ :99448 (064)  婚礼の儀において…送られる愛のこめられた**首輪**。
    #    :99162 (065)  婚礼の儀において…送られる愛のこめられた**指輪**。
    #    Identiche in giapponese tranne una parola, identiche in italiano
    #    tranne una parola. Se le due rese divergessero, il giocatore
    #    leggerebbe due testi diversi per la stessa cosa.

    99162: "Un anello carico d'amore, che nel rito nuziale si dona a chi diventa compagno di vita. È chiaro che da quel momento l'anello appartiene a lui, e a strapparglielo per forza ci si tira addosso una collera furiosa. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # GLI ANELLI COMUNI
    # =====================================================================
    # ⓘ L'indice 3 gia' in gioco dice «Un cerchio da infilare al dito»: la
    #   descrizione lunga riprende quelle parole. 装具 e' l'oggetto che si
    #   indossa, non un ornamento — e infatti la riga distingue subito i
    #   semplici da quelli col potere dentro.
    99233: "Un oggetto a forma di cerchio che si infila al dito. Ce n'è di ogni specie: dai più semplici, buoni per le cerimonie, a quelli in cui è sigillato un potere magico grave. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # 装飾品 «ornamento» come nel lotto 064.
    99305: "Un anello fatto apposta per proteggere meglio il dito. Come ornamento vale poco, ma quando si tratta di difendersi è questo che conviene. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ⭐ より高みを目指した e' la stessa espressione di :89077 (l'elmo del
    #   saggio, lotto 063): «per puntare più in alto». Stessa resa.
    99377: "Un anello che punta più in alto mescolando materiali di ogni sorta. Siccome dura molto se ne vedono parecchi nati da tentativi arditi, e pare che costino un po' più dei soliti. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    130385: "Un anello reso bellissimo da ornamenti d'ogni sorta. Dicono che un tempo gli artigiani si sfidassero a chi riuscisse a stipare più colore dentro quel piccolo cerchio. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # =====================================================================
    # I PEZZI UNICI 《…》 E I DUE ANELLI MAGICI
    # =====================================================================
    # ⓘ 螺旋 -> «spirale» (dizionario, «il re della spirale»). Il nome
    #   giapponese dell'oggetto e' ダブルヘリックス, la doppia elica: la
    #   descrizione ne e' il disegno, e le due linee vanno tenute.
    56737: "Un anello in cui abitano due forze diverse. Ha anche il compito di dare una mano alla capacità di rigenerarsi. Nel disegno, una linea rossa e una azzurra si intrecciano come una spirale. \\n# ~Dizionario Fantastico di Irva~",

    # 元素の神 -> «il dio degli elementi», gia' in gioco sul busto che lo
    # raffigura.
    75581: "Un anello che sigilla il potere magico, nato dal dio degli elementi. Tiene a bada anche un potere magico immenso. \\n# ~Dizionario Fantastico di Irva~",

    # ⭐ 老化するという弊害はない: nel gioco l'accelerazione fa invecchiare, e
    #   la riga dice che questo anello no. E' un fatto di gioco, non una
    #   figura: va detto chiaro. 〜のこめられた -> «racchiuso», come nel 064.
    86671: "Un anello in cui è racchiuso un potere magico che tiene una persona sempre accelerata. Non ha la controindicazione di far invecchiare, e pare che molti avventurieri se ne servano volentieri. \\n# ~Dizionario Fantastico di Irva~",

    # ⓘ L'indice 3 dice «Un anello che non fa rallentare col brutto tempo»:
    #   il corpo racconta il come, e i due si leggono nello stesso pannello.
    93627: "Un anello che sente il clima intorno e fa effetto quando il tempo si guasta. In quel momento, dicono, manda una luce morbida e crea attorno a sé un campo di forza che tiene la calma. \\n# ~Dizionario Fantastico di Irva~",

    # 気品 -> «eleganza», che e' la parola del gioco («Eleganza [clientela
    # migliore]»). L'indice 3 parla invece di 運勢, la fortuna: sono due
    # cose diverse e restano due parole diverse.
    107181: "Un anello piccolo e grazioso, che porta una gemma verde-azzurra. Dicono che, con una forza nascosta, alzi l'eleganza di chi lo possiede. \\n# ~Catalogo d'Arte di Lumiest~",

    # 鋼鉄竜 -> «drago d'acciaio» (dizionario: <Corgon> il drago d'acciaio),
    # ed e' anche il nome italiano dell'oggetto. 武骨 -> «rozzo», come nella
    # gorgiera del lotto 064.
    107390: "Un anello rozzo, che dicono ricavato dalle ossa di un drago d'acciaio. A portarlo si acquista una forza tanto immensa da far credere di essere diventati un drago d'acciaio. \\n# ~Dizionario Fantastico di Irva~",
}
