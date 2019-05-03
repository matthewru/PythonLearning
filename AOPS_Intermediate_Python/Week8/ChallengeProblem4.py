from tkinter import *
import random


class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self, master, width=60, height=60, bg='white', \
                        bd=5, relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top - 1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1, 7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1, 1)],
                   [(0, 0), (2, 2)],
                   [(0, 0), (1, 1), (2, 2)],
                   [(0, 0), (0, 2), (2, 0), (2, 2)],
                   [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
                   [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]]
        for location in pipList[self.top - 1]:
            self.draw_pip(location, self.colorList[self.top - 1])

    def draw_pip(self, location, color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx, centery) = (17 + 20 * location[1], 17 + 20 * location[0])  # center
        self.create_oval(centerx - 5, centery - 5, centerx + 5, centery + 5, fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class hurdles110meters(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.grid()
        self.dice = []
        self.rethrows = 6
        self.score = 0
        self.name = name
        self.rethrowsLabel = Label(self, text="Rethrows: " + str(self.rethrows-1))
        self.rethrowsLabel.grid(row=1, column=3)
        self.scoreLabel = Label(self, text="Score: " + str(self.score))
        self.scoreLabel.grid(row=1, column=6)
        self.nameLabel = Label(self, text=self.name)
        self.nameLabel.grid(row=1,column=0)
        for die in range(5):
            self.die = GUIDie(self)
            self.dice.append(self.die)
        for n in range(len(self.dice)):
            self.dice[n].grid(row=2, column=n)
        self.throwButton = Button(self, text='Throw', command=self.roll)
        self.throwButton.grid(row=2,column=6)
        self.stopButton = Button(self, text='Stop', command=self.stop)
        self.stopButton.grid(row=3,column=6)

    def update_Label(self):
        self.scoreLabel['text'] = "Score: " + str(self.score)
        self.rethrowsLabel['text'] = "Rethrows: " + str(self.rethrows-1)

    def roll(self):
        self.score = 0
        for n in range(len(self.dice)):
            self.dice[n].roll()
            self.score += self.dice[n].get_top()
            self.update_Label()
        self.rethrows -= 1
        if self.rethrows < 6 and self.rethrows > 0:
            self.throwButton['text'] = 'Rethrow'
        elif self.rethrows == 0:
            self.throwButton['state'] = DISABLED
            self.stopButton['text'] = 'Game Over'

    def stop(self):
        self.nameLabel.grid_remove()
        self.throwButton.grid_remove()
        self.scoreLabel.grid_remove()
        self.rethrowsLabel.grid_remove()
        self.stopButton.grid_remove()
        for die in self.dice:
            die.grid_remove()
        self.gameOver = Label(self, text='Game Over, you had ' + str(self.score) + ' points! and ' + str(self.rethrows) + ' rethrows!')
        self.gameOver.grid(row=2, column=2)


name = input("What's your name: ")
root = Tk()
test = hurdles110meters(root, name)
root.mainloop()