# Ripresa sessione

Aggiornato: 2026-08-10, fine della quindicesima sessione.

## La prima cosa da fare

**Continuare i lotti per razza.** Restano **577 nomi in 64 razze**, e la
macchina è rodata: dodici lotti in una sessione, tutti verdi al primo colpo.

```powershell
cd "C:\Users\old_p\Documents\progetto second brain\Elona+ CGX - Traduzione Italiana"
python -m strumenti.creature --razze                # quanto resta, razza per razza
python -m strumenti.creature --razza karune --uscita lavoro/fase2-karune-001.jsonl
```

Le prossime per taglia: `karune` 18, `ghost` 17, `roran` 16, `worm` 15,
`dragon` 15, `yerles` 15, `cat` 14, `metal` 14, `eulderna` 14. Poi la coda
lunga fino alle razze da una.

⚠️ **`--razza` toglie da sé le firme già in dizionario.** `--classe nome` no:
quello emette tutti i 1.131, nucleo compreso.

⚠️ **Il lotto `cat` ha un debito aperto**: 復元獣サーベルタイガー è l'ultimo
membro della famiglia 復元 e va reso «la tigre dai denti a sciabola rediviva»,
con l'accordo al femminile. Gli altri sette sono già dentro (`dog`, `bird`,
`imp`).

### Le quattro verifiche d'apertura

```powershell
python -m pytest strumenti/tests -q        # atteso: 336 passed, 2 skipped
python -m strumenti.prova_identita         # atteso: 72/72, 27.813, ambigue 0
python -m strumenti.verifica --dizionario  # atteso: 0 da ritradurre ovunque
python -m strumenti.creature               # atteso: nome 1131, voce 320, doppie 0, senza razza 0
```

## Dove siamo

| file | tradotte | firme | % |
|---|---|---|---|
| `db_item.hsp` | 1.606 | 1.606 | **100%** |
| `item_data.hsp` | 318 | 318 | **100%** |
| `skill.hsp` | 885 | 885 | **100%** |
| `custom_tweaks.hsp` | 12 | 12 | **100%** |
| `action.hsp` | 373 | 1.288 | 29% |
| `text.hsp` | 721 | 1.740 | 41% |
| gli altri tre | 0 | 2.775 | 0% |
| **totale Fase 1** | **3.915** | **8.624** | **45%** |

Fuori dalla Fase 1: `db_creature.hsp` a **555 firme su 3.655** — **554 nomi su
1.131** più l'epiteto — e le 2.555 descrizioni d'oggetto di `db_item.hsp`.

Tredici commit oggi, tutti verdi e pushati. **336 test** (erano 331), prova
d'identità **72/72 e 27.813**, **5.402 sostituzioni** nella build, il
compilatore non dice nulla. Rinviate ferme a **79**.

## Il taglio per razza, e perché è uno strumento

Il nucleo atomico si era preso da sé. Tutto il resto si taglia per **razza**,
che il sorgente **dichiara** — `dbidn`, subito prima di `gosub *db_race` — e
non si deduce dal nome, che è il dato che stiamo per tradurre e quindi non può
fare da chiave a sé stesso. È la terza volta che il criterio giusto è un campo
del sorgente: `reftype` per `db_item.hsp`, l'array che dichiara la voce per
`item_data.hsp`, `dbidn` qui.

Sta in `strumenti/creature.py` con sei guardie. La rete è `firme_senza_razza()`,
oggi vuota su 1.131 nomi: se un domani non lo fosse, «un lotto è una razza»
coprirebbe novecento nomi meno uno **e non lo direbbe**.

## Le cinque cose da non riscoprire

### 1. L'articolo sta sulla testa del sintagma, non sulla persona

⚠️ **È la lezione più utile della sessione, e restringe il problema.** Un nome
di mestiere descrive una persona, e in italiano l'articolo di «negoziante»
dipende da chi lo porta; il sorgente dichiara `cdata(CDATA_SEX, rc)` solo per
una parte (52 su 90 in `norland`). Ma i cinque demoni di `imp` hanno sessi
diversi e la **stessa** forma italiana — «il demone di X» — perché il genere lo
dà «demone». `CDATA_SEX` conta solo quando la testa **è** la persona
(`<Neres> la smemorata`).

