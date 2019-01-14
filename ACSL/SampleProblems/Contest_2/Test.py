from clsCheckers import Checkers
from clsLocation import Location

def toLocationListString(list):
    s = ''
    for loc in list:
        s += str(loc) + ' '
    return s

#testing Checker.adjacentOpponents()
def testAdjacentOpponents():
    location = Location(3, 5)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    list = checker.adjacentOpponents()
    print('Checker at %s has adjacent opponents %s' % (location, toLocationListString(list)))

    location = Location(3, 5)
    opLocationList = [Location(5, 7), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    list = checker.adjacentOpponents()
    print('Checker at %s has adjacent opponents %s' % (location, toLocationListString(list)))

#testing Checker.isAdjacent()
def testIsAdjacent():
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    location = Location(3, 5)
    opLocation = Location(2, 6)
    checker = Checkers(location, opLocationList)
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

    location = Location(3, 5)
    opLocation = Location(4, 6)
    checker = Checkers(location, opLocationList)
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

    location = Location(3, 5)
    opLocation = Location(4, 4)
    checker = Checkers(location, opLocationList)
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 6)
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 4)
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

    location = Location(8, 5)
    opLocation = Location(2, 6)
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s adjacent to opponent %s, %s' % (location, opLocation, checker.isAdjacent(opLocation)))

#testing Checker.isOccupied(location)
def testIsOccupied():
    location = Location(2, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    print('Location at %s is occupied, %s' % (Location(4, 6), checker.isOccupied(Location(4, 6))))
    print('Location at %s is occupied, %s' % (Location(4, 8), checker.isOccupied(Location(4, 8))))

#testing Checker.attempt(opLocation)
def testAttempt():
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    location = Location(3, 5)
    opLocation = Location(4, 6)
    checker = Checkers(location, opLocationList)
    print('Checker at %s jumps over opponent at %s, new location, %s' % (location, opLocation, checker.attempt(opLocation)))

    location = Location(3, 5)
    opLocation = Location(4, 4)
    checker = Checkers(location, opLocationList)
    print('Checker at %s jumps over opponent at %s, new location, %s' % (location, opLocation, checker.attempt(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 6)
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s jumps over opponent at %s, new location, %s' % (location, opLocation, checker.attempt(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 4)
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s jumps over opponent at %s, new location, %s' % (location, opLocation, checker.attempt(opLocation)))

#testing Checker.canJump(opLocation)
def testCanJump():
    location = Location(3, 5)
    opLocation = Location(2, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

    location = Location(3, 5)
    opLocation = Location(4, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

    location = Location(3, 5)
    opLocation = Location(4, 4)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

    location = Location(8, 5)
    opLocation = Location(7, 4)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

    location = Location(8, 5)
    opLocation = Location(2, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.king = True
    print('Checker at %s can jump over opponent at %s, %s' % (location, opLocation, checker.canJump(opLocation)))

#testing Checker.jumpOne(opLocation)
def testJumpOne():
    location = Location(3, 5)
    opLocation = Location(4, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.jumpOne(opLocation)
    print('Checker at %s jumps over opponent at %s, new location %s' % (location, opLocation, checker.location))

    location = Location(3, 5)
    opLocation = Location(4, 4)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.jumpOne(opLocation)
    print('Checker at %s jumps over opponent at %s, new location %s' % (location, opLocation, checker.location))

    location = Location(8, 5)
    opLocation = Location(7, 6)
    opLocationList = [Location(2, 6), Location(4, 6), Location(7, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.king = True
    checker.jumpOne(opLocation)
    print('Checker at %s jumps over opponent at %s, new location %s' % (location, opLocation, checker.location))

    location = Location(8, 5)
    opLocation = Location(7, 4)
    opLocationList = [Location(7, 4), Location(4, 6), Location(6, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.king = True
    checker.jumpOne(opLocation)
    print('Checker at %s jumps over opponent at %s, new location %s' % (location, opLocation, checker.location))

#testing Checker.jump()
def testJump():
    location = Location(1, 5)
    opLocationList = [Location(2, 6), Location(4, 6), Location(6, 6)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(2, 2)
    opLocationList = [Location(3, 3), Location(5, 3), Location(7, 3), Location(7, 5)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(1, 7)
    opLocationList = [Location(2, 6), Location(4, 4)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(2, 2)
    opLocationList = [Location(3, 3), Location(5, 5), Location(7, 7)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(1, 5)
    opLocationList = [Location(2, 4), Location(2, 6), Location(3, 7), Location(3, 3)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(1, 3)
    opLocationList = [Location(2, 4), Location(3, 5), Location(2, 2), Location(4, 2), Location(5, 3)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))

    location = Location(2, 2)
    opLocationList = [Location(3, 3), Location(5, 5), Location(7, 7), Location(3, 1), Location(4, 2)]
    checker = Checkers(location, opLocationList)
    checker.jump()
    print('Checker at %s jumps, new location %s, jumps %d times, king status %s' % (location, checker.location, checker.jumps, checker.king))



testAdjacentOpponents()
testIsAdjacent()
testIsOccupied()
testAttempt()
testCanJump()
testJumpOne()
testJump()