# Python Class 1889
# Lesson 7 Problem 2
# Author: madmathninja (272729)

import turtle

def teleport_and_draw(x,y):
    carol.pendown()
    carol.goto(x, y)

def teleport_and_no_draw(x,y):
    carol.penup()
    carol.goto(x, y)


# set up window and TT
wn = turtle.Screen()
carol = turtle.Turtle()

# listeners to teleport
wn.onclick(teleport_and_draw,1)    # left click
wn.onclick(teleport_and_no_draw,3) # right click

# turn on the listeners and run
wn.listen()
wn.mainloop()