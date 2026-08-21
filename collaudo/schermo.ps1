# collaudo/schermo.ps1 — pilotare il gioco per il collaudo in gioco.
#
# Serve quando il collaudo va fatto e non c'e' nessuno a giocare. Scritto il
# 2026-08-08, nona sessione.
#
#   .\schermo.ps1 -Uscita c1.png                    # solo cattura
#   .\schermo.ps1 -Tasti "ENTER" -Uscita c2.png     # carica il salvataggio
#   .\schermo.ps1 -Tasti "LEFT,LEFT,i" -Uscita c3.png
#
# Cose imparate, che non sono ovvie:
#
# - la finestra si cattura con `CopyFromScreen`: Elona+ CGX non usa una
#   superficie DirectX esclusiva, quindi la cattura funziona e basta;
# - i tasti si mandano con `keybd_event`, che imposta lo stato vero della
#   tastiera -- il gioco lo legge e risponde;
# - ⚠️ **le associazioni vere stanno in
#   `sorgente/dist/2.05-custom-gx/original/config.txt`**, non nella
#   documentazione. `key_interact` e' `i`, non Invio; il movimento e' 4/6/8/2
#   ma anche le frecce funzionano. Leggerle li' evita di tirare a indovinare;
# - il personaggio si trova col **puntino blu della minimappa** in basso a
#   sinistra. Il confronto fra due fotogrammi NON funziona: la pioggia animata
#   cambia mezzo schermo a ogni turno;
# - pilotare il gioco e' **lento**. Attraversare una citta' costa molti giri:
#   conviene solo se non c'e' alternativa.
#
# ⚠️ Prima di pilotare una partita vera, copiare i salvataggi:
#     Copy-Item "C:\Games\Elona\elonaplus2.31\save\*" "C:\Games\Elona\save-backup\<data>" -Recurse
#
# ⚠️⚠️⚠️ **QUESTO SCRIPT SCRIVE SULLA TASTIERA DI TUTTO IL COMPUTER, NON SUL
# GIOCO** (misurato il 2026-08-22, 83a). `keybd_event` imposta lo stato **globale**
# della tastiera: i tasti vanno a chi ha il fuoco in quel momento, e chi ha il
# fuoco puo' cambiare **a meta' di una parola**. Battendo `wizard` nella console
# del gioco, sei lettere su sei sono finite nel prompt di **un'altra sessione di
# Claude Code** aperta sulla stessa scrivania, che ci si e' ritrovata scritto
# «fallwliziard». Non e' un caso limite: `SetForegroundWindow` chiamato da un
# processo che non ha il fuoco Windows lo **ignora**, e il pilota non se ne
# accorge — l'unico segnale e' il gioco che risponde «Unknown command».
#
# 💡 Regola: **non pilotare il gioco mentre qualcun altro sta usando il
# computer.** Se il collaudo va fatto lo stesso, prima si controlla che la
# finestra in primo piano sia davvero quella del gioco, e si accetta che una
# sessione interattiva accanto possa rubarlo di nuovo in qualunque momento.
param(
  [string]$Tasti = "",
  [string]$Testo = "",
  [string]$Uscita = "",
  [int]$Pausa = 220,
  [int]$AttesaFinale = 700,
  [string]$Titolo = "Elona"
)
# ⚠️ `-Titolo Elona` NON basta piu': i terminali aperti sul progetto si chiamano
# «Elona traduzione…» e `-match` prende il primo che passa, che e' una finestra
# di testo. Per il gioco si usa `-Titolo "Custom-GX"`.
#
# `-Testo` batte una stringa qualunque, `-Tasti` i tasti con un nome. Servono
# tutt'e due perche' la CONSOLE del gioco (F12) vuole comandi come
# `spawn_item 1314`: l'underscore su una tastiera italiana e' SHIFT + `-`, e
# un pilota che manda solo codici virtuali nudi scrive `spawn-item` e non se ne
# accorge. `VkKeyScanW` restituisce insieme il codice E lo stato dei
# modificatori per la disposizione corrente, quindi la domanda «che tasti fanno
# questo carattere?» si gira al sistema invece di indovinarla.
Add-Type -AssemblyName System.Drawing
if (-not ("Win" -as [type])) {
Add-Type @"
using System;
using System.Runtime.InteropServices;
public class Win {
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern void keybd_event(byte vk, byte scan, uint flags, IntPtr extra);
  [DllImport("user32.dll")] public static extern uint MapVirtualKey(uint code, uint type);
  [DllImport("user32.dll")] public static extern short VkKeyScanW(char c);
  [StructLayout(LayoutKind.Sequential)] public struct RECT { public int L, T, R, B; }
}
"@
}
$p = Get-Process | Where-Object { $_.MainWindowTitle -match $Titolo } | Select-Object -First 1
if (-not $p) { Write-Output "IL GIOCO NON E' IN ESECUZIONE"; exit 1 }
$h = $p.MainWindowHandle
[void][Win]::SetForegroundWindow($h)
Start-Sleep -Milliseconds 350

