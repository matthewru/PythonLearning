import turtle
circ = turtle.Pen()
radius = 25
distance = 100
circ.circle(radius)
circ.penup()
circ.forward(distance)
circ.pendown()
circ.circle(radius * 2)
circ.penup()
circ.forward(distance + 100)
circ.pendown()
circ.circle(radius * 4)
