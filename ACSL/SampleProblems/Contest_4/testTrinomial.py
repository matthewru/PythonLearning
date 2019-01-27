from clsTrinomial import Trinomial

trinomial = Trinomial(1, 4)
print("Trinomial form: %s" % trinomial.printTrinomialForm())
print("Perfect Square form: %s" % trinomial.printPerfectSquareForm())
print("__str__: %s" % trinomial)

trinomial = Trinomial(1, -6)
print("Trinomial form: %s" % trinomial.printTrinomialForm())
print("Perfect Square form: %s" % trinomial.printPerfectSquareForm())
print("__str__: %s" % trinomial)

trinomial = Trinomial(3, -6)
print("Trinomial form: %s" % trinomial.printTrinomialForm())
print("Perfect Square form: %s" % trinomial.printPerfectSquareForm())
print("__str__: %s" % trinomial)