from clsLocation import Location
class Checkers:

    def __init__(self, location, opLocationList = [], king = False, jumps = 0):
        self.location = location
        self.opLocationList = opLocationList
        self.king = king
        self.jumps = jumps

    def jump(self, opLocation):
        if self.canJump(opLocation):
            self.location = self.attempt(opLocation)
            self.capture(opLocation)


    def jump(self):
        adjacentLocations = self.adjacentLocations()
        opLocation = adjacentLocations[0]
        while self.canJump(opLocation):
            self.jump(opLocation)
            adjacentLocations = self.adjacentLocations()
            opLocation = adjacentLocations[0]
            self.jumps += 1
            if self.location.row == 8:
                self.king = True

    def isOccupied(self, location):
        for loc in self.opLocationList:
            if (loc.row == location.row) and (loc.column == location.column):
                return True
        return False

    def canJump(self, opLocation):
        canJump = self.isAdjacent(opLocation)
        canJump &= (opLocation.row != 1 and opLocation.row != 8)
        canJump &= (opLocation.column != 1 and opLocation.column != 8)
        canJump &= self.isOccupied(self.attempt(opLocation))
        return canJump

    def addOpponentLocation(self, opLocation):
        self.opLocationList.append(opLocation)

    def isAdjacent(self, opLocation):
        if self.king:
            adjacent = (opLocation.row == self.location.row - 1)
            adjacent &= (opLocation.column == self.location.column + 1 or opLocation.column == self.location.column - 1)
        else:
            adjacent = (opLocation.row == self.location.row + 1)
            adjacent &= (opLocation.column == self.location.column + 1 or opLocation.column == self.location.column - 1)
        return adjacent

    def attempt(self, opLocation):
        newLocation = Location()
        if self.king:
            if opLocation.row < self.location.row:
                newLocation.row = opLocation.row - 1
                if opLocation.column < self.location.column:
                    newLocation.column = opLocation.column - 1
                elif opLocation.column > self.location.column:
                    newLocation.column = opLocation.column + 1
            elif opLocation.row > self.location.row:
                newLocation.row = opLocation.row + 1
                if opLocation.column < self.location.column:
                    newLocation.column = opLocation.column - 1
                elif opLocation.column > self.location.column:
                    newLocation.column = opLocation.column + 1
        else:
            if opLocation.column < self.location.column:
                newLocation.column = opLocation.column - 1
                newLocation.row = opLocation.row + 1
            elif opLocation.column > self.location.column:
                newLocation.column = opLocation.column + 1
                newLocation.row = opLocation.row + 1
        return newLocation

    def adjacentOpponent(self):
        adjacentLocations = []
        for loc in self.opLocationList:
            if self.isAdjacent(loc):
                adjacentLocations.append(loc)
        return adjacentLocations

    def capture(self, opLocation):
        self.opLocationList.remove(opLocation)




