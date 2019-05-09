from tkinter import *
import random


class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['red', 'black', 'red', 'black', 'red', 'black']):
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

    def change_color(self, color):
        self.config(bg=color)


### you should cut-and-paste this code from this week's lesson


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self, master, valueList=[1, 2, 3, 4, 5, 6], colorList=['black'] * 6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        super(GUIFreezeableDie, self).__init__(master)
        self.isFrozen = False

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.isFrozen

    def freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        if self.isFrozen == False:
            self.isFrozen = True
            self.change_color("gray")

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if self.isFrozen == False:
            self.top = random.randrange(1, 7)
            self.draw()


class DiscusFrame(Frame):
    '''a small application to test the freezeable die'''
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.dice = []
        self.attempt = 0
        self.score = 0
        self.highScore = 0
        self.attempt_scoreLabel = Label(self, text="Attempt #" + str(self.attempt) + " Score: " + str(self.score))
        self.attempt_scoreLabel.grid(row=1, column=3)
        self.highScoreLabel = Label(self, text="High Score: " + str(self.highScore))
        self.highScoreLabel.grid(row=1, column=6)
        for die in range(5):
            self.die = GUIFreezeableDie(self)
            self.dice.append(self.die)
        for n in range(len(self.dice)):
            self.dice[n].grid(row=2, column=n)
        self.rollButton = Button(self, text='Roll', command=self.roll).grid(row=2,column=6)
        self.freezeButtons = {}
        for n in range(5):
            freezeButton = Button(self, text='Freeze', command=self.dice[n].freeze)
            self.freezeButtons[self.dice[n]] = freezeButton
            self.freezeButtons[self.dice[n]]['state'] = DISABLED
            self.freezeButtons[self.dice[n]].grid(row=3, column=n)

    def roll(self):
        rollValue = []
        oddCount = 0
        for n in range(len(self.dice)):
            if self.dice[n].isFrozen:
                self.freezeButtons[self.dice[n]]['state'] = DISABLED
        for n in range(len(self.dice)):
            self.dice[n].roll()
            rollValue.append(self.dice[n].get_top())
        for n in range(len(self.dice)):
            if self.dice[n].get_top() == 1 or self.dice[n].get_top() == 3 or self.dice[n].get_top() == 5:
                self.freezeButtons[self.dice[n]]['state'] = DISABLED
            else:
                self.freezeButtons[self.dice[n]]['state'] = ACTIVE
        for value in rollValue:
            if value == 1 or value == 3 or value == 5:
                oddCount += 1
                if oddCount == 5:
                    self.attempt_scoreLabel['text'] = "FOULED ATTEMPT"
                    self.attempt_scoreLabel.grid(row=1, column=3)



# test application
root = Tk()
test = DiscusFrame(root)
root.mainloop()