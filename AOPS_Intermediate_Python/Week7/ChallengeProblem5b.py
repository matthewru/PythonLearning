# Python Class 1889
# Lesson 7 Problem 5 Part (b)
# Author: madmathninja (272729)

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed = 0
        self.getscreen().onkey(self.speed_up, "Up")
        self.getscreen().onkey(self.slow_down, "Down")
        self.getscreen().onkey(self.turn_left, "Left")
        self.getscreen().onkey(self.turn_right, "Right")
        self.getscreen().onkey(self.stop_turtle, "s")
        self.getscreen().onkey(self.close_window, "q")
        self.move()


    def move(self):
        self.forward(self.speed)
        self.getscreen().ontimer(self.move, 1000)

    def speed_up(self):
        self.speed += 25

    def slow_down(self):
        self.speed -= 25

    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)

    def stop_turtle(self):
        self.speed = 0

    def close_window(self):
        self.getscreen().bye()


wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()