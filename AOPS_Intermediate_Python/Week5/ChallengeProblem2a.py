import random

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9
      color: string'''

    def __init__(self,rank,color):
        '''UnoCard(rank,color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        return(str(self.color)+' '+str(self.rank))

    def is_match(self,other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        if (self.color == other.color) or (self.rank == other.rank):
            return True
        elif self.rank == "Wild":
            return True
        else:
            return False

class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0,color))  # one 0 of each color
            for i in range(2):
                for n in range(1,10):  # two of each of 1-9 of each color
                    self.deck.append(UnoCard(n,color))
            for i in range(2):
                self.deck.append(UnoCard("Skip", color))
                self.deck.append(UnoCard("Reverse", color))
                self.deck.append(UnoCard("Draw Two", color))
            self.deck.append(UnoCard("Wild", ""))
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck))+' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self,pile):
        '''UnoDeck.reset_deck(pile)
        resets the deck from the pile'''
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self,deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has '+str(self.pile[-1])+' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self,card):
        '''UnoPile.add_card(card)
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self,name,deck):
        '''UnoPlayer(name,deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name)+' has '+str(len(self.hand))+' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self,deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self,card,pile):
        '''UnoPlayer.play_card(card,pile)
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)

    def take_turn(self,deck,pile):
        '''UnoPlayer.take_turn(deck,pile)
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        # print player info
        print(self.name+", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.is_match(topcard)]
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
                # print the playable cards with their number
                print(str(index+1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            self.play_card(matches[choice-1],pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            print("You drew: "+str(newcard))
            if newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")
            input("Press enter to continue.")

class UnoGame:
    def __init__(self, numPlayers=2):
        self.numPlayers = numPlayers
        self.players = []
        self.deck = UnoDeck()
        self.pile = UnoPile(self.deck)
        self.reverse = False
        self.skip = False
        self.drawTwo = False
        self.currentPlayer = ''

    def printStatus(self):
        # print the game status
        print('-------')
        for player in self.players:
            print(player)
        print('-------')

    def getPlayers(self):
        for n in range(self.numPlayers):
            # get each player's name, then create an UnoPlayer
            name = input('Player #' + str(n + 1) + ', enter your name: ')
            self.players.append(UnoPlayer(name, self.deck))

    def nextPlayer(self):
        if self.reverse == False:
            if self.players.index(self.currentPlayer) == len(self.players)-1:
                self.currentPlayer = self.players[0]
            else:
                self.currentPlayer = self.players[self.players.index(self.currentPlayer) + 1]
        else:
            if self.players.index(self.currentPlayer) == 0:
                self.currentPlayer = self.players[len(self.players)-1]
            else:
                self.currentPlayer = self.players[self.players.index(self.currentPlayer) - 1]

    def actionCard(self, card):
        if card.rank == "Skip":
            self.skip = True
        elif card.rank == "Reverse":
            self.reverse = not self.reverse
        elif card.rank == "Draw Two":
            self.drawTwo = True
            self.skip = True

    def play_uno(self):
        self.getPlayers()
        # randomly assign who goes first
        self.currentPlayer = self.players[random.randrange(self.numPlayers-1)]
        # play the game
        while True:
            self.printStatus()
            # take a turn
            self.currentPlayer.take_turn(self.deck, self.pile)
            self.actionCard(self.pile.top_card())
            if self.pile.top_card().rank == "Wild":
                color = input("What color would you like it to be?")
                self.pile.top_card().color = color
            # check for a winner
            if self.currentPlayer.has_won():
                print(self.currentPlayer.get_name() + " wins!")
                print("Thanks for playing!")
                break
                # go to the next player
            self.nextPlayer()
            if self.drawTwo == True:
                self.currentPlayer.draw_card(self.deck)
                self.currentPlayer.draw_card(self.deck)
                self.drawTwo == False
            if self.skip == True:
                self.nextPlayer()
                self.skip = False

numPlayers = int(input("How many players? "))
u = UnoGame(numPlayers)
u.play_uno()