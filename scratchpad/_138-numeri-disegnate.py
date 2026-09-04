"""Allinea nei documenti i numeri della rete `disegnate`.

⚠️ Il primo giro misurava 162 distinte / 160 invisibili. Poi quattro stringhe
sono uscite dal fronte entrando in `invariati.md` (`Dv:`, ` Pv:`, `Sp`, la
citazione di Ken il guerriero), e il `--confronto` e' stato allineato al
censimento perche' sottraesse la stessa lista. Le misure buone, rilette dopo:

    158 distinte disegnate e scoperte, su 11 file
    153 invisibili a `_PROSA`
    300 viste da `_PROSA` e non da questa rete

Un numero non si scrive finche' non e' stato appena letto: questi tre vengono
da `python -m strumenti.disegnate` e `--confronto` lanciati adesso.
"""
from strumenti import percorsi

CAMBI = {
    "piani/2026-09-04-fase-7-chi-disegna.md": [
        ("livelli insieme ne trova 162.",
         "livelli insieme ne trova 162 — 158 dopo che quattro sono uscite\n"
         "entrando in `invariati.md`."),
        ("    162 stringhe distinte disegnate e non coperte, su 12 file\n"
         "    160 di queste il censimento vecchio NON le vedeva\n"
         "    301 ne vede `_PROSA` che questa rete non vede (tracce di debug,",
         "    158 stringhe distinte disegnate e non coperte, su 11 file\n"
         "    153 di queste il censimento vecchio NON le vedeva\n"
         "    300 ne vede `_PROSA` che questa rete non vede (tracce di debug,"),
    ],
    "decisioni.md": [
        ("## La domanda aperta più grossa ha un numero: 160 — 2026-09-04",
         "## La domanda aperta più grossa ha un numero: 153 — 2026-09-04"),
        ("schermo** invece che dalla forma della stringa: **162 stringhe distinte\n"
         "disegnate e non coperte, su 12 file, di cui 160 che il censimento vecchio non\n"
         "vedeva.**",
         "schermo** invece che dalla forma della stringa: **158 stringhe distinte\n"
         "disegnate e non coperte, su 11 file, di cui 153 che il censimento vecchio non\n"
         "vedeva.**"),
        ("venti righe più giù. Coi due livelli insieme il conto è 162.",
         "venti righe più giù. Coi due livelli insieme il conto è 158."),
        ("⭐ **Le due reti si scoprono a vicenda, e nessuna basta.** `_PROSA` vede 301\n"
         "cose che `disegnate` non vede (tracce di debug, stringhe di dato, testo che\n"
         "passa per più di un salto); `disegnate` ne vede 160 che `_PROSA` non vede.",
         "⭐ **Le due reti si scoprono a vicenda, e nessuna basta.** `_PROSA` vede 300\n"
         "cose che `disegnate` non vede (tracce di debug, stringhe di dato, testo che\n"
         "passa per più di un salto); `disegnate` ne vede 153 che `_PROSA` non vede."),
    ],
    "RIPRESA-sessione.md": [
        ("⭐⭐ **Adesso c'e': 160.**", "⭐⭐ **Adesso c'e': 153.**"),
        ("Coi due insieme: **158 distinte, su 11 file**.",
         "Coi due insieme: **158 distinte su 11 file, e 153 di loro nessun\ncensimento le vedeva**."),
        ("per piu' di un salto); `disegnate` ne vede 160 che `_PROSA` non vede.",
         "per piu' di un salto); `disegnate` ne vede 153 che `_PROSA` non vede."),
    ],
    "avanzamento.md": [
        ("⭐⭐ **Il numero più importante della sessione non è 92: è 160.**",
         "⭐⭐ **Il numero più importante della sessione non è 92: è 153.**"),
        ("risponde: **158 stringhe distinte disegnate e non coperte, su 11 file, di cui\n"
         "160 invisibili al censimento vecchio** (il conto scende a 158 dopo che quattro\n"
         "sono uscite entrando in `invariati.md`).",
         "risponde: **158 stringhe distinte disegnate e non coperte, su 11 file, di cui\n"
         "153 invisibili al censimento vecchio**. ⓘ Il primo giro diceva 162 e 160: le\n"
         "quattro di differenza sono uscite dal fronte entrando in `invariati.md`, senza\n"
         "tradurre niente."),
    ],
}

for nome, coppie in CAMBI.items():
    percorso = percorsi.PROGETTO / nome
    testo = percorso.read_text(encoding="utf-8")
    for prima, dopo in coppie:
        if prima not in testo:
            raise SystemExit("%s: non trovo %r" % (nome, prima[:60]))
        testo = testo.replace(prima, dopo, 1)
    percorso.write_text(testo, encoding="utf-8")
    print("allineato: %s (%d cambi)" % (nome, len(coppie)))
