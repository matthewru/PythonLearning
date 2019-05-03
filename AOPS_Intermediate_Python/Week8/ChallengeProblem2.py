from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)

class ShotPutFrame(Frame):
    '''frame for a game of 400 Meters'''

    def __init__(self,master,name):
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # initialize game data
        self.score = 0
        self.attemptScores = []
        self.attempt = 1
        self.highScore = 0
        self.attemptround = 0
        self.attempt_scoreLabel = Label(self, text="Attempt #" + str(self.attempt) + " Score: " + str(self.score), font=('Arial', 18))
        self.attempt_scoreLabel.grid(row=0, column=3, columnspan=2)
        self.highScoreLabel = Label(self, text="High Score: " + str(self.highScore), font=('Arial', 18))
        self.highScoreLabel.grid(row=0, column=6, columnspan=2)
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,columnspan=1)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=3,columnspan=1)
        self.stopButton['state'] = DISABLED

    def roll(self):
        '''Decath400MFrame.roll()
        handler method for the roll button click'''
        self.attempt_scoreLabel['text'] = "Attempt #" + str(self.attempt) + " Score: " + str(self.score)
        self.highScoreLabel['text'] = "High Score: " + str(self.highScore)
        self.dice[self.attemptround].roll()
        if self.dice[self.attemptround].get_top() != 1:
            self.score += self.dice[self.attemptround].get_top()
            self.attempt_scoreLabel['text'] = "Attempt #" + str(self.attempt) + " Score: " + str(self.score)
            self.attemptround += 1
            if self.attemptround < 8:
                self.rollButton.grid(row=2, column=1 * self.attemptround, columnspan=1)
                self.stopButton.grid(row=3, column=1 * self.attemptround, columnspan=1)
                self.rollButton['state'] = ACTIVE
                self.stopButton['state'] = ACTIVE
            else:
                self.attemptround = 0
                self.rollButton.grid(row=2, column=1 * self.attemptround, columnspan=1)
                self.stopButton.grid(row=3, column=1 * self.attemptround, columnspan=1)
                self.rollButton['state'] = ACTIVE
                self.stopButton['state'] = DISABLED
                if self.attempt < 3:
                    self.attempt += 1
                    self.attemptScores.append(self.score)
                    self.score = 0
                    self.highScore = max(self.attemptScores)
                    for die in self.dice:
                        die.erase()
                else:
                    self.attemptScores.append(self.score)
                    self.score = 0
                    self.highScore = max(self.attemptScores)
                    self.rollButton.grid_remove()
                    self.stopButton.grid_remove()
                self.attempt_scoreLabel['text'] = "Attempt #" + str(self.attempt) + " Score: " + str(self.score)
                self.highScoreLabel['text'] = "High Score: " + str(self.highScore)
        else:
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = 'FOUL'
            self.stopButton['state'] = ACTIVE
            self.score = 0
            self.attempt_scoreLabel['text'] = 'FOULED ATTEMPT'

    def stop(self):
        '''Decath400MFrame.keep()
        handler method for the keep button click'''
        # add dice to score and update the scoreboard
        self.stopButton['text'] = "Stop"
        if self.attempt < 3:
            self.attempt += 1
            self.attemptScores.append(self.score)
            self.score = 0
            self.highScore = max(self.attemptScores)
            self.attemptround = 0
            self.rollButton.grid(row=2, column=1 * self.attemptround, columnspan=1)
            self.stopButton.grid(row=3, column=1 * self.attemptround, columnspan=1)
            self.rollButton['state'] = ACTIVE
            self.stopButton['state'] = DISABLED
            self.attempt_scoreLabel['text'] = "Attempt #" + str(self.attempt) + " Score: " + str(self.score)
            for die in self.dice:
                die.erase()
        else:
            self.attemptScores.append(self.score)
            self.score = 0
            self.highScore = max(self.attemptScores)
            self.rollButton.grid_remove()
            self.stopButton.grid_remove()
            self.attempt_scoreLabel['text'] = "Game Over"
        self.highScoreLabel['text'] = "High Score: " + str(self.highScore)



# play the game
name = input("Enter your name: ")
root = Tk()
root.title('Shot Put')
game = ShotPutFrame(root,name)
game.mainloop()