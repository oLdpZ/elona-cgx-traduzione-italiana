# -*- coding: utf-8 -*-
"""Le rese del lotto 047 — I GRIMORI, prima parte: il CORPO.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 047 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa047.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `scratchpad/lotti-113/_forma.py 047`: **6** righe su 44 hanno lo
spazio prima del `\\n` — sono le quattro dell'indice 2 piu' la ricetta
(`:78727`) e il libro antico (`:85101`); le 38 dei grimori non ce l'hanno.

⚠️⚠️ Previsione di `applica`: **+44** per 44 rese. `_previsione.py 047` non
trova gemelle: 44 righe, 44 firme distinte.

⭐⭐⭐ Il nome dell'incantesimo NON si prende dal nome del libro: lo da'
`scratchpad/lotti-113/_incantesimo.py`, che passa dall'`efid` di
`DBMODE_ON_READ` e dallo `skillname()` di `skill.hsp`. Su `:91982` le due cose
divergono — il libro dice 「扉生成」, l'incantesimo si chiama ドア生成 /
`Door Creation` / **Crea porte** — e il nome del libro avrebbe dato al giocatore
una voce che nella lista degli incantesimi non esiste.
"""

IT = {
    # =====================================================================
    # I GRIMORI: 38 righe con la stessa testa formulaica
    #   「〜という呪文について学ぶことができる魔法書。〜なあなたに。」
    # La prima frase e' identica in tutte e 38 e si scrive identica; la
    # seconda e' una dedica in seconda persona (あなたに), che l'inglese
    # appiattisce in «For those who...» e che qui resta rivolta al lettore.
    # ⚠️ Il nome dell'incantesimo e' quello di `skill.hsp`, maiuscolo e senza
    #    virgolette, come «la magia Piuma» gia' in `chat.hsp`.
    # =====================================================================

    # --- le magie ad area -------------------------------------------------
    47359: "Un grimorio su cui studiare l'incantesimo Vortice di tuoni. Per te che, quando ti arrabbi, vuoi far cadere i fulmini.\\n#~Il Libro dei Libri: i Grimori~",

    47432: "Un grimorio su cui studiare l'incantesimo Gabbia d'eclissi. Per te che nel buio senti il mistero.\\n#~Il Libro dei Libri: i Grimori~",

    47505: "Un grimorio su cui studiare l'incantesimo Ruggito d'oltretomba. Per te che vuoi regnare sull'inferno.\\n#~Il Libro dei Libri: i Grimori~",

    47578: "Un grimorio su cui studiare l'incantesimo Tempesta velenosa. Per te che vuoi spargere veleno dappertutto.\\n#~Il Libro dei Libri: i Grimori~",

    47651: "Un grimorio su cui studiare l'incantesimo Tempesta di bolle. Per te che ami le bolle di sapone.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ l'inglese chiama l'incantesimo 'Dreaming Roar', ma lo skillname e'
    #    夢幻の咆哮 / Illusion Roar: il nome buono e' quello della lista.
    47724: "Un grimorio su cui studiare l'incantesimo Ruggito illusorio. Per te che sogni a occhi aperti.\\n#~Il Libro dei Libri: i Grimori~",

    47797: "Un grimorio su cui studiare l'incantesimo Gabbia d'angoscia. Per te che sei un sadico.\\n#~Il Libro dei Libri: i Grimori~",

    # --- le saette --------------------------------------------------------
    47870: "Un grimorio su cui studiare l'incantesimo Saetta d'oltretomba. Per te che hai qualcuno da mandare all'inferno.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 毒々しい non e' «tossico» (l'inglese dice «For genuinely toxic
    #    people»): e' il colore acceso e sgradevole di chi sembra velenoso.
    47943: "Un grimorio su cui studiare l'incantesimo Saetta velenosa. Per te che ami le cose dai colori velenosi.\\n#~Il Libro dei Libri: i Grimori~",

    48016: "Un grimorio su cui studiare l'incantesimo Saetta sonora. Per te che ami il baccano.\\n#~Il Libro dei Libri: i Grimori~",

    48089: "Un grimorio su cui studiare l'incantesimo Saetta caotica. Per te che stai più tranquillo quando è tutto in disordine.\\n#~Il Libro dei Libri: i Grimori~",

    48162: "Un grimorio su cui studiare l'incantesimo Saetta dei nervi. Per te che credi che l'amore sia proprio il dolore.\\n#~Il Libro dei Libri: i Grimori~",

    # --- le frecce --------------------------------------------------------
    48235: "Un grimorio su cui studiare l'incantesimo Artiglio di fuoco. Per te che vuoi lasciare cicatrici bollenti.\\n#~Il Libro dei Libri: i Grimori~",

    48308: "Un grimorio su cui studiare l'incantesimo Lama di gelo. Per te che resti freddo e imperturbabile.\\n#~Il Libro dei Libri: i Grimori~",

    # ⭐ 痺れさせる e' tutt'e due le cose — intorpidire e far restare a bocca
    #    aperta — e «folgorare» in italiano le tiene tutt'e due.
    48381: "Un grimorio su cui studiare l'incantesimo Lancia di fulmine. Per te che vuoi lasciare tutti folgorati.\\n#~Il Libro dei Libri: i Grimori~",

    48454: "Un grimorio su cui studiare l'incantesimo Spina mentale. Per te che vuoi prenderti gioco del nemico con le allucinazioni.\\n#~Il Libro dei Libri: i Grimori~",

    48527: "Un grimorio su cui studiare l'incantesimo Muco velenoso. Per te che ti interessi alle creature velenose.\\n#~Il Libro dei Libri: i Grimori~",

    48600: "Un grimorio su cui studiare l'incantesimo Cannonata sonora. Per te che vuoi far volare via la gente a suon di musica.\\n#~Il Libro dei Libri: i Grimori~",

    48673: "Un grimorio su cui studiare l'incantesimo Zanna d'acqua. Per te che sai quanto l'acqua faccia paura.\\n#~Il Libro dei Libri: i Grimori~",

    # --- i grimori sparsi -------------------------------------------------
    # ⚠️ パワーストーン e' la pietra dei cristalloterapeuti, non una gemma del
    #    gioco: l'inglese dice «Healing Crystals» ed e' d'accordo.
    58993: "Un grimorio su cui studiare l'incantesimo Pietra protettrice. Per te che ti interessi ai cristalli e al loro potere.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 水芸 e' il gioco di prestigio con l'acqua, non la navigazione:
    #    l'inglese («watercraft») legge male la parola.
    61866: "Un grimorio su cui studiare l'incantesimo Saetta d'acqua. Per te che vuoi diventare maestro nei giochi d'acqua.\\n#~Il Libro dei Libri: i Grimori~",

    65600: "Un grimorio su cui studiare l'incantesimo Concentrazione. Per te che vuoi concentrarti su quello che hai davanti.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 体を軽くする e' alleggerire il corpo, non dimagrire: l'inglese
    #    («lose body weight») fa della levitazione una dieta.
    72957: "Un grimorio su cui studiare l'incantesimo Piuma. Per te che vuoi alleggerirti il corpo, almeno per un po'.\\n#~Il Libro dei Libri: i Grimori~",

    82077: "Un grimorio su cui studiare l'incantesimo Raccolto del mago. Per te che hai avuto una spesa imprevista dopo l'altra.\\n#~Il Libro dei Libri: i Grimori~",

    82150: "Un grimorio su cui studiare l'incantesimo Tasca quadridimensionale. Per te che di carattere non riesci a mettere in ordine.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 死神 e' «la Morte» in tutto il progetto (`buff.hsp`, la riga del
    #    patto: «stringe un patto con la Morte»), non «il mietitore».
    83555: "Un grimorio su cui studiare l'incantesimo Patto. Per te che vuoi fare amicizia con la Morte.\\n#~Il Libro dei Libri: i Grimori~",

    84440: "Un grimorio su cui studiare l'incantesimo Saetta magica. Per te che vuoi sparare raggi dalle dita.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il giapponese dice solo «i giorni di pioggia»: il vento di etere
    #    l'aggiunge l'inglese.
    84513: "Un grimorio su cui studiare l'incantesimo Tempesta magica. Per te che nei giorni di pioggia non stai in casa.\\n#~Il Libro dei Libri: i Grimori~",

    86940: "Un grimorio su cui studiare l'incantesimo Cuneo d'oscurità. Per te che vuoi darti un'aria da duro.\\n#~Il Libro dei Libri: i Grimori~",

    89010: "Un grimorio su cui studiare l'incantesimo Incognito. Per te che ami i dispetti.\\n#~Il Libro dei Libri: i Grimori~",

    # ⭐⭐⭐ il libro dice 「扉生成」, ma l'incantesimo si chiama ドア生成 /
    #    Door Creation, e in italiano e' «Crea porte» (`skill.hsp:709`).
    #    Il nome del libro qui non e' il nome dell'incantesimo.
    91982: "Un grimorio su cui studiare l'incantesimo Crea porte. Per te che vuoi aprire la porta del cuore di qualcuno.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 冷え症 e' il patire il freddo per costituzione, e 万年 dice che dura
    #    tutto l'anno.
    92870: "Un grimorio su cui studiare l'incantesimo Muro di fuoco. Per te che patisci il freddo tutto l'anno.\\n#~Il Libro dei Libri: i Grimori~",

    93222: "Un grimorio su cui studiare l'incantesimo Terreno acido. Per te che sei debolmente alcalino.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il nome del libro e' «mani guaritrici», ma l'incantesimo si chiama
    #    癒しの手 / Healing Touch / «Tocco curativo» (`skill.hsp:434`).
    94175: "Un grimorio su cui studiare l'incantesimo Tocco curativo. Per te che tratti tutti allo stesso modo, senza distinzioni.\\n#~Il Libro dei Libri: i Grimori~",

    94319: "Un grimorio su cui studiare l'incantesimo Pioggia curativa. Per te che ami i tuoi compagni.\\n#~Il Libro dei Libri: i Grimori~",

    94454: "Un grimorio su cui studiare l'incantesimo Crea muri. Per te che vuoi restare solo.\\n#~Il Libro dei Libri: i Grimori~",

    98649: "Un grimorio su cui studiare l'incantesimo Ragnatela. Per te che vuoi divertirti con decorazioni un po' strane.\\n#~Il Libro dei Libri: i Grimori~",

    98874: "Un grimorio su cui studiare l'incantesimo Dominio. Per te che vuoi fare amicizia con quella ragazza che ti piace.\\n#~Il Libro dei Libri: i Grimori~",

    # =====================================================================
    # LE DUE RIGHE CHE NON SONO GRIMORI
    # =====================================================================

    # ⓘ la ricetta e' 紙片, un «foglio»: non si legge, si usa e si consuma
    #    (glossario, 110a). 調理人 e' «il cuoco», come in `:117599`.
    # ⚠️ i puntini di sospensione si scrivono con tre punti.
    78727: "Un foglio dove stanno chiusi il gusto e le tecniche segrete dei cuochi. Con questo si può avere un sapere che non è da meno di quello di un cuoco di prima categoria. ...Poi, che la mano tenga il passo, è un altro discorso. \\n# ~I Comprimari della Cucina~",

    85101: "Un documento prezioso, dove sta scritto di tutto un po'. Si crede che, a decifrarlo, si possano sfiorare esseri superiori. \\n# ~Il Libro dei Libri: i Libri da Decifrare~",

    # =====================================================================
    # LE QUATTRO CITAZIONI DELL'INDICE 2
    # ⚠️ il giapponese e' vuoto: qui l'unica fonte e' l'inglese.
    # ⓘ «tomo» viene dal glossario (`a Eulderna Researcher handling this
    #    tome` -> «un ricercatore Eulderna che maneggia questo tomo»).
    # =====================================================================

    48237: "\\\"Ho trovato una nuova ragione per VIVERE.\\\" \\n# ~un piromane Eulderna~",

    # ⓘ «go brrr» e' il verso della stamperia di banconote: si tiene.
    82079: "\\\"Il Raccolto del mago fa brrr.\\\" \\n#Ufficio Eulderna degli Studi Dotti (UESD)",

    86942: "\\\"Pare che questo tomo pieghi la luce con cura.\\\" \\n#un ricercatore Eulderna",

    98651: "\\\"Giuro di aver visto dei ragni uscire da questo tomo.\\\" \\n#un ricercatore Eulderna",
}
