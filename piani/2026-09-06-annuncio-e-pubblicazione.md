# Pubblicazione e annuncio — 2026-09-06, centoquarantatreesima

Quel che serve per far arrivare la traduzione a qualcuno che non sia noi. I
testi stanno qui e non in una chat perché il giorno in cui si pubblica non è
oggi, e chi li riscrive da capo li riscrive peggio.

⚠️ **Corretto nella 144ª, il 2026-09-06**: la voce «resta» mandava su una
pagina del wiki che non è quella giusta, e adesso la sezione «Dove» dice perché.
Il resto — l'ordine dei passi e il testo dell'annuncio — è invariato.

## Stato

    repo        oLdpZ/elona-cgx-traduzione-italiana — **PUBBLICO dalla 144ª**
                https://github.com/oLdpZ/elona-cgx-traduzione-italiana
    release     2.31.2.0-ita, creata nella 144ª; l'asset si scarica in anonimo
                (provato: 200, 4.973.020 byte, impronta 900e06e5… identica al
                file locale)
                ⚠️ Rifatto nella stessa sessione dopo la toppa dell'ottava riga
                di crediti: il primo pacchetto, di 4.972.407 byte, compilava
                senza il credito. Ogni toppa nuova invecchia l'asset, e
                sostituirlo e' `gh release upload … --clobber`.
    rami        master == fase-0 == origin/*, tutto spinto; PR #1 MERGED
                ⓘ Qui non si scrive l'impronta del commit: invecchia al
                commit dopo, e un valore vecchio in un documento di ripresa
                si legge come vero. Si guarda con `git status -sb`.
    archivio    C:\Games\Elona\_traduzione\dist\elona-cgx-ita-2.31.2.0.zip
                4.973.020 byte — si rifà con `python -m strumenti.pacchetto`
    permesso    issue #37 sul repo di Custom-GX, aperta il 05/09, in attesa

## L'ordine, e perché è questo

1. **Il collaudo a schermo, almeno delle schermate principali.** ⚠️ È il primo
   passo e non è prudenza generica: su un pubblico di poche decine di persone la
   prima impressione è quasi tutto quel che avrai, e un difetto banale trovato
   dal primo che scarica costa più di una settimana di attesa.
2. **Repo pubblico.** Dentro non c'è codice di monte: dizionario, strumenti e
   documenti. Il `README` è già scritto per essere la pagina di chi arriva.

   ⚠️⚠️ **«Non c'è codice di monte» è vero e incompleto, ed è stato verificato
   nella 144ª**: zero file `.hsp` tracciati, ma il dizionario conserva
   l'originale **inglese e giapponese riga per riga** (`en`, `jp_contesto`), e
   i 64 file del dizionario stanno anche dentro lo zip che si scarica.
   `dizionario/dati/book.txt.jsonl` da solo è 8,0 MB su 2.241 righe: è il testo
   dei libri del gioco per intero. Non è codice, è **testo di monte
   ripubblicato integralmente in due lingue** — cioè la cosa su cui verte
   l'issue #37, che il piano trattava come se riguardasse solo l'eseguibile.

   ⓘ `jp_contesto` **nessuno strumento lo legge**: lo scrive `dati_estrai.py` e
   lo leggono solo i test; nessun passo di `applica` o di `costruisci.py` lo
   tocca. Si potrebbe togliere dal pacchetto senza rompere niente, e toglierebbe
   di mezzo il giapponese. L'`en` invece serve, perché è la chiave con cui la
   toppa trova la riga da sostituire.

   ⭐ **Deciso nella 144ª: si pubblica com'è**, dizionario intero, sul
   presupposto che la #37 copra già la domanda. Scritto qui perché è una scelta,
   non una svista, e perché la strada per tornare indietro esiste ed è misurata.
3. **La release**, col tag che dice a quale versione di Custom-GX corrisponde —
   è l'informazione che serve davvero a chi installa:

       gh release create 2.31.2.0-ita \
         "C:\Games\Elona\_traduzione\dist\elona-cgx-ita-2.31.2.0.zip" \
         --title "Traduzione italiana — Custom-GX 2.31.2.0"

4. **Due o tre persone**, prese in un posto solo, che installino su macchine che
   non sono la nostra. È l'unico modo di trovare quel che qui non si vede:
   Python assente, cartella del gioco altrove, antivirus che guarda male un
   `.bat`, una versione di Custom-GX diversa.
5. **Poi** gli annunci.

## Dove, e la differenza fra i due tipi di posto

⭐ **Un posto che resta vale più di un posto grande.** I forum scorrono in
settimane; una riga su un wiki la trova fra due anni chi cerca «elona italian».

| dove | che cosa ci va | tipo |
|---|---|---|
| **una pagina propria** sul wiki (non esiste ancora) | la voce qui sotto | **resta** |
| [Elona+ Custom](https://elona.fandom.com/wiki/Elona%2B_Custom) | un link alla pagina propria | **resta** |
| [Elona variants](https://elona.fandom.com/wiki/Elona_variants), sezione `=== Elona+ custom ===` | un link alla pagina propria | **resta** |
| [Discussions del wiki](https://elona.fandom.com/f) | l'annuncio in inglese | scorre |
| [issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37) | «fatto, ecco il link» — e lì c'è già chi ha CGX installato | resta |
| [OldGamesItalia](https://www.oldgamesitalia.net/forum/) | l'annuncio in italiano; è il posto storico delle traduzioni amatoriali | scorre |
| [RPG Italia](https://steamcommunity.com/groups/rpgitalia) | idem, pubblico GDR | scorre |
| Discord Elin/Elona | le domande, si risponde in giornata | scorre |

⚠️ Il Discord esiste ed è attivo, ma **non abbiamo un invito verificato**: si
prende dai canali ufficiali di Elin o dal wiki, e non si copia un link vecchio.

⚠️ **Un post solo per posto.** Non uno per categoria.

### ⚠️⚠️ La riga «resta» di questo piano indicava la pagina sbagliata, ed è misurato

Fino al 06/09 questa tabella mandava la voce neutra su
[Elona variants/Resources](https://elona.fandom.com/wiki/Elona_variants/Resources).
La pagina esiste (pageid 23306) ma **non è un elenco di risorse per i
giocatori**: dentro c'è un CSV per generare il diagramma ad albero delle
varianti e una tabella «Editing progress» con le spunte `✔ ⏰ ✘` di chi cura il
wiki. Ultima modifica **7 novembre 2016**. Una voce lì non la legge nessuno.
Era un'ipotesi plausibile scritta senza aprire la pagina.

⭐ **Quel wiki non ha un indice delle traduzioni: le indicizza come varianti,
con una pagina propria.** I due precedenti:

- `Omake Overhaul English` — cinque righe (cos'è, di che variante è la
  traduzione) più `[[Category:Elona variants]]` e `[[Category:Article stubs]]`;
- `Elona+ Japanese/English Translation` — pagina di progetto lunga, del 2012.

⚠️ **E c'è il controesempio, che conta più dei due precedenti**: la pagina
`Translation of the game into other languages` **esiste**, è lunga **36 byte**, e
l'unica cosa che contiene è `[[Category:Candidates for deletion]]`. Qualcuno ha
già provato a fare questa pagina, vuota, ed è finita in cancellazione. La pagina
deve avere contenuto vero, non solo un link.

ⓘ Una pagina `Elona+ Custom-GX` su quel wiki **non esiste proprio**, e
`Elona+ Custom` è ferma ai download di Custom 1.89.3 e 1.90.4 su MEGA e Google
Drive, roba pre-GX. Non è un problema nostro da risolvere, ma spiega perché non
c'è un posto ovvio dove infilarsi.

⚠️ **Il wiki è vivo ma lento**: otto modifiche dall'11 agosto al 6 settembre,
due redattori. «Resta» sì, ma non porta traffico: il valore è che fra due anni
chi cerca «elona italian» la trovi.

⚠️ **Delle Discussions non sappiamo se siano attive.** Il 06/09 l'API ha
risposto 404, ma il controllo su un wiki grande e sicuramente attivo ha dato
**anche lui 404**: è rotto il metodo di sonda, non risposta la domanda. Si
guarda da browser loggato, sono dieci secondi.

## Il testo dell'annuncio (inglese, per le Discussions)

> **Italian translation for Elona+ Custom-GX 2.31.2.0**
>
> Hi everyone. I've been working on a full Italian translation of Custom-GX, and
> it's now at a point where it can be installed.
>
> It's not just the UI: item and creature names, descriptions, dialogue, quests,
> the card game, menus, combat messages and the `data/` text files are
> translated.
>
> **How it works.** Custom-GX's source has no license, so I didn't want to
> redistribute a prebuilt executable without asking (I opened issue #37 about
> that). Instead, the download is a small package that **builds the Italian
> executable on your own machine**: it pulls Custom-GX's source from GitHub, the
> HSP SDK from Onion Software, and only the dictionary comes from me. You need
> Python 3.11+ and a few minutes.
>
> **It doesn't touch your install.** The Italian build is written as
> `cgx-ita.exe` *next to* your `elonapluscgx.exe`, which is left alone — the same
> saves work with both — plus six additive `data/*_it.txt` files the game only
> loads if present. There's an uninstaller that deletes those seven files.
>
> Download and instructions: https://github.com/oLdpZ/elona-cgx-traduzione-italiana
>
> This is unofficial and not affiliated with the Custom-GX maintainers. Thanks to
> JianmengYu, Ruin0x11, Ano and Noa. Feedback and bug reports very welcome —
> especially from anyone on a machine that isn't mine.

## La pagina per il wiki (terza persona, niente aggettivi)

Titolo proposto: **`Elona+ Custom-GX Italian`**, sulla forma di
`Omake Overhaul English`. Wikitesto:

    '''Elona+ Custom-GX Italian''' is an unofficial Italian localization of
    [[Elona+ Custom|Elona+ Custom-GX]] 2.31.2.0.

    It is distributed as a dictionary plus a build script, not as a prebuilt
    executable: the script downloads Custom-GX's source and the HSP SDK and
    compiles an Italian executable on the player's own machine. It requires
    Python 3.11 or later.

    The Italian build is written as <code>cgx-ita.exe</code> alongside the
    existing <code>elonapluscgx.exe</code>, which is left unchanged; saves are
    shared between the two. Six additive <code>data/*_it.txt</code> files are
    added, and an uninstaller removes them.

    Download and instructions: [https://github.com/oLdpZ/elona-cgx-traduzione-italiana project page]

    [[Category:Elona variants]]
    [[Category:Elona+]]

E il link da `Elona+ Custom` e dalla sezione `=== Elona+ custom ===` di
`Elona variants`, una riga sola:

    See also: [[Elona+ Custom-GX Italian]] — unofficial Italian localization.

⚠️ **Il tono cambia col posto, e non è un dettaglio.** Nel post la prima persona
è quella giusta («I've been working on…»); nella pagina wiki si scrive in terza
persona e senza aggettivi promozionali — «unofficial Italian localization», mai
«complete, high-quality». Su un wiki la seconda forma viene tolta da qualcun
altro, ed è giusto così.

## Come si posta sulle Discussions

1. accedere: senza login **il pulsante per scrivere non compare**, ed è la
   ragione più comune per cui sembra che le Discussions non ci siano;
   ⚠️ ma su questo wiki potrebbero davvero non esserci — vedi sopra, non è
   stato possibile verificarlo da riga di comando;
2. `https://elona.fandom.com/f` → il pulsante in cima al feed (`+`, una matita o
   *New Post* a seconda della skin);
3. categoria **General**, titolo, testo, *Post*;
4. tornarci dopo un giorno o due: le domande arrivano lì, e una risposta rapida
   vale più dell'annuncio.

⚠️ Da telefono l'editor delle Discussions è scomodo per un post lungo: farlo da
computer.
