# -*- coding: utf-8 -*-
"""Le rese del lotto 059 — I LIBRI: `FILTER_ITEM_BOOK` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 059 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa059.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Forma, da `_forma.py 059`: qui la spaziatura **non e' uniforme in nessuno
dei due punti**, ed e' la prima volta in questa serie di lotti.
  - senza lo spazio prima del `\\n`: `:47220`, `:57577`, `:71100`, `:93292`;
  - senza lo spazio dopo il `#`: `:47220`, `:47222`, `:57577`, `:83697`.
Le due liste **non coincidono**: le code sono copiate una per una da
`_code.py 059`, non ricostruite.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 059`: **+24 per 23 rese**.
C'e' una **gemella**: `:129580` copre anche `:129651`, che sta fuori dal lotto.
ⓘ `_gia-reso.py 059`: 0 su 23. `_code.py 059`: 0 righe senza resa in tabella.
"""

IT = {
    # =====================================================================
    # I QUATTRO DIARI «したためたとされる» — la formula che non cambia
    # =====================================================================
    # ⭐ 「◯がしたためたとされる日記。」 si ripete QUATTRO volte, e cambia
    #    una parola sola. La resa e' «Un diario che si dice vergato da ◯.»
    #    in tutte e quattro. ⚠️ E tre di loro chiudono anche con la stessa
    #    seconda meta' — 中には… が事細かに書かれているという — resa
    #    «Dentro, a quanto pare, … per filo e per segno.»
    # ⚠️ `:97200` NON e' della serie: il giapponese li' dice 妹が書いた日記,
    #    «il diario che ha scritto», senza したためたとされる. La resa lo
    #    tiene distinto, perche' a distinguerlo e' l'originale.

    56055: "Un diario che si dice vergato dal maggiordomo. Dentro, a quanto pare, la vita del padrone è raccontata per filo e per segno più della sua. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    71100: "Un diario che si dice vergato da qualcuno. Di regola sulla copertina il nome non c'è, e finché non si guarda dentro non si sa di chi sia. Corre voce che, letta una dozzina abbondante di copie, salti fuori un autore raro.\\n# ~Il Libro dei Libri: i Libri per Bambini~",

    76935: "Un diario che si dice vergato dalla sorella maggiore. Dentro, a quanto pare, le sue fatiche e i suoi sentimenti sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    89284: "Un diario che si dice vergato dalla signorina. Dentro, a quanto pare, la sua vita sfavillante e qualcuno dei suoi passatempi graziosi sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # =====================================================================
    # I DUE DIARI SEGRETI — giapponese identico tranne una parola
    # =====================================================================
    # ⭐ 姉の秘密が隠された日記 e 妹の秘密が隠された日記 hanno la SECONDA
    #    META' identica byte per byte. Le due rese cambiano «maggiore» /
    #    «minore» e nient'altro: la sorella cane e la sorella gatta stanno
    #    una accanto all'altra nell'inventario.

    76791: "Un diario in cui la sorella maggiore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    89356: "Un diario in cui la sorella minore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ⚠️⚠️ IL GIAPPONESE QUI E' VUOTO. `db_item.hsp:89352` dice
    #    `description(2) = ""` nel ramo `if ( jp )`: il segmento lo ha
    #    soltanto l'inglese. E' il caso della 110a («il giapponese VUOTO...
    #    la riga si rende com'e'»), NON quello della rinviata `:129299`,
    #    dove il testo non ce l'aveva nessuna delle due lingue.
    # ⭐ «Nyo reading!» e' il bisticcio del gatto sulla copertina del diario
    #    segreto della sorella GATTA minore. Il tic e' gia' reso nel
    #    dizionario, ed e' «miao» in coda alla frase.
    89358: "\\\"Vietato leggere, miao!\\\" \\n# ~parole sulla copertina~",

    # ⚠️ 妹が書いた日記: fuori dalla serie, e la resa lo dice.
    97200: "Il diario che ha scritto la sorella minore. Dentro ci sono le cose che sente giorno per giorno, quel che le piace di questi tempi, i cibi che ha trovato buoni: e scrive saltando due giorni per volta. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # =====================================================================
    # I DUE LIBRI COMUNI — stessa apertura, e una GEMELLA
    # =====================================================================
    # ⭐ ノースティリスで広く流通している記録媒体。apre tutt'e due, e la resa
    #    e' la stessa parola per parola. 記録媒体 e' un tecnicismo secco —
    #    «supporto di registrazione» — ed e' la battuta: l'enciclopedia
    #    parla del libro come di un dispositivo.
    # ⚠️ `:129580` e' la GEMELLA di `:129651` (ITEM_ID_BOOK), che sta fuori
    #    dal lotto: una resa copre due righe, e `applica` sale di 24.

    50816: "Un supporto di registrazione che a Tyris del Nord circola parecchio. Semmai, più del contenuto tende a contare il volume. A darlo a un negozio, la fama dell'autore salirà. \\n# ~Il Libro dei Libri~",

    129580: "Un supporto di registrazione che a Tyris del Nord circola parecchio. Ce n'è qualcuno in cui sta scritto qualcosa d'importante, ma quasi tutti valgono sì e no quanto un appunto a margine. \\n# ~Il Libro dei Libri~",

    # =====================================================================
    # IL LIBRO ORRIBILE, e il foglietto infilato dentro
    # =====================================================================
    # ⚠️ :47220 e' senza lo spazio prima del \\n E senza quello dopo il #.
    #    深淵 e' l'«Abisso», e l'indice 3 gia' reso dice «la magia dell'Abisso».
    47220: "Si dice che compaia davanti a chi ha la sua stessa lunghezza d'onda. Freddo non è, eppure a tenerlo in mano la schiena si gela in modo innaturale, e ti prende la sensazione che qualcuno ti stringa l'anima nel pugno. Le pagine sono tutte nere e semitrasparenti, ma alla luce vi affiorano caratteri strani. È fatto di una materia che non è di questo mondo, e c'è chi sostiene che in verità non sia un libro, ma una finestra che riflette l'Abisso.\\n#~Dizionario Fantastico di Irva~",

    # 「私は　利用されていた」 — lo spazio a tutta larghezza e' una pausa, e
    #   in italiano si scrive coi tre punti (il carattere … e' proibito).
    #   ⓘ «uno strumento» tiene 利用 e non obbliga a un genere che la riga
    #   non dichiara.
    47222: "\\\"Io... ero solo uno strumento\\\" \\n#~Scarabocchio sul Foglietto Infilato Dentro~",

    # =====================================================================
    # GLI ALTRI
    # =====================================================================
    51150: "Un libro che un pescatore ha scritto per farsi più compagni di pesca. Pare che a scriverlo abbia messo a frutto le attese fra un pesce e l'altro. \\n# ~Il Libro dei Libri~",

    # 掲示板 e' la «bacheca», e 依頼 sono gli «incarichi» (il nome dell'oggetto).
    51221: "Un taccuino che un padre aveva preparato. Pare che, in pensiero per il figlio, gliel'avesse infilato di nascosto nei bagagli. Se sia caduto, buttato o dimenticato non si sa: stava lì accanto alla bacheca. \\n# ~Il Libro dei Libri~",

    # ⭐ 開発主任 non e' «un capo progetto» qualunque: e' `<Gavela> l'ingegnere
    #   capo`, un personaggio, e il dizionario lo chiama sempre cosi'.
    56201: "Un rapporto scritto dall'ingegnere capo. Da qui voleva partire per aprire una ricerca, ma pare che il budget, purtroppo, non sia mai arrivato. \\n# ~Il Libro dei Libri~",

    # ⚠️ :57577 e' senza lo spazio prima del \\n E senza quello dopo il #.
    #   シルフ sono le «silfidi», e la frase gemella e' gia' in gioco: Lulwy
    #   dice «l'ho fatto a pezzi e dato in pasto alle silfidi».
    57577: "Un album di foto in cui le immagini sexy di Lulwy sono stipate a non finire. Così spinte che l'occhio ci cade da solo, quali che siano i gusti. Lo pubblicò un fotografo che una volta era riuscito a metterla di buon umore, e si dice che abbia continuato a venderlo finché non fu proibito. Più tardi il fotografo propose un secondo volume, ma le guastò l'umore per sbadataggine e finì in pasto alle silfidi.\\n#~Il Libro dei Libri: le Riviste per Adulti~",

    62534: "Il taccuino di un ricercatore che non era contento dell'istituto per cui lavorava. Ci sono annotate le malefatte di chi gli stava intorno, e i lamenti che ne faceva. \\n# ~Il Libro dei Libri~",

    # ⭐⭐ カイン: l'inglese scrive «a mad man named Cain», ma il nome che il
    #   giocatore legge in gioco e' `<Caim> il riccone folle` — dodici voci
    #   del dizionario, nessuna con la n.
    74101: "Il diario che <Caim>, impazzito, ha scarabocchiato. Ci sta scritta la verità che in fondo alla sua follia ha conosciuto... o almeno così sembra. \\n# ~Il Libro dei Libri~",

    # ⭐ 真実であり、真っ赤な嘘である: e' l'epigrafe dei Libri di Bokonon di
    #   Vonnegut, che in italiano suona «spudorate menzogne». ⚠️ L'inglese
    #   qui butta la seconda meta' e ci mette «granfalloon», che il
    #   giapponese non nomina.
    81064: "Il libro sacro che innalza una congrega ritenuta stranissima. Aprendone le pagine saprai che quel che vi sta scritto è la verità, ed è una menzogna spudorata. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ⚠️ :83697 ha lo spazio prima del \\n ma NON dopo il #.
    #   ⭐ 失われた存在 / 生命が失われた: il giapponese ripete il verbo, e la
    #   resa ripete «perduto/perdute».
    83697: "Un libro prezioso che si dice richiami indietro chi è andato perduto. Per ironia, nell'antichità intorno a questo libro ci fu una grande guerra, e si dice che molte vite andarono perdute. \\n#~Il Libro dei Libri: i Grimori~",

    84233: "Un libro in cui è scritto come vanno le cose in città. Siccome però a Tyris del Nord si tiene alla libertà, pare che questo libro, che descrive dei regolamenti, sia diventato un ingombro inutile. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ⭐ レイチェル e' «Rachel» ed e' una DONNA: «la scrittrice di favole
    #   Rachel», «una raccolta di fiabe che scaldano il cuore, firmata
    #   Rachel». E i volumi sono quattro, come dice l'incarico di Renton.
    86403: "La raccolta di fiabe che ha fatto Rachel, la scrittrice di favole. Si dice che la scrittura e le illustrazioni, con quel loro calore tutto particolare, diano a chi legge qualcosa che tocca il cuore. I volumi sono quattro in tutto, ma metterli insieme è impresa difficilissima. Al mondo ci sarà di sicuro qualcuno che muore dalla voglia di leggerli. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ⚠️ :93292 e' senza lo spazio prima del \\n.
    #   技術 qui e' l'«abilità» della scheda, come dice l'indice 3 gia' reso
    #   («alza il potenziale di un'abilità scelta»).
    93292: "Un libro che, a leggerlo, allena l'abilità di cui parla. Si dice che nei villaggi di confine, dove una scuola non c'è, libri come questo facciano le veci del maestro.\\n# ~Il Libro dei Libri: i Manuali d'Insegnamento~",
}
