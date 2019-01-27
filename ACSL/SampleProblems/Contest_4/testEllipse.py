from clsEllipse import Ellipse


def testEllipse(a, b, c, d, e, f):
    ellipse = Ellipse(a, b, c, d, e, f)
    print("General form: %s" % ellipse.generalForm())
    print("Perfect Square form: %s" % ellipse.perfectSquareForm())
    print("Standard form: %s" % ellipse.standardForm())
    print("__str__: %s" % ellipse)


testEllipse(1, 0, 1, 4, -6, -3)
testEllipse(3, 0, 27, -18, 0, -216)
