@echo off
REM Build game into a single EXE with icon
pyinstaller --onefile --windowed --icon=thegrin.ico --name Click The Twing game.py

REM Move EXE to a clean "dist" folder
echo.
echo Build complete! Your exe is in the "dist" folder.
pause
