# -*- coding: utf-8 -*-
"""111a - Lotto 014 di `db_item.hsp`: il rapporto degli SCUDI.

`FILTER_SHIELD`, `description(3)`: **23 righe del sorgente, 23 firme**, 23
giapponesi distinti. Prima categoria dell'equipaggiamento, e la piu' facile che
resti: righe corte, e tre famiglie che si scrivono in fila.

### ⭐ NELLO SLOT DELLO SCUDO NON CI STANNO SOLO GLI SCUDI

Quattro **artigli** e cinque **tonfa** stanno in `FILTER_SHIELD`, e lo si vede
dal **nome** dell'oggetto, non dalla descrizione. Le tre famiglie si scrivono
insieme, se no le righe della stessa famiglia non si confrontano.

**Gli artigli (4)** — due parole giapponesi per «robusto», tre gradi di
«affilato», e quattro rese distinte perche' il sorgente distingue:

    とても丈夫で鋭い爪  -> molto resistenti e affilati   (:42855 Turahagi)
    軽くて鋭い爪        -> leggeri e affilati            (:67602 Otogiri)
    それなりに頑丈な爪  -> abbastanza robusti            (:68253 artiglio)
    恐ろしく鋭い爪      -> affilati da far paura         (:69259 Gur Bagh Nakh)

⚠️ 丈夫 e 頑丈 sono **due parole** e diventano «resistenti» e «robusti»: e' la
stessa mossa della 110a su 非常に重い / とても重い, le due mitragliatrici.

**I tonfa (5)** — 内蔵した torna **due volte** e va reso due volte uguale:

    推進装置を内蔵した  -> con un propulsore incorporato            (:71236)
    防御装置を内蔵した  -> con un dispositivo di difesa incorporato (:71442)

**Gli scudi comuni (7)** — il giapponese dice due o tre parole, e il
vocabolario sta nei **nomi degli oggetti**, gia' resi: 小盾 «scudo piccolo»,
丸型盾 «scudo rotondo», 長盾 «scudo a mandorla», 重層盾 «scudo a torre»,
騎士盾 «scudo da cavaliere», 鉤爪 «artiglio».

### ⭐ CINQUE PAROLE ERANO GIA' A SCHERMO, E NESSUNA E' STATA INVENTATA

- 出血 e' **«Sanguinamento»**, l'etichetta di stato di `command.hsp:1888`. Lo
  scudo di spine lo **provoca**.
- 光子 e' **«laser»**: il lotto 013 ha reso 光子銃 «pistola laser», e il file
  ha gia' «bazooka laser». Quindi 光子刃 sono **lame laser**.
- 黒曜石 e' **«ossidiana»**: `glossario.md` ha 黒曜鏡 «Specchio d'ossidiana».
- 推進装置 e' **«propulsore»**, gia' cosi' in `db_card.hsp` e in `chat.hsp`.
- 軽装備 e' **«armatura leggera»** nelle righe di potenziamento, e 連続攻撃 e'
  la **«raffica di colpi»** del messaggio d'attacco in `chara_func.hsp`.

### ⚠️⚠️ `:71512` — L'INGLESE DEL SORGENTE E' TRONCATO A META' PAROLA

    description(0) = "... It allows it's user to sac\n# ~Irva Fantasy ..."
    description(3) = "It is a tonfa that suc"

Non e' l'estrattore: sono **due** stringhe tagliate a meta' parola dentro
`db_item.hsp:71509` e `:71512`, un difetto di monte. Il giapponese dice solo
「トンファーだ。」 — cioe' **non dice niente**, com'e' suo diritto per un
artefatto non identificato. Si segue il giapponese: «Un tonfa.».
⚠️ Chi trova quella riga povera guardi l'inglese **prima** di allungarla: li'
l'inglese non e' una fonte, e' un troncone.

### ⚠️ DOVE L'INGLESE AGGIUNGE E IL GIAPPONESE TACE

- `:68253`, l'artiglio comune: l'inglese spiega «sturdy enough to be used like a
  shield», cioe' racconta il **fatto di gioco** — gli artigli si equipaggiano
  nello slot dello scudo. Vero (la categoria e' `FILTER_SHIELD`), ma il
  giapponese ha scelto di tacerlo e la riga sta gia' dentro quella scheda.
- `:57965`, God Binder: l'inglese ci mette «godly gift», che nel giapponese non
  c'e' e che sta gia' nel **nome**, «Vincolo degli Dei».
- `:82481`, Al'ud: qui e' il contrario — l'inglese **perde** 鉄壁を誇る, il
  vanto del muro di ferro. Si tiene: «difende come un muro».
"""
