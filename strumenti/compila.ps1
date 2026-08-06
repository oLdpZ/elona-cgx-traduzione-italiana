# strumenti/compila.ps1
# Pilota hspcmp.dll senza la GUI dell'editor HSP. Non va lanciato a mano:
# lo invoca strumenti/compila.py, che sa trovare il PowerShell a 32 bit.
#
# La DLL e' a 32 bit, quindi serve un host a 32 bit. Windows ne ha gia' uno
# installato: SysWOW64\WindowsPowerShell.
#
# ABI (verificata sul disassemblato degli export, non dedotta da hspcmp.as):
# ogni export e' decorato @16, quindi quattro slot sempre presenti.
#   - chi prende una stringa la legge da [esp+8]  -> slot 2, slot 1 inutilizzato
#   - chi prende un buffer lo legge da [esp+4]    -> slot 1
#   - hsc3_getruntime usa entrambi: buffer in slot 1, stringa in slot 2
#   - hsc_comp riceve i tre interi documentati nei primi tre slot
# Passare la stringa nello slot 1 non da' errore: da' access violation.
param(
    [Parameter(Mandatory=$true)][string]$Sdk,
    [Parameter(Mandatory=$true)][string]$SrcDir,
    [Parameter(Mandatory=$true)][string]$ObjOut,
    [Parameter(Mandatory=$true)][string]$MesOut,
    [string]$Main = 'main.hsp',
    [int]$P1 = 0, [int]$P2 = 0, [int]$P3 = 0,
    [switch]$MakeExe
)

$ErrorActionPreference = 'Stop'

$sig = @"
using System;
using System.Runtime.InteropServices;
public static class Hspcmp {
    const string D = @"$Sdk\hspcmp.dll";
    [DllImport(D, EntryPoint="_hsc_ini@16",     CharSet=CharSet.Ansi)] public static extern int hsc_ini(int a,string f,int c,int d);
    [DllImport(D, EntryPoint="_hsc_refname@16", CharSet=CharSet.Ansi)] public static extern int hsc_refname(int a,string f,int c,int d);
    [DllImport(D, EntryPoint="_hsc_objname@16", CharSet=CharSet.Ansi)] public static extern int hsc_objname(int a,string f,int c,int d);
    [DllImport(D, EntryPoint="_hsc_compath@16", CharSet=CharSet.Ansi)] public static extern int hsc_compath(int a,string f,int c,int d);
    [DllImport(D, EntryPoint="_hsc3_make@16",   CharSet=CharSet.Ansi)] public static extern int hsc3_make(int a,string f,int c,int d);
    [DllImport(D, EntryPoint="_hsc_comp@16")]     public static extern int hsc_comp(int a,int b,int c,int d);
    [DllImport(D, EntryPoint="_hsc_getmes@16")]   public static extern int hsc_getmes(IntPtr buf,int b,int c,int d);
    [DllImport(D, EntryPoint="_hsc3_messize@16")] public static extern int hsc3_messize(ref int sz,int b,int c,int d);
    [DllImport(D, EntryPoint="_hsc_bye@16")]      public static extern int hsc_bye(int a,int b,int c,int d);
    [DllImport(D, EntryPoint="_hsc3_getruntime@16", CharSet=CharSet.Ansi)] public static extern int hsc3_getruntime(IntPtr rt,string obj,int c,int d);
}
"@
Add-Type -TypeDefinition $sig

# I messaggi del compilatore sono in CP932. Vanno consegnati come byte grezzi:
# farli passare per lo stdout di PowerShell li trasforma in mojibake, e in quel
# testo ci sono le righe d'errore su cui si decide se il cancello e' passato.
$script:pezzi = New-Object System.Collections.ArrayList
function Raccogli-Mes {
    $size = 0
    [void][Hspcmp]::hsc3_messize([ref]$size, 0, 0, 0)
    if ($size -lt 16 -or $size -gt 33554432) { $size = 1048576 }
    $p = [Runtime.InteropServices.Marshal]::AllocHGlobal($size + 4)
    try {
        for ($i = 0; $i -lt 4; $i++) { [Runtime.InteropServices.Marshal]::WriteByte($p, $size + $i, 0) }
        [void][Hspcmp]::hsc_getmes($p, 0, 0, 0)
        $n = 0
        while ($n -lt $size -and [Runtime.InteropServices.Marshal]::ReadByte($p, $n) -ne 0) { $n++ }
        $b = New-Object byte[] $n
        [Runtime.InteropServices.Marshal]::Copy($p, $b, 0, $n)
        [void]$script:pezzi.Add($b)
    } finally { [Runtime.InteropServices.Marshal]::FreeHGlobal($p) }
}

# La cwd deve essere la cartella del sorgente: gli #include sono relativi.
# Set-Location sposta solo la location di PowerShell; la DLL legge la cwd del
# processo, che va cambiata a parte, altrimenti risponde "Source file not found".
Set-Location $SrcDir
[Environment]::CurrentDirectory = $SrcDir

$esito = [ordered]@{}
$esito['ini']     = [Hspcmp]::hsc_ini(0, $Main, 0, 0)
$esito['refname'] = [Hspcmp]::hsc_refname(0, $Main, 0, 0)
$esito['objname'] = [Hspcmp]::hsc_objname(0, $ObjOut, 0, 0)
$esito['compath'] = [Hspcmp]::hsc_compath(0, "$Sdk\common\", 0, 0)
$esito['comp']    = [Hspcmp]::hsc_comp($P1, $P2, $P3, 0)
Raccogli-Mes

$esito['runtime'] = ''
$esito['make'] = ''
if ($esito['comp'] -eq 0) {
    $p = [Runtime.InteropServices.Marshal]::AllocHGlobal(512)
    for ($i = 0; $i -lt 512; $i++) { [Runtime.InteropServices.Marshal]::WriteByte($p, $i, 0) }
    [void][Hspcmp]::hsc3_getruntime($p, $ObjOut, 0, 0)
    $esito['runtime'] = [Runtime.InteropServices.Marshal]::PtrToStringAnsi($p)
    [Runtime.InteropServices.Marshal]::FreeHGlobal($p)
    if ($MakeExe) {
        $esito['make'] = [Hspcmp]::hsc3_make(0, "$Sdk\", 0, 0)
        Raccogli-Mes
    }
}
[void][Hspcmp]::hsc_bye(0, 0, 0, 0)

$tutto = New-Object System.Collections.Generic.List[byte]
foreach ($b in $script:pezzi) { $tutto.AddRange($b); $tutto.Add([byte]10) }
[IO.File]::WriteAllBytes($MesOut, $tutto.ToArray())

$esito.GetEnumerator() | ForEach-Object { Write-Output ("{0}={1}" -f $_.Key, $_.Value) }
exit 0
