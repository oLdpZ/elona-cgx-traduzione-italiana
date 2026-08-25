# -*- coding: utf-8 -*-
"""Le rese di `data\\autopick.txt`: il modello delle regole di raccolta.

    python scratchpad/_100-rese-autopick.py lavoro/autopick-001.jsonl

⚠️⚠️ **Questo file non e' testo da leggere: e' il modello che insegna una
sintassi**, e ogni riga di regola dev'essere una regola che **aggancia
davvero**. Le chiavi vengono da `dizionario/custom_autopick.hsp.jsonl`, e a
tenerle allineate col modello e' `scratchpad/_100-modello-aggancia.py`.

⚠️ `dati_applica` **sostituisce** righe, non ne aggiunge: le rese sono 156, una
per riga piena, nell'ordine in cui `dati_estrai.voci()` le numera.

⭐ **La sezione giapponese di monte (`:103`-`:156`) diventa l'elenco delle
chiavi INGLESI**, ed e' un cambio di contenuto voluto. Quelle 53 righe sono la
stessa lista in una seconda lingua, e in un file italiano la lista giapponese
non serve a nessuno: le guide in rete — che il file stesso linka a `:24` — sono
in inglese, e un giocatore italiano che le legge ha bisogno **di quella**
corrispondenza. L'intestazione dice a chiare lettere che quelle chiavi in questa
versione non agganciano.

⚠️ `:sound123` resta com'e': `custom_autopick.hsp:647` lo cerca con
`instr(buff, 0, ":sound")`, che e' un **letterale nudo** fuori da ogni `lang()`
— tradurlo manderebbe il lettore a scrivere una parola che il codice non cerca.
E' la regola della 99a («un manuale cita quel che e' a schermo»), e sta in
`invariati.md`. Stessa cosa per i marcatori `#`, `~`, `!`, `!!`, `?`, `%`, `=`,
per il nome dei file (`autopick_1.txt`) e per l'indirizzo del wiki.
"""
import io
import json
import sys

