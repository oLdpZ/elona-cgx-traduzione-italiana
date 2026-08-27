# -*- coding: utf-8 -*-
"""Le rese del lotto 014 (gli SCUDI, `FILTER_SHIELD`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 014 scratchpad/lotti-111

**23 righe del sorgente, 23 firme**, 23 giapponesi distinti. Prima categoria
dell'equipaggiamento, e la piu' facile che resti: righe corte, e tre famiglie
che si scrivono in fila invece che una per volta.

⭐ **La categoria non e' fatta solo di scudi**: nello slot dello scudo ci
stanno anche i quattro **artigli** e i cinque **tonfa**, e si vede dal nome
dell'oggetto, non dalla descrizione.

### Le tre famiglie

**Gli artigli (4)**, che il giapponese grada con due parole diverse per
«robusto» e tre gradi di «affilato». Rese distinte perche' il sorgente le
distingue:

    とても丈夫で鋭い爪  -> molto resistenti e affilati   (:42855 Turahagi)
    軽くて鋭い爪        -> leggeri e affilati            (:67602 Otogiri)
    それなりに頑丈な爪  -> abbastanza robusti            (:68253 artiglio)
    恐ろしく鋭い爪      -> affilati da far paura         (:69259 Gur Bagh Nakh)

⚠️ 丈夫 e 頑丈 sono **due parole**, e diventano «resistenti» e «robusti»: la
110a ha gia' deciso cosi' per 非常に重い / とても重い (le due mitragliatrici).

**I tonfa (5)**, dove 内蔵した torna **due volte** e va reso due volte uguale,
se no la coppia non si legge come coppia:

    推進装置を内蔵した  -> con un propulsore incorporato            (:71236)
    防御装置を内蔵した  -> con un dispositivo di difesa incorporato (:71442)

**Gli scudi comuni (7)**, che il giapponese dice in due o tre parole e che
prendono il vocabolario dai **nomi degli oggetti**, gia' resi: 小盾 «scudo
piccolo», 丸型盾 «scudo rotondo», 長盾 «scudo a mandorla», 重層盾 «scudo a
torre», 騎士盾 «scudo da cavaliere», 鉤爪 «artiglio».

### ⭐ Quattro parole erano gia' a schermo, e nessuna e' stata inventata

- 出血 e' **«Sanguinamento»**: e' l'etichetta di stato che il giocatore legge
  in `command.hsp:1888`. Lo scudo di spine lo **provoca**.
- 光子 e' **«laser»**: il lotto 013 (110a) ha reso 光子銃 «pistola laser», e
  `db_item.hsp` ha gia' «bazooka laser». Quindi 光子刃 sono **lame laser**.
- 黒曜石 e' **«ossidiana»**: `glossario.md` ha gia' 黒曜鏡 «Specchio
  d'ossidiana».
- 推進装置 e' **«propulsore»**: gia' cosi' in `db_card.hsp` (110a) e in
  `chat.hsp`.
- 軽装備 e' **«armatura leggera»** nelle righe di potenziamento; 連続攻撃 e'
  **«raffica di colpi»** nel messaggio dell'attacco (`chara_func`).

### ⚠️⚠️ `:71512` — L'INGLESE DEL SORGENTE E' TRONCATO A META' PAROLA

    description(0) = "... It allows it's user to sac\n# ~Irva Fantasy ..."
    description(3) = "It is a tonfa that suc"

Non e' l'estrattore: sono **due** stringhe tagliate a meta' parola dentro
`db_item.hsp:71509` e `:71512`, un difetto di monte. Il giapponese li' dice
soltanto 「トンファーだ。」 — cioe' **non dice niente** dell'oggetto, com'e'
suo diritto per un artefatto non ancora identificato. Si segue il giapponese:
«Un tonfa.». ⚠️ Chi un giorno guarda quella riga e la trova povera, guardi
l'inglese prima di allungarla: qui l'inglese non e' una fonte, e' un troncone.

### ⚠️ Dove l'inglese aggiunge e il giapponese tace

- `:68253` (l'artiglio comune): l'inglese spiega «sturdy enough to be used like
  a shield», cioe' racconta il **fatto di gioco** — gli artigli si equipaggiano
  nello slot dello scudo. Il giapponese dice solo それなりに頑丈な爪だ. Il
  fatto e' vero (la categoria e' `FILTER_SHIELD`) ma il giapponese ha scelto di
  tacerlo, e la riga sta gia' dentro la scheda dello scudo: non si aggiunge.
- `:57965` (God Binder): l'inglese ci mette «godly gift», che nel giapponese
  non c'e' — e sta gia' nel **nome** dell'oggetto, «Vincolo degli Dei».
- `:82481` (Al'ud): qui e' il contrario, l'inglese **perde** 鉄壁を誇る, il
  vanto del muro di ferro. Si tiene: «difende come un muro».
"""

IT = {
    # === i quattro artigli — due parole per «robusto», tre gradi di «affilato»
    42855: "Degli artigli molto resistenti e affilati.",
    67602: "Degli artigli leggeri e affilati.",
    68253: "Degli artigli abbastanza robusti.",
    69259: "Degli artigli affilati da far paura.",

    # === i cinque tonfa — 内蔵した due volte, resa uguale due volte
    71236: "Un tonfa con un propulsore incorporato.",
    71442: "Un tonfa con un dispositivo di difesa incorporato.",
    71305: "Un tonfa da cui escono lame laser.",
    71374: "Un tonfa che attacca a raffica.",
    71512: "Un tonfa.",

    # === i sette scudi comuni — il nome dell'oggetto porta gia' il vocabolario
    100720: "Uno scudo pesantissimo.",
    100786: "Uno scudo lungo.",
    100852: "Uno scudo duro.",
    100918: "Un'armatura che si equipaggia in mano.",
    100984: "Uno scudo rotondo.",
    101050: "Uno scudo per chi porta armatura leggera.",
    127207: "Uno scudo per i cavalieri.",

    # === gli scudi artefatto
    59595: "Uno scudo piccolo e quadrato.",
    59863: "Uno scudo a specchio, fatto di ossidiana levigata.",
    73563: "Uno scudo con la difesa alta.",
    82413: "Uno scudo che provoca sanguinamento.",
    82481: "Uno scudo a forma di strumento musicale, difende come un muro.",
    81331: "Un'asse di legno che stava su una nave.",
    # ⚠️ ERA «in ceppi», cambiato nel lotto 024: 足枷 (gli stivali, :76118) e'
    #    l'altra meta' della coppia e il suo oggetto si chiama gia' «Ceppo
    #    della Terra». 手枷 sono le MANI: manette.
    57965: "Se lo indossi, si trasforma in manette.",
}
