import turtle


class colorfulTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.red = 0
        self.green = 0
        self.blue = 0
        self.gap = 1
        self.color((self.red, self.green, self.blue))
        self.shape('square')
        self.shapesize(5, 5, 12)
        self.getscreen().onkey(self.increase_gap, "Up")
        self.getscreen().onkey(self.decrease_gap, "Down")
        self.getscreen().onkey(self.darker_shade, "Right")
        self.getscreen().onkey(self.lighter_shade, "Left")
        self.getscreen().onkey(self.redder_shade, "r")
        self.getscreen().onkey(self.greener_shade, "g")
        self.getscreen().onkey(self.bluer_shade, "b")
        self.getscreen().onkey(self.less_red_shade, "e")
        self.getscreen().onkey(self.less_green_shade, "f")
        self.getscreen().onkey(self.less_blue_shade, "v")

    def increase_gap(self):
        self.gap += 1

    def decrease_gap(self):
        self.gap -= 1

    def darker_shade(self):
        self.red -= self.gap
        self.green -= self.gap
        self.blue -= self.gap
        for count in range(3):
            if self.red < 0:
                self.red = 0
            elif self.green < 0:
                self.green = 0
            elif self.blue < 0:
                self.blue = 0
        self.color((self.red, self.green, self.blue))

    def lighter_shade(self):
        self.red += self.gap
        self.green += self.gap
        self.blue += self.gap
        for count in range(3):
            if self.red > 255:
                self.red = 255
            elif self.green > 255:
                self.green = 255
            elif self.blue > 255:
                self.blue = 255
        self.color((self.red, self.green, self.blue))

    def redder_shade(self):
        self.red += self.gap
        if self.red > 255:
            self.red = 255
        self.color((self.red, self.green, self.blue))

    def bluer_shade(self):
        self.blue += self.gap
        if self.blue > 255:
            self.blue = 255
        self.color((self.red, self.green, self.blue))

    def greener_shade(self):
        self.green += self.gap
        if self.green > 255:
            self.green = 255
        self.color((self.red, self.green, self.blue))

    def less_red_shade(self):
        self.red -= self.gap
        if self.red < 0:
            self.red = 0
        self.color((self.red, self.green, self.blue))

    def less_green_shade(self):
        self.green -= self.gap
        if self.green < 0:
            self.green = 0
        self.color((self.red, self.green, self.blue))

    def less_blue_shade(self):
        self.blue -= self.gap
        if self.blue < 0:
            self.blue = 0
        self.color((self.red, self.green, self.blue))


wn = turtle.Screen()
wn.colormode(255)
wilma = colorfulTurtle()
wn.listen()
wn.mainloop()