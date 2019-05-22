from tkinter import *


class CheckerSquare(Canvas):

    def __init__(self, master, r, c):
        Canvas.__init__(self,master,width=50,height=50,bg="Blanched Almond")
        self.grid(row=r,column=c)
        self.position = (r,c)


class CheckerBoard:

    def __init__(self):
        self.board = {}

        pass

        self.currentPlayer = 0

        def get_piece(self, coords):
            return self.board[coords]

        def get_player(self):
            return self.currentPlayer

class CheckersGame(Frame):

    def __init__(self, master):
        Frame.__init__(self,master, bg='white')
        self.grid()
        self.colors = ('red', 'white')
        self.board = CheckerBoard
        self.squares = {}
        for row in range(8):
            for column in range(8):
                self.squares[(row,column)] = CheckerSquare(self, row, column)
        self.rowconfigure(8, minsize=3)
        self.turnSquares = []
        self.scoreLabels = []

