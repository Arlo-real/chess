import tkinter as tk
from tkinter import ttk
from math import floor

# Note to myself or to the mentaly unstable person reading this code:
# self.previouspiece is the index of the piece that is selected, not the piece itself
# it is used to store what piece is selected (or not) between button clicks

class chess:
    def __init__(self):
        self.main=tk.Tk()
        self.main.title("Chess")
        self.frame=tk.Frame(self.main, relief="ridge", bd=5)
        self.frame.pack()
        font=("Arial", 30)
        self.previouspiece=None
        self.player="white"
        self.playerinfo="Player "+self.player+" on turn."
        self.playerinfolabel=tk.Label(self.frame, font=("Arial", 10))
        self.playerinfolabel.grid(column=1, columnspan=8)
        self.list_of_cases= []
        self.list_of_pieces= ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        for i in range (8): self.list_of_pieces.append("♟")
        for i in range (32): self.list_of_pieces.append("")
        for i in range (8): self.list_of_pieces.append("♙")
        self.list_of_pieces.extend(["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"])
        self.list_of_colors = []
        for i in range(16): self.list_of_colors.append("black")
        for i in range(32): self.list_of_colors.append("green") #if I forget, it will stand out
        for i in range(16): self.list_of_colors.append("white")



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
            btn.grid(sticky="wens") #thanks stackoverflow
            
            self.buttonlist.append(btn)
            self.framelist.append(btn_frame)
        for i in range (8):
            for j in range (8):
                if (i+j)%2==0: self.list_of_cases.append("#b9a134")
                else: self.list_of_cases.append("#422900")
        self.updatebuttons()

        self.main.mainloop()
    
    def colorcases(self):
        for i in range (64):
            if (i%8 + floor(i/8))%2==0: self.list_of_cases[i] = "#b9a134"
            else: self.list_of_cases[i] = "#422900"
        self.updatebuttons()

    def updatebuttons(self):
        self.playerinfolabel["text"] = self.playerinfo
        for i in range(64):
            self.buttonlist[i]["text"] = self.list_of_pieces[i]
            self.buttonlist[i]["bg"] = self.list_of_cases[i]
            self.buttonlist[i]["activebackground"] = self.list_of_cases[i]
            self.buttonlist[i]["fg"] = self.list_of_colors[i]

    def updatecolor(self, buttonnumber, newcolor):
        print("Updating color of button", buttonnumber, "to", newcolor)
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
    def row(self, case):
        return floor(case/8)+1
    def column(self, case):
        return (case%8)+1
    def won_loose_tie(self):
        pass
    
    def movepiece(self, origin, destination):
        self.list_of_pieces[destination] = self.list_of_pieces[origin]
        self.list_of_pieces[origin] = ""

    def legalmove(self, origin, destination):

        if origin == destination:
            return False 
        if self.getpiece(destination) in ["♟", "♜", "♞", "♝", "♛", "♚"] and self.player=="black":
            return False
        if self.getpiece(destination) in ["♙", "♖", "♘", "♗", "♕", "♔"] and self.player=="white":
            return False
        
        if not(origin==None or destination==None) and self.simulate_move(origin, destination):
            return False
        
        if self.getpiece(origin) == "♙" and self.getpiece(destination) == "" and self.column(destination)==self.column(origin) and (self.row(destination)==self.row(origin)-1 or (self.row(origin)==7 and self.row(destination)==5 and self.getpiece(self.getindex(self.column(origin), 6))=="")):
            return True
        if self.getpiece(origin) == "♙" and self.getpiece(destination) in ["♟", "♜", "♞", "♝", "♛", "♚"] and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)-1:
            return True
        if self.getpiece(origin) == "♟" and self.getpiece(destination) == "" and self.column(destination)==self.column(origin) and (self.row(destination)==self.row(origin)+1 or (self.row(origin)==2 and self.row(destination)==4 and self.getpiece(self.getindex(self.column(origin), 3))=="")):
            return True
        if self.getpiece(origin) == "♟" and self.getpiece(destination) in ["♙", "♖", "♘", "♗", "♕", "♔"] and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)+1:
            return True
        if self.getpiece(origin) == "♖" and self.column(destination)==self.column(origin) and self.row(destination)!=self.row(origin):
            for i in range(min(self.row(origin), self.row(destination))+1, max(self.row(origin), self.row(destination))):
                if self.getpiece(self.getindex(self.column(origin), i))!="":
                    return False
            return True
        if self.getpiece(origin) == "♖" and self.row(destination)==self.row(origin) and self.column(destination)!=self.column(origin):
            for i in range(min(self.column(origin), self.column(destination))+1, max(self.column(origin), self.column(destination))):
                if self.getpiece(self.getindex(i, self.row(origin)))!="":
                    return False
            return True
        if self.getpiece(origin) == "♜" and self.column(destination)==self.column(origin) and self.row(destination)!=self.row(origin):
            for i in range(min(self.row(origin), self.row(destination))+1, max(self.row(origin), self.row(destination))):
                if self.getpiece(self.getindex(self.column(origin), i))!="":
                    return False
            return True
        if self.getpiece(origin) == "♜" and self.row(destination)==self.row(origin) and self.column(destination)!=self.column(origin):
            for i in range(min(self.column(origin), self.column(destination))+1, max(self.column(origin), self.column(destination))):
                if self.getpiece(self.getindex(i, self.row(origin)))!="":
                    return False
            return True
        

        if self.getpiece(origin) == "♗" and abs(self.column(destination)-self.column(origin)) == abs(self.row(destination)-self.row(origin)):
            steps=abs(self.column(destination)-self.column(origin))
            dowdirection=1 if self.row(destination)>self.row(origin) else -1
            columndirection=1 if self.column(destination)>self.column(origin) else -1
            for i in range(1,steps):
                if self.getpiece(self.getindex(self.column(origin)+i*columndirection, self.row(origin)+i*dowdirection))!="":
                    return False
            return True
        if self.getpiece(origin) == "♝" and abs(self.column(destination)-self.column(origin)) == abs(self.row(destination)-self.row(origin)):
            steps=abs(self.column(destination)-self.column(origin))
            dowdirection=1 if self.row(destination)>self.row(origin) else -1
            columndirection=1 if self.column(destination)>self.column(origin) else -1
            for i in range(1,steps):
                if self.getpiece(self.getindex(self.column(origin)+i*columndirection, self.row(origin)+i*dowdirection))!="":
                    return False
            return True
        
        if self.getpiece(origin) in ["♕", "♛"]:
            if self.column(destination)==self.column(origin) and self.row(destination)!=self.row(origin):
                for i in range(min(self.row(origin), self.row(destination))+1, max(self.row(origin), self.row(destination))):
                    if self.getpiece(self.getindex(self.column(origin), i))!="":
                        return False
            elif self.row(destination)==self.row(origin) and self.column(destination)!=self.column(origin):
                for i in range(min(self.column(origin), self.column(destination))+1, max(self.column(origin), self.column(destination))):
                    if self.getpiece(self.getindex(i, self.row(origin)))!="":
                        return False

            elif abs(self.column(destination)-self.column(origin)) == abs(self.row(destination)-self.row(origin)):
                steps=abs(self.column(destination)-self.column(origin))
                dowdirection=1 if self.row(destination)>self.row(origin) else -1
                columndirection=1 if self.column(destination)>self.column(origin) else -1
                for i in range(1,steps):
                    if self.getpiece(self.getindex(self.column(origin)+i*columndirection, self.row(origin)+i*dowdirection))!="":
                        return False
            else: return False
            return True        
        
        if self.getpiece(origin) in ["♔", "♚"] and abs(self.column(destination)-self.column(origin))<=1 and abs(self.row(destination)-self.row(origin))<=1:
            return True
        if self.getpiece(origin) in ["♘", "♞"] and ((abs(self.column(destination)-self.column(origin))==2 and abs(self.row(destination)-self.row(origin))==1) or (abs(self.column(destination)-self.column(origin))==1 and abs(self.row(destination)-self.row(origin))==2)):
            return True
        
        return False


    def simulate_move(self, origin, destination):
        original_piece_destination = self.getpiece(destination)
        self.movepiece(origin, destination)
        is_check = self.ischeck(self.player)
        self.movepiece(destination, origin)  # Move back to original position
        self.list_of_pieces[destination] = original_piece_destination  # Restore captured piece if any
        return is_check



    def ischeck(self, player):
        king_position=None
        for i in range(64):
            if self.getpiece(i) == ("♔" if player=="white" else "♚"):
                king_position = i
                break
        if king_position is None:
            raise LookupError("The king is gone, how did you even do that?")
        for i in range(64):
            if self.legalmove(i, king_position):
                return True
        return False
    def ischeckmate(self, player):
        if not self.ischeck(player):
            return False
        for i in range(64):
            if self.getpiece(i) in (["♙", "♖", "♘", "♗", "♕", "♔"] if player=="white" else ["♟", "♜", "♞", "♝", "♛", "♚"]):
                for j in range(64):
                    if self.legalmove(i, j) and not self.simulate_move(i, j):
                        return False
        return True


    def highlightlegalmoves(self, origin):
        for i in range(64):
            if self.legalmove(origin, i):
                self.list_of_cases[i] = "yellow"
        self.updatebuttons()

    def buttonclicked(self, buttonnumber):
        self.colorcases()
        piece=self.list_of_pieces[buttonnumber]
        print("Button", buttonnumber, "clicked. Piece on button:", piece)
        if self.previouspiece == None: #avoid selecting illegal pieces
            if piece=="":
                print("Empty button clicked.")
                return
            
            if self.player=="white" and piece in ["♟", "♜", "♞", "♝", "♛", "♚"]:
                print("Wrong piece clicked.")
                return
            
            if self.player=="black" and piece in ["♙", "♖", "♘", "♗", "♕", "♔"]:
                print("Wrong piece clicked.")
                return

            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.previouspiece == buttonnumber:
            self.previouspiece = None

        elif self.getpiece(buttonnumber) in ["♟", "♜", "♞", "♝", "♛", "♚"] and self.player=="black": #select another piece
            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.getpiece(buttonnumber) in ["♙", "♖", "♘", "♗", "♕", "♔"] and self.player=="white":
            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.legalmove(self.previouspiece, buttonnumber):
            self.movepiece(self.previouspiece, buttonnumber)
            self.updatecolor(buttonnumber, self.player)
            self.updatecolor(self.previouspiece, "green")
            self.previouspiece = None
            if self.player=="white": self.player="black"
            elif self.player=="black": self.player="white"
            self.playerinfo="Player "+self.player+" on turn."
            if self.ischeckmate(self.player):
                self.playerinfo="Player "+("white" if self.player=="black" else "black")+" wins by checkmate!"
            self.updatebuttons()
            
        print("Selected piece:", self.previouspiece)
        



chess()