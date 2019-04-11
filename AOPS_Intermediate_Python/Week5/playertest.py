from ChallengeProblem3 import UnoPlayer
from ChallengeProblem3 import UnoDeck
from ChallengeProblem3 import UnoPile


uDeck = UnoDeck()
uPile = UnoPile(uDeck)
uPlayer = UnoPlayer("A", uDeck, True)
uPlayer.take_turn(uDeck, uPile)
