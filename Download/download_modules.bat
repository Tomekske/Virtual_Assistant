@echo off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
=
call :ColorText 0A "Installing configparser"
echo.
pip install configparser
echo.
echo.

call :ColorText 0A "Installing SpeechRecognition"
echo.
pip install SpeechRecognition
echo.
echo.

call :ColorText 0A "Installing PyAudio"
echo.
pip install PyAudio
echo.
echo.

call :ColorText 0A "Installing colorama"
echo.
pip install colorama
echo.
echo.

call :ColorText 0A "Installing arrow"
echo.
pip install arrow
echo.
echo.

call :ColorText 0A "Installing nltk"
echo.
pip install nltk
echo.
echo.

call :ColorText 0A "Installing numpy"
echo.
pip install numpy
echo.
echo.

call :ColorText 0A "Installing requests"
echo.
pip install requests
echo.
echo.

call :ColorText 0A "Installing httplib2"
echo.
pip install httplib2
echo.
echo.

call :ColorText 0A "Installing pyglet"
echo.
pip install pyglet
echo.
echo.

call :ColorText 0A "Installing gtts"
echo.
pip install gtts
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