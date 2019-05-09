from tkinter import *
from random import *


class minesweeperCell(Canvas):
    def __init__(self, master, coord, remBombs, colormap = [], surroundingBombs=0):
        self.canvasWidth=50
        self.canvasHeight=50
        Canvas.__init__(self, master, width=self.canvasWidth, height=self.canvasHeight, bg='white', bd=3, relief=RAISED)
        self.coord = coord
        self.surroundingBombs = surroundingBombs
        self.mine = False
        self.blank = True
        self.flagged = False
        self.exposed = False
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-3>', self.flag)

    def expose(self, event):
        if self.exposed == False and self.flagged == False:
            self['bg'] = 'gray90'
            self['relief'] = SUNKEN
            self.create_text(self.canvasWidth/2, self.canvasHeight/2, text='0', font=("Arial", 18))
            self.exposed = True

    def flag(self, event):
        if self.flagged == False and self.exposed == False:
            self.flagged = True
            self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='*', font=("Arial", 18))
        elif self.flagged:
            self.delete("all")
            self.flagged = False

class minesweeperGrid(Frame):
    def __init__(self, master, height, width, numBombs):
        Frame.__init__(self, master,bg='black')
        self.grid()
        self.cells = []
        for c in range(height):
            for r in range(width):
                cell = minesweeperCell(master, (r, c), numBombs)
                cell.grid(row=c, column=r)
                self.cells.append(cell)

        remBombsLabel = Label(text=str(numBombs), font=('Arial', 24))
        remBombsLabel.grid(row=height + 1, column=int(width / 2) - 2, columnspan=3)

def play_minesweeper(width, height, numBombs, master):
    msG = minesweeperGrid(master, height, width, numBombs)



root = Tk()
root.title('Minesweeper')
play_minesweeper(12, 10, 15, root)
mainloop()