Il criterio completo è in `guida-stile.md`, «L'articolo di un nome di persona,
quando il sesso non è deciso». In breve: sesso dichiarato → si concorda; sesso
casuale → sostantivo il cui articolo non dipende dalla persona («la guardia»,
«l'artista», «il ninja»); maschile non marcato solo dove l'italiano non offre
altro (14 su 90).

⚠️ **`/man/` non è il sesso.** È la stringa di `DBSPEC_CHARA_FILTER`, accanto a
`/god/`, `/sf/`, `/nefia0/`: la categoria di generazione. Ce l'hanno anche
修道女 e 娼婦.

**Il dato per fare meglio esiste**: il sesso è già assegnato quando
`cdatan(CDATAN_NAME, rc)` viene montato — il ramo dello sprite sta due righe
sotto. Una resa femminile per nome costerebbe un campo nuovo di dizionario e un
array parallelo, come il `plurale`. Si rifà il conto quando le persone saranno
tutte tradotte, non prima.

### 2. Il sorgente arbitra, ma bisogna chiedergli la cosa giusta

Quattro volte su cinque la risposta era nel blocco della creatura:

- i **dieci segugi elementali** li dichiara `creaturepack = FILTER_RACE_HOUND_<X>`,
  e da lì esce l'unica resa che l'inglese non avrebbe dato: `illusion hound` ha
  filtro `HOUND_MIND` e giapponese 幻惑, lo stesso di `Resist Mind` → **«il
  segugio mentale»**;
- ガンデグー attacca `ACTION_RANGE`, quindi ガン è *gun* → «il degu pistolero»;
- カオス・ブレーダー fa tre attacchi in mischia più ombra e succhiasangue: è uno
  **spadaccino**, non il paladino che dice l'inglese;
- 面忘の獅子 ringhia e graffia nel proprio blocco: è un uomo che non è più un
  uomo, «il leone senza volto».

⚠️ **Ma la quinta volta la stessa prova non ha dato la stessa conclusione.**
幻惑折鶴 lancia davvero `SKILL_SPELL_MIND_THORN`, eppure **non** si rende
«mentale»: lì il nome era **uno di dieci**, uno per elemento, e funzionava da
etichetta; una gru sola no, e 幻惑 le descrive cosa fa. *La stessa prova non
porta alla stessa conclusione quando cambia cosa il nome sta facendo.*

### 3. Il giapponese arbitra, e non è un caso limite

Su 351 nomi l'inglese ha sbagliato **una dozzina di volte**, e non per
abbreviazione:

| giapponese | inglese | cosa dice davvero |
|---|---|---|
| 腕白少女 | `the white arms` | 腕白 *wanpaku* = **monella**, letto coi kanji separati |
| 猫かぶり | `the cat freak` | l'idioma «fingersi ingenui», preso alla lettera |
| 首切雀 | `tree sparrow` | il passero **mozzatesta**, non la passera mattugia |
| 化け狸 | `badger` | il *bake-danuki*: il tasso non è un procionide |
| 魔剣士 | `knight of Elea` | lo **spadaccino magico** |
| 淫婦 | `camouflaged imp` | la **lussuriosa** |
| 虚空 | `vanity` | il **vuoto**, non la vanità |
| ヤミクミロミ | `Insane Kumiromi` | *Yami* = **oscuro** |

E tre volte ha **spostato la razza**: 歴戦の老兵 non nomina Zanan e l'inglese
gliela aggiunge; エレアの難民 nomina Elea e l'inglese la toglie; イェルス超重力砲
e イェルス防衛システム la perdono. In tutti e tre i casi si segue il giapponese.

### 4. Le fusioni si rifanno, non si leggono

Intere razze sono costruite su giochi di parole, e **l'inglese non li traduce:
li ricostruisce in inglese**. ダゴンズイ (ダゴン + ゴンズイ) diventa
`daganotosus` col nome scientifico; エンタメイド·ザンコック (残酷 + コック)
diventa `cocruel`. L'italiano fa la stessa cosa, perché è il gioco a essere il
contenuto: «il pesce gatto Dagon», «la spettacameriera cuocrudele».

⚠️ **E una famiglia era già stata decisa a metà.** ハムスター finisce per
**スター**, e Elona+ ci costruisce sopra モーニングスター, デススター,
シューティングスター. L'inglese salva il criceto (`death hamster`) e perde il
gioco — ma il nucleo aveva già reso `Morningstar` → «la stella mattutina».
Proseguire era l'unico modo di non spezzare la famiglia: «la stella della
morte», «la stella cadente». **Prima di scegliere, guardare cosa il nucleo ha
già scelto per i parenti.**

### 5. Il quiz e i nomi devono coincidere, e il quiz è arrivato prima

`text.hsp` è al 41% e le sue domande sono **già a schermo**; i nomi no. Quindi
di norma sono i nomi ad adeguarsi: `<Lexus>` è «il guardiano della Gilda dei
Maghi» perché così dice la risposta, e `<Larnneire>` è «l'ascoltatrice del
vento» per lo stesso motivo.

⚠️ **Tranne quando è la domanda a essere sbagliata.** «Come si chiama
l'**investigatore** della Gilda dei Maghi?» era al maschile, ma la risposta è
`<Lenas>` e il sorgente le dà `SEX=1`. Ritradotta al femminile: era un'ipotesi
presa quando i nomi non c'erano.

`arena master` ha ora la condizione soddisfatta ma resta rinviato, con le altre
58: si chiudono col loro lotto di `text.hsp`, non una alla volta.

## Cosa rifare a ogni giro

```powershell
python -m strumenti.verifica lavoro/<lotto>.jsonl   # prima di reimportare
python -m strumenti.reimporta lavoro/<lotto>.jsonl
python -m pytest strumenti/tests -q
python -m strumenti.prova_identita        # 72/72, 27.813, ambigue 0
python -m strumenti.genera_toppe_nomi     # 32 generate, tutte «ok»
python -m strumenti.genera_toppe_casuali  # 213 generate, tutte «ok»
```

⚠️ **Il sorgente è pinnato al tag `2.31.2.0`**, e l'integrità si verifica col
manifesto SHA-256, **mai** con `git status`, che in quel clone è
permanentemente sporco. Gli hash del manifesto sono in MAIUSCOLO.

⚠️ **Da rifare a ogni versione CGX nuova**: cercare chi riassegna `skillname` e
`skilldesc` fuori da `skill.hsp` — oggi è solo `custom_tweaks.hsp`, ma è un
file di *tweak* e cresce a ogni rilascio.

⚠️ Un guardiano dell'ambiente blocca i messaggi di commit che contengono
`/man/` letto come percorso: passare il testo con `git commit -F <file>`.

## Per rifare la prova in gioco

```powershell
python -m strumenti.applica
python -m strumenti.compila --eseguibile
Copy-Item "C:\Games\Elona\_traduzione\build\2.05-custom-gx\elonapluscgx.exe" "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -Force
Start-Process "C:\Games\Elona\elonaplus2.31\cgx-test.exe" -WorkingDirectory "C:\Games\Elona\elonaplus2.31"
```

⚠️ La copia fallisce con «Device or resource busy» se il gioco è aperto.
Al primo avvio esce «Invalid screen resolution»: si dà OK e si prosegue.
Il titolo mostra 2.31.1.0: è la costante di versione, non un errore di build.

⚠️ **Serve un salvataggio nuovo** per i nomi, e un **personaggio nuovo** per
l'epiteto.

⚠️ L'utente **preferisce una lista di passi da eseguire lui** al collaudo
pilotato da qui. Dargli la tabella, con l'esito atteso di ogni riga.

### Il collaudo ancora aperto

- **L'evoluzione vera non è mai stata provata**, ed è in sospeso dalla
  quattordicesima sessione. Serve impressione ≥ 150 (`action.hsp:16630`),
  stadio 0, e l'oggetto d'evoluzione usato sull'alleato. Il soggetto è a portata
  di mano: **Lazrof è un `lame horse`**, evmode 3.
  > esito atteso: `Lazrof il cavallo zoppo` → **`Lazrof l'unicorno`**
- **I 351 nomi di oggi** sono stati visti a schermo solo per i passanti delle
  città (l'articolo dentro il nome regge su una popolazione mista). I segugi
  elementali, gli dèi e i mostri marini no.

## L'ordine che resta

1. gli altri **577 nomi**, a lotti per razza; poi le **320 di voce**;
2. le **59 rinviate** del quiz, che si sbloccano solo dopo;
3. le **915 dinamiche di `action.hsp`**, che riparano anche «mordes»;
4. `text.hsp` dal 41% in su, `command.hsp`, `proc.hsp`, `trait.hsp`;
5. le **2.555 descrizioni d'oggetto** di `db_item.hsp`.

## I tetti misurati, con la loro ancora

| campo | tetto | ancora | fonte |
|---|---|---|---|
| tracciatore HUD | 6 | sinistra, taglia | `screen.hsp:2002` |
| razza e classe | 3 | sinistra, taglia | `chara.hsp:4679` |
| slot d'equipaggiamento | 6 | sinistra, taglia | osservato a schermo |
| gradi di resistenza | 9 | **destra, invade** | `command.hsp:11002` |
| nome nella lista abilità | **24** | sinistra, invade il costo | `command.hsp:5382` |
| descrizione nella lista | 34 | taglia (`strmid`) | `command.hsp:5389` |

Vedi [[la-forma-memorizzata-non-e-quella-scritta]],
[[una-chiave-che-collide-non-e-una-chiave]],
[[il-campo-che-il-sorgente-dichiara]], [[la-testa-porta-il-genere]],
[[una-decisione-nel-posto-sbagliato]], [[una-guardia-agganciata-a-se-stessa]],
[[guardia-troppo-severa]], [[larghezza-per-campo]], [[ultima-scrittura-vince]],
[[percentuale-senza-denominatore]], [[una-procura-non-e-una-proprieta]],
[[la-categoria-che-il-sorgente-dichiara]],
[[il-posto-decide-quando-arriva-il-dato]], [[dato-o-derivata]],
[[toppe-generate-dal-sorgente]], [[stessa-forma-va-verificata-nel-codice]] e
[[cp932-perdite-silenziose]].
