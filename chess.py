import tkinter as tk
from tkinter import ttk
from math import floor

# Note to myself or to the mentaly unstable person reading this code:
# self.previouspiece is the index of the piece that is selected, not the piece itself
# it is used to store what piece is selected (or not) between button clicks

class chess:
    def __init__(self):
        self.enpassantenabled = True
        self.kastlingenabled = True
        self.turnboardenabled = True

        self.whitepieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
        self.blackpieces = ["♟", "♜", "♞", "♝", "♛", "♚"]
        self.newwhitepieces = ["♙", "♖", "♘", "♗", "♕", "♔"]
        self.newblackpieces = ["♟", "♜", "♞", "♝", "♛", "♚"]
        self.piecesreplaced = (
            self.whitepieces == self.newwhitepieces and
            self.blackpieces == self.newblackpieces)
        
        

        if self.kastlingenabled:
            self.whitecastlingkingside = True
            self.whitecastlingqueenside = True
            self.blackcastlingkingside = True
            self.blackcastlingqueenside = True
        else:
            self.whitecastlingkingside = False
            self.whitecastlingqueenside = False
            self.blackcastlingkingside = False
            self.blackcastlingqueenside = False
        self.main=tk.Tk()
        self.main.title("Chess")
        self.frame=tk.Frame(self.main, relief="ridge", bd=5)
        self.frame.pack()
        font=("Arial", 30)
        self.previouspiece=None
        self.player="White"
        self.playerinfo=self.player+"'s turn."
        self.playerinfolabel=tk.Label(self.frame, font=("Arial", 10))
        self.playerinfolabel.grid(column=1, columnspan=8)
        self.list_of_cases= []
        self.list_of_pieces= ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
        for i in range (8): self.list_of_pieces.append("♟")
        for i in range (32): self.list_of_pieces.append("")
        for i in range (8): self.list_of_pieces.append("♙")
        self.list_of_pieces.extend(["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"])
        self.list_of_colors = []
        for i in range(16): self.list_of_colors.append("Black")
        for i in range(32): self.list_of_colors.append("green") #if I forget, it will stand out
        for i in range(16): self.list_of_colors.append("White")

        self.buttonlist = []
        self.framelist = []
        self.button_size = 60  # pixels
                                # If using pyroid, change this value to 130.
                                # It was good for me (Pixel 8)

        for i in range(64):
            self.btn_frame = tk.Frame(self.frame, width=self.button_size, height=self.button_size)
            self.btn_frame.grid(column=(i%8)+1, row=floor(i/8)+2)
            self.btn_frame.grid_propagate(False) 
            self.btn_frame.columnconfigure(0, weight=1)
            self.btn_frame.rowconfigure(0, weight=1)
            btn = tk.Button(self.btn_frame, bd=0, font=font, command=lambda i=i: self.buttonclicked(i))
            btn.grid(sticky="wens") #thanks stackoverflow
            
            self.buttonlist.append(btn)
            self.framelist.append(self.btn_frame)
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
            piece = self.list_of_pieces[i]
            # Hide internal en passant markers from the UI
            if piece == "ep":
                piece = ""
            if self.piecesreplaced:
                if piece in self.whitepieces:
                    piece = self.newwhitepieces[self.whitepieces.index(piece)]
                elif piece in self.blackpieces:
                    piece = self.newblackpieces[self.blackpieces.index(piece)]

            
            self.buttonlist[i]["text"] = piece
            self.buttonlist[i]["bg"] = self.list_of_cases[i]
            self.buttonlist[i]["activebackground"] = self.list_of_cases[i]
            self.buttonlist[i]["fg"] = self.list_of_colors[i]
        if self.turnboardenabled:
            if self.player=="White":
                for i in range(64):
                    self.framelist[i].grid(column=(i%8)+1, row=floor(i/8)+2)
            
            else:
                for i in range(64):
                    self.framelist[i].grid(column=((63-i)%8)+1, row=floor((63-i)/8)+2)



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
    def row(self, case):
        return floor(case/8)+1
    def column(self, case):
        return (case%8)+1
    
    def movepiece(self, origin, destination, simulation=False):
        if self.enpassantenabled:
            if self.getpiece(origin) in ["♙", "♟"] and self.getpiece(destination) == "ep":
                captured_pawn_index = self.getindex(self.column(destination), self.row(origin))
                self.list_of_pieces[captured_pawn_index] = ""
                self.updatecolor(captured_pawn_index, "green")

            for i in range(64):
                if self.getpiece(i) == "ep":
                    self.list_of_pieces[i] = ""
                    self.updatecolor(i, "green")
        if self.kastlingenabled:
            # Update castling rights if king or rooks move / are captured
            if self.getpiece(origin) == "♔":
                self.whitecastlingkingside = False
                self.whitecastlingqueenside = False
            elif self.getpiece(origin) == "♚":
                self.blackcastlingkingside = False
                self.blackcastlingqueenside = False
            if self.getpiece(0) != "♜":
                self.blackcastlingqueenside = False
            if self.getpiece(7) != "♜":
                self.blackcastlingkingside = False
            if self.getpiece(56) != "♖":
                self.whitecastlingqueenside = False
            if self.getpiece(63) != "♖":
                self.whitecastlingkingside = False

        # Move the piece
        self.list_of_pieces[destination] = self.list_of_pieces[origin]
        self.list_of_pieces[origin] = ""

        # Handle rook movement for castling
        if self.kastlingenabled and self.getpiece(destination) in ["♔", "♚"] and abs(self.column(destination) - self.column(origin)) == 2 and self.row(destination) == self.row(origin):
            # White castling
            if self.getpiece(destination) == "♔":
                # Kingside: e1 (60) -> g1 (62), rook h1 (63) -> f1 (61)
                if destination == 62:
                    self.list_of_pieces[61] = self.list_of_pieces[63]
                    self.list_of_pieces[63] = ""
                    self.updatecolor(61, "White")
                    self.updatecolor(63, "green")
                # Queenside: e1 (60) -> c1 (58), rook a1 (56) -> d1 (59)
                elif destination == 58:
                    self.list_of_pieces[59] = self.list_of_pieces[56]
                    self.list_of_pieces[56] = ""
                    self.updatecolor(59, "White")
                    self.updatecolor(56, "green")
                self.whitecastlingkingside = False
                self.whitecastlingqueenside = False
            # Black castling
            elif self.getpiece(destination) == "♚":
                # Kingside: e8 (4) -> g8 (6), rook h8 (7) -> f8 (5)
                if destination == 6:
                    self.list_of_pieces[5] = self.list_of_pieces[7]
                    self.list_of_pieces[7] = ""
                    self.updatecolor(5, "Black")
                    self.updatecolor(7, "green")
                # Queenside: e8 (4) -> c8 (2), rook a8 (0) -> d8 (3)
                elif destination == 2:
                    self.list_of_pieces[3] = self.list_of_pieces[0]
                    self.list_of_pieces[0] = ""
                    self.updatecolor(3, "Black")
                    self.updatecolor(0, "green")
                self.blackcastlingkingside = False
                self.blackcastlingqueenside = False
        if self.enpassantenabled and self.getpiece(destination) in ["♙", "♟"] and abs(self.row(destination)-self.row(origin))==2:
            self.list_of_pieces[self.getindex(self.column(destination), (self.row(destination)+self.row(origin))//2)] = "ep"
            self.updatecolor(self.getindex(self.column(destination), (self.row(destination)+self.row(origin))//2), "green")
        if not simulation:
            if self.row(destination)==8 and self.getpiece(destination)=="♟":
                self.promote_pawn(destination)
            if self.row(destination)==1 and self.getpiece(destination)=="♙":
                self.promote_pawn(destination)
    
    def promote_pawn(self, index):
        aux=tk.Tk()
        aux.title("Tic-Tac-Toe")
        frame=tk.Frame(aux, relief="ridge", bd=5)
        frame.pack()
        if self.getpiece(index) == "♙":
            list_of_possibilities= ["♕","♖","♗","♘"]
        else:
            list_of_possibilities= ["♛","♜","♝","♞"]
        for i in range(4):
            btn = tk.Button(frame, text=list_of_possibilities[i], font=("Arial", 20), command=lambda i=i: self.promote_and_close(index, list_of_possibilities[i], aux))
            btn.grid(column=i, row=0)
    def promote_and_close(self, index, new_piece, window):
        self.list_of_pieces[index] = new_piece
        window.destroy()
        self.updatebuttons()


    def legalmove(self, origin, destination):

        if origin == destination:
            return False 
        if self.getpiece(destination) in ["♟", "♜", "♞", "♝", "♛", "♚"] and self.player=="Black":
            return False
        if self.getpiece(destination) in ["♙", "♖", "♘", "♗", "♕", "♔"] and self.player=="White":
            return False
        
        if not (origin is None or destination is None) and self.simulate_move(origin, destination):
            return False
        
        if self.getpiece(origin) == "♙":
            if self.getpiece(destination) == "" and self.column(destination)==self.column(origin) and (
                self.row(destination)==self.row(origin)-1 or (
                    self.row(origin)==7 and self.row(destination)==5 and self.getpiece(self.getindex(self.column(origin), 6))==""
                )
            ):
                return True
            if self.getpiece(destination) in ["♟", "♜", "♞", "♝", "♛", "♚"] and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)-1:
                return True
            if self.enpassantenabled and self.getpiece(destination) == "ep" and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)-1:
                return True

        if self.getpiece(origin) == "♟":
            if self.getpiece(destination) == "" and self.column(destination)==self.column(origin) and (
                self.row(destination)==self.row(origin)+1 or (
                    self.row(origin)==2 and self.row(destination)==4 and self.getpiece(self.getindex(self.column(origin), 3))==""
                )
            ):
                return True
            if self.getpiece(destination) in ["♙", "♖", "♘", "♗", "♕", "♔"] and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)+1:
                return True
            if self.enpassantenabled and self.getpiece(destination) == "ep" and abs(self.column(destination)-self.column(origin))==1 and self.row(destination)==self.row(origin)+1:
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
        
        if self.getpiece(origin) in ["♔", "♚"]:
            if abs(self.column(destination)-self.column(origin))<=1 and abs(self.row(destination)-self.row(origin))<=1:
                return True
            elif self.kastlingenabled and abs(self.column(destination)-self.column(origin))==2 and self.row(destination)==self.row(origin):
                if self.getpiece(origin) == "♔":
                    # White kingside: e1 -> g1 (destination 62), squares f1 (61) and g1 (62) must be empty
                    if destination == 62 and self.whitecastlingkingside and self.getpiece(61) == "" and self.getpiece(62) == "":
                        # Cannot castle out of, through, or into check
                        middle = (origin + destination) // 2
                        if self.ischeck(self.player) or self.simulate_move(origin, middle):
                            return False
                        return True
                    # White queenside: e1 -> c1 (destination 58), squares d1 (59), c1 (58), b1 (57) must be empty
                    if destination == 58 and self.whitecastlingqueenside and self.getpiece(59) == "" and self.getpiece(58) == "" and self.getpiece(57) == "":
                        middle = (origin + destination) // 2
                        if self.ischeck(self.player) or self.simulate_move(origin, middle):
                            return False
                        return True
                if self.getpiece(origin) == "♚":
                    # Black kingside: e8 -> g8 (destination 6), squares f8 (5) and g8 (6) must be empty
                    if destination == 6 and self.blackcastlingkingside and self.getpiece(5) == "" and self.getpiece(6) == "":
                        middle = (origin + destination) // 2
                        if self.ischeck(self.player) or self.simulate_move(origin, middle):
                            return False
                        return True
                    # Black queenside: e8 -> c8 (destination 2), squares d8 (3), c8 (2), b8 (1) must be empty
                    if destination == 2 and self.blackcastlingqueenside and self.getpiece(3) == "" and self.getpiece(2) == "" and self.getpiece(1) == "":
                        middle = (origin + destination) // 2
                        if self.ischeck(self.player) or self.simulate_move(origin, middle):
                            return False
                        return True
                
                    
        if self.getpiece(origin) in ["♘", "♞"] and ((abs(self.column(destination)-self.column(origin))==2 and abs(self.row(destination)-self.row(origin))==1) or (abs(self.column(destination)-self.column(origin))==1 and abs(self.row(destination)-self.row(origin))==2)):
            return True
        
        return False


    def simulate_move(self, origin, destination):
        """Simulate moving a piece from origin to destination, and
        return True if this leaves the current player in check."""

        original_player = self.player
        # Save castling rights so simulate_move is side‑effect free
        original_whitecastlingkingside = self.whitecastlingkingside
        original_whitecastlingqueenside = self.whitecastlingqueenside
        original_blackcastlingkingside = self.blackcastlingkingside
        original_blackcastlingqueenside = self.blackcastlingqueenside
        original_pieces = self.list_of_pieces.copy()
        original_colors = self.list_of_colors.copy()

        self.movepiece(origin, destination, simulation=True)

        in_check = self.ischeck(original_player)

        # Restore board and player/colour state
        self.list_of_pieces = original_pieces
        self.list_of_colors = original_colors
        self.player = original_player
        self.whitecastlingkingside = original_whitecastlingkingside
        self.whitecastlingqueenside = original_whitecastlingqueenside
        self.blackcastlingkingside = original_blackcastlingkingside
        self.blackcastlingqueenside = original_blackcastlingqueenside

        return in_check

    def piece_attacks_square(self, origin, destination): #This function is AI generated
        """Return True if the piece on origin attacks destination (ignores self-check rules)."""
        if origin == destination:
            return False

        piece = self.getpiece(origin)
        if piece == "":
            return False

        col_o, row_o = self.column(origin), self.row(origin)
        col_d, row_d = self.column(destination), self.row(destination)

        # Pawns: only capture moves matter for check detection
        if piece == "♙":  # white pawn
            return abs(col_d - col_o) == 1 and row_d == row_o - 1
        if piece == "♟":  # black pawn
            return abs(col_d - col_o) == 1 and row_d == row_o + 1

        # Rooks
        if piece in ["♖", "♜"]:
            if col_d == col_o and row_d != row_o:
                for r in range(min(row_o, row_d) + 1, max(row_o, row_d)):
                    if self.getpiece(self.getindex(col_o, r)) != "":
                        return False
                return True
            if row_d == row_o and col_d != col_o:
                for c in range(min(col_o, col_d) + 1, max(col_o, col_d)):
                    if self.getpiece(self.getindex(c, row_o)) != "":
                        return False
                return True

        # Bishops
        if piece in ["♗", "♝"]:
            if abs(col_d - col_o) == abs(row_d - row_o):
                steps = abs(col_d - col_o)
                row_dir = 1 if row_d > row_o else -1
                col_dir = 1 if col_d > col_o else -1
                for i in range(1, steps):
                    if self.getpiece(self.getindex(col_o + i * col_dir, row_o + i * row_dir)) != "":
                        return False
                return True

        # Queens
        if piece in ["♕", "♛"]:
            if col_d == col_o and row_d != row_o:
                for r in range(min(row_o, row_d) + 1, max(row_o, row_d)):
                    if self.getpiece(self.getindex(col_o, r)) != "":
                        return False
                return True
            if row_d == row_o and col_d != col_o:
                for c in range(min(col_o, col_d) + 1, max(col_o, col_d)):
                    if self.getpiece(self.getindex(c, row_o)) != "":
                        return False
                return True
            if abs(col_d - col_o) == abs(row_d - row_o):
                steps = abs(col_d - col_o)
                row_dir = 1 if row_d > row_o else -1
                col_dir = 1 if col_d > col_o else -1
                for i in range(1, steps):
                    if self.getpiece(self.getindex(col_o + i * col_dir, row_o + i * row_dir)) != "":
                        return False
                return True

        # Kings
        if piece in ["♔", "♚"]:
            return abs(col_d - col_o) <= 1 and abs(row_d - row_o) <= 1

        # Knights
        if piece in ["♘", "♞"]:
            return (abs(col_d - col_o) == 2 and abs(row_d - row_o) == 1) or \
                   (abs(col_d - col_o) == 1 and abs(row_d - row_o) == 2)

        return False

    def ischeck(self, player):
        king_position = None
        king_symbol = "♔" if player == "White" else "♚"
# why are you checking this code, do you not have something better to do?
        for i in range(64):
            if self.getpiece(i) == king_symbol:
                king_position = i
                break
        if king_position is None:
            raise LookupError("The king is gone, how did you even do that? This is illegal, get the chess police!")

        opponent_pieces = (["♟", "♜", "♞", "♝", "♛", "♚"]
                           if player == "White"
                           else ["♙", "♖", "♘", "♗", "♕", "♔"])

        for i in range(64):
            if self.getpiece(i) in opponent_pieces and self.piece_attacks_square(i, king_position):
                return True

        return False
    def ischeckmate(self, player):
        if not self.ischeck(player):
            return False
        for i in range(64):
            if self.getpiece(i) in (["♙", "♖", "♘", "♗", "♕", "♔"] if player=="White" else ["♟", "♜", "♞", "♝", "♛", "♚"]):
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
        if self.previouspiece == None: #avoid selecting illegal pieces
            if piece=="":
                return
            
            if self.player=="White" and piece in ["♟", "♜", "♞", "♝", "♛", "♚"]:
                return
            
            if self.player=="Black" and piece in ["♙", "♖", "♘", "♗", "♕", "♔"]:
                return

            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.previouspiece == buttonnumber:
            self.previouspiece = None

        elif self.getpiece(buttonnumber) in ["♟", "♜", "♞", "♝", "♛", "♚"] and self.player=="Black": #select another piece
            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.getpiece(buttonnumber) in ["♙", "♖", "♘", "♗", "♕", "♔"] and self.player=="White":
            self.previouspiece = buttonnumber
            self.highlightlegalmoves(buttonnumber)

        elif self.legalmove(self.previouspiece, buttonnumber):
            self.movepiece(self.previouspiece, buttonnumber)
            self.updatecolor(buttonnumber, self.player)
            self.updatecolor(self.previouspiece, "green")
            self.previouspiece = None
            if self.player=="White": self.player="Black"
            elif self.player=="Black": self.player="White"
            self.playerinfo=self.player+"'s turn."
            if self.ischeckmate(self.player):
                self.playerinfo="Player "+("White" if self.player=="Black" else "Black")+" wins by checkmate!"
            self.updatebuttons()
            
        

chess()
# Start eveything Yepeeeeeeee
