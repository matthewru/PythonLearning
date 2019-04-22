import turtle
import random


class MisbehavingTurtle(turtle.Turtle):
    def left(self, degree):
        chance = 0.25
        if random.random() < chance:
            turtle.Turtle.right(self, degree)
        else:
            turtle.Turtle.left(self, degree)

    def right(self, degree):
        chance = 0.25
        if random.random() < chance:
            turtle.Turtle.left(self, degree)
        else:
            turtle.Turtle.right(self, degree)


# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)


# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)
spice = MisbehavingTurtle()
spice.color('red')
drawing_test(spice)
wn.mainloop()