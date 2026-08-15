import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # *com_shape_change — «Cambia immagine» (:11825-:11852)
    # ================================================================
    # ⭐ Firma condivisa dai TRE menu (:11825, :12034, :12276): una resa sola
    #    li serve tutti. Riga senza valore appeso (get_pic_selection:11407 le
    #    da' rtval = -2), quindi l'imbottitura non incolonna niente — ma lo
    #    spazio in coda ci va lo stesso, per la regola qui sotto.
    (11825, 'Done    '): 'Conferma ',
    # 「元々の姿にする」 = «riportalo all'aspetto di prima». Senza valore
    #    (get_pic_selection:11410, rtval = -3): larghezza libera.
    (11825, 'Original'): 'Originale',
    # ⚠️ L'unica riga di questo menu che porta un numero (rtval = 100), quindi
    #    l'unica col tetto: 8 + ' 123' = 12 caratteri = 86 px, dentro i 111.
    #    «applica:Pic_» ne farebbe 12 e con il numero sfonderebbe.
    (11825, 'apply:Pic_'): 'usa:Pic_',
    # ⭐ 「個別画像の変更」: il titolo della finestra. Il piatto di sfondo
    #    (module.hsp:4328) parte da 171 px e cresce solo oltre i 15 caratteri.
    (11849, 'Appearance'): 'Cambia immagine',
    # ⚠️⚠️ 39 caratteri di tetto, l'inglese ne usa 38. Questa ne fa 34.
    #    Vedi il docstring. La forma viene da text.hsp:115.
    (11849, 'Right,left [Change]  Shift,Esc [Close]'):
        'Dx,Sx [Cambia]  Shift,Esc [Chiudi]',
    # ⚠️ Stesso giapponese di :12297 («Part»): la rete 4 pretende una resa
    #    sola, e «Voce» regge sopra tutt'e due gli elenchi.
    (11852, 'Category'): 'Voce',

    # ================================================================
    # *com_portrait_loop — «Cambia aspetto», pagina 0 (:12034-:12039)
    # ================================================================
    # ⚠️ Righe CON valore: tutte a DIECI colonne, o i numeri non si
    #    incolonnano piu'. Vedi il docstring.
    (12034, 'Portrait'): 'Ritratto  ',
    (12034, 'Hair    '): 'Capelli   ',
    (12034, 'Sub Hair'): 'Capelli 2 ',
    # ⚠️ «Col.capel.» riempirebbe tutte e dieci le colonne senza lasciare lo
    #    spazio in coda: abbreviata di due caratteri perche' la regola dello
    #    spazio finale vale per tutta la colonna. Vedi il docstring.
    (12034, 'Hair CL '): 'Col.cap.  ',
    (12034, 'Body    '): 'Corpo     ',
    (12034, 'Cloth   '): 'Veste     ',
    (12034, 'Pants   '): 'Pantaloni ',
    # ⭐ Riga SENZA valore (portrait_item:11357, rtval = -1): e' la sola
    #    ragione per cui upstream ha potuto scriverci dieci caratteri.
    #    Cambia pagina, e fa coppia con «Di base» di :12044.
    (12034, 'Set Detail'): 'Dettagli',
    # ⚠️ Porta un valore (cbit CHARA_BIT_PCC, 0 o 1): dieci colonne anche lei.
    #    「ｶｽﾀﾑｷｬﾗ」 accende il PCC su un alleato al posto dello sprite fisso.
    (12036, 'Custom  '): 'Su misura ',
    (12039, 'Riding  '): 'A cavallo ',

    # ================================================================
    # *com_portrait_loop — pagina 1, i colori (:12044)
    # ================================================================
    # 💡 Famiglia «Col.», con il nome abbreviato solo dove il tetto lo impone.
    (12044, 'Body CL '): 'Col.corpo ',
    (12044, 'Cloth CL'): 'Col.veste ',
    (12044, 'Pants CL'): 'Col.pant. ',
    # ⭐ 「アクセサリ」 dice «accessorio»; l'inglese «Etc» dice meno. E' una
    #    statica, nessun contratto di funzioni: la resa segue il giapponese.
    (12044, 'Etc1    '): 'Access. 1 ',
    (12044, 'Etc2    '): 'Access. 2 ',
    (12044, 'Etc3    '): 'Access. 3 ',
    (12044, 'Eyes    '): 'Occhi     ',
    # ⭐ Riga senza valore (portrait_item:11397): larghezza libera.
    (12044, 'Set Basic'): 'Di base',
    # ⚠️ Stesso inglese di :11849 e di :6062, tre giapponesi diversi.
    (12064, 'Appearance'): 'Cambia aspetto',

    # ================================================================
    # *com_mirror_loop — «Parti da nascondere» (:12276-:12297)
    # ================================================================
    # ⚠️⚠️ Qui l'imbottitura e' l'UNICO separatore: :12333 e :12336 fanno
    #    s += "On" / s += "Off" senza spazio davanti. Nove colonne, non otto,
    #    perche' «Mantello» ne riempie gia' otto da sola.
    (12276, 'Chest   '): 'Corazza  ',
    (12276, 'Leg     '): 'Gambali  ',
    (12276, 'Belt    '): 'Cintura  ',
    (12276, 'Glove   '): 'Guanti   ',
    (12276, 'Mantle  '): 'Mantello ',
    (12295, 'Parts to hide'): 'Parti da nascondere',
    # ⚠️ Stesso giapponese di :11852. Vedi sopra.
    (12297, 'Part'): 'Voce',
}
