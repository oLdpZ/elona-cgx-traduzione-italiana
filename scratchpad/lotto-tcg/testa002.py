# -*- coding: utf-8 -*-
"""Lotto fase4-tcg-002: l'editor del mazzo, e **chiude `tcg.hsp`**
(tcg.hsp, righe 2781-9999).

28 firme su 64 chiavi — le 34 chiavi in piu' sono «Elenco» e «Mazzo», le due
schede della colonna, riscritte in **diciassette** righe (`:3544`-`:3632`), una
per ogni tipo di filtro.

⭐⭐ **Questo lotto non sarebbe stato scrivibile ieri.** Contiene tre coppie che
la rete 4 vecchia avrebbe bocciato, perche' raggruppava per **giapponese** e
pretendeva una resa sola:

    :2781 / :2786 / :2791   「また今度ね」   «Maybe next time.» / «To the
                            Amur-cage you go!» / «Noooooooooooooo!»
    :4432 / :4433           「降参する」     «Surrender» / «No»
    :4424 / :4433           「いいえ」       la stessa firma in due menu

Sono tre punti dove chi ha scritto il mod ha riusato il primo argomento di
`lang()` senza toccarlo. La rete corretta oggi raggruppa per
`(giapponese, inglese, firma)` e li lascia passare dicendolo in un 💡.

⚠️ **`:2786` e `:2791` sono i bottoni di fine partita, e dicono cose opposte**:
il primo esce quando **vinci** — l'avversario finisce nella gabbia di Amur — il
secondo quando **perdi**. Il giapponese, identico, non lo distingue.
⭐ «gabbia di Amur» viene dalla 52ª, che l'aveva resa per la prima volta in
tutto il progetto a `tcg_custom.hsp:1608`.
⚠️ **«Noooooooooooooo!» resta identica**, e va detto perche' non e' una
dimenticanza: e' un urlo, si scrive uguale nelle due lingue. Stessa scelta di
«Mana», «Immune» e «Abnormal».

⭐⭐ **«F8 [Spec]» e' sbagliato anche in inglese, e la resa lo corregge.** F8 e'
il tasto virtuale 119 (`:3942`) e apre `*DeckExportImportMenu`, cioe' il menu di
esportazione e importazione che la 52ª ha gia' tradotto («Esporta il mazzo»,
«Importa il mazzo»…). «Spec» non vuol dire niente: la riga d'aiuto dice
**«F8 [File]»**. E' la stessa disciplina di «(Ora: ERRORE)» della 52ª — si
guarda il sito, non la parola — applicata a una riga d'aiuto invece che a uno
stato.

⚠️ **Due refusi di monte non ricalcati.** `:4065` dice «You can only put **2**
copy» mentre il giapponese dice 1枚, cioe' una; e tutte e quattro dicono «copy»
al singolare con un numero davanti. La resa segue l'**inglese**, che e' la
lingua di monte, e mette il plurale italiano dove ci vuole. ⚠️ `:4077` e'
l'altro verso: il giapponese dice «la stessa carta», l'inglese «lo stesso
seme» — e sono le carte da poker del negozio, quindi l'inglese ha ragione.

💡 **«Con che nome salvare?» non e' stata scelta: era gia' li'.** `:4553` ha lo
stesso giapponese 「どのファイル名で保存する？」 di `command.hsp:17552`, e
`gia_rese.py` l'ha trovata prima che scrivessi qualcosa. Lo stesso per
「キャンセル」 → «Annulla» (`command.hsp:17318`).

💡 **Il tetto delle due schede della colonna e' nel `sdim`.** `:3543` dichiara
`sdim cfname@tcg, 16, 10`: **quindici caratteri** per scheda. «Elenco» ne fa 6 e
«Mazzo» 5, e le nove schede di dominio che stanno nello stesso array arrivano da
`domname@tcg`, che e' un'altra riga.

💡 I tetti dei menu, col metro di `larghezze.py` — `(pixel − 46) / 7,7` — perche'
`*prompt_key@` e' l'etichetta del modulo principale, cioe' proprio `*prompt_key`:

    :3972  200px -> 20 caratteri   «Azzera il mazzo» (15)   «Annulla» (7)
    :4118  240px -> 25             «Salva ed esci» (13)     «Esci senza salvare» (18)
    :4425  200px -> 20             «Chiudi il turno» (15)   «No» (2)
    :4434  200px -> 20             «Arrenditi» (9)          «No» (2)

⭐ «Arrenditi» non e' una scelta nuova: e' quella che la 52ª ha gia' messo nella
barra in fondo al tavolo, `:1095` «S [Arrenditi]».
"""
