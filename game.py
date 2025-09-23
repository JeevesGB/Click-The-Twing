import os
import sys
import tkinter as tk
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

root = tk.Tk()
root.title("Click The Twing")
root.geometry("400x400")

ico_path = resource_path("thegrin.ico")
if os.path.exists(ico_path):
    root.iconbitmap(ico_path)
else:
    print(f"Warning: Icon '{ico_path}' not found. Using default.")

counter = 0
animating = False

image_names = [
    "thegrin.png", "thegrin2.png", "thegrin3.png", "thegrin4.png",
    "thegrin5.png", "thegrin4.png", "thegrin3.png", "thegrin2.png"
]
frames = []
for name in image_names:
    path = resource_path(name)
    if os.path.exists(path):
        frames.append(ImageTk.PhotoImage(Image.open(path)))
    else:
        raise FileNotFoundError(f"Image '{path}' not found.")

def click():
    global counter, animating
    counter += 1
    label.config(text=f"Clicks: {counter}")
    if not animating:
        animate(0)

def animate(i):
    global animating
    animating = True
    if i < len(frames):
        button.config(image=frames[i])
        root.after(50, animate, i+1)
    else:
        button.config(image=frames[0])
        animating = False

label = tk.Label(root, text="Clicks: 0", font=("Arial", 24))
label.pack(pady=20)

button = tk.Button(root, image=frames[0], command=click, borderwidth=0)
button.pack(pady=20)

root.mainloop()
