from tkinter import *
from tkinter import messagebox
import random


class minesweeperCell(Canvas):
    def __init__(self, master, coord, grid, surroundingBombs=0, mine=False):
        self.canvasWidth = 50
        self.canvasHeight = 50
        Canvas.__init__(self, master, width=self.canvasWidth, height=self.canvasHeight, bg='white', bd=3, relief=RAISED)
        self.coord = coord
        self.surroundingBombs = surroundingBombs
        self.mine = mine
        self.blank = True
        self.flagged = False
        self.exposed = False
        self.exposedMine = False
        self.parent = grid
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-3>', self.flag)
        self.colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']

    def expose(self, event):
        if self.mine:
            self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='*', font=("Arial", 18))
            self.configure(background='red')
            if not self.exposedMine:
                messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
                for cell in self.parent.cells.values():
                    if cell.mine:
                        cell.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='*', font=("Arial", 18))
                        cell.configure(background='red')
        elif self.exposed == False and self.flagged == False:
            self['bg'] = 'gray90'
            self['relief'] = SUNKEN
            if self.surroundingBombs == 1:
                self.create_text(self.canvasWidth/2, self.canvasHeight/2, text='1', font=("Arial", 18), fill=self.colormap[1])
            elif self.surroundingBombs == 2:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='2', font=("Arial", 18), fill=self.colormap[2])
            elif self.surroundingBombs == 3:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='3', font=("Arial", 18), fill=self.colormap[3])
            elif self.surroundingBombs == 4:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='4', font=("Arial", 18), fill=self.colormap[4])
            elif self.surroundingBombs == 5:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='5', font=("Arial", 18), fill=self.colormap[5])
            elif self.surroundingBombs == 6:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='6', font=("Arial", 18), fill=self.colormap[6])
            elif self.surroundingBombs == 7:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='7', font=("Arial", 18), fill=self.colormap[7])
            elif self.surroundingBombs == 8:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='8', font=("Arial", 18), fill=self.colormap[8])
        self.exposed = True

    def flag(self, event):
        if self.flagged == False and self.exposed == False:
            self.flagged = True
            self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='*', font=("Arial", 18))
            self.parent.remBombs -= 1
            self.parent.remBombsLabel['text'] = self.parent.remBombs
            self.parent.remBombsLabel.grid(row=self.parent.height + 1, column=int(self.parent.width / 2) - 2, columnspan=3)
            for cell in self.parent.cells.values():
                if cell.flagged and cell.mine:
                    self.parent.flaggedMines.add(cell)
            if self.parent.isComplete():
                messagebox.showinfo('Minesweeper', 'Congratulations -- you won!', parent=self)
        elif self.flagged:
            self.delete("all")
            self.flagged = False
            self.parent.remBombs += 1
            self.parent.remBombsLabel['text'] = self.parent.remBombs
            self.parent.remBombsLabel.grid(row=self.parent.height + 1, column=int(self.parent.width / 2) - 2,columnspan=3)

class minesweeperGrid(Frame):

    def __init__(self, width, height, numBombs, master):
        Frame.__init__(self, master,bg='black')
        self.grid()
        self.cells = {}
        self.numBombs = numBombs
        self.remBombs = numBombs
        self.width = width
        self.height = height
        self.master = master
        self.lost = False
        self.flaggedMines = set(())
        self.setupCells()
        self.placeMines()
        for coord in self.cells:
            print(coord)
            self.cells[coord].surroundingBombs = self.checkSurroundings(coord)
        self.remBombsLabel = Label(text=str(self.remBombs), font=('Arial', 24))
        self.remBombsLabel.grid(row=height + 1, column=int(width / 2) - 2, columnspan=3)
        for cell in self.cells.values():
            if cell.exposedMine:
                self.lost = True
        if self.lost:
            for cell in self.cells.values():
                if cell.mine:
                    cell.create_text(cell.canvasWidth / 2, cell.canvasHeight / 2, text='*', font=("Arial", 18))
                    cell.configure(background='red')

    def setupCells(self):
        for c in range(self.height):
            for r in range(self.width):
                cell = minesweeperCell(self.master, (c, r), self)
                cell.grid(row=c, column=r)
                self.cells[(c, r)] = cell

    def placeMines(self):
        mines = random.sample(list(self.cells.values()), k=15)
        for mine in mines:
            mine.mine = True

    def checkSurroundings(self, coord):
        mines = 0
        surroundingCells = []
        topCell = self.getTop(coord)
        surroundingCells.append(topCell)
        topRightCell = self.getTopRight(coord)
        surroundingCells.append(topRightCell)
        rightCell = self.getRight(coord)
        surroundingCells.append(rightCell)
        bottomRightCell = self.getBottomRight(coord)
        surroundingCells.append(bottomRightCell)
        bottomCell = self.getBottom(coord)
        surroundingCells.append(bottomCell)
        bottomLeftCell = self.getBottomLeft(coord)
        surroundingCells.append(bottomLeftCell)
        leftCell = self.getLeft(coord)
        surroundingCells.append(leftCell)
        topLeftCell = self.getTopLeft(coord)
        surroundingCells.append(topLeftCell)
        for cell in surroundingCells:
            if cell is not None and cell.mine:
                mines += 1
        return mines

    def getTop(self, coord):
        if (coord[0], coord[1] - 1) in self.cells:
            return self.cells[(coord[0], coord[1] - 1)]
        else:
            return None

    def getTopRight(self, coord):
        if (coord[0] + 1, coord[1] - 1) in self.cells:
            return self.cells[(coord[0] + 1, coord[1] - 1)]
        else:
            return None

    def getRight(self, coord):
        if (coord[0]+1, coord[1]) in self.cells:
            return self.cells[(coord[0]+1, coord[1])]
        else:
            return None

    def getBottomRight(self, coord):
        if (coord[0]+1, coord[1]+1) in self.cells:
            return self.cells[(coord[0]+1, coord[1]+1)]
        else:
            return None

    def getBottom(self, coord):
        if (coord[0], coord[1]+1) in self.cells:
            return self.cells[(coord[0], coord[1]+1)]
        else:
            return None

    def getBottomLeft(self, coord):
        if (coord[0] - 1, coord[1]+1) in self.cells:
            return self.cells[(coord[0] - 1, coord[1]+1)]
        else:
            return None

    def getLeft(self, coord):
        if (coord[0] - 1, coord[1]) in self.cells:
            return self.cells[(coord[0] - 1, coord[1])]
        else:
            return None

    def getTopLeft(self, coord):
        if (coord[0] - 1, coord[1] - 1) in self.cells:
            return self.cells[(coord[0] - 1, coord[1] - 1)]
        else:
            return None
    def isComplete(self):
        allMines = len(self.flaggedMines) == self.numBombs
        if allMines == True:
            for mine in self.flaggedMines:
                allMines &= mine.mine
                if allMines == False:
                    break
        return allMines

def play_minesweeper(width, height, numBombs, master):
    msG = minesweeperGrid(width, height, numBombs, master)


root = Tk()
root.title('Minesweeper')
play_minesweeper(12, 10, 15, root)
mainloop()