# -*- coding: utf-8 -*-
"""La toppa delle sei voci del menu del titolo, che il dizionario non raggiunge.

`system.hsp:3540` non usa `lang()`: assegna le sei voci **nude** dentro un ramo
`if ( en )`, con il ramo giapponese accanto che ne ha dodici (nome e didascalia
alternati). E' la quindicesima forma di punto cieco del progetto, e la stessa
che la 64a aveva gia' catalogato — «un ramo `jp`, un `if ( en )`».

    if ( jp ) {
        s = "Restore an adventurer", "冒険を再開する", ... (dodici)
    }
    if ( en ) {
        s = "Restore an Adventurer", "Generate an Adventurer", ... (sei)
    }

⚠️ **Solo il ramo `en` si tocca.** Il ramo `jp` alterna una riga inglese e una
giapponese ed e' letto da un'altra parte del disegno: cambiarlo sposterebbe gli
indici di un menu che non stiamo guardando.

## Le rese vengono dal giapponese, che dice piu' dell'inglese

    Restore an Adventurer     冒険を再開する        «riprendere l'avventura»
    Generate an Adventurer    新しい冒険者を作成する  «creare un avventuriero nuovo»
    Incarnate an Adventurer   冒険者の引継ぎ        «ereditare da un avventuriero»
    View the Homepage         本家Elonaホームページ  «la pagina della casa madre»
    Options                   設定の変更
    Exit                      終了

⭐ «Incarnate» in inglese non dice niente a chi non sa gia' che cos'e': il
giapponese 引継ぎ e' «subentro, eredita'», ed e' esattamente quel che la voce fa
— cominciare una partita nuova coi geni di un personaggio morto. La resa lo dice.

⚠️ **«Impostazioni», non «Opzioni»**: il menu dell'ESC in partita
(`command.hsp`) dice gia' «Impostazioni», e la 52a ha imparato a sue spese che la
porta e la stanza devono chiamarsi allo stesso modo. La voce inglese qui e'
«Options» e in partita e' un'altra parola: siamo noi a renderle coerenti.

## Il tetto

La finestra e' `display_window 80, winposy(308, 1), 320, 320` e le voci partono
dopo la lettera e l'icona. Misurato sulla schermata del 2026-08-19:
«Incarnate an Adventurer», 23 caratteri, occupa 176 px a partire da x 156, e il
bordo destro della finestra sta a 400 — restano 244 px, cioe' **32 caratteri**.
La piu' lunga delle sei rese ne fa 26.
"""
import io
import json

VECCHIA = ('\t\ts = "Restore an Adventurer", "Generate an Adventurer", '
           '"Incarnate an Adventurer", "View the Homepage", "Options", "Exit"')
NUOVA = ('\t\ts = "Riprendi un\'avventura", "Crea un avventuriero", '
         '"Eredita da un avventuriero", "Sito ufficiale di Elona", '
         '"Impostazioni", "Esci"')

TETTO = 32
for voce in NUOVA.split('", "'):
    v = voce.strip().strip('"').replace('\t\ts = "', '')
    if len(v) > TETTO:
        raise SystemExit(f"{v!r} fa {len(v)} caratteri, tetto {TETTO}")

toppa = {
    "file": "system.hsp",
    "cerca": VECCHIA,
    "sostituisci": NUOVA,
    "motivo": (
        "Le sei voci del menu del titolo -- la PRIMA schermata che vede chiunque "
        "apra il gioco -- sono assegnate nude dentro il ramo `if ( en )` di "
        "system.hsp:3540, senza lang(): il dizionario non le raggiunge. Trovate "
        "inglesi dal collaudo della 68a. Si tocca il solo ramo `en`; il ramo `jp` "
        "accanto alterna nome e didascalia su dodici elementi e cambiarlo "
        "sposterebbe gli indici. Le rese vengono dal giapponese, che dice piu' "
        "dell'inglese: 引継ぎ e' «subentro», non l'oscuro «Incarnate». "
        "«Impostazioni» e non «Opzioni» per accordarsi al menu dell'ESC in "
        "partita, che dice gia' cosi'. Tetto della finestra 32 caratteri "
        "(320 px di larghezza, voci da x 156 a 400, 7,6 px per carattere "
        "misurati sulla schermata del 2026-08-19); la piu' lunga ne fa 26."
    ),
}

io.open("scratchpad/_toppe-menu-titolo.jsonl", "w", encoding="utf-8",
        newline="").write(json.dumps(toppa, ensure_ascii=False) + "\n")
print("scritta scratchpad/_toppe-menu-titolo.jsonl")
for voce in NUOVA.split("s = ")[1].split(", "):
    print("   ", voce)
