# -*- coding: utf-8 -*-
"""`Gauge` aveva tre rese, e il glossario ne aveva decisa una nella 5a.

## Che cosa ha trovato la rete

`_130-glossario-nelle-toppe.py` ha segnalato una toppa di `custom_tweaks.hsp`
che scrive «Forza liberata» dove `glossario.md:72` dice **Barra**. Tirando il
filo, la divergenza non era della toppa: e' del progetto, ed e' su sei siti.

    barra    ~12 siti   action, buff, chat, command, config, custom_ai, custom_tweaks
    forza      3 siti   skill.hsp:1528, custom_tweaks.hsp:1255 e :1260, e due toppe
    carica     2 siti   command.hsp:1361 (dizionario) e command.hsp:191 (toppa)

## ⚠️⚠️⚠️ La prova che chiude la questione sta su due righe adiacenti

Il nome della mossa speciale e la sua descrizione si leggono **sulla stessa riga
dell'elenco**, e nominano la stessa risorsa con due parole diverse:

    skill.hsp:1528          «<Serba/libera la forza>»
    skill.hsp:1529          «Attiva o disattiva la barra»

    custom_tweaks.hsp:1255  «<Forza liberata>»
    custom_tweaks.hsp:1256  «Mossa di barra al colpo dopo»

E lo stesso pannello d'aiuto (toppa di `custom_tweaks.hsp:929`) dice tutte e due
**dentro lo stesso paragrafo**: «Torna al modo di attivare **la barra**… Prima si
premeva **Forza liberata**… E azzera **la barra** a inizio turno».

Non serve riaprire il term base: serve applicarlo.

## Perche' «barra» e non «forza», che pure e' piu' fedele al giapponese

⚠️ Il giapponese e' `【力の解放】`, «liberazione della **forza**»: «Forza
liberata» rende la fonte, e l'inglese `<Gauge Release>` e' gia' una scelta del
localizzatore inglese, che ha battezzato la mossa col nome dello **strumento**
invece che con quello della risorsa.

Si sceglie lo stesso l'inglese, per una ragione che non e' di fedelta' ma di
riconoscibilita': la 5a sessione ha deciso `Gauge` -> «Barra» **misurando** —
60 occorrenze su 75 sono etichette a larghezza compressa, `[50% Gauge] Party
Shooting` -> `[Barra 50%]`, e «Barra» costa 5 caratteri come l'inglese. Quelle
sessanta etichette sono il contatto principale del giocatore con la meccanica.
Una mossa che si chiama «Forza» e costa «Barra» chiede al giocatore di tenere
in testa due nomi per una cosa sola.

⭐ **Una parola sola, e sono sei siti.** «Potenza» resta dov'e' — `Power` ->
«Potenza», e in prosa la forma piena e' «barra di potenza» — ma non entra nei
nomi delle mosse: sarebbe la terza parola.

⚠️ `custom_ai.hsp` la condizione dell'IA diceva gia' **«Barra»** (toppa a
`:631`): l'elenco con cui il giocatore configura l'IA sulla stessa risorsa era
l'unico posto gia' in regola.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-una-parola-sola-per-la-barra.py
"""
import io
import json
import sys

from strumenti import percorsi

# (file, riga) -> (italiano vecchio, italiano nuovo)
RESE = {
    ("skill.hsp", 1528): ("<Serba/libera la forza>", "<Serba/libera la barra>"),
    ("custom_tweaks.hsp", 1255): ("<Forza liberata>", "<Libera la barra>"),
    ("custom_tweaks.hsp", 1260): ("<Serba/libera la forza>", "<Serba/libera la barra>"),
    ("command.hsp", 1361): ('" Carica:" + cdata(CDATA_POWER_GAUGE, i) + "%"',
                            '" Barra:" + cdata(CDATA_POWER_GAUGE, i) + "%"'),
}

# le toppe si riconoscono dal testo che scrivono, che non hanno un numero di riga
TOPPE = [
    ('"Torna alla Forza liberata di prima della 2.24."',
     '"Torna al modo di liberare la barra pre-2.24."'),
    ('Prima si premeva Forza liberata e poi si attaccava.',
     'Prima si liberava la barra e poi si attaccava.'),
    ('"  Carica:"', '"  Barra:"'),
]


def scrivi_dizionario() -> int:
    fatte = 0
    for nome in sorted({f for f, _ in RESE}):
        percorso = percorsi.DIZIONARIO / ("%s.jsonl" % nome)
        fuori = []
        for linea in io.open(percorso, encoding="utf-8").read().splitlines():
            if not linea.strip():
                fuori.append(linea)
                continue
            voce = json.loads(linea)
            chiave = (voce["file"], voce["riga"])
            if chiave in RESE:
                vecchio, nuovo = RESE[chiave]
                if voce.get("it") != vecchio:
                    print("⚠️ %s:%d non porta la resa attesa (%r): non scrivo niente"
                          % (chiave[0], chiave[1], voce.get("it")))
                    return -1
                voce["it"] = nuovo
                fatte += 1
            fuori.append(json.dumps(voce, ensure_ascii=False))
        io.open(percorso, "w", encoding="utf-8", newline="\n").write(
            "\n".join(fuori) + "\n")
    return fatte


def scrivi_toppe() -> int:
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    fuori = []
    fatte = 0
    for linea in io.open(percorso, encoding="utf-8").read().splitlines():
        if not linea.strip():
            fuori.append(linea)
            continue
        toppa = json.loads(linea)
        sostituisci = toppa["sostituisci"]
        if isinstance(sostituisci, str):
            for vecchio, nuovo in TOPPE:
                if vecchio in sostituisci:
                    toppa["sostituisci"] = sostituisci.replace(vecchio, nuovo)
                    fatte += 1
                    break
        fuori.append(json.dumps(toppa, ensure_ascii=False))
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(
        "\n".join(fuori) + "\n")
    return fatte


def main() -> int:
    n = scrivi_dizionario()
    if n < 0:
        return 1
    m = scrivi_toppe()
    print("rese di dizionario cambiate : %d su %d attese" % (n, len(RESE)))
    print("toppe cambiate              : %d su %d attese" % (m, len(TOPPE)))
    return 0 if (n == len(RESE) and m == len(TOPPE)) else 1


if __name__ == "__main__":
    sys.exit(main())
