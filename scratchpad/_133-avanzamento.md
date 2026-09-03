
---

## 2026-09-03, centotrentatreesima — il fronte di `scene2.hsp` passa la metà

**797 rese in una sessione**: lotto B chiuso e lotto C fino alla scena 131.

    scene2.hsp   1.701 blocchi con testo, 167.003 caratteri
                 tradotti:  **892 blocchi** (52,4%)
                 restano:   809 blocchi

| lotto | scene | voci | caratteri | stato |
|---|---|---:|---:|---|
| A — prologo e Vernis | 0-5 | 95 | 13.407 | ✅ tradotto (132ª) |
| B — la storia principale | 7-30 | 239 | 33.190 | ✅ tradotto (133ª) |
| C — il seguito | 101-135 | 632 | 56.397 | ⏳ **558 su 632** — restano le scene 132, 133, 134, 135 (74 voci) |
| D — il finale | 300-400 | 599 | 64.442 | ⬜ mai aperto |

ⓘ I numeri per lotto sono **voci**, non blocchi: comprendono le etichette
`{actor_N}`, che il piano contava a parte. Il lotto C ne ha 155 su 632, ed è la
ragione per cui 632 voci fanno 477 blocchi di prosa.

⚠️ **Il perimetro sale con le scene, e questo è nuovo.** `perimetro.py` passa da
26.422 a **27.219** (+797): il contatore conta le voci di dizionario, quindi da
quando `scene2.hsp.jsonl` esiste il fronte delle scene ci entra. ⚠️ Il «100,0%»
continua a non voler dire «finito»: dice che ogni voce **chiesta** è resa, e le
809 non ancora estratte non sono chieste da nessuno.

⭐ **E stavolta le rese sono in gioco.** `cgx-test.exe` ricompilato e installato
alle **11:04 del 03/09** con tutti e 892 i blocchi iniettati. Il che vuol dire
che oggi, con una partita nuova, il prologo e tutta la storia principale si
vedono in italiano — cosa che alla fine della 132ª non era vera.

⚠️⚠️ **Ma nessuna delle 797 è stata vista a schermo.** Il debito di collaudo sale
da ~9.745 a **~10.542**. ⓘ Dei cinque stati distinti — costruito, misurato dagli
strumenti, provato al contrario, compilato, visto a schermo — qui ci sono i
primi quattro. Il quinto no.

⭐ **Due difetti trovati non traducendo, ma controllando come si scriveva prima.**
Le due rese del lotto A che scrivevano «Ylva» invece di «Irva» non le ha trovate
nessuna misura: le ho trovate perché stavo per copiarle. Da lì 13 rese corrette
in cinque dizionari e due cancelli nuovi (le grafie inglesi, e il carattere che
CP932 non sa scrivere). Vedi `decisioni.md`, 133ª.
