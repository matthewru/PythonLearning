from clsTrinomial import Trinomial
class Ellipse:

    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.completeSquare()

    def isCircle(self):
        if self.a == self.c:
            return True
        else:
            return False

    def isEllipse(self):
        if self.a == self.c:
            return False
        else:
            return True

    def completeSquare(self):
        self.xTrinomial = Trinomial(self.a, self.d)
        self.yTrinomial = Trinomial(self.c, self.e)
        self.constant = -(self.f) + self.xTrinomial.c + self.yTrinomial.c
        # In completeSquare
        # 3.1 create X trinomial
        #  xTrinomial = Trinomial(a, b, c)
        #  xTrinomial.completeSquare()
        #  update constant => constant += xTrinomial.c
        # 3.2 create Y trinomial
        #  yTrinomial = Trinomial(a, b, c)
        #  yTrinomial.completeSquare()
        #  update constant => constant += yTrinomial.c

    #def toStringForm(self, number):
        #if number >= 0:
           # numStr = " + " + str(number)
        #else:
            #numStr = " - " + str(0-number)
       # return numStr

    def printCoefficient(self, coefficient):
        if coefficient == 1:
            numStr = " + "
        elif coefficient == -1:
            numStr = " - "
        elif coefficient == 0:
            return ""
        else:
            if coefficient > 0:
                numStr = " + " + str(coefficient)
            else:
                numStr = " - " + str(0 - coefficient)
        return numStr

    def printFirstCoefficient(self, coefficient):
        if coefficient == 1:
            numStr = ""
        elif coefficient == -1:
            numStr = "-"
        else:
            if coefficient >= 0:
                numStr = "" + str(coefficient)
            else:
                numStr = "-" + str(0 - coefficient)
        return numStr

    def perfectSquareForm(self):
        xPSForm = self.xTrinomial.printPerfectSquareForm()
        yPSForm = self.yTrinomial.printPerfectSquareForm()
        return "%s + %s = %s" % (xPSForm, yPSForm, str(self.constant))

    def standardForm(self):
        xPSForm = self.xTrinomial.printInternalPerfectSquareForm()
        yPSForm = self.yTrinomial.printInternalPerfectSquareForm()
        return "(%s)/%s + (%s)/%s = 1" % (xPSForm, int(self.constant/self.xTrinomial.a), yPSForm, int(self.constant/self.yTrinomial.a))

    def generalForm(self):
        return (self.printFirstCoefficient(self.a) + "x^2" if self.a != 0 else "") + \
               (self.printCoefficient(self.b) + "xy" if self.b != 0 else "") + \
               (self.printCoefficient(self.c) + "y^2" if self.c != 0 else "") + \
               (self.printCoefficient(self.d) + "x" if self.d != 0 else "") + \
               (self.printCoefficient(self.e) + "y" if self.e != 0 else "") + \
               (self.printCoefficient(self.f) if self.d != 0 else "") + \
               " = 0"

    def __str__(self):
        return self.generalForm()

    def getMajorAxis(self):
        # if it is circle return getMajorAxis/2
        pass

# Attributes a, b, c, d, e, f, xTrinomial, yTrinomial, Constant


# functions
# 1. isCircle
# 2. isEllipse
# 3. completeSquare()



# 7. getMajorAxis()
# 4. perfectSquareForm()
# 5. standardForm()
# 6. _str()
