# What is Click The Twing? 

A simple and silly little Twingo clicker game. 
---

[![Click The Twingo](https://img.itch.zone/aW1nLzI5ODk0NTcuZ2lm/original/abcd123.gif)](https://jeevesgb.itch.io/click-the-twingo)


## Features

- Click a button to increase your score.
- Easy to build into a standalone `.exe` for Windows.

---

## Screenshots

![Game Screenshot](screenshot.png)  

---

## Requirements

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)  ![Pillow](https://img.shields.io/badge/Pillow-Required-yellow)

- Python 3.8+  
- [Pillow](https://pypi.org/project/Pillow/) library for image support

Install Pillow via pip:

```bash
pip install pillow
```

---

## How to Run

1. Clone or download this repository.
2. Make sure your images (button frames, icon) are in the same folder as `game.py`.
3. Run the game:

```bash
python game.py
```

Or on Windows, double-click the `RunGame.bat`.
---

## 🛠 Building to an EXE

![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey)

To create a standalone `.exe` file:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run the provided batch file:

```bash
BuildGame.bat
```

3. Your `.exe` will be in the `dist` folder with the correct icon.

---

## License

This project is open source. Feel free to modify and distribute

---

## Credits

- Bob Ross 
