# -*- coding: utf-8 -*-
"""95a - CRAY, MARY e JENNA: si chiude l'imbocco della Valle di Raskilis.

Tre blocchi, 8 rese: `chat.hsp:15398`-`:15414` (CRAY, 4 su 4),
`:15415`-`:15430` (MARY, 3 su 3) e `:15434` (JENNA, l'ultima delle sue 6).

⭐⭐ IL RAGGRUPPAMENTO L'HA CORRETTO `map.hsp`, NON IL CONTEGGIO DELLE FIRME.
La ripresa della 94a proponeva **CRAY + NANCY + MARY** come «la Valle di
Raskilis che si chiude». `map.hsp` dice altro: la mappa dell'imbocco e'
`ras0` (`AREA_WEST_RASKILIS`, livello 1) e ci stanno **JENNA** (`:4971`),
**MARY** (`:4974`), **CRAY** (`:4977`) e **MANSON** (`:4980`), gia' reso ieri.
NANCY sta in `ras_south` (`:5096`), un'altra area, con TONI e CARTER. E' la
lezione della 94a su BONYAC applicata prima di tradurre invece che dopo:
**il conteggio delle firme non dice dove sta un parlante.**
Con questi tre la mappa dell'imbocco e' **finita**: quattro parlanti su quattro.

⭐⭐⭐ IL LESSICO DELLA VALLE ERA GIA' TUTTO SCRITTO, E NON IN UN POSTO SOLO.
  - 谷の奥      «il fondo della valle»        `:15382` (Manson), `:15439` (Jenna)
  - 谷の入口    «l'imbocco della valle»       `:15439`
  - 黒い獣      «le bestie nere»              `:15190`, `:15440`
  - 空間が閉じて «lo spazio si e' richiuso»    `:15440`
  - お店        «la bottega» (di Bonyac)      `:15473`, `:15479`
  - タイタン    «il titano»                   `action.hsp:17368` e altri tre
  - 神の啓示    «rivelazione divina»          `command.hsp:9642`
  - 〜さん      «il signor 〜»                 `db_creature.hsp:83964`, `:87568`

⭐⭐⭐ E UNA FRASE INTERA ERA GIA' RESA, A MILLE RIGHE DI DISTANZA.
`:15401` chiude con 「冒険じゃなく自殺行為だ」 e `chat.hsp:14394` — una lezione
del **Seminario d'Avventura**, resa nell'87a — chiude con 「冒険じゃなくて自殺
行為だ」: **le stesse parole**, gia' rese «non e' andare all'avventura, e'
suicidarsi». Si copia. 💡 E la coincidenza non e' casuale: Manson insegna a
Cray la stessa cosa che il seminario insegna al giocatore.

⚠️ DEROGA 1 — `:15407`, 裂け目 E' LA CASELLA SU CUI SI CAMMINA, E HA GIA' UN NOME.
Il 裂け目 di cui parla Cray e' la **scala in giu' di `ras0`**: `action.hsp:2853`
dice che nella sola `AREA_WEST_RASKILIS` la casella non e' una scala ma
「空間の裂け目」, e la riga e' gia' resa **«C'e' una fenditura nello spazio.»**
E' testo che il giocatore legge camminandoci sopra. Quindi qui si scrive
**«fenditura»**, non un sinonimo nuovo.
⚠️⚠️ E per la stessa ragione `:15440` di Jenna (91a) e' stata **rifatta**: diceva
«fessura», che e' un secondo nome per lo stesso oggetto sulla stessa mappa. Vedi
`scratchpad/_95-correzione-fenditura.py`.

⭐ DEROGA 2 — `:15401` E' MANSON CHE PARLA, NON CRAY.
La riga dopo lo dice («...me lo ripete di continuo»), quindi la massima e' di
Manson. Ma Manson da' del **voi** al giocatore (regola dell'88a) e qui sta
parlando **a Cray**, non al giocatore: la seconda persona cambierebbe
destinatario a meta' blocco. Si tiene l'**impersonale**, che e' anche la forma
di `:14394`, la sua gemella del seminario.

⭐ DEROGA 3 — `:15407`, «もうよく思い出せない» NON E' UN MODO DI DIRE.
Cray **non ricorda** chi si e' buttato nella fenditura, e nella stessa mappa
Manson dice di aver perso il senso del tempo (`:15385`). Due mappe piu' in la'
ci sono **RYUTYE e NERES, i due smemorati**. La perdita di memoria e' un tratto
della valle, non un intercalare: si rende per intero e non si alleggerisce.

PERIMETRO: 8 firme su 8 dentro i tre blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15398 15415 15431`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- CRAY: la massima di Manson, ripetuta a memoria
    15401: 'Andare all\'avventura vuol dire prepararsi come si deve e correre '
           'il rischio lo stesso. Buttarsi nel pericolo senza pensarci su e '
           'senza aver preparato niente non è andare all\'avventura, è '
           'suicidarsi.',
    15402: '...Manson me lo ripete di continuo. Gli sembrerò davvero così '
           'sconsiderato?',

    # --- CRAY: la prima volta
    15406: 'Accidenti. Mi rode da matti non sapere che cosa stia succedendo in '
           'questo momento in fondo alla valle. Però, se Manson si mette di '
           'traverso in quel modo, vuol dire che là sotto è pericoloso in un '
           'modo che dare la caccia ai titani non ci si avvicina nemmeno.',
    15407: 'Mi pare che ci fosse gente che ha ignorato i nostri avvertimenti e '
           'si è buttata nella fenditura a est... Erano avventurieri anche '
           'loro? Ormai non me lo ricordo più bene.',

    # --- MARY: quando la si risente
    15418: 'Anche in un momento come questo... no. Proprio perché il momento è '
           'questo, mi basta stare in mezzo a dei bei fiori per sentirmi '
           'felice.',

    # --- MARY: la prima volta
    15422: 'Chi l\'avrebbe mai detto che il signor Bonyac non se ne sarebbe '
           'andato dalla bottega. La bottega era circondata da un branco di '
           'bestie... chissà se sta bene.',
    15423: 'E spero che anche tutti gli altri che erano nella valle siano '
           'riusciti a uscirne sani e salvi.',

    # --- JENNA: quando la si risente
    15434: 'Quella voce che ho sentito non può essere che una rivelazione '
           'divina!',
}
