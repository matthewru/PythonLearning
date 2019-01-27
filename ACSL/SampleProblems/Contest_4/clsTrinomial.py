import math
class Trinomial:
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b
        self.completeSquare()

    def completeSquare(self):
        self.c = int((self.b / (2 * self.a)) ** 2)
        self.factor = int(math.sqrt(self.c)) if self.b >= 0 else int(-math.sqrt(self.c))
        return

    def __str__(self):
        return self.printTrinomialForm()

    def toStringForm(self, number):
        if number >= 0:
            numStr = " + " + str(number)
        else:
            numStr = " - " + str(0-number)
        return numStr

    def printCoefficiantAWrapper(self, internalForm):
        return "%s%s%s" % (str(self.a) + "(" if self.a > 1 else "", internalForm, (")" if self.a > 1 else ""))

    def printInternalTrinomialForm(self):
        return "x^2%sx%s" % (self.toStringForm(int(self.b/self.a)), self.toStringForm(self.c))

    def printTrinomialForm(self):
        return self.printCoefficiantAWrapper(self.printInternalTrinomialForm())

    def printPerfectSquareForm(self):
        return (str(self.a) if self.a > 1 else "") + "(" + "x" + self.toStringForm(self.factor) + ")^2"

    def hasPerfectSquare(self):
        pass
