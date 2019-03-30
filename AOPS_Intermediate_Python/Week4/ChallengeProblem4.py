# Python Class 1889
# Lesson 4 Problem 4
# Author: madmathninja (272729)

import random

class Die:
    '''Die class'''

    def __init__(self,sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sidesParam,int):
            sidesParam = range(1,sidesParam+1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return str(self.numSides)+'-sided die with '+str(self.top)+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def flip(self):
        topPosition = self.sides.index(self.top)
        self.sides.reverse()
        self.top = self.sides[topPosition]
        self.sides.reverse()

def mostFrequentNumInList(list):
    counter = 0
    num = list[0]

    for i in list:
        if i != 'W':
            curr_frequency = list.count(i)
            if (curr_frequency > counter):
                counter = curr_frequency
                num = i
    return num

def strRolls(list):
    ans = ''
    for num in list:
        if ans == '':
            ans += str(num) + ' '
        else:
            ans += str(num) + ' '
    return ans

def europadice():
    rolls = []
    for roll in range(1, 11):
        ed = Die([1,2,3,4,'W'])
        ed.roll()
        rolls.append(ed.top)
    numberGoal = mostFrequentNumInList(rolls)
    print(strRolls(rolls))
    print("We're going for all %ds" % (numberGoal))
    for reroll in range(1, 4):
        input("Reroll #%d. Press enter to reroll." % reroll)
        for num in rolls:
            if num != 'W' and num != numberGoal:
                ed = Die([1,2,3,4,'W'])
                ed.roll()
                numIndex = rolls.index(num)
                rolls[numIndex] = ed.top
        print(strRolls(rolls))
        if all(elem == numberGoal or elem =='W' for elem in rolls):
            break
    if all(elem == numberGoal or elem == 'W' for elem in rolls):
        print("Yay, you win!")
    else:
        numOfSameNumbers = rolls.count(numberGoal) + rolls.count('W')
        print("Sorry, you only got %d" % numOfSameNumbers)

#test cases
europadice()
