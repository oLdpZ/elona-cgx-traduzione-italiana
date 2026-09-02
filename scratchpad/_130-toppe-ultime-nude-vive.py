# -*- coding: utf-8 -*-
"""Le quattro righe nude ancora VIVE, e perche' erano solo quattro su sessanta.

## Il conto che sembrava sessanta

`triage_nudi` da' **60 righe di classe `testo`**, e la ripresa della 129a le
chiamava «il lavoro vero». Non lo erano: `_130-residuo-delle-righe-nude.py`
incrocia le 60 coi siti nominati in `invariati.md`, `decisioni.md` e
`rinviate.jsonl` e ne trova **38 gia' decise** — le sigle `Hp:`/`Lv.`/`Dv:`/`Pv:`
della colonna da venti caratteri, le chiavi di `config.txt`, il TSV
dell'autopick, `helloworld.hsp` che non sta nemmeno nella build.

⚠️⚠️ **Il referto lo dice di se stesso** (`invariati.md`, 127a): quei conti
contano i letterali **intatti**, e una riga che deve restare intatta e'
indistinguibile da una che nessuno ha guardato.

Delle 22 rimaste, guardate una per una, **quattro sono vive**. Le altre
diciotto:

    system.hsp:3521 e :3537     nel ramo `if ( jp )`: il menu iniziale vivo e'
                                a :3524 e :3540, ed e' gia' italiano
    item_func.hsp:1020          nel ramo `if ( jp )`
    item_func.hsp:1894 :1905    il pluralizzatore inglese, **gia' spento da una
                :1915 :1918     toppa**: `if ( locvar_itemname_s2 == "" )` e'
                :1921           diventato `if ( 0 )`, e il plurale italiano
                                viene da `ioriginalnamerefplur`
                                (`contratto-nomi.md` §4-bis). Codice morto.
    map_rand.hsp:691-:699       nomi di campo del file `mapinfo_%06d.txt`, come
                                il TSV di `custom_itemlist.hsp:49`: un file, non
                                una schermata
    main.hsp:3258               dentro il tasto F7 del modo mago
    item_data.hsp:339           `"error:"`, il ripiego diagnostico di
                                `*item_encdetail`: tradurlo nasconderebbe la sua
                                natura a chi segnala un difetto
    init.hsp:536                ⚠️⚠️⚠️ **`"user"` NON e' testo: e' l'OPERANDO di
                                due `sreplace`** (`item_func.hsp:967` e `:1073`),
                                che dentro il nome composto dell'oggetto
                                sostituiscono quella parola col nome del PNG
                                personalizzato. Tradurla spegnerebbe i due siti
                                in silenzio -- la famiglia della 128a, da un lato
                                che nessuna rete guarda: il cancello di allora
                                cerca `X == lang(J, E)`, non `sreplace`.
                                ⓘ Misurato: nella build `db_creature.hsp:97539`
                                torna ancora `lang("user", "user")`, quindi
                                **oggi i due rami sono vivi**. Il giorno in cui
                                quel nome verra' tradotto moriranno.

## Le quattro

    init.hsp:537      "unknown user"          -> «utente sconosciuto»
    quest.hsp:782     "You harvest rating…"   -> «Voto del raccolto: … (…s)!»
    text.hsp:11912    "Performance Score: …"  -> «Punteggio dell'esibizione: …»
    text.hsp:12104    "[News] "               -> «[Notizie] »

⭐ **`[Notizie]` non e' una scelta: e' gia' scritta.** Il diario intitola la sua
sezione `" - Notizie - "` e scrive «Nessuna notizia» quando e' vuota
(`command.hsp:2854` e `:2851`), e le testate delle notizie sono italiane da
sessioni («Scoperta», «Nuova forza», «Guarigione»). Il prefisso era l'unico
pezzo inglese di un sistema tutto tradotto.

⭐ **«Esibizione» viene dal glossario**, non dall'orecchio: `skill.hsp:357`
rende `Performer` con «Esibizione», e `action.hsp:7350` «Ottiene bonus in
Esibizione». La missione e' `QUEST_TYPE_PARTY`.

⚠️ **La `s` di `(3s)` resta.** `seedp` non e' il numero dei semi — quelli sono
`1 + (seedp - 120) / 150` — e che cosa misuri quella lettera il sorgente non lo
dice. Un'unita' opaca si ricopia; inventarne una vuol dire scrivere un dato che
il gioco non ha. ⓘ E l'inglese ha un refuso, «You» per «Your»: l'italiano non lo
eredita, perche' in italiano il possessivo non c'e' proprio.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-toppe-ultime-nude-vive.py
"""
import io
import json
import sys

from strumenti import percorsi

