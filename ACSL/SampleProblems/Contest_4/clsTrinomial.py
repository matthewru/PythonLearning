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

    def printTrinomialForm(self):
        if self.factor > 0:
            if self.a > 0:
                return str(self.a) + "(" + "x^2" + " " + "+" + " " + str(int(self.b/self.a)) + "x" + " " + "+" + " " + str(self.c) + ")"
            else:
                return (str(self.a) if self.a > 1 else "") + "x^2" + " " + "+" + " " + str(self.b) + "x" + " " + "+" + " " + str(self.c)

        else:
            if self.a > 0:
                return str(self.a) + "(" + "x^2" + " " + "-" + " " + str(-(int(self.b/self.a))) + "x" + " " + "+" + " " + str(self.c) + ")"
            else:
                return (self.a if self.a > 1 else "") + "x^2" + " " + "-" + " " + str(-self.b) + "x" + " " + "+" + " " + str(self.c)

    def printPerfectSquareForm(self):
        if self.factor > 0:
            return "(" + "x" + " " + "+" + " " + str(self.factor) + ")^2"
        else:
            return "(" + "x" + " " + "-" + " " + str(-(self.factor)) + ")^2"

    def hasPerfectSquare(self):
        pass