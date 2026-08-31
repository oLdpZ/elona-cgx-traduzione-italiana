# -*- coding: utf-8 -*-
"""Le rese del lotto 048 — I GRIMORI, seconda parte: la categoria si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 048 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa048.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `scratchpad/lotti-113/_forma.py 048`: **6** righe su 48 hanno lo
spazio prima del `\\n` — sono le quattro dell'indice 1 e le due dell'indice 2 —
e **nessuna** delle 48 code ha lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`: **+48** per 48 rese. `_previsione.py 048` non
trova gemelle: 48 righe, 48 firme distinte.

⭐⭐⭐ I nomi degli incantesimi vengono da
`scratchpad/lotti-113/_incantesimo.py 048`: 48 righe su 48 risolte, zero non
rese. Su **37 grimori su 80** il nome del libro e il nome dell'incantesimo non
coincidono (misurato da `scratchpad/_118-nomi-vs-incantesimi.py`): qui si scrive
il nome dell'**incantesimo** — vedi `testa048.py`.
"""

IT = {
    # =====================================================================
    # I GRIMORI: 42 righe con la testa formulaica della prima parte
    #   「〜という呪文について学ぶことができる魔法書。〜なあなたに。」
    # =====================================================================

    102037: "Un grimorio su cui studiare l'incantesimo Mutazione. Per te che vuoi cambiare te stesso.\\n#~Il Libro dei Libri: i Grimori~",

    103649: "Un grimorio su cui studiare l'incantesimo Percezione oggetti. Per te che vuoi fare il detective.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «conoscenza», l'incantesimo e' 知者の加護 / Divine Wisdom
    #    / «Saggezza divina» (`skill.hsp:689`).
    104519: "Un grimorio su cui studiare l'incantesimo Saggezza divina. Per te che stai per affrontare un esame.\\n#~Il Libro dei Libri: i Grimori~",

    104592: "Un grimorio su cui studiare l'incantesimo Incubo. Per te che finisci sempre per dormire troppo.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «pioggia sacra», l'incantesimo e' 全浄化 / Vanquish Hex /
    #    «Scaccia i malocchi» (`skill.hsp:444`).
    105228: "Un grimorio su cui studiare l'incantesimo Scaccia i malocchi. Per te che ti senti giù di morale.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 体調の優れぬ e' «non essere in forma». L'inglese scrive «For the
    #    hardcore exorcists», che nel giapponese non c'e' per niente.
    105301: "Un grimorio su cui studiare l'incantesimo Luce purificatrice. Per te che non ti senti in forma.\\n#~Il Libro dei Libri: i Grimori~",

    105525: "Un grimorio su cui studiare l'incantesimo Velo sacro. Per te che sei di salute delicata.\\n#~Il Libro dei Libri: i Grimori~",

    105669: "Un grimorio su cui studiare l'incantesimo Cicatrice elementale. Per te che vuoi sapere quanto la natura faccia paura.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «debolezza», l'incantesimo e' 脆弱の霧 / Mist of Frailness
    #    / «Nebbia di fragilità» (`skill.hsp:669`).
    105742: "Un grimorio su cui studiare l'incantesimo Nebbia di fragilità. Per te che hai un amico che si vanta troppo della sua forza.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ l'inglese butta la dedica e ci mette una battuta sua: «Strangely
    #    reading this book gives you a slight adrenalin rush».
    105886: "Un grimorio su cui studiare l'incantesimo Eroismo. Per te che vuoi crogiolarti nel sentirti un eroe.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 足を引っ張る e' «trattenere, ostacolare». L'inglese lo legge come
    #    «pull people's legs», prendere in giro: e' un'altra cosa.
    106181: "Un grimorio su cui studiare l'incantesimo Rallentamento. Per te che vuoi mettere i bastoni fra le ruote al rivale.\\n#~Il Libro dei Libri: i Grimori~",

    106254: "Un grimorio su cui studiare l'incantesimo Accelerazione. Per te che vuoi staccare il rivale.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «resistenza», l'incantesimo e' 属性保護 / Attribute Shield
    #    / «Scudo elementale» (`skill.hsp:649`).
    106398: "Un grimorio su cui studiare l'incantesimo Scudo elementale. Per te che vuoi difenderti da ogni sorta di pericolo.\\n#~Il Libro dei Libri: i Grimori~",

    106542: "Un grimorio su cui studiare l'incantesimo Rigenerazione. Per te che guarisci lentamente dalle ferite.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «silenzio», l'incantesimo e' 沈黙の霧 / Mist of Silence /
    #    «Nebbia di silenzio» (`skill.hsp:639`).
    106686: "Un grimorio su cui studiare l'incantesimo Nebbia di silenzio. Per te che hai un amico chiacchierone.\\n#~Il Libro dei Libri: i Grimori~",

    106839: "Un grimorio su cui studiare l'incantesimo Scudo sacro. Per te che tieni la guardia bassa.\\n#~Il Libro dei Libri: i Grimori~",

    # ⭐ l'unico dei 92 che apre con 珍しい魔法書, «un grimorio RARO»: e' il
    #    libro del desiderio, e l'inglese lascia cadere la parola.
    111850: "Un grimorio raro su cui studiare l'incantesimo Desiderio. Per te che credi nei miracoli.\\n#~Il Libro dei Libri: i Grimori~",

    112952: "Un grimorio su cui studiare l'incantesimo Vortice del caos. Per te che vuoi far casino a più non posso.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «onda di boato», l'incantesimo e' 轟音の波動 / Raging Roar
    #    / «Onda fragorosa» (`skill.hsp:594`).
    113025: "Un grimorio su cui studiare l'incantesimo Onda fragorosa. Per te che vuoi fare chiasso a tutto volume.\\n#~Il Libro dei Libri: i Grimori~",

    113098: "Un grimorio su cui studiare l'incantesimo Tempesta ardente. Per te che vuoi scaldare l'aria qui intorno.\\n#~Il Libro dei Libri: i Grimori~",

    113171: "Un grimorio su cui studiare l'incantesimo Onda di gelo. Per te che vuoi rinfrescare l'aria qui intorno.\\n#~Il Libro dei Libri: i Grimori~",

    113244: "Un grimorio su cui studiare l'incantesimo Saetta mentale. Per te che sai fare un occhiolino irresistibile.\\n#~Il Libro dei Libri: i Grimori~",

    113317: "Un grimorio su cui studiare l'incantesimo Saetta d'oscurità. Per te che hai uno sguardo che mette in soggezione.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «ago neurale», l'incantesimo e' 神経の針 / Nerve Needle /
    #    «Ago dei nervi» (`skill.hsp:489`).
    # ⚠️ l'inglese butta la dedica e scrive che fa tremare l'occhio.
    113459: "Un grimorio su cui studiare l'incantesimo Ago dei nervi. Per te che scambi facilmente un incontro qualunque per il destino.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 流し眼 e' l'occhiata di sottecchi, quella che si lancia di lato:
    #    l'inglese ne fa un problema agli occhi.
    113532: "Un grimorio su cui studiare l'incantesimo Occhio del caos. Per te che ti eserciti nello sguardo di sottecchi.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «sospiro infernale», l'incantesimo e' 地獄の吐息 /
    #    Nether Sigh / «Sospiro d'oltretomba» (`skill.hsp:484`).
    113605: "Un grimorio su cui studiare l'incantesimo Sospiro d'oltretomba. Per te che vuoi darti arie da demonio.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «freccia magica», l'incantesimo e' 魔法の矢 / Magic Dart /
    #    «Dardo magico» (`skill.hsp:479`).
    # ⚠️ e l'inglese butta la dedica: «Designed for beginners».
    114013: "Un grimorio su cui studiare l'incantesimo Dardo magico. Per te che vuoi toccare l'essenza della magia.\\n#~Il Libro dei Libri: i Grimori~",

    114350: "Un grimorio su cui studiare l'incantesimo Cura di Jure. Per te che vuoi scamparla per un pelo.\\n#~Il Libro dei Libri: i Grimori~",

    114423: "Un grimorio su cui studiare l'incantesimo Cura di Eris. Per te che vuoi tornare vivo per miracolo.\\n#~Il Libro dei Libri: i Grimori~",

    114496: "Un grimorio su cui studiare l'incantesimo Cura ferite gravi. Per te che, sfortunato come sei, negli incidenti ci finisci spesso.\\n#~Il Libro dei Libri: i Grimori~",

    114569: "Un grimorio su cui studiare l'incantesimo Cura ferite lievi. Per te che hai sempre addosso qualche ferita fresca.\\n#~Il Libro dei Libri: i Grimori~",

    114642: "Un grimorio su cui studiare l'incantesimo Ritorno. Per te che ti prende spesso la nostalgia di casa.\\n#~Il Libro dei Libri: i Grimori~",

    114715: "Un grimorio su cui studiare l'incantesimo Oracolo. Per te che ami farti predire il futuro.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «cartografia magica», l'incantesimo e' 魔法の地図 /
    #    Magic Map / «Mappa magica» (`skill.hsp:569`).
    114788: "Un grimorio su cui studiare l'incantesimo Mappa magica. Per te che ti perdi facilmente.\\n#~Il Libro dei Libri: i Grimori~",

    123357: "Un grimorio su cui studiare l'incantesimo Evoca mostri. Per te che ami gli animali.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ il libro e' «teletrasporto minore», l'incantesimo e' ショートテレポート
    #    / Short Teleport / «Teletrasporto breve» (`skill.hsp:459`).
    123492: "Un grimorio su cui studiare l'incantesimo Teletrasporto breve. Per te che camminare ti pesa.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ l'inglese butta la dedica e scrive che il tomo fa una scarica.
    128868: "Un grimorio su cui studiare l'incantesimo Saetta di fulmine. Per te che i fulmini li vorresti vedere sempre.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️ 寒がり e' «chi sente il freddo». L'inglese scrive «For those who
    #    catches the cold», il raffreddore: e' un'altra parola.
    128941: "Un grimorio su cui studiare l'incantesimo Saetta di fuoco. Per te che soffri il freddo.\\n#~Il Libro dei Libri: i Grimori~",

    129014: "Un grimorio su cui studiare l'incantesimo Saetta di gelo. Per te che soffri il caldo.\\n#~Il Libro dei Libri: i Grimori~",

    129724: "Un grimorio su cui studiare l'incantesimo Purificazione. Per te che credi che gli spiriti esistano.\\n#~Il Libro dei Libri: i Grimori~",

    129797: "Un grimorio su cui studiare l'incantesimo Identifica. Per te che hai il vizio di dubitare di tutto.\\n#~Il Libro dei Libri: i Grimori~",

    # ⚠️⚠️ 今すぐ旅に出たい e' «voglio partire subito». L'inglese scrive «For
    #    those who hates traveling»: il ROVESCIO della dedica.
    129870: "Un grimorio su cui studiare l'incantesimo Teletrasporto. Per te che vuoi partire per un viaggio subito.\\n#~Il Libro dei Libri: i Grimori~",

    # =====================================================================
    # LE SEI CITAZIONI, DOVE IL GIAPPONESE DICE UN'ALTRA COSA
    # ⚠️⚠️ Le quattro dell'indice 1 hanno per giapponese il TASSELLO DEL
    #    RANGO — `<ランク6魔法>`, `<ランク3魔法>` — e per inglese una battuta.
    #    Non sono due versioni della stessa riga: sono due contenuti diversi
    #    nello stesso posto. La build e' il ramo `en`, e la stringa che il
    #    giocatore legge e' quella inglese: si rende quella. Il rango resta
    #    non scritto, come dalla 110a.
    # =====================================================================

    113027: "\\\"Giuro che ho appena sentito qualcosa.\\\" \\n#un ricercatore Eulderna che tiene in mano questo tomo",

    113099: "\\\"Ahi! Scotta!\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    113100: "\\\"I-io volevo solo accendere una fiamma nel suo cuore...\\\" \\n#un incendiario in arresto",

    113172: "\\\"Iiih! Gela!\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    113245: "\\\"Mi fanno male gli occhi, e la testa ancora di più...\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    113460: "\\\"Secondo la mia teoria è una magia sonora che fa il rumore delle unghie sulla lavagna.\\\" \\n#un ricercatore Eulderna ripudiato",
}
