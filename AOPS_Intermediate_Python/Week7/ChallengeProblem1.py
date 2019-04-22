# Python Class 1889
# Lesson 7 Problem 1
# Author: madmathninja (272729)

import turtle
import random

# handlers
def forward():
    tRed.forward(random.randint(1, 51))
    tBlue.forward(random.randint(1, 51))
    tGreen.forward(random.randint(1, 51))

def turn_right():
    tRed.right(15)
    tBlue.right(30)
    tGreen.right(40)

def turn_left():
    tRed.left(15)
    tBlue.left(30)
    tGreen.left(40)


# set up window and turtles
wn = turtle.Screen()
tRed = turtle.Turtle()
tRed.color('red')
tBlue = turtle.Turtle()
tBlue.color('blue')
tGreen = turtle.Turtle()
tGreen.color('green')

# listeners
wn.onkey(forward, "Up")
wn.onkey(turn_right, "Right")
wn.onkey(turn_left, "Left")

# listen and run
wn.listen()
wn.mainloop()