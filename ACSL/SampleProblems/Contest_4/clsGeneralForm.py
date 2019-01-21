from clsTrinomial import Trinomial
class GeneralForm:

    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

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
        xTrinomial = Trinomial(self.a, self.b, self.c)

        # In completeSquare
        # 3.1 create X trinomial
        #  xTrinomial = Trinomial(a, b, c)
        #  xTrinomial.completeSquare()
        #  update constant => constant += xTrinomial.c
        # 3.2 create Y trinomial
        #  yTrinomial = Trinomial(a, b, c)
        #  yTrinomial.completeSquare()
        #  update constant => constant += yTrinomial.c
        pass

    def perfectSquareForm(self):
        pass

    def standardForm(self):
        pass

    def __str__(self):
        pass

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
