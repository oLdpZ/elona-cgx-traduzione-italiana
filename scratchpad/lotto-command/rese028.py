import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :4436 il desiderio che parte in rete (net_send, :4439).
    (4436, '  goes wild with joy, \\"!!\\" '):
        'cdatan(CDATAN_AKA, CHARA_PLAYER) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) '
        '+ " esulta di gioia, \\"" + inputlog + "!!\\" " + cnven(txtcopy)',

    # --- :4449-:4460 la dea dei desideri.
    # ⭐ stesso inglese di proc.hsp:14492
    (4449, 'The power of the Wish Goddess does not seem to reach here...'):
        'Nemmeno il potere della dea dei desideri arriva fin qui...',
    # ⚠️⚠️ l'inglese ha perso una negazione: 「神力に余裕がない」 dice che alla dea
    #    NON avanzano forze, e infatti la riga blocca il desiderio. Si segue il
    #    giapponese. Vedi il docstring.
    (4454, 'It seems that even the Wish Goddess can afford to use her powers now...'):
        'Nemmeno la dea dei desideri ha forze da spendere, adesso...',
    # lo spazio in coda è la giuntura con la finestra di input
    (4460, 'What do you wish for? '): 'Che cosa desideri? ',

    # --- :4465 NON si traduce: è la frase che il giocatore ha appena digitato,
    #     rimandata a schermo. Fuori da inputlog non c'è nessuna parola.
    #     Dichiarata in invariati.md, sezione «non c'è niente da rendere».
    (4465, '!!'): 'cnvtalk(inputlog + "!!")',

    # --- :4478-:4486 le tre risposte scherzose.
    (4478, "I don't quite understand what you're saying underwater..."):
        'Sott\'acqua fai solo glu glu, non ci capisco niente...',
    # ⚠️⚠️ l'inglese capovolge la chiusa: 「聞かなかったことにしてね」 è «fa' finta di
    #    non aver sentito», non «listen to me». La dea si lascia sfuggire il
    #    segreto e se lo rimangia. ⭐ «il dio dentro» è db_creature.hsp:101284.
    (4482, "It must be rough for the god insi... Ah... There's no god inside!... Hey, listen to me!"):
        'Dev\'essere dura per il dio dentro... ah... ma quale dio dentro, non esiste '
        'nessun dio dentro!... Ehi, fa\' finta di non aver sentito.',
    (4486, 'It must be rough for the person inside.'):
        'Dev\'essere dura per la persona dentro.',

    # --- :4490-:4547 gli otto dèi che rispondono al proprio nome.
    #     ⭐ il registro di ciascuno è quello di action.hsp:14051-:14228.
    # Ehekatl, la gatta: raddoppia (action.hsp:14108, «Mi hai chiamata? Mi hai chiamata?»)
    (4490, 'Meeewmew!'): 'Miaomiaomiaaa!',
    # Lulwy, altezzosa: apre col sostantivo di disprezzo (action.hsp:14207, «Che ingenuità.»)
    (4497, 'How bold you are to summon me like this.'):
        'Che sfacciataggine, convocarmi così.',
    # Opatos, fragoroso: «Muahahah» è di action.hsp:14051
    (4504, 'Muwahaha! Here I am!'): 'Muahahahah! Eccomi qua!',
    # Kumiromi, timido: parla a puntini (action.hsp:14068)
    (4511, "I'm happy... that you summoned me..."):
        'Mi hai chiamato... che gioia...',
    # Mani, che comanda (action.hsp:14099)
    (4518, "You did well to summon me. I'll allow you the honor of worshiping me."):
        'Hai fatto bene a chiamarmi. Ti concedo il diritto di adorarmi.',
    # Itzpalt, solenne, al vocativo (action.hsp:14161)
    (4526, 'The engraving upon your soul... This too is part of the fate spun by the Element.'):
        'Imprimilo nella tua anima: anche questo è destino tessuto dall\'Elemento.',
    # Yacatect, commerciante in tono familiare (action.hsp:14116)
    (4533, "You call on me and I appear! What's up? Got a business transaction for me?"):
        'Se mi chiami, arrivo subito! Allora? C\'è un affare da fare?',
    # Jure, che balbetta e nega (action.hsp:14058, «N-non è mica per te...»)
    (4540, "I-it's not like I wanted to come or anything! It's not!"):
        'N-non è mica che volessi venire, sai! Per niente!',
    # ⭐ la creatura quantistica: db_creature.hsp rende 「きゅう…」 «Quu...», ed è una
    #    delle tredici divergenze volute di `battute --divergenti`.
    (4547, 'q!'): 'Quu!',

    # --- :4554-:4570 il desiderio banale e il cambio di alias.
    (4554, 'A typical wish.'): 'Mmh... ti accontenti di poco.',
    # 「だめよ。」: in modalità mago il desiderio è rifiutato, e il giapponese lo
    # dice; l'inglese ci mette una risata.
    (4563, '*laugh*'): 'Neanche per idea.',
    # ⭐ «Alias» è il termine della scheda del personaggio, command.hsp:10504
    (4566, "What's your new alias?"): 'Qual è il tuo nuovo alias?',
    (4570, 'You will be known as <>.'):
        '"D\'ora in poi ti chiameranno <" + cmaka + ">."',
}
