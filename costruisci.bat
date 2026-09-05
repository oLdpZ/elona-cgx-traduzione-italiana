@echo off
setlocal
cd /d "%~dp0"

where python >nul 2>&1
if errorlevel 1 goto senzapython

python costruisci.py %*
echo.
pause
exit /b 0

:senzapython
echo.
echo Serve Python 3.11 o piu' nuovo, e in questo computer non lo trovo.
echo.
echo Scaricalo da   https://www.python.org/downloads/
echo e durante l'installazione spunta la casella
echo    "Add python.exe to PATH"
echo poi rilancia questo file.
echo.
pause
exit /b 1
