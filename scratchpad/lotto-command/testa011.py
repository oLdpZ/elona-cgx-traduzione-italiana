# -*- coding: utf-8 -*-
"""Lotto `command-011`: i 28 pensieri di `*com_knowOther`, seconda meta' — e
`*com_knowOther` e' chiuso.

Segue il `command-010` nella stessa cascata di `if`, e prende i blocchi che
parlano di quando il compagno **sta male**: stamina a terra, vita sotto un
quarto, e le tredici condizioni (cecita', ubriachezza, immobilizzazione,
paralisi, ira, confusione, ottundimento, lavaggio del cervello, veleno,
malattia, paura, soffocamento, sonno, follia).

⭐ **E l'ultima riga vince su tutte: `:1783` e' `if ( tc == CHARA_PLAYER )`.**
Quando il bersaglio della telepatia sei tu, il gioco butta via qualunque
pensiero avesse scelto e stampa 「自分の心を覗くのは奇妙な感じだ」. Una battuta
sola, e sta in fondo alla cascata proprio per sovrascrivere le altre
ventisette.

⭐⭐ **Due pensieri dipendono dal MASOCHISMO del compagno, non dalla sua vita.**
Con la vita sotto un quarto il blocco tira `rnd(3)`, ma poi `:1721` e `:1724`
guardano `CDATA_MASTER_SERVANT2`: sopra +5 esce 「痛い痛い嫌だ死にたくない」 —
il panico — e sotto -5 esce 「なんだかゾクゾクする」, cioe' che la cosa gli
**piace**. Le due rese vanno tenute lontane l'una dall'altra come le tiene il
sorgente: «Ahi ahi no non voglio morire» contro «Che brivido...».

⭐ **`:1750` e' in KATAKANA, e il katakana qui e' la voce.** 「命令ヲ実行スル」 e'
「命令を実行する」 scritto tutto in katakana, che in giapponese e' la lingua dei
robot e delle cose senza volonta': la condizione e' il **lavaggio del
cervello**. L'inglese lo appiattisce in «Trying to execute the order». ✅ In
italiano il maiuscolo fa lo stesso mestiere: «ESEGUO L'ORDINE».

⚠️ **Un errore di monte**: `:1703` 「なんかどうでもよくなってきた」 e' «comincia a
non importarmi piu' niente» — l'apatia della stanchezza — e l'inglese scrive
«It keeps getting more difficult...», che parla di fatica invece che di
disinteresse.

💡 `:1732` 「なんだか愉快♪」 tiene la **crome**, che l'inglese butta via
(«Somewhat funny»): e' l'ubriachezza, e la nota dice il tono meglio
dell'aggettivo. `guardie.py` la lascia passare apposta — e' l'unica eccezione
alla regola sulla doppia larghezza.

Tetto 52 caratteri (`:1784`); la resa piu' lunga ne fa 39. Zero copie da
`dossier.py`.
"""
