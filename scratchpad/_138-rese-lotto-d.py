"""Scrive le rese del lotto D dentro il file di lotto gia' estratto.

⚠️ Le chiavi NON si ricopiano a mano: tre di loro portano `\\"` dentro
(`tcg_skill.hsp:6630`) e una e' un punto esclamativo solo. Si indicizzano
sull'ordine del file di lotto, che questa sessione non ha piu' toccato.
"""
import json

from strumenti import percorsi

# numero nel dump di `_138-contesto.txt` -> resa, oppure ("", ragione)
RESE = {
    1: "Ahhh! Non voglio perdere!",
    2: "Sia la luce...",
    3: "Non e' mica colpa mia.",
    4: "Che tipo sospetto, ultimamente~",
    5: "Pfff! E quello che sarebbe~?",
    6: "Debolino~ debolino!",
    7: "Alloggio gratis!",
    8: ("", "verso di un motore: il camioncino del ladro (`CREATURE_ID_THIEF_"
            "LIGHT_TRUCK`). In italiano il rumore si scrive con le stesse "
            "lettere, e non c'e' nessuna parola dentro"),
    9: ("", "urlo: quattro lettere e tre punti esclamativi. Non e' una parola "
            "inglese, e' un suono, e in italiano si legge uguale"),
    10: "Niente mana? Tu mi ricordi... ehm..",
    11: ("", "punteggiatura, e la punteggiatura non ha lingua: e' il precedente "
             "di `???` (`chat.hsp:19135`), gia' dichiarato"),
    12: ("", "l'imprecazione mascherata dei fumetti (grawlix). Non sono parole: "
             "sono i segni sopra i tasti dei numeri, uguali in ogni lingua"),
    13: "H sta per HIGHLANDER!",
    14: "Giocare Highlander mi rende FELICE! FELICE!",
    15: "Qualcosa dall'aldila' ride.",
    16: "Costui e' noto come... aspetta.. non hai nessun CNPC nella cartella user?",
    17: "Non so che ti aspettassi, ma nella cartella user non hai nessun CNPC!",
    18: "Nessun CNPC nella cartella user? Ahhh! mi hai rovinato il piano!",
    19: "Mamma! Un'altra volta no!",
    20: "Renai, unisciti a me!",
    21: "Aspetta! Non adesso, fratello!",
    22: "Tezcatlipoca non si vede da nessuna parte. Strano.",
    23: "Tutto pronto! Si parte!",
    24: "Nessun sacrificio?",
    25: "Non c'e' nessuno in campo?",
    26: "Non hai posto in campo?",
    27: "Non hai carte in mano?",
    28: "Che spilorcio.",
    29: "Niente spazio in campo, sei rimbambito?",
    30: "..e fatto!",
    31: '\\"Hmm, stai giocando da ',
    32: " ore e ",
    33: ' minuti.\\"',
    34: "FELICI! FELICI! Dovete essere tutti FELICI!",
    35: "Mi avete stancato.",
    36: "Ho chiuso con i vostri giochi... Sarete tutti ridotti in cenere.",
    37: "<HOROBI NO YARI> Distruggi il giocatore bersaglio",
    38: "Mi ha stancato questo stupido gioco di carte.",
    39: "Ma ora che ho ottenuto questo potere immenso, e' una faccenda da nulla...",
    40: "<Origine del Caos> Cancella il testo della carta del Figlio del Caos",
    41: "Me ne vado, hai vinto.",
    42: "<Sospiro degli dei creatori>",
    43: "<Ruggito degli dei guerrieri>",
    44: "<Artigli degli dei bestiali>",
    45: "<Sentenza degli dei giudici>",
    46: "<Rancore degli dei abominevoli>",
    47: "<Comandamento degli dei infernali>",
    48: "<Fine di ogni cosa>",
    49: "Ahahah! Spero ti piaccia il mazzo di Aime, ",
    50: ("", "il punto esclamativo che chiude la battuta di <Aime> dopo "
             "`_onii()` (`tcg_skill.hsp:7435`): un segno, non una parola. "
             "L'italiano lo scrive uguale"),
    51: "Uno!",
    52: "Due!",
    53: "Tre!",
    54: "E..!",
    55: "Non puoi che invidiare il mio talento!",
    56: "Ecco come una vera maga usa il suo mana!",
    57: "Sentiti onorato, ho raccolto il mana che sprecavi!",
    58: "Non puoi che invidiare il... aspetta, niente mana?",
    59: "Uffa! Non mi hai lasciato neanche un po' di mana!",
    60: "Sentiti onorato, ho raccolto il tuo sprecato.. niente?!",
    61: "Non dirlo a mia figlia, okay?",
    62: "E' fatta! E' viva!",
    63: "Anche se mi chiedo se sia solo temporaneo...",
    64: "Okay! Scienza, si parte!?",
    65: "Non sono brava coi giochi di carte, eheh.",
    66: "Cosa giocherebbe Bethel...",
    67: "Il tuo mazzo fa SCHIFO, davvero!",
    68: "Ce l'hai Bethel nel mazzo, vero? Vero?",
    69: "Ma che mano e'?! Chikusho!",
    70: "Aaaaah! Sto per perdere!",
    71: "PESCA DEL DESTINO! Ma dai!",
    72: ("", "verso: la risata-lamento di <Rianna>, otto «a» e quattro «Oh». "
             "Non c'e' una parola dentro, e in italiano si legge uguale"),
    73: "Mollo tutto!! Mi arrendo!!",
    74: "Bethel... *snif*",
}

lotto = percorsi.LAVORO_LOTTI / "dialoghi-138-lotto-d.jsonl"
righe = [json.loads(r) for r in lotto.read_text(encoding="utf-8").splitlines()
         if r.strip()]
if len(righe) != len(RESE):
    raise SystemExit("il lotto ha %d voci e le rese sono %d: l'indice non"
                     " combacia piu'" % (len(righe), len(RESE)))

for numero, voce in enumerate(righe, 1):
    reso = RESE[numero]
    if isinstance(reso, tuple):
        voce["it"] = ""
        voce["invariata"] = reso[1]
    else:
        voce["it"] = reso

with lotto.open("w", encoding="utf-8") as scrittura:
    for voce in righe:
        scrittura.write(json.dumps(voce, ensure_ascii=False) + "\n")

rese = sum(1 for v in righe if v.get("it"))
print("scritte %d rese e %d invariate su %d voci"
      % (rese, len(righe) - rese, len(righe)))
