# -*- coding: utf-8 -*-
"""`db_class.hsp` — i 13 nomi di classe e le 12 descrizioni della creazione.

Il gemello di [[lotto-db_race-001]]: la finestra «Scelta della classe», la
seconda che un giocatore nuovo legge. Stessa geometria, stessi due tetti — 20
caratteri per il nome, **7 righe** per la descrizione ([[descrizioni_cm.py]]).

⚠️ **`classname` è l'etichetta, `CDATAN_CLASS` è la chiave.** Come per le razze:
la chiave è confrontata con letterali inglesi in 28 siti e non sta dentro una
`lang()`, quindi il dizionario non la raggiunge. `classname` invece non è
confrontato da nessuna parte — zero siti — ed è pura etichetta.

⚠️⚠️ **Qui l'inglese sfonda da solo**: sette descrizioni su dodici fanno **8
righe** e a schermo l'ottava finisce sopra «Bonus attributi» — il collaudo della
64a l'ha fotografato sulla classe Warrior, dove «[Onslaught] Increased chance…»
si sovrappone all'intestazione. Le rese italiane stanno tutte in **7**: qui
tradurre *ripara* un difetto di monte invece di limitarsi a non peggiorarlo.

## I nomi dei tratti vengono dal giapponese, che l'inglese ha appiattito

    猛攻      Onslaught             Attacco furioso
    奇襲      Ambush                Imboscata
    魔力循環  Magic Circulation     Circolo di mana
    ハーヴェスト Harvest            Raccolto
    強襲      Assault               Assalto
    鷹の眼    Hawk Eye              Occhio di falco    <- già reso in trait.hsp
    精神統一  Unified Mind          Concentrazione
    不用心    Careless              Imprudenza
    音楽干渉  Musical Interference  Interferenza musicale
    弾幕      Barrage               Sbarramento
    慈愛      Compassion            Compassione
    旋空剣    Drill Sword           Spada turbinante

⚠️ **`Onslaught` in inglese sono due cose diverse**: qui è 猛攻, il tratto del
guerriero; in `chat.hsp` è 突撃, la direttiva di combattimento degli alleati, già
resa «assalto» in `command.hsp:1350`. Il giapponese le distingue e l'inglese no:
seguendo l'inglese si sarebbe scritto lo stesso nome per due cose che non si
somigliano.

⚠️ Niente virgolette nei motti: dentro una stringa HSP andrebbero protette, e
`guardie.py` vieta le caporali. Le frasi sono girate in discorso indiretto.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import descrizioni_cm as D
from strumenti.accenti import degrada

ESTRAZIONE = "lavoro/_db_class.jsonl"
USCITA = "lavoro/fase4-db_class-001.jsonl"
TETTO_NOME = 20

NOMI = {
    31: "Nessuna",          # なし — l'etichetta quando la classe non c'è
    43: "Guerriero",        # 戦士
    101: "Ladro",           # 遺跡荒らし «predone di rovine»; ma la gilda è già «Gilda dei Ladri»
    156: "Mago",            # 魔法使い
    210: "Contadino",       # 農民
    263: "Predatore",       # プレデター
    315: "Arciere",         # 狩人
    370: "Mago guerriero",  # 魔法戦士 — il jp dice esattamente questo, l'inglese conia «Warmage»
    425: "Turista",         # 観光客
    471: "Pianista",        # ピアニスト
    524: "Fuciliere",       # 機工兵 — combatte con le armi da fuoco
    578: "Sacerdote",       # プリースト
    # 633 «Claymore» NON sta qui: è identica all'inglese e `reimporta` la
    # rifiuta, giustamente. Il giapponese usa lo stesso prestito (クレイモア)
    # e la classe prende il nome dall'arma, che la sua stessa descrizione
    # cita. Dichiarata in `invariati.md`.
}

DESCRIZIONI = {
    47: (  # Guerriero
        "Il guerriero sa tutto di armi che pungono, spezzano, tagliano e "
        "sparano: qualunque cosa gli finisca in mano è una brutta notizia per i "
        "nemici. Conosce le tattiche per abbattere anche i più forti ed è "
        "addestrato fin da giovane a muoversi con ogni armatura e scudo. Il suo "
        "motto: se la violenza non funziona, non ne stai usando abbastanza. "
        "*[Attacco furioso] Più probabilità di un colpo in più in mischia."
    ),
    105: (  # Ladro
        "Il ladro se la cava con spade e archi, ma non crede nella lotta leale "
        "e preferisce evitare i colpi. Sa battersi con due armi, purché non "
        "troppo pesanti. Anni di trattative coi ricettatori gli hanno insegnato "
        "a spuntare prezzi migliori. Il suo credo: quel che è tuo è mio, e quel "
        "che è mio è mio. *[Imboscata] Critico garantito sui nemici che non ti "
        "hanno visto."
    ),
    160: (  # Mago
        "Il mago è padrone dell'arcano, dell'occulto e dell'esoterico. Peccato "
        "che tanti anni sui libri gli abbiano lasciato poco tempo per i muscoli "
        "e i riflessi. Se la cava appena con bastone e spada corta, e all'inizio "
        "è così gracile che un putit gli fa paura; ma con qualche libro e un po' "
        "di pratica falcerà legioni. *[Circolo di mana] Gli incantesimi costano "
        "meno MP."
    ),
    214: (  # Contadino
        "Il contadino non è un guerriero d'acciaio né un mago di gran letture: è "
        "un tuttofare. Bravo con le armi in asta per via della trebbiatura e "
        "abile a contrattare coi mercanti, mastica un po' di ogni mestiere. Così "
        "non resta mai a digiuno: c'è sempre qualcuno disposto a pagare caro un "
        "lavoro. *[Raccolto] Più probabilità di mozzare la testa."
    ),
    267: (  # Predatore
        "Il predatore è un combattente che conta sulla forza del proprio corpo "
        "invece che sull'equipaggiamento, e vanta capacità di mischia fuori dal "
        "comune. *[Assalto] Più probabilità di colpo critico."
    ),
    319: (  # Arciere
        "L'arciere conosce il bosco e la caccia, è un tiratore scelto e non vede "
        "perché si debba cacciare un mostro diversamente da un cervo. Se la cava "
        "con spada corta, ascia e naturalmente con ogni tipo di arco, più qualche "
        "arte raccolta nei lunghi viaggi fra gli alberi. Il suo credo: quel che è "
        "morto laggiù non verrà a disturbarmi quaggiù. *[Occhio di falco] Aumenta "
        "la precisione."
    ),
    374: (  # Mago guerriero
        "Non del tutto mago e non del tutto guerriero, per lui è meglio "
        "infilzare qualcosa che va a fuoco piuttosto che limitarsi a infilzarlo "
        "o a dargli fuoco. Bravo con spade, armature, libri e incantesimi. "
        "L'unico difetto è che senza specializzarsi non eccelle in nulla; ma il "
        "suo motto è che quel che vale la pena di fare vale la pena di "
        "strafare. *[Concentrazione] Più probabilità di riuscire a lanciare."
    ),
    429: (  # Turista
        "Il turista non ha punti di forza né debolezze. Non ha proprio niente. "
        "Sa pescare, questo sì, ma se cerchi la sfida vera di costruire tutto da "
        "zero è la strada giusta: gli devi insegnare ogni cosa. Solo per chi ha "
        "parecchio tempo da spendere. Il motto puoi anche scrivertelo da te. "
        "*[Imprudenza] I borseggiatori ti portano via più monete."
    ),
    475: (  # Pianista
        "Se il contadino ha tutte le abilità pratiche, il pianista ha tutte "
        "quelle inutili. Sa comunque leggere un libro, suonare un motivo, "
        "lavorare i gioielli, e siccome ci si aspetta che si porti dietro un "
        "pianoforte diventa bravissimo a sollevare pesi. Per lui il mondo intero "
        "è un palcoscenico, e ci crede davvero. *[Interferenza musicale] Buona "
        "probabilità di annullare i danni da suono."
    ),
    528: (  # Fuciliere
        "Il fuciliere è maestro di ogni arma meccanica e combatte soprattutto a "
        "distanza con le armi da fuoco. *[Sbarramento] Più probabilità di un "
        "tiro in più."
    ),
    582: (  # Sacerdote
        "Il sacerdote è il fedele, il devoto. Porta nel mondo la parola del suo "
        "dio, un eretico bastonato alla volta. Bravo con ogni armatura, con gli "
        "scudi, con la magia divina, le armi contundenti e la lettura. È un tipo "
        "impegnativo, e a seconda del dio può nascondere qualche brutta sorpresa. "
        "*[Compassione] Aumenta la cura dei PV."
    ),
    637: (  # Claymore
        "Mezza umana, con occhi d'argento e una schivata non umana, la claymore "
        "è una classe quasi solo femminile: i maschi hanno... problemi. L'arma "
        "prediletta è la claymore, da cui il nome, e preferisce armature "
        "leggere, contando sulla gran velocità e sull'arte di schivare. "
        "Guarisce in fretta, ma la guarigione ha un prezzo: il corpo è "
        "instabile. *[Spada turbinante] Raro colpo che trapassa tutto."
    ),
}


def main():
    voci = [json.loads(l) for l in io.open(ESTRAZIONE, encoding="utf-8") if l.strip()]
    per_riga = {v["riga"]: v for v in voci}
    RESE = {**NOMI, **DESCRIZIONI}

    guai = []
    for riga, resa in RESE.items():
        if riga not in per_riga:
            guai.append(f"la riga {riga} non sta nell'estrazione")
            continue
        if riga in NOMI:
            if len(degrada(resa)) > TETTO_NOME:
                guai.append(f"«{resa}» è {len(degrada(resa))}, il tetto è {TETTO_NOME}")
        else:
            righe = len(D.talk_conv(degrada(resa)))
            if righe > D.TETTO:
                en = len(D.talk_conv(per_riga[riga]["en"]))
                guai.append(f"riga {riga}: {righe} righe, il tetto è {D.TETTO} (l'inglese ne fa {en})")
    INVARIATE = {633}  # Claymore, vedi invariati.md
    for v in voci:
        if v["riga"] not in RESE and v["riga"] not in INVARIATE:
            guai.append(f"la riga {v['riga']} ({v['en'][:40]}) non ha una resa")
    if guai:
        for g in guai:
            print("  ⚠️", g)
        raise SystemExit("il tavolo non è a posto: non scrivo niente")

    fuori = []
    for riga, resa in sorted(RESE.items()):
        d = dict(per_riga[riga])
        d["it"] = resa
        fuori.append(d)
    testo = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in fuori)
    io.open(USCITA, "w", encoding="utf-8", newline="").write(testo)

    print(f"{len(fuori)} voci in {USCITA}")
    for riga in sorted(DESCRIZIONI):
        print(
            f"   riga {riga}: it {len(D.talk_conv(degrada(DESCRIZIONI[riga])))} righe"
            f"  (en {len(D.talk_conv(per_riga[riga]['en']))})"
        )


if __name__ == "__main__":
    main()
