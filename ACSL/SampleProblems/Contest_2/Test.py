from clsCheckers import Checkers
from clsLocation import Location

#testing Checker.isKing()
location = Location(8, 1)
checker = Checkers(location)
print('Checker at location(%d, %d) is king %s' % (location.row, location.column, checker.isKing()))

location = Location(6, 4)
checker = Checkers(location)
print('Checker at location(%d, %d) is king %s' % (location.row, location.column, checker.isKing()))

#testing Checker.canJump(opLocation)
location = Location(2, 2)
checker = Checkers(location)
opLocation = Location(3,3)
print('Checker at location(%d, %d) can jump over opponent location(%d, %d) %s' % (location.row, location.column, opLocation.row, opLocation.column, checker.canJump(opLocation)))

location = Location(2, 2)
checker = Checkers(location)
opLocation = Location(3,6)
print('Checker at location(%d, %d) can jump over opponent location(%d, %d) %s' % (location.row, location.column, opLocation.row, opLocation.column, checker.canJump(opLocation)))

location = Location(7, 7)
checker = Checkers(location)
opLocation = Location(8, 6)
print('Checker at location(%d, %d) can jump over opponent location(%d, %d) %s' % (location.row, location.column, opLocation.row, opLocation.column, checker.canJump(opLocation)))

location = Location(7, 7)
checker = Checkers(location)
opLocation = Location(8, 8)
print('Checker at location(%d, %d) can jump over opponent location(%d, %d) %s' % (location.row, location.column, opLocation.row, opLocation.column, checker.canJump(opLocation)))

#testing Checker.jump(opLocation)
location = Location(2, 2)
checker = Checkers(location)
opLocation = Location(3, 3)
print('Checker at location(%d, %d) jumps over opponent location(%d, %d)' % (location.row, location.column, opLocation.row, opLocation.column))
checker.jump(opLocation)
print('New location(%d, %d)' % (checker.location.row, checker.location.column))

location = Location(1, 3)
checker = Checkers(location)
opLocation = Location(2, 2)
print('Checker at location(%d, %d) jumps over opponent location(%d, %d)' % (location.row, location.column, opLocation.row, opLocation.column))
checker.jump(opLocation)
print('New location(%d, %d)' % (checker.location.row, checker.location.column))

location = Location(8, 3)
checker = Checkers(location)
opLocation = Location(7, 2)
print('Checker at location(%d, %d) jumps over opponent location(%d, %d)' % (location.row, location.column, opLocation.row, opLocation.column))
checker.jump(opLocation)
print('New location(%d, %d)' % (checker.location.row, checker.location.column))

location = Location(8, 3)
checker = Checkers(location)
opLocation = Location(7, 4)
print('Checker at location(%d, %d) jumps over opponent location(%d, %d)' % (location.row, location.column, opLocation.row, opLocation.column))
checker.jump(opLocation)
print('New location(%d, %d)' % (checker.location.row, checker.location.column))