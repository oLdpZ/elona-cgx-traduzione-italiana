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
param(
  [string]$Tasti = "",
  [string]$Uscita = "",
  [int]$Pausa = 220,
  [int]$AttesaFinale = 700,
  [string]$Titolo = "Elona"
)
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
  "*"=0x6A; "+"=0x6B; "-"=0x6D
}
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
