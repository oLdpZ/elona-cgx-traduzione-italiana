# strumenti/funzioni.py
"""Classificazione delle funzioni HSP che compaiono nelle espressioni dinamiche.

Non tutte le chiamate dentro un'espressione dinamica sono contenuto. Alcune sono
grammatica **inglese**, e in italiano vanno tolte: `_s(tc)` restituisce la `s`
della terza persona, `your(tc)` il suffisso possessivo `'s`. Conservarle
significherebbe scrivere inglese dentro una frase italiana.

La distinzione fra le due classi non ovvie sta nel valore restituito, verificato
leggendo `init.hsp` (Fase 1, task 1 — vedi `.superpowers/sdd/2026-08-06-fase-1-
ui-e-messaggi/task-1-report.md` per l'elenco completo delle prove):

- **morfologia**: restituisce sempre una stringa inglese nuda, mai passata da
  `lang()`. Non si localizzera' mai, qualunque cosa succeda in Fase 4. In
  italiano va tolta.
- **pronome**: restituisce (almeno nel ramo che conta per l'uso reale nel
  corpus) `lang("彼", "he")` e simili, quindi si localizzera' insieme a
  `init.hsp` in Fase 4. Tenerla o toglierla sono due scelte entrambe
  legittime, e la verifica non deve imporne nessuna.

Tutto il resto e' contenuto e va conservato: perdere `name(tc)` significa
perdere il nome del personaggio dalla frase.

Un caso non entra in nessuna delle due liste apposta: `his2(EntityID)`. Il suo
codice sorgente e':

    if ( EntityID == CHARA_PLAYER ) { return "your" }
    return name(EntityID)

Nel ramo non-giocatore restituisce il nome vero del personaggio (contenuto),
non morfologia ne' pronome: classificarla in uno dei due set le farebbe
perdere un nome reale. Resta contenuto per esclusione (comportamento di
default di `funzioni_di_contenuto`), com'e' corretto che sia finche' non la
si vede usata nel corpus con un'analisi caso per caso.
"""
import re

# Verificate su init.hsp: restituiscono SEMPRE una stringa inglese nuda,
# mai attraverso lang(). _s/_s2/_s3/_s4 sono varianti della stessa desinenza
# di terza persona ("s"/"es"/""); him2/his3/its/its2/your2/yourself sono
# varianti di possessivi e riflessivi inglesi che, a differenza di he/his/him,
# non hanno alcun ramo che passa da lang() — restano inglese per sempre.
# have/does sono coniugazioni verbali (has/have, do/does), stesso discorso.
MORFOLOGIA_INGLESE = frozenset({
    "_s", "_s2", "_s3", "_s4",
    "is", "was", "your", "your2",
    "have", "does",
    "him2", "his3", "its", "its2", "yourself",
})

# Verificate su init.hsp: restituiscono lang("彼", "he") e simili (almeno nel
# ramo usato nel corpus reale, es. he(tc, 1)): si localizzeranno con init.hsp
# in Fase 4. A differenza della morfologia, tenerle o toglierle in italiano
# sono due scelte entrambe legittime.
PRONOMI = frozenset({"he", "his", "him"})

_CHIAMATA = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(")


def funzioni_di_contenuto(espressione: str) -> list[str]:
    """Le chiamate che devono sopravvivere alla traduzione, ordinate."""
    return sorted(
        nome for nome in _CHIAMATA.findall(espressione)
        if nome not in MORFOLOGIA_INGLESE and nome not in PRONOMI
    )
