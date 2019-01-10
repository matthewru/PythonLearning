class Checkers:

    def __init__(self, location):
        self.location = location

    def jump(self, opLocation):
        if self.canJump(opLocation):
            if not self.isKing():
                if opLocation.column < self.location.column:
                    self.location.column = opLocation.column - 1
                    self.location.row = opLocation.row + 1
                elif opLocation.column > self.location.column:
                    self.location.column = opLocation.column + 1
                    self.location.row = opLocation.row + 1
            else:
                if opLocation.row < self.location.row:
                    self.location.row = opLocation.row - 1
                    if opLocation.column < self.location.column:
                        self.location.column = opLocation.column - 1
                    elif opLocation.column > self.location.column:
                        self.location.column = opLocation.column + 1
                elif opLocation.row > self.location.row:
                    self.location.row = opLocation.row + 1
                    if opLocation.column < self.location.column:
                        self.location.column = opLocation.column - 1
                    elif opLocation.column > self.location.column:
                        self.location.column = opLocation.column + 1
        else:
            return

    def isKing(self):
        return (self.location.row == 8)

    def canJump(self, opLocation):
        if self.isKing():
            return (opLocation.row == self.location.row + 1 or self.location.row - 1) and (opLocation.column == self.location.column + 1 or opLocation.column == self.location.column - 1) and (opLocation.row != 1 and opLocation.row != 8) and (opLocation.column != 1 and opLocation.column != 8)
        else:
            return (opLocation.row == self.location.row + 1) and (opLocation.column == self.location.column + 1 or opLocation.column == self.location.column - 1) and (opLocation.row != 1 and opLocation.row != 8) and (opLocation.column != 1 and opLocation.column != 8)



