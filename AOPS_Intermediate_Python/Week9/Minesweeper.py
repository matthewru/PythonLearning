from tkinter import *
import random


class minesweeperCell(Canvas):
    def __init__(self, master, coord, remBombs, surroundingBombs=0, mine=False):
        self.canvasWidth=50
        self.canvasHeight=50
        Canvas.__init__(self, master, width=self.canvasWidth, height=self.canvasHeight, bg='white', bd=3, relief=RAISED)
        self.coord = coord
        self.surroundingBombs = surroundingBombs
        self.mine = mine
        self.blank = True
        self.flagged = False
        self.exposed = False
        self.bind('<Button-1>',self.expose)
        self.bind('<Button-3>', self.flag)
        self.colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']



    def expose(self, event):
        if self.exposed == False and self.flagged == False:
            self['bg'] = 'gray90'
            self['relief'] = SUNKEN
            if self.mine:
                self.create_text(self.canvasWidth / 2, self.canvasHeight / 2, text='*', font=("Arial", 18))
            else:
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
        elif self.flagged:
            self.delete("all")
            self.flagged = False

class minesweeperGrid(Frame):
    #setupCells
    #placeMines
    #identifyNumbers
    #checkSurroundings
    #getTop
    #getTopRight
    #getRight
    #getBottomRight
    #getBottom
    #getBottomLeft
    #getLeft
    #getTopLeft


    def __init__(self, width, height, numBombs, master):
        Frame.__init__(self, master,bg='black')
        self.grid()
        self.cells = {}
        self.numBombs = numBombs
        self.width = width
        self.height = height
        self.master = master
        self.setupCells()
        self.placeMines()
        for coord in self.cells:
            print(coord)
            self.cells[coord].surroundingBombs = self.checkSurroundings(coord)
        remBombsLabel = Label(text=str(numBombs), font=('Arial', 24))
        remBombsLabel.grid(row=height + 1, column=int(width / 2) - 2, columnspan=3)

    def setupCells(self):
        for c in range(self.height+1):
            for r in range(self.width+1):
                cell = minesweeperCell(self.master, (c, r), self.numBombs)
                cell.grid(row=c, column=r)
                self.cells[(c, r)] = cell

    def placeMines(self):
        for m in range(self.numBombs + 1):
            random.choice(list(self.cells.values())).mine = True

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

def play_minesweeper(width, height, numBombs, master):
    msG = minesweeperGrid(width, height, numBombs, master)



root = Tk()
root.title('Minesweeper')
play_minesweeper(12, 10, 15, root)
mainloop()