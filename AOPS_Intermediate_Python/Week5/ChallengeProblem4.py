import random

class Domino:

    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def __str__(self):
        return str(self.numOne) + "-" + str(self.numTwo)

    def is_match(self, otherDom):
        if self.numOne == otherDom.numTwo or self.numTwo == otherDom.numOne:
            return True
        else:
            return False

class DomSet:

    def __init__(self):
        self.domSet = []
        for count in range(0, 7):
            for countTwo in range(0, 7):
                combo = Domino(count, countTwo)
                self.domSet.append(combo)
        random.shuffle(self.domSet)

    def reset_Set(self, chain):
        self.domSet = chain.chain
        random.shuffle(self.domSet)



class Chain:

    def __init__(self):
        self.chain = []

    def canAdd(self, domino):
        if domino.is_match(self.chain[0]) or domino.is_match(self.chain[len(self.chain) - 1]):
            return True
        else:
            return False

    def add(self, domino):
        if domino.is_match(self.chain[0]):
            self.chain = [domino] + self.chain
        elif domino.is_match(self.chain[len(self.chain) - 1]):
            self.chain.append(domino)

class Player:

    def __init__(self, name, set):
        self.name = name
        self.hand = [set.pop() for i in range(7)]

    def __str__(self):
        return str(self.name) + " has " + str(len(self.hand)) + " pieces."

    def get_hand(self):
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output



class Game:
    pass

