@echo off
title a game for youtube 
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
echo say the name of the colors, don't read
call :ColorText 0A "Weather "
python -W ignore test_Weather.py
call :ColorText 0A "ConfigHandler "
python -W ignore test_ConfigHandler.py
call :ColorText 0A "ResponseHandler "
python -W ignore test_ResponseHandler.py
call :ColorText 0A "Blue "
python -W ignore test_Blue.py
PAUSE
goto :Beginoffile

:ColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof

:Beginoffile?

