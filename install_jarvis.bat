@echo off
REM JARVIS Installation Script for Windows
REM This script will set up JARVIS assistant on your Windows system

echo ======================================================
echo.
echo          JARVIS Installation Script
echo.
echo ======================================================
echo.

REM Check Python version
echo Checking Python version...
python --version 2>NUL
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.7 or higher from https://www.python.org
    pause
    exit /b 1
)

echo.
echo Installing Python packages...
echo.

REM Upgrade pip
python -m pip install --upgrade pip

REM Install required packages
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation encountered errors.
    echo You may need to manually install some packages.
    echo.
    echo For PyAudio on Windows, download the wheel file from:
    echo https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
    echo Then install with: pip install [downloaded-wheel-file]
    pause
    exit /b 1
)

echo.
echo ======================================================
echo.
echo          Installation Complete!
echo.
echo ======================================================
echo.
echo To run JARVIS:
echo   Text Mode:  python jarvis.py --text
echo   Voice Mode: python jarvis.py
echo.
echo For help:     python jarvis_examples.py
echo Documentation: See JARVIS_README.md
echo.
echo Note: Voice mode requires a working microphone.
echo If you have issues with PyAudio, see troubleshooting
echo section in JARVIS_README.md
echo.
echo Enjoy your personal AI assistant!
echo.
pause
