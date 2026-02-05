import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.geometry("660x640")
root.title('Chess')

Buttons=[]

# grid 64x64
# 2 more for displaying captured pieces
for i in range(64):
    root.rowconfigure(i, weight=1)

for i in range(64):
    root.columnconfigure(i, weight=1)


for i in range(64):
    button = ttk.Button(root, text="Login")
    button.grid(column=(i/8)__floor__, row=i%8)


root.mainloop()