# file, riga nel SORGENTE PINNATO, pezzo da cambiare, pezzo nuovo, motivo
LAVORO = [
    ("init.hsp", 537, '"unknown user"', '"utente sconosciuto"',
     "LETTERALE INGLESE NUDO: il nome di ripiego di `*getcnpcnamebychecksum` "
     "quando la somma di controllo di un PNG personalizzato non trova "
     "riscontro. Finisce a schermo dentro il nome dell'oggetto: i due "
     "`sreplace` di `item_func.hsp:967` e `:1073` sostituiscono con questo "
     "valore la parola «user» nel nome composto di carte, statuette e parti. "
     "⚠️⚠️ La riga sopra, `:536`, torna `\"user\"` e NON si tocca: quella e' "
     "l'operando che i due `sreplace` cercano, non testo. Tradurre l'una e non "
     "l'altra e' la distinzione che conta."),
    ("quest.hsp", 782,
     '"You harvest rating is: " + str(seedp2) + " (" + str(seedp) + "s)!"',
     '"Voto del raccolto: " + str(seedp2) + " (" + str(seedp) + "s)!"',
     "LETTERALE INGLESE NUDO: l'esito della missione di raccolta dei ritocchi "
     "(`TWEAK_GAMEPLAY_CUSTOM_JOB_QUESTS`), stampato con `txt` nel registro. "
     "⚠️ L'inglese ha un refuso, «You» per «Your»; l'italiano non lo eredita "
     "perche' il possessivo li' non serve. ⓘ La `s` di `(3s)` si ricopia: "
     "`seedp` non e' il numero dei semi (quelli sono `1 + (seedp - 120) / 150`) "
     "e il sorgente non dice che unita' sia. Un'unita' opaca non si inventa."),
    ("text.hsp", 11912,
     '"Performance Score: " + qdata(QDATA_PARAM2, rq) + " points!"',
     '"Punteggio dell\'esibizione: " + qdata(QDATA_PARAM2, rq) + " punti!"',
     "LETTERALE INGLESE NUDO: il punteggio della missione di intrattenimento "
     "(`QUEST_TYPE_PARTY`), stampato con `txt` accanto a due frasi che passano "
     "gia' da `lang()` ed erano italiane. «Esibizione» viene dal glossario: "
     "`skill.hsp:357` rende `Performer` cosi', e `action.hsp:7350` dice "
     "«Ottiene bonus in Esibizione»."),
    ("text.hsp", 12104, '"[News] "', '"[Notizie] "',
     "LETTERALE INGLESE NUDO: il prefisso con cui `*addnews2` annuncia una "
     "notizia nel registro. ⭐ Non e' una scelta di parola: il diario intitola "
     "la sezione `\" - Notizie - \"` (`command.hsp:2854`), scrive «Nessuna "
     "notizia» quando e' vuota (`:2851`) e le testate sono italiane da sessioni "
     "(«Scoperta», «Nuova forza», «Guarigione»). Era l'unico pezzo inglese di "
     "un sistema tutto tradotto."),
]


def main() -> int:
    nuove = []
    for nome, numero, vecchio, nuovo, motivo in LAVORO:
        percorso = percorsi.SORGENTE_HSP / nome
        # ⚠️⚠️ `.rstrip("\r")`: il sorgente pinnato e' CRLF, e spezzando su
        # "\n" ogni riga si porta dietro il ritorno a carrello. `applica`
        # confronta righe **senza** fine riga (`spezza_righe`), quindi una
        # `cerca` col `\r` non combacia con niente e il contratto delle toppe
        # diventa rosso -- com'e' successo al primo giro, ed e' il verso
        # giusto: la rete ha fermato quattro toppe mute prima della build.
        righe = [r.rstrip("\r") for r in
                 percorso.read_bytes().decode("cp932").split("\n")]
        riga = righe[numero - 1]
        if vecchio not in riga:
            print("⚠️ %s:%d non contiene %r\n   riga: %r"
                  % (nome, numero, vecchio, riga))
            return 1
        if riga.count(vecchio) != 1:
            print("⚠️ %s:%d contiene %r piu' di una volta" % (nome, numero, vecchio))
            return 1
        # ⚠️ la riga dev'essere unica nel file: una toppa a riga singola che
        #    combacia due volte e' ambigua, e `applica` la rifiuta
        if righe.count(riga) != 1:
            print("⚠️ %s:%d non e' unica nel file (%d volte): vuole un blocco"
                  % (nome, numero, righe.count(riga)))
            return 1
        nuove.append({
            "file": nome,
            "cerca": riga,
            "sostituisci": riga.replace(vecchio, nuovo),
            "motivo": motivo,
        })

    percorso = percorsi.PROGETTO / "toppe.jsonl"
    # toglie le toppe che un giro precedente di QUESTO script puo' aver scritto
    # col `\r` in coda: sono mute per costruzione, e vanno via prima di riprovare
    esistenti = []
    scartate = 0
    for l in io.open(percorso, encoding="utf-8").read().splitlines():
        if not l.strip():
            continue
        t = json.loads(l)
        if isinstance(t["cerca"], str) and "\r" in t["cerca"]:
            scartate += 1
            continue
        esistenti.append(l)
    if scartate:
        print("toppe col `\\r` in coda, scartate: %d" % scartate)
    gia = {json.loads(l)["cerca"] for l in esistenti
           if isinstance(json.loads(l)["cerca"], str)}
    da_scrivere = [t for t in nuove if t["cerca"] not in gia]
    if len(da_scrivere) != len(nuove):
        print("⚠️ %d toppe erano gia' dentro: non riscrivo"
              % (len(nuove) - len(da_scrivere)))
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(
        "\n".join(esistenti + [json.dumps(t, ensure_ascii=False)
                               for t in da_scrivere]) + "\n")
    print("toppe aggiunte: %d   (toppe in tutto: %d)"
          % (len(da_scrivere), len(esistenti) + len(da_scrivere)))
    for t in da_scrivere:
        print("   %-14s %s" % (t["file"], t["sostituisci"].strip()[:90]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
