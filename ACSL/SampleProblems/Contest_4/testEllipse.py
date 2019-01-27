from clsEllipse import Ellipse


def testEllipse(a, b, c, d, e, f):
    ellipse = Ellipse(a, b, c, d, e, f)
    origX, origY = ellipse.getCenter()
    print("General form: %s" % ellipse.generalForm())
    print("Perfect Square form: %s" % ellipse.perfectSquareForm())
    print("Standard form: %s" % ellipse.standardForm())
    print("__str__: %s" % ellipse)
    print("Circle or Not: %s" % ellipse.isCircle())
    print("Center: (%d, %d)" % (origX, origY))
    print("Major Axis: %d" % ellipse.getMajorAxis())


testEllipse(1, 0, 1, 4, -6, -3)
testEllipse(1, 0, 4, -6, -16, -11)
testEllipse(2, 0, 2, 8, 12, -6)
testEllipse(1, 0, 1, -2, -6, -26)
testEllipse(9, 0, 16, -72, 64, 64)
testEllipse(16, 0, 16, 0, 0, -64)
testEllipse(9, 0, 4, 0, 0, -144)
testEllipse(3, 0, 27, -18, 0, -216)
