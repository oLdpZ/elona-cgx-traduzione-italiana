# Pubblicazione e annuncio — 2026-09-06, centoquarantatreesima

Quel che serve per far arrivare la traduzione a qualcuno che non sia noi. I
testi stanno qui e non in una chat perché il giorno in cui si pubblica non è
oggi, e chi li riscrive da capo li riscrive peggio.

## Stato

    repo        oLdpZ/elona-cgx-traduzione-italiana — **PRIVATO**
    rami        master == fase-0 == 8bc7138, tutto spinto; PR #1 risulta MERGED
    archivio    C:\Games\Elona\_traduzione\dist\elona-cgx-ita-2.31.2.0.zip
                4.972.407 byte — si rifà con `python -m strumenti.pacchetto`
    permesso    issue #37 sul repo di Custom-GX, aperta il 05/09, in attesa

## L'ordine, e perché è questo

1. **Il collaudo a schermo, almeno delle schermate principali.** ⚠️ È il primo
   passo e non è prudenza generica: su un pubblico di poche decine di persone la
   prima impressione è quasi tutto quel che avrai, e un difetto banale trovato
   dal primo che scarica costa più di una settimana di attesa.
2. **Repo pubblico.** Dentro non c'è codice di monte: dizionario, strumenti e
   documenti. Il `README` è già scritto per essere la pagina di chi arriva.
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
| [Elona variants/Resources](https://elona.fandom.com/wiki/Elona_variants/Resources) | la riga neutra qui sotto | **resta** |
| [Discussions del wiki](https://elona.fandom.com/f) | l'annuncio in inglese | scorre |
| [issue #37](https://github.com/JianmengYu/ElonaPlusCustom-GX/issues/37) | «fatto, ecco il link» — e lì c'è già chi ha CGX installato | resta |
| [OldGamesItalia](https://www.oldgamesitalia.net/forum/) | l'annuncio in italiano; è il posto storico delle traduzioni amatoriali | scorre |
| [RPG Italia](https://steamcommunity.com/groups/rpgitalia) | idem, pubblico GDR | scorre |
| Discord Elin/Elona | le domande, si risponde in giornata | scorre |

⚠️ Il Discord esiste ed è attivo, ma **non abbiamo un invito verificato**: si
prende dai canali ufficiali di Elin o dal wiki, e non si copia un link vecchio.

⚠️ **Un post solo per posto.** Non uno per categoria.

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
> Download and instructions: <link al repo>
>
> This is unofficial and not affiliated with the Custom-GX maintainers. Thanks to
> JianmengYu, Ruin0x11, Ano and Noa. Feedback and bug reports very welcome —
> especially from anyone on a machine that isn't mine.

## La riga per il wiki (terza persona, niente aggettivi)

    * [Italian translation](<link>) — unofficial Italian localization of Elona+
      Custom-GX 2.31.2.0. Distributed as a dictionary plus a build script that
      compiles an Italian executable from the player's own copy of the game;
      installs alongside the English executable.

⚠️ **Il tono cambia col posto, e non è un dettaglio.** Nel post la prima persona
è quella giusta («I've been working on…»); nella pagina wiki si scrive in terza
persona e senza aggettivi promozionali — «unofficial Italian localization», mai
«complete, high-quality». Su un wiki la seconda forma viene tolta da qualcun
altro, ed è giusto così.

## Come si posta sulle Discussions

1. accedere: senza login **il pulsante per scrivere non compare**, ed è la
   ragione più comune per cui sembra che le Discussions non ci siano;
2. `https://elona.fandom.com/f` → il pulsante in cima al feed (`+`, una matita o
   *New Post* a seconda della skin);
3. categoria **General**, titolo, testo, *Post*;
4. tornarci dopo un giorno o due: le domande arrivano lì, e una risposta rapida
   vale più dell'annuncio.

⚠️ Da telefono l'editor delle Discussions è scomodo per un post lungo: farlo da
computer.
