# Fase 7 — la rete che parte da chi disegna, e il fronte che ha trovato

Aperta nella **centotrentottesima** sessione, 2026-09-04, dopo il lotto E della
Fase 6.

## Perché

La 137ª ha scoperto che `copertura._PROSA` — «due parole alfabetiche separate
da uno spazio» — **non vede le etichette**, e un'interfaccia è fatta di
etichette. In `tcg.hsp` ne sono state trovate **58** a schermo dentro un fronte
dichiarato e contato, e il conto non le comprendeva. La 138ª ne ha trovate
altre **25** fra le battute del gioco di carte.

Tutt'e due le volte il buco è stato misurato **su un file per volta, a mano**.
La domanda vera era rimasta aperta, ed era la cosa aperta più grossa del
progetto:

> *quante stringhe a schermo non le vede nessuno, negli altri novanta file?*

**Adesso c'è un numero: 160.**

## Come

`strumenti/disegnate.py` non guarda com'è fatta una stringa. Parte da **chi
manda un testo allo schermo** — `txt`, `mes`, `bmes`, `chatList`, `chatMore`,
`cardhelp`, `dialog`, `mesbox`, `objprm`, `poptext` — e lavora su due livelli:

    livello 0   il letterale sta sulla RIGA del comando
                    mes "Dv:" + dvr1
    livello 1   il letterale è assegnato a una VARIABILE che qualcuno disegna
                    s@tcg += "[Command Card] "     ...poi   mes s@tcg

⭐ Il livello 1 è il gradino che mancava, ed è esattamente il caso costato due
volte: da solo, il livello 0 su tutto il sorgente trova 34 stringhe. Coi due
livelli insieme ne trova 162.

Cosa si sottrae, e perché: il ramo giapponese di ogni `lang()` (⚠️ **anche
quando è scritto in lettere latine** — `chat.hsp:6711` è `lang("Yes", "Yes.")`,
e senza quel caso il censimento chiamava «scoperte» le due metà giapponesi di
righe già tradotte), i letterali senza nemmeno una lettera, quel che copre un
meccanismo del progetto (`schede`, `dialoghi`, `carte`, `scene`), le righe con
una toppa, e `invariati.md`.

⚠️ **I limiti sono dichiarati, non nascosti.** Il salto per variabile è **uno
solo e dentro lo stesso file**: una stringa messa in una variabile, passata a
una funzione e disegnata altrove resta fuori. E `noteadd` non è fra i comandi,
perché scrive anche i file di dato — mescolarlo direbbe «da tradurre» a righe
che tradotte romperebbero un salvataggio.

## Che cosa ha trovato

    162 stringhe distinte disegnate e non coperte, su 12 file
    160 di queste il censimento vecchio NON le vedeva
    301 ne vede `_PROSA` che questa rete non vede (tracce di debug,
        stringhe di dato, e il testo che passa per più di un salto)

Le due reti si scoprono a vicenda, e nessuna delle due basta da sola: è per
questo che `copertura` resta il cancello del **dizionario** e `disegnate` è il
cancello dello **schermo**. Tutt'e due chiedono la stessa cosa — o è coperta, o
è dichiarata con scritto perché.

### ⭐⭐ Il fronte vero: il menu dei filtri dell'editor di mazzo

`tcg.hsp:3552-3632`, `cfname@tcg`: **126 etichette** che nessun censimento ha
mai contato.

    All  Blue  Green  White  Black  Neutral  Legendary  Gray  Red
    Cost 0 … Cost 8+          1- Atk … 9+ Atk          1 HP … 9+ HP
    seamonster  frog  snail  shell  spirit  slime  bird  mushroom …
    warrior  thief  wizard  claymore  priest  archer  warmage  gunner …

⚠️ **Vanno guardate a schermo prima di tradurle**: stanno negli stessi slot a
larghezza fissa degli 8 `Filter:` del lotto B2, e l'italiano è più lungo.

⚠️⚠️ **E le razze e le classi non si decidono qui.** Sono gli stessi nomi che
`db_race.hsp`, `db_class.hsp` e le carte usano altrove: se il filtro dice
«dragon» e la carta dice «drago», il giocatore non trova le sue carte. Questo
lotto va fatto **insieme** a quella tabella, non prima.

### Gli altri, triati uno per uno

| file | quante | che cosa |
|---|---|---|
| `action.hsp` | 12 | le classi che il comando dei desideri scrive dentro il nome della creatura. ⚠️ Sulla stessa riga c'è l'**operando** (`if inputlog == "warrior"`), che è quel che il giocatore digita e non si tocca |
| `command.hsp` | 4 | `Dv:` e ` Pv:` — **decise invariate** dal glossario, manca solo la riga in `invariati.md` — più `,Tab ` e la «d» dei dadi |
| `main.hsp` | 2 | `lv:`, che va deciso insieme al `Lv` della barra e al ` liv.` del dizionario: **oggi il progetto ne ha due grafie e questa è la terza** |
| `module.hsp` | 1 | `,Tab `, lo stesso di `command.hsp` |
| `screen.hsp` | 4 | `Sp` e `Lv` della barra (italiano che coincide), più due tracce di debug |
| `system.hsp`, `net.hsp` | 5 | finestre d'errore di sistema, stessa famiglia dei comandi MCI di `sound.hsp` |
| `etc.hsp` | 2 | `Jo` (il Jolly) e `X ` (il segno di moltiplicazione della pila) |
| `proc.hsp` | 1 | «Omae wa mou shindeiru.», la citazione di Ken il guerriero: in italiano circola così |
| `config.hsp` | 1 | `%.1f`, un formato |
| `helloworld.hsp` | 1 | file di prova che nessuno `#include` |

## Come si saprà che è finita

    disegnate            12 file dichiarati -> il fronte di `tcg.hsp` a 3,
                         e la riga di `action.hsp` tolta
    invariati.md         `Dv:`, ` Pv:`, `Sp`, `Omae wa mou shindeiru.`
                         con la loro ragione
    una grafia sola      per `Lv` / ` liv.` / `lv:`
    pytest               verde DOPO i documenti, non prima

⚠️ Nessuno di questi numeri si eredita da qui: si rilanciano.