# i nomi sono quelli di config.txt dove esistono; il resto e' il codice virtuale
$VK = @{
  "ENTER"=0x0D; "ESC"=0x1B; "SPACE"=0x20; "SHIFT"=0x10; "TAB"=0x09; "BACK"=0x08;
  "UP"=0x26; "DOWN"=0x28; "LEFT"=0x25; "RIGHT"=0x27;
  "NUM1"=0x61; "NUM2"=0x62; "NUM3"=0x63; "NUM4"=0x64; "NUM5"=0x65;
  "NUM6"=0x66; "NUM7"=0x67; "NUM8"=0x68; "NUM9"=0x69;
  "*"=0x6A; "+"=0x6B; "-"=0x6D;
  # F12 apre la CONSOLE (help.hsp:452), che e' la via piu' corta per un
  # collaudo: `wizard` piu' `spawn_item <ID>` mette a terra qualunque oggetto
  # del gioco senza doverlo cercare. Senza queste righe «F12» finiva nel ramo
  # del carattere singolo e non partiva nessun tasto.
  "F1"=0x70; "F2"=0x71; "F3"=0x72; "F4"=0x73; "F5"=0x74; "F6"=0x75;
  "F7"=0x76; "F8"=0x77; "F9"=0x78; "F10"=0x79; "F11"=0x7A; "F12"=0x7B;
  "PERIOD"=0xBE; "COMMA"=0xBC
}
function Premi([int]$codice, [bool]$conShift) {
  $scan = [Win]::MapVirtualKey([uint32]$codice, 0)
  if ($conShift) { [Win]::keybd_event(0x10, [byte][Win]::MapVirtualKey(0x10, 0), 0, [IntPtr]::Zero); Start-Sleep -Milliseconds 30 }
  [Win]::keybd_event([byte]$codice, [byte]$scan, 0, [IntPtr]::Zero)
  Start-Sleep -Milliseconds 40
  [Win]::keybd_event([byte]$codice, [byte]$scan, 2, [IntPtr]::Zero)
  if ($conShift) { Start-Sleep -Milliseconds 30; [Win]::keybd_event(0x10, [byte][Win]::MapVirtualKey(0x10, 0), 2, [IntPtr]::Zero) }
}

foreach ($c in $Testo.ToCharArray()) {
  $r = [Win]::VkKeyScanW($c)
  if ($r -eq -1) { Write-Output "carattere non battibile con questa tastiera: $c"; continue }
  Premi ($r -band 0xFF) ((($r -shr 8) -band 1) -eq 1)
  Start-Sleep -Milliseconds 45
}
if ($Testo -ne "") { Start-Sleep -Milliseconds $Pausa }

foreach ($t in ($Tasti -split "," | Where-Object { $_ -ne "" })) {
  $t = $t.Trim()
  if ($VK.ContainsKey($t.ToUpper())) { $codice = $VK[$t.ToUpper()] }
  elseif ($t.Length -eq 1) { $codice = [byte][char]($t.ToUpper()) }
  else { Write-Output "tasto sconosciuto: $t"; continue }
  $scan = [Win]::MapVirtualKey([uint32]$codice, 0)
  [Win]::keybd_event([byte]$codice, [byte]$scan, 0, [IntPtr]::Zero)
  Start-Sleep -Milliseconds 60
  [Win]::keybd_event([byte]$codice, [byte]$scan, 2, [IntPtr]::Zero)
  Start-Sleep -Milliseconds $Pausa
}
Start-Sleep -Milliseconds $AttesaFinale

if ($Uscita -ne "") {
  $r = New-Object Win+RECT
  [void][Win]::GetWindowRect($h, [ref]$r)
  $w = $r.R - $r.L; $ht = $r.B - $r.T
  $bmp = New-Object System.Drawing.Bitmap($w, $ht)
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.CopyFromScreen($r.L, $r.T, 0, 0, (New-Object System.Drawing.Size($w, $ht)))
  $bmp.Save($Uscita, [System.Drawing.Imaging.ImageFormat]::Png)
  $g.Dispose(); $bmp.Dispose()
  Write-Output "salvato: $Uscita"
}
