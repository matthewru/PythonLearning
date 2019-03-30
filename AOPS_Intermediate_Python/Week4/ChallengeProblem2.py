# Python Class 1889
# Lesson 4 Problem 2
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

#test cases
d = Die(8)
print(d.get_top())
d.flip()
print(d)