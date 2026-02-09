import tkinter as tk
from tkinter import ttk
from math import floor


class chess:

    def __init__(self):
        self.main=tk.Tk()
        self.main.title("Chess")
        self.frame=tk.Frame(self.main, relief="ridge", bd=5)
        self.frame.pack()
        font=("Arial", 30)
        self.selectedpice=None
        self.list_of_cases= []
        for i in range (8):
            for j in range (8):
                if (i+j)%2==0: self.list_of_cases.append("#b9a134")
                else: self.list_of_cases.append("#422900")
        self.list_of_pieces= ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        for i in range (8): self.list_of_pieces.append("♟")
        for i in range (32): self.list_of_pieces.append("")
        for i in range (8): self.list_of_pieces.append("♙")
        self.list_of_pieces.extend(["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"])
        self.list_of_colors = []
        for i in range(16): self.list_of_colors.append("black")
        for i in range(32): self.list_of_colors.append("green") #if I forget, it will stand out
        for i in range(16): self.list_of_colors.append("white")

        self.player="white"
        self.playerinfo="Player "+self.player+" on turn."

        self.playerinfolabel=tk.Label(self.frame,text=self.playerinfo, font=("Arial", 10))
        self.playerinfolabel.grid(column=1, columnspan=8)

        self.buttonlist = []
        self.framelist = []
        button_size = 60  # pixels

        for i in range(64):
            btn_frame = tk.Frame(self.frame, width=button_size, height=button_size)
            btn_frame.grid(column=(i%8)+1, row=floor(i/8)+2)
            btn_frame.grid_propagate(False) 
            btn_frame.columnconfigure(0, weight=1)
            btn_frame.rowconfigure(0, weight=1)
            btn = tk.Button(btn_frame, bd=0, font=font, command=lambda i=i: self.buttonclicked(i))
            btn.grid(sticky="wens")
            
            self.buttonlist.append(btn)
            self.framelist.append(btn_frame)
        self.updatebuttons()

        self.main.mainloop()

    def updatebuttons(self):
        for i in range(64):
            self.buttonlist[i]["text"] = self.list_of_pieces[i]
            self.buttonlist[i]["bg"] = self.list_of_cases[i]
            self.buttonlist[i]["activebackground"] = self.list_of_cases[i]
            self.buttonlist[i]["fg"] = self.list_of_colors[i]

    def updatecolor(self, buttonnumber, newcolor):
        self.list_of_colors[buttonnumber] = newcolor

    def getindex(self, column, row):
        return floor((row-1)*8+column-1)
    
    def getcoordinates(self, index):
        return (index%8)+1, floor(index/8)+1
    
    def getpiece(self, columnOrIndex, row=None):
        if row is not None:
            return self.list_of_pieces[self.getindex(columnOrIndex, row)]
        else:
            return self.list_of_pieces[columnOrIndex]
    def row(self):
        return floor(self.selectedpice/8)+1
    def column(self):
        return (self.selectedpice%8)+1
    def won_loose_tie(self):
        pass




    def buttonclicked(self, buttonnumber):
        piece=self.list_of_pieces[buttonnumber]
        print("Button", buttonnumber, "clicked. Piece on button:", piece)
        if self.selectedpice == None: #avoid selecting illegal piece
            if piece=="":
                print("Empty button clicked.")
                return
            
            if self.player=="white" and piece in ["♟", "♜", "♞", "♝", "♛", "♚"]:
                print("Wrong piece clicked.")
                return
            
            if self.player=="black" and piece in ["♙", "♖", "♘", "♗", "♕", "♔"]:
                print("Wrong piece clicked.")
                return

            self.selectedpice = buttonnumber
            print("Selected piece:", piece)

        elif self.selectedpice == buttonnumber:
            self.selectedpice = None

        elif self.getpiece(buttonnumber) in ["♟", "♜", "♞", "♝", "♛", "♚"] and self.player=="white":
            print("You can't move to a place where your own piece is.")

        elif self.getpiece(buttonnumber) in ["♙", "♖", "♘", "♗", "♕", "♔"] and self.player=="black":
            print("You can't move to a place where your own piece is.")

        elif self.getpiece(buttonnumber) == "♙":
            if self.getpiece(buttonnumber-9) == "":
                self.list_of_pieces[buttonnumber-9] = "♙"
                self.list_of_pieces[self.selectedpice] = ""
                self.updatebuttons()
            

            print("Piece on button:", piece)
            self.updatecolor(self.selectedpice, self.player)
            if self.player=="white": self.player="black"
            elif self.player=="black": self.player="white"
            self.playerinfo="Player "+self.player+" on turn."
            self.updatebuttons()
            self.won_loose_tie()
        print("Selected piece:", self.selectedpice)



chess()