# Python Class 1889
# Lesson 4 Problem 5
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


class Player():
    def __init__(self, name, score = 0, rerolls = 5):
        self.name = name
        self.score = score
        self.rerolls = rerolls

    def take_turn(self):
        d1 = Die([1, 2, 3, 4, 5, -6])
        d2 = Die([1, 2, 3, 4, 5, -6])

        while True:
            input("Press enter to roll.")
            d1.roll()
            d2.roll()
            roundscore = d1.get_top() + d2.get_top()
            print(str(self.name) + " rolled " + str(d1.get_top()) + " and " + \
                  str(d2.get_top()) + " for a total of " + str(roundscore))
            # if the player has no rerolls, they're stuck with this
            if self.rerolls == 0:
                print("%s is out of rerolls so %s has to keep this." % (self.name, self.name))
                break
            # see if they want to reroll
            response = 'x'
            while response == None or response.lower() not in 'yn':
                answer = input("Do you want to reroll (y/n)? ")
                response = 'x' if answer == '' else answer
            if response.lower() == 'n':
                break  # keeping this roll, move on the the next roll
            # they're using a reroll
            self.rerolls -= 1
            print("OK, " + str(self.name) + " has " + str(self.rerolls) + " rerolls left.")

        self.score += roundscore  # update the score

    def __str__(self):
        return str(self.name) + ' has ' + \
               str(self.score) + ' points and ' + \
               str(self.rerolls) + ' rerolls left.'


def print_scores(playerList):
    for player in playerList:
        print(player)

def decathlon_400_meters():
    '''decathlon_400_meters()
    plays a multi-player version of Reiner Knizia's 400 Meters'''
    numPlayers = int(input('Enter number of players: '))
    playerList = []
    for i in range(numPlayers):
        name = ''
        while name == '' or name in playerList:
            name = input('Player ' + str(i + 1) + ', enter your name: ')
        playerList.append(Player(name))
    # play the game
    for turn in range(1,5):
        print("Round " + str(turn))
        for i in range(numPlayers):
            print_scores(playerList)
            print("%s, it is your turn" % playerList[i].name)
            playerList[i].take_turn()
    print_scores(playerList)
    winning_score = 0
    winner = []
    for player in playerList:
        if player.score > winning_score:
            winning_score = player.score
            winner.append(player.name)
    if len(winner) == 1:
        print("%s has won the game!" % winner[0])
        winner = []

#test
decathlon_400_meters()