RIGHE = [
    # ---------------------------------------------------------- l'intestazione
    "### Elona+ Custom-GX — Impostazioni della raccolta automatica ###",
    "# Per usarlo, accendi la raccolta automatica in Impostazioni extra 1, dal menu delle impostazioni.",
    '# Questo file va salvato come "autopick.txt" nella cartella di salvataggio del personaggio.',
    "# In gioco, [Maiusc+Backspace] ricarica questo file.",
    "# [Ctrl+Backspace] apre nell'editor di testo il file di raccolta che è caricato adesso.",
    "# [Alt+Backspace] accende e spegne al volo la raccolta automatica.",
    "# Tenendo premuto [Ctrl] mentre ti muovi, la raccolta automatica non scatta.",
    "#",
    "# Sintassi:",
    "# Il '#' apre un commento.",
    "# Il '~' davanti a una voce vuol dire: non raccoglierla, e salta tutte le regole che seguono.",
    "# Il '!' davanti a una voce vuol dire: distruggila.",
    "# Il '!!' davanti a una voce vuol dire: distruggila anche se è preziosa.",
    "# Il '?' dopo una voce vuol dire: chiedi prima di raccoglierla o di distruggerla.",
    "# Il '%' dopo una voce vuol dire: salva la partita quando la raccogli.",
    "# Il segno '=' dopo una voce vuol dire: metti il [Non posare] all'oggetto quando lo raccogli.",
    "# ':sound123' dopo una voce vuol dire: suona l'effetto numero 123 quando la regola aggancia.",
    "#",
    "# In ogni cartella di salvataggio puoi tenere fino a 10 gruppi di regole,",
    "# chiamati autopick.txt, autopick_1.txt, autopick_2.txt, e così via.",
    "#",
    "# NOTA: la raccolta automatica non scatta nei luoghi che sono tuoi (tranne fattorie e rifugi).",
    "#",
    "# Per saperne di più c'è il wiki: https://elona.fandom.com/wiki/Autopickup",
    "# (Attenzione: qualcosa è diverso dalla sintassi di omake, e il wiki è in inglese — le chiavi inglesi stanno in fondo.)",

    # -------------------------------------------------------------- gli esempi
    "### Esempi ###",
    "# Lascia stare gli oggetti maledetti.",
    "# Se aggancia una regola più in alto nel file, quelle che vengono dopo non vengono nemmeno provate.",
    "~oggetto con maledizione",
    "~oggetto con dannazione",
    "# Raccogli gli oggetti preziosi, poi salva la partita e mettici il [Non posare].",
    "oggetto prezioso%=",
    "# Raccogli oro, platino e medagliette.",
    "moneta d'oro",
    "moneta di platino",
    "medaglietta",
    "# Raccogli l'acqua, ma chiedi prima.",
    "acqua?",
    "# Distruggi i lingotti d'oro falsi.",
    "# Una regola scritta sul nome aggancia solo se il nome dell'oggetto è già noto.",
    "!lingotto d'oro falso",
    "# Distruggi i cadaveri, ma chiedi prima.",
    "!cadavere?",
    "# Più regole si possono incatenare sulla stessa riga.",
    "# Le regole sul pregio e sulla maledizione agganciano solo se il pregio dell'oggetto è già noto.",
    "pozione con benedizione e con effetti noti",
    "# Suona un effetto quando raccogli un minerale.",
    "ogni minerale:sound24",

    # ------------------------------------------------------- l'elenco italiano
    "### Tutte le chiavi ###",
    "# ogni oggetto",
    "# oggetto senza nome",
    "# oggetto con nome noto",
    "# oggetto con pregio noto",
    "# oggetto con effetti noti",
    "# oggetto senza valore",
    "# oggetto marcio",
    "# oggetto vuoto",
    "# oggetto scadente",
    "# oggetto comune",
    "# oggetto eccellente",
    "# oggetto eccezionale",
    "# oggetto celestiale",
    "# oggetto speciale",
    "# oggetto prezioso",
    "# oggetto con benedizione",
    "# oggetto senza maledizione",
    "# oggetto con maledizione",
    "# oggetto con dannazione",
    "# oggetto in vita",
    "# oggetto di evoluzione",
    "# ogni equipaggiamento",
    "# ogni arma da mischia",
    "# ogni elmo",
    "# ogni scudo",
    "# ogni armatura",
    "# ogni stivale",
    "# ogni cintura",
    "# ogni mantello",
    "# ogni guanto",
    "# ogni arma da tiro",
    "# ogni dardo",
    "# ogni anello",
    "# ogni collana",
    "# ogni pozione",
    "# ogni pergamena",
    "# ogni grimorio",
    "# ogni libro",
    "# ogni bacchetta",
    "# ogni commestibile",
    "# ogni attrezzo",
    "# ogni mobilio",
    "# ogni pozzo",
    "# ogni altare",
    "# ogni resto",
    "# ogni cianfrusaglia",
    "# ogni moneta d'oro",
    "# ogni moneta di platino",
    "# ogni baule",
    "# ogni minerale",
    "# ogni albero",
    "# ogni cibo da viaggio",
    "# ogni merce da commercio",

    # ------------------------------------------- l'elenco inglese, per il wiki
    "### Le stesse chiavi in inglese: NON agganciano in questa versione, servono a leggere le guide in rete ###",
    "# all item",
    "# unknown item",
    "# name identified item",
    "# quality identified item",
    "# fully identified item",
    "# worthless item",
    "# rotten item",
    "# empty item",
    "# bad item",
    "# good item",
    "# great item",
    "# miracle item",
    "# godly item",
    "# special item",
    "# precious item",
    "# blessed item",
    "# uncursed item",
    "# cursed item",
    "# doomed item",
    "# alive item",
    "# evolution item",
    "# all equipment",
    "# all melee weapon",
    "# all helm",
    "# all shield",
    "# all armor",
    "# all boot",
    "# all belt",
    "# all cloak",
    "# all glove",
    "# all ranged weapon",
    "# all ammo",
    "# all ring",
    "# all necklace",
    "# all potion",
    "# all scroll",
    "# all spellbook",
    "# all book",
    "# all rod",
    "# all food",
    "# all tool",
    "# all furniture",
    "# all well",
    "# all altar",
    "# all remains",
    "# all junk",
    "# all gold piece",
    "# all platinum coin",
    "# all chest",
    "# all ore",
    "# all tree",
    "# all traveler's food",
    "# all cargo",
]


def main(percorso):
    voci = [json.loads(r) for r in io.open(percorso, encoding="utf-8") if r.strip()]

    # ⚠️ La prova che il testo e' allineato al lotto: una riga in piu' o in meno
    # scivolerebbe su tutte quelle che vengono dopo, in silenzio.
    if len(RIGHE) != len(voci):
        raise SystemExit(f"{len(RIGHE)} rese contro {len(voci)} righe inglesi")

    for voce, resa in zip(sorted(voci, key=lambda v: v["riga"]), RIGHE):
        voce["it"] = resa

    with io.open(percorso, "w", encoding="utf-8", newline="\n") as f:
        for v in voci:
            f.write(json.dumps(v, ensure_ascii=False) + "\n")
    print(f"{sum(1 for v in voci if v['it'])} rese su {len(voci)} righe")


if __name__ == "__main__":
    main(sys.argv[1])
