@echo off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
=
call :ColorText 0A "Installing Module_Weather"
echo.
git clone https://github.com/Tomekske/Module_Weather
cd Module_Weather
move Weather.py ../Modules/Weather/Weather.py
move test_Weather.py ../Test/test_Weather.py
cd ..
RD /S /Q Module_Weather
echo.
echo.

call :ColorText 0A "Installing Module_ConfigHandler"
echo.
git clone https://github.com/Tomekske/Module_ConfigHandler
cd Module_ConfigHandler
move ConfigHandler.py ../Modules/ConfigHandler/ConfigHandler.py
move test_ConfigHandler.py ../Test/test_ConfigHandler.py
cd ..
RD /S /Q Module_ConfigHandler
echo.
echo.

call :ColorText 0A "Installing Module_ResponseHandler"
echo.
git clone https://github.com/Tomekske/Module_ResponseHandler
cd Module_ResponseHandler
move ResponseHandler.py ../Modules/ResponseHandler/ResponseHandler.py
move test_ResponseHandler.py ../Test/test_ResponseHandler.py
cd ..
RD /S /Q Module_ResponseHandler
echo.
echo.
goto :Beginoffile

:ColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof

:Beginoffile