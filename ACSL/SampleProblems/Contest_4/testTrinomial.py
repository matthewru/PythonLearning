from clsTrinomial import Trinomial


def testTrinomial(a, b):
    trinomial = Trinomial(a, b)
    print("Trinomial form: %s" % trinomial.printTrinomialForm())
    print("Perfect Square form: %s" % trinomial.printPerfectSquareForm())
    print("__str__: %s" % trinomial)


testTrinomial(5, 50)

