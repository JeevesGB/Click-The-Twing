@echo off
REM Build game into a single EXE with icon
pyinstaller --onefile --windowed --icon=thegrin.ico --name ClickTheTwing --add-data "thegrin.png;." --add-data "thegrin2.png;." --add-data "thegrin3.png;." --add-data "thegrin4.png;." --add-data "thegrin5.png;." game.py
REM Move EXE to a clean "dist" folder
echo.
echo Build complete! Your exe is in the "dist" folder.
pause
