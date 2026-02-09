try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class ttt:

    def __init__(self):
        self.main=tk.Tk()
        self.main.title("Tic-Tac-Toe")
        self.frame=tk.Frame(self.main, relief="ridge", bd=5)
        self.frame.pack()

        self.list_of_cases= ["","","","","","","","",""]

        self.player="X"
        self.playerinfo="Player "+self.player+" on turn."

        self.playerinfolabel=tk.Label(self.frame,text=self.playerinfo, font=("Arial", 10))
        self.playerinfolabel.grid(column=1, columnspan=3)

        self.buttonlist  =    [tk.Button(self.frame, text=self.list_of_cases[0], bd=2, height=2, width=4, command=lambda: self.buttonclicked(0))]
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[1], bd=2, height=2, width=4, command=lambda: self.buttonclicked(1)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[2], bd=2, height=2, width=4, command=lambda: self.buttonclicked(2)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[3], bd=2, height=2, width=4, command=lambda: self.buttonclicked(3)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[4], bd=2, height=2, width=4, command=lambda: self.buttonclicked(4)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[5], bd=2, height=2, width=4, command=lambda: self.buttonclicked(5)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[6], bd=2, height=2, width=4, command=lambda: self.buttonclicked(6)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[7], bd=2, height=2, width=4, command=lambda: self.buttonclicked(7)))
        self.buttonlist.append(tk.Button(self.frame, text=self.list_of_cases[8], bd=2, height=2, width=4, command=lambda: self.buttonclicked(8)))

        self.buttonlist[0].grid(column=1,row=2)
        self.buttonlist[1].grid(column=2,row=2)
        self.buttonlist[2].grid(column=3,row=2)
        self.buttonlist[3].grid(column=1,row=3)
        self.buttonlist[4].grid(column=2,row=3)
        self.buttonlist[5].grid(column=3,row=3)
        self.buttonlist[6].grid(column=1,row=4)
        self.buttonlist[7].grid(column=2,row=4)
        self.buttonlist[8].grid(column=3,row=4)

        self.main.mainloop()

    def won_loose_tie(self):
        if self.list_of_cases[0]=="X" and self.list_of_cases[1]=="X" and self.list_of_cases[2]=="X" or self.list_of_cases[3]=="X" and self.list_of_cases[4]=="X" and self.list_of_cases[5]=="X" or self.list_of_cases[6]=="X" and self.list_of_cases[7]=="X" and self.list_of_cases[8]=="X" or self.list_of_cases[0]=="X" and self.list_of_cases[3]=="X" and self.list_of_cases[6]=="X" or self.list_of_cases[1]=="X" and self.list_of_cases[4]=="X" and self.list_of_cases[7]=="X" or self.list_of_cases[2]=="X" and self.list_of_cases[5]=="X" and self.list_of_cases[8]=="X" or self.list_of_cases[0]=="X" and self.list_of_cases[4]=="X" and self.list_of_cases[8]=="X" or self.list_of_cases[6]=="X" and self.list_of_cases[4]=="X" and self.list_of_cases[2]=="X":
            for i in range (9):self.buttonlist[i]["state"]="disabled"
            self.playerinfo="Player X won!"
            self.playerinfolabel["text"]=self.playerinfo

        elif self.list_of_cases[0]=="O" and self.list_of_cases[1]=="O" and self.list_of_cases[2]=="O" or self.list_of_cases[3]=="O" and self.list_of_cases[4]=="O" and self.list_of_cases[5]=="O" or self.list_of_cases[6]=="O" and self.list_of_cases[7]=="O" and self.list_of_cases[8]=="O" or self.list_of_cases[0]=="O" and self.list_of_cases[3]=="O" and self.list_of_cases[6]=="O" or self.list_of_cases[1]=="O" and self.list_of_cases[4]=="O" and self.list_of_cases[7]=="O" or self.list_of_cases[2]=="O" and self.list_of_cases[5]=="O" and self.list_of_cases[8]=="O" or self.list_of_cases[0]=="O" and self.list_of_cases[4]=="O" and self.list_of_cases[8]=="O" or self.list_of_cases[6]=="O" and self.list_of_cases[4]=="O" and self.list_of_cases[2]=="O":
            for i in range (9):self.buttonlist[i]["state"]="disabled"
            self.playerinfo="Player O won!"
            self.playerinfolabel["text"]=self.playerinfo

        elif self.list_of_cases[0]!="" and self.list_of_cases[1]!="" and self.list_of_cases[2]!="" and self.list_of_cases[3]!="" and self.list_of_cases[4]!="" and self.list_of_cases[5]!="" and self.list_of_cases[6]!="" and self.list_of_cases[7]!="" and self.list_of_cases[8]!="":
            for i in range (9):self.buttonlist[i]["state"]="disabled"
            self.playerinfo="Tie!"
            self.playerinfolabel["text"]=self.playerinfo


    def buttonclicked(self, buttonnumber):
        print("Button", buttonnumber, "clicked.")
        self.list_of_cases[buttonnumber]=self.player
        if self.player=="O": self.player="X"
        elif self.player=="X": self.player="O"
        self.playerinfo="Player "+self.player+" on turn."
        self.playerinfolabel["text"]=self.playerinfo
        self.buttonlist[buttonnumber]["text"]=self.list_of_cases[buttonnumber]
        self.won_loose_tie()



ttt()
