import tkinter as tk
from tkinter import ttk
from math import floor

# main window
root = tk.Tk()
root.geometry("800x800")
root.title('Chess')

Buttons=[]

# grid 64x64
# 2 more for displaying captured pieces
for i in range(64):
    root.rowconfigure(i, weight=1)

for i in range(64):
    root.columnconfigure(i, weight=1)


for i in range(64):
    button = ttk.Button(root, text="")
    button.grid(column=floor((i/8)), row=i%8)


root.mainloop()