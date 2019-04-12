import random

class Domino:

    def __init__(self, numOne, numTwo):
        self.numOne = numOne
        self.numTwo = numTwo

    def __str__(self):
        return str(self.numOne if self.numOne <= self.numTwo else self.numTwo) + \
               "-" + \
               str(self.numTwo if self.numTwo > self.numOne else self.numOne)

    def __eq__(self, otherDom):
        return self.numOne == otherDom.numOne and self.numTwo == otherDom.numTwo

    def is_match(self, otherDom):
        if (self.numOne == otherDom.numOne) or (self.numOne == otherDom.numTwo) or (self.numTwo == otherDom.numOne) or (self.numTwo == otherDom.numTwo):
            return True
        else:
            return False

class DomSet:

    def __init__(self):
        self.domSet = []
        for count in range(0, 7):
            for countTwo in range(0, 7):
                combo = Domino(count if count <= countTwo else countTwo, countTwo if countTwo > count else count)
                if combo not in self.domSet:
                    self.domSet.append(combo)
        random.shuffle(self.domSet)

class Chain:

    def __init__(self):
        self.nums = []

    def __str__(self):
        s = ''
        for i in range(len(self.nums)):
            s += str(self.nums[i])
            if i % 2 == 0:
                s += '-'
            else:
                if i < len(self.nums)-1:
                    s += ', '
        return s

    def canAdd(self, domino):
        if len(self.nums) == 0:
            return True
        else:
            first = self.nums[0]
            last = self.nums[len(self.nums) - 1]
            if first == domino.numOne or \
                first == domino.numTwo or \
                last == domino.numOne or \
                last == domino.numTwo:
                return True
            else:
                return False

    def add(self, domino):
        if len(self.nums) == 0:
            self.nums.append(domino.numOne)
            self.nums.append(domino.numTwo)
        else:
            first = self.nums[0]
            last = self.nums[len(self.nums) - 1]
            if first == domino.numOne:
                self.nums = [domino.numTwo, domino.numOne] + self.nums
                return
            elif first == domino.numTwo:
                self.nums = [domino.numOne, domino.numTwo] + self.nums
                return
            elif last == domino.numOne:
                self.nums.append(domino.numOne)
                self.nums.append(domino.numTwo)
                return
            elif last == domino.numTwo:
                self.nums.append(domino.numTwo)
                self.nums.append(domino.numOne)
                return

class Player:

    def __init__(self, name, set, isComputer=True):
        self.name = name
        self.hand = [set.domSet.pop() for i in range(7)]
        self.isComputer = isComputer


    def __str__(self):
        return str(self.name) + " has " + str(len(self.hand)) + " pieces."

    def get_hand(self):
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def is_empty(self):
        return len(self.hand) == 0

    def play_domino(self,domino,chain):
        if chain.canAdd(domino):
            chain.add(domino)
            self.hand.remove(domino)

    def get_name(self):
        return self.name

    def take_turn(self, set, chain):
        print(self.name + ", it's your turn.")
        print(chain)
        matches = [domino for domino in self.hand if chain.canAdd(domino)]
        if len(matches) > 0:
            # get player's choice of which domino to play
            if self.isComputer == False:
                print("Your hand: ")
                print(self.get_hand())
                for index in range(len(matches)):
                    # print the playable domino with their number
                    print(str(index + 1) + ": " + str(matches[index]))
                choice = 0
                while choice < 1 or choice > len(matches):
                    choicestr = input("Which do you want to play? ")
                    if choicestr.isdigit():
                        choice = int(choicestr)
                # play the chosen domino from hand, add it to the chain
                self.play_domino(matches[choice - 1], chain)
            else:
                # play the chosen domino from hand, add it to the chain
                self.play_domino(random.sample(matches,1).pop(), chain)
        else:  # can't play
            print("You can't play, so you have to pass.")
            if self.isComputer == False:
                input("Press enter to pass.")

    def find66Domino(self):
        for domino in self.hand:
            if domino.numOne == 6 and domino.numTwo == 6:
                return domino
        return None

    def can_play(self, chain):
        for dom in self.hand:
            if chain.canAdd(dom):
                return True
        return False

class Game:

    def __init__(self, numPlayers=4):
        self.numPlayers = numPlayers
        self.players = []
        self.set = DomSet()
        self.chain = Chain()
        self.currentPlayer = None
        self.previousPlayer = None

    def printStatus(self):
        # print the game status
        print('-------')
        for player in self.players:
            print(player)
        print('-------')

    def getPlayers(self):
        name = input('Player, enter your name: ')
        self.players.append(Player(name, self.set, False))
        COMPNAMES = ["Tom", "Bob", "Robert", "John", "Jimmy", "Katie", "Kate", "Melissa", "Mary", "Amy"]
        for name in random.sample(COMPNAMES, self.numPlayers-1):
            self.players.append(Player(name, self.set, True))

    def nextPlayer(self):
        if self.players.index(self.currentPlayer) == len(self.players)-1:
            self.currentPlayer = self.players[0]
        else:
            self.currentPlayer = self.players[self.players.index(self.currentPlayer) + 1]

    def checkWinner(self):
        for player in self.players:
            if player.is_empty():
                return player
        if self.isFinished():
            return self.previousPlayer
        else:
            return None

    def isFinished(self):
        canPlay = True
        for player in self.players:
            canPlay = canPlay and player.can_play(self.chain)
        return not canPlay

    def play_Dominoes(self):
        self.getPlayers()
        for player in self.players:
            domino = player.find66Domino()
            if domino is not None:
                self.currentPlayer = player
                self.currentPlayer.play_domino(domino, self.chain)
                self.previousPlayer = self.currentPlayer
                break

        # play the game
        while True:
            self.nextPlayer()
            self.printStatus()
            # take a turn
            self.currentPlayer.take_turn(self.set, self.chain)
            input("Press enter to continue.")
            self.previousPlayer = self.currentPlayer
            if self.checkWinner() is not None:
                print(self.currentPlayer.get_name() + " wins!")
                print("Thanks for playing!")
                break

numPlayers = int(input("How many players? "))
u = Game(numPlayers)
u.play_Dominoes()