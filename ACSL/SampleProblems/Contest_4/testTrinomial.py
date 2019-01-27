from clsTrinomial import Trinomial


def testTrinomial(a, b):
    trinomial = Trinomial(a, b)
    print("Trinomial form: %s" % trinomial.printTrinomialForm())
    print("Perfect Square form: %s" % trinomial.printPerfectSquareForm())
    print("__str__: %s" % trinomial)


testTrinomial(1, 4)
testTrinomial(-1, 4)
testTrinomial(1, -4)
testTrinomial(-1, -4)
testTrinomial(4, 16)
testTrinomial(-4, 16)
testTrinomial(4, -16)
testTrinomial(-4, -16)
testTrinomial(1, 6)
testTrinomial(-1, 6)
testTrinomial(1, -6)
testTrinomial(-1, -6)
