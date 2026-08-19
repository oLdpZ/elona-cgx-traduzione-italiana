# -*- coding: utf-8 -*-
"""Lotto `system-avvio`: le schermate che il giocatore vede PRIMA di giocare.

⚠️⚠️ `system.hsp` ha **65 `lang()` e nessun file di dizionario**: e' uno dei
quattordici punti ciechi, e nessun conteggio del progetto lo nominava. Dentro ci
sono le **prime due schermate del gioco** — il menu del titolo e la scelta del
salvataggio — trovate inglesi dal collaudo della 68a. E' la lezione della 54a
nella sua forma piu' cara: *un file senza file di dizionario non e' un file
finito, e' un file che nessun conteggio guarda*.

Un lotto e' una classe, e questa classe e' **il percorso d'avvio**: dal riquadro
delle condizioni d'uso fino al momento in cui la partita comincia. Le altre 41
voci di `system.hsp` — i messaggi di aggiornamento del salvataggio, la creazione
dei PNG su misura — sono un'altra domanda e restano fuori.

## I tetti, calcolati e non stimati

La linguetta del titolo di `display_window` **cresce col testo**
(`module.hsp:4328`):

    window2 arg1 + 34, arg2 - 4, 45 * arg3 / 100 + limit(strlen(s) * 8 - 120, 0, 200), 32

Perche' stia dentro la finestra serve `34 + 0,45*L + limit(...) <= L`:

    :3526  finestra 320   ->  limit <= 142  ->  32 caratteri
    :3683  finestra 440   ->  limit <= 208, ma il `limit` taglia a 200  ->  40

⭐ Quindi il titolo NON e' vincolato alla lunghezza di monte, ed e' il motivo per
cui `:3526` puo' permettersi di rimettere quel che l'inglese aveva buttato via.

## ⭐ Due punti in cui l'inglese appiattisce e il giapponese no

`:3526` dice 冒険の道標, «il segnavia dell'avventura»: monte l'ha ridotto a
«Starting Menu», che e' il nome di un menu qualunque. Ventisei caratteri stanno
nei trentadue, quindi l'immagine si puo' tenere.

`:3655` dice どの冒険を再開するんだい？, cioe' «quale **avventura** vuoi
riprendere?» — non «quale file di salvataggio», che e' quel che dice monte. Ed e'
anche piu' corto: 32 contro 39.

## ⚠️ E una divergenza che NON si ripara qui

Il riquadro delle condizioni d'uso (`:3469`) e' **piu' corto in inglese che in
giapponese**: il giapponese ha due punti in piu' (non spingere il gioco a chi non
lo cerca; segnalare i difetti con la scheda apposita). La resa italiana traduce
**l'inglese**, che e' la versione che questa build mostra: rimetterci i due punti
del giapponese vorrebbe dire far dire all'autore, in italiano, due condizioni che
in inglese non ha mai posto. E' una scelta, non una svista.

⚠️ Gli accenti si scrivono **veri**: e' `applica` a degradarli in fase di build.
⚠️ I `\\n` sono due caratteri dentro la stringa, non un a capo: si contano.
⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json

LOTTO = "lavoro/_system.jsonl"

CONDIZIONI = (
    "Elonaplus è gratuito ed è un'opera derivata da Elona. "
    "\\n * Il programma è ancora in sviluppo: ci sono difetti, e l'equilibrio "
    "di gioco può cambiare di colpo. "
    "\\n * Non c'è alcuna intenzione di sminuire gli autori, l'equilibrio o "
    "l'ambientazione dell'opera originale e delle altre opere derivate. "
    "\\n * Contiene molte rappresentazioni violente, sessuali e bizzarre. "
    "\\n * L'autore non risponde di alcun danno derivante dall'uso di questo "
    "programma: si usa a proprio rischio. "
    "\\n * Può usare il programma solo chi accetta le istruzioni e i punti "
    "qui sopra."
)

# (riga, inglese riconosciuto) -> italiano
RESE = {
    (3409, "The game is not saved in this map."):
        "Qui la partita non si salva.",
    (3469, None): CONDIZIONI,
    (3526, "Starting Menu"):
        "Il segnavia dell'avventura",
    (3655, "Which save game do you want to continue?"):
        "Quale avventura vuoi riprendere?",
    (3683, "Game Selection"):
        "Scelta dell'avventuriero",
    (3683, "BackSpace [Delete]  "):
        "BackSpace [Elimina]  ",
    (3733, "Do you really want to delete  ?"):
        '"Vuoi davvero eliminare " + playerid + "?"',
    (3739, "Are you sure you really want to delete  ?"):
        '"Ma davvero davvero vuoi eliminare " + playerid + "?"',
    (3769, "Which gene do you want to incarnate?"):
        "Quali geni vuoi ereditare?",
    (3794, "Gene Selection"):
        "Scelta dei geni",
    (5118, "The program is already running."):
        "Il gioco è già in esecuzione.",
}

# I tetti delle linguette di titolo, dal docstring
TETTI = {3526: 32, 3683: 40, 3794: 40}

righe, fatte = [], 0
with io.open(LOTTO, encoding="utf-8") as f:
    for l in f:
        if not l.strip():
            continue
        d = json.loads(l)
        chiave = (d["riga"], d["en"])
        if chiave not in RESE and (d["riga"], None) in RESE:
            chiave = (d["riga"], None)
        if chiave in RESE:
            it = RESE[chiave]
            tetto = TETTI.get(d["riga"])
            if tetto and len(it) > tetto:
                raise SystemExit(f"{it!r} fa {len(it)} caratteri, tetto {tetto}")
            d["it"] = it
            fatte += 1
        righe.append(json.dumps(d, ensure_ascii=False))

if fatte != len(RESE):
    raise SystemExit(f"attese {len(RESE)} voci, riempite {fatte}: non scrivo niente")

io.open(LOTTO, "w", encoding="utf-8", newline="").write("\n".join(righe) + "\n")

# ⚠️ Il controllo della 67a, che ormai sta dentro ogni lotto di prosa: i
# trattini lunghi e le virgolette tipografiche vengono da soli quando si scrive
# italiano corrente, CP932 li codifica su due byte e la build ne disegna uno per
# byte. A schermo uscirebbero sbagliati.
doppi = sorted({c for it in RESE.values() for c in it if ord(c) > 0x2000})
print(f"{fatte} voci riempite in {LOTTO}")
print(f"caratteri a due byte: {doppi if doppi else 'nessuno'}")
for (riga, _en), it in sorted(RESE.items()):
    tetto = TETTI.get(riga)
    misura = f"  ({len(it)}/{tetto})" if tetto else ""
    print(f"   :{riga:<6} {it[:70]!r}{misura}")
