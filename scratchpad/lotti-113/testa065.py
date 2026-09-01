# -*- coding: utf-8 -*-
"""122a - Lotto 065 di `db_item.hsp`: GLI ANELLI, e la categoria CHIUDE.

`FILTER_ACCESSORY_RING`, righe da `:56737` a `:130385`: **11 righe**, tutte
dell'indice 0, su 11 oggetti. Con questo lotto `FILTER_ACCESSORY_RING` va a
**0 da fare su 11 vive**, ed e' la **ventesima** categoria del corpo che si
chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 065`: **+11** per 11 rese,
nessuna gemella. ⓘ `_gia-reso.py 065`: 0 su 11. `_code.py 065`: 0 righe senza
resa in tabella. `_forma.py 065`: 11 su 11 con lo spazio prima del `\\n`.

### ⭐⭐⭐ LA RIGA SORELLA STAVA NEL LOTTO DI VENTI MINUTI FA. DI NUOVO.

    :99448 (064)  婚礼の儀において、伴侶となる者へ送られる愛のこめられた**首輪**。
                  当然ながらこの**首輪**は伴侶の所有物となるので、無理やり…
    :99162 (065)  婚礼の儀において、伴侶となる者へ送られる愛のこめられた**指輪**。
                  当然ながらこの**指輪**は伴侶の所有物となるので、無理やり…

Identiche in giapponese tranne **una parola**, e le rese lo sono in italiano.

⚠️ **E' la terza volta in questa sessione**, dopo le due famiglie del lotto 063,
e la seconda volta in due sessioni che la sorella sta in un lotto **chiuso
poche ore prima**. `_gia-reso.py` dice 0 su 11 e ha ragione — cerca la prosa
intera, e le due stringhe differiscono di un carattere.
⭐ Stavolta non e' stata la fortuna: il dossier del 064 era ancora aperto e la
frase e' stata riconosciuta a occhio. **Su una sessione che riprendesse domani
non lo sarebbe.** Lo strumento che manca resta quello: la riga sorella **per
frase** su tutto `db_item.hsp`, non per prosa intera e non dentro il lotto.
ⓘ Il conto di questa sessione: tre famiglie trovate a mano, zero trovate da uno
strumento.

### ⭐ TRE ESPRESSIONI CHE TORNANO DA LOTTI PRECEDENTI, CERCATE PRIMA DI SCRIVERE

  - より高みを目指した (`:99377`) e' la stessa di `:89077`, l'elmo del saggio
    del lotto 063: «puntare più in alto», stessa resa;
  - 武骨 (`:107390`) e' la stessa parola di `:99663`, la gorgiera del lotto
    064: «rozzo»;
  - 〜のこめられた (`:86671`) -> «racchiuso», come i due indici 3 delle collane
    e le rese del 064.

### ⓘ Le decisioni minori, e da dove vengono

  - 元素の神 «il dio degli elementi», gia' in gioco sul busto che lo raffigura;
    鋼鉄竜 «drago d'acciaio», che e' anche il nome italiano dell'oggetto e il
    nome di <Corgon> in gioco; 螺旋 «spirale»;
  - 気品 (`:107181`) -> **«eleganza»**, la parola che il gioco usa gia' nel
    tratto «Eleganza [clientela migliore]». ⚠️ L'indice 3 dello stesso oggetto
    parla invece di 運勢, la **fortuna**: sono due cose diverse nello stesso
    pannello e restano due parole diverse. Appiattirle sarebbe un errore che
    nessuna rete vedrebbe;
  - `:86671` dice 老化するという弊害はない, e non e' una figura retorica: nel
    gioco l'accelerazione fa invecchiare, e la riga sta dicendo che questo
    anello no. E' un fatto di gioco e va detto chiaro;
  - `:99233` riprende le parole del suo indice 3 gia' in gioco, «Un cerchio da
    infilare al dito».

### ⓘ Il preflight ha segnalato una parola lunga, e non e' un difetto

`controindicazione` (17 caratteri). Vale quel che si e' misurato nel lotto 063:
il tetto vero e' il budget da 77 del corpo impaginato, nel dizionario ci sono
gia' 19 rese con parole da 17 caratteri o piu', e il cancello di
`_107-descrizioni-item` legge 0 parole spezzate.
"""
