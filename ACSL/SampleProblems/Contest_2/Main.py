from clsLocation import Location
from clsCheckers import Checkers

turn = input("What is your move? ")
turnList = turn.split(", ")

currentRow = int(turnList[0])
currentColumn = int(turnList[1])
opponentNumber = int(turnList[2])

checker = Checkers((Location(currentRow, currentColumn)))

for count in range(3, ((opponentNumber * 2) + 3), 2):
    row = int(turnList[count])
    column = int(turnList[count+1])
    checker.addOpponentLocation(Location(row, column))

checker.jump()
print('%d%s' % (checker.jumps, ", KING" if checker.king else ""))





