import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Click The Twing")
root.iconbitmap("thegrin.ico")
root.geometry("400x400")
counter = 0
frame_index = 0
animating = False 

# Load frames
image_files = ["thegrin.png", "thegrin2.png", "thegrin3.png", "thegrin4.png", "thegrin5.png", "thegrin4.png", "thegrin3.png", "thegrin2.png",] 
frames = [ImageTk.PhotoImage(Image.open(img)) for img in image_files]

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

# Label for score
label = tk.Label(root, text="Clicks: 0", font=("Arial", 24))
label.pack(pady=20)

# Button with first frame
button = tk.Button(root, image=frames[0], command=click, borderwidth=0)
button.pack(pady=20)

root.mainloop()
