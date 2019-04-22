# Python Class 1889
# Lesson 6 Problem 5
# Author: madmathninja (272729)

import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''
    def __init__(self, color, sides):
        Die.__init__(self, sides)
        self.color = color

    def get_color(self):
        return self.color

class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__(self, name):
        self.pile = []
        for i in range(6):
            self.pile.append(DinoDie("green", ["dino", "dino", "dino", "leaf", "leaf", "foot"]))
        for i in range(4):
            self.pile.append(DinoDie("yellow", ["dino", "dino", "leaf", "leaf", "foot", "foot"]))
        for i in range(3):
            self.pile.append(DinoDie("red", ["dino", "leaf", "leaf", "foot", "foot", "foot"]))
        self.score = 0
        self.name = name

    def __str__(self):
        return self.name + " has " + str(self.score) + " points."

    def get_name(self):
        return self.name

    def get_num_die(self, color):
        die_color = 0
        for die in self.pile:
            if die.color == color:
                die_color += 1
        return die_color

    def take_turn(self):
        print('\n' + self.name + ", it's your turn!")
        print("You have %d dice remaining" % len(self.pile))
        print("%d green, %d yellow, %d red" % (
        self.get_num_die('green'), self.get_num_die('yellow'), self.get_num_die('red')))
        dinos = 0
        feet = 0
        while True:
            input("Press enter to select dice and roll.")
            for count in range(3):
                if len(self.pile) == 0:
                    break
                die = random.sample(self.pile, 1).pop()
                die.roll()
                print("\tA %s Dino die with a %s on top." % (die.get_color(), die.get_top()))
                if die.top == "dino":
                    dinos += 1
                    self.pile.remove(die)
                elif die.top == "foot":
                    feet += 1
                    self.pile.remove(die)
            if feet >= 3:
                print("Too bad -- you got stomped!\n")
                self.score = 0
                break
            print("This turn so far: %d dinos and %d feet" % (dinos, feet))
            print("You have %d dice remaining" % len(self.pile))
            print("%d green, %d yellow, %d red" % (self.get_num_die('green'), self.get_num_die('yellow'), self.get_num_die('red')))
            response = 'x'
            while response == None or response.lower() not in 'yn':
                answer = input("Do you want to roll again (y/n)? ")
                response = 'x' if answer == '' else answer
            if response.lower() == 'n':
                self.score += dinos
                print("\n\n")
                break


def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    players = []
    for count in range(numPlayers):
        playerName = input('Player '+str(count+1)+', enter your name: ')
        player = DinoPlayer(playerName)
        players.append(player)
    for round in range(numRounds):
        print("\nROUND " + str(round+1) + "\n\n\n")
        for player in players:
            for p in players:
                print(p)
            player.take_turn()
    PlayerandScore = {}
    for player in players:
        PlayerandScore[player] = player.score
    winner = max(PlayerandScore.keys(), key=(lambda k: PlayerandScore[k]))
    print("We have a winner!")
    print(winner)


play_dino_hunt(2, 2)
